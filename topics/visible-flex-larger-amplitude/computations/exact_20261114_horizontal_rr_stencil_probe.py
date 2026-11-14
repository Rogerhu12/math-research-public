#!/usr/bin/env python3
"""Probe actual finite fields with higher nonuniform radial-slope stencils.

The complete endpoint position/first/vertical-second data remain unchanged.
Only the shared horizontal rr used in the C2 Hermite representation changes.
The caller's background sample grid is retained exactly, as is the width-.01
complete prefix cut correction. Selected stages are explicitly reported.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
from functools import lru_cache
import json
from pathlib import Path
import time
import numpy as np
from exact_20261114_refined_tail_adapter import RefinedTail,fourier,module,sha
import exact_20261114_common_grid_refinement as core

HERE=Path(__file__).resolve().parent


class HigherTail(RefinedTail):
    stencil=5
    @lru_cache(maxsize=96)
    def node_coefficients(self,index):
        z=self.raw(index);g=self.rows[index]['geometry']
        y,v,w=z[:,:3].copy(),z[:,3:6].copy(),np.empty_like(z[:,:3])
        y[:,2]+=np.longdouble(self.rows[index]['meanPerturbationInnerAnchor'])
        v[:,2]-=np.longdouble(g['w'])
        w[:,2]=z[:,9]-np.longdouble(g['w'])*np.longdouble(g['dlogwdx'])/np.longdouble(g['drdx'])
        size=self.stencil
        first=max(0,min(len(self.r)-size,index-size//2));indices=np.arange(first,first+size)
        radii=self.r[indices];scale=max(abs(radii-self.r[index]));x=(radii-self.r[index])/scale
        center=index-first;products=np.ones(size,np.longdouble)
        for j in range(size):products[j]=np.prod([x[j]-x[k]for k in range(size)if k!=j],dtype=np.longdouble)
        out=np.zeros((self.N,2),np.longdouble)
        for j,at in enumerate(indices):
            if j!=center:
                weight=products[center]/(products[j]*(-x[j]))/scale
                out+=weight*(self.raw(int(at))[:,3:5]-z[:,3:5])
        w[:,:2]=out
        return tuple(fourier(a)for a in (y,v,w))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('complete','background','source-topic','checkpoint','port','out'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--stages',default='0:193,1600:1649')
    p.add_argument('--angles',type=int,default=1024)
    a=p.parse_args();start=time.monotonic()
    sources={str(x):sha(x)for x in [Path(__file__),HERE/'exact_20261114_refined_tail_adapter.py',HERE/'exact_20261114_common_grid_refinement.py']}
    background=json.loads(a.background.read_text());indices=[]
    for part in a.stages.split(','):
        if ':'in part:
            lo,hi=map(int,part.split(':'));indices.extend(range(lo,hi))
        else:indices.append(int(part))
    indices=sorted(set(indices))
    if any(i<0 or i>=len(background['rows'])for i in indices):raise ValueError('Stage outside actual background')
    pb=module('exact_stencil_prefix',HERE/'geometric-checkpoint-core-pullback.py')
    saved,_=pb.load_saved(a.checkpoint,a.source_topic,a.port,angular=1280)
    meanN=max(512,16*(3*saved.M+1));_,b1,b2=saved.flow.basis(meanN);s=np.array([saved.flow.end])
    frame,_,dw=saved.flow.velocity_s(s,saved.sol.sol(s),saved.sol.sol(s,1),b1,b2)
    cut=(0.,float(np.mean(frame['V'][0,:,2])),float(np.mean(dw[0,:,2])))
    layers=[]
    for stencil in (3,5,7):
        core.RefinedTail=RefinedTail if stencil==3 else type('HigherTail'+str(stencil),(HigherTail,),{'stencil':stencil})
        layers.append(core.Layer(a.complete,'shared-rr-'+str(stencil),saved,cut,a.angles,.01,.3-.25))
    core.RefinedTail=RefinedTail
    theta=2*np.pi*np.arange(a.angles)/a.angles
    for count,stage in enumerate(indices):
        points=background['rows'][stage]['points'];r=np.array([x['r']for x in points],np.longdouble)
        for layer in layers:
            g=core.measured_geometry(layer.jets(r),r,points,theta)
            for key,value in g.items():core.update(layer.maxima,layer.witnesses,key,value,stage,points,theta)
        if (count+1)%96==0:print(json.dumps(dict(event='progress',completed=count+1,total=len(indices))),flush=True)
    result=dict(schema='same-node-higher-horizontal-rr-stencil-probe-v1',finished=True,
        source_sha256_at_start=sources,inputs={str(x):sha(x)for x in [a.complete,a.background,a.checkpoint,a.port]},
        stages=indices,all_stages_included=len(indices)==len(background['rows']),angles=a.angles,
        layers={x.label:dict(maxima=x.maxima,witnesses=x.witnesses)for x in layers},
        fixed_cut_width=.01,source_background_unchanged=True,endpoint_position_first_vertical_second_jets_unchanged=True,
        derivative_definition='Degree4/6 nonuniform Lagrange derivative of horizontal radial-first samples, evaluated by scaled barycentric weights on five/seven nearest-index nodes. Subtract the central sample before summing to annihilate constants.',
        baseline_definition='Existing three-point interior difference and two-point endpoint difference.',
        limitations=['Finite selected-domain probe, not a complete-domain result unless all_stages_included is true.',
            'Higher stencil changes shared horizontal rr and the associated finite Hermite field; no uncomputed true rr or derivative error certificate is asserted.',
            'The original shooting states supplied by the input readout are retained.'],seconds=time.monotonic()-start)
    with a.out.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(event='complete',output=str(a.out),seconds=result['seconds'],layers=result['layers'])),flush=True)


if __name__=='__main__':main()
