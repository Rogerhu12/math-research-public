#!/usr/bin/env python3
"""Directed finite-part collar for the true fixed-r parameter beta derivative.

Uses H=rho^(7/2) partial_delta J|_r from the physical-parameter note.
No derivative of a moving-root coordinate is substituted for this partial.
The actual coefficient rows and a complete complex disk/angle cover pay
both infinite radial and angular tails. Bulk is a separate requirement.
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
from fourfold_phase_beta_interval import (
    series_constant,array_derivative,vector_dot,vector_cross,add_real_cauchy_error,
    polynomial_disk_bound,primitive_fourier_budget,analytic_tail_derivative,pad_complex,ball_record,
)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_combine import stored_ball
from fourfold_phase_beta_parameter_derivative import ParameterDerivativeTarget,sha,record_budget
from fourfold_phase_beta_parameter_germ import provenance


class Dual:
    """A true first parameter jet; entries may themselves be radial series."""
    __slots__=("v","d")
    def __init__(self,value,derivative=0):
        self.v,self.d=value,derivative
    @staticmethod
    def pair(other):
        return other if isinstance(other,Dual) else Dual(other,0)
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
        return Dual(inverse,-self.d*inverse*inverse)
    def __truediv__(self,other):
        other=self.pair(other)
        value=self.v/other.v
        return Dual(value,(self.d-value*other.d)/other.v)
    def __rtruediv__(self,other):
        return self.pair(other)/self
    def __pow__(self,n):
        if not isinstance(n,int):
            raise TypeError("only integer parameter-jet powers are implicit")
        return Dual(self.v**n,0 if n==0 else n*self.v**(n-1)*self.d)


def geometry(F,X,Frr,Y,Frt,Ftt,K,*,check=False):
    normal=vector_cross(Y,X)
    nr1,nr2=vector_cross(Frt,X),vector_cross(Y,Frr)
    nt1,nt2=vector_cross(Ftt,X),vector_cross(Y,Frt)
    nr,nt=[nr1[k]+nr2[k] for k in range(3)],[nt1[k]+nt2[k] for k in range(3)]
    area2,radius2,support=vector_dot(normal,normal),vector_dot(F,F),vector_dot(normal,F)
    l,m,n=[vector_dot(normal,w) for w in (Frr,Frt,Ftt)]
    if check and any(not z.v.real>0 for z in (area2,radius2,support)):
        raise ValueError("actual complex geometry denominator has no positive real part")
    a,b,c=-n/area2,m/area2,-l/area2
    if check and (not a.v.real>0 or not F[2].v.real>0):
        raise ValueError("actual a or Fz has no positive real part")
    actual_K=(l*n-m*m)/area2**2
    omega,chat=(actual_K-K)/a,(b*b+K)/a
    FX,FY=vector_dot(F,X),vector_dot(F,Y)
    d=(a*(vector_dot(X,X)-FX*FX/radius2)
       +2*b*(vector_dot(X,Y)-FX*FY/radius2)
       +c*(vector_dot(Y,Y)-FY*FY/radius2))/radius2
    lzr=vector_dot(nr,F)/support-vector_dot(normal,nr)/area2-FX/radius2
    lzt=vector_dot(nt,F)/support-vector_dot(normal,nt)/area2-FY/radius2
    ell=Y[2]/F[2]-FY/radius2
    g=-2*lzt
    D=d+omega*(ell*ell+ell*g)
    minima=dict(area2=area2.v,radius2=radius2.v,support=support.v,a=a.v,Fz=F[2].v)
    return a,b,chat,D,lzr,g,minima


def H_expression(rho,q,qrho,Kr,k,kr,geom):
    a,b,chat,D,lzr,g,_=geom
    P=-arb(1)/2-rho*(qrho/(2*q)+2*lzr.v)
    R=-rho*kr/(2*q)-Kr*k/(2*q*q)-2*rho*rho*lzr.d
    N=rho*rho*D.v-(a.v*P*P+2*rho*b.v*P*g.v+rho*rho*chat.v*g.v*g.v)/4
    return (rho**3*D.d-rho*a.d*P*P/4-a.v*P*R/2
            -rho*rho*b.d*P*g.v/2-rho*b.v*R*g.v/2-rho*rho*b.v*P*g.d/2
            -rho**3*chat.d*g.v*g.v/4-rho**3*chat.v*g.v*g.d/2+N*k/(2*q))/q.sqrt()


class ParameterDerivativeCollar(ParameterDerivativeTarget):
    def density_coefficients(self,root,scale,degree,budgets):
        base,change=budgets
        data=self.parameter_target(root,scale,budgets)
        K=data["K"]
        K=acb_series([0]+[K[j] for j in range(1,K.prec)],prec=K.prec)
        q=acb_series([-K[j+1]/scale for j in range(K.prec-1)],prec=K.prec-1)
        qrho=q.derivative()/scale
        k,kr=data["Kd"],data["Kd"].derivative()/(-scale)
        Kr=K.derivative()/(-scale)
        rho=acb_series([0,acb(scale)])
        samples=[]
        for cf,fee in ((data["F"],base),(data["Fd"],change)):
            angular=[]
            for b in range(3):
                rows=self.evaluate(self.angular(cf,b))
                for key in np.ndindex(rows.shape):
                    rows[key]=add_real_cauchy_error(rows[key],fee["field_errors"][b],scale,fee["radial_radius"])
                angular.append(rows)
            F,Y,Ftt=angular
            samples.append((F,array_derivative(F,-scale),array_derivative(F,-scale,2),
                            Y,array_derivative(Y,-scale),Ftt))
        total,expected0=series_constant(0),acb(0)
        for j in range(self.angles):
            fields=[[Dual(samples[0][i][j,c],samples[1][i][j,c]) for c in range(3)] for i in range(6)]
            geom=geometry(*fields,Dual(K,k))
            total+=H_expression(rho,q,qrho,Kr,k,kr,geom)
            expected0+=-5*geom[0].v[0]*k[0]/(32*q[0]*q[0].sqrt())
        mean=total/self.angles
        if mean.prec<=degree:
            raise ValueError("insufficient retained physical derivative coefficients")
        expected0/=self.angles
        difference=mean[0]-expected0
        if not difference.real.contains(0) or not difference.imag.contains(0):
            raise ValueError("independent H0 identity failed")
        coefficients=[(mean[j]/scale**j).real for j in range(degree+1)]
        return coefficients,data,dict(H0=ball_record(coefficients[0]),
                                      H1=ball_record(coefficients[1]),
                                      independent_H0_identity_checked=True)

    def _disk_fields(self,cf,fee,root,scale,R,width):
        R0=fee["radial_radius"]
        errors,finite=primitive_fourier_budget(self.nodes,fee["sigma_normalized_x"],width,R0,
            fee["radius_bound"],fee["height_bound"],fee["tangent_bound"])
        sources=[cf,self.angular(cf),self.angular(cf,2)]
        result={}
        for ar,at in ((0,0),(1,0),(2,0),(0,1),(1,1),(0,2)):
            source=array_derivative(sources[at],-scale,ar)
            angular_fee=[arb(0),arb(0),arb(0)]
            for k in range(self.nodes):
                mode=abs(k if k<self.nodes//2 else k-self.nodes)
                factor=(mode*width).exp()-1
                for c in range(3):
                    angular_fee[c]+=polynomial_disk_bound(source[k,c],R/scale)*factor
            rows=self.evaluate(source)
            tail=analytic_tail_derivative(finite[at],R0,R,cf[0,0].prec,ar)
            infinite=math.factorial(ar)*errors[at]/(R0-R)**ar
            out=np.empty(rows.shape,object)
            for key in np.ndindex(rows.shape):
                out[key]=pad_complex(self.disk_series(rows[key],scale,R),
                                     angular_fee[key[1]]+tail+infinite)
            result[(ar,at)]=out
        return [result[k] for k in ((0,0),(1,0),(2,0),(0,1),(1,1),(0,2))]

    def density_domain(self,root,scale,R,sigma,budgets,data):
        base,change=budgets
        R0,RE=base["radial_radius"],base["E_radius"]
        if not 0<R<RE<R0:
            raise ValueError("root derivative disk radii are not nested")
        width=sigma+arb.pi()/self.angles
        fields0=self._disk_fields(data["F"],base,root,scale,R,width)
        fields1=self._disk_fields(data["Fd"],change,root,scale,R,width)
        gap=R0-RE
        M,Md=base["finite_field_bounds"][0]/gap,change["finite_field_bounds"][0]/gap
        Ef_bounds=[3*M*M,6*M*Md]
        Eseries=[]
        for source,fee,bound in zip((data["Efinite"],data["Edfinite"]),(base,change),Ef_bounds):
            jets=[]
            for order in range(4):
                tail=analytic_tail_derivative(bound,RE,R,source.prec,order)
                infinite=math.factorial(order)*fee["E_error"]/(RE-R)**order
                value=pad_complex(self.disk_series(source,scale,R,order),tail+infinite)
                jets.append((-1)**order*value)
            Eseries.append(acb_series([jets[j]/math.factorial(j) for j in range(4)],prec=4))
        arad=[]
        for source in (data["a"],data["ad"]):
            jets=[(-1)**j*self.disk_series(source,scale,R,j) for j in range(5)]
            arad.append(acb_series([jets[j]/math.factorial(j) for j in range(5)],prec=5))
        a,ad=arad
        E,Ed=Eseries
        C=a.derivative()*E.derivative()-2*a.derivative().derivative()*E
        Cd=(ad.derivative()*E.derivative()+a.derivative()*Ed.derivative()
            -2*ad.derivative().derivative()*E-2*a.derivative().derivative()*Ed)
        K=C/(2*a*E**2)
        Kd=Cd/(2*a*E**2)-K*(ad/a+2*Ed/E)
        q,qrho,Kr,k,kr=K[1],-K[2],K[1],Kd[0],Kd[1]
        if not q.real>0:
            raise ValueError("deflated true target curvature not in positive-real half-plane")
        rho=pad_complex(0,R)
        # Exact K(t)=0 gives K=-rho*q; each q is the segment average of K_r.
        target_K=Dual(-rho*q,k)
        maxima=[]
        minima={key:[] for key in ("area2","radius2","support","a","Fz")}
        for j in range(self.angles):
            fields=[[Dual(fields0[i][j,c],fields1[i][j,c]) for c in range(3)] for i in range(6)]
            geom=geometry(*fields,target_K,check=True)
            value=H_expression(rho,q,qrho,Kr,k,kr,geom)
            if not value.is_finite():
                raise ValueError("nonfinite regularized derivative density")
            maxima.append(abs(value).upper())
            for key,z in geom[-1].items():
                minima[key].append(z.real.lower())
        bound=max(maxima)
        return bound,dict(H_bound=ball_record(bound),normalized_angular_width=ball_record(width),
            deflated_curvature_real_lower=ball_record(q.real.lower()),
            deflated_curvature_real_upper=ball_record(q.real.upper()),
            deflated_curvature_imaginary_absolute_upper=ball_record(abs(q.imag).upper()),
            K_parameter_modulus_upper=ball_record(abs(k).upper()),
            K_radial_parameter_modulus_upper=ball_record(abs(kr).upper()),
            positive_real_minima={key:ball_record(min(values)) for key,values in minima.items()})


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--center-object",type=Path,required=True)
    ap.add_argument("--root-derivative-report",type=Path,required=True)
    ap.add_argument("--center-collar",type=Path,required=True)
    ap.add_argument("--bits",type=int,default=192)
    ap.add_argument("--quarter-nodes",type=int,default=512)
    ap.add_argument("--angles",type=int,default=2048)
    ap.add_argument("--degree",type=int,default=24)
    ap.add_argument("--precision",type=int,default=72)
    ap.add_argument("--radial-radius",default=".0006")
    ap.add_argument("--sigma",default=".02")
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    started=time.monotonic();ctx.prec,ctx.cap=args.bits,args.precision
    root_report=json.loads(args.root_derivative_report.read_text())
    center=json.loads(args.center_collar.read_text())
    core=Path(__file__).with_name("fourfold_phase_beta_parameter_derivative.py")
    if (root_report.get("kind")!="uniform_true_affine_parameter_root_first_derivative"
            or not root_report.get("proved") or root_report["source_sha256"]!=sha(core)
            or root_report["center_object_sha256"]!=sha(args.center_object)
            or not center.get("complete") or center["object_sha256"]!=sha(args.center_object)):
        raise ValueError("root derivative, exact center or finite collar identity differs")
    for name,digest in root_report["dependency_sha256"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("changed root derivative dependency: "+name)
    target=ParameterDerivativeCollar(args.center_object,Fraction(root_report["exact_parameter_half_width"]),
        args.quarter_nodes,args.angles,arb(".003"),arb(".0025"),arb(".32"))
    identity=provenance(target,args.center_object)
    for key in ("origin_inputs_sha256","direction_sha256","exact_center_parameter",
                "exact_parameter_half_width","exact_parameter_interval"):
        if identity[key]!=root_report[key]:
            raise ValueError("parameter family differs: "+key)
    root,cut=stored_ball(root_report["root"]),Fraction(center["fixed_cut"])
    cell=tuple(map(Fraction,root_report["exact_common_span"]))
    if not exact_arb(cell[0])<exact_arb(cut)<root.lower() or not root.upper()<exact_arb(cell[1]):
        raise ValueError("fixed collar is outside the exact common root span")
    target.set_cell(*cell)
    scale=exact_arb(Fraction(1,4096));R=arb(args.radial_radius);sigma=arb(args.sigma)
    eta=root-exact_arb(cut)
    if not 0<eta<R:
        raise ValueError("the entire parameter collar is not inside the Cauchy disk")
    budgets=target.parameter_input_budget(root,arb(".003"),arb(".32"),arb(".0025"))
    coefficients,data,diagnostic=target.density_coefficients(root,scale,args.degree,budgets)
    polynomial=sum((coefficients[j]*eta**(arb(j)-arb(5)/2)/(arb(j)-arb(5)/2)
                    for j in range(args.degree+1)),arb(0))
    identity["source_sha256"]=sha(__file__)
    report=dict(kind="uniform_true_fixed_r_parameter_derivative_collar",complete=False,**identity,
        derivative_core_sha256=sha(core),root_derivative_report_sha256=sha(args.root_derivative_report),
        center_collar_sha256=sha(args.center_collar),root=ball_record(root),fixed_cut=str(cut),
        eta=ball_record(eta),exact_common_span=list(map(str,cell)),
        bits=args.bits,quarter_nodes=args.quarter_nodes,angles=args.angles,
        degree=args.degree,series_precision=args.precision,
        radial_radius=args.radial_radius,sigma=args.sigma,
        coefficients=[ball_record(x) for x in coefficients],coefficient_diagnostics=diagnostic,
        polynomial_finite_part=ball_record(polynomial),
        base_input_budget=record_budget(budgets[0]),derivative_input_budget=record_budget(budgets[1]),
        limitations=["true fixed-r parameter derivative collar only; bulk is still required",
                     "no beta-prime or migration certificate follows from a collar alone"])
    def save():
        report["wall_seconds"]=time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(json.dumps(report,indent=2)+"\n")
    save()
    print(json.dumps(dict(stage="true derivative coefficients",polynomial=polynomial.str(28))),flush=True)
    bound,domain=target.density_domain(root,scale,R,sigma,budgets,data)
    radial=bound*eta**(arb(args.degree)-arb(3)/2)/(
        (arb(args.degree)-arb(3)/2)*R**(args.degree+1)*(1-eta/R))
    angle_mean=2*bound*(-sigma*args.angles).exp()/(1-(-sigma*args.angles).exp())
    angular=2*angle_mean*eta**(-arb(5)/2)/(1-eta/R)
    value=polynomial+arb(0,(radial+angular).upper())
    report.update(complete=True,domain=domain,radial_tail_error=ball_record(radial.upper()),
                  angular_error=ball_record(angular.upper()),derivative_collar_integral=ball_record(value))
    save()
    print(json.dumps(dict(stage="complete true derivative collar",integral=value.str(30),
                          wall_seconds=report["wall_seconds"])),flush=True)


if __name__=="__main__":
    main()

