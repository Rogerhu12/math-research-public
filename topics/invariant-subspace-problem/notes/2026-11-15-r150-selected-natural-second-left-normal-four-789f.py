#!/usr/bin/env python3
"""R150 same-selected second left jets: add true normal-four corrections.
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
PINS={
 "old_unit":(9008513,"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"),
 "old_solution":(18124389,"9c3b02d2674af645ffcfd5297cf5c9ac287fe314d0c40f49c8bb99be9396352d"),
 "old_full":(12690,"b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70"),
 "old_main":(20323,"2343123363d6c38a871c66770afb67b37a1b3a6b882baa7aed040134914a345b"),
 "old_rref":(17625,"de7bb03e76ca2dee0221d4f89e1de5db190b6c5b64fc4df70a67e13f405a7941"),
 "coefficients":(20580,"7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1"),
 "profile":(21066,"044b28d717749d23a2959a02c0f8ed7570bfa19bcdff04207056f2a66d2e413d")}
WORKER=(16409,"28928f4298d0689f72ea8d39e530d474c4d15076af1c26aee612a2cb1413982e")
MAX_HIGH_FREE=64
def input_paths(a):
 o=a.regauged_out
 return {"old_unit":o/"prepared"/"second-left-m0-unit-input.json.gz",
 "old_solution":o/"unit-solve"/"complete-m0-unit-solution.json.gz",
 "old_full":o/"full-products"/"second-left-full-products-receipt.json",
 "old_main":o/"selected-natural-second-left-regauged-pipeline-receipt.json",
 "old_rref":o/"full-products"/"complete-small-second-residual-rref.json.gz",
 "coefficients":a.rebuild_root/"rebuilt-first"/"same-original-natural-constant-and-first-coefficients.json.gz",
 "profile":a.rebuild_root/"rebuilt-inputs"/"same-selected-original-output-indices.json"}
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
def profile_worker(invpath,out):
 from flint import nmod_mat
 inv=load_inv(invpath);bind=inv["binding"];out=pathlib.Path(out)
 cp=out/"normal-four-profile-receipt.json";c=completed(cp,bind)
 if c:print(json.dumps({"status":"completed","reused":True,"outcome":c["outcome"]}),flush=True);return 0
 cp,rec,ck=stage_rec(out,cp.name,bind,"actual-original-normal-four-block")
 unit=read(inv["paths"]["old_unit"]);main=read(inv["paths"]["old_main"]);fr=read(inv["paths"]["old_full"])
 need(unit["binding"]==fr["binding"]==main["parameters"]["binding"]==PAID_BINDING and
 main["status"]==fr["status"]=="completed" and fr["secondHeadImageDimension"]==22 and
 fr["all4354OriginalSecondLeftProductsZero"] and fr["smallResidualRank"]==14,"actual paid22 original heads")
 J=list(map(int,unit["originalSourceRows"]));I=set(map(int,read(inv["paths"]["profile"])["originalOutputI"]))
 need(len(J)==len(set(J))==len(I)==4354,"same whole original I,J")
 oldrows=unit["originalCorrectionRows"];rhs=unit["originalRightHandSideRows"];high=list(map(int,unit["oldZeroRowPositions"]))
 need(len(high)==len(set(high))==1736 and all(not oldrows[i] and not any(map(int,rhs[i])) for i in high),"all1736 old-zero rows and all36 right sides zero exactly")
 whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
 wi={q:i for i,q in enumerate(whole)};nd=[sum(j<=8 for j in q) for q in whole]
 E4=[i for i,d in enumerate(nd) if d==4 and i in I];need(len(E4)==1485,"all original normal-four coordinates in same I")
 e4={v:i for i,v in enumerate(E4)};Eold=list(map(int,unit["secondCorrectionOutputCoordinates"]))
 need(len(Eold)==1546 and not(set(Eold)&set(E4)),"old and additional coordinates disjoint")
 co=read(inv["paths"]["coefficients"]);F0=[list(map(int,r)) for r in co["constant"]]
 need(len(F0)==17 and all(len(r)==77 for r in F0),"complete actual original constant coefficients")
 mon=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
 mult=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
 rows=[]
 for raw in J:
  e=(raw-1)%17;mu=mult[(raw-1)//17];row={}
  for k,q in enumerate(mon):
   v=F0[e][k]
   if not v:continue
   ix=wi[tuple(sorted(mu+q))]
   if ix in e4:row[e4[ix]]=row.get(e4[ix],0)+v
  rows.append(sorted((j,v) for j,v in row.items() if v))
 bp=out/"complete-original-normal-four-block.json.gz"
 block={"binding":bind,"paidSecondBinding":PAID_BINDING,"originalSourceRows":J,
  "normalFourOutputCoordinates":E4,"oldSecondCorrectionOutputCoordinates":Eold,
  "highOriginalRowPositions":high,"all1736OldCorrectionAndForcingRowsZero":True,
  "originalNormalFourRows":[[[j,str(v)] for j,v in r] for r in rows]}
 save(bp,block);rec["outputs"]=[{"file":bp.name,**identity(bp)}];rec["phase"]="actual-high-field-unit-profile";ck()
 hrows=[rows[i] for i in high]
 hdict=[dict(r) for r in hrows]
 H=nmod_mat(1736,1485,[r.get(j,0)%31 for r in hdict for j in range(1485)],31)
 R,rank=H.rref();rank=int(rank);pc=pivots(R,rank);free=[j for j in range(1485) if j not in set(pc)]
 prof={"binding":bind,"blockIdentity":identity(bp),"prime":31,"highRows":1736,"highColumns":1485,
 "rankModulo31":rank,"pivotColumns":pc,"freeColumns":free,"all1736RowsRetained":True,
 "finiteFieldKernelNotAcceptedAsRationalKernel":True}
 del H,R
 if rank:
  T=nmod_mat(rank,1736,[r.get(j,0)%31 for j in pc for r in hdict],31)
  R,rr=T.rref();need(int(rr)==rank,"actual independent high column basis");pr=pivots(R,rank);del T,R
  ds=[dict(hrows[i]) for i in pr]
  U31=nmod_mat(rank,rank,[r.get(j,0)%31 for r in ds for j in pc],31);det=int(U31.det())%31;del U31
  need(det!=0,"actual original high unit minor")
 else:pr=[];det=1
 prof["selectedHighRowIndices"]=pr;prof["unitDeterminantModulo31"]=det
 pp=out/"complete-normal-four-high-unit-profile.json.gz";save(pp,prof)
 rec["outputs"].append({"file":pp.name,**identity(pp)})
 rec.update(status="completed",phase="complete",rankHighModulo31=rank,highFreeColumnCount=len(free),
 all1736OldCorrectionAndForcingRowsZero=True,all4354OriginalNormalFourRowsConstructed=True,
 actualHighUnitDeterminantModulo31=det,highRationalKernelComputed=False,
 outcome="ready-for-exact-high-kernel" if len(free)<=MAX_HIGH_FREE else "high-nullity-above-bounded-entry",
 boundedHighFreeColumnLimit=MAX_HIGH_FREE)
 ck();print(json.dumps({k:v for k,v in rec.items() if k!="outputs"}),flush=True);return 0
def high_worker(invpath,out,profiledir):
 from flint import fmpq,fmpq_mat
 inv=load_inv(invpath);bind=inv["binding"];out=pathlib.Path(out);profiledir=pathlib.Path(profiledir)
 cp=out/"normal-four-exact-high-kernel-receipt.json";cc=completed(cp,bind)
 if cc:print(json.dumps({"status":"completed","reused":True}),flush=True);return 0
 cp,rec,ck=stage_rec(out,cp.name,bind,"complete-original-high-unit")
 bp=profiledir/"complete-original-normal-four-block.json.gz";pp=profiledir/"complete-normal-four-high-unit-profile.json.gz"
 b=read(bp);p=read(pp);need(b["binding"]==p["binding"]==bind and p["blockIdentity"]==identity(bp),"same complete high inputs")
 high=list(map(int,b["highOriginalRowPositions"]));rows=[[(int(j),int(v)) for j,v in r] for r in b["originalNormalFourRows"]]
 hr=[rows[i] for i in high];rank=int(p["rankModulo31"]);pc=list(map(int,p["pivotColumns"]));fc=list(map(int,p["freeColumns"]));pr=list(map(int,p["selectedHighRowIndices"]));nf=len(fc)
 need(rank+nf==1485 and len(pc)==len(pr)==rank and nf<=MAX_HIGH_FREE,"bounded complete high profile")
 candp=out/"complete-high-unit-rational-candidate.json.gz"
 if candp.exists():
  cand=read(candp);need(cand["binding"]==bind and cand["profileIdentity"]==identity(pp) and cand["blockIdentity"]==identity(bp),"same high returned solution")
  D=list(map(int,cand["denominators"]));N=[[int(v) for v in r] for r in cand["dependentNumeratorColumns"]]
 else:
  rec["phase"]="exact-high-unit-dixon";ck()
  if nf:
   drows=[dict(hr[i]) for i in pr];gs=[]
   for r in drows:
    g=0
    for v in r.values():g=math.gcd(g,abs(v))
    need(g>0 and g%31,"actual selected high row content is a31 unit");gs.append(g)
   U=fmpq_mat(rank,rank,[fmpq(r.get(j,0),g) for r,g in zip(drows,gs) for j in pc])
   RHS=fmpq_mat(rank,nf,[fmpq(-r.get(j,0),g) for r,g in zip(drows,gs) for j in fc])
   X=U.solve(RHS,algorithm="dixon");D=[];N=[]
   for j in range(nf):
    d=1
    for i in range(rank):d=math.lcm(d,int(X[i,j].q))
    D.append(d);N.append([int(X[i,j].p)*(d//int(X[i,j].q)) for i in range(rank)])
   del U,RHS,X,drows
  else:D=[];N=[]
  cand={"binding":bind,"profileIdentity":identity(pp),"blockIdentity":identity(bp),
  "dependentColumns":pc,"freeColumns":fc,"denominators":[str(d) for d in D],
  "dependentNumeratorColumns":[[str(v) for v in r] for r in N],
  "candidateOnlyUntilCompleteOriginalHighProducts":True}
  save(candp,cand)
 need(len(D)==len(N)==nf and all(d>0 for d in D) and all(len(c)==rank for c in N),"complete high rational columns")
 rec["phase"]="complete-high-Schur-and-products";rec["outputs"]=[{"file":candp.name,**identity(candp)}];ck()
 V=[]
 for c in range(nf):
  v=[0]*1485;v[fc[c]]=D[c]
  for i,j in enumerate(pc):v[j]=N[c][i]
  V.append(v)
 SR=[[sum(a*V[c][j] for j,a in row) for c in range(nf)] for row in hr]
 need(all(not any(SR[i]) for i in pr),"all original selected high unit equations exactly zero")
 nz=[i for i,r in enumerate(SR) if any(r)]
 if nf:
  Sm=fmpq_mat(len(nz),nf,[v for i in nz for v in SR[i]])
  RR,rs=Sm.rref();rs=int(rs);sp=pivots(RR,rs);sf=[j for j in range(nf) if j not in set(sp)]
 else:RR=None;rs=0;sp=[];sf=[]
 K=[];free_images=[]
 for f in sf:
  z=[fmpq(0) for _ in range(nf)];z[f]=fmpq(1)
  for i,j in enumerate(sp):z[j]=-RR[i,f]
  gam=primitive_q(z);v=[sum(V[c][j]*gam[c] for c in range(nf)) for j in range(1485)]
  g=0
  for w in v:g=math.gcd(g,abs(w))
  need(g>0,"nonzero full high kernel")
  v=[w//g for w in v]
  if next(w for w in v if w)<0:v=[-w for w in v]
  for i,row in enumerate(hr):need(sum(a*v[j] for j,a in row)==0,"all original high rows of trueQ kernel "+str(high[i]))
  K.append(v);free_images.append([v[j] for j in fc])
 k=len(K);need(k==nf-rs and rank+rs==1485-k,"complete high Schur dimension")
 if k:
  need(int(fmpq_mat(nf,k,[free_images[c][i] for i in range(nf) for c in range(k)]).rank())==k,"independent full free-coordinate kernel images")
 kp=out/"complete-original-normal-four-high-kernel.json.gz"
 kd={"binding":bind,"profileIdentity":identity(pp),"blockIdentity":identity(bp),
 "returnedCandidateIdentity":identity(candp),"rankModulo31":rank,"extraRationalSchurRank":rs,
 "rankOverQ":rank+rs,"kernelDimension":k,"originalNormalFourOutputCoordinates":b["normalFourOutputCoordinates"],
 "primitiveIntegerKernelColumns":[[str(v) for v in c] for c in K],
 "freeCoordinateImages":[[str(v) for v in c] for c in free_images],
 "all1736OriginalHighProductsZero":True,"originalProductCoordinates":1736*k,
 "completeRationalKernelProved":True}
 save(kp,kd)
 rec["outputs"].append({"file":kp.name,**identity(kp)})
 rec.update(status="completed",phase="complete",outcome="complete-rational-high-kernel",
 rankHighModulo31=rank,rankHighOverQ=rank+rs,highKernelDimension=k,
 extraRationalSchurRank=rs,completeRationalHighKernelProved=True,
 all1736OriginalHighProductsZero=True,originalHighProductCoordinates=1736*k,
 completeCandidateSavedBeforeFullProducts=True)
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
 need(k==kdata["kernelDimension"] and k<=64 and all(len(c)==1485 for c in K),"all actual high kernel columns")
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
 rec.update(status="completed",phase="complete",outcome="ready-for-actual-additional-unit-solve" if k else "normal-four-high-kernel-zero",
 highKernelDimension=k,additionalUnitRightHandSides=k,old36ExactUnitSolutionsReused=True,
 old36RightHandSidesRecomputed=False,all4354OriginalNewImagesConstructed=True,all1736HighRowsZero=True)
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
 need(1<=k<=64 and len(W)==4354 and all(len(r)==k for r in W),"only actual nonzero high kernel here")
 up=imagesdir/"additional-left-m0-unit-input.json.gz";sp=unitdir/"complete-m0-unit-solution.json.gz";ur=read(unitdir/"m0-unit-solve-receipt.json");sol=read(sp)
 need(sol["binding"]==ur["binding"]==bind and sol["inputIdentity"]==identity(up) and
 ur["status"]=="completed" and ur["all1546OriginalUnitRowsVerified"] and
 ur["candidateIdentity"]==identity(sp) and ur["originalUnitProductCoordinates"]==1546*k,"all new complete actual unit products")
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
   r=read(p);need(r["binding"]==bind and r["column"]==c and r["unitInputIdentity"]==identity(up) and
   r["unitSolutionIdentity"]==identity(sp),"same completed new residual")
   v=list(map(int,r["values"]));need(len(v)==4354 and r["all1546UnitResidualEntriesZero"],"complete new residual")
  else:
   v=[DN[c]*W[i][c]+sum(a*NN[c][j] for j,a in row) for i,row in enumerate(rows)]
   need(all(v[i]==0 for i in old["selectedUnitRowIndices"]),"all actual new unit residuals zero")
   r={"binding":bind,"column":c,"unitInputIdentity":identity(up),"unitSolutionIdentity":identity(sp),
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
 need(rank>=14 and pp[:3]==[0,1,2],"paid old residual rank14 and three first-failure axes retained")
 free=[j for j in range(nr) if j not in set(pp)];dim=len(free)
 need(22<=dim<=24,"complete old22 and paid full second lower9")
 GS=[];CS=[]
 for f in free:
  z=[fmpq(0) for _ in range(nr)];z[f]=fmpq(1)
  for row,j in zip(rrows,pp):z[j]=-row.get(f,fmpq(0))
  gam=primitive_q(z);GS.append(gam);CS.append([D[3+j]*gam[3+j] for j in range(33)])
 crank=int(fmpq_mat(33,dim,[CS[c][j] for j in range(33) for c in range(dim)]).rank())
 need(crank==dim,"actual original second-head projection independent; no zero-head directions counted")
 rec.update(phase="all-original-normal-four-second-jets",oldResidualRank=14,extendedSmallResidualRank=rank,
 actualHeadProjectionRank=crank,secondHeadImageDimension=dim,newIndependentHeads=dim-22,
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
   "oldUnitSolutionIdentity":inv["inputIdentities"]["old_solution"],"additionalUnitSolutionIdentity":identity(sp),
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
 for key in ["regauged-out","rebuild-root","unit-worker","out"]:ap.add_argument("--"+key,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=300);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=600 and 0<a.memory_mib<=4096,"explicit bounded continuous normal-four entry")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds;reserve=min(5,a.seconds/20)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-selected-natural-second-left-normal-four-v1","status":"running","phase":"paid-actual-inputs",
 "oldFirstRREFRecomputed":False,"old36ExactUnitSolutionsRecomputed":False,"old36RightHandSidesRecomputed":False,
 "oldLargeNormalFormsRecomputed":False,"newOriginalRankPrimeComputed":False,"leadingUnitProved":False,
 "largeDataUploadedOrCommitted":False,"parameters":{},"events":[]};code=1
 def remain():
  r=deadline-time.monotonic()-reserve
  if r<=0:raise BudgetExpired("shared continuous normal-four mathematical clock")
  return r
 def ck():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start;save(out/"selected-natural-second-left-normal-four-receipt.json",rec)
 def run(name,cmd,rp):
  rec["phase"]=name;ck();t=time.monotonic()
  available=remain()
  with (out/(name+".log")).open("a",encoding="utf-8") as log:
   proc=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
   grace=min(20.0,max(.5,available/8)) if name in ["high-kernel","additional-unit"] else .25
   try:proc.wait(timeout=max(.1,available-grace))
   except subprocess.TimeoutExpired:
    os.killpg(proc.pid,signal.SIGTERM)
    try:proc.wait(timeout=grace)
    except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
    rec["events"].append({"phase":name,"exitCode":proc.returncode,"deadlineStoppedWorker":True,"elapsedSeconds":time.monotonic()-t})
    raise BudgetExpired(name+" incomplete; all returned complete candidates remain temporary")
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
  wid=identity(a.unit_worker);need(wid=={"bytes":WORKER[0],"sha256":WORKER[1]},"frozen actual-k unit worker")
  material={"programIdentity":identity(__file__),"unitWorkerIdentity":wid,"inputIdentities":ids,
  "previousCompleteSecondBinding":PAID_BINDING,"normalFourCoordinates":1485,
  "allOriginalHighRows":1736,"allOriginalSourceRows":4354,"fixedProfilePrime":31,"maximumHighProfileFreeColumns":MAX_HIGH_FREE}
  bind=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  inv={**material,"binding":bind,"paths":{k:str(v.resolve()) for k,v in paths.items()}}
  ip=out/"invocation.json";save(ip,inv)
  rec["parameters"].update(material);rec["parameters"].update(binding=bind,secondsLimit=a.seconds,memoryMiBPerProcess=a.memory_mib)
  ck()
  profile=out/"high-profile";high=out/"high-kernel";images=out/"new-images";unit=out/"additional-unit";finish=out/"full-products"
  pr=local_stage("high-profile","--profile-worker",profile,"normal-four-profile-receipt.json")
  rec["parameters"]["highProfile"]={k:v for k,v in pr.items() if k not in ["outputs","parameters"]}
  rec["parameters"]["highProfileOutputs"]=pr.get("outputs",[])
  if pr["outcome"]=="high-nullity-above-bounded-entry":
   rec.update(status="completed-prefix",phase="complete-prefix",outcome="high-nullity-above-bounded-entry",
   completeFixedSupportSecondEnvelopeComputed=False,completeSelectedSecondHeadSpaceProved=False,
   highRationalKernelComputed=False,selectedSecondConnectionRankExactly9=False);code=75
  else:
   hr=local_stage("high-kernel","--high-worker",high,"normal-four-exact-high-kernel-receipt.json",profile)
   rec["parameters"]["completeHighKernel"]={k:v for k,v in hr.items() if k not in ["outputs","parameters"]}
   rec["parameters"]["completeHighKernelOutputs"]=hr.get("outputs",[])
   ir=local_stage("new-images","--images-worker",images,"normal-four-new-images-receipt.json",profile,high)
   rec["parameters"]["actualAdditionalImages"]={k:v for k,v in ir.items() if k not in ["outputs","parameters"]}
   rec["parameters"]["additionalImagesOutputs"]=ir.get("outputs",[])
   k=int(ir["highKernelDimension"]);need(k==hr["highKernelDimension"],"same actual complete high kernel count")
   if k==0:
    old=read(paths["old_full"])
    rec.update(status="completed",phase="complete",outcome="restricted-second-left-support-only",
    secondHeadImageDimension=22,newIndependentHeads=0,selectedSecondConnectionRankOverQLowerBound=9,
    selectedSecondConnectionRankOverQUpperBound=11,selectedSecondConnectionRankExactly9=False,
    completeSelectedSecondHeadSpaceProved=False,completeFixedSupportSecondEnvelopeComputed=True,
    correctionNormalDegreeAtMost=4,completeRationalHighKernelDimension=0,
    all4354OriginalSecondLeftProductsZero=True,originalSecondProductsInheritedFromPaid22=True,
    oldActualProductCoordinates=old["fullOriginalSecondJetProductCoordinates"],
    oldActualProductsRecomputed=False,allHeadProjectionFreeCoordinatesIndependent=True,
    higherCorrectionSupportExcludedAsPremise=False,sourceSupportExpansionNeeded=True,
    oldFirstKernelFreedomDimension=33,lastCorrectionKernelFreedomDimension=36,
    oldAndNewCorrectionEmbeddingsKeptDistinct=True);code=0
   else:
    up=images/"additional-left-m0-unit-input.json.gz";urp=unit/"m0-unit-solve-receipt.json"
    ur=read(urp) if urp.exists() else None
    if ur and ur.get("status")=="completed":
     need(ur["binding"]==bind and ur["inputIdentity"]==identity(up) and
     ur["all1546OriginalUnitRowsVerified"] and ur["originalUnitProductCoordinates"]==1546*k and
     ur["candidateIdentity"]==identity(unit/"complete-m0-unit-solution.json.gz"),"same completed actual-k unit solve")
     rec["events"].append({"phase":"additional-unit","reusedCompleteExactSolution":True})
    else:
     ur=run("additional-unit",[sys.executable,"-B",str(a.unit_worker.resolve()),"--input",str(up),"--out",str(unit)],urp)
    rec["parameters"]["additionalUnitSolve"]={j:v for j,v in ur.items() if j not in ["parameters"]}
    fr=local_stage("full-products","--finish-worker",finish,"normal-four-full-products-receipt.json",profile,high,images,unit)
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
  stages=[("high-profile","normal-four-profile-receipt.json"),("high-kernel","normal-four-exact-high-kernel-receipt.json"),
  ("new-images","normal-four-new-images-receipt.json"),("additional-unit","m0-unit-solve-receipt.json"),("full-products","normal-four-full-products-receipt.json")]
  for folder,name in stages:
   rp=out/folder/name
   if rp.exists():
    v=read(rp);rec["parameters"][folder+"LastActualStatus"]={j:w for j,w in v.items() if j not in ["outputs","parameters","paths"]}
  rec["parameters"]["temporaryStageDirectories"]=[x for x,y in stages];ck()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":
 if len(sys.argv)>1 and sys.argv[1]=="--profile-worker":sys.exit(profile_worker(sys.argv[2],sys.argv[3]))
 if len(sys.argv)>1 and sys.argv[1]=="--high-worker":sys.exit(high_worker(sys.argv[2],sys.argv[3],sys.argv[4]))
 if len(sys.argv)>1 and sys.argv[1]=="--images-worker":sys.exit(images_worker(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))
 if len(sys.argv)>1 and sys.argv[1]=="--finish-worker":sys.exit(finish_worker(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7]))
 sys.exit(main(sys.argv[1:]))
