#!/usr/bin/env python3
"""Mode-two adaptive-chart finite-prefix design experiment.

Runs the same Cartesian Frenet BVP as the documented mode-three source,
with every mode-dependent chart derivative changed consistently to mode 2.
The tail port is a *finite linear* DN. Neither it nor a solved prefix is a
closed isometric surface. Physical parameters may vary in design runs;
only --fixed freezes the profile for later numerical refinement.
The transformation operates in memory, leaves all source files unchanged,
and records SHA256 of each source plus the exact replacements.
"""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse, hashlib, importlib.util, json, math, sys, time, types, subprocess
from pathlib import Path
sys.dont_write_bytecode=True
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.optimize import brentq

TRANSFORMS={}

def source_revision(source_topic):
    origin=source_topic/'source-origin.json'
    if origin.is_file():return json.loads(origin.read_text())['source_revision']
    return subprocess.check_output(['git','-C',str(source_topic),'rev-parse','HEAD'],text=True).strip()

def source_module(name,path,replacements=()):
    source=Path(path).read_text(); original=source
    applied=[]
    for old,new in replacements:
        count=source.count(old)
        if not count: raise ValueError('Absent source transformation: '+repr(old))
        source=source.replace(old,new);applied.append([old,new,count])
    module=types.ModuleType(name);module.__file__=str(path);sys.modules[name]=module
    exec(compile(source,str(path),'exec'),module.__dict__)
    TRANSFORMS[str(path)]={'sha256':hashlib.sha256(original.encode()).hexdigest(),'replacements':applied}
    return module


def load(source_topic):
    S=source_topic/'scripts';N=source_topic/'notes';source_root=source_topic/'repro/source-root'
    sys.path[:0]=[str(N),str(source_root/'topics/large-amplitude-twist-flex/scripts')]
    # The numerical q guard is not a geometric theorem. Convexity is checked
    # directly by PlanarSupportCore, including all higher support modes.
    source_module('fixed_metric_mode3_bvp',N/'fixed_metric_mode3_bvp.py',[
        ('self.q<.2','self.q<.48'),('q<.2','q<.48')])
    old=source_module('numerical_mode2_warp',S/'950f-prefix-warped-bvp.py',[
        ('self.warp_e=8*float(warp_q)','self.warp_e=3*float(warp_q)'),
        ('3*psi','2*psi'),('3*theta','2*theta'),
        ('/3','/2'),('rho1=3*e','rho1=2*e'),
        ('cfg,port,q,M,angular,3,fixed','cfg,port,q,M,angular,2,fixed'),
        ('self.pscale,3)','self.pscale,2)'),('q<.124','q<.48')
    ])
    pre="spec=importlib.util.spec_from_file_location('prefixwarp',HERE/'950f-prefix-warped-bvp.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)"
    adaptive=source_module('numerical_mode2_adaptive',S/'950f-prefix-adaptive-chart-bvp-v2.py',[
        (pre,"old=sys.modules['numerical_mode2_warp']"),
        ('3*psi','2*psi'),('3*theta','2*theta'),('3*np.arange','2*np.arange'),
        ('*sn/3','*sn/2'),('rho_p=3*e','rho_p=2*e'),('rho_ps=3*ep','rho_ps=2*ep'),
        ('np.sin(2*theta)[:,:,None]*et/3','np.sin(2*theta)[:,:,None]*et/2'),
        ('max(64,self.nt),3,','max(64,self.nt),2,'),
        ('psi)/3-target','psi)/2-target')
    ])
    patch=source_module('numerical_mode2_flat',S/'db6f-prefix-flat-profile.py')
    patch.install(adaptive);adaptive.old.install_source(source_root)
    return adaptive


def dependencies(source_topic):
    result={}
    root=str(source_topic.resolve())
    for loaded in list(sys.modules.values()):
        filename=getattr(loaded,'__file__',None)
        if filename and str(Path(filename).resolve()).startswith(root+'/') and Path(filename).is_file():
            result[str(Path(filename).resolve().relative_to(source_topic.resolve()))]=hashlib.sha256(Path(filename).read_bytes()).hexdigest()
    return result


