"""Exact whole-K1 third-edge certificate for two groups plus one arbitrary bit.
Requires SymPy only. No repository/temp imports, precomputed tables, or sampling.
Default checks all three complete rational polynomials (about 17 min here).
--outer-only checks N1/N3; N2 also follows the published uniform P2 theorem.
--identities-only checks generic identities and the actual full-inverse calibration.
"""
import sys,time
import sympy as s
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from math import factorial,comb
start=time.time()
e,f,g,h,E,F,G,H,X,Y,chi=s.symbols('e f g h E F G H X Y chi')
a,b,c,d=1/e,1/f,1/g,1/h
p,Q,r,ss=e/E,f/F,g/G,h/H
xx=chi*X**2/(e*e*f*f*g*g)
yy=chi*Y**2/(f*f*g*g*h*h)
xy=-chi*X*Y/(e*f*f*g*g*h)
la=[a*c-b*b,a*d-b*c,b*d-c*c]
ff=[p*Q*(Q*ss-r*r),Q*r*(p*ss-Q*r),r*ss*(p*r-Q*Q)]
co=[sum(Q*la[i]*ff[k-i]for i in range(3)if 0<=k-i<3)for k in range(5)]
for fac,C,D0 in [(p*Q**3*r*xx,[c,d],[r,ss]),(Q*Q*r*r*ss*yy,[a,b],[p,Q]),(2*p*Q*Q*r*ss*xy,[b,c],[Q,r])]:
 for i in range(2):
  for j in range(2):co[i+j+1]-=fac*C[i]*D0[j]
co[2]-=p*Q**3*r*r*ss*xx*yy
vs=[e,f,g,h,E,F,G,H,X,Y,chi]
tables={};nums={}
for k in (1,2,3):
 num,den=s.fraction(s.cancel(co[k]));poly=s.Poly(num,*vs)
 expected_den=E*F**3*G**2*H*e*g*h if k!=2 else E*F**3*G**2*H*e*f*g**2*h
 assert s.expand(den-expected_den)==0
 assert len(poly.terms())==({1:11,2:19,3:11}[k])
 tables[k]=poly.terms();nums[k]=num
N1=(f*f-e*g)*g*h*(F*G*e*h-E*H*f*g)+(f*g-e*h)*e*f*(G*G*f*h-F*H*g*g)+chi*(2*G*X*Y*e*h-F*Y*Y*e*g-H*X*X*f*h)
N3=(f*g-e*h)*g*h*(F*F*e*g-E*G*f*f)+(g*g-f*h)*e*f*(F*G*e*h-E*H*f*g)+chi*(2*F*X*Y*e*h-E*Y*Y*e*g-G*X*X*f*h)
assert s.expand(nums[1]-N1)==s.expand(nums[3]-N3)==0
print('GENERIC_IDENTITIES_PASS: full quartic, 11/19/11 monomials, exact positive denominators, compact N1/N3',flush=True)

# Actual full 3x3 inverse at n=3, before compression, on one common source.
qc=Lc=4;zc=s.Rational(4);wc=s.Rational(3,2);Cc=qc*Lc*zc
bc=lambda n,k:comb(n,k)if 0<=k<=n else 0
Zc=[sum(s.Integer(bc(qc,r)*bc(Lc,j-r))*zc**r for r in range(j+1))for j in range(6)]
Pc=[sum(s.Integer(bc(qc-1,r)*bc(Lc-1,j-r))*zc**r for r in range(j+1))for j in range(6)]
Dc=[s.Integer(1)]+[Pc[j]**2-Pc[j-1]*Pc[j+1]for j in range(1,5)]
source=s.Matrix([[0,1],[-1,-1],[1,0]]);scale=s.diag(1,s.sqrt(Cc))
def full_source(n):
 k=n+1;M=s.zeros(3,3)
 for bit in (0,1):
  for rr in range(max(0,k-bit-Lc),min(qc,k-bit)+1):
   ll=k-bit-rr;vv=s.Integer(bc(qc,rr)*bc(Lc,ll))*zc**rr*wc**bit;ct=s.Matrix([rr,ll,bit]);M+=vv*ct*ct.T
 return scale*(wc*source.T*M.inv()*source)*scale
