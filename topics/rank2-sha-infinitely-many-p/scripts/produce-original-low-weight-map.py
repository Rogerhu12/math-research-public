#!/usr/bin/env sage-python
"""Reconstruct and strictly certify the original n Xi0 by low-weight forms."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("This mathematical producer runs only in the public repository Actions.")
import hashlib
import json
import time
from pathlib import Path
from sage.all import (QQ, ZZ, GF, ModularForms, PolynomialRing, PowerSeriesRing,
                      LaurentSeriesRing, matrix, next_prime, set_random_seed)
from sage.env import SAGE_VERSION
from original_low_weight_cm_tools import original_first_differential, original_y_germ

started = time.monotonic()
set_random_seed(20261116)
def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()
def progress(stage,**kw):
    print("RANK2_LOW_WEIGHT_STAGE "+canonical(dict(stage=stage,elapsed=time.monotonic()-started,**kw)),flush=True)
def coords(z):
    co = z.list()
    return [str(QQ(co[i])) if i<len(co) else "0" for i in range(3)]
request = json.loads(Path("topics/rank2-sha-infinitely-many-p/ci/original-low-weight-map-request.json").read_text())
pairs = [(int(n),int(k)) for n,k in request["pairs"]]
assert pairs and all(n>=1 and k>=2 and k%2==0 for n,k in pairs)
max_sturm = max(612*(k+1) for n,k in pairs)
cm_precision = 3*(max_sturm+2)+1
progress("complete original CM coefficients",precision=cm_precision)
F,v,H0,ideal_count = original_first_differential(cm_precision)
f = [H0[3*j+1] for j in range((cm_precision-1)//3+1)]
fhash = digest([coords(x) for x in f])
spaces = {}
results = []
certified = None

for n,k in pairs:
    low_order = 204*k+1
    low_precision = low_order+2
    germ_max = low_order+1
    cert_bound = 612*(k+1)
    cert_precision = cert_bound+3
    if k not in spaces:
        progress("global rational modular-form basis",weight=k,low_precision=low_precision)
        M = ModularForms(867,k,base_ring=QQ)
        assert M.dimension() == 102*k-84
        forms = list(M.basis())
        qlow = [g.q_expansion(low_precision) for g in forms]
        qrows = [[QQ(g[j]) for j in range(low_precision)] for g in qlow]
        spaces[k] = (M,forms,qrows)
    M,forms,qrows = spaces[k]
    dim = len(forms)
    progress("auxiliary exact residue-rank gate",n=n,weight=k,dimension=dim)
    auxiliary = ZZ(1000000)
    while True:
        auxiliary = next_prime(auxiliary)
        if auxiliary%3 != 2:
            continue
        if any(x.denominator()%auxiliary == 0 for row in qrows for x in row):
            continue
        if any(QQ(xi).denominator()%auxiliary == 0 for z in f[:germ_max+1] for xi in z.list()):
            continue
        fp = GF(auxiliary)
        a_mod = fp(17)**((2*auxiliary-1)//3)
        assert a_mod**3 == 17
        def reduce_f(z):
            return sum((fp(QQ(ci))*a_mod**i for i,ci in enumerate(F(z).list())),fp.zero())
        bmod = [[fp(x) for x in row] for row in qrows]
        if matrix(fp,bmod).rank() != dim:
            continue
        break
    v_mod = reduce_f(v)
    f_mod = [reduce_f(x) for x in f[:germ_max+1]]
    y_mod_coeff = original_y_germ(fp,v_mod,f_mod,n,germ_max)
    Sm = LaurentSeriesRing(fp,"Q",default_prec=low_precision+1)
    Qm = Sm.gen()
    ym = Sm(y_mod_coeff)*Qm**(-1)
    aprod = [Sm(row) for row in bmod]
    bprod = [ym*g for g in aprod]
    matmod = matrix(fp,low_order+1,2*dim,
        lambda i,j: aprod[j][i-1] if j<dim else -bprod[j-dim][i-1])
    rankmod = matmod.rank()
    case = {"n":n,"weight":k,"dimension":dim,"low_order":low_order,
            "auxiliary_prime":int(auxiliary),"auxiliary_a17":int(a_mod),
            "matrix_shape":[low_order+1,2*dim],"modular_rank":int(rankmod),
            "low_basis_sha256":digest([[str(x) for x in row] for row in qrows])}
    if rankmod == 2*dim:
        case["status"] = "proved_no_low_weight_ratio_for_this_pair"
        case["reason"] = "Full column rank of a reduction of the actual integral finite matrix implies full characteristic-zero rank."
        results.append(case)
        print("RANK2_LOW_WEIGHT_CASE "+canonical(case),flush=True)
        continue

    progress("characteristic-zero germ and complete kernel",n=n,weight=k,modular_kernel_dimension=2*dim-rankmod)
    yf = original_y_germ(F,v,f[:germ_max+1],n,germ_max)
    SF = LaurentSeriesRing(F,"Q",default_prec=low_precision+1)
    QF = SF.gen()
    YF = SF(yf)*QF**(-1)
    acol = [SF(row) for row in qrows]
    bcol = [YF*g for g in acol]
    mat = matrix(F,low_order+1,2*dim,
        lambda i,j: acol[j][i-1] if j<dim else -bcol[j-dim][i-1])
    kernel = mat.right_kernel()
    case["exact_kernel_dimension"] = int(kernel.dimension())
    if kernel.dimension() == 0:
        case["status"] = "proved_no_low_weight_ratio_for_this_pair"
        results.append(case)
        print("RANK2_LOW_WEIGHT_CASE "+canonical(case),flush=True)
        continue
    sol = kernel.basis()[0]
    assert (mat*sol).is_zero()
    av,bv = list(sol[:dim]),list(sol[dim:])
    assert any(x != 0 for x in bv)
    case["candidate_coefficients_sha256"] = digest({"A":[coords(x) for x in av],"B":[coords(x) for x in bv]})
    progress("same global basis extended for strict identity",n=n,weight=k,bound=cert_bound)
    qhigh = [g.q_expansion(cert_precision) for g in forms]
    assert all(all(QQ(g[j])==qrows[i][j] for j in range(low_precision)) for i,g in enumerate(qhigh))
    PS = PowerSeriesRing(F,"Q",default_prec=cert_precision)
    Q = PS.gen()
    AA = PS([sum((av[i]*qhigh[i][j] for i in range(dim)),F.zero()) for j in range(cert_precision)])
    BB = PS([sum((bv[i]*qhigh[i][j] for i in range(dim)),F.zero()) for j in range(cert_precision)])
    assert BB != 0 and BB.valuation()>=1
    assert AA.valuation() == BB.valuation()-1
    yy = SF(AA)/SF(BB)
    assert yy[-1] == -F(1)/n**3 and yy[0] == -(v+F(3)/n**3)/2
    C = (Q*AA.derivative())*BB-AA*(Q*BB.derivative())
    hh = Q*PS(f[:cert_precision])**3
    residual = C**3-n**3*hh*AA**2*(AA+v*BB)**2*BB**2
    bad = next((j for j in range(cert_bound+1) if residual[j] != 0),None)
    case["certification_bound"] = cert_bound
    case["basis_high_sha256"] = digest([[str(QQ(g[j])) for j in range(cert_precision)] for g in qhigh])
    if bad is not None:
        case["status"] = "low_weight_candidate_fails_original_exact_elliptic_identity"
        case["first_nonzero_certificate_coefficient"] = {"index":bad,"value":coords(residual[bad])}
        results.append(case)
        print("RANK2_LOW_WEIGHT_CASE "+canonical(case),flush=True)
        continue
    case["status"] = "certified_original_integer_hom_n_Xi0"
    case["degree_upper_bound"] = 102*k
    case["Y_pole_order_at_infinity"] = 1
    case["coordinate_recipe"] = "Y=A/B on X0(867); X=n*H0(q)*Y*(Y+v)/(Q*dY/dQ) on X0(2601)."
    case["full_0_through_bound_identity"] = True
    case["warning_scope"] = "This certifies the original map only; it does not assert a nonzero original shadow."
    results.append(case)
    certified = case
    print("RANK2_LOW_WEIGHT_CASE "+canonical(case),flush=True)
    break

result = {"kind":"rank2_original_low_weight_map_reconstruction","source":os.environ.get("RANK2_SOURCE_SHA"),
          "run_id":os.environ.get("RANK2_RUN_ID"),"run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
          "image":os.environ.get("RANK2_IMAGE"),"sage_version":SAGE_VERSION,
          "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "helper_sha256":hashlib.sha256(Path(__file__).with_name("original_low_weight_cm_tools.py").read_bytes()).hexdigest(),
          "readme_blobs":{"README.md":os.environ.get("RANK2_ROOT_README_SHA"),
              "topics/rank2-sha-infinitely-many-p/README.md":os.environ.get("RANK2_TOPIC_README_SHA")},
          "parameters":{"pairs":pairs,"level":867,"cm_precision":cm_precision},
          "original_ideal_count":ideal_count,"original_f_prefix_sha256":fhash,
          "cases":results,"certified_original_map":certified is not None,
          "elapsed_seconds":time.monotonic()-started}
payload = canonical(result)
print("RANK2_LOW_WEIGHT_RESULT "+payload,flush=True)
print("RANK2_LOW_WEIGHT_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)
