#!/usr/bin/env python3
"""R150: one original right-kernel Bockstein closes the outside gcd.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15 UTC.
Read only the 21 paid first-precision operations from the whole SHA-bound
large checkpoint; never decode its f**2 matrix. Reconstruct only the selected
21x21 unit, using exactly the paid pivot order and inverses. Solve two single
right-hand sides. Check Ax=fE and (E-Ay) mod f on all 56 original rows.
For squarefree f, residue corank one, and the actual upper f**2, the exact
outside maximal-minor gcd is f*gcd(f, every Bockstein residual).
All arrays are temporary; only the small receipt is publishable.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time
from flint import fmpq_poly

FORMAT="r150-original56-single-kernel-bockstein-v1"
LOWER_SOURCE={"bytes":29457,"sha256":"0e111c2334bf62e4b4404d84c8af5e9f62ee99a6b64f766bad541c126b1e7fa4"}
OLD_BINDING="862cca4d82af7c8031de01117b2f18516c0d3622a73b4e794c4f3280a0fe9850"
OLD_RAW={"bytes":6043,"sha256":"26917bb0ac3058ce08c57b18f91bca119b42ad866c4264e98ad9d4a02a7382cc"}
OLD_STATE={"file":"state-slot-1.json.gz","bytes":177991821,
 "sha256":"068922367edfca1458b0bd729d16b1a092ecd53f7c3de306cbaa4439f38b462c",
 "payloadSHA256":"669cddad863f7873b4b847ace1ef50af4e11647cba015a9958526404f04f30d0"}
FACTOR_SHA="c2e27cf7e732257b695a6fa655f24b2305fd817a779baa3965a2eccc5f663dc2"
ZERO=fmpq_poly([])
ONE=fmpq_poly([1])
STOP=False
DEADLINE=float("inf")

class BudgetStop(Exception):
    pass

def require(condition,message):
    if not condition:
        raise AssertionError(message)

def tick():
    if STOP or time.monotonic()>=DEADLINE:
        raise BudgetStop("Only a whole completed phase or row batch was committed")

def canonical(obj):
    return json.dumps(obj,sort_keys=True,ensure_ascii=True,separators=(",",":")).encode("ascii")

def digest(data):
    return hashlib.sha256(data).hexdigest()

def file_id(path):
    h=hashlib.sha256(); n=0
    with Path(path).open("rb") as stream:
        for data in iter(lambda:stream.read(1<<20),b""):
            h.update(data);n+=len(data)
    return {"bytes":n,"sha256":h.hexdigest()}

def atomic_bytes(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".pending-"+str(os.getpid()))
    with temporary.open("wb") as stream:
        stream.write(data);stream.flush();os.fsync(stream.fileno())
    os.replace(temporary,path)

def atomic_json(path,obj):
    atomic_bytes(path,canonical(obj))

def save_gzip(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    data=canonical(obj);temporary=path.with_name(path.name+".pending-"+str(os.getpid()))
    with temporary.open("wb") as stream:
        with gzip.GzipFile(filename="",fileobj=stream,mode="wb",compresslevel=1,mtime=0) as z:
            z.write(data)
        stream.flush();os.fsync(stream.fileno())
    os.replace(temporary,path)
    return dict(file_id(path),file=path.name,payloadSHA256=digest(data),temporaryOnly=True)

def load_gzip(path,pin):
    require(file_id(path)=={"bytes":pin["bytes"],"sha256":pin["sha256"]},
            "Whole temporary file bytes and SHA256")
    with gzip.open(path,"rb") as stream:
        data=stream.read()
    require(digest(data)==pin["payloadSHA256"],"Whole temporary payload SHA256")
    return json.loads(data)

def encp(poly):
    return {"n":[str(x) for x in poly.numer().coeffs()],"d":str(poly.denom())}

def decp(obj):
    return fmpq_poly([int(x) for x in obj["n"]],int(obj["d"]))

def encv(vector):
    return [encp(x) for x in vector]

def decv(vector):
    return [decp(x) for x in vector]

def encm(matrix):
    return [encv(row) for row in matrix]

def decm(matrix):
    return [decv(row) for row in matrix]

def monic(poly):
    require(bool(poly),"Nonzero polynomial to monic")
    return poly/poly.leading_coefficient()

def exact_division(a,b):
    quotient,remainder=divmod(a,b)
    require(not remainder and quotient*b==a,"Exact original polynomial division")
    return quotient

def pstats(poly):
    return {"degree":int(poly.degree()),
            "numeratorMaximumBits":int(poly.numer().height_bits()),
            "denominatorBits":abs(int(poly.denom())).bit_length(),
            "coefficientSHA256":digest(canonical(encp(poly)))}

def safe_summary(state):
    return {"generation":state["generation"],"stage":state["stage"],
            "completedUnitPivots":state.get("completedUnitPivots",0),
            "completedOriginalKernelRows":state.get("completedOriginalKernelRows",0),
            "completedOriginalBocksteinRows":state.get("completedOriginalBocksteinRows",0),
            "unitSchurCoordinateProducts":state.get("unitSchurCoordinateProducts",0),
            "unitRightHandSideProducts":state.get("unitRightHandSideProducts",0),
            "completeOriginalOutsideGcdComputed":state.get("stage")=="completed"}

class Checkpoints:
    def __init__(self,root,binding):
        self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True)
        self.binding=binding;self.pointer=self.root/"checkpoint-pointer.json"
    def load(self):
        if not self.pointer.exists():
            return None
        pointer=json.loads(self.pointer.read_text())
        require(pointer["format"]==FORMAT and pointer["binding"]==self.binding,
                "Same source and immutable inputs for continuation")
        obj=load_gzip(self.root/pointer["record"]["file"],pointer["record"])
        require(obj["format"]==FORMAT and obj["binding"]==self.binding,
                "Whole checkpoint semantic binding")
        require(obj["state"]["generation"]==pointer["generation"],"Checkpoint generation")
        return obj["state"]
    def save(self,state):
        pin=save_gzip(self.root/("state-slot-"+str(state["generation"]%2)+".json.gz"),
                      {"format":FORMAT,"binding":self.binding,"state":state})
        pointer={"format":FORMAT,"binding":self.binding,"generation":state["generation"],
                 "record":pin,"summary":safe_summary(state)}
        atomic_json(self.pointer,pointer)
        return pointer
    def phase(self,name,data):
        return save_gzip(self.root/(name+".json.gz"),
                         {"format":FORMAT,"binding":self.binding,"data":data})
    def read_phase(self,pin):
        obj=load_gzip(self.root/pin["file"],pin)
        require(obj["format"]==FORMAT and obj["binding"]==self.binding,"Phase binding")
        return obj["data"]

def stream_paid_profile(path):
    """Hash every decompressed byte, but JSON-decode only the first 21 operations."""
    require(file_id(path)=={"bytes":OLD_STATE["bytes"],"sha256":OLD_STATE["sha256"]},
            "Actual whole failed-replay checkpoint SHA before profile extraction")
    needle=b'"operations":['
    rawhash=hashlib.sha256();tail=b"";marker_count=0
    buffer="";found=False;finished=False;operations=[];decoder=json.JSONDecoder()
    with gzip.open(path,"rb") as stream:
        while True:
            tick()
            data=stream.read(1<<20)
            if not data:
                break
            rawhash.update(data)
            scan=tail+data;marker_count+=scan.count(needle)
            if not found:
                position=scan.find(needle)
                if position>=0:
                    found=True;buffer=scan[position+len(needle):].decode("ascii")
            elif not finished:
                buffer+=data.decode("ascii")
            tail=scan[-(len(needle)-1):]
            if found and not finished:
                while len(operations)<21:
                    buffer=buffer.lstrip(" \t\r\n,")
                    if not buffer:
                        break
                    require(buffer[0]=="{","Next paid operation is an object")
                    try:
                        obj,end=decoder.raw_decode(buffer)
                    except json.JSONDecodeError:
                        break
                    require(obj.get("kind")=="unit" and obj.get("mode")=="profile"
                            and obj.get("precision")==1,
                            "Only the 21 completed original first-precision unit operations")
                    require(obj.get("unitInverseVerified") is True
                            and obj.get("allRetainedRowsVerified") is True,
                            "Paid complete original-row checks")
                    operations.append({key:obj[key] for key in
                        ("kind","mode","precision","position","originalRow","originalColumn",
                         "factor","pivot","inverse","beforeSHA256","afterSHA256")})
                    buffer=buffer[end:]
                if len(operations)==21:
                    finished=True;buffer=""
                else:
                    require(len(buffer)<128*1024**2,
                            "Bounded profile parser; the large matrix is never decoded")
    require(rawhash.hexdigest()==OLD_STATE["payloadSHA256"],
            "Every decompressed checkpoint byte matches the paid payload SHA256")
    require(marker_count==1 and len(operations)==21,
            "Unique retained branch and all 21 paid unit operations")
    return operations

def extract_profile(args,f):
    raw=Path(args.profile_out)/"complete-original56-outside-gcd-receipt.json"
    require(file_id(raw)==OLD_RAW,"Exact actual MemoryError raw receipt")
    paid=json.loads(raw.read_text())
    require(paid["binding"]==OLD_BINDING and paid["status"]=="failed"
            and paid["error"]["type"]=="MemoryError",
            "Actual failed replay, not an invented success or timeout")
    last=paid["parameters"]["lastWholeCheckpoint"]
    require(last["binding"]==OLD_BINDING and last["generation"]==27,
            "Last whole saved replay generation 27")
    require(all(last["record"][key]==value for key,value in OLD_STATE.items()),
            "Exact retained state file")
    summary=last["summary"]
    require(summary["splitCount"]==0 and summary["closedBranchCount"]==0
            and summary["pendingBranchCount"]==1,"One complete squarefree support branch")
    branch=summary["pendingBranches"][0]
    require(branch["profilePivots"]==21 and branch["mode"]=="replay"
            and branch["precision"]==2 and branch["replayedPivots"]==5,
            "Completed residue rank21, incomplete precision-two replay")
    operations=stream_paid_profile(Path(args.profile_out)/"checkpoints"/OLD_STATE["file"])
    rows=list(range(56));columns=list(range(22));chosen_rows=[];chosen_columns=[]
    previous_after=None
    for number,op in enumerate(operations):
        tick()
        require(decp(op["factor"])==f,"The same exact monic squarefree factor")
        rr,cc=op["position"]
        require(0<=rr<len(rows) and 0<=cc<len(columns),"Paid shrinking row/column position")
        rows[0],rows[rr]=rows[rr],rows[0]
        columns[0],columns[cc]=columns[cc],columns[0]
        require(rows[0]==op["originalRow"] and columns[0]==op["originalColumn"],
                "Paid original row and column identities")
        if previous_after is not None:
            require(op["beforeSHA256"]==previous_after,"Whole paid profile hash chain")
        previous_after=op["afterSHA256"]
        pivot=decp(op["pivot"]);inverse=decp(op["inverse"])
        require((pivot*inverse)%f==ONE,"Each paid inverse is a true unit modulo the whole f")
        chosen_rows.append(rows.pop(0));chosen_columns.append(columns.pop(0))
    require(len(rows)==35 and len(columns)==1 and len(set(chosen_rows))==21
            and len(set(chosen_columns))==21,"Complete original rank21/corank1 profile")
    return {"operations":operations,"originalUnitRows":chosen_rows,
            "originalUnitColumns":chosen_columns,"originalFreeColumn":columns[0],
            "originalNonUnitRows":rows,"paidRaw":OLD_RAW,"paidState":OLD_STATE,
            "oldBinding":OLD_BINDING,"entireOldPayloadHashed":True,
            "oldPrecisionTwoMatrixDecoded":False}

def one_unit_step(matrix,pivot,inverse,f):
    require(matrix and len(matrix)==len(matrix[0]),"Actual retained square unit")
    require(matrix[0][0]==pivot,"Selected original square reproduces the exact paid pivot")
    require((pivot*inverse)%f==ONE,"Paid inverse rechecked in the whole squarefree ring")
    normalized=[(inverse*x)%f for x in matrix[0]]
    require(normalized[0]==ONE,"Normalized selected pivot row")
    lower=[row[0] for row in matrix]
    smaller=[];checks=0
    for i in range(1,len(matrix)):
        tick();row=[]
        for j in range(1,len(matrix)):
            value=(matrix[i][j]-lower[i]*normalized[j])%f
            require((value+lower[i]*normalized[j]-matrix[i][j])%f==ZERO,
                    "Each selected original-unit Schur coordinate")
            row.append(value);checks+=1
        smaller.append(row)
    return smaller,lower,normalized,checks

def solve_triangular(lower,upper,inverses,right,f):
    n=len(lower);require(len(right)==n,"Single unit right-hand side")
    mid=[];answer=[ZERO for _ in range(n)]
    for i in range(n):
        tick();value=right[i]
        for j in range(i):
            value-=lower[i][j]*mid[j]
        mid.append((value*inverses[i])%f)
    for i in range(n-1,-1,-1):
        tick();value=mid[i]
        for j in range(i+1,n):
            value-=upper[i][j]*answer[j]
        answer[i]=value%f
    return answer

def original_product(row,vector):
    value=ZERO
    for coefficient,entry in zip(row,vector):
        if coefficient and entry:
            value+=coefficient*entry
    return value

def verify_unit_rhs(A,profile,answer,right,f):
    for i,rawrow in enumerate(profile["originalUnitRows"]):
        tick()
        value=ZERO
        for j,rawcolumn in enumerate(profile["originalUnitColumns"]):
            value+=A[rawrow][rawcolumn]*answer[j]
        require((value-right[i])%f==ZERO,"All 21 original unit rows for this actual right-hand side")
    return 21

def tiny_verification():
    x=fmpq_poly([0,1]);f=x*x-1
    examples=[
        [[ONE+f,x],[ZERO,f*(x-1)],[f,f*x]],
        [[ONE+f,x],[ZERO,f*f],[f,f*x]]
    ]
    results=[]
    for A in examples:
        pivot=A[0][0]%f;g,a,b=pivot.xgcd(f)
        require(a*pivot+b*f==g and int(g.degree())==0,"Tiny true unit")
        inv=(a/g[0])%f
        xv=[(-inv*A[0][1])%f,ONE]
        E=[exact_division(original_product(row,xv),f) for row in A]
        y=[(inv*E[0])%f,ZERO]
        residual=[(E[i]-original_product(row,y))%f for i,row in enumerate(A)]
        support=f
        for value in residual:
            support=monic(support.gcd(value))
        calculated=monic(f*support);independent=ZERO
        for i,j in ((0,1),(0,2),(1,2)):
            minor=A[i][0]*A[j][1]-A[i][1]*A[j][0]
            independent=minor if not independent else independent.gcd(minor)
        require(calculated==monic(independent),"Independent gcd of all three tiny maximal minors")
        require(bool(E[0]) and bool(y[0]),"Tiny check has genuine nonzero second right-hand side")
        results.append(int(calculated.degree()))
    require(results==[3,4],"Both mixed exponents1/2 and identically zero Bockstein tested")
    return {"allTinyOriginalProductsVerified":True,
            "independentAllMinorGcdDegrees":results,"nonzeroCorrectionVerified":True,
            "mixedSquarefreeSupportVerified":True,"zeroBocksteinVerified":True}

def load_inputs(args):
    require(file_id(args.lower_source)==LOWER_SOURCE,"Exact frozen original56 local source")
    spec=importlib.util.spec_from_file_location("paid_original56_local",args.lower_source)
    old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old);old.tick=tick
    A,U,meta=old.load_inputs(args)
    groups=old.squarefree_groups(U)
    require(len(groups)==1 and groups[0][1]==2 and int(groups[0][0].degree())==60,
            "Actual degree120 upper equals one squarefree degree60 support squared")
    f=groups[0][0]
    require(digest(canonical(encp(f)))==FACTOR_SHA and U==f*f,
            "Same actual factor and exact upper, without irreducibility assumption")
    require(len(A)==56 and all(len(row)==22 for row in A),"All original56 by22 coordinates")
    return A,U,f,meta

def execute(args,cp,state,A,U,f,rec):
    if state is None:
        profile=extract_profile(args,f)
        profile_pin=cp.phase("paid-first-precision-profile",profile)
        matrix=[[A[r][c]%f for c in profile["originalUnitColumns"]]
                for r in profile["originalUnitRows"]]
        zero=[[ZERO for _ in range(21)] for _ in range(21)]
        state={"generation":0,"stage":"unit-factorization","profile":profile_pin,
               "completedUnitPivots":0,"unitSchurCoordinateProducts":0,
               "matrix":encm(matrix),"lower":encm(zero),"upper":encm(zero)}
        cp.save(state)
    profile=cp.read_phase(state["profile"])
    require(len(profile["operations"])==21,"Saved exact original profile")
    operations=profile["operations"]
    if state["stage"]=="unit-factorization":
        matrix=decm(state["matrix"]);lower=decm(state["lower"]);upper=decm(state["upper"])
        for k in range(state["completedUnitPivots"],21):
            tick()
            pivot=decp(operations[k]["pivot"]);inverse=decp(operations[k]["inverse"])
            smaller,column,row,checks=one_unit_step(matrix,pivot,inverse,f)
            next_lower=[list(r) for r in lower];next_upper=[list(r) for r in upper]
            for i,value in enumerate(column):
                next_lower[k+i][k]=value
            for j,value in enumerate(row):
                next_upper[k][k+j]=value
            next_state=dict(state)
            next_state.update(generation=state["generation"]+1,completedUnitPivots=k+1,
                unitSchurCoordinateProducts=state["unitSchurCoordinateProducts"]+checks,
                matrix=encm(smaller),lower=encm(next_lower),upper=encm(next_upper))
            cp.save(next_state)
            state=next_state;matrix=smaller;lower=next_lower;upper=next_upper
        require(not matrix and state["unitSchurCoordinateProducts"]==2870,
                "All 21 original pivots and all 2870 square Schur coordinates completed")
        pin=cp.phase("complete-original-unit-triangular-factor",
            {"lower":encm(lower),"upper":encm(upper),
             "all21PaidPivotsReproduced":True,"coordinateProducts":2870})
        state={key:value for key,value in state.items() if key not in ("matrix","lower","upper")}
        state.update(generation=state["generation"]+1,stage="right-kernel",factor=pin)
        cp.save(state)
    factor=None
    if state["stage"] in ("right-kernel","unit-correction"):
        factor=cp.read_phase(state["factor"])
    if state["stage"]=="right-kernel":
        lower=decm(factor["lower"]);upper=decm(factor["upper"])
        inverse=[decp(op["inverse"]) for op in operations]
        free=profile["originalFreeColumn"]
        right=[(-A[r][free])%f for r in profile["originalUnitRows"]]
        answer=solve_triangular(lower,upper,inverse,right,f)
        checks=verify_unit_rhs(A,profile,answer,right,f)
        vector=[ZERO for _ in range(22)];vector[free]=ONE
        for rawcolumn,value in zip(profile["originalUnitColumns"],answer):
            vector[rawcolumn]=value
        state=dict(state);state.update(generation=state["generation"]+1,stage="kernel-products",
            rightKernel=encv(vector),firstQuotient=[],completedOriginalKernelRows=0,
            unitRightHandSideProducts=checks)
        cp.save(state)
    if state["stage"]=="kernel-products":
        vector=decv(state["rightKernel"])
        while state["completedOriginalKernelRows"]<56:
            quotient=decv(state["firstQuotient"]);start=state["completedOriginalKernelRows"]
            for i in range(start,min(start+4,56)):
                tick()
                product=original_product(A[i],vector)
                entry=exact_division(product,f)
                require(f*entry==product,"Every one of the 56 original Ax=fE identities")
                quotient.append(entry)
            next_state=dict(state)
            next_state.update(generation=state["generation"]+1,firstQuotient=encv(quotient),
                              completedOriginalKernelRows=len(quotient))
            cp.save(next_state);state=next_state
        state=dict(state);state.update(generation=state["generation"]+1,stage="unit-correction")
        cp.save(state)
    if state["stage"]=="unit-correction":
        if factor is None:
            factor=cp.read_phase(state["factor"])
        lower=decm(factor["lower"]);upper=decm(factor["upper"])
        inverse=[decp(op["inverse"]) for op in operations]
        E=decv(state["firstQuotient"])
        right=[E[r]%f for r in profile["originalUnitRows"]]
        answer=solve_triangular(lower,upper,inverse,right,f)
        checks=verify_unit_rhs(A,profile,answer,right,f)
        vector=[ZERO for _ in range(22)]
        for rawcolumn,value in zip(profile["originalUnitColumns"],answer):
            vector[rawcolumn]=value
        require(not vector[profile["originalFreeColumn"]],"Correction has exactly zero free coordinate")
        state=dict(state);state.update(generation=state["generation"]+1,stage="bockstein-products",
            correction=encv(vector),bocksteinResiduals=[],correctionProducts=[],
            completedOriginalBocksteinRows=0,
            unitRightHandSideProducts=state["unitRightHandSideProducts"]+checks,
            secondExponentSupport=encp(f))
        cp.save(state)
    if state["stage"]=="bockstein-products":
        E=decv(state["firstQuotient"]);x=decv(state["rightKernel"]);y=decv(state["correction"])
        while state["completedOriginalBocksteinRows"]<56:
            residuals=decv(state["bocksteinResiduals"]);products=decv(state["correctionProducts"])
            support=decp(state["secondExponentSupport"])
            start=state["completedOriginalBocksteinRows"]
            for i in range(start,min(start+4,56)):
                tick()
                product=original_product(A[i],y)
                quotient,remainder=divmod(E[i]-product,f)
                require(quotient*f+remainder==E[i]-product,
                        "Every complete original E-Ay quotient/remainder identity")
                if i in profile["originalUnitRows"]:
                    require(not remainder,"The original 21 unit rows vanish in the Bockstein residual")
                products.append(product);residuals.append(remainder)
                support=monic(support.gcd(remainder))
                require(not divmod(f,support)[1],
                        "Every second-exponent support remains a true factor of squarefree f")
            next_state=dict(state)
            next_state.update(generation=state["generation"]+1,
                completedOriginalBocksteinRows=len(residuals),bocksteinResiduals=encv(residuals),
                correctionProducts=encv(products),secondExponentSupport=encp(support))
            cp.save(next_state);state=next_state
        support=decp(state["secondExponentSupport"]);omega=monic(f*support)
        residuals=decv(state["bocksteinResiduals"]);products=decv(state["correctionProducts"])
        require(len(residuals)==56 and state["unitRightHandSideProducts"]==42,
                "Both single right-hand sides and all 56 original output rows completed")
        require(all(not divmod(value,support)[1] for value in residuals),
                "Every Bockstein residual is divisible by the computed common support")
        coprime=exact_division(f,support)
        for value in residuals:
            coprime=monic(coprime.gcd(exact_division(value,support)))
        require(int(coprime.degree())==0,
                "No omitted support factor can carry a second positive exponent")
        exact_quotients=[]
        for i in range(56):
            tick()
            exact_quotients.append(exact_division(E[i]-products[i],support))
        z=[x[i]-f*y[i] for i in range(22)]
        require(z[profile["originalFreeColumn"]]==ONE,
                "The complete polynomial two-digit source retains free coordinate one")
        require(int(omega.degree())>=60 and int(omega.degree())<=120
                and not divmod(U,omega)[1],"Actual all56 gcd fits the paid exact upper")
        certificate={"factor":encp(f),"monicUpper":encp(U),"monicExactOutsideGcd":encp(omega),
            "monicSecondExponentSupport":encp(support),"monicUpperQuotient":encp(exact_division(U,omega)),
            "rightKernel":state["rightKernel"],"firstQuotient":state["firstQuotient"],
            "correction":state["correction"],"bocksteinResiduals":state["bocksteinResiduals"],
            "correctionProducts":state["correctionProducts"],"twoDigitPolynomialSource":encv(z),
            "exactQuotientAfterFAndSupport":encv(exact_quotients),
            "profile":state["profile"],"factorization":state["factor"],
            "all56OriginalAxDivisionsVerified":True,
            "all56OriginalCorrectionProductsVerified":True,
            "freeCoordinateExactlyOne":True,"allOriginal56RowsCertified":True,
            "actualResidueCorank":1,"noIrreducibilityAssumption":True,
            "completeOriginalOutsideGcdComputed":True,"exactGcdEqualsUpper":omega==U}
        pin=cp.phase("complete-original56-single-kernel-bockstein",certificate)
        state=dict(state);state.update(generation=state["generation"]+1,stage="completed",
            exactOutsideGcdStatistics=pstats(omega),secondExponentSupportStatistics=pstats(support),
            actualCompleteCertificate=pin,exactGcdEqualsUpper=omega==U)
        for key in ("rightKernel","firstQuotient","correction","bocksteinResiduals","correctionProducts"):
            state.pop(key,None)
        cp.save(state)
    require(state["stage"]=="completed","Actual all-original-row Bockstein completion")
    rec["parameters"].update(completeOriginalOutsideGcdComputed=True,
        allOriginal56RowsCertified=True,all56OriginalAxDivisionsVerified=True,
        all56OriginalCorrectionProductsVerified=True,all21PaidPivotsReproduced=True,
        allOldProfileBytesHashed=True,oldPrecisionTwoMatrixDecoded=False,
        exactOutsideGcdStatistics=state["exactOutsideGcdStatistics"],
        secondExponentSupportStatistics=state["secondExponentSupportStatistics"],
        exactGcdEqualsUpper=state["exactGcdEqualsUpper"],
        actualCompleteCertificate=state["actualCompleteCertificate"])
    return state

def main():
    global STOP,DEADLINE
    parser=argparse.ArgumentParser()
    for name in ("lower-source","upper-source","core-source","parent-checkpoints",
                 "upper-out","profile-out","out"):
        parser.add_argument("--"+name,required=True)
    parser.add_argument("--remaining-seconds",type=float,default=300)
    parser.add_argument("--memory-mib",type=int,default=2048)
    args=parser.parse_args()
    require(0<args.remaining_seconds<=1200 and 512<=args.memory_mib<=8192,
            "Explicit bounded mathematical time and memory")
    resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,args.memory_mib*1024**2))
    sys.set_int_max_str_digits(0)
    started=time.monotonic()
    DEADLINE=started+max(.01,args.remaining_seconds-min(12,args.remaining_seconds/8))
    def request_stop(signum,frame):
        global STOP
        STOP=True
    signal.signal(signal.SIGTERM,request_stop);signal.signal(signal.SIGALRM,request_stop)
    signal.setitimer(signal.ITIMER_REAL,args.remaining_seconds)
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    identity={"format":FORMAT,"source":file_id(__file__),"lowerSource":LOWER_SOURCE,
        "oldBinding":OLD_BINDING,"oldRaw":OLD_RAW,"oldState":OLD_STATE,
        "factorSHA256":FACTOR_SHA,
        "algorithm":"paid21unit; selected square only; two single RHS; all56 Ax/f and E-Ay; exact f*gcd"}
    binding=digest(canonical(identity))
    rec={"format":FORMAT,"binding":binding,"status":"started","events":[],
        "parameters":{"author":"Astra-ISP-789f / normal_annihilator","aiAssisted":"GPT-6 Astra Pro",
            "identity":identity,"remainingSeconds":args.remaining_seconds,"memoryMiB":args.memory_mib,
            "allLargeArraysTemporaryOnly":True,"oldDeterminantsNotRecomputed":True,
            "originalCoreNotRecomputed":True,"newGaussianProfileNotChosen":True,
            "oldPrecisionTwoMatrixDecoded":False,"oldPrecisionTwoReplayNotResumed":True,
            "newNineTargetGlobalMembershipClaim":False}}
    cp=Checkpoints(out/"checkpoints",binding);state=None
    try:
        rec["parameters"]["tinyExactVerification"]=tiny_verification()
        A,U,f,meta=load_inputs(args);rec["parameters"]["inputs"]=meta
        state=cp.load()
        rec["parameters"]["resumed"]=state is not None
        if state is not None:
            rec["parameters"]["startingCheckpoint"]=safe_summary(state)
        state=execute(args,cp,state,A,U,f,rec)
        rec["status"]="completed";rec["outcome"]="complete-original56-outside-gcd-by-single-kernel-bockstein"
    except BudgetStop as error:
        rec["status"]="budget-checkpoint"
        rec["parameters"]["stopReason"]=str(error)
    except BaseException as error:
        rec["status"]="failed"
        rec["parameters"]["error"]={"type":type(error).__name__,"message":str(error)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["elapsedSeconds"]=time.monotonic()-started
        rec["parameters"].setdefault("completeOriginalOutsideGcdComputed",False)
        if cp.pointer.exists():
            pointer=json.loads(cp.pointer.read_text())
            rec["parameters"]["lastWholeCheckpoint"]=pointer
        data=canonical(rec)
        require(len(data)<90000,"Only a small execution receipt may be published")
        atomic_bytes(out/"original56-single-kernel-bockstein-receipt.json",data)
        print(data.decode("ascii"),flush=True)
    return 1 if rec["status"]=="failed" else (75 if rec["status"]=="budget-checkpoint" else 0)

if __name__=="__main__":
    raise SystemExit(main())
