#!/usr/bin/env python3
"""Use an explicit curvature-size design budget on the same compact rows.

Only the LP budget changes. Every cached full-field direction, original
local geometry formula, finite-piece length row and actual finite warm
evaluation stays in force. A stricter sampled budget is a design margin,
not a curvature, reach, residual, or nonlinear-solution certificate.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import inspect
import json
from pathlib import Path
import sys

import strong_20261114_compact_loop_screen as loop


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--compact-kappa-budget', type=float, required=True)
    own, rest = parser.parse_known_args()
    if not 0 < own.compact_kappa_budget <= 33.:
        raise ValueError('A positive design budget no looser than 33 is required')
    prior = loop.screen.optimize
    original = inspect.getsource(prior)
    before = 'kcap=33.0/cap'
    after = 'kcap=' + repr(own.compact_kappa_budget) + '/cap'
    if original.count(before) != 1:
        raise ValueError('The unique compact curvature-budget expression changed')
    source = original.replace(before, after, 1)
    ast.parse(source)
    # The finite-piece wrapper patches this module's linprog at run time;
    # retaining the original globals is required to consume those rows.
    namespace = prior.__globals__
    exec(compile(source, '<compact-explicit-curvature-budget>', 'exec'), namespace)
    loop.screen.optimize = namespace['optimize']
    previous_argv = sys.argv
    sys.argv = [previous_argv[0], *rest]
    try:
        loop.main()
        out = Path(sys.argv[sys.argv.index('--compact-out') + 1])
        record = json.loads(out.read_text())
        record['explicit_curvature_size_design_budget'] = {
            'scope': __doc__,
            'budget': own.compact_kappa_budget,
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'original_optimizer_source_sha256': hashlib.sha256(original.encode()).hexdigest(),
            'transformed_optimizer_source_sha256': hashlib.sha256(source.encode()).hexdigest(),
            'exact_reverse_recovers_original': source.replace(after, before, 1) == original,
            'geometry_samples_and_formulas_unchanged': True,
            'nonlinear_solution': False,
        }
        out.write_text(json.dumps(record, indent=2) + '\n')
    finally:
        sys.argv = previous_argv
        loop.screen.optimize = prior


if __name__ == '__main__':
    main()
