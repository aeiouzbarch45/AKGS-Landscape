# SPECIFICATION SUIDAC-SPEC-01 — EARTHWORKS

**Project:** IRC SUIDAC — Assosa City Playground Design (6 Pre-Primary Schools)
**Client:** International Rescue Committee (IRC) — Ethiopia Mission
**Funder:** Cities Alliance (CA)
**Location:** Assosa City, Benishangul-Gumuz Regional State, Ethiopia (~1,500 m ASL)
**Work Section:** Site clearance, excavation, filling, formation and compaction
**Document No.:** SUIDAC-SPEC-01
**Revision:** 00 — First Issue
**Date of Issue:** 2026-08-02
**Status:** Issue for Construction

---

## 1. GENERAL

### 1.1 Scope of Works

This Specification governs all earthworks required for the construction of pre-primary playgrounds
at the six (6) SUIDAC schools listed in Clause 1.5. The Works comprise, without limitation:

1. Setting out from the two fixed site datum points shown on the `setting_out` drawings.
2. Site clearance, grubbing and removal of vegetation, refuse, debris and buried obstructions.
3. Removal, relocation or retention of existing play equipment in accordance with the
   retain / repair / remove inventory recorded on the `siteanalysis` drawings.
4. Stripping, stockpiling and re-use of topsoil.
5. Excavation to formation level for play surfaces, pathways, sand pits and drainage swales.
6. Hand excavation of equipment footing pits.
7. Placement and compaction of engineered fill.
8. Preparation and compaction of subgrade / formation to the specified density.
9. Grading of all finished formations to the falls required by SUIDAC-SPEC-05 (Drainage).
10. Protection of existing trees designated for retention.
11. Dust suppression, erosion control and disposal of surplus spoil.

### 1.2 Basis of Specification

All governing technical values in this Specification are extracted from the **SUIDAC AI Agent
Master Command Protocol** ("the Master Command"), Section 4 *Key Design Rules*, as reproduced in
the repository `README.md`. Values are traceable in Clause 1.6.

> **Issue note:** At the date of issue, the file `00_project-admin/SUIDAC_AI_Agent_Master_Command.md`
> was not present in the repository. All Master Command values used herein have been taken from the
> verbatim reproduction of the design rules in `README.md` §4 and the specification annotations in
> `README.md` §2. Should the Master Command source document be issued subsequently, this
> Specification shall be re-verified against it and re-issued as Rev 01 if any discrepancy is found.

### 1.3 Related Documents

| Reference | Title |
|-----------|-------|
| SUIDAC-SPEC-02 | Surfacing Specification |
| SUIDAC-SPEC-03 | Equipment Installation Specification |
| SUIDAC-SPEC-04 | Timber Treatment Specification |
| SUIDAC-SPEC-05 | Drainage Specification |
| `<S#>_006_grading_drainage.dwg` | Grading & Drainage Plan (spot levels, falls, swales) |
| `<S#>_008_detail_sections.dwg` | Details & Sections (sand pit edge, footing, swale) |
| `<S#>_setting_out.dwg` | Setting-Out Plan (datum points and dimensions) |
| `<S#>_earthwork_summary.xlsx` | Per-school cut / fill / disposal quantities |
| `DWG_footing_detail_300x300x400.dwg` | Standard equipment footing detail |

### 1.4 Standards and Test Methods

Where no Ethiopian Standard applies, the following shall govern:

| Purpose | Test method |
|---------|-------------|
| Laboratory maximum dry density (modified Proctor) | AASHTO T 180 Method D / ASTM D 1557 |
| Field dry density | Sand replacement (AASHTO T 191) or nuclear gauge |
| In-situ subgrade strength | Dynamic Cone Penetrometer (DCP), correlated to CBR |
| Particle size distribution | AASHTO T 88 / ASTM D 422 |
| Atterberg limits | AASHTO T 89 / T 90 |

### 1.5 Application to Schools

| Code | School | Students | Option | Earthworks extent |
|------|--------|----------|--------|-------------------|
| S1 | Gemeharu Primary & Midlevel | 68 | B (Phased) | Phase 1 footprint only; Phase 2 zone left undisturbed and hatched |
| S2 | Daresalam Primary & Midlevel | 85 | B (Phased) | Phase 1 footprint only; Phase 2 zone left undisturbed and hatched |
| S3 | Assosa Preprimary | 134 | A (Full) | Full play area footprint |
| S4 | Assosa Primary & Middle | 230 | A (Full) | Full play area footprint |
| S5 | Benishan Gulgumuz Primary & Middle | 124 | A (Full) | Full play area footprint |
| S6 | Selamber Primary School | 68 | B (Phased) | Phase 1 footprint only; Phase 2 zone left undisturbed and hatched |

