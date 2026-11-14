"""Exact certificate: whole K1, second adjacent edge, two groups plus one bit.
Requires SymPy; all arithmetic is rational/integer, with no parameter sampling.
Standalone: no repository imports, temporary data, network, or generated tables.
"""
import sympy as s,time
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from math import factorial
start=time.time()
e,f,g,h,E,F,G,H,X,Y,chi=s.symbols('e f g h E F G H X Y chi')
a,b,c,d=1/e,1/f,1/g,1/h;p,qq,r,ss=e/E,f/F,g/G,h/H
xx=chi*X**2/(e*e*f*f*g*g);yy=chi*Y**2/(f*f*g*g*h*h);xy=-chi*X*Y/(e*f*f*g*g*h);xyxy=xx*yy
la=[a*c-b*b,a*d-b*c,b*d-c*c];ff=[p*qq*(qq*ss-r*r),qq*r*(p*ss-qq*r),r*ss*(p*r-qq*qq)]
co=[sum(qq*la[i]*ff[k-i]for i in range(3)if 0<=k-i<3)for k in range(5)]
for fac,C,D0 in [(p*qq**3*r*xx,[c,d],[r,ss]),(qq*qq*r*r*ss*yy,[a,b],[p,qq]),(2*p*qq*qq*r*ss*xy,[b,c],[qq,r])]:
 for i in range(2):
  for j in range(2):co[i+j+1]-=fac*C[i]*D0[j]
co[2]-=p*qq**3*r*r*ss*xyxy
vs=[e,f,g,h,E,F,G,H,X,Y,chi];tables=[]
for k in [1,2,3]:
 num,den=s.fraction(s.cancel(co[k]));poly=s.Poly(num,*vs);tables.append(poly.terms());print('UNIVERSAL',k,'terms',len(poly.terms()),'positive monomial denominator',den,flush=True)
# Match the manuscript's positive monomial denominators and compact identities.
ns=[s.fraction(s.cancel(co[k])) for k in (1,2,3)]
base=E*F**3*G**2*H*e*g*h
for (num,den),want,n in zip(ns,[base,base*f*g,base],[11,19,11]):
 assert s.expand(den-want)==0
 assert len(s.Poly(num,*vs).terms())==n
N1=(f*f-e*g)*g*h*(F*G*e*h-E*H*f*g)+(f*g-e*h)*e*f*(G*G*f*h-F*H*g*g)+chi*(2*G*X*Y*e*h-F*Y*Y*e*g-H*X*X*f*h)
N3=(f*g-e*h)*g*h*(F*F*e*g-E*G*f*f)+(g*g-f*h)*e*f*(F*G*e*h-E*H*f*g)+chi*(2*F*X*Y*e*h-E*Y*Y*e*g-G*X*X*f*h)
assert s.expand(ns[0][0]-N1)==0
assert s.expand(ns[2][0]-N3)==0
print('MANUSCRIPT_IDENTITIES_PASS: all denominators, 11/19/11 terms, and compact N1/N3',flush=True)

R,x,y,u=ring('x,y,u',QQ);z=1+u;q=x+4;L=y+4

def choose(v,k):
 out=R.one
 for i in range(k):out*=v-i
 return out/QQ(factorial(k))
def coeffs(q,L):
 return [sum((choose(q,r)*choose(L,j-r)*z**r for r in range(j+1)),R.zero)for j in range(5)]
Z=coeffs(q,L);T=coeffs(q-1,L-1);DD=[R.one]+[T[j]**2-T[j-1]*T[j+1]for j in range(1,4)]
vals=[Z[1],Z[2],Z[3],Z[4]]+DD+[(Z[1]*DD[1]-Z[3])/2,(Z[2]*DD[2]-Z[4]*DD[1])/3,q*L*z*u*u]
# These are complete finite polynomials; every subsequent product is expanded exactly.
assert all(c>=0 for v in vals for c in v.values())
cache={}
def pw(i,k):
 if (i,k)not in cache:cache[i,k]=vals[i]**k
 return cache[i,k]
