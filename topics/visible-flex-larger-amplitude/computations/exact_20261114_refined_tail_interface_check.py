#!/usr/bin/env python3
"""Small actual-data readout for the new assembly interface, not a full audit.

Checks direct Fourier cut jets against the saved quintic at a common cut mean
anchor and compares the new Fourier evaluation with the prior Cartesian
Hermite consumer at its saved metric/curvature witnesses. No prefix mean
primitive, whole surface, nonlinear solve or global reach check is run here.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import json
import time
from pathlib import Path
import numpy as np
from exact_20261114_refined_tail_adapter import RefinedTail,RefinedAssembly,module,sha

HERE=Path(__file__).resolve().parent


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','checkpoint','port','complete','refined-background','plan','heights','base-metric','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--old-metric-source',type=Path,default=HERE/'exact_20261114_background_preserving_metric.py')
    a=p.parse_args();start=time.monotonic()
    paths=[Path(__file__),HERE/'exact_20261114_refined_tail_adapter.py',a.old_metric_source,
           a.checkpoint,a.port,a.complete,a.refined_background,a.plan,a.heights,a.base_metric]
    hashes={str(q):sha(q) for q in paths}
    pb=module('exact_interface_saved',HERE/'geometric-checkpoint-core-pullback.py')
    saved,_=pb.load_saved(a.checkpoint,a.source_topic,a.port,angular=1280)
    plan=json.loads(a.plan.read_text());height=json.loads(a.heights.read_text())
    tail=RefinedTail(a.complete);N=1024;theta=2*np.pi*np.arange(N)/N
    meanN=max(512,16*(3*saved.M+1));_,b1,b2=saved.flow.basis(meanN);s=np.array([saved.flow.end])
    frame,_,dw=saved.flow.velocity_s(s,saved.sol.sol(s),saved.sol.sol(s,1),b1,b2)
    cut_height=(0.,float(np.mean(frame['V'][0,:,2])),float(np.mean(dw[0,:,2])))
    A=RefinedAssembly(saved,tail,plan,height,cut_height)
    j,_,_=A.prefix_jets(s,theta,tuple(np.array([x]) for x in cut_height))
    t=A.tail_jets(np.array([A.cut]),theta)
    rs,rss=A.cut_radial_jets['r_s'],A.cut_radial_jets['r_ss']
    target=dict(pos=t['pos'],s1=rs*t['s1'],s2=rs*rs*t['s2']+rss*t['s1'],p1=t['p1'],p2=t['p2'],sp=rs*t['sp'])
    cut={k:float(np.max(np.linalg.norm(j[k]-target[k],axis=-1))) for k in target}
    cuff={k:float(np.max(np.linalg.norm(v,axis=-1))) for k,v in A.perturbation(np.array([A.cuff]),theta).items()}
    old=module('exact_interface_old_metric',a.old_metric_source)
    report,r,y,v,w=old.load_nodes(a.complete)
    y[:,:,2]+=np.array([row['meanPerturbationInnerAnchor'] for row in report['rows']],np.longdouble)[:,None]
    v[:,:,2]-=np.array([row['geometry']['w'] for row in report['rows']],np.longdouble)[:,None]
    w[:,:,2]-=np.array([row['geometry']['w']*row['geometry']['dlogwdx']/row['geometry']['drdx'] for row in report['rows']],np.longdouble)[:,None]
    r,y,v,w=r[::-1].copy(),y[::-1].copy(),v[::-1].copy(),w[::-1].copy()
    for i in range(1,len(r)-1):
        hm,hp=r[i]-r[i-1],r[i+1]-r[i]
        w[i,:,:2]=hp/(hm+hp)*(v[i,:,:2]-v[i-1,:,:2])/hm+hm/(hm+hp)*(v[i+1,:,:2]-v[i,:,:2])/hp
    w[0,:,:2]=(v[1,:,:2]-v[0,:,:2])/(r[1]-r[0])
    w[-1,:,:2]=(v[-1,:,:2]-v[-2,:,:2])/(r[-1]-r[-2])
    bg=json.loads(a.refined_background.read_text());base=json.loads(a.base_metric.read_text())
    witnesses=base['variants']['correct_background_quadrature']['witnesses']
    chosen=sorted(set([witnesses['metric']['stage'],witnesses['kappa']['stage'],43]))
    rows=[];ns=len(r)-1
    er=np.c_[np.cos(theta),np.sin(theta),np.zeros(N)]
    et=np.c_[-np.sin(theta),np.cos(theta),np.zeros(N)]
    for stage in chosen:
        i=ns-1-stage;h=r[i+1]-r[i]
        co=old.angular_jets(old.hermite(y[i],y[i+1],v[i],v[i+1],w[i],w[i+1],h),N)
        maximum={k:0. for k in ('s1','s2','p1','p2','sp')};metric=0.
        for point in bg['rows'][stage]['points']:
            radius=np.longdouble(point['r']);u=np.clip((radius-r[i])/h,0,1)
            reference=dict(s1=old.evaluate(co[0],u,h,1),s2=old.evaluate(co[0],u,h,2),
                p1=old.evaluate(co[1],u,h),p2=old.evaluate(co[2],u,h),sp=old.evaluate(co[1],u,h,1))
            # Unpatched new evaluator, to isolate the representation change.
            cc=tail.coefficients(radius)
            from exact_20261114_refined_tail_adapter import synth
            actual=dict(s1=synth(cc[1],theta),s2=synth(cc[2],theta),p1=synth(cc[0],theta,1),
                p2=synth(cc[0],theta,2),sp=synth(cc[1],theta,1))
            for key in maximum:
                maximum[key]=max(maximum[key],float(np.max(np.linalg.norm(actual[key]-reference[key],axis=-1))))
            patched=A.perturbation(np.array([float(radius)]),theta)
            fr=patched['s1'][0]+er;fr[:,2]+=point['w']
            ft=patched['p1'][0]+radius*et
            aa=(fr*fr).sum(1)/point['E']-1
            bb=(fr*ft).sum(1)/(np.sqrt(point['E'])*radius)
            dd=(ft*ft).sum(1)/radius**2-1
            value=(abs(aa+dd)+np.sqrt((aa-dd)**2+4*bb*bb))/2
            metric=max(metric,float(value.max()))
        rows.append(dict(stage=stage,radial_points=len(bg['rows'][stage]['points']),
                         new_vs_prior_unpatched_jet_maximum=maximum,patched_metric_maximum=metric))
    out=dict(schema='refined-tail-assembly-interface-readout-v1',finished=True,
        source_sha256_at_start=hashes,cut_mean_anchor=0.,absolute_prefix_mean_integrated=False,
        angular=N,mean_angular=meanN,cut_twojet_difference=cut,cuff_zero_twojet=cuff,
        endpoint_definition=A.cut_radial_jets,selected_stage_comparisons=rows,
        fixed_cut_width=A.W,background_queries=len(height['rows']),
        source_background_inverse_radius_residual=height['maximumInverseRadiusResidual'],
        loaded_tail_nodes=len(tail.verified_nodes),seconds=time.monotonic()-start,
        scope=__doc__,whole_closed_surface_evaluated=False)
    with a.out.open('x') as f:json.dump(out,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(output=str(a.out),cut=cut,cuff=cuff,stages=rows,seconds=out['seconds'])),flush=True)


if __name__=='__main__':main()
