#!/usr/bin/env python3
"""197 true lower-initial third directions: exact local solve and full315 positive continuation."""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,signal,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
from flint import nmod_mat
P=31
HELPER="2026-11-14-r150-ninth-first-matrices-789f.py"
HELPER_SHA="3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a"
# The exact current helper hash is checked again by the input contract.
SCHUR="2026-11-14-r150-local-jet-unit-schur-helper-789f.py"
SCHUR_SHA="d31c917fe0aaa0e9008e5cb0a85cb81600b5a431fe691261948354fb1d1ee42b"
TARGETS=list(range(2,11))
def sha(b):return hashlib.sha256(b).hexdigest()
def load(path,name):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def savejson(path,x):path.write_text(json.dumps(x,separators=(",",":"))+"\n")
def matrix(rows):return nmod_mat(rows,31)
def aslist(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def kernel_labels(path):
 with path.open("rb") as f:data=f.read(24+200*16)
 if data[:8]!=b"R150KK31" or struct.unpack_from("<4I",data,8)!=(31,6188,200,85):raise ValueError("same original200 K header")
 labels=[struct.unpack_from("<IHHII",data,24+16*j) for j in range(200)]
 if [x[2] for x in labels]!=[80]*160+[81]*38+[85]*2:raise ValueError("same original high kernel costs")
 return [x[1] for x in labels],labels
def readmap(a,h):
 b=a.map.read_bytes();meta=json.loads(a.map_receipt.read_text())
 if sha(b)!="3f291285db5a6e97a5db977b3402dbdcc9f7b9e5fb8a48d31b0e219e89e71716" or sha(a.map_receipt.read_bytes())!="5d3e09b26487355b32f20600764664def3dee0be34120e1c8202307eda5526df":raise ValueError("same complete143 map")
 return meta,{key:h.block(b,meta,key) for key in meta["matrices"]}
def readprepared(a,h):
 r=json.loads(a.prepared_receipt.read_text());b=h.actual(a.prepared_system,r["system"]["uncompressedSHA256"])
 if b[:8]!=b"R1503P1A" or r.get("status")!="completed" or not r.get("trueV10InvariantVerified"):raise ValueError("complete actual197 preparation")
 return r,b
def prepare(a,h,start):
 state,J=h.load_state(a.notes_root,a.out)
 five=json.loads(a.five_receipt.read_text());fb=h.actual(a.five_system,five["system"]["uncompressedSHA256"])
 if fb[:8]!=b"R150F3G1" or five.get("status")!="completed" or not five.get("actualFiveH5OriginalMod31SixDivisibilitiesVerified") or not five.get("fiveDirectionRelatedImageComplete") or five.get("newDirectionLabels")!=[9301,9302,9305,9306,9307]:raise ValueError("actual completed five H5 sources")
 U9=h.block(fb,five,"U9");J9=h.block(fb,five,"J9");raw=h.block(fb,five,"allNineRawTargets")
 D5=h.block(fb,five,"actualAll315NewThirdColumns");PD5=h.block(fb,five,"projectedAll315NewThirdColumns")
 if U9.rank()!=9 or J*U9!=U9*J9:raise ValueError("same U9 action")
 oldD,_,_=h.actual_ten_classes(a.ninth_remainders,state)
 if h.sub(oldD,range(315),range(1,10))!=raw:raise ValueError("same whole315 nine current raw")
 b10=h.sub(D5,range(315),[2]);p10=h.sub(PD5,range(315),[2]);V10=h.join(U9,b10)
 if V10.rank()!=10 or h.join(V10,D5).rank()!=10 or h.join(V10,p10).rank()!=10:raise ValueError("true V10 equality to paid five span")
 sp=h.solve_span(U9,b10-p10)
 if not all(sp["flags"]):raise ValueError("true b10/projected b10 coordinate correction")
 gamma=sp["solution"];vsolve=h.solve_span(V10,J*V10);J10=vsolve["solution"]
 if not all(vsolve["flags"]) or V10*J10!=J*V10:raise ValueError("true ten-dimensional invariance")
 projection,Jq,vrows,vfree,vinv,Vf=h.quotient(J,V10)
 if projection(raw).rank()!=3 or not h.zero((Jq-2*nmod_mat([[int(i==j) for j in range(305)] for i in range(305)],31))*projection(raw)):raise ValueError("same three-dimensional semisimple target quotient")
 mapmeta,M=readmap(a,h);p12=mapmeta["globalPrimaryProjectorAscending"]
 f1=h.mul(h.mul([-1,1],[-1,1]),[-1,1]);f2=[1]
 for _ in range(5):f2=h.mul(f2,[-2,1])
 e2=h.mul(f1,h.inverse_mod(f1,f2));projector=h.mul(p12,e2)
 if len(p12)!=190 or len(projector)>197:raise ValueError("paid actual189+7 projection")
 eye=nmod_mat([[int(i==j) for j in range(315)] for i in range(315)],31)
 PM=h.action(projector,J,eye)
 if PM*PM!=PM or PM.rank()!=32 or not h.zero(h.action(f2,J,PM)) or not h.zero(projection(PM*V10)) or not h.zero(projection(raw-PM*raw)):raise ValueError("actual full torsion 2-primary projection")
 if (PM*V10).rank()!=8:raise ValueError("true V10 relevant dimension")
 U7=h.sub(U9,range(315),range(7));U739=M["globalTorsionTo39"]*U7
 if U739.rank()!=7:raise ValueError("true old seven local sources are independent")
 oldmeta=json.loads(a.old_primary_receipt.read_text());ob=h.actual(a.old_primary_system,oldmeta["system"]["sha256"])
 if ob[:8]!=b"R150J2S1" or struct.unpack_from("<8I",ob,8)!=(31,143,104,39,37,198,7,9) or not oldmeta.get("all198GenuineColumnsComputed") or not oldmeta.get("all104FreeChecksVerified"):raise ValueError("actual complete old198 second primary")
 offset=8+8*4+7*4
 def take(n,m):
  nonlocal offset
  b=ob[offset:offset+n*m];offset+=n*m
  if len(b)!=n*m or any(x>30 for x in b):raise ValueError("same old198 matrix bytes")
  return nmod_mat(n,m,list(b),31)
 Yold=take(143,198);Fold=take(104,198);Dold=take(39,198)
 if not h.zero(Fold) or M["torsionEmbedding"]*Dold!=Yold:raise ValueError("old full143 source identities")
 oldlabels,lab=kernel_labels(a.kernels);labels=oldlabels[1:198]
 if oldmeta["actual198KernelHeadLabels"]!=oldlabels[:198]:raise ValueError("old actual high source ordering")
 Csolve=h.solve_span(U739,h.sub(Dold,range(39),range(1,198)))
 if not all(Csolve["flags"]):raise ValueError("old second image not in true U7")
 C=Csolve["solution"]
 payload=b"R1503C31"+struct.pack("<3I",31,7,197)+struct.pack("<197H",*labels)+h.serial(C)
 (a.out/"true-seven-cancellation.bin").write_bytes(payload)
 # A local projected39 column has a unique global2-primary preimage.
 pcols=h.pivots(PM);B32=h.sub(PM,range(315),pcols);L32=M["globalTorsionTo39"]*B32
 lrows=h.pivots(L32.transpose());Linv=h.sub(L32,lrows,range(32)).inv()
 if L32.rank()!=32 or B32.rank()!=32 or M["globalTorsionTo39"]*B32!=L32:raise ValueError("faithful local/global2 correspondence")
 blocks,system=h.save_system(a.out,"prepared-197-third.bin.gz",b"R1503P1A",[31,315,10,197,9],
  [("U7",U7),("U9",U9),("V10",V10),("J10",J10),("trueB10MinusProjectedB10",gamma),("rawTargets",raw),
   ("whole315PrimaryProjector",PM),("globalTwoPrimaryBasis",B32),("localTwoPrimaryBasis",L32),("localTwoPrimaryLeftInverse",Linv),
   ("trueSevenCancellation",C),("old197SecondLocalClasses",h.sub(Dold,range(39),range(1,198))),("quotientAction",Jq)])
 result={"status":"completed","format":"r150-197-third-true-V10-preparation-v1","trueV10InvariantVerified":True,
  "allFiveActualSourcesIncluded":True,"trueB10SourceLabel":9305,"trueB10SourceCost":87,"trueB10Divisor":28629151,
  "trueB10MinusProjectedB10Coefficients":aslist(gamma),"J10TrueSourceBasis":aslist(J10),
  "old198SecondRowsReused":True,"exactK1Deleted":True,"remaining197Labels":labels,
  "trueSevenCancellationVerifiedOnComplete39":True,"all104OldFreeChecksRetained":True,
  "sameCurrentNineRawVerifiedOnWhole315":True,"targetQuotientDimension":3,
  "relevantPrimaryDimension":32,"V10RelevantDimension":8,"relevantQuotientDimension":24,
  "projectorPolynomialAscending":projector,"projectorDegree":len(projector)-1,
  "twoPrimaryAnnihilatorAscending":f2,"globalTwoPrimaryPivotColumns":pcols,"localTwoPrimaryPivotRows":lrows,
  "K1RecipeRequiredSHA256":"f92af9882ddeba99410ded179c4495c0edf66cb06b51b8c9eeb69ddf84f1d1f1",
  "newThirdDirectionsComputed":False,"matrices":blocks,"system":system,"elapsedSeconds":time.monotonic()-start}
 if sha(a.k1_recipe.read_bytes())!=result["K1RecipeRequiredSHA256"]:raise ValueError("actual exactK1 source recipe")
 savejson(a.out/"prepared-197-third-receipt.json",result)
 print(json.dumps({k:result[k] for k in ("status","trueV10InvariantVerified","trueSevenCancellationVerifiedOnComplete39","relevantQuotientDimension","elapsedSeconds")}),flush=True)

def local_solve(a,h,start):
 if sha((a.notes_root/SCHUR).read_bytes())!=SCHUR_SHA:raise ValueError("same exact bounded unit-Schur helper")
 S=load(a.notes_root/SCHUR,"r150_197_exact_schur")
 g=a.G.read_bytes();r=a.rhs.read_bytes();binding=a.binding
 if g[:8]!=b"R1503G31" or struct.unpack_from("<4I",g,8)!=(31,1034,1021,10) or g[24:88].decode()!=binding:raise ValueError("same actual G10")
 if r[:8]!=b"R1503F31" or struct.unpack_from("<4I",r,8)!=(31,1034,197,10) or r[24:88].decode()!=binding:raise ValueError("same full original ten-jet RHS")
 records=[struct.unpack_from("<HBB",g,88+4*i) for i in range(1021)];gp=88+4084
 labels=list(struct.unpack_from("<197H",r,88));rp=88+394+1034*8
 if len(g)!=gp+10*1034*1021 or len(r)!=rp+10*1034*197:raise ValueError("complete ten-jet coefficient arrays")
 if [x[0] for x in records]!=sorted(set(x[0] for x in records)) or sum(x[1] for x in records)!=716:raise ValueError("actual G column labels/degrees")
 constants=[j for j,x in enumerate(records) if x[1]==0];rows=[records[j][0]-1 for j in constants]
 if len(constants)!=573 or len(set(rows))!=573:raise ValueError("actual573 constant units")
 restc=[j for j in range(1021) if j not in set(constants)];restr=[i for i in range(1034) if i not in set(rows)]
 inner=sha((binding+sha(g)+sha(r)+sha(Path(__file__).read_bytes())+SCHUR_SHA).encode())
 checkpoint=a.out/"schur-checkpoints";checkpoint.mkdir(exist_ok=True)
 seconds=max(0.001,a.remaining_seconds-(time.monotonic()-start))
 solver=S.SchurSolver(checkpoint,inner,5,13,seconds)
 if hasattr(signal,"SIGTERM"):
  signal.signal(signal.SIGTERM,lambda *_:(_ for _ in ()).throw(S.Deadline("shared wall-clock boundary")))
 prefile=a.out/"constant-prestrip.json"
 def decodeG(k):return nmod_mat(1034,1021,list(g[gp+k*1034*1021:gp+(k+1)*1034*1021]),31)
 def decodeR(k):return nmod_mat(1034,197,list(r[rp+k*1034*197:rp+(k+1)*1034*197]),31)
 try:
  if prefile.exists():
   pre=json.loads(prefile.read_text())
   if pre["binding"]!=inner or pre["constantRows"]!=rows or pre["constantColumns"]!=constants:raise ValueError("same true constant unit checkpoint")
   mats={k:S.get_series(a.out,v) for k,v in pre["matrices"].items()}
   Gp,Rp,AiB,AiU=mats["Gprime"],mats["rhsprime"],mats["AinvB"],mats["AinvRHS"]
  else:
   G0=decodeG(0);A0=h.sub(G0,rows,constants);Ainv=A0.inv();C0=h.sub(G0,restr,constants)
   if A0*Ainv!=nmod_mat([[int(i==j) for j in range(573)] for i in range(573)],31):raise ValueError("actual constant unit inverse")
   Gp=[];Rp=[];AiB=[];AiU=[]
   for k in range(10):
    solver.tick();Gk=G0 if k==0 else decodeG(k);Rk=decodeR(k)
    if k and not h.zero(h.sub(Gk,range(1034),constants)):raise ValueError("claimed constant G source contains positive jet")
    B=h.sub(Gk,rows,restc);D=h.sub(Gk,restr,restc);U=h.sub(Rk,rows,range(197));V=h.sub(Rk,restr,range(197))
    AB=Ainv*B;AU=Ainv*U;AiB.append(AB);AiU.append(AU);Gp.append(D-C0*AB);Rp.append(V-C0*AU)
   mats={"Gprime":Gp,"rhsprime":Rp,"AinvB":AiB,"AinvRHS":AiU,"actualConstantInverse":[Ainv],"actualConstantC":[C0]}
   desc={k:S.put_series(a.out,"pre-"+k,v) for k,v in mats.items()}
   pre={"binding":inner,"constantRows":rows,"constantColumns":constants,"remainingRows":restr,"remainingColumns":restc,"matrices":desc}
   S.atomic_write(prefile,S.canonical_json(pre))
   del G0,Gk,Rk,A0,Ainv,C0,B,D,U,V,AB,AU,mats
  outer_verify=a.out/"complete-G-verification-checkpoint.json"
  if outer_verify.exists():
   vx=json.loads(outer_verify.read_text())
   if vx["binding"]!=inner or not 0<=vx["verifiedCoefficients"]<=10:raise ValueError("same complete local solution checkpoint")
   q=S.get_series(a.out,vx["solution"]);verified_coefficients=vx["verifiedCoefficients"];qdesc=vx["solution"]
   if S.dims(q)!=(10,1021,197):raise ValueError("actual complete q checkpoint shape")
  else:
   qrest=solver.solve(Gp,Rp,row_labels=restr,col_labels=restc)
   qconst=S.series_sub(AiU,S.series_mul(AiB,qrest,10,solver.tick));q=[]
   for k in range(10):
    z=nmod_mat(1021,197,31)
    for i,j in enumerate(constants):
     for target in range(197):z[j,target]=qconst[k][i,target]
    for i,j in enumerate(restc):
     for target in range(197):z[j,target]=qrest[k][i,target]
    q.append(z)
   qdesc=S.put_series(a.out,"actual1021-q-all-ten-jets",q);verified_coefficients=0
   S.atomic_write(outer_verify,S.canonical_json({"binding":inner,"solution":qdesc,"verifiedCoefficients":0}))
  verified=verified_coefficients*1034*197
  for ell in range(verified_coefficients,10):
   solver.tick();res=nmod_mat(1034,197,31)
   for k in range(ell+1):res+=decodeG(k)*q[ell-k]
   if res!=decodeR(ell):raise ValueError("full1034 original G*q_N ten-jet identity")
   verified+=1034*197
   S.atomic_write(outer_verify,S.canonical_json({"binding":inner,"solution":qdesc,"verifiedCoefficients":ell+1}))
  output=bytearray(b"R1503Q31")+struct.pack("<4I",31,1021,197,10)+binding.encode()+struct.pack("<197H",*labels)
  for j,rec in enumerate(records):
   output+=struct.pack("<HBB",*rec)
   for k in range(10):output+=bytes(int(q[k][j,t]) for t in range(197))
  S.atomic_write(a.out/"complete-G-q2-root2-ten.bin",bytes(output))
  result={"status":"completed","fullOriginalG1034TenJetIdentityVerified":True,"all13FreeConditionsRetained":True,
   "actualConstantColumns":573,"remainingRows":461,"remainingColumns":448,"targetCount":197,"TaylorCenter":2,"TaylorPrecision":10,
   "maximumSmithExponent":5,"allOriginalGJetCoordinatesVerified":verified,"bindingSHA256":binding,
   "helperBindingSHA256":inner,"localSolutionOnly":True,"globalOriginalPolynomialSourceClaimed":False,"elapsedSeconds":time.monotonic()-start}
  savejson(a.out/"local-unit-solve-receipt.json",result);print(json.dumps(result),flush=True)
 except S.Deadline as ex:
  savejson(a.out/"local-unit-solve-receipt.json",{"status":"checkpointed-deadline","bindingSHA256":binding,"message":str(ex),"elapsedSeconds":time.monotonic()-start})
  raise SystemExit(75)

def complete(a,h,start):
 prep,pb=readprepared(a,h);mapmeta,M=readmap(a,h);state,J=h.load_state(a.notes_root,a.out)
 original=json.loads(a.original_metadata.read_text());normal=json.loads(a.normal_metadata.read_text())
 if original.get("mode")!="third" or original.get("status")!="completed" or not all(original.get(k) for k in ("allOriginalProductJetCoefficientsDivisible","fullOriginalTenJetQ2IdentityVerified","thirdTruncatedIntegerFiveBeforeDivision","root1SlotsAreExplicitProjectionZeros")):raise ValueError("actual original197 third jet products")
 if normal.get("status")!="completed" or normal.get("targets")!=197 or not all(normal.get(k) for k in ("fullLocalPrebasisSourceIdentity","fullLocalGQuotientIdentity","allRemaindersStandard")):raise ValueError("complete original197 projected local state")
 raw=a.standard_state.read_bytes()
 if raw[:8]!=b"R1503E31" or struct.unpack_from("<4I",raw,8)!=(31,820,197,8):raise ValueError("actual197 complete820 state")
 labels=list(struct.unpack_from("<197H",raw,24));off=24+394
 coords=[list(struct.unpack_from("<HB",raw,off+3*i)) for i in range(820)];off+=2460
 if labels!=prep["remaining197Labels"] or coords!=mapmeta["standardCoordinates"] or len(raw)!=off+820*197:raise ValueError("actual197 whole standard dictionary")
 E=nmod_mat(820,197,list(raw[off:]),31);Y=M["Pi"]*E;free=M["freeChecks"]*Y;D39=M["torsionCoordinates"]*Y
 if not h.zero(free) or M["torsionEmbedding"]*D39!=Y:
  savejson(a.out/"local-free-failure.json",{"status":"failed","nonzero":[[i,j,int(free[i,j])] for i in range(104) for j in range(197) if free[i,j]]})
  raise ValueError("all104 genuine local free conditions required")
 B=h.block(pb,prep,"globalTwoPrimaryBasis");L=h.block(pb,prep,"localTwoPrimaryBasis");Li=h.block(pb,prep,"localTwoPrimaryLeftInverse")
 D=B*Li*h.sub(D39,prep["localTwoPrimaryPivotRows"],range(197))
 if M["globalTorsionTo39"]*D!=D39:raise ValueError("local third has non2-primary part or wrong original quotient")
 V10=h.block(pb,prep,"V10");J10=h.block(pb,prep,"J10");targets=h.block(pb,prep,"rawTargets")
 PM=h.block(pb,prep,"whole315PrimaryProjector");poly=prep["projectorPolynomialAscending"]
 if PM*D!=D or J*V10!=V10*J10:raise ValueError("actual true source quotient and new projected columns")
 project,Jq,rows,qr,inv,Vf=h.quotient(J,V10);qt=project(targets);columns=project(D);full=D
 current=columns;fullcurrent=D;oldrank=-1;maximum=0
 for power in range(5):
  rank=columns.rank();maximum=power
  if rank>24:raise ValueError("actual relevant24 quotient dimension")
  print(json.dumps({"phase":"complete197-related-third-krylov","maximumPower":power,"rank":rank,"elapsedSeconds":time.monotonic()-start}),flush=True)
  if rank==oldrank:break
  if power<4:
   oldrank=rank;current=Jq*current;fullcurrent=J*fullcurrent;columns=h.join(columns,current);full=h.join(full,fullcurrent)
 if not h.zero(h.action(prep["twoPrimaryAnnihilatorAscending"],Jq,project(D))):raise ValueError("actual five-step third annihilator")
 sol=h.solve_span(columns,qt);basis=sol["basis"];rank=len(sol["indices"])
 JA=sol["inverse"]*h.sub(Jq*basis,sol["rows"],range(rank)) if rank else nmod_mat(0,0,31)
 if basis*JA!=Jq*basis:raise ValueError("complete197 polynomial third image not invariant")
 flags=sol["flags"];F=h.polynomial_solution(sol["indices"],sol["solution"],197)
 for j,ok in enumerate(flags):
  if not ok:
   for i in range(197):F[i][j]=[]
 if max([len(p)-1 for row in F for p in row]+[-1])>4:raise ValueError("paid local coefficient bound4")
 combination=h.source_action(J,D,F);masked=nmod_mat(aslist(targets),31)
 for j,ok in enumerate(flags):
  if not ok:
   for i in range(315):masked[i,j]=0
 correction=inv*h.sub(masked-combination,rows,range(9))
 if V10*correction!=masked-combination:raise ValueError("positive local identities with true V10 correction")
 duals=[]
 for j,ok in enumerate(flags):
  if ok:duals.append(None);continue
  k=next(i for i in range(305) if sol["residual"][i,j]);d=nmod_mat(1,305,31);d[0,k]=1
  if rank:
   c=h.sub(basis,[k],range(rank))*sol["inverse"]
   for i,row in enumerate(sol["rows"]):d[0,row]-=c[0,i]
  value=int((d*qt)[0,j]);d=pow(value,-1,31)*d
  if not h.zero(d*columns) or (d*qt)[0,j]!=1:raise ValueError("complete197 actual quotient dual")
  fullrow=nmod_mat(1,315,31)
  for i,row in enumerate(qr):fullrow[0,row]=d[0,i]
  c=d*Vf*inv
  for i,row in enumerate(rows):fullrow[0,row]-=c[0,i]
  fullrow=h.row_action(poly,J,fullrow)
  if not h.zero(fullrow*V10) or not h.zero(fullrow*full) or (fullrow*targets)[0,j]!=1:raise ValueError("actual complete projected third dual")
  duals.append({"target":TARGETS[j],"full315PrimaryComposedWeights":[int(fullrow[0,i]) for i in range(315)],
   "targetValue":1,"annihilatesTrueV10":True,"annihilatesWhole197RelevantThirdPolynomialImage":True,
   "scope":"complete relevant2-primary third obstruction in the proved F9/Lambda2 natural-source graph; not all original integer sources and not characteristic zero"})
 blocks,system=h.save_system(a.out,"complete-197-third-image.bin.gz",b"R1503G1A",[31,315,10,197,9],
  [("local143Columns",Y),("all104FreeChecks",free),("local39ThirdColumns",D39),("projected315ThirdColumns",D),
   ("V10",V10),("J10",J10),("rawTargets",targets),("quotientAction",Jq),("completeRelatedKrylov",columns),
   ("full315ProjectedKrylov",full),("selectedBasis",basis),("selectedBasisAction",JA),("targetResidual",sol["residual"]),
   ("actualLocalChosenCombination",combination),("actualLocalTrueV10Correction",correction)])
 result={"status":"completed","format":"r150-complete197-relevant-low-initial-third-image-v1",
  "all197ThirdDirectionsComputed":True,"all197OriginalLocalTenJetIdentitiesVerified":True,
  "all143LocalCoordinatesRetained":True,"all104LocalFreeChecksVerified":True,
  "oldFiveThirdDirectionsReused":True,"exactK1Covered":True,"low1632ExactDirectionsCovered":True,
  "oldFourHighExactDirectionsCovered":True,"higherDigitImagesPaid":True,
  "completeRelevantLowInitialThirdImageComputed":True,"completeGlobalThirdImageComputed":False,
  "originalWholeIntegerLatticeClaimed":False,"characteristicZeroIdentityAsserted":False,
  "targetLabels":TARGETS,"sourceLabels":labels,"relevantPrimaryRoot":2,"relevantQuotientDimension":24,
  "newRelatedThirdImageRank":rank,"KrylovMaximumPower":maximum,"KrylovColumnCount":columns.ncols(),
  "individualTargetCompatible":flags,"compatibleTargetLabels":[j for j,ok in zip(TARGETS,flags) if ok],
  "obstructedWithinNaturalGraphTargetLabels":[j for j,ok in zip(TARGETS,flags) if not ok],
  "allNineCompatible":all(flags),"numberOfCompatibleTargets":sum(flags),
  "solutionPolynomialsAscending":F,"maximumSolutionDegree":max([len(p)-1 for row in F for p in row]+[-1]),
  "projectorPolynomialAscending":poly,"projectorDegree":len(poly)-1,
  "allPositiveLocal315ProjectedIdentitiesVerified":True,"localPositiveIsNotGlobalOriginalIdentity":True,
  "completeRelevantDuals":duals,"matrices":blocks,"system":system,
  "outcome":"relevant-primary-compatible-global-source-continuation-required" if any(flags) else "complete-relevant-low-initial-third-obstruction",
  "elapsedSeconds":time.monotonic()-start}
 savejson(a.out/"complete-197-third-image-receipt.json",result)
 print(json.dumps({k:result[k] for k in ("status","all197ThirdDirectionsComputed","completeRelevantLowInitialThirdImageComputed","newRelatedThirdImageRank","individualTargetCompatible","outcome","elapsedSeconds")}),flush=True)

def nine_classes(path,state,h,labels):
 data=path.read_bytes();wide=data[:8]==b"R150NX31"
 if (not wide and data[:8]!=b"R150NF31") or struct.unpack_from("<3I",data,8)!=(0,9,1034):raise ValueError("all nine complete G remainders")
 index={tuple(c):i for i,c in enumerate(state["coordinates"])};V=nmod_mat(820,9,31);off=20
 for j in range(9):
  raw,label,n=struct.unpack_from("<IHI",data,off);off+=10
  if raw or label!=labels[j]:raise ValueError("actual synthetic nine source labels")
  previous=0
  for _ in range(n):
   c=struct.unpack_from("<H",data,off)[0];off+=2;size=2 if wide else 1;l=int.from_bytes(data[off:off+size],"little");off+=size
   if c<=previous or c>1034 or l<1:raise ValueError("complete G coordinate dictionary")
   previous=c
   for d in range(l):
    x=data[off];off+=1
    if x>30:raise ValueError("canonical whole remainder")
    if x:
     if (c,d) not in index:raise ValueError("synthetic whole original vector has a high free remainder")
     V[index[c,d],j]=x
 if off!=len(data):raise ValueError("whole G remainder tail")
 free=[i for i in range(820) if i+1 not in set(state["pivotStateCoordinates"])]
 D=h.sub(V,free,range(9));K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose();O=nmod_mat(state["observabilityEchelon"],31)
 if K*D!=V or not h.zero(O*V):raise ValueError("all505 free tests and315 whole source reconstruction")
 return D,V
def global_check(a,h,start):
 prep,pb=readprepared(a,h);complete=json.loads(a.complete_receipt.read_text());flags=complete["individualTargetCompatible"]
 if complete.get("status")!="completed" or not complete.get("completeRelevantLowInitialThirdImageComputed") or not any(flags):raise ValueError("actual positive local source continuation")
 state,J=h.load_state(a.notes_root,a.out);second=a.mode=="global-second";labels=list(range(9402,9411)) if second else list(range(9502,9511))
 original=json.loads(a.original_metadata.read_text());image=json.loads(a.image_metadata.read_text());div=961 if second else 28629151
 if original.get("status")!="completed" or original.get("targetLabels")!=labels or original.get("modulus")!=887503681 or original.get("divisor")!=div or not original.get("allOriginalProductCoefficientsDivisible"):raise ValueError("actual original full synthetic divisibility")
 if image.get("status")!="completed" or image.get("targets")!=9 or not image.get("fullImageQuotientIdentity") or not image.get("everyRemainderIsIrreducible"):raise ValueError("complete global synthetic G identity")
 D,V=nine_classes(a.image_remainders,state,h,labels);PM=h.block(pb,prep,"whole315PrimaryProjector");PD=PM*D
 U=h.block(pb,prep,"U7" if second else "V10");target=PD
 if not second:
  target=h.block(pb,prep,"rawTargets")
  for j,ok in enumerate(flags):
   if not ok:
    for i in range(315):target[i,j]=0
  target=target-PD
 for j,ok in enumerate(flags):
  if not ok and any(D[i,j] for i in range(315)):raise ValueError("inactive synthetic original column is not zero")
 sol=h.solve_span(U,target)
 if not all(sol["flags"]):raise ValueError("projected global source does not reconcile with the actual seven/ten source space")
 C=sol["solution"]
 if U*C!=target:raise ValueError("full315 source correction identity")
 blocks,system=h.save_system(a.out,"global-second-reconciliation.bin.gz" if second else "global-third-reconciliation.bin.gz",
  b"R1503C2A" if second else b"R1503C5A",[31,315,U.ncols(),9],
  [("whole315ActualSyntheticColumns",D),("whole820ActualSyntheticColumns",V),("projectedSyntheticColumns",PD),
   ("trueConstantSourceBasis",U),("actualConstantCorrections",C),("whole315Difference",target)])
 result={"status":"completed","format":"r150-197-third-whole315-continuation-v1","mode":a.mode,
  "all505FreeObservationsVerified":True,"all315SyntheticCoordinatesVerified":True,
  "allCompatibleWhole315IdentitiesVerified":True,"individualTargetCompatible":flags,
  "actualConstantCorrections":aslist(C),"constantSourceCount":U.ncols(),
  "projectorPolynomialAscending":prep["projectorPolynomialAscending"],"sourceDivisor":div,
  "trueUnprojectedB10Used":not second,"oldFivePolynomialCombinationNotRecomputed":True,
  "matrices":blocks,"system":system,"elapsedSeconds":time.monotonic()-start}
 savejson(a.out/("global-second-reconciliation.json" if second else "global-third-reconciliation.json"),result)
 print(json.dumps({k:result[k] for k in ("status","mode","all505FreeObservationsVerified","allCompatibleWhole315IdentitiesVerified","elapsedSeconds")}),flush=True)
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--mode",choices=("prepare","local-solve","complete","global-second","global-third"),required=True)
 p.add_argument("--notes-root",type=Path,required=True);p.add_argument("--out",type=Path,required=True)
 for key in ("five-receipt","five-system","old-primary-receipt","old-primary-system","map","map-receipt","ninth-remainders","kernels","k1-recipe","prepared-receipt","prepared-system","original-metadata","normal-metadata","standard-state","complete-receipt","image-metadata","image-remainders","G","rhs"):p.add_argument("--"+key,type=Path)
 p.add_argument("--binding");p.add_argument("--remaining-seconds",type=float,default=300)
 a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 path=a.notes_root/HELPER
 if sha(path.read_bytes())!="3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a":raise ValueError("same complete arithmetic helper")
 h=load(path,"r150_197_third_arithmetic")
 if a.mode=="prepare":prepare(a,h,start)
 elif a.mode=="local-solve":local_solve(a,h,start)
 elif a.mode=="complete":complete(a,h,start)
 else:global_check(a,h,start)
if __name__=="__main__":main()
