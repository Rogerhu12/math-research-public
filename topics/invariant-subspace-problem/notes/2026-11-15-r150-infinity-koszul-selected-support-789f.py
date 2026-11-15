#!/usr/bin/env python3
"""One exact-F31 support calculation for the physical-infinity Koszul family.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No original normal form or Dixon digit is recomputed. All arrays are temporary.
"""
import argparse, hashlib, importlib.util, itertools, json, math, os
import pathlib, resource, signal, struct, subprocess, sys, time, traceback
sys.dont_write_bytecode=True
P=31
ROWS=6188
COLUMNS=1632
HELPER_SHA="9332d9d394b1a17444c9ccc20b3971cf74b7e932cffc8d9189e4e2f64fe0c428"
POINT_SHA="97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"
SELECTED_SHA="5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"
PAID_SLOTS=[0,1,2,4,10,11,12,13,14,16,20,22,24,3,5,6,7,21,23,25,8,9,15]

class BudgetExpired(Exception):
    pass

def require(ok,message):
    if not ok: raise ValueError(message)

def sha_file(path):
    h=hashlib.sha256();n=0
    with path.open("rb") as f:
        while True:
            b=f.read(1<<20)
            if not b:break
            n+=len(b);h.update(b)
    return {"bytes":n,"sha256":h.hexdigest()}

