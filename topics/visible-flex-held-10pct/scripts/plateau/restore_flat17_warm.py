"""Pull back one immutable flat17 seed into the exact-core lift chart.
This constructs an initial guess; it asserts no solution or convergence.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import importlib.util,sys,json,math,argparse
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly
from plateau_core import PlateauSupportCore
from exact_core_lift import install_core_lift
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--input',type=Path,required=True);p.add_argument('--profile',type=Path,required=True);p.add_argument('--port-file',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--chart-out',type=Path,required=True);p.add_argument('--constant-chart',action='store_true');a=p.parse_args();SOURCE=a.source_topic.resolve();a.out.parent.mkdir(parents=True,exist_ok=True)
sys.path[:0]=[str(SOURCE/'notes'),str(SOURCE/'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
def load(n,p):
 sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
ad=load('warm_ad',SOURCE/'scripts/950f-prefix-adaptive-chart-bvp-v2.py');patch=load('warm_flat',SOURCE/'scripts/db6f-prefix-flat-profile.py');patch.install(ad);ad.old.install_source(SOURCE/'repro/source-root')
from curve_stable_prefix_bvp import load_checkpoint,save_checkpoint
from fixed_metric_mode3_core import PlanarSupportCore as OriginalCore
rec=load_checkpoint(a.input)
port=json.loads(a.port_file.read_text());base=json.loads(a.profile.read_text());q=rec['gauge_amplitude'];M=4;target_chart=dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.) if a.constant_chart else rec['chart'];a.chart_out.write_text(json.dumps(target_chart,indent=2)+'\n')
OldFlow,_=ad.build_classes(rec['chart']);of=OldFlow(rec['frozen_profile'],port,M,q,256,3,warp_q=rec['warp_reference_q'])
NewFlow,NewBVP=ad.build_classes(target_chart);NewBVP=install_core_lift(NewFlow,NewBVP)
# No source class is modified until the old core's defining parameters are read.
oldcore=OriginalCore(q,np.array(rec['parameters'][1:])*np.array(rec['central_correction_scales']),3)
import fixed_metric_mode3_core as cm
cm.PlanarSupportCore=lambda q,corrections=(),base_mode=3:PlateauSupportCore(q,corrections,base_mode,halfwidth=.5,transition=.05,homotopy=0.,arc_nodes=2048)
# Warped constructor closes over the original symbol, so build its class again.
NewFlow,NewBVP=ad.build_classes(target_chart);NewBVP=install_core_lift(NewFlow,NewBVP)
obj=NewBVP(base,port,q,M,256,False,q);obj.pscale=np.full(M-1,q);obj.bcweights=np.full(M,.01)
p=np.zeros(M);p[0]=rec['frozen_profile']['delta']-base['delta'];nf=obj.flow(p[0]);theta=2*np.pi*np.arange(2048)/2048;B,_,_=nf.basis(2048)
newcore=PlateauSupportCore(q,np.zeros(M-1),halfwidth=.5,transition=.05,homotopy=0.)
J=nf.project(newcore.parameter_derivatives(theta)[1:],B);target=nf.project((oldcore.evaluate(theta)['F']-newcore.evaluate(theta)['F'])[None,:,:],B)[:,0]
c=np.linalg.lstsq(J,target,rcond=None)[0];p[1:]=c/q;obj.initial(p)
s=np.array(rec['mesh']);pp=PPoly.construct_fast(np.array(rec['pp_coefficients']),s,extrapolate=True,axis=1);oy=pp(s);y=np.empty_like(oy);freq=3*np.arange(1,M+1);N=1024;B,_,_=nf.basis(N)
for first in range(0,len(s),32):
 sl=slice(first,first+32);ss=s[sl];target=nf.geo(ss,N)['theta'];e=of.geo(ss,1)['e'][:,None];psi=target.copy()
 for _ in range(40):
  d=(psi-e*np.sin(3*psi)/3-target)/(1-e*np.cos(3*psi));psi-=d
  if np.max(abs(d))<2e-14:break
 co=np.cos(psi[:,:,None]*freq);si=np.sin(psi[:,:,None]*freq);cc=oy[:,sl].T
 R=cc[:,0,None]+np.einsum('npk,nk->np',co,cc[:,1:M+1]);T=np.einsum('npk,nk->np',si,cc[:,M+1:2*M+1]);Z=np.einsum('npk,nk->np',co,cc[:,2*M+1:]);V=np.stack((R*np.cos(psi)-T*np.sin(psi),R*np.sin(psi)+T*np.cos(psi),Z),axis=-1)
 a=nf.profile(ss)[0];circle=np.stack((a[:,None]*np.cos(target),a[:,None]*np.sin(target),np.zeros_like(target)),axis=-1);lift=nf.geo(ss,N)['pos']-circle
 y[:,sl]=nf.project(V-lift/q,B)
correction=obj.initial(p)-y[:,0];cutoff=nf.Tu/2;y+=correction[:,None]*np.maximum(0,1-s/cutoff)[None,:]**3
physical=SimpleNamespace(x=s,y=y,p=p);physical.sol=nf.c2_interpolant(physical)
out=a.out;save_checkpoint(out,dict(scope=__doc__,config=dict(modes=M,base_mode=3,core_kind='plateau_core',exact_core_lift=True,angular=256,fixed_metric=False),profile=base,parameters=p.tolist(),central_correction_scales=obj.pscale.tolist(),gauge_amplitude=q,mesh=s.tolist(),pp_coefficients=physical.sol.c,physical_port=port,meridian_length=nf.end))
print(json.dumps(dict(out=str(out),parameters=p.tolist(),physical_core_corrections=c.tolist(),input_twojet_projection=obj.unlifted_projection)),flush=True)
