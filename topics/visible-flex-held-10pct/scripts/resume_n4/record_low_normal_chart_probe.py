#!/usr/bin/env python3
"""Record only selected scalar outcomes of the low-angle-filter probe."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('result', 'parent-record', 'resource', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    a = p.parse_args()
    d = json.loads(a.result.read_text())
    parent = json.loads(a.parent_record.read_text())
    assert d['input_checkpoint_sha256'] == parent['input_checkpoint_sha256']
    assert d['physical_control_sha256'] == parent['physical_control_sha256']
    assert d['actual_q'] == parent['actual_q'] and d['gauge_q'] == parent['gauge_q']
    source = Path(d['source_root']) / 'probe_low_normal_angle_chart.py'
    assert sha(source) == d['script_sha256'] == sha(Path(__file__).with_name(source.name))
    assert d['helper_sha256'] == parent['executed_script_sha256']
    resource = json.loads(a.resource.read_text())
    assert resource['child_returncode'] == 0
    selected = {}
    for lam in sorted({r['homotopy'] for r in d['rows']}):
        rows = [r for r in d['rows'] if r['homotopy'] == lam]
        original = next(r for r in rows if r['chart'] == 'original')
        best = min(rows, key=lambda r: r['second_reference_jet']['20'])
        exact_lower = Fraction(1) - sum(
            Fraction.from_float(abs(x)) for x in best['literal_cosine_derivative_coefficients'])
        assert Fraction.from_float(best['chart_derivative_triangle_lower']) <= exact_lower
        selected[str(lam)] = dict(
            original_M20=original['second_reference_jet']['20'],
            best_M20=best['second_reference_jet']['20'],
            best_label=best['chart'],
            best_to_original_ratio=best['second_reference_jet']['20']/
                                   original['second_reference_jet']['20'],
            literal_best_derivative_cosine_coefficients={
                str(j+1): x for j,x in enumerate(best['literal_cosine_derivative_coefficients']) if x},
            literal_chart_derivative_lower=best['chart_derivative_triangle_lower'],
            literal_lower_checked_with_exact_binary_fractions=True)
    result = dict(
        scope='Supplementary read-only low-angle-frequency filters after the full normal chart worsened the tail. This input provides only small M20 improvements; no changed-chart BVP was started.',
        collector_sha256=sha(__file__), parent_record_sha256=sha(a.parent_record),
        executed_source=str(source), executed_source_sha256=d['script_sha256'],
        helper_source_sha256=d['helper_sha256'], result_sha256=sha(a.result),
        resource_sha256=sha(a.resource), input_checkpoint_sha256=d['input_checkpoint_sha256'],
        actual_q=d['actual_q'], gauge_q=d['gauge_q'], settings=d['settings'],
        physical_control_sha256=d['physical_control_sha256'], samples=d['samples'],
        compared_filter_orders='1, 2, 4, 8; raw coefficients and the whole table stay in scratch',
        selected_M20_diagnostics=selected, child_returncode=0,
        total_seconds=resource['seconds'],
        limitation='Finite sampled angular diagnostics; literal candidate coefficients define a numerical chart only. The lambda-one core is unsolved.')
    a.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(bytes=a.out.stat().st_size,sha256=sha(a.out))))


if __name__ == '__main__':
    main()
