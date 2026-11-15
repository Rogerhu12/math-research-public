#!/usr/bin/env python3
"""Original infinity eighth forcing: two true quotient representatives.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro.
Read the actual full seventh pack, undo its saved column normalization, and
retain the projected exponent-eight head and the genuinely new seventh head.
Inspect all original high rows, including A2*lambda6 and A1*lambda7.
All higher coefficients of both the head maps and incoming maps are retained.  If nonzero, apply the paid full
constant-H row DAG to an exact primitive scaling of that new RHS only.
A nonzero field residual then proves Q nonmembership because Qrank(H) is
already exactly3760.  A zero field residual does not prove Q membership.
No new Gaussian, no whole-H rational solve, and no eighth rank is claimed.
All reconstructible matrices remain temporary.
"""
import argparse
import gzip
import hashlib
import importlib.util
import io
import json
from math import gcd
import os
from pathlib import Path
import resource
import struct
import sys
import time

FORMAT="r150-infinity-eighth-original-high-forcing-probe-v1"
GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
Q_SOURCE_SHA="dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79"
SIX_SOURCE_SHA="4d759c0efbc8a647bd5845b21da5e871de28f0d43ae6f2fc84c376afb472e328"
Q_RECEIPT_SHA="ea44027e462054b9fdb9c9101065faaba0b14dc5ab9b1a5602c06fecbb765207"
SEVEN_RECEIPT_SHA="6faacedfb22582d79a2cefc73d97a8a11eeb0cdb024bc5c6d93de995a3102e65"
HIGH_RECEIPT_SHA="0f6cbe9bb23601be632d0045f35839b922e16e4d893aca6b9d4e2f849cbd9141"
SEVEN_BINDING="8a9a52e60045cb4124f90e73ce2cb210d98f88acae2802287bd5e17a56d2ab42"
SEVEN_PACK_SHA="17e518267cd5a1091cf5dccdeaf39f2645020bd6a967ce4b4df1dad26481f43f"
SEVEN_PHASES={
"prepared-complete-low":(1496220,"811eb06f809856f3f82856e9aef04b07edc6ec065a501d66ea921b9b5ad2527b"),
"complete-seventh-cochains-verified":(610369,"0bb0b469006bc7a15ffff11b7bcfedc772813cfcd75f8bda8ecdaede49a01841")}
P31=31

def require(ok,msg):
    if not ok:raise AssertionError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def digest_obj(x):return hashlib.sha256(canonical(x)).hexdigest()
def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return h.hexdigest()
def atom(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".tmp");temp.write_bytes(canonical(obj));os.replace(temp,path)
def mod(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m
def remain(a):
    if time.monotonic()>=a._deadline:raise TimeoutError("Complete eighth forcing boundary")
def desc(path):
    p=Path(path);return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),"temporaryOnly":True}
def checked(root,item):
    require(Path(item["file"]).name==item["file"],"Temporary basename")
    p=Path(root)/item["file"]
    require(p.stat().st_size==item["bytes"] and sha(p)==item["sha256"],"Complete actual temporary file")
    return p
def read_result(path):
    o=json.loads(Path(path).read_bytes());return o.get("result",o)
def seven_phase(a,q,seven,name):
    root=Path(a.seventh_out);mp=root/"complete-seventh-checkpoints.json"
    require(sha(mp)==seven["parameters"]["temporaryManifestSHA256"],"Actual complete seventh manifest")
    man=json.loads(mp.read_bytes())
    require(man["format"]=="r150-infinity-complete-seventh-temporary-v1" and
            man["binding"]==SEVEN_BINDING and man["temporaryOnly"] is True,"Actual original seventh binding")
    item=man["phases"][name]
    require(item==seven["parameters"]["temporaryPhases"][name] and
            (item["bytes"],item["sha256"])==SEVEN_PHASES[name],"Actual seventh phase pin")
    p=checked(root,item)
    with gzip.open(p,"rt",encoding="utf-8") as f:o=json.load(f)
    require(o["format"]==man["format"] and o["binding"]==SEVEN_BINDING and
            o["phase"]==name and o["complete"] is True,"Complete original seventh source payload")
    return q.dec(o["data"],q.DQ)
