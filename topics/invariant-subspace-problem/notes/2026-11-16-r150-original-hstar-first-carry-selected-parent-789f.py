#!/usr/bin/env python3
"""One genuine coefficient carry for the nine original hstar targets.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
Uses the separately rebuilt 8 -> 7 -> 3 -> 1 true sources in one fresh basis.
The completed full210 E6 theorem is a prior result, not recomputed here.
All mathematical arrays and cochains remain temporary. No network operations.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,itertools,json,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
BASE_NAME="2026-11-16-r150-original-true16-selected-source-rebuild-789f.py"
BASE_SHA="381713af3c7d44ed496b0486650cf44e472ec3e21a00907b4da0722d4532cafb"
INTEGER_NAME="2026-11-16-r150-original-hstar-first-carry-integer-p7-789f.cpp"
INTEGER_SHA="ed2f42b3df51efa8fe0855c2a174caad2036f18c68f66bbf36c8b8b0456dbe55"
FORMAT="r150-original-hstar-first-carry-selected-parent-v1"
P7=27512614111
LABELS=list(range(2,11))
PARENT_READER_NAME="2026-11-16-r150-original-selected-true16-parent-reader-789f.py"
PARENT_READER_SHA="1c7152a767eac8d72f650c14c36416216537586c369ba4c45b26003ea9dec2d9"
EXP=[1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6]
class BudgetStop(Exception):pass
class StageFailure(Exception):pass
def check(ok,message):
 if not ok:raise ValueError(message)
def digest(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  while True:
   x=f.read(1048576)
   if not x:break
   h.update(x)
 return {"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)+"\n").encode("ascii")
def atomic(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
def atomic_json(p,x):atomic(p,canonical(x))
def load_module(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def pinned(p,size,sha,label):
 r=identity(p);check(r=={"bytes":size,"sha256":sha},"exact "+label);return r
def join_rows(*M):return [[int(A[i,j]) for A in M for j in range(A.ncols())] for i in range(M[0].nrows())]
def main():
 ap=argparse.ArgumentParser()
 for name in ("notes-root","parent-out","original-input-dir","small-input-dir","true-source-dir","exact-gzip","jet-map-dir","recipe","out"):
  ap.add_argument("--"+name,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=1800)
 ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--through",choices=("prepared","final"),default="final")
 a=ap.parse_args();check(0<a.seconds<=1800 and 1024<=a.memory_mib<=6144,"bounded original hstar execution")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();deadline=start+a.seconds
 rec={"format":FORMAT,"status":"running","parameters":{"prime":31,"modulus":P7,"targetLabels":LABELS,
  "originalSourceRows":6188,"originalOutputRows":4367,"parentCompletedExponent":6,
  "formalPrecisionChain":[25,20],"stages":{},"classes":{},"spanIdentities":{},"largeArraysTemporaryOnly":True}}
 outrec=a.out/"original-hstar-first-carry-receipt.json"
 def save():
  rec["elapsedSeconds"]=time.monotonic()-start;atomic_json(outrec,rec)
 def tick():
  if time.monotonic()>=deadline-2:raise BudgetStop("shared hstar first-carry clock")
 def stop(signum,frame):raise BudgetStop("signal "+str(signum))
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 logs=a.out/"logs";logs.mkdir(exist_ok=True);cache=a.out/"stage-cache";cache.mkdir(exist_ok=True)
 try:
  base_path=a.notes_root/BASE_NAME;pinned(base_path,36918,BASE_SHA,"minimal selected true16 rebuilding source")
  b=load_module(base_path,"r150_complete210_frozen_support")
  source_records={BASE_NAME:identity(base_path),INTEGER_NAME:pinned(a.notes_root/INTEGER_NAME,21734,INTEGER_SHA,"new original-target native")}
  for name,sha in b.SOURCES.items():
   r=identity(a.notes_root/name);check(r["sha256"]==sha,"frozen original helper "+name);source_records[name]=r
  reader_path=a.notes_root/PARENT_READER_NAME
  source_records[PARENT_READER_NAME]=pinned(reader_path,7512,PARENT_READER_SHA,"fresh-parent identity reader")
  parent_reader=load_module(reader_path,"r150_selected_true16_parent_reader")
  self_record=identity(Path(__file__))
  inputs={};files={}
  for key,d in b.ORIGINAL.items():
   p=a.original_input_dir/d["name"];files[key]=p;inputs[key]=pinned(p,d["bytes"],d["sha256"],key)
  for key,(name,size,sha) in b.FAMILIES.items():
   p=a.true_source_dir/name;files[key]=p;inputs[key]=pinned(p,size,sha,key)
  small={}
  for name,(size,sha) in b.SMALL.items():
   p=a.small_input_dir/name;small[name]=p;inputs[name]=pinned(p,size,sha,name)
  inputs["exactPrimitive"]=pinned(a.exact_gzip,*b.EXACT_PIN,"original primitive equations")
  mp=a.jet_map_dir/"jet-quotient-map.bin";mrp=a.jet_map_dir/"jet-quotient-map-receipt.json"
  inputs["jetMap"]=pinned(mp,*b.MAP_PIN,"full jet quotient map")
  inputs["jetMapReceipt"]=pinned(mrp,*b.MAP_RECEIPT_PIN,"full jet quotient map receipt")
  packed=a.recipe.read_bytes();raw=gzip.decompress(packed)
  check(len(raw)==b.RECIPE_PAYLOAD_BYTES and digest(raw)==b.RECIPE_PAYLOAD_SHA,"same complete210 recipe payload")
  recipe=json.loads(raw);check(recipe["binding"]==b.RECIPE_BINDING,"same complete210 recipe scope")
  inputs["recipePayload"]={"bytes":len(raw),"sha256":digest(raw)}
  PARENT,parent_pack,parent_classes,parent_pins=parent_reader.load_parent(a.parent_out,a.notes_root,inputs,source_records)
  inputs.update(parent_pins)
  semantic={"format":FORMAT,"driver":self_record,"sources":source_records,"inputs":inputs,
   "parentBinding":PARENT["binding"],"target":"original hstar binomial squares","targetLabels":LABELS,
   "precisionChain":[25,20],"chosenL6Index":12,"trueGeneratorExponents":[1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6]}
  binding=digest(canonical(semantic));rec["binding"]=binding;rec["parameters"]["inputIdentity"]=semantic
  bindfile=a.out/"binding.json"
  if bindfile.exists():check(json.loads(bindfile.read_text())=={"binding":binding,"semantic":semantic},"same complete socle continuation")
  else:atomic_json(bindfile,{"binding":binding,"semantic":semantic})
  save()
  from flint import nmod_mat
  h=load_module(a.notes_root/"2026-11-14-r150-ninth-first-matrices-789f.py","r150_socle_paid_matrix_helper")
  reader=load_module(a.notes_root/"2026-11-14-r150-torsion-characteristic-789f.py","r150_socle_paid_state_reader")
  state=reader.load_state(files["state"]);J=nmod_mat(state["matrices"]["action"],31)
  K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose()
  O=nmod_mat(state["observabilityEchelon"],31);Astate=nmod_mat(state["matrices"]["A"],31)
  pr=json.loads(small["second-prepared-receipt.json"].read_text())
  pb=b.read_system(small["second-prepared-system.bin.gz"],pr,b"R150SP2A")
  PM=h.block(pb,pr,"whole315PrimaryProjector");B=h.block(pb,pr,"globalTwoPrimaryBasis");Li=h.block(pb,pr,"localTwoPrimaryLeftInverse")
  map_raw=mp.read_bytes();map_rec=json.loads(mrp.read_text());maps={k:h.block(map_raw,map_rec,k) for k in map_rec["matrices"]}
  def parent_class(key):
   d=parent_classes[key];M=nmod_mat(d["matrixRows"],31)
   check(d["binding"]==PARENT["binding"] and b.matrix_record(M)==parent_pack["classes"][key]["matrix"],
         "actual fresh parent whole315 class "+key)
   return M
  D3=parent_class("L3");D4=parent_class("L4");D5=parent_class("L5");D6=parent_class("L6")
  U13=nmod_mat(recipe["true13Full315"],31)
  check(h.sub(U13,range(315),[8])==h.sub(D3,range(315),[0]),"true L3 K2 source coordinate")
  check(h.sub(U13,range(315),range(9,13))==h.sub(D4,range(315),range(4)),"true four L4 source sections")
  U15=nmod_mat(join_rows(U13,h.sub(D5,range(315),[0,1])),31)
  U16=nmod_mat(join_rows(U15,h.sub(D6,range(315),[0])),31)
  check(b.matrix_record(U16)["sha256"]==parent_reader.U16_SHA,"same paid true16 residue coordinates")
  old15=nmod_mat(recipe["futureCompleteIncoming15Full315"],31)
  check(U13.rank()==13 and U15.rank()==15 and U16.rank()==16 and h.join(U15,old15).rank()==15,
        "complete source-compatible true13/15/16; canonical13 not misused")
  for U in (U13,U15,U16):check(h.zero(h.solve_span(U,J*U)["residual"]),"whole parameter-invariant true source flag")
  rec["parameters"]["trueBasisIdentities"]={"true13":b.matrix_record(U13),"true15":b.matrix_record(U15),"true16":b.matrix_record(U16),
   "all315SourceSectionComparisons":True,"sameCompleteIncoming15Span":True}
  selected=a.out/"selected-parent";selected.mkdir(exist_ok=True)
  # Only explicit source-header transport is permitted. Every parent payload is pinned above.
  transports={}
  for key,offset,shape in (("G",24,(31,1034,1021,25)),("V",28,(31,1034,1021,2195,25))):
   d=PARENT[key];raw=(a.parent_out/d["path"]).read_bytes()
   check(raw[:8]==(b"R150SG31" if key=="G" else b"R150SV31") and struct.unpack_from("<"+"I"*len(shape),raw,8)==shape,
         "exact parent "+key+" cache schema")
   check(raw[offset:offset+64]==PARENT["binding"].encode("ascii"),"exact parent "+key+" cache binding")
   changed=raw[:offset]+binding.encode("ascii")+raw[offset+64:]
   check(changed[:offset]==raw[:offset] and changed[offset+64:]==raw[offset+64:],"only declared64 binding bytes change")
   p=selected/("actual-"+key+"-root2.bin")
   if p.exists():check(p.read_bytes()==changed,"unchanged restored "+key+" payload")
   else:atomic(p,changed)
   files[key]=p;transports[key]={"parent":inputs["parent-"+key],"child":identity(p),
    "headerBindingOffset":offset,"allMathematicalPayloadBytesIdentical":True,"payloadSHA256":digest(raw[offset+64:])}
  rec["parameters"]["explicitParentTransports"]=transports
  model_py=load_module(a.notes_root/(b.STEM+"original-model-p7-789f.py"),"r150_socle_original_model")
  p7model=a.out/"original-equations-mod31seven.txt"
  rec["parameters"]["originalP7Model"]=model_py.generate(a.exact_gzip,files["integerModel"],p7model)
  exact=json.loads(gzip.decompress(a.exact_gzip.read_bytes()));h0=list(map(int,exact["h0"]))
  def polynomial_product(a,b):
   c=[0]*(len(a)+len(b)-1)
   for i,x in enumerate(a):
    for j,y in enumerate(b):c[i+j]+=x*y
   return c
  fp=[-8,32,-25,5];fm=[864,864,135,5];e8=[9600,-25472,-3392,15936,-2888,-936,153,50,5]
  hs=polynomial_product([0,0,0,1],polynomial_product(polynomial_product(fp,fp),polynomial_product(polynomial_product(fm,fm),e8)))
  check(len(hs)==24 and hs[-1]==3125 and polynomial_product([-2,1],hs)==h0,
        "all original integer h0=(s-2)hstar coefficients")
  Xi=nmod_mat(state["matrices"]["targetCoordinates"],31).transpose()
  Targets=nmod_mat(state["matrices"]["targets"],31).transpose()
  check(K*Xi==Targets and Astate*K==K*J and h.zero(O*Targets),"whole original nine target dictionary/action/free checks")
  Hstar=nmod_mat(315,9,31)
  for c in reversed(hs):Hstar=J*Hstar+Xi*(c%31)
  initial_solution=h.solve_span(U16,Hstar)
  check(initial_solution["indices"]==list(range(16)) and h.zero(initial_solution["residual"]),
        "all original hstar classes belong to the complete true16 residue basis")
  C0=initial_solution["solution"]
  check(U16*C0==Hstar and h.zero(h.sub(C0,range(7,16),range(9))),
        "fresh complete315 original hstar classes, all initial directions in U7")
  atomic_json(a.out/"fresh-initial-hstar-coordinates.json",{"binding":binding,"coordinates":b.matrix_rows(C0),
    "originalHStarIntegerCoefficients":hs,"classes":b.matrix_record(Hstar)})
  C7=h.sub(C0,range(7),range(9))
  rec["parameters"]["initialClassesVerified"]={"all24IntegerHStarCoefficients":True,"all25HZeroReconstruction":True,
   "all7380OriginalTargetProducts":True,"all258300ActionProducts":True,"all4545FreeObservations":True,
   "all2835U16Products":True,"actualU7Coordinates":b.matrix_record(C7)}
  targetfile=a.out/"original-hstar-targets-mod31seven.txt"
  target_text="R150_ORIGINAL_HSTAR_SQUARE_TARGETS_P7_V1 31 %d 24 9\n%s\n%s\n"%(P7," ".join(str(x%P7) for x in hs)," ".join(map(str,LABELS)))
  atomic(targetfile,target_text.encode("ascii"));rec["parameters"]["originalTargetModel"]=identity(targetfile)
  save()
  if a.through=="prepared":rec["status"]="completed-prefix";save();return 0
  binaries=a.out/"bin";binaries.mkdir(exist_ok=True);programs={}
  native={**b.NATIVE,"integer":INTEGER_NAME}
  for key,name in native.items():
   tick();exe=binaries/key;meta=binaries/(key+".json")
   ckey=digest(canonical({"source":source_records[name],"headers":{k:v for k,v in source_records.items() if k.endswith(".hpp")},"flags":["g++","-O3","-std=c++17"]}))
   if not (exe.exists() and meta.exists() and json.loads(meta.read_text())=={"binding":ckey,"executable":identity(exe)}):
    with (logs/("compile-"+key+".log")).open("wb") as log:
     q=subprocess.run(["g++","-O3","-std=c++17","-I",str(a.notes_root),str(a.notes_root/name),"-o",str(exe)],
       stdout=log,stderr=subprocess.STDOUT,timeout=min(45,max(1,deadline-time.monotonic()-2)))
    check(q.returncode==0,"native compilation "+key);atomic_json(meta,{"binding":ckey,"executable":identity(exe)})
   programs[key]=[str(exe)]
  programs["solve"]=[sys.executable,str(a.notes_root/(b.STEM+"local-unit-solve-789f.py"))]
  def prefix(name):
   p=a.out/"stages"/name;p.mkdir(parents=True,exist_ok=True);return p/name
  def run(name,program,args,marker,gates,stage_inputs,outputs,logic):
   tick();source=native[program] if program in native else b.STEM+"local-unit-solve-789f.py"
   key=digest(canonical({"pipeline":binding,"source":source_records[source],"inputs":[identity(p) for p in stage_inputs],"logic":logic}))
   cp=cache/(name+".json");context=cache/(name+".context.json")
   if context.exists():check(json.loads(context.read_text())=={"inputBinding":key},"same partial socle stage")
   else:atomic_json(context,{"inputBinding":key})
   if cp.exists():
    old=json.loads(cp.read_text());check(old["inputBinding"]==key,"same completed socle stage")
    check(all(identity(p)==old["outputs"].get(str(p.relative_to(a.out))) for p in outputs),"completed socle outputs unchanged")
    rec["parameters"]["stages"][name]={"status":"completed","reused":True,"inputBinding":key,"statistics":old["statistics"]};save();return
   remain=deadline-time.monotonic()-1
   if remain<3:raise BudgetStop("before "+name)
   argv=[str(max(.1,remain-1)) if str(x)=="__REMAINING__" else str(x) for x in args]
   command=["timeout","--kill-after=10s",str(remain)+"s","prlimit","--as="+str(a.memory_mib*1048576),"--core=0","--"]+programs[program]+argv
   stage={"status":"running","inputBinding":key};rec["parameters"]["stages"][name]=stage;save();beg=time.monotonic();last={}
   logpath=logs/(name+".log")
   with logpath.open("w") as log:
    proc=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
    for line in proc.stdout:
     log.write(line);log.flush()
     try:event=json.loads(line)
     except ValueError:continue
     if isinstance(event,dict):
      last=event
      if event.get("status") or "completedOriginalRows" in event:print(json.dumps({"stage":name,**event},separators=(",",":")),flush=True)
    code=proc.wait()
   stage.update(exitCode=code,elapsedSeconds=time.monotonic()-beg,statistics=last,log=identity(logpath))
   if code in (75,124,-15):
    stage["status"]="budget-checkpoint";save();raise BudgetStop(name)
   if not (code==0 and last.get("status")==marker and all(last.get(k)==v for k,v in gates.items()) and all(p.is_file() for p in outputs)):
    stage["status"]="failed";stage["logTail"]=logpath.read_text(errors="replace")[-6000:];save();raise StageFailure(name)
   stage["status"]="completed";atomic_json(cp,{"inputBinding":key,"statistics":last,"outputs":{str(p.relative_to(a.out)):identity(p) for p in outputs}});save()
  specs=a.out/"specs";specs.mkdir(exist_ok=True)
  def spec(name,L,ring=2):
   p=specs/(name+".spec");b.write_spec(p,LABELS,L,ring);return p
  s25=spec("nine-original-hstar-targets-25",25)
  def integer(name,s,L,exponent,retained,power,families):
   p=prefix(name);mix=p.parent/(name+".mix");logic,inf=b.write_mix(mix,LABELS,L,[exponent]*9,families)
   run(name,"integer",[files["model"],p7model,s,mix,p,binding,retained,"__REMAINING__",targetfile,power],
       "original-hstar-first-carry-integer-p7-jets-complete",
       {"allOriginal17CoefficientsDivisible":True,"targetCount":9,"computedTaylorPrecision":L,"retainedFormalPrecision":retained,
        "targetScalarPower":power,"sameOriginalHStarAndAllNineSquaresVerified":True,"residualIsTargetMinusOriginalAProduct":True},
       [files["model"],p7model,s,targetfile]+inf,
       [b.suffix(p,x) for x in ("-original6188-integer-jets.bin","-divided-original-jets.bin","-field-root2-jets.bin","-field-projected-crt8-jets.bin","-integer-product.json")],
       {"targetPower":power,"divisorExponent":exponent,"retained":retained,"families":logic})
   return p
  def normal(name,s,field,crt=False):
   p=prefix(name)
   run(name,"normal",[files["model"],field,files["graph"],s,p,binding],
       "saturated-runtime-two-ring-state-complete" if crt else "saturated-runtime-root2-normal-form-complete",{},
       [files["model"],field,files["graph"],s],
       [b.suffix(p,x) for x in ("-standard-state.bin" if crt else "-original1034-root2.bin","-local-prebasis-source-jets.bin","-local-normal.json")],{"CRT8":crt})
   return p
  def complete_class(name,integer_output):
   s=spec(name+"-CRT8",8,12);p=normal(name,s,b.suffix(integer_output,"-field-projected-crt8-jets.bin"),True)
   raw=b.suffix(p,"-standard-state.bin").read_bytes()
   check(raw[:8]==b"R150SE31" and struct.unpack_from("<4I",raw,8)==(31,820,9,8),"all820 target state")
   check(list(struct.unpack_from("<9H",raw,24))==LABELS,"all nine original target labels")
   offset=42;coords=[list(struct.unpack_from("<HB",raw,offset+3*i)) for i in range(820)];offset+=2460
   check(coords==map_rec["standardCoordinates"] and len(raw)==offset+820*9,"same820 state dictionary and EOF")
   E=nmod_mat(820,9,list(raw[offset:]),31);Y=maps["Pi"]*E;F=maps["freeChecks"]*Y;T39=maps["torsionCoordinates"]*Y
   check(h.zero(F) and maps["torsionEmbedding"]*T39==Y,"all104 local free observations and exact39 reconstruction")
   D=B*Li*h.sub(T39,pr["localTwoPrimaryPivotRows"],range(9))
   check(maps["globalTorsionTo39"]*D==T39 and PM*D==D,"all315 original root2 coordinates")
   V=K*D;check(h.zero(O*V) and Astate*V==K*(J*D),"all505 original global observations and original s action")
   item={"status":"completed","all104LocalFreeChecks":True,"all315OriginalCoordinateReconstruction":True,
    "all505GlobalFreeChecks":True,"sameOriginalSAction":True,"matrix":b.matrix_record(D)}
   atomic_json(p.parent/"complete315-class.json",{"binding":binding,**item,"matrixRows":b.matrix_rows(D)})
   rec["parameters"]["classes"][name]=item;save();return D
  def coordinates(name,U,D):
   z=h.solve_span(U,D)
   check(z["indices"]==list(range(U.ncols())) and h.zero(z["residual"]),"complete actual true-generator span "+name)
   C=z["solution"];check(U*C==D,"full315 exact coordinate identity")
   rec["parameters"]["spanIdentities"][name]={"status":"completed","basis":b.matrix_record(U),"targets":b.matrix_record(D),
      "coordinates":b.matrix_record(C),"all315ProductsVerified":True}
   atomic_json(a.out/(name+"-coordinates.json"),{"binding":binding,"coordinates":b.matrix_rows(C)})
   save();return C
  def solve_source(name,mode,s,integer_output):
   nf=normal(name+"-normal",s,b.suffix(integer_output,"-field-root2-jets.bin"))
   d=a.out/"stages"/(name+"-complete");d.mkdir(parents=True,exist_ok=True)
   run(name+"-complete","solve",["--G",files["G"],"--rhs",b.suffix(nf,"-original1034-root2.bin"),"--binding",binding,
       "--notes-root",a.notes_root,"--out",d,"--remaining-seconds","__REMAINING__"],
       "saturated-local-unit-solve-complete",{"fullOriginalGIdentityVerified":True,"all13FreeConditionsRetained":True},
       [files["G"],b.suffix(nf,"-original1034-root2.bin")],[d/"complete-G-q-root2.bin",d/"local-unit-solve-receipt.json"],
       {"originalRows":1034,"maximumSourcePrecisionLoss":5})
   v=prefix(name+"-vq")
   run(name+"-vq","vq",[files["model"],files["V"],d/"complete-G-q-root2.bin",files["oldK"],"-",v,binding,mode,s],
       "saturated-runtime-jet-VQ-complete",{"mode":mode},
       [files["model"],files["V"],d/"complete-G-q-root2.bin",files["oldK"],s],
       [b.suffix(v,"-original2195-source-jets.bin"),b.suffix(v,"-vq.json")],{"mode":mode})
   p=prefix(name+"-transport")
   run(name+"-transport","transport",[files["model"],files["oldK"],b.suffix(v,"-original2195-source-jets.bin"),files["normalTrace"],
       b.suffix(nf,"-local-prebasis-source-jets.bin"),files["forward"],files["backward"],p,binding,mode,"-",s,p.parent/"checkpoints","__REMAINING__"],
       "runtime-local-original-source-transport-complete",{"mode":mode},
       [files[k] for k in ("model","oldK","normalTrace","forward","backward")]+[b.suffix(v,"-original2195-source-jets.bin"),b.suffix(nf,"-local-prebasis-source-jets.bin"),s],
       [b.suffix(p,"-original6188-q-jets.bin"),b.suffix(p,"-transport.json")],{"mode":mode})
   return b.suffix(p,"-original6188-q-jets.bin")
  def true_u7_corrections(C):
   check(C.nrows()==7 and C.ncols()==9,"all seven actual global source directions")
   configs=[("kernels",[2275,2276,2277,2278],[(0,0,1),(1,1,1)]),
    ("fourK2",[4001,4002,4003,4004],[(j,j+2,2) for j in range(4)]),
    ("selectedK2",LABELS,[(0,6,2)])]
   return [b.family(files[key],labs,[[i,j,[31**(2-e)*int(C[row,j])]]
       for i,row,e in indices for j in range(9) if C[row,j]]) for key,labs,indices in configs]
  # S0=sum p^(2-e_i) kappa_i a_i is a genuine global original source.
  # Mod p the divided residual is zero in the full original quotient.
  S0=integer("hstar-u7-corrected-p2-25",s25,25,2,25,2,true_u7_corrections(C7))
  D0=complete_class("hstar-initial-zero-complete315",S0)
  check(h.zero(D0),"actual global U7 subtraction kills the entire root2 field class")
  q0=solve_source("hstar-q0","q3",s25,S0)
  # Positive sign: p^2*b-A(S0+p^2*q0) = p^3*r1.
  # The finite unit solution has all25 coefficients checked and20 stable formal coefficients.
  R1=integer("hstar-first-true-carry-25",s25,25,3,20,2,
    [b.family(b.suffix(S0,"-original6188-integer-jets.bin"),LABELS,b.identity_edges(9)),
     b.family(q0,LABELS,b.identity_edges(9,31**2))])
  D1=complete_class("hstar-first-carry-complete315",R1)
  C1=coordinates("hstar-first-carry-in-true16",U16,D1)
  rlow=[];rup=[];low=[];up=[]
  for j in range(9):
   rlow.append(max([0]+[EXP[i] for i in range(16) if C1[i,j]]))
   rup.append(max(EXP[i] if C1[i,j] else EXP[i]-1 for i in range(16)))
   # Root1 has exponent <=2; the whole target has already proved exponent >=2.
   # p^2*b=p^3*r1 in the root2 completion, without a fake global q0 claim.
   low.append(max(2,rlow[-1]-1));up.append(max(2,rup[-1]-1))
   check(low[-1]<=up[-1]<=5,"proved exact exponent interval after one genuine carry")
  orders=[lo if lo==hi else None for lo,hi in zip(low,up)]
  check(orders==[5]*9 and all(int(C1[15,j]) for j in range(9)),"fresh-basis control matches all nine paid exact-five orders")
  final={"binding":binding,"targetLabels":LABELS,"trueGeneratorExponents":EXP,
   "firstCarry":b.matrix_record(D1),"firstCarryCoordinates":b.matrix_record(C1),
   "firstCarryCoordinateRows":b.matrix_rows(C1),"firstCarryClassRank":D1.rank(),
   "firstCarryCoefficientOrderLowerBounds":rlow,"firstCarryCoefficientOrderUpperBounds":rup,
   "minimum31DenominatorLowerBounds":low,"minimum31DenominatorUpperBounds":up,"exactExponentsWhenClosed":orders,
   "allOriginal17IntegerProductsVerified":True,"all104LocalFreeChecks":True,"all505GlobalFreeChecks":True,
   "allComplete315SpanIdentitiesVerified":True,"allOriginalSourceCorrectionsRetained":True,
   "originalHStarNotHZero":True,"fullFormalPrecisionChain":[25,20],"stablePrecisionExceedsRequiredFive":True,
   "rootTwoFormalClassNotClaimedAsGlobalPolynomialSource":True,"rootOneExponentAtMostTwo":True,
   "allNineOriginalHZeroTargetsAlreadyExactTwo":True,"hiddenHigherPDigitsNotDiscarded":True,
   "exactConclusionUsesCompletedE6AndDirectSumTrueGenerators":True,"globalSourceArraysMaterialized":False}
  atomic_json(a.out/"complete-hstar-first-carry-result.json",final)
  rec["status"]="completed";rec["parameters"]["final"]=final;save();return 0
 except (BudgetStop,subprocess.TimeoutExpired) as exc:
  rec["status"]="budget-checkpoint";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);save();return 75
 except BaseException as exc:
  rec["status"]="failed";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);save();return 1
 finally:
  save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
if __name__=="__main__":raise SystemExit(main())
