#!/usr/bin/env sage-python
"""Original r=29/41 X_0(867) function field and true RR front end.

Public Actions only.  This producer does not certify either characteristic-zero
map, does not replace either original Artin factor, and does not claim a
nonzero Frobenius shadow.  All computed bases remain in process memory.
The callable build_frontend() is also the entry point for the shadow consumer.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public repository Actions.")

import argparse
import hashlib
import json
import resource
import time
from pathlib import Path
from sage.all import (ZZ, GF, PolynomialRing, PowerSeriesRing, LaurentSeriesRing,
                      FunctionField, matrix)
from sage.rings.function_field.divisor import divisor
from sage.env import SAGE_VERSION

STARTED = time.monotonic()
CURRENT_STAGE = "initialization"

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=True)

def digest(x):
    return hashlib.sha256(canonical(x).encode()).hexdigest()

def progress(stage, **kw):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    obj = {"stage":stage, "elapsed_seconds":time.monotonic()-STARTED,
           "max_rss_kib":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)}
    obj.update(kw)
    print("RANK2_SHADOW_RR_STAGE " + canonical(obj), flush=True)

def hash_functions(fs):
    h = hashlib.sha256()
    for f in fs:
        for a in f.list():
            h.update(str(a.numerator()).encode())
            h.update(b"/")
            h.update(str(a.denominator()).encode())
            h.update(b";")
        h.update(b"\n")
    return h.hexdigest()

def hecke17_level3():
    """The original T_3=(eta/eta_3)^12, not the T_9 polynomial."""
    ell = 17
    bound = ell*(ell+1)
    progress("phi17: exact integer eta and Faber coefficients", maximum=bound)
    sig = [ZZ(0)]*(bound+1)
    for d in range(1,bound+1):
        for n in range(d,bound+1,d):
            sig[n] += d
    ld = [ZZ(0)]*(bound+1)
    for n in range(1,bound+1):
        ld[n] = -12*sig[n] + (36*sig[n//3] if n%3 == 0 else 0)
    eta = [ZZ(1)]
    for n in range(1,bound+1):
        a = sum((ld[j]*eta[n-j] for j in range(1,n+1)), ZZ(0))
        assert a%n == 0
        eta.append(a//n)
    assert eta[:4] == [1,-12,54,-76]

    ZX = PolynomialRing(ZZ,"X")
    X = ZX.gen()
    bc = [ZX(a) for a in eta]
    bc[1] -= X
    faber = [ZX.zero()]
    for n in range(1,bound+1):
        f = -n*bc[n]
        for j in range(1,n):
            f -= faber[j]*bc[n-j]
        assert f.degree() == n and f.leading_coefficient() == 1
        faber.append(f)

    Zq = PolynomialRing(ZZ,"q")
    short = Zq(eta[:19])
    ps = [ZX.zero()]
    for k in range(1,19):
        ep = (short**k).truncate(k+1)
        f = ZX(18*ep[k])
        for n in range(-k,0):
            f += ep[k+n]*faber[-17*n]
            if n%17 == 0:
                f += 17*ep[k+n]*faber[-n//17]
        ps.append(f)
    es = [ZX.one()]
    for n in range(1,19):
        num = sum(((-1)**(j-1)*es[n-j]*ps[j] for j in range(1,n+1)),ZX.zero())
        assert all(ZZ(a)%n == 0 for a in num.list())
        es.append(ZX([ZZ(a)//n for a in num.list()]))
    assert es[18] == X**18
    terms = {}
    for n,e in enumerate(es):
        for i,a in enumerate(e.list()):
            if a:
                terms[(i,18-n)] = ZZ((-1)**n*a)
    assert terms[(0,18)] == terms[(18,0)] == 1
    assert terms[(17,17)] == -1
    assert all(terms.get((j,i),0) == a for (i,j),a in terms.items())
    serial = [[i,j,str(terms[(i,j)])] for i,j in sorted(terms)]
    progress("phi17: complete", nonzero_terms=len(terms),
             bidegree=[18,18], integer_terms_sha256=digest(serial))
    return terms, digest(serial)

def evaluate_phi(terms, x, y, zero):
    xp = [x**i for i in range(19)]
    yp = [y**i for i in range(19)]
    return sum((a*xp[i]*yp[j] for (i,j),a in terms.items()),zero)

def make_field(prime, terms):
    """Eliminate precisely the 18 backtracking walks; retain the cyclic 17^2 component."""
    k = GF(prime)
    P3 = PolynomialRing(k, names=("tt","zz","vv"), order="degrevlex")
    tt,zz,vv = P3.gens()
    f = evaluate_phi(terms,tt,zz,P3.zero())
    g = evaluate_phi(terms,zz,vv,P3.zero())
    progress("phi289: resultant start", degree_in_middle=18)
    res = f.resultant(g,zz)
    assert all(e[1] == 0 for e in res.dict())
    kT = PolynomialRing(k,"T0")
    T0 = kT.gen()
    kTV = PolynomialRing(kT,"V0")
    V0 = kTV.gen()
    resultant = sum((k(c)*T0**e[0]*V0**e[2] for e,c in res.dict()),kTV.zero())
    cyclic, remainder = resultant.quo_rem((V0-T0)**18)
    assert remainder == 0 and cyclic.degree() == 306
    assert cyclic.leading_coefficient() == 1
    progress("phi289: backtracking removed", cyclic_degree=306,
             coefficients_sha256=digest([str(c) for c in cyclic.list()]))

    K = FunctionField(k,"T")
    T = K.gen()
    KV = PolynomialRing(K,"V")
    coeffs = []
    for p in cyclic.list():
        coeffs.append(sum((K(c)*T**i for i,c in enumerate(p.list())),K.zero()))
    poly = KV(coeffs)
    progress("field: separability check")
    assert poly.gcd(poly.derivative()).degree() == 0
    B = K.extension(poly,"V")
    TB,VB = B(T),B.gen()
    BZ = PolynomialRing(B,"Z")
    Z = BZ.gen()
    progress("field: exact intermediate U recovery")
    gcd = evaluate_phi(terms,TB,Z,BZ.zero()).gcd(
          evaluate_phi(terms,Z,VB,BZ.zero())).monic()
    assert gcd.degree() == 1
    UB = -gcd[0]
    assert evaluate_phi(terms,TB,UB,B.zero()) == 0
    assert evaluate_phi(terms,UB,VB,B.zero()) == 0
    assert UB != TB and UB != VB
    progress("field: cyclic tower recovered", degree=306,
             intermediate_sha256=hash_functions([UB]))
    return k,K,B,TB,UB,VB

def euler_series(R, N, dilation=1):
    """Euler's pentagonal expansion, so there is no division by n modulo r."""
    q = R.gen()
    out = R.one()
    j = 1
    while dilation*j*(3*j-1)//2 < N:
        a = dilation*j*(3*j-1)//2
        b = dilation*j*(3*j+1)//2
        sign = -1 if j%2 else 1
        out += sign*q**a
        if b < N:
            out += sign*q**b
        j += 1
    return out.add_bigoh(N)

