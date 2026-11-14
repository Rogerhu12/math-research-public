#!/usr/bin/env python3
"""Finite normalized nonlinear Codazzi branch for an explicit compact metric.

E_nu=E exp(nu*h), h supported in .05<|r|<.18.  At amplitude alpha,
B=alpha*b and C=Cref_nu+alpha*c.  This normalization has a regular
alpha=0 Jacobi limit.  The unknown nu enforces a fixed waist fourth mode;
all retained complementary modes and the C mean are present.  The true
R74 LINEAR stable-center rows are used at 25/8.  Nonlinear tail/mean
matching is explicitly not claimed.  Every result here is floating only.
"""
from __future__ import annotations
import argparse,inspect,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
import scipy
import scipy.integrate._bvp as bvp
from scipy.integrate import solve_bvp,solve_ivp
from scipy.sparse.linalg import splu
from flint import ctx
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_two_end_probe import TwoEnded,save_npz_gz
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_codazzi_compact_metric_return_probe import bumps
from fourfold_phase_local_correction_probe import sha


class CompactNormalized(TwoEnded):
    def __init__(self,geometry,modes,angles,body,graft):
        super().__init__(geometry,modes,angles)
        self.body=body;self.graft=graft;self.alpha=0.;self.target_calls=0

    def base(self,r):
        r=np.atleast_1d(np.asarray(r,dtype=float));key=r.tobytes()
        if key not in self.cache:
            if len(self.cache)>=8:self.cache.pop(next(iter(self.cache)))
            out=np.empty((6,len(r)));indices=np.flatnonzero(r<=3)
            for start in range(0,len(indices),32):
                ii=indices[start:start+32];t=self.body.values(r[ii])
                out[:,ii]=[t['a'],t['gamma'],t['beta'],t['K'],t['lambda_ref'],t['Cref']]
            for i in np.flatnonzero(r>3):
                t=self.graft.point(float(r[i]));out[:,i]=[t['a'],t['gamma'],t['beta'],t['K'],t['lambda_ref'],t['Cref']]
            self.cache[key]=out;self.target_calls+=1
        return self.cache[key]

    def controlled(self,r,nu):
        a,g,b,K,ell,Cr=self.base(r);h,hp=bumps(r);h,hp=h[0],hp[0]
        G=g*g;D=a*a*G*Cr*Cr;exp=np.exp(nu*h);Dn=D+G*np.expm1(nu*h)
        if np.any(Dn<=0) or not np.all(np.isfinite(Dn)):
            raise ValueError('controlled rotational chart denominator is nonpositive')
        gn=g*np.sqrt(exp);Kn=(K+b*nu*hp/(2*a*a*G))/exp
        ln=(ell*D+b*nu*hp/2)/Dn;Cn=Cr*np.sqrt(Dn/(D*exp))
        dg=gn*h/2;dD=G*exp*h
        dl=(b*hp/2-ln*dD)/Dn
        dC=Cn*h*b*b/(2*Dn)
        return a,gn,b,Kn,ln,Cn,dg,dl,dC

    def normalized_fields(self,y):return super().fields(y)

    def actual_fields(self,r,y,p):
        Cr=self.controlled(r,float(p[0]))[5];B,C=self.normalized_fields(y)
        return self.alpha*B,Cr+self.alpha*C

    def data(self,r,y,p):
        t=self.controlled(r,float(p[0]));a,g,b,K,ell,Cr,dg,dl,dCr=t
        B,c=self.normalized_fields(y);C=Cr+self.alpha*c
        if np.any(C==0):raise ZeroDivisionError('actual C vanishes')
        # Exact algebra avoids subtracting two large reference A values.
        A=-ell*c+self.alpha*(B*B+ell*c*c)/C
        return t,B,c,C,A

    def evaluate(self,r,y,p):
        t,B,c,C,A=self.data(r,y,p);a,g,b,K,ell,Cr,dg,dl,dCr=t;m=self.modes
        ac=self.proj@A;out=np.empty_like(y)
        out[:m]=-g*self.frequency[:,None]*ac[1:]-2*b*y[:m]
        out[m:]=b*(ac-y[m:]);out[m+1:]+=g*self.frequency[:,None]*y[:m]
        self.calls+=1
        if time.monotonic()-self.last_log>20:
            print(dict(amplitude=self.alpha,nu=float(p[0]),rhs_calls=self.calls,jac_calls=self.jac_calls,
                radial_nodes=len(r),sampled_C_min=float(np.min(C)),sampled_C_max=float(np.max(C))),flush=True)
            self.last_log=time.monotonic()
        return out

    def jacobian(self,r,y,p):
        t,B,c,C,A=self.data(r,y,p);a,g,b,K,ell,Cr,dg,dl,dCr=t;m=self.modes;n=2*m+1
        AB=2*self.alpha*B/C;Ac=-(ell*Cr*Cr+self.alpha*self.alpha*B*B)/(C*C)
        da_b=np.einsum('an,nr,bn->abr',self.proj,AB,self.sin,optimize=True)
        da_c=np.einsum('an,nr,bn->abr',self.proj,Ac,self.cos,optimize=True)
        da=np.concatenate([da_b,da_c],axis=1);out=np.empty((n,n,len(r)))
        out[:m]=-g*self.frequency[:,None,None]*da[1:];out[m:]=b*da
        for k in range(m):
            out[k,k]-=2*b;out[m+1+k,k]+=g*self.frequency[k]
        for k in range(m+1):out[m+k,m+k]-=b
        dA=-dl*c+self.alpha*dl*c*c/C-self.alpha*(B*B+ell*c*c)*dCr/(C*C)
        ap=self.proj@dA;ac=self.proj@A;dp=np.empty((n,1,len(r)))
        dp[:m,0]=-self.frequency[:,None]*(dg*ac[1:]+g*ap[1:])
        dp[m:,0]=b*ap;dp[m+1:,0]+=dg*self.frequency[:,None]*y[:m]
        self.jac_calls+=1;return out,dp


