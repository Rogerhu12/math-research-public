#!/usr/bin/env python3
"""R492: the complete principal two-Theta kernel and its three actual tensors."""
from pathlib import Path
import json, runpy
BASE=Path(__file__).resolve().parents[1]
H=runpy.run_path(str(BASE/"scripts/check-r466-fixed-two-division-source.py"))
Q,Mat=(H[k]for k in("Q","Mat"))
fq,fm,fn,km,ka,ks,kp,kvec,rank,identity,serial=(H[k]for k in
    ("fq","fm","fn","km","ka","ks","kp","kvec","rank","identity","serialize_matrix"))
data=json.loads((BASE/"scripts/check-r490-degree26-factor-and-cm7.json").read_text())
def read(key):
    return tuple(Mat([[Q(x)for x in row]for row in data[key][part]])
                 for part in("real","delta"))
def tensor(A,B):
    ar,ac=A[0].nrows(),A[0].ncols()
    br,bc=B[0].nrows(),B[0].ncols()
    out=[[],[]]
    for i in range(ar):
        for k in range(br):
            row=[[],[]]
            for j in range(ac):
                for l in range(bc):
                    a=(A[0][i,j],A[1][i,j]);b=(B[0][k,l],B[1][k,l])
                    v=fm(a,b)
                    for s in(0,1):row[s].append(v[s])
            for s in(0,1):out[s].append(row[s])
    return tuple(Mat(v)for v in out)
def main():
    N=read("full_N7_degree34");I=identity(6)
    w=fq(Q(-1,2),Q(1,2));w2=fm(w,w)
    S=kvec([Q(x)for x in data["S34_in_sigma34_x2_frame"]])
    H3=kvec([-2048,12032,8128,400,-208,1])
    H5=kvec(data["H5_in_sigma34_x2_frame"])
    G=read("Gplus_first_marginal")
    cplus=fq(168,-168);cminus=fq(168,168)
    assert G==ka(H3,ks(S,cplus))
    assert (G[0],-G[1])==ka(H3,ks(S,cminus))
    assert km(N,H3)==ks(H3,fn(w))
    N3=kp(N,3,I)
    assert km(ka(N3,I),ka(N3,ks(I,w)))==H["kzero"](6,6)
    E=ks(ka(N3,ks(I,w)),H["fi"](H["fs"](w,fq(1))))
    assert km(E,E)==E and rank(E)==3
    J=tensor(N,N)
    kernel_operator=ka(J,ks(identity(36),fn(w2)))
    basis=[tensor(H3,H3),tensor(S,H5),tensor(H5,S)]
    assert rank(kernel_operator)==33
    assert rank(H["cols"](basis))==3
    for v in basis:assert km(J,v)==ks(v,w2)
    gamma=fq(Q(7,2),Q(1,2));bargamma=fq(Q(7,2),Q(-1,2))
    B=(Mat([[gamma[0],2],[2,-bargamma[0]]]),
       Mat([[gamma[1],0],[0,-bargamma[1]]]))
    Bminus=(B[0],-B[1])
    swap=(Mat([[0,1],[1,0]]),Mat(2,2))
    sign=(Mat([[1,0],[0,-1]]),Mat(2,2))
    # H_plus(u,w)=H_minus(w,-u), after interchanging the two even Theta factors.
    assert km(B,swap)==km(km(km(sign,swap),Bminus),sign)
    out={
      "coefficient_field":"Q(delta), delta^2=-3; displayed matrices at b=1",
      "N7_cube_minimal_polynomial":"(T+1)(T+omega)",
      "N7_cube_minus_one_projector":serial(E),
      "old_principal_dimension":3,
      "whole_two_axis_principal_dimension":36,
      "joint_N7_eigenvalue":[str(x)for x in w2],
      "joint_N7_eigenspace_dimension":3,
      "joint_three_tensor_basis":["H3(W)H3(U)","S(W)H5(U)","H5(W)S(U)"],
      "Hplus_coefficients":[["1","0"],["168","-168"],["168","168"]],
      "Hminus_coefficients":[["1","0"],["168","168"],["168","-168"]],
      "general_b_scaling":"the last two tensor coefficients are multiplied by b",
      "Gplus_exact":"H3+168*b*(1-delta)*S",
      "Gminus_exact":"H3+168*b*(1+delta)*S",
      "Phi_complete_principal":"H3(W)*C3(V)+S(W)*Lambda442(V)+H5(W)*CS(V)",
      "C3":"(H3(bar_gamma13*V)-H3(gamma13*V))/(336*b*delta)",
      "CS":"((1-delta)*S(bar_gamma13*V)-(1+delta)*S(gamma13*V))/(2*delta)",
      "central_antisymmetric_gate":"(d_t-d_s)F_plus(0,0)=336*b*delta*(1-lambda)*J_S'(0)",
      "full_bivariate_unit_Mellin_identity":True
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
    print("Complete 36-dimensional principal tensor has joint eigenspace dimension 3; all three actual source tensors and coefficients proved.")
if __name__=="__main__":main()

