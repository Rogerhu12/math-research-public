#!/usr/bin/env python3
"""NEW W/b0/cross-zero: THREE COMPLETE QQ constant fields.
Input parameters are the exact four canonical profiles already returned:
(4u+5)(6u-1)(20u^3-4u^2-20u+9)/480. No old nu resultants, old cover
gcd/factorization, C2/Loww/4x5/PRS or old positive target is rerun.
Only the necessary raw Gram/qf/ri/B0/B1 definitions are regenerated.
In each WHOLE K[nu], specialize before any head division, return the
three original heads, and remove only complete already-paid components.
If a finite nu algebra remains, keep all its multiplicities; recover f
by an actual B0 unit combination, return all FIVE original equations,
then use one degree<=6 lambda polynomial CONTAINER (not a quotient).
Only a complete original 1,D,D^2,D^3 identity excludes a physical fiber.
No D, lambda head, determinant or norm is inverted.
180 seconds/4 GiB; one dependency; one first mathematical execution.
"""
import gc,hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx,fmpq_mat
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('fixed original 180-second deadline')
def say(stage,**data):
 data.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(data,separators=(',',':')),flush=True)
BASE='2026-11-28-unit211-W-b0-entire-cross-zero-three-original-lambda-f-heads-8542.py'
BASE_SHA='1e41e505bf925b8f5e4422c60267efc9e0db6cc5f311daef9524efa9f44f372f'
text=Path(__file__).with_name(BASE).read_text()
assert hashlib.sha256(text.encode()).hexdigest()==BASE_SHA
prefix=text[text.index('ctx=fmpq_mpoly_ctx'):text.index('def source_return')]
assert len(prefix.encode())==10695
assert hashlib.sha256(prefix.encode()).hexdigest()=='ceecdcd9fcc81892ea2ad0c2918423ae283d1afbe63a2198583189e2b1e4ebeb'
# No old coefficient normalization, fixed projection, xgcd or factorization.
# This necessary definition prefix has no resource/timer/import/file actions.
ns={'fmpq_mpoly_ctx':fmpq_mpoly_ctx,'fmpq_poly':fmpq_poly,
    'hashlib':hashlib,'json':json,'say':lambda *a,**k:None}
exec(compile(prefix,'<necessary-four-original-means-and-three-heads>','exec'),ns)
tick()
R=ns['R'];ctx=ns['ctx'];lp=ns['lp'];fp=ns['fp']
u,nu,lam,ell,m,delta,M,Q=tuple(ns[k] for k in ('u','nu','lam','ell','m','delta','M','Q'))
Tb=ns['Tb'];Astar=ns['Astar'];on_b0=ns['on_b0']
A2=2*lam*lam-2*lam+1
Dphysical=ell*A2-Tb*Tb
Cstar=Astar*m*m+ns['J']*delta*ell*ell
ad=(M*ell*ell*Q*(3-4*lam)+M*Astar*Tb*Tb
    +2*M*u*Q*(3-2*lam)*ell*Tb+Dphysical*Cstar)
q2=2*ad/ell
assert ns['weight'](q2.d) and ns['fdeg'](q2)<=0
assert ns['geomdegree'](q2)<=2
raw_five=list(ns['original_b'])+[q2]
qtag=[ns['ck'](v) for v in ns['qtag']]
ri_tags=[row['tag'] for row in ns['rowdata']]
Arows=[on_b0(row['A']) for row in ns['rowdata']]
Bzero=ns['B0'];Bone=ns['B1'];paid_atoms=ns['paid_atoms']
for value in raw_five+[Dphysical]+Arows+Bzero+Bone:
 ns['ck'](value)
say('new_crosszero_three_fields_original_definitions_ready',
    necessaryPrefixBytes=10695,
    necessaryPrefixSHA256='ceecdcd9fcc81892ea2ad0c2918423ae283d1afbe63a2198583189e2b1e4ebeb',
    rawFiveNames=['E1','EBe','EBo','N1','q2'],
    rawFiveDegrees=[ns['geomdegree'](v) for v in raw_five],
    noOldNuProjectionOrCoverGcdRegenerated=True)

