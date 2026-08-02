# IRC SUIDAC — Assosa City Playground Design

> **Client:** International Rescue Committee (IRC) — Ethiopia Mission  
> **Funder:** Cities Alliance (CA)  
> **Location:** Assosa City, Benishangul-Gumuz Regional State, Ethiopia  
> **Elevation:** ~1,500 m ASL  
> **Climate:** Tropical savanna; wet season Apr–Oct (~1,200 mm/yr), dry season Nov–Mar  
> **Design Phase:** Phases 1–3 (Site Analysis → Concept Design → Detailed Design)  
> **Age Group:** Pre-primary children, 5–6 years  

---

## 1. Project Overview

This repository contains the full landscape architecture and playground design package for **six (6) pre-primary schools** in Assosa City, developed under the IRC **SUIDAC** (Safe Urban Infrastructure Design for African Cities) programme. The project delivers construction-ready design proposals for child-safe, community-maintainable play spaces using locally sourced materials and a mix of procured metal equipment (E1–E4) and locally constructed elements (L1–L4).

### Schools Inventory

| # | School Name | Students (M/F) | Total | Selected Option |
|---|-------------|----------------|-------|-----------------|
| S1 | Gemeharu Primary & Midlevel | 25 / 43 | 68 | Option B (Phased) |
| S2 | Daresalam Primary & Midlevel | 40 / 45 | 85 | Option B (Phased) |
| S3 | Assosa Preprimary | 78 / 56 | 134 | Option A (Full) |
| S4 | Assosa Primary & Middle | 124 / 106 | 230 | Option A (Full) |
| S5 | Benishan Gulgumuz Primary & Middle | 65 / 59 | 124 | Option A (Full) |
| S6 | Selamber Primary School | 30 / 38 | 68 | Option B (Phased) |

> **Option selection rule:** Schools with >100 students receive Option A (maximum play value); schools with ≤100 students receive Option B (minimum viable / phased implementation).

---

## 2. Repository Structure

