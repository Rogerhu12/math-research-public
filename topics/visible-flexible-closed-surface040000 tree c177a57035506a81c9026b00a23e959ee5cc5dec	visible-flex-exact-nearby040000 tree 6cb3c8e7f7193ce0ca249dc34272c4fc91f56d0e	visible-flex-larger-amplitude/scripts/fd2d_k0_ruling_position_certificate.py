#!/usr/bin/env python3
"""Continuous R121 position windows for the actual frozen R137 ruled field.

Arb encloses the actual finite position/e1/e2 Fourier definition.  Complete
radial extrema use line segments and a quadratic minimum; no radial grid
or exact Gauss-Codazzi assumption is needed for these position conclusions.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
import flint
from flint import arb,ctx
from fd2d_k0_ruling_angular_certificate import moment,bounds


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dot(x,y):return sum((a*b for a,b in zip(x,y)),arb(0))


def main():
    ap=argparse.ArgumentParser(description=__doc__);root=Path(__file__).resolve().parent.parent
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--candidate',type=Path,default=root/'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json')
    ap.add_argument('--moments',type=Path,default=root/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json')
    ap.add_argument('--initial-boxes',type=int,default=128)
    ap.add_argument('--maximum-depth',type=int,default=8)
    ap.add_argument('--position-modes',type=int,default=64)
    ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    start=time.monotonic();ctx.prec=args.precision
    p=np.load(args.inlet,allow_pickle=False);candidate=json.loads(args.candidate.read_text())
    if str(p['candidate_sha256'].item())!=digest(args.candidate):raise ValueError('Candidate binding mismatch')
    mom=json.loads(args.moments.read_text());ref_a0=moment(mom['enclosures']['a0'])
    last=next(q for q in reversed(candidate['segments']) if q['kind']=='hermite')
    a=(ref_a0+arb(float(last['jet1'][0]))).union(arb(float(p['a'])))
    v=arb(float(last['jet1'][1])).union(arb(float(p['v'])))
    L=arb(float(p['coast_length']));rho0=a/v
    freqs=[int(x) for x in p['frequencies']]
    nc={f:arb(float(c)) for f,c in zip(freqs,p['n_phi_cos'])}
    mc={f:arb(float(c)) for f,c in zip(freqs[1:],p['m_phi_sin'])}
    raw=p['frame_fourier'][:,:9];nyquist=len(raw)-1;stop=min(args.position_modes,nyquist)
    cos=[];sin=[]
    for j in range(len(raw)):
        weight=1 if j in (0,nyquist) else 2
        cos.append([weight*arb(float(x)) for x in raw[j].real])
        sin.append([arb(0) if j in (0,nyquist) else -weight*arb(float(x)) for x in raw[j].imag])
    tails=[sum((abs(cos[j][q])+abs(sin[j][q]) for j in range(stop+1,len(raw))),arb(0)) for q in range(9)]
    tail_balls=[arb(0,tuple(map(int,r.upper().man_exp()))) for r in tails]
    waves=sorted(set(range(1,stop+1))|set(freqs[1:]));pi=arb.pi();records=[];bad=[];calls=0
    held=[arb(0),arb('281/200'),arb(0)]
    def evaluate(i,j,den):
        nonlocal calls
        calls+=1;phi=(2*pi*i/den).union(2*pi*j/den)
        n=arb(nc[0]);m=arb(0);field=[cos[0][q]+tail_balls[q] for q in range(9)]
        for f in waves:
            sn,cs=(phi*f).sin_cos()
            if f in nc:n+=nc[f]*cs;m+=mc[f]*sn
            if f<=stop:
                for q in range(9):field[q]+=cos[f][q]*cs+sin[f][q]*sn
        if not n>0:return None
        k=m/n
        W=L*(2*rho0+L)/(rho0+(rho0*rho0+(1+k*k)*L*(2*rho0+L)).sqrt())
        X,e1,e2=field[:3],field[3:6],field[6:9]
        G=[e1[q]-k*e2[q] for q in range(3)]
        Y=[X[q]+W*G[q] for q in range(3)]
        delta=[X[q]-held[q] for q in range(3)]
        A=dot(delta,delta);B=dot(delta,G);E=dot(G,G)
        if not E>0:return None
        if B>=0:
            min_dist=A;which='initial endpoint, derivative nonnegative'
        elif B+E*W<=0:
            min_dist=dot([Y[q]-held[q] for q in range(3)],[Y[q]-held[q] for q in range(3)])
            which='final endpoint, derivative nonpositive throughout'
        else:
            min_dist=A-B*B/E;which='infinite-line quadratic minimum, conservative for segment'
        rad0,rad1=dot(X,X),dot(Y,Y)
        ok=(rad0<arb(81)/16 and rad1<arb(81)/16 and abs(X[1])<arb(17)/20 and abs(Y[1])<arb(17)/20
            and X[2]>0 and Y[2]>0 and X[2]<arb(9)/10 and Y[2]<arb(9)/10 and min_dist>arb(81)/100)
        if not ok:return None
        return dict(n=n,W=W,radius2_start=rad0,radius2_end=rad1,y_start=X[1],y_end=Y[1],
            z_start=X[2],z_end=Y[2],held_distance2_lower=min_dist,held_minimum_case=which)
    def visit(i,j,den,depth):
        value=evaluate(i,j,den)
        if value is None:
            if depth>=args.maximum_depth:bad.append(dict(left=[i,den],right=[j,den],depth=depth));return
            visit(2*i,i+j,2*den,depth+1);visit(i+j,2*j,2*den,depth+1);return
        kind=value.pop('held_minimum_case')
        records.append(dict(left_over_2pi=[i,den],right_over_2pi=[j,den],depth=depth,
            held_minimum_case=kind,**{k:bounds(v) for k,v in value.items()}))
    for i in range(args.initial_boxes):visit(i,i+1,args.initial_boxes,0)
    report=dict(schema='fd2d-r137-actual-ruled-position-continuous-v1',actual_execution=True,
        source_sha256=digest(__file__),inlet_sha256=digest(args.inlet),candidate_sha256=digest(args.candidate),
        moments_sha256=digest(args.moments),helper_sha256=digest(Path(__file__).with_name('fd2d_k0_ruling_angular_certificate.py')),
        flint_version=flint.__version__,precision_bits=args.precision,position_modes_evaluated=stop,
        all_remaining_position_frame_modes_enclosed_by_exact_l1_tail=True,
        tail_bounds=[bounds(x) for x in tails],a=bounds(a),v=bounds(v),coast_length=bounds(L),
        actual_definition='Frozen Fourier X/e1/e2 and finite n,m in R137 inlet; F=X+w(e1-(m/n)e2).',
        radial_coverage='All 0<=w<=W(phi), no radial grid; norm/slab extrema at endpoints and distance quadratic minimum.',
        angular_coverage='Complete [0,2*pi], no symmetry assumed for approximate position/frame coefficients.',
        strict_claims=['|F|<9/4','|F_y|<17/20','0<F_z<9/10','|F-(0,281/200,0)|>9/10'],
        passed=not bad,accepted_boxes=len(records),interval_evaluations=calls,unresolved=bad,boxes=records,
        metric_or_Codazzi_compatibility_assumed=False,metric_certificate=False,reach_certificate=False,
        negative_support_not_repaired=True,numerical_displays_are_not_outward_rounded=True,
        strict_bounds_are_in_binary_fields=True,seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:report[k] for k in ('passed','accepted_boxes','interval_evaluations','strict_claims','seconds')},allow_nan=False))
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
