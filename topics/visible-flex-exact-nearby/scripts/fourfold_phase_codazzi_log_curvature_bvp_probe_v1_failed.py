#!/usr/bin/env python3
"""Finite two-ended Codazzi diagnostic in the strictly negative chart C=-exp(W).

No C sign clipping is used. B is represented by sine coefficients and W by
cosine coefficients, including its mean. The true equations are projected
only for this floating candidate; independent sampled residuals are also
evaluated before projection. The cap condition remains artificial.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_local_correction_probe import sha,scalar_target
from fourfold_phase_codazzi_two_end_probe import save_npz_gz,load_candidate
from fourfold_phase_codazzi_two_end_homotopy_probe import ChunkedTwoEnded


class LogTwoEnded(ChunkedTwoEnded):
    def fields(self,y):
        B=self.sin.T@y[:self.modes];W=self.cos.T@y[self.modes:]
        C=-np.exp(W)
        return B,W,C

    def evaluate(self,r,y):
        m=self.modes;gamma,beta,K=self.target(r);B,W,C=self.fields(y)
        A=(K[None,:]+B*B)/C;ac=self.proj@A
        Bt=self.cos[1:].T@(self.frequency[:,None]*y[:m])
        result=np.empty_like(y)
        result[:m]=-gamma*self.frequency[:,None]*ac[1:]-2*beta*y[:m]
        result[m:]=self.proj@(gamma*Bt/C+beta*((K[None,:]+B*B)/(C*C)-1))
        self.calls+=1
        if time.monotonic()-self.last_log>20:
            print(dict(rhs_calls=self.calls,jac_calls=self.jac_calls,radial_nodes=len(r),
                sampled_C_min=float(np.min(C)),sampled_C_max=float(np.max(C))),flush=True)
            self.last_log=time.monotonic()
        return result

    def jacobian(self,r,y):
        m=self.modes;n=2*m+1;gamma,beta,K=self.target(r);B,W,C=self.fields(y)
        A=(K[None,:]+B*B)/C
        Bt=self.cos[1:].T@(self.frequency[:,None]*y[:m])
        def product(weight,basis):return np.einsum('an,nr,bn->abr',self.proj,weight,basis,optimize=True)
        da_b=product(2*B/C,self.sin);da_w=product(-A,self.cos)
        result=np.empty((n,n,len(r)))
        result[:m,:m]=-gamma*self.frequency[:,None,None]*da_b[1:]
        result[:m,m:]=-gamma*self.frequency[:,None,None]*da_w[1:]
        result[m:,:m]=product(gamma/C,self.cos[1:]*self.frequency[:,None])+product(2*beta*B/(C*C),self.sin)
        result[m:,m:]=product(-gamma*Bt/C-2*beta*(K[None,:]+B*B)/(C*C),self.cos)
        for k in range(m):result[k,k]-=2*beta
        self.jac_calls+=1
        return result

    def curvature_coefficients(self,at):
        return self.proj@(-np.exp(self.cos.T@at[self.modes:]))

    def old_guess(self,r):
        m=self.modes;actual=self.old_fields(r)
        # Sample the old C at a finer grid before taking log, keeping this
        # initialization distinct from the actual target and boundary data.
        from fourfold_phase_core_low_block import uniform_fields
        from fourfold_phase_local_correction_probe import dot
        t=scalar_target(self.geometry,float(r));F,P,T,PP,PT,TT=uniform_fields(self.geometry,float(r),self.angular_grid)
        normal=np.cross(T,P);normal/=np.linalg.norm(normal,axis=1)[:,None]
        C=dot(normal,TT)/t['a']**2
        if not np.all(C<0):raise ValueError('old geometry does not lie in the negative C chart')
        return np.concatenate([actual[:m],self.proj@np.log(-C)])


def diagnostics(system,result,a0,right_target):
    m=system.modes;fine=LogTwoEnded(system.geometry,m,2*system.angular_grid)
    points=np.unique(np.concatenate([result.x,(result.x[:-1]+result.x[1:])/2]))
    maxima=dict(finite_PDE_residual=0.,full_B_residual=0.,full_C_residual=0.,C_min=np.inf,C_max=-np.inf)
    for j in range(0,len(points),128):
        r=points[j:j+128];y=result.sol(r);yr=result.sol(r,1)
        gamma,beta,K=fine.target(r);B,W,C=fine.fields(y)
        Bt=fine.cos[1:].T@(fine.frequency[:,None]*y[:m])
        Wt=-fine.sin.T@(fine.frequency[:,None]*y[m+1:])
        Br=fine.sin.T@yr[:m];Wr=fine.cos.T@yr[m:]
        A=(K[None,:]+B*B)/C;At=2*B*Bt/C-A*Wt
        RB=Br-gamma*At+2*beta*B;RC=C*Wr-gamma*Bt-beta*(A-C)
        finite=yr-system.evaluate(r,y)
        frB=system.sin.T@finite[:m];frW=system.cos.T@finite[m:]
        maxima['finite_PDE_residual']=max(maxima['finite_PDE_residual'],float(np.max(abs(frB))),float(np.max(abs(frW))))
        maxima['full_B_residual']=max(maxima['full_B_residual'],float(np.max(abs(RB))))
        maxima['full_C_residual']=max(maxima['full_C_residual'],float(np.max(abs(RC))))
        maxima['C_min']=min(maxima['C_min'],float(np.min(C)));maxima['C_max']=max(maxima['C_max'],float(np.max(C)))
    initial=result.y[:,0];end=result.y[:,-1]
    c0=fine.curvature_coefficients(initial);c1=fine.curvature_coefficients(end)
    maxima.update(initial_B_l1=float(np.sum(abs(initial[:m]))),initial_C_mean=float(c0[0]),
        initial_C_mean_gap=float(c0[0]+1/a0),initial_total_turn=float(-2*np.pi*a0*c0[0]),
        initial_turn_number=float(-a0*c0[0]),free_outer_C_mean=float(c1[0]),
        outer_nonmean_C_boundary_gap_l1=float(np.sum(abs(c1[1:]-right_target))))
    return maxima


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--modes',type=int,default=24);p.add_argument('--angles',type=int,default=384)
    p.add_argument('--right',type=float,default=.25);p.add_argument('--radial-nodes',type=int,default=251)
    p.add_argument('--tol',type=float,default=1e-5);p.add_argument('--max-nodes',type=int,default=3000)
    p.add_argument('--initial',choices=['old','rotational'],default='old')
    p.add_argument('--amplitudes',default='1');p.add_argument('--guess',type=Path)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--candidate',type=Path,required=True)
    args=p.parse_args();started=time.monotonic();amplitudes=[float(x) for x in args.amplitudes.split(',')]
    if args.angles<8*args.modes or args.angles%4:raise ValueError('insufficient angular grid')
    geometry,definition=load_exact_object(args.object,512);system=LogTwoEnded(geometry,args.modes,args.angles)
    m=args.modes;n=2*m+1;r=np.linspace(0.,args.right,args.radial_nodes)
    a0=scalar_target(geometry,0.)['a'];right_old=system.old_fields(args.right)[m+1:]
    if args.initial=='old':guess=np.column_stack([system.old_guess(x) for x in r])
    else:
        guess=np.zeros((n,len(r)))
        for j in range(0,len(r),128):
            t=geometry.radial_target_metric(r[j:j+128]);speed=t['a_x']/np.sqrt(t['E'])
            if np.max(abs(speed))>=1:raise ValueError('rotational reference is not real')
            guess[m,j:j+128]=np.log(np.sqrt(1-speed*speed)/t['a'])
    if args.guess:
        saved=load_candidate(args.guess);meta=json.loads(str(saved['metadata']))
        if meta['object_sha256']!=sha(args.object) or meta['coordinates']!='B,W=log(-C)':
            raise ValueError('different target or coordinate chart in guess')
        pm=int(meta['modes']);prior=PPoly(saved['piece_coefficients'],saved['radial_nodes'])(r).T
        count=min(pm,m);guess[:count]=prior[:count];guess[m:m+count+1]=prior[pm:pm+count+1]
    attempts=[]
    for amplitude in amplitudes:
        def bc(left,right):
            cl=system.curvature_coefficients(left);cr=system.curvature_coefficients(right)
            return np.concatenate([left[:m],[cl[0]+1/a0],cr[1:]-amplitude*right_old])
        def bc_jac(left,right):
            jl=np.zeros((n,n));jr=np.zeros((n,n));jl[np.arange(m),np.arange(m)]=1
            Cl=-np.exp(system.cos.T@left[m:]);Cr=-np.exp(system.cos.T@right[m:])
            dl=(system.proj*Cl)@system.cos.T;dr=(system.proj*Cr)@system.cos.T
            jl[m,m:]=dl[0];jr[m+1:,m:]=dr[1:]
            return jl,jr
        print(dict(boundary_amplitude=amplitude,modes=m,initial=args.initial),flush=True)
        result=solve_bvp(system.evaluate,bc,r,guess,fun_jac=system.jacobian,bc_jac=bc_jac,
            tol=args.tol,bc_tol=args.tol/100,max_nodes=args.max_nodes,verbose=1)
        row=dict(amplitude=amplitude,success=bool(result.success),status=int(result.status),message=result.message,
            nodes=len(result.x),iterations=int(result.niter),max_collocation_rms_residual=float(np.max(result.rms_residuals)),
            boundary_residual=float(np.max(abs(bc(result.y[:,0],result.y[:,-1])))),elapsed=time.monotonic()-started)
        attempts.append(row);print(row,flush=True)
        if not result.success:break
        r=result.x;guess=result.y
    diagnostic=diagnostics(system,result,a0,amplitude*right_old)
    meta=dict(kind='floating_finite_log_curvature_Codazzi_BVP',coordinates='B,W=log(-C)',modes=m,
        object_sha256=sha(args.object),source_sha256=sha(__file__),boundary_amplitude=amplitude,
        state_order='B sine k=1..M, W cosine k=0..M',physical_frequency_factor=4,
        original_target_fixed=True,initial_waist_curve_changed=True,
        right_boundary='scaled old actual nonmean C only, no cap DN, outer C mean free')
    save_npz_gz(args.candidate,radial_nodes=result.x,piece_coefficients=result.sol.c,initial_state=result.y[:,0],
        right_boundary_C_nonmean=amplitude*right_old,metadata=np.array(json.dumps(meta)))
    doc=dict(**meta,certified=False,success=bool(result.success and amplitude==amplitudes[-1]),attempts=attempts,
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],primitive_nodes=512,angular_grid=args.angles,
        diagnostic_grid=2*args.angles,right=args.right,tol=args.tol,max_nodes=args.max_nodes,
        initialization=args.initial,requested_amplitudes=amplitudes,initial_radial_nodes=args.radial_nodes,
        guess_path=str(args.guess) if args.guess else None,guess_sha256=sha(args.guess) if args.guess else None,
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),diagnostics=diagnostic,
        exact_initial_mean_repair='W_mean=-log(a_true(0)*mean(exp(W_nonmean))); then C0=-exp(W_mean+W_nonmean) has mean -1/a_true(0).',
        exact_initial_closure='Integrate beta_theta=-a_true(0)*C0-1 with zero mean beta. Its pi/2-periodicity makes the tangent i exp(i theta+i beta) close by fourfold symmetry; X0=ez gives identity frame holonomy.',
        mean_retained=True,regular_trace=None,regular_flux=None,whole_parameter_interval=False,
        whole_real_angular_circle=False,whole_radial_domain=False,
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in
            ('fourfold_phase_codazzi_two_end_probe.py','fourfold_phase_codazzi_two_end_homotopy_probe.py',
             'fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py','fourfold_phase_core_low_block.py',
             'fourfold_phase_local_correction_probe.py')},
        wall_seconds=time.monotonic()-started,
        limitations=['Floating finite Fourier/radial BVP only; no unprojected PDE validation or infinite-tail bound.',
            'The negative-C chart is exact for real finite W, but an arbitrarily small C is not excluded by the coordinate alone.',
            'The initial waist curve changes, and only a chosen nonmean C outer boundary is imposed.',
            'Mean/turning gaps above are sampled diagnostics. The stated exact mean repair is necessary before promoting a new initial curve.'])
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print(dict(success=doc['success'],diagnostics=diagnostic,wall_seconds=doc['wall_seconds']),flush=True)


if __name__=='__main__':main()
