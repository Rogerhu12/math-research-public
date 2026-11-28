#!/usr/bin/env python3
"""FIRST NEW W positive-e generic-k joint five-original six-generator input.
Use only the necessary Gram definition prefix of the completed singleton
first-jet source, never its assertions, four-form loop or f-resultants.
The already paid q_mu (monic degree2) and P_B (monic degree3 in f) give
a genuine free-six ambient algebra. Form all 18 original columns from
P1=(N_B-P_B)/e, COMPLETE R6, COMPLETE N5 at the same residual point.
Three fixed 6-column cofactors, then one FIRST F_1009[L] joint Bezout,
returned to ALL FIVE originals. 120 seconds / 1 GiB, no adaptive groups,
no replay of the old q/R/N5 gate or old singleton f-resultant.
"""
import ast,hashlib,json,resource,signal,time
from pathlib import Path
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
dep=Path(__file__).with_name('2026-11-29-unit211-W-positive-e-generic-k-complete-singleton-NP-first-jets-8542.py')
text=dep.read_text()
assert hashlib.sha256(text.encode()).hexdigest()=='958f1bbbf613211a047bb2adf91d340c8fd3ed23b5794470dee3f4d0ba9cfc5a'
prefix=text.split('NB,NC=N4(rows[2]),N4(rows[3])')[0]
assert len(prefix.encode())==4750
assert hashlib.sha256(prefix.encode()).hexdigest()=='ce658823d68f6afba617d80088f5073fcccb79a3550509bce4b220f7a8d8f3b8'
nodes=[]
for node in ast.parse(prefix).body:
 if isinstance(node,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef)):
  nodes.append(node)
 elif isinstance(node,ast.Assign):
  names={n.id for t in node.targets for n in ast.walk(t) if isinstance(n,ast.Name)}
  if not names.intersection({'START','DEADLINE'}):nodes.append(node)
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(dep),'exec'),globals())
STAT.update(monicDivisions=0,originalModuleReturns=0,columnCoordinates=0,
            cofactorCoordinates=0,fiveSourceReturns=0,pIntegralChecks=0,
            finiteFieldDivisions=0,finiteFieldBezoutChecks=0)
P=1009
ATOMS=[lp,lp-1,2*lp-1,2*lp-3]
PAID=lp*(lp-1)*(2*lp-1)*(2*lp-3)
def weight(p):
 return all(int(ex[1])==0 and int(ex[2])==0 for ex in p.to_dict())
def strip(p):
 rem=p;removed=ONE
 if not p:return p,removed
 for atom in ATOMS:
  while rem:
   gg=rem.gcd(atom)
   if int(gg.total_degree())==0:break
   rem=exact(rem,gg);removed*=gg
   STAT['oldPaidSupportProducts']+=1
 assert rem*removed==p
 return rem,removed
def paid(p):
 assert p and weight(p)
 rr,_=strip(p);assert int(rr.total_degree())==0
def cmod(c):
 ss=str(c)
 nu,de=map(int,ss.split('/')) if '/' in ss else (int(ss),1)
 assert de%P
 return (nu%P)*pow(de%P,P-2,P)%P
def integral(v):
 v=R(v);paid(v.d)
 for pp0 in [v.n,v.d]:
  for cc in pp0.to_dict().values():cmod(cc)
 STAT['pIntegralChecks']+=1
 return v
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 bb=json.dumps(data,separators=(',',':')).encode()
 return {'degrees':list(map(int,p.degrees())) if p else [-1,-1,-1],
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(data),'bytes':len(bb),'sha256':hashlib.sha256(bb).hexdigest()}
def rp(v):
 v=R(v);return {'numerator':profile(v.n),'denominator':profile(v.d)}
def coeffs(v,index):
 v=R(v);paid(v.d);groups={}
 for ex,cc in v.n.to_dict().items():
  j=int(ex[index]);ee=list(ex);ee[index]=0
  groups.setdefault(j,{})[tuple(ee)]=cc
 return [R(ctx.from_dict(groups.get(j,{})),v.d)
         for j in range(max(groups,default=-1)+1)]
def trim(aa):
 while aa and not aa[-1]:aa.pop()
 return aa
def rebuild(aa,xx):
 out=R()
 for cc in reversed(aa):out=out*xx+cc
 return out
