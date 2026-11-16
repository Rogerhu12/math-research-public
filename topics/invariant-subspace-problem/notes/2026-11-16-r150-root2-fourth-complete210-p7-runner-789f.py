#!/usr/bin/env python3
"""Complete210 genuine fourth-page sources for the original root2 B-module.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.

All197/204/208/210 sources and the six field-zero recipes are carried in integers.
The prior two-probe classes are recomputed and checked, never treated as a full page.
All arrays and checkpoints remain temporary. No network operations.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,math,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
from math import comb
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
P=31
P7=27512614111
FORMAT="r150-root2-fourth-complete210-original-p7-v1"
STEM="2026-11-16-r150-root2-fourth-"
ORIGINAL={"model":{"name":"model.txt","bytes":128145,"sha256":"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"},"graph":{"name":"graph.bin","bytes":101365853,"sha256":"bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce"},"normalTrace":{"name":"normalTrace.bin","bytes":101244784,"sha256":"e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b"},"forward":{"name":"forward.bin","bytes":2378937,"sha256":"66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e"},"backward":{"name":"backward.bin","bytes":3052119,"sha256":"cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f"},"oldK":{"name":"oldK.bin","bytes":48275717,"sha256":"ec067d86ce7c838697369d1f6a986c823de8564823d85b6684fe7a2926127a88"},"oldQ":{"name":"oldQ.bin","bytes":16649150,"sha256":"0bd81e4ae045daef1e224922ff0cceabd81436dc1680af29595ba2e169865338"},"oldTrace":{"name":"oldTrace.bin","bytes":113614260,"sha256":"85105ff9a84a81c05b88ee09d1f3a8de4bd9a1e7faf5657889c74e95f4f441ae"},"integerModel":{"name":"integerModel.txt","bytes":22824,"sha256":"2785c53d015d05db4550e1978c05db7d42009cfa8942e915541599a76d3701cc"},"state":{"name":"state.bin","bytes":1470456,"sha256":"06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"}}
SOURCES={"2026-11-16-r150-root2-fourth-local-common-789f.hpp":"beb0168cbbecbbc961482066961eb5bc36b241e311ee847f4a4d36a6851b7655","2026-11-16-r150-root2-fourth-local-vq-789f.cpp":"c0d233014dd71816f956021bd669ca3b9254768cc3186b920be2133cd27c19ae","2026-11-16-r150-root2-fourth-local-original-transport-789f.cpp":"00a1b72e02b09f20bac3115dc81ff77c4ce7c51efc52a987c8507bdd8159af48","2026-11-16-r150-root2-fourth-local-normal-789f.cpp":"9d070b6030538fa7c5b412b7ee00c819c7db68fa5c1f6ca2a9e9aeb00bd8dda0","2026-11-16-r150-root2-fourth-local-unit-solve-789f.py":"f4e5934b387d5800060b0aef77e41e627680e771eadb1dad890090a58de5f7f7","2026-11-16-r150-root2-fourth-integer-p7-jets-789f.cpp":"7623e3297d2cda154f1afdaddb4dc8cf00be29c98d6b131c6f2564827a4c6cd5","2026-11-16-r150-root2-fourth-original-model-p7-789f.py":"00deeeca38867d24043a6f842996e1e84116cfab03b36eb144ccff1928f5bf92","2026-11-14-r150-f31-bitplane-789f.hpp":"73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec","2026-11-14-r150-ninth-first-common-789f.hpp":"591dedf2c8a1d9d67fc644d21fae6e56ffc7ef8c840560831422197cbc5e9531","2026-11-14-r150-local-jet-unit-schur-helper-789f.py":"d31c917fe0aaa0e9008e5cb0a85cb81600b5a431fe691261948354fb1d1ee42b","2026-11-14-r150-ninth-first-matrices-789f.py":"3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a","2026-11-14-r150-torsion-characteristic-789f.py":"8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2","2026-11-15-r150-root2-fourth-complete210-source-preparation-789f.py":"105961c4d6f105dd16a3f70e5ce974c28c1e0e64534510e1af50370525c9fb51"}
SMALL={
 "second-prepared-receipt.json":(18840,"f8ffc939972363e79d0027946c5268c32f869e90adc6fead115fbd29b0ea1ca4"),
 "second-prepared-system.bin.gz":(42012,"691717421b0b7558f7ca053054c6c3f23bde5aa96fc93f36a744ad1171c4ba03"),
 "second-complete-receipt.json":(22107,"50e8aa0cecafc697b1d52a43792e095be35c4dadc71eff07b861569591d092b7"),
 "second-complete-system.bin.gz":(72934,"f20487d290193e738a5df67dccdf0c6d11c1c0b9e224dbd310fdc1a0180acaf7"),
 "third-complete-receipt.json":(17757,"3bb98210ccf8a7941f2a9a71c0d8d1a5fc8c0e11891c26d0e76d8079fa413619"),
 "third-complete-system.bin.gz":(70591,"786333a4baa562a15e38666a31207e3ce0179e03a0e9505da2d6a4cc5fbe7c2c")}
FAMILIES={
 "kernels":("kernels.bin",2200126,"c6ebd427d59033755a8f9852f64d7509f249727e05c0d62834537aa0a3bdbf7f"),
 "fourK2":("fourK2.bin",2236198,"653867bccc606ec234c65eacfbb014fe14e055fcd50f2ea3f2506344d2aad8c7"),
 "selectedK2":("selectedK2.bin",4700740,"5ab8223d69912ea5b102f71ad3439b3860594188386fce9b82f937944c90a554"),
 "newOriginal":("newOriginal.bin",17260416,"0258b6690b107a3cd45d9f6ace7ddb3003bb64ff1345ab0eab7ac4d650c49f34"),
 "currentK4":("currentK4.bin",7645286,"a5e16cfe2f6c6665c0806c488ea0ba3db11516e81be259c1f213126d9339566a")}
CURRENT_K4_RECEIPT_PIN=(1020,"22f1bc8d89f3a63b3ad4f40b18e598681d7ce08f5fe283f09b078c9fb5be762a")
PAID_PROBE={"run":43798780106,"job":133073660023,"sourceSHA256":"16ce81045e0c40ba875894ee926df138b7db0210efa5ce3fcf677b19eaabb01c",
 "binding":"bc5cbe06a37423f0dcd8ac48fc3495b4a082483153afd422fe0fa092f2428fea",
 "rawBytes":26380,"rawSHA256":"1ac76082fa32eecf1e8f0939515909efceb712056abf2f7acc059ee33eb397d4",
 "sourceLabels":[30209,30210],"whole315ClassSHA256":"f1a0d314fe738a42b8d72313fe11b3f89b870b5a196e3cd27886371a331c33c6",
 "quotientSHA256":"bd50e12c55dda3ee443c1cb6d71c7bcf6351c4ec96f7bc8d6adec015d1192eea"}
RECIPE_PAYLOAD_BYTES=709918
RECIPE_PAYLOAD_SHA="d4d486d0d1c6a33e091da3e99d58cb604d7b2ef828a84a20ba23edf76d19a63c"
RECIPE_BINDING="918f7a2c9663741bcb670bded5dff4b22a7a9b84d19e579faaad6501703a8b05"
MAP_PIN=(181038,"3f291285db5a6e97a5db977b3402dbdcc9f7b9e5fb8a48d31b0e219e89e71716")
MAP_RECEIPT_PIN=(34774,"5d3e09b26487355b32f20600764664def3dee0be34120e1c8202307eda5526df")
EXACT_PIN=(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe")
NATIVE={"vq":STEM+"local-vq-789f.cpp","transport":STEM+"local-original-transport-789f.cpp",
        "normal":STEM+"local-normal-789f.cpp","integer":STEM+"integer-p7-jets-789f.cpp"}
LABEL16=list(range(7001,7008))+list(range(2,11))
NEW198=list(range(15001,15199))
ALL204=[7001,7002,7005,7006,7007,7004]+NEW198
ALL208=list(range(20001,20209))
ALL210=list(range(30001,30211))
class BudgetStop(Exception):pass
class StageFailure(Exception):pass
def check(ok,text):
 if not ok:raise ValueError(text)
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)+"\n").encode("ascii")
def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha_file(path):
 h=hashlib.sha256()
 with path.open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   h.update(b)
 return h.hexdigest()
def record(path):return {"bytes":path.stat().st_size,"sha256":sha_file(path)}
def atomic(path,data):
 path.parent.mkdir(parents=True,exist_ok=True)
 tmp=path.with_name(path.name+".tmp");tmp.write_bytes(data);os.replace(tmp,path)
def atomic_json(path,x):atomic(path,canonical(x))
def pinned(path,pin,label):
 check(path.is_file() and path.stat().st_size==pin[0] and sha_file(path)==pin[1],"pinned "+label)
 return {"bytes":pin[0],"sha256":pin[1]}
def import_module(path,name):
 q=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(q);q.loader.exec_module(m);return m
def read_system(path,receipt,magic):
 raw=gzip.decompress(path.read_bytes());d=receipt["system"]
 check(len(raw)==d["uncompressedBytes"] and sha_bytes(raw)==d["uncompressedSHA256"] and raw[:8]==magic,"paid complete small matrix system")
 return raw
def suffix(path,ending):return Path(str(path)+ending)
def trim_integer(p):
 p=[int(x)%P7 for x in p]
 while p and not p[-1]:p.pop()
 return p
def taylor(p):
 return trim_integer([sum(int(p[d])*comb(d,k)*2**(d-k) for d in range(k,len(p)))%P7 for k in range(len(p))])
def matrix_rows(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def matrix_record(A):
 raw=bytes(x for row in matrix_rows(A) for x in row)
 return {"rows":A.nrows(),"columns":A.ncols(),"sha256":sha_bytes(raw)}
def write_spec(path,labels,L,ring=2):
 atomic(path,("R150_S2_LOCAL_JET_SPEC_V1\n31 %d %d %d\n%s\n"%(len(labels),L,ring," ".join(map(str,labels)))).encode("ascii"))
def family(path,labels,edges):
 return {"file":path,"labels":list(labels),"edges":[[i,j,trim_integer(p)] for i,j,p in edges if trim_integer(p)]}
def identity_edges(n,scale=1):return [[j,j,[scale]] for j in range(n)]
def write_mix(path,labels,L,exponents,families):
 active=[f for f in families if f["edges"]]
 check(active,"nonempty true integer source combination")
 lines=["R150_ROOT2_FOURTH_INTEGER_MIX_V1 %d %d %d"%(len(labels),L,len(active))," ".join(map(str,exponents))]
 semantic=[]
 for f in active:
  check(not any(c.isspace() for c in str(f["file"])),"source paths must not contain whitespace")
  lines.append("%s %d %d"%(f["file"],len(f["labels"]),len(f["edges"])))
  lines.append(" ".join(map(str,f["labels"])))
  for i,j,p in f["edges"]:lines.append("%d %d %d %s"%(i,j,len(p)," ".join(map(str,p))))
  semantic.append({"input":record(f["file"]),"labels":f["labels"],"edges":f["edges"]})
 atomic(path,("\n".join(lines)+"\n").encode("ascii"))
 return semantic,[f["file"] for f in active]
def main():
 ap=argparse.ArgumentParser()
 for name in ("notes-root","original-input-dir","small-input-dir","true-source-dir","exact-gzip","jet-map-dir","out"):
  ap.add_argument("--"+name,type=Path,required=True)
 ap.add_argument("--recipe",type=Path)
 ap.add_argument("--seconds",type=float,default=1800)
 ap.add_argument("--memory-mib",type=int,default=6144)
 ap.add_argument("--through",choices=("q1","l3","l4","l5","final"),default="final")
 a=ap.parse_args()
 check(0<a.seconds<=1800 and 1024<=a.memory_mib<=8192,"explicit bounded resource contract")
 a.out.mkdir(parents=True,exist_ok=True)
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 start=time.monotonic();deadline=start+a.seconds
 rec={"format":FORMAT,"status":"running","parameters":{"prime":31,"modulus":P7,
  "positiveProbeOnly":False,"all210CompleteImageComputed":False,"largeArraysTemporaryOnly":True,
  "priorTwoProbeIdentity":PAID_PROBE,"allSixFieldZeroRecipesRetained":True,
  "originalSourceRows":6188,"originalOutputRows":4367,"precisionChain":[25,20,15,10,5],
  "dependencySourceCounts":{"L3":197,"L4":204,"L5":208,"L6":210},
  "stages":{},"comparisons":{}}}
 receipt_path=a.out/"root2-fourth-complete210-receipt.json"
 def save():
  rec["elapsedSeconds"]=time.monotonic()-start;atomic_json(receipt_path,rec)
 def tick():
  if time.monotonic()>=deadline-2:raise BudgetStop("shared source-chain budget")
 def stop(signum,frame):raise BudgetStop("source-chain signal "+str(signum))
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 logs=a.out/"logs";logs.mkdir(exist_ok=True);checkpoints=a.out/"stage-cache";checkpoints.mkdir(exist_ok=True)
 try:
  files={};identities={}
  for k,d in ORIGINAL.items():
   files[k]=a.original_input_dir/d["name"];identities[k]=pinned(files[k],(d["bytes"],d["sha256"]),k);tick()
  small={}
  for name,pin in SMALL.items():
   small[name]=a.small_input_dir/name;identities[name]=pinned(small[name],pin,name)
  for key,(name,size,digest) in FAMILIES.items():
   files[key]=a.true_source_dir/name;identities[key]=pinned(files[key],(size,digest),key)
  current_receipt_path=a.true_source_dir/"currentK4-product.json"
  identities["currentK4Product"]=pinned(current_receipt_path,CURRENT_K4_RECEIPT_PIN,"paid original K4 product receipt")
  current_receipt=json.loads(current_receipt_path.read_bytes())
  check(current_receipt["status"]=="completed" and current_receipt["modulus"]==31**5
    and current_receipt["divisor"]==31**4 and current_receipt["originalRawRows"]==6188
    and current_receipt["originalComponents"]==4367 and current_receipt["targetLabels"]==list(range(7001,7008))
    and current_receipt["allOriginalProductCoefficientsDivisible"] is True and current_receipt["failedCoefficientCount"]==0,
    "all seven original K4 columns have paid global p4 divisibility")
  identities["exactPrimitive"]=pinned(a.exact_gzip,EXACT_PIN,"exact original primitive model")
  mp=a.jet_map_dir/"jet-quotient-map.bin";mrp=a.jet_map_dir/"jet-quotient-map-receipt.json"
  identities["jetMap"]=pinned(mp,MAP_PIN,"complete local quotient map")
  identities["jetMapReceipt"]=pinned(mrp,MAP_RECEIPT_PIN,"complete local quotient map receipt")
  source_records={}
  for name,digest in SOURCES.items():
   path=a.notes_root/name;check(path.is_file() and sha_file(path)==digest,"pinned mathematical source "+name)
   source_records[name]={"sha256":digest,"bytes":path.stat().st_size}
  self_record=record(Path(__file__))
  recipe_path=a.recipe or (a.out/"prepared210"/"complete210-fourth-source-recipes.json.gz")
  if not recipe_path.exists():
   tick();recipe_path.parent.mkdir(parents=True,exist_ok=True)
   args=[sys.executable,str(a.notes_root/"2026-11-15-r150-root2-fourth-complete210-source-preparation-789f.py")]
   for flag,name in [("second-prepared-receipt","second-prepared-receipt.json"),("second-prepared-system","second-prepared-system.bin.gz"),
    ("second-complete-receipt","second-complete-receipt.json"),("second-complete-system","second-complete-system.bin.gz"),
    ("third-complete-receipt","third-complete-receipt.json"),("third-complete-system","third-complete-system.bin.gz")]:
    args+=["--"+flag,str(small[name])]
   args+=["--state",str(files["state"]),"--reader",str(a.notes_root/"2026-11-14-r150-torsion-characteristic-789f.py"),
    "--helper",str(a.notes_root/"2026-11-14-r150-ninth-first-matrices-789f.py"),"--out",str(recipe_path.parent),
    "--seconds",str(min(60,max(1,deadline-time.monotonic()-5))),"--memory-mib","512"]
   with (logs/"rebuild-paid210.log").open("wb") as log:
    r=subprocess.run(args,stdout=log,stderr=subprocess.STDOUT,timeout=max(1,deadline-time.monotonic()-2))
   check(r.returncode==0 and recipe_path.is_file(),"actual reconstruction of complete210 recipes")
  packed=recipe_path.read_bytes();payload=gzip.decompress(packed)
  check(len(payload)==RECIPE_PAYLOAD_BYTES and sha_bytes(payload)==RECIPE_PAYLOAD_SHA,"same complete210 source recipe payload")
  recipe=json.loads(payload)
  check(recipe["format"]=="r150-root2-fourth-complete210-source-preparation-data-v1" and recipe["binding"]==RECIPE_BINDING,"paid210 scope binding")
  identities["recipePayload"]={"bytes":len(payload),"sha256":sha_bytes(payload)}
  semantic={"format":FORMAT,"sources":source_records,"driver":self_record,"inputs":identities,
    "completeOriginalKNumbers":list(range(2,199)),"completeOriginalL4Indices":list(range(204)),
    "completeOriginalL5Indices":list(range(208)),"completeOriginalF3Indices":list(range(210)),
    "priorTwoProbeIdentity":PAID_PROBE,"precisionChain":[25,20,15,10,5]}
  binding=sha_bytes(canonical(semantic));rec["binding"]=binding;rec["parameters"]["inputIdentity"]=semantic
  bindfile=a.out/"binding.json"
  if bindfile.exists():check(json.loads(bindfile.read_text())=={"binding":binding,"semantic":semantic},"same complete continuation binding")
  else:atomic_json(bindfile,{"binding":binding,"semantic":semantic})
  rec["parameters"]["recipeStoredIdentity"]=record(recipe_path);save()
  from flint import nmod_mat
  h=import_module(a.notes_root/"2026-11-14-r150-ninth-first-matrices-789f.py","r150_b4_positive_paid_h")
  reader=import_module(a.notes_root/"2026-11-14-r150-torsion-characteristic-789f.py","r150_b4_positive_paid_reader")
  state=reader.load_state(files["state"]);J=nmod_mat(state["matrices"]["action"],31)
  K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose()
  O=nmod_mat(state["observabilityEchelon"],31);Astate=nmod_mat(state["matrices"]["A"],31)
  check((state["stateDimension"],state["torsionDimension"],state["observabilityRank"])==(820,315,505),"same complete315/505 module")
  pr=json.loads(small["second-prepared-receipt.json"].read_text())
  sr=json.loads(small["second-complete-receipt.json"].read_text())
  tr=json.loads(small["third-complete-receipt.json"].read_text())
  for r in (pr,sr,tr):check(r["status"]=="completed","completed original B2/B3 parent")
  pb=read_system(small["second-prepared-system.bin.gz"],pr,b"R150SP2A")
  sb=read_system(small["second-complete-system.bin.gz"],sr,b"R150SS2A")
  tb=read_system(small["third-complete-system.bin.gz"],tr,b"R150SS3A")
  PM=h.block(pb,pr,"whole315PrimaryProjector");V10=h.block(pb,pr,"V10");C197=h.block(pb,pr,"trueV10Coordinates")
  D4old=h.block(sb,sr,"all204Projected315SecondColumns");D5old=h.block(tb,tr,"allProjected315ThirdColumns")
  B=h.block(pb,pr,"globalTwoPrimaryBasis");Li=h.block(pb,pr,"localTwoPrimaryLeftInverse")
  incoming=nmod_mat(recipe["futureCompleteIncoming15Full315"],31)
  Jin=nmod_mat(recipe["futureCompleteIncoming15SAction"],31)
  check(incoming.rank()==15 and J*incoming==incoming*Jin,"complete invariant incoming15")
  project,Jq,_,_,_,_=h.quotient(J,incoming)
  map_raw=mp.read_bytes();map_rec=json.loads(mrp.read_text())
  M={k:h.block(map_raw,map_rec,k) for k in map_rec["matrices"]}
  labels197=pr["sourceLabels197"];check(len(labels197)==197 and len(set(labels197))==197,"original197 source labels")
  labels3=labels197;labels4=ALL204;labels5=ALL208;labels6=ALL210
  F2=recipe["secondKernelGeneratorsInSAscending"];F3t=recipe["thirdKernelCanonicalIntegerTaylorMod31Seven"]
  check(recipe["sourceLabels204"]==ALL204 and recipe["sourceLabels208"]==ALL208 and recipe["sourceLabels210"]==ALL210,"all original generator labels")
  check(recipe["thirdImageSAction"]==[[2,0],[0,2]],"actual last two t-section recipes")
  for j in (208,209):
   nonzero=[i for i in range(208) if trim_integer(F3t[i][j])]
   check(nonzero==[10+j-208] and trim_integer(F3t[nonzero[0]][j])==[31,1],
         "canonical s+29 lift is31+t, never silently replaced by t")
  for j in (10,11):check(all(not F2[i][j] for i in range(204) if i not in range(6,12)),"minimal six true L4 dependencies")
  check(recipe["directZeroF3Indices"]==[10,11] and recipe["inheritedFieldZeroF2Indices"]==[6,7,8,9],
        "all six previously field-zero recipes are identified and retained")
  rec["parameters"]["canonicalF3LastLift"]=[31,1]
  rec["parameters"]["sixFieldZeroRecipeIndices"]=[6,7,8,9,10,11];save()
  build=a.out/"bin";build.mkdir(exist_ok=True);programs={}
  for key,name in NATIVE.items():
   tick();exe=build/key;meta=build/(key+".json");compile_key=sha_bytes(canonical({"source":source_records[name],
    "headers":{k:v for k,v in source_records.items() if k.endswith(".hpp")},"flags":["g++","-O3","-std=c++17"]}))
   valid=meta.exists() and exe.exists()
   if valid:
    old=json.loads(meta.read_text());valid=old.get("binding")==compile_key and old.get("executable")==record(exe)
   if not valid:
    timeout=min(45,max(1,deadline-time.monotonic()-2))
    with (logs/("compile-"+key+".log")).open("wb") as log:
     r=subprocess.run(["g++","-O3","-std=c++17","-I",str(a.notes_root),str(a.notes_root/name),"-o",str(exe)],stdout=log,stderr=subprocess.STDOUT,timeout=timeout)
    check(r.returncode==0,"native compilation "+key)
    atomic_json(meta,{"binding":compile_key,"executable":record(exe)})
   programs[key]=[str(exe)]
  programs["solve"]=[sys.executable,str(a.notes_root/(STEM+"local-unit-solve-789f.py"))]
  model_py=import_module(a.notes_root/(STEM+"original-model-p7-789f.py"),"r150_b4_positive_p7_model")
  p7model=a.out/"original-equations-mod31seven.txt"
  model_info=model_py.generate(a.exact_gzip,files["integerModel"],p7model)
  rec["parameters"]["originalP7Model"]=model_info;save()
  def prefix(name):
   d=a.out/"stages"/name;d.mkdir(parents=True,exist_ok=True);return d/name
  def run(name,program,args,marker,gates,inputs,outputs,logic):
   tick();source=NATIVE[program] if program in NATIVE else STEM+"local-unit-solve-789f.py"
   key=sha_bytes(canonical({"pipeline":binding,"source":source_records[source],"inputs":[record(p) for p in inputs],"logic":logic}))
   cp=checkpoints/(name+".json");context=checkpoints/(name+".context.json")
   if context.exists():check(json.loads(context.read_text())=={"inputBinding":key},"partial stage binding "+name)
   else:atomic_json(context,{"inputBinding":key})
   if cp.exists():
    old=json.loads(cp.read_text())
    check(old.get("inputBinding")==key,"completed stage input identity")
    if all(p.is_file() and record(p)==old["outputs"].get(str(p.relative_to(a.out))) for p in outputs):
     rec["parameters"]["stages"][name]={"status":"completed","reused":True,"inputBinding":key,"statistics":old["statistics"]}
     save();return
    raise ValueError("completed actual stage output changed "+name)
   remain=deadline-time.monotonic()-1
   if remain<3:raise BudgetStop("before "+name)
   actual=[str(max(0.1,remain-1)) if x=="__REMAINING__" else str(x) for x in args]
   command=["timeout","--kill-after=10s",str(remain)+"s","prlimit","--as="+str(a.memory_mib*1048576),"--core=0","--"]+programs[program]+actual
   stage={"status":"running","inputBinding":key};rec["parameters"]["stages"][name]=stage;save();began=time.monotonic();last={};logpath=logs/(name+".log")
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
   stage.update(exitCode=code,elapsedSeconds=time.monotonic()-began,statistics=last,log=record(logpath))
   if code in (75,124,-15):
    stage["status"]="budget-checkpoint";save();raise BudgetStop("actual unfinished stage "+name)
   ok=code==0 and last.get("status")==marker and all(last.get(k)==v for k,v in gates.items()) and all(p.is_file() for p in outputs)
   if not ok:
    stage["status"]="failed";stage["logTail"]=logpath.read_text(errors="replace")[-5000:];save();raise StageFailure("original stage did not complete "+name)
   stage["status"]="completed"
   atomic_json(cp,{"inputBinding":key,"statistics":last,"outputs":{str(p.relative_to(a.out)):record(p) for p in outputs}})
   save()
  specs=a.out/"specs";specs.mkdir(exist_ok=True)
  def spec(name,labels,L,ring=2):
   path=specs/(name+".spec");write_spec(path,labels,L,ring);return path
  spec25=spec("K2-through-K198-25",labels3,25)
  spec20=spec("new198-next-relations-20",NEW198,20)
  spec204=spec("L4-all204-20",labels4,20)
  spec15=spec("L5-all208-15",labels5,15)
  spec10=spec("L6-all210-10",labels6,10)
  def vq(name,mode,specfile,Q,V):
   p=prefix(name);outputs=[suffix(p,x) for x in ("-original2195-source-jets.bin","-vq.json")]
   if mode=="q1":outputs += [suffix(p,"-actual-G-root2.bin"),suffix(p,"-actual-V-root2.bin")]
   run(name,"vq",[files["model"],V,Q,files["oldK"],"-",p,binding,mode,specfile],
       "saturated-runtime-jet-VQ-complete",{"mode":mode},[files["model"],V,Q,files["oldK"],specfile],outputs,{"mode":mode})
   return p
  def transport(name,mode,specfile,C,trace):
   p=prefix(name)
   run(name,"transport",[files["model"],files["oldK"],suffix(C,"-original2195-source-jets.bin"),files["normalTrace"],trace,
       files["forward"],files["backward"],p,binding,mode,"-",specfile,p.parent/"checkpoints","__REMAINING__"],
       "runtime-local-original-source-transport-complete",{"mode":mode},
       [files[k] for k in ("model","oldK","normalTrace","forward","backward")]+[suffix(C,"-original2195-source-jets.bin"),trace,specfile],
       [suffix(p,"-original6188-q-jets.bin"),suffix(p,"-transport.json")],{"mode":mode})
   return p
  def integer(name,specfile,L,labels,exponent,retained,families):
   p=prefix(name);mix=p.parent/(name+".mix")
   logical,inf=write_mix(mix,labels,L,[exponent]*len(labels),families)
   run(name,"integer",[files["model"],p7model,specfile,mix,p,binding,retained,"__REMAINING__"],
       "root2-fourth-original-integer-p7-jets-complete",
       {"allOriginal17CoefficientsDivisible":True,"targetCount":len(labels),"computedTaylorPrecision":L,"retainedFormalPrecision":retained},
       [files["model"],p7model,specfile]+inf,
       [suffix(p,x) for x in ("-original6188-integer-jets.bin","-divided-original-jets.bin","-field-root2-jets.bin","-field-projected-crt8-jets.bin","-integer-product.json")],
       {"exponents":[exponent]*len(labels),"retained":retained,"families":logical})
   return p
  def normal(name,specfile,field,crt=False):
   p=prefix(name)
   run(name,"normal",[files["model"],field,files["graph"],specfile,p,binding],
       "saturated-runtime-two-ring-state-complete" if crt else "saturated-runtime-root2-normal-form-complete",{},
       [files["model"],field,files["graph"],specfile],
       [suffix(p,"-standard-state.bin" if crt else "-original1034-root2.bin"),suffix(p,"-local-prebasis-source-jets.bin"),suffix(p,"-local-normal.json")],
       {"CRT8":crt})
   return p
  def solve(name,G,NF):
   d=a.out/"stages"/name;d.mkdir(parents=True,exist_ok=True)
   run(name,"solve",["--G",G,"--rhs",suffix(NF,"-original1034-root2.bin"),"--binding",binding,
       "--notes-root",a.notes_root,"--out",d,"--remaining-seconds","__REMAINING__"],
       "saturated-local-unit-solve-complete",{"fullOriginalGIdentityVerified":True,"all13FreeConditionsRetained":True},
       [G,suffix(NF,"-original1034-root2.bin")],[d/"complete-G-q-root2.bin",d/"local-unit-solve-receipt.json"],
       {"completeOriginalRows":1034,"maximumSourcePrecisionLoss":5})
   return d/"complete-G-q-root2.bin"
  def correction7(C,exponent):
   n=len(C[0]);out=[]
   for key,labels,indices in [("kernels",[2275,2276,2277,2278],[(0,0),(1,1)]),
       ("fourK2",[4001,4002,4003,4004],[(0,2),(1,3),(2,4),(3,5)]),
       ("selectedK2",list(range(2,11)),[(0,6)])]:
    edges=[]
    for source,i in indices:
     ei=1 if i<2 else 2
     for j in range(n):
      if C[i][j]:edges.append([source,j,[-31**(exponent-ei)*int(C[i][j])]])
    out.append(family(files[key],labels,edges))
   return out
  def state_class(name,Lsource,labels,expected=None):
   sp=spec(name+"-CRT8",labels,8,12)
   nf=normal(name,sp,suffix(Lsource,"-field-projected-crt8-jets.bin"),True)
   path=suffix(nf,"-standard-state.bin");raw=path.read_bytes();n=len(labels)
   check(raw[:8]==b"R150SE31" and struct.unpack_from("<4I",raw,8)==(31,820,n,8),"all820 original standard states")
   check(list(struct.unpack_from("<%dH"%n,raw,24))==labels,"same true source labels in full quotient")
   at=24+2*n;coords=[list(struct.unpack_from("<HB",raw,at+3*i)) for i in range(820)];at+=2460
   check(coords==map_rec["standardCoordinates"] and len(raw)==at+820*n,"all820 coordinate dictionary and EOF")
   E=nmod_mat(820,n,list(raw[at:]),31);Y=M["Pi"]*E
   free=M["freeChecks"]*Y;D39=M["torsionCoordinates"]*Y
   check(h.zero(free) and M["torsionEmbedding"]*D39==Y,"all104 local free conditions and39 reconstruction")
   D=B*Li*h.sub(D39,pr["localTwoPrimaryPivotRows"],range(n))
   check(M["globalTorsionTo39"]*D==D39 and PM*D==D,"complete315 root2 reconstruction")
   globalstate=K*D
   check(h.zero(O*globalstate) and Astate*globalstate==K*(J*D),"all505 original global free observations and same s action")
   if expected is not None:check(D==expected,"new p7 source changed a paid true lower-page class")
   item={"status":"completed","sourceLabels":labels,"all104LocalFreeChecks":True,
         "all315OriginalCoordinateReconstruction":True,"all505GlobalFreeChecks":True,
         "sameOriginalSAction":True,"matchesPaidClass":expected is not None,
         "matrix":matrix_record(D)}
   atomic_json(nf.parent/"exact-class.json",{"binding":binding,**item,"matrixRows":matrix_rows(D)})
   rec["parameters"]["comparisons"][name]=item;save()
   return D
  def finish_prefix(name):
   if a.through==name:
    rec["status"]="completed-prefix";rec["parameters"]["completedThrough"]=name;save();return True
   return False
  q1=vq("q1-all197-original25-vq","q1",spec25,files["oldQ"],files["graph"])
  q1raw=transport("q1-all197-original25-transport","q1",spec25,q1,files["oldTrace"])
  G=suffix(q1,"-actual-G-root2.bin");V=suffix(q1,"-actual-V-root2.bin")
  if finish_prefix("q1"):return 0
  with files["oldK"].open("rb") as f:
   check(f.read(8)==b"R150KK31" and struct.unpack("<4I",f.read(16))==(31,6188,200,85),"same original K200 family")
   allK=[]
   for j in range(200):
    graph,head,cost,source,raw=struct.unpack("<IHHII",f.read(16));allK.append(head)
  check(allK[1:198]==labels3,"all K2..K198 in the original head dictionary")
  C7=[[int(pr["trueSevenCancellation197"][i][j]) for j in range(197)] for i in range(7)]
  families=[family(files["oldK"],allK,[[j+1,j,[1]] for j in range(197)]),
            family(suffix(q1raw,"-original6188-q-jets.bin"),labels3,identity_edges(197,-31))]
  families+=correction7(C7,2)
  T2=integer("T2-all197-corrected25",spec25,25,labels3,2,25,families)
  N2=normal("q2-all197-normal25",spec25,suffix(T2,"-field-root2-jets.bin"))
  Q2=solve("q2-all197-complete25",G,N2)
  q2=vq("q2-all197-vq25","q2",spec25,Q2,V)
  q2raw=transport("q2-all197-transport25","q2",spec25,q2,suffix(N2,"-local-prebasis-source-jets.bin"))
  L3=integer("L3-all197-true25",spec25,25,labels3,3,20,[
    family(suffix(T2,"-original6188-integer-jets.bin"),labels3,identity_edges(197)),
    family(suffix(q2raw,"-original6188-q-jets.bin"),labels3,identity_edges(197,-31**2))])
  D3=state_class("L3-all197-paid-class-check",L3,labels3,PM*(V10*C197))
  if finish_prefix("l3"):return 0
  alpha=pr["omegaAlphaB8"];beta=pr["omegaBetaD2"]
  check(len(alpha)==len(beta)==196,"all196 omega coefficient pairs; the two t-relations are separate")
  Cnew=[[int(pr["trueSevenCancellation198"][i][j]) for j in range(198)] for i in range(7)]
  edge3=[];edge8=[]
  for j in range(196):
   edge3.append([j+1,j,[1]])
   if beta[j]:edge3.append([0,j,[-int(beta[j])]])
   if alpha[j]:edge8.append([2,j,[-int(alpha[j])]])
  # These two are the exact t-relations of the paid 198-family.
  # They are distinct from the later F3 canonical lift s+29=31+t.
  edge8.append([2,196,[0,1]]);edge3.append([0,197,[0,1]])
  families=[family(suffix(L3,"-original6188-integer-jets.bin"),labels3,edge3),
            family(files["newOriginal"],LABEL16,edge8)]+correction7(Cnew,3)
  M3=integer("M3-all198-corrected20",spec20,20,NEW198,3,20,families)
  N3=normal("q3-all198-normal20",spec20,suffix(M3,"-field-root2-jets.bin"))
  Q3=solve("q3-all198-complete20",G,N3)
  q3=vq("q3-all198-vq20","q3",spec20,Q3,V)
  q3raw=transport("q3-all198-transport20","q3",spec20,q3,suffix(N3,"-local-prebasis-source-jets.bin"))
  families=[
    family(suffix(M3,"-original6188-integer-jets.bin"),NEW198,[[j,j+6,[1]] for j in range(198)]),
    family(suffix(q3raw,"-original6188-q-jets.bin"),NEW198,[[j,j+6,[-31**3]] for j in range(198)]),
    family(files["currentK4"],list(range(7001,7008)),[[i,j,[1]] for j,i in enumerate([0,1,4,5,6,3])])]
  L4=integer("L4-all204-true20",spec204,20,labels4,4,15,families)
  D4=state_class("L4-all204-paid-class-check",L4,labels4,D4old)
  if finish_prefix("l4"):return 0
  C9=[[int(recipe["oldTrueFirstNineCorrectionsForAll208"][i][j]) for j in range(208)] for i in range(9)]
  edges=[[i,j,taylor(F2[i][j])] for i in range(204) for j in range(208) if F2[i][j]]
  families=[family(suffix(L4,"-original6188-integer-jets.bin"),labels4,edges)]+correction7(C9[:7],4)
  families += [
    family(files["newOriginal"],LABEL16,[[2,j,[-31*C9[7][j]]] for j in range(208) if C9[7][j]]),
    family(suffix(L3,"-original6188-integer-jets.bin"),labels3,[[0,j,[-31*C9[8][j]]] for j in range(208) if C9[8][j]])]
  M4=integer("M4-all208-corrected15",spec15,15,labels5,4,15,families)
  N4=normal("q4-all208-normal15",spec15,suffix(M4,"-field-root2-jets.bin"))
  Q4=solve("q4-all208-complete15",G,N4)
  q4=vq("q4-all208-vq15","q4",spec15,Q4,V)
  q4raw=transport("q4-all208-transport15","q4",spec15,q4,suffix(N4,"-local-prebasis-source-jets.bin"))
  L5=integer("L5-all208-true15",spec15,15,labels5,5,10,[
    family(suffix(M4,"-original6188-integer-jets.bin"),labels5,identity_edges(208)),
    family(suffix(q4raw,"-original6188-q-jets.bin"),labels5,identity_edges(208,-31**4))])
  D5=state_class("L5-all208-paid-class-check",L5,labels5,D5old)
  if finish_prefix("l5"):return 0
  C13=[[int(recipe["trueThirteenCorrectionsForAll210"][i][j]) for j in range(210)] for i in range(13)]
  edges=[[i,j,F3t[i][j]] for i in range(208) for j in range(210) if trim_integer(F3t[i][j])]
  families=[family(suffix(L5,"-original6188-integer-jets.bin"),labels5,edges)]+correction7(C13[:7],5)
  families += [
    family(files["newOriginal"],LABEL16,[[2,j,[-31**2*C13[7][j]]] for j in range(210) if C13[7][j]]),
    family(suffix(L3,"-original6188-integer-jets.bin"),labels3,[[0,j,[-31**2*C13[8][j]]] for j in range(210) if C13[8][j]]),
    family(suffix(L4,"-original6188-integer-jets.bin"),labels4,
           [[6+i,j,[-31*C13[9+i][j]]] for i in range(4) for j in range(210) if C13[9+i][j]])]
  M5=integer("M5-all210-corrected10",spec10,10,labels6,5,10,families)
  N5=normal("q5-all210-normal10",spec10,suffix(M5,"-field-root2-jets.bin"))
  Q5=solve("q5-all210-complete10",G,N5)
  q5=vq("q5-all210-vq10","q5",spec10,Q5,V)
  q5raw=transport("q5-all210-transport10","q5",spec10,q5,suffix(N5,"-local-prebasis-source-jets.bin"))
  L6=integer("L6-all210-true10",spec10,10,labels6,6,5,[
    family(suffix(M5,"-original6188-integer-jets.bin"),labels6,identity_edges(210)),
    family(suffix(q5raw,"-original6188-q-jets.bin"),labels6,identity_edges(210,-31**5))])
  D6=state_class("L6-all210-complete-quotient",L6,labels6)
  paid_pair=h.sub(D6,range(315),[208,209])
  pair_quotient=project(paid_pair)
  check(matrix_record(paid_pair)["sha256"]==PAID_PROBE["whole315ClassSHA256"] and
        matrix_record(pair_quotient)["sha256"]==PAID_PROBE["quotientSHA256"] and pair_quotient.rank()==0,
        "exact prior two-source 315 classes and complete quotient reproduced")
  rec["parameters"]["priorTwoSourceClassesReproduced"]=True
  new=project(D6);rank=new.rank()
  check(rank<=1,"the known single remaining exponent permits at most one new direction")
  closed=h.join(new,Jq*new)
  check(closed.rank()==rank and h.zero((Jq-2*nmod_mat([[int(i==j) for j in range(300)] for i in range(300)],31))*new),
        "all210 polynomial source images are closed under the original root2 action")
  fullrank=h.join(incoming,D6).rank()
  check(fullrank==15+rank,"complete incoming quotient rank")
  columns_nonzero=[j for j in range(210) if any(int(new[i,j]) for i in range(300))]
  selected_basis=[]
  if columns_nonzero:selected_basis=[columns_nonzero[0]]
  zero_recipe_columns=h.sub(D6,range(315),[6,7,8,9,10,11])
  final={"binding":binding,"sourceLabels":labels6,"divisorExponent":6,
    "originalRows":6188,"originalOutputs":4367,"retainedFormalPrecision":5,
    "whole315Classes":matrix_rows(D6),"completeIncoming15":matrix_record(incoming),
    "quotientMatrix":matrix_record(new),"newRank":rank,"whole315CombinedRank":fullrank,
    "fullPolynomialSourceGeneratorCount":210,"all210CompleteImageComputed":True,
    "allSixFieldZeroRecipesRetained":True,"sixFieldZeroRecipeIndices":[6,7,8,9,10,11],
    "sixFieldZeroRecipeActual315Classes":matrix_record(zero_recipe_columns),
    "nonzeroQuotientSourceIndices":columns_nonzero,"basisOriginalSourceIndices":selected_basis,
    "basisOriginalSourceLabels":[labels6[i] for i in selected_basis],
    "all104LocalFreeChecks":True,"all505GlobalFreeChecks":True,
    "allOriginalIntegerCarriesVerified":True,"allPriorPaid315ClassesMatched":True,
    "priorTwoSourceClassesReproduced":True,
    "completeFourthSuccessiveIncrementOfB":rank,"canonicalI4DimensionOfB":8+rank,
    "remainingExponentExact":6 if rank else None,"remainingExponentLowerBound":6 if rank else 7,
    "allTrueSourceFilesRetainedTemporary":True}
  atomic_json(a.out/"complete210-exact-result.json",final)
  rec["status"]="completed"
  rec["outcome"]="complete-fourth-image-one-exponent-six" if rank else "complete-fourth-image-zero-exponent-at-least-seven"
  rec["parameters"]["final"]={k:v for k,v in final.items() if k!="whole315Classes"}
  rec["parameters"]["all210CompleteImageComputed"]=True
  rec["parameters"]["completeFourthImageComputed"]=True
  rec["parameters"]["negativeScope"]="zero covers all210 polynomial source generators and their full s multiples"
  save();return 0
 except (BudgetStop,subprocess.TimeoutExpired) as exc:
  rec["status"]="budget-checkpoint";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);save();return 75
 except BaseException as exc:
  rec["status"]="failed";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);save();return 1
 finally:
  save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
if __name__=="__main__":raise SystemExit(main())
