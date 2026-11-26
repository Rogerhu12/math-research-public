#!/usr/bin/env python3
"""R150 S=0,h=k,2lambda^2=1: original full nine conditions on both roots.
A polynomial scaled Gram matrix avoids every artificial norm denominator.
Use the already closed S=Af=0,L!=0 layer; never invert a P1 coefficient.
"""
import argparse,hashlib,itertools,json,os,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
started=time.perf_counter()
ap=argparse.ArgumentParser()
ap.add_argument('--seconds',type=int,default=int(os.environ.get('ISP_S0_SECONDS','120')))
args=ap.parse_args()
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(args.seconds)
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
ctx=fmpq_mpoly_ctx.get(('b','q'),'lex')
bp,qp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
def profile(v):
 dd=v.to_dict()
 return {'degrees':[max((int(m[i]) for m in dd),default=-1) for i in range(2)],'terms':len(dd)}
# A complete moment cover, with no division by l or by the mean.
xx=fmpq_poly([0,1]);av=2*xx*xx-2*xx+1;vv=xx-fmpq(1,2)
lambda_cover=(2*xx-1)*(2*xx*xx-1)
assert 4*xx**3-3*xx+2-av*(vv+2)==lambda_cover/2
assert lambda_cover.gcd(vv-1).degree()==0
say({'stage':'complete_original_equal_value_moment_cover_verified','lambdaPolynomial':str(lambda_cover),'completeThreeRootMomentCoverVerified':True,'lambdaHalfSeparatelyClosed':True,'claimExcluded':False})
def run_case(case):
 delta=0 if case=='lambda_half' else 2
 class E:
  def __init__(self,a0=0,b0=0):
   if isinstance(a0,E):self.a=a0.a;self.b=a0.b;return
   self.a=poly(a0);self.b=poly(b0)
  def __bool__(self):return bool(self.a) or bool(self.b)
  def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
  __radd__=__add__
  def __neg__(self):return E(-self.a,-self.b)
  def __sub__(self,o):return self+-E(o)
  def __rsub__(self,o):return E(o)+-self
  def __mul__(self,o):o=E(o);return E(self.a*o.a+delta*self.b*o.b,self.a*o.b+self.b*o.a)
  __rmul__=__mul__
  def __pow__(self,n):
   out=E(1);v=self
   while n:
    if n&1:out=out*v
    v=v*v;n//=2
   return out
  def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
  def conj(self):return E(self.a,-self.b)
  def norm(self):return self.a*self.a-delta*self.b*self.b
 half=fmpq(1,2)
 if case=='lambda_half':
  lam=E(half);l=E(half);w=E();h=E()
 else:
  lam=E(0,half);l=8*(5+lam)*fmpq(1,49);w=(3*lam+1)*fmpq(1,7);h=lam-half
  assert 2*lam*lam==1
 b=E(bp);c=l-b;a=1-l;p=E(1);q=E(qp);k=h
 assert 2*h+1==2*lam
 assert a+w+l*h==lam
 assert a+2*w+l*h*h==2*lam*lam
 assert a+3*w+l*h**3==4*lam**3
 assert h!=1
 u=b+c*q;V2=b+c*q*q;P02=b+c*q**3-3*u*V2+2*u**3
 D=2*b*c*q*(q-1)
 class P:
  def __init__(self,co=None):self.co={ij:E(v) for ij,v in (co or {}).items() if E(v)}
  def __bool__(self):return bool(self.co)
  def __add__(self,o):
   if not isinstance(o,P):o=cp(o)
   dd=dict(self.co)
   for ij,v in o.co.items():dd[ij]=dd.get(ij,E())+v
   return P(dd)
  __radd__=__add__
  def __neg__(self):return P({ij:-v for ij,v in self.co.items()})
  def __sub__(self,o):return self+-o
  def __rsub__(self,o):return cp(o)+-self
  def __mul__(self,o):
   if not isinstance(o,P):return scale(E(o),self)
   dd={}
   for ij,v in self.co.items():
    for kl,vv in o.co.items():
     key=(ij[0]+kl[0],ij[1]+kl[1]);dd[key]=dd.get(key,E())+v*vv
   return P(dd)
  __rmul__=__mul__
  def __pow__(self,n):
   out=cp(1)
   for _ in range(n):out=out*self
   return out
 def cp(v):return P({(0,0):E(v)})
 def scale(v,pp):return P({ij:E(v)*vv for ij,vv in pp.co.items()})
 fp=P({(1,0):E(1)});tp=P({(0,1):E(1)});zero=P()
 one=[cp(1),zero,cp(1),cp(1)]
 def va(v,z0):return [x+y for x,y in zip(v,z0)]
 def vs(v0,v):return [v0*x for x in v]
 def vm(v,z0):return [v[0]*z0[0],v[0]*z0[1]+v[1]*z0[0],v[2]*z0[2],v[3]*z0[3]]
 def tau(v):return scale(a,v[0])+v[1]+scale(b,v[2])+scale(c,v[3])
 T0=V2-2*u*u
 W1=cp(T0*half)+scale(2*u,fp)
 W2=cp(u*T0+lam*P02)+scale(V2+2*u*u,fp)-scale(b*c*q,tp)
 # D*X and D*Y, with D=2bcq(q-1), are polynomial identities.
 Xhat=scale(2*c*q,scale(q,W1)-W2)
 Yhat=scale(2*b,W2-W1)
 rhat=Xhat-cp(D*a)-scale(D*c,tp)
 shat=Yhat-cp(D*a*q)-scale(D*b,tp)
 Ahat=scale(2*D,fp)-scale(2*b,Xhat)-scale(2*c,Yhat)+scale(2*D*b*c,tp)
 rows=[[zero,zero,cp(D),cp(D*q)],[zero,Ahat,rhat,shat],[cp(D),rhat,zero,scale(D,tp)],[cp(D*q),shat,scale(D,tp),zero]]
 def DK(v):return [tau(vm(row,v)) for row in rows]
 d=DK(one);F2=tau(d);DKd=DK(d);dd=vm(d,d)
 assert not (F2-scale(2*D,fp))
 def P2(v):
  cen=va(v,vs(-tau(v),one))
  return tau(vm(vm(cen,cen),cen))
 def N4(v):
  return scale(E(2),tau(vm(d,vm(v,v))))-F2*tau(vm(v,v))-scale(E(4),tau(v)*tau(vm(d,v)))+scale(E(2),F2*tau(v)**2)+tau(vm(v,DK(v)))
 def Pjet2(v,z0):
  v0=va(v,vs(-tau(v),one));z1=va(z0,vs(-tau(z0),one))
  return scale(E(3),tau(vm(vm(v0,v0),z1)))
 def Njet4(v,z0):return N4(va(v,z0))-N4(v)-N4(z0)
 def mean(jj):
  ev=scale(E(2),tau(vm(rows[0],rows[1]))) if jj==1 else tau(vm(rows[jj],rows[jj]))
  return ev-scale(E(2),DKd[jj])-scale(E(2),dd[jj])+scale(E(2),F2*d[jj])
 scaledP02=D**3*P02
 assert not mean(0) and not (P2(rows[0])-cp(scaledP02))
 assert not (N4(rows[0])-cp(2*lam*scaledP02))
 VV=[cp(1),cp(w),cp(h),cp(k)]
 assert not P2(VV)
 NV=N4(VV)
 assert set(NV.co).issubset({(1,0),(0,0)})
 raw=[mean(1),mean(2),mean(3),Pjet2(rows[0],rows[1])-cp(3*w*scaledP02),P2(rows[2])-cp(h**3*scaledP02),P2(rows[3])-cp(k**3*scaledP02),Njet4(rows[0],rows[1])-cp(4*lam*w*scaledP02),N4(rows[2])-cp(2*lam*h*h*scaledP02),N4(rows[3])-cp(2*lam*k*k*scaledP02)]
 names=['E1','EB','EC','P1','PB','PC','N1','NB','NC']
 hh=hashlib.sha256()
 for name,po in zip(names+['NV'],raw+[NV]):
  for ij,v in sorted(po.co.items()):
   hh.update((name+str(ij)+str(sorted(v.a.to_dict().items()))+'/'+str(sorted(v.b.to_dict().items()))+'\n').encode())
 inputsha=hh.hexdigest()
 say({'stage':'full_original_scaled_Gram_nine_and_Nvalue_generated','case':case,'sourceSha256':source_sha,'inputSha256':inputsha,'ftDegrees':[max((sum(ij) for ij in po.co),default=-1) for po in raw],'allPhysicalParameterConjugatesRetained':True,'claimExcluded':False})
 # Exact division by an actual original nonzero E-polynomial. Its norm is used
 # only to compute a polynomial quotient, NEVER assumed nonzero at a point.
 quotient_checks=0
 def exact_div(v,atom,norm):
  nonlocal quotient_checks
  na=v.a*atom.a-delta*v.b*atom.b
  nb=v.b*atom.a-v.a*atom.b
  gg=norm.gcd(na).gcd(nb)
  if gg.total_degree()!=norm.total_degree():return None
  out=E(na/norm,nb/norm)
  assert out*atom==v
  quotient_checks+=1
  return out
 atomdata=[]
 for label,v in [('b',b),('c',c),('q',q),('q-1',q-1),('q+1',q+1)]:
  atomdata.append((label,v,v.norm()))
 def strip_coefficients(vv):
  vv=list(vv)
  for label,atom,norm in atomdata:
   if norm.total_degree()==0:continue
   while any(vv):
    out=[exact_div(v,atom,norm) for v in vv]
    if any(v is None for v in out):break
    vv=out
  return vv
 nvline=strip_coefficients([NV.co.get((1,0),E()),NV.co.get((0,0),E())])
 Af,Cf=nvline
 assert Af
 # L=(q-1)(h-1) is nonzero on both complete collision fibers.
 # The entire S=Af=0,L!=0 layer is already closed (51d84b503698...).
 # Thus the actual NV f coefficient is a paid unit; no norm is paid.
 atomdata.append(('actual_NV_f_coefficient',Af,Af.norm()))
 clear_cache={}
 def get_poly(index):
  if index in clear_cache:return clear_cache[index]
  po=raw[index]
  m=max((ij[0] for ij in po.co),default=0)
  nt=max((ij[1] for ij in po.co),default=-1)
  out=[E() for _ in range(nt+1)]
  for (i,j0),v in po.co.items():out[j0]=out[j0]+v*((-Cf)**i)*(Af**(m-i))
  out=strip_coefficients(out)
  while out and not out[-1]:out.pop()
  clear_cache[index]=out
  say({'stage':'original_f_replacement_without_norm_inversion','case':case,'name':names[index],'tDegree':len(out)-1,'coefficientProfiles':[{'even':profile(v.a),'odd':profile(v.b)} for v in out],'claimExcluded':False})
  return out
 # Verify the substituted original NV exactly, with its own f-degree one.
 assert NV.co.get((1,0),E())*(-Cf)+NV.co.get((0,0),E())*Af==0
 def determinant(mm):
  n=len(mm)
  if n==0:return E(1)
  if n==1:return mm[0][0]
  out=E()
  for j0 in range(n):
   if mm[0][j0]:out=out+((-1)**j0)*mm[0][j0]*determinant([row[:j0]+row[j0+1:] for row in mm[1:]])
  return out
 def resultant(pp,qq):
  if not pp or not qq:return E()
  n=len(pp)-1;m=len(qq)-1
  if n==0:return pp[0]**m if m else pp[0]
  if m==0:return qq[0]**n
  mat=[]
  for i in range(m):mat.append([E()]*i+pp[::-1]+[E()]*(m-1-i))
  for i in range(n):mat.append([E()]*i+qq[::-1]+[E()]*(n-1-i))
  return determinant(mat)
 line=get_poly(3);assert len(line)<=2
 projections=[];labels=[]
 for index in [0,1,2,6,4,5,7,8]:
  projections.append(strip_coefficients([resultant(line,get_poly(index))])[0])
  labels.append(['P1',names[index]])
 for ii,jj in [(0,1),(0,2),(1,2)]:
  projections.append(strip_coefficients([resultant(get_poly(ii),get_poly(jj))])[0])
  labels.append([names[ii],names[jj]])
 return complete_quadratic_return(projections,labels,Af,inputsha,quotient_checks)

