#!/usr/bin/env python3
"""SUIDAC Coordinate Utilities — Haversine distance, geodesic area, centroid helpers."""

import math

R_EARTH = 6_371_000  # metres


def haversine(lat1, lon1, lat2, lon2):
    """Return distance in metres between two WGS-84 points."""
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2
         + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))
         * math.sin(dlon / 2) ** 2)
    return R_EARTH * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def polygon_area_m2(coords):
    """Geodesic area (m²) from list of [(lat, lon), ...] using Shoelace on projected coords.
    Accurate for small polygons (< 1 km²) at tropical latitudes.
    """
    if len(coords) < 3:
        return 0.0
    ref_lat, ref_lon = coords[0]
    x0 = math.radians(ref_lon) * R_EARTH * math.cos(math.radians(ref_lat))
    y0 = math.radians(ref_lat) * R_EARTH
    projected = []
    for lat, lon in coords:
        x = math.radians(lon) * R_EARTH * math.cos(math.radians(ref_lat)) - x0
        y = math.radians(lat) * R_EARTH - y0
        projected.append((x, y))
    n = len(projected)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += projected[i][0] * projected[j][1]
        area -= projected[j][0] * projected[i][1]
    return abs(area) / 2.0


def centroid(coords):
    """Return (lat, lon) centroid of a polygon."""
    n = len(coords)
    lat = sum(c[0] for c in coords) / n
    lon = sum(c[1] for c in coords) / n
    return lat, lon


def wgs84_to_local(coords, ref=None):
    """Convert [(lat, lon), ...] to local metres relative to ref point (or first coord).
    Returns [(x, y), ...] in metres — suitable for AutoCAD insertion at 1:1.
    """
    if ref is None:
        ref = coords[0]
    ref_lat, ref_lon = ref
    result = []
    for lat, lon in coords:
        x = haversine(ref_lat, ref_lon, ref_lat, lon)
        y = haversine(ref_lat, ref_lon, lat, ref_lon)
        if lon < ref_lon:
            x = -x
        if lat < ref_lat:
            y = -y
        result.append((round(x, 3), round(y, 3)))
    return result


if __name__ == "__main__":
    # Quick self-test
    test = [(10.0625, 34.5388), (10.0625, 34.5390), (10.0624, 34.5390), (10.0624, 34.5388)]
    print(f"Area: {polygon_area_m2(test):.1f} m²")
    print(f"Centroid: {centroid(test)}")
    print(f"Local coords: {wgs84_to_local(test)}")
