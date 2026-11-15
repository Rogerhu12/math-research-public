#!/usr/bin/env python3
"""Original infinity complete constant normal3/4/5 kernel, one fixed31 lower bound.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro; native rank fork from literature_audit.
Read the current, actually verified original P coefficient cache.  Do not
regenerate P jets or its Smith calculation.  Read the two true homogeneous
cubic columns from the paid fifth high-lift cache.  Retain all5100 original
normal2/3 source rows and all3762 normal3/4/5 target columns, including every
cross block.  Verify both Q columns on all original rows.  Row normalization
is applied only to this constant block, never to a jet or a forcing.
A single field31 rank may close the Q kernel dimension2.  No field kernel
is lifted, and no sixth connection is claimed in this constant task.
All large data remains temporary.
"""
import argparse
import gzip
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

GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
PROJECTION_SOURCE_SHA="dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79"
PROJECTION_RECEIPT_SHA="ea44027e462054b9fdb9c9101065faaba0b14dc5ab9b1a5602c06fecbb765207"
PROJECTION_BINDING="01ba6e6d1f1d0c0ae9ae22a319615887dce4c313d29c9ce1bde346445ae10766"
COEFFICIENT_BYTES=267400
COEFFICIENT_SHA="94cffcf53fe22e7693e4c22bd67b237fe9d65933a50571891647c378a4b98034"
FIFTH_RECEIPT_SHA="17361fc2f385bbc1ffe8b843d185d0c3acd2998276579d08e5d76e8233eaf036"
FIFTH_BINDING="ccacc20f5bf3e678c4b3fcab2090e25b84c72abb35440c9b0c8473fa007a8576"
FIFTH_MANIFEST_SHA="911bfc575782bd81aa69bf98e47efab546bb0d4dd164370d943aaaebda1b5e34"
HIGH_BYTES=15355
HIGH_SHA="d8dff9e38bad4a0a41a21679e5654609f36b7da36dbb84f996a0778bfa73eb50"
HIGH_MATRIX_SHA="4411183498cbdb63db83317b53436ac4deb4e374b517e22155254392cf2b3093"
NATIVE_SHA="cee59e862dc22bd5ade469177ce9e4541d2a6b4743ab811684a5e387a4402ba4"
PRIME=31
NR=5100
NC=3762
FORMAT="r150-infinity-complete-normal345-high-field31-v1"

def require(ok,message):
    if not ok:raise AssertionError(message)
