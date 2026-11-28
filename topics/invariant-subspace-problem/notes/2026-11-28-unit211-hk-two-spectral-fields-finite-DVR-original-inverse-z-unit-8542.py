#!/usr/bin/env python3
"""NEW h=k, Delta=0: one finite-DVR residue model for EACH whole F99/F300.
The already proved reduced base has u=eta_d and Q=theta_d in K_d.
Choose the FIRST admissible residue place by integrality / old units only.
Then, once per K_d, use the inverse-z MONIC CUBIC and the complete eight
correct original z rows. Only a full Bezout ONE can exclude that K_d.
No old QQ(K_d)[u] gcd, same-Q algebra, Gram matrix, or target is replayed.
Only exact existing P/M/F_d parameter-definition prefixes are regenerated.
180 seconds / 4 GiB, including definitions. No coefficient cache/payload.
"""
import contextlib,hashlib,io,json,math,resource,signal,time
from fractions import Fraction
from pathlib import Path
from flint import fmpq_poly
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
REAL_TIMER=signal.setitimer
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 180 second boundary')
def bounded_timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return REAL_TIMER(which,seconds,interval)
 tick();assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return REAL_TIMER(which,min(left,float(seconds) if seconds>0 else left),0.0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.setitimer=bounded_timer;signal.alarm=bounded_alarm
bounded_timer(signal.ITIMER_REAL,180)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(',',':')),flush=True)

# Exact parameter definition only. The marker precedes old K99 arithmetic.
NAME='2026-11-28-unit211-h-equals-k-corrected-Delta-zero-F99-original-fibers-8542.py'
path=Path(__file__).with_name(NAME);full=path.read_bytes()
assert hashlib.sha256(full).hexdigest()=='daa2c5331f45b5583c657cbfe407660552763b65a42abda7fa379ae6b92fa005'
marker=b'\nchoices=[f for f,e in fac if int(f.degree())==99]'
assert full.count(marker)==1
prefix=full.split(marker)[0]+b'\n'
assert len(prefix)==4728
assert hashlib.sha256(prefix).hexdigest()=='f3de7830b2ff98c6f4e7df0a891eb7fe2bff61c8ccf6ba6ae83134316ae82f59'
ns={'__name__':'new_DVR_only_existing_parameter_definitions','__file__':str(path)}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(path)+'#necessary_P_M_F_definitions_only','exec'),ns)
signal.setitimer=bounded_timer;signal.alarm=bounded_alarm
bounded_timer(signal.ITIMER_REAL,180)
orig=ns['orig'];pdata=ns['pdata'];mdata=ns['mdata']
specs=[
 (99,'e422b38e5f712eb9237d85ad116dfcdf8ec94f3886a7d97d210b48e3ce6a5a7e'),
 (300,'5bfbc9ddc3b558dbef77fc19cd495175a1c8ad16461e6166c44cb982a1dca7ea')]
exact_fields={}
for degree,sha in specs:
 candidates=[(f,int(e)) for f,e in ns['fac'] if int(f.degree())==degree]
 assert len(candidates)==1
 ff,multiplicity=candidates[0]
 assert multiplicity==1 and ns['fprofile'](ff)['sha256']==sha
 monic=ff/ff[degree];assert monic[degree]==1
 exact_fields[degree]=[Fraction(str(monic[j])) for j in range(degree+1)]
say('existing_two_whole_spectral_parameters_defined',
 F99_SHA256=specs[0][1],F300_SHA256=specs[1][1],
 exactFieldDegrees=[99,300],knownIrreducibilityAndMultiplicityOneUsed=True,
 necessaryPrefixBytes=len(prefix),
 necessaryPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
 noOldWholeFieldUGCDOrQGCDOrEightZGateExecuted=True,
 parameterRegenerationIsNotANewMathematicalConclusion=True,
 historicalPOnlyInRunnerTemporaryMemory=True)

# The fixed prime/point order is declared before ANY original z-row test.
# Selection NEVER looks at a z ideal rank, z gcd, or positive target.
PRIMES=(1009,1013,1019,1021,1031,1033,1039,1049,
        1051,1061,1063,1069,1087,1091,1093,1097)
