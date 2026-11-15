#!/usr/bin/env python3
"""Prepare the exact-Q selected Koszul outside equations, with a reversible sparse DAG.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only this bounded preparation is executed; no Q solve is claimed here.
"""
import argparse,collections,gzip,hashlib,importlib.util,itertools,json,math,os,pathlib,resource,sys,time,traceback
sys.dont_write_bytecode=True
H_SHA="9332d9d394b1a17444c9ccc20b3971cf74b7e932cffc8d9189e4e2f64fe0c428"
P_SHA="97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"
S_SHA="5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"
def sha(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def need(b,s):
 if not b:raise ValueError(s)
def save(p,x,gz=False):
 p=pathlib.Path(p);q=p.with_name(p.name+".tmp")
 if gz:
  with gzip.open(q,"wt",encoding="utf-8",compresslevel=1) as f:json.dump(x,f,separators=(",",":"))
 else:q.write_text(json.dumps(x,separators=(",",":"))+"\n")
 os.replace(q,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["helper","native-model","point-model","selected-receipt","out"]:ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args();need(0<a.seconds<=60,"bounded preparation <=60s")
 need(0<a.memory_mib<=2048,"memory <=2048MiB")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-2
 out=a.out.resolve();need(not out.exists() or not any(out.iterdir()),"fresh directory");out.mkdir(parents=True,exist_ok=True)
 r={"format":"isp-koszul-exact-outside-sparse-preparation-v1","status":"running","parameters":{},"largeDataUploadedOrCommitted":False,"characteristicZeroKernelConstructed":False,"oldNormalFormsRecomputed":False,"newDixonDigitsComputed":0}
 temp=[];code=1
 def check():
  if time.monotonic()>=deadline:raise TimeoutError("shared preparation budget")
 try:
  need(sha(a.helper)["sha256"]==H_SHA,"helper SHA");need(sha(a.point_model)["sha256"]==P_SHA,"point SHA");need(sha(a.selected_receipt)["sha256"]==S_SHA,"selected dictionary SHA")
  sp=importlib.util.spec_from_file_location("paid_helper",a.helper);H=importlib.util.module_from_spec(sp);sp.loader.exec_module(H)
  point=json.loads(a.point_model.read_text());sr=json.loads(a.selected_receipt.read_text())
  selected=H.read_native_selected(a.native_model,point)
  need(len(selected)==4354 and sr["selectedFullConstantRankModulo31"]==4318,"selected4354")
  free=list(map(int,sr["selectedConstantKernelFreeOriginalRows"]));need(len(free)==36,"free36")
  outside=[i for i in range(1,6189) if i not in selected];need(len(outside)==1834,"outside1834")
  c=[[int(x) for x in v] for v in point["primitivePointCoefficients"]]
  need(len(c)==17 and all(len(v)==77 for v in c),"17x77 original integer coefficients")
  vv=[8**i for i in range(11)]
  mm=[sum(vv[i] for i in q) for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
  mi={v:i for i,v in enumerate(mm)};terms=vv+[vv[i]+vv[j] for i in range(11) for j in range(i,11)]
  phi=[{} for _ in range(6188)];col=0
  for i in range(17):
   for j in range(i+1,17):
    for factor in [0]+vv:
     for eq,pol,sgn in [(i,j,1),(j,i,-1)]:
      for key,v in zip(terms,c[pol]):
       if v:
        row=17*mi[key+factor]+eq
        phi[row][col]=phi[row].get(col,0)+sgn*v
     col+=1
    check()
  need(col==1632,"full1632 family")
  phi=[{j:v for j,v in row.items() if v} for row in phi]
  original=[dict(phi[i-1]) for i in outside]
  binding_material={"scriptSHA256":sha(__file__)["sha256"],"helperSHA256":H_SHA,"pointSHA256":P_SHA,"nativeModelSHA256":H.NATIVE_SHA,"selectedSHA256":S_SHA,"family":"i<j lex; multiplier1,m0,...,m10"}
  binding=hashlib.sha256(json.dumps(binding_material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  original_path=out/"exact-original-koszul-outside-model.json.gz"
  original_data={"format":"isp-exact-integer-koszul-source-model-v1","binding":binding,"inputIdentity":binding_material,"outsideRows":outside,"freeRows":free,"selectedRows":sorted(selected),"phiRows":[[[j,str(v)] for j,v in sorted(row.items())] for row in phi],"outsideRowCount":1834,"sourceCount":6188,"familyColumns":1632}
  temp.append(save(original_path,original_data,True))
  rows=[dict(x) for x in original];active=set(range(1632));inc=[set() for _ in range(1632)]
  for i,row in enumerate(rows):
   for j in row:inc[j].add(i)
  queue=collections.deque(i for i,row in enumerate(rows) if 0<len(row)<=2)
  dag=[];nonunit=0;rowops=0
  while queue:
   check();ri=queue.popleft();row=rows[ri]
   if not 0<len(row)<=2:continue
   keys=list(row)
   pivot=min(keys,key=lambda j:(len(inc[j]),j))
   target=next((j for j in keys if j!=pivot),None)
   aa=row[pivot];bb=0 if target is None else row[target]
   need(aa!=0 and pivot in active,"active pivot")
   dag.append({"pivot":pivot,"target":target,"a":str(aa),"b":str(bb),"equationRow":ri})
   nonunit+=int(aa%31==0)
   affected=list(inc[pivot])
   for rr in affected:
    old=rows[rr]
    if rr==ri:
     for j in old:inc[j].discard(rr)
     rows[rr]={};continue
    cc=old[pivot]
    new={j:(aa*v if target is not None else v) for j,v in old.items() if j!=pivot}
    if target is not None:new[target]=new.get(target,0)-cc*bb
    new={j:v for j,v in new.items() if v}
    if new:
     g=0
     for v in new.values():g=math.gcd(g,abs(v))
     sg=-1 if new[min(new)]<0 else 1
     if g!=1 or sg==-1:new={j:sg*(v//g) for j,v in new.items()}
    for j in old:
     if j not in new:inc[j].discard(rr)
    for j in new:
     if j not in old:inc[j].add(rr)
    rows[rr]=new;rowops+=1
    if 0<len(new)<=2:queue.append(rr)
   active.remove(pivot);inc[pivot].clear()
  check()
  av=sorted(active);row_ids=[i for i,row in enumerate(rows) if row];ci={j:i for i,j in enumerate(av)}
  core_path=out/"exact-koszul-sparse-core-and-dag.json.gz"
  core={"format":"isp-exact-koszul-sparse-core-v1","binding":binding,"originalModel":temp[0],"activeVariables":av,"coreOriginalRowIds":row_ids,"coreRows":[[[j,str(v)] for j,v in sorted(rows[i].items())] for i in row_ids],"eliminationDAG":dag,"everyEliminationIsExactOverQ":True,"divisionBy31AllowedOnlyAsQOperation":True}
  temp.append(save(core_path,core,True))
  r.update({"status":"completed","originalOutsideRows":1834,"originalKoszulVariables":1632,"peeledVariables":len(dag),"remainingVariables":len(av),"remainingNonzeroRows":len(row_ids),"exactIntegerRowOperations":rowops,"eliminationPivotsDivisibleBy31":nonunit,"exactQKernelBijectionRecorded":True})
  r["parameters"].update({"binding":binding,"inputIdentity":binding_material,"temporaryFiles":temp,"nonzeroOriginalOutsideEntries":sum(map(len,original)),"nonzeroRemainingEntries":sum(len(rows[i]) for i in row_ids),"maximumRemainingIntegerCoefficientBits":max((abs(v).bit_length() for i in row_ids for v in rows[i].values()),default=0),"nextStep":"select a mod31 unit block in the exact core; exact-Q solve, complete residual kernel, reverse DAG, complete6188 support and4367 products","noClaimOfMod31ProfilePreservationAfterQPeeling":True})
  code=0
 except TimeoutError as e:r.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:
  r.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  r["parameters"]["temporaryFiles"]=temp;r["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"koszul-exact-sparse-preparation-receipt.json",r)
 print(json.dumps(r),flush=True);return code
if __name__=="__main__":sys.exit(main())
