#!/usr/bin/env python3
"""Ordinary time germs and whole-angle moduli with the exact sine image bound.

The radial displacement bound keeps the zero radial velocity at a turn.
All coefficients still represent the same exact affine infinite R33 graph.
This module supplies geometric inputs; a caller must pay its domain gates,
all required germs, Fourier/time tails, and any true-flow comparison.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,acb_series,ctx

from fourfold_phase_beta_affine import AffineBulkTarget,sha
from fourfold_phase_beta_interval import (
    array_derivative,series_derivative,series_constant,vector_dot,
)
from fourfold_phase_beta_bulk_interval import exact_arb,complex_pad
from fourfold_phase_field_time_taylor import FieldTimeModel,truncate,phase_evaluation
from fourfold_phase_field_time_refined_root import RefinedRoot,prepare_refined_root
from fourfold_phase_field_time_germ_union import radial_cover
from fourfold_phase_time_outer_taylor_gate import frame_invariants


def sine_radial_displacement(root,tau_center,time_halfwidth,time_radius):
    """Uniform on |u|<=R, centered at the identical t*sin(tau_center)."""
    R=time_radius if isinstance(time_radius,arb) else exact_arb(time_radius)
    H=abs(time_halfwidth)*R
    return (abs(root)*(abs(tau_center.sin())*(H.cosh()-1)
                     +abs(tau_center.cos())*H.sinh())).upper()


class SineGermTimeModel(FieldTimeModel):
    """The true ordinary/union time model with its sharp trigonometric image."""
    def __init__(self,object_path,root_certificate,tau_center,time_halfwidth,
                 *,refined_root=None,cell=None,nodes=512,order=40,outer_radius=3,
                 radial_radius=Fraction(3,1000),E_radius=Fraction(1,400),
                 tail_sigma=Fraction(8,25),branch_sign=1):
        if branch_sign not in (-1,1) or order<4:raise ValueError('invalid branch or time order')
        package=refined_root or prepare_refined_root(object_path,root_certificate,nodes=nodes,
            radial_radius=radial_radius,E_radius=E_radius,tail_sigma=tail_sigma)
        if (not isinstance(package,RefinedRoot) or package.object_sha256!=sha(object_path)
            or package.certificate_sha256!=sha(root_certificate)):
            raise ValueError('refined root belongs to another object')
        self.root_package,self.root=package,package.root
        self.order,self.precision=int(order),int(order)+1
        self.work_precision=max(21,self.precision+3);ctx.cap=self.work_precision
        self.object_path,self.root_certificate=Path(object_path),Path(root_certificate)
        self.tau0,self.h=exact_arb(tau_center),exact_arb(time_halfwidth)
        self.outer=exact_arb(outer_radius)
        self.R0,self.RE,self.sigma=map(exact_arb,(radial_radius,E_radius,tail_sigma))
        self.sign,self.nodes=branch_sign,nodes
        if self.h.contains(0) or not self.outer>1 or not self.R0>self.RE>0:
            raise ValueError('invalid nonzero time scale or geometric radii')
        self.target=AffineBulkTarget(object_path,nodes,nodes,self.R0,self.RE,self.sigma)
        if self.target.affine_delta!=package.exact_delta:raise ValueError('root parameter mismatch')
        self.radial_range,_,cells,_=radial_cover(self.target,self.root,tau_center,time_halfwidth)
        if cell is None:
            if len(cells)!=1:raise ValueError('cross-knot interval requires explicit complete germ union')
            self.cell=cells[0]
        else:
            self.cell=tuple(map(Fraction,cell))
            if self.cell not in cells:raise ValueError('chosen germ does not meet the actual radial range')
        self.required_common_cells=cells;self.target.set_cell(*self.cell)
        self.tau=acb_series([acb(self.tau0),acb(self.h)])
        radial=self.root*self.tau.sin();self.center=self.root*self.tau0.sin()
        self.argument=acb_series([0]+[-radial[j]/self.RE for j in range(1,radial.prec)],prec=radial.prec)
        self.radial_image=sine_radial_displacement(self.root,self.tau0,self.h,self.outer)
        if not self.radial_image<self.RE:
            raise ValueError('true sine time image leaves the paid geometric radial disk')
        self.budget=self.target.analytic_input_budget(acb(self.center),self.R0,self.sigma,self.RE)
        coefficient,radius,_,_,K=self.target.target(self.center,self.RE,self.budget)
        beta,gamma,_,_=self.target.scalars(self.center,-self.RE)
        first=array_derivative(coefficient,-self.RE)
        self.X_coefficient=np.empty(first.shape,object)
        for key in np.ndindex(first.shape):self.X_coefficient[key]=truncate(first[key](self.argument),self.precision)
        self.beta=[truncate(v(self.argument),self.precision) for v in beta]
        self.gamma=[truncate(v(self.argument),self.precision) for v in gamma]
        self.beta_r=[truncate(series_derivative(v,-self.RE)(self.argument),self.precision) for v in beta]
        self.gamma_r=[truncate(series_derivative(v,-self.RE)(self.argument),self.precision) for v in gamma]
        self.a=truncate(radius(self.argument),self.precision)
        self.ar=truncate(series_derivative(radius,-self.RE)(self.argument),self.precision)
        self.K=truncate(K(self.argument),self.precision)
        self.r_tau=truncate(self.root*self.tau.cos(),self.precision)
        if not (-self.K[0]).real>0:raise ValueError('negative curvature unresolved at this germ center')


def whole_angle_outer_invariants(model,time_radius,theta_strip):
    """Whole physical-angle invariant moduli on a specified complex-time disk.

