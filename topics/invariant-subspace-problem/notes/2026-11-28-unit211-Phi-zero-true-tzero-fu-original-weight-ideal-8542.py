#!/usr/bin/env python3
"""NEW true Phi=0, t=0, f=u original three-quadratic necessary weight ideal.

No withdrawn Rbar or head is used.  The free-A1 original jet identity is
SHA256 5d074fb01bab7ae4e3428730aa16d9173465f05f94d71a0aadd48e4d0aedfe87.
The weighted/odd original means are from the corrected seven-variable
certificate a7f1db4305a58c2e733c573158f746d5b4adc312090472de25e472c96ddfeaae.
This new input does NOT repeat either certificate or the four-head test.
"""
import hashlib,itertools,json,resource,signal,time
from flint import fmpq_mpoly_ctx
began=time.perf_counter()
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
ctx=fmpq_mpoly_ctx.get(('u','Q'),'lex')
u,Q=ctx.gens();Z=ctx.constant(0);ONE=ctx.constant(1)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw,sort_keys=True),flush=True)
def sha(p):return hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()
def info(p,small=False):
 ans={'degrees':list(map(int,p.degrees())) if p else [-1,-1],
      'terms':len(p.to_dict()),'sha256':sha(p)}
 if small and len(p.to_dict())<=45:ans['polynomial']=str(p)
 return ans
def const(x):return x if hasattr(x,'to_dict') else ctx.constant(x)
def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 return trim([(a[i] if i<len(a) else Z)+(b[i] if i<len(b) else Z)
              for i in range(max(len(a),len(b)))])
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def scale(a,p):return trim([x*const(p) for x in a])
def mul(a,b):
 out=[Z for _ in range(max(0,len(a)+len(b)-1))]
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return trim(out)
def psum(*items):
 out=[]
 for item in items:out=add(out,item)
 return out
def eq(a,b):return not sub(a,b)
def as3(a):assert len(a)<=3;return a+[Z]*(3-len(a))
def det3(a):
 return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
exact_divisions=0
def dex(a,b):
 global exact_divisions
 q,r=divmod(a,b);assert not r and q*b==a
 exact_divisions+=1
 return q

s=u-1;delta=1-Q
K=Q+4*s;L=Q-2*s*(u-2)
Mn=2*u*L-L*L-u*u*Q
mnum=u*Q-L
A=4*s*s-Q
paid=Q*delta*s*K*L*Mn
# Original Phi P1 with f=u, not a highest-term specialization:
# T = Tnum/(2*L*Q), Tnum = -2*L^2-2*L*K*lambda-K*A.
Tnum=[-2*L*L-K*A,-2*L*K]
A2=[ONE,-2*ONE,2*ONE]
lam=[Z,ONE];two_lam_minus_one=[-ONE,2*ONE]
# Complete free-A1 t=0 jet cancellation on f=u:
# A2-2*ell*lambda-(2*lambda-1)*T=0, ell=L/Q.
jet=psum(scale(A2,2*L*Q),scale(lam,-4*L*L),
          neg(mul(two_lam_minus_one,Tnum)))
assert jet==[2*L*Q-2*L*L-K*A,
 -2*L*(3*Q+4*s)+2*K*A,8*L*(Q+2*s)]
# True E0/N0 gives QV=J*u-G, J=Q-4*s^2.
vn=[Q*(2*u-1)-4*s**3,-2*s*L]
nn=sub([Q*(-K+4*u*u)],scale(vn,2))
Snum=sub(scale(vn,2*L*delta),scale(nn,mnum))
Dnum=add(scale(vn,-2*mnum),scale(nn,L))
# Precisely Q times the original W4, and Q^2*(1-Q) times Obar:
weighted=psum([-2*Q*Mn*L*K],scale(mul(vn,vn),-4*L*delta),
 scale(mul(nn,nn),-L),scale(mul(vn,nn),4*mnum),
 scale(vn,8*Q*Mn*u))
odd=psum([2*Q*Mn*Mn*(Q-L)*s-4*Q*Q*Mn*Mn*u],
 scale(Snum,Q*Mn),scale(vn,2*Q*Mn*Mn),
 scale(Dnum,Q*Mn*(u+1)),neg(mul(Snum,Dnum)))
