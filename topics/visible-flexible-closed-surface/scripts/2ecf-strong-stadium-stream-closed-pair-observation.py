#!/usr/bin/env python3
"""Stream genuine ordered tangent-ball observations on both p32 halves, R205, and flat disks."""
import os
for key in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):
    os.environ[key]="1"
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.spatial import cKDTree


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp)
    sys.modules[n]=m;sp.loader.exec_module(m);return m


home=Path(__file__).parent
arb=load(home/"2ecf-strong-stadium-arbitrary-physical-suffix.py","dense_actual_p32_two_sides");c=arb.c


def cloud(f,args):
    d=arb.rd(args.observer);au=np.asarray(d["angles"]);N=args.count
    if len(au)%N:raise ValueError("Use one equally-spaced subset of the independent shifted true outer R205 angles")
    stride=len(au)//N;u=au[::stride]
    turns=np.array([.179,.509,.838]);kb=f.cutraw.breaks
    fresh=(kb[:-1,None]+np.diff(kb)[:,None]*turns[None,:]).ravel()
    xx=np.unique(np.r_[np.linspace(0,f.b,41),np.linspace(f.b,f.cut,28),fresh,kb])
    outer=np.asarray(d["physicalNodes"]);oi=np.flatnonzero(outer>f.end)
    oi=np.unique(np.r_[oi[::max(1,len(oi)//46)],oi[-1]])
    jets=[]
    for j in range(0,len(xx),6):jets.append(f.jets(xx[j:j+6],u)[0][:,:3])
    if c.sha(d["files"]["jets"])!=d["SHA256"]["jets"]:raise ValueError("Original outer physical field required")
    raw=np.load(d["files"]["jets"],mmap_mode="r")
    jets.append(raw[oi][:,:3,::stride]);xs=np.r_[xx,outer[oi]]
    H=np.concatenate(jets);P=H[:,0].reshape(-1,3);n=np.cross(H[:,1],H[:,2]).reshape(-1,3);n/=np.linalg.norm(n,axis=1)[:,None]
    # Cartesian points on the actual horizontal flat disk. Include both centers and skip the duplicated outer ring.
    diskR=.32;dr=diskR/13
    Pdisk=[[0.,0.,.51]];ud=[0.];rd=[0.]
    for r in np.arange(1,13)*dr:
        angles=u+(np.pi/N if int(round(r/dr))%2 else 0.)
        Pdisk.extend(np.column_stack([r*np.cos(angles),r*np.sin(angles),np.full(N,.51)]))
        ud.extend(angles);rd.extend([r]*N)
    P=np.r_[P,np.asarray(Pdisk)];n=np.r_[n,np.tile([0,0,1],(len(Pdisk),1))]
    material=np.r_[np.repeat(xs,N),np.full(len(Pdisk),xs[-1])+diskR-np.asarray(rd)]
    angle=np.r_[np.tile(u,len(xs)),ud]
    kind=np.r_[np.repeat(np.where(xs<=f.cut,0,np.where(xs<=f.end,1,2)),N),np.full(len(Pdisk),3,dtype=int)]
    both=np.flatnonzero(material>0);flip=np.array([1,1,-1])
    return np.r_[P,P[both]*flip],np.r_[n,n[both]*flip],np.r_[material,-material[both]],np.r_[angle,angle[both]],np.r_[kind,kind[both]]


def run(args):
    st=time.monotonic();f=arb.Field(args)
    P,n,x,u,kind=cloud(f,args);R=args.reach;tree=cKDTree(P)
    parts=("locked prefix","free suffix","fixed developed tail","flat filling disk")
    best={};admitted=0;dups=0;mind=np.inf
    for start in range(0,len(P),args.batch):
        stop=min(start+args.batch,len(P));near=tree.query_ball_point(P[start:stop],2*R+args.chord_extra)
        I=np.repeat(np.arange(start,stop),list(map(len,near)));J=np.concatenate(near).astype(int)
        use=J!=I;I,J=I[use],J[use];d=P[J]-P[I];d2=np.einsum("ij,ij->i",d,d)
        dups+=int(np.sum(d2<1e-24));mind=min(mind,float(d2.min()));admitted+=len(I)
        sn=np.einsum("ij,ij->i",n[I],d)
        ratio=np.divide(d2,2*abs(sn),out=np.full_like(sn,np.inf),where=abs(sn)>0.)
        gap=abs(x[J]-x[I])
        keys=4*kind[I]+kind[J]
        for typ,mask in (("all",np.ones(len(I),dtype=bool)),("far",gap>.19),("opposite",x[I]*x[J]<0)):
            for k in np.unique(keys[mask]):
                jj=np.flatnonzero(mask&(keys==k));a=jj[np.argmin(ratio[jj])]
                val=float(ratio[a]);key=(typ,int(k))
                if val<best.get(key,(np.inf,))[0]:best[key]=(val,int(I[a]),int(J[a]),float(np.sqrt(d2[a])))
    rows=[]
    for (typ,k),(v,i,j,dist) in sorted(best.items(),key=lambda it:it[1][0]):
        rows.append(dict(group=typ,first=parts[k//4],second=parts[k%4],radius=v,chord=dist,
            firstMaterial=float(x[i]),firstU=float(u[i]),secondMaterial=float(x[j]),secondU=float(u[j]),
            P=P[i].tolist(),Q=P[j].tolist(),normalAtFirst=n[i].tolist()))
    result=dict(schema="streaming-shifted-both-sides-complete-flat-core-point-pair-receipt-v1",sourceMetric=f.ident,
        sourceStates=[c.sha(z) for z in args.extra_state],entry=c.sha(__file__),points=len(P),orderedPairsSeen=admitted,
        maximumChord=2*R+args.chord_extra,angles=args.count,minimumDistinctChord=float(np.sqrt(mind)),nanocoincidences=dups,
        sampledMinimum=min(q["radius"] for q in rows),finitePairObservations=rows,
        upperAndLowerIncluded=True,flatDiskIncluded=True,reachLowerBoundCertified=False,seconds=time.monotonic()-st)
    if dups:raise ArithmeticError(("Observed coincident material points",dups))
    receipt=c.save(Path(str(args.prefix)+"-two-sided-pairs.json"),result)
    print(json.dumps(dict(points=len(P),pairs=admitted,minimum=result["sampledMinimum"],far=min(q["radius"] for q in rows if q["group"]=="far"),
        opposite=min(q["radius"] for q in rows if q["group"]=="opposite"),SHA=receipt)),flush=True)


if __name__=="__main__":
    p=arb.parser();p.add_argument("--count",type=int,default=128);p.add_argument("--batch",type=int,default=48)
    p.add_argument("--reach",type=float,default=.097);p.add_argument("--chord-extra",type=float,default=.008)
    a=p.parse_args();a.resume=None;run(a)
