#!/usr/bin/env python3
"""One new ORIGINAL s=2 field11 order, reusing all three paid unit-graph stages.

Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
Date: 2026-11-15.
The original4345 constant DAG and paid L1/L2/L3 are read only.  New A4 and
L4/S4 retain all22 heads and every original6188 source.  A complete finite
Toeplitz kernel, not the individual unit-graph columns, tests all nine
original h0 targets modulo t^5 over F11.  No field target conclusion is
silently promoted to characteristic zero.
"""
import argparse
import hashlib
import importlib.util
import json
from itertools import combinations_with_replacement
from math import comb
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
TWO4_SHA="7b0ec2814a716e236d2dce048d0c8b1b6cea6bca8400e54d846b8e403aa1b7b9"
NATIVE_SHA="dddffc59c5ab8f9fea24954d4e53c3fe30d5a706313c081c8e38cd3fd09c8699"
FIRST_RECEIPT_SHA="aebdd169ec950f7eb4c17b7e9ac4dc30ecb205dfc6a2d9476af9d4d03ebc9d3a"
THREE_RECEIPT_SHA="0d721310db73560427a1c14a59c08853387c9761e117cb0dcaf24951b9aa2ac8"
PROJECTION_SHA="693da6446a6f04cba2c343ea49d9d3466caad1aebd056e91db338163b20d3332"
FIRST_BINDING="f33e3980c2fce162495692f24258b6d32ef00f782d9a1c2817fa054364237f02"
THREE_BINDING="56c8b50a909bf2bb163e80734890bef26d927b5a7b7491e1d7dbb1b74d0dbdb4"
PRIME=11
ORDER=4

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

