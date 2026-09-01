# Contributing

This is a **ledger**, not a blog. A useful contribution is a sourced claim, a documented conflict, a catalogued source, or a review of someone else’s sources.

## Claim lifecycle

```
issue → proposed YAML → CI green → independent review → reviewed
                                              ↘ contested (conflict recorded)
                                              ↘ withdrawn (with reason)
```

- **proposed** — sources exist; nobody has independently checked them yet.
- **reviewed** — at least one reviewer who did not author the claim has opened the cited sources and recorded a verdict.
- **contested** — credible sources disagree, or a reviewer rejects the statement as written. The record stays. Disagreement is data.
- **withdrawn** — the statement should not be used. Keep the file; set `status: withdrawn` and explain.

`reviewed` with an empty `reviewers:` list will fail CI. So will `contested` with empty `conflicts:`.

## What we accept

| Kind | Example | Bar |
|------|---------|-----|
| Quantitative | ATM share, line counts, age | Amount, unit, date, method, conflicts |
| Qualitative | Universities largely dropped COBOL | Named sources, not vibes |
| Historical | CODASYL 1959, ISO/IEC 1989 | Primary or standards citations |
| Operational | COMP-3 packed decimal gotchas | Attested practice + a public example or spec cite |
| Idiom | `PERFORM UNTIL` vs `GO TO` shop rules | Attestation + dialect/platform |

## What we reject

- Unsourced statistics, including numbers “everybody knows”
- Verbatim vendor manuals or copyrighted course PDFs
- Employer source code, account layouts, or customer data
- Anonymous “I worked at a bank” with no checkable source *and* no attestation
- LLM-invented COBOL snippets presented as production patterns
- Drive-by README essays that do not add a record

## How to add a claim

1. Open an issue (template: New claim).
2. Add the source(s) to `sources/catalog.yaml` first.
3. Copy an existing file in `claims/` and change the `id` (kebab-case, unique).
4. Every `sources[].id` must exist in the catalog.
5. If published numbers disagree, `status: contested` and fill `conflicts`.
6. Run `python scripts/validate.py`.
7. PR. In the body, quote the exact sentence you verified in each source.

## How to review

A review is not a thumbs-up. Open the URLs. For each source, record:

- Did the source actually state this, or is it a paraphrase?
- Date and population (survey of vendors? of banks? of “COBOL experts”?)
- Funding / vendor interest (Micro Focus commissioned Vanson Bourne; say so)
- Whether a more recent primary supersedes it

Then add a `reviewers` entry:

```yaml
reviewers:
  - name: Your Name
    github: yourhandle
    date: 2026-09-01
    verdict: confirm   # confirm | contest | insufficient
    notes: >
      Reuters graphic states 95% ATM swipes; it cites IBM/Micro Focus/
      Celent/Accenture as a bundle. No method visible on the graphic.
```

If you contest, also add a `conflicts` note and set `status: contested`.

## Practitioner attestation (idioms)

Idioms require `attestation.role` and `attestation.years_approx`. You do **not** need to name an employer. You do need to be a real person with a GitHub account. Fake-practice PRs will be closed.

## Local checks

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
python -m pytest -q
```

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). No vendor-bashing as a substitute for citations. No age jokes about practitioners — they are the knowledge this ledger is trying to keep.
