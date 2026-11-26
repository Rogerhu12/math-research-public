#!/usr/bin/env python3
"""New original L0 general w(w-1)!=0 chart, three rational parameters.
Both exceptional w=0 and w=1 faces were already closed separately.
No division by the original P1 coefficient: homogeneous evaluation
and complete original mean resultants retain every zero-leading fiber.
This source works over QQ on the quadratic factor of the original E1/N1 resultant.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx,fmpq_poly
resource.setrlimit(resource.RLIMIT_AS,(12884901888,12884901888))
started=time.perf_counter()
def say(stage,**kw):
 print(json.dumps(dict(stage=stage,elapsedSeconds=round(time.perf_counter()-started,6),**kw),sort_keys=True),flush=True)
def alarm(signum,frame):
 say("source_timeout",claimExcluded=False);raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm);signal.alarm(1800)
ctx=fmpq_mpoly_ctx.get(("rho","lam","w"),"lex")
rp,lp,wp=ctx.gens();zero=ctx.constant(0);unit=ctx.constant(1)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=n if hasattr(n,"to_dict") else ctx.constant(n)
  d=unit if d is None else d
  assert d
  if not n:self.n=zero;self.d=unit;return
  if reduce:
   gg=n.gcd(d);n=n/gg;d=d/gg
  self.n=n;self.d=d
 def __bool__(self):return bool(self.n)
 def __add__(self,o):o=R(o);return R(self.n*o.d+o.n*self.d,self.d*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):o=R(o);return R(self.n*o.n,self.d*o.d)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);return R(self.n*o.d,self.d*o.n)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):
  return R(self.n**n,self.d**n,False) if n>=0 else R(self.d**(-n),self.n**(-n),False)
 def __eq__(self,o):return not (self-R(o))
rho=R(rp);lam=R(lp);w=R(wp)
rr=lam-1-w;A=2*lam*lam-2*lam+1;B=4*lam**3-6*lam*lam+3*lam-1
C=rr*B-A*A;DD=A-rr*rho;NN=B-A*rho;MM=B-2*A*rho+rr*rho*rho;JJ=B-rr*rho*rho
PN=B-3*rr*A+2*rr**3
q=NN/(rho*DD);b=C/(rho*MM);c=DD**3/(NN*MM);a=1-b-c
u=rr/rho;V2=A/rho**2;P0=PN/(2*rho**3);P02=2*P0
f=(4*rr*w*w-2*rr*w-A+2*rr*rr-2*lam*PN)/(4*rho*w*(w-1))
h=1+rho;k=1+rho*q
assert b+c*q==u and b+c*q*q==V2
assert b+c*q**3==B/rho**3
assert (b+c*q**3-3*u*V2+2*u**3)/2==P0
assert a+w+b*h+c*k==lam
assert a+2*w+b*h*h+c*k*k==2*lam*lam
assert a+3*w+b*h**3+c*k**3==4*lam**3
assert C==rho**4*b*c*q*(q-1)**2
assert q-1==MM/(rho*DD) and q+1==JJ/(rho*DD)
units=[rp,lp,wp,wp-1,rr.n,C.n,DD.n,NN.n,MM.n,JJ.n,PN.n]
def strip(po):
 for atom in units:
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   po=po/gg
 return po
for v in [q,b,c,u,V2,P0,f]:
 assert strip(v.d).total_degree()==0
say("original_three_parameter_L0_graph",scope="rho,lambda,w; all original units and moments; w(w-1)!=0",claimExcluded=False)
def tr(p):
 p=list(p)
 while p and not p[-1]:p.pop()
 return p
def cp(v):return tr([R(v)])
def pa(p,z):
 out=[R(0) for _ in range(max(len(p),len(z)))]
 for i in range(len(out)):out[i]=(p[i] if i<len(p) else R(0))+(z[i] if i<len(z) else R(0))
 return tr(out)
def neg(p):return [-v for v in p]
def sub(p,z):return pa(p,neg(z))
def pm(p,z):
 if not p or not z:return []
 out=[R(0) for _ in range(len(p)+len(z)-1)]
 for i,v in enumerate(p):
  for j,wv in enumerate(z):out[i+j]=out[i+j]+v*wv
 return tr(out)
def sc(v,p):return tr([v*x for x in p])
def power(p,n):
 ans=cp(1)
 for _ in range(n):ans=pm(ans,p)
 return ans
tp=[R(0),R(1)];zp=[];one=[cp(1),zp,cp(1),cp(1)]
W1=cp(V2/2-u*u+2*f*u)
W2=[u*V2-2*u**3+f*(V2+2*u*u)+2*lam*P0,-b*c*q]
bx=sc(1/(b*(q-1)),sub(sc(q,W1),W2))
cy=sc(1/(c*q*(q-1)),sub(W2,W1))
rrow=sub(sub(bx,cp(a)),sc(c,tp))
srow=sub(sub(cy,cp(a*q)),sc(b,tp))
Arow=pa(sub(sub(cp(2*f),sc(2*b,bx)),sc(2*c,cy)),sc(2*b*c,tp))
rows=[[zp,zp,cp(1),cp(q)],[zp,Arow,rrow,srow],[cp(1),rrow,zp,tp],[cp(q),srow,tp,zp]]
def va(v,z):return [pa(x,y) for x,y in zip(v,z)]
def vs(v,z):return [pm(v,x) for x in z]
def vm(v,z):return [pm(v[0],z[0]),pa(pm(v[0],z[1]),pm(v[1],z[0])),pm(v[2],z[2]),pm(v[3],z[3])]
def tau(v):return pa(pa(sc(a,v[0]),v[1]),pa(sc(b,v[2]),sc(c,v[3])))
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);assert not sub(F2,cp(2*f))
def P2(v):
 vc=va(v,vs(neg(tau(v)),one))
 return tau(vm(vm(vc,vc),vc))
def Pj(v,z):
 vc=va(v,vs(neg(tau(v)),one));zc=va(z,vs(neg(tau(z)),one))
 return sc(R(3),tau(vm(vm(vc,vc),zc)))
def N4(v):
 ans=sub(sc(R(2),tau(vm(d,vm(v,v)))),pm(F2,tau(vm(v,v))))
 ans=sub(ans,sc(R(4),pm(tau(v),tau(vm(d,v)))))
 return pa(pa(ans,sc(R(2),pm(F2,power(tau(v),2)))),tau(vm(v,DK(v))))
def Nj(v,z):return sub(sub(N4(va(v,z)),N4(v)),N4(z))
ev=[tau(vm(rows[0],rows[0])),sc(R(2),tau(vm(rows[0],rows[1]))),tau(vm(rows[2],rows[2])),tau(vm(rows[3],rows[3]))]
E=va(va(ev,vs(cp(-2),DK(d))),va(vs(cp(-2),vm(d,d)),vs(sc(R(2),F2),d)))
VV=[cp(1),cp(w),cp(h),cp(k)]
assert not E[0] and not sub(P2(rows[0]),cp(P02))
assert not sub(N4(rows[0]),cp(2*lam*P02))
assert not P2(VV) and not N4(VV)
polys=E[1:]+[sub(Pj(rows[0],rows[1]),cp(3*w*P02)),sub(P2(rows[2]),cp(h**3*P02)),sub(P2(rows[3]),cp(k**3*P02)),sub(Nj(rows[0],rows[1]),cp(4*lam*w*P02)),sub(N4(rows[2]),cp(2*lam*h*h*P02)),sub(N4(rows[3]),cp(2*lam*k*k*P02))]
labels=["E1","EB","EC","P1","PB","PC","N1","NB","NC"]
cleared=[]
for label,po in zip(labels,polys):
 den=unit
 for v in po:
  assert strip(v.d).total_degree()==0
  den=den*(v.d/den.gcd(v.d))
 nums=[v.n*(den/v.d) for v in po]
 for atom in units:
  while nums:
   gg=atom
   for num in nums:gg=gg.gcd(num)
   if gg.total_degree()==0:break
   nums=[num/gg for num in nums]
 cleared.append(nums)
 say("all_original_condition",name=label,tDegree=len(nums)-1,coefficientTerms=[len(x.to_dict()) for x in nums],inputSha256=hashlib.sha256("\n".join(map(str,nums)).encode()).hexdigest())
assert len(cleared[3])<=2
alpha=cleared[3][1] if len(cleared[3])==2 else zero
beta=cleared[3][0] if cleared[3] else zero
eqs=[]
if not alpha and beta:eqs.append(("P1_constant",strip(beta)))
for label,co in zip(labels,cleared):
 if label not in ("E1","EB","EC","N1") or not co:continue
 deg=len(co)-1
 val=sum((v*(-beta)**i*alpha**(deg-i) for i,v in enumerate(co)),zero)
 if val:eqs.append(("P1_"+label,strip(val)))
def det(mat):
 n=len(mat)
 if n==0:return unit
 if n==1:return mat[0][0]
 return sum(((-1)**j*mat[0][j]*det([row[:j]+row[j+1:] for row in mat[1:]]) for j in range(n) if mat[0][j]),zero)
def res(p,z):
 if not p or not z:return zero
 n=len(p)-1;m=len(z)-1
 if n==0:return p[0]**m if m else p[0]
 if m==0:return z[0]**n
 mat=[]
 for i in range(m):mat.append([zero]*i+p[::-1]+[zero]*(m-1-i))
 for i in range(n):mat.append([zero]*i+z[::-1]+[zero]*(n-1-i))
 return det(mat)
for i,j in [(0,1),(0,2),(1,2),(0,6),(1,6),(2,6)]:
 val=res(cleared[i],cleared[j])
 if val:eqs.append((labels[i]+"_"+labels[j],strip(val)))
Pi=unit
for atom in units:Pi*=atom
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
for label,po in eqs:
 say("original_no_leading_division_projection",name=label,degrees=list(map(int,po.degrees())),terms=len(po.to_dict()),sha256=hashlib.sha256(str(po).encode()).hexdigest())

# New original branch: the small factor of Res_t(E1,N1).
# Its complementary factor is retained as an unresolved branch elsewhere.
def norm(po):
 return po/next(iter(po.to_dict().values())) if po else po
def rho_co(po,j):
 return ctx.from_dict({(0,int(m[1]),int(m[2])):v for m,v in po.to_dict().items() if int(m[0])==j})
def dr(po):
 return int(po.degrees()[0]) if po else -1
def profile(po):
 return dict(degrees=list(map(int,po.degrees())) if po else [-1,-1,-1],terms=len(po.to_dict()),sha256=hashlib.sha256(str(po).encode()).hexdigest())
Phi=rr.n**2*rp**2-A.n*rr.n*rp-C.n
lookup=dict(eqs)
quotient=lookup["E1_N1"]/Phi
assert quotient*Phi==lookup["E1_N1"]
p0,p1,p2=[rho_co(Phi,j) for j in range(3)]
assert p2==rr.n**2
# R=lambda-1-w=rho*u is already a unit. No new parameter is inverted.
say("original_quadratic_resultant_factor_verified",Phi=str(Phi),profile=profile(Phi),complement=profile(norm(quotient)),complementExcluded=False,claimExcluded=False)
def reduced(po):
 rem=norm(po);steps=0
 while rem and dr(rem)>=2:
  ndeg=dr(rem);lead=rho_co(rem,ndeg)
  old=rem
  raw=p2*old-lead*rp**(ndeg-2)*Phi
  assert dr(raw)<ndeg
  rem=norm(strip(raw));steps+=1
 assert dr(rem)<=1
 return rem,steps
remains=[]
for label in ["P1_E1","P1_EB","P1_EC","P1_N1","E1_EB","E1_EC","EB_EC","EB_N1","EC_N1"]:
 rem,steps=reduced(lookup[label])
 remains.append((label,rem))
 say("original_quadratic_branch_linear_remainder",name=label,pseudoSteps=steps,profile=profile(rem),claimExcluded=False)
projections=[]
for label,rem in remains:
 aa=rho_co(rem,1);bb=rho_co(rem,0)
 val=norm(strip(p0*aa*aa-p1*aa*bb+p2*bb*bb))
 if val:projections.append(("Phi_"+label,val))
for i,j in [(0,1),(0,2),(4,5),(4,6),(4,7),(4,8),(0,4),(0,5)]:
 a1,b1=rho_co(remains[i][1],1),rho_co(remains[i][1],0)
 a2,b2=rho_co(remains[j][1],1),rho_co(remains[j][1],0)
 val=norm(strip(a1*b2-a2*b1))
 if val:projections.append((remains[i][0]+"__"+remains[j][0],val))
for label,po in projections:
 assert not any(int(m[0]) for m in po.to_dict())
 say("original_quadratic_branch_QQ_parameter_projection",name=label,profile=profile(po),claimExcluded=False)
assert projections
# Every finite common original point makes every projection vanish,
# including zero leading coefficients of all original P1/linear remainders.
projections.sort(key=lambda v:(int(v[1].degrees()[2]),int(v[1].total_degree()),len(v[1].to_dict())))
anchor_name,anchor=projections[0]
gg=None;used=[]
for label,po in projections[1:]:
 say("begin_exact_QQ_w_resultant",anchor=anchor_name,other=label,claimExcluded=False)
 res=anchor.resultant(po,"w")
 if not res:
  say("zero_QQ_w_resultant",other=label,claimExcluded=False)
  continue
 assert not any(int(m[0]) or int(m[2]) for m in res.to_dict())
 co={int(m[1]):v for m,v in res.to_dict().items()}
 qq=fmpq_poly([co.get(i,0) for i in range(max(co)+1)])
 if gg is None:gg=qq/qq[int(qq.degree())]
 else:
  nextg,left,right=gg.xgcd(qq)
  assert left*gg+right*qq==nextg
  gg=nextg/nextg[int(nextg.degree())]
 used.append(label)
 say("exact_QQ_w_resultant_and_lambda_gcd",anchor=anchor_name,other=label,resultantDegree=int(qq.degree()),resultantSha256=hashlib.sha256(str(qq).encode()).hexdigest(),gcdDegree=int(gg.degree()),gcdSha256=hashlib.sha256(str(gg).encode()).hexdigest(),gcdPolynomial=str(gg) if len(str(gg))<1800 else None,originalLeadingZeroFibersRetained=True,claimExcluded=gg.degree()==0)
 if gg.degree()==0:break
signal.alarm(0)
say("complete_original_L0_quadratic_factor_branch",sourceSha256=source_sha,usedResultants=used,lambdaGcdDegree=None if gg is None else int(gg.degree()),claimExcluded=gg is not None and gg.degree()==0,complementExcluded=False,ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
