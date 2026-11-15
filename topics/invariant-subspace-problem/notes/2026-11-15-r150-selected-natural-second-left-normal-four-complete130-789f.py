#!/usr/bin/env python3
"""R150 consume the proved130-dimensional high kernel; only new unit solves.
Author Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Retain the complete1736-row high kernel, old36 exact unit solutions,
and every original4354 source product. Recomputable arrays are temporary only.
"""
import argparse,gzip,hashlib,io,itertools,json,math,os,pathlib,resource,signal,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
os.environ["OPENBLAS_NUM_THREADS"]="1"
os.environ["OMP_NUM_THREADS"]="1"
class BudgetExpired(Exception):pass
class NextActualKernelShape(Exception):pass
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
    with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as f:json.dump(v,f,separators=(",",":"),sort_keys=True)
 else:
  b=json.dumps(v,separators=(",",":"),sort_keys=True).encode()
  need(len(b)<100000,"only small uncompressed receipts/metadata")
  q.write_bytes(b)
 os.replace(q,p);return {"file":p.name,**identity(p),"temporaryOnly":True}
def pivots(R,rank):
 ans=[]
 for i in range(int(rank)):
  j=next((j for j in range(R.ncols()) if R[i,j]),None)
  need(j is not None and R[i,j]==1,"complete normalized RREF pivot");ans.append(j)
 need(ans==sorted(set(ans)),"strict RREF pivot order");return ans
