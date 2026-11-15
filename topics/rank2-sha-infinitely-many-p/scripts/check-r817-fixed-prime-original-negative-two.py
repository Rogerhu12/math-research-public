#!/usr/bin/env python3
"""R817: a single fixed-prime detector for the three original B4 negative-two moments.

Public execution only. Fixed p=7993 and pi0=69-32*omega; no prime search,
no saved numerical outputs as inputs, no change of target if a moment is zero.
Rebuilds the complete R798/R732 CM13 operator and canonical B4 projector.
Dependencies: python-flint==0.9.0. Parameters: --workers=4 (default).
All generated coefficient arrays stay in memory; stdout is a small certificate.
"""
from __future__ import annotations
import concurrent.futures, hashlib, importlib.util, json, math, pathlib, sys

HERE=pathlib.Path(__file__).resolve().parent
HP=HERE/"check-r798-type-four-halfperiod-and-cm13.py"
spec=importlib.util.spec_from_file_location("r817_hp",HP)
hp=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=hp
spec.loader.exec_module(hp)

P=7993
BPAR=17
PI=(69,-32)
S=(P-1)//6
M=P-3
TOP=S-1

def prime_by_trial(n):
    if n<2:return False
    for d in range(2,math.isqrt(n)+1):
        if n%d==0:return False
    return True

def qmod(x):
    den=int(x.denominator)%P
    assert den, "A fixed exact coefficient has a p denominator"
    return int(x.numerator)%P*pow(den,-1,P)%P

def kmod(x):
    return (qmod(x[0])+OMEGA*qmod(x[1]))%P

def matmod(A):
    return [[kmod(x) for x in row] for row in A]

def mm(A,B):
    return [[sum(x*y for x,y in zip(row,col))%P for col in zip(*B)]
            for row in A]

def mv(A,v):
    return [sum(x*y for x,y in zip(row,v))%P for row in A]

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))%P

def conv(a,b,n):
    out=[0]*(n+1)
    for i,x in enumerate(a):
        if i>n:break
        if x:
            for j in range(min(len(b)-1,n-i)+1):
                out[i+j]+=x*b[j]
    return [v%P for v in out]

