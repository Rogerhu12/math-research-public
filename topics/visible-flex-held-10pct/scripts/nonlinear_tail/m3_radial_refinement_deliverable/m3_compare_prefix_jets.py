#!/usr/bin/env python3
"""Compare actual saved C2 prefix maps at the same physical material points.

This is a finite sampled refinement diagnostic, not a convergence theorem.
Both maps include the nonlinear mean height and its differentiated values.
No ODE second jet replaces a saved second derivative, and no fit of rigid
motion or reparametrization is performed. Regenerable arrays stay in memory.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly

p=argparse.ArgumentParser(description=__doc__)
for key in ('source-topic','short-bridge','coarse','fine','port','output'):
    p.add_argument('--'+key,type=Path,required=True)
p.add_argument('--angular',type=int,default=512)
a=p.parse_args()
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out
ad=module('m3_compare_adaptive',a.source_topic/'scripts/950f-prefix-adaptive-chart-bvp-v2.py')
module('m3_compare_flat',a.source_topic/'scripts/db6f-prefix-flat-profile.py').install(ad)
ad.old.install_source(a.source_topic/'repro/source-root')
module('m3_compare_short',a.short_bridge).install()
from curve_stable_prefix_bvp import load_checkpoint
records=[load_checkpoint(path)for path in (a.coarse,a.fine)]
checks=['frozen_profile','physical_tail_parameters','physical_tail_cut','chart',
        'warp_reference_q','angular_chart','gauge_amplitude']
for key in checks:
    if records[0][key]!=records[1][key]:raise ValueError('Different physical input: '+key)
for r in records:
    if not r['solver_success'] or not r['config']['fixed_metric'] or r['config']['base_mode']!=3:
        raise ValueError('Accepted fixed-metric m3 maps are required')
port=json.loads(a.port.read_text());port['cut']['_prefix_bridge']=records[0]['frozen_profile']['prefix_bridge']
if port['parameters']!=records[0]['physical_tail_parameters'] or port['cut']!=records[0]['physical_tail_cut']:
    raise ValueError('Physical port differs from the saved pair')
_,BVP=ad.build_classes(records[0]['chart'])
N=max(a.angular,16*(3*max(r['config']['modes']for r in records)+1))
data=[]
for r in records:
    obj=BVP(r['frozen_profile'],port,r['gauge_amplitude'],r['config']['modes'],
            r['config']['angular'],True,r['warp_reference_q'])
    par=np.array(r['parameters']);par[0]=math.log(r['actual_primary_amplitude']/obj.q)
    obj.initial(par);flow=obj.flow(par[0]);mesh=np.array(r['mesh'])
    pp=PPoly.construct_fast(np.array(r['pp_coefficients']),mesh,extrapolate=True,axis=1)
    sol=SimpleNamespace(x=mesh,y=pp(mesh),p=par,sol=pp)
    data.append(dict(record=r,obj=obj,flow=flow,mesh=mesh,pp=pp,sol=sol,basis=flow.basis(N)))
if abs(data[0]['flow'].end-data[1]['flow'].end)>3e-13:
    raise ValueError('Different physical endpoint')
mesh0,mesh1=data[0]['mesh'],data[1]['mesh']
samples=np.unique(np.r_[mesh0,mesh1,(mesh0[:-1]+mesh0[1:])/2,
                        (mesh1[:-1]+mesh1[1:])/2,np.linspace(0,data[0]['flow'].end,151)])
for d in data:d['height']=d['flow'].height_integral(d['sol'],samples,N,6)

def jets(d,s,height):
    obj,flow,pp=d['obj'],d['flow'],d['pp'];B,B1,B2=d['basis']
    Y,Yp,Ypp=pp(s),pp(s,1),pp(s,2)
    fr,Fsp,dW=flow.velocity_s(s,Y,Yp,B1,B2);g=fr['geo'];rho=g['rho'];v=g['v']
    X=g['pos']+obj.q*flow.values(Y,B);X[:,:,2]+=height[:,None]
    Fsc=g['s1']+obj.q*flow.values(Yp,B);Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
    Fssc=g['s2']+obj.q*flow.values(Ypp,B);Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
    Fs=Fsc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None]
    Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
    Fst=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None]
    Fss=Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']
    return dict(X=X,Xs=Fs,Xu=Ft,Xss=Fss,Xsu=Fst,Xuu=Ftt)

out={key:dict(sup_euclidean=0.)for key in ['X','Xs','Xu','Xss','Xsu','Xuu']}
for first in range(0,len(samples),24):
    sl=slice(first,first+24);s=samples[sl]
    values=[jets(d,s,d['height'][sl])for d in data]
    for key in out:
        norm=np.linalg.norm(values[0][key]-values[1][key],axis=2);index=np.unravel_index(np.argmax(norm),norm.shape)
        maximum=float(norm[index])
        if maximum>out[key]['sup_euclidean']:
            out[key].update(sup_euclidean=maximum,s=float(s[index[0]]),
                            numerical_angle=float(2*np.pi*index[1]/N))
idx=np.searchsorted(mesh1,mesh0)
distance=np.minimum(np.abs(mesh0-mesh1[np.clip(idx,0,len(mesh1)-1)]),
                    np.abs(mesh0-mesh1[np.clip(idx-1,0,len(mesh1)-1)]))
sha=lambda path:hashlib.sha256(Path(path).read_bytes()).hexdigest()
result=dict(scope=__doc__,source_sha256=sha(__file__),coarse_sha256=sha(a.coarse),fine_sha256=sha(a.fine),
            fixed_inputs_checked=checks,coarse_nodes=len(mesh0),fine_nodes=len(mesh1),
            coarse_q=records[0]['actual_primary_amplitude'],fine_q=records[1]['actual_primary_amplitude'],
            coarse_node_distance_to_fine_max=float(distance.max()),
            angular=N,radial_samples=len(samples),differences=out)
a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
