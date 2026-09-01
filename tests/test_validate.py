from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATE = ROOT / "scripts" / "validate.py"


def run_validate() -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(VALIDATE)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )


def test_seed_ledger_passes():
    proc = run_validate()
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "PASS" in proc.stdout


def test_reviewed_without_reviewers_fails(tmp_path, monkeypatch):
    # The seed must never mark reviewed with an empty reviewers list.
    import yaml

    claim_dir = ROOT / "claims"
    for path in claim_dir.glob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if data.get("status") == "reviewed":
            assert data.get("reviewers"), f"{path.name} is reviewed with no reviewers"
        if data.get("status") == "contested":
            assert data.get("conflicts"), f"{path.name} is contested with no conflicts"


def test_catalog_urls_are_http():
    import yaml

    catalog = yaml.safe_load((ROOT / "sources" / "catalog.yaml").read_text(encoding="utf-8"))
    for row in catalog["sources"]:
        assert row["url"].startswith("http"), row["id"]
