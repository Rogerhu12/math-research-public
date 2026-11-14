#!/usr/bin/env python3
"""Actual wide-collar pilot with correlated primitive Taylor and finite height.

The original infinite Fourier errors remain present. The radial Taylor error
is uniform on a whole complex disk before computing target E and curvature.
A degree-four height agrees with the true normalized height at the root; away
from the root it is a new exact gauge, with E11 retained. This is a local pilot,
not a completed wide collar, reflection, or inverse.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from collections import OrderedDict
from fractions import Fraction as F
import hashlib,json,math,time
from pathlib import Path
import numpy as np
from flint import acb,acb_series,arb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import ParameterGermBulkTarget,provenance
from fourfold_phase_canonical_collar_far import (
    OrdinarySpanGeometry,common_knots,ordinary_canonical_operator)
from fourfold_phase_canonical_collar_bivariate_recovery import FortyTermGeometry
from fourfold_phase_canonical_collar_finite import (
    FiniteRootCoordinates,physical_polynomial_trial,root_potential_coefficients,
    trial_residual_coefficients,physical_radial_derivative,derivative,align,
    jet_function,real_jet,mul,add,radial_series,angular_lift,jet_summary)
from fourfold_time_angle_jets import TimeAngleJet as Jet


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def shift_polynomial(value,constant,direction,precision):
    """Exact finite composition; all discarded analytic tails are separate."""
    if precision>value.prec:
        raise ValueError("unknown native coefficient requested")
    z=acb_series([acb(constant),acb(direction)],prec=precision)
    out=acb_series([value[value.prec-1]],prec=precision)
    for j in range(value.prec-2,-1,-1):
        out=out*z+value[j]
    return out


class CorrelatedGermTarget(ParameterGermBulkTarget):
    def __init__(self,*args,native_order=48,native_radius=F(1,128),**kwargs):
        if native_order<24:raise ValueError("native polynomial too short")
        self.native_order=int(native_order)
        self.native_radius=exact_arb(F(native_radius))
        self.native_anchor=None;self.native_key=None
        self.native_coefficient=None;self.native_budget=None
        self.last_correlated_budget=None
        super().__init__(*args,**kwargs)

    def set_anchor(self,anchor):
        anchor=F(anchor)
        if self.cell is None or not self.cell[0]<=anchor<=self.cell[1]:
            raise ValueError("native anchor outside the selected exact scalar germ")
        key=(self.cell,anchor,ctx.prec,self.native_order)
        if key!=self.native_key:
            self.native_key=key;self.native_anchor=exact_arb(anchor)
            self.native_coefficient=None;self.native_budget=None

    def build_native(self,sigma):
        if self.native_anchor is None:raise ValueError("set the exact anchor first")
        if self.native_coefficient is None:
            old=ctx.cap
            try:
                ctx.cap=self.native_order
                coefficient,_=super().primitive(acb(self.native_anchor),self.native_radius)
                if any(v.prec!=self.native_order for v in coefficient.flat):
                    raise ValueError("unexpected retained native Taylor precision")
                self.native_coefficient=coefficient
            finally:ctx.cap=old
        key=arb(sigma).repr()
        if self.native_budget is None or self.native_budget[0]!=key:
            budget=super().analytic_input_budget(
                self.native_anchor,self.native_radius,arb(sigma),self.native_radius/2)
            self.native_budget=(key,budget)

    def analytic_input_budget(self,center,radial_radius,sigma,E_radius):
        base=super().analytic_input_budget(center,radial_radius,sigma,E_radius)
        self.build_native(sigma)
        # Every disk about every allowed centre lies in this native disk.
        distance=(abs(acb(center)-acb(self.native_anchor)).upper()+radial_radius).upper()
        if not distance<self.native_radius:
            raise ValueError("whole working disk leaves the native analytic germ disk")
        q=(distance/self.native_radius).upper()
        outer=self.native_budget[1]
        tail=[(M*q**self.native_order/(1-q)).upper()
              for M in outer["finite_field_bounds"]]
        errors=[(e+t).upper() for e,t in zip(base["field_errors"],tail)]
        finite=[(M+t).upper() for M,t in zip(base["finite_field_bounds"],tail)]
        gap=radial_radius-E_radius
        if not gap>0:raise ValueError("nested physical E Cauchy disks required")
        e1,m1=errors[0]/gap,finite[0]/gap
        result=dict(base,field_errors=errors,finite_field_bounds=finite,
                    E_error=(3*e1*(2*m1+e1)).upper(),
                    E_full_bound=(3*((finite[0]+errors[0])/gap)**2).upper())
        self.last_correlated_budget=dict(
            exact_anchor=ball_record(self.native_anchor),
            exact_scalar_span=list(map(str,self.cell)),
            native_order=self.native_order,
            native_radius=ball_record(self.native_radius),
            whole_working_radius=ball_record(radial_radius),
            enclosing_distance=ball_record(distance),q=ball_record(q),
            actual_finite_outer_moduli=[ball_record(x) for x in outer["finite_field_bounds"]],
            complete_native_Taylor_errors=[ball_record(x) for x in tail],
            original_infinite_Fourier_errors=[ball_record(x) for x in base["field_errors"]],
            combined_errors=[ball_record(x) for x in errors],
            complete_E_error=ball_record(result["E_error"]),
            scope="All real centres in the cell, the full complex working disk, every physical angle, and the shared exact parameter.")
        return result

    def primitive(self,center,direction):
        if self.native_coefficient is None:
            raise ValueError("pay the full correlated budget before primitive evaluation")
        precision=ctx.cap
        if precision>self.native_order:
            raise ValueError("native degree does not cover requested local derivatives")
        z=(acb(center)-acb(self.native_anchor))/self.native_radius
        d=acb(direction)/self.native_radius
        out=np.empty(self.native_coefficient.shape,object)
        for key in np.ndindex(out.shape):
            out[key]=shift_polynomial(self.native_coefficient[key],z,d,precision)
        return out,self.scalars(acb(center),direction)[2]


class CorrelatedOrdinaryGeometry(OrdinarySpanGeometry):
    def __init__(self,object_path,half_width,*,nodes=512,
                 radial_precision=6,angle_precision=10,scale=F(1,1024),
                 native_order=48,native_radius=F(1,128)):
        self.m,self.n=radial_precision,angle_precision
        self.scale=exact_arb(scale)
        self.target=CorrelatedGermTarget(object_path,half_width,nodes,nodes,
            arb(".003"),arb(".0025"),arb(".32"),
            native_order=native_order,native_radius=native_radius)
        self.knots=common_knots(self.target);self.offset=arb(1)
        self._states=OrderedDict()

    def prepare_cell(self,left,right,*,span=None):
        left,right=F(left),F(right)
        if left>right:raise ValueError("reversed ordinary physical interval")
        if span is None:
            i=bisect_right(self.knots,(left+right)/2)-1
            span=self.knots[i],self.knots[i+1]
        if not span[0]<=left<=right<=span[1]:
            raise ValueError("physical radial interval crosses a true scalar knot")
        self.target.set_cell(*span);self.target.set_anchor((left+right)/2)
        self.actual_span=span;self.center=exact_arb(left).union(exact_arb(right))
        old=ctx.cap
        try:
            ctx.cap=max(self.m+3,self.n+3)
            budget=self.target.analytic_input_budget(self.center,arb(".003"),arb(".32"),arb(".0025"))
            coefficient,radius,E,C,K=self.target.target(self.center,self.scale,budget)
            beta,gamma,_,_=self.target.scalars(acb(self.center),-self.scale)
            fees=[(budget["field_errors"][0]*(self.scale/budget["radial_radius"])**j).upper()
                  for j in range(self.m)]
        finally:ctx.cap=old
        self.budget=budget;self.coefficient=coefficient;self.radius=radius
        self.E=E;self.C=C;self.K=K;self.beta=beta;self.gamma=gamma
        self.primitive_fees=fees


def polynomial_height(root_height,offset,scale,m,n,degree=4):
    if root_height.m<degree+1:raise ValueError("missing true root height jets")
    n=min(n,root_height.n)
    w=Jet.constant(-offset/scale,time_precision=m,angle_precision=n)
    w+=Jet.variable("time",time_precision=m,angle_precision=n)
    out=angular_lift(radial_series(root_height,degree),m,n)
    for j in range(degree-1,-1,-1):
        out=out*w+angular_lift(radial_series(root_height,j),m,n)
    return real_jet(out)


def gauged_operator(principal,chart,height,scale):
    B11,B12,B22=[principal[name] for name in ("B11","B12","B22")]
    y,ys,yt,ps,pt,J=[chart[name] for name in ("y","ys","yt","ps","pt","J")]
    B11,B12,B22,y,ys,yt,ps,pt,J,height=align(
        B11,B12,B22,y,ys,yt,ps,pt,J,height)
    if not J.coefficient(0,0).real>0 or not height.coefficient(0,0).real>0:
        raise ValueError("new exact gauge or coordinate Jacobian is not positive")
    invJ=jet_function(J,"inverse")
    A11=real_jet((B11*ys*ys+2*B12*ys*yt+B22*yt*yt)*invJ)
    A12=real_jet((B11*ys*ps+B12*(ys*pt+yt*ps)+B22*yt*pt)*invJ)
    A22=real_jet((B11*ps*ps+2*B12*ps*pt+B22*pt*pt)*invJ)
    h2=height*height
    C11,C12,C22=real_jet(h2*A11),real_jet(h2*A12),real_jet(h2*A22)
    hs,ht=physical_radial_derivative(height,scale),derivative(height,"angle")
    fs=add(mul(B11,hs),mul(B12,ht));ft=add(mul(B12,hs),mul(B22,ht))
    div=add(physical_radial_derivative(fs,scale),derivative(ft,"angle"))
    V=-mul(mul(height,invJ),div)
    return dict(**chart,A11=A11,C11=C11,height=height,
        normal_error=C11-1,cross_error=C12,tangential_error=C22-y,V=V,
        physical_source_factor=real_jet(J*jet_function(height,"inverse")))


def max_fields(values,scale):
    out={}
    for name in ("defining_ratio","ys","pt","J","A11","C11","height",
                 "normal_error","cross_error","tangential_error","V",
                 "physical_source_factor","DB_without_Cphi","DB_Cphi","DC",
                 "LC_normal","LC_angle","LC_potential","LB_normal",
                 "LB_angle","LB_potential"):
        if name in values:
            value=values[name]
            out[name]={"value":ball_record(value.coefficient(0,0).real),
                "physical_theta_derivative_bounds":[
                    ball_record((abs(value.coefficient(0,j).real)*math.factorial(j)).upper())
                    for j in range(min(3,value.n))]}
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--root-certificate",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    p.add_argument("--half-width",type=F,default=F(1,10**9))
    p.add_argument("--radius",type=F,default=F(2423,10000))
    p.add_argument("--radius-half-width",type=F,default=F(1,65536))
    p.add_argument("--angle",type=F,default=F(1,16))
    p.add_argument("--angle-half-width",type=F,default=F(1,2048))
    p.add_argument("--native-order",type=int,default=48)
    p.add_argument("--native-radius",type=F,default=F(1,128))
    p.add_argument("--nodes",type=int,default=512)
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if min(a.radius_half_width,a.angle_half_width)<0:
        raise ValueError("negative local width")
    ctx.prec=a.bits;ctx.cap=32;start=time.monotonic()
    root=FortyTermGeometry(a.object,a.half_width,a.root_certificate,nodes=a.nodes)
    angle=(exact_arb(a.angle)+arb(0,exact_arb(a.angle_half_width)))*arb.pi()
    rp=root.principal(angle,at_root=True)
    coords=FiniteRootCoordinates(rp,root.scale)
    root_values=root_potential_coefficients(rp,root.scale)
    root_chart=coords.positive(arb(0),root.m-1,root.n)
    root_op=ordinary_canonical_operator(rp,root_chart,root.scale)
    root_height=root_op["height"]
    model=CorrelatedOrdinaryGeometry(a.object,a.half_width,nodes=a.nodes,
        native_order=a.native_order,native_radius=a.native_radius)
    model.prepare_cell(a.radius-a.radius_half_width,a.radius+a.radius_half_width)
    principal=model.principal(angle)
    offset=model.center-root.root
    if not offset>0:raise ValueError("ordinary pilot meets an unresolved root")
    chart=coords.positive(offset,model.m-1,model.n)
    direct=ordinary_canonical_operator(principal,chart,model.scale)
    height=polynomial_height(root_height,offset,model.scale,chart["y"].m,chart["y"].n)
    poly=gauged_operator(principal,chart,height,model.scale)
    trial=physical_polynomial_trial(root_values,chart,offset,model.scale)
    dres=trial_residual_coefficients(direct,trial,model.scale)
    pres=trial_residual_coefficients(poly,trial,model.scale)
    output=dict(kind="actual-correlated-wide-collar-and-polynomial-height-local-pilot",
      proved_specified_local_box=True,proved_complete_collar=False,
      source_sha256=sha(__file__),identity=provenance(model.target,a.object),
      root_certificate_sha256=sha(a.root_certificate),
      physical_radial_interval=[str(a.radius-a.radius_half_width),str(a.radius+a.radius_half_width)],
      physical_angle_over_pi_interval=[str(a.angle-a.angle_half_width),str(a.angle+a.angle_half_width)],
      exact_selected_span=list(map(str,model.actual_span)),
      root=ball_record(root.root),positive_offset=ball_record(offset),
      correlated_native_budget=model.target.last_correlated_budget,
      true_normalized_height_gauge=max_fields({**direct,**dres},model.scale),
      degree_four_root_matched_height_gauge=max_fields({**poly,**pres},model.scale),
      root_height_jet=jet_summary(root_height,max_radial=4,max_angle=2,scale=root.scale),
      root_coordinate_degree=6,height_polynomial_degree=4,
      source_pullback="P_ground(tau_* U o Psi)=(J/tau_*) (P_* U) o Psi",
      retained_additional_weak_flux="E11 U_y; cutoff flux norm includes sqrt(C11)",
      limitations=["One continuous physical radial-angle box only.",
        "All recorded angular derivatives are at fixed physical r, not fixed canonical y.",
        "No complete source/contact, outer matching, or feedback inverse follows."],
      dependencies={n:sha(Path("scripts")/n) for n in (
        "fourfold_phase_canonical_collar_far.py","fourfold_phase_canonical_collar_finite.py",
        "fourfold_phase_canonical_collar_bivariate_recovery.py",
        "fourfold_phase_beta_parameter_germ.py","fourfold_phase_beta_interval.py",
        "fourfold_phase_beta_bulk_interval.py")},seconds=time.monotonic()-start)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"local_box_proved":True,"complete_collar":False,
        "source_sha256":sha(__file__),"report_sha256":sha(a.out),
        "V_direct":str(direct["V"].coefficient(0,0)),
        "V_polynomial_height":str(poly["V"].coefficient(0,0)),
        "normal_error":str(poly["normal_error"].coefficient(0,0)),
        "seconds":output["seconds"]}))


if __name__=="__main__":
    main()
