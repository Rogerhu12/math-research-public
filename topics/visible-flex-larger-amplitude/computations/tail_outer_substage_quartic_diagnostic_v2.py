"""Run the preserved six-case diagnostic with finite integer Horner only.

No candidate, background, mean, derivative or residual formula changes.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import ast
import hashlib
from pathlib import Path


def main():
    template = Path(__file__).with_name("tail_outer_substage_quartic_diagnostic.py")
    original = template.read_text()
    expected = "43c4b0b2cf4f90f3e17ddc7bf2c34db1578115765279962ed81b9b2e1d07537a"
    if hashlib.sha256(original.encode()).hexdigest() != expected:
        raise ValueError("The preserved six-case diagnostic changed")
    edits = [
        ("from tail_outer_centered_quartic_fields import (",
         "from tail_outer_centered_quartic_fields_v2 import ("),
        ('Path(__file__).name, "tail_outer_centered_quartic_fields.py",',
         'Path(__file__).name, "tail_outer_centered_quartic_fields.py",\n'
         '            "tail_outer_centered_quartic_fields_v2.py",\n'
         '            "tail_outer_substage_quartic_diagnostic_v2.py",'),
        ('exact_same_candidate_and_complete_mean=True,',
         'exact_same_candidate_and_complete_mean=True,\n'
         '        finite_integer_horner_replacement=FINITE_HORNER_PROVENANCE,')]
    source = original
    for before, after in edits:
        if source.count(before) != 1:
            raise ValueError("The finite-Horner diagnostic anchor is not unique")
        source = source.replace(before, after)
    recovered = source
    for before, after in reversed(edits):
        recovered = recovered.replace(after, before)
    if recovered != original:
        raise AssertionError("The original diagnostic was not exactly recoverable")
    ast.parse(source)
    provenance = dict(original_diagnostic_sha256=expected,
        adapter_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        compiled_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        candidate_and_all_R64_full_J_gates_unchanged=True,
        substitutions=[dict(before=a, after=b) for a, b in edits])
    namespace = dict(__file__=str(template), __name__="tail_finite_horner_diagnostic",
                     FINITE_HORNER_PROVENANCE=provenance)
    exec(compile(source, str(template)+":finite-integer-Horner", "exec"), namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()
