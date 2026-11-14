"""Exact whole-K2 second/penultimate-edge certificate, all two-group multiplicities.
Standalone: SymPy generates only the small input polynomials; exact bounded signed
integer encoding expands the entire large numerator. No data files or sampling.
--identities-only checks universal formulas and the full physical inverse.
"""
import sympy as s,time,sys
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from math import factorial,comb
from itertools import combinations
start=time.time()
g2,g3,g4,g5,F2,F3,F4,F5,E3,E4,E5,X,Y,chi=s.symbols('g2 g3 g4 g5 F2 F3 F4 F5 E3 E4 E5 X Y chi')
a,b,c,d=g2/F2,g3/F3,g4/F4,g5/F5
p,Q,r,ss=F2,F3/E3,F4/E4,F5/E5
xx=chi*X*X/(F2*F2*F3*F3*F4*F4)
yy=chi*Y*Y/(F3*F3*F4*F4*F5*F5)
xy=-chi*X*Y/(F2*F3*F3*F4*F4*F5)
la=[a*c-b*b,a*d-b*c,b*d-c*c]
ff=[p*Q*(Q*ss-r*r),Q*r*(p*ss-Q*r),r*ss*(p*r-Q*Q)]
co=[sum(Q*la[i]*ff[k-i]for i in range(3)if 0<=k-i<3)for k in range(5)]
for fac,U,V in [(p*Q**3*r*xx,[c,d],[r,ss]),(Q*Q*r*r*ss*yy,[a,b],[p,Q]),(2*p*Q*Q*r*ss*xy,[b,c],[Q,r])]:
 for i in range(2):
  for j in range(2):co[i+j+1]-=fac*U[i]*V[j]
co[2]-=p*Q**3*r*r*ss*xx*yy
vs=[g2,g3,g4,g5,F2,F3,F4,F5,E3,E4,E5,X,Y,chi];tables={}
for k in (1,3,2):
 nn,dd=s.fraction(s.cancel(co[k]));pp=s.Poly(nn,*vs);tables[k]=pp.terms()
 assert len(pp.terms())=={1:11,2:19,3:11}[k]
 expected_den=E3**3*E4**2*E5*F2*F4*F5 if k!=2 else E3**3*E4**2*E5*F2*F3*F4**2*F5
 assert s.expand(dd-expected_den)==0
 print('UNIVERSAL_IDENTITIES_PASS',k,len(pp.terms()),flush=True)

weights=[4,6,8,10,4,8,12,16,6,12,18,18,30,5]
for ki in (1,2,3):assert max(sum(a*b for a,b in zip(powers,weights))for powers,_ in tables[ki])=={1:94,2:112,3:90}[ki]
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
 for k in range(2,6):
  nu=[s.Integer(bc(q,i)*bc(L,k-i))*z**i for i in range(k+1)]
  mm=[sum(nu[i]*s.Integer(i)**j for i in range(k+1))for j in range(5)]
  gg.append(mm[0]);ff.append(s.det(s.Matrix(2,2,lambda a,b:mm[a+b]))/C1)
  ee.append(s.det(s.Matrix(3,3,lambda a,b:mm[a+b]))/(q*q*(q-1)*L*L*(L-1)*z**3))
 values=gg+ff+ee[1:]+[(gg[2]*ee[1]*ff[0]-gg[1]*ff[2])/2,(gg[3]*ee[2]*ff[1]-gg[2]*ee[1]*ff[3])/3,C2*(z-1)**2]
 sub=dict(zip(vs,values));Pc=sum(s.cancel(co[k]).subs(sub)*w**k for k in range(5))
 H1,H2,H3=[full(n)for n in (1,2,3)];KK=H1-H2*H3.inv()*H2
 pc=ff[0];Qc=ff[1]/ee[1];rc=ff[2]/ee[2];sc=ff[3]/ee[3];cc=gg[2]/ff[2];dc=gg[3]/ff[3]
 denom=(pc+w*Qc)*(Qc+w*rc)**2*(cc+w*dc)*sc/w
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
for k in range(2,6):
 nu=measure(k);GG=sum(nu,R.zero);FF=hankel(nu,2).exquo(C1);EE=hankel(nu,3).exquo(C3)
 Gs.append(GG);Fs.append(FF);Es.append(EE)
 print('BASE',k,'G',len(GG),'F',len(FF),'E',len(EE),flush=True)
assert Es[0]==R.one
XX=(Gs[2]*Es[1]*Fs[0]-Gs[1]*Fs[2])/2
YY=(Gs[3]*Es[2]*Fs[1]-Gs[2]*Es[1]*Fs[3])/3
vals=Gs+Fs+Es[1:]+[XX,YY,(q-1)*(L-1)*z*u*u]
for name,val in zip(vs,vals):print('VALUE',name,'terms',len(val),'negative',sum(c<0 for c in val.values()),flush=True)

