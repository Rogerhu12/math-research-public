#!/usr/bin/env python3
"""Complete critical high-kernel recovery from a true153x60 number-field system.

Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro,2026-11-16.
Original17 equations and every6188 source are retained in final products.
Only seven independent true columns plus the paid residue rank4259 can
establish completeness; finite-field kernel values are never lifted.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import signal
import sys
import time
from flint import fmpq

FORMAT="r150-critical-complete-high-number-field-seven-v1"
WEAK_SHA="f211696b5cb789f054e259648a54be7a60f2d8c7c7772d410143bc0025025b1b"
PINS={
 "generator":"2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186",
 "jet_actions":"2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332",
 "low_generator":"4d215c80fa40d5f3548fd604e4ed77c6317db44b5b80518a03cf15e2ceeffa2f",
 "field_helper":"54f88bdbd926d38fb7a78fdaa1128f6bae96617461e4d2d4e4064736f6cf842c"}
PARENT_PINS={
  "plus": {
    "receiptBytes": 29268,
    "receiptSHA256": "30043fb3e263f861166f439c198af93bc10a69a8c5940acad42fe0429c3d86e6",
    "binding": "fc1dd340764a2c3f419f2f8fa2cb13581585be8af1a680871ddac1d7fa157593",
    "rawBytes": 14425,
    "rawSHA256": "c7b70b2ec6155d0d9e3e4dc706ba5c39b3cd6433383458551f695c162600557e",
    "manifest": {
      "bytes": 10739,
      "file": "checkpoints/manifest.json",
      "sha256": "3a6c668298211eb5831ab35876f59ce88be6f164f50077a7dbb2e8f402aa8e98"
    }
  },
  "minus": {
    "receiptBytes": 29275,
    "receiptSHA256": "708cc521471fd10e493be27c206420ca34ef89db71a52791e3e0b5e21eb1954f",
    "binding": "108c040d0df21708a57e1bdc8ba64d796ad894d066476efa56871abd2ffa976d",
    "rawBytes": 14429,
    "rawSHA256": "79ef5a020dcdbf1a113eed0940208f5bad7449a6b4467f6c886429c708776885",
    "manifest": {
      "bytes": 10740,
      "file": "checkpoints/manifest.json",
      "sha256": "529a47b394c74f08558ef775f9a477c88d8a966ad536e06f85a10268dd6e8098"
    }
  },
  "e8": {
    "receiptBytes": 29037,
    "receiptSHA256": "8b17d7ffc4bc63f6a8d8d7be42df1767c8fe1088958e4a8745e394ef4898d211",
    "binding": "6b2bd281d07a3796c302c5ca8a09d00f22433fb9501c62ff0df682733d8ce7f5",
    "rawBytes": 14267,
    "rawSHA256": "dc8f194bbc11634cf60b3b40968ff3123d2cd60f61a87a752e7925e8744c90f7",
    "manifest": {
      "bytes": 10411,
      "file": "checkpoints/manifest.json",
      "sha256": "555f91cb50825c78aec5bafc8289bc277fd9f8a30e76a775f7aaa33bf49fdcf3"
    }
  }
}

HIGH_PINS={
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

def require(ok,message):
    if not ok:
        raise AssertionError(message)

def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":")).encode()

def sha_file(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for x in iter(lambda:f.read(1048576),b""):
            h.update(x)
    return h.hexdigest()

def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m

class BudgetStop(Exception):
    pass

class Cache:
    def __init__(self,root,binding):
        self.root=Path(root)
        self.root.mkdir(parents=True,exist_ok=True)
        self.binding=binding
        self.path=self.root/"manifest.json"
        if self.path.exists():
            self.manifest=json.loads(self.path.read_text())
            require(self.manifest["format"]==FORMAT and
                    self.manifest["binding"]==binding,"Same immutable phase ancestry")
        else:
            self.manifest={"format":FORMAT,"binding":binding,"stages":{}}
            self.flush()
    def flush(self):
        tmp=self.path.with_name("manifest.json.tmp")
        tmp.write_bytes(canonical(self.manifest))
        tmp.replace(self.path)
    def put(self,name,obj,verified):
        require("/" not in name,"Local phase name")
        payload={"format":FORMAT,"binding":self.binding,"stage":name,
                 "verified":bool(verified),"payload":obj}
        raw=canonical(payload)
        digest=hashlib.sha256(raw).hexdigest()
        path=self.root/(name+"-"+digest+".json.gz")
        if not path.exists():
            tmp=path.with_name(path.name+".tmp")
            with open(tmp,"wb") as f:
                with gzip.GzipFile(filename="",fileobj=f,mode="wb",
                                   compresslevel=1,mtime=0) as z:
                    z.write(raw)
            tmp.replace(path)
        record={"file":path.name,"bytes":path.stat().st_size,
                "sha256":sha_file(path),"payloadSHA256":digest,
                "verified":bool(verified),"temporaryOnly":True}
        self.manifest["stages"][name]=record
        self.flush()
        return record
    def get(self,name):
        r=self.manifest["stages"].get(name)
        if r is None:
            return None
        path=self.root/r["file"]
        require(path.stat().st_size==r["bytes"] and sha_file(path)==r["sha256"],
                "Saved phase complete bytes and SHA")
        with gzip.open(path,"rb") as z:
            raw=z.read()
        require(hashlib.sha256(raw).hexdigest()==r["payloadSHA256"],
                "Saved phase canonical payload SHA")
        obj=json.loads(raw)
        require(obj["format"]==FORMAT and obj["binding"]==self.binding and
                obj["stage"]==name and obj["verified"]==r["verified"],
                "Saved phase semantic binding and verified status")
        return obj["payload"]


class Parent:
    """Read only; a failed or unbound phase is never promoted."""
    def __init__(self,w,root,receipt,field):
        pin=PARENT_PINS[field]
        path=Path(receipt)
        require(path.stat().st_size==pin["receiptBytes"] and
                sha_file(path)==pin["receiptSHA256"],"Exact completed parent outer")
        outer=json.loads(path.read_text())
        result=outer["result"]
        require(outer["exitCode"]==0 and result["status"]=="completed" and
                result["scriptSHA256"]==WEAK_SHA and
                result["binding"]==pin["binding"] and
                outer["fullTemporaryReceiptBytes"]==pin["rawBytes"] and
                outer["fullTemporaryReceiptSHA256"]==pin["rawSHA256"],
                "Same completed original weak-slice parent")
        params=result["parameters"]
        require(params["field"]==field and params["allOriginal6188JetProductsZero"]
                and params["actualCanonicalLow"]["allEarlierRowsZero"]
                and params["candidateLeadingRank"]==9,
                "Original parent mathematical gates")
        self.root=Path(root)/"checkpoints"
        manifest=self.root/"manifest.json"
        require(manifest.stat().st_size==pin["manifest"]["bytes"] and
                sha_file(manifest)==pin["manifest"]["sha256"],"Pinned parent manifest")
        self.cache=w.Cache(self.root,pin["binding"])
        self.result=result
        self.pin=pin
    def get(self,name):
        record=self.cache.manifest["stages"].get(name)
        require(record is not None and record["verified"],
                "Only a complete verified original parent phase: "+name)
        value=self.cache.get(name)
        require(value is not None,"Required original parent phase")
        return value


def high_rank_bound(path,field):
    pin=HIGH_PINS[field]
    path=Path(path)
    require(path.stat().st_size==pin["bytes"] and sha_file(path)==pin["sha256"],
            "Exact complete6018-by4266 actual residue receipt")
    outer=json.loads(path.read_text())
    result=outer["result"]
    require(outer["exitCode"]==0 and result["status"]=="completed" and
            result["binding"]==pin["binding"] and
            result["scriptSHA256"]==pin["scriptSHA256"],"Actual complete high lower bound")
    p=result["parameters"]
    n=p["actualNativeRank"]
    require(p["field"]==field and n["rank"]==4259 and n["nullity"]==7,
            "Actual complete high rank4259 only")
    for key in ("all6018OriginalSourceRowsRetained","all4266OriginalHighColumnsRetained",
                "independentOriginalPivotMinorVerified","allDependentOriginalRowsReducedToZero"):
        require(n[key] is True,"Original complete rank gate "+key)
    for key in ("all6018WholeRowScalingsVerified","allHighLow101CrossEntriesZero",
                "all12036CompleteHighProductsZero","all12376OriginalParentProductsMatched"):
        require(p["originalPreparation"][key] is True,"Original number-field gate "+key)
    return p

def recover(F,h,w,m,actions,parent,cache,report,params):
    saved=cache.get("complete-original-number-field-high-kernel")
    if saved is not None:
        require(saved["all6018OriginalHighProductsZero"] and saved["independentColumns"],
                "Only already verified whole high columns are resumed")
        params.update(saved["summary"])
        return
    _,poly,physical=w.decode_polynomial_model(m,parent.get("original-polynomial-model"))
    coeff=w.field_coefficients(F,poly,0)
    qmeta=w.physical_quadratic_constant(F,h,m,coeff)
    require(qmeta==parent.result["parameters"]["quadraticPhysicalChecks"],
            "All original physical constant coefficients equal actual parent")
    L=[[coeff["linear"][j][0][0][i] for j in range(2,11)] for i in range(17)]
    C=[[coeff["linear"][j][1][0][i] for j in range(2,11)] for i in range(17)]
    D=[[coeff["linear"][j][2][0][i] for j in range(2,11)] for i in range(17)]
    q=[[coeff["pure"][0][i]] for i in range(17)]
    paid=parent.get("normal-linear-kernel")
    require(paid["rank"]==8 and paid["inputSHA256"]==F.matrix_hash(L),
            "Actual original normal linear rank8")
    V=F.matrix_from_json(paid["kernel"])
    require(h.shape(V)==(9,1) and h.zero_matrix(h.product(F,L,V)),
            "All17 original linear kernel products")
    rows,cols=paid["independentRows"],paid["independentColumns"]
    U=h.submatrix(L,rows,cols)
    factor=h.lu_factor(F,U,cache,"original-eight-normal-unit")
    zpart=h.lu_solve(F,factor,h.submatrix(q,rows,[0]))
    z=h.zeros(F,9,1)
    for i,c in enumerate(cols):
        z[c]=zpart[i][:]
    require(h.product(F,L,z)==q,"Actual q belongs to original im L; no guessed identity")
    _,vzmeta=w.exact_kernel(F,h,w.join_columns(V,z),cache,"independent-v-and-z",report)
    require(vzmeta["rank"]==2,"q nonzero and v,z independent")
    v=[a[0] for a in V];z=[a[0] for a in z]
    T=[
      [[F.mul(v[i],v[j]) for j in range(9)] for i in range(9)],
      [[F.mul(v[i],z[j])+F.mul(z[i],v[j]) for j in range(9)] for i in range(9)],
      [[F.mul(z[i],z[j]) for j in range(9)] for i in range(9)]]
    Zcomp=[[F.zero]*9,[-x for x in v],[-x for x in z]]
    for b in range(3):
        require(h.zero_matrix(w.add_matrices(h.product(F,L,T[b]),
                    h.product(F,q,[Zcomp[b]]))),
                "All153 equations L T_b + q Z_b^T zero")
    pairs=[(j,l) for j in range(9) for l in range(j,9)]
    require(len(pairs)==45,"Ordinary symmetric coordinates")
    A=h.zeros(F,153,60)
    CT=[h.product(F,C,t) for t in T]
    DT=[h.product(F,D,t) for t in T]
    for i in range(17):
        for j in range(9):
            row=9*i+j
            for a,(l,n) in enumerate(pairs):
                if j==l:
                    A[row][a]+=L[i][n]
                if j==n and n!=l:
                    A[row][a]+=L[i][l]
            A[row][45+j]=q[i][0]
            for b in range(3):
                A[row][54+b]=CT[b][i][j]
                A[row][57+b]=DT[b][i][j]
    K,km=w.exact_kernel(F,h,A,cache,"actual-153-by60-high-system",report)
    nk=h.shape(K)[1]
    require(0<nk<=7,"True high candidates cannot exceed the paid whole residue bound")
    Z1=h.zeros(F,135,nk);Z2=h.zeros(F,450,nk)
    ix1={key:i for i,key in enumerate(actions.target_columns(1))}
    ix2={key:i for i,key in enumerate(actions.target_columns(2))}
    for j in range(9):
        Z1[ix1[(0,2,(j+2,))]]=K[45+j][:]
        for a in range(nk):
            Z1[ix1[(1,2,(j+2,))]][a]=sum((F.mul(Zcomp[b][j],K[54+b][a])
                                                        for b in range(3)),F.zero)
            Z1[ix1[(0,3,(j+2,))]][a]=sum((F.mul(Zcomp[b][j],K[57+b][a])
                                                        for b in range(3)),F.zero)
    for pos,(j,l) in enumerate(pairs):
        Z2[ix2[(0,0,(j+2,l+2))]]=K[pos][:]
        for a in range(nk):
            Z2[ix2[(1,0,(j+2,l+2))]][a]=sum((F.mul(T[b][j][l],K[54+b][a])
                                                        for b in range(3)),F.zero)
            Z2[ix2[(0,1,(j+2,l+2))]][a]=sum((F.mul(T[b][j][l],K[57+b][a])
                                                        for b in range(3)),F.zero)
    high1=[key for key in actions.target_columns(1) if key[1]>=2]
    high=[Z1[ix1[key]][:] for key in high1]+Z2+h.zeros(F,990+1485+1287,nk)
    require(h.shape(high)==(4266,nk),"Complete4266 high target coordinates")
    _,im=w.exact_kernel(F,h,high,cache,"all-original-high-column-independence",report)
    require(im["rank"]==nk,"Actual number-field columns independent")
    product=w.action(F,h,actions,coeff,0,{1:Z1,2:Z2},nk)
    require(h.shape(product)==(6188,nk) and h.zero_matrix(product[170:]),
            "Every6018 original high source product zero")
    original_rows=[r for degree in range(4) for r in actions.source_rows(degree)]
    require(len(actions.source_rows(0))==170 and len(original_rows)==6188,
            "Exact complete original source partition")
    require(all(not x for key,row in zip(actions.target_columns(1),Z1)
                         if key[1]<2 for x in row),
            "No low101 coordinate hidden in the high columns")
    G=product[:170]
    exact=nk==7
    summary={"physicalCoefficientChecks":qmeta,"normalLinearRank":8,
      "qInImageLAll17Verified":True,"vAndZIndependent":True,
      "originalSymmetricBasisIdentityCoordinates":3*153,
      "smallSystem":w.compact_kernel(km),"smallSystemShape":[153,60],
      "trueHighKernelColumns":nk,"trueHighKernelSHA256":F.matrix_hash(high),
      "completeHighShape":[6018,4266],"all6018OriginalHighProductsZero":True,
      "originalProductCoordinates":6188*nk,"independentColumns":True,
      "allNormalThreeFourFiveCoordinatesZero":True,
      "oneNormalHighSupport":[[0,2],[1,2],[0,3]],
      "twoNormalHighSupport":[[0,0],[1,0],[0,1]],
      "completeHighKernelProved":exact,
      "numberFieldHighRank":4259 if exact else None,
      "numberFieldKernelDimensionLowerBound":nk,"numberFieldKernelDimensionUpperBound":7,
      "lowReturnShape":[170,nk],"lowReturnSHA256":F.matrix_hash(G),
      "noNewParameterConnectionYet":True}
    record=cache.put("complete-original-number-field-high-kernel",{
      "highColumns":F.matrix_json(high),"oneNormal":F.matrix_json(Z1),
      "twoNormal":F.matrix_json(Z2),"lowReturn":F.matrix_json(G),
      "originalProduct":F.matrix_json(product),"smallKernel":F.matrix_json(K),
      "smallSystemSHA256":F.matrix_hash(A),"v":F.matrix_json(V),
      "z":[F.encode(x) for x in z],
      "all6018OriginalHighProductsZero":True,"independentColumns":True,
      "summary":summary},True)
    params.update(summary);params["completeHighKernelCheckpoint"]=record

def main():
    ap=argparse.ArgumentParser()
    for name in PINS:
        ap.add_argument("--"+name.replace("_","-"),required=True)
    for name in ("weak-driver","parent-out","parent-receipt","high-rank-receipt","out"):
        ap.add_argument("--"+name,required=True)
    ap.add_argument("--field",choices=tuple(PARENT_PINS),required=True)
    ap.add_argument("--remaining-seconds",type=float,default=300)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args()
    require(0<a.remaining_seconds<=1800 and 512<=a.memory_mib<=8192,"Explicit resources")
    for key,value in PINS.items():
        require(sha_file(getattr(a,key))==value,"Pinned original helper "+key)
    require(sha_file(a.weak_driver)==WEAK_SHA,"Actual weak parent code")
    require(Path(a.out).resolve()!=Path(a.parent_out).resolve(),"Read-only actual parent")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    w=module_at("critical_q7_actual_parent",a.weak_driver)
    parent=Parent(w,a.parent_out,a.parent_receipt,a.field)
    bound=high_rank_bound(a.high_rank_receipt,a.field)
    source_sha=sha_file(__file__)
    binding=hashlib.sha256(canonical({"format":FORMAT,"scriptSHA256":source_sha,
      "helpers":PINS,"parentSourceSHA256":WEAK_SHA,"field":a.field,
      "weakParent":PARENT_PINS[a.field],"completeHighParent":HIGH_PINS[a.field]})).hexdigest()
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    cache=Cache(out/"checkpoints",binding)
    receipt=out/"critical-complete-high-number-field-seven-receipt.json"
    start=time.monotonic()
    result={"format":FORMAT,"status":"started","binding":binding,"scriptSHA256":source_sha,
      "parameters":{"field":a.field,"parent":PARENT_PINS[a.field],
       "highRankParent":HIGH_PINS[a.field],"helperSHA256":PINS,
       "remainingSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
       "actualResidueRankLowerBound":4259,"actualResidueKernelNotLifted":True,
       "originalSources":6188,"originalTargets":4367,"largeDataTemporaryOnly":True,
       "parentReadOnly":True,"trueKernelDimensionNotPrespecified":True}}
    def save():
        result["elapsedSeconds"]=time.monotonic()-start
        result["parameters"]["checkpointManifest"]={"file":"checkpoints/manifest.json",
          "bytes":cache.path.stat().st_size,"sha256":sha_file(cache.path)}
        raw=canonical(result);require(len(raw)<90000,"Small exact high-kernel receipt")
        tmp=receipt.with_name(receipt.name+".tmp");tmp.write_bytes(raw);tmp.replace(receipt)
    def report(phase,step):
        result["parameters"]["currentPhase"]={"name":phase,"step":step};save()
    def stop(signum,frame):
        raise BudgetStop("Actual number-field budget exhausted")
    signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    code=1
    try:
        m=w.load_module("critical_q7_original",a.generator)
        actions=w.load_module("critical_q7_actions",a.jet_actions)
        h=w.load_module("critical_q7_field",a.field_helper)
        F=w.make_field(h,w.FIELDS[a.field]["polynomial"])
        recover(F,h,w,m,actions,parent,cache,report,result["parameters"])
        result["status"]="completed";code=0
    except BudgetStop as exc:
        result["status"]="budget-checkpoint";code=75
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    except Exception as exc:
        result["status"]="failed";code=1
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);save()
        print(json.dumps({"status":result["status"],"receipt":str(receipt),
          "bytes":receipt.stat().st_size,"sha256":sha_file(receipt),
          "elapsedSeconds":result["elapsedSeconds"],
          "trueHighColumns":result["parameters"].get("trueHighKernelColumns")},
          sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    sys.exit(main())
