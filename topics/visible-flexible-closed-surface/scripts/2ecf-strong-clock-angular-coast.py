#!/usr/bin/env python3
"""New fixed-length chart with physical s derivatives of angularly localized coast corrections."""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[k]="1"
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import BSpline

def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p)
    a=importlib.util.module_from_spec(spec)
    sys.modules[name]=a
    spec.loader.exec_module(a)
    return a

clockmod=load(Path(__file__).with_name("2ecf-strong-new-material-clock.py"),"newcoastclock")
lm=load(Path(__file__).with_name("2ecf-strong-new-material-solve.py"),"newcoastbase")
RADIAL=(.0025,.005,.009,.016,.028,.05,.085,.135,.19)
FREQ=(0,2,4,8,14,22)

def radial(b,x,clock):
    T=np.r_[np.repeat(b,6),b+np.asarray(RADIAL),np.repeat(b+.24,6)]
    f=BSpline(T,np.eye(len(T)-6),5,extrapolate=False)
    m=(x>b)&(x<b+.24)
    v=clock.jets(x)[1][:,None]
    vx=clock.jets(x)[2][:,None]
    z=[]
    for j in range(3):
        a=np.zeros((len(x),len(RADIAL)))
        a[m]=f(x[m],nu=j)[:,3:-3]
        z.append(a)
    return z[0],z[1]/v,z[2]/v**2-z[1]*vx/v**3

def angular(u):
    k=np.array(FREQ)
    w=u[:,None]*k
    return np.cos(w),-k*np.sin(w),-k**2*np.cos(w)

def scalar_basis(rad,ang):
    return [np.einsum("ri,uj->ruij",rad[r],ang[a]).reshape(len(rad[r]),len(ang[a]),-1)
        for r,a in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))]

def variations(D,rad,ang):
    # Shape (radial, angular, jet, cartesian component, physical parameter).
    h=scalar_basis(rad,ang)
    delta=D.swapaxes(1,2)
    v=delta[...,None]*h[0][:,:,None,None,:]
    for j,t,der,mult in ((1,1,0,1),(2,2,0,1),(3,3,0,1),(3,1,1,2),
                 (4,4,0,1),(4,1,2,1),(4,2,1,1),(5,5,0,1),(5,2,2,2)):
        v[:,:,j]+=mult*delta[:,:,der,:,None]*h[t][:,:,None,:]
    return v

