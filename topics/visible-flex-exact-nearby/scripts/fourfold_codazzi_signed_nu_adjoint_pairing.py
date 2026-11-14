#!/usr/bin/env python3
"""Signed actual nu/adjoint pairing, with exact full mean and all joins.

Prepared during the runtime outage. This source has not been executed.
It requires the complete actual ac1 candidate, a real physical nonmean
adjoint trial, and the completed scalar-mean/body certificate. It produces
two full-circle, whole-radial enclosures of the same integral. It does not
assert a nonzero true Schur denominator or a complete BVP inverse.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right, bisect_left
from fractions import Fraction
from pathlib import Path
import time

from flint import arb, ctx
from fourfold_codazzi_final_nu_return_derivative import (
    prepare as prepare_return, extended_target, Finite,
    exact_w_integral, exact_w_value, CONTROL_LEFT, CONTROL_RIGHT,
    EXPECTED_CANDIDATE, maximum, interval_bounds)
from fourfold_codazzi_nu_full_adjoint_kernel import (
    lift as lift_background, nu_polynomials, adjoint_action,
    operator_action, exact_delta_state, add, scale, theta)
from fourfold_codazzi_mean_completed_head_body_residual import (
    read_trial, lift as lift_trial, circle_pair, constant_pair,
    zero_mean_by_identity, MEAN_KIND, MEAN_SOURCE, RIGHT)
from fourfold_codazzi_curvature_angle_energy_prefix import (
    read, polynomial_ranges, actual_jump)
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

KIND='actual_final_complete_signed_nu_adjoint_double_integral'
BODY_KIND='actual_final_exact_mean_completed_response_adjoint_body_residual'
BODY_SOURCE='190291987e288beaa9647afd90b54f16df2c6610d706fee01cac4623e1a4b62f'
REQUIRED_SOURCES={
 'fourfold_codazzi_final_nu_return_derivative.py':
 '33ae536750241497e7ad73b72aedb2be8d7185542b5f71a88f081af005c7ebbe',
 'fourfold_codazzi_nu_full_adjoint_kernel.py':
 '09807e405455b58c043a5ff26b7ff5e4e1569a96c81ecd860125552bfba95a3b',
 'fourfold_codazzi_mean_completed_head_body_residual.py':BODY_SOURCE}
MID=(CONTROL_LEFT+CONTROL_RIGHT)/2


def intersect(x,y,label):
    try:
        return x.intersection(y)
    except ValueError as exc:
        raise ValueError('two complete enclosures disagree: '+label) from exc


def piece_at(nodes,r,side='right'):
    j=(bisect_left(nodes,r)-1 if side=='left' else bisect_right(nodes,r)-1)
    j=max(0,min(j,len(nodes)-2))
    if not nodes[j]<=r<=nodes[j+1]:
        raise ValueError('the requested true one-sided piece does not contain the point')
    return j


def prepare(args):
    for name,expected in REQUIRED_SOURCES.items():
        if sha(Path(__file__).with_name(name))!=expected:
            raise ValueError('a published full operator/source dependency changed: '+name)
    # Rebuild the base true common partition first; refine only after adding
    # every actual adjoint and mean-flow interface.
    base=argparse.Namespace(**vars(args));base.radial_subdivisions=1
    c,base_doc=prepare_return(base)
    if c['modes']!=32:
        raise ValueError('the complete actual final centre has 32 modes')
    body=read(args.body);mean=read(args.mean)
    if (body.get('kind')!=BODY_KIND or body.get('source_sha256')!=BODY_SOURCE
        or not body.get('complete') or body.get('failure') is not None
        or body.get('stage')!='complete_body_only'
        or body.get('candidate_sha256')!=EXPECTED_CANDIDATE
        or body.get('candidate_metadata')!=c['meta']
        or not body.get('whole_original_eta')
        or not body.get('exact_mean_ODEs_and_continuous_mean_interfaces_preserved')):
        raise ValueError('the complete same-centre exact-mean body certificate is required')
    for path in (args.candidate,args.adjoint,args.mean):
        if sha(path) not in body['inputs'].values():
            raise ValueError('body and signed-pairing input bytes differ: '+str(path))
    if (mean.get('kind')!=MEAN_KIND or mean.get('source_sha256')!=MEAN_SOURCE
        or not mean.get('complete') or mean.get('failure') is not None
        or mean.get('candidate_sha256')!=EXPECTED_CANDIDATE
        or mean.get('candidate_metadata')!=c['meta']
        or mean.get('exact_interval')!=['0','25/8']
        or not mean.get('whole_original_affine_parameter_interval')
        or mean.get('original_parameter_half_width')!='1/1000000000'
        or not mean.get('complete_original_primitive_tail_reused')
        or sha(args.target) not in mean['inputs'].values()):
        raise ValueError('body and source must use the same full original target/eta data')
    adjoint=read_trial(args.adjoint,'adjoint_nonmean',c['meta'])
    if body['adjoint_metadata']!=adjoint['meta']:
        raise ValueError('the true full nonmean adjoint trial identity changed')
    nr=body['total_common_cells'];bn=[];endpoint=Fraction(0)
    for name in ('coefficient_rows','adjoint_flow','residual_rows'):
        if len(body[name])!=nr:
            raise ValueError('the completed body certificate lost full rows: '+name)
    for i,co in enumerate(body['coefficient_rows']):
        l,r=map(Fraction,co['interval'])
        if co['common_row']!=i or l!=endpoint or not l<r:
            raise ValueError('the complete mean-flow partition is not a closed cover')
        for name in ('adjoint_flow','residual_rows'):
            x=body[name][i]
            if x['common_row']!=i or x['interval']!=co['interval']:
                raise ValueError('scalar flow and residual interfaces differ')
        gl,gr=map(Fraction,co['actual_scalar_germ'])
        if not gl<=l<r<=gr:
            raise ValueError('an actual scalar germ was crossed')
        # Check both valid descriptions of a continuous ordinary mu trace.
        if i:
            intersect(box_from_record(body['adjoint_flow'][i-1]['right']),
                      box_from_record(body['adjoint_flow'][i]['left']),
                      'continuous adjoint mean at body join')
        bn.append(l);endpoint=r
    if endpoint!=RIGHT:
        raise ValueError('the mean-filled adjoint must be defined on the complete body')
    bn.append(RIGHT)
    original=sorted(set(c['cuts'])|{MID}
        |{r for r in bn+adjoint['nodes'] if CONTROL_LEFT<r<CONTROL_RIGHT})
    if args.radial_subdivisions<1:
        raise ValueError('positive explicit radial refinement is required')
    cuts=[]
    for l,r in zip(original,original[1:]):
        cuts.extend(l+(r-l)*j/args.radial_subdivisions
                    for j in range(args.radial_subdivisions))
    cuts.append(CONTROL_RIGHT)
    grid=1;support=max(5*c['modes'],adjoint['m']+2*c['modes'])
    while grid<=2*support:grid*=2
    if args.angles<grid or args.angles&(args.angles-1):
        raise ValueError('the complete directed grid must contain every finite output mode')
    c.update(body=body,mean=mean,bn=bn,adjoint=adjoint,cuts=cuts,grid=grid)
    # Only these real joins contribute distributional point sources.
    joins=sorted({r for r in c['nodes']+adjoint['nodes']
                  if CONTROL_LEFT<r<CONTROL_RIGHT})
    c['joins']=joins
    deps=dict(base_doc['dependencies'])
    for name in REQUIRED_SOURCES:deps[name]=sha(Path(__file__).with_name(name))
    deps['fourfold_codazzi_mean_completed_head_body_residual.py']=BODY_SOURCE
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None,
        stage='signed_closed_cells',
        inputs={str(p):sha(p) for p in
                (args.candidate,args.adjoint,args.body,args.mean,args.target,args.type_cover)},
        dependencies=deps,candidate_sha256=EXPECTED_CANDIDATE,
        candidate_metadata=c['meta'],adjoint_metadata=adjoint['meta'],
        exact_amp_multiplier=body['exact_amp_multiplier'],
        exact_parameter=base_doc['exact_parameter'],
        exact_amplitude=base_doc['exact_amplitude'],
        exact_interval=[str(CONTROL_LEFT),str(CONTROL_RIGHT)],
        original_object_sha256=base_doc['original_object_sha256'],
        original_affine_parameter_half_width=base_doc['original_affine_parameter_half_width'],
        original_exact_center_parameter=base_doc['original_exact_center_parameter'],
        whole_original_eta=True,full_original_primitive_tail=True,
        physical_unnormalized_nu_source=True,
        exact_continuous_adjoint_mean=True,
        source_maximum_support=3*c['modes'],
        integrated_kernel_maximum_support=5*c['modes'],
        complete_adjoint_residual_support=adjoint['m']+2*c['modes'],
        finite_product_grid=grid,closed_angular_cells=args.angles,
        radial_subdivisions=args.radial_subdivisions,
        total_radial_cells=len(cuts)-1,total_actual_product_jumps=len(joins),
        exact_all_jump_radii=list(map(str,joins)),
        rows=[],jumps=[],resume_history=[],
        complete_actual_source_pairing_proved=False,
        actual_nu_scalar_nonzero_proved=False,
        actual_body_BVP_inverse_proved=False)
    return c,doc


def identity(c,i):
    l,r=c['cuts'][i:i+2]
    bg=piece_at(c['nodes'],l)
    ad=piece_at(c['adjoint']['nodes'],l)
    k=bisect_right(c['tn'],l)-1;raw=c['rows'][k]
    b=bisect_right(c['bn'],l)-1
    tl,tr=map(Fraction,raw['interval'])
    if (not c['nodes'][bg]<=l<r<=c['nodes'][bg+1]
        or not c['adjoint']['nodes'][ad]<=l<r<=c['adjoint']['nodes'][ad+1]
        or not tl<=l<r<=tr or not c['bn'][b]<=l<r<=c['bn'][b+1]
        or (l<MID<r)):
        raise ValueError('a closed candidate/adjoint/target/mean or monotonicity interface was crossed')
    return l,r,bg,ad,k,b,raw


def fields(c,i):
    l,r,bg,ad,k,b,raw=identity(c,i)
    a=extended_target(raw,l,r,c['nu'])
    y,yr=polynomial_ranges(c['saved'],c['nodes'],bg,l,r)
    Q,Qr=lift_background(c,a,y,yr)
    z,zr=polynomial_ranges(c['adjoint']['saved'],c['adjoint']['nodes'],ad,l,r)
    lam=lift_trial(z,c['adjoint']['m'],c['grid'],c['fft'])
    lamr=lift_trial(zr,c['adjoint']['m'],c['grid'],c['fft'])
    mu=box_from_record(c['body']['adjoint_flow'][b]['entire'])
    co=c['body']['coefficient_rows'][b]['coefficients']
    beta,K=a['beta'],a['K'];m=Q[1].mean();M=c['modes']
    U2=c['alpha']**2*sum((x*x for x in y[:M]),arb(0))/2
    V2=c['alpha']**2*sum((x*x for x in y[M+1:]),arb(0))/2
    cm=beta*(1-U2-K*V2-3*K*m*m)
    zero=constant_pair(c['grid'],c['fft'])
    e2=constant_pair(c['grid'],c['fft'],y=arb(1))
    ae2=tuple(-z for z in operator_action(Q,e2,zero,a))
    g=circle_pair(ae2,lam)
    cm=intersect(cm,box_from_record(co['cm']),'same actual mean diagonal')
    g=intersect(g,box_from_record(co['adjoint_forcing']),'same actual adjoint forcing')
    mur=-cm*mu-g
    psi=(lam[0],lam[1]+mu)
    psir=(lamr[0],lamr[1]+mur)
    R=adjoint_action(Q,psi,psir,a)
    # This coefficient vanishes by the exact mu equation, including g.
    R=(R[0],zero_mean_by_identity(R[1]))
    v=Q[1].closed_cells(c['angles'])
    if not m<0 or not maximum(v)<0:
        raise ValueError('the complete actual moving chart lost its strictly negative v/mean')
    pol=nu_polynomials(Q,Qr,a)
    return l,r,bg,ad,k,b,raw,a,Q,psi,R,pol,v,mu


def row_budget(c,i):
    l,r,bg,ad,k,b,raw,a,Q,psi,R,pol,v,mu=fields(c,i)
    iw=exact_w_integral(l,r)
    dw=exact_w_value(r)-exact_w_value(l)
    if iw<0 or (r<=MID and dw<0) or (l>=MID and dw>0):
        raise ValueError('the exact nonnegative bump or monotone derivative changed sign')
    pg=circle_pair(psi,pol['G'])
    pa=circle_pair(psi,pol['A'])
    pb=circle_pair(psi,pol['B'])
    ra=circle_pair(R,pol['A'])
    main=exact_arb(iw)*pg;residual=exact_arb(iw)*ra
    direct=exact_arb(dw)*pa+exact_arb(iw)*pb
    return dict(common_row=i,interval=list(map(str,(l,r))),
        candidate_piece=bg,adjoint_piece=ad,original_target_row=k,body_mean_row=b,
        actual_scalar_germ=raw['actual_scalar_germ'],
        exact_bump_integral=str(iw),exact_signed_bump_change=str(dw),
        actual_adjoint_mean=record(mu),actual_moving_mean=record(Q[1].mean()),
        actual_v=record(interval_bounds(v)),
        actual_target={name:record(a[name]) for name in
            ('beta','beta1','gamma','gamma1','K','K1','T','T1','s','s1')},
        full_pairing={name:record(z) for name,z in
            dict(psi_G=pg,psi_A=pa,psi_B=pb,adjoint_residual_A=ra).items()},
        complete_kernel_support={name:[f.degree for f in val] for name,val in pol.items()},
        exact_adjoint_body_mean_residual=0,
        weighted_G_integral=record(main),
        weighted_adjoint_residual_integral=record(residual),
        integrated_by_parts_cell=record(main+residual),
        direct_original_source_cell=record(direct))


def mean_at(c,r):
    j=bisect_left(c['bn'],r)
    if j>=len(c['bn']) or c['bn'][j]!=r:
        raise ValueError('every actual product jump must occur at a complete mean-flow interface')
    if j==0:return box_from_record(c['body']['adjoint_flow'][0]['left'])
    if j==len(c['bn'])-1:return box_from_record(c['body']['adjoint_flow'][-1]['right'])
    return intersect(box_from_record(c['body']['adjoint_flow'][j-1]['right']),
                     box_from_record(c['body']['adjoint_flow'][j]['left']),
                     'the unique continuous actual mu trace')


def endpoint_background(c,a,r,side):
    j=piece_at(c['nodes'],r,side)
    y,yr=polynomial_ranges(c['saved'],c['nodes'],j,r,r)
    Q,Qr=lift_background(c,a,y,yr)
    return j,Q,Qr


def endpoint_adjoint(c,r,side):
    t=c['adjoint'];j=piece_at(t['nodes'],r,side)
    y,_=polynomial_ranges(t['saved'],t['nodes'],j,r,r)
    return j,lift_trial(y,t['m'],c['grid'],c['fft'])


def A_only(Q,a):
    u,v=Q;qp=theta(Q);v2=v*v
    W=add(scale(qp,v2.primitive()),scale(Q,v2))
    return add(scale(W,-a['beta']*a['T']),
               (a['gamma']*v.mean()*a['T']*qp[1],0*qp[1]))


def jump_budget(c,i):
    r=c['joins'][i];k=min(bisect_right(c['tn'],r)-1,len(c['rows'])-1)
    raw=c['rows'][k]
    tl,tr=map(Fraction,raw['interval'])
    if not tl<=r<=tr:raise ValueError('a product jump has no true closed target germ')
    a=extended_target(raw,r,r,c['nu'])
    jl,Ql,_=endpoint_background(c,a,r,'left')
    jr,Qr,_=endpoint_background(c,a,r,'right')
    al,laml=endpoint_adjoint(c,r,'left')
    ar,lamr=endpoint_adjoint(c,r,'right')
    M=c['modes'];N=c['grid'];fft=c['fft']
    if jl!=jr:
        if jr!=jl+1 or c['nodes'][jr]!=r:
            raise ValueError('the true candidate join lost its two adjacent traces')
        delta=actual_jump(c['saved'],c['nodes'],jr)
        dQ=exact_delta_state(delta,c['alpha'],M,N,fft)
    else:
        dQ=constant_pair(N,fft)
    if al!=ar:
        if ar!=al+1 or c['adjoint']['nodes'][ar]!=r:
            raise ValueError('the true adjoint join lost its two adjacent traces')
        delta_lam=actual_jump(c['adjoint']['saved'],c['adjoint']['nodes'],ar)
        if delta_lam[c['adjoint']['m']]!=0:
            raise ValueError('the supplied explicitly nonmean adjoint has a mean jump')
        dlam=lift_trial(list(map(exact_arb,delta_lam)),c['adjoint']['m'],N,fft)
    else:
        dlam=constant_pair(N,fft)
    vl,vr,dv=Ql[1],Qr[1],dQ[1];vl2=vl*vl
    dv2=(vr+vl)*dv
    dW=add(add(scale(theta(Qr),dv2.primitive()),
              scale(theta(dQ),vl2.primitive())),
           add(scale(Qr,dv2),scale(dQ,vl2)))
    dA=add(scale(dW,-a['beta']*a['T']),
        (a['gamma']*a['T']*(dv.mean()*vr.derivative()+vl.mean()*dv.derivative()),0*dv))
    mu=mean_at(c,r);psir=(lamr[0],lamr[1]+mu)
    # [<psi,A>] = <[lambda],A-> + <psi+,[A]>.
    # The ordinary scalar mu has no jump. Its value in psi+ is retained.
    mean_continuous_part=circle_pair(dlam,A_only(Ql,a))
    centre_jump_part=circle_pair(psir,dA)
    product_jump=mean_continuous_part+centre_jump_part
    weight=exact_w_value(r)
    return dict(product_join=i,radius=str(r),candidate_pieces=[jl,jr],
        adjoint_pieces=[al,ar],original_target_row=k,
        actual_scalar_germ=raw['actual_scalar_germ'],
        exact_bump=str(weight),continuous_adjoint_mean=record(mu),
        exact_completed_adjoint_mean_jump=0,
        exact_candidate_mean_jump=record(dv.mean()),
        adjoint_jump_times_left_A=record(mean_continuous_part),
        right_complete_adjoint_times_A_jump=record(centre_jump_part),
        complete_signed_product_jump=record(product_jump),
        weighted_signed_product_jump=record(exact_arb(weight)*product_jump),
        convention='right minus left; subtract this weighted scalar in the complete identity')


def finish(c,doc):
    if len(doc['rows'])!=len(c['cuts'])-1 or len(doc['jumps'])!=len(c['joins']):
        raise ValueError('both signed integrals require every closed cell and every true product join')
    main=arb(0);res=arb(0);direct=arb(0);jump=arb(0)
    for row in doc['rows']:
        main+=box_from_record(row['weighted_G_integral'])
        res+=box_from_record(row['weighted_adjoint_residual_integral'])
        direct+=box_from_record(row['direct_original_source_cell'])
    for row in doc['jumps']:
        jump+=box_from_record(row['weighted_signed_product_jump'])
    ibp=main+res-jump
    body=box_from_record(c['body']['summary']['signed_full_adjoint_parameter_integral'])
    double=intersect(direct,ibp,'original source versus complete integration by parts')
    triple=intersect(double,body,'same full body/mean source pairing')
    doc.update(complete=True,stage='complete_signed_source_pairing',
        complete_actual_source_pairing_proved=True,
        summary=dict(
            signed_weighted_G_integral=record(main),
            signed_weighted_adjoint_residual_integral=record(res),
            signed_all_product_jumps=record(jump),
            signed_original_source_integral=record(direct),
            signed_complete_integration_by_parts=record(ibp),
            same_body_source_integral=record(body),
            common_signed_actual_nu_pairing=record(triple),
            enclosure_excludes_zero=bool(not triple.contains(0)),
            exact_control_endpoint_terms=0),
        actual_nu_scalar_nonzero_proved=False,actual_body_BVP_inverse_proved=False,
        scope='actual source paired with the supplied mean-completed adjoint only; all actual finite modes, whole eta, primitive tails, and all jumps retained')


def validate_resume(c,doc,old):
    keys=('kind','source_sha256','inputs','dependencies','candidate_sha256',
        'candidate_metadata','adjoint_metadata','exact_amp_multiplier','exact_parameter',
        'exact_amplitude','exact_interval','original_object_sha256',
        'original_affine_parameter_half_width','original_exact_center_parameter',
        'finite_product_grid','closed_angular_cells','radial_subdivisions',
        'total_radial_cells','total_actual_product_jumps','exact_all_jump_radii')
    for key in keys:
        if old[key]!=doc[key]:raise ValueError('signed-pairing checkpoint identity changed: '+key)
    if old.get('complete') or old.get('failure') is not None:
        raise ValueError('only a successful explicit saved prefix may be resumed')
    if len(old['rows'])>doc['total_radial_cells'] or len(old['jumps'])>doc['total_actual_product_jumps']:
        raise ValueError('saved prefix is longer than its actual exact partition')
    for i,row in enumerate(old['rows']):
        l,r,bg,ad,k,b,raw=identity(c,i)
        if (row['common_row']!=i or row['interval']!=list(map(str,(l,r)))
            or row['candidate_piece']!=bg or row['adjoint_piece']!=ad
            or row['original_target_row']!=k or row['body_mean_row']!=b
            or row['actual_scalar_germ']!=raw['actual_scalar_germ']):
            raise ValueError('a saved signed cell changed its full exact identity')
    for i,row in enumerate(old['jumps']):
        if row['product_join']!=i or row['radius']!=str(c['joins'][i]):
            raise ValueError('a saved actual product jump changed identity')
    if old['jumps'] and len(old['rows'])!=doc['total_radial_cells']:
        raise ValueError('saved jump stage precedes completion of all signed cells')
    doc['rows']=old['rows'];doc['jumps']=old['jumps']
    doc['resume_history']=old.get('resume_history',[])+[
        dict(path=str(c['resume']),sha256=sha(c['resume']),
             signed_cells=len(old['rows']),product_jumps=len(old['jumps']))]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','adjoint','body','mean'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--target',type=Path,default=Path(
        'notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    ap.add_argument('--type-cover',type=Path,default=Path(
        'notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    ap.add_argument('--angles',type=int,default=1024)
    ap.add_argument('--radial-subdivisions',type=int,default=1)
    ap.add_argument('--max-new-rows',type=int,default=64)
    ap.add_argument('--resume',type=Path)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if args.max_new_rows<1:raise ValueError('a positive explicit checkpoint work limit is required')
    if args.out.exists():raise FileExistsError('preserve every actual prior signed outcome')
    c,doc=prepare(args);c['angles']=args.angles;c['resume']=args.resume
    if args.resume:validate_resume(c,doc,read(args.resume))
    done=0
    try:
        while done<args.max_new_rows:
            if len(doc['rows'])<doc['total_radial_cells']:
                doc['stage']='signed_closed_cells'
                doc['rows'].append(row_budget(c,len(doc['rows'])))
            elif len(doc['jumps'])<doc['total_actual_product_jumps']:
                doc['stage']='exact_signed_product_jumps'
                doc['jumps'].append(jump_budget(c,len(doc['jumps'])))
            else:
                finish(c,doc);break
            done+=1;doc['wall_seconds']=time.monotonic()-started
            save(args.out,doc)
            print(dict(stage=doc['stage'],rows=len(doc['rows']),
                       jumps=len(doc['jumps']),complete=False),flush=True)
        if (not doc['complete'] and len(doc['rows'])==doc['total_radial_cells']
            and len(doc['jumps'])==doc['total_actual_product_jumps']):
            finish(c,doc)
        doc['wall_seconds']=time.monotonic()-started
        save(args.out,doc)
    except Exception as exc:
        doc['failure']=dict(type=type(exc).__name__,message=str(exc),
            completed_signed_cells=len(doc['rows']),completed_product_jumps=len(doc['jumps']))
        doc['wall_seconds']=time.monotonic()-started
        save(args.out,doc)
        raise
    print(dict(complete=doc['complete'],stage=doc['stage'],
               signed_cells=len(doc['rows']),product_jumps=len(doc['jumps'])),flush=True)


if __name__=='__main__':main()