```
AKGS-Landscape/
│
├── README.md                          ← YOU ARE HERE
├── .gitignore
│
├── 00_project-admin/
│   ├── SUIDAC_AI_Agent_Master_Command.md    ← Master design protocol & guidelines
│   ├── meeting-notes/
│   │   └── YYYY-MM-DD_topic.md
│   ├── correspondence/
│   │   └── IRC_CitiesAlliance_designbrief_v01.pdf
│   └── contracts/
│       └── TBD
│
├── 01_survey-data/
│   ├── kml/
│   │   ├── S1_Gemeharu_siteplan.kml
│   │   ├── S2_Daresalam_siteplan.kml
│   │   ├── S3_AssosaPreprimary_siteplan.kml
│   │   ├── S4_AssosaPrimaryMiddle_siteplan.kml
│   │   ├── S5_BenishanGulgumuz_siteplan.kml
│   │   └── S6_Selamber_siteplan.kml
│   ├── georeferenced-imagery/
│   │   ├── S1_Gemeharu_existingconditions.png
│   │   ├── S2_Daresalam_existingconditions.png
│   │   ├── S3_AssosaPreprimary_existingconditions.png
│   │   ├── S4_AssosaPrimaryMiddle_existingconditions.png
│   │   ├── S5_BenishanGulgumuz_existingconditions.png
│   │   └── S6_Selamber_existingconditions.png
│   ├── field-photos/
│   │   └── .gitkeep          ← Placeholder for future site-visit photos
│   └── parsed-data/
│       └── kml_parsed_data.json   ← Machine-extracted site metrics (areas, centroids)
│
├── 02_design-reports/
│   ├── SUIDAC_Master_Summary_6_Schools.pdf  ← Cross-school summary report
│   ├── S1_Gemeharu_Design.pdf
│   ├── S2_Daresalam_Design.pdf
│   ├── S3_Assosa_Preprimary_Design.pdf
│   ├── S4_Assosa_Primary_Middle_Design.pdf
│   ├── S5_Benishan_Gulgumuz_Design.pdf
│   └── S6_Selamber_Design.pdf
│
├── 03_cad/
│   ├── _xrefs/
│   │   └── SUIDAC_titleblock.dwg      ← Reusable title block / sheet template
│   ├── _templates/
│   │   ├── SUIDAC_baseplan_template.dwg   ← Pre-configured layers, styles, scales
│   │   └── SUIDAC_hatch_patterns.pat      ← Custom hatches (sand, gravel, grass, phased)
│   ├── S1_Gemeharu/
│   │   ├── S1_001_baseplan.dwg
│   │   ├── S1_002_siteanalysis.dwg
│   │   ├── S1_003_concept_optA.dwg
│   │   ├── S1_003_concept_optB.dwg
│   │   ├── S1_004_masterlayout.dwg
│   │   ├── S1_005_equipment_layout.dwg
│   │   ├── S1_006_grading_drainage.dwg
│   │   ├── S1_007_planting.dwg
│   │   └── S1_008_detail_sections.dwg
│   ├── S2_Daresalam/
│   │   └── ...  (same drawing set)
│   ├── S3_AssosaPreprimary/
│   │   └── ...
│   ├── S4_AssosaPrimaryMiddle/
│   │   └── ...
│   ├── S5_BenishanGulgumuz/
│   │   └── ...
│   └── S6_Selamber/
│       └── ...
│
├── 04_schedules/
│   ├── equipment_schedule_master.xlsx     ← Consolidated procurement across all schools
│   ├── planting_schedule_master.xlsx      ← Consolidated plant list across all schools
│   ├── S1_Gemeharu/
│   │   ├── S1_equipment_schedule.xlsx
│   │   ├── S1_surface_schedule.xlsx
│   │   ├── S1_planting_schedule.xlsx
│   │   └── S1_earthwork_summary.xlsx
│   ├── S2_Daresalam/
│   │   └── ...
│   ├── S3_AssosaPreprimary/
│   │   └── ...
│   ├── S4_AssosaPrimaryMiddle/
│   │   └── ...
│   ├── S5_BenishanGulgumuz/
│   │   └── ...
│   └── S6_Selamber/
│       └── ...
│
├── 05_boq/
│   ├── BOQ_master_consolidated.xlsx        ← All 6 schools, summable for procurement
│   ├── S1_Gemeharu_BOQ.xlsx
│   ├── S2_Daresalam_BOQ.xlsx
│   ├── S3_AssosaPreprimary_BOQ.xlsx
│   ├── S4_AssosaPrimaryMiddle_BOQ.xlsx
│   ├── S5_BenishanGulgumuz_BOQ.xlsx
│   └── S6_Selamber_BOQ.xlsx
│
├── 06_construction/
│   ├── specifications/
│   │   ├── earthworks_spec.md              ← Clearance, grading, compaction (95% modified Proctor)
│   │   ├── surfacing_spec.md               ← Sand, gravel, grass, mulch depths & sources
│   │   ├── equipment_installation_spec.md  ← Footing sizes, anchor bolts, anti-corrosion
│   │   ├── timber_treatment_spec.md        ← Anti-termite (boron-based, 24-hr soak)
│   │   └── drainage_spec.md                ← 1% min slope, swale dimensions
│   ├── details/
│   │   ├── DWG_footing_detail_300x300x400.dwg
│   │   ├── DWG_sand_pit_edge_detail.dwg
│   │   ├── DWG_fence_setback_detail.dwg
│   │   └── DWG_drainage_swale_section.dwg
│   └── safety_checklists/
│       ├── S1_Gemeharu_safety_checklist.pdf
│       ├── S2_Daresalam_safety_checklist.pdf
│       ├── S3_AssosaPreprimary_safety_checklist.pdf
│       ├── S4_AssosaPrimaryMiddle_safety_checklist.pdf
│       ├── S5_BenishanGulgumuz_safety_checklist.pdf
│       └── S6_Selamber_safety_checklist.pdf
│
├── 07_output-plots/
│   ├── A1/
│   │   └── ...  (full-size plots for printing)
│   ├── A3/
│   │   └── ...  (reduced plots for review)
│   └── PDF_sets/
│       └── SUIDAC_full_drawing_set_combined.pdf  ← All schools, all sheets
│
└── scripts/
    ├── kml_parser.py                   ← KML → JSON extraction utility
    └── coordinate_utils.py             ← Haversine, Shoelace, centroid helpers
```

