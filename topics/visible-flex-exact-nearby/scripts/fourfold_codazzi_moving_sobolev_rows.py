#!/usr/bin/env python3
"""Full strong moving-energy coefficients on complete actual radial rows.

Adds the true second phi derivative of the whole candidate, for the exact
three-state (energy, mean, first-derivative energy) comparison. Every field
uses complete directed trigonometric sums and its full angular Taylor fee.
"""
from __future__ import annotations
import argparse,time
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_moving_mean_energy_rows import arguments,prepare,identify
from fourfold_codazzi_moving_mean_energy_direct_rows import DirectTrigonometricSums
from fourfold_codazzi_moving_mean_energy_prefix_v2 import (
    read,target_bounds,polynomial_ranges,record,save,sha,Box,arb_box,square_box,maxabs,upper,lower)
from fourfold_codazzi_rotational_cap_jacobi import box_from_record


class StrongDirectSums(DirectTrigonometricSums):
    def __init__(self,m,angles):
        super().__init__(m,angles)
        self.columns=[(component,q) for component in (0,1) for q in range(5)]

    def fields(self,y,alpha,s):
        sincoef=np.zeros((self.m,len(self.columns)));coscoef=np.zeros_like(sincoef)
        errors=[arb(0) for _ in self.columns];dotnorm=[arb(0) for _ in self.columns];norms={}
        for component in (0,1):
            for order in range(6):
                norms[component,order]=sum((abs(alpha*y[self.m+j] if component else alpha*y[j-1])*(4*j)**order
                    for j in range(1,self.m+1)),arb(0)).upper()
        for col,(component,order) in enumerate(self.columns):
            use_sin=(order%2==1) if component else (order%2==0)
            sign=(-1)**((order+1)//2 if component else order//2);trig=1 if use_sin else 0
            for j in range(1,self.m+1):
                value=sign*(4*j)**order*alpha*(y[self.m+j] if component else y[j-1]);midpoint=float(value.mid())
                if not np.isfinite(midpoint):raise ValueError('nonfinite exact Fourier coefficient proposal')
                (sincoef if use_sin else coscoef)[j-1,col]=midpoint;mid=arb(midpoint)
                errors[col]+=abs(value-mid)+abs(mid)*arb(float(self.radius[j-1,trig]))
                dotnorm[col]+=abs(mid)*arb(float(self.mid_abs[j-1,trig]))
        values=np.zeros((self.angles,len(self.columns)))
        for j in range(self.m):
            values+=self.sin[j,:,None]*sincoef[j][None,:]+self.cos[j,:,None]*coscoef[j][None,:]
        if not np.all(np.isfinite(values)):raise ValueError('explicit strong Fourier arithmetic overflowed')
        nodes=[]
        for col,(component,order) in enumerate(self.columns):
            fee=(errors[col]+self.gamma*dotnorm[col]+self.underflow).upper();radius=arb_box(fee).hi
            box=Box(values[:,col])+Box(-radius,radius)
            if component and order==0:box+=arb_box(s+alpha*y[self.m])
            nodes.append(box)
        half=arb.pi()/(4*self.angles);h=arb_box(half);closed=[];selected=[]
        for component,order in ((0,0),(1,0),(0,1),(1,1),(1,2),(0,2)):
            col=self.columns.index((component,order));remainder=(half**3*norms[component,order+3]/6).upper()
            fee=(h*Box(nodes[col+1].abs_upper())+h*h*Box(nodes[col+2].abs_upper())/2+arb_box(remainder)).hi
            closed.append(nodes[col]+Box(-fee,fee));selected.append(nodes[col])
        return closed,selected


def derivative_budget(fields,a,base):
    u,v,ut,vt,vtt,utt=fields;D=arb_box(base['actual_D']);K=arb_box(a['K']);beta=arb_box(a['beta'])
    upp=square_box(D)*v*(vt*ut+v*utt)
    vpp=square_box(D)*v*(square_box(vt)+v*vtt)
    L2=upper(square_box(upp)-K*square_box(vpp)).sqrt().upper()
    S=square_box(u)+K*square_box(v);dphi=beta*(arb_box(base['actual_S_mean'])-S)
    G1=-beta*(1+3*square_box(u)+K*square_box(v))+dphi/2
    G2=beta*(1-square_box(u)-3*K*square_box(v))+arb_box(a['K1']/(2*a['K']))+dphi/2
    R,L=base['actual_R_upper'],base['actual_L_upper']
    return dict(actual_Q_phi_phi_energy_upper=L2,actual_v_phi_absolute=maxabs(D*v*vt),
        full_u_theta_theta_absolute=maxabs(utt),full_v_theta_theta_absolute=maxabs(vtt),
        forward_derivative_rate=max(upper(G1),upper(G2)).upper(),
        backward_derivative_rate=max(-lower(G1),-lower(G2)).upper(),
        coupling_E0_to_E1=(abs(a['beta'])*R*(10*L+L2/2)).upper(),
        coupling_mean_to_E1=(a['gamma']*(-a['K']).sqrt()*L2).upper())


def main():
    ap=arguments(argparse.ArgumentParser(description=__doc__))
    ap.add_argument('--energy',type=Path,default=Path('notes/2026-11-13-R133-moving-mean-energy-alpha075-r0238-complete-native.json.gz'))
    ap.add_argument('--first-row',type=int,required=True);ap.add_argument('--row-count',type=int,default=382)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve every actual strong-energy part')
    c=prepare(args);base=read(args.energy)
    if (not base['complete'] or base['kind']!='actual_complete_moving_mean_energy_from_saved_rows_and_parts'
        or base['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_moving_mean_energy_complete.py'))
        or any(base['inputs'].get(k)!=v for k,v in c['header']['inputs'].items())
        or base['candidate_metadata']!=c['meta'] or base['closed_angular_cells']!=c['angles']
        or len(base['rows'])!=c['header']['total_common_partition_rows']):
        raise ValueError('the same complete real zero-order energy certificate is required')
    first=args.first_row;last=min(len(base['rows']),first+args.row_count)
    if not 0<=first<last<=len(base['rows']):raise ValueError('the requested strong row range is invalid')
    sampler=StrongDirectSums(c['m'],c['angles'])
    doc=dict(c['header'],kind='actual_complete_moving_H1_coefficient_row_part',complete=False,
        source_sha256=sha(__file__),inputs={**c['header']['inputs'],str(args.energy):sha(args.energy)},
        first_common_row=first,last_common_row_exclusive=last,
        exact_requested_subinterval=list(map(str,(c['cuts'][first],c['cuts'][last]))),rows=[],failure=None,
        direct_arithmetic_source_sha256=sha(Path(__file__).with_name('fourfold_codazzi_moving_mean_energy_direct_rows.py')),
        full_candidate_fifth_angular_derivative_Taylor_fee_paid=True,ordinary_source_mean_not_deleted=True)
    checkpoint=time.monotonic()
    try:
        for index in range(first,last):
            left,right,j,k,row=identify(c,index);original=base['rows'][index]
            if (original['interval']!=list(map(str,(left,right))) or original['candidate_piece']!=j
                or original['native_row']!=k or original['actual_scalar_germ']!=row['actual_scalar_germ']):
                raise ValueError('the complete original zero-order row identity changed')
            a=target_bounds(row,left,right,c['nu'])
            if original['actual_target']!={name:record(a[name]) for name in ('gamma','beta','K','K1')}:
                raise ValueError('the actual target changed')
            y,_=polynomial_ranges(c['saved'],c['nodes'],j,left,right)
            fields,_=sampler.fields(y,c['alpha'],a['s'])
            b={name:box_from_record(value) for name,value in original['bounds'].items()}
            extra=derivative_budget(fields,a,b)
            doc['rows'].append(dict(common_row=index,interval=list(map(str,(left,right))),
                candidate_piece=j,native_row=k,bounds={name:record(value) for name,value in extra.items()}))
            if time.monotonic()-checkpoint>20:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(common_row=index,completed=len(doc['rows']),planned=last-first,L2=extra['actual_Q_phi_phi_energy_upper'].str(10)),flush=True)
                checkpoint=time.monotonic()
        doc.update(complete=True,whole_requested_radial_subinterval=True)
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],first=first,last=last,rows=len(doc['rows']),wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
