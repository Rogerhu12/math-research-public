#!/usr/bin/env python3
"""Select fixed omitted-velocity rows through a full collocation nullspace.

Read-only linearization of one accepted inward parent. All 3M+2 ODEs and
2M+5 homogeneous left conditions are retained. An orthonormal M-3 space is
transported through every actual collocation interval; no Newton solve is
performed. The candidate row selections are fixed at this input, not updated
during a future solve. A good reduced condition is not nonlinear existence.
"""
import argparse,gzip,hashlib,importlib.util,json,time,warnings
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import qr,lu_factor,lu_solve,LinAlgWarning
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_inward_profile import InwardProfile


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class OmittedRows:
    def __init__(self,q,k):
        self.q=q;self.k=k;self.modes=np.arange(q.M+1,2*q.M-2);self.f=2*self.modes
        if self.f[-1]>=q.N//2:raise ValueError('Omitted row is at or above Nyquist')
        self.plus=(self.f[:,None]-q.freq[None,:])%q.N
        self.minus=(self.f[:,None]+q.freq[None,:])%q.N
        self.labels=[dict(component=c,mode=int(m),frequency=int(2*m)) for c in ('R','T','Z') for m in self.modes]

    def value(self,y):
        v=self.q.local(y,self.k)['V']
        def real(a):
            h=np.fft.rfft(a,axis=0)/self.q.N
            return np.r_[2*h[self.f,0].real,-2*h[self.f,1].imag,2*h[self.f,2].real]
        return real(v.real)+1j*real(v.imag) if np.iscomplexobj(v) else real(v)

    def jacobian(self,y):
        q=self.q;local=q.local(y,self.k);zero=np.zeros((q.N,3));Ad=np.empty((q.N,3,3));Ae=np.empty_like(Ad)
        for j in range(3):
            unit=zero.copy();unit[:,j]=1
            Ad[:,:,j]=q.variation(local,unit,zero);Ae[:,:,j]=q.variation(local,zero,unit)
        Ah=np.fft.fft(Ad,axis=0)/q.N;Eh=np.fft.fft(Ae,axis=0)/q.N
        plus=Ah[self.plus]@q.Dp[None,:,:,:]+Eh[self.plus]@q.D2p[None,:,:,:]
        minus=Ah[self.minus]@q.Dm[None,:,:,:]+Eh[self.minus]@q.D2m[None,:,:,:]
        C=(plus+minus)/2;S=(-1j*plus+1j*minus)/2
        rows=[]
        for c in range(3):
            blocks=[C[:,:,c,0],S[:,1:,c,1],C[:,:,c,2]]
            rows.append(np.hstack([-2*b.imag if c==1 else 2*b.real for b in blocks]))
        return np.vstack(rows)


def spectrum(A):
    s=np.linalg.svd(A,compute_uv=False);threshold=max(A.shape)*np.finfo(float).eps*s[0]
    return dict(singular_max=float(s[0]),singular_min=float(s[-1]),condition=float(s[0]/s[-1]),
                numerical_rank=int(np.sum(s>threshold)),rank_threshold=float(threshold))


def unit_rows(A):
    norms=np.linalg.norm(A,axis=1)
    if np.any(norms==0):raise ValueError('A candidate boundary row vanished')
    return A/norms[:,None]


def select(A,count):return qr(A.T,mode='economic',pivoting=True,check_finite=False)[2][:count]