def guarded_parameter_newton(system,history,floor,ceiling,maxnu,max_iterations):
    def feasible(r,y,p):
        if not np.all(np.isfinite(y)) or not np.all(np.isfinite(p)) or abs(p[0])>=maxnu:return False
        try:B,C=system.actual_fields(r,y,p)
        except (ValueError,ZeroDivisionError,FloatingPointError):return False
        return bool(np.all(np.isfinite(B)) and np.all(np.isfinite(C)) and
            np.all(C < -floor) and np.all(C > -ceiling) and np.all(abs(B)<ceiling))
    def newton(n,m,h,col_fun,bc,jac,y,p,singular_projection,bvp_tol,bc_tol):
        r=np.r_[0.,np.cumsum(h)];midr=r[:-1]+h/2;threshold=(2/3)*h*.05*bvp_tol
        if not feasible(r,y,p):
            history.append(dict(reason='initial iterate leaves chosen actual C/nu search domain',nodes=m,nu=float(p[0])))
            return y,p,True
        for iteration in range(max_iterations):
            col,mid,f,fmid=col_fun(y,p);boundary=bc(y[:,0],y[:,-1],p)
            if not feasible(midr,mid,p) or not all(np.all(np.isfinite(z)) for z in (col,mid,f,fmid,boundary)):
                history.append(dict(reason='current midpoint leaves chosen actual search domain',nodes=m,iteration=iteration))
                return y,p,True
            residual=np.r_[col.ravel(order='F'),boundary]
            if np.all(abs(col)<threshold*(1+abs(fmid))) and np.all(abs(boundary)<bc_tol):
                history.append(dict(reason='collocation Newton tolerance reached',nodes=m,iteration=iteration,nu=float(p[0])))
                return y,p,False
            try:factor=splu(jac(y,p,mid,f,fmid,boundary))
            except RuntimeError:
                history.append(dict(reason='linear factorization failed',nodes=m,iteration=iteration));return y,p,True
            step=factor.solve(residual);cost=float(step@step)
            if not np.isfinite(cost):
                history.append(dict(reason='nonfinite normalized Newton correction',nodes=m,iteration=iteration));return y,p,True
            dy=step[:n*m].reshape(n,m,order='F');dp=step[n*m:];accepted=False;fraction=1.
            for trial in range(24):
                proposed=y-fraction*dy;newp=p-fraction*dp
                if singular_projection is not None:proposed[:,0]=singular_projection@proposed[:,0]
                if feasible(r,proposed,newp):
                    cc,mm,ff,fm=col_fun(proposed,newp);bb=bc(proposed[:,0],proposed[:,-1],newp)
                    if feasible(midr,mm,newp) and all(np.all(np.isfinite(z)) for z in (cc,mm,ff,fm,bb)):
                        rr=np.r_[cc.ravel(order='F'),bb];correction=factor.solve(rr);newcost=float(correction@correction)
                        if np.isfinite(newcost) and newcost<(1-.1*fraction)*cost:accepted=True;break
                fraction*=.5
            history.append(dict(nodes=m,iteration=iteration,accepted=accepted,step_fraction=fraction,
                nu=float(p[0]),proposed_nu=float(newp[0]),affine_invariant_cost=cost,next_cost=newcost if accepted else None,
                max_collocation_residual=float(np.max(abs(col))),max_boundary_residual=float(np.max(abs(boundary)))))
            if not accepted:
                history.append(dict(reason='no admissible decreasing step in 24 backtracks; not an asserted singularity',nodes=m))
                return y,p,True
            y,p=proposed,newp
        history.append(dict(reason='per-mesh Newton iteration limit',nodes=m,iterations=max_iterations));return y,p,False
    return newton


