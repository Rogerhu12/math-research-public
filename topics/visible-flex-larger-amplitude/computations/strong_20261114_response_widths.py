#!/usr/bin/env python3
"""Select explicit finite-difference widths while keeping full/half gates.

This composes with the complete loop-and-finite-bridge response entry. The
collocation matrix, complete tail derivative, field layout, backward-error
checks and 2e-4 physical full/half agreement gate are unchanged. A requested
width is only a numerical differentiation choice, not a passed derivative.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
from pathlib import Path
import sys

import strong_20261114_loop_control_response as loop


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--response-relative-width', action='append', default=[])
    own, rest = parser.parse_known_args()
    widths = {}
    for item in own.response_relative_width:
        name, value = item.split('=', 1)
        value = float(value)
        if name in widths or not math.isfinite(value) or not 0 < value < .01:
            raise ValueError('Use distinct positive, finite differentiation widths below .01')
        widths[name] = value
    if '--response-fields' not in rest:
        raise ValueError('Declare all response fields explicitly')
    fields = set(rest[rest.index('--response-fields') + 1].split(','))
    if not set(widths) <= fields:
        raise ValueError('A differentiation width names an unrequested field')
    previous = loop.laws.transformed_source

    def transform():
        source, provenance = previous()
        before = 'width=2e-6*max(.1,abs(original));forcings=[]'
        after = ('width=' + repr(dict(sorted(widths.items()))) +
                 '.get(field,2e-6)*max(.1,abs(original));forcings=[]')
        if source.count(before) != 1:
            raise ValueError('The original differentiation-width site changed')
        changed = source.replace(before, after, 1)
        ast.parse(changed)
        record = dict(provenance)
        record['source_sha256'] = {**provenance['source_sha256'],
            str(Path(__file__).resolve()): hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
        record['transformed_source_sha256'] = hashlib.sha256(changed.encode()).hexdigest()
        record['explicit_transforms'] = list(provenance['explicit_transforms']) + [
            dict(before=before, after=after, replacements=1)]
        record['requested_response_widths'] = dict(
            relative_factors=widths, default_relative_factor=2e-6,
            width_formula='factor * max(.1, abs(current_physical_control))',
            original_full_half_gate=2e-4, original_backward_checks_preserved=True,
            derivative_or_nonlinear_solution_not_yet_claimed=True)
        return changed, record

    old_argv = sys.argv
    sys.argv = [old_argv[0], *rest]
    loop.laws.transformed_source = transform
    try:
        loop.main()
    finally:
        loop.laws.transformed_source = previous
        sys.argv = old_argv


if __name__ == '__main__':
    main()
