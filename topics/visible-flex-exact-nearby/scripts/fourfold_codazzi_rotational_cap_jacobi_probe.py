#!/usr/bin/env python3
"""Floating Jacobi Riccati probe on the actual body and actual natural graft.

The regular initial value is the stable-center representative; the true
R74 exponentially small non-fourth-mode fee is explicitly not propagated
by this floating diagnostic. The separate native producer pays that fee.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
from numpy.polynomial import Polynomial
from scipy.integrate import solve_ivp
from flint import ctx
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget,primitive_difference
from fourfold_phase_cap_graft_tail_energy import ExactGraftPoint
from fourfold_phase_local_correction_probe import sha


class RotationalGraftTarget:
    def __init__(self,geometry,object_path):
        self.geometry=geometry;g=ExactGraftPoint(object_path);self.actual=g
        def mids(series,n):return [float(series[j].real.mid()) for j in range(n)]
        l=mids(g.entry['log_radius'],5);h=mids(g.entry['slope_ratio'],4)
        s=Polynomial([0.,1.]);u=8*s
        chi=(1-u)**5*(1+5*u+15*u*u+35*u**3+70*u**4)
        self.loga=Polynomial(l[:2])+chi*Polynomial([0.,0.,*l[2:]])
        self.H=Polynomial([h[0]])+chi*Polynomial([0.,*h[1:]])
        self.phases=[]
        for rows in (g.beta_normalized,g.gamma_normalized):
            self.phases.append([chi*Polynomial([float(x.mid()) for x in row]) for row in rows])
        self.omega=-l[1]/(4*h[0]);self.a_endpoint=np.exp(self.loga(.125))

    def point(self,r):
        if not 3<=r<=3.125:raise ValueError('outside actual natural graft')
        s=r-3;L=self.loga.deriv()(s);Lp=self.loga.deriv(2)(s);a=np.exp(self.loga(s));H=self.H(s);Hp=self.H.deriv()(s)
        phase=np.zeros((3,1,self.geometry.modes,2))
        for component,power in enumerate((3,2)):
            for j,poly in enumerate(self.phases[component]):
                u=poly(s);ur=poly.deriv()(s);urr=poly.deriv(2)(s);weight=a**power
                phase[:,0,j,component]=[weight*u,weight*(ur+power*L*u),
                    weight*(urr+2*power*L*ur+(power*power*L*L+power*Lp)*u)]
        p=primitive_difference(self.geometry,phase)[:,0]
        u=L*p[0]+p[1];ur=Lp*p[0]+L*p[1]+p[2];rev=(-np.arange(self.geometry.nodes))%self.geometry.nodes
        e=(2*L*u[0,0]+np.sum(u*u[rev])).real
        er=(2*Lp*u[0,0]+2*L*ur[0,0]+2*np.sum(u*ur[rev])).real
        Ebar=L*L+a*a*H*H+e;R=H*H+e/(a*a)
        K=(H*H*(L*L-Lp)+L*H*Hp+(L*er-2*Lp*e)/(2*a*a))/Ebar**2
        if min(Ebar,R,K)<=0:raise ValueError('floating actual graft chart failed')
        Cref=-np.sqrt(R/Ebar)
        return dict(r=r,a=a,beta=L,gamma=np.sqrt(Ebar),K=K,Cref=Cref,lambda_ref=K/Cref**2)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--endpoint',type=Path,default=Path('notes/2026-11-13-codazzi-to-r0239-n1024-endpoint-floating.npz'))
    ap.add_argument('--modes',type=int,default=16);ap.add_argument('--nodes',type=int,default=512)
    ap.add_argument('--left',type=float,default=.239);ap.add_argument('--rtol',type=float,default=2e-10)
    ap.add_argument('--atol',type=float,default=2e-12);ap.add_argument('--max-step',type=float,default=.005)
    ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();ctx.prec=192;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('refusing to overwrite a diagnostic')
    g,definition=load_exact_object(a.object,a.nodes);body=RotationalBodyTarget(g);graft=RotationalGraftTarget(g,a.object)
    def target(r):return body.point(r) if r<=3 else graft.point(r)
    m=4*np.arange(1,a.modes+1);initial=1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)
    calls=0
    def rhs(r,q):
        nonlocal calls
        t=target(float(r));calls+=1
        return m*t['gamma']*(q*q-t['lambda_ref'])+t['beta']*(t['lambda_ref']-1)*q
    solution=solve_ivp(rhs,(3.125,a.left),np.full(a.modes,initial),method='DOP853',
        rtol=a.rtol,atol=a.atol,max_step=a.max_step,dense_output=True)
    if not solution.success or not np.all(np.isfinite(solution.y)):
        failed=dict(kind='floating_actual_body_graft_rotational_Jacobi_probe',certified=False,success=False,
            source_sha256=sha(__file__),object_sha256=sha(a.object),message=solution.message,
            reached_radius=float(solution.t[-1]),requested_left=a.left,finite_state=bool(np.all(np.isfinite(solution.y))),
            rhs_calls=calls,wall_seconds=time.monotonic()-started)
        a.out.write_text(json.dumps(failed,indent=2,allow_nan=False)+'\n');print(failed,flush=True);return
    data=np.load(a.endpoint,allow_pickle=False);meta=json.loads(str(data['metadata']));r=float(data['r'])
    if meta['object_sha256']!=sha(a.object) or r<a.left or r>3.125:raise ValueError('invalid endpoint identity/domain')
    q=solution.sol(r);state=data['state'];t=target(r)
    bc=np.fft.fft(state[:,:2],axis=0)/len(state);b=-2*bc[1:a.modes+1,0].imag;c=2*bc[1:a.modes+1,1].real
    mismatch=b+q*c
    entries=[dict(physical_frequency=int(f),q=float(qq),B_sine_over_C_cosine=float(-qq),
        candidate_B_sine=float(bb),candidate_C_nonmean_cosine=float(cc),
        rotational_linear_graph_mismatch=float(rr)) for f,qq,bb,cc,rr in zip(m,q,b,c,mismatch)]
    join_left,join_right=body.point(3.),graft.point(3.)
    join={name:join_right[name]-join_left[name] for name in ('gamma','beta','K','Cref','lambda_ref')}
    report=dict(kind='floating_actual_body_graft_rotational_Jacobi_probe',certified=False,
        source_sha256=sha(__file__),object_sha256=sha(a.object),endpoint_sha256=sha(a.endpoint),
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],success=bool(solution.success),message=solution.message,
        requested_interval=[a.left,3.125],primitive_nodes=a.nodes,modes=a.modes,physical_frequencies=m.tolist(),
        rtol=a.rtol,atol=a.atol,max_step=a.max_step,rhs_calls=calls,accepted_steps=len(solution.t)-1,
        actual_graft_used=True,body_spline_extrapolation_used=False,body_graft_float_join_mismatch=join,
        actual_omega_center=graft.omega,actual_graft_end_radius=graft.a_endpoint,stable_center_initial_q=initial,
        true_R74_nonfourth_mode_initial_fee='<=2^42 exp(-2m omega_lower*(2^24-25/8)); NOT propagated in this floating run',
        endpoint_radius=r,endpoint_reference=t,entries=entries,
        candidate_B_mean=float(bc[0,0].real),candidate_C_mean=float(bc[0,1].real),
        candidate_C_mean_minus_Cref=float(bc[0,1].real-t['Cref']),
        omitted_candidate_B_C_DFT_l1=np.sum(abs(bc[abs(np.fft.fftfreq(len(state),1/len(state)))>a.modes,:]),axis=0).tolist(),
        finite_mismatch_l1=float(np.sum(abs(mismatch))),
        mean_height_port='Separate regular axial translation; no forced mean contact computed.',
        nonlinear_remainder='Not paid: A-Aref+lambda_ref*(C-Cref)=B^2/C+K*(C-Cref)^2/(C*Cref^2).',
        limitations=['Floating finite-primitive scalar coefficients and unvalidated radial ODE integration.',
            'The initial stable-center representative differs from the true non-fourth-mode regular line by the recorded tiny fee; the independent native run pays it.',
            'The displayed mismatch is against the rotational LINEAR graph, not the unknown nonlinear cap map.',
            'All omitted high channels and the candidate mean difference remain unclosed.'],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_phase_cap_graft_tail_energy.py',
            'fourfold_phase_natural_exterior_graft.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        wall_seconds=time.monotonic()-started)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(dict(success=solution.success,rhs_calls=calls,entries=entries[:4],finite_mismatch_l1=report['finite_mismatch_l1'],
        wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
