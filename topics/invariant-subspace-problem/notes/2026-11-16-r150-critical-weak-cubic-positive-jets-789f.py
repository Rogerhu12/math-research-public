#!/usr/bin/env python3
"""Original critical positive jets across the pure cubic-normal layer.

Astra-ISP-789f / literature_audit; AI-assisted with GPT-6 Astra Pro.
2026-11-16. Exact original17 equations, all6188 source rows.

The high slice is normal2*tangent<=1 plus pure normal3 (135+165 values).
Its COMPLETE high kernel is ker[L,Cv,Dv,qvv], at most4 columns.
The parent canonical chains and original25 unit are read only.
A zero gain is restricted to this high slice and the declared low corrections.
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

FORMAT="r150-critical-weak-cubic-positive-jets-v1"
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


def prepare(F,h,w,m,actions,parent,order):
    small,poly,meta=w.decode_polynomial_model(m,parent.get("original-polynomial-model"))
    coeff=w.field_coefficients(F,poly,order)
    qmeta=w.physical_quadratic_constant(F,h,m,coeff)
    require(qmeta==parent.result["parameters"]["quadraticPhysicalChecks"],
            "All physical quadratic coefficients match completed parent")
    low=[(a,b,tuple(mon)) for a,b,mon in meta["lowTargetColumns"]]
    exact=[(a,b,tuple(mon)) for a,b,mon in meta["exactPureTargetColumns"]]
    raw,norm=h.normalize_and_taylor(F,small,order)
    S=[]
    for A in raw:
        B=h.zeros(F,51,36)
        for j,c in enumerate(norm["retainedOriginalLowColumns"]):
            for i in range(51):
                B[i][c]=A[i][j]
        S.append(B)
    paid=parent.get("canonical-low-jets")
    require(hashlib.sha256(canonical([F.matrix_hash(A) for A in S])).hexdigest()==
            paid["seriesIdentity"],"Every parent original Taylor coefficient matched")
    X=[F.matrix_from_json(A) for A in paid["jets"]]
    R=F.matrix_from_json(paid["exitResidual"])
    require(len(X)==order+1 and all(h.shape(A)==(36,11) for A in X),
            "All eleven original canonical cochains retained")
    for k in range(order+1):
        residual=h.zeros(F,51,11)
        for j in range(k+1):
            residual=w.add_matrices(residual,h.product(F,S[j],X[k-j]))
        require(residual==R if k==order else h.zero_matrix(residual),
                "Inherited entire low jet product")
    _,rows=w.row_indices(actions)
    E=w.embed_low(F,h,actions,low,h.identity(F,36))
    allowed=set(rows)
    units=[fmpq(x) for x in norm["nonzeroRationalRowContents"]]
    for k in range(order+1):
        product=w.action(F,h,actions,coeff,k,E,36)
        require(all(not x for i,row in enumerate(product) if i not in allowed for x in row),
                "All6137 inherited low-embedding outside rows zero")
        require([[x/units[i] for x in product[r]] for i,r in enumerate(rows)]==S[k],
                "Full original low Taylor block")
    km=parent.get("constant-low-kernel")
    ur,uc=km["independentRows"],km["independentColumns"]
    require(km["rank"]==25,"Paid constant rank25")
    U=h.submatrix(S[0],ur,uc)
    saved=parent.get("canonical-low-original-unit-unit-lu")
    require(saved["inputSHA256"]==F.matrix_hash(U),"Actual same original25 unit")
    factor=(F.matrix_from_json(saved["L"]),F.matrix_from_json(saved["U"]),saved["rows"])
    require(h.product(F,factor[0],factor[1])==[U[i] for i in factor[2]],
            "All625 original unit factor products")
    return coeff,low,exact,S,X,R,rows,units,ur,uc,U,factor,qmeta

def high_slice(F,h,w,actions,coeff,parent,cache,rows,units,report):
    L=[[coeff["linear"][j][0][0][i] for j in range(2,11)] for i in range(17)]
    C=[[coeff["linear"][j][1][0][i] for j in range(2,11)] for i in range(17)]
    D=[[coeff["linear"][j][2][0][i] for j in range(2,11)] for i in range(17)]
    paid=parent.get("normal-linear-kernel")
    require(paid["rank"]==8 and paid["inputSHA256"]==F.matrix_hash(L),
            "Actual same original rank8 linear part")
    V=F.matrix_from_json(paid["kernel"])
    require(h.shape(V)==(9,1) and h.zero_matrix(h.product(F,L,V)),
            "All original linear weak-vector products")
    v=[row[0] for row in V]
    Cv,Dv=h.product(F,C,V),h.product(F,D,V)
    qvv=[[sum((F.mul(coeff["quadratic"][(j,l)][0][i],
                         F.mul(v[j-2],v[l-2]))
                     for j in range(2,11) for l in range(j,11)),F.zero)]
          for i in range(17)]
    pencil=w.join_columns(L,Cv,Dv,qvv)
    K,km=w.exact_kernel(F,h,pencil,cache,"complete-weak-cubic-pencil",report)
    q=h.shape(K)[1]
    require(2<=q<=4,"Old two-dimensional slice retained; at most four columns")
    cols2,cols3=actions.target_columns(2),actions.target_columns(3)
    ix2={key:j for j,key in enumerate(cols2)}
    ix3={key:j for j,key in enumerate(cols3)}
    Z2,Z3=h.zeros(F,len(cols2),q),h.zeros(F,len(cols3),q)
    for j in range(2,11):
        for l in range(j,11):
            vv=F.mul(v[j-2],v[l-2])
            for a in range(q):
                Z2[ix2[(0,0,(j,l))]][a]=F.mul(v[j-2],K[l-2][a])+F.mul(K[j-2][a],v[l-2])
                Z2[ix2[(1,0,(j,l))]][a]=F.mul(K[9][a],vv)
                Z2[ix2[(0,1,(j,l))]][a]=F.mul(K[10][a],vv)
            for n in range(l,11):
                vvv=F.mul(vv,v[n-2])
                for a in range(q):
                    Z3[ix3[(0,0,(j,l,n))]][a]=F.mul(K[11][a],vvv)
    Z=Z2+Z3
    _,ind=w.exact_kernel(F,h,Z,cache,"complete-weak-cubic-column-rank",report)
    require(ind["rank"]==q,"Independent complete high-slice values")
    product=w.action(F,h,actions,coeff,0,{2:Z2,3:Z3},q)
    allowed=set(rows)
    require(all(not x for i,row in enumerate(product) if i not in allowed for x in row),
            "All6137 original source rows outside low51 zero, including allnormal2/3")
    G=[[x/units[i] for x in product[r]] for i,r in enumerate(rows)]
    old=F.matrix_from_json(parent.get("weak-quadratic-original-columns")["highColumns"])
    old=old+h.zeros(F,990,2)
    _,nested=w.exact_kernel(F,h,w.join_columns(Z,old),cache,
                           "weak-cubic-contains-complete-old-slice",report)
    require(nested["rank"]==q,"Every old quadratic high column belongs to the new slice")
    record=cache.put("complete-weak-cubic-high-slice",{
      "quadratic":F.matrix_json(Z2),"cubic":F.matrix_json(Z3),
      "pencilKernel":F.matrix_json(K),"qvv":F.matrix_json(qvv),
      "originalProduct":F.matrix_json(product),"scaledLowReturn":F.matrix_json(G),
      "all6137OutsideRowsZero":True,"all6188OriginalProductsVerified":True},True)
    return Z2,Z3,G,{"pencil":w.compact_kernel(km),"dimension":q,
       "quadraticSHA256":F.matrix_hash(Z2),"cubicSHA256":F.matrix_hash(Z3),
       "qvvSHA256":F.matrix_hash(qvv),"lowReturnSHA256":F.matrix_hash(G),
       "all6137OutsideRowsZero":True,"allOldQuadraticColumnsIncluded":True,
       "ordinaryCubicValuesHaveNoExtraMultiplicityFactor":True,
       "originalProductCoordinates":6188*q,"checkpoint":record}

def kernel_using_parent_unit(F,h,w,A,rows,cols,U,factor,cache,prefix,report):
    nr,nc=h.shape(A)
    require(h.submatrix(A,rows,cols)==U and len(rows)==len(cols)==25,
            "Same paid25 original unit within the larger equation")
    keep=[j for j in range(nc) if j not in set(cols)]
    rest=[i for i in range(nr) if i not in set(rows)]
    key=prefix+"-old-unit-graph"
    old=cache.get(key)
    digest=F.matrix_hash(A)
    if old is None:
        rhs=w.negate(h.submatrix(A,rows,keep))
        X=h.lu_solve(F,factor,rhs)
        require(h.product(F,U,X)==rhs,"All old25 actual new right-hand sides")
        graph=h.zeros(F,nc,len(keep))
        for j,c in enumerate(keep):
            graph[c][j]=F.one
        for i,c in enumerate(cols):
            graph[c]=X[i][:]
        full=h.product(F,A,graph)
        require(h.zero_matrix(h.submatrix(full,rows,range(len(keep)))),
                "All original reused unit rows zero")
        schur=h.submatrix(full,rest,range(len(keep)))
        cache.put(key,{"inputSHA256":digest,"graph":F.matrix_json(graph),
                      "fullProduct":F.matrix_json(full),"schur":F.matrix_json(schur),
                      "allUnitEquationsVerified":True},True)
    else:
        require(old["inputSHA256"]==digest and old["allUnitEquationsVerified"],
                "Same actual extended equation for continued Schur")
        graph=F.matrix_from_json(old["graph"])
        schur=F.matrix_from_json(old["schur"])
    K,km=w.exact_kernel(F,h,schur,cache,prefix+"-complete-schur",report)
    full_kernel=h.product(F,graph,K)
    require(h.zero_matrix(h.product(F,A,full_kernel)),
            "All original expanded equation rows times the complete kernel")
    meta={"inputShape":[nr,nc],"reusedUnitRank":25,
          "schurShape":list(h.shape(schur)),"schurRank":km["rank"],
          "rank":25+km["rank"],"kernelDimension":h.shape(full_kernel)[1],
          "originalInputSHA256":digest,"kernelSHA256":F.matrix_hash(full_kernel),
          "allOriginalRowsVerified":True}
    cache.put(prefix+"-complete-kernel",{"metadata":meta,
              "kernel":F.matrix_json(full_kernel)},True)
    return full_kernel,meta


def finish(F,h,w,actions,coeff,low,exact,S,X,R,Z2,Z3,G,order,upper,
           ur,uc,U,factor,cache,report,params):
    q=h.shape(Z2)[1]
    A=w.join_columns(S[0],G,R)
    K,km=kernel_using_parent_unit(F,h,w,A,ur,uc,U,factor,cache,
                                 "complete-weak-cubic-last-equation",report)
    H=h.submatrix(K,range(36+q,47+q),range(h.shape(K)[1]))
    _,hm=w.exact_kernel(F,h,H,cache,"weak-cubic-leading-projection",report)
    r=hm["rank"]
    require(9<=r<=11,"Actual low leading image contains the nine formal free heads")
    selected=h.submatrix(K,range(47+q),hm["independentColumns"])
    c=h.submatrix(selected,range(36+q,47+q),range(r))
    x=h.submatrix(selected,range(36),range(r))
    a=h.submatrix(selected,range(36,36+q),range(r))
    Y=[h.product(F,jet,c) for jet in X]
    Y[-1]=w.add_matrices(Y[-1],x)
    high2,high3=h.product(F,Z2,a),h.product(F,Z3,a)
    full=[]
    for k,jet in enumerate(Y):
        sections=w.embed_low(F,h,actions,low,jet)
        sections[2]=high2 if k==order else h.zeros(F,450,r)
        sections[3]=high3 if k==order else h.zeros(F,990,r)
        full.append(sections)
    pure=h.zeros(F,20,4)
    index={key:j for j,key in enumerate(actions.target_columns(0))}
    require(len(exact)==4,"All four additional exact pure columns retained")
    for j,key in enumerate(exact):
        pure[index[key]][j]=F.one
    for k in range(order+1):
        for degree in (0,1,2,3):
            extra=pure if k==0 and degree==0 else h.zeros(F,len(actions.target_columns(degree)),4)
            full[k][degree]=w.join_columns(full[k][degree],extra)
    width=r+4
    lead=sum((full[0][d] for d in (0,1,2,3)),[])
    _,lm=w.exact_kernel(F,h,lead,cache,"weak-cubic-full-leading-rank",report)
    require(lm["rank"]==width,"Actual original leading heads independent")
    hashes=[]
    for k in range(order+1):
        product=h.zeros(F,6188,width)
        for j in range(k+1):
            product=w.add_matrices(product,w.action(F,h,actions,coeff,j,full[k-j],width))
        require(h.zero_matrix(product),"Every original6188 jet product at order"+str(k))
        hashes.append(F.matrix_hash(product))
    gain=r-9
    lower=2*order+gain
    require(lower<=upper,"Positive length bound compatible with paid full upper")
    sq=[actions.target_columns(2).index((0,0,(j,j))) for j in range(2,11)]
    readouts=[]
    for k in range(order+1):
        a=h.submatrix(full[k][2],sq,range(width))
        readouts.append({"order":k,"shape":[9,width],"sha256":F.matrix_hash(a),
                         "nonzeroEntries":sum(bool(x) for row in a for x in row)})
    pack=cache.put("weak-cubic-full-original-jets-verified",{
      "cochains":[{str(d):F.matrix_json(a) for d,a in section.items()} for section in full],
      "targetSectors4And5ExactlyZero":True,"leadingMap":F.matrix_json(c),
      "selectedEquationKernel":F.matrix_json(selected),
      "all6188OriginalProductsZero":True,"originalProductSHA256":hashes,
      "fullLeadingRank":width,"gain":gain},True)
    params.update({"combined":km,"candidateLeadingRank":r,"fullLeadingRank":width,
      "additionalPositiveLengthLowerBound":gain,"fullOriginalLengthLowerBound":lower,
      "paidFullLengthUpperBound":upper,"all6188OriginalJetProductsZero":True,
      "originalJetProductCoordinates":6188*width*(order+1),
      "originalProductSHA256":hashes,"nineOriginalSquareReadouts":readouts,
      "completeCochainCheckpoint":pack,
      "zeroGainOnlyForDeclaredSupportAndInheritedLowerJets":True,
      "noFullHigherConnectionLowerBoundClaimed":True})

def main():
    ap=argparse.ArgumentParser()
    for name in PINS:
        ap.add_argument("--"+name.replace("_","-"),required=True)
    ap.add_argument("--weak-driver",required=True)
    ap.add_argument("--field",choices=tuple(PARENT_PINS),required=True)
    ap.add_argument("--parent-out",required=True)
    ap.add_argument("--parent-receipt",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--remaining-seconds",type=float,default=300)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args()
    require(0<a.remaining_seconds<=1800 and 512<=a.memory_mib<=8192,"Explicit budgets")
    for key,value in PINS.items():
        require(sha_file(getattr(a,key))==value,"Pinned actual helper "+key)
    require(sha_file(a.weak_driver)==WEAK_SHA,"Exact completed parent source")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    w=module_at("critical_cubic_weak_parent",a.weak_driver)
    parent=Parent(w,a.parent_out,a.parent_receipt,a.field)
    source_sha=sha_file(__file__)
    binding=hashlib.sha256(canonical({"format":FORMAT,"sourceSHA256":source_sha,
      "helperSHA256":PINS,"parentSourceSHA256":WEAK_SHA,
      "field":a.field,"parent":PARENT_PINS[a.field]})).hexdigest()
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    cache=Cache(out/"checkpoints",binding)
    receipt=out/"critical-weak-cubic-positive-jets-receipt.json"
    start=time.monotonic()
    setting=w.FIELDS[a.field]
    result={"format":FORMAT,"status":"started","binding":binding,
      "scriptSHA256":source_sha,"parameters":{
       "field":a.field,"minimalPolynomialAscending":setting["polynomial"],
       "parent":PARENT_PINS[a.field],"helperSHA256":PINS,
       "remainingSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
       "lastJetOrder":setting["exit"],"actualNaturalParameter":"t=s-alpha",
       "originalEquations":17,"originalSources":6188,"originalTargets":4367,
       "parentReadOnly":True,"newCanonicalSeriesSolved":False,
       "newMathematicalGainNotPrespecified":True,"largeDataUploadedOrCommitted":False}}
    def save():
        result["elapsedSeconds"]=time.monotonic()-start
        result["parameters"]["checkpointManifest"]={"file":"checkpoints/manifest.json",
          "bytes":cache.path.stat().st_size,"sha256":sha_file(cache.path)}
        raw=canonical(result);require(len(raw)<90000,"Small exact receipt")
        tmp=receipt.with_name(receipt.name+".tmp");tmp.write_bytes(raw);tmp.replace(receipt)
    def report(phase,step):
        result["parameters"]["currentPhase"]={"name":phase,"step":step};save()
    def stop(signum,frame):
        raise BudgetStop("Shared weak-cubic mathematical budget exhausted")
    signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    code=1
    try:
        m=w.load_module("critical_cubic_original",a.generator)
        actions=w.load_module("critical_cubic_actions",a.jet_actions)
        h=w.load_module("critical_cubic_field_helper",a.field_helper)
        F=w.make_field(h,setting["polynomial"])
        coeff,low,exact,S,X,R,rows,units,ur,uc,U,factor,qmeta=prepare(
             F,h,w,m,actions,parent,setting["exit"])
        result["parameters"].update({"quadraticPhysicalChecks":qmeta,
          "allParentTaylorCoefficientsMatched":True,"old25UnitSHA256":F.matrix_hash(U),
          "allInheritedCanonicalProductsVerified":True})
        save()
        Z2,Z3,G,meta=high_slice(F,h,w,actions,coeff,parent,cache,rows,units,report)
        result["parameters"]["completeHighSlice"]=meta;save()
        finish(F,h,w,actions,coeff,low,exact,S,X,R,Z2,Z3,G,setting["exit"],
               setting["upper"],ur,uc,U,factor,cache,report,result["parameters"])
        result["parameters"]["fieldArithmetic"]={"multiplications":F.mul_count,
                                                "verifiedInverses":F.inv_count}
        result["status"]="completed";code=0
    except BudgetStop as exc:
        result["status"]="budget-checkpoint"
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)};code=75
    except Exception as exc:
        result["status"]="failed"
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)};code=1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);save()
        print(json.dumps({"status":result["status"],"receipt":str(receipt),
          "bytes":receipt.stat().st_size,"sha256":sha_file(receipt),
          "elapsedSeconds":result["elapsedSeconds"],
          "gain":result["parameters"].get("additionalPositiveLengthLowerBound")},
          sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    sys.exit(main())
