#!/usr/bin/env python3
"""New W original three quadratic rows: low two-column cofactor relations.
Reuse only the frozen monic-input construction, not its previous row/matrix gate.
Return a same-point affine (F,S) row, a pure S quadratic, and all three
F-eliminating pair cubics with complete original traces and paid denominators.
No new leading factor is inverted.  180 seconds / 4 GiB.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-global-monic-T4-F2-original-eight-column-return-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='af928bbd7240d5235feb3188e65fc8ee5c92aaf8866433a077f1ab96b7507913'
marker=b"say(stage='new_W_actual_monic_T4_F2_same_original_input',"
assert raw.count(marker)==1
prefix=raw.split(marker)[0];ns={'__file__':str(dep),'__name__':'__new_original_low_cofactor_input__'}
log=io.StringIO()
with contextlib.redirect_stdout(log):exec(compile(prefix,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,F,S,qF,hF=[ns[n] for n in ['C','P','F','S','qF','hF']]
ppaid,profile,original=[ns[n] for n in ['ppaid','profile','original']]
ctx,zero,one=[ns[n] for n in ['ctx','zero','one']]
def redF(pp):
 orig=P(pp);rr=P(pp);tr=P()
 while any(mm[0]>=2 for mm in rr.t):
  mm=max((mm for mm in rr.t if mm[0]>=2),key=lambda a:(a[0],a[1]))
  term=P.monomial((mm[0]-2,mm[1]),rr.t[mm]);rr=rr-term*qF;tr=tr+term
 assert rr+tr*qF==orig
 for x in [rr,tr]:ppaid(x)
 return rr,tr
labels=['E1','EBe','N1'];rs=[];ts=[]
for name in labels:
 r,t=redF(original[name])
 assert all(mm in [(0,0),(0,1),(0,2),(1,0),(1,1)] for mm in r.t)
 rs.append(r);ts.append(t)
def column(mm):return [r.t.get(mm,C()) for r in rs]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def digest(parts):
 h=hashlib.sha256();count=0
 for po in parts:
  bb=json.dumps(po.data(),separators=(',',':')).encode();h.update(bb);h.update(b'\n');count+=len(bb)+1
 return dict(bytes=count,sha256=h.hexdigest())
def factor_profile(cf):
 cf=C(cf);ppaid(P(cf))
 def prof(pol):
  dd=[[list(map(int,mm)),str(c)] for mm,c in sorted(pol.to_dict().items())]
  bb=json.dumps(dd,separators=(',',':')).encode()
  r=dict(degrees=list(map(int,pol.degrees())),terms=len(dd),bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
  if len(bb)<=8192:r['coefficients']=dd
  return r
 cn,fn=cf.n.factor() if cf.n else (0,[])
 cd,fd=cf.d.factor()
 pn=ctx.constant(cn);pd=ctx.constant(cd)
 for f,m in fn:pn*=f**m
 for f,m in fd:pd*=f**m
 assert pn==cf.n and pd==cf.d
 return dict(numeratorContent=str(cn),numeratorFactors=[dict(multiplicity=int(m),factor=prof(f)) for f,m in fn],
 denominatorContent=str(cd),denominatorFactors=[dict(multiplicity=int(m),factor=prof(f)) for f,m in fd])
def scalar_combo(name,a,b,allowed):
 ws=cross(column(a),column(b))
 rr=sum((rs[i].scale(ws[i]) for i in range(3)),P())
 tr=sum((ts[i].scale(ws[i]) for i in range(3)),P())
 raw=sum((original[labels[i]].scale(ws[i]) for i in range(3)),P())
 assert rr+tr*qF==raw
 assert all(mm in allowed for mm in rr.t)
 for pp in [rr,tr]+[P(v) for v in ws]:ppaid(pp)
 data=dict(stage='W_new_original_three_row_low_cofactor',name=name,
 columnsCancelled=[list(a),list(b)],completeOriginalCombinationActuallyVerified=True,
 relation=profile(rr),zeroRelation=not bool(rr),noNewHeadInverse=True,
 coefficientFactorizations=[dict(monomial=list(mm),value=factor_profile(cf)) for mm,cf in sorted(rr.t.items())],
 originalTrace=digest([rr,tr]+[P(v) for v in ws]))
 say(**data)
 return rr,ws,tr
lin,wlin,tlin=scalar_combo('same_point_affine_F_S',(1,1),(0,2),[(0,0),(0,1),(1,0)])
quad,wquad,tquad=scalar_combo('same_point_pure_S_quadratic',(1,0),(1,1),[(0,0),(0,1),(0,2)])
# Each actual F coefficient is a_i+b_i*S. Eliminate that same F,
# rather than treating F and F*S as independent values.
pair_records=[]
for i,j in [(0,1),(0,2),(1,2)]:
 ai=P(rs[i].t.get((1,0),C()))+S.scale(rs[i].t.get((1,1),C()))
 aj=P(rs[j].t.get((1,0),C()))+S.scale(rs[j].t.get((1,1),C()))
 rr=ai*rs[j]-aj*rs[i];tr=ai*ts[j]-aj*ts[i]
 assert rr+tr*qF==ai*original[labels[j]]-aj*original[labels[i]]
 assert all(mm[0]==0 and mm[1]<=3 for mm in rr.t)
 for pp in [ai,aj,rr,tr]:ppaid(pp)
 rec=dict(pair=[labels[i],labels[j]],relation=profile(rr),
 completeOriginalSameFTraceActuallyVerified=True,
 leadingS=max((mm[1] for mm in rr.t),default=-1),
 originalTrace=digest([rr,tr,ai,aj]))
 pair_records.append(rec);say(stage='W_new_original_same_F_pair_cubic',**rec)
say(stage='W_new_original_three_quadratic_low_cofactor_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 originalInputPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
 prefixLogSHA256=hashlib.sha256(log.getvalue().encode()).hexdigest(),
 independentScalarVariables=['e','k','lambda'],
 allTwoScalarCofactorAndThreeSameFPolynomialIdentitiesActuallyReturned=True,
 affineRelationNonzero=bool(lin),pureSQuadraticNonzero=bool(quad),
 noUnpaidFactorRemoved=True,allNewLeadingZeroFibersRetained=True,
 noParameterProjectionOrExclusion=True,wholeWExcluded=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
