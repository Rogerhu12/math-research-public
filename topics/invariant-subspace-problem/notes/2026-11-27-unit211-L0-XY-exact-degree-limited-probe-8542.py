from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx,nmod_mpoly_ctx,nmod_poly,fmpq_poly
import json,time,hashlib,signal,resource
start=time.perf_counter();signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(6*1024**3,6*1024**3))
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

def coefs(pp):
 out=[]
 for j in range(int(pp.degrees()[2]),-1,-1):
  dd={int(m[1]):a for m,a in pp.to_dict().items() if int(m[2])==j}
  out.append(fmpq_poly([dd.get(i,fmpq(0)) for i in range(max(dd,default=-1)+1)]))
 return out
xp,yp=map(coefs,pol);zero=fmpq_poly([])
M=[[zero]*i+xp+[zero]*(dy-1-i) for i in range(dy)]+[[zero]*i+yp+[zero]*(dx-1-i) for i in range(dx)]
shifts=v[1:]
def lead(row):
 choices=[(pp.degree()+shifts[j],j) for j,pp in enumerate(row) if pp]
 assert choices
 dd,j=max(choices)
 return dd,j,row[j].leading_coefficient()
leads=[lead(row) for row in M];steps=0
while True:
 pivots={};collision=None
 for i,(di,pi,ci) in enumerate(leads):
  if pi in pivots:collision=(pivots[pi],i);break
  pivots[pi]=i
 if collision is None:break
 a,b=collision
 if leads[a][0]<leads[b][0]:a,b=b,a
 da,pa,ca=leads[a];db,pb,cb=leads[b];assert pa==pb and da>=db
 power=da-db;factor=fmpq_poly([0]*power+[ca/cb])
 row=[aa-factor*bb for aa,bb in zip(M[a],M[b])]
 old=leads[a];new=lead(row)
 assert new[:2]<old[:2]
 scalar=new[2];row=[vv/scalar for vv in row];new=lead(row)
 M[a]=row;leads[a]=new;steps+=1
 if steps%100==0:say(stage='new_exact_shifted_row_reduction',steps=steps,currentUpperDegree=sum(x[0] for x in leads)-sum(shifts),maxRowDegree=max(x[0] for x in leads))
assert sorted(x[1] for x in leads)==list(range(n))
actual=sum(x[0] for x in leads)-sum(shifts)
say(stage='new_exact_Sylvester_degree_certificate',actualDegree=actual,steps=steps,distinctLeadingPositions=True,leadingDegrees=[x[0] for x in leads],columnShifts=shifts,claimExcluded=False)
signal.alarm(0)