PARAMETERS=[
 ('linear_minus_five_quarters',[5,4],
  '9b702a5320030eb66ea9572167b2589cb503a6035fd67b350256e6248dcbe9ec'),
 ('linear_one_sixth',[-1,6],
  'c708effec8346a565d2ecf2264cb6635e4adeffe15c1ec12f222a57378d441ed'),
 ('entire_cubic',[9,-20,-4,20],
  'bf8d54f313b63c7f42b5f24b2bfc31e789f1c65ca2b4c5fd5bf3b8be236675b2')]
def parameter_profile(poly):
 data=[[[j,0,0,0,0],str(poly[j])] for j in range(poly.degree()+1) if poly[j]]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'degree':int(poly.degree()),'terms':len(data),'bytes':len(raw),
         'sha256':hashlib.sha256(raw).hexdigest()}
prod=fmpq_poly([1])
for name,co,sha in PARAMETERS:
 phi=fmpq_poly(co);assert parameter_profile(phi)['sha256']==sha;prod*=phi
G=prod/480
assert parameter_profile(G)['sha256']=='9f9544b1500bc385df9f8a04d4693c3895655712721661a109854be0845ea8d2'
assert prod==fmpq_poly([-45,334,-284,-684,424,480])
say('new_crosszero_exact_three_small_parameters',
    factors=[dict(name=name,**parameter_profile(fmpq_poly(co))) for name,co,sha in PARAMETERS],
    product=parameter_profile(G),allFourPublishedParameterSHAsMatch=True,
    noOldFactorizationOrProjectionRun=True)