def monic_div(value,divisor,index):
 aa=trim(coeffs(value,index));bb=trim(coeffs(divisor,index))
 assert bb and bb[-1]==1
 qq=[R() for _ in range(max(0,len(aa)-len(bb)+1))]
 while aa and len(aa)>=len(bb):
  tick();j=len(aa)-len(bb);lc=aa[-1];qq[j]+=lc
  for i,bi in enumerate(bb):aa[j+i]-=lc*bi
  trim(aa)
 xx=(L,mu,physical_f)[index]
 quotient,remainder=rebuild(qq,xx),rebuild(aa,xx)
 assert R(value)==quotient*divisor+remainder
 STAT['monicDivisions']+=1
 return quotient,remainder

# Only necessary definitions for the NEW same-point joint original target.
P0=P2(rows[2]).a
P1=(N4(rows[2])-P2(rows[2])).b
h=3-2*L
qraw=h**3*mu*mu/9-4*h*(L-1)*mu+2*h*h-3
qlead=h**3/9;qmu=qraw/qlead
flead=16*(2*L-2)*(2*L-3)/(2*L-1)**2
Wq,Ptilde=monic_div(P0/flead,qmu,1)
assert len(coeffs(qmu,1))==3 and coeffs(qmu,1)[2]==1
assert len(coeffs(Ptilde,2))==4 and coeffs(Ptilde,2)[3]==1
assert all(int(ex[1])<2 for ex in Ptilde.n.to_dict())
M0=2*L-1;m0=1-L;Tbar=T.a;lam0=(mu+3)/2
A2=(mu*mu+4*mu+5)/2;B3=(mu**3+6*mu*mu+12*mu+7)/2
D0=L*A2-Tbar*Tbar
K0=L*L*B3-3*L*A2*Tbar+2*Tbar**3
R6=M0*K0*K0-4*m0*m0*D0**3
V0=Vs.a;ts0=ts.a;ys0=-V0/M0;w0=lam0-1-Tbar
z1=-2*(-L*mu+2*Tbar)*ys0-2*L*w0+m0*Tbar*ts0
z2=-4*m0*ys0
Z0=2*(Tbar-L*mu)*(L*w0+V0*Tbar)+M0*ts0*Tbar*Tbar/2
N5=2*m0*D0*(Z0+D0*z2)+M0*K0*z1
ORIGINAL=[integral(v) for v in [qraw,P0,P1,R6,N5]]
LABELS=['complete_q2_over_Q_residue','complete_P_B_order_zero',
        'complete_N_B_minus_P_B_divided_e','complete_R6_residue',
        'complete_N5_residue']
assert P0/flead==Ptilde+Wq*qmu
STAT['originalModuleReturns']+=1
for vv in [qmu,Ptilde,Wq,1/qlead,1/flead]:integral(vv)
basis=[R(1),mu,physical_f,mu*physical_f,physical_f**2,mu*physical_f**2]
def normal(value):
 qf,rr=monic_div(value,Ptilde,2)
 qm,rem=monic_div(rr,qmu,1)
 omega=[(qm-qf*Wq)/qlead,qf/flead]
 assert R(value)==rem+omega[0]*qraw+omega[1]*P0
 assert all(int(ex[1])<2 and int(ex[2])<3 for ex in rem.n.to_dict())
 STAT['originalModuleReturns']+=1
 return rem,omega
def coordinates(rem):
 groups=[{} for _ in range(6)]
 for ex,cc in rem.n.to_dict().items():
  ee=tuple(map(int,ex));assert ee[1]<2 and ee[2]<3
  groups[2*ee[2]+ee[1]][(ee[0],0,0)]=cc
 cs=[R(ctx.from_dict(gg),rem.d) for gg in groups]
 assert rem==sum((cs[i]*basis[i] for i in range(6)),R())
 for vv in cs:integral(vv)
 STAT['columnCoordinates']+=6
 return cs
say('new_five_original_same_point_definitions_and_true_free_six_environment',
    originalLabels=LABELS,originalProfiles=[rp(v) for v in ORIGINAL],
    qMu=rp(qmu),monicF=rp(Ptilde),
    sourceDefinitionPrefixBytes=len(prefix.encode()),
    sourceDefinitionPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
    oldTopLevelAssertionsAndProofLoopsNotExecuted=True,
    paidSupport=profile(PAID),fullSamePointR6AndN5=True,
    physicalFAndAllGramIntegralityAlreadyProved=True)
columns=[];tags=[];columnInfo=[]
for seed in [2,3,4]:
 for j,bj in enumerate(basis):
  rem,cor=normal(bj*ORIGINAL[seed])
  omega=[-cor[0],-cor[1],R(),R(),R()];omega[seed]+=bj
  assert rem==sum((omega[i]*ORIGINAL[i] for i in range(5)),R())
  STAT['fiveSourceReturns']+=1
  cc=coordinates(rem)
  columns.append(cc);tags.append(omega)
  payload=json.dumps([rp(v) for v in cc],sort_keys=True,separators=(',',':')).encode()
  columnInfo.append({'seedOriginalIndex':seed,'basisIndex':j,
       'coordinateNumeratorLDegrees':[int(v.n.degrees()[0]) if v.n else -1 for v in cc],
       'coordinateDenominatorLDegrees':[int(v.d.degrees()[0]) for v in cc],
       'coordinateProfilesSHA256':hashlib.sha256(payload).hexdigest()})
