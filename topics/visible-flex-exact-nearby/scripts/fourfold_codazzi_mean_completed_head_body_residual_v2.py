#!/usr/bin/env python3
"""Exact mean completion of finite full-body response/adjoint trials.

Explicit v2 fixes the original input parser: the real waist certificate is
plain JSON, whereas the full mean and long native reports use gzip. The
original source and its actual BadGzipFile process record are preserved.
No mathematical row, flow, full Fourier product or error bound is changed. It consumes an actual complete ac1 mean/target certificate and two
explicit physical nonmean PPoly trials. The response mean is the exact
backward scalar solution with the true regular mean row, enclosed using its
published complete operator bound. The adjoint mean is the exact forward
scalar solution with the actual physical waist-amplitude mean column.

Whole finite body residuals, including every output mode through N+2M, and
all true nonmean PPoly jumps are bounded. The complete true physical
boundary adjoint and b4 output are NOT replaced by a finite Fourier row;
they remain an explicit separate, unpaid output contract.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time
import numpy as np
from flint import arb,acb,ctx

from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_curvature_angle_energy_prefix import (
    dyadic,polynomial_ranges,actual_jump,bump_jets)
from fourfold_codazzi_final_nu_return_derivative import (
    Finite,EXPECTED_CANDIDATE,CONTROL_LEFT,CONTROL_RIGHT)
from fourfold_codazzi_nu_full_adjoint_kernel import operator_action,adjoint_action,parts
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import CBox,zeros,DirectedFFT
from fourfold_phase_metric_defect import record,save,sha

KIND='actual_final_exact_mean_completed_response_adjoint_body_residual_v2'
MEAN_KIND='actual_final_complete_scalar_mean_Green_cached_full_target'
MEAN_SOURCE='6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93'
WAIST_SOURCE='e1e16cfa270811353c7dccdc58cfe959561a1301a81bd6aebec18861bfaa8221'
TRIAL_KIND='actual_final_mean_eliminated_trial_v1'
COORDINATES='physical moving nonmean variation; h1 sine(4j phi), h2 cosine(4j phi); mean supplied by exact scalar Green'
RIGHT=Fraction(25,8)


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==bytes((31,139)) else raw)


def scalar_cb(z):
    return acb(arb(float(z.real.lo)).union(arb(float(z.real.hi))),
               arb(float(z.imag.lo)).union(arb(float(z.imag.hi))))


def circle_pair(x,y):
    """Complete real mean; no cyclic convolution or omitted high product."""
    total=acb(0)
    for f,g in zip(x,y):
        for j in range(-min(f.degree,g.degree),min(f.degree,g.degree)+1):
            total+=scalar_cb(f.c[j%f.grid])*scalar_cb(g.c[(-j)%g.grid])
    if not total.imag.contains(0):raise ValueError('a true real full-circle pairing lost reality')
    return total.real


def lift(values,m,grid,fft,scale=arb(1),background=arb(0)):
    cu=zeros((grid,));cv=zeros((grid,))
    cv[0]=CBox.from_acb(acb(background+scale*values[m]))
    for j in range(1,m+1):
        u=scale*values[j-1]/2;v=scale*values[m+j]/2
        cu[j]=CBox.from_acb(acb(0,-u));cu[-j]=CBox.from_acb(acb(0,u))
        cv[j]=cv[-j]=CBox.from_acb(acb(v))
    return Finite(cu,m,fft),Finite(cv,m,fft)


def exact_pair(values,m,grid,fft):
    return lift(list(map(exact_arb,values)),m,grid,fft)


def constant_pair(grid,fft,x=arb(0),y=arb(0)):
    return Finite.constant(x,grid,fft),Finite.constant(y,grid,fft)


def zero_mean_by_identity(p):
    """Only for the two separately proved exact scalar mean equations."""
    z=scalar_cb(p.c[0])
    if not z.real.contains(0) or not z.imag.contains(0):
        raise ValueError('the exact scalar mean cancellation was not enclosed')
    out=Finite(p.c,p.degree,p.fft);out.c[0]=0
    return out


def norms(pair,width):
    a0=arb(0);a_sigma=arb(0);l2=arb(0);hthird=arb(0);h1=arb(0)
    for p in pair:
        for j in range(-p.degree,p.degree+1):
            z=scalar_cb(p.c[j%p.grid])
            value=(abs(z.real).upper()**2+abs(z.imag).upper()**2).upper()
            mod=value.sqrt().upper();freq=4*abs(j)
            a0+=mod;a_sigma+=mod*(exact_arb(width*freq)).exp()
            l2+=value
            hthird+=value*(arb(1+freq*freq).log()/3).exp()
            h1+=value*(1+freq*freq)
    return dict(A0=a0.upper(),A_sigma=a_sigma.upper(),L2=l2.sqrt().upper(),
                H_one_third=hthird.sqrt().upper(),H1=h1.sqrt().upper())


def phi1(z):
    """Entire (exp(z)-1)/z, with a complete geometric Taylor remainder."""
    magnitude=abs(z).upper()
    if not magnitude<32:
        raise ValueError('scalar flow cell too wide: refine common radial cells explicitly')
    term=arb(1);answer=arb(1)
    for n in range(1,2000):
        term=term*z/(n+1);answer+=term
        first=(abs(term).upper()*magnitude/(n+2)).upper()
        ratio=(magnitude/(n+3)).upper()
        if ratio<arb(1)/2:
            fee=(first/(1-ratio)).upper()
            if fee<arb(2)**(-280):
                out=answer+(-fee).union(fee)
                low=min(arb(0),z.lower()).exp()
                high=max(arb(0),z.upper()).exp()
                return out.intersection(low.union(high))
    raise ValueError('complete scalar flow exponential remainder unresolved')


def flow(A,B,initial,length):
    """Enclose y'=A(r)y+B(r) with genuinely varying scalar coefficients."""
    t=exact_arb(length)
    end=(A*t).exp()*initial+t*phi1(A*t)*B
    all_t=arb(0).union(t)
    entire=(A*all_t).exp()*initial+all_t*phi1(A*all_t)*B
    return end,entire


