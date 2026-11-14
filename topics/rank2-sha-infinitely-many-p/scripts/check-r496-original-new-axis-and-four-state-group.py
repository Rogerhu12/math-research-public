#!/usr/bin/env python3
"""R496 exact complete quarter coefficients and actual four-source closure."""
from pathlib import Path
import json
import sympy as s

def main():
    delta=s.I*s.sqrt(3);om=(-1+delta)/2;ga=(5+delta)/2
    H=s.Matrix([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])
    E=s.diag(1,om,om**2,1)
    O=s.Matrix([[-om,0,0,0],[0,0,om**2,0],[0,0,0,om],[0,1,0,0]])
    T4=s.simplify(E*H*O/2);T=s.eye(6);ind=[0,2,3,4]
    for i,ii in enumerate(ind):
        for j,jj in enumerate(ind):T[ii,jj]=T4[i,j]
    W=s.Matrix([[delta,2*delta,ga,s.conjugate(ga),3*delta,4]])
    Y=s.Matrix([[delta,2*delta,ga,s.conjugate(ga),1,2]])
    V=s.Matrix([[1+delta,delta,1+delta,0,(3+delta)/2,2]])
    assert s.simplify(W*T-2*V)==s.zeros(1,6)
    assert s.simplify(Y*T-Y)==s.zeros(1,6)
    assert s.simplify(T*T.conjugate().T)==s.eye(6)
    assert s.simplify(V*V.conjugate().T)==s.Matrix([[18]])
    a=s.simplify((W*V.conjugate().T)[0])
    assert s.simplify(a-(51+7*delta)/2)==0
    assert s.simplify(a*s.conjugate(a))==687
    MV=s.zeros(6);MV[0,:]=V
    for j in range(5):
        MV[j+1,j]=2;MV[j+1,5]=-s.conjugate(V[j])
    assert s.simplify(MV.det())==-288
    gram=s.simplify(MV*MV.conjugate().T)
    assert gram[0,0]==18
    assert all(gram[0,j]==gram[j,0]==0 for j in range(1,6))

    ray_a,ray_b=23776637887,77586679170
    mod=576;ni=pow((ray_a**2-ray_a*ray_b+ray_b**2)%mod,-1,mod)
    g=((ray_a**2-ray_b**2)*ni%mod,(2*ray_a*ray_b-ray_b**2)*ni%mod)
    assert g==(91,72)
    mul=lambda x,y:((x[0]*y[0]-x[1]*y[1])%mod,
                   (x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%mod)
    g2=mul(g,g);assert g2==(217,432)
    g8=mul(mul(g2,g2),mul(g2,g2));assert g8==(289,0)
    # The whole center: exp(-pi*i*3*N(a)*N(ell)/2)=i^(-3*687*N(ell)).
    pts=[(m,n) for m in range(4) for n in range(4)]
    ix={t:i for i,t in enumerate(pts)}
    norm=lambda t:(t[0]**2-t[0]*t[1]+t[1]**2)%4
    det=lambda t,u:t[0]*u[1]-t[1]*u[0]
    eps=lambda t:s.I**((-norm(t))%4)
    at=lambda t:-s.Rational((-1)**norm(t),4)
    for t in pts:assert (-3*687*norm(t))%4==(-norm(t))%4
    K=s.zeros(16);F=s.diag(*[eps(t) for t in pts]);HH=s.zeros(16)
    for j,t in enumerate(pts):
        for i,r in enumerate(pts):
            z=((r[0]+t[0])%4,(r[1]+t[1])%4)
            K[i,j]=at(z)*s.I**((-det(t,r))%4)
        for h in [(0,0),(2,0),(0,2),(2,2)]:
            r=((t[0]+h[0])%4,(t[1]+h[1])%4)
            HH[ix[r],j]+=s.I**(det(h,t)%4)
    assert K**2==s.eye(16) and F**4==s.eye(16)
    e0=s.zeros(16,1);e0[0]=1
    e1=K*e0;e2=F**2*e1;q=F*e1;h=e1+e2
    u=e0+h/2;v=e1-h/2;z=q-h/2
    source=s.Matrix.hstack(u,v,z,h)
    assert source.rank()==4
    K4=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,-1,0],[0,0,0,-1]])
    F4=s.Matrix([[1,0,0,0],[0,0,-1,0],[0,1,0,0],[0,0,0,1]])
    assert K*source==source*K4 and F*source==source*F4
    B2=HH/2-s.eye(16)
    B24=s.diag(-1,-1,1,1)
    assert B2*source==source*B24
    assert K*F**2*K*F**2*source==source*B24
    assert (K4*F4)**3==s.diag(1,1,1,-1)
    seen={tuple(s.eye(4))};todo=[s.eye(4)]
    while todo:
        x=todo.pop()
        for gen in (K4,F4):
            y=gen*x
            if tuple(y) not in seen:
                seen.add(tuple(y));todo.append(y)
    assert len(seen)==48

    # Exact degree56 weighted quarter operator and its degree14 descent.
    N=56;JE=s.zeros(N);H2=s.zeros(N)
    for j in range(N):
        for r in range(4):
            for t in range(4):
                phase=s.I**((t*(j+7*r))%4)
                JE[(j+14*r)%N,j]+=eps((t,r))*phase/4
                if r%2==t%2==0:H2[(j+14*r)%N,j]+=phase
    assert JE*H2==4*JE
    P=s.zeros(56,14)
    for j in range(14):P[2*j,j]=1;P[(2*j+28)%56,j]=1
    X7=s.diag(*[(-1)**j for j in range(14)])
    Z7=s.zeros(14)
    for j in range(14):Z7[(j+7)%14,j]=1
    U14=((s.eye(14)-s.I*Z7)*(s.eye(14)-s.I*X7)/2).applyfunc(s.expand)
    assert (JE*P-P*(2*U14)).applyfunc(s.expand)==s.zeros(56,14)
    assert (U14**2-U14+s.eye(14)).applyfunc(s.expand)==s.zeros(14)

    # Physical new-axis scaling; the genuinely unused fourth sigma is fixed.
    k=s.symbols("k")
    PV=s.eye(6)+(k**2-1)*V.conjugate().T*V/18
    assert s.simplify(V*PV-k**2*V)==s.zeros(1,6)
    assert s.simplify(MV[1:,:]*PV-MV[1:,:])==s.zeros(5,6)
    assert PV[3,:]==s.eye(6)[3,:]
    assert s.simplify(Y*PV-Y-(k**2-1)*(37-3*delta)*V/36)==s.zeros(1,6)
    B=s.Matrix([[delta,2*delta,ga,s.conjugate(ga),3*delta,0]])
    assert s.simplify(B*T-s.Matrix([[2+2*delta,2*delta,2+2*delta,0,3+delta,0]]))==s.zeros(1,6)
    assert s.simplify((B*Y.conjugate().T)[0]-(29+3*delta))==0
    report={
        "V_prime_bare_coefficients":[str(s.simplify(x)) for x in V],
        "degree_V_prime":18,
        "determinant_first_V_and_five_companions":-288,
        "W_cross_barV":"29+7*omega=(51+7*delta)/2","norm_cross":687,
        "g_mod576":list(g),"g_squared_mod576":list(g2),"g_eighth_mod576":list(g8),
        "complete_quarter_even_V_core":"K_V^2 f_t=(-i)^Norm(4t) f_t",
        "K_in_u_v_z_h":[list(map(int,K4.row(j))) for j in range(4)],
        "F_in_u_v_z_h":[list(map(int,F4.row(j))) for j in range(4)],
        "actual_group_order":48,
        "central_word_KF_cubed":[1,1,1,-1],
        "A_two_step":"F^2=K_A^2 on all four actual sources",
        "q_definition":"q=F e1; z=q-h/2",
        "q_weighted_B_identity":"q=(J_epsilon,B/2)h",
        "q_three_half_identity":"q=h/2-(i/2)(T_B,1/4+T_B,omega/4+T_B,(1+omega)/4)h",
        "complete_W_marginals":{"u":"6delta*T","v":"6delta*T","z":"0","h":"0","q":"0"},
        "negative_Y_block":{"q":"h/2","z":"0"},
        "Y_flat_three_half":"(29+3delta)*ell/4=omega*ell/2 mod Lambda, nonzero ell in O/2",
        "new_axis_Y_displacement":"(kappa^2-1)*(37-3delta)*Vprime/36",
        "new_axis_preserves":"xi4 and each 2*xi_j-conjugate(V_j)*d0, j=1,...,5",
        "old_M_q_z_signs":{"W":-1,"B":-1,"Q":"chi29","U":-1,"three_R":"chi29"},
        "word_lattice":"((P_V,2 P_W)^3) maps sources u,v,z identically and h to -h, scalar lambda^9",
        "boundary":"Only even V depths are closed with old W here; all physical word lattices and complements remain."
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(report,indent=2)+"\n")
    print("R496 complete quarter center, four-source group48, B-half identity and physical axes checked.")

if __name__=="__main__":main()