def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def small_hash(x):return hashlib.sha256(canonical(x)).hexdigest()
def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return h.hexdigest()
def atomic_json(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_bytes(canonical(obj));os.replace(tmp,path)
def descriptor(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":file_sha(path),"temporaryOnly":True}
def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj);return obj
def remaining(a):
    r=a._deadline-time.monotonic()
    if r<=0:raise TimeoutError("Shared time exhausted at a complete boundary")
    return r
def check_descriptor(root,item):
    require(Path(item["file"]).name==item["file"],"Temporary basename")
    path=Path(root)/item["file"]
    require(path.stat().st_size==item["bytes"] and file_sha(path)==item["sha256"],
            "Actual temporary full bytes and SHA")
    return path
def paid_inputs(a,q,m,projection,fifth):
    root=Path(a.projection_out)/"temporary"
    manifest=root/"small-projection-checkpoints.json"
    require(file_sha(manifest)==projection["parameters"]["temporaryManifestSHA256"],
            "Actual completed P manifest")
    man=json.loads(manifest.read_bytes())
    require(man["binding"]==PROJECTION_BINDING and man["temporaryOnly"] is True,
            "Same actual P semantic binding")
    item=man["phases"]["original-projection-coefficients"]
    require(item["bytes"]==COEFFICIENT_BYTES and item["sha256"]==COEFFICIENT_SHA and
            item==projection["parameters"]["temporaryPhaseFiles"]["original-projection-coefficients"],
            "Actual P coefficient descriptor")
    path=check_descriptor(root,item)
    with gzip.open(path,"rt",encoding="utf-8") as f:obj=json.load(f)
    require(obj["format"]=="r150-infinity-small-projection-temporary-v1" and
            obj["binding"]==PROJECTION_BINDING and obj["domain"]=="Q" and
            obj["phase"]=="original-projection-coefficients" and obj["complete"] is True,
            "Actual original coefficient cache identity")
    coeff=q.coefficient_decode(obj["data"]["coefficients"])
    require(coeff["chart"]=="infinity" and coeff["maxOrder"]==11 and
            coeff["physical"]==projection["parameters"]["originalProjection"]["originalPhysicalCoefficientHashes"],
            "Same exact original natural-infinity coefficients")
    fp=Path(a.fifth_checkpoint_dir)
    require(file_sha(fp/"fifth-joint-high-low-checkpoint.json")==FIFTH_MANIFEST_SHA,
            "Actual fifth immutable manifest")
    fm=json.loads((fp/"fifth-joint-high-low-checkpoint.json").read_bytes())
    require(fm["binding"]==FIFTH_BINDING and fm["temporaryOnly"] is True,"Actual fifth binding")
    item=fm["phases"]["high-fifth-lifts"]
    require(item["bytes"]==HIGH_BYTES and item["sha256"]==HIGH_SHA and
            item["matrixSHA256"]==HIGH_MATRIX_SHA and
            item==fifth["parameters"]["checkpointPhases"]["high-fifth-lifts"],
            "Actual complete fifth high-lift descriptor")
    hp=check_descriptor(fp,item)
    with gzip.open(hp,"rt",encoding="utf-8") as f:h=json.load(f)
    require(h["format"]=="r150-infinity-fifth-shifted-incoming-temporary-v1" and
            h["binding"]==FIFTH_BINDING and h["phase"]=="high-fifth-lifts" and
            h["complete"] is True and h["shape"]==[999,11],
            "Actual999 by11 fifth high lifts")
    T=m.fmpq_mat([[m.fmpq(x) for x in r] for r in h["matrix"]])
    require(m.matrix_hash(T)==HIGH_MATRIX_SHA and h["metadata"]["all2295HighFifthLiftRowsVerified"] is True,
            "Actual canonical high-lift products")
    require(all(not T[i,j] for i in range(990,999) for j in range(2)),
            "Two selected columns have no new head: they are homogeneous")
    W=m.submatrix(T,range(990),range(2))
    require(W[164,0]==1 and W[164,1]==0 and W[494,0]==0 and W[494,1]==1,
            "True two homogeneous high sources have free I2")
    meta={"shape":[990,2],"embeddedShape":[3762,2],
          "matrixSHA256":m.matrix_hash(W),"freeOriginalCubicCoordinates":[164,494],
          "freeMinor":"1","normalFourFiveCandidateCoordinatesZero":True,
          "paidHighLiftFileSHA256":HIGH_SHA}
    return coeff,W,meta

def prepare(a,q,m,j,projection,fifth,binding,result):
    root=Path(a.checkpoint_dir);path=root/"prepared-complete-high.json"
    if path.exists():
        obj=json.loads(path.read_bytes())
        require(obj["binding"]==binding and obj["verified"] is True,"Same complete prepared high block")
        binary=check_descriptor(root,obj["input"])
        result["parameters"]["originalPreparation"]=obj["metadata"]
        result["parameters"]["originalInput"]=obj["input"]
        return binary,obj["metadata"]
    coeff,W,wmeta=paid_inputs(a,q,m,projection,fifth)
    require(all(not v for v in coeff["pure"][0]),"Actual original infinity F0 pure part zero")
    blocks={r:j.target_columns(r) for r in (3,4,5)}
    require([len(blocks[r]) for r in (3,4,5)]==[990,1485,1287],"All high target sectors")
    indices={r:{key:i for i,key in enumerate(blocks[r])} for r in (3,4,5)}
    offsets={3:0,4:990,5:2475}
    sources=j.source_rows(2)+j.source_rows(3)
    require(len(sources)==NR and len(j.source_rows(2))==2295,"All original5100 high source rows")
    columns=[(r,key) for r in (3,4,5) for key in blocks[r]]
    require(len(columns)==NC,"All3762 high target columns")
    original_hash=hashlib.sha256();primitive_hash=hashlib.sha256();scale_hash=hashlib.sha256()
    checked_products=0;checked_scalings=0;nnz=0;field_nnz=0
    maxbits=0;denp=0;contentp=0;zero_rows=0
    sector_counts=[[0,0,0],[0,0,0]]
    temporary=root/"complete-high-primitive-input.bin.tmp"
    with temporary.open("wb") as f:
        f.write(b"R15H4531");f.write(struct.pack("<3I",PRIME,NR,NC));f.write(binding.encode("ascii"))
        for row_index,row in enumerate(sources):
            if row_index%64==0:remaining(a)
            combined={}
            source_sector=0 if row_index<2295 else 1
            for r in (3,4,5):
                for c,v in j.sparse_row_terms(coeff,0,row,r,indices[r]):
                    col=offsets[r]+c
                    combined[col]=combined.get(col,m.ZERO)+v
            values=[(c,v) for c,v in sorted(combined.items()) if v]
            require(len(values)<=77,"Original quadratic polynomial support")
            for c,v in values:
                t=0 if c<990 else (1 if c<2475 else 2)
                sector_counts[source_sector][t]+=1
            for k in range(2):
                v=sum((v*W[c,k] for c,v in values if c<990),m.ZERO)
                require(not v,"All actual complete high Q candidate products")
                checked_products+=1
            den=1
            for _,v in values:
                qd=int(v.denom());den=den//gcd(den,qd)*qd
            ints0=[(c,int(v.numer())*(den//int(v.denom()))) for c,v in values]
            content=0
            for _,v in ints0:content=gcd(content,abs(v))
            content=content or 1
            ints=[(c,v//content) for c,v in ints0]
            scale=m.fmpq(den,content)
            require(all(m.fmpq(v)==scale*combined[c] for c,v in ints),
                    "One exact scale for each complete original rational row")
            checked_scalings+=1
            require(len(ints)==len(values),"No coefficient discarded before the field reduction")
            maxbits=max(maxbits,max((abs(v).bit_length() for _,v in ints),default=0))
            denp+=int(den%PRIME==0);contentp+=int(content%PRIME==0)
            zero_rows+=int(not ints);nnz+=len(ints)
            original_hash.update(canonical([[c,str(v)] for c,v in values])+b"\n")
            primitive_hash.update(canonical([[c,str(v)] for c,v in ints])+b"\n")
            scale_hash.update(canonical([str(den),str(content)])+b"\n")
            reduced=[(c,v%PRIME) for c,v in ints if v%PRIME]
            field_nnz+=len(reduced)
            f.write(struct.pack("<H",len(reduced)))
            for c,v in reduced:f.write(struct.pack("<HB",c,v))
    require(checked_products==10200 and checked_scalings==5100,"Every original product and whole-row scale")
    require(sector_counts[1][0]==0,"Original source-normal3 / target-normal3 constant block zero")
    digest=file_sha(temporary);binary=root/("complete-high-primitive-"+digest+".bin")
    if binary.exists():
        require(file_sha(binary)==digest,"Immutable prepared field input")
        temporary.unlink()
    else:os.replace(temporary,binary)
    wmeta.update({"all10200OriginalHighProductsVerified":True,"QRankUpperBound":3760})
    meta={"shape":[NR,NC],"sourceNormalDegrees":[2,3],"targetNormalDegrees":[3,4,5],
          "sourceSectorSizes":[2295,2805],"targetSectorSizes":[990,1485,1287],
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
          "noParameterJetGoodPrimeClaim":True,
          "originalConstantNonzeroEntries":nnz,"fieldNonzeroEntries":field_nnz,
          "originalZeroRows":zero_rows,"maximumPrimitiveCoefficientBits":maxbits,
          "rowsWithDenominatorDivisibleBy31":denp,"rowsWithClearedContentDivisibleBy31":contentp,
          "allRowScalesAre31Units":denp==0 and contentp==0,
          "primePredetermined":31,"rationalUpperCertificate":wmeta,
          "paidPSeriesAndSmithNotRecomputed":True}
    obj={"binding":binding,"verified":True,"input":descriptor(binary),"metadata":meta,"temporaryOnly":True}
    atomic_json(path,obj)
    result["parameters"]["originalPreparation"]=meta
    result["parameters"]["originalInput"]=obj["input"]
    return binary,meta

def build_native(a,binding,result):
    root=Path(a.checkpoint_dir);mp=root/"native-build.json"
    if mp.exists():
        old=json.loads(mp.read_bytes())
        require(old["binding"]==binding and old["sourceSHA256"]==NATIVE_SHA,"Same compiled native")
        binary=check_descriptor(root,old["binary"])
        result["parameters"]["nativeBuild"]=old
        return binary
    binary=root/("complete-high-native-"+NATIVE_SHA);log=root/"native-build-log.txt"
    with log.open("wb") as f:
        process=subprocess.run([a.cxx,"-O3","-std=c++17",str(Path(a.native_source).resolve()),"-o",str(binary)],
            stdout=f,stderr=subprocess.STDOUT,timeout=remaining(a),check=False)
    require(process.returncode==0,"Native compile failed: "+log.read_text(errors="replace")[-3000:])
    old={"binding":binding,"sourceSHA256":NATIVE_SHA,"binary":descriptor(binary),
         "compiler":a.cxx,"flags":["-O3","-std=c++17"],"log":descriptor(log),"temporaryOnly":True}
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
        if process.returncode==124:raise TimeoutError("Native fixed31 rank reached its actual deadline")
        require(process.returncode==0,"Native fixed31 rank failed: "+log.read_text(errors="replace")[-3000:])
    n=json.loads(rp.read_bytes())
    require(n["format"]=="r150-infinity-complete-high-constant-rank-field31-v1" and
            n["status"]=="completed" and n["binding"]==binding and n["prime"]==31 and
            n["originalSourceRows"]==NR and n["originalTargetCoordinates"]==NC,
            "Actual native completed original rank identity")
    for k in ("all5100OriginalSourceRowsRetained","all3762OriginalHighColumnsRetained",
              "allDependentOriginalRowsReducedToZero","independentOriginalPivotMinorVerified",
              "all961BitPlaneAdditionIdentitiesVerified","all30FieldInversesVerified",
              "primePredeterminedNoScan","noRationalKernelInferredFromFieldKernel"):
        require(n[k] is True,"Native exact gate "+k)
    require(n["rank"]+n["dependentOriginalRows"]==NR and n["rank"]+n["nullity"]==NC,
            "Complete native rank dimensions")
    dag=out/"complete-high-row-operations.bin";piv=out/"complete-high-normalized-pivots.bin"
    with dag.open("rb") as f:
        require(f.read(8)==b"R15HDG31" and struct.unpack("<3I",f.read(12))==(31,NR,NC)
                and f.read(64).decode("ascii")==binding,"Complete original row-operation identity")
    with piv.open("rb") as f:
        require(f.read(8)==b"R15HPV31" and
                struct.unpack("<5I",f.read(20))==(31,n["rank"],NC,5,(NC+63)//64)
                and f.read(64).decode("ascii")==binding,"Actual normalized-pivot identity")
    require(piv.stat().st_size==92+n["rank"]*(4+5*((NC+63)//64)*8),"All actual pivot rows retained")
    result["parameters"]["actualNativeRank"]=n
    items={p.name:descriptor(p) for p in (rp,dag,piv)}
    atomic_json(root/"native-completed-outputs.json",
                {"binding":binding,"verified":True,"outputs":items,"temporaryOnly":True})
    result["parameters"]["temporaryNativeOutputs"]=items
    return n

def main():
    p=argparse.ArgumentParser()
    for key in ("projection-consumer","generator","jet-actions","projection-receipt","projection-out",
                "fifth-receipt","fifth-checkpoint-dir","native-source","checkpoint-dir","out"):
        p.add_argument("--"+key,required=True)
    p.add_argument("--cxx",default="g++")
    p.add_argument("--remaining-seconds",type=float,default=60)
    p.add_argument("--memory-mib",type=int,default=2048)
    a=p.parse_args()
    require(0<a.remaining_seconds<=300 and 512<=a.memory_mib<=4096,"Finite resources")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    result={"format":FORMAT,"status":"started","parameters":{"selfSHA256":file_sha(__file__),
        "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
        "chart":"original natural infinity u=1/s","ancestorCachesReadOnly":True,
        "primePredeterminedNoScan":31,"allArraysTemporary":True,
        "noLargeRecomputableDataUploaded":True,"completeSixthConnectionNotComputed":True},
        "events":[]}
    try:
        pins=((a.projection_consumer,PROJECTION_SOURCE_SHA),(a.generator,GEN_SHA),(a.jet_actions,ACT_SHA),
              (a.projection_receipt,PROJECTION_RECEIPT_SHA),(a.fifth_receipt,FIFTH_RECEIPT_SHA),
              (a.native_source,NATIVE_SHA))
        for path,digest in pins:require(file_sha(path)==digest,"Pinned input "+path)
        require(Path(a.checkpoint_dir).resolve() not in
                (Path(a.projection_out).resolve(),Path(a.fifth_checkpoint_dir).resolve()),
                "Child checkpoint cannot overwrite an ancestor")
        Path(a.checkpoint_dir).mkdir(parents=True,exist_ok=True)
        projection=json.loads(Path(a.projection_receipt).read_bytes())["result"]
        fifth=json.loads(Path(a.fifth_receipt).read_bytes())["result"]
        require(projection["status"]=="completed" and
                projection["parameters"]["semanticBinding"]==PROJECTION_BINDING and
                projection["parameters"]["QProjectionSmith"]["positiveLength"]==61 and
                projection["parameters"]["QProjectionSmith"]["complete"] is True and
                projection["parameters"]["allOriginal6188PositiveAndRemainingJetProductsZero"] is True,
                "Actual completed original P state")
        require(fifth["status"]=="completed" and
                fifth["parameters"]["checkpointBinding"]==FIFTH_BINDING and
                fifth["parameters"]["fullFirstFiveRanks"]==[4,0,1,3,1],
                "Actual completed original fifth incoming")
        binding=small_hash({"format":FORMAT,"selfSHA256":file_sha(__file__),
            "inputSHA256":{"projectionConsumer":PROJECTION_SOURCE_SHA,"generator":GEN_SHA,
                "actions":ACT_SHA,"projectionReceipt":PROJECTION_RECEIPT_SHA,
                "fifthReceipt":FIFTH_RECEIPT_SHA,"native":NATIVE_SHA},
            "coefficientSHA256":COEFFICIENT_SHA,"twoHighSourcePackSHA256":HIGH_SHA,
            "prime":31,"shape":[5100,3762],"chart":"original natural infinity"})
        result["parameters"]["binding"]=binding
        result["parameters"]["inputSHA256"]={str(Path(x).name):y for x,y in pins}
        q=module_at("r150_infinity_high_projection_base",a.projection_consumer)
        m=module_at("r150_infinity_high_first",a.generator)
        j=module_at("r150_infinity_high_actions",a.jet_actions)
        data,meta=prepare(a,q,m,j,projection,fifth,binding,result)
        binary=build_native(a,binding,result)
        native=native_rank(a,binary,data,binding,result)
        r=native["rank"];require(0<=r<=3760,"Actual field lower versus true Q two-column upper")
        exact=(r==3760)
        result["parameters"]["conclusion"]={
            "completeHighQRankLowerBound":r,"completeHighQRankUpperBound":3760,
            "completeHighQRankExact":3760 if exact else None,
            "completeHighQKernelEqualsPaidTwoCubicColumns":exact,
            "allNormalFourFiveCoordinatesOfAnyHighKernelAreZero":exact,
            "noFieldKernelLiftedToQ":True,"noParameterJetGoodPrimeClaim":True,
            "fullSixthConnectionStillRequiresActualLowForcingSolve":True}
        result["status"]="completed"
    except (TimeoutError,subprocess.TimeoutExpired) as exc:
        result["status"]="prefix-completed";result["error"]=str(exc)
    except BaseException as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc)
        raise
    finally:
        result["elapsedSeconds"]=time.monotonic()-started
        raw=canonical(result);require(len(raw)<90000,"Small actual constant-high receipt")
        atomic_json(a.out,result)
        print(json.dumps({"status":result["status"],"receipt":a.out,"bytes":len(raw),
                          "sha256":hashlib.sha256(raw).hexdigest(),
                          "elapsedSeconds":result["elapsedSeconds"]}),flush=True)
if __name__=="__main__":main()
