#!/usr/bin/env python3
"""Complete ORIGINAL s=2 first connection at the single good prime11.

Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
All6188 original source rows and all4367 target coordinates are retained.
The bit-plane native eliminates only constant columns, transports22 actual
RHS, and returns finite-field cochains verified on every original row.
The characteristic-zero upper bound7 uses the already verified15 rational
first heads.  No new finite-field cochain is claimed to be a rational lift.
No primitive row-content division is used anywhere in the parameter jet.
Large working arrays remain temporary inside this job.
"""
import argparse
import hashlib
import importlib.util
import json
from itertools import combinations_with_replacement
from pathlib import Path
import os
import resource
import struct
import subprocess
import sys
import time

GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
BASE_SHA="8f55c5b5f0db2a7dd9b0b042e00cd506fd6e38698b9dc264a602e3dc8ccb510b"
CONST_SHA="5d83b8784ea4e1d2b99f9ccd8881dcf6f2abe4241586219a3b459541c10d6272"
PAID_FIRST_SHA="2a75b4dba0b1e28902bc3a441ec7ce03a7e7fbdf46abfa5c138f4f7ab29b269a"
NATIVE_SHA="f2e5bf564781eb7dabce1a9c7c277389af65410b2f91adee996fc4274fa7df76"
J3_DET=23366320238786911411830138211362846399922176000
P=11

def require(ok,message):
    if not ok:raise AssertionError(message)
def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),
                      ensure_ascii=True).encode("ascii")
def small_hash(value):return hashlib.sha256(canonical(value)).hexdigest()
def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        while True:
            b=f.read(1024*1024)
            if not b:break
            h.update(b)
    return h.hexdigest()
def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m
    spec.loader.exec_module(m);return m
