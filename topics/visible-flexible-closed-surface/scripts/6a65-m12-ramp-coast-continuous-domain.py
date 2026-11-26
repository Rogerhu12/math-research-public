#!/usr/bin/env python3
"""R220 integer interval checker on an actual ramp-generated Fourier coast.

The source is the exact saved binary64 Cartesian Fourier curve, not the old
M12 middle slice. All source hashes and exact physical f0/L/v are rebound.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('ramp_coast_integer_checker',HERE/'6a65-m12-r137-continuous-domain.py')
cert=importlib.util.module_from_spec(spec);spec.loader.exec_module(cert)
I=cert.I


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def local_curve_cells(co,si,N):
    """Second-order Taylor boxes, with exact global derivative remainders.

    For 0<=r<=4, use gamma^(r)(center), gamma^(r+1)(center),
    and 1/2*eta^2*sum m^(r+2)(|a_m|+|b_m|). This is enclosure
    refinement of the same curve; all point values still use cert.sincos.
    """
    degree=len(co)-1;pi=cert.pi_interval();delta=pi/N
    trig={j:cert.sincos(pi*Q(j if j<=N else j-2*N,N)) for j in range(2*N)}
    second_bounds=[[sum((Q(m**(r+2))*(abs(co[m][d])+abs(si[m][d])) for m in range(1,degree+1)),Q(0))
                    for d in range(3)] for r in range(5)]
    terms=[]
    for r in range(6):
        out=[]
        for d in range(3):
            row=[]
            for m in range(1,degree+1):
                a,b=co[m][d]*m**r,si[m][d]*m**r
                if r%4==1:a,b=b,-a
                if r%4==2:a,b=-a,-b
                if r%4==3:a,b=-b,a
                if a or b:row.append((m,I(a),I(b)))
            out.append(row)
        terms.append(out)
    cells=[];mean=I(0);speedlo=None;qmax=I(0);rmax=I(0)
    for j in range(N):
        point=[]
        for r in range(6):
            vec=[]
            for d in range(3):
                val=I(co[0][d]) if r==0 else I(0)
                for m,a,b in terms[r][d]:
                    sn,cs=trig[(m*(2*j+1))%(2*N)];val+=a*cs+b*sn
                vec.append(val)
            point.append(vec)
        box=[]
        for r in range(5):
            vec=[]
            for d in range(3):
                absolute=point[r+1][d].absupper()
                err=cert.upper_i(delta*I.raw(absolute,absolute)+delta.square()*I(second_bounds[r][d])/2)
                vec.append(point[r][d]+I.raw(-err.hi,err.hi))
            box.append(vec)
        speed=cert.norm2(box[1]).sqrt()
        if speed.lo<=0:raise ArithmeticError('Local Taylor box did not prove positive raw speed')
        speedlo=cert.lower_i(speed) if speedlo is None else I.raw(min(speedlo.lo,speed.lo),min(speedlo.lo,speed.lo))
        qmax=cert.max_upper(qmax,cert.norm2(box[2]).sqrt());rmax=cert.max_upper(rmax,cert.norm2(box[3]).sqrt())
        mean+=cert.norm2(point[1]).sqrt()/N;cells.append(box)
    second=qmax.square()/speedlo+rmax;remainder=cert.upper_i(second*delta.square()/6)
    arc=mean+I.raw(-remainder.hi,remainder.hi)
    if arc.lo<=0:raise ArithmeticError('Arclength integral not positive')
    refined_trig={}
    def refined_box(index,count):
        halfwidth=pi/count;point=[]
        cache=refined_trig.setdefault(count,{})
        for r in range(6):
            vec=[]
            for d in range(3):
                val=I(co[0][d]) if r==0 else I(0)
                for m,a,b in terms[r][d]:
                    residue=(m*(2*index+1))%(2*count)
                    if residue not in cache:
                        numerator=residue if residue<=count else residue-2*count
                        cache[residue]=cert.sincos(pi*Q(numerator,count))
                    sn,cs=cache[residue];val+=a*cs+b*sn
                vec.append(val)
            point.append(vec)
        box=[]
        for r in range(5):
            vec=[]
            for d in range(3):
                absolute=point[r+1][d].absupper()
                err=cert.upper_i(halfwidth*I.raw(absolute,absolute)+halfwidth.square()*I(second_bounds[r][d])/2)
                vec.append(point[r][d]+I.raw(-err.hi,err.hi))
            box.append(vec)
        return box
    return cells,arc,{'pi':pi.display(),'raw_speed_lower':speedlo.display(),
                     'speed_second_derivative_bound':cert.upper_i(second).display(),
                     'midpoint_mean_speed':mean.display(),'mean_integral_remainder':remainder.display(),
                     'whole_cell_enclosure':'center derivative plus center next derivative times halfwidth, plus exact global second Taylor remainder'},refined_box


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--glue-report',type=Path,required=True);ap.add_argument('--definition',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--cells',type=int,default=2048)
    ap.add_argument('--max-depth',type=int,default=6)
    ap.add_argument('--curvature-cap',type=str,default='6')
    ap.add_argument('--denominator-floor',type=str,default='1/2')
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh output required')
    start=time.monotonic();source=json.loads(args.glue_report.read_text())
    curvature_cap=I(Q(args.curvature_cap));denominator_floor=I(Q(args.denominator_floor))
    if source['coast_definition_sha256']!=sha(args.definition):raise ValueError('Coast definition hash mismatch')
    with np.load(args.definition,allow_pickle=False) as d:half=d['positive_cartesian_coefficients'].copy()
    degree=len(half)-1
    if degree!=source['coast_raw_curve_degree']:raise ValueError('Fourier degree mismatch')
    co=[];si=[]
    for k,row in enumerate(half):
        co.append([Q.from_float(float(z.real))*(1 if k==0 else 2) for z in row])
        si.append([Q(0) if k==0 else -2*Q.from_float(float(z.imag)) for z in row])
    if any(half[0].imag):raise ValueError('Constant vector is not real')
    # The same exact finite curve; a tighter whole-cell Taylor enclosure.
    cells,arc,quadrature,refine=local_curve_cells(co,si,args.cells)
    f0=Q(source['coast_radius_exact']);length=Q(source['coast_length_exact'])
    metadata=HERE.parent/'notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json'
    meta=json.loads(metadata.read_text());v=Q(float(meta['frozen_profile']['vu']))
    cfg=meta['frozen_profile'];delta,eps=Q(float(cfg['delta'])),Q(float(cfg['ramp']))
    Tu=delta/(v*(1-eps));R=Tu*eps
    if f0!=1+v*R/2 or length!=Tu*(1-2*eps):raise ValueError('Original complete affine metric identity mismatch')
    center=[I(x) for x in co[0]];bounds={};rows=hashlib.sha256()
    leaf_count=0;depth_used=0;split_count=0
    def consume(j,count,depth,data):
        nonlocal leaf_count,depth_used,split_count
        try:
            g=cert.geometry(data,arc,I(f0),I(v),I(length),center)
            if g['nonzero_principal_curvature'].hi>=curvature_cap.lo or g['D'].lo<=denominator_floor.hi:
                raise ArithmeticError('Need sharper enclosure of the same curvature/denominator')
        except ArithmeticError as exc:
            if depth>=args.max_depth:raise ArithmeticError(f'New coast interval {j}/{count}: {exc}') from exc
            split_count+=1
            for child in (2*j,2*j+1):consume(child,2*count,depth+1,refine(child,2*count))
            return
        for key,value in g.items():bounds[key]=value if key not in bounds else cert.hull(bounds[key],value)
        rows.update(json.dumps({'index':j,'subdivisions':count,'bounds':{key:[value.lo,value.hi] for key,value in sorted(g.items())}},sort_keys=True).encode()+b'\n')
        leaf_count+=1;depth_used=max(depth_used,depth)
    for j,data in enumerate(cells):
        consume(j,args.cells,0,data)
        if (j+1)%1024==0:print(json.dumps({'coarse_covered':j+1,'coarse_total':args.cells,'proved_leaves':leaf_count,'splits':split_count}),flush=True)
    kr=I.raw(bounds['ratio'].absupper(),bounds['ratio'].absupper());ruling=cert.upper_i(I(length)*(1+kr.square()).sqrt())
    lower=cert.lower_i(bounds['nonzero_principal_curvature'])
    out={'schema':'6a65-ramp-generated-exact-coast-integer-domain-v1','script_sha256':sha(__file__),
         'checker_sha256':sha(HERE/'6a65-m12-r137-continuous-domain.py'),'glue_report_sha256':sha(args.glue_report),
         'curve_definition_sha256':sha(args.definition),'original_geometry_sha256':sha(metadata),
         'coast_degree':degree,'initial_angular_cells':args.cells,'proved_angular_leaves':leaf_count,
         'binary_splits':split_count,'maximum_subdivision_depth':depth_used,'physical_f0_exact':str(f0),
         'proved_curvature_cap':args.curvature_cap,'proved_denominator_floor':args.denominator_floor,
         'physical_length_exact':str(length),'physical_slope_exact':str(v),
         'raw_arc_radius':arc.display(),'arc_proof':quadrature,
         'whole_domain_bounds':{key:value.display() for key,value in bounds.items()},
         'ruling_length_upper':ruling.display(),
         'Green_bounds':{'C0':cert.upper_i(ruling.square()/(2*lower)).display(),'ruling_C1':cert.upper_i(ruling/lower).display(),'ruling_C2':cert.upper_i(1/lower).display()},
         'all_angle_integer_rows_sha256':rows.hexdigest(),'whole_angle_and_ruling_domain_certified':True,
         'approximate_ramp_metric_not_continuously_certified_here':True,'whole_closed_surface_constructed':False,
         'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2,allow_nan=False))


if __name__=='__main__':main()