def read_trial(path,role,background):
    saved=load_candidate(path);meta=json.loads(str(saved['metadata']))
    if (meta.get('kind')!=TRIAL_KIND or meta.get('role')!=role
        or meta.get('coordinates')!=COORDINATES
        or meta.get('background_candidate_sha256')!=EXPECTED_CANDIDATE
        or Fraction(meta['background_exact_alpha'])!=Fraction(background['exact_float_amplitude'])
        or Fraction(meta['background_exact_nu'])!=Fraction(background['exact_float_nu'])):
        raise ValueError('trial physical coordinates, role, or actual background changed')
    m=int(meta['modes']);nodes=list(map(dyadic,saved['radial_nodes']))
    if m<1 or saved['piece_coefficients'].shape!=(4,len(nodes)-1,2*m+1):
        raise ValueError('complete finite trial shape is invalid')
    if nodes[0]!=0 or nodes[-1]!=RIGHT or any(x>=y for x,y in zip(nodes,nodes[1:])):
        raise ValueError('every trial must cover the complete physical body')
    if np.any(saved['piece_coefficients'][:,:,m]!=0):
        raise ValueError('trial mean must be explicitly zero; the exact full mean is reconstructed')
    if (len(saved['initial_state'])!=2*m+1
        or not np.array_equal(saved['initial_state'],saved['piece_coefficients'][-1,0,:])):
        raise ValueError('trial initial state and exact first PPoly value differ')
    return dict(saved=saved,meta=meta,nodes=nodes,m=m)