def diagnostic(system,result):
    if not np.all(np.isfinite(result.sol.c)):return dict(valid=False,reason='nonfinite collocation polynomial')
    fine=CompactNormalized(system.geometry,system.modes,2*system.angular_grid,system.body,system.graft)
    fine.alpha=system.alpha;m=system.modes;p=result.p
    rr=np.unique(np.r_[result.x,*[result.x[:-1]+z*np.diff(result.x) for z in (.25,.5,.75)]])
    out=dict(normalized_finite_residual=0.,normalized_full_B_residual=0.,normalized_full_C_residual=0.,
        normalized_A_projection_defect=0.,C_min=np.inf,C_max=-np.inf,B_abs_max=0.)
    for start in range(0,len(rr),32):
        r=rr[start:start+32];y=result.sol(r);yr=result.sol(r,1)
        try:t,B,c,C,A=fine.data(r,y,p)
        except (ValueError,ZeroDivisionError):return dict(valid=False,reason='invalid actual C/reference diagnostic sample')
        a,g,b,K,ell,Cr,dg,dl,dCr=t
        Bt=fine.cos[1:].T@(fine.frequency[:,None]*y[:m]);ct=-fine.sin.T@(fine.frequency[:,None]*y[m+1:])
        At=(2*fine.alpha*B/C)*Bt-(ell*Cr*Cr+fine.alpha*fine.alpha*B*B)*ct/(C*C)
        RB=fine.sin.T@yr[:m]-g*At+2*b*B
        RC=fine.cos.T@yr[m:]-g*Bt-b*(A-c)
        finite=yr-system.evaluate(r,y,p);ac=fine.proj@A
        values=dict(normalized_finite_residual=max(float(np.max(abs(system.sin.T@finite[:m]))),float(np.max(abs(system.cos.T@finite[m:])))),
            normalized_full_B_residual=float(np.max(abs(RB))),normalized_full_C_residual=float(np.max(abs(RC))),
            normalized_A_projection_defect=float(np.max(abs(A-fine.cos.T@ac))))
        if not all(np.isfinite(z) for z in values.values()):return dict(valid=False,reason='nonfinite normalized rational residual')
        for name,value in values.items():out[name]=max(out[name],value)
        out['C_min']=min(out['C_min'],float(np.min(C)));out['C_max']=max(out['C_max'],float(np.max(C)))
        out['B_abs_max']=max(out['B_abs_max'],float(np.max(abs(system.alpha*B))))
    out.update(actual_full_B_residual=system.alpha*out['normalized_full_B_residual'],
        actual_full_C_residual=system.alpha*out['normalized_full_C_residual'],
        actual_A_projection_defect=system.alpha*out['normalized_A_projection_defect'],
        radial_samples='nodes and quarter/mid/three-quarter points',radial_sample_count=len(rr),
        valid=bool(out['C_max']<0 and out['C_min']>-np.inf))
    return out


