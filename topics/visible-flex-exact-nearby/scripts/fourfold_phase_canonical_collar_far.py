#!/usr/bin/env python3
"""Extend the same finite canonical chart through actual positive scalar spans.

This is an actual-germ local diagnostic, not a global cover or source norm.
The polynomial root coordinates are evaluated at r-t.  Geometry away from
the root is regenerated from the true scalar polynomial on the exact span;
no analytic continuation of the root spline germ is used there.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from collections import OrderedDict
from fractions import Fraction
import json
from pathlib import Path
import time
from flint import acb, arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_parameter_germ import ParameterGermBulkTarget, provenance
from fourfold_phase_canonical_collar_centered import CenteredPhysicalRootGeometry
from fourfold_phase_canonical_collar_finite import (
    PhysicalRootGeometry, FiniteRootCoordinates, finite_canonical_operator,
    physical_polynomial_trial, root_potential_coefficients,
    trial_residual_coefficients, jet_summary, sha,
    align, jet_function, physical_radial_derivative, derivative, add, mul)
from fourfold_phase_canonical_root_jets import real_jet
from fourfold_phase_root_potential_complex_strip import ComplexRootModel


def common_knots(target):
    splines=[target.raw,target.raw_direction,target.base,target.shift,
             *target.means,*target.height_integrals]
    return sorted(set(abs(Fraction.from_float(float(v))) for spline in splines
                      for v in spline.knots_float))


class OrdinarySpanGeometry(PhysicalRootGeometry):
    def __init__(self, object_path, half_width, *, nodes=512,
                 radial_precision=6, angle_precision=8, scale=Fraction(1,1024)):
        self.m,self.n=radial_precision,angle_precision
        self.scale=exact_arb(scale)
        self.target=ParameterGermBulkTarget(object_path,half_width,nodes,nodes,
                                          arb('.003'),arb('.0025'),arb('.32'))
        self.knots=common_knots(self.target)
        self.offset=arb(1)
        # A state contains the complete native Fourier primitive.  Keeping
        # every adaptive radial slab alive is unnecessary and can exhaust
        # memory.  Eviction changes no interval calculation.
        self._states=OrderedDict()

    def phases(self, angle):
        beta,gamma=ComplexRootModel.complex_phases(self,acb(angle))
        return real_jet(beta),real_jet(gamma)

    def prepare_cell(self, left, right, *, span=None):
        left,right=Fraction(left),Fraction(right)
        if left>right:
            raise ValueError('reversed actual ordinary radial interval')
        if span is None:
            i=bisect_right(self.knots,(left+right)/2)-1
            span=self.knots[i],self.knots[i+1]
        if not span[0] <= left <= right <= span[1]:
            raise ValueError('actual radial input crosses a scalar span')
        self.target.set_cell(*span)
        self.actual_span=span
        self.center=exact_arb(left).union(exact_arb(right))
        key=(span,left,right,ctx.prec)
        if key in self._states:
            self._states.move_to_end(key)
            for name,value in self._states[key].items():
                setattr(self,name,value)
            return
        old,ctx.cap=ctx.cap,max(self.m+3,self.n+3)
        try:
            budget=self.target.analytic_input_budget(self.center,arb('.003'),arb('.32'),arb('.0025'))
            coefficient,radius,E,C,K=self.target.target(self.center,self.scale,budget)
            beta,gamma,_,_=self.target.scalars(acb(self.center),-self.scale)
            fees=[(budget['field_errors'][0]*(self.scale/budget['radial_radius'])**j).upper()
                  for j in range(self.m)]
        finally:
            ctx.cap=old
        state=dict(budget=budget,coefficient=coefficient,radius=radius,E=E,C=C,K=K,
                   beta=beta,gamma=gamma,primitive_fees=fees)
        self._states[key]=state
        while len(self._states)>4:
            self._states.popitem(last=False)
        for name,value in state.items():
            setattr(self,name,value)


def ordinary_canonical_operator(principal, chart, scale):
    """The exact R87 operator, without its root high-jet width heuristic.

    Positivity of the two denominators is still mandatory.  This routine
    returns ordinary values and angular jets only; it does not claim any
    root division order or global radial analyticity.
    """
    y,ys,yt,ps,pt,J=[chart[name] for name in ('y','ys','yt','ps','pt','J')]
    B11,B12,B22=[principal[name] for name in ('B11','B12','B22')]
    B11,B12,B22,y,ys,yt,ps,pt,J=align(B11,B12,B22,y,ys,yt,ps,pt,J)
    if not J.coefficient(0,0).real>0:
        raise ValueError('ordinary coordinate Jacobian not positive')
    invJ=jet_function(J,'inverse')
    A11=real_jet((B11*ys*ys+2*B12*ys*yt+B22*yt*yt)*invJ)
    A12=real_jet((B11*ys*ps+B12*(ys*pt+yt*ps)+B22*yt*pt)*invJ)
    A22=real_jet((B11*ps*ps+2*B12*ps*pt+B22*pt*pt)*invJ)
    if not A11.coefficient(0,0).real>0:
        raise ValueError('ordinary principal normal coefficient not positive')
    invA11=jet_function(A11,'inverse')
    height=real_jet(jet_function(jet_function(A11,'log')*(-arb(1)/2),'exp'))
    C12,C22=real_jet(A12*invA11),real_jet(A22*invA11)
    hs,ht=physical_radial_derivative(height,scale),derivative(height,'angle')
    fs=add(mul(B11,hs),mul(B12,ht))
    ft=add(mul(B12,hs),mul(B22,ht))
    div=add(physical_radial_derivative(fs,scale),derivative(ft,'angle'))
    V=-mul(mul(height,invJ),div)
    source=real_jet(J*jet_function(height,'inverse'))
    return dict(**chart,A11=A11,height=height,cross_error=C12,
                tangential_error=C22-y,V=V,physical_source_factor=source)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--root-certificate',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json'))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,2500000))
    ap.add_argument('--radius',type=Fraction,default=Fraction(2423,10000))
    ap.add_argument('--radius-half-width',type=Fraction,default=Fraction(0))
    ap.add_argument('--angle',type=Fraction,default=Fraction(1,16))
    ap.add_argument('--angle-half-width',type=Fraction,default=Fraction(0))
    ap.add_argument('--nodes',type=int,default=512)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if min(args.radius_half_width,args.angle_half_width)<0:
        raise ValueError('negative diagnostic half-width')
    ctx.prec,ctx.cap=args.bits,32
    start=time.monotonic()
    root=CenteredPhysicalRootGeometry(args.object,args.half_width,args.root_certificate,nodes=args.nodes)
    model=OrdinarySpanGeometry(args.object,args.half_width,nodes=args.nodes)
    model.prepare_cell(args.radius-args.radius_half_width,args.radius+args.radius_half_width)
    angle=(exact_arb(args.angle)+arb(0,exact_arb(args.angle_half_width)))*arb.pi()
    rp=root.principal(angle,at_root=True)
    coordinates=FiniteRootCoordinates(rp,root.scale)
    root_values=root_potential_coefficients(rp,root.scale)
    actual=model.principal(angle)
    offset=model.center-root.root
    if not offset>0:
        raise ValueError('ordinary positive diagnostic does not stay beyond every actual root')
    chart=coordinates.positive(offset,model.m-1,model.n)
    values=finite_canonical_operator(actual,chart,model.scale)
    amplitudes=physical_polynomial_trial(root_values,chart,offset,model.scale)
    residual=trial_residual_coefficients(values,amplitudes,model.scale)
    report=dict(kind='actual_finite_chart_across_true_ordinary_scalar_spans_diagnostic',
      proved_global_cover=False,source_sha256=sha(__file__),object=provenance(model.target,args.object),
      root_certificate_sha256=sha(args.root_certificate),root=ball_record(root.root),
      actual_radial_interval=[str(args.radius-args.radius_half_width),str(args.radius+args.radius_half_width)],
      exact_selected_common_span=list(map(str,model.actual_span)),
      physical_positive_offset=ball_record(offset),physical_angle=ball_record(angle),
      dependencies={name:sha(Path(__file__).parent/name) for name in (
        'fourfold_phase_canonical_collar_centered.py','fourfold_phase_canonical_collar_finite.py',
        'fourfold_phase_root_potential_complex_strip.py','fourfold_phase_beta_parameter_germ.py',
        'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_interval.py')},
      operator_jet_bounds={name:jet_summary(v,max_radial=0,max_angle=2,scale=model.scale)
                           for name,v in values.items()},
      trial_residual_jet_bounds={name:jet_summary(v,max_radial=0,max_angle=2,scale=model.scale)
                               for name,v in residual.items()},seconds=time.monotonic()-start)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'seconds':report['seconds'],'Jacobian':str(values['J'].coefficient(0,0)),
                      'y_over_s':str(values['defining_ratio'].coefficient(0,0)),
                      'V':str(values['V'].coefficient(0,0))}),flush=True)


if __name__=='__main__':
    main()
