#!/usr/bin/env python3
"""NEW corrected h=k, Delta=0: the entire existing F99 constant fiber.
Only the exact old P/M/F99 parameter definitions are regenerated.
No old fixed-17 Bareiss, P/M gcd, 722 proof, or frozen Gram matrix runs.
NEW: whole K99[u] gcd; same-Q Delta/Tnum/true-RWO gcd; only paid
primary removal; for Q degree <=2, full same-z original eight values.
Every leading nonunit retains the whole factor. Never invert physical D.
Total 180 seconds /4 GiB, including both definition prefixes.
"""
import base64,contextlib,hashlib,io,json,math,resource,signal,time,zlib
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
REAL_TIMER=signal.setitimer;REAL_ALARM=signal.alarm
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 180 second boundary')
def bounded_timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return REAL_TIMER(which,seconds,interval)
 tick();assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return REAL_TIMER(which,min(left,float(seconds) if seconds>0 else left),0.0)
def bounded_alarm(seconds):
 return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.setitimer=bounded_timer;signal.alarm=bounded_alarm
bounded_timer(signal.ITIMER_REAL,180)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(',',':')),flush=True)

# These are coefficient definitions, not a repetition of their proof gates.
NAME='2026-11-28-unit211-h-equals-k-corrected-Delta-zero-RWO-Q-projection-8542.py'
path=Path(__file__).with_name(NAME);full=path.read_bytes()
assert hashlib.sha256(full).hexdigest()=='3fcc2e90677b7bbd0247d72c1922fc6ed0b60da4ced715a7cecbeae656aade33'
mark=b'\n # Reuse only the independent, already executed D/T curve P.'
assert full.count(mark)==1
prefix=full.split(mark)[0]
assert len(prefix)==6055 and hashlib.sha256(prefix).hexdigest()=='09e0b44a9b6f244d0e2a11c1361b5382219aa5cad609efc3ae08fd370d318c7b'
ns={'__name__':'new_F99_necessary_parameter_definitions','__file__':str(path)}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(path)+'#only_known_parameter_definitions','exec'),ns)
signal.setitimer=bounded_timer;signal.alarm=bounded_alarm
bounded_timer(signal.ITIMER_REAL,180)
orig=ns['ns'];ctx=ns['ctx'];Ftrue=ns['F']
assert ns['profile'](Ftrue)['sha256']=='69babd37fc45ade649b12b4b849151574080a2bf92c7c2266141d17be1a9d999'
mdata=[[int(m[0]),int(m[1]),str(c)] for m,c in sorted(ns['newM'].to_dict().items())]
assert all(int(m[2])==0 for m in ns['newM'].to_dict())
mraw=json.dumps(mdata,separators=(',',':')).encode()
assert hashlib.sha256(mraw).hexdigest()=='65d420e901bd60b711d76ad23699daab655414b0595383a19a93d13180f30663'
legacy=Path(__file__).with_name('isp-hk-independent-Delta-Tnum-legacy.json')
doc=json.loads(legacy.read_text())
def walk(obj):
 if isinstance(obj,dict):
  yield obj
  for v in obj.values():yield from walk(v)
 elif isinstance(obj,list):
  for v in obj:yield from walk(v)
matches=[r for r in walk(doc)
 if r.get('sha256')=='8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c'
 and r.get('encoding')=='base64+zlib+json-lambda-u-coeff' and 'data' in r]
assert matches
pdata=json.loads(zlib.decompress(base64.b64decode(matches[0]['data'])))
praw=json.dumps(pdata,separators=(',',':')).encode()
assert hashlib.sha256(praw).hexdigest()=='8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c'
del doc,matches,mraw,praw
bctx=fmpq_mpoly_ctx.get(('lam','u'),'lex')
pp=bctx.from_dict({(int(i),int(j)):fmpq(c) for i,j,c in pdata})
mm=bctx.from_dict({(int(i),int(j)):fmpq(c) for i,j,c in mdata})
assert list(map(int,pp.degrees()))==[28,3]
assert list(map(int,mm.degrees()))==[110,14]
def fprofile(p):
 data=[str(p[i]) for i in range(int(p.degree())+1)] if p else []
 raw=json.dumps(data,separators=(',',':')).encode()
 return dict(degree=int(p.degree()) if p else -1,bytes=len(raw),
             sha256=hashlib.sha256(raw).hexdigest())
