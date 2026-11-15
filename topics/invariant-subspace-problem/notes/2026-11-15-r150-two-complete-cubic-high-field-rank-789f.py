#!/usr/bin/env python3
"""Original s=2 complete normal-three high block: field lower / true Q upper.

Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
The two true rational cubic columns are verified on ALL5100 high-source rows.
Exactly one predetermined prime11 rank is taken after exact row normalization.
A lower rank remains only a lower bound; no finite-field kernel is lifted.
No constant-unit solve, prior RHS solve, or rational990-column RREF is run.
"""
import argparse
from copy import copy
import gzip
import hashlib
import importlib.util
import json
from math import gcd
import os
from pathlib import Path
import resource
import signal
import sys
import time
from flint import nmod_mat

BASE_SHA="8f55c5b5f0db2a7dd9b0b042e00cd506fd6e38698b9dc264a602e3dc8ccb510b"
COUPLED_SHA="459538fc066f2df2372752c1a32ba33b6f2abe8f1ecd0ac44787cefd44214628"
PAID_SHA="2342b75a4c4c57015157e8df8c19d7ae617fe4a1863ffd7b24abad3211b113a6"
PAID_BINDING="ef9b747b9ad8c6b0413fb61b23e402df4c3ca14b13ad2ab568f7f8d1f048a03b"
PAID_MANIFEST_SHA="74771ab772fe3ec392d2b5cbc237542480853a36b4274808530a107f5255283f"
GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
PRIME=11

def require(ok,message):
    if not ok:raise AssertionError(message)
def file_sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m
    spec.loader.exec_module(m);return m
def immutable_json(d,a,binding,name,obj):
    """Payload is immutable before a small manifest pointer is replaced."""
    value={"binding":binding,"phase":name,"payload":obj,"temporaryOnly":True}
    raw=d.canonical_bytes(value);logical=hashlib.sha256(raw).hexdigest()
    root=Path(a.checkpoint_dir);root.mkdir(parents=True,exist_ok=True)
    path=root/(name+"-"+logical+".json.gz")
    if not path.exists():
        temporary=path.with_name(path.name+".tmp")
        with temporary.open("wb") as f:
            with gzip.GzipFile(filename="",mode="wb",fileobj=f,mtime=0,
                               compresslevel=1) as z:z.write(raw)
        os.replace(temporary,path)
    item={"file":path.name,"bytes":path.stat().st_size,"sha256":file_sha(path),
          "payloadSHA256":logical,"binding":binding}
    mp=root/"field-proof-manifest.json"
    old=json.loads(mp.read_bytes()) if mp.exists() else {"binding":binding,"phases":{}}
    require(old["binding"]==binding,"Same field-proof binding")
    old["phases"][name]=item;d.atomic_json(mp,old)
    return item

