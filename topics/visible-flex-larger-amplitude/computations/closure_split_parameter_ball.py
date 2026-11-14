#!/usr/bin/env python3
"""R47 positive46 parameter ball using an actual successful R51 full641 box.

Only positive row products are evaluated.  The complete mean, original
metric and all original641 radii remain unchanged on the lifted domain.
This source is prepared independently of the still-pending joint result;
it refuses to run without that actual successful certificate.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gzip
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx
from closure_real_head_source_enclosure import power2, ball_record
from closure_real_head_green_enclosure import ball
from closure_split_joint_io import digest, read, iter_array, metadata_without_array, validate_common, label


def compact(value):
    return arb(int(value[0])) * power2(int(value[1]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('low', 'split', 'density', 'joint', 'lifts', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 192
    started = time.monotonic()
    if args.out.exists():
        raise FileExistsError('Use a fresh full641 parameter-ball output')
    hashes = {str(getattr(args, name)): digest(getattr(args, name))
              for name in ('low', 'split', 'density', 'joint', 'lifts')}
    low, density = read(args.low), read(args.density)
    split = metadata_without_array(args.split, 'gamma_rows')
    joint, lifts = read(args.joint), read(args.lifts)
    cells = validate_common(low, split, density, hashes, args.density)
    N, dim = len(cells), 3 * len(cells) + 2
    inf, zi = 3 * N, 3 * N + 1
    if not joint['whole_head_closed'] or not all(joint['gates'].values()):
        raise ValueError('A successful actual full641 joint certificate is required')
    if joint['dimension'] != dim or len(joint['rows']) != dim:
        raise ValueError('Every original641 row is required')
    for name in ('low', 'split', 'density'):
        path = str(getattr(args, name))
        if joint['input_hashes'].get(path) != hashes[path]:
            raise ValueError('The actual successful joint certificate used another input')
    for name in ('low', 'density'):
        path = str(getattr(args, name))
        if lifts['input_hashes'].get(path) != hashes[path]:
            raise ValueError('The true parameter lifts have another exact norm or field')
    if lifts['cells'] != cells or lifts['modes'] != list(range(2, 93, 2)):
        raise ValueError('The complete46-parameter true chart is required')
    if [r['cell'] for r in lifts['parameter_cell_lift']] != cells:
        raise ValueError('A true lift source cell was omitted')
    Z, rho = ball(joint['independent_far_z']), ball(joint['physical_domain'])
    if not Z == ball(lifts['parameter_far_scale']):
        raise ValueError('The independent far parameter scales differ')
    r, image, slack = [], [], []
    for i, row in enumerate(joint['rows']):
        if row['index'] != i or any(row[key] != val for key, val in label(i, N).items()):
            raise ValueError('The actual joint rows were reordered')
        r.append(ball(row['radius']).lower())
        image.append(ball(row['image']).upper())
        slack.append(ball(row['map_slack']).lower())
    if not all(x > 0 for x in r + slack):
        raise ValueError('The original strict radius or map slack is absent')
    t = [(r[n] + r[N + n] + r[2 * N + n] + r[inf]).upper() for n in range(N)]
    A = [ball(row['V_over_w_upper']).upper() for row in density['rows']]
    ell = [ball(row['l']).upper() for row in lifts['parameter_cell_lift']]
    e = ball(lifts['parameter_far_lift']).upper()
    gamma = ball(density['gamma_high']).upper()
    slopes = [(3 * (1 + rho.upper()) + 216 * a * (1 + rho.upper()) ** 2).upper() for a in A]
    c = [arb(0) for _ in range(dim)]
    names = ('main', 'corr', 'base', 'remainder')
    for k in range(N):
        total = arb(0)
        for n in range(N):
            gm, gc, gq, gr = [compact(low['gamma_upper'][name][k][n]) for name in names]
            total += (gm + 3 * gc + 3 * rho.upper() * gq + 216 * (1 + rho.upper()) ** 2 * gr) * ell[n]
        c[k] = total.upper()
    total = arb(0)
    for n in range(N):
        fm, fc, fq, fr = [compact(low['far_z_source_upper'][name][n]) for name in names]
        total += (fm + 3 * fc + 3 * rho.upper() * fq + 216 * (1 + rho.upper()) ** 2 * fr) * ell[n]
    c[zi] = (total / Z.lower() + e).upper()
    del low
    count = 0
    for k, row in enumerate(iter_array(args.split, 'gamma_rows')):
        if row['output_cell'] != 12 + k or len(row['sources']) != N - k:
            raise ValueError('The complete high causal coverage differs')
        near, rest = arb(0), arb(0)
        for n, source in enumerate(row['sources'], k):
            if source['source_cell'] != 12 + n:
                raise ValueError('A high causal source cell was omitted')
            near += ball(source['near_gamma']).upper() * slopes[n] * ell[n]
            rest += ball(source['rest_gamma']).upper() * slopes[n] * ell[n]
            count += 1
        c[N + k], c[2 * N + k] = near.upper(), rest.upper()
    if count != N * (N + 1) // 2:
        raise ValueError('Both complete high triangles are required')
    c[inf] = (gamma * sum((slopes[n] * ell[n] for n in range(N)), arb(0))).upper()
    limits = [(arb(1), 'unit_parameter_ball', None)]
    for n in range(N):
        if ell[n] > 0:
            limits.append((((rho.lower() - t[n]) / ell[n]).lower(), 'total_state_rho', cells[n]))
            limits.append((((1 / (64 * A[n]) - 1 - t[n]) / ell[n]).lower(), 'complete_mean_domain', cells[n]))
    for i in range(dim):
        if c[i] > 0:
            limits.append(((slack[i] / c[i]).lower(), 'map_slack', i))
    if not all(item[0] > 0 for item in limits):
        raise ArithmeticError('An original strict parameter margin is absent')
    limiting = min(limits, key=lambda item: item[0])
    bound = (limiting[0] / 2).lower()
    mantissa, exponent = bound.man_exp()
    log2 = int(mantissa).bit_length() - 1 + int(exponent)
    R = power2(log2)
    if not 0 < R <= bound:
        raise ArithmeticError('The inward dyadic parameter radius is invalid')
    lifted_t = [(t[n] + R * ell[n]).upper() for n in range(N)]
    lifted_image = [(image[i] + R * c[i]).upper() for i in range(dim)]
    gates = dict(positive_dyadic_parameter_radius=R > 0,
        all46_parameter_units_positive=len(lifts['parameter_units']) == 46 and all(ball(v).lower() > 0 for v in lifts['parameter_units']),
        all641_lifted_map_inclusions=all(lifted_image[i] < r[i] for i in range(dim)),
        all213_lifted_total_states_below_original_rho=all(v < rho.lower() for v in lifted_t),
        all213_complete_mean_domains=all((A[n] * (1 + lifted_t[n])).upper() < arb(1) / 64 for n in range(N)),
        original_full_far_domain=ball(joint['auxiliary_far_z']).upper() + Z.upper() * r[zi] < Z.lower(),
        original_joint_metric_still_strict=ball(joint['maximum_joint_Lipschitz']).upper() < 1)
    result = dict(status=('Positive full46 true-head parameter ball paid from the actual strict641 certificate'
        if all(gates.values()) else 'Completed parameter-ball attempt with explicit failed gates'),
        all_gates=all(gates.values()), gates=gates, parameter_radius=ball_record(R), parameter_radius_log2=log2,
        parameter_units=lifts['parameter_units'], parameter_norm=lifts['norm'],
        original_radii_unchanged=True, original_J_and_W_unchanged=True,
        domain_reason='The parameter lift is purely low46. It enters both s and total t; all lifted total states remain below the original rho and inside A*(1+t)<1/64. The same complete R51 derivative bound therefore holds over the entire parameter ball.',
        limiting_constraint=dict(kind=limiting[1], cell_or_row=limiting[2], unhalved_radius_bound=ball_record(limiting[0])),
        original_joint_Lipschitz=joint['maximum_joint_Lipschitz'],
        rows=[dict(index=i, **label(i, N), parameter_column=ball_record(c[i]),
            lifted_image=ball_record(lifted_image[i]), retained_map_slack=ball_record((r[i] - lifted_image[i]).lower())) for i in range(dim)],
        cells=[dict(cell=n, lifted_total_radius=ball_record(lifted_t[k]),
            full_mean_domain=ball_record((A[k] * (1 + lifted_t[k])).upper())) for k, n in enumerate(cells)],
        input_hashes=hashes, source_sha256=digest(Path(__file__)),
        helper_hashes={name: digest(Path(__file__).with_name(name)) for name in (
            'closure_split_joint_io.py', 'closure_real_head_source_enclosure.py', 'closure_real_head_green_enclosure.py')},
        inverse_solves=0, radial_integrations=0,
        scope='True node12-to-cuff parameter family only. Outer0..11/full strong-prefix matching and closed-surface geometry remain separate.',
        high_shallow_heights_are_outputs=True,
        elapsed_seconds=time.monotonic() - started, peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload = gzip.compress((json.dumps(result, separators=(',', ':')) + '\n').encode(), mtime=0)
    if len(payload) >= 5000000:
        raise ArithmeticError('Repository file cap exceeded')
    args.out.write_bytes(payload)
    print(json.dumps(dict(event='done', all_gates=all(gates.values()), gates=gates,
        parameter_radius_log2=log2, output=str(args.out), sha256=digest(args.out), bytes=len(payload),
        seconds=result['elapsed_seconds'], RSS_KiB=result['peak_RSS_KiB'])), flush=True)
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
