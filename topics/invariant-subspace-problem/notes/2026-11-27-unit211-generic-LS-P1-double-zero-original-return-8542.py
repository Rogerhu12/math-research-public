#!/usr/bin/env python3
"""R150: complete original generic-LS P1 double-zero exclusion.
Reconstruct the weighted-moment four-parameter chart without dropping ell=0,
T=0 or equal weights; check the original two lines, then return the entire
P1 zero-coefficient branch using a full QQ cover and actual exact certificates.
"""
from pathlib import Path
import time,signal,resource,json,hashlib
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(360);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3));start=time.perf_counter()
def say(stage,**kw):print(json.dumps({'stage':stage,'seconds':time.perf_counter()-start,**kw}),flush=True)
ctx=fmpq_mpoly_ctx.get(('lam','ell','T','theta','f','t'),'lex');la,l,T,th,f,t=ctx.gens();oo=ctx.constant(1);zz=ctx.constant(0)
A=2*la*la-2*la+1;B=4*la**3-6*la*la+3*la-1
D=l*A-T*T;sn=l*B-A*T;zn=T*B-A*A;disc=sn*sn-4*zn*D;Hn=2*T*D-l*sn
assert sn*T-l*zn==A*D and sn*A-zn*T==B*D
assert l*l*disc-Hn*Hn==4*D**3
Un=l*D+th*Hn;Qn=D*D-th*th*disc
Lnum=D-th*sn;Snum=sn+(3-2*la)*D
_paid_rational_atoms=[D,disc,Qn,th]
_paid_rational_checked=set()
_paid_rational_inverse_count=0
def check_rational_unit(pp):
 key=str(sorted(pp.to_dict().items()))
 if key in _paid_rational_checked:return
 assert pp
 original=pp;product=oo
 for atom in _paid_rational_atoms:
  while pp.total_degree()>0:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   qq=pp/gg;assert qq*gg==pp;pp=qq;product*=gg
 assert pp and pp.total_degree()==0 and product*pp==original
 _paid_rational_checked.add(key)

