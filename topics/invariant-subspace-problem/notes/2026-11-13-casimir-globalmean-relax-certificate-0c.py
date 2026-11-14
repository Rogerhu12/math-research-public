"""Exact nonactual relaxation counterexample; never an actual Schur/ISP counterexample."""
from fractions import Fraction as F
from json import dumps

def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out

def quartic(a,b,c,d,p,q,r,s,x,y):
 U=[a*c-b*b,a*d-b*c,b*d-c*c]
 V=[p*q*(q*s-r*r),q*r*(p*s-q*r),r*s*(p*r-q*q)]
 out=[q*v for v in mul(U,V)]
 for fac,C,E in [(p*q**3*r*x*x,[c,d],[r,s]),(q*q*r*r*s*y*y,[a,b],[p,q]),(2*p*q*q*r*s*x*y,[b,c],[q,r])]:
  for k,v in enumerate(mul(C,E)):out[k+1]-=fac*v
 out[2]-=p*q**3*r*r*s*x*x*y*y
 return out

n=12;m=13;D=12;t=5000;N=n+m+1;J=t+N-D
z=F(403,400);R=F(1213636691,10**9);mu=F(2260636031854,10**9)
u=mu*(J-mu);v=(D+mu)*(t-mu)
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

assert denP>0 and denV>0 and beta>0
assert 0<P<R<T and P<al<T
assert a*c>b*b and b*d>c*c and p*r>q*q and q*s>r*r
assert x<0<y and 0<mu-y<mu<mu-x<t
assert x==(z-1)*(b/p-c/q)/n==(z-1)*(b/r-a/q)/(z*(m+1))
assert y==(z-1)*(d/r-c/q)/(n+1)==(z-1)*(b/r-c/s)/(z*m)

def Q(j,w):
 av=[a,b,c,d];bv=[p,q,r,s]
 return (av[j]+w*av[j+1])*(bv[j]+w*bv[j+1])/(w*bv[j]*bv[j+1])

mus=[mu-x,mu,mu-y]
for j,M in enumerate(mus):
 assert Q(j,F(1))==M*(J-M)
 assert Q(j,z)==(D+M)*(t-M)

C0=x*(d/s-b/q)+y*(c/r-a/p)+(y-x)*x*y
assert C0+(z+1)*x*y/(z-1)==0
for w in [F(1),z,F(1,8000),F(7,3)]:
 C=x*Q(2,w)-y*Q(0,w)+(y-x)*(x*y+Q(1,w))
 assert C==x*y*(w-1)*(w-z)/((z-1)*w)

kap=z/(z-1)**2
def curvature_cap(j):return kap*F(t*min(j,D)*(N-max(j,D)),t+abs(j-D))
local_curvatures=[a/p,b/q,c/r,d/s]
for j,curv in zip(range(n-1,n+3),local_curvatures):
 assert 0<curv<curvature_cap(j)

# All N+1 first derivatives are fixed explicitly, with strict concavity.
f={n:(z-1)*c/q+n*mu}
f[n-1]=f[n]-(mu-x);f[n+1]=f[n]+mu;f[n+2]=f[n+1]+(mu-y)
left=n-1;right=n+2
for j in range(left):f[j]=F(j,left)*f[left]+j*(left-j)
for j in range(right+1,N+1):f[j]=f[right]+F(j-right,N-right)*(t*D-f[right])+(j-right)*(N-j)
assert f[0]==0 and f[N]==t*D
for j in range(1,N):
 C=F(t*min(j,D)*(N-max(j,D)),t+abs(j-D))
 lower=max(F(j*t*D,N),t*min(j,D)-C/(z-1))
 assert lower<f[j]<t*min(j,D),(j,float(lower),float(f[j]))
 assert 2*f[j]>f[j-1]+f[j+1]
for j,ei in [(n-1,(z-1)*b/p),(n,(z-1)*c/q),(n+1,(z-1)*d/r)]:
 assert (j+1)*f[j]-j*f[j+1]==ei

co=quartic(a,b,c,d,p,q,r,s,x,y);w=F(1,8000)
val=sum(c*w**j for j,c in enumerate(co))
assert co[0]>0 and co[4]>0 and val<-20000
lam=beta/kap
Em=z*(1+P)+1+n/R-F(n-1)/P-z*lam*(P*(A*P-1)/(n-1)+(P-al)/n)
outer_den=z*(m+2-lam*A*P/(n-1))
assert outer_den>0 and Em<F(-1,10)
Pprev=P-Em/outer_den
assert Pprev>P
out={'scope':'nonactual local relaxation only','parameters':{'n':n,'m':m,'D':D,'t':t,'z':str(z),'R':str(R),'mu':str(mu),'w':str(w)},'exact_quartic_value':str(val),'approx_quartic_value':float(val),'outer_constraint':float(Em),'preceding_lower_ratio':float(Pprev),'approx_norm_parameters':{k:float(v)for k,v in dict(P=P,R=R,T=T,alpha=al,beta=beta,A=A,B=B,x=x,y=y).items()},'assertions':'all three-point two-collapse Casimirs; both Pearson directions; third coupling; four finite-rectangle caps; all global mean bounds and strict first-derivative concavity; quartic negative; actual outer-height constraint violated'}
print(dumps(out,ensure_ascii=False,indent=2))
