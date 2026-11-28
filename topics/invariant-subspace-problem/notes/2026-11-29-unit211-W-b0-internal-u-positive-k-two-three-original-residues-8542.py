#!/usr/bin/env python3
"""NEW W/b0 internal u=0 valuation boundary, residue k=2.
Only the remaining case v(A*/u)=v(u)/2 and mu a unit.
Three complete original leading residues q2/(20u^3), R6/u^5, N5/u^4
are transported without a new leading inverse to two fixed F1009
polynomials in r. One exact Bezout and a final THREE-source return.
This is a valuation-residue calculation, NOT a QQ emptiness lifting.
No old ray, scalar projection, Newton, local jet or saturation gate.
Self-contained; fixed p1009; 30 seconds /256MiB; no adaptive retry.
"""
import hashlib,json,resource,signal,time
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
signal.setitimer(signal.ITIMER_REAL,30)
P=1009
STAT={'fieldInverseProducts':0,'univariateDivisionProducts':0,
      'threeSourceReturns':0,'scaledOriginalResidueReturns':0}
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
def iv(a):
 a%=P;assert a
 b=pow(a,P-2,P);assert a*b%P==1
 STAT['fieldInverseProducts']+=1;return b
def rat(a,b=1):return a%P*iv(b)%P
def tr(a):
 a=[v%P for v in a]
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 z=[0]*max(len(a),len(b))
 for i,v in enumerate(a):z[i]+=v
 for i,v in enumerate(b):z[i]+=v
 return tr(z)
def scale(a,c):return tr([v*c for v in a])
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 if not a or not b:return []
 z=[0]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  for j,w in enumerate(b):z[i+j]+=v*w
 return tr(z)
def div(a,b):
 assert b
 rem=a[:];out=[0]*max(0,len(a)-len(b)+1);ib=iv(b[-1])
 while rem and len(rem)>=len(b):
  j=len(rem)-len(b);c=rem[-1]*ib%P;out[j]=c
  rem=sub(rem,[0]*j+scale(b,c))
 out=tr(out)
 assert add(mul(out,b),rem)==a and (not rem or len(rem)<len(b))
 STAT['univariateDivisionProducts']+=1
 return out,rem
def xgcd(a,b):
 aa,bb=a[:],b[:];s0,s1=[1],[];t0,t1=[],[1]
 while bb:
  q,rr=div(aa,bb);aa,bb=bb,rr
  s0,s1=s1,sub(s0,mul(q,s1))
  t0,t1=t1,sub(t0,mul(q,t1))
  assert add(mul(s0,a),mul(t0,b))==aa
 c=iv(aa[-1]);g,s,t=scale(aa,c),scale(s0,c),scale(t0,c)
 assert add(mul(s,a),mul(t,b))==g
 return g,s,t
def bc(c):return {(0,0):c%P} if c%P else {}
def ba(a,b):
 d=dict(a)
 for e,c in b.items():d[e]=(d.get(e,0)+c)%P
 return {e:c for e,c in d.items() if c}