assert all(p>3 and all(p%d for d in range(2,math.isqrt(p)+1)) for p in PRIMES)
MOD=1009
stats={'constantInverseProducts':0,'polynomialDivisionProducts':0,
       'completePairBezoutReturns':0,'goodPlaceScalarChecks':0,
       'originalGramReturns':0,'originalMomentReturns':0,
       'originalEightRows':0,'completeInverseZBezoutReturns':0}
class F:
 _level=0
 def __init__(self,v=0):
  if isinstance(v,F):self.v=v.v;return
  q=v if isinstance(v,Fraction) else Fraction(v)
  den=q.denominator%MOD
  assert den,'coefficient not integral at the selected prime'
  self.v=(q.numerator%MOD)*pow(den,MOD-2,MOD)%MOD
 def __bool__(self):return self.v!=0
 def __neg__(self):return F(-self.v)
 def __add__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return F(self.v+F(v).v)
 __radd__=__add__
 def __sub__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return self+-F(v)
 def __rsub__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return F(v)+-self
 def __mul__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return F(self.v*F(v).v)
 __rmul__=__mul__
 def inv(self):
  assert self
  a=F(pow(self.v,MOD-2,MOD))
  assert self.v*a.v%MOD==1
  stats['constantInverseProducts']+=1
  return a
 def __truediv__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return self*F(v).inv()
 def __rtruediv__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return F(v)*self.inv()
 def __pow__(self,n):
  n=int(n)
  return self.inv()**(-n) if n<0 else F(pow(self.v,n,MOD))
 def __eq__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return self.v==F(v).v
 def __int__(self):return self.v

def trim(v):
 v=list(v)
 while v and not v[-1]:v.pop()
 return v
