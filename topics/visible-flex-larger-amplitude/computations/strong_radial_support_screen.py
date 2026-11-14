#!/usr/bin/env python3
"""Sample F dot n on the saved physical prefix, including its mean height.

Use actual derivatives of the saved physical quintic, not the pointwise PDE
velocity in place of F_s.  The height mean is the same segmentwise Gauss
antiderivative used by the saved-surface tools.  Only its independent radial
batch size is reduced.  n = F_theta cross F_s is oriented outward at the
equator.  This is a finite, open-prefix numerical screen, not a global
closed-surface reach or radial-graph certificate.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import textwrap
import time
import types
import numpy as np

HERE=Path(__file__).resolve().parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('checkpoint','source-topic','port','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--radial',type=int,default=161)
    parser.add_argument('--angular',type=int,default=128)
    parser.add_argument('--height-angular',type=int,default=512)
    parser.add_argument('--batch',type=int,default=8)
    args=parser.parse_args();start=time.monotonic()
    if min(args.radial,args.angular,args.height_angular,args.batch)<=0 or args.batch>128:
        raise ValueError('Positive sample counts and a bounded radial batch are required')
    hashes={str(Path(__file__)):hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        str(args.checkpoint):hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()}
    pullback=load('strong_radial_support_pullback',HERE/'geometric-checkpoint-core-pullback.py')
    saved,unused=pullback.load_saved(args.checkpoint,args.source_topic,args.port,
        angular=max(args.angular,args.height_angular))
    if not saved.rec.get('solver_success') or saved.rec.get('audit_pending',True):
        raise ValueError('An audited converged saved finite prefix is required')
    flow=saved.flow;pp=saved.sol.sol
    original=textwrap.dedent(inspect.getsource(flow.height_integral.__func__))
    if original.count('128')!=3:
        raise ValueError('The source height-integral batch sites changed')
    transformed=original.replace('128',str(args.batch))
    scope={'np':np};exec(compile(transformed,'<bounded-original-height-integral>','exec'),scope)
    bounded_height=types.MethodType(scope['height_integral'],flow)
    s=np.unique(np.r_[np.linspace(0,flow.end,args.radial),flow.breaks,flow.end])
    heights=bounded_height(saved.sol,s,args.height_angular,6)
    B,B1,B2=flow.basis(args.angular)
    unused_B,H1,H2=flow.basis(args.height_angular)
    segment_rows=[]
    def label(seg,inside_loop,bridge):
        if bridge:return 'terminal-'+seg['kind']
        if seg['kind']=='hermite':return 'initial-hermite'
        if seg['kind']=='boost':return 'boost'
        return ('loop-' if inside_loop else 'descending-')+seg['kind']
    prefix=flow._alternative_neck
    for j,seg in enumerate(prefix.segments):
        segment_rows.append(dict(index=j,label=label(seg,seg['s0']>=prefix.loop_begin-1e-13,False),
            s_left=seg['s0'],s_right=seg['s1'],minimum=None,negative_samples=0,samples=0))
    for j,seg in enumerate(flow.bridge.segments):
        segment_rows.append(dict(index=len(prefix.segments)+j,label=label(seg,False,True),
            s_left=prefix.end+seg['s0'],s_right=prefix.end+seg['s1'],minimum=None,negative_samples=0,samples=0))
    minimum=None;maximum=-np.inf;normal_area_min=np.inf;negative=0;total=0
    equator_min=None;core_outward_dot_min=None
    for first in range(0,len(s),args.batch):
        sl=slice(first,first+args.batch);ss=s[sl];Y=pp(ss);Yp=pp(ss,1)
        frame=flow.frame(ss,saved.q*Y,B1,B2);geo=frame['geo']
        hp=np.mean(flow.frame(ss,saved.q*Y,H1,H2)['V'][:,:,2],axis=1)
        point=geo['pos']+saved.q*flow.values(Y,B);point[:,:,2]+=heights[sl,None]
        Fs_chart=geo['s1']+saved.q*flow.values(Yp,B);Fs_chart[:,:,2]+=hp[:,None]
        Fs=Fs_chart-geo['v'][:,:,None]*frame['d']
        Ft=frame['d']/geo['rho'][:,:,None]
        cross=np.cross(Ft,Fs);area=np.linalg.norm(cross,axis=2)
        if np.min(area)<=0:raise FloatingPointError('A sampled tangent area vanished')
        normals=cross/area[:,:,None];support=np.sum(point*normals,axis=2)
        normal_area_min=min(normal_area_min,float(np.min(area)))
        maximum=max(maximum,float(np.max(support)))
        negative+=int(np.count_nonzero(support<0));total+=support.size
        for row,sv in enumerate(ss):
            segment=next((r for r in segment_rows if r['s_left']-1e-12<=sv<=r['s_right']+1e-12),segment_rows[-1])
            j=int(np.argmin(support[row]));value=float(support[row,j])
            witness=dict(value=value,s=float(sv),psi=float(2*np.pi*j/args.angular),
                material_theta=float(geo['theta'][row,j]),point=point[row,j].tolist(),
                outward_normal=normals[row,j].tolist(),Fs=Fs[row,j].tolist(),Ftheta=Ft[row,j].tolist(),
                height_mean=float(heights[first+row]),height_mean_derivative=float(hp[row]),
                segment=segment['label'],segment_index=segment['index'],
                physical_quintic_interval=int(np.clip(np.searchsorted(saved.sol.x,sv,side='right')-1,0,len(saved.sol.x)-2)))
            if minimum is None or value<minimum['value']:minimum=witness
            if segment['minimum'] is None or value<segment['minimum']['value']:segment['minimum']=witness
            segment['samples']+=args.angular;segment['negative_samples']+=int(np.count_nonzero(support[row]<0))
            if sv==0:
                equator_min=value
                radial=point[row].copy();radial[:,2]=0.;radial/=np.linalg.norm(radial,axis=1)[:,None]
                core_outward_dot_min=float(np.min(np.sum(normals[row]*radial,axis=1)))
    result=dict(scope=__doc__,checkpoint=str(args.checkpoint),source_sha256=hashes,
        actual_primary_amplitude=saved.rec['actual_primary_amplitude'],gauge_amplitude=saved.q,
        modes=saved.M,saved_metric_l1=saved.rec['summary']['metric_l1'],
        radial_samples=len(s),angular_samples=args.angular,height_angular=args.height_angular,
        mean_quadrature_order=6,batch=args.batch,samples=total,negative_samples=negative,
        minimum=minimum,maximum=float(maximum),sampled_positive_support=minimum['value']>0,
        normal_area_min=float(normal_area_min),equator_minimum=equator_min,
        equator_normal_radial_dot_min=core_outward_dot_min,segment_minima=segment_rows,
        height_integral_batch_transform=dict(original_function_sha256=hashlib.sha256(original.encode()).hexdigest(),
            transformed_function_sha256=hashlib.sha256(transformed.encode()).hexdigest(),old_batch=128,new_batch=args.batch,
            replacements=3,original_quadrature_and_integration_order_preserved=True),
        normal_formula='Ftheta cross Fs normalized; Fs uses saved PPoly derivative plus the full integrated height mean derivative.',
        mirror_note='Reflecting both F and the outward normal across z=0 preserves F dot n. No caps or missing tail are included.',
        limitations=['This is a sampled open finite prefix; neither embedding nor continuous support/reach is certified.',
            'Negative samples disqualify the positive-radial-support hypothesis for this saved approximation about this center.',
            'The source physical metric can fail its requested accuracy despite finite Galerkin convergence.'],
        seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('actual_primary_amplitude','gauge_amplitude','minimum',
        'negative_samples','samples','equator_normal_radial_dot_min','seconds')}),flush=True)


if __name__=='__main__':main()
