#!/usr/bin/env python3
"""Complete missing natural third heads through one original constant4318 unit.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Eighteen RHS: fourteen paid rational quotient columns and four missing heads.
Complete the two missing second and four missing third cochains, then pair
all21 fourth forcings modulo all24 third incoming columns. No906-column solve.
"""
import argparse,gzip,hashlib,io,itertools,json,math,os,pathlib,resource,shlex,signal,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
CPP_SHA="d592f2086e81be2206adb67c7553de15ce36d49a9d1e62721a47a469d8afece2"
PREPARER_SHA="6bfab671f390be5f40c30e3d2260bb873ac7c8a37302d2a4902228e6521089b7"
BRIDGE_SHA="8e2b059af823dd8fc089470f5d20c930649ae1fd8e4ae695626ba6b88048d2a7"
PREFIX_BINDING="8a66f5f182b224bcdf158b3cbd739f23692f333c9c338e7056ca8c5162018ebf"
OLD="c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e"
PREP="3ac423ccd312ea0fa7084f70b9a2fb788a26822a62e9918998f17d6762fc371a"
CONSUMER="68b83b621a2219162ca36499757ab327cac7431f669e2fcc83e1de232affef50"
PAIR="ea772f01fa0ab8a761287893c15a94f83ebc6326703b40b82a5846e02b020e39"
SOURCE="2d9b068281400ec635fc2c912edf29e59d2bec1e3686bf6c3f6abd6ac01890f2"
THIRD="7aa59b81b9364f4e3a214b9f809af030000a524fbe7cf94b3bdf4606e9867a1f"
FOURTH="da459937e6c591f59ab0e803903412a8b57154511756c513080b8a3eeab5eaf6"
PINS={
 "prefix":(3375,"23035e646b1d3598fae8c42e2c34195f910962213a846289fca656ad9f1b7742"),
 "old_unit":(9008513,"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"),
 "old_full":(12690,"b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70"),
 "heads":(633788,"3107ab8547071205466ff5b5aa2ef5f0e3ea81a976258a25184c9a0d7e709fe2"),
 "first_jets":(1701626,"2aabfc92860f66942e7a8eb3d9254ab911e7b8b2f255d40bfaa1235ed4d482fe"),
 "prepared_rhs":(4617848,"22d41ddbd72836d013f0855cf094f243ae5bc63a07f9006b9603031383794598"),
 "old17_products":(10890,"8a147b79e6f7a502aacc58fc07605c6754addf5d550295e838929955f5d1055f"),
 "through4":(49917,"c56c548375c779327ea908f2513c5cc8ed8e6635fce729f089fdf02bc9feb19f"),
 "old75":(217868,"7152e00502d422002750641047c0c0db9131d35bee2603dbc3f41cee0fe7c660"),
 "old58":(152226,"912a777573f261446f87fda25b71fe889963f31cb5a7f34dc192b42045a1af47"),
 "source_receipt":(15304,"11b0f10e9c0750b73644c425f91b48a249e5829a8dc7960e68e7713ef545f289")}
class BudgetExpired(Exception):pass
class UnitComplete(Exception):pass
STOP=False
def sigstop(signum,frame):
 global STOP
 STOP=True
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
  b=json.dumps(v,sort_keys=True,separators=(",",":")).encode();need(len(b)<100000,"small permanent metadata only");q.write_bytes(b)
 os.replace(q,p);return {"file":p.name,**identity(p),"temporaryOnly":True}
def vecsha(v):
 h=hashlib.sha256()
 for x in v:h.update((str(x)+"\n").encode())
 return h.hexdigest()
