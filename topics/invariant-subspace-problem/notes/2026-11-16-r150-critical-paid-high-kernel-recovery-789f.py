#!/usr/bin/env python3
"""Recover and describe the complete paid residue high kernel; no elimination.

Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro,2026-11-16.
All large arrays remain in the original job's temporary filesystem.
A finite-field kernel is not promoted to a number-field kernel.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import signal
import struct
import subprocess
import sys
import time

FORMAT="r150-critical-paid-high-kernel-recovery-v1"
PARENT_SOURCE_SHA="4a9c045763014812e3805da7f7c24408e27775b3fac1dc8beb5940ba89626ef9"
ACTIONS_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
NATIVE_SHA="d4a4639d2920754160b2c5e9e08d6552bf925301c532273fb932e94cc440f44f"
PINS={
  "plus": {
    "field": "plus",
    "bytes": 34539,
    "sha256": "893ba678754194bbbc2aa5156039ad4db8dfa8d83a78f5d339ce109c066f47d3",
    "blob": "4d4988863bff007121897eb27f8a689ba24bffa5",
    "binding": "c3cda40e1e99f191eb5c34a29036525c5fbaa29952cad5b7d82bcfc7b56e316a",
    "scriptSHA256": "4a9c045763014812e3805da7f7c24408e27775b3fac1dc8beb5940ba89626ef9",
    "manifest": {
      "bytes": 1561,
      "file": "checkpoints/manifest.json",
      "sha256": "0db405992db5638e819e62b1e7aa6505fcbbab17260b4201bd07a62f587bbad0"
    }
  },
  "minus": {
    "field": "minus",
    "bytes": 35007,
    "sha256": "faf2a2bcc5ee9451f46868e677d4af7eedc65944a1b097d6ee65cf1207616e74",
    "blob": "df08d831de2751c659198f4966c535eff070f573",
    "binding": "65e7bd29f1e6ee6c35b932cd7f01d63e6fcbc0eb595e56e9d300bc5a9e0a92f1",
    "scriptSHA256": "4a9c045763014812e3805da7f7c24408e27775b3fac1dc8beb5940ba89626ef9",
    "manifest": {
      "bytes": 1562,
      "file": "checkpoints/manifest.json",
      "sha256": "b58a134e244e85f0eef5a66d34fa11414d3cddae585a3d0a5ae7f4b73f9d77af"
    }
  },
  "e8": {
    "field": "e8",
    "bytes": 42686,
    "sha256": "f5d8b9ddbe858deb2b04f16281feed88a47dab11f06946dca0eed7538f2e4eda",
    "blob": "b4d0dd92b112c477f99217050f710b6646136ac6",
    "binding": "1124ef03b855859da33751856495eb768ae100b5ddbeabe0515dea49adfbbefd",
    "scriptSHA256": "4a9c045763014812e3805da7f7c24408e27775b3fac1dc8beb5940ba89626ef9",
    "manifest": {
      "bytes": 1563,
      "file": "checkpoints/manifest.json",
      "sha256": "57296d33553aec729fd897a6b53f728aac5315dce9797a1844b0bcc7758d4f38"
    }
  }
}
NR=6018
NC=4266

def require(v,msg):
    if not v:
        raise AssertionError(msg)

def canonical(v):
    return json.dumps(v,sort_keys=True,separators=(",",":")).encode()

def sha_file(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for x in iter(lambda:f.read(1048576),b""):
            h.update(x)
    return h.hexdigest()

def descriptor(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,
            "sha256":sha_file(path),"temporaryOnly":True}

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m

def rank_mod(rows,p,n=7):
    basis={}
    for original in rows:
        row=list(original)
        require(len(row)==n,"Small projection has every kernel column")
        for j in sorted(basis):
            if row[j]:
                a=row[j]
                row=[(x-a*y)%p for x,y in zip(row,basis[j])]
        lead=next((j for j,x in enumerate(row) if x),None)
        if lead is not None:
            inv=pow(row[lead],-1,p)
            basis[lead]=[(x*inv)%p for x in row]
    return len(basis)

class BudgetStop(Exception):
    pass

def main():
    ap=argparse.ArgumentParser()
    for k in ("parent-driver","jet-actions","native-source","parent-out","parent-receipt","out"):
        ap.add_argument("--"+k,required=True)
    ap.add_argument("--field",choices=tuple(PINS),required=True)
    ap.add_argument("--remaining-seconds",type=float,default=60)
    ap.add_argument("--memory-mib",type=int,default=1024)
    ap.add_argument("--cxx",default="g++")
    a=ap.parse_args()
    require(0<a.remaining_seconds<=600 and 512<=a.memory_mib<=4096,"Finite explicit resources")
    require(sha_file(a.parent_driver)==PARENT_SOURCE_SHA and
            sha_file(a.jet_actions)==ACTIONS_SHA and sha_file(a.native_source)==NATIVE_SHA,
            "All immutable executable sources pinned")
    require(Path(a.out).resolve()!=Path(a.parent_out).resolve(),"Parent remains read only")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    pin=PINS[a.field]
    rp=Path(a.parent_receipt)
    require(rp.stat().st_size==pin["bytes"] and sha_file(rp)==pin["sha256"],
            "Exact actual complete-high parent outer")
    outer=json.loads(rp.read_text())
    paid=outer["result"]
    require(outer["exitCode"]==0 and paid["status"]=="completed" and
            paid["scriptSHA256"]==PARENT_SOURCE_SHA and paid["binding"]==pin["binding"],
            "Completed actual original parent")
    pp=paid["parameters"]
    pr=pp["actualNativeRank"]
    require(pr["rank"]==4259 and pr["nullity"]==7 and pr["originalSourceRows"]==NR
            and pr["originalTargetCoordinates"]==NC and pp["field"]==a.field,
            "Use only the three actual complete rank4259 ancestors")
    for key in ("all6018OriginalSourceRowsRetained","all4266OriginalHighColumnsRetained",
                "independentOriginalPivotMinorVerified","allDependentOriginalRowsReducedToZero"):
        require(pr[key] is True,"Paid native gate "+key)
    for key in ("all6018OriginalRowsRetained","all4266OriginalColumnsRetained",
                "all6018WholeRowScalingsVerified","allHighLow101CrossEntriesZero",
                "all12036CompleteHighProductsZero","all12376OriginalParentProductsMatched"):
        require(pp["originalPreparation"][key] is True,"Paid original gate "+key)
    parent_root=Path(a.parent_out)/"checkpoints"
    manifest=parent_root/"manifest.json"
    require(manifest.stat().st_size==pin["manifest"]["bytes"] and
            sha_file(manifest)==pin["manifest"]["sha256"],"Actual immutable parent manifest")
    d=load_module("critical_paid_h7_parent",a.parent_driver)
    actions=load_module("critical_paid_h7_actions",a.jet_actions)
    cache=d.Cache(parent_root,pin["binding"])
    def get(name):
        rec=cache.manifest["stages"].get(name)
        require(rec is not None and rec["verified"],"Verified paid phase "+name)
        obj=cache.get(name)
        require(obj is not None,"Actual paid phase available")
        return obj
    prepared=get("prepared-original-complete-high")
    completed=get("native-completed-original-high")
    require(prepared["binding"]==pin["binding"] and prepared["verified"] and
            completed["binding"]==pin["binding"] and completed["result"]==pr,
            "Actual parent phase identities")
    input_path=d.checked_file(parent_root,prepared["input"])
    pivdesc=completed["outputs"]["complete-high-normalized-pivots.bin"]
    piv_path=d.checked_file(parent_root/"native-result",pivdesc)
    source_sha=sha_file(__file__)
    binding=hashlib.sha256(canonical({"format":FORMAT,"scriptSHA256":source_sha,
      "parentSourceSHA256":PARENT_SOURCE_SHA,"actionsSHA256":ACTIONS_SHA,
      "nativeSHA256":NATIVE_SHA,"field":a.field,"parent":pin,
      "originalInput":prepared["input"],"originalPivots":pivdesc})).hexdigest()
    root=Path(a.out);root.mkdir(parents=True,exist_ok=True)
    receipt=root/"critical-paid-high-kernel-recovery-receipt.json"
    started=time.monotonic()
    deadline=started+a.remaining_seconds
    result={"format":FORMAT,"status":"started","scriptSHA256":source_sha,"binding":binding,
      "parameters":{"field":a.field,"parent":pin,"parentSourceSHA256":PARENT_SOURCE_SHA,
        "actionsSHA256":ACTIONS_SHA,"nativeSHA256":NATIVE_SHA,"parentIsReadOnly":True,
        "originalInput":prepared["input"],"originalPivots":pivdesc,
        "remainingSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
        "noNewGaussianElimination":True,"noNumberFieldKernelClaim":True,
        "allLargeDataTemporaryOnly":True}}
    def save():
        result["elapsedSeconds"]=time.monotonic()-started
        raw=canonical(result)
        require(len(raw)<90000,"Small recovery receipt")
        tmp=receipt.with_name(receipt.name+".tmp");tmp.write_bytes(raw);tmp.replace(receipt)
    def left():
        t=deadline-time.monotonic()
        if t<=0:
            raise BudgetStop("Recovery budget exhausted")
        return t
    def stop(signum,frame):
        raise BudgetStop("Recovery budget exhausted")
    signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    code=1
    try:
        srcs,columns,low,_,_=d.original_dictionaries(actions)
        meta=prepared["metadata"]
        require(hashlib.sha256(canonical(srcs)).hexdigest()==meta["sourceOrderSHA256"] and
                hashlib.sha256(canonical(columns)).hexdigest()==meta["targetOrderSHA256"] and
                hashlib.sha256(canonical(low)).hexdigest()==meta["low101OrderSHA256"],
                "Exact complete original coordinate dictionaries")
        require(meta["rowsWithClearedDenominatorDivisibleByPrime"]==0 and
                meta["rowsWithIntegerContentDivisibleByPrime"]==0,
                "All paid whole-row scales are units at this residue")
        result["parameters"]["sourceOrderSHA256"]=meta["sourceOrderSHA256"]
        result["parameters"]["targetOrderSHA256"]=meta["targetOrderSHA256"]
        result["parameters"]["allPaidRowScalingsAreResidueUnits"]=True
        binary=root/("kernel-recovery-"+NATIVE_SHA)
        log=root/"native-kernel-recovery.log"
        with log.open("wb") as f:
            cp=subprocess.run([a.cxx,"-O3","-std=c++17",str(Path(a.native_source).resolve()),
                               "-o",str(binary)],stdout=f,stderr=subprocess.STDOUT,
                              timeout=left(),check=False)
        require(cp.returncode==0,"Recovery native compilation failed; see log")
        with log.open("ab") as f:
            cp=subprocess.run([str(binary.resolve()),str(input_path.resolve()),
                str(piv_path.resolve()),str(root.resolve()),str(left()),binding],
                stdout=f,stderr=subprocess.STDOUT,timeout=left(),check=False)
        if cp.returncode==124:
            raise BudgetStop("Native recovery actual budget")
        require(cp.returncode==0,"Native kernel recovery failed; see complete log")
        native=json.loads((root/"native-kernel-recovery-receipt.json").read_text())
        require(native["format"]==FORMAT and native["status"]=="completed"
                and native["binding"]==binding and native["parentBinding"]==pin["binding"]
                and native["rank"]==4259 and native["nullity"]==7
                and native["prime"]==pr["prime"],"Complete actual recovery identity")
        for key in ("allOriginalHighProductsZero","freeCoordinateBlockIsIdentity",
                    "allPivotPrefixesAndPaddingVerified","allInputAndPivotEOFVerified",
                    "noNewGaussianElimination","noRationalKernelClaim"):
            require(native[key] is True,"Native completed gate "+key)
        require(native["originalProductCoordinates"]==NR*7,"All42126 actual original products")
        path=root/"complete-high-free-kernel.bin"
        raw=path.read_bytes()
        require(len(raw)==152+2*7+NC*7 and raw[:8]==b"R15CKR01" and
                struct.unpack_from("<4I",raw,8)==(pr["prime"],NR,NC,7) and
                raw[24:88].decode()==binding and raw[88:152].decode()==pin["binding"],
                "Complete saved kernel binary identity")
        free=list(struct.unpack_from("<7H",raw,152))
        require(free==native["freeHighColumnsZeroBased"] and len(set(free))==7,
                "Seven actual free original coordinates")
        K=[list(raw[166+7*i:166+7*(i+1)]) for i in range(NC)]
        p=pr["prime"]
        require(all(v<p for row in K for v in row) and
                all(K[c]==[int(k==j) for j in range(7)] for k,c in enumerate(free)),
                "Complete canonical field matrix and free I7")
        groups={}
        for i,(r,(ca,db,mon)) in enumerate(columns):
            groups.setdefault((r,ca,db),[]).append(i)
        block_profiles=[]
        for (r,ca,db),indices in sorted(groups.items()):
            counts=[sum(K[i][k]!=0 for i in indices) for k in range(7)]
            samples=[]
            for k in range(7):
                ix=[i for i in indices if K[i][k]]
                samples.append([[i,K[i][k]] for i in ix[:4]])
            block_profiles.append({"normalDegree":r,"cDegree":ca,"dDegree":db,
              "ordinaryTotalDegree":r+ca+db,"coordinateCount":len(indices),
              "projectionRank":rank_mod([K[i] for i in indices],p),
              "columnNonzeroCounts":counts,"firstFourNonzeroHighCoordinateSamples":samples,
              "blockSHA256":hashlib.sha256(bytes(v for i in indices for v in K[i])).hexdigest()})
        per_columns=[]
        for k in range(7):
            ix=[i for i in range(NC) if K[i][k]]
            per_columns.append({"column":k,"freeHighCoordinate":free[k],
              "freeOriginalTarget":columns[free[k]],"nonzeroCoordinates":len(ix),
              "maximumNormalDegree":max(columns[i][0] for i in ix),
              "maximumTangentDegree":max(sum(columns[i][1][:2]) for i in ix),
              "maximumTotalDegree":max(columns[i][0]+sum(columns[i][1][:2]) for i in ix),
              "supportHighCoordinatesSHA256":hashlib.sha256(canonical(ix)).hexdigest(),
              "coefficientColumnSHA256":hashlib.sha256(bytes(K[i][k] for i in range(NC))).hexdigest()})
        sector_profiles=[]
        for r in range(1,6):
            ix=[i for i,c in enumerate(columns) if c[0]==r]
            sector_profiles.append({"normalDegree":r,"coordinates":len(ix),
             "projectionRank":rank_mod([K[i] for i in ix],p),
             "columnNonzeroCounts":[sum(K[i][k]!=0 for i in ix) for k in range(7)]})
        result["parameters"].update({"nativeResult":native,"completeKernel":descriptor(path),
          "kernelLogicalSHA256":hashlib.sha256(bytes(v for row in K for v in row)).hexdigest(),
          "freeOriginalTargets":[columns[i] for i in free],"perColumnSupport":per_columns,
          "normalSectorProjections":sector_profiles,"completeTangentBlockProjections":block_profiles,
          "all4266KernelRowsRead":True,"allSevenFreeColumnsIndependent":True,
          "all42126OriginalHighProductsZero":True,
          "numberFieldKernelBoundsRemain":[2,7],
          "nextNumberFieldConstructionMustBeVerifiedOverTheOriginalField":True})
        result["status"]="completed";code=0
    except (BudgetStop,subprocess.TimeoutExpired) as exc:
        result["status"]="budget-checkpoint";code=75
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    except Exception as exc:
        result["status"]="failed";code=1
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);save()
        print(json.dumps({"status":result["status"],"receipt":str(receipt),
          "bytes":receipt.stat().st_size,"sha256":sha_file(receipt),
          "elapsedSeconds":result["elapsedSeconds"]},sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    sys.exit(main())
