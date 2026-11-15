#!/usr/bin/env python3
"""Same-I/J normal-five high elimination; retain all normal-four compensation.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only H5 pivot columns are eliminated. Each exact pivot is transactional;
all H4 columns and a complete reverse-substitution DAG remain temporary.
"""
import argparse,collections,gc,gzip,hashlib,heapq,io,itertools,json,math,os,pathlib,resource,signal,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
STOP=False
class BudgetExpired(Exception):pass
class ResourceGate(Exception):pass
def need(v,s):
 if not v:raise ValueError(s)
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 p=pathlib.Path(p)
 with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open("r",encoding="utf-8")) as f:return json.load(f)
def save(p,v):
 p=pathlib.Path(p);p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp")
 if p.suffix==".gz":
  with q.open("wb") as raw:
   with gzip.GzipFile(fileobj=raw,mode="wb",mtime=0,compresslevel=1) as gz:
    with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as f:json.dump(v,f,sort_keys=True,separators=(",",":"))
 else:
  b=json.dumps(v,sort_keys=True,separators=(",",":")).encode()
  need(len(b)<100000,"only small permanent metadata");q.write_bytes(b)
 os.replace(q,p);return {"file":p.name,**identity(p),"temporaryOnly":True}
def pivots(R,rank):
 ans=[]
 for i in range(int(rank)):
  j=next((j for j in range(R.ncols()) if R[i,j]),None)
  need(j is not None and R[i,j]==1,"normalized finite RREF");ans.append(j)
 need(ans==sorted(set(ans)),"strict original pivot order");return ans
def signal_stop(signum,frame):
 global STOP
 STOP=True
