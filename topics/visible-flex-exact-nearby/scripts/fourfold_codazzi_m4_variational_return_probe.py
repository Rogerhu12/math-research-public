#!/usr/bin/env python3
"""Floating analytic variational m4 waist/regular return for g_delta.

The parameter differential is applied to the actual scalar primitives and
natural graft, then integrated as a separate ODE state. It is diagnostic,
not a directed derivative or a replacement for a fixed-metric certificate.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from flint import ctx
from fourfold_phase_symmetric_geometry import load_exact_object,SymmetricAffineGeometry
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_codazzi_rotational_target_parameter import RotationalTargetParameter
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--rtol',type=float,default=2e-11);ap.add_argument('--atol',type=float,default=2e-13)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6
    if a.out.exists():raise FileExistsError('refusing to overwrite a variational diagnostic')
    geometry,definition=load_exact_object(a.object,512);target=RotationalTargetParameter(geometry)
    body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,a.object)
    h=1e-5
    minus=RotationalTargetParameter(SymmetricAffineGeometry(geometry.frozen,geometry.direction,geometry.delta-h,512))
    plus=RotationalTargetParameter(SymmetricAffineGeometry(geometry.frozen,geometry.direction,geometry.delta+h,512))
    audits=[]
    for r in [0.,.05,.239,.8,1.5,2.99,3.,3.0625,3.125]:
        value,dvalue=target.point(r);reference=body.point(r) if r<=3 else graft.point(r)
        vm,_=minus.point(r);vp,_=plus.point(r)
        audit=dict(r=r,independent_reference_value_difference={},parameter_derivative={},coefficient_central_secant={},derivative_minus_secant={})
        for k in ('a','beta','gamma','K','Cref','lambda_ref'):
            fd=(vp[k]-vm[k])/(2*h)
            audit['independent_reference_value_difference'][k]=value[k]-reference[k]
            audit['parameter_derivative'][k]=dvalue[k];audit['coefficient_central_secant'][k]=fd
            audit['derivative_minus_secant'][k]=dvalue[k]-fd
        audits.append(audit)
    counts=[0,0];qstar,dqstar=target.regular_q4_pair()
    def cap_rhs(r,y):
        counts[0]+=1;t,dt=target.point(float(r));q,dq=y
        g,b,l=t['gamma'],t['beta'],t['lambda_ref'];dg,db,dl=dt['gamma'],dt['beta'],dt['lambda_ref']
        f=4*g*(q*q-l)+b*(l-1)*q
        df=(8*g*q+b*(l-1))*dq+4*dg*(q*q-l)-4*g*dl+db*(l-1)*q+b*dl*q
        return [f,df]
    cap=solve_ivp(cap_rhs,(3.125,.239),[qstar,dqstar],method='DOP853',rtol=a.rtol,atol=a.atol,max_step=.005)
    def waist_rhs(r,y):
        counts[1]+=1;t,dt=target.point(float(r));b,c,db,dc=y
        g,v,l=t['gamma'],t['beta'],t['lambda_ref'];dg,dv,dl=dt['gamma'],dt['beta'],dt['lambda_ref']
        return [-2*v*b+4*g*l*c,4*g*b-v*(l+1)*c,
                -2*v*db+4*g*l*dc-2*dv*b+4*(dg*l+g*dl)*c,
                4*g*db-v*(l+1)*dc+4*dg*b-(dv*(l+1)+v*dl)*c]
    waist=solve_ivp(waist_rhs,(0.,.239),[0.,1.,0.,0.],method='DOP853',rtol=a.rtol,atol=a.atol,max_step=.00025)
    finite=bool(np.all(np.isfinite(cap.y)) and np.all(np.isfinite(waist.y)))
    success=bool(cap.success and waist.success and finite)
    report=dict(kind='floating_analytic_parameter_variation_of_actual_m4_return',certified=False,success=success,
        source_sha256=sha(__file__),object_sha256=sha(a.object),exact_center_parameter=definition['delta_fraction'],
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        metric_parameter_direction_not_a_fixed_metric_isometry=True,original_fixed_metric_certificates_modified=False,
        primitive_nodes=512,rtol=a.rtol,atol=a.atol,cap_max_step=.005,waist_max_step=.00025,
        cap_calls=counts[0],waist_calls=counts[1],cap_message=cap.message,waist_message=waist.message,
        cap_reached_radius=float(cap.t[-1]),waist_reached_radius=float(waist.t[-1]),
        exact_finite_formula_parameter_differential=True,actual_natural_graft_differentiated=True,
        regular_q4_initial=qstar,regular_q4_initial_derivative=dqstar,
        point_audit_secant_step=h,point_audits=audits,
        point_audit_scope='The independent center value provider uses the old exact-graft Arb constructor; coefficient secants are only a check of the analytic finite-formula differential.',
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_rotational_target_parameter.py','fourfold_phase_codazzi_rotational_reference_probe.py',
            'fourfold_codazzi_rotational_cap_jacobi_probe.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        limitations=['Floating finite primitive and unvalidated ODE, even though the differential formulas are analytic.',
            'The derivative belongs to the separate metric family g_delta, not to a deformation preserving the already fixed g0.',
            'No sign, interval root, nonlinear bifurcation or regular/full-cap inverse is certified.'],
        wall_seconds=time.monotonic()-started)
    if success:
        q,dq=cap.y[:,-1];b,c,db,dc=waist.y[:,-1];F=b+q*c;dF=db+dq*c+q*dc
        predicted=geometry.delta-F/dF if dF else None
        report.update(cap_q4=float(q),cap_q4_derivative=float(dq),returned_B=float(b),returned_C=float(c),
            returned_B_derivative=float(db),returned_C_derivative=float(dc),return_mismatch=float(F),
            return_parameter_derivative=float(dF),sampled_Newton_delta=float(predicted) if predicted is not None else None,
            sampled_Newton_shift=float(-F/dF) if dF else None)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print({k:report[k] for k in ('success','return_mismatch','return_parameter_derivative','sampled_Newton_shift','wall_seconds') if k in report},flush=True)


if __name__=='__main__':main()
