#!/usr/bin/env python3
"""Finite two-ended Codazzi diagnostic, allowing the initial waist curve to vary.

The target E,a,K remains the original target. B is odd and C is even in the
physical angle, with every retained sine/cosine mode and the C mean present.
At r=0 impose B=0 and mean C=-1/a(0). At the positive end prescribe the
NONMEAN C coefficients of the old actual geometry. This is an explicitly
artificial finite boundary condition, not the old cap DN and not cap closure.
"""
from __future__ import annotations
import argparse,gzip,io,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_core_low_block import uniform_fields
from fourfold_phase_local_correction_probe import sha,dot,scalar_target


class TwoEnded:
    def __init__(self,geometry,modes,angular_grid):
        self.geometry=geometry;self.modes=modes;self.angular_grid=angular_grid
        self.theta=np.arange(angular_grid)*np.pi/(2*angular_grid)
        self.frequency=4*np.arange(1,modes+1)
        self.sin=np.sin(self.frequency[:,None]*self.theta)
        self.cos=np.cos(4*np.arange(modes+1)[:,None]*self.theta)
        self.proj=self.cos*(2/angular_grid);self.proj[0]*=.5
        self.cache={};self.calls=0;self.jac_calls=0;self.last_log=time.monotonic()
        self.minimum_abs_C_seen=np.inf

    def target(self,r):
        key=np.asarray(r).tobytes()
        if key not in self.cache:
            if len(self.cache)>=5:self.cache.pop(next(iter(self.cache)))
            t=self.geometry.radial_target_metric(r)
            self.cache[key]=(np.sqrt(t['E'])/t['a'],t['a_x']/t['a'],t['K'])
        return self.cache[key]

    def fields(self,y):
        m=self.modes
        return self.sin.T@y[:m],self.cos.T@y[m:]

    def evaluate(self,r,y):
        m=self.modes;gamma,beta,K=self.target(r);B,C=self.fields(y)
        self.minimum_abs_C_seen=min(self.minimum_abs_C_seen,float(np.min(abs(C))))
        A=(K[None,:]+B*B)/C;ac=self.proj@A
        result=np.empty_like(y)
        result[:m]=-gamma*self.frequency[:,None]*ac[1:]-2*beta*y[:m]
        result[m:]=beta*(ac-y[m:])
        result[m+1:]+=gamma*self.frequency[:,None]*y[:m]
        self.calls+=1
        if time.monotonic()-self.last_log>20:
            print(dict(rhs_calls=self.calls,jac_calls=self.jac_calls,radial_nodes=len(r),
                sampled_C_min=float(np.min(C)),sampled_C_max=float(np.max(C))),flush=True)
            self.last_log=time.monotonic()
        return result

    def jacobian(self,r,y):
        m=self.modes;n=2*m+1;gamma,beta,K=self.target(r);B,C=self.fields(y)
        A=(K[None,:]+B*B)/C
        da_b=np.einsum('an,nr,bn->abr',self.proj,2*B/C,self.sin,optimize=True)
        da_c=np.einsum('an,nr,bn->abr',self.proj,-A/C,self.cos,optimize=True)
        da=np.concatenate([da_b,da_c],axis=1)
        result=np.empty((n,n,len(r)))
        result[:m]=-gamma*self.frequency[:,None,None]*da[1:]
        result[m:]=beta*da
        for k in range(m):
            result[k,k]-=2*beta
            result[m+1+k,k]+=gamma*self.frequency[k]
        for k in range(m+1):result[m+k,m+k]-=beta
        self.jac_calls+=1
        return result

    def old_fields(self,r):
        t=scalar_target(self.geometry,float(r))
        F,P,T,PP,PT,TT=uniform_fields(self.geometry,float(r),self.angular_grid)
        normal=np.cross(T,P);normal/=np.linalg.norm(normal,axis=1)[:,None]
        B=dot(normal,PT)/(np.sqrt(t['E'])*t['a'])
        C=dot(normal,TT)/t['a']**2
        return np.concatenate([(2/self.angular_grid)*(self.sin@B),self.proj@C])


def save_npz_gz(path,**arrays):
    memory=io.BytesIO();np.savez(memory,**arrays)
    with gzip.GzipFile(filename=str(path),mode='wb',mtime=0) as stream:stream.write(memory.getvalue())


