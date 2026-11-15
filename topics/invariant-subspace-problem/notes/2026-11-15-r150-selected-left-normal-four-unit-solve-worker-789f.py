#!/usr/bin/env python3
"""Temporary exact additional unit solve for an R150 selected-left page.

Input: the original sparse M0 rows and k original integer right-hand sides,
with 1 <= k <= 130. The1546 correction variables and4354 original rows are fixed.
Solve diag(g)^-1 M0[I] X = -diag(g)^-1 rhs[I] using python-flint 0.9.0
fmpq_mat.solve(..., algorithm="dixon").  Preserve the complete rational X as
positive column denominators and integer numerator columns BEFORE checking
any original product.  Then verify all1546 original unit rows columnwise.

The caller owns the one shared deadline and memory limit. SIGTERM requests
a checkpoint stop at a safe boundary; a blocked native solve might not
observe Python signals until it returns. No partial solve is called exact.
Only same-job temporary candidates/checkpoints are written. This worker
does not verify the other2808 original source rows; the caller must do so.

Official API:
https://python-flint.readthedocs.io/en/latest/fmpq_mat.html#flint.fmpq_mat.solve
https://python-flint.readthedocs.io/en/latest/fmpq.html
"""
import argparse
import gzip
import hashlib
import io
import json
from math import gcd
import os
from pathlib import Path
import re
import signal
import sys
import time

FORMAT="isp-selected-second-left-unit-input-v1"
SOLUTION_FORMAT="isp-selected-second-left-unit-solution-v1"
RECEIPT_FORMAT="isp-selected-second-left-unit-solve-receipt-v1"
INTEGER=re.compile(r"(?:0|-[1-9][0-9]*|[1-9][0-9]*)\Z")
HEX64=re.compile(r"[0-9a-f]{64}\Z")
STOP=False

class SafeStop(Exception):
    pass

def require(condition,message):
    if not condition:
        raise AssertionError(message)

def integer(value,where):
    require(isinstance(value,str) and INTEGER.fullmatch(value) is not None,
            "Noncanonical integer at "+where)
    return int(value)

def identity(path):
    h=hashlib.sha256();size=0
    with Path(path).open("rb") as f:
        while True:
            b=f.read(1024*1024)
            if not b:
                break
            h.update(b);size+=len(b)
    return {"bytes":size,"sha256":h.hexdigest()}

def read_json(path):
    path=Path(path)
    opener=gzip.open if path.suffix==".gz" else open
    with opener(path,"rt",encoding="utf-8") as f:
        return json.load(f)

def atomic_json(path,obj,compressed=False):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".tmp")
    if compressed:
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw,mode="wb",compresslevel=1,mtime=0) as gz:
                with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as out:
                    json.dump(obj,out,sort_keys=True,separators=(",",":"))
            raw.flush();os.fsync(raw.fileno())
    else:
        data=json.dumps(obj,sort_keys=True,indent=2).encode("utf-8")
        require(len(data)<100000,"Small receipt limit exceeded")
        with temporary.open("wb") as f:
            f.write(data);f.flush();os.fsync(f.fileno())
    os.replace(temporary,path)

def request_stop(signum,frame):
    global STOP
    STOP=True

def check_stop():
    if STOP:
        raise SafeStop("Caller requested a safe checkpoint stop")

