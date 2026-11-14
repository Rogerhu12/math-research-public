#!/usr/bin/env python3
"""Local experiment: original source-knot retention versus horizontal rr rule.

Compares the actual same-RK24 node data on a requested common-grid window.
The Gauss-Weingarten target-metric rule defines an alternative finite field;
it is not automatically equal to the exact ODE Cartesian second derivative.
No wider-domain improvement or adoption is implied by this local experiment.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from functools import lru_cache
import json
from pathlib import Path
import time
import numpy as np
import exact_20261114_common_grid_refinement as core
from exact_20261114_refined_tail_adapter import RefinedTail,RefinedAssembly,fourier

HERE=Path(__file__).resolve().parent


class TargetMetricTail(RefinedTail):
    def __init__(self,path):
        super().__init__(path)
        self.diag=dict(minimum_normal_z=float('inf'),maximum_cardinal_saved_angular_difference=0.,maximum_radial_metric_derivative_residual=0.)

    @lru_cache(maxsize=64)
    def node_coefficients(self,index):
        z=self.raw(index);g=self.rows[index]['geometry'];r=self.r[index]
        y=z[:,:3].copy();y[:,2]+=np.longdouble(self.rows[index]['meanPerturbationInnerAnchor'])
        v=z[:,3:6].copy();w=np.empty_like(y)
        ww=np.longdouble(g['w']);wr=ww*np.longdouble(g['dlogwdx'])/np.longdouble(g['drdx'])
        theta=2*np.pi*np.arange(self.N)/self.N;k=np.arange(self.N//2+1)[:,None]
        er=np.c_[np.cos(theta),np.sin(theta),np.zeros(self.N)];et=np.c_[-np.sin(theta),np.cos(theta),np.zeros(self.N)]
        fr=z[:,3:6]+er
        ft=np.asarray(np.fft.irfft(np.fft.rfft(np.asarray(y,float),axis=0)*(1j*k),n=self.N,axis=0),np.longdouble)+r*et
        pointft=z[:,6:9]+r*et
        cross=np.cross(fr,ft);nz=cross[:,2]/np.linalg.norm(cross,axis=1)
        if nz.min()<=0:raise ValueError('Positive normal z required')
        gamma=ww*wr/np.longdouble(g['E']);normal_height=z[:,9]-gamma*fr[:,2]
        w[:,:2]=gamma*fr[:,:2]+normal_height[:,None]*cross[:,:2]/cross[:,2,None]
        w[:,2]=z[:,9]
        self.diag['minimum_normal_z']=min(self.diag['minimum_normal_z'],float(nz.min()))
        self.diag['maximum_cardinal_saved_angular_difference']=max(self.diag['maximum_cardinal_saved_angular_difference'],float(np.max(np.linalg.norm(ft-pointft,axis=1))))
        self.diag['maximum_radial_metric_derivative_residual']=max(self.diag['maximum_radial_metric_derivative_residual'],float(np.max(abs(2*np.sum(fr*w,axis=1)-2*ww*wr))))
        v[:,2]-=ww;w[:,2]-=wr
        return tuple(fourier(t)for t in (y,v,w))


class TargetLayer(core.Layer):
    def __init__(self,path,label,saved,cut_height,angles,width,cuff):
        self.path,self.label=path,label;self.tail=TargetMetricTail(path)
        if angles<2*self.tail.N:raise ValueError('Resolve all cardinal angular derivatives')
        plan=dict(cut=float(self.tail.r[-1]),tail_inner=float(self.tail.r[0]),cuff=cuff,prefix_end=saved.flow.end,cut_correction_width=width)
        self.assembly=RefinedAssembly(saved,self.tail,plan,dict(rows=[dict(r=cuff,heightFromRToCut=0.)]),cut_height)
        self.angles,self.W=angles,np.longdouble(width)
        self.patch=core.angle_coefficients(self.assembly.patch,angles)
        self.cached_index=None;self.cached=None;self.maxima={};self.witnesses={}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('regular-complete','cusp-complete','background','source-topic','checkpoint','port','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--first-common-stage',type=int,required=True);p.add_argument('--last-common-stage',type=int,required=True)
    p.add_argument('--angles',type=int,default=1024)
    a=p.parse_args();started=time.monotonic()
    sources={str(q):core.sha(q)for q in [Path(__file__),HERE/'exact_20261114_refined_tail_adapter.py',HERE/'exact_20261114_common_grid_refinement.py',a.regular_complete,a.cusp_complete,a.background,a.checkpoint,a.port]}
    pb=core.module('exact_source_knot_rr_saved',HERE/'geometric-checkpoint-core-pullback.py')
    saved,_=pb.load_saved(a.checkpoint,a.source_topic,a.port,angular=1280)
    meanN=max(512,16*(3*saved.M+1));_,b1,b2=saved.flow.basis(meanN);s=np.array([saved.flow.end])
    frame,_,dw=saved.flow.velocity_s(s,saved.sol.sol(s),saved.sol.sol(s,1),b1,b2)
    cut_height=(0.,float(np.mean(frame['V'][0,:,2])),float(np.mean(dw[0,:,2])))
    layers=[]
    for path,label in [(a.regular_complete,'regular'),(a.cusp_complete,'source-knot')]:
        layers.append(core.Layer(path,label+'-difference-rr',saved,cut_height,a.angles,.01,.3-.25))
        layers.append(TargetLayer(path,label+'-target-metric-rr',saved,cut_height,a.angles,.01,.3-.25))
    bg=json.loads(a.background.read_text());theta=2*np.pi*np.arange(a.angles)/a.angles
    if any(q.tail.meta['original_profile_fingerprint']!=bg['original_profile_fingerprint']for q in layers):raise ValueError('Changed source background')
    if any(q.tail.meta.get('refinement_binding')!=layers[0].tail.meta.get('refinement_binding')for q in layers):raise ValueError('Different shooting response binding')
    stages=range(a.first_common_stage,a.last_common_stage+1)
    for si in stages:
        points=bg['rows'][si]['points'];r=np.asarray([q['r']for q in points],np.longdouble)
        for layer in layers:
            values=core.measured_geometry(layer.jets(r),r,points,theta)
            for key,value in values.items():core.update(layer.maxima,layer.witnesses,key,value,si,points,theta)
    result=dict(finished=True,scope=__doc__,source_sha256_at_start=sources,common_stages=list(stages),angles=a.angles,cut_width=.01,mean_angular=meanN,layers={q.label:dict(maxima=q.maxima,witnesses=q.witnesses,target_rule_diagnostics=getattr(q.tail,'diag',None))for q in layers},seconds=time.monotonic()-started,limitations=['This is only the stated finite common-grid window, not a full-tail maximum.','Target-metric completion is a different finite interpolation rule; it has not been adopted in the closed assembly.'])
    with a.out.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(event='complete',out=str(a.out),seconds=result['seconds'],layers={q.label:q.maxima for q in layers})),flush=True)

if __name__=='__main__':main()
