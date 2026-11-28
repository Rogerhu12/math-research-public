#!/usr/bin/env python3
"""FIRST NEW original residual singleton input at the ONLY returned center.
The prior complete five-original return forced L=3/4 in F1009; the exact
original q2 residue is (3/8)(mu+2)^2, so every residual field point has mu=-2.
Keep physical f free. Compute the two complete singleton conditions
PB[0], (NB-PB)[1] from the necessary real Gram prefix at this center,
then return one fixed F1009[f] two-original Bezout.
No old generic first-jet resultant or 18-column input is executed.
30 seconds /256 MiB; fixed p1009 and one source pair.
"""
import ast,hashlib,json,resource,signal,time
from pathlib import Path
START=time.perf_counter();DEADLINE=START+30
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
signal.setitimer(signal.ITIMER_REAL,30)
dep=Path(__file__).with_name('2026-11-29-unit211-W-positive-e-generic-k-complete-singleton-NP-first-jets-8542.py')
data=dep.read_text()
assert hashlib.sha256(data.encode()).hexdigest()=='958f1bbbf613211a047bb2adf91d340c8fd3ed23b5794470dee3f4d0ba9cfc5a'
prefix=data.split('NB,NC=N4(rows[2]),N4(rows[3])')[0]
assert len(prefix.encode())==4750
assert hashlib.sha256(prefix.encode()).hexdigest()=='ce658823d68f6afba617d80088f5073fcccb79a3550509bce4b220f7a8d8f3b8'
old='L,mu,physical_f=map(R,(lp,mp,fp))'
assert prefix.count(old)==1
prefix=prefix.replace(old,'L,mu,physical_f=R(3)/4,R(-2),R(fp)')
nodes=[]
for node in ast.parse(prefix).body:
 if isinstance(node,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef)):nodes.append(node)
 elif isinstance(node,ast.Assign):
  names={n.id for t in node.targets for n in ast.walk(t) if isinstance(n,ast.Name)}
  if not names.intersection({'START','DEADLINE'}):nodes.append(node)
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(dep),'exec'),globals())
P=1009
STAT.update(newCenterOriginalReturns=0,finiteFieldDivisions=0,finiteFieldBezoutChecks=0)
F0=P2(rows[2]).a
F1=(N4(rows[2])-P2(rows[2])).b
assert F0==R(48*fp**3-480*fp**2+1686*fp-1944)
STAT['newCenterOriginalReturns']+=1
FORMS=[F0,F1]
def fraction(c):
 ss=str(c)
 return tuple(map(int,ss.split('/'))) if '/' in ss else (int(ss),1)
def cm(c):
 a,b=fraction(c);assert b%P
 return a%P*pow(b%P,P-2,P)%P
def trim(a):
 a=[int(x)%P for x in a]
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
              for i in range(max(len(a),len(b)))])
def sub(a,b):return add(a,[-x for x in b])
def mul(a,b):
 if not a or not b:return []
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%P
 return trim(out)
def scale(a,c):return trim([x*c for x in a])
def div(a,b):
 tick();a0=trim(a);b=trim(b);assert b
 rem=list(a0);out=[0]*max(0,len(a0)-len(b)+1);inv=pow(b[-1],P-2,P)
 while rem and len(rem)>=len(b):
  j=len(rem)-len(b);cc=rem[-1]*inv%P;out[j]=cc
  for i,v in enumerate(b):rem[j+i]=(rem[j+i]-cc*v)%P
  rem=trim(rem)
 out=trim(out);assert add(mul(out,b),rem)==a0
 STAT['finiteFieldDivisions']+=1
 return out,rem
def xgcd(a,b):
 r0,r1=trim(a),trim(b);s0,s1=[1],[];t0,t1=[],[1]
 while r1:
  qq,r2=div(r0,r1)
  r0,r1=r1,r2;s0,s1=s1,sub(s0,mul(qq,s1));t0,t1=t1,sub(t0,mul(qq,t1))
 if not r0:return [],[],[]
 inv=pow(r0[-1],P-2,P);g,s,t=scale(r0,inv),scale(s0,inv),scale(t0,inv)
 assert add(mul(s,a),mul(t,b))==g
 STAT['finiteFieldBezoutChecks']+=1
 return g,s,t
def fpcoeff(v):
 assert int(v.d.total_degree())==0
 den=v.d.coefficient(0);out=[0]*(int(v.n.degrees()[2])+1) if v.n else []
 for ex,c in v.n.to_dict().items():
  assert int(ex[0])==0 and int(ex[1])==0
  out[int(ex[2])]=cm(c/den)
 return trim(out)
def lift(a):return R(ctx.from_dict({(0,0,i):c for i,c in enumerate(a) if c}))
def prof(a):
 bb=json.dumps(a,separators=(',',':')).encode()
 return {'degree':len(a)-1,'terms':sum(bool(x) for x in a),
         'bytes':len(bb),'sha256':hashlib.sha256(bb).hexdigest()}
ff=[fpcoeff(v) for v in FORMS]
say('new_only_positive_e_generic_k_center_original_singletons',
    center={'L':'3/4','mu':'-2','lambda':'1/2','k':'-8'},
    centerForcedByPriorWholeOriginalReturn=True,
    q2AtCenterBeforeMuReduction='3*(mu+2)^2/8',
    physicalFStillFree=True,
    originalLabels=['complete_P_B_order_zero','complete_N_B_minus_P_B_divided_e'],
    originalFpProfiles=[prof(v) for v in ff],
    smallActualOriginalCoefficientLists=ff,
    onlyNecessaryGramDefinitionsSpecialized=True,
    noPriorGenericProofGateExecuted=True)
g,a,b=xgcd(ff[0],ff[1])
assert add(mul(a,ff[0]),mul(b,ff[1]))==g
difference=lift(a)*F0+lift(b)*F1-lift(g)
assert int(difference.d.total_degree())==0
assert all(cm(c)==0 for c in difference.n.to_dict().values())
STAT['newCenterOriginalReturns']+=1
say('new_only_center_two_complete_original_singleton_return',
    gcd=prof(g),smallGcd=g,
    actualOriginalMultiplierProfiles=[prof(a),prof(b)],
    smallActualOriginalMultiplierLists=[a,b],
    completeTwoOriginalCoefficientReturnModulo1009=True,
    excludesEntireNamedResidualFieldCenter=(g==[1]),
    nonconstantGcdRetainsEveryRoot=(g!=[1]),
    allFValuesAndMultiplicitiesRetained=True,
    noPhysicalFZeroOrChosenF=True,noOrdinaryISPClaim=True,statistics=STAT)
