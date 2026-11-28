#!/usr/bin/env python3
"""Complete R774 material fold and all four end poses, independent spatial and phase prices."""
import argparse
import json
import os
from pathlib import Path
import numpy as np
import r774_two_oblique_folds_on_true_flat_panel as fold

G=fold.core;m=G.m
def grid(na,nv,t,order):
    a=np.linspace(-fold.WIDTH/2,fold.WIDTH/2,na);v=np.linspace(0,fold.T,nv)
    ph=.90*fold.smooth((t-1/3)/(2/3));lam=G.state(order,ph)[2] if ph else 0.
    b1,q,b2,c1,c2=fold.pose(lam)
    w=fold.smooth((t-1/6)*6);w2=(1-w)*fold.L+w*fold.W2;center=(1-w)*(fold.E+fold.L/2)+w*c2
    xy=[]
    for s in a:
        u=np.r_[v,fold.E,fold.E+fold.RAM,fold.T-fold.RAM]
        for angle,width,c in ((fold.P,fold.W1,c1),(q,w2,center)):
            start=c+np.tan(angle)*s-width/(2*np.cos(angle))
            u=np.r_[u,start+np.array([0.,fold.RAM,width/2,width-fold.RAM,width])/np.cos(angle)]
        u=np.unique(np.clip(u,0,fold.T));u=u[np.r_[True,np.diff(u)>2e-13]]
        xy.append(np.column_stack((np.full(len(u),s),u)))
    return np.vstack(xy),ph,lam

def best_pair(f,n,uv):
    best=np.inf;addr=None;near=0
    for i in range(0,len(f),64):
        d=f[None,:,:]-f[i:i+64,None,:]
        dd=np.einsum("imk,imk->im",d,d)
        cross=2*abs(np.einsum("imk,ik->im",d,n[i:i+64]))
        du=uv[None,:,:]-uv[i:i+64,None,:];mat=np.einsum("imk,imk->im",du,du)
        near+=int(np.count_nonzero((mat>0)&(mat<=1e-12)))
        score=np.divide(dd,cross,out=np.full_like(dd,np.inf),where=(cross>0)&(mat>1e-12))
        ii,j=np.unravel_index(np.argmin(score),score.shape)
        if score[ii,j]<best:best=float(score[ii,j]);addr=[uv[i+ii].tolist(),uv[j].tolist()]
    return [best,addr,near]

def run(folder):
    allrows=[]
    for lev,(ns,nv,nt,order) in enumerate(((13,49,7,16),(21,81,13,24),(31,129,25,32))):
        rows=[]
        for t in np.unique(np.r_[np.linspace(0,1,nt),1/6,1/3,.25]):
            uv,ph,lam=grid(ns,nv,float(t),order);a,v=uv.T
            j=fold.local_jet(a,v,float(t),True,1,order,False);f,ta,tv,aa,av,vv=np.moveaxis(j,1,0)
            d=lambda x,y:np.einsum("ij,ij->i",x,y)
            normal=np.cross(ta,tv);area=np.linalg.norm(normal,axis=1)
            normal/=area[:,None]
            cost=[np.max(abs(d(ta,ta)-1)),np.max(abs(d(ta,tv))),np.max(abs(d(tv,tv)-1))]
            ii=np.einsum("nki,ni->nk",j[:,3:6],normal)
            mat=np.stack((ii[:,0],ii[:,1],ii[:,1],ii[:,2]),axis=1).reshape(-1,2,2)
            _,sv,V=np.linalg.svd(np.swapaxes(j[:,1:3],1,2),full_matrices=False)
            kk=np.linalg.eigvalsh((V@mat@np.swapaxes(V,1,2))/(sv[:,:,None]*sv[:,None,:]))
            pair=best_pair(f,normal,uv);poses={}
            for side in (-1,1):
                targets=[]
                for upper in (True,False):
                    end=fold.local_jet(np.array([0.]),np.array([fold.T]),float(t),upper,side,order,False)[0]
                    beg=fold.local_jet(np.array([0.]),np.array([fold.T]),0.,upper,side,order,False)[0]
                    tr=end[0]-beg[0];targets.append(tr)
                    poses[str((upper,side))]=[tr.tolist(),np.max(abs(end[1:]-beg[1:]),axis=1).tolist()]
                poses["paired-translation-"+str(side)]=float(np.linalg.norm(targets[0]-targets[1]))
            rows.append({"time":float(t),"true_external_phase":float(ph),"lambda":float(lam),"points":len(f),
                "max_abs_G11_G12_G22":np.asarray(cost).tolist(),"minimum_area":float(area.min()),
                "maximum_principal":float(np.max(abs(kk))),"sampled_directed_pair_radius":pair,"terminal_poses":poses})
        allrows.append({"level":[ns,nv,nt,order],"rows":rows})
        print("R774 complete local fold level",lev,rows[-1],flush=True)
    obj={"schema":"R774-real-two-fold-complete-material-patch-study-v1","run":os.environ["GITHUB_RUN_ID"],
         "attempt":os.environ["GITHUB_RUN_ATTEMPT"],"source_commit":os.environ["R774_SOURCE_COMMIT"],
         "levels":allrows,"pair_scope":"all directed sampled material pairs separated by more than one microunit; near pairs counted; this is not a certified full-patch reach"}
    (folder/"fold.json").write_text(json.dumps(obj,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")
if __name__=="__main__":
    a=argparse.ArgumentParser(description=__doc__);a.add_argument("--folder",type=Path,required=True);v=a.parse_args()
    m.old.disk._public();v.folder.mkdir(exist_ok=True,parents=True);run(v.folder)