---

## 3. Filename Standards

### 3.1 Drawing Numbering Convention

```
<SchoolCode>_<SequentialNumber>_<DrawingType>_<Variant>.dwg
```

| Field | Format | Example | Description |
|-------|--------|---------|-------------|
| SchoolCode | `S1` – `S6` | `S3` | School identifier (see inventory table) |
| SeqNumber | `001` – `999` | `004` | Drawing sequence (controls sheet order in plot sets) |
| DrawingType | lowercase, underscored | `masterlayout` | Descriptive name (see approved list below) |
| Variant | optional suffix | `_optA`, `_optB`, `_rev01` | Concept variants or revision identifiers |

### 3.2 Approved Drawing Type Names

| Code | Sheet Title | Typical Scale | Content |
|------|-------------|---------------|---------|
| `baseplan` | Base Plan | 1:500 | Boundary, buildings, trees, fences from KML/field survey |
| `siteanalysis` | Site Analysis | 1:500 | Constraint zones (red/yellow/green/blue), sun path, drainage arrows |
| `concept_optA` | Concept Option A | 1:200 / 1:500 | Maximum play value layout |
| `concept_optB` | Concept Option B | 1:200 / 1:500 | Minimum viable / phased layout |
| `masterlayout` | Master Layout Plan | 1:200 | Selected option, fully dimensioned, with all zones labeled |
| `equipment_layout` | Equipment Layout | 1:100 / 1:200 | Enlarged equipment placement with safety zones, surface extents |
| `grading_drainage` | Grading & Drainage | 1:200 | Spot elevations, slopes, swales, drainage direction arrows |
| `planting` | Planting Plan | 1:200 | Existing trees (preserve), new trees, ground cover zones |
| `detail_sections` | Details & Sections | 1:20 / 1:50 | Footing details, edge details, surface cross-sections |
| `setting_out` | Setting-Out Plan | 1:100 | Coordinates/dimensions from two fixed site datum points for construction |

### 3.3 Schedule & Document Naming

```
<SchoolCode>_<ScheduleType>.xlsx
<SchoolCode>_BOQ.xlsx
BOQ_master_consolidated.xlsx
<SchoolCode>_safety_checklist.pdf
```

**Approved ScheduleType values:** `equipment_schedule`, `surface_schedule`, `planting_schedule`, `earthwork_summary`

### 3.4 Revision Control

- Initial issue: no suffix (e.g., `S3_004_masterlayout.dwg`)
- Revisions: append `_rev<NN>` (e.g., `S3_004_masterlayout_rev01.dwg`)
- Superseded drawings move to `_archive/` subfolder — never delete
- Plot PDFs follow drawing name: `S3_004_masterlayout.pdf`

### 3.5 Layer Naming Convention (AutoCAD)

```
<SchoolCode>-<Discipline>-<Element>-<Status>
```

| Component | Values |
|-----------|--------|
| SchoolCode | `S1`, `S2`, … `S6` |
| Discipline | `SURV` (survey), `ARCH` (existing buildings), `PLAY` (playground), `PLNT` (planting), `CIVL` (grading/drainage), `ANNO` (annotations) |
| Element | `BOUNDARY`, `BLDG`, `FENCE`, `TREE`, `EQUIP`, `SANDEDGE`, `PATH`, `SWALE`, `DIM`, `TEXT`, `HATCH` |
| Status | `EXIST`, `PROP` (proposed), `DEMO` (demolition), `FUTR` (future phase) |

**Examples:**
- `S3-SURV-BOUNDARY-EXIST` — Existing site boundary from KML
- `S3-PLAY-EQUIP-PROP` — Proposed playground equipment
- `S3-ARCH-BLDG-EXIST` — Existing classroom building
- `S3-PLAY-SANDEDGE-PROP` — Proposed sand safety surface edge
- `S3-PLNT-TREE-FUTR` — Future phase planting

