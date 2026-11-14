import sympy as s
from math import comb, factorial

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


def mul(a,b):
 c=[s.S.Zero]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def coefficients(a,b,c,d,p,q,r,t,x,y):
 U=[a*c-b*b,a*d-b*c,b*d-c*c]
 V=[p*q*(q*t-r*r),q*r*(p*t-q*r),r*t*(p*r-q*q)]
 out=[q*z for z in mul(U,V)]
 terms=[(p*q**3*r*x*x,mul([c,d],[r,t])),
        (q*q*r*r*t*y*y,mul([a,b],[p,q])),
        (2*p*q*q*r*t*x*y,mul([b,c],[q,r]))]
 for factor,poly in terms:
  for k,z in enumerate(poly):out[k+1]-=factor*z
 out[2]-=p*q**3*r*r*t*x*x*y*y
 return [s.factor(v) for v in out]

if __name__=='__main__':
 count=0;least=None
 for Q in range(1,7):
  for L in range(Q,Q+5):
   for birth in range(1,Q+1):
    delta=Q-birth;h=Q+L+1-2*birth
    if h<4:continue
    for z in [s.Rational(1,16),s.Rational(1,4),s.S.One,s.Integer(4),s.Integer(16)]:
     av=[monic(Q,L,delta+1,j,z) for j in range(h+2)]
     bv=[monic(Q,L,delta,j,z)[0] for j in range(h)]
     dv=[av[j+1][1]-av[j][1] for j in range(h+1)]
     for n in range(2,h-1):
      co=coefficients(*[av[j][0] for j in range(n-1,n+3)],*[bv[j] for j in range(n-2,n+2)],dv[n-1]-dv[n],dv[n+1]-dv[n])
      if any(x<0 for x in co):
       print('NEGATIVE',Q,L,birth,n,z,co,flush=True);raise SystemExit(1)
      if any(x==0 for x in co):print('ZERO',Q,L,birth,n,z,flush=True)
      count+=1
   print('DONE',Q,L,count,flush=True)
 print('PASS all quartic coefficients positive',count,flush=True)
