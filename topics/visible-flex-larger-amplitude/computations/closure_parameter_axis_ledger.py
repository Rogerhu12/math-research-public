#!/usr/bin/env python3
"""Exact46 canonical and physical-height axes of an actual parameter ball.

Q=h_perp/r^4 as in R45, so physical cosine heights are H=r_b^4 Q.
An extra factor w belongs to the legacy raw variable q=Q/w, not to Q.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx
from closure_real_head_source_enclosure import power2, ball_record
from closure_real_head_green_enclosure import ball
from closure_split_joint_io import read, digest


def exact_power_exponent(record):
    if record['lower'] != record['upper']:
        raise ValueError('A chosen parameter unit must be an exact dyadic point')
    m = int(record['lower']['mantissa'])
    e = int(record['lower']['binary_exponent'])
    if m <= 0 or m & (m - 1):
        raise ValueError('A positive power-of-two parameter unit was required')
    return m.bit_length() - 1 + e


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source', 'low', 'lifts', 'parameter-ball', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    ctx.prec = 192
    if args.out.exists():
        raise FileExistsError('Use a fresh exact-axis ledger')
    paths = {name: getattr(args, name) for name in ('source', 'low', 'lifts', 'parameter_ball')}
    docs = {name: read(path) for name, path in paths.items()}
    hashes = {str(path): digest(path) for path in paths.values()}
    source, low, lifts, domain = (docs[name] for name in ('source', 'low', 'lifts', 'parameter_ball'))
    if not all(source['checks'].values()) or not domain['all_gates'] or not all(domain['gates'].values()):
        raise ValueError('The true radius and actual uniform parameter ball must be paid')
    for name in ('low', 'lifts'):
        path = str(paths[name])
        if domain['input_hashes'].get(path) != hashes[path]:
            raise ValueError('The parameter ball and actual axis inputs differ')
    shared_ready = [path for path, sha in source['input_hashes'].items()
                    if path.endswith('-exclusive-ready.json') and low['input_hashes'].get(path) == sha]
    if len(shared_ready) != 1:
        raise ValueError('The real node12 radius must use the same exact source-ready object')
    port = source['ports']['12']
    if port['physical_node'] != 12:
        raise ValueError('The physical cut is node12, not the nominal outer cut')
    rb = ball(port['radius'])
    if not rb.lower() > 0:
        raise ValueError('The same real cut radius must be strictly positive')
    factor = rb ** 4
    rlog = exact_power_exponent(domain['parameter_radius'])
    if rlog != domain['parameter_radius_log2'] or lifts['modes'] != list(range(2, 93, 2)):
        raise ValueError('The actual full46 parameter domain changed')
    if lifts['parameter_units'] != domain['parameter_units']:
        raise ValueError('The actual positive parameter units changed')
    rows = []
    for j, unit in enumerate(domain['parameter_units'], 1):
        ulog = exact_power_exponent(unit)
        qlog = rlog + ulog
        qaxis = power2(qlog)
        haxis = factor * qaxis
        rows.append(dict(j=j, physical_mode=2*j, unit_log2=ulog,
            canonical_Q_axis_log2=qlog, canonical_Q_axis=ball_record(qaxis),
            actual_physical_height_axis=ball_record(haxis),
            actual_physical_height_axis_log2=ball_record(haxis.log()/arb(2).log()),
            guaranteed_physical_height_axis=ball_record(haxis.lower())))
    checks = dict(all46_axes_present=len(rows) == 46,
        all46_positive_Q_axes=all(ball(row['canonical_Q_axis']).lower() > 0 for row in rows),
        all46_positive_physical_height_axes=all(ball(row['guaranteed_physical_height_axis']).lower() > 0 for row in rows),
        same_real_source_and_node12=True, exact_canonical_convention_Q_equals_h_over_r4=True,
        no_extra_w_in_Q_to_H=True)
    result = dict(status='Complete actual46 parameter axes and true physical cut-height conversion paid',
        checks=checks, parameter_radius_log2=rlog, true_cut_radius=port['radius'],
        Q_to_physical_H_factor=ball_record(factor), Q_to_physical_H_log2_factor=ball_record(factor.log()/arb(2).log()),
        canonical_definition='a_j=delta Q_(2j)(b), Q=h_perp/r^4; full real cosine amplitude, not a complex Fourier half.',
        parameter_domain='sum_j |a_j|/u_j <= R. Listed axes are intercepts of this weighted l1 ball, not a product box allowing every axis maximum simultaneously.',
        physical_definition='delta H_(2j)=b^4*a_j at the same true node12 b. The actual physical intercept is enclosed by its recorded interval; the recorded lower endpoint is a guaranteed positive intercept.',
        legacy_raw_q_relation='If raw q=Q/w is used elsewhere, H=b^4*w*q. That different variable is not the parameter here.',
        shared_ready_source=shared_ready[0], rows=rows, input_hashes=hashes,
        source_sha256=digest(Path(__file__)),
        helper_hashes={name:digest(Path(__file__).with_name(name)) for name in (
            'closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py','closure_split_joint_io.py')},
        new_radial_integrations=0, inverse_solves=0,
        elapsed_seconds=time.monotonic()-started, peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='done', checks=checks, parameter_radius_log2=rlog,
        first_axis_Q_log2=rows[0]['canonical_Q_axis_log2'],last_axis_Q_log2=rows[-1]['canonical_Q_axis_log2'],
        Q_to_H_log2=str(factor.log()/arb(2).log()),seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
