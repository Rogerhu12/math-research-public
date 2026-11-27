#!/usr/bin/env python3
"""NEW fifth P201 block: actual lambda relation and original T,v geometry.

Only the degree-five completion block is addressed. The preceding source
is used through its necessary same-Q/same-lambda coefficient construction,
not its five-block standalone driver. A new 25-by-25 original-column unit
minor returns lambda-lambar. The SAME completed quotient then has a unit
original quadratic head, so the actual original three quadratic relations
make 1,T,v generate a finite algebra. We return the four original quadratic
polynomials, all commutator columns, and the COMPLETE original F6/NV values.
Actual column closure under both original multiplication matrices preserves
a source DAG. A unit is accepted only after the selected original product
columns, expanded over the entire coefficient field basis, times an actual
inverse give I. No modular zero head from another block is discarded.
120s/1GiB. 2026-11-28 Asia/Taipei. Small identities only, no payload.
"""
import os,time,json,hashlib,signal,resource,contextlib,io
from pathlib import Path
from flint import nmod_poly,nmod_mat
START=time.perf_counter();DEADLINE=START+120;PRIME=1009
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def identity(obj):
 raw=json.dumps(obj,separators=(",",":")).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def pdigest(a):
 out=identity([int(c) for c in a.coeffs()]);out["degree"]=int(a.degree());return out
def restore_deadline():
 signal.setitimer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
