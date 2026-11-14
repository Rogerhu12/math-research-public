#!/usr/bin/env python3
"""Compare actual same-g radial readouts on one complete common sample grid.

Uses the closed assembly's Fourier/Hermite field and direct-prefix cut patch.
The background is the same source function, so position and jet differences
cancel it analytically. A common prefix cut mean fixes all vertical gauges.
Reports finite all-domain samples, not interval bounds or new BVP solutions.
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
from exact_20261114_refined_tail_adapter import RefinedTail,RefinedAssembly,module,sha

HERE=Path(__file__).resolve().parent
JET_RULES={'position':(0,0),'radial_first':(1,0),'angular_first':(0,1),
           'radial_second':(2,0),'mixed':(1,1),'angular_second':(0,2)}


def angle_coefficients(c,N):
    k=np.arange(N//2+1)[None,:,None]
    g=np.zeros((6,N//2+1,3),complex)
    g[:,:c.shape[1]]=np.asarray(c,dtype=complex)
    g[:,1:c.shape[1]]/=2
    return [np.fft.irfft(g*(1j*k)**d,n=N,axis=1)*N for d in range(3)]


def evaluate(c,u,h,d):
    weights=np.zeros((len(u),6),np.longdouble)
    for k in range(d,6):
        fac=math.prod(range(k-d+1,k+1)) if d else 1
        weights[:,k]=fac*u**(k-d)/h**d
    return np.einsum('pk,knc->pnc',weights,c)


class Layer:
    def __init__(self,path,label,saved,cut_height,angles,width,cuff):
        self.path,self.label=path,label
        self.tail=RefinedTail(path)
        if angles<2*self.tail.N:
            raise ValueError('Use at least twice the source angular grid for Nyquist derivatives')
        plan=dict(cut=float(self.tail.r[-1]),tail_inner=float(self.tail.r[0]),cuff=cuff,
                  prefix_end=saved.flow.end,cut_correction_width=width)
        self.assembly=RefinedAssembly(saved,self.tail,plan,
            dict(rows=[dict(r=cuff,heightFromRToCut=0.)]),cut_height)
        self.angles,self.W=angles,np.longdouble(width)
        self.patch=angle_coefficients(self.assembly.patch,angles)
        self.cached_index=None;self.cached=None
        self.maxima={};self.witnesses={}

    def jets(self,r):
        midpoint=(r[0]+r[-1])/2
        i=int(np.clip(np.searchsorted(self.tail.r,midpoint,side='right')-1,0,len(self.tail.r)-2))
        h=self.tail.r[i+1]-self.tail.r[i]
        u=(r-self.tail.r[i])/h
        if u.min() < -1e-6 or u.max() > 1+1e-6:
            raise ValueError('Common sample span crosses a represented radial cell')
        u=np.clip(u,0,1)
        if i!=self.cached_index:
            self.cached=angle_coefficients(self.tail.span(i),self.angles)
            self.cached_index=i
        out={key:evaluate(self.cached[t],u,h,d) for key,(d,t) in JET_RULES.items()}
        # The actual closed map has one fixed prefix cut anchor. Do not shift
        # node heights before forming Hermite coefficients: thin spans would
        # then amplify needless subtraction roundoff in their second jets.
        out['position'][:,:,2]-=np.longdouble(self.assembly.tail_cut_mean)
        mask=r>=np.longdouble(self.assembly.cut-self.assembly.W)
        if np.any(mask):
            u=np.clip((r[mask]-np.longdouble(self.assembly.cut-self.assembly.W))/self.W,0,1)
            for key,(d,t) in JET_RULES.items():
                out[key][mask]+=evaluate(self.patch[t],u,self.W,d)
        return out


def measured_geometry(jets,r,points,theta):
    er=np.c_[np.cos(theta),np.sin(theta),np.zeros(len(theta))]
    et=np.c_[-np.sin(theta),np.cos(theta),np.zeros(len(theta))]
    w=np.asarray([q['w'] for q in points],np.longdouble)
    wr=np.asarray([q['wr'] for q in points],np.longdouble)
    Eg=np.asarray([q['E'] for q in points],np.longdouble)
    fr=jets['radial_first']+er[None,:,:];fr[:,:,2]+=w[:,None]
    ft=jets['angular_first']+r[:,None,None]*et[None,:,:]
    rr=jets['radial_second'].copy();rr[:,:,2]+=wr[:,None]
    rt=jets['mixed']+et[None,:,:]
    tt=jets['angular_second']-r[:,None,None]*er[None,:,:]
    E=np.sum(fr*fr,axis=-1);F=np.sum(fr*ft,axis=-1);G=np.sum(ft*ft,axis=-1)
    aa=E/Eg[:,None]-1;bb=F/(np.sqrt(Eg)[:,None]*r[:,None]);dd=G/r[:,None]**2-1
    metric=(abs(aa+dd)+np.sqrt((aa-dd)**2+4*bb*bb))/2
    normal=np.cross(fr,ft);normal/=np.linalg.norm(normal,axis=-1)[:,:,None]
    ee=np.sum(rr*normal,axis=-1);ff=np.sum(rt*normal,axis=-1);gg=np.sum(tt*normal,axis=-1)
    det=E*G-F*F;tr=(ee*G+gg*E-2*ff*F)/det;prod=(ee*gg-ff*ff)/det
    curvature=(abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*prod)))/2
    return dict(metric=metric,kappa=curvature)


def update(maxima,witnesses,key,values,stage,points,theta):
    at=np.unravel_index(np.argmax(values),values.shape);value=float(values[at])
    if key not in maxima or value>maxima[key]:
        maxima[key]=value
        j,k=at
        witnesses[key]=dict(common_stage=stage,x=points[j]['x'],r=points[j]['r'],theta=float(theta[k]))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--complete',type=Path,action='append',required=True)
    p.add_argument('--labels',required=True,help='Comma-separated labels in comparison order')
    for key in ('background','source-topic','checkpoint','port','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--cut-width',type=float,default=.01)
    p.add_argument('--cuff',type=float,default=.3-.25)
    a=p.parse_args();start=time.monotonic();labels=a.labels.split(',')
    if len(labels)!=len(a.complete) or len(labels)<2 or len(set(labels))!=len(labels):
        raise ValueError('At least two uniquely labelled actual readouts required')
    inputs=[Path(__file__),HERE/'exact_20261114_refined_tail_adapter.py',a.background,a.checkpoint,a.port]+a.complete
    source_inputs={str(q):sha(q) for q in inputs}
    pb=module('exact_common_saved_prefix',HERE/'geometric-checkpoint-core-pullback.py')
    saved,_=pb.load_saved(a.checkpoint,a.source_topic,a.port,angular=1280)
    meanN=max(512,16*(3*saved.M+1));_,b1,b2=saved.flow.basis(meanN);s=np.array([saved.flow.end])
    frame,_,dw=saved.flow.velocity_s(s,saved.sol.sol(s),saved.sol.sol(s,1),b1,b2)
    cut_height=(0.,float(np.mean(frame['V'][0,:,2])),float(np.mean(dw[0,:,2])))
    layers=[Layer(path,label,saved,cut_height,a.angles,a.cut_width,a.cuff) for path,label in zip(a.complete,labels)]
    fingerprint=layers[0].tail.meta['original_profile_fingerprint']
    if any(layer.tail.meta['original_profile_fingerprint']!=fingerprint or
           layer.tail.r[0]!=layers[0].tail.r[0] or layer.tail.r[-1]!=layers[0].tail.r[-1] for layer in layers):
        raise ValueError('Changing g or the represented interval is not a fixed-problem refinement')
    response=a.checkpoint.parent/Path(saved.rec['actual_tail']['final_response']).name
    if any(sha(response) not in layer.tail.meta['input_sha256'].values() for layer in layers):
        raise ValueError('Every readout must retain the same complete accepted H/tail response')
    background=json.loads(a.background.read_text())
    if background['original_profile_fingerprint']!=fingerprint:
        raise ValueError('Background differs')
    theta=2*np.pi*np.arange(a.angles)/a.angles
    comparisons=[dict(left=labels[i],right=labels[i+1],maxima={},witnesses={}) for i in range(len(labels)-1)]
    checkpoints=a.out.with_suffix('.checkpoint.json');samples=0
    for stage,row in enumerate(background['rows']):
        points=row['points'];r=np.asarray([x['r'] for x in points],np.longdouble)
        values=[layer.jets(r) for layer in layers]
        geometries=[]
        for layer,jets in zip(layers,values):
            g=measured_geometry(jets,r,points,theta);geometries.append(g)
            for key,x in g.items():update(layer.maxima,layer.witnesses,key,x,stage,points,theta)
        for i,record in enumerate(comparisons):
            for key in JET_RULES:
                difference=np.linalg.norm(values[i+1][key]-values[i][key],axis=-1)
                update(record['maxima'],record['witnesses'],key,difference,stage,points,theta)
            update(record['maxima'],record['witnesses'],'metric_scalar_difference',
                   abs(geometries[i+1]['metric']-geometries[i]['metric']),stage,points,theta)
            update(record['maxima'],record['witnesses'],'kappa_scalar_difference',
                   abs(geometries[i+1]['kappa']-geometries[i]['kappa']),stage,points,theta)
        samples+=len(points)
        if (stage+1)%192==0:
            data=dict(completed_common_stages=stage+1,total_common_stages=len(background['rows']),
                seconds=time.monotonic()-start,layers={v.label:v.maxima for v in layers},comparisons=comparisons)
            checkpoints.write_text(json.dumps(data,indent=2)+'\n')
            print(json.dumps(dict(event='progress',completed=stage+1,total=len(background['rows']),seconds=data['seconds'],metric={v.label:v.maxima['metric'] for v in layers})),flush=True)
    cap_shifts={v.label:v.assembly.tail_cut_mean for v in layers}
    result=dict(schema='same-g-actual-readout-common-grid-comparison-v1',finished=True,
        source_sha256_at_start=source_inputs,profile_fingerprint=fingerprint,
        same_accepted_actual_response_sha256=sha(response),angles=a.angles,
        radial_samples=samples,common_stages=len(background['rows']),fixed_cut_width=a.cut_width,
        layers={v.label:dict(nodes=len(v.tail.r),steps=v.tail.meta['steps'],maxima=v.maxima,witnesses=v.witnesses,
            small_mean_at_cut=v.assembly.tail_cut_mean,diagnostics=v.tail.meta['diagnostics']) for v in layers},
        adjacent_comparisons=comparisons,
        closed_cap_vertical_displacements=[dict(left=labels[i],right=labels[i+1],
            signed=cap_shifts[labels[i+1]]-cap_shifts[labels[i]]) for i in range(len(labels)-1)],
        common_gauge='The original prefix cut mean is shared. Small-mean cut constants are removed after evaluating each finite field; the unchanged background cancels in every position/jet difference.',
        all_other_prefix_and_fixed_cap_derivative_data_unchanged=True,
        mean_angular=meanN,seconds=time.monotonic()-start,
        limitations=['Complete represented-domain finite sampling, not an interval supremum certificate.',
            'Raw radial and angular derivatives are reported in the common r/theta coordinates.',
            'Each field includes the same-width outer patch; the inner collar difference is separately determined by terminal jets.',
            'Original accepted shooting endpoint data remain fixed; RK endpoint defects are reported and may limit refinement.',
            'Fourier/Hermite coefficients use the closed assembly definition; FFT evaluation of coefficient functions introduces ordinary floating error.'])
    with a.out.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(event='complete',output=str(a.out),seconds=result['seconds'],layers={v.label:v.maxima for v in layers},comparisons=[dict(left=x['left'],right=x['right'],maxima=x['maxima']) for x in comparisons])),flush=True)


if __name__=='__main__':main()
