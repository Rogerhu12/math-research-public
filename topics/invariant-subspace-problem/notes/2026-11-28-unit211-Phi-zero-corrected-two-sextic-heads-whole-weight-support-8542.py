#!/usr/bin/env python3
"""NEW corrected whole Phi: exact pure-weight support of both true sextic heads.
Regenerate only the two established sextic coefficient DEFINITIONS.
Do not rerun old action/overlap/matrix-defect/I6/cofactor proof gates.
New targets: actual paid-head factorization, whole QQ head gcd and its
two exact quotients.  A gcd of one means only finite common head zeros;
no original weight/fiber emptiness is inferred.  120 seconds / 1 GiB.
"""
import ast,hashlib,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
RAW_ALARM=signal.alarm
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
def bounded_alarm(seconds):
 tick();left=max(1,math.ceil(DEADLINE-time.perf_counter()))
 return RAW_ALARM(left if seconds<=0 else max(1,min(int(seconds),left)))
signal.alarm=bounded_alarm;signal.alarm(120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
NAME='2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py'
BASE_SHA='84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0'
path=pathlib.Path(__file__).with_name(NAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/NAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
marker='seeds=[rN,rNS,rPS,c1,c2]'
assert full.count(marker)==1
prefix=full[:full.index(marker)]
assert hashlib.sha256(prefix.encode()).hexdigest()=='e2e9bab84bca700400c8e26d5787208c9aceafe27c64aa7ecf828b0552025a1f'
tree=ast.parse(prefix,str(path));kept=[];omitted=[]
for node in tree.body:
 skip=isinstance(node,ast.Assert)
 if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
  skip=skip or isinstance(node.value.func,ast.Name) and node.value.func.id=='say'
 if isinstance(node,ast.For):
  # The sole definition loop creates the four original coefficient rows.
  # All other top-level loops in this exact prefix are the old proof gates.
  skip=not(isinstance(node.target,ast.Name) and node.target.id=='f'
           and isinstance(node.iter,ast.Name) and node.iter.id=='forms')
 if isinstance(node,ast.Assign):
  names={v.id for v in node.targets if isinstance(v,ast.Name)}
  skip=skip or bool(names & {'AA','BB','normalized','eT','eZ','ntrace'})
 if skip:omitted.append([node.lineno,type(node).__name__])
 else:kept.append(node)
ns={'__name__':'new_true_sextic_head_necessary_coefficient_definitions',
    '__file__':str(path),'print':lambda *a,**kw:None}
exec(compile(ast.fix_missing_locations(ast.Module(body=kept,type_ignores=[])),
             str(path)+'#coefficient-definitions-only','exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
R=ns['R'];ctx=ns['ctx'];O=ns['O'];Z=ns['Z']
exact=ns['exact'];profile=ns['profile'];strip_paid=ns['strip_paid']
seed=[ns['rN'],ns['rNS'],ns['rPS'],ns['c1'],ns['c2']]
expected=[
 ('NP',[0,1,2],
  'fcf79be98410a2eea2ebdb588b441b8f4aceb20acb4704a96ee34fc0012d01d5',
  '63c05c345cbc7055d652d46c173684bd7fdb159db3741232ef94d6cb58992bf6'),
 ('overlaps',[0,3,4],
  '2407107501f1790a288ecabd75f14f92c7602859bfc033727b76312675f91014',
  '9794fac2ee8bf7de08d80b9f3102480f1d06c9cfb4ff8be3981817dcfbd682fb')]
heads=[]
for label,chosen,knowncore,knownhead in expected:
 rr=[seed[i] for i in chosen]
 mu=[rr[1][1]*rr[2][2]-rr[1][2]*rr[2][1],
     rr[2][1]*rr[0][2]-rr[2][2]*rr[0][1],
     rr[0][1]*rr[1][2]-rr[0][2]*rr[1][1]]
 den=O
 for v in mu:den=exact(den,den.gcd(v.d))*v.d
 nums=[v.n*exact(den,v.d) for v in mu];content=Z
 for p in nums:content=content.gcd(p)
 primitive=[R(exact(p,content)) for p in nums]
 # Only the known scalar coefficient is regenerated, not its old
 # three-coordinate original-source certificate.
 C=sum((primitive[i]*rr[i][0] for i in range(3)),R())
 core,unit=strip_paid(C.n)
 lc=core.coefficient(0);core/=lc;unit*=lc
 assert core*unit==C.n and profile(core)['sha256']==knowncore
 head=ctx.from_dict({(ex[0],ex[1],0,0,0):v for ex,v in core.to_dict().items()
                     if int(ex[2])==6})
 assert profile(head)['sha256']==knownhead
 assert head and ns['weight'](head)
 heads.append((label,head))
say('existing_true_original_sextic_head_parameters_defined',
 originalFullSourceSHA256=BASE_SHA,
 originalNecessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 omittedOldTopLevelProofStatements=omitted,
 oldEighteenActionsOverlapsDefectsFifteenRowsAndCofactorGatesNotExecuted=True,
 fullRawN4P2OnlyAsKnownCoefficientDefinitions=True,
 exactExistingHeadSHA256=[profile(h)['sha256'] for _,h in heads])
newheads=[];factors_by_head=[]
for label,h in heads:
 tick();core,paidpart=strip_paid(h)
 lc=core.coefficient(0);core/=lc;paidpart*=lc
 assert core*paidpart==h and ns['weight'](core)
 content,factors=core.factor();back=ctx.constant(content);facts=[]
 for f,e in factors:
  e=int(e);back*=f**e
  facts.append({'factor':profile(f),'multiplicity':e})
 assert back==core
 newheads.append(core);factors_by_head.append(facts)
 say('new_true_sextic_head_complete_paid_support',
     label=label,originalHead=profile(h),
     removedOnlyOriginalPaidWeightPart=profile(paidpart),
     retainedPureWeightHead=profile(core),
     completeQQFactors=facts,
     completeHeadAndFactorProductsReturned=True,
     headUnitOnWholeCurrentPhi=int(core.total_degree())==0,
     everyRetainedWeightZeroFaceKept=True)
g=newheads[0].gcd(newheads[1]);assert g
g/=g.coefficient(0)
qa=exact(newheads[0],g);qb=exact(newheads[1],g)
assert qa*g==newheads[0] and qb*g==newheads[1]
# Coprime after the exact greatest common divisor, not a multivariate
# unit-ideal assertion.  No actual head is inverted in this script.
common_curve=int(g.total_degree())>0
global_head=any(int(h.total_degree())==0 for h in newheads)
off_curve_bound=int(qa.total_degree())*int(qb.total_degree())
gcontent,gfactors=g.factor();back=ctx.constant(gcontent);gf=[]
for f,e in gfactors:
 e=int(e);back*=f**e;gf.append({'factor':profile(f),'multiplicity':e})
assert back==g
say('new_two_true_original_sextic_heads_complete_QQ_gcd',
 completeCommonWeightSupport=profile(g),
 completeQQCommonFactorization=gf,
 firstExactQuotient=profile(qa),secondExactQuotient=profile(qb),
 bothFullWeightQuotientProductsReturned=True,
 wholeOriginalHeadZeroCurveRetained=common_curve,
 commonHeadZeroDistinctWeightPointUpperBound=None if common_curve else off_curve_bound,
 commonHeadZeroOffCommonCurveDistinctPointUpperBound=off_curve_bound,
 unlocalizedNecessaryI6EighteenGeneratorsOverWholePaidWeightRing=global_head,
 originalMeanI6EighteenGeneratorsOnHeadUnionOpen=True,
 noTwoVariableGcdOneToEmptyInference=True,
 allLambdaLeadingZeroFibersKept=True,
 noDOrItsNormInverse=True,wholePhiExcluded=False,ordinaryISPClaim=False,
 noCoefficientPayloadSaved=True,
 sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