Hm,H0,Hp=[full_source(n)for n in (2,3,4)]
Kc=Hm-H0*Hp.inv()*H0
assert Kc.det()>0 and Kc[0,0]>0
ec,fc,gc,hc=Zc[2:6];Ec,Fc,Gc,Hc=Dc[1:5]
ac,bc0,cc,dc=1/ec,1/fc,1/gc,1/hc
pc,Qc,rc,sc=ec/Ec,fc/Fc,gc/Gc,hc/Hc
Xc=(ec*Fc-gc*Ec)/3;Yc=(fc*Gc-hc*Fc)/4
xc=-s.sqrt(Cc)*(zc-1)*Xc/(ec*fc*gc);yc=s.sqrt(Cc)*(zc-1)*Yc/(fc*gc*hc)
Lc0=(ac*cc-bc0*bc0)+wc*(ac*dc-bc0*cc)+wc**2*(bc0*dc-cc*cc)
Fc0=pc*Qc*(Qc*sc-rc*rc)+wc*Qc*rc*(pc*sc-Qc*rc)+wc**2*rc*sc*(pc*rc-Qc*Qc)
PV=Qc*Lc0*Fc0-wc*pc*Qc**3*rc*(cc+wc*dc)*(rc+wc*sc)*xc**2-wc*Qc**2*rc**2*sc*(ac+wc*bc0)*(pc+wc*Qc)*yc**2-2*wc*pc*Qc**2*rc*sc*(bc0+wc*cc)*(Qc+wc*rc)*xc*yc-wc**2*pc*Qc**3*rc**2*sc*xc**2*yc**2
DF=(pc+wc*Qc)*(Qc+wc*rc)**2*(cc+wc*dc)*sc/wc
assert s.cancel(PV-Kc.det()*DF)==0
print('FULL_INVERSE_CALIBRATION_PASS: actual 3x3 inverse, fixed source, common sqrt(qLz) scaling, full numerator',flush=True)
if '--identities-only' in sys.argv:
 print('IDENTITIES_ALL_PASS',flush=True);raise SystemExit

R,x,y,u=ring('x,y,u',QQ);z=1+u;q=x+4;L=y+4
def choose(v,k):
 out=R.one
 for i in range(k):out*=v-i
 return out/QQ(factorial(k))
def coeffs(q,L):
 return [sum((choose(q,r)*choose(L,j-r)*z**r for r in range(j+1)),R.zero)for j in range(6)]
Z=coeffs(q,L);T=coeffs(q-1,L-1)
DD=[R.one]+[T[j]**2-T[j-1]*T[j+1]for j in range(1,5)]
vals=[Z[2],Z[3],Z[4],Z[5]]+DD[1:]+[(Z[2]*DD[2]-Z[4]*DD[1])/3,(Z[3]*DD[3]-Z[5]*DD[2])/4,q*L*z*u*u]
# No positivity of individual falling-factorial coefficients is assumed.
cache={}
def pw(i,k):
 if (i,k)not in cache:cache[i,k]=vals[i]**k
 return cache[i,k]
expected={1:(12528,64,1031956070400,7,255855511794806371123200000),2:(20539,76,12383472844800,3,13539873684181153159839744000000),3:(10415,60,85996339200,7,12792775589740318556160000)}
for k in ((1,3)if '--outer-only' in sys.argv else (1,2,3)):
 out=R.zero
 for powers,c0 in tables[k]:
  p0=R(QQ.from_sympy(c0))
  for _,i,v in sorted((len(pw(i,v)),i,v)for i,v in enumerate(powers)if v):p0*=pw(i,v)
  out+=p0
 nterms,degree,den,mincoef,anchor=expected[k];integer=out*den
 assert len(integer)==nterms and max(map(sum,integer))==degree
 assert all(c.denominator==1 and c>0 for c in integer.values())
 assert min(integer.values())==mincoef and integer.get((0,0,0),QQ.zero)==anchor>0
 print('PASS',k,'positive integer terms',nterms,'degree',degree,'multiplier',den,'min',mincoef,'constant',anchor,'sec',round(time.time()-start,2),flush=True)
print('ALL_PASS: entire finite polynomials, no sampling or external tables',round(time.time()-start,2),'seconds',flush=True)
