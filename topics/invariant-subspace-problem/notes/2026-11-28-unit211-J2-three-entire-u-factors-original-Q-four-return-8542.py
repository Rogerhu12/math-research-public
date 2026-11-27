#!/usr/bin/env python3
"""NEW entire J2 constant fibers: original monic O(Q), all same-lambda
rows, and original physical Delta powers. Read saved exact pairs and the
complete three-factor u cover. No earlier QQ projection/norm gate replay.
Every finite algebra retains both lambda embeddings and every u root.
180 seconds /4 GiB. A modular deficit never proves a QQ deficit."""
import json,time,signal,resource,hashlib,math
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat,nmod_mat
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw),flush=True)
filename="2026-11-28-unit211-J2-original-pairs-and-three-u-factors-exact-input-8542.json"
raw=Path(__file__).with_name(filename).read_bytes()
assert hashlib.sha256(raw).hexdigest()=="e1b9c53c299df8c6725067444c7c6838c1b1573157bc8271c7037234bd112e0f"
data=json.loads(raw)
assert data["producerSourceSHA256"]=="ef759c56aac43b8b6513c39fc31c6daf87fda63491c68a9b453e0c879a7b2524"
assert data["lambdaRelationAscending"]==["1/3","-2/3","1"]
rawpairs={}
for label,obj in data["pairs"].items():
 nums=[fmpq(c) for p in obj.values() for e,c in p["terms"]]
 den=math.lcm(*(int(c.denominator) for c in nums))
 ints=[int(c*den) for c in nums]
 content=math.gcd(*ints);scale=fmpq(den,content)
 pp={}
 for ab,poly in obj.items():
  pp[ab]=[(tuple(map(int,e)),fmpq(c)*scale) for e,c in poly["terms"]]
  assert all(c/scale==fmpq(old) for (e,c),(eo,old) in zip(pp[ab],poly["terms"]))
 rawpairs[label]=pp
 say("new_exact_J2_saved_original_pair_rational_normalization",original=label,
     nonzeroRationalScale=str(scale),allCoefficientProductsReturned=True)
