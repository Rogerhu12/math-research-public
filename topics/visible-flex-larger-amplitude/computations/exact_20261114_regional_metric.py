#!/usr/bin/env python3
"""Regional metric samples of the unchanged patched field and its bare-tail diagnostic.

The finite field and source background are unchanged. This consumer evaluates
only its first jets in float64, using cancellation-free Gram differences; a
small prescribed set is compared with the original longdouble all-jet reader.
The original prefix is not solved again. No continuous supremum is certified.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import json
import math
import time
from pathlib import Path
import numpy as np
import exact_20261114_common_grid_refinement as core

HERE=Path(__file__).resolve().parent


def evaluate64(c,u,h,d):
    weights=np.zeros((len(u),6),float)
    for k in range(d,6):
        factor=math.prod(range(k-d+1,k+1)) if d else 1
        weights[:,k]=np.asarray(factor*u**(k-d)/h**d,float)
    return np.einsum('pk,knc->pnc',weights,c,optimize=True)


class FirstJetLayer(core.Layer):
    def first_jets(self,r):
        midpoint=(r[0]+r[-1])/2
        i=int(np.clip(np.searchsorted(self.tail.r,midpoint,side='right')-1,0,len(self.tail.r)-2))
        h=self.tail.r[i+1]-self.tail.r[i];u=(r-self.tail.r[i])/h
        if u.min() < -1e-6 or u.max()>1+1e-6:
            raise ValueError('Common grid crosses a represented cell')
        u=np.clip(u,0,1)
        if i!=self.cached_index:
            self.cached=core.angle_coefficients(self.tail.span(i),self.angles)
            self.cached_index=i
        bare=(evaluate64(self.cached[0],u,h,1),evaluate64(self.cached[1],u,h,0))
        patched=tuple(v.copy() for v in bare)
        mask=r>=np.longdouble(self.assembly.cut-self.assembly.W)
        if np.any(mask):
            t=np.clip((r[mask]-np.longdouble(self.assembly.cut-self.assembly.W))/self.W,0,1)
            patched[0][mask]+=evaluate64(self.patch[0],t,self.W,1)
            patched[1][mask]+=evaluate64(self.patch[1],t,self.W,0)
        return bare,patched,mask


def metric(first,r,points,er,et):
    vr,vt=first
    w=np.array([q['w']for q in points],float)
    Eg=np.array([q['E']for q in points],float)
    base=np.array([np.longdouble(1)+np.longdouble(q['w'])**2-np.longdouble(q['E'])for q in points],float)
    rr=np.asarray(r,float)
    delta_E=base[:,None]+2*(np.sum(vr*er[None,:,:],axis=-1)+w[:,None]*vr[:,:,2])+np.sum(vr*vr,axis=-1)
    delta_F=np.sum(vt*er[None,:,:],axis=-1)+w[:,None]*vt[:,:,2]+rr[:,None]*np.sum(vr*et[None,:,:],axis=-1)+np.sum(vr*vt,axis=-1)
    delta_G=2*rr[:,None]*np.sum(vt*et[None,:,:],axis=-1)+np.sum(vt*vt,axis=-1)
    a=delta_E/Eg[:,None];b=delta_F/(np.sqrt(Eg)[:,None]*rr[:,None]);d=delta_G/rr[:,None]**2
    return (abs(a+d)+np.hypot(a-d,2*b))/2


def update(record,values,mask,stage,points,theta):
    ids=np.flatnonzero(mask)
    if not len(ids):return
    record['radial_samples']+=len(ids)
    j,k=np.unravel_index(np.argmax(values[ids]),values[ids].shape);j=int(ids[j])
    v=float(values[j,k])
    if v>record.get('maximum',-1.):
        record.update(maximum=v,witness=dict(common_stage=stage,x=points[j]['x'],r=points[j]['r'],theta=float(theta[k])))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--complete',type=Path,action='append',required=True)
    p.add_argument('--labels',required=True)
    for key in ('background','source-topic','checkpoint','port','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--cut-width',type=float,default=.01)
    p.add_argument('--cuff',type=float,default=.3-.25)
    a=p.parse_args();start=time.monotonic();labels=a.labels.split(',')
    if len(labels)!=len(a.complete)or len(set(labels))!=len(labels):raise ValueError('Unique labels required')
    source_inputs={str(q):core.sha(q)for q in [Path(__file__),HERE/'exact_20261114_common_grid_refinement.py',HERE/'exact_20261114_refined_tail_adapter.py',a.background,a.checkpoint,a.port]+a.complete}
    pb=core.module('exact_regional_prefix',HERE/'geometric-checkpoint-core-pullback.py')
    saved,_=pb.load_saved(a.checkpoint,a.source_topic,a.port,angular=1280)
    meanN=max(512,16*(3*saved.M+1));_,b1,b2=saved.flow.basis(meanN);s=np.array([saved.flow.end])
    frame,_,dw=saved.flow.velocity_s(s,saved.sol.sol(s),saved.sol.sol(s,1),b1,b2)
    cut_height=(0.,float(np.mean(frame['V'][0,:,2])),float(np.mean(dw[0,:,2])))
    layers=[FirstJetLayer(path,label,saved,cut_height,a.angles,a.cut_width,a.cuff)for path,label in zip(a.complete,labels)]
    background=json.loads(a.background.read_text());fingerprint=background['original_profile_fingerprint']
    response=a.checkpoint.parent/Path(saved.rec['actual_tail']['final_response']).name
    for layer in layers:
        m=layer.tail.meta
        if m['original_profile_fingerprint']!=fingerprint or core.sha(response)not in m['input_sha256'].values():raise ValueError('Different source or original H binding')
        binding=m.get('refinement_binding')
        if binding:
            if not all(binding.get(k)is True for k in ('all_physical_parameters_equal','all_complete_H_equal','actual_newton_converged','DN_jacobian_present'))or binding['original_endpoint_nonmean_jets_reused']or not binding['residual']<binding['original_tolerance']:
                raise ValueError('Incomplete actual new shooting state')
    theta=2*np.pi*np.arange(a.angles)/a.angles
    er=np.c_[np.cos(theta),np.sin(theta),np.zeros(a.angles)];et=np.c_[-np.sin(theta),np.cos(theta),np.zeros(a.angles)]
    records={label:{k:dict(radial_samples=0)for k in ('actual_full_tail','actual_outer_patch_region','actual_outside_patch','bare_tail_diagnostic')}for label in labels}
    checks=[];check_stages=sorted(set([0,1,223,len(background['rows'])-1]))
    for stage,row in enumerate(background['rows']):
        points=row['points'];r=np.asarray([q['r']for q in points],np.longdouble)
        for layer in layers:
            bare,patched,mask=layer.first_jets(r);bm=metric(bare,r,points,er,et);pm=metric(patched,r,points,er,et)
            for key,values,subset in [('actual_full_tail',pm,np.ones(len(r),bool)),('actual_outer_patch_region',pm,mask),('actual_outside_patch',pm,~mask),('bare_tail_diagnostic',bm,np.ones(len(r),bool))]:
                update(records[layer.label][key],values,subset,stage,points,theta)
            if stage in check_stages:
                original=layer.jets(r);g=core.measured_geometry(original,r,points,theta)
                checks.append(dict(label=layer.label,stage=stage,radial_first_max_norm_difference=float(np.max(np.linalg.norm(patched[0]-original['radial_first'],axis=-1))),angular_first_max_norm_difference=float(np.max(np.linalg.norm(patched[1]-original['angular_first'],axis=-1))),metric_max_absolute_difference=float(np.max(abs(pm-g['metric'])))))
        if(stage+1)%768==0:
            print(json.dumps(dict(event='progress',stages=stage+1,total=len(background['rows']),seconds=time.monotonic()-start)),flush=True)
    result=dict(schema='fixed-g-regional-metric-sampling-v1',finished=True,source_sha256_at_start=source_inputs,original_profile_fingerprint=fingerprint,angles=a.angles,common_stages=len(background['rows']),fixed_cut_width=a.cut_width,mean_angular=meanN,regions=records,arithmetic_validation=checks,definition='Same finite Fourier/Hermite coefficients and fixed Cartesian cut patch. Bare tail is a diagnostic with that patch omitted; it is not a changed closed assembly.',accepted_prefix_resolved=False,seconds=time.monotonic()-start,limitations=['Finite spatial samples only; no interval supremum.','First-jet-only float64 consumer, with cancellation-free Gram differences and listed original-reader comparisons.','The unchanged original prefix cut has its own solver tolerance; this audit does not impose the tail Newton tolerance on that prefix.'])
    with a.out.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(event='complete',output=str(a.out),seconds=result['seconds'],regions=records)),flush=True)

if __name__=='__main__':main()
