#!/usr/bin/env python3
"""Verify the saved complete run only; no native mathematics is invoked."""
import hashlib
import json
import os
from pathlib import Path

OUT = Path(os.environ["RUNNER_TEMP"]) / "isp-r150-final-publication-only"
RESULTS, RECOVERY = OUT / "results", OUT / "recovery"
EXPECTED = {
    "saturated-third-global-pipeline-receipt.json": "59916ee24c253ab3324ff7ecd2130846191de50eb7c66e12df5a5ef48825d032",
    "actions-outcome.json": "568a1b658c5d4318ae8b793e07166fd1cdf6f54baec4ed2796aabab6f3463233",
    "actions-source.json": "5236ff6139d426688f8179ac63799199ba2f74e5e8c1e3d31109d2260b4bbbdd",
    "recovery-manifest.json": "01d1df02c14d9bd5a30213db087e8d6e437a06babc66af9c1ed6a61cb688117d",
    "certificate-manifest.json": "592bd477348cbbe62ff091d2373e810fd6af26d875cd9a5fca9f09e49814e8a5",
    "text-recovery-manifest.json": "a18ff2a61ce3fdf170613142150a5d91c0c8fb13b0504d005ebda21091dba672",
}
def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()

for name, expected in EXPECTED.items():
    assert digest(RESULTS / name) == expected, name
source = json.loads((RESULTS / "actions-source.json").read_text())
assert source["source_commit"] == "88be0c86d8924b4874e16b51c26732588696a5e3"
assert str(source["run_id"]) == "43674463008" and str(source["run_attempt"]) == "1"
pipeline = json.loads((RESULTS / "saturated-third-global-pipeline-receipt.json").read_text())
assert pipeline["status"] == "completed"
assert pipeline["outcome"] == "all-nine-original-p6-complete"
assert pipeline["completedOriginalTargetLabels"] == list(range(2, 11))
assert pipeline["actualFinalSourceCostsBySlot"] == [1339] * 9
for key in ("fullOriginalAllNineMod887503681IdentityVerified",
            "allNineOriginalSeventeenIdentitiesVerified",
            "allSixAuxiliaryOriginalIdentitiesVerified",
            "full315FinalReconciliationVerified",
            "finitePositiveSourceBudgetsVerified", "finite_budget_verified",
            "sameQ1IntegerCarryVerified"):
    assert pipeline[key] is True, key
assert pipeline["oldLocalPagesRecomputed"] is False
assert pipeline["characteristicZeroIdentityAsserted"] is False
manifest = json.loads((RESULTS / "recovery-manifest.json").read_text())
names = set()
for item in manifest["files"]:
    rel = Path(item["file"])
    assert not rel.is_absolute() and ".." not in rel.parts
    p = RECOVERY / rel
    assert p.is_file() and not p.is_symlink()
    assert p.stat().st_size == item["bytes"]
    assert digest(p) == item["sha256"], str(rel)
    names.add(str(rel))
assert len(names) == 623
assert sum(x["bytes"] for x in manifest["files"]) == 3746395040
assert {str(p.relative_to(RECOVERY)) for p in RECOVERY.rglob("*") if p.is_file()} == names
receipt = {"format": "r150-complete-global-publication-only-verification-v1",
           "status": "verified", "mathematicsRerun": False,
           "originatingRun": "43674463008", "originatingAttempt": "1",
           "mathematicalSource": source["source_commit"],
           "all623ActualRecoveryFilesVerified": True,
           "originalRecoveryBytes": 3746395040,
           "allNineOriginalIdentitiesVerified": True,
           "actualFinalSourceCosts": [1339] * 9,
           "maximumAdvertisedBatchBytes": 400000000,
           "sourceReceiptsSHA256": EXPECTED}
pub = RESULTS / "publication"
pub.mkdir(exist_ok=True)
(pub / "publication-only-restoration.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt), flush=True)
