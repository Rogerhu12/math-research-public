#!/usr/bin/env python3
"""Complete first critical exit after the genuine seven-column high kernel.

Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro,2026-11-16.
Retains all original6188 equations and all lower cochain coefficients.
An86-column constant unit is solved only for seven high returns and two exits.
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

FORMAT="r150-critical-complete-first-critical-exit-v1"
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

Q7_SHA="de723d530fe0f2b3ab7876b76c8fc605a5156702309482f02a38c7b582a54753"
CUBIC_SHA="634b258dec87cdba34d01a2be8f1ab61fce7f944b910b5c9438343b3b423a314"

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


def read_high(a,q7):
    p=Path(a.high_receipt)
    require(p.stat().st_size==a.high_receipt_bytes and sha_file(p)==a.high_receipt_sha,
            "Pinned actual completed seven-kernel outer")
    outer=json.loads(p.read_text());paid=outer["result"]
    require(outer["exitCode"]==0 and paid["status"]=="completed" and
            paid["scriptSHA256"]==Q7_SHA,"Actual completed number-field generator")
    pp=paid["parameters"]
    require(pp["field"]==a.field and pp["parent"]==PARENT_PINS[a.field] and
            pp["highRankParent"]==HIGH_PINS[a.field] and pp["trueHighKernelColumns"]==7
            and pp["completeHighKernelProved"] and pp["all6018OriginalHighProductsZero"]
            and pp["independentColumns"] and pp["numberFieldHighRank"]==4259,
            "Complete original number-field high kernel, not a field candidate")
    r=Path(a.high_out)/"checkpoints";mf=r/"manifest.json";mi=pp["checkpointManifest"]
    require(mf.stat().st_size==mi["bytes"] and sha_file(mf)==mi["sha256"],
            "Actual immutable seven-kernel manifest")
    cache=q7.Cache(r,paid["binding"])
    record=cache.manifest["stages"].get("complete-original-number-field-high-kernel")
    require(record is not None and record["verified"],"Verified original seven-kernel phase")
    value=cache.get("complete-original-number-field-high-kernel")
    require(value["summary"]["completeHighKernelProved"] and
            value["all6018OriginalHighProductsZero"],"Complete high-kernel saved gates")
    identity={"bytes":a.high_receipt_bytes,"sha256":a.high_receipt_sha,
              "binding":paid["binding"],"manifest":mi,"checkpoint":record}
    return value,identity

def residue_profile(a,prime,root):
    from flint import fmpq
    def val(x):
        y=0
        for q in reversed(x.coeffs()):
            q=fmpq(q);num=int(q.p);den=int(q.q)
            require(den%prime!=0,"Selected whole-row profile coefficient residue unit")
            y=(y*root+(num%prime)*pow(den%prime,-1,prime))%prime
        return y
    b=[[val(x) for x in row] for row in a]
    nr,nc=len(b),len(b[0]);rs=list(range(nr));cs=list(range(nc));k=0
    while k<min(nr,nc):
        pivot=next(((i,j) for i in range(k,nr) for j in range(k,nc) if b[i][j]),None)
        if pivot is None:
            break
        i,j=pivot;b[i],b[k]=b[k],b[i];rs[i],rs[k]=rs[k],rs[i]
        if j!=k:
            for row in b:row[j],row[k]=row[k],row[j]
            cs[j],cs[k]=cs[k],cs[j]
        inv=pow(b[k][k],-1,prime)
        for i in range(k+1,nr):
            if b[i][k]:
                c=b[i][k]*inv%prime
                for j in range(k,nc):
                    b[i][j]=(b[i][j]-c*b[k][j])%prime
        k+=1
    return rs[:k],cs[:k]

def embed_low101(F,h,actions,columns,X):
    nc=h.shape(X)[1]
    out={r:h.zeros(F,len(actions.target_columns(r)),nc) for r in (0,1)}
    ix={r:{key:i for i,key in enumerate(actions.target_columns(r))} for r in (0,1)}
    for i,(r,key) in enumerate(columns):
        out[r][ix[r][key]]=X[i][:]
    return out

def compute(F,h,w,cubic,m,actions,parent,high,cache,report,params,setting):
    order=setting["exit"]
    coeff,low36,exact,series,X,R,oldrows,oldunits,_,_,_,_,qmeta=cubic.prepare(
        F,h,w,m,actions,parent,order)
    Z1=F.matrix_from_json(high["oneNormal"])
    Z2=F.matrix_from_json(high["twoNormal"])
    G=F.matrix_from_json(high["lowReturn"])
    require(h.shape(Z1)==(135,7) and h.shape(Z2)==(450,7) and h.shape(G)==(170,7),
            "All original high columns and returns")
    highprod=w.action(F,h,actions,coeff,0,{1:Z1,2:Z2},7)
    require(h.zero_matrix(highprod[170:]) and highprod[:170]==G,
            "All43316 original seven-column products rechecked")
    cols=[(0,key) for key in actions.target_columns(0)]+[
          (1,key) for key in actions.target_columns(1) if key[1]<2]
    require(len(cols)==101,"Complete low101 complement")
    lowI=embed_low101(F,h,actions,cols,h.identity(F,101))
    Sp=w.action(F,h,actions,coeff,0,lowI,101)
    require(h.shape(Sp)==(6188,101) and h.zero_matrix(Sp[170:]),
            "All6018-by101 high/low cross entries zero")
    S=Sp[:170]
    colindex={c:i for i,c in enumerate(cols)}
    heads=h.zeros(F,101,15)
    for i,key in enumerate(low36):
        heads[colindex[(len(key[2]),key)]][:11]=X[0][i][:]
    for j,key in enumerate(exact):
        heads[colindex[(0,key)]][11+j]=F.one
    require(h.zero_matrix(h.product(F,S,heads)),"All2550 original constant low head products")
    _,headmeta=w.exact_kernel(F,h,heads,cache,"complete-low-fifteen-heads",report)
    require(headmeta["rank"]==15,"Paid fifteen true constant low heads independent")
    Sprim,units=w.rational_rows(S)
    prof=cache.get("complete-low-unit-profile")
    if prof is None:
        prime,root={"plus":(19,5),"minus":(17,4),"e8":(17,5)}[params["field"]]
        profile_method="prescribed-residue-with-exact-unit-verification"
        try:
            rows,uc=residue_profile(S,prime,root)
        except AssertionError:
            rows,uc=[],[]
        if len(rows)!=86:
            rows,uc,_=h.bareiss_profile(F,Sprim,cache,"complete-low-exact-profile",report)
            profile_method="exact-number-field-fallback"
        require(len(rows)==len(uc)==86,"Original S has exact rank86")
        prof={"inputSHA256":F.matrix_hash(S),"rows":rows,"columns":uc,
              "method":profile_method,"rank":86}
        cache.put("complete-low-unit-profile",prof,True)
    else:
        require(prof["inputSHA256"]==F.matrix_hash(S) and prof["rank"]==86,
                "Same complete constant low matrix")
        rows,uc=prof["rows"],prof["columns"]
    U=h.submatrix(Sprim,rows,uc)
    fac=h.lu_factor(F,U,cache,"complete-low-original86-unit")
    em=parent.get("paid-low-exit-kernel")
    require(em["inputSHA256"]==F.matrix_hash(R) and em["rank"]==2,
            "Actual inherited two-exit map")
    exitcols=em["independentColumns"]
    require(len(exitcols)==2,"Exactly two original exit representatives")
    exitkernel=F.matrix_from_json(em["kernel"])
    require(h.shape(exitkernel)==(11,9) and h.zero_matrix(h.product(F,R,exitkernel)),
            "All nine original free low exit directions")
    pure_rows=actions.source_rows(0)
    pure_index={row:i for i,row in enumerate(pure_rows)}
    low_original_rows=[r for r in pure_rows if r[1]+r[2]<=1]
    require(len(low_original_rows)==51,"Exact original pure source row embedding")
    Rfull=h.zeros(F,170,11)
    for i,row in enumerate(low_original_rows):
        Rfull[pure_index[row]]=[oldunits[i]*x for x in R[i]]
    E=h.submatrix(Rfull,range(170),exitcols)
    exitrows=em["independentRows"]
    exitunit=h.submatrix(R,exitrows,exitcols)
    exitfac=h.lu_factor(F,exitunit,cache,"paid-two-exit-original-unit")
    exitspan=h.lu_solve(F,exitfac,h.submatrix(R,exitrows,range(11)))
    require(h.product(F,h.submatrix(R,range(51),exitcols),exitspan)==R
            and h.product(F,E,exitspan)==Rfull,
            "All eleven original exits exactly generated by the two selected columns")
    params["all1870OriginalExitSpanningCoordinatesVerified"]=True
    params["completeExitSpanningMapSHA256"]=F.matrix_hash(exitspan)
    cache.put("all-eleven-original-exit-span",{"map":F.matrix_json(exitspan),
       "originalExitSHA256":F.matrix_hash(Rfull),"allOriginalRowsVerified":True},True)
    B=w.join_columns(G,E)
    Bprim=[[x/units[i] for x in row] for i,row in enumerate(B)]
    key="nine-actual-original-unit-right-hand-sides"
    saved=cache.get(key)
    if saved is None:
        rhs=w.negate(h.submatrix(Bprim,rows,range(9)))
        sol=h.lu_solve(F,fac,rhs)
        require(h.product(F,U,sol)==rhs,"All774 original86-unit RHS coordinates")
        lift=h.zeros(F,101,9)
        for i,c in enumerate(uc):
            lift[c]=sol[i][:]
        residual=w.add_matrices(h.product(F,S,lift),B)
        require(h.zero_matrix(h.submatrix(residual,rows,range(9))),
                "All original selected constant unit rows zero")
        saved={"inputSHA256":F.matrix_hash(S),"rhsSHA256":F.matrix_hash(B),
             "lowLift":F.matrix_json(lift),"fullResidual":F.matrix_json(residual),
             "allOriginalUnitProductsVerified":True}
        cache.put(key,saved,True)
    else:
        require(saved["inputSHA256"]==F.matrix_hash(S) and
                saved["rhsSHA256"]==F.matrix_hash(B) and saved["allOriginalUnitProductsVerified"],
                "Exact same original nine RHS continuation")
        lift=F.matrix_from_json(saved["lowLift"])
        residual=F.matrix_from_json(saved["fullResidual"])
        require(w.add_matrices(h.product(F,S,lift),B)==residual,"Every original resumed residual")
    _,gm=w.exact_kernel(F,h,h.submatrix(residual,range(170),range(7)),
                       cache,"complete-seven-returns-modulo-low",report)
    require(gm["rank"]==7,"All seven original high returns independent modulo S")
    N,nm=w.exact_kernel(F,h,residual,cache,"complete-two-exits-modulo-original-image",report)
    b=nm["rank"]-7
    require(b in (0,1,2),"Actual complete first critical connection rank")
    t=2-b
    require(h.shape(N)==(9,t),"Complete residual kernel with no zero-head fibre")
    a=h.submatrix(N,range(7),range(t))
    c=h.submatrix(N,[7,8],range(t))
    if t:
        _,cm=w.exact_kernel(F,h,c,cache,"actual-exit-head-independence",report)
        require(cm["rank"]==t,"Every compatible quotient head independent")
    selector=h.zeros(F,11,2)
    for j,c0 in enumerate(exitcols):
        selector[c0][j]=F.one
    C=w.join_columns(exitkernel,h.product(F,selector,c))
    width=13+t
    lowcorr=h.product(F,lift,N)
    highone=h.product(F,Z1,a)
    hightwo=h.product(F,Z2,a)
    corrections=embed_low101(F,h,actions,cols,lowcorr)
    full=[]
    for k in range(order+1):
        section=w.embed_low(F,h,actions,low36,h.product(F,X[k],C))
        section[2]=h.zeros(F,450,9+t)
        if k==order:
            for r in (0,1):
                addition=corrections[r]
                if r==1:
                    addition=w.add_matrices(addition,highone)
                section[r]=w.add_matrices(section[r],w.join_columns(h.zeros(F,len(addition),9),addition))
            section[2]=w.join_columns(h.zeros(F,450,9),hightwo)
        for r in (0,1,2):
            extra=h.zeros(F,len(actions.target_columns(r)),4)
            if k==0 and r==0:
                ix={key:i for i,key in enumerate(actions.target_columns(0))}
                for j,key in enumerate(exact):
                    extra[ix[key]][j]=F.one
            section[r]=w.join_columns(section[r],extra)
        full.append(section)
    _,lm=w.exact_kernel(F,h,full[0][0]+full[0][1]+full[0][2],
                       cache,"complete-original-new-leading-heads",report)
    require(lm["rank"]==width and width==15-b,"All original new leading heads independent")
    hashes=[]
    for k in range(order+1):
        product=h.zeros(F,6188,width)
        for j in range(k+1):
            product=w.add_matrices(product,w.action(F,h,actions,coeff,j,full[k-j],width))
        require(h.zero_matrix(product),"Every original6188 source at order"+str(k))
        hashes.append(F.matrix_hash(product))
    sq=[actions.target_columns(2).index((0,0,(j,j))) for j in range(2,11)]
    readouts=[]
    for k in range(order+1):
        a=h.submatrix(full[k][2],sq,range(width))
        nonzero=[[i,j,F.encode(v)] for i,row in enumerate(a) for j,v in enumerate(row) if v]
        readouts.append({"order":k,"shape":[9,width],"sha256":F.matrix_hash(a),
                         "nonzeroEntries":len(nonzero),"nonzero":nonzero})
    lower=2*order+2-b
    require(lower<=setting["upper"],"Actual full positive length versus paid full upper")
    cochain=cache.put("complete-original-first-critical-exit",{
      "cochains":[{str(d):F.matrix_json(a) for d,a in section.items()} for section in full],
      "allOriginalProductsZero":True,"originalProductSHA256":hashes,
      "leadingMap":F.matrix_json(C),"fullLeadingRank":width,"connectionRank":b,
      "originalS":F.matrix_json(S),"originalHighReturn":F.matrix_json(G),
      "originalExitResidual":F.matrix_json(Rfull),"exactEarlierConnectionsZero":True,
      "constantRank4352Verified":True,"wholeHighRank4259Verified":True},True)
    params.update({"constantLowRank":86,"highReturnRankModuloLow":7,
      "fullOriginalConstantRank":4259+86+7,"originalFirstExitOrder":order,
      "completeConnectionRank":b,"completeLeadingHeads":width,
      "allEarlierFullConnectionsZero":True,"completeLowResidualRank":nm["rank"],
      "completeLowResidualShape":[170,9],"actualLowUnitProfile":prof,
      "allOriginal6188ProductsZero":True,"originalProductCoordinates":6188*width*(order+1),
      "fullLengthLowerBound":lower,"paidFullLengthUpperBound":setting["upper"],
      "fullLengthExact":2*order if b==2 else (lower if lower==setting["upper"] else None),
      "targetSquareReadouts":readouts,"completeCochainCheckpoint":cochain})

def main():
    ap=argparse.ArgumentParser()
    for name in PINS:
        ap.add_argument("--"+name.replace("_","-"),required=True)
    for name in ("weak-driver","cubic-helper","high-driver","parent-out","parent-receipt",
                 "high-out","high-receipt","high-receipt-sha","out"):
        ap.add_argument("--"+name,required=True)
    ap.add_argument("--high-receipt-bytes",type=int,required=True)
    ap.add_argument("--field",choices=tuple(PARENT_PINS),required=True)
    ap.add_argument("--remaining-seconds",type=float,default=300)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args()
    require(0<a.remaining_seconds<=1800 and 512<=a.memory_mib<=8192,"Explicit resources")
    for key,value in PINS.items():
        require(sha_file(getattr(a,key))==value,"Pinned original helper "+key)
    require(sha_file(a.weak_driver)==WEAK_SHA and sha_file(a.cubic_helper)==CUBIC_SHA
            and sha_file(a.high_driver)==Q7_SHA,"Pinned original actual sources")
    require(Path(a.out).resolve() not in (Path(a.parent_out).resolve(),Path(a.high_out).resolve()),
            "Both actual parents remain read only")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    w=module_at("critical_exit_weak_parent",a.weak_driver)
    q7=module_at("critical_exit_q7_parent",a.high_driver)
    cubic=module_at("critical_exit_prepare_helper",a.cubic_helper)
    parent=Parent(w,a.parent_out,a.parent_receipt,a.field)
    high,high_identity=read_high(a,q7)
    source_sha=sha_file(__file__)
    binding=hashlib.sha256(canonical({"format":FORMAT,"scriptSHA256":source_sha,
       "helpers":PINS,"weakSourceSHA256":WEAK_SHA,"cubicSHA256":CUBIC_SHA,
       "highSourceSHA256":Q7_SHA,"field":a.field,"weakParent":PARENT_PINS[a.field],
       "highParent":high_identity})).hexdigest()
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    cache=Cache(out/"checkpoints",binding)
    receipt=out/"critical-complete-first-exit-receipt.json"
    started=time.monotonic()
    result={"format":FORMAT,"status":"started","binding":binding,"scriptSHA256":source_sha,
      "parameters":{"field":a.field,"parent":PARENT_PINS[a.field],"highParent":high_identity,
      "helperSHA256":PINS,"remainingSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
      "allParentsReadOnly":True,"largeDataTemporaryOnly":True,"connectionRankNotPrespecified":True}}
    def save():
        result["elapsedSeconds"]=time.monotonic()-started
        result["parameters"]["checkpointManifest"]={"file":"checkpoints/manifest.json",
           "bytes":cache.path.stat().st_size,"sha256":sha_file(cache.path)}
        raw=canonical(result);require(len(raw)<90000,"Small complete-connection receipt")
        tmp=receipt.with_name(receipt.name+".tmp");tmp.write_bytes(raw);tmp.replace(receipt)
    def report(phase,step):
        result["parameters"]["currentPhase"]={"name":phase,"step":step};save()
    def stop(signum,frame):raise BudgetStop("Actual complete critical connection budget")
    signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    code=1
    try:
        m=w.load_module("critical_exit_original",a.generator)
        actions=w.load_module("critical_exit_actions",a.jet_actions)
        h=w.load_module("critical_exit_field",a.field_helper)
        setting=w.FIELDS[a.field];F=w.make_field(h,setting["polynomial"])
        compute(F,h,w,cubic,m,actions,parent,high,cache,report,result["parameters"],setting)
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
          "connectionRank":result["parameters"].get("completeConnectionRank")},sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    sys.exit(main())