say('new_exact_five_original_six_by_eighteen_presentation',
    freeAmbientBasis=['1','mu','f','mu*f','f^2','mu*f^2'],
    columns=columnInfo,statistics=STAT,fullOriginalValueQuotientNotAssumedFree=True)
def lcm(a,b):return exact(a,a.gcd(b))*b
def cofactor(group):
 n=6;den=ONE
 for jj in group:
  for v0 in columns[jj]:den=lcm(den,v0.d)
 paid(den)
 mat=[[exact(den,columns[jj][i].d)*columns[jj][i].n for jj in group] for i in range(n)]
 work=[list(mat[i])+[ONE if i==0 else ZERO] for i in range(n)]
 previous=ONE;sgn=1
 for i in range(n-1):
  tick();pivot=next((r for r in range(i,n) if work[r][i]),None)
  if pivot is None:return None,{'step':i}
  if pivot!=i:work[i],work[pivot]=work[pivot],work[i];sgn=-sgn
  vv=work[i][i]
  for r in range(i+1,n):
   aa=work[r][i]
   for c0 in range(i+1,n+1):
    work[r][c0]=exact(vv*work[r][c0]-aa*work[i][c0],previous)
   work[r][i]=ZERO
  previous=vv
 if not work[-1][-2]:return None,{'step':5}
 det=sgn*work[-1][-2];co=[ZERO]*n
 for i in range(n-1,-1,-1):
  num=det*work[i][-1]-sum((work[i][j]*co[j] for j in range(i+1,n)),ZERO)
  co[i]=exact(num,work[i][i])
 for i in range(n):
  assert sum((mat[i][j]*co[j] for j in range(n)),ZERO)==(det if i==0 else ZERO)
  STAT['cofactorCoordinates']+=1
 omega=[sum((R(co[j]*den)*tags[group[j]][i] for j in range(n)),R()) for i in range(5)]
 assert R(det)==sum((omega[i]*ORIGINAL[i] for i in range(5)),R())
 STAT['fiveSourceReturns']+=1
 scalar,removed=strip(det)
 omega=[integral(v/R(removed)) for v in omega]
 assert R(scalar)==sum((omega[i]*ORIGINAL[i] for i in range(5)),R())
 STAT['fiveSourceReturns']+=1
 assert weight(scalar)
 return (scalar,omega),{'determinant':profile(det),'clearedOldDenominator':profile(den),
                         'removedOldPaidSupport':profile(removed)}
GROUPS=[[0,1,2,3,6,7],[0,1,2,3,12,13],[0,1,6,7,14,15]]
results=[]
for j,group in enumerate(GROUPS):
 got,metadata=cofactor(group)
 if got is None:
  say('new_prescribed_joint_six_column_scalar_zero',index=j,group=group,**metadata)
  results.append((ZERO,[R() for _ in range(5)]));continue
 scalar,omega=got;results.append(got)
 say('new_prescribed_joint_six_column_full_five_original_return',
     index=j,group=group,scalar=profile(scalar),
     allFiveOriginalMultiplierProfiles=[rp(v) for v in omega],
     sixCofactorCoordinatesAndAllOriginalSourcesReturned=True,
     allUnpaidHeadsAndMultiplicityFibersRetained=True,**metadata)

# FIRST joint univariate finite-field test of these NEW three original scalars.
# Pure small polynomial routines avoid an unverified multivariate modular API.
def ft(a):
 a=[int(c)%P for c in a]
 while a and not a[-1]:a.pop()
 return a
def fa(a,b):
 return ft([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))])
def fs(a,b):return fa(a,[-c for c in b])
def fm(a,b):
 if not a or not b:return []
 cc=[0]*(len(a)+len(b)-1)
 for i,x0 in enumerate(a):
  for j,y0 in enumerate(b):cc[i+j]=(cc[i+j]+x0*y0)%P
 return ft(cc)
