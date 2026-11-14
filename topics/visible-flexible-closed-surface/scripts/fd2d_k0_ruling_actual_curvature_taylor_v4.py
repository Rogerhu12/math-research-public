#!/usr/bin/env python3
"""Same actual ruled curvature, with dependency-preserving angular Taylor boxes.

Uses four exact Fourier derivatives and order-two Taylor enclosures of the
complete radial quadratic coefficients.  Scalar jets use Taylor coefficients
(derivative divided by factorial).  No PDE or matrix solver is involved.
"""
from __future__ import annotations
import argparse,gzip,json,time
from pathlib import Path
import flint
from flint import arb,ctx
from fd2d_k0_ruling_actual_curvature_certificate import ActualRuledIntervals,digest,bounds


def jadd(a,b):return [x+y for x,y in zip(a,b)]
def jneg(a):return [-x for x in a]
def jsub(a,b):return jadd(a,jneg(b))
def jscale(c,a):return [c*x for x in a]
def jmul(a,b):return [sum((a[k]*b[d-k] for k in range(d+1)),arb(0)) for d in range(min(len(a),len(b)))]
def jinv(a):
    b=[1/a[0]]
    for d in range(1,len(a)):b.append(-sum((a[k]*b[d-k] for k in range(1,d+1)),arb(0))/a[0])
    return b
def jder(a):return [(d+1)*a[d+1] for d in range(len(a)-1)]
def vadd(a,b):return [jadd(x,y) for x,y in zip(a,b)]
def vsub(a,b):return [jsub(x,y) for x,y in zip(a,b)]
def vmul(c,a):return [jmul(c,x) for x in a]
def vder(a):return [jder(x) for x in a]
def jdot(a,b):
    terms=[jmul(x,y) for x,y in zip(a,b)]
    return [sum((row[d] for row in terms),arb(0)) for d in range(min(map(len,terms)))]
def jcross(a,b):return [jsub(jmul(a[1],b[2]),jmul(a[2],b[1])),jsub(jmul(a[2],b[0]),jmul(a[0],b[2])),jsub(jmul(a[0],b[1]),jmul(a[1],b[0]))]
def taylor_value(center,interval,delta):return center[0]+center[1]*delta+interval[2]*(delta*delta)


class TaylorActualRuledIntervals(ActualRuledIntervals):
    def __init__(self,*args):
        super().__init__(*args)
        self.tails=[[sum((j**d*(abs(self.cos[j][q])+abs(self.sin[j][q])) for j in range(self.stop+1,len(self.cos))),arb(0)) for q in range(9)] for d in range(5)]
        factorial=(1,1,2,6,24)
        self.tail_balls=[[arb(0,tuple(map(int,(x/factorial[d]).upper().man_exp()))) for x in row] for d,row in enumerate(self.tails)]

    def fourier_jets(self,phi):
        F=[[self.tail_balls[d][q]+(self.cos[0][q] if d==0 else 0) for d in range(5)] for q in range(9)]
        n=[self.nc[0],arb(0),arb(0),arb(0),arb(0)];m=[arb(0) for _ in range(5)]
        for f in self.waves:
            sn,cs=(phi*f).sin_cos()
            cj=[cs,-f*sn,-f*f*cs/2,f**3*sn/6,f**4*cs/24]
            sj=[sn,f*cs,-f*f*sn/2,-f**3*cs/6,f**4*sn/24]
            if f in self.nc:
                n=jadd(n,jscale(self.nc[f],cj));m=jadd(m,jscale(self.mc[f],sj))
            if f<=self.stop:
                for q in range(9):F[q]=jadd(F[q],jadd(jscale(self.cos[f][q],cj),jscale(self.sin[f][q],sj)))
        return F,n,m

    @staticmethod
    def refine_field(center,interval,delta):
        result=list(interval)
        for d in range(3):
            result[d]=center[d]+(d+1)*center[d+1]*delta+((d+1)*(d+2)/2)*interval[d+2]*(delta*delta)
        return result

    @staticmethod
    def coefficient_jets(F,n,m):
        k=jmul(m,jinv(n));X,e1,e2=F[:3],F[3:6],F[6:9]
        G=vsub(e1,vmul(k,e2));Gp=vder(G);Gpp=vder(Gp);Xp=vder(X);Xpp=vder(Xp)
        C0=jcross(G,Xp);C1=jcross(G,Gp);E=jdot(G,G);fn=jdot(C0,Gp)
        area=[jdot(C0,C0),jscale(2,jdot(C0,C1)),jdot(C1,C1)]
        num=[jsub(jmul(E,jdot(C0,Xpp)),jscale(2,jmul(jdot(G,Xp),fn))),
            jsub(jmul(E,jadd(jdot(C0,Gpp),jdot(C1,Xpp))),jscale(2,jmul(jdot(G,Gp),fn))),
            jmul(E,jdot(C1,Gpp))]
        return dict(k=k,area=area,num=num,fn=fn)

    def angle_box(self,left,right,den):
        pi=arb.pi();phi=(2*pi*left/den).union(2*pi*right/den)
        mid=pi*(left+right)/den;half=pi*(right-left)/den
        delta=arb(0,tuple(map(int,half.upper().man_exp())))
        Fc,nc,mc=self.fourier_jets(mid);Fi,ni,mi=self.fourier_jets(phi)
        Fi=[self.refine_field(c,i,delta) for c,i in zip(Fc,Fi)]
        ni=self.refine_field(nc,ni,delta);mi=self.refine_field(mc,mi,delta)
        if not ni[0]>0:return None
        center=self.coefficient_jets(Fc,nc,mc);interval=self.coefficient_jets(Fi,ni,mi)
        k=taylor_value(center['k'],interval['k'],delta)
        W=self.L*(2*self.rho0+self.L)/(self.rho0+(self.rho0*self.rho0+(1+k*k)*self.L*(2*self.rho0+self.L)).sqrt())
        return dict(n=ni[0],W=W,area_coeff=[taylor_value(c,i,delta) for c,i in zip(center['area'],interval['area'])],
            numerator_coeff=[taylor_value(c,i,delta) for c,i in zip(center['num'],interval['num'])],
            fnum=taylor_value(center['fn'],interval['fn'],delta))


