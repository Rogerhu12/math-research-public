#!/usr/bin/env sage-python
"""Exact normalized G3, and a two-section pencil certified on its whole zero scheme."""
import os
if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Run only in the named public research Actions.")
import numpy as np
from original_short_graph_field import PackedField
from original_short_graph_kernel import left_kernel, paired_pivots, prime_rows, prime_rref
from original_descended_pencil_sections import require, coefficients, pack_polys, packed_hash


def packed_rank(field, rows):
    _, pivots = prime_rref(field.p, prime_rows(field, rows))
    return len(paired_pivots(field, pivots, rows.shape[2]))


def normalized_source(two_or_three, size, field):
    values = np.zeros((field.f, len(two_or_three), size), dtype=np.uint8)
    values[0] = pack_polys(two_or_three, size)
    return values


def certify_g3(sections, qf, degree, genus, pole_degree):
    length = 3*degree + pole_degree + 1
    three = sections["three"]
    dim = len(three)
    nullity = 3*degree - pole_degree + 1 - genus
    require(3*degree-pole_degree >= 2*genus and qf.precision_absolute() >= length and
            qf[0] and sections["length"] >= length and dim == 3*degree+1-genus,
            "Unpaid degree, pole, or genuine full G3 germ")
    field = PackedField(qf.base_ring())
    require(int(sections["ring"].base_ring().characteristic()) == field.p, "Wrong source constants")
    poly = sections["ring"]
    coordinates = np.asarray([field.coords(qf[j]) for j in range(length)], dtype=np.uint8).T
    eq = np.zeros((field.f, 2*dim, length), dtype=np.uint8)
    for a in range(field.f):
        multiplier = poly(coordinates[a].tolist())
        for i, h in enumerate(three):
            eq[a, i] = coefficients(multiplier*h.truncate(length), length)
    # Each true equation is (q*f)(q^3 h) - q(q^3 x).
    eq[0, dim:, 1:] = (-pack_polys(three, length-1).astype(np.int64)) % field.p
    K, proof = left_kernel(field, eq)
    require(K.shape == (field.f, nullity, 2*dim) and proof["original_rank"] == 2*dim-nullity and
            packed_rank(field, K[:, :, :dim]) == nullity and packed_rank(field, K[:, :, dim:]) == nullity,
            "The complete G3 or one of its actual projections failed")
    return field, K, dict(germ_sha256=packed_hash(coordinates), equation_sha256=packed_hash(eq),
                          kernel_sha256=packed_hash(K), full_kernel_proof=proof,
                          actual_complete_kernel_dimension=nullity, both_projections_injective=True,
                          true_equation_coefficients=length)


class WholePencil:
    """Every test measures the complete gcd divisor, including its multiplicities."""
    def __init__(self, field, sections, degree, genus, pole_degree):
        self.field = field
        self.poly = sections["ring"]
        self.two = sections["two"]
        self.dim = len(sections["three"])
        self.divisor_degree = 3*degree-pole_degree
        self.target_degree = 5*degree-pole_degree
        self.target_rank = self.target_degree+1-genus
        self.window = self.target_degree+1
        require(self.divisor_degree >= 2*genus and 2*degree-self.divisor_degree > 2*genus-2 and
                self.divisor_degree < field.p**field.f and sections["length"] >= self.window+1,
                "Missing whole-scheme pencil hypotheses or adequate normalized jets")
        self.three = normalized_source(sections["three"], self.window+1, field)

    def multiplier_rows(self, h):
        field = self.field
        normalized = field.product(h[:, None, :self.dim], self.three)[:, 0, :]
        # Since h cancels the simple pole, q^3 h has a factor q. The
        # faithful normalized q^4 h W2 rows are ((q^3 h)/q)*(q^2 W2).
        require(not np.any(normalized[:, 0]), "A section is missing its mandatory zero at the marked point")
        rows = np.zeros((field.f, len(self.two), self.window), dtype=np.uint8)
        for a in range(field.f):
            first = self.poly(normalized[a, 1:].tolist())
            for i, w in enumerate(self.two):
                rows[a, i] = coefficients(first*w.truncate(self.window), self.window)
        return rows

    def select(self, K):
        field = self.field
        first = np.ascontiguousarray(K[:, 0, :])
        fixed = self.multiplier_rows(first)
        tested = []
        def trial(second):
            incoming = self.multiplier_rows(second)
            rank = packed_rank(field, np.concatenate((fixed, incoming), axis=1))
            require(0 <= self.target_rank-rank <= self.divisor_degree, "Impossible base divisor length")
            tested.append([packed_hash(second), rank])
            return rank
        # Deterministic trials are accepted solely by the full rank certificate.
        # If none succeeds, the bounded basis sweep below is independent of any RNG.
        seed = int(packed_hash(K)[:16], 16)
        random = np.random.default_rng(seed)
        for _ in range(12):
            scalars = random.integers(field.p, size=(field.f, 1, K.shape[1]), dtype=np.uint8)
            candidate = field.product(scalars, K)[:, 0, :].astype(np.uint8)
            if trial(candidate) == self.target_rank:
                return self.finish(first, candidate, fixed, tested, "verified deterministic initial trials")
        second = np.zeros_like(first)
        for j in range(K.shape[1]):
            best, best_rank = None, -1
            for number in range(self.divisor_degree+1):
                digits = [(number // field.p**a) % field.p for a in range(field.f)]
                additive = field.scalar_times(digits, K[:, j, :])
                candidate = ((second.astype(np.int64)+additive) % field.p).astype(np.uint8)
                rank = trial(candidate)
                if rank == self.target_rank:
                    return self.finish(first, candidate, fixed, tested, "verified bounded basis sweep")
                if rank > best_rank:
                    best, best_rank = candidate, rank
            require(best is not None, "Empty finite-field coefficient sweep")
            second = best
        raise ArithmeticError("The complete source did not generate its actual line bundle")

    def finish(self, first, second, fixed, trials, selection):
        rows = np.concatenate((fixed, self.multiplier_rows(second)), axis=1)
        require(packed_rank(self.field, rows) == self.target_rank, "Final whole basepoint-free check failed")
        from section_quotient_algebra import digest
        return [first, second], dict(selection=selection, actual_independent_multiplier_rank=self.target_rank,
              true_product_coefficients=self.window, full_product_rows=int(rows.shape[1]),
              full_product_rows_sha256=packed_hash(rows), first_paired_section_sha256=packed_hash(first),
              second_paired_section_sha256=packed_hash(second), checked_combinations=len(trials),
              checked_combination_rank_stream_sha256=digest(trials), whole_base_divisor_length=0)
