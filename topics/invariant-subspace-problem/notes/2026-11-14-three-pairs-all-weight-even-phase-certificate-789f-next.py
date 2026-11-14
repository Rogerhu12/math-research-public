"""Three spin-one groups: exact full 3D phase defect, no numerical scan."""
import argparse, hashlib, json, resource, time
from itertools import product
from pathlib import Path
from flint import fmpz_mpoly_ctx
resource.setrlimit(resource.RLIMIT_CPU,(55,60))
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
ctx=fmpz_mpoly_ctx.get(('a','b','c'))
a,b,c=ctx.gens(); z=(a,b,c); one=ctx.constant(1); zero=ctx.constant(0)
start=time.monotonic()
def emit(**d): print(json.dumps(d,sort_keys=True),flush=True)
def tr(A):return [list(r) for r in zip(*A)]
def add(A,B,scale=1):return [[x+scale*y for x,y in zip(r,s)] for r,s in zip(A,B)]
def mul(*As):
 A=As[0]
 for B in As[1:]:
  A=[[sum((A[i][k]*B[k][j] for k in range(len(B))),zero) for j in range(len(B[0]))] for i in range(len(A))]
 return A
def scale(A,f):return [[f*x for x in r] for r in A]
def det(A):
 return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
# Cyclic 3x3 adjugate has no extra parity signs.
def adj(A):
 return [[A[(j+1)%3][(i+1)%3]*A[(j+2)%3][(i+2)%3]-A[(j+1)%3][(i+2)%3]*A[(j+2)%3][(i+1)%3] for j in range(3)] for i in range(3)]
def div(p,q):
 v,r=divmod(p,q);assert not r;return v
def prof(p):return dict(degree=int(p.total_degree()) if p else -1,terms=len(p),negative=sum(v<0 for v in p.coeffs()),positive=sum(v>0 for v in p.coeffs()))
Y=[(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]
V=[[1,0,0],[0,0,1],[1,1,1],[0,1,0],[-2,-1,0],[0,-1,-2]]
Cstates=[(2,1,0),(2,0,1),(1,2,0),(0,2,1),(1,0,2),(0,1,2),(1,1,1)]
u=[1,-1,-1,1,1,-1,0]
E=[[0]*3 for _ in Cstates]
for state,row in zip(Y,V):
 for i in range(3):
  if state[i]<2:
   new=list(state);new[i]+=1;r=Cstates.index(tuple(new))
   for j in range(3):E[r][j]+=(2-state[i])*row[j]
def mon(state):return a**state[0]*b**state[1]*c**state[2]
def count(state):return 2**sum(k==1 for k in state)
pi=a*a*b*b*c*c
H=[[zero]*3 for _ in range(3)];L=[[zero]*3 for _ in range(3)]
Q=[[zero]*3 for _ in range(3)];cross=[[zero] for _ in range(3)];M=zero
for state,row in zip(Y,V):
 m=mon(state);coef=8//count(state)
 for i in range(3):
  for j in range(3):
   H[i][j]+=coef*div(pi,m)*row[i]*row[j];L[i][j]+=coef*m*row[i]*row[j]
for state,row,ui in zip(Cstates,E,u):
 m=mon(state);coef=8//count(state)
 M+=coef*m*ui*ui
 for i in range(3):
  cross[i][0]+=coef*m*row[i]*ui
  for j in range(3):Q[i][j]+=coef*m*row[i]*row[j]
CC=mul(cross,tr(cross));G=add(scale(Q,M),CC,-1)
dH=det(H);aH=adj(H)
assert mul(H,aH)==[[dH if i==j else zero for j in range(3)] for i in range(3)]
Tnum=add(scale(Q,M),CC)
R=add(scale(L,8*M*M*dH),mul(G,aH,Tnum),-1)
D=add(scale(mul(G,aH,L,aH,G),4*M*M*dH),mul(R,aH,tr(R)),-1)
assert D==tr(D)
gcd=zero
for row in D:
 for x in row:gcd=gcd.gcd(x)
emit(stage='constructed',seconds=time.monotonic()-start,entry=prof(D[0][0]),gcd=str(gcd))
D=[[div(x,gcd) for x in row] for row in D]
mins=[D[0][0],D[0][0]*D[1][1]-D[0][1]**2,det(D)]
emit(stage='reduced',entries=[prof(D[i][i]) for i in range(3)],minors=[prof(x) for x in mins],seconds=time.monotonic()-start)
ordered=(one,1+b,1+b+c)
receipt={'model':'three spin-one groups','gcd':str(gcd),'source_basis':['(x-z)^2','(x-z)(y-z)','(y-z)^2'],'minors':[]}
for i,p in enumerate(mins,1):
 sub=p.compose(*ordered)
 coefficients=[[list(map(int,exponent)),str(coefficient)] for exponent,coefficient in sorted(sub.to_dict().items())]
 entry={'index':i,'original':prof(p),'ordered':prof(sub),'sha256':hashlib.sha256(json.dumps(coefficients,separators=(',',':')).encode()).hexdigest(),'coefficients':coefficients}
 assert entry['ordered']['negative']==0 and entry['ordered']['positive']>0
 receipt['minors'].append(entry);emit(stage='ordered',index=i,profile=entry['ordered'],sha256=entry['sha256'],seconds=time.monotonic()-start)
receipt['source_matrix']=V
receipt['raising_matrix']=E
receipt['hard_source']=u
receipt['ordered_substitution']=['1','1+x','1+x+y']
receipt['certificate_passed']=True
receipt['elapsed_seconds']=time.monotonic()-start
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
args=parser.parse_args()
args.output.write_text(json.dumps(receipt,ensure_ascii=False,separators=(',',':'))+'\n')
emit(stage='complete',seconds=time.monotonic()-start)

