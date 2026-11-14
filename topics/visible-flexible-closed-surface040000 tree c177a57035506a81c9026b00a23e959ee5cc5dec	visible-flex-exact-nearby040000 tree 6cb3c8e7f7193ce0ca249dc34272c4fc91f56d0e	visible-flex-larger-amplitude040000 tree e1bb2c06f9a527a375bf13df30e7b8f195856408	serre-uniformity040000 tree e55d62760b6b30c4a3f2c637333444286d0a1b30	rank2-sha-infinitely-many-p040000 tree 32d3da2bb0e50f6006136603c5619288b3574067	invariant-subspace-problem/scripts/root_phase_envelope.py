#!/usr/bin/env python3
"""Sample the centred diameter envelope of a frozen ellipse prefix.

This is geometry screening only. It does not supply the missing compact tail,
certify continuous extrema, or assert an exact isometry. Dependencies and the
checkpoint are hashed in the output. The exact centre-symmetry lemma is in the
companion note, and does not depend on this numerical screening.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root',type=Path,required=True)
    ap.add_argument('--ellipse-notes',type=Path,required=True)
    ap.add_argument('--checkpoint',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--angular',type=int,default=512)
    ap.add_argument('--subdivisions',type=int,default=2)
    args=ap.parse_args()
    sys.path.insert(0,str(args.ellipse_notes))
    sys.path.insert(0,str(args.source_root/'topics/large-amplitude-twist-flex/scripts'))
    from repo_scan_ellipse_bvp import EllipseBVP
    from repo_scan_gentle import scaled_port
    from f6curve_outward_bridge_linear import read_port
    from curve_stable_prefix_bvp import load_checkpoint
    old=load_checkpoint(args.checkpoint)
    cfg=old['frozen_profile'];M=old['config']['modes']
    source=read_port(args.source_root/'topics/large-amplitude-twist-flex/notes/f6curve_wide_m2_r2_m16_linear_port.json')
    port=scaled_port(source,cfg['cut_radius'],cfg.get('cut_slope'),cfg.get('dimensionless_D'))
    obj=EllipseBVP(cfg,port,old['config']['aspect'],M,old['config']['angular'])
    p=np.asarray(old['parameters']).copy();p[0]=0.
    flow=obj.flow(0.);obj.initial(p);core=obj._core
    mesh=np.asarray(old['mesh'])
    pp=PPoly.construct_fast(np.asarray(old['pp_coefficients']),mesh,extrapolate=True,axis=1)
    sol=SimpleNamespace(x=mesh,y=pp(mesh),p=p,sol=pp)
    s=np.unique(np.r_[mesh,*[(1-u)*mesh[:-1]+u*mesh[1:]
        for u in np.linspace(0,1,args.subdivisions+1)[1:-1]]])
    heights=flow.height_integral(sol,s,args.angular,8)
    B=flow.basis(args.angular)[0]
    th=2*np.pi*np.arange(args.angular)/args.angular
    g=core.evaluate(th)['F'];R=float(core.major_radius)
    r=float(np.max(np.abs(g[:,1])));anisotropy=R-r
    halfwidths=[0.,max(0.,anisotropy),.26,.3,.4]
    rows=[{'ell':ell,'centred_diameter_sample':0.,'cylinder_diameter_sample':0.,
           'radius_max':0.,'height_max':0.,'where':None} for ell in halfwidths]
    min_height=float('inf');symmetry_error=0.
    for j in range(0,len(s),64):
        ss=s[j:j+64];C=flow.base(ss)+obj.q*pp(ss)
        x=flow.values(C,B);x[:,:,2]+=heights[j:j+len(ss),None]
        min_height=min(min_height,float(np.min(x[:,:,2])))
        # The Fourier basis has the prescribed half-turn symmetry.
        x2=np.roll(x,args.angular//2,axis=1)
        symmetry_error=max(symmetry_error,float(np.max(np.abs(x2[:,:,:2]+x[:,:,:2]))),
                           float(np.max(np.abs(x2[:,:,2]-x[:,:,2]))))
        rr=np.sum(x[:,:,:2]**2,axis=2)
        for row in rows:
            zz=x[:,:,2]+row['ell'];norm2=rr+zz*zz
            k=np.unravel_index(int(np.argmax(norm2)),norm2.shape)
            d=2*float(np.sqrt(norm2[k]))
            if d>row['centred_diameter_sample']:
                row['centred_diameter_sample']=d
                row['where']={'s':float(ss[k[0]]),'theta':float(th[k[1]]),
                              'rho':float(np.sqrt(rr[k])),'z':float(zz[k])}
            row['radius_max']=max(row['radius_max'],float(np.sqrt(rr.max())))
            row['height_max']=max(row['height_max'],float(np.abs(zz).max()))
    for row in rows:
        row['cylinder_diameter_sample']=2*float(np.hypot(row['radius_max'],row['height_max']))
        row['conditional_delta_hold']=min(max(0.,anisotropy),row['ell'])
        row['conditional_ratio_before_tail']=row['conditional_delta_hold']/row['centred_diameter_sample']
        d_allowed=20*row['conditional_delta_hold']
        # Additional cap/tail assumed contained in rho<=cut_radius, |z|<=H.
        row['diameter_limit_for_5percent']=d_allowed
        row['allowed_height_if_tail_radius_cut']=float(np.sqrt(max(0.,(d_allowed/2)**2-cfg['cut_radius']**2)))
        row['additional_height_budget_sample']=row['allowed_height_if_tail_radius_cut']-row['height_max']
    dependencies={}
    for mod in list(sys.modules.values()):
        name=getattr(mod,'__file__',None)
        if name and (str(args.source_root) in name or str(args.ellipse_notes) in name):
            fp=Path(name)
            if fp.is_file():dependencies[str(fp)]=hashlib.sha256(fp.read_bytes()).hexdigest()
    out={'scope':__doc__,'checkpoint':str(args.checkpoint),
         'checkpoint_sha256':hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
         'sampling':{'s':len(s),'theta':args.angular},'config':cfg,'aspect':obj.aspect,
         'central_R':R,'sampled_support_y':r,'sampled_anisotropy':anisotropy,
         'sampled_prefix_min_z':min_height,'half_turn_numerical_error':symmetry_error,
         'rows':rows,'dependencies_sha256':dependencies}
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['aspect','sampled_anisotropy','sampled_prefix_min_z','half_turn_numerical_error','rows']}))


if __name__=='__main__':
    main()
