#!/usr/bin/env python3
"""Original QQ checks for all exceptional elimination curves on the q=-1 regular mean chart."""
import hashlib,json,resource,time
from pathlib import Path
import sympy as S
from flint import fmpq_mpoly_ctx,fmpq
started=time.perf_counter()
u,l,A,r,s,t=S.symbols('u l A r s t');a=1-l;b=(l+u)/2;c=(l-u)/2
one=S.Matrix([1,0,1,1]);K=S.Matrix([[0,0,1,-1],[0,A,r,s],[1,r,0,t],[-1,s,t,0]])
def mul(x,y):return S.Matrix([x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]])
def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
def dk(x):return S.Matrix([tau(mul(K.row(i),x)) for i in range(4)])
d=dk(one);F=tau(d)/2
def P(x):
 z=x-tau(x)*one
 return tau(mul(mul(z,z),z))/2
def N(x):return tau(mul(d-F*one,mul(x,x)))/2-tau(x)*tau(mul(d,x))+F*tau(x)**2+tau(mul(x,dk(x)))/4
evec=S.Matrix([tau(mul(K.row(0),K.row(0))),2*tau(mul(K.row(0),K.row(1))),tau(mul(K.row(2),K.row(2))),tau(mul(K.row(3),K.row(3)))])
E=[S.factor(z) for z in evec-2*dk(d)-2*mul(d,d)+4*F*d]
j=S.symbols('j');pj=P(K.row(0).T+j*K.row(1).T);nj=N(K.row(0).T+j*K.row(1).T)
Ps=[pj.subs(j,0),S.diff(pj,j).subs(j,0),P(K.row(2).T),P(K.row(3).T)]
Ns=[nj.subs(j,0),S.diff(nj,j).subs(j,0),N(K.row(2).T),N(K.row(3).T)]
def eq(x,y):assert S.cancel(x-y)==0
def sf(seq,sub):return [S.factor(z.subs(sub,simultaneous=True)) for z in seq]
X,v,T,w,e=S.symbols('X v T w e')
x=X+(v+1)/2;y=X-(v+1)/2;ff=X/2+u/2+l*v/(4*u)
chart={r:x-a-c*t,s:y+a-b*t,A:2*ff-2*b*x-2*c*y+2*b*c*t}
EC=sf(E,chart);PC=sf(Ps,chart);NC=sf(Ns,chart);eq(EC[0],0)
SP=S.factor(a*PC[0]+PC[1]+b*PC[2]+c*PC[3]-2*(a*NC[0]+NC[1]+b*NC[2]+c*NC[3]))
C0=S.factor(3*PC[0]*NC[1]-2*NC[0]*PC[1])
def ev(expr):
 nu,de=S.fraction(S.factor(expr))
 def cv(poly):
  po=S.Poly(poly,u);assert all(mm[0]%2==0 for mm,co in po.terms())
  return sum(co*e**(mm[0]//2) for mm,co in po.terms())
 return S.factor(cv(nu)/cv(de))
sub={X:T/u,t:w/u}
Ep=S.factor(e*ev((EC[2]+EC[3]).subs(sub,simultaneous=True)))
Em=S.factor(e*ev(((EC[2]-EC[3])/u).subs(sub,simultaneous=True)))
MM=S.factor(e*ev(EC[1].subs(sub,simultaneous=True)))
SS=ev((SP/u).subs(sub,simultaneous=True));CC=ev(C0.subs(sub,simultaneous=True))
D1=-2*l+v-w+1;B=v*v+v*w-w+1;D2=-2*l*(v+1)+B
H=-2*l*l*v-2*l*l+2*l*v*v+l*v-2*l*w+l-w*w
ee=l*(l*v**3-l*v*v-l*v*w*w-l*w*w+w*w)/(D1*D2)
TT=ee+(l*(v-1)*(v+w)-w*w)/(2*D1)
eq(Ep.subs({T:TT,e:ee},simultaneous=True),0)
eq(Em.subs({T:TT,e:ee},simultaneous=True),0)
eq(ee-l*l,l*(2*l-1)*H/(D1*D2))
def nr(ex):return S.fraction(S.factor(ex))[0]
en=nr(ee);known=l*(2*l-1)*D1*D2*en*H
def strip(po,kn):
 assert po!=0 and kn!=0
 while True:
  gg=S.gcd(po,kn)
  if S.total_degree(gg)==0:return S.factor(po)
  quo,rem=S.div(po,gg,l,v,w);assert rem==0;po=quo
def monic(ex,*xs):return S.Poly(ex,*xs,domain=S.QQ).monic().as_expr()
def fiber(ss):
 es=S.factor(ee.subs(ss));ts=S.factor(TT.subs(ss))
 kn=S.prod(nr(z.subs(ss)) for z in [l,2*l-1,D1,D2,en,H])
 vals=[S.factor(ex.subs(ss).subs({T:ts,e:es},simultaneous=True)) for ex in [MM,SS,CC]]
 return vals,[strip(nr(ex),kn) for ex in vals]

# v=0: the two original equations force the already excluded l=1/2.
_,pvs=fiber({v:0})
eq(monic(pvs[0],l,w),l+w/2);eq(monic(pvs[1],l,w),l-w/2-1)

# w=0, including the one remaining rank-two physical Gram candidate.
wv,wp=fiber({w:0})
eq(monic(wp[0],l,v),monic((v-l)*(v*v+1-2*l),l,v))
RW=S.resultant(wp[0],wp[1],l)
eq(monic(RW,v),monic(v*v*(v-1)**2*(v+1)**2*(2*v-1),v))
eq(monic(S.gcd(wp[0].subs(v,-1),wp[1].subs(v,-1)),l),l*l-1)
eq(monic(S.gcd(wp[0].subs(v,S.Rational(1,2)),wp[1].subs(v,S.Rational(1,2))),l),l-S.Rational(1,2))
eq(wv[2].subs({l:-1,v:-1}),S.Rational(27,4))
rankcase={l:1,v:-1,w:0}
eq(ee.subs(rankcase),S.Rational(1,2));eq(TT.subs(rankcase),0)
rankoriginal={l:1,A:0,r:0,s:0,t:0}
prank=sf(Ps,rankoriginal)
eq(prank[1],0);eq(prank[2],0);eq(prank[3],0)
assert S.rem(nr(prank[0]+u/2),u*u-S.Rational(1,2),u)==0

# v+w=0: no allowed root of the exact two-resultant gcd.
_,op=fiber({w:-v})
ro=[S.resultant(op[0],po,l) for po in op[1:]]
eq(monic(S.gcd(*ro),v),v**3*(v+1))

# B=0: retain the quartic fiber instead of deleting it.
wb=-(v*v+1)/(v-1);_,bp=fiber({w:wb})
rb=[S.resultant(bp[0],po,l) for po in bp[1:]]
F4=2*v**4+v*v+1
eq(monic(S.gcd(*rb),v),monic(v**3*(v-1)**10*(v+1)*(v*v+1)**4*F4**4,v))
br=[S.rem(po,F4,v) for po in bp]
gb=S.groebner(br+[F4],l,v,domain=S.QQ)
L2=l*l+l*v**3+l*v*v-l*v/2-l/2-3*v**3/4-v*v/4-v/8+S.Rational(1,8)
assert list(gb)==[L2,F4/2]
eq(gb.reduce(nr(D1.subs(w,wb))**2)[1],0)

# The cubic curves: divide only the nonzero Cramer denominator factors.
Gm=v**3-v*w*w-v*w+v-w*w-w;Gp=v**3-v*w*w+v*w-v-w*w-w
regs=[strip(nr(ex.subs({T:TT,e:ee},simultaneous=True)),known) for ex in [MM,SS,CC]]
ctx=fmpq_mpoly_ctx.get(('l','w','v'),'lex')
def fp(ex):return ctx.from_dict({mm:fmpq(str(co)) for mm,co in S.Poly(ex,l,w,v,domain=S.QQ).terms()})
def rg(po,g):return nr(S.rem(po,g,w))
curve_degrees=[]
for label,g,divisor,wantcounts,wantdegrees,wantgcd in [
 ('minus',Gm,D2,[1,1,4],[93,145],v**25*(v+1)**40*(v*v+1)**4),
 ('plus',Gp,D1,[2,2,4],[67,146],v**17*(v-1)**6*(v+1)**31*F4)]:
 out=[];counts=[]
 for original in regs:
  po=rg(original,g);count=0
  while S.degree(po,l)>=S.degree(divisor,l):
   quo,rem=S.div(po,divisor,l)
   if S.rem(nr(rem),g,w)!=0:break
   po=rg(nr(quo),g);count+=1
  out.append(po);counts.append(count)
 assert counts==wantcounts
 mp,sp,cp,kp=map(fp,out+[g])
 rs=mp.resultant(sp,'l').resultant(kp,'w')
 rc=mp.resultant(cp,'l').resultant(kp,'w')
 dd=[max(mm[2] for mm in po.to_dict()) for po in [rs,rc]]
 assert dd==wantdegrees;curve_degrees.append(dd)
 gg=rs.gcd(rc);ww=fp(wantgcd)
 assert gg/gg.leading_coefficient()==ww/ww.leading_coefficient()

# Gminus: v^2+1=0 gives w=0 or -1; w=0 was completely excluded above.
gmfiber=[S.rem(po.subs(w,-1),v*v+1,v) for po in regs]
gminus=S.groebner(gmfiber+[v*v+1],l,v,domain=S.QQ)
assert list(gminus)==[l+v/2,v*v+1]
eq(gminus.reduce(D2.subs(w,-1)**2)[1],0)

# Gplus: on F4 its first w-root is B=0, already excluded; retain the other.
wo=(v-1)/(v+1)-wb
eq(S.rem(nr(Gp+(v+1)*(w-wb)*(w-wo)),F4,v),0)
eq(S.rem(nr(wo-(-2*v*v+v-1)),F4,v),0)
gpfiber=[nr(S.rem(nr(po.subs(w,wo)),F4,v)) for po in regs]
gplus=S.groebner(gpfiber+[F4],l,v,domain=S.QQ)
Lplus=l*l-2*l*v*v-2*l+3*v*v/2+S.Rational(1,2)
assert list(gplus)==[Lplus,F4/2]
eq(gplus.reduce(nr(D1.subs(w,wo))**2)[1],0)
print(json.dumps({'schema':'r150-unit211-opposite-regular-exceptional-curves-20261126-v1','status':'all_exact_QQ_checks_pass','scope':'p=1,q=-1,regular mean chart; v,w,v+w,B,Gminus,Gplus zero fibers all excluded','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cubicCurveResultantDegrees':curve_degrees,'ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True,default=int))
