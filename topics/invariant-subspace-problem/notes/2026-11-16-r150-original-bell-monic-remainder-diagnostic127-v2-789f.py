#!/usr/bin/env python3
"""Read-only original fifty-column Bell-monic diagnostic, not a unit search.
Author: ChatGPT (AI), literature_audit / Astra-ISP-789f. 2026-11-16 UTC.
Every remainder and source is recomputed over the actual F127,d100 model.
Parents are read only; mathematical statistics remain temporary.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,resource,signal,time
from pathlib import Path
FMT='r150-original-bell-monic-remainder-diagnostic127-v2'
V2SHA='ee9bdabfdd325150b622e77a91d20eb814c642c8cb66bbf4734106466af630e3'
V2BIND='8e701750318d6bed82bd5e202266e025a60da1d23397f2c740badae301ad0bff'
MANIFEST={'bytes':16438,'sha256':'b0d7349d9a1b27f91f0b4ac12483a065ae8063a5f304d7c3f8ff6861b2d96bf9'}
RECEIPT={'bytes':18411,'sha256':'16cc0dddd8680857c0dc9df1bfe2702cd5d9687653eacb0a4b51b14dc1783d38'}
MODEL_SHA='4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4'
P=127;WEIGHTS=(1,)*6+(2,)*11;GWEIGHTS=(4,)*11+(5,)*6+(3,)
class Budget(Exception):pass
def need(a,s):
 if not a:raise ValueError(s)
def canon(a):return json.dumps(a,sort_keys=True,separators=(',',':')).encode('ascii')
def sha(a):return hashlib.sha256(a).hexdigest()
def ident(p):
 b=p.read_bytes();return {'path':p.name,'bytes':len(b),'sha256':sha(b)}
def exact(p,d):
 q=ident(p);need(q['bytes']==d['bytes'] and q['sha256']==d['sha256'],'exact whole '+p.name);return q
def module(p,h,name):
 need(ident(p)['sha256']==h,'exact source '+name)
 sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def weight(f):return int(max((sum(a*b for a,b in zip(e,WEIGHTS)) for e in f.to_dict()),default=-1))
def source_weight(v):return max((weight(f)+w for f,w in zip(v,GWEIGHTS) if f!=0),default=-1)
def main():
 ap=argparse.ArgumentParser()
 for n in ('source-v2','out-v2','model-source','model-out','out'):ap.add_argument('--'+n,type=Path,required=True)
 ap.add_argument('--seconds',type=float,default=180);ap.add_argument('--memory-mib',type=int,default=1024)
 a=ap.parse_args();need(0<a.seconds<=180 and 256<=a.memory_mib<=1024,'explicit small diagnostic bounds')
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2);beg=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 own=ident(Path(__file__));semantic={'format':FMT,'source':own,'v2SourceSHA256':V2SHA,'v2Binding':V2BIND,'v2Manifest':MANIFEST,'v2Receipt':RECEIPT,'modelSourceSHA256':MODEL_SHA,'prime':127,'coefficientRoot':100,'variableOrder':['y%d'%i for i in range(6)]+['w%d'%i for i in range(6)]+['u%d'%i for i in range(5)],'monomialOrdering':'lex','singleDivisor':'sum_i y_i*w_i - 1','leadingMonomial':'y0*w0','parameterInversions':False,'unitSearch':False}
 binding=sha(canon(semantic));rec={'format':FMT,'binding':binding,'source':own,'status':'running','parameters':{'seconds':a.seconds,'memoryMiB':a.memory_mib,'completedColumns':[],'mathematicalUnitConclusion':False,'characteristicZeroConclusion':False}}
 def flush():
  rec['elapsedSeconds']=time.monotonic()-beg;rec['parameters']['peakRssKiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  p=a.out/'bell-monic-diagnostic-receipt.json';q=p.with_suffix('.tmp');q.write_bytes(canon(rec));q.replace(p)
 def alarm(*unused):raise Budget('original Bell remainder diagnostic budget')
 def tick():
  if time.monotonic()-beg>=a.seconds-5:raise Budget('original Bell remainder diagnostic budget')
 signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,max(.1,a.seconds-3));code=1
 try:
  u=module(a.source_v2,V2SHA,'paid_unexpanded_local_source');m=module(a.model_source,MODEL_SHA,'paid_original_fifty_model')
  mp=a.out_v2/'rank-four-local-source-manifest.json';rp=a.out_v2/'rank-four-local-source-receipt.json';exact(mp,MANIFEST);exact(rp,RECEIPT)
  cm=json.loads(mp.read_bytes());cr=json.loads(rp.read_bytes())
  need(cm['binding']==cr['binding']==V2BIND and cr['status']=='completed-prefix' and cr['parameters']['all4Original18BellRemovalProductsVerified'],'actual complete original parent input')
  inp=cm['inputs'];pmp=a.model_out/'original-parameter-module-manifest.json';exact(pmp,inp['modelManifest']);pm=json.loads(pmp.read_bytes());need(pm['binding']==u.MODEL_BINDING,'original model binding')
  dd=pm['phases']['complete-original-ten-parameter-action127'];base=m.load_gz(a.model_out/dd['path'],dd,u.MODEL_BINDING)
  original=m.unpackvec(base['allOriginal18Generators']);bell=original[17]
  need(bell==sum((m.Y[i]*m.W[i] for i in range(6)),m.ZERO)-1,'literal original Bell divisor')
  need(all(all(sum(a*b for a,b in zip(e,WEIGHTS))==GWEIGHTS[i] for e in f.to_dict()) for i,f in enumerate(original[:17])),'complete original transformed generator weights in u5,w6,y6 order')
  lead=(1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0)
  need(max(bell.to_dict())==lead and int(bell.to_dict()[lead])==1,'same original monic leading term')
  idx=inp['retainedParentIndices'];ds=inp['retainedParentPhases'];need(len(idx)==len(ds)==50 and idx[:6]==list(range(100,106)) and idx[-10:]==list(range(106,116)),'all original mean and Bell source labels')
  means=[];meanSources=[];originalMeans=[];bellVectors=[];bellSources=[]
  totals={'originalTerms':0,'allCoordinateRemainderTerms':0,'normalizedCandidateTerms':0,'divisionQuotientTerms':0}
  per=rec['parameters']['completedColumns'];zeroNonBell=[]
  for j,(ix,d) in enumerate(zip(idx,ds)):
   tick();need(d==pm['seeds'][ix],'same literal seed descriptor');z=m.load_gz(a.model_out/d['path'],d,u.MODEL_BINDING)
   need(z['seedIndex']==ix and z['fullOriginal18ProductVerified'],'actual original full source column')
   V=m.unpackvec(z['vector']);S=m.unpackvec(z['original18Source']);need(len(V)==10 and len(S)==18 and m.dot(m.MON,V)==m.dot(original,S),'whole original product before division')
   Q=[];R=[]
   for i,f in enumerate(V):
    q,r=divmod(f,bell);need(f==bell*q+r,'every complete original coordinate division product')
    need(all(e[0]==0 or e[6]==0 for e in r.to_dict()),'complete monic leading-term remainder')
    need(all(not any(e[12:]) for e in q.to_dict()) and all(not any(e[12:]) for e in r.to_dict()),'all12 parameters and no hidden u dependence')
    Q.append(q);R.append(r)
   NS=S[:17]+[S[17]-m.dot(m.MON,Q)]
   need(m.dot(original,NS)==m.dot(m.MON,R),'every complete original18 remainder source product')
   oc=[len(f.to_dict()) for f in V];rc=[len(f.to_dict()) for f in R];qc=[len(f.to_dict()) for f in Q]
   candidate=V if ix>=106 else R;candidateSource=S if ix>=106 else NS
   if ix>=106:
    axis=ix-106;need(all(V[k]==(bell if k==axis else m.ZERO) for k in range(10)) and all(f==0 for f in R),'all ten original Bell columns reduce exactly to zero')
    bellVectors.append(V);bellSources.append(S)
   if 100<=ix<=105:
    need(all(R[k]==V[k] and Q[k]==0 for k in range(6,10)),'all24 mean quad coordinates unchanged')
    means.append(R);meanSources.append(NS);originalMeans.append(V)
   if ix<100 and all(f==0 for f in R):zeroNonBell.append(ix)
   item={'retainedPosition':j,'originalSeedIndex':ix,'originalCoordinateTerms':oc,'remainderCoordinateTerms':rc,'quotientCoordinateTerms':qc,
    'candidateCoordinateTerms':[len(f.to_dict()) for f in candidate],
    'originalSourceWeight':source_weight(S),'normalizedSourceWeight':source_weight(candidateSource),
    'originalSourceCoordinateWeights':[weight(f) for f in S],'normalizedSourceCoordinateWeights':[weight(f) for f in candidateSource],
    'all10DivisionProductsVerified':True,'all18OriginalRemainderProductVerified':True,
    'quotientLogicalSHA256':sha(canon(m.packvec(Q))),'remainderLogicalSHA256':sha(canon(m.packvec(R))),
    'normalizedSourceLogicalSHA256':sha(canon(m.packvec(candidateSource)))}
   per.append(item);totals['originalTerms']+=sum(oc);totals['allCoordinateRemainderTerms']+=sum(rc);totals['normalizedCandidateTerms']+=sum(item['candidateCoordinateTerms']);totals['divisionQuotientTerms']+=sum(qc)
   if len(per)%10==0:flush();print(canon({'phase':'complete-original-column-remainders','columns':len(per),'elapsedSeconds':time.monotonic()-beg}).decode(),flush=True)
  need(len(means)==len(meanSources)==6 and len(bellVectors)==len(bellSources)==10,'complete normalized means and original Bell columns')
  chartd=cm['phases']['complete-original-rank-four-unexpanded-input'];chart=u.load_gz(a.out_v2/chartd['path'],chartd,V2BIND);rows=chart['originalMeanRows']
  A=[[means[j][6+i] for j in rows] for i in range(4)];oldA=[[originalMeans[j][6+i] for j in rows] for i in range(4)]
  need(u.same(A,oldA),'same entire literal mean pivot after monic reduction');delta=u.det(A,m);adj=u.adj(A,m)
  need(delta==m.unpack(chart['delta']) and u.same(u.mm(A,adj,m),[[delta if i==j else m.ZERO for j in range(4)] for i in range(4)]),'same selected delta and exact adjugate')
  C=[[means[j][i] for j in rows] for i in range(6)];CA=u.mm(C,adj,m)
  for k in range(4):
   tick();co=[adj[l][k]*bell for l in range(4)];cb=[-CA[i][k] for i in range(6)]
   for i in range(10):need(sum((co[l]*means[j][i] for l,j in enumerate(rows)),m.ZERO)+sum((cb[j]*bellVectors[j][i] for j in range(6)),m.ZERO)==delta*bellVectors[6+k][i],'all40 normalized-mean Bell removal coordinates')
   sig=[sum((co[l]*meanSources[j][i] for l,j in enumerate(rows)),m.ZERO)+sum((cb[j]*bellSources[j][i] for j in range(6)),m.ZERO) for i in range(18)]
   need(m.dot(original,sig)==delta*m.dot(original,bellSources[6+k]),'all4 complete original18 normalized Bell removal products')
  rec['status']='completed-diagnostic';rec['parameters'].update(totals=totals,zeroNormalizedNonBellSeedIndices=zeroNonBell,
   all500CoordinateDivisionsVerified=True,all50Original18RemainderProductsVerified=True,all24MeanQuadCoordinatesUnchanged=True,
   all40NormalizedBellRemovalCoordinatesVerified=True,all4Original18NormalizedBellRemovalProductsVerified=True,
   chartIndex=chart['chartIndex'],originalMeanRows=rows,deltaLogicalSHA256=sha(canon(m.pack(delta))),
   sourceWeightDefinition='weights y=1,w=u=2; original transformed gradient weights (4^11,5^6) in u5,w6,y6 order, Bell upper weight3',
   originalInputIdentities={'parentManifest':ident(mp),'parentReceipt':ident(rp),'modelManifest':ident(pmp),'chartPhase':chartd},
   pendingCandidateScope='Diagnostic only. Any new normalized input must separately carry its literal remainder columns and complete original source recipes; current frozen v2 is unchanged.')
  code=0
 except Budget as e:rec['status']='budget-checkpoint';rec['parameters']['error']={'type':type(e).__name__,'message':str(e)};code=75
 except BaseException as e:rec['status']='failed';rec['parameters']['error']={'type':type(e).__name__,'message':str(e)};code=1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);flush();print(canon(rec).decode(),flush=True)
 return code
if __name__=='__main__':raise SystemExit(main())
