#!/usr/bin/env python3
"""Continuous angular n/D bounds for the explicitly frozen R137 inlet.

Uses Arb balls, the actual finite binary Fourier n,m, and the already
certified exact balanced-chart moments.  It certifies the ruling coordinate
map for this finite inlet, not exact inlet Gauss-Codazzi compatibility.
Rank-one curvature bounds are explicitly conditional on that compatibility.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
import flint
from flint import arb,ctx


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dyadic(row):
    sign,m,e,bits=map(int,row)
    return arb((-m if sign else m,e))
def moment(row):return dyadic(row['binary_lower']).union(dyadic(row['binary_upper']))
def binary(x):
    m,e=x.man_exp();return [str(m),int(e)]
def bounds(x):
    return dict(lower_binary=binary(x.lower()),upper_binary=binary(x.upper()),
        lower_display=float(x.lower()),upper_display=float(x.upper()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    root=Path(__file__).resolve().parent.parent
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--candidate',type=Path,default=root/'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json')
    ap.add_argument('--moments',type=Path,default=root/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json')
    ap.add_argument('--initial-boxes',type=int,default=128)
    ap.add_argument('--maximum-depth',type=int,default=7)
    ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();ctx.prec=args.precision
    p=np.load(args.inlet,allow_pickle=False);candidate=json.loads(args.candidate.read_text())
    if str(p['candidate_sha256'].item())!=digest(args.candidate):raise ValueError('Candidate binding mismatch')
    mom=json.loads(args.moments.read_text());par=mom['parameters']
    ref_a0=moment(mom['enclosures']['a0'])
    adjust={key:moment(mom['enclosures'][key]) for key in ('u0','u2','u4')}
    r0,D0,c0,K0=(arb(par[k]) for k in ('r','D','c','k'))
    raw=candidate['segments'];last=next(q for q in reversed(raw) if q['kind']=='hermite')
    # Cover both the true shared-jet radius and the stored numerical radius.
    a=(ref_a0+arb(float(last['jet1'][0]))).union(arb(float(p['a'])))
    v=arb(float(last['jet1'][1])).union(arb(float(p['v'])))
    L=arb(float(p['coast_length']));rho0=a/v
    nc=[arb(float(x)) for x in p['n_phi_cos']]
    mc=[arb(float(x)) for x in p['m_phi_sin']]
    freq=[int(x) for x in p['frequencies']]
    if freq!=list(range(0,2*len(freq),2)):raise ValueError('Expected the actual even D2 basis')
    pi=arb.pi();records=[];unresolved=[];calls=0

    def evaluate(left,right):
        nonlocal calls
        calls+=1;phi=(pi*left/2).union(pi*right/2)
        n=nc[0];m=arb(0);np1=arb(0);mp1=arb(0)
        for j,f in enumerate(freq[1:],1):
            sn,cs=(phi*f).sin_cos()
            n+=nc[j]*cs;m+=mc[j-1]*sn
            np1-=f*nc[j]*sn;mp1+=f*mc[j-1]*cs
        c2=(2*phi).cos();c4=(4*phi).cos()
        rho=r0+D0*(1-(K0*(c2-c0)).tanh())/2+adjust['u0']+adjust['u2']*c2+adjust['u4']*c4
        h=rho/ref_a0
        if not (n>0 and h>0):return None
        k=m/n;ku=(mp1*n-m*np1)/(h*n*n)
        B=v*(1+k*k)-ku
        W=L*(2*rho0+L)/(rho0+(rho0*rho0+(1+k*k)*L*(2*rho0+L)).sqrt())
        D=a+W*B
        if not D>0:return None
        kap0=n*(1+k*k);kap1=a*n*(1+k*k)/D
        # A useful true target margin, not a claim that exact compatibility
        # has been established for this approximate input frame.
        if not (kap0<arb(125)/17 and kap1<arb(125)/17):return None
        return dict(n=n,rho=rho,B=B,D_end=D,kappa_entry=kap0,kappa_end=kap1)

    def visit(i,j,denominator,depth):
        left=arb(i)/denominator;right=arb(j)/denominator
        value=evaluate(left,right)
        if value is None:
            if depth>=args.maximum_depth:
                unresolved.append(dict(left=[i,denominator],right=[j,denominator],depth=depth));return
            visit(2*i,i+j,2*denominator,depth+1);visit(i+j,2*j,2*denominator,depth+1);return
        records.append(dict(left_pi_over_two=[i,denominator],right_pi_over_two=[j,denominator],
            depth=depth,**{k:bounds(v) for k,v in value.items()}))
    for i in range(args.initial_boxes):visit(i,i+1,args.initial_boxes,0)
    passed=not unresolved
    minima={k:min((row[k]['lower_display'] for row in records),default=None) for k in ('n','rho','D_end')}
    maximum_kappa=max((max(row['kappa_entry']['upper_display'],row['kappa_end']['upper_display']) for row in records),default=None)
    report=dict(schema='fd2d-r137-continuous-angular-ruling-map-v1',actual_execution=True,
        source_sha256=digest(__file__),inlet_sha256=digest(args.inlet),candidate_sha256=digest(args.candidate),
        moments_sha256=digest(args.moments),flint_version=flint.__version__,precision_bits=args.precision,
        a= bounds(a),v=bounds(v),coast_length=bounds(L),
        angular_coverage='[0,pi/2] with exact D2 cos(2j phi)/sin(2j phi) reflection and pi-periodicity covering the complete circle',
        input_n_m='Actual frozen binary64 finite Fourier coefficients, not a numerical fit to samples',
        seed_chart='Exact balanced rho/a0 with certified moment intervals',
        radial_coverage='D affine in ruling w; w increases from zero to W(phi). Curvature extrema conditional on exact compatibility occur at endpoints.',
        accepted_boxes=len(records),interval_evaluations=calls,unresolved=unresolved,passed=passed,
        global_lower_displays=minima,conditional_rankone_curvature_upper_display=maximum_kappa,
        numerical_displays_are_not_outward_rounded=True,strict_bounds_are_in_binary_fields=True,
        inlet_exact_compatibility_certified=False,actual_surface_metric_certified=False,actual_surface_reach_certified=False,
        boxes=records,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:report[k] for k in ('passed','accepted_boxes','interval_evaluations','global_lower_displays','conditional_rankone_curvature_upper_display','seconds')},allow_nan=False))
    if not passed:raise SystemExit(1)


if __name__=='__main__':main()
