#!/usr/bin/env python3
"""Exact original ordered saturated flags for R760/R769/R775.
All mathematics is intended for the public Actions runner. No output files.
python-flint==0.9.0. This is not a mod-p nullspace or a scaled-row Smith proxy.
At each new rational row, a unimodular gcd reduction computes its image ideal
on the entire preceding saturated integer kernel; only that exact kernel is kept.
"""
from __future__ import annotations
import argparse, concurrent.futures, hashlib, json, math, sys
from flint import ctx, fmpq as Q, fmpq_series as Series, fmpz_mat

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

def egcd(a, b):
    x, y, u, v = 1, 0, 0, 1
    aa, bb = abs(a), abs(b)
    while bb:
        q, rr = divmod(aa, bb)
        aa, bb, x, u, y, v = bb, rr, u, x-q*u, v, y-q*v
    return aa, x if a >= 0 else -x, y if b >= 0 else -y

def prime_list(n):
    sieve = bytearray(b"\x01") * (n+1)
    sieve[:2] = b"\x00\x00"
    for j in range(2, math.isqrt(n)+1):
        if sieve[j]:
            sieve[j*j:n+1:j] = b"\x00" * (((n-j*j)//j)+1)
    return [j for j in range(2, n+1) if sieve[j]]

def denominator_factors(den, primes):
    out = []
    for p in primes:
        if den % p == 0:
            v = 0
            while den % p == 0:
                den //= p
                v += 1
            out.append([p, v])
    if den != 1:
        raise AssertionError("Unexpected denominator prime beyond the original series bound")
    return out

def exact_sources(D, cap):
    ctx.cap = cap+1
    t = Series([0,1])
    qcoef = [Q(0)] * (cap+1)
    qcoef[1] = Q(-2,5)
    for j in range(2, cap+1):
        qcoef[j] = qcoef[j-1] * Q(6*j-4,6*j-1)
    affQ = Series(qcoef)
    logtheta = Series([Q(0)]+[-qcoef[j]/(3*j) for j in range(1,cap+1)])
    theta = logtheta.exp()
    p4 = (1-t)*(1+8*t)*(1+Q(4,7)*t+Q(16,7)*t*t)
    v0 = (1-4*t)*(1-20*t-8*t*t)*(1+96*t+48*t*t-64*t*t*t)
    B = 34*affQ*p4 - 6*p4 - 6*t*p4.derivative()
    S = -t*(theta**17)*p4
    T = -t*(theta**36)*p4*v0
    U = -(t**5)*((1-t)**3)*(theta**102)*(B**6)
    assert S[1] == T[1] == -1 and U[5] == -(6**6)
    powers = []
    for F in (S,T,U):
        pp = [Series([1])]
        for j in range(D):
            pp.append(pp[-1]*F)
        powers.append(pp)
    labels, columns = [], []
    for total in range(D+1):
        for nu in range(total+1):
            for b in range(total-nu+1):
                a = total-b-nu
                F = powers[0][a]*powers[1][b]*powers[2][nu]
                labels.append([a,b,nu])
                columns.append([F[k] for k in range(cap+1)])
    assert len(columns) == math.comb(D+3,3)
    return labels, columns

def one_degree(item):
    D, capfactor = item
    N = math.comb(D+3,3)
    cap = capfactor*N+16
    print("R775 exact saturated prefix: D=%s N=%s cap=%s" % (D,N,cap),
          file=sys.stderr, flush=True)
    labels, columns = exact_sources(D,cap)
    basis = [[int(i==j) for j in range(N)] for i in range(N)]
    primes = prime_list(6*cap+7)
    jumps, zero_rows, by_prime = [], [], {}
    digest = hashlib.sha256()
    max_basis_bits = 1
    for k in range(cap+1):
        dim = len(basis[0])
        if not dim:
            break
        row = [columns[j][k] for j in range(N)]
        values = [sum((row[i]*basis[i][j] for i in range(N)),Q(0))
                  for j in range(dim)]
        if not any(values):
            zero_rows.append(k)
            continue
        den = 1
        for v in values:
            den = math.lcm(den,int(v.q))
        ints = [int(v.p)*(den//int(v.q)) for v in values]
        pivot = next(j for j,v in enumerate(ints) if v)
        if pivot:
            ints[0],ints[pivot] = ints[pivot],ints[0]
            for rowB in basis:
                rowB[0],rowB[pivot] = rowB[pivot],rowB[0]
        for j in range(1,dim):
            if not ints[j]:
                continue
            aa,bb = ints[0],ints[j]
            gg,uu,vv = egcd(aa,bb)
            assert uu*aa+vv*bb == gg and gg > 0
            for rowB in basis:
                x,y = rowB[0],rowB[j]
                rowB[0] = uu*x+vv*y
                rowB[j] = -(bb//gg)*x+(aa//gg)*y
            ints[0],ints[j] = gg,0
        image = Q(abs(ints[0]),den)
        factors = denominator_factors(int(image.q),primes)
        text = str(image)
        digest.update((str(k)+":"+text+"\n").encode())
        jumps.append({"k":k,"rank_after":len(jumps)+1,
                      "image_numerator_bits":int(image.p).bit_length(),
                      "image_numerator_sha256":hashlib.sha256(str(image.p).encode()).hexdigest(),
                      "image_denominator_factors":factors})
        for p,v in factors:
            rec = by_prime.setdefault(p,{"prime":p,"mod6":p%6,
                                         "first_jump":k,"last_jump":k,
                                         "max_negative_valuation":0,
                                         "sum_negative_valuations":0,
                                         "layers":0})
            rec["last_jump"] = k
            rec["max_negative_valuation"] = max(rec["max_negative_valuation"],v)
            rec["sum_negative_valuations"] += v
            rec["layers"] += 1
        basis = [rowB[1:] for rowB in basis]
        if dim > 1:
            H = fmpz_mat([[basis[i][j] for i in range(N)]
                          for j in range(dim-1)]).hnf()
            basis = [[int(H[j,i]) for j in range(dim-1)] for i in range(N)]
            assert all(sum((row[i]*basis[i][j] for i in range(N)),Q(0)) == 0
                       for j in range(dim-1))
            max_basis_bits = max(max_basis_bits,
                                 max(abs(v).bit_length() for rr in basis for v in rr))
        if len(jumps)%8 == 0 or dim == 1:
            print("R775 D=%s actual rank %s/%s at k=%s" % (D,len(jumps),N,k),
                  file=sys.stderr,flush=True)
    if len(jumps) != N:
        raise AssertionError("Prefix cap did not exhaust the exact rational rank for D=%s" % D)
    summary = [by_prime[p] for p in sorted(by_prime)]
    return {"degree":D,"source_rank":N,"source_labels":labels,
            "parameter":"original t; physical w flag differs by (-1)^k (R769)",
            "cap":cap,"jump_orders":[x["k"] for x in jumps],
            "skipped_zero_rows":zero_rows,
            "exact_image_ideal_sequence_sha256":digest.hexdigest(),
            "maximum_kernel_entry_bits":max_basis_bits,
            "negative_prime_summary":summary,
            "ordinary_negative_outside_2_3_7":[x for x in summary if x["mod6"]==1 and x["prime"]!=7],
            "jumps":jumps,"final_saturated_kernel_rank":0}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--degrees",default="1,2,3,4")
    ap.add_argument("--cap-factor",type=int,default=3)
    ap.add_argument("--workers",type=int,default=4)
    args=ap.parse_args()
    degrees=[int(v) for v in args.degrees.split(",")]
    if not degrees or min(degrees)<1 or max(degrees)>8 or args.cap_factor<2:
        raise ValueError("Explicit finite scope required")
    jobs=[(D,args.cap_factor) for D in degrees]
    with concurrent.futures.ProcessPoolExecutor(max_workers=min(args.workers,len(jobs))) as pool:
        reports=list(pool.map(one_degree,jobs))
    print(json.dumps({"format":"R775 exact ordered rational saturated prefix flags",
                      "python_flint":"0.9.0",
                      "scope":"The displayed finite degrees only; no asymptotic or central nonvanishing claim",
                      "algorithm":"Unimodular gcd on each entire saturated kernel, followed only by row-lattice HNF",
                      "reports":reports,"outputs_persisted":False},
                     separators=(",",":")))

if __name__ == "__main__":
    main()
