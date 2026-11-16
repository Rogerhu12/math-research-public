#!/usr/bin/env python3
"""Complete the joint original B over Z_(31), without recomputing full210.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
Only the original eight/seven/three/one source dependency closure is inherited.
All original 6188 source and4367 output rows and complete315 checks remain.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
P=31
MOD=26439622160671
BASE_NAME="2026-11-16-r150-joint-b-true16-source-rebuild-p9-789f.py"
BASE_SHA="e4b2b935882e899a55d7db10d590e5ce8d35f5fedcab6063a14008a5efe4b69e"
BASE_BYTES=38570
READER_NAME="2026-11-16-r150-joint-b-selected-parent-reader-p9-789f.py"
READER_SHA="a99c8308e47d940bcd06861bfedd81666e14ec1a28499c8116d267376a7af39a"
READER_BYTES=7435
INTEGER_NAME="2026-11-16-r150-joint-b-target-integer-p9-jets-789f.cpp"
INTEGER_SHA="1b35e729813e2ed162c3a7a314a798797073b5ff6269c5644492fa09742df93b"
INTEGER_BYTES=22969
FORMAT="r150-original-joint-b-complete-d-module-v1"
EXP16=[1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6]
LABEL9=list(range(2,11))
PAID_C1_SHA="4a2086fdfc64ffeb9171c3198cabb46ae04c2e013788711de44eb0f71ddab1e6"
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

def main():
 ap=argparse.ArgumentParser()
 for name in ("notes-root","parent-out","original-input-dir","small-input-dir","true-source-dir","exact-gzip","jet-map-dir","recipe","out"):
  ap.add_argument("--"+name,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=1800)
 ap.add_argument("--memory-mib",type=int,default=4096)
 ap.add_argument("--through",choices=("high","final"),default="final")
 a=ap.parse_args()
 check(0<a.seconds<=1800 and 1024<=a.memory_mib<=6144,"bounded same-job joint-B resource contract")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();deadline=start+a.seconds
 rec={"format":FORMAT,"status":"running","parameters":{"prime":31,"integerModulus":MOD,
  "originalSourceRows":6188,"originalOutputRows":4367,"full210Recomputed":False,
  "highDigitPrecisions":[15,10,5],"lowDigitPrecisions":[30,25,20,15,10,5],
  "largeArraysTemporaryOnly":True,"stages":{},"classes":{},"coordinateChecks":{}}}
 rp=a.out/"original-joint-b-complete-d-module-receipt.json"
 def save():
  rec["elapsedSeconds"]=time.monotonic()-start;atomic_json(rp,rec)
 def tick():
  if time.monotonic()>=deadline-2:raise BudgetStop("joint-B shared budget")
 def stop(signum,frame):raise BudgetStop("joint-B signal "+str(signum))
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 logs=a.out/"logs";logs.mkdir(exist_ok=True);cache=a.out/"stage-cache";cache.mkdir(exist_ok=True)
 try:
  bp=a.notes_root/BASE_NAME;pinned(bp,BASE_BYTES,BASE_SHA,"p9 true16 dependency reconstruction")
  b=module(bp,"r150_joint_b_selected_base")
  sources={BASE_NAME:identity(bp)}
  for name,sha in b.SOURCES.items():
   z=identity(a.notes_root/name);check(z["sha256"]==sha,"frozen mathematical helper "+name);sources[name]=z
  sources[READER_NAME]=pinned(a.notes_root/READER_NAME,READER_BYTES,READER_SHA,"p9 exact parent reader")
  sources[INTEGER_NAME]=pinned(a.notes_root/INTEGER_NAME,INTEGER_BYTES,INTEGER_SHA,"original p9 target consumer")
  reader_parent=module(a.notes_root/READER_NAME,"r150_joint_b_selected_parent")
  files={};inputs={}
  for key,d in b.ORIGINAL.items():
   files[key]=a.original_input_dir/d["name"];inputs[key]=pinned(files[key],d["bytes"],d["sha256"],key)
  small={}
  for name,(size,sha) in b.SMALL.items():
   small[name]=a.small_input_dir/name;inputs[name]=pinned(small[name],size,sha,name)
  for key,(name,size,sha) in b.FAMILIES.items():
   files[key]=a.true_source_dir/name;inputs[key]=pinned(files[key],size,sha,key)
  inputs["exactPrimitive"]=pinned(a.exact_gzip,*b.EXACT_PIN,"original exact primitive")
  mp=a.jet_map_dir/"jet-quotient-map.bin";mrp=a.jet_map_dir/"jet-quotient-map-receipt.json"
  inputs["jetMap"]=pinned(mp,*b.MAP_PIN,"complete local quotient map")
  inputs["jetMapReceipt"]=pinned(mrp,*b.MAP_RECEIPT_PIN,"complete local quotient map receipt")
  raw=gzip.decompress(a.recipe.read_bytes())
  check(len(raw)==b.RECIPE_PAYLOAD_BYTES and digest(raw)==b.RECIPE_PAYLOAD_SHA,"complete paid source recipe payload")
  recipe=json.loads(raw);check(recipe["binding"]==b.RECIPE_BINDING,"same original source recipe scope")
  inputs["recipePayload"]={"bytes":len(raw),"sha256":digest(raw)}
  parent,pack,parent_classes,parent_pins=reader_parent.load_parent(a.parent_out,a.notes_root,inputs,sources)
  inputs.update(parent_pins)
  semantic={"format":FORMAT,"driver":identity(Path(__file__)),"sources":sources,"inputs":inputs,
   "parentBinding":parent["binding"],"highDigitPrecisions":[15,10,5],"lowDigitPrecisions":[30,25,20,15,10,5],
   "originalTargetLabels":LABEL9,"coefficientModulus":MOD,"sameFreshParentForAllCoordinates":True}
  binding=digest(canonical(semantic));rec["binding"]=binding;rec["parameters"]["inputIdentity"]=semantic
  binding_file=a.out/"binding.json"
  if binding_file.exists():check(json.loads(binding_file.read_text())=={"binding":binding,"semantic":semantic},"same exact joint-B continuation")
  else:atomic_json(binding_file,{"binding":binding,"semantic":semantic})
  from flint import nmod_mat
  h=module(a.notes_root/"2026-11-14-r150-ninth-first-matrices-789f.py","r150_joint_b_paid_matrix_helper")
  state_reader=module(a.notes_root/"2026-11-14-r150-torsion-characteristic-789f.py","r150_joint_b_original_state")
  state=state_reader.load_state(files["state"]);J=nmod_mat(state["matrices"]["action"],31)
  K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose()
  O=nmod_mat(state["observabilityEchelon"],31);Astate=nmod_mat(state["matrices"]["A"],31)
  check((state["stateDimension"],state["torsionDimension"],state["observabilityRank"])==(820,315,505),"all original quotient dimensions")
  pr=json.loads(small["second-prepared-receipt.json"].read_text())
  pb=b.read_system(small["second-prepared-system.bin.gz"],pr,b"R150SP2A")
  PM=h.block(pb,pr,"whole315PrimaryProjector");Broot=h.block(pb,pr,"globalTwoPrimaryBasis")
  Li=h.block(pb,pr,"localTwoPrimaryLeftInverse")
  mapraw=mp.read_bytes();maprec=json.loads(mrp.read_text())
  maps={k:h.block(mapraw,maprec,k) for k in maprec["matrices"]}
  def pc(key):
   d=parent_classes[key];A=nmod_mat(d["matrixRows"],31)
   check(d["binding"]==parent["binding"] and field_record(A)==pack["classes"][key]["matrix"],"whole315 parent class "+key);return A
  D3,D4,D5,D6=[pc(k) for k in ("L3","L4","L5","L6")]
  U13=nmod_mat(recipe["true13Full315"],31)
  check(h.sub(U13,range(315),[8])==h.sub(D3,range(315),[0]) and h.sub(U13,range(315),range(9,13))==h.sub(D4,range(315),range(4)),
        "same actual higher source sections")
  U15=h.join(U13,h.sub(D5,range(315),[0,1]));U16=h.join(U15,D6)
  check(U16.rank()==16 and field_record(U16)["sha256"]==b.OLD_U16_SHA,"same complete true16 residue basis")
  action16=h.solve_span(U16,J*U16)
  check(h.zero(action16["residual"]) and field_record(action16["solution"])["sha256"]==b.OLD_J16_SHA,"same complete true16 parameter action")
  PU=PM*U16;chosen=[];rank=0
  for group,need in ((range(2),1),(range(2,7),5),(range(7,16),14)):
   for j in group:
    candidate=chosen+[j];r=h.sub(PU,range(315),candidate).rank()
    if r>rank:chosen.append(j);rank=r
   check(rank==need,"root2 complete basis rank at each exact exponent stratum")
  E=[EXP16[j] for j in chosen];U=h.sub(PU,range(315),chosen)
  check(len(chosen)==14 and E==[1,2,2,2,2,3,3,4,4,4,4,5,5,6] and sum(E)==47,
        "root2 invariant-factor basis: independent residues and exact total length")
  check(PM*U==U and h.zero(h.solve_span(U,J*U)["residual"]),"complete root2 basis and original parameter action")
  rec["parameters"]["actualRootTwoBasis"]={"originalTrue16Indices":chosen,"exponents":E,"length":47,
    "matrix":field_record(U),"projectedNotFalselyGlobalCoordinates":True}
  # Only the declared64 binding bytes change; every mathematical payload byte is retained.
  selected=a.out/"selected-parent";selected.mkdir(exist_ok=True);transports={}
  def rebind(key,offset):
   d=parent[key];src=a.parent_out/d["path"];dst=selected/(key+"-same-mathematical-payload.bin")
   head_length=offset+64
   with src.open("rb") as fi:
    head=fi.read(head_length);check(len(head)==head_length and head[offset:]==parent["binding"].encode(),"actual inherited source binding "+key)
    temporary=dst.with_name(dst.name+".tmp");ph=hashlib.sha256()
    with temporary.open("wb") as fo:
     fo.write(head[:offset]+binding.encode())
     for z in iter(lambda:fi.read(1048576),b""):ph.update(z);fo.write(z)
   new_identity=identity(temporary)
   if dst.exists():check(identity(dst)==new_identity,"same previously restored mathematical payload "+key);temporary.unlink()
   else:os.replace(temporary,dst)
   transports[key]={"parent":identity(src),"child":new_identity,"headerBindingOffset":offset,
    "allMathematicalPayloadBytesIdentical":True,"payloadSHA256":ph.hexdigest()}
   return dst
  for key,offset in (("G",24),("V",28),("L3",36),("L4",36),("L5",36),("L6",36)):files[key]=rebind(key,offset)
  rec["parameters"]["explicitParentTransports"]=transports
  model=module(a.notes_root/(b.STEM+"original-model-p9-789f.py"),"r150_joint_b_exact_model")
  model_file=a.out/"original-equations-mod31nine.txt"
  rec["parameters"]["originalP9Model"]=model.generate(a.exact_gzip,files["integerModel"],model_file)
  exact=json.loads(gzip.decompress(a.exact_gzip.read_bytes()))
  def product(A,B):
   C=[0]*(len(A)+len(B)-1)
   for i,x in enumerate(A):
    for j,y in enumerate(B):C[i+j]+=x*y
   return C
  fp=[-8,32,-25,5];fm=[864,864,135,5];e8=[9600,-25472,-3392,15936,-2888,-936,153,50,5]
  hs=product([0,0,0,1],product(product(fp,fp),product(product(fm,fm),e8)))
  check(len(hs)==24 and hs[-1]==3125 and product([-2,1],hs)==list(map(int,exact["h0"])),"same exact original hstar/h0 polynomial identity")
  Xi=nmod_mat(state["matrices"]["targetCoordinates"],31).transpose()
  Targets=nmod_mat(state["matrices"]["targets"],31).transpose()
  check(K*Xi==Targets and Astate*K==K*J and h.zero(O*Targets),"all original nine targets, action and505 observations")
  Hstar=nmod_mat(315,9,31)
  for c in reversed(hs):Hstar=J*Hstar+Xi*(c%31)
  initial=h.solve_span(U16,Hstar)
  check(initial["indices"]==list(range(16)) and h.zero(initial["residual"]),"complete original initial hstar class")
  Cglobal=initial["solution"]
  check(h.zero(h.sub(Cglobal,range(7,16),range(9))) and U16*Cglobal==Hstar,"true global U7 initial correction")
  C7=h.sub(Cglobal,range(7),range(9))
  rec["parameters"]["initialGlobalClass"]={"matrix":field_record(Hstar),"trueU7Coordinates":field_record(C7),
    "allOriginalTargetAndFreeProductsVerified":True}
  save()

  binaries=a.out/"bin";binaries.mkdir(exist_ok=True);programs={}
  native={**b.NATIVE,"integer":INTEGER_NAME}
  for key,name in native.items():
   tick();exe=binaries/key;meta=binaries/(key+".json")
   ck=digest(canonical({"source":sources[name],"headers":{k:v for k,v in sources.items() if k.endswith(".hpp")},"flags":["g++","-O3","-std=c++17"]}))
   if not (exe.exists() and meta.exists() and json.loads(meta.read_text())=={"binding":ck,"executable":identity(exe)}):
    with (logs/("compile-"+key+".log")).open("wb") as log:
     q=subprocess.run(["g++","-O3","-std=c++17","-I",str(a.notes_root),str(a.notes_root/name),"-o",str(exe)],
       stdout=log,stderr=subprocess.STDOUT,timeout=min(60,max(1,deadline-time.monotonic()-2)))
    check(q.returncode==0,"native compilation "+key);atomic_json(meta,{"binding":ck,"executable":identity(exe)})
   programs[key]=[str(exe)]
  programs["solve"]=[sys.executable,str(a.notes_root/(b.STEM+"local-unit-solve35-789f.py"))]
  def prefix(name):
   d=a.out/"stages"/name;d.mkdir(parents=True,exist_ok=True);return d/name
  def run(name,program,args,marker,gates,stage_inputs,outputs,logic):
   tick();source=native[program] if program in native else b.STEM+"local-unit-solve35-789f.py"
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
    "TaylorPrecision","GCachePrecision","allOriginal17CoefficientsDivisible","sameOriginalHStarAndAllNineSquaresVerified",
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
  def spec(name,labels,L,ring=2):
   p=specs/(name+".spec");b.write_spec(p,labels,L,ring);return p
  def target(name,labels,weights):
   """weights[seed][target] is an exact constant or linear polynomial in x=s-2."""
   check(len(weights)==9 and all(len(row)==len(labels) for row in weights),"original target-combination dimensions")
   edges=[]
   for i,row in enumerate(weights):
    for j,polynomial in enumerate(row):
     q=b.trim_integer(polynomial)
     check(len(q)<=2,"only actual constant/linear Taylor target multipliers")
     if q:edges.append((i,j,q))
   lines=["R150_JOINT_B_ORIGINAL_HSTAR_TARGETS_P9_V1 31 %d 24 9 %d %d"%(MOD,len(labels),len(edges)),
     " ".join(str(z%MOD) for z in hs)," ".join(map(str,LABEL9))," ".join(map(str,labels))]
   lines+=["%d %d %d %s"%(i,j,len(q)," ".join(map(str,q))) for i,j,q in edges]
   p=specs/(name+".targets");atomic(p,("\n".join(lines)+"\n").encode("ascii"))
   return p
  target9=target("nine-original-b",LABEL9,[[[int(i==j)] for j in range(9)] for i in range(9)])
  def mix(path,labels,L,power,families):
   active=[f for f in families if f["edges"]]
   if active:return b.write_mix(path,labels,L,[power]*len(labels),active)
   text="R150_JOINT_B_INTEGER_MIX_V1 %d %d 0\n%s\n"%(len(labels),L," ".join([str(power)]*len(labels)))
   atomic(path,text.encode("ascii"));return [],[]
  def integer(name,labels,L,divisor,retained,target_power,target_file,families):
   p=prefix(name);s=spec(name,labels,L);mi=p.parent/(name+".mix")
   logic,inf=mix(mi,labels,L,divisor,families)
   run(name,"integer",[files["model"],model_file,s,mi,p,binding,retained,"__REMAINING__",target_file,target_power],
    "joint-b-target-integer-p9-jets-complete",
    {"allOriginal17CoefficientsDivisible":True,"targetCount":len(labels),"computedTaylorPrecision":L,
     "retainedFormalPrecision":retained,"targetScalarPower":target_power,
     "sameOriginalHStarAndAllNineSquaresVerified":True,"residualIsTargetMinusOriginalAProduct":True},
    [files["model"],model_file,s,target_file]+inf,
    [b.suffix(p,k) for k in ("-original6188-integer-jets.bin","-divided-original-jets.bin",
     "-field-root2-jets.bin","-field-projected-crt8-jets.bin","-integer-product.json")],
    {"divisorExponent":divisor,"targetPower":target_power,"retained":retained,"families":logic})
   return p
  def normal(name,labels,L,field,crt=False):
   p=prefix(name);s=spec(name,labels,L,12 if crt else 2)
   run(name,"normal",[files["model"],field,files["graph"],s,p,binding],
    "saturated-runtime-two-ring-state-complete" if crt else "saturated-runtime-root2-normal-form-complete",{},
    [files["model"],field,files["graph"],s],
    [b.suffix(p,k) for k in ("-standard-state.bin" if crt else "-original1034-root2.bin",
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
   D=Broot*Li*h.sub(D39,pr["localTwoPrimaryPivotRows"],range(n))
   check(maps["globalTorsionTo39"]*D==D39 and PM*D==D,"complete315 root2 primary class, not a global interpolation claim")
   original=K*D
   check(h.zero(O*original) and Astate*original==K*(J*D),"all505 original free conditions and same full parameter action")
   item={"matrix":field_record(D),"all104LocalFreeChecks":True,"all315OriginalCoordinateReconstruction":True,
    "all505GlobalFreeChecks":True,"sameOriginalSAction":True,"rootTwoPrimaryProjectionExplicit":True}
   atomic_json(p.parent/"complete315-class.json",{"binding":binding,**item,"matrixRows":rows(D)})
   rec["parameters"]["classes"][name]=item;save();return D
  def coordinates(name,D,max_order=None):
   solved=h.solve_span(U,D)
   check(solved["indices"]==list(range(14)) and h.zero(solved["residual"]),"complete actual root2 true-source span "+name)
   C=solved["solution"];check(U*C==D,"all315 exact true-coordinate products "+name)
   if max_order is not None:
    check(all(not int(C[i,j]) for i,e in enumerate(E) if e>max_order for j in range(C.ncols())),
      "actual digit respects proved p-order bound "+name)
   rec["parameters"]["coordinateChecks"][name]={"basis":field_record(U),"targets":field_record(D),
    "coordinates":field_record(C),"all315ProductsVerified":True,"provedOrderUpperBound":max_order}
   atomic_json(a.out/(name+"-coordinates.json"),{"binding":binding,"coordinates":rows(C)})
   save();return C
  def solve_source(name,labels,L,integer_output):
   nf=normal(name+"-normal",labels,L,b.suffix(integer_output,"-field-root2-jets.bin"))
   d=a.out/"stages"/(name+"-complete");d.mkdir(parents=True,exist_ok=True)
   run(name+"-complete","solve",["--G",files["G"],"--rhs",b.suffix(nf,"-original1034-root2.bin"),
    "--binding",binding,"--notes-root",a.notes_root,"--out",d,"--remaining-seconds","__REMAINING__"],
    "saturated-local-unit-solve-complete",{"fullOriginalGIdentityVerified":True,"all13FreeConditionsRetained":True},
    [files["G"],b.suffix(nf,"-original1034-root2.bin")],[d/"complete-G-q-root2.bin",d/"local-unit-solve-receipt.json"],
    {"originalRows":1034,"maximumFormalSourcePrecisionLoss":5})
   s=spec(name,labels,L);v=prefix(name+"-vq");mode="q3"
   run(name+"-vq","vq",[files["model"],files["V"],d/"complete-G-q-root2.bin",files["oldK"],"-",v,binding,mode,s],
    "saturated-runtime-jet-VQ-complete",{"mode":mode},
    [files["model"],files["V"],d/"complete-G-q-root2.bin",files["oldK"],s],
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
  def true_correction(C,scalar_power,L,indices=chosen):
   """Positive source correction: target minus A(source+correction)."""
   check(C.nrows()==len(indices),"source basis coordinate count")
   n=C.ncols();where={g:i for i,g in enumerate(indices)};out=[]
   configs=[
    ("kernels",[2275,2276,2277,2278],[(0,0),(1,1)],None),
    ("fourK2",[4001,4002,4003,4004],[(j,j+2) for j in range(4)],None),
    ("selectedK2",LABEL9,[(0,6)],None),
    ("newOriginal",b.LABEL16,[(2,7)],None),
    ("L3",parent["L3"]["sourceLabels"],[(0,8)],parent["L3"]["valid"]),
    ("L4",parent["L4"]["sourceLabels"],[(j,9+j) for j in range(4)],parent["L4"]["valid"]),
    ("L5",parent["L5"]["sourceLabels"],[(0,13),(1,14)],parent["L5"]["valid"]),
    ("L6",parent["L6"]["sourceLabels"],[(0,15)],parent["L6"]["valid"])]
   for key,labels,pairs,valid in configs:
    edges=[]
    for source,g in pairs:
     if g not in where:continue
     row=where[g];active=any(int(C[row,j]) for j in range(n))
     if active:
      check(scalar_power>=EXP16[g],"no negative source power in actual correction")
      check(valid is None or L<=valid,"do not use an unproved high Taylor tail of a source")
      for j in range(n):
       if int(C[row,j]):edges.append([source,j,[31**(scalar_power-EXP16[g])*int(C[row,j])]])
    if edges:out.append(b.family(files[key],labels,edges))
   return out

  # p^2*b-A*S1=p^3*r1. Initial U7 correction is genuinely global; q0 is local.
  S0=integer("b-initial-u7-correction",LABEL9,20,2,20,2,target9,
    true_correction(C7,2,20,list(range(7))))
  check(h.zero(complete_class("b-initial-full-zero-class",LABEL9,S0)),"true initial correction kills the complete root2 class")
  q0=solve_source("b-initial-q0",LABEL9,20,S0)
  R1=integer("b-first-true-carry",LABEL9,20,3,15,2,target9,
    [b.family(source_of(S0),LABEL9,b.identity_edges(9)),b.family(q0,LABEL9,b.identity_edges(9,31**2))])
  D1=complete_class("b-first-carry-complete315",LABEL9,R1)
  old_basis_coordinates=h.solve_span(U16,D1)
  check(h.zero(old_basis_coordinates["residual"]) and field_record(old_basis_coordinates["solution"])["sha256"]==PAID_C1_SHA,
    "all original first-carry315 coordinates match the paid control in the full residue basis")
  high_digits=[coordinates("high-r1",D1)]
  current=R1
  # Multiply the whole original identity by p^3 before using the e6 source.
  # p^5*b-A*(p^3*S1)=p^6*r1; both subsequent source powers remain nonnegative.
  for k,L in enumerate((15,10)):
   divisor=6+k
   families=[b.family(source_of(current),LABEL9,b.identity_edges(9,31**3 if k==0 else 1))]
   families+=true_correction(high_digits[k],divisor,L)
   corrected=integer("high-digit%d-corrected"%k,LABEL9,L,divisor,L,5,target9,families)
   check(h.zero(complete_class("high-digit%d-full-zero"%k,LABEL9,corrected)),"all original high-digit field obstructions vanish")
   q=solve_source("high-digit%d-q"%k,LABEL9,L,corrected)
   current=integer("high-digit%d-next"%(k+1),LABEL9,L,divisor+1,L-5,5,target9,
    [b.family(source_of(corrected),LABEL9,b.identity_edges(9)),b.family(q,LABEL9,b.identity_edges(9,31**divisor))])
   D=complete_class("high-digit%d-complete315"%(k+1),LABEL9,current)
   high_digits.append(coordinates("high-r%d"%(k+2),D))
  high_index=[i for i,e in enumerate(E) if e>=4];small_exp=[E[i]-3 for i in high_index]
  check(small_exp==[1,1,1,1,2,2,3],"all seven actual high-coordinate moduli")
  relative=[[sum(31**k*int(high_digits[k][i,j]) for k in range(3))%(31**(E[i]-3))
             for j in range(9)] for i in high_index]
  full_high=[[0]*9 for _ in E]
  for r,i in enumerate(high_index):
   for j in range(9):full_high[i][j]=31**3*relative[r][j]%(31**E[i])
  high_image=group_image(full_high,E)
  check(high_image["exponents"]==[1,2,2,3] and high_image["length"]==8,"true complete p^2B invariant factors")
  high3=group_image(scaled(full_high,31,E),E)
  check(high3["exponents"]==[1,1,2],"true complete p^3B equals the paid p^4T type")
  c1_high=h.sub(high_digits[0],high_index,range(9))
  chosen_targets=[];r=0
  for j in range(9):
   q=h.sub(c1_high,range(7),chosen_targets+[j]).rank()
   if q>r:chosen_targets.append(j);r=q
  check(r==4 and len(chosen_targets)==4,"four actual original b_i generate p^2B modulo p^3B")
  modulus3=31**3
  uniform=[[31**(3-e)*x%modulus3 for x in row] for e,row in zip(small_exp,relative)]
  selected_uniform=[[row[j] for j in chosen_targets] for row in uniform]
  adapted=smith_mod(selected_uniform,3)
  check(adapted["valuations"]==[0,1,1,2],"exact high source adapted orders (5,4,4,3)")
  V4=adapted["right"];U7=adapted["left"];transformed=mm(U7,uniform,modulus3)
  coefficient_in_adapted=[]
  for i,v in enumerate(adapted["valuations"]):
   divisor=31**v;check(all(x%divisor==0 for x in transformed[i]),"all nine exact high compatibility divisibilities")
   coefficient_in_adapted.append([(x//divisor)%(31**(3-v)) for x in transformed[i]])
  check(all(x==0 for row in transformed[4:] for x in row),"all high residual rows for all nine original b targets")
  coefficients=mm(V4,coefficient_in_adapted,modulus3)
  check(mm(selected_uniform,coefficients,modulus3)==uniform,"all63 original high relations, not only their mod31 ranks")
  selected_full=[[row[j] for j in chosen_targets] for row in full_high]
  full_adapted=mm(selected_full,V4,31**6)
  full_adapted=[[x%(31**E[i]) for x in row] for i,row in enumerate(full_adapted)]
  Horders=[5,4,4,3]
  for j,e in enumerate(Horders):
   check(group_image([[row[j]] for row in full_adapted],E)["exponents"]==[e-2],"each adapted p^2h has the exact declared order")
  remaining=[j for j in range(9) if j not in chosen_targets]
  check(len(remaining)==5,"exact five low residual original b targets")
  low_labels=list(range(40001,40016));weights=[[[] for _ in range(15)] for _ in range(9)]
  for pos,j in enumerate(remaining):
   weights[j][pos]=[1]
   for k,i in enumerate(chosen_targets):
    if coefficients[k][j]:weights[i][pos]=[-coefficients[k][j]]
  for j in range(9):weights[j][5+j]=[0,1]
  h3_index=Horders.index(3)
  for k,i in enumerate(chosen_targets):
   if V4[k][h3_index]:weights[i][14]=[31*V4[k][h3_index]]
  target_low=target("fourteen-low-generators-and-true-p-h3",low_labels,weights)
  high_data={"binding":binding,"rootTwoBasisOriginalIndices":chosen,"rootTwoExponents":E,
   "chosenOriginalBIndices":chosen_targets,"chosenOriginalBLabels":[LABEL9[j] for j in chosen_targets],
   "highDigitCoordinateRows":[rows(C) for C in high_digits],"p2BRelativeCoordinates":relative,
   "p2BFullRootTwoCoordinates":full_high,"uniformSevenByNine":uniform,
   "adaptedOriginalFourByFour":V4,"adaptedHOrders":Horders,
   "allNineOriginalHighCoefficients":coefficients,"remainingOriginalBIndices":remaining,
   "adaptedP2HRootTwoCoordinates":full_adapted,"lowTargetWeightsInX":weights,
   "highImage":high_image,"p3BImage":high3,
   "all63HighRelationsVerified":True,"sameActualIntegerCoefficientLiftsUsedForLowTargets":True}
  atomic_json(a.out/"exact-high-relations.json",high_data)
  rec["parameters"]["highRelations"]={"file":identity(a.out/"exact-high-relations.json"),
   "chosenOriginalBLabels":high_data["chosenOriginalBLabels"],"p2B":high_image,"p3B":high3,
   "all63OriginalHighRelationsVerified":True,"adaptedHOrders":Horders,
   "trueLowTargetCount":15,"lowTargetModel":identity(target_low)}
  save()
  if a.through=="high":
   rec["status"]="completed-prefix";rec["parameters"]["completedThrough"]="exact-high-relations";save();return 0
  # Every low target w has proved order<=p^2: five exact residuals, nine xb_j,
  # and the additional actual p*h3, which is not inferred by dividing p^2h3.
  current=integer("low-initial-original-targets",low_labels,30,2,30,2,target_low,[])
  low_digits=[]
  D=complete_class("low-digit0-complete315",low_labels,current)
  low_digits.append(coordinates("low-r0",D,max_order=2))
  for k,L in enumerate((30,25,20,15,10)):
   scalar_power=2+k
   families=[b.family(source_of(current),low_labels,b.identity_edges(15))]
   families+=true_correction(low_digits[k],scalar_power,L)
   corrected=integer("low-digit%d-corrected"%k,low_labels,L,scalar_power,L,2,target_low,families)
   check(h.zero(complete_class("low-digit%d-full-zero"%k,low_labels,corrected)),"complete actual low-digit zero quotient")
   q=solve_source("low-digit%d-q"%k,low_labels,L,corrected)
   current=integer("low-digit%d-next"%(k+1),low_labels,L,scalar_power+1,L-5,2,target_low,
    [b.family(source_of(corrected),low_labels,b.identity_edges(15)),
     b.family(q,low_labels,b.identity_edges(15,31**scalar_power))])
   D=complete_class("low-digit%d-complete315"%(k+1),low_labels,current)
   low_digits.append(coordinates("low-r%d"%(k+1),D,max_order=3+k))
  low_coordinates=[[sum(31**k*int(low_digits[k][i,j]) for k in range(6))%(31**e)
                    for j in range(15)] for i,e in enumerate(E)]
  check(all((31**2*x)%(31**E[i])==0 for i,row in enumerate(low_coordinates) for x in row),
    "all fifteen true low classes are killed by p^2 in the complete root2 D module")
  # The first three columns of H[p^2] follow from the true high identities.
  # The last column is the separately computed actual p*h3.
  H2=[]
  for i,e in enumerate(E):
   H2.append([(31**(Horders[j]-4)*full_adapted[i][j])%(31**e) for j in range(3)]+[low_coordinates[i][14]])
  S=[row[:14] for row in low_coordinates];X=[row[5:14] for row in low_coordinates]
  h2_image=group_image(H2,E)
  check(h2_image["exponents"]==[2,2,2,2] and h2_image["length"]==8,"all four genuine H[p^2] generators and complete independence")
  for j in range(9):
   check(group_image([[row[j]] for row in X],E)["exponents"]==[2],"each original x*b_j retains its paid exact order two")
  check(group_image([[row[14]] for row in low_coordinates],E)["exponents"]==[2],"the true p*h3 has exact order two")
  Kcoordinates=joined(H2,S);imageK=group_image(Kcoordinates,E)
  denominator_coordinates=joined(H2,scaled(S,31,E))
  denominator=group_image(denominator_coordinates,E)
  quotient_length=imageK["length"]-8;n2=denominator["length"]-8;n1=quotient_length-2*n2
  check(n1>=0 and n2>=0 and n1+n2<=14,"complete low quotient has legitimate exact one/two multiplicities")
  invariant=sorted([1]*n1+[2]*n2+[3,4,4,5])
  check(sum(invariant)==16+quotient_length<=47,"complete joint B length and actual root2 ambient bound")
  x_image=group_image(X,E);px_image=group_image(scaled(X,31,E),E)
  check(px_image["exponents"]==[1],"same paid one-dimensional image p*x*B")
  denominator_with_x=group_image(joined(denominator_coordinates,X),E)
  x_rank_on_low_mod_p=denominator_with_x["length"]-denominator["length"]
  minimum_r=4+n1+n2-x_rank_on_low_mod_p
  check(0<=x_rank_on_low_mod_p<=n1+n2 and 1<=minimum_r<=9,"exact R-generator count from B/(pB+xB)")
  # A complete D presentation uses four adapted high generators and14 low ones.
  # Every relation involving the low subgroup intersects H in exactly H[p^2].
  # Compute the complete finite kernel of [H[p^2],S], then pull it back into H+S.
  full_mod=31**6
  Kembedded=[[31**(6-e)*z%full_mod for z in row] for e,row in zip(E,Kcoordinates)]
  Ksmith=smith_mod(Kembedded,6);KV=Ksmith["right"];kr=len(Ksmith["valuations"])
  Krelations=[[KV[i][j]*(31**(6-Ksmith["valuations"][j]) if j<kr else 1)%full_mod for j in range(18)] for i in range(18)]
  check(mm(Kembedded,Krelations,full_mod)==[[0]*18 for _ in range(14)],"complete original finite-kernel product")
  presentation=[[0]*22 for _ in range(18)]
  for i,e in enumerate(Horders):presentation[i][i]=31**e
  for i in range(18):
   factor=31**(Horders[i]-2) if i<4 else 1
   for j in range(18):presentation[i][4+j]=factor*Krelations[i][j]%full_mod
  Psmith=smith_mod(presentation,6)
  check(len(Psmith["valuations"])==18 and sorted(v for v in Psmith["valuations"] if v)==invariant,
    "full original joint B presentation Smith factors agree with the independent quotient-length computation")
  action=[[0]*18 for _ in range(18)]
  for k,i in enumerate(chosen_targets):
   for j in range(4):action[4+5+i][j]=V4[k][j]%full_mod
  for pos,j in enumerate(remaining):
   action[4+5+j][4+pos]=1
   for k,i in enumerate(chosen_targets):action[4+5+i][4+pos]=(-coefficients[k][j])%full_mod
  check(mm(action,action,full_mod)==[[0]*18 for _ in range(18)],"literal original x action is square-zero")
  def relation_membership(M):
   transformed=mm(Psmith["left"],M,full_mod)
   return all(z%(31**Psmith["valuations"][i])==0 for i,row in enumerate(transformed) for z in row)
  check(relation_membership(mm(action,presentation,full_mod)),"literal original parameter action preserves every complete D relation")
  pmat=nmod_mat([[z%31 for z in row] for row in presentation],31)
  join=nmod_mat([[z%31 for z in row] for row in joined(presentation,action)],31)
  check(18-pmat.rank()==len(invariant) and 18-join.rank()==minimum_r,"independent Nakayama counts for D and D[x] generators")
  # Carry the original nine b_j through the same adapted H basis.
  Vinv=[row[:] for row in V4];inverse=eye(4)
  for k in range(4):
   pivot=next((i for i in range(k,4) if Vinv[i][k]%31),None);check(pivot is not None,"D-unit adapted basis inverse")
   Vinv[k],Vinv[pivot]=Vinv[pivot],Vinv[k];inverse[k],inverse[pivot]=inverse[pivot],inverse[k]
   inv=pow(Vinv[k][k],-1,full_mod);Vinv[k]=[z*inv%full_mod for z in Vinv[k]];inverse[k]=[z*inv%full_mod for z in inverse[k]]
   for i in range(4):
    if i==k:continue
    q=Vinv[i][k]
    Vinv[i]=[(z-q*w)%full_mod for z,w in zip(Vinv[i],Vinv[k])]
    inverse[i]=[(z-q*w)%full_mod for z,w in zip(inverse[i],inverse[k])]
  check(mm(V4,inverse,full_mod)==eye(4) and mm(inverse,V4,full_mod)==eye(4),"both exact adapted basis inverse products")
  original_b=[[0]*9 for _ in range(18)]
  for k,j in enumerate(chosen_targets):
   for i in range(4):original_b[i][j]=inverse[i][k]
  for pos,j in enumerate(remaining):
   for i in range(4):original_b[i][j]=sum(inverse[i][k]*coefficients[k][j] for k in range(4))%full_mod
   original_b[4+pos][j]=1
  original_xb=[[int(i==4+5+j) for j in range(9)] for i in range(18)]
  discrepancy=[[(z-w)%full_mod for z,w in zip(row,other)] for row,other in zip(mm(action,original_b,full_mod),original_xb)]
  check(relation_membership(discrepancy),"all original nine x*b transports in the complete presentation")
  check(nmod_mat([[z%31 for z in row] for row in joined(presentation,original_b,original_xb)],31).rank()==18,
        "all eighteen original b_j and x*b_j generate the complete presentation")
  nonunit=[i for i,v in enumerate(Psmith["valuations"]) if v]
  quotient_exponents=[Psmith["valuations"][i] for i in nonunit]
  cyclic_checks=[]
  for j in range(9):
   block=[[original_b[i][j],original_xb[i][j]] for i in range(18)]
   changed=mm(Psmith["left"],block,full_mod)
   c=[[z%(31**Psmith["valuations"][i]) for z in changed[i]] for i in nonunit]
   actual=group_image(c,quotient_exponents)
   check(actual["exponents"]==[2,5],"each original R cyclic module has the independently paid exact D type(5,2)")
   cyclic_checks.append({"label":LABEL9[j],"exponents":actual["exponents"],"length":actual["length"]})
  complete={"binding":binding,"ambientRootTwoBasisOriginalIndices":chosen,"ambientExponents":E,
   "highOriginalTargetIndices":chosen_targets,"adaptedHOrders":Horders,"lowTargetLabels":low_labels,
   "highCoordinates":high_data,"lowDigitCoordinateRows":[rows(C) for C in low_digits],
   "lowRootTwoCoordinates":low_coordinates,"Hp2Coordinates":H2,"lowFourteenCoordinates":S,
   "KCoordinates":Kcoordinates,"DPresentation":presentation,"parameterXAction":action,
   "originalNineBTransport":original_b,"originalNineXBTransport":original_xb,
   "completeDInvariantExponents":invariant,"minimumDGenerators":len(invariant),"minimumRGenerators":minimum_r,
   "jointLength":sum(invariant),"lowExponentOneMultiplicity":n1,"lowExponentTwoMultiplicity":n2,
   "allOriginalSmallProductsAndRelationTransportsVerified":True}
  atomic_json(a.out/"complete-original-joint-b-presentation.json",complete)
  final={"completeDInvariantExponents":invariant,"jointLength":sum(invariant),
   "minimumDGenerators":len(invariant),"minimumDPolynomialGenerators":minimum_r,
   "lowExponentOneMultiplicity":n1,"lowExponentTwoMultiplicity":n2,
   "highDirectSummandExponents":[3,4,4,5],"p2B":high_image,"p3B":high3,
   "Hp2":h2_image,"Hp2PlusLow":imageK,"lowQuotientLength":quotient_length,
   "xB":x_image,"pXB":px_image,"xRankOnLowQuotientModuloP":x_rank_on_low_mod_p,
   "DPresentation":integer_record(presentation),"parameterXAction":integer_record(action),
   "actualOriginalNineBTransport":integer_record(original_b),"actualOriginalNineXBTransport":integer_record(original_xb),
   "completePresentationFile":identity(a.out/"complete-original-joint-b-presentation.json"),
   "individualOriginalCyclicChecks":cyclic_checks,
   "allOriginal6188SourceRowsAnd4367OutputRowsRetained":True,
   "all104LocalFreeAnd315CoordinateAnd505GlobalFreeChecks":True,
   "allHighRelationsVerifiedModuloTheirFullPowers":True,"allSixLowDigitsActuallyComputed":True,
   "allHigherOrderDigitSupportsChecked":True,"lastRemainderKilledByPaidFullP6T":True,
   "rootTwoCompletionUsedThroughout":True,"rootOneAbsenceUsesPaidXSquareBZero":True,
   "completePresentationAndXStabilityVerified":True,"bothMinimumGeneratorCountsIndependentlyVerified":True,
   "individualCyclicLengthNotConfusedWithJointLength":True,"highPActionNotReadFromResidueJ16":True,
   "full210NotRecomputed":True,"newGlobalPolynomialSourcesClaimed":False}
  rec["status"]="completed";rec["parameters"]["final"]=final;save();return 0
 except (BudgetStop,subprocess.TimeoutExpired) as exc:
  rec["status"]="budget-checkpoint";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);save();return 75
 except BaseException as exc:
  rec["status"]="failed";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);save();return 1
 finally:
  save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
if __name__=="__main__":raise SystemExit(main())
