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
for q0 in range(1,5):
 for L in range(q0,q0+4):
  for t0 in range(1,q0+1):
   de=q0-t0;h=q0+L+1-2*t0
   if h<2:continue
   D=de+1
   for z in [s.Rational(1,4),s.Integer(4)]:
    aa=[monic(q0,L,D,j,z) for j in range(h+2)]
    bb=[monic(q0,L,D-1,j,z)[0] for j in range(h)]
    for n in range(1,h):
     a,b,c,d=[aa[j][0]for j in range(n-1,n+3)]
     ip=0 if n==1 else 1/bb[n-2]
     q,r=bb[n-1:n+1]
     it=0 if n==h-1 else 1/bb[n+1]
     x=2*aa[n][1]-aa[n-1][1]-aa[n+1][1]
     y=aa[n+2][1]-2*aa[n+1][1]+aa[n][1]
     C0=x*(d*it-b/q)+y*(c/r-a*ip)+(y-x)*x*y
     assert C0+(z+1)/(z-1)*x*y==0,('new coupling',q0,L,t0,z,n)
     for w in [s.Rational(2,3),s.Integer(5)]:
      lm=a/(w*q)+a*ip+b/q+w*b*ip
      l0=b/(w*r)+b/q+c/r+w*c/q
      lp=c*it/w+c/r+d*it+w*d/r
      val=x*lp-y*lm+(y-x)*(x*y+l0)
      assert val==x*y*(w-1)*(w-z)/((z-1)*w),('whole w',q0,L,t0,z,n,w)
     checks+=1
print('PASS exact collapsed coupling and full-w commutator including all hard endpoints:',checks)