# Needed later only as the actual D numerator, not inverted or imposed here:
physical_D_numerator=sub(scale(A2,4*L**3*Q),mul(Tnum,Tnum))
original=[as3(weighted),as3(odd),as3(jet)]
say('true_tzero_fu_original_three_quadratics',
 originalLambdaDegrees=[len(trim(x))-1 for x in original],
 exactOriginalScales=['Q*W4','Q^2*(1-Q)*Obar','2*L*Q*(A2-2*ell*lambda-(2*lambda-1)*T)'],
 usesCorrectedTrueGerm=True,oldHeadOrWeightExclusionUsed=False,
 actualPaidProduct=info(paid),DNotInverted=True,
 originalPhysicalDNumeratorCoefficients=[info(p) for p in physical_D_numerator])
# A polynomial lambda content is only removed if all of it is a true paid
# weight divisor; every coefficient is multiplied back.
rows=[];removed_contents=[]
for row in original:
 content=Z
 for p in row:
  if p:content=p if not content else content.gcd(p)
 removed=ONE;current=list(row)
 while content and int(content.total_degree())>0:
  g=content.gcd(paid)
  if int(g.total_degree())<=0:break
  current=[dex(p,g) if p else Z for p in current]
  removed=removed*g;content=dex(content,g)
 assert all(removed*current[i]==row[i] for i in range(3))
 rows.append(current);removed_contents.append(info(removed,True))
say('only_true_weight_contents_removed',removedContents=removed_contents,
 resultingCoefficients=[[info(c) for c in row] for row in rows],
 noLambdaHeadInverted=True,allLambdaDegreeDropsKept=True)
# Four pure-weight elements of the ORIGINAL three-lambda-polynomial ideal.
# The determinant uses the exact first adjugate row.
h=det3(rows)
# Explicit cofactor signs, avoiding cyclic-row orientation conventions.
hcoeff=[rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1],
        rows[0][2]*rows[2][1]-rows[0][1]*rows[2][2],
        rows[0][1]*rows[1][2]-rows[0][2]*rows[1][1]]
assert eq(psum(*(scale(rows[i],hcoeff[i]) for i in range(3))),[h])
necessary=[h];conic_records=[]
for i,j in itertools.combinations(range(3),2):
 a,b=rows[i],rows[j]
 c0=a[1]*b[2]-a[2]*b[1]
 c1=a[2]*b[0]-a[0]*b[2]
 c2=a[0]*b[1]-a[1]*b[0]
 l1=sub(scale(b,a[2]),scale(a,b[2]))
 l2=sub(scale(a,b[1]),scale(b,a[1]))
 assert eq(l1,[c1,-c0]) and eq(l2,[c2,Z,-c0])
 f=c0*c2-c1*c1
 returned=sub(scale(l2,c0),mul([c1,c0],l1))
 assert eq(returned,[f])
 necessary.append(f);conic_records.append({'rows':[i,j],**info(f)})
say('four_pure_weight_original_ideal_rows',
 determinant=info(h),threeConics=conic_records,
 allFourCompleteOriginalLambdaPolynomialIdentitiesReturned=True)
# Exact two-variable Buchberger in the paid localization.  Every row update
# and every division by a TRUE paid factor is an exact polynomial return.
# This is a new ideal, not an old resultant or a modular emptiness test.
dag=[];raw_update_returns=0
def term(exponent,coefficient=1):
 return ctx.from_dict({tuple(exponent):coefficient})
def leading(p):
 dic=p.to_dict();e=max(dic);return tuple(e),dic[e]
def monomial_divides(a,b):return all(a[i]<=b[i] for i in range(2))
def strip_paid(p,parent):
 if not p:return p,parent
 while int(p.total_degree())>0:
  g=p.gcd(paid)
  if int(g.total_degree())<=0:break
  q=dex(p,g)
  dag.append({'op':'true_paid_division','parent':parent,
              'divisorSHA256':sha(g),'valueSHA256':sha(q)})
  p=q;parent=len(dag)-1
 if p:
  lc=leading(p)[1];q=p/lc;assert q*lc==p
  dag.append({'op':'rational_number_normalization','parent':parent,
              'constant':str(lc),'valueSHA256':sha(q)})
  p=q;parent=len(dag)-1
 return p,parent
