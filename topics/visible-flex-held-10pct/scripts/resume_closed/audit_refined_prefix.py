#!/usr/bin/env python3
"""Audit a refined finite Cartesian C2 prefix in its explicit C2 material angle.

Audits are finite samples unless an explicit analytic inequality is stated.
No BVP is rerun; no old/coarse endpoint packet is substituted.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"finite_closure/m3_m8_closed_map"))
import argparse,hashlib,importlib.util,json,time,sys
import numpy as np
from m3_shared_prefix import load_prefix,M3SharedPrefix,M3CartesianPrefix,TailCutTarget,CartesianCutLift
from phase_angle_chart import PhaseAngleChart

p=argparse.ArgumentParser(description=__doc__)
for k in ['source-topic','short-bridge','checkpoint','port','tail-manifest','tail-reader','cap-source','outdir']:p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--angular',type=int,default=512);p.add_argument('--radial',type=int,default=1025)
p.add_argument('--center-width',type=float,default=.04);p.add_argument('--cut-width',type=float,default=.04)
a=p.parse_args();out=a.outdir;out.mkdir(parents=True,exist_ok=False);started=time.monotonic()
r,obj,flow,sol,raw=load_prefix(a.source_topic,a.short_bridge,a.checkpoint,a.port,a.angular)
base=M3SharedPrefix(obj,flow,sol,a.center_width);model=M3CartesianPrefix(base,32)
spec=importlib.util.spec_from_file_location('m3_cap_source',a.cap_source);capmod=importlib.util.module_from_spec(spec);spec.loader.exec_module(capmod)
tail=capmod.FiniteClosedTail(a.tail_manifest,a.tail_reader)
target=TailCutTarget(model,tail);lift=CartesianCutLift(model,target,a.cut_width)
psi=2*np.pi*np.arange(a.angular)/a.angular
delta=lift.delta(psi)
delta_sup=np.array([[np.linalg.norm(x,axis=1).max()for x in d]for d in delta])
delta_fourier=np.array([[np.sum(np.sqrt(np.sum(abs(np.fft.fft(x,axis=0)/a.angular)**2,axis=1)))for x in d]for d in delta])
center_delta=model.center_delta(psi)
model.end_lift=lift
phase_chart=PhaseAngleChart(model)
np.savez_compressed(out/'prefix-shared-cartesian.npz',knots=model.rep.x,jets=model.rep.jets,
    planar_modes=model.pm,height_modes=model.hm,core_frequencies=model.core.frequencies,
    core_coefficients=model.core.coefficients,mean_knots=sol.mean_spline.x,mean_jets=sol.mean_spline.jets,phase_knots=phase_chart.rep.x,phase_jets=phase_chart.rep.jets)
print(json.dumps({'event':'built','q':r['actual_primary_amplitude'],'nodes':len(model.rep.x),'delta_sample_norms':delta_sup.tolist(),'delta_fft_norms':delta_fourier.tolist()}),flush=True)
ss=np.unique(np.r_[np.linspace(0,flow.end,a.radial),model.rep.x,
    (model.rep.x[:-1]+model.rep.x[1:])/2,flow.breaks,
    np.linspace(0,a.center_width,161),np.linspace(flow.end-a.cut_width,flow.end,161)])
maxima={k:0. for k in ['metric_l1','curvature','radius','height','representation_position_change','representation_first_change','representation_second_change']}
minima={k:float('inf')for k in ['support','area','xy_radius']};center=None
beforemax={'metric_l1':0.,'curvature':0.}
def metric_curvature(jets,g,rad):
    X,Xs,Xss,Xp,Xpp,Xsp=jets
    Fs=Xs-g['v'][:,:,None]*Xp;Ft=Xp/g['rho'][:,:,None]
    errors=np.stack([np.sum(Fs*Fs,axis=2)-1,np.sum(Fs*Ft,axis=2)/rad[:,None],
                    np.sum(Ft*Ft,axis=2)/rad[:,None]**2-1],axis=2)
    metric=float(np.sum(abs(np.fft.fft(errors,axis=1)/a.angular),axis=1).max())
    cross=np.cross(Xp,Xs);area=np.linalg.norm(cross,axis=2);normal=cross/area[:,:,None]
    E,F,G=[np.sum(U*V,axis=2)for U,V in [(Xs,Xs),(Xs,Xp),(Xp,Xp)]]
    L,M,N=[np.sum(U*normal,axis=2)for U in [Xss,Xsp,Xpp]]
    det=E*G-F*F;tr=(L*G-2*M*F+N*E)/det;kg=(L*N-M*M)/det
    kap=(abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*kg)))/2
    return metric,float(kap.max()),normal,area,Fs
for first in range(0,len(ss),24):
    s=ss[first:first+24];vals=model.grid(s,a.angular);jets,g=vals[:-1],vals[-1]
    theta,rho,rhop,ts,tss,rhos=phase_chart.angular(s[:,None],psi[None,:])
    g=dict(g,theta=theta,rho=rho,rhop=rhop,v=ts/rho,vp=(rhos*rho-ts*rhop)/rho**2,vs=(tss*rho-ts*rhos)/rho**2)
    rad=flow.profile(s)[0];metric,K,normal,area,Fs=metric_curvature(jets,g,rad)
    maxima['metric_l1']=max(maxima['metric_l1'],metric);maxima['curvature']=max(maxima['curvature'],K)
    X,Xs,Xss,Xp,Xpp,Xsp=jets
    maxima['radius']=max(maxima['radius'],float(np.linalg.norm(X,axis=2).max()))
    maxima['height']=max(maxima['height'],float(X[:,:,2].max()))
    minima['support']=min(minima['support'],float(np.sum(X*normal,axis=2).min()))
    minima['area']=min(minima['area'],float(area.min()));minima['xy_radius']=min(minima['xy_radius'],float(np.linalg.norm(X[:,:,:2],axis=2).min()))
    old=base.grid(s,a.angular)[:-1]
    for key,j in [('representation_position_change',0),('representation_first_change',1),('representation_second_change',2)]:
        maxima[key]=max(maxima[key],float(np.linalg.norm(jets[j]-old[j],axis=2).max()))
    before_metric,before_K,*_=metric_curvature(old,g,rad)
    beforemax['metric_l1']=max(beforemax['metric_l1'],before_metric);beforemax['curvature']=max(beforemax['curvature'],before_K)
    if first==0:
        core=model.core.evaluate(g['theta'][0]);ez=np.zeros_like(Fs[0]);ez[:,2]=1
        Fss=Xss-2*g['v'][:,:,None]*Xsp+g['v'][:,:,None]**2*Xpp+(g['v']*g['vp']-g['vs'])[:,:,None]*Xp
        center=dict(position=float(np.linalg.norm(X[0]-core['F'],axis=1).max()),Fs=float(np.linalg.norm(Fs[0]-ez,axis=1).max()),Fss=float(np.linalg.norm(Fss[0],axis=1).max()))
actual=model.evaluate([flow.end],psi);targ=target.angular_jets(psi)
expected=[targ[0][0],targ[0][1],targ[0][2],targ[1][0],targ[2][0],targ[1][1]]
seam={key:float(np.linalg.norm(arr[0]-goal,axis=1).max())for key,arr,goal in zip(['X','Xs','Xss','Xpsi','Xpsipsi','Xspsi'],actual,expected)}
report=dict(scope=__doc__,argv=sys.argv,checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
    tail_manifest_sha256=hashlib.sha256(a.tail_manifest.read_bytes()).hexdigest(),
    source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),Path(__import__('m3_shared_prefix').__file__),Path(__import__('shared_jet').__file__),Path(__import__('phase_angle_chart').__file__),a.cap_source]},
    actual_q=r['actual_primary_amplitude'],modes=r['config']['modes'],fixed_profile=r['frozen_profile'],core=model.core.summary(),explicit_c2_material_angle=phase_chart.report(),
    angular=a.angular,radial_samples=len(ss),cartesian_coefficients=model.C,shared_knots=len(model.rep.x),inserted_knots=model.inserted_knots,
    center_width=a.center_width,cut_width=a.cut_width,
    exact_c2_reason='Finite shared-2jet Cartesian coefficient quintics; exact analytic core lift; endpoint lift uses the same full angular function as tail cut. C2 is algebraic, not a residual tolerance.',
    delta_angular_by_radial_jet_sample_norms=delta_sup.tolist(),delta_angular_by_radial_jet_fft_l1=delta_fourier.tolist(),
    center_delta_sample_norms=[[float(np.linalg.norm(x,axis=1).max())for x in d]for d in center_delta],
    sampled_maxima=maxima,sampled_minima=minima,before_cartesian_and_cut_lift_sampled=beforemax,
    center_numerical_identity_check=center,seam_numerical_identity_check=seam,
    zcut_mean=target.zcut,tail_mean_at_cut_approx=target.mean,
    outer_radius_adjustment=float(tail.c-np.longdouble(target.R)),outer_adjustment_width=.02,
    target_cut_jets=[target.R,target.ap,target.app],bvp_solves=0,seconds=time.monotonic()-started,
    whole_closed_embedding_or_reach_certified=False)
(out/'prefix-common-audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'event':'done','maxima':maxima,'minima':minima,'center':center,'seam':seam,'seconds':report['seconds']}),flush=True)
