# 06_construction / specifications — Specification Register

**Project:** IRC SUIDAC — Assosa City Playground Design (6 Pre-Primary Schools)
**Client:** International Rescue Committee (IRC) — Ethiopia Mission
**Funder:** Cities Alliance (CA)
**Location:** Assosa City, Benishangul-Gumuz Regional State, Ethiopia
**Register Revision:** 00 — First Issue
**Date of Issue:** 2026-08-02

---

## 1. Purpose

This folder contains the written construction specifications for the SUIDAC playground works at all
six schools (S1–S6). The specifications are read together with the drawing set (`03_cad/`), the
schedules (`04_schedules/`), the bills of quantities (`05_boq/`), the construction details
(`06_construction/details/`) and the per-school safety checklists
(`06_construction/safety_checklists/`).

In the event of conflict, the following order of precedence applies:

1. The **SUIDAC AI Agent Master Command Protocol** (`00_project-admin/`);
2. These specifications;
3. Figured dimensions on the issued drawings;
4. Scaled dimensions on the issued drawings;
5. The bills of quantities.

Where a specification value is expressed as a **minimum** (fall, footing size, fall zone, path
width, soak duration), it shall never be reduced. Where expressed as a **maximum** (slide platform
height, climbing structure height, footing concrete volume), it shall never be exceeded.

---

## 2. Document Register

| Doc No. | Title | File | Rev | Status |
|---------|-------|------|-----|--------|
| SUIDAC-SPEC-01 | Earthworks | [`earthworks_spec.md`](earthworks_spec.md) | 00 | Issue for Construction |
| SUIDAC-SPEC-02 | Surfacing | [`surfacing_spec.md`](surfacing_spec.md) | 00 | Issue for Construction |
| SUIDAC-SPEC-03 | Equipment Installation | [`equipment_installation_spec.md`](equipment_installation_spec.md) | 00 | Issue for Construction |
| SUIDAC-SPEC-04 | Timber and Bamboo Treatment | [`timber_treatment_spec.md`](timber_treatment_spec.md) | 00 | Issue for Construction |
| SUIDAC-SPEC-05 | Drainage | [`drainage_spec.md`](drainage_spec.md) | 00 | Issue for Construction |
| — | Specification Register (this document) | `README.md` | 00 | Issue for Construction |

---

## 3. Source of Technical Values

Every technical value in these specifications is extracted from the **SUIDAC AI Agent Master
Command Protocol**, Section 4 *Key Design Rules* (§4.1 Spatial Zoning, §4.2 Equipment, §4.3 Surface
Materials, §4.4 Climate & Environmental Constraints, §4.5 Banned Materials, §4.6 Construction
Constraints) and the detailed design requirements at §5 D3 / D5.

