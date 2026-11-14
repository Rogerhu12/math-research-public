#!/usr/bin/env python3
"""Exact weighted-tail sums of two saved Float64 core records, not an error bound.

The complete stored coefficients are converted by their exact binary rational
values. No uncomputed Fourier modes, continuous solution or metric truncation
error is bounded by these design diagnostics.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def exact_record(value):
    number = float(value)
    rounded = Fraction.from_float(number)
    return dict(numerator=str(value.numerator), denominator=str(value.denominator),
                nearest_float=number,
                lower_float=math.nextafter(number, -math.inf) if rounded > value else number,
                upper_float=math.nextafter(number, math.inf) if rounded < value else number)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--coarse', type=Path, required=True)
    parser.add_argument('--fine', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    coarse, fine = map(read, (args.coarse, args.fine))
    for a in (coarse, fine):
        if (not a.get('solver_success') or a.get('audit_pending', True)
                or not a['config'].get('actual_nonlinear_tail')
                or len(a['core']['coefficients']) != a['modes']
                or a['core']['frequencies'] != list(range(2, 2*a['modes']+1, 2))
                or not all(math.isfinite(x) for x in a['core']['coefficients'])):
            raise ValueError('Two complete accepted finite core records are required')
    common = ('gauge_amplitude', 'frozen_profile', 'angular_chart',
              'chart_reference_coefficients', 'chart_reference_frequencies',
              'physical_tail_parameters', 'physical_tail_cut')
    if any(coarse[name] != fine[name] for name in common):
        raise ValueError('The two records differ in physical g or their material coordinate')
    rows = []
    for threshold in (16, 24, 32, 40, 48, 58):
        values = [sum((m*m-1)*abs(Fraction.from_float(c))
                      for m, c in zip(a['core']['frequencies'], a['core']['coefficients'])
                      if m >= threshold) for a in (coarse, fine)]
        rows.append(dict(actual_frequency_lower=threshold,
                         coarse=exact_record(Fraction(values[0])),
                         fine=exact_record(Fraction(values[1])),
                         coarse_div_fine=exact_record(Fraction(values[0])/values[1]) if values[1] else None))
    result = dict(scope=__doc__, formula='sum_{actual even frequency m >= threshold} (m*m-1)*abs(c_m)',
        source_sha256={str(path): digest(path) for path in (Path(__file__), args.coarse, args.fine)},
        coarse_modes=coarse['modes'], fine_modes=fine['modes'],
        coarse_core=coarse['core'], fine_core=fine['core'],
        all_stored_coefficients_consumed=True, exact_arithmetic_of_saved_binary_values=True,
        same_physical_g_and_material_chart_fields=list(common), rows=rows,
        physical_truncation_error_or_infinite_tail_bound_claim=False, new_solver_run=False)
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(out=str(args.out), sha256=digest(args.out), rows=len(rows),
                          exact_saved_value_sums_only=True)), flush=True)


if __name__ == '__main__':
    main()