def save_phase(a,q,binding,name,data,rec):
    root=Path(a.checkpoint_dir);root.mkdir(parents=True,exist_ok=True)
    o={"format":FORMAT,"binding":binding,"phase":name,"complete":True,
       "temporaryOnly":True,"data":q.enc(data)}
    p=root/(name+".tmp.json.gz")
    with p.open("wb") as raw:
        with gzip.GzipFile(filename="",mode="wb",fileobj=raw,compresslevel=1,mtime=0) as gz:
            with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as f:
                json.dump(o,f,sort_keys=True,separators=(",",":"))
    h=sha(p);dest=root/(name+"-"+h+".json.gz");os.replace(p,dest)
    rec["parameters"].setdefault("temporaryPhases",{})[name]=desc(dest)
    atom(root/"eighth-forcing-checkpoints.json",{"format":FORMAT,"binding":binding,
        "temporaryOnly":True,"phases":rec["parameters"]["temporaryPhases"]})
    atom(a.out,rec)
    return dest

def original_pair(a,q,s,m,j,projection,seven,rec):
    prepared=seven_phase(a,q,seven,"prepared-complete-low")
    verified=seven_phase(a,q,seven,"complete-seventh-cochains-verified")
    pack=verified["pack"];N=verified["normalizer"]
    require((pack.nrows(),pack.ncols())==(4120,16) and q.mh(pack)==SEVEN_PACK_SHA and
            verified["metadata"]["allEightOrdersAll6188OriginalSourceRowsVerified"] is True,
            "Actual sixteen full original seventh cochains")
    require((N.nrows(),N.ncols())==(16,16) and
            q.mh(N)==seven["parameters"]["actualCanonicalCochain"]["normalizerSHA256"],
            "Actual original seventh column normalizer")
    Ni=N.inv();require(N*Ni==q.DQ.eye(16) and Ni*N==q.DQ.eye(16),"Actual invertible normalization")
    pre=pack*Ni;require(pre*N==pack,"Every original source coefficient transported exactly")
    lowranges=[(155*k,155*(k+1)) for k in range(6)]+[(930,1085),(2525,2680)]
    for k,(lo,hi) in enumerate(lowranges):
        require(q.DQ.sub(pre,range(lo,hi),range(15))==prepared["stableMaps"][k],
                "All fifteen projected seventh maps recovered")
    for lo,hi in ((1085,1535),(1535,2525),(2680,3130),(3130,4120)):
        require(q.zero(q.DQ.sub(pre,range(lo,hi),range(15))),
                "Projected seventh maps have no unrecorded high coordinates")
    original=s.read_q_phase(a,q,projection,"original-projection-coefficients",s.COEFF)
    coeff=q.coefficient_decode(original["coefficients"])
    PM=q.dec(original["P"][:9],q.DQ)
    require([q.mh(x) for x in PM]==
            projection["parameters"]["originalProjection"]["originalProjectionCoefficientSHA256"][:9],
            "Actual nine original projection coefficient hashes")
    require(coeff["chart"]=="infinity" and coeff["maxOrder"]==11 and
            all(not v for v in coeff["pure"][0]+coeff["pure"][1]),"Original F0/F1 pure zero")
    Top=[q.DQ.sub(x,range(170),range(155)) for x in PM]
    state=q.dec(s.read_q_phase(a,q,projection,"Q-smith-state",s.Q_STATE),q.DQ)
    require(state["complete"] is True,"Actual complete projected Q maps")
    g8=next(g for g in state["positive"] if g["exponent"]==8)
    require(g8["map"][0].ncols()==1,"Actual projected exponent-eight direction")
    L=[]
    for k in range(9):
        extra=q.DQ.sub(pre,range(*lowranges[k]),[15]) if k<8 else q.DQ.mat(155,1)
        L.append(q.DQ.cat([g8["map"][k],extra]))
    X6={2:q.DQ.cat([q.DQ.mat(450,1),q.DQ.sub(pre,range(1085,1535),[15])]),
        3:q.DQ.cat([q.DQ.mat(990,1),q.DQ.sub(pre,range(1535,2525),[15])])}
    X7={2:q.DQ.cat([q.DQ.mat(450,1),q.DQ.sub(pre,range(2680,3130),[15])]),
        3:q.DQ.cat([q.DQ.mat(990,1),q.DQ.sub(pre,range(3130,4120),[15])])}
    later=[g for g in state["positive"] if g["exponent"]>8]
    stable=[q.DQ.cat([g["map"][k] for g in later]+[state["map"][k]]) for k in range(9)]
    require(all(x.ncols()==14 for x in stable),"Fourteen actual projected eighth heads")
    require(q.DQ.cat([stable[0],L[0]]).rref()[1]==16,"Two complete quotient head representatives")
    free=seven["parameters"]["completeLowKernel"]["freeColumns"]
    chosen=[i for i in (0,1) if 597+i not in free]
    require(len(chosen)==1,"Actual seventh incoming original pivot selection")
    k7=chosen[0];U=[]
    for k in range(9):
        if k==0:U.append(q.DQ.mat(155,11))
        else:U.append(q.DQ.cat([prepared["incomingMaps"][k-1],
                               q.DQ.sub(prepared["twoMaps"][k-1],range(155),[k7])]))
    UX7={2:q.DQ.cat([q.DQ.mat(450,10),q.DQ.sub(prepared["sixthNormalTwo"],range(450),[k7])]),
         3:q.DQ.cat([q.DQ.mat(990,10),q.DQ.sub(prepared["sixthNormalThree"],range(990),[k7])])}
    require(q.zero(U[0]),"All eleven whole incoming shifts have zero head")
    count=0
    for k in range(8):
        remain(a)
        V=s.original_low(q,m,j,coeff,Top,L,k)
        for t,X in ((6,X6),(7,X7)):
            if k>=t:V+=q.DQ.vcat([j.apply(m,coeff,k-t,r,X,2) for r in (0,1)])
        require(q.zero(V),"Original lower low identities of both true eighth representatives")
        for r in (2,3):
            H=q.DQ.mat(len(j.source_rows(r)),2)
            for t,X in ((6,X6),(7,X7)):
                if k>=t:H+=j.apply_sparse(m,coeff,k-t,r,X,2)
            require(q.zero(H),"Original lower high identities of both true eighth representatives")
        count+=2*6188
    W=s.original_low(q,m,j,coeff,Top,U,8)
    W+=q.DQ.vcat([j.apply(m,coeff,1,r,UX7,11) for r in (0,1)])
    expected=q.DQ.cat([q.DQ.sub(prepared["M"],range(1088),range(587,597)),
                      q.DQ.sub(prepared["M"],range(1088),[597+k7])])
    require(W==expected,"Exact eleven incoming residues with entire high-source shifts")
    incoming_high=q.DQ.vcat([j.apply_sparse(m,coeff,1,r,UX7,11) for r in (2,3)])
    require(q.zero(incoming_high),"Every complete incoming order-eight high residue is zero")
    low=s.original_low(q,m,j,coeff,Top,L,8)
    for order,X in ((2,X6),(1,X7)):
        low+=q.DQ.vcat([j.apply(m,coeff,order,r,X,2) for r in (0,1)])
    pieces={}
    for label,order,X in (("A2lambda6",2,X6),("A1lambda7",1,X7)):
        pieces[label]=q.DQ.vcat([j.apply_sparse(m,coeff,order,r,X,2) for r in (2,3)])
    H=pieces["A2lambda6"]+pieces["A1lambda7"]
    require((H.nrows(),H.ncols())==(5100,2) and q.zero(q.DQ.sub(H,range(5100),[0])),
            "Projected exponent-eight high column zero")
    require(q.zero(q.DQ.sub(H,range(2295,5100),range(2))),
            "Every source-normal3 eighth forcing row zero")
    nonzero=[i for i in range(5100) if H[i,1]]
    highcounts={}
    for label,X in (("lambda6",X6),("lambda7",X7),("incomingLambda7",UX7)):
        highcounts[label]=[sum(bool(M[i,c]) for i in range(M.nrows()) for c in range(M.ncols()))
                           for M in (X[2],X[3])]
    meta={"fullSeventhHeadCount":16,"paidProjectionEighthHeadCount":14,
        "newEighthQuotientRepresentatives":2,"originalSourceRows":6188,
        "allOriginalRepresentativeLowerProductsZero":True,"originalLowerProductCoordinates":count,
        "oldNormalizerInvertedAndAllOriginalCoefficientsMatched":True,
        "actualSeventhIncomingOriginalFailureIndex":k7,"allElevenPriorIncomingDirectionsTransported":True,
        "allIncomingHighCoefficientsRetained":True,"incomingHighForcingExactlyZero":True,
        "priorIncomingSHA256":q.mh(W),"originalEighthLowSHA256":q.mh(low),
        "originalEighthHighSHA256":q.mh(H),"highShape":[5100,2],"highQRank":int(bool(nonzero)),
        "allOriginalSourceNormal3ForcingCoordinatesZero":True,
        "projectedExponentEightHighColumnZero":True,"extraSeventhHeadHighForcingZero":not nonzero,
        "nonzeroExtraHighCoordinates":len(nonzero),
        "firstNonzeroExtraHighCoordinate":nonzero[0] if nonzero else None,
        "firstNonzeroExtraHighValue":str(H[nonzero[0],1]) if nonzero else None,
        "actualHighCoefficientNonzeroCounts":highcounts,
        "A2Lambda6HighProductSHA256":q.mh(pieces["A2lambda6"]),
        "A1Lambda7HighProductSHA256":q.mh(pieces["A1lambda7"]),
        "sixthNormalTwoSHA256":q.mh(X6[2]),"sixthNormalThreeSHA256":q.mh(X6[3]),
        "seventhNormalTwoSHA256":q.mh(X7[2]),"seventhNormalThreeSHA256":q.mh(X7[3]),
        "incomingSeventhNormalTwoSHA256":q.mh(UX7[2]),"incomingSeventhNormalThreeSHA256":q.mh(UX7[3]),
        "noOldRankOrSmithCalculationRepeated":True,"noEighthConnectionRankClaimed":True}
    rec["parameters"]["originalForcing"]=meta
    data={"twoMaps":L,"sixthNormalTwo":X6[2],"sixthNormalThree":X6[3],
        "seventhNormalTwo":X7[2],"seventhNormalThree":X7[3],"stableMaps":stable,
        "incomingMaps":U,"incomingSeventhNormalTwo":UX7[2],"incomingSeventhNormalThree":UX7[3],
        "incoming":W,"low":low,"high":H,"highProducts":pieces,"Z3":prepared["Z3"],
        "constantLow":q.DQ.sub(prepared["M"],range(1088),range(587)),
        "coefficientData":q.coefficient_encode(coeff),"top":Top,"metadata":meta}
    return data,coeff

