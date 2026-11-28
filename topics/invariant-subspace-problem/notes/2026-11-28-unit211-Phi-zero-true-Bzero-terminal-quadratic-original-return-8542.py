#!/usr/bin/env python3
"""NEW complete QQ quadratic factor of the true B terminal cover.
phi(x)=2*x^2+4*x-1.  Reconstruct only necessary original definitions,
specialize the full two-dimensional QQ field, then form original lambda
cofactors and their actual Bezout gcd.  If needed, keep the full monic
lambda quotient and monic omega quadratic, including all nilpotents,
and return a positive (lambda*t*Dval)^n target in the original ideal.
No old C76/C315 computation, large factor, norm inverse, or D inverse.
120 seconds / 1 GiB, small receipts only.
"""
import hashlib,itertools,json,math,os,pathlib,resource,signal,time
from flint import fmpq,fmpq_mat
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
RAW_ALARM=signal.alarm
def bounded_alarm(seconds):
 if seconds<=0:return RAW_ALARM(0)
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute boundary')
 return RAW_ALARM(max(1,min(int(seconds),math.ceil(DEADLINE-time.perf_counter()))))
signal.alarm=bounded_alarm;signal.alarm(120)
BASENAME='2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542.py'
BASE_SHA='b802d6c9b7a46b544f1fd5f814b05337a552f938a660b8d047fe4e62ff4eae56'
path=pathlib.Path(__file__).with_name(BASENAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASENAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
MARKER='newValues=[];quotients=[]';assert full.count(MARKER)==1
prefix=full[:full.index(MARKER)]
env={'__name__':'isp_B_original_definitions_for_new_QQ2',
     '__file__':str(path),'print':lambda *a,**kw:None}
exec(compile(prefix,str(path)+'#necessary_definitions','exec'),env)
signal.alarm=bounded_alarm;signal.alarm(120)
stats={'quadraticWholeInverses':0,'lambdaShortDivisions':0,
       'lambdaBezoutReturns':0,'originalCofactorCoordinates':0,
       'originalRowsReturned':0,'omegaProductReturns':0,
       'selectedMatrixInverseCoordinates':0,'targetCoordinates':0}
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute boundary')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
# x^2=-2x+1/2.  Its discriminant 24 is not a rational square.
# The conjugation x -> -2-x is the full quadratic algebra involution.
# Every used inverse is explicitly returned on the complete two coordinates.
class K:
 def __init__(self,a=0,b=0):
  if isinstance(a,K):self.a=a.a;self.b=a.b
  else:self.a=fmpq(a);self.b=fmpq(b)
 def __bool__(self):return bool(self.a or self.b)
 def __add__(self,o):o=K(o);return K(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return K(-self.a,-self.b)
 def __sub__(self,o):return self+-K(o)
 def __rsub__(self,o):return K(o)+-self
 def __mul__(self,o):
  o=K(o);bd=self.b*o.b
  return K(self.a*o.a+bd/2,self.a*o.b+self.b*o.a-2*bd)
 __rmul__=__mul__
 def inverse(self):
  assert self
  norm=self.a*self.a-2*self.a*self.b-self.b*self.b/2
  assert norm,('nonunit whole QQ quadratic element',str(self.a),str(self.b))
  ans=K((self.a-2*self.b)/norm,-self.b/norm)
  assert self*ans==K(1) and ans*self==K(1)
  stats['quadraticWholeInverses']+=1;return ans
 def __truediv__(self,o):return self*K(o).inverse()
 def __eq__(self,o):o=K(o);return self.a==o.a and self.b==o.b
 def pair(self):return [str(self.a),str(self.b)]
K0=K();K1=K(1);X=K(0,1)
assert 2*X*X+4*X-1==0
def trim(p):
 p=p[:]
 while p and not p[-1]:p.pop()
 return p
def padd(a,b):
 return trim([(a[i] if i<len(a) else K0)+(b[i] if i<len(b) else K0)
              for i in range(max(len(a),len(b)))])
def pneg(a):return [-v for v in a]
def psub(a,b):return padd(a,pneg(b))
def pscale(a,c):return trim([v*c for v in a])
def pmul(a,b):
 if not a or not b:return []
 out=[K0 for _ in range(len(a)+len(b)-1)]
 for i,v in enumerate(a):
  for j,w in enumerate(b):out[i+j]=out[i+j]+v*w
 return trim(out)
def pdiv(a,b):
 assert b;a=trim(a);rem=a[:];quot=[K0 for _ in range(max(0,len(a)-len(b)+1))]
 inv=b[-1].inverse()
 while rem and len(rem)>=len(b):
  k=len(rem)-len(b);c=rem[-1]*inv;quot[k]=quot[k]+c
  rem=psub(rem,[K0]*k+pscale(b,c))
 quot=trim(quot)
 assert not psub(a,padd(pmul(quot,b),rem))
 assert not rem or len(rem)<len(b)
 stats['lambdaShortDivisions']+=1
 return quot,rem
def pxgcd(a,b):
 r0,r1=trim(a),trim(b);s0,s1=[K1],[];t0,t1=[],[K1]
 while r1:
  tick();q,r=pdiv(r0,r1)
  r0,r1=r1,r;s0,s1=s1,psub(s0,pmul(q,s1));t0,t1=t1,psub(t0,pmul(q,t1))
 if r0:
  inv=r0[-1].inverse();r0=pscale(r0,inv);s0=pscale(s0,inv);t0=pscale(t0,inv)
 assert not psub(r0,padd(pmul(s0,a),pmul(t0,b)))
 stats['lambdaBezoutReturns']+=1
 return r0,s0,t0
def pinfo(p):
 pairs=[v.pair() for v in p]
 out={'lambdaDegree':len(p)-1,
      'sha256':hashlib.sha256(json.dumps(pairs,separators=(',',':')).encode()).hexdigest()}
 if len(p)<=9:out['quadraticCoefficientsLowToHigh']=pairs
 return out
def eval_weight(p):
 assert env['pure_x'](p)
 a=K0;d=int(p.degrees()[0]) if p else -1
 data=p.to_dict()
 for j in range(d,-1,-1):a=a*X+K(data.get((j,0,0,0,0),0))
 return a
assert eval_weight(env['paid'])
eval_weight(env['paid']).inverse()
def convert(v):
 assert env['pure_x'](v.d)
 den=eval_weight(v.d);inv=den.inverse()
 coeff={}
 for e,a in v.n.to_dict().items():
  assert e[1]==e[3]==e[4]==0
  j=int(e[2]);n=K(a)
  for _ in range(int(e[0])):n=n*X
  coeff[j]=coeff.get(j,K0)+n
 out=trim([coeff.get(j,K0)*inv for j in range(max(coeff,default=-1)+1)])
 for j,n in coeff.items():assert (out[j] if j<len(out) else K0)*den==n
 return out
qw=[convert(v) for v in env['qw']]
assert qw[2]==[K1]
fhat=[convert(v) for v in env['fhat']]
that=[convert(v) for v in env['that']]
def oadd(a,b):return [padd(a[0],b[0]),padd(a[1],b[1])]
def oscale(a,c):return [pmul(a[0],c),pmul(a[1],c)]
def omul(a,b):
 c0=pmul(a[0],b[0]);c1=padd(pmul(a[0],b[1]),pmul(a[1],b[0]));c2=pmul(a[1],b[1])
 out=[psub(c0,pmul(c2,qw[0])),psub(c1,pmul(c2,qw[1]))]
 assert not psub(c0,padd(out[0],pmul(c2,qw[0])))
 assert not psub(c1,padd(out[1],pmul(c2,qw[1])))
 stats['omegaProductReturns']+=1;return out
def opow(a,n):
 out=[[K1],[]]
 for _ in range(n):out=omul(out,a)
 return out
def original_remainder(value,limit):
 out=[[],[]]
 for (i,j),v in env['coefficients'](value,limit).items():
  out=oadd(out,oscale(omul(opow(fhat,i),opow(that,j)),convert(v)))
 return out
linear=[[convert(v) for v in row] for row in env['linear']]
assert len(linear)==4
for i,v in enumerate(env['original']):
 ret=original_remainder(v,2)
 assert all(not psub(ret[j],linear[i][j]) for j in range(2))
 stats['originalRowsReturned']+=1
# New full original NS/PS reduction is done only after the actual constant
# field specialization; there is no old two-variable twelve-row replay.
linear.extend([original_remainder(env['NS'],3),original_remainder(env['PS'],3)])
stats['originalRowsReturned']+=2
say('new_B_complete_QQ_quadratic_original_input',
 factor='2*x^2+4*x-1',weightFieldQQDimension=2,
 completeBothComplexEmbeddings=True,
 originalFullSourceSHA256=BASE_SHA,
 originalNecessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 originalRowLambdaDegrees=[[len(v)-1 for v in row] for row in linear],
 monicOmegaDegrees=[len(v)-1 for v in qw],
 noTerminalC76OrC315Reconstruction=True,noPhysicalDInverse=True)
cofactors=[];g=[];bez=[]
for i,j in itertools.combinations(range(6),2):
 c=psub(pmul(linear[i][0],linear[j][1]),pmul(linear[i][1],linear[j][0]))
 assert not psub(c,psub(pmul(linear[j][1],linear[i][0]),pmul(linear[i][1],linear[j][0])))
 assert not psub(pmul(linear[j][1],linear[i][1]),pmul(linear[i][1],linear[j][1]))
 stats['originalCofactorCoordinates']+=2
 cofactors.append((i,j,c))
 if not c:bez.append([]);continue
 gg,a,b=pxgcd(g,c)
 bez=[pmul(a,z) for z in bez]+[b];g=gg
 assert not psub(g,__import__('functools').reduce(padd,[pmul(v,C[2]) for v,C in zip(bez,cofactors)],[]))
 if len(g)==1:break
assert len(bez)==len(cofactors)
comb=[[] for _ in range(6)]
for be,(i,j,c) in zip(bez,cofactors):
 comb[i]=padd(comb[i],pmul(be,linear[j][1]))
 comb[j]=psub(comb[j],pmul(be,linear[i][1]))
for k in range(2):
 val=[]
 for c,row in zip(comb,linear):val=padd(val,pmul(c,row[k]))
 assert not psub(val,g if k==0 else [])
say('new_B_QQ2_complete_original_lambda_Bezout',
 actualCofactorsUsed=len(cofactors),cofactorLambdaDegrees=[len(c)-1 for _,_,c in cofactors],
 monicGCD=pinfo(g),fullSixOriginalCombinationCoordinatesReturned=True,
 wholeQuadraticFactorExcluded=len(g)==1,noOtherFactorExcluded=True,
 statistics=stats)
if not g or len(g)==1:
 say('new_B_QQ2_terminal_result',wholeQuadraticFactorExcluded=len(g)==1,
     reason='original unit' if len(g)==1 else 'all original scalar cofactors zero; no lambda model paid',
     remainingC76DifferentWeightBound=74 if len(g)==1 else 76,
     wholeBExcluded=False,wholePhiExcluded=False,ordinaryISPClaim=False)
else:
 n=len(g)-1;DIM=4*n
 def br(p):return pdiv(p,g)[1]
 def ba(a,b):return br(padd(a,b))
 def bn(a):return pneg(a)
 def bs(a,b):return br(psub(a,b))
 def bm(a,b):return br(pmul(a,b))
 q0,q1=br(qw[0]),br(qw[1])
 def ar(a):return [br(a[0]),br(a[1])]
 def am(a,b):
  c0=bm(a[0],b[0]);c1=ba(bm(a[0],b[1]),bm(a[1],b[0]));c2=bm(a[1],b[1])
  out=[bs(c0,bm(c2,q0)),bs(c1,bm(c2,q1))]
  assert not bs(c0,ba(out[0],bm(c2,q0)))
  assert not bs(c1,ba(out[1],bm(c2,q1)))
  stats['omegaProductReturns']+=1;return out
 def flat(a):
  out=[]
  for omega in range(2):
   for j in range(n):
    k=a[omega][j] if j<len(a[omega]) else K0
    out.extend([k.a,k.b])
  assert len(out)==DIM;return out
 ONE=ar([[K1],[]])
 algebra_basis=[]
 for omega in range(2):
  for j in range(n):
   for xpow in range(2):
    val=[[],[]];val[omega]=[K0]*j+[K1 if xpow==0 else X]
    algebra_basis.append(ar(val))
 for j,v in enumerate(algebra_basis):
  assert flat(v)==[fmpq(int(i==j)) for i in range(DIM)]
 original_rows=list(map(ar,linear))
 columns=[];tags=[]
 for i,row in enumerate(original_rows):
  for j,b in enumerate(algebra_basis):
   columns.append(flat(am(row,b)));tags.append((i,j))
 MAT=fmpq_mat([[columns[j][i] for j in range(len(columns))] for i in range(DIM)])
 rr,rank=MAT.rref();rank=int(rank)
 selected=[]
 for i in range(rank):selected.append(next(j for j in range(len(columns)) if rr[i,j]))
 assert len(set(selected))==rank
 if rank:
  N=fmpq_mat([[MAT[i,j] for j in selected] for i in range(DIM)])
  tt0,r0=N.transpose().rref();assert int(r0)==rank
  I=[next(j for j in range(DIM) if tt0[i,j]) for i in range(rank)]
  SQ=fmpq_mat([[MAT[i,j] for j in selected] for i in I]);INV=SQ.inv()
  ID=fmpq_mat([[int(i==j) for j in range(rank)] for i in range(rank)])
  assert SQ*INV==ID and INV*SQ==ID
  stats['selectedMatrixInverseCoordinates']+=2*rank*rank
  restriction=fmpq_mat([[MAT[i,j] for j in range(len(columns))] for i in I])
  assert N*INV*restriction==MAT
  stats['allOriginalIdealColumnCoordinates']=DIM*len(columns)
 else:N=None;I=[];INV=None
 def member(v):
  target=flat(v)
  if not rank:return not any(target)
  rhs=fmpq_mat([[target[i]] for i in I]);coef=INV*rhs
  ret=N*coef
  okay=all(ret[i,0]==target[i] for i in range(DIM))
  if okay:stats['targetCoordinates']+=DIM
  return okay
 # The actual algebra is K[lambda,omega]/(g,q), not an assumed free
 # representation of the original quotient.  All original ideal columns
 # are multiplied by its complete QQ basis.
 D0=env['ell']*(2*env['lam']**2-2*env['lam']+1)-env['T']**2
 Drow=ar(original_remainder(D0,2))
 Trow=ar(that);Lrow=ar([[K0,K1],[]])
 unit=am(am(Lrow,Trow),Drow)
 power=ONE;found=None
 for exponent in range(DIM+1):
  tick();ok=member(power)
  say('new_B_QQ2_actual_positive_unit_target',
      power=exponent,target='(lambda*t*Dval)^n',
      exactOriginalIdealMembershipReturned=ok,
      idealMatrixQQRank=rank,completeQQAlgebraDimension=DIM)
  if ok:found=exponent;break
  if exponent<DIM:power=am(power,unit)
 say('new_B_QQ2_finite_original_algebra_return',
     monicLambdaDegree=n,completeQQAlgebraDimension=DIM,
     originalIdealMatrixShape=[DIM,len(columns)],actualIdealQQRank=rank,
     quotientQQDimension=DIM-rank,selectedOriginalColumns=selected,
     selectedCoefficientRows=I,selectedOriginalColumnTags=[tags[j] for j in selected],
     positiveUnitPowerReturned=found,
     entireLambdaAndOmegaNilpotentsKept=True,
     bothQuadraticEmbeddingsKept=True,
     physicalTargetIdentity='Dval=ell*(2lambda^2-2lambda+1)-T^2=bc*(h-k)^2',
     noPhysicalDInverse=True,
     wholeQuadraticFactorExcluded=found is not None,
     remainingC76DifferentWeightBound=74 if found is not None else 76,
     wholeBExcluded=False,wholePhiExcluded=False,ordinaryISPClaim=False,
     statistics=stats)
