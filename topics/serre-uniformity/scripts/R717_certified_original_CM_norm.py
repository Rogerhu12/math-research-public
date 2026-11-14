#!/usr/bin/env python3
"""Certified original S2*S3 via AFE bins, ball DFTs, and integral traces.

The mathematical specification is R717.  Formal runs belong on the public
repository's GitHub Actions.  Completed compatible artifacts are reused.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import time

from flint import acb, acb_poly, arb, ctx, fmpz, fmpz_poly
import flint


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()


def digest(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def save_gzip(path, obj):
    path = Path(path)
    tmp = path.with_name(path.name + '.next')
    with tmp.open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0,
                           compresslevel=6) as stream:
            stream.write(canonical(obj))
            stream.write(b'\n')
    tmp.replace(path)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_gzip(path):
    with gzip.open(path, 'rt') as stream:
        return json.load(stream)


def serial_arb(x):
    m, e = x.mid().man_exp()
    r, f = x.rad().man_exp()
    return [str(m), int(e), str(r), int(f)]


def load_arb(v):
    return arb((int(v[0]), v[1]), (int(v[2]), v[3]))


def serial_acb(x):
    return [serial_arb(x.real), serial_arb(x.imag)]


def fm(x, y, modulus):
    a, b = x
    c, d = y
    return ((a*c-b*d) % modulus, (a*d+b*c-b*d) % modulus)


def fp(x, exponent, modulus):
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = fm(out, x, modulus)
        exponent >>= 1
        if exponent:
            x = fm(x, x, modulus)
    return out


def neg_index(i, n):
    return (-i) % n


def exact_tame_checks():
    zeta = (0, 1)

    def zm(x, y):
        a, b = x
        c, d = y
        return (a*c-b*d, a*d+b*c-b*d)

    def zp(x, power):
        out = (1, 0)
        for _ in range(power):
            out = zm(out, x)
        return out

    mod3 = {(1, 0): (1, 0), (0, 1): (1, 1), (2, 2): (1, 2),
            (2, 0): (-1, 0), (0, 2): (-1, 1), (1, 1): (-1, 2)}
    mod2 = {(1, 0): 0, (0, 1): 1, (1, 1): 2}
    rows = []
    total = (0, 0)
    lookup = {}
    for a in range(6):
        for b in range(6):
            if (a % 3, b % 3) not in mod3 or (a % 2, b % 2) not in mod2:
                continue
            sign, i = mod3[(a % 3, b % 3)]
            j = mod2[(a % 2, b % 2)]
            h = (j-i) % 3
            eta = tuple(sign*x for x in zp(zeta, h))
            term = zm(eta, zp((1, 1), b))
            total = tuple(x+y for x, y in zip(total, term))
            rows.append({'a': a, 'b': b, 'chi': list(eta), 'term': list(term)})
            lookup[(a, b)] = (sign, h)
    assert len(rows) == 18 and total == (-6, 0)
    return lookup, {'tau6': list(total), 'all_eighteen_terms': rows,
                    'tau_p_proved_value': 'p', 'CRT_extra_factor': -1,
                    'tau_6p_proved_value': '6*p', 'both_root_numbers': 1}


def field_data(p):
    n = p+1
    factors = [int(q) for q, _ in fmpz(n).factor()]
    gamma = None
    # Every nonzero field element is allowed; scanning (a,1) covers all
    # finite projective classes, and a/bar(a) covers the norm-one group.
    for a in range(p):
        norm = (a*a-a+1) % p
        sq = fm((a, 1), (a, 1), p)
        candidate = tuple(x*pow(norm, -1, p) % p for x in sq)
        if any(fp(candidate, n//q, p) == (1, 0) for q in factors):
            continue
        if fp(candidate, n//3, p) != (0, 1):
            candidate = fp(candidate, n-1, p)
        assert fp(candidate, n//3, p) == (0, 1)
        gamma = candidate
        break
    assert gamma is not None
    powers = []
    logs = {}
    u = (1, 0)
    for j in range(n):
        assert u not in logs
        logs[u] = j
        powers.append(list(u))
        u = fm(u, gamma, p)
    assert u == (1, 0) and len(logs) == n
    inverses = [0]*p
    inverses[1] = 1
    for j in range(2, p):
        inverses[j] = (p-p//j)*inverses[p % j] % p
    projective = []
    for t in range(p):
        norm = (1-t+t*t) % p
        norminv = inverses[norm]
        ratio = ((1-t*t)*norminv % p, (2*t-t*t)*norminv % p)
        projective.append(logs[ratio])
    projective.append(logs[(p-1, p-1)])  # a=0, b != 0: theta(zeta)=zeta^2
    assert projective[-1] == 2*n//3
    assert len(set(projective)) == n
    record = {'basis': ['1', 'zeta'], 'relation': 'zeta^2+zeta+1=0',
              'gamma': list(gamma), 'order': n, 'prime_factors_order': factors,
              'gamma_to_n_over_3': [0, 1],
              'all_powers_sha256': digest(powers),
              'projective_log_table_sha256': digest(projective)}
    return inverses, projective, record


def tail_bound(r, cp, cutoff):
    x = cp*cutoff
    term = arb(1)
    poly = arb(r+1)
    for j in range(1, r+1):
        term = term*x/j
        poly += (r-j+1)*term
    return 4*(-x).exp()*poly/cp


def configuration(args):
    p = args.prime
    assert p >= 41 and p % 6 == 5 and fmpz(p).is_prime()
    if flint.__version__ != '0.9.0':
        raise RuntimeError('This certificate pins python-flint 0.9.0')
    D = 2**37*3**26*p**5
    tailbits = args.tail_bits or max(192, D.bit_length()+3*p.bit_length()+80)
    precision = args.prec_bits or tailbits+2*(p+1).bit_length()+64
    ctx.prec = precision
    cp = arb.pi()/(3*arb(3).sqrt()*p)
    multiplier = args.cutoff_multiple or math.ceil(1.2*(tailbits+2*p.bit_length()+25))
    while True:
        cutoff = multiplier*p
        tails = [tail_bound(r, cp, cutoff) for r in (2, 3)]
        target = arb((1, -tailbits))
        if all(t < target for t in tails):
            break
        if args.cutoff_multiple:
            raise RuntimeError('The requested cutoff does not certify both analytic tails')
        multiplier += 10
    inv, projective, field = field_data(p)
    tame_lookup, tame_check = exact_tame_checks()
    cfg = {'result': 'R717', 'prime': p, 'n': p+1, 'D': str(D),
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'python_flint': flint.__version__, 'prec_bits': precision,
           'tail_bits': tailbits, 'cutoff': cutoff, 'cutoff_multiple': multiplier,
           'a_max': math.isqrt((4*cutoff)//3), 'shard_count': args.shard_count,
           'finite_field': field,
           'normalization': 'R588 original chi6, theta_{-1}, S2*S3/C0^2; R717 v1'}
    cfg['parameter_sha256'] = digest(cfg)
    return cfg, cp, inv, projective, tame_lookup, tame_check, tails


def integer_pair_mul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c-b*d)


def rotate_and_sign(x, sign, power):
    a, b = x
    if power == 1:
        a, b = -b, a-b
    elif power == 2:
        a, b = b-a, -a
    return sign*a, sign*b


def bins_path(outdir, shard):
    return outdir / f'R717-bins-{shard}.json.gz'


def run_bins(args, cfg, cp, inverses, projective, tame_lookup):
    outdir = args.output_dir
    path = bins_path(outdir, args.shard_index)
    n, p = cfg['n'], cfg['prime']
    if path.exists():
        saved = read_gzip(path)
        if saved['configuration'] != cfg or saved['shard_index'] != args.shard_index:
            raise RuntimeError('Existing bin checkpoint has incompatible source or parameters')
        if saved['complete']:
            print(json.dumps({'status': 'REUSED_COMPLETE', 'path': str(path),
                              'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}), flush=True)
            return
        bins = [[load_arb(x) for x in row] for row in saved['bins']]
        last = saved['completed_through_a']
        rows = saved['row_count']
        terms = saved['term_count']
    else:
        bins = [[arb(0) for _ in range(n)] for _ in range(4)]
        last, rows, terms = 0, 0, 0
    step_exp = (-2*cp).exp()
    started = time.monotonic()

    def checkpoint(complete):
        payload = {'configuration': cfg, 'shard_index': args.shard_index,
                   'complete': complete, 'completed_through_a': last,
                   'row_count': rows, 'term_count': terms,
                   'bin_basis': ['5:1', '5:zeta', '7:1', '7:zeta'],
                   'bins': [[serial_arb(x) for x in row] for row in bins]}
        sha = save_gzip(path, payload)
        print(json.dumps({'phase': 'bins', 'shard': args.shard_index,
                          'a': last, 'rows': rows, 'terms': terms,
                          'complete': complete, 'sha256': sha,
                          'elapsed_seconds': round(time.monotonic()-started, 3)}), flush=True)

    for a in range(args.shard_index+1, cfg['a_max']+1, args.shard_count):
        if a <= last:
            continue
        discr = 4*cfg['cutoff']-3*a*a
        assert discr >= 0
        root = math.isqrt(discr)
        lo = max(0, (a-root+1)//2)
        hi = min(a-1, (a+root)//2)
        if lo <= hi:
            norm0 = a*a-a*lo+lo*lo
            expn = (-cp*norm0).exp()
            ratio = (-cp*(2*lo+1-a)).exp()
            amod = a % p
            ainv = inverses[amod] if amod else 0
            for b in range(lo, hi+1):
                norm = a*a-a*b+b*b
                assert 0 < norm <= cfg['cutoff']
                tame = tame_lookup.get((a % 6, b % 6))
                bmod = b % p
                if tame is not None and (amod or bmod):
                    k = projective[bmod*ainv % p] if amod else projective[p]
                    sign, power = tame
                    x = cp*norm
                    x2 = x*x
                    kernel2 = 1+x+x2/2
                    kernel3 = kernel2+x2*x/6
                    weight2 = expn*kernel2/(norm**3)
                    weight3 = expn*kernel3/(norm**4)
                    aa = (a, b)
                    square = integer_pair_mul(aa, aa)
                    fourth = integer_pair_mul(square, square)
                    fifth = integer_pair_mul(fourth, aa)
                    seventh = integer_pair_mul(fifth, square)
                    u5, v5 = rotate_and_sign(fifth, sign, power)
                    u7, v7 = rotate_and_sign(seventh, sign, power)
                    bins[0][k] += u5*weight2
                    bins[1][k] += v5*weight2
                    bins[2][k] += u7*weight3
                    bins[3][k] += v7*weight3
                    terms += 1
                expn *= ratio
                ratio *= step_exp
        last = a
        rows += 1
        if rows % args.checkpoint_rows == 0:
            checkpoint(False)
    checkpoint(True)


def chirps(n):
    # Evaluate each exact phase independently.  Recursively multiplying
    # rectangular complex balls accumulates wrapping over long rotations.
    return [(acb((j*j) % (2*n))/n).exp_pi_i() for j in range(n)]

def ball_dft(values, chirp, sign):
    n = len(values)
    assert sign in (-1, 1) and len(chirp) == n
    c = chirp if sign == 1 else [x.conjugate() for x in chirp]
    a = [values[j]*c[j] for j in range(n)]
    b = [acb(0) for _ in range(2*n-1)]
    for j in range(n):
        v = c[j].conjugate()
        b[n-1+j] = v
        b[n-1-j] = v
    product = acb_poly(a)*acb_poly(b)
    return [c[k]*product[n-1+k] for k in range(n)]


def padic_evaluation(p, gamma, integer_coefficients, exact_zero):
    if exact_zero:
        return {'P_exactly_zero': True, 'M2_exactly_zero': True}
    digits = 6
    while True:
        modulus = p**digits
        lift = tuple(gamma)
        for _ in range((digits+1)//2):
            lift = fp(lift, p*p, modulus)
        assert fp(lift, p+1, modulus) == (1, 0)
        assert fp(lift, (p+1)//3, modulus) == (0, 1)
        value = (0, 0)
        for coefficient in reversed(integer_coefficients):
            value = fm(value, lift, modulus)
            value = ((value[0]+coefficient) % modulus, value[1])
        assert value[1] == 0, 'Real cyclotomic descent failed in the unramified ring'
        if value[0]:
            break
        digits *= 2
    numerator = value[0]
    val_num = 0
    stripped = numerator
    while stripped % p == 0:
        val_num += 1
        stripped //= p
    val_P = val_num-5
    assert val_P >= -2, 'The original R595 lower bound is violated'
    assert val_P % 2 == 0, 'The original R711 integer valuation is violated'
    unitden = (p+1)*2**37*3**26
    leading_P = stripped % p * pow(unitden, -1, p) % p
    alpha = pow(4, pow(3, -1, p-1), p)
    c0square = 15552*pow(alpha, -2, p) % p
    leading_square = 8*c0square*leading_P % p
    mod2 = p*p
    phi2 = p*(p-1)
    alpha2 = pow(4, pow(3, -1, phi2), mod2)
    c02 = 15552*pow(alpha2, -2, mod2) % mod2
    assert numerator % (p**3) == 0 and digits >= 5
    old_norm = (numerator//(p**3))*pow(unitden, -1, mod2)*c02 % mod2
    return {'P_exactly_zero': False, 'padic_digits': digits,
            'modulus': str(modulus), 'teichmueller_lift': list(map(str, lift)),
            'integer_polynomial_value': list(map(str, value)),
            'valuation_integer_numerator': val_num, 'valuation_P': val_P,
            'valuation_M2': val_P//2, 'normalized_P_leading_mod_p': leading_P,
            'normalized_M2_square_over_zeta2_mod_p': leading_square,
            'p2_S2S3_mod_p2': old_norm, 'C0_square_mod_p2': c02,
            'alpha_mod_p2': alpha2,
            'actual_M2_unit': val_P == 0,
            'height_or_Serre_exclusion_claimed': False}



def verified_legacy_bin_inputs(args, cfg):
    """Adopt only the four fixed completed 137147 bins after a source-scope audit."""
    if args.bin_compatibility is None:
        return None
    if args.phase != 'recover':
        raise RuntimeError('Legacy bins are allowed only in explicit recover mode')
    outdir = args.output_dir.resolve()
    path = args.bin_compatibility.resolve()
    if path.parent != outdir or path.name != 'R717-reused-bin-compatibility.json':
        raise RuntimeError('The compatibility manifest must be archived in the output directory')
    manifest = json.loads(path.read_text())
    expected_bins = {
        'R717-bins-0.json.gz': 'fae9b0aadc62a36f0a5d251a17c802d698af183145cccec7f0f3b6e4352a71d8',
        'R717-bins-1.json.gz': 'eabe4b445631f071839f9cf45ec162620c0537ed1eb6e1d28d79b27d66316f6a',
        'R717-bins-2.json.gz': '5ef6d896e45f62d7ed24be78eb70b6913a6109ac044ae74a375daca969dfeea8',
        'R717-bins-3.json.gz': 'fa90bcd9cfe7b392dbcd6ea526eb765ef819770418cbe2df1530a71a0773496b',
    }
    old_source_sha = '75a81149a898e71ab33413ddd2cebc49a4b8abdbe6e8c0bc964a56092098d402'
    old_parameter_sha = '1a174a52ff6037bd8b6c963884869b21b38240d1f54b9acf94ad338e2c5fef71'
    assert manifest['schema'] == 'R717-fixed-bins-direct-chirps-v1'
    assert manifest['old_core_sha256'] == old_source_sha
    assert manifest['new_core_sha256'] == cfg['source_sha256']
    assert manifest['source_run_id'] == '43597802237'
    assert manifest['source_artifact_name'] == 'serre-cartier-R717-original-CM-norm-p137147-recover-43597802237-1'
    assert manifest['source_commit'] == 'ffc69b45d58ea9aaafd1e0686fc55377701a00be'
    assert manifest['bin_files_sha256'] == expected_bins
    assert manifest['original_source_archive'] == 'R717-original-binned-source.py.gz'
    archive = outdir / manifest['original_source_archive']
    archive_sha = hashlib.sha256(archive.read_bytes()).hexdigest()
    assert archive_sha == '9524db636dc1e9d033186ec9ad9d1fc3ad00f366969db964dc48340a8915201b'
    with gzip.open(archive, 'rb') as stream:
        original = stream.read()
    current = Path(__file__).read_bytes()
    assert hashlib.sha256(original).hexdigest() == old_source_sha
    assert hashlib.sha256(current).hexdigest() == cfg['source_sha256']
    marker = b'\ndef chirps(n):\n'
    assert original.count(marker) == current.count(marker) == 1
    original_prefix = original.split(marker)[0]
    current_prefix = current.split(marker)[0]
    # This exact common prefix includes imports, every bin dependency,
    # configuration(), and the entire run_bins().  Nothing is waived.
    assert original_prefix == current_prefix
    old_cfg = manifest['old_configuration']
    check_old = dict(old_cfg)
    assert check_old.pop('parameter_sha256') == old_parameter_sha
    assert digest(check_old) == old_parameter_sha
    assert old_cfg['source_sha256'] == old_source_sha
    assert old_cfg['prime'] == 137147 and old_cfg['shard_count'] == 4
    expected_cfg = dict(check_old)
    expected_cfg['source_sha256'] = cfg['source_sha256']
    expected_cfg['parameter_sha256'] = digest(expected_cfg)
    assert cfg == expected_cfg
    record = {
        'schema': manifest['schema'], 'source_run_id': manifest['source_run_id'],
        'source_commit': manifest['source_commit'],
        'source_artifact_name': manifest['source_artifact_name'],
        'old_core_sha256': old_source_sha, 'new_core_sha256': cfg['source_sha256'],
        'old_parameter_sha256': old_parameter_sha,
        'new_parameter_sha256': cfg['parameter_sha256'],
        'entire_bin_producer_prefix_byte_equal': True,
        'bin_producer_prefix_sha256': hashlib.sha256(original_prefix).hexdigest(),
        'fixed_bin_files_sha256': expected_bins,
        'all_numeric_configuration_fields_unchanged': True,
        'completed_bins_recomputed': False,
    }
    return {'configuration': old_cfg, 'files': expected_bins, 'record': record,
            'artifacts': [
                {'file': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()},
                {'file': archive.name, 'sha256': archive_sha}]}


def recover(args, cfg, tame_check, tails):
    outdir = args.output_dir
    final = outdir/'R717-exact-original-CM-norm.json'
    if final.exists():
        prior = json.loads(final.read_text())
        if prior['configuration'] != cfg or not prior['complete']:
            raise RuntimeError('Existing final receipt has incompatible parameters')
        assert prior['all_rows_covered'] and prior['all_trace_roundings_unique']
        for item in prior['artifacts']:
            path = outdir/item['file']
            assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256']
        if args.expect_p2_product is not None:
            assert prior['padic_result'].get('p2_S2S3_mod_p2') == args.expect_p2_product, (
                'Historical independent calibration failed on a reused complete result')
        print(json.dumps({'status': 'REUSED_COMPLETE', 'receipt': str(final)}), flush=True)
        return
    legacy = verified_legacy_bin_inputs(args, cfg)
    n, p = cfg['n'], cfg['prime']
    bins = [[arb(0) for _ in range(n)] for _ in range(4)]
    input_records = []
    total_rows = total_terms = 0
    for shard in range(args.shard_count):
        path = bins_path(outdir, shard)
        record = read_gzip(path)
        expected_bin_cfg = legacy['configuration'] if legacy else cfg
        assert record['configuration'] == expected_bin_cfg and record['complete']
        if legacy:
            assert hashlib.sha256(path.read_bytes()).hexdigest() == legacy['files'][path.name]
        assert record['shard_index'] == shard
        expected_rows = len(range(shard+1, cfg['a_max']+1, args.shard_count))
        assert record['row_count'] == expected_rows
        assert record['completed_through_a'] == (shard+1+(expected_rows-1)*args.shard_count
                                                if expected_rows else 0)
        total_rows += record['row_count']
        total_terms += record['term_count']
        for k in range(4):
            assert len(record['bins'][k]) == n
            for j in range(n):
                bins[k][j] += load_arb(record['bins'][k][j])
        input_records.append({'file': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    assert total_rows == cfg['a_max']
    print(json.dumps({'phase': 'merge', 'complete_rows': total_rows,
                      'lattice_terms': total_terms}), flush=True)
    root3half = arb(3).sqrt()/2
    a5 = [acb(bins[0][j]-bins[1][j]/2, bins[1][j]*root3half) for j in range(n)]
    a7 = [acb(bins[2][j]-bins[3][j]/2, bins[3][j]*root3half) for j in range(n)]
    del bins
    chirp = chirps(n)
    print(json.dumps({'phase': 'dft', 'transform': 'weight5-positive'}), flush=True)
    f5 = ball_dft(a5, chirp, 1)
    del a5
    print(json.dumps({'phase': 'dft', 'transform': 'weight7-positive'}), flush=True)
    f7 = ball_dft(a7, chirp, 1)
    del a7
    omega = (arb(1)/6).gamma()*(arb(1)/2).gamma()/(3*(arb(2)/3).gamma())
    area = arb(3).sqrt()*omega**2/(2*arb.pi())
    alpha_square = (arb(4).log()*2/3).exp()
    period_factor = alpha_square*p*p/(144*omega**2*area**5)
    analytic_error = arb(0, (1, -cfg['tail_bits']))
    D = int(cfg['D'])
    conjugates = [acb(0) for _ in range(n)]
    embedding_records = []
    for h in range(1, n):
        if math.gcd(h, n) != 1 or h % 3 != 1:
            continue
        left = 2*f5[neg_index(h, n)]
        right = 2*f7[h]
        assert left.imag.contains(0) and right.imag.contains(0)
        L5 = left.real+analytic_error
        L7 = right.real+analytic_error
        P = period_factor*L5*L7
        conjugates[h] = acb(D*P)
        conjugates[neg_index(h, n)] = acb(D*P)
        embedding_records.append({'h': h, 'L5': serial_arb(L5), 'L7': serial_arb(L7),
                                  'P': serial_arb(P)})
    assert 2*len(embedding_records) == sum(math.gcd(h, n) == 1 for h in range(n))
    del f5, f7
    analytic = {'configuration': cfg, 'tame_gauss_check': tame_check,
                'Omega': serial_arb(omega), 'A': serial_arb(area),
                'alpha_squared': serial_arb(alpha_square),
                'complete_period_factor': serial_arb(period_factor),
                'tail_bounds': [serial_arb(t) for t in tails],
                'tail_bounds_below_target': [bool(t < arb((1, -cfg['tail_bits']))) for t in tails],
                'original_primitive_character_embeddings': embedding_records}
    analytic_path = outdir/'R717-complex-embeddings.json.gz'
    analytic_sha = save_gzip(analytic_path, analytic)
    print(json.dumps({'phase': 'dft', 'transform': 'integral-traces-negative',
                      'primitive_embedding_pairs': len(embedding_records)}), flush=True)
    trace_balls = ball_dft(conjugates, chirp, -1)
    coefficients = []
    failures = []
    max_radius = arb(0)
    for j, ball in enumerate(trace_balls):
        integer = ball.unique_fmpz()
        radius = ball.real.rad()
        if radius > max_radius:
            max_radius = radius
        if integer is None or not ball.imag.contains(0) or not radius < arb(1)/4:
            failures.append(j)
            coefficients.append(None)
        else:
            coefficients.append(int(integer))
    trace_path = outdir/'R717-integral-trace-balls.json.gz'
    trace_sha = save_gzip(trace_path, {'configuration': cfg,
                                      'all_trace_balls': [serial_acb(x) for x in trace_balls],
                                      'unique_integers': [str(x) if x is not None else None for x in coefficients],
                                      'failed_indices': failures,
                                      'max_real_radius': serial_arb(max_radius)})
    if failures:
        raise RuntimeError(f'Integer trace certification failed at {len(failures)} indices; artifacts saved')
    assert all(coefficients[j] == coefficients[(-j) % n] for j in range(n))
    polynomial = fmpz_poly(coefficients)
    cyclotomic = fmpz_poly.cyclotomic(n)
    remainder = polynomial % cyclotomic
    exact_zero = remainder == 0
    integer_path = outdir/'R717-exact-integer-polynomial.json.gz'
    integer_sha = save_gzip(integer_path, {
        'configuration': cfg, 'meaning': 'T(zeta_n) = n*D*P, P=S2*S3/C0^2',
        'coefficients_ascending': list(map(str, coefficients)),
        'cyclotomic_coefficients_ascending': [str(x) for x in cyclotomic],
        'remainder_coefficients_ascending': [str(x) for x in remainder],
        'P_exactly_zero': bool(exact_zero), 'integer_trace_uniqueness_verified': True})
    padic = padic_evaluation(p, cfg['finite_field']['gamma'], coefficients, exact_zero)
    if args.expect_p2_product is not None:
        assert padic.get('p2_S2S3_mod_p2') == args.expect_p2_product, 'Historical independent calibration failed'
    artifacts = input_records+(legacy['artifacts'] if legacy else [])+[
        {'file': analytic_path.name, 'sha256': analytic_sha},
        {'file': trace_path.name, 'sha256': trace_sha},
        {'file': integer_path.name, 'sha256': integer_sha}]
    receipt = {'configuration': cfg, 'complete': True, 'all_rows_covered': True,
               'total_lattice_terms': total_terms, 'all_trace_roundings_unique': True,
               'max_real_trace_radius': serial_arb(max_radius),
               'historical_expected_p2_product': args.expect_p2_product,
               'padic_result': padic, 'artifacts': artifacts}
    if legacy:
        receipt['reused_legacy_bin_proof'] = legacy['record']
    tmp = final.with_name(final.name+'.next')
    tmp.write_text(json.dumps(receipt, indent=2)+'\n')
    tmp.replace(final)
    print(json.dumps({'status': 'PASS', 'receipt': str(final), 'padic_result': padic,
                      'receipt_sha256': hashlib.sha256(final.read_bytes()).hexdigest()}), flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prime', type=int, required=True)
    ap.add_argument('--phase', choices=['all', 'bins', 'recover'], default='all')
    ap.add_argument('--output-dir', type=Path, required=True)
    ap.add_argument('--shard-count', type=int, default=1)
    ap.add_argument('--shard-index', type=int, default=0)
    ap.add_argument('--prec-bits', type=int)
    ap.add_argument('--tail-bits', type=int)
    ap.add_argument('--cutoff-multiple', type=int)
    ap.add_argument('--checkpoint-rows', type=int, default=100)
    ap.add_argument('--expect-p2-product', type=int)
    ap.add_argument('--bin-compatibility', type=Path)
    args = ap.parse_args()
    assert 1 <= args.shard_count <= 16 and 0 <= args.shard_index < args.shard_count
    assert args.checkpoint_rows > 0
    if args.bin_compatibility is not None and args.phase != 'recover':
        raise RuntimeError('A bin compatibility manifest only authorizes recover')
    if args.phase == 'all' and args.shard_count != 1:
        raise RuntimeError('Use separate bins jobs and one recover job for sharded runs')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    cfg, cp, inv, projective, lookup, tame, tails = configuration(args)
    print(json.dumps({'phase': 'configuration', 'configuration': cfg,
                      'tail_bounds': [t.str() for t in tails]}), flush=True)
    if args.phase in ('all', 'bins'):
        run_bins(args, cfg, cp, inv, projective, lookup)
    if args.phase in ('all', 'recover'):
        recover(args, cfg, tame, tails)


if __name__ == '__main__':
    main()
