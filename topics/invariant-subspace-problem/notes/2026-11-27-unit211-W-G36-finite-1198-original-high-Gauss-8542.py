#!/usr/bin/env python3
"""NEW finite original return on the saved COMPLETE F1198 G36 cover.
Reads six exact parameter chunks and their manifest. Never executes the
completed generic G36 source. Splits off every B80 norm-zero k fibre in QQ,
then returns the fixed original 48x35 matrix on the entire complementary
finite constant algebra. Every modular conclusion uses the monic finite
free Z_(p) model, not multivariate modular emptiness. 180 seconds / 4 GiB.
"""
import json,time,hashlib,signal,resource,math,contextlib,io,base64,zlib
from pathlib import Path
from fractions import Fraction
from flint import fmpq_poly,fmpq,nmod_poly,fmpz_mod_poly_ctx,fq_default_ctx,fq_default_poly_ctx
start=time.perf_counter();deadline=start+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r,separators=(',',':')),flush=True)
def coefficients(pp):return [str(c) for c in pp.coeffs()]
def qexact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a;return q
P=lambda v=():fmpq_poly([fmpq(x) for x in v])
one=P([1]);kk=P([0,1])
def monic(p):assert p;return p/p[p.degree()]
def digest_json(obj):
 bb=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
def report_poly(pp,include_mod=None):
 co=coefficients(pp);out=dict(degree=int(pp.degree()),**digest_json(co))
 if out['bytes']<=8192:out['coefficients']=co
 if include_mod is not None:out['modularCoefficients']=[cm(c,include_mod) for c in pp.coeffs()]
 return out
manifest_path=Path(__file__).with_name('2026-11-27-unit211-W-G36-exact-1198-cover-8542.manifest.json')
manifest_raw=manifest_path.read_bytes()
assert hashlib.sha256(manifest_raw).hexdigest()=='f063cc9bb1588b0f03136adc6657c45b25670d462b50244fcf2cf2839a275c1a'
manifest=json.loads(manifest_raw);chunks=[]
assert manifest['degree']==1198 and len(manifest['chunks'])==6
for i,rec in enumerate(manifest['chunks']):
 assert rec['index']==i and Path(rec['file']).name==rec['file']
 raw=Path(__file__).with_name(rec['file']).read_bytes()
 assert len(raw)==rec['bytes'] and hashlib.sha256(raw).hexdigest()==rec['sha256']
 part=json.loads(raw)
 assert part['index']==i and part['total']==6
 encoded=part['dataChunk']
 assert len(encoded)==rec['dataCharacters']
 assert hashlib.sha256(encoded.encode()).hexdigest()==rec['dataSHA256']
 chunks.append(encoded)
encoded=''.join(chunks)
assert len(encoded)==manifest['base64Characters']
assert hashlib.sha256(encoded.encode()).hexdigest()==manifest['base64SHA256']
compressed=base64.b64decode(encoded,validate=True)
assert len(compressed)==manifest['compressedBytes']
cover_raw=zlib.decompress(compressed)
assert len(cover_raw)==manifest['rawBytes']
assert hashlib.sha256(cover_raw).hexdigest()==manifest['rawSHA256']=='a464f7f2c50dbe4c7661d25b65f363ac6fb945fac76bfec9fa2474c88bb7cb74'
cover=P(json.loads(cover_raw))
assert cover.degree()==1198 and cover[1198]==1
assert cover.gcd(cover.derivative()).degree()==0
removed=[]
for name,atom in [('k',kk),('k+1',kk+1),('k+2',kk+2),('k+4',kk+4)]:
 multiplicity=0
 while cover.degree()>0:
  q,r=divmod(cover,atom)
  if r:break
  assert q*atom==cover;cover=q;multiplicity+=1
 if multiplicity:removed.append([name,multiplicity])
