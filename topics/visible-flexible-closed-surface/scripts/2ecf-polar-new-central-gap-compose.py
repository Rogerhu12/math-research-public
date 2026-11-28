#!/usr/bin/env python3
"""Compose a genuinely new gap-H65 prefix and its changed C2 port with the complete old suffix chart."""
import argparse
import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
for k in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[k]="1"
import mpmath as mp
import numpy as np


def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(sp)
    sys.modules[name]=obj;sp.loader.exec_module(obj)
    return obj


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):h.update(b)
    return h.hexdigest()


def canonical(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()


def dump(path,obj):
    with Path(path).open("x") as f:json.dump(obj,f,separators=(",",":"),allow_nan=False);f.write("\n")


def mean_radius(a,b):
    with mp.workdps(75):
        a,b=mp.mpf(a),mp.mpf(b)
        return 2*a*mp.ellipe(1-(b/a)**2)/mp.pi


def prepare(args):
    t0=time.monotonic();here=Path(__file__).resolve().parent
    parent_path=here/"2ecf-polar-raw-ramp-source-compose.py";par=load(parent_path,"parent_physical")
    parent,olddef,basis,_,mods,*_=par.validate_prepared(argparse.Namespace(scripts=args.scripts,prepared=args.parent_prepared))
    oldg11=json.loads(args.parent_observer.read_text());report=json.loads(args.master.read_text())
    if (report["rampSHA256"]!=sha(args.ramp) or report["coastSHA256"]!=sha(args.coast)
            or oldg11["sourceIdentity"]!=olddef["sourceIdentity"] or parent["sourceMetadata"]["nodes"]!=65):
        raise ValueError("Actual old and new physical sources required")
    if sha(args.old_ramp)!=parent["sourceMetadata"]["rampMasterSHA256"] or sha(args.old_coast)!=parent["sourceMetadata"]["coastMasterSHA256"]:
        raise ValueError("Old Gamma95 port identity mismatch")
    warm_path=args.scripts/"6a65-geometry-cauchy-unit-t-warm.py"
    warm=load(warm_path,"gap_transplant_warm")
    old=warm.WarmMaster(args.old_ramp,args.old_coast,coast_length=.02)
    new=warm.WarmMaster(args.ramp,args.coast,coast_length=.02)
    b=old.coast_end
    L=basis.end-b
    if (old.c,old.ramp,old.v,old.coast,b)!=(new.c,new.ramp,new.v,new.coast,new.coast_end) or new.A<1.4:raise ValueError("Changed material lengths or support")
    with mp.workdps(75):da=float(mean_radius(new.A,new.B)-mean_radius(old.A,old.B))
    c,r,ell=new.c,new.ramp,new.coast
    d=float(Fraction(c)+Fraction(r)+Fraction(ell)-Fraction(b));assert d==3/2**58
    identity=dict(schema="physical-new-central-gap-H65-Gamma95-plus-polar-port-difference-v1",
        oldSource=olddef["sourceIdentity"],masterSHA256=sha(args.master),rampMasterSHA256=sha(args.ramp),coastMasterSHA256=sha(args.coast),
        oldRampSHA256=sha(args.old_ramp),oldCoastSHA256=sha(args.old_coast),actualAxesHex=[new.A.hex(),new.B.hex()],
        nodes=len(new.sx),originalPhysicalS=basis.end,originalPhysicalB=b,wholeTailAndBothCapsAndZUnchanged=True,
        generator="raw physical Cauchy Hermite; Gamma95 short b as R261; old accurate polar chart plus its port delta times quintic PVA Hermite to zero at S",
        target="old exact scalar plus delta of true means of the two dyadic ellipses; unit on s<=b, quintic to zero at S; all endpoint derivatives fixed",
        deltaA0Numerical=da,warmSHA256=sha(warm_path),evaluationAtLiteralNodesNotIntervalCertified=True)
    code=canonical(identity);definition=copy.deepcopy(olddef)
    definition["sourceIdentity"]=dict(schema=identity["schema"],identitySHA256=code,sourceDefinition=identity)
    definition["pointConfig"]["central_a"]=new.A
    ex=load(here/"2ecf-polar-source-prefix-spans.py","newgap_stats")
    groups={};records={}
    keys=("X","Xs","Xu","Xss","Xsu","Xuu")
    for name in ("training","observer","independent"):
        rec=copy.deepcopy(oldg11 if name=="independent" else parent["caches"][name])
        nodes=np.asarray(rec["physicalNodes" if name=="independent" else "nodes"]);u=np.asarray(rec["angles"])
        for k,fn in rec["files"].items():
            if sha(fn)!=rec["SHA256"][k]:raise ValueError("Changed old cache")
        source=np.load(rec["files"]["jets"],mmap_mode="r")
        rd=np.load(rec["files"]["radius"],mmap_mode="r").copy()
        out=Path(str(args.prefix)+"-"+name+"-jets.npy").resolve()
        if out.exists():raise FileExistsError(out)
        jets=np.lib.format.open_memmap(out,mode="w+",dtype=source.dtype,shape=source.shape)
        jets[:]=source
        left_new=new.coast_port(ell,u);left_old=old.coast_port(ell,u)
        port_keys=("P","V","A","Pu","Vu","Au","Puu","Vuu","Auu")
        dp={k:left_new[k]-left_old[k] for k in port_keys}
        delta=np.stack([[dp[k] for k in block] for block in (("P","V","A"),("Pu","Vu","Au"),("Puu","Vuu","Auu"))])
        central=[i for i,s in enumerate(nodes) if s<=c]
        centre=np.stack([warm.packet_from_port(warm.ports.central_port(new.A,new.B,0.,u))[k] for k in keys])
        for i in central:
            jets[i]=centre
            jets[i,0,:,2]+=nodes[i]
        for i in np.flatnonzero((nodes>c)&(nodes<=b)):
            s=float(nodes[i])
            if s<=c+r:
                packet=new.jet(s,u)
            else:
                x=s-(c+r);t=x/(ell-d);co=x+d*t**3*(10+t*(-15+6*t))
                if s==b:co=ell
                ds=1+d*30*t*t*(1-t)**2/(ell-d);d2s=d*60*t*(1-t)*(1-2*t)/(ell-d)**2
                packet=warm.packet_from_port(new.coast_port(co,u))
                packet["Xss"]=packet["Xss"]*ds**2+packet["Xs"]*d2s
                packet["Xs"]=packet["Xs"]*ds;packet["Xsu"]=packet["Xsu"]*ds
            jets[i]=np.stack([packet[k] for k in keys])
        rd[nodes<=b,0]+=da
        for i in np.flatnonzero((nodes>b)&(nodes<basis.end)):
            s=nodes[i];tw=(s-b)/L
            mats=[warm.ports.hermite_weights(tw,L,j)[:3] for j in range(3)]
            jets[i]+=np.stack([mats[j]@block.reshape(3,-1) for block,j in (
                (delta[0],0),(delta[0],1),(delta[1],0),(delta[0],2),(delta[1],1),(delta[2],0))]).reshape(6,len(u),3)
            rd[i]+=da*np.array([k[0] for k in mats])
        ii=np.flatnonzero(nodes<=b)
        met,curv=ex.extrema(jets[ii],rd[ii,0,None])
        idx=np.unravel_index(np.argmax(met),met.shape)
        record=dict(schema=identity["schema"],newSourceSHA256=code,oldSourceRecord=rec["SHA256"],
            prefixSampleMetric=float(met[idx]),prefixSampleCurvature=float(curv.max()),
            prefixPeakNode=[float(nodes[ii[idx[0]]]),float(u[idx[1]])],prefixRadials=len(ii),
            actualPortDeltaMax={k:float(np.max(abs(v))) for k,v in dp.items()},
            tailIdentical=np.array_equal(jets[nodes>=basis.end],source[nodes>=basis.end]),finiteOnly=True)
        if not record["tailIdentical"]:raise ArithmeticError("Right cut and tail changed")
        jets.flush();del jets
        rout=Path(str(args.prefix)+"-"+name+"-radius.npy").resolve()
        with rout.open("xb") as f:np.save(f,rd)
        meta=Path(str(args.prefix)+"-"+name+"-source.json").resolve()
        record["jetSHA256"]=sha(out);record["radiusSHA256"]=sha(rout);dump(meta,record)
        rec["files"]=dict(jets=str(out),radius=str(rout),report=str(meta))
        rec["SHA256"]=dict(jets=record["jetSHA256"],radius=record["radiusSHA256"],report=sha(meta))
        rec["sourceDefinitionSHA256"]=code
        if name=="independent":
            rec.update(schema=identity["schema"]+"-independent",sourceIdentity=definition["sourceIdentity"],
                sourceEntrySHA256=sha(__file__),originalIndependentSHA256=sha(args.parent_observer))
            dump(str(args.prefix)+"-independent.json",rec)
        else:records[name]=rec
        groups[name]=record;print(name,json.dumps(record),flush=True)
    merged=dict(schema=identity["schema"]+"-prepared",definition=definition,definitionSHA256=canonical(definition),
        parentPrepared=str(args.parent_prepared.resolve()),parentPreparedSHA256=sha(args.parent_prepared),
        originalFullSpaceAuditParentSHA256=parent["parentPreparedSHA256"],parentPrepareEntrySHA256=sha(parent_path),
        prepareEntrySHA256=sha(__file__),caches=records,sourceMetadata=identity,groups=groups,seconds=time.monotonic()-t0)
    dump(str(args.prefix)+"-prepared.json",merged)


def validate_prepared(args):
    data=json.loads(args.prepared.read_text());par=Path(__file__).with_name("2ecf-polar-raw-ramp-source-compose.py")
    oldpath=Path(data["parentPrepared"]);de=data["definition"]
    if (data["prepareEntrySHA256"]!=sha(__file__) or data["definitionSHA256"]!=canonical(de) or sha(par)!=data["parentPrepareEntrySHA256"]
        or sha(oldpath)!=data["parentPreparedSHA256"]):raise ValueError("Actual gap composition identity changed")
    parent,old,basis,_,mods,*_=load(par,"gap_original_validation").validate_prepared(argparse.Namespace(scripts=args.scripts,prepared=oldpath))
    assert data["originalFullSpaceAuditParentSHA256"]==parent["parentPreparedSHA256"]
    caches={}
    for key,row in data["caches"].items():
        prior=parent["caches"][key]
        if any(row[k]!=prior[k] for k in ("nodes","angles","weights")):raise ValueError("Complete quadrature required")
        if any(sha(f)!=row["SHA256"][k] for k,f in row["files"].items()):raise ValueError("Changed new cache")
        caches[key]=mods["generic"].Cached(row)
    return data,de,basis,caches,mods,parent,old,basis


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for key in ("scripts","master","ramp","coast","old-ramp","old-coast","parent-prepared","parent-observer","prefix"):
        ap.add_argument("--"+key,type=Path,required=True)
    prepare(ap.parse_args())
