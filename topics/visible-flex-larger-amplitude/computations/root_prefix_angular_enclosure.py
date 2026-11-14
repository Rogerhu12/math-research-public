#!/usr/bin/env python3
"""Continuous cylindrical-angle derivative of the finite horizontal formula.

Uses the same exact binary-input representation as root_prefix_radius_enclosure.
All angular bounds are Fourier absolute-sum inequalities, not samples. This
only certifies a positive horizontal-angle derivative and winding one, not a
vertical Jacobian, C2 seams, an exact integral profile, embedding, or reach.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import resource
import time
import numpy as np
import flint
from flint import arb,ctx
import root_prefix_radius_enclosure as radius


def from_bound(value):
    return arb(int(value['mantissa']))*arb(2)**int(value['exponent'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--snapshot',type=Path,required=True)
    p.add_argument('--radius-report',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--bits',type=int,default=96)
    args=p.parse_args();started=time.monotonic();ctx.prec=args.bits
    if args.bits<80:raise ValueError('Use at least 80-bit midpoint precision')
    rec=radius.load_json(args.input);program=radius.load_json(args.snapshot)
    report=radius.load_json(args.radius_report)
    if report['input_sha256']!=radius.sha(args.input) or report['snapshot_sha256']!=radius.sha(args.snapshot):
        raise ValueError('Radius report and actual inputs differ')
    if report['source_sha256']!=radius.sha(Path(radius.__file__)):
        raise ValueError('Rerun the radius enclosure after a helper change')
    if not report['all_horizontal_radius_lower_bounds_positive']:
        raise ValueError('The radial projection must already have a positive certificate')
    if rec['angular_chart']!='general-support-core-blend-v1' or int(rec['config'].get('base_mode',2))!=2:
        raise ValueError('Expected the successful mode-2 general-core representation')
    if rec.get('chart_transition_start',0.)!=0. or rec.get('chart_transition_end',1.)!=1.:
        raise ValueError('Expected the full-length quintic blend')
    chunks=[];next_state=0
    for item in rec['pp_coefficient_chunks']:
        path=args.input.parent/item['file']
        if Path(item['file']).name!=item['file'] or radius.sha(path)!=item['sha256'] or item['state_first']!=next_state:
            raise ValueError('Coefficient chunk identity or layout differs')
        with gzip.open(path,'rb') as stream:chunk=np.load(stream,allow_pickle=False)
        if chunk.shape[2]!=item['state_last_exclusive']-next_state:
            raise ValueError('Wrong coefficient state dimension')
        chunks.append(chunk);next_state=item['state_last_exclusive']
    coefficients=np.concatenate(chunks,axis=2)
    M=int(rec['config']['modes']);mesh=rec['mesh'];q=arb(rec['gauge_amplitude'])
    if coefficients.shape!=(6,len(mesh)-1,3*M+1) or not q>0:
        raise ValueError('Unexpected quintic layout or gauge')
    ref=rec['chart_reference_coefficients'];freq=rec['chart_reference_frequencies']
    A=sum((abs(arb(c))*abs(1-n*n)/n for n,c in zip(freq,ref)),arb(0)).upper()
    H=sum((abs(arb(c)) for c in ref),arb(0)).upper()
    Hp=sum((n*abs(arb(c)) for n,c in zip(freq,ref)),arb(0)).upper()
    Ap=sum((abs(1-n*n)*abs(arb(c)) for n,c in zip(freq,ref)),arb(0)).upper()
    rho_min=(1-Ap).lower();rho_max=(1+Ap).upper()
    if not rho_min>0:raise ValueError('Positive frozen reference curvature radius is needed')
    gu=list(map(arb,program['quadrature']['nodes']));gw=list(map(arb,program['quadrature']['weights']))
    length=arb(rec['meridian_length']);rows=[];worst=None
    for old in report['intervals']:
        i,j=old['interval'],old['segment'];seg=program['segments'][j]
        a=Fraction.from_float(seg['offset'])+Fraction.from_float(seg['s0'])
        b=Fraction.from_float(seg['offset'])+Fraction.from_float(seg['s1'])
        lo=max(Fraction.from_float(mesh[i]),a-Fraction(1,10**12))
        hi=min(Fraction.from_float(mesh[i+1]),b+Fraction(1,10**12))
        if lo>hi:raise ValueError('Radius-report partition changed')
        S=radius.interval(arb(str(lo)),arb(str(hi)));t=S-arb(mesh[i])
        aa=radius.radius_program(seg,S,gu,gw);amin=aa.lower();amax=aa.upper()
        x=radius.clipped(arb(str(lo))/length)
        B=(1-x**3*(10-15*x+6*x*x)).upper()
        B=arb(1) if B>1 else arb(0) if B<0 else B
        cmin=(B*A).cos().lower();smax=(B*A).sin().upper()
        material_min=(1-B*Ap).lower();material_max=(1+B*Ap).upper()
        base_w=min((cmin*material_min).lower(),((1-B)*cmin*material_min+B*rho_min).lower())
        values=[]
        for state in range(2*M+1):
            v=arb(float(coefficients[0,i,state]))
            for k in range(1,6):v=v*t+arb(float(coefficients[k,i,state]))
            values.append(v)
        r=values[:M+1];tt=values[M+1:]
        rabs=sum((v.abs_upper() for v in r),arb(0)).upper()
        rlow=(r[0].lower()-sum((v.abs_upper() for v in r[1:]),arb(0))).lower()
        tabs=sum((v.abs_upper() for v in tt),arb(0)).upper()
        dr=sum((2*(k+1)*v.abs_upper() for k,v in enumerate(r[1:])),arb(0)).upper()
        dt=sum((2*(k+1)*v.abs_upper() for k,v in enumerate(tt)),arb(0)).upper()
        # Z=e^(i eta)(U+iV), Z_eta=e^(i eta)(P+iW).
        ulo=from_bound(old['horizontal_radius_lower'])
        uabs=(amax*(1+B*H)+q*rabs).upper()
        vabs=(amax*(smax+B*Hp)+q*tabs).upper()
        wlo=(amin*base_w+q*(rlow-dt)).lower()
        pabs=(amax*smax*material_max+q*(dr+tabs)).upper()
        product=(ulo*wlo).lower() if wlo>=0 else (uabs*wlo).lower()
        determinant=(product-vabs*pabs).lower()
        radius2=(uabs*uabs+vabs*vabs).upper()
        denominator=radius2 if determinant>=0 else (ulo*ulo).lower()
        beta_eta=(determinant/denominator).lower()
        beta_theta=(beta_eta/(material_max if beta_eta>=0 else material_min)).lower()
        row=dict(interval=i,segment=j,kind=seg['kind'],positive=bool(determinant>0),
            radial_projection_lower=radius.binary_bound(ulo),
            tangential_derivative_lower=radius.binary_bound(wlo),
            angular_determinant_lower=radius.binary_bound(determinant),
            horizontal_radius_squared_upper=radius.binary_bound(radius2,False),
            beta_eta_lower=radius.binary_bound(beta_eta),beta_theta_lower=radius.binary_bound(beta_theta))
        rows.append(row)
        if worst is None or beta_theta<worst[0]:worst=(beta_theta,row)
    out=dict(scope=__doc__,input_sha256=radius.sha(args.input),snapshot_sha256=radius.sha(args.snapshot),
        radius_report_sha256=radius.sha(args.radius_report),radius_helper_sha256=radius.sha(Path(radius.__file__)),
        source_sha256=radius.sha(Path(__file__)),python_flint_version=flint.__version__,arb_precision_bits=args.bits,
        covered_quintic_intervals=report['covered_quintic_intervals'],piece_intersections=len(rows),
        all_angular_determinants_positive=all(row['positive'] for row in rows),
        reference_curvature_radius_lower=radius.binary_bound(rho_min),worst=worst[1],intervals=rows,
        winding_one_reason='Positive radial projection gives a continuous argument lift eta+atan(V/U), with periodic atan(V/U).',
        seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=(json.dumps(out,indent=2)+'\n').encode()
    if len(raw)>1_000_000 and args.out.suffix!='.gz':raise ValueError('Compress reports over 1 MB')
    if args.out.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    if len(raw)>=5_000_000:raise ValueError('Output exceeds repository file cap')
    args.out.write_bytes(raw)
    print(json.dumps(dict(output=str(args.out),seconds=out['seconds'],peak_RSS_KiB=out['peak_RSS_KiB'],
        all_positive=out['all_angular_determinants_positive'],worst=out['worst'])),flush=True)


if __name__=='__main__':main()
