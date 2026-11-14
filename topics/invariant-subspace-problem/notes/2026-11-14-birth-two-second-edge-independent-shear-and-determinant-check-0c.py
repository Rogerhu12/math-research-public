"""Independent symbolic second-edge bridge from actual log Hankel determinants.

No supplied Pearson identity is used to construct the adjacent shears. The
generic three-matrix Schur determinant is independently reconstructed as well.
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
Gs={k:s.expand(sum(bc(q,i)*bc(L,k-i)*z**i for i in range(k+1))) for k in range(2,6)}
Fs={k:s.cancel(detmom(k,2)/(q*L*z)) for k in range(2,6)}
Es={k:s.cancel(detmom(k,3)/(q*q*(q-1)*L*L*(L-1)*z**3)) for k in range(2,6)}
assert all(not v.has(s.Float) for v in [*Gs.values(),*Fs.values(),*Es.values()])
assert Es[2]==1
C2=(q-1)*(L-1)*z
X=(Gs[4]*Es[3]*Fs[2]-Gs[3]*Fs[4])/2
Y=(Gs[5]*Es[4]*Fs[3]-Gs[4]*Es[3]*Fs[5])/3
theta_log={k:z*s.diff(Fs[k],z)/Fs[k] for k in Fs}
x_raw=-2*theta_log[3]+theta_log[2]+theta_log[4]
y_raw=-theta_log[5]+2*theta_log[4]-theta_log[3]
# Clear the known positive moment denominators before polynomial multiplication.
# This avoids expensive generic rational simplification without changing the
# identity being checked or adding any parameter specialization.
poly=lambda v:s.Poly(v,q,L,z,domain=s.QQ)
fp={k:poly(v) for k,v in Fs.items()}
gp={k:poly(v) for k,v in Gs.items()}
ep={k:poly(v) for k,v in Es.items()}
xp=(gp[4]*ep[3]*fp[2]-gp[3]*fp[4]).mul_ground(s.Rational(1,2))
yp=(gp[5]*ep[4]*fp[3]-gp[4]*ep[3]*fp[5]).mul_ground(s.Rational(1,3))
px=poly(z)*(-2*fp[3].diff(z)*fp[2]*fp[4]
             +fp[2].diff(z)*fp[3]*fp[4]+fp[4].diff(z)*fp[2]*fp[3])
py=poly(z)*(-fp[5].diff(z)*fp[3]*fp[4]
             +2*fp[4].diff(z)*fp[3]*fp[5]-fp[3].diff(z)*fp[4]*fp[5])
assert (px+poly(C2*(z-1))*xp).is_zero
print('ACTUAL_SECOND_EDGE_LEFT_SHEAR_FROM_LOG_DETERMINANTS_PASS',flush=True)
assert (py-poly(C2*(z-1))*yp).is_zero
print('ACTUAL_SECOND_EDGE_RIGHT_SHEAR_FROM_LOG_DETERMINANTS_PASS',flush=True)
a,b,c,d,p,Q,r,ss,xv,yv,w=s.symbols('a b c d p Q r s x y w')
Am,A0,Ap=a+w*b,b+w*c,c+w*d
Bm,B0,Bp=w*p*Q/(p+w*Q),w*Q*r/(Q+w*r),w*r*ss/(r+w*ss)
K11=Am-A0*A0/Ap+Bm*xv*xv
K12=-Bm*xv-A0*B0*yv/Ap
K22=Bm-B0*B0/Bp-B0*B0*yv*yv/Ap
la=(a*c-b*b)+w*(a*d-b*c)+w*w*(b*d-c*c)
ph=p*Q*(Q*ss-r*r)+w*Q*r*(p*ss-Q*r)+w*w*r*ss*(p*r-Q*Q)
formula=(Q*la*ph-w*p*Q**3*r*(c+w*d)*(r+w*ss)*xv*xv
         -w*Q**2*r**2*ss*(a+w*b)*(p+w*Q)*yv*yv
         -2*w*p*Q**2*r*ss*(b+w*c)*(Q+w*r)*xv*yv
         -w*w*p*Q**3*r**2*ss*xv*xv*yv*yv)
cleared=(K11*K22-K12*K12)*(p+w*Q)*(Q+w*r)**2*(c+w*d)*ss/w
assert s.cancel(cleared-formula)==0
print('GENERIC_COMPLETE_INTERIOR_SCHUR_DETERMINANT_PASS',flush=True)
print('ALL_PASS: independent second-edge log determinants and full Schur bridge',flush=True)
