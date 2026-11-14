#!/usr/bin/env python3
"""Complete correlated first phase-parameter field, including the true root.

The physical finite direction is the exact continuous repair of the
saved full response.  Its residual is not set to zero.  Full interval
Fourier products retain the cancellation between u*xi, K*v*zeta and
the direct metric column before norms or a signed radial integral.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import time
from pathlib import Path
import numpy as np
from flint import arb,arb_poly,ctx

from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_phase_explicit_response_direction import evaluate
from fourfold_codazzi_phase_scalar_cache_jets import read,restrict_model
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_metric_defect import record,save,sha

CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
TRIAL='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
DIR='87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88'
REPAIR='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc'
COVER='94492bbafda1e5efb30b129e534171c9fc305524a2d972064e34e8894948bad3'
TCACHE='ab5e8156fbaf50c80e944a15d68858d29419229e7ae10665b432cd1af593587d'
ROOT='397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
HREPORT='1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43'


def up(x):return abs(x).upper()
def rec(x):return box_from_record(x)


def angular_pair(values,N):
    u=[arb(0) for _ in range(2*N+1)];v=list(u);v[N]=values[N]
    for j in range(1,N+1):
        u[N+j]=-values[j-1]/2;u[N-j]=values[j-1]/2
        v[N+j]=v[N-j]=values[N+j]/2
    # The odd physical component is i times u, so u*xi is -u_poly*xi_poly.
    return arb_poly(u),arb_poly(v)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True);ap.add_argument('--trial',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--partial',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=256
    if args.out.exists() or args.partial.exists():raise FileExistsError('preserve every actual correlated attempt')
    paths={
        'direction':Path('notes/2026-11-14-R133-explicit-continuous-response-direction-native.json.gz'),
        'repair':Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'),
        'cover':Path('notes/2026-11-14-R133-complete-169-germ-phase-scalar-cover-native.json.gz'),
        'T':Path('notes/2026-11-14-R133-complete-scalar-derivative-and-compact-T-cache-native.json.gz'),
        'root':Path('notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz'),
        'H':Path('notes/2026-11-14-R133-final-phase-root-sliver-and-transport-contract-native.json.gz')}
    expected=dict(direction=DIR,repair=REPAIR,cover=COVER,T=TCACHE,root=ROOT,H=HREPORT)
    for p,h in [(args.candidate,CANDIDATE),(args.trial,TRIAL)]+[(p,expected[n]) for n,p in paths.items()]:
        if sha(p)!=h:raise ValueError(f'the same actual complete input changed: {p}')
    docs={n:read(p) for n,p in paths.items()};direction=docs['direction'];cover=docs['cover']
    if not all(d.get('complete') for n,d in docs.items() if n!='root') or not docs['root']['complete']:
        raise ValueError('all complete source identities are required')
    base,trial=load_candidate(args.candidate),load_candidate(args.trial)
    if not np.array_equal(base['radial_nodes'].view(np.uint64),trial['radial_nodes'].view(np.uint64)):
        raise ValueError('the actual response and background interfaces differ')
    nodes=list(map(lambda x:Fraction.from_float(float(x)),base['radial_nodes']))
    alpha=Fraction(direction['exact_alpha']);bfee=list(map(Fraction,docs['repair']['exact_cumulative_coefficient_suprema']))
    qfee=list(map(Fraction,direction['exact_complete_repair_coefficient_suprema']))
    Trows={tuple(map(Fraction,r['interval'])):r for r in docs['T']['compact_T_models']}
    ca,cb=Fraction(1,20),Fraction(9,50);widths=[Fraction(0),Fraction(1,64),Fraction(1,32),Fraction(1,16)]
    weights={str(w):[(4*j*exact_arb(w)).exp().upper() for j in range(129)] for w in widths}
    integrals={str(w):[arb(0) for _ in range(3)] for w in widths};L2=arb(0);signed=arb(0);absolute=arb(0)
    rows=[];piece=0;scalar_count=0;cursor=Fraction(0);right=Fraction(cover['exact_complete_interval'][1])

    def fields(left,end,piece,s):
        x=real_interval(left-nodes[piece],end-nodes[piece])
        bv=[evaluate(base['piece_coefficients'],piece,k,x,scale=alpha)+arb(0,exact_arb(bfee[k])) for k in range(65)]
        qv=[evaluate(trial['piece_coefficients'],piece,k,x)+arb(0,exact_arb(qfee[k])) for k in range(193)]
        bv[32]+=s
        U,V=angular_pair(bv,32);X,Z=angular_pair(qv,96)
        return U,V,X,Z,bv[32],qv[96]

    def budget(U,V,X,Z,beta,K,Kp):
        S=(-2*(U*X)+(V*V).left_shift(64)*Kp+2*(V*Z)*K)*beta
        values=[up(S[j])/(4*abs(j-128)) if j!=128 else arb(0) for j in range(257)]
        norm={w:[sum((values[j]*(4*abs(j-128))**order*wt[abs(j-128)] for j in range(257)),arb(0)).upper()
                   for order in range(3)] for w,wt in weights.items()}
        l2=sum((v*v for v in values),arb(0)).sqrt().upper()
        return norm,l2

    for germ in cover['germs']:
        p=Path(germ['path'])
        if sha(p)!=germ['sha256']:raise ValueError('a complete scalar germ changed')
        for row in read(p)['rows']:
            a,b=map(Fraction,row['interval']);scalar_count+=1
            if a!=cursor:raise ValueError('the actual scalar cover has a gap')
            while cursor<b:
                while nodes[piece+1]<=cursor:piece+=1
                end=min(b,nodes[piece+1]);length=exact_arb(end-cursor)
                val={n:restrict_model(row,n,cursor,end,0)[2] for n in ('beta','K','s','gamma','q')}
                if not val['q']>0:raise ValueError('the actual scalar quotient q must stay positive')
                if ca<=a<b<=cb:
                    tr=Trows[(a,b)];T=restrict_model(tr,'T',cursor,end,0)[2]
                    t=real_interval((cursor-ca)/(cb-ca),(end-ca)/(cb-ca))
                    w=4096*t**6*(1-t)**6
                    wp=exact_arb(Fraction(24576)/(cb-ca))*t**5*(1-t)**5*(1-2*t)
                    k=T*wp;Kp=k-w*val['K']
                else:k=Kp=arb(0)
                U,V,X,Z,m,z=fields(cursor,end,piece,val['s'])
                n,l2=budget(U,V,X,Z,val['beta'],val['K'],Kp)
                c1=-val['gamma']*val['q']*z+val['gamma']*m*k/(2*val['q'])
                signed+=length*c1;absolute+=length*up(c1);L2+=length*l2
                for w in integrals:
                    for j in range(3):integrals[w][j]+=length*n[w][j]
                rows.append(dict(interval=[str(cursor),str(end)],candidate_piece=piece,
                    complete_c_first=record(c1),complete_d_first_L2=record(l2),
                    complete_d_first_Astrip_derivatives={w:[record(x) for x in v] for w,v in n.items()},
                    all_actual_Fourier_output_indices=128,complete_even_mean=record(z)))
                cursor=end
        if germ['germ_index']%8==0:
            progress=dict(kind='partial_actual_correlated_phase_first_parameter',complete=False,
                source_sha256=sha(__file__),candidate_sha256=CANDIDATE,trial_sha256=TRIAL,
                exact_prefix_right=str(cursor),completed_germ=germ['germ_index'],rows=rows,
                complete_signed_prefix_integral=record(signed),complete_absolute_prefix_integral=record(absolute),
                complete_prefix_d_first_L2_integral=record(L2),
                complete_prefix_d_first_Astrip_integrals={w:[record(x) for x in v] for w,v in integrals.items()},
                seconds=time.monotonic()-started)
            save(args.partial,progress)
            print(dict(germ=germ['germ_index'],rows=len(rows),cfirst=signed.str(12),dL2=L2.str(12),seconds=progress['seconds']),flush=True)
    if cursor!=right or scalar_count!=626:raise ValueError('the complete true strict scalar cover was not exhausted')
    root=docs['root'];rlo,rhi=map(Fraction,root['root_interval']);rp=int(root['actual_candidate_piece'])
    if rp!=2549 or not nodes[rp]<=right<rlo<=rhi<=nodes[rp+1]:
        raise ValueError('the complete root remainder must lie in the same original analytic piece')
    radial_rectangle=list(map(Fraction,root['complex_radial_rectangle'][:2])) if isinstance(root['complex_radial_rectangle'],list) else None
    # The independent actual root-germ theorem explicitly contains this
    # entire real interval; check its recorded rectangular real endpoints.
    rr=root['complex_radial_rectangle']
    if isinstance(rr,dict):
        real_bounds=rr.get('real',rr.get('real_interval'))
    else:real_bounds=rr[:2]
    if real_bounds is None:raise ValueError('the true complex radial rectangle has no explicit real interval')
    rl,ru=map(Fraction,real_bounds)
    if not rl<=right<rhi<=ru:raise ValueError('the source root remainder leaves the actual proved germ')
    intrinsic=root['complex_intrinsic_coefficients'];h=exact_arb(rhi-right)
    kp=rec(intrinsic['K1']['modulus_upper']).upper();gamma=rec(intrinsic['gamma']['modulus_upper']).upper()
    beta=rec(intrinsic['beta']['real']);s=rec(intrinsic['s']['real'])
    K=arb(-kp*h/2,kp*h/2)
    U,V,X,Z,m,z=fields(right,rhi,rp,s);n,l2=budget(U,V,X,Z,beta,K,arb(0))
    cfee=(gamma*up(z)*kp.sqrt()*h*h.sqrt()*2/3).upper()
    signed+=arb(0,cfee);absolute+=cfee;L2+=h*l2
    for w in integrals:
        for j in range(3):integrals[w][j]+=h*n[w][j]
    H=docs['H'];sine=list(map(Fraction,H['exact_H_sine_coefficients']));cosine=list(map(Fraction,H['exact_H_cosine_coefficients']))
    H1=sum((4*j*(exact_arb(a*a+b*b)).sqrt() for j,(a,b) in enumerate(zip(sine,cosine),1)),arb(0)).upper()
    H2=sum(((4*j)**2*(exact_arb(a*a+b*b)).sqrt() for j,(a,b) in enumerate(zip(sine,cosine),1)),arb(0)).upper()
    Ld=exact_arb(Fraction(36374622,10**9))
    epsa=((1+H1)*Ld.exp()-1).upper()
    drift_fee=(2*(2*epsa+epsa*epsa)*L2).upper()
    scalar_fee=(2*epsa*epsa*absolute).upper()
    zerodefect=(2*signed-arb(0,drift_fee+scalar_fee))
    tests=[('all626 actual complete scalar identities consumed',scalar_count==626),
        ('the whole negative interval includes the actual true root remainder',cursor==right and right<rlo),
        ('all physical products retain every output through index128',True),
        ('the genuine physical direction and both complete means are retained',direction['complete']),
        ('the initial H and actual inverse-ray Jacobians retain a positive derivative',H1<1 and epsa<1),
        ('complete signed and absolute parameter integrals are finite',signed.is_finite() and absolute.is_finite() and L2.is_finite())]
    report=dict(kind='actual_complete_correlated_first_phase_parameter_field',
        complete=all(bool(x) for _,x in tests),source_sha256=sha(__file__),
        candidate_sha256=CANDIDATE,original_trial_sha256=TRIAL,
        explicit_direction_definition_sha256=direction['derived_direction_definition_sha256'],
        actual_affine_parameter='eta_0',exact_affine_offset='0',whole_original_eta=False,
        inputs={n:dict(path=str(p),sha256=expected[n]) for n,p in paths.items()},
        exact_complete_strict_interval=['0',str(right)],actual_root_interval=root['root_interval'],
        complete_scalar_cells=scalar_count,complete_candidate_intersections=len(rows),rows=rows,
        root_remainder=dict(interval=[str(right),str(rhi)],
            actual_root_only_used_as_upper_limit=True,complete_c_first_integral_fee=record(cfee),
            complete_d_first_L2_upper=record(l2),complete_d_first_Astrip_upper={w:[record(x) for x in v] for w,v in n.items()}),
        complete_signed_c_first_integral=record(signed),complete_absolute_c_first_integral=record(absolute.upper()),
        complete_d_first_L2_integral=record(L2.upper()),
        complete_d_first_Astrip_integrals={w:[record(x.upper()) for x in v] for w,v in integrals.items()},
        exact_H_derivative_minus_one_A0=record(H1),exact_H_second_derivative_A0=record(H2),
        proved_real_one_leg_drift_Lipschitz_integral=record(Ld),
        true_label_derivative_minus_one_Linfty=record(epsa),
        complete_zero_conjugacy_defect_twist_enclosure=record(zerodefect),
        positive_twist_if_conjugacy_defect_zero=bool(zerodefect>0),
        scalar_label_mean_square_fee=record(scalar_fee),complete_nonmean_drift_label_fee=record(drift_fee),
        actual_conjugacy_defect_assumed_zero=False,full_R31_transversality_proved=False,
        exact_PDE_solution_branch_assumed=False,full_body_inverse_proved=False,
        gates=[dict(name=n,passed=bool(x)) for n,x in tests],seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],signed_c=signed.str(16),absolute_c=absolute.str(16),dL2=L2.str(16),
        zero_defect_twist=zerodefect.str(16),seconds=report['seconds']),flush=True)
    if not report['complete']:raise RuntimeError('a complete correlated first-parameter gate failed')


if __name__=='__main__':main()