def bs(a,c):return {e:v*c%P for e,v in a.items() if v*c%P}
def bn(a,b):return ba(a,bs(b,-1))
def bm(a,b):
 d={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():
   e=(i+k,j+l);d[e]=(d.get(e,0)+v*w)%P
 return {e:c for e,c in d.items() if c}
def bp(a,n):
 z=bc(1)
 while n:
  if n&1:z=bm(z,a)
  a=bm(a,a);n//=2
 return z
def bu(a):return {(0,j):v%P for j,v in enumerate(a) if v%P}
def prof(a):
 raw=json.dumps([[list(e),c] for e,c in sorted(a.items())],
                separators=(',',':')).encode()
 return {'degrees':[max((e[i] for e in a),default=-1) for i in range(2)],
         'terms':len(a),'bytes':len(raw),
         'sha256':hashlib.sha256(raw).hexdigest()}
one=bc(1);n={(1,0):1};r={(0,1):1}
mu=bs(bn(n,bc(3)),rat(1,2))
A2=bs(ba(ba(bp(mu,2),bs(mu,4)),bc(5)),rat(1,2))
d=bs(n,rat(59,12));x=bm(d,r)
# Original three leading residues; x=T^2/u, d=59(2mu+3)/12.
q0=ba(ba(ba(bs(x,12),bs(bp(mu,2),-30)),bs(mu,-2)),bc(27))
dOriginal=bn(bs(A2,5),x)
hOriginal=ba(bs(A2,-15),bs(x,2))
gg=ba(bs(mu,13),bc(27))
Y=bs(bn(bc(33),bs(mu,13)),rat(1,118))
z2=ba(gg,bs(Y,16))
Rraw=bn(bs(bm(x,bp(hOriginal,2)),59),bs(bp(dOriginal,3),64))
Nraw=bn(bs(bm(dOriginal,ba(bm(gg,x),bm(dOriginal,z2))),-8),
        bs(bm(bm(x,hOriginal),Y),236))
q=ba(bn(bs(bp(n,2),15),bm(ba(bc(88),bs(r,118)),n)),bc(75))
assert q0==bs(q,rat(-1,2))
assert dOriginal==ba(d,bs(q,rat(1,24)))
assert hOriginal==bn(ba(bs(x,-1),bs(d,-3)),bs(q,rat(1,8)))
STAT['scaledOriginalResidueReturns']+=3
# Necessary R and N after q, retaining ordinary polynomial errors.
Ru=[-64,531,354,59]
H=[204,413,59]
au=scale(H,-13)
bu_=sub(scale(H,105),[28320,28320])
Nu=ba(bm(bu(au),n),bu(bu_))
Rerr=ba(ba(ba(bs(bm(x,ba(x,bs(d,3))),rat(59,4)),
                  bs(bm(x,q),rat(59,64))),bs(bp(d,2),-8)),
        ba(bs(bm(d,q),rat(-1,3)),bs(bp(q,2),rat(-1,216))))
Nerr=ba(ba(bs(bm(gg,x),rat(-1,3)),bs(bm(d,z2),rat(-2,3))),
        ba(bs(bm(q,z2),rat(-1,72)),bs(bm(x,Y),rat(59,2))))
assert Rraw==ba(bm(bp(d,3),bu(Ru)),bm(q,Rerr))
assert Nraw==ba(bs(bm(bp(d,2),Nu),rat(1,59)),bm(q,Nerr))
STAT['scaledOriginalResidueReturns']+=2
say('new_internal_u_positive_k_two_complete_original_residues',
    prime=P,valuationScope={'u':'positive','e':'unit,residue -1',
       'k':'unit,residue 2','Astar_over_u':'valuation v(u)/2','mu':'unit'},
    variableOrder=['n=2mu+3','r=(T^2/u)/(59n/12)'],
    originalSourceOrder=['q2/(20u^3)','complete_R6/u^5','complete_N5/u^4'],
    threeOriginalProfiles=[prof(q0),prof(Rraw),prof(Nraw)],
    necessaryResidues=[prof(q),prof(bu(Ru)),prof(Nu)],
    dNonzeroIsProvedFromOriginalQAndR=True,
    noOriginalDInverse=True,noOldGate=True,statistics=STAT)
# ONE predetermined (quadratic n, linear n) elimination identity.
AA=[15];BB=[-88,-118];CC=[75]
E=add(sub(mul(AA,mul(bu_,bu_)),mul(BB,mul(au,bu_))),mul(CC,mul(au,au)))
lin=ba(bm(bu(mul(AA,au)),n),bu(sub(mul(BB,au),mul(AA,bu_))))
assert bu(E)==bn(bm(bu(mul(au,au)),q),bm(lin,Nu))
STAT['threeSourceReturns']+=1
g,sR,sE=xgcd(tr(Ru),tr(E))
Oq=bu(mul(sE,mul(au,au)))
OR=bu(sR)
ON=bs(bm(bu(sE),lin),-1)
assert bu(g)==ba(ba(bm(Oq,q),bm(OR,bu(Ru))),bm(ON,Nu))
STAT['threeSourceReturns']+=1
# Full return to the THREE complete original leading residues:
# multiply only by the already nonzero residue d^3, never invert it.
Tq=bn(bn(bm(bp(d,3),Oq),bm(OR,Rerr)),bs(bm(bm(d,ON),Nerr),59))
Omega=[bs(Tq,-2),OR,bs(bm(d,ON),59)]
target=bm(bp(d,3),bu(g))
assert target==ba(ba(bm(Omega[0],q0),bm(Omega[1],Rraw)),bm(Omega[2],Nraw))
STAT['threeSourceReturns']+=1
say('new_fixed_same_point_residual_Bezout_and_three_original_return',
    prime=P,firstDegree=len(tr(Ru))-1,secondDegree=len(tr(E))-1,
    gcdDegree=len(g)-1,gcd=prof(bu(g)),
    exactThreeSourceTarget=prof(target),
    originalMultipliers=[prof(z) for z in Omega],
    excludesOnlyNamedValuationCenter=(g==[1]),
    allUnremovedResidualFactorsRetained=(g!=[1]),
    onlyPositiveDLeadingPower=True,noQQEmptyLifting=True,
    noPrimeOrTargetChange=True,statistics=STAT)
