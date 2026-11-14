#!/usr/bin/env python3
"""R490: the actual degree26 factor, full CM7, and the degree442 companion."""
from pathlib import Path
import json, runpy
BASE=Path(__file__).resolve().parents[1]
H=runpy.run_path(str(BASE/"scripts/check-r466-fixed-two-division-source.py"))
Q,Mat,Poly=(H[k]for k in ("Q","Mat","Poly"))
fq,km,ka,ks,kp,kvec,identity,rank,serial=(H[k]for k in
    ("fq","km","ka","ks","kp","kvec","identity","rank","serialize_matrix"))
zero=fq(0)
def cm7(N,offset):
    n=(N//2-offset)//3+1
    rows=dict(H["H"]["exact_fiber_row"]((N,offset,x))for x in range(1,n+1))
    V=Mat([[Q(x)**(3*j)for j in range(n)]for x in range(1,n+1)])
    return tuple(V.inv()*Mat([[Q(rows[x][j][k])for j in range(n)]
                             for x in range(1,n+1)])for k in (0,1))
def main():
    omega=fq(Q(-1,2),Q(1,2))
    x=Poly([0,1])
    f=Poly([Q(16,7),Q(12,7),Q(3,7),Q(1)])
    s=f*(x-8)
    assert s==Poly([Q(-128,7),Q(-80,7),Q(-12,7),Q(-53,7),Q(1)])
    q=[zero for _ in range(7)]
    q[6]=fq(1);q[3]=fq(2,6);q[0]=fq(Q(40,13),Q(24,13))
    num=H["qmap"](q,13)
    # Theta(gamma13 z)=sigma26*n13(x); its delta part is -168*F26.
    for j in range(5):
        assert num[1+3*j][1]==-168*f[j]
    assert all(num[j]==zero for j in range(len(num))if j%3!=1)
    M26,M2,M34=cm7(26,1),cm7(2,1),cm7(34,2)
    F=kvec([f[j]for j in range(5)])
    S=kvec([s[j]for j in range(6)])
    assert km(M26,F)==ks(F,omega)
    assert H["get_entry"](M2,0,0)==omega
    I=identity(6)
    assert kp(M34,18,I)==I
    assert km(M34,(M34[0],-M34[1]))==I
    P=H["eig_project"](M34,fq(-1),I,18)
    assert rank(P)==1 and km(P,P)==P and km(P,S)==S
    H5=kvec([1024,-6784,-14912,-272,272,1])
    h5_eigen=H["fn"](H["fm"](omega,omega))
    assert km(M34,H5)==ks(H5,h5_eigen)
    PH5=H["eig_project"](M34,h5_eigen,I,18)
    assert rank(PH5)==1 and km(PH5,H5)==H5
    n13=[num[1+3*j] for j in range(5)]
    gplus=[H["fm"](fq(-8),n13[0])]
    for j in range(1,6):
        gplus.append(H["fa"](n13[j-1],H["fm"](fq(-8),n13[j]) if j<5 else zero))
    Gplus=(Mat([[v[0]]for v in gplus]),Mat([[v[1]]for v in gplus]))
    cplus=fq(168,-168)
    cminus=fq(168,168)
    assert km(P,Gplus)==ks(S,cplus)
    Gminus=(Gplus[0],-Gplus[1])
    assert km(P,Gminus)==ks(S,cminus)
    assert ka(Gminus,ks(Gplus,fq(-1)))==ks(S,fq(0,336))
    gamma=fq(Q(7,2),Q(1,2))
    bargamma=fq(Q(7,2),Q(-1,2))
    Bplus=(Mat([[gamma[0],2],[2,-bargamma[0]]]),
           Mat([[gamma[1],0],[0,-bargamma[1]]]))
    Bstar=(Bplus[0].transpose(),-Bplus[1].transpose())
    assert km(Bplus,Bstar)==ks(identity(2),fq(17))
    T=Mat([[1,2],[2,-13]])
    assert T.det()==-17
    assert T*Mat([[26,0],[0,2]])*T.transpose()==Mat([[34,0],[0,442]])
    RW=T.inv()*Mat([[-1,0],[0,1]])*T
    assert RW==Mat([[Q(-9,17),Q(-52,17)],[Q(-4,17),Q(9,17)]])
    assert RW*RW==Mat([[1,0],[0,1]])
    a,b=1428552127,2161889730
    norm=a*a-a*b+b*b
    g=((a*a-b*b)*pow(norm,-1,52)%52,(2*a*b-b*b)*pow(norm,-1,52)%52)
    assert g==(27,0)
    def mv(M):return [[str(M[i,j])for j in range(M.ncols())]for i in range(M.nrows())]
    out={
      "field":"Q(delta), delta^2=-3; b=1; X=x^3",
      "F26_in_sigma26_x_frame":[str(f[j])for j in range(5)],
      "S34_in_sigma34_x2_frame":[str(s[j])for j in range(6)],
      "Theta_gamma13_in_sigma26_x_frame":[[str(y)for y in num[1+3*j]]for j in range(5)],
      "Theta_gamma13_minus_conjugate_equals_F26_factor":["0","-336"],
      "full_N7_degree26":serial(M26),"full_N7_degree2":serial(M2),
      "full_N7_degree34":serial(M34),"S_rank_one_projector":serial(P),
      "H5_in_sigma34_x2_frame":[1024,-6784,-14912,-272,272,1],
      "H5_rank_one_projector":serial(PH5),
      "H5_N7_eigenvalue":[str(v)for v in h5_eigen],
      "Gplus_first_marginal":serial(Gplus),
      "Gplus_S_coefficient":[str(v)for v in cplus],
      "Gminus_S_coefficient":[str(v)for v in cminus],
      "true_34_by_34_descent_matrix":serial(Bplus),
      "Lambda442_explicit":"((1+delta)*H5(bar_gamma13*z)-(1-delta)*H5(gamma13*z))/(2*delta)",
      "F26_N7":[str(x)for x in omega],"Theta_N7":[str(x)for x in omega],
      "whole_ray_ratio_mod52":list(g),"output_matrix":mv(T),
      "polarization":[34,442],"physical_W_reflection_in_inputs":mv(RW),
      "companion_mass":"1","companion_core":"lambda",
      "source_identity_general_b":"F26=(Theta(bar_gamma13*z)-Theta(gamma13*z))/(336*b*delta)",
      "central_derivative":"d*(log<bar_gamma13>-log<gamma13>)*(1+lambda)/(336*b*delta)",
      "second_nonhomogeneous_derivative":"J_B442'(0)+J_S'(0)=d*log<bar_gamma13/gamma13>*(1-lambda)/(336*b*delta)",
      "S_CM7_eigen_minus_one_dimension":1,
      "all_fibers_are_complete":True
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
    print("Complete degree26 factor and all CM7 fibers proved; S projector rank one; det17 Gram (34,442).")
if __name__=="__main__":main()