"""Exact signed multivariate polynomial arithmetic via bounded integer encoding.
Input: QQ polynomial elements in three variables and a finite monomial expression.
Output coefficients are integers, divided by the returned common denominator.
No approximate evaluation or interpolation is used.
"""
from math import lcm,prod
from fractions import Fraction
import time

def encoded_polynomial(vals,terms,progress=print):
 start=time.time();ds=[];iv=[];degrees=[];l1=[]
 for v in vals:
  di=lcm(*(int(c.denominator)for c in v.values()))if v else 1
  vi={mon:int(c*di)for mon,c in v.items()}
  ds.append(di);iv.append(vi);l1.append(sum(abs(c)for c in vi.values()))
  degrees.append(tuple(max((mon[j]for mon in vi),default=0)for j in range(3)))
 denom_terms=[]
 for powers,cf in terms:
  cf=Fraction(int(cf.p),int(cf.q))
  denom_terms.append(cf.denominator*prod(ds[i]**p for i,p in enumerate(powers)))
 denominator=lcm(*denom_terms)
 coeffs=[]
 for (powers,cf),dt in zip(terms,denom_terms):coeffs.append(int(cf.p)*(denominator//dt))
 bound=sum(abs(cf)*prod(l1[i]**p for i,p in enumerate(powers))for (powers,_),cf in zip(terms,coeffs))
 width=(bound.bit_length()+2+7)//8;bits=8*width;radix=1<<bits
 limits=[max(sum(p*degrees[i][j]for i,p in enumerate(powers))for powers,_ in terms)for j in range(3)]
 sx=limits[0]+1;sy=limits[1]+1;slots=sx*sy*(limits[2]+1)
 progress('ENCODING',limits,'coefficient_bytes',width,'slots',slots,'bound_bits',bound.bit_length(),flush=True)
 packed=[]
 for vi in iv:
  packed.append(sum(c << (bits*(mon[0]+sx*(mon[1]+sy*mon[2])))for mon,c in vi.items()))
 cache={};total=0
 for j,((powers,_),cf)in enumerate(zip(terms,coeffs)):
  parts=[]
  for i,p in enumerate(powers):
   if p:
    if(i,p)not in cache:cache[i,p]=pow(packed[i],p)
    parts.append(cache[i,p])
  parts.sort(key=lambda a:abs(a).bit_length())
  value=cf
  for part in parts:value*=part
  total+=value
  progress('TERM',j,'seconds',round(time.time()-start,2),flush=True)
 raw=total.to_bytes(slots*width+1,'little',signed=True);data=memoryview(raw)
 carry=0;out={}
 for pos in range(slots):
  val=int.from_bytes(data[pos*width:(pos+1)*width],'little')+carry
  if val>=radix//2:val-=radix;carry=1
  else:carry=0
  assert abs(val)<=bound
  if val:
   xx=pos%sx;yy=(pos//sx)%sy;uu=pos//(sx*sy)
   out[xx,yy,uu]=val
 assert carry==int(total<0)
 progress('DECODED','terms',len(out),'negative',sum(c<0 for c in out.values()),'seconds',round(time.time()-start,2),flush=True)
 return out,denominator


# Exercise both borrow propagation and a negative leading coefficient independently.
for sign in (1,-1):
 vv=[x-1,y+2,u-3];out,den=encoded_polynomial(vv,[((1,1,1),s.Integer(sign))],progress=lambda *a,**k:None)
 assert out==dict(sign*(x-1)*(y+2)*(u-3)*den)
print('SIGNED_DECODING_PASS',flush=True)
expected={1:(38017,94,128391846454886400,5,131145938506697234448384000000000000),2:(63358,112,36976851779007283200,3,694024306577441764700848128000000000000000),3:(33504,90,21398641075814400,5,10928828208891436204032000000000000)}
for ki in (1,3,2):
 out,den=encoded_polynomial(vals,tables[ki]);nt,deg,mult,mn,anc=expected[ki]
 assert len(out)==nt and max(map(sum,out))==deg and all(v>0 for v in out.values())
 assert all((v*mult)%den==0 for v in out.values())
 integer={mon:(v*mult)//den for mon,v in out.items()}
 assert min(integer.values())==mn and integer.get((0,0,0),0)==anc>0
 print('PASS',ki,'positive integer terms',nt,'degree',deg,'multiplier',mult,'minimum',mn,'constant',anc,flush=True)
print('ALL_PASS: all independent q,L>=4 and z>=1; exact full signed coefficient decoding',flush=True)