B80=P(["81916813537087272878090485760","2547325176658345904765034037248","34430073454090116575450793771008","271909481805379320836501264138240","1463505544168437221237861226905600","6274258877132501718546223690940416","25246270011612505759869241011470336","99137103614414984422799375884877824","338341162048177879520403256086888448","877454574558587052352522772008665088","1486831735774071219217859065480740864","841137030218825228908413895248445440","-3404949487929336438377519935446319104","-11805551656459862083652012633768329216","-18385781168082911611654100769526775808","-10643092330042251449026422886449020928","18949068249356034221341886012645703680","56577873872815944911702284681133162496","67423288384685836611606100951577919488","24725774175724760777121918859811487744","-55346954047697611549202781173903785984","-115038461976625576625694158883351691264","-102572228651514690927960497257074130944","-21997627337551211149231595019246239744","67648684293459388916342906097699389440","104376042910099864164834138401668071424","73688960566964586875781493815431397376","11250566572390300600496718498964176896","-35679950868643417572071367571150995456","-45387716517848655066427947824854335488","-27682568779436560584725430187149230080","-4845566800980818675860665788323069952","8239052328751396236856376931742908416","9863217064298316877029959148710658048","5720665397273961035050733928809365504","1422781492047178662490638658731114496","-737870525671054358458538474058760192","-1073847614980690562475889969076772864","-661607945124217433677195756471336960","-234553878578297412872879881664382976","-15404110720027924358853806231867392","42831227043837471905493285402036224","34779854679244523595365618026413312","16477198381669382538486494091023744","5228214517785857205645108010507648","854748311940977066177728129200224","-198156429589110960481225017198272","-227940757477093626168893358174704","-109218183355563884006989925758648","-37048542094340488891515194939008","-9451631418113215198181336197596","-1607424909277811127058925375708","-129943537806703281133452846","143395069328675485574524851738","76264590356269091535189679519","27792476546206712573173384658","8027607273838973134692038211","1863391518849283432024742149","330241707091273716749292559","35995886961085366348406838","-1364016733840960289784337","-1788801448325654687316815","-492935954577809297055041","-85772148009337960840978","-9807002719282136151009","-514396011012762126941","55623450362616766501","15950300013694785150","1605379304786116775","20274406602278441","-16321749133263342","-2139473863698584","-46969879106130","23177688385028","4221831301848","418735942960","27997641312","1305024192","41154688","795904","7168"])
assert B80.degree()==80
assert digest_json(coefficients(B80))['sha256']=='b7c0f7e22050450b7cc7ad83ea151028cef75ac8d94f23519397aac92da1d284'
normcover=B80*kk*(kk+1)*(kk+2)*(kk+4)
low=monic(cover.gcd(normcover));high=monic(qexact(cover,low))
assert low*high==cover
gb,sb,tb=low.xgcd(high);assert sb*low+tb*high==gb and gb.degree()==0
gn,sn,tn=high.xgcd(normcover);assert sn*high+tn*normcover==gn and gn.degree()==0
lc,lf=low.factor();back=P([lc]);lowfactors=[]
for ff,mul in lf:
 back*=ff**int(mul)
 lowfactors.append(dict(multiplicity=int(mul),**report_poly(ff)))
assert back==low
say(stage='G36_saved_exact_1198_input_new_QQ_low_high_partition',
    originalSavedDegree=1198,removedOnlyAlreadyPaidKLines=removed,
    afterPaidKLines=report_poly(cover),lowNormCover=report_poly(low),
    completeLowQQFactors=lowfactors,highNormUnitCover=report_poly(high),
    completeQQPartitionAndBothBezoutProductsReturned=True,
    lowNormBound=80,allLowQBranchesRetained=True,
    noGenericG36SourceExecuted=True,wholeG36Excluded=False)

