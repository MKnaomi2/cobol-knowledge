# Governance

v0 is a public ledger under [MKnaomi2/cobol-knowledge](https://github.com/MKnaomi2/cobol-knowledge).

## Roles

| Role | Who | Power |
|------|-----|--------|
| Maintainer | repo admin | Merge, status overrides, withdraw records, ban bad-faith PRs |
| Reviewer | anyone who opens the sources | Can move `proposed` → `reviewed` or `contested` on a claim they did not author |
| Author | PR opener | Proposes records; cannot self-review into `reviewed` |

Self-review is allowed for fixing typos and schema. It is **not** allowed for `status: reviewed`.

## Independence

A reviewer is independent if they did not write the claim YAML in the same PR. Two people in the same vendor sales org should not be the only review pair on a vendor-commissioned statistic.

## Evidence rank (highest first)

1. Primary survey with method, n, date, and population
2. Standards and language specs (ISO/IEC 1989, IBM Enterprise COBOL Language Reference — cite, do not paste)
3. Reproducible public datasets (BLS occupational series, TIOBE with date)
4. Reputable secondary (Reuters, GAO, peer-reviewed paper) that names its primary
5. Vendor claims (Micro Focus, IBM marketing, consultancies) — allowed, labelled `role: vendor`
6. Practitioner attestation — allowed for idioms, not for global statistics

A viral social post is **not** a source. It can be recorded under `viral_misuse`.

## Conflicts of interest

Record them. A Vanson Bourne study paid for by Micro Focus is still evidence; it is not independent census data. The catalog field `independence` exists for this.

## Withdrawal

Withdrawn claims remain in git history and in `claims/` with `status: withdrawn`. We do not rewrite the past to look cleaner than it was.

## Scope changes

Adding a new record *kind* or schema field requires a PR that updates `schema/*.json`, `scripts/validate.py`, and at least one example. Do not silently extend the YAML.

## Not a standards body

This repo does not certify programmers, bless dialects, or speak for CODASYL, ISO, IBM, or the Open Mainframe Project. It records claims.
