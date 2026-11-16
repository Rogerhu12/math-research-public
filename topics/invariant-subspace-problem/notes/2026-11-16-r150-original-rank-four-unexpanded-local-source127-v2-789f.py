#!/usr/bin/env python3
"""Source-certified rank-four Bell chart over the actual F127,d=100 model.

Author: ChatGPT (AI), literature_audit. 2026-11-16 UTC.
Keep the ten literal generators. On one rank-four mean chart, four Bell
columns are redundant by a source-checked adjugate identity. The remaining
forty-six literal columns and ten localizers avoid expanded Schur entries.
This initial parameter submodule is not asserted stable or complete.
Only a fully checked original18 identity delta**N is a positive conclusion.
Every localizer denominator is cleared; no E/characteristic-zero lift is assumed.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,itertools,json,os,re,resource,shutil,signal,subprocess,sys,time
from pathlib import Path
sys.set_int_max_str_digits(0)
FORMAT="r150-original-rank-four-unexpanded-local-source127-v2"
P=127;ROOT=100
MODEL_SHA="4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4"
COMPRESS_SHA="b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9"
MODEL_BINDING="7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4"
MODEL_MANIFEST={"bytes":30466,"sha256":"9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2"}
COMPRESS_BINDING="baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca"
COMPRESS_MATH={"bytes":620742,"sha256":"a1d73ea1ce5809c87bdc34724c1eb4407d6a5c0ae78fbf16aa3650563aa089dd"}
NAMES=tuple(["y%d"%i for i in range(6)]+["w%d"%i for i in range(6)]+["rho"])
MAX_TEXT=64*1024*1024
class Budget(Exception):pass
def need(v,s):
 if not v:raise ValueError(s)
def canon(v):return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 p=Path(p);h=hashlib.sha256()
 with p.open("rb") as f:
  for z in iter(lambda:f.read(1048576),b""):h.update(z)
 return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact(p,d):
 v=identity(p);need(v["bytes"]==d["bytes"] and v["sha256"]==d["sha256"],"whole exact file "+p.name);return v
def atomic(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
def save_json(p,x):atomic(p,canon(x));return identity(p)
def save_gz(p,x,binding):
 b=canon({"format":FORMAT+"-phase","binding":binding,"data":x});atomic(p,gzip.compress(b,compresslevel=1,mtime=0))
 return {**identity(p),"logicalBytes":len(b),"logicalSha256":sha(b)}
def load_gz(p,d,binding):
 exact(p,d);need(d["bytes"]<=128*1024*1024 and d["logicalBytes"]<=512*1024*1024,"bounded whole polynomial phase")
 b=gzip.decompress(p.read_bytes());need(len(b)==d["logicalBytes"] and sha(b)==d["logicalSha256"],"whole logical phase")
 v=json.loads(b);need(v["format"]==FORMAT+"-phase" and v["binding"]==binding,"same child polynomial phase");return v["data"]
def module(p,h,name):
 need(identity(p)["sha256"]==h,"exact helper source "+name)
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def permutation_sign(p):return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1
def det(A,m):
 n=len(A);need(n<=4 and all(len(r)==n for r in A),"literal small square determinant")
 v=m.ZERO
 for pp in itertools.permutations(range(n)):
  t=m.ONE
  for i,j in enumerate(pp):t*=A[i][j]
  v+=permutation_sign(pp)*t
 return v
def adj(A,m):
 n=len(A)
 return [[(-1)**(i+j)*det([[A[a][b] for b in range(n) if b!=i] for a in range(n) if a!=j],m) for j in range(n)] for i in range(n)]
def mm(A,B,m):
 need(A and B and all(len(r)==len(B) for r in A) and len({len(r) for r in B})==1,"full small matrix product shape")
 return [[sum((a*B[k][j] for k,a in enumerate(r)),m.ZERO) for j in range(len(B[0]))] for r in A]
def packmat(A,m):return [m.packvec(r) for r in A]
def unpackmat(A,m):return [m.unpackvec(r) for r in A]
def same(A,B):return len(A)==len(B) and all(len(a)==len(b) and all(x==y for x,y in zip(a,b)) for a,b in zip(A,B))
def ss(p,mode=""):
 s=str(p);need(not any(c in s for c in ('"',"\\","\r","\n")),"safe literal Singular path");return '"'+mode+s+'"'
def polytext(f):
 parts=[]
 for e,c in sorted(f.to_dict().items()):
  need(len(e)==17 and not any(e[12:]) and 0<int(c)<P,"complete parameter-only coefficient")
  mon="*".join(n+("^%d"%k if k!=1 else "") for n,k in zip(NAMES[:12],e[:12]) if k)
  parts.append(str(int(c))+("*"+mon if mon else ""))
 return "+".join(parts) if parts else "0"
def parse_poly(path,names):
 need(path.stat().st_size<=MAX_TEXT,"one expanded coefficient obeys explicit text limit")
 s="".join(path.read_text(encoding="ascii").split())
 if s=="0":return {}
 need(s and s[0] not in "*^","complete expanded polynomial text")
 terms=re.findall(r"[+-]?[^+-]+",s);need("".join(terms)==s,"whole polynomial token coverage")
 where={n:i for i,n in enumerate(names)};out={}
 for t in terms:
  c=1
  if t[0] in "+-":
   if t[0]=="-":c=-1
   t=t[1:]
  need(t,"nonempty signed monomial");e=[0]*len(names)
  for f in t.split("*"):
   if f.isdigit():c=c*int(f)%P;continue
   z=f.split("^");need(len(z)<=2 and z[0] in where,"only declared original parameter or localizer")
   need(len(z)==1 or z[1].isdigit(),"nonnegative integer exponent")
   e[where[z[0]]]+=1 if len(z)==1 else int(z[1])
  e=tuple(e);out[e]=(out.get(e,0)+c)%P
 return {e:c for e,c in out.items() if c}
def ring():
 return ["ring r=127,("+",".join(NAMES)+"),(wp(1,1,1,1,1,1,2,2,2,2,2,2,1),C);","short=0; degBound=0; option(redSB); option(redTail);"]
def original_lines(out):
 return ring()+["def Original=read("+ss(out/"literal-ten-by-fifty-six.ssi","ssi:r ")+");",
 'if(ncols(Original)!=56){print("@@FAIL original56-shape");quit;}',
 "matrix OM[10][56]=Original; matrix TM[10][1]; TM[1,1]=1; module Target=TM;"]
def markers(path):
 good=[];bad=[]
 with path.open("r",encoding="utf-8",errors="replace") as f:
  for line in f:
   s=line.strip()
   if s.startswith("@@"):good.append(s)
   if s.startswith("@@FAIL") or s.startswith("?"):bad.append(s[:600])
 need(len(good)<=10000 and len(bad)<=10000,"bounded complete marker transcript");return good,bad
def one(ms,prefix,required=True):
 x=[s for s in ms if s.startswith(prefix)];need(len(x)<=1,"unique completion marker "+prefix)
 if required:need(len(x)==1,"complete marker "+prefix)
 return x[0] if x else None
def main():
 ap=argparse.ArgumentParser()
 for n in ("model-source","model-out","compression-source","compression-out","out"):ap.add_argument("--"+n,type=Path,required=True)
 ap.add_argument("--chart",default="sparsest",help="lexicographic index 0..14, or sparsest by literal minor then adjugate term counts")
 ap.add_argument("--singular",default="Singular");ap.add_argument("--through",choices=("prepare","selftest","final"),default="prepare")
 ap.add_argument("--seconds",type=float,default=300);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args();need(0<a.seconds<=1800 and 512<=a.memory_mib<=6144,"explicit local source budget")
 need(a.chart=="sparsest" or a.chart.isdigit() and 0<=int(a.chart)<15,"literal original mean-row chart")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 begun=time.monotonic();deadline=begun+a.seconds;a.out.mkdir(parents=True,exist_ok=True)
 own=identity(Path(__file__))
 semantic={"format":FORMAT,"source":own,"modelSourceSHA256":MODEL_SHA,"compressionSourceSHA256":COMPRESS_SHA,
  "modelBinding":MODEL_BINDING,"modelManifest":MODEL_MANIFEST,"compressionBinding":COMPRESS_BINDING,"compressionMathematics":COMPRESS_MATH,
  "prime":P,"coefficientRoot":ROOT,"chart":a.chart,"chartDictionary":"lexicographic four subsets of the six literal mean columns",
  "selection":"nonzero determinant: minimum (minor terms, adjugate terms, four-row tuple)","keptGeneratorAxes":list(range(10)),
  "rankFourMeanPivotAxes":list(range(6,10)),"parentColumns":50,"literalColumns":46,"localizerColumns":10,
  "parameters":NAMES,"ordering":"wp(1,1,1,1,1,1,2,2,2,2,2,2,1),C","completeStableClosureClaimed":False,
  "positiveGate":"all4 Bell removal source identities; full10 localized product; denominator clearing; full10 original seeds; original18 product; original17 Jacobian transport",
  "EUnitIdentityClaimed":False,"expandedCoefficientTextLimit":MAX_TEXT}
 binding=sha(canon(semantic));mp=a.out/"rank-four-local-source-manifest.json";rp=a.out/"rank-four-local-source-receipt.json"
 state={"format":FORMAT+"-manifest","binding":binding,"semantic":semantic,"generation":0,"phases":{},"sourceTexts":[]}
 rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,"through":a.through,
  "stages":[],"nonmembershipClaimed":False,"completeCriticalQuotientClaimed":False,"characteristicZeroConclusion":False}}
 child=None;code=1
 def tick():
  if time.monotonic()>=deadline-8:raise Budget("rank-four actual source budget")
 def flush():
  rec["parameters"]["manifest"]=save_json(mp,state);rec["elapsedSeconds"]=time.monotonic()-begun
  rec["parameters"]["parentPeakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  rec["parameters"]["childPeakRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss;save_json(rp,rec)
 def event(name,**kw):
  z={"phase":name,"elapsedSeconds":time.monotonic()-begun};z.update(kw);rec["parameters"]["lastWholePhase"]=name;print(canon(z).decode(),flush=True)
 def alarm(*unused):raise Budget("rank-four actual signal budget")
 def phase(name,data):
  d=save_gz(a.out/(name+".json.gz"),data,binding);state["phases"][name]=d;flush();return d
 def read_phase(name):return load_gz(a.out/state["phases"][name]["path"],state["phases"][name],binding)
 def checked(d):p=a.out/d["path"];exact(p,d);return p
 def run(name,lines):
  nonlocal child
  tick();state["generation"]+=1;g=state["generation"];flush()
  sp=a.out/("%04d-%s.sing"%(g,name));lp=a.out/("%04d-%s.log"%(g,name))
  atomic(sp,("\n".join(lines)+"\n").encode("ascii"));stage={"name":name,"script":identity(sp),"status":"running"}
  rec["parameters"]["stages"].append(stage);flush();start=time.monotonic();budget=False;rc=1
  signal.setitimer(signal.ITIMER_REAL,0)
  try:
   with lp.open("wb") as f:
    child=subprocess.Popen([str(engine),"-q",str(sp)],stdout=f,stderr=subprocess.STDOUT);last=time.monotonic()
    while child.poll() is None:
     tick()
     if time.monotonic()-last>=30:event(name+"-running",childSeconds=time.monotonic()-start);last=time.monotonic()
     time.sleep(.2)
    rc=child.returncode;child=None
  except Budget:
   budget=True;rc=75
   if child is not None and child.poll() is None:
    child.terminate()
    try:child.wait(timeout=3)
    except subprocess.TimeoutExpired:child.kill();child.wait()
   child=None
  finally:
   if time.monotonic()<deadline-7:signal.setitimer(signal.ITIMER_REAL,max(.1,deadline-time.monotonic()-7))
  ms,bad=markers(lp)
  with lp.open("rb") as f:f.seek(max(0,lp.stat().st_size-4096));tail=f.read().decode(errors="replace")
  stage.update(status="budget" if budget else "returned",exitCode=rc,elapsedSeconds=time.monotonic()-start,log=identity(lp),markers=ms,tail=tail);flush()
  need(not bad,"actual Singular failure "+repr(bad[:3]))
  if not budget:need(rc==0,"actual Singular nonzero exit "+str(rc))
  return {"script":identity(sp),"log":identity(lp),"markers":ms,"budget":budget,"exitCode":rc}
 signal.signal(signal.SIGTERM,alarm);signal.signal(signal.SIGINT,alarm);signal.signal(signal.SIGALRM,alarm)
 signal.setitimer(signal.ITIMER_REAL,max(.1,a.seconds-7))
 try:
  if mp.exists():
   state=json.loads(mp.read_bytes());need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and state["semantic"]==semantic,"same exact local source continuation")
  m=module(a.model_source,MODEL_SHA,"rank4_original_model");c=module(a.compression_source,COMPRESS_SHA,"rank4_original_compression")
  exact(a.model_out/"original-parameter-module-manifest.json",MODEL_MANIFEST)
  pm=json.loads((a.model_out/"original-parameter-module-manifest.json").read_bytes());pr=json.loads((a.model_out/"original-parameter-module-receipt.json").read_bytes())
  need(pm["binding"]==MODEL_BINDING and pr["binding"]==MODEL_BINDING and pr["status"]=="completed" and pr["source"]["sha256"]==MODEL_SHA and
       pr["parameters"]["all116OriginalSeedsVerified"] and len(pm["seeds"])==116,"complete verified original116 parent")
  cm=json.loads((a.compression_out/"complete-parameter-seed-compression-manifest.json").read_bytes());cr=json.loads((a.compression_out/"complete-parameter-seed-compression-receipt.json").read_bytes())
  need(cm["binding"]==COMPRESS_BINDING and cr["binding"]==COMPRESS_BINDING and cr["status"]=="completed" and cr["source"]["sha256"]==COMPRESS_SHA and
       cr["parameters"]["all1160ModuleCoordinatesVerified"] and cr["parameters"]["allDeletedOriginal18ProductsVerified"] and cr["parameters"]["retainedOriginalSeedCount"]==50,
       "complete source-preserving original50 compression")
  exact(a.compression_out/"complete-parameter-seed-compression-manifest.json",cr["parameters"]["manifest"])
  cd=cm["phases"]["complete-original-compressed-parameter-seeds"];cp=c.load_gz(a.compression_out/cd["path"],cd,COMPRESS_BINDING)
  bb=canon({k:cp[k] for k in ("parentBinding","prime","coefficientRoot","allOriginal116SeedExpansionColumns","retainedOriginalSeedIndices")})
  need(len(bb)==COMPRESS_MATH["bytes"] and sha(bb)==COMPRESS_MATH["sha256"],"all pure original compression mathematics")
  need(cp["parentBinding"]==MODEL_BINDING and cp["prime"]==P and cp["coefficientRoot"]==ROOT and cp["all1160FinalParameterCoordinatesVerified"] and
       cp["retainedSourcesArePaidFullOriginal18Sources"],"original coefficient place and source scope")
  retained=cp["retainedOriginalSeedIndices"];descs=cp["retainedOriginalSeedDescriptors"]
  need(len(retained)==len(set(retained))==50 and retained[:6]==list(range(100,106)) and len(descs)==50 and
       all(d==pm["seeds"][i] for d,i in zip(descs,retained)),"fifty literal parent columns including all six mean sources")
  bd=pm["phases"]["complete-original-ten-parameter-action127"];base=m.load_gz(a.model_out/bd["path"],bd,MODEL_BINDING)
  hd=pm["phases"]["complete-original-global-chart127"];oldchart=m.load_gz(a.model_out/hd["path"],hd,MODEL_BINDING)
  original=m.unpackvec(base["allOriginal18Generators"]);old=m.unpackvec(oldchart["originalComposedGradients"]);J=unpackmat(base["sourceCoordinateChange"],m)
  need(len(original)==18 and len(old)==17 and len(J)==17 and all(len(row)==17 for row in J),"complete original source dimensions")
  need(all(m.dot(row,old)==original[i] for i,row in enumerate(J)) and original[17]==m.unpack(oldchart["originalBellMinusOne"]),"all original seventeen-gradient transports and Bell identity")
  vectors=[];sources=[]
  for i,d in zip(retained,descs):
   tick();z=m.load_gz(a.model_out/d["path"],d,MODEL_BINDING)
   need(z["seedIndex"]==i and z["fullOriginal18ProductVerified"] and z["allTenParameterCoordinatesRetained"],"whole selected literal source")
   v=m.unpackvec(z["vector"]);s=m.unpackvec(z["original18Source"])
   need(len(v)==10 and len(s)==18 and all(not any(e[12:]) for f in v for e in f.to_dict()),"all parameter-only ten-coordinate columns")
   need(m.dot(m.MON,v)==m.dot(original,s),"whole original eighteen-generator product")
   vectors.append(v);sources.append(s)
  inputs={"modelManifest":identity(a.model_out/"original-parameter-module-manifest.json"),"modelReceipt":identity(a.model_out/"original-parameter-module-receipt.json"),
   "compressionManifest":identity(a.compression_out/"complete-parameter-seed-compression-manifest.json"),"compressionReceipt":identity(a.compression_out/"complete-parameter-seed-compression-receipt.json"),
   "compressionPhase":cd,"modelPhase":bd,"originalChartPhase":hd,"retainedParentIndices":retained,"retainedParentPhases":descs}
  if "inputs" in state:need(state["inputs"]==inputs,"same actual parent files and recipes")
  else:state["inputs"]=inputs;flush()
  T=base["allFourOriginalMeanMatrices"]
  need(len(T)==4 and all(len(t)==6 and all(len(row)==6 for row in t) for t in T),"four original mean matrices")
  for a0 in range(4):
   need(all(T[a0][i][j]==T[a0][j][i] for i in range(6) for j in range(6)),"literal symmetric mean matrix")
   for i in range(6):need(vectors[i][6+a0]==sum((int(T[a0][i][j])*m.Y[j] for j in range(6)),m.ZERO),"all24 mean-quadratic columns are the actual original pencil")
  need(base["parameterNames"]==list(NAMES[:12]),"all twelve parameter labels")
  event("all-original-fifty-seeds-and-full-source-transport",originalProducts=50,originalJacobianProducts=17)
  name="complete-original-rank-four-unexpanded-input"
  if name in state["phases"]:
   chart=read_phase(name);rows=chart["originalMeanRows"];delta=m.unpack(chart["delta"])
   charts=chart["allFifteenLiteralMinorStatistics"];ci=chart["chartIndex"]
   A=unpackmat(chart["pivotMatrix"],m);adjA=unpackmat(chart["adjugate"],m)
  else:
   charts=[];allrows=list(itertools.combinations(range(6),4));saved={}
   for ci,rows0 in enumerate(allrows):
    tick();AA=[[vectors[j][6+i] for j in rows0] for i in range(4)];dd=det(AA,m);ad=adj(AA,m)
    need(same(mm(AA,ad,m),[[dd if i==j else m.ZERO for j in range(4)] for i in range(4)]) and
         same(mm(ad,AA,m),[[dd if i==j else m.ZERO for j in range(4)] for i in range(4)]),"both full original four-by-four adjugate products")
    stats={"chartIndex":ci,"originalMeanRows":list(rows0),"nonzero":dd!=0,"minorTerms":len(dd.to_dict()),"adjugateTerms":sum(len(f.to_dict()) for row in ad for f in row),"minorLogicalSHA256":sha(canon(m.pack(dd)))}
    charts.append(stats);saved[ci]=(AA,dd,ad)
   admissible=[q for q in charts if q["nonzero"]];need(admissible,"at least one actual nonzero original rank-four minor")
   ci=min(admissible,key=lambda q:(q["minorTerms"],q["adjugateTerms"],q["originalMeanRows"]))["chartIndex"] if a.chart=="sparsest" else int(a.chart)
   need(charts[ci]["nonzero"],"selected literal minor is nonzero at the legal coefficient place")
   rows=list(allrows[ci]);A,delta,adjA=saved[ci]
  need(len(rows)==4 and rows==list(list(itertools.combinations(range(6),4))[ci]) and delta!=0,"same literal original rank-four chart")
  need(same(A,[[vectors[j][6+i] for j in rows] for i in range(4)]) and det(A,m)==delta and same(adj(A,m),adjA),"saved original four-column indices and determinant")
  C=[[vectors[j][i] for j in rows] for i in range(6)];CA=mm(C,adjA,m)
  bell=original[17];bellPositions=[retained.index(106+i) for i in range(10)]
  for i,j in enumerate(bellPositions):
   need(all(vectors[j][k]==(bell if k==i else m.ZERO) for k in range(10)),"all ten literal Bell parameter columns")
  removed=bellPositions[6:];keep=[j for j in range(50) if j not in removed]
  need(len(set(removed))==4 and len(keep)==46 and all(j in keep for j in rows+bellPositions[:6]),"retain all four mean pivots and six low Bell columns")
  removal=[]
  for k,j in enumerate(removed):
   tick();coeff=[m.ZERO for _ in range(50)]
   for l,q in enumerate(rows):coeff[q]=adjA[l][k]*bell
   for i,q in enumerate(bellPositions[:6]):coeff[q]-=CA[i][k]
   need(all(coeff[q]==0 for q in removed),"Bell relation uses only the retained original columns")
   for i in range(10):need(sum((coeff[q]*vectors[q][i] for q in keep),m.ZERO)==delta*vectors[j][i],"all forty original Bell removal module coordinates")
   sig=[sum((coeff[q]*sources[q][i] for q in keep),m.ZERO) for i in range(18)]
   need(m.dot(original,sig)==delta*m.dot(original,sources[j]),"all four complete original eighteen-generator Bell removal products")
   removal.append({"removedParentPosition":j,"originalSeedIndex":retained[j],"coefficientLogicalSHA256":sha(canon(m.packvec(coeff))),"source18LogicalSHA256":sha(canon(m.packvec(sig)))})
  M=[[vectors[j][i] for j in keep] for i in range(10)]
  info={"chartIndex":ci,"originalMeanRows":rows,"allFifteenLiteralMinorStatistics":charts,
   "retainedParentPositions":keep,"retainedOriginalSeedIndices":[retained[j] for j in keep],"discardedBellParentPositions":removed,
   "delta":m.pack(delta),"pivotMatrix":packmat(A,m),"adjugate":packmat(adjA,m),"fourBellRemovalIdentities":removal,
   "all480AdjugateCoordinatesVerified":True,"all40OriginalBellRemovalCoordinatesVerified":True,
   "all4Original18BellRemovalProductsVerified":True,"allFiftyOriginal18ProductsVerified":True,"all17OriginalGradientTransportsVerified":True,
   "localizedInitialModuleEqualityVerified":True,"fullSchurMatrixMaterialized":False,
   "completeCriticalPresentationClaimed":False,"characteristicZeroUnitClaimed":False}
  if name in state["phases"]:need(info==chart,"same complete literal unexpanded input and repeated source verification")
  else:phase(name,info)
  rec["parameters"].update(chartIndex=ci,originalMeanRows=rows,deltaLogicalSHA256=sha(canon(m.pack(delta))),deltaTerms=len(delta.to_dict()),
   allFifteenLiteralMinorStatistics=charts,moduleShape=[10,46],localizedShape=[10,56],
   moduleTerms=sum(len(f.to_dict()) for row in M for f in row),all40OriginalBellRemovalCoordinatesVerified=True,
   all4Original18BellRemovalProductsVerified=True,localizedInitialModuleEqualityVerified=True,fullSchurMatrixMaterialized=False,
   all50Original18ProductsVerified=True,all17OriginalGradientTransportsVerified=True,originalInputs=inputs)
  event("complete-original-unexpanded-local-module",chartIndex=ci,originalMeanRows=rows,deltaTerms=len(delta.to_dict()),moduleTerms=rec["parameters"]["moduleTerms"])
  if "asciiModule" not in state:
   p=a.out/"literal-ten-by-fifty-six.sing";tmp=p.with_name(p.name+".tmp")
   with tmp.open("w",encoding="ascii",newline="\n") as f:
    for line in ring()+["matrix OM[10][56];"]:f.write(line+"\n")
    for i in range(10):
     for k in range(46):
      tick()
      if M[i][k]!=0:f.write("OM[%d,%d]=%s;\n"%(i+1,k+1,polytext(M[i][k])))
    f.write("poly Delta="+polytext(delta)+";\n")
    for i in range(10):f.write("OM[%d,%d]=rho*Delta-1;\n"%(i+1,47+i))
    f.write("module Original=OM;\n")
   os.replace(tmp,p);state["asciiModule"]=identity(p);flush()
  else:checked(state["asciiModule"])
  if a.through=="prepare":rec["status"]="completed-prefix";rec["parameters"]["outcome"]="all-original-rank-four-source-inputs-prepared";flush();return 0
  engine=shutil.which(a.singular) if not Path(a.singular).is_file() else str(a.singular);need(engine is not None,"actual installed Singular executable")
  engine=Path(engine).resolve();v=subprocess.run([str(engine),"--version"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=15)
  need(v.returncode==0,"actual Singular version response");ev={"binary":identity(engine),"versionFirstLine":v.stdout.decode(errors="replace").splitlines()[0],"wholeVersionSHA256":sha(v.stdout)}
  if "engine" in state:need(state["engine"]==ev,"same actual engine and SSI protocol")
  else:state["engine"]=ev;atomic(a.out/"actual-singular-version.txt",v.stdout);flush()
  if "selftest" not in state:
   lines=["ring r=127,(x,z),(dp,C); short=0; degBound=0; option(redSB);",
    "matrix A[2][3]; A[1,1]=x; A[2,2]=x; A[1,3]=x*z-1; module Original=A;",
    "matrix T[2][1]; T[1,1]=1; module Target=T; module G=slimgb(Original);",
    'if(reduce(Target[1],G)!=0){print("@@FAIL local-selftest-positive");quit;}',
    'vector Guard=[0,1]; if(reduce(Guard,G)==0){print("@@FAIL local-selftest-negative");quit;}',
    'matrix Units; matrix Sources=lift(Original,Target,Units,"slimgb");',
    'if(nrows(Sources)!=3 || ncols(Sources)!=1 || nrows(Units)!=1 || ncols(Units)!=1 || Units[1,1]!=1){print("@@FAIL local-selftest-source");quit;}',
    'matrix R=A*Sources-T; if(R[1,1]!=0 || R[2,1]!=0){print("@@FAIL local-selftest-product");quit;}']
   for i in range(3):lines.append("write("+ss(a.out/("selftest-source-%d.txt"%i),":w ")+",Sources[%d,1]);"%(i+1))
   lines+=['print("@@LOCAL-SOURCE-SELFTEST-COMPLETE");quit;'];st=run("local-source-selftest",lines)
   if not one(st["markers"],"@@LOCAL-SOURCE-SELFTEST-COMPLETE",False):
    if st["budget"]:raise Budget("local source selftest incomplete")
    raise ValueError("missing local source selftest marker")
   from flint import nmod_mpoly_ctx
   ctx=nmod_mpoly_ctx.get(("x","z"),P,"lex");xx,zz=ctx.gens();cc=[ctx.from_dict(parse_poly(a.out/("selftest-source-%d.txt"%i),("x","z"))) for i in range(3)]
   need(xx*cc[0]+(xx*zz-1)*cc[2]==1 and xx*cc[1]==0,"independent complete localizer selftest products")
   state["selftest"]={"evidence":st,"allProductsVerified":True,"files":[identity(a.out/("selftest-source-%d.txt"%i)) for i in range(3)]};flush()
  else:
   for d in state["selftest"]["files"]:checked(d)
  if a.through=="selftest":rec["status"]="completed-prefix";rec["parameters"]["outcome"]="local-source-selftest-completed";flush();return 0
  if "originalSSI" not in state:
   lines=checked(state["asciiModule"]).read_text("ascii").splitlines()+["write("+ss(a.out/"literal-ten-by-fifty-six.ssi","ssi:w ")+",Original);",
    "def Copy=read("+ss(a.out/"literal-ten-by-fifty-six.ssi","ssi:r ")+");",
    'if(ncols(Copy)!=56){print("@@FAIL local-SSI-shape");quit;} matrix CM[10][56]=Copy; int i; int j;',
    'for(i=1;i<=10;i++){for(j=1;j<=56;j++){if(CM[i,j]!=OM[i,j]){print("@@FAIL local-SSI-product");quit;}}}',
    'print("@@ALL-560-LOCAL-SSI-PRODUCTS");quit;']
   st=run("materialize-original-localized-module",lines)
   if not one(st["markers"],"@@ALL-560-LOCAL-SSI-PRODUCTS",False):
    if st["budget"]:raise Budget("whole localized original SSI incomplete")
    raise ValueError("missing complete local SSI marker")
   state["originalSSI"]={"data":identity(a.out/"literal-ten-by-fifty-six.ssi"),"evidence":st};flush()
  checked(state["originalSSI"]["data"])
  if "candidate" not in state:
   lines=original_lines(a.out)+['print("@@LOCAL-SLIMGB-START");module G=slimgb(Original);',
    'print("@@LOCAL-SLIMGB-RETURN "+string(ncols(G)));',"write("+ss(a.out/"whole-local-candidate.ssi","ssi:w ")+",G);",
    "def Copy=read("+ss(a.out/"whole-local-candidate.ssi","ssi:r ")+");",
    'if(ncols(Copy)!=ncols(G)){print("@@FAIL local-candidate-SSI-shape");quit;} int i;',
    'for(i=1;i<=ncols(G);i++){if(Copy[i]!=G[i]){print("@@FAIL local-candidate-SSI-product");quit;}}',
    'print("@@WHOLE-LOCAL-CANDIDATE-SAVED "+string(ncols(G)));quit;']
   st=run("unexpanded-ten-row-local-slim-groebner-candidate",lines);end=one(st["markers"],"@@WHOLE-LOCAL-CANDIDATE-SAVED ",False)
   if end is None:
    if st["budget"]:raise Budget("candidate engine has no complete saved basis; no partial GB is reusable")
    raise ValueError("missing complete local candidate")
   n=int(end.split()[-1]);need(n>0,"nonempty complete local candidate")
   state["candidate"]={"data":identity(a.out/"whole-local-candidate.ssi"),"columns":n,"evidence":st,"allSPairsIndependentlyVerified":False};flush()
  checked(state["candidate"]["data"])
  if "targetReduction" not in state:
   lines=original_lines(a.out)+["def G=read("+ss(a.out/"whole-local-candidate.ssi","ssi:r ")+");","vector residual=reduce(Target[1],G);"]
   for i in range(10):lines.append("write("+ss(a.out/("local-remainder-%d.txt"%i),":w ")+",residual[%d]);"%(i+1))
   lines+=['print("@@LOCAL-TARGET-REDUCTION "+string(residual==0));quit;'];st=run("literal-local-e0-reduction",lines)
   end=one(st["markers"],"@@LOCAL-TARGET-REDUCTION ",False)
   if end is None:
    if st["budget"]:raise Budget("local target reduction incomplete")
    raise ValueError("missing local target reduction")
   bit=int(end.split()[-1]);need(bit in (0,1),"literal local remainder boolean")
   files=[identity(a.out/("local-remainder-%d.txt"%i)) for i in range(10)]
   need(bit==int(all(not parse_poly(a.out/d["path"],NAMES) for d in files)),"all ten parsed local remainders")
   state["targetReduction"]={"zero":bool(bit),"files":files,"evidence":st};flush()
  for d in state["targetReduction"]["files"]:checked(d)
  if not state["targetReduction"]["zero"]:
   rec["status"]="completed-diagnostic";rec["parameters"]["outcome"]="nonzero-local-candidate-remainder-only";flush();return 0
  if "sourceCandidate" not in state:
   lines=original_lines(a.out)+['matrix Units; matrix Sources=lift(Original,Target,Units,"slimgb");',
    'if(nrows(Sources)!=56 || ncols(Sources)!=1){print("@@FAIL local-source-shape");quit;}',
    'if(nrows(Units)!=1 || ncols(Units)!=1 || Units[1,1]!=1){print("@@FAIL local-source-unit");quit;}',
    "write("+ss(a.out/"whole-local-source.ssi","ssi:w ")+",Sources);","def Copy=read("+ss(a.out/"whole-local-source.ssi","ssi:r ")+");",
    'if(nrows(Copy)!=56 || ncols(Copy)!=1){print("@@FAIL local-source-SSI-shape");quit;} int i;',
    'for(i=1;i<=56;i++){if(Copy[i,1]!=Sources[i,1]){print("@@FAIL local-source-SSI-product");quit;}}',
    'print("@@WHOLE-LOCAL-SOURCE-SAVED");quit;'];st=run("target-only-local-original-lift",lines)
   if not one(st["markers"],"@@WHOLE-LOCAL-SOURCE-SAVED",False):
    if st["budget"]:raise Budget("complete target-only local lift not returned")
    raise ValueError("missing whole original local source")
   state["sourceCandidate"]={"data":identity(a.out/"whole-local-source.ssi"),"evidence":st};flush()
  checked(state["sourceCandidate"]["data"])
  if len(state["sourceTexts"])<56:
   first=len(state["sourceTexts"]);lines=original_lines(a.out)+["def Sources=read("+ss(a.out/"whole-local-source.ssi","ssi:r ")+");",
    'if(nrows(Sources)!=56 || ncols(Sources)!=1){print("@@FAIL local-export-shape");quit;}',
    'matrix Difference=OM*Sources-TM;int i;for(i=1;i<=10;i++){if(Difference[i,1]!=0){print("@@FAIL all-ten-localized-products");quit;}}',
    'print("@@ALL-TEN-LOCALIZED-PRODUCTS");']
   for i in range(first,56):
    lines += ["write("+ss(a.out/("local-source-%02d.txt"%i),":w ")+",Sources[%d,1]);"%(i+1),'print("@@LOCAL-SOURCE-TEXT '+str(i)+' "+string(size(Sources[%d,1])));'%(i+1)]
   lines+=['print("@@ALL-LOCAL-SOURCE-TEXTS");quit;'];st=run("verify-export-all-local-coefficients",lines)
   if one(st["markers"],"@@ALL-TEN-LOCALIZED-PRODUCTS",False):
    state["allTenLocalProductsEvidence"]=st
    for i in range(first,56):
     if not one(st["markers"],"@@LOCAL-SOURCE-TEXT %d "%i,False):break
     state["sourceTexts"].append(identity(a.out/("local-source-%02d.txt"%i)))
    flush()
   if len(state["sourceTexts"])<56:
    if st["budget"]:raise Budget("whole coefficient text prefix retained")
    raise ValueError("incomplete local source export")
   one(st["markers"],"@@ALL-LOCAL-SOURCE-TEXTS")
  need(len(state["sourceTexts"])==56 and state.get("allTenLocalProductsEvidence"),"all local source products before extraction")
  rawcoef=[]
  for d in state["sourceTexts"]:tick();rawcoef.append(parse_poly(checked(d),NAMES))
  from flint import nmod_mpoly_ctx
  ctx=nmod_mpoly_ctx.get(tuple(m.NEW_NAMES)+("rho",),P,"lex");rrho=ctx.gens()[-1];cz=ctx.constant(0)
  def ext(f):return ctx.from_dict({tuple(e)+(0,):int(c0) for e,c0 in f.to_dict().items()})
  lc=[ctx.from_dict({e[:12]+(0,)*5+(e[12],):c0 for e,c0 in v.items()}) for v in rawcoef]
  dd=ext(delta)
  for i in range(10):
   tick();need(sum((ext(M[i][j])*lc[j] for j in range(46)),cz)+(rrho*dd-1)*lc[46+i]==int(i==0),"independent full ten localizer polynomial products")
  N=max((e[12] for v in rawcoef[:46] for e in v),default=0)
  def clear(v):
   out=m.ZERO
   for e,c0 in v.items():out+=m.CTX.from_dict({e[:12]+(0,)*5:c0})*delta**(N-e[12])
   return out
  alphas=[clear(v) for v in rawcoef[:46]];target=delta**N
  for i in range(10):tick();need(m.dot(M[i],alphas)==(target if i==0 else m.ZERO),"all ten denominator-cleared products")
  gamma=[m.ZERO for _ in range(50)]
  for k,j in enumerate(keep):gamma[j]=alphas[k]
  for i in range(10):tick();need(sum((gamma[j]*vectors[j][i] for j in range(50)),m.ZERO)==(target if i==0 else m.ZERO),"all ten original fifty-source coordinates")
  sigma=[]
  for i in range(18):
   name="complete-original18-source-%02d"%i
   if name in state["phases"]:z0=read_phase(name);need(z0["generator"]==i and z0["deltaExponent"]==N,"same original source phase");v=m.unpack(z0["coefficient"])
   else:
    tick();v=sum((gamma[j]*sources[j][i] for j in range(50)),m.ZERO);phase(name,{"generator":i,"deltaExponent":N,"coefficient":m.pack(v)})
   sigma.append(v)
  tick();need(m.dot(original,sigma)==target,"all eighteen original polynomial generators multiply to delta power")
  oldsigma=[]
  for i in range(17):
   name="complete-original17-source-%02d"%i
   if name in state["phases"]:z0=read_phase(name);need(z0["generator"]==i and z0["deltaExponent"]==N,"same physical source phase");v=m.unpack(z0["coefficient"])
   else:
    tick();v=sum((sigma[j]*J[j][i] for j in range(17)),m.ZERO);phase(name,{"generator":i,"deltaExponent":N,"coefficient":m.pack(v)})
   oldsigma.append(v)
  tick();need(m.dot(old,oldsigma)+original[17]*sigma[17]==target,"all seventeen physical gradients plus Bell multiply to the literal delta power")
  alphaPhases=[]
  for k,v in enumerate(alphas):
   name="complete-cleared-literal-coefficient-%02d"%k
   if name in state["phases"]:
    z0=read_phase(name);need(z0["parentPosition"]==keep[k] and z0["deltaExponent"]==N and m.unpack(z0["coefficient"])==v,"same complete cleared literal coefficient")
   else:phase(name,{"parentPosition":keep[k],"deltaExponent":N,"coefficient":m.pack(v)})
   alphaPhases.append(state["phases"][name])
  cert={"prime":P,"coefficientRoot":ROOT,"chartIndex":ci,"originalMeanRows":rows,"delta":m.pack(delta),"deltaExponent":N,
   "allClearedLiteralSourceCoefficientPhases":alphaPhases,"retainedOriginalFiftySeedPositions":keep,"allOtherFourSeedCoefficientsAreZero":True,
   "allOriginal18SourcePhases":[state["phases"]["complete-original18-source-%02d"%i] for i in range(18)],
   "allOriginal17PhysicalSourcePhases":[state["phases"]["complete-original17-source-%02d"%i] for i in range(17)],
   "originalBellSourcePhase":state["phases"]["complete-original18-source-17"],
   "coordinateForwardOriginalContext":base["coordinateForwardOriginalContext"],"coordinateInverse":base["coordinateInverse"],
   "allTenLocalizedAndClearedProductsVerified":True,"allTenOriginalSeedProductsVerified":True,"allOriginal18ProductVerified":True,
   "all17PhysicalGradientPlusBellProductVerified":True,"characteristicZeroLiftVerified":False,"allOriginalInputs":inputs}
  d=phase("complete-original-rank-four-field-source-certificate",cert)
  rec["status"]="completed-positive";rec["parameters"].update(outcome="literal-original-delta-power-source-over-F127-only",deltaExponent=N,
   allTenLocalizedAndClearedProductsVerified=True,allTenOriginalSeedProductsVerified=True,all18OriginalProductsVerified=True,
   all17PhysicalGradientPlusBellProductVerified=True,certificate=d);flush();return 0
 except Budget as e:rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75
 except BaseException as e:rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0)
  if child is not None and child.poll() is None:
   child.terminate()
   try:child.wait(timeout=3)
   except subprocess.TimeoutExpired:child.kill();child.wait()
  flush();print(canon(rec).decode(),flush=True)
 return code
if __name__=="__main__":raise SystemExit(main())
