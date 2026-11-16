#!/usr/bin/env python3
"""Complete original generalized coefficient-127 Bockstein on one critical primary.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Consume an immutable complete detector phase, transport to all4367 original
outputs, replay all global polynomial source relations modulo127-square,
and verify positive generators by full original multiplication.
All1834 Z sources are retained. A zero result concerns only the first
coefficient image on this primary, never higher coefficient torsion or Q
target membership. Aggregate parent manifests may append unrelated phases.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,math,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
P=127;MOD=16129
FORMAT="r150-original127-complete-generalized-source-bockstein-v1"
PARENT_FORMAT="r150-original127-complete-generalized-critical-detectors-v1"
PARENT_BINDING="45dfea7c2c8ac12c7f3e5bd0ecd0e4e29937c11f767625e2ab36e9cd2ec6c35e"
PARENT_SHA="e762cf7703e83c63de4c121a926844fd4e5583a4e4ec59ed889fe79cd51fd9ad"
PROFILE_BINDING="7fd6a5d4a535e55f7fb06909bcec10634e7c8e0706f8fa1bd6dfd115a6da51c2"
PROFILE_MANIFEST=(1379,"1a5901c7b7621dbfcc4b73bf3ee032872948e0a988291b6c7a3ac1d8017cd654")
NATIVE="2026-11-16-r150-original127-generalized-source-bockstein-native-789f.cpp"
NATIVE_PIN=(37127,"61e2c2dbbbb0c07e4c936f29ab17bb74b18e453aacea7e3ff207e627f8dbdc55")
SCALAR_CPP="2026-11-16-r150-original127-root63-source-bockstein-native-789f.cpp"
SCALAR_CPP_PIN=(24871,"6a932e17fbeb7c81f335281c88bd1dfe0003a09371d454ea23f1861c86823bfc")
SCALAR_PY="2026-11-16-r150-original127-root63-source-bockstein-789f.py"
SCALAR_PY_PIN=(27228,"3ee3b83dbac5fa3f96aea04cfc01a7c86cf2423fd027f050bc46f3a97406253f")
MATRIX_PY="2026-11-16-r150-original127-nine-target-cyclic-module-789f.py"
MATRIX_PY_PIN=(20947,"d520b190ac84f1990ed8ee84d405cc34c31d09e140ad26b8442c099872d26ed3")
LABELS=("FPlus-1","FMinus-1","E8-1","E8-2","E8-3")
stopped=False
class Budget(Exception):pass
def stop(signum,frame):
 global stopped
 stopped=True
def need(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def digest(b):return hashlib.sha256(b).hexdigest()
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def verify(p,pin,label):
 need(p.is_file() and p.stat().st_size==pin[0] and sha(p)==pin[1],"actual bytes: "+label)
def atomic(p,x):
 tmp=p.with_name(p.name+".tmp");tmp.write_bytes(canonical(x)+b"\n");os.replace(tmp,p)
def binary(p,b):
 tmp=p.with_name(p.name+".tmp");tmp.write_bytes(b);os.replace(tmp,p)
def import_source(p,name):
 spec=importlib.util.spec_from_file_location(name,p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
def identity(n,nmod_mat):return nmod_mat(n,n,[int(i==j) for i in range(n) for j in range(n)],P)
def zero(A):return all(int(v)==0 for v in A.entries())
def matrix_equal_record(A,B):return A.nrows()==B.nrows() and A.ncols()==B.ncols() and A==B
def read_parent_phase(root,name,descriptor,binding,format_name):
 need(Path(descriptor["file"]).name==descriptor["file"],"parent phase is a local filename")
 path=root/descriptor["file"];verify(path,(descriptor["bytes"],descriptor["sha256"]),"immutable parent "+name)
 payload=gzip.decompress(path.read_bytes());need(digest(payload)==descriptor["payloadSHA256"],"exact parent phase payload "+name)
 data=json.loads(payload)
 need(data["binding"]==binding and data["format"]==format_name+"-temporary-phase" and data["phase"]==name,"exact parent phase identity "+name)
 return data["data"]
def theta_matrix(h,order,nmod_mat):
 d=len(h)-1;L=d*order;v=[0]*(L*L)
 for k in range(order):
  for e in range(d):
   if e:v[(k*d+e)*L+k*d+e-1]=1
   v[(k*d+e)*L+k*d+d-1]=(-h[e])%P
   if k:v[(k*d+e)*L+(k-1)*d+e]=1
 return nmod_mat(L,L,v,P)
def encode_config(binding,nfb,gbb,h,order,columns,original):
 d=len(h)-1;L=d*order;T=columns*L
 need(len(original)==order and all(A.nrows()==1034*d and A.ncols()==columns for A in original),"all original component jet coefficients")
 flat=bytes(int(original[k][c*d+e,j]) for c in range(1034) for j in range(columns) for k in range(order) for e in range(d))
 need(len(flat)==1034*T,"complete generalized config ordering")
 return (b"R15GX127"+binding.encode()+nfb.encode()+gbb.encode()+struct.pack("<4I",P,d,order,columns)+bytes(h)+flat+b"ENDGX127")
def encode_primitive(primitive,scalar,binding):
 raw=primitive.read_bytes()
 if raw[:2]==b"\x1f\x8b":raw=gzip.decompress(raw)
 need((len(raw),digest(raw))==scalar.RAW_PRIMITIVE,"complete original primitive before generalized lift")
 obj=json.loads(raw);eq=[[[int(c) for c in pol] for pol in row] for row in obj["equations"]]
 need(len(eq)==17 and all(len(row)==77 for row in eq),"all original parameter polynomials")
 out=bytearray(b"R15GI127"+binding.encode()+struct.pack("<3I",MOD,17,77));count=0
 for row in eq:
  for pol in row:
   need(len(pol)<=11,"complete original parameter degree")
   out.append(len(pol))
   for c in pol:out.extend(struct.pack("<H",c%MOD));count+=1
 out.extend(b"ENDGI127")
 return bytes(out),{"allOriginal17By77ParameterPolynomialsRetained":True,"storedOriginalPolynomialCoefficientCount":count,
  "integerModulus":MOD,"integerPolynomialModelNotPointEvaluation":True}
def read_original_ell(path,binding,h,order,columns,scalar):
 raw=path.read_bytes();d=len(h)-1;T=d*order*columns
 need(raw[:8]==b"R15GL127" and raw[8:72].decode()==binding and raw[-8:]==b"ENDGL127","whole original generalized functional")
 need(struct.unpack_from("<5I",raw,72)==(P,d,order,columns,4367),"same original output geometry")
 need(len(raw)==92+4367*(8+T)+8,"whole original functional byte count")
 keys=sum((scalar.monomials(k) for k in range(1,6)),[]);off=92;values=[]
 for key in keys:
  need(struct.unpack_from("<Q",raw,off)[0]==key,"every original output monomial");off+=8
  v=raw[off:off+T];off+=T;need(all(c<P for c in v),"canonical original functional");values.append(v)
 return keys,values
def read_all_z(path,binding,h,order,columns,nmod_mat):
 b=path.read_bytes();d=len(h)-1;T=d*order*columns
 need(b[:8]==b"R15GZ127" and b[8:72].decode()==binding and b[-8:]==b"ENDGZ127","complete original Z values")
 need(struct.unpack_from("<5I",b,72)==(P,d,order,columns,1834),"all1834 original global polynomial zero sources")
 need(len(b)==92+1834*(12+T)+8,"complete Z values exact length")
 off=92;labels=[];values=[];seen=set()
 for _ in range(1834):
  ordinal,raw,node=struct.unpack_from("<3I",b,off);off+=12
  need(1<=ordinal<=2855 and 1<=raw<=6188 and 1<=node<=2855+69407428 and ordinal not in seen,"distinct original global Z endpoint")
  seen.add(ordinal);labels.append({"ordinal":ordinal,"originalRawSource":raw,"globalNode":node})
  v=b[off:off+T];off+=T;need(all(x<P for x in v),"complete canonical divided source values");values.extend(v)
 return labels,nmod_mat(1834,T,values,P).transpose()
def complete_image(V,R,J,helper,nmod_mat,nmod_poly,beat):
 n=J.nrows();need(J.ncols()==n and R.ncols()==n and V.nrows()==R.nrows() and V.ncols()==1834,"same complete primary detector coordinates")
 RR,rank=R.transpose().rref();need(int(rank)==n,"actual full primary restriction rank")
 rows=helper.pivots(RR,n);unit=helper.choose_rows(R,rows,nmod_mat);inverse=unit.inv()
 need(unit*inverse==identity(n,nmod_mat),"actual complete detector unit inverse")
 U=inverse*helper.choose_rows(V,rows,nmod_mat)
 need(R*U==V,"all1834 generalized source values recovered in the original complete primary")
 image=nmod_mat(n,0,P);selected=[];hist=[];cycles={}
 def cycle(j):
  if j in cycles:return cycles[j]
  x=helper.choose_columns(U,[j],nmod_mat);parts=[]
  for _ in range(n):
   parts.append(x);x=J*x
  Z=nmod_mat(n,n,[int(parts[k][i,0]) for i in range(n) for k in range(n)],P)
  cycles[j]=Z;return Z
 nonzero=[j for j in range(1834) if any(int(U[i,j]) for i in range(n))]
 while True:
  beat();old=image.ncols();best=None;best_rank=old;best_trial=None
  for j in nonzero:
   if j in selected:continue
   Z=cycle(j);trial=nmod_mat(n,old+n,[int(image[i,k]) if k<old else int(Z[i,k-old]) for i in range(n) for k in range(old+n)],P)
   T,rr=trial.transpose().rref();rr=int(rr)
   if rr>best_rank:
    # Transposed RREF rows span the image in original primary coordinates.
    best=j;best_rank=rr;best_trial=T
   if best_rank==n:break
  if best is None:break
  selected.append(best);hist.append(best_rank)
  image=nmod_mat(n,best_rank,[int(best_trial[k,i]) for i in range(n) for k in range(best_rank)],P)
  if best_rank==n:break
 b=image.ncols()
 if b:
  trans,rank=image.transpose().rref();need(int(rank)==b,"actual complete coefficient image basis")
  erows=helper.pivots(trans,b);E=helper.choose_rows(image,erows,nmod_mat);ei=E.inv()
  coords=ei*helper.choose_rows(U,erows,nmod_mat);action=ei*helper.choose_rows(J*image,erows,nmod_mat)
  need(image*coords==U,"all1834 original sources belong to the complete image")
  need(image*action==J*image,"complete original parameter image closure")
  cp=helper.monic(action.charpoly(),nmod_poly);mp=helper.monic(action.minpoly(),nmod_poly)
 else:
  coords=nmod_mat(0,1834,P);action=nmod_mat(0,0,P);need(zero(U),"zero complete original coefficient image")
  cp=nmod_poly([1],P);mp=nmod_poly([1],P);erows=[]
 # Selected actual Z sources, with all their parameter multiples, span image.
 selected_cols=[]
 for j in selected:
  Z=cycle(j)
  selected_cols.extend([helper.choose_columns(Z,[k],nmod_mat) for k in range(n)])
 check=nmod_mat(n,len(selected_cols),[int(selected_cols[j][i,0]) for i in range(n) for j in range(len(selected_cols))],P)
 need(int(check.rank())==b,"all selected original global Z cyclic sources span the exact image")
 return {"completeOriginalPrimaryCoordinates":helper.mat_data(U),"imageBasis":helper.mat_data(image),
  "imageAction":helper.mat_data(action),"allOriginalSourceImageCoordinates":helper.mat_data(coords),
  "detectorUnitRows":rows,"imageCoordinateRows":erows,"selectedOriginalZeroIndices":selected,
  "selectedCoverageRanks":hist,
  "summary":{"originalGlobalZeroSources":1834,"nonzeroZeroEndpointsNotDimension":len(nonzero),
   "completeFirstCoefficientImageDimension":b,"selectedActualOriginalSourceCount":len(selected),
   "selectedCoverageRanks":hist,"originalPrimaryDimension":n,
   "all1834OriginalDetectorCoordinateProductsVerified":True,"originalDetectorCoordinateProducts":R.nrows()*1834,
   "all1834SourcesInCompleteImageVerified":True,"allOriginalImageParameterProductsVerified":True,
   "completeImageActionProductCoordinates":n*b,"selectedOriginalSourceCyclicSpansComplete":True,
   "imageCharacteristic":helper.poly_summary(cp,nmod_poly),"imageMinimalPolynomial":helper.poly_summary(mp,nmod_poly),
   "onlyFirstCoefficientImage":True,"higherCoefficientTorsionExcluded":False}}

def main():
 ap=argparse.ArgumentParser()
 for key in ("model-out","normal-forms-out","gb-out","whole-out","profile-out","detectors-out","primitive","sources-root","out"):
  ap.add_argument("--"+key,type=Path,required=True)
 ap.add_argument("--factor",choices=LABELS,required=True)
 ap.add_argument("--detector-receipt-bytes",type=int,required=True)
 ap.add_argument("--detector-receipt-sha256",required=True)
 ap.add_argument("--seconds",type=float,default=300);ap.add_argument("--memory-mib",type=int,default=4096)
 ap.add_argument("--compile-seconds",type=float,default=30);ap.add_argument("--through",choices=("scan","final"),default="final")
 a=ap.parse_args()
 need(30<=a.seconds<=3600 and 1024<=a.memory_mib<=8192 and 1<=a.compile_seconds<=60,"bounded complete generalized consumer")
 need(a.detector_receipt_bytes>0 and len(a.detector_receipt_sha256)==64 and all(c in "0123456789abcdef" for c in a.detector_receipt_sha256),"actual selected parent receipt pin")
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();deadline=start+a.seconds
 rp=a.out/"original127-generalized-source-bockstein-receipt.json";mp=a.out/"generalized-bockstein-manifest.json"
 r={"format":FORMAT,"status":"running","parameters":{"prime":P,"coefficientModulus":MOD,"factorLabel":a.factor,
  "author":"Astra-ISP-789f / normal_annihilator","aiAssisted":"GPT-6 Astra Pro",
  "allLargeArraysTemporaryOnly":True,"normalFormsRecomputed":False,"gradedBasisRecomputed":False,
  "wholeTorsionRecomputed":False,"pointKernelUsedAsGlobalSource":False,
  "higherCoefficientTorsionExcluded":False,"characteristicZeroTargetMembershipInferred":False},"events":[]}
 manifest=None;rc=1;binding=None
 def rec(p):
  return {"file":p.relative_to(a.out).as_posix(),"bytes":p.stat().st_size,"sha256":sha(p),"temporaryOnly":True}
 def save():
  r["elapsedSeconds"]=time.monotonic()-start
  if manifest is not None:
   r["parameters"]["completedTemporaryPhases"]=manifest["phases"]
   if manifest.get("nativeCheckpoint"):r["parameters"]["nativeCheckpoint"]=manifest["nativeCheckpoint"]
  atomic(rp,r)
 def beat():
  if stopped or time.monotonic()>=deadline:raise Budget("bounded complete phase or whole original source checkpoint retained")
 def limits():
  resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2);resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 def cached(name):
  descriptor=manifest["phases"].get(name)
  if descriptor is None:return None
  p=a.out/descriptor["file"];verify(p,(descriptor["bytes"],descriptor["sha256"]),"complete generalized phase "+name)
  payload=gzip.decompress(p.read_bytes());need(digest(payload)==descriptor["payloadSHA256"],"whole cached phase payload")
  obj=json.loads(payload);need(obj["format"]==FORMAT+"-temporary-phase" and obj["binding"]==binding and obj["phase"]==name,"same immutable generalized phase")
  for fd in obj["files"]:
   fp=a.out/fd["file"];need(fp.resolve().is_relative_to(a.out.resolve()),"phase output stays in its actual temporary directory")
   verify(fp,(fd["bytes"],fd["sha256"]),"complete bound output "+fd["file"])
  r["events"].append({"phase":name,"reusedCompletedPhase":True});return obj["data"]
 def put(name,data,files=()):
  payload=canonical({"format":FORMAT+"-temporary-phase","binding":binding,"phase":name,"data":data,"files":[rec(p) for p in files]})
  p=a.out/(name+".json.gz");tmp=p.with_name(p.name+".tmp")
  with tmp.open("wb") as f:
   with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=1) as z:z.write(payload)
  os.replace(tmp,p);descriptor=rec(p);descriptor["payloadSHA256"]=digest(payload)
  manifest["phases"][name]=descriptor;atomic(mp,manifest)
  r["events"].append({"phase":name,"reusedCompletedPhase":False,"elapsedSeconds":time.monotonic()-start});save();return data
 def inspect_scan():
  selector=a.out/"scan"/"generalized-active.bin"
  if not selector.exists():return
  b=selector.read_bytes()
  need(len(b)==92 and b[:8]==b"R15GVACT" and b[8:72].decode()==binding and b[-8:]==b"ENDGVACT","whole native checkpoint selector")
  generation,slot=struct.unpack_from("<QI",b,72)
  need(slot==generation%2,"whole native checkpoint generation")
  path=a.out/"scan"/("generalized-checkpoint-"+str(slot)+".bin")
  with path.open("rb") as f:
   prefix=f.read(224);f.seek(-8,2);tail=f.read(8)
  need(prefix[:8]==b"R15GT127" and prefix[8:72].decode()==binding and prefix[72:136].decode()==scalar.NFB and prefix[136:200].decode()==scalar.GBB and tail==b"ENDGT127","whole native checkpoint source bindings")
  need(struct.unpack_from("<4I",prefix,200)==(P,d,order,columns) and struct.unpack_from("<Q",prefix,216)[0]==generation,"same original checkpoint detector geometry")
  old=manifest.get("nativeCheckpoint")
  need(old is None or generation>=old["generation"],"native checkpoint never loses a committed source prefix")
  new={"generation":generation,"selector":rec(selector),"activeState":rec(path),"allDataTemporaryOnly":True}
  if old is not None and generation==old["generation"]:
   need(new==old,"same completed native checkpoint bytes")
  manifest["nativeCheckpoint"]=new;atomic(mp,manifest)
 def run_native(mode,paths,nreceipt):
  beat();remaining=deadline-time.monotonic()
  if remaining<2:raise Budget("insufficient time for another complete native boundary")
  log=a.out/(mode+".log");began=time.monotonic();hard=False
  with log.open("ab") as f:
   child=subprocess.Popen([str(executable),mode,binding,scalar.NFB,scalar.GBB,str(remaining),str(config),*[str(p) for p in paths]],
    stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits,start_new_session=True)
   try:code=child.wait(timeout=remaining+8)
   except subprocess.TimeoutExpired:
    hard=True;os.killpg(child.pid,signal.SIGTERM)
    try:code=child.wait(timeout=4)
    except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait();code=75
  event={"phase":mode,"nativeExitCode":code,"nativeWallSeconds":time.monotonic()-began,"nativeHardBudgetStop":hard}
  r["events"].append(event);native=None
  if nreceipt.exists():
   native=json.loads(nreceipt.read_text())
   need(native.get("binding")==binding,"same original generalized native phase")
   r["parameters"].setdefault("nativeStatistics",{})[mode]=native
  if mode=="scan":inspect_scan()
  save()
  if code==75:raise Budget("native complete source prefix retained; this is not an all-zero conclusion")
  need(code==0 and native is not None and native.get("status")=="completed","native "+mode+" failed: "+log.read_bytes()[-3000:].decode(errors="replace"))
  return native
 try:
  limits();signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
  from flint import nmod_mat,nmod_poly
  for file,pin in ((SCALAR_PY,SCALAR_PY_PIN),(MATRIX_PY,MATRIX_PY_PIN),(SCALAR_CPP,SCALAR_CPP_PIN),(NATIVE,NATIVE_PIN)):
   verify(a.sources_root/file,pin,"frozen consumer dependency "+file)
  scalar=import_source(a.sources_root/SCALAR_PY,"paid_generalized_original_scalar_reader")
  helper=import_source(a.sources_root/MATRIX_PY,"paid_generalized_original_matrix_reader")
  directories={"model":a.model_out,"nf":a.normal_forms_out,"gb":a.gb_out,"whole":a.whole_out}
  for group,files in scalar.PAID.items():
   for name,pin in files.items():verify(directories[group]/name,pin,"paid complete original "+group+"/"+name)
  nfr=json.loads((a.normal_forms_out/"original127-normal-form-pipeline-receipt.json").read_text())
  gbr=json.loads((a.gb_out/"original127-graded-module-pipeline-receipt.json").read_text())
  whr=json.loads((a.whole_out/"original127-whole-torsion-pipeline-receipt.json").read_text())
  need(nfr["status"]=="completed" and nfr["binding"]==scalar.NFB and nfr["parameters"]["completeNormalFormAudit"]["noSourceDroppedBeforeOrAfterNormalForms"],"all6188 source normal forms")
  gs=gbr["parameters"]["nativeStatistics"]
  need(gbr["status"]=="completed" and gbr["binding"]==scalar.GBB and gs["parentNFBinding"]==scalar.NFB and gs["allOriginalComplementSourcesCompleted"] and gs["processedSources"]==2855 and gs["basisRank"]==1021 and gs["reductions"]==69407428 and gs["swaps"]==11591 and gs["finalized"],"whole original global source DAG")
  need(whr["status"]=="completed" and whr["binding"]==scalar.WB and whr["parameters"]["wholeAffineDegreeVerified"] and whr["parameters"]["wholeAffineTorsionDegree"]==299,"complete original299 torsion")
  parent_path=a.detectors_out/("original127-generalized-detectors-"+a.factor+"-receipt.json")
  verify(parent_path,(a.detector_receipt_bytes,a.detector_receipt_sha256),"actual selected complete detector receipt")
  parent=json.loads(parent_path.read_text());pp=parent["parameters"]
  need(parent["format"]==PARENT_FORMAT and parent["status"]=="completed" and parent["binding"]==PARENT_BINDING and pp["factorLabel"]==a.factor,"same completed original generalized parent")
  need(pp["identity"]["wrapperSHA256"]==PARENT_SHA and digest(canonical(pp["identity"]))==PARENT_BINDING,"exact frozen parent semantic binding")
  finalname=a.factor+"-complete-original-component-detectors";commonname="original-degree-zero-unit-quotient"
  selected_desc=pp["completedTemporaryPhases"][finalname];common_desc=pp["completedTemporaryPhases"][commonname]
  parent_manifest=json.loads((a.detectors_out/"generalized-detectors-manifest.json").read_text())
  need(parent_manifest["format"]==PARENT_FORMAT+"-manifest" and parent_manifest["binding"]==PARENT_BINDING,"same append-only parent manifest")
  for name,descriptor in ((finalname,selected_desc),(commonname,common_desc)):
   need(parent_manifest["phases"].get(name)==descriptor,"selected immutable descriptor survives other factor appends")
  final=read_parent_phase(a.detectors_out,finalname,selected_desc,PARENT_BINDING,PARENT_FORMAT)
  common=read_parent_phase(a.detectors_out,commonname,common_desc,PARENT_BINDING,PARENT_FORMAT)
  need(common["summary"]==pp["degreeZeroQuotient"] and common["summary"]["allOriginalZeroRowProductsVerified"] and common["summary"]["allPositiveOriginalRowsProjected"],"complete common original unit quotient")
  fs=final["summary"];need(fs==pp["completeGeneralizedDetectors"],"same complete original detector summary")
  need(fs["allCriticalPrimaryDirectionsSeparated"] and fs["allOriginalGBJetProductsVerified"] and fs["allPrimaryParameterIntertwiningProductsVerified"] and fs["originalNFComponentCount"]==1034 and fs["factorLabel"]==a.factor,"complete generalized original GB detector")
  verify(a.profile_out/"critical-primary-manifest.json",PROFILE_MANIFEST,"actual complete primary manifest")
  pm=json.loads((a.profile_out/"critical-primary-manifest.json").read_text())
  need(pm["binding"]==PROFILE_BINDING,"same complete original primary profile")
  pd=pm["phases"]["primary-"+a.factor];path=a.profile_out/pd["file"]
  verify(path,(pd["bytes"],pd["sha256"]),"actual whole selected primary")
  payload=gzip.decompress(path.read_bytes());need(digest(payload)==pd["payloadSHA256"],"whole primary payload")
  pobj=json.loads(payload);need(pobj["binding"]==PROFILE_BINDING and pobj["phase"]=="primary-"+a.factor,"same original primary source coordinates")
  pdata=pobj["data"];ps=pdata["summary"]
  need(ps["label"]==a.factor and ps["allPrimaryDirectionsRetained"] and ps["allOriginalPrimaryActionProductsVerified"],"all primary coordinates and parameter action")
  h=list(map(int,fs["factorCoefficients"]));d=int(fs["extensionDegree"]);order=int(fs["jetOrder"]);columns=int(fs["detectorCount"]);n=int(fs["primaryDimension"]);L=d*order;T=L*columns
  need(h==ps["coefficients"] and d==ps["degree"] and order==ps["maximumExponent"] and n==ps["primaryDimension"] and len(h)==d+1 and h[-1]==1,"same original complete primary and actual maximum exponent")
  need(2<=d<=4 and 1<=order<=5 and 1<=columns<=8,"actual bounded extension geometry")
  original=[helper.from_data(v,nmod_mat) for v in final["original1034ComponentJetCoefficients"]]
  restrictions=[helper.from_data(v,nmod_mat) for v in final["completePrimaryRestrictions"]]
  need(len(restrictions)==columns and all(A.nrows()==L and A.ncols()==n for A in restrictions),"complete detector restrictions")
  R=nmod_mat(T,n,[int(v) for A in restrictions for v in A.entries()],P)
  J=helper.from_data(pdata["primaryAction"],nmod_mat);Uprimary=helper.from_data(pdata["original299Basis"],nmod_mat)
  need(matrix_equal_record(Uprimary,helper.from_data(final["originalPrimaryBasis"],nmod_mat)),"identical original299 primary basis")
  theta=theta_matrix(h,order,nmod_mat)
  need(int(R.rank())==n and all(A*J==theta*A for A in restrictions),"all complete primary restrictions and theta products reverified")
  _,_,coeffaudit=scalar.original_coefficients(a.primitive,a.model_out/"original127-normal-form-input.txt")
  originalaudit={k:coeffaudit[k] for k in ("all4433PrimitiveToPaidModelCoefficientChecks","all6188OriginalSourceIdentitiesVerified","primitiveDecodedBytes","primitiveDecodedSHA256")}
  ident={"algorithm":"all-original-source-unramified-jet-carry-complete-primary-image-v1","prime":P,"coefficientModulus":MOD,
   "wrapperSHA256":sha(Path(__file__)),"nativeSHA256":NATIVE_PIN[1],"scalarNativeSHA256":SCALAR_CPP_PIN[1],
   "scalarReaderSHA256":SCALAR_PY_PIN[1],"matrixReaderSHA256":MATRIX_PY_PIN[1],
   "allOriginalInputPins":scalar.PAID,"primitiveDecoded":scalar.RAW_PRIMITIVE,
   "parentBinding":PARENT_BINDING,"parentReceiptBytes":a.detector_receipt_bytes,"parentReceiptSHA256":a.detector_receipt_sha256,
   "immutableDetectorPhase":selected_desc,"immutableCommonPhase":common_desc,"originalPrimaryPhase":pd,
   "factorLabel":a.factor,"factorCoefficients":h,"extensionDegree":d,"jetOrder":order,"detectorCount":columns}
  binding=digest(canonical(ident));r["binding"]=binding
  r["parameters"].update({"identity":ident,"seconds":a.seconds,"memoryMiB":a.memory_mib,"through":a.through,
   "factorCoefficients":h,"extensionDegree":d,"jetOrder":order,"detectorCount":columns,"primaryDimension":n,
   "parentManifestMayAppendOtherFactors":True,"selectedParentDescriptorsVerified":True,
   "allOriginalCoefficientChecks":originalaudit,"allOriginalRestrictionProductsReverified":True})
  if mp.exists():
   manifest=json.loads(mp.read_text());need(manifest["format"]==FORMAT+"-manifest" and manifest["binding"]==binding and canonical(manifest["identity"])==canonical(ident),"same exact generalized consumer continuation")
  else:
   need(not any(a.out.glob("*.json.gz")) and not (a.out/"scan"/"generalized-active.bin").exists(),"no unbound generalized arrays")
   manifest={"format":FORMAT+"-manifest","binding":binding,"identity":ident,"phases":{}};atomic(mp,manifest)
  save();beat()
  config=a.out/"original-complete-generalized-detectors.bin";integer=a.out/"original-primitive-integer-polynomials-mod16129.bin"
  data=cached("original-generalized-inputs")
  if data is None:
   cfg=encode_config(binding,scalar.NFB,scalar.GBB,h,order,columns,original);binary(config,cfg)
   enc,ea=encode_primitive(a.primitive,scalar,binding);binary(integer,enc)
   data=put("original-generalized-inputs",{"originalCoefficientAudit":originalaudit,"integerPolynomialAudit":ea,
    "completePrimaryRestrictions":helper.mat_data(R),"originalPrimaryAction":helper.mat_data(J),
    "allOriginalPrimaryRestrictionProductsVerified":True,"completePrimaryRestrictionRank":n},[config,integer])
  executable=a.out/"original127-generalized-source-bockstein-native"
  build=cached("native-build")
  if build is None:
   beat();compiler=subprocess.run(["g++","--version"],capture_output=True,text=True,check=True,timeout=10).stdout.splitlines()[0]
   cs=time.monotonic();cp=subprocess.run(["g++","-std=c++17","-O3","-DNDEBUG",str(a.sources_root/NATIVE),"-o",str(executable)],
    capture_output=True,text=True,timeout=a.compile_seconds)
   r["parameters"]["compileSeconds"]=time.monotonic()-cs
   need(cp.returncode==0,"complete generalized native compilation: "+cp.stderr[-3000:])
   build=put("native-build",{"compiler":compiler,"flags":["-std=c++17","-O3","-DNDEBUG"],"compileSeconds":r["parameters"]["compileSeconds"]},[executable])
   r["parameters"]["compileReused"]=False
  else:r["parameters"]["compileReused"]=True
  r["parameters"]["compiler"]=build["compiler"];save()

  ell_file=a.out/"original4367-generalized-functional.bin"
  transport=cached("whole-original-functional-transport")
  if transport is None:
   native=run_native("transport",[a.normal_forms_out/"nf-prebasis.bin",a.normal_forms_out/"nf-component-dictionary.bin",ell_file],Path(str(ell_file)+".json"))
   need(native["all4367OriginalOutputsRetained"] and native["originalPrebasisJetProducts"]==3333*T,"complete original transport audit")
   transport=put("whole-original-functional-transport",native,[ell_file,Path(str(ell_file)+".json")])
  read_original_ell(ell_file,binding,h,order,columns,scalar)
  r["parameters"]["original4367TransportComplete"]=True;r["parameters"]["originalPrebasisJetProducts"]=transport["originalPrebasisJetProducts"];save()
  leaves=a.out/"all6188-original-generalized-divided-leaves.bin"
  data=cached("whole-original-integer-source-leaves")
  if data is None:
   native=run_native("leaves",[integer,ell_file,leaves],Path(str(leaves)+".json"))
   need(native["all6188OriginalScalarColumnsDivisible"] and native["originalDivisibleCoefficientCount"]==6188*T,"all original integer generalized leaf equations")
   data=put("whole-original-integer-source-leaves",native,[leaves,Path(str(leaves)+".json")])
  r["parameters"]["allOriginal6188IntegerScalarProductsDivisible"]=True
  r["parameters"]["originalScalarProductCoordinates"]=data["originalDivisibleCoefficientCount"];save()
  nf_values=a.out/"all2855-original-generalized-normal-values.bin"
  data=cached("whole-original-NF-source-values")
  if data is None:
   native=run_native("nf",[leaves,a.normal_forms_out/"nf-forward.bin",a.normal_forms_out/"nf-backward.bin",a.normal_forms_out/"nf-reduction.bin",nf_values],Path(str(nf_values)+".json"))
   need(native["forwardOperations"]==801468 and native["backwardOperations"]==1041956 and native["normalOperations"]==29606398 and native["all6188OriginalSourcesExactlyOnce"],"whole original NF source recipe coverage")
   data=put("whole-original-NF-source-values",native,[nf_values,Path(str(nf_values)+".json")])
  r["parameters"]["originalNFSourceCoverage"]={k:data[k] for k in ("forwardOperations","backwardOperations","normalOperations","all6188OriginalSourcesExactlyOnce")};save()
  scandir=a.out/"scan";scandir.mkdir(exist_ok=True)
  zfile=scandir/"all-original-Z-generalized-values.bin";scanreceipt=scandir/"generalized-scan-native.json"
  scan=cached("whole-original1834-global-Z-values")
  if scan is None:
   inspect_scan()
   native=run_native("scan",[nf_values,a.gb_out/"gb-operations.bin",scandir],scanreceipt)
   need(native["GBReductions"]==69407428 and native["GBSwaps"]==11591 and native["processedOriginalSources"]==2855 and native["originalGlobalZeroSources"]==1834 and native["all1834OriginalPolynomialZeroSourcesCovered"] and native["noPointKernelSubstituted"],"complete original global polynomial source scan")
   cp=manifest["nativeCheckpoint"]
   scan=put("whole-original1834-global-Z-values",native,[zfile,scanreceipt,a.out/cp["selector"]["file"],a.out/cp["activeState"]["file"]])
  r["parameters"]["completeOriginalZScan"]={k:scan[k] for k in ("processedOriginalSources","GBReductions","GBSwaps","originalGlobalZeroSources","nonzeroZeroEndpointsNotDimension","integerDividedCoefficientRecurrences","allSourceRoutesVerified","all1834OriginalPolynomialZeroSourcesCovered","noPointKernelSubstituted")};save()
  labels,V=read_all_z(zfile,binding,h,order,columns,nmod_mat)
  image=cached("complete-first-coefficient-primary-image")
  if image is None:
   image=complete_image(V,R,J,helper,nmod_mat,nmod_poly,beat)
   b=image["summary"]["completeFirstCoefficientImageDimension"]
   hp=nmod_poly(h,P);cp=nmod_poly(image["summary"]["imageCharacteristic"]["coefficients"],P)
   need(b%d==0 and cp==hp**(b//d),"complete first image has only the selected original primary")
   image["summary"]["selectedPrimaryCharacteristicVerified"]=True
   image["selectedOriginalGlobalSourceLabels"]=[dict(labels[j],zeroIndex=j) for j in image["selectedOriginalZeroIndices"]]
   image=put("complete-first-coefficient-primary-image",image)
  r["parameters"]["completeFirstCoefficientImage"]=image["summary"]
  r["parameters"]["selectedOriginalGlobalSourceLabels"]=image["selectedOriginalGlobalSourceLabels"];save()
  selected=image["selectedOriginalZeroIndices"];dimension=image["summary"]["completeFirstCoefficientImageDimension"]
  # These verification phases are independent complete positive source certificates.
  verified=[]
  if a.through=="final":
   for zi in selected:
    beat();base="positive-original-Z-"+str(zi)
    source=a.out/(base+"-source.bin");product=a.out/(base+"-full-products.bin")
    source_data=cached(base+"-reversal")
    if source_data is None:
     native=run_native("reverse",[a.normal_forms_out/"nf-forward.bin",a.normal_forms_out/"nf-backward.bin",
      a.normal_forms_out/"nf-reduction.bin",a.gb_out/"gb-operations.bin",scandir,str(zi),source],Path(str(source)+".json"))
     need(native["zeroIndex"]==zi and native["originalGlobalZeroNode"]==labels[zi]["globalNode"] and native["originalInputOrdinal"]==labels[zi]["ordinal"] and native["originalRawSource"]==labels[zi]["originalRawSource"],"same selected complete original global source")
     source_data=put(base+"-reversal",native,[source,Path(str(source)+".json")])
    product_data=cached(base+"-full-original-products")
    if product_data is None:
     native=run_native("products",[integer,ell_file,source,leaves,product],Path(str(product)+".json"))
     need(native["zeroIndex"]==zi and native["originalGlobalZeroNode"]==labels[zi]["globalNode"] and native["all4367IntegerProductsDivisible"] and native["originalIntegerProductCoordinates"]==4367*L and native["allDetectorPairingsVerified"] and native["all6188IndependentSourceContractionsVerified"] and native["positiveOriginalGlobalPolynomialSource"],"all original positive product gates")
     product_data=put(base+"-full-original-products",native,[product,Path(str(product)+".json")])
    verified.append({"zeroIndex":zi,"globalNode":labels[zi]["globalNode"],"ordinal":labels[zi]["ordinal"],
     "originalRawSource":labels[zi]["originalRawSource"],"sourceSupport":source_data["sourceSupport"],
     "allOriginal4367ProductsVerified":True,"originalIntegerProductCoordinates":product_data["originalIntegerProductCoordinates"],
     "all6188IndependentSourceContractionsVerified":True})
    r["parameters"]["verifiedPositiveOriginalGenerators"]=verified;save()
  r["parameters"]["all1834OriginalZeroSourcesCovered"]=True
  r["parameters"]["firstCoefficientImageComputed"]=True
  r["parameters"]["higherCoefficientTorsionExcluded"]=False
  r["parameters"]["completeFirstImageDimension"]=dimension
  r["parameters"]["verifiedPositiveSourceCount"]=len(verified)
  r["parameters"]["allSelectedPositiveGeneratorsOriginal4367Verified"]=len(verified)==len(selected)
  r["parameters"]["verifiedPositiveOriginalGenerators"]=verified
  r["parameters"]["allFirstCoefficientImageDirectionsHaveOriginalVerifiedGenerators"]=len(verified)==len(selected)
  if dimension==0:
   need(not selected and zero(V),"complete zero first coefficient image actually read from every original source")
   r["status"]="completed";r["outcome"]="complete-first-coefficient-image-zero-on-selected-primary";rc=0
  elif len(verified)==len(selected):
   r["status"]="completed";r["outcome"]="complete-first-coefficient-primary-image-and-original-positive-generators";rc=0
  else:
   r["status"]="completed-prefix";r["outcome"]="complete-source-scan-and-image-positive-original-products-pending";rc=75
 except Budget as e:
  r["status"]="budget-checkpoint";r["outcome"]="whole-generalized-phases-and-source-prefix-retained"
  r["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};rc=75
 except BaseException as e:
  r["status"]="failed";r["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};rc=1
 finally:
  if manifest is not None:
   r["parameters"]["completedTemporaryPhases"]=manifest["phases"]
   if mp.exists():r["parameters"]["temporaryManifest"]=rec(mp)
  save()
 print(json.dumps({"status":r["status"],"outcome":r.get("outcome"),"elapsedSeconds":r["elapsedSeconds"],
  "completeFirstImageDimension":r["parameters"].get("completeFirstImageDimension"),
  "verifiedPositiveSourceCount":r["parameters"].get("verifiedPositiveSourceCount"),"error":r["parameters"].get("error")}),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
