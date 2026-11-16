#!/usr/bin/env python3
"""Rebuild complete original ten-generator parameter-module seeds at127.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
All17 original gradients, the global Bell chart,50 literal border columns,
six mean columns,100 commutator columns and ten Bell columns remain.
This creates a verified finite-field candidate model, never a Q unit-ideal claim.
No parameter is specialized; the only field map is the legal fixed E-place.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,itertools,json,os,resource,signal,sys,time
from pathlib import Path
from flint import fmpq,nmod_mat,nmod_mpoly_ctx
sys.set_int_max_str_digits(0)
FORMAT="r150-original-ten-generator-complete-parameter-seeds127-v2"
P=127;ROOT=100
MODEL_SHA="da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d"
HELPER_SHA="31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10"
MATCHED=[52565262336,6080833024,-43931504,3725]
HP=[2,1,0,3,4,5];HU=[6,7,8,9,10]
KEEP=[(1,4),(2,3),(2,4),(3,4)]
OLD_NAMES=tuple(["y%d"%i for i in range(6)]+["H%d"%i for i in range(11)])
NEW_NAMES=tuple(["y%d"%i for i in range(6)]+["w%d"%i for i in range(6)]+["u%d"%i for i in range(5)])
CTX=nmod_mpoly_ctx.get(NEW_NAMES,P,"lex")
OCTX=nmod_mpoly_ctx.get(OLD_NAMES,P,"lex")
ZERO=CTX.constant(0);ONE=CTX.constant(1)
GEN=CTX.gens();Y=GEN[:6];W=GEN[6:12];U=GEN[12:]
def need(b,msg):
 if not b:raise ValueError(msg)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 h=hashlib.sha256()
 with Path(p).open("rb") as f:
  for q in iter(lambda:f.read(1048576),b""):h.update(q)
 return {"path":Path(p).name,"bytes":Path(p).stat().st_size,"sha256":h.hexdigest()}
def atomic(p,data):
 p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+".tmp");tmp.write_bytes(data);os.replace(tmp,p)
def save_json(p,x):
 raw=canon(x);atomic(p,raw);return {"path":p.name,"bytes":len(raw),"sha256":sha(raw)}
def save_gz(p,data,binding):
 raw=canon({"format":FORMAT+"-phase","binding":binding,"data":data})
 z=gzip.compress(raw,compresslevel=1,mtime=0);atomic(p,z)
 return {"path":p.name,"bytes":len(z),"sha256":sha(z),"logicalBytes":len(raw),"logicalSha256":sha(raw)}
def load_gz(p,d,binding):
 z=p.read_bytes();need(len(z)==d["bytes"] and sha(z)==d["sha256"],"complete compressed phase")
 raw=gzip.decompress(z);need(len(raw)==d["logicalBytes"] and sha(raw)==d["logicalSha256"],"complete logical phase")
 v=json.loads(raw);need(v["format"]==FORMAT+"-phase" and v["binding"]==binding,"same original model phase")
 return v["data"]
def module(p,expected,name):
 need(identity(p)["sha256"]==expected,"exact source "+name)
 sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def residue(q):
 q=fmpq(q);a=int(q.denom())%P;need(a!=0,"all original rational coefficients127-integral")
 return int(q.numer())%P*pow(a,-1,P)%P
def qpoly(row,ctx):
 v={}
 for ee,c in row:
  e=tuple(ee);need(len(e)==17 and e not in v and all(type(t)is int and t>=0 for t in e),"all literal original rational monomials")
  v[e]=residue(c)
 return ctx.from_dict({e:c for e,c in v.items() if c})
def pack(f):
 return [[list(map(int,e)),int(c)] for e,c in sorted(f.to_dict().items())]
def unpack(v):
 d={}
 for e,c in v:
  e=tuple(e);need(len(e)==17 and e not in d and all(type(z)is int and z>=0 for z in e) and type(c)is int and 0<c<P,"canonical complete polynomial record")
  d[e]=c
 return CTX.from_dict(d)
def packvec(v):return [pack(x) for x in v]
def unpackvec(v):return [unpack(x) for x in v]
def mons(n,d):
 out=[]
 for ii in itertools.combinations_with_replacement(range(n),d):
  e=[0]*n
  for i in ii:e[i]+=1
  out.append(tuple(e))
 return out
M2=mons(5,2);M3=mons(5,3)
def umon(e):
 v=ONE
 for i,k in enumerate(e):
  if k:v*=U[i]**k
 return v
MEXP=[(0,)*5]+[tuple(int(i==j) for i in range(5)) for j in range(5)]
for i,j in KEEP:MEXP.append(tuple(int(a==i)+int(a==j) for a in range(5)))
MON=[umon(e) for e in MEXP]
def eye(n):return nmod_mat([[int(i==j) for j in range(n)] for i in range(n)],P)
def mat(v):return nmod_mat(v,P)
def tab(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def inverse(A,label):
 need(A.nrows()==A.ncols(),label+" square")
 det=int(A.det());need(det!=0,label+" actual nonzero unit")
 V=A.inv();need(A*V==eye(A.nrows()) and V*A==eye(A.nrows()),label+" both full inverse products")
 return V,det
def addv(a,b):return [x+y for x,y in zip(a,b)]
def subv(a,b):return [x-y for x,y in zip(a,b)]
def scale(a,c):return [c*x for x in a]
def zerov(n):return [ZERO for _ in range(n)]
def unit(n,i):return [ONE if j==i else ZERO for j in range(n)]
def dot(a,b):
 need(len(a)==len(b),"whole scalar source product lengths")
 return sum((x*y for x,y in zip(a,b)),ZERO)
def mv(A,v):
 need(all(len(row)==len(v) for row in A),"complete parameter matrix action dimensions")
 return [dot(row,v) for row in A]
def coeff_u(f,maximum=3):
 data={}
 for e,c in f.to_dict().items():
  ue=tuple(map(int,e[12:]));need(sum(ue)<=maximum,"full moment degree bound")
  pe=tuple(map(int,e[:12]))+(0,)*5
  data.setdefault(ue,{})[pe]=int(c)
 return {e:CTX.from_dict(v) for e,v in data.items()}
def constant(f,label):
 d=f.to_dict();need(not d or set(d)=={(0,)*17},label+" fixed coefficient")
 return int(d.get((0,)*17,0))
def param(f):
 need(all(not any(e[12:]) for e in f.to_dict()),"all moment variables genuinely eliminated")
 return f
def original_chart(fd,m):
 original=fd.prepare(m)
 need(original["matchedCubic"]==MATCHED and original["all17OriginalGradientPolynomialsVerified"] and
      original["all512OriginalJ3InverseProductsVerified"] and original["allWeightedEulerCoefficientsVerified"],
      "all original physical source identities")
 need(sum(c*pow(ROOT,i,P) for i,c in enumerate(MATCHED))%P==0 and
      sum(i*c*pow(ROOT,i-1,P) for i,c in enumerate(MATCHED) if i)%P==49,
      "same simple original number-field place")
 oldG=[qpoly(row,OCTX) for row in original["originalSeventeenGradients"]]
 oldR=qpoly(original["R3"],OCTX)
 bell=sum((pow(ROOT,i,P)*qpoly(row,OCTX) for i,row in enumerate(original["BellFieldComponents"])),OCTX.constant(0))
 L=[[0]*11 for _ in range(6)];pure={}
 for e,c in bell.to_dict().items():
  if sum(e[6:]):
   need(sum(e[:6])==1 and sum(e[6:])==1,"every original Bell Hankel term y-linear")
   a=next(i for i,v in enumerate(e[:6]) if v);j=next(i for i,v in enumerate(e[6:]) if v)
   L[a][j]=int(c)
  else:
   need(sum(e[:6])==3,"original pure Bell is cubic")
   pure[tuple(map(int,e))]=int(c)
 Cold=OCTX.from_dict(pure);Cnew=CTX.from_dict(pure)
 A=mat([[L[i][j] for j in HP] for i in range(6)])
 Ai,detA=inverse(A,"same original six Bell Hankel columns")
 rhs=[W[i]-sum((L[i][j]*U[k] for k,j in enumerate(HU)),ZERO)-Cnew.derivative(i)*pow(3,-1,P) for i in range(6)]
 hh=[ZERO for _ in range(11)]
 for k,j in enumerate(HU):hh[j]=U[k]
 for k,j in enumerate(HP):hh[j]=sum((int(Ai[k,i])*rhs[i] for i in range(6)),ZERO)
 backward=list(Y)+hh
 og=OCTX.gens()
 forward=list(og[:6])+[sum((L[i][j]*og[6+j] for j in range(11)),OCTX.constant(0))+Cold.derivative(i)*pow(3,-1,P) for i in range(6)]+[og[6+j] for j in HU]
 need(all(backward[i].compose(*forward)==og[i] for i in range(17)),"all17 original inverse-then-forward identities")
 need(all(forward[i].compose(*backward)==GEN[i] for i in range(17)),"all17 original forward-then-inverse identities")
 need(bell.compose(*backward)==sum((Y[i]*W[i] for i in range(6)),ZERO),"whole original Bell equals y dot w")
 R=oldR.compose(*backward);composed=[g.compose(*backward) for g in oldG]
 order=list(range(12,17))+list(range(6,12))+list(range(6))
 coord=list(range(6,17))+list(range(6))
 J=[[backward[b].derivative(a) for b in coord] for a in order]
 GG=[R.derivative(i) for i in order]
 need(all(dot(row,composed)==g for row,g in zip(J,GG)),"all17 literal original gradient-Jacobian source identities")
 backJ=[[backward[i].derivative(j) for j in range(17)] for i in range(17)]
 forwJ=[[forward[i].derivative(j).compose(*backward) for j in range(17)] for i in range(17)]
 for i in range(17):
  for j in range(17):
   v=ONE if i==j else ZERO
   need(sum((backJ[i][k]*forwJ[k][j] for k in range(17)),ZERO)==v,"all289 backward-forward source Jacobian coordinates")
   need(sum((forwJ[i][k]*backJ[k][j] for k in range(17)),ZERO)==v,"all289 forward-backward source Jacobian coordinates")
 B=sum((Y[i]*W[i] for i in range(6)),ZERO)
 need(all(sum(e[12:])<=2 for g in GG for e in g.to_dict()),"all17 transformed gradient moment degrees")
 return original,{"originalPhysicalLogicalSHA256":sha(canon(original)),"originalHankelPivotOrder":HP,"originalHankelFreeOrder":HU,
  "originalBellUnit":tab(A),"originalBellUnitInverse":tab(Ai),"originalBellUnitDeterminant127":detA,
  "all34OriginalPolynomialInverseCoordinatesVerified":True,"all578OriginalJacobianCoordinatesVerified":True,
  "all17OriginalGradientSourceIdentitiesVerified":True,"sameOriginalBellPolynomialVerified":True,
  "originalPotential":pack(R),"originalComposedGradients":packvec(composed),"newGradients":packvec(GG),
  "originalGradientTransport": [packvec(row) for row in J],
  "coordinateInverse":packvec(backward),"coordinateForwardOriginalContext":[pack(v) for v in forward],
  "originalBellMinusOne":pack(B-ONE),"pureBellCubic":pack(Cnew)}

def build_base(chart):
 A=unpackvec(chart["newGradients"])+[unpack(chart["originalBellMinusOne"])]
 F=A[:5];Wg=A[5:11];Yg=A[11:17]
 squares=[tuple(2*int(i==j) for i in range(5)) for j in range(5)]
 topF=[coeff_u(g,2) for g in F]
 Q=mat([[constant(topF[i].get(e,ZERO),"original five square block") for e in squares] for i in range(5)])
 Qi,detQ=inverse(Q,"same original five-square coefficient block")
 G=list(F);Gsrc=[unit(18,i) for i in range(5)]
 for j,g in enumerate(Wg):
  parts=coeff_u(g,2)
  alpha=mat([[constant(parts.get(e,ZERO),"complete w-square coefficient") for e in squares]])
  cc=alpha*Qi
  lam=[int(cc[0,i]) for i in range(5)]
  nf=g-dot(F,[CTX.constant(c) for c in lam])
  src=subv(unit(18,5+j),[sum((lam[k]*unit(18,k)[i] for k in range(5)),ZERO) for i in range(18)])
  need(dot(A,src)==nf and all(coeff_u(nf,2).get(e,ZERO)==0 for e in squares),"complete original w-square source reduction")
  G.append(nf);Gsrc.append(src)
 need(len(G)==11 and len(Gsrc)==11,"all original eleven moment generators")
 gparts=[coeff_u(g,2) for g in G]
 gtop=[[constant(d.get(e,ZERO),"complete original quadratic top") for e in M2] for d in gparts]
 kept=[M2.index(e) for e in MEXP[6:]]
 elim=[j for j in range(15) if j not in kept]
 A2=mat([[gtop[g][j] for g in range(11)] for j in elim])
 A2i,det2=inverse(A2,"complete original eleven quadratic coefficient unit")
 def normal2(poly):
  parts=coeff_u(poly,2)
  v=[parts.get(M2[j],ZERO) for j in elim]
  sourceG=[sum((int(A2i[g,j])*v[j] for j in range(11)),ZERO) for g in range(11)]
  nf=poly-dot(G,sourceG)
  pp=coeff_u(nf,2);need(set(pp)<=set(MEXP),"full degree-two normal form in ten actual monomials")
  vector=[param(pp.get(e,ZERO)) for e in MEXP]
  source=[sum((sourceG[g]*Gsrc[g][i] for g in range(11)),ZERO) for i in range(18)]
  need(poly-dot(MON,vector)==dot(A,source),"complete original degree-two source identity")
  return vector,source
 for g in G:
  v,s=normal2(g);need(all(x==0 for x in v),"all eleven full quadratic generators have zero normal form")
 columns=[(g,i) for g in range(11) for i in range(5)]
 C3=mat([[next((gtop[g][M2.index(tuple(e[k]-int(k==i) for k in range(5)))] for _ in [0] if e[i]>0),0)
          for g,i in columns] for e in M3])
 rr,rank=C3.rref();need(rank==35,"all35 original cubic outputs spanned by all55 original columns")
 piv=[]
 for i in range(rank):
  j=next(j for j in range(55) if int(rr[i,j]));piv.append(j)
 need(piv==sorted(set(piv)) and len(piv)==35,"complete actual original-column pivot dictionary")
 Cunit=mat([[int(C3[i,j]) for j in piv] for i in range(35)])
 Ci,det3=inverse(Cunit,"same complete original cubic source unit")
 need(det3==32,"same paid original cubic unit determinant127")
 cache={}
 def normal_monomial(e):
  if e in cache:return cache[e]
  poly=umon(e);d=sum(e)
  if d<=2:v,s=normal2(poly)
  else:
   need(d==3 and e in M3,"only actual cubic border products")
   row=M3.index(e);sourceG=zerov(11)
   for k,j in enumerate(piv):
    g,i=columns[j];sourceG[g]+=int(Ci[k,row])*U[i]
   rem=poly-dot(G,sourceG);need(all(sum(x[12:])<=2 for x in rem.to_dict()),"all original cubic terms cancel")
   v,t=normal2(rem)
   s=addv([sum((sourceG[g]*Gsrc[g][i] for g in range(11)),ZERO) for i in range(18)],t)
   need(poly-dot(MON,v)==dot(A,s),"whole original cubic-border source product")
  cache[e]=(v,s);return v,s
 N=[];SS=[]
 for i in range(5):
  cols=[];sources=[]
  for e in MEXP:
   ee=list(e);ee[i]+=1
   v,s=normal_monomial(tuple(ee));cols.append(v);sources.append(s)
  N.append([[cols[j][a] for j in range(10)] for a in range(10)])
  SS.append([[sources[j][a] for j in range(10)] for a in range(18)])
 for i in range(5):
  for a in range(10):
   need(U[i]*MON[a]-dot(MON,[N[i][j][a] for j in range(10)])==
        dot(A,[SS[i][j][a] for j in range(18)]),"all50 original border columns multiply back")
 for i in range(5):
  need([N[i][a][0] for a in range(10)]==unit(10,1+i) and
       all(SS[i][a][0]==0 for a in range(18)),"all five original literal degree-one cyclic paths")
 for k,(i,j) in enumerate(KEEP):
  need([N[i][a][1+j] for a in range(10)]==unit(10,6+k) and
       all(SS[i][a][1+j]==0 for a in range(18)),"all four original literal degree-two cyclic paths")
 # Independent literal completeness: every original quadratic generator
 # times e0 is an original border combination, retaining all10 coordinates.
 Rm=[[[ (U[i] if a==j else ZERO)-N[i][a][j] for j in range(10)] for a in range(10)] for i in range(5)]
 for g in G:
  rem=scale(unit(10,0),g)
  for e,c in coeff_u(g,2).items():
   if sum(e)==0:continue
   if sum(e)==1:
    i=e.index(1);rel=[Rm[i][a][0] for a in range(10)]
   else:
    ii=[k for k,v in enumerate(e) for _ in range(v)];i,j=ii
    rel=[U[i]*Rm[j][a][0]+Rm[i][a][1+j] for a in range(10)]
   rem=subv(rem,scale(rel,c))
  need(all(x==0 for x in rem),"all110 module coordinates: eleven original generators are in the border submodule")
 H=[];Hs=[]
 for j,g in enumerate(Yg):
  v,t=normal2(g);s=subv(unit(18,11+j),t)
  need(dot(MON,v)==dot(A,s),"all six complete original mean source identities")
  H.append(v);Hs.append(s)
 T=[]
 for k in range(4):
  tk=[]
  for j in range(6):
   d=H[j][6+k].to_dict()
   row=[int(d.get(tuple(int(a==l) for a in range(17)),0)) for l in range(6)]
   need(H[j][6+k]==sum((row[l]*Y[l] for l in range(6)),ZERO),"complete original mean top is exactly y-linear")
   tk.append(row)
  need(tk==[list(x) for x in zip(*tk)],"all original mean matrices symmetric")
  T.append(tk)
 need([int(mat(t).det()) for t in T]==[106,93,100,92],"same four original mean tensor determinants")
 Tinv,detT=inverse(mat(T[0]),"same original T1 coefficient unit")
 eta=[sum((W[i]*int(Tinv[i,j]) for i in range(6)),ZERO) for j in range(6)]
 r=[sum((eta[j]*H[j][a] for j in range(6)),ZERO) for a in range(10)]
 B=A[17]+ONE;need(r[6]==B,"whole original global-nine eliminated coefficient equals Bell")
 K=[0,1,2,3,4,5,7,8,9];c=[r[a] for a in K]
 srh=[sum((eta[j]*Hs[j][a] for j in range(6)),ZERO)-(MON[6] if a==17 else ZERO) for a in range(18)]
 need(MON[6]+dot([MON[a] for a in K],c)==dot(A,srh),"full original unit relation source, including Bell correction")
 return {"prime":P,"coefficientRoot":ROOT,"matchedCubic":MATCHED,"parameterNames":list(NEW_NAMES[:12]),"momentNames":list(NEW_NAMES[12:]),
  "tenOriginalMonomials":[list(x) for x in MEXP],"allOriginal18Generators":packvec(A),
  "allElevenMomentGenerators":packvec(G),"allElevenMomentGeneratorSources":[packvec(s) for s in Gsrc],
  "allFiveOriginalParameterMatrices":[[packvec(row) for row in Ni] for Ni in N],
  "allFiveOriginalBorderSourceMatrices":[[packvec(row) for row in Si] for Si in SS],
  "allSixOriginalMeanColumns":[packvec(v) for v in H],"allSixOriginalMeanSources":[packvec(s) for s in Hs],
  "quadraticUnit":tab(A2),"quadraticUnitInverse":tab(A2i),"quadraticUnitDeterminant127":det2,
  "all55OriginalCubicLabels":[list(z) for z in columns],"all35OriginalCubicMonomials":[list(x) for x in M3],
  "selectedOriginalCubicColumns":piv,"cubicUnit":tab(Cunit),"cubicUnitInverse":tab(Ci),"cubicUnitDeterminant127":det3,
  "all50OriginalBorderSourceProductsVerified":True,"allElevenOriginalGeneratorsInBorderSubmoduleVerified":True,
  "allSixCompleteOriginalMeanSourceProductsVerified":True,"allNineLiteralCyclicPathsRetained":True,
  "allFourOriginalMeanMatrices":T,"sameOriginalMeanDeterminants127":[106,93,100,92],
  "globalNineSourceRecipe":{"retainedTenAxes":K,"deletedTenAxis":6,"c":packvec(c),"eta":packvec(eta),
   "r_hSource":packvec(srh),"allOriginalUnitRelationProductsVerified":True,
   "matrix":"N_i=P*Nold_i*iota, P(e6)=-c",
   "extraParameterColumn":"-N_i*c-P*Nold_i*e6",
   "borderSource":"oldSource-oldDeletedCoordinate*r_hSource",
   "allParameterCoordinatesRetained":True,"newNineHighParameterProductsExpanded":False},
  "sourceCoordinateChange":chart["originalGradientTransport"],"coordinateInverse":chart["coordinateInverse"],
  "coordinateForwardOriginalContext":chart["coordinateForwardOriginalContext"],
  "allSourceRecurrencesUseOriginal18Generators":True,"characteristicZeroUnitIdealClaimed":False}

def decode_base(base):
 A=unpackvec(base["allOriginal18Generators"])
 N=[[[unpack(p) for p in row] for row in Ni] for Ni in base["allFiveOriginalParameterMatrices"]]
 SS=[[[unpack(p) for p in row] for row in Si] for Si in base["allFiveOriginalBorderSourceMatrices"]]
 H=[unpackvec(v) for v in base["allSixOriginalMeanColumns"]]
 Hs=[unpackvec(v) for v in base["allSixOriginalMeanSources"]]
 return A,N,SS,H,Hs

def prepare_seed(decoded,index):
 A,N,SS,H,Hs=decoded
 if index<100:
  pairs=list(itertools.combinations(range(5),2));i,j=pairs[index//10];a=index%10
  vi=[N[i][k][a] for k in range(10)];vj=[N[j][k][a] for k in range(10)]
  v=subv(mv(N[i],vj),mv(N[j],vi))
  s=addv(subv(scale([SS[i][k][a] for k in range(18)],U[j]),
               scale([SS[j][k][a] for k in range(18)],U[i])),
         subv(mv(SS[j],vi),mv(SS[i],vj)))
  label={"kind":"complete-original-commutator","left":i,"right":j,"tenAxis":a}
 elif index<106:
  j=index-100;v=H[j];s=Hs[j];label={"kind":"complete-original-mean","index":j}
 else:
  a=index-106;need(0<=a<10,"all ten original Bell axes")
  v=scale(unit(10,a),A[17]);s=scale(unit(18,17),MON[a]);label={"kind":"original-Bell-minus-one","tenAxis":a}
 need(len(v)==10 and len(s)==18 and all(not any(e[12:]) for x in v for e in x.to_dict()),"every seed is a complete ten-row parameter vector")
 need(dot(MON,v)==dot(A,s),"entire original18 source product for seed "+str(index))
 return {"seedIndex":index,"label":label,"vector":packvec(v),"original18Source":packvec(s),
  "allTenParameterCoordinatesRetained":True,"fullOriginal18ProductVerified":True,
  "allVariablesRetained":True,"nonzero":any(x!=0 for x in v),
  "vectorTermCount":sum(len(x.to_dict()) for x in v),"sourceTermCount":sum(len(x.to_dict()) for x in s)}

def main():
 ap=argparse.ArgumentParser()
 for name in ("model-driver","helper","out"):ap.add_argument("--"+name,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=180)
 ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--through",choices=("base","seeds"),default="seeds")
 a=ap.parse_args();need(0<a.seconds<=900 and 512<=a.memory_mib<=4096,"bounded original parameter model")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 a.out.mkdir(parents=True,exist_ok=True);started=time.monotonic()
 own=identity(Path(__file__))
 semantic={"format":FORMAT,"source":own,"modelSHA256":MODEL_SHA,"helperSHA256":HELPER_SHA,"prime":P,"coefficientRoot":ROOT,
  "originalHankelPivotOrder":HP,"originalHankelFreeOrder":HU,"keptQuadraticPairs":KEEP,
  "seedDictionary":"100commutator+6mean+10Bell","noMeanOrMomentParameterSpecialized":True}
 binding=sha(canon(semantic));mp=a.out/"original-parameter-module-manifest.json"
 manifest={"format":FORMAT+"-manifest","binding":binding,"semantic":semantic,"phases":{},"seeds":[]}
 if mp.exists():
  manifest=json.loads(mp.read_bytes());need(manifest["format"]==FORMAT+"-manifest" and manifest["binding"]==binding and manifest["semantic"]==semantic,"same original whole-phase continuation")
 rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,"through":a.through,
  "prime":P,"coefficientRoot":ROOT,"noCharacteristicZeroMembershipConclusion":True,"sameOriginal17GradientsRetained":True}}
 def event(name):
  rec["parameters"]["lastWholePhase"]=name
  print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-started,"peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
 def phase(name,build):
  if name in manifest["phases"]:
   data=load_gz(a.out/manifest["phases"][name]["path"],manifest["phases"][name],binding);event("reused-"+name);return data
  data=build();desc=save_gz(a.out/(name+".json.gz"),data,binding)
  manifest["phases"][name]=desc;save_json(mp,manifest);event(name);return data
 def timeout(sig,frame):raise TimeoutError("complete original parameter-module whole-phase budget")
 signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
 try:
  fd=module(a.model_driver,MODEL_SHA,"paid_original_parameter_field_driver")
  m=module(a.helper,HELPER_SHA,"paid_original_parameter_physical_helper")
  chart=phase("complete-original-global-chart127",lambda:original_chart(fd,m)[1])
  base=phase("complete-original-ten-parameter-action127",lambda:build_base(chart))
  rec["parameters"].update({"all34CoordinateInverseProducts":True,"all578JacobianProducts":True,"all17GradientTransportProducts":True,
   "all50OriginalBorderProducts":True,"all11OriginalGeneratorsInBorderSubmodule":True,"allSixMeanProducts":True,
   "originalCubicUnitDeterminant127":base["cubicUnitDeterminant127"],"globalNineSourceRecipeRetained":True})
  if a.through=="seeds":
   decoded=decode_base(base)
   for i in range(116):
    if i<len(manifest["seeds"]):
     d=manifest["seeds"][i];z=load_gz(a.out/d["path"],d,binding)
     need(z["seedIndex"]==i and z["fullOriginal18ProductVerified"],"same completed literal seed")
    else:
     need(i==len(manifest["seeds"]),"sequential complete original seed prefix")
     z=prepare_seed(decoded,i);d=save_gz(a.out/("complete-original-parameter-seed-%03d.json.gz"%i),z,binding)
     manifest["seeds"].append(d);save_json(mp,manifest);event("seed-%03d"%i)
   rec["parameters"].update({"all116OriginalSeedsVerified":True,"allOriginalParameterRows":10,"allOriginalSourceRows":18,
    "completeSeedCount":len(manifest["seeds"]),"stableClosureComputed":False,"newUnitIdealClaimed":False})
  rec["status"]="completed" if a.through=="seeds" else "completed-prefix";code=0
 except BaseException as e:
  rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed"
  rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75 if isinstance(e,TimeoutError) else 1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-started
  rec["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  rec["parameters"]["completeSeedPrefix"]=len(manifest["seeds"])
  if mp.exists():rec["parameters"]["manifest"]=identity(mp)
  rec["parameters"]["wholePhaseDescriptors"]=manifest["phases"]
  rec["parameters"]["wholeSeedDescriptors"]=manifest["seeds"]
  save_json(a.out/"original-parameter-module-receipt.json",rec)
  print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
 return code
if __name__=="__main__":sys.exit(main())