def prepare(args):
    if sha(args.candidate)!=EXPECTED_CANDIDATE:raise ValueError('restore the complete exact ac1 candidate')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    mean=read(args.mean);waist=read(args.waist)
    if (mean['kind']!=MEAN_KIND or mean['source_sha256']!=MEAN_SOURCE or not mean['complete']
        or mean['candidate_sha256']!=EXPECTED_CANDIDATE or mean['candidate_metadata']!=meta
        or mean['exact_interval']!=['0','25/8']
        or not mean['whole_original_affine_parameter_interval']
        or mean['original_parameter_half_width']!='1/1000000000'):
        raise ValueError('the actual complete full-target mean certificate is required')
    if (not waist['complete'] or waist['candidate_sha256']!=EXPECTED_CANDIDATE
        or waist['producer_sha256']!=WAIST_SOURCE or not waist['whole_original_eta']
        or waist['whole_unknown_Wiener_ball']['radius']!='1/1000000'):
        raise ValueError('the actual full unknown-tail waist mean column is required')
    bm=arb(waist['derivative_interval_outward_decimal'][0]).union(
        arb(waist['derivative_interval_outward_decimal'][1]))
    if not bm<0:raise ValueError('the actual physical waist mean column lost its sign')
    response=read_trial(args.response,'response',meta)
    adjoint=read_trial(args.adjoint,'adjoint_nonmean',meta)
    nodes=list(map(dyadic,saved['radial_nodes']))
    tn=[];endpoint=Fraction(0)
    for i,row in enumerate(mean['rows']):
        left,right=map(Fraction,row['interval']);gl,gr=map(Fraction,row['actual_scalar_germ'])
        if row['common_row']!=i or left!=endpoint or not gl<=left<right<=gr:
            raise ValueError('the complete original closed scalar cover changed')
        tn.append(left);endpoint=right
    if endpoint!=RIGHT:raise ValueError('the actual mean target cover is not complete')
    tn.append(RIGHT)
    original=sorted(set(tn+nodes+response['nodes']+adjoint['nodes'])|{CONTROL_LEFT,CONTROL_RIGHT})
    if args.radial_subdivisions<1:raise ValueError('positive exact radial refinement is required')
    cuts=[]
    for l,r in zip(original,original[1:]):
        cuts.extend(l+(r-l)*j/args.radial_subdivisions for j in range(args.radial_subdivisions))
    cuts.append(RIGHT)
    m=int(meta['modes']);grid=1;maxmode=max(response['m'],adjoint['m'])
    while grid<=2*max(maxmode+2*m,3*m):grid*=2
    c=dict(saved=saved,meta=meta,nodes=nodes,mean=mean,tn=tn,cuts=cuts,m=m,
           alpha=exact_arb(Fraction(meta['exact_float_amplitude'])),
           response=response,adjoint=adjoint,grid=grid,fft=DirectedFFT(),
           amp=exact_arb(args.amp_multiplier),waist_mean_column=bm,width=args.analytic_width)
    ry,_=polynomial_ranges(response['saved'],response['nodes'],len(response['nodes'])-2,RIGHT,RIGHT)
    yp=lift(ry,response['m'],grid,c['fft'])
    y_norm=norms((yp[1],),Fraction(0))['L2']
    # This is a rigorous enclosure of the genuine homogeneous nonlinear
    # outer mean derivative. It is not a zero mean boundary condition.
    outer=(arb('0.000001084')*y_norm).upper()
    c['response_mean_R']=(-outer).union(outer)
    c['adjoint_mean_0']=c['amp']*bm
    deps=('fourfold_codazzi_candidate_shards.py','fourfold_codazzi_curvature_angle_energy_prefix.py',
          'fourfold_codazzi_final_nu_return_derivative.py','fourfold_codazzi_nu_full_adjoint_kernel.py',
          'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_beta_bulk_interval.py',
          'fourfold_phase_beta_bulk_box.py','fourfold_phase_metric_defect.py')
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None,stage='coefficients',
        inputs={str(p):sha(p) for p in (args.candidate,args.mean,args.waist,args.response,args.adjoint)},
        dependencies={name:sha(Path(__file__).with_name(name)) for name in deps},
        candidate_sha256=EXPECTED_CANDIDATE,candidate_metadata=meta,
        response_metadata=response['meta'],adjoint_metadata=adjoint['meta'],
        exact_amp_multiplier=str(args.amp_multiplier),exact_analytic_width=str(args.analytic_width),
        radial_subdivisions=args.radial_subdivisions,total_common_cells=len(cuts)-1,
        exact_interval=['0','25/8'],whole_original_eta=True,full_primitive_tail_reused=True,
        parameter_response_coordinates='physical h, complete source F_nu at fixed physical u,v; no normalized reference silently removed',
        finite_trial_means_replaced_by_exact_scalar_solutions=True,
        outer_response_mean=record(c['response_mean_R']),adjoint_initial_mean=record(c['adjoint_mean_0']),
        complete_scalar_mean_boundary_identity='z(R)=ell_R h2_perp(R), true nonlinear regular graph; ell_R not replaced by zero',
        complete_body_residual_output_support=max(maxmode+2*m,3*m),
        finite_product_grid=grid,coefficient_rows=[],adjoint_flow=[],response_flow_reverse=[],
        residual_rows=[],response_jumps=[],adjoint_jumps=[],resume_history=[],
        complete_physical_boundary_residual_paid=False,complete_physical_boundary_adjoint_paid=False,
        true_b4_Schur_evaluated=False,complete_BVP_inverse_proved=False)
    return c,doc


