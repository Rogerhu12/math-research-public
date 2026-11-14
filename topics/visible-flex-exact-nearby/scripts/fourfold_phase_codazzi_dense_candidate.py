#!/usr/bin/env python3
"""Produce a complete piecewise-polynomial/Fourier B,C candidate in r.

The numerical producer is FLOATING. The saved candidate itself has an exact
finite definition: all stored binary64 coefficients are dyadic; negative
Fourier coefficients are conjugates; mode zero is real; Nyquist is zero.
Each degree-seven time polynomial has shared endpoint coefficients, hence
the candidate and every theta derivative are exactly continuous at joins.
No accuracy, PDE residual, infinite-solution or whole-eta bound is asserted.

For one piece x=(r-left)/(right-left), with endpoint vectors L,R and stored
F1,...,F6, its coefficient polynomial is
 (1-x)L+xR+x(1-x)[F1+x(F2+(1-x)(F3+x(F4+(1-x)(F5+x F6)))))].
The dense-output F0 is replaced by the exact endpoint difference. This pays
no hidden join discontinuity. Radial first derivatives may jump at joins;
residual bounds are to be applied piecewise/integrally.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip,io,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853

from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_local_correction_probe import sha,scalar_target
from fourfold_phase_codazzi_evolution_probe import resample,scalar_derivative


def positive_hermitian(values):
    N=len(values);raw=np.fft.fft(values,axis=0)/N
    pos=np.zeros((N//2,values.shape[1]),complex);pos[0]=raw[0].real
    for k in range(1,N//2):pos[k]=(raw[k]+np.conj(raw[-k]))/2
    return pos


def full_coefficients(pos,N):
    out=np.zeros((N,pos.shape[-1]),complex);out[:len(pos)]=pos
    out[(-np.arange(1,len(pos)))%N]=np.conj(pos[1:])
    return out


def polynomial_jet(left,right,correction,x):
    """Coefficient value and d/dx; algebraic formula also usable with boxes."""
    value=correction[5];derivative=np.zeros_like(value)
    for j in range(4,-1,-1):
        factor=x if j%2==0 else 1-x
        sign=1 if j%2==0 else -1
        derivative=sign*value+factor*derivative
        value=correction[j]+factor*value
    result=(1-x)*left+x*right+x*(1-x)*value
    result_x=right-left+(1-2*x)*value+x*(1-x)*derivative
    return result,result_x


class DenseCandidate:
    def __init__(self,path):
        self.path=Path(path)
        raw=gzip.decompress(self.path.read_bytes())
        self.data=np.load(io.BytesIO(raw),allow_pickle=False)
        self.nodes=self.data['time_nodes'];self.endpoints=self.data['positive_endpoint_coefficients']
        self.corrections=self.data['positive_dense_corrections']
        self.metadata=json.loads(str(self.data['metadata']))
        self.grid=int(self.metadata['angular_grid'])

    def coefficient_jet(self,index,x):
        value,dx=polynomial_jet(self.endpoints[index],self.endpoints[index+1],self.corrections[index],x)
        return value,dx/(self.nodes[index+1]-self.nodes[index])

    def evaluate(self,r,angles=None):
        if not self.nodes[0]<=r<=self.nodes[-1]:raise ValueError('r outside complete finite candidate')
        j=min(len(self.nodes)-2,bisect_right(self.nodes,float(r))-1)
        x=(r-self.nodes[j])/(self.nodes[j+1]-self.nodes[j]);value,dr=self.coefficient_jet(j,x)
        angles=angles or 2*self.grid;v=full_coefficients(value,angles);rv=full_coefficients(dr,angles)
        f=4*np.fft.fftfreq(angles,1/angles)
        samples=lambda c:(angles*np.fft.ifft(c,axis=0)).real
        return dict(piece=j,coordinate=x,BC=samples(v),BC_r=samples(rv),
            BC_theta=samples(1j*f[:,None]*v),BC_thetatheta=samples(-f[:,None]**2*v),
            BC_rtheta=samples(1j*f[:,None]*rv))


class ScalarEvolution:
    def __init__(self,geometry,angles):self.geometry=geometry;self.angles=angles;self.calls=0
    def __call__(self,r,y):
        bc=resample(y.reshape(self.angles,2),2*self.angles);B,C=bc.T
        t=scalar_target(self.geometry,r);gamma=np.sqrt(t['E'])/t['a'];beta=t['a_x']/t['a']
        if np.min(abs(C))<.02:raise ValueError('finite C denominator gate')
        A=(t['K']+B*B)/C;deriv=scalar_derivative(np.column_stack([B,A]))
        rhs=np.column_stack([gamma*deriv[:,1]-2*beta*B,
            gamma*deriv[:,0]+beta*(A-C)])
        self.calls+=1;return resample(rhs,self.angles).ravel()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--right',type=Fraction,default=Fraction(1,200));p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--max-step',type=float,default=.00025);p.add_argument('--rtol',type=float,default=3e-11)
    p.add_argument('--atol',type=float,default=3e-13);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--candidate',type=Path,required=True);args=p.parse_args();start=time.monotonic()
    g,definition=load_exact_object(args.object,512);N=args.angles
    if N%2 or N//2<=g.modes:raise ValueError('insufficient exact Fourier support')
    t0=scalar_target(g,0.);phase=g.profile_jets(np.array([0.]),order=2)['phase'][0,0,:,0]
    initial=np.zeros((N//2,2),complex);initial[0,1]=-1/t0['a']
    for j,b in enumerate(phase,1):initial[j,1]=-(4*j)*b/(2*t0['a'])
    state=(N*np.fft.ifft(full_coefficients(initial,N),axis=0)).real.ravel()
    right=float(args.right)
    if Fraction.from_float(right)<args.right:right=float(np.nextafter(right,np.inf))
    allcuts={0.}
    for name,values in g.frozen.items():
        if name.endswith('_knots'):allcuts.update(abs(float(v)) for v in values)
    allcuts=sorted(allcuts)
    stages=sorted({0.,right}|{v for v in allcuts if 0<v<right})
    time_nodes=[0.];ends=[initial];corrections=[];germs=[];rhs=ScalarEvolution(g,N)
    largest_endpoint_replacement=0.;steps=0
    for a,b in zip(stages,stages[1:]):
        j=bisect_right(allcuts,a)-1;germ=(allcuts[j],allcuts[j+1])
        solver=DOP853(rhs,a,state,b,rtol=args.rtol,atol=args.atol,max_step=args.max_step)
        while solver.status=='running':
            message=solver.step()
            if solver.status=='failed':raise ValueError('dense integration failed: '+str(message))
            dense=solver.dense_output();end=positive_hermitian(solver.y.reshape(N,2))
            higher=np.stack([positive_hermitian(row.reshape(N,2)) for row in dense.F[1:]])
            rawF0=positive_hermitian(dense.F[0].reshape(N,2))
            replacement=(end-ends[-1])-rawF0
            largest_endpoint_replacement=max(largest_endpoint_replacement,float(np.sum(abs(replacement))))
            time_nodes.append(float(solver.t));ends.append(end);corrections.append(higher);germs.append(germ);steps+=1
        state=solver.y
    nodes=np.asarray(time_nodes);ends=np.asarray(ends);corrections=np.asarray(corrections)
    metadata=dict(kind='exact_finite_piecewise_degree7_Fourier_BC_candidate',accuracy_certified=False,
        angular_grid=N,positive_modes=N//2,physical_frequencies='4*k; k=0,...,N/2-1; negative modes exact conjugates',
        Nyquist_exact_zero=True,mean_retained=True,time_polynomial_degree=7,
        endpoint_continuity_exact=True,radial_derivative_continuity_claimed=False,
        coefficient_semantics='Every stored real and imaginary binary64 value is interpreted as its exact dyadic rational.',
        polynomial_contract='(1-x)L+xR+x(1-x)*(F1+x*(F2+(1-x)*(F3+x*(F4+(1-x)*(F5+x*F6))))))',
        requested_exact_right=str(args.right),time_nodes_exact_fractions=[str(Fraction.from_float(t)) for t in nodes],
        scalar_germs_exact_fractions=[[str(Fraction.from_float(t)) for t in germ] for germ in germs],
        source_sha256=sha(__file__),object_sha256=sha(args.object),
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        exact_center_parameter=definition['delta_fraction'])
    buffer=io.BytesIO();np.savez(buffer,time_nodes=nodes,positive_endpoint_coefficients=ends,
        positive_dense_corrections=corrections,scalar_germs=np.asarray(germs),metadata=np.array(json.dumps(metadata)))
    args.candidate.write_bytes(gzip.compress(buffer.getvalue(),compresslevel=6,mtime=0))
    candidate=DenseCandidate(args.candidate);checks=[]
    for r in np.linspace(0.,right,21):
        d=candidate.evaluate(float(r));t=scalar_target(g,float(r));B,C=d['BC'].T;Br,Cr=d['BC_r'].T
        Bt,Ct=d['BC_theta'].T;Btt,Ctt=d['BC_thetatheta'].T;Brt,Crt=d['BC_rtheta'].T
        gamma=np.sqrt(t['E'])/t['a'];beta=t['a_x']/t['a'];A=(t['K']+B*B)/C
        At=2*B*Bt/C-(t['K']+B*B)*Ct/C**2
        Att=2*(Bt*Bt+B*Btt)/C-4*B*Bt*Ct/C**2-(t['K']+B*B)*Ctt/C**2+2*(t['K']+B*B)*Ct**2/C**3
        RB=Br-gamma*At+2*beta*B;RC=Cr-gamma*Bt-beta*(A-C)
        RBt=Brt-gamma*Att+2*beta*Bt;RCt=Crt-gamma*Btt-beta*(At-Ct)
        k=np.sqrt(-t['K']);P=(B+k)/C;Q=(B-k)/C
        Pt=Bt/C-(B+k)*Ct/C**2;Qt=Bt/C-(B-k)*Ct/C**2
        Ptt=Btt/C-2*Bt*Ct/C**2-(B+k)*Ctt/C**2+2*(B+k)*Ct**2/C**3
        Qtt=Btt/C-2*Bt*Ct/C**2-(B-k)*Ctt/C**2+2*(B-k)*Ct**2/C**3
        RP=(RB-P*RC)/C;RQ=(RB-Q*RC)/C
        RPt=(RBt-Pt*RC-P*RCt)/C-(RB-P*RC)*Ct/C**2
        RQt=(RBt-Qt*RC-Q*RCt)/C-(RB-Q*RC)*Ct/C**2
        checks.append(dict(r=float(r),C_min_abs=float(np.min(abs(C))),
            BC_residual_C0=float(max(np.max(abs(RB)),np.max(abs(RC)))),
            BC_residual_theta_C0=float(max(np.max(abs(RBt)),np.max(abs(RCt)))),
            Riemann_residual_C0=float(max(np.max(abs(RP)),np.max(abs(RQ)))),
            Riemann_residual_theta_C0=float(max(np.max(abs(RPt)),np.max(abs(RQt)))),
            Riemann_theta_C0=float(max(np.max(abs(Pt)),np.max(abs(Qt)))),
            Riemann_thetatheta_C0=float(max(np.max(abs(Ptt)),np.max(abs(Qtt))))))
    report=dict(**metadata,complete=True,certified=False,primitive_nodes=512,nonlinear_grid=2*N,
        producer='DOP853 finite dealiased two-field ODE, restarted at every actual common scalar knot',
        rtol=args.rtol,atol=args.atol,max_step=args.max_step,pieces=steps,actual_scalar_stages=len(stages)-1,
        exact_time_interval=[metadata['time_nodes_exact_fractions'][0],metadata['time_nodes_exact_fractions'][-1]],
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),candidate_bytes=args.candidate.stat().st_size,
        largest_floating_endpoint_replacement_l1=largest_endpoint_replacement,
        diagnostic_samples=checks,diagnostic_maxima={key:max(row[key] for row in checks) for key in checks[0] if key!='r'},
        rhs_calls=rhs.calls,wall_seconds=time.monotonic()-start,
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in ('fourfold_phase_codazzi_evolution_probe.py','fourfold_phase_local_correction_probe.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        limitations=['Complete finite candidate, but its accuracy, residual enclosures and PDE continuation remain unvalidated.',
            'Diagnostic samples are finite floating evaluations, not a full radial/angular cover or whole-eta certificate.',
            'Riemann variables must use the actual target k(r)=sqrt(-K(r)), with its parameter dependence included in validation.',
            'DOP853 dense values are redefined with shared exact endpoints; the displayed replacement is only a floating size diagnostic.'])
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print({key:report[key] for key in ('pieces','actual_scalar_stages','candidate_bytes','rhs_calls','wall_seconds','diagnostic_maxima')},flush=True)


if __name__=='__main__':main()
