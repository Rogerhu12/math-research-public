#!/usr/bin/env python3
"""R474: the actual degree72 source, two-output lattice, and Riemann maps."""
from pathlib import Path
import json
import runpy
from flint import fmpq as Q, fmpq_mat as Mat, fmpq_poly as Poly

base = Path(__file__).resolve().parents[1]
h = runpy.run_path(str(base/"scripts/check-r466-fixed-two-division-source.py"))
km, ka, ks, kp, fq, kvec, rank, cols, identity = [
    h[k] for k in ("km","ka","ks","kp","fq","kvec","rank","cols","identity")]
raw = json.loads((base/"notes/2026-11-14-literature-degree72-cm7-exact.json").read_text())
M = tuple(Mat([[Q(x) for x in row] for row in raw["matrix"][part]])
          for part in ("real","delta"))
I = identity(13)
assert kp(M,6,I) == I
data = json.loads((base/"scripts/check-r471-original-six-sigma-normtwo-factor.json").read_text())
v = kvec([Q(x) for x in data["six_sigma_in_sigma72_frame"]]+[Q(0)])
omega = fq(Q(-1,2),Q(1,2))
v1 = h["eig_project"](M,fq(1),v,6)
v2 = h["eig_project"](M,h["fp"](omega,2),v,6)
assert ka(v1,v2) == v
assert rank(cols([v,km(M,v)])) == 2
assert v1[0][12,0] == Q(1,6) and v2[0][12,0] == Q(-1,6)
assert v1[1] == Mat(13,1) and v2[1] == Mat(13,1)
assert km(kp(M,3,I),v) == v
assert h["eig_project"](M,fq(-1),v,6) == h["kzero"](13,1)
# Independent complete fiber for the degree4 principal line Theta^2.
_, tiny = h["H"]["exact_fiber_row"]((4,2,1))
assert tiny == [["1/2","-1/2"]]

T = Mat([[1,1],[8,-9]])
R = T.inv()*Mat([[-1,0],[0,1]])*T
assert R == Mat([[Q(-1,17),Q(-18,17)],[Q(-16,17),Q(1,17)]])
assert R*R == Mat([[1,0],[0,1]])
G = Mat([[72,0],[0,64]])
assert T*G*T.transpose() == Mat([[136,0],[0,9792]])
# The canonical B2 operator's exact signed permutation.
N = 136
B = Mat(N,N)
for j in range(N):
    B[((1+N//2)*j+N//2)%N,j] = (-1)**j
assert B*B == Mat([[int(i==j) for j in range(N)] for i in range(N)])
# Its four-E2-translation formula.
shift = Mat(N,N); sign = Mat(N,N)
for j in range(N):
    shift[(j+N//2)%N,j]=1; sign[j,j]=(-1)**j
IN = Mat([[int(i==j) for j in range(N)] for i in range(N)])
assert B == (IN+shift+sign+shift*sign)/2-IN

H = Mat([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])/2
J = Mat([[int(i==j)*(-1 if i==3 else 1) for j in range(4)]for i in range(4)])
a = Mat([[1],[1],[2],[8]])
assert H*H == Mat([[int(i==j)for j in range(4)]for i in range(4)])
assert H*a == Mat([[6],[-4],[-3],[3]])
assert H*J*a == Mat([[-2],[4],[5],[-5]])

X=Poly([0,1]);D=X**2+20*X-8
psi5=32*(X+1)**2*D-27*X*(X+4)**3
# Both six-sigma branches are expressed in the sigma^72 frame.
branchA = 216*X*(X+1)*(X+4)**3*D*(psi5-4*D**2)
branchB = 8*(X+1)*D*psi5**2
assert branchA-branchB == Poly([Q(x)for x in data["six_sigma_in_sigma72_frame"]])

out = {
    "F72_N7_eigen_one": [str(v1[0][j,0])for j in range(13)],
    "F72_N7_eigen_omega_squared": [str(v2[0][j,0])for j in range(13)],
    "F72_minus_one_projection_zero": True,
    "compressed_output_matrix": [[str(T[i,j])for j in range(2)]for i in range(2)],
    "physical_reflection": [[str(R[i,j])for j in range(2)]for i in range(2)],
    "polarization_degrees": [136,9792],
    "whole_B2_signed_permutation_verified": True,
    "riemann_sigma_coefficients": [[6,-4,-3,3],[-2,4,5,-5]],
    "riemann_full_polynomial_identity": True,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("Actual F72, full B2, both-output lattice, and Riemann branches passed.")