def identity(c,i):
    l,r=c['cuts'][i:i+2];k=bisect_right(c['tn'],l)-1
    row=c['mean']['rows'][k]
    indices={}
    for name,t in [('background',dict(nodes=c['nodes'])),('response',c['response']),('adjoint',c['adjoint'])]:
        j=min(bisect_right(t['nodes'],l)-1,len(t['nodes'])-2)
        if not t['nodes'][j]<=l<r<=t['nodes'][j+1]:raise ValueError('a true trial/background PPoly join was crossed')
        indices[name]=j
    tl,tr=map(Fraction,row['interval'])
    if not tl<=l<r<=tr:raise ValueError('an actual complete target box was crossed')
    return l,r,k,row,indices


def row_fields(c,i):
    l,r,k,row,indices=identity(c,i)
    a={name:box_from_record(row['actual_target'][name]) for name in ('a','gamma','beta','K','s')}
    y,yr=polynomial_ranges(c['saved'],c['nodes'],indices['background'],l,r)
    Q=lift(y,c['m'],c['grid'],c['fft'],c['alpha'],a['s'])
    fields={}
    for name in ('response','adjoint'):
        t=c[name];q,qp=polynomial_ranges(t['saved'],t['nodes'],indices[name],l,r)
        fields[name]=(q,qp,lift(q,t['m'],c['grid'],c['fft']),lift(qp,t['m'],c['grid'],c['fft']))
    return l,r,k,row,indices,a,y,Q,fields


def coefficient_row(c,i):
    l,r,k,row,indices,a,y,Q,fields=row_fields(c,i)
    m=a['s']+c['alpha']*y[c['m']]
    U2=c['alpha']**2*sum((x*x for x in y[:c['m']]),arb(0))/2
    V2=c['alpha']**2*sum((x*x for x in y[c['m']+1:]),arb(0))/2
    cm=a['beta']*(1-U2-a['K']*V2-3*a['K']*m*m)
    w,w1,_=bump_jets(l,r)
    Knu=-a['K']*w+a['beta']*w1/(2*a['gamma']**2*a['a']**2)
    Fm=-a['beta']*m*Knu*(m*m+V2)
    q=fields['response'][0];n=c['response']['m'];inner=arb(0)
    for j in range(1,min(c['m'],n)+1):
        inner+=c['alpha']*(y[j-1]*q[j-1]+a['K']*y[c['m']+j]*q[n+j])/2
    B=2*a['beta']*m*inner
    zero=constant_pair(c['grid'],c['fft'])
    e2=constant_pair(c['grid'],c['fft'],y=arb(1))
    neg_a=operator_action(Q,e2,zero,a)
    aa=tuple(-z for z in neg_a)
    # The supplied dual is nonmean; its product with the constant part
    # of the second column is zero, so no unproved mean is discarded.
    g=circle_pair(aa,fields['adjoint'][2])
    return dict(common_row=i,interval=list(map(str,(l,r))),source_mean_row=k,
        actual_scalar_germ=row['actual_scalar_germ'],pieces=indices,
        coefficients={name:record(value) for name,value in
          dict(cm=cm,response_forcing=Fm-B,physical_parameter_mean=Fm,
               complete_nonmean_to_mean=B,adjoint_forcing=g,actual_mean=m).items()})


