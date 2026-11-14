#!/usr/bin/env python3
"""Small independent checks of the new full reciprocal finite equations."""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
from flint import ctx
from fourfold_codazzi_reciprocal_polynomial_system import ReciprocalPolynomial
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


def relative(x,y):
    # Each radial location gets its own scale: the very large outer gamma
    # must not hide a wrong compact-support parameter column near the waist.
    if np.ndim(x)>1:
        axes=tuple(range(np.ndim(x)-1))
        return float(np.max(np.max(abs(x-y),axis=axes)/(1+np.max(abs(y),axis=axes))))
    return float(np.max(abs(x-y))/(1+np.max(abs(y))))


def direct_curvature_rhs(system,r,y,p):
    """Independent trig synthesis, physical B,C equations, exact chart map."""
    m=system.modes;al=system.alpha
    if al==0:raise ValueError('this independent quotient check uses positive amplitude')
    a,g,b,K,ell,Cr,*_=system.controlled(r,float(p[0]));s=1/Cr
    U=system.sin.T@y[:m];V=system.cos.T@y[m:]
    Ut=system.cos[1:].T@(system.frequency[:,None]*y[:m])
    Vt=-system.sin.T@(system.frequency[:,None]*y[m+1:])
    u=al*U;v=s+al*V;B=u/v;C=1/v
    Bt=al*Ut/v-u*al*Vt/(v*v);Ct=-al*Vt/(v*v)
    A=(K+B*B)/C;At=2*B*Bt/C-A*Ct/C
    Br=g*At-2*b*B;Crhs=g*Bt+b*(A-C)
    sr=b*s*(1-K*s*s)
    ur=(v*Br-u*v*Crhs)/al;vr=(-v*v*Crhs-sr)/al
    out=np.r_[(2/system.angular_grid)*(system.sin@ur),system.proj@vr]
    return out


def audit(system):
    m=system.modes;n=2*m+1;r=np.array([0.,.055,.10,.17,.235,.5,1.5,3.125])
    rng=np.random.default_rng(20261113);y=rng.normal(size=(n,len(r)))*.002
    y[:m]/=(1+np.arange(1,m+1)[:,None])**2
    y[m+1:]/=(1+np.arange(1,m+1)[:,None])**2
    y[m]=.01;y[m+1]+=.03;p=np.array([-.03]);checks=[]
    for al in (0.,.7,.75):
        system.alpha=al;J,Jp=system.jacobian(r,y,p);action=system.full_action(r,y,p)
        delta=rng.normal(size=y.shape);dp=.21
        assembled=np.einsum('ijr,jr->ir',J,delta)+Jp[:,0]*dp
        FFT=action(delta,dp);h=1e-6
        fd=(system.evaluate(r,y+h*delta,p+h*dp)-system.evaluate(r,y-h*delta,p-h*dp))/(2*h)
        fdp=(system.evaluate(r,y,p+h)-system.evaluate(r,y,p-h))/(2*h)
        rhs=system.evaluate(r,y,p)
        trig=None if al==0 else relative(rhs,direct_curvature_rhs(system,r,y,p))
        jl,jr,jp=system.boundary_jac(y[:,0],y[:,-1],p)
        dl=rng.normal(size=n);dr=rng.normal(size=n);dpar=.17
        db=jl@dl+jr@dr+jp[:,0]*dpar
        fdb=(system.boundary(y[:,0]+h*dl,y[:,-1]+h*dr,p+h*dpar)
            -system.boundary(y[:,0]-h*dl,y[:,-1]-h*dr,p-h*dpar))/(2*h)
        tail=system.rhs_tail(r,y,p)
        item=dict(amplitude=al,full_table_Jacobian_vs_independent_FFT=relative(assembled,FFT),
            full_parameter_and_state_Jacobian_vs_finite_difference=relative(fd,assembled),
            parameter_column_alone_per_radial_scale=relative(fdp,Jp[:,0]),
            parameter_column_norm=float(np.max(abs(Jp))),
            all_physical_boundary_rows_vs_finite_difference=relative(fdb,db),
            polynomial_rhs_vs_original_physical_Codazzi=trig,full_cubic_tail=tail)
        item['passed']=bool(item['full_table_Jacobian_vs_independent_FFT']<1e-11
            and item['full_parameter_and_state_Jacobian_vs_finite_difference']<1e-7
            and item['parameter_column_alone_per_radial_scale']<1e-7
            and item['all_physical_boundary_rows_vs_finite_difference']<1e-7
            and (trig is None or trig<1e-10)
            and tail['roundoff_beyond_exact_cubic_support_l1']<1e-10)
        checks.append(item)
    return dict(passed=all(x['passed'] for x in checks),modes=m,angles=system.angular_grid,
        complete_rows=2*m+2,radial_samples=r.tolist(),checks=checks,
        finite_arithmetic_checks_only=True,infinite_PDE_or_cross_type_Cauchy_not_certified=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve the new coordinate checks')
    ctx.prec=192;ctx.cap=6;geometry,definition=load_exact_object(args.object,512)
    body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    system=ReciprocalPolynomial(geometry,8,128,body,graft);result=audit(system)
    result.update(kind='reciprocal_polynomial_full_Jacobian_and_physical_boundary_audit',
        source_sha256=sha(__file__),system_sha256=sha(Path(__file__).with_name('fourfold_codazzi_reciprocal_polynomial_system.py')),
        object_sha256=sha(args.object),wall_seconds=time.monotonic()-started,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_compact_metric_branch_probe.py','fourfold_phase_symmetric_geometry.py',
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_codazzi_rotational_cap_jacobi_probe.py')})
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(result,indent=2),flush=True)
    if not result['passed']:raise ValueError('the new reciprocal Jacobian/boundary check failed')


if __name__=='__main__':main()