def prepared(a,g,m,j,two,first,three,binding,result):
    root=Path(a.checkpoint_dir);mp=root/"prepared-series-input.json"
    if mp.exists():
        old=json.loads(mp.read_bytes())
        require(old["binding"]==binding and old["verified"],"Same verified fourth-order input")
        path=root/old["input"]["file"]
        require(path.stat().st_size==old["input"]["bytes"] and
                file_sha(path)==old["input"]["sha256"],"Immutable fourth-order input")
        result["parameters"]["originalPreparation"]=old["metadata"]
        result["parameters"]["originalSeriesInput"]=old["input"]
        return path
    coeff=two.original_at_two(m,j,4)
    phy=three["originalPreparation"]["physicalCoefficientSHA256"]
    require(all(coeff["physical"].get(k)==v for k,v in phy.items()),
            "Every original physical coefficient0..3 prefix retained")
    polys=[[g.polynomial(coeff,k,eq,m) for eq in range(17)] for k in range(5)]
    logical=lambda layers:digest([[[[list(mon),str(v)] for mon,v in eq] for eq in layer]
                                  for layer in layers])
    prefix=logical(polys[:4])
    require(prefix==three["originalPreparation"]["completeRationalThroughThreeSHA256"],
            "ALL17 full rational coefficient0..3 prefixes equal the paid series")
    for layer in polys:
        for eq in layer:
            for mon,value in eq:
                require(1<=len(mon)<=2,"Original equation degree")
                g.modq(value)
    require(any(coeff["pure"][1]),"Original nonzero g'(2) pure coefficient retained")
    targets=[mon for deg in range(5,0,-1) for mon in combinations_with_replacement(range(11),deg)]
    sources=[(eq,mon) for deg in range(4) for eq in range(17)
             for mon in combinations_with_replacement(range(11),deg)]
    require(digest(targets)==first["originalPreparation"]["targetOrderSHA256"]
            and digest(sources)==first["originalPreparation"]["sourceOrderSHA256"],
            "Same complete original monomial dictionaries")
    ix={mon:i for i,mon in enumerate(targets)}
    tmp=root/"original-series-input.bin.tmp"
    with tmp.open("wb") as f:
        f.write(b"R15SJ411");f.write(struct.pack("<5I",11,6188,4367,22,4))
        f.write(binding.encode("ascii"));f.write(FIRST_BINDING.encode("ascii"))
        f.write(THREE_BINDING.encode("ascii"))
        for k in range(5):
            for row,(eq,mult) in enumerate(sources):
                if row%256==0:remaining(a)
                terms={}
                for mon,value in polys[k][eq]:
                    col=ix[tuple(sorted(mon+mult))]
                    terms[col]=(terms.get(col,0)+g.modq(value))%11
                ordered=[(col,v) for col,v in sorted(terms.items()) if v]
                require(len(ordered)<=77,"Original sparse quadratic support")
                f.write(struct.pack("<H",len(ordered)))
                for col,v in ordered:f.write(struct.pack("<HB",col,v))
    sha=file_sha(tmp);path=root/("original-series-input-"+sha+".bin")
    if path.exists():
        require(file_sha(path)==sha,"Immutable fourth-order input collision");tmp.unlink()
    else:os.replace(tmp,path)
    meta={"originalSourceRows":6188,"originalTargetCoordinates":4367,
          "constantHeadColumns":22,"throughOrder":4,
          "allOriginalCoefficient0Through3PrefixesEqualPaid":True,
          "completeRationalPrefixThroughThreeSHA256":prefix,
          "completeRationalThroughFourSHA256":logical(polys),
          "physicalCoefficientSHA256":coeff["physical"],
          "allOriginalParameterDenominatorsUnitsAt11":True,
          "noPrimitiveRowContentDivision":True,
          "originalFirstPureCoefficientRetained":True,
          "gAtTwoCoefficients":[0,-64,-72,-24,-2],
          "sameSourceOrderSHA256":digest(sources),
          "sameTargetOrderSHA256":digest(targets)}
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
    path=root/("schur-four-native-"+NATIVE_SHA);log=root/"series-native-build.log"
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
    require(raw[:8]==b"R15SC411","Original fourth Schur magic")
    require(struct.unpack_from("<4I",raw,8)==(11,1843,22,4),"Original fourth Schur dimensions")
    require(raw[24:88].decode("ascii")==binding,"Original fourth Schur binding")
    rows=list(struct.unpack_from("<1843H",raw,88));offset=88+2*1843
    require(rows==sorted(set(rows)) and all(r<6188 for r in rows),"Original dependent source dictionary")
    count=1843*22
    require(len(raw)==offset+5*count,"Every original Schur coefficient retained")
    seq=[]
    for k in range(5):
        b=raw[offset+k*count:offset+(k+1)*count]
        require(all(v<11 for v in b),"Schur field coordinates")
        seq.append(nmod_mat(1843,22,list(b),11))
    require(matrix_zero(seq[0]),"Full constant Schur zero")
    return seq,rows

def read_unit_graph(path,binding):
    raw=Path(path).read_bytes()
    require(raw[:8]==b"R15LC411" and
            struct.unpack_from("<4I",raw,8)==(11,4367,22,4),
            "Complete original fourth unit graph")
    require(raw[24:88].decode("ascii")==binding,"Original unit graph binding")
    count=4367*22
    require(len(raw)==88+5*count,"Full original graph EOF")
    seq=[]
    for k in range(5):
        b=raw[88+k*count:88+(k+1)*count]
        require(all(v<11 for v in b),"Original unit graph field coordinates")
        seq.append(nmod_mat(4367,22,list(b),11))
    return seq

def h0_at_two_coefficients(order):
    """Exact integer Taylor coefficients of the actual original h0."""
    def taylor(coef):
        return [sum(coef[k]*comb(k,j)*2**(k-j) for k in range(j,len(coef)))
                for j in range(order+1)]
    def mul(a,b):
        return [sum(a[i]*b[k-i] for i in range(k+1)) for k in range(order+1)]
    factors=[[0,0,0,1],[-2,1],
             [-8,32,-25,5],[-8,32,-25,5],
             [864,864,135,5],[864,864,135,5],
             [9600,-25472,-3392,15936,-2888,-936,153,50,5]]
    out=[1]+[0]*order
    for factor in factors:out=mul(out,taylor(factor))
    require(out[0]==0 and out[1]==17886115659776,"Original h0 at2 has its true first coefficient")
    return out

