#!/usr/bin/env python3
"""Read-only exact column contents and SCC of the paid2751 low-fill core.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Does not redo any of the1567 pivots or solve any new rational system.
"""
import argparse,collections,gzip,hashlib,heapq,json,math,os,pathlib,resource,sys,time,traceback
sys.dont_write_bytecode=True
sys.setrecursionlimit(20000)
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
INPUT_BYTES=80674893
INPUT_SHA="54288bdab2af917695df1a9e2e681cafffaee435ef0fcc86d766f058324d94ba"
INPUT_BINDING="044ea5d75d28042c53c2db1896ec186173b6b320e598cc35208d761f48dbdad0"
class BudgetExpired(Exception):pass
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   z=f.read(1048576)
   if not z:break
   n+=len(z);h.update(z)
 return {"bytes":n,"sha256":h.hexdigest()}
def save(p,x):
 p=pathlib.Path(p);t=p.with_name(p.name+".tmp")
 with (gzip.open(t,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else t.open("w")) as f:json.dump(x,f,separators=(",",":"))
 os.replace(t,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument("--state",type=pathlib.Path,required=True);ap.add_argument("--out",type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=30);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=60 and 0<a.memory_mib<=4096,"bounded read-only structure probe")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-min(2,a.seconds/10)
 out=a.out.resolve();need(not out.exists() or not any(out.iterdir()),"fresh output");out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-seven-low-fill-column-content-and-scc-v1","status":"running",
  "newPivotsPerformed":0,"newRationalSolvePerformed":False,"largeDataUploadedOrCommitted":False,"events":[],
  "parameters":{"secondsLimit":a.seconds,"memoryMiB":a.memory_mib}};temps=[];code=1
 def check():
  if time.monotonic()>=deadline:raise BudgetExpired("actual read-only content/SCC deadline")
 try:
  need(sha(a.state)=={"bytes":INPUT_BYTES,"sha256":INPUT_SHA},"same actual complete2751 source state")
  with gzip.open(a.state,"rt",encoding="utf-8") as f:st=json.load(f)
  need(st["binding"]==INPUT_BINDING and len(st["reverseSubstitutionDAG"])==1567,"paid1541+26 exact pivots")
  original=st["originalBinding"];source=list(map(int,st["sourceOriginalRows4325"]))
  active=set(map(int,st["remainingSourceColumnPositions"]));rawrows=st.pop("rows")
  need(len(active)==len(rawrows)==2751,"exact2751 checkpoint")
  del st["reverseSubstitutionDAG"];st.pop("initialRowContentDivisors",None)
  rows={};contents={j:0 for j in active};rhsbits=0;nnz=0;beforemax=0;beforebits=0
  for z,r in enumerate(rawrows):
   i=int(r["originalOutputRow"]);terms=r.pop("coefficients");row={}
   for j,ss in terms:
    j=int(j);v=int(ss);need(v!=0 and j in active,"all actual active nonzero source coefficients");row[j]=v
    if contents[j]!=1:contents[j]=math.gcd(contents[j],abs(v))
    hb=abs(v).bit_length();beforemax=max(beforemax,hb);beforebits+=hb
   rows[i]=row;nnz+=len(row)
   rhsbits=max(rhsbits,max(abs(int(v)).bit_length() for v in r["rightHandSideSeven"]))
   if z%64==0:check()
  del rawrows
  need(nnz==424921 and all(g>0 for g in contents.values()),"full complete paid nonzero column set")
  material={"codeSHA256":sha(__file__)["sha256"],"inputBytes":INPUT_BYTES,"inputSHA256":INPUT_SHA,
   "inputBinding":INPUT_BINDING,"originalBinding":original}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material})
  aftermax=0;afterbits=0
  for z,(i,row) in enumerate(rows.items()):
   for j,v in row.items():
    g=contents[j];need(v%g==0,"exact column content divides every actual coefficient")
    b=abs(v//g).bit_length();aftermax=max(aftermax,b);afterbits+=b
   if z%64==0:check()
  data={"format":"isp-seven-exact-column-content-v1","binding":binding,"inputBinding":INPUT_BINDING,
    "columnPositionsAndPositiveContents":[[j,str(contents[j])] for j in sorted(active)],
    "sourceOriginalRows4325":source,
    "coordinateEquation":"B'=B*diag(1/g); z=diag(g)*x; same seven RHS; restore x=z/g before the inherited DAG",
    "all424921EntriesExactlyDivisible":True,"originalStateUnchanged":True}
  temps.append(save(out/"seven-low-fill-exact-column-contents.json.gz",data))
  gcd_bits=sorted(g.bit_length() for g in contents.values())
  rec.update({"columnContentsComplete":True,"actualUnitSize":2751,"actualNonzeroEntries":nnz,
    "nonunitColumnContents":sum(g!=1 for g in contents.values()),"maximumColumnContentBits":max(gcd_bits),
    "medianColumnContentBits":gcd_bits[len(gcd_bits)//2],
    "maximumCoefficientBitsBefore":beforemax,"maximumCoefficientBitsAfterColumnDivision":aftermax,
    "sumCoefficientBitsBefore":beforebits,"sumCoefficientBitsAfterColumnDivision":afterbits,
    "rightHandSideMaximumBitsUnchanged":rhsbits,"all424921EntriesExactlyDivisible":True})
  try:
   import flint
   rec["parameters"]["flintVersions"]={key:str(getattr(flint,key)) for key in ("__version__","__FLINT_VERSION__","__FLINT_RELEASE__") if hasattr(flint,key)}
  except ImportError:rec["parameters"]["flintVersions"]={"available":False}
  check()
  # Structural matching/SCC uses the actual support; positive column division preserves it.
  rlist=sorted(rows);adj={i:sorted(rows[i]) for i in rlist};del rows
  mr={i:None for i in rlist};mc={j:None for j in active};INF=10**9;dist={}
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
  need(all(v is not None for v in mr.values()) and len(set(mr.values()))==2751,"complete original structural matching")
  graph={j:[] for j in active};reverse={j:[] for j in active}
  for i in rlist:
   v=mr[i]
   for j in adj[i]:
    if j!=v:graph[v].append(j);reverse[j].append(v)
  seen=set();finish=[]
  for v in sorted(active):
   if v in seen:continue
   seen.add(v);stack=[(v,0)]
   while stack:
    x,k=stack[-1]
    if k<len(graph[x]):
     y=graph[x][k];stack[-1]=(x,k+1)
     if y not in seen:seen.add(y);stack.append((y,0))
    else:finish.append(x);stack.pop()
   check()
  owner={};blocks=[]
  for v in reversed(finish):
   if v in owner:continue
   c=len(blocks);stack=[v];owner[v]=c;nodes=[]
   while stack:
    x=stack.pop();nodes.append(x)
    for y in reverse[x]:
     if y not in owner:owner[y]=c;stack.append(y)
   blocks.append(sorted(nodes));check()
  deps=[set() for _ in blocks];users=[set() for _ in blocks]
  for x,ys in graph.items():
   c=owner[x]
   for y in ys:
    d=owner[y]
    if c!=d:deps[c].add(d);users[d].add(c)
  degs=[len(d) for d in deps];ready=[c for c,d in enumerate(degs) if d==0];heapq.heapify(ready);order=[]
  while ready:
   c=heapq.heappop(ready);order.append(c)
   for d in users[c]:
    degs[d]-=1
    if degs[d]==0:heapq.heappush(ready,d)
  need(len(order)==len(blocks),"complete dependency order")
  pos={c:i for i,c in enumerate(order)}
  need(all(pos[d]<pos[c] for c in range(len(blocks)) for d in deps[c]),"exact structural block dependency")
  temps.append(save(out/"seven-low-fill-structural-blocks.json.gz",{"binding":binding,"rowMatching":[[i,mr[i]] for i in rlist],
   "blocks":[{"sourceColumnPositions":v,"originalOutputRows":sorted(mc[j] for j in v),"dependsOn":sorted(deps[c])} for c,v in enumerate(blocks)],
   "solveOrder":order,"allOffDiagonalEntriesFollowDependencyOrder":True}))
  sizes=sorted(map(len,blocks),reverse=True)
  rec.update({"status":"completed","perfectMatchingVerified":True,"blockCount":len(blocks),
    "largestBlockSize":sizes[0],"blockSizeHistogram":{str(k):v for k,v in sorted(collections.Counter(sizes).items())},
    "allOffDiagonalEntriesFollowDependencyOrder":True})
  rec["parameters"].update({"blockSizeHistogram":rec["blockSizeHistogram"],"allTemporaryCoordinateDataHaveParentBinding":True})
  code=0
 except BudgetExpired as e:rec.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  rec["parameters"]["temporaryFiles"]=temps;rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"seven-low-fill-content-scc-receipt.json",rec)
 need((out/"seven-low-fill-content-scc-receipt.json").stat().st_size<100000,"small persistent receipt")
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
