#!/usr/bin/env python3
"""New full u=1/2 and u=2/3 original J=Q lines.
Use the original 48x35 Gram Macaulay system and physical D as a true unit.
Every target identity is checked on all 35 polynomial columns after common
cancellation. Parameter denominators are retained, including every pivot zero.
180 seconds / 1 GiB. No old QQ projection or cofactor gate is repeated.
"""
import json,time,hashlib,resource,signal
from pathlib import Path
from fractions import Fraction
from flint import fmpq,fmpq_mpoly_ctx,fmpq_poly
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(x=None,**kw):
 if x is None:x=kw
 x['seconds']=time.perf_counter()-start
 print(json.dumps(x),flush=True)
def run_line(uvalue):
 ctx=fmpq_mpoly_ctx.get(('Q','unused_Q','x','y','t','dummy_t','zeta','dummy'),'lex');ep,kp,Lp,Tp,fp,tp,zp,dp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
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
 m,qp,x0,x1,t,unused,zeta=map(R,ctx.gens()[:7]);u=R(uvalue);Q=m;l=1-2*u*(1-u)/Q;Delta=1-Q
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
 
 assert J==Q and not Pf
 assert T0==4*u*(1-u)-Q
 assert Phi==-4*(u-1)**2
 H=2*u+Q-2
 symbolic={'lam':lam,'T':T,'f':f,'ell':l,'Dphysical':Dphysical,'E1':E1.a,'EBe':EB.a,'EBo':EB.b,'N1':NH.a,'NS':NS.a,'PS':PS.a}
 units=[('Q',Q.n),('Q_minus_one',(Q-1).n),('original_P02',P02.n),
        ('original_bc_M',M.n),('whole_general_ell',l.n),
        ('whole_general_equal_weights',(l-u).n),
        ('whole_general_T0',T0.n),('whole_JQ_H_zero',H.n)]
 assert all(atom for _,atom in units)
 say(stage='new_JQ_two_rational_u_lines_same_original_Gram',
     u=str(uvalue),originalE0N0P1Verified=True,
     weightedOriginalNPThroughHAHBVerified=True,
     allPreviouslyPaidWholeZeroBranchesRetained=True,
     physicalDOriginalUnitRetained=True,claimExcluded=False)
 out=[];cleared_polys=[];cleared_scales=[]
 for name,rr,deg in [('E1',E1.a,2),('EBe',EB.a,2),('EBo',EB.b,2),('N1',NH.a,2),('weighted_N',NS.a,3),('weighted_P',PS.a,3)]:
  assert all(int(m[2])+int(m[3])+int(m[4])<=deg for m in rr.n.to_dict())
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
  say({'stage':'new_JQ_rational_u_line_original_X_Gram_coordinates','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})
 # New entire rational-u line; original degree-four Macaulay input.
 # No quadratic head or cubic minor is inverted.
 from fractions import Fraction
 from flint import fmpq_poly
 def mons_upto(d):
  return [(i,j,k) for n in range(d+1) for i in range(n,-1,-1) for j in range(n-i,-1,-1) for k in [n-i-j]]
 allmons=mons_upto(4);assert len(allmons)==35
 allmons=allmons[1:]+allmons[:1]
 posmon={mm:i for i,mm in enumerate(allmons)}
 def mxyz(mm):return Lp**mm[0]*Tp**mm[1]*fp**mm[2]
 def coefdict(po):
  out={}
  for mm,cc in po.to_dict().items():
   assert mm[1]==mm[5]==mm[6]==mm[7]==0
   key=tuple(map(int,mm[2:5]))
   out[key]=out.get(key,zz)+cc*ep**int(mm[0])
  return out
 matrix=[];labels=[]
 for gi,po in enumerate(cleared_polys):
  cmap=coefdict(po)
  for multiplier in mons_upto(2 if gi<4 else 1):
   row=[zz for _ in range(35)]
   for mm,cf in cmap.items():
    target=tuple(mm[j]+multiplier[j] for j in range(3));row[posmon[target]]+=cf
   ret=sum((row[j]*mxyz(allmons[j]) for j in range(35)),zz)
   assert ret==mxyz(multiplier)*po
   assert R(ret)==R(mxyz(multiplier))*cleared_scales[gi]*symbolic[['E1','EBe','EBo','N1','NS','PS'][gi]]
   matrix.append(row);labels.append([gi,list(multiplier)])
 assert len(matrix)==48
 inputhash=hashlib.sha256('|'.join(str(po) for row in matrix for po in row).encode()).hexdigest()
 say(stage='new_JQ_rational_u_line_original_Macaulay4',rows=48,columns=35,
     originalSixRows=6,all48OriginalMonomialProductsMultipliedBack=True,constantColumn=34,inputSHA256=inputhash,
     G2Inverted=False,cubicMinorInverted=False,claimExcluded=False)
 
 
 def evalmod(po,qv,p):
  ans=0
  for mm,cc in po.to_dict().items():
   assert all(mm[j]==0 for j in range(1,8))
   cf=Fraction(str(cc));assert cf.denominator%p
   ans=(ans+cf.numerator%p*pow(cf.denominator%p,-1,p)*pow(qv,int(mm[0]),p))%p
  return ans
 def select(order,qv,prime=1009):
  aa=[[evalmod(pp,qv,prime) for pp in matrix[i]] for i in order]
  inds=order[:];columns=[];rank=0
  for col in range(35):
   choices=[i for i in range(rank,len(aa)) if aa[i][col]]
   if not choices:continue
   j=choices[0];aa[rank],aa[j]=aa[j],aa[rank];inds[rank],inds[j]=inds[j],inds[rank]
   inv=pow(aa[rank][col],-1,prime);aa[rank]=[v*inv%prime for v in aa[rank]]
   for i in range(rank+1,len(aa)):
    v=aa[i][col]
    if v:aa[i]=[(a-v*b)%prime for a,b in zip(aa[i],aa[rank])]
   columns.append(col);rank+=1
   if rank==35:break
  return inds[:rank],columns
 def paid_strip(po):
  old=po;paid=oo;history=[]
  for name,atom in units:
   count=0
   while po:
    gg=po.gcd(atom)
    if gg.total_degree()==0:break
    quotient=po/gg;assert quotient*gg==po
    po=quotient;paid*=gg;count+=1
   if count:history.append([name,count])
  assert po*paid==old
  return po,paid,history
 def univariate(po):
  degree=int(po.degrees()[0]) if po else -1
  cs=[fmpq(0) for _ in range(max(0,degree+1))]
  for mm,cc in po.to_dict().items():
   assert all(mm[j]==0 for j in range(1,8))
   cs[int(mm[0])]+=cc
  return fmpq_poly(cs)
 def target_row(po):
  cm=coefdict(po);out=[zz for _ in range(35)]
  for mm,cf in cm.items():
   assert mm in posmon;out[posmon[mm]]+=cf
  assert sum((out[j]*mxyz(allmons[j]) for j in range(35)),zz)==po
  return out
 assert paid_strip(Dphysical.d)[0].total_degree()==0
 target_data=[('one',oo,target_row(oo)),
              ('original_physical_D_numerator',Dphysical.n,target_row(Dphysical.n))]
 def solve_selected(indices,columns):
  rank=len(indices);assert rank==len(columns)>0
  # A is the selected coefficient map from original rows to selected columns.
  aa=[[matrix[indices[j]][columns[i]] for j in range(rank)]
      +[row[columns[i]] for _,_,row in target_data] for i in range(rank)]
  previous=oo;checks=0
  for j in range(rank-1):
   if not aa[j][j]:
    options=[i for i in range(j+1,rank) if aa[i][j]]
    assert options
    sw=options[0];aa[j],aa[sw]=aa[sw],aa[j]
   pivot=aa[j][j]
   for i in range(j+1,rank):
    for k in range(j+1,rank+len(target_data)):
     numerator=aa[i][k]*pivot-aa[i][j]*aa[j][k]
     quotient=numerator/previous;assert quotient*previous==numerator
     aa[i][k]=quotient;checks+=1
    aa[i][j]=zz
   previous=pivot
  answers=[]
  for ti,(name,target,tarow) in enumerate(target_data):
   coefs=[R() for _ in range(rank)]
   for i in range(rank-1,-1,-1):
    coefs[i]=(R(aa[i][rank+ti])-sum((R(aa[i][j])*coefs[j] for j in range(i+1,rank)),R()))/R(aa[i][i])
   matches=[sum((coefs[i]*R(matrix[indices[i]][j]) for i in range(rank)),R())==R(tarow[j]) for j in range(35)]
   if not all(matches):
    say(stage='new_JQ_rational_line_target_not_in_selected_original_span',
        u=str(uvalue),target=name,rank=rank,
        failedOriginalColumnCount=sum(not q for q in matches),
        noExclusionClaim=True)
    continue
   denominator=oo
   for cf in coefs:denominator=denominator*(cf.d/denominator.gcd(cf.d))
   numerators=[cf.n*(denominator/cf.d) for cf in coefs]
   assert all(sum((numerators[i]*matrix[indices[i]][j] for i in range(rank)),zz)==denominator*tarow[j] for j in range(35))
   common=denominator
   for pp in numerators:common=common.gcd(pp)
   den0=denominator/common;nums=[pp/common for pp in numerators]
   assert den0*common==denominator
   assert all(nums[i]*common==numerators[i] for i in range(rank))
   assert all(sum((nums[i]*matrix[indices[i]][j] for i in range(rank)),zz)==den0*tarow[j] for j in range(35))
   remaining,paid,hist=paid_strip(den0)
   assert remaining*paid==den0
   cp=univariate(remaining);assert cp
   cb=json.dumps(dict(u=str(uvalue),rows=indices,columns=columns,target=name,
        denominator=str(den0),coefficients=[str(z) for z in nums]),
        separators=(',',':')).encode()
   say(stage='new_JQ_rational_line_complete_original_target_identity',
       u=str(uvalue),target=name,selectedOriginalRows=indices,
       selectedColumns=columns,selectedRank=rank,
       exactBareissDivisionProducts=checks,
       all35OriginalPolynomialColumnsMultipliedBack=True,
       commonCancellationRecheckedInFreePolynomialColumns=True,
       onlyPreviouslyPaidParameterFactorsRemoved=True,paidRemoved=hist,
       fullDenominatorDegree=int(den0.degrees()[0]),
       remainingNecessaryQDegree=int(cp.degree()),
       remainingNecessaryQCoefficients=[str(v) for v in cp.coeffs()] if len(str(cp))<8192 else None,
       certificateBytes=len(cb),certificateSHA256=hashlib.sha256(cb).hexdigest(),
       allIntermediatePivotZeroFibersRetainedByFinalDenominator=True,
       claimExcluded=cp.degree()==0)
   answers.append(cp)
  return answers
 gcd_all=None;records=[];closed=False
 for rotation in [0,7,17,29]:
  order=list(range(rotation,48))+list(range(rotation))
  options=[(select(order,qv),qv) for qv in [7,11,13]]
  (indices,columns),sample=max(options,key=lambda pair:len(pair[0][0]))
  say(stage='new_JQ_rational_line_selector_only',
      u=str(uvalue),rotation=rotation,p=1009,Q=sample,
      rank=len(indices),numericSamplesOnlyChooseAnExactOriginalSubmatrix=True,
      claimExcluded=False)
  answers=solve_selected(indices,columns)
  for cp in answers:
   if gcd_all is None:gcd_all=cp/cp[cp.degree()]
   else:
    gg,aa,bb=gcd_all.xgcd(cp)
    assert aa*gcd_all+bb*cp==gg
    gcd_all=gg
   records.append(dict(rotation=rotation,remainingQDegree=int(cp.degree()),
                       runningQQGCDDegree=int(gcd_all.degree())))
   say(stage='new_JQ_rational_line_original_QQ_Bezout_step',
       u=str(uvalue),**records[-1],actualCombinationProductVerified=True,
       claimExcluded=gcd_all.degree()==0)
   if gcd_all.degree()==0:closed=True;break
  if closed:break
 factors=[];sf=None
 if gcd_all and gcd_all.degree()>0:
  repeated=gcd_all.gcd(gcd_all.derivative())
  sf,sfr=divmod(gcd_all,repeated);assert not sfr and sf*repeated==gcd_all
  cc,fac=sf.factor();back=fmpq_poly([cc])
  for ff,mult in fac:
   back*=ff**int(mult)
   ffbytes=json.dumps([str(v) for v in ff.coeffs()],separators=(',',':')).encode()
   factors.append(dict(degree=int(ff.degree()),multiplicity=int(mult),
      coefficients=[str(v) for v in ff.coeffs()] if len(ffbytes)<=8192 else None,
      coefficientBytes=len(ffbytes),coefficientSHA256=hashlib.sha256(ffbytes).hexdigest()))
  assert back==sf
 rec=dict(u=str(uvalue),wholeRationalULineExcluded=closed,
     originalMacaulayDimensions=[48,35],
     originalPhysicalDUnitAndAllZeroFibersRetained=True,
     necessaryQQQDegree=int(gcd_all.degree()) if gcd_all else None,
     necessaryQQQCoefficients=[str(v) for v in gcd_all.coeffs()] if gcd_all and len(str(gcd_all))<=8192 else None,
     squareFreeQDegree=int(sf.degree()) if sf else None,
     completeQQFactors=factors,
     noModularEmptinessClaim=True,
     originalIdentityCount=len(records))
 say(stage='new_JQ_rational_u_line_original_return_complete',**rec)
 return rec
 
returns=[]
for uvalue in [fmpq(1,2),fmpq(2,3)]:
 returns.append(run_line(uvalue))
signal.alarm(0)
say(stage='new_JQ_two_rational_u_lines_complete_original_gate',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    returns=returns,bothWholeLinesExcluded=all(r['wholeRationalULineExcluded'] for r in returns),
    onlyRemainingJQWeightsAreTheseTwoULinesByPublishedStrictGauss=True,
    wholeGeneralJQBoundaryExcluded=all(r['wholeRationalULineExcluded'] for r in returns),
    oldQQProjectionsNotRerun=True,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    ordinaryISPClaim=False)
