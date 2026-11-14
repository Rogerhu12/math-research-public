#!/usr/bin/env python3
"""Actual weight-two Serre derivative after clearing the 21 elliptic points."""
import argparse
import hashlib
from pathlib import Path
import random
import time
from p41_actual_differentials47 import ActualModel, P, Q, digest, report, save


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    started=time.monotonic()
    a=ActualModel(args.script_dir)
    r,np,M=a.r,a.np,a.M
    cm3=a.read('p41_cm3_makdisi47_certificate.json')
    E=r.from_json(a.cm4['coarse_point_values']+[cm3['coarse_evaluation_coefficients'][0]])
    rr,cc=r.rank_pivots(E)
    assert len(rr)==21
    K,free,block=r.kernel_from_rows(r.rows(E,rr),rr,cc)
    assert r.iszero(r.mm(E,K)) and len(free)==52
    kr,kc=r.rank_pivots(K)
    AK=r.mm(r.inverse_matrix(r.rows(K,kr)),r.rows(r.mm(M['A1'],r.conjugate(K)),kr))
    assert r.equal(r.mm(K,AK),r.mm(M['A1'],r.conjugate(K)))
    U=r.mm(M['W'],K)
    selected=r.zeros(820,0)
    ranks=[]
    for j in range(52):
        V=r.hcat(selected,r.mul(M['W'],r.cols(U,[j])))
        pr,pc=r.rank_pivots(V)
        V=r.cols(V,pc)
        selected=r.mm(V,r.inverse_matrix(r.rows(V,pr)))
        rank=len(pr)
        ranks.append(rank)
        assert rank<=178
        assert r.equal(r.mm(M['V2'],r.rows(selected,M['P2'])),selected)
        if rank==178:break
    assert rank==178
    report('H0(L-E2-E3) rank52 and product H0(2L-E2-E3) rank178 verified')
    rng=random.Random(20447)
    for attempt in range(100):
        seed=r.column([[rng.randrange(P),rng.randrange(P)] for _ in free])
        v0=r.mm(K,seed)
        v=r.add(v0,r.mm(M['A1'],r.conjugate(v0)))
        vv=r.mm(M['W'],v)
        assert r.iszero(r.mm(E,v))
        if np.all(r.units(vv)):break
    else:raise AssertionError('No unit source chart')
    jets=a.read('p41_evaluation_jets47_checkpoint.json.gz')
    WD=r.from_json(jets['evaluation_derivatives'])
    delta=r.add(a.scale(WD,-27652*pow(3,-1,Q)),a.scale(M['W'],96))
    values=r.mul(vv,delta)
    G=r.rows(values,M['P3'])
    assert r.equal(r.mm(M['V3'],G),values)
    assert r.equal(r.mm(M['A3'],r.conjugate(G)),r.mm(G,M['A1']))
    # All 52 clearing sections give honest global cubic sections, not just v.
    hashes=[]
    for j in range(52):
        val=r.mul(r.cols(U,[j]),delta)
        co=r.rows(val,M['P3'])
        assert r.equal(r.mm(M['V3'],co),val)
        hashes.append(digest(r.to_json(co)))
    out={'status':'complete actual cleared Serre derivative and integral basepoint-free cover',
         'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
         'elliptic_restriction_rank':21,'clearing_space_rank':52,'product_rank':178,
         'product_rank_history':ranks,'elliptic_kernel_coefficients':r.to_json(K),
         'elliptic_kernel_frobenius':r.to_json(AK),'chosen_clearing_section':r.to_json(v),
         'chosen_clearing_seed':r.to_json(seed),'chosen_attempt':attempt,
         'chosen_clearing_all_820_units':True,'cleared_derivative_coefficients':r.to_json(G),
         'cleared_derivative_sha256':digest(r.to_json(G)),
         'all_52_cleared_derivative_sha256':hashes,'all_52_full_evaluation_equalities':True,
         'entries_checked_per_clearing_section':59860,'Frobenius':True,
         'formula':'delta(W)=W_derivative/beta0+96W; G=v*delta(W), beta0=-3/27652',
         'input_sha256':a.inputs,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'engine_sha256':hashlib.sha256(Path(__file__).with_name('p41_actual_differentials47.py').read_bytes()).hexdigest()}
    h=save(args.output,out)
    report('All52 cubic identities and Frobenius verified; seconds='+str(round(time.monotonic()-started,3)))
    print(str(args.output)+' SHA256 '+h,flush=True)


if __name__=='__main__':main()
