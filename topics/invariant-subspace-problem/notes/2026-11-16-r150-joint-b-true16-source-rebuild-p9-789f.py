#!/usr/bin/env python3
"""Rebuild only the actual true16 basis columns modulo31^9: 8 -> 7 -> 3 -> 1.
AI-assisted: GPT-6 Astra Pro / literature_audit, 2026-11-16.
The original full210 theorem is already paid. This program does not recompute it.
The actual Taylor precision is35; all source recipes and complete original product gates remain.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,math,os,resource,signal,struct,subprocess,sys,time
from pathlib import Path
from math import comb
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
P=31
P9=26439622160671
FORMAT="r150-joint-b-true16-selected-source-rebuild-p9-v1"
STEM="2026-11-16-r150-joint-b-"
ORIGINAL={"model":{"name":"model.txt","bytes":128145,"sha256":"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"},"graph":{"name":"graph.bin","bytes":101365853,"sha256":"bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce"},"normalTrace":{"name":"normalTrace.bin","bytes":101244784,"sha256":"e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b"},"forward":{"name":"forward.bin","bytes":2378937,"sha256":"66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e"},"backward":{"name":"backward.bin","bytes":3052119,"sha256":"cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f"},"oldK":{"name":"oldK.bin","bytes":48275717,"sha256":"ec067d86ce7c838697369d1f6a986c823de8564823d85b6684fe7a2926127a88"},"oldQ":{"name":"oldQ.bin","bytes":16649150,"sha256":"0bd81e4ae045daef1e224922ff0cceabd81436dc1680af29595ba2e169865338"},"oldTrace":{"name":"oldTrace.bin","bytes":113614260,"sha256":"85105ff9a84a81c05b88ee09d1f3a8de4bd9a1e7faf5657889c74e95f4f441ae"},"integerModel":{"name":"integerModel.txt","bytes":22824,"sha256":"2785c53d015d05db4550e1978c05db7d42009cfa8942e915541599a76d3701cc"},"state":{"name":"state.bin","bytes":1470456,"sha256":"06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"}}
SOURCES={"2026-11-16-r150-joint-b-local-common35-789f.hpp":"3fb7910935f46592c3f22cb3c2c727e8c25fdb0b34e7c8d65d1c558dca6e402c","2026-11-16-r150-joint-b-local-vq35-789f.cpp":"4381ac9e5c8b12567cb31b8f7f7151a20914ac5218cb5f0a0d9eec0880d054db","2026-11-16-r150-joint-b-local-original-transport35-789f.cpp":"d7f5dd75eb8139b014f309f8c8da3b98c7380efff3aa1243e4e9f921ddd74cb6","2026-11-16-r150-joint-b-local-normal35-789f.cpp":"b21a633ae018ccd54f4f4890ebfa4daec3f719a212a82ffd3a3e941decd493b3","2026-11-16-r150-joint-b-local-unit-solve35-789f.py":"3a1d41ddd0c7eaeb1047fbbf18da01e1af667a4726e462fcc41c381c7c2e7e62","2026-11-16-r150-joint-b-integer-p9-jets-789f.cpp":"1e309f6ecfc5e492b25dc39e58c37c1ee8ad685de798285f3fb398313115608e","2026-11-16-r150-joint-b-original-model-p9-789f.py":"1043eaacc50d0228f9bb2e8c00198a99ba4f405d1cad78453c2011455f4932f6","2026-11-14-r150-f31-bitplane-789f.hpp":"73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec","2026-11-14-r150-ninth-first-common-789f.hpp":"591dedf2c8a1d9d67fc644d21fae6e56ffc7ef8c840560831422197cbc5e9531","2026-11-14-r150-local-jet-unit-schur-helper-789f.py":"d31c917fe0aaa0e9008e5cb0a85cb81600b5a431fe691261948354fb1d1ee42b","2026-11-14-r150-ninth-first-matrices-789f.py":"3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a","2026-11-14-r150-torsion-characteristic-789f.py":"8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2","2026-11-15-r150-root2-fourth-complete210-source-preparation-789f.py":"105961c4d6f105dd16a3f70e5ce974c28c1e0e64534510e1af50370525c9fb51"}
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
FAMILIES.pop("currentK4")
I3=list(range(8))
I4=list(range(6,13))
I5=[10,11,12]
I6=[12]
OLD_FULL_BINDING="712f9b426017d3f63c05e755a314e14d79ac03d22bce6a4b3f943efcd80d7093"
OLD_GV={"G":(26397022,"ef9976aca179c382c4bf265b362e56280ea725aea16e164e8d29d5759bd92202",24),
        "V":(55688902,"ed02ca487853bff3a9f117b2e3c749c0cf5c9897bb4bb9d4dd53184ee0597d5a",28)}
OLD_U16_SHA="679132fd4727fd305b77c82beb5d3f2e002df1860045200c3392158ab8eb48b9"
OLD_J16_SHA="59d09cbeec71ebf7cda6f12ddd21c1b7ffe1c83a3f9de81b776df0a97df687d8"
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
NATIVE={"vq":STEM+"local-vq35-789f.cpp","transport":STEM+"local-original-transport35-789f.cpp",
        "normal":STEM+"local-normal35-789f.cpp","integer":STEM+"integer-p9-jets-789f.cpp"}
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
 p=[int(x)%P9 for x in p]
 while p and not p[-1]:p.pop()
 return p
def taylor(p):
 return trim_integer([sum(int(p[d])*comb(d,k)*2**(d-k) for d in range(k,len(p)))%P9 for k in range(len(p))])
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
 lines=["R150_JOINT_B_INTEGER_MIX_V1 %d %d %d"%(len(labels),L,len(active))," ".join(map(str,exponents))]
 semantic=[]
 for f in active:
  check(not any(c.isspace() for c in str(f["file"])),"source paths must not contain whitespace")
  lines.append("%s %d %d"%(f["file"],len(f["labels"]),len(f["edges"])))
  lines.append(" ".join(map(str,f["labels"])))
  for i,j,p in f["edges"]:lines.append("%d %d %d %s"%(i,j,len(p)," ".join(map(str,p))))
  semantic.append({"input":record(f["file"]),"labels":f["labels"],"edges":f["edges"]})
 atomic(path,("\n".join(lines)+"\n").encode("ascii"))
 return semantic,[f["file"] for f in active]

def paid_gv_prefix(path,key,binding):
 """Verify the complete saved35 cache and its exact paid25 mathematical prefix."""
 size,expected,offset=OLD_GV[key];h=hashlib.sha256()
 def read(f,n):
  z=f.read(n);check(len(z)==n,"complete actual G/V35 payload");return z
 with path.open("rb") as f:
  head=bytearray(read(f,offset+64))
  check(head[:8]==(b"R150SG31" if key=="G" else b"R150SV31"),"original G/V magic")
  shape=(31,1034,1021,35) if key=="G" else (31,1034,1021,2195,35)
  check(struct.unpack_from("<"+"I"*len(shape),head,8)==shape and head[offset:offset+64]==binding.encode(),"actual35 G/V dimensions and binding")
  struct.pack_into("<I",head,offset-4,25);head[offset:offset+64]=OLD_FULL_BINDING.encode()
  h.update(head);used=len(head)
  if key=="G":
   meta=read(f,4*1021);h.update(meta);used+=len(meta)
   left=25*1034*1021
   while left:
    z=read(f,min(left,1048576));check(max(z,default=0)<31,"all G field coefficients");h.update(z);used+=len(z);left-=len(z)
   left=10*1034*1021
   while left:
    z=read(f,min(left,1048576));check(not any(z),"original G has no higher25 Taylor coefficients");left-=len(z)
  else:
   previous=0
   for _ in range(1021):
    meta=read(f,8);c,d,lc,n=struct.unpack("<HBBI",meta)
    check(previous<c<=1034 and 0<=d<=8 and 0<lc<31 and n<=2195,"complete original V row metadata")
    previous=c;items=[]
    for _ in range(n):
     raw=read(f,37);source=struct.unpack_from("<H",raw,0)[0];co=raw[2:]
     check(1<=source<=2195 and max(co,default=0)<31 and any(co),"complete original V coefficient entry")
     if any(co[:25]):items.append(raw[:27])
    oldrow=struct.pack("<HBBI",c,d,lc,len(items));h.update(oldrow);used+=8
    for raw in items:h.update(raw);used+=len(raw)
  check(not f.read(1),"complete original G/V35 EOF")
 check(used==size and h.hexdigest()==expected,"same entire paid25 G/V mathematical prefix")
 return {"TaylorPrecision":35,"paidTaylorPrefix":25,"normalizedPaidPrefixBytes":used,
  "normalizedPaidPrefixSHA256":expected,"headerBindingOffset":offset,"complete35PayloadVerified":True}

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
 rec={"format":FORMAT,"status":"running","parameters":{"prime":31,"modulus":P9,
  "largeArraysTemporaryOnly":True,"complete210Recomputed":False,
  "originalSourceRows":6188,"originalOutputRows":4367,"precisionChain":[35,30,25,20,15],
  "originalSelectedIndices":{"L3":I3,"L4":I4,"L5":I5,"L6":I6},
  "dependencySourceCounts":{"L3":8,"L4":7,"L5":3,"L6":1},"stages":{},"comparisons":{}}}
 receipt_path=a.out/"selected-true16-source-rebuild-receipt.json"
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
    "originalSelectedIndices":{"L3":I3,"L4":I4,"L5":I5,"L6":I6},
    "paidFull210Binding":OLD_FULL_BINDING,"precisionChain":[35,30,25,20,15]}
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
  map_raw=mp.read_bytes();map_rec=json.loads(mrp.read_text())
  M={k:h.block(map_raw,map_rec,k) for k in map_rec["matrices"]}
  labels197=pr["sourceLabels197"];check(len(labels197)==197 and len(set(labels197))==197,"original197 source labels")
  labels3=[labels197[i] for i in I3];labels4=[ALL204[i] for i in I4];labels5=[ALL208[i] for i in I5];labels6=[ALL210[i] for i in I6]
  new_labels=[NEW198[i-6] for i in I4]
  F2=recipe["secondKernelGeneratorsInSAscending"];F3t=recipe["thirdKernelCanonicalIntegerTaylorMod31Seven"]
  check(recipe["sourceLabels204"]==ALL204 and recipe["sourceLabels208"]==ALL208 and recipe["sourceLabels210"]==ALL210,"all original generator labels")
  check(recipe["thirdImageSAction"]==[[2,0],[0,2]],"actual last two t-section recipes")
  for j in I6:
   check(all(not trim_integer(F3t[i][j]) for i in range(208) if i not in I5),
         "entire selected F3 column has no omitted source dependency")
  for j in I5:
   check(all(not F2[i][j] for i in range(204) if i not in I4),
         "entire selected F2 column has no omitted source dependency")
  check(I4==list(range(6,13)) and I3==list(range(8)),"complete selected M3/L3 dependency closure")
  rec["parameters"]["fullRecipeSupportChecks"]={"all208F3Rows":True,"all204F2Rows":True,"canonicalP9PolynomialsUnchanged":True}
  save()
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
  programs["solve"]=[sys.executable,str(a.notes_root/(STEM+"local-unit-solve35-789f.py"))]
  model_py=import_module(a.notes_root/(STEM+"original-model-p9-789f.py"),"r150_joint_b_p9_model")
  p9model=a.out/"original-equations-mod31nine.txt"
  model_info=model_py.generate(a.exact_gzip,files["integerModel"],p9model)
  rec["parameters"]["originalP9Model"]=model_info;save()
  def prefix(name):
   d=a.out/"stages"/name;d.mkdir(parents=True,exist_ok=True);return d/name
  def run(name,program,args,marker,gates,inputs,outputs,logic):
   tick();source=NATIVE[program] if program in NATIVE else STEM+"local-unit-solve35-789f.py"
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
  spec35=spec("K2-through-K9-35",labels3,35)
  spec30=spec("new-selected7-relations-30",new_labels,30)
  spec204=spec("L4-selected7-30",labels4,30)
  spec25=spec("L5-selected3-25",labels5,25)
  spec20=spec("L6-selected1-20",labels6,20)
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
   run(name,"integer",[files["model"],p9model,specfile,mix,p,binding,retained,"__REMAINING__"],
       "joint-b-original-integer-p9-jets-complete",
       {"allOriginal17CoefficientsDivisible":True,"targetCount":len(labels),"computedTaylorPrecision":L,"retainedFormalPrecision":retained},
       [files["model"],p9model,specfile]+inf,
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
   if expected is not None:check(D==expected,"new p9 source changed a paid true lower-page class")
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
  q1=vq("q1-selected8-original35-vq","q1",spec35,files["oldQ"],files["graph"])
  q1raw=transport("q1-selected8-original35-transport","q1",spec35,q1,files["oldTrace"])
  G=suffix(q1,"-actual-G-root2.bin");V=suffix(q1,"-actual-V-root2.bin")
  gv={}
  for key,path in (("G",G),("V",V)):
   prefix_identity=paid_gv_prefix(path,key,binding)
   gv[key]={"path":str(path.relative_to(a.out)),**record(path),**prefix_identity}
  rec["parameters"]["completeConstantCacheIdentity"]=gv;save()
  if finish_prefix("q1"):return 0
  with files["oldK"].open("rb") as f:
   check(f.read(8)==b"R150KK31" and struct.unpack("<4I",f.read(16))==(31,6188,200,85),"same original K200 family")
   allK=[]
   for j in range(200):
    graph,head,cost,source,raw=struct.unpack("<IHHII",f.read(16));allK.append(head)
  check([allK[i+1] for i in I3]==labels3,"selected actual K2..K9 in the original head dictionary")
  C7=[[int(pr["trueSevenCancellation197"][i][j]) for j in I3] for i in range(7)]
  families=[family(files["oldK"],allK,[[j+1,k,[1]] for k,j in enumerate(I3)]),
            family(suffix(q1raw,"-original6188-q-jets.bin"),labels3,identity_edges(8,-31))]
  families+=correction7(C7,2)
  T2=integer("T2-selected8-corrected35",spec35,35,labels3,2,35,families)
  N2=normal("q2-selected8-normal35",spec35,suffix(T2,"-field-root2-jets.bin"))
  Q2=solve("q2-selected8-complete35",G,N2)
  q2=vq("q2-selected8-vq35","q2",spec35,Q2,V)
  q2raw=transport("q2-selected8-transport35","q2",spec35,q2,suffix(N2,"-local-prebasis-source-jets.bin"))
  L3=integer("L3-selected8-true35",spec35,35,labels3,3,30,[
   family(suffix(T2,"-original6188-integer-jets.bin"),labels3,identity_edges(8)),
   family(suffix(q2raw,"-original6188-q-jets.bin"),labels3,identity_edges(8,-31**2))])
  D3=state_class("L3-selected8-paid-class-check",L3,labels3,h.sub(PM*(V10*C197),range(315),I3))
  if finish_prefix("l3"):return 0
  alpha=pr["omegaAlphaB8"];beta=pr["omegaBetaD2"]
  check(len(alpha)==len(beta)==196,"original omega coefficient dictionary")
  pos3={j:i for i,j in enumerate(I3)};pos4={j:i for i,j in enumerate(I4)}
  new_indices=[i-6 for i in I4]
  Cnew=[[int(pr["trueSevenCancellation198"][i][j]) for j in new_indices] for i in range(7)]
  edge3=[];edge8=[]
  for k,j in enumerate(new_indices):
   edge3.append([pos3[j+1],k,[1]])
   if beta[j]:edge3.append([pos3[0],k,[-int(beta[j])]])
   if alpha[j]:edge8.append([2,k,[-int(alpha[j])]])
  families=[family(suffix(L3,"-original6188-integer-jets.bin"),labels3,edge3),
            family(files["newOriginal"],LABEL16,edge8)]+correction7(Cnew,3)
  M3=integer("M3-selected7-corrected30",spec30,30,new_labels,3,30,families)
  N3=normal("q3-selected7-normal30",spec30,suffix(M3,"-field-root2-jets.bin"))
  Q3=solve("q3-selected7-complete30",G,N3)
  q3=vq("q3-selected7-vq30","q3",spec30,Q3,V)
  q3raw=transport("q3-selected7-transport30","q3",spec30,q3,suffix(N3,"-local-prebasis-source-jets.bin"))
  L4=integer("L4-selected7-true30",spec204,30,labels4,4,25,[
   family(suffix(M3,"-original6188-integer-jets.bin"),new_labels,identity_edges(7)),
   family(suffix(q3raw,"-original6188-q-jets.bin"),new_labels,identity_edges(7,-31**3))])
  D4=state_class("L4-selected7-paid-class-check",L4,labels4,h.sub(D4old,range(315),I4))
  if finish_prefix("l4"):return 0
  C9=[[int(recipe["oldTrueFirstNineCorrectionsForAll208"][i][j]) for j in I5] for i in range(9)]
  edges=[[pos4[i],k,taylor(F2[i][j])] for i in I4 for k,j in enumerate(I5) if F2[i][j]]
  families=[family(suffix(L4,"-original6188-integer-jets.bin"),labels4,edges)]+correction7(C9[:7],4)
  families += [
   family(files["newOriginal"],LABEL16,[[2,j,[-31*C9[7][j]]] for j in range(3) if C9[7][j]]),
   family(suffix(L3,"-original6188-integer-jets.bin"),labels3,[[pos3[0],j,[-31*C9[8][j]]] for j in range(3) if C9[8][j]])]
  M4=integer("M4-selected3-corrected25",spec25,25,labels5,4,25,families)
  N4=normal("q4-selected3-normal25",spec25,suffix(M4,"-field-root2-jets.bin"))
  Q4=solve("q4-selected3-complete25",G,N4)
  q4=vq("q4-selected3-vq25","q4",spec25,Q4,V)
  q4raw=transport("q4-selected3-transport25","q4",spec25,q4,suffix(N4,"-local-prebasis-source-jets.bin"))
  L5=integer("L5-selected3-true25",spec25,25,labels5,5,20,[
   family(suffix(M4,"-original6188-integer-jets.bin"),labels5,identity_edges(3)),
   family(suffix(q4raw,"-original6188-q-jets.bin"),labels5,identity_edges(3,-31**4))])
  D5=state_class("L5-selected3-paid-class-check",L5,labels5,h.sub(D5old,range(315),I5))
  if finish_prefix("l5"):return 0
  C13=[[int(recipe["trueThirteenCorrectionsForAll210"][i][j]) for j in I6] for i in range(13)]
  edges=[[k,jj,F3t[i][j]] for k,i in enumerate(I5) for jj,j in enumerate(I6) if trim_integer(F3t[i][j])]
  families=[family(suffix(L5,"-original6188-integer-jets.bin"),labels5,edges)]+correction7(C13[:7],5)
  families += [
   family(files["newOriginal"],LABEL16,[[2,0,[-31**2*C13[7][0]]]] if C13[7][0] else []),
   family(suffix(L3,"-original6188-integer-jets.bin"),labels3,[[pos3[0],0,[-31**2*C13[8][0]]]] if C13[8][0] else []),
   family(suffix(L4,"-original6188-integer-jets.bin"),labels4,
          [[pos4[6+i],0,[-31*C13[9+i][0]]] for i in range(4) if C13[9+i][0]])]
  M5=integer("M5-selected1-corrected20",spec20,20,labels6,5,20,families)
  N5=normal("q5-selected1-normal20",spec20,suffix(M5,"-field-root2-jets.bin"))
  Q5=solve("q5-selected1-complete20",G,N5)
  q5=vq("q5-selected1-vq20","q5",spec20,Q5,V)
  q5raw=transport("q5-selected1-transport20","q5",spec20,q5,suffix(N5,"-local-prebasis-source-jets.bin"))
  L6=integer("L6-selected1-true20",spec20,20,labels6,6,15,[
   family(suffix(M5,"-original6188-integer-jets.bin"),labels6,identity_edges(1)),
   family(suffix(q5raw,"-original6188-q-jets.bin"),labels6,identity_edges(1,-31**5))])
  D6=state_class("L6-selected1-complete-class",L6,labels6)
  U13=nmod_mat(recipe["true13Full315"],31)
  check(h.sub(U13,range(315),[8])==h.sub(D3,range(315),[pos3[0]]),"same paid true L3 source class")
  check(h.sub(U13,range(315),range(9,13))==h.sub(D4,range(315),[pos4[i] for i in range(6,10)]),
        "same paid true four L4 source classes")
  U15=h.join(U13,h.sub(D5,range(315),[I5.index(10),I5.index(11)]));U16=h.join(U15,D6)
  check(U16.rank()==16 and matrix_record(U16)["sha256"]==OLD_U16_SHA,"same complete original true16 residue basis")
  j16=h.solve_span(U16,J*U16)
  check(j16["indices"]==list(range(16)) and h.zero(j16["residual"]),"complete original parameter action on true16")
  J16=j16["solution"];check(U16*J16==J*U16 and matrix_record(J16)["sha256"]==OLD_J16_SHA,
                          "all5040 original parameter-action products and same paid action")
  source_specs={"L3":(L3,labels3,I3,35,30,3,[pos3[0]],"L3-selected8-paid-class-check"),
                "L4":(L4,labels4,I4,30,25,4,[pos4[i] for i in range(6,10)],"L4-selected7-paid-class-check"),
                "L5":(L5,labels5,I5,25,20,5,[I5.index(10),I5.index(11)],"L5-selected3-paid-class-check"),
                "L6":(L6,labels6,I6,20,15,6,[0],"L6-selected1-complete-class")}
  source_families={};class_records={}
  for key,(p,labs,indices,L,valid,e,selected_indices,class_name) in source_specs.items():
   file=suffix(p,"-original6188-integer-jets.bin");cp=a.out/"stages"/class_name/"exact-class.json"
   source_families[key]={"path":str(file.relative_to(a.out)),**record(file),"stage":p.name,
    "labels":len(labs),"sourceLabels":labs,"originalIndices":indices,"L":L,"valid":valid,"e":e,"indices":selected_indices}
   class_records[key]={"path":str(cp.relative_to(a.out)),**record(cp),"matrix":rec["parameters"]["comparisons"][class_name]["matrix"]}
  pack={"format":"r150-joint-b-selected-true16-parent-p9-v1","status":"completed","binding":binding,
    "sourceSHA256":self_record["sha256"],"sources":source_records,"inputs":identities,
    "full210OriginalTheoremBinding":OLD_FULL_BINDING,"complete210Recomputed":False,
    "precisionChain":[35,30,25,20,15],"originalSelectedIndices":{"L3":I3,"L4":I4,"L5":I5,"L6":I6},
    "constantCaches":gv,"sourceFamilies":source_families,"classes":class_records,
    "trueBasisIdentities":{"true13":matrix_record(U13),"true15":matrix_record(U15),"true16":matrix_record(U16),"parameterAction16":matrix_record(J16)},
    "allOriginalIntegerCarriesVerified":True,"allLowerPaid315ClassesMatched":True,
    "all104LocalFreeChecks":True,"all505GlobalFreeChecks":True,
    "samePaid25PrefixAndComplete35OriginalGAndV":True,"canonicalOriginalColumnRecipesPreserved":True}
  atomic_json(a.out/"selected-true16-parent.json",pack)
  rec["status"]="completed";rec["parameters"]["parentPack"]=record(a.out/"selected-true16-parent.json")
  rec["parameters"]["trueBasisIdentities"]=pack["trueBasisIdentities"]
  rec["parameters"]["allOriginalIntegerCarriesVerified"]=True
  rec["parameters"]["full210NotRecomputed"]=True
  save();return 0
 except (BudgetStop,subprocess.TimeoutExpired) as exc:
  rec["status"]="budget-checkpoint";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);save();return 75
 except BaseException as exc:
  rec["status"]="failed";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);save();return 1
 finally:
  save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
if __name__=="__main__":raise SystemExit(main())