# Direct resultant is solely a reproducible definition of the already
# published factor. No old Bareiss matrix or old curve-gcd is built.
rr=pp.resultant(mm,'u');assert rr
assert all(int(m[1])==0 for m in rr.to_dict())
rp=fmpq_poly([rr.to_dict().get((i,0),fmpq(0))
              for i in range(int(rr.degrees()[0])+1)])
lp=fmpq_poly([0,1]);aa=fmpq_poly([1,-2,2]);bb=fmpq_poly([-1,3,-6,4])
ss=fmpq_poly([1,-2,-2,4])
for atom in (aa,bb,lp,2*lp-1,ss):
 while True:
  g=rp.gcd(atom)
  if int(g.degree())==0:break
  quotient,remainder=divmod(rp,g)
  assert not remainder and quotient*g==rp
  rp=quotient
rp/=rp[int(rp.degree())]
unit,fac=rp.factor()
choices=[f for f,e in fac if int(f.degree())==99]
assert len(choices)==1
F99=choices[0]
assert fprofile(F99)['sha256']=='e422b38e5f712eb9237d85ad116dfcdf8ec94f3886a7d97d210b48e3ce6a5a7e'
mod=F99/F99[int(F99.degree())]
assert int(mod.degree())==99
say('existing_F99_parameter_definition_ready',
 originalP_SHA256='8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c',
 originalMtrue_SHA256='65d420e901bd60b711d76ad23699daab655414b0595383a19a93d13180f30663',
 originalF99=fprofile(F99),entireQQConstantFieldDegree=99,
 historicalInputOnlyInRunnerMemory=True,
 old17BareissAndOldPMCurveGCDNotExecuted=True,
 oldF99DefinitionNotANewConclusion=True,F300Untouched=True,
 everyComplexEmbeddingRetained=True,noCoefficientPayloadSaved=True)
del rr,rp,fac,choices

stats={'constantInverseReturns':0,'polynomialDivisionReturns':0,
 'completeBezoutReturns':0,'multiSourceReturns':0,
 'paidPrimaryDivisionReturns':0,'quotientInverseReturns':0,
 'originalGramComponentReturns':0,'sameZOriginalValueReturns':0}
class Nonunit(Exception):
 def __init__(self,where,degree):
  self.where=where;self.degree=int(degree)
  super().__init__(where)