def parse_input(a,receipt):
    obj=read_json(a.input)
    require(obj.get("format")==FORMAT,"Input format")
    binding=obj.get("binding")
    require(isinstance(binding,str) and HEX64.fullmatch(binding),"Semantic binding")
    n=obj.get("correctionVariables");k=obj.get("rhsColumns")
    require(n==1546 and isinstance(k,int) and not isinstance(k,bool) and 1<=k<=130,
            "Expected true1546 correction variables and1..130 actual RHS")
    labels=obj.get("originalSourceRows")
    rows=obj.get("originalCorrectionRows")
    rhs=obj.get("originalRightHandSideRows")
    contents=obj.get("rowCoefficientContents")
    selected=obj.get("selectedUnitRowIndices")
    require(isinstance(labels,list) and len(labels)==4354
            and len(set(labels))==4354
            and all(isinstance(x,int) and not isinstance(x,bool) and x>0 for x in labels),
            "All4354 distinct original source labels")
    require(isinstance(rows,list) and len(rows)==4354
            and isinstance(rhs,list) and len(rhs)==4354
            and isinstance(contents,list) and len(contents)==4354,
            "Full original input row count")
    require(isinstance(selected,list) and len(selected)==n and len(set(selected))==n
            and all(isinstance(x,int) and not isinstance(x,bool) and 0<=x<4354
                    for x in selected),"Original unit-row indices")
    require(obj.get("unitPrime")==31,"Unit prime")
    determinant=obj.get("unitDeterminantModulo31")
    if isinstance(determinant,str):
        determinant=integer(determinant,"unitDeterminantModulo31")
    require(isinstance(determinant,int) and not isinstance(determinant,bool)
            and 1<=determinant%31<=30,"Paid nonzero unit determinant metadata")
    actual_rows=[];actual_rhs=[];actual_contents=[]
    for i in range(4354):
        check_stop()
        row=rows[i]
        require(isinstance(row,list),"Sparse original row")
        previous=-1;parsed=[];content=0
        for item in row:
            require(isinstance(item,list) and len(item)==2,"Sparse row entry")
            c,v=item
            require(isinstance(c,int) and not isinstance(c,bool) and previous<c<n,
                    "Sparse columns must be distinct and strictly increasing")
            previous=c
            x=integer(v,"M0 row"+str(i)+" col"+str(c))
            require(x!=0,"Sparse original rows must not store zero entries")
            parsed.append((c,x));content=gcd(content,abs(x))
        g=integer(contents[i],"row content"+str(i))
        require(g>0 and g==(content if content else 1),
                "Actual original row coefficient content")
        rr=rhs[i]
        require(isinstance(rr,list) and len(rr)==k,"Full actual-k RHS row")
        actual_rows.append(parsed)
        actual_rhs.append([integer(v,"rhs"+str(i)+","+str(j)) for j,v in enumerate(rr)])
        actual_contents.append(g)
    receipt["binding"]=binding
    receipt["parameters"].update({
        "correctionVariables":n,"rhsColumns":k,
        "all4354InputRowsDecoded":True,"allOriginalRowContentsVerified":True,
        "unitPrime":31,"paidUnitDeterminantModulo31":determinant%31,
        "unitDeterminantRecomputedByWorker":False,
        "selectedOriginalRowsSHA256":hashlib.sha256(
            json.dumps([labels[i] for i in selected],separators=(",",":")).encode()).hexdigest(),
        "originalRowCount":4354,"unitRowCount":n,
    })
    return binding,n,k,selected,actual_rows,actual_rhs,actual_contents

def candidate_columns(solution,binding,input_id,n,k):
    require(solution.get("format")==SOLUTION_FORMAT
            and solution.get("binding")==binding
            and solution.get("inputIdentity")==input_id
            and solution.get("correctionVariables")==n and solution.get("rhsColumns")==k
            and solution.get("candidateOnlyUntilMatchingCompletedReceipt") is True,
            "Candidate must match same original input and binding")
    ds=solution.get("denominators")
    cs=solution.get("numeratorColumns")
    require(isinstance(ds,list) and len(ds)==k and isinstance(cs,list) and len(cs)==k,
            "All actual-k rational columns required")
    denominators=[];columns=[]
    for j in range(k):
        d=integer(ds[j],"candidate denominator"+str(j))
        require(d>0,"Positive candidate denominator")
        col=cs[j]
        require(isinstance(col,list) and len(col)==n,"Full1546 numerator column")
        col=[integer(v,"candidate"+str(j)+","+str(i)) for i,v in enumerate(col)]
        common=d
        for v in col:
            common=gcd(common,abs(v))
        require(common==1,"Candidate column must use its least positive common denominator")
        denominators.append(d);columns.append(col)
    return denominators,columns