> ### ⚠ Issue note — source document not present in repository
>
> At the date of issue (2026-08-02), the file
> `00_project-admin/SUIDAC_AI_Agent_Master_Command.md` was **not present in this repository** — the
> repository contained only `README.md`, `LICENSE` and `.gitignore` across all commits and branches.
>
> All Master Command values used in these specifications have therefore been extracted from the
> **verbatim reproduction of the design rules in the repository `README.md` §4** (titled *"Key
> Design Rules (from SUIDAC Guidelines)"*), together with §2 (specification annotations), §5 D3/D5
> (detailed design requirements) and §7 (coordinate reference).
>
> **Action required:** when the Master Command source document is added to the repository, these
> specifications shall be re-verified clause by clause against Section 4 of that document. Any
> discrepancy shall be corrected and the affected documents re-issued at Rev 01.

### 3.1 Notation

| Marker | Meaning |
|--------|---------|
| *(no marker)* | Value extracted directly from the Master Command; a source reference is cited in each specification's *Schedule of Governing Values* |
| **[E]** | Engineering elaboration — standard good practice added to make a Master Command value buildable, testable or maintainable. Elaborations never override, relax or contradict a Master Command value |

---

## 4. Master Traceability Matrix

Every Master Command value carried into the specifications, and where it is applied:

| Master Command source | Value | SPEC-01 | SPEC-02 | SPEC-03 | SPEC-04 | SPEC-05 |
|---|---|:--:|:--:|:--:|:--:|:--:|
| §4.1 Fall zone, moving equipment | 2.0 m clear radius | ● | ● | ● | | ● |
| §4.1 Building setback, general | 1.5 m minimum | ● | | ● | | ● |
| §4.1 Building setback, swing / slide | 3.0 m minimum | ● | | ● | | ● |
| §4.1 Pathway width | 1.2 m minimum | ● | ● | ● | | ● |
| §4.1 Active play zone provision | 80 m² per 50 students | ● | ● | | | |
| §4.1 Quiet / shade zone | ≥ 20 % of play area | ● | ● | | | |
| §4.2 E1 Merry-Go-Round | Ø 2.3 m × H 1.0 m; RHS 40 × 20 × 1.5 mm | | ● | ● | | |
| §4.2 E2 See-Saw | L 4.0 m × H 1.0 m; RHS 40 × 40 mm; 8 m × 3 m zone | | ● | ● | | ● |
| §4.2 E3 Slide | W 3.0 m × H 2.0 m; platform max 1.5 m | | ● | ● | | ● |
| §4.2 E4 Chain Swing | W 2.5 m × H 2.5 m; pipe 60 × 60 × 2 mm | | ● | ● | | |
| §4.2 L1 Balance Beam | L 3.0–4.0 m, H 0.2–0.3 m, W 0.15–0.2 m; bamboo ≥ 80 mm dia. | | | ● | ● | |
| §4.2 L2 Climbing Structure | Max H 1.2 m; bamboo poles 60–80 mm dia. | | | ● | ● | |
| §4.2 L3 Tunnel Crawl | Ø 0.6–0.8 m, L 2.0–3.0 m | | | ● | | ● |
| §4.2 L4 Stepping Logs / Stones | Ø 0.15–0.2 m, H 0.1–0.15 m, spacing 0.3–0.4 m | | | ● | ● | |
| §4.3 Sand, moving equipment | Washed river sand, 150–200 mm | ● | ● | ● | | ● |
| §4.3 Sand, slide runout | Washed river sand, 300 mm | ● | ● | ● | | ● |
| §4.3 Pathway gravel | Fine gravel 10–20 mm, 100 mm compacted | ● | ● | | | ● |
| §4.3 Play lawn | Drought-tolerant grass | ● | ● | | | ● |
| §4.3 Tree protection ring | Stone or tire mulch, 100 mm | ● | ● | | | ● |
| §4.3 Drainage swale | Rubble / coarse gravel, 200 mm | ● | ● | | | ● |
| §4.4 Wet season | April – October, ~1,200 mm/yr | ● | ● | ● | ● | ● |
| §4.4 Dry season / dust suppression | November – March | ● | ● | ● | ● | ● |
| §4.4 Drain-down performance | All surfaces drain within 24 hours | ● | ● | | ● | ● |
| §4.4 Termite risk | HIGH — boron-based treatment, 24-hour minimum soak | ● | ● | ● | ● | ● |
| §4.4 UV / corrosion | Zinc-chromate primer + enamel topcoat | | | ● | | |
| §4.4 Soil | Lateritic red soil, assumed CBR 5–10 % | ● | | | | ● |
| §4.4 Sourcing radius | All materials within 50 km of Assosa | ● | ● | ● | ● | ● |
| §4.5 Banned materials | Synthetic turf; rubber tiles (except recycled tire mulch); imported specialty items; complex prefab; exotic invasive species | | ● | ● | ● | ● |
| §4.6 Plant | Manual labour + basic tools; no heavy machinery | ● | | ● | | ● |
| §4.6 Footing concrete volume | Max 0.05 m³ per footing, hand-mixed C20 | | | ● | | ● |
| §4.6 Crew | 4 unskilled labourers + 1 skilled metalworker | ● | | ● | | |
| §4.6 Drainage method | Gravity-based only; no pumps | | | | | ● |
| §4.6 Footing size | Minimum 300 × 300 × 400 mm per leg, with anchor bolts | ● | | ● | | |
| §5 D3 Minimum slope | 1 % minimum | ● | ● | ● | | ● |
| §5 D3 Swale section | 300 × 300 mm standard section | ● | | | | ● |
| §5 A6 Tree canopy protection | 3–5 m radius | ● | ● | | | ● |
| §2 Earthworks annotation | Compaction to 95 % modified Proctor | ● | ● | ● | | ● |
| §5 E4 BOQ | 10 % contingency, priced in ETB | ● | ● | ● | ● | ● |

**Derived value check:** the standard footing of 300 × 300 × 400 mm = **0.036 m³**, satisfying the
0.05 m³ per-footing maximum (SPEC-03 Clause 2.4). The standard swale of 300 mm depth with 200 mm
rubble fill leaves **100 mm freeboard** (SPEC-05 Clause 3.3).

---

## 5. Consolidated Hold Point Register

Work shall not proceed past a hold point until inspected and released in writing by the Engineer.

| No. | Hold point | Specification | Stage |
|-----|------------|---------------|-------|
| 1 | Setting out verified from the two site datum points | SPEC-01 §3.1 | Before excavation |
| 2 | Formation compaction and level released | SPEC-01 §3.7 | Before surfacing or concrete |
| 3 | Pre-surfacing check — level, fall, compaction, footing tops | SPEC-02 §3.1 | Before sand / gravel placement |
| 4 | Equipment setting out — fall zones and setbacks verified | SPEC-03 §3.1 | Before footing excavation |
| 5 | Footings — dimensions, anchor bolts, top level | SPEC-03 §3.3 | Before backfill and surfacing |
| 6 | Timber treatment records and penetration test accepted | SPEC-04 §3.4 | Before delivery to the installation area |
| 7 | Swale invert level, gradient and filter layer | SPEC-05 §4.2 | Before rubble placement |

---

## 6. Construction Sequence

| Stage | Works | Governing specification |
|-------|-------|-------------------------|
| 1 | Setting out; tree protection; site clearance | SPEC-01 |
| 2 | Topsoil strip and stockpile | SPEC-01 |
| 3 | Timber and bamboo treatment commences (long lead — 24-hour soak plus 14-day diffusion plus drying) | SPEC-04 |
| 4 | Bulk excavation, filling and compaction to 95 % modified Proctor | SPEC-01 |
| 5 | Drainage swales, sumps, soakaways and outfalls | SPEC-05 |
| 6 | Equipment footing excavation and C20 concrete; 7-day cure | SPEC-03 |
| 7 | Erection and coating of metal equipment E1–E4 | SPEC-03 |
| 8 | Installation of treated L-series elements L1–L4 | SPEC-03 / SPEC-04 |
| 9 | Sand, gravel, mulch and grass surfacing | SPEC-02 |
| 10 | 24-hour drain-down commissioning test | SPEC-05 |
| 11 | Safety checklist, snagging and handover | SPEC-03 / all |

**Programme note:** timber treatment (Stage 3) has the longest lead time — a 24-hour minimum soak
followed by a 14-day diffusion period and 14–28 days of covered drying — and shall be started at
mobilisation. Bulk earthworks are best programmed in the dry season, November–March.

---

## 7. Application by School

| Code | School | Students | Option | Notes |
|------|--------|----------|--------|-------|
| S1 | Gemeharu Primary & Midlevel | 68 | **B** (Phased) | Phase 1 scope; future zone hatched and left undisturbed |
| S2 | Daresalam Primary & Midlevel | 85 | **B** (Phased) | Phase 1 scope; future zone hatched and left undisturbed |
| S3 | Assosa Preprimary | 134 | **A** (Full) | Full complement E1–E4, L1–L4 |
| S4 | Assosa Primary & Middle | 230 | **A** (Full) | Full complement E1–E4, L1–L4 |
| S5 | Benishan Gulgumuz Primary & Middle | 124 | **A** (Full) | Full complement E1–E4, L1–L4 |
| S6 | Selamber Primary School | 68 | **B** (Phased) | Phase 1 scope; future zone hatched and left undisturbed |

Option rule: > 100 students → Option A (maximum play value); ≤ 100 students → Option B (minimum
viable / phased). All specification requirements apply equally to Phase 1 and future-phase works.

---

## 8. Pre-Handover Verification Summary

The following are absolute bars to handover at any school:

- [ ] Any formation below **95 % modified Proctor**
- [ ] Any surface with less than a **1 % fall**, or any standing water at **24 hours**
- [ ] Any sand fall zone below **150 mm** (or **250 mm** at a slide runout) in service depth
- [ ] Any fall zone less than the **2.0 m clear radius**
- [ ] Any setback less than **1.5 m** general or **3.0 m** at a swing or slide
- [ ] Any footing smaller than **300 × 300 × 400 mm**, or exceeding **0.05 m³**
- [ ] Any exposed concrete, base plate, bolt or rubble within a fall zone
- [ ] Any metal element without the complete **zinc-chromate primer + enamel topcoat** system
- [ ] Any timber or bamboo without a treatment record showing a **≥ 24-hour boron soak**
- [ ] Any banned material present on site
- [ ] Any pump or powered component in the drainage system
- [ ] Any sharp edge, protrusion, entrapment gap or splinter accessible to children
- [ ] Any unsigned item on the per-school `<S#>_safety_checklist.pdf`

---

## 9. Revision Record

| Rev | Date | Description |
|-----|------|-------------|
| 00 | 2026-08-02 | First issue of the register and of SUIDAC-SPEC-01 to SUIDAC-SPEC-05. |

---

*IRC SUIDAC Programme — Assosa City Playground Design. All specifications comply with the spatial,
safety, material and construction constraints defined in the Master Command Protocol.*
