#!/usr/bin/env python3
"""Actual strong-core prefix phase geometry, with optional ruled extension.

Samples the C2 quintic interpolant determined by saved ODE nodes and their
actual finite-ODE first/second jets. Results are geometric screening values,
not closed-surface, exact-continuum Hausdorff, or reach certificates.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
from scipy.interpolate import PPoly
from scipy.spatial import cKDTree
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj;spec.loader.exec_module(obj)
    return obj


def make_probe(cfg,angular):
    if cfg.get('radial_law')=='fast_outward':
        fast=module('geometric_alternative_fast',HERE/'alternative-fast-profile.py')
        return fast.probe_class()(cfg['A'],cfg['M'],angular,cfg['v'],cfg['S'],cfg['power'])
    if cfg.get('radial_law') not in (None,'outward'):
        raise ValueError('Unknown physical radial law: '+str(cfg.get('radial_law')))
    source=module('geometric_alternative_probe',HERE/'alternative-outward-probe.py')
    return source.Probe(cfg['A'],cfg['M'],angular,cfg['v'],cfg['S'],cfg['amax'],
                        cfg.get('coast_at'),cfg.get('coast_length',.1))


def world(points,phi):
    c=np.cos(phi);s=np.sin(phi)
    return np.stack((c*points[...,0]-s*points[...,1],s*points[...,0]+c*points[...,1],points[...,2]),axis=-1)


def finite_ode_jets(probe,s,y):
    fr=probe.frame(s,y);yp=probe.project(fr['V'])
    h=1e-25
    jy=probe.project(probe.frame(s,y.astype(complex)+1j*h*yp,strict=False)['V']).imag/h
    da=-fr['app']/(fr['a']*fr['kap'])+fr['ap']**2/(fr['a']**2*fr['kap'])
    db=-fr['al']*da/fr['be']
    ypp=jy+probe.project(da[:,None]*fr['N']+db[:,None]*fr['B'])
    return yp,ypp


def interpolant(data):
    cfg=data['config'];probe=make_probe(cfg,cfg['N'])
    s=np.array([r['s']for r in data['rows']]);Y=np.asarray(data['coefficient_states'])
    if len(s)!=len(Y):raise ValueError('Saved state and radial-node counts differ')
    D=[];Q=[]
    for ss,y in zip(s,Y):
        d,q=finite_ode_jets(probe,float(ss),y);D.append(d);Q.append(q)
    D=np.asarray(D);Q=np.asarray(Q)
    h=np.diff(s)[:,None]
    e0=Y[1:]-Y[:-1]-h*D[:-1]-h*h*Q[:-1]/2
    e1=D[1:]-D[:-1]-h*Q[:-1];e2=Q[1:]-Q[:-1]
    u=10*e0-4*h*e1+h*h*e2/2
    v=-15*e0+7*h*e1-h*h*e2
    w=6*e0-3*h*e1+h*h*e2/2
    coeff=np.stack((w/h**5,v/h**4,u/h**3,Q[:-1]/2,D[:-1],Y[:-1]))
    return PPoly.construct_fast(coeff,s,extrapolate=False,axis=0),D[-1],Q[-1]


def ruled_cloud(probe,entry,entry_derivative,entry_s,width,radial):
    a0,c,acc=probe.profile(entry_s)
    if abs(acc)>2e-11:raise ValueError('Cannot append ruled extension at nonzero a second derivative')
    if c<=0:raise ValueError('This ruled entry adapter expects positive radial speed')
    fr=probe.frame(entry_s,entry);V,Vp,Vpp=probe.jet(entry_derivative)
    gamma=world(fr['F'],probe.phi);gp=world(fr['d'],probe.phi);gpp=world(fr['dd'],probe.phi)
    d0=world(V,probe.phi);dp=world(Vp,probe.phi)
    T0=gp/(a0*probe.rho0[:,None]);normal=np.cross(d0,T0);normal/=np.linalg.norm(normal,axis=1)[:,None]
    Cden=np.sum(gpp*normal,axis=1)
    if np.min(abs(Cden))<1e-9:raise FloatingPointError('Ruled entry normal curvature denominator too small')
    b0=a0*probe.rho0*np.sum(dp*normal,axis=1)/Cden
    root=np.sqrt(1+b0*b0);t0=a0/root;k=a0*b0/root
    e=(d0-b0[:,None]*T0)/root[:,None]
    points=[]
    radial_s=np.linspace(0,width,radial)
    for ss in radial_s:
        a=a0+c*ss
        if np.min(a*a-k*k)<=0:raise FloatingPointError('Ruled square root left its real domain')
        ell=(np.sqrt(a*a-k*k)-t0)/c
        points.append(gamma+ell[:,None]*e)
    return np.asarray(points),radial_s+entry_s,dict(entry_a=a0,entry_speed=c,
          entry_b_max=float(abs(b0).max()),entry_ez_min=float(e[:,2].min()))


def phase_geometry(path,angular=512,radial=181,phases=9,width=0.,flat_radial=61):
    begin=time.time();data=json.loads(path.read_text());cfg=data['config']
    if 'coefficient_states'not in data:raise ValueError('Full stored coefficient states are required')
    pp,entryD,entryQ=interpolant(data);probe=make_probe(cfg,angular)
    s=np.unique(np.r_[np.linspace(0,data['reached_s'],radial),pp.x])
    states=pp(s);up=np.array([world(probe.jet(y)[0],probe.phi)for y in states])
    source_labels=np.zeros(len(s),dtype=int);flat_metadata=None
    if width:
        extra,es,flat_metadata=ruled_cloud(probe,np.asarray(data['final_coefficients']),entryD,
                                         data['reached_s'],width,flat_radial)
        up=np.concatenate((up,extra[1:]));s=np.r_[s,es[1:]]
        source_labels=np.r_[source_labels,np.ones(len(es)-1,dtype=int)]
    down=up.copy();down[:,:,2]*=-1
    points=np.concatenate((up.reshape(-1,3),down.reshape(-1,3)))
    # m=2 symmetry + z reflection make the continuous doubled prefix central.
    norms=np.linalg.norm(points,axis=1);D=2*float(norms.max())
    tree=cKDTree(points)
    def locate(index):
        half=len(up)*angular;local=int(index)%half;j=local//angular;k=local%angular
        return dict(s=float(s[j]),phi=float(probe.phi[k]),half='upper'if index<half else'lower',
                    part='ruled'if source_labels[j]else'prefix')
    A=1+cfg['A']-cfg['A']/(10*math.sqrt(2))
    B=1-cfg['A']-cfg['A']/(10*math.sqrt(2))
    witnesses={}
    for key,point in [('outward_rotated_core',[0.,A,0.]),('inward_rotated_core',[B,0.,0.])]:
        dist,index=tree.query(point)
        witnesses[key]=dict(point=point,distance_to_initial_cloud=float(dist),nearest=points[index].tolist(),nearest_parameter=locate(index))
    rows=[]
    for alpha in np.linspace(0,np.pi/2,phases):
        c,si=math.cos(alpha),math.sin(alpha)
        rot=points.copy();rot[:,0]=c*points[:,0]-si*points[:,1];rot[:,1]=si*points[:,0]+c*points[:,1]
        distances,nearest=tree.query(rot,workers=1)
        other=cKDTree(rot);back,backnear=other.query(points,workers=1)
        if distances.max()>=back.max():
            i=int(np.argmax(distances));gap=float(distances[i]);p=rot[i];q=points[nearest[i]]
            which='rotated_to_initial';near_location=locate(nearest[i])
        else:
            i=int(np.argmax(back));gap=float(back[i]);p=points[i];q=rot[backnear[i]]
            which='initial_to_rotated';near_location=locate(backnear[i])
        rows.append(dict(alpha=float(alpha),point_cloud_Hausdorff=gap,ratio_to_sampled_prefix_D=gap/D,
                         direction=which,witness=p.tolist(),witness_parameter=locate(i),nearest=q.tolist(),nearest_parameter=near_location))
    d=A-B
    mask=abs(points[:,2])<=d
    surplus=points[mask,1]-B-points[mask,2]**2/(2*d)
    masked_indices=np.flatnonzero(mask);i=int(masked_indices[int(np.argmax(surplus))])
    summary=dict(scope=__doc__,input_file=str(path),input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),config=cfg,input_status=data['status'],
        prefix_endpoint=data['reached_s'],append_ruled_width=width,flat_metadata=flat_metadata,
        samples=dict(radial=len(s),angular=angular,phases=phases),
        D_reflected_prefix_sample=D,diameter_max_norm_location=locate(int(np.argmax(norms))),
        core_gap=d,core_witnesses=witnesses,phase_rows=rows,
        max_sampled_Hausdorff=max(r['point_cloud_Hausdorff']for r in rows),
        max_sampled_Hausdorff_over_D=max(r['ratio_to_sampled_prefix_D']for r in rows),
        sufficient_parabola_violation_max=float(np.max(surplus)),
        sufficient_parabola_worst_point=points[i].tolist(),sufficient_parabola_worst_parameter=locate(i),
        input_metric_sample=data.get('whole_sample_max_metric',max(r['metric_sample']for r in data['rows'])),
        input_kappa_sample=data.get('whole_sample_max_kappa',max(r['surface_kappa_sample']for r in data['rows'])),
        curvature_radius_over_prefix_D_from_input_samples=1/(D*max(r['surface_kappa_sample']for r in data['rows'])),
        caveats=['With boundary; both fixed caps and inward closing leg absent.',
                 'Hausdorff and diameter are finite samples of a reconstructed C2 interpolant, not certified continuum bounds.',
                 'A sampled curvature ratio does not certify reach or embedding.',
                 'Interpolant between saved ODE nodes is not a newly solved trajectory.'],seconds=time.time()-begin)
    return summary


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angular',type=int,default=512);p.add_argument('--radial',type=int,default=181)
    p.add_argument('--phases',type=int,default=9);p.add_argument('--width',type=float,default=0.)
    p.add_argument('--flat-radial',type=int,default=61)
    a=p.parse_args();report=phase_geometry(a.input,a.angular,a.radial,a.phases,a.width,a.flat_radial)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k]for k in ('input_file','input_status','prefix_endpoint','append_ruled_width',
         'D_reflected_prefix_sample','max_sampled_Hausdorff','max_sampled_Hausdorff_over_D',
         'core_witnesses','sufficient_parabola_violation_max','seconds')}),flush=True)


if __name__=='__main__':main()