results=[]
for factorRecord in data["uFactors"]:
 coefficients={}
 for (i,j),c in factorRecord["terms"]:
  assert j==0;coefficients[int(i)]=fmpq(c)
 n=max(coefficients);F0=fmpq_poly([coefficients.get(i,0) for i in range(n+1)])
 F=F0*(1/F0[n]);assert F*F0[n]==F0 and F[n]==1
 q0=fmpq_poly([]);q1=fmpq_poly([1]);uv=fmpq_poly([0,1])
 divchecks=0;inversechecks=0
 def red(a):
  global divchecks
  q,r=divmod(a,F);assert q*F+r==a;divchecks+=1
  return r
 def K(a=0,b=0):
  if not isinstance(a,fmpq_poly):a=fmpq_poly([a])
  if not isinstance(b,fmpq_poly):b=fmpq_poly([b])
  return (red(a),red(b))
 kz=(q0,q0);ko=(q1,q0)
 def ka(x,y):return (x[0]+y[0],x[1]+y[1])
 def kn(x):return (-x[0],-x[1])
 def ks(x,y):return ka(x,kn(y))
 def km(x,y):
  a,b=x;c,d=y
  return K(a*c-fmpq(1,3)*b*d,a*d+b*c+fmpq(2,3)*b*d)
 def kr(x,c):return (x[0]*c,x[1]*c)
 def iszero(x):return not x[0] and not x[1]
 def ki(x,label):
  global inversechecks
  a,b=x;norm=red(a*a+fmpq(2,3)*a*b+fmpq(1,3)*b*b)
  g,s,t=norm.xgcd(F);assert s*norm+t*F==g
  if g.degree()!=0:
   say("new_J2_retained_nonunit_constant_fiber",uDegree=n,name=label,
       normGcdAscending=[str(g[i]) for i in range(g.degree()+1)],
       entireUAndBothLambdaFibersRetained=True)
   return None
  iv=red(s*(1/g[0]))
  out=K((a+fmpq(2,3)*b)*iv,-b*iv)
  assert km(out,x)==ko;inversechecks+=1
  return out
 def trim(p):
  p=list(p)
  while p and iszero(p[-1]):p.pop()
  return p
 def pa(p,q):
  out=[kz]*max(len(p),len(q))
  for i,c in enumerate(p):out[i]=ka(out[i],c)
  for i,c in enumerate(q):out[i]=ka(out[i],c)
  return trim(out)
 def pn(p):return [kn(c) for c in p]
 def pm(p,q):
  if not p or not q:return []
  out=[kz]*(len(p)+len(q)-1)
  for i,a in enumerate(p):
   for j,b in enumerate(q):out[i+j]=ka(out[i+j],km(a,b))
  return trim(out)
 def readpair(obj):
  degree=max(e[1] for ab in obj.values() for e,c in ab)
  out=[]
  for j in range(degree+1):
   pair=[]
   for ab in ("a","b"):
    v=fmpq_poly([])
    for (i,k),c in obj[ab]:
     if k==j:
      cc=[fmpq(0)]*(i+1);cc[i]=c;v+=fmpq_poly(cc)
    pair.append(red(v))
   out.append(tuple(pair))
  return trim(out)
 original={label:readpair(p) for label,p in rawpairs.items()}
 assert len(original["O"])==5
 head=original["O"][-1]
 invhead=ki(head,"actual complete original O Q-four leading coefficient")
 if invhead is None:
  results.append(dict(uDegree=n,excluded=False,reason="entire leading nonunit fibers retained"))
  continue
 rule=[km(c,invhead) for c in original["O"]]
 assert rule[-1]==ko and [km(c,head) for c in rule]==original["O"]
 def reduceQ(p):
  originalp=trim(p);p=list(originalp);quo=[kz]*max(0,len(p)-4)
  while len(p)>=5:
   j=len(p)-5;c=p[-1];quo[j]=ka(quo[j],c)
   for i in range(5):p[j+i]=ks(p[j+i],km(c,rule[i]))
   p=trim(p)
  assert pa(pm(trim(quo),rule),p)==originalp
  return tuple(p+[kz]*(4-len(p)))
 zero=(kz,)*4
 one=(ko,kz,kz,kz)
 def ea(x,y):return tuple(ka(a,b) for a,b in zip(x,y))
 def en(x):return tuple(kn(a) for a in x)
 def es(x,y):return ea(x,en(y))
 def em(x,y):return reduceQ(pm(list(x),list(y)))
 def er(x,c):return tuple(kr(a,c) for a in x)
 def ec(x):return (x,kz,kz,kz)
 def eu(x):return tuple((red(a*uv),red(b*uv)) for a,b in x)
 def el(x):return tuple((-fmpq(1,3)*b,a+fmpq(2,3)*b) for a,b in x)
 def eq(x):return reduceQ([kz]+list(x))
 def flat(x):
  return [c[i] for pair in x for c in pair for i in range(n)]
 dimension=8*n
 assert flat(one)==[fmpq(1)]+[fmpq(0)]*(dimension-1)
 rows=[];sources=[]
 remainders={label:reduceQ(p) for label,p in original.items()}
 assert remainders["O"]==zero
 for label in ("R","W","N1"):
  qp=remainders[label]
  for j in range(4):
   for l in range(2):
    current=el(qp) if l else qp
    for i in range(n):
     rows.append(flat(current));sources.append([label,i,l,j])
     if i+1<n:current=eu(current)
   if j+1<4:qp=eq(qp)
 assert len(rows)==3*dimension
 say("new_J2_complete_same_original_finite_Q_environment",uDegree=n,
     QQDimension=dimension,originalRows=len(rows),QMonicDegree=4,
     bothLambdaEmbeddingsAndAllURootsRetained=True,
     actualOriginalOLeadingInverseReturned=True,
     allOriginalReductionProductsReturned=True,
     noNewPhysicalHeadDeclaredUnit=True)
 prime=None
 for p in [1009,1013,1019,1031,1033]:
  coefficients_to_check=[c for row in rows for c in row]
  coefficients_to_check += [F[i] for i in range(n+1)]
  coefficients_to_check += [fmpq(1,3),fmpq(2,3)]
  if all(int(c.denominator)%p for c in coefficients_to_check):
   prime=p;break
 if prime is None:
  results.append(dict(uDegree=n,excluded=False,reason="no declared integral prime"))
  continue
 def mod(c):
  den=int(c.denominator)%prime;assert den
  return int(c.numerator)%prime*pow(den,-1,prime)%prime
 matrix=nmod_mat([[mod(c) for c in row] for row in rows],prime)
 at,rank=matrix.transpose().rref();rank=int(rank)
 selected=[]
 for i in range(rank):selected.append(next(j for j in range(len(rows)) if at[i,j]))
 selected_matrix=nmod_mat([[matrix[i,j] for j in range(dimension)] for i in selected],prime)
 say("new_J2_actual_integral_original_ideal_rank",uDegree=n,prime=prime,
     originalColumns=dimension,actualRank=rank,
     fixedQQMatrixAllCoefficientDenominatorsUnits=True,
     modularDeficitNotCalledQQDeficit=True)
 if rank==dimension:
  inverse=selected_matrix.inv()
  identity=nmod_mat(dimension,dimension,prime)
  for i in range(dimension):identity[i,i]=1
  assert selected_matrix*inverse==identity and inverse*selected_matrix==identity
  encoded=json.dumps([[int(inverse[i,j]) for j in range(dimension)] for i in range(dimension)],separators=(",",":")).encode()
  results.append(dict(uDegree=n,QQDimension=dimension,excluded=True,
    reason="actual integral fixed QQ original ideal matrix has full column rank",
    selectedRows=selected,allInverseProductsReturned=True,
    inverseBytes=len(encoded),inverseSHA256=hashlib.sha256(encoded).hexdigest()))
  say("new_J2_entire_original_finite_u_factor_excluded",**results[-1])
  continue
 if rank==0:
  results.append(dict(uDegree=n,excluded=False,reason="no original row pivot"))
  continue
 # A rank deficit triggers a NEW exact original physical Delta target.
 # Use the independent actual rows, a minor with nonzero modular determinant,
 # and verify the entire QQ target combination, never lift modular membership.
 rowrref,rrank=selected_matrix.rref();assert int(rrank)==rank
 columns=[next(j for j in range(dimension) if rowrref[i,j]) for i in range(rank)]
 block=fmpq_mat([[rows[i][j] for j in columns] for i in selected])
 exactinverse=block.inv()
 exactidentity=fmpq_mat(rank,rank)
 for i in range(rank):exactidentity[i,i]=1
 assert block*exactinverse==exactidentity and exactinverse*block==exactidentity
 B=fmpq_mat([rows[i] for i in selected])
 le=ec(K(0,1));ue=ec(K(uv));qe=(kz,ko,kz,kz)
 T0=es(es(er(ue,2),er(qe,fmpq(1,2))),er(em(ue,ue),2))
 Phi=ea(es(ea(T0,er(ue,4)),er(one,4)),qe)
 J=ea(T0,qe);xi=es(one,le);eta=es(er(one,4),er(le,3));S=es(er(one,5),er(le,4))
 NF=ea(em(es(er(one,3),er(le,4)),qe),em(em(J,xi),eta))
 Delta=es(em(Phi,NF),em(em(S,xi),em(T0,T0)))
 current=one;returned=None
 for power in range(1,5):
  current=em(current,Delta);target=flat(current)
  rhs=fmpq_mat([[target[j] for j in columns]])
  alpha=rhs*exactinverse
  back=alpha*B
  success=all(back[0,j]==target[j] for j in range(dimension))
  say("new_J2_actual_QQ_original_Delta_power_target",uDegree=n,
      power=power,allQQTargetColumns=dimension,allOriginalCoefficientProductsReturned=success,
      noModularMembershipLift=True,originalDeltaNonzeroPreviouslyPaid=True)
  if success:
   witness=json.dumps({"selectedOriginalRows":[sources[i] for i in selected],
      "coefficients":[str(alpha[0,i]) for i in range(rank)]},separators=(",",":")).encode()
   returned=dict(uDegree=n,QQDimension=dimension,excluded=True,
      reason="complete QQ original row combination equals actual physical Delta power",
      DeltaPower=power,allOriginalQQTargetColumnsReturned=True,
      certificateBytes=len(witness),certificateSHA256=hashlib.sha256(witness).hexdigest())
   if len(witness)<50000:returned["exactOriginalCombination"]=json.loads(witness)
   break
 if returned is None:
  returned=dict(uDegree=n,QQDimension=dimension,excluded=False,
      reason="four exact Delta targets not returned from selected actual original rows",
      allConstantFibersRetained=True)
 results.append(returned)
 say("new_J2_entire_original_Delta_nonzero_finite_factor_return",**returned)
 say("new_J2_finite_exact_arithmetic_counts",uDegree=n,divisionProducts=divchecks,inverseProducts=inversechecks)
say("new_complete_J2_original_finite_fiber_returns_finished",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    results=results,wholeJ2OriginalFiberExcluded=all(x["excluded"] for x in results) and len(results)==3,
    noEarlierProjectionOrNormGateReplayed=True,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
