#!/usr/bin/env python3
"""Locate full physical residuals of one saved double-mode prefix.

The shadow ODE jet is a diagnostic at the same represented position, not a
replacement map or a convergence certificate. No physical parameter changes.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,json,sys
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
from run_dual_prefix import module,load_even,load_module,ReferenceCore,make_core_class


def load(args):
    source=args.source_topic.resolve()
    sys.path[:0]=[str(source/'notes'),str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
    ad=load_even(source,4)
    load_module('diagnostic_short_bridge',source.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py').install()
    from curve_stable_prefix_bvp import load_checkpoint
    rec=load_checkpoint(args.checkpoint)
    settings=rec['plateau_settings'];Core=make_core_class(ReferenceCore)
    coremod=__import__('fixed_metric_mode3_core')
    coremod.PlanarSupportCore=lambda q,corrections=(),base_mode=4:Core(q,corrections,base_mode,arc_nodes=1024,**settings)
    backend=module('diagnostic_fourier_jacobian',source/'scripts/78718-prefix-fourier-jacobian.py');backend.install(ad)
    Flow,BVP=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.))
    from exact_core_lift import install_core_lift
    BVP=install_core_lift(Flow,BVP)
    from analytic_adaptive_core_jac import install as analytic_install
    analytic_install(BVP)
    from dual_design_bvp import install as dual_install
    BVP=dual_install(Flow,BVP,settings['bimodal_eta'])
    cfg=rec['profile'];port=rec['physical_port'];M=rec['config']['modes'];q=rec['gauge_amplitude']
    obj=BVP(cfg,port,q,M,rec['config']['angular'],False,q)
    obj.pscale=np.asarray(rec['central_correction_scales']);obj.bcweights=np.full(M,.01)
    par=np.asarray(rec['parameters']);obj.initial(par);flow=obj.flow(par[0])
    mesh=np.asarray(rec['mesh']);pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),mesh,extrapolate=True,axis=1)
    return rec,obj,flow,par,mesh,pp


def evaluate(obj,flow,p,pp,ss,N,shadow=False):
    B,B1,B2=flow.basis(N);out={k:[]for k in ('metric_l1','metric_point','tensor_l1','flow_defect','root_min')}
    for first in range(0,len(ss),24):
        s=ss[first:first+24];Y=pp(s);Yp=flow.fun(s,Y,p)if shadow else pp(s,1)
        fr,Fsp,dW=flow.velocity_s(s,Y,Yp,B1,B2);g=fr['geo'];a,ap,app=flow.profile(s);rho=g['rho'];v=g['v']
        Ypp=flow.project(dW-g['s2'],B)/obj.q if shadow else pp(s,2)
        Fsc=g['s1']+obj.q*flow.values(Yp,B);Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
        Fssc=g['s2']+obj.q*flow.values(Ypp,B);Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
        Fs=Fsc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None]
        Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
        Fst=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None]
        Fss=Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']
        E=np.sum(Fs*Fs,axis=2);F=np.sum(Fs*Ft,axis=2);G=np.sum(Ft*Ft,axis=2)
        errors=np.stack((E-1,F/a[:,None],G/a[:,None]**2-1),axis=2)
        l1=np.sum(abs(np.fft.fft(errors,axis=1)/N),axis=1)
        out['metric_l1'].extend(l1.tolist());out['metric_point'].extend(np.max(abs(errors),axis=1).tolist())
        out['flow_defect'].extend(np.max(np.linalg.norm(Fs-fr['Vnormal'],axis=2),axis=1).tolist())
        out['root_min'].extend(np.min(fr['margin'],axis=1).tolist())
        Hst=(Fst-ap[:,None,None]/a[:,None,None]*Ft)/a[:,None,None]
        Htt=(Ftt+(a*ap)[:,None,None]*Fs)/a[:,None,None]**2
        gram=np.eye(3)[None,None,:,:]-Fs[:,:,:,None]*Fs[:,:,None,:]-(Ft/a[:,None,None])[:,:,:,None]*(Ft/a[:,None,None])[:,:,None,:]
        tensor=.5*(Fss[:,:,:,None]*Htt[:,:,None,:]+Htt[:,:,:,None]*Fss[:,:,None,:])-Hst[:,:,:,None]*Hst[:,:,None,:]+(app/a)[:,None,None,None]*gram
        ft=np.fft.fft(tensor,axis=1)/N
        out['tensor_l1'].extend(np.sum(np.sqrt(np.sum(abs(ft)**2,axis=(2,3))),axis=1).tolist())
    return {k:np.asarray(v)for k,v in out.items()}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angular',type=int,default=512);a=p.parse_args()
    rec,obj,f,par,mesh,pp=load(a)
    critical=np.unique(np.r_[f.breaks,.5*f.prefix_end,.9*f.prefix_end,.75*f.end])
    sets=dict(nodes=mesh,midpoints=(mesh[:-1]+mesh[1:])/2,
              audit=np.unique(np.r_[np.linspace(0,f.end,151),mesh,(mesh[:-1]+mesh[1:])/2]))
    result=dict(scope=__doc__,checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
                q=obj.q,modes=obj.M,parameters=par.tolist(),physical_profile=rec['physical_profile'],
                code_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in Path(__file__).parent.glob('*.py')},groups={})
    for key,s in sets.items():
        group={}
        for shadow in (False,True):
            values=evaluate(obj,f,par,pp,s,a.angular,shadow)
            def locate(name):
                z=values[name];j=np.unravel_index(np.argmax(z),z.shape);at=float(s[j[0]])
                ci=int(np.argmin(abs(critical-at)));mi=int(np.clip(np.searchsorted(mesh,at)-1,0,len(mesh)-2))
                return dict(value=float(z[j]),s=at,component=None if len(j)==1 else int(j[1]),
                    physical_critical=float(critical[ci]),critical_distance=float(abs(critical[ci]-at)),
                    interval=[float(mesh[mi]),float(mesh[mi+1])])
            group['shadow_projected_ode'if shadow else 'saved_C2_map']={k:locate(k)for k in ('metric_l1','metric_point','tensor_l1','flow_defect')}
            group['shadow_projected_ode'if shadow else 'saved_C2_map']['root_min']=float(values['root_min'].min())
        result['groups'][key]=group
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['groups'],indent=2))


if __name__=='__main__':main()