def sha(value):
    raw=json.dumps(value,separators=(",",":"),sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()

assert prime_by_trial(P), "The fixed detector is not prime; do not substitute another one"
assert P==PI[0]*PI[0]-PI[0]*PI[1]+PI[1]*PI[1]
assert P%6==1 and P%9==1
assert (PI[0]%2,PI[1]%2)==(1,0)
# pi0=1+2*delta*(-22-28*omega), delta=1+2*omega.
assert (1+2*(-22)-4*(-28),2*(-28)+4*(-22)-4*(-28))==PI
assert ((PI[0]-1)%17,(PI[1]-2)%17)==(0,0)
assert P%17==3
OMEGA=PI[0]*pow(-PI[1],-1,P)%P
assert (OMEGA*OMEGA+OMEGA+1)%P==0
assert (PI[0]+PI[1]*OMEGA)%P==0
assert math.gcd(P,2*3*5*7*13*17*19*34)==1

def rebuild_operator():
    with concurrent.futures.ProcessPoolExecutor(max_workers=hp.core.ARGS.workers) as ex:
        rows=dict(ex.map(hp.fiber,range(2,10)))
    A=hp.operator(rows,"type4",[3*j for j in range(6)],range(2,8),(8,9))
    assert hp.mm(A,hp.H4)==hp.mm(hp.H4,A)
    assert hp.mm(A,hp.PB4)==hp.mm(hp.PB4,A)
    assert hp.characteristic(A)==[hp.O,hp.Z,hp.Z,hp.neg(hp.O),hp.Z,hp.Z,hp.O]
    basis,restricted,piv=hp.restriction(A,hp.PB4)
    assert len(piv)==3
    assert hp.characteristic(restricted)==[hp.O,hp.Z,hp.Z,hp.W]
    assert hp.mpow(A,18)==hp.eye(6)
    return A

def actual_series():
    # w=b*z^6; x_b=z^-2*A(w), A_1=-1/7.
    # x''=6*x^2 gives
    # A_n=sum_{i=1}^{n-1}A_i*A_(n-i)/((n-1)*(6*n+1)).
    a=[0]*(TOP+1)
    a[0]=1
    a[1]=-pow(7,-1,P)%P
    for n in range(2,TOP+1):
        den=(n-1)*(6*n+1)%P
        assert den
        a[n]=sum(a[i]*a[n-i] for i in range(1,n))*pow(den,-1,P)%P
    # Check the actual y^2=x^3+b normalization to the full paid window.
    ab=[(1-3*n)*a[n]%P for n in range(TOP+1)]
    a2=conv(a,a,TOP)
    a3=conv(a2,a,TOP)
    rhs=a3[:]
    rhs[1]=(rhs[1]+1)%P
    assert conv(ab,ab,TOP)==rhs
    f=[0]*(TOP+1)
    for n in range(1,TOP+1):
        den=6*n*(6*n-1)%P
        assert den
        f[n]=-a[n]*pow(den,-1,P)%P
    # e=exp(34*F), F=log(sigma_b/z).
    e=[0]*(TOP+1)
    e[0]=1
    for n in range(1,TOP+1):
        e[n]=34*sum(k*f[k]*e[n-k] for k in range(1,n+1))*pow(n,-1,P)%P
    # Basis b^(5-j)*sigma_b^34*x_b^(3j), j=0,...,5.
    # [z^(p-3)] of every basis vector has the same b^(s-1) factor.
    row=[]
    power=[0]*(TOP+1)
    power[0]=1
    indices=[]
    for j in range(6):
        index=S-6+j
        assert 34-6*j+6*index==M
        indices.append(index)
        row.append(sum(e[k]*power[index-k] for k in range(index+1))%P)
        if j<5:power=conv(power,a3,TOP)
    fact=1
    for n in range(1,M+1):fact=fact*n%P
    scalar=fact*pow(BPAR,S-1,P)%P
    return row,scalar,{"A":sha(a),"F":sha(f),"exp34F":sha(e),
                      "basis_coefficient_indices":indices,
                      "last_A":a[-1],"last_F":f[-1],"last_exp34F":e[-1]}

def main():
    A_exact=rebuild_operator()
    A=matmod(A_exact)
    PB=matmod(hp.PB4)
    assert mm(PB,PB)==PB and mm(A,PB)==mm(PB,A)
    row,scalar,series_certificate=actual_series()
    zetas=[x for x in range(1,P) if pow(x,6,P)==OMEGA and pow(x,9,P)==P-1]
    assert len(zetas)==3
    zeta=min(zetas)
    assert pow(zeta,18,P)==1 and pow(zeta,6,P)==OMEGA
    A2=mm(A,A)
    q=[r[0] for r in PB]
    I=[[int(i==j) for j in range(6)] for i in range(6)]
    roots={4:pow(zeta,17,P),10:pow(zeta,11,P),16:pow(zeta,5,P)}
    entries=[]
    normalized_vectors=[]
    for label,mu in roots.items():
        assert (pow(mu,3,P)+OMEGA)%P==0
        invden=pow(3*mu*mu%P,-1,P)
        projector=[[(A2[i][j]+mu*A[i][j]+mu*mu*I[i][j])*invden%P
                    for j in range(6)] for i in range(6)]
        vector=mv(projector,q)
        assert mv(PB,vector)==vector
        assert mv(A,vector)==[mu*x%P for x in vector]
        lead=vector[5]
        item={"j":label,"CM13_eigenvalue":mu,
              "projected_Q0":vector,"z4_normalizer":lead}
        if lead:
            vector=[x*pow(lead,-1,P)%P for x in vector]
            reduced_coefficient=dot(row,vector)
            reduced_moment=scalar*reduced_coefficient%P
            item.update({"normalized_eigenvector_ascending":vector,
                         "coefficient_without_b_power":reduced_coefficient,
                         "negative_two_residue_div_Omega_pow_p_minus_3":reduced_moment,
                         "unit":bool(reduced_moment)})
            normalized_vectors.append(vector)
        else:
            item.update({"unit":False,"normalization_failure":True})
        entries.append(item)
    if len(normalized_vectors)==3:
        # The fixed three eigenlines really span the original B4 carrier.
        E=[list(x) for x in zip(*normalized_vectors)]
        assert len(hp.rref([[hp.K(x) for x in r] for r in E])[1])==3
    all_nonzero=all(x["unit"] for x in entries)
    report={
      "format":"R817 fixed original three negative-two moments",
      "status":"PASS" if all_nonzero else "NOT_ALL_FIXED_MOMENTS_CERTIFIED",
      "fixed_prime":P,"prime_verified_by_trial_division_through":math.isqrt(P),
      "pi0":PI,"primary_quotient_by_2delta":[-22,-28],
      "pi0_mod17":[1,2],"eta_values_at_p":"all -1 from the full R806 finite character",
      "omega_at_selected_prime":OMEGA,"zeta18":zeta,
      "b":BPAR,"s":S,"moment_exponent":M,"series_max_index":TOP,
      "basis":"b^(5-j)*sigma_b^34*x_b^(3j), j=0,...,5",
      "basis_reduced_coefficient_row":row,
      "factorial_times_b_power":scalar,
      "basis_negative_two_residue_row_div_Omega_pow_p_minus_3":[scalar*x%P for x in row],
      "B4_reduced_row":mv(list(map(list,zip(*PB))),row),
      "complete_exact_CM13_sha256":sha(hp.encode_matrix(A_exact)),
      "complete_exact_PB4_sha256":sha(hp.encode_matrix(hp.PB4)),
      "series_certificate":series_certificate,
      "three_actual_eigenlines":entries,
      "all_three_nonzero":all_nonzero,
      "unit_depletion":"On Zp^x, x^-2=x^(p-3) mod p; on pZp the positive moment lies in p^(p-3) O. The actual bounded measure and period are retained.",
      "period_scope":"Displayed residues mean Omega_p^(-(p-3))*I_(j,-2); Omega_p is a p-adic unit. No period is numerically substituted.",
      "input_sha256":{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest()
                      for x in (HP,hp.path)},
      "script_sha256":hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      "scope":"One fixed detector only. Does not infer nonvanishing at another prime, on the full original ray, or of an arbitrary native linear combination.",
      "outputs_persisted":False}
    output=json.dumps(report,separators=(",",":"),sort_keys=True)
    assert len(output.encode())<20000
    print(output)

if __name__=="__main__":main()