def run(a,receipt,receipt_path,solution_path):
    import flint
    from flint import fmpq,fmpq_mat,fmpz_mat
    require(flint.__version__=="0.9.0","Pinned python-flint0.9.0")
    receipt["parameters"]["pythonFlint"]=flint.__version__
    binding,n,k,selected,rows,rhs,contents=parse_input(a,receipt)
    old=None
    if receipt_path.exists():
        old=read_json(receipt_path)
        require(old.get("format")==RECEIPT_FORMAT
                and old.get("binding")==binding
                and old.get("inputIdentity")==receipt["inputIdentity"]
                and old.get("workerSHA256")==receipt["workerSHA256"],
                "Prior verification checkpoint is not the same worker and actual input")
    receipt["parameters"]["checkpointBindingVerified"]=True
    receipt["phase"]="input-verified"
    atomic_json(receipt_path,receipt)
    check_stop()
    if solution_path.exists():
        solution=read_json(solution_path)
        ds,columns=candidate_columns(solution,binding,receipt["inputIdentity"],n,k)
        candidate_id=identity(solution_path)
        if old and old.get("candidateIdentity") is not None:
            require(candidate_id==old["candidateIdentity"],
                    "Saved rational candidate changed after verification checkpoint")
        receipt["parameters"]["resumedCompleteCandidate"]=True
    else:
        U=fmpq_mat(n,n);R=fmpq_mat(n,k)
        for i,r in enumerate(selected):
            check_stop()
            g=contents[r]
            for c,v in rows[r]:
                require(v%g==0,"Original matrix row content must divide every coefficient")
                U[i,c]=v//g
            for j in range(k):
                R[i,j]=fmpq(-rhs[r][j],g)
        receipt["phase"]="dixon-running"
        receipt["parameters"]["rhsAndMatrixBothRowDivided"]=True
        atomic_json(receipt_path,receipt)
        # The documented API returns the complete exact rational solution.
        X=U.solve(R,algorithm="dixon")
        receipt["phase"]="rational-solution-returned"
        receipt["parameters"]["dixonReturnedCompleteRationalMatrix"]=True
        atomic_json(receipt_path,receipt)
        # Prioritize saving the COMPLETE candidate before any product verification.
        ds=[];columns=[]
        for j in range(k):
            d=1
            for i in range(n):
                den=int(X[i,j].denom())
                d=d//gcd(d,den)*den
            col=[int(X[i,j].numer())*(d//int(X[i,j].denom())) for i in range(n)]
            require(d>0,"Positive complete solution denominator")
            ds.append(d);columns.append(col)
        solution={
            "format":SOLUTION_FORMAT,"binding":binding,
            "inputIdentity":receipt["inputIdentity"],
            "correctionVariables":n,"rhsColumns":k,
            "denominators":[str(d) for d in ds],
            "numeratorColumns":[[str(v) for v in col] for col in columns],
            "candidateOnlyUntilMatchingCompletedReceipt":True,
        }
        atomic_json(solution_path,solution,compressed=True)
        candidate_id=identity(solution_path)
        del U,R,X
        receipt["parameters"]["resumedCompleteCandidate"]=False
    receipt["candidateIdentity"]=candidate_id
    receipt["candidateFile"]=solution_path.name
    receipt["completeSolutionSavedBeforeProductVerification"]=True
    receipt["phase"]="candidate-saved"
    receipt["lastVerifiedColumn"]=-1
    receipt["verifiedColumnCount"]=0
    if old and old.get("candidateIdentity")==candidate_id:
        count=old.get("verifiedColumnCount",0)
        require(isinstance(count,int) and not isinstance(count,bool) and 0<=count<=k
                and old.get("lastVerifiedColumn",-1)==count-1,
                "Prior verified column checkpoint")
        require(count==0 or old.get("originalUnitProductCoordinates",0)==count*n,
                "Prior verified coordinate count")
        receipt["verifiedColumnCount"]=count
        receipt["lastVerifiedColumn"]=count-1
        receipt["parameters"]["resumedVerifiedColumnCount"]=count
    receipt["originalUnitProductCoordinates"]=receipt["verifiedColumnCount"]*n
    atomic_json(receipt_path,receipt)
    check_stop()
    # Verify the UNDIVIDED ORIGINAL selected rows, not g times the wrong RHS.
    Aint=fmpz_mat(n,n)
    for i,r in enumerate(selected):
        for c,v in rows[r]:
            Aint[i,c]=v
    receipt["phase"]="original-unit-products"
    atomic_json(receipt_path,receipt)
    for j in range(receipt["verifiedColumnCount"],k):
        check_stop()
        product=Aint*fmpz_mat(n,1,columns[j])
        d=ds[j]
        for i,r in enumerate(selected):
            if int(product[i,0])+d*rhs[r][j]!=0:
                receipt["firstFailure"]={
                    "column":j,"selectedRowPosition":i,
                    "originalSourceRowPosition":r,
                }
                raise AssertionError("Complete original unit product is nonzero")
        receipt["lastVerifiedColumn"]=j
        receipt["verifiedColumnCount"]=j+1
        receipt["originalUnitProductCoordinates"]=(j+1)*n
        atomic_json(receipt_path,receipt)
    receipt["all1546OriginalUnitRowsVerified"]=True
    receipt["phase"]="completed"
    receipt["status"]="completed"
    receipt["parameters"].update({
        "all1546OriginalUnitRowsVerified":True,
        "originalUnitProductCoordinates":n*k,
        "allCompleteRationalColumnsSaved":True,
        "full4354ProductVerificationStillRequiredByCaller":True,
        "denominatorBitLengths":[d.bit_length() for d in ds],
        "candidateTemporaryOnly":True,"largeDataUploadedOrCommitted":False,
    })

def main():
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True)
    p.add_argument("--out",required=True)
    a=p.parse_args()
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    receipt_path=out/"m0-unit-solve-receipt.json"
    solution_path=out/"complete-m0-unit-solution.json.gz"
    start=time.monotonic()
    receipt={
        "format":RECEIPT_FORMAT,"status":"incomplete","phase":"started",
        "workerSHA256":identity(__file__)["sha256"],
        "inputIdentity":identity(a.input),
        "lastVerifiedColumn":-1,"verifiedColumnCount":0,
        "originalUnitProductCoordinates":0,
        "all1546OriginalUnitRowsVerified":False,
        "parameters":{"timeoutAndMemoryManagedByCaller":True,
                      "candidateTemporaryOnly":True,
                      "algorithm":"fmpq_mat.solve(dixon)",
                      "largeDataUploadedOrCommitted":False},
    }
    signal.signal(signal.SIGTERM,request_stop)
    signal.signal(signal.SIGINT,request_stop)
    code=1
    try:
        run(a,receipt,receipt_path,solution_path)
        code=0
    except SafeStop as exc:
        receipt["status"]="incomplete"
        receipt["error"]=str(exc);code=75
    except BaseException as exc:
        receipt["status"]="failed"
        receipt["error"]=type(exc).__name__+": "+str(exc)
        code=1
    finally:
        receipt["elapsedSeconds"]=time.monotonic()-start
        receipt["parameters"]["signalStopRequested"]=STOP
        # Do not overwrite a mismatched prior checkpoint before its binding is known.
        can_write_checkpoint=receipt["parameters"].get("checkpointBindingVerified",False)
        if can_write_checkpoint:
            atomic_json(receipt_path,receipt)
        else:
            atomic_json(out/"m0-unit-solve-failed-input-receipt.json",receipt)
        actual=receipt_path if can_write_checkpoint else out/"m0-unit-solve-failed-input-receipt.json"
        info=identity(actual)
        print(json.dumps({
            "status":receipt["status"],"phase":receipt["phase"],
            "receipt":str(actual),"receiptBytes":info["bytes"],"receiptSHA256":info["sha256"],
            "elapsedSeconds":receipt["elapsedSeconds"],
            "completeSolutionSavedBeforeProductVerification":
                receipt.get("completeSolutionSavedBeforeProductVerification",False),
            "all1546OriginalUnitRowsVerified":receipt["all1546OriginalUnitRowsVerified"],
            "originalUnitProductCoordinates":receipt["originalUnitProductCoordinates"],
            "lastVerifiedColumn":receipt["lastVerifiedColumn"],
            "verifiedColumnCount":receipt["verifiedColumnCount"],
            "candidateIdentity":receipt.get("candidateIdentity"),
        }),flush=True)
    raise SystemExit(code)

if __name__=="__main__":
    main()
