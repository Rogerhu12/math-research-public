#!/usr/bin/env python3
"""NEW complete H198-complement original value model in twenty x two rows.
Eliminate the actual N1 coordinate. Three mean quadratics in Z, minus
their Z^2 coefficients times the proved monic qZ, give three LINEAR
relations. NS/PS add two. In the explicit monic quadratic environment,
these five rows and Z times each give the EXACT original I6 quotient.
The new five original conditions qT4,R6,Nlow,Plow,entire N4(V) are first
reduced by the genuine THREE mean matrices, then undergo only ONE
N1-coordinate change; their Z products give the exact enlarged I11.
This avoids T^6 iteration in the large H198-denominator Z environment.
Complete original source DAGs, no free three-generator assumption.
Two new fixed pairs use R6/N4(V) and individual Nlow/Plow.
180s /4GiB. No old norm, old determinant, old module or payload cache.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
started=time.perf_counter();deadline=started+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-started
 print(json.dumps(kw,separators=(',',':')),flush=True)
path=Path(__file__).with_name(
 '2026-11-28-unit211-W-original-N1-slope-weight-coordinate-monic-square-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='9b7731d221175a88edbf7f98bb1c811402ab1d8e332b94fb005dd073b7894d00'
marka=b'\nscalar,factors=remaining.factor()';markb=b'\ndef pay_chart(p):'
markend=b"\nsay(stage='new_W_N1_slope_coordinate_monic_square_complete_original_return',"
assert raw.count(marka)==raw.count(markb)==raw.count(markend)==1
parta=raw.split(marka)[0];partb=markb+raw.split(markb)[1].split(markend)[0]
assert len(parta)==4799 and hashlib.sha256(parta).hexdigest()=='be7547a34352074e9fd8ded0bfb8ede4ef0179614c5b72527483ffaaf2165871'
assert len(partb)==1851 and hashlib.sha256(partb).hexdigest()=='060d92ecc52c08cabb909b7c3d8b8b86f5dae62a7bda9e385fa8d453596287ab'
ns={'__file__':str(path),'__name__':'necessary_original_N1_coordinate_and_square_for_new_full_values'}
saved_alarm=signal.alarm;saved_setitimer=signal.setitimer
def bounded_setitimer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return saved_setitimer(which,seconds,interval)
 assert not interval
 remaining=max(.001,deadline-time.perf_counter())
 return saved_setitimer(which,min(remaining,float(seconds) if seconds>0 else remaining),0.0)
def bounded_alarm(seconds):
 previous=bounded_setitimer(signal.ITIMER_REAL,seconds)
 return math.ceil(previous[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_setitimer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(parta+partb,str(path)+'#new_twenty_two_original_model_definition','exec'),ns)
finally:
 signal.alarm=saved_alarm;signal.setitimer=saved_setitimer
saved_setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
tri=ns['tri'];phys=tri['ns'];old=phys['ns']
R=ns['R'];ctx=ns['ctx'];zero=ns['zero'];one=ns['one']
ep,kp,xp,yp,Lp,Zp=ctx.gens()[:6]
xx,yy,L,Z=[ns[k] for k in ['x','y','L','Z']]
xhat,yhat=ns['xhat'],ns['yhat'];Delta=ns['Delta']
aa,cc=ns['a'],ns['c'];p0,p1,p2=ns['nrow']
ntag=ns['ntag'];qZ=ns['qZ'];beta0,beta1=ns['beta0'],ns['beta1']
original=ns['original'];pay=ns['pay'];strip=ns['strip']
pay_chart=ns['pay_chart'];legal=ns['legal'];profile=ns['profile'];rp=ns['rp']
assert Delta and not ns['whole'] and ntag[3]==1 and not ntag[4] and not ntag[5]
assert aa*p2-cc*p1==Delta
def coeff_only(co,chart=False):
 co=R(co)
 assert all(not any(mm[j] for j in [2,3,5,6,7]) for mm in co.n.to_dict())
 assert all(not any(mm[j] for j in range(2,8)) for mm in co.d.to_dict())
 (pay_chart if chart else pay)(co.d)
 return co
def strip_chart(poly):
 assert poly
 rest,removed,hist=strip(poly);assert rest*removed==poly
 ct=0
 while rest.total_degree()>0:
  gg=rest.gcd(Delta.n)
  if gg.total_degree()==0:break
  qq=rest/gg;assert qq*gg==rest
  rest=qq;removed*=gg;ct+=1
 assert rest*removed==poly;pay_chart(removed)
 return rest,removed,hist,ct
def clear_two(row):
 for co in row:coeff_only(co,True)
 if not any(row):return [zero,zero],R(1)
 den=one
 for co in row:den*=co.d/den.gcd(co.d)
 pay_chart(den)
 pp=[co.n*(den/co.d) for co in row]
 common=pp[0].gcd(pp[1])
 _,removed,_,_=strip_chart(common)
 pp2=[p/removed for p in pp]
 assert all(pp2[j]*removed==pp[j] for j in range(2))
 scalar=next(p for p in pp2 if p).coefficient(0)
 pp2=[p/scalar for p in pp2]
 factor=R(den,removed)/scalar
 assert all(R(pp2[j])==factor*row[j] for j in range(2))
 return pp2,factor
rows=[];labels=[];source_nodes=[]
def save_two(label,row,origin):
 for co in row:coeff_only(co,True)
 out,scale=clear_two(row)
 rows.append(out);labels.append(label)
 source_nodes.append((origin,scale))
 say(stage='new_twenty_two_original_relation',label=label,
     entries=[profile(p) for p in out],
     allTwoPolynomialScalingProductsReturned=True,
     originalSource=origin,
     unpaidContentsRetained=True,entireH198ZeroPreserved=True,
     claimExcluded=False)
 return out
def add_pair(label,row,origin):
 save_two(label,row,origin)
 zr=[-beta0*row[1],row[0]-beta1*row[1]]
 assert (row[0]+row[1]*Z)*Z-zr[0]-zr[1]*Z==row[1]*qZ
 save_two(label+'*Z',zr,origin+'; actual Z multiplication modulo qZ')
def change_three(row):
 r0,r1,r2=[coeff_only(v) for v in row]
 kappa=(-cc*r1+aa*r2)/Delta
 s0=r0+(cc*r1-aa*r2)*p0/Delta
 s1=(p2*r1-p1*r2)/Delta
 assert s0+kappa*p0==r0
 assert aa*s1+kappa*p1==r1
 assert cc*s1+kappa*p2==r2
 for co in [s0,s1,kappa]:coeff_only(co,True)
 return [s0,s1],kappa
# The exact I4 construction: invertible (1,x,y)->(1,Z,Nrow).
# No commutator is silently set zero in a free three-dimensional space.
images=[xhat,yhat,L]
mean_sub=[phys['subst'](original[i],images) for i in range(3)]
n1_sub=phys['subst'](original[3],images)
for co in ntag+ns['ztag']:coeff_only(co)
assert n1_sub+sum((ntag[i]*mean_sub[i] for i in range(3)),R())==0
assert qZ==-sum((ns['ztag'][i]*mean_sub[i] for i in range(3)),R())
for i,ff in enumerate(mean_sub):
 cs=ns['zcoeff'](ff);assert max(cs,default=-1)<=2
 head=cs.get(2,R())
 linear=ff-head*qZ
 lc=ns['zcoeff'](linear);assert max(lc,default=-1)<=1
 assert linear+head*qZ==ff
 add_pair('mean_linear_'+str(i),[lc.get(0,R()),lc.get(1,R())],
          'Fmean_i(xhat,yhat)-[Z^2]Fmean_i*qZ')
for i,label in [(4,'NS'),(5,'PS')]:
 r,tag=tri['reduce_row'](original[i],[R(int(j==i)) for j in range(6)])
 assert not tag[3] and tag[i]==1
 rr,kappa=change_three(r)
 add_pair(label,rr,'actual original '+label+' mean reduction minus kappa*Nrow')
assert len(rows)==10
say(stage='new_exact_original_I6_ten_by_two_completed',
 basis=['1','Z'],formalRows=10,
 allThreeOriginalMeanQuadraticsAndN1Recovered=True,
 qZActuallyReturnedAsCombinationOfThreeSubstitutedMeans=True,
 exactI6OverExplicitH198Complement=True,
 originalNSPSAndTheirZMultiplesRetained=True,
 noFreenessOfOriginalQuotientAssumed=True,
 noOldFifteenCofactorOrNormExecuted=True,claimExcluded=False)

# Genuine mean quotient arithmetic. Each node is a full original
# polynomial modulo the three means, NOT a vector in a presumed free
# algebra. Mx/My and their actual error traces were returned by the
# frozen prefix. Multiplication uses one fixed order and the full
# original error identity, so every node has an exact source DAG.
Mx,My=tri['matrices'];Ex,Ey=tri['errors']
nodes=[]
def new_node(op,data,row):
 for co in row:coeff_only(co)
 index=len(nodes);nodes.append((op,data))
 return index
class A3:
 __slots__=('row','node')
 def __init__(self,value=0):
  if isinstance(value,A3):self.row=value.row;self.node=value.node;return
  co=coeff_only(value);self.row=[co,R(),R()]
  self.node=new_node('scalar',co,self.row)
 @classmethod
 def from_row(cls,row,op,data):
  out=object.__new__(cls);out.row=row;out.node=new_node(op,data,row);return out
 def __neg__(self):
  return A3.from_row([-c for c in self.row],'neg',self.node)
 def __add__(self,other):
  other=A3(other)
  return A3.from_row([a+b for a,b in zip(self.row,other.row)],'add',[self.node,other.node])
 __radd__=__add__
 def __sub__(self,other):return self+-A3(other)
 def __rsub__(self,other):return A3(other)+-self
 def __mul__(self,other):
  other=A3(other);ar=self.row;br=other.row
  if not br[1] and not br[2]:
   row=[c*br[0] for c in ar]
  elif not ar[1] and not ar[2]:
   row=[ar[0]*c for c in br]
  else:
   row=[br[0]*ar[j]+sum((ar[i]*(br[1]*Mx[i][j]+br[2]*My[i][j]) for i in range(3)),R())
        for j in range(3)]
  # Exact defect for the two represented LINEAR polynomials is
  # sum_i ar_i*(br_1*Ex_i+br_2*Ey_i).F6. Combine with the two existing
  # source DAGs by multiplication; no matrix commutation is assumed.
  return A3.from_row(row,'mul',[self.node,other.node])
 __rmul__=__mul__
 def __truediv__(self,other):
  co=coeff_only(other)
  assert all(not any(mm[j] for j in range(2,8)) for mm in co.n.to_dict())
  pay(co.n)
  return A3.from_row([c/co for c in self.row],'divide_paid_weight',[self.node,co])
 def __pow__(self,power):
  assert power>=0
  out=A3(1);base=self
  while power:
   if power&1:out=out*base
   power//=2
   if power:base=base*base
  return out
def original_geometry(name,oldpoly):
 pp=phys['subst'](oldpoly,[xx,yy,phys['tnew']])
 rr,tag=tri['reduce_row'](pp)
 assert not tag[3] and not tag[4] and not tag[5]
 # reduce_row actually returns rr.(1,x,y)-pp=tag.Fmean.
 return A3.from_row(rr,'actual_original_geometry_base',[name,tag])
def add_value(label,value,definition):
 value=A3(value)
 rr,kappa=change_three(value.row)
 add_pair(label,rr,definition+'; mean DAG node '+str(value.node)+'; minus kappa*Nrow')
 say(stage='new_original_value_first_reduced_by_three_means_then_changed_once',
     label=label,threeRowProfiles=[rp(c) for c in value.row],
     originalDAGNode=value.node,sourceDAGOperations=len(nodes),
     allThreeFinalCoordinateProductsReturned=True,
     noHighPowersOfH198UsedInValueReduction=True,
     noDNormOrLambdaInverse=True,claimExcluded=False)

u,Q,ell,M,P02=[old[z] for z in ['u','Q','l','M','P02']]
J=old['J'];m=u-ell;delta=1-Q
for unit in [m,u,Q,ell,delta,M]:
 pay(unit.n);pay(unit.d)
T=original_geometry('actual original T',old['T'])
Al=2*L*L-2*L+1;Bl=4*L**3-6*L*L+3*L-1
T2=T*T;T3=T2*T
D=A3(ell*Al)-T2
K=A3(ell*ell*Bl)-T*(3*ell*Al)+T3*2
D2=D*D
Ast=4*u*Q-J;Cst=Ast*m*m+J*delta*ell*ell;cval=3-2*L
ad=A3(M*ell*ell*Q*(3-4*L))+T2*(M*Ast)+T*(2*M*u*Q*cval*ell)+D*Cst
bd=(T*Ast+A3(u*Q*cval*ell))*(2*M*m)
C4=(D*ad)*(2*m)+K*bd
qT4=C4/(8*m*u*Q*ell*ell*delta)
add_value('original_qT4',qT4,'full original C4 divided only by its published paid weight head')
R6=(K*K)*M-(D2*D)*(4*m*m)
add_value('original_R6',R6,'full same-value moment M*K^2-4*m^2*D^3')
Nold,Pold=old['N4'],old['P2'];gram=old['rows']
nb=original_geometry('complete odd rho coefficient N4(rowB)',Nold(gram[2]).b)
pb=original_geometry('complete odd rho coefficient P2(rowB)',Pold(gram[2]).b)
A0=A3(1)+T/ell
Nlow=D*nb+(K*A0)*(2*L*P02/m)+D2*(4*L*P02*m/(ell*M))
add_value('original_Nlow',Nlow,
          'complete D-linear N odd identity; NS and R6 recover even N')
Plow=D*pb+(K*A0*A0)*(3*P02/(2*m))+(K*D)*(P02*(3*m*m/(ell*ell)+delta)/(2*m*M))+(A0*D2)*(6*P02*m/(ell*M))
add_value('original_Plow',Plow,
          'complete D-linear P odd identity; PS and R6 recover even P')
Eold=old['E'];l0=old['l'];m0=old['u']-l0;t0=old['T'];lam0=old['lam']
V0=[Eold(1),Eold(lam0-1-t0),Eold(1+t0/l0),Eold(1+t0/l0)]
V1=[Eold(),Eold(),Eold(m0/l0,-1),Eold(m0/l0,1)]
Z0raw=Nold(V0);Z2raw=Nold(V1)
Z1raw=Nold([V0[j]+V1[j] for j in range(4)])-Z0raw-Z2raw
assert not Z0raw.b and not Z1raw.b and not Z2raw.b
Z0=original_geometry('entire N4(V0)',Z0raw.a)
Z1=original_geometry('entire N4 polarized V0,V1',Z1raw.a)
Z2=original_geometry('entire N4(V1)',Z2raw.a)
Vlow=D*Z0+(K*Z1)/(2*m)+(D2*Z2)/M
add_value('original_entire_Vlow',Vlow,
          'D*N4(V0)+K*N4polar(V0,V1)/(2m)+D^2*N4(V1)/M; no Phi multiple substitute')
assert len(rows)==20 and len(labels)==20
say(stage='new_complete_original_eleven_equation_twenty_by_two_model',
 exactRing='A_W[H198^-1][lambda]',
 actualRowCount=20,basis=['1','Z'],
 originalElevenEquations=['E1','EBe','EBo','N1','NS','PS','qT4','R6','Nlow','Plow','entire_Vlow'],
 exactOriginalI11QuotientByMonicQZAndTenLinearGenerators=True,
 allTenZProductsActuallyReturned=True,
 allOriginalValueDAGsFirstUseOnlyThreeMeanRules=True,
 physicalDNonzeroScopeForPublishedFullValueEquivalenceRetained=True,
 noDInverseOrDNormInverseUsedInNewAlgebra=True,
 noUnpaidLambdaLeadingOrWeightContentRemoved=True,
 entireH198ZeroBranchRetained=True,
 noFreeOriginalModuleAssumed=True,
 finalExpandedLargeOriginalMultipliersNotClaimed=True,
 sourceDAGOperations=len(nodes),wholeWExcluded=False)

# Two genuinely new pairs, each using individual original values.
pairs=[('moment_and_entire_original_N4V',['original_R6','original_entire_Vlow']),
       ('both_individual_original_N_P',['original_Nlow','original_Plow'])]
for name,which in pairs:
 ra,rb=[rows[labels.index(label)] for label in which]
 omega=[rb[1],-ra[1]]
 if not any(omega):
  say(stage='new_value_pair_already_constant',name=name,labels=which,
      originalConstantRows=[profile(ra[0]),profile(rb[0])],
      noRankOrNonzeroClaim=True,wholeWExcluded=False)
  continue
 common=omega[0].gcd(omega[1]);assert common
 primitive=[v/common for v in omega]
 assert all(primitive[j]*common==omega[j] for j in range(2))
 scalar=primitive[0]*ra[0]+primitive[1]*rb[0]
 assert primitive[0]*ra[1]+primitive[1]*rb[1]==0
 assert common*scalar==ra[0]*rb[1]-ra[1]*rb[0]
 say(stage='new_full_value_two_column_original_cofactor_returned',
     name=name,labels=which,cancelledOnlyBothActualMultiplierContent=profile(common),
     originalScalar=profile(scalar),bothColumnProductsReturned=True,
     completeCommonFactorZeroFibrePreserved=True,
     allUnpaidHeadsAndContentRetained=True,wholeWExcluded=False)
 if not scalar:continue
 out,paid,hist,hct=strip_chart(scalar)
 norm=out.coefficient(0);out=out/norm;unit=paid*norm
 assert unit*out==scalar;pay_chart(unit)
 coeffs=[R(v,unit) for v in primitive]
 assert coeffs[0]*R(ra[0])+coeffs[1]*R(rb[0])==R(out)
 assert coeffs[0]*R(ra[1])+coeffs[1]*R(rb[1])==0
 say(stage='new_full_value_two_column_scalar_paid_normalization',
     name=name,definition=profile(out),paidFactorLabels=hist,
     explicitH198ComplementRemovals=hct,
     finalBothOriginalColumnProductsReturned=True,
     allOtherWeightAndLambdaLeadingFactorsUnpaid=True,wholeWExcluded=False)
say(stage='new_H198_complete_original_twenty_two_model_and_value_pairs_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 allTwentyRowsActuallyConstructed=True,
 noOldC8NormTwelveResultantEighteenModuleOrNativeDeterminantExecuted=True,
 noOldSixTwelveColumnFullValueGateReplayed=True,
 noCoefficientPayloadCacheEncodedOrSplitOutputWritten=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 wholeWExcluded=False,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
