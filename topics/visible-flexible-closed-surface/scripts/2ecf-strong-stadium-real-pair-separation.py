#!/usr/bin/env python3
"""Separate actual far-material p32 layers using directed chord supports and true held supports."""
import os
for key in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[key]="1"
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy import sparse
from scipy.optimize import linprog
from scipy.optimize._highspy import _core
from scipy.spatial import cKDTree


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m


here=Path(__file__).parent;mat=load(here/"2ecf-strong-stadium-actual-two-material-step.py","p32_pair_real_material_field")
arb=mat.arb;c=arb.c


def coarse(f,args):
    N=args.count;u=2*np.pi*np.arange(N)/N
    if 192%N:raise ValueError("Actual supplied outer R205 Fourier samples required")
    x=np.unique(np.r_[np.linspace(0.,f.b,20),np.linspace(f.b,f.cut,15),f.cutraw.breaks,
        (f.cutraw.breaks[:-1]+f.cutraw.breaks[1:])/2]);parts=[]
    for j in range(0,len(x),8):parts.append(f.jets(x[j:j+8],u)[0][:,:3])
    d=f.saved["caches"]["observer"];ox=np.asarray(d["nodes"]);ext=np.flatnonzero(ox>f.end);raw=np.load(d["files"]["jets"],mmap_mode="r")
    ext=np.unique(np.r_[ext[::max(1,len(ext)//28)],ext[-1]]);J=np.concatenate(parts+[raw[ext][:,:3,::192//N]])
    return np.r_[x,ox[ext]],u,J


def basis_from(f,args):
    t=np.linspace(0.,1.,args.controls+2);o=f.stream.HalfTurnBasis(f.cut,f.end,radial_count=args.controls,max_frequency=args.modes,
        normalized_breaks=.5*t+.5*t*t)
    o.channels=f.full_channels(args.modes);o.na=len(o.channels);o.modes=np.array([q[1] for q in o.channels]);o.dimension=o.nb*o.na
    o.definition=dict(schema="p32-unrestricted-spatial-pair-separating-clamped-Fourier-quintic-v1",physicalKnots=o.knots.tolist(),
        degree=5,dimension=o.dimension,angularChannels=o.na,radialBasisCount=o.nb,maxAngularFrequency=o.M,
        channelOrder=[dict(component=a,frequency=k,kind=z) for a,k,z in o.channels],allSixEndpointJetsZero=True)
    return c.physical_basis(o,f.dclock,f.ident)


def screen(P,n,px,pu,radial_gap,angle_gap,R,far):
    pair=cKDTree(P).query_pairs(R,output_type="ndarray");i,j=pair.T
    radial=abs(px[j]-px[i]);angular=abs(np.angle(np.exp(1j*(pu[j]-pu[i]))))
    keep=(radial>radial_gap)|(angular>angle_gap);i,j=i[keep],j[keep];d=P[j]-P[i];d2=np.sum(d*d,axis=1)
    den=2*np.maximum(abs(np.sum(d*n[i],axis=1)),abs(np.sum(d*n[j],axis=1)))
    ratio=np.divide(d2,den,out=np.full_like(d2,np.inf),where=den>1e-15)
    k=np.argmin(ratio)
    farids=abs(px[j]-px[i])>far
    return dict(radius=float(ratio[k]),minFarChord=float(np.sqrt(np.min(d2[farids]))),pairs=len(i),farPairs=int(sum(farids)),
        x1=float(px[i[k]]),u1=float(pu[i[k]]),x2=float(px[j[k]]),u2=float(pu[j[k]]),chord=float(np.sqrt(d2[k])))


def main(args):
    ti=time.monotonic();f=arb.Field(args);basis=basis_from(f,args);x,u,J=coarse(f,args);N=len(u)
    nvar=basis.dimension;nb,na=basis.nb,basis.na
    px=np.repeat(x,N);pu=np.tile(u,len(x));P=J[:,0].reshape(-1,3)
    def normals(S):
        n=np.cross(S[:,1],S[:,2]).reshape(-1,3)
        return n/np.linalg.norm(n,axis=1)[:,None]
    n=normals(J);pre=screen(P,n,px,pu,.055,.30,args.search,args.far)
    iid,jjd=cKDTree(P).query_pairs(args.pool,output_type="ndarray").T
    mask=abs(px[jjd]-px[iid])>args.far;iid,jjd=iid[mask],jjd[mask]
    d=P[jjd]-P[iid];length=np.linalg.norm(d,axis=1);direction=d/length[:,None]
    # For every kept pair its current chord direction gives an affine sufficient physical distance condition.
    comp=np.array([ch[0] for ch in basis.channels]);k=basis.modes;cs=np.array([q[2]=="cos" for q in basis.channels])
    trig=np.where(cs,np.cos(u[:,None]*k),np.sin(u[:,None]*k))
    B=basis.matrices(x)[0].toarray()
    def jac(points,v):
        a=points//N;b=points%N
        return (B[a,:,None]*(trig[b]*v[:,comp])[:,None,:]).reshape(len(points),nvar)
    pa=float(f.definition["pointConfig"]["central_a"])
    test=np.array([[0.,pa,0.],[0.,-pa,0.]])
    hvec=P[:,None,:]-test[None,:,:];hlen=np.linalg.norm(hvec,axis=2);hdir=hvec/hlen[...,None]
    # Cap upper height at the original measured guide plus a small allowance during the repair.
    geom=f.stream.point.geometry_cache(P,f.stream.point.PointConfig(**f.definition["pointConfig"]))
    priorHeld=float(hlen.min());coarseXYZ=basis.matrices(x)
    baseh=geom["signed"][:,3]
    scales=1/(1+.28*k*k);D=np.tile(scales,nb)
    # Select minimal amplitude plus a common bound on each scalar derivative in the physical coordinate.
    knots=basis.knots;g=np.unique(np.r_[basis.c,basis.end,(knots[3:-4]+knots[4:-3])/2,knots[3:-3]])
    _,b1,b2=basis.matrices(g);I=sparse.eye(na,format="csr")
    reg=[]
    for matrix,cap in ((sparse.eye(nb),.10),(b1,.65),(b2,10.)):
        reg.append(sparse.kron(matrix,I,format="csr")/cap)
    reg=sparse.vstack(reg,format="csr").multiply(D).tocsr()
    Zero=sparse.csr_matrix;eye=sparse.eye(nvar,format="csr")
    initial=sparse.vstack((sparse.hstack((reg,-np.ones((reg.shape[0],1)),Zero(reg.shape))),
        sparse.hstack((-reg,-np.ones((reg.shape[0],1)),Zero(reg.shape))),
        sparse.hstack((eye,Zero((nvar,1)),-eye)),sparse.hstack((-eye,Zero((nvar,1)),-eye))),format="csr")
    initialrhs=np.zeros(initial.shape[0]);objective=np.r_[np.zeros(nvar),1.,np.full(nvar,args.l1)]
    _core._Highs.resetGlobalScheduler(True);solutions=[];allhist=[]
    for target in args.targets:
        # Sweep fresh true support inequalities after each finite LP. Preserve all previously found constraints.
        z=np.zeros((nb,na));witness=[];rhs=[];seen=set();hist=[]
        for it in range(args.exchange):
            change=basis.packet(coarseXYZ,z,N)[:,0].reshape(-1,3)
            pv=target-(length+np.sum(direction*(change[jjd]-change[iid]),axis=1))
            hv=args.hold-(hlen+np.einsum("nsc,nc->ns",hdir,change))
            zv=baseh+change[:,2]-args.height_limit
            # This height upper uses the original allowance against a fixed initial radial location.
            # All actual updated guide values are subsequently recomputed from the moved Cartesian positions.
            violation=max(float(pv.max()),float(hv.max()),float(zv.max()))
            hist.append(dict(iteration=it,pair=float(pv.max()),held=float(hv.max()),height=float(zv.max()),totalChosen=len(seen)))
            if violation<args.tolerance:break
            add=0
            for label,values in (("p",pv),("h",hv.ravel()),("z",zv)):
                ix=np.flatnonzero(values>args.tolerance)
                if not len(ix):continue
                ix=sorted(ix,key=lambda i:values[i],reverse=True)
                chosen=[]
                for j in ix:
                    key=(label,int(j))
                    if key not in seen:
                        chosen.append(j);seen.add(key)
                    if len(chosen)>=args.batch:break
                if not chosen:continue
                j=np.array(chosen);add+=len(j)
                if label=="p":
                    A=jac(jjd[j],direction[j])-jac(iid[j],direction[j]);b=length[j]-target
                elif label=="h":
                    pos=j//2;sg=j%2;A=jac(pos,hdir[pos,sg]);b=hlen[pos,sg]-args.hold
                else:
                    vv=np.zeros((len(j),3));vv[:,2]=-1;A=jac(j,vv);b=args.height_limit-baseh[j]
                witness.append(sparse.csr_matrix(-A*D));rhs.append(b)
            if not add:break
            W=sparse.vstack(witness,format="csr")
            A=sparse.vstack((initial,sparse.hstack((W,Zero((W.shape[0],nvar+1))))),format="csr")
            sol=linprog(objective,A_ub=A,b_ub=np.r_[initialrhs,np.concatenate(rhs)],bounds=[(-.20,.20)]*nvar+[(0,None)]+[(0,.20)]*nvar,method="highs",options={"threads":1,"parallel":False})
            if not sol.success:hist[-1]["solver"]=sol.message;break
            z=(sol.x[:nvar]*D).reshape(nb,na)
        JJ=J+basis.packet(coarseXYZ,z,N)[:,:3]
        after=screen(JJ[:,0].reshape(-1,3),normals(JJ),px,pu,.055,.30,args.search,args.far)
        actualHeld=float(np.min(np.linalg.norm(JJ[:,0].reshape(-1,3)[:,None,:]-test[None,:,:],axis=2)))
        histinfo=dict(target=target,supportPool=len(length),history=hist,coarseTrue=after,actualHeld=actualHeld,
            dimension=nvar,pastAllOriginalAndNewPhysicalRows=False)
        solutions.append(z);allhist.append(histinfo)
        print(json.dumps(dict(target=target,baseline=pre,new=after,held=actualHeld,remaining=hist[-1],n=nvar)),flush=True)
    # All original physical samples with each literal new correction, evaluated at both resolutions.
    summary=[]
    for name in ("training","observer","independent"):
        xx,uu,yy,rad,w=mat.source_rows(f,name)
        for i,z in enumerate(solutions):
            shifted=yy.copy()
            for j in range(0,len(xx),12):
                sl=slice(j,j+12)
                shifted[sl]+=f.direct(basis,xx[sl],z,uu) if name=="independent" else basis.packet(basis.matrices(xx[sl]),z,len(uu))
            report=mat.observed(f,None,None,(xx,uu,shifted,rad,w),None,None,False,args)
            if len(summary)<=i:summary.append({})
            summary[i][name]=report
        del yy,shifted
    for i,(z,record) in enumerate(zip(solutions,allhist)):
        data=dict(schema="p32-genuine-full-XYZ-closed-layer-separation-and-held-support-v1",entry=c.sha(__file__),source=c.sha(args.background),
            sourceMetric=f.ident,previousPhysicalCorrection=c.sha(args.extra_state[-1]),physicalCorrectionBasis=basis.definition,coefficients=z.ravel().tolist(),
            frozenMeasure=record,targetDistance=args.targets[i],priorPairObservation=pre,actualG10AndG11=summary[i],
            originalFourMillionRowsPreserved=True,wholeClosedReachCertified=False,continuousMetricCertified=False,seconds=time.monotonic()-ti)
        sha=c.save(Path(str(args.prefix)+f"-{i+1:02}.json"),data)
        print(json.dumps(dict(target=args.targets[i],SHA=sha,G11={k:summary[i]["independent"][k] for k in ("metric","curvature","held")},radius=record["coarseTrue"]["radius"])),flush=True)


if __name__=="__main__":
    ap=arb.parser()
    for key,val in (("count",96),("controls",14),("modes",3),("batch",80),("exchange",24)):ap.add_argument("--"+key,type=int,default=val)
    for key,val in (("pool",.225),("search",.265),("far",.23),("hold",.645),("height-limit",.0025),("l1",.02),("tolerance",2e-5)):ap.add_argument("--"+key,type=float,default=val)
    ap.add_argument("--targets",type=float,nargs="+",default=[.18,.19,.198])
    args=ap.parse_args();args.resume=None;main(args)