Active play zone area shall be provided at the rate of **80 m² per 50 students**, scaled
proportionally to enrolment, with not less than **20 %** of the total play area retained as quiet /
shade zone.

### 1.6 Schedule of Governing Values

| Ref | Parameter | Specified value | Source |
|-----|-----------|-----------------|--------|
| E-01 | Compaction of formation and engineered fill | **95 % of maximum dry density (modified Proctor)** | Master Command / README §2 (earthworks_spec annotation) |
| E-02 | Design subgrade | **Lateritic red soil, assumed CBR 5–10 %** | Master Command §4.4 |
| E-03 | Minimum finished gradient (all graded surfaces) | **1 % minimum slope** | Master Command §5 D3 / SUIDAC-SPEC-05 |
| E-04 | Equipment footing excavation (per leg) | **300 × 300 × 400 mm minimum** | Master Command §4.6 |
| E-05 | Plant and methods | **Manual labour + basic tools only; no heavy machinery** | Master Command §4.6 |
| E-06 | Installation crew | **4 unskilled labourers + 1 skilled metalworker** | Master Command §4.6 |
| E-07 | Surface drainage performance | **All surfaces to drain within 24 hours** | Master Command §4.4 |
| E-08 | Dry-season dust control | **Dust suppression required on bare areas (Nov–Mar)** | Master Command §4.4 |
| E-09 | Material sourcing radius | **50 km of Assosa** | Master Command §4.4 |
| E-10 | Building / fence setback kept clear | **1.5 m general; 3.0 m at swings and slides** | Master Command §4.1 |
| E-11 | Fall zone kept clear of obstruction | **2.0 m clear radius to moving equipment** | Master Command §4.1 |
| E-12 | Existing tree canopy protection radius | **3–5 m (as marked on `planting` drawings)** | Master Command §5 A6 |

Values marked **[E]** elsewhere in this document are engineering elaborations of standard good
practice adopted to make the Master Command values buildable; they do not override any value above.

### 1.7 Definitions

- **Formation** — the finished, compacted surface of the subgrade upon which surfacing is laid.
- **Engineered fill** — imported or re-used material placed and compacted under this Specification.
- **Unsuitable material** — topsoil, peat, organic silt, material containing vegetable matter,
  refuse, timber, roots, termite-affected soil, or material with liquid limit > 50 % or
  plasticity index > 25 % [E].
- **Hold point** — a stage of the Works that shall not proceed until inspected and released in
  writing by the Engineer.

---

## 2. PRODUCTS AND MATERIALS

### 2.1 General Material Requirements

All materials shall be sourced from within a **50 km radius of Assosa** (Master Command §4.4).
The Contractor shall submit the source location, haul distance and a representative 25 kg sample of
each fill material for approval not less than 14 days before first delivery [E].

### 2.2 Topsoil

Topsoil stripped from the site shall be free of stones exceeding 50 mm, roots, weeds with
rhizomes and refuse [E]. It shall be stockpiled separately for re-use in grass and planting
zones under SUIDAC-SPEC-02.

### 2.3 Engineered Fill

Engineered fill shall be approved lateritic gravel or selected site-won granular material
complying with the following [E, consistent with Master Command §4.4 soil assumption]:

| Property | Requirement |
|----------|-------------|
| Maximum particle size | 50 mm, and not exceeding two-thirds of the compacted layer thickness |
| Passing 0.075 mm sieve | ≤ 35 % |
| Plasticity index | ≤ 20 % |
| Soaked CBR at 95 % MDD | ≥ 10 % |
| Organic content | Nil |
| Swelling / expansive clay | Not permitted |

### 2.4 Prohibited Fill Materials

The following shall not be incorporated into any fill or formation: topsoil; organic or
vegetable matter; refuse and demolition waste containing timber, plastic or glass; expansive
black cotton clay; termite-mound material or material taken from within 2 m of an active
termite mound [E — Master Command §4.4 records termite risk as **HIGH**].

### 2.5 Imported Water

Water for compaction and dust suppression shall be clean, free of oil, salt and organic
contamination, and shall not be drawn from any source used for drinking water without the
written consent of the School Director [E].

---

## 3. EXECUTION

