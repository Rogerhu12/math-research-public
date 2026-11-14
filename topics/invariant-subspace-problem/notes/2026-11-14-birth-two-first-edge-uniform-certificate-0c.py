"""Exact full-K2 first/last-edge certificate, two arbitrary ordinary groups plus one bit.
Standalone SymPy rational/integer arithmetic; no imported tables or sampling.
Default runs all complete coefficient polynomials (about four minutes here).
--identities-only checks generic formulas and full 5x5 source calibrations.
"""
import sympy as s,time,sys
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from math import factorial,comb
from itertools import combinations
start=time.time()
g1,g2,g3,g4,F2,F3,F4,E3,E4,Y,chi=s.symbols('g1 g2 g3 g4 F2 F3 F4 E3 E4 Y chi')
a,b,c,d=g1,g2/F2,g3/F3,g4/F4
Q,r,ss=F2,F3/E3,F4/E4
xx=chi*g3*g3/(F2*F2*F3*F3)
yy=chi*Y*Y/(F2*F2*F3*F3*F4*F4)
xy=-chi*g3*Y/(F2*F2*F3*F3*F4)
la=[a*c-b*b,a*d-b*c,b*d-c*c]
ff=[Q*(Q*ss-r*r),Q*r*ss,r*r*ss]
co=[sum(Q*la[i]*ff[k-i]for i in range(3)if 0<=k-i<3)for k in range(5)]
for fac,U,V in [(Q**3*r*xx,[c,d],[r,ss]),(Q*Q*r*r*ss*yy,[a,b],[1,0]),(2*Q*Q*r*ss*xy,[b,c],[Q,r])]:
 for i in range(2):
  for j in range(2):co[i+j+1]-=fac*U[i]*V[j]
co[2]-=Q**3*r*r*ss*xx*yy
vs=[g1,g2,g3,g4,F2,F3,F4,E3,E4,Y,chi];tables={};nums={}
for k in (1,2,3):
 nn,dd=s.fraction(s.cancel(co[k]));pp=s.Poly(nn,*vs);tables[k]=pp.terms()
 assert len(pp.terms())=={1:9,2:14,3:6}[k]
 expected_den=E3**2*E4*F3*F4 if k==1 else E3**2*E4*F2*F3**2*F4 if k==2 else E3**2*E4*F3
 assert s.expand(dd-expected_den)==0
 nums[k]=nn
 print('UNIVERSAL_IDENTITIES_PASS',k,len(pp.terms()),flush=True)

N1=E3*F3*F4**2*(F2**2*g1*g3-F3*g2**2)+F2*(F2*F3*g1*g4-F4*g2*g3)*(F2*F4*E3**2-F3**2*E4)+chi*(2*E3*F4*g2*g3*Y-F2*E4*F4*g3**3-g1*F3*Y**2)
N3=F3**2*(F2*F3*g1*g4-F4*g2*g3)+E3*F2*(F3**2*g2*g4-F2*F4*g3**2)+chi*g3**2*(2*Y-E3*F2*g4)
assert s.expand(nums[1]-N1)==s.expand(nums[3]-N3)==0
assert s.expand(N3.subs(Y,(F2*E3*g4-F4*g3)/2)-(F3**2*(F2*F3*g1*g4-F4*g2*g3)+E3*F2*(F3**2*g2*g4-F2*F4*g3**2)-chi*F4*g3**3))==0
print('COMPACT_NUMERATORS_AND_HARD_ENDPOINT_PASS',flush=True)
weights=[2,4,6,8,4,8,12,6,12,18,5]
for ki in (1,2,3):assert max(sum(a*b for a,b in zip(powers,weights))for powers,_ in tables[ki])=={1:54,2:64,3:38}[ki]
print('PRIOR_TOTAL_DEGREE_BOUNDS_PASS',flush=True)

