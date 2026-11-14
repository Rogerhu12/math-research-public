#!/usr/bin/env python3
"""Actual finite-BVP linear response of natural c6 to design directions.

One Jacobian at a successful two-control warm checkpoint is factored. Each
physical profile direction is differentiated in that same numerical chart;
the coupled delta/LB and all free core coefficients respond through the
actual collocation equations. Additional actual q1/q4 directions use exact
inlet derivatives at fixed reference angle chart, with no physical-profile
change inserted directly. These are tangent predictions, never new solved
surfaces, fixed-g refinement, or existence/obstruction certificates.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,gc,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
from scipy.integrate import _bvp
from strong_block_qr import BlockQRFactor
P=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--response-output',type=Path,required=True)
    parser.add_argument('--response-fields',default='boost_speed,vu,descending_turn_curvature,start_acceleration')
    parser.add_argument('--third-target-factor',type=float,default=.95)
    parser.add_argument('--target-primary',type=float)
    opts,remaining=parser.parse_known_args();sys.argv=[sys.argv[0]]+remaining
    hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ('strong_control_response.py','strong_neck_bvp.py','strong_block_qr.py')}
    spec=importlib.util.spec_from_file_location('strong_response_runner',P/'strong_neck_bvp.py')
    runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
    original=runner.module

    def inspect_solver(fun,bc,x,y,p,**kw):
        begin=time.time();obj=fun.__self__;n,m=y.shape;k=len(p);h=np.diff(x)
        col,jac=_bvp.prepare_sys(n,m,k,fun,bc,kw['fun_jac'],kw['bc_jac'],x,h)
        def vector():
            cr,ym,ff,fm=col(y,p);br=bc(y[:,0],y[:,-1],p)
            return np.r_[cr.ravel(order='F'),br]
        cr,ym,ff,fm=col(y,p);br=bc(y[:,0],y[:,-1],p)
        obj.initial(p);baseline_profile=dict(obj.flow(p[0]).cfg)
        coefficients=np.asarray(obj._core.coefficients).copy()
        baseline=dict(profile=baseline_profile,coefficients=coefficients.tolist(),
            scaled_collocation_max=float(np.max(abs(cr)/(h[None,:]*(1+abs(fm))))),
            boundary_max=float(np.max(abs(br))),numerical_reference_coefficients=obj.ref_coeff.tolist())
        start=time.time();J=jac(y,p,ym,ff,fm,br);jac_seconds=time.time()-start
        if hasattr(J,'matvec'):
            from root_block_collocation import DirectBlockQRFactor
            Factor=DirectBlockQRFactor
            hashes['root_block_collocation.py']=hashlib.sha256((P/'root_block_collocation.py').read_bytes()).hexdigest()
        else:Factor=BlockQRFactor
        start=time.time();factor=Factor(J,n,m,k);factor_seconds=time.time()-start;gc.collect()
        print(json.dumps(dict(event='response_factor',n=n,nodes=m,parameters=k,jacobian_seconds=jac_seconds,factor_seconds=factor_seconds)),flush=True)
        rows=[];target_delta=(opts.third_target_factor-1)*coefficients[2]

        def record(name,dR,steps=None,second=None):
            direction=-factor.solve(dR);dp=direction[n*m:]
            dc=np.zeros(len(coefficients));dc[2:]=dp[2:]*obj.pscale[1:]
            if name=='actual_q1':dc[0]=1.
            if name=='actual_q4':dc[1]=1.
            if hasattr(J,'matvec'):
                ay=abs(direction[:n*m]).reshape(m,n);ap=abs(dp);scale=0.
                for lo in range(0,m-1,24):
                    hi=min(lo+24,m-1)
                    denom=(np.einsum('mij,mj->mi',abs(J.a[lo:hi]),ay[lo:hi])
                           +np.einsum('mij,mj->mi',abs(J.b[lo:hi]),ay[lo+1:hi+1])
                           +np.einsum('mik,k->mi',abs(J.c[lo:hi]),ap)
                           +abs(dR[lo*n:hi*n]).reshape(hi-lo,n))
                    scale=max(scale,float(denom.max()))
                scale=max(scale,float(np.max(abs(J.boundary_a)@ay[0]+abs(J.boundary_b)@ay[-1]+abs(J.boundary_p)@ap+abs(dR[n*(m-1):]))))
                residual=J.matvec(direction)+dR
            else:
                scale=float(np.max(abs(J)@abs(direction)+abs(dR)));residual=J@direction+dR
            scale=max(scale,np.finfo(float).tiny)
            row=dict(direction=name,parameter_derivative=dp.tolist(),core_derivative=dc.tolist(),
                     equation_relative_backward_error=float(np.max(abs(residual))/scale),
                     physical_state_derivative_max=float(np.max(abs(direction[:n*m])))*obj.q)
            if steps is not None:row['finite_difference_steps']=steps
            if second is not None:
                d2=-factor.solve(second);p2=d2[n*m:]
                row['half_step_c6_derivative']=float(p2[2]*obj.pscale[1])
                row['half_step_c6_relative_difference']=float(abs(p2[2]-dp[2])/max(abs(dp[2]),np.finfo(float).tiny))
            if dc[2]!=0:
                step=target_delta/dc[2];profile=dict(baseline_profile)
                profile['delta']+=float(step*dp[0]);profile[obj.second_control]+=float(step*dp[1])
                if name not in ('actual_q1','actual_q4'):profile[name]+=float(step)
                row['target_c6_tangent_prediction']=dict(target=float(coefficients[2]+target_delta),direction_step=float(step),
                    physical_profile=profile,actual_core_coefficients=(coefficients+step*dc).tolist(),
                    scope='First derivative prediction only. A separate full nonlinear solve is mandatory.')
            rows.append(row);print(json.dumps(row),flush=True)

        # A prescribed q4 changes the actual inlet curve, while the numerical
        # reference chart remains exactly the old chart. This is analytic at
        # fixed arclength and does not perturb the profile itself.
        obj.select(p);obj.initial(p);f=obj.flow(p[0]);N=max(2048,128*obj.M)
        gi=f.general_core_chart.inlet_geometry(N);B,_,_=f.basis(N)
        inlet_derivatives=f.project(obj._core.parameter_derivatives(gi['theta']),B)/obj.q
        for name,index in [('actual_q1',0),('actual_q4',1)]:
            dR=np.zeros(n*m+k);dR[n*(m-1):n*m]=-inlet_derivatives[:,index]
            record(name,dR)
        for field in filter(None,opts.response_fields.split(',')):
            if field in ('delta',obj.second_control):raise ValueError('An already coupled control is not an external direction')
            if field not in obj.cfg:raise ValueError('Unknown physical design field '+field)
            value=float(obj.cfg[field]);step=2e-6*max(.1,abs(value));derivatives=[]
            try:
                for width in (step,step/2):
                    obj.cfg[field]=value+width;obj._flow_key=None;plus=vector();gc.collect()
                    obj.cfg[field]=value-width;obj._flow_key=None;minus=vector();gc.collect()
                    derivatives.append((plus-minus)/(2*width))
            finally:
                obj.cfg[field]=value;obj._flow_key=None;obj.select(p);obj.flow(p[0]);obj.initial(p);gc.collect()
            record(field,derivatives[0],[step,step/2],derivatives[1])
        joint=None
        if opts.target_primary is not None:
            r1=next(row for row in rows if row['direction']=='actual_q1')
            r4=next(row for row in rows if row['direction']=='actual_q4')
            dq1=opts.target_primary-coefficients[0]
            dq4=(target_delta-dq1*r1['core_derivative'][2])/r4['core_derivative'][2]
            dp=dq1*np.asarray(r1['parameter_derivative'])+dq4*np.asarray(r4['parameter_derivative'])
            dc=dq1*np.asarray(r1['core_derivative'])+dq4*np.asarray(r4['core_derivative'])
            profile=dict(baseline_profile);profile['delta']+=float(dp[0]);profile[obj.second_control]+=float(dp[1])
            joint=dict(target_primary=opts.target_primary,target_c6=float(coefficients[2]+target_delta),
                       actual_q4_step=float(dq4),physical_profile=profile,
                       actual_core_coefficients=(coefficients+dc).tolist(),
                       scope='Joint q1/q4 tangent prediction at fixed reference chart and fixed gauge; no nonlinear solution claimed.')
        result=dict(scope=__doc__,inspection_only=True,nonlinear_solution=False,
                    modes=obj.M,angular=obj.nt,nodes=m,baseline=baseline,rows=rows,
                    requested_third_factor=opts.third_target_factor,joint_tangent_prediction=joint,
                    jacobian_seconds=jac_seconds,factor_seconds=factor_seconds,
                    source_sha256=hashes,seconds=time.time()-begin)
        opts.response_output.write_text(json.dumps(result,indent=2)+'\n')
        raise RuntimeError('Response inspection complete; no nonlinear solve requested')

    def module(name,path):
        loaded=original(name,path)
        if Path(path).name=='root_dual_core_bvp.py':loaded.solve_bvp=inspect_solver
        return loaded
    runner.module=module;runner.main()

if __name__=='__main__':main()
