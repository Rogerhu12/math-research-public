from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx,nmod_mpoly_ctx,nmod_poly
import json,time,hashlib,signal,resource
start=time.perf_counter();signal.alarm(90);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
root=Path('/workspace/scratch/8542378f2b73');ctx=fmpq_mpoly_ctx.get(('rho','lam','w'),'lex');mc=nmod_mpoly_ctx.get(('rho','lam','w'),1031,'lex')
def say(**kw):print(json.dumps(dict(seconds=time.perf_counter()-start,**kw)),flush=True)
pol=[]
for name,sha in [('P1_N1','519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68'),('P1_EBe','c696ee10ac72763cbc2d9e01cd84cdda6bfd5116faa3262ddbf6f96490c54d33')]:
 pp=ctx.from_dict({tuple(m):fmpq(a) for m,a in json.loads((root/('L0_XY_'+name+'.json')).read_text())})
 assert hashlib.sha256(str(pp).encode()).hexdigest()==sha
 pol.append(pp)
x,y=pol;dx=int(x.degrees()[2]);dy=int(y.degrees()[2]);n=dx+dy
xd=[max((int(m[1]) for m in x.to_dict() if int(m[2])==j),default=-100000) for j in range(dx,-1,-1)]
yd=[max((int(m[1]) for m in y.to_dict() if int(m[2])==j),default=-100000) for j in range(dy,-1,-1)]
rows=[[-100000]*i+xd+[-100000]*(dy-1-i) for i in range(dy)]+[[-100000]*i+yd+[-100000]*(dx-1-i) for i in range(dx)]
assert len(rows)==n and all(len(row)==n for row in rows)
a=[[-z for z in row] for row in rows];u=[0]*(n+1);v=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
for i in range(1,n+1):
 p[0]=i;j0=0;minv=[10**9]*(n+1);used=[False]*(n+1)
 while True:
  used[j0]=True;i0=p[j0];delta=10**9;j1=0
  for j in range(1,n+1):
   if not used[j]:
    cur=a[i0-1][j-1]-u[i0]-v[j]
    if cur<minv[j]:minv[j]=cur;way[j]=j0
    if minv[j]<delta:delta=minv[j];j1=j
  for j in range(n+1):
   if used[j]:u[p[j]]+=delta;v[j]-=delta
   else:minv[j]-=delta
  j0=j1
  if p[j0]==0:break
 while True:
  j1=way[j0];p[j0]=p[j1];j0=j1
  if j0==0:break
assert sorted(p[1:])==list(range(1,n+1))
val=sum(a[p[j]-1][j-1] for j in range(1,n+1));assert val==sum(u[1:])+sum(v[1:])
assert all(a[i-1][j-1]>=u[i]+v[j] for i in range(1,n+1) for j in range(1,n+1))
bound=-val
say(stage='actual_Sylvester_assignment_dual_degree_bound',matrixSize=n,lambdaDegreeBound=bound,ordinaryBidegreeBound=int(x.degrees()[1])*dy+int(y.degrees()[1])*dx,dualVerified=True)
def modrat(a):
 d=int(a.denominator)%1031;assert d;return int(a.numerator)%1031*pow(d,-1,1031)%1031
def modp(pp):return mc.from_dict({tuple(map(int,m)):modrat(a) for m,a in pp.to_dict().items()})
xm,ym=map(modp,pol);assert int(xm.degrees()[2])==dx and int(ym.degrees()[2])==dy
say(stage='new_modular_complete_resultant_begin',originalWDegrees=[dx,dy])
r=xm.resultant(ym,'w');assert r
cs=[0]*(int(r.degrees()[1])+1)
for m,a in r.to_dict().items():assert int(m[0])==int(m[2])==0;cs[int(m[1])]=int(a)
rr=nmod_poly(cs,1031);say(stage='new_modular_complete_resultant_return',actualDegree=rr.degree(),equalsProvedUpperBound=rr.degree()==bound,coefficientSha256=hashlib.sha256(str(rr).encode()).hexdigest(),claimExcluded=False)
(root/'L0_XY_modular_complete_resultant_1031.json').write_text(json.dumps([int(a) for a in rr]))
signal.alarm(0)