def main():
    root=Path(__file__).resolve().parent.parent
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--candidate',type=Path,default=root/'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json')
    ap.add_argument('--moments',type=Path,default=root/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json')
    ap.add_argument('--initial-angle-boxes',type=int,default=256)
    ap.add_argument('--radial-boxes',type=int,default=16)
    ap.add_argument('--maximum-angle-depth',type=int,default=5)
    ap.add_argument('--position-modes',type=int,default=96)
    ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--curvature-bound',default='73/10')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();ctx.prec=args.precision
    definition=TaylorActualRuledIntervals(args.inlet,args.candidate,args.moments,args.position_modes)
    target=arb(args.curvature_bound);records=[];bad=[];calls=0;radial_calls=0
    def visit(left,right,den,depth):
        nonlocal calls,radial_calls
        calls+=1;data=definition.angle_box(left,right,den);rows=[];ok=data is not None
        if ok:
            for r in range(args.radial_boxes):
                radial_calls+=1;value=definition.radial_box(data,r,r+1,args.radial_boxes)
                if value is None or not value['curvature_upper']<target:ok=False;break
                rows.append(value)
        if ok:
            envelope=dict(rows[0])
            for row in rows[1:]:
                for key in envelope:envelope[key]=envelope[key].union(row[key])
            records.append(dict(angle_left_over_2pi=[left,den],angle_right_over_2pi=[right,den],depth=depth,
                n=bounds(data['n']),W=bounds(data['W']),radial_uniform_cells=args.radial_boxes,
                all_radial_cells_verified=True,radial_envelope={key:bounds(x) for key,x in envelope.items()}))
        elif depth<args.maximum_angle_depth:
            visit(2*left,left+right,2*den,depth+1);visit(left+right,2*right,2*den,depth+1)
        else:bad.append(dict(left_over_2pi=[left,den],right_over_2pi=[right,den],depth=depth))
    for j in range(args.initial_angle_boxes):
        visit(j,j+1,args.initial_angle_boxes,0)
        if (j+1)%32==0:print(json.dumps(dict(progress=j+1,total=args.initial_angle_boxes,accepted_angles=len(records),unresolved=len(bad),seconds=time.monotonic()-started)),flush=True)
    report=dict(schema='fd2d-actual-finite-ruled-curvature-Taylor-Arb-v4',actual_execution=True,
        source_sha256=digest(__file__),algebra_helper_sha256=digest(Path(__file__).with_name('fd2d_k0_ruling_actual_curvature_certificate.py')),
        binary_helper_sha256=digest(Path(__file__).with_name('fd2d_k0_ruling_angular_certificate.py')),
        inlet_sha256=digest(args.inlet),candidate_sha256=digest(args.candidate),moments_sha256=digest(args.moments),
        flint_version=flint.__version__,precision_bits=args.precision,position_modes_explicit=definition.stop,
        angular_derivatives_enclosed=4,angular_Taylor_order=2,
        all_remaining_modes_included_as_exact_l1_derivative_tails=True,
        derivative_tail_bounds=[[bounds(x) for x in row] for row in definition.tails],
        a=bounds(definition.a),v=bounds(definition.v),coast_length=bounds(definition.L),
        actual_surface_definition='F(phi,w)=X(phi)+w(e1(phi)-[m(phi)/n(phi)]e2(phi)), saved Cartesian Fourier coefficients',
        radial_range_method='Quadratic Bernstein convex hull of true area and curvature numerator',
        radial_cover='All 0<=w<=W(phi), using uniform tau=w/W(phi) strips',
        angular_cover='Full [0,2pi], no assumed Cartesian symmetry',
        strict_curvature_claim='max(abs(actual principal curvatures)) < '+args.curvature_bound,
        curvature_upper_enclosures_are_of_computed_upper_bounds_not_two_sided_curvature_ranges=True,
        generic_power_on_zero_containing_Arb_intervals_not_used=True,
        strict_immersion_claim='actual |F_w cross F_phi|^2 > 0',
        exact_metric_or_Gauss_Codazzi_assumed=False,metric_certificate=False,global_embedding_certificate=False,full_reach_certificate=False,
        passed=not bad,accepted_angle_boxes=len(records),accepted_radial_boxes=len(records)*args.radial_boxes,
        interval_angle_evaluations=calls,interval_radial_evaluations=radial_calls,unresolved=bad,boxes=records,
        strict_bounds_in_exact_binary_fields=True,numerical_displays_not_outward_rounded=True,seconds=time.monotonic()-started)
    raw=(json.dumps(report,indent=2,allow_nan=False)+'\n').encode()
    if args.out.suffix=='.gz':args.out.write_bytes(gzip.compress(raw,mtime=0))
    else:
        if len(raw)>1000000:raise ValueError('Use .json.gz for data over 1 MB')
        args.out.write_bytes(raw)
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),bytes=args.out.stat().st_size,passed=report['passed'],angles=len(records),radial_boxes=len(records)*args.radial_boxes,unresolved=len(bad),seconds=report['seconds'])),flush=True)
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