def main(args):
    begin=time.perf_counter();raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if sha(args.input)!=args.input_sha256 or not data.get('success') or data.get('fixed_modes')!=3:
        raise ValueError('Require the exact accepted three-fixed-mode parent')
    q=Frenet(data['M'],data['N']);n=q.n;free=q.M-3;nl=n-free
    spec=data['inward_scalar_profile'];profile_source=Path(__file__).with_name('parallel_20261117_inward_profile.py')
    if sha(profile_source)!=data['inward_profile_sha256']:raise ValueError('Stored scalar source identity differs')
    profile=InwardProfile(data['fixed_scalar_profile']['geometry'],data['analytic_extension_origin'],
        spec['cut'],spec['curvature'],spec['ramp_in'],spec['ramp_out'],spec['quadrature'])
    path=Path(__file__).resolve().parents[1]/'computations/geometry_20261114_separated_qr_bvp.py'
    module=importlib.util.spec_from_file_location('reachable_existing_qr',path);blocks=importlib.util.module_from_spec(module);module.loader.exec_module(blocks)
    x=np.asarray(data['mesh']);Y=np.asarray(data['states']);h=np.diff(x)
    scalar=np.array([profile(t) for t in x]);k=scalar[:,1]/scalar[:,0]
    f=np.array([q.rhs(y,kk) for y,kk in zip(Y,k)])
    middle=(Y[:-1]+Y[1:])/2-h[:,None]*(f[1:]-f[:-1])/8
    BA=np.zeros((nl,n));BA[0,0]=1;BA[1:4,1:4]=np.eye(3)
    for j in range(q.M):BA[4+j,1+j]=q.freq[j+1];BA[4+j,q.M+1+j]=1
    BA[4+q.M:,2*q.M+1:]=np.eye(q.M+1)
    Z=qr(BA.T,mode='full',check_finite=False)[0][:,nl:];Zleft=Z.copy()
    initial_left_error=float(np.max(abs(BA@Z)));orth=0.;relative=0.;collocation=0.;next_J=q.jacobian(Y[0],k[0])
    for i,step in enumerate(h):
        left_J=next_J;am,apm,_=profile((x[i]+x[i+1])/2);mid_J=q.jacobian(middle[i],apm/am)
        next_J=q.jacobian(Y[i+1],k[i+1]);L,R=blocks.local_blocks(step,left_J,mid_J,next_J)
        with warnings.catch_warnings():
            warnings.simplefilter('error',LinAlgWarning)
            propagated=lu_solve(lu_factor(R,check_finite=False),-L@Z,check_finite=False)
        new_Z,transport=qr(propagated,mode='economic',check_finite=False)
        scale=np.linalg.norm(L@Z,'fro')+np.linalg.norm(R@new_Z@transport,'fro')
        relative=max(relative,float(np.linalg.norm(R@new_Z@transport+L@Z,'fro')/max(scale,np.finfo(float).tiny)))
        orth=max(orth,float(np.max(abs(new_Z.T@new_Z-np.eye(free)))))
        fm=q.rhs(middle[i],apm/am)
        collocation=max(collocation,float(np.max(abs(Y[i+1]-Y[i]-step*(f[i]+4*fm+f[i+1])/6))))
        Z=new_Z
        if (i+1)%64==0:print(json.dumps(dict(event='actual_parent_nullspace_transfer',intervals=i+1,total=len(h),seconds=time.perf_counter()-begin)),flush=True)
    omitted=OmittedRows(q,k[-1]);values=omitted.value(Y[-1]);J=omitted.jacobian(Y[-1]);A=J@Z
    rng=np.random.default_rng(20261117);checks=[]
    for j in range(5):
        v=rng.standard_normal(n);v/=np.linalg.norm(v);eps=1e-28
        exact=omitted.value(Y[-1].astype(complex)+1j*eps*v).imag/eps;delta=J@v-exact
        checks.append(dict(index=j,max_abs_error=float(np.max(abs(delta))),relative_inf_error=float(np.max(abs(delta))/np.max(abs(exact)))))
    selections={name:np.arange(i*free,(i+1)*free) for i,name in enumerate(('only_R','only_T','only_Z'))}
    selections.update(local_raw_qr=select(J,free),local_unit_qr=select(unit_rows(J),free),
        reachable_raw_qr=select(A,free),reachable_unit_qr=select(unit_rows(A),free),
        reachable_full_row_unit_qr=select(unit_rows(J)@Z,free))
    comparisons={}
    for name,indices in selections.items():
        comparisons[name]=dict(row_indices=indices.tolist(),rows=[dict(index=int(i),**omitted.labels[i],raw_value=float(values[i])) for i in indices],
            selected_raw_value_max=float(np.max(abs(values[indices]))),local=spectrum(J[indices]),local_unit=spectrum(unit_rows(J[indices])),
            reduced=spectrum(A[indices]),reduced_unit=spectrum(unit_rows(A[indices])))
    sources={p.name:sha(p) for p in [Path(__file__),profile_source,path,
        Path(__file__).with_name('parallel_20261117_profile.py'),Path(__file__).with_name('parallel_20261117_frenet_symbol.py')]}
    arrays=args.out.with_suffix('.arrays.npz')
    np.savez_compressed(arrays,terminal_basis=Z,left_basis=Zleft,right_raw_jacobian=J,reachable_jacobian=A,
        raw_values=values,mesh=x,left_rows=BA)
    report=dict(scope=__doc__,input_sha256=hashlib.sha256(raw).hexdigest(),sources=sources,M=q.M,N=q.N,nodes=len(x),endpoint=float(x[-1]),
        all_ode_components=n,left_rows=nl,free_dimensions=free,source_identity='Exact accepted input bytes; no other-parent or later-Newton cache was used.',
        array_path=str(arrays),array_sha256=sha(arrays),numpy_version=np.__version__,scipy_version=scipy.__version__,
        saved_rhs_difference=float(np.max(abs(f-np.asarray(data['rhs'])))),collocation_residual_max=collocation,
        left_homogeneous_residual_max=initial_left_error,transfer_relative_frobenius_max=relative,orthogonality_max=orth,
        candidate_rows=omitted.labels,raw_values=values.tolist(),all_local=spectrum(J),all_reachable=spectrum(A),
        analytic_jacobian_directional_checks=checks,selections=comparisons,seconds=time.perf_counter()-begin)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='reachable_row_selection_complete',seconds=report['seconds'],
        selections={name:{key:r[key] for key in ('local','reduced','reduced_unit','selected_raw_value_max')} for name,r in comparisons.items()},
        transfer_relative_frobenius_max=relative,output_sha256=sha(args.out))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--input-sha256',required=True);p.add_argument('--out',type=Path,required=True)
    main(p.parse_args())
