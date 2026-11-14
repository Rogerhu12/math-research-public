#!/usr/bin/env python3
"""R79: whole actual closed-background curvature/support and reach constants.

The finite graph is enclosed first by an infinite Wiener primitive bound;
where that loses angular information, a directed full-angle FFT enclosure is
used.  Both retain the exact affine scalar family and every common radial
span.  The natural graft and R74's actual radial bumps, connector, infinite
tail and flat disks are included separately.  Positive support is combined
with a proved global parallel-surface argument in R79, not with a curvature-
only assertion of reach.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_series, ctx

from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_beta_bulk_box import (
    Box, CBox, arb_box, reduce_box, square_box, complex_sincos)
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_parameter_germ import ParameterGermBulkTarget, provenance
from fourfold_phase_positive_family_outer import StablePositiveFamily
from fourfold_phase_natural_exterior_graft import NaturalGraft
from fourfold_phase_uniform_tail import down, up


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    with (gzip.open(path, "rt") if str(path).endswith(".gz") else open(path)) as f:
        return json.load(f)


def lo(record):
    return arb(record["lower"]).lower()


def hi(record):
    return arb(record["upper"]).upper()


def real_coefficient(value, index):
    z = value[index]
    if not z.imag.contains(0):
        raise ValueError("a real scalar jet lost real structure")
    return z.real


def abs_upper(value):
    return abs(value).upper()


def symmetric(radius):
    return arb(0, arb(radius).upper())


def adot(left, right):
    return sum((x*y for x, y in zip(left, right)), arb(0))


def across(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def positive_majorant(series, order=2):
    return acb_series([acb(abs_upper(series[j])) for j in range(order+1)])


def sinh_series(value):
    return (value.exp()-(-value).exp())/2


def cosh_minus_one(value):
    return 2*sinh_series(value/2)**2


def shape_from_arb(F, X, XX, a, beta, gamma, br, gr, bt, gt):
    """Exact symmetric second-form matrix in the true orthonormal frame."""
    if not a > 0:
        raise ValueError("the actual radius is not positive")
    sb, cb, sg, cg = beta.sin(), beta.cos(), gamma.sin(), gamma.cos()
    T = [-cg*sb, cg*cb, sg]
    Tr = [-cg*cb*br+sg*sb*gr, -cg*sb*br-sg*cb*gr, cg*gr]
    Tt = [-cg*cb*(1+bt)+sg*sb*gt, -cg*sb*(1+bt)-sg*cb*gt, cg*gt]
    h = -sb*X[0]+cb*X[1]
    v = -cb*X[0]-sb*X[1]
    Q, R = cg*X[2]-sg*h, cg*h+sg*X[2]
    W = Q**2+v**2
    if not W > 0:
        raise ValueError("the true transverse tangent square is not positive")
    rootW = W.sqrt()
    n = [value/rootW for value in across(T, X)]
    nt, nr, nrr = adot(n, Tt), adot(n, Tr), adot(n, XX)
    k11 = nt/a
    k12 = (nr-R*nt/a)/rootW
    k22 = (nrr-2*R*nr+R**2*nt/a)/W
    off = abs_upper(k12)
    curvature = max((abs_upper(k11)+off).upper(), (abs_upper(k22)+off).upper())
    support = adot(F, n).lower()
    if not support.is_finite() or not curvature.is_finite():
        raise ValueError("the actual shape enclosure is nonfinite")
    return dict(curvature_upper=curvature, support_lower=support,
                transverse_square_lower=W.lower(), radius_lower=a.lower(),
                k11_absolute_upper=abs_upper(k11), k12_absolute_upper=off,
                k22_absolute_upper=abs_upper(k22))


def wiener_shape(beta, gamma, radius, height_derivatives):
    """Whole-angle, true infinite primitive enclosure from scalar radial jets."""
    B = acb_series([acb(sum((abs_upper(v[j]) for v in beta), arb(0))) for j in range(3)])
    G = acb_series([acb(sum((abs_upper(v[j]) for v in gamma), arb(0))) for j in range(3)])
    cmB, cmG = cosh_minus_one(B), cosh_minus_one(G)
    dh = (1+cmG)*sinh_series(B)+cmB+cmG+cmB*cmG
    dv = sinh_series(G)/4
    Aa = positive_majorant(radius)
    Eh, Ev = Aa*dh, Aa*dv
    rows, errors = [], []
    for j in range(3):
        hfee = (math.factorial(j)*abs_upper(Eh[j])).upper()
        vfee = (math.factorial(j)*abs_upper(Ev[j])).upper()
        ar = math.factorial(j)*real_coefficient(radius,j)
        rows.append([ar+symmetric(hfee), symmetric(hfee),
                     height_derivatives[j]+symmetric(vfee)])
        errors.append(dict(horizontal=ball_record(hfee), vertical=ball_record(vfee)))
    b0, g0 = abs_upper(B[0]), abs_upper(G[0])
    b1, g1 = abs_upper(B[1]), abs_upper(G[1])
    bt = sum((4*(j+1)*abs_upper(v[0]) for j,v in enumerate(beta)),arb(0)).upper()
    gt = sum((4*(j+1)*abs_upper(v[0]) for j,v in enumerate(gamma)),arb(0)).upper()
    answer = shape_from_arb(*rows, real_coefficient(radius,0),
                           *[symmetric(v) for v in (b0,g0,b1,g1,bt,gt)])
    return answer, errors


def bdot(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]


def bcross(a,b):
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]


def box_sqrt(value):
    if np.any(value.lo <= 0):
        raise ValueError("a positive square-root interval contains zero")
    left, right = np.empty_like(value.lo), np.empty_like(value.hi)
    for key in np.ndindex(value.lo.shape):
        left[key]=float(arb(float(value.lo[key])).sqrt().lower())
        right[key]=float(arb(float(value.hi[key])).sqrt().upper())
    return Box(down(left),up(right))


class ReachFastTarget(StablePositiveFamily):
    def angular_shape(self,left,right):
        self.set_cell(left,right)
        radial=acb(real_interval(left,right))
        coefficient,_=self.finite_data(radial)
        errors=self.tail_errors(radial)
        fields=self.fast_fields(radial,coefficient,errors,True,sigma=arb(0))
        beta,gamma,radius,_=self.last_scalar
        ss,cc=self.angle_shift_cache[arb(0).str(35)]
        frequencies=CBox((4*np.arange(1,self.modes+1)).reshape(-1,1))
        def phase(values,radial_order=0,angular=False):
            row=values[radial_order].reshape(-1,1)
            answer=(row*(frequencies*cc if angular else ss)).sum()
            if np.any(answer.imag.lo>0) or np.any(answer.imag.hi<0):
                raise ValueError("a real phase enclosure lost real structure")
            return answer.real
        b,g,br,gr,bt,gt=[phase(v,j,t) for v,j,t in
                         ((beta,0,False),(gamma,0,False),(beta,1,False),
                          (gamma,1,False),(beta,0,True),(gamma,0,True))]
        sb,cb=[v.real for v in complex_sincos(CBox(b))]
        sg,cg=[v.real for v in complex_sincos(CBox(g))]
        F,X,XX=[[fields[(j,0)].real[:,k] for k in range(3)] for j in range(3)]
        aa=radius[0].real
        if not np.min(aa.lo)>0:
            raise ValueError("the actual radius is not positive")
        T=[-cg*sb,cg*cb,sg]
        Tr=[-cg*cb*br+sg*sb*gr,-cg*sb*br-sg*cb*gr,cg*gr]
        Tt=[-cg*cb*(1+bt)+sg*sb*gt,-cg*sb*(1+bt)-sg*cb*gt,cg*gt]
        h=-sb*X[0]+cb*X[1]
        v=-cb*X[0]-sb*X[1]
        Q,R=cg*X[2]-sg*h,cg*h+sg*X[2]
        W=square_box(Q)+square_box(v)
        rootW=box_sqrt(W)
        n=[value/rootW for value in bcross(T,X)]
        nt,nr,nrr=bdot(n,Tt),bdot(n,Tr),bdot(n,XX)
        k11=nt/aa
        k12=(nr-R*nt/aa)/rootW
        k22=(nrr-2*R*nr+square_box(R)*nt/aa)/W
        off=k12.abs_upper()
        curvature=float(np.max(up(np.maximum(k11.abs_upper()+off,k22.abs_upper()+off))))
        support=float(np.min(bdot(F,n).lo))
        if not np.isfinite(curvature) or not np.isfinite(support):
            raise ValueError("nonfinite actual full-angle shape interval")
        self.fast_cell_cache.clear()
        return dict(curvature_upper=arb(curvature),support_lower=arb(support),
                    transverse_square_lower=arb(float(np.min(W.lo))),
                    radius_lower=arb(float(np.min(aa.lo))),
                    k11_absolute_upper=arb(float(np.max(k11.abs_upper()))),
                    k12_absolute_upper=arb(float(np.max(off))),
                    k22_absolute_upper=arb(float(np.max(k22.abs_upper())))),[ball_record(e) for e in errors]


def common_partition(target,left,right):
    points={Fraction(left),Fraction(right)}
    for key,values in target.frozen.items():
        if key.endswith("_knots"):
            points.update(q for q in (abs(Fraction.from_float(float(x))) for x in values)
                          if left<q<right)
    return sorted(points)


def scalar_domain(target):
    left,right=None,None
    for spline in [target.base,target.shift,target.raw,target.raw_direction,*target.means,*target.height_integrals]:
        knots=[Fraction.from_float(float(x)) for x in spline.knots_float]
        a,b=knots[spline.degree],knots[-spline.degree-1]
        a,b=max(a,-b),min(b,-a)
        left=a if left is None else max(left,a)
        right=b if right is None else min(right,b)
    if not (left<=-3 and right>=3):
        raise ValueError("the full finite body leaves a true scalar base interval")
    return left,right


def check_cover(rows,left,right,key="radial_interval"):
    cursor=Fraction(left)
    for row in sorted(rows,key=lambda x:Fraction(x[key][0])):
        a,b=map(Fraction,row[key])
        if a!=cursor or not a<b:
            raise ValueError("the exact reach cover has a gap or overlap")
        cursor=b
    if cursor!=Fraction(right):
        raise ValueError("the exact reach cover stops early")


def far_geometry(closed,robin):
    geometry=closed["closed_approximate_geometry"]
    entry=robin["actual_entrance"]
    bump=robin["added_actual_geometry"]
    displacement=hi(bump["Cartesian_displacement_upper"])
    aa=hi(entry["radius_upper"])+displacement
    zz=lo(entry["height_lower"])-displacement
    ww=min(lo(bump["omega_lower"]),arb(9)/10)
    if not aa<1 or not zz>0 or not ww>0:
        raise ValueError("the true full-tail support input box failed")
    radial_support=(zz/(1+(aa/(4*ww))**2).sqrt()).lower()
    tail_slope=(aa*hi(geometry["infinite_tail_curvature_upper"])).upper()
    graph_support=((zz-aa*tail_slope)/(1+tail_slope**2).sqrt()).lower()
    support=min(radial_support,graph_support,zz.lower())
    curvature=max(hi(geometry["constant_radial_curvature_upper"]),
                  hi(bump["principal_curvature_upper"]),
                  hi(geometry["connector_curvature_upper"]),
                  hi(geometry["infinite_tail_curvature_upper"]))
    if not support>arb(9)/10 or not curvature<1:
        raise ValueError("the actual bump/connector/infinite-tail support or curvature gate failed")
    return {k:ball_record(v) for k,v in dict(radius_upper=aa,height_lower=zz,
            radial_omega_lower=ww,radial_support_lower=radial_support,
            infinite_graph_slope_upper=tail_slope,infinite_graph_support_lower=graph_support,
            full_tail_support_lower=support,full_tail_curvature_upper=curvature).items()}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--center-object",type=Path,
        default=Path("data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_object.json"))
    ap.add_argument("--half-width",type=Fraction,default=Fraction(1,2000000))
    ap.add_argument("--closed",type=Path,default=Path("notes/2026-11-12-actual-closed-approximate-exterior.json"))
    ap.add_argument("--robin",type=Path,default=Path("notes/2026-11-12-actual-exterior-robin-certificate.json"))
    ap.add_argument("--geometry",type=Path,default=Path("notes/2026-11-12-actual-diameter-and-phase-separation.json.gz"))
    ap.add_argument("--bits",type=int,default=192)
    ap.add_argument("--quarter-nodes",type=int,default=256)
    ap.add_argument("--angles",type=int,default=512)
    ap.add_argument("--max-depth",type=int,default=15)
    ap.add_argument("--max-attempts",type=int,default=10000)
    ap.add_argument("--resume",action="store_true")
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    if args.bits<128 or args.angles<args.quarter_nodes or args.angles%4:
        raise ValueError("insufficient precision or full angular cover")
    ctx.prec,ctx.cap=args.bits,3
    started=time.monotonic()
    closed,robin,geometric=map(read,(args.closed,args.robin,args.geometry))
    if not all(x.get("complete") for x in (closed,robin,geometric)):
        raise ValueError("all same-object exterior and diameter inputs must be complete")
    if sha(args.closed) not in robin["input_sha256"].values():
        raise ValueError("the tail realization is not attached to this closed background")
    for path in (args.closed,args.robin):
        if sha(path) not in geometric["input_sha256"].values():
            raise ValueError("the actual diameter/witness does not bind both exterior inputs")
    target=ParameterGermBulkTarget(args.center_object,args.half_width,args.quarter_nodes,args.angles,
                                  arb(".003"),arb(".0025"),arb(".32"))
    domain=scalar_domain(target)
    identity=provenance(target,args.center_object)
    for key in ("origin_inputs_sha256","direction_sha256","exact_parameter_interval"):
        if any(identity[key]!=x[key] for x in (closed,robin,geometric)):
            raise ValueError("the reach calculation uses a different exact family")
    identity.pop("dependency_sha256")
    identity["source_sha256"]=sha(__file__)
    dependencies=["fourfold_phase_beta_parameter_germ.py","fourfold_phase_beta_parameter_root.py",
        "fourfold_phase_beta_bulk_interval.py","fourfold_phase_beta_bulk_box.py",
        "fourfold_phase_beta_interval.py","fourfold_phase_beta_affine.py",
        "fourfold_phase_beta_combine.py","fourfold_phase_positive_family_outer.py",
        "fourfold_phase_actual_positive_cap.py","fourfold_phase_natural_exterior_graft.py",
        "fourfold_phase_exterior_entry_jet.py","fourfold_phase_root_interval.py",
        "fourfold_phase_uniform_tail.py","fourfold_interval_scalar.py"]
    dependency_sha={name:sha(Path(__file__).with_name(name)) for name in dependencies}
    points=common_partition(target,Fraction(0),Fraction(3))
    queue=deque(dict(kind="body",left=str(a),right=str(b),depth=0)
                for a,b in zip(points,points[1:]))
    graft_path=next(Path(p) for p in closed["input_sha256"] if "natural-graft" in p)
    if sha(graft_path)!=closed["input_sha256"][str(graft_path)]:
        raise ValueError("the actual natural graft report changed")
    old_graft=read(graft_path)
    if old_graft["source_sha256"]!=sha(Path(__file__).with_name("fourfold_phase_natural_exterior_graft.py")):
        raise ValueError("the true natural graft source changed")
    for row in old_graft["rows"]:
        queue.append(dict(kind="graft",left=row["offset_interval"][0],
                          right=row["offset_interval"][1],depth=0))
    report=dict(kind="actual_whole_closed_support_curvature_and_reach",complete=False,
        **identity,dependency_sha256=dependency_sha,
        input_sha256={str(p):sha(p) for p in (args.closed,args.robin,args.geometry,graft_path)},
        bits=args.bits,quarter_nodes=args.quarter_nodes,angular_boxes=args.angles,
        exact_reflected_scalar_domain=list(map(str,domain)),initial_common_body_spans=len(points)-1,
        target_support="1/10",target_curvature="12",far_geometry=far_geometry(closed,robin),
        body_cells=[],graft_cells=[],failed_cells=[],attempts=0,
        scope=["The same exact affine family, true infinite primitive and actual R74 far bumps are used.",
               "Reach uses the full positive-support parallel-surface proof in R79.",
               "The corrected-family conclusion requires the displayed uniform intrinsic C0/C1/C2 error budget.",
               "No exact isometric family or noncongruence conclusion is supplied by this certificate."])
    if args.resume:
        saved=read(args.out)
        for key in ("source_sha256","dependency_sha256","input_sha256","exact_parameter_interval",
                    "bits","quarter_nodes","angular_boxes"):
            if report[key]!=saved[key]:raise ValueError("resume identity mismatch: "+key)
        if saved["complete"]:raise ValueError("the reach certificate is already complete")
        report=saved;queue=deque(saved["pending"])
    previous_seconds=report.get("elapsed_seconds",0.)
    fast=None;graft=None
    def save():
        report["pending"]=list(queue)
        report["elapsed_seconds"]=previous_seconds+time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        with (gzip.open(args.out,"wt") if str(args.out).endswith(".gz") else open(args.out,"w")) as f:
            json.dump(report,f,ensure_ascii=False,indent=2);f.write("\n")
    save()
    while queue and report["attempts"]<args.max_attempts:
        task=queue.popleft();a,b=Fraction(task["left"]),Fraction(task["right"])
        report["attempts"]+=1
        try:
            ctx.cap=3
            if task["kind"]=="body":
                target.set_cell(a,b)
                beta,gamma,radius,height=target.scalars(acb(real_interval(a,b)),1)
                z=[math.factorial(j)*real_coefficient(height,j) for j in range(3)]
                try:
                    values,fees=wiener_shape(beta,gamma,radius,z)
                    if not (values["curvature_upper"]<12 and values["support_lower"]>arb(1)/10):
                        raise ValueError("whole-angle Wiener bound needs local angle information")
                    method="infinite_Wiener_primitive"
                except (ValueError,ZeroDivisionError):
                    if fast is None:
                        fast=ReachFastTarget(args.center_object,args.half_width,args.quarter_nodes,args.angles,
                                             arb(".003"),arb(".0025"),arb(".32"))
                    values,fees=fast.angular_shape(a,b)
                    method="directed_full_angle_infinite_primitive"
                radial=[str(a),str(b)]
            else:
                if graft is None:
                    graft=NaturalGraft(args.center_object,args.half_width,Fraction(1,8))
                ctx.cap=3
                jets=graft.jets(a,b)
                z=[graft.Z_global,real_coefficient(jets["slope"],0),real_coefficient(jets["slope"],1)]
                values,fees=wiener_shape(jets["beta"],jets["gamma"],jets["radius"],z)
                method="actual_natural_graft_infinite_Wiener_primitive"
                radial=[str(3+a),str(3+b)]
            if not (values["curvature_upper"]<12 and values["support_lower"]>arb(1)/10):
                raise ValueError("the continuous shape bounds exceed the strict target")
            row=dict(radial_interval=radial,offset_interval=[str(a),str(b)] if task["kind"]=="graft" else None,
                     depth=task["depth"],method=method,primitive_error=fees,
                     **{k:ball_record(v) for k,v in values.items()})
            report[task["kind"]+"_cells"].append(row)
        except (ValueError,ZeroDivisionError,OverflowError) as exc:
            if task["depth"]<args.max_depth:
                mid=(a+b)/2
                queue.appendleft(dict(task,left=str(mid),right=str(b),depth=task["depth"]+1))
                queue.appendleft(dict(task,left=str(a),right=str(mid),depth=task["depth"]+1))
            else:report["failed_cells"].append(dict(task,reason=str(exc)))
        if report["attempts"]%10==0:
            save()
            print(json.dumps(dict(attempts=report["attempts"],pending=len(queue),
                body=len(report["body_cells"]),graft=len(report["graft_cells"]),
                failed=len(report["failed_cells"]))),flush=True)
    if not queue and not report["failed_cells"]:
        check_cover(report["body_cells"],0,3)
        check_cover(report["graft_cells"],3,Fraction(25,8))
        sigma=min([lo(report["far_geometry"]["full_tail_support_lower"]),
                   *[lo(r["support_lower"]) for r in report["body_cells"]+report["graft_cells"]]])
        K=max([hi(report["far_geometry"]["full_tail_curvature_upper"]),
               *[hi(r["curvature_upper"]) for r in report["body_cells"]+report["graft_cells"]]])
        D=hi(geometric["certified_geometry"]["diameter_upper"])
        reach=min(sigma,(1/K).lower())
        e0=e1=e2=arb(1)/1000
        corrected_sigma=(sigma-e0-D*e1/(1-e1)).lower()
        corrected_K=((K+e2)/(1-e1)**2).upper()
        corrected_D=(D+2*e0).upper()
        corrected_reach=min(corrected_sigma,(1/corrected_K).lower())
        if not (sigma>arb(1)/10 and K<12 and reach/D>arb(3)/100
                and corrected_sigma>0 and corrected_reach/corrected_D>arb(3)/100):
            raise ValueError("the complete reach or C2 stability gate failed")
        report["certified_geometry"]={k:ball_record(v) for k,v in dict(
            support_lower=sigma,principal_curvature_upper=K,diameter_upper=D,
            global_reach_lower=reach,reach_over_D_lower=(reach/D).lower(),
            intrinsic_C0_budget=e0,intrinsic_C1_budget=e1,intrinsic_C2_budget=e2,
            corrected_support_lower=corrected_sigma,corrected_curvature_upper=corrected_K,
            corrected_D_upper=corrected_D,corrected_global_reach_lower=corrected_reach,
            corrected_reach_over_D_lower=(corrected_reach/corrected_D).lower()).items()}
        report["complete"]=True
    save()
    print(json.dumps(dict(complete=report["complete"],report_sha256=sha(args.out),
                         attempts=report["attempts"],failed=len(report["failed_cells"]),
                         elapsed_seconds=report["elapsed_seconds"])),flush=True)
    if not report["complete"]:
        raise SystemExit("the reach cover is incomplete; resume its saved exact queue")


if __name__=="__main__":
    main()
