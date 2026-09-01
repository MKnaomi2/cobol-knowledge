#!/usr/bin/env python
"""Validate COBOL Knowledge ledger records against schema and cross-refs."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schema"
CLAIMS_DIR = ROOT / "claims"
IDIOMS_DIR = ROOT / "idioms"
CATALOG_PATH = ROOT / "sources" / "catalog.yaml"


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def iter_yaml(directory: Path):
    if not directory.exists():
        return
    for path in sorted(directory.glob("*.yaml")):
        yield path, load_yaml(path)


def main() -> int:
    errors: list[str] = []
    claim_schema = load_json(SCHEMA_DIR / "claim.schema.json")
    source_schema = load_json(SCHEMA_DIR / "source.schema.json")
    idiom_schema = load_json(SCHEMA_DIR / "idiom.schema.json")
    claim_v = Draft202012Validator(claim_schema)
    source_v = Draft202012Validator(source_schema)
    idiom_v = Draft202012Validator(idiom_schema)

    catalog = load_yaml(CATALOG_PATH)
    for err in source_v.iter_errors(catalog):
        errors.append(f"sources/catalog.yaml: {err.message}")

    catalog_ids = {row["id"] for row in catalog.get("sources", []) if isinstance(row, dict) and "id" in row}
    if len(catalog_ids) != len(catalog.get("sources", [])):
        errors.append("sources/catalog.yaml: duplicate or missing source ids")

    claim_ids: set[str] = set()
    n_claims = 0
    for path, data in iter_yaml(CLAIMS_DIR):
        n_claims += 1
        rel = path.relative_to(ROOT).as_posix()
        if not isinstance(data, dict):
            errors.append(f"{rel}: not a mapping")
            continue
        for err in claim_v.iter_errors(data):
            errors.append(f"{rel}: {err.message} ({'/'.join(str(p) for p in err.path)})")
        cid = data.get("id")
        if cid:
            if cid in claim_ids:
                errors.append(f"{rel}: duplicate claim id {cid}")
            claim_ids.add(cid)
            if path.stem != cid:
                errors.append(f"{rel}: filename stem must match id '{cid}'")
        for src in data.get("sources") or []:
            sid = src.get("id")
            if sid and sid not in catalog_ids:
                errors.append(f"{rel}: source id '{sid}' not in catalog")
        status = data.get("status")
        reviewers = data.get("reviewers") or []
        conflicts = data.get("conflicts") or []
        if status == "reviewed" and not reviewers:
            errors.append(f"{rel}: status=reviewed requires at least one reviewer")
        if status == "contested" and not conflicts:
            errors.append(f"{rel}: status=contested requires conflicts[]")
        if status == "reviewed":
            verdicts = {r.get("verdict") for r in reviewers}
            if verdicts and verdicts <= {"contest", "insufficient"}:
                errors.append(f"{rel}: reviewed claim has no confirming reviewer")
        if data.get("kind") == "quantitative":
            values = data.get("values") or []
            if not values:
                errors.append(f"{rel}: quantitative claims need values[]")

    n_idioms = 0
    for path, data in iter_yaml(IDIOMS_DIR):
        n_idioms += 1
        rel = path.relative_to(ROOT).as_posix()
        if not isinstance(data, dict):
            errors.append(f"{rel}: not a mapping")
            continue
        for err in idiom_v.iter_errors(data):
            errors.append(f"{rel}: {err.message}")
        for src in data.get("sources") or []:
            sid = src.get("id")
            if sid and sid not in catalog_ids:
                errors.append(f"{rel}: source id '{sid}' not in catalog")

    print(f"catalog sources: {len(catalog_ids)}")
    print(f"claims: {n_claims}")
    print(f"idioms: {n_idioms}")
    if errors:
        print(f"FAIL ({len(errors)} errors)")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
