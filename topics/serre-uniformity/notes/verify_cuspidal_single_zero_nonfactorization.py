from math import isqrt
p,z,d,L,xi,eta=41,38,14,12547,1692,6217
assert all(L%r for r in range(2,isqrt(L)+1))
assert pow(xi,p,L)==1 and xi!=1 and pow(eta,3,L)==1 and eta!=1
assert next(j for j in range(1,7) if pow(L,j,14)==1)==6

def mul(a,b):return ((a[0]*b[0]+z*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def pw(a,n):
 r=(1,0)
 while n:
  if n&1:r=mul(r,a)
  a=mul(a,a);n//=2
 return r

g=next((x,y) for x in range(p) for y in range(1,p) if all(pw((x,y),1680//q)!=(1,0) for q in (2,3,5,7)))
logs={};v=(1,0)
for j in range(1680):logs[v]=j;v=mul(v,g)
Z=pw((1,1),560);labels={pw(Z,j):j for j in range(3)}
colour={v:labels[pw(v,560)] for v in logs}
S=[sum(pow(eta,colour[(t,1)],L)*pow(xi,t*y%p,L) for t in range(p))%L for y in range(p)]
Sm=[sum(pow(eta,-colour[(t,1)]%3,L)*pow(xi,t*y%p,L) for t in range(p))%L for y in range(p)]
a=21*pow(z,-1,p)%p
assert S[a]==0 and Sm[a]==4541
powers=[]
for j in range(6):powers.append(tuple(int(i==j) for i in range(6)))
powers.append((-1,1,-1,1,-1,1))
powers += [tuple(-x for x in v) for v in powers]
assert len(powers)==14
rows=[]
for b in (a,1):
 v=[p*int(a==b),0,0,0,0,0]
 for w,j in logs.items():
  x,y=w
  if (x*x-z*y*y)%p!=a*b%p:continue
  c=pow(xi,-2*z*y%p,L)*S[(a+b-2*x)%p]%L
  v=[(vv-c*tt)%L for vv,tt in zip(v,powers[j%d])]
 assert any(v)
 rows.append({'a':a,'b':b,'old_S':S[a],'old_opposite':Sm[a],
        'p(p+1)*B_theta_theta_eta_inverse_mod_Phi14':v,
        'nonzero':any(v)})

import json
from pathlib import Path
result={'p':p,'quadratic_parameter':z,'coefficient_prime':L,'psi_root':xi,'cubic_root':eta,'field_generator':list(g),'theta_generator_image':'T mod Phi_14','Phi_14_coefficients':[1,-1,1,-1,1,-1,1],'Phi_14_irreducible':True,'rows':rows,'scope':'Reuse of the prior individual Fourier zero; not a paired-zero example or an exceptional-prime search.'}
Path('/tmp/cuspidal_kernel_single_zero_certificate.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