basis=[];basis_nodes=[]
def reduced(p,node):
 global raw_update_returns
 r=Z;current=p;qs=[Z for _ in basis]
 while current:
  ep,cp=leading(current);found=False
  for i,g in enumerate(basis):
   eg,cg=leading(g)
   if monomial_divides(eg,ep):
    mult=term([ep[k]-eg[k] for k in range(2)],cp/cg)
    new=current-mult*g
    assert new+mult*g==current
    qs[i]=qs[i]+mult;current=new;found=True
    raw_update_returns+=1;break
  if not found:
   t=term(ep,cp);r=r+t;current=current-t
 rebuilt=r
 for q,g in zip(qs,basis):rebuilt=rebuilt+q*g
 assert rebuilt==p
 dag.append({'op':'full_basis_remainder','parent':node,
   'basisParents':list(basis_nodes),
   'quotientSHA256':[sha(q) for q in qs],'valueSHA256':sha(r)})
 return r,len(dag)-1
def insert(p,node):
 p,node=strip_paid(p,node)
 if p:p,node=reduced(p,node)
 p,node=strip_paid(p,node)
 if not p:return None
 basis.append(p);basis_nodes.append(node)
 return len(basis)-1
for i,p in enumerate(necessary):
 dag.append({'op':'original_determinant_or_conic','input':i,'valueSHA256':sha(p)})
 insert(p,len(dag)-1)
unit=any(int(p.total_degree())==0 for p in basis)
pairs=set(itertools.combinations(range(len(basis)),2));processed=0
while pairs and not unit:
 def priority(ij):
  a=leading(basis[ij[0]])[0];b=leading(basis[ij[1]])[0]
  c=tuple(max(a[k],b[k]) for k in range(2))
  return (sum(c),c,ij)
 i,j=min(pairs,key=priority);pairs.remove((i,j));processed+=1
 ei,ci=leading(basis[i]);ej,cj=leading(basis[j])
 # Buchberger's relatively-prime leading-monomial criterion.
 if all(min(ei[k],ej[k])==0 for k in range(2)):continue
 lcm=tuple(max(ei[k],ej[k]) for k in range(2))
 aa=term([lcm[k]-ei[k] for k in range(2)],1/ci)
 bb=term([lcm[k]-ej[k] for k in range(2)],1/cj)
 sp=aa*basis[i]-bb*basis[j]
 assert sp+bb*basis[j]==aa*basis[i]
 dag.append({'op':'original_S_pair','parents':[basis_nodes[i],basis_nodes[j]],
  'leftSHA256':sha(aa),'rightSHA256':sha(bb),'valueSHA256':sha(sp)})
 oldlen=len(basis);idx=insert(sp,len(dag)-1)
 if idx is not None:
  unit=int(basis[idx].total_degree())==0
  for k in range(oldlen):pairs.add((k,idx))
  say('new_true_tzero_weight_ideal_row',basisSize=len(basis),
      value=info(basis[idx],True),processedPairs=processed,
      exactRowUpdates=raw_update_returns,unitReturned=unit)
  if len(basis)>=96 and not unit:
   say('new_true_tzero_weight_ideal_size_boundary',basisSize=len(basis),
       remainingPairs=len(pairs),originalBranchExcluded=False)
   break
say('true_tzero_fu_weight_ideal_final',
 necessaryOnly=True,wholeTzeroFuExcluded=unit,
 completedBuchberger=not pairs or unit,
 retainedBasis=[info(p,True) for p in basis] if not unit else [],
 basisSize=len(basis),processedPairs=processed,
 actualDAGNodes=len(dag),dagSHA256=hashlib.sha256(json.dumps(dag,sort_keys=True).encode()).hexdigest(),
 everyOriginalIdentityAndPaidDivisionReturned=True,
 exactDivisions=exact_divisions,exactRowUpdates=raw_update_returns,
 allOriginalHeadsAndWeightZeroFibersKeptExceptDeclaredPhysicalUnits=True,
 actualPhysicalDNotUsedForExclusion=True,originalPhiExcluded=False,
 ordinaryISPClaim=False)