def actual_parameter_source(Q,a,left,right):
    u,v=Q;beta,K,gamma=(a[k] for k in ('beta','K','gamma'))
    m=v.mean();w,w1,_=bump_jets(left,right)
    Knu=-K*w+beta*w1/(2*gamma**2*a['a']**2)
    v2=v*v;I=v2.primitive();up=u.derivative();vp=v.derivative()
    F1=-beta*Knu*(I*up+v2*u)+gamma*m*(K*w/2+Knu)*vp
    F2=-beta*Knu*(I*vp+v2*v)-gamma*m*w*up/2
    return F1,F2


def residual_row(c,doc,i):
    l,r,k,row,indices,a,y,Q,fields=row_fields(c,i)
    zc=box_from_record(doc['response_flow_reverse'][-1-i]['entire'])
    mu=box_from_record(doc['adjoint_flow'][i]['entire'])
    co={k:box_from_record(v) for k,v in doc['coefficient_rows'][i]['coefficients'].items()}
    zr=co['cm']*zc+co['response_forcing']
    mur=-co['cm']*mu-co['adjoint_forcing']
    w,wr=fields['response'][2:];lam,lamr=fields['adjoint'][2:]
    h=(w[0],w[1]+zc);hr=(wr[0],wr[1]+zr)
    psi=(lam[0],lam[1]+mu);psir=(lamr[0],lamr[1]+mur)
    D=operator_action(Q,h,hr,a);F=actual_parameter_source(Q,a,l,r)
    response=(D[0]-F[0],zero_mean_by_identity(D[1]-F[1]))
    A=adjoint_action(Q,psi,psir,a)
    dual=(A[0],zero_mean_by_identity(A[1]))
    if any(p.degree>c['response']['m']+2*c['m'] for p in D):
        raise ValueError('the full response operator angular support was lost')
    if any(p.degree>c['adjoint']['m']+2*c['m'] for p in A):
        raise ValueError('the full adjoint operator angular support was lost')
    return dict(common_row=i,interval=list(map(str,(l,r))),source_mean_row=k,
        actual_scalar_germ=row['actual_scalar_germ'],pieces=indices,
        actual_completed_response_mean=record(zc),actual_completed_adjoint_mean=record(mu),
        full_primal_residual={name:record(v) for name,v in norms(response,c['width']).items()},
        full_dual_body_residual={name:record(v) for name,v in norms(dual,c['width']).items()},
        exact_response_mean_residual=0,exact_adjoint_body_mean_residual=0,
        true_full_primal_support=[p.degree for p in response],
        true_full_dual_support=[p.degree for p in dual],
        body_dual_response_residual_pairing=record(circle_pair(lam,response)),
        body_full_adjoint_parameter_pairing=record(circle_pair(psi,F)))


def jump_row(c,name,j):
    t=c[name];delta=actual_jump(t['saved'],t['nodes'],j)
    if delta[t['m']]!=0:raise ValueError('the explicitly supplied nonmean trial acquired a mean jump')
    pair=exact_pair(delta,t['m'],c['grid'],c['fft'])
    return dict(candidate_join=j,radius=str(t['nodes'][j]),
        full_nonmean_jump={k:record(v) for k,v in norms(pair,c['width']).items()},
        exact_completed_mean_jump=0,
        original_complete_component_support=t['m'])


