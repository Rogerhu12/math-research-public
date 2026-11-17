#!/usr/bin/env python3
"""Independent actual geometry readout for the direct-height AcceptedBase API.

All atomic background/state/spline cells are integrated. The returned height
and its actual derivatives define the geometry; optimizer Gram/curvature and
PDE residuals are never substituted. The nonsingular unscaled R631 formulas
also evaluate the flat w=0 endpoint. All extrema remain sampled evidence.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time

import numpy as np


HERE=Path(__file__).parent


def import_file(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out)
    return out


radial=import_file(HERE/'2026-11-17-parallel-geometry-radial-tail-readout.py','literal_radial_tools')


def coefficients(data,rho):
    r,w,wr=(data[k][:,None] for k in ('r','w','wr'))
    hr,hrr,hp,hrp=(data[k] for k in ('hr','hrr','h_phi','hr_phi'))
    p=hp/(r*rho);pr=hrp/(r*rho)-p/r
    E=1+w*w;Er=2*w*wr;S=1-p*p;Sr=-2*p*pr
    D=E*S-hr*hr;Dr=Er*S+E*Sr-2*hr*hrr
    if np.min(S)<=0 or np.min(D)<=0:
        raise FloatingPointError('Actual height exits S,D>0; no branch clamping is permitted')
    a=np.sqrt(D/S);ar=a*(Dr/D-Sr/S)/2
    b=-hr*p/np.sqrt(S)
    br=-(hrr*p+hr*pr)/np.sqrt(S)+hr*p*Sr/(2*S**1.5)
    connection=hr*(hrp/rho-p)/(r*S*np.sqrt(D))
    return dict(a=a,ar=ar,b=b,br=br,connection=connection,S=S,D=D,
                q=r*rho*np.sqrt(S))


def geometry(alpha,xy,data,co,rho,correction):
    t=np.stack((np.cos(alpha),np.sin(alpha)),axis=2)
    n=np.stack((np.sin(alpha),-np.cos(alpha)),axis=2)
    a,b,ar,br,A=(co[k] for k in ('a','b','ar','br','connection'))
    v=b[:,:,None]*t+a[:,:,None]*n+correction['first']
    vr=(br+a*A)[:,:,None]*t+(ar-b*A)[:,:,None]*n+correction['second']
    xy=xy+correction['value']
    xp=radial.angular_derivative(xy);xpp=radial.angular_derivative(xy,2)
    vp=radial.angular_derivative(v)
    F=np.concatenate((xy,data['h'][:,:,None]),axis=2)
    Fr=np.concatenate((v,data['hr'][:,:,None]),axis=2)
    Frr=np.concatenate((vr,data['hrr'][:,:,None]),axis=2)
    Fp=np.concatenate((xp,data['h_phi'][:,:,None]),axis=2)
    Fpp=np.concatenate((xpp,data['h_phiphi'][:,:,None]),axis=2)
    Frp=np.concatenate((vp,data['hr_phi'][:,:,None]),axis=2)
    E=np.sum(Fr*Fr,axis=2);G=np.sum(Fp*Fp,axis=2);C=np.sum(Fr*Fp,axis=2)
    Eg=1+data['w'][:,None]**2;Gg=(data['r'][:,None]*rho)**2
    er=E/Eg-1;gr=G/Gg-1;fr=C/np.sqrt(Eg*Gg)
    op=(abs(er+gr)+np.sqrt((er-gr)**2+4*fr*fr))/2
    cross=np.cross(Fr,Fp);det=np.sum(cross*cross,axis=2)
    normal=cross/np.sqrt(det)[:,:,None]
    ee,ff,gg=(np.sum(jet*normal,axis=2) for jet in (Frr,Frp,Fpp))
    tr=(ee*G+gg*E-2*ff*C)/det;kd=(ee*gg-ff*ff)/det
    curvature=(abs(tr)+np.sqrt(np.maximum(0.,tr*tr-4*kd)))/2
    return dict(F=F,Fr=Fr,Frr=Frr,Fphi=Fp,op=op,er=er,gr=gr,fr=fr,
                curvature=curvature,det=det,angular_error=xp-co['q'][:,:,None]*t)


def run(args):
    started=time.perf_counter();raw=args.input.read_bytes();saved=json.loads(raw)
    files=[args.height_source,
           HERE/'2026-11-17-parallel-model-direct-height-autodiff.py',
           HERE/'2026-11-17-parallel-model-direct-height-gram.py',
           HERE/'2026-11-17-parallel-geometry-height-mode-api.py',
           HERE/'2026-11-17-parallel-geometry-flat-cuff.py',
           HERE/'2026-11-17-parallel-model-angular-reconstruct.py',
           HERE/'2026-11-17-parallel-geometry-stable-height-reader.py',
           HERE/'2026-11-17-parallel-geometry-tail-readout.py',
           HERE/'2026-11-17-parallel-geometry-radial-tail-readout.py']
    initial_bytes={p:p.read_bytes() for p in files}
    module=import_file(args.height_source,'actual_direct_height')
    params=saved['parameters'].copy()
    for key in ('trace','background','out','input','accepted_state','template'):
        if params.get(key) is not None:params[key]=Path(params[key])
    params['angles']=args.angles
    q=module.AcceptedBase(argparse.Namespace(**params));x=np.asarray(saved['coefficients'])
    if len(x)!=q.n:raise ValueError('Saved coefficients do not fit the loaded actual API')
    for p,b in initial_bytes.items():
        if p.read_bytes()!=b:raise RuntimeError('A height dependency changed during import/construction')
    source_manifest={p.name:hashlib.sha256(b).hexdigest() for p,b in initial_bytes.items()}
    edges=np.asarray(q.atomic_radii());edges=edges[(edges>=q.r0)&(edges<=q.r1)]
    if edges[0]!=q.r0 or edges[-1]!=q.r1 or np.any(np.diff(edges)<=0):
        raise ValueError('Atomic domain is incomplete or unordered')
    rho=q.rho[None,:];phi=q.phi
    alpha=q.alpha0.copy();xy=q.xy0.copy();ac=np.zeros_like(alpha);xc=np.zeros_like(xy)
    nodes,weights,matrix=radial.integration_matrix(args.radial_gauss)
    fractions=np.r_[0.,nodes,1.];nf=len(fractions)
    maxs={k:0. for k in ('gram_operator','rr','rphi','phiphi','principal_curvature',
                        'reference_curvature','angular_compatibility','join_F','join_Fr','join_Frr')}
    mins={k:float('inf') for k in ('S','D','gram_determinant','witness_distance')}
    worst={};worst_curvature={};count=0;previous=None;length=0.;length_c=0.
    maxnorm=0.;initial=None;deep=None;last=None
    witness=np.array([0.,args.witness_major,0.])
    for batch in range(0,len(edges)-1,args.batch_cells):
        chosen=np.arange(batch,min(batch+args.batch_cells,len(edges)-1))
        lo=edges[chosen];width=np.diff(edges)[chosen]
        rr=(lo[:,None]+width[:,None]*fractions).ravel()
        # Avoid a final ulp outside the declared closed interval.
        rr=np.minimum(np.maximum(rr,q.r0),q.r1)
        all_data=q.evaluate_height(rr,x,mean_gauss=args.mean_gauss)
        all_co=coefficients(all_data,rho)
        all_correction=q.cartesian_join_correction(rr)
        for j,cell in enumerate(chosen):
            sl=slice(j*nf,(j+1)*nf);d={k:v[sl] for k,v in all_data.items()}
            co={k:v[sl] for k,v in all_co.items()};cor={k:v[sl] for k,v in all_correction.items()}
            width=float(edges[cell+1]-edges[cell]);A=co['connection'][1:-1]
            an=alpha+width*(matrix@A)
            ae,ac=radial.compensated_add(alpha,ac,width*(weights@A))
            t=np.stack((np.cos(an),np.sin(an)),axis=2)
            n=np.stack((np.sin(an),-np.cos(an)),axis=2)
            v=co['b'][1:-1,:,None]*t+co['a'][1:-1,:,None]*n
            xn=xy+width*np.einsum('ij,jkl->ikl',matrix,v)
            xe,xc=radial.compensated_add(xy,xc,width*np.einsum('j,jkl->kl',weights,v))
            aall=np.vstack((alpha,an,ae));xall=np.concatenate((xy[None],xn,xe[None]))
            g=geometry(aall,xall,d,co,rho,cor)
            val=float(g['op'].max())
            if val>maxs['gram_operator']:
                i,k=np.unravel_index(np.argmax(g['op']),g['op'].shape)
                worst=dict(cell=int(cell),r=float(d['r'][i]),phi=float(phi[k]),value=val,
                    rr=float(g['er'][i,k]),rphi=float(g['fr'][i,k]),phiphi=float(g['gr'][i,k]))
                maxs['gram_operator']=val
            for label,key in (('rr','er'),('rphi','fr'),('phiphi','gr')):
                maxs[label]=max(maxs[label],float(abs(g[key]).max()))
            kr=abs(d['wr'])/(1+d['w']**2)**1.5
            maxs['reference_curvature']=max(maxs['reference_curvature'],float(kr.max()))
            val=float(g['curvature'].max())
            if val>maxs['principal_curvature']:
                i,k=np.unravel_index(np.argmax(g['curvature']),g['curvature'].shape)
                worst_curvature=dict(cell=int(cell),r=float(d['r'][i]),phi=float(phi[k]),
                    value=val,reference_curvature=float(kr[i]),w=float(d['w'][i]),wr=float(d['wr'][i]),
                    height_rr=float(d['hrr'][i,k]),S=float(co['S'][i,k]),D=float(co['D'][i,k]))
                maxs['principal_curvature']=val
            maxs['angular_compatibility']=max(maxs['angular_compatibility'],float(np.linalg.norm(g['angular_error'],axis=2).max()))
            for key in ('S','D'):mins[key]=min(mins[key],float(co[key].min()))
            mins['gram_determinant']=min(mins['gram_determinant'],float(g['det'].min()))
            mins['witness_distance']=min(mins['witness_distance'],float(np.linalg.norm(g['F']-witness,axis=2).min()))
            maxnorm=max(maxnorm,float(np.linalg.norm(g['F'],axis=2).max()))
            if previous is not None:
                for k,label in enumerate(('F','Fr','Frr')):
                    maxs['join_'+label]=max(maxs['join_'+label],float(np.linalg.norm(g[label][0]-previous[k],axis=1).max()))
            previous=[g[k][-1].copy() for k in ('F','Fr','Frr')]
            length,length_c=radial.compensated_add(length,length_c,width*float(weights@np.sqrt(1+d['w'][1:-1]**2)))
            if initial is None:initial=g['F'][0].copy()
            if edges[cell+1]==q.deep_r:
                deep=dict(r=q.deep_r,position=g['F'][-1].copy(),reference_length_prefix=float(length))
            last=dict(F=g['F'][-1].copy(),Fr=g['Fr'][-1].copy(),Frr=g['Frr'][-1].copy(),
                      alpha=ae.copy(),height=d['h'][-1].copy(),hr=d['hr'][-1].copy(),hrr=d['hrr'][-1].copy())
            alpha,xy=ae,xe;count+=nf*q.N
        if args.progress and batch%args.progress<args.batch_cells:
            print(json.dumps(dict(event='actual-reader-progress',cells=int(chosen[-1]+1),
                total_cells=len(edges)-1,gram=maxs['gram_operator'],curvature=maxs['principal_curvature'])),flush=True)
    endpoint_circle=last['F'][:,:2]-q.r1*np.column_stack((np.sin(alpha),-np.cos(alpha)))
    initial_radial=np.abs(q.r1-np.linalg.norm(initial[:,:2],axis=1))
    endpoint=dict(reference_length=float(length),height_mean=float(last['height'].mean()),
        height_spread=float(np.ptp(last['height'])),maximum_abs_hr=float(abs(last['hr']).max()),
        maximum_abs_hrr=float(abs(last['hrr']).max()),
        maximum_circle_displacement=float(np.linalg.norm(endpoint_circle,axis=1).max()),
        initial_minimum_planar_radius=float(np.linalg.norm(initial[:,:2],axis=1).min()),
        sampled_initial_to_round_cuff_radial_necessary_epsilon=float(max(0.,np.max((initial_radial/length)**2-1))))
    if deep is not None:
        L=length-deep['reference_length_prefix'];gap=np.abs(q.r1-np.linalg.norm(deep['position'][:,:2],axis=1))
        endpoint['deep_to_cuff']=dict(length=float(L),maximum_radial_need=float(gap.max()),
            necessary_epsilon=float(max(0.,np.max((gap/L)**2-1))))
    out=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        candidate_sha256=hashlib.sha256(raw).hexdigest(),source_manifest=source_manifest,
        saved_source_sha256=saved.get('source_sha256'),same_height_coefficients=True,
        homotopy=q.homotopy,angles=q.N,radial_gauss=args.radial_gauss,mean_gauss=args.mean_gauss,
        atomic_cells=len(edges)-1,sampled_points=count,maxima=maxs,minima=mins,
        maximum_origin_norm=maxnorm,worst_metric=worst,worst_curvature=worst_curvature,
        endpoint=endpoint,seconds=time.perf_counter()-started,
        prefix_alignment_certified=False,closed_surface=False,reach_certificate=False,
        rule='No branch flooring, no substitution of optimizer diagnostics, and no certification of continuous extrema')
    text=json.dumps(out,indent=2)+'\n';args.out.write_text(text);print(text,end='')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--height-source',type=Path,default=HERE/'2026-11-17-parallel-model-direct-height-accepted-base.py')
    p.add_argument('--angles',type=int,default=512);p.add_argument('--radial-gauss',type=int,default=8)
    p.add_argument('--mean-gauss',type=int,default=12);p.add_argument('--batch-cells',type=int,default=8)
    p.add_argument('--progress',type=int,default=512)
    p.add_argument('--witness-major',type=float,default=1.4141197181548968)
    run(p.parse_args())
