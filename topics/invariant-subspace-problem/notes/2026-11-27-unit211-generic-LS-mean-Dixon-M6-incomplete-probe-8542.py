from pathlib import Path
import json,hashlib,signal,time,resource
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(150);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3));start=time.perf_counter()
def say(d):d['seconds']=time.perf_counter()-start;print(json.dumps(d),flush=True)
root=Path('/workspace/scratch/8542378f2b73/r150-scratch');data=json.loads((root/'generic_three_quad_Dixon_rows.json').read_text())[0]
ctx=fmpq_mpoly_ctx.get(('l','u','Q','lam'),'lex');l,u,Q,lam=ctx.gens();one=ctx.constant(1);zero=ctx.constant(0)
mons=[(2,0),(1,1),(0,2),(1,0),(0,1),(0,0)]
M=[]
for row in data['rows']:
 M.append([ctx.from_dict({tuple(m[:4]):fmpq(a) for m,a in row['poly'] if tuple(m[4:6])==mo}) for mo in mons])
AA=[list(r) for r in M];prev=one;steps=[]
for z in range(5):
 swap=z
 if not AA[z][z]:
  swap=next(i for i in range(z+1,6) if AA[i][z]);AA[z],AA[swap]=AA[swap],AA[z]
 pivot=AA[z][z];assert pivot;lower=[AA[i][z] for i in range(z+1,6)];steps.append((pivot,lower,swap))
 for i in range(z+1,6):
  for j in range(z+1,6):
   num=AA[i][j]*pivot-AA[i][z]*AA[z][j];rr=num/prev;assert rr*prev==num;AA[i][j]=rr
  AA[i][z]=zero
 prev=pivot;say({'stage':'generic_mean_Dixon_M6_fraction_free_step','index':z,'swap':swap,'degrees':list(map(int,pivot.degrees())),'terms':len(pivot.to_dict()),'claimExcluded':False})
det=AA[-1][-1];assert det
cf=[zero]*6;cf[-1]=steps[-1][0]
for z in range(4,-1,-1):
 pivot,lower,swap=steps[z];num=-sum((cf[i]*lower[i-z-1] for i in range(z+1,6)),zero);cf[z]=num/pivot;assert cf[z]*pivot==num
 if swap!=z:cf[z],cf[swap]=cf[swap],cf[z]
for j in range(6):assert sum((cf[i]*M[i][j] for i in range(6)),zero)==(det if j==5 else zero)
say({'stage':'generic_mean_Dixon_M6_constant_column','degrees':list(map(int,det.degrees())),'terms':len(det.to_dict()),'allSixIdentitiesMultipliedBack':True,'claimExcluded':False})
scalar,factors=det.factor();prod=ctx.constant(scalar);out=[]
for ff,n in factors:
 prod*=ff**n;out.append({'multiplicity':int(n),'degrees':list(map(int,ff.degrees())),'terms':len(ff.to_dict()),'poly':[[list(map(int,m)),str(a)] for m,a in ff.to_dict().items()],'sha256':hashlib.sha256(str(sorted(ff.to_dict().items())).encode()).hexdigest()})
assert prod==det;say({'stage':'generic_mean_Dixon_M6_complete_factorization','factors':[{k:v for k,v in r.items() if k!='poly'} for r in out],'claimExcluded':False})
(root/'generic_mean_Dixon_M6_factors.json').write_text(json.dumps(out));signal.alarm(0)
