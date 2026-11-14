#!/usr/bin/env python3
"""Fast actual-prefix geometry screen using rotated core witnesses.

Queries the exact planar core against a dense cloud of the reconstructed C2
prefix plus an optional R71 ruled continuation. The largest core candidate is
not the full surface Hausdorff distance. Nearest-point and radius polishing
are local numerical searches, not certified continuum bounds. All surfaces
here have boundary and lack the inward leg, fixed caps, and holding region.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.optimize import minimize
from scipy.spatial import cKDTree
import importlib.util
import sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent


def load(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m)
    return m


geo=load('geometric_screen_geometry',HERE/'geometric-alternative-geometry.py')
control=load('geometric_screen_control',HERE/'alternative-controlled-profile.py')
# Runtime adapter only; no source file is modified.
geo.make_probe=lambda cfg,angular:control.make_probe(cfg,N=angular)


class Prefix:
    def __init__(self,path,angular=1024,radial=201):
        self.path=path;self.data=control.read_json(path);self.cfg=self.data['config']
        if self.data['rows'][0]['s']!=0:
            raise ValueError('Need full history from the core, not a continuation-only history')
        if 'coefficient_states'not in self.data:raise ValueError('Stored full states are required')
        self.pp,self.entryD,self.entryQ=geo.interpolant(self.data)
        self.M=self.cfg['M'];self.freq=2*np.arange(self.M+1)
        self.probe=control.make_probe(self.cfg,N=angular)
        self.end=float(self.data['reached_s'])
        self.s=np.unique(np.r_[np.linspace(0,self.end,radial),self.pp.x])
        self.angular=angular;self.phi=self.probe.phi
        self.up=np.array([geo.world(self.probe.jet(y)[0],self.phi)for y in self.pp(self.s)])
        self.entry=np.asarray(self.data['final_coefficients'])
        self.a0,self.speed,self.acc=self.probe.profile(self.end)
        self.A=1+self.cfg['A']-self.cfg['A']/(10*math.sqrt(2))
        self.B=1-self.cfg['A']-self.cfg['A']/(10*math.sqrt(2))

    def jet(self,y,phi):
        c=np.cos(self.freq*phi);s=np.sin(self.freq*phi)
        r=y[:self.M+1];t=y[self.M+1:2*self.M+1];z=y[2*self.M+1:]
        R=r@c;T=t@s[1:];Z=z@c
        Rp=(-self.freq*r)@s;Tp=(self.freq[1:]*t)@c[1:];Zp=(-self.freq*z)@s
        Rpp=(-self.freq**2*r)@c;Tpp=(-self.freq[1:]**2*t)@s[1:];Zpp=(-self.freq**2*z)@c
        cp=math.cos(phi);sp=math.sin(phi)
        def world(v):return np.array([cp*v[0]-sp*v[1],sp*v[0]+cp*v[1],v[2]])
        return (world([R,T,Z]),world([Rp-T,Tp+R,Zp]),
                world([Rpp-2*Tp-R,Tpp+2*Rp-T,Zpp]))

    def point(self,s,phi,part):
        if part=='prefix':return self.jet(self.pp(s),phi)[0]
        if abs(self.acc)>2e-11 or self.speed<=0:raise ValueError('Invalid ruled entry')
        gamma,gp,gpp=self.jet(self.entry,phi)
        d0,dp,_=self.jet(self.entryD,phi)
        rho=1-3*self.cfg['A']*math.cos(2*phi)+15*self.cfg['A']/(10*math.sqrt(2))*math.cos(4*phi)
        T0=gp/(self.a0*rho);normal=np.cross(d0,T0);normal/=np.linalg.norm(normal)
        b0=self.a0*rho*(dp@normal)/(gpp@normal)
        root=math.sqrt(1+b0*b0);t0=self.a0/root;k=self.a0*b0/root
        e=(d0-b0*T0)/root
        aa=self.a0+self.speed*(s-self.end)
        ell=(math.sqrt(aa*aa-k*k)-t0)/self.speed
        return gamma+ell*e

    def cloud(self,width,flat_radial):
        points=self.up.reshape(-1,3)
        ps=np.repeat(self.s,self.angular);phi=np.tile(self.phi,len(self.s))
        parts={'prefix':dict(points=points,s=ps,phi=phi)}
        flat_info=None
        if width:
            flat,fs,flat_info=geo.ruled_cloud(self.probe,self.entry,self.entryD,self.end,width,flat_radial)
            parts['ruled']=dict(points=flat.reshape(-1,3),s=np.repeat(fs,self.angular),
                                phi=np.tile(self.phi,len(fs)))
        for part in parts.values():part['tree']=cKDTree(part['points'])
        all_points=np.concatenate([x['points']for x in parts.values()])
        return parts,all_points,flat_info

    def nearest_polished(self,p,parts,width,seeds=2):
        best=None
        for name,part in parts.items():
            ds,idx=part['tree'].query(p,k=seeds)
            lo,hi=(0,self.end)if name=='prefix'else(self.end,self.end+width)
            for d,i in zip(np.atleast_1d(ds),np.atleast_1d(idx)):
                s0=part['s'][i];phi0=part['phi'][i]
                def objective(u):
                    q=self.point(u[0],u[1],name);v=q-p
                    return float(v@v)
                bounds=[(lo,hi),(phi0-.15,phi0+.15)]
                fit=minimize(objective,[s0,phi0],bounds=bounds,method='L-BFGS-B',
                             options=dict(ftol=1e-15,gtol=1e-11,maxiter=120))
                if fit.fun>d*d:
                    ss,ph=float(s0),float(phi0);value=float(d*d)
                else:ss,ph=map(float,fit.x);value=float(fit.fun)
                record=dict(distance=math.sqrt(max(0,value)),point=self.point(ss,ph,name).tolist(),
                            s=ss,phi=ph%(2*math.pi),part=name,optimizer_success=bool(fit.success))
                if best is None or record['distance']<best['distance']:best=record
        return best

    def radius_polished(self,parts,width):
        best=None
        for name,part in parts.items():
            norms2=np.sum(part['points']**2,axis=1)
            seeds=np.argsort(norms2)[-8:]
            lo,hi=(0,self.end)if name=='prefix'else(self.end,self.end+width)
            for i in seeds:
                s0=part['s'][i];phi0=part['phi'][i]
                def objective(u):
                    q=self.point(u[0],u[1],name);return -float(q@q)
                fit=minimize(objective,[s0,phi0],bounds=[(lo,hi),(phi0-.15,phi0+.15)],
                             method='L-BFGS-B',options=dict(ftol=1e-15,gtol=1e-11,maxiter=120))
                if -fit.fun<norms2[i]:ss,ph=float(s0),float(phi0);value=float(norms2[i])
                else:ss,ph=map(float,fit.x);value=float(-fit.fun)
                record=dict(radius=math.sqrt(value),s=ss,phi=ph%(2*math.pi),part=name,
                            point=self.point(ss,ph,name).tolist(),optimizer_success=bool(fit.success))
                if best is None or record['radius']>best['radius']:best=record
        return best

    def screen(self,width,phases=33,core_angles=512,flat_radial=41,polish=20):
        begin=time.time();parts,points,flat_info=self.cloud(width,flat_radial)
        tree=cKDTree(points);D=2*float(np.linalg.norm(points,axis=1).max())
        cp=2*np.pi*np.arange(core_angles)/core_angles
        e=self.cfg['A'];cc=e/(10*math.sqrt(2))
        h=1+e*np.cos(2*cp)-cc*np.cos(4*cp)
        hp=-2*e*np.sin(2*cp)+4*cc*np.sin(4*cp)
        core=np.stack((h*np.cos(cp)-hp*np.sin(cp),h*np.sin(cp)+hp*np.cos(cp),np.zeros_like(cp)),axis=1)
        rows=[];candidates=[]
        for alpha in np.linspace(0,np.pi/2,phases):
            c=math.cos(alpha);s=math.sin(alpha)
            rot=core.copy();rot[:,0]=c*core[:,0]-s*core[:,1];rot[:,1]=s*core[:,0]+c*core[:,1]
            dist,near=tree.query(rot,workers=1)
            for i in np.argsort(dist)[-max(2,polish//phases+1):]:
                candidates.append(dict(alpha=float(alpha),phi=float(cp[i]),cloud_distance=float(dist[i]),
                                       point=rot[i].tolist()))
            i=int(np.argmax(dist));rows.append(dict(alpha=float(alpha),core_angle=float(cp[i]),
                rotated_core_to_initial_cloud_max=float(dist[i]),ratio_to_sampled_D=float(dist[i]/D),
                point=rot[i].tolist(),nearest_cloud_point=points[near[i]].tolist()))
        candidates.sort(key=lambda x:x['cloud_distance'],reverse=True)
        polished=[]
        for candidate in candidates[:polish]:
            refined=self.nearest_polished(np.array(candidate['point']),parts,width)
            polished.append(dict(**candidate,nearest=refined,polished_distance=refined['distance']))
        radius=self.radius_polished(parts,width);Dpol=2*radius['radius']
        winner=max(polished,key=lambda x:x['polished_distance'])if polished else None
        p=np.array([0,self.A,0]);core_near=self.nearest_polished(p,parts,width)
        gap=self.A-self.B
        exact_ball_margin=float(np.min(np.sum((points-p)**2,axis=1)-gap**2))
        return dict(width=width,flat_metadata=flat_info,
            samples=dict(radial_prefix=len(self.s),angular=self.angular,core_angles=core_angles,
                         phases=phases,flat_radial=flat_radial if width else 0,upper_points=len(points)),
            D_reflected_prefix_sample=D,D_reflected_prefix_locally_polished=Dpol,
            radius_maximizer=radius,phase_rows=rows,
            maximum_core_cloud_candidate=max(r['rotated_core_to_initial_cloud_max']for r in rows),
            maximum_core_cloud_candidate_over_D=max(r['ratio_to_sampled_D']for r in rows),
            polished_core_witness_candidates=polished,polished_core_winner=winner,
            polished_core_winner_over_D=winner['polished_distance']/Dpol if winner else None,
            principal_core_witness=dict(point=p.tolist(),core_gap=gap,nearest=core_near,
                ratio_to_polished_D=core_near['distance']/Dpol),
            sampled_exact_ball_margin_min=exact_ball_margin,seconds=time.time()-begin)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angular',type=int,default=1024);p.add_argument('--radial',type=int,default=201)
    p.add_argument('--core-angles',type=int,default=512);p.add_argument('--phases',type=int,default=33)
    p.add_argument('--widths',type=float,nargs='+',default=[0,.05,.1]);p.add_argument('--flat-radial',type=int,default=41)
    p.add_argument('--polish',type=int,default=20);args=p.parse_args()
    start=time.time();q=Prefix(args.input,args.angular,args.radial)
    result=dict(scope=__doc__,input_file=str(args.input),input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),config=q.cfg,
        endpoint=q.end,input_metric_sample=q.data.get('whole_sample_max_metric'),
        input_kappa_sample=q.data.get('whole_sample_max_kappa'),rows=[],
        caveats=['This is a subset witness screen, not full-surface Hausdorff maximization.',
                 'Target-cloud distances overestimate exact nearest distances; local polishing is not a proof of global minimality.',
                 'Continuous diameter uses central symmetry, but its radius maximum is only sampled and locally optimized.',
                 'All prefixes have boundary; no reach or closed-family claim is made.'])
    for width in args.widths:
        row=q.screen(width,args.phases,args.core_angles,args.flat_radial,args.polish);result['rows'].append(row)
        print(json.dumps(dict(input=str(args.input),width=width,D=row['D_reflected_prefix_locally_polished'],
            core_winner=row['polished_core_winner']['polished_distance'],ratio=row['polished_core_winner_over_D'],
            principal_distance=row['principal_core_witness']['nearest']['distance'],seconds=row['seconds'])),flush=True)
        result['seconds']=time.time()-start;args.out.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
