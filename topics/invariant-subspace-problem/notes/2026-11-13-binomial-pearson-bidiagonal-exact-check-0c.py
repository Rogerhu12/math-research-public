import sympy as s
from math import comb
def monic(q,L,d,j,z):
 h=L-q+2*d;u=max(d-j,0);v=max(d-h+j,0);k=d-u-v
 rr=list(range(u,q-v+1))
 ff=[s.prod(r-i for i in range(u))*s.prod(r-q+i for i in range(v)) for r in rr]
 ww=[s.Rational(comb(q,r),comb(L,j+r-d))*z**r*f*f for r,f in zip(rr,ff)]
 xx=[r-u for r in rr]
 mm=[sum(w*x**l for w,x in zip(ww,xx)) for l in range(2*k+1)]
 if k:
  J=s.Matrix(k,k,lambda i,j:mm[i+j]);b=s.Matrix([mm[k+i]for i in range(k)])
  coeff=-J.inv()*b
  norm=mm[2*k]+(b.T*coeff)[0]
  sub=coeff[k-1]
 else:norm=mm[0];sub=0
 sub=sub-u*k-s.Rational(u*(u-1),2)-s.Rational(v*(2*q-v+1),2)
 return norm,sub


checks=0
for q in range(1,5):
 for L in range(q,q+4):
  for t in range(1,q+1):
   de=q-t;h=q+L+1-2*t
   if h<2:continue
   D=de+1
   for z in [s.Rational(1,4),s.Integer(1),s.Integer(4)]:
    av=[monic(q,L,D,j,z) for j in range(h+2)]
    bv=[monic(q,L,D-1,j,z)[0] for j in range(h)]
    for j in range(1,h+1):
     lhs=j*av[j+1][1]-(j+1)*av[j][1]-s.Rational(D*(D-1),2)
     assert lhs==(z-1)*av[j+1][0]/bv[j-1],('first',q,L,t,z,j,lhs)
     checks+=1
    for n in range(1,h):
     x=2*av[n][1]-av[n-1][1]-av[n+1][1]
     y=av[n+2][1]-2*av[n+1][1]+av[n][1]
     left=x-(z-1)/n*((0 if n==1 else av[n][0]/bv[n-2])-av[n+1][0]/bv[n-1])
     right=x-(z-1)/(z*(h+1-n))*(av[n][0]/bv[n]-av[n-1][0]/bv[n-1])
     lefty=y-(z-1)/(n+1)*(av[n+2][0]/bv[n]-av[n+1][0]/bv[n-1])
     righty=y-(z-1)/(z*(h-n))*(av[n][0]/bv[n]-(0 if n==h-1 else av[n+1][0]/bv[n+1]))
     assert left==right==lefty==righty==0,('shear',q,L,t,z,n)
     r1=z*(h+1-n)*((0 if n==1 else av[n][0]/bv[n-2])-av[n+1][0]/bv[n-1])-n*(av[n][0]/bv[n]-av[n-1][0]/bv[n-1])
     r2=z*(h-n)*(av[n+2][0]/bv[n]-av[n+1][0]/bv[n-1])-(n+1)*(av[n][0]/bv[n]-(0 if n==h-1 else av[n+1][0]/bv[n+1]))
     assert r1==r2==0,('cancelled-z1',q,L,t,z,n)
     checks+=1
print('PASS exact Pearson bidiagonal, both endpoint shears and z=1 norm relations:',checks)
