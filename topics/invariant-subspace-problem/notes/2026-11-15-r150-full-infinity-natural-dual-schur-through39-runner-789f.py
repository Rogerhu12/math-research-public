#!/usr/bin/env python3
"""Full original natural-infinity dual27 jets; paid4340 transpose-DAG, full6188 residual.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only source, parameters, run and small receipts are permanent; all arrays temporary.
"""
import argparse,gzip,hashlib,itertools,json,math,os,pathlib,resource,shutil,signal,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for key in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):os.environ[key]="1"
P=31
PIN={
"native_model":(128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
"forward":(1660293,"445ec1d9acfa14932d8c3122fe98b471d869b3a8df0fa09a9ce14027e67c96ca"),
"backward":(2031817,"b6a40b3bb5b54053ac71dd8eb0a2b3555ffc88bb958229ef23c756b705fb5a28"),
"full_operations":(4706546,"bfcc10520abedfab362b91adc6414481660d4a951aae0d7dfd13da3efba4e3ec"),
"paid_full_receipt":(72072,"d904b1afcd6feb6d07e310e758869aa345342f7d013773aa0c433203291c438e"),
"primitive_equations":(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
"paid_selected_summary":(26242,"e57d4bc56bbd50e1d1700b819a3f5f6499c92b885788ec3fe55089b5a6755657"),
"generic_rank_proof":(9957,"b803d92f159bf26bc9b4a80bbaf5a150ff8f17e81e201b0a99e845b7777038e4"),
"native_source":(21017,"54631a695dbd6dc41c446c8c3ab60ba527c5dd4f34fbe70187cdd0613caef1fb"),
"paid_full_summary":(35730,"2782f380fe5731fd4766fb05fa94a6fa38c36d2d5e491bd63dd1149adc3a9388")}
RAW={
"forward":(2378937,"66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e"),
"backward":(3052119,"cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f"),
"full_operations":(8548344,"d2555a117c9f79db448e8eb183d5420952fe001707f5ca81e20e98705b83a3ad")}
HEADER={
"2026-11-15-r150-saturated-global-common-789f.hpp":(11284,"f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1"),
"2026-11-14-r150-f31-bitplane-789f.hpp":(3030,"73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec")}
PRIMITIVE_RAW_SHA="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
PAID_B_BINDING="43124d7d621b24353e3686cb1db8932ee6259822f22c1dbb1f8e0cd1d7b54600"
class BudgetExpired(Exception):pass
def need(x,msg):
 if not x:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def digest(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   h.update(b);n+=len(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):return json.loads(pathlib.Path(p).read_text())
def save(p,obj):
 p=pathlib.Path(p);q=p.with_name(p.name+".partial")
 q.write_bytes(canonical(obj)+b"\n");os.replace(q,p)
 return {"file":p.name,**identity(p),"temporaryOnly":True}
def checked(p,pin):
 b=pathlib.Path(p).read_bytes();need(digest(b)=={"bytes":pin[0],"sha256":pin[1]},"complete pinned input: "+str(p));return b
def rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def sub(M,ri,ci):
 from flint import nmod_mat
 return nmod_mat(len(ri),len(ci),[int(M[i,j]) for i in ri for j in ci],P)
def zero(M):return not any(M.entries())
def pivots(M):
 R,r=M.rref();r=int(r)
 pp=[next(j for j in range(M.ncols()) if R[i,j]) for i in range(r)]
 need(pp==sorted(set(pp)),"strict field pivot order");return pp
def eye(n):
 from flint import nmod_mat
 return nmod_mat(n,n,[int(i==j) for i in range(n) for j in range(n)],P)
def zmat(n,m):
 from flint import nmod_mat
 return nmod_mat(n,m,[0]*(n*m),P)
def field_read(p,magic,degree,nr,nc,binding,expected=None):
 b=pathlib.Path(p).read_bytes()
 if expected is not None:need(hashlib.sha256(b).hexdigest()==expected,"native complete checkpoint SHA256")
 need(b[:8]==magic and struct.unpack_from("<IIII",b,8)==(P,degree,nr,nc) and b[24:88].decode()==binding
      and len(b)==88+nr*nc and all(v<P for v in b[88:]),"full original bound field array")
 return b[88:]
def field_write(p,magic,degree,M,binding):
 need(len(magic)==8,"bound magic length");nr,nc=M.nrows(),M.ncols()
 data=magic+struct.pack("<IIII",P,degree,nr,nc)+binding.encode()+bytes(int(x) for x in M.entries())
 q=p.with_name(p.name+".partial");q.write_bytes(data);os.replace(q,p)
 return {"file":p.name,**digest(data),"rows":nr,"columns":nc,"degree":degree,"temporaryOnly":True}
def series_write(p,mats,binding,height):
 nr,nc=mats[0].nrows(),mats[0].ncols()
 data=b"R15FDSS1"+struct.pack("<IIIII",P,height,nr,nc,len(mats))+binding.encode()+b"".join(bytes(int(v) for v in M.entries()) for M in mats)
 q=p.with_name(p.name+".partial");q.write_bytes(data);os.replace(q,p)
 return {"file":p.name,**digest(data),"temporaryOnly":True}
def series_read(p,binding,expected):
 from flint import nmod_mat
 b=p.read_bytes();need(digest(b)=={"bytes":expected["bytes"],"sha256":expected["sha256"]},"complete small-series checkpoint")
 need(b[:8]==b"R15FDSS1","small-series magic");field,height,nr,nc,nm=struct.unpack_from("<IIIII",b,8)
 need(field==P and b[28:92].decode()==binding and len(b)==92+nr*nc*nm,"small-series binding/extent")
 mats=[nmod_mat(nr,nc,list(b[92+k*nr*nc:92+(k+1)*nr*nc]),P) for k in range(nm)]
 return height,mats
def full_smith(series,out,binding,check,keep):
 """All1848 rows retained; exact original row/column labels and formal mapper."""
 from flint import nmod_mat
 cache=out/"small-series-smith-state.json"
 nr,nc=1848,27;row_labels=list(range(nr));col_labels=list(range(nc));input_degree=len(series)-1
 paid=[];selected_rows=[];selected_cols=[];steps=[];height=0
 mapper=eye(27);mats=series
 if cache.exists() and read(cache).get("inputDegree")==input_degree:
  c=read(cache);need(c["binding"]==binding,"same original Smith checkpoint binding")
  height,mats=series_read(out/c["series"]["file"],binding,c["series"])
  nr,nc=mats[0].nrows(),mats[0].ncols()
  row_labels=c["rowLabels"];col_labels=c["columnLabels"];paid=c["paidExponents"]
  selected_rows=c["selectedOriginalSchurRows"];selected_cols=c["selectedOriginalHeadColumns"];steps=c["steps"]
  mapper=nmod_mat(c["constantMapper"],P)
  need(len(row_labels)==nr and len(col_labels)==nc and mapper.nrows()==27 and mapper.ncols()==nc
       and len(paid)==27-nc and len(paid)<=14,"complete Smith checkpoint shapes")
  keep(cache);keep(out/c["series"]["file"])
 def commit():
  sf=out/("small-series-state-"+str(height)+".bin")
  item=series_write(sf,mats,binding,height);keep(sf)
  save(cache,{"binding":binding,"inputDegree":input_degree,"height":height,"series":item,"paidExponents":paid,"rowLabels":row_labels,
   "columnLabels":col_labels,"selectedOriginalSchurRows":selected_rows,"selectedOriginalHeadColumns":selected_cols,
   "constantMapper":rows(mapper),"steps":steps})
  keep(cache)
 while True:
  check();precision=len(mats)-1;pc=pivots(mats[0]);rank=len(pc)
  need(len(paid)+rank<=14,"actual full Schur cannot exceed paid generic14")
  if rank:
   pr=pivots(sub(mats[0],list(range(nr)),pc).transpose());need(len(pr)==rank,"actual full rectangular unit")
  else:pr=[]
  prs,pcs=set(pr),set(pc);ri=pr+[i for i in range(nr) if i not in prs];ci=pc+[i for i in range(nc) if i not in pcs]
  steps.append({"exponent":height,"rows":nr,"columns":nc,"availableDegree":precision,"constantRank":rank,
   "unitRows":pr,"unitColumns":pc,"originalSchurRows":[row_labels[i] for i in pr],
   "originalHeadColumns":[col_labels[j] for j in pc]})
  paid.extend([height]*rank);selected_rows.extend(row_labels[i] for i in pr);selected_cols.extend(col_labels[j] for j in pc)
  mr,mc=nr-rank,nc-rank
  if rank:
   U=[sub(M,ri[:rank],ci[:rank]) for M in mats]
   V=[sub(M,ri[:rank],ci[rank:]) for M in mats]
   W=[sub(M,ri[rank:],ci[:rank]) for M in mats]
   Z=[sub(M,ri[rank:],ci[rank:]) for M in mats]
   inv=[U[0].inv()]
   for d in range(1,precision+1):
    check();v=zmat(rank,rank)
    for j in range(1,d+1):v+=U[j]*inv[d-j]
    inv.append(-inv[0]*v)
   for d in range(precision+1):
    check();v=zmat(rank,rank)
    for j in range(d+1):v+=U[j]*inv[d-j]
    need(v==(eye(rank) if d==0 else zmat(rank,rank)),"every coefficient of actual unit inverse")
   graph=zmat(nc,mc);top=-(inv[0]*V[0])
   for i in range(rank):
    for j in range(mc):graph[ci[i],j]=top[i,j]
   for i in range(mc):graph[ci[rank+i],i]=1
   mapper=mapper*graph
   WI=[]
   for d in range(precision+1):
    check();v=zmat(mr,rank)
    for j in range(d+1):v+=W[j]*inv[d-j]
    WI.append(v)
   schur=[]
   for d in range(precision+1):
    check();v=Z[d]
    for j in range(d+1):v=v-WI[j]*V[d-j]
    schur.append(v)
  else:schur=mats
  row_labels=[row_labels[i] for i in ri[rank:]]
  col_labels=[col_labels[j] for j in ci[rank:]]
  nr,nc=mr,mc
  need(zero(schur[0]),"all complete rectangular Schur constant coordinates")
  if len(paid)==14:
   need(nc==13 and nr==1834 and all(zero(M) for M in schur),
        "all retained free remainder coefficients vanish after14 actual pivots")
   need(all(1<=x<=21 for x in paid) and len(set(selected_rows))==14 and len(set(selected_cols))==14,
        "all14 actual positive exponents and original minor labels")
   need(sub(mapper,col_labels,list(range(13)))==eye(13),"formal13 graph has exact original free identity")
   return {"complete":True,"paidExponents":paid,"torsionLength":sum(paid),"maximumPositiveExponent":max(paid),
    "unresolvedPositiveCount":0,"formalKernelRank":13,"formalCokernelRank":1834,
    "genericRankSource":"paid original13 rational kernel theorem and same nonzero selected4354 minor",
    "selectedOriginalSchurRows":selected_rows,"selectedOriginalHeadColumns":selected_cols,
    "freeOriginalHeadColumns":col_labels,"allRetainedFreeRemainderCoefficientsZero":True,"steps":steps},mapper
  if precision==0:
   return {"complete":False,"paidExponents":paid,"unresolvedPositiveCount":14-len(paid),
    "unresolvedExponentAtLeast":height+1,"torsionLengthLowerBound":sum(paid)+(height+1)*(14-len(paid)),
    "formalKernelRankUpperBasedOnPaidGenericRank":13,"steps":steps},None
  mats=schur[1:];height+=1;commit()
def main(argv=None):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in PIN:ap.add_argument("--"+k.replace("_","-"),type=pathlib.Path,required=True)
 ap.add_argument("--out",type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=180)
 ap.add_argument("--memory-mib",type=int,default=1024)
 ap.add_argument("--compile-seconds",type=float,default=30)
 ap.add_argument("--maximum-degree",type=int,default=21)
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 0<a.seconds<=1200 and 0<a.compile_seconds<=60
      and 256<=a.memory_mib<=4096 and 1<=a.maximum_degree<=39,"explicit finite budgets through39")
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2))
 preflight=time.monotonic();start=None;rc=1;stop=False
 rp=out/"full-infinity-natural-dual-schur-receipt.json"
 rec={"format":"isp-full-original-natural-infinity-dual27-schur-v2","status":"running","field":P,
  "completeFullInfinitySmithLengthComputed":False,"full13FormalKernelMapperConstructed":False,
  "characteristicZeroInfinitySmithComputed":False,"selectedLeadingCoefficientUnitProved":False,
  "newLargeGaussianEliminations":0,"oldNormalFormsRecomputed":False,
  "largeDataUploadedOrCommitted":False,"events":[],"parameters":{}}
 files={}
 def keep(p):
  p=pathlib.Path(p)
  if p.exists():files[str(p.relative_to(out))]={"file":str(p.relative_to(out)),**identity(p),"temporaryOnly":True}
 def checkpoint():
  rec["parameters"]["temporaryFiles"]=list(files.values())
  rec["parameters"]["largeDataRemainOnlyInCurrentJob"]=True
  rec["mathematicalElapsedSeconds"]=0.0 if start is None else time.monotonic()-start
  save(rp,rec)
 def check():
  if stop or (start is not None and time.monotonic()-start>=a.seconds):raise BudgetExpired("shared full original dual-jet deadline")
 def remaining():
  check();return a.seconds-(time.monotonic()-start)
 def beat(phase):
  rec["phase"]=phase;checkpoint();print(json.dumps({"phase":phase,"mathematicalElapsedSeconds":rec["mathematicalElapsedSeconds"]}),flush=True);check()
 def signalled(sig,frame):
  nonlocal stop
  stop=True
 signal.signal(signal.SIGTERM,signalled);signal.signal(signal.SIGINT,signalled)
 try:
  blobs={};ids={}
  for key,pin in PIN.items():
   blobs[key]=checked(getattr(a,key),pin);ids[key]=digest(blobs[key])
  build=out/"native-build";build.mkdir(exist_ok=True)
  shutil.copyfile(a.native_source,build/a.native_source.name)
  for name,pin in HEADER.items():
   data=checked(a.native_source.parent/name,pin);ids[name]=digest(data);(build/name).write_bytes(data)
  exe=build/"full-natural-dual-jets";cache=build/"compile-cache.json"
  compile_binding=hashlib.sha256(canonical({"native":ids["native_source"],"headers":{n:ids[n] for n in HEADER},
    "flags":["g++","-std=c++17","-O2"]})).hexdigest()
  cc=read(cache) if cache.exists() else {}
  if exe.exists() and cc.get("binding")==compile_binding and cc.get("binary")==identity(exe):
   rec["events"].append({"reusedNativeCompilation":True});rec["compileElapsedSeconds"]=0.0
  else:
   t=time.monotonic();lp=build/"compile.log"
   with lp.open("wb") as log:
    z=subprocess.run(["g++","-std=c++17","-O2",str(build/a.native_source.name),"-o",str(exe)],
      stdout=log,stderr=subprocess.STDOUT,timeout=a.compile_seconds,check=False,cwd=build)
   rec["compileElapsedSeconds"]=time.monotonic()-t;keep(lp)
   if z.returncode!=0:
    rec["compileLogTail"]=lp.read_text(errors="replace")[-5000:]
    raise ValueError("actual native compilation failed")
   save(cache,{"binding":compile_binding,"binary":identity(exe),"elapsedSeconds":rec["compileElapsedSeconds"]})
  keep(cache)
  rec["preflightElapsedSeconds"]=time.monotonic()-preflight
  start=time.monotonic()
  prepared=out/"prepared";prepared.mkdir(exist_ok=True);rawpaths={}
  for key,pin in RAW.items():
   data=gzip.decompress(blobs[key]);need(digest(data)=={"bytes":pin[0],"sha256":pin[1]},"complete paid raw operation bytes: "+key)
   p=prepared/(key+".bin")
   if p.exists():need(identity(p)==digest(data),"unchanged prepared operation input")
   else:p.write_bytes(data)
   rawpaths[key]=p;keep(p)
  pr=gzip.decompress(blobs["primitive_equations"])
  need(hashlib.sha256(pr).hexdigest()==PRIMITIVE_RAW_SHA,"complete original primitive integer equations")
  primitive=json.loads(pr);eq=primitive["equations"]
  need(primitive["format"]=="r150-original-primitive-integer-equations-v1" and len(eq)==17
       and all(len(row)==77 for row in eq),"all17 original polynomial coefficient records")
  need(len(primitive["contents"])==17 and all(int(x)%31 for x in [primitive["denominator"]]+primitive["contents"]),
       "all original fixed rational row scales are31 units")
  F=[[[0]*77 for _ in range(17)] for __ in range(11)]
  for e,row in enumerate(eq):
   for j,pol in enumerate(row):
    vals=list(map(int,pol));need(bool(vals),"nonempty exact coefficient polynomial")
    if e>=11 and j<11:
     need(not any(vals),"Gamma has no linear part");continue
    degree=10 if e<11 and j<11 else 0 if e<11 else 5
    need(not any(vals[degree+1:]),"same original natural parameter degree")
    for d in range(degree+1):F[d][e][j]=(vals[degree-d] if degree-d<len(vals) else 0)%31
  tok=iter(blobs["native_model"].decode().split())
  need(next(tok)=="R150_NATIVE_NF_V1","paid original native model")
  def take(n):return [next(tok) for _ in range(n)]
  checks=0
  for e in range(11):
   Q=list(map(int,take(66)))
   need(all(Q[j]==int(eq[e][11+j][0])%31 for j in range(66)),"all original N quadratic coefficients");checks+=66
   for j in range(11):
    v=list(map(int,take(11)));pol=list(map(int,eq[e][j]))
    need(all(v[d]==(pol[d] if d<len(pol) else 0)%31 for d in range(11)),"all original N parameter coefficients");checks+=11
  need(int(next(tok))==3333,"original prebasis extent");take(3333*4)
  for e in range(11,17):
   for j in range(66):
    v=list(map(int,take(6)));pol=list(map(int,eq[e][11+j]))
    need(all(v[d]==(pol[d] if d<len(pol) else 0)%31 for d in range(6)),"all original Gamma parameter coefficients");checks+=6
  ns,nt=map(int,take(2));need((ns,nt)==(2195,9),"same original native source/target schema")
  take(ns*3);need(list(map(int,take(nt)))==list(range(2,11)) and next(tok,None) is None and checks==4433,
     "complete4433 original coefficient checks and native tail")
  paid=json.loads(blobs["paid_full_receipt"]);ps=paid["summary"]
  need(paid["status"]=="completed" and (ps["field"],ps["components"],ps["sources"],ps["constantRank"],ps["kernelRows"],ps["connectingRank"])
       ==(31,1034,2855,1007,1848,4),"complete paid full constant/first profile")
  bound=json.loads(blobs["paid_selected_summary"]);br=bound["result"];bs=br["parameters"]["smallSeriesSmith"]
  need(str(bound["runId"])=="43702348535" and bound["exitCode"]==0 and br["completeSelectedInfinitySmithLengthComputed"]
       and br["all51PaidPrefixFilesCoefficientIdentitiesVerified"] and bs["complete"]
       and len(bs["paidExponents"])==36 and sum(bs["paidExponents"])==243 and max(bs["paidExponents"])==21
       and br["parameters"]["newSchurBinding"]==PAID_B_BINDING,"paid same original selected maximum21/length243")
  material={"version":"full-original-infinity-dual27-transpose-dag-v2","source":identity(__file__),"inputs":ids,
   "field":31,"originalShape":[4367,6188],"constantUnitRank":4340,"dualHeads":27,"genericRankUpperBound":4354,
   "genericUpperSource":"original13-kernel theorem, every4355 minor integral zero",
   "smallSchurShape":[1848,27],"paidSelectedBinding":PAID_B_BINDING,"maximumPositiveExponentBound":21}
  binding=hashlib.sha256(canonical(material)).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material,"secondsLimit":a.seconds,"memoryMiB":a.memory_mib,
   "inclusiveRequestedDegree":a.maximum_degree,"paidSelectedLength31":243,"paidSelectedMaximumExponent31":21,
   "genericRank4340Plus14FromPaidOriginalUpperAndSelectedMinor":True,
   "genericRankProofSHA256":ids["generic_rank_proof"]["sha256"],
   "constantUnitRankIsActuallyChecked":True,"oldFullFirstConnectingRank":4})
  rec["all4433OriginalParameterCoefficientsVerified"]=True
  profile=prepared/"full-original-constant-profile.txt"
  lines=["R150_FULL_NATURAL_U_DUAL31_V2 "+binding,"1007"]+[" ".join(map(str,r)) for r in ps["constantPivots"]]+["4"]+[" ".join(map(str,r)) for r in ps["connectingPivots"]]
  pp=("\n".join(lines)+"\n").encode()
  if profile.exists():need(profile.read_bytes()==pp,"same actual full prepared profile and binding")
  else:profile.write_bytes(pp)
  keep(profile);beat("full-original-coefficients-and-profile")
  prefix=out/"full-dual";nreceipt=pathlib.Path(str(prefix)+"-receipt.json")
  old=read(nreceipt) if nreceipt.exists() else {}
  if old.get("inputBinding")==binding and old.get("completedDegree",-1)>=a.maximum_degree:
   rec["events"].append({"reusedCompleteNativeDualDegrees":old["completedDegree"]})
  else:
   logpath=out/"native.log";t=time.monotonic();budget=max(0.1,remaining()-4)
   cmd=[str(exe),str(a.native_model.resolve()),str(profile),str(rawpaths["forward"]),str(rawpaths["backward"]),
        str(rawpaths["full_operations"]),str(prefix),str(a.maximum_degree),str(budget)]
   with logpath.open("ab") as log:
    proc=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT)
    try:er=proc.wait(timeout=remaining())
    except subprocess.TimeoutExpired:
     proc.terminate()
     try:er=proc.wait(timeout=10)
     except subprocess.TimeoutExpired:proc.kill();er=proc.wait()
     rec["events"].append({"nativeSharedDeadlineReached":True,"exitCode":er})
     raise BudgetExpired("native stopped at shared deadline; last complete ledger retained")
   rec["nativeExecutionSeconds"]=time.monotonic()-t;rec["nativeExitCode"]=er;keep(logpath)
   if er not in (0,75):
    rec["nativeLogTail"]=logpath.read_text(errors="replace")[-5000:]
    raise ValueError("actual full dual native failed")
  nr=read(nreceipt);need(nr["inputBinding"]==binding,"native original full semantic binding")
  keep(nreceipt)
  completed=int(nr["completedDegree"]);need(0<=completed<=39,"actual complete native degree")
  rec["parameters"]["nativeSummary"]={k:v for k,v in nr.items() if k not in ("tailOriginalSourceRowsOneBased","unitOriginalSourceRowsOneBased","unitOriginalOutputIndicesZeroBased")}
  rec["parameters"]["nativeDictionarySHA256"]={k:hashlib.sha256(canonical(nr[k])).hexdigest() for k in
     ("tailOriginalSourceRowsOneBased","unitOriginalSourceRowsOneBased","unitOriginalOutputIndicesZeroBased")}
  for key in ("all3333OriginalPrebasisTriangularUnitProductsVerified","all1007OriginalFullPivotProductsVerified",
    "all27OriginalConstantHeadsIndependent","all6188OriginalConstantProductsZero","all4340OriginalUnitJetCancellationsVerified",
    "all6188OriginalJetResidualCoordinatesRetained","all27FreeOutputCoordinatesVerified","constantFullRank4340Verified"):
   need(nr.get(key) is True,"complete native original check: "+key);rec[key]=True
  ledger=pathlib.Path(str(prefix)+"-ledger.txt");lt=ledger.read_text().split()
  need(lt[:2]==["R15FDJLEDGER1",binding] and int(lt[2])==completed and len(lt)==3+3*(completed+1),
       "complete contiguous native hash ledger")
  from flint import nmod_mat
  import flint
  rec["pythonFlintVersion"]=flint.__version__;series=[]
  paid_full=json.loads(blobs["paid_full_summary"])
  need(str(paid_full["runId"])=="43731615668" and paid_full["exitCode"]==0,
       "paid full original spectrum execution")
  paid_result=paid_full["result"];paid_parameters=paid_result["parameters"]
  need(paid_result["status"]=="completed" and paid_result["fullInfinityTorsionLengthModulo31"]==66
       and paid_result["fullInfinityMaximumPositiveExponentModulo31"]==11
       and paid_parameters["binding"]=="3e51cbe960ac668c9addb12be36856d2aaf13686f5acc15571317ccf3dd7d2ad",
       "paid full66 and maximal exponent11")
  need(rec["parameters"]["nativeDictionarySHA256"]==paid_parameters["nativeDictionarySHA256"],
       "same three complete original full unit and tail dictionaries")
  paid_files={x["file"]:x for x in paid_parameters["temporaryFiles"]};prefix_checks=0
  for d in range(completed+1):
   for k,magic,nrows in (("cochain",b"R15FDL31",4367),("residual",b"R15FDR31",6188),("schur",b"R15FDS31",1848)):
    p=pathlib.Path(str(prefix)+"-"+k+"-"+str(d)+".bin")
    ix={"cochain":0,"residual":1,"schur":2}[k]
    bb=field_read(p,magic,d,nrows,27,binding,lt[3+3*d+ix]);keep(p)
    if d<=21:
     old_header=magic+struct.pack("<IIII",P,d,nrows,27)+paid_parameters["binding"].encode()
     old_identity=digest(old_header+bb);expected=paid_files[p.name]
     need(old_identity=={"bytes":expected["bytes"],"sha256":expected["sha256"]},
          "every original completed0..21 coefficient identity after honest binding transport")
     prefix_checks+=1
    if k=="schur":series.append(nmod_mat(1848,27,list(bb),P))
  keep(ledger);rec["completedNaturalDegree"]=completed
  rec["paidPrefixCoefficientFilesVerified"]=prefix_checks
  rec["all66PaidOriginalPrefixCoefficientIdentitiesVerified"]=(prefix_checks==66)
  rec["parameters"]["paidFullSpectrumSummary"]=ids["paid_full_summary"]
  beat("complete1848-by27-full-series-smith")
  smith,mapper=full_smith(series,out,binding,check,keep)
  rec["parameters"]["smallSeriesSmith"]=smith
  if completed>=21:
   need(smith["complete"],"proved original21 cutoff resolves all14 positive full indices")
   need(smith["paidExponents"]==paid_parameters["smallSeriesSmith"]["paidExponents"],
        "all14 original full exponents retained exactly")
  if not smith["complete"]:
   rec.update(status="completed-prefix",outcome="checkpointed-full-original-dual-jets");rc=75
  else:
   need(sum(smith["paidExponents"])<=243 and smith["paidExponents"].count(1)==4,"sameB upper and paid full first rank4")
   L0b=field_read(pathlib.Path(str(prefix)+"-cochain-0.bin"),b"R15FDL31",0,4367,27,binding,lt[3])
   L0=nmod_mat(4367,27,list(L0b),P);K0=L0*mapper
   fp=nr["freeOriginalOutputIndicesZeroBased"];fcols=smith["freeOriginalHeadColumns"]
   need(len(fp)==27 and sub(K0,[fp[j] for j in fcols],list(range(13)))==eye(13),"all13 formal free heads independent in original coordinates")
   var=[8**i for i in range(11)]
   mon=[sum(var[i] for i in q) for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
   mul=[sum(var[i] for i in q) for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
   terms=var+[var[i]+var[j] for i in range(11) for j in range(i,11)];index={x:i for i,x in enumerate(mon)}
   need(len(mon)==4367 and len(mul)*17==6188,"same complete original product dictionary")
   kr=rows(K0);product_count=0
   for raw in range(6188):
    q=[0]*13;e=raw%17;m=mul[raw//17]
    for j,v in enumerate(F[0][e]):
     if v:
      row=kr[index[m+terms[j]]]
      for c in range(13):q[c]+=v*row[c]
    need(all(v%31==0 for v in q),"all6188 original formal-kernel constant products")
    product_count+=13
    if raw%256==0:check()
   mf=out/"constant-formal-kernel-mapper27-by13.bin";kf=out/"original-formal-kernel-heads4367-by13.bin"
   field_write(mf,b"R15FDM31",0,mapper,binding);field_write(kf,b"R15FDK31",0,K0,binding);keep(mf);keep(kf)
   tail=nr["tailOriginalSourceRowsOneBased"]
   recipe={"format":"isp-original-full13-formal-kernel-mapper-v1","binding":binding,"field":31,
    "unitOriginalSources":nr["unitOriginalSourceRowsOneBased"],"unitOriginalOutputs":nr["unitOriginalOutputIndicesZeroBased"],
    "freeOriginalOutputs":fp,"tailOriginalSources":tail,
    "selectedSchurOriginalSources":[tail[i] for i in smith["selectedOriginalSchurRows"]],
    "selectedHeadColumns":smith["selectedOriginalHeadColumns"],"freeHeadColumns":fcols,
    "constantMapper":rows(mapper),"constantOriginalProductCoordinates":product_count,
    "formulaL":"L=E_free-E_unit*(A_unitOutputs,unitSources^T)^(-1)*A_freeOutputs,unitSources^T",
    "formulaS":"S=A_tailSources^T L",
    "formulaN":"N=E_F-E_C*(S_R,C)^(-1)*S_R,F",
    "formulaK":"K=L*N; all6188 original source equations vanish formally",
    "regularityReason":"actual successive unit-Schur graph maps have unit free block; their exact formal versions compose",
    "identityReason":"paid original generic upper4354 plus actual14 pivot minor forces residual formal rank0",
    "higherKernelCoefficientsClaimedNumericallyVerified":False,
    "exactOriginalPolynomialData":ids["primitive_equations"],"exactNaturalDegreeAtMost":10,
    "allOriginalNaturalResidualCoefficientsThroughDegree":completed}
   rr=out/"full13-original-formal-kernel-mapper.json";save(rr,recipe);keep(rr)
   rec.update(status="completed",outcome="complete-full-original-infinity-field-smith",
    completeFullInfinitySmithLengthComputed=True,full13FormalKernelMapperConstructed=True,
    fullConstantRankModulo31=4340,fullGenericRankModulo31=4354,
    fullInfinityTorsionLengthModulo31=smith["torsionLength"],
    fullInfinityMaximumPositiveExponentModulo31=smith["maximumPositiveExponent"],
    fullInfinityPositiveExponentCount=14,fullOriginalFreeCokernelRank=13,
    all80444OriginalFormalKernelConstantProductsVerified=True)
   rec["originalFormalKernelConstantProductCoordinates"]=product_count
   rec["completeFourteenPositiveIndicesAndThirteenFormalFreeDirectionsJustified"]=True
   rc=0
 except BudgetExpired as e:
  rec.update(status="budget-exhausted",outcome="checkpointed-full-original-dual-jets",error=str(e));rc=75
 except subprocess.TimeoutExpired as e:
  rec.update(status="budget-exhausted",outcome="checkpointed-before-native-mathematics",error=str(e));rc=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());keep(out/"exception.log");rc=1
 finally:
  for p in [pathlib.Path(str(out/"full-dual")+"-ledger.txt"),pathlib.Path(str(out/"full-dual")+"-receipt.json")]:
   if p.exists():keep(p)
  checkpoint()
 need(rp.stat().st_size<100000,"only small execution summaries may be published")
 print(json.dumps(rec,separators=(",",":")),flush=True);return rc
if __name__=="__main__":sys.exit(main())
