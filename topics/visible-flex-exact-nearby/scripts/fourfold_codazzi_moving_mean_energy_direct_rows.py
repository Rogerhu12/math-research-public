#!/usr/bin/env python3
"""Actual moving-energy rows with explicitly rounded direct Fourier sums.

Each true trigonometric root is enclosed by Arb, all powers by directed
interval multiplication. The only ordinary floating sums have exactly
four operations per physical frequency, with their complete forward error
and underflow fee paid. No FFT error assumption or sampled-circle gate is
used. Third-order angular Taylor remainders cover every closed angle cell.
"""
from __future__ import annotations
import argparse,time
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_moving_mean_energy_rows import arguments,prepare,identify
from fourfold_codazzi_moving_mean_energy_prefix_v2 import (
    target_bounds,polynomial_ranges,row_coefficients,record,save,sha,
    Box,CBox,arb_box,exact_arb)
from fourfold_phase_uniform_tail import up,down


class DirectTrigonometricSums:
    def __init__(self,m,angles):
        self.m=m;self.angles=angles
        tiny=np.nextafter(np.float64(0),np.float64(1))
        if not tiny>0 or np.multiply(tiny,1.)!=tiny or np.add(tiny,tiny)!=2*tiny:
            raise ValueError('the explicit gradual-underflow arithmetic model is unavailable')
        rr=np.empty(angles);rh=np.empty(angles);ii=np.empty(angles);ih=np.empty(angles)
        for k in range(angles):
            theta=2*arb.pi()*k/angles
            c=arb_box(theta.cos());s=arb_box(theta.sin())
            rr[k],rh[k],ii[k],ih[k]=float(c.lo),float(c.hi),float(s.lo),float(s.hi)
        roots=CBox(Box(rr,rh),Box(ii,ih));power=CBox(1.)
        self.cos=np.empty((m,angles));self.sin=np.empty((m,angles))
        self.radius=np.empty((m,2));self.mid_abs=np.empty((m,2))
        for j in range(m):
            power=power*roots
            for col,part in enumerate((power.real,power.imag)):
                lo=np.maximum(part.lo,-1.);hi=np.minimum(part.hi,1.)
                if not np.all(lo<=hi):raise ValueError('a complete real trigonometric root interval is inconsistent')
                mid=lo/2+hi/2
                radius=up(np.maximum(up(np.abs(mid-lo)),up(np.abs(hi-mid))))
                (self.cos if col==0 else self.sin)[j]=mid
                self.radius[j,col]=np.max(radius);self.mid_abs[j,col]=np.max(np.abs(mid))
        # A unit roundoff of 2^-52 is deliberately wider than nearest-mode
        # binary64. Exactly two products and two sums occur per frequency.
        self.operations=4*m;unit=arb(2)**(-52)
        self.gamma=self.operations*unit/(1-self.operations*unit)
        self.underflow=self.operations*arb(2)**(-1074)/(1-self.operations*unit)
        self.columns=[(0,q) for q in range(4)]+[(1,q) for q in range(5)]

    def fields(self,y,alpha,s):
        sincoef=np.zeros((self.m,len(self.columns)));coscoef=np.zeros_like(sincoef)
        errors=[arb(0) for _ in self.columns];dotnorm=[arb(0) for _ in self.columns]
        norms={}
        for component in (0,1):
            for order in range(5 if component==0 else 6):
                norms[component,order]=sum((abs(alpha*y[self.m+j] if component else alpha*y[j-1])*(4*j)**order
                    for j in range(1,self.m+1)),arb(0)).upper()
        for col,(component,order) in enumerate(self.columns):
            use_sin=(order%2==1) if component else (order%2==0)
            sign=(-1)**((order+1)//2 if component else order//2)
            trig=1 if use_sin else 0
            for j in range(1,self.m+1):
                value=sign*(4*j)**order*alpha*(y[self.m+j] if component else y[j-1])
                midpoint=float(value.mid())
                if not np.isfinite(midpoint):raise ValueError('a true Fourier coefficient cannot be represented finitely')
                (sincoef if use_sin else coscoef)[j-1,col]=midpoint
                mid=arb(midpoint)
                errors[col]+=abs(value-mid)+abs(mid)*arb(float(self.radius[j-1,trig]))
                dotnorm[col]+=abs(mid)*arb(float(self.mid_abs[j-1,trig]))
        values=np.zeros((self.angles,len(self.columns)))
        for j in range(self.m):
            # The operation count and its arithmetic proof correspond to
            # these two multiplications, one inner sum, one accumulation.
            term=self.sin[j,:,None]*sincoef[j][None,:]+self.cos[j,:,None]*coscoef[j][None,:]
            values+=term
        if not np.all(np.isfinite(values)):raise ValueError('ordinary direct Fourier arithmetic overflowed')
        nodes=[]
        for col,(component,order) in enumerate(self.columns):
            fee=(errors[col]+self.gamma*dotnorm[col]+self.underflow).upper()
            radius=arb_box(fee).hi
            box=Box(values[:,col])+Box(-radius,radius)
            if component and order==0:box=box+arb_box(s+alpha*y[self.m])
            nodes.append(box)
        half=arb.pi()/(4*self.angles);h=arb_box(half);closed=[];selected=[]
        for component,order in ((0,0),(1,0),(0,1),(1,1),(1,2)):
            col=self.columns.index((component,order))
            remainder=(half**3*norms[component,order+3]/6).upper()
            fee=(h*Box(nodes[col+1].abs_upper())+h*h*Box(nodes[col+2].abs_upper())/2+arb_box(remainder)).hi
            closed.append(nodes[col]+Box(-fee,fee));selected.append(nodes[col])
        return closed,selected


def main():
    ap=arguments(argparse.ArgumentParser(description=__doc__))
    ap.add_argument('--first-row',type=int,required=True);ap.add_argument('--row-count',type=int,default=150)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve each actual direct-sum row part')
    c=prepare(args);total=c['header']['total_common_partition_rows']
    first=args.first_row;last=min(total,first+args.row_count)
    if not 0<=first<last<=total:raise ValueError('the requested complete-row range is invalid')
    sampler=DirectTrigonometricSums(c['m'],c['angles'])
    doc=dict(c['header'],kind='actual_moving_mean_energy_direct_complete_row_part',complete=False,
        source_sha256=sha(__file__),first_common_row=first,last_common_row_exclusive=last,
        exact_requested_subinterval=list(map(str,(c['cuts'][first],c['cuts'][last]))),
        whole_body_interval_claimed=False,rows=[],failure=None,
        arithmetic=dict(trigonometric_roots='320-bit Arb; directed complex powers; exact dyadic midpoints',
            explicit_binary64_operations_per_node=sampler.operations,
            complete_relative_roundoff_factor=record(sampler.gamma),
            complete_absolute_underflow_fee=record(sampler.underflow),
            actual_coefficient_uncertainty_and_every_trigonometric_power_error_paid=True,
            no_floating_FFT_error_assumption=True,full_closed_angle_third_Taylor_remainder=True),
        row_partition_source_sha256=sha(Path(__file__).with_name('fourfold_codazzi_moving_mean_energy_rows.py')))
    checkpoint=time.monotonic()
    try:
        for index in range(first,last):
            left,right,j,k,row=identify(c,index);a=target_bounds(row,left,right,c['nu'])
            y,_=polynomial_ranges(c['saved'],c['nodes'],j,left,right)
            fields,nodes=sampler.fields(y,c['alpha'],a['s']);b=row_coefficients(fields,nodes,a,c['angles'])
            doc['rows'].append(dict(common_row=index,interval=[str(left),str(right)],candidate_piece=j,native_row=k,
                actual_scalar_germ=row['actual_scalar_germ'],
                actual_target={name:record(a[name]) for name in ('gamma','beta','K','K1')},
                bounds={name:record(value) for name,value in b.items()}))
            if time.monotonic()-checkpoint>20:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(common_row=index,completed=len(doc['rows']),planned=last-first,right=str(right)),flush=True)
                checkpoint=time.monotonic()
        doc.update(complete=True,whole_requested_radial_subinterval=True)
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],first=first,last=last,rows=len(doc['rows']),
        total=total,wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