# Only the published complete original Gram-construction prefix is used.
dep=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py')
depraw=dep.read_bytes()
assert hashlib.sha256(depraw).hexdigest()=='10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1'
oldtext=depraw.decode();marker='\n# New mathematical input: all four original quadratics'
assert oldtext.count(marker)==1
prefix=oldtext[:oldtext.index(marker)]
ns={'__file__':str(dep),'__name__':'__original_Gram_prefix_only__'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(prefix,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
names=['E1','EBe','EBo','N1','NS','PS']
raworiginal=[ns['symbolic'][name] for name in names]
for rr in raworiginal:
 assert all(all(mm[j]==0 for j in range(2,len(mm))) for mm in rr.d.to_dict())
 assert all(all(mm[j]==0 for j in range(5,len(mm))) for mm in rr.n.to_dict())
gcoeff=[P(v)/32 for v in [["4096","9216","7680","3072","592","24","-10","-1"],["-6144","-16128","-14336","-6048","-1416","-186","-9"],["512","6016","6560","2528","468","50","2"],["1792","832","-832","-392","-50","-2"],["-256","-544","-24","24","4"],["-192","0","-8"],["32"]]]
assert len(gcoeff)==7 and gcoeff[6]==1
integral_arrays=[cover,low,high,normcover]+gcoeff
original_rational_coefficients=[]
for rr in raworiginal:
 original_rational_coefficients.extend(rr.n.to_dict().values())
 original_rational_coefficients.extend(rr.d.to_dict().values())
def cm(cc,p):
 q=Fraction(str(cc));assert q.denominator%p
 return q.numerator%p*pow(q.denominator%p,-1,p)%p
rejected=[];prime=None
for pp in [1009,1013,1019,1021,1031,1033,1039,1049,1051]:
 if any(Fraction(str(c)).denominator%pp==0 for f in integral_arrays for c in f.coeffs()) or any(Fraction(str(c)).denominator%pp==0 for c in original_rational_coefficients):
  rejected.append([pp,'an actual rational denominator is not p-integral']);continue
 mp=lambda f:nmod_poly([cm(c,pp) for c in f.coeffs()],pp)
 hh,nn=mp(high),mp(normcover)
 if hh.degree()!=high.degree() or int(hh[hh.degree()])!=1:
  rejected.append([pp,'monic complete high degree not preserved']);continue
 gg,ss,tt=hh.xgcd(nn);assert ss*hh+tt*nn==gg
 if gg.degree()!=0:
  rejected.append([pp,'modular high cover meets an explicitly retained weight norm']);continue
 gi=pow(int(gg[0]),-1,pp)
 assert (ss*gi)*hh+(tt*gi)*nn==nmod_poly([1],pp)
 prime=pp;break
assert prime is not None
MP=lambda f:nmod_poly([cm(c,prime) for c in f.coeffs()],prime)
hmod=MP(high);nmod=MP(normcover)
content,factors=hmod.factor();modback=nmod_poly([content],prime)
for ff,mul in factors:modback*=ff**int(mul)
assert modback==hmod
say(stage='G36_new_finite_original_good_prime_and_complete_factorization',
    prime=prime,rejectedPrimes=rejected,QQHighDegree=int(high.degree()),
    modularHighDegree=int(hmod.degree()),monicFullQSixRelation=True,
    allActualOriginalRationalCoefficientsPIntegral=True,
    completeNormBezoutActuallyMultipliedBack=True,
    fullModularFactorizationProductActuallyReturned=True,
    completeModularFactors=[dict(degree=int(ff.degree()),multiplicity=int(mul),coefficients=[int(c) for c in ff.coeffs()]) for ff,mul in factors],
    finiteFreeBaseRank=int(high.degree()),finiteFreeWeightRank=6*int(high.degree()),
    multiplicitiesKeptForFiniteArtinianNakayama=True,
    wholeG36Excluded=False)

monomials=sorted([(i,j,h) for i in range(5) for j in range(5-i) for h in range(5-i-j)],key=lambda z:(sum(z),z[1],z[0],z[2]),reverse=True)
assert len(monomials)==35 and monomials[-1]==(0,0,0)
monindex={m:i for i,m in enumerate(monomials)}
allresults=[];splitrecords=[];inverse_count=0
class EZeroDivisor(Exception):
 def __init__(self,g,q):self.g=g;self.q=q
for factor_index,(ff,multiplicity) in enumerate(factors):
 # The official finite-field constructor checks the complete actual modulus.
 kmod=fmpz_mod_poly_ctx(prime)([int(c) for c in ff.coeffs()])
 FC=fq_default_ctx(modulus=kmod,var='k',check_modulus=True)
 assert FC.modulus()==kmod
 kg=FC([0,1]);fc0=FC(0);fc1=FC(1)
 assert sum((FC(int(ff[j]))*kg**j for j in range(ff.degree()+1)),fc0)==0
 kinv=kg.inverse();assert kg*kinv==fc1
 PC=fq_default_poly_ctx(FC)
 def ev(pp):return FC([cm(c,prime) for c in pp.coeffs()])
 qmonic=PC([ev(c) for c in gcoeff])
 assert qmonic.degree()==6 and qmonic[6]==fc1
 powers={0:fc1}
 def kp(j):
  if j not in powers:powers[j]=kg**j if j>=0 else kinv**(-j)
  return powers[j]
 def in_q_weight(po):
  dct={}
  for mm,c in po.to_dict().items():
   assert all(mm[j]==0 for j in range(2,len(mm)))
   i,j=int(mm[0]),int(mm[1])
   dct[i]=dct.get(i,fc0)+FC(cm(c,prime))*kp(j-i)
  return PC([dct.get(i,fc0) for i in range(max(dct,default=-1)+1)])
 def in_q_geometry(po):
  dct={}
  for mm,c in po.to_dict().items():
   assert all(mm[j]==0 for j in range(5,len(mm)))
   i,j=int(mm[0]),int(mm[1]);mon=tuple(map(int,mm[2:5]))
   if mon not in dct:dct[mon]={}
   dd=dct[mon];dd[i]=dd.get(i,fc0)+FC(cm(c,prime))*kp(j-i)
  return {mon:PC([dd.get(i,fc0) for i in range(max(dd,default=-1)+1)]) for mon,dd in dct.items()}
 native_original=[]
 for rr in raworiginal:
  den=in_q_weight(rr.d)
  dq,dr=divmod(den,qmonic);assert dq*qmonic+dr==den
  dg,ds,dt=dr.xgcd(qmonic);assert ds*dr+dt*qmonic==dg and dg.degree()==0
  deninv=ds*dg[0].inverse()
  assert deninv.mul_mod(dr,qmonic)==PC([1])
  inverse_count+=1
  pp=in_q_geometry(rr.n)
  out={mon:cf.mul_mod(deninv,qmonic) for mon,cf in pp.items()}
  for mon,cf in pp.items():
   quotient,remainder=divmod(cf,qmonic)
   assert quotient*qmonic+remainder==cf
   assert out[mon].mul_mod(dr,qmonic)==remainder
  native_original.append(out)
 def pdata(pp):return [[int(c) for c in z.to_list()] for z in pp.coeffs()]
 def process(H,path):
  global inverse_count
  class A:
   def __init__(self,v=0):
    if isinstance(v,A):self.p=v.p;return
    vv=PC(v);qq,rr=divmod(vv,H)
    assert qq*H+rr==vv;self.p=rr
   def __bool__(self):return bool(self.p)
   def __neg__(self):return A(-self.p)
   def __add__(self,v):return A(self.p+A(v).p)
   __radd__=__add__
   def __sub__(self,v):return A(self.p-A(v).p)
   def __rsub__(self,v):return A(v)-self
   def __mul__(self,v):return A(self.p.mul_mod(A(v).p,H))
   __rmul__=__mul__
   def __eq__(self,v):return self.p==A(v).p
   def inv(self):
    global inverse_count
    assert self
    gg,ss,tt=self.p.xgcd(H)
    assert ss*self.p+tt*H==gg
    if gg.degree()>0:
     qq,rr=divmod(H,gg);assert not rr and qq*gg==H and 0<gg.degree()<H.degree()
     raise EZeroDivisor(gg,qq)
    out=A(ss*gg[0].inverse());assert self*out==1
    inverse_count+=1;return out
   def data(self):return pdata(self.p)
  try:
   rows=[];labels=[]
   for ni,rr in enumerate(native_original):
    formal_degree=2 if ni<4 else 3
    for mm in sorted([m for m in monomials if sum(m)<=4-formal_degree],key=lambda z:(sum(z),z[1],z[0],z[2])):
     row=[A() for _ in monomials]
     for m,c in rr.items():
      target=tuple(m[j]+mm[j] for j in range(3));assert sum(target)<=4
      row[monindex[target]]=row[monindex[target]]+A(c)
     rows.append(row);labels.append([names[ni],mm])
   assert len(rows)==48
   basis0=[];tags=[];pivots=[]
   for idx,rawrow in enumerate(rows):
    row=rawrow[:];tag={idx:A(1)}
    for brow,pv,bt in zip(basis0,pivots,tags):
     cf=row[pv]
     if not cf:continue
     row=[row[j]-cf*brow[j] for j in range(35)]
     for ii,vv in bt.items():tag[ii]=tag.get(ii,A())-cf*vv
    if not any(row):continue
    pv=next(j for j,v in enumerate(row) if v);iv=row[pv].inv()
    row=[v*iv for v in row];tag={j:v*iv for j,v in tag.items() if v}
    assert row[pv]==1 and all(not row[j] for j in pivots)
    for j in range(35):assert sum((vv*rows[ii][j] for ii,vv in tag.items()),A())==row[j]
    basis0.append(row);tags.append(tag);pivots.append(pv)
    if len(basis0)==35:break
   full=len(basis0)==35;actual={};unit_verified=False
   if full:
    target=[A(int(j==34)) for j in range(35)];rem=target[:]
    for brow,pv,bt in zip(basis0,pivots,tags):
     cf=rem[pv]
     if not cf:continue
     rem=[rem[j]-cf*brow[j] for j in range(35)]
     for ii,vv in bt.items():actual[ii]=actual.get(ii,A())+cf*vv
    assert not any(rem)
    for j in range(35):assert sum((vv*rows[ii][j] for ii,vv in actual.items()),A())==target[j]
    unit_verified=True
   cert=dict(prime=prime,kFactor=[int(c) for c in ff.coeffs()],qModulus=pdata(H),labels=labels,pivots=pivots,allBasisRows=[{str(j):v.data() for j,v in tag.items()} for tag in tags],originalUnitCombination={str(j):v.data() for j,v in actual.items()})
   rec=dict(kFactorIndex=factor_index,kDegree=int(ff.degree()),kMultiplicity=int(multiplicity),qPath=path,qDegree=int(H.degree()),originalRows=48,columns=35,rank=len(basis0),allBasisOriginalThirtyFiveColumnProductsActuallyVerified=True,originalUnitThirtyFiveColumnProductsActuallyVerified=unit_verified,allActualInverseProductsOne=True,fullColumnRank=full,certificate=digest_json(cert))
   allresults.append(rec)
   say(stage='new_G36_finite_whole_Q_six_algebra_original_48x35_return',**rec,wholeG36Excluded=False,claimExcluded=False)
  except EZeroDivisor as ex:
   assert ex.g*ex.q==H and 0<ex.g.degree()<H.degree() and 0<ex.q.degree()<H.degree()
   rec=dict(kFactorIndex=factor_index,qPath=path,left=pdata(ex.g),right=pdata(ex.q),wholeQPolynomialProductActuallyVerified=True,bothOriginalBranchesRetained=True)
   splitrecords.append(rec)
   say(stage='new_G36_finite_actual_Q_zero_divisor_complete_split',**rec,claimExcluded=False)
   process(ex.g,path+'/a');process(ex.q,path+'/b')
 process(qmonic,'G36_Q6')
passed=bool(allresults) and all(r['fullColumnRank'] and r['originalUnitThirtyFiveColumnProductsActuallyVerified'] for r in allresults)
signal.alarm(0)
say(stage='new_G36_entire_high_QQ_cover_original_finite_Gauss_return_complete',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),prime=prime,fullPublishedCoverDegree=1198,entireQQHighCover=report_poly(high,prime),retainedQQNormZeroCover=report_poly(low),retainedQQNormZeroFactors=lowfactors,modularConstantAlgebraReturns=allresults,completeQSplits=splitrecords,actualInverseCount=inverse_count,allHighQQFibersExcludedByFiniteConstantAlgebraGauss=passed,multiplicitiesRetainedByFiniteArtinianNakayama=True,noModularDOnlyMembershipLiftUsed=True,allLowNormQBranchesStillRequireQQReturn=True,noMultivariateGcdOrSamplingEmptinessClaim=True,wholeG36Excluded=False,claimExcluded=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
