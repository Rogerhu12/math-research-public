# Exact rational verification of the all-height two-weight MP/Schur identity.
# Astra-ISP-0c017065 / two_weight_general_height_1856, 2026-11-13.
# Run: python3 this_file.py; requires SymPy. The proof is analytic, not finite testing.
import sympy as s
from math import comb, factorial

def ch(k,m,z):
 if k<0:return s.S.Zero
 if m==0:return s.S.One if k==0 else s.S.Zero
 return comb(m+k-1,k)*z**k

def rect(t,k,N,m,z):
 if t==0 or k==0:return s.S.One
 hs=[sum(ch(r,m,z)*ch(d-r,N-m,1) for r in range(d+1)) for d in range(t+k)]
 return s.det(s.Matrix(k,k,lambda i,j: hs[t-i+j] if t-i+j>=0 else 0))

def physical(q,h,de,n,a):
 L=q+h-2*de;t=q-de;p=t+n
 src=list(range(max(0,p-L),min(q,p)+1));out=list(range(t+1))
 A=s.Matrix([[a**(j-i)*comb(q-i,j-i)*comb(L-t+i,n-j+i) if 0<=j-i<=n and n-j+i<=L-t+i else 0 for j in src] for i in out])
 Wi=s.diag(*[s.Rational(1,comb(q,j)*comb(L,p-j)) for j in src])
 g=s.Matrix([(-1)**(q-i-de)*a**(q-i)*s.Rational(comb(q-i,de),comb(L,t-i)) for i in out])
 return (g.T*(A*Wi*A.T).inv()*g)[0]

cnt=0
for h in range(2,8):
 for de in range(h//2+1):
  for q in sorted(set([de,de+1,de+3])):
   L=q+h-2*de;t=q-de
   for a in [s.Rational(1,2),s.Rational(1),s.Rational(3)]:
    z=a*a
    for n in range(h+1):
     fixed=s.Rational(factorial(q)*factorial(n)*factorial(h-n),factorial(L)*factorial(de)**2)*z**de*rect(t,de+1,h+2,n+1,z)/rect(t+1,de,h,n,z)
     raw=physical(q,h,de,n,a)
     assert s.cancel(fixed-raw)==0,(q,h,de,n,a,fixed,raw)
     cnt+=1
print('PASS exact full symmetric-layer MP versus fixed rectangle quotient:',cnt)