PHASE='constant field'
class K:
 _level=0
 def __init__(self,v=0):
  if isinstance(v,K):self.p=v.p;return
  if isinstance(v,fmpq_poly):self.p=v%mod
  else:self.p=fmpq_poly([fmpq(v)])%mod
 def __bool__(self):return bool(self.p)
 def __neg__(self):return K(-self.p)
 def __add__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return K(self.p+K(v).p)
 __radd__=__add__
 def __sub__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return self+-K(v)
 def __rsub__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return K(v)+-self
 def __mul__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return K(self.p*K(v).p)
 __rmul__=__mul__
 def inv(self):
  tick()
  if not self:raise Nonunit(PHASE,99)
  g,a,b=self.p.xgcd(mod)
  assert a*self.p+b*mod==g
  if int(g.degree())!=0:raise Nonunit(PHASE,int(g.degree()))
  out=K(a/g[0]);assert self*out==1 and out*self==1
  stats['constantInverseReturns']+=1
  return out
 def __truediv__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return self*K(v).inv()
 def __rtruediv__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return K(v)*self.inv()
 def __pow__(self,n):
  n=int(n)
  if n<0:return self.inv()**(-n)
  out=K(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def __eq__(self,v):
  if getattr(v,'_level',0)>0:return NotImplemented
  return self.p==K(v).p
K0=K();K1=K(1);LK=K(lp)
def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a
def padd(a,b,z):
 return trim([(a[i] if i<len(a) else z)+(b[i] if i<len(b) else z)
              for i in range(max(len(a),len(b)))])
def pneg(a):return [-c for c in a]
def psub(a,b,z):return padd(a,pneg(b),z)
def pscale(a,c):return trim([v*c for v in a])
def pmul(a,b,z):
 if not a or not b:return []
 c=[z for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=c[i+j]+x*y
 return trim(c)
def pdiv(a,b,z,inv):
 tick();a=trim(a);b=trim(b);assert b
 original=a[:];q=[z for _ in range(max(0,len(a)-len(b)+1))]
 lead=inv(b[-1])
 while len(a)>=len(b):
  d=len(a)-len(b);c=a[-1]*lead;q[d]=q[d]+c
  for j,y in enumerate(b):a[d+j]=a[d+j]-c*y
  a=trim(a)
 q=trim(q);assert padd(pmul(q,b,z),a,z)==original
 stats['polynomialDivisionReturns']+=1
 return q,a
def pxgcd(a,b,z,o,inv):
 r0=trim(a);r1=trim(b);s0=[o];s1=[];t0=[];t1=[o]
 while r1:
  q,r=pdiv(r0,r1,z,inv)
  r0,r1=r1,r
  s0,s1=s1,psub(s0,pmul(q,s1,z),z)
  t0,t1=t1,psub(t0,pmul(q,t1,z),z)
 if not r0:return [],[],[]
 sc=inv(r0[-1]);g=pscale(r0,sc);s0=pscale(s0,sc);t0=pscale(t0,sc)
 assert padd(pmul(s0,a,z),pmul(t0,b,z),z)==g
 stats['completeBezoutReturns']+=1
 return g,s0,t0
def peval(a,x,z):
 out=z
 for c in reversed(a):out=out*x+c
 return out
def kpoly_profile(a):
 raw=json.dumps([[str(v.p[i]) for i in range(int(v.p.degree())+1)]
                 if v else [] for v in a],separators=(',',':')).encode()
 return dict(degree=len(a)-1,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def multi_gcd(rows,z,o,inv,label):
 global PHASE
 g=[];tags=[[] for _ in rows]
 for i,row in enumerate(rows):
  PHASE=label+' row '+str(i)
  new,a,b=pxgcd(g,row,z,o,inv)
  tags=[pmul(a,t,z) for t in tags]
  tags[i]=padd(tags[i],b,z);g=new
  back=[]
  for t,r in zip(tags,rows):back=padd(back,pmul(t,r,z),z)
  assert back==g;stats['multiSourceReturns']+=1
  say('new_whole_field_original_gcd_step',variable=label,index=i,
      actualInputDegree=len(row)-1,commonDegree=len(g)-1,
      completeSameVariableBezoutReturned=True)
  if len(g)==1:break
 return g,tags
def data_in_u(data):
 du=max(int(j) for _,j,_ in data);out=[K0 for _ in range(du+1)]
 by=[{} for _ in range(du+1)]
 for i,j,c in data:by[int(j)][int(i)]=fmpq(c)
 for j,coeff in enumerate(by):
  out[j]=K(fmpq_poly([coeff.get(i,fmpq(0)) for i in range(max(coeff,default=-1)+1)]))
 return trim(out)

good=[];U0=None
def evaluate_Q(poly):
 # Every lambda and u coefficient is evaluated in the ENTIRE K99.
 cacheL={0:K1};cacheU={0:K1}
 out=[K0 for _ in range(max((int(m[2]) for m in poly.to_dict()),default=-1)+1)]
 for ex,c in poly.to_dict().items():
  il,iu,iq=map(int,ex)
  if il not in cacheL:cacheL[il]=LK**il
  if iu not in cacheU:cacheU[iu]=U0**iu
  out[iq]=out[iq]+K(c)*cacheL[il]*cacheU[iu]
 return trim(out)

class Aq:
 _level=1
 def __init__(self,v=0):
  if isinstance(v,Aq):self.c=v.c[:];return
  a=trim([K(x) for x in v]) if isinstance(v,(list,tuple)) else ([K(v)] if K(v) else [])
  assert good and good[-1]==1
  while len(a)>=len(good):
   d=len(a)-len(good);c=a[-1]
   for i,vv in enumerate(good):a[d+i]=a[d+i]-c*vv
   a=trim(a)
  self.c=a
 def __bool__(self):return bool(self.c)
 def __neg__(self):return Aq(pneg(self.c))
 def __add__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  return Aq(padd(self.c,Aq(v).c,K0))
 __radd__=__add__
 def __sub__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  return self+-Aq(v)
 def __rsub__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  return Aq(v)+-self
 def __mul__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  return Aq(pmul(self.c,Aq(v).c,K0))
 __rmul__=__mul__
 def inv(self):
  g,a,b=pxgcd(self.c,good,K0,K1,lambda x:x.inv())
  if len(g)!=1:raise Nonunit(PHASE,len(g)-1)
  out=Aq(pscale(a,g[0].inv()))
  assert out*self==1 and self*out==1
  stats['quotientInverseReturns']+=1
  return out
 def __truediv__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  return self*Aq(v).inv()
 def __rtruediv__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  return Aq(v)*self.inv()
 def __pow__(self,n):
  n=int(n)
  if n<0:return self.inv()**(-n)
  out=Aq(1);a=self
  while n:
   if n&1:out=out*a
   n//=2
   if n:a=a*a
  return out
 def __eq__(self,v):
  if getattr(v,'_level',0)>1:return NotImplemented
  return self.c==Aq(v).c
def aq_profile(x):return kpoly_profile(x.c)
AZ=None;AO=None
class Pz:
 _level=2
 def __init__(self,v=0):
  if isinstance(v,Pz):self.c=v.c[:];return
  self.c=trim([Aq(x) for x in v]) if isinstance(v,(list,tuple)) else ([Aq(v)] if Aq(v) else [])
 def __bool__(self):return bool(self.c)
 def __neg__(self):return Pz(pneg(self.c))
 def __add__(self,v):
  if getattr(v,'_level',0)>2:return NotImplemented
  return Pz(padd(self.c,Pz(v).c,AZ))
 __radd__=__add__
 def __sub__(self,v):
  if getattr(v,'_level',0)>2:return NotImplemented
  return self+-Pz(v)
 def __rsub__(self,v):
  if getattr(v,'_level',0)>2:return NotImplemented
  return Pz(v)+-self
 def __mul__(self,v):
  if getattr(v,'_level',0)>2:return NotImplemented
  return Pz(pmul(self.c,Pz(v).c,AZ))
 __rmul__=__mul__
 def __truediv__(self,v):
  assert getattr(v,'_level',0)<2
  return Pz(pscale(self.c,Aq(v).inv()))
 def __pow__(self,n):
  assert n>=0
  out=Pz(1);a=self
  while n:
   if n&1:out=out*a
   n//=2
   if n:a=a*a
  return out
 def __eq__(self,v):
  if getattr(v,'_level',0)>2:return NotImplemented
  return self.c==Pz(v).c
DELTA=None
class E:
 _level=3
 def __init__(self,e=0,o=0):
  if isinstance(e,E):self.e=e.e;self.o=e.o;return
  self.e=Pz(e);self.o=Pz(o)
 def __bool__(self):return bool(self.e) or bool(self.o)
 def __neg__(self):return E(-self.e,-self.o)
 def __add__(self,v):
  v=E(v);return E(self.e+v.e,self.o+v.o)
 __radd__=__add__
 def __sub__(self,v):return self+-E(v)
 def __rsub__(self,v):return E(v)+-self
 def __mul__(self,v):
  v=E(v)
  return E(self.e*v.e+DELTA*self.o*v.o,self.e*v.o+self.o*v.e)
 __rmul__=__mul__
 def __truediv__(self,v):
  assert getattr(v,'_level',0)<2
  return E(self.e/v,self.o/v)
 def __pow__(self,n):
  assert n>=0
  out=E(1);a=self
  while n:
   if n&1:out=out*a
   n//=2
   if n:a=a*a
  return out
 def conj(self):return E(self.e,-self.o)
 def __eq__(self,v):
  v=E(v);return self.e==v.e and self.o==v.o

def run_new_fiber():
 global U0,good,PHASE,AZ,AO,DELTA
 upol=data_in_u(pdata);mpol=data_in_u(mdata)
 ug,utags=multi_gcd([upol,mpol],K0,K1,lambda x:x.inv(),'u')
 say('new_F99_whole_u_gcd_return',common=kpoly_profile(ug),
     actualOriginalUDegrees=[len(upol)-1,len(mpol)-1],
     allOriginalULeadingZeroSpecializationsRetained=True,
     allNinetyNineEmbeddingsRetained=True)
 if len(ug)==1:
  return dict(excluded=True,reason='complete original P/M Bezout one')
 if len(ug)!=2:
  return dict(excluded=False,reason='whole original u factor retained',
              remainingUDegree=len(ug)-1)
 U0=-ug[0];assert ug[1]==1
 assert peval(upol,U0,K0)==0 and peval(mpol,U0,K0)==0
 say('new_F99_unique_original_u',u= fprofile(U0.p),
     originalMonicULinearIdentityReturned=True)
 qrows=[evaluate_Q(orig['Delta'].n),evaluate_Q(orig['Tnum'].n),evaluate_Q(Ftrue)]
 qg,qtags=multi_gcd(qrows,K0,K1,lambda x:x.inv(),'Q')
 if len(qg)==1:
  return dict(excluded=True,reason='same-Q original Delta Tnum Ftrue Bezout one')
 if not qg:
  return dict(excluded=False,reason='all original same-Q conditions zero',
              allQFibersRetained=True)
 atoms=[('A',orig['A']),('B',orig['B']),('Q',orig['Q']),
        ('1-Q',orig['disc']),('Pf',orig['Pf']),('bc',orig['bc']),
        ('P02',orig['P02']),('u',orig['u']),('u-1',orig['u']-1),
        ('S',orig['S'])]
 paid=[]
 for name,value in atoms:
  p=evaluate_Q(value.n)
  if not p:
   say('new_F99_whole_original_paid_atom_zero',originalAtom=name,
       entireOriginalWeightFiberExcluded=True)
   return dict(excluded=True,reason='an entire original paid atom is zero',atom=name)
  paid.append((name,p))
 good=qg[:];removed=[K1]
 for name,atom in paid:
  layers=[]
  while len(good)>1:
   PHASE='paid primary '+name
   cut,_,_=pxgcd(good,atom,K0,K1,lambda x:x.inv())
   if len(cut)==1:break
   q,r=pdiv(good,cut,K0,lambda x:x.inv());assert not r
   a,r=pdiv(atom,cut,K0,lambda x:x.inv());assert not r
   good=q;removed=pmul(removed,cut,K0)
   assert pmul(good,removed,K0)==qg
   stats['paidPrimaryDivisionReturns']+=2
   layers.append(len(cut)-1)
  if layers:say('new_F99_same_Q_paid_primary_removal',
       atom=name,removedDegreeLayers=layers,remainingQDegree=len(good)-1,
       completeOriginalGCDAndDivisionProductsReturned=True,
       noUnpaidPrimaryFactorRemoved=True)
 if len(good)==1:
  return dict(excluded=True,reason='all same-Q roots excluded by original paid atoms')
 if len(good)>3:
  return dict(excluded=False,reason='whole same-Q factor exceeds new small model',
              remainingQDegree=len(good)-1)
 AZ=Aq();AO=Aq(1);q=Aq([K0,K1])
 PHASE='complete finite Q algebra original units'
 for name,atom in paid:
  PHASE='whole Q algebra paid '+name
  value=Aq(atom);inverse=value.inv()
  assert value*inverse==1 and inverse*value==1
 PHASE='original collision Gram recovery'
 ll=Aq(LK);uu=Aq(U0);delta=1-q;DELTA=delta
 A=2*ll*ll-2*ll+1;B=4*ll**3-6*ll*ll+3*ll-1
 xi=B/A;ell=A**3/(B*B);T=A*A/B;w=ll-1-T;h=1+xi
 m=uu-ell;aa0=1-ell
 bc=(ell*ell-m*m/delta)/4;M=4*bc*delta
 V2=2*uu-ell*q;T0=V2-2*uu*uu;J=2*uu*(1-uu)+ell*q
 Phi=T0+4*uu-4+q
 P02=(2-3*uu)*V2-q*uu+2*uu**3
 Pf=T0*(J-q);G=ll*P02-(1-uu)*T0
 Pc=q*P02*(ell+T)-G*T0
 def mapped(value):
  return Aq(evaluate_Q(value.n))/Aq(evaluate_Q(value.d))
 for name,value in [('A',A),('B',B),('ell',ell),('T',T),('Pf',Pf),
                    ('bc',bc),('P02',P02),('Phi',Phi),('Pc',Pc)]:
  assert value==mapped(orig[name]);stats['originalGramComponentReturns']+=1
 z=Pz([0,1]);t=z/q
 ff=-(Pz(Pc)+bc*Phi*z)/Pf
 VV=(J*ff-G+bc*z)/q;WW=T0/2+2*uu*ff
 xx=((uu-ell*q)*VV-m*WW)/M
 yy=(ell*WW-uu*VV)/M
 A1=2*ff-2*VV+2*bc*t
 rho=E(0,1);b=E(ell/2,m/(2*delta));c=b.conj()
 p=1+rho;qc=1-rho;X=E(xx,yy);Y=X.conj()
 r=X-aa0*p-c*t;ss=Y-aa0*qc-b*t
 rows=[[E(),E(),p,qc],[E(),E(A1),r,ss],
       [p,r,E(),E(t)],[qc,ss,E(t),E()]]
 one=[E(1),E(),E(1),E(1)]
 def vm(vv,ww):
  return [vv[0]*ww[0],vv[0]*ww[1]+vv[1]*ww[0],
          vv[2]*ww[2],vv[3]*ww[3]]
 def tau(vv):return aa0*vv[0]+vv[1]+b*vv[2]+c*vv[3]
 def DK(vv):return [tau(vm(row,vv)) for row in rows]
 d=DK(one);F2=tau(d);Kd=DK(d)
 assert d[0]==uu and d[2]==X and d[3]==Y and F2==2*ff
 assert b*c==bc and b+c==ell and b*p+c*qc==uu and p*qc==q
 stats['originalGramComponentReturns']+=8
 def N4(vv):
  vv2=vm(vv,vv);tv=tau(vv)
  return (2*tau(vm(d,vv2))-F2*tau(vv2)
          -4*tv*tau(vm(d,vv))+2*F2*tv*tv+tau(vm(vv,DK(vv))))
 def center(vv):
  tv=tau(vv)
  return [v-tv*e for v,e in zip(vv,one)]
 def P2(vv):
  vc=center(vv);return tau(vm(vm(vc,vc),vc))
 g0,g1,gB,gC=rows
 N0=N4(g0);Nrow1=N4(g1)
 NJ=N4([x+y for x,y in zip(g0,g1)])-N0-Nrow1
 c0=center(g0);c1=center(g1);PJ=3*tau(vm(vm(c0,c0),c1))
 assert P2(g0)==P02 and N0==2*ll*P02 and PJ==3*w*P02
 stats['originalGramComponentReturns']+=3
 e1=2*tau(vm(g0,g1))-2*Kd[1]-2*vm(d,d)[1]+2*F2*d[1]
 eb=tau(vm(gB,gB))-2*Kd[2]-2*d[2]*d[2]+2*F2*d[2]
 ec=tau(vm(gC,gC))-2*Kd[3]-2*d[3]*d[3]+2*F2*d[3]
 n1=NJ-4*ll*w*P02
 nb=N4(gB)-2*ll*h*h*P02
 pb=P2(gB)-h**3*P02
 assert not e1.o and not n1.o and ec==eb.conj()
 values=[('E1even',e1.e),('EBe',eb.e),('EBo',eb.o),('N1jet',n1.e),
         ('NB_even',nb.e),('NB_odd',nb.o),('PB_even',pb.e),('PB_odd',pb.o)]
 # rho is a physical unit, so both spectrum coefficients of a value
 # vanishing at a point are necessary together with its B/C conjugate.
 assert N4(gC)-2*ll*h*h*P02==nb.conj()
 assert P2(gC)-h**3*P02==pb.conj()
 stats['originalGramComponentReturns']+=5
 for name,value in values:
  stats['sameZOriginalValueReturns']+=1
  say('new_F99_whole_same_z_original_value',name=name,
      actualZDegree=len(value.c)-1,wholeQDegree=len(good)-1,
      fullDualMultiplicationUsed=True,noPhysicalDInverse=True)
 zrows=[v.c for _,v in values]
 zg,ztags=multi_gcd(zrows,AZ,AO,lambda x:x.inv(),'z')
 # multi_gcd returns the full eight-source identity in the WHOLE
 # finite Q algebra; a nonunit leading coefficient is caught, not divided.
 returned=[]
 for tag,row in zip(ztags,zrows):returned=padd(returned,pmul(tag,row,AZ),AZ)
 assert returned==zg
 if len(zg)==1:
  assert zg[0]==1
  return dict(excluded=True,reason='whole same-z original eight-value Bezout one',
              finiteQAlgebraDimension=99*(len(good)-1),
              allEightOriginalSourcesReturned=True)
 return dict(excluded=False,reason='whole same-z original factor retained',
             remainingQDegree=len(good)-1,remainingZDegree=len(zg)-1,
             allQAndZMultiplicityRetained=True)

try:
 result=run_new_fiber()
except Nonunit as exc:
 result=dict(excluded=False,reason='whole algebra nonunit retained',
             firstNonunitStage=exc.where,nonunitGCDDegree=exc.degree,
             allOriginalF99EmbeddingsAndRemainingFibersRetained=True)
say('new_F99_entire_original_fiber_first_input_finished',
 result=result,entireF99OriginalFiberExcluded=bool(result.get('excluded')),
 F300Untouched=True,noWholeCollisionOrOrdinaryISPClaim=True,
 noOld17BareissOrOldPMCurveGCDGateReplayed=True,
 noFrozenOriginalMatrixOrPositiveTargetReplayed=True,
 noPhysicalDOrItsNormInverse=True,
 noCoefficientCachePayloadOrChunksSaved=True,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 statistics=stats,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
REAL_TIMER(signal.ITIMER_REAL,0)
