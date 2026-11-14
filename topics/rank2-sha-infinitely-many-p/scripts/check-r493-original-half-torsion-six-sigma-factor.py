#!/usr/bin/env python3
"""R493: exact six-sigma half-period factor and its physical transports."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sy

BASE = Path(__file__).resolve().parents[1]

def k(a=0,b=0): return (Q(a),Q(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def inv(x):
    n=x[0]*x[0]+3*x[1]*x[1]
    assert n
    return (x[0]/n,-x[1]/n)
def div(x,y): return mul(x,inv(y))
def sc(c,A): return [[mul(c,x)for x in row]for row in A]
def eye(n): return [[k(i==j)for j in range(n)]for i in range(n)]
def transpose(A): return [list(row)for row in zip(*A)]
def adjoint(A): return [[conj(x)for x in row]for row in transpose(A)]
def mm(A,B):
    BT=transpose(B)
    return [[sumk(mul(x,y)for x,y in zip(row,col))for col in BT]for row in A]
def sumk(xs):
    z=k()
    for x in xs:z=add(z,x)
    return z
def ma(A,B):return [[add(x,y)for x,y in zip(a,b)]for a,b in zip(A,B)]
def ms(A,B):return ma(A,sc(k(-1),B))
def diag(xs):return [[x if i==j else k()for j in range(len(xs))]for i,x in enumerate(xs)]
def mi(A):
    n=len(A);M=[row[:]+e[:]for row,e in zip(A,eye(n))]
    for j in range(n):
        ii=next(i for i in range(j,n)if M[i][j]!=k())
        M[j],M[ii]=M[ii],M[j]
        c=inv(M[j][j]);M[j]=[mul(c,x)for x in M[j]]
        for i in range(n):
            if i==j:continue
            c=M[i][j];M[i]=[sub(x,mul(c,y))for x,y in zip(M[i],M[j])]
    assert [row[:n]for row in M]==eye(n)
    return [row[n:]for row in M]
def enc(A):
    return {"real":[[str(x[0])for x in row]for row in A],
            "delta":[[str(x[1])for x in row]for row in A]}
def encv(v):return enc([v])

d=k(0,1);w=k(Q(-1,2),Q(1,2));w2=mul(w,w)
g=div(add(k(5),d),k(2));gb=conj(g)
H=[[k(x)for x in row]for row in
   [[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]]
E=diag([k(1),w,w2,k(1)])
Cp=sc(k(Q(1,2)),H)
Cm=[[k(Q(1,2)-int(i==j))for j in range(4)]for i in range(4)]
A=mm(E,Cp);Am=mm(E,Cm)
O=[[neg(w),k(),k(),k()],
   [k(),k(),w2,k()],
   [k(),k(),k(),w],
   [k(),k(1),k(),k()]]
O2=[[w2,k(),k(),k()],
    [k(),k(),k(),neg(w2)],
    [k(),neg(w),k(),k()],
    [k(),k(),k(-1),k()]]
T=mm(A,O);T2=mm(T,T)
assert mm(T2,T)==eye(4)
assert mm(T,adjoint(T))==eye(4)
assert T2==mm(Am,O2)

v=[[k(1)],[w],[neg(w2)],[k(-1)]]
U=ms(eye(4),sc(k(Q(1,2)),mm(v,adjoint(v))))
P=[[k(),k(1),k(),k()],
   [k(),k(),k(),neg(w2)],
   [k(),k(),neg(w),k()],
   [neg(w),k(),k(),k()]]
assert U==mm(T2,P) and mm(U,U)==eye(4)
assert mm(U,adjoint(U))==eye(4)

I=[0,2,3,4]
def embed(B):
    Z=eye(6)
    for i,ii in enumerate(I):
        for j,jj in enumerate(I):Z[ii][jj]=B[i][j]
    return Z
T6,U6,A6=embed(T),embed(U),embed(A)
y=[d,mul(k(2),d),g,gb,k(1),k(2)]
q=[d,mul(k(2),d),g,gb,mul(k(3),d),k(4)]
yp=mm([y],T6)[0];qp=mm([q],T6)[0];qpp=mm([q],mm(T6,T6))[0]
assert yp==y and mm([q],U6)[0]==q
assert qp==[mul(k(2),add(k(1),d)),mul(k(2),d),
            mul(k(2),add(k(1),d)),k(),add(k(3),d),k(4)]
assert sumk(mul(x,conj(x))for x in qp)==k(72)

# Exact old L/M companion transforms; the coordinates before this diagonal
# are R465's physical t_i, while T acts on the original unscaled sigma inputs.
L0=[[2,2,2,2,2,4],[2,2,2,2,-58,0],[2,2,2,2,2,-30],
    [4,-1,0,0,0,0],[7,7,-15,0,0,0],[7,7,7,-22,0,0]]
L0=[[k(x)for x in row]for row in L0]
M0=[[k(1),k(1),k(1),k(1),mul(k(3),d),k(4)],
    [mul(k(3),d)]*4+[k(29),k()],
    [k(1),k(1),k(1),k(1),mul(k(3),d),k(-14)],
    [k(4),k(-1),k(),k(),k(),k()],
    [k(7),k(7),k(-15),k(),k(),k()],
    [k(7),k(7),k(7),k(-22),k(),k()]]
scale=diag([d,mul(k(2),d),g,gb,k(1),k(1)])
L=mm(L0,scale);M=mm(M0,scale)
DL=mm(mm(L,T6),mi(L));DM=mm(mm(M,U6),mi(M))
for D in [DL,DM]:
    assert D[0]==[k(1)]+[k()]*5
    assert [row[0]for row in D]==[k(1)]+[k()]*5
assert mm(mm(DL,DL),DL)==eye(6)
assert mm(DM,DM)==eye(6)
NL=diag([k(n)for n in [136,3480,1020,60,2310,4466]])
NM=diag([k(n)for n in [72,1624,252,60,2310,4466]])
assert mm(mm(DL,NL),adjoint(DL))==NL
assert mm(mm(DM,NM),adjoint(DM))==NM

# All four canonical half-period phase products.  The selected coefficients
# divided by eta=(1,omega^2,omega,1) are 1+2*k_i.
ks=[(0,1),(-1,1),(-2,-1),(1,3)]
phases=[]
for s,r in [(0,0),(1,0),(0,1),(1,1)]:
    ch=0;ph=0
    for aa,bb in ks:
        m,n=aa*s-bb*r,bb*s+(aa-bb)*r
        ch+=m+n+m*n
        ph+=m*r-n*s
    exponent=(2*ch+ph)%4
    assert exponent==0
    # delta*(s+r*omega)=(s-2r)+(2s-r)*omega.
    m,n=s-2*r,2*s-r
    sign=(-1)**((m+n+m*n)%2)
    assert sign==(1 if (s,r)==(0,0)else -1)
    phases.append({"s":s,"r":r,"four_factor_i_exponent":exponent,
                   "sigma_2delta_period_sign":sign,
                   "sigma_4_period_sign":1})

# Complete rational proof of sum_t prod sigma_t =2 prod sigma(s-z_i).
# The nonzero half-period roots satisfy e^3=-b and c_t^4=1/(3e^2).
x1,x2,x3,x4,e,b=sy.symbols("x1 x2 x3 x4 e b")
f=(x1*x2-e*(x1+x2)-2*e**2)*(x3*x4-e*(x3+x4)-2*e**2)
reduced=sy.rem(sy.Poly(-e*f/(3*b),e),sy.Poly(e**3+b,e)).as_expr()
trace=3*sy.expand(reduced).coeff(e,0)
complete=sy.expand((x2-x1)*(x4-x3)+trace)
assert sy.expand(complete-2*(x1-x4)*(x3-x2))==0

# The actual complementary five-sigma source has degree 27, not 33.
Z0=[[1,1,1,1,1],[4,-1,0,0,0],[7,7,-15,0,0],
    [1,1,1,-22,0],[4,4,4,4,-23]]
Z0=[[k(x)for x in row]for row in Z0]
Zscale=diag([d,mul(k(2),d),g,k(1),k(2)])
Zmat=mm(Z0,Zscale)
assert mm(Zmat,adjoint(Zmat))==diag([k(n)for n in [27,60,2310,506,2484]])
a0,b0=1428552127,2161889730
n0=a0*a0-a0*b0+b0*b0
ratio54=((a0*a0-b0*b0)*pow(n0,-1,54)%54,
         (2*a0*b0-b0*b0)*pow(n0,-1,54)%54)
assert ratio54==(1,0)

# A fixed complete W' companion frame on its five nonzero inputs.
others=[0,1,2,4,5];aa=[qp[i]for i in others]
frame=[aa]
for j in range(1,5):
    row=[k()]*5
    row[0]=neg(div(conj(aa[j]),conj(aa[0])))
    row[j]=k(1)
    assert sumk(mul(x,conj(y))for x,y in zip(row,aa))==k()
    frame.append(row)
frame_inverse=mi(frame)

out={
 "field":"Q(delta), delta^2=-3; omega=(-1+delta)/2",
 "input_order":["xi1","xi2","xi3","xi4","c","d"],
 "selected_order":["xi1","xi3","xi4","c"],
 "half_period_phases":phases,
 "half_period_rational_identity":str(complete),
 "A4":enc(A),"O4":enc(O),"T4":enc(T),"T6":enc(T6),
 "T_order":3,"T_is_unitary":True,"T_fixes_Ys":True,
 "U4":enc(U),"U6":enc(U6),"U_order":2,"U_fixes_W":True,
 "U_reflection_vector":enc(v),
 "source_relations":["h=-A_*rho0","h=omega^2*T_*rho0",
                    "(T^2)_*rho0=-omega^2*(rho0+h)","U_*rho0=rho0+h"],
 "Y_row":encv(y),"W_row":encv(q),"W_prime":encv(qp),"W_second":encv(qpp),
 "L_companion_transform":enc(DL),"M_companion_transform":enc(DM),
 "first_Y_CM_projectors_commute_with_T":True,
 "first_W_CM_projectors_commute_with_U":True,
 "Z27_full_frame":enc(Zmat),"Z27_degrees":[27,60,2310,506,2484],
 "whole_odd27_ratio_mod54":list(ratio54),
 "odd27_anchor":"sigma(3*delta*z), true scalar core beta=-lambda",
 "W_prime_five_input_frame":enc(frame),
 "W_prime_five_input_frame_inverse":enc(frame_inverse),
 "deep_grid":"xi4 unit, all other five original sigma inputs in p^n",
 "weighted_central_first_coefficient":"24*d*Omega^5*bar(gamma7)^(-6)*I_sigma,1",
 "weighted_central_value":"beta^(5*n)*A(kappa^n), valuation exactly 5*n",
 "boundaries":["The Y weight depends on xi4; the W-prime zero-mass argument cannot be applied to it.",
               "The independent five-sigma deep grid is transported in full; no complementary domain is deleted."]
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("Full half-period phases, six-sigma factor, T/U transforms, companion blocks, degree27 core, and exact grid frame passed.")