def load_candidate(path):
    with gzip.open(path,'rb') as stream:saved=np.load(io.BytesIO(stream.read()),allow_pickle=False)
    return saved


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--modes',type=int,default=16);p.add_argument('--angles',type=int,default=256)
    p.add_argument('--radial-nodes',type=int,default=251);p.add_argument('--right',type=float,default=.25)
    p.add_argument('--tol',type=float,default=1e-5);p.add_argument('--max-nodes',type=int,default=4000)
    p.add_argument('--guess',type=Path);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--candidate',type=Path,required=True)
    args=p.parse_args();start=time.monotonic()
    if args.angles<8*args.modes or args.angles%4:raise ValueError('at least eight angular points per retained index are required')
    geometry,definition=load_exact_object(args.object,512)
    system=TwoEnded(geometry,args.modes,args.angles);m=args.modes;n=2*m+1
    a0=scalar_target(geometry,0.)['a'];boundary_right=system.old_fields(args.right)[m+1:]
    r=np.linspace(0.,args.right,args.radial_nodes)
    guess=np.column_stack([system.old_fields(x) for x in r]);guess_sha=None
    if args.guess:
        prior=load_candidate(args.guess);meta=json.loads(str(prior['metadata']))
        if meta['object_sha256']!=sha(args.object):raise ValueError('a different target object in initial guess')
        pm=int(meta['modes']);pp=PPoly(prior['piece_coefficients'],prior['radial_nodes'])
        prior_values=pp(r).T;count=min(m,pm)
        guess[:count]=prior_values[:count];guess[m:m+count+1]=prior_values[pm:pm+count+1]
        guess_sha=sha(args.guess)
    def bc(left,right):
        return np.concatenate([left[:m],[left[m]+1/a0],right[m+1:]-boundary_right])
    def bc_jac(left,right):
        jl=np.zeros((n,n));jr=np.zeros((n,n))
        jl[np.arange(m+1),np.arange(m+1)]=1
        jr[np.arange(m+1,n),np.arange(m+1,n)]=1
        return jl,jr
    result=solve_bvp(system.evaluate,bc,r,guess,fun_jac=system.jacobian,bc_jac=bc_jac,
        tol=args.tol,bc_tol=args.tol/100,max_nodes=args.max_nodes,verbose=2)
    checks=np.unique(np.concatenate([result.x,(result.x[:-1]+result.x[1:])/2]))
    values=result.sol(checks);B,C=system.fields(values)
    actual_rhs=system.evaluate(checks,values);poly_derivative=result.sol(checks,1)
    residual=poly_derivative-actual_rhs
    theta_B_residual=system.sin.T@residual[:m]
    theta_C_residual=system.cos.T@residual[m:]
    # Nonlinear angular projection defects, sampled on a separately doubled grid.
    fine=TwoEnded(geometry,m,2*args.angles);gamma,beta,K=fine.target(checks)
    B2,C2=fine.fields(values);A2=(K[None,:]+B2*B2)/C2
    Ac=fine.proj@A2;fproj=fine.cos.T@Ac
    angular_projection_A=float(np.max(abs(A2-fproj)))
    initial=values[:,0];old_initial=system.old_fields(0.)
    metadata=dict(kind='floating_finite_two_ended_Codazzi_candidate',object_sha256=sha(args.object),
        source_sha256=sha(__file__),modes=m,physical_frequency_factor=4,
        state_order='B sine k=1..M, C cosine k=0..M',original_target_fixed=True,
        initial_waist_curve_changed=True,right_boundary='old actual nonmean angular normal curvature only; NOT cap DN')
    save_npz_gz(args.candidate,radial_nodes=result.x,piece_coefficients=result.sol.c,
        initial_state=initial,right_boundary_C_nonmean=boundary_right,metadata=np.array(json.dumps(metadata)))
    doc=dict(**metadata,certified=False,success=bool(result.success),status=int(result.status),message=result.message,
        original_object_path=str(args.object),exact_center_parameter=definition['delta_fraction'],
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        angular_grid=args.angles,angular_diagnostic_grid=2*args.angles,
        requested_radial_interval=[0.,args.right],radial_nodes_initial=args.radial_nodes,
        radial_nodes_final=len(result.x),iterations=int(result.niter),rhs_calls=system.calls,jac_calls=system.jac_calls,
        tol=args.tol,max_nodes=args.max_nodes,guess_path=str(args.guess) if args.guess else None,guess_sha256=guess_sha,
        bc_residual=float(np.max(abs(bc(result.y[:,0],result.y[:,-1])))),
        maximum_collocation_rms_residual=float(np.max(result.rms_residuals)),
        sampled_finite_PDE_residual=float(max(np.max(abs(theta_B_residual)),np.max(abs(theta_C_residual)))),
        sampled_A_angular_projection_defect=angular_projection_A,
        sampled_C_range=[float(np.min(C2)),float(np.max(C2))],
        sampled_minimum_abs_C=float(np.min(abs(C2))),
        minimum_abs_C_at_all_newton_samples=system.minimum_abs_C_seen,
        initial_C_coefficients=initial[m:].tolist(),old_initial_C_coefficients=old_initial[m:].tolist(),
        initial_C_coefficient_difference_l1=float(np.sum(abs(initial[m:]-old_initial[m:]))),
        initial_B_coefficient_l1=float(np.sum(abs(initial[:m]))),
        right_boundary_C_nonmean=boundary_right.tolist(),
        complete_mean_retained=True,whole_real_angular_circle=False,whole_parameter_interval=False,whole_radial_domain=False,
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in
            ('fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py','fourfold_phase_core_low_block.py','fourfold_phase_local_correction_probe.py')},
        wall_seconds=time.monotonic()-start,
        limitations=['Floating finite Fourier/radial collocation only; no PDE, rounding, radial or angular-tail validation.',
            'This candidate adjusts the waist curve; it is a different branch from the frozen R124/R125 initial curve.',
            'The positive end prescribes only nonmean C from the old geometry; no exact nonlinear cap response or regular closure is imposed.',
            'The C mean and all retained modes are present. Full geometric frame/position reconstruction is not performed by this producer.'])
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print({k:doc[k] for k in ('success','message','radial_nodes_final','sampled_finite_PDE_residual',
        'sampled_A_angular_projection_defect','sampled_C_range','initial_C_coefficient_difference_l1','wall_seconds')},flush=True)


if __name__=='__main__':main()
