#!/usr/bin/env python3
"""Pay actual q106 radial node placement and positive height reduction costs.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This is an actual saved-input consumer, not a new physical calculation.
The exact 1360-point repaired-field mean and its radial derivative are taken
from the full signed interval certificate. Every full-cell binary affine
Gauss node is replayed exactly. A uniform bound also covers any final partial
cell. The positive weighted reduction has an explicit IEEE basic-operation
fee. The as-yet-unpaid pointwise mean evaluation error epsilon is kept as an
explicit nonnegative term; no libm, frame or coordinate-alignment error is
silently set to zero. No complete floating-field or metric certificate follows.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

import numpy as np

HEIGHT_SOURCE_SHA = 'e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2'
HEIGHT_FUNCTION_SHA = 'ad9ba92e667ebbf572c6d31622959b804aba482d506e6523a7538e33569cd282'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    data = p.read_bytes()
    return json.loads(gzip.decompress(data) if p.suffix == '.gz' else data)


def rat(q):
    return F(int(q['numerator']), int(q['denominator']))


def exact(q):
    q = F(q)
    return dict(numerator=str(q.numerator), denominator=str(q.denominator))


def binary(q):
    return F.from_float(float(q))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('certificate', 'certificate-resource', 'saved-check',
                 'saved-check-resource', 'primary', 'height-source', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Fresh actual radial arithmetic budget required')
    start = time.monotonic()
    data, checked, primary = map(read, (args.certificate, args.saved_check, args.primary))
    gates = []

    def check(name, condition, **details):
        gates.append(dict(name=name, passed=bool(condition), **details))
        if not condition:
            raise ArithmeticError(name)

    for path in (args.certificate_resource, args.saved_check_resource):
        value = read(path)
        check('actual_prerequisite_owned_exit0', value['exitcode'] == 0 and value['wait4_observed'])
    check('complete_same_actual_signed_mean', data['all_domain_and_quadrature_gates']
          and data['primary_sha256'] == sha(args.primary) and data['exact_mean_angular'] == 1360)
    check('independent_saved_payments_replayed', checked['all_gates'] and
          checked['input_sha256'][str(args.certificate)] == sha(args.certificate))
    check('frozen_actual_radial_height_rule', sha(args.height_source) == HEIGHT_SOURCE_SHA and
          data['original_height_function_sha256'] == HEIGHT_FUNCTION_SHA)
    check('binary64_machine_model', np.finfo(np.float64).bits == 64 and
          binary(np.finfo(np.float64).eps) == F(2) ** -52)

    mesh = np.asarray(primary['mesh'], dtype=np.float64)
    x = list(map(binary, mesh))
    J, L = len(x) - 1, x[-1]
    check('complete_q106_original_mesh', J == 2227 and x[0] == 0 and
          all(a < b for a, b in zip(x, x[1:])))
    table = data['actual_binary_gauss_table']
    g = np.array([float(2 * rat(row['node']) - 1) for row in table], dtype=np.float64)
    raw = [rat(row['raw_weight']) for row in table]
    mass = sum(raw)
    check('all_actual_gauss_nodes_remain_exact_binary_inputs',
          len(g) == 6 and all(binary(t) == 2 * rat(row['node']) - 1
                             for t, row in zip(g, table)))
    gmax = max(map(abs, map(binary, g)))
    check('strictly_internal_positive_quadrature_table', gmax < 1 and min(raw) > 0)

    # Literal original height_integral affine expression, with each NumPy
    # elementary operation producing its own binary64 array.
    left, right = mesh[:-1], mesh[1:]
    h = right - left
    rounded_nodes = ((left + right)[:, None] + h[:, None] * g[None, :]) / 2
    cells = data['per_original_cell']
    check('complete_original_cell_bounds', len(cells) == J)
    F0 = max(max(map(abs, map(F, row['mean_value_interval']))) for row in cells)
    F1 = max(max(map(abs, map(F, row['mean_derivative_interval']))) for row in cells)
    check('finite_small_actual_mean_envelopes', 0 <= F0 < F(2) ** 500 and
          0 <= F1 < F(2) ** 500 and 0 < L < 4)

    u = F(2) ** -53
    eta = F(2) ** -1075
    full_fee = F(0)
    partial_fees = []
    rows = []
    for j, (a, b, saved) in enumerate(zip(x, x[1:], cells)):
        H = b - a
        deriv = max(map(abs, map(F, saved['mean_derivative_interval'])))
        check('same_original_interval_derivative_cap', saved['original_interval'] == j and
              list(map(F, saved['physical_interval'])) == [a, b], cell=j)
        full_errors = []
        for k, (gg, weight) in enumerate(zip(g, raw)):
            ideal = (a + b + H * binary(gg)) / 2
            actual = binary(rounded_nodes[j, k])
            check('actual_full_affine_node_inside_original_cell', a <= actual <= b, cell=j, node=k)
            full_errors.append(abs(actual - ideal))
        cell_fee = H * deriv * sum(w * e for w, e in zip(raw, full_errors))
        full_fee += cell_fee

        # For every floating final s in [a,b], use the IEEE RN bound
        # |fl(z)-z| <= u*|z| + eta, including subnormal operations.
        # The final division by two is exact except for a possible eta.
        eh = u * H + eta
        es = u * (a + b) + eta
        em = u * (H + eh) * gmax + eta
        ea = u * ((a + b) + es + (H + eh) * gmax + em) + eta
        eq = (es + eh * gmax + em + ea) / 2 + eta

        # A very short partial interval can round a node to the neighboring
        # original cell. Hence its displacement is paid by the full-domain
        # derivative cap. At the two global endpoints positivity and the
        # strict internal-node margin keep every actual node in [0,L].
        if j == 0:
            endpoint_ok = a == 0 and b * (1 + gmax) / 2 + eq < L
        elif j == J - 1:
            endpoint_ok = a - eq > 0 and H * (1 - gmax) / 2 > eq
        else:
            endpoint_ok = a - eq > 0 and b + eq < L
        check('all_final_partial_nodes_stay_inside_whole_domain', endpoint_ok, cell=j)
        partial = H * mass * F1 * eq
        partial_fees.append(partial)
        rows.append(dict(original_interval=j, physical_interval=[str(a), str(b)],
                         actual_full_node_errors=list(map(str, full_errors)),
                         full_cell_node_placement_H_fee=str(cell_fee),
                         any_final_partial_node_displacement=str(eq),
                         any_final_partial_H_fee=str(partial),
                         partial_uses_global_derivative_for_neighboring_cell_rounding=True))

    max_partial = max(partial_fees)
    node_fee = full_fee + max_partial
    hmax = max(b - a for a, b in zip(x, x[1:]))
    total_positive_mass = (L + hmax) * mass
    # One prefix and one final partial interval. This depth safely exceeds
    # every multiplication/addition along a 6-term dot plus the <=2227-term
    # original prefix cumsum. No cancellation is used. IEEE subnormals have
    # an extra absolute budget far larger than 2^20 elementary eta fees.
    depth = 2 * J + 64
    gamma = depth * u / (1 - depth * u)
    underflow = F(2) ** -1020 * (F0 + 2)
    reduction_fee = gamma * total_positive_mass * F0 + underflow
    epsilon_coefficient = (1 + gamma) * total_positive_mass
    arithmetic_constant = node_fee + reduction_fee
    input_rounding = F0 * (u * L + eta)
    check('positive_reduction_depth_and_no_overflow_domain', depth * u < F(1, 2) and
          total_positive_mass * (F0 + 1) < F(2) ** 1000)
    out = dict(schema='actual-q106-radial-affine-and-reduction-arithmetic-budget-v1',
               scope=__doc__, source_sha256=sha(__file__),
               input_sha256={str(p): sha(p) for p in
                             (args.certificate, args.certificate_resource,
                              args.saved_check, args.saved_check_resource,
                              args.primary, args.height_source)},
               all_gates=True, gate_count=len(gates), gates=gates,
               actual_original_cells=J, complete_mean_angular=1360,
               actual_full_affine_nodes_replayed=6 * J,
               exact_uniform_mean_abs=exact(F0), exact_uniform_mean_derivative_abs=exact(F1),
               exact_full_node_placement_H_fee=exact(full_fee),
               exact_any_final_partial_node_placement_H_fee=exact(max_partial),
               exact_positive_reduction_H_fee=exact(reduction_fee),
               exact_arithmetic_constant_H_fee=exact(arithmetic_constant),
               exact_unpaid_point_mean_epsilon_coefficient=exact(epsilon_coefficient),
               exact_optional_real_input_rounding_H_fee=exact(input_rounding),
               display=dict(full_node_fee=float(full_fee), partial_node_fee=float(max_partial),
                            positive_reduction_fee=float(reduction_fee),
                            arithmetic_constant=float(arithmetic_constant),
                            unpaid_point_mean_epsilon_coefficient=float(epsilon_coefficient),
                            optional_input_rounding=float(input_rounding)),
               binary64_unit_roundoff=exact(u), half_smallest_subnormal=exact(eta),
               positive_reduction_max_path_length=depth,
               explicit_unpaid_epsilon='At every actually rounded radial Gauss node, absolute error of the stored floating mean versus the exact 1360-angle mean of the identified repaired mathematical field. Includes frame/libm, angular-node/evaluation, original-to-comparison and coordinate-alignment differences unless each is separately paid. Conditional range 0<=epsilon<=1.',
               conditional_operator_bound='For every binary64 final s in [0,L], |computed_height(s)-exact_binary_Gauss6_of_repaired_mean(s)| <= arithmetic_constant + epsilon_coefficient*epsilon. The separate saved Gauss6 analytic fee and angular alias must still be added.',
               optional_continuous_input_bound='If a real input s is first rounded to binary64, add the separately displayed F0*(u*L+eta), provided the rounded input remains in the same [0,L] domain.',
               rows=rows,
               libm_frame_or_point_mean_epsilon_has_been_certified=False,
               original_accepted_metric_PDE_reach_or_closed_surface_certified=False,
               new_ODE_Node_Newton_calls=0,
               elapsed_seconds=time.monotonic() - start,
               peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('wb') as f:
        with gzip.GzipFile(filename='', mode='wb', fileobj=f, mtime=0) as z:
            z.write((json.dumps(out, separators=(',', ':')) + '\n').encode())
    print(json.dumps(dict(event='actual_radial_affine_arithmetic_budget_finished',
                         gates=len(gates), display=out['display'],
                         out=str(args.out), sha256=sha(args.out))), flush=True)


if __name__ == '__main__':
    main()