No D division or curvature square root is used.  The returned analytic-K
flag concerns the ordinary curvature; root-deflated callers may instead use
their independently proved Q domain.  A false flag does not invalidate D/M/W.
"""
    R,width=exact_arb(time_radius),exact_arb(theta_strip)
    if not R>0 or not width>0:raise ValueError('positive time radius and angle width required')
    old_cap,ctx.cap=ctx.cap,4
    try:
        radial_fee=sine_radial_displacement(model.root,model.tau0,model.h,R)
        radial=complex_pad(acb(model.center),radial_fee)
        theta=acb(arb(0,(arb.pi()/4).upper()),arb(0,width.upper()))
        budget=model.target.analytic_input_budget(radial,model.R0,model.sigma,model.RE)
        coefficient,radius=model.target.primitive(radial,1)
        beta,gamma,_,height=model.target.scalars(radial,1)
        phases=phase_evaluation([v[0] for v in beta],[v[0] for v in gamma],
            [v[1] for v in beta],[v[1] for v in gamma],theta)
        angular_width=(4*abs(theta.imag)).upper()
        if not angular_width<model.sigma:raise ValueError('whole angle strip leaves the paid Fourier domain')
        choices=[]
        for sf in (Fraction(1,8),Fraction(4,25),Fraction(1,5),Fraction(8,25),Fraction(1,2)):
            sigma=exact_arb(sf)
            if not sigma>angular_width:continue
            imaginary_phase,radial_phase=arb(0),arb(0)
            for k in range(model.target.modes):
                sh,ch=(sigma*(k+1)).sinh(),(sigma*(k+1)).cosh()
                for phase in (beta,gamma):
                    imaginary_phase+=abs(phase[k][0].real)*sh+abs(phase[k][0].imag)*ch
                    radial_phase+=abs(phase[k][1])*ch
            source=((abs(radius[1])+abs(radius[0])*radial_phase)*imaginary_phase.exp()).upper()
            decay=(-(sigma-angular_width)).exp();logarithm=-(1-decay).log()
            horizontal=(2*source*logarithm/3).upper()
            choices.append((sf,source,[(source+horizontal).upper(),horizontal,
                                      (abs(height[1])+source*logarithm/2).upper()]))
        if not choices:raise ValueError('no true primitive Fourier decay strip is available')
        selected=[min(choices,key=lambda row:float(row[2][j])) for j in range(3)]
        Xbounds=[selected[j][2][j] for j in range(3)]
        X=[complex_pad(acb(0),value) for value in Xbounds]
        rows=frame_invariants(X,radius[0],radius[1],*phases)
        bounds={key:abs(value).upper() for key,value in rows.items()}
        first=array_derivative(coefficient)
        Efinite=sum((vector_dot(first[k],first[(-k)%model.nodes]) for k in range(model.nodes)),series_constant(0))
        E=[complex_pad(Efinite[j],budget['E_error']/model.RE**j) for j in range(2)]
        analytic_K=bool(radius[0].abs_lower()>0 and E[0].abs_lower()>0);Kbound=None
        if analytic_K:
            K=(radius[1]*E[1]-4*radius[2]*E[0])/(2*radius[0]*E[0]**2)
            analytic_K=bool(K.is_finite())
            if analytic_K:Kbound=abs(K).upper()
        info=dict(radial_displacement=radial_fee,physical_theta_strip=width,
            true_X_radial_component_modulus=Xbounds[0],true_X_azimuthal_component_modulus=Xbounds[1],
            true_X_vertical_component_modulus=Xbounds[2],radius_modulus_lower=radius[0].abs_lower(),
            E_modulus_lower=E[0].abs_lower(),E_infinite_error=budget['E_error'])
        for j,name in enumerate(['radial','azimuthal','vertical']):
            info['true_X_'+name+'_decay_strip']=exact_arb(selected[j][0])
        return bounds,Kbound,analytic_K,info
    finally:
        ctx.cap=old_cap