### 3.6 Color & Lineweight Standards

| Layer Type | Color (ACI) | Lineweight | Linetype |
|------------|-------------|------------|----------|
| Existing buildings | 8 (Grey) | 0.18 mm | Continuous |
| Existing trees (preserve) | 3 (Green) | 0.25 mm | Continuous |
| Proposed equipment | 1 (Red) | 0.35 mm | Continuous |
| Safety zones / fall areas | 30 (Orange) | 0.13 mm | Dashed |
| Surface hatching | 41 (Tan) | 0.09 mm | Continuous |
| Proposed planting | 93 (Light Green) | 0.18 mm | Continuous |
| Grading / contours | 9 (Cyan) | 0.13 mm | Continuous |
| Dimensions | 2 (Yellow) | 0.13 mm | Continuous |
| Annotation text | 7 (White) | 0.13 mm | Continuous |
| Phase 2 / Future | 252 (Light Grey) | 0.09 mm | Dashed |
| Boundary / fence | 30 (Orange) | 0.18 mm | Continuous |

---

## 4. Key Design Rules (from SUIDAC Guidelines)

### 4.1 Spatial Zoning Rules

| Rule | Requirement | Rationale |
|------|-------------|-----------|
| Fall zone (moving equip.) | **2.0 m** clear radius from edge of all swings, see-saws, merry-go-rounds | Impact attenuation per child-safety standard |
| Building setback (general) | **1.5 m** minimum from wall/fence to any equipment edge | Maintenance access & dust control |
| Building setback (swing/slide) | **3.0 m** minimum from building wall to swing frame or slide platform | Extended runout safety |
| Pathway width | **1.2 m** minimum (wheelchair-accessible where possible) | IRC accessibility requirement |
| Active play zone area | **80 m² per 50 students** (scale proportionally) | Ensures adequate play space per child |
| Quiet / shade zone | **≥ 20%** of total play area | Rest & sun protection |
| Future development zone | Mark clearly with hatching — not ambiguous open space | Phased construction clarity |

### 4.2 Equipment Specifications

**Procured Metal (E-series):**

| ID | Equipment | Key Dimensions | Safety Zone |
|----|-----------|-----------------|--------------|
| E1 | Merry-Go-Round | Ø 2.3 m × H 1.0 m; RHS 40×20×1.5 mm | 2.0 m radius |
| E2 | See-Saw | L 4.0 m × H 1.0 m (fulcrum); RHS 40×40 mm | 2.0 m front/back (8 m × 3 m total) |
| E3 | Slide | W 3.0 m × H 2.0 m (legs); platform max 1.5 m | 2.0 m at base runout |
| E4 | Chain Swing | W 2.5 m × H 2.5 m; pipe 60×60×2 mm | 2.0 m all around |

**Locally Constructed (L-series):**

| ID | Element | Key Dimensions | Material |
|----|---------|-----------------|----------|
| L1 | Balance Beam | L 3.0–4.0 m, H 0.2–0.3 m, W 0.15–0.2 m | Treated bamboo (≥80 mm dia.) or hardwood |
| L2 | Climbing Structure | Max H 1.2 m | Treated bamboo poles (60–80 mm dia.) |
| L3 | Tunnel Crawl | Ø 0.6–0.8 m, L 2.0–3.0 m | Concrete culvert or corrugated metal pipe |
| L4 | Stepping Logs/Stones | Ø 0.15–0.2 m, H 0.1–0.15 m, spacing 0.3–0.4 m | Hardwood timber or local stone |

### 4.3 Surface Materials

| Zone | Material | Depth | Source |
|------|----------|-------|--------|
| Under moving equipment | Washed river sand | 150–200 mm | Local riverbed |
| Under slides (runout) | Washed river sand | 300 mm | Local riverbed |
| Pathways | Fine gravel (10–20 mm) | 100 mm compacted | Local quarry |
| General play lawn | Drought-tolerant grass | — | Transplant or seed |
| Tree protection ring | Stone mulch or tire mulch | 100 mm | Recycled / local stone |
| Drainage swale | Rubble / coarse gravel | 200 mm | Local quarry |

