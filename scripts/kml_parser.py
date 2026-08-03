import xml.etree.ElementTree as ET
import math
import json
import os
import sys

def haversine(lat1, lon1, lat2, lon2):
    """Calculate distance in meters between two lat/lon points."""
    R = 6371000  # Earth radius in meters
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1-a))

def polygon_area_m2(coords):
    """Calculate area of a polygon given list of (lon, lat) using shoelace formula projected to meters.
    Uses equidistant approximation for small areas."""
    if len(coords) < 3:
        return 0
    # Convert to local meter coordinates using first point as origin
    lat0, lon0 = coords[0][1], coords[0][0]
    xs = []
    ys = []
    for lon, lat in coords:
        x = haversine(lat0, lon0, lat0, lon)
        y = haversine(lat0, lon0, lat, lon0)
        if lon < lon0:
            x = -x
        if lat < lat0:
            y = -y
        xs.append(x)
        ys.append(y)
    # Shoelace formula
    n = len(xs)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += xs[i] * ys[j]
        area -= xs[j] * ys[i]
    return abs(area) / 2.0

def centroid(coords):
    """Calculate centroid of polygon."""
    n = len(coords)
    cx = sum(c[0] for c in coords) / n
    cy = sum(c[1] for c in coords) / n
    return cx, cy

def parse_kml(filepath):
    """Parse a KML file and extract site data."""
    tree = ET.parse(filepath)
    root = tree.getroot()
    ns = {'kml': 'http://www.opengis.net/kml/2.2'}
    
    result = {
        'buildings': [],
        'fences': [],
        'boundaries': [],
        'streets': [],
        'points': [],
        'site_area_m2': 0,
        'building_area_total_m2': 0,
    }
    
    for pm in root.iter('{http://www.opengis.net/kml/2.2}Placemark'):
        name_el = pm.find('kml:name', ns)
        name = name_el.text if name_el is not None else ''
        desc_el = pm.find('kml:description', ns)
        desc = desc_el.text if desc_el is not None else ''
        
        # Parse Polygon
        for poly in pm.iter('{http://www.opengis.net/kml/2.2}Polygon'):
            coords_raw = []
            for coord_el in poly.iter('{http://www.opengis.net/kml/2.2}coordinates'):
                for coord_str in coord_el.text.strip().split():
                    parts = coord_str.split(',')
                    if len(parts) >= 2:
                        coords_raw.append((float(parts[0]), float(parts[1]), float(parts[2]) if len(parts) > 2 else 0))
            
            if coords_raw:
                area = polygon_area_m2([(c[0], c[1]) for c in coords_raw])
                cx, cy = centroid([(c[0], c[1]) for c in coords_raw])
                elevations = [c[2] for c in coords_raw if c[2] != 0]
                
                feature = {
                    'name': name,
                    'description': desc,
                    'coordinates': [(c[0], c[1], c[2]) for c in coords_raw],
                    'area_m2': round(area, 1),
                    'centroid_lon': cx,
                    'centroid_lat': cy,
                    'elevations': elevations,
                    'avg_elevation': round(sum(elevations)/len(elevations), 1) if elevations else 0,
                }
                
                desc_upper = desc.upper()
                if 'FENCE' in desc_upper:
                    result['fences'].append(feature)
                    result['site_area_m2'] = area  # Fence = site boundary
                elif 'BUILDING' in desc_upper:
                    result['buildings'].append(feature)
                    result['building_area_total_m2'] += area
                else:
                    result['boundaries'].append(feature)
        
        # Parse LineString
        for ls in pm.iter('{http://www.opengis.net/kml/2.2}LineString'):
            coords_raw = []
            for coord_el in ls.iter('{http://www.opengis.net/kml/2.2}coordinates'):
                for coord_str in coord_el.text.strip().split():
                    parts = coord_str.split(',')
                    if len(parts) >= 2:
                        coords_raw.append((float(parts[0]), float(parts[1]), float(parts[2]) if len(parts) > 2 else 0))
            
            if coords_raw:
                total_length = 0
                for i in range(len(coords_raw)-1):
                    total_length += haversine(coords_raw[i][1], coords_raw[i][0], 
                                              coords_raw[i+1][1], coords_raw[i+1][0])
                
                line_feature = {
                    'name': name,
                    'description': desc,
                    'coordinates': [(c[0], c[1], c[2]) for c in coords_raw],
                    'length_m': round(total_length, 1),
                }
                
                desc_upper = desc.upper()
                if 'ROAD' in desc_upper or 'STREET' in desc_upper:
                    result['streets'].append(line_feature)
                else:
                    result['streets'].append(line_feature)  # Treat all lines as streets/paths
        
        # Parse Point
        for pt in pm.iter('{http://www.opengis.net/kml/2.2}Point'):
            for coord_el in pt.iter('{http://www.opengis.net/kml/2.2}coordinates'):
                parts = coord_el.text.strip().split(',')
                if len(parts) >= 2:
                    result['points'].append({
                        'name': name,
                        'description': desc,
                        'lon': float(parts[0]),
                        'lat': float(parts[1]),
                        'elevation': float(parts[2]) if len(parts) > 2 else 0,
                    })
    
    # Calculate available open space
    result['open_space_m2'] = max(0, result['site_area_m2'] - result['building_area_total_m2'])
    result['site_area_m2'] = round(result['site_area_m2'], 1)
    result['open_space_m2'] = round(result['open_space_m2'], 1)
    result['building_area_total_m2'] = round(result['building_area_total_m2'], 1)
    
    return result

def main():
    base_dir = '/home/z/my-project/upload/sites'
    schools = {
        'assosa-priprimary': 'Assosa Preprimary (School 3)',
        'Benishangul': 'Benishan Gulgumuz (School 5)',
        'selamber': 'Selamber (School 6)',
        'assos primary': 'Assosa Primary & Middle (School 4)',
        'Dareselam': 'Daresalam (School 2)',
        'Gemeharu': 'Gemeharu (School 1)',
    }
    
    all_results = {}
    for folder, school_name in schools.items():
        kml_path = os.path.join(base_dir, folder, 'site plan.kml')
        if os.path.exists(kml_path):
            print(f"\n{'='*60}")
            print(f"SCHOOL: {school_name}")
            print(f"{'='*60}")
            
            data = parse_kml(kml_path)
            all_results[folder] = data
            
            print(f"Site Area (Fence): {data['site_area_m2']} m2")
            print(f"Total Building Footprint: {data['building_area_total_m2']} m2")
            print(f"Available Open Space: {data['open_space_m2']} m2")
            print(f"Number of Buildings: {len(data['buildings'])}")
            print(f"Number of Fences/Boundaries: {len(data['fences'])}")
            print(f"Number of Lines (streets/paths): {len(data['streets'])}")
            print(f"Number of Points: {len(data['points'])}")
            
            for i, b in enumerate(data['buildings']):
                print(f"  Building {i+1}: {b['area_m2']} m2, centroid=({b['centroid_lon']:.6f}, {b['centroid_lat']:.6f})")
            
            for i, f in enumerate(data['fences']):
                print(f"  Fence {i+1}: {f['area_m2']} m2, {len(f['coordinates'])} vertices")
                if f.get('elevations'):
                    print(f"    Elevations: {f['elevations']}")
    
    # Save to JSON for later use
    output_path = '/home/z/my-project/scripts/kml_parsed_data.json'
    with open(output_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nParsed data saved to: {output_path}")

if __name__ == '__main__':
    main()