#!/usr/bin/env python3
"""R497: complete S34 positive-moment frame for the actual degree27+1 source."""
from pathlib import Path
from math import comb, factorial, lcm
import json
import runpy

BASE=Path(__file__).resolve().parents[1]
H=runpy.run_path(str(BASE/"scripts/check-r466-fixed-two-division-source.py"))
Q,Mat=(H[x]for x in ["Q","Mat"])
fq,fa,fs,fm,fi,fp=(H[x]for x in ["fq","fa","fs","fm","fi","fp"])
km,ka,ks,kinv=(H[x]for x in ["km","ka","ks","kinv"])
serialize=H["serialize_matrix"]
ZERO,ONE=fq(0),fq(1)
length=12

def rsum(xs):
    out=Q(0)
    for x in xs:out+=x
    return out
def fsum(xs):
    out=ZERO
    for x in xs:out=fa(out,x)
    return out
def multiply(a,b):
    out=[Q(0)]*length
    for i,x in enumerate(a):
        for j,y in enumerate(b[:length-i]):out[i+j]+=x*y
    return out
def power(a,n):
    out=[Q(1)]+[Q(0)]*(length-1)
    for _ in range(n):out=multiply(out,a)
    return out
def encode_scalar(x):return [str(a)for a in x]
def matrix(xs):
    return tuple(Mat([[x[k]for x in row]for row in xs])for k in [0,1])
def det(A):
    n=A[0].nrows()
    rows=[[H["get_entry"](A,i,j)for j in range(n)]for i in range(n)]
    ans=ONE
    for j in range(n):
        r=next(r for r in range(j,n)if rows[r][j]!=ZERO)
        if r!=j:rows[r],rows[j]=rows[j],rows[r];ans=fm(ans,fq(-1))
        pivot=rows[j][j];ans=fm(ans,pivot)
        for i in range(j+1,n):
            scale=fm(rows[i][j],fi(pivot))
            for k in range(j,n):rows[i][k]=fs(rows[i][k],fm(scale,rows[j][k]))
    return ans

q=[Q(0)]*length;q[0],q[1]=Q(1),Q(-1,7)
for n in range(2,length):
    q[n]=rsum(q[i]*q[n-i]for i in range(1,n))/((6*n+1)*(n-1))
log_a=[Q(0)]+[-q[n]/(6*n*(6*n-1))for n in range(1,length)]
a=[Q(0)]*length;a[0]=Q(1)
for n in range(1,length):
    a[n]=rsum(k*log_a[k]*a[n-k]for k in range(1,n+1))/n
ps=[Q(-128,7),Q(-80,7),Q(-12,7),Q(-53,7),Q(1)]
a34=power(a,34)
qpow={j:power(q,j)for j in [2,5,8,11,14,17]}
basis={j:multiply(a34,qpow[2+3*j])for j in range(6)}
J=Mat([[Q(0)if ell-5+j<0 else basis[j][ell-5+j]
        for j in range(6)]for ell in range(6)])
assert J.det()==-1
S=[Q(0)]*length
for j in range(5):
    for n in range(4-j,length):S[n]+=ps[j]*basis[j][n-4+j]
assert S[0]==1

gamma=fq(Q(5,2),Q(1,2));barg=fq(Q(5,2),Q(-1,2))
gamma6,barg6=fp(gamma,6),fp(barg,6)
assert fm(gamma,barg)==fq(7)
# B27(z)=z^5/bar(gamma) * S_series(z^6)/A(bar(gamma)^6 z^6).
h=[ZERO]*length
for n in range(length):
    h[n]=fs(fq(S[n]),fsum(fm(fq(a[i]),fm(fp(barg6,i),h[n-i]))
                          for i in range(1,n+1)))
assert h[0]==ONE

def moment_jet(k,ell):
    total=ZERO
    for i in range(length):
        j=k+ell-1-i
        if not 0<=j<length:continue
        r,s=1+6*i,5+6*j
        collision=rsum(Q(comb(r,v)*comb(s,6*k-v)*(-27)**v,7**v)
                       for v in range(max(0,6*k-s),min(r,6*k)+1))
        term=fm(fq(a[i]*collision),fm(h[j],fp(barg6,i)))
        total=fa(total,term)
    return fm(fq(factorial(6*k)),fm(fp(gamma6,k),total))

V=matrix([[moment_jet(k,ell)for k in range(7)]for ell in range(6)])
M=km((J.inv(),Mat(6,6)),V)
target=matrix([[fq(x)]for x in ps+[Q(0)]])
assert H["column"](M,0)==target
positive=tuple(Mat([[M[c][i,j]for j in range(1,7)]for i in range(6)])
               for c in [0,1])
determinant=det(positive)
assert determinant!=ZERO
coeff=km(kinv(positive),target)
assert km(positive,coeff)==target