def summarize(c,doc):
    N=len(c['cuts'])-1
    if any(len(doc[k])!=N for k in ('coefficient_rows','adjoint_flow','response_flow_reverse','residual_rows')):
        raise ValueError('all complete closed coefficient/flow/residual rows are required')
    if len(doc['response_jumps'])!=len(c['response']['nodes'])-2 or len(doc['adjoint_jumps'])!=len(c['adjoint']['nodes'])-2:
        raise ValueError('every actual nonmean trial join must be retained')
    summary={}
    for kind in ('full_primal_residual','full_dual_body_residual'):
        sums={name:arb(0) for name in ('L2','H_one_third','H1')}
        a1=arb(0);asup=arb(0)
        for i,row in enumerate(doc['residual_rows']):
            length=exact_arb(c['cuts'][i+1]-c['cuts'][i])
            b={k:box_from_record(v).upper() for k,v in row[kind].items()}
            for name in sums:sums[name]+=length*b[name]**2
            a1+=length*b['A_sigma'];asup=max(asup,b['A_sigma']).upper()
        summary[kind]={name+'_L2_radial':record(value.sqrt().upper()) for name,value in sums.items()}
        summary[kind].update(A_sigma_L1_radial=record(a1.upper()),A_sigma_radial_sup=record(asup))
    for name in ('response','adjoint'):
        sums={k:arb(0) for k in ('A0','A_sigma','L2','H_one_third','H1')}
        for row in doc[name+'_jumps']:
            for k in sums:sums[k]+=box_from_record(row['full_nonmean_jump'][k]).upper()
        summary[name+'_all_jumps_l1']={k:record(v.upper()) for k,v in sums.items()}
    pairing=arb(0);param=arb(0)
    for i,row in enumerate(doc['residual_rows']):
        length=exact_arb(c['cuts'][i+1]-c['cuts'][i])
        pairing+=length*box_from_record(row['body_dual_response_residual_pairing'])
        param+=length*box_from_record(row['body_full_adjoint_parameter_pairing'])
    summary['signed_body_dual_response_residual_integral']=record(pairing)
    summary['signed_full_adjoint_parameter_integral']=record(param)
    doc.update(complete=True,stage='complete_body_only',summary=summary,
       endpoint_mean_traces=dict(
          response_R=doc['outer_response_mean'],
          response_0=doc['response_flow_reverse'][-1]['left'],
          adjoint_0=doc['adjoint_initial_mean'],
          adjoint_R=doc['adjoint_flow'][-1]['right']),
       exact_mean_ODEs_and_continuous_mean_interfaces_preserved=True,
       complete_physical_boundary_residual_paid=False,complete_physical_boundary_adjoint_paid=False,
       true_b4_Schur_evaluated=False,complete_BVP_inverse_proved=False)


def validate_resume(c,doc,old):
    for key in ('kind','source_sha256','inputs','dependencies','candidate_sha256','candidate_metadata',
                'response_metadata','adjoint_metadata','exact_amp_multiplier','exact_analytic_width',
                'radial_subdivisions','total_common_cells','finite_product_grid'):
        if old[key]!=doc[key]:raise ValueError('actual scalar lift resume identity changed: '+key)
    if old['complete'] or old['failure'] is not None:raise ValueError('only a successful explicit row prefix may resume')
    N=len(c['cuts'])-1
    for kind in ('coefficient_rows','adjoint_flow','residual_rows'):
        for i,row in enumerate(old[kind]):
            if i>=N or row['common_row']!=i or row['interval']!=list(map(str,c['cuts'][i:i+2])):
                raise ValueError('an actual saved radial row changed its full closed domain')
    for t,row in enumerate(old['response_flow_reverse']):
        i=N-1-t
        if i<0 or row['common_row']!=i or row['interval']!=list(map(str,c['cuts'][i:i+2])):
            raise ValueError('a saved backward mean row lost its actual direction')
    if old['adjoint_flow'] and len(old['coefficient_rows'])!=N:raise ValueError('flow cannot precede full coefficient cover')
    if old['response_flow_reverse'] and len(old['adjoint_flow'])!=N:raise ValueError('saved stage order changed')
    if old['residual_rows'] and len(old['response_flow_reverse'])!=N:raise ValueError('body residual lacks complete scalar lifts')
    for name in ('response','adjoint'):
        for i,row in enumerate(old[name+'_jumps'],1):
            if row['candidate_join']!=i or row['radius']!=str(c[name]['nodes'][i]):
                raise ValueError('a saved actual trial jump changed')
    for key in ('coefficient_rows','adjoint_flow','response_flow_reverse','residual_rows','response_jumps','adjoint_jumps','stage'):
        doc[key]=old[key]


