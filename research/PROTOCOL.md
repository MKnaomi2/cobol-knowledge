# COBOL Knowledge research protocol (2026-09-01)

AJ correction: do not ship scaffolding. Do not call it peer-reviewed or data-backed.
Research for ~5 hours, then commit **content** (sourced claims / attested public idioms).

## Hard rules

1. Every claim quotes a source you opened. Paraphrase is marked paraphrase.
2. Vendor marketing and 2017 Reuters graphics are not measurements.
3. Do not paste IBM/ISO manuals. Cite section + URL.
4. Do not invent shop lore. Idioms only from public specs, OMP labs, GnuCOBOL docs, or named public forum posts.
5. Status is `proposed` unless an independent pass opened the URLs.
6. Prefer language/runtime facts over viral market stats.

## Target corpus (open these)

- IBM Enterprise COBOL for z/OS Language Reference (public IBM Docs)
- IBM Enterprise COBOL Programming Guide
- GnuCOBOL Programmer's Guide / News
- ISO/IEC 1989:2023 bibliographic record only (no paste)
- Open Mainframe Project COBOL Programming Course (labs, not PDF dump)
- PhaseChange cobol-defects-suite README + programs
- CODASYL / Grace Hopper / COBOL-60 history from primary or LOC/NIST
- IBM CICS, IMS, DB2, JCL public docs (facts that are in the manual)
- arXiv / peer-reviewed SE papers on COBOL (rare; still not "this repo is peer-reviewed")

## Output shape

YAML under `claims/` matching `schema/claim.schema.json`.
New sources in `sources/catalog.yaml`.
Research notes in `research/notes/` (not published as knowledge).

## Done when

≥25 claims that a COBOL programmer would actually look up (PICTURE, COMP-3, 88-level, GOBACK vs STOP RUN, COPY, REDEFINES, EVALUATE, file status, packed decimal, EBCDIC vs NATIONAL, SSRANGE, etc.), each with a spec cite — not 9 Instagram-stat takedowns.
