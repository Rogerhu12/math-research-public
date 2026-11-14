#!/usr/bin/env python3
"""R113 correlated curvature numerator with the complete primitive remainder.

The finite polynomial Delta is formed BEFORE taking absolute values.
All Fourier products are zero-padded beyond their exact support. Complete
A0 primitive errors propagate through every product; no finite mode or
angle sample is treated as the true infinite geometry. The angular cells
cover the entire circle. Radial coverage is only the stated exact germs.

This entry was written after the 2026-11-13 executor loss. Numerical
execution must be recorded separately; its existence is not a certificate.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_metric_defect import MetricDefectTarget, save, record
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_bulk_interval import real_interval
from fourfold_phase_beta_bulk_box import (
    Box, CBox, zeros, reduce_box, arb_box, square_box, DirectedFFT)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def component_upper(value):
    return arb(float(np.max(value.magnitude_upper()))).upper()

def box_abs_upper(value):
    return arb(float(np.max(np.maximum(abs(value.lo),abs(value.hi))))).upper()

def sqrt_box_arb(value):
    """Arb roots of the exact binary64 endpoints, not an unverified libm call."""
    if not np.all(value.lo>0):
        raise ValueError("positive square-root gate unresolved")
    lower=np.empty_like(value.lo);upper=np.empty_like(value.hi)
    for index in np.ndindex(value.lo.shape):
        lo=arb(float(value.lo[index]));hi=arb(float(value.hi[index]))
        enclosure=(lo+hi)/2+arb(0,(hi-lo)/2)
        result=arb_box(enclosure.sqrt())
        lower[index]=float(result.lo);upper[index]=float(result.hi)
    return Box(lower,upper)

def range_record(value):
    return dict(lower_bound=record(arb(float(np.min(value.lo)))),
                upper_bound=record(arb(float(np.max(value.hi)))))

class Polynomial:
    """One scalar finite Fourier polynomial plus its full A0 error.

    Coefficients are interval arrays; the represented finite polynomial is
    the exact one from the exact finite tangent DFT. Its Nyquist coefficient
    is structurally zero. Intervals enclose its rounding and parameter/r
    variation. error bounds the TRUE infinite field minus that polynomial.
    """
    def __init__(self, coefficient, error, degree, fft):
        self.c=coefficient
        self.error=arb(error).upper()
        self.degree=int(degree)
        self.fft=fft
        self.grid=len(coefficient.real.lo)
        self._norm=None
        self._nonconstant_samples=None
        if not self.error>=0 or not self.error.is_finite():
            raise ValueError("invalid complete Fourier remainder")
        if not 0<=self.degree<self.grid//2:
            raise ValueError("Fourier support reaches convolution boundary")

    @classmethod
    def constant(cls,value,grid,fft):
        c=zeros((grid,))
        c[0]=CBox.from_acb(acb(value))
        return cls(c,arb(0),0,fft)

    def coerce(self,value):
        if isinstance(value,Polynomial):
            if value.grid!=self.grid or value.fft is not self.fft:
                raise ValueError("different polynomial algebras")
            return value
        return Polynomial.constant(value,self.grid,self.fft)

    def norm(self,derivative=0):
        if derivative==0 and self._norm is not None:return self._norm
        frequencies=np.asarray([k if k<self.grid//2 else k-self.grid
                                for k in range(self.grid)],dtype=float)*4
        weights=abs(frequencies)**derivative
        value=reduce_box(Box(self.c.magnitude_upper())*Box(weights))
        result=arb(float(value.hi)).upper()
        if derivative==0:self._norm=result
        return result

    def samples_without_constant(self):
        if self._nonconstant_samples is None:
            c=CBox(Box(self.c.real.lo.copy(),self.c.real.hi.copy()),
                   Box(self.c.imag.lo.copy(),self.c.imag.hi.copy()))
            c[0]=0
            self._nonconstant_samples=self.fft.fft(c,inverse=True)*self.grid
        return self._nonconstant_samples

    def __add__(self,value):
        value=self.coerce(value)
        return Polynomial(self.c+value.c,self.error+value.error,
                          max(self.degree,value.degree),self.fft)
    __radd__=__add__

    def __neg__(self):
        return Polynomial(-self.c,self.error,self.degree,self.fft)

    def __sub__(self,value):return self+(-self.coerce(value))
    def __rsub__(self,value):return self.coerce(value)+(-self)

    def __mul__(self,value):
        value=self.coerce(value)
        degree=self.degree+value.degree
        if degree>=self.grid//2:
            raise ValueError("aliased finite polynomial product refused")
        a0,b0=self.c[0],value.c[0]
        if self.degree==0:
            coefficient=value.c*a0
        elif value.degree==0:
            coefficient=self.c*b0
        else:
            sa=self.samples_without_constant()
            sb=value.samples_without_constant()
            coefficient=self.fft.fft(sa*sb)/self.grid
            # Constant contributions are evaluated without sending a large
            # constant through the inverse FFT and cancelling it afterwards.
            a=CBox(Box(self.c.real.lo.copy(),self.c.real.hi.copy()),
                   Box(self.c.imag.lo.copy(),self.c.imag.hi.copy()))
            b=CBox(Box(value.c.real.lo.copy(),value.c.real.hi.copy()),
                   Box(value.c.imag.lo.copy(),value.c.imag.hi.copy()))
            a[0]=0;b[0]=0
            coefficient=coefficient+a*b0+b*a0
            coefficient[0]=coefficient[0]+a0*b0
        error=self.norm()*value.error+value.norm()*self.error+self.error*value.error
        return Polynomial(coefficient,error,degree,self.fft)
    __rmul__=__mul__

    def mean(self):
        z=self.c[0].to_acb()
        if not z.imag.contains(0):
            raise ValueError("real geometry mean lost its reality enclosure")
        return z.real+arb(0,self.error)

    def angular_cells(self,angles):
        if angles<self.grid or angles&(angles-1):
            raise ValueError("angle grid must be a power of two >= product grid")
        if angles==self.grid:
            c=self.c
        else:
            c=zeros((angles,))
            frequencies=np.asarray([k if k<self.grid//2 else k-self.grid
                                    for k in range(self.grid)])
            c[frequencies%angles]=self.c
        samples=self.fft.fft(c,inverse=True)*angles
        if not np.all((samples.imag.lo<=0)&(samples.imag.hi>=0)):
            raise ValueError("finite real polynomial angular samples lost reality")
        # Normalized period is 2pi; physical theta has period pi/2.
        half_width=arb.pi()/(4*angles)
        fee=(self.error+half_width*self.norm(1)).upper()
        boxes=samples.pad(arb_box(fee),real_only=True).real
        # Intersect with a second independently valid complete Wiener bound.
        magnitude=arb_box((self.norm()+self.error).upper()).hi
        lo=np.maximum(boxes.lo,-magnitude)
        hi=np.minimum(boxes.hi,magnitude)
        if not np.all(lo<=hi):raise ValueError("inconsistent angular enclosures")
        return Box(lo,hi)

def dot(left,right):
    return sum((a*b for a,b in zip(left,right)),left[0].coerce(0))

def cross(left,right):
    return [left[1]*right[2]-left[2]*right[1],
            left[2]*right[0]-left[0]*right[2],
            left[0]*right[1]-left[1]*right[0]]

class CorrelatedCurvature(MetricDefectTarget):
    def __init__(self,object_path,half_width,nodes,angles):
        super().__init__(object_path,half_width,nodes)
        self.product_grid=8*nodes
        self.curvature_angles=angles or self.product_grid
        self.polynomial_fft=DirectedFFT()

    def lift(self,finite,error):
        c=zeros((self.product_grid,))
        frequency=np.asarray(self.frequency)//4
        c[frequency%self.product_grid]=finite
        # unit_finite_data sets the primitive Nyquist exactly to zero;
        # radial/physical-angle derivatives and the circle constants keep it zero.
        c[(-self.nodes//2)%self.product_grid]=0
        return Polynomial(c,error,self.nodes//2-1,self.polynomial_fft)

    def curvature_budget(self,left,right,ell_mode):
        radial=acb(real_interval(left,right))
        F,Y,a,EF,EY,primitive_tail=self.scalar_jets_and_fourier(radial)
        f=[[self.lift(F[j][:,i],EF[j][0]) for i in range(3)] for j in range(3)]
        y=[[self.lift(Y[j][:,i],EY[j][0]) for i in range(3)] for j in range(2)]
        frequency=np.asarray(self.frequency)
        z=Y[0]*CBox(0.,Box(frequency[:,None]))
        z[:,0]=z[:,0]-Y[0][:,1]
        z[:,1]=z[:,1]+Y[0][:,0]
        ez=(EF[0][2]+2*EF[0][1]+EF[0][0]).upper()
        z=[self.lift(z[:,i],ez) for i in range(3)]

        Epoly=dot(f[1],f[1])
        E1poly=2*dot(f[1],f[2])
        E,E1=Epoly.mean(),E1poly.mean()
        aa=[a[j].to_acb().real for j in range(3)]
        if not E>0 or not aa[0]>0:
            raise ValueError("target metric positivity unresolved")
        K0=-aa[2]/(aa[0]*E)+aa[1]*E1/(2*aa[0]*E*E)
        C=cross(y[0],f[1])
        G=dot(C,C);T=dot(f[0],f[0]);S=dot(C,f[0])
        L=dot(C,f[2]);M=dot(C,y[1]);N=dot(C,z)
        Delta=L*N-M*M-G*G*K0
        fdot=dot(f[0],y[0])
        polys=dict(G=G,T=T,S=S,L=L,M=M,N=N,Delta=Delta,F_dot_Ftheta=fdot)
        if ell_mode=="cap":
            polys.update(F_z=f[0][2],Ftheta_z=y[0][2])
        boxes={name:value.angular_cells(self.curvature_angles)
               for name,value in polys.items()}
        gg,tt,ss,nn=boxes["G"],boxes["T"],boxes["S"],boxes["N"]
        if not all(np.all(v.lo>0) for v in (gg,tt,ss)) or not np.all(nn.hi<0):
            raise ValueError("G/T/S positive or N negative angular gate unresolved")
        delta=boxes["Delta"]
        difference=delta/square_box(gg)
        omega=-tt*delta/(nn*square_box(ss))
        sqrtT=sqrt_box_arb(tt)
        jacobian=ss/(tt*sqrtT)
        angular_norm=arb_box(aa[0]*aa[0])/tt-square_box(boxes["F_dot_Ftheta"])/square_box(tt)
        if not np.all(angular_norm.hi>=0):
            raise ValueError("angular spherical metric enclosure inconsistent")
        angular_norm=Box(np.maximum(0.,angular_norm.lo),angular_norm.hi)
        if ell_mode=="cap":
            if not np.all(boxes["F_z"].lo>0):
                raise ValueError("positive cap ground state unresolved")
            ell=boxes["Ftheta_z"]/boxes["F_z"]-boxes["F_dot_Ftheta"]/tt
        else:
            ell=Box(np.zeros_like(tt.lo))
        magnitude_delta=Box(np.zeros_like(delta.lo),
                           np.maximum(abs(delta.lo),abs(delta.hi)))
        weak=(square_box(tt)*sqrtT*magnitude_delta/((-nn)*ss*ss*ss)
              *(angular_norm+square_box(ell)))
        if not np.all(np.isfinite(weak.hi)):
            raise ValueError("nonfinite weak correction budget")
        return dict(
            exact_radial_interval=list(map(str,(left,right))),
            exact_scalar_germ=list(map(str,self.cell)),
            whole_angular_circle=True,ell_mode=ell_mode,
            angular_cells=self.curvature_angles,
            physical_angular_half_width=record(arb.pi()/(4*self.curvature_angles)),
            target_mean_radial_metric_0_1=[record(E),record(E1)],
            target_K0=record(K0),
            correlated_Delta_A0_upper=record(Delta.norm()+Delta.error),
            correlated_Delta_complete_remainder=record(Delta.error),
            curvature_difference_C0_upper=record(box_abs_upper(difference)),
            omega_C0_upper=record(box_abs_upper(omega)),
            weak_correction_H1_to_Hminus1_upper=record(arb(float(np.max(weak.hi))).upper()),
            spherical_angular_norm_squared=range_record(angular_norm),
            cap_log_ground_state_theta=range_record(ell),
            radial_projection_density=range_record(jacobian),
            geometric_chart_ranges={k:range_record(boxes[k]) for k in ("G","T","S","N")},
            complete_primitive_A_sigma_error=record(primitive_tail),
            finite_support_degree={k:v.degree for k,v in polys.items()},
            complete_polynomial_A0_remainders={k:record(v.error) for k,v in polys.items()},
            limitations=[
                "Only the explicitly declared radial interval, all real theta and parameters.",
                "Weak fee uses |chi|<=1 and exactly the selected core/cap ell; a transition ell must be certified separately.",
                "No strong derivatives, continuous full closed-surface domain, inverse, neighborhood or Newton convergence are asserted."
            ])

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--half-width",type=Fraction,default=Fraction(1,10**9))
    p.add_argument("--nodes",type=int,default=512)
    p.add_argument("--angles",type=int)
    p.add_argument("--points",type=Fraction,nargs="+")
    p.add_argument("--left",type=Fraction)
    p.add_argument("--right",type=Fraction)
    p.add_argument("--ell",choices=("core","cap"),default="core")
    p.add_argument("--bits",type=int,default=192)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec,ctx.cap=args.bits,4
    if args.half_width<0:raise ValueError("parameter half-width must be nonnegative")
    if args.nodes<=0 or args.nodes&(args.nodes-1):raise ValueError("power-of-two nodes required")
    started=time.monotonic()
    definition,_,_,delta=load_definition(args.object)
    target=CorrelatedCurvature(args.object,args.half_width,args.nodes,args.angles)
    common=common_cells(target)
    domains=[(v,v) for v in args.points] if args.points else [(args.left,args.right)]
    if any(a is None or b is None or a>b for a,b in domains):
        raise ValueError("supply points or a valid radial interval")
    doc=dict(kind="actual_R113_correlated_curvature_numerator",complete=False,
        full_radial_domain_complete=False,full_PDE_inverse_complete=False,
        nonlinear_family_complete=False,source_sha256=sha(__file__),
        object_path=str(args.object),object_sha256=sha(args.object),
        origin_sha256=definition["origin_inputs"]["sha256"],
        direction_sha256=definition["direction"]["sha256"],
        exact_center=str(delta),exact_half_width=str(args.half_width),
        exact_parameter_interval=[str(delta-args.half_width),str(delta+args.half_width)],
        primitive_nodes=args.nodes,product_grid=target.product_grid,
        angular_cells=target.curvature_angles,bits=args.bits,ell_mode=args.ell,rows=[])
    save(args.out,doc)
    for left,right in domains:
        index=min(len(common)-2,bisect_right(common,(left+right)/2)-1)
        span=common[index:index+2]
        if not span[0]<=left<=right<=span[1]:
            raise ValueError("requested radial interval crosses an exact scalar germ")
        target.set_cell(*span)
        row=target.curvature_budget(left,right,args.ell)
        doc["rows"].append(row);doc["wall_seconds"]=time.monotonic()-started
        save(args.out,doc)
        print(json.dumps(dict(r=list(map(str,(left,right))),
            K_difference=row["curvature_difference_C0_upper"],
            omega=row["omega_C0_upper"],
            weak=row["weak_correction_H1_to_Hminus1_upper"],
            seconds=doc["wall_seconds"])),flush=True)
    doc.update(complete=True,wall_seconds=time.monotonic()-started,
        dependency_sha256={n:sha(Path(__file__).with_name(n)) for n in (
            "fourfold_phase_metric_defect.py","fourfold_phase_cap_parameter_comparison.py",
            "fourfold_phase_cap_scaled_body.py","fourfold_phase_beta_affine.py",
            "fourfold_phase_beta_parameter_germ.py","fourfold_phase_beta_bulk_interval.py",
            "fourfold_phase_beta_bulk_box.py","fourfold_phase_beta_interval.py",
            "fourfold_phase_root_interval.py","fourfold_phase_uniform_tail.py")})
    save(args.out,doc)

if __name__=="__main__":main()
