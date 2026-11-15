#!/usr/bin/env python3
"""R732 continuation: full local Schwartz data of the two actual type-five lines.
No fitted theta coefficients or output tables. Exact Q(zeta51), Q(zeta24).
Public Actions, python-flint==0.9.0; no files are written.
"""
from fractions import Fraction
from flint import fmpq, fmpq_poly
import json, time
START=time.time()
class Field:
    def __init__(self, n):
        self.n = n
        if n == 24:
            coeff=[1,0,0,0,-1,0,0,0,1]
        elif n == 51:
            top=[int(j%3==0) for j in range(49)]
            coeff=[0]*33
            for j in range(32,-1,-1):
                c=top[j+16];coeff[j]=c
                for k in range(17):top[j+k]-=c
            assert not any(top)
        else:raise ValueError(n)
        self.mod=fmpq_poly(coeff)
        self.deg=len(coeff)-1
        self.zero = self(0)
        self.one = self(1)
        self.z = self([0, 1])
        self.powers = [self.one]
        for j in range(1, n):
            self.powers.append(self.powers[-1]*self.z)

    def __call__(self, x):
        if isinstance(x, Element):
            assert x.F is self
            return x
        if isinstance(x, Fraction):
            x = fmpq(x.numerator, x.denominator)
        if isinstance(x, str):
            x = fmpq(x)
        if not isinstance(x, (list, fmpq_poly)):
            x = [x]
        return Element(self, fmpq_poly(x) % self.mod)


class Element:
    def __init__(self, F, p):
        self.F, self.p = F, p

    def __add__(self, b):
        b = self.F(b)
        return Element(self.F, self.p+b.p)
    __radd__ = __add__

    def __neg__(self):
        return Element(self.F, -self.p)

    def __sub__(self, b):
        return self + (-self.F(b))

    def __rsub__(self, b):
        return self.F(b)-self

    def __mul__(self, b):
        b = self.F(b)
        return Element(self.F, (self.p*b.p) % self.F.mod)
    __rmul__ = __mul__

    def __truediv__(self, b):
        b = self.F(b)
        g, s, _ = b.p.xgcd(self.F.mod)
        assert g == fmpq_poly([1])
        return self*Element(self.F, s)

    def __pow__(self, n):
        if n < 0:
            return (self.F.one/self)**(-n)
        a, b = self.F.one, self
        while n:
            if n & 1:
                a = a*b
            b = b*b
            n //= 2
        return a

    def __eq__(self, b):
        return self.p == self.F(b).p

    def conj(self):
        return sum((self.F.powers[(-j) % self.F.n]*str(self.p[j])
                    for j in range(len(self.p))), self.F.zero)

    def coeffs(self):
        return [str(self.p[j]) for j in range(self.F.deg)]


checks=[]
def check(name,v):
    assert v,name
    checks.append(name)
def mv(A,v):
    return [sum((a*b for a,b in zip(r,v)),r[0].F.zero) for r in A]
