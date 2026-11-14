"""All 53 actual bad-height directions, spectra and kernels from R135."""
import json,gzip,hashlib,math,itertools
from pathlib import Path
from fractions import Fraction as Q
from sympy import Matrix, mobius, divisors
import p41_drinfeld_hecke as base
Ring=base.Ring; labels=base.labels; weights=base.weights
root=base.root
full=json.loads(gzip.decompress((root/'p41_full_chow_heegner_certificate.json.gz').read_bytes()))
qv=[Q(1,10),Q(3,10),Q(3,10),Q(3,10)];lengths=[Q(a,420) for a in weights]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def ma(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def ms(A,c):return [[x*c for x in a] for a in A]
def ev(coeff,A):
 n=len(A);B=[[0]*n for _ in range(n)];I=eye(n)
 for c in coeff:B=ma(mm(B,A),ms(I,c))
 return B
H4=ma(base.Hs[2],ms(base.Hs[3],-2))
Ht=[[H4[i+1][j+1]-H4[i+1][0] for j in range(3)] for i in range(3)]
ft=[int(x) for x in Matrix(Ht).charpoly().all_coeffs()]
assert ft==base.factors[1]
blocks=[]
for item in base.out['blocks']:
 R=Ring(item['inertia_order']);active=item['labels'];H=[[tuple(x) for x in row] for row in item['H']]
 d=R.d;ct=[sum(int(r*mobius(d//r)) for r in divisors(d) if k%r==0) for k in range(R.n)]
 fi=item['R89_matching_factors'];assert len(fi)==1
 blocks.append((R,active,H,ct,fi[0]))
def traceelt(a,ct):return sum(x*y for x,y in zip(a,ct))
def tau_for_block(M,active,ct):
 tau=[0]*4
 for j in active:tau[labels.index(j)]=traceelt(M[active.index(j)][active.index(j)],ct)
 return tau
def Qgraph(A):
 out=[]
 for j in range(4):
  v=[Q(int(i==j))-qv[i] for i in range(1,4)]
  w=[sum(a*b for a,b in zip(row,v)) for row in A]
  w0=-sum(w);fullw=[w0]+w
  out.append(lengths[j]*fullw[j]/2)
 return out
def beta_values(tau,qg):
 Xi=[weights[i]*tau[i]+840*qg[i] for i in range(4)]
 return [-Q(40,42)*(x-Xi[0]) for x in Xi]
rows=[]
for k,meta in enumerate(full['row_metadata']):
 tau=[0]*4
 for R,active,H,ct,fi in blocks:
  pair=full['fields'][fi]['directions'][k][0];den,coeff=pair
  M=R.evalmat(coeff,H)
  assert all(x%den==0 for row in M for a in row for x in a),('nonintegral Drinfeld',meta['n'],fi)
  M=[[tuple(x//den for x in a) for a in row] for row in M]
  F=R.ma(R.ms(M,meta['F_Tn_coefficient']),R.ms(R.ident(len(active)),meta['F_identity_coefficient']))
  tt=tau_for_block(F,active,ct);tau=[a+b for a,b in zip(tau,tt)]
 den,coeff=full['fields'][1]['directions'][k][0]
 M=ev(coeff,Ht);assert all(x%den==0 for row in M for x in row),('nonintegral toric',meta['n'])
 M=[[x//den for x in row] for row in M]
 F=ma(ms(M,meta['F_Tn_coefficient']),ms(eye(3),meta['F_identity_coefficient']))
 qg=Qgraph(F);bv=beta_values(tau,qg)
 assert all(x.denominator==1 for x in bv),('nonintegral bad height',meta['n'],bv)
 rows.append({'n':meta['n'],'a':meta['F_Tn_coefficient'],'b':meta['F_identity_coefficient'],'tau':tau,'Q':[str(x) for x in qg],'bad_values':[int(x) for x in bv]})
 if k%10==0:print('direction',k,meta['n'],'bad',bv,flush=True)
assert rows[0]['bad_values']==[0]*4
Bad=Matrix([[r['bad_values'][j] for r in rows] for j in range(1,4)])
_,pivots=Bad.rref();rank=len(pivots)
print('BAD RANK',rank,'basis directions',[rows[k]['n'] for k in pivots],flush=True)
spectra=[]
for R,active,H,ct,fi in blocks:
 deg=len(base.factors[fi])-1;M=R.ident(len(active));vals=[[] for _ in range(3)]
 for k in range(deg):
  bv=beta_values(tau_for_block(M,active,ct),[Q(0)]*4)
  for j in range(3):vals[j].append(bv[j+1])
  M=R.mm(M,H)
 spectra.append({'field_index':fi,'moments':vals})
M=eye(3);vals=[[] for _ in range(3)]
for k in range(3):
 bv=beta_values([0]*4,Qgraph(M))
 for j in range(3):vals[j].append(bv[j+1])
 M=mm(M,Ht)
spectra.append({'field_index':1,'moments':vals})
def power_traces(f,upto):
 n=len(f)-1;ts=[n]
 for k in range(1,upto+1):
  v=sum(f[i]*ts[k-i] for i in range(1,min(k-1,n)+1))
  if k<=n:v+=k*f[k]
  ts.append(-v)
 return ts
for sp in spectra:
 fi=sp['field_index'];f=base.factors[fi];n=len(f)-1;ts=power_traces(f,2*n-2)
 G=Matrix([[ts[i+j] for j in range(n)] for i in range(n)])
 cols=Matrix(n,3,lambda i,j:sp['moments'][j][i]);coef=G.inv()*cols
 assert G*coef==cols
 sp['beta_coefficients_ascending']=[[str(coef[i,j]) for i in range(n)] for j in range(3)]
 sp['moments']=[[str(x) for x in row] for row in sp['moments']]
 print('spectral beta field',fi,'degree',n,'complete',flush=True)
# Check every beta trace against the independent complete direction calculation.
for k,meta in enumerate(full['row_metadata']):
 vals=[Q(0)]*3
 for sp in spectra:
  fi=sp['field_index'];den,coeff=full['fields'][fi]['directions'][k][0]
  c=[Q(x*meta['F_Tn_coefficient'],den) for x in coeff[::-1]]
  c[0]+=meta['F_identity_coefficient']
  for j in range(3):vals[j]+=sum(x*Q(y) for x,y in zip(c,sp['moments'][j]))
 assert vals==[Q(x) for x in rows[k]['bad_values'][1:]],('spectral trace mismatch',meta['n'])
assert all(sum(Q(sp['moments'][j][0]) for sp in spectra)==0 for j in range(3))
tor=next(sp for sp in spectra if sp['field_index']==1)
assert [18*Q(v[0]) for v in tor['moments']]==[Q(240,7)]*3
out={'level':41,'component_labels':labels,'T2_Brandt':base.Hs[2],'T3_Brandt':base.Hs[3],'H_toric_cycle_matrix':Ht,'H_toric_factor':ft,'directions':rows,'bad_rank':rank,'rank_pivot_direction_indices':[rows[k]['n'] for k in pivots],'rank_minor':[[int(Bad[i,k]) for k in pivots] for i in range(3)],'rank_minor_determinant':int(Bad[:,list(pivots)].det()) if rank==3 else None,'beta_spectra':spectra,'principal_series_field_indices':[0,3,4,5],'R57_check':'18*Tr(beta_toric)=240/7 on all three nonzero labels','status':'Exact actual all-direction bad-height spectrum and kernels; geometric identification proved in R135. Auxiliary local heights remain to be computed.'}

# Exact determinantal divisors of the listed integer direction lattice.
bint=[[r['bad_values'][j] for r in rows] for j in range(1,4)]
div1=math.gcd(*(x for row in bint for x in row));div2=0;div3=0
for i,j in itertools.combinations(range(3),2):
 for u,v in itertools.combinations(range(53),2):
  div2=math.gcd(div2,bint[i][u]*bint[j][v]-bint[i][v]*bint[j][u])
for u,v,w in itertools.combinations(range(53),3):
 det=bint[0][u]*(bint[1][v]*bint[2][w]-bint[1][w]*bint[2][v])-bint[0][v]*(bint[1][u]*bint[2][w]-bint[1][w]*bint[2][u])+bint[0][w]*(bint[1][u]*bint[2][v]-bint[1][v]*bint[2][u])
 div3=math.gcd(div3,det)
assert (div1,div2,div3)==(20,2400,576000)
P=Bad[:,list(pivots)];coeff=P.inv()*Bad;kb=[]
for i,row in enumerate(rows):
 if i not in pivots:
  cs=[coeff[j,i] for j in range(3)];assert all(int(c.q)%47 for c in cs)
  assert P*Matrix(cs)==Bad[:,i]
  kb.append({'n':row['n'],'subtract_pivot_coefficients':[str(c) for c in cs]})
assert len(kb)==50
K=Matrix(53,3,lambda i,j:Q(full['xi_right_kernel'][j][1][i],full['xi_right_kernel'][j][0]))
T=Bad*K;assert T.rank()==2
c=T.nullspace()[0];v=K*c;den=math.lcm(*(int(a.q) for a in v))
w=[int(a*den) for a in v];common=math.gcd(*w);w=[a//common for a in w]
if next(a for a in w if a)<0:w=[-a for a in w]
assert Bad*Matrix(w)==Matrix.zeros(3,1) and math.gcd(*w)==1
minor=None
for ir in itertools.combinations(range(3),2):
 for jc in itertools.combinations(range(3),2):
  value=T.extract(ir,jc).det()
  if value and minor is None:minor={'rows':ir,'columns':jc,'determinant':str(value)}
assert minor
out.update(determinantal_divisors=[div1,div2,div3],smith_invariants=[div1,div2//div1,div3//div2],
 bad_kernel_50_basis=kb,bad_on_xi_kernel=[[str(x) for x in row] for row in T.tolist()],
 bad_on_xi_kernel_rank=2,bad_on_xi_kernel_nonzero_minor=minor,xi_kernel_combination=[str(a) for a in c],
 primitive_common_kernel_coefficients=w,
 source_sha256={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in ['p41_jacobi_cm_certificate.json','p41_full_chow_heegner_certificate.json.gz','p41_drinfeld_hecke_certificate.json']})

(root/'p41_all_bad_heights_certificate.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('All 53 bad-height rows, full spectral vectors, trace-zero and R57 independent normalization PASS.',flush=True)
