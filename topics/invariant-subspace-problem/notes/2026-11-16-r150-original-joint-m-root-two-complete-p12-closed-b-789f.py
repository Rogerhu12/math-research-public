#!/usr/bin/env python3
"""Recover the complete root-two coefficient torsion of the original joint M.
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
MOD=787662783788549761
BASE_NAME="2026-11-16-r150-joint-m-true16-source-rebuild-p9-bounded50-789f.py"
BASE_SHA="07cd9a2c6d09c9efc11be8aba50cbdd5bceba6f058f1fab986f6a1017a150d87"
BASE_BYTES=38621
READER_NAME="2026-11-16-r150-joint-m-bounded50-parent-reader-789f.py"
READER_SHA="47d4ea67ed5144bc3764bc2c0662f861e0a3bc791dae016a10bafe3c09d3b903"
READER_BYTES=7515
INTEGER_NAME="2026-11-16-r150-joint-m-original-target-integer-p12-jets50-789f.cpp"
INTEGER_SHA="42be4d23378406896d6e4e8779b363fab8f877e62e4309eec1507c38206ac8e9"
INTEGER_BYTES=22675
MODEL_NAME="2026-11-16-r150-joint-m-original-model-p12-789f.py"
MODEL_BYTES=4294
MODEL_SHA="6310cf2217dbe7770b117bb37c2d7d84a0cc6f77a9e0dffcbdb0ae036ed2362c"
UNIT_NAME="2026-11-16-r150-joint-m-bounded50-local-unit-solve-789f.py"
FORMAT="r150-original-joint-m-root-two-complete-p12-closed-B-v2"
EXP16=[1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6]
LABEL9=list(range(2,11))
QUALIFICATION_BYTES=20106
QUALIFICATION_SHA="9b8c104b8cbd9d7fbe17c7e6fbddd1067c66d6a6a17252ed9c8f854b7cd2a2a7"
DIGIT_PRECISIONS=[30,25,20,15,10,5]
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
 for name in ("notes-root","parent-out","original-input-dir","small-input-dir","true-source-dir","exact-gzip","jet-map-dir","recipe","qualification-receipt","out"):
  ap.add_argument("--"+name,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=1800)
 ap.add_argument("--memory-mib",type=int,default=4096)
 ap.add_argument("--through",choices=("coordinates","final"),default="final")
 a=ap.parse_args()
 check(0<a.seconds<=1800 and 1024<=a.memory_mib<=6144,"bounded same-job joint-M root-two resource contract")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();deadline=start+a.seconds
 rec={"format":FORMAT,"status":"running","parameters":{"prime":31,"integerModulus":MOD,
  "originalSourceRows":6188,"originalOutputRows":4367,"full210Recomputed":False,
  "digitPrecisions":DIGIT_PRECISIONS,
  "largeArraysTemporaryOnly":True,"stages":{},"classes":{},"coordinateChecks":{}}}
 rp=a.out/"original-joint-m-root-two-complete-p12-receipt.json"
 def save():
  rec["elapsedSeconds"]=time.monotonic()-start;atomic_json(rp,rec)
 def tick():
  if time.monotonic()>=deadline-2:raise BudgetStop("joint-M root-two shared budget")
 def stop(signum,frame):raise BudgetStop("joint-M root-two signal "+str(signum))
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 logs=a.out/"logs";logs.mkdir(exist_ok=True);cache=a.out/"stage-cache";cache.mkdir(exist_ok=True)
 try:
  bp=a.notes_root/BASE_NAME;pinned(bp,BASE_BYTES,BASE_SHA,"p9 true16 dependency reconstruction")
  b=module(bp,"r150_joint_b_selected_base")
  sources={BASE_NAME:identity(bp)}
  for name,sha in b.SOURCES.items():
   z=identity(a.notes_root/name);check(z["sha256"]==sha,"frozen mathematical helper "+name);sources[name]=z
  sources[READER_NAME]=pinned(a.notes_root/READER_NAME,READER_BYTES,READER_SHA,"p9 exact parent reader")
  sources[INTEGER_NAME]=pinned(a.notes_root/INTEGER_NAME,INTEGER_BYTES,INTEGER_SHA,"original p12 raw-target consumer")
  sources[MODEL_NAME]=pinned(a.notes_root/MODEL_NAME,MODEL_BYTES,MODEL_SHA,"original p12 primitive coefficient reduction")
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
  inputs["primitiveMQualification"]=pinned(a.qualification_receipt,QUALIFICATION_BYTES,QUALIFICATION_SHA,"actual full original M primitive-lattice qualification")
  qualification=json.loads(a.qualification_receipt.read_bytes())
  check(qualification["status"]=="completed" and qualification["parameters"]["final"]["completePrimitiveFreeLatticeQualified"] is True,
        "paid primitive integral free lattice is actually qualified")
  parent,pack,parent_classes,parent_pins=reader_parent.load_parent(a.parent_out,a.notes_root,inputs,sources)
  inputs.update(parent_pins)
  semantic={"format":FORMAT,"driver":identity(Path(__file__)),"sources":sources,"inputs":inputs,
   "parentBinding":parent["binding"],"digitPrecisions":DIGIT_PRECISIONS,
   "originalTargetLabels":LABEL9,"coefficientModulus":MOD,"sameFreshParentForAllCoordinates":True}
  binding=digest(canonical(semantic));rec["binding"]=binding;rec["parameters"]["inputIdentity"]=semantic
  binding_file=a.out/"binding.json"
  if binding_file.exists():check(json.loads(binding_file.read_text())=={"binding":binding,"semantic":semantic},"same exact joint-M continuation")
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
  # G/V change only binding bytes. The p9 source jets are genuine canonical
  # integer representatives: crop to the paid30 prefix, then recalculate A*kappa
  # in p12 arithmetic. No previously calculated A*kappa coefficient is reused.
  selected=a.out/"selected-parent";selected.mkdir(exist_ok=True);transports={}
  def rebind_field(key,offset):
   d=parent[key];src=a.parent_out/d["path"];dst=selected/(key+"-same-field-payload.bin")
   temporary=dst.with_name(dst.name+".tmp");ph=hashlib.sha256()
   with src.open("rb") as fi,temporary.open("wb") as fo:
    head=fi.read(offset+64);check(len(head)==offset+64 and head[offset:]==parent["binding"].encode(),"actual field parent binding "+key)
    fo.write(head[:offset]+binding.encode())
    for z in iter(lambda:fi.read(1048576),b""):ph.update(z);fo.write(z)
   new_identity=identity(temporary)
   if dst.exists():check(identity(dst)==new_identity,"same restored field payload "+key);temporary.unlink()
   else:os.replace(temporary,dst)
   transports[key]={"parent":identity(src),"child":new_identity,"headerBindingOffset":offset,"allFieldPayloadBytesIdentical":True,"payloadSHA256":ph.hexdigest()}
   return dst
  for key,offset in (("G",24),("V",28)):files[key]=rebind_field(key,offset)
  def bridge_source(key):
   d=parent[key];src=a.parent_out/d["path"];dst=selected/(key+"-canonical-p9-lift-in-p12-valid30.bin")
   n,L,valid,e=d["labels"],d["L"],d["valid"],d["e"]
   check(valid>=30 and L>=30 and e<=6,"all30 lifted coefficients are actually stable "+key)
   temporary=dst.with_name(dst.name+".tmp");selected_hash=hashlib.sha256();count=0
   with src.open("rb") as fi,temporary.open("wb") as fo:
    fixed=fi.read(100);labels=fi.read(2*n);exponents=fi.read(n)
    check(fixed[:8]==b"R150SJ91" and struct.unpack_from("<IQ4I",fixed,8)==(31,31**9,6188,n,L,2) and fixed[36:100]==parent["binding"].encode(),"actual canonical p9 parent header "+key)
    check(list(struct.unpack("<%dH"%n,labels))==d["sourceLabels"] and exponents==bytes([e]*n),"exact original source labels and divisor orders "+key)
    fo.write(b"R150SJ12"+struct.pack("<IQ4I",31,MOD,6188,n,30,2)+binding.encode()+labels+exponents)
    for r in range(6188):
     head=fi.read(15);payload=fi.read(8*L*n)
     check(len(head)==15 and len(payload)==8*L*n,"all6188 complete canonical original rows "+key)
     values=struct.unpack("<%dQ"%(L*n),payload)
     check(all(v<31**9 for v in values),"canonical p9 source representative coefficients "+key)
     selected_bytes=payload[:8*30*n];fo.write(head);fo.write(selected_bytes)
     selected_hash.update(head);selected_hash.update(selected_bytes);count+=30*n
    check(not fi.read(1),"complete canonical source EOF "+key)
   new_identity=identity(temporary)
   if dst.exists():check(identity(dst)==new_identity,"same canonical source lift "+key);temporary.unlink()
   else:os.replace(temporary,dst)
   transports[key]={"parent":identity(src),"child":new_identity,"parentModulus":31**9,"newModulus":MOD,
    "actualStableTaylorPrecision":30,"allOriginalRowsPreserved":6188,"canonicalSelectedCoefficients":count,
    "selectedOriginalPayloadSHA256":selected_hash.hexdigest(),"previousAProductNotReused":True,
    "sameDividedSourceClassUsesExponentAtMostSix":e<=6}
   return dst
  for key in ("L3","L4","L5","L6"):files[key]=bridge_source(key)
  rec["parameters"]["explicitParentTransports"]=transports
  model=module(a.notes_root/MODEL_NAME,"r150_joint_m_exact_p12_model")
  model_file=a.out/"original-equations-mod31twelve.txt"
  rec["parameters"]["originalP12Model"]=model.generate(a.exact_gzip,files["integerModel"],model_file)
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
  f=PM*h.sub(Xi,range(315),[0]);basis15=h.join(U,f)
  check(basis15.rank()==15 and h.zero(h.solve_span(basis15,J*basis15)["residual"]),"same primitive original t2 line plus the complete root2 torsion")
  field_x=J-nmod_mat([[2*int(i==j) for j in range(315)] for i in range(315)],31)
  Wfield=h.join(PM*h.sub(Xi,range(315),range(1,9)),field_x*PM*Xi,field_x*field_x*PM*Xi)
  check(Wfield.ncols()==26 and h.zero(h.solve_span(basis15,Wfield)["residual"]),"all26 original targets lie in the same complete primitive line and true torsion")
  rec["parameters"]["primitiveRootTwoLine"]={"originalFreeTargetLabel":2,"matrix":field_record(f),
   "trueTorsionAndPrimitiveLineRank":15,"all26OriginalTargetClasses":field_record(Wfield),
   "full315SpanAndParameterActionVerified":True,"rootOneTorsionNotExcluded":True}
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
  def spec(name,labels,L,ring=2):
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
  def coordinates(name,D):
   solved=h.solve_span(basis15,D)
   check(solved["indices"]==list(range(15)) and h.zero(solved["residual"]),"complete primitive line and true torsion span "+name)
   C=solved["solution"];check(basis15*C==D,"all315 primitive-line coordinate products "+name)
   rec["parameters"]["coordinateChecks"][name]={"basis":field_record(basis15),"targets":field_record(D),
    "coordinates":field_record(C),"all315ProductsVerified":True,"residueOnlyDoesNotReplaceHighPAction":True}
   atomic_json(a.out/(name+"-coordinates.json"),{"binding":binding,"coordinates":rows(C)})
   save();return h.sub(C,range(14),range(C.ncols())),h.sub(C,[14],range(C.ncols()))
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
    if edges:out.append(family(files[key],labels,edges))
   return out

  labels=list(range(41001,41027));nt=26
  initial_weights=[[[] for _ in labels] for _ in range(9)]
  for j in range(1,9):initial_weights[j][j-1]=[1]
  for j in range(9):initial_weights[j][8+j]=[0,1];initial_weights[j][17+j]=[0,0,1]
  free_digits=[];torsion_digits=[];free_coefficients=[0]*nt
  def current_target(name):
   weights=[[p[:] for p in row] for row in initial_weights]
   for j,c in enumerate(free_coefficients):
    if c:
     if not weights[0][j]:weights[0][j]=[0]
     weights[0][j][0]-=c
   return target(name,labels,weights)
  target_file=current_target("digit0-original-targets")
  current=integer("digit0-actual-raw-target",labels,30,6,30,6,target_file,[])
  for k,L in enumerate(DIGIT_PRECISIONS):
   tick();Dk=complete_class("digit%d-complete315"%k,labels,current)
   dk,ak=coordinates("digit%d-complete-line-coordinates"%k,Dk)
   torsion_digits.append(rows(dk));free_digits.append(rows(ak)[0])
   for j in range(nt):free_coefficients[j]=(free_coefficients[j]+31**k*int(ak[0,j]))%(31**6)
   # This last complete quotient identity suffices for the existence of q5,r6:
   # six torsion digits are exact because p^6 T=0. No free tail is set to zero.
   if k==5:break
   target_file=current_target("digit%d-free-corrected-targets"%k)
   families=[family(source_of(current),labels,b.identity_edges(nt))]
   families+=true_correction(dk,6+k,L)
   corrected=integer("digit%d-subtract-true-coordinate-classes"%k,labels,L,6+k,L,6,target_file,families)
   check(h.zero(complete_class("digit%d-complete-zero-class"%k,labels,corrected)),"complete field obstruction vanishes after both original corrections")
   q=solve_source("digit%d-q"%k,labels,L,corrected)
   current=integer("digit%d-next-original-carry"%(k+1),labels,L,7+k,L-5,6,target_file,
    [family(source_of(corrected),labels,b.identity_edges(nt)),family(q,labels,b.identity_edges(nt,31**(6+k)))])
  mod=31**6
  A=[[sum(31**k*torsion_digits[k][i][j] for k in range(6))%(31**e) for j in range(nt)] for i,e in enumerate(E)]
  c0=[1]+free_coefficients[:8];c1=free_coefficients[8:17];c2=free_coefficients[17:26]
  beta=c1[0]
  check(beta%31==0 and c1==[beta*c%mod for c in c0] and c2==[beta*beta*c%mod for c in c0],"all nine original free coordinates have the same actual Hensel action")
  from math import comb
  ht=[sum(hs[d]*comb(d,k)*2**(d-k) for d in range(k,len(hs)))%mod for k in range(len(hs))]
  check(sum(ht[k]*pow(beta,k,mod) for k in range(len(ht)))%mod==0 and ht[1]%31!=0,
    "exact original hstar has the unique simple root-two Hensel root with these six digits")
  check(all(A[i][j]%31==torsion_digits[0][i][j] for i in range(14) for j in range(nt)),"actual first complete residue coordinates retained")
  Af=nmod_mat([[x%31 for x in row] for row in A],31)
  cf=nmod_mat([[x%31 for x in free_coefficients]],31)
  check(U*Af+f*cf==Wfield,"all8190 original target/free/torsion residue products")
  coordinates_data={"format":"r150-original-joint-m-root-two-complete-six-digit-coordinates-v1","binding":binding,
   "basisOriginalTrue16Indices":chosen,"ambientExponents":E,"coordinateRows":A,"freeCoefficientsModuloP6":free_coefficients,
   "torsionDigits":torsion_digits,"freeDigits":free_digits,"betaModuloP6":beta,"freeRemainderNotSetToZero":True,
   "lastComplete315IdentityGivesFormalRemainderExistence":True,"rootTwoCompletionOnly":True}
  coordinate_file=a.out/"root-two-complete-six-digit-coordinates.json";atomic_json(coordinate_file,coordinates_data)
  rec["parameters"]["completeCoordinates"]={"file":coordinate_file.name,**identity(coordinate_file),"matrix":integer_record(A),
   "actualOriginal26Targets":nt,"allSixComplete315DigitsVerified":True,"allFiveTrueIntegerCarriesVerified":True,
   "all30StableParentCoefficientsRequired":True,"p12ProductsRecomputedFromOriginalPrimitive":True,
   "higherFreeTailRetained":True,"completeTorsionCoordinatesFollowFromPrimitiveLineAndP6TZero":True}
  if a.through=="coordinates":rec["status"]="completed-coordinates";save();return 0
  image=group_image(A,E)
  Z=[[31**(6-e)*x%mod for x in row] for e,row in zip(E,A)]
  sn=smith_mod(Z,6);r=len(sn["valuations"])
  relation_powers=[6-v for v in sn["valuations"]]+[0]*(nt-r)
  Rels=[[sn["right"][i][j]*31**relation_powers[j] for j in range(nt)] for i in range(nt)]
  check(null_image(mm(A,Rels,mod),E),"all original complete D relations for the26 torsion generators")
  relation_smith=smith_mod(Rels,6)
  # Rels is the actual unreduced integral lift V diag(p^relation_powers),
  # including any p^6 columns that become zero in the modular Smith table.
  # In all cases this column lattice
  # contains p^6D^26 since V is a D unit, and is the exact preimage of ker(Z).
  check(sum(relation_powers)==image["length"],"complete relation-lattice length equals the independently computed original image length")
  X=[[0]*nt for _ in range(nt)]
  u=[[int(i==8)] for i in range(nt)]
  for j in range(1,9):X[8+j][j-1]=1;X[8][j-1]=(X[8][j-1]-c0[j])%mod
  for j in range(9):
   X[17+j][8+j]=1;X[8][8+j]=(X[8][8+j]-beta*c0[j])%mod
   X[17+j][17+j]=beta;X[8][17+j]=(X[8][17+j]-beta*beta*c0[j])%mod
  check(null_image(mm(mm(A,X,mod),Rels,mod),E),"original parameter action preserves every complete D relation")
  X2=mm(X,X,mod);X3=mm(X2,X,mod)
  check(null_image(mm(A,add(X3,[[-beta*z%mod for z in row] for row in X2],mod),mod),E),"exact x^2(x-beta) relation on all original torsion generators")
  q=[0]*(len(ht)-1);q[-1]=ht[-1]
  for i in range(len(q)-2,-1,-1):q[i]=(ht[i+1]+beta*q[i+1])%mod
  check((ht[0]+beta*q[0])%mod==0,"complete synthetic division of the original hstar at its actual Hensel root")
  hX=matrix_poly(ht,X,mod);qX=matrix_poly(q,X,mod);bfree=mm(qX,u,mod)
  Bgen=[[0]*9 for _ in range(nt)]
  for i in range(nt):
   for j in range(9):Bgen[i][j]=(c0[j]*bfree[i][0]+(hX[i][j-1] if j else 0))%mod
  Bcoords=reduce_rows(mm(A,Bgen,mod),E)
  BXcoords=reduce_rows(mm(mm(A,X,mod),Bgen,mod),E)
  Bimage=group_image(joined(Bcoords,BXcoords),E);BX=group_image(BXcoords,E)
  BPX=group_image(scaled(BXcoords,31,E),E)
  check(Bimage["exponents"]==[1,1,1,1,1,1,2,3,4,4,5] and Bimage["length"]==24 and BX["exponents"]==[1,1,1,2] and BPX["exponents"]==[1],
        "independent complete original joint-B type and parameter images are reproduced from the new raw targets")
  check(null_image(mm(A,mm(X2,Bgen,mod),mod),E),"all original x^2hstar target classes vanish")
  relf=nmod_mat([[x%31 for x in row] for row in Rels],31)
  xf=nmod_mat([[x%31 for x in row] for row in X],31);uf=nmod_mat(u,31)
  s_min=nt-h.join(relf,xf).rank()
  m_min=1+nt-h.join(relf,xf,uf).rank()
  check(s_min<=nt and 8<=m_min<=9,"original eight-to-nine joint-M generator interval is respected")
  sx=group_image(reduce_rows(mm(A,X,mod),E),E)
  px=group_image(scaled(reduce_rows(mm(A,X,mod),E),31,E),E)
  final_data={"format":"r150-original-joint-m-root-two-D-presentation-and-action-v1","binding":binding,
   "ambientExponents":E,"basisOriginalTrue16Indices":chosen,"original26TargetDefinitions":{"rawLabels":list(range(3,11)),"xLabels":LABEL9,"xSquaredLabels":LABEL9},
   "coordinateRows":A,"completeDRelationMatrix":Rels,"relationLatticeRightUnit":sn["right"],"relationPowers":relation_powers,
   "xActionOnOriginal26Generators":X,"xOfPrimitiveFreeGeneratorTorsionColumn":u,"betaModuloP6":beta,
   "freeActionIsTheExactSimpleHenselRootNotAZeroPaddedRepresentative":True,
   "originalNineHstarCoordinates":Bcoords,"freeCoefficientDigits":free_coefficients,
   "completeSmallSmithTransformation":sn,"relationSmithModuloP6":relation_smith}
  datafile=a.out/"root-two-complete-presentation-and-action.json";atomic_json(datafile,final_data)
  rec["parameters"]["final"]={"completeRootTwoCoefficientTorsion":image,"xImage":sx,"pxImage":px,
   "minimumRootTwoPolynomialGeneratorsOfTorsion":s_min,"minimumRootTwoPolynomialGeneratorsOfOriginalM":m_min,
   "minimumGlobalPolynomialGeneratorsOfOriginalM":m_min,
   "otherMaximalGeneratorCountsBoundedByThree":True,"fullGlobalCoefficientTorsionStillNeedsRootOneSocleCheck":True,
   "rootOneHiddenSocleNotDiscarded":True,"originalJointBReproduced":Bimage,"originalJointBXReproduced":BX,
   "originalJointBPXReproduced":BPX,"completeDRelations":integer_record(Rels),"originalXAction":integer_record(X),
   "allOriginalRelationProductsVerified":True,"allOriginalParameterTransportsVerified":True,
   "completeSixDigitCoordinates":rec["parameters"]["completeCoordinates"],
   "temporaryCompleteDataFile":{"file":datafile.name,**identity(datafile)},
   "noHighPActionInferredFromResidueJ16":True,"noParentAProductZeroPadding":True,
   "primitiveFreeTailNotSetToZero":True,"complete210NotRecomputed":True,"globalPolynomialSourceClaimed":False}
  rec["status"]="completed";save();return 0
 except (BudgetStop,subprocess.TimeoutExpired) as exc:
  rec["status"]="budget-checkpoint";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);save();return 75
 except BaseException as exc:
  rec["status"]="failed";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);rec["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)};save();return 1
 finally:
  save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
if __name__=="__main__":raise SystemExit(main())