outcomes=[]
def run_field(name,co,sha):
 tick()
 phi0=fmpq_poly(co);phi=phi0/phi0[phi0.degree()]
 nk=int(phi.degree())
 stats={'constantInverseProducts':0,'nuDivisionProducts':0,
        'nuBezoutProducts':0,'originalThreeHeadReturns':0,
        'oldPaidComponentProducts':0,'weightAlgebraInverseProducts':0,
        'fullOriginalFCoordinates':0,'QQInverseCoordinates':0,
        'wholeOriginalMatrixCoordinates':0,'targetMatrixCoordinates':0,
        'fullOriginalTargetCoordinates':0}
 class K:
  def __init__(self,v=0):
   if isinstance(v,K):self.p=v.p;return
   pp=v if isinstance(v,fmpq_poly) else fmpq_poly([v])
   self.p=pp%phi
  def __bool__(self):return bool(self.p)
  def __add__(self,v):return K(self.p+K(v).p)
  __radd__=__add__
  def __neg__(self):return K(-self.p)
  def __sub__(self,v):return self+-K(v)
  def __rsub__(self,v):return K(v)+-self
  def __mul__(self,v):return K(self.p*K(v).p)
  __rmul__=__mul__
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   a=self;out=K(1)
   while n:
    if n&1:out=out*a
    n//=2
    if n:a=a*a
   return out
  def inv(self):
   assert self
   gg,aa,bb=self.p.xgcd(phi)
   assert aa*self.p+bb*phi==gg and int(gg.degree())==0
   out=K(aa/gg[0]);assert self*out==K(1) and out*self==K(1)
   stats['constantInverseProducts']+=2;return out
  def __truediv__(self,v):return self*K(v).inv()
  def __eq__(self,v):return self.p==K(v).p
 K0=K();K1=K(1);ku=K(fmpq_poly([0,1]))
 def trim(p):
  p=list(p)
  while p and not p[-1]:p.pop()
  return p
 def add(a,b):
  return trim([(a[i] if i<len(a) else K0)+(b[i] if i<len(b) else K0)
       for i in range(max(len(a),len(b)))])
 def neg(a):return [-v for v in a]
 def sub(a,b):return add(a,neg(b))
 def scale(a,c):return trim([v*c for v in a])
 def mul(a,b):
  if not a or not b:return []
  out=[K0 for _ in range(len(a)+len(b)-1)]
  for i,x in enumerate(a):
   for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
  return trim(out)
 def power(a,n):
  assert isinstance(n,int) and n>=0
  out=[K1];a=trim(a)
  while n:
   if n&1:out=mul(out,a)
   n//=2
   if n:a=mul(a,a)
  return out
 def divide(a,b):
  tick();a=trim(a);b=trim(b);assert b
  if len(a)<len(b):return [],a
  rem=list(a);quot=[K0 for _ in range(len(a)-len(b)+1)];iv=b[-1].inv()
  while rem and len(rem)>=len(b):
   at=len(rem)-len(b);cc=rem[-1]*iv;quot[at]=quot[at]+cc
   for j,v in enumerate(b):rem[at+j]=rem[at+j]-cc*v
   rem=trim(rem)
  quot=trim(quot)
  assert add(mul(quot,b),rem)==a
  stats['nuDivisionProducts']+=1;return quot,rem
 def exactp(a,b):
  qq,rr=divide(a,b);assert not rr and mul(qq,b)==trim(a);return qq
 def bezout(a,b):
  a=trim(a);b=trim(b)
  r0,r1=a,b;s0,s1=[K1],[];t0,t1=[],[K1]
  while r1:
   qq,rr=divide(r0,r1)
   r0,r1=r1,rr;s0,s1=s1,sub(s0,mul(qq,s1));t0,t1=t1,sub(t0,mul(qq,t1))
  if not r0:return [],[],[]
  iv=r0[-1].inv();gg=scale(r0,iv);ss=scale(s0,iv);tt=scale(t0,iv)
  assert add(mul(ss,a),mul(tt,b))==gg
  stats['nuBezoutProducts']+=1;return gg,ss,tt
 def pp_profile(p):
  p=trim(p)
  raw=json.dumps([[str(cc.p[j]) for j in range(nk)] for cc in p],
       separators=(',',':')).encode()
  return {'nuDegree':len(p)-1,'constantFieldDegree':nk,'bytes':len(raw),
          'sha256':hashlib.sha256(raw).hexdigest()}
 def spweight(poly):
  assert ns['weight'](poly)
  dd=max((int(ex[1]) for ex in poly.to_dict()),default=-1)
  out=[K0 for _ in range(dd+1)]
  for ex,cc in poly.to_dict().items():
   assert all(int(ex[j])==0 for j in (2,3,4))
   at=int(ex[1]);out[at]=out[at]+K(cc)*ku**int(ex[0])
  return trim(out)
 units=[]
 for label,atom in paid_atoms:
  pa=spweight(atom);units.append((label,pa))
  if not pa:
   say('new_crosszero_whole_u_field_paid_zero',factor=name,paidSupport=label,
       wholeFieldExcluded=True,allQQEmbeddingsIncluded=True)
   return {'factor':name,'excluded':True,'reason':'original_paid_polynomial_identically_zero'}
 numer=[spweight(v.n) for v in Bone]
 denom=[spweight(v.d) for v in Bone]
 assert all(denom)
 head=[];headtags=[[],[],[]]
 for j,nn in enumerate(numer):
  gg,ss,tt=bezout(head,nn)
  headtags=[mul(ss,v) for v in headtags]
  headtags[j]=add(headtags[j],tt);head=gg
  assert trim(sum_poly([mul(headtags[i],numer[i]) for i in range(3)],add))==head
  stats['originalThreeHeadReturns']+=1
  say('new_crosszero_whole_field_three_head_nu_gcd',factor=name,
      inputIndex=j,head=pp_profile(head),allNuLeadingDropsRetained=True,
      exactThreeNumeratorCombinationReturned=True)
 if not head:
  say('new_crosszero_entire_nu_line_retained',factor=name,
      allThreeOriginalHeadsZeroAsPolynomials=True,noExclusion=True)
  return {'factor':name,'excluded':False,'reason':'entire_nu_line_retained'}
 common_den=mul(mul(denom[0],denom[1]),denom[2])
 original_tags=[mul(headtags[i],denom[i]) for i in range(3)]
 ret=[]
 for i in range(3):
  ret=add(ret,mul(mul(original_tags[i],numer[i]),exactp(common_den,denom[i])))
 assert ret==mul(head,common_den)
 stats['originalThreeHeadReturns']+=1
 good=list(head);removed=[K1];inv_num=[K1];inv_den=[K1];removed_history=[]
 for label,pa in units:
  layers=0
  while len(good)>1:
   gg,ss,tt=bezout(good,pa)
   if len(gg)<=1:break
   quotient=exactp(pa,gg);good=exactp(good,gg);removed=mul(removed,gg)
   inv_num=mul(inv_num,quotient);inv_den=mul(inv_den,pa);layers+=1
   assert mul(good,removed)==head and mul(removed,inv_num)==inv_den
   stats['oldPaidComponentProducts']+=2
  if layers:removed_history.append({'paidSupport':label,'gcdLayers':layers})
 assert good
 say('new_crosszero_whole_field_complete_paid_component_return',
     factor=name,originalHead=pp_profile(head),retainedNu=pp_profile(good),
     removedOldPaidComponents=removed_history,
     allRetainedNuMultiplicitiesIncluded=True)
 if len(good)==1:
  unit_num=scale(inv_num,good[0].inv())
  assert mul(head,unit_num)==inv_den
  final_tags=[mul(unit_num,tt) for tt in original_tags]
  ret=[]
  for i in range(3):
   ret=add(ret,mul(mul(final_tags[i],numer[i]),exactp(common_den,denom[i])))
  assert ret==mul(inv_den,common_den)
  stats['originalThreeHeadReturns']+=1
  say('new_crosszero_whole_u_field_original_paid_unit_return',
      factor=name,oldPaidPositiveTarget=pp_profile(inv_den),
      completeThreeOriginalRationalHeadsReturned=True,
      wholeFieldExcluded=True,noNewNuOrGeometricInverse=True,statistics=stats)
  return {'factor':name,'excluded':True,'reason':'complete_original_heads_paid_unit'}
 # The WHOLE retained finite algebra, possibly nonreduced or reducible.
 # No root, irreducible factor, norm or geometric head is selected.
 nn=len(good)-1;ADIM=nk*nn
 class A:
  def __init__(self,v=0):
   if isinstance(v,A):self.p=v.p;return
   pp=v if isinstance(v,list) else [K(v)]
   pp=trim(pp)
   self.p=divide(pp,good)[1] if len(pp)>=len(good) else pp
  def __bool__(self):return bool(self.p)
  def __add__(self,v):return A(add(self.p,A(v).p))
  __radd__=__add__
  def __neg__(self):return A(neg(self.p))
  def __sub__(self,v):return self+-A(v)
  def __rsub__(self,v):return A(v)+-self
  def __mul__(self,v):return A(mul(self.p,A(v).p))
  __rmul__=__mul__
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   out=A(1);base=self
   while n:
    if n&1:out=out*base
    n//=2
    if n:base=base*base
   return out
  def inv(self):
   gg,ss,tt=bezout(self.p,good)
   assert len(gg)==1
   out=A(scale(ss,gg[0].inv()))
   assert self*out==A(1) and out*self==A(1)
   stats['weightAlgebraInverseProducts']+=2;return out
  def __truediv__(self,v):return self*A(v).inv()
  def __eq__(self,v):return not sub(self.p,A(v).p)
 A0=A();Aone=A(1)
 for label,pa in units:
  av=A(pa);iv=av.inv();assert av*iv==Aone
 denominator_cache={}
 def deninv(poly):
  key=str(poly)
  if key not in denominator_cache:
   pa=spweight(poly);assert pa
   denominator_cache[key]=A(pa).inv()
  return denominator_cache[key]
 def weightvalue(v):
  v=R(v);assert ns['weight'](v.n) and ns['weight'](v.d)
  return A(spweight(v.n))*deninv(v.d)
 def clean2(dic):return {key:val for key,val in dic.items() if val}
 def ga(a,b):
  out=dict(a)
  for key,val in b.items():out[key]=out.get(key,A0)+val
  return clean2(out)
 def gn(a):return {key:-val for key,val in a.items()}
 def gs(a,b):return ga(a,gn(b))
 def gc(a,c):return clean2({key:val*c for key,val in a.items()})
 def gm(a,b):
  out={}
  for (i,j),x in a.items():
   for (k,l),y in b.items():
    key=(i+k,j+l);out[key]=out.get(key,A0)+x*y
  return clean2(out)
 def gp(a,n):
  assert n>=0
  out={(0,0):Aone}
  while n:
   if n&1:out=gm(out,a)
   n//=2
   if n:a=gm(a,a)
  return out
 def original_poly(v):
  v=R(v);assert ns['weight'](v.d)
  iv=deninv(v.d);groups={}
  for ex,cc in v.n.to_dict().items():
   assert not int(ex[3])
   key=(int(ex[2]),int(ex[4]));j=int(ex[1])
   pp=groups.setdefault(key,[])
   while len(pp)<=j:pp.append(K0)
   pp[j]=pp[j]+K(cc)*ku**int(ex[0])
  return clean2({key:A(trim(pp))*iv for key,pp in groups.items()})
 vals=[original_poly(v) for v in raw_five]
 bzero=[weightvalue(v) for v in Bzero]
 assert all(weightvalue(v)==A0 for v in Bone)
 aa=[original_poly(v) for v in Arows]
 assert all(all(j==0 for i,j in pp) for pp in aa)
 # A true B0 unit combination is newly returned in this WHOLE algebra.
 gg=list(good);g0tag=[K1];vtags=[[],[],[]]
 for j,bv in enumerate(bzero):
  newg,ss,tt=bezout(gg,bv.p)
  g0tag=mul(ss,g0tag);vtags=[mul(ss,vv) for vv in vtags]
  vtags[j]=add(vtags[j],tt);gg=newg
  ret=mul(g0tag,good)
  for i in range(3):ret=add(ret,mul(vtags[i],bzero[i].p))
  assert ret==gg
 assert len(gg)==1
 vi=[A(scale(vv,gg[0].inv())) for vv in vtags]
 assert sum((vi[i]*bzero[i] for i in range(3)),A0)==Aone
 gpoly={}
 for i in range(3):gpoly=ga(gpoly,gc(aa[i],vi[i]))
 assert all(j==0 and i<=2 for i,j in gpoly)
 Rline=ga({(0,1):Aone},gpoly)
 rcoeff=[sum((vi[i]*weightvalue(ri_tags[i][j]) for i in range(3)),A0) for j in range(4)]+[A0]
 rback={}
 for j in range(5):rback=ga(rback,gc(vals[j],rcoeff[j]))
 assert rback==Rline
 stats['fullOriginalFCoordinates']+=len(set(rback)|set(Rline))
 # Simultaneous SAME f: F_i = U_i + Q_i (f+g), in the full ordinary
 # lambda,f polynomial algebra over A, NOT merely a chosen quotient basis.
 ups=[];qparts=[]
 for vv in vals:
  assert max((b for a,b in vv),default=-1)<=2
  coeffs=[clean2({(a,0):cc for (a,b),cc in vv.items() if b==j}) for j in range(3)]
  up=ga(gs(coeffs[0],gm(coeffs[1],gpoly)),gm(coeffs[2],gm(gpoly,gpoly)))
  qq=ga(coeffs[1],gm(coeffs[2],gs({(0,1):Aone},gpoly)))
  assert ga(up,gm(qq,Rline))==vv
  assert all(b==0 for a,b in up)
  stats['fullOriginalFCoordinates']+=len(set(vv)|set(up)|set(gm(qq,Rline)))
  ups.append(up);qparts.append(qq)
 Dpoly=original_poly(Dphysical)
 assert all(b==0 and a<=2 for a,b in Dpoly)
 # Retain every q2 head-zero fiber. Its three coefficients have the
 # published unit combination -32*L, checked here in the entire A.
 kap=weightvalue(ns['kappa'])
 Lunit=weightvalue(u*Q*delta*ell*ns['kappa']*ns['kappa'])
 q2a=[vals[4].get((j,0),A0) for j in range(3)]
 assert q2a[2]+3*q2a[1]+4*q2a[0]==-32*Lunit
 assert Lunit*Lunit.inv()==Aone
 def flatA(av):
  av=A(av)
  return [(av.p[j].p[h] if j<len(av.p) else fmpq(0)) for j in range(nn) for h in range(nk)]
 basis=[];basis_tags=[]
 for j in range(nn):
  for h in range(nk):
   basis.append(A([K0]*j+[ku**h]));basis_tags.append([j,h])
 assert len(basis)==ADIM
 CAP=6;NROWS=(CAP+1)*ADIM
 def flatU(pp):
  assert all(b==0 and a<=CAP for a,b in pp)
  out=[]
  for j in range(CAP+1):out.extend(flatA(pp.get((j,0),A0)))
  assert len(out)==NROWS;return out
 columns=[];column_tags=[]
 for i,pp in enumerate(ups):
  if not pp:continue
  deg=max(a for a,b in pp)
  assert deg<=4
  for shift in range(CAP-deg+1):
   for k,base in enumerate(basis):
    col={(a+shift,0):cc*base for (a,b),cc in pp.items()}
    columns.append(flatU(clean2(col)));column_tags.append([i,shift,k])
 say('new_crosszero_finite_nu_same_f_original_container',
     factor=name,constantFieldDegree=nk,wholeNuDegree=nn,weightQQDimension=ADIM,
     lambdaContainerMaximumDegree=CAP,originalUnivariateDegrees=[max((a for a,b in p),default=-1) for p in ups],
     shape=[NROWS,len(columns)],allFiveSameFPolynomialIdentitiesReturned=True,
     notALambdaQuotientOrFreeOriginalAlgebra=True,
     allQ2LeadingZeroAndNonreducedNuComponentsRetained=True)
 tick()
 if not columns:
  say('new_crosszero_no_original_container_columns',factor=name,noExclusion=True)
  return {'factor':name,'excluded':False,'reason':'no_original_columns'}
 MAT=fmpq_mat([[columns[j][i] for j in range(len(columns))] for i in range(NROWS)])
 RR,rank=MAT.rref();rank=int(rank)
 selected=[next(j for j in range(len(columns)) if RR[i,j]) for i in range(rank)]
 if rank:
  NM=fmpq_mat([[MAT[i,j] for j in selected] for i in range(NROWS)])
  RT,rnk=NM.transpose().rref();assert int(rnk)==rank
  selected_rows=[next(j for j in range(NROWS) if RT[i,j]) for i in range(rank)]
  square=fmpq_mat([[MAT[i,j] for j in selected] for i in selected_rows])
  inverse=square.inv()
  ident=fmpq_mat([[int(i==j) for j in range(rank)] for i in range(rank)])
  assert square*inverse==ident and inverse*square==ident
  stats['QQInverseCoordinates']+=2*rank*rank
  restricted=fmpq_mat([[MAT[i,j] for j in range(len(columns))] for i in selected_rows])
  assert NM*inverse*restricted==MAT
  stats['wholeOriginalMatrixCoordinates']+=NROWS*len(columns)
 else:NM=None;inverse=None;selected_rows=[]
 say('new_crosszero_complete_QQ_original_container_rank',
     factor=name,shape=[NROWS,len(columns)],rank=rank,
     actualSelectedOriginalColumns=selected,
     allOriginalColumnsReturned=True if rank else not any(any(c) for c in columns),
     noDimensionOrEmptinessClaimFromRankAlone=True)
 found=None
 targets=[('one',0,{(0,0):Aone})]+[('Dphysical',n,gp(Dpoly,n)) for n in (1,2,3)]
 for label,powerD,target in targets:
  tick();rhs=flatU(target)
  if rank:
   solution=inverse*fmpq_mat([[rhs[i]] for i in selected_rows])
   back=NM*solution
   ok=all(back[i,0]==rhs[i] for i in range(NROWS))
  else:solution=None;ok=not any(rhs)
  say('new_crosszero_actual_original_positive_target',
      factor=name,target=label,power=powerD,allContainerCoordinatesReturned=ok)
  if not ok:continue
  stats['targetMatrixCoordinates']+=NROWS
  omega=[{} for _ in range(5)]
  if rank:
   for t,jcol in enumerate(selected):
    i,shift,k=column_tags[jcol]
    av=basis[k]*A(K(solution[t,0]))
    omega[i]=ga(omega[i],{(shift,0):av} if av else {})
  total={}
  for i in range(5):total=ga(total,gm(omega[i],ups[i]))
  assert total==target
  qsum={}
  for i in range(5):qsum=ga(qsum,gm(omega[i],qparts[i]))
  actual_multipliers=[gs(omega[i],gc(qsum,rcoeff[i])) for i in range(5)]
  total={}
  for i in range(5):total=ga(total,gm(actual_multipliers[i],vals[i]))
  assert total==target
  stats['fullOriginalTargetCoordinates']+=len(set(total)|set(target))
  compact=[[i,a,b,[str(v) for v in flatA(cc)]] for i,pp in enumerate(actual_multipliers)
       for (a,b),cc in sorted(pp.items())]
  raw=json.dumps(compact,separators=(',',':')).encode()
  say('new_crosszero_full_five_original_polynomial_target_return',
      factor=name,target=label,power=powerD,
      allFiveActualOriginalMultipliersReturned=True,
      fullOrdinaryLambdaFPolynomialIdentityReturned=True,
      certificateBytes=len(raw),certificateSHA256=hashlib.sha256(raw).hexdigest(),
      onlyOldPaidWeightInverses=True,noDOrNewGeometricHeadInverse=True,
      allQQEmbeddingsAndWholeNuMultiplicitiesPreserved=True)
  found=powerD;break
 say('new_crosszero_whole_constant_field_finished',
     factor=name,constantFieldDegree=nk,wholeNuDegree=nn,
     weightQQDimension=ADIM,originalContainerShape=[NROWS,len(columns)],
     originalContainerRank=rank,positiveDpowerReturned=found,
     wholeFieldExcluded=found is not None,
     remainingWholeAlgebraRetained=found is None,statistics=stats)
 return {'factor':name,'excluded':found is not None,
         'reason':'full_original_positive_target' if found is not None else 'unreturned_entire_algebra',
         'Dpower':found,'retainedNuDegree':nn,'weightQQDimension':ADIM}
def sum_poly(values,addfn):
 out=[]
 for pp in values:out=addfn(out,pp)
 return out
for name,co,sha in PARAMETERS:
 outcomes.append(run_field(name,co,sha))
 tick();gc.collect()
say('new_crosszero_three_entire_constant_fields_finished',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    fields=outcomes,wholeCurrentCrossZeroExcluded=all(o['excluded'] for o in outcomes),
    originalG5HasAllThreeSimpleQQFactors=True,
    noWholeBzeroOrWholeWEmptinessClaim=True,
    allUnreturnedFieldsRetained=True,
    maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    noOldProjectionFactorOrPositiveTargetReplayed=True,
    noLargeCoefficientPayloadOrCacheWritten=True,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)
