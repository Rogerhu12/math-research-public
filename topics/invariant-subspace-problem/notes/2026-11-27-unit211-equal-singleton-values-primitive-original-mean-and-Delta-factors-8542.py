#!/usr/bin/env python3
"""New exact Delta factor strata and primitive original means on h=k!=1.
Reuse only the already published moment parameterization. Retain D=0.
Reuse the original cleared input only to factor the actual Delta relation
and the first three original mean numerators. All factor zero fibers retained.
Corrected original scale H=b*c*Delta clears the physical c weight.
No norm, D, Pf or S inverse. 180 seconds / 4 GiB.
"""
import os,json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
hp=Path(os.environ.get("ISP_RANK_ONE_GRAM_HELPER",
 str(Path(__file__).with_name("2026-11-27-unit211-rank-one-centered-value-original-gram-helper-8542.py"))))
hs=hp.read_text()
assert hashlib.sha256(hs.encode()).hexdigest()=="41459fea3ff0419d8c9230a2f6093cc0b1bc5f528b6f2d2e714a4469f11e5c3e"
exec(compile(hs,str(hp),"exec"),globals())
ctx=fmpq_mpoly_ctx.get(("b","lam","rho","f","t"),"lex")
bp,Lp,rp,fp,tp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
def poly(x):return x if hasattr(x,'to_dict') else ctx.constant(x)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oneP if d is None else poly(d);assert d
  if not n:self.n=zeroP;self.d=oneP;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);assert o;return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):
  return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):
  o=R(o)
  if self.n==o.n and self.d==o.d:return True
  return self.n*o.d==o.n*self.d

b,lam,rho,f,t=map(R,(bp,Lp,rp,fp,tp))
A=2*lam*lam-2*lam+1
B=4*lam**3-6*lam*lam+3*lam-1
xi=B/A;ell=A**3/(B*B);c=ell-b;a=1-ell
p,q=1+rho,1-rho;Q=p*q
u=p*b+q*c
T=A*A/B
w=lam-1-T
h=k=1+xi
S=2*xi+3-2*lam
eta=xi+3-2*lam
V2=2*u-ell*Q
T0=V2-2*u*u
J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q
P02=(2-3*u)*V2-Q*u+2*u**3
Pf=T0*(J-Q)
G=lam*P02-(1-u)*T0
Pc=Q*P02*(ell+T)-G*T0
NF=(3-4*lam)*Q+J*xi*eta
NT=b*c*Q*S*xi
NC=eta*(-G*xi+Q*w*u)
Delta=Phi*NF-S*xi*Pf
v=dict(a=a,b=b,c=c,ell=ell,lam=lam,rho=rho,p=p,q=q,Q=Q,u=u,
       A2=A,B3=B,xi=xi,T=T,w=w,h=h,k=k,S=S,zeta=xi,v0=xi,v1=R(0),
       V2=V2,T0=T0,J=J,Phi=Phi,P02=P02,Pf=Pf,G=G,Pc=Pc,
       NF=NF,NT=NT,NC=NC,determinant=Delta)
assert u==2*rho*b+q*ell
assert ell*xi*xi==A and ell*xi**3==B
assert a+w+b*h+c*k==lam
assert a+2*w+b*h*h+c*k*k==2*lam*lam
assert a+3*w+b*h**3+c*k**3==4*lam**3
assert S==(2*lam-1)*(2*lam*lam-1)/A
assert ell*A-T*T==0
units=[("A2",A.n),("B3",B.n),("rho",rp),("p",p.n),("q",q.n)]
den_cache=set()
def audit_base_den(pp):
 assert pp
 key=str(pp)
 if key in den_cache:return
 rr=pp
 for name,atom in units:
  while True:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   qq=rr/gg;assert qq*gg==rr
   rr=qq
 assert rr.total_degree()==0,("unpaid base inverse",str(rr))
 den_cache.add(key)
def profile(pp):
 txt=str(pp).encode()
 return dict(degrees_b_lambda_rho_f_t=list(map(int,pp.degrees())),
             terms=len(pp.to_dict()),totalDegree=int(pp.total_degree()),
             bytes=len(txt),sha256=hashlib.sha256(txt).hexdigest())
def base_profile(rr):
 rr=R(rr);audit_base_den(rr.d)
 return dict(numerator=profile(rr.n),denominator=profile(rr.d))
def extract_b(rr,degree):
 rr=R(rr)
 assert all(mm[0]==0 and mm[3]==0 and mm[4]==0 for mm in rr.d.to_dict())
 audit_base_den(rr.d)
 aa=[zeroP]*(degree+1)
 for mm,cf in rr.n.to_dict().items():
  assert mm[0]<=degree
  nn=list(mm);nn[0]=0
  aa[int(mm[0])]=aa[int(mm[0])]+ctx.from_dict({tuple(nn):cf})
 cc=[R(pp,rr.d) for pp in aa]
 assert sum((z*b**j for j,z in enumerate(cc)),R())==rr
 return cc
