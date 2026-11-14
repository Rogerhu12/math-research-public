#!/usr/bin/env python3
"""Independent Arb verification of complete real-cusp cover certificates.

This file does not import the cover generator or its Curve class.  It
reconstructs target orbits through the inverse cusp matrix, uses ordinary
pi/sin/cos interval arithmetic, rebuilds every series coefficient, checks
exact adjacent dyadic coverage, and verifies every saved leaf.

The already-certified first-reduction and tail files are linked by SHA256;
their old proofs are not rerun here.  A -2 leaf is accepted only when its
integer j-set is a subset of the saved singleton.  No floating-point value
is used for a decision.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from math import isqrt
from pathlib import Path
import re
import time

from flint import arb, arb_mat, arb_poly, ctx, fmpq


HERE = Path(__file__).resolve().parent
DEFAULT_DATA = HERE / "data"
ALLOWED_LEVELS = (41, 47, 59, 83)


def require(test, message):
    if not test:
        raise AssertionError(message)


def A(x):
    if isinstance(x, Fraction):
        return arb(fmpq(x.numerator, x.denominator))
    return arb(x)


def load_json(path):
    raw = path.read_bytes()
    decoded = gzip.decompress(raw) if path.suffix == ".gz" else raw
    return json.loads(decoded), hashlib.sha256(raw).hexdigest()


def divisors(n):
    out = []
    for a in range(1, isqrt(n) + 1):
        if n % a == 0:
            out.append(a)
            if a * a != n:
                out.append(n // a)
    return sorted(out)


def integer_bounds(ball):
    lo = ball.lower().ceil().unique_fmpz()
    hi = ball.upper().floor().unique_fmpz()
    require(lo is not None and hi is not None, "non-finite integer enclosure")
    return int(lo), int(hi)


def primitive_root(g, p):
    n, factors = p - 1, []
    for r in range(2, isqrt(n) + 1):
        if n % r == 0:
            factors.append(r)
            while n % r == 0:
                n //= r
    if n > 1:
        factors.append(n)
    return all(pow(g, (p - 1) // r, p) != 1 for r in factors)


class IndependentLevel:
    def __init__(self, p, first, tail, terms):
        self.p = p
        self.d = (p - 1) // 2
        self.terms = terms
        self.first = first
        self.tail_record = tail
        self.upper = int(tail["S_uniform"])
        self.g, self.xi = int(first["g"]), int(first["xi"])
        require(primitive_root(self.g, p), "g is not primitive")
        require(pow(self.xi, (p - 1) // 2, p) == p - 1,
                "xi is not a nonsquare")
        require(first["kappa_upper_numerator"] == tail["kappa_upper_numerator"],
                "first/tail kappa mismatch")
        self.kappa = A(Fraction(int(first["kappa_upper_numerator"]), 2**64))
        self.pi = arb.pi()

        # This deliberately does not use sin_pi_fmpq/cos_pi_fmpq.
        self.logs = [None]
        for a in range(1, p):
            v = 2 * (self.pi * a / p).sin()
            require(v > 0, "positive cyclotomic sine not certified")
            self.logs.append(v.log())
        rows = []
        for k in range(self.d):
            r = pow(self.g, k, p)
            rows.append([2 * self.logs[r]] +
                        [self.logs[(j * r) % p] - self.logs[r]
                         for j in range(2, self.d + 1)])
        self.E = arb_mat(rows)
        self.inv = self.E.inv()
        require((self.inv * self.E -
                 arb_mat([[int(i == j) for j in range(self.d)]
                          for i in range(self.d)])).contains(arb_mat(self.d, self.d)),
                "inverse enclosure does not contain the identity")
        for i in range(self.d):
            norm = sum((abs(self.inv[i, j]) for j in range(self.d)), arb(0))
            require(norm < self.kappa, "saved kappa fails independent inverse bound")

        self.cosine = [(2 * self.pi * r / p).cos() for r in range(p)]
        self.phase = [(self.pi * r / p).cos() for r in range(2 * p)]
        self.orbit_index = {}
        for k in range(self.d):
            v = pow(self.g, k, p)
            for sign in (1, -1):
                u = sign * v % p
                require(u not in self.orbit_index, "duplicate orbit norm class")
                self.orbit_index[u] = k
        require(len(self.orbit_index) == p - 1, "incomplete orbit norm classes")

        # An independent truncation length for j.
        self.j_terms = 32
        self.e4 = arb_poly([1] +
                          [240 * sum(d**3 for d in divisors(n))
                           for n in range(1, self.j_terms + 1)])

    def cusp(self, c, matrix):
        p, d, terms = self.p, self.d, self.terms
        require(len(matrix) == 4 and all(type(x) is int and 0 <= x < p
                                        for x in matrix), "invalid cusp matrix")
        aa, bb, cc, dd = matrix
        require((aa * dd - bb * cc) % p == 1, "cusp determinant is not one")
        require((aa * aa - self.xi * cc * cc) % p == c,
                "incorrect cusp norm label")
        a, b = dd, cc * pow(c, -1, p) % p
        require(aa == c * a % p and bb == self.xi * b % p,
                "cusp matrix is not the specified diagonal representative")
        require((a * a - self.xi * b * b) % p == pow(c, -1, p),
                "diagonal norm equation fails")

        # Inverse-matrix enumeration, not the generator's diagonal conic test.
        rows = [[[] for _ in range(p)] for _ in range(d)]
        for x in range(p):
            for y in range(p):
                if x == y == 0:
                    continue
                x0 = (dd * x - cc * y) % p
                y0 = (-bb * x + aa * y) % p
                n0 = (self.xi * x0 * x0 - y0 * y0) % p
                require(n0 != 0, "anisotropic form acquired a nonzero zero")
                rows[self.orbit_index[n0]][x].append(y)

        old = self.first["cusps"][c - 1]
        require(int(old["s"]) == c, "first-reduction cusp labels are unordered")
        slopes, constants = [], []
        for k, row in enumerate(rows):
            require(sum(map(len, row)) == 2 * (p + 1), "wrong orbit cardinality")
            for ys in row:
                require(len(ys) <= 4, "more than four ordinates in a column")
                require(sorted(ys) == sorted((-y) % p for y in ys),
                        "ordinate symmetry fails")
            moment = sum(len(ys) * (6*x*x - 6*p*x + p*p)
                         for x, ys in enumerate(row))
            v = Fraction(-moment, 6*p*p)
            require(v == Fraction(*old["v"][k]), "independent slope mismatch")
            require([[y, 1] for y in row[0]] == old["gamma"][k],
                    "independent constant-term multiplicities mismatch")
            slopes.append(A(v))
            constants.append(2 * sum((self.logs[y] for y in row[0]), arb(0)))
        delta_mat = self.inv * arb_mat([[x] for x in slopes])
        theta_mat = self.inv * arb_mat([[x] for x in constants])
        delta = [delta_mat[i, 0] for i in range(d)]
        theta = [theta_mat[i, 0] for i in range(d)]
        require(delta[0].contains(0) and theta[0].contains(2),
                "norm-coordinate identity fails")

        # Rebuild each N from its complete divisor list.  Inner cosine sums are
        # cached only as a performance improvement; all arguments are exact.
        cache = {}
        s_rows = [[arb(0) for _ in range(terms)] for _ in range(d)]
        for n in range(1, terms + 1):
            for divisor in divisors(n):
                x, r = divisor % p, (n // divisor) % p
                for k in range(d):
                    key = (k, x, r)
                    if key not in cache:
                        cache[key] = sum((self.cosine[y*r % p]
                                          for y in rows[k][x]), arb(0))
                    s_rows[k][n - 1] += divisor * cache[key]
        trans = self.inv * arb_mat(s_rows)
        coeff = [[arb(0)] + [-4 * trans[j, n-1] / n
                             for n in range(1, terms+1)]
                 for j in range(d)]
        return delta, theta, coeff

    def tail(self, lower):
        t = (-A(lower) / self.p).exp()
        require(t > 0 and t < 1, "invalid real-cusp radius")
        u = self.terms + 1
        # Positive-term form, different from the searcher's numerator form.
        return 8 * self.kappa * t**u * (
            (u + 1) / (1 - t) + t / (1 - t)**2)

    def j_ball(self, interval, negative):
        radius = (-interval).exp()
        q = -radius if negative else radius
        require(not q.contains(0), "j parameter enclosure contains zero")
        r = arb(radius.upper())
        n = self.j_terms
        e4_error = (480 * (n+1)**3 * r**(n+1) *
                    (1 + 4*r + r*r) / (1-r)**4)
        e4 = self.e4(q) + arb(0, e4_error.upper())
        prod = arb(1)
        power = arb(1)
        for _ in range(1, n + 1):
            power *= q
            prod *= (1 - power)**(-24)
        log_error = 24 * r**(n+1) / (1-r)**2
        prod *= arb(0, log_error.upper()).exp()
        return e4**3 * prod / q

    def branch(self, c, row, delta, theta, coeff):
        h = row["h"]
        require(type(h) is int and 0 <= h <= self.p, "invalid phase")
        lower = Fraction(int(row["endpoint_numerator"]),
                         int(row["endpoint_denominator"]))
        upper = Fraction(int(row["upper"]))
        require(0 < lower < upper, "invalid root interval")
        require(upper == self.upper, "root upper endpoint not certified tail bound")
        endpoint = self.pi * (arb(3).sqrt() if h % 2 else 2)
        require(endpoint >= A(lower), "lower endpoint omits real-j endpoint")
        span = upper - lower
        phases = [self.phase[(h*n) % (2*self.p)]
                  for n in range(self.terms + 1)]
        polys = [arb_poly([a*b for a, b in zip(co, phases)]) for co in coeff]

        next_fraction = Fraction(0)
        saved_candidates, nonempty_candidates = set(), set()
        coordinate_count = no_j_count = candidate_count = 0
        leaves = row["leaves"]
        require(isinstance(leaves, list) and leaves, "empty branch cover")
        for number, leaf in enumerate(leaves):
            require(isinstance(leaf, list) and len(leaf) in (3, 4),
                    "malformed leaf")
            depth, pos, code = leaf[:3]
            require(type(depth) is int and 0 <= depth <= 512,
                    "invalid dyadic depth")
            require(type(pos) is int and 0 <= pos < 2**depth,
                    "invalid dyadic position")
            require(type(code) is int, "noninteger leaf code")
            left, right = Fraction(pos, 2**depth), Fraction(pos+1, 2**depth)
            require(left == next_fraction,
                    f"gap/overlap in cusp {c}, phase {h}, leaf {number}")
            next_fraction = right
            a, b = lower + span * left, lower + span * right
            interval = A(a).union(A(b))
            if code > 0:
                require(len(leaf) == 3 and code < self.d,
                        "invalid coordinate leaf")
                t = (-interval / self.p).exp()
                error = self.tail(a)
                value = (delta[code] * interval + theta[code] +
                         polys[code](t) + arb(0, error.upper()))
                lo, hi = integer_bounds(value)
                require(lo > hi,
                        f"coordinate leaf fails: p={self.p}, c={c}, h={h}, "
                        f"leaf={number}, coordinate={code}, integers={lo}..{hi}")
                coordinate_count += 1
            elif code == -1:
                require(len(leaf) == 3, "invalid no-j leaf")
                lo, hi = integer_bounds(self.j_ball(interval, bool(h % 2)))
                require(lo > hi,
                        f"no-j leaf fails: p={self.p}, c={c}, h={h}, "
                        f"leaf={number}, integers={lo}..{hi}")
                no_j_count += 1
            elif code == -2:
                require(len(leaf) == 4 and isinstance(leaf[3], str) and
                        re.fullmatch(r"-?[0-9]+", leaf[3]) is not None,
                        "invalid singleton j leaf")
                saved = int(leaf[3])
                saved_candidates.add(saved)
                lo, hi = integer_bounds(self.j_ball(interval, bool(h % 2)))
                require(lo > hi or lo == hi == saved,
                        f"singleton leaf fails: p={self.p}, c={c}, h={h}, "
                        f"leaf={number}, saved={saved}, integers={lo}..{hi}")
                if lo <= hi:
                    nonempty_candidates.add(saved)
                candidate_count += 1
            else:
                raise AssertionError(f"unproved leaf code {code}")
        require(next_fraction == 1, "branch cover does not reach the upper endpoint")
        return {
            "leaves": len(leaves),
            "coordinate_leaves": coordinate_count,
            "no_j_leaves": no_j_count,
            "candidate_leaves": candidate_count,
            "saved_candidates": saved_candidates,
            "nonempty_candidates": nonempty_candidates,
        }


def verify_level(data_dir, p, precision, verbose=True):
    cert_path = data_dir / f"small_levels_real_cover_p{p}.json.gz"
    certificate, certificate_sha = load_json(cert_path)
    first, first_sha = load_json(data_dir / "small_levels_archimedean_reduction.json")
    tail, tail_sha = load_json(data_dir / "small_levels_archimedean_tail.json")
    require(certificate["version"] == 1, "unsupported cover schema")
    require(certificate["p"] == p and p in ALLOWED_LEVELS, "invalid level")
    require(certificate["precision_bits"] == 256, "unexpected search precision")
    require(certificate["terms"] == 12 * p, "unexpected series truncation")
    require(certificate["first_reduction_sha256"] == first_sha,
            "first-reduction SHA256 mismatch")
    require(certificate["tail_sha256"] == tail_sha, "tail SHA256 mismatch")
    require(tail["initial_sha256"] == first_sha, "tail-to-first SHA256 mismatch")
    first_level = next(x for x in first["levels"] if x["p"] == p)
    tail_level = next(x for x in tail["levels"] if x["p"] == p)
    ctx.prec = precision
    level = IndependentLevel(p, first_level, tail_level, certificate["terms"])
    cusps = certificate["cusps"]
    require(len(cusps) == level.d and sorted(x["c"] for x in cusps) ==
            list(range(1, level.d + 1)), "incomplete/duplicate cusp list")
    totals = {"leaves": 0, "coordinate_leaves": 0,
              "no_j_leaves": 0, "candidate_leaves": 0}
    all_saved, all_nonempty = set(), set()
    started = time.monotonic()
    for cusp in sorted(cusps, key=lambda x: x["c"]):
        c = cusp["c"]
        delta, theta, coeff = level.cusp(c, cusp["matrix"])
        branches = cusp["branches"]
        require(len(branches) == p + 1 and sorted(x["h"] for x in branches) ==
                list(range(p + 1)), "incomplete/duplicate phase list")
        for row in sorted(branches, key=lambda x: x["h"]):
            result = level.branch(c, row, delta, theta, coeff)
            for key in totals:
                totals[key] += result[key]
            all_saved.update(result["saved_candidates"])
            all_nonempty.update(result["nonempty_candidates"])
        if verbose:
            print(f"p={p} cusp={c}/{level.d}: cumulative {totals['leaves']} leaves",
                  flush=True)
    out = {
        "p": p,
        "status": "PASS",
        "verification_precision_bits": precision,
        "certificate_sha256": certificate_sha,
        "cusps": level.d,
        "phases_per_cusp": p + 1,
        **totals,
        "saved_candidate_j": sorted(all_saved),
        "nonempty_candidate_j": sorted(all_nonempty),
        "seconds": time.monotonic() - started,
    }
    print(json.dumps(out, sort_keys=True), flush=True)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--levels", default=",".join(map(str, ALLOWED_LEVELS)))
    parser.add_argument("--precision", type=int, default=384)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--summary", type=Path)
    args = parser.parse_args()
    require(args.precision >= 384, "verification requires at least 384 bits")
    levels = tuple(int(x) for x in args.levels.split(",") if x)
    require(levels and len(set(levels)) == len(levels) and
            all(p in ALLOWED_LEVELS for p in levels), "invalid level selection")
    results = [verify_level(args.data_dir, p, args.precision, not args.quiet)
               for p in levels]
    if args.summary:
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        args.summary.write_text(json.dumps(
            {"version": 1, "scope": "all saved real-cusp leaves, independent Arb",
             "levels": results}, sort_keys=True, separators=(",", ":")) + "\n")
    print("PASS: complete cusp/phase coverage and every certified leaf.", flush=True)


if __name__ == "__main__":
    main()