say('global_weighted_moment_coordinate_identities',parameters=['lambda','ell','T','theta'],invertedMomentDeterminant='ell*A-T^2=bc*(h-k)^2',momentIdentities=2,weightDiscriminantIdentity=True,noEllTOrEqualWeightNumeratorInverted=True,profiles={nm:{'degrees':list(map(int,p.degrees())),'terms':len(p.to_dict())} for nm,p in [('D',D),('sn',sn),('zn',zn),('disc',disc),('Hn',Hn),('Qn',Qn)]})
def conv(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  self.n=conv(n);self.d=oo if d is None else conv(d);assert self.d
  if not self.n:self.d=oo;return
  gg=self.n.gcd(self.d);self.n=self.n/gg;self.d=self.d/gg
  cc=self.d.coefficient(0);self.n=self.n/cc;self.d=self.d/cc;check_rational_unit(self.d)
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  gg=self.d.gcd(o.d);a=self.d/gg;b=o.d/gg
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g1=self.n.gcd(o.d);g2=o.n.gcd(self.d)
  return R((self.n/g1)*(o.n/g2),(self.d/g2)*(o.d/g1))
 __rmul__=__mul__
 def inv(self):
  global _paid_rational_inverse_count
  assert self;check_rational_unit(self.n);out=R(self.d,self.n);assert self.n*out.n==self.d*out.d;_paid_rational_inverse_count+=1;return out
 def __truediv__(self,o):return self*R(o).inv()
 def __rtruediv__(self,o):return R(o)*self.inv()
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  out=R(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):o=R(o);return self.n*o.d==o.n*self.d
Delta=R(disc,D*D)
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):o=E(o);return E(self.a*o.a+self.b*o.b*Delta,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def inv(self):
  norm=self.a*self.a-self.b*self.b*Delta;assert norm
  out=E(self.a/norm,-self.b/norm);assert self*out==1;return out
 def __truediv__(self,o):return self*E(o).inv()
 def __rtruediv__(self,o):return E(o)*self.inv()
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  out=E(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
bb=E(R(l,2),R(Hn*D,2*disc));cc=E(R(l,2),-R(Hn*D,2*disc));aa=E(1-l)
p=E(1,th);q=E(1,-th);hh=E(1+R(sn,2*D),fmpq(1,2));kk=E(1+R(sn,2*D),-fmpq(1,2));ww=E(la-1-T)
u=R(Un,D);Q=R(Qn,D*D);s=R(sn,D);z=R(zn,D);bc=R(D**3,disc)
assert bb+cc==l and bb*cc==bc and p*q==Q
assert bb*p+cc*q==u and bb*(hh-1)+cc*(kk-1)==T
assert q*(hh-1)-p*(kk-1)==E(0,R(Lnum,D))
assert hh+kk+1-2*la==R(Snum,D)
one=[E(1),E(),E(1),E(1)]
def va(v,w):return [a+b for a,b in zip(v,w)]
def vs(a,v):return [a*b for b in v]
def vm(v,w):return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def tau(v):return aa*v[0]+v[1]+bb*v[2]+cc*v[3]
V=[E(1),ww,hh,kk]
assert tau(V)==la and tau(vm(V,V))==2*la*la and tau(vm(vm(V,V),V))==4*la**3
say('entire_quadratic_value_and_pairing_reconstruction',bothEmbeddingsRetained=True,momentIdentities=3,weightProductIdentity=True,LAndSIdentities=True)
V2=2*u-l*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
W1=T0/2+2*R(f)*u;W2=u*T0+R(f)*(V2+2*u*u)-bc*Q*R(t)+R(la)*P02
XX=(q*E(W1)-E(W2))/(bb*p*(q-p));YY=(E(W2)-p*E(W1))/(cc*q*(q-p))
rr=XX-aa*p-cc*t;ss=YY-aa*q-bb*t;A1=2*f-2*bb*XX-2*cc*YY+2*E(bc)*t
rows=[[E(),E(),p,q],[E(),A1,rr,ss],[p,rr,E(),E(t)],[q,ss,E(t),E()]]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);assert F2==2*f
say('original_E0_N0_linear_Gram_coordinates_constructed',secondsSoFar=time.perf_counter()-start)
def P2(v):
 cen=va(v,vs(-tau(v),one));return tau(vm(vm(cen,cen),cen))
def Pjet2(v,w):
 cen=va(v,vs(-tau(v),one));wc=va(w,vs(-tau(w),one));return 3*tau(vm(vm(cen,cen),wc))
def N4(v):return 2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
assert P2(rows[0])==P02 and N4(rows[0])==2*la*P02
NV=N4(V);PV=Pjet2(rows[0],rows[1])-3*ww*P02
assert not NV.b and not PV.b
S=s+3-2*la;RR=3-4*la;J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q
A1expected=2*(1-J/Q)*R(f)+(-2*(1-u)*T0+2*R(la)*P02)/Q
assert A1==A1expected
Nf=R(th)*(2*RR*Q-2*z*J)+S*(2*u*Q+(R(th)*s-1)*J)
Nt=bc*S*(R(th)*s-1)*Q
N0=R(th)*z*(-2*(1-u)*T0+2*R(la)*P02)+S*(Q*T0/2+(R(th)*s-1)*((1-u)*T0-R(la)*P02))+2*R(th)*Q*R(la-1-T)*((3-2*la)*u+R(T)+R(th)*(R(A)-l*z))
Pf=T0*(J-Q);Pt=bc*Q*Phi;Pconst=(1-u)*T0*T0+P02*(Q*(l+T)-R(la)*T0)
assert NV.a*R(th)*Q==Nf*R(f)+Nt*R(t)+N0
assert PV.a*Q==3*(Pf*R(f)+Pt*R(t)+Pconst)
smallDelta=Phi*Nf-S*(R(th)*s-1)*T0*(J-Q)
assert Nf*Pt-Nt*Pf==bc*Q*smallDelta
assert smallDelta==2*R(th)*Phi*(RR*Q-z*J)+S*(2*u*Q*Phi+4*(u-1)*(R(th)*s-1)*(J-u*Q))
for name,po in [('Nf',Nf),('Nt',Nt),('N0',N0),('Pf',Pf),('Pt',Pt),('P0',Pconst),('Delta',smallDelta)]:
 say('new_original_linear_coefficient',name=name,numeratorDegrees=list(map(int,po.n.degrees())),numeratorTerms=len(po.n.to_dict()),denominatorDegrees=list(map(int,po.d.degrees())),denominatorTerms=len(po.d.to_dict()),numeratorSha256=hashlib.sha256(str(sorted(po.n.to_dict().items())).encode()).hexdigest())
say('complete_new_original_moment_coordinate_and_line_return',allOriginalIdentities=True,DeltaZeroRetained=True,claimExcluded=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

say("generic_coordinate_unit_trace",checkedPolynomials=len(_paid_rational_checked),inverseMultiplications=_paid_rational_inverse_count,allPaid=True,DeltaNotInverted=True)

# Exact identities forcing the complete original P1 zero-coefficient branch.
aux=fmpq_mpoly_ctx.get(('u','ell','Q'),'lex');au,al,aq=aux.gens()
at0=2*au-al*aq-2*au*au;aj=2*au*(1-au)+al*aq;aphi=at0+4*au-4+aq
assert aj-aq+aphi+4*(au-1)**2==0
assert at0+aq+4*(au-1)==aphi
assert at0==2*(au-1)*(2*al-au)-al*(aq+4*(au-1))
say('original_P1_double_zero_weight_identities',allPolynomialIdentitiesMultipliedBack=True,consequences=['T0=0','Q=-4(u-1)','u=2ell','T=-ell from original constant term'],paidForTheseImplications=['u-1','P0','Q','u'],claimExcluded=False)
ctx=fmpq_mpoly_ctx.get(('lam','ell','f'),'lex');la,l,f=ctx.gens();oo=ctx.constant(1);zz=ctx.constant(0)
A=2*la*la-2*la+1;B=4*la**3-6*la*la+3*la-1
D2=A-l;sn=A+B;W=B+3*A-2*l;Zn=l*B+A*A
Dn=l*sn*sn+4*D2*Zn
H=D2**3-l*(2*l-1)*W**2
Ln=B+2*A-l;Sn=sn+(3-2*la)*D2
assert H.degrees()[1]==4
_paid_rational_atoms=[l,2*l-1,D2,Dn,W,Ln,Sn,la,Zn]
_paid_rational_checked=set()
_paid_rational_inverse_count=0
def check_rational_unit(pp):
 key=str(sorted(pp.to_dict().items()))
 if key in _paid_rational_checked:return
 assert pp
 original=pp;product=oo
 for atom in _paid_rational_atoms:
  while pp.total_degree()>0:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   qq=pp/gg;assert qq*gg==pp;pp=qq;product*=gg
 assert pp and pp.total_degree()==0 and product*pp==original
 _paid_rational_checked.add(key)

def conv(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  self.n=conv(n);self.d=oo if d is None else conv(d);assert self.d
  if not self.n:self.d=oo;return
  gg=self.n.gcd(self.d);self.n=self.n/gg;self.d=self.d/gg
  cc=self.d.coefficient(0);self.n=self.n/cc;self.d=self.d/cc;check_rational_unit(self.d)
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  gg=self.d.gcd(o.d);a=self.d/gg;b=o.d/gg
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g1=self.n.gcd(o.d);g2=o.n.gcd(self.d)
  return R((self.n/g1)*(o.n/g2),(self.d/g2)*(o.d/g1))
 __rmul__=__mul__
 def inv(self):
  global _paid_rational_inverse_count
  assert self;check_rational_unit(self.n);out=R(self.d,self.n);assert self.n*out.n==self.d*out.d;_paid_rational_inverse_count+=1;return out
 def __truediv__(self,o):return self*R(o).inv()
 def __rtruediv__(self,o):return R(o)*self.inv()
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  out=R(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):o=R(o);return self.n*o.d==o.n*self.d

s=R(sn,D2);z=-R(Zn,l*D2);Delta=R(Dn,l*D2*D2);th=-R(D2,W);T=-l;Q=-R(4*D2**3,l*W*W);u=R(2*l);bc=R(l*l*D2**3,Dn)
assert Delta==s*s-4*z
assert Q==1-th*th*Delta
assert Q+4*(2*l-1)==-R(4*H,l*W*W)
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):o=E(o);return E(self.a*o.a+self.b*o.b*Delta,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def inv(self):
  norm=self.a*self.a-self.b*self.b*Delta;assert norm
  out=E(self.a/norm,-self.b/norm);assert self*out==1;return out
 def __truediv__(self,o):return self*E(o).inv()
 def __rtruediv__(self,o):return E(o)*self.inv()
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  out=E(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b

bb=E(R(l,2),-R(l)*(s+2)/(2*Delta));cc=E(R(l,2),R(l)*(s+2)/(2*Delta));aa=E(1-l)
p=E(1,th);q=E(1,-th);hh=E(1+s/2,fmpq(1,2));kk=E(1+s/2,-fmpq(1,2));ww=E(la-1+l)
assert bb+cc==l and bb*cc==bc and p*q==Q
assert bb*p+cc*q==u and bb*(hh-1)+cc*(kk-1)==-l
assert q*(hh-1)-p*(kk-1)==E(0,R(2*Ln,W))
assert hh+kk+1-2*la==R(Sn,D2)
one=[E(1),E(),E(1),E(1)]
def va(v,w):return [a+b for a,b in zip(v,w)]
def vs(a,v):return [a*b for b in v]
def vm(v,w):return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def tau(v):return aa*v[0]+v[1]+bb*v[2]+cc*v[3]
V=[E(1),ww,hh,kk]
assert tau(V)==la and tau(vm(V,V))==2*la*la and tau(vm(vm(V,V),V))==4*la**3
V2=2*u-l*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
S=s+3-2*la;RR=3-4*la;J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q
Nf=th*(2*RR*Q-2*z*J)+S*(2*u*Q+(th*s-1)*J)
Nt=bc*S*(th*s-1)*Q
N0=th*z*(-2*(1-u)*T0+2*R(la)*P02)+S*(Q*T0/2+(th*s-1)*((1-u)*T0-R(la)*P02))+2*th*Q*R(la-1+l)*((3-2*la)*u+R(T)+th*(R(A)-l*z))
assert Nt==R(8*l*D2**5*Sn*Ln,Dn*W**3)
t=-(Nf*R(f)+N0)/Nt
say('P1_identically_zero_two_parameter_geometry',Hdegrees=list(map(int,H.degrees())),Hterms=len(H.to_dict()),tNumeratorDegrees=list(map(int,t.n.degrees())),tTerms=len(t.n.to_dict()),tDenominatorDegrees=list(map(int,t.d.degrees())),sameRootAndMomentsVerified=True)
W1=T0/2+2*R(f)*u;W2=u*T0+R(f)*(V2+2*u*u)-bc*Q*t+R(la)*P02
XX=(q*E(W1)-E(W2))/(bb*p*(q-p));YY=(E(W2)-p*E(W1))/(cc*q*(q-p))
rr=XX-aa*p-cc*E(t);ss=YY-aa*q-bb*E(t);A1=2*f-2*bb*XX-2*cc*YY+2*E(bc)*E(t)
rows=[[E(),E(),p,q],[E(),A1,rr,ss],[p,rr,E(),E(t)],[q,ss,E(t),E()]]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);assert F2==2*f
E0=tau(vm(rows[0],rows[0]))-2*tau(vm(rows[0],d))-2*d[0]*d[0]+2*F2*d[0];assert not E0

def P2(v):
 cen=va(v,vs(-tau(v),one));return tau(vm(vm(cen,cen),cen))
def Pjet2(v,w):
 cen=va(v,vs(-tau(v),one));wc=va(w,vs(-tau(w),one));return 3*tau(vm(vm(cen,cen),wc))
def N4(v):return 2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
def Njet4(v,w):return N4(va(v,w))-N4(v)-N4(w)
assert P2(rows[0])==P02 and N4(rows[0])==2*la*P02
assert not N4(V)
PV=Pjet2(rows[0],rows[1])-3*ww*P02;assert not PV.b
qq=PV.a.n/H;assert qq*H==PV.a.n
say('same_point_original_N_value_and_P1_return',NvalueExactlyZero=True,P1NumeratorOriginalHMultiple=True)
# These eight original equations retain the two embeddings of the same d.
ev=[tau(vm(rows[0],rows[0])),2*tau(vm(rows[0],rows[1])),tau(vm(rows[2],rows[2])),tau(vm(rows[3],rows[3]))]
EE=va(va(ev,vs(-2,DK(d))),va(vs(-2,vm(d,d)),vs(2*F2,d)))
assert not EE[0] and not EE[1].b and EE[3]==E(EE[2].a,-EE[2].b)
N1=Njet4(rows[0],rows[1])-4*la*ww*P02;assert not N1.b
NB=N4(rows[2])-2*la*hh*hh*P02;NC=N4(rows[3])-2*la*kk*kk*P02;assert NC==E(NB.a,-NB.b)
PB=P2(rows[2])-hh**3*P02;PC=P2(rows[3])-kk**3*P02;assert PC==E(PB.a,-PB.b)
raw=[('E1',EE[1].a),('EB_even',EE[2].a),('EB_odd',EE[2].b),('N1',N1.a),('NB_even',NB.a),('NB_odd',NB.b),('PB_even',PB.a),('PB_odd',PB.b)]
# Monic ell division costs only rational content; all parameter leading fibers remain.
ellctx=fmpq_mpoly_ctx.get(('ell','lam','f'),'lex');el,al,fl=ellctx.gens()
def swap(p):return ellctx.from_dict({(int(m[1]),int(m[0]),int(m[2])):a for m,a in p.to_dict().items()})
Hm=swap(H);lc=ellctx.from_dict({(0,int(m[1]),int(m[2])):a for m,a in Hm.to_dict().items() if int(m[0])==4});assert lc==-8;Hm=Hm/(-8)
paid=[l,2*l-1,D2,Dn,W,Ln,Sn,la,Zn]
def check_paid(p):
 original=p;pay=oo
 for atom in paid:
  while p:
   gg=p.gcd(atom)
   if gg.total_degree()==0:break
   rr=p/gg;assert rr*gg==p;p=rr;pay*=gg
 assert p.total_degree()==0 and p and original==p*pay
records=[]
for label,frac in raw:
 check_paid(frac.d);pp=frac.n;prod=oo;hist=[]
 for i,atom in enumerate(paid):
  ct=0
  while pp:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   rr=pp/gg;assert rr*gg==pp;pp=rr;prod*=gg;ct+=1
  if ct:hist.append([i,ct])
 assert pp*prod==frac.n
 po=swap(pp);quo,red=divmod(po,Hm);assert quo*Hm+red==po
 assert not red or int(red.degrees()[0])<4
 say('original_P1_zero_scalar_equation',name=label,degreesOriginal=list(map(int,pp.degrees())),termsOriginal=len(pp.to_dict()),degreesEllMonicRemainder=list(map(int,red.degrees())) if red else None,termsEllMonicRemainder=len(red.to_dict()),paid=hist,denominatorPaid=True,monicEllReturnMultipliedBack=True)
 records.append({'name':label,'poly':[[list(map(int,m)),str(a)] for m,a in red.to_dict().items()]})

say('original_generic_P1_zero_eight_equations_verified',monicEllDegree=4,rawEllLeadingCoefficient=-8,originalScalarRows=8,checkedUnitPolynomials=len(_paid_rational_checked),inverseMultiplications=_paid_rational_inverse_count,claimExcluded=False)
# Two exact original three-row minors acting on the true column (f^2,f,1).
Mctx=ellctx;le,lam0,ff=Mctx.gens();mz=Mctx.constant(0);mo=Mctx.constant(1)
He=Hm
peq=[(rec['name'],Mctx.from_dict({tuple(m):fmpq(a) for m,a in rec['poly']})) for rec in records]
qrows=[]
for label,pp in peq[:4]:
 rr=[Mctx.from_dict({(int(m[0]),int(m[1]),0):aa for m,aa in pp.to_dict().items() if int(m[2])==deg}) for deg in [2,1,0]]
 assert pp==rr[0]*ff*ff+rr[1]*ff+rr[2];qrows.append(rr)
def original_minor(inds):
 a,b,cc=[qrows[i] for i in inds]
 cof=[b[0]*cc[1]-b[1]*cc[0],-(a[0]*cc[1]-a[1]*cc[0]),a[0]*b[1]-a[1]*b[0]]
 dd=sum((cof[i]*qrows[inds[i]][2] for i in range(3)),mz)
 for col in range(3):assert sum((cof[i]*qrows[inds[i]][col] for i in range(3)),mz)==(dd if col==2 else mz)
 qq,rr=divmod(dd,He);assert qq*He+rr==dd and rr and int(rr.degrees()[0])<4
 say('original_three_quadratic_cofactor_parameter_minor',rowIndices=list(inds),rowNames=[peq[i][0] for i in inds],actualCoefficientIdentities=3,trueValueColumn=['f^2','f','1'],degrees=list(map(int,rr.degrees())),terms=len(rr.to_dict()),cofactorSha256=hashlib.sha256('|'.join(str(sorted(pp.to_dict().items())) for pp in cof).encode()).hexdigest(),HMultipleAndOriginalCombinationVerified=True,noFLeadingCoefficientInverted=True,claimExcluded=False)
 return rr
minorC=original_minor((0,2,3));minorS=original_minor((0,1,2))
assert list(map(int,minorC.degrees()))==[3,163,0] and list(map(int,minorS.degrees()))==[3,169,0]
from flint import fmpq_poly,nmod_poly,nmod_mpoly_ctx
full=He.resultant(minorC,'ell');assert full
cs=[fmpq(0)]*(int(full.degrees()[1])+1)
for mm,aa in full.to_dict().items():assert int(mm[0])==int(mm[2])==0;cs[int(mm[1])]=aa
cover=fmpq_poly(cs);assert cover.degree()==559
assert hashlib.sha256(str(cover).encode()).hexdigest()=='de90e5dad9bd6247dfacdb8e3735fe0abde995ff05116b43d5be5272226889bb'
scalar,factors=cover.factor();product=fmpq_poly([scalar])
for pp,n in factors:product*=pp**n
assert product==cover
assert sorted((pp.degree(),int(n)) for pp,n in factors)==[(1,102),(1,300),(2,45),(4,3),(4,3),(43,1)]
C43=next(pp for pp,n in factors if pp.degree()==43)
assert hashlib.sha256(str(C43).encode()).hexdigest()=='b312b9ffb13dd2f4df3b45c2aec07941c82ccabf6bbc29cf11dec73947cee179'
say('complete_original_generic_P1_zero_QQ_cover',fullDegree=559,fullEllDegrees=[4,3],fullSha256=hashlib.sha256(str(cover).encode()).hexdigest(),factors=[{'degree':pp.degree(),'multiplicity':int(n),'sha256':hashlib.sha256(str(pp).encode()).hexdigest(),'polynomial':str(pp) if pp.degree()<5 else None} for pp,n in factors],allFactorAndScalarProductsVerified=True,allEllLeadingZeroFibersRetained=True,claimExcluded=False)
# Only lambda=0 is removed here; all other complete QQ factors are returned.
assert any(pp==fmpq_poly([0,1]) and int(n)==102 for pp,n in factors)
prime=1009;mc=nmod_mpoly_ctx.get(('ell','lam'),ordering='lex',modulus=prime)
def redq(aa):
 den=int(aa.denominator)%prime;assert den;return int(aa.numerator)%prime*pow(den,-1,prime)%prime
def modp(pp,ell_degree):
 out=mc.from_dict({(int(m[0]),int(m[1])):redq(aa) for m,aa in pp.to_dict().items()});assert int(out.degrees()[0])==int(pp.degrees()[0])==ell_degree;return out
Sbar=modp(He,4).resultant(modp(minorS,3),'ell');assert Sbar
cs=[0]*(int(Sbar.degrees()[1])+1)
for mm,aa in Sbar.to_dict().items():assert int(mm[0])==0;cs[int(mm[1])]=int(aa)
Sbar=nmod_poly(cs,prime);Cbar=nmod_poly([redq(aa) for aa in C43],prime)
assert Cbar.degree()==C43.degree()==43 and redq(C43.leading_coefficient())
for aa in C43/C43.leading_coefficient():redq(aa)
gg,ss,tt=Cbar.xgcd(Sbar);assert gg==ss*Cbar+tt*Sbar and gg==1
say('whole_degree43_original_modular_Bezout',prime=prime,actualQQCandidateDegree=43,modCandidateDegree=43,QQLeadingCoefficientModPrime=redq(C43.leading_coefficient()),allMonicQQCoefficientsPrimeIntegral=True,fullEllDegreesQQ=[4,3],fullEllDegreesMod=[4,3],fullResultantModDegree=Sbar.degree(),coefficientDegrees=[ss.degree(),tt.degree()],coefficientSha256=hashlib.sha256((str(ss)+'|'+str(tt)).encode()).hexdigest(),actualBezoutMultipliedBack=True,onlyActualUnivariateQQCoverUsed=True,whole43CandidateExcluded=True,claimExcluded=True)
class FE:
 def __init__(self,field,v=0):
  self.field=field
  if isinstance(v,FE):assert v.field is field;self.p=v.p;return
  pp=v if isinstance(v,fmpq_poly) else fmpq_poly([v])
  self.p=divmod(pp,field.mod)[1]
 def __bool__(self):return bool(self.p)
 def __add__(self,o):o=FE(self.field,o);return FE(self.field,self.p+o.p)
 __radd__=__add__
 def __neg__(self):return FE(self.field,-self.p)
 def __sub__(self,o):return self+-FE(self.field,o)
 def __mul__(self,o):o=FE(self.field,o);return FE(self.field,self.p*o.p)
 __rmul__=__mul__
 def __eq__(self,o):o=FE(self.field,o);return self.p==o.p
 def inv(self):
  assert self
  gg,ss,tt=self.p.xgcd(self.field.mod)
  assert self.p*ss+self.field.mod*tt==gg and gg.degree()==0
  vv=FE(self.field,ss/gg[0]);assert self*vv==1
  self.field.inverses+=1;return vv
class Field:
 def __init__(self,phi):
  self.mod=phi/phi.leading_coefficient();self.inverses=0;self.bezout=0;self.divisions=0
  self.zero=FE(self);self.one=FE(self,1)
 def __call__(self,v=0):return FE(self,v)
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

tr=trim
def quo(pp,qq):
 out,remainder=dividep(pp,qq);assert not remainder;return out
def spec(poly,field):
 terms=poly.to_dict()
 if not terms:return []
 out=[]
 for j0 in range(max(int(m[1]) for m in terms)+1):
  dd={int(m[0]):v for m,v in terms.items() if int(m[1])==j0}
  cs=[fmpq(0)]*(max(dd,default=-1)+1)
  for i,v in dd.items():cs[i]=v
  out.append(field(fmpq_poly(cs)))
 return tr(out)
def fpower(self,n):
 assert n>=0
 out=self.field.one;v=self
 while n:
  if n&1:out=out*v
  v=v*v;n//=2
 return out
FE.__pow__=fpower
FE.__rsub__=lambda self,o:FE(self.field,o)+-self
FE.__truediv__=lambda self,o:self*FE(self.field,o).inv()
FE.__rtruediv__=lambda self,o:FE(self.field,o)*self.inv()



def spec_ell(poly,field):
 terms=poly.to_dict()
 if not terms:return []
 assert all(int(m[2])==0 for m in terms)
 out=[]
 for j0 in range(max(int(m[0]) for m in terms)+1):
  dd={int(m[1]):aa for m,aa in terms.items() if int(m[0])==j0};cs=[fmpq(0)]*(max(dd,default=-1)+1)
  for i,aa in dd.items():cs[i]=aa
  out.append(field(fmpq_poly(cs)))
 return tr(out)
Ae=2*lam0*lam0-2*lam0+1;Be=4*lam0**3-6*lam0*lam0+3*lam0-1
D2e=Ae-le;We=Be+3*Ae-2*le;Zne=le*Be+Ae*Ae;Dne=le*(Ae+Be)**2+4*D2e*Zne;Lne=Be+2*Ae-le;Sne=Ae+Be+(3-2*lam0)*D2e
ell_units=[('ell',le),('u-1',2*le-1),('D2',D2e),('Delta',Dne),('W',We),('L',Lne),('S',Sne),('value_z',Zne)]
raw_pair=peq[0][1].resultant(peq[1][1],'f');assert raw_pair
assert int(peq[0][1].degrees()[2])==int(peq[1][1].degrees()[2])==2
pair_q,pair_r=divmod(raw_pair,He);assert pair_q*He+pair_r==raw_pair
small_count=0
for phi,n in factors:
 if phi.degree()==43 or phi==fmpq_poly([0,1]):continue
 field=Field(phi);hh=spec_ell(He,field);history=[]
 for name,un in ell_units:
  at=spec_ell(un,field)
  assert at,'a paid unit vanished identically; this field would already be excluded'
  while len(hh)>1:
   gg=gcdp(hh,at)
   if len(gg)<=1:break
   hh=quo(hh,gg);history.append([name,len(gg)-1])
 remaining_degree=len(hh)-1
 result=gcdp(hh,spec_ell(pair_r,field));assert len(result)==1 and result[0]==1
 small_count+=1
 say('whole_small_QQ_lambda_field_original_return',fieldPolynomial=[str(aa) for aa in phi],fieldDegree=phi.degree(),fieldSha256=hashlib.sha256(str(phi).encode()).hexdigest(),originalEllDegree=4,onlyPaidEllRootRemovals=history,remainingEllDegree=remaining_degree,finalOriginalInputs=['entire retained H fiber','full Res_f(original E1,original EB_even)'],originalFullFDegrees=[2,2],fResultantHReductionMultipliedBack=True,finalGcd='1',inversesMultipliedBack=field.inverses,divisionsMultipliedBack=field.divisions,bezoutCombinationsMultipliedBack=field.bezout,allEmbeddingsRetained=True,wholeCandidateExcluded=True,claimExcluded=True)
assert small_count==4
signal.alarm(0)
say('complete',scope='entire original three-distinct-value LS-nonzero P1-double-coefficient-zero branch',genericMomentCoordinateChartVerified=True,allOriginalNAndPReturned=True,fullQQProjectionDegree=559,completeHighDegreeCandidate=43,completeSmallFieldDegrees=[4,4,2,1],wholeBranchExcluded=True,generalLSExcluded=False,ordinaryISPClaim=False,sourceSha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
