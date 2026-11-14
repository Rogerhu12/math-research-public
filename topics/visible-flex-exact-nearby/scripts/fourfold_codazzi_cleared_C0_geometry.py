#!/usr/bin/env python3
"""Use the new complete cleared residual and its own R131 certificate for the true geometry."""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_two_jet_newton_source import record,save,sha
from fourfold_codazzi_piecewise_barrier import read_json,up,down


def parameter(x):
    return Fraction(int(x['numerator']),int(x['denominator'])) if isinstance(x,dict) else Fraction(x)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-Codazzi-cleared-polynomial-r05-v1-native.json.gz'))
    ap.add_argument('--barrier',type=Path,default=Path('notes/2026-11-13-R131-cleared-full-r05-v1-C0-native.json.gz'))
    ap.add_argument('--signs',type=Path,default=Path('notes/2026-11-13-R132-invariant-rectangle-r05-native.json.gz'))
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();ctx.prec=a.bits
    if a.out.exists():raise FileExistsError('refusing to overwrite a geometric certificate')
    native,barrier,signs=map(read_json,(a.native,a.barrier,a.signs))
    if (not native['complete'] or native['failure'] is not None or not barrier['continuation_certified']
        or not barrier['barrier']['passed'] or not signs['continuation_certified']
        or not signs['embedding_certified'] or not down(signs['bounds']['final_Riemann_sign_lower'])>0):
        raise ValueError('actual full PDE/sign certificates are required')
    if (native.get('kind')!='actual_complete_Codazzi_cleared_polynomial_residual_for_R134'
        or barrier.get('kind')!='R131_true_C0_continuation_from_complete_cleared_polynomial_residual'
        or barrier['inputs'].get(str(a.native))!=sha(a.native)
        or not native.get('exact_denominator_clearing') or not native.get('full_target_quadratic_remainder')):
        raise ValueError('new complete cleared native and its actual C0 consumer are required')
    for report in (native,barrier):
        for path,digest in report['inputs'].items():
            if sha(Path(path))!=digest:raise ValueError('frozen native input changed: '+path)
        for name,digest in report['dependencies'].items():
            if sha(Path(__file__).with_name(name))!=digest:raise ValueError('frozen native dependency changed: '+name)
    source_names=((native,'fourfold_codazzi_cleared_polynomial_residual.py'),
        (barrier,'fourfold_codazzi_cleared_C0_continuation.py'),
        (signs,'fourfold_codazzi_invariant_rectangle.py'))
    for report,name in source_names:
        if report['source_sha256']!=sha(Path(__file__).with_name(name)):
            raise ValueError('frozen producer changed: '+name)
    for report in (native,barrier,signs):
        if (not report['whole_real_angular_circle'] or not report['whole_affine_parameter_interval']
            or report['object_sha256']!=native['object_sha256']
            or parameter(report['exact_center_parameter'])!=parameter(native['exact_center_parameter'])
            or Fraction(report['parameter_half_width'])!=Fraction(native['parameter_half_width'])):
            raise ValueError('actual branch/parameter identity mismatch')
    if (native['exact_requested_interval']!=barrier['exact_requested_interval']
        or native['exact_requested_interval']!=signs['exact_positive_interval']):
        raise ValueError('actual geometry domains differ')
    if len(native['rows'])!=len(barrier['barrier']['rows']):
        raise ValueError('actual closed covers differ')
    X=Y=Fh=F=curvature=arb(0)
    a_lower=sqrtE_lower=gap_lower=None
    endpoint=Fraction(0);rows=[]
    for index,(nr,br) in enumerate(zip(native['rows'],barrier['barrier']['rows'])):
        if nr['interval']!=br['interval'] or br['native_row']!=index or not all(br['gates'].values()):
            raise ValueError('actual C0 barrier row invalid')
        left,right=map(Fraction,nr['interval']);h=exact_arb(right-left)
        if left!=endpoint:raise ValueError('noncontiguous closed geometry cover')
        c=nr['true_target_coefficients'];k=up(c['k']);e=up(c['E']).sqrt().upper()
        M=up(br['actual_M']);gap=down(br['actual_gap_lower'])
        if not gap>0:raise ValueError('actual Riemann separation failed')
        A=(k*M).upper();B=k;C=(2*k/gap).upper()
        Fh=(Fh+min(h*e,h*e*X+h*h*e*e*A/2)).upper()
        F=(F+h*e).upper();X=(X+h*e*A).upper();Y=(Y+h*e*B).upper()
        rowcurv=(max(A,C)+B).upper();curvature=max(curvature,rowcurv).upper()
        al=down(c['a']);el=down(c['E']).sqrt().lower()
        a_lower=al if a_lower is None else min(a_lower,al).lower()
        sqrtE_lower=el if sqrtE_lower is None else min(sqrtE_lower,el).lower()
        gap_lower=gap if gap_lower is None else min(gap_lower,gap).lower()
        rows.append(dict(native_row=index,interval=nr['interval'],actual_M=record(M),
            actual_gap_lower=record(gap),A_upper=record(A),B_absolute_upper=record(B),
            C_absolute_upper=record(C),principal_curvature_upper=record(rowcurv),
            horizontal_displacement_accumulated=record(Fh)))
        endpoint=right
    if ['0',str(endpoint)]!=native['exact_requested_interval']:
        raise ValueError('incomplete actual requested geometry domain')
    Nh=(Y+X*X/2).upper()
    support=arb(1)/2;radius=arb(13)/10
    rlo=(support-Fh).lower();rhi=(radius+Fh).upper()
    angular=(support-Fh-radius*Y).lower();normal=(support-Fh-radius*Nh).lower()
    phi=(a_lower*angular/(rhi*rhi)).lower()
    J=(sqrtE_lower*a_lower*normal/(rhi*rhi)).lower()
    gates=dict(positive_horizontal_radius=bool(rlo>0),positive_argument_derivative=bool(phi>0),
        positive_cylindrical_Jacobian=bool(J>0),actual_local_curvature_below_twelve=bool(curvature<12))
    vals=dict(final_C0_error=up(barrier['barrier']['final_C0_barrier']),actual_gap_lower=gap_lower,
        principal_curvature_upper=curvature,full_position_displacement_upper=F,
        horizontal_position_displacement_upper=Fh,X_turn_upper=X,Y_turn_upper=Y,
        horizontal_normal_change_upper=Nh,horizontal_radius_lower=rlo,horizontal_radius_upper=rhi,
        argument_theta_lower=phi,cylindrical_Jacobian_lower=J,
        angular_numerator_lower=angular,horizontal_normal_support_lower=normal)
    out=dict(kind='R132_complete_cleared_C0_curvature_and_true_horizontal_frame',complete=True,
        source_sha256=sha(__file__),bits=a.bits,embedding_certified=all(gates.values()),
        closed_surface_complete=False,object_sha256=native['object_sha256'],
        exact_center_parameter=native['exact_center_parameter'],parameter_half_width=native['parameter_half_width'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,
        exact_positive_interval=native['exact_requested_interval'],reflected_interval=[str(-endpoint),str(endpoint)],
        inputs={str(p):sha(p) for p in (a.native,a.barrier,a.signs)},
        initial_reference_bounds='Same R123/R128 actual waist: support>1/2 and radius<13/10, X0 vertical.',
        rows=rows,gates=gates,bounds={name:record(v) for name,v in vals.items()},
        scope='Same true annulus only; actual C0 comparison and geometric curvature, no derivative-error claim and no closed-surface reach.')
    save(a.out,out)
    print(dict(all_gates=all(gates.values()),rows=len(rows),out=str(a.out)),flush=True)
    for key,value in vals.items():print(key,value.str(15),flush=True)


if __name__=='__main__':main()
