#!/usr/bin/env python3
"""Actual outer low46 flow in physical trace-zero coordinates.

Y=sqrt(r*w^3)*(P_sine,K_cosine) has source-x matrix
 [[(ell-s)/2,-m*s],[-m*ell,-(ell-s)/2]], s=r_x/r, ell=w_x/w.
The physical mode enters linearly.  One shared positive derivative
majorant at the largest mode encloses the Taylor remainder for every
mode; signed Taylor polynomials and all projective columns remain
separate.  The original true low46 head slopes, real metric, and exact
mu11 conversion are retained.  Existing m2/m4 columns are independently
intersected at every completed original segment.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import resource
import time

from flint import arb,arb_mat,arb_series,ctx

from closure_outer_taylor_shared_flow import raw_source_identity
from closure_projective_interval_column import ProjectiveColumn
from closure_real_head_source_enclosure import exact_q,power2
from closure_real_linear_head_enclosure import PositiveKernels
from closure_split_joint_io_v2 import digest,read_field
from closure_taylor_cut_slope_v2 import (source_series,rough_radius,monotone_parts,
    record,ball,intersect,add_error,column_record,restore_column,save)
from tail_r33_middle_ordered_physical import SourceValues


EXPECTED={
 'closure_outer_taylor_shared_flow.py':'81d8bd9ad3da434eb8ab98d381a32a09bbe7aca5fa3be8a0bfe493ccd62455b7',
 'closure_projective_interval_column.py':'45997a1d5be6326a1ebbe85ac4240ea7d9dde1c2fb6acdf832460dade89e4f97',
 'closure_real_head_source_enclosure.py':'97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47',
 'closure_real_linear_head_enclosure.py':'1b8023b53eeca7a0ef28816a99b1b7d4a43f025c2482afae9e88db572e174b8e',
 'closure_taylor_cut_slope_v2.py':'8e150b6fe16c33da98043bc7ebe952abf123e2f7c8da8ebbfb10bfec700fb5ea',
 'tail_r33_middle_ordered_physical.py':'ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e'}


def jets(h,segment,xbase,span,rbase,order,sign):
    w,g=source_series(h,segment,xbase,span,order,sign)
    r=arb_series([rbase]+[g[k-1]/k for k in range(1,order+2)],prec=order+2)
    x=arb_series([xbase,span],prec=order+2)
    if segment['transition']:
        derivative=30*x*x*(1-x)*(1-x)
    else:
        derivative=arb_series([0],prec=order+2)
    ell=span*(segment['log_jump']*derivative-7*segment['length']/h.sqrt12)
    s=g/r
    return (ell-s)/2,s,ell,g


def matrix_jets(d,s,ell,mode,order,absolute=False):
    out=[]
    for k in range(order+1):
        rows=[[d[k],-mode*s[k]],[-mode*ell[k],-d[k]]]
        if absolute:rows=[[abs(x).upper() for x in row] for row in rows]
        out.append(arb_mat(rows))
    return out


def coefficients(M,order,initial):
    result=[initial]
    for n in range(order):
        total=arb_mat(2,2)
        for k in range(n+1):total+=M[k]*result[n-k]
        result.append(total/(n+1))
    return result


def balanced_majorant(d,s,ell,max_mode):
    du,su,eu=abs(d).upper(),abs(s).upper(),abs(ell).upper()
    B=(eu/su).sqrt() if su>0 and eu>0 else arb(1)
    if not B>0:raise ArithmeticError('The local balance must be strictly positive')
    q=(du+max(max_mode*su*B,max_mode*eu/B)).upper()
    if not q<arb(1)/2:raise ArithmeticError('Subdivide the full46 balanced local integral norm')
    C=(1/(1-q)).upper()
    major=arb_mat([[C,(C/B).upper()],[(C*B).upper(),C]])
    return B,q,major


def taylor_physical(h,segment,left,right,radius,modes,order,tol):
    sign=segment['_monotone_sign'];x0=exact_q(left);span=exact_q(right-left)
    rr,_=rough_radius(h,segment,left,right,radius)
    d,s,e,g=jets(h,segment,x0,span,radius,order,sign)
    di,si,ei,gi=jets(h,segment,x0.union(exact_q(right)),span,rr,order,sign)
    B,q,major=balanced_majorant(di[0],si[0],ei[0],max(modes))
    # Absolute coefficientwise domination at max(m) is valid because
    # the diagonals are independent of m and both offdiagonals linear.
    derivative=coefficients(matrix_jets(di,si,ei,max(modes),order,True),order+1,major)[order+1]
    rem=[[derivative[i,j].upper() for j in range(2)] for i in range(2)]
    error=max((rem[0][0]+rem[1][0]/B).upper(),(B*rem[0][1]+rem[1][1]).upper())
    if not error<tol:raise ArithmeticError('Subdivide the full46 rigorous Taylor remainder')
    identity=arb_mat([[1,0],[0,1]]);flows=[]
    for m in modes:
        series=coefficients(matrix_jets(d,s,e,m,order),order,identity)
        total=arb_mat(2,2)
        for C in series:total+=C
        flow=[[add_error(total[i,j],rem[i][j]) for j in range(2)] for i in range(2)]
        if any(not x.is_finite() for row in flow for x in row):
            raise ArithmeticError('A true physical Taylor entry is nonfinite')
        flows.append(flow)
    dr=sum((g[k]/(k+1) for k in range(order)),arb(0))
    dr=add_error(dr,abs(gi[order]).upper()/(order+1))
    if not dr>0:raise ArithmeticError('Subdivide a true positive-radius increment')
    return flows,intersect(radius+dr,rr),error,q


def root_physical(h,segment,left,right,radius,modes):
    rr,dr=rough_radius(h,segment,left,right,radius)
    span=exact_q(right-left)
    source=h.source_point(segment,exact_q(left).union(exact_q(right)))
    w,ell=source['w'],source['log_w_x'];E=1+w*w
    rx=abs(w*ell)/(8*E*E.sqrt())+h.alpha*source['ro_x']/E
    s=span*rx/rr;e=span*ell;d=(e-s)/2
    B,q,unused=balanced_majorant(d,s,e,max(modes))
    error=(q*q/(1-q)).upper()
    rem=[[error,(error/B).upper()],[(error*B).upper(),error]]
    flows=[]
    for m in modes:
        M=[[d,-m*s],[-m*e,-d]]
        flows.append([[add_error(M[i][j]+(1 if i==j else 0),rem[i][j])
                       for j in range(2)] for i in range(2)])
    return flows,intersect(radius+arb(0).union(dr),rr),error,q


def to_Q(column,r,w,mode):
    F=(r*w*w*w).sqrt()
    return -w/(mode*r**3*F)*column.values()[0]


def coordinate(h,r,w,mode,mu):
    F=(r*w*w*w).sqrt();scale=(r/h.rc)**(mode*mode-4)
    return arb_mat([[-F*mode*r**3*scale/w,0],
        [F*mode*mode*r**3*scale/w,F*h.sqrt12*mu/(r**4*w*w*scale)]])


def triangle_inverse(C):
    return arb_mat([[1/C[0,0],0],[-C[1,0]/(C[0,0]*C[1,1]),1/C[1,1]]])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('ready','outer-flow','head-summary','head-manifest','true-slope','out-prefix'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--modes',default='2:92')
    p.add_argument('--precision',type=int,default=256)
    p.add_argument('--order',type=int,default=24)
    p.add_argument('--remainder-bits',type=int,default=100)
    p.add_argument('--root-bits',type=int,default=160)
    p.add_argument('--initial-parts',type=int,default=8)
    p.add_argument('--rss-kib',type=int,default=40960)
    p.add_argument('--resume',type=Path)
    a=p.parse_args();began=time.monotonic()
    if ':' in a.modes:
        first,last=map(int,a.modes.split(':'));modes=list(range(first,last+1,2))
    else:modes=[int(x) for x in a.modes.split(',')]
    if (modes!=sorted(set(modes)) or any(m<2 or m>92 or m%2 for m in modes)
            or not modes or a.precision<a.root_bits+32 or a.order<4 or a.initial_parts<1):
        raise ValueError('Retain a defined subwindow of the actual even low46 modes and validated precision')
    if Path(str(a.out_prefix)+'.json').exists() or Path(str(a.out_prefix)+'-failure.json').exists():
        raise FileExistsError('A completed or failed physical-window primary must be retained')
    ctx.prec,ctx.cap,ctx.threads=a.precision,a.order+2,1
    for name,sha in EXPECTED.items():
        if digest(Path(__file__).with_name(name))!=sha:
            raise ValueError('A frozen actual-source implementation changed: '+name)
    paths=[getattr(a,k) for k in ('ready','outer_flow','head_summary','head_manifest','true_slope')]
    hashes={str(x):digest(x) for x in paths}
    flow=json.loads(a.outer_flow.read_text());head=json.loads(a.head_summary.read_text())
    manifest=json.loads(a.head_manifest.read_text());precise=json.loads(a.true_slope.read_text())
    if (not all(flow['gates'].values()) or not all(precise['gates'].values())
            or head['modes']!=list(range(2,93,2)) or head['start_physical_node']!=12
            or head['far_physical_node']!=225 or any(not r['height_chart_paid'] for r in manifest['endpoint_rows'])
            or head['source_enclosure_sha256']!=EXPECTED['closure_real_head_source_enclosure.py']
            or manifest['source_enclosure_sha256']!=head['source_enclosure_sha256']):
        raise ValueError('The complete true original low46 head and refined two-mode slope are required')
    ready_hash=hashes[str(a.ready)]
    if (manifest['input_hashes'].get(str(a.ready))!=ready_hash
            or flow['input_hashes'].get(str(a.ready))!=ready_hash
            or flow['input_hashes'].get(str(a.true_slope))!=hashes[str(a.true_slope)]):
        raise ValueError('The complete head and outer metric differ')
    if digest(Path(head['output']))!=head['output_sha256']:
        raise ValueError('The paid complete low46 primary changed')
    hashes[head['output']]=head['output_sha256']
    ready=dict(rationalDeepModel=read_field(a.ready,'rationalDeepModel'),
        shallowSourceParameters=read_field(a.ready,'shallowSourceParameters'))
    identity=[raw_source_identity(ready,n) for n in (11,10)]
    h=SourceValues(ready);del ready
    kernel=PositiveKernels(h,12,4)
    h.cells={n:kernel.source_cell(n) for n in (11,10)}
    order=[(n,j) for n in (11,10) for j in range(9)]
    flow_stem=str(a.outer_flow)[:-5]
    anchors={}
    for n,j in order:
        path=Path(flow_stem+f'-cell{n:03d}-seg{j}.json')
        anchors[n,j]=json.loads(path.read_text());hashes[str(path)]=digest(path)
        if anchors[n,j]['config']!=flow['config']:raise ValueError('An original real outer anchor differs')
    b=ball(precise['cut_radius']);mu=ball(flow['config']['global_mu_star'])
    w_b=h.source_point(h.cells[11]['segments'][0],arb(0))['w']
    F_b=(b*w_b*w_b*w_b).sqrt()
    original_slopes={r['mode']:ball(r['raw_worker_slope']) for r in head['endpoint_rows']}
    better={r['mode']:r for r in precise['rows']}
    slopes={m:(intersect(original_slopes[m],ball(better[m]['true_slope_mu_outer']))
               if m in better else original_slopes[m]) for m in modes}
    columns=[]
    for m in modes:
        P=-m*b**3/w_b
        K=m*m*b**3/w_b+h.sqrt12*mu*slopes[m]/(b**4*w_b*w_b)
        columns.append([ProjectiveColumn([F_b*P,F_b*K]),
            ProjectiveColumn([arb(1),arb(0)]),ProjectiveColumn([arb(0),arb(1)])])
    config=dict(modes=modes,cells=[11,10],precision=a.precision,order=a.order,
        remainder_bits=a.remainder_bits,root_bits=a.root_bits,initial_parts=a.initial_parts,
        input_hashes=hashes,source_hashes=EXPECTED,entrypoint_sha256=digest(__file__),
        io_helper_sha256=digest(Path(__file__).with_name('closure_split_joint_io_v2.py')),
        true_cut_radius=record(b),true_cut_w=record(w_b),global_mu11=record(mu),
        actual_true_initial_slopes={str(m):record(slopes[m]) for m in modes},
        coordinates='Y=sqrt(r*w^3)*(P_sine,K_cosine); exact trace0; both source and physical functions unchanged',
        exact_coordinate_determinant_from_global_qv='-m*sqrt12*mu11, independent of r',
        full_signed_mode_data_not_zeroed=True)
    counts=dict(taylor=0,root_brackets=0,rejected=0);completed=[];cell_rows=[]
    greatest=arb(0);greatest_integral=arb(0)
    if a.resume:
        old=json.loads(a.resume.read_text())
        if old['config']!=config:raise ValueError('Recovery refers to another exact problem/arithmetic')
        completed=[tuple(x) for x in old['completed_groups']]
        if completed!=order[:len(completed)]:raise ValueError('Recovery source order differs')
        columns=[[restore_column(v) for v in row] for row in old['columns']]
        counts=old['counts'];cell_rows=old['cell_rows']
        greatest=ball(old['greatest_balanced_Taylor_remainder'])
        greatest_integral=ball(old['greatest_balanced_integral_norm'])
    def guard():
        peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak>a.rss_kib:raise MemoryError('The observed owned physical46 RSS exceeded its stop threshold: '+str(peak))
    try:
        for index,(n,j) in enumerate(order):
            if (n,j) in completed:continue
            segment=h.cells[n]['segments'][j]
            segment['physical_inner_radius']=b if index==0 else ball(anchors[order[index-1]]['radius'])
            segment['physical_outer_radius']=ball(anchors[n,j]['radius'])
            radius=segment['physical_inner_radius']
            for left,right,sign in monotone_parts(segment,a.root_bits):
                segment['_monotone_sign']=sign
                pieces=([(left,right,0)] if sign==0 else
                    [(left+(right-left)*k/a.initial_parts,left+(right-left)*(k+1)/a.initial_parts,0)
                     for k in range(a.initial_parts)])
                stack=list(reversed(pieces))
                while stack:
                    lo,hi,level=stack.pop()
                    try:
                        T,next_radius,error,q=(root_physical(h,segment,lo,hi,radius,modes)
                            if sign==0 else taylor_physical(h,segment,lo,hi,radius,modes,
                                a.order,power2(-a.remainder_bits)))
                        advanced=[]
                        for row,transition in zip(columns,T):
                            new=[]
                            for v in row:
                                c=restore_column(column_record(v));c.advance(transition);new.append(c)
                            advanced.append(new)
                    except (ArithmeticError,ValueError,ZeroDivisionError) as error0:
                        if sign==0 or level>=40:
                            raise ArithmeticError('Unresolved physical46 true panel '+str((n,j,lo,hi,sign))+': '+str(error0)) from error0
                        mid=(lo+hi)/2;stack.extend([(mid,hi,level+1),(lo,mid,level+1)])
                        counts['rejected']+=1;continue
                    columns=advanced;radius=next_radius
                    counts['root_brackets' if sign==0 else 'taylor']+=1
                    greatest_integral=max(greatest_integral,q)
                    if sign:greatest=max(greatest,error)
                    guard()
            radius=intersect(radius,segment['physical_outer_radius'])
            w=h.source_point(segment,arb(1))['w']
            # This independent conversion is checked at EVERY completed
            # segment, not just at a favorable selected endpoint.
            comparisons=[]
            for k,m in enumerate(modes):
                if m not in (2,4):continue
                z=(0 if m==2 else 1);old=anchors[n,j]['columns'][z]
                shared=restore_column(old[0]).values();basis=restore_column(old[2]).values()
                delta=(b/h.rc)**(m*m-4)*ball(better[m]['true_minus_shared_exact_slope'])
                oldQ=(radius/h.rc)**(m*m-4)*(shared[0]+delta*basis[0])
                newQ=to_Q(columns[k][0],radius,w,m)
                agree=intersect(newQ,oldQ)
                comparisons.append(dict(mode=m,new_S0_Q=record(newQ),old_true_S0_Q=record(oldQ),
                    intersection=record(agree)))
            if j==8:
                rows=[];F=(radius*w*w*w).sqrt()
                oldcell=next(c for c in flow['cell_rows'] if c['cell']==n)
                for k,m in enumerate(modes):
                    S=to_Q(columns[k][0],radius,w,m)
                    basis=arb_mat([[columns[k][z+1].values()[i] for z in range(2)] for i in range(2)])
                    compared=False
                    if m in (2,4):
                        oldmode=next(x for x in oldcell['modes'] if x['mode']==m)
                        S=intersect(S,ball(oldmode['S0_true_Q']))
                        C_R=coordinate(h,radius,w,m,mu);C_b=coordinate(h,b,w_b,m,mu)
                        oldPhi=arb_mat([[ball(v) for v in row] for row in oldmode['global_gauge_fundamental_matrix']])
                        transformed=C_R*oldPhi*triangle_inverse(C_b)
                        for row in range(2):
                            for col in range(2):intersect(basis[row,col],transformed[row,col])
                        compared=True
                    rows.append(dict(mode=m,S0_true_Q=record(S),height_chart_excludes_zero=not S.contains(0),
                        true_physical_PK_per_unit_shallow_Q=[record(x/F) for x in columns[k][0].values()],
                        trace0_physical_fundamental_matrix=[[record(basis[i,jj]) for jj in range(2)] for i in range(2)],
                        old_m2m4_full_matrix_identity_compared=compared,
                        columns=[column_record(c) for c in columns[k]]))
                cell_rows.append(dict(cell=n,endpoint_physical_node=n,radius=record(radius),w=record(w),
                    modes=rows,all_true_height_charts_paid=all(r['height_chart_excludes_zero'] for r in rows)))
            completed.append((n,j))
            cp=dict(status='Complete physical trace0 actual source segment',config=config,
                completed_groups=completed,cell_rows=cell_rows,radius=record(radius),w=record(w),
                columns=[[column_record(c) for c in row] for row in columns],counts=counts,
                independent_m2m4_comparisons=comparisons,
                greatest_balanced_Taylor_remainder=record(greatest),greatest_balanced_integral_norm=record(greatest_integral),
                elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            path=Path(str(a.out_prefix)+f'-completed-cell{n:03d}-segment{j}.json')
            if path.exists():raise FileExistsError('A completed physical46 segment would be overwritten')
            save(path,cp)
            print(json.dumps(dict(event='actual_physical_window_segment_complete',cell=n,segment=j,
                modes=len(modes),counts=counts,elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=cp['peak_RSS_KiB'])),flush=True)
        if completed!=order:raise ValueError('The whole actual two-cell window is incomplete')
        charts=all(c['all_true_height_charts_paid'] for c in cell_rows)
        gates=dict(same_exact_metric_and_caps_proved_inactive=True,all_declared_true_low_modes_retained=True,
            true_head_linear_boundary_not_finite_Robin=True,all18_real_source_segments_complete=True,
            physical_trace0_identity_and_exact_constant_determinant=True,
            rigorous_shared_max_mode_derivative_majorant=True,all_critical_root_strips_and_Taylor_remainders_paid=True,
            independent_m2m4_source_and_matrix_identity=True,all_true_endpoint_height_charts_paid=charts)
        result=dict(status='Complete actual physical low-window flow and height-chart certificate',
            all_gates=all(gates.values()),gates=gates,config=config,cell_rows=cell_rows,
            completed_groups=completed,counts=counts,source_identity=identity,
            greatest_balanced_Taylor_remainder=record(greatest),greatest_balanced_integral_norm=record(greatest_integral),
            input_hashes=hashes,complete_outer_PDE_or_full_frequency_fixed_point_claimed=False,
            whole_field_Green_profiles_for_new_modes_not_yet_paid=True,
            elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(Path(str(a.out_prefix)+'.json'),result);guard()
        print(json.dumps(dict(event='actual_physical_window_complete',all_gates=result['all_gates'],
            unpaid_charts=[dict(cell=c['cell'],mode=r['mode']) for c in cell_rows for r in c['modes']
                          if not r['height_chart_excludes_zero']],counts=counts,
            elapsed_seconds=result['elapsed_seconds'],peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    except Exception as error:
        save(Path(str(a.out_prefix)+'-failure.json'),dict(status='Incomplete actual physical-mode window; no singularity inferred',
            error=repr(error),config=config,completed_groups=completed,cell_rows=cell_rows,counts=counts,
            elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        raise


if __name__=='__main__':main()
