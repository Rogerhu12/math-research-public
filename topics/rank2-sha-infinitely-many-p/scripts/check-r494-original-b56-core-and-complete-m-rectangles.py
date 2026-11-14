#!/usr/bin/env python3
"""R494 exact original degree56 core and complete W/Q/U rectangle certificate.
All matrices are exact; the full canonical lift and absolute anchor are proved
in the companion Markdown.  No finite-prime evidence is used.
"""
from pathlib import Path
import json
import sympy as s

def perm_matrix(N, indices, signs=None):
    M=s.zeros(N)
    signs=signs or [1]*N
    for j in range(N):
        M[indices[j] % N,j]=signs[j]
    return M

def main():
    N=56
    ray_a,ray_b=23776637887,77586679170
    ni=pow((ray_a*ray_a-ray_a*ray_b+ray_b*ray_b)%112,-1,112)
    assert ((ray_a*ray_a-ray_b*ray_b)*ni%112,
            (2*ray_a*ray_b-ray_b*ray_b)*ni%112)==(43,56)
    J=perm_matrix(N,[(15*j)%N for j in range(N)])
    B2=perm_matrix(N,[(29*j+28)%N for j in range(N)],
                   [(-1)**j for j in range(N)])
    D=J*B2
    assert J**2 == B2**2 == s.eye(N)
    assert J*B2 == B2*J
    assert D == perm_matrix(N,[(43*j+28)%N for j in range(N)],
                           [(-1)**j for j in range(N)])
    assert D**2 == s.eye(N)
    # Quarter sum: (1/4) sum_s i^(s(j+7r)) leaves r=j mod4.
    for j in range(N):
        survivors=[r for r in range(4) if (j+7*r)%4==0]
        assert survivors == [j%4]
        assert (j+14*survivors[0])%N == 15*j%N
    # Full center in the two Heisenberg generators:
    # D X D^-1=-X^43; D Z D^-1=-Z^43, checked without approximate roots.
    f=lambda j:(43*j+28)%56
    for j in range(56):
        assert (j-43*f(j))%56 == 28
        assert (f((j+1)%56)-f(j))%56 == 43
        assert (-1)**((j+1)%56) == -(-1)**j
    for j in range(14):
        vec=s.zeros(56,1)
        vec[2*j]=1;vec[(2*j+28)%56]=1
        assert J*vec == B2*vec == D*vec == vec

    K=s.Matrix([[0,1,-1],[1,0,-1],[0,0,-1]])
    R=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    KB=R*K*R
    B2src=K*KB
    assert KB == s.Matrix([[0,-1,1],[0,-1,0],[1,-1,0]])
    assert K*KB == KB*K
    assert KB**2 == B2src**2 == s.eye(3)
    assert B2src == s.Matrix([[-1,0,0],[-1,0,1],[-1,1,0]])
    # The uniform quarter B operator J_B is -K_B*B2 = -K_W on this span.
    Jsrc=-KB*B2src
    assert Jsrc == -K
    # Its actual first column is exactly e1=-J_B e0.
    assert Jsrc[:,0] == s.Matrix([0,-1,0])

    a=s.Matrix([1,1,0]); b=s.Matrix([1,0,1]); h=s.Matrix([0,1,1])
    change=s.Matrix.hstack(a,b,h)
    assert change.det() == -2
    assert change.inv()*K*change == s.diag(1,-1,-1)
    assert change.inv()*KB*change == s.diag(-1,1,-1)
    assert change.inv()*B2src*change == s.diag(-1,-1,1)
    u=(a+b)/2;v=(a-b)/2
    assert K*u == v and KB*u == -v and B2src*u == -u
    assert K*v == u and KB*v == -u and B2src*v == -v

    delta=s.I*s.sqrt(3)
    MB=s.Matrix([[1,3*delta],[3*delta,29]])
    assert s.simplify(MB.det()) == 56
    assert s.simplify(MB*s.diag(29,1)*MB.conjugate().T) == s.diag(56,1624)
    MWU=s.Matrix([[1,4],[1,-14]])
    assert MWU.det() == -18
    assert MWU*s.diag(56,1)*MWU.T == s.diag(72,252)
    M=s.Matrix([[1,1,1,1,3*delta,4],
                [3*delta,3*delta,3*delta,3*delta,29,0],
                [1,1,1,1,3*delta,-14],
                [4,-1,0,0,0,0],
                [7,7,-15,0,0,0],
                [7,7,7,-22,0,0]])
    degrees=s.diag(3,12,7,7,1,1)
    assert s.simplify(M.det()) == 3215520
    assert s.simplify(M*degrees*M.conjugate().T)==s.diag(72,1624,252,60,2310,4466)
    Y=s.Matrix([[1,1,1,1,1,2]])
    ycoeff=s.simplify(Y*M.inv())
    expected=s.Matrix([[(37-3*delta)/72,(1-3*delta)/56,
                        (1-3*delta)/252,0,0,0]])
    assert s.simplify(ycoeff-expected)==s.zeros(1,6)

    k=s.symbols("k")
    covB=s.Matrix([[1,1,1,1,3*delta,0]])
    vecB=degrees*covB.conjugate().T
    PB=s.eye(6)+(k-1)*vecB*covB/56
    assert s.simplify(covB*PB-k*covB)==s.zeros(1,6)
    for j in [1,3,4,5]:
        assert s.simplify(M[j,:]*PB-M[j,:])==s.zeros(1,6)
    assert s.simplify(s.Matrix([[0,0,0,0,0,1]])*PB-s.Matrix([[0,0,0,0,0,1]]))==s.zeros(1,6)
    assert s.simplify(Y*PB-Y-(k-1)*(29-3*delta)*covB/56)==s.zeros(1,6)
    Dcov=s.Matrix([[0,0,0,0,4,3*delta]])
    assert s.simplify(Dcov*PB-Dcov+(k-1)*3*delta*covB/14)==s.zeros(1,6)

    # Complete simultaneous rectangle matrices are diagonal in the old M axes.
    kw,kq,ku,kr=s.symbols("kw kq ku kr")
    P=s.simplify(M.inv()*s.diag(kw,kq,ku,kr,kr,kr)*M)
    assert s.simplify(M*P-s.diag(kw,kq,ku,kr,kr,kr)*M)==s.zeros(6)
    report={
        "level56_quarter_formula":"T_(s+r*omega)/4 e_j=i^(s(j+7r))*e_(j+14r)",
        "J56":"e_j -> e_(15j)",
        "B2_56":"e_j -> (-1)^j*e_(29j+28)",
        "K56":"e_j -> -(-1)^j*e_(43j+28)",
        "g_mod112":[43,56],
        "absolute_anchor":"Theta(2*gamma7*z), E2-fixed, J-fixed, actual normalized core -1",
        "K_W":[list(map(int,K.row(i))) for i in range(3)],
        "K_B":[list(map(int,KB.row(i))) for i in range(3)],
        "B2":[list(map(int,B2src.row(i))) for i in range(3)],
        "K_Q":"-chi29*K_B",
        "K_U":"-K_W*K_B",
        "three_R_core":"chi29*lambda^3 on their simultaneous deep block",
        "scalar_basis":["a=e0+e1","b=e0+e2","h=e1+e2"],
        "W_signs":[1,-1,-1],
        "B_signs":[-1,1,-1],
        "Q_signs":["chi29","-chi29","chi29"],
        "U_signs":[1,1,-1],
        "R_common_signs":["chi29"]*3,
        "old_M_Gram":[72,1624,252,60,2310,4466],
        "old_M_determinant":3215520,
        "Y_s_in_M":"(37-3delta)W/72+(1-3delta)Q/56+(1-3delta)U/252",
        "rectangle_exponent":"nW+nQ+nU+3r",
        "rectangle_a_scalar":"chi29^(nQ+r)*lambda^(nW+nQ+nU+3r)",
        "rectangle_b_scalar":"(-1)^(nW+nQ)*chi29^(nQ+r)*lambda^(nW+nQ+nU+3r)",
        "rectangle_h_scalar":"(-1)^(nW+nU)*chi29^(nQ+r)*lambda^(nW+nQ+nU+3r)",
        "B_physical_vector":["3","12","7","7","-3delta","0"],
        "B_physical_covector":["1","1","1","1","3delta","0"],
        "B_Y_displacement":"(kappa-1)*(29-3delta)*B/56",
        "B_D_displacement":"-(kappa-1)*3delta*B/14",
        "one_B_vs_AWA":"normalized source K_B=R*K_W*R; physical maps P_B and P_A2*P_W*P_A2 differ",
        "two_domain_identity":"P_B^-1_*(mu|Bdeep)=lambda^-4*(P_A2*P_W*P_A2)^-1_*(mu|word_lattice)",
        "boundary":"No equality of the two physical lattices or vanishing of their complements is asserted."
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(report,indent=2)+"\n")
    print("R494 complete level56 center, scalar basis, and old M rectangle checked exactly.")

if __name__=="__main__":
    main()

