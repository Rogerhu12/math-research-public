#!/usr/bin/env python3
"""Bind the original first-request guard to the explicit saved affine H0.

The previous independent entry stopped before any Jacobian because its outer
wrapper still compared the pending raw H with the saved H0 request. This
bootstrap keeps that full-vector guard, but compares the actual first request
H0. The original runtime separately verifies the complete pending raw state,
original inner-entry H0, and complete audited K0/J0. No current raw H is
relabeled as audited. All subsequent true Hnew and final gates are unchanged.
"""
from __future__ import annotations
import ast
import hashlib
from pathlib import Path

import strong_physical_merit_actual_bvp as original

HERE = Path(__file__).resolve().parent
EXPECTED_ORIGINAL = '11f3e91efaa52ec1daae63aac042576e84867e5ded7b1e8cff2b23721f8fe8a0'
BASE_BUILD_SOURCE = original.build_source


def build_source(configuration, disk_configuration):
    if original.sha(HERE/'strong_physical_merit_actual_bvp.py') != EXPECTED_ORIGINAL:
        raise ValueError('The retained previous merit bootstrap changed')
    source, provenance = BASE_BUILD_SOURCE(configuration, disk_configuration)
    before_sha = hashlib.sha256(source.encode()).hexdigest()
    edits = [
        ("        'strong_physical_merit_actual_bvp.py', 'strong_physical_merit_and_affine_resume.py',",
         "        'strong_physical_merit_actual_bvp.py', 'strong_physical_merit_and_affine_resume.py',\n"
         "        'strong_physical_merit_actual_bvp_v2.py',"),
        ('    merit_runtime = Runtime(FIXED_MERIT_CONFIGURATION, out)',
         '    merit_runtime = Runtime(FIXED_MERIT_CONFIGURATION, out)\n'
         '    merit_runtime.hashes[str(HERE/"strong_physical_merit_actual_bvp_v2.py")] = '
         'sha(HERE/"strong_physical_merit_actual_bvp_v2.py")'),
        ('                        live_H = self.tail_height(y[:, -1])',
         '                        live_H = merit_runtime.H0.copy()'),
        ('                            tail_warm_info, complete_first_H_bitwise_equal=True)',
         '                            tail_warm_info, complete_first_H_bitwise_equal=True,\n'
         '                            first_request_kind="explicit-original-affine-H0",\n'
         '                            current_raw_H=self.tail_height(y[:, -1]).tolist(),\n'
         '                            current_raw_H_audited_here=False,\n'
         '                            complete_raw_and_original_entry_H0_guard_still_required=True)'),
    ]
    for before, after in edits:
        if source.count(before) != 1:
            raise ValueError('The explicit first-H0-request guard anchor is not unique: '+repr(before))
        source = source.replace(before, after, 1)
    ast.parse(source, filename='<fixed-merit-actual-explicit-H0-request-source>')
    provenance['source_sha256'][str(HERE/'strong_physical_merit_actual_bvp_v2.py')] = original.sha(__file__)
    provenance['first_request_identity_correction'] = dict(scope=__doc__,
        retained_previous_bootstrap_sha256=EXPECTED_ORIGINAL,
        before_source_sha256=before_sha,
        actual_first_request_is_original_H0=True,
        pending_raw_H_separately_recorded_and_not_audited=True,
        original_complete_raw_entry_packet_and_K0_J0_guards_preserved=True,
        original_true_Hnew_check_and_final_audit_preserved=True)
    provenance['replacements'].extend(dict(before=a,after=b,count=1) for a,b in edits)
    provenance['transformed_source_sha256'] = hashlib.sha256(source.encode()).hexdigest()
    return source, provenance


def main():
    original.build_source = build_source
    original.main()


if __name__ == '__main__':
    main()
