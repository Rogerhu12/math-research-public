#!/usr/bin/env python3
"""Ten-row, twelve-parameter original-source positive search over F127.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
The fifty literal original columns generate the paid 116-seed parameter module.
slimgb is only a candidate finder. A positive result requires U=I, all ten
module coordinates, the complete original18 polynomial product, and the
original-gradient Jacobian transport. A negative remainder is diagnostic only.
No parameter is specialized, no stable closure is assumed, and no E lift is
claimed. SSI and polynomial arrays are temporary; only identities enter Git.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,re,resource,shutil,signal,subprocess,sys,time
from pathlib import Path
sys.set_int_max_str_digits(0)
FORMAT="r150-original-compressed-parameter-module-positive127-v1"
P=127;ROOT=100
MODEL_SHA="4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4"
COMPRESSION_SHA="b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9"
MODEL_BINDING="7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4"
MODEL_MANIFEST={"bytes":30466,"sha256":"9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2"}
COMPRESSION_BINDING="baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca"
COMPRESSION_MATH={"bytes":620742,"sha256":"a1d73ea1ce5809c87bdc34724c1eb4407d6a5c0ae78fbf16aa3650563aa089dd"}
PARAMETERS=tuple(["y%d"%i for i in range(6)]+["w%d"%i for i in range(6)])
MWEIGHT=[0]+[2]*5+[4]*4
class Budget(Exception):pass
def need(b,s):
 if not b:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 p=Path(p);h=hashlib.sha256()
 with p.open("rb") as f:
  for z in iter(lambda:f.read(1048576),b""):h.update(z)
 return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact(p,d):
 z=identity(p);need(z["bytes"]==d["bytes"] and z["sha256"]==d["sha256"],"complete exact file "+p.name);return z
def atomic(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
def save_json(p,x):atomic(p,canon(x));return identity(p)
def save_gz(p,x,binding):
 b=canon({"format":FORMAT+"-phase","binding":binding,"data":x});z=gzip.compress(b,compresslevel=1,mtime=0);atomic(p,z)
 return {**identity(p),"logicalBytes":len(b),"logicalSha256":sha(b)}
def load_gz(p,d,binding):
 exact(p,d);b=gzip.decompress(p.read_bytes());need(len(b)==d["logicalBytes"] and sha(b)==d["logicalSha256"],"whole logical phase")
 z=json.loads(b);need(z["format"]==FORMAT+"-phase" and z["binding"]==binding,"same positive-source phase");return z["data"]
def module(p,digest,name):
 need(identity(p)["sha256"]==digest,"exact executable dependency "+name)
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def ss(p,mode=""):
 s=str(p);need(not any(c in s for c in ('"',"\\","\r","\n")),"safe literal Singular path")
 return '"'+mode+s+'"'
def markers(p):
 good=[];bad=[]
 with p.open("r",encoding="utf-8",errors="replace") as f:
  for line in f:
   x=line.strip()
   if x.startswith("@@"):good.append(x)
   if x.startswith("@@FAIL") or x.startswith("?"):bad.append(x[:600])
 need(len(good)<=10000 and len(bad)<=10000,"bounded literal transcript")
 return good,bad
def one(ms,prefix,required=True):
 z=[s for s in ms if s.startswith(prefix)];need(len(z)<=1,"unique marker "+prefix)
 if required:need(len(z)==1,"complete marker "+prefix)
 return z[0] if z else None
def parse_poly(path,names):
 """Only expanded short=0 finite-field monomials; never evaluate input code."""
 s="".join(path.read_text(encoding="ascii").split())
 if s=="0":return {}
 need(s and s[0] not in "*^","nonempty complete polynomial text")
 terms=re.findall(r"[+-]?[^+-]+",s);need("".join(terms)==s,"full polynomial token coverage")
 where={x:i for i,x in enumerate(names)};out={}
 for t in terms:
  c=1
  if t[0] in "+-":
   if t[0]=="-":c=-1
   t=t[1:]
  need(t,"nonempty signed term");e=[0]*len(names)
  for fac in t.split("*"):
   if fac.isdigit():c=c*int(fac)%P;continue
   z=fac.split("^");need(len(z)<=2 and z[0] in where,"literal parameter polynomial variable")
   need(len(z)==1 or z[1].isdigit(),"literal nonnegative monomial power")
   k=1 if len(z)==1 else int(z[1]);e[where[z[0]]]+=k
  e=tuple(e);out[e]=(out.get(e,0)+c)%P
 return {e:c for e,c in out.items() if c}
def singular_poly(f):
 parts=[]
 for e,c in sorted(f.to_dict().items()):
  need(len(e)==17 and not any(e[12:]) and 0<int(c)<P,"all twelve complete parameter exponents")
  s="*".join(x+("^%d"%a if a!=1 else "") for x,a in zip(PARAMETERS,e[:12]) if a)
  parts.append(str(int(c))+("*"+s if s else ""))
 return "+".join(parts) if parts else "0"
def ring():
 return ["ring r=127,("+",".join(PARAMETERS)+"),(wp(1,1,1,1,1,1,2,2,2,2,2,2),C);",
         "short=0; degBound=0; option(redSB); option(redTail);"]
def read_original(out):
 return ring()+["def Original=read("+ss(out/"complete-original-ten-by-fifty.ssi","ssi:r ")+");",
  'if(ncols(Original)!=50){print("@@FAIL original50-shape");quit;}',
  "matrix OM[10][50]=Original; matrix TM[10][1]; TM[1,1]=1; module Target=TM;"]
def selftest_script(out):
 lines=["ring r=127,(x,y),(dp,C); short=0; degBound=0; option(redSB); option(redTail);",
  "matrix OM[2][2]; OM[1,1]=x; OM[2,1]=1; OM[1,2]=1-x*y; OM[2,2]=-y; module Original=OM;",
  "matrix TM[2][1]; TM[1,1]=1; module Target=TM;",
  'print("@@MODULE-SELFTEST-START"); module G=slimgb(Original);',
  'if(reduce(Target[1],G)!=0){print("@@FAIL module-positive-remainder");quit;}',
  "module Guard=[x,1]; module GuardG=slimgb(Guard);",
  'if(reduce(Target[1],GuardG)==0){print("@@FAIL module-negative-control");quit;}',
  "write("+ss(out/"selftest-module-basis.ssi","ssi:w ")+",G); def GC=read("+ss(out/"selftest-module-basis.ssi","ssi:r ")+");",
  'if(ncols(GC)!=ncols(G)){print("@@FAIL selftest-module-SSI-shape");quit;}',
  'int i; for(i=1;i<=ncols(G);i++){if(G[i]!=GC[i]){print("@@FAIL selftest-module-SSI-product");quit;}}',
  'matrix Units; matrix Sources=lift(Original,Target,Units,"slimgb");',
  'if(nrows(Sources)!=2 || ncols(Sources)!=1){print("@@FAIL selftest-source-shape");quit;}',
  'if(nrows(Units)!=1 || ncols(Units)!=1 || Units[1,1]!=1){print("@@FAIL selftest-source-unit");quit;}',
  "matrix Difference=OM*Sources-TM;",
  'for(i=1;i<=2;i++){if(Difference[i,1]!=0){print("@@FAIL selftest-original-product");quit;}}',
  "write("+ss(out/"selftest-module-source.ssi","ssi:w ")+",Sources); def SC=read("+ss(out/"selftest-module-source.ssi","ssi:r ")+");",
  'if(nrows(SC)!=2 || ncols(SC)!=1){print("@@FAIL selftest-source-SSI-shape");quit;}',
  'for(i=1;i<=2;i++){if(SC[i,1]!=Sources[i,1]){print("@@FAIL selftest-source-SSI-product");quit;}}']
 for i in range(2):lines.append("write("+ss(out/("selftest-source-%d.txt"%i),":w ")+",Sources[%d,1]);"%(i+1))
 lines += ["write("+ss(out/"selftest-parser.txt",":w ")+",-5*x^4+3*x*y^3+2);",'print("@@MODULE-SELFTEST-COMPLETE"); quit;']
 return "\n".join(lines)+"\n"
def materialize_script(out,ascii_source):
 return ascii_source+"\n".join([
  "write("+ss(out/"complete-original-ten-by-fifty.ssi","ssi:w ")+",Original);",
  "def Copy=read("+ss(out/"complete-original-ten-by-fifty.ssi","ssi:r ")+");",
  'if(ncols(Copy)!=50){print("@@FAIL original50-SSI-shape");quit;}',
  "matrix CM[10][50]=Copy; int i; int j;",
  'for(i=1;i<=10;i++){for(j=1;j<=50;j++){if(OM[i,j]!=CM[i,j]){print("@@FAIL original500-SSI-product");quit;}}}',
  'print("@@ALL-500-ORIGINAL-MODULE-SSI-COORDINATES"); quit;'])+"\n"
def discovery_script(out):
 return "\n".join(read_original(out)+[
  'print("@@PARAMETER-MODULE-SLIMGB-START"); module G=slimgb(Original);',
  'print("@@PARAMETER-MODULE-SLIMGB-RETURN "+string(ncols(G)));',
  "write("+ss(out/"whole-parameter-module-candidate.ssi","ssi:w ")+",G);",
  "def GC=read("+ss(out/"whole-parameter-module-candidate.ssi","ssi:r ")+");",
  'if(ncols(GC)!=ncols(G)){print("@@FAIL candidate-module-SSI-shape");quit;}',
  'int i; for(i=1;i<=ncols(G);i++){if(GC[i]!=G[i]){print("@@FAIL candidate-module-SSI-product");quit;}}',
  'print("@@WHOLE-PARAMETER-MODULE-CANDIDATE-SAVED "+string(ncols(G))); quit;'])+"\n"
def target_script(out):
 lines=read_original(out)+["def G=read("+ss(out/"whole-parameter-module-candidate.ssi","ssi:r ")+");",
  'print("@@PARAMETER-TARGET-REDUCTION-START"); vector residual=reduce(Target[1],G);',
  "matrix RM[10][1]; RM[1,1]=residual[1]; int i;",
  "for(i=1;i<=10;i++){RM[i,1]=residual[i];}"]
 for i in range(10):lines.append("write("+ss(out/("target-remainder-%02d.txt"%i),":w ")+",RM[%d,1]);"%(i+1))
 lines+=['print("@@PARAMETER-TARGET-REDUCTION-END "+string(residual==0)); quit;']
 return "\n".join(lines)+"\n"
def lift_script(out):
 return "\n".join(read_original(out)+[
  'print("@@FIFTY-ORIGINAL-SOURCE-LIFT-START"); matrix Units;',
  'matrix Sources=lift(Original,Target,Units,"slimgb");',
  'print("@@FIFTY-ORIGINAL-SOURCE-LIFT-RETURN");',
  'if(nrows(Sources)!=50 || ncols(Sources)!=1){print("@@FAIL original50-source-shape");quit;}',
  'if(nrows(Units)!=1 || ncols(Units)!=1 || Units[1,1]!=1){print("@@FAIL original50-source-unit");quit;}',
  "write("+ss(out/"whole-fifty-original-target-sources.ssi","ssi:w ")+",Sources);",
  "def SC=read("+ss(out/"whole-fifty-original-target-sources.ssi","ssi:r ")+");",
  'if(nrows(SC)!=50 || ncols(SC)!=1){print("@@FAIL source50-SSI-shape");quit;}',
  'int i; for(i=1;i<=50;i++){if(SC[i,1]!=Sources[i,1]){print("@@FAIL source50-SSI-product");quit;}}',
  'print("@@WHOLE-FIFTY-ORIGINAL-SOURCES-SAVED-UNIT-IDENTITY"); quit;'])+"\n"
def export_script(out,first,product_paid):
 lines=read_original(out)+["def Sources=read("+ss(out/"whole-fifty-original-target-sources.ssi","ssi:r ")+");",
  'if(nrows(Sources)!=50 || ncols(Sources)!=1){print("@@FAIL verify-source50-shape");quit;}']
 if not product_paid:
  lines += ["matrix Difference=OM*Sources-TM; int i;",
   'for(i=1;i<=10;i++){if(Difference[i,1]!=0){print("@@FAIL all-ten-original-module-products");quit;}}',
   'print("@@ALL-TEN-ORIGINAL-MODULE-PRODUCTS-VERIFIED");']
 for i in range(first,50):
  lines += ["write("+ss(out/("original-source-%02d.txt"%i),":w ")+",Sources[%d,1]);"%(i+1),
   'print("@@ORIGINAL-SOURCE-TEXT '+str(i)+' "+string(size(Sources[%d,1])));'%(i+1)]
 lines+=['print("@@ALL-FIFTY-ORIGINAL-SOURCE-TEXTS-SAVED"); quit;']
 return "\n".join(lines)+"\n"
def main():
 ap=argparse.ArgumentParser()
 for x in ("model-source","model-out","compression-source","compression-out","out"):ap.add_argument("--"+x,type=Path,required=True)
 ap.add_argument("--singular",default="Singular");ap.add_argument("--seconds",type=float,default=600)
 ap.add_argument("--memory-mib",type=int,default=4096);ap.add_argument("--through",choices=("prepare","selftest","final"),default="final")
 a=ap.parse_args();need(0<a.seconds<=3600 and 512<=a.memory_mib<=8192,"bounded whole-source search")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 started=time.monotonic();deadline=started+a.seconds;a.out.mkdir(parents=True,exist_ok=True)
 own=identity(Path(__file__))
 sem={"format":FORMAT,"source":own,"modelSourceSHA256":MODEL_SHA,"compressionSourceSHA256":COMPRESSION_SHA,
  "modelBinding":MODEL_BINDING,"modelManifest":MODEL_MANIFEST,"compressionBinding":COMPRESSION_BINDING,
  "completeCompressionMathematics":COMPRESSION_MATH,"prime":P,"coefficientRoot":ROOT,
  "originalParameters":PARAMETERS,"momentModuleWeights":MWEIGHT,"originalColumnCount":50,
  "ringOrdering":"wp(1,1,1,1,1,1,2,2,2,2,2,2),C","degreeBound":0,
  "target":"literal e0","candidate":"slimgb(module)","sourceExtraction":"lift(Original,Target,U,slimgb)",
  "positiveGate":"U=I;10 module products;18 original product;17 original Jacobian transport"}
 binding=sha(canon(sem));mp=a.out/"original-parameter-positive-manifest.json";rp=a.out/"original-parameter-positive-receipt.json"
 state={"format":FORMAT+"-manifest","binding":binding,"semantic":sem,"generation":0,"phases":{},"sourceTexts":[],"parsedSources":[]}
 rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,
  "through":a.through,"completeStableClosureClaimed":False,"nonmembershipClaimed":False,"characteristicZeroConclusion":False,"stages":[]}}
 child=None;code=1
 def save():
  rec["elapsedSeconds"]=time.monotonic()-started
  rec["parameters"]["peakParentRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  rec["parameters"]["peakChildRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
  rec["parameters"]["wholePhaseState"]=state;save_json(rp,rec)
 def checkpoint():
  rec["parameters"]["manifest"]=save_json(mp,state);save()
 def tick():
  if time.monotonic()>=deadline-8:raise Budget("whole parameter-module phase budget")
 def alarm(signum=None,frame=None):raise Budget("actual parameter-module budget or signal")
 signal.signal(signal.SIGTERM,alarm);signal.signal(signal.SIGINT,alarm);signal.signal(signal.SIGALRM,alarm)
 signal.setitimer(signal.ITIMER_REAL,max(.1,a.seconds-7))
 def event(name,**kw):
  z={"phase":name,"elapsedSeconds":time.monotonic()-started,"peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss};z.update(kw)
  rec["parameters"]["lastWholePhase"]=name;print(json.dumps(z,separators=(",",":")),flush=True)
 def checked(d):p=a.out/d["path"];exact(p,d);return p
 def run_stage(name,script):
  nonlocal child
  tick();state["generation"]+=1;checkpoint();g=state["generation"]
  sp=a.out/("%04d-%s.sing"%(g,name));lp=a.out/("%04d-%s.log"%(g,name));atomic(sp,script.encode("ascii"))
  stage={"name":name,"script":identity(sp),"status":"running"};rec["parameters"]["stages"].append(stage);save()
  begin=time.monotonic();budget=False;rc=1
  signal.setitimer(signal.ITIMER_REAL,0)
  try:
   with lp.open("wb") as f:
    child=subprocess.Popen([str(engine),"-q",str(sp)],stdout=f,stderr=subprocess.STDOUT)
    last=time.monotonic()
    while child.poll() is None:
     tick()
     if time.monotonic()-last>=30:
      event(name+"-running",childElapsedSeconds=time.monotonic()-begin,
            completeCandidateSaved="candidate" in state,completeTargetSourceSaved="sourceCandidate" in state)
      last=time.monotonic()
     time.sleep(.2)
    rc=child.returncode;child=None
  except Budget:
   budget=True
   if child is not None and child.poll() is None:
    child.terminate()
    try:child.wait(timeout=3)
    except subprocess.TimeoutExpired:child.kill();child.wait()
   child=None;rc=75
  finally:
   if time.monotonic()<deadline-7:signal.setitimer(signal.ITIMER_REAL,max(.1,deadline-time.monotonic()-7))
  ms,bad=markers(lp)
  with lp.open("rb") as f:f.seek(max(0,lp.stat().st_size-4096));tail=f.read().decode("utf-8",errors="replace")
  stage.update(status="budget" if budget else "returned",exitCode=rc,elapsedSeconds=time.monotonic()-begin,
               log=identity(lp),actualMarkers=ms,diagnosticTail=tail)
  save();need(not bad,"Singular explicit failure "+repr(bad[:3]))
  if not budget:need(rc==0,"Singular actual nonzero exit "+str(rc))
  return {"script":identity(sp),"log":identity(lp),"markers":ms,"budget":budget,"exitCode":rc}
 def phase_save(name,data):
  d=save_gz(a.out/(name+".json.gz"),data,binding);state["phases"][name]=d;checkpoint();return d
 try:
  if mp.exists():
   state=json.loads(mp.read_bytes());need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and state["semantic"]==sem,"same exact positive-source continuation")
  m=module(a.model_source,MODEL_SHA,"original_ten_model");c=module(a.compression_source,COMPRESSION_SHA,"original_seed_compression")
  exact(a.model_out/"original-parameter-module-manifest.json",MODEL_MANIFEST)
  pm=json.loads((a.model_out/"original-parameter-module-manifest.json").read_bytes());pr=json.loads((a.model_out/"original-parameter-module-receipt.json").read_bytes())
  need(pm["binding"]==MODEL_BINDING and pr["binding"]==MODEL_BINDING and pr["status"]=="completed" and pr["source"]["sha256"]==MODEL_SHA and
       pr["parameters"]["all116OriginalSeedsVerified"] and len(pm["seeds"])==116,"complete true original116 parent")
  cm=json.loads((a.compression_out/"complete-parameter-seed-compression-manifest.json").read_bytes())
  cr=json.loads((a.compression_out/"complete-parameter-seed-compression-receipt.json").read_bytes())
  need(cm["binding"]==COMPRESSION_BINDING and cr["binding"]==COMPRESSION_BINDING and cr["status"]=="completed" and
       cr["source"]["sha256"]==COMPRESSION_SHA and cr["parameters"]["all1160ModuleCoordinatesVerified"] and
       cr["parameters"]["allDeletedOriginal18ProductsVerified"] and cr["parameters"]["retainedOriginalSeedCount"]==50,
       "complete same-source50 compression, never a budget prefix")
  exact(a.compression_out/"complete-parameter-seed-compression-manifest.json",cr["parameters"]["manifest"])
  cd=cm["phases"]["complete-original-compressed-parameter-seeds"]
  cp=c.load_gz(a.compression_out/cd["path"],cd,COMPRESSION_BINDING)
  pure={k:cp[k] for k in ("parentBinding","prime","coefficientRoot","allOriginal116SeedExpansionColumns","retainedOriginalSeedIndices")}
  bb=canon(pure);need(len(bb)==COMPRESSION_MATH["bytes"] and sha(bb)==COMPRESSION_MATH["sha256"],"all pure compression mathematics independent of timing metadata")
  need(cp["parentBinding"]==MODEL_BINDING and cp["prime"]==P and cp["coefficientRoot"]==ROOT and
       cp["all1160FinalParameterCoordinatesVerified"] and cp["retainedSourcesArePaidFullOriginal18Sources"],"all parameter columns and their true sources")
  retained=cp["retainedOriginalSeedIndices"];need(len(retained)==len(set(retained))==50,"fifty distinct literal original source columns")
  descs=cp["retainedOriginalSeedDescriptors"];need(len(descs)==50 and all(d==pm["seeds"][i] for d,i in zip(descs,retained)),"same complete parent column payloads")
  base_d=pm["phases"]["complete-original-ten-parameter-action127"];base=m.load_gz(a.model_out/base_d["path"],base_d,MODEL_BINDING)
  chart_d=pm["phases"]["complete-original-global-chart127"];chart=m.load_gz(a.model_out/chart_d["path"],chart_d,MODEL_BINDING)
  A=m.unpackvec(base["allOriginal18Generators"]);old=m.unpackvec(chart["originalComposedGradients"])
  J=[m.unpackvec(row) for row in base["sourceCoordinateChange"]]
  need(len(A)==18 and len(old)==17 and len(J)==17 and all(len(row)==17 for row in J),"all original gradient-source dimensions")
  need(all(m.dot(row,old)==A[i] for i,row in enumerate(J)) and A[17]==m.unpack(chart["originalBellMinusOne"]),"all17 actual original gradient products and Bell equality")
  vectors=[];sources=[]
  for i,d in zip(retained,descs):
   tick();z=m.load_gz(a.model_out/d["path"],d,MODEL_BINDING)
   need(z["seedIndex"]==i and z["fullOriginal18ProductVerified"] and z["allTenParameterCoordinatesRetained"],"same actual complete selected seed")
   v=m.unpackvec(z["vector"]);s=m.unpackvec(z["original18Source"])
   need(len(v)==10 and len(s)==18 and all(not any(e[12:]) for f in v for e in f.to_dict()),"all complete ten parameter coordinates")
   need(m.dot(m.MON,v)==m.dot(A,s),"independent whole original18 product for every retained source")
   vectors.append(v);sources.append(s)
  actual_inputs={"parentManifest":identity(a.model_out/"original-parameter-module-manifest.json"),
   "parentReceipt":identity(a.model_out/"original-parameter-module-receipt.json"),"compressionManifest":identity(a.compression_out/"complete-parameter-seed-compression-manifest.json"),
   "compressionReceipt":identity(a.compression_out/"complete-parameter-seed-compression-receipt.json"),"compressionPhase":cd,
   "pureMathematics":COMPRESSION_MATH,"base":base_d,"chart":chart_d,"retainedOriginalSources":descs}
  if "inputs" in state:need(state["inputs"]==actual_inputs,"same real input descriptors for continued search")
  else:state["inputs"]=actual_inputs;checkpoint()
  event("all-fifty-original-source-products",columns=50,moduleCoordinates=500,originalGeneratorCount=18,all17GradientTransportProducts=True)
  if "asciiModule" not in state:
   lines=ring()+["matrix OM[10][50];"]
   for k,v in enumerate(vectors):
    tick()
    for i,f in enumerate(v):
     if f!=0:lines.append("OM[%d,%d]=%s;"%(i+1,k+1,singular_poly(f)))
   lines += ["module Original=OM;"]
   p=a.out/"complete-original-ten-by-fifty.sing";atomic(p,("\n".join(lines)+"\n").encode("ascii"));state["asciiModule"]=identity(p);checkpoint()
  else:checked(state["asciiModule"])
  rec["parameters"].update(allFiftyOriginal18ProductsVerified=True,all17OriginalGradientTransportProductsVerified=True,
   allParametersRetained=True,parameterCount=12,moduleRows=10,originalSeedColumns=50,actualInputs=actual_inputs,
   vectorTerms=sum(len(f.to_dict()) for v in vectors for f in v),sourceTerms=sum(len(f.to_dict()) for s in sources for f in s))
  if a.through=="prepare":
   rec["status"]="completed-prefix";rec["parameters"]["outcome"]="all-original-fifty-column-inputs-prepared";checkpoint();return 0
  engine=shutil.which(a.singular) if not Path(a.singular).is_file() else str(a.singular)
  need(engine is not None,"actual installed Singular executable");engine=Path(engine).resolve()
  q=subprocess.run([str(engine),"--version"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=15)
  need(q.returncode==0,"actual Singular version probe");version=q.stdout.decode("utf-8",errors="replace")
  ev={"binary":identity(engine),"versionFirstLine":version.splitlines()[0],"wholeVersionSHA256":sha(q.stdout)}
  if "engine" in state:need(state["engine"]==ev,"same actual engine and SSI format")
  else:state["engine"]=ev;atomic(a.out/"actual-singular-version.txt",q.stdout);checkpoint()
  rec["parameters"]["actualEngine"]=ev
  if "selftest" not in state:
   st=run_stage("independent-module-selftest",selftest_script(a.out));ms=st["markers"]
   if not one(ms,"@@MODULE-SELFTEST-COMPLETE",False):
    if st["budget"]:raise Budget("module selftest not complete")
    raise ValueError("missing independent module selftest completion")
   from flint import nmod_mpoly_ctx
   ctx=nmod_mpoly_ctx.get(("x","y"),P,"lex");x,y=ctx.gens();z=ctx.constant(0)
   src=[ctx.from_dict(parse_poly(a.out/("selftest-source-%d.txt"%i),("x","y"))) for i in range(2)]
   need(x*src[0]+(1-x*y)*src[1]==1 and src[0]-y*src[1]==0,"independent FLINT two original module-source products")
   need(ctx.from_dict(parse_poly(a.out/"selftest-parser.txt",("x","y")))==-5*x**4+3*x*y**3+2,"independent expanded polynomial parser")
   state["selftest"]={**st,"allTwoIndependentOriginalProducts":True,
      "files":[identity(a.out/n) for n in ("selftest-module-basis.ssi","selftest-module-source.ssi","selftest-source-0.txt","selftest-source-1.txt","selftest-parser.txt")]}
   checkpoint();event("independent-module-selftest-complete")
  else:
   for d in state["selftest"]["files"]:checked(d)
   checked(state["selftest"]["script"]);checked(state["selftest"]["log"])
  if a.through=="selftest":
   rec["status"]="completed-prefix";rec["parameters"]["outcome"]="independent-module-source-selftest-complete";checkpoint();return 0
  if "originalSSI" not in state:
   st=run_stage("materialize-original-fifty",materialize_script(a.out,checked(state["asciiModule"]).read_text("ascii")))
   if not one(st["markers"],"@@ALL-500-ORIGINAL-MODULE-SSI-COORDINATES",False):
    if st["budget"]:raise Budget("complete original module SSI not yet verified")
    raise ValueError("missing complete original module roundtrip")
   state["originalSSI"]={"data":identity(a.out/"complete-original-ten-by-fifty.ssi"),"evidence":st};checkpoint()
  checked(state["originalSSI"]["data"])
  if "candidate" not in state:
   st=run_stage("slimgb-ten-parameter-module",discovery_script(a.out));end=one(st["markers"],"@@WHOLE-PARAMETER-MODULE-CANDIDATE-SAVED ",False)
   if end is None:
    if st["budget"]:raise Budget("slimgb has not returned a complete SSI candidate")
    raise ValueError("no complete slimgb module candidate")
   n=int(end.split()[-1]);need(n>0,"nonempty complete module candidate")
   state["candidate"]={"data":identity(a.out/"whole-parameter-module-candidate.ssi"),"columns":n,"evidence":st,
                        "independentAllSPairsVerified":False};checkpoint();event("whole-module-candidate-saved",columns=n)
  checked(state["candidate"]["data"])
  if "targetReduction" not in state:
   st=run_stage("literal-e0-reduction",target_script(a.out));end=one(st["markers"],"@@PARAMETER-TARGET-REDUCTION-END ",False)
   if end is None:
    if st["budget"]:raise Budget("literal target reduction incomplete")
    raise ValueError("missing target reduction completion")
   value=int(end.split()[-1]);need(value in (0,1),"literal target boolean")
   files=[identity(a.out/("target-remainder-%02d.txt"%i)) for i in range(10)]
   residual=[parse_poly(a.out/d["path"],PARAMETERS) for d in files]
   need(value==int(all(not q for q in residual)),"all ten independently parsed target remainder coordinates")
   state["targetReduction"]={"zero":bool(value),"files":files,"evidence":st};checkpoint()
  for d in state["targetReduction"]["files"]:checked(d)
  if not state["targetReduction"]["zero"]:
   rec["status"]="completed-diagnostic";rec["parameters"]["outcome"]="initial-parameter-module-candidate-has-nonzero-e0-remainder"
   rec["parameters"]["positiveOriginalIdentityVerified"]=False;checkpoint();return 0
  if "sourceCandidate" not in state:
   st=run_stage("target-only-original-fifty-lift",lift_script(a.out))
   if not one(st["markers"],"@@WHOLE-FIFTY-ORIGINAL-SOURCES-SAVED-UNIT-IDENTITY",False):
    if st["budget"]:raise Budget("target-only source lift not returned complete")
    raise ValueError("missing complete original source candidate")
   state["sourceCandidate"]={"data":identity(a.out/"whole-fifty-original-target-sources.ssi"),"unitsIdentityVerified":True,"evidence":st};checkpoint()
  checked(state["sourceCandidate"]["data"])
  if len(state["sourceTexts"])<50:
   first=len(state["sourceTexts"]);paid=bool(state.get("allTenModuleProductsEvidence"))
   st=run_stage("verify-and-export-target-sources",export_script(a.out,first,paid));ms=st["markers"]
   if one(ms,"@@ALL-TEN-ORIGINAL-MODULE-PRODUCTS-VERIFIED",False):state["allTenModuleProductsEvidence"]=st
   need(state.get("allTenModuleProductsEvidence") or st["budget"],"source export requires complete original module products")
   if state.get("allTenModuleProductsEvidence"):
    for i in range(first,50):
     marker=one(ms,"@@ORIGINAL-SOURCE-TEXT %d "%i,False)
     if marker is None:break
     state["sourceTexts"].append(identity(a.out/("original-source-%02d.txt"%i)))
    checkpoint()
   if len(state["sourceTexts"])<50:
    if st["budget"]:raise Budget("complete source text prefix retained")
    raise ValueError("noncontiguous or incomplete source text export")
   one(ms,"@@ALL-FIFTY-ORIGINAL-SOURCE-TEXTS-SAVED")
  need(state.get("allTenModuleProductsEvidence") and len(state["sourceTexts"])==50,"entire module-source validation gate")
  coefficients=[]
  for i,d in enumerate(state["sourceTexts"]):
   tick();p=checked(d);name="verified-source-coefficient-%02d"%i
   if i<len(state["parsedSources"]):data=load_gz(a.out/state["parsedSources"][i]["path"],state["parsedSources"][i],binding)
   else:
    pp=parse_poly(p,PARAMETERS);f=m.CTX.from_dict({e+(0,)*5:c for e,c in pp.items()})
    data={"retainedColumn":i,"originalSeedIndex":retained[i],"sourceText":d,"coefficient":m.pack(f)}
    z=save_gz(a.out/(name+".json.gz"),data,binding);state["parsedSources"].append(z);checkpoint()
   need(data["retainedColumn"]==i and data["originalSeedIndex"]==retained[i] and data["sourceText"]==d,"same whole original source coefficient")
   coefficients.append(m.unpack(data["coefficient"]))
  for axis in range(10):
   name="complete-module-product-%02d"%axis
   if name not in state["phases"]:
    tick();v=sum((coefficients[k]*vectors[k][axis] for k in range(50)),m.ZERO)
    need(v==(m.ONE if axis==0 else m.ZERO),"independent full ten-coordinate original source product")
    phase_save(name,{"axis":axis,"allFiftyOriginalSourcesUsed":True,"targetCoordinate":int(axis==0),"productVerified":True})
   else:load_gz(a.out/state["phases"][name]["path"],state["phases"][name],binding)
  original_sources=[]
  for j in range(18):
   name="complete-original-source-%02d"%j
   if name in state["phases"]:data=load_gz(a.out/state["phases"][name]["path"],state["phases"][name],binding)
   else:
    tick();f=sum((coefficients[k]*sources[k][j] for k in range(50)),m.ZERO)
    data={"originalGenerator":j,"source":m.pack(f)};phase_save(name,data)
   need(data["originalGenerator"]==j,"same literal original18 generator");original_sources.append(m.unpack(data["source"]))
  tick();need(m.dot(A,original_sources)==m.ONE,"complete original18 polynomial product equals one")
  event("all-original18-polynomial-product-one",sourceTerms=sum(len(f.to_dict()) for f in original_sources))
  old_sources=[]
  for i in range(17):
   name="complete-original-gradient-source-%02d"%i
   if name in state["phases"]:data=load_gz(a.out/state["phases"][name]["path"],state["phases"][name],binding)
   else:
    tick();f=sum((original_sources[j]*J[j][i] for j in range(17)),m.ZERO)
    data={"originalPhysicalGradient":i,"sourceInGlobalChart":m.pack(f)};phase_save(name,data)
   need(data["originalPhysicalGradient"]==i,"same complete original physical gradient");old_sources.append(m.unpack(data["sourceInGlobalChart"]))
  tick();need(m.dot(old,old_sources)+A[17]*original_sources[17]==m.ONE,"independent complete original physical17 plus Bell polynomial product")
  cert={"prime":P,"coefficientRoot":ROOT,"allParametersRetained":True,"allFiftyCoefficients":m.packvec(coefficients),
   "allOriginal18Sources":m.packvec(original_sources),"allOriginal17PhysicalSourcesInGlobalChart":m.packvec(old_sources),
   "originalBellMinusOneSource":m.pack(original_sources[17]),"originalGradientTransport":base["sourceCoordinateChange"],
   "coordinateInverse":base["coordinateInverse"],"coordinateForwardOriginalContext":base["coordinateForwardOriginalContext"],
   "literalOldSourceSLP":"replace all new variables by coordinateForwardOriginalContext in the listed sources",
   "allTenOriginalModuleProductsVerified":True,"allOriginal18PolynomialProductVerified":True,
   "allOriginalPhysical17PlusBellProductVerified":True,"noAllSPairsOrStableClosureNeededForPositiveIdentity":True,
   "characteristicZeroLiftVerified":False,"allOriginalInputs":actual_inputs}
  d=phase_save("complete-original-field-unit-source-certificate",cert)
  rec["status"]="completed-positive";rec["parameters"].update(outcome="original-field127-unit-identity-with-complete-sources",
   positiveOriginalIdentityVerified=True,allTenIndependentModuleProductsVerified=True,
   allOriginal18IndependentPolynomialProductVerified=True,allOriginal17PhysicalPlusBellProductVerified=True,certificate=d)
  checkpoint();return 0
 except Budget as e:
  rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75
 except BaseException as e:
  rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0)
  if child is not None and child.poll() is None:
   child.terminate()
   try:child.wait(timeout=3)
   except subprocess.TimeoutExpired:child.kill();child.wait()
  checkpoint();print(canon(rec).decode("ascii"),flush=True)
 return code
if __name__=="__main__":raise SystemExit(main())
