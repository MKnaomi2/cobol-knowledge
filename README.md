# COBOL Knowledge

**A sourced COBOL claim ledger. Not peer-reviewed. Not a dataset.**

Viral posts still say the global financial system runs on *220 billion lines of COBOL*, that practitioners retire at *10% a year*, and that *nobody has a plan*. Those sentences are directionally serious. They are not measurements this repo can vouch for.

This repository is a **claim ledger**: statements with citations, conflicts, and an explicit review status. Right now every seed claim is `proposed` or `contested`. Zero are `reviewed`. Citing a 2017 Reuters graphic or a 2019 practitioner essay is not the same as having data, and opening a pull request is not peer review.

> Existing public work already covers *teaching COBOL* ([Open Mainframe Project course](https://github.com/openmainframeproject/cobol-programming-course)), *compilers/parsers*, and a *defect suite*. This project does not replace them. It stores **cited claims**, including ones that do not hold up, and refuses to relabel citations as data or a PR as peer review.

## Why this exists

The bottleneck is not “COBOL is hard.” The language was designed to be readable. The bottleneck is **institutional knowledge** walking out the door: eligibility rules, batch windows, JCL folklore, shop dialects, and the undocumented “why” behind systems that still move money.

A manual can teach `PERFORM VARYING`. It cannot teach why a particular bank’s night batch is structured the way it is. Capture the public, citable layer here before the people who still hold it are gone.

Inspiration (not affiliation): [Maxx Rosenblum’s reel](https://www.instagram.com/reel/Db4r5CpMRCy/) arguing this is a knowledge problem with a closing window.

## What a record looks like

```yaml
id: loc-in-production
status: contested          # proposed | reviewed | contested | withdrawn
confidence: low
statement: >
  Published estimates of COBOL lines in production disagree by more
  than 3x. The 220 billion figure still circulating in 2026 is the
  1990s Gartner-era number, not current research.
sources:
  - {id: reuters-cobol-blues, role: secondary}
  - {id: vanson-bourne-2022, role: primary}
conflicts:
  - note: 220B vs ~250B vs 775–850B
```

Browse:

- [`claims/`](claims/) — sourced statements (the ledger)
- [`sources/catalog.yaml`](sources/catalog.yaml) — bibliographic catalog
- [`schema/`](schema/) — machine-checkable shapes
- [`idioms/`](idioms/) — practitioner patterns (empty until attested)

## Status of the seed

The seed claims in this first commit are **proposed or contested**, not peer-reviewed. They exist so the process has something real to chew on: conflicting line-count estimates, ATM/banking share figures that trace to a 2017 Reuters graphic, and the 10%/year retirement rate that traces to Phil Teplitzky (2019), not a BLS series.

CI will fail a PR that:

- adds a claim without sources in the catalog
- marks `status: reviewed` with no reviewers
- marks `status: contested` with no `conflicts`
- breaks the JSON Schema

## How to contribute

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md).
2. Open an issue with the [new-claim](.github/ISSUE_TEMPLATE/new-claim.yml) or [challenge-claim](.github/ISSUE_TEMPLATE/challenge-claim.yml) template.
3. Add or edit YAML under `claims/` and `sources/`.
4. Run `python scripts/validate.py`.
5. Open a pull request. Claims move `proposed → reviewed` only after an independent review of the sources.

Do **not** paste IBM manuals, vendor courseware, or employer code. Do **not** invent shop lore. If you held production COBOL on the clock, say so in the reviewer attestation — the code stays out.

## Not in scope

- A COBOL textbook (use the Open Mainframe Project course)
- A compiler, IDE, or migration product
- Scraping private bank or agency source
- “AI will rewrite the mainframe” hot takes without evidence

## License

Knowledge records and documentation: [CC BY 4.0](LICENSE).
Validator and tests: the same license, for simplicity.

## Verification

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
python -m pytest -q
```