### 4.4 Climate & Environmental Constraints

- **Wet season:** April – October. All surfaces must drain within 24 hours.
- **Dry season:** November – March. Dust suppression required on bare areas.
- **Termite risk:** HIGH — all timber/bamboo requires boron-based treatment (24-hour minimum soak).
- **UV / corrosion:** All metal equipment requires zinc-chromate primer + enamel topcoat.
- **Soil:** Lateritic red soil, assumed CBR 5–10%.
- **Material sourcing radius:** All materials must be available within **50 km** of Assosa.

### 4.5 Banned Materials

- Synthetic turf
- Rubber tiles (unless recycled tire mulch)
- Imported specialty items
- Complex prefab structures
- Exotic invasive plant species

### 4.6 Construction Constraints

- All foundations achievable by manual labor + basic tools (no heavy machinery).
- Maximum concrete volume per footing: 0.05 m³ (hand-mixed C20).
- Installation crew: 4 unskilled laborers + 1 skilled metalworker.
- Drainage: gravity-based only (no pumps).
- Footing spec: minimum 300 × 300 × 400 mm per leg with anchor bolts.

---

## 5. To-Do Checklist — Next Design Steps (AutoCAD)

### Phase A: CAD Setup & Base Plans

- [ ] **A1.** Create `SUIDAC_titleblock.dwg` — ISO A1 / A3 title block with project logo, school name field, scale bar, north arrow, revision table.
- [ ] **A2.** Create `SUIDAC_baseplan_template.dwg` — Pre-configured with all standard layers (per Section 3.5), colors, lineweights (per Section 3.6), text styles, dimension styles, and hatch patterns.
- [ ] **A3.** Create `SUIDAC_hatch_patterns.pat` — Custom AutoCAD hatch patterns for: washed sand, compacted gravel, local grass, tire mulch, phased/future zone, and drainage swale rubble.
- [ ] **A4.** For each school, import KML boundary and building polygons into AutoCAD as closed polylines on `SURV-BOUNDARY-EXIST` and `ARCH-BLDG-EXIST` layers (use GIS import or coordinate-to-XY conversion at 1:500 scale).
- [ ] **A5.** For each school, draw fence lines on `SURV-FENCE-EXIST` from KML data or aerial imagery.
- [ ] **A6.** For each school, mark existing tree canopy circles on `PLNT-TREE-EXIST` (estimated 3–5 m radius) from aerial imagery interpretation and VLM analysis notes.
- [ ] **A7.** Add north arrow, scale bar (1:500), and coordinate grid to each base plan.
- [ ] **A8.** Plot-check each `baseplan` at A3 and A1 to verify legibility, layer visibility, and title block population.

### Phase B: Site Analysis Drawings

- [ ] **B1.** On each `siteanalysis` drawing, overlay constraint zones using closed polylines: Red (buildings + 3 m buffer), Orange (fence + 1.5 m buffer), Green (available play area), Blue (circulation paths).
- [ ] **B2.** Add sun path diagram (Assosa ~10°N latitude) showing approximate shadow patterns at 09:00, 12:00, and 15:00 for equinox conditions.
- [ ] **B3.** Add drainage direction arrows based on elevation data and assumed slope from KML coordinates.
- [ ] **B4.** Mark existing equipment to retain/repair/remove per the inventory in the Master Command document.
- [ ] **B5.** Annotate material sourcing notes (e.g., "River sand source: Blue Nile, ~8 km east").

### Phase C: Concept Design Drawings

- [ ] **C1.** For each school, draft `concept_optA` (full layout) and `concept_optB` (phased layout) on separate sheets using the Option A/B rules from the Master Command.
- [ ] **C2.** Place equipment blocks (E1–E4, L1–L4) at proposed positions with correct dimensions and orientations.
- [ ] **C3.** Draw 2.0 m safety zone circles around all moving equipment — verify no overlap with red/orange constraint zones.
- [ ] **C4.** Draw surface material zones (sand, gravel, grass) with appropriate hatching.
- [ ] **C5.** Verify supervision sight lines from building entrances (no blind corners).
- [ ] **C6.** Add dimension strings showing equipment spacing, setbacks, and zone widths.
- [ ] **C7.** Create legend with equipment symbols, zone colors, and hatching key.

