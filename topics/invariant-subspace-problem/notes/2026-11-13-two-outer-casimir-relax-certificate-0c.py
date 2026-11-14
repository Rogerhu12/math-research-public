"""Nonactual relaxation only: five collapse layers and full first outer steps do not suffice.
Every sign assertion below uses fractions.Fraction. No numerical minimization is needed.
"""
from fractions import Fraction as F
import json

n0,m0,D,t=25,30,20,78000
N=n0+m0+1;h=N-1;J=t+N-D
z=F(1001,1000)
R0=F(14798576423825875,10**16)
mu0=F(23879157497691315,10**12)
kap=z/(z-1)**2

def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out

def quartic(a,b,c,d,p,q,r,s,x,y):
 out=[q*v for v in mul([a*c-b*b,a*d-b*c,b*d-c*c],
                      [p*q*(q*s-r*r),q*r*(p*s-q*r),r*s*(p*r-q*q)])]
 for fac,C,E in [(p*q**3*r*x*x,[c,d],[r,s]),
                (q*q*r*r*s*y*y,[a,b],[p,q]),
                (2*p*q*q*r*s*x*y,[b,c],[q,r])]:
  for k,v in enumerate(mul(C,E)):out[k+1]-=fac*v
 out[2]-=p*q**3*r*r*s*x*x*y*y
 return out

def cap(j):return kap*F(t*min(j,D)*(N-max(j,D)),t+abs(j-D))

def phase(n,R,mu):
 m=h-n;u=mu*(J-mu);v=(D+mu)*(t-mu)
 den=u*(1+z*R)-v*(1+R)
 beta=z*R*den/((z-1)*(1+R)*(1+z*R))
 al=(z*v*(1+R)-u*(1+z*R))/(z*den)
 sigma=J-2*mu
 denP=z*(m+1)-beta*(z-1)**2/n
 P=al+((z-1)*sigma-z*(m+1)*(1+al)+n*(1+1/R))/denP
 denV=F(n+1)/al-beta*(z-1)**2/(z*m*R)
 V=((z-1)*sigma-z*m*(1+R)+F(n+1)*(1+al)/al)/denV
 T=al/(1-V)
 A=1/R+z*(m+1)*(al-P)/n
 B=al*R+F(n+1)*(1-al/T)/(z*m)
 x=beta*(z-1)*(P-al)/n
 y=beta*(z-1)*(1-al/T)/(z*m*R)
 a,b,c,d=beta*A,beta,beta*al,beta*B
 p,q,r,s=1/P,F(1),R,R*T
 lam=beta/kap
 Em=z*(1+P)+1+n/R-F(n-1)/P-z*lam*(P*(A*P-1)/(n-1)+(P-al)/n)
 def em(nn,mm,zz,PP,RR,aa,ll,AA):
  return zz*(1+PP)+1+nn/RR-F(nn-1)/PP-zz*ll*(PP*(AA*PP-1)/(nn-1)+(PP-aa)/nn)
 Ep=em(m,n,1/z,1/T,1/R,1/al,lam*al/R,B/al)
 return locals()

def check_local(v):
 n=v['n'];a,b,c,d,p,q,r,s,x,y=[v[k]for k in ['a','b','c','d','p','q','r','s','x','y']]
 P,R,T,al,beta,A,B=[v[k]for k in ['P','R','T','al','beta','A','B']]
 assert v['denP']>0 and v['denV']>0 and min(a,b,c,d,p,q,r,s)>0
 assert 0<P<R<T and P<al<T
 assert a*c>b*b and b*d>c*c and p*r>q*q and q*s>r*r
 assert x<0<y and 0<v['mu']-y<v['mu']<v['mu']-x<t
 assert x==(z-1)*(b/p-c/q)/n==(z-1)*(b/r-a/q)/(z*(v['m']+1))
 assert y==(z-1)*(d/r-c/q)/(n+1)==(z-1)*(b/r-c/s)/(z*v['m'])
 def Q(j,w):
  av=[a,b,c,d];bv=[p,q,r,s]
  return (av[j]+w*av[j+1])*(bv[j]+w*bv[j+1])/(w*bv[j]*bv[j+1])
 for j,M in enumerate([v['mu']-x,v['mu'],v['mu']-y]):
  assert Q(j,F(1))==M*(J-M)
  assert Q(j,z)==(D+M)*(t-M)
 C0=x*(d/s-b/q)+y*(c/r-a/p)+(y-x)*x*y
 assert C0+(z+1)*x*y/(z-1)==0
 for j,cv in zip(range(n-1,n+3),[a/p,b/q,c/r,d/s]):assert 0<cv<cap(j)
 return True