### 3.1 Setting Out

1. All setting out shall be taken from the **two fixed site datum points** established on the
   `setting_out` drawing for each school. Datum points shall be permanent concrete markers
   protected for the duration of the Works [E].
2. Coordinates derived from KML data are in WGS 84 (EPSG:4326), converted to a local metric grid
   (UTM Zone 36N, or a site-local system with the KML centroid as origin) — see `README.md` §7.
3. Setting out shall be checked against the `masterlayout` (1:200) and `equipment_layout` (1:100)
   drawings before excavation commences.

> **HOLD POINT 1 — Setting out.** Excavation shall not commence until the setting out, including
> all 2.0 m fall zones and 1.5 m / 3.0 m setbacks, has been verified and released by the Engineer.

### 3.2 Programme and Seasonal Constraints

1. Bulk earthworks shall be programmed for the **dry season, November to March**
   (Master Command §4.4).
2. Where earthworks are unavoidable during the **wet season, April to October**
   (~1,200 mm annual rainfall), the Contractor shall provide temporary cut-off drains, protect open
   formations with sheeting and shall not place or compact fill during or immediately after
   rainfall, nor when the material moisture content exceeds optimum + 2 % [E].
3. Open excavations within the school compound shall be barricaded and shall not be left open
   overnight where children have access [E].

### 3.3 Site Clearance

1. Clear the working area of all vegetation, grass, refuse, loose stone and debris.
2. Grub out roots and stumps to a depth of not less than 300 mm below formation level and backfill
   the voids with engineered fill compacted to Clause 3.7 [E]. Complete removal of woody root
   material is mandatory given the **HIGH termite risk** recorded in Master Command §4.4.
3. Existing play equipment shall be retained, repaired or removed strictly in accordance with the
   inventory recorded on the `siteanalysis` drawings. Equipment marked "retain" shall be protected;
   equipment marked "remove" shall have its foundations broken out to 300 mm below formation [E].
4. Arisings shall be removed from the school compound to a location approved by the Assosa City
   Administration. Burning of cleared vegetation within the compound is not permitted [E].

### 3.4 Protection of Existing Trees

1. Trees marked for retention on the `planting` drawings shall be fenced off at the canopy
   line — **3 to 5 m radius** (Master Command §5 A6) — before any clearance begins.
2. No excavation, fill, material storage, vehicle movement or washing out shall take place within
   the protection ring.
3. Roots exceeding 25 mm diameter encountered outside the ring shall be cleanly cut and sealed;
   they shall not be torn [E].
4. Tree protection rings shall subsequently receive **100 mm of stone mulch or recycled tire
   mulch** under SUIDAC-SPEC-02 (Master Command §4.3).

### 3.5 Topsoil Stripping

1. Strip topsoil over the full construction footprint to its full depth, typically 150 mm [E], or
   to the depth directed by the Engineer.
2. Stockpile topsoil clear of the works in heaps not exceeding **1.5 m** in height, with side
   slopes no steeper than 1:2, seeded or sheeted if to be stored longer than 60 days [E].
3. Stockpiles shall not be placed within tree protection rings, within any 2.0 m fall zone or
   across any drainage line.

### 3.6 Excavation

1. Excavate to the formation levels and falls shown on the `grading_drainage` drawings, using
   **manual labour and basic hand tools only — no heavy machinery** (Master Command §4.6).
2. **Sand pit / fall zone excavation:** excavate to accept the full specified surfacing depth
   below the surrounding finished level, namely:
   - **150–200 mm** beneath moving equipment (E1 Merry-Go-Round, E2 See-Saw, E4 Chain Swing);
   - **300 mm** beneath the slide runout (E3);
   plus the thickness of any free-draining blanket required by SUIDAC-SPEC-05
   (Master Command §4.3).
3. **Pathway excavation:** excavate to accept **100 mm of compacted fine gravel** over a prepared
   formation, to a minimum finished pathway width of **1.2 m** (Master Command §4.1, §4.3).
4. **Swale excavation:** excavate to the standard **300 × 300 mm** section
   (Master Command §5 D3) — see SUIDAC-SPEC-05.
5. **Footing excavation:** hand-excavate each equipment leg pit to a minimum of
   **300 × 300 × 400 mm** (Master Command §4.6), with vertical faces, square to the setting-out
   grid, and with the base level, undisturbed and free of loose spoil.
6. Over-excavation shall be made good with engineered fill compacted to Clause 3.7 at the
   Contractor's expense. Backfilling of over-excavated footing pits with loose spoil is prohibited.
