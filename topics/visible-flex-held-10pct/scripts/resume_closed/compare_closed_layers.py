#!/usr/bin/env python3
"""Compare two accepted fixed-g explicit closed maps in common material charts.

The prefix comparison uses the identical physical meridian coordinate and
material angle, inverting each finite C2 angle chart. Tail comparisons cancel
the common exact rotational background and include the single mean gauge.
This is a sampled radial / Fourier-norm diagnostic, not a C2 convergence proof.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"finite_closure/m3_m8_closed_map"))
import argparse,hashlib,importlib.util,json,math,time
import numpy as np
from m3_shared_prefix import load_prefix,M3SharedPrefix,M3CartesianPrefix,TailCutTarget,CartesianCutLift
from phase_angle_chart import PhaseAngleChart
from paired_prefix_jets import physical_jets

p=argparse.ArgumentParser(description=__doc__)
for k in ['source-topic','short-bridge','coarse-checkpoint','fine-checkpoint','coarse-port','fine-port',
          'coarse-manifest','fine-manifest','tail-reader','cap-source','out']:
    p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--angular',type=int,default=256);p.add_argument('--batch',type=int,default=16)
a=p.parse_args();started=time.monotonic()
spec=importlib.util.spec_from_file_location('compare_closed_cap',a.cap_source);capmod=importlib.util.module_from_spec(spec);spec.loader.exec_module(capmod)
def build(cp,port,manifest):
    r,obj,flow,sol,_=load_prefix(a.source_topic,a.short_bridge,cp,port,512)
    model=M3CartesianPrefix(M3SharedPrefix(obj,flow,sol),32)
    cap=capmod.FiniteClosedTail(manifest,a.tail_reader);target=TailCutTarget(model,cap)
    model.end_lift=CartesianCutLift(model,target,.04)
    return dict(record=r,prefix=model,cap=cap,target=target,angle=PhaseAngleChart(model))
c=build(a.coarse_checkpoint,a.coarse_port,a.coarse_manifest)
f=build(a.fine_checkpoint,a.fine_port,a.fine_manifest)
keys=['frozen_profile','chart','warp_reference_q','physical_tail_parameters','physical_tail_cut','meridian_length']
for k in keys:
    if c['record'][k]!=f['record'][k]:raise ValueError('Physical g changed: '+k)
for k in ['a','b','c']:
    if getattr(c['cap'],k)!=getattr(f['cap'],k):raise ValueError('Closure radial anchor changed: '+k)
end=c['prefix'].flow.end;theta=2*np.pi*np.arange(a.angular)/a.angular
s=np.unique(np.r_[c['prefix'].rep.x,f['prefix'].rep.x,
    (c['prefix'].rep.x[:-1]+c['prefix'].rep.x[1:])/2,
    (f['prefix'].rep.x[:-1]+f['prefix'].rep.x[1:])/2,
    np.linspace(0,.04,81),np.linspace(end-.04,end,81)])
prefix_diff=np.zeros(6);prefix_metric=np.zeros((2,2));interface=np.zeros((2,6))
for first in range(0,len(s),a.batch):
    ss=s[first:first+a.batch]
    jj=[physical_jets(z['prefix'],z['angle'],ss,theta)for z in [c,f]]
    prefix_diff=np.maximum(prefix_diff,[np.max(np.linalg.norm(jj[1][j]-jj[0][j],axis=2))for j in range(6)])
    rad=c['prefix'].flow.profile(ss)[0][:,None]
    for k,J in enumerate(jj):
        Fs,Ft=J[1],J[3]
        e=np.sum(Fs*Fs,axis=2)-1;ff=np.sum(Fs*Ft,axis=2)/rad;g=np.sum(Ft*Ft,axis=2)/rad**2-1
        op=(abs(e+g)+np.sqrt((e-g)**2+4*ff*ff))/2
        co=np.fft.fft(np.stack([e,ff,g],axis=2),axis=1)/a.angular
        l1=np.sum(abs(co),axis=1);row=np.maximum(l1[:,0]+l1[:,1],l1[:,2]+l1[:,1])
        prefix_metric[k]=np.maximum(prefix_metric[k],[op.max(),row.max()])
    if first%(a.batch*30)==0:print(json.dumps({'event':'paired_prefix','done':first+len(ss),'total':len(s)}),flush=True)

gauge=[z['target'].zcut+z['target'].mean for z in [c,f]]
delta_gauge=gauge[1]-gauge[0]
caps=[z['cap']for z in [c,f]]
rr=np.unique(np.r_[caps[0].finite.r,caps[1].finite.r,
    (caps[0].finite.r[:-1]+caps[0].finite.r[1:])/2,
    (caps[1].finite.r[:-1]+caps[1].finite.r[1:])/2,
    np.linspace(float(caps[0].a),float(caps[0].b),65,dtype=np.longdouble),np.longdouble(c['target'].R)])
pm=np.union1d(caps[0].finite.planar_modes,caps[1].finite.planar_modes)
hm=np.union1d(caps[0].finite.height_modes,caps[1].finite.height_modes);P=len(pm);C=P+len(hm)
px={int(k):j for j,k in enumerate(pm)};hz={int(k):P+j for j,k in enumerate(hm)}
def tail_coeff(z,R):
    out=[np.zeros((len(R),C),dtype=np.longdouble)for _ in range(3)]
    cut=R==np.longdouble(z['target'].R);use=~cut
    vals=[np.zeros((len(R),z['cap'].finite.C),dtype=np.longdouble)for _ in range(3)]
    vR,r1,r2=z['target'].perturbation_radius(R)
    if np.any(use):
        vv=z['cap'].coefficients(vR[use])
        vals[0][use]=vv[0];vals[1][use]=vv[1]*r1[use,None]
        vals[2][use]=vv[2]*r1[use,None]**2+vv[1]*r2[use,None]
    if np.any(cut):
        for j in range(3):vals[j][cut]=z['target'].A[j]
    idx=[px[int(k)]for k in z['cap'].finite.planar_modes]+[hz[int(k)]for k in z['cap'].finite.height_modes]
    for j in range(3):out[j][:,idx]=vals[j]
    return out
tail_diff=np.zeros(6);tail_first_covariant=0.;tail_second_covariant=0.
for first in range(0,len(rr),128):
    R=rr[first:first+128];vv=[tail_coeff(z,R)for z in [c,f]]
    diff=[y-x for x,y in zip(vv[0],vv[1])]
    for j in range(3):diff[j][:,P:]*=-1
    diff[0][:,hz[0]]+=delta_gauge
    norms={}
    for radial,angular in [(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]:
        d=diff[radial];planar=np.sum(abs(d[:,:P])*abs(pm)**angular,axis=1)
        height=np.sum(abs(d[:,P:])*hm**angular,axis=1)
        norms[(radial,angular)]=np.sqrt(planar*planar+height*height)
    tail_diff=np.maximum(tail_diff,[float(norms[k].max())for k in [(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]])
    v1=norms[(1,0)];vt=norms[(0,1)];v2=norms[(2,0)];vrt=norms[(1,1)];vtt=norms[(0,2)]
    first_bound=np.sqrt(v1*v1+(vt/R)**2)
    h0=v2+8*.41*math.sqrt(1+.41**2)*v1;h1=vrt/R+vt/R**2;h2=vtt/R**2+v1/R
    second_bound=np.sqrt(h0*h0+2*h1*h1+h2*h2)
    tail_first_covariant=max(tail_first_covariant,float(first_bound.max()))
    tail_second_covariant=max(tail_second_covariant,float(second_bound.max()))

out=dict(scope=__doc__,source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in
    [Path(__file__),Path(__file__).with_name('paired_prefix_jets.py'),Path(__import__('m3_shared_prefix').__file__),Path(__import__('phase_angle_chart').__file__)]},
    inputs={str(x.resolve()):hashlib.sha256(x.read_bytes()).hexdigest()for x in [a.coarse_checkpoint,a.fine_checkpoint,a.coarse_port,a.fine_port,a.coarse_manifest,a.fine_manifest]},
    fixed_g_identical_fields=keys,actual_q=[z['record']['actual_primary_amplitude']for z in [c,f]],
    prefix_samples=dict(radial=len(s),angular=a.angular,coordinates='common physical (s,theta), with each explicit C2 chart inverted'),
    prefix_six_jet_difference_maxima=prefix_diff.tolist(),prefix_metric_diagnostics_coarse_fine=prefix_metric.tolist(),
    prefix_metric_columns=['sampled_relative_operator_norm','sampled_angle_Fourier_l1_row_sum'],
    tail_radial_samples=len(rr),tail_six_jet_angular_l1_difference_maxima=tail_diff.tolist(),
    tail_sampled_covariant_first_difference_upper=tail_first_covariant,tail_sampled_covariant_second_difference_upper=tail_second_covariant,
    new_minus_old_cap_mean_gauge=delta_gauge,tail_background_cancels_identically=True,
    closed_metric_continuous_certificate=False,C2_limit_proved=False,seconds=time.monotonic()-started)
a.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['prefix_six_jet_difference_maxima','prefix_metric_diagnostics_coarse_fine','tail_six_jet_angular_l1_difference_maxima','new_minus_old_cap_mean_gauge','seconds']}),flush=True)