def complete_target_pairing(a,S,L,binding,out,result):
    """All original left kernels modulo t^5, expressed in the full unit graph."""
    remaining(a)
    require(len(S)==5 and len(L)==5 and matrix_zero(S[0]),"Paid full original graph through4")
    M=nmod_mat(4*1843,4*22,[0]*(4*1843*4*22),11)
    for k in range(1,5):
        for i in range(1,k+1):
            for r in range(1843):
                for c in range(22):
                    M[(k-1)*1843+r,(k-i)*22+c]=S[i][r,c]
        remaining(a)
    RR,rk=M.rref();pc=pivots(RR,rk);used=set(pc)
    fc=[c for c in range(88) if c not in used]
    K=nmod_mat(88,len(fc),[0]*(88*len(fc)),11)
    for j,c in enumerate(fc):
        K[c,j]=1
        for i,p in enumerate(pc):K[p,j]=-RR[i,c]
    require(matrix_zero(M*K),"COMPLETE original Schur Toeplitz kernel")
    require(block(K,fc,list(range(len(fc))))==identity(len(fc)),
            "Complete Toeplitz free coordinate normalization")
    E=[block(K,list(range(22*k,22*(k+1))),list(range(len(fc)))) for k in range(4)]
    E.append(nmod_mat(22,len(fc),[0]*(22*len(fc)),11))
    count=0
    for k in range(5):
        prod=nmod_mat(1843,len(fc),[0]*(1843*len(fc)),11)
        for i in range(k+1):prod+=S[i]*E[k-i]
        require(matrix_zero(prod),"Every dependent original source in complete kernel composition")
        count+=1843*len(fc)
    targets=[mon for deg in range(5,0,-1)
             for mon in combinations_with_replacement(range(11),deg)]
    ix={mon:i for i,mon in enumerate(targets)}
    squares=[ix[(j,j)] for j in range(2,11)]
    low=[block(X,squares,list(range(22))) for X in L]
    require(matrix_zero(low[0]),"All22 true original constant heads kill the nine squares")
    for j in range(2,11):
        for b in range(j+1):
            actual=sum(comb(j,a)*comb(a,b)*(-1)**(j-a) for a in range(b,j+1))
            require(actual==int(b==j),"Actual original binomial target transport to n_j squared")
    Q=[]
    for k in range(5):
        read=nmod_mat(9,len(fc),[0]*(9*len(fc)),11)
        for i in range(k+1):read+=low[i]*E[k-i]
        Q.append(read)
    h=h0_at_two_coefficients(4)
    H=[]
    for k in range(5):
        read=nmod_mat(9,len(fc),[0]*(9*len(fc)),11)
        for i in range(k+1):
            scalar=h[i]%11
            if scalar:
                read+=nmod_mat(9,len(fc),[(int(Q[k-i][r,c])*scalar)%11
                                         for r in range(9) for c in range(len(fc))],11)
        H.append(read)
    require(matrix_zero(H[0]),"Actual h0 has zero constant term")
    allzero=all(matrix_zero(X) for X in H)
    first=None
    for k,X in enumerate(H):
        for i in range(9):
            for j in range(len(fc)):
                if X[i,j] and first is None:
                    first={"order":k,"target":i+2,"kernelColumn":j,"valueModulo11":int(X[i,j])}
    kernel_path=Path(out)/("complete-left-toeplitz-kernel-"+binding+".bin")
    payload=struct.pack("<3I",11,88,len(fc))+bytes(int(K[i,j]) for i in range(88) for j in range(len(fc)))
    tmp=kernel_path.with_name(kernel_path.name+".tmp")
    tmp.write_bytes(payload);os.replace(tmp,kernel_path)
    result["parameters"]["completeOriginalFieldTargetPairing"]={
        "ring":"F11[t]/(t^5)","allOriginalSources":6188,"allOriginalTargets":4367,
        "toeplitzShape":[4*1843,88],"toeplitzRank":rk,
        "toeplitzSHA256":mat_hash(M),"completeKernelColumns":len(fc),
        "completeKernelSHA256":mat_hash(K),"temporaryKernel":descriptor(kernel_path),
        "omittedButRetainedFinalCoefficientFreeDimensions":22,
        "completeLeftKernelF11Dimension":len(fc)+22,
        "all22LastFreeCoefficientsHaveZeroNineTargetReadings":True,
        "allToeplitzKernelProductsVerified":True,
        "allRemainingOriginalSourceConvolutionsVerified":True,
        "verifiedResidualProductCoordinates":count,
        "fullOriginalProductsFollowFromPaidUnitGraphAndVerifiedComposition":True,
        "unitGraphColumnsNotMistakenForKernelCochains":True,
        "originalNineBinomialSquaresTransportVerified":True,
        "h0ExactTaylorCoefficients":[str(v) for v in h],
        "squarePairingCoefficientSHA256":[mat_hash(X) for X in Q],
        "h0PairingCoefficientSHA256":[mat_hash(X) for X in H],
        "allNineH0PairingsZeroModuloT5":allzero,
        "firstNonzeroH0Pairing":first,
        "h0PairingLastCoefficientRows":[[int(H[4][i,j]) for j in range(len(fc))] for i in range(9)],
        "allNineH0TargetsInFullOriginalFieldImageModuloT5":allzero,
        "membershipUsesCompleteDoubleAnnihilatorOverTruncatedFieldDVR":True,
        "noCharacteristicZeroTargetMembershipInferredFromFieldPairing":True}
    return allzero

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
    ap.add_argument("--two-four-generator",required=True)
    ap.add_argument("--native-source",required=True)
    ap.add_argument("--first-receipt",required=True)
    ap.add_argument("--parent-receipt",required=True)
    ap.add_argument("--projection-receipt",required=True)
    ap.add_argument("--first-checkpoint-dir",required=True)
    ap.add_argument("--parent-checkpoint-dir",required=True)
    ap.add_argument("--checkpoint-dir",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--remaining-seconds",type=float,default=180)
    ap.add_argument("--memory-mib",type=int,default=2048)
    ap.add_argument("--cxx",default="c++")
    a=ap.parse_args();start=time.monotonic();a._deadline=start+a.remaining_seconds
    require(a.remaining_seconds>0 and a.memory_mib>=512,"Finite shared resources")
    soft,hard=resource.getrlimit(resource.RLIMIT_AS);limit=a.memory_mib*1024*1024
    if hard!=resource.RLIM_INFINITY:limit=min(limit,hard)
    resource.setrlimit(resource.RLIMIT_AS,(limit,hard))
    root=Path(a.checkpoint_dir);root.mkdir(parents=True,exist_ok=True)
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    result={"format":"r150-two-full-original-schur-four-and-targets-field11-receipt-v1",
            "status":"running","parameters":{},"events":[]};status=0
    try:
        pins={"firstDriver":(a.first_driver,FIRST_DRIVER_SHA),
              "firstNativeSource":(a.first_native_source,FIRST_NATIVE_SHA),
              "generator":(a.generator,GEN_SHA),"actions":(a.actions,ACT_SHA),
              "originalTwoFourGenerator":(a.two_four_generator,TWO4_SHA),
              "nativeSource":(a.native_source,NATIVE_SHA),
              "firstReceipt":(a.first_receipt,FIRST_RECEIPT_SHA),
              "paidThroughThreeReceipt":(a.parent_receipt,THREE_RECEIPT_SHA),
              "projectionReceipt":(a.projection_receipt,PROJECTION_SHA)}
        actual={}
        for name,(path,expected) in pins.items():
            actual[name]=file_sha(path);require(actual[name]==expected,"Pinned input "+name)
        fo=json.loads(Path(a.first_receipt).read_bytes())
        po=json.loads(Path(a.parent_receipt).read_bytes())
        qo=json.loads(Path(a.projection_receipt).read_bytes())
        for obj in (fo,po,qo):
            require(obj["exitCode"]==0 and obj["result"]["status"]=="completed",
                    "Only actually completed ancestor receipts")
        first=fo["result"]["parameters"];three=po["result"]["parameters"]
        qp=qo["result"]["parameters"]
        require(first["binding"]==FIRST_BINDING and
                first["nativeResult"]["constantRank"]==4345 and
                first["nativeResult"]["completeFirstConnectionRank"]==7,
                "Same actual original first connection")
        require(three["binding"]==THREE_BINDING and
                three["parentBinding"]==FIRST_BINDING and
                three["nativeResult"]["allOriginalResidualIdentitiesVerified"] and
                three["nativeResult"]["throughOrder"]==3,
                "All original paid three-stage identities")
        require(qp["projectedTorsionLengthExact"]==12 and
                qp["projectionGenericRankReached"] and
                qp["all6188OriginalProjectedSourcesRetained"] and
                qp["localGenerationBothDirectionsVerified"],
                "Same original true Q projected length12")
        firstroot=Path(a.first_checkpoint_dir);paidroot=Path(a.parent_checkpoint_dir)
        old_input=firstroot/first["originalInput"]["file"]
        oldfiles={"originalInput":(old_input,first["originalInput"])}
        for name in ("constant-normalized-pivot-rows.bin",
                     "constant-source-row-operations.bin",
                     "field-complete-connection-residual.bin"):
            oldfiles[name]=(firstroot/"native-result"/name,first["temporaryNativeFiles"][name])
        for name,(path,item) in oldfiles.items():
            require(path.stat().st_size==item["bytes"] and file_sha(path)==item["sha256"],
                    "Actual first-stage temporary file "+name)
        paidstages={}
        for k in range(1,4):
            name="original-unit-graph-order"+str(k)+"-"+THREE_BINDING+".bin"
            item=three["temporaryNativeFiles"][name];path=paidroot/"native-result"/name
            require(path.stat().st_size==item["bytes"] and file_sha(path)==item["sha256"],
                    "Actual verified paid order"+str(k)+" reused without recomputing")
            paidstages[name]=item
        selfsha=file_sha(__file__)
        binding=digest({"format":"r150-original-full-field11-fourth-child-binding-v1",
                        "selfSHA256":selfsha,"inputSHA256":actual,
                        "firstBinding":FIRST_BINDING,"paidThroughThreeBinding":THREE_BINDING,
                        "firstTemporaryFiles":{n:v[1] for n,v in oldfiles.items()},
                        "paidOriginalUnitStages":paidstages,"prime":11,"order":4})
        result["parameters"].update({
            "binding":binding,"selfSHA256":selfsha,"inputSHA256":actual,
            "firstBinding":FIRST_BINDING,"paidThroughThreeBinding":THREE_BINDING,
            "firstExecutionSource":fo["executionSourceCommit"],
            "parentExecutionSource":po["executionSourceCommit"],
            "paidOriginalUnitStages":paidstages,
            "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
            "constantGaussianEliminationRepeated":False,
            "paidFirstThreeUnitSolvesRepeated":False,
            "all22OriginalHeadsRetained":True,
            "allMatricesTemporary":True,"noLargeRecomputableDataUploaded":True,
            "paidTrueQProjectedLength":12,
            "paidFullConstantRank":4345,"paidFullGenericRankOverQ":4354})
        g=module_at("r150_first_driver_for_four",a.first_driver)
        m=module_at("r150_physical_generator_for_four",a.generator)
        j=module_at("r150_original_actions_for_four",a.actions)
        two=module_at("r150_original_two_four",a.two_four_generator)
        path=prepared(a,g,m,j,two,first,three,binding,result)
        binary=native_binary(a,binding,result)
        nd=root/"native-result";nd.mkdir(exist_ok=True)
        nr=nd/"native-original-schur-through-four-receipt.json"
        if nr.exists():
            native=json.loads(nr.read_bytes())
            require(native["status"]=="completed" and native["binding"]==binding,
                    "Same completed new native stage")
        else:
            seconds=max(.001,remaining(a)-min(8.0,remaining(a)/10))
            cmd=[str(binary.resolve()),str(path.resolve()),str(old_input.resolve()),
                 str(oldfiles["constant-normalized-pivot-rows.bin"][0].resolve()),
                 str(oldfiles["constant-source-row-operations.bin"][0].resolve()),
                 str(oldfiles["field-complete-connection-residual.bin"][0].resolve()),
                 str((paidroot/"native-result").resolve()),str(nd.resolve()),repr(seconds)]
            with (root/"native-series-stdout.json").open("wb") as stdout, \
                 (root/"native-series-stderr.log").open("wb") as stderr:
                p=subprocess.run(cmd,stdout=stdout,stderr=stderr,timeout=remaining(a),check=False)
            result["parameters"]["nativeExitCode"]=p.returncode
            require(p.returncode==0 and nr.exists(),"New fourth order incomplete; no conclusion")
            native=json.loads(nr.read_bytes())
        require(native["binding"]==binding and native["parentBinding"]==FIRST_BINDING and
                native["paidThroughThreeBinding"]==THREE_BINDING and
                native["throughOrder"]==4 and
                native["allOriginalResidualIdentitiesVerified"] and
                native["paidOrdersOneThroughThreeReused"] and
                native["onlyOrderFourNewlySolved"] and
                native["allFirstSchurEntriesEqualPaidResidual"] and
                native["unitSourceResidualsAllZero"],
                "One new actual order with all paid original stages retained")
        result["parameters"]["nativeResult"]=native
        files=[nr,nd/"complete-original-schur-through-four.bin",
               nd/"complete-original-unit-graph-through-four.bin"]
        files+=sorted(nd.glob("original-unit-graph-order*-"+binding+".bin"))
        result["parameters"]["temporaryNativeFiles"]={p.name:descriptor(p) for p in files}
        seq,rows=read_schur(nd/"complete-original-schur-through-four.bin",binding)
        exponents,covered=complete_small_smith(a,seq,rows,result)
        require(exponents[:7]==[1]*7,"Same complete first connection seven")
        complete=(covered==9);length=sum(exponents) if complete else None
        if complete:require(length>=12,"Field bound cannot contradict actual true Q projection12")
        L=read_unit_graph(nd/"complete-original-unit-graph-through-four.bin",binding)
        complete_target_pairing(a,seq,L,binding,out,result)
        result["parameters"]["conclusion"]={
            "fullFieldGenericRankReached":complete,
            "fullFieldPositiveSmithExponentsExact":exponents if complete else None,
            "fullFieldLocalTorsionLengthExact":length,
            "fullFieldFreeRank":13 if complete else None,
            "fullCharacteristicZeroLocalLengthInterval":[12,length] if complete else None,
            "fullCharacteristicZeroLocalLengthExact":12 if length==12 else None,
            "sameOriginalWQuotientLengthUpperBound":length-12 if complete else None,
            "wholeOriginalWLocallyInSourceOverQ":True if length==12 else None,
            "allNineH0TargetsLocallyInSourceOverQ":True if complete and length<=13 else None,
            "onlyLengthComparisonMayImplyQMembershipNotFieldPairing":True,
            "fieldPositiveLengthNotAutomaticallyCalledQEquality":True,
            "noOtherFinitePointOrGlobalPolynomialMembershipClaim":True}
        result["status"]="completed"
    except (TimeoutError,subprocess.TimeoutExpired) as exc:
        result["status"]="budget-paused";result["error"]=str(exc);status=124
    except Exception as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc);status=1
    finally:
        result["elapsedSeconds"]=time.monotonic()-start
        require(len(canonical(result))<85000,"Small source and parameter receipt")
        atomic_json(out/"two-full-original-schur-four-and-targets-field11-receipt.json",result)
        print(canonical(result).decode("ascii"),flush=True)
    return status

if __name__=="__main__":raise SystemExit(main())
