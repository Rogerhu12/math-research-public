#!/usr/bin/env python3
"""Compare two genuinely solved finite tails at one complete physical cut H.

The fine input adds zero high Fourier coefficients to the coarse H. All
non-mode/non-I/O parameters, common numerical sources and actual same-g
constructor evidence are checked. This is a finite-tail consistency check;
it does not accept the fine prefix, transfer the coarse audit or prove a
continuous/infinite tail bound. Jacobian blocks retain physical H units.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np

EXCLUDED = {'modes', 'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}
TANGENT_SHA = 'ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def comparison(old, fine):
    old, fine = np.asarray(old, dtype=np.float64), np.asarray(fine, dtype=np.float64)
    if old.shape != fine.shape or not np.isfinite(old).all() or not np.isfinite(fine).all():
        raise ValueError('A complete shared finite comparison block differs in shape/domain')
    difference = abs(fine-old)
    maximum = float(np.max(difference))
    index = np.unravel_index(int(np.argmax(difference)), difference.shape)
    return dict(shape=list(old.shape), max_absolute_difference=maximum,
        max_difference_index_zero_based=[int(k) for k in index],
        old_at_index=float(old[index]), fine_at_index=float(fine[index]),
        old_max_absolute=float(np.max(abs(old))), fine_max_absolute=float(np.max(abs(fine))),
        difference_l1=float(np.sum(difference)),
        max_row_sum_difference=float(np.max(np.sum(difference,axis=-1))) if old.ndim == 2 else maximum,
        relative_to_old_max=maximum/max(float(np.max(abs(old))),np.finfo(float).tiny))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('coarse-packet','fine-packet','physical-identity','source-topic','out'):
        p.add_argument('--'+name, type=Path, required=True)
    a = p.parse_args()
    packets = [read(a.coarse_packet), read(a.fine_packet)]
    old, fine = [packet['response'] for packet in packets]
    heights = [np.asarray(packet['request']['height'],dtype=np.float64) for packet in packets]
    m, n = map(len, heights)
    if not 1 <= m < n:
        raise ValueError('The fine complete physical spectrum must increase')
    for packet, response, H in zip(packets, (old, fine), heights):
        if (not packet['request'].get('jacobian') or not response.get('converged')
                or not np.isfinite(response['residual'])
                or response['residual'] > packet['config']['solveTolerance']
                or not np.isfinite(H).all() or packet['config']['modes'] != len(H)
                or not np.array_equal(response['checkpoint']['cutHeight'], H)):
            raise ValueError('A genuine complete-H/full-J finite-tail acceptance is missing')
    if heights[0].tobytes() != heights[1][:m].tobytes() or np.any(heights[1][m:] != 0.):
        raise ValueError('The fine solve is not the same physical H with added zero high modes')
    for container in ('config', 'effective_checkpoint_parameters'):
        values = [packet['config'] if container == 'config' else packet['response']['checkpoint']['parameters']
                  for packet in packets]
        if canonical({k:v for k,v in values[0].items() if k not in EXCLUDED}) != canonical(
                {k:v for k,v in values[1].items() if k not in EXCLUDED}):
            raise ValueError('A non-mode/non-I/O tail parameter differs: '+container)
    source_intersection = set(packets[0]['source_sha256']) & set(packets[1]['source_sha256'])
    if not source_intersection:
        raise ValueError('The actual tail numerical source identity is absent')
    for key in source_intersection:
        if packets[0]['source_sha256'][key] != packets[1]['source_sha256'][key]:
            raise ValueError('A common numerical tail source differs: '+key)
    physical = read(a.physical_identity)
    physical_keys = ('all_effective_non_mode_non_IO_parameters_equal',
        'complete_calibration_adapter_and_160_original_cells_identical',
        'profile_fingerprints_identical', 'original_cut_scalars_bitwise_equal',
        'new_full_flow_snapshot_not_restored_from_old_M',
        'distinct_exact_stage_identity_for_new_M', 'original_warm_gate_passed')
    if not all(physical.get(key) is True for key in physical_keys):
        raise ValueError('The actual same-g constructor identity gate did not pass')
    original_ready = Path(physical['old_reference'])
    if sha(original_ready) != physical['old_reference_sha256']:
        raise ValueError('The original constructor reference bytes differ')
    tangent = a.source_topic/'scripts/78718-tail-tangent-core.mjs'
    if sha(tangent) != TANGENT_SHA or "rows:['slope[m]','second[m]','meanSlopeCorrection','meanSecondCorrection','height[m]']" not in tangent.read_text():
        raise ValueError('The exact original cut-jet Jacobian row layout differs')
    if old['heightJetJacobianMethod'] != fine['heightJetJacobianMethod']:
        raise ValueError('The original physical Jacobian methods differ')
    for key in ('radius','backgroundSlope','backgroundSecond','E','Ep'):
        if np.asarray(old['jets'][key],dtype=np.float64).tobytes() != np.asarray(fine['jets'][key],dtype=np.float64).tobytes():
            raise ValueError('The fixed physical cut geometry changed: '+key)
    jets, extra = {}, {}
    for key in ('height','slope','second'):
        jets[key] = comparison(old['jets'][key], fine['jets'][key][:m])
        value = np.asarray(fine['jets'][key][m:], dtype=np.float64)
        extra[key] = dict(values=value.tolist(), max_absolute=float(np.max(abs(value))),
                          l1=float(np.sum(abs(value))))
    means = {key:comparison([old['jets'][key]],[fine['jets'][key]])
             for key in ('meanSlopeCorrection','meanSecondCorrection')}
    J0 = np.asarray(old['heightJetJacobian'],dtype=np.float64).reshape(3*m+2,m)
    J1 = np.asarray(fine['heightJetJacobian'],dtype=np.float64).reshape(3*n+2,n)
    indices = {'slope':(range(0,m),range(0,m)),
        'second':(range(m,2*m),range(n,n+m)),
        'meanSlopeCorrection':([2*m],[2*n]),
        'meanSecondCorrection':([2*m+1],[2*n+1]),
        'height':(range(2*m+2,3*m+2),range(2*n+2,2*n+2+m))}
    jacobian = {key:comparison(J0[list(pair[0]),:],J1[list(pair[1]),:m]) for key,pair in indices.items()}
    result = dict(scope=__doc__, finished=True, no_ODE_or_Newton_executed=True,
        finite_tail_only=True, fine_prefix_or_closed_surface_accepted=False,
        source_sha256={str(path):sha(path) for path in
            (a.coarse_packet,a.fine_packet,a.physical_identity,original_ready,tangent,Path(__file__))},
        modes=[m,n], complete_old_H_bits_preserved=True, extra_H_values_exactly_zero=True,
        all_non_mode_non_IO_configuration_and_effective_parameters_equal=True,
        actual_same_g_constructor_gates={key:physical[key] for key in physical_keys},
        common_numerical_sources={key:packets[0]['source_sha256'][key] for key in sorted(source_intersection)},
        actual_request_audit=[bool(packet['request'].get('audit')) for packet in packets],
        audit_transferred=False, residuals=[old['residual'],fine['residual']],
        original_tolerances=[packet['config']['solveTolerance'] for packet in packets],
        physical_cut={key:old['jets'][key] for key in ('radius','backgroundSlope','backgroundSecond','E','Ep')},
        common_cut_jets=jets, fine_added_cut_jets=extra, mean_cut_corrections=means,
        full_common_physical_H_jacobian_blocks=jacobian,
        original_jacobian_methods=old['heightJetJacobianMethod'],
        limitations=['This compares one actually solved common-H finite-tail pair, not the fine prefix or an infinite closed surface.',
            'The coarse request has its original audit; no fine audit is supplied or inferred here.',
            'Jacobian differences are finite numerical block norms in physical H units, not interval operator bounds.',
            'The current original M32 prefix solve and its final physical gates continue independently.'])
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with a.out.open('x') as stream:
        json.dump(result,stream,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(event='actual_same_H_tail_spectral_comparison',out=str(a.out),sha256=sha(a.out),
        common_slope_max=jets['slope']['max_absolute_difference'],
        common_second_max=jets['second']['max_absolute_difference'],
        added_second_max=extra['second']['max_absolute'],
        common_slope_J_max=jacobian['slope']['max_absolute_difference'],fine_prefix_accepted=False)),flush=True)


if __name__ == '__main__':
    main()
