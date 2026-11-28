#!/usr/bin/env python3
"""NEW true B: actual terminal original multipliers and cancellation.
Only the seven necessary I4 rows, no old twelve-row gate, C315 LCM,
positive-unit action, old cofactors, or NS/PS definitions.
120 seconds / 1 GiB, absolute nested deadline, small output only.
"""
import hashlib,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
_RAW_ALARM=signal.alarm
def bounded_alarm(seconds):
 if seconds<=0:return _RAW_ALARM(0)
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
 return _RAW_ALARM(max(1,min(int(seconds),math.ceil(DEADLINE-time.perf_counter()))))
signal.alarm=bounded_alarm;signal.alarm(120)
BASENAME='2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542.py'
BASE_SHA='b802d6c9b7a46b544f1fd5f814b05337a552f938a660b8d047fe4e62ff4eae56'
path=pathlib.Path(__file__).with_name(BASENAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASENAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
MARKER='newValues=[];quotients=[]';assert full.count(MARKER)==1
original_prefix=full[:full.index(MARKER)]
lines=original_prefix.splitlines()
dropped=[line for line in lines if line.startswith('NS=pure(') or line.startswith('PS=pure(')]
assert len(dropped)==2
prefix='\n'.join(line for line in lines if line not in dropped)+'\n'
env={'__name__':'isp_B_only_four_original_rows','__file__':str(path),'print':lambda *a,**k:None}
exec(compile(prefix,str(path)+'#I4_definitions_only','exec'),env)
signal.alarm=bounded_alarm;signal.alarm(120)
R=env['R'];ctx=env['ctx'];up,Qp,Lp,Tp,zp=ctx.gens()
zeroP=ctx.constant(0);oneP=ctx.constant(1);lam=env['lam']
qw=env['qw'];linear=env['linear'];changed=env['changed'];tag=env['tag']
univar=env['univar'];paid=env['paid']
inputs=[]
for row in linear[:3]:
 inputs.extend([row,[-qw[0]*row[1],row[0]-qw[1]*row[1]]])
inputs.append(linear[3])
assert len(inputs)==7
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
def pure_x(p):return all(not any(e[1:]) for e in p.to_dict())
def allowed(p):return all(e[1]==e[3]==e[4]==0 for e in p.to_dict())
def degree(p):return max((int(e[2]) for e in p.to_dict()),default=-1)
def coeff(p,n):
 return ctx.from_dict({(e[0],0,0,0,0):a for e,a in p.to_dict().items() if int(e[2])==n})
def leading(v):return max((degree(p),i) for i,p in enumerate(v))
def profile(p):
 out={'degrees':list(map(int,p.degrees())) if p else [-1]*5,'terms':len(p.to_dict()),
      'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
 if p and pure_x(p) and int(p.degrees()[0])<=12:out['polynomial']=str(p)
 return out
returns={'polynomialDivisions':0,'seedCoordinates':0,'edgeCoordinates':0,
         'zeroRowCoordinates':0,'terminalTwoCoordinates':0,'originalOmegaIdentities':0}
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 returns['polynomialDivisions']+=1;return q
def lcm(a,b):
 assert pure_x(a) and pure_x(b) and a and b
 return exact(a,a.gcd(b))*b
def primitive(v):
 if not any(v):return None,None
 assert all(allowed(p) for p in v)
 g=zeroP
 for p in v:
  for j in range(degree(p)+1):
   a=coeff(p,j)
   if a:g=g.gcd(a)
   if g and int(g.total_degree())==0:break
  if g and int(g.total_degree())==0:break
 d,j=leading(v);lc=univar(coeff(v[j],d))
 g*=ctx.constant(lc[int(lc.degree())])
 out=[exact(p,g) for p in v]
 return out,g
nodes=[]
def seed(index,row):
 den=oneP
 for a in row:
  assert pure_x(a.d);den=lcm(den,a.d)
 raw=[a.n*exact(den,a.d) for a in row]
 if not any(raw):return None
 v,g=primitive(raw);scale=R(den,g)
 assert all(R(v[j])==scale*row[j] for j in range(2))
 returns['seedCoordinates']+=2
 nodes.append({'v':v,'seed':index,'scale':scale,'parents':[]})
 return len(nodes)-1
def cancel(current,pivot):
 old=nodes[current]['v'];pv=nodes[pivot]['v']
 d,j=leading(old);dp,jp=leading(pv);assert j==jp and d>=dp
 aa=coeff(old[j],d);bb=coeff(pv[j],dp);shift=Lp**(d-dp)
 raw=[bb*old[i]-aa*shift*pv[i] for i in range(2)]
 if not any(raw):
  assert all(bb*old[i]==aa*shift*pv[i] for i in range(2))
  returns['zeroRowCoordinates']+=2;return None
 v,g=primitive(raw)
 assert all(g*v[i]==bb*old[i]-aa*shift*pv[i] for i in range(2))
 returns['edgeCoordinates']+=2
 assert leading(v)<(d,j)
 nodes.append({'v':v,'seed':None,'parents':[(current,R(bb,g)),(pivot,R(-aa*shift,g))]})
 return len(nodes)-1
basis={}
for i,row in enumerate(inputs):
 current=seed(i,row)
 while current is not None:
  d,j=leading(nodes[current]['v'])
  if j not in basis:basis[j]=current;break
  old=basis[j]
  if d<leading(nodes[old]['v'])[0]:basis[j]=current;current=old
  current=cancel(current,basis[j])
assert sorted(basis)==[0,1] and all(leading(nodes[basis[j]]['v'])[0]==0 for j in basis)
p0=nodes[basis[0]]['v']
assert not p0[1] and p0[0] and pure_x(p0[0])
terminal={basis[0]:R(1,p0[0])}
for j in range(2):
 assert sum((a*R(nodes[n]['v'][j]) for n,a in terminal.items()),R())==R(int(j==0))
returns['terminalTwoCoordinates']+=2
say('new_B_only_seven_I4_rows_input',necessaryRows=7,definitionDAGNodes=len(nodes),
 noOldC315LCMOrFullTwelveGateExecuted=True,noNSPSDefinitionsExecuted=True,
 originalFullSourceSHA256=BASE_SHA,
 originalNecessaryPrefixSHA256=hashlib.sha256(original_prefix.encode()).hexdigest(),
 actuallyUsedPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest())
# NEW target: full actual original coefficients, with cancellations at each sum.
pending=dict(terminal);omega=[R() for _ in inputs];reachable=set()
for n in range(len(nodes)-1,-1,-1):
 value=pending.get(n,R())
 if not value:continue
 reachable.add(n);node=nodes[n]
 if node['seed'] is not None:
  omega[node['seed']]+=value*node['scale']
 else:
  for parent,mult in node['parents']:
   pending[parent]=pending.get(parent,R())+value*mult
for j in range(2):
 assert sum((omega[i]*inputs[i][j] for i in range(7)),R())==R(int(j==0))
returns['terminalTwoCoordinates']+=2
say('new_B_actual_terminal_seven_source_coefficients',
 allTwoCoordinatesReturned=True,reachableDefinitionNodes=len(reachable),
 nonzeroOriginalCoefficients=sum(bool(v) for v in omega),
 coefficientLambdaDegrees=[degree(v.n) for v in omega],
 originalCoefficientDenominatorDegrees=[int(v.d.degrees()[0]) for v in omega])
# Transport to the actual four changed original quadratics, not just their q-remainders.
betas=[[omega[0],omega[1]],[omega[2],omega[3]],[omega[4],omega[5]],[omega[6]]]
combined=[]
for beta,fi in zip(betas,changed):combined=env['add'](combined,env['mul'](beta,fi))
difference=env['sub'](combined,[R(1)])
rem,k=env['reduce_omega'](difference)
assert not any(rem)
final=[env['sub'](beta,env['scale'](k,a)) for beta,a in zip(betas,tag)]
check=[]
for beta,fi in zip(final,changed):check=env['add'](check,env['mul'](beta,fi))
assert not env['sub'](check,[R(1)])
returns['originalOmegaIdentities']+=1
den=oneP
for beta in final:
 for a in beta:
  assert pure_x(a.d);den=lcm(den,a.d)
cover=den;removed=oneP
while int(cover.total_degree())>0:
 g=cover.gcd(paid)
 if int(g.total_degree())<=0:break
 cover=exact(cover,g);removed*=g
assert cover*removed==den
scaled=[[R(cover)*a for a in beta] for beta in final]
for beta in scaled:
 for a in beta:env['ckden'](a)
check=[]
for beta,fi in zip(scaled,changed):check=env['add'](check,env['mul'](beta,fi))
assert not env['sub'](check,[R(cover)])
returns['originalOmegaIdentities']+=1
say('new_B_full_original_four_multiplier_actual_cover',
 rawTerminalDenominatorLCM=profile(den),retainedNecessaryCover=profile(cover),
 allFourCompleteOriginalMultipliersReturned=True,
 strictIdentity='Cnew=sum_i Omega_i*Fi in the exact changed original I4; paid coordinate isomorphism returns Cnew to the original I4',
 exponent=1,everyRetainedWeightZeroFiberKept=True,
 noNewHeadOrDInverse=True,wholeBExcluded=int(cover.total_degree())==0,
 previous315BoundNotUsedAsAGate=True,statistics=returns,ordinaryISPClaim=False)
# New exact univariate support classification, after the full identity was emitted.
pu=univar(cover);constant,factors=pu.factor()
product=type(pu)([constant]);radical=type(pu)([1]);maxpower=0;factor_info=[]
for fac,power in factors:
 power=int(power);product*=fac**power;radical*=fac;maxpower=max(maxpower,power)
 pm=env['multivar'](fac)
 factor_info.append({'power':power,**profile(pm)})
assert product==pu
if factors:
 quotient,remainder=divmod(radical**maxpower,pu)
 assert not remainder and quotient*pu==radical**maxpower
else:maxpower=0
say('new_B_actual_terminal_cover_factor_support',
 exactQQFactorProductReturned=True,nonconstantFactors=factor_info,
 radicalDegree=int(radical.degree()),maximumMultiplicity=maxpower,
 radicalPowerDivisibleByActualCoverReturned=True,
 differentOriginalWeightPairsUpperBound=int(radical.degree()),
 completeGeometricPointCountClaim=False,
 wholeBExcluded=int(radical.degree())==0,ordinaryISPClaim=False)
