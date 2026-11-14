#!/usr/bin/env python3
"""Independently replay every saved radial Gauss6 payment with Fractions.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The producer's full radial interval enclosures remain their explicitly
identified analytic premise. This consumer independently verifies coverage,
the actual positive quadrature table, the transport norm by the quantile
formula, all 2227 derivative-oscillation payments, and the single-anchor sum.
No physical ODE, new field, floating-error certificate or reach is claimed.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    data = p.read_bytes()
    return json.loads(gzip.decompress(data) if p.suffix == '.gz' else data)


def rat(q):
    return F(int(q['numerator']), int(q['denominator']))


def dy(q):
    return F(int(q[0])) * F(2) ** int(q[1])


def exact(q):
    q = F(q)
    return dict(numerator=str(q.numerator), denominator=str(q.denominator))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('certificate', 'resource', 'domain', 'primary', 'producer', 'out'):
        parser.add_argument('--' + name, required=True, type=Path)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh exact radial-mean saved consumer output')
    start = time.monotonic()
    data, owned, domain, primary = map(read, (args.certificate, args.resource,
                                            args.domain, args.primary))
    gates = []

    def check(name, condition, **details):
        gates.append(dict(name=name, passed=bool(condition), **details))
        if not condition:
            raise ArithmeticError(name)

    check('owned_actual_producer_exit0', owned['exitcode'] == 0 and
          owned['wait4_observed'] and owned['automatic_restarts'] == 0)
    check('actual_source_identity', data['source_sha256'] == sha(args.producer))
    check('same_actual_primary_and_domain', data['primary_sha256'] == sha(args.primary)
          and data['input_sha256'][str(args.domain)] == sha(args.domain)
          and domain['primary_sha256'] == sha(args.primary))
    check('complete_analytic_producer_domain', data['all_domain_and_quadrature_gates']
          and data['complete_radial_cover'] and not data['failed_atoms'])
    check('same_repaired_comparison',
          data['state_comparison_definition_sha256'] == domain['state_comparison_definition_sha256']
          and data['background_comparison_definition_sha256'] == domain['background_comparison_definition_sha256'])
    check('same_actual_1360_mean', data['exact_mean_angular'] == 1360)
    check('single_anchor_and_unpaid_costs_are_explicit', data['no_cellwise_anchor_reset']
          and not data['angular_alias_paid_here']
          and not data['original_floating_node_affine_arithmetic_libm_or_coordinate_alignment_paid']
          and not data['original_g_PDE_reach_or_closed_surface_certified'])

    table = data['actual_binary_gauss_table']
    nodes = [rat(row['node']) for row in table]
    raw = [rat(row['raw_weight']) for row in table]
    weights = [rat(row['normalized_weight']) for row in table]
    mass = sum(raw)
    check('positive_six_point_actual_table', len(table) == 6 and
          nodes == sorted(nodes) and 0 < nodes[0] < nodes[-1] < 1 and
          min(raw) > 0 and min(weights) > 0)
    check('exact_table_normalization', mass == rat(data['exact_table_mass']) and
          weights == [w / mass for w in raw] and sum(weights) == 1)
    moment = abs(sum(x * w for x, w in zip(nodes, weights)) - F(1, 2))
    mass_error = abs(mass - 1)
    check('exact_first_moment_and_mass_defects',
          moment == rat(data['exact_normalized_first_moment_defect']) and
          mass_error == rat(data['exact_weight_mass_error']))

    # Independently integrate the monotone quantile coupling. The producer
    # instead integrates |CDF(x)-x| between physical node positions.
    previous = F(0)
    W1 = F(0)
    transport_pieces = []
    for x, w in zip(nodes, weights):
        following = previous + w
        if x <= previous:
            piece = (following ** 2 - previous ** 2) / 2 - x * w
        elif x >= following:
            piece = x * w - (following ** 2 - previous ** 2) / 2
        else:
            piece = ((x - previous) ** 2 + (following - x) ** 2) / 2
        check('nonnegative_exact_quantile_transport_piece', piece >= 0)
        transport_pieces.append(exact(piece))
        W1 += piece
        previous = following
    check('independent_quantile_and_CDF_W1_agree', previous == 1 and
          W1 == rat(data['exact_unit_interval_Wasserstein1']))

    mesh = [F.from_float(float(x)) for x in primary['mesh']]
    rows = data['whole_radial_interval_mean_rows']
    check('all_original_cells_and_actual_atoms', len(mesh) == 2228 and
          len(rows) == len(domain['rows']) == data['complete_atoms'] == 3326)
    cells = {}
    cursor = mesh[0]
    for index, (row, original) in enumerate(zip(rows, domain['rows'])):
        left, right = map(F, row['s_interval'])
        j = row['original_interval']
        check('atom_cover_and_same_original_domain', row['atom'] == index and
              left == cursor and left < right and mesh[j] <= left < right <= mesh[j + 1]
              and row['s_interval'] == original['s_interval']
              and row['background_piece'] == original['background_piece']
              and j == original['original_interval'], atom=index)
        check('whole_interval_exact_mean_premise', row['positive_domain'] and
              row['all_N_exact_mean_angles_enclosed_on_the_whole_radial_interval'], atom=index)
        bounds = [list(map(F, pair)) for pair in
                  row['exact_N_point_mean_value_derivative_intervals']]
        check('ordered_value_and_full_derivative_intervals',
              len(bounds) == 2 and all(len(v) == 2 and v[0] <= v[1] for v in bounds), atom=index)
        if j not in cells:
            cells[j] = dict(value=bounds[0], derivative=bounds[1], atoms=[])
        else:
            for name, pair in zip(('value', 'derivative'), bounds):
                cells[j][name] = [min(cells[j][name][0], pair[0]),
                                  max(cells[j][name][1], pair[1])]
        cells[j]['atoms'].append(index)
        cursor = right
    check('global_radial_coverage_exact', cursor == mesh[-1] and
          set(cells) == set(range(len(mesh) - 1)))
    check('all_square_root_endpoint_checks_counted',
          data['verified_square_root_endpoint_inequalities'] == 2 * 1360 * len(rows))

    payments = data['per_original_cell']
    check('complete_original_cell_payments', len(payments) == len(mesh) - 1)
    total = F(0)
    maximum = F(0)
    for j, saved in enumerate(payments):
        cell = cells[j]
        h = mesh[j + 1] - mesh[j]
        low, high = cell['derivative']
        midpoint, radius = (low + high) / 2, (high - low) / 2
        cap = max(map(abs, cell['value']))
        fee = h * h * (W1 * radius + moment * abs(midpoint)) + h * cap * mass_error
        check('original_cell_source_union_matches', saved['original_interval'] == j and
              list(map(F, saved['physical_interval'])) == [mesh[j], mesh[j + 1]] and
              saved['complete_source_atoms'] == cell['atoms'] and
              list(map(F, saved['mean_value_interval'])) == cell['value'] and
              list(map(F, saved['mean_derivative_interval'])) == cell['derivative'], cell=j)
        check('saved_derivative_midpoint_and_radius_exact',
              F(saved['exact_derivative_midpoint']) == midpoint and
              F(saved['exact_derivative_radius']) == radius, cell=j)
        check('exact_cell_payment_and_outward_saved_upper', fee >= 0 and
              F(saved['exact_error_before_rounding']) == fee and
              dy(saved['radial_quadrature_error_upper']) >= fee, cell=j)
        check('full_and_every_final_partial_cell_paid',
              saved['same_bound_covers_every_final_partial_cell'], cell=j)
        total += fee
        maximum = max(maximum, fee)
    check('uniform_same_anchor_total_is_outward',
          dy(data['full_anchored_radial_quadrature_H_error_upper']) >= total)
    output = dict(schema='independent-exact-saved-radial-Gauss6-mean-consumer-v1',
                  scope=__doc__, source_sha256=sha(__file__),
                  input_sha256={str(p): sha(p) for p in
                                (args.certificate, args.resource, args.domain,
                                 args.primary, args.producer)},
                  all_gates=True, gate_count=len(gates), gates=gates,
                  exact_independent_Wasserstein1=exact(W1),
                  exact_quantile_transport_pieces=transport_pieces,
                  complete_atoms=len(rows), complete_original_cells=len(payments),
                  exact_uniform_anchored_H_error=exact(total),
                  exact_largest_cell_payment=exact(maximum),
                  uniform_anchored_H_error_display=float(total),
                  analytic_interval_enclosures_recomputed=False,
                  remaining_angular_alias_libm_affine_alignment_costs_explicit=True,
                  new_ODE_Node_Newton_calls=0,
                  elapsed_seconds=time.monotonic() - start,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    serialized = (json.dumps(output, separators=(',', ':')) + '\n').encode()
    if args.out.suffix == '.gz':
        with args.out.open('wb') as f:
            with gzip.GzipFile(filename='', mode='wb', fileobj=f, mtime=0) as z:
                z.write(serialized)
    else:
        args.out.write_bytes(serialized)
    print(json.dumps(dict(event='exact_saved_radial_mean_payment_check_finished',
                         gates=len(gates), H_error=float(total),
                         out=str(args.out), sha256=sha(args.out))), flush=True)


if __name__ == '__main__':
    main()