def run(a):
    start=time.time();a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    adaptive=load(a.source_topic)
    if a.jacobian=='fourier':
        backend=source_module('numerical_mode2_jacobian',a.source_topic/'scripts/78718-prefix-fourier-jacobian.py')
        backend.install(adaptive)
    from curve_stable_prefix_bvp import save_checkpoint
    from f6curve_domain_newton import install,STATS
    cfg=json.loads(a.profile.read_text());chart=json.loads(a.chart.read_text());port=json.loads(a.port.read_text())
    port['_sha256']=hashlib.sha256(a.port.read_bytes()).hexdigest()
    if cfg.get('prefix_bridge'):
        short=source_module('numerical_short_bridge',Path(__file__).with_name('root_short_bridge.py'))
        short.install();port['cut']={**port['cut'],'_prefix_bridge':cfg['prefix_bridge']}
    _,BVP=adaptive.build_classes(chart)
    obj=BVP(cfg,port,a.amplitude,a.modes,a.angular,a.fixed,a.warp_reference)
    if hasattr(obj.bridge,'breakpoints'):
        f=obj.flow(0.)
        obj.chart_breaks=np.unique(np.r_[obj.chart_breaks,obj.inverse_chart(f.prefix_end+obj.bridge.breakpoints,0.)])
    obj.restart_remesh=a.nodes;obj.bcweights=np.full(obj.M,a.physical_bc_tol/a.bc_tol)
    if a.scan:
        values=[];roots=[];previous=None
        for d in np.geomspace(.003,.8,60):
            try:
                f=obj.Flow({**cfg,'delta':d},port,obj.M,obj.q,obj.nt,2,obj.bridge)
                v=float(f.backward_line().core[1]);values.append([float(d),v])
                if previous and previous[1]*v<0:
                    def target(x):return float(obj.Flow({**cfg,'delta':x},port,obj.M,obj.q,obj.nt,2,obj.bridge).backward_line().core[1])
                    root=brentq(target,previous[0],float(d),xtol=2e-12);roots.append(root)
                previous=(float(d),v)
            except Exception as e:values.append([float(d),repr(e)]);previous=None
        result={'scope':'linear branch design roots only','profile':cfg,'roots':roots,'sampled_values':values,'source_transforms':TRANSFORMS,'seconds':time.time()-start}
        a.out_prefix.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({'roots':roots,'seconds':result['seconds']}),flush=True);return
    summary={'scope':__doc__,'source_git_head':source_revision(a.source_topic),'solver_success':False,'requested_amplitude':a.amplitude,'requested_modes':a.modes,'source_transforms':TRANSFORMS}
    try:
        if a.restart:x,y,par=obj.restart(a.restart)
        else:x,y,par=obj.seed(a.nodes)
        install()
        print(json.dumps({'event':'start','amplitude':a.amplitude,'modes':a.modes,'nodes':len(x),'delta':cfg['delta']}),flush=True)
        sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=a.tol,bc_tol=a.bc_tol,max_nodes=a.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
        f=obj.flow(sol.p[0]);obj.initial(sol.p)
        physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
        physical.sol=f.c2_interpolant(physical)
        frozen=cfg if a.fixed else {**cfg,'delta':cfg['delta']+sol.p[0]}
        out={'scope':__doc__,'source_git_head':summary['source_git_head'],'angular_chart':'frozen-spline-adaptive-v1','chart':chart,'warp_reference_q':a.warp_reference,
             'config':dict(modes=obj.M,base_mode=2,core_kind='adaptive_warped_support',angular=obj.nt,tol=a.tol,bc_tol=a.bc_tol,physical_bc_tol=a.physical_bc_tol,fixed_metric=a.fixed,actual_nonlinear_tail=False),
             'frozen_profile':frozen,'gauge_amplitude':obj.q,'actual_primary_amplitude':obj.support_amplitude,'meridian_length':f.end,
             'physical_port_sha256':port['_sha256'],'physical_tail_parameters':port['parameters'],'physical_tail_cut':port['cut'],
             'parameters':sol.p.tolist(),'central_correction_scales':obj.pscale.tolist(),'nodes':len(sol.x),'solver_success':bool(sol.success),
             'message':sol.message,'max_rms_collocation_residual':float(np.max(sol.rms_residuals)),
             'newton_domain_audit':dict(STATS),'mesh':physical.x.tolist(),'pp_coefficients':physical.sol.c,'source_transforms':TRANSFORMS}
        cp=a.out_prefix.with_suffix('.json.gz');save_checkpoint(cp,out)
        if sol.success or a.audit_failure:out['summary']=adaptive.audit(obj,physical,a.audit_angular)
        out['seconds']=time.time()-start;out['dependencies_sha256']=dependencies(a.source_topic);save_checkpoint(cp,out)
        summary={k:v for k,v in out.items()if k not in ('mesh','pp_coefficients')}
        print(json.dumps({'event':'result','success':sol.success,'delta':frozen['delta'],'amplitude':obj.support_amplitude,'core':obj._core.summary(),'seconds':out['seconds'],
                          'metrics':{k:v for k,v in out.get('summary',{}).items()if k in ['metric_l1','kappa_sample','height_max','radius_max','terminal_height_coeff_max']}}),flush=True)
    except Exception as e:summary['error']=repr(e);print(json.dumps({'event':'failure','error':repr(e)}),flush=True)
    summary['seconds']=time.time()-start
    summary['dependencies_sha256']=dependencies(a.source_topic)
    a.out_prefix.with_name(a.out_prefix.name+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('source-topic','profile','chart','port','out-prefix'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--amplitude',type=float,default=.01);p.add_argument('--warp-reference',type=float,default=.01)
    p.add_argument('--modes',type=int,default=4);p.add_argument('--angular',type=int,default=128);p.add_argument('--audit-angular',type=int,default=256)
    p.add_argument('--nodes',type=int,default=181);p.add_argument('--max-nodes',type=int,default=2200)
    p.add_argument('--tol',type=float,default=2e-7);p.add_argument('--bc-tol',type=float,default=1e-7);p.add_argument('--physical-bc-tol',type=float,default=2e-9)
    p.add_argument('--jacobian',choices=['original','fourier'],default='fourier')
    p.add_argument('--restart',type=Path);p.add_argument('--fixed',action='store_true');p.add_argument('--scan',action='store_true');p.add_argument('--audit-failure',action='store_true')
    run(p.parse_args())