### Phase D: Detailed Design Drawings

- [ ] **D1.** Finalize selected option per school as `masterlayout` at 1:200 — fully dimensioned with grid references.
- [ ] **D2.** Produce `equipment_layout` at 1:100 — enlarged view of each equipment cluster with safety zones, surface extents, and footing locations marked.
- [ ] **D3.** Produce `grading_drainage` — spot elevations, 1% minimum slope indicators, swale alignments with dimensions (300 × 300 mm standard section).
- [ ] **D4.** Produce `planting` — preserve circles for existing trees, proposed tree locations (min. 2 per school, drought-tolerant shade species), ground cover zones.
- [ ] **D5.** Produce `detail_sections` — cross-sections through sand pit with edge containment, footing detail (300 × 300 × 400 mm with anchor bolt), swale section, fence setback detail.
- [ ] **D6.** Produce `setting_out` — dimensions from two fixed site datum points to each equipment center and path intersection for construction layout.

### Phase E: Schedules & BOQ

- [ ] **E1.** Generate per-school equipment schedules (`.xlsx`) listing item, spec ref, quantity, unit, location, installation notes.
- [ ] **E2.** Generate per-school surface schedules calculating area (m²), depth (mm), and volume (m³) for each material type.
- [ ] **E3.** Generate per-school planting schedules with species/type, quantity, location, and purpose.
- [ ] **E4.** Generate per-school BOQ (`.xlsx`) with itemized earthworks, surfacing, equipment, local materials, planting, labor, and 10% contingency in ETB.
- [ ] **E5.** Consolidate all 6 schools into `BOQ_master_consolidated.xlsx` and `equipment_schedule_master.xlsx` for bulk procurement.

### Phase F: QA, Plotting & Handover

- [ ] **F1.** Run safety checklist per school (Section 4.1 rules) — all items must pass before plot.
- [ ] **F2.** Cross-check all CAD dimensions against the design report PDFs for consistency.
- [ ] **F3.** Plot full drawing sets at A1 for construction issue.
- [ ] **F4.** Plot reduced A3 sets for review by Assosa City Education Office and Cities Alliance.
- [ ] **F5.** Combine all plot PDFs into `SUIDAC_full_drawing_set_combined.pdf`.
- [ ] **F6.** Archive superseded drawings to `_archive/` folders.
- [ ] **F7.** Prepare transmittal letter and drawing issue log.

---

## 6. Option Selection Summary

| School | Students | Option | Rationale |
|--------|----------|--------|-----------|
| Gemeharu | 68 | **B** | Small enrollment; phased approach minimizes initial cost |
| Daresalam | 85 | **B** | Medium enrollment; core equipment sufficient for Phase 1 |
| Assosa Preprimary | 134 | **A** | Large enrollment; needs full complement immediately |
| Assosa Primary & Middle | 230 | **A** | Largest school; maximum play value essential |
| Benishan Gulgumuz | 124 | **A** | Large enrollment; full layout justified |
| Selamber | 68 | **B** | Small enrollment; phased approach appropriate |

---

## 7. Coordinate Reference

All KML data uses **WGS 84** (EPSG:4326). For AutoCAD drafting at 1:500, convert geographic coordinates to a local metric grid using a UTM projection (Zone 36N for Assosa) or a site-specific local coordinate system established from the KML centroid as (0, 0). Ensure the projection method is documented on each base plan sheet.

---

## 8. Contact & Review

- **Design review:** Assosa City Administration Education Office
- **Donor compliance:** IRC Ethiopia — SUIDAC Programme
- **Funder:** Cities Alliance

---

*This repository supports the IRC SUIDAC playground design programme. All designs comply with the spatial, safety, material, and construction constraints defined in the Master Command Protocol.*