expected={1:(4324,44,2985984,5,10576038020618649600),2:(6930,52,5971968,3,21321292649567197593600),3:(3311,40,497664,5,352534600687288320)}
for k,terms in zip([1,2,3],tables):
 out=R.zero
 for count,(powers,c0)in enumerate(terms):
  p0=R(QQ.from_sympy(c0))
  parts=sorted([(len(pw(i,v)),i,v)for i,v in enumerate(powers)if v])
  for _,i,v in parts:p0*=pw(i,v)
  out+=p0

 nterms,degree,den,mincoef,anchor=expected[k]
 integer=out*den
 assert len(integer)==nterms and max(map(sum,integer))==degree
 assert all(c.denominator==1 and c>0 for c in integer.values())
 assert min(integer.values())==mincoef
 assert integer.get((0,0,0),QQ.zero)==anchor>0
 print('PASS',k,'positive integer coefficients',nterms,'degree',degree,'denominator multiplier',den,'minimum',mincoef,'constant',anchor,flush=True)
print('ALL_PASS: all three middle quartic numerators are strictly positive for x,y,u >= 0; no sampling',round(time.time()-start,2),'seconds',flush=True)

# Independent actual full-inverse calibration of the common source scaling.
from math import comb
qc=Lc=4;zc=s.Rational(4);wc=s.Rational(3,2);Cc=qc*Lc*zc
Zc=[sum(s.Integer(comb(qc,r)*comb(Lc,j-r))*zc**r for r in range(j+1))for j in range(5)]
Pc=[sum(s.Integer(comb(qc-1,r)*comb(Lc-1,j-r))*zc**r for r in range(j+1)if r<=qc-1 and j-r<=Lc-1)for j in range(5)]
Dc=[s.Integer(1)]+[Pc[j]**2-Pc[j-1]*Pc[j+1]for j in range(1,4)]
source=s.Matrix([[0,1],[-1,-1],[1,0]]);scale=s.diag(1,s.sqrt(Cc))
def full_source(n):
 k=n+1;M=s.zeros(3,3)
 for bit in [0,1]:
  for rr in range(max(0,k-bit-Lc),min(qc,k-bit)+1):
   ll=k-bit-rr;vv=s.Integer(comb(qc,rr)*comb(Lc,ll))*zc**rr*wc**bit;ct=s.Matrix([rr,ll,bit]);M+=vv*ct*ct.T
 return scale*(wc*source.T*M.inv()*source)*scale
H1,H2,H3=[full_source(n)for n in [1,2,3]];Kc=H1-H2*H3.inv()*H2
assert Kc.det()>0 and Kc[0,0]>0
ec,fc,gc,hc=Zc[1:5];Ec,Fc,Gc,Hc=Dc
ac,bc,cc,dc=1/ec,1/fc,1/gc,1/hc;pc,Qc,rc,sc=ec/Ec,fc/Fc,gc/Gc,hc/Hc
Xc=(ec*Fc-gc*Ec)/2;Yc=(fc*Gc-hc*Fc)/3
xc=-s.sqrt(Cc)*(zc-1)*Xc/(ec*fc*gc);yc=s.sqrt(Cc)*(zc-1)*Yc/(fc*gc*hc)
Lc0=(ac*cc-bc*bc)+wc*(ac*dc-bc*cc)+wc**2*(bc*dc-cc*cc)
Fc0=pc*Qc*(Qc*sc-rc*rc)+wc*Qc*rc*(pc*sc-Qc*rc)+wc**2*rc*sc*(pc*rc-Qc*Qc)
PV=Qc*Lc0*Fc0-wc*pc*Qc**3*rc*(cc+wc*dc)*(rc+wc*sc)*xc**2-wc*Qc**2*rc**2*sc*(ac+wc*bc)*(pc+wc*Qc)*yc**2-2*wc*pc*Qc**2*rc*sc*(bc+wc*cc)*(Qc+wc*rc)*xc*yc-wc**2*pc*Qc**3*rc**2*sc*xc**2*yc**2
DF=(pc+wc*Qc)*(Qc+wc*rc)**2*(cc+wc*dc)*sc/wc
assert s.cancel(PV-Kc.det()*DF)==0
print('FULL_INVERSE_CALIBRATION_PASS: actual 3x3 inverse, unchanged source, common sqrt(qLz) scaling, and full determinant numerator',flush=True)