7. Soft spots identified at formation shall be excavated out and replaced with engineered fill.

### 3.7 Filling and Compaction

1. Fill shall be placed in horizontal layers not exceeding **150 mm compacted thickness** [E], each
   layer being compacted before the next is placed.
2. Each layer shall be moisture-conditioned to within −2 % / +2 % of optimum moisture content [E]
   and compacted to not less than **95 % of the maximum dry density determined by the modified
   Proctor test** (Master Command; README §2 earthworks annotation).
3. Compaction shall be achieved with hand-guided plant compatible with the no-heavy-machinery
   constraint — vibrating plate compactor, pedestrian roller or hand rammer [E].
4. The compaction requirement applies to:
   - formation beneath all pathways and gravel surfaces;
   - formation beneath sand pits and fall zones;
   - all engineered fill in cut / fill transitions and reinstated excavations;
   - backfill around equipment footings above the concrete.
5. Grass and planting zones shall not be over-compacted; formation in these zones shall be
   scarified to 100 mm before topsoil is replaced [E].

> **HOLD POINT 2 — Formation.** No surfacing material shall be placed and no footing concrete
> poured until the formation has been proof-checked, density-tested to Clause 4.2 and released in
> writing by the Engineer.

### 3.8 Grading and Falls

1. All formations shall be graded to a **minimum fall of 1 %** to the drainage outlets, swales and
   discharge points shown on the `grading_drainage` drawings (Master Command §5 D3).
2. Falls shall be set so that **all surfaces drain within 24 hours** of a rainfall event
   (Master Command §4.4). Flat spots, reverse falls and closed depressions are not acceptable.
3. The finished gradient across active play zones shall not exceed 2.5 % in any direction, so that
   surfaces remain safe for 5–6 year-old users while satisfying the 1 % minimum [E].
4. Cross-fall on pathways shall be 1 % minimum to 2 % maximum, discharging to the adjacent grass or
   swale [E].
5. Earth slopes formed in cut or fill shall not be steeper than 1:3 within play areas, and shall
   not be steeper than 1:2 elsewhere, and shall be grassed on completion [E].

### 3.9 Tolerances

| Item | Tolerance |
|------|-----------|
| Formation level beneath sand pits and fall zones | ± 20 mm [E] |
| Formation level beneath pathways | ± 15 mm [E] |
| Formation level, general play areas | ± 25 mm [E] |
| Surface regularity, measured under a 3 m straightedge | 20 mm maximum deviation [E] |
| Plan position of excavations against setting-out grid | ± 25 mm [E] |
| Footing pit plan dimensions | +50 mm / −0 mm on 300 × 300 mm [E] |
| Footing pit depth | +50 mm / −0 mm on 400 mm [E] |
| Achieved gradient | Not less than the specified 1 % minimum in any case |

Negative tolerance on any dimension derived from a Master Command minimum value
(300 × 300 × 400 mm footing, 1 % fall, 1.2 m path width, 2.0 m fall zone) is **not permitted**.

### 3.10 Clearances to be Maintained

Earthworks shall not encroach upon, and no spoil, plant or material shall be stored within:

- the **2.0 m clear fall zone radius** around all moving equipment (Master Command §4.1);
- the **1.5 m general setback** from any building wall or fence to equipment edge;
- the **3.0 m setback** from any building wall to a swing frame or slide platform;
- the **1.2 m minimum pathway width** of any route required for site access or supervision;
- any existing tree protection ring.

### 3.11 Dust Suppression and Erosion Control

1. During the **dry season (November–March)**, bare and stripped areas shall be dampened with
   water at the frequency necessary to prevent airborne dust, and in any case not less than twice
   daily during active earthmoving adjacent to occupied classrooms (Master Command §4.4) [E].
2. Chemical dust palliatives are not permitted.
3. Completed formations left exposed for more than 14 days shall be sealed by rolling and shall be
   protected from scour by temporary cut-off drains discharging to the permanent swale system [E].
4. Erosion of formations into the swale network shall be made good by the Contractor, and silt
   shall be removed from swales before handover.

### 3.12 Spoil and Surplus Material

1. Surplus suitable material shall be used first for on-site regrading, mounding within quiet
   zones or berm formation, subject to the Engineer's approval [E].
2. Unsuitable material and surplus spoil shall be removed from the school compound to an approved
   tip. Quantities shall reconcile with `<S#>_earthwork_summary.xlsx`.
