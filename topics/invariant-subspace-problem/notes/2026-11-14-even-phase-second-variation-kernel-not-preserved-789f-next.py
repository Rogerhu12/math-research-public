"""The fixed N=4 second-order-kernel line; exact full source metric.

This preserves the symbolic computation already completed for the accompanying
note.  A positive value on its specified source is not a general fourth-order
Schur theorem.
"""
import resource
import sympy as sp

resource.setrlimit(resource.RLIMIT_CPU, (55, 60))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
u = sp.symbols('u', real=True)
z = [1-u, sp.Integer(1), sp.Integer(1), 1+u]
S = sum(z)
q = sum(z[i]*z[j] for i in range(4) for j in range(i+1, 4))
f = sum(z[i]*z[j]*z[k] for i in range(4) for j in range(i+1, 4)
        for k in range(j+1, 4))
p = sp.prod(z)
H = sp.diag(*[1/z[i] for i in range(3)])+sp.ones(3)/z[3]
C = sp.Matrix(3, 3, lambda i, j: ((S-2*z[i]) if i == j else 0)
              + z[i]*(S-z[i])*(z[j]-z[3])/q)
L = sp.Matrix(3, 3, lambda i, j: ((S*z[i]**2 if i == j else 0)
              - z[i]*(z[j]**2-z[3]**2))/(S*p))
Q = sp.Matrix(3, 3, lambda i, j: ((S*(f-2*p/z[i]) if i == j else 0)
              + (S-2*z[i])*(p/z[j]-p/z[3]))/(S*p))
H0 = (C*L+2*C.inv()-Q).applyfunc(sp.cancel)
defect = (H-H0.T*H*L.inv()*H0).applyfunc(sp.factor)
v = sp.Matrix([1, -1, -1])/2
print('defect determinant:', sp.factor(defect.det()))
print('fixed-source defect:', sp.factor((v.T*defect*v)[0]))
print('fixed-source norm:', sp.factor((v.T*H*v)[0]))
print('rank at u=1/2:', defect.subs(u, sp.Rational(1, 2)).rank())
