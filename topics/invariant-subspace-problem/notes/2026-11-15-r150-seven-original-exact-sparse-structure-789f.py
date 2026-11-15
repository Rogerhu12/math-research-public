#!/usr/bin/env python3
"""Exact support-1/2 peeling and structural block decomposition of the paid4318 unit.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No new numerical rank, no rational solve, no replacement of original sources.
"""
import argparse,collections,gzip,hashlib,heapq,json,math,os,pathlib,resource,sys,time,traceback
sys.dont_write_bytecode=True
sys.setrecursionlimit(20000)
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
CORE_BYTES=1497227
CORE_SHA="5cd0c5430089a3d4431ef6d058ec36a55d084d70e311cf13790fd60a5457efcc"
PROFILE_BYTES=62084
PROFILE_SHA="43cd638dfe13978f375490db9afdca5f318e137a384820b69bbc74b0ce48a7df"
OLD_BINDING="74bf887ac9ce134b551b8957061bc713cded79bd6a88e7a35fe8faa3101bb58c"
class BudgetExpired(Exception):pass
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   x=f.read(1048576)
   if not x:break
   n+=len(x);h.update(x)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 p=pathlib.Path(p)
 with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open()) as f:return json.load(f)
def save(p,v):
 p=pathlib.Path(p);t=p.with_name(p.name+".tmp")
 with (gzip.open(t,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else t.open("w")) as f:json.dump(v,f,separators=(",",":"))
 os.replace(t,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def source_degree(raw):
 m=(raw-1)//17
 return 0 if m<1 else 1 if m<12 else 2 if m<78 else 3
def output_degree(i):
 return 5 if i<3003 else 4 if i<4004 else 3 if i<4290 else 2 if i<4356 else 1
def hist(vals):return {str(k):v for k,v in sorted(collections.Counter(vals).items())}
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["core","profile","out"]:ap.add_argument("--"+k,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=30);ap.add_argument("--memory-mib",type=int,default=512)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=60,"bounded structure budget <=60 seconds")
 need(0<a.memory_mib<=2048,"explicit memory bound <=2048 MiB")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-min(3,a.seconds/10)
 out=a.out.resolve();need(not out.exists() or not any(out.iterdir()),"fresh structure output");out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-seven-original-unit-exact-sparse-structure-v1","status":"running",
      "mathematicalSecondsLimit":a.seconds,"memoryMiB":a.memory_mib,"newRationalSolvePerformed":False,
      "newFiniteFieldEliminationPerformed":False,"oldNormalFormsRecomputed":False,
      "largeDataUploadedOrCommitted":False,"parameters":{},"events":[]}
 temp=[];code=1;rows={};rhs={};active=set();dag=[];source=[];mr={};mc={};binding=None;peeling_done=False
 def check():
  if time.monotonic()>=deadline:raise BudgetExpired("actual structure deadline")
 def remember(p):
  r={"file":p.name,**sha(p),"temporaryOnly":True}
  for j,x in enumerate(temp):
   if x["file"]==r["file"]:temp[j]=r;return r
  temp.append(r);return r
 def keep_state(stage):
  if binding is None:return
  p=out/"seven-exact-peeled-core-and-backsubstitution.json.gz"
  save(p,{"format":"isp-seven-exact-peeled-unit-v1","binding":binding,"oldBinding":OLD_BINDING,
    "stage":stage,"peelingCompleted":peeling_done,"remainingSourceColumnPositions":sorted(active),
    "sourceOriginalRows4325":source,"rows":[{"originalOutputRow":i,
      "coefficients":[[j,str(v)] for j,v in sorted(rows[i].items())],
      "rightHandSideSeven":[str(v) for v in rhs[i]]} for i in sorted(rows)],
    "reverseSubstitutionDAG":dag,
    "currentMatchingByOriginalOutputRows":[[i,j] for i,j in sorted(mr.items()) if j is not None],
    "allTransformationsOverQ":True,"originalSevenRHSRetained":True,
    "originalCoreIdentity":{"bytes":CORE_BYTES,"sha256":CORE_SHA},
    "originalProfileIdentity":{"bytes":PROFILE_BYTES,"sha256":PROFILE_SHA}})
  remember(p)
 try:
  need(sha(a.core)=={"bytes":CORE_BYTES,"sha256":CORE_SHA},"same paid original integer core")
  need(sha(a.profile)=={"bytes":PROFILE_BYTES,"sha256":PROFILE_SHA},"same paid original unit profile")
  core=read(a.core);p=read(a.profile)
  need(core["binding"]==p["binding"]==OLD_BINDING and p["coreIdentity"]==sha(a.core),"original source/profile binding")
  need(p["unitBlockNonzeroModulo65521"] and p["unitRowsSubsetOriginalI"],"paid nonsingular original unit inside I")
  pp=list(map(int,p["pivotColumnPositions"]));ff=list(map(int,p["freeColumnPositions"]));ii=list(map(int,p["unitOriginalRowsZeroBased"]))
  need(len(pp)==len(ii)==4318 and len(ff)==7 and len(set(pp+ff))==4325,"complete original4318+7 profile")
  source=list(map(int,core["sourceRows"]));need(len(source)==4325,"same4325 original source columns")
  pset=set(pp)
  for i in ii:
   row={int(j):int(v) for j,v in core["integerRows"][i]}
   rows[i]={j:v for j,v in row.items() if j in pset and v};rhs[i]=[row.get(j,0) for j in ff]
  del core
  active=set(pp)
  material={"codeSHA256":sha(__file__)["sha256"],"oldBinding":OLD_BINDING,
    "core":{"bytes":CORE_BYTES,"sha256":CORE_SHA},"profile":{"bytes":PROFILE_BYTES,"sha256":PROFILE_SHA}}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material,"freeOriginalSourceRows":[source[j] for j in ff]})
  rec.update({"originalUnitRows":4318,"originalUnitNonzeroEntries":sum(map(len,rows.values())),
    "originalSourceDegreeHistogram":hist(source_degree(source[j]) for j in pp),
    "originalOutputDegreeHistogram":hist(output_degree(i) for i in ii)})
  check()
  incidence={j:set() for j in pp}
  for i,row in rows.items():
   need(row,"nonsingular original unit has no zero row")
   for j in row:incidence[j].add(i)
  heap=[(len(row),i) for i,row in rows.items() if len(row)<=2];heapq.heapify(heap)
  updates=0
  # Each stored row is an actual equation for B*X=E.
  # a*x_j + b*x_k = e allows x_j=(e-b*x_k)/a.
  # Other equations are transformed to a*r-r_j*pivot; gcd scaling is exact over Q.
  while heap:
   check();count,i=heapq.heappop(heap)
   if i not in rows or len(rows[i])!=count or count>2:continue
   pivot=rows[i].copy();target=rhs[i][:]
   j=min(pivot,key=lambda k:(abs(pivot[k]).bit_length(),k));aa=pivot[j]
   others=[(k,v) for k,v in pivot.items() if k!=j]
   affected=sorted(incidence[j]-{i})
   for r in affected:
    old=rows[r];c=old[j];new={k:aa*v for k,v in old.items()}
    for k,v in pivot.items():new[k]=new.get(k,0)-c*v
    new={k:v for k,v in new.items() if v}
    rr=[aa*rhs[r][t]-c*target[t] for t in range(7)]
    need(j not in new and new,"exact nonsingular peeling cannot leave a zero row")
    g=0
    for v in new.values():g=math.gcd(g,abs(v))
    for v in rr:g=math.gcd(g,abs(v))
    if g>1:new={k:v//g for k,v in new.items()};rr=[v//g for v in rr]
    for k in old.keys()-new.keys():incidence[k].discard(r)
    for k in new.keys()-old.keys():incidence[k].add(r)
    rows[r]=new;rhs[r]=rr;updates+=1
    if len(new)<=2:heapq.heappush(heap,(len(new),r))
   for k in pivot:incidence[k].discard(i)
   del rows[i];del rhs[i];active.remove(j);incidence.pop(j)
   dag.append({"originalOutputRow":i,"sourceColumnPosition":j,"originalSourceRow":source[j],
       "pivotCoefficient":str(aa),"otherTerms":[[k,str(v)] for k,v in others],
       "rightHandSideSeven":[str(v) for v in target]})
  peeling_done=True
  rec.update({"exactPeelingCompleted":True,"exactPeeledVariables":len(dag),"exactRowUpdates":updates,
      "remainingUnitSize":len(active),"remainingNonzeroEntries":sum(map(len,rows.values())),
      "remainingMaximumIntegerBits":max((abs(v).bit_length() for row in rows.values() for v in row.values()),default=0)})
  need(len(active)==len(rows),"exact square remaining core")
  keep_state("peeling-complete")
  # Perfect structural matching, used only as row/column permutations.
  # No matching entry is interpreted as a Gaussian pivot.
  check();rlist=sorted(rows);adj={i:sorted(rows[i]) for i in rlist}
  mr={i:None for i in rlist};mc={j:None for j in active};dist={};INF=10**9
  while True:
   check();q=collections.deque();found=INF
   for i in rlist:
    if mr[i] is None:dist[i]=0;q.append(i)
    else:dist[i]=INF
   while q:
    i=q.popleft()
    if dist[i]>=found:continue
    for j in adj[i]:
     r=mc[j]
     if r is None:found=dist[i]+1
     elif dist[r]==INF:dist[r]=dist[i]+1;q.append(r)
   if found==INF:break
   def dfs(i):
    for j in adj[i]:
     r=mc[j]
     if r is None or (dist.get(r,INF)==dist[i]+1 and dfs(r)):
      mr[i]=j;mc[j]=i;return True
    dist[i]=INF;return False
   for z,i in enumerate(rlist):
    if mr[i] is None:dfs(i)
    if z%128==0:check()
  need(all(mr[i] is not None for i in rlist) and len(set(mr.values()))==len(active),"structural perfect matching of paid nonsingular unit")
  rec["structuralPerfectMatchingVerified"]=True
  # Directed source dependency: matched source of a row -> every other source in that row.
  graph={j:[] for j in active};rev={j:[] for j in active}
  for i in rlist:
   v=mr[i]
   for j in adj[i]:
    if j!=v:graph[v].append(j);rev[j].append(v)
  seen=set();finish=[]
  for v in sorted(active):
   if v in seen:continue
   stack=[(v,0)];seen.add(v)
   while stack:
    x,k=stack[-1]
    if k<len(graph[x]):
     y=graph[x][k];stack[-1]=(x,k+1)
     if y not in seen:seen.add(y);stack.append((y,0))
    else:finish.append(x);stack.pop()
   check()
  comps=[];owner={}
  for v in reversed(finish):
   if v in owner:continue
   ci=len(comps);nodes=[];stack=[v];owner[v]=ci
   while stack:
    x=stack.pop();nodes.append(x)
    for y in rev[x]:
     if y not in owner:owner[y]=ci;stack.append(y)
   comps.append(sorted(nodes));check()
  deps=[set() for _ in comps];users=[set() for _ in comps]
  for x,targets in graph.items():
   a0=owner[x]
   for y in targets:
    b0=owner[y]
    if a0!=b0:deps[a0].add(b0);users[b0].add(a0)
  degree=[len(x) for x in deps];ready=[j for j,d in enumerate(degree) if d==0];heapq.heapify(ready);order=[]
  while ready:
   c=heapq.heappop(ready);order.append(c)
   for a0 in users[c]:
    degree[a0]-=1
    if degree[a0]==0:heapq.heappush(ready,a0)
  need(len(order)==len(comps),"complete acyclic block solve order")
  position={c:i for i,c in enumerate(order)}
  need(all(position[d]<position[c] for c in range(len(comps)) for d in deps[c]),"all dependencies solved before row block")
  records=[]
  for c,nodes in enumerate(comps):
   check();rr=sorted(mc[j] for j in nodes);node_set=set(nodes)
   records.append({"block":c,"size":len(nodes),"sourceColumnPositions":nodes,"originalOutputRows":rr,
     "dependsOnBlocks":sorted(deps[c]),"sourceDegreeHistogram":hist(source_degree(source[j]) for j in nodes),
     "outputDegreeHistogram":hist(output_degree(i) for i in rr),
     "internalNonzeroEntries":sum(sum(k in node_set for k in rows[i]) for i in rr)})
  bpath=out/"seven-exact-structural-blocks-and-order.json.gz"
  save(bpath,{"format":"isp-seven-original-unit-block-triangular-v1","binding":binding,
    "peeledCoreIdentity":sha(out/"seven-exact-peeled-core-and-backsubstitution.json.gz"),
    "rowToMatchedSource":[[i,mr[i]] for i in rlist],"blocks":records,"solveOrder":order,
    "allOffDiagonalEntriesFollowDependencyOrder":True,
    "eachDiagonalBlockNonsingularOverQByPaidUnitDeterminant":True,
    "noRationalSolutionComputed":True})
  remember(bpath)
  largest=sorted(records,key=lambda x:(-x["size"],x["block"]))[:20]
  rec.update({"status":"completed","blockCount":len(comps),"blockSizeHistogram":hist(map(len,comps)),
    "largestBlockSize":max(map(len,comps),default=0),"sumBlockCubes":sum(len(x)**3 for x in comps),
    "originalDenseCube":4318**3,"allOffDiagonalEntriesFollowDependencyOrder":True,
    "eachDiagonalBlockNonsingularOverQByPaidUnitDeterminant":True,
    "largestTwentyBlocks":[{k:v for k,v in x.items() if k not in ("sourceColumnPositions","originalOutputRows","dependsOnBlocks")} for x in largest]})
  rec["parameters"].update({k:rec[k] for k in ("originalSourceDegreeHistogram","originalOutputDegreeHistogram","blockSizeHistogram","largestTwentyBlocks")})
  code=0
 except BudgetExpired as e:
  rec.update(status="budget-exhausted",error=str(e));keep_state("budget-exhausted");code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc());keep_state("failed-with-exact-partial-state");code=1
 finally:
  rec["parameters"]["temporaryFiles"]=temp;rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"seven-original-exact-sparse-structure-receipt.json",rec)
 need((out/"seven-original-exact-sparse-structure-receipt.json").stat().st_size<100000,"small long-term receipt")
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
