#!/usr/bin/env python3
"""Enclose true Codazzi residuals by joint radial/angular Taylor cancellation.

At each box/cell midpoint the full residual and its first derivatives are
evaluated before taking absolute values. Its complete second derivatives
on the closed box/cell pay the Taylor remainder. The residual itself is enclosed, with original infinite target tails and
the whole real parameter interval. R131 supplies true derivative continuation from
the C0 tube and gap. No residual theta derivative or C1 Riccati test is used.
No projected PDE identity is assumed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import math
from pathlib import Path
import time
import numpy as np
from flint import arb, ctx
from fourfold_codazzi_high_target_jets import HighCodazziTarget
from fourfold_phase_codazzi_continuation_validate import (
    ExactCandidate, complex_box, positive_to_full, initial_error, maxabs)
from fourfold_phase_newton_source_centered import CenteredPolynomial
from fourfold_phase_two_jet_newton_source import (
    Box,CBox,zeros,arb_box,square_box,real_interval,record,save,sha)
from fourfold_phase_beta_bulk_interval import exact_arb


class Jet:
    """Real interval normalized derivatives, with explicit finite rectangle."""
    def __init__(self,rows):
        self.rows = [[x if isinstance(x,Box) else Box(x) for x in row] for row in rows]
        self.m,self.n = len(rows),len(rows[0])
        if not self.m or not self.n or any(len(r)!=self.n for r in rows):
            raise ValueError("invalid jet rectangle")
    def __getitem__(self,key):
        return self.rows[key[0]][key[1]]
    def scalar(self,x):
        return Jet([[x if i==j==0 else 0 for j in range(self.n)] for i in range(self.m)])
    def coerce(self,x):
        return x if isinstance(x,Jet) else self.scalar(x)
    def __add__(self,x):
        x=self.coerce(x);m,n=min(self.m,x.m),min(self.n,x.n)
        return Jet([[self[i,j]+x[i,j] for j in range(n)] for i in range(m)])
    __radd__=__add__
    def __neg__(self):
        return Jet([[-x for x in row] for row in self.rows])
    def __sub__(self,x):
        return self+-self.coerce(x)
    def __rsub__(self,x):
        return self.coerce(x)+-self
    def __mul__(self,x):
        if not isinstance(x,Jet):
            return Jet([[v*x for v in row] for row in self.rows])
        m,n=min(self.m,x.m),min(self.n,x.n)
        return Jet([[sum((self[a,b]*x[i-a,j-b] for a in range(i+1)
                          for b in range(j+1)),Box(0.))
                     for j in range(n)] for i in range(m)])
    __rmul__=__mul__
    def inv(self):
        rows=[[Box(0.) for _ in range(self.n)] for _ in range(self.m)]
        z=Box(1.)/self[0,0];rows[0][0]=z
        for i in range(self.m):
            for j in range(self.n):
                if not i and not j:continue
                rows[i][j]=-z*sum((self[a,b]*rows[i-a][j-b]
                    for a in range(i+1) for b in range(j+1) if a or b),Box(0.))
        return Jet(rows)
    def __truediv__(self,x):
        return self*x.inv() if isinstance(x,Jet) else self*(Box(1.)/(x if isinstance(x,Box) else Box(x)))
    def dr(self):
        if self.m<2:raise ValueError("unpaid radial jet")
        return Jet([[(i+1)*self[i+1,j] for j in range(self.n)] for i in range(self.m-1)])
    def dt(self):
        if self.n<2:raise ValueError("unpaid angular jet")
        return Jet([[(j+1)*self[i,j+1] for j in range(self.n-1)] for i in range(self.m)])


def radial_add(a,b):
    return [x+y for x,y in zip(a,b)]


def radial_mul(a,b):
    return [sum((a[j]*b[i-j] for j in range(i+1)),CBox(0.))
            for i in range(min(len(a),len(b)))]


def radial_constant(c):
    return [c,CBox(0.),CBox(0.),CBox(0.)]


class TaylorCandidate(ExactCandidate):
    def radial_jets(self,piece,left,right):
        lo,hi=self.times[piece:piece+2]
        if not lo<=left<=right<=hi:
            raise ValueError("candidate radial jet crosses its exact polynomial join")
        h=exact_arb(hi-lo)
        x=[CBox(arb_box((real_interval(left,right)-exact_arb(lo))/h)),
           CBox(arb_box(1/h)),CBox(0.),CBox(0.)]
        one_minus_x=radial_add(radial_constant(CBox(1.)),[-v for v in x])
        L,R=complex_box(self.ends[piece]),complex_box(self.ends[piece+1])
        cc=[radial_constant(complex_box(v)) for v in self.corrections[piece]]
        value=cc[5]
        for j in range(4,-1,-1):
            factor=x if j%2==0 else one_minus_x
            value=radial_add(cc[j],radial_mul(value,factor))
        field=radial_add(radial_add(radial_constant(L),radial_mul(radial_constant(R-L),x)),
                         radial_mul(radial_mul(value,x),one_minus_x))
        return [positive_to_full(v,self.grid) for v in field]

    def enclosed_jets(self,piece,left,right,angles,closed):
        radial=self.radial_jets(piece,left,right)
        max_angle=5 if closed else 3
        polys={}
        for i in range(4):
            for component in range(2):
                coefficient=radial[i][:,component]
                for j in range(max_angle+1):
                    polys[i,j,component]=CenteredPolynomial(
                        coefficient,arb(0),self.degree,self.target.polynomial_fft)
                    coefficient=coefficient*CBox(0.,Box(self.frequencies))/(j+1)
        keys=list(polys)
        block=zeros((angles,len(keys)))
        modes=np.asarray([j if j<self.grid//2 else j-self.grid for j in range(self.grid)])
        for column,key in enumerate(keys):
            block[modes%angles,column]=polys[key].c
        values=self.target.polynomial_fft.fft(block,inverse=True)*angles
        if not np.all((values.imag.lo<=0)&(values.imag.hi>=0)):
            raise ValueError("real candidate jets lost zero imaginary enclosure")
        sample={key:values.real[:,column] for column,key in enumerate(keys)}
        angular_h=arb.pi()/(4*angles)
        out=[]
        for component in range(2):
            rows=[]
            for i in range(4):
                row=[]
                for j in range(4):
                    key=(i,j,component);p=polys[key]
                    fee=arb_box(p.error)
                    if closed:
                        dp=polys[i,j+1,component]
                        d2p=polys[i,j+2,component]
                        d1=Box(sample[i,j+1,component].abs_upper())+arb_box(dp.error)
                        # The coefficients are normalized angular derivatives.
                        second=(d2p.norm()+d2p.error).upper()
                        fee=fee+d1*arb_box((j+1)*angular_h)
                        fee=fee+arb_box((j+1)*(j+2)*angular_h**2*second/2)
                    row.append(sample[key]+Box(-fee.hi,fee.hi))
                rows.append(row)
            out.append(Jet(rows))
        return out


def target_jet(coeff,prefix):
    keys=(prefix,prefix+"1",prefix+"2")
    return Jet([[arb_box(coeff[key]/math.factorial(i)) if j==0 else 0
                 for j in range(4)] for i,key in enumerate(keys)])


def residual_jets(B,C,coeff):
    if not np.all(C[0,0].hi<0):
        raise ValueError("complete candidate C chart is not negative")
    K=target_jet(coeff,"K")
    gamma=target_jet(coeff,"gamma")
    beta=target_jet(coeff,"beta")
    A=(K+B*B)/C
    RB=B.dr()-gamma*A.dt()+2*beta*B
    RC=C.dr()-gamma*B.dt()-beta*(A-C)
    if (RB.m,RB.n,RC.m,RC.n)!=(3,3,3,3):
        raise ValueError("insufficient true mixed residual derivative rectangle")
    return RB,RC


def taylor_residual(center,full,angular_order,radial_h,angular_h):
    j=angular_order
    r,t=arb_box(radial_h),arb_box(angular_h)
    magnitude=lambda v:Box(v.abs_upper())
    fee=(r*magnitude(center[1,j])
         +(j+1)*t*magnitude(center[0,j+1])
         +r*r*magnitude(full[2,j])
         +(j+1)*r*t*magnitude(full[1,j+1])
         +((j+1)*(j+2)/2)*t*t*magnitude(full[0,j+2]))
    refined=center[0,j]+Box(-fee.hi,fee.hi)
    direct=full[0,j]
    lo,hi=np.maximum(refined.lo,direct.lo),np.minimum(refined.hi,direct.hi)
    if not np.all(lo<=hi):
        raise ValueError("two independently valid residual enclosures are disjoint")
    return Box(lo,hi)*math.factorial(j)


def piece_budget(candidate,target,piece,left,right,angles):
    full_coeff=target.coefficients(left,right)
    if not full_coeff["K"]<0:
        raise ValueError("strict true negative curvature unresolved")
    germ=list(map(str,target.cell))
    Bf,Cf=candidate.enclosed_jets(piece,left,right,angles,True)
    RBf,RCf=residual_jets(Bf,Cf,full_coeff)
    mid=(left+right)/2
    mid_coeff=target.coefficients(mid,mid)
    Bm,Cm=candidate.enclosed_jets(piece,mid,mid,angles,False)
    RBm,RCm=residual_jets(Bm,Cm,mid_coeff)
    hr=exact_arb((right-left)/2);ht=arb.pi()/(4*angles)
    RB,RC=(taylor_residual(m,f,0,hr,ht) for m,f in ((RBm,RBf),(RCm,RCf)))
    B,C=Bf[0,0],Cf[0,0]
    Bt,Ct=Bf[0,1],Cf[0,1]
    k=arb_box(full_coeff["k"]);C2=square_box(C)
    P,Q=(B+k)/C,(B-k)/C
    Pt,Qt=Bt/C-(B+k)*Ct/C2,Bt/C-(B-k)*Ct/C2
    RP,RQ=(RB-P*RC)/C,(RB-Q*RC)/C
    bounds=dict(Mhat=maxabs(P,Q),D1=maxabs(Pt,Qt),
        rho0=maxabs(RP,RQ),BCrho0=maxabs(RB,RC),
        gamma=full_coeff["gamma"].upper(),beta=abs(full_coeff["beta"]).upper(),
        kappa=abs(full_coeff["kappa"]).upper(),k_lower=full_coeff["k"].lower(),
        C_abs_lower=arb(float(np.min(-C.hi))),C_abs_upper=maxabs(C),
        candidate_gap=(2*full_coeff["k"].lower()/maxabs(C)).lower())
    diagnostics=dict(RB=maxabs(RB),RC=maxabs(RC),direct_RB=maxabs(RBf[0,0]))
    return bounds,full_coeff,germ,diagnostics


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate",type=Path,default=Path(
        "notes/2026-11-13-codazzi-dense-r005-n512-candidate.npz.gz"))
    parser.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    parser.add_argument("--right",type=Fraction,default=Fraction(1,100))
    parser.add_argument("--half-width",type=Fraction,default=Fraction(1,10**9))
    parser.add_argument("--nodes",type=int,default=512)
    parser.add_argument("--angles",type=int,default=4096)
    parser.add_argument("--candidate-grid",type=int,default=1024)
    parser.add_argument("--subdivide",type=int,default=1)
    parser.add_argument("--bits",type=int,default=192)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args();ctx.prec=args.bits;ctx.cap=4
    if args.out.exists():raise FileExistsError("refusing to overwrite a native residual report")
    started=time.monotonic()
    target=HighCodazziTarget(args.object,args.half_width,args.nodes,args.angles)
    if args.candidate_grid < 2 or args.candidate_grid & (args.candidate_grid-1):
        raise ValueError("finite candidate FFT grid must be a power of two")
    if args.angles < args.candidate_grid:
        raise ValueError("closed angular cover is smaller than the candidate grid")
    # No finite Fourier products are formed: all nonlinear products/quotients
    # are real point/cell interval jet operations. The grid need only contain
    # every exact candidate Fourier coefficient, checked by ExactCandidate.
    # Original primitive nodes and every infinite target tail stay unchanged.
    target.product_grid=args.candidate_grid
    candidate=TaylorCandidate(args.candidate,target)
    initial=initial_error(candidate,target,args.angles)
    report=dict(kind="actual_R126_continuous_Codazzi_Cauchy_validation",
        complete=False,continuation_certified=False,closed_surface_complete=False,
        exact_requested_interval=["0",str(args.right)],whole_affine_parameter_interval=True,
        parameter_half_width=str(args.half_width),
        exact_center_parameter=candidate.metadata["exact_center_parameter"],
        whole_real_angular_circle=True,source_sha256=sha(__file__),
        candidate_sha256=sha(args.candidate),candidate_metadata=candidate.metadata,
        object_sha256=sha(args.object),coefficient_provider_sha256=sha(
            Path(__file__).with_name("fourfold_codazzi_high_target_jets.py")),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ("fourfold_phase_codazzi_coefficients.py",
             "fourfold_phase_codazzi_continuation_validate.py",
             "fourfold_phase_newton_source_centered.py")},
        bits=args.bits,primitive_nodes=args.nodes,angular_closed_cells=args.angles,
        exact_finite_candidate_grid=args.candidate_grid,
        residual_enclosure="full joint second-order radial/angular Taylor; C0 residual only; complete mixed remainder",
        initial_error={key:record(value) for key,value in initial.items()},rows=[],failure=None)
    end=Fraction(0)
    try:
        for piece,(a,b) in enumerate(zip(candidate.times,candidate.times[1:])):
            if a>=args.right:break
            b=min(b,args.right)
            for part in range(args.subdivide):
                left=a+(b-a)*part/args.subdivide
                right=a+(b-a)*(part+1)/args.subdivide
                if left!=end:raise ValueError("incomplete exact radial cover")
                bounds,coeff,germ,diagnostic=piece_budget(candidate,target,piece,left,right,args.angles)
                report["rows"].append(dict(piece=piece,part=part,
                    interval=[str(left),str(right)],actual_scalar_germ=germ,
                    bounds={key:record(v) for key,v in bounds.items()},
                    true_target_coefficients={key:record(v) for key,v in coeff.items()},
                    residual_comparison={key:record(v) for key,v in diagnostic.items()}))
                end=right;report["covered_interval"]=["0",str(end)]
                report["wall_seconds"]=time.monotonic()-started
                save(args.out,report)
                print(dict(piece=piece,part=part,right=str(right),rho0=bounds["rho0"].str(10),
                    RB=diagnostic["RB"].str(8),
                    direct_RB=diagnostic["direct_RB"].str(8),seconds=report["wall_seconds"]),flush=True)
        if end!=args.right:raise ValueError("requested radial endpoint not covered")
        report["complete"]=True
    except Exception as exc:
        report["failure"]=repr(exc)
    report["wall_seconds"]=time.monotonic()-started
    save(args.out,report)
    print(dict(complete=report["complete"],failure=report["failure"],
               rows=len(report["rows"]),wall_seconds=report["wall_seconds"]),flush=True)


if __name__=="__main__":main()
