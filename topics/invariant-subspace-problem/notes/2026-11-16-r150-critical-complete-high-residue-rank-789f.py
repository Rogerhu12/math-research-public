#!/usr/bin/env python3
"""Complete original critical high block: number-field upper / residue lower.

Astra-ISP-789f / literature_audit; AI-assisted with GPT-6 Astra Pro.
2026-11-16. Every original normal>=1 source and all complementary targets.
This is a constant-rank qualification only, not a local-jet or good-prime claim.
All large arrays, field row operations and normalized pivots remain temporary.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from math import gcd
from pathlib import Path
import resource
import signal
import struct
import subprocess
import sys
import time
from flint import fmpq

FORMAT="r150-critical-complete-high-residue-rank-v1"
WEAK_SHA="f211696b5cb789f054e259648a54be7a60f2d8c7c7772d410143bc0025025b1b"
NATIVE_SHA="bada5f20f24efd06ba9ca9a5f2bda16f1d935d42f89d32be08166a184a609fa7"
PINS={
 "generator":"2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186",
 "jet_actions":"2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332",
 "low_generator":"4d215c80fa40d5f3548fd604e4ed77c6317db44b5b80518a03cf15e2ceeffa2f",
 "field_helper":"54f88bdbd926d38fb7a78fdaa1128f6bae96617461e4d2d4e4064736f6cf842c"}
RESIDUES={"plus":{"prime":19,"root":5},"minus":{"prime":17,"root":4},
          "e8":{"prime":17,"root":5}}
NR=6018
NC=4266
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



def descriptor(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,
            "sha256":sha_file(path),"temporaryOnly":True}

def checked_file(root,item):
    require(Path(item["file"]).name==item["file"],"Local temporary basename")
    p=Path(root)/item["file"]
    require(p.stat().st_size==item["bytes"] and sha_file(p)==item["sha256"],
            "Complete temporary file identity")
    return p

def remaining(a):
    r=a.deadline-time.monotonic()
    if r<=0:
        raise BudgetStop("Shared complete-high budget exhausted")
    return r

def eval_integer(values,root,prime):
    y=0
    for v in reversed(values):
        y=(y*root+int(v))%prime
    return y

def original_dictionaries(actions):
    sources=sum((actions.source_rows(r) for r in (1,2,3)),[])
    require([len(actions.source_rows(r)) for r in (1,2,3)]==[918,2295,2805],
            "All original high source sectors")
    high={}
    high[1]=[key for key in actions.target_columns(1) if key[1]>=2]
    for r in (2,3,4,5):
        high[r]=actions.target_columns(r)
    low={0:actions.target_columns(0),
         1:[key for key in actions.target_columns(1) if key[1]<2]}
    require([len(high[r]) for r in range(1,6)]==[54,450,990,1485,1287],
            "Complete high complementary target sectors")
    require([len(low[r]) for r in (0,1)]==[20,81],
            "Complete remaining low101 target coordinates")
    columns=[(r,key) for r in range(1,6) for key in high[r]]
    low_columns=[(r,key) for r in (0,1) for key in low[r]]
    require(len(sources)==NR and len(columns)==NC and
            len(columns)+len(low_columns)==4367,"Exact original partition")
    high_indices={}
    offset=0
    for r in range(1,6):
        high_indices[r]={key:offset+i for i,key in enumerate(high[r])}
        offset+=len(high[r])
    low_indices={r:{key:i for i,key in enumerate(low[r])} for r in (0,1)}
    return sources,columns,low_columns,high_indices,low_indices

def prepare(a,F,h,w,m,actions,parent,cache,binding,report):
    existing=cache.get("prepared-original-complete-high")
    if existing is not None:
        require(existing["verified"] and existing["binding"]==binding,
                "Same completed original high preparation")
        path=checked_file(cache.root,existing["input"])
        return path,existing["metadata"]
    _,poly,poly_meta=w.decode_polynomial_model(
        m,parent.get("original-polynomial-model"))
    coeff=w.field_coefficients(F,poly,0)
    qmeta=w.physical_quadratic_constant(F,h,m,coeff)
    require(qmeta==parent.result["parameters"]["quadraticPhysicalChecks"],
            "Same actual original physical quadratic coefficients")
    paid=parent.get("weak-quadratic-original-columns")
    W=F.matrix_from_json(paid["highColumns"])
    require(h.shape(W)==(450,2),"Two completed original Q(alpha) high columns")
    require(paid["all6137OriginalHighAndOtherRowsZero"] and
            paid["all6188OriginalProductsComputed"],"Actual parent full-source certificate")
    product=w.action(F,h,actions,coeff,0,{2:W},2)
    require(product==F.matrix_from_json(paid["originalProduct"]),
            "All12376 actual original products equal the paid columns")
    require(h.zero_matrix(product[170:]),"All6018 actual high rows vanish")
    i0=next(i for i in range(450) if W[i][0])
    i1=next(i for i in range(450)
            if F.mul(W[i0][0],W[i][1])-F.mul(W[i0][1],W[i][0]))
    minor=F.mul(W[i0][0],W[i1][1])-F.mul(W[i0][1],W[i1][0])
    require(bool(minor),"Independent two-column number-field certificate")
    Z=h.zeros(F,54,2)+W+h.zeros(F,990+1485+1287,2)
    require(h.shape(Z)==(NC,2),"All4266 candidate coordinates retained")
    zrecord=cache.put("original-two-column-high-upper-certificate",{
      "columns":F.matrix_json(Z),"originalProduct":F.matrix_json(product),
      "matrixSHA256":F.matrix_hash(Z),"independenceRows":[54+i0,54+i1],
      "independenceMinor":F.encode(minor),"all6188OriginalProductsMatched":True,
      "all6018HighProductsZero":True},True)
    sources,columns,low_columns,indices,low_indices=original_dictionaries(actions)
    residue=RESIDUES[a.field]
    p,s=residue["prime"],residue["root"]
    polynomial=w.FIELDS[a.field]["polynomial"]
    derivative=[i*polynomial[i] for i in range(1,len(polynomial))]
    require(polynomial[-1]%p and eval_integer(polynomial,s,p)==0 and
            eval_integer(derivative,s,p)!=0,"Prescribed simple root of original field polynomial")
    require((-2*s*s*(s-2)*(s+6))%p!=0,"Prescribed residue is noncontact")
    J3=m.polynomial_power_kernel(m.fmpq_mat(m.ORIGINAL_K),3)
    jd=J3.det()
    require(int(jd.denom())%p and int(jd.numer())%p,
            "Original J3 determinant is a residue unit")
    original_hash=hashlib.sha256()
    primitive_hash=hashlib.sha256()
    scale_hash=hashlib.sha256()
    eval_hash=hashlib.sha256()
    original_nnz=0;field_nnz=0;scalars=0;maxbits=0
    denominator_p=0;content_p=0;zero_rows=0;checked=0
    sector_counts=[[0]*5 for _ in range(3)]
    temporary=cache.root/"original-complete-high-field-input.bin.tmp"
    with temporary.open("wb") as f:
        f.write(b"R15CH601")
        f.write(struct.pack("<3I",p,NR,NC))
        f.write(binding.encode("ascii"))
        for ri,row in enumerate(sources):
            if ri%64==0:
                remaining(a)
            # The low101 column block is ZERO on these exact original rows.
            for r in (0,1):
                require(all(not v for _,v in
                        actions.sparse_row_terms(coeff,0,row,r,low_indices[r])),
                        "All original high-source / low101 cross entries zero")
            combined={}
            for r in range(1,6):
                for col,value in actions.sparse_row_terms(coeff,0,row,r,indices[r]):
                    combined[col]=combined.get(col,F.zero)+value
            values=[(col,value) for col,value in sorted(combined.items()) if value]
            require(len(values)<=77,"Original quadratic polynomial row support")
            source_sector=0 if ri<918 else (1 if ri<3213 else 2)
            for col,value in values:
                target_sector=next(k for k,bound in enumerate((54,504,1494,2979,4266))
                                   if col<bound)
                sector_counts[source_sector][target_sector]+=1
            for k in range(2):
                z=sum((F.mul(value,W[col-54][k])
                       for col,value in values
                       if 54<=col<504 and W[col-54][k]),F.zero)
                require(not z,"Original whole high-row number-field product")
                checked+=1
            canonical_values=[(col,value.coeffs()) for col,value in values]
            den=1
            for _,poly_coeffs in canonical_values:
                for value in poly_coeffs:
                    d=int(value.denom())
                    den=den//gcd(den,d)*d
            integer_values=[(col,[int(x.numer())*(den//int(x.denom()))
                                 for x in poly_coeffs])
                            for col,poly_coeffs in canonical_values]
            content=0
            for _,poly_coeffs in integer_values:
                for value in poly_coeffs:
                    content=gcd(content,abs(value))
            content=content or 1
            integer_values=[(col,[x//content for x in poly_coeffs])
                            for col,poly_coeffs in integer_values]
            scale=fmpq(den,content)
            for (col,raw),(icol,integers) in zip(canonical_values,integer_values):
                require(col==icol and len(raw)==len(integers) and
                        all(fmpq(x)==scale*y for x,y in zip(integers,raw)),
                        "One exact rational scalar for the entire polynomial row")
                scalars+=len(integers)
                maxbits=max(maxbits,max((abs(x).bit_length() for x in integers),default=0))
            require(len(values)==len(integer_values),
                    "No original nonzero entry lost before residue specialization")
            reduced=[(col,eval_integer(v,s,p)) for col,v in integer_values]
            reduced=[(col,value) for col,value in reduced if value]
            original_hash.update(canonical([[col,F.encode(value)] for col,value in values])+b"\n")
            primitive_hash.update(canonical([[col,[str(x) for x in v]]
                                              for col,v in integer_values])+b"\n")
            scale_hash.update(canonical([str(den),str(content)])+b"\n")
            eval_hash.update(canonical(reduced)+b"\n")
            original_nnz+=len(values);field_nnz+=len(reduced);zero_rows+=not values
            denominator_p+=den%p==0;content_p+=content%p==0
            f.write(struct.pack("<H",len(reduced)))
            for col,value in reduced:
                f.write(struct.pack("<HB",col,value))
    require(checked==12036,"All original6018 by two high products")
    digest=sha_file(temporary)
    binary=cache.root/("original-complete-high-"+digest+".bin")
    if binary.exists():
        require(sha_file(binary)==digest,"Immutable original input collision")
        temporary.unlink()
    else:
        temporary.replace(binary)
    metadata={
      "shape":[NR,NC],"originalLowComplement":[170,101],
      "sourceSectorSizes":[918,2295,2805],
      "targetSectorSizes":[54,450,990,1485,1287],
      "sourceOrder":"source_rows(1),source_rows(2),source_rows(3)",
      "targetOrder":"one-normal with d-exponent>=2, then all normal2,3,4,5",
      "sourceOrderSHA256":hashlib.sha256(canonical(sources)).hexdigest(),
      "targetOrderSHA256":hashlib.sha256(canonical(columns)).hexdigest(),
      "low101OrderSHA256":hashlib.sha256(canonical(low_columns)).hexdigest(),
      "all6018OriginalRowsRetained":True,"all4266OriginalColumnsRetained":True,
      "allHighLow101CrossEntriesZero":True,"allCrossHighSectorTermsRetained":True,
      "originalPhysicalChecks":qmeta,"originalPolynomialPhysicalIdentity":poly_meta,
      "originalNumberFieldRowsSHA256":original_hash.hexdigest(),
      "primitiveIntegerPolynomialRowsSHA256":primitive_hash.hexdigest(),
      "wholeRationalRowScalesSHA256":scale_hash.hexdigest(),
      "evaluatedResidueRowsSHA256":eval_hash.hexdigest(),
      "all6018WholeRowScalingsVerified":True,"verifiedRationalCoefficientCount":scalars,
      "prime":p,"residueRoot":s,"minimalPolynomialAscending":polynomial,
      "residueRootSimple":True,"J3DeterminantResidueUnit":True,
      "normalizationOnlyOnConstantBlock":True,
      "noParameterJetFlatnessOrGoodPrimeClaim":True,
      "originalNonzeroEntries":original_nnz,"fieldNonzeroEntries":field_nnz,
      "originalZeroRows":zero_rows,"maximumPrimitiveIntegerBits":maxbits,
      "rowsWithClearedDenominatorDivisibleByPrime":denominator_p,
      "rowsWithIntegerContentDivisibleByPrime":content_p,
      "sectorNonzeroCounts":sector_counts,
      "numberFieldRankUpperBound":4264,"twoOriginalNumberFieldKernelColumns":2,
      "all12376OriginalParentProductsMatched":True,
      "all12036CompleteHighProductsZero":True,"independenceRows":[54+i0,54+i1],
      "independenceMinor":F.encode(minor),"candidateCheckpoint":zrecord}
    cache.put("prepared-original-complete-high",{"binding":binding,"verified":True,
              "input":descriptor(binary),"metadata":metadata},True)
    return binary,metadata

def build_native(a,cache,binding):
    p=RESIDUES[a.field]["prime"]
    saved=cache.get("native-build")
    if saved is not None:
        require(saved["binding"]==binding and saved["sourceSHA256"]==NATIVE_SHA
                and saved["prime"]==p,"Same native build and prescribed prime")
        return checked_file(cache.root,saved["binary"]),saved
    binary=cache.root/("critical-complete-high-"+str(p)+"-"+NATIVE_SHA)
    log=cache.root/"native-build-log.txt"
    flags=["-O3","-std=c++17","-DR150_CRITICAL_PRIME="+str(p)]
    with log.open("wb") as f:
        proc=subprocess.run([a.cxx]+flags+[str(Path(a.native_source).resolve()),
                            "-o",str(binary)],stdout=f,stderr=subprocess.STDOUT,
                            timeout=remaining(a),check=False)
    require(proc.returncode==0,"Native compile failed; see complete temporary log")
    saved={"binding":binding,"sourceSHA256":NATIVE_SHA,"prime":p,
           "compiler":a.cxx,"flags":flags,"binary":descriptor(binary),
           "log":descriptor(log)}
    cache.put("native-build",saved,True)
    return binary,saved

def run_native(a,binary,input_path,cache,binding):
    old=cache.get("native-completed-original-high")
    out=cache.root/"native-result"
    out.mkdir(exist_ok=True)
    if old is not None:
        require(old["binding"]==binding,"Same completed native binding")
        for item in old["outputs"].values():
            checked_file(out,item)
        return old["result"],old["outputs"]
    rp=out/"native-complete-high-rank-receipt.json"
    if not rp.exists():
        log=cache.root/"native-rank-log.txt"
        with log.open("wb") as f:
            proc=subprocess.run([str(binary),str(input_path),str(out),
                       str(remaining(a))],stdout=f,stderr=subprocess.STDOUT,
                       timeout=remaining(a),check=False)
        if proc.returncode==124:
            raise BudgetStop("Native complete high rank reached its actual budget")
        require(proc.returncode==0,"Native complete rank failed; see temporary log")
    n=json.loads(rp.read_text())
    p=RESIDUES[a.field]["prime"]
    require(n["format"]==FORMAT and n["status"]=="completed" and
            n["binding"]==binding and n["prime"]==p and
            n["originalSourceRows"]==NR and n["originalTargetCoordinates"]==NC,
            "Actual completed full native identity")
    for k in ("all6018OriginalSourceRowsRetained","all4266OriginalHighColumnsRetained",
              "allDependentOriginalRowsReducedToZero","independentOriginalPivotMinorVerified",
              "allPrimeSquaredBitPlaneAdditionIdentitiesVerified",
              "allNonzeroFieldInversesVerified","primePredeterminedNoScan",
              "noRationalKernelInferredFromFieldKernel"):
        require(n[k] is True,"Actual native gate "+k)
    require(n["rank"]+n["dependentOriginalRows"]==NR and
            n["rank"]+n["nullity"]==NC,"Every original field row and column counted")
    dag=out/"complete-high-row-operations.bin"
    piv=out/"complete-high-normalized-pivots.bin"
    nw=(NC+63)//64
    with dag.open("rb") as f:
        require(f.read(8)==b"R15CHDG1" and
                struct.unpack("<3I",f.read(12))==(p,NR,NC) and
                f.read(64).decode()==binding,"Original row-operation identity")
    with piv.open("rb") as f:
        require(f.read(8)==b"R15CHPV1" and
                struct.unpack("<5I",f.read(20))==(p,n["rank"],NC,5,nw) and
                f.read(64).decode()==binding,"All normalized original-pivot identity")
    require(piv.stat().st_size==92+n["rank"]*(4+5*nw*8),
            "Complete normalized pivot output size")
    outputs={p.name:descriptor(p) for p in (rp,dag,piv)}
    cache.put("native-completed-original-high",{"binding":binding,"result":n,
                                               "outputs":outputs},True)
    return n,outputs

def main():
    ap=argparse.ArgumentParser()
    for name in PINS:
        ap.add_argument("--"+name.replace("_","-"),required=True)
    for name in ("weak-driver","native-source","field","parent-out","parent-receipt","out"):
        ap.add_argument("--"+name,required=True,**({"choices":tuple(RESIDUES)} if name=="field" else {}))
    ap.add_argument("--cxx",default="g++")
    ap.add_argument("--remaining-seconds",type=float,default=180)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args()
    require(0<a.remaining_seconds<=1800 and 512<=a.memory_mib<=8192,"Explicit resources")
    for name,digest in PINS.items():
        require(sha_file(getattr(a,name))==digest,"Pinned helper "+name)
    require(sha_file(a.weak_driver)==WEAK_SHA and sha_file(a.native_source)==NATIVE_SHA,
            "Exact original parent and independent complete-high native")
    require(Path(a.out).resolve()!=Path(a.parent_out).resolve(),"Parent directory remains read only")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    w=module_at("critical_complete_high_parent",a.weak_driver)
    parent=Parent(w,a.parent_out,a.parent_receipt,a.field)
    source_sha=sha_file(__file__)
    binding=hashlib.sha256(canonical({"format":FORMAT,"sourceSHA256":source_sha,
       "helperSHA256":PINS,"nativeSHA256":NATIVE_SHA,"parentSourceSHA256":WEAK_SHA,
       "parent":PARENT_PINS[a.field],"field":a.field,"residue":RESIDUES[a.field],
       "shape":[NR,NC]})).hexdigest()
    root=Path(a.out);root.mkdir(parents=True,exist_ok=True)
    cache=Cache(root/"checkpoints",binding)
    receipt=root/"critical-complete-high-residue-rank-receipt.json"
    started=time.monotonic();a.deadline=started+a.remaining_seconds
    result={"format":FORMAT,"status":"started","binding":binding,"scriptSHA256":source_sha,
      "parameters":{"field":a.field,"residue":RESIDUES[a.field],"parent":PARENT_PINS[a.field],
        "helperSHA256":PINS,"nativeSHA256":NATIVE_SHA,"remainingSeconds":a.remaining_seconds,
        "memoryMiB":a.memory_mib,"originalEquations":17,"originalTotalSources":6188,
        "originalTotalTargets":4367,"completeHighShape":[NR,NC],
        "completeLowComplementShape":[170,101],"parentIsReadOnly":True,
        "rankNotPrespecified":True,"noFieldKernelLiftedToNumberField":True,
        "noNewParameterConnectionClaimed":True,"largeDataTemporaryOnly":True}}
    def save():
        result["elapsedSeconds"]=time.monotonic()-started
        result["parameters"]["checkpointManifest"]={"file":"checkpoints/manifest.json",
          "bytes":cache.path.stat().st_size,"sha256":sha_file(cache.path)}
        raw=canonical(result);require(len(raw)<90000,"Small complete-high receipt")
        tmp=receipt.with_name(receipt.name+".tmp");tmp.write_bytes(raw);tmp.replace(receipt)
    def report(phase,step):
        result["parameters"]["currentPhase"]={"name":phase,"step":step};save()
    def stop(signum,frame):
        raise BudgetStop("Shared complete-high budget exhausted")
    signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    code=1
    try:
        m=w.load_module("critical_high_original_generator",a.generator)
        actions=w.load_module("critical_high_original_actions",a.jet_actions)
        h=w.load_module("critical_high_original_field",a.field_helper)
        F=w.make_field(h,w.FIELDS[a.field]["polynomial"])
        input_path,meta=prepare(a,F,h,w,m,actions,parent,cache,binding,report)
        result["parameters"]["originalPreparation"]=meta;save()
        binary,bmeta=build_native(a,cache,binding)
        result["parameters"]["nativeBuild"]=bmeta;save()
        n,outputs=run_native(a,binary,input_path,cache,binding)
        rank=n["rank"]
        require(0<=rank<=4264,"Actual field lower bound versus two true number-field kernels")
        exact=rank==4264
        result["parameters"].update({"actualNativeRank":n,"temporaryNativeOutputs":outputs,
           "conclusion":{"numberFieldRankLowerBound":rank,"numberFieldRankUpperBound":4264,
              "numberFieldHighKernelDimensionLowerBound":2,
              "numberFieldHighKernelDimensionUpperBound":NC-rank,
              "completeHighKernelEqualsPaidTwo":exact,
              "completeNumberFieldRankExact":4264 if exact else None,
              "fullCriticalJetStillRequiresTheActualCompleteLowSystem":True}})
        result["status"]="completed";code=0
    except (BudgetStop,subprocess.TimeoutExpired) as exc:
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
          "rank":result["parameters"].get("actualNativeRank",{}).get("rank")},
          sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    sys.exit(main())
