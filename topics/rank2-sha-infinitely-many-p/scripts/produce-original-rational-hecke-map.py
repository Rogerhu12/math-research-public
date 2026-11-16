#!/usr/bin/env sage-python
"""Original rational-Hecke map via product bases and exact CRT certification.

All execution is restricted to the public repository Actions.  The selected
u is R874's exact cusp-ideal generator.  Finite fields choose a characteristic-
zero candidate; only the full original elliptic identity certifies a map.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research repository Actions.")
import hashlib
import importlib.util
import itertools
import json
import time
from pathlib import Path
from sage.all import (QQ, ZZ, GF, NumberField, ModularForms, PolynomialRing,
                      PowerSeriesRing, LaurentSeriesRing, matrix, vector,
                      identity_matrix, next_prime, set_random_seed)
from sage.env import SAGE_VERSION
from original_low_weight_cm_tools import original_y_germ

STARTED = time.monotonic()
set_random_seed(20261116)
ROOT = Path("topics/rank2-sha-infinitely-many-p")
REQUEST = json.loads((ROOT/"ci/original-rational-hecke-map-request.json").read_text())
WEIGHTS = [int(k) for k in REQUEST["weights"]]
assert WEIGHTS and all(k in (4,6) for k in WEIGHTS)
MAX_PRIMES = int(REQUEST["max_split_primes"])
assert 1 <= MAX_PRIMES <= 512
def canonical(o):
    return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def digest(o):
    return hashlib.sha256(canonical(o).encode()).hexdigest()
def progress(stage, **kw):
    print("RANK2_RATIONAL_MAP_STAGE "+canonical(dict(
        stage=stage,elapsed_seconds=time.monotonic()-STARTED,**kw)),flush=True)
def coords(z):
    p = z.list()
    return [str(QQ(p[i])) if i < len(p) else "0" for i in range(3)]
def hash_rows(rows):
    h = hashlib.sha256()
    for row in rows:
        for x in row:
            h.update(str(QQ(x)).encode())
            h.update(b"\n")
        h.update(b";\n")
    return h.hexdigest()

# Exact original eigenvalues from the established finite-ideal producer.
dep = Path(__file__).with_name("check-r873-original-cm-petersson-degree.py")
spec = importlib.util.spec_from_file_location("original_r873", str(dep))
r873 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r873)
CERT_MAX = max(612*(k+1) for k in WEIGHTS)
CERT_PREC = CERT_MAX+3
CM_PREC = 3*(CERT_PREC-1)+1
progress("original complete CM input in the fixed rational Hecke direction",
         precision=CM_PREC)
K9, eigen, squared_eigen, ideal_count, eigen_hash = r873.exact_coefficients(CM_PREC)
z9 = K9.gen()
th9 = z9**2+z9**(-2)
eb9 = [K9.one(),th9,th9**2-2]
def coords9(z):
    p = K9(z).list()
    return vector(QQ,[p[i] if i<len(p) else 0 for i in range(6)])
B9 = matrix(QQ,[coords9(t) for t in eb9]).transpose()
chosen_rows = tuple(B9.transpose().pivots())
assert len(chosen_rows)==3
inv9 = matrix(QQ,[[B9[i,j] for j in range(3)] for i in chosen_rows]).inverse()
Pa = PolynomialRing(QQ,"a_var")
a_var = Pa.gen()
F = NumberField(a_var**3-17,"a17")
a17 = F.gen()
v = -122465-47628*a17-QQ(314892)/17*a17**2
lam = (68+7*a17-13*a17**2)/3
assert lam.norm()==34
lambda_basis = [F.one(),-497+237*a17-17*a17**2,609-44*a17-75*a17**2]
M1 = matrix(QQ,[[0,2,-1],[1,0,1],[0,1,0]])
M2 = matrix(QQ,[[0,-1,2],[0,1,-1],[1,0,-1]])
ucoords = vector(QQ,[QQ(915)/55569,QQ(1097)/55569,QQ(2962)/55569])
Mu = ucoords[0]*identity_matrix(QQ,3)+ucoords[1]*M1+ucoords[2]*M2
ret = 106*identity_matrix(QQ,3)+59*M1+185*M2
assert Mu*ret==17*identity_matrix(QQ,3)
f = []
for j in range(CERT_PREC):
    m = 3*j+1
    ev = coords9(eigen[m])
    ac = inv9*vector(QQ,[ev[i] for i in chosen_rows])
    assert B9*ac==ev and all(t.denominator()==1 for t in ac)
    uc = Mu*ac
    hu = sum((lambda_basis[i]*uc[i] for i in range(3)),F.zero())
    f.append(hu/lam)
assert f[0]==1 and f[1]==-2
# This is an actual target isomorphism, not free normalization of H_u.
# Xnew=lam^2 X, Ynew=lam^3 Y, vnew=lam^3 v, pullback differential H_u/lam.
vnew = lam**3*v
assert vnew.norm()==-2312
f_hash = digest([coords(t) for t in f])
progress("rational weight-two modular forms",dimension=120)
LOW_MAX = max(204*k+1 for k in WEIGHTS)
LOW_PREC = LOW_MAX+2
Mweight2 = ModularForms(867,2,base_ring=QQ)
assert Mweight2.dimension()==120
forms2 = list(Mweight2.basis())
q2exp = [g.q_expansion(LOW_PREC) for g in forms2]
q2low = [[QQ(g[j]) for j in range(LOW_PREC)] for g in q2exp]
q2hash = hash_rows(q2low)
product_prime = ZZ(REQUEST["product_basis_prime"])
fpbase = GF(product_prime)
assert all(x.denominator()%product_prime for row in q2low for x in row)
assert matrix(fpbase,[[fpbase(x) for x in row[:205]] for row in q2low]).rank()==120

# A finite-field independent set of the correct size proves a complete rational
# basis.  No spanning assertion is inferred from a partial product search.
recipes_by_power = {1:[(i,) for i in range(120)]}
for power in range(2,max(WEIGHTS)//2+1):
    weight = 2*power
    expected = 102*weight-84
    nsturm = 102*weight+1
    Sp = PowerSeriesRing(fpbase,"Q",default_prec=nsturm)
    m2 = [Sp([fpbase(t) for t in row[:nsturm]]).add_bigoh(nsturm) for row in q2low]
    def recipe_series(recipe, ring, two_forms, precision):
        ans = ring.one().add_bigoh(precision)
        for ii in recipe:
            ans *= two_forms[ii]
        return ans.add_bigoh(precision)
    prev_recipes = recipes_by_power[power-1]
    prev_series = [recipe_series(r,Sp,m2,nsturm) for r in prev_recipes]
    selected, selected_rows, seen = [],[],set()
    for i in range(120):
        batch_recipes, batch_rows = [],[]
        for rr,ss in zip(prev_recipes,prev_series):
            recipe = tuple(sorted((i,)+rr))
            if recipe in seen:
                continue
            seen.add(recipe)
            prod = m2[i]*ss
            batch_recipes.append(recipe)
            batch_rows.append([prod[j] for j in range(nsturm)])
        if not batch_rows:
            continue
        all_recipes = selected+batch_recipes
        all_rows = selected_rows+batch_rows
        pivots = tuple(matrix(fpbase,all_rows).transpose().pivots())
        selected = [all_recipes[j] for j in pivots]
        selected_rows = [all_rows[j] for j in pivots]
        progress("product basis rank",weight=weight,rank=len(selected),
                 expected=expected,batches=i+1)
        if len(selected)==expected:
            break
    assert len(selected)==expected, "Product set did not provide a complete certified basis"
    recipes_by_power[power]=selected
    progress("complete rational product basis",weight=weight,
             dimension=expected,recipe_sha256=digest(selected),
             good_prime=int(product_prime),sturm_prefix=nsturm)
SQQ = PowerSeriesRing(QQ,"Q",default_prec=LOW_PREC)
two_low = [SQQ(row).add_bigoh(LOW_PREC) for row in q2low]
qhigh_cache = {}
def rational_product_rows(weight, precision, high=False):
    recipes = recipes_by_power[weight//2]
    if high:
        if precision not in qhigh_cache:
            progress("extend same rational weight-two basis for strict identity",
                     precision=precision)
            expanded=[g.q_expansion(precision) for g in forms2]
            qhigh_cache[precision]=[
                [QQ(g[j]) for j in range(precision)] for g in expanded]
        two_rows=qhigh_cache[precision]
    else:
        two_rows=[row[:precision] for row in q2low]
    ring=PowerSeriesRing(QQ,"Q",default_prec=precision)
    two=[ring(row).add_bigoh(precision) for row in two_rows]
    result=[]
    for recipe in recipes:
        ps=ring.one().add_bigoh(precision)
        for i in recipe:
            ps*=two[i]
        result.append([QQ(ps[j]) for j in range(precision)])
    return result

def reduce_element(z, fp, aa):
    pp=F(z).list()
    return sum((fp(QQ(c))*aa**i for i,c in enumerate(pp)),fp.zero())

def canonical_residue_solution(qrows, fp, aa, low_order):
    precision=low_order+2
    dim=len(qrows)
    Sm=PowerSeriesRing(fp,"Q",default_prec=precision)
    bm=[Sm([fp(x) for x in row]).add_bigoh(precision) for row in qrows]
    fm=[reduce_element(t,fp,aa) for t in f[:low_order+2]]
    ym=Sm(original_y_germ(fp,reduce_element(vnew,fp,aa),fm,1,low_order+1)).add_bigoh(precision)
    by=[ym*g for g in bm]
    # Row i is the coefficient of Q^(i-1) in A-Ynew B.
    mat=matrix(fp,low_order+1,2*dim,lambda i,j:
        (fp.zero() if i==0 else bm[j][i-1]) if j<dim else -by[j-dim][i])
    ech=mat.echelon_form()
    piv=tuple(ech.pivots())
    if len(piv)==2*dim:
        return {"rank":len(piv),"pivots":piv,"solution":None}
    pivset=set(piv)
    free=next(j for j in range(2*dim) if j not in pivset)
    sol=vector(fp,2*dim)
    sol[free]=1
    for row,j in enumerate(piv):
        sol[j]=-ech[row,free]
    assert (mat*sol).is_zero()
    bseries=sum((sol[dim+j]*bm[j] for j in range(dim)),Sm.zero())
    assert bseries!=0 and bseries.valuation()>=1
    return {"rank":len(piv),"pivots":piv,"solution":sol,"free":free,
            "B_valuation":int(bseries.valuation())}

def initial_exact_germ_check(sol,qrows,bval):
    dim=len(qrows)
    n=bval+12
    ring=PowerSeriesRing(F,"Q",default_prec=n+1)
    aa=ring([sum((sol[i]*qrows[i][j] for i in range(dim)),F.zero())
             for j in range(n+1)]).add_bigoh(n+1)
    bb=ring([sum((sol[dim+i]*qrows[i][j] for i in range(dim)),F.zero())
             for j in range(n+1)]).add_bigoh(n+1)
    if bb==0 or bb.valuation()!=bval or aa.valuation()!=bval-1:
        return False
    yg=original_y_germ(F,vnew,f[:13],1,12)
    low=ring(yg).add_bigoh(13)
    check=(ring.gen()*aa-low*bb).add_bigoh(bval+10)
    return check==0

def strict_original_certificate(weight,sol,qrows):
    dim=len(qrows)
    bound=612*(weight+1)
    precision=bound+3
    qhigh=rational_product_rows(weight,precision,high=True)
    assert all(row[:len(qrows[i])]==qrows[i] for i,row in enumerate(qhigh))
    ring=PowerSeriesRing(F,"Q",default_prec=precision)
    Q=ring.gen()
    A=ring([sum((sol[i]*qhigh[i][j] for i in range(dim)),F.zero())
            for j in range(precision)]).add_bigoh(precision)
    B=ring([sum((sol[dim+i]*qhigh[i][j] for i in range(dim)),F.zero())
            for j in range(precision)]).add_bigoh(precision)
    assert B!=0 and B.valuation()>=1 and A.valuation()==B.valuation()-1
    LQ=LaurentSeriesRing(F,"Q",default_prec=precision)
    Y=LQ(A)/LQ(B)
    assert Y[-1]==-1 and Y[0]==-(vnew+3)/2
    C=(Q*A.derivative())*B-A*(Q*B.derivative())
    h=Q*ring(f[:precision]).add_bigoh(precision)**3
    residual=(C**3-h*A**2*(A+vnew*B)**2*B**2).add_bigoh(bound+1)
    bad=next((j for j in range(bound+1) if residual[j]!=0),None)
    info={"bound":bound,"full_0_through_bound_identity":bad is None,
          "coordinate_coefficients_sha256":digest([coords(x) for x in sol]),
          "global_product_basis_high_sha256":hash_rows(qhigh),
          "B_order_at_infinity":int(B.valuation())}
    if bad is not None:
        info["first_nonzero_index"]=bad
        info["first_nonzero_value"]=coords(residual[bad])
    return bad is None,info

cases=[]
CERTIFIED_SOLUTION=None
CERTIFIED_WEIGHT=None
for weight in WEIGHTS:
    low_order=204*weight+1
    low_precision=low_order+2
    dim=102*weight-84
    qrows=rational_product_rows(weight,low_precision)
    assert len(qrows)==dim
    progress("original finite low-reconstruction matrix",weight=weight,
             dimension=dim,rows=low_order+1,columns=2*dim)
    row_hash=hash_rows(qrows)
    prime=ZZ(REQUEST["split_prime_start"])
    modulus=ZZ(1)
    residues=None
    reference=None
    accepted=0
    excluded=False
    case={"weight":weight,"dimension":dim,"low_order":low_order,
          "matrix_shape":[low_order+1,2*dim],
          "rational_product_basis_sha256":row_hash,
          "product_recipes_sha256":digest(recipes_by_power[weight//2])}
    for attempt in range(MAX_PRIMES*40):
        if accepted>=MAX_PRIMES:
            break
        prime=next_prime(prime)
        if prime%3!=1 or pow(17,int((prime-1)//3),int(prime))!=1:
            continue
        if any(x.denominator()%prime==0 for row in qrows for x in row):
            continue
        if any(QQ(c).denominator()%prime==0
               for t in f[:low_order+2]+[vnew] for c in F(t).list()):
            continue
        fp=GF(prime)
        PR=PolynomialRing(fp,"t")
        t=PR.gen()
        roots=sorted((t**3-17).roots(multiplicities=False),key=lambda x:int(x))
        assert len(roots)==3 and all(aa**3==17 for aa in roots)
        if matrix(fp,[[fp(x) for x in row[:102*weight+1]] for row in qrows]).rank()!=dim:
            continue
        data=[]
        for aa in roots:
            ans=canonical_residue_solution(qrows,fp,aa,low_order)
            if ans["solution"] is None:
                case.update(status="proved_no_ratio_for_original_u_at_this_weight",
                            full_rank_prime=int(prime),a17_residue=int(aa),
                            modular_rank=ans["rank"])
                excluded=True
                break
            data.append(ans)
        if excluded:
            break
        if not all(d["pivots"]==data[0]["pivots"] and
                   d["B_valuation"]==data[0]["B_valuation"] for d in data):
            progress("skip exceptional split prime",weight=weight,prime=int(prime))
            continue
        pattern=(data[0]["pivots"],data[0]["free"],data[0]["B_valuation"])
        if reference is not None and pattern!=reference:
            progress("reset to new common exact pivot pattern",weight=weight,
                     prime=int(prime),previous_bits=int(modulus.nbits()))
            residues=None
            modulus=ZZ(1)
            accepted=0
        reference=pattern
        vand=matrix(fp,[[1,aa,aa**2] for aa in roots])
        coeffs=vand.inverse()*matrix(fp,[list(d["solution"]) for d in data])
        current=[ZZ(coeffs[i,j]) for i in range(3) for j in range(2*dim)]
        if residues is None:
            residues=current
            modulus=prime
        else:
            inv=modulus.inverse_mod(prime)
            residues=[old+modulus*((new-old)*inv%prime)
                      for old,new in zip(residues,current)]
            modulus*=prime
        accepted+=1
        progress("three-embedding CRT",weight=weight,prime=int(prime),
                 accepted_primes=accepted,modulus_bits=int(modulus.nbits()),
                 modular_rank=data[0]["rank"],B_valuation=data[0]["B_valuation"])
        if accepted<2:
            continue
        try:
            rational=[r.rational_reconstruction(modulus) for r in residues]
        except (ArithmeticError,ValueError,ZeroDivisionError):
            continue
        sol=vector(F,[sum((rational[i*(2*dim)+j]*a17**i for i in range(3)),F.zero())
                      for j in range(2*dim)])
        assert sol[data[0]["free"]]==1
        if not initial_exact_germ_check(sol,qrows,data[0]["B_valuation"]):
            continue
        progress("exact candidate reaches full original elliptic certificate",
                 weight=weight,accepted_primes=accepted)
        passed,info=strict_original_certificate(weight,sol,qrows)
        case["last_exact_certificate"]=info
        if not passed:
            progress("candidate requires further reconstruction",weight=weight,
                     first_nonzero_index=info["first_nonzero_index"])
            continue
        CERTIFIED_SOLUTION=sol
        CERTIFIED_WEIGHT=weight
        case.update(status="certified_original_rational_hecke_hom",
                    accepted_split_primes=accepted,modulus_bits=int(modulus.nbits()),
                    degree_upper_bound=102*weight,
                    certified_original_integer_return=17,
                    return_hecke_coordinates=["106","59","185"],
                    scaled_target_parameter=coords(vnew),
                    original_leading_coefficient=coords(lam),
                    coordinate_recipe="Construct Ynew=A/B on X0(867), Xnew=(H_u/lam)*Ynew*(Ynew+lam^3*v)/(Q*dYnew/dQ) on X0(2601); original X=Xnew/lam^2, Y=Ynew/lam^3.",
                    source_basis_recipe="Products of the ordered rational M2(867) basis, selected by the committed deterministic finite-field rank rule.",
                    full_original_artin_source_preserved=True)
        break
    if CERTIFIED_SOLUTION is None and not excluded:
        case["status"]="reconstruction_budget_exhausted_without_a_certificate"
        case["accepted_split_primes"]=accepted
        case["modulus_bits"]=int(modulus.nbits())
        case["scope"]="No conclusion that the actual original map fails to exist."
    cases.append(case)
    print("RANK2_RATIONAL_MAP_CASE "+canonical(case),flush=True)
    if CERTIFIED_SOLUTION is not None:
        break

result={
    "kind":"rank2_original_rational_hecke_map",
    "source":os.environ.get("RANK2_SOURCE_SHA"),
    "run_id":os.environ.get("RANK2_RUN_ID"),
    "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
    "image":os.environ.get("RANK2_IMAGE"),
    "sage_version":SAGE_VERSION,
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "CM_dependency_sha256":hashlib.sha256(dep.read_bytes()).hexdigest(),
    "germ_dependency_sha256":hashlib.sha256(Path(__file__).with_name(
        "original_low_weight_cm_tools.py").read_bytes()).hexdigest(),
    "readme_blobs":{"README.md":os.environ.get("RANK2_ROOT_README_SHA"),
        "topics/rank2-sha-infinitely-many-p/README.md":os.environ.get("RANK2_TOPIC_README_SHA")},
    "parameters":REQUEST,
    "source_CM_ideal_count":ideal_count,
    "original_CM_coefficients_sha256":eigen_hash,
    "normalized_original_Hu_sha256":f_hash,
    "M2_low_basis_sha256":q2hash,
    "selected_original_u":["915/55569","1097/55569","2962/55569"],
    "actual_target_rescaling":coords(lam),
    "cases":cases,
    "certified_original_map":CERTIFIED_SOLUTION is not None,
    "original_shadow_computed":False,
    "elapsed_seconds":time.monotonic()-STARTED
}
payload=canonical(result)
print("RANK2_RATIONAL_MAP_RESULT "+payload,flush=True)
print("RANK2_RATIONAL_MAP_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)
