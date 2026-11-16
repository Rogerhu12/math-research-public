#!/usr/bin/env sage-python
"""Exact original T9 Hecke equation and CM differential input; public Actions only."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("This mathematical producer runs only in the public repository Actions.")
import hashlib
import json
import math
import time
from pathlib import Path
from sage.all import ZZ, QQ, PolynomialRing, NumberField, GF
from sage.env import SAGE_VERSION

started = time.monotonic()
def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()
def progress(stage):
    print("RANK2_MODULAR_STAGE " + canonical({"stage":stage, "elapsed":time.monotonic()-started}), flush=True)
request = json.loads(Path("topics/rank2-sha-infinitely-many-p/ci/original-modular-input-request.json").read_text())
precision = int(request["cm_precision"])
prime = int(request["hecke_prime"])
assert prime == 17 and precision >= 541
faber_bound = prime*(prime+1)

progress("integer eta coefficients and Faber polynomials")
sigma1 = [ZZ(0)]*(faber_bound+1)
for d in range(1,faber_bound+1):
    for n in range(d,faber_bound+1,d):
        sigma1[n] += d
logder = [ZZ(0)]*(faber_bound+1)
for r in range(1,faber_bound+1):
    logder[r] = -3*sigma1[r] + (27*sigma1[r//9] if r%9 == 0 else 0)
eta = [ZZ(1)]
for n in range(1,faber_bound+1):
    numerator = sum((logder[r]*eta[n-r] for r in range(1,n+1)), ZZ(0))
    assert numerator%n == 0
    eta.append(numerator//n)
ZX = PolynomialRing(ZZ,"X")
X = ZX.gen()
bcoeff = [ZX(a) for a in eta]
bcoeff[1] -= X
faber = [ZX.zero()]
for m in range(1,faber_bound+1):
    fm = -m*bcoeff[m]
    for i in range(1,m):
        fm -= faber[i]*bcoeff[m-i]
    assert fm.degree() == m and fm.leading_coefficient() == 1
    faber.append(fm)

progress("exact eighteen-root Hecke equation")
Zq = PolynomialRing(ZZ,"q")
q = Zq.gen()
eta_short = Zq(eta[:19])
powersums = [ZX.zero()]
for k in range(1,19):
    apow = (eta_short**k).truncate(k+1)
    pk = ZX.zero()
    for n in range(-k,0):
        pk += apow[k+n]*faber[-17*n]
        if n%17 == 0:
            pk += 17*apow[k+n]*faber[-n//17]
    pk += 18*apow[k]
    powersums.append(pk)
elementary = [ZX.one()]
for m in range(1,19):
    num = ZX.zero()
    for k in range(1,m+1):
        num += (-1)**(k-1)*elementary[m-k]*powersums[k]
    assert all(ZZ(a)%m == 0 for a in num.list())
    em = ZX([ZZ(a)//m for a in num.list()])
    if m < 18:
        assert em.degree() <= 17
    elementary.append(em)
assert elementary[18] == X**18
assert -elementary[1].leading_coefficient() == -1
phi = {}
for m,em in enumerate(elementary):
    for i,a in enumerate(em.list()):
        if a:
            phi[(i,18-m)] = ZZ((-1)**m*a)
assert phi[(0,18)] == 1 and phi[(18,0)] == 1
assert phi[(17,17)] == -1
assert all(phi.get((j,i),0) == a for (i,j),a in phi.items())
assert all((j == 0 and i == 18) or j > 0 for (i,j) in phi)
phi_serial = [[i,j,str(phi[(i,j)])] for i,j in sorted(phi)]
phi_hash = digest(phi_serial)
phi_summary = {
    "bidegree":[max(i for i,j in phi),max(j for i,j in phi)],
    "total_degree":max(i+j for i,j in phi),
    "nonzero_terms":len(phi),
    "max_coefficient_bits":max(abs(a).nbits() for a in phi.values()),
    "symmetric":True,
    "constant_in_Y":"X^18",
    "coefficient_X17_Y17":"-1",
    "canonical_terms_sha256":phi_hash,
    "coefficient_convention":"sorted [X_degree,Y_degree,integer_as_string]",
    "eta_q_times_T_initial":[str(a) for a in eta[:19]]
}

progress("the fixed cubic field and original Artin generator")
ZT = PolynomialRing(QQ,"T")
T = ZT.gen()
K = NumberField(T**2+T+1,"omega")
omega = K.gen()
alpha = -1+2*omega
c = -1-19*omega
KV = PolynomialRing(K,"V")
V = KV.gen()
L = K.extension(V**3+367395*V**2+147*V+K(QQ(1)/17),"v")
v = L.gen()
ell = ((21905009-23122022*omega)
       +(112353990182+54575060764*omega)*v
       +(305813+148546*omega)*v**2)/25505280
tau_v = alpha**3*v/ell**3
def tau(z):
    co = L(z).list()
    return sum((L(co[i])*tau_v**i for i in range(len(co))), L.zero())
assert tau_v != v and tau(tau(tau_v)) == v
assert ell*tau(ell)*tau(tau(ell)) == c
u1 = tau(tau(ell))
u2 = L(c)/ell
assert u1 != 0 and u2 != 0

progress("complete original ideal coefficients, including the ideal (2)")
F17 = GF(17)
Fpol = PolynomialRing(F17,"W")
W = Fpol.gen()
F289 = GF(17**2,name="omega17",modulus=W**2+W+1)
omega17 = F289.gen()
alpha17 = -1+2*omega17
dlog = {}
power = F289.one()
for r in range(288):
    assert power not in dlog
    dlog[power] = r%9
    power *= alpha17
assert power == 1 and len(dlog) == 288 and dlog[F289(2)] == 0

fcoeff = [[K.zero(),K.zero(),K.zero()] for _ in range(precision+1)]
ideal_counts = [0]*(precision+1)
bound = math.isqrt((4*precision)//3)+2
for A in range(-bound,bound+1):
    for B in range(-bound,bound+1):
        norm = A*A-A*B+B*B
        if norm < 1 or norm > precision:
            continue
        orbit = [(A,B),(-B,A-B),(B-A,-A)]
        orbit += [(-a,-b) for a,b in orbit]
        assert len(set(orbit)) == 6
        if (A,B) != min(orbit):
            continue
        if (A+B)%3 == 0 or (A%17 == 0 and B%17 == 0):
            continue
        eps = 1 if (A+B)%3 == 1 else -1
        residue = F289(A)+F289(B)*omega17
        r = dlog[residue]
        fcoeff[norm][r%3] += eps*(A+B*omega)*c**(r//3)/alpha**r
        ideal_counts[norm] += 1
assert fcoeff[1] == [K.one(),K.zero(),K.zero()]
assert fcoeff[4] == [-K(2),K.zero(),K.zero()]
assert fcoeff[7] == [K.zero(),K.one(),K(7)/c]
assert all(all(a == 0 for a in fcoeff[n]) for n in range(precision+1) if n%3 != 1)

Hs = [[],[],[]]
for f0,f1,f2 in fcoeff:
    Hs[0].append(L(f0)+u1*f1+u2*f2)
    Hs[1].append(u1*f0+u2*f1+c*f2)
    Hs[2].append(u2*f0+c*f1+c*u1*f2)
assert [row[1] for row in Hs] == [L.one(),u1,u2]
assert [row[4] for row in Hs] == [-L(2),-2*u1,-2*u2]
def kcoords(z):
    co = K(z).list()
    return [str(QQ(co[i])) if i < len(co) else "0" for i in range(2)]
def lcoords(z):
    co = L(z).list()
    return [kcoords(co[i]) if i < len(co) else ["0","0"] for i in range(3)]
hs_serial = [[lcoords(z) for z in row] for row in Hs]
f_serial = [[kcoords(a) for a in row] for row in fcoeff]
cm_summary = {
    "precision":precision,
    "index_range":[0,precision],
    "field_basis":"[1,v,v^2] over K; each K coordinate in [1,omega]",
    "v_polynomial":"v^3+367395*v^2+147*v+1/17",
    "prefix_all_three_sha256":digest(hs_serial),
    "prefix_row_sha256":[digest(row) for row in hs_serial],
    "original_eigenform_b_basis_sha256":digest(f_serial),
    "ideal_count":sum(ideal_counts),
    "nonzero_coefficients_per_row":[sum(z != 0 for z in row) for row in Hs],
    "H_at_q1":[lcoords(row[1]) for row in Hs],
    "H_at_q4_is_minus_two_q1":True,
    "H0_at_q7":lcoords(Hs[0][7]),
    "eigenform_q7_b_basis":[kcoords(a) for a in fcoeff[7]],
    "all_nonzero_indices_are_one_modulo_three":True,
    "normalization":"Xi_i^*omega_v=H_i dq/q; no assertion that Xi_i is integral"
}
result = {
    "kind":"rank2_original_modular_function_input",
    "status":"exact",
    "source":os.environ.get("RANK2_SOURCE_SHA"),
    "run_id":os.environ.get("RANK2_RUN_ID"),
    "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
    "sage_version":SAGE_VERSION,
    "image":os.environ.get("RANK2_IMAGE"),
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "parameters":{"hecke_prime":prime,"faber_max":faber_bound,"cm_precision":precision},
    "readme_blobs":{
        "README.md":os.environ.get("RANK2_ROOT_README_SHA"),
        "topics/rank2-sha-infinitely-many-p/README.md":os.environ.get("RANK2_TOPIC_README_SHA")},
    "phi":phi_summary,
    "cm":cm_summary,
    "scope":"exact original finite inputs only; no certified modular-map coordinates or nonzero shadow yet",
    "elapsed_seconds":time.monotonic()-started
}
payload = canonical(result)
print("RANK2_MODULAR_INPUT_RESULT " + payload,flush=True)
print("RANK2_MODULAR_INPUT_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(),flush=True)
