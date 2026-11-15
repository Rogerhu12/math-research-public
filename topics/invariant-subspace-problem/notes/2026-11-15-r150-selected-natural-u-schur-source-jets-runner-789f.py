#!/usr/bin/env python3
"""Same original I,J: source-preserving natural-u Schur jets over F31.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only temporary arrays; permanent output is this script, parameters, receipts and SHA.
"""
import argparse,gzip,hashlib,itertools,json,os,pathlib,resource,signal,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
for _n in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):
 os.environ[_n]="1"
P=31
NATIVE="2026-11-15-r150-selected-natural-u-schur-source-jets-789f.cpp"
NATIVE_PIN=(16667,"40dc42b367d241fb7d1cf0c3dd9ef35d61ad0ce756a63559ca8110188b2206dd")
HEADERS={
 "2026-11-15-r150-saturated-global-common-789f.hpp":(11284,"f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1"),
 "2026-11-14-r150-f31-bitplane-789f.hpp":(3030,"73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec")}
PIN={
 "native_model":(128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "point_model":(87459,"97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"),
 "selected_model":(814572,"0aa2d6d5c368b9885e279cd5b8e2cc7a59ba574ca161c0535193c30defe52d3d"),
 "unit_profile":(62084,"43cd638dfe13978f375490db9afdca5f318e137a384820b69bbc74b0ce48a7df"),
 "kernel36":(222788,"c008e57b7a7e80312f8ba292bb24241d53bb59d4c57b2a8d07ec1017b9de0744"),
 "source_dag":(957557,"c50e7bb8558a7f637d9d6951f64ae002c96cdce06dfcb7d1a4619ea6dc07337a")}
FIRST={
 "receipt":("selected-natural-first-connection-f31-receipt.json",15594,"ef7b8a3f935eb376353a235c95d257b8f0785c7459d7c45b348b6e238390fb62"),
 "product":("whole-natural-first-product-field31.json.gz",105574,"6612dc599486f386c562c3ebc0081cddf0df94f08fbb757b307d2109c60ece1f"),
 "cokernel":("complete-selected-cokernel36-field31.json.gz",5473,"8cf6eed29b26407a6a2fdad36ceb7a2fd56929eef88536042e08daeb856abe6a"),
 "full_connection":("full-output-selected-first-connection49-field31.bin",1784,"e5efd96e8062c0f1b2baa703868de8a981f4bd3034c08b71495d067954b7280b")}
FIRST_BINDING="479d3295113d0e1ea0bc5e2b404a0426e5f584229a16dcfdb18aa2d6ef5dac31"
DAGS={
 "forward":("r150-module-actions-789f/43588728414-1/char31/nf-forward.bin.gz",1660293,"445ec1d9acfa14932d8c3122fe98b471d869b3a8df0fa09a9ce14027e67c96ca",2378937,"66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e"),
 "backward":("r150-module-actions-789f/43588728414-1/char31/nf-backward.bin.gz",2031817,"b6a40b3bb5b54053ac71dd8eb0a2b3555ffc88bb958229ef23c756b705fb5a28",3052119,"cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f")}
class BudgetExpired(Exception):pass
def need(x,s):
 if not x:raise ValueError(s)
def digest(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def file_identity(p):return digest(p.read_bytes())
def checked(p,pin):
 b=p.read_bytes();need((len(b),hashlib.sha256(b).hexdigest())==pin,"actual input SHA/bytes "+str(p));return b
def jsave(p,o):
 q=p.with_name(p.name+".partial");q.write_text(json.dumps(o,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");os.replace(q,p)
def decode_json(b):return json.loads(gzip.decompress(b) if b[:2]==b"\x1f\x8b" else b)
def matrix_rows(m):return [[int(m[i,j]) for j in range(m.ncols())] for i in range(m.nrows())]
def zero(m):return not any(m.entries())
def select(m,rows,cols):
 from flint import nmod_mat
 return nmod_mat(len(rows),len(cols),[int(m[i,j]) for i in rows for j in cols],31)
def pivots(m):
 rr,r=m.rref();p=[]
 for i in range(int(r)):
  p.append(next(j for j in range(m.ncols()) if rr[i,j]))
 return p
def read_field(b,rows,cols):
 need(b[:8]==b"R150BC31" and struct.unpack_from("<III",b,8)==(31,rows,cols),"paid canonical field header")
 need(len(b)==20+rows*cols and all(x<31 for x in b[20:]),"paid field full extent")
 from flint import nmod_mat
 return nmod_mat(rows,cols,list(b[20:]),31)
def save_field(path,m):
 b=b"R150BC31"+struct.pack("<III",31,m.nrows(),m.ncols())+bytes(int(x) for x in m.entries())
 path.write_bytes(b);return {"file":path.name,**digest(b),"rows":m.nrows(),"cols":m.ncols(),"temporaryOnly":True}
def read_bound(path,magic,k,rows,cols,binding):
 b=path.read_bytes()
 need(b[:8]==magic and struct.unpack_from("<IIII",b,8)==(31,k,rows,cols) and b[24:88].decode()==binding,"source jet binding/header")
 need(len(b)==88+rows*cols and all(x<31 for x in b[88:]),"source jet complete canonical array")
 from flint import nmod_mat
 return nmod_mat(rows,cols,list(b[88:]),31)
def finite_smith(series,left):
 """Exact series unit Schur reduction; unresolved exponents give only a lower bound."""
 from flint import nmod_mat
 mats=series;active=mats[0].nrows();height=0;paid=[];steps=[]
 need(all(x.nrows()==active and x.ncols()==active for x in mats),"small square Schur series")
 while active:
  left();precision=len(mats)-1
  pc=pivots(mats[0]);r=len(pc)
  if r:
   pr=pivots(select(mats[0],list(range(active)),pc).transpose())
   need(len(pr)==r,"actual constant unit row profile")
   rows=pr+[i for i in range(active) if i not in set(pr)]
   cols=pc+[j for j in range(active) if j not in set(pc)]
  else:rows=cols=list(range(active))
  steps.append({"uExponent":height,"activeSize":active,"availableJetDegree":precision,
    "constantRank":r,"unitRows":rows[:r],"unitColumns":cols[:r]})
  paid.extend([height]*r)
  if r==active:
   active=0;break
  m=active-r
  if r:
   blocks=[select(a,rows,cols) for a in mats]
   U=[select(a,list(range(r)),list(range(r))) for a in blocks]
   V=[select(a,list(range(r)),list(range(r,active))) for a in blocks]
   W=[select(a,list(range(r,active)),list(range(r))) for a in blocks]
   Z=[select(a,list(range(r,active)),list(range(r,active))) for a in blocks]
   inv=[U[0].inv()]
   for k in range(1,precision+1):
    s=nmod_mat(r,r,[0]*(r*r),31)
    for i in range(1,k+1):s+=U[i]*inv[k-i]
    inv.append(-inv[0]*s)
   # Verify the complete truncated inverse before using its Schur complement.
   for k in range(precision+1):
    s=nmod_mat(r,r,[0]*(r*r),31)
    for i in range(k+1):s+=U[i]*inv[k-i]
    want=nmod_mat([[int(i==j) for j in range(r)] for i in range(r)],31) if k==0 else nmod_mat(r,r,[0]*(r*r),31)
    need(s==want,"complete small unit series inverse")
   WI=[]
   for k in range(precision+1):
    s=nmod_mat(m,r,[0]*(m*r),31)
    for i in range(k+1):s+=W[i]*inv[k-i]
    WI.append(s)
   schur=[]
   for k in range(precision+1):
    s=Z[k]
    for i in range(k+1):s=s-WI[i]*V[k-i]
    schur.append(s)
  else:schur=mats
  need(zero(schur[0]),"true unit Schur constant remainder zero")
  active=m;height+=1
  if precision==0:
   return {"complete":False,"paidExponents":paid,"unresolvedCount":active,
    "unresolvedExponentAtLeast":height,"determinantOrderLowerBound":sum(paid)+height*active,"steps":steps}
  mats=schur[1:]
 return {"complete":True,"paidExponents":paid,"unresolvedCount":0,"unresolvedExponentAtLeast":None,
  "determinantOrder":sum(paid),"determinantOrderLowerBound":sum(paid),"steps":steps}
def bounded(cmd,seconds,log,memory,grace=5):
 start=time.monotonic()
 with log.open("wb") as f:
  p=subprocess.Popen(["prlimit","--as="+str(memory*1024**2),"--core=0","--"]+list(map(str,cmd)),
      stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
  signalled=False
  try:rc=p.wait(timeout=max(.001,seconds))
  except subprocess.TimeoutExpired:
   signalled=True;os.killpg(p.pid,signal.SIGTERM)
   try:rc=p.wait(timeout=grace)
   except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait();rc=124
 return {"exitCode":rc,"elapsedSeconds":time.monotonic()-start,"sharedDeadlineSignalSent":signalled,"log":log.name}
def main(argv=None):
 ap=argparse.ArgumentParser()
 for n in ("native-model","point-model","selected-model","unit-profile","kernel36","source-dag","repo-notes","first-dir","out"):
  ap.add_argument("--"+n,type=pathlib.Path,required=True)
 ap.add_argument("--maximum-degree",type=int,default=8)
 ap.add_argument("--seconds",type=float,default=60)
 ap.add_argument("--memory-mib",type=int,default=512)
 ap.add_argument("--compile-seconds",type=float,default=30)
 a=ap.parse_args(argv)
 need(1<=a.maximum_degree<=32 and 0<a.seconds<=600 and 0<a.memory_mib<=2048 and 0<a.compile_seconds<=30,"explicit source jet/clock/memory bounds")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 src=pathlib.Path(__file__).resolve().parent;out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 build=out/"build";build.mkdir(exist_ok=True);prefix=out/"natural"
 rp=out/"selected-natural-u-schur-pipeline-receipt.json";cp=out/"complete-jet-checkpoint-files.json"
 rec={"format":"isp-same-selected-natural-u-source-schur-f31-v1","status":"running","phase":"compile",
  "requestedMaximumDegree":a.maximum_degree,"sharedMathematicalSeconds":a.seconds,"memoryMiB":a.memory_mib,
  "compileSecondsLimit":a.compile_seconds,"newLargeGaussianEliminations":0,"newDixonDigitsComputed":0,
  "numpyRequired":False,"sameOriginalIAndJRetained":True,"characteristicZeroInfinityOrderComputed":False,
  "leadingUnitProved":False,"largeDataUploadedOrCommitted":False,"parameters":{},"events":[]}
 start=None;rc=1;temps=[];binding=None
 def left():
  r=a.seconds-(time.monotonic()-start)
  if r<=0:raise BudgetExpired("shared natural-u source deadline")
  return r
 def save():
  if start is not None:rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  rec["parameters"]["temporaryFiles"]=temps;jsave(rp,rec)
 def beat(phase):
  rec["phase"]=phase;save();print(json.dumps({"phase":phase,"elapsedSeconds":None if start is None else time.monotonic()-start}),flush=True)
 try:
  cpp=checked(src/NATIVE,NATIVE_PIN);(build/NATIVE).write_bytes(cpp)
  source_ids={NATIVE:digest(cpp),pathlib.Path(__file__).name:file_identity(pathlib.Path(__file__))}
  for name,pin in HEADERS.items():
   hp=src/name
   if not hp.exists():hp=a.repo_notes/name
   raw=checked(hp,pin);(build/name).write_bytes(raw);source_ids[name]=digest(raw)
  compile_binding=hashlib.sha256(json.dumps(source_ids,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  exe=build/"same-original-natural-u-schur";compile_receipt=build/"compile-receipt.json"
  if exe.exists() and compile_receipt.exists():
   old=json.loads(compile_receipt.read_text())
   need(old["binding"]==compile_binding and old["binary"]==file_identity(exe),"same completed actual native executable")
   rec["compile"]={**old["compile"],"reused":True}
  else:
   cm=bounded(["g++","-std=c++17","-O3","-DNDEBUG","-I",build,build/NATIVE,"-o",exe],a.compile_seconds,out/"compile.log",a.memory_mib)
   rec["compile"]=cm
   if cm["exitCode"]:rec["compile"]["logTail"]=(out/"compile.log").read_text(errors="replace")[-4000:]
   need(cm["exitCode"]==0,"native compile failed or incomplete; see actual compile.log")
   jsave(compile_receipt,{"binding":compile_binding,"binary":file_identity(exe),"compile":cm})
  start=time.monotonic();beat("bind-complete-original-inputs")
  data={k:checked(getattr(a,k),pin) for k,pin in PIN.items()}
  ids={k:digest(v) for k,v in data.items()}
  fd={k:checked(a.first_dir/name,(n,h)) for k,(name,n,h) in FIRST.items()}
  ids.update({"paid_first_"+k:digest(v) for k,v in fd.items()})
  paid=json.loads(fd["receipt"]);par=paid["parameters"]
  need(paid["status"]=="completed" and par["binding"]==FIRST_BINDING,"actual paid first connection")
  need(paid["all4367ConstantKernelProductsZero"] and paid["allOriginalNaturalFirstProductsRetained"] and
    paid["allOriginalParameterCoefficientsModulo31Verified"] and paid["all1309ExactPrimitiveConstantCoefficientsVerified"],
    "all paid original parameter/source identity gates")
  need(paid["selectedNaturalFirstConnectionRankModulo31"]==paid["fullOutputSelectedFirstConnectionRankModulo31"]==3,"actual complete same source first ranks")
  dags={}
  for key,(name,n,h,rn,rh) in DAGS.items():
   raw=checked(a.repo_notes/name,(n,h));ids[key]=digest(raw);un=gzip.decompress(raw)
   need((len(un),hashlib.sha256(un).hexdigest())==(rn,rh),"complete uncompressed prebasis DAG "+key)
   dags[key]=build/(key+".bin");dags[key].write_bytes(un)
  gd=gzip.decompress(data["source_dag"])
  need((len(gd),hashlib.sha256(gd).hexdigest())==(1397793,"41097ab491dcedda36746204a92ab29fcdfe97d09ed03cd9ec66ecd90ed8684c"),"complete original985 source DAG")
  gdfile=build/"paid985-source-dag.bin";gdfile.write_bytes(gd)
  point=json.loads(data["point_model"]);model=decode_json(data["selected_model"]);profile=json.loads(data["unit_profile"])
  sources=list(map(int,point["selectedSourceRows"]));outputs=list(map(int,point["selectedOutputIndicesZeroBased"]))
  independent=list(map(int,point["independentSelectedSourceIndicesZeroBased"]));free_raw=list(map(int,par["selectedFreeOriginalRows"]))
  idx={r:i for i,r in enumerate(sources)};free=[idx[r] for r in free_raw]
  need(len(sources)==len(set(sources))==len(outputs)==len(set(outputs))==1021 and len(independent)==len(set(independent))==985,
    "same paid1021/985 dictionaries")
  need(free_raw==list(map(int,model["freeRows"])) and set(free)==set(range(1021))-set(independent),"same complete36 free indices")
  I=set(map(int,profile["originalOutputI"]));J=set(map(int,model["selectedRows"]))
  need(len(I)==len(J)==4354,"same original complete4354 I,J")
  # Hashes bind raw content and mathematical conventions, never recovery directory names.
  semantic={"sources":source_ids,"inputs":ids,"field":31,"originalRows":4367,"originalSources":6188,
    "constantUnitRank":4318,"freeCoordinates":free_raw,"naturalParameter":"u=1/s; N linear u10 L, Gamma u5 G",
    "normalization":"all4318 fixed unit outputs zero; original36 source free coordinates I"}
  binding=hashlib.sha256(json.dumps(semantic,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":semantic,"selectedFreeOriginalRows":free_raw,
    "requestedMaximumDegree":a.maximum_degree,"sharedMathematicalSeconds":a.seconds,"memoryMiB":a.memory_mib})
  prep=build/"same-selected-model.txt"
  lines=["R150_SELECTED_NATURAL_U_SCHUR31_V1",binding]
  for v in (sources,outputs,independent,free):lines.extend((str(len(v))," ".join(map(str,v))))
  prep.write_text("\n".join(lines)+"\n")
  from flint import nmod_mat
  pj=decode_json(fd["product"])
  need(pj["binding"]==FIRST_BINDING and pj["all4367ConstantProductsZero"],"same full original paid R1")
  R1=nmod_mat(pj["naturalFirstProductRows"],31);need((R1.nrows(),R1.ncols())==(4367,36),"whole4367 R1 shape")
  first_bin=build/"paid-whole-first31.bin";save_field(first_bin,R1)
  # An interrupted invocation may only reuse full layers whose real byte hashes were saved.
  ledger=pathlib.Path(str(prefix)+"-ledger.txt")
  old_n=0
  if ledger.exists():
   need(cp.exists(),"actual completed-layer hash manifest required for resume")
   old=json.loads(cp.read_text());need(old["binding"]==binding,"same source-jet resume binding")
   for e in old["files"]:need(file_identity(out/e["file"])=={"bytes":e["bytes"],"sha256":e["sha256"]},"complete saved source layer SHA")
   lb,ln=ledger.read_text().split();old_n=int(ln)
   need(lb==binding and old_n==old["completedDegree"] and old_n<=a.maximum_degree,"actual completed source-layer cursor")
  beat("native-natural-source-layers")
  nrpath=pathlib.Path(str(prefix)+"-receipt.json")
  if old_n==a.maximum_degree and nrpath.exists():
   nr=json.loads(nrpath.read_text())
   need(nr["inputBinding"]==binding and nr["completedDegree"]==old_n,"actual complete native source receipt")
   rec["nativeStage"]={"exitCode":0,"reusedCompleteRequestedLayers":True,"elapsedSeconds":0}
  else:
   remain=left();native_seconds=max(.01,remain-min(5.0,remain/4))
   cmd=[exe,a.native_model,prep,dags["forward"],dags["backward"],gdfile,a.kernel36,first_bin,prefix,
      str(a.maximum_degree),format(native_seconds,".17g")]
   rec["nativeStage"]=bounded(cmd,left(),out/"native.log",a.memory_mib)
   need(nrpath.exists(),"native stopped before complete stage receipt; completed layer arrays remain temporary")
   nr=json.loads(nrpath.read_text())
  rec["nativeStatistics"]=nr
  rec["parameters"]["nativeSummary"]={k:v for k,v in nr.items() if k!="unitOriginalOutputIndices"}
  need(nr["inputBinding"]==binding and nr["all4354SelectedJetIdentitiesVerified"] and
     nr["all4367OriginalResidualCoordinatesRetained"] and nr["all36FreeSourceCoordinatesVerified"] and
     nr["sameSelectedSourceSupportVerified"],"complete original selected natural source identities")
  n=int(nr["completedDegree"]);need(0<=n<=a.maximum_degree,"actual finite completed degree")
  co=list(map(int,nr["oldCokerOriginalOutputIndices"]));units=list(map(int,nr["unitOriginalOutputIndices"]))
  need(len(co)==len(set(co))==36 and len(units)==len(set(units))==4318 and set(co).isdisjoint(units) and set(co)|set(units)==I,
    "same original selected unit and complement output dictionaries")
  fs=[]
  for k in range(n+1):
   for name in ("source","schur","residual"):
    pp=pathlib.Path(str(prefix)+"-"+name+"-"+str(k)+".bin");fs.append({"file":pp.name,**file_identity(pp),"temporaryOnly":True})
  jsave(cp,{"binding":binding,"completedDegree":n,"files":fs});temps.extend(fs)
  need(rec["nativeStage"]["exitCode"] in (0,75),"native arithmetic/transport failure")
  if n<1:raise BudgetExpired("complete constant layer only")
  beat("exact-small-quotient-and-first-source-comparison")
  S=[read_bound(pathlib.Path(str(prefix)+"-schur-"+str(k)+".bin"),b"R150UJ31",k,36,36,binding) for k in range(n+1)]
  E1=read_bound(pathlib.Path(str(prefix)+"-residual-1.bin"),b"R150UR31",1,4367,36,binding)
  X1=read_bound(pathlib.Path(str(prefix)+"-source-1.bin"),b"R150US31",1,6188,36,binding)
  cj=decode_json(fd["cokernel"]);need(cj["binding"]==FIRST_BINDING,"same paid complete49/36 coker")
  L=nmod_mat(cj["fullProjectedLeftKernel"],31);Z=nmod_mat(cj["excludedRowKernel"],31);LS=L*Z
  need((L.nrows(),L.ncols(),Z.nrows(),Z.ncols())==(585,29,29,26),"same paid complete small dimensions")
  whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
  projected=[i for i,q in enumerate(whole) if 1<=sum(j<=8 for j in q)<=2]
  pureI=list(map(int,par["pureSelectedOutputIndices"]));pureFull=[i for i,q in enumerate(whole) if all(j>=9 for j in q)]
  pi={c:i for i,c in enumerate(projected)}
  F=[]
  for c in pureI:F.append([int(c==v) for v in co])
  for k in range(26):F.append([int(LS[pi[c],k]) if c in pi else 0 for c in co])
  change=nmod_mat(F,31);need(int(change.rank())==36,"complete old-to-new coker change is a field unit")
  beta=nmod_mat(par["selectedConnectionMatrix36"],31)
  need(change*S[1]==beta,"all1296 original sameI first-connection coordinates")
  Erows=matrix_rows(E1)
  low=nmod_mat([Erows[i] for i in projected],31)
  fullbeta=nmod_mat([Erows[i] for i in pureFull]+matrix_rows(L.transpose()*low),31)
  need(fullbeta==read_field(fd["full_connection"],49,36),"all1764 complete full-output first-connection coordinates")
  H=nmod_mat(par["selectedFirstKernelCoefficientMatrix36"],31)
  need((H.nrows(),H.ncols())==(36,33) and int(H.rank())==33,"complete first-kernel source coefficient basis")
  need(zero(E1*H),"all4367 true first corrected source products")
  first_correction=X1*H
  temps.append(save_field(out/"all33-original-first-corrections31.bin",first_correction))
  rec["all33CompleteOriginalFirstCorrectionsVerified"]=True
  rec["all4367FirstCorrectedProductsZero"]=True
  rec["parameters"].update({"sameFirstConnectionRank":3,"completeOldToNewCokernelChange36":matrix_rows(change),
    "oldCokerOriginalOutputIndices":co,"fullOriginalFirstKernelDimension":33,
    "oldFirstProductsRecomputed":False,"sameIAndComplete49FirstCoordinatesVerified":True})
  beat("small-unit-series-schur")
  sm=finite_smith(S,left)
  rec.update({"status":"completed" if n==a.maximum_degree else "checkpointed-time-budget","phase":"complete",
    "completedNaturalDegree":n,"previouslyCompletedNaturalDegree":old_n,
    "all4354SelectedJetIdentitiesVerified":True,"all4367OriginalResidualCoordinatesRetained":True,
    "all36FreeSourceCoordinatesVerified":True,"sameSelectedSourceSupportVerified":True,
    "completeSelectedInfinitySmithLengthComputed":sm["complete"],
    "selectedMinorInfinityOrderModulo31":sm.get("determinantOrder"),
    "selectedMinorInfinityOrderModulo31LowerBound":sm["determinantOrderLowerBound"]})
  rec["parameters"]["smallSeriesSmith"]=sm
  rec["parameters"]["sameSelectedSchurFirstCoefficient"]=matrix_rows(S[1])
  rc=0 if n==a.maximum_degree else 75
 except (BudgetExpired,subprocess.TimeoutExpired) as e:
  rec.update(status="budget-exhausted",error=str(e));rc=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());rc=1
 finally:
  # Preserve byte identities even if a native process stopped after a complete layer.
  if binding is not None:
   ledger=pathlib.Path(str(prefix)+"-ledger.txt")
   if ledger.exists():
    try:
     lb,ln=ledger.read_text().split();nn=int(ln);need(lb==binding,"last complete actual layer binding")
     fs=[]
     for k in range(nn+1):
      for name in ("source","schur","residual"):
       pp=pathlib.Path(str(prefix)+"-"+name+"-"+str(k)+".bin")
       fs.append({"file":pp.name,**file_identity(pp),"temporaryOnly":True})
     jsave(cp,{"binding":binding,"completedDegree":nn,"files":fs})
     rec["parameters"]["actualLastCompleteNativeDegree"]=nn
     known={x["file"] for x in temps};temps.extend(x for x in fs if x["file"] not in known)
    except Exception as e:rec["checkpointInventoryError"]=str(e)
  save()
 need(rp.stat().st_size<100000,"small source/parameter result receipt")
 print(json.dumps(rec,ensure_ascii=False),flush=True);return rc
if __name__=="__main__":sys.exit(main())
