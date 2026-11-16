#!/usr/bin/env python3
"""Original global-source first coefficient127 Bockstein at s=63.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Only already completed original NF/GB/whole-torsion data are consumed.
A positive witness is a global polynomial F127[s] Z relation and receives a
new complete original4367 mod127-square product. No point kernel is used as
a substitute for a global source relation, and no Q membership is inferred.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
P=127;MOD=P*P;ALPHA=63
FORMAT="r150-original127-root63-global-source-bockstein-v1"
NATIVE="2026-11-16-r150-original127-root63-source-bockstein-native-789f.cpp"
NATIVE_SHA="6a932e17fbeb7c81f335281c88bd1dfe0003a09371d454ea23f1861c86823bfc"
NFB="36cdc5a084df381a91838d58a8a9f8adbc255bae39e267f2956fb1170ec0a994"
GBB="9e8510d9519e43fe4f8765a6672194c9dba6d1776a9adf652ac343c5261ebc3e"
WB="05c13d9a57fee12f0751d40feccbfb601686b3d02f497d0e8a99092c44db4211"
RAW_PRIMITIVE=(158741,"fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3")
PAID={
 "model":{"original127-normal-form-input.txt":(140346,"f29e09f075efc20cf9dbc0b78ddffc58c35d46fe26212515397938ba78e853a3")},
 "nf":{
  "original127-normal-form-pipeline-receipt.json":(4468,"e77db837596bfbd988a4dc58dbb631b7ea46cdbeca331be241b82b3ba9b48cfe"),
  "nf-prebasis.bin":(34229300,"c08fb8308bd96fb926e7ae3176e627766b7c6930a2af92afafff318be812f926"),
  "nf-forward.bin":(2434477,"0fe0d5dfde6606ca61907ed043426cd748f6fc11d84df8b3409280d69566f0e0"),
  "nf-backward.bin":(3145942,"6186dab0ec8618ee8eee9d10d92a1c72fe6fb313d49fe64405ed35ab4fbf40cc"),
  "nf-component-dictionary.bin":(8348,"bfafcf821687bf6b3a0c2517606314ec5e4c30a4dfec1140e7f041c5ba01f312"),
  "nf-reduction.bin":(118454308,"5ac3317c3c5af868dff913448fa4d41dca04756fdf942f67908c4d873505d6f1")},
 "gb":{
  "original127-graded-module-pipeline-receipt.json":(5289,"3442ad58f08ff1b7b7b4865bfc7715f43e747f40b65e702e1d4b191142ad17f2"),
  "gb-basis.bin":(43787388,"144871db774835d8b5c369f243cebb441258bc4419d577ed0a0ba3062e21129d"),
  "gb-operations.bin":(763659470,"7c60b9c0466e8cf13bd1b95018beb9b5357cd7d3e2e41e8e6d3655bb05051ba8")},
 "whole":{
  "original127-whole-torsion-pipeline-receipt.json":(9819,"2c1054b2c3224c7c27c4ff09e1852bbab3a219429f8d08528832d81041de8c07"),
  "torsion-whole-state.bin":(1414575,"948d6e78dc96e8d9e367797d33919ce4c1e1deb406dee346505200da00ea4d60"),
  "whole-torsion-characteristic.json":(2560,"ee048002bcda7090ed599709d88ad2d74ecd46448e647bfb3513fa3ad9b64bd6")}}
stopped=False
class Budget(Exception):pass
def stop(sig,frame):
 global stopped
 stopped=True
def need(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def digest(b):return hashlib.sha256(b).hexdigest()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def record(p):return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),"temporaryOnly":True}
def verify(p,pin,label):need(p.is_file() and p.stat().st_size==pin[0] and sha(p)==pin[1],"actual original input "+label)
def atomic(p,x):
 t=p.with_name(p.name+".tmp");t.write_bytes(canonical(x)+b"\n");os.replace(t,p)
def binary(p,b):
 t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
def monomials(d):
 v=[]
 def rec(left,lo,key):
  if not left:v.append(key);return
  for j in range(lo,11):rec(left-1,j,key+(1<<(3*j)))
 rec(d,0,0);return v
def at(poly,a,mod):
 x=0
 for c in reversed(poly):x=(x*a+c)%mod
 return x
def zero(A):return all(int(x)==0 for x in A.entries())
def matrix_record(A):
 b=bytes(int(x) for x in A.entries())
 return {"rows":A.nrows(),"columns":A.ncols(),"entriesHex":b.hex(),"entriesSHA256":digest(b)}
def matrix_read(d,nmod_mat):
 b=bytes.fromhex(d["entriesHex"]);need(len(b)==d["rows"]*d["columns"] and digest(b)==d["entriesSHA256"] and all(x<P for x in b),"complete cached field matrix")
 return nmod_mat(d["rows"],d["columns"],list(b),P)
def row_pivots(R,rank):
 piv=[];prev=-1
 for i in range(rank):
  j=next((j for j in range(R.ncols()) if int(R[i,j])),None)
  need(j is not None and j>prev and int(R[i,j])==1,"actual field RREF pivot")
  piv.append(j);prev=j
 need(all(int(R[i,j])==0 for i in range(rank,R.nrows()) for j in range(R.ncols())),"all point matrix remaining rows zero")
 return piv
def original_coefficients(primitive,model):
 raw=primitive.read_bytes()
 if raw[:2]==b"\x1f\x8b":raw=gzip.decompress(raw)
 need((len(raw),digest(raw))==RAW_PRIMITIVE,"whole primitive integer equations")
 x=json.loads(raw);need(x["format"]=="r150-original-primitive-integer-equations-v1","original primitive schema")
 eq=[[[int(c) for c in pol] for pol in row] for row in x["equations"]]
 need(len(eq)==17 and all(len(row)==77 for row in eq),"original17 by77 polynomial coefficients")
 need(all(int(v)%P for v in [x["denominator"],*x["contents"]]),"original physical-to-primitive constants are127 units")
 tokens=model.read_text().split();at0=0;need(tokens[0]=="R150_NATIVE_NF127_V2","full original127 model");at0=1;checks=0
 def coefficient(pol,k):return pol[k] if k<len(pol) else 0
 for i in range(11):
  need(all(not any(pol[1:]) for pol in eq[i][11:]) and all(not any(pol[11:]) for pol in eq[i][:11]),"original N exact parameter degrees")
  values=[coefficient(eq[i][11+k],0) for k in range(66)]+[coefficient(eq[i][v],d) for v in range(11) for d in range(11)]
  for c in values:need(c%P==int(tokens[at0]),"whole original N coefficient identity");at0+=1;checks+=1
 need(int(tokens[at0])==3333,"original prebasis source count");at0+=1;pre=[]
 for _ in range(3333):pre.append(tuple(map(int,tokens[at0:at0+4])));at0+=4
 for i in range(11,17):
  need(all(not any(pol) for pol in eq[i][:11]) and all(not any(pol[6:]) for pol in eq[i][11:]),"original Gamma exact parameter degrees")
  for k in range(66):
   for d in range(6):need(coefficient(eq[i][11+k],d)%P==int(tokens[at0]),"whole original Gamma coefficient identity");at0+=1;checks+=1
 need(tuple(map(int,tokens[at0:at0+2]))==(2855,9),"all6188 original model complement");at0+=2;rest=[]
 for _ in range(2855):rest.append(tuple(map(int,tokens[at0:at0+3])));at0+=3
 need(list(map(int,tokens[at0:]))==list(range(2,11)) and checks==4433,"all4433 original coefficients and target labels")
 mult=sum((monomials(d) for d in range(4)),[]);index={v:i for i,v in enumerate(mult)};seen=set()
 for e,k,oldpivot,raw_id in pre:
  need(0<=e<11 and k in index and raw_id==17*index[k]+e+1 and raw_id not in seen,"whole distinct prebasis original source");seen.add(raw_id)
 for e,k,raw_id in rest:
  need(0<=e<17 and k in index and raw_id==17*index[k]+e+1 and raw_id not in seen,"whole distinct original complement");seen.add(raw_id)
 need(seen==set(range(1,6189)),"all original6188 sources exactly once")
 variables=[1<<(3*j) for j in range(11)]
 moment=variables+[variables[i]+variables[j] for i in range(11) for j in range(i,11)]
 point=[[(moment[k],v) for k,pol in enumerate(row) if (v:=at(pol,ALPHA,MOD))] for row in eq]
 return point,mult,{"all4433PrimitiveToPaidModelCoefficientChecks":True,"all6188OriginalSourceIdentitiesVerified":True,
  "primitiveDecodedBytes":len(raw),"primitiveDecodedSHA256":digest(raw),"modulus":MOD,"point":ALPHA}
def read_state(path,nmod_mat):
 b=path.read_bytes();need(b[:8]==b"R15TS127" and b[-8:]==b"ENDTS127" and b[8:72].decode()==WB and b[72:136].decode()==GBB,"same complete whole-torsion state")
 geom=struct.unpack_from("<12I",b,136);need(geom==(127,1034,45,1021,8,701,805,13,299,9,506,57),"complete whole state geometry")
 coords=list(struct.iter_unpack("<HB",b[184:184+3*805]));need(len(coords)==805 and all(1<=c<=1034 and 0<=d<8 for c,d in coords),"whole finite-window source component/degree coordinates")
 body=184+3*805+2*13;flags=body+805*805+13*805+9*805;ka=flags+18;ja=ka+299*805;ta=ja+299*299
 need(ja==909073 and len(b)==ta+9*299+506*(4+805)+506*8+8,"whole original basis and free-leakage layout")
 k=b[ka:ja];j=b[ja:ta];need(all(v<P for v in k+j),"canonical complete kernel/action entries")
 return coords,nmod_mat(299,805,list(k),P).transpose(),nmod_mat(299,299,list(j),P)
def original_functional(path,binding):
 b=path.read_bytes();need(b[:8]==b"R15LF127" and b[8:72].decode()==binding and struct.unpack_from("<3I",b,72)==(P,ALPHA,4367) and b[-8:]==b"ENDLF127","complete transported original functional")
 entries=list(struct.iter_unpack("<QB",b[84:-8]));keys=sum((monomials(d) for d in range(1,6)),[])
 need(len(entries)==4367 and [k for k,v in entries]==keys and all(v<P for k,v in entries),"all original output keys in degree order")
 return entries
def main():
 ap=argparse.ArgumentParser()
 for key in ("model-out","normal-forms-out","gb-out","whole-out","primitive","sources-root","out"):ap.add_argument("--"+key,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=1024);ap.add_argument("--compile-seconds",type=float,default=30)
 a=ap.parse_args();need(30<=a.seconds<=600 and 512<=a.memory_mib<=4096 and 1<=a.compile_seconds<=60,"bounded scalar consumer")
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();deadline=start+a.seconds
 rp=a.out/"original127-root63-source-bockstein-receipt.json";mp=a.out/"bockstein-manifest.json"
 r={"format":FORMAT,"status":"running","parameters":{"prime":P,"coefficientModulus":MOD,"point":ALPHA,
   "author":"Astra-ISP-789f / normal_annihilator","aiAssisted":"GPT-6 Astra Pro","allLargeArraysTemporaryOnly":True,
   "normalFormsRecomputed":False,"gradedBasisRecomputed":False,"wholeTorsionRecomputed":False,
   "pointKernelUsedAsGlobalSource":False,"characteristicZeroTargetMembershipInferred":False},"events":[]}
 manifest=None;rc=1
 def save():
  r["elapsedSeconds"]=time.monotonic()-start
  if manifest is not None:r["parameters"]["completedTemporaryPhases"]=manifest["phases"]
  atomic(rp,r)
 def beat():
  if stopped or time.monotonic()>=deadline:raise Budget("stopped at a completed exact phase or retained scalar checkpoint")
 def load_phase(name):
  d=manifest["phases"].get(name)
  if d is None:return None
  p=a.out/d["file"];verify(p,(d["bytes"],d["sha256"]),"complete temporary phase "+name)
  with gzip.open(p,"rb") as f:payload=f.read()
  need(digest(payload)==d["payloadSHA256"],"phase payload "+name);x=json.loads(payload)
  need(x["binding"]==r["binding"] and x["format"]==FORMAT+"-temporary-phase" and x["phase"]==name,"exact phase semantics")
  for fd in x["files"]:verify(a.out/fd["file"],(fd["bytes"],fd["sha256"]),"complete phase output "+fd["file"])
  r["events"].append({"phase":name,"reusedCompletedPhase":True});return x["data"]
 def put_phase(name,data,files=()):
  payload=canonical({"format":FORMAT+"-temporary-phase","binding":r["binding"],"phase":name,"data":data,"files":[record(p) for p in files]})
  p=a.out/(name+".json.gz");tmp=p.with_name(p.name+".tmp")
  with tmp.open("wb") as f:
   with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=1) as g:g.write(payload)
  os.replace(tmp,p);d=record(p);d["payloadSHA256"]=digest(payload);manifest["phases"][name]=d;atomic(mp,manifest)
  r["events"].append({"phase":name,"reusedCompletedPhase":False,"elapsedSeconds":time.monotonic()-start});save();return data
 def limits():
  resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2);resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 def run_native(mode,paths,receipt_path):
  beat();remaining=deadline-time.monotonic();need(remaining>1,"time for next complete native phase")
  log=a.out/(mode+".log");st=time.monotonic();hard=False
  with log.open("ab") as f:
   p=subprocess.Popen([str(binary_path),mode,r["binding"],NFB,GBB,str(remaining),*[str(v) for v in paths]],stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits,start_new_session=True)
   try:code=p.wait(timeout=remaining+8)
   except subprocess.TimeoutExpired:
    hard=True;os.killpg(p.pid,signal.SIGTERM)
    try:code=p.wait(timeout=4)
    except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait();code=75
  event={"phase":mode,"nativeExitCode":code,"nativeWallSeconds":time.monotonic()-st,"nativeHardBudgetStop":hard}
  r["events"].append(event)
  if receipt_path.exists():
   native=json.loads(receipt_path.read_text());need(native.get("binding")==r["binding"],"same native phase binding")
   r["parameters"].setdefault("nativeStatistics",{})[mode]=native;save()
  else:native=None
  if code==75:raise Budget("native complete scalar prefix retained")
  need(code==0 and native is not None and native["status"]=="completed","native "+mode+" failed: "+log.read_bytes()[-3000:].decode(errors="replace"))
  return native
 try:
  limits();signal.signal(signal.SIGTERM,stop)
  from flint import nmod_mat
  directories={"model":a.model_out,"nf":a.normal_forms_out,"gb":a.gb_out,"whole":a.whole_out}
  for group,files in PAID.items():
   for name,pin in files.items():verify(directories[group]/name,pin,group+"/"+name)
  nf=json.loads((a.normal_forms_out/"original127-normal-form-pipeline-receipt.json").read_text())
  gb=json.loads((a.gb_out/"original127-graded-module-pipeline-receipt.json").read_text())
  whole=json.loads((a.whole_out/"original127-whole-torsion-pipeline-receipt.json").read_text())
  need(nf["status"]=="completed" and nf["binding"]==NFB and nf["parameters"]["completeNormalFormAudit"]["noSourceDroppedBeforeOrAfterNormalForms"] is True,"whole original source normal forms")
  gs=gb["parameters"]["nativeStatistics"]
  need(gb["status"]=="completed" and gb["binding"]==GBB and gs["parentNFBinding"]==NFB and gs["allOriginalComplementSourcesCompleted"] and gs["processedSources"]==2855 and gs["basisRank"]==1021 and gs["reductions"]==69407428 and gs["swaps"]==11591 and gs["finalized"],"complete original polynomial source DAG")
  need(whole["status"]=="completed" and whole["binding"]==WB and whole["parameters"]["wholeAffineDegreeVerified"] is True and whole["parameters"]["wholeAffineTorsionDegree"]==299,"complete whole original torsion action")
  char=json.loads((a.whole_out/"whole-torsion-characteristic.json").read_text())
  need(char["status"]=="completed" and char["binding"]==WB and char["characteristicDegree"]==299 and char["completeFactorProductVerified"],"complete action characteristic")
  chi=list(map(int,char["coefficients"]));need(len(chi)==300 and at(chi,ALPHA,P)==0 and at([i*c%P for i,c in enumerate(chi)][1:],ALPHA,P)!=0,"actual sole simple s+64 torsion primary")
  primitive_point,multipliers,original_audit=original_coefficients(a.primitive,a.model_out/"original127-normal-form-input.txt")
  need(sha(a.sources_root/NATIVE)==NATIVE_SHA,"frozen scalar native source")
  identity={"prime":P,"point":ALPHA,"coefficientModulus":MOD,"originalInputs":PAID,"primitiveDecoded":RAW_PRIMITIVE,
   "nfBinding":NFB,"gbBinding":GBB,"wholeBinding":WB,"nativeSHA256":NATIVE_SHA,"wrapperSHA256":sha(Path(__file__)),
   "algorithm":"complete-global-zero-source-scalar-carry-with-positive-original-reverse-product"}
  binding=digest(canonical(identity));r["binding"]=binding;r["parameters"].update({"identity":identity,"originalCoefficientAudit":original_audit,"simplePointPrimaryVerified":True,"seconds":a.seconds,"memoryMiB":a.memory_mib})
  if mp.exists():
   manifest=json.loads(mp.read_text());need(manifest["format"]==FORMAT+"-manifest" and manifest["binding"]==binding,"same immutable scalar consumer")
  else:
   need(not (a.out/"scalar-checkpoint.bin").exists(),"no unbound scalar checkpoint")
   manifest={"format":FORMAT+"-manifest","binding":binding,"identity":identity,"phases":{}};atomic(mp,manifest)
  binary_path=a.out/"original127-root63-source-bockstein-native";build=a.out/"compile.json"
  compiler=subprocess.run(["g++","--version"],capture_output=True,text=True,check=True,timeout=10).stdout.splitlines()[0]
  build_key=digest(canonical({"source":NATIVE_SHA,"compiler":compiler,"flags":["-std=c++17","-O3","-DNDEBUG"]}))
  old=json.loads(build.read_text()) if build.exists() else {}
  if not(binary_path.exists() and old.get("key")==build_key and old.get("binary")==record(binary_path)):
   cs=time.monotonic();cp=subprocess.run(["g++","-std=c++17","-O3","-DNDEBUG",str(a.sources_root/NATIVE),"-o",str(binary_path)],capture_output=True,text=True,timeout=a.compile_seconds)
   r["parameters"]["compileSeconds"]=time.monotonic()-cs;need(cp.returncode==0,"native compilation: "+cp.stderr[-3000:])
   atomic(build,{"key":build_key,"compiler":compiler,"binary":record(binary_path)});r["parameters"]["compileReused"]=False
   deadline+=r["parameters"]["compileSeconds"]
  else:r["parameters"]["compileReused"]=True
  r["parameters"]["compiler"]=compiler;r["parameters"]["binary"]=record(binary_path);save()
  evaluation=a.out/"original-basis-at63.bin"
  d=load_phase("evaluated-original-basis")
  if d is None:
   native=run_native("evaluate",[a.gb_out/"gb-basis.bin",evaluation],Path(str(evaluation)+".json"))
   d=put_phase("evaluated-original-basis",native,[evaluation,Path(str(evaluation)+".json")])
  component=a.out/"component-functional.bin"
  d=load_phase("complete-point-functional")
  if d is None:
   beat();b=evaluation.read_bytes()
   need(b[:8]==b"R15EV127" and b[8:72].decode()==binding and b[72:136].decode()==GBB and struct.unpack_from("<4I",b,136)==(P,ALPHA,1021,1034) and b[-8:]==b"ENDEV127","complete evaluated original GB matrix")
   entries=b[152:-8];need(len(entries)==1021*1034 and all(x<P for x in entries),"whole point matrix coefficients")
   G=nmod_mat(1021,1034,list(entries),P);R,rank=G.rref();rank=int(rank);need(rank==1020,"actual original specialization rank and14 left coordinates")
   piv=row_pivots(R,rank);free=[j for j in range(1034) if j not in set(piv)]
   need(len(free)==14,"complete original point left kernel")
   N=nmod_mat(1034,14,P)
   for j,f in enumerate(free):
    N[f,j]=1
    for i,c in enumerate(piv):N[c,j]=(-int(R[i,f]))%P
   need(zero(G*N),"all14294 original point-basis kernel products")
   coords,K,J=read_state(a.whole_out/"torsion-whole-state.bin",nmod_mat)
   X=nmod_mat(805,14,[(pow(ALPHA,d,P)*int(N[c-1,j]))%P for c,d in coords for j in range(14)],P)
   restriction=X.transpose()*K
   need(int(restriction.rank())==1,"the fourteen point functionals have exactly one nonzero complete-torsion restriction")
   scaled=nmod_mat(14,299,[(ALPHA*int(v))%P for v in restriction.entries()],P)
   need(restriction*J==scaled,"all complete-torsion eigenfunctional products")
   chosen=next(i for i in range(14) if any(int(restriction[i,j]) for j in range(299)))
   pivot=next(j for j in range(299) if int(restriction[chosen,j]));scale=pow(int(restriction[chosen,pivot]),-1,P)
   av=bytes((scale*int(N[i,chosen]))%P for i in range(1034));qv=bytes((scale*int(restriction[chosen,j]))%P for j in range(299))
   need(qv[pivot]==1,"normalized nonzero torsion functional")
   binary(component,b"R15CF127"+binding.encode()+struct.pack("<3I",P,ALPHA,1034)+av+b"ENDCF127")
   d=put_phase("complete-point-functional",{"pointBasisRank":rank,"pointCokernelDimension":14,
    "pointOriginalRank":3333+rank,"completeTorsionRestrictionRank":1,"allPointBasisProductsVerified":True,
    "pointBasisProductCount":1021*14,"allTorsionEigenfunctionalProductsVerified":True,"torsionEigenProductCount":14*299,
    "selectedNullspaceColumn":chosen,"normalizingTorsionCoordinate":pivot,"normalizingFieldScale":scale,
    "componentFunctionalSHA256":digest(av),"torsionFunctionalSHA256":digest(qv),
    "torsionFunctionalHex":qv.hex(),"completePointKernel":matrix_record(N),"wholeRestriction":matrix_record(restriction)},[component])
  r["parameters"]["pointFunctionalAudit"]={k:v for k,v in d.items() if k not in ("completePointKernel","wholeRestriction","torsionFunctionalHex")};save()
  ell_file=a.out/"original4367-functional.bin"
  d=load_phase("original-functional-transport")
  if d is None:
   native=run_native("transport",[a.normal_forms_out/"nf-prebasis.bin",a.normal_forms_out/"nf-component-dictionary.bin",component,ell_file],Path(str(ell_file)+".json"))
   d=put_phase("original-functional-transport",native,[ell_file,Path(str(ell_file)+".json")])
  ell_entries=original_functional(ell_file,binding);ell=dict(ell_entries);output_index={k:i for i,(k,v) in enumerate(ell_entries)}
  leaves=a.out/"original6188-divided-scalar-leaves.bin"
  d=load_phase("original-integer-scalar-leaves")
  if d is None:
   beat();payload=bytearray();checks=0;nonzero=0
   for key in multipliers:
    for equation in range(17):
     value=sum(v*ell[key+k] for k,v in primitive_point[equation])%MOD
     need(value%P==0,"every one of6188 complete original point columns annihilated")
     payload+=struct.pack("<HB",value,value//P);nonzero+=value!=0;checks+=len(primitive_point[equation])
   need(len(payload)==3*6188,"complete original monomial-major scalar leaves")
   binary(leaves,b"R15SC127"+binding.encode()+struct.pack("<3I",P,ALPHA,6188)+payload+b"ENDSC127")
   d=put_phase("original-integer-scalar-leaves",{"all6188OriginalPointProductsZeroMod127":True,"all6188OriginalScalarsComputedMod16129":True,
    "all6188OriginalScalarsExactlyDividedBy127":True,"sourceCoefficientProducts":checks,"nonzeroDividedLeafCount":nonzero,
    "leafPayloadSHA256":digest(payload),"originalOutputFunctionalSHA256":digest(bytes(v for k,v in ell_entries))},[leaves])
  r["parameters"]["originalScalarAudit"]=d;save()
  paths=[leaves,a.normal_forms_out/"nf-forward.bin",a.normal_forms_out/"nf-backward.bin",a.normal_forms_out/"nf-reduction.bin",a.gb_out/"gb-operations.bin",a.out]
  d=load_phase("complete-global-source-scalar-scan")
  if d is None:
   native=run_native("replay",paths,a.out/"scalar-replay-native.json")
   need(native["all1834GlobalZeroEndpointsCovered"] is True and native["globalZeroEndpoints"]==1834 and native["GBReductions"]==69407428 and native["allGlobalSourceRoutesVerified"],"all complete polynomial source syzygies tested")
   d=put_phase("complete-global-source-scalar-scan",native,[a.out/"scalar-checkpoint.bin",a.out/"scalar-replay-native.json"])
  r["parameters"]["sourceDAGAudit"]=d;positive=d["nonzeroBocksteinEndpoints"]>0
  r["parameters"]["nonzeroGlobalSourceCarryFound"]=positive;save()
  if not positive:
   r["status"]="completed";r["outcome"]="all-complete-global-source-first-carries-zero-at63"
   r["parameters"].update({"globalPolynomialZeroRelationsCovered":1834,"newCoefficient127TorsionDirectionProved":False,
    "negativeScope":"only the first coefficient127 Bockstein at the actual simple s+64 primary",
    "higherCoefficient127TorsionExcluded":False,"characteristicZeroAffineDegreeImproved":False})
   rc=0
  else:
   witness_path=a.out/"positive-original-source-evaluated.bin"
   d=load_phase("positive-source-reverse")
   if d is None:
    native=run_native("witness",paths,a.out/"witness-reverse-native.json")
    need(native["all6188EvaluatedSourceScalarProductsVerified"] is True and 0<native["bocksteinResidue"]<P,"complete positive original source evaluation")
    d=put_phase("positive-source-reverse",native,[witness_path,a.out/"witness-reverse-native.json"])
   r["parameters"]["reverseWitnessAudit"]=d
   final=load_phase("full-original-positive-certificate")
   if final is None:
    beat();b=witness_path.read_bytes()
    need(b[:8]==b"R15YV127" and b[8:72].decode()==binding and b[-8:]==b"ENDYV127","positive original evaluated source binding")
    p,alpha,count,node,ordinal,raw=struct.unpack_from("<6I",b,72);residue=b[96]
    need((p,alpha,count)==(P,ALPHA,6188) and node==d["originalGlobalZeroNode"] and ordinal==d["inputOrdinal"] and raw==d["inputOriginalRawSource"] and residue==d["bocksteinResidue"],"same exact global zero endpoint")
    y=[v[0] for v in struct.iter_unpack("<H",b[97:-8])]
    need(len(y)==6188 and all(v<MOD for v in y),"all original6188 source coordinates modulo127-square")
    product=[0]*4367;terms=0;support=0
    for i,key in enumerate(multipliers):
     for eq in range(17):
      a0=y[17*i+eq]
      if not a0:continue
      support+=1
      for mon,c in primitive_point[eq]:product[output_index[key+mon]]+=a0*c;terms+=1
    product=[v%MOD for v in product]
    need(all(v%P==0 for v in product),"all4367 original source products divisible by127")
    divided=bytes(v//P for v in product);reading=sum(v*q for (k,v),q in zip(ell_entries,divided))%P
    need(reading==residue and reading!=0,"nonzero original4367 first coefficient Bockstein product")
    product_path=a.out/"positive-original-divided-product.bin"
    binary(product_path,b"R15BV127"+binding.encode()+struct.pack("<4I",P,ALPHA,4367,node)+divided+b"ENDBV127")
    final=put_phase("full-original-positive-certificate",{"globalZeroNode":node,"originalInputOrdinal":ordinal,"originalInputRawSource":raw,
     "bocksteinResidue":residue,"all4367OriginalProductCoordinatesDivisibleBy127":True,
     "all4367OriginalProductCoordinatesVerified":True,"all6188OriginalSourceCoordinatesRetained":True,
     "originalSourceSupport":support,"originalSourceCoefficientProducts":terms,
     "dividedProductSHA256":digest(divided),"fullOriginalFunctionalProductVerified":True,
     "globalPolynomialRelationScope":"A(s)y(s) is coefficientwise zero modulo127 by the paid complete F/B, NF and GB Z-source recipe",
     "sourceEvaluationIsTheIntegerLiftDAGEvaluatedModulo16129":True,
     "pointOnlySourceKernelSubstitution":False,"nonzeroClassInCoefficient127CokerMod127":True,
     "atLeastOneCoefficient127ExponentOneDirection":True},[product_path])
   r["parameters"]["positiveCertificate"]=final
   r["parameters"].update({"newCoefficient127TorsionDirectionProved":True,"coefficient127TorsionLowerBound":1,
    "affineDegreeUpper298FollowsWithSeparatelyPaidWhole299AndJ127Zero":True,
    "characteristicZeroTargetMembershipInferred":False,"allOriginalPolynomialSourceCoordinatesExpanded":False,
    "globalSourceReproducibleFromPaidDAGAndZeroNode":True,"noClaimAboutAdditionalCoefficient127PrimaryDirections":True})
   r["status"]="completed";r["outcome"]="positive-first-coefficient127-torsion-with-complete-original-source-product";rc=0
 except Budget as e:
  r["status"]="budget-checkpoint";r["outcome"]="completed-phases-and-whole-scalar-prefix-retained";r["error"]=str(e);r["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};rc=75
 except BaseException as e:
  r["status"]="failed";r["errorType"]=type(e).__name__;r["error"]=str(e);r["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};rc=1
 finally:
  checkpoint=a.out/"scalar-checkpoint.bin"
  if checkpoint.exists():r["parameters"]["scalarCheckpoint"]=record(checkpoint)
  for mode in ("replay","witness"):
   p=a.out/("scalar-replay-native.json" if mode=="replay" else "witness-reverse-native.json")
   if p.exists():
    try:
     d=json.loads(p.read_text())
     if d.get("binding")==r.get("binding"):r["parameters"].setdefault("nativeStatistics",{})[mode]=d
    except (ValueError,OSError):pass
  if manifest is not None:r["parameters"]["manifest"]=record(mp)
  save()
 print(json.dumps({"status":r["status"],"outcome":r.get("outcome"),"elapsedSeconds":r["elapsedSeconds"],"error":r.get("error")}),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
