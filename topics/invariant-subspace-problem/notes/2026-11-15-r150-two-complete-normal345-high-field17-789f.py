#!/usr/bin/env python3
"""Original s=2 complete high constant block: fixed17 lower / two true Q kernels.

Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
The block has ALL5100 normal2/3 source rows and ALL3762 normal3/4/5
target columns.  Cross terms between normal3/4/5 are never discarded.
Only this constant rational matrix is row-primitive normalized; this does
not claim a good17 parameter-jet model or transport any field kernel to Q.
The already paid two Q kernels are read from the same-job immutable cache
and rechecked on every actual original row.  A single native fixed17 rank
provides only a Q lower bound unless it equals the verified upper3760.
No old592/583 unit, incompatible RHS, or full rational RREF is recomputed.
All large working data remains temporary; only the small receipt is public.
"""
import argparse
from copy import copy
import hashlib
import importlib.util
import json
from math import gcd
import os
from pathlib import Path
import resource
import struct
import subprocess
import sys
import time

BASE_SHA="8f55c5b5f0db2a7dd9b0b042e00cd506fd6e38698b9dc264a602e3dc8ccb510b"
GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
PAID_SHA="950aecf40605fbd3156c223d7e18d4ee1821940386872f59d88cc24f756ed1a2"
PAID_BINDING="3de42bed91acf562cce951f7c79f9e4f871cbd31ec82e7430d03bb97198f970f"
PAID_SOURCE_SHA="d4ff08a474ef3abe6c7ee08bea7829e6fa3d52eb2e04c71469b18b2ea2c27bb8"
NATIVE_SHA="ac89263afb07205d418d8dbb6c967b48e287f2a1ff572b4fb20f1704b78e1ba4"
W_SHA="00653919cd7eadeb0e5df0531fdf33c1bbc3864643fe5b588ccba77bc4303924"
PRIME=17
NR=5100
NC=3762

def require(ok,message):
    if not ok:raise AssertionError(message)
def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),
                      ensure_ascii=True).encode("ascii")
def small_hash(x):return hashlib.sha256(canonical(x)).hexdigest()
def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        while True:
            b=f.read(1024*1024)
            if not b:break
            h.update(b)
    return h.hexdigest()
def atomic_json(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_bytes(canonical(obj));os.replace(tmp,path)
def descriptor(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,
            "sha256":file_sha(path),"temporaryOnly":True}
def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj);return obj
def remaining(a):
    r=a._deadline-time.monotonic()
    if r<=0:raise TimeoutError("Shared time exhausted")
    return r
def check_descriptor(root,item):
    require(Path(item["file"]).name==item["file"],"Temporary basename")
    path=Path(root)/item["file"]
    require(path.stat().st_size==item["bytes"] and
            file_sha(path)==item["sha256"],"Actual temporary byte identity")
    return path
def paid_kernel(d,m,a,pp,result):
    old=copy(a);old.checkpoint_dir=a.paid_checkpoint_dir
    loaded=d.load_matrix(m,old,PAID_BINDING,"full-cubic-high-kernel",result)
    require(loaded is not None,"Paid complete cubic kernel exists")
    W,meta,verified=loaded
    actual=d.manifest(old,PAID_BINDING)["phases"]["full-cubic-high-kernel"]
    item=pp["checkpointPhases"]["full-cubic-high-kernel"]
    require(verified and actual["verified"] and item["verified"],
            "Only verified actual old phase is reused")
    for k in ("shape","matrixSHA256","bytes","fileSHA256"):
        require(actual[k]==item[k],"Paid receipt versus same-job phase "+k)
    require((W.nrows(),W.ncols())==(990,2) and m.matrix_hash(W)==W_SHA,
            "All actual paid two high columns")
    i0=next(i for i in range(990) if W[i,0])
    i1=next(i for i in range(990)
            if W[i0,0]*W[i,1]-W[i0,1]*W[i,0])
    determinant=W[i0,0]*W[i1,1]-W[i0,1]*W[i1,0]
    require(determinant,"Two original rational columns are independent")
    return W,{"originalCandidateShape":[990,2],"embeddedShape":[3762,2],
              "originalCandidateSHA256":W_SHA,"independenceRows":[i0,i1],
              "independenceMinor":str(determinant),
              "normalFourAndFiveCandidateCoordinatesAllZero":True,
              "sourcePhaseFileSHA256":actual["fileSHA256"]}
