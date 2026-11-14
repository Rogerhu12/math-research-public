#!/usr/bin/env python3
"""Continuous whole-angle absolute bounds for the true fixed-r beta derivative.

Each real radial cell and the entire real affine parameter interval are
covered together. A direct interval enclosure of every angle is integrated
by length; no finite angular sample or quadrature accuracy is substituted.
A separate true-root finite-part collar is required to bound beta-prime.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import time
import numpy as np
from flint import arb,acb,acb_series,ctx
from fourfold_phase_beta_interval import vector_dot,vector_cross,ball_record
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_beta_combine import stored_ball
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_beta_parameter_derivative import ParameterDerivativeTarget,sha
class Dual:
    """True first parameter jet with a stable certified reciprocal derivative."""
    __slots__=("v","d")
    def __init__(self,value,derivative=0):
        self.v,self.d=value,derivative
    @staticmethod
    def pair(value):
        return value if isinstance(value,Dual) else Dual(value,0)
    def __add__(self,other):
        other=self.pair(other)
        return Dual(self.v+other.v,self.d+other.d)
    __radd__=__add__
    def __neg__(self):
        return Dual(-self.v,-self.d)
    def __sub__(self,other):
        return self+-self.pair(other)
    def __rsub__(self,other):
        return self.pair(other)+-self
    def __mul__(self,other):
        other=self.pair(other)
        return Dual(self.v*other.v,self.d*other.v+self.v*other.d)
    __rmul__=__mul__
    def inverse(self):
        inverse=1/self.v
        # A wide complex enclosure of v*v may contain zero even when v is
        # separated from zero. Squaring the certified reciprocal is valid.
        return Dual(inverse,-self.d*inverse*inverse)
    def __truediv__(self,other):
        return self*self.pair(other).inverse()
    def __rtruediv__(self,other):
        return self.pair(other)*self.inverse()
    def __pow__(self,n):
        return Dual(self.v**n,0 if n==0 else n*self.v**(n-1)*self.d)
    def sin(self):
        return Dual(self.v.sin(),self.v.cos()*self.d)
    def cos(self):
        return Dual(self.v.cos(),-self.v.sin()*self.d)


class ParameterDerivativeBulk(ParameterDerivativeTarget):
    def complete_parameter_fields(self,radial):
        if radial.imag!=0:
            raise ValueError("this absolute-bound engine covers real radial intervals")
        budgets=self.parameter_input_budget(radial,arb(".003"),arb(".32"),arb(".0025"))
        data=self.parameter_target(radial,arb(1),budgets)
        self.local_scalars=self.scalars(radial,1)
        self.local_directions=self.direction_scalars(radial,1)
        rows=[]
        for key,budget in zip(("F","Fd"),budgets):
            coefficient=data[key]
            reflected=np.empty(coefficient.shape,object)
            for index in np.ndindex(coefficient.shape):
                source=coefficient[index]
                reflected[index]=acb_series([(-1)**j*source[j] for j in range(source.prec)],prec=source.prec)
            budget=dict(budget,real_input=True)
            # sigma=0 still covers the complete real circle by +/-pi/angles.
            fields=self.physical_fields(reflected,budget,angular_sigma=arb(0))
            rows.append([fields[key] for key in ((0,0),(1,0),(2,0),(0,1),(1,1),(0,2))])
        K=Dual(data["K"][0],data["Kd"][0])
        Kp=Dual(-data["K"][1],-data["Kd"][1])
        return rows,K,Kp,budgets

    def true_angular_fields(self,index):
        # Every normalized x angle lies in one of these overlapping real
        # boxes. The phase profiles are finite but their trigonometric graph
        # is exact; no Fourier differentiation error is introduced here.
        if not hasattr(self,"real_angle_cache"):
            self.real_angle_cache={}
        if index not in self.real_angle_cache:
            x=2*arb.pi()*index/self.angles+arb(0,(arb.pi()/self.angles).upper())
            self.real_angle_cache[index]=([(k*x).sin() for k in range(1,self.modes+1)],
                                          [(k*x).cos() for k in range(1,self.modes+1)])
        ss,cc=self.real_angle_cache[index]
        beta,gamma,a,_=self.local_scalars
        bd,gd,ad,_=self.local_directions
        def mode_sum(values,change,order,angular=False):
            factors=[4*(k+1)*cc[k] if angular else ss[k] for k in range(self.modes)]
            return Dual(sum((values[k][order]*factors[k] for k in range(self.modes)),acb(0)),
                        sum((change[k][order]*factors[k] for k in range(self.modes)),acb(0)))
        b,g=mode_sum(beta,bd,0),mode_sum(gamma,gd,0)
        br,gr=mode_sum(beta,bd,1),mode_sum(gamma,gd,1)
        bt,gt=mode_sum(beta,bd,0,True),mode_sum(gamma,gd,0,True)
        sb,cb,sg,cg=b.sin(),b.cos(),g.sin(),g.cos()
        T=[-sb*cg,cb*cg,sg]
        Tr=[-cb*cg*br+sb*sg*gr,-sb*cg*br-cb*sg*gr,cg*gr]
        Tt=[-cb*cg*bt+sb*sg*gt-T[1],-sb*cg*bt-cb*sg*gt+T[0],cg*gt]
        aa,ar=Dual(a[0],ad[0]),Dual(a[1],ad[1])
        return [aa*z for z in T],[ar*T[c]+aa*Tr[c] for c in range(3)],[aa*z for z in Tt]

    def bound_density(self,left,right,waist=False):
        radial=acb(real_interval(left,right))
        rows,K,Kp,budgets=self.complete_parameter_fields(radial)
        if not (-K.v).real>0:
            raise ValueError("true negative target curvature is not separated from zero")
        kappa=(-K.v).sqrt()
        bounds=[]
        minimum={key:[] for key in ("area2","radius2","support","a","height_ratio")}
        for j in range(self.angles):
            F,X,Frr,Y,Frt,Ftt=[
                [Dual(rows[0][i][j,c],rows[1][i][j,c]) for c in range(3)]
                for i in range(6)]
            Y,Frt,Ftt=self.true_angular_fields(j)
            normal=vector_cross(Y,X)
            nr1,nr2=vector_cross(Frt,X),vector_cross(Y,Frr)
            nt1,nt2=vector_cross(Ftt,X),vector_cross(Y,Frt)
            nr=[nr1[c]+nr2[c] for c in range(3)]
            nt=[nt1[c]+nt2[c] for c in range(3)]
            area,radius,support=vector_dot(normal,normal),vector_dot(F,F),vector_dot(normal,F)
            if any(not z.v.real>0 for z in (area,radius,support)):
                raise ValueError("continuous geometry denominator failed")
            l,m,n=[vector_dot(normal,z) for z in (Frr,Frt,Ftt)]
            a,b,c=-n/area,m/area,-l/area
            if not a.v.real>0:
                raise ValueError("continuous actual a denominator failed")
            FX,FY=vector_dot(F,X),vector_dot(F,Y)
            actual_K=(l*n-m*m)/area**2
            omega,chat=(actual_K-K)/a,(b*b+K)/a
            d=(a*(vector_dot(X,X)-FX*FX/radius)
               +2*b*(vector_dot(X,Y)-FX*FY/radius)
               +c*(vector_dot(Y,Y)-FY*FY/radius))/radius
            lzr=vector_dot(nr,F)/support-vector_dot(normal,nr)/area-FX/radius
            lzt=vector_dot(nt,F)/support-vector_dot(normal,nt)/area-FY/radius
            fr,ft=Kp/(2*K)-2*lzr,-2*lzt
            numerator,denominator=(Frt[2],X[2]) if waist else (Y[2],F[2])
            if not denominator.v.real>0:
                raise ValueError("continuous height ratio denominator failed")
            ell=numerator/denominator-FY/radius
            value=d+omega*(ell*ell+ell*ft)-(a*fr*fr+2*b*fr*ft+chat*ft*ft)/4
            derivative=value.d/kappa+value.v*K.d/(2*kappa**3)
            if not derivative.is_finite():
                raise ValueError("nonfinite true parameter density derivative: "+str({
                    "angle_index":j,"value":str(value.v),"change":str(value.d),
                    "a":str(a.v),"omega":str(omega.v),"chat":str(chat.v),
                    "fr":str(fr.v),"ft":str(ft.v),"ell":str(ell.v),
                    "a_d":str(a.d),"omega_d":str(omega.d),"chat_d":str(chat.d),
                    "fr_d":str(fr.d),"ft_d":str(ft.d),"ell_d":str(ell.d)}))
            bounds.append(abs(derivative).upper())
            for key,z in zip(minimum,(area.v,radius.v,support.v,a.v,denominator.v)):
                minimum[key].append(z.real.lower())
        bound=max(bounds)
        return bound,dict(positive_real_minima={key:ball_record(min(x)) for key,x in minimum.items()},
            minus_K_real_lower=ball_record((-K.v).real.lower()),
            K_parameter_modulus_upper=ball_record(abs(K.d).upper()),
            K_radial_parameter_modulus_upper=ball_record(abs(Kp.d).upper()),
            original_E_infinite_error=ball_record(budgets[0]["E_error"]),
            derivative_E_infinite_error=ball_record(budgets[1]["E_error"]))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--center-object",type=Path,required=True)
    ap.add_argument("--root-derivative-report",type=Path,required=True)
    ap.add_argument("--center-collar",type=Path,required=True)
    ap.add_argument("--bits",type=int,default=128)
    ap.add_argument("--quarter-nodes",type=int,default=256)
    ap.add_argument("--angles",type=int,default=512)
    ap.add_argument("--start-cell",type=int,default=0)
    ap.add_argument("--max-cells",type=int)
    ap.add_argument("--cell-depth",type=int,default=12)
    ap.add_argument("--relative-root-width",default="1/4")
    ap.add_argument("--base-total-budget",default="1000")
    ap.add_argument("--root-total-budget",default="9000")
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec,ctx.cap=args.bits,4
    rr=json.loads(args.root_derivative_report.read_text());cc=json.loads(args.center_collar.read_text())
    core=Path(__file__).with_name("fourfold_phase_beta_parameter_derivative.py")
    if (rr.get("kind")!="uniform_true_affine_parameter_root_first_derivative"
            or not rr.get("proved") or rr["source_sha256"]!=sha(core)
            or rr["center_object_sha256"]!=sha(args.center_object)
            or not cc.get("complete") or cc["object_sha256"]!=sha(args.center_object)):
        raise ValueError("exact center or derivative input differs")
    target=ParameterDerivativeBulk(args.center_object,Fraction(rr["exact_parameter_half_width"]),
        args.quarter_nodes,args.angles,arb(".003"),arb(".0025"),arb(".32"))
    identity=provenance(target,args.center_object)
    for key in ("origin_inputs_sha256","direction_sha256","exact_center_parameter",
                "exact_parameter_half_width","exact_parameter_interval"):
        if identity[key]!=rr[key]:
            raise ValueError("parameter family identity differs: "+key)
    for name,digest in rr["dependency_sha256"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("changed derivative dependency: "+name)
    cut,waist=Fraction(cc["fixed_cut"]),Fraction(1,1048576)
    root_floor=stored_ball(rr["root"]).lower()
    knots={Fraction(0),cut}
    for key,values in target.frozen.items():
        if key.endswith("_knots"):
            knots.update(q for q in (abs(Fraction.from_float(float(x))) for x in values) if 0<q<cut)
    if not waist<sorted(knots)[1] or not exact_arb(cut)<root_floor:
        raise ValueError("waist crosses a knot or fixed cut crosses a true root")
    knots.add(waist);points=sorted(knots)
    cells=[(a,b) for a,b in zip(points,points[1:]) if a>=waist]
    relative=Fraction(args.relative_root_width)
    if not 0<relative<=1:
        raise ValueError("invalid deterministic near-root subdivision factor")
    base_budget,root_budget=arb(args.base_total_budget),arb(args.root_total_budget)
    if not base_budget>0 or not root_budget>=0:
        raise ValueError("invalid requested absolute derivative budgets")
    exponent=-arb(5)/2
    normalization=(root_floor-exact_arb(cut))**exponent-root_floor**exponent
    allocations=[(base_budget/len(cells)+root_budget*(
        (root_floor-exact_arb(b))**exponent-(root_floor-exact_arb(a))**exponent)/normalization).lower()
        for a,b in cells]
    identity["source_sha256"]=sha(__file__)
    report=dict(kind="uniform_true_fixed_r_parameter_derivative_bulk",complete=False,**identity,
        derivative_core_sha256=sha(core),
        root_derivative_report_sha256=sha(args.root_derivative_report),center_collar_sha256=sha(args.center_collar),
        fixed_cut=str(cut),waist_width=str(waist),bits=args.bits,quarter_nodes=args.quarter_nodes,
        angles=args.angles,radial_cells_total=len(cells),start_cell=args.start_cell,
        base_total_budget=args.base_total_budget,root_total_budget=args.root_total_budget,
        accepted_cells=[],failed_cells=[],subdivision_count=0,
        continuous_angle_cover="every real angle lies within pi/angles of a native FFT node; no trapezoidal alias is used as the integral",
        limitations=["partial absolute derivative bulk alone does not bound beta-prime",
                     "same exact parameter interval and true-root finite-part collar must be combined"])
    def save():
        report["wall_seconds"]=time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(json.dumps(report,indent=2)+"\n")
    if args.start_cell==0:
        target.set_cell(Fraction(0),waist)
        bound,domain=target.bound_density(0,waist,waist=True)
        report["waist_derivative_absolute_integral_bound"]=ball_record((exact_arb(waist)*bound).upper())
        report["waist_domain"]=domain
        save()
    stop=len(cells) if args.max_cells is None else min(len(cells),args.start_cell+args.max_cells)
    for index in range(args.start_cell,stop):
        a,b=cells[index];target.set_cell(a,b)
        pending=[(a,b,0)]
        while pending:
            left,right,depth=pending.pop()
            try:
                if exact_arb(right-left)>exact_arb(relative)*(root_floor-exact_arb(right)):
                    raise ValueError("deterministic root-distance refinement requested")
                # On the first common scalar span, the exact odd F_z and
                # F_{theta,z} divided by r are integrals from zero. Cover
                # that whole segment before differentiating their quotient.
                bound,domain=(target.bound_density(0,right,waist=True) if index==0
                              else target.bound_density(left,right))
                value=(exact_arb(right-left)*bound).upper()
                allocation=allocations[index]*exact_arb(right-left)/exact_arb(b-a)
                if not value<allocation:
                    raise ValueError("actual absolute derivative bound exceeds allocated finite budget")
                report["accepted_cells"].append(dict(index=index,left=str(left),right=str(right),depth=depth,
                    density_derivative_absolute_bound=ball_record(bound),
                    derivative_absolute_integral_bound=ball_record(value),allocated_budget=ball_record(allocation),
                    height_quotient_covered_from_zero=(index==0),domain=domain))
                print(json.dumps(dict(stage="true derivative bulk",index=index,depth=depth,bound=value.str(18))),flush=True)
            except (ValueError,ZeroDivisionError,OverflowError) as exc:
                if depth<args.cell_depth:
                    mid=(left+right)/2
                    pending.extend([(mid,right,depth+1),(left,mid,depth+1)])
                    report["subdivision_count"]+=1
                    report["latest_subdivision"]=dict(index=index,left=str(left),right=str(right),reason=repr(exc))
                else:
                    report["failed_cells"].append(dict(index=index,left=str(left),right=str(right),error=repr(exc)))
            save()
    report["complete"]=(args.start_cell==0 and stop==len(cells) and not report["failed_cells"])
    save()


if __name__=="__main__":
    main()

