#!/usr/bin/env python3
"""Retain a physical-polynomial sample across a checked fixed-view conversion.

The original interior-audit input identity is preserved.  Equal complete raw
states, physical polynomial chunks, core, metric and charts are checked before
the original physical witness is mapped to the fixed numerical chart.  The
output is a one-point comparison grid for the existing geometry-plan adapter.
It does not replace either polynomial evaluation, solve a BVP, or certify a
continuous curvature bound.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path

import numpy as np
from root_neck_chart import NeckChart


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('accepted-reference', 'accepted-raw', 'fixed-reference',
                 'fixed-raw', 'fixed-report', 'accepted-tail', 'interior-audit',
                 'out'):
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh witness bridge')
    inputs = [args.accepted_reference, args.accepted_raw, args.fixed_reference,
              args.fixed_raw, args.fixed_report, args.accepted_tail,
              args.interior_audit]
    hashes = {str(p): sha(p) for p in inputs}
    old, oldraw, fixed, raw, report, tail, audit = map(read, inputs)
    checks = []

    def check(name, passed):
        if not passed:
            raise ValueError('Fixed-view physical witness bridge failed: '+name)
        checks.append(dict(name=name, passed=True))

    check('both_primary_states_formally_accepted',
          all(d.get('solver_success') and not d.get('audit_pending', True)
              and d['config'].get('actual_nonlinear_tail') for d in (old, fixed)))
    check('both_raw_states_formally_accepted',
          all(d.get('solver_success') and d.get('raw_collocation_only')
              and d.get('physical_surface') is False for d in (oldraw, raw)))
    check('primary_raw_links_match',
          old['raw_collocation_checkpoint']['sha256'] == sha(args.accepted_raw)
          and fixed['raw_collocation_checkpoint']['sha256'] == sha(args.fixed_raw))
    check('fixed_conversion_report_inputs_match',
          all(report['source_sha256'].get(str(p)) == sha(p)
              for p in (args.accepted_reference, args.accepted_raw, args.accepted_tail)))
    check('fixed_conversion_report_outputs_match',
          report['output']['sha256'] == sha(args.fixed_reference)
          and report['raw_output']['sha256'] == sha(args.fixed_raw))
    for name in ('complete_H_bitwise_equal', 'raw_x_y_cubic_unchanged',
                 'physical_quintics_unchanged', 'all_core_coefficients_unchanged',
                 'gauge_unchanged', 'original_numerical_reference_unchanged',
                 'eight_physical_data_unchanged', 'rms_array_bitwise_equal'):
        check('original_report_'+name, report.get(name) is True)
    check('fixed_conversion_did_not_solve_or_start_tail',
          report.get('nonlinear_solve_run') is False
          and report.get('tail_worker_started') is False)
    physical_keys = ('frozen_profile', 'physical_tail_parameters', 'physical_tail_cut',
                     'angular_chart', 'chart_reference_coefficients',
                     'chart_reference_frequencies', 'gauge_amplitude', 'meridian_length',
                     'physical_port_sha256', 'core', 'numerical_meridian_chart',
                     'mesh', 'pp_coefficient_chunks', 'array_format', 'modes', 'nodes')
    for key in physical_keys:
        check('complete_primary_identity_'+key,
              canonical(old[key]) == canonical(fixed[key]))
    M = int(fixed['modes'])
    for label, rec, state in (('accepted', oldraw, old), ('fixed', raw, fixed)):
        for a, b in (('profile', 'frozen_profile'), ('gauge', 'gauge_amplitude'),
                     ('physical_tail_parameters', 'physical_tail_parameters'),
                     ('physical_tail_cut', 'physical_tail_cut'),
                     ('reference_coefficients', 'chart_reference_coefficients'),
                     ('reference_frequencies', 'chart_reference_frequencies')):
            check(label+'_raw_'+a,
                  canonical(rec['identity'][a]) == canonical(state[b]))
        check(label+'_raw_chart', rec['identity']['numerical_reference_knots']
              == state['numerical_meridian_chart']['reference_t'])

    def raw_array(path, record, name):
        descriptor = record['arrays'][name]
        check(str(path)+':'+name+':dtype', descriptor['dtype'] == 'float64')
        flat = np.empty(int(np.prod(descriptor['shape'])), dtype=np.float64)
        at = 0
        for part in descriptor['chunks']:
            check(str(path)+':'+name+':chunk_order',
                  part['first'] == at and Path(part['file']).name == part['file'])
            file = path.parent/part['file']
            check(str(file)+':sha', sha(file) == part['sha256'])
            hashes[str(file)] = sha(file)
            data = np.load(io.BytesIO(gzip.decompress(file.read_bytes())), allow_pickle=False)
            check(str(file)+':shape', data.dtype == np.float64
                  and data.shape == (part['count'],))
            flat[at:at+len(data)] = data
            at += len(data)
        check(str(path)+':'+name+':complete_finite',
              at == len(flat) and np.isfinite(flat).all())
        return flat.reshape(descriptor['shape'])

    old_arrays, arrays = {}, {}
    for name in ('x', 'y', 'cubic', 'rms', 'p'):
        old_arrays[name] = raw_array(args.accepted_raw, oldraw, name)
        arrays[name] = raw_array(args.fixed_raw, raw, name)
        if name != 'p':
            check('raw_'+name+'_same_complete_binary64',
                  old_arrays[name].shape == arrays[name].shape
                  and old_arrays[name].tobytes() == arrays[name].tobytes())
    check('all_retained_parameter_bits_equal',
          old_arrays['p'].shape == (M+3,) and arrays['p'].shape == (M,)
          and old_arrays['p'][:M].tobytes() == arrays['p'].tobytes())
    check('all_original_raw_nodes_retained',
          arrays['x'].shape == (fixed['nodes'],)
          and arrays['y'].shape == (3*M+1, fixed['nodes'])
          and arrays['cubic'].shape == (4, fixed['nodes']-1, 3*M+1)
          and arrays['x'][0] == 0 and arrays['x'][-1] == 1
          and np.all(np.diff(arrays['x']) > 0))
    H = -float(fixed['gauge_amplitude'])*arrays['y'][2*M+1:, -1]
    check('complete_tail_height_bits_equal',
          H.shape == (M,)
          and H.tobytes() == np.asarray(tail['request']['height'], dtype=np.float64).tobytes())
    check('original_tail_full_jacobian_audit_retained',
          tail['request'].get('jacobian') and tail['request'].get('audit')
          and tail['response'].get('converged') and tail['response'].get('audit')
          and tail['response']['residual'] <= tail['config']['solveTolerance']
          and len(tail['response']['heightJetJacobian']) == (3*M+2)*M)
    at = 0
    for item in fixed['pp_coefficient_chunks']:
        check('physical_quintic_chunk_order_'+str(at),
              item['state_first'] == at and Path(item['file']).name == item['file'])
        file = args.fixed_reference.parent/item['file']
        check(str(file)+':physical_quintic',
              file.stat().st_size == item['bytes'] and sha(file) == item['sha256']
              and report['source_sha256'].get(str(file)) == item['sha256'])
        hashes[str(file)] = sha(file)
        at = item['state_last_exclusive']
    check('all_physical_quintic_states_and_mean_retained', at == 3*M+1)
    check('original_audit_primary_identity_retained',
          audit['input_sha256'] == sha(args.accepted_reference)
          and audit['modes'] == M)
    check('audit_full_mean_rule', audit['config']['mean_angular'] == max(512,16*(3*M+1)))
    check('audit_physical_metric_identity', audit['physical_metric_sha256']
          == hashlib.sha256(json.dumps(fixed['frozen_profile'],sort_keys=True).encode()).hexdigest())
    here = Path(__file__).resolve().parent
    sources = [Path(__file__), here/'root_neck_chart.py',
               here/'root_actual_freeze_design_view.py',
               here/'strong_interior_jet_fullmean_audit.py', here/'strong_interior_jet_audit.py']
    check('audit_actual_source_identity', sha(sources[3]) == audit['source_sha256']
          and sha(sources[4]) == audit['config']['original_audit_source_sha256'])
    conversion_sources = [(p,h) for p,h in report['source_sha256'].items()
                          if Path(p).name == 'root_actual_freeze_design_view.py']
    check('conversion_actual_source_identity',
          len(conversion_sources) == 1 and conversion_sources[0][1] == sha(sources[2]))
    hashes.update({str(p): sha(p) for p in sources})
    chart_record = fixed['numerical_meridian_chart']
    chart = NeckChart(chart_record['reference_t'], chart_record['physical_s'])
    witness = audit['top']['kappa']
    s, eta = float(witness['s']), float(witness['psi'])
    N = int(audit['config']['angular'])
    angular_index = int(round(eta*N/(2*np.pi))) % N
    check('exact_saved_angular_witness_in_grid',
          abs(angular_index*2*np.pi/N-eta) < 1e-13)
    check('physical_witness_within_original_chart', chart.s[0] <= s <= chart.s[-1])
    t = float(chart.inverse(np.asarray([s]))[0])
    mismatch = abs(float(chart.evaluate(np.asarray([t]))[0][0])-s)
    check('physical_numerical_witness_roundtrip', mismatch < 1e-12)
    result = dict(scope=__doc__, finished=True,
        accepted_primary=str(args.accepted_reference),
        accepted_primary_sha256=sha(args.accepted_reference),
        fixed_primary=str(args.fixed_reference), fixed_primary_sha256=sha(args.fixed_reference),
        original_audit=str(args.interior_audit), original_audit_sha256=sha(args.interior_audit),
        original_audit_input_sha256=audit['input_sha256'],
        conversion_report=str(args.fixed_report), conversion_report_sha256=sha(args.fixed_report),
        all_physical_polynomials_metric_core_and_charts_identical=True,
        comparison_grid_only=True, numerical_t=[t], angular=N,
        known_reference_witnesses=[dict(radial_index=0,angular_index=angular_index,eta=eta,
            physical_s=s,source_polynomial_sample=witness['value'],source_witness=witness,
            source_audit_input_sha256=audit['input_sha256'],
            same_physical_field_through_explicit_fixed_view_bridge=True)],
        original_complete_mean_angular=audit['config']['mean_angular'],
        witness_physical_roundtrip_error=mismatch,
        checks=checks, checks_count=len(checks), all_checks_passed=True,
        source_and_input_sha256=hashes,
        limitations=['The physical quintic sample keeps the original audit identity.',
                     'The next geometry plan uses the original raw cubic; its value does not replace this quintic audit.',
                     'No new solve, tail response, interval certification or continuous curvature bound.'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),checks=len(checks),
                         numerical_t=t,angular=N,angular_index=angular_index)),flush=True)


if __name__ == '__main__':
    main()