alpha=ZERO
nonlog,logcoeff=[],[]
for k in range(1,7):
    m=6*k;c=H["get_entry"](coeff,k-1,0)
    collision=rsum(Q((-1)**(r-1)*comb(m,5-r)*(-27)**(m-5+r),r*7**r)
                   for r in range(1,6))
    Ak=fm(fp(gamma,5),fq(collision))
    Bk=fm(fp(gamma,5),fq(comb(m,5)*(-27)**(m-5)))
    fac=fm(fq(120),fm(fi(barg),c))
    aa=fm(fac,Ak);bb=fm(fac,Bk)
    nonlog.append(aa);logcoeff.append(bb)
    alpha=fa(alpha,fm(aa,fq(factorial(m-5)*a[k-1])))
assert alpha!=ZERO
alpha_norm=alpha[0]**2+3*alpha[1]**2
assert alpha_norm>0
den=1
for i in range(6):
    for c in H["get_entry"](coeff,i,0):den=lcm(den,int(c.denominator))
test_denominator=den
assert all(H["get_entry"](coeff,i,0)[1]==0 for i in range(6))
test_numerators=[int(H["get_entry"](coeff,i,0)[0]*test_denominator)
                 for i in range(6)]
alpha_denominator=lcm(*[int(c.denominator)for c in alpha])
alpha_numerators=[int(c*alpha_denominator)for c in alpha]
den=lcm(den,alpha_denominator)
bad=17*test_denominator*alpha_denominator*(
    alpha_numerators[0]**2+3*alpha_numerators[1]**2)
def mod101(x):return int(x.numerator)*pow(int(x.denominator),-1,101)%101
det101=[mod101(x)for x in determinant]
assert det101!=[0,0]

transport=json.loads((BASE/"scripts/check-r493-original-half-torsion-six-sigma-factor.json").read_text())
def decode_entry(A,i,j):return fq(Q(A["real"][i][j]),Q(A["delta"][i][j]))
wp=[decode_entry(transport["W_prime"],0,i)for i in [0,1,2,4,5]]
def conjugate(x):return (x[0],-x[1])
shifts=[]
for i in range(5):
    row=[decode_entry(transport["Z27_full_frame"],i,j)for j in range(5)]
    shifts.append(fsum(fm(x,conjugate(y))for x,y in zip(row,wp)))
assert shifts==[fq(37,-3),fq(12,8),fq(6,74),fq(-40,20),fq(-68,-12)]

out={
 "field":"Q(delta), delta^2=-3; gamma=(5+delta)/2",
 "source":"B27(y+gamma*t)*sigma(bar(gamma)*y-27*t), B27=S/sigma(bar(gamma)*z)",
 "degrees":[34,918],
 "rows":"sigma^34*x^(2+3a), a=0..5",
 "columns":"(Tc/Omega)^(6k), k=0..6, all factorials included",
 "b_scaling":"column k row a is b^(k+4-a) times b=1 entry",
 "sigma_A":[str(x)for x in a],"x_B":[str(x)for x in q],
 "S_series":[str(x)for x in S],"B27_H":[encode_scalar(x)for x in h],
 "jet_basis":[[str(J[i,j])for j in range(6)]for i in range(6)],
 "moment_matrix":serialize(M),"positive_determinant":encode_scalar(determinant),
 "positive_determinant_mod101":det101,
 "test_coefficients":serialize(coeff),
 "test_common_denominator":str(test_denominator),
 "test_numerators":test_numerators,
 "fifth_nonlog_coefficients":[encode_scalar(x)for x in nonlog],
 "fifth_log_coefficients":[encode_scalar(x)for x in logcoeff],
 "fifth_residue_alpha":encode_scalar(alpha),"fifth_residue_norm":str(alpha_norm),
 "fifth_residue_common_denominator":str(alpha_denominator),
 "fifth_residue_numerators":alpha_numerators,
 "common_denominator":str(den),"fixed_bad_integer":str(bad),
 "test":"sum_{k=1}^6 c_k*b^(-k)*(Tc/Omega)^(6k)",
 "unit_test":"replace c_k by c_k/(1-lambda*kappa^(6k))",
 "whole_Y_source":"S",
 "whole_Tc_core":"lambda*R_Y, preserving all four original five-sigma companions",
 "four_companion_common_core":"lambda^4, preserving Y and Tc",
 "complete_fifth_jet":"d sum b^-k Omega^(5-6k) [alpha_k I_(6k-5)+beta_k (I_(6k-5),log+log<bar(gamma)> I_(6k-5))]",
 "unit_fifth_residue":"(d/b)*alpha modulo p",
 "grid":"xi4 unit, original other five sigma inputs all in p^n",
 "grid_value":"beta^(5*n)*A(kappa^n), valuation 5*n outside fixed_bad_integer",
 "remaining_complement":"R_1,...,R_4 in p^n; Tc unit; Y unit; Z not in p^n"
 ,"W_core_shift_numerators_Y_R":[encode_scalar(x)for x in shifts]
 ,"W_core_shift_denominator":72
 ,"W_core_shift_Tc_numerator":encode_scalar(fm(gamma,shifts[0]))
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("Complete degree918 six-positive-moment extraction and fifth residue passed.")
print("det modulo 101:",det101)
print("alpha numerator lengths:",[len(str(x.numerator))for x in alpha])