3. No spoil shall be deposited in drainage channels, on neighbouring land, or within tree
   protection rings.

---

## 4. QUALITY ASSURANCE AND TESTING

### 4.1 Submittals

| Submittal | Timing |
|-----------|--------|
| Fill material source, haul distance (≤ 50 km) and test certificates | 14 days before delivery [E] |
| Modified Proctor (AASHTO T 180-D) result for each fill source | Before first placement |
| Setting-out record referenced to the two site datum points | Before Hold Point 1 |
| Field density test results | Within 48 hours of each test [E] |
| Earthwork quantity reconciliation against `<S#>_earthwork_summary.xlsx` | At completion |

### 4.2 Testing Frequency

| Test | Minimum frequency |
|------|-------------------|
| Field dry density on compacted layers | 1 test per 200 m² per layer, minimum 3 tests per school [E] |
| DCP / CBR verification of natural subgrade | 3 positions per school, to confirm the assumed **CBR 5–10 %** (Master Command §4.4) [E] |
| Level and fall check (dumpy level or water level) | On every graded panel prior to surfacing [E] |
| Straightedge regularity check | 1 per 100 m² of formation [E] |
| Footing pit dimension check | Every pit, 100 % |

Any test recording less than 95 % of modified Proctor MDD shall require the layer to be scarified,
re-conditioned and re-compacted, and re-tested at the Contractor's expense.

### 4.3 Non-Conformance

Non-conforming earthworks shall be recorded, notified to the Engineer within 24 hours, and
rectified before the affected area is covered. Rectified work shall be re-tested at twice the
standard frequency [E].

### 4.4 Site Safety

1. The works are executed within occupied school compounds. All excavations shall be barricaded
   and supervised during school hours [E].
2. The standard crew comprises **4 unskilled labourers and 1 skilled metalworker**
   (Master Command §4.6); the metalworker is not to be deployed on bulk earthworks while equipment
   fabrication or installation is programmed.
3. No excavation shall be left unbackfilled or unprotected outside working hours where children
   have access.
4. Personal protective equipment (boots, gloves, eye protection, dust masks during dry-season
   works) shall be provided to all operatives [E].

---

## 5. COMPLETION

### 5.1 Handover Criteria

Earthworks shall be accepted only when all of the following are demonstrated:

1. All formations achieve **≥ 95 % modified Proctor** density, evidenced by test records.
2. All graded surfaces achieve **≥ 1 % fall** to a positive outlet, with no ponding.
3. A flood / drain-down check confirms **no standing water after 24 hours**
   (Master Command §4.4) — witnessed jointly with SUIDAC-SPEC-05 commissioning.
4. All 2.0 m fall zones, 1.5 m / 3.0 m setbacks and 1.2 m pathway widths are clear and verifiable
   on site against the `masterlayout` drawing.
5. All footing pits conform to **300 × 300 × 400 mm** minimum and are clean and dry.
6. Tree protection rings are intact and undamaged.
7. Surplus spoil is removed and the compound is left clean and safe.
8. The per-school safety checklist items relating to levels, falls and clearances are signed off.

### 5.2 Measurement and Payment

| Item | Unit | Notes |
|------|------|-------|
| Site clearance and grubbing | m² | Measured on plan over the cleared footprint |
| Topsoil strip and stockpile | m³ | Measured in bank volume |
| Excavation to formation | m³ | Measured net; no allowance for bulking |
| Hand excavation, footing pits | nr | Per pit, 300 × 300 × 400 mm minimum |
| Engineered fill, placed and compacted to 95 % MDD | m³ | Measured compacted in place |
| Grading and trimming of formation | m² | Includes achievement of 1 % minimum fall |
| Dust suppression | item | Dry season provision, Nov–Mar |
| Disposal of surplus / unsuitable material | m³ | Includes cartage off compound |

Quantities shall be reconciled with `<S#>_earthwork_summary.xlsx` and priced into
`<S#>_BOQ.xlsx` in ETB, inclusive of the programme-standard **10 % contingency**
(README §5 E4).

---

## 6. REVISION RECORD

| Rev | Date | Description | Prepared | Checked |
|-----|------|-------------|----------|---------|
| 00 | 2026-08-02 | First issue. All technical values extracted from the SUIDAC Master Command Protocol §4 as reproduced in `README.md`. | SUIDAC Design Team | — |

---

*End of SUIDAC-SPEC-01 — Earthworks*
