#!/usr/bin/env python3
"""Same continuous span audit with an intersected centered-quartic enclosure.

The frozen span-audit source, all mathematical gates, parameters and output
records are retained.  Only the global weighted_panel_fields callable is
replaced by an exact enclosure of the identical R48 polynomial intersected
with its original basis evaluation.  The height primitive is unchanged.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import ast
import hashlib
from pathlib import Path

from tail_outer_centered_quartic_fields import (
    weighted_panel_fields, rational_identity_checks)

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE/"tail_outer_substage_span_refinement.py"
EXPECTED = "85bf30e818e7ab92107a5f5a537225afb9273877327bf6e0092b303b01a1b5d8"


def main():
    original = TEMPLATE.read_text()
    if hashlib.sha256(original.encode()).hexdigest() != EXPECTED:
        raise ValueError("The original executed continuous audit source changed")
    before = 'source_names = (Path(__file__).name, "tail_outer_general_mean_bounds.py",'
    after = ('source_names = (Path(__file__).name, "tail_outer_centered_span_refinement.py",\n'
             '        "tail_outer_centered_quartic_fields.py", "tail_outer_general_mean_bounds.py",')
    marker = 'same_exact_candidate_and_background=True, new_source_integrals=0,'
    addition = ('same_exact_candidate_and_background=True, new_source_integrals=0,\n'
        '        same_quartic_interval_refinement=CENTERED_QUARTIC_ENCLOSURE,')
    if original.count(before) != 1 or original.count(marker) != 1:
        raise ValueError("The reversible same-enclosure metadata anchors changed")
    source = original.replace(before, after).replace(marker, addition)
    if source.replace(after, before).replace(addition, marker) != original:
        raise AssertionError("The original continuous audit is not recoverable exactly")
    ast.parse(source)
    record = dict(scope=__doc__, original_continuous_audit_sha256=EXPECTED,
        wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        enclosure_helper_sha256=hashlib.sha256(
            (HERE/"tail_outer_centered_quartic_fields.py").read_bytes()).hexdigest(),
        compiled_continuous_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        exact_identity_checks=rational_identity_checks(),
        original_all_mean_domain_residual_and_spectrum_gates_unchanged=True,
        original_candidate_endpoints_total_moments_bubble_and_H_unchanged=True,
        original_basis_K_and_Kx_intersected_not_discarded=True,
        substitutions=[dict(before=before, after=after), dict(before=marker, after=addition)])
    namespace = dict(__file__=str(TEMPLATE), __name__="tail_centered_same_quartic_audit",
                     CENTERED_QUARTIC_ENCLOSURE=record)
    exec(compile(source, str(TEMPLATE)+":centered-quartic-enclosure", "exec"), namespace)
    namespace["weighted_panel_fields"] = weighted_panel_fields
    namespace["main"]()


if __name__ == "__main__":
    main()