class TateEvaluator:
    """Evaluate the actual T_3(Q), T_3(Q^289) branch, with certified truncation loss."""
    def __init__(self,k):
        self.k = k
        self.relative_precision = 0
        self.R = None
        self.L = None
        self.z = None
        self.vunit = None
        self.cache = {}

    def prepare(self, relative):
        relative = int(relative)
        if relative <= self.relative_precision:
            return
        N = relative+2
        self.R = PowerSeriesRing(self.k,"Q",default_prec=N)
        self.L = LaurentSeriesRing(self.k,"Q",default_prec=N)
        q = self.R.gen()
        e1 = euler_series(self.R,N)
        e3 = euler_series(self.R,N,3)
        eta = ((e1/e3)**12).add_bigoh(N)
        self.z = (q/eta).add_bigoh(N+1)   # exactly 1/T_3(Q)
        self.vunit = self.R([eta[n//289] if n%289 == 0 else self.k.zero()
                            for n in range(N)]).add_bigoh(N)
        self.relative_precision = relative
        self.cache = {}
        progress("tate: prepared certified Laurent precision", relative=relative)

    def eval_reverse(self,p):
        key = tuple(int(c) for c in p.list())
        if key in self.cache:
            return self.cache[key]
        rev = self.R(list(reversed(p.list())))
        # Polynomial composition is in the nilpotent series z=Q+O(Q^2).
        value = rev.polynomial()(self.z)
        self.cache[key] = value
        return value

    def expansion(self,f,precision):
        precision = int(precision)
        terms = []
        lower = None
        for i,a in enumerate(f.list()):
            if not a:
                continue
            num,den = a.numerator(),a.denominator()
            val = int(den.degree()-num.degree()-289*i)
            terms.append((i,num,den,val))
            lower = val if lower is None else min(lower,val)
        if lower is None:
            return [self.k.zero()]*precision,0
        rel = max(1,precision-lower)
        self.prepare(rel)
        q = self.R.gen()
        inveta = self.z/q
        out = self.L.zero()
        for i,num,den,val in terms:
            shift = int(den.degree()-num.degree())
            unit = (self.eval_reverse(num)/self.eval_reverse(den))
            unit *= inveta**shift
            if i:
                unit *= self.vunit**i
            term = self.L(unit) << val
            assert term.prec() >= precision
            out += term
        out = out.add_bigoh(precision)
        assert out.valuation() >= 0, "A claimed RR section has a pole at the original Tate cusp."
        return [self.k(out[n]) for n in range(precision)],lower

def divisor_record(d):
    return [{"degree":int(p.degree()),"multiplicity":int(m),
             "place_sha256":hashlib.sha256(str(p).encode()).hexdigest()}
            for p,m in d.list()]

def build_frontend(prime=29, rr_powers=(1,), q_precision=None):
    assert prime in (29,41)
    powers = tuple(sorted(set(int(m) for m in rr_powers)))
    assert powers and powers[0] >= 1
    q_precision = max(205,204*max(powers)+1) if q_precision is None else int(q_precision)
    assert q_precision >= 204*max(powers)+1

    terms,phi_hash = hecke17_level3()
    k,K,B,T,U,V = make_field(prime,terms)

    progress("normalization: finite maximal order start")
    Ofin = B.maximal_order()
    progress("normalization: finite maximal order complete",
             integral_rank=len(Ofin.basis()))
    assert len(Ofin.basis()) == 306
    progress("normalization: infinite maximal order start")
    Oinf = B.maximal_order_infinite()
    progress("normalization: infinite maximal order complete",
             integral_rank=len(Oinf.basis()))
    assert len(Oinf.basis()) == 306

    progress("cusps: full divisor of T start")
    divT = T.divisor()
    cusps = divT.support()
    assert sum(int(p.degree()) for p in cusps) == 36
    assert divT.numerator().degree() == divT.denominator().degree() == 306
    candidates = [p for p in cusps if p.degree() == 1 and
                  divT.multiplicity(p) == -1 and V.valuation(p) == -289]
    assert len(candidates) == 1
    pinf = candidates[0]
    assert U.valuation(pinf) == -17
    Cusp = divisor(B,{p:1 for p in cusps})
    progress("cusps: complete", closed_places=len(cusps), geometric_degree=36,
             valuation_pattern=divisor_record(divT))

    progress("divisor: weight two logarithmic differential start")
    omega = T.differential()/T
    D = omega.divisor()+Cusp
    assert D.is_effective() and D.degree() == 204
    assert D.multiplicity(pinf) == 0
    assert omega.divisor().degree() == 168
    progress("divisor: complete", weight_two_degree=204, genus_from_canonical=85,
             effective_support=divisor_record(D))

    evaluator = TateEvaluator(k)
    bases = {}
    jets = {}
    summaries = []
    for m in powers:
        progress("rr: layer start", divisor_multiple=m, expected_dimension=204*m-84)
        bas = (m*D).basis_function_space()
        assert len(bas) == 204*m-84
        progress("rr: exact basis complete", divisor_multiple=m, dimension=len(bas),
                 functions_sha256=hash_functions(bas))
        # Prepare once for every cancellation in this exact function-field basis.
        raw_bounds = []
        for f in bas:
            raw_bounds.extend(int(a.denominator().degree()-a.numerator().degree()-289*i)
                              for i,a in enumerate(f.list()) if a)
        evaluator.prepare(max(1,q_precision-min(raw_bounds,default=0)))
        rows = []
        lowest_raw = 0
        for i,f in enumerate(bas):
            row,low = evaluator.expansion(f,q_precision)
            rows.append(row)
            lowest_raw = min(lowest_raw,low)
            if i%8 == 7 or i+1 == len(bas):
                progress("rr: Tate rows", divisor_multiple=m,
                         completed=i+1,total=len(bas),lowest_raw_valuation=lowest_raw)
        M = matrix(k,rows)
        # Multiplication by E3^m, whose constant term is 1, preserves this rank.
        rank = M[:,:204*m+1].rank()
        assert rank == len(bas)
        serial = [[int(a) for a in row] for row in rows]
        bases[m],jets[m] = bas,M
        summaries.append({"divisor_multiple":m,"weight":2*m,"dimension":len(bas),
                          "jet_precision":q_precision,"sturm_rank":int(rank),
                          "basis_sha256":hash_functions(bas),
                          "jets_sha256":digest(serial),
                          "lowest_raw_laurent_valuation":lowest_raw})
        progress("rr: layer certified", **summaries[-1])

    context = {"prime":prime,"constants":k,"rational_base":K,"field":B,
               "T":T,"U":U,"V":V,"cusps":tuple(cusps),"original_cusp":pinf,
               "weight_two_divisor":D,"rr_bases":bases,"rr_jets":jets,
               "tate_evaluator":evaluator,"phi17_terms":terms}
    result = {
        "kind":"rank2_original_good_prime_rr_front",
        "status":"exact_frontend_only",
        "prime":prime,"level":867,"function_field_degree":306,
        "genus":85,"geometric_cusps":36,"weight_two_divisor_degree":204,
        "phi17_integer_terms_sha256":phi_hash,
        "rr_layers":summaries,
        "scope":"Actual original function field, all cusps, RR functions and Tate jets only. Neither original characteristic-zero map nor a nonzero shadow is asserted.",
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID",os.environ.get("GITHUB_RUN_ID")),
        "sage_version":SAGE_VERSION,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds":time.monotonic()-STARTED,
        "readme_blobs":{"README.md":os.environ.get("RANK2_ROOT_README_SHA"),
                       "topic":os.environ.get("RANK2_TOPIC_README_SHA")}
    }
    return context,result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime",type=int,choices=(29,41),default=29)
    parser.add_argument("--rr-powers",default="1")
    parser.add_argument("--q-precision",type=int,default=None)
    args = parser.parse_args()
    powers = tuple(int(a) for a in args.rr_powers.split(","))
    context,result = build_frontend(args.prime,powers,args.q_precision)
    globals()["ORIGINAL_SHADOW_RR_CONTEXT"] = context
    payload = canonical(result)
    print("RANK2_SHADOW_RR_RESULT " + payload,flush=True)
    print("RANK2_SHADOW_RR_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(),flush=True)

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        progress("failed",failed_stage=CURRENT_STAGE,
                 exception_type=type(exc).__name__,message=str(exc))
        raise
