#!/usr/bin/env python3
"""New general LS projective quadratic-head directions after the whole J=Q exclusion.
Use the paid fixed four-head inverse and an exact two-chart rank-one description.
Every new coefficient and fixed quadratic-pair identity is symbolic over QQ.
No old fifteen-minor atlas scan, finite samples, or old boundary gate is rerun.
120 seconds / 1 GiB.
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import signal
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(x=None,**kw):
 if x is None:x=kw
 x['seconds']=time.perf_counter()-start;print(json.dumps(x),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','Q','ell','x','y','t','zeta','dummy'),'lex');ep,kp,Lp,Tp,fp,tp,zp,dp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d);assert d
  if not n:self.n=zz;self.d=oo;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);assert o;return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):o=R(o);return self.n*o.d==o.n*self.d
m,qp,l,x0,x1,t,zeta=map(R,ctx.gens()[:7]);u=m;Q=qp;Delta=1-Q
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)
b=E(l/2,(u-l)/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,1);q=p.conj();bc=(l*l-(u-l)**2/Delta)/4
ivdiff=E(0,-1/(2*Delta));ivbp=c*q*ivdiff*E(1/(bc*Q));ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
V2=2*u-l*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
X=E(x0,x1);Y=X.conj()
f=(u*x0+(u-l*Q)*x1-T0/2)/(2*u)
W2=V2*x0+(2*u-u*Q-l*Q)*x1
lam=(W2-u*T0-(V2+2*u*u)*f+bc*Q*t)/P02
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
g=lam*P02-(1-u)*T0
T=(g*T0-Pf*f-Phi*bc*Q*t)/(Q*P02)-l
r=X-a*p-c*E(t);s=Y-a*q-b*E(t);A=E(2*f)-2*b*X-2*c*Y+E(2*bc*t)
rows=[[E(),E(),p,q],[E(),A,r,s],[p,r,E(),E(t)],[q,s,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(a,v):return [a*b for b in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert F2==E(2*f)
def mean(j):
 ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert not mean(0)
E1,EB,EC=mean(1),mean(2),mean(3)
assert not E1.b and EB.conj()==EC

def N4(v):
 return 2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
v=rows[0];zzv=rows[1]
Nv=N4(va(v,zzv))-N4(v)-N4(zzv)
vc=va(v,vs(-tau(v),one));zc=va(zzv,vs(-tau(zzv),one))
Pj=3*tau(vm(vm(vc,vc),zc))
NH=Nv-E(lam*fmpq(4,3))*Pj
assert not NH.b




assert N4(rows[0])==E(2*lam*P02)
assert Pj==E(3*(lam-1-T)*P02)
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1

def P2(vv):
 cc=va(vv,vs(-tau(vv),one));return tau(vm(vm(cc,cc),cc))
NS=b*N4(rows[2])+c*N4(rows[3])-E(2*lam*P02*(l+2*T+A2))
PS=b*P2(rows[2])+c*P2(rows[3])-E(P02*(l+3*T+3*A2+B3))
assert not NS.b and not PS.b

# Explicit original value traces for the two weighted singleton rows.
assert P2(rows[0])==E(P02)
v1=(T-l*zeta)/u;v0=v1+zeta;hh=E(1+v0,v1);kk=hh.conj()
M=l*(2*u-l*Q)-u*u;Dphysical=l*A2-T*T
HA=l*M*zeta*zeta-2*T*M*zeta+V2*T*T-u*u*A2
zvalue=(hh-1)*(kk-1);assert not zvalue.b
HB=u*u*(B3-2*v0*A2+zvalue.a*T)
assert b*(hh-1)+c*(kk-1)==E(T)
assert b*hh*hh+c*kk*kk==E(l+2*T+A2+HA/(u*u))
assert b*hh**3+c*kk**3==E(l+3*T+3*A2+B3+((3+2*v0)*HA-HB)/(u*u))
weightedNB=b*(N4(rows[2])-E(2*lam*P02)*hh*hh)+c*(N4(rows[3])-E(2*lam*P02)*kk*kk)
weightedPB=b*(P2(rows[2])-E(P02)*hh**3)+c*(P2(rows[3])-E(P02)*kk**3)
assert weightedNB==NS-E(2*lam*P02*HA/(u*u))
assert weightedPB==PS-E(P02*((3+2*v0)*HA-HB)/(u*u))
assert E(Dphysical+l*HA/(u*u))==E(bc)*(hh-kk)**2
assert 4*bc*(1-Q)==M

symbolic={'lam':lam,'T':T,'f':f,'ell':l,'Dphysical':Dphysical,'E1':E1.a,'EBe':EB.a,'EBo':EB.b,'N1':NH.a,'NS':NS.a,'PS':PS.a}
say(stage='new_full_general_LS_same_original_Gram',originalE0N0P1Verified=True,weightedOriginalNPThroughHAHBVerified=True,originalDistinctValueRetained=True,wholeWeightChartExcluded=False)
units=[('u',ep),('u_minus_one',ep-1),('Q',kp),('Q_minus_one',kp-1),('original_P02',P02.n),('original_bc_M',M.n),('proved_general_ell_nonzero',Lp),('proved_general_equal_weights',Lp-ep)]
out=[];cleared_polys=[];cleared_scales=[]
for name,rr,deg in [('E1',E1.a,2),('EBe',EB.a,2),('EBo',EB.b,2),('N1',NH.a,2),('weighted_N',NS.a,3),('weighted_P',PS.a,3)]:
 assert all(int(m[3])+int(m[4])+int(m[5])<=deg for m in rr.n.to_dict())
 po=rr.n;paid=oo;hist=[]
 for name0,atom in units:
  ct=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   po=po/gg;paid*=gg;ct+=1
  if ct:hist.append([name0,ct])
 assert po*paid==rr.n
 den=rr.d
 for name0,atom in units:
  while den:
   gg=den.gcd(atom)
   if gg.total_degree()==0:break
   den=den/gg
 assert den.total_degree()==0
 rec={'name':name,'poly':[[list(map(int,m)),str(a)] for m,a in po.to_dict().items()],'den':[[list(map(int,m)),str(a)] for m,a in rr.d.to_dict().items()]};out.append(rec);cleared_polys.append(po);cleared_scales.append(R(rr.d,paid))
 say({'stage':'new_full_general_LS_original_X_Gram_coordinates','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})

def determinant(matrix):
 n=len(matrix)
 if n==0:return oo
 if n==1:return matrix[0][0]
 outp=zz
 for j in range(n):
  minor=[row[:j]+row[j+1:] for row in matrix[1:]]
  outp+=(-1)**j*matrix[0][j]*determinant(minor)
 return outp

def strip_known(po,atoms):
 previous=po;paid=oo;hist=[]
 for name,atom in atoms:
  count=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   quotient=po/gg
   assert quotient*gg==po
   po=quotient;paid*=gg;count+=1
  if count:hist.append([name,count])
 assert po*paid==previous
 return po,paid,hist

def factor_profile(po):
 if not po:return dict(zero=True)
 sc,fac=po.factor();back=ctx.constant(sc);outf=[]
 for ff,mul in fac:
  back*=ff**int(mul)
  dd=ff.to_dict()
  assert all(all(mm[j]==0 for j in range(3,8)) for mm in dd)
  rec=dict(degrees=list(map(int,ff.degrees()[:3])),totalDegree=int(ff.total_degree()),terms=len(dd),multiplicity=int(mul),sha256=hashlib.sha256(str(ff).encode()).hexdigest())
  if len(dd)<=80:rec['coefficients_u_Q_ell']=[[int(mm[0]),int(mm[1]),int(mm[2]),str(cc)] for mm,cc in dd.items()]
  outf.append(rec)
 assert back==po
 return dict(content=str(sc),factors=outf,entireProductMultipliedBack=True)


from itertools import combinations
def pc(po,mon):
 ans=zz
 for mm,cc0 in po.to_dict().items():
  assert all(int(mm[j])==0 for j in range(6,8))
  if tuple(map(int,mm[3:6]))==mon:ans+=cc0*ep**int(mm[0])*kp**int(mm[1])*Lp**int(mm[2])
 return ans
headmons=[(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
heads=[[pc(po,mon) for mon in headmons] for po in cleared_polys[:4]]

# The entire T0=0 and J=Q faces are already independently excluded.
units=units+[('proved_whole_general_T0',T0.n),('proved_whole_general_J_minus_Q',(J-Q).n)]
fixed_columns=[0,2,3,4]
Hmat=[[row[j] for j in fixed_columns] for row in heads]
hd=determinant(Hmat);assert hd
assert strip_known(hd,units)[0].total_degree()==0
Hinverse=[]
for i in range(4):
 row=[]
 for j in range(4):
  minor=[[Hmat[r][c] for c in range(4) if c!=i] for r in range(4) if r!=j]
  row.append(R(((-1)**(i+j))*determinant(minor),hd))
 Hinverse.append(row)
for i in range(4):
 for j in range(4):
  assert sum((Hinverse[i][k]*R(Hmat[k][j]) for k in range(4)),R())==int(i==j)
quad=[];quad_traces=[]
for i in range(4):
 pp=sum((Hinverse[i][j]*R(cleared_polys[j]) for j in range(4)),R())
 tr=[Hinverse[i][j]*cleared_scales[j] for j in range(4)]
 assert sum((tr[j]*[E1.a,EB.a,EB.b,NH.a][j] for j in range(4)),R())==pp
 assert strip_known(pp.d,units)[0].total_degree()==0
 quad.append(pp);quad_traces.append(tr)
def rcoef(rr,mon):
 assert all(all(int(mm[j])==0 for j in range(3,8)) for mm in rr.d.to_dict())
 return R(pc(rr.n,mon),rr.d)
qcoeff=[[rcoef(rr,mm) for mm in headmons] for rr in quad]
for i in range(4):
 for j,col in enumerate(fixed_columns):
  assert qcoeff[i][col]==int(i==j)
aH,bH=-qcoeff[0][1],-qcoeff[0][5]
cH,dH=-qcoeff[1][1],-qcoeff[1][5]
eH,fH=-qcoeff[2][1],-qcoeff[2][5]
gH,hH=-qcoeff[3][1],-qcoeff[3][5]
say(stage='new_general_LS_global_four_original_quadratic_rules',
    fixedHeadColumns=fixed_columns,
    headEquations=['x^2=a*xy+b*t^2','x*t=c*xy+d*t^2',
                   'y^2=e*xy+f*t^2','y*t=g*xy+h*t^2'],
    all16InverseProductsVerified=True,
    allFourCompleteOriginalRowTracesVerified=True,
    allDenominatorsPreviouslyPaidByEntireT0AndJQTheorems=True,
    noMonomialDescentOrderAssumed=True,noSixGeneratorClaim=True)

def report_weight(name,rr):
 rr=R(rr)
 assert strip_known(rr.d,units)[0].total_degree()==0
 red,paid,hist=strip_known(rr.n,units)
 assert red*paid==rr.n
 rec=dict(name=name,fullDegrees=list(map(int,rr.n.degrees()[:3])) if rr else None,
          terms=len(rr.n.to_dict()),paidRemoved=hist,
          remaining=factor_profile(red),
          polynomialSHA256=hashlib.sha256(str(red).encode()).hexdigest(),
          individuallyPaidUnit=bool(red) and red.total_degree()==0,
          zeroPolynomial=not bool(red))
 say(stage='new_general_LS_projective_weight_constraint',**rec)
 return rec
# Projective t=0: xy cannot vanish, so precisely c=g=0 and a*e=1.
zero_t=[report_weight('t_zero_c',cH),report_weight('t_zero_g',gH),
        report_weight('t_zero_a_times_e_minus_one',aH*eH-1)]
tzero_excluded=any(r['individuallyPaidUnit'] for r in zero_t)
# On the other chart t=1 and z=xy. The complete converse uses the same z.
z=R(zp);xhat=cH*z+dH;yhat=gH*z+hH
Pz=xhat*yhat-z
Px=xhat*xhat-aH*z-bH
Py=yhat*yhat-eH*z-fH
pheads=[Pz,Px,Py]
def eval_head(coeffs,xv,yv,tv):
 return sum((coeffs[i]*xv**mm[0]*yv**mm[1]*tv**mm[2] for i,mm in enumerate(headmons)),R())
assert eval_head(qcoeff[0],xhat,yhat,R(1))==Px-aH*Pz
assert eval_head(qcoeff[1],xhat,yhat,R(1))==-cH*Pz
assert eval_head(qcoeff[2],xhat,yhat,R(1))==Py-eH*Pz
assert eval_head(qcoeff[3],xhat,yhat,R(1))==-gH*Pz
def zcoeffs(rr):
 assert all(all(int(mm[j])==0 for j in range(3,8)) for mm in rr.d.to_dict())
 out=[R() for _ in range(3)]
 for mm,cc in rr.n.to_dict().items():
  assert all(int(mm[j])==0 for j in [3,4,5,7]) and 0<=int(mm[6])<=2
  out[int(mm[6])]+=R(cc*ep**int(mm[0])*kp**int(mm[1])*Lp**int(mm[2]),rr.d)
 assert sum((out[j]*z**j for j in range(3)),R())==rr
 return out
C=[zcoeffs(pp) for pp in pheads]
for i,pp in enumerate(pheads):
 cb=json.dumps([dict(numerator=str(cf.n),denominator=str(cf.d)) for cf in C[i]],separators=(',',':')).encode()
 say(stage='new_general_LS_t_nonzero_same_z_head_equation',
     name=['Pz','Px','Py'][i],zDegree=max((j for j,cf in enumerate(C[i]) if cf),default=-1),
     coefficientBytes=len(cb),coefficientSHA256=hashlib.sha256(cb).hexdigest(),
     explicitSameZConverseProductsVerified=True,
     noGeometricLeadingCoefficientInverted=True)
def detR(mat):
 if not mat:return R(1)
 if len(mat)==1:return mat[0][0]
 return sum((((-1)**j)*mat[0][j]*detR([row[:j]+row[j+1:] for row in mat[1:]]) for j in range(len(mat))),R())
cofs=[((-1)**i)*detR([[C[j][k] for k in [1,2]] for j in range(3) if j!=i]) for i in range(3)]
delta=sum((cofs[i]*C[i][0] for i in range(3)),R())
for j in range(3):assert sum((cofs[i]*C[i][j] for i in range(3)),R())==(delta if j==0 else R())
assert sum((cofs[i]*pheads[i] for i in range(3)),R())==delta
reports=[report_weight('t_nonzero_three_quadratic_constant_cofactor',delta)]
for i,j in [(0,1),(0,2),(1,2)]:
 aa,bb=C[i],C[j]
 K0=aa[1]*bb[2]-aa[2]*bb[1]
 K1=aa[2]*bb[0]-aa[0]*bb[2]
 K2=aa[0]*bb[1]-aa[1]*bb[0]
 lin=K0*z-K1;quad0=K0*z*z-K2
 assert lin==bb[2]*pheads[i]-aa[2]*pheads[j]
 assert quad0==aa[1]*pheads[j]-bb[1]*pheads[i]
 res=K1*K1-K0*K2
 assert res==K0*quad0-(K0*z+K1)*lin
 rr=report_weight('t_nonzero_fixed_2_2_pair_'+str(i)+'_'+str(j),res)
 rr['pair']=[i,j];reports.append(rr)
finite_excluded=any(r['individuallyPaidUnit'] for r in reports)
signal.alarm(0)
say(stage='new_general_LS_complete_projective_quadratic_direction_input',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    tZeroConditions=['c=0','g=0','a*e-1=0'],
    tNonzeroExactlyThreeSameZQuadratics=True,
    bothProjectiveChartsAndAllLeadingZeroFibersRetained=True,
    tZeroAlreadyExcludedByIndividualUnit=tzero_excluded,
    tNonzeroAlreadyExcludedByIndividualUnit=finite_excluded,
    noProjectiveHeadDirectionByTheseUnitCertificates=tzero_excluded and finite_excluded,
    noMultivariateGcdOneUsedAsEmptiness=True,
    noGlobalSixGeneratorClaimWithoutFurtherProof=True,
    originalFiniteSystemExclusionClaim=False,
    oldFifteenMinorAtlasNotRerun=True,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    ordinaryISPClaim=False)
