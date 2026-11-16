#!/usr/bin/env python3
"""Resolve the entire possible root-one socle of the original joint M.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
Only paid true16 residue classes are inherited; center-one G/V is freshly rebuilt.
All original 6188 source and4367 output rows and complete315 checks remain.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
P=31
MOD=787662783788549761
BASE_NAME="2026-11-16-r150-joint-m-true16-source-rebuild-p9-bounded50-789f.py"
BASE_SHA="07cd9a2c6d09c9efc11be8aba50cbdd5bceba6f058f1fab986f6a1017a150d87"
BASE_BYTES=38621
INTEGER_NAME="2026-11-16-r150-joint-m-root-one-original-target-integer-p12-789f.cpp"
MODEL_NAME="2026-11-16-r150-joint-m-original-model-p12-789f.py"
UNIT_NAME="2026-11-16-r150-joint-m-root-one-local-unit-solve-789f.py"
FORMAT="r150-original-joint-m-root-one-complete-two-digits-v1"
EXP16=[1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6]
LABEL9=list(range(2,11))
QUALIFICATION_BYTES=20106
QUALIFICATION_SHA="9b8c104b8cbd9d7fbe17c7e6fbddd1067c66d6a6a17252ed9c8f854b7cd2a2a7"
QUAL_DATA_BYTES=2112889
QUAL_DATA_SHA="a7a21b4c00e306ee0278451217491aedf88c6bcb59c3ca23668198516a74a29d"
QUAL_BINDING="f03f4892d70cdf39aceaebf8d8e9dc979196904e8ca75afbfc3d080230cb365f"
DIGIT_PRECISIONS=[10,5]
NATIVE={"vq":"2026-11-16-r150-joint-m-root-one-vq-789f.cpp",
 "normal":"2026-11-16-r150-joint-m-root-one-normal-789f.cpp",
 "transport":"2026-11-16-r150-joint-m-root-one-original-transport-789f.cpp",
 "integer":INTEGER_NAME}
SOURCES={'2026-11-16-r150-joint-m-root-one-common-789f.hpp': '1861bdb101a05c3653b2d726306741650f73022fb18c54602629db10ac382c08', '2026-11-16-r150-joint-m-root-one-vq-789f.cpp': '51eeadba395105bf4c1f0e8b88185b80953dae8c109fb4139876218f1a0cda64', '2026-11-16-r150-joint-m-root-one-normal-789f.cpp': 'a619ed26d6edbb58665e7387889a6c1355b624a91f86c37b416ec662548ed6e2', '2026-11-16-r150-joint-m-root-one-original-transport-789f.cpp': 'b048caa8b699ddff2c20aa60e54ee50b718cefcd06e627fbb9adc9a4e627f99a', '2026-11-16-r150-joint-m-root-one-local-unit-solve-789f.py': '871c673f68ddb17a6ab53dcd2612c94b4743bcccc6e0006efaa23ce5f769f0ae', '2026-11-16-r150-joint-m-root-one-original-target-integer-p12-789f.cpp': 'a7eb77bcf4d267015c8430d60b2bdd02e1682514a4452a0517a7a4f45a6ffb17', '2026-11-14-r150-f31-bitplane-789f.hpp': '73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec', '2026-11-14-r150-ninth-first-common-789f.hpp': '591dedf2c8a1d9d67fc644d21fae6e56ffc7ef8c840560831422197cbc5e9531', '2026-11-16-r150-joint-m-bounded50-unit-schur-789f.py': '71295507dddb64dc7f60172910158d0d9043721597e397df0fb264dfd51fdcd9', '2026-11-14-r150-ninth-first-matrices-789f.py': '3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a', '2026-11-14-r150-torsion-characteristic-789f.py': '8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2', '2026-11-16-r150-joint-m-original-model-p12-789f.py': '6310cf2217dbe7770b117bb37c2d7d84a0cc6f77a9e0dffcbdb0ae036ed2362c'}
class BudgetStop(Exception):pass
class StageFailure(Exception):pass
def check(ok,message):
 if not ok:raise ValueError(message)
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)+"\n").encode("ascii")
def digest(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for chunk in iter(lambda:f.read(1048576),b""):h.update(chunk)
 return {"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def atomic(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
def atomic_json(p,x):atomic(p,canonical(x))
def module(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def pinned(p,size,sha,label):
 z=identity(p);check(z=={"bytes":size,"sha256":sha},"exact "+label);return z
def rows(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def field_record(A):
 rr=rows(A);return {"rows":A.nrows(),"columns":A.ncols(),"sha256":digest(bytes(x for row in rr for x in row))}
def integer_record(A):
 return {"rows":len(A),"columns":len(A[0]) if A else 0,"sha256":digest(canonical(A))}
def mm(A,B,mod):
 n=len(A);r=len(B);m=len(B[0]) if B else 0
 check(all(len(row)==r for row in A) and all(len(row)==m for row in B),"small matrix product dimensions")
 return [[sum(A[i][k]*B[k][j] for k in range(r))%mod for j in range(m)] for i in range(n)]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def valuation(a,cap):
 if not a:return cap
 v=0
 while a%31==0:a//=31;v+=1
 return v
def smith_mod(A,precision):
 """Full invertible row/column operations over Z/(31^precision), with product gate."""
 m=len(A);n=len(A[0]) if A else 0;mod=31**precision
 check(all(len(row)==n for row in A),"rectangular small DVR matrix")
 original=[[int(x)%mod for x in row] for row in A]
 C=[row[:] for row in original];U=eye(m);V=eye(n);piv=[]
 for k in range(min(m,n)):
  choices=[(valuation(C[i][j],precision),i,j) for i in range(k,m) for j in range(k,n) if C[i][j]]
  if not choices:break
  v,i,j=min(choices)
  C[k],C[i]=C[i],C[k];U[k],U[i]=U[i],U[k]
  for W in (C,V):
   for row in W:row[k],row[j]=row[j],row[k]
  a=31**v;unit=(C[k][k]//a)%mod;inv=pow(unit,-1,mod)
  C[k]=[z*inv%mod for z in C[k]];U[k]=[z*inv%mod for z in U[k]]
  check(C[k][k]==a,"exact DVR pivot normalization")
  for i in range(k+1,m):
   check(C[i][k]%a==0,"minimum-valuation row division")
   q=C[i][k]//a
   if q:
    C[i]=[(z-q*t)%mod for z,t in zip(C[i],C[k])]
    U[i]=[(z-q*t)%mod for z,t in zip(U[i],U[k])]
  for j in range(k+1,n):
   check(C[k][j]%a==0,"minimum-valuation column division")
   q=C[k][j]//a
   if q:
    for W in (C,V):
     for row in W:row[j]=(row[j]-q*row[k])%mod
  check(all(C[i][k]==0 for i in range(m) if i!=k) and all(C[k][j]==0 for j in range(n) if j!=k),
        "complete original small pivot row and column")
  piv.append(v)
 check(mm(mm(U,original,mod),V,mod)==C,"all original small DVR transformation products")
 check(all(C[i][j]==(31**piv[i] if i==j and i<len(piv) else 0) for i in range(m) for j in range(n)),
       "full small Smith diagonal, including all residual rows")
 from flint import nmod_mat
 check(nmod_mat([[z%31 for z in row] for row in U],31).rank()==m,"left transformation is a true D unit")
 check(n==0 or nmod_mat([[z%31 for z in row] for row in V],31).rank()==n,"right transformation is a true D unit")
 return {"valuations":piv,"diagonal":C,"left":U,"right":V,"precision":precision,
         "allOriginalProductsVerified":True,"bothTransformationsDUnits":True}
def joined(*matrices):
 if not matrices:return []
 n=len(matrices[0]);check(all(len(A)==n for A in matrices),"small horizontal block rows")
 return [[x for A in matrices for x in A[i]] for i in range(n)]
def scaled(A,c,exponents):
 return [[c*x%(31**exponents[i]) for x in row] for i,row in enumerate(A)]
def group_image(A,exponents):
 check(len(A)==len(exponents),"actual ambient torsion coordinate dimension")
 precision=max(exponents)
 Z=[[31**(precision-e)*int(x)%(31**precision) for x in row] for e,row in zip(exponents,A)]
 S=smith_mod(Z,precision)
 invariant=sorted(precision-v for v in S["valuations"])
 return {"exponents":invariant,"length":sum(invariant),"minimumDGenerators":len(invariant),
  "coordinates":integer_record(A),"uniformEmbedding":integer_record(Z),"smithValuations":S["valuations"],
  "allOriginalSmallProductsVerified":True,"bothTransformationsDUnits":True}

def trim_integer(poly):
 p=[int(x)%MOD for x in poly]
 while p and not p[-1]:p.pop()
 return p
def family(path,labels,edges):
 return {"file":path,"labels":list(labels),"edges":[[i,j,trim_integer(p)] for i,j,p in edges if trim_integer(p)]}
def write_mix(path,labels,L,exponents,families):
 active=[f for f in families if f["edges"]]
 lines=["R150_JOINT_M_INTEGER_MIX_P12_V1 %d %d %d"%(len(labels),L,len(active))," ".join(map(str,exponents))]
 semantic=[];inputs=[]
 for f in active:
  check(not any(c.isspace() for c in str(f["file"])),"actual source path without whitespace")
  lines.append("%s %d %d"%(f["file"],len(f["labels"]),len(f["edges"])))
  lines.append(" ".join(map(str,f["labels"])))
  for i,j,p in f["edges"]:lines.append("%d %d %d %s"%(i,j,len(p)," ".join(map(str,p))))
  semantic.append({"input":identity(f["file"]),"labels":f["labels"],"edges":f["edges"]});inputs.append(f["file"])
 atomic(path,("\n".join(lines)+"\n").encode("ascii"))
 return semantic,inputs
def reduce_rows(A,exponents):return [[int(x)%(31**e) for x in row] for e,row in zip(exponents,A)]
def add(A,B,mod):return [[(x+y)%mod for x,y in zip(a,b)] for a,b in zip(A,B)]
def matrix_poly(poly,X,mod):
 n=len(X);out=[[0]*n for _ in range(n)];I=eye(n)
 for c in reversed(poly):out=add(mm(X,out,mod),[[c*z%mod for z in row] for row in I],mod)
 return out
def null_image(A,exponents):return all(x==0 for row in reduce_rows(A,exponents) for x in row)

def main():
 ap=argparse.ArgumentParser()
 for name in ("notes-root","original-input-dir","exact-gzip","jet-map-dir","qualification-receipt","qualification-data","out"):
  ap.add_argument("--"+name,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=600)
 ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args()
 check(0<a.seconds<=1800 and 1024<=a.memory_mib<=4096,"bounded independent root-one resource contract")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();deadline=start+a.seconds
 rec={"format":FORMAT,"status":"running","parameters":{"prime":31,"integerModulus":MOD,
  "TaylorCenter":1,"originalSourceRows":6188,"originalOutputRows":4367,
  "rootTwoCacheRelabelled":False,"full210Recomputed":False,"digitPrecisions":DIGIT_PRECISIONS,
  "largeArraysTemporaryOnly":True,"stages":{},"classes":{},"coordinateChecks":{}}}
 rp=a.out/"original-joint-m-root-one-complete-two-digits-receipt.json"
 def save():
  rec["elapsedSeconds"]=time.monotonic()-start;atomic_json(rp,rec)
 def tick():
  if time.monotonic()>=deadline-2:raise BudgetStop("joint-M root-one shared budget")
 def stop(signum,frame):raise BudgetStop("joint-M root-one signal "+str(signum))
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 logs=a.out/"logs";logs.mkdir(exist_ok=True);cache=a.out/"stage-cache";cache.mkdir(exist_ok=True)
 try:
  bp=a.notes_root/BASE_NAME;pinned(bp,BASE_BYTES,BASE_SHA,"paid original input dictionaries")
  b=module(bp,"r150_joint_m_root1_original_dictionary")
  sources={BASE_NAME:identity(bp)}
  for name,sha in SOURCES.items():
   z=identity(a.notes_root/name);check(z["sha256"]==sha,"frozen root-one helper "+name);sources[name]=z
  files={};inputs={}
  for key,d in b.ORIGINAL.items():
   files[key]=a.original_input_dir/d["name"];inputs[key]=pinned(files[key],d["bytes"],d["sha256"],key)
  inputs["exactPrimitive"]=pinned(a.exact_gzip,*b.EXACT_PIN,"original exact primitive")
  mp=a.jet_map_dir/"jet-quotient-map.bin";mrp=a.jet_map_dir/"jet-quotient-map-receipt.json"
  inputs["jetMap"]=pinned(mp,*b.MAP_PIN,"complete two-center local quotient map")
  inputs["jetMapReceipt"]=pinned(mrp,*b.MAP_RECEIPT_PIN,"complete two-center local quotient map receipt")
  inputs["qualification"]=pinned(a.qualification_receipt,QUALIFICATION_BYTES,QUALIFICATION_SHA,"complete original M qualification")
  inputs["qualificationData"]=pinned(a.qualification_data,QUAL_DATA_BYTES,QUAL_DATA_SHA,"complete original M mathematical data")
  qualification=json.loads(a.qualification_receipt.read_bytes());qd=json.loads(a.qualification_data.read_bytes())
  check(qualification["status"]=="completed" and qualification["binding"]==qd["binding"]==QUAL_BINDING and qualification["parameters"]["final"]["completePrimitiveFreeLatticeQualified"],"same actually qualified integral primitive free lattice")
  semantic={"format":FORMAT,"driver":identity(Path(__file__)),"sources":sources,"inputs":inputs,
   "TaylorCenter":1,"digitPrecisions":DIGIT_PRECISIONS,"originalTargetLabels":LABEL9,
   "coefficientModulus":MOD,"noRootTwoFieldOrIntegerCacheUsed":True}
  binding=digest(canonical(semantic));rec["binding"]=binding;rec["parameters"]["inputIdentity"]=semantic
  binding_file=a.out/"binding.json"
  if binding_file.exists():check(json.loads(binding_file.read_text())=={"binding":binding,"semantic":semantic},"same exact root-one continuation")
  else:atomic_json(binding_file,{"binding":binding,"semantic":semantic})
  from flint import nmod_mat
  h=module(a.notes_root/"2026-11-14-r150-ninth-first-matrices-789f.py","r150_joint_m_root1_matrix_helper")
  state_reader=module(a.notes_root/"2026-11-14-r150-torsion-characteristic-789f.py","r150_joint_m_root1_original_state")
  state=state_reader.load_state(files["state"]);J=nmod_mat(state["matrices"]["action"],31)
  K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose();O=nmod_mat(state["observabilityEchelon"],31);Astate=nmod_mat(state["matrices"]["A"],31)
  check((state["stateDimension"],state["torsionDimension"],state["observabilityRank"])==(820,315,505),"all original quotient dimensions")
  U16=nmod_mat(qd["true16"],31);J16=nmod_mat(qd["true16Action"],31)
  check(U16.rank()==16 and field_record(U16)["sha256"]==b.OLD_U16_SHA and field_record(J16)["sha256"]==b.OLD_J16_SHA and J*U16==U16*J16,"complete paid true16 original classes and action")
  root1=[d for d in qd["summary"]["primary"] if d.get("center")==1]
  check(len(root1)==1 and root1[0]["primitiveFreeLineQualified"] and root1[0]["primitiveTargetLabel"]==2 and root1[0]["torsionIntersectionResidueDimension"]==0,"actual root-one primitive line and zero initial torsion intersection")
  I=nmod_mat(eye(315),31);PM=h.action(root1[0]["fullOriginalCRTProjector"],J,I)
  check(PM*PM==PM and PM*J==J*PM and PM.rank()==7,"same complete original root-one primary projector")
  xp=h.mul(h.mul([30,1],[30,1]),[30,1]);check(h.zero(h.action(xp,J,PM)),"the entire original root-one parameter torsion is detected by three Taylor terms")
  Broot=h.sub(PM,range(315),h.pivots(PM));PU=PM*U16;chosen=[];rank=0
  for group,need in ((range(2),1),(range(2,7),2)):
   for j in group:
    candidate=chosen+[j];r=h.sub(PU,range(315),candidate).rank()
    if r>rank:chosen.append(j);rank=r
   check(rank==need,"root-one complete coefficient basis at each exact p exponent")
  E=[EXP16[j] for j in chosen];U=h.sub(PU,range(315),chosen)
  check(E==[1,2] and PU.rank()==2 and h.zero(h.solve_span(U,PU)["residual"]) and h.zero(h.solve_span(U,J*U)["residual"]),"all sixteen true sources project into the complete root-one p,p2 basis")
  Xi=nmod_mat(state["matrices"]["targetCoordinates"],31).transpose();Targets=nmod_mat(state["matrices"]["targets"],31).transpose()
  check(K*Xi==Targets and Astate*K==K*J and h.zero(O*Targets),"all original nine targets, action and505 observations")
  f=PM*h.sub(Xi,range(315),[0]);basis3=h.join(U,f);Wfield=PM*h.sub(Xi,range(315),range(1,9))
  check(basis3.rank()==3 and f.rank()==1 and h.zero(h.solve_span(f,PM*Xi)["residual"]),"all nine root-one target residues lie on the actual primitive original t2 line")
  check(h.zero((J-I)*f),"root-one field free generator has parameter eigenvalue one")
  mapraw=mp.read_bytes();maprec=json.loads(mrp.read_text());maps={k:h.block(mapraw,maprec,k) for k in maprec["matrices"]}
  check((maps["globalTorsionTo39"]*Broot).rank()==7,"complete root-one primary injects into the paid39-dimensional local quotient")
  rec["parameters"]["actualRootOneBasis"]={"originalTrue16Indices":chosen,"exponents":E,"length":3,"matrix":field_record(U),"wholeOriginalPrimaryDimension":7,"all315ProjectionChecks":True}
  rec["parameters"]["primitiveRootOneLine"]={"originalTargetLabel":2,"matrix":field_record(f),"allNineResiduesInThePrimitiveLine":True,"fullCoefficientTorsionNotSilentlyDiscarded":True}
  model=module(a.notes_root/MODEL_NAME,"r150_root1_exact_p12_model");model_file=a.out/"original-equations-mod31twelve.txt"
  rec["parameters"]["originalP12Model"]=model.generate(a.exact_gzip,files["integerModel"],model_file);save()
  binaries=a.out/"bin";binaries.mkdir(exist_ok=True);programs={}
  native=NATIVE
  for key,name in native.items():
   tick();exe=binaries/key;meta=binaries/(key+".json")
   ck=digest(canonical({"source":sources[name],"headers":{k:v for k,v in sources.items() if k.endswith(".hpp")},"flags":["g++","-O3","-std=c++17"]}))
   if not (exe.exists() and meta.exists() and json.loads(meta.read_text())=={"binding":ck,"executable":identity(exe)}):
    with (logs/("compile-"+key+".log")).open("wb") as log:
     q=subprocess.run(["g++","-O3","-std=c++17","-I",str(a.notes_root),str(a.notes_root/name),"-o",str(exe)],
       stdout=log,stderr=subprocess.STDOUT,timeout=min(60,max(1,deadline-time.monotonic()-2)))
    check(q.returncode==0,"native compilation "+key);atomic_json(meta,{"binding":ck,"executable":identity(exe)})
   programs[key]=[str(exe)]
  programs["solve"]=[sys.executable,str(a.notes_root/(UNIT_NAME))]
  def prefix(name):
   d=a.out/"stages"/name;d.mkdir(parents=True,exist_ok=True);return d/name
  def run(name,program,args,marker,gates,stage_inputs,outputs,logic):
   tick();source=native[program] if program in native else UNIT_NAME
   key=digest(canonical({"pipeline":binding,"source":sources[source],"inputs":[identity(p) for p in stage_inputs],"logic":logic}))
   cp=cache/(name+".json");context=cache/(name+".context.json")
   if context.exists():check(json.loads(context.read_text())=={"inputBinding":key},"same partial original stage "+name)
   else:atomic_json(context,{"inputBinding":key})
   if cp.exists():
    old=json.loads(cp.read_text());check(old["inputBinding"]==key,"same completed original stage "+name)
    check(all(p.is_file() and identity(p)==old["outputs"].get(str(p.relative_to(a.out))) for p in outputs),"unchanged completed original stage outputs "+name)
    rec["parameters"]["stages"][name]={"status":"completed","reused":True,"inputBinding":key,"statistics":old["statistics"]};save();return
   remain=deadline-time.monotonic()-1
   if remain<3:raise BudgetStop("before "+name)
   argv=[str(max(.1,remain-1)) if str(x)=="__REMAINING__" else str(x) for x in args]
   command=["timeout","--kill-after=10s",str(remain)+"s","prlimit","--as="+str(a.memory_mib*1048576),"--core=0","--"]+programs[program]+argv
   stage={"status":"running","inputBinding":key};rec["parameters"]["stages"][name]=stage;save()
   began=time.monotonic();last={};logpath=logs/(name+".log")
   with logpath.open("w") as log:
    proc=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
    for line in proc.stdout:
     log.write(line);log.flush()
     try:event=json.loads(line)
     except ValueError:continue
     if isinstance(event,dict):
      last=event
      if event.get("status") or "completedOriginalRows" in event:
       print(json.dumps({"stage":name,**event},separators=(",",":")),flush=True)
    code=proc.wait()
   full_statistics=dict(last)
   keep={"status","mode","targets","targetCount","targetScalarPower","computedTaylorPrecision","retainedFormalPrecision",
    "TaylorPrecision","GCachePrecision","allOriginal17CoefficientsDivisible","sameOriginalUnmultipliedNineSquaresVerified",
    "residualIsTargetMinusOriginalAProduct","fullOriginalGIdentityVerified","all13FreeConditionsRetained","elapsedSeconds"}
   summary={k:v for k,v in last.items() if k in keep}
   stage.update(exitCode=code,elapsedSeconds=time.monotonic()-began,statistics=summary,log=identity(logpath))
   if code in (75,124,-15):
    stage["status"]="budget-checkpoint";save();raise BudgetStop(name)
   if not (code==0 and last.get("status")==marker and all(last.get(k)==v for k,v in gates.items()) and all(p.is_file() for p in outputs)):
    stage["status"]="failed";stage["logTail"]=logpath.read_text(errors="replace")[-6000:];save();raise StageFailure(name)
   stage["status"]="completed"
   atomic_json(cp,{"inputBinding":key,"statistics":summary,"fullStatistics":full_statistics,
    "outputs":{str(p.relative_to(a.out)):identity(p) for p in outputs}});save()
  specs=a.out/"specs";specs.mkdir(exist_ok=True)
  def spec(name,labels,L,ring=1):
   p=specs/(name+".spec");b.write_spec(p,labels,L,ring);return p
  def target(name,labels,weights):
   """Exact original ordinary squares with constant, x or x^2 multipliers."""
   check(len(weights)==9 and all(len(row)==len(labels) for row in weights),"all nine original target-combination rows")
   edges=[]
   for i,row in enumerate(weights):
    for j,p in enumerate(row):
     q=trim_integer(p);check(len(q)<=3,"original Taylor target multiplier degree at most two")
     if q:edges.append((i,j,q))
   lines=["R150_JOINT_M_ORIGINAL_NINE_TARGETS_P12_V1 31 %d 1 9 %d %d"%(MOD,len(labels),len(edges)),
     "1"," ".join(map(str,LABEL9))," ".join(map(str,labels))]
   lines += ["%d %d %d %s"%(i,j,len(q)," ".join(map(str,q))) for i,j,q in edges]
   p=specs/(name+".targets");atomic(p,("\n".join(lines)+"\n").encode("ascii"));return p
  def mix(path,labels,L,power,families):return write_mix(path,labels,L,[power]*len(labels),families)
  def integer(name,labels,L,divisor,retained,target_power,target_file,families):
   p=prefix(name);s=spec(name,labels,L);mi=p.parent/(name+".mix")
   logic,inf=mix(mi,labels,L,divisor,families)
   run(name,"integer",[files["model"],model_file,s,mi,p,binding,retained,"__REMAINING__",target_file,target_power],
    "joint-m-raw-target-integer-p12-jets-complete",
    {"allOriginal17CoefficientsDivisible":True,"targetCount":len(labels),"computedTaylorPrecision":L,
     "retainedFormalPrecision":retained,"targetScalarPower":target_power,
     "sameOriginalUnmultipliedNineSquaresVerified":True,"residualIsTargetMinusOriginalAProduct":True},
    [files["model"],model_file,s,target_file]+inf,
    [b.suffix(p,k) for k in ("-original6188-integer-jets.bin","-divided-original-jets.bin",
     "-field-root1-jets.bin","-field-projected-crt8-jets.bin","-integer-product.json")],
    {"divisorExponent":divisor,"targetPower":target_power,"retained":retained,"families":logic})
   return p
  def normal(name,labels,L,field,crt=False):
   p=prefix(name);s=spec(name,labels,L,12 if crt else 1)
   run(name,"normal",[files["model"],field,files["graph"],s,p,binding],
    "saturated-runtime-two-ring-state-complete" if crt else "saturated-runtime-root1-normal-form-complete",{},
    [files["model"],field,files["graph"],s],
    [b.suffix(p,k) for k in ("-standard-state.bin" if crt else "-original1034-root1.bin",
      "-local-prebasis-source-jets.bin","-local-normal.json")],{"CRT8":crt})
   return p
  def complete_class(name,labels,integer_output):
   p=normal(name,labels,8,b.suffix(integer_output,"-field-projected-crt8-jets.bin"),True)
   raw=b.suffix(p,"-standard-state.bin").read_bytes();n=len(labels)
   check(raw[:8]==b"R150SE31" and struct.unpack_from("<4I",raw,8)==(31,820,n,8),"all820 original standard coordinates")
   check(list(struct.unpack_from("<%dH"%n,raw,24))==labels,"same target labels in original quotient")
   at=24+2*n;coordinates=[list(struct.unpack_from("<HB",raw,at+3*i)) for i in range(820)];at+=2460
   check(coordinates==maprec["standardCoordinates"] and len(raw)==at+820*n,"complete820 dictionary and EOF")
   V=nmod_mat(820,n,list(raw[at:]),31);Y=maps["Pi"]*V;F=maps["freeChecks"]*Y;D39=maps["torsionCoordinates"]*Y
   check(h.zero(F) and maps["torsionEmbedding"]*D39==Y,"all104 local free conditions and exact39 reconstruction")
   solved_root=h.solve_span(maps["globalTorsionTo39"]*Broot,D39)
   check(h.zero(solved_root["residual"]),"complete root-one local image in the original315 quotient")
   D=Broot*solved_root["solution"]
   check(maps["globalTorsionTo39"]*D==D39 and PM*D==D,"complete315 root1 primary class, not a global interpolation claim")
   original=K*D
   check(h.zero(O*original) and Astate*original==K*(J*D),"all505 original free conditions and same full parameter action")
   item={"matrix":field_record(D),"all104LocalFreeChecks":True,"all315OriginalCoordinateReconstruction":True,
    "all505GlobalFreeChecks":True,"sameOriginalSAction":True,"rootOnePrimaryProjectionExplicit":True}
   atomic_json(p.parent/"complete315-class.json",{"binding":binding,**item,"matrixRows":rows(D)})
   rec["parameters"]["classes"][name]=item;save();return D
  def coordinates(name,D):
   solved=h.solve_span(basis3,D)
   check(solved["indices"]==list(range(3)) and h.zero(solved["residual"]),"complete primitive line and true torsion span "+name)
   C=solved["solution"];check(basis3*C==D,"all315 primitive-line coordinate products "+name)
   rec["parameters"]["coordinateChecks"][name]={"basis":field_record(basis3),"targets":field_record(D),
    "coordinates":field_record(C),"all315ProductsVerified":True,"residueOnlyDoesNotReplaceHighPAction":True}
   atomic_json(a.out/(name+"-coordinates.json"),{"binding":binding,"coordinates":rows(C)})
   save();return h.sub(C,range(2),range(C.ncols())),h.sub(C,[2],range(C.ncols()))
  def solve_source(name,labels,L,integer_output):
   nf=normal(name+"-normal",labels,L,b.suffix(integer_output,"-field-root1-jets.bin"))
   d=a.out/"stages"/(name+"-complete");d.mkdir(parents=True,exist_ok=True)
   run(name+"-complete","solve",["--G",files["G"],"--rhs",b.suffix(nf,"-original1034-root1.bin"),
    "--binding",binding,"--notes-root",a.notes_root,"--out",d,"--remaining-seconds","__REMAINING__"],
    "saturated-local-unit-solve-complete",{"fullOriginalGIdentityVerified":True,"all13FreeConditionsRetained":True},
    [files["G"],b.suffix(nf,"-original1034-root1.bin")],[d/"complete-G-q-root1.bin",d/"local-unit-solve-receipt.json"],
    {"originalRows":1034,"maximumFormalSourcePrecisionLoss":5})
   s=spec(name,labels,L);v=prefix(name+"-vq");mode="q3"
   run(name+"-vq","vq",[files["model"],files["V"],d/"complete-G-q-root1.bin",files["oldK"],"-",v,binding,mode,s],
    "saturated-runtime-jet-VQ-complete",{"mode":mode},
    [files["model"],files["V"],d/"complete-G-q-root1.bin",files["oldK"],s],
    [b.suffix(v,"-original2195-source-jets.bin"),b.suffix(v,"-vq.json")],{"mode":mode})
   p=prefix(name+"-transport")
   run(name+"-transport","transport",[files["model"],files["oldK"],b.suffix(v,"-original2195-source-jets.bin"),files["normalTrace"],
    b.suffix(nf,"-local-prebasis-source-jets.bin"),files["forward"],files["backward"],p,binding,mode,"-",s,p.parent/"checkpoints","__REMAINING__"],
    "runtime-local-original-source-transport-complete",{"mode":mode},
    [files[k] for k in ("model","oldK","normalTrace","forward","backward")]+
     [b.suffix(v,"-original2195-source-jets.bin"),b.suffix(nf,"-local-prebasis-source-jets.bin"),s],
    [b.suffix(p,"-original6188-q-jets.bin"),b.suffix(p,"-transport.json")],{"mode":mode})
   return b.suffix(p,"-original6188-q-jets.bin")
  def source_of(p):return b.suffix(p,"-original6188-integer-jets.bin")
  # Rebuild the actual field G and V at center one from the complete paid
  # global source DAG. No root-two cache header is reused or relabelled.
  with files["oldK"].open("rb") as fh:head=fh.read(30)
  check(head[:8]==b"R150KK31", "original K200 identity for the one-column G/V bootstrap")
  bootstrap_label=struct.unpack_from("<H",head,28)[0]
  gv=prefix("fresh-root-one-GV10");gvspec=spec("fresh-root-one-GV10",[bootstrap_label],10)
  run("fresh-root-one-GV10","vq",[files["model"],files["graph"],files["oldQ"],files["oldK"],"-",gv,binding,"q1",gvspec],
   "saturated-runtime-jet-VQ-complete",{"mode":"q1"},[files[k] for k in ("model","graph","oldQ","oldK")]+[gvspec],
   [b.suffix(gv,z) for z in ("-actual-G-root1.bin","-actual-V-root1.bin","-original2195-source-jets.bin","-vq.json")],
   {"TaylorCenter":1,"TaylorPrecision":10,"originalGlobalDAGReevaluated":True})
  files["G"]=b.suffix(gv,"-actual-G-root1.bin");files["V"]=b.suffix(gv,"-actual-V-root1.bin")
  labels=list(range(42003,42011));weights=[[[] for _ in labels] for _ in range(9)]
  for j in range(1,9):weights[j][j-1]=[1]
  original_target=target("eight-original-root-one-targets",labels,weights)
  first=integer("root-one-initial-original-target",labels,10,2,10,2,original_target,[])
  D0=complete_class("root-one-initial-complete315",labels,first);d0,a0=coordinates("root-one-initial-coordinate",D0)
  check(D0==Wfield and h.zero(d0),"all original initial target residues have exactly zero true torsion coordinates")
  corrected_weights=[[v[:] for v in row] for row in weights]
  for j in range(8):corrected_weights[0][j]=[-int(a0[0,j])]
  corrected_target=target("root-one-free-corrected-targets",labels,corrected_weights)
  corrected=integer("root-one-subtract-primitive-free-class",labels,10,2,10,2,corrected_target,[])
  check(h.zero(complete_class("root-one-corrected-zero315",labels,corrected)),"all315 original field obstructions vanish after the true free correction")
  q=solve_source("root-one-q0",labels,10,corrected)
  carried=integer("root-one-next-true-integer-carry",labels,10,3,5,2,corrected_target,[family(q,labels,b.identity_edges(8,31**2))])
  D1=complete_class("root-one-next-complete315",labels,carried);d1,a1=coordinates("root-one-next-coordinate",D1)
  A=[[31*int(d1[i,j])%(31**e) for j in range(8)] for i,e in enumerate(E)]
  check(all(x==0 for x in A[0]) and all(x%31==0 for x in A[1]),"only the actual p-socle of the exponent-two direction may remain")
  free=[(int(a0[0,j])+31*int(a1[0,j]))%(31**2) for j in range(8)]
  image=group_image(A,E);check(image["exponents"] in ([],[1]),"complete root-one torsion is zero or one p-socle")
  data={"format":"r150-original-joint-m-root-one-complete-two-digit-coordinates-v1","binding":binding,
   "basisOriginalTrue16Indices":chosen,"ambientExponents":E,"originalTargetLabels":list(range(3,11)),
   "initialTorsionCoordinates":rows(d0),"secondTorsionCoordinates":rows(d1),"coordinateRows":A,
   "freeCoefficientsModuloP2":free,"primitiveFreeTargetLabel":2,"freeTailNotSetToZero":True,
   "sameCompleteRootOnePrimaryOnly":True,"parameterSActsAsOneOnTheFiniteSocle":True}
  datafile=a.out/"root-one-complete-two-digit-coordinates.json";atomic_json(datafile,data)
  rec["parameters"]["final"]={"completeRootOneCoefficientTorsion":image,
   "minimumRootOnePolynomialGeneratorsOfOriginalM":1+image["minimumDGenerators"],
   "allEightRawTargetDifferencesIncluded":True,"initialTorsionCoordinatesAllZero":True,
   "secondDigitUsesTheCompleteOriginal315Quotient":True,"primitiveFreeLineRetained":True,
   "twoDigitsCompleteBecauseP2T1Zero":True,"allOriginalIntegerProductsVerified":True,
   "actualCenterOneGAndVRebuiltFromOriginalDAG":True,"rootTwoCacheRelabelled":False,
   "all104And505FreeConditionsVerified":True,"all315ReconstructionChecksVerified":True,
   "higherFreeTailRetained":True,"complete210NotRecomputed":True,
   "temporaryCompleteDataFile":{"file":datafile.name,**identity(datafile)},"globalPolynomialSourceClaimed":False}
  rec["status"]="completed";save();return 0
 except (BudgetStop,subprocess.TimeoutExpired) as exc:
  rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)};save();return 75
 except BaseException as exc:
  rec["status"]="failed";rec["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)};save();return 1
 finally:
  save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
if __name__=="__main__":raise SystemExit(main())
