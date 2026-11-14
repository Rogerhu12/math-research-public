# v1 source SHA256 233db335814628f447a90f4ae82d1e1f07d26e49dc3e7401337d9c48e9c30dbe
#!/usr/bin/env python3
"""Refine only the cell12/13 diagonal Green kernels, keeping all 46 heights.

Far-admissible phi and cut-zero psi are propagated with signed panel flows.
The Green products retain the radial order phi(inner)*psi(outer).  Original
off-diagonal cell bounds are kept.  No equation, metric, or boundary changes.
Version2 also exports true panelwise full-cell phi/psi majorants for off-diagonal use.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb,ctx
from closure_real_head_source_enclosure import RealHead,exact_q,power2,ball_record
from closure_real_linear_head_enclosure import PositiveKernels,ideal_slope,peano_matrix,interval
from closure_real_head_green_enclosure import (load_json,ball,endpoint,mat,mv,
    inverse_unimodular,ceil_log2_upper,maximum)
from closure_projective_interval_column import ProjectiveColumn


def abs_upper(x):return abs(x).upper()


def smaller(a,b):
    # Both arguments are certified nonnegative upper bounds.
    return min(a.upper(),b.upper())


def prepare_panels(head):
    kernels=PositiveKernels(head,225,92);out={};count=0
    for n in (13,12):
        panels=[]
        for j in range(9):
            for lo,hi,kernel in kernels.panels(n,j,power2(-20)):
                panels.append(dict(segment=j,left=lo,right=hi,kernel=kernel))
        out[n]=panels;count+=len(panels)
        kernels.release_cell(n)
        print(json.dumps(dict(event='material_panels',cell=n,panels=len(panels),
            RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    return kernels,out,count


def ordered_kernel(phi,psi,m):
    q_prefix=arb(0);xi_prefix=arb(0);Qmax=arb(0);Ximax=arb(0)
    q_witness=None;xi_witness=None
    for i,(ph,ps) in enumerate(zip(phi,psi)):
        q_prefix=maximum(q_prefix,ph[0]);xi_prefix=maximum(xi_prefix,ph[1])
        q=q_prefix*ps[0]
        xi=maximum(xi_prefix*ps[0],q_prefix*ps[1])
        if q>Qmax:q_witness=i
        if xi>Ximax:xi_witness=i
        Qmax=maximum(Qmax,q);Ximax=maximum(Ximax,xi)
    return ((1+m)**3*Qmax+(1+m)*Ximax,
        dict(Q_kernel=ball_record(Qmax),Xi_kernel=ball_record(Ximax),
             Q_outer_panel=q_witness,Xi_outer_panel=xi_witness))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--columns',required=True,type=Path)
    p.add_argument('--green',required=True,type=Path)
    p.add_argument('--ready',required=True,type=Path)
    p.add_argument('--out-prefix',required=True,type=Path)
    p.add_argument('--relative-radius',default='1/100')
    p.add_argument('--precision',type=int,default=192)
    args=p.parse_args();ctx.prec=args.precision;started=time.monotonic()
    data,raw=load_json(args.columns);old,old_raw=load_json(args.green)
    ready,ready_raw=load_json(args.ready)
    if data['modes']!=list(range(2,93,2)) or old['modes']!=data['modes']:
        raise ValueError('This refinement keeps exactly all original low46 modes')
    if hashlib.sha256(raw).hexdigest()!=old['input_hashes'].get(str(args.columns)):
        raise ValueError('Green and linear data differ')
    if hashlib.sha256(ready_raw).hexdigest() not in data['input_hashes'].values():
        raise ValueError('Source ready does not match columns')
    head=RealHead(ready,start=12,far=159,exact_through=23)
    kernels,panels,panel_count=prepare_panels(head)
    gamma=[list(row) for row in old['gamma_log2_upper']]
    refined={12:None,13:None};mode_rows=[];group_hashes={}
    for group_ref in data['column_groups']:
        path=Path(group_ref['path']);group,graw=load_json(path)
        digest=hashlib.sha256(graw).hexdigest()
        if digest!=group_ref['sha256']:raise ValueError('Column group hash differs')
        group_hashes[str(path)]=digest
        rows=group['cell_rows'];by_cell={r['cell']:r for r in rows}
        for col,m in enumerate(group['modes']):
            u=m*m-4;nu=arb(m*m*(m*m-1))/12
            gain=group['endpoint_rows'][col]['Q_gain']
            glo=endpoint(gain['lower']);ghi=endpoint(gain['upper'])
            if not(glo>0 or ghi<0):raise ArithmeticError('Height chart not paid')
            gain_lower=glo if glo>0 else -ghi
            rfar=ball(rows[-1]['r_inner']);scale=(rfar/head.rc)**u
            slope=ideal_slope(m,head.rho)+interval(-nu*power2(-60),nu*power2(-60))
            phi=ProjectiveColumn([1/scale,scale*slope])
            for n in range(224,13,-1):
                if n<224:phi.multiply_component(1,1/head.rho)
                phi.advance(mat(by_cell[n]['linear_rows'][col]['gauge_matrix']))
            phi_bounds={};flow={};old_caps={}
            for n in (13,12):
                phi.multiply_component(1,1/head.rho)
                bound=[];mats=[];lin=by_cell[n]['linear_rows'][col]
                capQ=ball(lin['column_Q_sup']).upper()/gain_lower
                capXi=ball(lin['column_Xi_sup']).upper()/gain_lower
                old_caps[n]=(capQ,capXi)
                for panel in panels[n]:
                    A,B=kernels.mode_integrals(panel['kernel'],m)
                    T,major,_=peano_matrix(A,B)
                    within=mv(major,phi.absolute_uppers())
                    r=panel['kernel']['r']
                    q=abs_upper((r/head.rc)**u)*within[0]/gain_lower
                    xi=abs_upper((head.rc/r)**u)*within[1]/gain_lower
                    # Intersect two independent valid majorants of this
                    # same actual column; no dependence is discarded.
                    bound.append((smaller(q,capQ),smaller(xi,capXi)))
                    mats.append((T,major));phi.advance(T)
                phi_bounds[n]=bound;flow[n]=mats
            cut_r=ball(rows[0]['r_outer'])
            psi=ProjectiveColumn([arb(0),(cut_r/head.rc)**u])
            psi_bounds={}
            for n in (12,13):
                if n>12:psi.multiply_component(1,head.rho)
                bound=[None]*len(panels[n])
                for i in range(len(panels[n])-1,-1,-1):
                    T,major=flow[n][i];r=panels[n][i]['kernel']['r']
                    within=mv(major,psi.absolute_uppers())
                    bound[i]=(abs_upper((r/head.rc)**u)*within[0],
                        abs_upper((head.rc/r)**u)*within[1])
                    psi.advance(inverse_unimodular(T))
                psi_bounds[n]=bound
            entries=[]
            for n in (12,13):
                value,witness=ordered_kernel(phi_bounds[n],psi_bounds[n],m)
                value*=ball(by_cell[n]['mu'])/ball(by_cell[12]['mu'])
                exponent=ceil_log2_upper(value)
                refined[n]=exponent if refined[n] is None else max(refined[n],exponent)
                entries.append(dict(cell=n,kernel_log2_upper=exponent,
                    kernel_bound=ball_record(value),component_kernel=witness,
                    refined_phi_Q_sup=ball_record(max(x[0].upper() for x in phi_bounds[n])),
                    refined_phi_Xi_sup=ball_record(max(x[1].upper() for x in phi_bounds[n])),
                    refined_psi_Q_sup=ball_record(max(x[0].upper() for x in psi_bounds[n])),
                    refined_psi_Xi_sup=ball_record(max(x[1].upper() for x in psi_bounds[n])),
                    old_full_cell_phi_Q=ball_record(old_caps[n][0]),
                    old_full_cell_phi_Xi=ball_record(old_caps[n][1])))
            mode_rows.append(dict(mode=m,refined_cells=entries))
        print(json.dumps(dict(event='column_group',modes=group['modes'],
            refined_diagonals=refined,seconds=time.monotonic()-started,
            RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    for n,e in refined.items():gamma[n-12][n-12]=min(gamma[n-12][n-12],e)
    eta=arb(0);response=[]
    for k,row in enumerate(data['cell_rows']):
        x=ball(row['whole_cell_reference_X']).upper()
        value=sum((power2(gamma[k][n])*ball(src['complete_source_L1_bound']).upper()
            for n,src in enumerate(data['cell_rows'])),arb(0))
        ratio=value/x;eta=maximum(eta,ratio)
        response.append(dict(cell=row['cell'],reference_X=ball_record(x),
            source_response_bound=ball_record(value),relative_response=ball_record(ratio)))
    r=exact_q(Q(args.relative_radius));mapping=eta*(1+r)**2;lip=4*eta*(1+r)
    small=all((1+r)*ball(row['relative_to_R23_radius']).upper()<1 for row in data['cell_rows'])
    result=dict(status='Validated ordered-panel low46 Green refinement; original metric and all shallow heights preserved',
        modes=data['modes'],tau=data['tau'],refined_cells=[12,13],material_panel_count=panel_count,
        refined_diagonal_exponents=refined,mode_rows=mode_rows,
        gamma_log2_upper=gamma,response_rows=response,
        maximum_relative_response=ball_record(eta),
        projected_fixed_point=dict(relative_radius=str(Q(args.relative_radius)),
            mapping_bound=ball_record(mapping),contraction_bound=ball_record(lip),
            all_R23_balls_paid=small,gate_paid=bool(small and mapping<r and lip<1)),
        input_hashes={str(args.columns):hashlib.sha256(raw).hexdigest(),
            str(args.green):hashlib.sha256(old_raw).hexdigest(),str(args.ready):hashlib.sha256(ready_raw).hexdigest(),**group_hashes},
        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in
            ['closure_ordered_cell_green_v2.py','closure_real_linear_head_enclosure.py','closure_real_head_green_enclosure.py',
             'closure_projective_interval_column.py','closure_real_head_source_enclosure.py']},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['The full pointwise source is projected only at output into low46 in this auxiliary nonlinear problem.',
            'The exact linear far subspaces and original fixed shallow low heights are retained; nonlinear R18 far trace is not yet coupled.',
            'The kernel here has constant strip1. A varying-strip or R33 physical-density feedback needs its own estimate.',
            'Ordered panel products bound the two component suprema separately; no simultaneous-maximizer assumption is made.'])
    out=Path(str(args.out_prefix)+'.json.gz');encoded=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(encoded)>=5_000_000:raise ArithmeticError('Repository file cap exceeded')
    out.write_bytes(encoded)
    summary={k:v for k,v in result.items() if k not in ['gamma_log2_upper','response_rows','mode_rows','input_hashes']}
    summary.update(first_responses=response[:3],output=str(out),output_sha256=hashlib.sha256(encoded).hexdigest())
    Path(str(args.out_prefix)+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',refined=refined,eta=str(eta),gate=result['projected_fixed_point']['gate_paid'],
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
