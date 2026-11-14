#!/usr/bin/env python3
"""Freeze the meridian metric and solve for the extrinsic planar-core aspect.

This only solves the finite Frenet prefix with the explicitly recorded Robin
port.  It neither closes the tail nor certifies a closed isometric family.
Unlike repo_scan_ellipse_bvp, no metric parameter is a BVP unknown.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,gzip,hashlib,json,math,sys,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from repo_scan_ellipse_bvp import EllipseBVP,install_source,audit
from repo_scan_ellipse_core import PlanarEllipseCore
from repo_scan_gentle import finite_value,scaled_port

class FixedMetricBVP(EllipseBVP):
    def __init__(self,cfg,port,aspect=1.2,modes=4,angular=128,arc_nodes=4096):
        super().__init__(cfg,port,aspect,modes,angular,arc_nodes)
        self.seed_aspect=aspect
        self.fixed_flow=self.Flow(self.cfg,self.port,self.bridge,self.M,self.q,self.nt)
        self._flow=self.fixed_flow;self._flow_key=0.
    def flow(self,p0):
        return self.fixed_flow
    def initial(self,p):
        key=tuple(np.asarray(p,float))
        if key!=self._core_key:
            aspect=1+(self.seed_aspect-1)*math.exp(float(p[0]))
            if not 1.0001<aspect<2.:
                raise FloatingPointError('extrinsic aspect outside search domain')
            core=PlanarEllipseCore(aspect,np.asarray(p[1:])*self.pscale,self.arc_nodes)
            C,metrics=core.inlet(self.fixed_flow,max(1024,64*self.M))
            self._initial=(C-self.fixed_flow.base(np.array([0.]))[:,0])/self.q
            self._core=core;self._inlet_metrics=metrics;self._core_key=key
            self.aspect=aspect
        return self._initial
    def fun(self,t,y,p):
        L=self.fixed_flow.end
        return L*self.fixed_flow.fun(np.asarray(t)*L,y,p)
    def fun_jac(self,t,y,p):
        L=self.fixed_flow.end
        J,_=self.fixed_flow.fun_jac(np.asarray(t)*L,y,p)
        return L*J,np.zeros((self.n,self.M,len(t)))
    def bc_jac(self,ya,yb,p):
        A,B,P=super().bc_jac(ya,yb,p)
        step=2e-6
        v=np.zeros(self.M);v[0]=step
        P[:self.n,0]=-(-self.initial(p+2*v)+8*self.initial(p+v)-8*self.initial(p-v)+self.initial(p-2*v))/(12*step)
        self.initial(p)
        return A,B,P
    def restart(self,path):
        from curve_stable_prefix_bvp import load_checkpoint
        old=load_checkpoint(path);M0=old['config']['modes'];q0=old['gauge_amplitude']
        if old['frozen_profile']!=self.cfg:
            raise ValueError('restart metric differs from the requested frozen metric')
        oa=old.get('actual_core_aspect',old['config']['aspect'])
        p=np.zeros(self.M);p[0]=math.log((oa-1)/(self.seed_aspect-1))
        oscale=np.asarray(old['central_correction_scales'])
        for j in range(1,min(M0,self.M)):
            p[j]=old['parameters'][j]*oscale[j-1]/self.pscale[j-1]
        ox=np.asarray(old['mesh']);L=old['meridian_length']
        if L!=self.fixed_flow.end:
            raise ValueError('restart meridian length differs')
        op=PPoly.construct_fast(np.asarray(old['pp_coefficients']),ox,extrapolate=True,axis=1)
        t=np.unique(np.r_[ox/L,self.fixed_flow.breaks/L])
        oy=op(t*L);y=np.zeros((self.n,len(t)))
        y[0]=oy[0]*q0/self.q
        for j in range(min(M0,self.M)):
            for ni,oi in [(1+j,1+j),(self.M+1+j,M0+1+j),(self.iz+j,2*M0+1+j)]:
                y[ni]=oy[oi]*q0/self.q
        return t,y,p

def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--source-root',type=Path,required=True)
    a.add_argument('--restart',type=Path,required=True)
    a.add_argument('--out-prefix',type=Path,required=True)
    a.add_argument('--modes',type=int,nargs='+',default=[4,8,12,16])
    a.add_argument('--angular',type=int,default=192)
    a.add_argument('--audit-angular',type=int,default=384)
    a.add_argument('--tol',type=float,default=2e-9)
    a.add_argument('--bc-tol',type=float,default=2e-10)
    a.add_argument('--max-nodes',type=int,default=3000)
    a.add_argument('--seed-aspect',type=float,default=1.2)
    args=a.parse_args();install_source(args.source_root)
    from curve_stable_prefix_bvp import load_checkpoint,save_checkpoint
    from f6curve_domain_newton import install,STATS
    from f6curve_outward_bridge_linear import read_port
    old=load_checkpoint(args.restart)
    cfg=old['frozen_profile']
    source=read_port(args.source_root/'topics/large-amplitude-twist-flex/notes/f6curve_wide_m2_r2_m16_linear_port.json')
    port=scaled_port(source,cfg['cut_radius'],cfg.get('cut_slope'),cfg.get('dimensionless_D'))
    install();report=dict(scope=__doc__,fixed_profile=cfg,fixed_port=port,
        source_restart=str(args.restart),source_hashes={},rows=[])
    for name in ['fixed_metric_ellipse_bvp.py','repo_scan_ellipse_bvp.py','repo_scan_ellipse_core.py','repo_scan_gentle.py']:
        report['source_hashes'][name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    prev=args.restart
    for M in args.modes:
        row=dict(modes=M,tol=args.tol,bc_tol=args.bc_tol,success=False)
        begin=time.time()
        try:
            obj=FixedMetricBVP(cfg,port,args.seed_aspect,M,args.angular)
            x,y,p=obj.restart(prev)
            print(json.dumps(dict(event='start',modes=M,nodes=len(x),delta=cfg['delta'])),flush=True)
            sol=solve_bvp(obj.fun,obj.bc,x,y,p,tol=args.tol,bc_tol=args.bc_tol,
                max_nodes=args.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac)
            flow=obj.fixed_flow;L=flow.end;obj.initial(sol.p)
            physical=SimpleNamespace(x=sol.x*L,y=sol.y,p=sol.p)
            physical.sol=flow.c2_interpolant(physical)
            out=dict(scope=__doc__,config=dict(modes=M,aspect=obj.seed_aspect,angular=args.angular,
                tol=args.tol,bc_tol=args.bc_tol),frozen_profile=cfg,gauge_amplitude=obj.q,
                meridian_length=L,parameters=sol.p.tolist(),actual_core_aspect=obj.aspect,
                central_correction_scales=obj.pscale.tolist(),nodes=len(sol.x),
                solver_success=bool(sol.success),message=sol.message,
                max_rms_collocation_residual=float(np.max(sol.rms_residuals)),
                newton_domain_audit=dict(STATS),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c)
            cp=args.out_prefix.with_name(args.out_prefix.name+f'_m{M}.json.gz')
            out=save_checkpoint(cp,out)
            metrics=audit(obj,physical,251,args.audit_angular)
            out['summary']=metrics;out['seconds']=time.time()-begin
            save_checkpoint(cp,out)
            row.update(success=bool(sol.success),message=sol.message,checkpoint=cp.name,
                actual_core_aspect=obj.aspect,nodes=len(sol.x),rms=out['max_rms_collocation_residual'],
                bc_max=float(np.max(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)))),**metrics)
            if sol.success:prev=cp
        except Exception as exc:
            row['error']=repr(exc)
        row['seconds']=time.time()-begin;report['rows'].append(finite_value(row))
        args.out_prefix.with_name(args.out_prefix.name+'_summary.json').write_text(json.dumps(finite_value(report),indent=2,allow_nan=False)+'\n')
        print(json.dumps({k:v for k,v in finite_value(row).items() if k in ['modes','success','actual_core_aspect','nodes','metric_l1','flow_defect','darboux_l1','kappa_sample','root_min','seconds','error','message']}),flush=True)
        if not row['success']:break

if __name__=='__main__':main()