def write_json(path,obj):
    tmp=path.with_name(path.name+".tmp")
    tmp.write_text(json.dumps(obj,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    os.replace(tmp,path)

def write_bytes(path,data):
    tmp=path.with_name(path.name+".tmp")
    tmp.write_bytes(data);os.replace(tmp,path)

def worker(argv):
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True,type=pathlib.Path)
    ap.add_argument("--output",required=True,type=pathlib.Path)
    ap.add_argument("--receipt",required=True,type=pathlib.Path)
    a=ap.parse_args(argv)
    started=time.monotonic()
    from flint import nmod_mat
    raw=a.input.read_bytes()
    require(raw[:8]==b"R150KO31" and len(raw)>=20,"outside matrix header")
    p,n,m=struct.unpack_from("<III",raw,8)
    require((p,n,m)==(31,1834,1632) and len(raw)==20+n*m,"outside dimensions")
    require(all(x<31 for x in raw[20:]),"outside residues")
    M=nmod_mat(n,m,list(raw[20:]),31)
    R,rank=M.rref()
    data=bytes(int(x) for x in R.entries())
    require(len(data)==n*m,"full RREF entries")
    write_bytes(a.output,b"R150KR31"+struct.pack("<IIII",31,n,m,int(rank))+data)
    result={"status":"completed","rank":int(rank),
            "input":sha_file(a.input),"output":sha_file(a.output),
            "elapsedSeconds":time.monotonic()-started,
            "temporaryOnly":True}
    write_json(a.receipt,result)
    print(json.dumps(result),flush=True)
    return 0

def main(argv):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--helper",required=True,type=pathlib.Path)
    ap.add_argument("--native-model",required=True,type=pathlib.Path)
    ap.add_argument("--point-model",required=True,type=pathlib.Path)
    ap.add_argument("--selected-receipt",required=True,type=pathlib.Path)
    ap.add_argument("--out",required=True,type=pathlib.Path)
    ap.add_argument("--seconds",type=float,default=60)
    ap.add_argument("--memory-mib",type=int,default=512)
    a=ap.parse_args(argv)
    require(math.isfinite(a.seconds) and 0<a.seconds<=60,"one shared <=60s budget")
    require(0<a.memory_mib<=512,"memory <=512MiB per process")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    started=time.monotonic();deadline=started+a.seconds-min(2,a.seconds/10)
    out=a.out.resolve()
    require(not out.exists() or not any(out.iterdir()),"fresh output directory")
    out.mkdir(parents=True,exist_ok=True)
    receipt_path=out/"koszul-selected-support-receipt.json"
    receipt={
        "format":"isp-physical-infinity-koszul-selected-support-f31-v1",
        "status":"running","field":31,"standardKoszulSourceCount":1632,
        "originalSourceCount":6188,"selectedSourceCount":4354,
        "outsideSelectedSourceCount":1834,
        "secondsLimit":a.seconds,"memoryMiBPerProcess":a.memory_mib,
        "oldNormalFormsRecomputed":False,"newDixonDigitsComputed":0,
        "characteristicZeroKernelConstructed":False,
        "characteristicZeroPaid23KoszulMembershipProved":False,
        "largeFilesTemporaryOnly":True,"largeDataUploadedOrCommitted":False,
        "parameters":{}
    }
    temps=[]
    code=1
    def check():
        if time.monotonic()>=deadline:raise BudgetExpired("actual shared time budget")
    def remember(path):
        rec={"file":path.name,**sha_file(path),"temporaryOnly":True}
        temps.append(rec);return rec
    try:
        require(sha_file(a.helper)["sha256"]==HELPER_SHA,"paid helper SHA")
        spec=importlib.util.spec_from_file_location("paid_source_helper",a.helper)
        H=importlib.util.module_from_spec(spec);spec.loader.exec_module(H)
        import flint
        from flint import nmod_mat
        receipt["pythonFlintVersion"]=getattr(flint,"__version__","unavailable")
        pbytes=a.point_model.read_bytes();sbytes=a.selected_receipt.read_bytes()
        require(hashlib.sha256(pbytes).hexdigest()==POINT_SHA,"original point SHA")
        require(hashlib.sha256(sbytes).hexdigest()==SELECTED_SHA,"selected dictionary SHA")
        point=json.loads(pbytes);selected_receipt=json.loads(sbytes)
        require(point.get("characteristicZeroSameOriginal17Verified") is True,"original17")
        selected=H.read_native_selected(a.native_model,point)
        require(set(map(int,selected_receipt["selectedSourceRows"]))==
                set(map(int,point["selectedSourceRows"])),"same1021 extra source dictionary")
        require(selected_receipt["selectedFullConstantRankModulo31"]==4318,
                "paid selected mod31 rank")
        free=list(map(int,selected_receipt["selectedConstantKernelFreeOriginalRows"]))
        require(len(free)==len(set(free))==36 and set(free)<=selected,"same free36")
        outside=[r for r in range(1,ROWS+1) if r not in selected]
        require(len(outside)==1834,"same outside1834")
        outside_index={r:i for i,r in enumerate(outside)}
        free_index={r:i for i,r in enumerate(free)}
        coeff=[[int(x)%31 for x in row] for row in point["primitivePointCoefficients"]]
        require(len(coeff)==17 and all(len(row)==77 for row in coeff),"original17x77")
        variables=[8**i for i in range(11)]
        multipliers=[sum(variables[i] for i in ij)
                     for degree in range(4)
                     for ij in itertools.combinations_with_replacement(range(11),degree)]
        require(len(multipliers)==364 and len(set(multipliers))==364,"original monomials")
        monomial_index={key:i for i,key in enumerate(multipliers)}
        terms=variables+[variables[i]+variables[j] for i in range(11) for j in range(i,11)]
        outmat=bytearray(1834*COLUMNS)
        freemat=bytearray(36*COLUMNS)
        family_hash=hashlib.sha256()
        column=0;nonzero_terms=0
        for i in range(17):
            for j in range(i+1,17):
                for factor in [0]+variables:
                    # f_j*e_i-f_i*e_j, multiplied by the same factor.
                    for source_equation,polynomial_equation,sign in [(i,j,1),(j,i,-1)]:
                        for key,c in zip(terms,coeff[polynomial_equation]):
                            if not c:continue
                            monomial=key+factor
                            require(monomial in monomial_index,"source multiplier degree<=3")
                            raw=17*monomial_index[monomial]+source_equation+1
                            require((raw-1)%17==source_equation,"original source equation dictionary")
                            value=sign*c%31
                            family_hash.update(("%d,%d,%d\n"%(raw,column,value)).encode("ascii"))
                            nonzero_terms+=1
                            if raw in outside_index:
                                p=outside_index[raw]*COLUMNS+column
                                outmat[p]=(outmat[p]+value)%31
                            if raw in free_index:
                                p=free_index[raw]*COLUMNS+column
                                freemat[p]=(freemat[p]+value)%31
                    column+=1
                check()
        require(column==COLUMNS,"all136*12 source columns")
        receipt["parameters"].update({
            "scriptSHA256":sha_file(pathlib.Path(__file__))["sha256"],
            "helperSHA256":HELPER_SHA,"pointSHA256":POINT_SHA,
            "nativeModelSHA256":H.NATIVE_SHA,"selectedReceiptSHA256":SELECTED_SHA,
            "outsideOriginalSourceRows":outside,"normalizedFreeOriginalSourceRows":free,
            "familyColumnOrder":"i<j lexicographic, then multiplier1,m0,...,m10",
            "fullStandardKoszulFormulaRetained":True,
            "allOriginalSourceDictionaryIdentitiesVerified":True,
            "standardFamilySparseF31SHA256":family_hash.hexdigest(),
            "generatedNonzeroSparseTerms":nonzero_terms,
            "standardFamilyInjectionUsesPaidInfinity187Theorem":True,
            "declaredPaidSlotsFromP768Proof":PAID_SLOTS,
        })
        input_path=out/"temporary-koszul-outside-mod31.bin"
        free_path=out/"temporary-koszul-free-mod31.bin"
        write_bytes(input_path,b"R150KO31"+struct.pack("<III",31,1834,COLUMNS)+outmat)
        write_bytes(free_path,b"R150KF31"+struct.pack("<III",31,36,COLUMNS)+freemat)
        input_rec=remember(input_path);remember(free_path)
        receipt["parameters"]["temporaryFiles"]=temps
        write_json(receipt_path,receipt)
        check()
        rrpath=out/"temporary-koszul-outside-rref-mod31.bin"
        rrreceipt=out/"rref-worker-receipt.json"
        log=out/"rref-worker.log"
        remaining=deadline-time.monotonic()
        cmd=[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),"--rref-worker",
             "--input",str(input_path),"--output",str(rrpath),"--receipt",str(rrreceipt)]
        worker_start=time.monotonic()
        with log.open("w",encoding="utf-8") as f:
            proc=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                proc.wait(timeout=max(.001,remaining))
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid,signal.SIGKILL);proc.wait()
                receipt["parameters"]["rrefWorker"]={
                    "status":"terminated-at-shared-wall-budget",
                    "exitCode":proc.returncode,"elapsedSeconds":time.monotonic()-worker_start,
                    "inputRetained":input_rec,"reductionCompleted":False}
                raise BudgetExpired("RREF worker stopped at shared deadline")
        receipt["parameters"]["rrefWorker"]={
            "exitCode":proc.returncode,"elapsedSeconds":time.monotonic()-worker_start}
        require(proc.returncode==0 and rrreceipt.exists(),"RREF worker did not complete")
        wr=json.loads(rrreceipt.read_text())
        require(wr.get("status")=="completed" and wr["input"]==sha_file(input_path) and
                wr["output"]==sha_file(rrpath),"actual worker output binding")
        receipt["parameters"]["rrefWorker"]["completedReceipt"]=wr
        remember(rrpath);remember(rrreceipt)
        raw=rrpath.read_bytes()
        require(raw[:8]==b"R150KR31" and len(raw)==24+1834*COLUMNS,"RREF output format")
        p,n,m,rank=struct.unpack_from("<IIII",raw,8)
        require((p,n,m)==(31,1834,1632) and rank<=1632,"RREF dimensions/rank")
        body=memoryview(raw)[24:]
        require(all(x<31 for x in body),"RREF coefficients")
        pivot=[];c=0
        for row in range(rank):
            while c<COLUMNS and not body[row*COLUMNS+c]:c+=1
            require(c<COLUMNS and body[row*COLUMNS+c]==1,"RREF pivot")
            pivot.append(c);c+=1
        pivotset=set(pivot)
        fcols=[c for c in range(COLUMNS) if c not in pivotset]
        dim=len(fcols)
        require(dim<=36,"injective original Koszul/free support bound")
        Z=bytearray(COLUMNS*dim)
        for j,col in enumerate(fcols):
            Z[col*dim+j]=1
            for i,piv in enumerate(pivot):
                Z[piv*dim+j]=(-body[i*COLUMNS+col])%31
        check()
        if dim:
            O=nmod_mat(1834,COLUMNS,list(outmat),31)
            K=nmod_mat(COLUMNS,dim,list(Z),31)
            product=O*K
            require(all(int(x)==0 for x in product.entries()),"all1834 outside coordinates of complete kernel")
            F=nmod_mat(36,COLUMNS,list(freemat),31)*K
            fd=bytes(int(x) for x in F.entries())
            frank=int(F.rref()[1])
            require(frank==dim,"full36 free image injectivity")
            union=[]
            for r in range(36):
                union.extend(fd[r*dim:(r+1)*dim])
                union.extend(int(r==s) for s in PAID_SLOTS)
            urank=int(nmod_mat(36,dim+23,union,31).rref()[1])
        else:
            fd=b"";frank=0;urank=23
        kernel_path=out/"temporary-koszul-outside-kernel-mod31.bin"
        image_path=out/"temporary-koszul-free-image-mod31.bin"
        write_bytes(kernel_path,b"R150KZ31"+struct.pack("<III",31,1632,dim)+Z)
        write_bytes(image_path,b"R150KI31"+struct.pack("<III",31,36,dim)+fd)
        remember(kernel_path);remember(image_path)
        receipt.update({
            "status":"completed","outsideSupportRankModulo31":rank,
            "selectedStandardKoszulDimensionModulo31":dim,
            "selectedStandardKoszulDimensionOverQUpperBound":dim,
            "all1834CompleteKernelOutputIdentitiesVerifiedModulo31":True,
            "complete36FreeImageRankModulo31":frank,
            "unionWithPaid23FreeAxesRankModulo31":urank,
            "newFreeDirectionsModulo31BeyondPaid23":urank-23,
            "characteristicZeroRankEqualityFromThisStepProved":False,
        })
        receipt["parameters"].update({
            "rrefPivotColumnsZeroBased":pivot,"rrefFreeColumnsZeroBased":fcols,
            "completeFreeImageRowMajor":list(fd),
            "characteristicZeroScope":"only1632-rank_mod31(outside) is an upper bound for the selected-support standard Koszul space",
            "finiteFieldNewDirectionsAreNotCharacteristicZeroKernels":True,
        })
        code=0
    except BudgetExpired as e:
        receipt["status"]="budget-exhausted";receipt["error"]=str(e);code=75
    except Exception as e:
        receipt["status"]="failed";receipt["error"]=str(e);receipt["exceptionType"]=type(e).__name__
        (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8")
        code=1
    finally:
        receipt["parameters"]["temporaryFiles"]=temps
        receipt["mathematicalElapsedSeconds"]=time.monotonic()-started
        write_json(receipt_path,receipt)
        require(receipt_path.stat().st_size<100000,"small receipt cap")
    print(json.dumps({key:receipt.get(key) for key in [
        "status","outsideSupportRankModulo31","selectedStandardKoszulDimensionModulo31",
        "selectedStandardKoszulDimensionOverQUpperBound","unionWithPaid23FreeAxesRankModulo31",
        "newFreeDirectionsModulo31BeyondPaid23","mathematicalElapsedSeconds"]}),flush=True)
    return code

if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]=="--rref-worker":
        sys.exit(worker(sys.argv[2:]))
    sys.exit(main(sys.argv[1:]))
