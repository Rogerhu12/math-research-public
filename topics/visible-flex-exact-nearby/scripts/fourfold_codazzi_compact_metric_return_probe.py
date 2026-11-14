#!/usr/bin/env python3
"""Floating m4 sensitivity to explicit compact changes of the radial metric.

E_nu=E*exp(nu*h), with an even C5 polynomial bump supported inside
.05<|r|<.18, a unchanged. The exact waist germ and complete positive cap
are unchanged. These are new metric families, never a fixed-g0 correction.
"""
from __future__ import annotations
import argparse,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_phase_local_correction_probe import sha


SUPPORTS=[('broad','1/20','9/50'),('early','1/20','1/10'),('middle','9/100','7/50'),('late','13/100','9/50')]


def bumps(r):
    r=np.atleast_1d(np.asarray(r,dtype=float));out=np.zeros((len(SUPPORTS),len(r)));derivative=np.zeros_like(out)
    for i,(_,aa,bb) in enumerate(SUPPORTS):
        a,b=float(Fraction(aa)),float(Fraction(bb));s=(abs(r)-a)/(b-a);inside=(s>0)&(s<1);t=s[inside]
        out[i,inside]=4096*t**6*(1-t)**6
        derivative[i,inside]=np.sign(r[inside])*24576*t**5*(1-t)**5*(1-2*t)/(b-a)
    return out,derivative


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--cap',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-cap-Jacobi-floating.json'))
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('refusing to overwrite a metric-control diagnostic')
    cap=json.loads(a.cap.read_text())
    if cap['object_sha256']!=sha(a.object) or cap['endpoint_radius']!=.239:raise ValueError('incompatible true positive-cap reference')
    q4=cap['entries'][0]['q'];geometry,definition=load_exact_object(a.object,512);target=RotationalBodyTarget(geometry)
    count=len(SUPPORTS);calls=0
    def rhs(r,state):
        nonlocal calls
        calls+=1;t=target.point(float(r));gamma,beta,ell=t['gamma'],t['beta'],t['lambda_ref']
        b,c=state[:2];variations=state[2:].reshape(count,2);h,hp=bumps([r]);h,hp=h[:,0],hp[:,0]
        dg=gamma*h/2;dl=(-ell*gamma*gamma*h+beta*hp/2)/(gamma*gamma-beta*beta)
        db,dc=variations[:,0],variations[:,1]
        result=np.empty_like(state);result[:2]=[-2*beta*b+4*gamma*ell*c,4*gamma*b-beta*(ell+1)*c]
        result[2:]=np.column_stack([-2*beta*db+4*gamma*ell*dc+4*(dg*ell+gamma*dl)*c,
            4*gamma*db-beta*(ell+1)*dc+4*dg*b-beta*dl*c]).ravel()
        return result
    sol=solve_ivp(rhs,(0.,.239),np.r_[0.,1.,np.zeros(2*count)],method='DOP853',rtol=2e-11,atol=2e-13,max_step=.00025)
    success=bool(sol.success and np.all(np.isfinite(sol.y)));entries=[]
    sample=np.linspace(.05,.18,521);t=target.values(sample);h,hp=bumps(sample)
    dK=-t['K'][None,:]*h+t['beta'][None,:]*hp/(2*t['E'][None,:])
    if success:
        b,c=sol.y[:2,-1];F=b+q4*c;variations=sol.y[2:,-1].reshape(count,2)
        for j,(label,left,right) in enumerate(SUPPORTS):
            derivative=variations[j,0]+q4*variations[j,1]
            entries.append(dict(label=label,exact_positive_support=[left,right],
                exact_even_bump='h(r)=4096*t^6*(1-t)^6 for t=(|r|-left)/(right-left) in (0,1), zero elsewhere',
                boundary_zero_jets_through_order=5,return_parameter_derivative=float(derivative),
                sampled_Newton_nu=float(-F/derivative) if derivative else None,
                returned_B_derivative=float(variations[j,0]),returned_C_derivative=float(variations[j,1]),
                sampled_max_abs_dK=float(np.max(abs(dK[j]))),sampled_max_abs_h_prime=float(np.max(abs(hp[j])))))
    report=dict(kind='floating_explicit_compact_radial_metric_m4_return_controls',certified=False,success=success,
        source_sha256=sha(__file__),object_sha256=sha(a.object),cap_input_sha256=sha(a.cap),
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],original_fixed_metric_certificates_modified=False,
        family_definition='g_nu=E*exp(nu*h) dr^2+a^2 dtheta^2; each entry is a separate one-parameter family.',
        exact_scalar_formulas=dict(gamma_nu='gamma*exp(nu*h/2)',beta_nu='beta',
            K_nu='exp(-nu*h)*(K+beta*nu*h_prime/(2*E))',
            gamma_derivative_at_zero='gamma*h/2',
            lambda_ref_derivative_at_zero='(-lambda_ref*gamma^2*h+beta*h_prime/2)/(gamma^2-beta^2)'),
        unchanged_exact_regions=['|r|<=1/20','|r|>=9/50, including the entire actual [.239,25/8] cap and its real regular extension'],
        same_initial_curve_and_initial_Frame=True,cap_q4_independent_of_nu=True,
        no_new_target_adopted=True,primitive_nodes=512,rtol=2e-11,atol=2e-13,max_step=.00025,
        requested_interval=[0.,.239],reached_radius=float(sol.t[-1]),rhs_calls=calls,solver_message=sol.message,
        entries=entries,sample_grid_points=len(sample),
        limitations=['Analytic differential of a precisely defined new metric family, integrated only in floating arithmetic.',
            'No directed parameter derivative, root, nonlinear branch or fixed-metric flex follows from this diagnostic.',
            'Existing g0 certificates apply to nu=0; the declared unchanged regions are exact identities, not a transfer of the whole waist continuation.',
            'The reference return is rotational and linear; nonlinear cap, mean, complement and true regular matching remain separate.'],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        wall_seconds=time.monotonic()-start)
    if success:report.update(return_mismatch=float(F),returned_B=float(b),returned_C=float(c),cap_q4=q4)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(dict(success=success,F=report.get('return_mismatch'),entries=entries,wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
