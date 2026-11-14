#!/usr/bin/env python3
"""Actual moving-curvature-angle Cauchy energy with the complete mean.

All real radial boxes, the original full eta interval, all physical angular
cells, and all infinite Fourier variations are retained. Exact finite
candidate polynomials only describe the centre. The comparison is a genuine
two by two positive evolution, including the independent mean. This does
not solve the nonlinear BVP or discard the centre residual.
"""
from __future__ import annotations
import argparse,json,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES
from fourfold_codazzi_curvature_angle_energy_prefix import (
    read,dyadic,target_bounds,polynomial_ranges,actual_jump)
from fourfold_phase_newton_source_centered import CenteredPolynomial
from fourfold_phase_beta_bulk_box import (
    Box,CBox,zeros,arb_box,scalar_arb,reduce_box,square_box,DirectedFFT)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def maxabs(x):return arb(float(np.max(np.maximum(np.abs(x.lo),np.abs(x.hi))))).upper()
def upper(x):return arb(float(np.max(x.hi))).upper()
def lower(x):return arb(float(np.min(x.lo))).lower()
def interval(x):return lower(x).union(upper(x))
def mean_box(x):return scalar_arb(reduce_box(x)/len(x.lo))


def angular_fields(y,m,alpha,s,angles,fft):
    """Directed node and complete closed-cell values of u,v,u_theta,v_theta,v_tt."""
    grid=1
    while grid<=2*m:grid*=2
    fields=[]
    for component,order in ((0,0),(1,0),(0,1),(1,1),(1,2)):
        c=zeros((grid,))
        if component and order==0:c[0]=CBox(arb_box(s+alpha*y[m]))
        for j in range(1,m+1):
            value=alpha*(y[m+j] if component else y[j-1])/2
            base=CBox(arb_box(value),0.) if component else CBox(0.,arb_box(-value))
            for _ in range(order):base=base*CBox(0.,4*j)
            c[j]=base;c[-j]=CBox(base.real,-base.imag)
        fields.append(CenteredPolynomial(c,arb(0),m,fft))
    modes=np.asarray([j if j<grid//2 else j-grid for j in range(grid)])
    frequencies=4*modes;block=zeros((angles,3*len(fields)))
    for j,p in enumerate(fields):
        value=p.c
        for derivative in range(3):
            block[modes%angles,3*j+derivative]=value
            value=value*CBox(0.,Box(frequencies))
    samples=fft.fft(block,inverse=True)*angles
    if not np.all((samples.imag.lo<=0)&(samples.imag.hi>=0)):
        raise ValueError('finite real candidate lost its exact reflection reality')
    half=arb.pi()/(4*angles);h=arb_box(half);closed=[];nodes=[]
    for j,p in enumerate(fields):
        # The complete original coefficient uncertainty is paid separately
        # for every field, including the differentiated ones.
        remainder=(p.error+half**3*p.norm(3)/6).upper()
        fee=(h*Box(samples.real[:,3*j+1].abs_upper())+
             h*h*Box(samples.real[:,3*j+2].abs_upper())/2+arb_box(remainder)).hi
        closed.append(samples.real[:,3*j]+Box(-fee,fee))
        error=arb_box(p.error).hi
        nodes.append(samples.real[:,3*j]+Box(-error,error))
    return closed,nodes


def row_coefficients(fields,nodes,a,angles):
    u,v,ut,vt,vtt=fields
    if not np.all(v.hi<0):raise ValueError('whole-circle negative v gate is unresolved')
    g=(-upper(v)).lower();vmax=(-lower(v)).upper()
    C=Box(1.)/v;Dcells=mean_box(C)
    Ctt=2*square_box(vt)/(square_box(v)*v)-vtt/square_box(v)
    Cttmax=maxabs(Ctt)
    trap=mean_box(Box(1.)/nodes[1]);spacing=arb.pi()/(2*angles)
    trapfee=(spacing**2*Cttmax/12).upper()
    Dtrap=trap+arb(0,trapfee)
    D=Dcells.intersection(Dtrap)
    if not D<0:raise ValueError('complete actual C mean is not strictly negative')
    mean=1/D
    K=arb_box(a['K']);beta=arb_box(a['beta']);Db=arb_box(D)
    u2=square_box(u);v2=square_box(v);S=u2+K*v2
    # C*S=u^2/v+K*v avoids an unnecessary denominator dependency.
    Smean=(mean_box(u2/v+K*v)/D).intersection(interval(S))
    dphi=beta*(arb_box(Smean)-S)
    R=upper(u2-K*v2).sqrt().upper()
    L=upper(square_box(Db*v)*(square_box(ut)-K*square_box(vt))).sqrt().upper()
    G1=-beta*(1+3*u2+K*v2)-dphi/2
    G2=beta*(1-u2-3*K*v2)+arb_box(a['K1']/(2*a['K']))-dphi/2
    nonlocal_fee=(abs(a['beta'])*R*L/2).upper()
    gf=(max(upper(G1),upper(G2))+nonlocal_fee).upper()
    gb=(max(-lower(G1),-lower(G2))+nonlocal_fee).upper()
    q=(-a['K']).sqrt()
    off12=(a['gamma']*q*L).upper();off21=(2*abs(a['beta']*mean)*R).upper()
    c=a['beta']*(1-Smean)
    return dict(v=interval(v),v_abs_lower=g,v_abs_upper=vmax,
        actual_D=D,actual_m=mean,D_closed_cell_average=Dcells,D_node_average=trap,
        D_trapezoid_error=trapfee,full_C_theta_theta_absolute=Cttmax,
        actual_S_mean=Smean,actual_d_phi=interval(dphi),actual_R_upper=R,actual_L_upper=L,
        full_u_theta_absolute=maxabs(ut),full_v_theta_absolute=maxabs(vt),
        energy_diagonal_1=interval(G1),energy_diagonal_2=interval(G2),
        nonlocal_primitive_energy_fee=nonlocal_fee,forward_rate=gf,backward_rate=gb,
        coupling_mean_to_energy=off12,coupling_energy_to_mean=off21,
        forward_mean_rate=c.upper(),backward_mean_rate=(-c).upper(),q=q,
        extra_v_residual_energy_factor=(L/(4*g)).upper(),
        physical_to_phi_density_upper=upper(C/Db))


def mat_upper(A):
    return arb_mat([[max(arb(0),A[i,j].upper()).upper() for j in range(A.ncols())]
                    for i in range(A.nrows())])


def matrix_record(A):return [[record(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]


def comparison_matrix(c,reverse=False,positive_diagonal=False):
    diag=(c['backward_rate'],c['backward_mean_rate']) if reverse else (c['forward_rate'],c['forward_mean_rate'])
    if positive_diagonal:diag=tuple(max(arb(0),x).upper() for x in diag)
    return arb_mat([[diag[0],c['coupling_mean_to_energy']],
                    [c['coupling_energy_to_mean'],diag[1]]])


def moving_jump(saved,nodes,j,alpha,m,left,right):
    delta=actual_jump(saved,nodes,j)
    du=(abs(alpha)*sum((abs(exact_arb(z)) for z in delta[:m]),arb(0))).upper()
    dv=(abs(alpha)*sum((abs(exact_arb(z)) for z in delta[m:]),arb(0))).upper()
    g=min(left['v_abs_lower'],right['v_abs_lower']).lower()
    vmax=max(left['v_abs_upper'],right['v_abs_upper']).upper()
    dmin=min((-left['actual_D']).lower(),(-right['actual_D']).lower()).lower()
    dmax=max(abs(left['actual_D']),abs(right['actual_D'])).upper()
    deltaC=(dv/(g*g)).upper()
    deltaWeight=(deltaC/dmin+deltaC/(g*dmin*dmin)).upper()
    deltaPhi=(arb.pi()*deltaWeight/4).upper()
    deltaTheta=(vmax*dmax*deltaPhi).upper()
    ut=max(left['full_u_theta_absolute'],right['full_u_theta_absolute']).upper()
    vt=max(left['full_v_theta_absolute'],right['full_v_theta_absolute']).upper()
    ju=(du+ut*deltaTheta).upper();jv=(dv+vt*deltaTheta).upper()
    q=max(left['q'].upper(),right['q'].upper()).upper()
    energy=(ju*ju+q*q*jv*jv).sqrt().upper()
    return dict(radius=str(nodes[j]),candidate_join=j,
        exact_physical_u_jump_A0=record(du),exact_physical_v_jump_A0=record(dv),
        both_negative_v_gap=record(g),both_mean_C_abs_lower=record(dmin),
        mean_C_difference_upper=record(deltaC),curvature_angle_difference_upper=record(deltaPhi),
        inverse_angle_difference_upper=record(deltaTheta),moving_u_jump_absolute=record(ju),
        moving_v_jump_absolute=record(jv),moving_energy_jump=record(energy),moving_mean_jump=record(jv)),(energy,jv)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--target',type=Path,default=Path('notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    ap.add_argument('--collar',type=Path,default=Path('notes/2026-11-13-R133-actual-root-collar-complete-coefficients-v2-native.json.gz'))
    ap.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    ap.add_argument('--right',type=Fraction,default=Fraction(1,5))
    ap.add_argument('--angles',type=int,default=4096)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve each actual moving-energy attempt')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    native=read(args.target);types=read(args.type_cover)
    inputs=[args.candidate,args.target,args.type_cover]
    if (meta['coordinates']!=COORDINATES or meta['object_sha256']!=native['object_sha256']
        or not native['complete'] or not types['complete'] or not types['exactly_one_real_K_root']
        or types['inputs'].get(str(args.target))!=sha(args.target)):
        raise ValueError('the complete actual candidate and true target identities differ')
    right=args.right
    if not 0<right<=Fraction(119,500):raise ValueError('only the proved strictly negative prefix is accepted')
    target_rows=list(native['rows'])
    if right>Fraction(1,5):
        collar=read(args.collar);inputs.append(args.collar)
        if (not collar['complete'] or not collar['whole_real_radial_interval']
            or collar['object_sha256']!=native['object_sha256']
            or collar['parameter_half_width']!=native['parameter_half_width']
            or collar['inputs'].get(str(args.type_cover))!=sha(args.type_cover)):
            raise ValueError('the full genuine root collar is required beyond .2')
        target_rows.extend(collar['rows'])
    nuq=Fraction(meta['exact_float_nu']);nulo,nuhi=map(Fraction,types['exact_nu_interval'])
    if nuq!=dyadic(meta['nu']) or not nulo<=nuq<=nuhi:raise ValueError('actual fixed nu lies outside the proved type cover')
    alpha=exact_arb(dyadic(meta['amplitude']));nu=exact_arb(nuq);m=int(meta['modes'])
    angles=args.angles
    if angles<=2*m or angles&(angles-1):raise ValueError('a complete power-of-two Fourier grid is required')
    nodes=list(map(dyadic,saved['radial_nodes']))
    if nodes[0]!=0 or nodes[-1]<right:raise ValueError('candidate extrapolation is forbidden')
    target_nodes=[Fraction(row['interval'][0]) for row in target_rows]+[Fraction(target_rows[-1]['interval'][1])]
    if target_nodes[0]!=0 or any(Fraction(a['interval'][1])!=Fraction(b['interval'][0]) for a,b in zip(target_rows,target_rows[1:])):
        raise ValueError('all original native closed boxes must form a continuous target cover')
    cuts=sorted({Fraction(0),right}|{x for x in (Fraction(1,20),Fraction(9,50)) if x<right}|
        {x for x in nodes if 0<x<right}|{x for x in target_nodes if 0<x<right})
    doc=dict(kind='actual_full_Fourier_moving_curvature_angle_mean_energy_v2',complete=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in inputs},object_sha256=meta['object_sha256'],
        candidate_metadata=meta,actual_fixed_nu=str(nuq),exact_amplitude=str(dyadic(meta['amplitude'])),
        exact_interval=['0',str(right)],parameter_half_width=native['parameter_half_width'],
        whole_affine_parameter_interval=True,complete_primitive_tail=True,closed_angular_cells=angles,
        all_Fourier_variations_retained=True,independent_allowed_mean_retained=True,
        rows=[],jumps=[],failure=None,full_body_BVP_inverse_not_proved=True,
        actual_centre_continuous_PDE_residual_not_certified_here=True,
        original_finite_BVP_outcome_not_changed=True,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_reciprocal_candidate_tools.py',
            'fourfold_codazzi_curvature_angle_energy_prefix.py','fourfold_phase_newton_source_centered.py',
            'fourfold_phase_correlated_curvature.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')})
    fft=DirectedFFT();calculated=[];last=time.monotonic()
    try:
        for index,(left,end) in enumerate(zip(cuts,cuts[1:])):
            j=min(bisect_right(nodes,left)-1,len(nodes)-2);k=bisect_right(target_nodes,left)-1
            row=target_rows[k];tl,tr=map(Fraction,row['interval'])
            if not nodes[j]<=left<end<=nodes[j+1] or not tl<=left<end<=tr:
                raise ValueError('the common candidate/actual-target refinement is incomplete')
            a=target_bounds(row,left,end,nu);y,_=polynomial_ranges(saved,nodes,j,left,end)
            fields,node_fields=angular_fields(y,m,alpha,a['s'],angles,fft)
            c=row_coefficients(fields,node_fields,a,angles);calculated.append(c)
            doc['rows'].append(dict(interval=[str(left),str(end)],candidate_piece=j,native_row=k,
                actual_scalar_germ=row['actual_scalar_germ'],
                actual_target={name:record(a[name]) for name in ('gamma','beta','K','K1')},
                bounds={name:record(value) for name,value in c.items()}))
            if time.monotonic()-last>20:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(rows=len(doc['rows']),right=str(end),L=c['actual_L_upper'].str(9),m=c['actual_m'].str(9)),flush=True)
                last=time.monotonic()
        jump_at={}
        for i in range(1,len(calculated)):
            if doc['rows'][i-1]['candidate_piece']==doc['rows'][i]['candidate_piece']:continue
            j=doc['rows'][i]['candidate_piece']
            if nodes[j]!=cuts[i]:raise ValueError('an actual candidate join is missing from the common partition')
            entry,amount=moving_jump(saved,nodes,j,alpha,m,calculated[i-1],calculated[i])
            doc['jumps'].append(entry);jump_at[i]=arb_mat([[amount[0]],[amount[1]]])
        matrices={};jump_results={}
        for reverse in (False,True):
            exact=arb_mat([[1,0],[0,1]]);uniform=arb_mat([[1,0],[0,1]]);jump=arb_mat([[0],[0]])
            order=range(len(calculated)-1,-1,-1) if reverse else range(len(calculated))
            for i in order:
                entry=jump_at.get(i+1 if reverse else i)
                if entry is not None:jump=mat_upper(jump+entry)
                length=exact_arb(cuts[i+1]-cuts[i]);c=calculated[i]
                flow=mat_upper((comparison_matrix(c,reverse)*length).exp())
                positive_flow=mat_upper((comparison_matrix(c,reverse,True)*length).exp())
                exact=mat_upper(flow*exact);uniform=mat_upper(positive_flow*uniform)
                jump=mat_upper(flow*jump)
            name='backward' if reverse else 'forward';matrices[name]=(exact,uniform)
            jump_results[name]=jump
        qmin=min(c['q'].lower() for c in calculated).lower()
        qleft=calculated[0]['q'].lower();qright=calculated[-1]['q'].lower()
        jump_sum=arb_mat([[sum((j[0,0] for j in jump_at.values()),arb(0)).upper()],
                          [sum((j[1,0] for j in jump_at.values()),arb(0)).upper()]])
        bounds={}
        for name,(exact,uniform) in matrices.items():
            qi=qright if name=='backward' else qleft
            bounds[name]=dict(endpoint_matrix=matrix_record(exact),
                all_subinterval_positive_majorant=matrix_record(uniform),
                complete_initial_energy_endpoint_gain=record((exact[0,0]+exact[0,1]/qi).upper()),
                complete_initial_energy_uniform_gain=record((uniform[0,0]+uniform[0,1]/qi).upper()),
                full_ordinary_L1_energy_source_uniform_gain=record((uniform[0,0]+uniform[0,1]/qmin).upper()),
                actual_moving_jump_endpoint_energy=record(jump_results[name][0,0]),
                actual_moving_jump_uniform_energy=record((uniform*jump_sum)[0,0].upper()))
        doc.update(complete=True,all_closed_radial_and_angular_boxes_passed=True,
            all_exact_PPoly_moving_jumps_paid=True,bounds=bounds,
            global_bounds={name:record(value) for name,value in dict(
                q_abs_lower=qmin,minimum_actual_v_abs=min(c['v_abs_lower'] for c in calculated).lower(),
                maximum_actual_R=max(c['actual_R_upper'] for c in calculated).upper(),
                maximum_actual_L=max(c['actual_L_upper'] for c in calculated).upper(),
                total_actual_moving_energy_jumps=jump_sum[0,0],
                total_actual_moving_mean_jumps=jump_sum[1,0]).items()})
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),jumps=len(doc['jumps']),
        bounds=doc.get('bounds'),wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