def atomic_json(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_bytes(canonical(obj));os.replace(tmp,path)
def remaining(a):
    value=a._deadline-time.monotonic()
    if value<=0:raise TimeoutError("Shared time budget exhausted")
    return value
def descriptor(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,
            "sha256":file_sha(path),"temporaryOnly":True}
def modq(value):
    n=int(value.numer());d=int(value.denom())
    require(d%P,"Original rational coefficient has a nonunit denominator at11")
    return (n%P)*pow(d%P,-1,P)%P
def polynomial(coeff,k,eq,m):
    out={}
    def add(mon,value):
        if value:out[tuple(sorted(mon))]=out.get(tuple(sorted(mon)),m.ZERO)+value
    add((1,1),coeff["pure"][k][eq])
    for var in range(2,11):
        add((var,),coeff["linear"][var][0][k][eq])
        add((0,var),coeff["linear"][var][1][k][eq])
        add((1,var),coeff["linear"][var][2][k][eq])
    for pair,value in coeff["quadratic"].items():add(pair,value[k][eq])
    return [(mon,value) for mon,value in sorted(out.items()) if value]
def normal_key_to_monomial(key):
    a,b,normal=key
    return (0,)*a+(1,)*b+tuple(normal)
def write_prepared_input(a,m,j,d,receipt,paid,binding,result):
    root=Path(a.checkpoint_dir)
    oldpath=root/"prepared-original-input.json"
    if oldpath.exists():
        old=json.loads(oldpath.read_bytes())
        require(old["binding"]==binding,"Prepared original input binding")
        path=root/old["input"]["file"]
        require(path.stat().st_size==old["input"]["bytes"] and
                file_sha(path)==old["input"]["sha256"],"Prepared original input identity")
        require(old["verified"] is True,"Prepared exact original products")
        result["parameters"]["originalPreparation"]=old["metadata"]
        result["parameters"]["originalInput"]=old["input"]
        return path,old["metadata"]
    coeff=d.original_at_two(m,j,2)
    require(coeff["physical"]==paid["physicalCoefficientSHA256"],
            "All original parameter coefficient matrices match the paid rational first jets")
    K=m.fmpq_mat(m.ORIGINAL_K);J3=m.polynomial_power_kernel(K,3);det=J3.det()
    require(int(det.denom())==1 and int(det.numer())==J3_DET and J3_DET%11==4,
            "Original J3 determinant is the same11 unit")
    targets=[mon for deg in range(5,0,-1)
             for mon in combinations_with_replacement(range(11),deg)]
    sources=[(eq,mon) for deg in range(4) for eq in range(17)
             for mon in combinations_with_replacement(range(11),deg)]
    require(len(targets)==4367 and len(sources)==6188,"Complete original monomial dimensions")
    target_index={mon:i for i,mon in enumerate(targets)}
    pcols=j.target_columns(0);ncols=j.target_columns(1)
    require(len(pcols)==20 and len(ncols)==135,"Complete constant projection sectors")
    pk=receipt["projectionKernel"]
    require(pk["free"]==[8,26] and len(pk["kernels"])==2 and
            all(len(v)==135 for v in pk["kernels"]),"Pinned exact two constant normal columns")
    kernels=[[int(x) for x in v] for v in pk["kernels"]]
    lam={}
    for col,key in enumerate(pcols):lam[target_index[normal_key_to_monomial(key)]]=[(col,1)]
    for i,key in enumerate(ncols):
        entries=[(20+c,kernels[c][i]) for c in range(2) if kernels[c][i]]
        if entries:lam[target_index[normal_key_to_monomial(key)]]=entries
    free=[target_index[normal_key_to_monomial(key)] for key in pcols]
    free += [target_index[normal_key_to_monomial(ncols[i])] for i in pk["free"]]
    free_block=[[dict(lam.get(row,[])).get(c,0)%11 for c in range(22)] for row in free]
    require(all(free_block[i][k]==0 for i in range(22) for k in range(22) if i!=k)
            and all(free_block[i][i] for i in range(22)),"Original22 constant heads have11-unit free block")
    require([free_block[20][20],free_block[21][21]]==[5,5],
            "Original two integer normal columns retain the paid11 normalization")
    poly=[[polynomial(coeff,k,eq,m) for eq in range(17)] for k in range(3)]
    maxnum=maxden=0
    for layer in poly:
        for equation in layer:
            for mon,value in equation:
                require(1<=len(mon)<=2,"Original degree<=2 with no constant term")
                modq(value)
                maxnum=max(maxnum,abs(int(value.numer())).bit_length())
                maxden=max(maxden,int(value.denom()).bit_length())
    equations_identity=small_hash([[[[list(mon),str(v)] for mon,v in equation]
                                   for equation in layer] for layer in poly])
    temporary=root/"original-field-input.bin.tmp"
    exact_a_hash=hashlib.sha256();exact_c_hash=hashlib.sha256()
    constant_products=0;nnz=0
    with temporary.open("wb") as f:
        f.write(b"R150FJ11");f.write(struct.pack("<4I",11,6188,4367,22))
        f.write(binding.encode("ascii"))
        for row_index,(eq,mult) in enumerate(sources):
            if row_index%128==0:remaining(a)
            actual0={}
            for mon,value in poly[0][eq]:
                col=target_index[tuple(sorted(mon+mult))]
                actual0[col]=actual0.get(col,m.ZERO)+value
            actual0={col:v for col,v in actual0.items() if v}
            tests=[m.ZERO]*22
            for col,value in actual0.items():
                for h,v in lam.get(col,[]):tests[h]+=value*v
            require(all(not v for v in tests),"A0^T Lambda exact rational identity on an original source")
            constant_products+=22
            rhs=[m.ZERO]*22
            for mon,value in poly[1][eq]:
                col=target_index[tuple(sorted(mon+mult))]
                for h,v in lam.get(col,[]):rhs[h]+=value*v
            exact_a_hash.update(canonical([[col,str(v)] for col,v in sorted(actual0.items())])+b"\n")
            exact_c_hash.update(canonical([str(v) for v in rhs])+b"\n")
            reduced=[(col,modq(v)) for col,v in sorted(actual0.items()) if modq(v)]
            require(len(reduced)<=77,"Original sparse polynomial row support")
            f.write(struct.pack("<H",len(reduced)))
            for col,v in reduced:f.write(struct.pack("<HB",col,v))
            f.write(bytes(modq(v) for v in rhs));nnz+=len(reduced)
        field_lambda=bytearray(4367*22)
        for row,entries in lam.items():
            for h,v in entries:field_lambda[row*22+h]=v%11
        f.write(field_lambda)
        f.write(struct.pack("<22H",*free))
    require(constant_products==136136,"All6188 times22 exact constant identities")
    sha=file_sha(temporary);path=root/("original-field-input-"+sha+".bin")
    if path.exists():
        require(file_sha(path)==sha,"Immutable original input collision")
        temporary.unlink()
    else:os.replace(temporary,path)
    metadata={
        "originalSourceRows":6188,"originalTargetCoordinates":4367,
        "sourceOrder":"total degree0..3, equation0..16, sorted multiplier tuples",
        "targetOrder":"total degree5..1, sorted variable tuples",
        "sourceOrderSHA256":small_hash(sources),"targetOrderSHA256":small_hash(targets),
        "originalAll17PolynomialJetsSHA256":equations_identity,
        "physicalCoefficientSHA256":coeff["physical"],
        "originalA0RationalRowSHA256":exact_a_hash.hexdigest(),
        "originalA1TransposeLambdaRationalRowSHA256":exact_c_hash.hexdigest(),
        "allParameterDenominatorsUnitsAt11":True,
        "noPrimitiveOrRowContentDivision":True,
        "J3Determinant":str(J3_DET),"J3DeterminantModulo11":4,
        "constantNormalFreeRows":[8,26],"constantNormalFreeBlockModulo11":[[5,0],[0,5]],
        "constantHeadFreeBlockRankModulo11":22,
        "all136136OriginalConstantProductCoordinatesZero":True,
        "constantKernelSupportAtMostOneNormal":True,
        "fieldConstantNonzeroEntries":nnz,
        "maximumOriginalCoefficientNumeratorBits":maxnum,
        "maximumOriginalCoefficientDenominatorBits":maxden,
        "nineSquareTargetIndices":[target_index[(v,v)] for v in range(2,11)],
        "constantFreeTargetCoordinates":free
    }
    item=descriptor(path)
    atomic_json(oldpath,{"binding":binding,"verified":True,"input":item,
                        "metadata":metadata,"temporaryOnly":True})
    result["parameters"]["originalPreparation"]=metadata
    result["parameters"]["originalInput"]=item
    return path,metadata

def compiled_native(a,binding,result):
    root=Path(a.checkpoint_dir);mp=root/"native-build.json"
    if mp.exists():
        old=json.loads(mp.read_bytes())
        path=root/old["binary"]["file"]
        require(old["binding"]==binding and old["sourceSHA256"]==NATIVE_SHA,
                "Native build binding")
        require(path.stat().st_size==old["binary"]["bytes"] and
                file_sha(path)==old["binary"]["sha256"],"Native binary bytes")
        result["parameters"]["nativeBuild"]=old
        return path
    output=root/("first-connection-native-"+NATIVE_SHA)
    log=root/"native-build-log.txt"
    command=[a.cxx,"-O3","-std=c++17",str(Path(a.native_source).resolve()),"-o",str(output)]
    with log.open("wb") as f:
        proc=subprocess.run(command,stdout=f,stderr=subprocess.STDOUT,
                            timeout=remaining(a),check=False)
    require(proc.returncode==0,"Native compilation failed; see temporary build log")
    old={"binding":binding,"sourceSHA256":NATIVE_SHA,"binary":descriptor(output),
         "compiler":a.cxx,"flags":["-O3","-std=c++17"],"log":descriptor(log),
         "temporaryOnly":True}
    atomic_json(mp,old);result["parameters"]["nativeBuild"]=old
    return output

def read_field_square_rows(path,binding,meta,native):
    raw=Path(path).read_bytes()
    require(raw[:8]==b"R15B1F11","Actual finite-field lift magic")
    prime,nc,nh,k,ra,rb=struct.unpack_from("<6I",raw,8)
    require((prime,nc,nh,ra,rb)==(11,4367,22,4345,native["completeFirstConnectionRank"])
            and k==22-rb,"Actual finite-field lift dimensions")
    require(raw[32:96].decode("ascii")==binding,"Finite-field lift binding")
    offset=96+22*k
    require(len(raw)==offset+4367*k,"Complete finite-field correction bytes")
    reads=[list(raw[offset+i*k:offset+(i+1)*k]) for i in meta["nineSquareTargetIndices"]]
    require(all(v<11 for row in reads for v in row),"Field square coordinates")
    return {"shape":[9,k],"matrix":reads,"sha256":small_hash(reads),
            "allZero":all(not v for row in reads for v in row),
            "theseAreFieldCochainsOnly":True}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--generator",required=True)
    ap.add_argument("--actions",required=True)
    ap.add_argument("--original-two-generator",required=True)
    ap.add_argument("--constant-receipt",required=True)
    ap.add_argument("--paid-first-receipt",required=True)
    ap.add_argument("--native-source",required=True)
    ap.add_argument("--checkpoint-dir",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--remaining-seconds",type=float,default=300)
    ap.add_argument("--memory-mib",type=int,default=2048)
    ap.add_argument("--cxx",default="c++")
    a=ap.parse_args();start=time.monotonic()
    require(a.remaining_seconds>0 and a.memory_mib>=512,"Finite shared resource bounds")
    a._deadline=start+a.remaining_seconds
    soft,hard=resource.getrlimit(resource.RLIMIT_AS)
    limit=a.memory_mib*1024*1024
    if hard!=resource.RLIM_INFINITY:limit=min(limit,hard)
    resource.setrlimit(resource.RLIMIT_AS,(limit,hard))
    root=Path(a.checkpoint_dir);root.mkdir(parents=True,exist_ok=True)
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    pins={"generator":(a.generator,GEN_SHA),"actions":(a.actions,ACT_SHA),
          "originalTwoGenerator":(a.original_two_generator,BASE_SHA),
          "constantReceipt":(a.constant_receipt,CONST_SHA),
          "paidRationalFirstReceipt":(a.paid_first_receipt,PAID_FIRST_SHA),
          "nativeSource":(a.native_source,NATIVE_SHA)}
    actual={}
    for name,(path,sha) in pins.items():
        actual[name]=file_sha(path);require(actual[name]==sha,"Pinned input "+name)
    self_sha=file_sha(__file__)
    paid_outer=json.loads(Path(a.paid_first_receipt).read_bytes())
    require(paid_outer["exitCode"]==0 and paid_outer["result"]["status"]=="completed",
            "Paid rational first family completed")
    paid=paid_outer["result"]["parameters"]
    family=paid["firstRestrictedFamily"];verification=paid["firstRestrictedFamilyVerification"]
    require(family["leadingDimension"]==15 and family["nineLambda1SquareReadAllZero"]
            and verification["all6188OriginalRowsVerified"] and verification["heads"]==15
            and verification["originalProductCoordinates"]==185640,
            "Paid15 independent true rational first jets with full original products")
    receipt=json.loads(Path(a.constant_receipt).read_bytes())
    require(receipt["characteristicZeroRank"]==4345 and
            receipt["largeMacaulay"]["field"]==11 and receipt["largeMacaulay"]["rank"]==4345,
            "Paid full original constant ranks")
    binding=small_hash({"format":"r150-two-full-original-field-first-connection-v1",
                       "sourceSHA256":self_sha,"inputSHA256":actual,
                       "physicalCoefficientSHA256":paid["physicalCoefficientSHA256"],
                       "prime":11,"sourceRows":6188,"targetCoordinates":4367,
                       "constantHeads":22})
    result={"format":"r150-two-full-original-first-connection-field11-receipt-v1",
            "status":"started","parameters":{
                "binding":binding,"selfSHA256":self_sha,"inputSHA256":actual,
                "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
                "allMatricesTemporary":True,"noLargeRecomputableDataUploaded":True,
                "paidRationalFirstHeadDimension":15,
                "paidRationalFirstConnectionUpperBound":7,
                "paidRationalFirstExecutionSource":paid_outer["executionSourceCommit"],
                "nativeSourceSHA256":NATIVE_SHA}}
    status=0
    try:
        m=module_at("r150_full_beta1_physical",a.generator)
        j=module_at("r150_full_beta1_actions",a.actions)
        d=module_at("r150_full_beta1_original_two",a.original_two_generator)
        path,meta=write_prepared_input(a,m,j,d,receipt,paid,binding,result)
        binary=compiled_native(a,binding,result)
        nd=root/"native-result";nd.mkdir(exist_ok=True)
        nr=nd/"native-first-connection-receipt.json"
        if nr.exists():
            native=json.loads(nr.read_bytes())
            require(native.get("binding")==binding and native.get("status")=="completed",
                    "Only completed same-binding native result may be resumed")
        else:
            native_seconds=max(0.001,remaining(a)-min(5.0,remaining(a)/10))
            with (root/"native-stdout.json").open("wb") as stdout, \
                 (root/"native-stderr.log").open("wb") as stderr:
                proc=subprocess.run([str(binary.resolve()),str(path.resolve()),str(nd.resolve()),
                                     repr(native_seconds)],stdout=stdout,stderr=stderr,
                                    timeout=remaining(a),check=False)
            result["parameters"]["nativeExitCode"]=proc.returncode
            require(proc.returncode==0 and nr.exists(),"Native did not complete; no rank is inferred")
            native=json.loads(nr.read_bytes())
        require(native["binding"]==binding and native["constantRank"]==4345 and
                native["allOriginalConstantKernelProductsVerified"] and
                native["allOriginalFirstJetProductsVerified"] and
                native["allOriginalSourcesRetained"] and native["constantPivotOnly"],
                "Complete original native certificate")
        b=native["completeFirstConnectionRank"]
        require(0<=b<=7,"Good11 lower bound contradicts the paid rational15 heads")
        files=["native-first-connection-receipt.json","constant-source-row-operations.bin",
               "field-original-first-lifts.bin","field-complete-connection-residual.bin",
               "constant-normalized-pivot-rows.bin"]
        data={name:descriptor(nd/name) for name in files}
        result["parameters"]["nativeResult"]=native
        result["parameters"]["temporaryNativeFiles"]=data
        result["parameters"]["fieldFirstSquareRead"]=read_field_square_rows(
            nd/"field-original-first-lifts.bin",binding,meta,native)
        result["parameters"]["conclusion"]={
            "completeFirstConnectionRankModulo11":b,
            "completeFirstConnectionRankOverQInterval":[b,7],
            "completeFirstConnectionRankOverQExact":7 if b==7 else None,
            "completeRationalFirstHeadDimensionExact":15 if b==7 else None,
            "sameConstantRankAndUnitKernelNormalizationVerified":True,
            "rankComparisonUsesConstantUnitSchurOverZLocalizedAt11":True,
            "allRationalFirstJetsHaveZeroNineSquareRead":True if b==7 else None,
            "normalFourAndFiveCorrectionsIncludedInFieldComputation":True,
            "finiteFieldLiftsNotPromotedToRationalLifts":True,
            "noSecondJetOrTargetLocalMembershipClaim":True}
        result["status"]="completed"
    except (TimeoutError,subprocess.TimeoutExpired) as exc:
        result["status"]="budget-paused";result["error"]=str(exc);status=124
    except Exception as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc);status=1
    finally:
        result["elapsedSeconds"]=time.monotonic()-start
        require(len(canonical(result))<80000,"Small mathematical receipt limit")
        atomic_json(out/"two-full-original-first-connection-field11-receipt.json",result)
        print(canonical(result).decode("ascii"),flush=True)
    return status

if __name__=="__main__":raise SystemExit(main())
