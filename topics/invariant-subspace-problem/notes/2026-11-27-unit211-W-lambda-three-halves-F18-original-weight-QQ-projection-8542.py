#!/usr/bin/env python3
"""New whole lambda=3/2 finite QQ projection from F18 and original Gram cofactors.
Regenerate only the necessary polynomial inputs, without replaying previous
adjugate/hash gates; the new computation is exact resultant_e and QQ k Bezout.
Every leading drop and original k fiber is retained. 180 seconds / 4 GiB.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-lambda-three-halves-global-original-ten-column-weight-cofactors-8542.py')
raw=dep.read_bytes();assert hashlib.sha256(raw).hexdigest()=='d8daeec98b4870b3672d7737afea8771bf5e48d747297859dbf9c3095b10810c'
ns={'__file__':str(dep),'__name__':'__regenerate_frozen_original_cofactor_inputs_for_new_QQ_projection__'}
log=io.StringIO()
with contextlib.redirect_stdout(log):exec(compile(raw,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
ctx,e,k,zero,one=[ns[n] for n in ['wctx','we','wk','wzero','wone']]
F18DATA=[[[0,0],"8120172544"],[[0,1],"46841987072"],[[0,2],"123677442048"],[[0,3],"197445812224"],[[0,4],"211612860416"],[[0,5],"159003967488"],[[0,6],"83818577920"],[[0,7],"28902883328"],[[0,8],"4312940544"],[[0,9],"-1567227904"],[[0,10],"-1245347840"],[[0,11],"-392392704"],[[0,12],"-59726848"],[[0,13],"802816"],[[0,14],"2118144"],[[0,15],"363776"],[[0,16],"21952"],[[1,0],"76034342912"],[[1,1],"463772581888"],[[1,2],"1303409328128"],[[1,3],"2237112778752"],[[1,4],"2617343737856"],[[1,5],"2201289424896"],[[1,6],"1361197465600"],[[1,7],"615723761664"],[[1,8],"193132183552"],[[1,9],"32847671296"],[[1,10],"-3743162368"],[[1,11],"-5003964416"],[[1,12],"-2138898432"],[[1,13],"-654010112"],[[1,14],"-156316416"],[[1,15],"-27430144"],[[1,16],"-3041472"],[[1,17],"-156016"],[[2,0],"158058151936"],[[2,1],"982515712000"],[[2,2],"2716053012480"],[[2,3],"4353666842624"],[[2,4],"4343944577024"],[[2,5],"2524377038848"],[[2,6],"356090892288"],[[2,7],"-812615970816"],[[2,8],"-883159367680"],[[2,9],"-504271169536"],[[2,10],"-184603704064"],[[2,11],"-40892785152"],[[2,12],"-2194067456"],[[2,13],"2287717312"],[[2,14],"1121707376"],[[2,15],"314095248"],[[2,16],"59288352"],[[2,17],"6941536"],[[2,18],"375879"],[[3,0],"-93314875392"],[[3,1],"-372445806592"],[[3,2],"-1011972308992"],[[3,3],"-2864343941120"],[[3,4],"-6547087949824"],[[3,5],"-10350529396736"],[[3,6],"-11251953827840"],[[3,7],"-8510543593472"],[[3,8],"-4391058892800"],[[3,9],"-1364537423872"],[[3,10],"-68992118272"],[[3,11],"175242767104"],[[3,12],"105086719232"],[[3,13],"34710928960"],[[3,14],"7438031936"],[[3,15],"921206624"],[[3,16],"-10618312"],[[3,17],"-31196640"],[[3,18],"-5980310"],[[3,19],"-418117"],[[4,0],"12230590464"],[[4,1],"279239983104"],[[4,2],"579597238272"],[[4,3],"-1218926870528"],[[4,4],"-6573260079104"],[[4,5],"-11719232192512"],[[4,6],"-11033632096256"],[[4,7],"-4840582156288"],[[4,8],"1187306763264"],[[4,9],"3300014989312"],[[4,10],"2422715147520"],[[4,11],"1007547342848"],[[4,12],"226416791168"],[[4,13],"-806810368"],[[4,14],"-20799219872"],[[4,15],"-8495450320"],[[4,16],"-2003876444"],[[4,17],"-295267920"],[[4,18],"-19732351"],[[4,19],"1174698"],[[4,20],"229957"],[[5,1],"-563865452544"],[[5,2],"-3275667537920"],[[5,3],"-8922772799488"],[[5,4],"-13684033716224"],[[5,5],"-10416311762944"],[[5,6],"1728850362368"],[[5,7],"13367210782720"],[[5,8],"15635576741888"],[[5,9],"9884731490304"],[[5,10],"3266677865472"],[[5,11],"-80310777600"],[[5,12],"-684037313024"],[[5,13],"-380651653888"],[[5,14],"-117916615808"],[[5,15],"-22065799088"],[[5,16],"-1798144672"],[[5,17],"302495008"],[[5,18],"132180348"],[[5,19],"20125467"],[[5,20],"925190"],[[5,21],"-60711"],[[6,1],"-133177540608"],[[6,2],"483523559424"],[[6,3],"4945210245120"],[[6,4],"15684766531584"],[[6,5],"29495115579392"],[[6,6],"37109187985408"],[[6,7],"31163796766720"],[[6,8],"15273586876416"],[[6,9],"864909177856"],[[6,10],"-4981263977728"],[[6,11],"-4167959581440"],[[6,12],"-1753761843072"],[[6,13],"-351510174784"],[[6,14],"35511688000"],[[6,15],"48264149936"],[[6,16],"16727029144"],[[6,17],"3487906704"],[[6,18],"470107709"],[[6,19],"28873824"],[[6,20],"-2628576"],[[6,21],"-458514"],[[6,22],"7056"],[[7,2],"226895069184"],[[7,3],"708549017600"],[[7,4],"-397171228672"],[[7,5],"-5608571600896"],[[7,6],"-14398780866560"],[[7,7],"-22457272434688"],[[7,8],"-24500173971456"],[[7,9],"-18787186332672"],[[7,10],"-9346721167360"],[[7,11],"-2016291215360"],[[7,12],"945329160576"],[[7,13],"1074107103552"],[[7,14],"498272380256"],[[7,15],"137539829424"],[[7,16],"22089900168"],[[7,17],"1248150160"],[[7,18],"-301745750"],[[7,19],"-101786343"],[[7,20],"-16163730"],[[7,21],"-870901"],[[7,22],"75096"],[[8,2],"-34527510528"],[[8,3],"35555115008"],[[8,4],"64054362112"],[[8,5],"-167059652608"],[[8,6],"8051884032"],[[8,7],"1185241251840"],[[8,8],"3133616099328"],[[8,9],"5135613313024"],[[8,10],"5952793696256"],[[8,11],"4828276484352"],[[8,12],"2636276177088"],[[8,13],"864633113984"],[[8,14],"74993803472"],[[8,15],"-78615624208"],[[8,16],"-44630432908"],[[8,17],"-12112562800"],[[8,18],"-1908052541"],[[8,19],"-173659510"],[[8,20],"-5917167"],[[8,21],"1673316"],[[8,22],"326649"],[[9,3],"184352243712"],[[9,4],"159073173504"],[[9,5],"-1262553923584"],[[9,6],"-4034386460672"],[[9,7],"-6594641772544"],[[9,8],"-7527832322048"],[[9,9],"-6502191554560"],[[9,10],"-4524848553984"],[[9,11],"-2905119890176"],[[9,12],"-1932557246976"],[[9,13],"-1226746163456"],[[9,14],"-632066880000"],[[9,15],"-237364338400"],[[9,16],"-58735192416"],[[9,17],"-7185961840"],[[9,18],"576942064"],[[9,19],"394683837"],[[9,20],"73478780"],[[9,21],"8879724"],[[9,22],"740826"],[[10,3],"-80564191232"],[[10,4],"-824344313856"],[[10,5],"-2476167135232"],[[10,6],"-3207049248768"],[[10,7],"-1219614212096"],[[10,8],"2306877767680"],[[10,9],"4816801157120"],[[10,10],"5062165185536"],[[10,11],"3603458195456"],[[10,12],"1842175611904"],[[10,13],"709779760384"],[[10,14],"238489388608"],[[10,15],"91505651840"],[[10,16],"41004080912"],[[10,17],"16308026624"],[[10,18],"4800484568"],[[10,19],"967746368"],[[10,20],"129754699"],[[10,21],"12564736"],[[10,22],"920473"],[[11,3],"-40282095616"],[[11,4],"80564191232"],[[11,5],"1342000070656"],[[11,6],"4673236893696"],[[11,7],"8580890034176"],[[11,8],"9980630532096"],[[11,9],"8099179442176"],[[11,10],"4861379985408"],[[11,11],"2184995779584"],[[11,12],"707554899968"],[[11,13],"161331483648"],[[11,14],"40799449216"],[[11,15],"24781042560"],[[11,16],"15597696608"],[[11,17],"6795767664"],[[11,18],"2027920504"],[[11,19],"409061796"],[[11,20],"54478930"],[[11,21],"5731066"],[[11,22],"591920"],[[12,4],"161128382464"],[[12,5],"362538860544"],[[12,6],"-334588018688"],[[12,7],"-2817216217088"],[[12,8],"-6200147443712"],[[12,9],"-8099308011520"],[[12,10],"-7343279747072"],[[12,11],"-5014117146624"],[[12,12],"-2710894899200"],[[12,13],"-1184101694976"],[[12,14],"-418473701824"],[[12,15],"-120147779776"],[[12,16],"-28570037392"],[[12,17],"-5829425664"],[[12,18],"-1052004788"],[[12,19],"-165305180"],[[12,20],"-21679271"],[[12,21],"-1552328"],[[12,22],"153664"],[[13,5],"-271904145408"],[[13,6],"-916417675264"],[[13,7],"-1290324410368"],[[13,8],"-722585780224"],[[13,9],"555716722688"],[[13,10],"1572671668224"],[[13,11],"1692466319360"],[[13,12],"1180425629696"],[[13,13],"609349935616"],[[13,14],"247974112768"],[[13,15],"81237636224"],[[13,16],"21244485760"],[[13,17],"4237083168"],[[13,18],"563572576"],[[13,19],"29647688"],[[13,20],"-5858072"],[[13,21],"-1451968"],[[14,6],"251763097600"],[[14,7],"931523461120"],[[14,8],"1625837273088"],[[14,9],"1815131652096"],[[14,10],"1450120101888"],[[14,11],"860878405632"],[[14,12],"391109784576"],[[14,13],"147275932672"],[[14,14],"51986807552"],[[14,15],"18292910080"],[[14,16],"6233209280"],[[14,17],"1880090688"],[[14,18],"440456976"],[[14,19],"73275168"],[[14,20],"7117840"],[[15,7],"-138469703680"],[[15,8],"-513596719104"],[[15,9],"-892008857600"],[[15,10],"-991233703936"],[[15,11],"-803846668288"],[[15,12],"-502286680064"],[[15,13],"-246249553920"],[[15,14],"-96425330688"],[[15,15],"-30869617664"],[[15,16],"-8061205504"],[[15,17],"-1641785088"],[[15,18],"-240838784"],[[15,19],"-19882240"],[[16,8],"45317357568"],[[16,9],"161128382464"],[[16,10],"260022468608"],[[16,11],"258257879040"],[[16,12],"181048557568"],[[16,13],"95892840448"],[[16,14],"38980354048"],[[16,15],"11979282432"],[[16,16],"2708057088"],[[16,17],"418944512"],[[16,18],"33743360"],[[17,9],"-8182300672"],[[17,10],"-27064532992"],[[17,11],"-39039336448"],[[17,12],"-32681033728"],[[17,13],"-17991909376"],[[17,14],"-6998147072"],[[17,15],"-1942614016"],[[17,16],"-348221440"],[[17,17],"-29503488"],[[18,10],"629407744"],[[18,11],"1888223232"],[[18,12],"2360279040"],[[18,13],"1573519360"],[[18,14],"590069760"],[[18,15],"118013952"],[[18,16],"9834496"]]
EXPECTED={"N1":"1df822932bb9b41b79e2a9fe8d757fc6b36b018a96dd23d8212f546644c1802d","NS":"3ab1d726c4cf8f8e00c09eabe8c15f3c2474abf2da8159a202fe01a4b48d9fdf","PS":"b651d55fb1846c78c6a6a107d25cb32d9b0f3cd7cd299af33a9d391ea4ec9115"}
F18=zero
for mm,cc in F18DATA:F18+=ctx.constant(fmpq(cc))*e**mm[0]*k**mm[1]
assert list(F18.degrees())==[18,22]
top=zero
for mm,cc in F18.to_dict().items():
 if mm[0]==18:top+=cc*k**int(mm[1])
assert top==9834496*k**10*(k+2)**6
def det_only(rows):
 aa=[r[:] for r in rows];n=len(aa);prev=one;sgn=1
 for j in range(n-1):
  h=next((i for i in range(j,n) if aa[i][j]),None)
  if h is None:return zero
  if h!=j:aa[h],aa[j]=aa[j],aa[h];sgn=-sgn
  pv=aa[j][j]
  for i in range(j+1,n):
   for c in range(j+1,n):
    num=pv*aa[i][c]-aa[i][j]*aa[j][c]
    nxt=num/prev;assert nxt*prev==num;aa[i][c]=nxt
   aa[i][j]=zero
  prev=pv
 return sgn*aa[-1][-1]
def norm_weight(p):
 rem=p
 for atom in ns['unitpolys']:
  while True:
   g=rem.gcd(atom)
   if g.total_degree()==0:break
   nxt=rem/g;assert nxt*g==rem;rem=nxt
 return rem/rem.coefficient(0)
def univar(p):
 dd={}
 for mm,c0 in p.to_dict().items():
  assert mm[0]==0
  dd[int(mm[1])]=c0
 return fmpq_poly([dd.get(i,0) for i in range(max(dd,default=-1)+1)])
ku=fmpq_poly([0,1]);paidK=[ku,ku+1,ku+2,ku+4]
def strip_k(p):
 q=p;removed=fmpq_poly([1])
 for atom in paidK:
  while True:
   g=q.gcd(atom)
   if g.degree()<=0:break
   nq,rr=divmod(q,g);assert not rr and nq*g==q;q=nq;removed*=g
 lc=q[q.degree()];q=q/lc;removed*=lc
 assert removed*q==p
 return q
def pprofile(p):
 hh=hashlib.sha256();size=0;full=[]
 for c0 in p:
  s=str(c0);full.append(s);bb=(s+'\n').encode();hh.update(bb);size+=len(bb)
 rec=dict(degree=int(p.degree()),canonicalEncoding='coefficient strings constant first, each followed by newline',bytes=size,sha256=hh.hexdigest())
 js=json.dumps(full,separators=(',',':')).encode()
 if len(js)<=8192:rec['coefficients']=full
 mod=[]
 for c0 in p:
  num_s,sep,den_s=str(c0).partition('/');num=int(num_s);den=int(den_s) if sep else 1
  if den%1009==0:
   rec['allCoefficientsIntegralAt1009']=False;break
  mod.append((num%1009)*pow(den%1009,-1,1009)%1009)
 else:
  rec['allCoefficientsIntegralAt1009']=True
  rec['degreePreservedAt1009']=bool(mod) and mod[-1]!=0
  mb=json.dumps(mod,separators=(',',':')).encode()
  rec['mod1009']={'degree':len(mod)-1,'bytes':len(mb),'sha256':hashlib.sha256(mb).hexdigest()}
  if len(mb)<=8192:rec['mod1009']['coefficients']=mod
 return rec
cover=None;completed=[]
for name in EXPECTED:
 begin=time.perf_counter()
 rows=ns['base']+[ns['vector'](ns['polys'][name])]
 det=det_only(rows);assert det
 curve=norm_weight(det);actual=ns['prof'](curve)['sha256']
 assert actual==EXPECTED[name],'frozen necessary curve mismatch'
 say(stage='W_lambda_three_halves_new_QQ_projection_input_ready',name=name,
     actualOriginalNecessaryPolynomialSHA256=actual,
     actualDegreeE=int(curve.degrees()[0]),F18DegreeE=18,
     F18LeadingOnlyPaidKAndKplus2=True,noNewLeadingInverse=True)
 result=F18.resultant(curve,'e')
 if not result:
  say(stage='W_lambda_three_halves_new_QQ_projection_zero_resultant',name=name,
      noExclusionClaim=True,inputSeconds=time.perf_counter()-begin)
  completed.append({'name':name,'zeroProjection':True});continue
 rawK=univar(result);assert rawK
 say(stage='W_lambda_three_halves_exact_QQ_resultant_returned',name=name,QQDegree=int(rawK.degree()),allOtherVariablesActuallyAbsent=True,projectionSeconds=time.perf_counter()-begin)
 nextcover=strip_k(rawK)
 say(stage='W_lambda_three_halves_new_original_QQ_projection_complete',name=name,
     fullFixedOriginalResultant=True,rawQQProjection=pprofile(rawK),
     strippedOnlyPaidKFactors=pprofile(nextcover),projectionSeconds=time.perf_counter()-begin)
 if cover is None:
  cover=nextcover;bezout=None
 else:
  previous=cover;gg,ss,tt=previous.xgcd(nextcover)
  assert ss*previous+tt*nextcover==gg
  lc=gg[gg.degree()];gg=gg/lc;ss=ss/lc;tt=tt/lc
  assert ss*previous+tt*nextcover==gg
  cover=gg
  say(stage='W_lambda_three_halves_QQ_Bezout_both_products_returned',name=name,commonDegree=int(cover.degree()),wholeLambdaFiberExcluded=cover.degree()==0)
  bezout=dict(left=pprofile(ss),right=pprofile(tt),bothQQProductsActuallyReturned=True)
 completed.append({'name':name,'zeroProjection':False,'coverDegree':int(cover.degree())})
 say(stage='W_lambda_three_halves_new_full_QQ_cover_intersection',
     name=name,commonNecessaryCover=pprofile(cover),actualQQBezout=bezout,
     wholeLambdaFiberExcluded=cover.degree()==0)
 if cover.degree()==0:break
factor_records=None
if cover is not None and 0<cover.degree()<=128:
 content,factors=cover.factor();product=fmpq_poly([content]);factor_records=[]
 for f,m in factors:product*=f**m;factor_records.append(dict(multiplicity=int(m),factor=pprofile(f)))
 assert product==cover
say(stage='W_lambda_three_halves_F18_original_QQ_projection_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 completed=completed,finalNecessaryCover=None if cover is None else pprofile(cover),
 completeLowDegreeQQFactorization=factor_records,
 wholeLambdaFiberExcluded=cover is not None and cover.degree()==0,
 noA143OrAhatInverse=True,noPhysicalDOrNormInverse=True,
 allLeadingZeroFibersRetained=True,largeCoefficientCachesWritten=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