def field_necessary(a,q,m,j,high,coeff,H,rec):
    if q.zero(H):
        return {"performed":False,"allHighForcingsZeroOverQ":True,
                "QHighCorrectionCanBeHomogeneous":True}
    remain(a)
    hp=high["parameters"]["originalPreparation"]
    sources=j.source_rows(2)+j.source_rows(3)
    offsets={3:0,4:990,5:2475}
    ix={r:{v:i for i,v in enumerate(j.target_columns(r))} for r in (3,4,5)}
    scaled=[];rat_hash=hashlib.sha256();scale_hash=hashlib.sha256()
    int_hash=hashlib.sha256();unit=True
    for i,row in enumerate(sources):
        if i%64==0:remain(a)
        terms={}
        for r in (3,4,5):
            for c,v in j.sparse_row_terms(coeff,0,row,r,ix[r]):
                cc=offsets[r]+c;terms[cc]=terms.get(cc,m.ZERO)+v
        values=[(c,v) for c,v in sorted(terms.items()) if v]
        den=1
        for _,v in values:
            d=int(v.denom());den=den//gcd(den,d)*d
        raw=[(c,int(v.numer())*(den//int(v.denom()))) for c,v in values]
        content=0
        for _,v in raw:content=gcd(content,abs(v))
        content=content or 1
        ints=[(c,v//content) for c,v in raw]
        scale=m.fmpq(den,content)
        require(all(m.fmpq(v)==scale*terms[c] for c,v in ints),"Original complete-H row scale")
        unit=unit and den%31!=0 and content%31!=0
        scaled.append(scale*H[i,1])
        rat_hash.update(canonical([[c,str(v)] for c,v in values])+b"\n")
        int_hash.update(canonical([[c,str(v)] for c,v in ints])+b"\n")
        scale_hash.update(canonical([str(den),str(content)])+b"\n")
    require(rat_hash.hexdigest()==hp["originalRationalRowsSHA256"] and
            int_hash.hexdigest()==hp["primitiveIntegerRowsSHA256"] and
            scale_hash.hexdigest()==hp["exactWholeRowScalesSHA256"] and unit,
            "Same actual original complete-H rows and unit scales as paid DAG")
    den=1
    for v in scaled:
        d=int(v.denom());den=den//gcd(den,d)*d
    numer=[int(v.numer())*(den//int(v.denom())) for v in scaled]
    content=0
    for v in numer:content=gcd(content,abs(v))
    require(content>0,"Actually nonzero extra original high forcing")
    numer=[v//content for v in numer]
    factor=m.fmpq(den,content)
    require(all(m.fmpq(v)==factor*r for v,r in zip(numer,scaled)),
            "One exact rational scale on the complete new high RHS")
    item=high["parameters"]["temporaryNativeOutputs"]["complete-high-row-operations.bin"]
    path=checked(Path(a.high_out)/"native-result",item)
    raw=path.read_bytes();view=memoryview(raw);pos=0
    require(raw[:8]==b"R15HDG31" and struct.unpack_from("<3I",raw,8)==(31,5100,3762)
            and raw[20:84].decode("ascii")==high["parameters"]["binding"],"Paid complete original high DAG header")
    pos=84;pivot=[None]*3762;residual=[];resrows=[];ops=0
    for i in range(5100):
        if i%64==0:remain(a)
        count=struct.unpack_from("<I",view,pos)[0];pos+=4
        value=numer[i]%31
        for _ in range(count):
            c,f=struct.unpack_from("<HB",view,pos);pos+=3
            require(c<3762 and 0<f<31 and pivot[c] is not None,"Paid earlier normalized pivot in row DAG")
            value+=f*pivot[c];ops+=1
        newcol,first=struct.unpack_from("<HB",view,pos);pos+=3;value%=31
        if newcol==65535:
            require(first==0,"Actual dependent original row marker")
            residual.append(value);resrows.append(i)
        else:
            require(newcol<3762 and pivot[newcol] is None and 0<first<31,"Actual new original pivot")
            pivot[newcol]=(value*pow(first,-1,31))%31
    require(pos==len(raw) and len(residual)==1340 and
            sum(v is not None for v in pivot)==3760 and
            ops==high["parameters"]["actualNativeRank"]["rowAdditions"],
            "Every original high row and paid row operation applied once")
    nz=[k for k,v in enumerate(residual) if v]
    out={"performed":True,"prime":31,"allOriginalHighRows":5100,"allPaidRowOperations":ops,
        "rationalRHSScale":str(factor),"scaledOriginalRHSIntegerSHA256":digest_obj([str(x) for x in numer]),
        "sameCompleteConstantRowScalesVerified":True,"rowScalesActually31Units":True,
        "completeResidualLength":1340,"completeResidualSHA256":digest_obj(residual),
        "fieldResidualRank":int(bool(nz)),
        "firstNonzeroResidualOriginalRow":resrows[nz[0]] if nz else None,
        "firstNonzeroResidualValue":residual[nz[0]] if nz else None,
        "extraHeadHighQNonmembershipProved":bool(nz),
        "QHighMembershipNotInferredFromZeroFieldResidual":True,
        "noNewGaussianPerformed":True,"noQParticularClaimed":True}
    return out,{"primitiveRHS":[str(x) for x in numer],"normalizedUnitPivotValues":pivot,
                "originalDependentRows":resrows,"fullFieldResidual":residual,
                "metadata":out}

def main():
    p=argparse.ArgumentParser()
    for key in ("generator","jet-actions","projection-consumer","sixth-consumer","projection-receipt",
                "seventh-receipt","high-receipt","projection-out","seventh-out","high-out","checkpoint-dir","out"):
        p.add_argument("--"+key,required=True)
    p.add_argument("--remaining-seconds",type=float,default=90)
    p.add_argument("--memory-mib",type=int,default=2048)
    a=p.parse_args()
    require(0<a.remaining_seconds<=180 and 512<=a.memory_mib<=4096,"Finite original eighth probe")
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    start=time.monotonic();a._deadline=start+a.remaining_seconds-min(5,a.remaining_seconds/10)
    rec={"format":FORMAT,"status":"running","events":[],"parameters":{"selfSHA256":sha(__file__),
        "author":"Astra-ISP-789f / normal_annihilator","aiAssisted":"GPT-6 Astra Pro",
        "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,"temporaryOnly":True,
        "allAncestorFilesReadOnly":True,"largeDataUploadedOrCommitted":False,
        "fullEighthRankNotYetClaimed":True,"newPhaseGzipMtime":0,"newPhaseGzipFilename":""}}
    try:
        pins={"generator":GEN_SHA,"jet_actions":ACT_SHA,"projection_consumer":Q_SOURCE_SHA,
            "sixth_consumer":SIX_SOURCE_SHA,"projection_receipt":Q_RECEIPT_SHA,
            "seventh_receipt":SEVEN_RECEIPT_SHA,"high_receipt":HIGH_RECEIPT_SHA}
        for key,d in pins.items():require(sha(getattr(a,key))==d,"Pinned source/input "+key)
        projection=read_result(a.projection_receipt)
        seven=read_result(a.seventh_receipt);high=read_result(a.high_receipt)
        require(projection["status"]=="completed" and
                projection["parameters"]["allOriginal6188PositiveAndRemainingJetProductsZero"] is True,
                "Actual original projected source maps")
        require(seven["status"]=="completed" and seven["parameters"]["binding"]==SEVEN_BINDING and
                seven["parameters"]["fullFirstSevenRanks"]==[4,0,1,3,1,1,1] and
                seven["parameters"]["allEightOrdersAll6188OriginalSourceRowsVerified"] is True,
                "Complete original seventh source domain")
        require(high["status"]=="completed" and
                high["parameters"]["conclusion"]["completeHighQRankExact"]==3760,
                "Actual complete Q high constant rank")
        binding=digest_obj({"format":FORMAT,"sourceSHA256":sha(__file__),"inputSHA256":pins,
            "seventhBinding":SEVEN_BINDING,"highBinding":high["parameters"]["binding"],
            "actualPair":["projected-positive-eight","new-full-seventh-head"],
            "retainedHigherOrders":[6,7],"incomingHigherOrders":[7]})
        rec["parameters"]["binding"]=binding;rec["parameters"]["inputSHA256"]=pins
        require(Path(a.checkpoint_dir).resolve() not in
                (Path(a.projection_out).resolve(),Path(a.seventh_out).resolve(),Path(a.high_out).resolve()),
                "New probe cannot overwrite any ancestor")
        q=mod("r150_infinity_eighth_projection",a.projection_consumer)
        s=mod("r150_infinity_eighth_sixth",a.sixth_consumer)
        m=mod("r150_infinity_eighth_first",a.generator)
        j=mod("r150_infinity_eighth_actions",a.jet_actions)
        data,coeff=original_pair(a,q,s,m,j,projection,seven,rec)
        save_phase(a,q,binding,"complete-two-original-eighth-forcings",data,rec)
        necessity=field_necessary(a,q,m,j,high,coeff,data["high"],rec)
        if isinstance(necessity,tuple):
            info,arrays=necessity
            save_phase(a,q,binding,"complete-paid-high-DAG-new-RHS",arrays,rec)
        else:info=necessity
        rec["parameters"]["highNecessity"]=info
        rec["status"]="completed";rec["outcome"]="actual-original-eighth-high-forcing-inspected"
    except TimeoutError as e:
        rec["status"]="prefix-completed";rec["error"]=str(e)
    except BaseException as e:
        rec["status"]="failed";rec["error"]=type(e).__name__+": "+str(e);raise
    finally:
        rec["elapsedSeconds"]=time.monotonic()-start
        require(len(canonical(rec))<95000,"Small original eighth probe receipt")
        atom(a.out,rec)
        print(json.dumps({"status":rec["status"],"receipt":a.out,"bytes":Path(a.out).stat().st_size,
            "sha256":sha(a.out),"elapsedSeconds":rec["elapsedSeconds"]}),flush=True)
    if rec["status"]=="prefix-completed":raise SystemExit(75)
if __name__=="__main__":main()