def main(args):
    tic=time.monotonic()
    saved,definition,coarse,basis,caches,mods,z,alpha,radius,parent=clockmod.inputs(args)
    doc=json.loads(args.clock.read_text())
    binding=doc["definition"]
    warm=json.loads(args.warm.read_text())
    if (clockmod.stable(binding)!=doc["definitionSHA256"] or warm["model"]["clockDefinitionSHA256"]!=doc["definitionSHA256"]
            or warm["model"]["solveEntrySHA256"]!=clockmod.sha(lm.__file__) or warm["model"]["prepareSHA256"]!=clockmod.sha(args.prepared)
            or warm["model"]["warmParentSHA256"]!=clockmod.sha(args.parent)):
        raise ValueError("An actual complete newly clocked field is required")
    z=np.asarray(warm["z"]).reshape(basis.nb,basis.na)
    clock=clockmod.Clock(basis,[float.fromhex(v) for v in binding["gammaHex"]])
    stream=mods["stream"]
    cfg0=stream.point.PointConfig(**definition["pointConfig"])
    cfga=stream.point.PointConfig(**dict(definition["pointConfig"],curvature_tau=args.curvature_tau))
    peak=load(args.helpers/"2ecf-polar-peak-sextic-point.py","newcoastpeak")
    oldPoint,fitPoint=peak.install(stream,args.beta)
    area=radius.dependencies(args.scripts)["area"]
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","newcoastdirect").direct_packet
    coast=load(args.helpers/"2ecf-polar-extended-coast-splice.py","newcoastverify")
    independent=json.loads(args.observer.read_text())
    if (independent["sourceIdentity"]!=definition["sourceIdentity"] or any(clockmod.sha(p)!=independent["SHA256"][k]
            for k,p in independent["files"].items())):
        raise ValueError("Original G11 changed")
    caches["independent"]=SimpleNamespace(nodes=np.asarray(independent["physicalNodes"]),u=np.asarray(independent["angles"]),
        jets=np.load(independent["files"]["jets"],mmap_mode="r"),radius=np.load(independent["files"]["radius"],mmap_mode="r"))
    groups={}
    for name,cache in caches.items():
        x,u=cache.nodes,cache.u
        shifted=name=="independent"
        pth=args.coast_dir/("polar-extended-coast-"+name+"-extended-coast.json")
        ix,other,_=coast.verified_coast(pth,clockmod.sha(args.observer if shifted else args.prepared),name,x,u)
        g=radius.LogRadiusCache(coarse,cache,alpha)
        s,h,hx=clock.jets(x)
        packet=cache.jets+(direct(basis,x,z,u) if shifted else basis.packet(basis.matrices(x),z,len(u)))
        stable=clockmod.physical_jet(packet,h,hx)
        D=clockmod.physical_jet(other-packet[ix],h[ix],hx[ix])
        wr={k:np.ones(len(x)) if shifted else .5*np.asarray(v)*h for k,v in saved["caches"]["training" if shifted else name]["weights"].items()}
        groups[name]=dict(x=x,u=u,s=s,ix=ix,D=D,rad=radial(basis.c,x[ix],clock),ang=angular(u),
            stable=stable,radius=g.radius[:,0],weights=wr,coastSHA=clockmod.sha(pth))
    nr=len(RADIAL)*len(FREQ)
    controls=np.zeros(nr)
    def evaluate(controls,name):
        group=groups[name]
        pos=group["stable"].copy()
        ix=group["ix"]
        for lo in range(0,len(ix),8):
            sl=slice(lo,lo+8)
            var=variations(group["D"][sl],[a[sl] for a in group["rad"]],group["ang"])
            pos[ix[sl]]+=np.einsum("rujcn,n->rujc",var,controls,optimize=True).swapaxes(1,2)
        total=None
        orig=enhanced=barriercost=0.
        N=len(group["u"])
        for lo in range(0,len(pos),16):
            sl=slice(lo,lo+16)
            packet=pos[sl]
            a=group["radius"][sl,None]
            W={k:v[sl,None]/N for k,v in group["weights"].items()}
            origpoint=oldPoint(packet.swapaxes(1,2),a,cfg0,W)
            fitpoint=fitPoint(packet.swapaxes(1,2),a,cfga,W)
            area_row=area.AreaPacket(packet,a,W["metric"],.5)
            part=stream._block_statistics(origpoint,group["x"][sl],N)
            for k in ("worstMetric","worstCurvature"):
                part[k]["u"]+=group["u"][0]
            total=stream._merge_statistics(total,part)
            orig+=float(np.sum(origpoint.residual**2))
            enhanced+=float(np.sum(fitpoint.residual**2))
            barriercost+=float(np.sum(area_row.residual**2))
        stats=lm.labels(total,clock)
        stats.pop("squaredNorm",None)
        stats.pop("groupSquaredNorm",None)
        return dict(original=orig+barriercost,enhanced=enhanced+barriercost,
            q2=barriercost,rows=len(pos)*N*14,statistics=stats)
    def physical(controls):
        return {name:evaluate(controls,name) for name in ("training","observer")}
    def score(groups,objective):
        return sum(g[objective] for g in groups.values())
    def normal(controls):
        G=np.zeros((nr,nr))
        S=np.zeros_like(G)
        grad=np.zeros(nr)
        for name in ("training","observer"):
            g=groups[name];inds=g["ix"];N=len(g["u"])
            for lo in range(0,len(inds),8):
                sl=slice(lo,lo+8);ix=inds[sl]
                var=variations(g["D"][sl],[m[sl] for m in g["rad"]],g["ang"])
                jet=g["stable"][ix].swapaxes(1,2)+np.einsum("rujcn,n->rujc",var,controls,optimize=True)
                W={k:w[ix,None]/N for k,w in g["weights"].items()}
                a=g["radius"][ix,None]
                point=fitPoint(jet,a,cfga,W)
                ar=area.AreaPacket(jet.swapaxes(1,2),a,W["metric"],.5)
                res=np.concatenate([point.residual,ar.residual[...,None]],axis=-1)
                J=np.empty((*res.shape,nr))
                cot=np.zeros_like(point.residual)
                for r in range(13):
                    cot[...,r]=1.
                    cj=point.vjp(cot)
                    J[...,r,:]=np.einsum("rujc,rujcn->run",cj,var,optimize=True)
                    cot[...,r]=0.
                J[...,13,:]=(np.einsum("ruc,rucn->run",ar.gs,var[:,:,1],optimize=True)
                    +np.einsum("ruc,rucn->run",ar.gu,var[:,:,2],optimize=True))
                j=J.reshape(-1,nr)
                G+=j.T@j
                grad+=j.T@res.ravel()
                # Sum of six true physical jet Grams with coefficient .01,1,1,.001,.002,.001.
                v=(var*np.sqrt(W["metric"])[:,:,None,None,None]
                    *np.sqrt([.01,1.,1.,.001,.002,.001])[None,None,:,None,None]).reshape(-1,nr)
                S+=v.T@v
        return G,grad,S
    current=physical(controls)
    if sum(g["rows"] for g in current.values())!=4291840 or abs(score(current,"original")-warm["evaluation"]["squaredNorm"])>1e-10:
        raise ArithmeticError("Reconstructed full fixed-g warm shape or all row costs differ")
    parent11=evaluate(controls,"independent")
    summary=dict(schema="new-positive-clock-angular-selective-coast-position-solve-v1",entry=clockmod.sha(__file__),
        clock=clockmod.sha(args.clock),warm=clockmod.sha(args.warm),parent=clockmod.sha(args.parent),prepared=clockmod.sha(args.prepared),
        observer=clockmod.sha(args.observer),coasts={k:g["coastSHA"] for k,g in groups.items()},
        fixedPhysicalTarget=doc["definitionSHA256"],radialInterior=list(RADIAL),harmonics=list(FREQ),
        additionalPositionColumns=nr,sourceDefinition="B_i(x)cos(ku) times extended coast minus complete warm field",
        physicalDamping="all six actual weighted H2 position jets",curvatureTau=args.curvature_tau,
        metricSextic=args.beta,additionalDescentCondition="original complete quartic must strictly decrease",
        initialDamping=args.damping,independentUsedForChoice=False,finiteOnly=True,
        initialG10=current,initialG11=parent11,history=[])
    damp=args.damping
    for step in range(1,args.steps+1):
        G,grad,S=normal(controls)
        old0=score(current,"original");old1=score(current,"enhanced")
        trace=[]
        accepted=False
        for unused in range(3):
            H=G+damp*S
            scale=1/np.sqrt(np.diag(H))
            direction=-scale*np.linalg.solve(scale[:,None]*H*scale[None,:],scale*grad)
            rel=float(np.linalg.norm(H@direction+grad)/np.linalg.norm(grad))
            if rel>1e-8:raise ArithmeticError("Unresolved full mixed normal")
            slope=float(grad@direction)
            for t in (1.,.5,.25,.125,.0625,.03125,.015625):
                test=physical(controls+t*direction)
                f0=score(test,"original");f1=score(test,"enhanced")
                ok=slope<0 and f0<old0 and f1<old1 and f1<=old1+2e-4*t*slope
                trace.append(dict(damping=damp,t=t,normalRelative=rel,original=f0,enhanced=f1,accepted=ok))
                if ok:
                    controls+=t*direction
                    current=test
                    damp=damp/3 if t==1 else 2*damp
                    accepted=True
                    break
            if accepted:break
            damp*=10
        g11=evaluate(controls,"independent")
        row=dict(accepted=accepted,own=sum(int(r["accepted"]) for r in summary["history"])+int(accepted),
            controlsHex=[float(q).hex() for q in controls],G10=current,G11=g11,trials=trace,nextDamping=damp,
            seconds=time.monotonic()-tic)
        summary["history"].append(row)
        p=Path(str(args.prefix)+f"-{step:02}.json")
        clockmod.save(p,summary)
        v=g11["statistics"]
        print(json.dumps(dict(step=step,accepted=accepted,normalRelative=rel,original=score(current,"original"),
            enhanced=score(current,"enhanced"),metric=v["maxRelativeMetric"],curvature=v["maxCurvature"],
            held=v["minHeldDistance"],SHA256=clockmod.sha(p),seconds=row["seconds"])),flush=True)
        if not accepted:break

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    clockmod.common_args(ap)
    for k in ("clock","observer","warm","coast-dir","prefix"):
        ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--curvature-tau",type=float,default=3.)
    ap.add_argument("--beta",type=float,default=.2)
    ap.add_argument("--damping",type=float,default=.02)
    ap.add_argument("--steps",type=int,default=3)
    main(ap.parse_args())
