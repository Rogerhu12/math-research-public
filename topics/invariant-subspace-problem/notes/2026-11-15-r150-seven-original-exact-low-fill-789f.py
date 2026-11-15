#!/usr/bin/env python3
"""Bounded exact low-fill continuation of the paid4292 original integer unit.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Each pivot is transactional. All seven RHS and the inherited source DAG survive.
"""
import argparse,collections,gzip,hashlib,heapq,json,math,os,pathlib,resource,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
STATE_BYTES=1605177
STATE_SHA="9032a239fd7e0ff617f8248181b3caa72f8689472df4ec836ce40629b187f47f"
PARENT_BINDING="808f8f923a6787ef2f9c7044a2238cf73add420c004d02cb4370f317ee65650a"
ORIGINAL_BINDING="74bf887ac9ce134b551b8957061bc713cded79bd6a88e7a35fe8faa3101bb58c"
class BudgetExpired(Exception):pass
class ResourceGate(Exception):pass
def need(b,s):
 if not b:raise ValueError(s)
def sha(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   x=f.read(1048576)
   if not x:break
   n+=len(x);h.update(x)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 with gzip.open(p,"rt",encoding="utf-8") as f:return json.load(f)
def save(p,x):
 p=pathlib.Path(p);t=p.with_name(p.name+".tmp")
 with (gzip.open(t,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else t.open("w")) as f:json.dump(x,f,separators=(",",":"))
 os.replace(t,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def degree(raw):
 k=(raw-1)//17
 return 0 if k<1 else 1 if k<12 else 2 if k<78 else 3
def hist(xs):return {str(k):v for k,v in sorted(collections.Counter(xs).items())}
def primitive(row,rhs):
 g=0
 for v in row.values():
  g=math.gcd(g,abs(v))
  if g==1:break
 if g!=1:
  for v in rhs:
   g=math.gcd(g,abs(v))
   if g==1:break
 need(g>0,"nonzero current unit row")
 if g>1:return ({k:v//g for k,v in row.items()},[v//g for v in rhs],g)
 return row,rhs,1
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument("--state",type=pathlib.Path,required=True);ap.add_argument("--out",type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=30);ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--candidate-rows",type=int,default=64)
 ap.add_argument("--max-nnz",type=int,default=500000)
 ap.add_argument("--max-integer-bits",type=int,default=4096)
 ap.add_argument("--max-pivot-work",type=int,default=60000)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=120,"explicit finite <=120 second bound")
 need(0<a.memory_mib<=2048 and 1<=a.candidate_rows<=128,"explicit memory and candidate rows")
 need(0<a.max_nnz<=1000000 and 0<a.max_integer_bits<=8192 and 0<a.max_pivot_work<=200000,"explicit fill/height/one-pivot gates")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 out=a.out.resolve();need(not out.exists() or not any(out.iterdir()),"fresh low-fill output");out.mkdir(parents=True,exist_ok=True)
 start=time.monotonic();deadline=start+a.seconds-min(3,a.seconds/10)
 rec={"format":"isp-seven-original-exact-low-fill-v1","status":"running","parameters":{
    "secondsLimit":a.seconds,"memoryMiB":a.memory_mib,"candidateRows":a.candidate_rows,
    "maximumNonzeroEntries":a.max_nnz,"maximumIntegerBits":a.max_integer_bits,
    "maximumSinglePivotWork":a.max_pivot_work},
    "newFiniteFieldEliminationPerformed":False,"newRationalDenseSolvePerformed":False,
    "largeDataUploadedOrCommitted":False,"events":[]}
 rows={};rhs={};source=[];active=set();dag=[];scales=[];binding=None;nnz=0;last_bits=0;total_updates=0
 added=0;max_pivot_sec=0.0;max_used_work=0;original_state=None;code=1;pending_started=False
 def check():
  if time.monotonic()>=deadline:raise BudgetExpired("actual shared low-fill deadline")
 def persist(reason):
  if binding is None:return None
  vals={"format":"isp-seven-exact-low-fill-unit-v1","binding":binding,"originalBinding":ORIGINAL_BINDING,
   "parentBinding":PARENT_BINDING,"parentStateIdentity":{"bytes":STATE_BYTES,"sha256":STATE_SHA},
   "stopReason":reason,"remainingSourceColumnPositions":sorted(active),"sourceOriginalRows4325":source,
   "rows":[{"originalOutputRow":i,"coefficients":[[j,str(v)] for j,v in sorted(rows[i].items())],
       "rightHandSideSeven":[str(v) for v in rhs[i]]} for i in sorted(rows)],
   "reverseSubstitutionDAG":dag,"initialRowContentDivisors":scales,
   "allSevenOriginalRHSRetained":True,"everyCommittedPivotComplete":True,
   "originalCoreIdentity":original_state["originalCoreIdentity"],
   "originalProfileIdentity":original_state["originalProfileIdentity"]}
  return save(out/"seven-exact-low-fill-core-and-backsubstitution.json.gz",vals)
 try:
  need(sha(a.state)=={"bytes":STATE_BYTES,"sha256":STATE_SHA},"same actual rootb61 peeled input bytes")
  st=read(a.state);original_state=st
  need(st["binding"]==PARENT_BINDING and st["oldBinding"]==ORIGINAL_BINDING and st["peelingCompleted"],"actual structural checkpoint identity")
  source=list(map(int,st["sourceOriginalRows4325"]));active=set(map(int,st["remainingSourceColumnPositions"]))
  dag=list(st["reverseSubstitutionDAG"])
  need(len(source)==4325 and len(active)==4292 and len(dag)==26,"inherit exactly paid26 removals")
  for r in st["rows"]:
   i=int(r["originalOutputRow"]);rr={int(j):int(v) for j,v in r["coefficients"]};ee=list(map(int,r["rightHandSideSeven"]))
   need(rr and len(ee)==7 and set(rr)<=active,"complete active integer row and seven RHS")
   rr,ee,g=primitive(rr,ee);rows[i]=rr;rhs[i]=ee
   if g!=1:scales.append([i,str(g)])
  need(len(rows)==4292,"same square4292")
  material={"codeSHA256":sha(__file__)["sha256"],"parentState":{"bytes":STATE_BYTES,"sha256":STATE_SHA},
      "parentBinding":PARENT_BINDING,"originalBinding":ORIGINAL_BINDING,
      "candidateRows":a.candidate_rows,"maxNnz":a.max_nnz,"maxBits":a.max_integer_bits,"maxPivotWork":a.max_pivot_work}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material,"initialRowNormalizations":len(scales)})
  incidence={j:set() for j in active}
  for i,row in rows.items():
   for j in row:incidence[j].add(i)
  revision={i:0 for i in rows}
  heap=[(len(row),i,0) for i,row in rows.items()];heapq.heapify(heap)
  nnz=sum(map(len,rows.values()));last_bits=max(abs(v).bit_length() for row in rows.values() for v in row.values())
  rec["events"].append({"preparedPrimitiveExactRows":len(rows),"nnz":nnz,"maximumIntegerBits":last_bits})
  stop_reason="all-unit-variables-eliminated"
  while active:
   check()
   # This is a fixed heuristic: all entries in the64 sparsest current rows.
   # It is not reported as a global Markowitz minimizer.
   chosen=[]
   while heap and len(chosen)<a.candidate_rows:
    length,i,ver=heapq.heappop(heap)
    if i in rows and revision[i]==ver and len(rows[i])==length:chosen.append((length,i,ver))
   need(chosen,"actual active rows retained in selection heap")
   for item in chosen:heapq.heappush(heap,item)
   cand=[]
   for length,i,ver in chosen:
    for j,v in rows[i].items():
     score=(length-1)*(len(incidence[j])-1)
     cand.append((score,abs(v).bit_length(),i,j))
   cand.sort()
   pick=None
   for score,bits,i,j in cand[:128]:
    work=sum(len(rows[r])+len(rows[i])+7 for r in incidence[j] if r!=i)
    if work<=a.max_pivot_work:
     pick=(score,bits,i,j,work);break
   if pick is None:raise ResourceGate("single-pivot-work-gate among128 best fixed-row candidates")
   score,bits,i,j,work=pick;pv=rows[i].copy();pe=rhs[i][:];aa=pv[j]
   affected=sorted(incidence[j]-{i});pending={};pending_nnz=nnz-len(pv);newmax=0;pstart=time.monotonic();pending_started=True
   # No live row, incidence set or DAG changes before this whole transaction completes.
   for z,r in enumerate(affected):
    old=rows[r];c=old[j];g=math.gcd(abs(aa),abs(c));mul=aa//g;sub=c//g
    rr={k:mul*v for k,v in old.items()}
    for k,v in pv.items():rr[k]=rr.get(k,0)-sub*v
    rr={k:v for k,v in rr.items() if v};ee=[mul*rhs[r][t]-sub*pe[t] for t in range(7)]
    need(j not in rr and rr,"exact nonsingular unit row elimination")
    rr,ee,gcontent=primitive(rr,ee)
    hb=max([abs(v).bit_length() for v in rr.values()]+[abs(v).bit_length() for v in ee])
    if hb>a.max_integer_bits:raise ResourceGate("actual pending row exceeds integer-height gate; pivot discarded")
    pending_nnz+=len(rr)-len(old);newmax=max(newmax,hb)
    pending[r]=(rr,ee)
    if z%8==0:check()
   if pending_nnz>a.max_nnz:raise ResourceGate("actual complete pending fill exceeds nnz gate; pivot discarded")
   check()
   # Atomic mathematical commit: no deadline interruption during this bounded update.
   for r,(rr,ee) in pending.items():
    old=rows[r]
    for k in old.keys()-rr.keys():incidence[k].discard(r)
    for k in rr.keys()-old.keys():incidence[k].add(r)
    rows[r]=rr;rhs[r]=ee;revision[r]+=1;heapq.heappush(heap,(len(rr),r,revision[r]))
   for k in pv:incidence[k].discard(i)
   del rows[i];del rhs[i];revision.pop(i);active.remove(j);incidence.pop(j)
   dag.append({"originalOutputRow":i,"sourceColumnPosition":j,"originalSourceRow":source[j],
       "pivotCoefficient":str(aa),"otherTerms":[[k,str(v)] for k,v in sorted(pv.items()) if k!=j],
       "rightHandSideSeven":[str(v) for v in pe],
       "lowFillHeuristicScore":score,"estimatedSinglePivotWork":work})
   added+=1;total_updates+=len(affected);nnz=pending_nnz;last_bits=max(last_bits,newmax);pending_started=False
   dt=time.monotonic()-pstart;max_pivot_sec=max(max_pivot_sec,dt);max_used_work=max(max_used_work,work)
   if len(heap)>max(10000,4*len(rows)):
    heap=[(len(row),r,revision[r]) for r,row in rows.items()];heapq.heapify(heap)
   if added%100==0:
    rec["events"].append({"completedNewPivots":added,"remainingSize":len(active),"nnz":nnz,"heightUpperBound":last_bits,
       "elapsedSeconds":time.monotonic()-start})
  rec["status"]="completed";code=0
 except ResourceGate as e:
  stop_reason=str(e);rec["status"]="completed-bounded-compression";code=0
 except BudgetExpired as e:
  stop_reason=str(e);rec["status"]="budget-exhausted";code=75
 except Exception as e:
  stop_reason=str(e);rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  if binding is not None:
   need(len(active)==len(rows)==4318-len(dag),"complete square state after all committed pivots")
   rec["completedMathematicalSeconds"]=time.monotonic()-start;pack_start=time.monotonic()
   identity=persist(stop_reason)
   rec["checkpointSeconds"]=time.monotonic()-pack_start
   actual_bits=max((abs(v).bit_length() for row in rows.values() for v in row.values()),default=0)
   rhs_bits=max((abs(v).bit_length() for row in rhs.values() for v in row),default=0)
   rec.update({"stopReason":stop_reason,"inheritedPivots":26,"newExactPivots":added,
     "totalExactPivots":len(dag),"remainingUnitSize":len(active),"remainingNonzeroEntries":sum(map(len,rows.values())),
     "remainingMaximumCoefficientBits":actual_bits,"remainingMaximumRHSMagnitudeBits":rhs_bits,
     "exactRowUpdates":total_updates,"maximumCompletedPivotSeconds":max_pivot_sec,
     "maximumCompletedPivotWork":max_used_work,"allSevenOriginalRHSRetained":True,"everyCommittedPivotComplete":True,
     "partialPivotDiscarded":pending_started})
   rec["parameters"].update({"temporaryFiles":[identity],"remainingSourceDegreeHistogram":hist(degree(source[j]) for j in active)})
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"seven-exact-low-fill-receipt.json",rec)
 need((out/"seven-exact-low-fill-receipt.json").stat().st_size<100000,"small long-term receipt")
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