def prepare(a,d,m,j,pp,binding,result):
    root=Path(a.checkpoint_dir);path=root/"prepared-complete-high.json"
    if path.exists():
        obj=json.loads(path.read_bytes())
        require(obj["binding"]==binding and obj["verified"] is True,
                "Same completed high input preparation")
        binary=check_descriptor(root,obj["input"])
        result["parameters"]["originalPreparation"]=obj["metadata"]
        result["parameters"]["originalInput"]=obj["input"]
        return binary,obj["metadata"]
    W,wmeta=paid_kernel(d,m,a,pp,result)
    coeff=d.original_at_two(m,j,2)
    require(coeff["physical"]==pp["physicalCoefficientSHA256"],
            "Same original physical matrices0,1,2 as actual one-RHS source")
    require(all(not v for v in coeff["pure"][0]),
            "Original F0 pure part is actually zero at s=2")
    blocks={r:j.target_columns(r) for r in (3,4,5)}
    require([len(blocks[r]) for r in (3,4,5)]==[990,1485,1287],
            "All original high target sectors")
    indices={r:{key:i for i,key in enumerate(blocks[r])} for r in (3,4,5)}
    offsets={3:0,4:990,5:2475}
    sources=j.source_rows(2)+j.source_rows(3)
    require(len(sources)==NR and len(j.source_rows(2))==2295,
            "All original normal2/3 source rows")
    columns=[(r,key) for r in (3,4,5) for key in blocks[r]]
    require(len(columns)==NC,"Complete3762 target coordinates")
    original_hash=hashlib.sha256();primitive_hash=hashlib.sha256()
    scale_hash=hashlib.sha256()
    checked_products=0;checked_scalings=0;nnz=0;field_nnz=0
    maxbits=0;den17=0;content17=0;zero_rows=0
    sector_counts=[[0,0,0],[0,0,0]]
    temporary=root/"complete-high-primitive-input.bin.tmp"
    with temporary.open("wb") as f:
        f.write(b"R15H4517");f.write(struct.pack("<3I",PRIME,NR,NC))
        f.write(binding.encode("ascii"))
        for row_index,row in enumerate(sources):
            if row_index%64==0:remaining(a)
            combined={}
            source_sector=0 if row_index<2295 else 1
            for r in (3,4,5):
                for c,value in j.sparse_row_terms(coeff,0,row,r,indices[r]):
                    col=offsets[r]+c
                    combined[col]=combined.get(col,m.ZERO)+value
            values=[(c,v) for c,v in sorted(combined.items()) if v]
            require(len(values)<=77,"Actual original polynomial support")
            for c,v in values:
                t=0 if c<990 else (1 if c<2475 else 2)
                sector_counts[source_sector][t]+=1
            # Recheck original rational equations BEFORE any row scaling.
            for k in range(2):
                value=sum((v*W[c,k] for c,v in values if c<990),m.ZERO)
                require(not value,"Actual complete high Q candidate product")
                checked_products+=1
            den=1
            for _,v in values:
                q=int(v.denom());den=den//gcd(den,q)*q
            integer_values=[(c,int(v.numer())*(den//int(v.denom())))
                            for c,v in values]
            content=0
            for _,v in integer_values:content=gcd(content,abs(v))
            content=content or 1
            ints=[(c,v//content) for c,v in integer_values]
            scale=m.fmpq(den,content)
            require(all(m.fmpq(v)==scale*combined[c] for c,v in ints),
                    "One exact nonzero rational scale for the ENTIRE original row")
            checked_scalings+=1
            require(len(ints)==len(values),"No original nonzero coefficient lost before mod17")
            maxbits=max(maxbits,max((abs(v).bit_length() for _,v in ints),default=0))
            den17+=int(den%17==0);content17+=int(content%17==0)
            zero_rows+=int(not ints);nnz+=len(ints)
            original_hash.update(canonical([[c,str(v)] for c,v in values])+b"\n")
            primitive_hash.update(canonical([[c,str(v)] for c,v in ints])+b"\n")
            scale_hash.update(canonical([str(den),str(content)])+b"\n")
            reduced=[(c,v%PRIME) for c,v in ints if v%PRIME]
            field_nnz+=len(reduced)
            f.write(struct.pack("<H",len(reduced)))
            for c,v in reduced:f.write(struct.pack("<HB",c,v))
    require(checked_products==10200 and checked_scalings==5100,
            "Complete original products and all original row identities")
    require(sector_counts[1][0]==0,"At s=2 source-normal3 pure block is actually zero")
    digest=file_sha(temporary);binary=root/("complete-high-primitive-"+digest+".bin")
    if binary.exists():
        require(file_sha(binary)==digest,"Immutable high input collision")
        temporary.unlink()
    else:os.replace(temporary,binary)
    wmeta.update({"all10200OriginalProductsVerified":True,
                 "rankUpperBoundOverQ":3760,"independentRationalKernelColumns":2})
    meta={"shape":[NR,NC],"sourceNormalDegrees":[2,3],"targetNormalDegrees":[3,4,5],
          "sourceSectorSizes":[2295,2805],"targetSectorSizes":[990,1485,1287],
          "sourceOrder":"source_rows(2) followed by source_rows(3), original equation order",
          "targetOrder":"target_columns(3), target_columns(4), target_columns(5)",
          "sourceOrderSHA256":small_hash(sources),"targetOrderSHA256":small_hash(columns),
          "physicalCoefficientSHA256":coeff["physical"],
          "all5100OriginalSourceRowsRetained":True,"all3762OriginalColumnsRetained":True,
          "allCrossSectorTermsRetained":True,"sectorNonzeroCounts":sector_counts,
          "originalRationalRowsSHA256":original_hash.hexdigest(),
          "primitiveIntegerRowsSHA256":primitive_hash.hexdigest(),
          "exactWholeRowScalesSHA256":scale_hash.hexdigest(),
          "all5100WholeRationalRowScalingsVerified":True,
          "normalizationUsesOnlyConstantBlockNotAnyRHS":True,
          "normalizationNeverAppliedToParameterJets":True,
          "noGoodPrimeOrConnectionFlatnessClaim":True,
          "originalConstantNonzeroEntries":nnz,"fieldNonzeroEntries":field_nnz,
          "originalZeroRows":zero_rows,"maximumPrimitiveCoefficientBits":maxbits,
          "rowsWithDenominatorDivisibleBy17":den17,
          "rowsWithClearedContentDivisibleBy17":content17,
          "primePredetermined":17,"rationalUpperCertificate":wmeta}
    obj={"binding":binding,"verified":True,"input":descriptor(binary),
         "metadata":meta,"temporaryOnly":True}
    atomic_json(path,obj)
    result["parameters"]["originalPreparation"]=meta
    result["parameters"]["originalInput"]=obj["input"]
    return binary,meta
def build_native(a,binding,result):
    root=Path(a.checkpoint_dir);mp=root/"native-build.json"
    if mp.exists():
        old=json.loads(mp.read_bytes())
        require(old["binding"]==binding and old["sourceSHA256"]==NATIVE_SHA,
                "Same compiled native source and binding")
        binary=check_descriptor(root,old["binary"])
        result["parameters"]["nativeBuild"]=old
        return binary
    binary=root/("complete-high-native-"+NATIVE_SHA)
    log=root/"native-build-log.txt"
    with log.open("wb") as f:
        process=subprocess.run([a.cxx,"-O3","-std=c++17",
            str(Path(a.native_source).resolve()),"-o",str(binary)],
            stdout=f,stderr=subprocess.STDOUT,timeout=remaining(a),check=False)
    require(process.returncode==0,"Native compile failed; see temporary build log")
    old={"binding":binding,"sourceSHA256":NATIVE_SHA,"binary":descriptor(binary),
         "compiler":a.cxx,"flags":["-O3","-std=c++17"],"log":descriptor(log),
         "temporaryOnly":True}
    atomic_json(mp,old);result["parameters"]["nativeBuild"]=old
    return binary
def native_rank(a,binary,input_path,binding,result):
    root=Path(a.checkpoint_dir);out=root/"native-result";out.mkdir(exist_ok=True)
    rp=out/"native-complete-high-rank-receipt.json"
    if not rp.exists():
        log=root/"native-field-rank-log.txt"
        with log.open("wb") as f:
            process=subprocess.run([str(binary),str(input_path),str(out),str(remaining(a))],
                stdout=f,stderr=subprocess.STDOUT,timeout=remaining(a),check=False)
        if process.returncode==124:raise TimeoutError("Native fixed17 rank reached actual deadline")
        require(process.returncode==0,"Native fixed17 rank failed; see temporary log")
    n=json.loads(rp.read_bytes())
    require(n["format"]=="r150-two-complete-high-constant-rank-field17-v1"
            and n["status"]=="completed" and n["binding"]==binding
            and n["prime"]==17 and n["originalSourceRows"]==NR
            and n["originalTargetCoordinates"]==NC,"Actual native completed rank identity")
    for k in ("all5100OriginalSourceRowsRetained","all3762OriginalHighColumnsRetained",
              "allDependentOriginalRowsReducedToZero","independentOriginalPivotMinorVerified",
              "all289BitPlaneAdditionIdentitiesVerified","all16FieldInversesVerified",
              "primePredeterminedNoScan","noRationalKernelInferredFromFieldKernel"):
        require(n[k] is True,"Actual native gate "+k)
    require(n["rank"]+n["dependentOriginalRows"]==NR and
            n["rank"]+n["nullity"]==NC,"Complete native rank dimensions")
    dag=out/"complete-high-row-operations.bin"
    piv=out/"complete-high-normalized-pivots.bin"
    with dag.open("rb") as f:
        require(f.read(8)==b"R15HDG17" and struct.unpack("<3I",f.read(12))==(17,NR,NC)
                and f.read(64).decode("ascii")==binding,"Complete row-operation identity")
    with piv.open("rb") as f:
        require(f.read(8)==b"R15HPV17" and
                struct.unpack("<5I",f.read(20))==(17,n["rank"],NC,5,(NC+63)//64)
                and f.read(64).decode("ascii")==binding,"Actual normalized-pivot identity")
    require(piv.stat().st_size==92+n["rank"]*(4+5*((NC+63)//64)*8),
            "All normalized pivot rows retained")
    result["parameters"]["actualNativeRank"]=n
    items={p.name:descriptor(p) for p in (rp,dag,piv)}
    atomic_json(root/"native-completed-outputs.json",
                {"binding":binding,"verified":True,"outputs":items,"temporaryOnly":True})
    result["parameters"]["temporaryNativeOutputs"]=items
    return n
def main():
    p=argparse.ArgumentParser()
    for key in ("paid-probe","generator","jet-actions","paid-receipt",
                "paid-checkpoint-dir","native-source","checkpoint-dir","out"):
        p.add_argument("--"+key,required=True)
    p.add_argument("--cxx",default="g++")
    p.add_argument("--remaining-seconds",type=float,default=180)
    p.add_argument("--memory-mib",type=int,default=2048)
    a=p.parse_args()
    require(0<a.remaining_seconds<=600 and 512<=a.memory_mib<=8192,"Explicit shared resources")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    pins=((a.paid_probe,BASE_SHA),(a.generator,GEN_SHA),(a.jet_actions,ACT_SHA),
          (a.paid_receipt,PAID_SHA),(a.native_source,NATIVE_SHA))
    for path,digest in pins:require(file_sha(path)==digest,"Pinned source or actual receipt "+path)
    require(Path(a.checkpoint_dir).resolve()!=Path(a.paid_checkpoint_dir).resolve(),
            "Ancestor cache is read-only; use a distinct child directory")
    Path(a.checkpoint_dir).mkdir(parents=True,exist_ok=True)
    outer=json.loads(Path(a.paid_receipt).read_bytes());pp=outer["result"]["parameters"]
    require(outer["result"]["status"]=="completed" and outer["exitCode"]==0
            and pp["binding"]==PAID_BINDING and pp["selfSHA256"]==PAID_SOURCE_SHA,
            "Same actual completed restricted second calculation")
    require(pp["conclusion"]["normalAtMostThreeSecondHeadDimensionExact"]==14 and
            pp["actualOneRHS"]["constantRank"]==592 and
            pp["one-second-actualCompleteSchurKernel"]["rank"]==593 and
            pp["completeHighHomogeneous"]["kernelDimension"]==2,
            "Strict paid normal<=3 result and two real high columns")
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    binding=small_hash({"format":"r150-two-complete-normal345-high-field17-v1",
        "selfSHA256":file_sha(__file__),"nativeSHA256":NATIVE_SHA,
        "paidReceiptSHA256":PAID_SHA,"paidBinding":PAID_BINDING,
        "baseSHA256":BASE_SHA,"generatorSHA256":GEN_SHA,"actionsSHA256":ACT_SHA,
        "prime":17,"sourceNormalDegrees":[2,3],"targetNormalDegrees":[3,4,5],
        "shape":[5100,3762]})
    result={"format":"r150-two-complete-normal345-high-field17-v1","status":"started",
        "parameters":{"binding":binding,"selfSHA256":file_sha(__file__),
        "inputSHA256":{"paidProbe":BASE_SHA,"generator":GEN_SHA,"jetActions":ACT_SHA,
                      "paidReceipt":PAID_SHA,"native":NATIVE_SHA},
        "paidBinding":PAID_BINDING,"sharedSeconds":a.remaining_seconds,
        "memoryMiB":a.memory_mib,"ancestorCacheReadOnly":True,
        "primePredeterminedNoScan":17,"noOldUnitOrRHSSolveRepeated":True,
        "allMatricesTemporary":True,"noLargeRecomputableDataUploaded":True}}
    try:
        d=module_at("r150_complete_high_paid_base",a.paid_probe)
        m=module_at("r150_complete_high_generator",a.generator)
        j=module_at("r150_complete_high_actions",a.jet_actions)
        data,meta=prepare(a,d,m,j,pp,binding,result)
        binary=build_native(a,binding,result)
        native=native_rank(a,binary,data,binding,result)
        rank=native["rank"]
        require(0<=rank<=3760,"Field lower bound versus two independently verified Q kernels")
        exact=(rank==3760)
        result["parameters"]["conclusion"]={
            "completeHighRationalRankLowerBound":rank,
            "completeHighRationalRankUpperBound":3760,
            "completeHighRationalRankExact":3760 if exact else None,
            "completeHighQKernelEqualsTheTwoEmbeddedCubicColumns":exact,
            "noHigherNormalCorrectionCanChangePaidLowImage":exact,
            "completeCharacteristicZeroSecondRankExact":1 if exact else None,
            "completeCharacteristicZeroSecondRankInterval":[1,1] if exact else [0,1],
            "completeSecondHeadDimensionExact":14 if exact else None,
            "h0LocalMembershipNotDecided":True,
            "noClaimThat17IsAGoodParameterJetPrime":True,
            "noFiniteFieldKernelLiftedToQ":True}
        result["status"]="completed"
    except (TimeoutError,subprocess.TimeoutExpired) as exc:
        result["status"]="prefix-completed";result["error"]=str(exc)
    except BaseException as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc);raise
    finally:
        result["elapsedSeconds"]=time.monotonic()-started
        raw=canonical(result);require(len(raw)<90000,"Small complete-high receipt")
        atomic_json(a.out,result)
        print(json.dumps({"status":result["status"],"receipt":a.out,"bytes":len(raw),
            "sha256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"]}),flush=True)
if __name__=="__main__":main()
