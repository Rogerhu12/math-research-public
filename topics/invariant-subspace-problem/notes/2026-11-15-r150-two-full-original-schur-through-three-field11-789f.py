#!/usr/bin/env python3
"""Full ORIGINAL s=2 field11 Schur to order3 using the paid constant DAG.

Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
All22 original constant heads are transported, not only the compatible15.
Each unit-graph coefficient is checked on all6188 original source rows.
Only the remaining1843x22 finite-field series is newly Smith-reduced.
A completed field length gives a Q upper bound; it is not automatically a
Q equality.  Equality uses the separately verified true projected length12.
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
from flint import nmod_mat

FIRST_DRIVER_SHA="5033e098f01b7daf0b64e2c15291935c972c2459e1dc338c14887fdfde238e7c"
FIRST_NATIVE_SHA="f2e5bf564781eb7dabce1a9c7c277389af65410b2f91adee996fc4274fa7df76"
GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
TWO3_SHA="11b727a08cab142bc016c84eff61ad70360598c73334f39903b5bafd5aab36aa"
NATIVE_SHA="a5b34ee383e2484421188dfd5317418aea2649779b09219271d90e28d72f6592"
PARENT_SHA="aebdd169ec950f7eb4c17b7e9ac4dc30ecb205dfc6a2d9476af9d4d03ebc9d3a"
PROJECTION_SHA="693da6446a6f04cba2c343ea49d9d3466caad1aebd056e91db338163b20d3332"
PARENT_BINDING="f33e3980c2fce162495692f24258b6d32ef00f782d9a1c2817fa054364237f02"
PRIME=11
ORDER=3

def require(ok,message):
    if not ok:raise AssertionError(message)
def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def digest(obj):return hashlib.sha256(canonical(obj)).hexdigest()
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
    tmp=path.with_name(path.name+".tmp");tmp.write_bytes(canonical(obj));os.replace(tmp,path)
def module_at(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
def descriptor(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":file_sha(path),"temporaryOnly":True}
def remaining(a):
    value=a._deadline-time.monotonic()
    if value<=0:raise TimeoutError("Shared time budget exhausted")
    return value
def matrix_zero(M):
    return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))
def block(M,rows,cols):
    return nmod_mat(len(rows),len(cols),[int(M[i,j]) for i in rows for j in cols],PRIME)
def mat_hash(M):
    h=hashlib.sha256(struct.pack("<3I",11,M.nrows(),M.ncols()))
    h.update(bytes(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols())))
    return h.hexdigest()
def pivots(R,rank):
    p=[]
    for i in range(rank):
        c=next((j for j in range(R.ncols()) if R[i,j]),None)
        require(c is not None and R[i,c]==1,"Actual field RREF pivot")
        p.append(c)
    require(p==sorted(set(p)),"Actual ordered field pivots");return p
def identity(n):
    return nmod_mat(n,n,[int(i==j) for i in range(n) for j in range(n)],PRIME)

def prepared(a,g,m,j,two,parent,binding,result):
    root=Path(a.checkpoint_dir);mp=root/"prepared-series-input.json"
    if mp.exists():
        old=json.loads(mp.read_bytes())
        require(old["binding"]==binding and old["verified"],"Same verified series input")
        path=root/old["input"]["file"]
        require(path.stat().st_size==old["input"]["bytes"] and
                file_sha(path)==old["input"]["sha256"],"Immutable series input bytes")
        result["parameters"]["originalPreparation"]=old["metadata"]
        result["parameters"]["originalSeriesInput"]=old["input"]
        return path
    coeff=two.original_at_two(m,j,3)
    oldphy=parent["originalPreparation"]["physicalCoefficientSHA256"]
    require(all(coeff["physical"].get(k)==v for k,v in oldphy.items()),
            "All original physical0..2 prefixes retained")
    polys=[[g.polynomial(coeff,k,eq,m) for eq in range(17)] for k in range(4)]
    logical=lambda layers:digest([[[[list(mon),str(v)] for mon,v in eq] for eq in layer]
                                  for layer in layers])
    prefix=logical(polys[:3])
    require(prefix==parent["originalPreparation"]["originalAll17PolynomialJetsSHA256"],
            "ALL17 original complete rational coefficient0..2 prefixes retained")
    for layer in polys:
        for eq in layer:
            for mon,value in eq:
                require(1<=len(mon)<=2,"Original equation degree")
                g.modq(value)
    require(any(coeff["pure"][1]),"Original g'(2) pure coefficient is retained")
    targets=[mon for deg in range(5,0,-1) for mon in combinations_with_replacement(range(11),deg)]
    sources=[(eq,mon) for deg in range(4) for eq in range(17)
             for mon in combinations_with_replacement(range(11),deg)]
    require(digest(targets)==parent["originalPreparation"]["targetOrderSHA256"]
            and digest(sources)==parent["originalPreparation"]["sourceOrderSHA256"],
            "Same complete original target and source dictionaries")
    ix={mon:i for i,mon in enumerate(targets)}
    tmp=root/"original-series-input.bin.tmp"
    with tmp.open("wb") as f:
        f.write(b"R15SJ311");f.write(struct.pack("<5I",11,6188,4367,22,3))
        f.write(binding.encode("ascii"));f.write(PARENT_BINDING.encode("ascii"))
        for k in range(4):
            for row,(eq,mult) in enumerate(sources):
                if row%256==0:remaining(a)
                terms={}
                for mon,value in polys[k][eq]:
                    col=ix[tuple(sorted(mon+mult))]
                    terms[col]=(terms.get(col,0)+g.modq(value))%11
                ordered=[(col,v) for col,v in sorted(terms.items()) if v]
                require(len(ordered)<=77,"Original series support bound")
                f.write(struct.pack("<H",len(ordered)))
                for col,v in ordered:f.write(struct.pack("<HB",col,v))
    sha=file_sha(tmp);path=root/("original-series-input-"+sha+".bin")
    if path.exists():
        require(file_sha(path)==sha,"Immutable series input collision");tmp.unlink()
    else:os.replace(tmp,path)
    meta={"originalSourceRows":6188,"originalTargetCoordinates":4367,"constantHeadColumns":22,
          "throughOrder":3,"allOriginalCoefficient0Through2PrefixesEqualPaid":True,
          "completeRationalPrefixSHA256":prefix,
          "completeRationalThroughThreeSHA256":logical(polys),
          "physicalCoefficientSHA256":coeff["physical"],
          "allOriginalParameterDenominatorsUnitsAt11":True,
          "noPrimitiveRowContentDivision":True,"originalFirstPureCoefficientRetained":True,
          "gAtTwoCoefficients":[0,-64,-72,-24,-2],
          "sameSourceOrderSHA256":digest(sources),"sameTargetOrderSHA256":digest(targets)}
    item=descriptor(path)
    atomic_json(mp,{"binding":binding,"verified":True,"input":item,
                    "metadata":meta,"temporaryOnly":True})
    result["parameters"]["originalPreparation"]=meta
    result["parameters"]["originalSeriesInput"]=item
    return path

def native_binary(a,binding,result):
    root=Path(a.checkpoint_dir);mp=root/"series-native-build.json"
    if mp.exists():
        old=json.loads(mp.read_bytes());path=root/old["binary"]["file"]
        require(old["binding"]==binding and old["sourceSHA256"]==NATIVE_SHA
                and old["includedFirstNativeSHA256"]==FIRST_NATIVE_SHA,"Native build binding")
        require(path.stat().st_size==old["binary"]["bytes"] and file_sha(path)==old["binary"]["sha256"],
                "Actual native binary bytes")
        result["parameters"]["nativeBuild"]=old;return path
    path=root/("schur-three-native-"+NATIVE_SHA);log=root/"series-native-build.log"
    include="-DR150_FIRST_NATIVE_SOURCE="+json.dumps(str(Path(a.first_native_source).resolve()))
    cmd=[a.cxx,"-O3","-std=c++17",include,str(Path(a.native_source).resolve()),"-o",str(path)]
    with log.open("wb") as f:
        p=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=remaining(a),check=False)
    require(p.returncode==0,"Series native compilation failed")
    old={"binding":binding,"sourceSHA256":NATIVE_SHA,"includedFirstNativeSHA256":FIRST_NATIVE_SHA,
         "binary":descriptor(path),"compiler":a.cxx,"flags":["-O3","-std=c++17"],
         "log":descriptor(log),"temporaryOnly":True}
    atomic_json(mp,old);result["parameters"]["nativeBuild"]=old;return path

def read_schur(path,binding):
    raw=Path(path).read_bytes()
    require(raw[:8]==b"R15SC311","Original Schur binary magic")
    require(struct.unpack_from("<4I",raw,8)==(11,1843,22,3),"Original Schur binary dimensions")
    require(raw[24:88].decode("ascii")==binding,"Original Schur binding")
    rows=list(struct.unpack_from("<1843H",raw,88));offset=88+2*1843
    require(rows==sorted(set(rows)) and all(r<6188 for r in rows),"All remaining original source rows")
    count=1843*22
    require(len(raw)==offset+4*count,"Every Schur series coefficient retained")
    seq=[]
    for k in range(4):
        b=raw[offset+k*count:offset+(k+1)*count]
        require(all(v<11 for v in b),"Schur field values")
        seq.append(nmod_mat(1843,22,list(b),11))
    require(matrix_zero(seq[0]),"Exact constant Schur zero")
    return seq,rows

def complete_small_smith(a,seq,source_rows,result):
    """Unit Schur and division only; all residual original rows are retained."""
    phases=[];exponents=[];power=0;covered=0
    row_labels=list(source_rows);column_labels=list(range(22))
    while seq and covered<9:
        remaining(a)
        nr,nc=seq[0].nrows(),seq[0].ncols()
        R,r=seq[0].rref();pc=pivots(R,r)
        phase={"exponent":power,"shape":[nr,nc],"rank":r,
               "coefficientSHA256":[mat_hash(M) for M in seq],
               "precisionCoefficients":len(seq)}
        require(covered+r<=9,"Original generic Q rank4354 forbids more than9 field directions")
        if r==0:
            require(matrix_zero(seq[0]),"Rank zero means the entire constant block is zero")
            phase.update({"allOriginalRemainingRowsRetained":True,"constantBlockZero":True,
                          "cumulativePositiveRank":covered,
                          "positiveLengthSoFar":sum(exponents)})
            phases.append(phase);seq=seq[1:];power+=1;continue
        Rt,rt=block(seq[0],list(range(nr)),pc).transpose().rref()
        require(rt==r,"True unit-row profile");pr=pivots(Rt,rt)
        pset=set(pc);rset=set(pr)
        fc=[i for i in range(nc) if i not in pset]
        fr=[i for i in range(nr) if i not in rset]
        U=[block(M,pr,pc) for M in seq];V=[block(M,pr,fc) for M in seq]
        W=[block(M,fr,pc) for M in seq];Z=[block(M,fr,fc) for M in seq]
        inv=U[0].inv();require(U[0]*inv==identity(r) and inv*U[0]==identity(r),
                                 "Actual finite-field unit inverse")
        Y=[inv]
        for k in range(1,len(seq)):
            v=nmod_mat(r,r,[0]*(r*r),11)
            for i in range(1,k+1):v+=U[i]*Y[k-i]
            Y.append(-(inv*v))
        for k in range(len(seq)):
            left=nmod_mat(r,r,[0]*(r*r),11);right=nmod_mat(r,r,[0]*(r*r),11)
            for i in range(k+1):
                left+=U[i]*Y[k-i];right+=Y[i]*U[k-i]
            wanted=identity(r) if k==0 else nmod_mat(r,r,[0]*(r*r),11)
            require(left==wanted and right==wanted,"Both exact unit inverse convolutions")
        corrections=[]
        for k in range(len(seq)):
            v=nmod_mat(r,len(fc),[0]*(r*len(fc)),11)
            for i in range(k+1):v+=Y[i]*V[k-i]
            corrections.append(-v)
        schur=[]
        for k in range(len(seq)):
            t=Z[k]
            for i in range(k+1):t+=W[i]*corrections[k-i]
            schur.append(t)
        lifts=[]
        for k in range(len(seq)):
            X=nmod_mat(nc,len(fc),[0]*(nc*len(fc)),11)
            if k==0:
                for j,c in enumerate(fc):X[c,j]=1
            for i,c in enumerate(pc):
                for j in range(len(fc)):X[c,j]=corrections[k][i,j]
            lifts.append(X)
        count=0
        for k in range(len(seq)):
            v=nmod_mat(nr,len(fc),[0]*(nr*len(fc)),11)
            for i in range(k+1):v+=seq[i]*lifts[k-i]
            require(matrix_zero(block(v,pr,list(range(len(fc))))) and
                    block(v,fr,list(range(len(fc))))==schur[k],
                    "FULL original remaining-row Schur multiplication")
            count+=nr*len(fc)
        require(matrix_zero(schur[0]),"Complete residual constant block vanishes")
        exponents.extend([power]*r);covered+=r
        phase.update({"unitRows":pr,"unitColumns":pc,
                      "originalResidualSourceUnitRows":[row_labels[i] for i in pr],
                      "originalConstantHeadUnitColumns":[column_labels[i] for i in pc],
                      "unitConstantDeterminantModulo11":int(U[0].det()),
                      "unitConstantSHA256":mat_hash(U[0]),
                      "allUnitConvolutionsVerified":True,
                      "allRemainingOriginalRowSchurProductsVerified":True,
                      "originalRemainingProductCoordinates":count,
                      "allOriginalRemainingRowsRetained":True,
                      "schurSHA256":[mat_hash(M) for M in schur],
                      "cumulativePositiveRank":covered,"positiveLengthSoFar":sum(exponents)})
        phases.append(phase)
        row_labels=[row_labels[i] for i in fr]
        column_labels=[column_labels[i] for i in fc]
        seq=schur[1:];power+=1
    result["parameters"]["exactFieldTaylorPhases"]=phases
    result["parameters"]["confirmedFieldPositiveExponents"]=exponents
    result["parameters"]["coveredFieldPositiveRank"]=covered
    result["parameters"]["allNineGenericPositiveDirectionsCompleted"]=(covered==9)
    result["parameters"]["allFieldSchurOriginalRowsVerified"]=True
    return exponents,covered

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--first-driver",required=True)
    ap.add_argument("--first-native-source",required=True)
    ap.add_argument("--generator",required=True)
    ap.add_argument("--actions",required=True)
    ap.add_argument("--two-three-generator",required=True)
    ap.add_argument("--native-source",required=True)
    ap.add_argument("--parent-receipt",required=True)
    ap.add_argument("--projection-receipt",required=True)
    ap.add_argument("--parent-checkpoint-dir",required=True)
    ap.add_argument("--checkpoint-dir",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--remaining-seconds",type=float,default=180)
    ap.add_argument("--memory-mib",type=int,default=2048)
    ap.add_argument("--cxx",default="c++")
    a=ap.parse_args();start=time.monotonic()
    require(a.remaining_seconds>0 and a.memory_mib>=512,"Finite shared resources")
    a._deadline=start+a.remaining_seconds
    soft,hard=resource.getrlimit(resource.RLIMIT_AS);limit=a.memory_mib*1024*1024
    if hard!=resource.RLIM_INFINITY:limit=min(limit,hard)
    resource.setrlimit(resource.RLIMIT_AS,(limit,hard))
    root=Path(a.checkpoint_dir);root.mkdir(parents=True,exist_ok=True)
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    pins={"firstDriver":(a.first_driver,FIRST_DRIVER_SHA),
          "firstNativeSource":(a.first_native_source,FIRST_NATIVE_SHA),
          "generator":(a.generator,GEN_SHA),"actions":(a.actions,ACT_SHA),
          "originalTwoThreeGenerator":(a.two_three_generator,TWO3_SHA),
          "nativeSource":(a.native_source,NATIVE_SHA),
          "parentReceipt":(a.parent_receipt,PARENT_SHA),
          "projectionReceipt":(a.projection_receipt,PROJECTION_SHA)}
    actual={}
    for name,(path,expected) in pins.items():
        actual[name]=file_sha(path);require(actual[name]==expected,"Pinned input "+name)
    parent_outer=json.loads(Path(a.parent_receipt).read_bytes())
    require(parent_outer["exitCode"]==0 and parent_outer["result"]["status"]=="completed",
            "Paid complete first connection")
    parent=parent_outer["result"]["parameters"]
    require(parent["binding"]==PARENT_BINDING and parent["nativeResult"]["constantRank"]==4345
            and parent["nativeResult"]["completeFirstConnectionRank"]==7,
            "Same paid full constant and first connection")
    project_outer=json.loads(Path(a.projection_receipt).read_bytes())
    pp=project_outer["result"]["parameters"]
    require(project_outer["exitCode"]==0 and project_outer["result"]["status"]=="completed"
            and pp["projectedTorsionLengthExact"]==12 and pp["projectionGenericRankReached"]
            and pp["all6188OriginalProjectedSourcesRetained"]
            and pp["localGenerationBothDirectionsVerified"]
            and pp["paidFullGenericRank"]==4354 and pp["paidFullConstantRank"]==4345,
            "True projected length12 with the same original complete source module")
    proot=Path(a.parent_checkpoint_dir)
    old_input=proot/parent["originalInput"]["file"]
    oldfiles={"originalInput":(old_input,parent["originalInput"])}
    for name in ("constant-normalized-pivot-rows.bin","constant-source-row-operations.bin",
                 "field-complete-connection-residual.bin"):
        oldfiles[name]=(proot/"native-result"/name,parent["temporaryNativeFiles"][name])
    for name,(path,item) in oldfiles.items():
        require(path.stat().st_size==item["bytes"] and file_sha(path)==item["sha256"],
                "Actual immutable parent file "+name)
    prep=json.loads((proot/"prepared-original-input.json").read_bytes())
    require(prep["binding"]==PARENT_BINDING and prep["verified"] and
            prep["input"]==parent["originalInput"] and
            prep["metadata"]==parent["originalPreparation"],
            "Same paid preparation manifest, not a new or altered constant model")
    self_sha=file_sha(__file__)
    binding=digest({"format":"r150-two-original-full-field-schur-through-three-v1",
                    "sourceSHA256":self_sha,"inputs":actual,"parentBinding":PARENT_BINDING,
                    "parentFiles":{name:item for name,(_,item) in oldfiles.items()},
                    "order":3,"allOriginalConstantHeads":22})
    result={"format":"r150-two-full-original-schur-through-three-field11-receipt-v1",
            "status":"started","parameters":{"binding":binding,"parentBinding":PARENT_BINDING,
                "selfSHA256":self_sha,"inputSHA256":actual,
                "parentExecutionSource":parent_outer["executionSourceCommit"],
                "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
                "allMatricesTemporary":True,"noLargeRecomputableDataUploaded":True,
                "all22OriginalHeadsRetained":True,
                "paidFullGenericRankOverQ":4354,"paidFullConstantRank":4345,
                "paidTrueProjectedLength":12,"constantGaussianEliminationRepeated":False}}
    status=0
    try:
        g=module_at("r150_series_paid_first",a.first_driver)
        m=module_at("r150_series_physical",a.generator)
        j=module_at("r150_series_actions",a.actions)
        two=module_at("r150_series_original_two_three",a.two_three_generator)
        path=prepared(a,g,m,j,two,parent,binding,result)
        binary=native_binary(a,binding,result)
        nd=root/"native-result";nd.mkdir(exist_ok=True)
        nr=nd/"native-original-schur-through-three-receipt.json"
        if nr.exists():
            native=json.loads(nr.read_bytes())
            require(native.get("status")=="completed" and native.get("binding")==binding,
                    "Only complete same-binding native Schur may be resumed")
        else:
            native_seconds=max(.001,remaining(a)-min(8.0,remaining(a)/10))
            cmd=[str(binary.resolve()),str(path.resolve()),str(old_input.resolve()),
                 str(oldfiles["constant-normalized-pivot-rows.bin"][0].resolve()),
                 str(oldfiles["constant-source-row-operations.bin"][0].resolve()),
                 str(oldfiles["field-complete-connection-residual.bin"][0].resolve()),
                 str(nd.resolve()),repr(native_seconds)]
            with (root/"native-series-stdout.json").open("wb") as stdout, \
                 (root/"native-series-stderr.log").open("wb") as stderr:
                p=subprocess.run(cmd,stdout=stdout,stderr=stderr,
                                 timeout=remaining(a),check=False)
            result["parameters"]["nativeExitCode"]=p.returncode
            require(p.returncode==0 and nr.exists(),"Native series incomplete; no local length inferred")
            native=json.loads(nr.read_bytes())
        require(native["binding"]==binding and native["parentBinding"]==PARENT_BINDING
                and native["throughOrder"]==3 and native["allOriginalResidualIdentitiesVerified"]
                and native["allFirstSchurEntriesEqualPaidResidual"]
                and native["unitSourceResidualsAllZero"],
                "Full actual original Schur identities")
        result["parameters"]["nativeResult"]=native
        files=[nr,nd/"complete-original-schur-through-three.bin",
               nd/"complete-original-unit-graph-through-three.bin"]
        files+=sorted(nd.glob("original-unit-graph-order*-"+binding+".bin"))
        result["parameters"]["temporaryNativeFiles"]={p.name:descriptor(p) for p in files}
        seq,rows=read_schur(nd/"complete-original-schur-through-three.bin",binding)
        exponents,covered=complete_small_smith(a,seq,rows,result)
        require(exponents[:7]==[1]*7,"Same paid full first connection seven")
        complete=(covered==9)
        length=sum(exponents) if complete else None
        if complete:require(length>=12,"Field upper bound contradicts true original projected length12")
        result["parameters"]["conclusion"]={
            "fullFieldGenericRankReached":complete,
            "fullFieldPositiveSmithExponentsExact":exponents if complete else None,
            "fullFieldLocalTorsionLengthExact":length,
            "fullFieldFreeRank":13 if complete else None,
            "fullCharacteristicZeroLocalLengthInterval":[12,length] if complete else None,
            "fullCharacteristicZeroLocalLengthExact":12 if length==12 else None,
            "sameOriginalWQuotientLengthUpperBound":length-12 if complete else None,
            "wholeOriginalWLocallyInSource":True if length==12 else None,
            "allNineOriginalSquaresLocallyInSource":True if length==12 else None,
            "allNineH0TargetsLocallyInSource":True if complete and length<=13 else None,
            "someOriginalMaximalMinorOrder12And11UnitLeadingCoefficient":True if length==12 else None,
            "characteristicZeroComparisonUsesOriginal11IntegralModel":True,
            "fieldGenericRankUpperUsesOnlyConstantJ3Denominators":True,
            "fieldPositiveLengthNotAutomaticallyCalledQEquality":True,
            "constantUnitGraphIsNot22LeftKernelJets":True,
            "noOtherFinitePointOrGlobalPolynomialMembershipClaim":True}
        result["status"]="completed"
    except (TimeoutError,subprocess.TimeoutExpired) as exc:
        result["status"]="budget-paused";result["error"]=str(exc);status=124
    except Exception as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc);status=1
    finally:
        result["elapsedSeconds"]=time.monotonic()-start
        require(len(canonical(result))<85000,"Small source and parameter receipt")
        atomic_json(out/"two-full-original-schur-through-three-field11-receipt.json",result)
        print(canonical(result).decode("ascii"),flush=True)
    return status

if __name__=="__main__":raise SystemExit(main())
