#!/usr/bin/env python3
"""Only the required actual T2 target discs, from71 global quadrics and a unit Jacobian.

Each record keeps its independently generated cubic anchor, local parameter,
exact branch identification and the4e+3 coefficients needed for a shifted unit.
Existing records are retained; higher required orders extend the same parameter.
"""
import argparse
import ctypes
import gc
import gzip
import hashlib
import json
from pathlib import Path
import random
import resource
import sys
import time


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def release():
    gc.collect()
    try:
        ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--jets', type=Path, default=Path('/tmp/p41_t2_first_family_cubic47_checkpoint.json.gz'))
    parser.add_argument('--inventory', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=Path('/tmp/p41_t2_quadratic_discs47_checkpoint.json.gz'))
    parser.add_argument('--minimum-order', type=int, default=3)
    parser.add_argument('--max-new-records', type=int)
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model
    from p41_cm4_divisor47 import kernel
    from p41_poincare_norms47 import determinant
    from p41_formal47_multiply import write_checkpoint
    start = time.monotonic()
    inventory, isha = read(args.inventory)
    needed = inventory['records']
    target, tsha = read(args.jets)
    source_hashes = target['source_sha256']
    assert inventory['source_sha256'] == source_hashes and inventory['input_sha256']['target_cubic'] == tsha
    points = target['points_1based']
    known = [r.from_json([row for t in target['targets'] for row in t['evaluation_coefficients'][k]]) for k in range(4)]
    del inventory, target
    release()
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.output.exists():
        out, _ = read(args.output)
        assert out['source_sha256'] == source_hashes and out['target_cubic_sha256'] == tsha
        assert out['generating_source_sha256'] == source_sha
        saved = {record['label']: record for record in out['records']}
    else:
        saved = {}
        out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4,
               'source_sha256': source_hashes, 'target_cubic_sha256': tsha,
               'inventory_sha256_history': [], 'generating_source_sha256': source_sha,
               'normalization': 'weight2 coordinates divided by the same f0; z=u/f0 minus its value at the actual target constant',
               'records': [], 'status': 'actual T2 nonunit discs in progress'}
    if isha not in out['inventory_sha256_history']:
        out['inventory_sha256_history'].append(isha)
    pending = []
    for item in needed:
        order = max([args.minimum_order]+[a['minimum_required_last_jet'] for a in item['nonunit_sections']])
        if item['label'] not in saved or saved[item['label']]['order'] < order:
            pending.append((item, order))
    if not pending:
        print('All required actual T2 discs already saved; no computation repeated.', flush=True)
        return
    if args.max_new_records is not None:
        pending = pending[:args.max_new_records]
    sources, hashes = load_sources(folder/'data')
    assert hashes == source_hashes
    M = make_model(sources)
    divs = sources[1]
    K = r.from_json(kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'], divs['canonical_kernel_block']))
    fc = r.mm(K, r.column(divs['canonical_coefficients']))
    sq = [(a-1, b-1) for a, b in divs['square_basis_monomials_1based']]
    S = r.from_json(divs['square_basis_inverse'])
    pairs = [(i, j) for i in range(73) for j in range(i, 73)]
    wp = r.rows(M['W'], M['P2'])
    # Build and verify each block directly, without two huge temporary matrices.
    H = r.zeros(199, len(pairs))
    for lower in range(0, len(pairs), 128):
        upper = min(lower+128, len(pairs))
        group = pairs[lower:upper]
        aa, bb = [a for a, b in group], [b for a, b in group]
        C = r.mul(r.cols(wp, aa), r.cols(wp, bb))
        chunk = r.mm(S, C)
        for z in range(2):
            H[z][:, lower:upper] = chunk[z]
        actual = r.mul(r.cols(M['W'], aa), r.cols(M['W'], bb))
        assert r.equal(actual, r.mm(M['V2'], C))
    A1 = M['A1']
    del sources, M, divs, K, wp, C, chunk, actual, S
    release()
    transpose = lambda x: (x[0].T.copy(), x[1].T.copy())
    f = [r.mm(v, fc) for v in known]
    assert np.all(r.units(f[0]))
    inverses = [r.inverse_values(f[0])]
    for k in range(1, 4):
        total = r.zeros(162, 1)
        for j in range(1, k+1):
            total = r.add(total, r.mul(f[j], inverses[k-j]))
        inverses.append(r.neg(r.mul(inverses[0], total)))
    normalized = []
    for k in range(4):
        value = r.zeros(162, 73)
        for j in range(k+1):
            value = r.add(value, r.mul(known[j], inverses[k-j]))
        normalized.append(value)
    del known, inverses, f
    release()

    def bilinear(x, y, pp):
        return transpose(r.mul(r.rows(x, [a for a, b in pp]), r.rows(y, [b for a, b in pp])))

    for item, order in pending:
        position = item['branch_index_0based']*54+item['first_family_position_0based']
        assert points[item['first_family_position_0based']] == item['source_point_index_1based']
        anchor = [transpose(r.rows(v, [position])) for v in normalized]
        x0 = anchor[0]
        assert r.equal(r.mm(transpose(fc), x0), r.eye(1))
        grad, gs = r.zeros(73, len(pairs)), r.zeros(73, 199)
        for index, (a, b) in enumerate(pairs):
            for z in range(2):
                grad[z][a, index] = (grad[z][a, index]+x0[z][b, 0]) % r.Q
                grad[z][b, index] = (grad[z][b, index]+x0[z][a, 0]) % r.Q
        for index, (a, b) in enumerate(sq):
            for z in range(2):
                gs[z][a, index] = (gs[z][a, index]+x0[z][b, 0]) % r.Q
                gs[z][b, index] = (gs[z][b, index]+x0[z][a, 0]) % r.Q
        grad = r.sub(grad, r.mm(gs, H))
        rr, cc = r.rank_pivots(transpose(grad))
        assert len(rr) == 71
        jac = transpose(r.cols(grad, rr))
        Hs = r.cols(H, rr)
        selected_pairs = [pairs[j] for j in rr]
        rng = random.Random(410471830000+position)
        for attempt in range(1, 101):
            seed, uc = r.rational_trace(A1, rng)
            J = (np.vstack([jac[0], fc[0].T, uc[0].T]), np.vstack([jac[1], fc[1].T, uc[1].T]))
            if len(r.rank_pivots(J)[0]) == 73:
                break
        else:
            raise RuntimeError('No unit local parameter on actual T2 target')
        Ji = r.inverse_matrix(J)
        assert r.equal(r.mm(J, Ji), r.eye(73))
        previous = saved.get(item['label'])
        if previous:
            assert previous['parameter_coefficients'] == r.to_json(uc)
            assert previous['selected_quadric_pairs_1based'] == [[a+1, b+1] for a, b in selected_pairs]
            jets = [transpose(r.from_json([v])) for v in previous['normalized_weight2_coefficients']]
            assert r.equal(jets[0], x0)
        else:
            jets = [x0]
        for k in range(len(jets), order+1):
            nonlinear = r.zeros(1, 71)
            for j in range(1, k):
                term = r.sub(bilinear(jets[j], jets[k-j], selected_pairs), r.mm(bilinear(jets[j], jets[k-j], sq), Hs))
                nonlinear = r.add(nonlinear, term)
            rhs = r.zeros(73, 1)
            for z in range(2):
                rhs[z][:71, 0] = -nonlinear[z][0] % r.Q
            rhs[0][72, 0] = int(k == 1)
            jets.append(r.mm(Ji, rhs))
        for k in range(order+1):
            allpairs, squared = r.zeros(1, len(pairs)), r.zeros(1, 199)
            for j in range(k+1):
                allpairs = r.add(allpairs, bilinear(jets[j], jets[k-j], pairs))
                squared = r.add(squared, bilinear(jets[j], jets[k-j], sq))
            assert r.equal(allpairs, r.mm(squared, H))
            fvalue, uvalue = r.mm(transpose(fc), jets[k]), r.mm(transpose(uc), jets[k])
            if k:
                expected = r.zeros(1, 1)
                expected[0][0, 0] = int(k == 1)
                assert r.iszero(fvalue) and r.equal(uvalue, expected)
        # Recover the actual local z as a cubic series in the original source
        # parameter and compare every independent GP anchor coefficient.
        zcoeff = [r.zeros(1, 1)]+[r.mm(transpose(uc), a) for a in anchor[1:]]
        assert r.units(zcoeff[1])[0, 0]
        powers = [[r.eye(1)]+[r.zeros(1, 1) for _ in range(3)]]
        for k in range(1, 4):
            power = []
            for n in range(4):
                value = r.zeros(1, 1)
                for j in range(n+1):
                    value = r.add(value, r.mul(powers[-1][j], zcoeff[n-j]))
                power.append(value)
            powers.append(power)
        for n in range(4):
            value = r.zeros(73, 1)
            for k in range(n+1):
                value = r.add(value, r.mul(jets[k], powers[k][n]))
            assert r.equal(value, anchor[n]), 'Actual independent target cubic anchor mismatch'
        encoded = [r.to_json(transpose(v))[0] for v in jets]
        record = {k: item[k] for k in ['label', 'branch_index_0based', 'first_family_position_0based', 'source_point_index_1based']}
        record.update({'order': order, 'selected_quadric_pairs_1based': [[a+1, b+1] for a, b in selected_pairs],
                       'parameter_seed': r.to_json(seed), 'parameter_coefficients': r.to_json(uc),
                       'parameter_attempt': attempt, 'unit_jacobian_determinant': determinant(J),
                       'parameter_cubic_in_original_source_t': [r.to_json(v)[0][0] for v in zcoeff],
                       'independent_modular_anchor_orders': 3, 'all_2701_quadrics_coefficientwise_verified': True,
                       'normalized_weight2_coefficients': encoded,
                       'jets_sha256': hashlib.sha256(json.dumps(encoded, separators=(',', ':')).encode()).hexdigest(),
                       'latest_requiring_inventory_sha256': isha})
        if previous:
            record['previous_order_history'] = previous.get('previous_order_history', [])+[{'order': previous['order'], 'jets_sha256': previous['jets_sha256']}]
        saved[item['label']] = record
        out['records'] = sorted(saved.values(), key=lambda a: (a['branch_index_0based'], a['first_family_position_0based']))
        out['maximum_order'] = max(a['order'] for a in out['records'])
        out['status'] = 'actual target discs with unit73 Jacobian, all2701 global quadrics and all independent cubic anchors verified; only required nonunit discs generated'
        sha, size = write_checkpoint(args.output, out)
        print('ACTUAL T2 LOCAL DISC', item['label'], 'order', order, 'saved', len(saved), 'bytes', size,
              'sha', sha, 'seconds', round(time.monotonic()-start, 2),
              'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