def primitive_q(values):
 den=1
 for v in values:den=math.lcm(den,int(v.q))
 z=[int(v.p)*(den//int(v.q)) for v in values];g=0
 for v in z:g=math.gcd(g,abs(v))
 need(g>0,"nonzero exact kernel column")
 sign=-1 if next(v for v in z if v)<0 else 1
 return [sign*(v//g) for v in z]

PAID_BINDING="c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e"
HIGH_BINDING="c18a0a21f0ca0e44aeaa65c138bbf02e5b26fc7d01542573aef47dbc7b532fec"
PINS={
 "old_unit":(9008513,"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"),
 "old_solution":(18124389,"9c3b02d2674af645ffcfd5297cf5c9ac287fe314d0c40f49c8bb99be9396352d"),
 "old_full":(12690,"b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70"),
 "old_main":(20323,"2343123363d6c38a871c66770afb67b37a1b3a6b882baa7aed040134914a345b"),
 "old_rref":(17625,"de7bb03e76ca2dee0221d4f89e1de5db190b6c5b64fc4df70a67e13f405a7941"),
 "coefficients":(20580,"7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1"),
 "profile":(21066,"044b28d717749d23a2959a02c0f8ed7570bfa19bcdff04207056f2a66d2e413d"),
 "paid_high_block":(911018,"88d9f609c39c754913beaf06c4b5e945ce84fde5c0a0bde78f7e57216bd33f0e"),
 "paid_high_kernel":(1446855,"46b047a303d68a3502aa076836f77dc0fde101ca93d6df2c8568380f2d190d63"),
 "paid_high_main":(5667,"161e2a48e5b82fd26c67a9100b95e75b88ce85ecb395eb59dc84a760c637aa34")}
WORKER=(16412,"c9e1eee6142d29daf661682e177702825e90aef7222611baa2adadaffe0dc731")
ACTUAL_K=130
UNIT_BATCH=32
def input_paths(a):
 o=a.regauged_out;h=a.high_prefix
 return {"old_unit":o/"prepared"/"second-left-m0-unit-input.json.gz",
 "old_solution":o/"unit-solve"/"complete-m0-unit-solution.json.gz",
 "old_full":o/"full-products"/"second-left-full-products-receipt.json",
 "old_main":o/"selected-natural-second-left-regauged-pipeline-receipt.json",
 "old_rref":o/"full-products"/"complete-small-second-residual-rref.json.gz",
 "coefficients":a.rebuild_root/"rebuilt-first"/"same-original-natural-constant-and-first-coefficients.json.gz",
 "profile":a.rebuild_root/"rebuilt-inputs"/"same-selected-original-output-indices.json",
 "paid_high_block":h/"high-profile"/"complete-original-normal-four-block.json.gz",
 "paid_high_kernel":h/"high-kernel"/"complete-original-normal-four-high-kernel.json.gz",
 "paid_high_main":h/"selected-natural-second-left-normal-four-continue-receipt.json"}
def load_inv(p):
 v=read(p)
 for k,path in v["paths"].items():need(identity(path)==v["inputIdentities"][k],"same actual input "+k)
 need(identity(__file__)==v["programIdentity"],"same normal-four source")
 return v
def completed(path,binding):
 if not path.exists():return None
 r=read(path);need(r["binding"]==binding,"same exact stage binding")
 if r["status"]!="completed":return None
 for t in r.get("outputs",[]):need(identity(path.parent/t["file"])=={"bytes":t["bytes"],"sha256":t["sha256"]},"same completed array "+t["file"])
 return r
def stage_rec(out,name,bind,phase):
 out.mkdir(parents=True,exist_ok=True);cp=out/name;start=time.monotonic()
 rec={"status":"running","binding":bind,"phase":phase,"outputs":[],"parameters":{}}
 def ck():
  rec["elapsedSeconds"]=time.monotonic()-start;save(cp,rec)
 ck();return cp,rec,ck
def reuse_high_worker(invpath,out):
 inv=load_inv(invpath);bind=inv["binding"];out=pathlib.Path(out)
 cp=out/"normal-four-paid-high-reuse-receipt.json";cc=completed(cp,bind)
 if cc:print(json.dumps({"status":"completed","reused":True}),flush=True);return 0
 cp,rec,ck=stage_rec(out,cp.name,bind,"reuse-complete-rational-high-kernel")
 b=read(inv["paths"]["paid_high_block"]);kd=read(inv["paths"]["paid_high_kernel"])
 paid=read(inv["paths"]["paid_high_main"]);p=paid["parameters"];h=p["completeHighKernel"]
 need(b["binding"]==kd["binding"]==p["binding"]==HIGH_BINDING and
 kd["blockIdentity"]==inv["inputIdentities"]["paid_high_block"],"same actual complete high block and kernel")
 need(paid["status"]=="completed-prefix" and paid["outcome"]=="actual-high-kernel-needs-wider-next-worker" and
 h["status"]=="completed" and h["rankHighOverQ"]==1355 and h["highKernelDimension"]==130 and
 h["extraRationalSchurRank"]==0 and h["all1736OriginalHighProductsZero"] and
 h["originalHighProductCoordinates"]==225680,"actual proved130 high kernel, not a field inference")
 need(kd["kernelDimension"]==130 and kd["completeRationalKernelProved"] and
 kd["all1736OriginalHighProductsZero"] and len(kd["primitiveIntegerKernelColumns"])==130 and
 all(len(c)==1485 for c in kd["primitiveIntegerKernelColumns"]),"all proved1485-coordinate high kernel columns")
 old=read(inv["paths"]["old_unit"])
 need(b["originalSourceRows"]==old["originalSourceRows"] and
 b["highOriginalRowPositions"]==old["oldZeroRowPositions"] and b["all1736OldCorrectionAndForcingRowsZero"],
 "same complete old zero rows and source coordinates")
 bp=out/"complete-original-normal-four-block.json.gz"
 kp=out/"complete-original-normal-four-high-kernel.json.gz"
 b={**b,"binding":bind,"inheritedCompleteHighBinding":HIGH_BINDING,
 "inheritedOriginalBlockIdentity":inv["inputIdentities"]["paid_high_block"],"originalM4EntriesReconstructed":False}
 save(bp,b)
 kd={**kd,"binding":bind,"blockIdentity":identity(bp),"inheritedCompleteHighBinding":HIGH_BINDING,
 "inheritedCompleteKernelIdentity":inv["inputIdentities"]["paid_high_kernel"],"highRationalSolveRecomputed":False}
 save(kp,kd)
 rec["outputs"]=[{"file":bp.name,**identity(bp)},{"file":kp.name,**identity(kp)}]
 rec.update(status="completed",phase="complete",outcome="complete-rational-high-kernel-reused",
 completeRationalHighKernelProved=True,rankHighOverQ=1355,highKernelDimension=130,
 inheritedHighProductCoordinates=225680,originalM4EntriesReconstructed=False,
 originalUnitProfileRecomputed=False,highRationalSolveRecomputed=False,
 all1736OldCorrectionAndForcingRowsZero=True)
 ck();print(json.dumps({k:v for k,v in rec.items() if k!="outputs"}),flush=True);return 0
def images_worker(invpath,out,profiledir,highdir):
 inv=load_inv(invpath);bind=inv["binding"];out=pathlib.Path(out);profiledir=pathlib.Path(profiledir);highdir=pathlib.Path(highdir)
 cp=out/"normal-four-new-images-receipt.json";cc=completed(cp,bind)
 if cc:print(json.dumps({"status":"completed","reused":True}),flush=True);return 0
 cp,rec,ck=stage_rec(out,cp.name,bind,"actual-full-original-new-images")
 bp=profiledir/"complete-original-normal-four-block.json.gz";kp=highdir/"complete-original-normal-four-high-kernel.json.gz"
 b=read(bp);kdata=read(kp);old=read(inv["paths"]["old_unit"])
 need(b["binding"]==kdata["binding"]==bind and kdata["blockIdentity"]==identity(bp) and
 kdata["completeRationalKernelProved"] and kdata["all1736OriginalHighProductsZero"],"same complete true high kernel")
 K=[[int(v) for v in c] for c in kdata["primitiveIntegerKernelColumns"]];k=len(K)
 need(k==kdata["kernelDimension"] and k==ACTUAL_K and all(len(c)==1485 for c in K),"all actual high kernel columns")
 rows=[[(int(j),int(v)) for j,v in row] for row in b["originalNormalFourRows"]]
 W=[[sum(a*K[c][j] for j,a in row) for c in range(k)] for row in rows]
 need(len(W)==4354 and all(not any(W[i]) for i in b["highOriginalRowPositions"]),"all original new high products zero")
 wp=out/"complete-original-normal-four-kernel-images.json.gz"
 w={"binding":bind,"blockIdentity":identity(bp),"highKernelIdentity":identity(kp),
 "originalSourceRows":b["originalSourceRows"],"kernelDimension":k,
 "originalImageRows":[[str(v) for v in r] for r in W],
 "all1736HighRowsZero":True,"all4354OriginalRowsConstructed":True}
 save(wp,w);rec["outputs"]=[{"file":wp.name,**identity(wp)}]
 if k:
  up=out/"additional-left-m0-unit-input.json.gz"
  unit={**old,"binding":bind,"format":"isp-selected-second-left-unit-input-v1","rhsColumns":k,
  "originalRightHandSideRows":[[str(v) for v in r] for r in W],
  "forcingIdentity":identity(wp),"previousUnitInputIdentity":inv["inputIdentities"]["old_unit"],
  "highKernelIdentity":identity(kp),"old36RightHandSidesRecomputed":False,
  "originalRightHandSideRowsUnchanged":False,
  "secondFamilyFormula":"auxiliary equations M0_new*x+M4*Z4*a=0; full second family is recorded by the outer original-product stage",
  "newRightHandSidesAreExactlyActualHighKernelImages":True}
  need(unit["originalCorrectionRows"]==old["originalCorrectionRows"] and
  unit["selectedUnitRowIndices"]==old["selectedUnitRowIndices"],"same complete old M0 unit block reused")
  save(up,unit);rec["outputs"].append({"file":up.name,**identity(up)})
  parentid=identity(up);batch_records=[]
  for lo in range(0,k,UNIT_BATCH):
   hi=min(k,lo+UNIT_BATCH);q=out/("additional-unit-input-%03d-%03d.json.gz"%(lo,hi-1))
   batch={**unit,"rhsColumns":hi-lo,"originalRightHandSideRows":[r[lo:hi] for r in unit["originalRightHandSideRows"]],
   "parentCompleteUnitInputIdentity":parentid,"actualHighKernelGlobalColumnIndices":list(range(lo,hi)),
   "actualBatchColumns":hi-lo,"totalActualHighKernelColumns":k}
   save(q,batch);ident={"file":q.name,**identity(q)}
   rec["outputs"].append(ident);batch_records.append({"first":lo,"stop":hi,"input":ident})
  rec["batchInputs"]=batch_records
 rec.update(status="completed",phase="complete",outcome="ready-for-actual-additional-unit-solve" if k else "normal-four-high-kernel-zero",
 highKernelDimension=k,additionalUnitRightHandSides=k,old36ExactUnitSolutionsReused=True,
 old36RightHandSidesRecomputed=False,all4354OriginalNewImagesConstructed=True,all1736HighRowsZero=True)
 ck();print(json.dumps({k:v for k,v in rec.items() if k!="outputs"}),flush=True);return 0
def assemble_worker(invpath,out,imagesdir):
 inv=load_inv(invpath);bind=inv["binding"];out=pathlib.Path(out);imagesdir=pathlib.Path(imagesdir)
 cp=out/"m0-unit-solve-receipt.json";cc=completed(cp,bind)
 if cc:print(json.dumps({"status":"completed","reused":True}),flush=True);return 0
 cp,rec,ck=stage_rec(out,cp.name,bind,"assemble-complete-verified-130-unit-columns")
 up=imagesdir/"additional-left-m0-unit-input.json.gz";parent=read(up);parentid=identity(up)
 need(parent["binding"]==bind and parent["rhsColumns"]==ACTUAL_K,"same complete130 actual RHS")
 ds=[];cols=[];audit=[];outputs=[]
 for lo in range(0,ACTUAL_K,UNIT_BATCH):
  hi=min(ACTUAL_K,lo+UNIT_BATCH);bd=out/("batch-%03d-%03d"%(lo,hi-1))
  bp=imagesdir/("additional-unit-input-%03d-%03d.json.gz"%(lo,hi-1))
  brp=bd/"m0-unit-solve-receipt.json";sp=bd/"complete-m0-unit-solution.json.gz"
  batch=read(bp);br=read(brp);sol=read(sp);iid=identity(bp);sid=identity(sp)
  need(batch["binding"]==bind and batch["parentCompleteUnitInputIdentity"]==parentid and
  batch["actualHighKernelGlobalColumnIndices"]==list(range(lo,hi)) and
  batch["originalRightHandSideRows"]==[r[lo:hi] for r in parent["originalRightHandSideRows"]] and
  batch["originalCorrectionRows"]==parent["originalCorrectionRows"] and
  batch["selectedUnitRowIndices"]==parent["selectedUnitRowIndices"] and
  batch["rowCoefficientContents"]==parent["rowCoefficientContents"],"complete original actual RHS batch and unchanged unit matrix")
  need(br["status"]=="completed" and br["binding"]==bind and br["inputIdentity"]==iid and
  br["workerSHA256"]==inv["unitWorkerIdentity"]["sha256"] and br["candidateIdentity"]==sid and
  br["all1546OriginalUnitRowsVerified"] and br["originalUnitProductCoordinates"]==1546*(hi-lo) and
  br["verifiedColumnCount"]==hi-lo and sol["binding"]==bind and sol["inputIdentity"]==iid and
  sol["rhsColumns"]==hi-lo and sol["correctionVariables"]==1546,"all complete saved batch columns and original unit products")
  need(len(sol["denominators"])==len(sol["numeratorColumns"])==hi-lo and
  all(int(d)>0 for d in sol["denominators"]) and all(len(c)==1546 for c in sol["numeratorColumns"]),
  "full positive-denominator batch solution")
  ds.extend(sol["denominators"]);cols.extend(sol["numeratorColumns"])
  audit.append({"first":lo,"stop":hi,"inputIdentity":iid,"solutionIdentity":sid,"receiptIdentity":identity(brp),
  "originalUnitProductCoordinates":1546*(hi-lo)})
  outputs.extend([{"file":str(sp.relative_to(out)),**sid},{"file":str(brp.relative_to(out)),**identity(brp)}])
  rec["completedAssembledColumns"]=hi;ck()
 need(len(ds)==len(cols)==130,"all130 actual complete columns")
 sol={"format":"isp-selected-second-left-unit-solution-v1","binding":bind,"inputIdentity":parentid,
 "correctionVariables":1546,"rhsColumns":130,"denominators":ds,"numeratorColumns":cols,
 "candidateOnlyUntilMatchingCompletedReceipt":True,"assembledFromActualVerifiedBatches":audit}
 sp=out/"complete-m0-unit-solution.json.gz";save(sp,sol);sid=identity(sp)
 rec["outputs"]=outputs+[{"file":sp.name,**sid}]
 rec.update(status="completed",phase="complete",format="isp-selected-normal-four-batched-unit-assembly-v1",
 inputIdentity=parentid,candidateIdentity=sid,candidateFile=sp.name,
 all1546OriginalUnitRowsVerified=True,originalUnitProductCoordinates=1546*130,
 completeSolutionSavedBeforeProductVerification=False,completeSolutionAssemblyOnly=True,
 allBatchSolutionsSavedBeforeTheirProductVerification=True,
 verifiedColumnCount=130,lastVerifiedColumn=129,batchCompletion=audit,
 allCompleteRationalColumnsSaved=True,full4354ProductVerificationStillRequiredByCaller=True,
 old36ExactUnitSolutionsRecomputed=False)
 ck();print(json.dumps({k:v for k,v in rec.items() if k!="outputs"}),flush=True);return 0
def finish_worker(invpath,out,profiledir,highdir,imagesdir,unitdir):
 from flint import fmpq,fmpq_mat
 inv=load_inv(invpath);bind=inv["binding"];out=pathlib.Path(out);profiledir=pathlib.Path(profiledir)
 highdir=pathlib.Path(highdir);imagesdir=pathlib.Path(imagesdir);unitdir=pathlib.Path(unitdir)
 cp=out/"normal-four-full-products-receipt.json";cc=completed(cp,bind)
 if cc:print(json.dumps({"status":"completed","reused":True}),flush=True);return 0
 cp,rec,ck=stage_rec(out,cp.name,bind,"actual-old-and-additional-complete-solutions")
 old=read(inv["paths"]["old_unit"]);osol=read(inv["paths"]["old_solution"]);ofull=read(inv["paths"]["old_full"])
 need(old["binding"]==osol["binding"]==ofull["binding"]==PAID_BINDING and
 osol["inputIdentity"]==inv["inputIdentities"]["old_unit"] and ofull["smallResidualRank"]==14,"same paid old exact solve and residual space")
 D=list(map(int,osol["denominators"]));N=[[int(v) for v in c] for c in osol["numeratorColumns"]]
 need(len(D)==len(N)==36 and all(len(c)==1546 for c in N) and all(d>0 for d in D),"all36 old exact columns")
 rows=[[(int(j),int(v)) for j,v in row] for row in old["originalCorrectionRows"]]
 rhs=[[int(v) for v in row] for row in old["originalRightHandSideRows"]]
 bp=profiledir/"complete-original-normal-four-block.json.gz";kp=highdir/"complete-original-normal-four-high-kernel.json.gz"
 wp=imagesdir/"complete-original-normal-four-kernel-images.json.gz"
 b=read(bp);kd=read(kp);w=read(wp)
 need(b["binding"]==kd["binding"]==w["binding"]==bind and
 kd["blockIdentity"]==identity(bp) and w["highKernelIdentity"]==identity(kp) and kd["completeRationalKernelProved"],"same full extra source chain")
 K=[[int(v) for v in c] for c in kd["primitiveIntegerKernelColumns"]];k=len(K)
 W=[[int(v) for v in r] for r in w["originalImageRows"]]
 m4=[[(int(j),int(v)) for j,v in row] for row in b["originalNormalFourRows"]]
 need(k==ACTUAL_K and len(W)==4354 and all(len(r)==k for r in W),"only actual nonzero high kernel here")
 up=imagesdir/"additional-left-m0-unit-input.json.gz";sp=unitdir/"complete-m0-unit-solution.json.gz";ur=read(unitdir/"m0-unit-solve-receipt.json");sol=read(sp)
 upid=identity(up);spid=identity(sp)
 need(sol["binding"]==ur["binding"]==bind and sol["inputIdentity"]==upid and
 ur["status"]=="completed" and ur["all1546OriginalUnitRowsVerified"] and
 ur["candidateIdentity"]==spid and ur["originalUnitProductCoordinates"]==1546*k,"all new complete actual unit products")
 DN=list(map(int,sol["denominators"]));NN=[[int(v) for v in c] for c in sol["numeratorColumns"]]
 need(len(DN)==len(NN)==k and all(len(c)==1546 for c in NN) and all(d>0 for d in DN),"actual k new rational columns")
 residual=[];oldbase=pathlib.Path(inv["paths"]["old_full"]).parent;oldtable={r["file"]:r for r in ofull["outputs"]}
 rec["phase"]="reuse-old36-residuals-and-form-new-columns";ck()
 for c in range(36):
  name="original-residual-column-%02d.json.gz"%c;p=oldbase/name;t=oldtable[name]
  need(identity(p)=={"bytes":t["bytes"],"sha256":t["sha256"]},"same actual old residual "+name)
  r=read(p);need(r["binding"]==PAID_BINDING and r["column"]==c and
  r["unitInputIdentity"]==inv["inputIdentities"]["old_unit"] and
  r["unitSolutionIdentity"]==inv["inputIdentities"]["old_solution"],"full original old residual identity")
  v=list(map(int,r["values"]));need(len(v)==4354 and r["all1546UnitResidualEntriesZero"],"all original old residual rows retained")
  residual.append(v)
 newids=[]
 for c in range(k):
  p=out/("additional-original-residual-column-%02d.json.gz"%c)
  if p.exists():
   r=read(p);need(r["binding"]==bind and r["column"]==c and r["unitInputIdentity"]==upid and
   r["unitSolutionIdentity"]==spid,"same completed new residual")
   v=list(map(int,r["values"]));need(len(v)==4354 and r["all1546UnitResidualEntriesZero"],"complete new residual")
  else:
   v=[DN[c]*W[i][c]+sum(a*NN[c][j] for j,a in row) for i,row in enumerate(rows)]
   need(all(v[i]==0 for i in old["selectedUnitRowIndices"]),"all actual new unit residuals zero")
   r={"binding":bind,"column":c,"unitInputIdentity":upid,"unitSolutionIdentity":spid,
   "values":[str(vv) for vv in v],"all1546UnitResidualEntriesZero":True,"all4354OriginalResidualRowsRetained":True}
   save(p,r)
  residual.append(v);newids.append({"file":p.name,**identity(p)})
  rec["completedAdditionalResidualColumns"]=c+1;rec["outputs"]=newids[:];ck()
 nr=36+k;sr=out/"complete-normal-four-extended-small-residual-rref.json.gz"
 if sr.exists():
  rr=read(sr);need(rr["binding"]==bind and rr["additionalResidualIdentities"]==newids and
  rr["oldFullProductReceiptIdentity"]==inv["inputIdentities"]["old_full"],"same whole extended residual")
  rank=int(rr["rank"]);pp=list(map(int,rr["pivotColumns"]));rrows=[{int(j):fmpq(v) for j,v in r} for r in rr["nonzeroRREFRows"]]
 else:
  inds=[i for i in range(4354) if any(residual[c][i] for c in range(nr))]
  S=fmpq_mat(len(inds),nr,[residual[c][i] for i in inds for c in range(nr)])
  R,rank=S.rref();rank=int(rank);pp=pivots(R,rank)
  rr={"binding":bind,"oldFullProductReceiptIdentity":inv["inputIdentities"]["old_full"],
  "additionalResidualIdentities":newids,"rank":rank,"columns":nr,"pivotColumns":pp,
  "nonzeroOriginalRowIndices":inds,"nonzeroRREFRows":[[[j,str(R[i,j])] for j in range(nr) if R[i,j]] for i in range(rank)]}
  save(sr,rr);rrows=[{j:R[i,j] for j in range(nr) if R[i,j]} for i in range(rank)];del S,R
 need(142<=rank<=144 and pp[:3]==[0,1,2],"paid old residual rank14 and three first-failure axes retained")
 free=[j for j in range(nr) if j not in set(pp)];dim=len(free)
 need(22<=dim<=24,"complete old22 and paid full second lower9")
 GS=[];CS=[]
 for f in free:
  z=[fmpq(0) for _ in range(nr)];z[f]=fmpq(1)
  for row,j in zip(rrows,pp):z[j]=-row.get(f,fmpq(0))
  gam=primitive_q(z);GS.append(gam);CS.append([D[3+j]*gam[3+j] for j in range(33)])
 crank=int(fmpq_mat(33,dim,[CS[c][j] for j in range(33) for c in range(dim)]).rank())
 need(crank==dim,"actual original second-head projection independent; no zero-head directions counted")
 rec.update(phase="all-original-normal-four-second-jets",extendedSmallResidualRank=rank,
 actualHeadProjectionRank=crank,secondHeadImageDimension=dim,newIndependentHeads=dim-22,
 oldResidualRank=14,additionalResidualRankFromProvedInjectivity=130,
 oldNewResidualIntersectionDimension=144-rank,
 completeSmallResidualRREF=identity(sr));rec["outputs"]=newids+[{"file":sr.name,**identity(sr)}];ck()
 candidates=[];verified=[]
 for c,(f,gam) in enumerate(zip(free,GS)):
  p=out/("complete-original-normal-four-second-left-jet-%02d.json.gz"%c);vp=out/("verified-normal-four-second-left-jet-%02d.json"%c)
  if p.exists():
   ca=read(p);need(ca["binding"]==bind and ca["extendedSmallResidualIdentity"]==identity(sr) and
   ca["freeResidualCoordinate"]==f and ca["highKernelIdentity"]==identity(kp),"same true full second candidate")
   x=list(map(int,ca["oldSupportSecondCorrectionVariables"]));eta=list(map(int,ca["normalFourSecondCorrectionVariables"]))
   t=list(map(int,ca["threeFirstHeadComplementCoefficients"]));h=list(map(int,ca["firstHeadKernelCoefficients"]))
  else:
   alpha=[DN[j]*gam[36+j] for j in range(k)]
   x=[sum(N[j][i]*gam[j] for j in range(36))+sum(NN[j][i]*gam[36+j] for j in range(k)) for i in range(1546)]
   eta=[sum(K[j][i]*alpha[j] for j in range(k)) for i in range(1485)]
   t=[D[j]*gam[j] for j in range(3)];h=CS[c]
   ca={"binding":bind,"extendedSmallResidualIdentity":identity(sr),"freeResidualCoordinate":f,
   "oldUnitSolutionIdentity":inv["inputIdentities"]["old_solution"],"additionalUnitSolutionIdentity":spid,
   "highKernelIdentity":identity(kp),"primitiveResidualKernel":[str(v) for v in gam],
   "normalFourKernelCoefficients":[str(v) for v in alpha],
   "oldSupportSecondCorrectionVariables":[str(v) for v in x],"normalFourSecondCorrectionVariables":[str(v) for v in eta],
   "threeFirstHeadComplementCoefficients":[str(v) for v in t],"firstHeadKernelCoefficients":[str(v) for v in h],
   "headComplementCoordinates":old["headComplementCoordinates"],
   "oldFirstCorrectionOutputCoordinates":old["oldFirstCorrectionOutputCoordinates"],
   "oldSupportSecondCorrectionOutputCoordinates":old["secondCorrectionOutputCoordinates"],
   "normalFourOutputCoordinates":b["normalFourOutputCoordinates"],
   "oldFirstSourceIdentities":{j:old["inputIdentities"][j] for j in ["heads","first_jets"]},
   "fullSourceFormula":"lambda0=Lambda*C*c; lambda1=E_old*X*c+Lambda*F*t+Lambda*C*y; lambda2=E_new*x2+E4*eta4+E_old*X*y+Lambda*e",
   "candidateOnlyUntilMatchingVerifiedReceipt":True}
   save(p,ca)
  need(len(x)==1546 and len(eta)==1485 and len(t)==3 and len(h)==33 and h==CS[c],"complete actual candidate and independently checked head")
  cid=identity(p)
  if vp.exists():
   v=read(vp);need(v["binding"]==bind and v["candidateIdentity"]==cid and v["all4354OriginalSecondProductsZero"],"same completed original products")
  else:
   z=t+h
   for i,(a,brow) in enumerate(zip(rows,m4)):
    value=sum(q*x[j] for j,q in a)+sum(q*eta[j] for j,q in brow)+sum(rhs[i][j]*z[j] for j in range(36))
    need(value==0,"original second product at raw source "+str(old["originalSourceRows"][i])+" candidate "+str(c))
   v={"binding":bind,"candidateIdentity":cid,"all4354OriginalSecondProductsZero":True,
   "originalProductCoordinates":4354,"headBasisColumn":c,"completeHeadProjectionRank":crank};save(vp,v)
  candidates.append({"file":p.name,**cid});verified.append({"file":vp.name,**identity(vp)})
  rec["completedOriginalSecondHeadCandidates"]=c+1
  rec["maximumCandidateVariableIntegerBits"]=max(rec.get("maximumCandidateVariableIntegerBits",0),max((abs(v).bit_length() for v in x+eta+t+h),default=0))
  rec["outputs"]=newids+[{"file":sr.name,**identity(sr)}]+candidates+verified;ck()
 rec.update(status="completed",phase="complete",
 outcome="same-selected-second-rank-nine-proved" if dim==24 else "restricted-second-left-support-only",
 selectedSecondConnectionRankOverQLowerBound=9,selectedSecondConnectionRankOverQUpperBound=33-dim,
 selectedSecondConnectionRankExactly9=dim==24,completeSelectedSecondHeadSpaceProved=dim==24,
 completeFixedSupportSecondEnvelopeComputed=True,correctionNormalDegreeAtMost=4,
 all4354OriginalSecondLeftProductsZero=True,fullOriginalSecondJetProductCoordinates=4354*dim,
 allHeadProjectionFreeCoordinatesIndependent=True,allOriginalNormalFourHighConditionsRetained=True,
 allOldFirstKernelFreedomRetained=True,oldFirstKernelFreedomDimension=33,lastCorrectionKernelFreedomDimension=36,
 oldAndNewCorrectionEmbeddingsKeptDistinct=True,old36ExactUnitSolutionsReused=True,
 old36RightHandSidesRecomputed=False,higherCorrectionSupportExcludedAsPremise=False,
 sourceSupportExpansionNeeded=dim<24,leadingUnitProved=False,largeDataUploadedOrCommitted=False)
 ck();print(json.dumps({k:v for k,v in rec.items() if k!="outputs"}),flush=True);return 0

def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for key in ["regauged-out","rebuild-root","high-prefix","unit-worker","out"]:ap.add_argument("--"+key,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=600);ap.add_argument("--memory-mib",type=int,default=4096)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=600 and 0<a.memory_mib<=8192,"explicit bounded actual130 continuation")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds;reserve=min(5,a.seconds/20)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-selected-natural-second-left-normal-four-complete130-v1","status":"running","phase":"paid-actual-inputs",
 "oldFirstRREFRecomputed":False,"old36ExactUnitSolutionsRecomputed":False,"old36RightHandSidesRecomputed":False,
 "oldLargeNormalFormsRecomputed":False,"newOriginalRankPrimeComputed":False,"leadingUnitProved":False,
 "highRationalSolveRecomputed":False,"originalHighProfileRecomputed":False,
 "largeDataUploadedOrCommitted":False,"parameters":{},"events":[]};code=1
 def remain():
  r=deadline-time.monotonic()-reserve
  if r<=0:raise BudgetExpired("shared actual130 mathematical clock")
  return r
 def ck():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start;save(out/"selected-natural-second-left-normal-four-complete130-receipt.json",rec)
 def run(name,cmd,rp):
  rec["phase"]=name;ck();t=time.monotonic();available=remain()
  with (out/(name+".log")).open("a",encoding="utf-8") as log:
   proc=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
   grace=min(20.0,max(.5,available/8)) if name.startswith("additional-unit") else .25
   try:proc.wait(timeout=max(.1,available-grace))
   except subprocess.TimeoutExpired:
    os.killpg(proc.pid,signal.SIGTERM)
    try:proc.wait(timeout=grace)
    except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
    rec["events"].append({"phase":name,"exitCode":proc.returncode,"deadlineStoppedWorker":True,"elapsedSeconds":time.monotonic()-t})
    raise BudgetExpired(name+" incomplete; every returned complete batch remains temporary")
  rec["events"].append({"phase":name,"exitCode":proc.returncode,"elapsedSeconds":time.monotonic()-t})
  if proc.returncode==75:raise BudgetExpired(name+" saved at safe boundary")
  need(proc.returncode==0 and rp.exists(),"actual "+name+" incomplete: "+(out/(name+".log")).read_text(encoding="utf-8",errors="replace")[-1800:])
  r=read(rp);need(r["status"]=="completed","actual "+name+" completion")
  return r
 def local_stage(name,worker,folder,receipt,*extras):
  rp=folder/receipt;c=completed(rp,bind)
  if c:rec["events"].append({"phase":name,"reusedCompleteStage":True});return c
  return run(name,[sys.executable,"-B",str(pathlib.Path(__file__).resolve()),worker,str(ip),str(folder)]+[str(x) for x in extras],rp)
 try:
  paths=input_paths(a);ids={k:identity(v) for k,v in paths.items()}
  for k,v in ids.items():need(v=={"bytes":PINS[k][0],"sha256":PINS[k][1]},"actual paid input "+k)
  wid=identity(a.unit_worker);need(wid=={"bytes":WORKER[0],"sha256":WORKER[1]},"frozen130-cap unit worker")
  material={"programIdentity":identity(__file__),"unitWorkerIdentity":wid,"inputIdentities":ids,
  "previousCompleteSecondBinding":PAID_BINDING,"inheritedCompleteHighBinding":HIGH_BINDING,
  "normalFourCoordinates":1485,"allOriginalHighRows":1736,"allOriginalSourceRows":4354,
  "provedHighKernelDimension":ACTUAL_K,"actualAdditionalUnitBatchColumns":UNIT_BATCH}
  bind=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  inv={**material,"binding":bind,"paths":{k:str(v.resolve()) for k,v in paths.items()}}
  ip=out/"invocation.json";save(ip,inv)
  rec["parameters"].update(material);rec["parameters"].update(binding=bind,secondsLimit=a.seconds,memoryMiBPerProcess=a.memory_mib);ck()
  high=out/"paid-high";images=out/"new-images";unit=out/"additional-unit";finish=out/"full-products"
  hr=local_stage("paid-high","--reuse-high-worker",high,"normal-four-paid-high-reuse-receipt.json")
  rec["parameters"]["inheritedCompleteHighKernel"]={j:v for j,v in hr.items() if j not in ["outputs","parameters"]}
  rec["parameters"]["inheritedHighOutputs"]=hr.get("outputs",[])
  ir=local_stage("new-images","--images-worker",images,"normal-four-new-images-receipt.json",high,high)
  need(ir["highKernelDimension"]==ir["additionalUnitRightHandSides"]==130,"all130 new images")
  rec["parameters"]["actualAdditionalImages"]={j:v for j,v in ir.items() if j not in ["outputs","parameters","batchInputs"]}
  rec["parameters"]["additionalImagesOutputs"]=ir.get("outputs",[])
  rec["parameters"]["actualBatchInputs"]=ir["batchInputs"];ck()
  combined=completed(unit/"m0-unit-solve-receipt.json",bind)
  if combined:
   rec["events"].append({"phase":"additional-unit","reusedAll130CompleteExactColumns":True})
  else:
   for lo in range(0,ACTUAL_K,UNIT_BATCH):
    hi=min(ACTUAL_K,lo+UNIT_BATCH);bd=unit/("batch-%03d-%03d"%(lo,hi-1))
    bp=images/("additional-unit-input-%03d-%03d.json.gz"%(lo,hi-1));rp=bd/"m0-unit-solve-receipt.json"
    r=read(rp) if rp.exists() else None
    if r and r.get("status")=="completed":
     need(r["binding"]==bind and r["inputIdentity"]==identity(bp) and
     r["workerSHA256"]==wid["sha256"] and r["all1546OriginalUnitRowsVerified"] and
     r["originalUnitProductCoordinates"]==1546*(hi-lo) and r["verifiedColumnCount"]==hi-lo and
     r["candidateIdentity"]==identity(bd/"complete-m0-unit-solution.json.gz"),"same completed actual RHS batch")
     rec["events"].append({"phase":"additional-unit","first":lo,"stop":hi,"reusedCompleteExactBatch":True})
    else:
     r=run("additional-unit-%03d-%03d"%(lo,hi-1),
     [sys.executable,"-B",str(a.unit_worker.resolve()),"--input",str(bp),"--out",str(bd)],rp)
    rec["parameters"]["completedAdditionalUnitColumns"]=hi;ck()
   combined=local_stage("additional-unit-assembly","--assemble-worker",unit,"m0-unit-solve-receipt.json",images)
  need(combined["all1546OriginalUnitRowsVerified"] and combined["originalUnitProductCoordinates"]==1546*130,
  "complete actual130 unit identity inherited from all batches")
  rec["parameters"]["additionalUnitSolve"]={j:v for j,v in combined.items() if j not in ["outputs","parameters"]}
  rec["parameters"]["completeAdditionalUnitSolution"]=combined["candidateIdentity"];ck()
  fr=local_stage("full-products","--finish-worker",finish,"normal-four-full-products-receipt.json",high,high,images,unit)
  rec["parameters"]["fullProductTemporaryOutputs"]=fr.get("outputs",[])
  rec["parameters"]["actualFullProductReceipt"]=identity(finish/"normal-four-full-products-receipt.json")
  for j,v in fr.items():
   if j not in ["outputs","parameters","binding","phase","elapsedSeconds"]:rec[j]=v
  rec["phase"]="complete";code=0
 except BudgetExpired as e:
  rec.update(status="checkpointed-time-budget",outcome="checkpointed-time-budget",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed-or-incomplete",outcome="failed-or-incomplete",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8");code=1
 finally:
  stages=[("paid-high","normal-four-paid-high-reuse-receipt.json"),
  ("new-images","normal-four-new-images-receipt.json"),("additional-unit","m0-unit-solve-receipt.json"),
  ("full-products","normal-four-full-products-receipt.json")]
  for folder,name in stages:
   rp=out/folder/name
   if rp.exists():
    v=read(rp);rec["parameters"][folder+"LastActualStatus"]={j:w for j,w in v.items() if j not in ["outputs","parameters","paths"]}
  batch_status=[]
  for lo in range(0,ACTUAL_K,UNIT_BATCH):
   hi=min(ACTUAL_K,lo+UNIT_BATCH);rp=out/"additional-unit"/("batch-%03d-%03d"%(lo,hi-1))/"m0-unit-solve-receipt.json"
   if rp.exists():
    v=read(rp);batch_status.append({"first":lo,"stop":hi,**{j:v[j] for j in
    ["status","phase","verifiedColumnCount","lastVerifiedColumn","originalUnitProductCoordinates","candidateIdentity","elapsedSeconds"] if j in v}})
  rec["parameters"]["actualAdditionalUnitBatchStatuses"]=batch_status
  rec["parameters"]["temporaryStageDirectories"]=[x for x,y in stages];ck()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--reuse-high-worker":sys.exit(reuse_high_worker(sys.argv[2],sys.argv[3]))
 if len(sys.argv)>1 and sys.argv[1]=="--images-worker":sys.exit(images_worker(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))
 if len(sys.argv)>1 and sys.argv[1]=="--assemble-worker":sys.exit(assemble_worker(sys.argv[2],sys.argv[3],sys.argv[4]))
 if len(sys.argv)>1 and sys.argv[1]=="--finish-worker":sys.exit(finish_worker(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7]))
 sys.exit(main(sys.argv[1:]))

