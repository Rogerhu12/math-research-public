#!/usr/bin/env python3
"""NEW correct whole Phi: individual N/P and FULL isolated N4 original rows.
Only the established true three rules, N1, and raw dual Gram definitions
are reused. No old weighted NS/PS, 15-column gate, C6 cofactor or fixed
12 resultant is executed. New original rows are moment R6, Nlow, Plow,
and full Vlow, with their T/z actions; original I6 remains intact.
No physical D, norm, or new lambda head is inverted. The restored whole
original equal-weight theorem alone pays m. 120 seconds / 1 GiB.
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
SECOND='2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py'
def input_path(name):
 path=pathlib.Path(__file__).with_name(name)
 if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/name
 return path
path=input_path(NAME);full=path.read_text()
assert hashlib.sha256(full.encode()).hexdigest()=='84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0'
assert hashlib.sha256(input_path(SECOND).read_bytes()).hexdigest()=='5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7'
marker='NS=es(esm(em(b,N4(rows[2])),em(c,N4(rows[3]))),'
assert full.count(marker)==1
prefix=full[:full.index(marker)]
assert len(prefix)==11204
assert hashlib.sha256(prefix.encode()).hexdigest()=='2693b11fb556d56d04b04750be5342f063bedb3d03cefb11faf2d49dee2106a6'
kept=[];omitted=[]
for node in ast.parse(prefix,str(path)).body:
 skip=isinstance(node,ast.Assert)
 if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
  skip=skip or isinstance(node.value.func,ast.Name) and node.value.func.id=='say'
 if isinstance(node,ast.For):
  skip=not(isinstance(node.target,ast.Name) and node.target.id=='f'
           and isinstance(node.iter,ast.Name) and node.iter.id=='forms')
 if isinstance(node,ast.Assign):
  names={v.id for v in node.targets if isinstance(v,ast.Name)}
  skip=skip or bool(names & {'AA','BB','AB','BA','comm','c1','c2',
                            'normalized','eT','eZ','ntrace'})
 if skip:omitted.append([node.lineno,type(node).__name__])
 else:kept.append(node)
ns={'__name__':'new_correct_individual_NP_and_entire_NV_definitions',
    '__file__':str(path),'print':lambda *a,**kw:None}
exec(compile(ast.fix_missing_locations(ast.Module(body=kept,type_ignores=[])),
             str(path)+'#true-rules-and-Gram-definitions-only','exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
ns['tick']=tick
R=ns['R'];Alg=ns['A'];ctx=ns['ctx'];O=ns['O'];Z=ns['Z']
exact=ns['exact'];profile=ns['profile'];weight=ns['weight']
u,Q,lam,T,z,ell,m,delta,M,bc,P02,T0,J=(
 ns[k] for k in ('u','Q','lam','T','z','ell','m','delta','M','bc','P02','T0','J'))
ff,tt,V,W,A1,ww=(ns['ff'],ns['tt'],ns['V'],ns['W'],ns['A1'],lam-1-T)
A2=ns['A2'];B3=ns['B3'];MT=ns['MT'];MZ=ns['MZ'];rN=ns['rN']
# m is paid by the independently read WHOLE original equal-weight theorem.
# No payment is borrowed from the withdrawn compact Phi chain or W.
assert weight(m.n) and m.n
ns['paidSupport']=ns['paidSupport']*m.n
ck=ns['ck'];strip_paid=ns['strip_paid'];ldegree=ns['ldegree']
for value in [ell,m,M,bc,P02,1/m,1/ell,1/M]:ck(value)
defined_nodes=len(ns['nodes'])
defined_products=ns['statistics']['newMultiplicationCoordinates']
statistics={'newRawIndividualNPColumns':0,'newValueRowCoordinates':0,
            'newActionCoordinates':0,'newFixedCofactorCoordinates':0}
def scalar(value):return Alg.scalar(value)
def affine(value,label):return Alg.affine(value,label)
def check_vector(vec,total):
 assert len(vec)==3
 for j,v in enumerate(vec):
  ck(v);assert ldegree(v)<=total-int(j>0)
 return [ldegree(v) for v in vec]
def vprofile(vec):return [{'numerator':profile(v.n),'denominator':profile(v.d)} for v in vec]
say('new_individual_value_original_prefix_ready',
 fullOriginalSourceSHA256='84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0',
 actualPrefixBytes=len(prefix),
 actualPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 omittedOldTopLevelProofStatements=omitted,
 oldWeightedNSPSAndFifteenColumnCofactorAndFixed12NotExecuted=True,
 wholeOriginalEqualWeightMUnitUsed=True,noPhysicalDOrNormInverse=True)

# First NEW complete individual raw cubic source: both coordinates are
# computed from the same original dual Gram, not from weighted NS/PS.
NB=ns['N4'](ns['rows'][2])
PB=ns['P2'](ns['rows'][2])
for label,ee in [('N4B',NB),('P2B',PB)]:
 for value in ee:
  check_vector(value.v,3);statistics['newRawIndividualNPColumns']+=1
 say('new_full_individual_original_cubic_coordinates',
     label=label,even=vprofile(ee[0].v),odd=vprofile(ee[1].v),
     lambdaDegreeBounds=[3,2,2],
     sameTrueDualProductAndSameOriginalGram=True,
     conjugateCRowUsesSameRhoExtension=True)

new_rows=[]
def record_value(label,value,total):
 degrees=check_vector(value.v,total);statistics['newValueRowCoordinates']+=3
 new_rows.append((label,value,total))
 say('new_complete_original_value_row_in_correct_three_generators',
     label=label,coefficientProfiles=vprofile(value.v),lambdaDegrees=degrees,
     totalGeometryDegreeUpperBound=total,
     actualOriginalMultiplicationDAGNode=value.id,
     allWeightDenominatorsAlreadyPaid=True,
     allMomentAndIndividualOriginalConditionsKept=True,
     physicalDOnlyMultipliedNeverInverted=True)

TA=affine(T,'original_T');ZA=affine(z,'original_z')
fA=affine(ff,'original_f');tA=affine(tt,'original_t')
VA=affine(V,'original_V');WA=affine(W,'original_W')
A1A=affine(A1,'original_A1');wA=affine(ww,'original_w')
Tsq=TA*TA
D=scalar(ell*A2)-Tsq
Kval=scalar(ell*ell*B3)-TA.scale(3*ell*A2)+(Tsq*TA).scale(2)
Dsq=D*D
Acenter=scalar(1)+TA.scale(1/ell)
# q=M*sval^2-D and H=Kval-2*m*D*sval come from the TWO
# shifted original moment equations. The following cleared expressions
# use only q,H, and original individual errors. No D inverse occurs.
R6=(Kval*Kval).scale(M)-(Dsq*D).scale(4*m*m)
record_value('moment_R6',R6,6)
Nadd=(Kval*Acenter).scale(2*lam*P02/m)+Dsq.scale(4*lam*P02*m/(ell*M))
Nlow=D*NB[1]+Nadd
record_value('individual_Nlow',Nlow,5)
Pbracket=(Acenter*Acenter).scale(3)+D.scale((3*m*m/(ell*ell)+delta)/M)
Padd=(Kval*Pbracket).scale(P02/(2*m))+(Acenter*Dsq).scale(6*P02*m/(ell*M))
Plow=D*PB[1]+Padd
record_value('individual_Plow',Plow,5)

# FULL N4, not one component or a Phi multiple. These three exact general
# identities were proved in nine FREE original variables in:
# R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md
# They require neither W nor Phi nor D!=0. Here they are transported by
# the true first-mean multiplication DAG to the NEW correct three columns.
c_lambda=3-2*lam
Z0=(A1A.scale(ell*ell)+fA.scale(4*ell*ell*(1-2*lam))
    +(fA*D).scale(2*ell)
    +(wA*(scalar(ell*c_lambda)+TA)).scale(2*ell*u)
    +(VA*(scalar(ell*ell)+TA.scale(ell*c_lambda)+Tsq)).scale(2)
    +(tA*(Tsq-scalar(ell*ell))).scale(2*bc))
Z1=((scalar(ell*c_lambda)+TA.scale(2))*
     (VA.scale(u)-WA.scale(ell))).scale(2)-wA.scale(2*ell*M)+(TA*tA).scale(4*bc*m)
Z2=(VA.scale(2*(u*u-ell*ell*Q))-WA.scale(4*m*ell)
    -fA.scale(2*ell*M)-tA.scale(2*bc*M))
for value,total in [(Z0,3),(Z1,2),(Z2,1)]:
 check_vector(value.v,total)
# On the ORIGINAL moment ring,
# Vlow = D*ell^2*N4(Vphys) + Z1*H/(2m) - D*Z2*q/M.
# It retains every coefficient of the same isolated value vector.
Vlow=D*Z0+(Kval*Z1).scale(1/(2*m))+(Dsq*Z2).scale(1/M)

record_value('entire_N4_Vlow',Vlow,5)

# Original I6 already has its exact 15-column presentation. Add each NEW
# row and its TWO original-variable actions, without replaying the old
# 15 columns. The published four matrix defects imply stable closure
# for the resulting exact auxiliary I10 presentation.
new_relations=[]
for label,value,total in new_rows:
 for action,matrix,original_factor in [('one',None,None),('T',MT,TA),('z',MZ,ZA)]:
  if matrix is None:vec=value.v
  else:
   vec=ns['mv'](matrix,value.v)
   via=(original_factor*value).v
   assert vec==via
   statistics['newActionCoordinates']+=3
  degrees=check_vector(vec,total+int(matrix is not None))
  new_relations.append((label,action,vec))
say('new_four_value_rows_and_original_action_closure',
 newRelationCount=len(new_relations),originalFifteenRelationsRetained=True,
 newRelationLambdaDegrees=[[name,action,[ldegree(v) for v in row]]
                           for name,action,row in new_relations],
 exactAuxiliaryPresentation='I10=I6+(R6,Nlow,Plow,Vlow), 15 old plus 12 new columns',
 oldMatrixDefectsUsedAsPublishedTheoremNotReexecuted=True,
 noFreenessOrBareThreeVectorAssociativityAssumed=True,
 noPhysicalWholeSystemSufficiencyClaim=True)

# GENUINELY NEW fixed scalar sources: each includes full N4(V), one
# individual N/P condition, and the true N1. Cancel only a common factor
# of ALL THREE actual multipliers, then return ALL THREE original columns.
def original_cofactor(label,row_names,rows):
 tick()
 mu=[rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1],
     rows[2][1]*rows[0][2]-rows[2][2]*rows[0][1],
     rows[0][1]*rows[1][2]-rows[0][2]*rows[1][1]]
 if not any(mu):
  say('new_individual_NV_original_cofactor_zero',label=label,
      allOriginalRowsAndZeroFibersRetained=True)
  return
 denominator=O
 for v in mu:
  ck(v);denominator=exact(denominator,denominator.gcd(v.d))*v.d
 numerators=[v.n*exact(denominator,v.d) for v in mu];content=Z
 for v in numerators:content=content.gcd(v)
 assert content
 primitive=[R(exact(v,content)) for v in numerators]
 returned=[sum((primitive[i]*rows[i][j] for i in range(3)),R()) for j in range(3)]
 assert not returned[1] and not returned[2]
 statistics['newFixedCofactorCoordinates']+=3
 C=ck(returned[0]);core,paidpart=strip_paid(C.n)
 if core:
  lc=core.coefficient(0);core/=lc;paidpart*=lc
 assert core*paidpart==C.n
 degree=max((int(ex[2]) for ex in core.to_dict()),default=-1)
 leading=ctx.from_dict({(ex[0],ex[1],0,0,0):v for ex,v in core.to_dict().items()
                       if int(ex[2])==degree}) if core else Z
 say('new_individual_NV_complete_original_scalar_return',
     label=label,originalRows=row_names,
     threeActualMultiplierCommonContent=profile(content),
     actualOriginalScalarNumerator=profile(C.n),
     actualOriginalScalarDenominator=profile(C.d),
     allThreeOriginalModuleCoordinatesReturned=True,
     retainedOriginalNecessaryPolynomial=profile(core),
     actualLambdaDegree=degree,actualLambdaLeadingNumerator=profile(leading),
     onlyWholeOriginalPaidWeightFactorsRemoved=True,
     allCommonContentAndLambdaLeadingZeroFibersKept=True,
     physicalDOrItsNormNeverInverted=True,
     wholePhiExcluded=bool(core) and int(core.total_degree())==0)
original_cofactor('N1_individual_N_full_NV',
                  ['N1','individual_Nlow','entire_N4_Vlow'],
                  [rN,Nlow.v,Vlow.v])
original_cofactor('N1_individual_P_full_NV',
                  ['N1','individual_Plow','entire_N4_Vlow'],
                  [rN,Plow.v,Vlow.v])
say('new_correct_whole_Phi_individual_NP_full_NV_original_input_finished',
 statistics=statistics,
 newMultiplicationCoordinates=ns['statistics']['newMultiplicationCoordinates']-defined_products,
 newDAGNodes=len(ns['nodes'])-defined_nodes,
 allOriginalI6AndAllFourNewValueRowsRetained=True,
 noOldWeightedSixOrFirstHeadOrFixed12ProofGateReplayed=True,
 noDOrItsNormInverse=True,noCoefficientCacheOrChunksSaved=True,
 sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
RAW_ALARM(0)
