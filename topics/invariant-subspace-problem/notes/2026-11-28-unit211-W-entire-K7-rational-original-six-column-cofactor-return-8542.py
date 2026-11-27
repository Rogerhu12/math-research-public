#!/usr/bin/env python3
"""NEW entire K7 rational weight curve: original QQ[m] six-column return.
Only necessary ORIGINAL Gram/rule prefixes are rebuilt after e=e(m),k=k(m).
No prior two-parameter determinant, Gaussian, or failed gate is replayed.
All original head inverses have already proved whole-W weight units.
QQ(m) is used ONLY to select independent original rows. Final cofactors,
paid stripping and Bezout identities are polynomial, preserving every
temporary pivot-zero fibre. A nonconstant final gcd is only a finite cover.
180 seconds / 4 GiB. Source/definitions/hash/small receipt, no data cache.
"""
import json,time,hashlib,signal,resource,contextlib,io,math,itertools
from pathlib import Path
from flint import fmpq,fmpq_poly
task_started=time.perf_counter();deadline=task_started+180
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-task_started
 print(json.dumps(r,separators=(',',':')),flush=True)
def digest_bytes(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def small_poly(p,include_small_exact=False):
 cs=[str(p[j]) for j in range(max(0,p.degree()+1))]
 raw=json.dumps(cs,separators=(',',':')).encode()
 out=dict(degree=int(p.degree()),**digest_bytes(raw))
 if include_small_exact and p.degree()<=12 and len(raw)<=2048:out['coefficientsAscending']=cs
 return out
dep=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1'
s=raw.decode()
hmark='\nM=l*(2*u-l*Q)-u*u\nunits='
bmark='\n# New mathematical input: all four original quadratics'
endmark='\ndef multiply_matrix(MM,NN):'
assert s.count(hmark)==s.count(bmark)==s.count(endmark)==1
header=s[:s.index(hmark)];body=s[s.index(bmark):s.index(endmark)]
assert len(header.encode())==6015
assert hashlib.sha256(header.encode()).hexdigest()=='be4109dc6cb4a8f788a9083b805ee2ad9e4f6f1176bb7d519727226aa4b1df4a'
assert len(body.encode())==8441
assert hashlib.sha256(body.encode()).hexdigest()=='81c1543cabd0fdb63dfee43d9cdf7d8204f806169dbac611144b82078948f627'
old="e,k,x0,x1,t,unused,zeta=map(R,ctx.gens()[:7]);u=e+1;Q=e*k;Vbar=(e+1)*k+2;l=(e+1)*((k+2)**2-2*e*k)/(k*Vbar);Delta=1-Q"
new="""mm=R(ep);pA=mm**2-6*mm+6;pB=mm**2-4*mm+6;pC=mm**3-10*mm**2+36*mm-36
e=pC/(6*pA);k=2*pA/mm
x0,x1,t,unused,zeta=map(R,[Lp,Tp,fp,tp,zp])
u=e+1;Q=e*k;Vbar=(e+1)*k+2;l=(e+1)*((k+2)**2-2*e*k)/(k*Vbar);Delta=1-Q"""
assert header.count(old)==1
header=header.replace(old,new)
ns={'__file__':str(dep),'__name__':'original_definitions_on_new_entire_K7_parameter'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(header,str(dep)+'#new_entire_K7_Gram','exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
R=ns['R'];ctx=ns['ctx'];ep=ns['ep'];oo=ns['oo'];zz=ns['zz']
m,e,k,u,Q,ell,bc,P02,T0,J,Phi,V=[ns[x] for x in ['mm','e','k','u','Q','l','bc','P02','T0','J','Phi','Vbar']]
pA,pB,pC=[ns[x] for x in ['pA','pB','pC']]
K=12*e**2*k**2-e*k**3+8*e*k**2-k**3-4*k**2-16*k-16
theta=2*(m*m-6)/m
assert not K
assert theta**2==(k+12)**2-96
assert (theta+k+12)/4==m and m*(k+12-theta)/24==1
assert pA==k*m/2 and pB==(k+4)*m/2
assert Q==pC/(3*m) and V==pB/3
C9=4*e*e*k*k-e*(k**4+9*k**3+20*k*k+16*k)+k**3+10*k*k+24*k+16
J19=(16*e**4*k**3-8*e**3*k**4-16*e**3*k**3-96*e**3*k**2
 -e**2*k**5-8*e**2*k**4+24*e**2*k**3+64*e**2*k**2+192*e**2*k
 -2*e*k**5-14*e*k**4-12*e*k**3-128*e-k**5-10*k**4-40*k**3-104*k**2-160*k-128)
D27=(16*e**5*k**4-4*e**4*k**5+32*e**4*k**4+2*e**3*k**6
 -12*e**3*k**5-96*e**3*k**4-384*e**3*k**3-384*e**3*k**2
 +3*e**2*k**6+8*e**2*k**5+60*e**2*k**4+384*e**2*k**3
 +1088*e**2*k**2+1024*e**2*k-10*e*k**5-28*e*k**4
 +48*e*k**3+64*e*k**2-512*e*k-768*e-k**6-18*k**5
 -120*k**4-440*k**3-1008*k**2-1344*k-768)
gcoeff=[[4096,9216,7680,3072,592,24,-10,-1],
 [-6144,-16128,-14336,-6048,-1416,-186,-9],
 [512,6016,6560,2528,468,50,2],
 [1792,832,-832,-392,-50,-2],
 [-256,-544,-24,24,4],[-192,0,-8],[32]]
G36=sum((sum((R(v)*k**j for j,v in enumerate(row)),R())*Q**i for i,row in enumerate(gcoeff)),R())
# m,A,B are units by the displayed COMPLETE reverse parameter identities.
# All other entries are pre-existing whole-current-W weight units.
weight_units=[
 ('entire_parameter_m',m),('entire_parameter_A',pA),('entire_parameter_B',pB),
 ('e',e),('k',k),('u',u),('Q',Q),('distinct_p_q',1-Q),
 ('W_paid_leading',V),('Phi',Phi),('P02',P02),('bc',bc),
 ('k_plus_one',k+1),('whole_equal_weights_k_plus_two',k+2),
 ('old_whole_H',4*e*k-k*k-4*k-8),('whole_u_half',2*e+1),
 ('ell',ell),('ell_minus_u',ell-u),('Q_minus_two',Q-2),('u_minus_Q',u-Q),
 ('T0',T0),('J_minus_Q',J-Q),
 ('whole_C9',C9),('whole_J19',J19),('whole_D27',D27),('whole_G36',G36)]
def strip_with(po,atoms):
 initial=po;paid=oo;hist=[]
 for name,atom in atoms:
  count=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   qq=po/gg;assert qq*gg==po
   po=qq;paid*=gg;count+=1
  if count:hist.append([name,count])
 assert po*paid==initial
 return po,paid,hist
basic=[('m',m.n),('A',pA.n),('B',pB.n)]
units=[]
for name,v in weight_units:
 assert all(all(mm[j]==0 for j in range(1,8)) for po in [v.n,v.d] for mm in po.to_dict())
 if not v:
  say(stage='entire_K7_inside_previously_excluded_weight_fibre',unit=name,
      originalRationalIdentityZeroVerified=True,wholeCurrentK7Excluded=True)
  sys_exit=__import__('sys').exit;sys_exit(0)
 # Every rational substitution denominator is supported by m,A,B.
 assert strip_with(v.d,basic)[0].total_degree()==0
 if v.n.total_degree()>0:units.append((name,v.n))
 if v.d.total_degree()>0:units.append((name+'_paid_denominator',v.d))
def strip(po):return strip_with(po,units)
def pay(po):
 assert po and strip(po)[0].total_degree()==0
 return True
cleared_polys=[];cleared_scales=[]
original=[ns['symbolic'][name] for name in ['E1','EBe','EBo','N1','NS','PS']]
for name,rr in zip(['E1','EBe','EBo','N1','NS','PS'],original):
 pay(rr.d)
 po,removed,hist=strip(rr.n);assert po*removed==rr.n
 scale=R(rr.d,removed);assert R(po)==scale*rr
 cleared_polys.append(po);cleared_scales.append(scale)
 say(stage='new_entire_K7_original_Gram_row',name=name,
     mDegree=int(po.degrees()[0]),terms=len(po.to_dict()),
     originalScaleMultipliedBack=True,allDenominatorsPaid=True)
ns.update(units=units,cleared_polys=cleared_polys,cleared_scales=cleared_scales,C9_weight=C9)
def replace_once(a,b):
 global body
 assert body.count(a)==1
 body=body.replace(a,b)
replace_once("Hpaid=4*ep*kp-kp*kp-4*kp-8\nbase_units=units+[('previous_whole_k_minus_one',kp+1),('previous_complete_H_zero',Hpaid)]",
             "Hpaid=(4*e*k-k*k-4*k-8).n\nbase_units=units[:]")
replace_once("d2unpaid,d2paid,d2hist=strip_known(delta2,base_units)",
             "d2unpaid,d2paid,d2hist=strip_known(delta2,base_units)\nassert d2unpaid.total_degree()==0")
replace_once("C9=4*ep*ep*kp*kp-ep*(kp**4+9*kp**3+20*kp*kp+16*kp)+kp**3+10*kp*kp+24*kp+16",
             "C9=C9_weight.n")
replace_once("assert d3unpaid==fmpq(-1,2)*C9","assert d3unpaid.total_degree()==0")
prefix_stages=[]
def prefix_say(x=None,**kw):
 r=kw if x is None else x
 prefix_stages.append(r['stage'])
ns['say']=prefix_say
exec(compile(body,str(dep)+'#new_entire_K7_original_rules','exec'),ns)
assert ns['d2unpaid'].total_degree()==ns['d3unpaid'].total_degree()==0
basis,variables,matrices,errors=[ns[v] for v in ['basis','variables','matrices','errors']]
verify_trace=ns['verify_trace'];reduce_six=ns['reduce_six']
full_units=ns['full_chart_units']
# No hidden kp or any geometric variable may occur in a scalar coefficient.
def upoly(po):
 dd=po.to_dict();deg=max((int(mm[0]) for mm in dd),default=-1)
 out=[fmpq(0) for _ in range(deg+1)]
 for mm,cc in dd.items():
  assert not any(mm[j] for j in range(1,8))
  out[int(mm[0])]+=cc
 return fmpq_poly(out)
def native(p):
 return sum((ep**j*p[j] for j in range(max(0,p.degree()+1))),zz)
paid_u=[(name,upoly(p)) for name,p in units]
UZ=fmpq_poly();UO=fmpq_poly([1])
def udiv(a,b):
 assert b
 q,r=divmod(a,b);assert not r and q*b==a
 return q
def ustrip(p):
 initial=p;removed=UO;hist=[]
 for name,atom in paid_u:
  count=0
  while p:
   gg=p.gcd(atom)
   if gg.degree()<=0:break
   p=udiv(p,gg);removed*=gg;count+=1
  if count:hist.append([name,count])
 assert p*removed==initial
 if p:
  c=p[p.degree()];p=p/c;removed=removed*c
 assert p*removed==initial
 return p,removed,hist
def bezout(a,b):
 r0,r1=a,b;s0,s1=UO,UZ;t0,t1=UZ,UO
 while r1:
  qq,rr=divmod(r0,r1);assert qq*r1+rr==r0
  r0,r1=r1,rr;s0,s1=s1,s0-qq*s1;t0,t1=t1,t0-qq*t1
 if r0:
  lc=r0[r0.degree()];r0=r0/lc;s0=s0/lc;t0=t0/lc
 assert s0*a+t0*b==r0
 return r0,s0,t0
class U:
 def __init__(self,n=0,d=None):
  if isinstance(n,U):self.n=n.n;self.d=n.d;return
  if not isinstance(n,fmpq_poly):n=fmpq_poly([n])
  if d is None:d=UO
  if not isinstance(d,fmpq_poly):d=fmpq_poly([d])
  assert d
  if not n:self.n=UZ;self.d=UO;return
  g=n.gcd(d);n=udiv(n,g);d=udiv(d,g)
  lc=d[d.degree()];self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,v):
  v=U(v);return U(self.n*v.d+v.n*self.d,self.d*v.d)
 __radd__=__add__
 def __neg__(self):return U(-self.n,self.d)
 def __sub__(self,v):return self+-U(v)
 def __rsub__(self,v):return U(v)+-self
 def __mul__(self,v):
  v=U(v);return U(self.n*v.n,self.d*v.d)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=U(v);assert v;return U(self.n*v.d,self.d*v.n)
 def __eq__(self,v):
  v=U(v);return self.n*v.d==v.n*self.d
def nr(v):
 v=U(v);return R(native(v.n),native(v.d))
say(stage='new_entire_K7_global_original_six_rules_and_18_products',
    originalDefinitionPrefixBytes=6015,originalRulePrefixBytes=8441,
    actualHeadNumeratorsAndDenominatorsPaid=True,
    fullOriginalTraceProductsVerified=True,wholeK7RationalCoverVerified=True,
    temporaryFieldPivotsWillNotBeAssumedUnits=True,
    basis=['1','x','y','t','y^2','y*t'],claimExcluded=False)

poly_rows=[];poly_tags=[];labels=[];rr_basis=[];chosen=[]
def add_original_row(row,tag,label):
 if not any(row):return False
 verify_trace(sum((row[j]*basis[j] for j in range(6)),R()),tag)
 den=oo
 for cf in row:
  pay(cf.d);den*=cf.d/den.gcd(cf.d)
 pay(den)
 pols=[cf.n*(den/cf.d) for cf in row];removed=oo
 for name,atom in units:
  while any(pols):
   gg=atom
   for pol in pols:gg=gg.gcd(pol)
   if gg.total_degree()==0:break
   nxt=[pol/gg for pol in pols]
   assert all(nxt[i]*gg==pols[i] for i in range(6))
   pols=nxt;removed*=gg
 pay(removed)
 ups=[upoly(p) for p in pols]
 first=next(p for p in ups if p);c=first[first.degree()]
 ups=[p/c for p in ups];scale=R(den,removed)/c
 trace=[scale*v for v in tag]
 for p,cf in zip(ups,row):assert R(native(p))==scale*cf
 verify_trace(sum((R(native(ups[j]))*basis[j] for j in range(6)),R()),trace)
 idx=len(poly_rows);poly_rows.append(ups);poly_tags.append(trace);labels.append(label)
 rr=[U(p) for p in ups]
 for col,br in rr_basis:
  fac=rr[col]
  if fac:rr=[rr[j]-fac*br[j] for j in range(6)]
 pivot=next((j for j,v in enumerate(rr) if v),None)
 if pivot is not None:
  p=rr[pivot];rr=[v/p for v in rr];assert rr[pivot]==1
  rr_basis.append((pivot,rr));chosen.append(idx)
 say(stage='new_entire_K7_polynomial_original_six_column_row',
     index=idx,label=label,degree=max(p.degree() for p in ups),
     genericRowRank=len(chosen),fullOriginalTraceAndPaidProductsVerified=True,
     genericSelectionPivotsNotInvertedGeometrically=True,claimExcluded=False)
 return True
native_indices=[]
for row,tag,label in zip(ns['necessary'],ns['necessary_tags'],ns['necessary_labels']):
 idx=len(poly_rows)
 if add_original_row(row,tag,label):native_indices.append(idx)
for idx in [1,3]:
 row,tag=reduce_six(ns['overlaps'][idx],ns['overlap_tags'][idx])
 add_original_row(row,tag,'unused_original_overlap_'+str(idx))
def multiply_original_row(idx,axis):
 row=poly_rows[idx];tag=poly_tags[idx]
 rawrow=[sum((R(native(row[i]))*matrices[axis][i][j] for i in range(6)),R()) for j in range(6)]
 rawtag=[variables[axis]*tag[g]-sum((R(native(row[i]))*errors[axis][i][g] for i in range(6)),R()) for g in range(6)]
 return rawrow,rawtag
# These four rows are the fixed native NS/PS products, but on the NEW m curve.
for idx in native_indices:
 for axis in [1,2]:
  row,tag=multiply_original_row(idx,axis)
  add_original_row(row,tag,labels[idx]+'*'+'xyt'[axis])
# The same-point commutators are legitimate necessary ORIGINAL rows even
# when the six generating monomials are dependent. No matrix freeness.
for ax,bx in [(0,1),(0,2),(1,2)]:
 MA,MB=matrices[ax],matrices[bx]
 for i in range(6):
  row=[sum((MA[i][h]*MB[h][j]-MB[i][h]*MA[h][j] for h in range(6)),R()) for j in range(6)]
  if not any(row):continue
  tag=[variables[ax]*errors[bx][i][g]-variables[bx]*errors[ax][i][g]
    +sum((MB[i][h]*errors[ax][h][g]-MA[i][h]*errors[bx][h][g] for h in range(6)),R())
    for g in range(6)]
  add_original_row(row,tag,'comm_%d_%d_%d'%(ax,bx,i))
# If necessary, use a genuinely enlarged original module by multiplying
# each first-batch row by x,y,t, once. All new traces are multiplied back.
if len(chosen)<6:
 initial_count=len(poly_rows)
 for idx in range(initial_count):
  for axis in range(3):
   row,tag=multiply_original_row(idx,axis)
   add_original_row(row,tag,labels[idx]+'*'+'xyt'[axis])
  if len(chosen)==6:break
if len(chosen)<6:
 say(stage='new_entire_K7_original_six_column_rank_unresolved',
     rank=len(chosen),rows=len(poly_rows),noUnitOrFiniteCoverClaimed=True)
 raise SystemExit(2)
chosen=chosen[:6];B=[poly_rows[i][:] for i in chosen]
det_divisions=0
def det(A):
 global det_divisions
 n=len(A)
 if n==0:return UO
 if n==1:return A[0][0]
 A=[r[:] for r in A];prev=UO;sgn=1
 for col in range(n-1):
  sw=next((i for i in range(col,n) if A[i][col]),None)
  if sw is None:return UZ
  if sw!=col:A[col],A[sw]=A[sw],A[col];sgn=-sgn
  p=A[col][col]
  for i in range(col+1,n):
   for j in range(col+1,n):
    num=p*A[i][j]-A[i][col]*A[col][j]
    A[i][j]=udiv(num,prev);det_divisions+=1
   A[i][col]=UZ
  prev=p
 return sgn*A[-1][-1]
D=det(B);assert D
Adj=[]
for i in range(6):
 row=[]
 for j in range(6):
  minor=[[B[r][c] for c in range(6) if c!=i] for r in range(6) if r!=j]
  row.append((-1)**(i+j)*det(minor))
 Adj.append(row)
for i in range(6):
 for j in range(6):
  assert sum((B[i][h]*Adj[h][j] for h in range(6)),UZ)==D*int(i==j)
  assert sum((Adj[i][h]*B[h][j] for h in range(6)),UZ)==D*int(i==j)
nrows=len(poly_rows)
def scalar_cofactor_vector(indices,expected):
 C=[poly_rows[i] for i in indices]
 assert det(C)==expected
 c=[(-1)**i*det([[C[r][j] for j in range(1,6)] for r in range(6) if r!=i]) for i in range(6)]
 for j in range(6):
  assert sum((c[i]*C[i][j] for i in range(6)),UZ)==expected*int(j==0)
 out=[U() for _ in range(nrows)]
 for i,idx in enumerate(indices):out[idx]=out[idx]+U(c[i])
 return out
g,rem,hist=ustrip(D)
coef=[c/U(rem) for c in scalar_cofactor_vector(chosen,D)]
assert all(sum((coef[i]*U(poly_rows[i][j]) for i in range(nrows)),U())==U(g*int(j==0)) for j in range(6))
events=[dict(source='selected_six',degree=int(g.degree()),paidRemoved=hist)]
say(stage='new_entire_K7_first_polynomial_constant_cofactor',
    selectedOriginalRows=chosen,rawDeterminant=small_poly(D),
    paidResidual=small_poly(g),all72AdjugateAndSixColumnProductsVerified=True,
    temporaryPivotZeroFibresPreserved=True,claimExcluded=False)
for idx,row in enumerate(poly_rows):
 if g.degree()==0:break
 if idx in chosen:continue
 ratios=[sum((row[i]*Adj[i][j] for i in range(6)),UZ) for j in range(6)]
 for j,C in enumerate(ratios):
  if g.degree()==0:break
  if not C:continue
  c,paid,ph=ustrip(C)
  gg,aa,bb=bezout(g,c)
  if gg.degree()==g.degree():continue
  indices=chosen[:];indices[j]=idx
  newcoef=[v/U(paid) for v in scalar_cofactor_vector(indices,C)]
  coef=[U(aa)*coef[i]+U(bb)*newcoef[i] for i in range(nrows)]
  g=gg
  for col in range(6):
   assert sum((coef[i]*U(poly_rows[i][col]) for i in range(nrows)),U())==U(g*int(col==0))
  events.append(dict(row=idx,replacedPosition=j,degree=int(g.degree()),paidRemoved=ph))
  say(stage='new_entire_K7_polynomial_cofactor_Bezout_drop',
      row=idx,replacedPosition=j,gcd=small_poly(g),
      fullReplacementDeterminantAndSixConstantProductsVerified=True,
      fullUnivariateBezoutAndUpdatedOriginalRowProductsVerified=True,
      allTemporaryPivotZeroFibresPreserved=True,claimExcluded=False)
# A true original ideal trace is formed and multiplied back, not inferred
# from generic rank or from the six monomials being independent.
for v in coef:pay(native(v.d))
final_tags=[sum((nr(coef[i])*poly_tags[i][j] for i in range(nrows)),R()) for j in range(6)]
for t in final_tags:pay(t.d)
verify_trace(R(native(g)),final_tags)
for j in range(6):
 assert sum((coef[i]*U(poly_rows[i][j]) for i in range(nrows)),U())==U(g*int(j==0))
tag_bytes=json.dumps([dict(n=[[[int(a) for a in mm],str(c)] for mm,c in sorted(v.n.to_dict().items())],
                          d=[[[int(a) for a in mm],str(c)] for mm,c in sorted(v.d.to_dict().items())])
                     for v in final_tags],separators=(',',':')).encode()
fac_data=[]
if 0<g.degree()<=12:
 scalar,factors=g.factor();product=fmpq_poly([scalar])
 for ff,mul in factors:
  product*=ff**int(mul)
  fac_data.append(dict(multiplicity=int(mul),**small_poly(ff,True)))
 assert product==g
say(stage='new_entire_K7_original_polynomial_constant_return_complete',
    originalRows=nrows,selectedRows=chosen,cofactorGcdEvents=events,
    exactBareissDivisionProducts=det_divisions,cover=small_poly(g,True),
    wholeCoverFactorization=fac_data,wholeCoverFactored=(g.degree()<=12),
    completeOriginalSixTermTraceVerified=True,
    originalTraceDefinitionOnly=digest_bytes(tag_bytes),
    allTraceDenominatorsPreviouslyPaid=True,
    everyTemporaryFieldPivotZeroFibrePreserved=True,
    wholeCurrentK7Excluded=g.degree()==0,
    finiteParameterCoverOnly=g.degree()>0,noCoefficientCacheWritten=True)