def primitive(row):
 g=0
 for v in row.values():
  g=math.gcd(g,abs(v))
  if g==1:break
 if g>1:return {j:v//g for j,v in row.items()},g
 return row,1
PINS={
 "old_unit":(9008513,"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"),
 "coefficients":(20580,"7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1"),
 "profile":(21066,"044b28d717749d23a2959a02c0f8ed7570bfa19bcdff04207056f2a66d2e413d"),
 "paid_m4":(911218,"a359450582e0081fbabd6ff79e6e0e7083d7cd5bfdcef1d801438d00a3d5c814"),
 "paid_full":(27679,"4158cc3b978edeafd9c993e7f1c054d9acc419eb9a5d3f34cf8e9f2cff965c22")}
PAID_SECOND="c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e"
PAID_NORMAL4="672a21c0de59ec537f5d19333524f92ceb71ad3621eec643b9c11cf3f3fce2d3"
N5=1287
N4=1485
NH=1736
def prepare(paths,ids,out,bind,check):
 from flint import nmod_mat
 out.mkdir(parents=True,exist_ok=True);cp=out/"normal-five-high-preparation-receipt.json"
 if cp.exists():
  r=read(cp);need(r["binding"]==bind,"same prepared high binding")
  if r["status"]=="completed":
   for z in r["outputs"]:need(identity(out/z["file"])=={"bytes":z["bytes"],"sha256":z["sha256"]},"unchanged prepared high output")
   return r
 unit=read(paths["old_unit"]);co=read(paths["coefficients"]);prof=read(paths["profile"])
 m4=read(paths["paid_m4"]);paid=read(paths["paid_full"])
 need(unit["binding"]==PAID_SECOND and m4["binding"]==paid["binding"]==PAID_NORMAL4 and
 paid["status"]=="completed" and paid["secondHeadImageDimension"]==22 and
 paid["extendedSmallResidualRank"]==144 and paid["oldNewResidualIntersectionDimension"]==0 and
 paid["all4354OriginalSecondLeftProductsZero"],"same actual complete normal-four result")
 J=list(map(int,unit["originalSourceRows"]));I=set(map(int,prof["originalOutputI"]))
 high=list(map(int,unit["oldZeroRowPositions"]));highset=set(high)
 need(len(J)==len(set(J))==len(I)==4354 and len(high)==len(highset)==1736,"same complete original I,J and high row positions")
 need(m4["originalSourceRows"]==J and m4["highOriginalRowPositions"]==high and
 all(not unit["originalCorrectionRows"][i] and not any(map(int,unit["originalRightHandSideRows"][i])) for i in high),
 "all actual high correction and36 forcing rows zero")
 whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
 wi={q:i for i,q in enumerate(whole)};nd=[sum(j<=8 for j in q) for q in whole]
 E5=[i for i,d in enumerate(nd) if d==5 and i in I];E4=[i for i,d in enumerate(nd) if d==4 and i in I]
 need(len(E5)==1287 and len(E4)==1485 and E4==m4["normalFourOutputCoordinates"],"complete original high target coordinates")
 F0=[list(map(int,r)) for r in co["constant"]]
 need(len(F0)==17 and all(len(r)==77 for r in F0),"whole original constant17 equations")
 mon=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
 need(all(v==0 for row in F0 for q,v in zip(mon,row) if all(j>=9 for j in q)),"original endpoint equations vanish on the pure plane")
 mult=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
 mp={v:i for i,v in enumerate(E5)};rows=[];degrees=[]
 for ii,raw in enumerate(J):
  check();e=(raw-1)%17;mu=mult[(raw-1)//17];row={};degrees.append(sum(j<=8 for j in mu))
  for q,v in zip(mon,F0[e]):
   if v:
    ix=wi[tuple(sorted(mu+q))]
    if ix in mp:row[mp[ix]]=row.get(mp[ix],0)+v
  row={j:v for j,v in row.items() if v};rows.append(row)
  if row:need(ii in highset and degrees[-1]==3,"every normal-five contribution is in actual original high source rows")
 need(all(not row for i,row in enumerate(rows) if i not in highset),"all original nonhigh M5 rows zero")
 bp=out/"complete-original-normal-five-block.json.gz"
 data={"format":"isp-original-normal-five-block-v1","binding":bind,"inputIdentities":ids,
 "originalSourceRows":J,"originalSourceNormalDegrees":degrees,"normalFiveOutputCoordinates":E5,
 "highOriginalRowPositions":high,"allOriginalNonhighRowsZero":True,
 "originalNormalFiveRows":[[[j,str(v)] for j,v in sorted(row.items())] for row in rows]}
 save(bp,data)
 m4rows=[{int(j):int(v) for j,v in row} for row in m4["originalNormalFourRows"]]
 need(len(m4rows)==4354,"whole paid M4 row count")
 pairrows=[]
 for i in high:
  rr=rows[i].copy();rr.update({N5+j:v for j,v in m4rows[i].items()})
  pairrows.append({"originalSourcePosition":i,"originalSourceRow":J[i],
  "coefficients":[[j,str(v)] for j,v in sorted(rr.items())]})
 pair=out/"complete-original-high-normal-five-and-four.json.gz"
 save(pair,{"format":"isp-original-high-h5-h4-v1","binding":bind,"inputIdentities":ids,
 "normalFiveBlockIdentity":identity(bp),"normalFiveOutputCoordinates":E5,
 "normalFourOutputCoordinates":E4,"highOriginalRowPositions":high,
 "firstPivotColumns":1287,"attachedNormalFourColumns":1485,"rows":pairrows,
 "allOriginalHighForcingRowsZero":True,"allNormalFourColumnsRetained":True})
 check()
 h=[rows[i] for i in high]
 H=nmod_mat(NH,N5,[row.get(j,0)%31 for row in h for j in range(N5)],31)
 R,r=H.rref();r=int(r);pc=pivots(R,r);del H,R
 need(r==N5 and pc==list(range(N5)),"actual full original H5 rank1287 modulo31")
 check()
 HT=nmod_mat(N5,NH,[row.get(j,0)%31 for j in range(N5) for row in h],31)
 RT,rr=HT.rref();need(int(rr)==N5,"actual transposed H5 rank");pr=pivots(RT,N5);del HT,RT
 U=nmod_mat(N5,N5,[h[i].get(j,0)%31 for i in pr for j in range(N5)],31);det=int(U.det())%31;del U
 need(det!=0,"actual original H5 unit minor")
 pp=out/"original-h5-field-unit-profile.json.gz"
 save(pp,{"binding":bind,"normalFiveBlockIdentity":identity(bp),"highPairIdentity":identity(pair),
 "prime":31,"rows":NH,"columns":N5,"rankModulo31":N5,"selectedHighRowIndices":pr,
 "selectedOriginalSourcePositions":[high[i] for i in pr],"unitDeterminantModulo31":det,
 "fullQColumnRankProvedByMinor":True,"allOriginalHighRowsRetained":True})
 rec={"status":"completed","binding":bind,"outcome":"complete-original-h5-unit-profile",
 "rankH5Modulo31":N5,"rankH5OverQ":N5,"actualH5UnitDeterminantModulo31":det,
 "all4354OriginalM5RowsConstructed":True,"allOriginalNonhighRowsZero":True,
 "all1736HighRowsRetained":True,"all1485NormalFourCompensationColumnsRetained":True,
 "sourceNormalDegreeHistogram":dict(sorted(collections.Counter(map(str,degrees)).items())),
 "outputs":[{"file":p.name,**identity(p)} for p in [bp,pair,pp]]}
 save(cp,rec);gc.collect();return rec
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["regauged-out","rebuild-root","normal-four-out","out"]:ap.add_argument("--"+k,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--candidate-rows",type=int,default=64);ap.add_argument("--max-nnz",type=int,default=500000)
 ap.add_argument("--max-integer-bits",type=int,default=8192);ap.add_argument("--max-pivot-work",type=int,default=150000)
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 0<a.seconds<=120 and 0<a.memory_mib<=4096,"finite shared high-only budget")
 need(1<=a.candidate_rows<=128 and 1<=a.max_nnz<=1000000 and 1<=a.max_integer_bits<=16384 and
 1<=a.max_pivot_work<=300000,"explicit low-fill and height gates")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 signal.signal(signal.SIGTERM,signal_stop);signal.signal(signal.SIGINT,signal_stop)
 start=time.monotonic();deadline=start+a.seconds-min(5,a.seconds/10)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True);prep=out/"prepared"
 rec={"format":"isp-selected-normal-five-high-elimination-v1","status":"running","phase":"paid-inputs",
 "newM0RightHandSidesSolved":0,"oldNormalFourKernelRecomputed":False,
 "old130AdditionalUnitSolutionsRecomputed":False,"normalFiveSecondEnvelopeComputed":False,
 "allFinalOriginalSecondProductsVerified":False,"leadingUnitProved":False,
 "largeDataUploadedOrCommitted":False,"parameters":{},"events":[]}
 binding=None;rows={};active=set();dag=[];scales=[];rowlabels={};pair_id=None
 nnz=0;maxbits=0;updates=0;newpivots=0;pending_started=False;generation=-1;slot=-1;last_checkpoint=None;initial_pivots=0
 stop_reason="not-started";code=1;state_ready=False
 def check():
  if STOP or time.monotonic()>=deadline:raise BudgetExpired("shared high elimination time or signal boundary")
 def checkpoint(reason):
  nonlocal generation,slot,last_checkpoint
  if binding is None or pair_id is None:return
  state={"format":"isp-normal-five-high-exact-state-v1","binding":binding,"inputPairIdentity":pair_id,
  "remainingNormalFiveColumns":sorted(active),"remainingRows":[{"originalSourcePosition":i,
  "originalSourceRow":rowlabels[i],"coefficients":[[j,str(v)] for j,v in sorted(rows[i].items())]} for i in sorted(rows)],
  "reverseSubstitutionDAG":dag,"initialRowContentDivisors":scales,
  "committedPivots":len(dag),"stopReason":reason,"everyCommittedPivotComplete":True,
  "all1485NormalFourColumnsRetained":True,"originalHighEquationKernelPreservedOverQ":True}
  slot=1-slot if slot in [0,1] else 0;generation+=1
  sp=out/("normal-five-high-state-slot%d.json.gz"%slot);si=save(sp,state)
  ptr={"binding":binding,"generation":generation,"activeSlot":slot,"stateIdentity":si,
  "committedPivots":len(dag),"remainingNormalFiveColumns":len(active),"remainingHighRows":len(rows)}
  save(out/"normal-five-high-active-checkpoint.json",ptr);last_checkpoint=ptr
 def finish_receipt():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"normal-five-high-elimination-receipt.json",rec)
 try:
  paths={"old_unit":a.regauged_out/"prepared"/"second-left-m0-unit-input.json.gz",
  "coefficients":a.rebuild_root/"rebuilt-first"/"same-original-natural-constant-and-first-coefficients.json.gz",
  "profile":a.rebuild_root/"rebuilt-inputs"/"same-selected-original-output-indices.json",
  "paid_m4":a.normal_four_out/"paid-high"/"complete-original-normal-four-block.json.gz",
  "paid_full":a.normal_four_out/"full-products"/"normal-four-full-products-receipt.json"}
  ids={k:identity(p) for k,p in paths.items()}
  for k,v in ids.items():need(v=={"bytes":PINS[k][0],"sha256":PINS[k][1]},"actual pinned input "+k)
  material={"programIdentity":identity(__file__),"inputIdentities":ids,"paidNormalFourBinding":PAID_NORMAL4,
  "pivotColumnCount":N5,"attachedColumnCount":N4,"originalHighRowCount":NH,
  "candidateRows":a.candidate_rows,"maxNnz":a.max_nnz,"maxIntegerBits":a.max_integer_bits,
  "maxSinglePivotWork":a.max_pivot_work}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["parameters"].update(material);rec["parameters"].update(binding=binding,secondsLimit=a.seconds,memoryMiB=a.memory_mib)
  rec["phase"]="construct-original-H5-and-unit-profile";finish_receipt()
  pr=prepare(paths,ids,prep,binding,check);rec["parameters"]["actualPreparation"]=pr;check()
  pair_path=prep/"complete-original-high-normal-five-and-four.json.gz";pair_id=identity(pair_path)
  ptrpath=out/"normal-five-high-active-checkpoint.json"
  if ptrpath.exists():
   ptr=read(ptrpath);need(ptr["binding"]==binding,"same active portable checkpoint")
   sp=out/ptr["stateIdentity"]["file"];need(identity(sp)=={k:ptr["stateIdentity"][k] for k in ["bytes","sha256"]},"whole active state SHA")
   st=read(sp);need(st["binding"]==binding and st["inputPairIdentity"]==pair_id and st["everyCommittedPivotComplete"],"same actual high equations")
   active=set(map(int,st["remainingNormalFiveColumns"]));dag=st["reverseSubstitutionDAG"];scales=st["initialRowContentDivisors"]
   for r in st["remainingRows"]:
    i=int(r["originalSourcePosition"]);rows[i]={int(j):int(v) for j,v in r["coefficients"]};rowlabels[i]=int(r["originalSourceRow"])
   slot=int(ptr["activeSlot"]);generation=int(ptr["generation"]);last_checkpoint=ptr;initial_pivots=len(dag)
  else:
   data=read(pair_path);need(data["binding"]==binding and data["firstPivotColumns"]==1287 and
   data["attachedNormalFourColumns"]==1485 and len(data["rows"])==1736,"complete exact original high pair")
   active=set(range(N5))
   for r in data["rows"]:
    i=int(r["originalSourcePosition"]);row={int(j):int(v) for j,v in r["coefficients"]}
    row,g=primitive(row);rows[i]=row;rowlabels[i]=int(r["originalSourceRow"])
    if g!=1:scales.append([i,str(g)])
  need(len(active)+len(dag)==1287 and len(rows)+len(dag)==1736 and
 len({int(r["normalFiveColumn"]) for r in dag})==len(dag),"actual rectangular pivot accounting")
  need(all((j in active) or (N5<=j<N5+N4) for row in rows.values() for j in row),
  "all remaining H5 and every attached H4 coordinate")
  state_ready=True
  if not ptrpath.exists():checkpoint("initial-complete-original-high-system")
  incidence={j:set() for j in active}
  for i,row in rows.items():
   for j in row:
    if j in active:incidence[j].add(i)
  revision={i:0 for i in rows}
  heap=[(len(row),i,0) for i,row in rows.items() if any(j in active for j in row)];heapq.heapify(heap)
  nnz=sum(map(len,rows.values()));maxbits=max((abs(v).bit_length() for row in rows.values() for v in row.values()),default=0)
  last_save=time.monotonic();rec["phase"]="exact-H5-only-pivots";finish_receipt()
  stop_reason="all1287-H5-columns-eliminated"
  while active:
   check();chosen=[]
   while heap and len(chosen)<a.candidate_rows:
    length,i,ver=heapq.heappop(heap)
    if i in rows and revision[i]==ver and len(rows[i])==length and any(j in active for j in rows[i]):chosen.append((length,i,ver))
   need(chosen,"full-column-rank remaining H5 has actual pivots")
   for item in chosen:heapq.heappush(heap,item)
   candidates=[]
   for length,i,ver in chosen:
    for j,v in rows[i].items():
     if j in active:candidates.append(((length-1)*(len(incidence[j])-1),abs(v).bit_length(),i,j))
   candidates.sort();pick=None
   for score,bits,i,j in candidates[:128]:
    work=sum(len(rows[r])+len(rows[i]) for r in incidence[j] if r!=i)
    if work<=a.max_pivot_work:pick=(score,i,j,work);break
   if pick is None:raise ResourceGate("single-pivot work gate; exact current equations saved")
   score,i,j,work=pick;pv=rows[i].copy();aa=pv[j];need(aa!=0,"actual nonzero rational H5 pivot")
   affected=sorted(incidence[j]-{i});pending={};pending_nnz=nnz-len(pv);pending_bits=0;pending_started=True
   for z,r in enumerate(affected):
    oldrow=rows[r];bb=oldrow[j];g=math.gcd(abs(aa),abs(bb));mul=aa//g;sub=bb//g
    rr={c:mul*v for c,v in oldrow.items()}
    for c,v in pv.items():rr[c]=rr.get(c,0)-sub*v
    rr={c:v for c,v in rr.items() if v};need(j not in rr,"exact H5 pivot cancellation")
    rr,gc0=primitive(rr);hb=max((abs(v).bit_length() for v in rr.values()),default=0)
    if hb>a.max_integer_bits:raise ResourceGate("pending row height gate; uncommitted pivot discarded")
    pending_nnz+=len(rr)-len(oldrow);pending_bits=max(pending_bits,hb);pending[r]=rr
    if z%8==0:check()
   if pending_nnz>a.max_nnz:raise ResourceGate("pending complete fill gate; uncommitted pivot discarded")
   check()
   for r,rr in pending.items():
    oldrow=rows[r]
    for c in oldrow.keys()-rr.keys():
     if c in active:incidence[c].discard(r)
    for c in rr.keys()-oldrow.keys():
     if c in active:incidence[c].add(r)
    rows[r]=rr;revision[r]+=1
    if any(c in active and c!=j for c in rr):heapq.heappush(heap,(len(rr),r,revision[r]))
   for c in pv:
    if c in active:incidence[c].discard(i)
   del rows[i];revision.pop(i);active.remove(j);incidence.pop(j)
   dag.append({"originalSourcePosition":i,"originalSourceRow":rowlabels[i],
   "normalFiveColumn":j,"pivotCoefficient":str(aa),
   "otherTerms":[[c,str(v)] for c,v in sorted(pv.items()) if c!=j],
   "estimatedSinglePivotWork":work,"lowFillScore":score})
   newpivots+=1;updates+=len(affected);nnz=pending_nnz;maxbits=max(maxbits,pending_bits);pending_started=False
   if len(heap)>max(10000,4*len(rows)):
    heap=[(len(row),r,revision[r]) for r,row in rows.items() if any(c in active for c in row)];heapq.heapify(heap)
   if newpivots%50==0 or time.monotonic()-last_save>=5:
    checkpoint("complete-pivot-checkpoint");last_save=time.monotonic()
    rec["events"].append({"committedPivots":len(dag),"remainingH5":len(active),"remainingRows":len(rows),
    "nnz":nnz,"heightUpperBound":maxbits,"elapsedSeconds":time.monotonic()-start})
    finish_receipt()
  need(len(rows)==449 and all(all(c>=N5 for c in row) for row in rows.values()),"all449 original high residual rows retained")
  schur={"format":"isp-complete-normal-five-high-normal-four-schur-v1","binding":binding,
  "originalHighPairIdentity":pair_id,"pivotNormalFiveColumns":1287,"normalFourColumns":1485,
  "rows":[{"originalSourcePosition":i,"originalSourceRow":rowlabels[i],
  "normalFourCoefficients":[[j-N5,str(v)] for j,v in sorted(rows[i].items())]} for i in sorted(rows)],
  "reverseSubstitutionDAG":dag,"all1736HighEquationsEquivalentOverQ":True,
  "normalFiveCorrectionUniqueGivenNormalFour":True,"normalFourCorrectionNotSetToZero":True}
  si=save(out/"complete-high-normal-four-schur.json.gz",schur)
  rec["parameters"]["completeHighSchur"]=si
  rec.update(status="completed",outcome="complete-normal-five-high-schur",
  completeExactH5Elimination=True,all1287H5PivotsSaved=True,remainingHighRows=449,
  all1485NormalFourCompensationColumnsRetained=True);code=0
 except ResourceGate as e:
  stop_reason=str(e);rec.update(status="completed-prefix",outcome="bounded-high-elimination-prefix",
  error=str(e),completeExactH5Elimination=False);code=75
 except BudgetExpired as e:
  stop_reason=str(e);rec.update(status="checkpointed-time-budget",outcome="checkpointed-time-budget",
  error=str(e),completeExactH5Elimination=False);code=75
 except Exception as e:
  stop_reason=str(e);rec.update(status="failed-or-incomplete",outcome="failed-or-incomplete",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8");code=1
 finally:
  rec["completedMathematicalSecondsBeforeFinalCheckpoint"]=time.monotonic()-start
  if state_ready:
   need(len(active)+len(dag)==1287 and len(rows)+len(dag)==1736,"whole committed exact checkpoint dimensions")
   t=time.monotonic();checkpoint(stop_reason);rec["finalCheckpointSeconds"]=time.monotonic()-t
   rec.update(inheritedExactPivots=initial_pivots,newExactPivots=newpivots,committedExactPivots=len(dag),
   remainingNormalFiveColumns=len(active),remainingHighRows=len(rows),
   remainingNonzeroEntries=sum(map(len,rows.values())),
   remainingMaximumIntegerBits=max((abs(v).bit_length() for row in rows.values() for v in row.values()),default=0),
   exactRowUpdatesThisRun=updates,everyCommittedPivotComplete=True,partialPivotDiscarded=pending_started,
   originalHighEquationKernelPreservedOverQ=True)
   rec["parameters"]["actualTemporaryCheckpoint"]=last_checkpoint
  rec["parameters"]["normalFiveNoNewSecondHeadClaim"]=True;finish_receipt()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))

