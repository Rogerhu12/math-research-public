#!/usr/bin/env python3
"""Full endpoint Jacobian of the fixed finite-arclength er/fr functions.

This is a finite algebraic probe, not a BVP or a new accepted field.  The
Frenet velocity is the complete PROJECTED finite RHS.  The construction
grid is fixed; er/fr are expressed at the source angle, so no left rho is
present in these normalized functions.  The optional old transported basis
is explicitly a frozen other-parent predictor, not the true derivative of
the full collocation solution at this input.
"""
import argparse,gzip,hashlib,json,sys,time
from pathlib import Path
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class RetractedGram:
    def __init__(self,q,a,ap):
        self.q=q;self.a=a;self.k=ap/a;self.N=q.N
        self.frequency=np.arange(q.N//2+1)
        self.e_modes=2*np.arange(q.N//4+1)
        self.f_modes=2*np.arange(1,q.N//4)
        if q.N%4:raise ValueError('Need a construction grid divisible by four')

    def primitive_real(self,value):
        # Same trigonometric interpolant as the frozen arclength reader:
        # original Nyquist coefficient has half weight off grid.  On this
        # construction grid its primitive vanishes, but retain the same rule.
        h=np.fft.rfft(value)/self.N;h[-1]*=.5;h[0]=0
        h[1:]/=1j*self.frequency[1:];h[-1]*=2
        result=np.fft.irfft(self.N*h,n=self.N)
        return result-result[0]

    def primitive(self,value):
        if np.iscomplexobj(value):
            return self.primitive_real(value.real)+1j*self.primitive_real(value.imag)
        return self.primitive_real(value)

    def fields(self,y):
        q=self.q;dy=q.rhs(y,self.k)
        F,t,_=q.jet(y);V,ts,_=q.jet(dy)
        speed=np.sqrt(np.sum(t*t,axis=1))
        speed_s=np.sum(t*ts,axis=1)/speed
        b=speed.mean();rate=speed_s.mean()/b
        lam=self.a/b;lam_s=lam*(self.k-rate)
        psi_s=-self.primitive(speed_s-rate*speed)/speed
        center=np.zeros(3,dtype=y.dtype);center[2]=y[2*q.M+1]
        center_s=np.zeros(3,dtype=y.dtype);center_s[2]=dy[2*q.M+1]
        velocity=lam*V+(1-lam)*center_s+lam_s*(F-center)+lam*t*psi_s[:,None]
        er=np.sum(velocity*velocity,axis=1)-1
        fr=np.sum(velocity*t,axis=1)/speed
        return er,fr,dict(scale=lam,scale_s=lam_s,psi_s=psi_s,velocity=velocity,
                          speed=speed,projected_rhs=dy)

    def coefficients_real(self,er,fr):
        # All finite even-parity er and odd-parity fr modes, in a Parseval
        # orthonormal real convention.  E includes its mean and Nyquist;
        # F has sine modes 2,...,N/2-2. Total N/2 rows, no arbitrary cutoff.
        he=np.fft.rfft(er)/self.N;hf=np.fft.rfft(fr)/self.N
        e=np.sqrt(2.)*he[self.e_modes].real
        e[[0,-1]]/=np.sqrt(2.)
        f=-np.sqrt(2.)*hf[self.f_modes].imag
        return np.r_[e,f]

    def value(self,y):
        er,fr,_=self.fields(y)
        if np.iscomplexobj(y):
            return self.coefficients_real(er.real,fr.real)+1j*self.coefficients_real(er.imag,fr.imag)
        return self.coefficients_real(er,fr)

    def metrics(self,y):
        er,fr,v=self.fields(y)
        error=(abs(er)+np.sqrt(er*er+4*fr*fr))/2
        z=self.q.local(y,self.k)
        return dict(gram_at_construction_grid=float(max(error)),er_max=float(max(abs(er))),
            fr_max=float(max(abs(fr))),min_H_over_W=float(min(z['H']/z['W'])),
            scale_minus_one=float(v['scale']-1),scale_s=float(v['scale_s']),
            psi_s_max=float(max(abs(v['psi_s']))),coefficient_l2=float(np.linalg.norm(self.value(y))))


def main(args):
    begin=time.perf_counter();sys.path.insert(0,str(args.scripts))
    from parallel_20261117_frenet_symbol import Frenet
    from parallel_20261117_inward_profile import InwardProfile
    if sha(args.reference_reader)!=args.reference_reader_sha:
        raise ValueError('The frozen finite-arclength definition changed')
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('Accepted true input required')
    q=Frenet(data['M'],args.construction_angles or data['N'])
    if q.N!=data['N']:raise ValueError('This probe keeps the original finite RHS grid')
    source=args.scripts/'parallel_20261117_inward_profile.py'
    if sha(source)!=data['inward_profile_sha256']:raise ValueError('Scalar source changed')
    spec=data['inward_scalar_profile']
    profile=InwardProfile(data['fixed_scalar_profile']['geometry'],data['analytic_extension_origin'],
        spec['cut'],spec['curvature'],spec['ramp_in'],spec['ramp_out'],spec['quadrature'])
    a,ap,_=profile(data['mesh'][-1]);model=RetractedGram(q,a,ap);y=np.asarray(data['states'][-1])
    values=model.value(y);jac=np.empty((len(values),q.n));eps=1e-28
    for j in range(q.n):
        yy=y.astype(complex);yy[j]+=1j*eps;jac[:,j]=model.value(yy).imag/eps
    rng=np.random.default_rng(20261117);checks=[]
    for j in range(5):
        direction=rng.normal(size=q.n);direction/=np.linalg.norm(direction)
        exact=model.value(y.astype(complex)+1j*eps*direction).imag/eps
        predicted=jac@direction
        checks.append(dict(index=j,absolute_inf=float(max(abs(predicted-exact))),
            derivative_inf=float(max(abs(exact))),relative_inf=float(max(abs(predicted-exact))/max(abs(exact)))))
    fd=[]
    direction=rng.normal(size=q.n);direction/=np.linalg.norm(direction)
    predicted=jac@direction
    for step in [1e-8,2e-9]:
        finite=(model.value(y+step*direction)-model.value(y-step*direction))/(2*step)
        fd.append(dict(step=step,relative_inf=float(max(abs(finite-predicted))/max(abs(predicted)))))
    transfer=json.loads(args.old_transfer_report.read_bytes())
    path=args.old_transfer_report.parent/transfer['array_path']
    if sha(path)!=transfer['array_sha256']:raise ValueError('Frozen transfer array changed')
    if (transfer['M'],transfer['N'])!=(q.M,q.N):raise ValueError('Transfer shape differs')
    with np.load(path,allow_pickle=False) as stored:Z=stored['terminal_basis'].copy()
    A=jac@Z;U,s,Vt=np.linalg.svd(A,full_matrices=False)
    rank_threshold=max(A.shape)*np.finfo(float).eps*s[0]
    coordinates=Vt.T@((U.T@values)/s)
    delta=Z@coordinates;remainder=values-A@coordinates
    trials=[]
    for alpha in [1.,.5,.25,.125,.0625]:
        candidate=y-alpha*delta
        try:
            metrics=model.metrics(candidate);actual=model.value(candidate)
            metrics.update(alpha=alpha,nonlinear_linearization_remainder_inf=float(max(abs(actual-(values-alpha*(A@coordinates))))),
                residual_to_scaled_parent_inf=float(max(abs(actual-(1-alpha)*values))))
        except FloatingPointError as err:metrics=dict(alpha=alpha,domain_error=str(err))
        trials.append(metrics)
    arrays=args.out.with_suffix('.arrays.npz')
    np.savez_compressed(arrays,values=values,jacobian=jac,old_terminal_basis=Z,
        reduced_jacobian=A,U=U,singular_values=s,endpoint_correction=delta,
        projected_remainder=remainder)
    report=dict(scope=__doc__,input_sha256=hashlib.sha256(raw).hexdigest(),M=q.M,N=q.N,
        endpoint=float(data['mesh'][-1]),source_sha256=sha(__file__),
        reference_reader_sha256=sha(args.reference_reader),
        source_dependencies={p.name:sha(p) for p in [source,args.scripts/'parallel_20261117_frenet_symbol.py']},
        rows=len(values),columns=q.n,function_definition='All N/2 Parseval-weighted er-cosine/fr-sine coefficients on the fixed construction grid; projected finite RHS, complete lambda_s and center_s; no left-rho argument.',
        initial=model.metrics(y),saved_rhs_max_difference=float(max(abs(q.rhs(y,ap/a)-np.asarray(data['rhs'][-1])))),
        jacobian_complex_step=eps,directional_checks=checks,central_difference_checks=fd,
        linear_range_identity='Frozen other-parent endpoint basis ONLY; not an actual full collocation derivative at this input.',
        old_transfer_parent_sha256=transfer['input_sha256'],old_transfer_report_sha256=sha(args.old_transfer_report),old_transfer_array_sha256=sha(path),
        reduced_singular_max=float(s[0]),reduced_singular_min=float(s[-1]),reduced_condition=float(s[0]/s[-1]),
        reduced_numerical_rank=int(sum(s>rank_threshold)),rank_threshold=float(rank_threshold),
        correction_inf=float(max(abs(delta))),correction_l2=float(np.linalg.norm(delta)),
        linear_remainder_inf=float(max(abs(remainder))),linear_remainder_l2=float(np.linalg.norm(remainder)),
        linear_remainder_l2_fraction=float(np.linalg.norm(remainder)/np.linalg.norm(values)),
        endpoint_only_nonlinear_trials=trials,array_path=str(arrays),array_sha256=sha(arrays),
        actual_current_parent_transfer_cost='The frozen reachable_rows script can transport all338 ODE/229 left over this 510-node parent; this probe has not done so. Cost is another complete 509-interval QR transport.',
        seconds=time.perf_counter()-begin)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2));print(json.dumps(dict(output_sha256=sha(args.out))))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('scripts','input','reference-reader','old-transfer-report','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--reference-reader-sha',required=True)
    p.add_argument('--construction-angles',type=int,default=2048)
    main(p.parse_args())