def run(d,c,m,j,a,old_a,binding,pp,result):
    coeff=d.original_at_two(m,j,2)
    require(coeff["physical"]==pp["physicalCoefficientSHA256"],
            "All original coefficient matrices agree with paid parameter2")
    L,_=c.paid_phase(d,m,old_a,"constant-heads",pp)
    W0,W1,wmeta=c.tangent_cubic(d,m,j,a,old_a,binding,coeff,L,pp,result)
    cols=j.target_columns(3);ix={key:i for i,key in enumerate(cols)}
    require(len(cols)==990 and W0.nrows()==W1.nrows()==990,
            "Complete six tangent slices of the cubic-normal target")
    # Independence is exact over Q and uses a nonzero pure/tangent minor.
    i0=next(i for i,key in enumerate(cols) if key[0]+key[1]==0 and W0[i,0])
    i1=next(i for i,key in enumerate(cols) if key[0]+key[1]==1 and W1[i,0])
    determinant=W0[i0,0]*W1[i1,0]-W0[i1,0]*W1[i0,0]
    require(determinant and not W0[i1,0],"Two true independent rational high columns")
    rows=j.source_rows(2);high3=j.source_rows(3)
    require(len(rows)==2295 and len(high3)==2805,"All original high sources")
    original=[];primitive=[];scales=[];maxbits=0;original_count=0
    for row in rows:
        d.guard(a,"all original H3 rows and exact field normalization",0)
        combined={}
        for col,value in j.sparse_row_terms(coeff,0,row,3,ix):
            combined[col]=combined.get(col,m.fmpq(0))+value
        values=[(col,value) for col,value in sorted(combined.items()) if value]
        # Full original rational products, never a modular-kernel claim.
        for W in (W0,W1):
            product=sum((value*W[col,0] for col,value in values),m.fmpq(0))
            require(not product,"A true cubic candidate failed an original normal2 source")
            original_count+=1
        denominator=1
        for _,value in values:
            q=int(value.denom());denominator=denominator//gcd(denominator,q)*q
        numerators=[(col,int(value.numer())*(denominator//int(value.denom())))
                    for col,value in values]
        content=0
        for _,value in numerators:content=gcd(content,abs(value))
        content=content or 1
        ints=[(col,value//content) for col,value in numerators]
        scale=m.fmpq(denominator,content)
        require(all(m.fmpq(value)==scale*combined[col] for col,value in ints),
                "Every original sparse row scaling identity")
        maxbits=max(maxbits,max((abs(value).bit_length() for _,value in ints),default=0))
        original.append([[col,str(value)] for col,value in values])
        primitive.append([[col,str(value)] for col,value in ints])
        scales.append([str(denominator),str(content)])
    for row in high3:
        terms=list(j.sparse_row_terms(coeff,0,row,3,ix))
        # Original F0 pure=0 at2; these are retained rather than dropped by guess.
        require(not terms,"Every original normal3 source row is actually zero")
        for W in (W0,W1):
            require(not sum((value*W[col,0] for col,value in terms),m.fmpq(0)),
                    "Original highest-source product")
            original_count+=1
    require(original_count==10200,"Both candidates checked on all5100 original rows")
    inputs={"shape":[2295,990],"originalSparseRows":original,
            "primitiveIntegerSparseRows":primitive,"rowScales":scales,
            "sourceRows":[[eq,ca,db,list(mon)] for eq,ca,db,mon in rows],
            "targetColumns":[[ca,db,list(mon)] for ca,db,mon in cols],
            "normal3SourceRowsActuallyZero":2805,
            "coefficientSHA256":coeff["physical"],"prime":PRIME,
            "trueRationalCandidateHashes":[m.matrix_hash(W0),m.matrix_hash(W1)]}
    item=immutable_json(d,a,binding,"verified-complete-H3-input",inputs)
    result["parameters"]["actualInputCheckpoint"]=item
    result["parameters"]["rationalUpperCertificate"]={
        "rankUpperBound":988,"twoIndependentQColumns":True,
        "independenceRows":[i0,i1],"exactMinor":str(determinant),
        "candidateSHA256":[m.matrix_hash(W0),m.matrix_hash(W1)],
        "all10200OriginalProductsVerified":True,
        "all5100HighSourcesRetained":True,"finiteFieldKernelNeverUsedAsRational":True}
    del original,scales,inputs
    d.guard(a,"one predetermined exact finite-field rank",1)
    A=nmod_mat(2295,990,[0]*(2295*990),PRIME)
    for i,row in enumerate(primitive):
        for col,value in row:A[i,col]=int(value)%PRIME
    del primitive
    started=time.monotonic()
    R,rank=A.rref()
    seconds=time.monotonic()-started
    require(0<=rank<=988,"Field lower bound cannot exceed the verified Q upper bound")
    pivots=[]
    for i in range(rank):
        pivot=next(k for k in range(990) if R[i,k])
        require(R[i,pivot]==1,"Actual field RREF pivot")
        pivots.append(pivot)
    require(pivots==sorted(set(pivots)),"Distinct ordered actual field pivots")
    # The certificate of a positive result is Q upper plus field lower, not
    # identification of a field kernel with the original rational candidates.
    rank_identity={"prime":PRIME,"rank":rank,"shape":[2295,990],
                   "pivotColumns":pivots,"exactRowInputPayloadSHA256":item["payloadSHA256"]}
    ritem=immutable_json(d,a,binding,"completed-field-rank",rank_identity)
    result["parameters"]["fieldRank"]={
        "prime":PRIME,"shape":[2295,990],"rank":rank,"nativeSeconds":seconds,
        "rowPrimitiveNormalizationExact":True,"maxPrimitiveCoefficientBits":maxbits,
        "pivotColumnsSHA256":d.small_hash(pivots),"checkpoint":ritem,
        "primeWasPredeterminedNoScan":True,
        "thisIsOnlyACharacteristicZeroRankLowerBound":True}
    result["parameters"]["conclusion"]={
        "rationalRankLowerBound":rank,"rationalRankUpperBound":988,
        "rationalRankExactly988":rank==988,
        "completeNormalThreeHighKernelEqualsTheTwoTrueCandidates":rank==988,
        "completeNormalThreeHighKernelDimensionIfExact":2 if rank==988 else None,
        "normalFourAndFiveCorrectionsNotCovered":True,
        "noFullFirstConnectionOrTargetMembershipClaim":True,
        "noNewOriginalPrime31ModuleClaim":True}
    result["parameters"]["physicalCoefficientSHA256"]=coeff["physical"]

def main():
    p=argparse.ArgumentParser()
    for key in ("paid-probe","coupled-cubic-source","paid-receipt",
                "paid-checkpoint-dir","generator","jet-actions","checkpoint-dir","out"):
        p.add_argument("--"+key,required=True)
    p.add_argument("--remaining-seconds",type=float,default=60)
    p.add_argument("--memory-mib",type=int,default=2048)
    a=p.parse_args()
    require(0<a.remaining_seconds<=180 and 512<=a.memory_mib<=8192,"Actual resource bounds")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    for path,digest in ((a.paid_probe,BASE_SHA),(a.coupled_cubic_source,COUPLED_SHA),
                        (a.paid_receipt,PAID_SHA),(a.generator,GEN_SHA),(a.jet_actions,ACT_SHA)):
        require(file_sha(path)==digest,"Pinned original input "+path)
    require(Path(a.checkpoint_dir).resolve()!=Path(a.paid_checkpoint_dir).resolve(),
            "Read-only paid cache, independent child cache")
    outer=json.loads(Path(a.paid_receipt).read_bytes());pp=outer["result"]["parameters"]
    require(outer["result"]["status"]=="completed" and pp["binding"]==PAID_BINDING,
            "Actual completed pure-cubic ancestor")
    mp=Path(a.paid_checkpoint_dir)/"manifest.json"
    require(mp.stat().st_size==16411 and file_sha(mp)==PAID_MANIFEST_SHA,
            "Same verified immutable paid cache")
    d=module_at("r150_two_field_paid_base",a.paid_probe)
    c=module_at("r150_two_field_actual_coupled_source",a.coupled_cubic_source)
    m=module_at("r150_two_field_original_generator",a.generator)
    j=module_at("r150_two_field_original_actions",a.jet_actions)
    old_a=copy(a);old_a.checkpoint_dir=a.paid_checkpoint_dir
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    binding=d.small_hash({"format":"r150-two-complete-cubic-field-rank-input-v1",
        "selfSHA256":file_sha(__file__),"base":BASE_SHA,"coupled":COUPLED_SHA,
        "paidReceipt":PAID_SHA,"paidManifest":PAID_MANIFEST_SHA,
        "paidBinding":PAID_BINDING,"generator":GEN_SHA,"actions":ACT_SHA,
        "prime":PRIME,"allOriginalHighSources":5100,"shape":[2295,990]})
    result={"format":"r150-two-complete-cubic-high-field-rank-v1",
        "status":"started","parameters":{"binding":binding,"selfSHA256":file_sha(__file__),
        "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
        "inputSHA256":{"paidProbe":BASE_SHA,"coupledSource":COUPLED_SHA,
                      "paidReceipt":PAID_SHA,"paidManifest":PAID_MANIFEST_SHA,
                      "generator":GEN_SHA,"jetActions":ACT_SHA},
        "noLargeRecomputableDataUploaded":True,"allMatricesTemporary":True,
        "ancestorCacheReadOnly":True,"noOldUnitOrRHSSolveRepeated":True}}
    def alarm(_s,_f):raise d.SafeStop("Actual shared field-profile budget exhausted")
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        run(d,c,m,j,a,old_a,binding,pp,result);result["status"]="completed"
    except d.SafeStop as exc:
        result["status"]="prefix-completed";result["error"]=str(exc)
    except BaseException as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc);raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        result["elapsedSeconds"]=time.monotonic()-started
        d.compact_metadata(result);raw=d.canonical_bytes(result)
        require(len(raw)<90000,"Compact field-proof receipt")
        d.atomic_json(a.out,result)
        print(json.dumps({"status":result["status"],"receipt":a.out,"bytes":len(raw),
            "sha256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"]}),flush=True)

if __name__=="__main__":main()