dc=extract_b(Delta,4)
assert dc[4]==-64*xi*xi*rho**4
rel=[z/dc[4] for z in dc[:4]]
for z in rel:
 assert all(mm[0]==0 and mm[3]==0 and mm[4]==0 for mm in z.n.to_dict())
 audit_base_den(z.d)
assert b**4+sum((z*b**j for j,z in enumerate(rel)),R())==Delta/dc[4]
say("new_equal_singleton_collision_monic_b_quartic",
    scope="whole h=k!=1 collision; D=0 retained",
    oldMomentChartOnlyReused=True,baseParameters=["lambda","rho"],
    determinant="Phi*NF-S*xi*Pf",
    leading="-64*xi^2*rho^4",
    allFiveDeterminantCoefficientsVerified=True,
    completeMonicCoefficients=[base_profile(z) for z in rel],
    noSOrPfOrDInverse=True,allLeadingZeroFibersPaidByOriginalA_B_rho=True,
    claimExcluded=False)
raw=original_rank_one_gram(v,f,t,1/b)
V=[1,w,h,k]
assert raw["tau"](V)==lam
nraw=raw["N4"](V)
assert Q*nraw/2==NF*f+NT*t+NC
say("new_equal_singleton_actual_N4_line",
    sameOriginalGram=True,actualValues=["1","w","h","h"],
    originalPhysicalDZero=True,rawN4Identity="Q*N4(V)/2=NF*f+bcQ*S*xi*t+NC",
    noCoefficientVanishingInference=True,claimExcluded=False)
f0=c*(S*xi*Pc-Phi*NC)
t0=(Pf*NC-Pc*NF)/Q
weight_den=c*Delta
assert Pf*f0+c*Q*Phi*t0+Pc*weight_den==0
assert NF*f0+c*Q*S*xi*t0+NC*weight_den==0
for z in [f0,t0,weight_den]:audit_base_den(z.d)
say("new_equal_singleton_Delta_nonzero_original_lines",
    originalF="f0/(c*Delta)",originalT="t0/(b*c*Delta)",
    exactP1Line=True,exactNVLine=True,originalUnitScale="H=b*c*Delta",
    noPfOrSInverse=True,wholeDeltaZeroRetainedByMonicQuartic=True,
    fnum=base_profile(f0),tnum=base_profile(t0),
    claimExcluded=False)

def original_equal_singleton_cleared_gram(v,fnum,tnum,weight_den):
    """Use f=fnum/weight_den, t=tnum/(b*weight_den), H=b*weight_den.

    The caller proves H!=0 from the original chart.  No H, b, or weight_den
    inverse is taken by this builder.  Every displayed row is H times the
    ORIGINAL Gram row.  Means are H^2 times original means; N/P rows H^3.
    """
    a,b,c,p,q,Q,u=(v[k] for k in ("a","b","c","p","q","Q","u"))
    T0,P02,V2,lam=(v[k] for k in ("T0","P02","V2","lam"))
    H=b*weight_den
    W1P=T0*weight_den/2+2*u*fnum
    W2P=(u*T0+lam*P02)*weight_den+(V2+2*u*u)*fnum-c*Q*tnum
    X0=(q*W1P-W2P)*(1/(p*(q-p)))
    Y0=(W2P-p*W1P)*(1/(c*q*(q-p)))
    rg0=X0-a*p*H-c*tnum
    sg0=Y0-a*q*weight_den-tnum
    AA0=2*fnum-2*X0-2*c*Y0+2*c*tnum
    zero=H*0
    rows=[[zero,zero,p*H,q*H],[zero,b*AA0,rg0,b*sg0],
          [p*H,rg0,zero,tnum],[q*H,b*sg0,tnum,zero]]
    one=[1,0,1,1]
    def va(x,y):return [a+b for a,b in zip(x,y)]
    def vs(a,x):return [a*b for b in x]
    def vm(x,y):
        return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
    def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
    def DKnum(x):return [tau(vm(row,x)) for row in rows]
    dN=DKnum(one);F2N=tau(dN)
    assert F2N==2*b*fnum
    def N4num(x):
        tv=tau(x)
        return (2*tau(vm(dN,vm(x,x)))-F2N*tau(vm(x,x))
                -4*tv*tau(vm(dN,x))+2*F2N*tv**2+tau(vm(x,DKnum(x))))
    def P2(x):
        centered=va(x,vs(-tau(x),one))
        return tau(vm(vm(centered,centered),centered))
    H3=H**3
    x,y=rows[0],rows[1]
    xc=va(x,vs(-tau(x),one));yc=va(y,vs(-tau(y),one))
    Pj=3*tau(vm(vm(xc,xc),yc))
    def equations():
        Kd=DKnum(dN)
        for j,name in ((1,"E1"),(2,"EB"),(3,"EC")):
            ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
            yield name,ee-2*Kd[j]-2*vm(dN,dN)[j]+2*F2N*dN[j]
        Nv=(4*tau(vm(dN,vm(x,y)))-2*F2N*tau(vm(x,y))
            -4*(tau(x)*tau(vm(dN,y))+tau(y)*tau(vm(dN,x)))
            +4*F2N*tau(x)*tau(y)+tau(vm(x,DKnum(y)))+tau(vm(y,DKnum(x))))
        yield "N1",Nv-(4*lam/3)*Pj
        yield "NB",N4num(rows[2])-2*lam*P02*v["h"]**2*H3
        yield "PB",P2(rows[2])-P02*v["h"]**3*H3
        yield "NC",N4num(rows[3])-2*lam*P02*v["k"]**2*H3
        yield "PC",P2(rows[3])-P02*v["k"]**3*H3
    return dict(rows=rows,one=one,dN=dN,F2N=F2N,H=H,tau=tau,DKnum=DKnum,
                N4num=N4num,P2=P2,Pj=Pj,
                P1Residual=Pj-3*v["w"]*P02*H3,
                equations=equations,originalValues=[1,v["w"],v["h"],v["k"]])