def jacobian_audit(system):
    r=np.array([.02,.08,.12,.17,.25,1.,3.07]);m=system.modes;n=2*m+1
    y=np.zeros((n,len(r)));y[0]=.025;y[m+1]=-.2;y[m]=.01
    system.alpha=.2;p=np.array([.001]);J,Jp=system.jacobian(r,y,p);h=1e-6
    fd=(system.evaluate(r,y,p+h)-system.evaluate(r,y,p-h))/(2*h)
    parameter=float(np.max(abs(fd-Jp[:,0]))/(1+np.max(abs(Jp))))
    errors=[]
    for col in (0,m,m+1,n-1):
        z=np.zeros_like(y);z[col]=h
        fd=(system.evaluate(r,y+z,p)-system.evaluate(r,y-z,p))/(2*h)
        errors.append(float(np.max(abs(fd-J[:,col]))/(1+np.max(abs(J[:,col])))))
    passed=bool(parameter<2e-6 and max(errors)<2e-6);system.alpha=0.
    if not passed:raise ValueError('analytic normalized/parameter Jacobian disagrees with independent finite difference')
    return dict(passed=passed,diagnostic_only=True,radial_points=r.tolist(),central_step=h,
        parameter_relative_error=parameter,state_relative_errors=errors)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--modes',type=int,default=16);ap.add_argument('--angles',type=int,default=256)
    ap.add_argument('--amplitudes',default='0,0.025,0.05,0.1,0.2,0.35,0.5,0.65')
    ap.add_argument('--mean-boundary',choices=['waist','outer'],default='waist')
    ap.add_argument('--nu-initial',type=float,default=.0009455711279349692)
    ap.add_argument('--max-nu',type=float,default=.2);ap.add_argument('--C-floor',type=float,default=.02)
    ap.add_argument('--field-ceiling',type=float,default=30.);ap.add_argument('--newton-iterations',type=int,default=24)
    ap.add_argument('--tol',type=float,default=2e-6);ap.add_argument('--max-nodes',type=int,default=3500)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--candidate',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists() or args.candidate.exists():raise FileExistsError('refusing to overwrite a compact metric branch diagnostic')
    if args.angles<8*args.modes or args.modes<2:raise ValueError('invalid finite angular resolution')
    amplitudes=[float(x) for x in args.amplitudes.split(',')]
    if not amplitudes or amplitudes[0]!=0 or any(x<0 for x in amplitudes):raise ValueError('start with the normalized zero-amplitude Jacobi limit')
    geometry,definition=load_exact_object(args.object,512);body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    system=CompactNormalized(geometry,args.modes,args.angles,body,graft);m=args.modes;n=2*m+1
    audit=jacobian_audit(system);qstar=1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)
    nu=np.array([args.nu_initial]);seed_calls=0
    def seed_rhs(r,z):
        nonlocal seed_calls
        seed_calls+=1;a,g,b,K,ell,Cr,*_=system.controlled([r],nu[0]);g,b,ell=g[0],b[0],ell[0];q=z[0]
        return [4*g*(q*q-ell)+b*(ell-1)*q,-4*g*q-b*(ell+1)]
    seed=solve_ivp(seed_rhs,(3.125,0.),[qstar,0.],method='DOP853',rtol=2e-9,atol=2e-11,max_step=.004,dense_output=True)
    if not seed.success or seed.t[-1]!=0 or not np.all(np.isfinite(seed.y)):raise ValueError('true body/graft Riccati warm start failed')
    r=np.unique(np.r_[np.linspace(0,.3,241),np.linspace(.3,1.,121),np.linspace(1.,3.,161),np.linspace(3.,3.125,25)])
    z=seed.sol(r);c=-np.exp(z[1]-seed.sol(0.)[1]);guess=np.zeros((n,len(r)));guess[0]=-z[0]*c;guess[m+1]=c
    def bc(left,right,p):
        mean=left[m] if args.mean_boundary=='waist' else right[m]
        return np.r_[left[:m],mean,left[m+1]+1,right[:m]+qstar*right[m+1:]]
    def bc_jac(left,right,p):
        jl=np.zeros((n+1,n));jr=np.zeros_like(jl);jp=np.zeros((n+1,1))
        jl[np.arange(m),np.arange(m)]=1
        if args.mean_boundary=='waist':jl[m,m]=1
        else:jr[m,m]=1
        jl[m+1,m+1]=1;jr[np.arange(m+2,n+1),np.arange(m)]=1
        jr[np.arange(m+2,n+1),np.arange(m+1,n)]=qstar
        return jl,jr,jp
    attempts=[];last=None;last_alpha=None;failed=None
    for alpha in amplitudes:
        system.alpha=alpha;history=[];old=bvp.solve_newton
        bvp.solve_newton=guarded_parameter_newton(system,history,args.C_floor,args.field_ceiling,args.max_nu,args.newton_iterations)
        try:result=solve_bvp(system.evaluate,bc,r,guess,p=nu,fun_jac=system.jacobian,bc_jac=bc_jac,
            tol=args.tol,bc_tol=args.tol/100,max_nodes=args.max_nodes,verbose=1)
        finally:bvp.solve_newton=old
        dd=diagnostic(system,result);success=bool(result.success and dd['valid']);left,right=result.y[:,0],result.y[:,-1]
        a0=system.base([0.])[0,0];Cr0=system.controlled([0.],result.p[0])[5][0];CrR=system.controlled([3.125],result.p[0])[5][0]
        waistC=alpha*left[m:].copy();waistC[0]+=Cr0;outerC=alpha*right[m:].copy();outerC[0]+=CrR
        item=dict(amplitude=alpha,nu=float(result.p[0]),exact_float_nu=str(Fraction(float(result.p[0]))),
            success=success,solver_status=int(result.status),solver_message=result.message,radial_nodes=len(result.x),
            diagnostics=dd,guarded_Newton_history=history,waist_mean_C=float(waistC[0]),
            waist_mean_closure_gap=float(waistC[0]+1/a0),waist_turn_number=float(-a0*waistC[0]),
            waist_total_turn=float(-2*np.pi*a0*waistC[0]),waist_B_coefficients=(alpha*left[:m]).tolist(),
            waist_C_coefficients=waistC.tolist(),outer_B_coefficients=(alpha*right[:m]).tolist(),outer_C_coefficients=outerC.tolist(),
            outer_C_mean_minus_reference=float(alpha*right[m]),
            normalized_outer_regular_linear_residual_l1=float(np.sum(abs(right[:m]+qstar*right[m+1:]))),
            maximum_boundary_residual=float(np.max(abs(bc(left,right,result.p)))))
        attempts.append(item);print(dict(alpha=alpha,nu=item['nu'],success=success,diagnostics=dd,
            waist_mean_gap=item['waist_mean_closure_gap'],outer_mean_gap=item['outer_C_mean_minus_reference']),flush=True)
        if not success:failed=(result,alpha);break
        last,last_alpha=result,alpha;r,guess,nu=result.x,result.y,result.p
    chosen=last if last is not None else failed[0];chosen_alpha=last_alpha if last is not None else failed[1]
    meta=dict(kind='floating_compact_metric_normalized_Codazzi_branch',coordinates='B=alpha*b; C=Cref_nu+alpha*c',
        normalized_state_order='b sine k=1..M, c cosine k=0..M',modes=m,physical_frequency_factor=4,
        amplitude=chosen_alpha,nu=float(chosen.p[0]),exact_float_nu=str(Fraction(float(chosen.p[0]))),
        source_sha256=sha(__file__),object_sha256=sha(args.object),new_metric_family='E_nu=E exp(nu*h); a fixed',
        exact_bump='h=4096 t^6(1-t)^6 for t=(|r|-1/20)/(13/100) in (0,1), zero elsewhere',
        mean_boundary=args.mean_boundary,original_target_fixed=bool(float(chosen.p[0])==0),
        old_waist_branch_reused=False,waist_nonmean_complement_allowed_to_change=True,
        outer_boundary='Complete retained R74 regular LINEAR stable-center rows; nonlinear tail terms unpaid.')
    save_npz_gz(args.candidate,radial_nodes=chosen.x,piece_coefficients=chosen.sol.c,initial_state=chosen.y[:,0],metadata=np.array(json.dumps(meta)))
    failed_path=None
    if failed is not None and failed[0] is not chosen:
        failed_path=args.candidate.with_name(args.candidate.name.replace('.npz.gz','-failed.npz.gz'))
        if failed_path.exists():raise FileExistsError('refusing to overwrite failed compact candidate')
        fm=dict(meta,amplitude=failed[1],nu=float(failed[0].p[0]),exact_float_nu=str(Fraction(float(failed[0].p[0]))),finite_BVP_success=False)
        save_npz_gz(failed_path,radial_nodes=failed[0].x,piece_coefficients=failed[0].sol.c,initial_state=failed[0].y[:,0],metadata=np.array(json.dumps(fm)))
    report=dict(**meta,certified=False,finite_BVP_success=last is not None,
        reached_requested_amplitude=bool(last_alpha==amplitudes[-1]),attempts=attempts,requested_amplitudes=amplitudes,
        requested_interval=['0','25/8'],angular_grid=args.angles,diagnostic_angular_grid=2*args.angles,
        primitive_nodes=512,tol=args.tol,max_nodes=args.max_nodes,analytic_Jacobian_audit=audit,
        seed_rhs_calls=seed_calls,seed_waist_q=float(seed.y[0,-1]),seed_message=seed.message,
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        failed_candidate_path=str(failed_path) if failed_path else None,failed_candidate_sha256=sha(failed_path) if failed_path else None,
        mean_retained=True,regular_mean_height=None,regular_mean_flux=None,nonlinear_regular_tail=None,
        whole_affine_parameter_interval=False,whole_real_angular_circle=False,whole_radial_interval=False,
        scipy_version=scipy.__version__,scipy_collocation_module_sha256=sha(inspect.getsourcefile(bvp)),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_compact_metric_return_probe.py','fourfold_phase_codazzi_two_end_probe.py',
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_codazzi_rotational_cap_jacobi_probe.py',
            'fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        limitations=['Floating finite Fourier/radial boundary model, no continuous PDE or parameter certificate.',
            'nu changes the target on .05<|r|<.18; existing g0 proofs do not transfer there.',
            'The waist curve is also changed by the complementary C modes; old exact waist Cauchy branches are not reused.',
            'The selected mean boundary is explicit; the opposite mean is an output, not an erased matching row.',
            'Every nonlinear regular tail term, true non-fourth-mode linear fee, mean height and flux remain unpaid.',
            'The normalized alpha=0 result is a Jacobi eigenfunction; it is not a nonrotational nonlinear surface.',
            'Neither a guard stop nor a large residual is a mathematical nonexistence theorem.'],
        wall_seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(dict(last_amplitude=last_alpha,nu=float(chosen.p[0]),reached=report['reached_requested_amplitude'],
        candidate=str(args.candidate),wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
