#!/usr/bin/env python3
"""Complete directed positive-weight comparison on the actual Codazzi tube.

All finite BC/weight polynomials are multiplied before interval collapse.
The two signs of each cooperative row are separately cleared by C^2.
Actual target-constant differences and the full nonlinear error-tube terms
are paid afterwards on every closed angular/radial/parameter box.
This producer encloses the weight inequalities; it does not itself claim
that the unweighted continuation bootstrap closes.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
import time
import numpy as np
from flint import arb,ctx
from fourfold_phase_beta_bulk_box import DirectedFFT
from fourfold_phase_newton_source_centered import CenteredPolynomial
from fourfold_phase_codazzi_continuation_validate import positive_to_full,maxabs
from fourfold_phase_two_jet_newton_source import Box,CBox,zeros,arb_box,square_box,record,save,sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_codazzi_cubic_cleared_residual import (
    candidate_radial_series,real_sample_series,p_add,p_mul,p_scale,p_derivative,p_eval,
    numerator_polynomials,actual_ball)
from fourfold_codazzi_piecewise_barrier import read_json
from fourfold_codazzi_sharded_candidate import ShardedExactCandidate
from fourfold_codazzi_positive_weight_candidate import ExactWeightCandidate,STORAGE


def angular_coefficients(polynomials,angles):
    """Batched complete closed-angle bounds, before radial collapse."""
    if not polynomials:raise ValueError('empty exact polynomial list')
    grid=polynomials[0].grid;fft=polynomials[0].fft
    if angles<grid or angles&(angles-1):raise ValueError('complete power-of-two angular grid required')
    modes=np.asarray([j if j<grid//2 else j-grid for j in range(grid)])
    physical=4*modes;block=zeros((angles,3*len(polynomials)))
    for j,p in enumerate(polynomials):
        if p.grid!=grid or p.fft is not fft:raise ValueError('different exact finite polynomial algebras')
        value=p.c
        for q in range(3):
            block[modes%angles,3*j+q]=value
            value=value*CBox(0.,Box(physical))
    samples=fft.fft(block,inverse=True)*angles
    if not np.all((samples.imag.lo<=0)&(samples.imag.hi>=0)):
        raise ValueError('closed-angle exact real polynomial lost zero imaginary part')
    half=arb.pi()/(4*angles);h=arb_box(half);output=[]
    for j,p in enumerate(polynomials):
        remainder=(p.error+half**3*p.norm(3)/6).upper()
        fee=(h*Box(samples.real[:,3*j+1].abs_upper())
             +h*h*Box(samples.real[:,3*j+2].abs_upper())/2+arb_box(remainder)).hi
        output.append(samples.real[:,3*j]+Box(-fee,fee))
    return output


def finite_fields(candidate,coefficients,half,angles):
    """Pointwise radial Horner bounds retain the angular location of variation."""
    all_polynomials=[];groups={};frequency=CBox(0.,Box(candidate.frequencies))
    for component in range(2):
        for order in range(2):
            indices=[]
            for coefficient in coefficients:
                full=positive_to_full(coefficient,candidate.grid)[:,component]
                if order:full=full*frequency
                indices.append(len(all_polynomials))
                all_polynomials.append(CenteredPolynomial(full,arb(0),candidate.degree,
                                                          candidate.target.polynomial_fft))
            groups[(component,order)]=indices
    bounded=angular_coefficients(all_polynomials,angles);u=Box(-1.,1.)
    fields={}
    for key,indices in groups.items():
        values=[bounded[j] for j in indices]
        fields[key]=p_eval(values,u)
        if key[1]==0:
            fields[(key[0],'r')]=p_eval(p_derivative(values,arb_box(1/exact_arb(half))),u)
    return fields


def scalar_constant(full,key):
    value=float(full[key].mid())
    return value,full[key]-arb(value)


def row_budget(bc,weights,item,left,right,wpiece,angles,tubes):
    full={k:actual_ball(v) for k,v in item['true_target_coefficients'].items()}
    if not full['K']<0 or not full['k']>0:raise ValueError('actual target negative chart required')
    bcoef,half=candidate_radial_series(bc,item['piece'],left,right)
    wcoef,whalf=candidate_radial_series(weights,wpiece,left,right)
    if half!=whalf:raise ValueError('inconsistent exact normalized radial variable')
    B,C,Bt,Ct=real_sample_series(bc,bcoef)
    Wp,Wq,Wpt,Wqt=real_sample_series(weights,wcoef)
    Wpr=p_derivative(Wp,arb_box(1/exact_arb(half)))
    Wqr=p_derivative(Wq,arb_box(1/exact_arb(half)))
    constants={};differences={}
    for name in ('k','gamma','beta','kappa'):
        constants[name],differences[name]=scalar_constant(full,name)
    k,gamma,beta,kappa=[Box(constants[k]) for k in ('k','gamma','beta','kappa')]
    Bplus=p_add(B,[k]);Bminus=p_add(B,[-k])
    B2,C2=p_mul(B,B),p_mul(C,C)
    PQnumerator=p_add(B2,[-k*k])
    common=p_add(p_scale(PQnumerator,-2*beta),p_scale(C2,kappa))
    hp=p_add(p_add(p_scale(p_mul(p_mul(C,Bminus),Wpt),gamma),p_mul(common,Wp)),
             p_scale(p_mul(C2,Wpr),-1))
    hq=p_add(p_add(p_scale(p_mul(p_mul(C,Bplus),Wqt),gamma),p_mul(common,Wq)),
             p_scale(p_mul(C2,Wqr),-1))
    cross=[]
    for shifted in (Bplus,Bminus):
        derivative=p_add(p_mul(Bt,C),p_scale(p_mul(shifted,Ct),-1))
        value=p_add(p_add(p_scale(derivative,gamma),
                         p_scale(p_add(C2,p_mul(shifted,shifted)),-beta)),p_scale(C2,-kappa))
        cross.append(value)
    all_num=[];num_groups=[];degree=2*bc.degree+weights.degree
    for head,crossrow,other in ((hp,cross[0],Wq),(hq,cross[1],Wp)):
        term=p_mul(crossrow,other)
        for sign in (1,-1):
            polys=numerator_polynomials(p_add(head,p_scale(term,sign)),bc,degree)
            num_groups.append((len(all_num),len(all_num)+len(polys)));all_num.extend(polys)
    nvalues=angular_coefficients(all_num,angles)
    numerators=[p_eval(nvalues[a:b],Box(-1.,1.)) for a,b in num_groups]
    f=finite_fields(bc,bcoef,half,angles);w=finite_fields(weights,wcoef,half,angles)
    b,c,bt,ct=f[(0,0)],f[(1,0)],f[(0,1)],f[(1,1)]
    wp,wq,wpt,wqt=w[(0,0)],w[(1,0)],w[(0,1)],w[(1,1)]
    if not np.all(c.hi<0):raise ValueError('finite BC denominator chart unresolved')
    if not np.all(wp.lo>0) or not np.all(wq.lo>0):raise ValueError('complete closed-box weight positivity unresolved')
    c2=square_box(c);ka=arb_box(full['k']);ga=arb_box(full['gamma'])
    ba=arb_box(full['beta']);kap=arb_box(full['kappa'])
    P,Q=(b+ka)/c,(b-ka)/c
    Pt,Qt=bt/c-(b+ka)*ct/c2,bt/c-(b-ka)*ct/c2
    P0,Q0=(b+k)/c,(b-k)/c
    dk,dg,db,dc=[arb_box(differences[name]) for name in ('k','gamma','beta','kappa')]
    deltaK=arb_box(full['K']+arb(constants['k'])**2)
    PQ=(square_box(b)+arb_box(full['K']))/c2
    diagonal_error=-2*db*PQ-2*beta*deltaK/c2+dc
    velocity_error_p=dg*Q-gamma*dk/c
    velocity_error_q=dg*P+gamma*dk/c
    cross_error_p=(dg*Pt-gamma*dk*ct/c2-db*(1+square_box(P))
                   -beta*(dk/c)*(2*P0+dk/c)-dc)
    cross_error_q=(dg*Qt+gamma*dk*ct/c2-db*(1+square_box(Q))
                   +beta*(dk/c)*(2*Q0-dk/c)-dc)
    absbox=lambda value:Box(value.abs_upper())
    ep=absbox(velocity_error_p)*absbox(wpt)+absbox(diagonal_error)*wp+absbox(cross_error_p)*wq
    eq=absbox(velocity_error_q)*absbox(wqt)+absbox(diagonal_error)*wq+absbox(cross_error_q)*wp
    l0p=[v/(c2*wp)+ep/wp for v in numerators[:2]]
    l0q=[v/(c2*wq)+eq/wq for v in numerators[2:]]
    l1p=absbox(ga*wpt-2*ba*P*wp)/wp+absbox(ba)*absbox(Q)
    l1q=absbox(ga*wqt-2*ba*Q*wq)/wq+absbox(ba)*absbox(P)
    rates={}
    for tube in tubes:
        T=arb_box(exact_arb(tube));quadratic=absbox(ba)*T*T
        candidates=[v+T*l1p+quadratic for v in l0p]+[v+T*l1q+quadratic for v in l0q]
        value=arb(float(max(float(np.max(v.hi)) for v in candidates))).upper()
        rates[str(tube)]=record(max(arb(0),value).upper())
    lower=arb(float(min(float(np.min(wp.lo)),float(np.min(wq.lo))))).lower()
    upper=arb(float(max(float(np.max(wp.hi)),float(np.max(wq.hi))))).upper()
    return dict(weight_lower=record(lower),weight_upper=record(upper),rates=rates,
        exact_dyadic_scalar_models=constants,
        full_scalar_model_differences={k:record(v) for k,v in differences.items()},
        original_rho0=item['bounds']['rho0'],original_Mhat=item['bounds']['Mhat'],
        original_candidate_gap=item['bounds']['candidate_gap'],original_k_lower=item['bounds']['k_lower'],
        original_beta=item['bounds']['beta'],original_kappa=item['bounds']['kappa'],
        nominal_rate_upper=record(arb(float(max(float(np.max(v.hi)) for v in l0p+l0q))).upper()),
        error_tube_linear_rate_upper=record(maxabs(l1p,l1q)),
        finite_numerator_degree=degree,maximum_radial_numerator_degree=max(b-a-1 for a,b in num_groups))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-Codazzi-cubic-cleared-r02-n1024-v1-native.json.gz'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-codazzi-dense-r02-n1024-candidate-shards.json'))
    ap.add_argument('--weights',type=Path,required=True)
    ap.add_argument('--grid',type=int,default=4096);ap.add_argument('--angles',type=int,default=4096)
    ap.add_argument('--bits',type=int,default=192);ap.add_argument('--subdivide',type=int,default=1)
    ap.add_argument('--first',type=int,default=0);ap.add_argument('--rows',type=int)
    ap.add_argument('--tubes',type=Fraction,nargs='+',default=[Fraction(1,500),Fraction(1,200),Fraction(1,100),Fraction(1,50),Fraction(1,16)])
    ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();ctx.prec=a.bits;ctx.cap=4
    if a.out.exists():raise FileExistsError('new complete comparison report required')
    if a.grid&(a.grid-1) or a.angles<a.grid or a.angles&(a.angles-1) or a.subdivide<1 or a.first<0:
        raise ValueError('complete angular and radial partitions required')
    if not a.tubes or min(a.tubes)<=0:raise ValueError('positive exact bootstrap tubes required')
    d=read_json(a.native)
    if (d.get('kind')!='actual_complete_Codazzi_cubic_target_cleared_polynomial_residual'
        or not d.get('complete') or d.get('failure') is not None
        or d['covered_interval']!=d['exact_requested_interval']
        or not d.get('whole_affine_parameter_interval') or not d.get('whole_real_angular_circle')):
        raise ValueError('complete actual cubic residual input required')
    if d['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cubic_cleared_residual.py')):
        raise ValueError('actual cubic producer changed')
    for p,h in d['inputs'].items():
        if sha(p)!=h:raise ValueError('complete actual residual input changed: '+p)
    for p,h in d['dependencies'].items():
        if sha(Path(__file__).with_name(p))!=h:raise ValueError('actual residual dependency changed: '+p)
    target=SimpleNamespace(product_grid=a.grid,polynomial_fft=DirectedFFT())
    bc=ShardedExactCandidate(a.candidate,target);weights=ExactWeightCandidate(a.weights,target)
    if bc.original_payload_sha256!=d['candidate_sha256'] or sha(a.candidate)!=d['candidate_manifest_sha256']:
        raise ValueError('the same complete finite BC object is required')
    wm=weights.metadata
    if (wm['candidate_original_sha256']!=bc.original_payload_sha256
        or wm['candidate_manifest_sha256']!=sha(a.candidate) or wm['object_sha256']!=d['object_sha256']
        or wm['exact_center_parameter']!=d['exact_center_parameter']):
        raise ValueError('weight and actual target/candidate identities differ')
    if a.grid<=2*(2*bc.degree+weights.degree):raise ValueError('complete finite numerator would alias')
    storage=read_json(a.weights)
    if storage['kind']!=STORAGE or storage['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_positive_weight_candidate.py')):
        raise ValueError('complete weight storage source differs')
    inputs={str(p):sha(p) for p in (a.native,a.candidate,a.weights)}
    for row in storage['shards']:
        p=a.weights.parent/row['file'];inputs[str(p)]=sha(p)
    right=Fraction(d['covered_interval'][1]);partition=[]
    if weights.times[-1]<right:raise ValueError('complete weights do not cover the actual native interval')
    for index,item in enumerate(d['rows']):
        lo,hi=map(Fraction,item['interval']);cuts=[lo]+[v for v in weights.times if lo<v<hi]+[hi]
        for left,end in zip(cuts,cuts[1:]):
            wpiece=min(weights.pieces-1,bisect_right(weights.times,left)-1)
            for n in range(a.subdivide):
                l=left+(end-left)*n/a.subdivide;r=left+(end-left)*(n+1)/a.subdivide
                partition.append((index,wpiece,l,r))
    selected=partition[a.first:None if a.rows is None else a.first+a.rows]
    if not selected:raise ValueError('empty complete comparison partition')
    requested=list(map(str,(selected[0][2],selected[-1][3])))
    dependencies=('fourfold_codazzi_cubic_cleared_residual.py','fourfold_codazzi_positive_weight_candidate.py',
        'fourfold_codazzi_sharded_candidate.py','fourfold_phase_codazzi_continuation_validate.py',
        'fourfold_phase_newton_source_centered.py','fourfold_phase_beta_bulk_box.py',
        'fourfold_phase_two_jet_newton_source.py','fourfold_phase_beta_bulk_interval.py',
        'fourfold_codazzi_piecewise_barrier.py')
    out=dict(kind='actual_complete_Codazzi_positive_weight_comparison_coefficients',
        complete=False,failure=None,continuation_certified=False,closed_surface_complete=False,
        source_sha256=sha(__file__),inputs=inputs,dependencies={p:sha(Path(__file__).with_name(p)) for p in dependencies},
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,
        object_sha256=d['object_sha256'],exact_center_parameter=d['exact_center_parameter'],parameter_half_width=d['parameter_half_width'],
        full_BC_candidate_sha256=bc.original_payload_sha256,full_weight_candidate_sha256=weights.original_payload_sha256,
        actual_initial_error=d['actual_initial_error'],initial_weights_exactly_one=True,
        original_full_native_interval=d['covered_interval'],exact_requested_interval=requested,
        all_original_radial_weight_and_actual_germ_joins_retained=True,full_mean_retained=True,
        exact_denominator_clearing=True,complete_actual_scalar_model_fees=True,
        full_nonlinear_error_tube_terms_retained=True,tubes=list(map(str,a.tubes)),
        bits=a.bits,angular_grid=a.angles,product_grid=a.grid,subdivide=a.subdivide,
        planned_boxes=len(selected),original_partition_first=a.first,rows=[])
    cursor=Fraction(requested[0]);tick=time.monotonic()
    try:
        for number,(index,wpiece,left,end) in enumerate(selected):
            item=d['rows'][index];gl,gr=map(Fraction,item['actual_scalar_germ'])
            if left!=cursor or not gl<=left<end<=gr:raise ValueError('actual contiguous germ cover lost')
            budget=row_budget(bc,weights,item,left,end,wpiece,a.angles,a.tubes)
            out['rows'].append(dict(partition_row=a.first+number,native_row=index,weight_piece=wpiece,
                interval=list(map(str,(left,end))),actual_scalar_germ=item['actual_scalar_germ'],**budget))
            cursor=end;out['covered_interval']=[requested[0],str(cursor)]
            out['wall_seconds']=time.monotonic()-tick;save(a.out,out)
            print(dict(row=number,partition_row=a.first+number,r=str(end),
                Wmin=budget['weight_lower']['mid_float'],Wmax=budget['weight_upper']['mid_float'],
                rates={k:v['mid_float'] for k,v in budget['rates'].items()},seconds=out['wall_seconds']),flush=True)
        if str(cursor)!=requested[1]:raise ValueError('complete requested endpoint missing')
        out['complete']=True
    except Exception as exc:out['failure']=repr(exc)
    out['wall_seconds']=time.monotonic()-tick;save(a.out,out)
    print(dict(complete=out['complete'],failure=out['failure'],rows=len(out['rows']),seconds=out['wall_seconds']),flush=True)


if __name__=='__main__':main()