def advance_one(c,doc):
    N=len(c['cuts'])-1
    if len(doc['coefficient_rows'])<N:
        doc['stage']='coefficients';doc['coefficient_rows'].append(coefficient_row(c,len(doc['coefficient_rows'])));return True
    if len(doc['adjoint_flow'])<N:
        i=len(doc['adjoint_flow']);l,r=c['cuts'][i:i+2]
        co={k:box_from_record(v) for k,v in doc['coefficient_rows'][i]['coefficients'].items()}
        initial=c['adjoint_mean_0'] if i==0 else box_from_record(doc['adjoint_flow'][-1]['right'])
        end,entire=flow(-co['cm'],-co['adjoint_forcing'],initial,r-l)
        doc['stage']='adjoint_mean_forward'
        doc['adjoint_flow'].append(dict(common_row=i,interval=list(map(str,(l,r))),
             left=record(initial),right=record(end),entire=record(entire)));return True
    if len(doc['response_flow_reverse'])<N:
        i=N-1-len(doc['response_flow_reverse']);l,r=c['cuts'][i:i+2]
        co={k:box_from_record(v) for k,v in doc['coefficient_rows'][i]['coefficients'].items()}
        initial=c['response_mean_R'] if i==N-1 else box_from_record(doc['response_flow_reverse'][-1]['left'])
        end,entire=flow(-co['cm'],-co['response_forcing'],initial,r-l)
        doc['stage']='response_mean_backward'
        doc['response_flow_reverse'].append(dict(common_row=i,interval=list(map(str,(l,r))),
             left=record(end),right=record(initial),entire=record(entire)));return True
    if len(doc['residual_rows'])<N:
        doc['stage']='full_body_residuals'
        doc['residual_rows'].append(residual_row(c,doc,len(doc['residual_rows'])));return True
    for name in ('response','adjoint'):
        if len(doc[name+'_jumps'])<len(c[name]['nodes'])-2:
            doc['stage']=name+'_exact_nonmean_jumps'
            doc[name+'_jumps'].append(jump_row(c,name,len(doc[name+'_jumps'])+1));return True
    summarize(c,doc);return False


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','mean','response','adjoint'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--waist',type=Path,default=Path('notes/2026-11-14-R133-final-waist-mean-adjoint-column-rational.json'))
    p.add_argument('--amp-multiplier',type=Fraction,required=True)
    p.add_argument('--analytic-width',type=Fraction,default=Fraction(1,2048))
    p.add_argument('--radial-subdivisions',type=int,default=1)
    p.add_argument('--resume',type=Path);p.add_argument('--max-new-rows',type=int)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if args.analytic_width<0:raise ValueError('nonnegative explicitly fixed analytic width required')
    if args.out.exists():raise FileExistsError('preserve all previous complete, partial and failed outputs')
    c,doc=prepare(args)
    if args.resume:
        old=read(args.resume);validate_resume(c,doc,old)
        doc['resume_history']=old['resume_history']+[dict(path=str(args.resume),sha256=sha(args.resume),
             prior_stage=old['stage'],original_complete=False,missing_exit_not_inferred=True)]
    count=0;checkpoint=time.monotonic()
    try:
        if args.max_new_rows is not None and args.max_new_rows<1:raise ValueError('positive explicit new row budget required')
        while args.max_new_rows is None or count<args.max_new_rows:
            if not advance_one(c,doc):break
            count+=1
            if time.monotonic()-checkpoint>15:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(stage=doc['stage'],new_rows=count,total_common_cells=doc['total_common_cells']),flush=True)
                checkpoint=time.monotonic()
        doc['explicit_complete_stage_row_prefix_only']=not doc['complete']
    except Exception as exc:
        doc['complete']=False;doc['failure']=dict(type=type(exc).__name__,message=str(exc));raise
    finally:
        doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],stage=doc['stage'],failure=doc['failure'],out=str(args.out)),flush=True)


if __name__=='__main__':
    main()