def calibration(q,L,a0,c0):
 z=a0*a0;w=c0*c0;t=2;D=q-1;Cq=s.Integer(factorial(q)**2)*z**q;C1=q*L*z;C2=(q-1)*(L-1)*z
 def bc(n,k):return comb(n,k)if 0<=k<=n else 0
 def bs(p):return [(r,b,p-r-b)for r in range(q+1)for b in (0,1)if 0<=p-r-b<=L]
 def full(n):
  src=bs(t+n);out=bs(t)
  def coef(o,v):
   ds=[v[i]-o[i]for i in range(3)]
   if min(ds)<0 or sum(ds)!=n:return s.Integer(0)
   return a0**ds[0]*c0**ds[1]*bc(q-o[0],ds[0])*bc(1-o[1],ds[1])*bc(L-o[2],ds[2])
  AA=s.Matrix([[coef(o,v)for v in src]for o in out]);Wi=s.diag(*[s.Rational(1,comb(q,r)*comb(L,l))for r,b,l in src])
  EE=s.Matrix([[(-1)**l*a0**(q-r)*c0**(1-b)*s.Rational(factorial(D)*bc(q-r,D),comb(L,l)),(-1)**l*a0**(q-r)*c0**(1-b)*s.Rational(factorial(D-1)*(1-b)*bc(q-r,D-1),comb(L,l))]for r,b,l in out])
  assert len(out)==5
  HH=EE.T*(AA*Wi*AA.T).inv()*EE;S=s.diag(1,s.sqrt(C2))
  return (C1/Cq)*S*HH*S
 gg=[];ff=[];ee=[]
 for k in range(1,5):
  nu=[s.Integer(bc(q,i)*bc(L,k-i))*z**i for i in range(k+1)]
  mm=[sum(nu[i]*s.Integer(i)**j for i in range(k+1))for j in range(5)]
  gg.append(mm[0]);ff.append(s.det(s.Matrix(2,2,lambda a,b:mm[a+b]))/C1)
  ee.append(s.det(s.Matrix(3,3,lambda a,b:mm[a+b]))/(q*q*(q-1)*L*L*(L-1)*z**3))
 values=gg+ff[1:]+ee[2:]+[(ff[1]*ee[2]*gg[3]-ff[3]*gg[2])/2,C2*(z-1)**2]
 sub=dict(zip(vs,values));Pc=sum(s.cancel(co[k]).subs(sub)*w**k for k in range(5))
 H0,H1,H2=[full(n)for n in (0,1,2)];KK=H0-H1*H2.inv()*H1
 Qc=ff[1];rc=ff[2]/ee[2];sc=ff[3]/ee[3];cc=gg[2]/ff[2];dc=gg[3]/ff[3]
 denom=(Qc+w*rc)**2*(cc+w*dc)*sc/w
 assert s.simplify(Pc-KK.det()*denom)==0 and KK.det()>0
 print('ACTUAL_FIVE_DIMENSIONAL_FULL_INVERSE_PASS',q,L,a0,c0,flush=True)
calibration(4,4,s.Integer(2),s.Integer(3))
calibration(5,4,s.Rational(1,2),s.Integer(2))
if '--identities-only' in sys.argv:
 print('IDENTITIES_ALL_PASS',flush=True);raise SystemExit

R,x,y,u=ring('x,y,u',QQ);q=x+4;L=y+4;z=1+u

def choose(v,k):
 out=R.one
 for i in range(k):out*=v-i
 return out/QQ(factorial(k))
def measure(k):return [choose(q,i)*choose(L,k-i)*z**i for i in range(k+1)]
def hankel(nu,d):
 ans=R.zero
 for inds in combinations(range(len(nu)),d):
  term=R.one
  for a,b in combinations(inds,2):term*=QQ((b-a)**2)
  for i in inds:term*=nu[i]
  ans+=term
 return ans
Gs=[];Fs=[];Es=[];C1=q*L*z;C3=q*q*(q-1)*L*L*(L-1)*z**3
for k in range(1,5):
 nu=measure(k);GG=sum(nu,R.zero);FF=hankel(nu,2).exquo(C1)
 EE=hankel(nu,3).exquo(C3)if k>=2 else R.zero
 Gs.append(GG);Fs.append(FF);Es.append(EE)
 print('BASE',k,'G',len(GG),'F',len(FF),'E',len(EE),flush=True)
assert Fs[0]==Es[1]==R.one
YY=(Fs[1]*Es[2]*Gs[3]-Fs[3]*Gs[2])/2
vals=Gs+Fs[1:]+Es[2:]+[YY,(q-1)*(L-1)*z*u*u]
for name,val in zip(vs,vals):print('VALUE',name,'terms',len(val),'negative',sum(c<0 for c in val.values()),flush=True)
cache={}
def pw(i,k):
 if(i,k)not in cache:cache[i,k]=vals[i]**k
 return cache[i,k]
expected={1:(7714,54,71663616,3,1859069183311872000000),2:(12529,64,859963392,3,21081844538756628480000000),3:(2870,38,248832,3,3688629331968000)}
for k in (1,2,3):
 out=R.zero
 for powers,cf in tables[k]:
  p0=R(QQ.from_sympy(cf))
  for _,i,j in sorted((len(pw(i,j)),i,j)for i,j in enumerate(powers)if j):p0*=pw(i,j)
  out+=p0
 nt,deg,den,mn,anc=expected[k];integer=out*den
 assert len(integer)==nt and max(map(sum,integer))==deg
 assert all(c.denominator==1 and c>0 for c in integer.values())
 assert min(integer.values())==mn and integer.get((0,0,0),QQ.zero)==anc>0
 print('PASS',k,'positive integer terms',nt,'degree',deg,'multiplier',den,'minimum',mn,'constant',anc,'sec',round(time.time()-start,2),flush=True)
print('ALL_PASS: entire finite polynomials, all independent q,L>=4 and z>=1',flush=True)
