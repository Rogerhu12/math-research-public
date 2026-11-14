#!/usr/bin/env python3
"""Assemble all actual CM norms from the local Miller unit atlas.

The D0 linear factors are cancelled in physical coordinates as in R221.  Their
unit change from projective to physical parameters is retained.  Actual CM4
points use the fixed j-1728 tangent; near CM4 logarithms use the R223 six-digit
kernel lifts.  No division by 47 or by a colliding linear factor occurs.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import sys
from p41_miller_unit_atlas47 import Q, P, ZERO, ONE, add, sub, mul, scale, inv, power, log_unit, evaluate, save


def load(path):
    raw = Path(path).read_bytes()
    data = json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)
    return data, hashlib.sha256(raw).hexdigest()


def d0_parameter_correction(zseries, t, ti):
    """log[(z(t)/t)/((z(t)-z(ti))/(t-ti))], with integral difference quotients."""
    assert len(zseries) == 5 and tuple(zseries[0]) == ZERO
    numer = evaluate(zseries[1:], t)
    denom = ZERO
    for k in range(1, 5):
        complete = ZERO
        for j in range(k): complete = add(complete, mul(power(t, k-1-j), power(ti, j)))
        denom = add(denom, mul(zseries[k], complete))
    ratio = mul(numer, inv(denom))
    assert sub(ratio, ONE)[0] % P == sub(ratio, ONE)[1] % P == 0
    return log_unit(ratio)


def cm4_tangent_correction(zseries, u):
    """log[z(u)/(j(u)-1728)], to four digits when v47(u)>=2."""
    assert len(zseries) >= 3 and tuple(zseries[0]) == ZERO
    assert all(x % (P*P) == 0 for x in u)
    a1, a2 = zseries[1:3]
    r0 = scale(a1, -4*pow(46656, -1, Q))
    r1 = scale(add(scale(a2, 4), scale(a1, 27)), -pow(46656, -1, Q))
    return add(log_unit(r0), mul(mul(r1, inv(r0)), u))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--atlas-dir', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    folder = args.script_dir.resolve()/'data'
    inputs = {}
    def read(name):
        d, h = load(folder/name); inputs[name] = h; return d
    level = read('p41_CM4_descending_level47.json.gz')
    dag = read('p41_CM4_descending_kernel_dag47.json.gz')
    cancellation = read('p41_all_D0_cancellation_and_CM4_poles47.json.gz')
    precision = read('p41_selected_CM4_precision6.json.gz')
    assert level['complete'] and precision['complete']
    assert cancellation['all_54_D0_counters_match'] and cancellation['all_horizontal_counts_match_Gaussian_cyclic_rho']
    atlas = {}
    multiplier = None
    for ref in ('9','10','44','0','36','CM4','CM3'):
        path = args.atlas_dir/('p41_Miller_unit_atlas_'+ref+'47.json.gz')
        d, h = load(path); inputs[path.name] = h
        assert d['complete'] and d['reference'] == ref
        assert len(d['records']) == len(set(x['necklace_index_1based'] for x in d['records']))
        atlas[ref] = {x['necklace_index_1based']: x for x in d['records']}
        if multiplier is None: multiplier = int(d['multiplier'])
        assert multiplier == int(d['multiplier'])
    assert sum(map(len,atlas.values())) == 4100
    near = precision['near_CM4_logarithms']
    horizontal = {row['node'] for row in cancellation['horizontal_CM4_nodes']}
    near_counts, d0_counts = Counter(), Counter()
    node_records = {}

    def ordinary_value(record, t):
        zs = record['physical_to_projective_coefficients']
        z = evaluate(zs, t)
        value = evaluate(record['unit_log_coefficients'], z)
        correction = ZERO
        if record['D0_displacement'] is not None:
            ti = tuple(record['D0_displacement']['physical_t'])
            correction = d0_parameter_correction(zs, t, ti)
            value = add(value, correction)
        return value, correction

    def coarse_value(record, u, node):
        zs = record['physical_to_projective_coefficients']
        z = evaluate(zs, u)
        value = evaluate(record['unit_log_coefficients'], z)
        static = ZERO
        if record['kind'] == 'CM4':
            value = add(value, scale(cm4_tangent_correction(zs, u), multiplier))
            if u == ZERO:
                assert node in horizontal
            else:
                assert node in near
                n = near[node]
                # Match the actual invariant, not merely its valuation.
                u6 = n['u_mod47_sixth']
                assert tuple(x % Q for x in u6) == u
                static = scale(tuple(n['log_j_minus1728_mod47_fourth']), multiplier)
                value = add(value, static)
                near_counts[node] += 1
        else:
            assert record['kind'] == 'CM3' and all(x % (P**3) == 0 for x in u)
        return value, static

    targets = {n: [row['node'] for row in rows] for n, rows in dag['targets'].items()}
    target_nodes = set(node for ids in targets.values() for node in ids)
    assert len(target_nodes) == 3282
    for node, info in level['nodes'].items():
        if node not in target_nodes: continue
        rows, values = [], []
        counter = Counter()
        d0correction = ZERO
        staticlogs = ZERO
        for row, label in enumerate(info['image_indices_1based']):
            ref = info['reference_key']
            if label in atlas[ref]:
                record = atlas[ref][label]
                t = tuple(info['reference_parameter'])
                value, correction = ordinary_value(record, t)
                d0correction = add(d0correction, correction)
                counter['ordinary'] += 1
                if record['D0_displacement'] is not None:
                    counter['D0'] += 1
                    d0_counts[node] += 1
                rows.append([ref, label, list(value)])
            else:
                coarse = info['coarse']
                cref = coarse['reference_key']
                clabel = coarse['image_indices_1based'][row]
                record = atlas[cref][clabel]
                u = tuple(coarse['invariant_parameter'])
                value, static = coarse_value(record, u, node)
                staticlogs = add(staticlogs, static)
                counter[cref] += 1
                rows.append([cref, clabel, list(value)])
            values.append(value)
        total = ZERO
        for value in values: total = add(total, value)
        assert len(rows) == 20
        node_records[node] = {'degree': info['degree'], 'counts': dict(counter),
                              'CM_norm_after_D0_factor_removal': total,
                              'D0_parameter_change_logarithm': d0correction,
                              'm_log_j_minus1728_near_CM4': staticlogs,
                              'rows': rows}
    assert set(near_counts) == set(near) and all(v == 1 for v in near_counts.values())
    aggregates = {}
    for n, target_ids in targets.items():
        sums = {k: ZERO for k in ('CM_norm_after_D0_factor_removal','D0_parameter_change_logarithm','m_log_j_minus1728_near_CM4')}
        counter = Counter()
        for node in target_ids:
            record = node_records[node]
            counter.update(record['counts'])
            for k in sums: sums[k] = add(sums[k], record[k])
        assert all(v[1] == 0 for v in sums.values()), ('Frobenius norm sum', n, sums)
        assert counter['D0'] == cancellation['per_index'][n]['D0_collision_norm_rows']
        aggregates[n] = {'index': int(n), 'effective_degree': len(target_ids),
                         'counts': dict(counter), **sums}
    assert aggregates['1']['CM_norm_after_D0_factor_removal'] == (2452507,0)
    # The ramified Gaussian prime 2 has one horizontal return and two vertical
    # branches: T2 Z1 = Z1 + 2 Z2 (not just 2 Z2).
    assert aggregates['2']['CM_norm_after_D0_factor_removal'] == ((2452507+2*1668829) % Q,0), aggregates['2']
    assert aggregates['3']['CM_norm_after_D0_factor_removal'] == (2*5546 % Q,0)
    result = {'complete': True, 'level': 41, 'auxiliary_prime': 47, 'precision': 4,
              'modulus': Q, 'multiplier': str(multiplier),
              'input_sha256': inputs, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'norm_evaluator_sha256': hashlib.sha256((Path(__file__).parent/'p41_miller_unit_atlas47.py').read_bytes()).hexdigest(),
              'nodes': node_records, 'aggregates': aggregates,
              'all_54_aggregate_imaginary_parts_zero': True,
              'all_200_static_CM4_logarithms_used_once_per_target': True,
              'D0_physical_parameter_correction_retained': True,
              'first_three_R197_CM_norms_match': True,
              'scope': 'All CM norms with physical D0 singular factors removed; add R221 merged tiny, subtract degree*cusp, divide once by m, then subtract R195 K.'}
    sha = save(args.output, result)
    print(json.dumps({'complete':True,'indices':len(aggregates),'node_count':len(node_records),
                      'first_three':[aggregates[str(i)]['CM_norm_after_D0_factor_removal'] for i in (1,2,3)],
                      'sha256':sha}),flush=True)


if __name__ == '__main__': main()