def fscale(a,c):return ft([c*v for v in a])
def fd(a,b):
 tick();a0=ft(a);bb=ft(b);assert bb
 rr=list(a0);qq=[0]*max(0,len(rr)-len(bb)+1);inv=pow(bb[-1],P-2,P)
 while rr and len(rr)>=len(bb):
  j=len(rr)-len(bb);vv=rr[-1]*inv%P;qq[j]=vv
  for i,cc in enumerate(bb):rr[j+i]=(rr[j+i]-vv*cc)%P
  rr=ft(rr)
 qq=ft(qq);assert fa(fm(qq,bb),rr)==a0
 STAT['finiteFieldDivisions']+=1
 return qq,rr
def fx(a,b):
 r0,r1=ft(a),ft(b);s0,s1=[1],[];t0,t1=[],[1]
 while r1:
  qq,r2=fd(r0,r1)
  r0,r1=r1,r2;s0,s1=s1,fs(s0,fm(qq,s1));t0,t1=t1,fs(t0,fm(qq,t1))
 if not r0:return [],[],[]
 cc=pow(r0[-1],P-2,P)
 gg,ss,tt=fscale(r0,cc),fscale(s0,cc),fscale(t0,cc)
 assert fa(fm(ss,a),fm(tt,b))==gg
 STAT['finiteFieldBezoutChecks']+=1
 return gg,ss,tt
def fexact(a,b):
 qq,rr=fd(a,b);assert not rr;return qq
def fpower(a,n):
 out=[1]
 for _ in range(n):out=fm(out,a)
 return out
def from_poly(p):
 assert weight(p)
 out=[0]*(int(p.degrees()[0])+1) if p else []
 for ex,cc in p.to_dict().items():out[int(ex[0])]=cmod(cc)
 return ft(out)
def lift(a):return ctx.from_dict({(i,0,0):cc for i,cc in enumerate(a) if cc})
def fprofile(a):
 bb=json.dumps(a,separators=(',',':')).encode()
 return {'degree':len(a)-1,'terms':sum(bool(v) for v in a),
         'bytes':len(bb),'sha256':hashlib.sha256(bb).hexdigest()}
scalars=[from_poly(v[0]) for v in results]
gg=[];weights=[[],[],[]]
for j,cc in enumerate(scalars):
 if not cc:continue
 new,a,b=fx(gg,cc)
 weights=[fm(a,w) for w in weights];weights[j]=fa(weights[j],b);gg=new
assert gg==fa(fa(fm(weights[0],scalars[0]),fm(weights[1],scalars[1])),fm(weights[2],scalars[2]))
STAT['finiteFieldBezoutChecks']+=1
if not gg:
 say('new_joint_scalars_all_zero_mod1009',fixedGroups=GROUPS,
     noUnitOrExclusion=True,statistics=STAT)
else:
 Uf=from_poly(PAID);reduced=list(gg);removed=[1];layers=0
 while len(reduced)>1:
  common=fx(reduced,Uf)[0]
  if len(common)==1:break
  reduced=fexact(reduced,common);removed=fm(removed,common);layers+=1
 assert fm(reduced,removed)==gg
 support=fpower(Uf,layers);quotient=fexact(support,removed)
 weights=[fm(w,quotient) for w in weights]
 target=fm(support,reduced)
 assert target==fa(fa(fm(weights[0],scalars[0]),fm(weights[1],scalars[1])),fm(weights[2],scalars[2]))
 final=[sum((R(lift(weights[j]))*results[j][1][i] for j in range(3)),R()) for i in range(5)]
 for v in final:integral(v)
 difference=sum((final[i]*ORIGINAL[i] for i in range(5)),R())-R(lift(target))
 integral(difference)
 assert all(cmod(cc)==0 for cc in difference.n.to_dict().values())
 STAT['fiveSourceReturns']+=1
 say('new_joint_mod1009_complete_five_original_Bezout_return',
     fixedGroups=GROUPS,scalarProfiles=[fprofile(v) for v in scalars],
     exactJointGcd=fprofile(gg),onlyOldPaidSupportRemoved=fprofile(removed),
     remainingNecessaryLPolynomial=fprofile(reduced),
     originalPaidSupportPower=layers,actualTarget=fprofile(target),
     allFiveOriginalMultipliers=[rp(v) for v in final],
     allFiveOriginalCoefficientReturnsModulo1009=True,
     denominatorSupportOnlyPreviouslyPaidU=True,
     entireGenericPositiveEChartExcluded=(len(reduced)==1),
     noClaimFromGcdDegreeAlone=True,statistics=STAT)
say('new_joint_six_by_eighteen_five_original_input_finished',
    fixedGroups=GROUPS,statistics=STAT,
    oldSingletonResultantAndOldSixRayGateNotReplayed=True,
    noOtherWeightChartOrWholeWClaim=True,ordinaryISPClaim=False,
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    noCoefficientCacheWritten=True)
