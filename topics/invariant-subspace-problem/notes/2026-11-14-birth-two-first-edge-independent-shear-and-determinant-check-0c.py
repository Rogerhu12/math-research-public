"""Independent symbolic shear bridge from physical dual moment determinants.

This uses actual finite weights and log derivatives, not the supplied Pearson
formula. It checks the complete hard first edge at arbitrary q,L,z.
"""
import sympy as s
from itertools import combinations
from math import factorial

q,L,z=s.symbols('q L z',positive=True)
def bc(a,k):
    return s.Rational(1,factorial(k))*s.prod(a-i for i in range(k))
def detmom(k,d):
    weights=[bc(q,i)*bc(L,k-i)*z**i for i in range(k+1)]
    return s.expand(sum(s.prod((b-a)**2 for a,b in combinations(ids,2))*
                        s.prod(weights[i] for i in ids)
                        for ids in combinations(range(k+1),d)))
Gs={k:s.expand(sum(bc(q,i)*bc(L,k-i)*z**i for i in range(k+1))) for k in range(1,5)}
Fs={k:s.cancel(detmom(k,2)/(q*L*z)) for k in range(1,5)}
Es={k:s.cancel(detmom(k,3)/(q*q*(q-1)*L*L*(L-1)*z**3)) for k in range(2,5)}
assert all(not value.has(s.Float) for value in list(Fs.values())+list(Es.values()))
assert Fs[1]==Es[2]==1
C2=(q-1)*(L-1)*z
Y=(Fs[2]*Es[3]*Gs[4]-Fs[4]*Gs[3])/2
theta_log={k:z*s.diff(Fs[k],z)/Fs[k] for k in Fs}
x_raw=-2*theta_log[2]+theta_log[1]+theta_log[3]
y_raw=-theta_log[4]+2*theta_log[3]-theta_log[2]
assert s.cancel(x_raw+C2*(z-1)*Gs[3]/(Fs[2]*Fs[3]))==0
print('ACTUAL_HARD_ENDPOINT_SHEAR_FROM_LOG_DETERMINANTS_PASS',flush=True)
assert s.cancel(y_raw-C2*(z-1)*Y/(Fs[2]*Fs[3]*Fs[4]))==0
print('ACTUAL_NEXT_SHEAR_FROM_LOG_DETERMINANTS_PASS',flush=True)
a,b,c,d,Q,rv,sv,xv,yv,w=s.symbols('a b c d Q r s x y w')
Am,A0,Ap=a+w*b,b+w*c,c+w*d
Bm,B0,Bp=w*Q,w*Q*rv/(Q+w*rv),w*rv*sv/(rv+w*sv)
K11=Am-A0*A0/Ap+Bm*xv*xv
K12=-Bm*xv-A0*B0*yv/Ap
K22=Bm-B0*B0/Bp-B0*B0*yv*yv/Ap
la=(a*c-b*b)+w*(a*d-b*c)+w*w*(b*d-c*c)
ph=Q*(Q*sv-rv*rv)+w*Q*rv*sv+w*w*rv*rv*sv
formula=(Q*la*ph-w*Q**3*rv*(c+w*d)*(rv+w*sv)*xv*xv
         -w*Q**2*rv**2*sv*(a+w*b)*yv*yv
         -2*w*Q**2*rv*sv*(b+w*c)*(Q+w*rv)*xv*yv
         -w*w*Q**3*rv**2*sv*xv*xv*yv*yv)
cleared=(K11*K22-K12*K12)*(Q+w*rv)**2*(c+w*d)*sv/w
assert s.cancel(cleared-formula)==0
print('GENERIC_FINITE_HARD_ENDPOINT_SCHUR_DETERMINANT_PASS',flush=True)
print('ALL_PASS: independent symbolic source and determinant bridges',flush=True)
