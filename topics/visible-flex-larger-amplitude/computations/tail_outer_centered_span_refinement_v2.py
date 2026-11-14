"""Whole-segment unchanged-candidate audit using finite integer Horner.

Only the same-polynomial enclosure and recorded provenance are replaced.
The original span/root/J conditions and streaming recovery remain unchanged.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import ast
import hashlib
from pathlib import Path

from tail_outer_centered_quartic_fields_v2 import (
    weighted_panel_fields, rational_identity_checks)


def main():
    here = Path(__file__).parent
    template = here/"tail_outer_substage_span_refinement.py"
    original = template.read_text()
    expected = "85bf30e818e7ab92107a5f5a537225afb9273877327bf6e0092b303b01a1b5d8"
    if hashlib.sha256(original.encode()).hexdigest() != expected:
        raise ValueError("The original continuous audit changed")
    edits = [
        ('source_names = (Path(__file__).name, "tail_outer_general_mean_bounds.py",',
         'source_names = (Path(__file__).name, "tail_outer_centered_span_refinement_v2.py",\n'
         '        "tail_outer_centered_quartic_fields_v2.py",\n'
         '        "tail_outer_centered_quartic_fields.py", "tail_outer_general_mean_bounds.py",'),
        ('same_exact_candidate_and_background=True, new_source_integrals=0,',
         'same_exact_candidate_and_background=True, new_source_integrals=0,\n'
         '        same_quartic_finite_horner_enclosure=FINITE_HORNER_PROVENANCE,')]
    source = original
    for before, after in edits:
        if source.count(before) != 1:
            raise ValueError("The continuous-audit replacement is not unique")
        source = source.replace(before, after)
    recovered = source
    for before, after in reversed(edits):
        recovered = recovered.replace(after, before)
    if recovered != original:
        raise AssertionError("The original continuous audit is not recoverable")
    ast.parse(source)
    provenance = dict(scope=__doc__, original_continuous_audit_sha256=expected,
        adapter_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        enclosure_helper_sha256=hashlib.sha256(
            (here/"tail_outer_centered_quartic_fields_v2.py").read_bytes()).hexdigest(),
        compiled_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        exact_identity_and_finiteness_checks=rational_identity_checks(),
        original_candidate_g_H_moments_and_full_mean_J_gates_unchanged=True,
        substitutions=[dict(before=a, after=b) for a, b in edits])
    namespace = dict(__file__=str(template), __name__="tail_finite_horner_span",
                     FINITE_HORNER_PROVENANCE=provenance)
    exec(compile(source, str(template)+":finite-integer-Horner", "exec"), namespace)
    namespace["weighted_panel_fields"] = weighted_panel_fields
    namespace["main"]()


if __name__ == "__main__":
    main()
