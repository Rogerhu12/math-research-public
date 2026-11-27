from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx,fmpq_poly
import hashlib,json,signal,time,resource
start=time.perf_counter();root=Path('/workspace/scratch/8542378f2b73');ctx=fmpq_mpoly_ctx.get(('rho','lam','w'),'lex')
def say(**kw):print(json.dumps(dict(seconds=time.perf_counter()-start,**kw)),flush=True)
def alarm(s,f):say(stage='new_lambda_projection_timeout_unknown',claimExcluded=False);raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm);signal.alarm(150);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
pol=[]
for name,field,sha in [('L0_original_eight_by_eight_curve.json','curve','6057a487720992327d9e065ec6b7ef5e54896637f1c756a28391fd734737b50c'),('L0_XY_P1_N1.json',None,'519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68')]:
 data=json.loads((root/name).read_text());data=data[field] if field else data
 pp=ctx.from_dict({tuple(m):fmpq(a) for m,a in data});assert hashlib.sha256(str(pp).encode()).hexdigest()==sha;pol.append(pp)
say(stage='BEGIN_new_73_by_73_QQ_lambda_projection',matrixSize=73,degree3352PreviouslyIndependentlyProved=True,distinctFromFrozen105By105WProjection=True)
full=pol[0].resultant(pol[1],'lam');assert full and int(full.degrees()[2])==3352
cs=[fmpq(0)]*3353
for m,a in full.to_dict().items():assert int(m[0])==int(m[1])==0;cs[int(m[2])]=a
R=fmpq_poly(cs);out=root/'L0_CX_complete_lambda_QQ_resultant.json';out.write_text(json.dumps([str(a) for a in R]))
say(stage='complete_actual_new_lambda_QQ_resultant',degree=R.degree(),sha256=hashlib.sha256(str(R).encode()).hexdigest(),cacheBytes=out.stat().st_size,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,claimExcluded=False)
signal.alarm(0)
