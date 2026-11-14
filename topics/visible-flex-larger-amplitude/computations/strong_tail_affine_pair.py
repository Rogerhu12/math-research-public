#!/usr/bin/env python3
"""Compare two converged full-height responses of the same finite tail.

All heights and all M slope rows of the original full Jacobian are retained.
The old primary binds the physical cut metric and boundary tolerance. This
measures a finite affine discrepancy; it is not a derivative remainder bound
or an acceptance test for the new prefix, and performs no new tail evaluation.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('old-primary', 'old-packet', 'new-packet', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise ValueError('Use a fresh diagnostic output')
    primary, old, new = map(read, (args.old_primary, args.old_packet, args.new_packet))
    if (not primary.get('solver_success') or primary.get('audit_pending', True) or
            Path(primary['actual_tail']['final_response']).resolve() != args.old_packet.resolve() or
            old['source_sha256'] != primary['actual_tail']['source_sha256']):
        raise ValueError('The original actually accepted primary/packet binding differs')
    io = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}
    equation = lambda record: {k: v for k, v in record['config'].items() if k not in io}
    if equation(old) != equation(new):
        raise ValueError('Different complete finite tail equations')
    common = set(old['source_sha256']) & set(new['source_sha256'])
    if not all(old['source_sha256'][k] == new['source_sha256'][k] for k in common):
        raise ValueError('A common original numerical tail source changed')
    modes = int(old['config']['modes'])
    arrays = []
    for record in (old, new):
        response, request = record['response'], record['request']
        if (not request.get('jacobian') or not response.get('converged') or
                not np.isfinite(response['residual']) or
                response['residual'] > record['config']['solveTolerance']):
            raise ValueError('A complete converged original response is required')
        H = np.asarray(request['height'], dtype=float)
        J = np.asarray(response['heightJetJacobian'], dtype=float)
        slope = np.asarray(response['jets']['slope'], dtype=float)
        if H.shape != (modes,) or J.shape != ((3*modes+2)*modes,) or slope.shape != (modes,):
            raise ValueError('Complete original H/J/slope shape differs')
        if not all(np.isfinite(x).all() for x in (H, J, slope)):
            raise ValueError('Nonfinite physical values')
        arrays.append((H, J.reshape(3*modes+2, modes)[:modes], slope))
    (H0, J0, s0), (H1, J1, s1) = arrays
    delta = H1-H0
    forward = s1-(s0+J0@delta)
    backward = s0-(s1-J1@delta)
    E = float(primary['physical_tail_cut']['E'])
    if not np.isfinite(E) or E <= 0:
        raise ValueError('The original physical cut E must be positive')
    tolerance = primary['actual_tail']['actual_physical_bc_tolerance']
    output = dict(scope=__doc__, created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_sha256={str(p): sha(p) for p in (Path(__file__), args.old_primary, args.old_packet, args.new_packet)},
        original_finite_equations=equation(old), all_common_numerical_sources_identical=True,
        common_source_sha256={k: old['source_sha256'][k] for k in sorted(common)},
        additional_new_source_names=sorted(set(new['source_sha256'])-set(old['source_sha256'])),
        old_audit=old['request'].get('audit'), new_audit=new['request'].get('audit'),
        residuals=[old['response']['residual'], new['response']['residual']],
        complete_height_change=delta.tolist(), max_height_change=float(np.max(abs(delta))),
        forward_slope_error=forward.tolist(), backward_slope_error=backward.tolist(),
        forward_slope_max_abs_error=float(np.max(abs(forward))),
        backward_slope_max_abs_error=float(np.max(abs(backward))),
        forward_worst_mode=int(old['config']['spacing'])*(int(np.argmax(abs(forward)))+1),
        maximum_absolute_slope_change=float(np.max(abs(s1-s0))),
        slope_J_difference_induced_inf=float(np.max(np.sum(abs(J1-J0), axis=1))),
        physical_cut_E=E,
        physical_BC_conversion='Original actual boundary: q*dy - physical_tail_slope/sqrt(E).',
        forward_slope_affine_discrepancy_in_physical_BC_units=float(np.max(abs(forward))/np.sqrt(E)),
        original_physical_BC_tolerance=tolerance,
        not_a_new_prefix_boundary_measurement=True,
        no_continuous_or_future_remainder_bound=True, new_tail_evaluations=0)
    args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out),
        forward_slope_max_abs_error=output['forward_slope_max_abs_error'],
        forward_discrepancy_in_physical_BC_units=output['forward_slope_affine_discrepancy_in_physical_BC_units'])), flush=True)


if __name__ == '__main__':
    main()
