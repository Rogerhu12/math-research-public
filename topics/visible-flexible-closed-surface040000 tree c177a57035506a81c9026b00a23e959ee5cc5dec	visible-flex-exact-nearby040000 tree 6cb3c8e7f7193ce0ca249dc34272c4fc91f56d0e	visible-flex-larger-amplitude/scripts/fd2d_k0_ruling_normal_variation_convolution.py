#!/usr/bin/env python3
"""Strict all-angle normal variation along every saved R137 ruling.

Clear n denominators before exact finite Laurent convolution:
fnum=(G cross X_phi).G_phi = det(A,X_phi,A_phi)/n^2,
A=n e1-m e2.  This pays the actual nondevelopability instead of dropping it.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
import flint
from flint import arb,acb,ctx
from fd2d_k0_ruling_metric_convolution import Laurent,dot,digest,load,from_bounds,magnitude_upper
from fd2d_k0_ruling_angular_certificate import moment,bounds


def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]


def exact_inlet_polynomials(path):
    saved=np.load(path,allow_pickle=False);raw=saved['frame_fourier'][:,:9];nyquist=len(raw)-1;fields=[]
    for q in range(9):
        cs={0:acb(arb(float(raw[0,q].real)))}
        for j in range(1,nyquist):
            re,im=arb(float(raw[j,q].real)),arb(float(raw[j,q].imag));cs[j]=acb(re,im);cs[-j]=acb(re,-im)
        edge=arb(float(raw[-1,q].real))/2;cs[nyquist]=acb(edge);cs[-nyquist]=acb(edge)
        fields.append(Laurent.coefficients(cs))
    nc={0:acb(arb(float(saved['n_phi_cos'][0])))};mc={0:acb(0)}
    for f,c in zip(saved['frequencies'][1:],saved['n_phi_cos'][1:]):
        nc[int(f)]=acb(arb(float(c))/2);nc[-int(f)]=acb(arb(float(c))/2)
    for f,c in zip(saved['frequencies'][1:],saved['m_phi_sin']):
        mc[int(f)]=acb(0,-arb(float(c))/2);mc[-int(f)]=acb(0,arb(float(c))/2)
    return fields[:3],fields[3:6],fields[6:9],Laurent.coefficients(nc),Laurent.coefficients(mc)


def main():
    root=Path(__file__).resolve().parent.parent;ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--metric',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-metric-convolution-01.json')
    ap.add_argument('--ruling',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-angular-certificate-01.json')
    ap.add_argument('--moments',type=Path,default=root/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json')
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();ctx.prec=192
    metric,ruling,mom=load(args.metric),load(args.ruling),load(args.moments)
    for packet in (metric,ruling):
        if packet['inlet_sha256']!=digest(args.inlet) or not packet['passed']:raise ValueError('Mismatched or incomplete actual input')
    if ruling['moments_sha256']!=digest(args.moments):raise ValueError('Moment mismatch')
    X,e1,e2,n,m=exact_inlet_polynomials(args.inlet)
    A=[n*x-m*y for x,y in zip(e1,e2)];Xp=[x.derivative() for x in X];Ap=[x.derivative() for x in A]
    determinant=dot(cross(A,Xp),Ap);P=determinant.norm_upper()
    H=from_bounds(metric['frame_Gram_operator_error_upper']).upper()
    C=from_bounds(metric['C_vector_upper']).upper();B=from_bounds(metric['B_vector_upper']).upper()
    a=from_bounds(ruling['a']);a0=moment(mom['enclosures']['a0']);length=from_bounds(ruling['coast_length']).upper()
    rows=[];maximum=arb(0);minimum_area=None
    for row in ruling['boxes']:
        nlo=from_bounds(row['n']).lower();hlo=(from_bounds(row['rho']).lower()/a0.upper()).lower()
        Dlo=min(a.lower(),from_bounds(row['D_end']).lower());s0hi=from_bounds(row['kappa_entry']).upper()
        G=((1+H)*s0hi/nlo).sqrt().upper();d=(C+length/nlo*B).upper()
        area_lower=(hlo*Dlo*(1-H)-G*d).lower()
        if not area_lower>0:raise ValueError('Whole-ruling area lower bound did not close')
        f=(P/(nlo*nlo)).upper()
        eps=(length*G*f/(area_lower*area_lower)).upper()
        maximum=max(maximum,eps);minimum_area=area_lower if minimum_area is None else min(minimum_area,area_lower)
        rows.append(dict(quarter_left=row['left_pi_over_two'],quarter_right=row['right_pi_over_two'],
            whole_ruling_area_lower=bounds(area_lower),G_norm_upper=bounds(G),fnum_abs_upper=bounds(f),normal_variation_upper=bounds(eps)))
    report=dict(schema='fd2d-actual-ruling-normal-variation-convolution-v1',actual_execution=True,
        source_sha256=digest(__file__),laurent_helper_sha256=digest(Path(__file__).with_name('fd2d_k0_ruling_metric_convolution.py')),
        inlet_sha256=digest(args.inlet),metric_sha256=digest(args.metric),ruling_sha256=digest(args.ruling),moments_sha256=digest(args.moments),
        flint_version=flint.__version__,precision_bits=192,full_Laurent_products_retained=True,
        cleared_determinant_global_upper=bounds(P),whole_ruling_area_global_lower=bounds(minimum_area),
        actual_normal_variation_global_upper=bounds(maximum),
        exact_identity='N_w norm = |det(A,X_phi,A_phi)| |G| / (n^2 |G cross (X_phi+w G_phi)|^2)',
        angular_and_radial_coverage_complete=True,exact_developability_assumed=False,passed=True,boxes=rows,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),P_upper_display=float(P),normal_variation_upper_display=float(maximum),area_lower_display=float(minimum_area),seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
