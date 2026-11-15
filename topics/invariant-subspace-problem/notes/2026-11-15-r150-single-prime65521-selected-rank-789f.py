#!/usr/bin/env python3
"""One fixed-prime65521 rank of the true original selected columns after paid29 elimination.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No old31 prebasis coefficients are used over another field or over Q.
"""
import argparse,array,gzip,hashlib,importlib.util,json,math,os,pathlib,resource,signal,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
PRIME=65521
H_SHA="9332d9d394b1a17444c9ccc20b3971cf74b7e932cffc8d9189e4e2f64fe0c428"
P_SHA="97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"
MODEL_SHA="0aa2d6d5c368b9885e279cd5b8e2cc7a59ba574ca161c0535193c30defe52d3d"
MODEL_BIND="504e56f3cdd71d9527fbf7db4d0b37eff12c55e57b20a7292171c7d1c40806e0"
def need(b,s):
 if not b:raise ValueError(s)
def sha(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def savejson(p,d):
 q=p.with_name(p.name+".tmp");q.write_text(json.dumps(d,separators=(",",":"))+"\n");os.replace(q,p)
 return {"file":p.name,**sha(p),"temporaryOnly":True}
def savearray(p,magic,header,data):
 q=p.with_name(p.name+".tmp");need(data.typecode=="H" and data.itemsize==2,"u16 array")
 if sys.byteorder!="little":data.byteswap()
 with q.open("wb") as f:f.write(magic);f.write(struct.pack("<"+"I"*len(header),*header));data.tofile(f)
 if sys.byteorder!="little":data.byteswap()
 os.replace(q,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def readarray(p,magic,nhead):
 with p.open("rb") as f:
  need(f.read(8)==magic,"matrix magic")
  h=struct.unpack("<"+"I"*nhead,f.read(4*nhead));data=array.array("H");data.frombytes(f.read())
 if sys.byteorder!="little":data.byteswap()
 return h,data
def worker(argv):
 ap=argparse.ArgumentParser();ap.add_argument("--input",required=True,type=pathlib.Path);ap.add_argument("--out",required=True,type=pathlib.Path);a=ap.parse_args(argv)
 start=time.monotonic();from flint import nmod_mat
 h,data=readarray(a.input,b"R150FP65",3);p,m,n=h
 need((p,m,n)==(PRIME,4367,4325) and len(data)==m*n,"complete original matrix")
 M=nmod_mat(m,n,list(data),p);R,rank=M.rref();rank=int(rank)
 output=array.array("H",(int(x) for x in R.entries()))
 rr=savearray(a.out/"original-selected-65521-rref.bin",b"R150FR65",(p,m,n,rank),output)
 rec={"status":"completed","prime":p,"rows":m,"columns":n,"rank":rank,"input":sha(a.input),"rref":rr,"elapsedSeconds":time.monotonic()-start}
 savejson(a.out/"rank-worker-receipt.json",rec);print(json.dumps(rec),flush=True);return 0
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["helper","point-model","prepared-model","out"]:ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=60,"unique <=60-second request")
 need(0<a.memory_mib<=2048,"<=2048MiB per process")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-2;out=a.out.resolve()
 need(not out.exists() or not any(out.iterdir()),"fresh directory");out.mkdir(parents=True,exist_ok=True)
 r={"format":"isp-single-prime65521-original-selected-rank-after29-v1","status":"running","prime":PRIME,
  "parameters":{},"newDixonDigitsComputed":0,"oldNormalFormsRecomputed":False,
  "old31RowOperationsReusedInNewField":False,"largeDataUploadedOrCommitted":False}
 temps=[];code=1
 def check():
  if time.monotonic()>=deadline:raise TimeoutError("actual single-prime shared time")
 try:
  need(sha(a.helper)["sha256"]==H_SHA and sha(a.point_model)["sha256"]==P_SHA,"paid helper/point")
  need(sha(a.prepared_model)=={"bytes":814572,"sha256":MODEL_SHA},"actual prepared source dictionary")
  with gzip.open(a.prepared_model,"rt") as f:model=json.load(f)
  need(model["binding"]==MODEL_BIND,"original source dictionary binding")
  free=list(map(int,model["freeRows"]));selected=set(map(int,model["selectedRows"]))
  need(len(free)==36 and len(selected)==4354 and set(free)<=selected,"same selected/free source dictionary")
  removed=free[:29];columns=sorted(selected-set(removed));need(len(columns)==4325,"exact29 removed source columns")
  sp=importlib.util.spec_from_file_location("paid_helper",a.helper);H=importlib.util.module_from_spec(sp);sp.loader.exec_module(H)
  point=json.loads(a.point_model.read_text());rowterms=H.original_row_terms(point)
  data=array.array("H",[0])*(4367*4325)
  for c,raw in enumerate(columns):
   for rr,v in rowterms[raw-1]:
    k=rr*4325+c;data[k]=(data[k]+v)%PRIME
   if c%128==0:check()
  inp=out/"original-selected-columns-65521.bin"
  temps.append(savearray(inp,b"R150FP65",(PRIME,4367,4325),data))
  source_hash=hashlib.sha256((",".join(map(str,columns))+"\n").encode()).hexdigest()
  r["parameters"].update({"sourceSHA256":sha(__file__)["sha256"],"helperSHA256":H_SHA,"pointSHA256":P_SHA,
    "preparedModelSHA256":MODEL_SHA,"removedOriginalSourceRows":removed,"remainingOriginalSourceRowsSHA256":source_hash,
    "allOriginal17IntegerCoefficientsReducedDirectly":True,
    "deletingColumnsPreservesQImageByPaidNormalized29Kernels":True,"noClaimOfImagePreservationModulo65521BeforeRank":True,
    "temporaryFiles":temps})
  savejson(out/"single-prime65521-selected-rank-receipt.json",r);check()
  log=out/"rank-worker.log";cmd=[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),"--rank-worker","--input",str(inp),"--out",str(out)]
  with log.open("w") as f:
   proc=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
   try:proc.wait(timeout=max(.01,deadline-time.monotonic()))
   except subprocess.TimeoutExpired:
    os.killpg(proc.pid,signal.SIGKILL);proc.wait()
    r["parameters"]["workerStoppedAtDeadline"]=True;r["parameters"]["workerExitCode"]=proc.returncode
    raise TimeoutError("finite-field exact RREF not returned before shared deadline")
  need(proc.returncode==0,"finite-field worker completed")
  wr=json.loads((out/"rank-worker-receipt.json").read_text())
  need(wr["status"]=="completed" and wr["input"]==sha(inp),"worker bound actual original matrix")
  rrpath=out/"original-selected-65521-rref.bin";need(sha(rrpath)=={k:wr["rref"][k] for k in ["bytes","sha256"]},"actual full RREF hash")
  hh,rr=readarray(rrpath,b"R150FR65",4);p,m,n,rank=hh
  need((p,m,n)==(PRIME,4367,4325) and rank==wr["rank"] and len(rr)==m*n,"all RREF dimensions")
  piv=[];c=0
  for i in range(rank):
   while c<n and rr[i*n+c]==0:c+=1
   need(c<n and rr[i*n+c]==1,"RREF leading unit");piv.append(c);c+=1
  need(all(x==0 for x in rr[rank*n:]),"all remaining RREF rows zero")
  fs=[j for j in range(n) if j not in set(piv)];d=len(fs)
  check();from flint import nmod_mat
  K=array.array("H",[0])*(n*d)
  for j,col in enumerate(fs):
   K[col*d+j]=1
   for i,pivcol in enumerate(piv):K[pivcol*d+j]=(-rr[i*n+col])%PRIME
  if d:
   product=nmod_mat(m,n,list(data),PRIME)*nmod_mat(n,d,list(K),PRIME)
   need(all(int(x)==0 for x in product.entries()),"all4367 complete nullspace original products")
  kr=savearray(out/"original-selected-65521-kernel.bin",b"R150FK65",(PRIME,n,d),K)
  temps.extend([{"file":rrpath.name,**sha(rrpath),"temporaryOnly":True},kr])
  profile={"prime":PRIME,"rank":rank,"pivotColumnsZeroBased":piv,"freeColumnsZeroBased":fs,
      "selectedOriginalSourceRows":columns,"all4367KernelProductsZero":True}
  temps.append(savejson(out/"selected-65521-column-profile.json",profile))
  r.update({"status":"completed","exactRankModulo65521":rank,"nullityModulo65521":d,
   "all4367CompleteKernelProductsZeroModulo65521":True,
   "selectedOriginalRankOverQLowerBound":max(4318,rank),"selectedOriginalRankOverQUpperBound":4325,
   "selectedOriginalQRankExactly4325Proved":rank==4325,
   "noFurtherPrimeRequested":True})
  code=0
 except TimeoutError as e:r.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:r.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  r["parameters"]["temporaryFiles"]=temps;r["mathematicalElapsedSeconds"]=time.monotonic()-start
  savejson(out/"single-prime65521-selected-rank-receipt.json",r)
 print(json.dumps(r),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--rank-worker":sys.exit(worker(sys.argv[2:]))
 sys.exit(main(sys.argv[1:]))