center=phase(n0,R0,mu0)
left=phase(n0-1,center['P'],mu0-center['x'])
right=phase(n0+1,center['T'],mu0-center['y'])
assert all(check_local(v)for v in [left,center,right])
# Exact overlap consistency; both first outer steps are genuine extensions of the same data.
assert left['R']==center['P'] and left['T']==R0
assert right['P']==R0 and right['R']==center['T']
assert left['beta']==center['beta']*center['A']*center['P']
assert right['beta']==center['beta']*center['al']/R0
assert left['mu']-left['y']==center['mu']
assert right['mu']-right['x']==center['mu']
for lk,ck in [('b','a'),('c','b'),('d','c'),('q','p'),('r','q'),('s','r')]:
 assert left[lk]/center['P']==center[ck]
for rk,ck in [('a','b'),('b','c'),('c','d'),('p','q'),('q','r'),('r','s')]:
 assert right[rk]*center['R']==center[ck]
assert center['Em']>3 and center['Ep']>4
left_den=z*(center['m']+2-center['lam']*center['A']*center['P']/(center['n']-1))
assert left_den>0 and center['Em']==left_den*(center['P']-left['P'])
assert 0<left['P']<center['P'] and right['T']>center['T']>0

# Complete all one-derivative constraints, keeping all five fixed local slopes.
f={n0:(z-1)*center['c']/center['q']+n0*mu0}
mu={n0-2:left['mu']-left['x'],n0-1:left['mu'],n0:mu0,
    n0+1:right['mu'],n0+2:right['mu']-right['y']}
for j in range(n0-1,n0-3,-1):f[j]=f[j+1]-mu[j]
for j in range(n0,n0+3):f[j+1]=f[j]+mu[j]
l=n0-2;r=n0+3
for j in range(l):f[j]=F(j,l)*f[l]+j*(l-j)
for j in range(r+1,N+1):f[j]=f[r]+F(j-r,N-r)*(t*D-f[r])+(j-r)*(N-j)
assert f[0]==0 and f[N]==t*D
for j in range(1,N):
 C=cap(j)/kap
 lower=max(F(j*t*D,N),t*min(j,D)-C/(z-1))
 assert lower<f[j]<t*min(j,D),('mean interval',j)
 assert 2*f[j]>f[j-1]+f[j+1],('mean concavity',j)
for v in [left,center,right]:
 nn=v['n']
 for j,ei in [(nn-1,(z-1)*v['b']/v['p']),(nn,(z-1)*v['c']/v['q']),(nn+1,(z-1)*v['d']/v['r'])]:
  assert (j+1)*f[j]-j*f[j+1]==ei

co=quartic(*[center[k]for k in ['a','b','c','d','p','q','r','s','x','y']])
w=F(1,40000);value=sum(v*w**j for j,v in enumerate(co))
assert co[0]>0 and co[4]>0 and co[1]<0 and value<-3_000_000
# First failures occur only on the second outward step.
left2=phase(n0-2,left['P'],left['mu']-left['x'])
right2=phase(n0+2,right['T'],right['mu']-right['y'])
assert left2['P']>0 and left2['P']<left2['R']<left2['T']
assert left2['A']*left2['al']<1 # newly introduced upper norm violates scalar comparison
assert 0<right2['T']<right2['R'] # newly introduced lower norm violates scalar comparison
assert right2['B']<right2['al']**2
print(json.dumps({
 'scope':'nonactual relaxation; not a counterexample to the actual product-weight conjecture',
 'parameters':{k:str(v)for k,v in dict(n=n0,m=m0,D=D,t=t,z=z,R=R0,mu=mu0,w=w).items()},
 'all_first_outer_steps':'positive norms, both positive phase denominators, both scalar families, both shear signs, mu interval, all three-point Casimirs, finite-width curvature caps: PASS',
 'all_global_means':'all 57 endpoints and mean bounds, all 55 strict concavity inequalities, all five local slopes: PASS',
 'center_outer_constraints':{k:float(center[k])for k in ['Em','Ep']},
 'quartic_coefficient_signs':[('+'if x>0 else'-')for x in co],
 'exact_quartic_value':str(value),
 'approx_quartic_value':float(value),
 'first_left_failure':{'n':n0-2,'upper_defect':float(left2['A']*left2['al']-1)},
 'first_right_failure':{'n':n0+2,'next_lower_ratio':float(right2['T']),'present_lower_ratio':float(right2['R']),'upper_defect':float(right2['B']-right2['al']**2)},
},ensure_ascii=False,indent=2))