def primitive(v):
 den=1
 for x in v:den=math.lcm(den,int(x.q))
 z=[int(x.p)*(den//int(x.q)) for x in v];g=0
 for x in z:g=math.gcd(g,abs(x))
 need(g>0,"nonzero rational vector")
 sg=-1 if next(x for x in z if x)<0 else 1
 return [sg*(x//g) for x in z]
def integer_column(v):
 den=1
 for x in v:den=math.lcm(den,int(x.q))
 return den,[int(x.p)*(den//int(x.q)) for x in v]
def pivots(M,rank):
 ans=[]
 for i in range(int(rank)):
  j=next((j for j in range(M.ncols()) if M[i,j]),None)
  need(j is not None and M[i,j]==1,"normalized exact RREF");ans.append(j)
 need(ans==sorted(set(ans)),"strict exact pivot order");return ans
def ident_only(v):return {"bytes":v["bytes"],"sha256":v["sha256"]}
class BinWriter:
 def __init__(self,p):
  self.p=pathlib.Path(p);self.tmp=self.p.with_name(self.p.name+".tmp")
  self.f=self.tmp.open("wb");self.sha=hashlib.sha256();self.n=0
 def raw(self,b):self.f.write(b);self.sha.update(b);self.n+=len(b)
 def u(self,v):self.raw(struct.pack("<I",int(v)))
 def z(self,v):
  v=int(v);b=abs(v).to_bytes((abs(v).bit_length()+7)//8,"big")
  self.raw(struct.pack("<i",-len(b) if v<0 else len(b)));self.raw(b)
 def close(self):
  self.f.flush();os.fsync(self.f.fileno());self.f.close();os.replace(self.tmp,self.p)
  return {"file":self.p.name,"bytes":self.n,"sha256":self.sha.hexdigest(),"temporaryOnly":True}
class BinReader:
 def __init__(self,p):self.f=pathlib.Path(p).open("rb")
 def raw(self,n):
  b=self.f.read(n);need(len(b)==n,"complete actual native solution");return b
 def u(self):return struct.unpack("<I",self.raw(4))[0]
 def z(self):
  n=struct.unpack("<i",self.raw(4))[0];need(abs(n)<100000000,"bounded native integer")
  v=int.from_bytes(self.raw(abs(n)),"big");return -v if n<0 else v
 def close(self):need(self.f.read(1)==b"","complete native solution EOF");self.f.close()
def child(cmd,log,seconds,grace):
 st=time.monotonic()
 with pathlib.Path(log).open("a",encoding="utf-8") as f:
  p=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
  try:p.wait(timeout=max(.01,seconds));timed=False
  except subprocess.TimeoutExpired:
   timed=True;os.killpg(p.pid,signal.SIGTERM)
   try:p.wait(timeout=grace)
   except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
 return {"exitCode":p.returncode,"elapsedSeconds":time.monotonic()-st,"outerDeadlineReached":timed}
class Context:
 def __init__(self,a,rec,out):
  self.a=a;self.rec=rec;self.out=out;self.start=time.monotonic();self.deadline=self.start+a.seconds-min(4,a.seconds/30)
  self.binding=None;self.paths={};self.ids={}
 def check(self):
  if STOP or time.monotonic()>=self.deadline:raise BudgetExpired("shared exact original continuation deadline")
 def save(self):
  self.rec["mathematicalElapsedSeconds"]=time.monotonic()-self.start
  save(self.out/"missing-third-constant-unit-pipeline-receipt.json",self.rec)
 def phase(self,s):
  self.rec["phase"]=s;self.save();self.check()
 def stage(self,name):
  p=self.out/name;p.mkdir(exist_ok=True);return p
 def done(self,p):
  if not p.exists():return None
  r=read(p);need(r["binding"]==self.binding,"same complete stage binding")
  if r.get("status")!="completed":return None
  for z in r.get("outputs",[]):need(identity(p.parent/z["file"])==ident_only(z),"all actual complete stage output bytes")
  return r
 def finish(self,p,r,outputs):
  r.update(status="completed",binding=self.binding,outputs=[{"file":q.name,**identity(q),"temporaryOnly":True} for q in outputs])
  save(p,r);self.rec["parameters"][p.parent.name+"Receipt"]={"file":str(p.relative_to(self.out)),**identity(p)}
  self.save();return r
def original_rows(J,coeff):
 whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
 wi={q:i for i,q in enumerate(whole)}
 mon=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
 mus=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
 Fs=[[list(map(int,r)) for r in coeff[k]] for k in ("constant","naturalFirst","naturalSecond","naturalThird","naturalFourth")]
 need(len(whole)==4367 and all(len(F)==17 and all(len(r)==77 for r in F) for F in Fs),"all original natural F0..F4")
 rows=[]
 for raw in J:
  e=(raw-1)%17;mu=mus[(raw-1)//17];rr=[]
  for j,m in enumerate(mon):
   fs=[F[e][j] for F in Fs]
   if any(fs):rr.append((wi[tuple(sorted(mu+m))],*fs))
  rows.append(rr)
 return rows
def prepare_native(ctx,data,model):
 out=ctx.stage("native-input");mp=out/"constant-unit-native-input-receipt.json"
 done=ctx.done(mp)
 if done:return out/"actual-constant-unit-eighteen.bin",done
 ctx.phase("serialize-original-constant-unit-and18-rhs")
 n=int(data["unitSize"]);m=int(data["targets"])
 need((n,m)==(4318,18) and data["rightHandSideSignForNative"]==-1,"actual original eighteen-RHS shape and sign")
 rows=data["scaledSparseUnitRows"];g=list(map(int,data["positiveRowContents"]));h=list(map(int,data["positiveColumnContents"]))
 E=list(map(int,data["originalCorrectionOutputCoordinates"]));rr=list(map(int,data["sourceUnitRowPositions"]))
 raw=list(map(int,data["originalSourceUnitRows"]));W=[[int(v) for v in c] for c in data["wholeOriginalRightHandSideColumns"]]
 need(len(rows)==len(g)==len(h)==len(E)==len(rr)==len(raw)==n and len(W)==m and all(len(v)==4354 for v in W),
  "all original unit, scales, and full right-side arrays")
 need(all(v>0 for v in g+h) and all(g[i]%31 and h[i]%31 for i in range(n)),"same positive31-unit row and column contents")
 original=[dict((int(j),int(v)) for j,v in row) for row in model["originalSparseRows"]]
 nz=sum(len(r) for r in rows);bp=out/"actual-constant-unit-eighteen.bin";w=BinWriter(bp)
 w.raw(b"R15CUM01");w.u(1);w.u(n);w.u(m);w.u(nz);w.raw(ctx.binding.encode())
 for j in range(n):w.u(E[j]);w.z(h[j])
 for i in range(n):
  need(raw[i]==int(model["originalSourceRows"][rr[i]]),"same original unit row label")
  terms=[(int(j),int(v)) for j,v in rows[i]]
  need(terms==sorted(terms) and len({j for j,v in terms})==len(terms) and all(v for j,v in terms),"canonical actual unit terms")
  need({j:v*g[i]*h[j] for j,v in terms}==original[rr[i]],"all original constant coefficient scales exactly restored")
  w.u(raw[i]);w.z(g[i])
  for j in range(m):w.z(-W[j][rr[i]])
  w.u(len(terms))
  for j,v in terms:w.u(j);w.z(v)
  if i%128==127:ctx.check()
 q=w.close()
 r={"format":"isp-original-constant-unit-eighteen-native-input-v1","input":q,"unitSize":n,"targets":m,
  "allOriginalCoefficientScaleIdentitiesVerified":True,"originalSparseNonzeros":nz,
  "protocol":"R15CUM01/version1; diag(g)Aprime*Z=-W_I; x=diag(h)^(-1)Z"}
 return bp,ctx.finish(mp,r,[bp])
def native_solve(ctx,exe,bp,inputrec):
 out=ctx.stage("native");rp=out/"constant-unit-dixon-native-receipt.json";sol=out/"active-unit-rational-solution.bin"
 nr=read(rp) if rp.exists() else {}
 already=nr.get("status")=="completed" and nr.get("binding")==ctx.binding and nr.get("allOriginalUnitRowsVerified") and sol.exists()
 if already:
  need(identity(sol)=={"bytes":nr["parameters"]["solutionBytes"],"sha256":nr["parameters"]["solutionSHA256"]},"same complete actual native rational solution")
  ctx.rec["events"].append({"reusedCompleteNativeUnitSolution":True})
 else:
  ctx.phase("checkpointed-sparse-original-constant-unit")
  rem=ctx.deadline-time.monotonic()
  cr=child([str(exe),str(bp),str(out),ctx.binding,str(rem),str(ctx.a.maximum_digits)],ctx.out/"native-unit.log",rem,8)
  ctx.rec["events"].append({"nativeUnitRun":cr})
  nr=read(rp) if rp.exists() else {};ctx.rec["parameters"]["nativeStatistics"]=nr;ctx.save()
  need(nr.get("binding")==ctx.binding and nr.get("parameters",{}).get("inputSHA256")==inputrec["input"]["sha256"],
   "native actual whole input SHA and binding")
  if cr["exitCode"]!=0 or nr.get("status")!="completed":
   if cr["outerDeadlineReached"] or cr["exitCode"]==75 or nr.get("status")=="budget-exhausted":
    raise BudgetExpired("actual inverse and last complete digit retained; unit solve unfinished")
   raise ValueError("actual native unit solver failed")
 need(nr["phase"]=="constant-unit-multiple-rhs-rational-solution-complete" and nr["unitSolutionExactVerified"] and
  nr["allOriginalUnitRowsVerified"] and nr["originalUnitProductCoordinates"]==4318*18 and
  nr["verificationScope"]=="square-unit-only" and nr["targets"]==18 and nr["unitSize"]==4318,
  "all actual original unit rows, not only modular reconstruction")
 need(nr["parameters"]["inputSHA256"]==inputrec["input"]["sha256"] and
  identity(sol)=={"bytes":nr["parameters"]["solutionBytes"],"sha256":nr["parameters"]["solutionSHA256"]},
  "complete original native solution identity")
 ctx.rec["unitSolutionExactVerified"]=True;ctx.rec["parameters"]["nativeStatistics"]=nr;ctx.save()
 return sol
def full_residuals(ctx,data,model,solution):
 from flint import fmpq
 out=ctx.stage("whole-unit-residuals");rp=out/"complete-original-unit-residuals-receipt.json"
 done=ctx.done(rp)
 if done:return done
 ctx.phase("whole4354-original-unit-residuals")
 r=BinReader(solution);need(r.raw(8)==b"R15CUSL1" and r.raw(64).decode()==ctx.binding,"same native complete solution header")
 n,m,p,digits=[r.u() for _ in range(4)];need((n,m)==(4318,18),"actual full solution dimensions")
 dn=[r.z() for _ in range(m)];need(all(v>0 for v in dn),"all positive native denominators")
 numer=[[0]*n for _ in range(m)]
 for i in range(n):
  for j in range(m):numer[j][i]=r.z()
 r.close();solution_id=identity(solution)
 h=list(map(int,data["positiveColumnContents"]));W=[[int(v) for v in c] for c in data["wholeOriginalRightHandSideColumns"]]
 rows=[[(int(j),int(v)) for j,v in row] for row in model["originalSparseRows"]]
 unitrows=set(map(int,data["sourceUnitRowPositions"]));outputs=[];audit=[]
 for j in range(m):
  ctx.check();cp=out/("complete-original-unit-column-%02d.json.gz"%j)
  if cp.exists():
   x=read(cp);need(x["binding"]==ctx.binding and x["column"]==j and x["nativeSolutionIdentity"]==solution_id and
    x["all4318OriginalUnitResidualsZero"],"same actual retained normalized unit column")
  else:
   values=[fmpq(numer[j][i],dn[j]*h[i]) for i in range(n)]
   D,N=integer_column(values);del values
   v=[]
   for i,row in enumerate(rows):
    value=D*W[j][i]+sum(a*N[k] for k,a in row)
    if i in unitrows:need(value==0,"all original unit products after source-scale restoration")
    v.append(value)
    if i%128==127:ctx.check()
   x={"binding":ctx.binding,"column":j,"nativeSolutionIdentity":solution_id,
    "denominator":str(D),"original4318NumeratorColumn":[str(v) for v in N],
    "complete4354OriginalResidual":[str(value) for value in v],
    "rightHandSideSHA256":vecsha(W[j]),"all4318OriginalUnitResidualsZero":True,
    "wholeOriginalResidualRetained":True,"equation":"S=Mstar*N+D*W; no row-content scaling is discarded"}
   save(cp,x)
  outputs.append(cp);audit.append({"file":cp.name,**identity(cp),"denominatorBits":int(x["denominator"]).bit_length()})
  ctx.rec["parameters"]["completedWholeOriginalUnitResidualColumns"]=j+1;ctx.save()
 del numer
 return ctx.finish(rp,{"all18WholeOriginalResidualsRetained":True,"all77724OriginalUnitProductsZero":True,
  "wholeOriginalResidualCoordinates":4354*18,"originalUnitProductCoordinates":4318*18,
  "columnIdentities":audit},outputs)

def quotient_lifts(ctx,data,model):
 from flint import fmpq,fmpq_mat
 out=ctx.stage("original-quotient-lifts");rp=out/"complete-original-constant-unit-lifts-receipt.json"
 done=ctx.done(rp)
 if done:return done
 ctx.phase("complete36-by18-residual-schur")
 parent=ctx.out/"whole-unit-residuals"
 cols=[read(parent/("complete-original-unit-column-%02d.json.gz"%j)) for j in range(18)]
 D=[int(x["denominator"]) for x in cols];N=[list(map(int,x["original4318NumeratorColumn"])) for x in cols]
 S=[list(map(int,x["complete4354OriginalResidual"])) for x in cols]
 need(all(x["binding"]==ctx.binding and x["column"]==j and x["all4318OriginalUnitResidualsZero"] for j,x in enumerate(cols)),
  "same full18 original residue columns")
 free=list(map(int,model["sourceFreeRowPositions"]));need(len(free)==36 and len(set(free))==36,"all36 original residual rows")
 mat=[[S[j][i] for j in range(18)] for i in free];scaled=[];rowcontents=[]
 for row in mat:
  g=0
  for value in row:g=math.gcd(g,abs(value))
  g=g or 1;rowcontents.append(g);scaled.append([value//g for value in row])
 RR,rank=fmpq_mat(scaled).rref();rank=int(rank);pp=pivots(RR,rank)
 first_rank=int(fmpq_mat([row[:14] for row in scaled]).rank())
 need(rank==first_rank==12 and all(j<14 for j in pp),
  "actual14 span complete12 incoming classes and all4 true third targets")
 free_incoming=[j for j in range(14) if j not in pp]
 need(len(free_incoming)==2,"exactly two additional homogeneous incoming relations")
 rrfile=out/"complete-original36-by18-residual-schur.json.gz"
 save(rrfile,{"binding":ctx.binding,"rankOverQ":rank,"first14RankOverQ":first_rank,"pivotColumns":pp,
  "sourceFreeRowPositions":free,"complete36By18OriginalResidual":[[str(v) for v in row] for row in mat],
  "nonzeroNormalizedRREFRows":[[str(RR[i,j]) for j in range(18)] for i in range(rank)],
  "rowContents":[str(v) for v in rowcontents],"freeIncomingColumns":free_incoming,
  "allFourTargetsInFullPaidQuotientImage":True,"oldHFandT31SaturationAsserted":False})
 outputs=[rrfile];selected=list(map(int,data["selectedOriginalHFandTColumns"]))
 content=list(map(int,data["selectedIncomingColumnContents"]));targets=list(map(int,data["targetHeadCoordinates"]))
 need(len(selected)==len(content)==14 and targets==[15,18,19,20] and all(c>0 for c in content),
  "all original fourteen incoming labels, contents, and four head labels")
 def relation(col,homogeneous):
  eta=[fmpq(0) for _ in range(14)]
  if homogeneous:eta[col]=fmpq(1)
  for i,j in enumerate(pp):eta[j]=-RR[i,col]
  return eta
 def verify(eta,t=None):
  for i in range(4354):
   value=sum((eta[j]*S[j][i] for j in range(14)),fmpq(0))
   if t is not None:value+=S[t][i]
   need(value==0,"complete4354 original residual relation")
   if i%256==255:ctx.check()
 for a,col in enumerate(free_incoming):
  ctx.check();cp=out/("complete-original-homogeneous-incoming-lift-%02d.json.gz"%a)
  if cp.exists():
   x=read(cp);need(x["binding"]==ctx.binding and x["freeIncomingColumn"]==col and
    x["all4354OriginalResidualCombinationProductsZero"],"same actual homogeneous relation")
  else:
   eta=relation(col,True);verify(eta)
   u=[sum((eta[j]*N[j][i] for j in range(14)),fmpq(0)) for i in range(4318)]
   z=[fmpq(0) for _ in range(36)]
   for j,old in enumerate(selected):z[old]=eta[j]*fmpq(D[j],content[j])
   x={"binding":ctx.binding,"column":a,"freeIncomingColumn":col,
    "complete4318RationalCorrection":[str(v) for v in u],
    "complete36OriginalHFandTCoefficients":[str(v) for v in z],
    "complete14ResidualCombination":[str(v) for v in eta],
    "all4354OriginalResidualCombinationProductsZero":True,
    "equation":"Mstar*u+[HF,T]*z=0; u=sum eta*N; z_pj=eta_j*D_j/content_j",
    "newSecondHeadIndependentOnlyAfterOriginalProductsAndJointRank":True}
   save(cp,x)
  outputs.append(cp);ctx.rec["parameters"]["completedHomogeneousIncomingLifts"]=a+1;ctx.save()
 for a in range(4):
  ctx.check();cp=out/("complete-original-constant-unit-lift-%02d.json.gz"%a)
  if cp.exists():
   x=read(cp);need(x["binding"]==ctx.binding and x["targetHeadCoordinate"]==targets[a] and
    x["all4354OriginalResidualCombinationProductsZero"],"same actual target lift")
  else:
   t=14+a;eta=relation(t,False);verify(eta,t)
   u=[]
   for i in range(4318):
    u.append((fmpq(N[t][i])+sum((eta[j]*N[j][i] for j in range(14)),fmpq(0)))/D[t])
    if i%256==255:ctx.check()
   z=[fmpq(0) for _ in range(36)]
   for j,old in enumerate(selected):z[old]=eta[j]*fmpq(D[j],D[t]*content[j])
   x={"binding":ctx.binding,"column":a,"targetHeadCoordinate":targets[a],
    "originalCorrectionOutputCoordinates":data["originalCorrectionOutputCoordinates"],
    "complete4318RationalCorrection":[str(v) for v in u],
    "complete36OriginalHFandTCoefficients":[str(v) for v in z],
    "complete14ResidualCombination":[str(v) for v in eta],
    "all4354OriginalResidualCombinationProductsZero":True,
    "equation":"Mstar*u+q_target+[HF,T]*z=0; q_target=(R3*Z_target)/g_target already",
    "noSecondDivisionByTargetG":True,"fullNormalizedZeroHeadKernelConstructed":False}
   save(cp,x)
  outputs.append(cp);ctx.rec["parameters"]["completedOriginalParticularLifts"]=a+1;ctx.save()
 return ctx.finish(rp,{"allFourWholeOriginalResidualsCorrected":True,"newParticularRationalLifts":4,
  "newHomogeneousIncomingRelations":2,"completeOriginalResidualSchurRank":12,
  "originalResidualCombinationProducts":4354*6,"completeNormalizedZeroHeadKernelConstructed":False},outputs)

def cochain_context(ctx,data,model):
 if hasattr(ctx,"cochain_data"):return ctx.cochain_data
 p=ctx.paths;old=read(p["old_unit"]);heads=read(p["heads"]);first=read(p["first_jets"])
 J=list(map(int,old["originalSourceRows"]));need(old["binding"]==OLD and J==model["originalSourceRows"],
  "same complete original4354 source order")
 Enew=list(map(int,old["secondCorrectionOutputCoordinates"]));Eold=list(map(int,old["oldFirstCorrectionOutputCoordinates"]))
 E=list(map(int,data["originalCorrectionOutputCoordinates"]));F=list(map(int,old["headComplementCoordinates"]))
 need(E[:1546]==Enew and len(Eold)==1546 and len(F)==3 and len(E)==4318,
  "complete4318 correction and both old1546 embeddings")
 basis=[list(map(int,col)) for col in first["primitiveIntegerVariableColumns"]]
 need(len(basis)==33 and all(len(col)==1582 for col in basis),"actual complete33 first cochain family")
 X=[[basis[j][i] for j in range(33)] for i in range(1546)]
 C=[[basis[j][1546+i] for j in range(33)] for i in range(36)]
 L={int(i):[(int(j),int(v)) for j,v in row] for i,row in heads["primitiveIntegerRows"]}
 outputI=set(map(int,model["originalOutputI"]));need(set(L)<=outputI,"same originalI left-head support")
 rows=original_rows(J,read(p["through4"]))
 ctx.cochain_data={"J":J,"Enew":Enew,"Eold":Eold,"E":E,"F":F,"X":X,"C":C,"L":L,"outputI":outputI,"rows":rows}
 return ctx.cochain_data

def actual_second_cochains(ctx,data,model):
 from flint import fmpq,fmpq_mat
 out=ctx.stage("new-second-products");rp=out/"complete-new-original-second-cochains-receipt.json"
 done=ctx.done(rp)
 if done:return done
 ctx.phase("two-new-second-heads-all-original-three-layer-products")
 d=cochain_context(ctx,data,model);J,E,Eold,F,X,C,L,outputI,rows=[d[k] for k in ("J","E","Eold","F","X","C","L","outputI","rows")]
 outputs=[];newheads=[];certs=[];verified=[]
 for a in range(2):
  ctx.check();lp=ctx.out/"original-quotient-lifts"/("complete-original-homogeneous-incoming-lift-%02d.json.gz"%a)
  lift=read(lp);need(lift["binding"]==ctx.binding and lift["all4354OriginalResidualCombinationProductsZero"],
   "complete new homogeneous incoming relation")
  cp=out/("complete-new-original-second-left-jet-%02d.json.gz"%a)
  vp=out/("verified-new-original-second-left-jet-%02d.json"%a)
  if cp.exists():
   ca=read(cp);need(ca["binding"]==ctx.binding and ca["liftIdentity"]==identity(lp),"same retained new second cochain")
   layers=[list(map(int,row)) for row in ca["primitiveOriginalLambdaLayers"]]
   c=list(map(int,ca["primitiveIntegerParameters"]["complete33FirstKernelCoefficients"]))
  else:
   z=[fmpq(v) for v in lift["complete36OriginalHFandTCoefficients"]]
   u=[fmpq(v) for v in lift["complete4318RationalCorrection"]]
   need(len(z)==36 and len(u)==4318,"full homogeneous source coordinates")
   flat=primitive(z[3:]+z[:3]+u);c,t,u=flat[:33],flat[33:36],flat[36:]
   ch=[sum(C[i][j]*c[j] for j in range(33)) for i in range(36)];ft=[0]*36
   for j,f in enumerate(F):ft[f]=t[j]
   layers=[[0]*4367 for _ in range(3)]
   for i,row in L.items():
    layers[0][i]=sum(v*ch[j] for j,v in row)
    layers[1][i]=sum(v*ft[j] for j,v in row)
   for i in range(1546):layers[1][Eold[i]]+=sum(X[i][j]*c[j] for j in range(33))
   for i,original in enumerate(E):layers[2][original]+=u[i]
   need(any(layers[0]) and all(not v for layer in layers for i,v in enumerate(layer) if i not in outputI),
    "nonzero new second head in same originalI")
   ca={"format":"isp-new-original-natural-second-left-jet-v1","binding":ctx.binding,"column":a,
    "liftIdentity":identity(lp),"oldFirstBasisIdentity":ctx.ids["first_jets"],"oldConstantBasisIdentity":ctx.ids["heads"],
    "primitiveIntegerParameters":{"complete33FirstKernelCoefficients":[str(v) for v in c],
     "threeFirstHeadComplementCoefficients":[str(v) for v in t],"complete4318SecondCorrection":[str(v) for v in u]},
    "primitiveOriginalLambdaLayers":[[str(v) for v in row] for row in layers],
    "formula":"lambda0=Lambda C c; lambda1=Eold X c+Lambda F t; lambda2=Efull u",
    "candidateOnlyUntilMatchingVerifiedReceipt":True}
   save(cp,ca)
  need(len(c)==33 and len(layers)==3 and all(len(v)==4367 for v in layers),"all actual new second cochain entries")
  cid=identity(cp)
  if vp.exists():
   vr=read(vp);need(vr["binding"]==ctx.binding and vr["candidateIdentity"]==cid and
    vr["all13062OriginalProductsZero"],"same complete new second verification")
  else:
   for i,row in enumerate(rows):
    value=[0,0,0]
    for ix,f0,f1,f2,f3,f4 in row:
     l0,l1,l2=[layer[ix] for layer in layers]
     value[0]+=f0*l0;value[1]+=f0*l1+f1*l0;value[2]+=f0*l2+f1*l1+f2*l0
    need(not any(value),"all original three layers for new second column"+str(a)+" at raw"+str(J[i]))
    if i%128==127:ctx.check()
   vr={"binding":ctx.binding,"column":a,"candidateIdentity":cid,"all13062OriginalProductsZero":True,
    "originalSourceRows":4354,"completeCoChainLayers":3,"originalProductCoordinates":13062,
    "sameOriginalOutputISupportVerified":True}
   save(vp,vr)
  outputs.extend([cp,vp]);newheads.append(c);certs.append({"file":cp.name,**cid});verified.append({"file":vp.name,**identity(vp)})
  ctx.rec["parameters"]["completedNewOriginalSecondCoChains"]=a+1;ctx.save()
 oldfull=read(ctx.paths["old_full"]);need(oldfull["status"]=="completed" and oldfull["binding"]==OLD,
  "actual complete old second family")
 audit={q["file"]:q for q in oldfull["outputs"]};oldheads=[]
 for j in range(22):
  name="complete-original-second-left-jet-%02d.json.gz"%j;cp=ctx.paths["old_full"].parent/name
  need(identity(cp)==ident_only(audit[name]),"actual paid old22 cochain bytes")
  ca=read(cp);need(ca["binding"]==OLD,"same old22 cochain binding")
  oldheads.append(list(map(int,ca["firstHeadKernelCoefficients"])))
 rank=int(fmpq_mat(oldheads+newheads).rank())
 need(rank==24 and int(fmpq_mat(oldheads).rank())==22 and int(fmpq_mat(newheads).rank())==2,
  "two actual heads independent modulo old22, completing the full24 domain")
 return ctx.finish(rp,{"allTwoNewOriginalSecondCoChainsVerified":True,"newOriginalThreeLayerProductCoordinates":26124,
  "actualExplicitSecondHeadDimension":24,"completeGlobalSecondHeadDimension":24,
  "all24CompleteSecondHeadsExplicit":True,"allOriginalThreeLayerProductsZero":True,
  "allNewSecondHeadsIndependentModuloPaid22":True,"old22OriginalProductsRecomputed":False,
  "parameters":{"newCandidateIdentities":certs,"newVerifiedIdentities":verified,
   "old22ProductReceiptIdentity":ctx.ids["old_full"],"fullNormalizedZeroHeadKernelConstructed":False}},outputs)

def actual_third_cochains(ctx,data,model):
 from flint import fmpq,fmpq_mat
 out=ctx.stage("original-products");rp=out/"complete-new-original-third-cochains-receipt.json"
 done=ctx.done(rp)
 if done:return done
 ctx.phase("complete-original-four-layer-cochains")
 second=read(ctx.out/"new-second-products"/"complete-new-original-second-cochains-receipt.json")
 need(second["binding"]==ctx.binding and second["status"]=="completed" and second["all24CompleteSecondHeadsExplicit"],
  "actual complete24 second family already verified")
 p=ctx.paths;old=read(p["old_unit"]);prep=read(p["prepared_rhs"])
 heads=read(p["heads"]);first=read(p["first_jets"]);coeff=read(p["through4"]);oldfull=read(p["old_full"])
 need(old["binding"]==OLD and prep["binding"]==PREP,"same original forcing and second family")
 J=list(map(int,old["originalSourceRows"]));need(J==model["originalSourceRows"],"same original4354 source order")
 Enew=list(map(int,old["secondCorrectionOutputCoordinates"]));Eold=list(map(int,old["oldFirstCorrectionOutputCoordinates"]))
 E=list(map(int,data["originalCorrectionOutputCoordinates"]));F=list(map(int,old["headComplementCoordinates"]))
 need(E[:1546]==Enew and len(Eold)==1546 and len(F)==3,"both true correction embeddings retained")
 basis=[list(map(int,c)) for c in first["primitiveIntegerVariableColumns"]]
 need(len(basis)==33 and all(len(c)==1582 for c in basis),"actual complete33 first lift columns")
 X=[[basis[j][i] for j in range(33)] for i in range(1546)]
 C=[[basis[j][1546+i] for j in range(33)] for i in range(36)]
 L={int(i):[(int(j),int(v)) for j,v in row] for i,row in heads["primitiveIntegerRows"]}
 outputI=set(map(int,model["originalOutputI"]));need(set(L)<=outputI,"original constant heads remain in sameI")
 ot={z["file"]:z for z in oldfull["outputs"]};source=[]
 for j,a in enumerate(prep["forcingInputAudit"]):
  name="complete-original-second-left-jet-%02d.json.gz"%j;cp=p["old_full"].parent/name;aid=ot[name]
  need(identity(cp)==ident_only(aid),"actual complete old second cochain")
  ca=read(cp);need(ca["binding"]==OLD,"same old second source binding")
  source.append((list(map(int,ca["firstHeadKernelCoefficients"])),
   list(map(int,ca["threeFirstHeadComplementCoefficients"])),
   list(map(int,ca["secondCorrectionVariables"])),int(a["oldPrimitiveCoChainCommonDivisor"])))
 need(len(source)==22 and all(len(c)==33 and len(t)==3 and len(x)==1546 and d!=0 for c,t,x,d in source),"complete old22 source parameters")
 Z=[list(map(int,c)) for c in prep["headCoordinatesInPrimitiveOld22"]];G=list(map(int,prep["rightHandSideCommonDivisors"]))
 need(len(Z)==len(G)==21 and all(len(v)==22 for v in Z) and all(g>0 for g in G),"complete source21 scaling")
 rows=original_rows(J,coeff);outputs=[];newheads=[];certs=[];verified=[]
 for a,target in enumerate(data["targetHeadCoordinates"]):
  target=int(target);ctx.check()
  cp=out/("complete-new-original-third-left-jet-%02d.json.gz"%a)
  vp=out/("verified-new-original-third-left-jet-%02d.json"%a)
  liftp=ctx.out/"original-quotient-lifts"/("complete-original-constant-unit-lift-%02d.json.gz"%a)
  lift=read(liftp);need(lift["binding"]==ctx.binding and lift["targetHeadCoordinate"]==target and
   lift["all4354OriginalResidualCombinationProductsZero"],"whole original corrected target")
  if cp.exists():
   ca=read(cp);need(ca["binding"]==ctx.binding and ca["liftIdentity"]==identity(liftp),"same actual retained original cochain")
   layers=[list(map(int,v)) for v in ca["primitiveOriginalLambdaLayers"]]
   c=list(map(int,ca["primitiveIntegerParameters"]["oldSecondFirstHeadCoefficients"]))
  else:
   weights=[fmpq(Z[target][k],G[target]*source[k][3]) for k in range(22)]
   c0=[sum((weights[k]*source[k][0][i] for k in range(22)),fmpq(0)) for i in range(33)]
   t0=[sum((weights[k]*source[k][1][i] for k in range(22)),fmpq(0)) for i in range(3)]
   x2=[sum((weights[k]*source[k][2][i] for k in range(22)),fmpq(0)) for i in range(1546)]
   z=[fmpq(v) for v in lift["complete36OriginalHFandTCoefficients"]]
   correction=[fmpq(v) for v in lift["complete4318RationalCorrection"]]
   need(len(z)==36 and len(correction)==4318,"all new particular source parameters")
   groups=[c0,t0,x2,z[:3],z[3:],correction]
   flat=primitive([v for group in groups for v in group]);parts=[];off=0
   for group in groups:parts.append(flat[off:off+len(group)]);off+=len(group)
   c,t,x2i,ai,yi,ui=parts
   ch=[sum(C[i][j]*c[j] for j in range(33)) for i in range(36)]
   yh=[sum(C[i][j]*yi[j] for j in range(33)) for i in range(36)]
   ft=[0]*36;fa=[0]*36
   for j,f in enumerate(F):ft[f]=t[j];fa[f]=ai[j]
   layers=[[0]*4367 for _ in range(4)]
   for i,row in L.items():
    layers[0][i]=sum(v*ch[j] for j,v in row)
    layers[1][i]=sum(v*(ft[j]+yh[j]) for j,v in row)
    layers[2][i]=sum(v*fa[j] for j,v in row)
   for i in range(1546):
    layers[1][Eold[i]]+=sum(X[i][j]*c[j] for j in range(33))
    layers[2][Enew[i]]+=x2i[i]
    layers[2][Eold[i]]+=sum(X[i][j]*yi[j] for j in range(33))
   for i,original in enumerate(E):layers[3][original]+=ui[i]
   need(any(layers[0]) and all(not v for layer in layers for i,v in enumerate(layer) if i not in outputI),
    "nonzero complete head and same originalI support")
   ca={"format":"isp-new-original-natural-third-left-jet-v1","binding":ctx.binding,"column":a,
    "targetHeadCoordinate":target,"liftIdentity":identity(liftp),
    "preparedOriginalRightHandSidesIdentity":ctx.ids["prepared_rhs"],
    "oldFirstBasisIdentity":ctx.ids["first_jets"],"oldConstantBasisIdentity":ctx.ids["heads"],
    "primitiveIntegerParameters":{"oldSecondFirstHeadCoefficients":[str(v) for v in c],
     "oldSecondFirstComplementCoefficients":[str(v) for v in t],"oldSecondCorrectionVariables":[str(v) for v in x2i],
     "thirdFirstComplementCompensation":[str(v) for v in ai],"thirdFirstKernelCompensation":[str(v) for v in yi],
     "complete4318ThirdCorrection":[str(v) for v in ui]},
    "primitiveOriginalLambdaLayers":[[str(v) for v in row] for row in layers],
    "completeLowerBaseFormula":"old22 primitive cochains times Z_target/g_target, including old common divisor",
    "twoEmbeddingFormula":"lambda1 += Lambda C y; lambda2 += Lambda F a+Eold X y; lambda3=Efull u",
    "candidateOnlyUntilMatchingVerifiedReceipt":True}
   save(cp,ca)
  need(len(c)==33 and len(layers)==4 and all(len(v)==4367 for v in layers),"complete four original cochain layers")
  cid=identity(cp)
  if vp.exists():
   vr=read(vp);need(vr["binding"]==ctx.binding and vr["candidateIdentity"]==cid and vr["all17416OriginalProductsZero"],
    "same actual fully verified original third cochain")
  else:
   for i,row in enumerate(rows):
    v=[0,0,0,0]
    for ix,f0,f1,f2,f3,f4 in row:
     l0,l1,l2,l3=[layer[ix] for layer in layers]
     v[0]+=f0*l0;v[1]+=f0*l1+f1*l0
     v[2]+=f0*l2+f1*l1+f2*l0
     v[3]+=f0*l3+f1*l2+f2*l1+f3*l0
    need(not any(v),"all four original products for target"+str(target)+" at raw"+str(J[i]))
    if i%128==127:ctx.check()
   vr={"binding":ctx.binding,"column":a,"targetHeadCoordinate":target,"candidateIdentity":cid,
    "all17416OriginalProductsZero":True,"originalSourceRows":4354,"completeCoChainLayers":4,
    "originalProductCoordinates":17416,"sameOriginalOutputISupportVerified":True}
   save(vp,vr)
  outputs.extend([cp,vp]);newheads.append(c);certs.append({"file":cp.name,**cid});verified.append({"file":vp.name,**identity(vp)})
  ctx.rec["parameters"]["completedNewOriginalThirdCoChains"]=a+1
  ctx.rec["parameters"]["maximumNewCoChainBits"]=max(ctx.rec["parameters"].get("maximumNewCoChainBits",0),
   max(abs(v).bit_length() for layer in layers for v in layer));ctx.save()
 # Reuse actual old17 products by their complete identities; only the joint
 # original33-coordinate head rank is new.
 old17=read(p["old17_products"])
 need(old17["binding"]==CONSUMER and old17["status"]=="completed" and old17["actualExplicitThirdHeadDimension"]==17 and
  old17["allOriginalFourLayerProductsZero"] and old17["allActualHeadCoordinatesIndependent"],"actual old17 four-layer certificates")
 oldheads=[]
 for aid in old17["parameters"]["originalCandidateIdentities"]:
  cp=p["old17_products"].parent/aid["file"];need(identity(cp)==ident_only(aid),"whole paid old17 source bytes")
  ca=read(cp);need(ca["binding"]==CONSUMER,"same paid original17 source binding")
  oldheads.append(list(map(int,ca["primitiveIntegerParameters"]["oldSecondFirstHeadCoefficients"])))
 need(len(oldheads)==17 and len(newheads)==4,"all paid17 and new4 head vectors")
 rank=int(fmpq_mat(oldheads+newheads).rank())
 need(rank==21 and int(fmpq_mat(newheads).rank())==4,"all four missing heads independent modulo paid17")
 return ctx.finish(rp,{"allFourNewOriginalThirdCoChainsVerified":True,"newOriginalFourLayerProductCoordinates":4*17416,
  "paidOriginalFourLayerProductCoordinates":296072,"actualExplicitThirdHeadDimension":21,
  "completeGlobalThirdHeadDimension":21,"all21CompleteThirdHeadsExplicit":True,
  "allOriginalFourLayerProductsZero":True,"allNewHeadsIndependentModuloPaid17":True,
  "old17OriginalProductsRecomputed":False,"maximumNewCoChainBits":ctx.rec["parameters"].get("maximumNewCoChainBits",0),
  "parameters":{"newCandidateIdentities":certs,"newVerifiedIdentities":verified,
   "old17ProductReceiptIdentity":ctx.ids["old17_products"],"fullNormalizedZeroHeadKernelConstructed":False,
   "all33KnownZeroHeadTransportsRetainedByFormula":True,"completeFourthIncomingImageDimension":15,
   "newCompleteSecondFamilyAvailable":True,
   "completeLowerCochainFamiliesAvailableForZeroHeadTransport":True,
   "transportFamilyDimensions":[24,33,36],
   "zeroHeadKernelsExplicitlyExpanded":False}},outputs)


def full_fourth_pairing(ctx,model):
 from flint import fmpq,fmpq_mat,fmpz_mat
 out=ctx.stage("fourth-pairing");rp=out/"complete21-fourth-pairing-receipt.json"
 done=ctx.done(rp)
 if done:return done
 ctx.phase("same29-complete-fourth-domain-and-incoming")
 p=ctx.paths;J=list(map(int,model["originalSourceRows"]));rows=original_rows(J,read(p["through4"]))
 old=read(p["old75"]);old58=read(p["old58"]);sr=read(p["source_receipt"])
 need(old["binding"]==FOURTH and old58["binding"]==THIRD and old["paidThirdPairIdentity"]==ctx.ids["old58"],
  "same actual paid17 fourth and old22 third pairing")
 oldrows=[list(map(int,row)) for row in old["integerRows"]]
 need(len(oldrows)==29 and all(len(row)==75 for row in oldrows) and
  [row[:58] for row in oldrows]==[list(map(int,row)) for row in old58["integerRows"]],
  "exact paid75 and58 original pairing blocks")
 need(sr["binding"]==PAIR and sr["status"]=="completed" and sr["completeFree36ImageRankOverQ"]==29 and
  sr["all29FullOriginal4367ProductsZero"] and sr["parameters"]["sourceBinding"]==SOURCE,
  "paid full true29 original source family")
 sources=[];support=ctx.a.pairing_out/"reconstructed-source29"
 for j,audit in enumerate(sr["parameters"]["verifiedSourceColumns"]):
  aid=audit["certificate"];cp=support/aid["file"];need(identity(cp)==ident_only(aid),"same actual true29 source bytes")
  ca=read(cp);v=list(map(int,ca["original6188IntegerCoefficients"]))
  need(ca["binding"]==SOURCE and ca["column"]==j and len(v)==6188 and
   ca["all1834OutsideSourceCoefficientsZero"] and ca["all4367ExactIntegerProductsZero"] and
   vecsha(v)==audit["sourceSHA256"],"same29 source basis and all paid original kernel identities")
  sources.append([v[i-1] for i in J]);ctx.check()
 need(len(sources)==29,"all same29 source rows")
 second_dir=ctx.out/"new-second-products";third_dir=ctx.out/"original-products"
 second=read(second_dir/"complete-new-original-second-cochains-receipt.json")
 third=read(third_dir/"complete-new-original-third-cochains-receipt.json")
 need(second["binding"]==third["binding"]==ctx.binding and second["status"]==third["status"]=="completed" and
  second["all24CompleteSecondHeadsExplicit"] and third["all21CompleteThirdHeadsExplicit"],
  "both actual complete24 second and21 third cochain families before a full fourth rank")
 forces=[];outputs=[];audit=[]
 specs=[(second_dir,second,3,2),(third_dir,third,4,4)]
 for parent,pr,order,count in specs:
  ids=pr["parameters"]["newCandidateIdentities"];need(len(ids)==count,"complete new forcing family")
  for j,aid in enumerate(ids):
   ctx.check();cp=parent/aid["file"];need(identity(cp)==ident_only(aid),"same actual new cochain bytes")
   ca=read(cp);layers=[list(map(int,row)) for row in ca["primitiveOriginalLambdaLayers"]]
   need(len(layers)==order and all(len(row)==4367 for row in layers),"complete lower cochain layers for forcing")
   fp=out/("new-original-order%d-forcing-%02d.json.gz"%(order,j))
   if fp.exists():
    fc=read(fp);need(fc["binding"]==ctx.binding and fc["candidateIdentity"]==ident_only(aid) and
     fc["order"]==order,"same retained actual original forcing")
    forcing=list(map(int,fc["originalForcingIntegerColumn"]))
   else:
    forcing=[]
    for i,row in enumerate(rows):
     value=0
     for ix,f0,f1,f2,f3,f4 in row:
      fs=[f0,f1,f2,f3,f4]
      for k in range(1,order+1):value+=fs[k]*layers[order-k][ix]
     forcing.append(value)
     if i%256==255:ctx.check()
    fc={"binding":ctx.binding,"column":j,"order":order,"candidateIdentity":ident_only(aid),
     "originalSourceRows":J,"originalForcingIntegerColumn":[str(v) for v in forcing],
     "allLowerOriginalLayerProductsInheritedByHashes":True}
    save(fp,fc)
   need(len(forcing)==4354,"all original forcing coordinates retained")
   forces.append(forcing);outputs.append(fp);audit.append({"file":fp.name,**identity(fp)})
 need(len(forces)==6,"exactly two newR3 and four newR4 columns")
 pairp=out/"complete-same-source29-by81-fourth-pairing.json.gz"
 if pairp.exists():
  q=read(pairp);need(q["binding"]==ctx.binding and q["old75Identity"]==ctx.ids["old75"] and q["newForcingIdentities"]==audit,
   "same complete21-domain complete24-incoming fourth pairing cache")
  combined=[list(map(int,row)) for row in q["integerRows"]]
 else:
  K=fmpz_mat(29,4354,[v for row in sources for v in row])
  F=fmpz_mat(4354,6,[forces[j][i] for i in range(4354) for j in range(6)])
  Z=K*F
  combined=[oldrows[i][:58]+[int(Z[i,j]) for j in range(2)]+oldrows[i][58:]+[int(Z[i,j]) for j in range(2,6)] for i in range(29)]
  save(pairp,{"binding":ctx.binding,"old75Identity":ctx.ids["old75"],"newForcingIdentities":audit,
   "integerRows":[[str(v) for v in row] for row in combined],"rows":29,"columns":81,
   "columnOrder":"HF3,T33,paidR3_on22,newR3_on2,paidR4_on17,newR4_on4",
   "sameOriginal29SourceBasisRetained":True,"all24SecondAnd21ThirdHeadsExplicit":True})
 outputs.append(pairp);ctx.check()
 need(len(combined)==29 and all(len(row)==81 for row in combined),"complete original29-by81 pairing")
 rd=[]
 for row in combined:
  g=0
  for v in row:g=math.gcd(g,abs(v))
  rd.append(g or 1)
 A=[[v//rd[i] for v in row] for i,row in enumerate(combined)];cd=[]
 for j in range(81):
  g=0
  for i in range(29):g=math.gcd(g,abs(A[i][j]))
  cd.append(g or 1)
 normalized=[[A[i][j]//cd[j] for j in range(81)] for i in range(29)]
 r36=int(fmpq_mat([row[:36] for row in normalized]).rank())
 r58=int(fmpq_mat([row[:58] for row in normalized]).rank())
 r60=int(fmpq_mat([row[:60] for row in normalized]).rank())
 rold75=int(fmpq_mat([row[:58]+row[60:77] for row in normalized]).rank())
 need((r36,r58,rold75)==(5,6,7),"all previously paid unscaled ranks remain exactly the same")
 need(r60==8,"actual24 third forcings now span complete W3, not only the old13-dimensional incoming")
 RR,rank=fmpq_mat(normalized).rref();rank=int(rank);pv=pivots(RR,rank)
 beta=rank-r60
 need(3<=beta<=5,"full fourth exact rank must respect paid lower3 and upper5")
 null=[]
 for j in range(81):
  if j in pv:continue
  v=[fmpq(0) for _ in range(81)];v[j]=fmpq(1)
  for i,k in enumerate(pv):v[k]=-RR[i,j]
  null.append(primitive([v[k]/cd[k] for k in range(81)]))
 Z=fmpq_mat(81,len(null),[null[j][i] for i in range(81) for j in range(len(null))])
 need(all(not v for v in (fmpq_mat(combined)*Z).entries()),"all original81 pairing kernel products after restoring column scales")
 P=fmpq_mat(21,len(null),[null[j][60+i] for i in range(21) for j in range(len(null))])
 PR,h=P.transpose().rref();h=int(h)
 need(h==21-beta,"complete21-domain fourth kernel projection")
 hp=out/"complete-original81-kernel-and21-fourth-head-projection.json.gz"
 save(hp,{"binding":ctx.binding,"pairingIdentity":identity(pairp),"rank":rank,"incomingPrefix60Rank":r60,
  "completeFourthRankOverQ":beta,"primitiveOriginal81KernelColumns":[[str(v) for v in c] for c in null],
  "complete21FourthHeadProjectionColumns":[[str(v) for v in primitive([PR[i,j] for j in range(21)])] for i in range(h)],
  "actualProjectionDimension":h,"rowContents":[str(v) for v in rd],"columnContents":[str(v) for v in cd],
  "allOriginal81PairingKernelProductsZero":True,"explicitLambda4SourcesConstructed":False})
 outputs.append(hp)
 return ctx.finish(rp,{"completeGlobalSecondHeadDimension":24,"all24CompleteSecondHeadsExplicit":True,
  "completeGlobalThirdHeadDimension":21,"all21CompleteThirdHeadsExplicit":True,
  "completeFourthIncomingImageComputed":True,"fullIncomingDimension":15,"actualIncomingPairingRank":8,
  "complete21FourthImageComputed":True,"completeCombined29By81PairingRank":rank,
  "fullSelectedFourthRankOverQ":beta,"fullSelectedFourthRankOverQLowerBound":beta,
  "fullSelectedFourthRankOverQUpperBound":beta,"fullSelectedFourthRankExactlyKnown":True,
  "allOriginal81PairingKernelProductsZero":True,"completeFourthHeadDimension":h,
  "selectedMinorInfinityOrderOverQLowerBound":114+h,
  "selectedCofactorInfinityOrderOverQLowerBound":110+h-1,
  "selectedOriginalSourceReplacementOrderOverQLowerBound":110+h-1,
  "explicitLambda4SourcesConstructed":False,"leadingUnitProved":False,
  "parameters":{"sameThirdDomainComplete":True,"completeSecondCochainFamilyAvailable":True,
   "incomingCodimension":0,"rankFormula":"rank29x81-rank(prefix60)=rank29x81-8",
   "quotient":"E/W3 is K29*/pi(W3), since ker(pi) is contained in W2",
   "transportFamilyDimensions":[24,33,36],"zeroHeadKernelsExplicitlyExpanded":False,
   "allLowCochainAmbiguitiesRepresentedByCompleteLowerFamilies":True,
   "costDeferredToActualCurrentCommonFactor":True}},outputs)


def compile_native(a,out,rec):
 build=out/"build";build.mkdir(exist_ok=True)
 src=a.native_source.resolve();sid=identity(src)
 need(sid["sha256"]==CPP_SHA,"exact frozen generic native source")
 flags=shlex.split(a.cxxflags);libs=shlex.split(a.ldflags)
 material={"nativeSource":sid,"compiler":a.compiler,"cxxflags":flags,"ldflags":libs}
 exe=build/"constant-unit-dixon";rp=build/"compile-receipt.json"
 if rp.exists() and exe.exists():
  old=read(rp)
  if old.get("status")=="completed" and old.get("material")==material and identity(exe)==old.get("executableIdentity"):
   rec["compilation"]={**old,"reusedActualCompilation":True};return exe
 start=time.monotonic()
 rr=child([a.compiler,*flags,str(src),"-o",str(exe),*libs],build/"compile.log",a.compile_seconds,2)
 cr={"status":"completed" if rr["exitCode"]==0 else "failed","material":material,
  "compileSecondsLimit":a.compile_seconds,"result":rr,"elapsedSeconds":time.monotonic()-start,
  "mathematicalExecutionPerformed":False}
 if rr["exitCode"]!=0:
  cr["logTail"]=(build/"compile.log").read_text(encoding="utf-8",errors="replace")[-6000:]
  save(rp,cr);rec["compilation"]=cr
  raise ValueError("actual bounded native compilation failed")
 need(exe.exists(),"actual compiled native exists")
 cr["executableIdentity"]=identity(exe);save(rp,cr);rec["compilation"]=cr
 return exe

def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for name in ("constant-preparation-out","unit-prepared-out","second-out","first-out","prepared-out",
              "third-out","consumer-out","pairing-out","fourth-out","native-source","out"):
  ap.add_argument("--"+name,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=600)
 ap.add_argument("--memory-mib",type=int,default=4096)
 ap.add_argument("--compile-seconds",type=float,default=30)
 ap.add_argument("--maximum-digits",type=int,default=100000)
 ap.add_argument("--through",choices=("unit","final"),default="final")
 ap.add_argument("--compiler",default="g++")
 ap.add_argument("--cxxflags",default="-std=c++17 -O2")
 ap.add_argument("--ldflags",default="-lflint -lgmp")
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 0<a.seconds<=7200 and 0<a.memory_mib<=8192 and
  0<a.compile_seconds<=60 and 0<a.maximum_digits<=100000,"explicit bounded original-unit continuation")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 signal.signal(signal.SIGTERM,sigstop);signal.signal(signal.SIGINT,sigstop)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True);wall=time.monotonic();ctx=None
 rec={"format":"isp-missing-third-constant-unit-eighteen-pipeline-v1","status":"running","phase":"compile",
  "outcome":"not-complete","parameters":{"secondsLimit":a.seconds,"memoryMiB":a.memory_mib,"rightHandSides":18,"requestedThrough":a.through},
  "events":[],"completedStages":[],"largeDataUploadedOrCommitted":False,
  "old786PivotsRecomputed":False,"old906DirectionsRecomputed":False,
  "old22SecondProductsRecomputed":False,"old17ThirdProductsRecomputed":False,
  "unitSolutionExactVerified":False,"all18CompleteOriginalResidualsRetained":False,
  "all24CompleteSecondHeadsExplicit":False,"all21CompleteThirdHeadsExplicit":False,
  "completeFourthIncomingImageComputed":False,"fullSelectedFourthRankExactlyKnown":False,
  "explicitLambda4SourcesConstructed":False,"fullNormalizedZeroHeadKernelConstructed":False,
  "leadingUnitProved":False,"characteristicZeroOriginalTargetMembershipProved":False}
 rp=out/"missing-third-constant-unit-pipeline-receipt.json";code=1
 try:
  save(rp,rec);exe=compile_native(a,out,rec);save(rp,rec)
  ctx=Context(a,rec,out);ctx.phase("actual-input-identities")
  ps={
   "prefix":a.constant_preparation_out/"missing-third-constant-unit-preparation-receipt.json",
   "bridge":a.unit_prepared_out/"missing-third-constant-unit-eighteen-preparation-receipt.json",
   "unit_data":a.unit_prepared_out/"constant-unit-eighteen-right-hand-sides.json.gz",
   "model":a.constant_preparation_out/"complete-original-constant-unit-model.json.gz",
   "old_unit":a.second_out/"prepared"/"second-left-m0-unit-input.json.gz",
   "old_full":a.second_out/"full-products"/"second-left-full-products-receipt.json",
   "heads":a.first_out/"left-envelope"/"complete-same-I-characteristic-zero-left-heads.json.gz",
   "first_jets":a.first_out/"left-envelope"/"complete-original-left-first-jets.json.gz",
   "prepared_rhs":a.prepared_out/"complete-third21-original-right-hand-sides.json.gz",
   "old17_products":a.consumer_out/"original-products"/"third21-complete-original-four-layer-products-receipt.json",
   "through4":a.fourth_out/"original-forcing"/"same-original-natural-through-fourth-coefficients.json.gz",
   "old75":a.fourth_out/"pairing"/"actual-same-source29-by75-fourth-on17-pairing.json.gz",
   "old58":a.third_out/"pairing"/"actual-same-source29-by58-third-pairing.json.gz",
   "source_receipt":a.pairing_out/"pairing"/"same-source-koszul29-pairing-worker-receipt.json"}
  pins={**PINS,
   "bridge":(2628,"a692c7c920346fc5473fd8ee662b08d91c709682a1cca7dfb8a7efe8342cf36b"),
   "unit_data":(9305373,"c2d645d0d59aa565c5aea537f66a3e3ba671dd0088f7dd9f3dfde65846405819"),
   "model":(5245792,"cbd7329c2447a6f44a5b8f93a9ba7906c702e5193212cfd4a12137c1b98ce658")}
  ids={k:identity(v) for k,v in ps.items()}
  for k,(n,h) in pins.items():need(ids[k]=={"bytes":n,"sha256":h},"exact actual input "+k)
  prefix=read(ps["prefix"]);bridge=read(ps["bridge"]);data=read(ps["unit_data"]);model=read(ps["model"])
  need(prefix["binding"]==PREFIX_BINDING and prefix["status"]=="completed-prefix" and
   prefix["constantUnitPrime31Proved"] and prefix["parameters"]["programIdentity"]["sha256"]==PREPARER_SHA,
   "actual proven constant unit with former field-rank4 prefix")
  need(bridge["binding"]=="25c4d03014a3754e6b5b22d1ae1d7d8835708a53092b7d2e5b923d151ecebab8" and
   bridge["status"]=="completed" and bridge["outcome"]=="complete-constant-unit-and-eighteen-rhs-prepared" and
   bridge["parameters"]["programIdentity"]["sha256"]==BRIDGE_SHA and bridge["actualRightHandSides"]==18 and
   bridge["constantUnitPrime31Proved"] and bridge["selectedFourteenCompleteOldQuotientBasis"] and
   bridge["actualIncomingPrimitiveFieldRankRetained"]==4,"actual18 bridge and exact source identity")
  audit={z["file"]:z for z in bridge["outputs"]}
  need(ident_only(audit[ps["unit_data"].name])==ids["unit_data"],"actual prepared18 output bytes")
  need(data["binding"]==bridge["binding"] and data["unitSize"]==4318 and data["targets"]==18 and data["incomingColumns"]==14 and
   data["modelIdentity"]==ids["model"] and data["modelSourceBinding"]==PREFIX_BINDING and
   data["prefixReceiptIdentity"]==ids["prefix"] and data["constantUnitPrime31Proved"] and
   data["old36ForcingImageSpannedBySelected14ModuloM0"] and data["selected14StillSpanFull12ImageModuloB0"] and
   not data["oldHFandT31SaturationAsserted"],"complete18 protocol and no false31 saturation")
  need(model["binding"]==PREFIX_BINDING and model["actualOriginalConstantUnitPrime31Proved"] and
   model["allOriginalRowsAndKernelProductsVerified"],"same actual originalMstar model")
  need(data["selectedOriginalHFandTColumns"]==[0,1,2,13,14,18,20,25,26,28,29,30,31,32] and
   data["targetHeadCoordinates"]==[15,18,19,20] and data["targetColumnContents"]==["1"]*4,
   "exact14 rational profile and actualfour target coordinates")
  need(data["sourceUnitRowPositions"]==model["sourceUnitRowPositions"] and
   data["originalCorrectionOutputCoordinates"]==model["correctionOutputCoordinates"],
   "same original unit rows and original output-source columns")
  material={"format":"isp-original-constant-unit-eighteen-semantic-v1","programIdentity":identity(__file__),
   "nativeSourceIdentity":identity(a.native_source),"inputIdentities":ids,"protocol":"R15CUM01/version1",
   "constantUnitSize":4318,"targets":18,"selectedOriginalHFandTColumns":data["selectedOriginalHFandTColumns"],
   "targetHeadCoordinates":data["targetHeadCoordinates"],"completeSecondHeadDimension":24,
   "completeThirdHeadDimension":21,"originalSelectedSourceRows":4354}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  ctx.binding=binding;ctx.paths=ps;ctx.ids=ids;rec["binding"]=binding
  rec["parameters"].update(material);rec["parameters"].update(bridgeBinding=bridge["binding"],
   constantModelBinding=PREFIX_BINDING,actualPreviousPrimitiveIncomingFieldRank=4)
  inv=out/"invocation.json"
  if inv.exists():need(read(inv)["binding"]==binding,"same portable mathematical continuation binding")
  save(inv,{**material,"binding":binding,"paths":{k:str(v.resolve()) for k,v in ps.items()}})
  ctx.save();ctx.check()
  bp,br=prepare_native(ctx,data,model);rec["completedStages"].append("original-native-input")
  sol=native_solve(ctx,exe,bp,br);rec["completedStages"].append("complete-original-unit-solution")
  if a.through=="unit":raise UnitComplete("actual18 unit solution retained before full original correction")
  full=full_residuals(ctx,data,model,sol)
  rec["all18CompleteOriginalResidualsRetained"]=full["all18WholeOriginalResidualsRetained"]
  rec["completedStages"].append("complete18-whole4354-residuals");ctx.save()
  lifts=quotient_lifts(ctx,data,model)
  rec["completedStages"].append("complete36-residual-schur-and-six-lifts")
  rec["parameters"]["actualFullIncomingResidualRank"]=lifts["completeOriginalResidualSchurRank"];ctx.save()
  second=actual_second_cochains(ctx,data,model)
  rec["all24CompleteSecondHeadsExplicit"]=second["all24CompleteSecondHeadsExplicit"]
  rec["allNewOriginalThreeLayerProductsZero"]=second["allOriginalThreeLayerProductsZero"]
  rec["parameters"]["newSecondOriginalProductCoordinates"]=second["newOriginalThreeLayerProductCoordinates"]
  rec["completedStages"].append("complete-two-second-cochains");ctx.save()
  third=actual_third_cochains(ctx,data,model)
  rec["all21CompleteThirdHeadsExplicit"]=third["all21CompleteThirdHeadsExplicit"]
  rec["allNewOriginalFourLayerProductsZero"]=third["allOriginalFourLayerProductsZero"]
  rec["parameters"]["newThirdOriginalProductCoordinates"]=third["newOriginalFourLayerProductCoordinates"]
  rec["completedStages"].append("complete-four-third-cochains");ctx.save()
  fourth=full_fourth_pairing(ctx,model)
  for k in ("completeFourthIncomingImageComputed","fullSelectedFourthRankExactlyKnown","fullSelectedFourthRankOverQ",
            "fullSelectedFourthRankOverQLowerBound","fullSelectedFourthRankOverQUpperBound","completeFourthHeadDimension",
            "completeCombined29By81PairingRank","actualIncomingPairingRank","allOriginal81PairingKernelProductsZero",
            "selectedMinorInfinityOrderOverQLowerBound","selectedCofactorInfinityOrderOverQLowerBound",
            "selectedOriginalSourceReplacementOrderOverQLowerBound"):
   rec[k]=fourth[k]
  rec["completedStages"].append("complete-original29-by81-fourth-pairing")
  rec.update(status="completed",phase="complete",outcome="complete-second24-third21-and-fourth-rank")
  rec["parameters"].update(explicitNewSecondCoChains=2,explicitNewThirdCoChains=4,
   completeLowerCochainFamiliesForZeroHeadTransport=[24,33,36],costUsesCurrentFactorInSeparateProof=True)
  code=0
 except UnitComplete as e:
  rec.update(status="completed-prefix",phase="complete-unit-only",outcome="complete-original-unit-only",note=str(e));code=0
 except BudgetExpired as e:
  rec.update(status="checkpointed-time-budget",outcome="checkpointed-time-budget",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",outcome="failed",error=str(e),exceptionType=type(e).__name__);code=1
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8")
 finally:
  rec["wallElapsedSeconds"]=time.monotonic()-wall
  if ctx is not None:rec["mathematicalElapsedSeconds"]=time.monotonic()-ctx.start
  else:rec["mathematicalElapsedSeconds"]=0.0
  save(rp,rec)
 print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
 return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
