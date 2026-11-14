#!/usr/bin/env python3
"""Compose full original leaves after certified SAME true-moment refinement.

The old composition checker retains its exact full-cover, all-mode, mean,
positivity and physical-unit checks. This entry adds the explicit R80 identity:
old enclosures first reproduced, then identical real integrals and endpoint
formulas narrowed. It never labels new interval values bitwise equal to old.
Only standard-library exact Fraction arithmetic is used.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import ast
import hashlib
import json
from pathlib import Path
import types


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def same_true_candidate(part, data):
    if part.get("original_total_moments_and_bubble_enclosures_identical") is True:
        return True
    if (part.get("original_enclosures_bitwise_checked_before_refinement") is not True
            or data["source_hashes"].get("tail_outer_capped_moment_replay.py") !=
            "d4bb3fd3c8c1cafb901ce6bbe5a1ceba707a42f8b9f0b578d34e5117799c2980"):
        return False
    report = part.get("same_true_moment_refinement", {})
    flags = ("original_candidate_enclosures_bitwise_checked_before_refinement",
             "identical_true_integral_definition_and_shared_two_jets",
             "actual_capped_source_and_warp_retained", "no_true_integral_midpoint_selection")
    if not all(report.get(key) is True for key in flags):
        return False
    certificate = Path(report["certificate"])
    if (sha(certificate) != report["certificate_sha256"]
            or data["input_hashes"].get(str(certificate)) != report["certificate_sha256"]):
        return False
    meta = json.loads(certificate.read_text())
    if (not all(meta["gates"].values()) or meta["cell"] != 0
            or meta["segment"] != part["segment"]
            or meta["counts"]["original_leaves"] != part["panels"]
            or report["complete_refined_integral_count"] != part["panels"]
            or meta["source_hashes"].get("tail_outer_capped_true_moments.py") !=
            "88ca736fe426fc3aa9d7f09507aba4f11dd80ea7100dcbec346df6d542b53c6b"):
        return False
    return all(data["input_hashes"].get(path) == checksum
               for path,checksum in meta["input_hashes"].items())


def main():
    original = Path(__file__).with_name("tail_outer_combine_complete_audits.py")
    raw = original.read_text()
    if sha(original) != "32a9f0c5de34fa230bd7c9392a09b8080dff323a5194f8ee1d8109bbb34656a1":
        raise ValueError("The original complete same-candidate composition checker changed")
    edits = [
        ('not part["original_total_moments_and_bubble_enclosures_identical"]',
         'not _same_true_candidate(part, data)'),
        ('source_sha256=sha(__file__),',
         'source_sha256=sha(_entry_source), original_checker_sha256=sha(__file__),'),
        ('origin="Same original candidate complete finite-Horner/full-J/R77 audit",',
         'origin="Same original candidate complete finite-Horner/full-J/R77 audit, with certified identical true-moment refinement where recorded",'),
    ]
    changed = raw
    for before,after in edits:
        if changed.count(before) != 1:
            raise ValueError("A narrow complete-composition anchor changed")
        changed = changed.replace(before,after)
    reverse = changed
    for before,after in reversed(edits):
        reverse = reverse.replace(after,before)
    if reverse != raw:
        raise AssertionError("The original full-leaf checker was not exactly recovered")
    ast.parse(changed)
    module = types.ModuleType("tail_outer_compose_same_true_moments")
    module.__file__ = str(original)
    module._entry_source = str(Path(__file__).resolve())
    module._same_true_candidate = same_true_candidate
    exec(compile(changed,str(original),"exec"),module.__dict__)
    module.__doc__ = __doc__
    module.main()


if __name__ == "__main__":
    main()