# Coefficients for the q-resultant: Q[sqrt(2)][b], without a norm projection.
class BQ:
 def __init__(self,a=0,b=0):
  if isinstance(a,BQ):self.a=a.a;self.b=a.b;return
  self.a=a if isinstance(a,fmpq_poly) else fmpq_poly([a])
  self.b=b if isinstance(b,fmpq_poly) else fmpq_poly([b])
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=BQ(o);return BQ(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return BQ(-self.a,-self.b)
 def __sub__(self,o):return self+-BQ(o)
 def __rsub__(self,o):return BQ(o)+-self
 def __mul__(self,o):o=BQ(o);return BQ(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=BQ(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):o=BQ(o);return self.a==o.a and self.b==o.b
 def exact_quotient(self,o):
  o=BQ(o);assert o
  norm=o.a*o.a-2*o.b*o.b
  qa,ra=divmod(self.a*o.a-2*self.b*o.b,norm)
  qb,rb=divmod(self.b*o.a-self.a*o.b,norm)
  assert not ra and not rb
  out=BQ(qa,qb);assert out*o==self
  return out
 def norm(self):return self.a*self.a-2*self.b*self.b
 def degree(self):return max(int(self.a.degree()),int(self.b.degree()))
def trim(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
def addpoly(pp,qq,zero):
 out=[zero]*max(len(pp),len(qq))
 for j,v in enumerate(pp):out[j]=out[j]+v
 for j,v in enumerate(qq):out[j]=out[j]+v
 return trim(out)
def mulpoly(pp,qq,zero):
 if not pp or not qq:return []
 out=[zero]*(len(pp)+len(qq)-1)
 for i,v in enumerate(pp):
  for j,w in enumerate(qq):out[i+j]=out[i+j]+v*w
 return trim(out)
def pseudoremainder(f,g):
 f=trim(f);g=trim(g);assert g
 d=len(f)-len(g)+1;original=list(f);quotient=[];original_d=d
 while f and len(f)>=len(g):
  a=f[-1];shift=len(f)-len(g)
  f=[v*g[-1] for v in f];quotient=[v*g[-1] for v in quotient]
  quotient=addpoly(quotient,[BQ()] * shift+[a],BQ())
  for j,v in enumerate(g):f[shift+j]=f[shift+j]-a*v
  f=trim(f);d-=1
 power=g[-1]**d
 f=[v*power for v in f];quotient=[v*power for v in quotient]
 assert trim([v*(g[-1]**original_d) for v in original])==addpoly(mulpoly(quotient,g,BQ()),f,BQ())
 return f
def subresultant(f,g):
 # Brown's exact subresultant PRS. The scalar last subresultant is the
 # Sylvester determinant; all ring divisions below are exact identities.
 f=trim(f);g=trim(g)
 if len(f)<len(g):f,g=g,f
 n=len(f)-1;m=len(g)-1;d=n-m
 h=[v*((-1)**(d+1)) for v in pseudoremainder(f,g)]
 lc=g[-1];c=-(lc**d);scalar=BQ(1);degrees=[];divisions=0
 while h:
  k=len(h)-1;f,g,m,d=g,h,k,m-k
  divisor=-lc*c**d
  raw=pseudoremainder(f,g)
  h=[v.exact_quotient(divisor) for v in raw];divisions+=len(raw)
  lc=g[-1]
  if d>1:c=((-lc)**d).exact_quotient(c**(d-1));divisions+=1
  else:c=-lc
  scalar=-c;degrees.append([k,max(v.degree() for v in g)])
 if len(g)>1:return BQ(),degrees,divisions
 return scalar,degrees,divisions

# Finite commutative Q-algebras; no irreducibility assumption is needed.
class FE:
 def __init__(self,field,v=0):
  self.field=field
  if isinstance(v,FE):assert v.field is field;self.p=v.p;return
  self.p=divmod(v if isinstance(v,fmpq_poly) else fmpq_poly([v]),field.mod)[1]
 def __bool__(self):return bool(self.p)
 def __add__(self,o):o=FE(self.field,o);return FE(self.field,self.p+o.p)
 __radd__=__add__
 def __neg__(self):return FE(self.field,-self.p)
 def __sub__(self,o):return self+-FE(self.field,o)
 def __rsub__(self,o):return FE(self.field,o)+-self
 def __mul__(self,o):o=FE(self.field,o);return FE(self.field,self.p*o.p)
 __rmul__=__mul__
 def __pow__(self,n):
  out=FE(self.field,1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):o=FE(self.field,o);return self.p==o.p
 def inv(self):
  assert self
  gg,ss,tt=self.p.xgcd(self.field.mod)
  assert self.p*ss+self.field.mod*tt==gg and gg.degree()==0
  out=FE(self.field,ss/gg[0]);assert out*self==1
  self.field.inverses+=1;return out
class Algebra:
 def __init__(self,p):
  self.mod=p/p.leading_coefficient();self.inverses=0;self.bezout=0;self.divisions=0
  self.zero=FE(self);self.one=FE(self,1)
 def __call__(self,v=0):return FE(self,v)
def dividep(pp,qq):
 pp=trim(pp);qq=trim(qq);assert qq
 field=qq[0].field;original=list(pp);inv=qq[-1].inv()
 out=[field.zero]*max(0,len(pp)-len(qq)+1)
 while pp and len(pp)>=len(qq):
  shift=len(pp)-len(qq);a=pp[-1]*inv;out[shift]=out[shift]+a
  for j,v in enumerate(qq):pp[shift+j]=pp[shift+j]-a*v
  pp=trim(pp)
 out=trim(out)
 assert original==addpoly(mulpoly(out,qq,field.zero),pp,field.zero)
 field.divisions+=1
 return out,pp
def gcdp(pp,qq):
 pp=trim(pp);qq=trim(qq)
 if not pp and not qq:return []
 field=(pp or qq)[0].field;zero=field.zero;one=field.one
 originalp=list(pp);originalq=list(qq)
 s0=[one];s1=[];t0=[];t1=[one]
 while qq:
  quotient,remainder=dividep(pp,qq);pp,qq=qq,remainder
  s0,s1=s1,addpoly(s0,[-v for v in mulpoly(quotient,s1,zero)],zero)
  t0,t1=t1,addpoly(t0,[-v for v in mulpoly(quotient,t1,zero)],zero)
 if pp:
  inv=pp[-1].inv();pp=[inv*v for v in pp];s0=[inv*v for v in s0];t0=[inv*v for v in t0]
 assert pp==addpoly(mulpoly(s0,originalp,zero),mulpoly(t0,originalq,zero),zero)
 field.bezout+=1
 return pp

def complete_quadratic_return(projections,labels,Af,inputsha,quotient_checks):
 def to_q_poly(expr):
  ad=expr.a.to_dict();bd=expr.b.to_dict();terms=set(ad)|set(bd)
  out=[]
  for j in range(max(int(m[1]) for m in terms)+1):
   n=max((int(m[0]) for m in terms if int(m[1])==j),default=-1)
   out.append(BQ(fmpq_poly([ad.get((i,j),0) for i in range(n+1)]),fmpq_poly([bd.get((i,j),0) for i in range(n+1)])))
  return trim(out)
 qpolys=[to_q_poly(v) for v in projections]
 rr=[];rprofiles=[];normgcd=fmpq_poly()
 for j in [1,2,3]:
  v,seq,divisions=subresultant(qpolys[0],qpolys[j]);assert v
  rr.append(v);nn=v.norm();normgcd=nn if not normgcd else normgcd.gcd(nn)
  raw=json.dumps([[str(c) for c in v.a],[str(c) for c in v.b]],separators=(',',':'))
  rprofiles.append({'pair':[labels[0],labels[j]],'bDegree':v.degree(),'normDegree':int(nn.degree()),'subresultantDegrees':seq,'exactQuotientIdentities':divisions,'sha256':hashlib.sha256(raw.encode()).hexdigest()})
  say({'stage':'same_lambda_original_q_resultant','result':rprofiles[-1],'claimExcluded':False})
 sf=normgcd/normgcd.gcd(normgcd.derivative());sf=sf/sf.leading_coefficient()
 content,factors=sf.factor(monic=True);product=fmpq_poly([content])
 for phi,mul in factors:product*=phi**mul
 assert product==sf
 factorinfo=[{'degree':int(phi.degree()),'polynomial':str(phi),'multiplicity':int(mul)} for phi,mul in factors]
 say({'stage':'complete_same_lambda_finite_b_cover','squarefreeBDegree':int(sf.degree()),'factors':factorinfo,'claimExcluded':False})
 def evaluate_q(expr,alg,bval,alpha):
  values={}
  for component,weight in [(expr.a,alg.one),(expr.b,alpha)]:
   for (ib,iq),v in component.to_dict().items():
    iq=int(iq);values[iq]=values.get(iq,alg.zero)+v*(bval**int(ib))*weight
  return trim([values.get(i,alg.zero) for i in range(max(values,default=-1)+1)])
 reports=[]
 for phi,mul in factors:
  if phi.degree()==1 and phi[0]==0:
   reports.append({'phi':str(phi),'excluded':True,'reason':'original_b_is_nonzero'});continue
  if phi.degree()==1:
   alg=Algebra(fmpq_poly([-2,0,1]));bval=alg(-phi[0]);alpha=alg(fmpq_poly([0,1]))
  else:
   alg=Algebra(phi);bval=alg(fmpq_poly([0,1]));alpha=None
   for v in rr:
    even=alg(v.a);odd=alg(v.b)
    if odd:alpha=-even*odd.inv();assert alpha*alpha==2;break
    assert not even
   assert alpha is not None
   for v in rr:assert alg(v.a)+alpha*alg(v.b)==0
  lam=alpha*fmpq(1,2);ell=(5+lam)*fmpq(8,49);cval=ell-bval
  if not cval:
   reports.append({'phi':str(phi),'excluded':True,'reason':'original_c_is_nonzero','inverseIdentities':alg.inverses});continue
  pp=[];history=[]
  for index,expr in enumerate(projections):
   pp=gcdp(pp,evaluate_q(expr,alg,bval,alpha));history.append(len(pp)-1)
   if len(pp)==1:break
  removed=[]
  units=[('original_q',[alg.zero,alg.one]),('original_q_minus_one',[-alg.one,alg.one]),('previously_closed_q_plus_one',[alg.one,alg.one]),('previously_closed_Af_zero',evaluate_q(Af,alg,bval,alpha))]
  for label,unit in units:
   while len(pp)>1:
    gg=gcdp(pp,unit)
    if len(gg)<=1:break
    pp,remainder=dividep(pp,gg);assert not remainder
    removed.append({'paidUnit':label,'degree':len(gg)-1})
  report={'phi':str(phi),'bDegree':int(phi.degree()),'qGcdDegrees':history,'removedPaidUnits':removed,'remainingQDegree':len(pp)-1,'inverseIdentities':alg.inverses,'divisionIdentities':alg.divisions,'bezoutIdentities':alg.bezout,'excluded':len(pp)==1}
  reports.append(report);say({'stage':'same_lambda_original_q_fiber_return','report':report,'claimExcluded':False})
 closed=all(v['excluded'] for v in reports)
 return {'sourceSha256':source_sha,'inputSha256':inputsha,'originalPolynomialQuotientIdentities':quotient_checks,'sameLambdaResultants':rprofiles,'bCover':factorinfo,'reports':reports,'excluded':closed,'scope':'only S=0,h=k,2lambda^2=1; lambda=1/2 previously closed','ordinaryISPClaim':False}

report=run_case('lambda_square_half')
signal.alarm(0)
say({'status':'entire_original_S0_equal_values_nonhalf_excluded' if report['excluded'] else 'original_fibers_remain','report':report,'claimExcluded':report['excluded'],'claimWholeS0LayerEmpty':False,'ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
raise SystemExit(0 if report['excluded'] else 2)