class P:
 """Ordinary univariate polynomials over the current F_p; NO quotient."""
 _level=1
 def __init__(self,v=0):
  if isinstance(v,P):self.c=v.c[:];return
  self.c=trim([F(x) for x in v]) if isinstance(v,(list,tuple)) else ([F(v)] if F(v) else [])
 def __bool__(self):return bool(self.c)
 def degree(self):return len(self.c)-1
 def __getitem__(self,j):return self.c[j] if 0<=j<len(self.c) else F()
 def __neg__(self):return P([-x for x in self.c])
 def __add__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  v=P(v)
  return P([self[j]+v[j] for j in range(max(len(self.c),len(v.c)))])
 __radd__=__add__
 def __sub__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  return self+-P(v)
 def __rsub__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  return P(v)+-self
 def __mul__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  v=P(v)
  if not self or not v:return P()
  out=[F() for _ in range(len(self.c)+len(v.c)-1)]
  for i,x in enumerate(self.c):
   for j,y in enumerate(v.c):out[i+j]=out[i+j]+x*y
  return P(out)
 __rmul__=__mul__
 def __truediv__(self,v):
  assert getattr(v,'_level',0)==0
  iv=F(v).inv();return P([x*iv for x in self.c])
 def __pow__(self,n):
  n=int(n);assert n>=0
  out=P(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def __eq__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  v=P(v)
  return len(self.c)==len(v.c) and all(x==y for x,y in zip(self.c,v.c))
 def evaluate(self,x):
  x=F(x);out=F()
  for c in self.c[::-1]:out=out*x+c
  return out
 def derivative(self):return P([j*self[j] for j in range(1,len(self.c))])

def pdiv(a,b):
 tick();a=P(a);b=P(b);assert b
 old=P(a);qq=[F() for _ in range(max(0,len(a.c)-len(b.c)+1))]
 lead=b.c[-1].inv()
 while a and a.degree()>=b.degree():
  d=a.degree()-b.degree();c=a.c[-1]*lead;qq[d]=qq[d]+c
  cc=a.c[:]
  for j,y in enumerate(b.c):cc[d+j]=cc[d+j]-c*y
  a=P(cc)
 q=P(qq)
 assert q*b+a==old
 stats['polynomialDivisionProducts']+=1
 return q,a
def pxgcd(a,b):
 a=P(a);b=P(b);r0,r1=a,b;s0,s1=P(1),P();t0,t1=P(),P(1)
 while r1:
  q,r=pdiv(r0,r1)
  r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
 if not r0:return P(),P(),P()
 inv=r0.c[-1].inv();g=r0*inv;s=s0*inv;t=t0*inv
 assert s*a+t*b==g and g.c[-1]==1
 stats['completePairBezoutReturns']+=1
 return g,s,t
def pprofile(v):
 v=P(v);raw=json.dumps([int(c) for c in v.c],separators=(',',':')).encode()
 return {'degree':v.degree(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def eval_int_poly(cs,x,p):
 out=0
 for c in cs[::-1]:out=(out*x+c)%p
 return out

# Exact rational coefficient definitions. No historical payload is printed.
pdata=[(int(i),int(j),Fraction(c)) for i,j,c in pdata]
mdata=[(int(i),int(j),Fraction(c)) for i,j,c in mdata]
def exact_data(value):
 return [(tuple(map(int,m)),Fraction(str(c))) for m,c in value.to_dict().items()]
unit_names=['A','B','lam','u','Q','disc','Pf','bc','P02','S']
old_units={name:orig[name] for name in unit_names}
old_units['u_minus_one']=orig['u']-1
old_units['two_lambda_minus_one']=2*orig['lam']-1
old_units['M']=4*orig['bc']*orig['disc']
old_data={name:(exact_data(v.n),exact_data(v.d)) for name,v in old_units.items()}
delta_data=(exact_data(orig['Delta'].n),exact_data(orig['Delta'].d))
tnum_data=(exact_data(orig['Tnum'].n),exact_data(orig['Tnum'].d))
all_rational_coefficients=([c for _,_,c in pdata]+[c for _,_,c in mdata]
 +[c for cs in exact_fields.values() for c in cs]
 +[c for pair in list(old_data.values())+[delta_data,tnum_data]
   for data in pair for _,c in data])
def specialize_u(data,l):
 cc=[F() for _ in range(max(j for _,j,_ in data)+1)]
 powers=[F(1)]
 for i in range(max(i for i,_,_ in data)):powers.append(powers[-1]*l)
 for i,j,c in data:cc[j]=cc[j]+F(c)*powers[i]
 return P(cc)
def specialize_Q(data,l,u):
 n=max((m[2] for m,c in data),default=0)
 cc=[F() for _ in range(n+1)]
 for (i,j,k),c in data:cc[k]=cc[k]+F(c)*(l**i)*(u**j)
 return P(cc)
def scalar_value(data,l,u,q):
 out=F()
 for (i,j,k),c in data:out=out+F(c)*(l**i)*(u**j)*(q**k)
 return out

def choose_place(degree):
 """All decisions here precede construction/testing of the eight z rows."""
 global MOD
 counts={'primeCoefficientChecks':0,'simpleSpectrumCandidates':0,
         'uLinearCandidates':0,'QLinearCandidates':0,'oldUnitCandidates':0}
 other=300 if degree==99 else 99
 for p in PRIMES:
  tick();MOD=p
  if any(c.denominator%p==0 for c in all_rational_coefficients):continue
  counts['primeCoefficientChecks']+=1
  fc=[int(F(c)) for c in exact_fields[degree]]
  oc=[int(F(c)) for c in exact_fields[other]]
  df=[j*fc[j]%p for j in range(1,len(fc))]
  assert len(fc)==degree+1 and fc[-1]==1
  for lv in range(p):
   if eval_int_poly(fc,lv,p) or not eval_int_poly(df,lv,p):continue
   if not eval_int_poly(oc,lv,p):continue
   counts['simpleSpectrumCandidates']+=1
   l=F(lv);pp=specialize_u(pdata,l);mm=specialize_u(mdata,l)
   if pp.degree()!=3:continue
   ug,utagP,utagM=pxgcd(pp,mm)
   if ug.degree()!=1:continue
   u=-ug[0];assert ug[1]==1 and not pp.evaluate(u) and not mm.evaluate(u)
   if not u or u==1:continue
   counts['uLinearCandidates']+=1
   dn=specialize_Q(delta_data[0],l,u);dd=specialize_Q(delta_data[1],l,u)
   tn=specialize_Q(tnum_data[0],l,u);td=specialize_Q(tnum_data[1],l,u)
   # These exact denominators are Q-independent by their original definitions.
   assert dd.degree()<=0 and td.degree()<=0
   if not dd or not td or dn.degree()!=2:continue
   qg,qtagD,qtagN=pxgcd(dn,tn)
   if qg.degree()!=1:continue
   q=-qg[0];assert qg[1]==1 and not dn.evaluate(q) and not tn.evaluate(q)
   counts['QLinearCandidates']+=1
   vals={};ok=True
   for name,(num,den) in old_data.items():
    n=scalar_value(num,l,u,q);d=scalar_value(den,l,u,q)
    if not n or not d:ok=False;break
    vals[name]=int(n/d)
   if not ok:continue
   counts['oldUnitCandidates']+=1
   c0=-2*F(vals['P02'])*l*l*(2*l-1)**2/F(vals['B'])
   if not c0:continue
   stats['goodPlaceScalarChecks']+=len(vals)+8
   return dict(fieldDegree=degree,prime=p,lambdaResidue=lv,
               uResidue=int(u),QResidue=int(q),LowwConstantResidue=int(c0),
               originalUnitResidues=vals,
               PLeadingResidue=int(pp[3]),DeltaLeadingNumeratorResidue=int(dn[2]),
               selectionCounts=counts,
               uBezoutProfiles=[pprofile(utagP),pprofile(utagM)],
               QBezoutProfiles=[pprofile(qtagD),pprofile(qtagN)],
               checkedRationalCoefficientCount=len(all_rational_coefficients),
               firstAdmissiblePlaceChosenBeforeAnyOriginalZTest=True)
 return dict(fieldDegree=degree,selected=False,selectionCounts=counts,
             reason='no admissible finite-DVR model in the fixed prime/point list',
             entireFieldRetained=True)

class E:
 """The complete rho^2=DELTA algebra over ordinary F_p[z]."""
 _level=2
 def __init__(self,e=0,o=0):
  if isinstance(e,E):self.e=e.e;self.o=e.o;return
  self.e=P(e);self.o=P(o)
 def __bool__(self):return bool(self.e) or bool(self.o)
 def __neg__(self):return E(-self.e,-self.o)
 def __add__(self,v):v=E(v);return E(self.e+v.e,self.o+v.o)
 __radd__=__add__
 def __sub__(self,v):return self+-E(v)
 def __rsub__(self,v):return E(v)+-self
 def __mul__(self,v):
  v=E(v);return E(self.e*v.e+DELTA*self.o*v.o,self.e*v.o+self.o*v.e)
 __rmul__=__mul__
 def __truediv__(self,v):
  assert getattr(v,'_level',0)==0
  return E(self.e/v,self.o/v)
 def __pow__(self,n):
  n=int(n);assert n>=0
  out=E(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def conj(self):return E(self.e,-self.o)
 def __eq__(self,v):
  v=E(v);return self.e==v.e and self.o==v.o

def original_eight(place):
 """NEW only at the already selected place. All expressions lift over its DVR."""
 global DELTA
 l=F(place['lambdaResidue']);u=F(place['uResidue']);Q=F(place['QResidue'])
 delta=1-Q;DELTA=delta
 A=2*l*l-2*l+1;B=4*l**3-6*l*l+3*l-1
 xi=B/A;ell=A**3/(B*B);T=A*A/B;w=l-1-T;h=1+xi
 m=u-ell;aa=1-ell;bc=(ell*ell-m*m/delta)/4;M=4*bc*delta
 V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
 Phi=T0+4*u-4+Q;P02=(2-3*u)*V2-Q*u+2*u**3
 Pf=T0*(J-Q);G=l*P02-(1-u)*T0;Pc=Q*P02*(ell+T)-G*T0
 for name,value in [('A',A),('B',B),('lam',l),('u',u),('Q',Q),('disc',delta),
                    ('Pf',Pf),('bc',bc),('P02',P02),('M',M)]:
  assert int(value)==place['originalUnitResidues'][name]
  stats['originalGramReturns']+=1
 z=P([0,1]);t=z/Q
 f=-(P(Pc)+bc*Phi*z)/Pf
 V=(J*f-G+bc*z)/Q;W1=T0/2+2*u*f
 x=((u-ell*Q)*V-m*W1)/M;y=(ell*W1-u*V)/M
 A1=2*f-2*V+2*bc*t
 rho=E(0,1);b=E(ell/2,m/(2*delta));c=b.conj()
 p=1+rho;qc=1-rho;X=E(x,y);Y=X.conj()
 r=X-aa*p-c*t;s=Y-aa*qc-b*t
 rows=[[E(),E(),p,qc],[E(),E(A1),r,s],
       [p,r,E(),E(t)],[qc,s,E(t),E()]]
 one=[E(1),E(),E(1),E(1)]
 def vm(vv,ww):
  return [vv[0]*ww[0],vv[0]*ww[1]+vv[1]*ww[0],
          vv[2]*ww[2],vv[3]*ww[3]]
 def tau(vv):return aa*vv[0]+vv[1]+b*vv[2]+c*vv[3]
 def DK(vv):return [tau(vm(row,vv)) for row in rows]
 d=DK(one);F2=tau(d);Kd=DK(d)
 assert d[0]==u and d[2]==X and d[3]==Y and F2==2*f
 assert b*c==bc and b+c==ell and b*p+c*qc==u and p*qc==Q
 assert aa+w+ell*h==l and aa+2*w+ell*h*h==2*l*l
 assert aa+3*w+ell*h**3==4*l**3
 stats['originalGramReturns']+=11
 def N4(vv):
  vv2=vm(vv,vv);tv=tau(vv)
  return (2*tau(vm(d,vv2))-F2*tau(vv2)
          -4*tv*tau(vm(d,vv))+2*F2*tv*tv+tau(vm(vv,DK(vv))))
 def center(vv):
  tv=tau(vv);return [v-tv*e for v,e in zip(vv,one)]
 def P2(vv):
  vc=center(vv);return tau(vm(vm(vc,vc),vc))
 g0,g1,gB,gC=rows
 N0=N4(g0);Nrow1=N4(g1)
 NJ=N4([x+y for x,y in zip(g0,g1)])-N0-Nrow1
 c0=center(g0);c1=center(g1);PJ=3*tau(vm(vm(c0,c0),c1))
 assert P2(g0)==P02 and N0==2*l*P02 and PJ==3*w*P02
 VV=[E(1),E(w),E(h),E(h)]
 assert N4(VV)==0
 stats['originalMomentReturns']+=4
 e0=tau(vm(g0,g0))-2*Kd[0]-2*d[0]*d[0]+2*F2*d[0]
 assert not e0
 stats['originalMomentReturns']+=1
 e1=2*tau(vm(g0,g1))-2*Kd[1]-2*vm(d,d)[1]+2*F2*d[1]
 eb=tau(vm(gB,gB))-2*Kd[2]-2*d[2]*d[2]+2*F2*d[2]
 ec=tau(vm(gC,gC))-2*Kd[3]-2*d[3]*d[3]+2*F2*d[3]
 n1=NJ-4*l*w*P02;nb=N4(gB)-2*l*h*h*P02;pb=P2(gB)-h**3*P02
 assert not e1.o and not n1.o and ec==eb.conj()
 assert N4(gC)-2*l*h*h*P02==nb.conj()
 assert P2(gC)-h**3*P02==pb.conj()
 stats['originalGramReturns']+=5
 names=['E1even','EBe','EBo','N1jet','NB_even','NB_odd','PB_even','PB_odd']
 values=[e1.e,eb.e,eb.o,n1.e,nb.e,nb.o,pb.e,pb.o]
 capacities=[2,2,2,2,3,3,3,3]
 assert all(value.degree()<=cap for value,cap in zip(values,capacities))
 stats['originalEightRows']+=8

 # Same original Loww, including the full free-f correction.
 # This is an exact old original identity, now checked at the selected place.
 EW2=(2*u-u*ell-V)*eb.e+(2*(u-ell*Q)-u*m-m*x-ell*delta*y)*eb.o
 NS=ell*nb.e+m*nb.o;PS=ell*pb.e+m*pb.o
 Loww=NS-PS+EW2
 Kw=2*(t*t+(5*u-4*x-2)*t+2*(x*x-delta*y*y)
       +4*x+4*delta*y-4*u*x+2*u*u-6*u+Q)
 expected=2*P02*(2*l-1)*w-bc*t*(Kw+4*(f-u)*(t-2))
 assert Loww==expected and Loww.degree()<=3
 c0=-2*P02*l*l*(2*l-1)**2/B
 assert Loww[0]==c0 and int(c0)==place['LowwConstantResidue'] and c0
 stats['originalMomentReturns']+=2
 # q(zeta) is a FIXED monic cubic even if Loww's z-leading term drops.
 qzeta=P([Loww[3],Loww[2],Loww[1],Loww[0]])/c0
 assert qzeta.degree()==3 and qzeta[3]==1
 reversed_values=[P([v[cap-j] for j in range(cap+1)])
                  for v,cap in zip(values,capacities)]
 say('new_selected_DVR_complete_original_inverse_z_model',
     fieldDegree=place['fieldDegree'],prime=MOD,
     originalRows=[{'name':n,'zDegree':v.degree(),'fixedReverseCapacity':cap,
                    'profile':pprofile(v)}
                   for n,v,cap in zip(names,values,capacities)],
     Loww=pprofile(Loww),monicInverseZCubic=pprofile(qzeta),
     finiteFreeRankOverDVR=3,allOriginalCoefficientsRegularByCheckedUnits=True,
     completeTrueDualProductUsed=True,
     originalLowwFromWeightedNPAndTwoMeansReturned=True,
     noZLeadingCoefficientOrPhysicalDInverted=True,
     rhoAlgebraBothOrderedSignsRetained=True)
 return names,qzeta,reversed_values

results=[]
for degree,sha in specs:
 tick();place=choose_place(degree)
 if 'prime' not in place:
  say('new_whole_field_DVR_model_unavailable',**place)
  results.append(place);continue
 say('new_first_admissible_DVR_place_fixed',**place,
     selectionUsesNoOriginalZIdealTest=True,
     knownWholeFieldUniqueUAndQUsed=True,
     integrallyClosedDVRMakesUAndQIntegral=True)
 names,qzeta,rows=original_eight(place)
 generators=[qzeta]+rows
 g=qzeta;tags=[P(1)]+[P() for _ in rows];steps=[]
 for i,row in enumerate(rows,1):
  gg,a,b=pxgcd(g,row)
  tags=[a*v for v in tags];tags[i]=tags[i]+b;g=gg
  assert sum((tag*value for tag,value in zip(tags,generators)),P())==g
  steps.append({'name':names[i-1],'commonDegree':g.degree()})
  if g==1:break
 returned=sum((tag*value for tag,value in zip(tags,generators)),P())
 assert returned==g
 unit=g==1
 if unit:stats['completeInverseZBezoutReturns']+=1
 certificate={'prime':MOD,'generators':[[int(c) for c in v.c] for v in generators],
              'multipliers':[[int(c) for c in v.c] for v in tags],
              'target':[int(c) for c in g.c]}
 encoded=json.dumps(certificate,separators=(',',':')).encode()
 result=dict(fieldDegree=degree,prime=MOD,
             lambdaResidue=place['lambdaResidue'],uResidue=place['uResidue'],
             QResidue=place['QResidue'],finiteFreeDVRRank=3,
             completeOrdinaryInverseZBezoutOne=unit,
             entireQQSpectrumFieldExcluded=unit,allComplexEmbeddingsCovered=unit,
             actualGCD=pprofile(g),steps=steps,
             exactReturnedCertificateBytes=len(encoded),
             exactReturnedCertificateSHA256=hashlib.sha256(encoded).hexdigest(),
             completeNineSourceReturn=True,
             noPositiveZOrDTargetUsed=True,noPlaceRetriedAfterOriginalTest=True,
             allUnexcludedWholeFieldsRetained=not unit)
 say('new_whole_spectrum_DVR_original_unit_result',**result)
 results.append(result)
 del encoded,certificate,tags,generators,rows
say('new_two_whole_spectral_DVR_first_input_finished',
 results=results,
 bothWholeFieldsExcluded=all(r.get('entireQQSpectrumFieldExcluded',False) for r in results),
 lifting='finite free DVR cubic / finite cokernel / Nakayama / fraction field',
 noBareFiniteFieldEmptinessOrDNilpotenceLift=True,
 noOldWholeFieldUGCDQGCDOrFrozenEightZTargetReplayed=True,
 noWholeCollisionDeltaNonzeroOrOrdinaryISPClaim=True,
 noCoefficientPayloadCacheOrChunksSaved=True,
 statistics=stats,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
REAL_TIMER(signal.ITIMER_REAL,0)
