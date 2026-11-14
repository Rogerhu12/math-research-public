#!/usr/bin/env python3
"""R282 fixed CM5 orbit of the actual R277 odd primitive. No target-prime scan."""
import json
from pathlib import Path
import sympy as s
from flint import fmpq,fmpq_mat
root=Path(__file__).parent
base=json.loads((root/"check-ray17-conjugate-trace-and-yang-projection.json").read_text())
new=json.loads((root/"check-original-three-ordinary-adjoint.json").read_text())
def fq(x):return fmpq(str(x))
def pair(z):
    z=s.expand(s.sympify(z))
    return fq(s.re(z)),fq(s.im(z))
Nre=fmpq_mat(17,17);Nim=fmpq_mat(17,17)
for col in range(17):
    for row in range(17):
        a,b=pair(base["CM5_matrix_columns"][col][row])
        Nre[row,col]=(2*a+b)/5
        Nim[row,col]=(2*b-a)/5
def cmul(A,B,x,y): return A*x-B*y,A*y+B*x
def serial(x,y):return [[str(x[i,0]),str(y[i,0])] for i in range(17)]
coeffs=[s.Rational(z) for z in new["branch_regular_RH_coefficients"]]
assert len(coeffs)==17
vr=fmpq_mat(17,1,[fq(x) for x in coeffs[::-1]])
vi=fmpq_mat(17,1)
orbit=[]
x,y=vr,vi
for j in range(16):
    orbit.append((x,y))
    x,y=cmul(Nre,Nim,x,y)
assert x==vr and y==vi
realblock=fmpq_mat(34,32)
for j,(x,y) in enumerate(orbit):
    for n in range(17):
        realblock[n,j]=x[n,0]
        realblock[n+17,j]=y[n,0]
        realblock[n,j+16]=-y[n,0]
        realblock[n+17,j+16]=x[n,0]
rank=realblock.rank()
assert rank==32
rr,rrank=realblock.transpose().rref()
rows=[]
for n in range(rrank):
    rows.append(next(j for j in range(34) if rr[n,j]))
minor=fmpq_mat(32,32,[realblock[i,j] for i in rows for j in range(32)])
det=minor.det()
assert det
def project_quartic(k):
    x=fmpq_mat(17,1);y=fmpq_mat(17,1)
    for j,(a,b) in enumerate(orbit):
        phase=(-k*j)%4
        if phase==0:x+=a;y+=b
        elif phase==1:x-=b;y+=a
        elif phase==2:x-=a;y-=b
        else:x+=b;y-=a
    return x/16,y/16
proj=[project_quartic(k) for k in range(4)]
scalars={}
for k,key,pos in [(1,"1",15),(2,"2",16),(3,"3",16)]:
    a,b=proj[k]
    scalar_a,scalar_b=a[pos,0],b[pos,0]
    reference=[fq(z) for z in base["normalized_primitive_polynomials"][key]]
    assert all(a[i,0]==scalar_a*reference[i] and b[i,0]==scalar_b*reference[i] for i in range(17))
    scalars[key]=[str(scalar_a),str(scalar_b)]
resr=vr;resi=vi
for a,b in proj:resr-=a;resi-=b
assert any(resr[i,0] or resi[i,0] for i in range(17))
# The actual two CM17 polynomials are Q_beta(U)^2 D_beta(U).
U=s.symbols("U");I=s.I
Q=U**4+(12-20*I)*U**3+(-10+28*I)*U**2+(-20-12*I)*U+(1+4*I)
D=sum(s.sympify(z)*U**j for j,z in enumerate(base["D_beta"]))
CM=s.Poly(s.expand(Q**2*D),U)
cm=[pair(CM.nth(j)) for j in range(17)]
# P0=a CM+b barCM; use coefficient 16 (=1), and a nonreal coefficient.
x0,y0=proj[0]
sumr,sumi=x0[16,0],y0[16,0]
j0=next(j for j,(a,b) in enumerate(cm) if b)
cr,ci=cm[j0]
# x0[j]= (a+b) cr+i(a-b)ci.
diffr=(y0[j0,0]-sumi*cr)/ci
diffi=-(x0[j0,0]-sumr*cr)/ci
ar,ai=(sumr+diffr)/2,(sumi+diffi)/2
br,bi=(sumr-diffr)/2,(sumi-diffi)/2
for j,(cr,ci) in enumerate(cm):
    assert x0[j,0]==(ar+br)*cr+(-ai+bi)*ci
    assert y0[j,0]==(ai+bi)*cr+(ar-br)*ci
out={
 "status":"PASS",
 "scope":"Fixed actual R277 P_R; exact rational/Gaussian CM5 orbit, no target-prime scan.",
 "input_P_R_ascending":[str(z) for z in coeffs[::-1]],
 "N_order_16_on_input":True,
 "complex_krylov_rank":rank//2,
 "full_character_support":"All sixteen CM5 eigencharacters have nonzero projection; rank-two eigenvalue 1 contributes one input projection.",
 "real_rank_certificate_rows":rows,
 "real_rank_certificate_determinant":str(det),
 "CM_beta_coefficient":[str(ar),str(ai)],
 "CM_barbeta_coefficient":[str(br),str(bi)],
 "primitive_coefficients_H_S2312_S39304":scalars,
 "extra_twelve_character_remainder":serial(resr,resi)
}
outp=Path(__file__).with_suffix(".json")
outp.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","complex_rank":rank//2,"bytes":outp.stat().st_size,
                 "primitive_coefficients":scalars,
                 "CM_beta":[str(ar),str(ai)],"CM_barbeta":[str(br),str(bi)]},indent=2))

