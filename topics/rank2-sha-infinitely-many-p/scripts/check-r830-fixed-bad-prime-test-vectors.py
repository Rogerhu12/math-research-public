#!/usr/bin/env python3
"""R830: exact fixed q=3,17 finite cuspidal test-vector norms.
No target ordinary-prime search; no numerical approximations; no saved data.
Run: python scripts/check-r830-fixed-bad-prime-test-vectors.py
The parent publishes/runs this producer through the public small-check workflow.
"""
import hashlib
import json
from fractions import Fraction

class Cyclo:
    def __init__(self, m):
        self.m = m
        self.d = {4: 2, 18: 6}[m]
        self.zero = (0,) * self.d
        self.one = (1,) + (0,) * (self.d - 1)
        self.roots = [self.one]
        x = (0, 1) + (0,) * (self.d - 2)
        for _ in range(1, m):
            self.roots.append(self.mul(self.roots[-1], x))
        assert self.mul(self.roots[-1], x) == self.one

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def scalar(self, n):
        return (n,) + (0,) * (self.d - 1)

    def mul(self, a, b):
        c = [0] * (2 * self.d - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        c[i + j] += x * y
        for k in range(len(c) - 1, self.d - 1, -1):
            v = c[k]
            if not v:
                continue
            c[k] = 0
            if self.m == 4:       # X^2 = -1
                c[k - 2] -= v
            else:                 # Phi_18=X^6-X^3+1
                c[k - 3] += v
                c[k - 6] -= v
        return tuple(c[:self.d])

    def conj(self, a):
        r = self.zero
        for i, v in enumerate(a):
            r = self.add(r, tuple(v*x for x in self.roots[-i % self.m]))
        return r

    def ratio(self, a, den):
        return [str(Fraction(v, den)) for v in a]

def fmul(z, w, q, A, B):
    a, b = z
    c, d = w
    return ((a*c + A*b*d) % q, (a*d+b*c+B*b*d) % q)

def fpow(z, n, q, A, B):
    r = (1, 0)
    while n:
        if n & 1:
            r = fmul(r, z, q, A, B)
        z = fmul(z, z, q, A, B)
        n //= 2
    return r

def canon(g, q):
    first = next(x for x in g if x % q)
    inv = pow(first, -1, q)
    return tuple(x*inv % q for x in g)

def minverse(g, q):
    a,b,c,d = g
    return canon((d,-b,-c,a), q)

def fixed_table(q, A, B, generator, parameters, triples):
    ring = Cyclo(q + 1)
    powers = {}
    z = (1,0)
    for k in range(q*q - 1):
        assert z not in powers
        powers[z] = k
        z = fmul(z, generator, q, A, B)
    assert z == (1,0) and len(powers) == q*q-1
    elliptic = {}
    for z, k in powers.items():
        if z[1] == 0:
            continue
        zq = fpow(z, q, q, A, B)
        tr = ((z[0]+zq[0]) % q, (z[1]+zq[1]) % q)
        norm = fmul(z,zq,q,A,B)
        assert tr[1] == norm[1] == 0
        key = (tr[0], norm[0])
        if key in elliptic:
            old = elliptic[key]
            assert (old-k) % (q+1) == 0 or (old+k) % (q+1) == 0
        else:
            elliptic[key] = k
    assert len(elliptic) == q*(q-1)//2

    G = [(1,b,c,d) for b in range(q) for c in range(q)
         for d in range(q) if (d-b*c) % q]
    G += [(0,1,c,d) for c in range(1,q) for d in range(q)]
    assert len(G) == q*(q*q-1) and len(set(G)) == len(G)
    index = {g:i for i,g in enumerate(G)}

    def character(g, m):
        a,b,c,d = [x % q for x in g]
        det = (a*d-b*c) % q
        assert det
        tr = (a+d) % q
        if b == c == 0 and a == d:
            return ring.scalar(q-1)
        if (tr*tr-4*det) % q == 0:
            return ring.scalar(-1)
        k = elliptic.get((tr,det))
        if k is None:
            return ring.zero
        return ring.neg(ring.add(ring.roots[m*k % (q+1)],
                                 ring.roots[-m*k % (q+1)]))

    chi = {}
    M = {}
    torus_ranks = {}
    digest = hashlib.sha256()
    for m in parameters:
        chi[m] = [character(g,m) for g in G]
        M[m] = []
        for g in G:
            a,b,c,d = g
            total = ring.zero
            for t in range(1,q):
                total = ring.add(total,character((a*t,b,c*t,d),m))
            M[m].append(total)
        torus = ring.zero
        for t in range(1,q):
            torus = ring.add(torus,character((t,0,0,1),m))
        assert torus == ring.scalar(q-1)
        torus_ranks[str(m)] = ring.ratio(torus,q-1)
        for i,g in enumerate(G):
            assert M[m][index[minverse(g,q)]] == ring.conj(M[m][i])
    for i,g in enumerate(G):
        rec = {"g":g,"chi":[chi[m][i] for m in parameters],
               "Tsum":[M[m][i] for m in parameters]}
        digest.update(json.dumps(rec,separators=(",",":"),sort_keys=True).encode()+b"\n")

    results = []
    for label, ms in triples:
        invariant_num = ring.zero
        norm_num = ring.zero
        for i in range(len(G)):
            u = ring.one
            v = ring.one
            for m in ms:
                u = ring.mul(u,chi[m][i])
                v = ring.mul(v,M[m][i])
            invariant_num = ring.add(invariant_num,u)
            norm_num = ring.add(norm_num,v)
        assert invariant_num == ring.scalar(len(G))
        assert ring.conj(norm_num) == norm_num
        den = len(G)*(q-1)**3
        results.append({
            "label":label,"torus_character_indices":ms,
            "invariant_dimension":ring.ratio(invariant_num,len(G)),
            "squared_projector_norm_coefficients":ring.ratio(norm_num,den),
            "norm_numerator":norm_num,"norm_denominator":den,
            "nonzero":norm_num != ring.zero
        })
    return {
        "q":q,"quadratic_field_relation":f"u^2={A}+({B})u",
        "generator":generator,"verified_generator_order":q*q-1,
        "group":"PGL2(F_q)","group_order":len(G),"split_torus_order":q-1,
        "cyclotomic_polynomial":"X^2+1" if q==3 else "X^6-X^3+1",
        "torus_projector_ranks":torus_ranks,
        "fixed_table_sha256":digest.hexdigest(),"triples":results
    }

def main():
    # q=3: all three local representations have the same order-4 cuspidal type.
    q3 = fixed_table(3,-1,0,(1,1),[1],
                     [("all_three_original_triples",[1,1,1])])
    # q=17: theta_f has index 3. theta_{g_j} has index -2(j-9) mod 18.
    # The specified generator is in the basis 1,omega, omega^2+omega+1=0.
    # Any change of primitive generator only permutes the three original rows
    # and possibly replaces an index by its inverse, which leaves the character.
    q17 = fixed_table(17,-1,-1,(2,11),[3,10,16,4],[
        ("lambda_4__g10_h16",[3,16,4]),
        ("lambda_10__g16_h4",[3,4,10]),
        ("lambda_16__g4_h10",[3,10,16])
    ])
    out = {
        "version":"R830-fixed-bad-prime-types-v1",
        "arithmetic_scope":"only fixed residue fields F3 and F17; no target-p scan",
        "formula":"|G|^-1 sum_g product_i (|T|^-1 sum_t chi_i(g t))",
        "inner_product":"Hermitian projector norm; no pointwise absolute-value substitution",
        "results":[q3,q17]
    }
    print(json.dumps(out,separators=(",",":"),sort_keys=True))
if __name__ == "__main__":
    main()