NAME="2026-11-28-unit211-Phi-zero-H1-P201-Q-linear-relation-and-same-lambda-original-ideals-8542.py"
SHA="dcd0cb2690aeee630ed8398e89ab79029694a7f4ffaa5361b3d32e88bac84311"
pp=Path(os.environ.get("ISP_H1_P201_Q_LAMBDA_SOURCE",str(Path(__file__).with_name(NAME))))
raw=pp.read_bytes();assert hashlib.sha256(raw).hexdigest()==SHA
ss=raw.decode()
cut="\nresults=[]";assert ss.count(cut)==1
prefix=ss.split(cut,1)[0]
# Expose precisely the constructed fifth-block original matrix and field,
# before the prior source's status/counter driver. No original input changes.
cut2="\n quotient_dimension=D-rank\n detail={}"
assert prefix.count(cut2)==1
prefix=prefix.split(cut2,1)[0]+"\n quotient_dimension=D-rank\n return locals()\n"
env={"__file__":str(pp),"__name__":"__necessary_original_Q_lambda_input_for_new_geometry__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(pp)+":necessary-prefix","exec"),env)
 restore_deadline()
 chosen=[phi for phi,e in env["factors"] if phi.degree()==5 and int(e)==1]
 assert len(chosen)==1
 phi=chosen[0]
 state=env["test_block"](phi)
restore_deadline()
p=PRIME;d=int(state["d"]);m=int(state["m"]);D=int(state["D"])
assert d==5 and m==6 and D==30 and int(state["rank"])==25
zero,one,u=state["zero"],state["one"],state["u"]
kr,kmul,kinv=state["kr"],state["kmul"],state["kinv"]
qbar=state["qbar"];venv=env["venv"];mp=env["mp"]
columns=state["lambda_columns"];tags=state["lambda_tags"]
flat=state["flat"];evaluateQ=state["evaluateQ"]
lower_dimension=D-d
lower=nmod_mat([[columns[j][i] for j in range(len(columns))]
               for i in range(d,D)],p)
rr,rank=lower.rref();assert int(rank)==lower_dimension
pivots=[]
for i in range(lower_dimension):
 j=next(j for j in range(len(columns)) if int(rr[i,j]))
 assert int(rr[i,j])==1;pivots.append(j)
assert len(set(pivots))==lower_dimension
square=nmod_mat([[columns[j][i] for j in pivots] for i in range(d,D)],p)
inverse=square.inv()
eye=nmod_mat(lower_dimension,lower_dimension,
 [1 if i==j else 0 for i in range(lower_dimension) for j in range(lower_dimension)],p)
assert square*inverse==eye
full=nmod_mat([[columns[j][i] for j in pivots] for i in range(D)],p)
relations=full*inverse
assert all(int(relations[d+i,j])==(1 if i==j else 0)
           for i in range(lower_dimension) for j in range(lower_dimension))
lbar=kr(nmod_poly([(-int(relations[a,0]))%p for a in range(d)],p))
lpowers=[one]
for j in range(1,max(env["degrees"])+1):lpowers.append(kmul(lpowers[-1],lbar))
for j in range(1,m):
 for a in range(d):
  col=(j-1)*d+a
  top=nmod_poly([int(relations[i,col]) for i in range(d)],p)
  assert kr(top+lpowers[j]*(u**a))==zero
def evaluate_lambda(poly):
 ans=zero
 for co in reversed(poly):ans=kr(ans*lbar+co)
 return ans
assert all(evaluate_lambda(poly)==zero for poly in state["values"])
say("new_fifth_P201_actual_same_lambda_linear_relation",
 actualP201Block=pdigest(phi),originalQRelation=state["q_return"],
 sameLambdaOriginalIdealRank=25,
 originalNonconstantLambdaUnitMinorOrder=25,
 selectedOriginalProducts=[tags[j] for j in pivots],
 selectedMinorIdentity=identity([[int(square[i,j]) for j in range(25)] for i in range(25)]),
 selectedMinorTimesInverseReturned=True,
 allFiveLambdaPowerFamiliesReturnedAsActualOriginalCombinations=True,
 exactResidualLambda=pdigest(lbar),
 allFourOriginalLambdaPolynomialsReturnedAtSameLambda=True,
 noQQLambdaFactorOrWholeP201FactorIdentification=True)

# Recover the already-constructed ACTUAL original module, without computing
# a new norm, cofactor, generic Gaussian, or factorization.
frame=env["ienv"]["generator"].gi_frame
assert frame is not None
ff=frame.f_locals
for key in ["head","rules","MT","MZ","r","comm","originals","extras","indices"]:
 assert key in ff,key
head=ff["head"];assert head.d==venv["one"]
def ea(co):
 # All original cleared coefficients used here are p-integral polynomials.
 # Never repair an unexpected denominator by an unproved residue inverse.
 assert co.d==venv["one"]
 return evaluateQ([kr(mp(c)) for c in co.n],qbar)
def eu(poly):
 ans=zero
 for co in reversed(poly.c):ans=kr(ans*lbar+ea(co))
 return ans
h=ea(head);assert h
ih=kinv(h,"same actual completed original three-quadratic head")
assert kmul(h,ih)==one
MT=[[kmul(eu(ff["MT"][i][j]),ih) for j in range(3)] for i in range(3)]
MV=[[kmul(eu(ff["MZ"][i][j]),ih) for j in range(3)] for i in range(3)]
e0=[one,zero,zero];eT=[zero,one,zero];eV=[zero,zero,one]
def madd(a,b):return [[kr(x+y) for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def mm(a,b):
 return [[kr(sum((a[i][k]*b[k][j] for k in range(3)),zero))
          for j in range(3)] for i in range(3)]
def mv(a,v):
 return [kr(sum((a[i][k]*v[k] for k in range(3)),zero)) for i in range(3)]
assert mv(MT,e0)==eT and mv(MV,e0)==eV
rules=[[kmul(eu(c),ih) for c in row] for row in ff["rules"]]
assert mv(MT,eT)==rules[0] and mv(MT,eV)==rules[1]
assert mv(MV,eT)==rules[1] and mv(MV,eV)==rules[2]
cache={(0,0):e0}
def monomial_column(t,v):
 if (t,v) not in cache:
  cache[t,v]=mv(MT,monomial_column(t-1,v)) if t else mv(MV,monomial_column(0,v-1))
 return cache[t,v]
def original_value_column(poly):
 out=[zero,zero,zero]
 for (ll,t,v),co in poly.v.items():
  scalar=kmul(ea(co),lpowers[ll] if ll<len(lpowers) else kr(lbar**ll))
  mon=monomial_column(t,v)
  out=[kr(x+scalar*y) for x,y in zip(out,mon)]
 return out
original_columns=[original_value_column(poly) for poly in ff["originals"]]
for j in ff["indices"]:assert original_columns[j]==[zero,zero,zero]
assert original_columns[2]==[kmul(eu(c),ih) for c in ff["r"]]
ta,tb=mm(MT,MV),mm(MV,MT)
comm=[[kr(ta[i][j]-tb[i][j]) for i in range(3)] for j in range(3)]
assert comm[0]==[zero,zero,zero]
for j in range(3):
 assert comm[j]==[kmul(eu(c),kmul(ih,ih)) for c in ff["comm"][j]]
extra_columns=[original_value_column(poly) for poly in ff["extras"]]
seeds=list(zip(["original_R","original_W","original_O","original_N1"],original_columns))
seeds+=list(zip(["actual_commutator_1","actual_commutator_T","actual_commutator_v"],comm))
seeds+=list(zip(["same_complete_F6","same_complete_NV"],extra_columns))
def vid(v):return identity([[int(c) for c in co.coeffs()] for co in v])
say("new_fifth_P201_actual_original_three_generator_geometry",
 actualP201Block=pdigest(phi),originalHead=pdigest(h),
 originalHeadInverseProductReturned=True,
 exactSamePoint="(1,T,v)*MT=T*(1,T,v); (1,T,v)*Mv=v*(1,T,v)",
 allSixTrueGeometricMultiplicationColumnsReturned=True,
 threeOriginalQuadraticRulesReturned=True,
 allFourOriginalQuadraticColumnsReturned=True,
 allThreeActualCommutatorColumnsReturned=True,
 completeOriginalF6AndNVIncluded=True,
 matricesIdentity=identity([[[[int(c) for c in co.coeffs()] for co in row]
                           for row in mat] for mat in [MT,MV]]),
 seedColumnIdentities=[dict(original=name,identity=vid(col)) for name,col in seeds],
 noPhysicalDInverseUsed=True,noBiggerFieldOrNormInverseUsed=True)

# Keep every actual source column. Gaussian normalization is only for
# dependence selection; propagated children act on ORIGINAL selected
# columns, not normalized vectors. Final unit proof uses original columns.
nodes=[];queue=[];selected=[];echelon=[]
def append_node(vector,kind,label=None,parent=None,action=None):
 idx=len(nodes)
 nodes.append(dict(vector=vector[:],kind=kind,label=label,parent=parent,action=action))
 queue.append(idx);return idx
for name,col in seeds:append_node(col,"original_seed",label=name)
cursor=0
while cursor<len(queue):
 idx=queue[cursor];cursor+=1
 col=nodes[idx]["vector"]
 rem=col[:]
 for pivot,row in echelon:
  co=rem[pivot]
  if co:rem=[kr(x-co*y) for x,y in zip(rem,row)]
 if not any(rem):continue
 pivot=next(i for i,c in enumerate(rem) if c)
 ii=kinv(rem[pivot],"residue dependence-selection pivot only")
 normalized=[kmul(c,ii) for c in rem]
 assert normalized[pivot]==one
 echelon.append((pivot,normalized));selected.append(idx)
 assert len(selected)<=3
 for action,mat in [("T",MT),("v",MV)]:
  child=mv(mat,col)
  child_idx=append_node(child,"actual_multiplication",parent=idx,action=action)
  assert nodes[child_idx]["vector"]==mv(mat,nodes[idx]["vector"])
rankK=len(selected)
for idx in selected:
 for mat in [MT,MV]:
  rem=mv(mat,nodes[idx]["vector"])
  for pivot,row in echelon:
   co=rem[pivot]
   if co:rem=[kr(x-co*y) for x,y in zip(rem,row)]
  assert not any(rem)
all_columns=[];column_origins=[]
for idx in selected:
 for a in range(d):
  vector=[kr(co*(u**a)) for co in nodes[idx]["vector"]]
  all_columns.append(flat(vector));column_origins.append(dict(sourceNode=idx,uPower=a))
size=3*d
matrix=(nmod_mat([[all_columns[j][i] for j in range(len(all_columns))]
                 for i in range(size)],p) if all_columns else nmod_mat(size,0,[],p))
actual_rank=0 if not all_columns else int(matrix.rref()[1])
assert actual_rank==rankK*d
detail={}
closed=(rankK==3)
if closed:
 assert matrix.nrows()==size and matrix.ncols()==size
 inverse=matrix.inv()
 eye=nmod_mat(size,size,[1 if i==j else 0 for i in range(size) for j in range(size)],p)
 assert matrix*inverse==eye
 unit=[int(inverse[j,0]) for j in range(size)]
 assert all(sum(all_columns[j][i]*unit[j] for j in range(size))%p==(1 if i==0 else 0)
            for i in range(size))
 detail=dict(originalUnitColumnOrigins=column_origins,
  selectedOriginalMatrixIdentity=identity([[int(matrix[i,j]) for j in range(size)] for i in range(size)]),
  originalUnitCombinationIdentity=identity(unit),
  fullOriginalMatrixTimesInverseReturned=True,
  originalConstantOneCombinationReturned=True)
remaining_geometry=d*(3-rankK)
dag=[{k:v for k,v in nd.items() if k!="vector"}|{"columnIdentity":vid(nd["vector"])} for nd in nodes]
say("new_fifth_P201_actual_original_geometry_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualP201Block=pdigest(phi),
 actualOriginalSeedCount=len(seeds),actualSourceDAG=dag,
 actualKRank=rankK,actualFullFieldRank=actual_rank,
 finiteOriginalGeometricGeneratorBound=15,
 actualResidualOriginalGeometricQuotientDimension=remaining_geometry,
 fifthActualCompletionBlockExcluded=closed,
 characteristicZeroDistinctWeightPairUpperBound=(9 if closed else 14),
 characteristicZeroDistinctWeightLambdaUpperBound=(54 if closed else 59),
 characteristicZeroDistinctFiveCoordinatePointUpperBound=162+remaining_geometry,
 characteristicZeroDistinctFullNormalizedPointUpperBound=2*(162+remaining_geometry),
 firstFourHeadZeroModuloBlocksRetained=True,
 wholeOriginalH1GraphExcluded=False,
 noQQModularFactorIdentification=True,
 originalProductDAGAndEachClosureEdgeReturned=True,
 completedFiniteOriginalModuleNakayamaOnly=True,
 noCoherentSourceReplaced=True,
 coefficientPayloadTransmitted=False,encodedOrSplitPayloadCreated=False,
 ordinaryISPClaim=False,arithmeticCounts=state["counts"],
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**detail)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
