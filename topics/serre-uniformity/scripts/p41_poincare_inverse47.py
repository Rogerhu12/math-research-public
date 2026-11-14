#!/usr/bin/env python3
"""An actual left inverse in a nonzero Poincare fibre, modulo47^4.

The input fibre is (B_minus4,-B_minus4), with genuinely disjoint divisor
representatives.  This is a biextension operation, not a local height value.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
import numpy as np
import p41_r2_matrix as r
from p41_group_operations47 import load_sources, make_model, replay_negative, onebased
from p41_formal47_multiply import write_checkpoint
from p41_poincare_norms47 import norm_data
from p41_poincare_algebras47 import make_algebra, polynomial_norm, polycol
from p41_cm4_divisor47 import kernel


def scalar(A, k):
    return tuple(x*(k % r.Q) % r.Q for x in A)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('data')/'p41_poincare_inverse47_checkpoint.json.gz')
    args = parser.parse_args()
    folder = Path(__file__).with_name('data')
    sources, hashes = load_sources(folder)
    nraw = (folder/'p41_poincare_norms47_checkpoint.json.gz').read_bytes()
    norms = json.loads(gzip.decompress(nraw))
    assert norms['source_sha256'] == hashes
    M = make_model(sources)
    minus, Aminus = replay_negative(M, sources[3])
    divs, ck = sources[1], sources[3]
    K1 = r.from_json(kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'],
                            divs['canonical_kernel_block']))
    fcoeff = r.mm(K1, r.column(divs['canonical_coefficients']))
    f = r.mm(M['W'], fcoeff)
    uc, vc = [r.column(c) for seed, c in ck['norm_section_seeds_and_coefficients']]
    u, v = r.mm(M['W'], uc), r.mm(M['W'], vc)
    rng = random.Random(4104712105)
    minus_record, minus_alg = make_algebra('E_minusB', minus, norms['divisors']['E_minusB'],
                                          M, sources, u, v, rng)
    f_norm = polynomial_norm(polycol(r.mm(minus_alg[0], fcoeff), 0), minus_alg[3])
    assert f_norm is not None and f_norm[1] == 0
    print('E_minusB is disjoint from D0; norm(f/v)=', f_norm, flush=True)
    Dv = r.rows(r.mul(v, M['W']), M['P2'])
    Dv_norms = norm_data(Dv, u, f, M, rng)
    Dv_record, Dv_alg = make_algebra('D_v', Dv, Dv_norms, M, sources, u, f, rng)
    s_coeff = r.mm(M['B'], r.column(ck['negative_flip_section_seeds_and_coefficients'][0][1]))
    t_coeff = r.mm(M['B'], r.column(ck['negative_flip_section_seeds_and_coefficients'][1][1]))
    s = r.mm(M['V2'], s_coeff)
    t_norm_minus = polynomial_norm(polycol(r.mm(minus_alg[1], t_coeff), 0), minus_alg[3])
    assert t_norm_minus == [1412636, 0]
    for k in range(47):
        a_coeff = r.add(t_coeff, scalar(s_coeff, k))
        a = r.mm(M['V2'], a_coeff)
        if not np.all(r.units(a)):
            continue
        a_norm_Dv = polynomial_norm(polycol(r.mm(Dv_alg[1], a_coeff), 0), Dv_alg[3])
        if a_norm_Dv is None:
            continue
        a_norm_minus = polynomial_norm(polycol(r.mm(minus_alg[1], a_coeff), 0), minus_alg[3])
        assert a_norm_minus == t_norm_minus
        ratio = r.mul(s, r.inverse_values(a))
        scaled = r.mul(ratio, M['V2'])
        R = r.sub(scaled, r.mm(M['V2'], r.rows(scaled, M['P2'])))
        rr, cc = r.rank_pivots(R)
        assert len(rr) == 126
        Ka, free, block = r.kernel_from_rows(r.rows(R, rr), rr, cc)
        assert r.iszero(r.mm(R, Ka))
        expected = r.mm(M['A2'], r.conjugate(Ka))
        Aa = r.rows(expected, free)
        assert r.equal(r.mm(Ka, Aa), expected) and r.equal(r.mm(Aa, r.conjugate(Aa)), r.eye(73))
        break
    else:
        raise RuntimeError('No disjoint actual inverse representative in the tested pencil')
    assert a_norm_Dv[1] == 0
    # psi=a/f^2 and B_y=E_minusB-D_v.  The inverse torsor coordinate is
    # psi(B_y)^(-1)=Norm_Dv(a/f^2)*Norm_Eminus(f/v)^2/Norm_Eminus(a/v^2).
    psi_on_y = a_norm_minus[0]*pow(f_norm[0]**2*a_norm_Dv[0] % r.Q, -1, r.Q) % r.Q
    inverse_scalar = pow(psi_on_y, -1, r.Q)
    assert inverse_scalar*psi_on_y % r.Q == 1
    w = (pow(inverse_scalar, 46, r.Q)-1) % r.Q
    logscalar = (w-w*w*pow(2, -1, r.Q)+w**3*pow(3, -1, r.Q))*pow(46, -1, r.Q) % r.Q
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': r.Q,
              'source_sha256': hashes, 'norm_source_sha256': hashlib.sha256(nraw).hexdigest(),
              'initial_fibre': ['B_minus4', '-B_minus4'],
              'first_divisor': 'E_B-D0', 'second_divisor': 'E_minusB-D_v',
              'D_v': 'div_L(v), v is the R117 principal-norm denominator',
              'D_v_norm_data': Dv_norms, 'D_v_algebra': Dv_record,
              'E_minusB_algebra': minus_record,
              'norm_f_over_v_on_E_minusB': f_norm,
              'pencil_coefficient': k, 'norm_a_over_f_squared_on_D_v': a_norm_Dv,
              'norm_a_over_v_squared_on_E_minusB': a_norm_minus,
              'inverse_effective_divisor_rank_rows_1based': onebased(rr),
              'inverse_effective_divisor_rank_columns_1based': onebased(cc),
              'inverse_effective_divisor_free_columns_1based': onebased(free),
              'inverse_effective_divisor_kernel_block': r.to_json(block),
              'inverse_effective_divisor_frobenius': r.to_json(Aa),
              'rational_function': 'psi=a/f^2, a=t_negative_flip+k*s_negative_flip',
              'psi_on_second_divisor': psi_on_y,
              'left_inverse_torus_scalar': inverse_scalar, 'log_of_inverse_torus_scalar': logscalar,
              'status': 'actual left inverse in P_(B,-B) with disjoint supports; this torus logarithm is not a nonprincipal height'}
    digest, size = write_checkpoint(args.output, result)
    print('ACTUAL POINCARE LEFT INVERSE', inverse_scalar, 'log47', logscalar,
          'pencil coefficient', k, flush=True)
    print('Saved', size, 'bytes; SHA256', digest, flush=True)


if __name__ == '__main__':
    main()
