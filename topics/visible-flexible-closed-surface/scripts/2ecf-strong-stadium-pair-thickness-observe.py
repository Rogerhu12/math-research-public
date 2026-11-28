#!/usr/bin/env python3
"""Actual upper core pairs and diameter witnesses on arbitrary p32 geometry, with origin labels."""
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.spatial import cKDTree


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m


here=Path(__file__).parent;arb=load(here/"2ecf-strong-stadium-arbitrary-physical-suffix.py","p32_tangent_ball_source");c=arb.c


def scan(args):
    ti=time.monotonic();f=arb.Field(args);N=args.count;u=2*np.pi*np.arange(N)/N
    if 192%N:raise ValueError("Use actual R205 later samples at the 192 angular grid")
    x0=np.r_[np.linspace(0.,f.b,20),np.linspace(f.b,f.cut,15),f.cutraw.breaks,(f.cutraw.breaks[:-1]+f.cutraw.breaks[1:])/2]
    x=np.unique(x0);pieces=[]
    for j in range(0,len(x),6):pieces.append(f.jets(x[j:j+6],u)[0][:,:3])
    J=np.concatenate(pieces);del pieces
    data=arb.rd(args.prepared)["caches"]["observer"];grid=np.asarray(data["nodes"]);raw=np.load(data["files"]["jets"],mmap_mode="r")
    ext=np.flatnonzero(grid>f.end)
    if len(ext):
        ext=np.unique(np.r_[ext[::max(1,len(ext)//28)],ext[-1]])
        J=np.concatenate((J,raw[ext][:,:3,::192//N]));x=np.r_[x,grid[ext]]
    P=J[:,0].reshape(-1,3);n=np.cross(J[:,1],J[:,2]).reshape(-1,3);n/=np.linalg.norm(n,axis=1)[:,None];tree=cKDTree(P)
    px=np.repeat(x,N);pu=np.tile(u,len(x));labels=np.where(px<=f.cut,"locked prefix",np.where(px>f.end,"fixed R205","movable"))
    rows=[];group={}
    for i,z in enumerate(P):
        which=np.array(tree.query_ball_point(z,args.chord),dtype=int)
        ds=abs(px[which]-px[i]);du=abs(np.angle(np.exp(1j*(pu[which]-pu[i]))));adv=(ds>args.radial_gap)|(du>args.angle_gap)
        rawidx=which[adv]
        if not len(rawidx):continue
        V=P[rawidx]-z;dist=np.sum(V*V,axis=1);nn=abs(V@n[i]);ok=(nn>1e-11)&(dist>1e-12)
        if not np.any(ok):continue
        idx=rawidx[ok];rr=dist[ok]/(2*nn[ok])
        for label in set(labels[idx]):
            jj=np.flatnonzero(labels[idx]==label);j=jj[np.argmin(rr[jj])];k=idx[j]
            record=dict(r=float(rr[j]),chord=float(np.sqrt(dist[ok][j])),x1=float(px[i]),u1=float(pu[i]),x2=float(px[k]),u2=float(pu[k]),
                part1=str(labels[i]),part2=str(label),P1=P[i].tolist(),P2=P[k].tolist(),normal=n[i].tolist())
            kk=(labels[i],label)
            if kk not in group or group[kk]["r"]>record["r"]:group[kk]=record
    # Antipodal support pair is just a valid diameter lower witness; no maximum claim is needed.
    eu=np.arange(96)*np.pi/96;directions=np.column_stack((np.cos(eu),np.sin(eu),np.zeros_like(eu)))
    supp=P@directions.T;i,j=np.argmax(supp,axis=0),np.argmin(supp,axis=0)
    d=np.linalg.norm(P[i]-P[j],axis=1);i0,j0=i[np.argmax(d)],j[np.argmax(d)]
    res=dict(schema="genuine-upper-stadium-closure-interior-Federer-witness-search-v1",entry=c.sha(__file__),source=c.sha(args.background),
        extra=[c.sha(q) for q in args.extra_state],actualPhysicalMetric=f.ident,radialCount=len(x),angles=N,points=len(P),minimumRadialSeparation=args.radial_gap,
        minimumAngularSeparation=args.angle_gap,searchChord=args.chord,originTaggedObservations=sorted(group.values(),key=lambda row:row["r"]),
        actualDiameterLowerWitness=dict(distance=float(d.max()),x1=float(px[i0]),u1=float(pu[i0]),x2=float(px[j0]),u2=float(pu[j0])),
        finiteObservationOnly=True,seconds=time.monotonic()-ti)
    c.save(Path(str(args.prefix)+"-tangent-pairs.json"),res)
    print(json.dumps(dict(diam=res["actualDiameterLowerWitness"],witness=[(z["part1"],z["part2"],z["r"],z["x1"],z["x2"]) for z in res["originTaggedObservations"]])),flush=True)


if __name__=="__main__":
    ap=arb.parser();ap.add_argument("--count",type=int,default=96);ap.add_argument("--chord",type=float,default=.26)
    ap.add_argument("--radial-gap",type=float,default=.055);ap.add_argument("--angle-gap",type=float,default=.30)
    args=ap.parse_args();args.resume=None;scan(args)