gram=original_equal_singleton_cleared_gram(v,f0,t0,weight_den)
assert gram["P1Residual"]==0
assert gram["originalValues"]==V
assert gram["N4num"](V)==0
say("new_equal_singleton_same_original_cleared_Gram",
    originalP1Zero=True,originalNVZero=True,originalE0N0Restored=True,
    scale="H=b*c*Delta",bothSingletonTargets="NB,NC use h^2; PB,PC use h^3",
    weightDenominatorsOnly=True,noNormInverse=True,noDInverse=True,
    claimExcluded=False)

# P02 is twice the original nonzero highest value at the double-point base.
# b,c are the two original nonzero singleton weights. Delta is paid ONLY
# on the explicitly separated Delta!=0 chart. No T0/Pf/S/ell-u unit is used.
physical_atoms=units+[("lambda",Lp),("original_b",bp),
                      ("original_c",c.n),("original_P02",P02.n)]
def strip_actual(pp,atoms):
 original=pp;prod=oneP;history=[]
 if not pp:return pp,prod,history
 for name,atom in atoms:
  count=0
  while True:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   old=pp;pp=pp/gg;assert pp*gg==old
   prod=prod*gg;count+=1
  if count:history.append(dict(name=name,count=count))
 scalar=pp.coefficient(0)
 normalized=pp/scalar;assert normalized*scalar*prod==original
 return normalized,scalar*prod,history
def exact_factor(label,pp):
 if not pp:
  say("new_equal_singleton_exact_factor_zero",name=label,claimExcluded=False)
  return []
 content,factors=pp.factor();rebuilt=ctx.constant(content);items=[]
 for index,(factor,mult) in enumerate(factors):
  mult=int(mult);rebuilt=rebuilt*factor**mult
  rec=dict(index=index,multiplicity=mult,profile=profile(factor))
  ss=str(factor)
  if len(ss.encode())<=5000:rec["polynomial"]=ss
  items.append(rec)
 assert rebuilt==pp
 say("new_equal_singleton_full_QQ_factorization",name=label,
     original=profile(pp),rationalContent=str(content),factors=items,
     completeQQProductActuallyReturned=True,allUnpaidFactorZeroFibersRetained=True,
     noNormOrDUnitAdded=True,claimExcluded=False)
 return items
delta_core,delta_removed,delta_history=strip_actual(Delta.n,physical_atoms)
say("new_equal_singleton_complete_Delta_primitive_relation",
    actualOriginalDelta=True,necessaryNumerator=profile(delta_core),
    onlyOriginalPhysicalFactorsRemoved=delta_history,
    completeScaleProductVerified=True,claimExcluded=False)
delta_factors=exact_factor("whole_Delta_zero_original_relation",delta_core)
cores={};core_factors={}
for name,raw in gram["equations"]():
 if name not in ("E1","EB","EC"):break
 raw=R(raw);audit_base_den(raw.d)
 pp,removed,hist=strip_actual(raw.n,physical_atoms+[("chart_Delta_nonzero",Delta.n)])
 assert pp*removed==raw.n
 cores[name]=pp
 say("new_equal_singleton_Delta_nonzero_primitive_original_mean",
     name=name,originalNumerator=profile(raw.n),primitive=profile(pp),
     actualOriginalPaidFactorsRemoved=hist,wholeScaleProductVerified=True,
     allDeltaZeroFibersRetainedSeparatelyByCompleteMonicQuartic=True,
     noOtherWeightFaceDiscarded=True,claimExcluded=False)
 core_factors[name]=exact_factor(name,pp)
assert list(cores)==["E1","EB","EC"]
common=cores["E1"].gcd(cores["EB"]).gcd(cores["EC"])
say("new_equal_singleton_primitive_mean_common_factor",
    gcd=profile(common),
    role="structural factor only, NOT a necessary zero condition",
    noMultivariateGcdIdealInference=True,claimExcluded=False)
say("complete_equal_singleton_new_exact_factor_input",
    DeltaFactors=delta_factors,
    originalMeanCores={name:profile(pp) for name,pp in cores.items()},
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    allCompleteQQFactorProductsVerified=True,
    fullOriginalGramAndValueConditionsStillRetained=True,
    noT0PfSOrDInverse=True,ordinaryISPClaim=False,claimExcluded=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