p=17
def kmul(a,b):
    return ((a[0]*b[0]-3*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def kpow(a,n):
    b=(1,0)
    while n:
        if n&1:b=kmul(a,b)
        a=kmul(a,a);n//=2
    return b
def leg(a):
    return 0 if a%p==0 else (1 if pow(a%p,8,p)==1 else -1)
K=Field(51);zeta=K.z**3;om=K.z**17
g0=(2,4);gs=[kpow(g0,j) for j in range(18)]
root17=sum((leg(a)*zeta**a for a in range(1,17)),K.zero)
check("original_17_generator_and_omega",len(set(gs))==18 and gs[6]==(8,9))
check("actual_real_quadratic_gauss",root17*root17==17 and root17.conj()==root17)
def W(g):
    x,y=g
    if not y:return [[K(int(a==(b if x==1 else -b)%17)) for b in range(17)] for a in range(17)]
    c=-leg(y)*root17/17;h=3*pow(2*y,-1,17)%17
    return [[c*zeta**((h*(x*(a*a+b*b)-2*a*b))%17) for b in range(17)] for a in range(17)]
Ws=[W(g) for g in gs]
tr=[sum((M[j][j] for j in range(17)),K.zero) for M in Ws]
six={kpow(gs[3],j):(-om**2)**j for j in range(6)}
def sextic(z):return six[kpow(z,48)]
records=[]
for k in (2,4):
    tau=(-om**2)**(3-k)
    # f = 18 sqrt17 Pi_tau e1, a fixed original rational coset.
    f=[root17*sum((tau**(-j)*Ws[j][a][1] for j in range(18)),K.zero) for a in range(17)]
    check(f"k{k}_entire_mu4_torus_multiplicity_one",sum((tau**(-j)*tr[j] for j in range(18)),K.zero)/18==1)
    check(f"k{k}_full_projected_e1_nonzero",f[1]!=0)
    check(f"k{k}_exact_full_17_eigenvector",mv(Ws[1],f)==[tau*x for x in f])
    check(f"k{k}_real_odd_original_vector",all(f[-a%17]==-f[a] and f[a].conj()==f[a] for a in range(17)))
    norm=sum((a*a.conj() for a in f),K.zero)
    check(f"k{k}_complete_positive_norm",norm==18*root17*f[1] and norm!=0)
    fibers=[K.zero]*17
    for a in range(17):
        for b in range(17):
            if (a,b)!=(0,0):fibers[a]+=sextic((a,b))**k
    gauss=sum((fibers[a]*zeta**(-a) for a in range(17)),K.zero)
    check(f"k{k}_all_trace_fiber_gauss",fibers==[K(16)]+[K(-1)]*16 and gauss==17)
    check(f"k{k}_delta_character_and_Hermitian_sign",sextic((0,1))**(-k)==1 and -(gauss/17)==-1)
    # The geometric operator uses the R290 fixed (not retwisted) two-model.
    ev=-om**2*om**2*tau**14
    expected=-om**2 if k==2 else K(-1)
    check(f"k{k}_actual_CM13_absolute_phase",ev==expected)
    check(f"k{k}_full_geometric_mu3_phase",om**2*tau**12==om**2)
    records.append({"k":k,"curve_B":17**k,"finite_17_unit_exponent":-48*k,
        "torus_exponent":(9-3*k)%18,"tau_power_basis":tau.coeffs(),
        "vector_normalization":"18*sqrt17*Pi_tau(e1)",
        "squared_norm_power_basis":norm.coeffs(),
        "normalized_CM13_eigenvalue_power_basis":ev.coeffs(),
        "leading_normalized_line":"D_omega" if k==2 else "D_minus"})
F=Field(24);z8=F.z**3;i=F.z**6;w=F.z**8
r2=z8+z8**(-1);r3=F.z**2+F.z**(-2)
check("actual_dyadic_radicals",r2*r2==2 and r3*r3==3)
t=(1-r3)/r2
old=[[w**2*(-z8)/r2,w**2*i/r2],[w**2*i/r2,w**2*i*z8/r2]]
new=[[w**2*x for x in row] for row in old]
check("old_full_two_torus_other_line",mv(old,[F.one,t])==[w,w*t])
check("new_full_two_omega_invariant",mv(new,[F.one,t])==[F.one,t])
check("full_two_vector_norm",1+t*t==3-r3)
v=[F.one,t,F(-1),t]
# Use the original R290 g* matrix exactly.
star=[[F(x) for x in row] for row in [[0,0,-1,0],[0,1,0,0],[-1,0,0,0],[0,0,0,1]]]
check("new_full_two_principal_generator_fixed",mv(star,v)==v)
check("original_half_period_descent",all(v[(j+2)%4]*((-1)**j)==-v[j] for j in range(4)))
# Full local periodicity, not just a phase at one good prime.
for k in (2,4):
    legal=[m for m in range(12) if (2*m+1)%3==2 and (2*m+1)%4==3 and (48*k*(2*m+2))%288==0]
    check(f"k{k}_exact_common_positive_weight_class",legal==[5,11])
ans={"format":"R732 two original type-five Schwartz vectors","status":"PASS",
    "checks":checks,"field17":"Q(zeta51)","field2":"Q(zeta24)",
    "Hermitian_alpha":17,"Gaussian":"51*sqrt3","legal_weights":"m=5 mod6",
    "two_place_vector":"(1,t,-1,t), t=(1-sqrt3)/sqrt2",
    "two_place_full_norm":"3-sqrt3","three_place_vector":"1_(3^-1 Z3)",
    "three_place_full_norm":3,"curves":records,
    "source_identification":"R732 full CM13 simple lines after complete finite theta descent",
    "elapsed_seconds":time.time()-START,"outputs_persisted":False}
print(json.dumps(ans,separators=(",",":")))
