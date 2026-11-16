#!/usr/bin/env sage-python
"""R883(G): exact reduced-Tate reader for six times a complete closed-point trace.

This is an optional in-process replacement of
    ((1-(-r)^d)//ell) * P
in the original relative-four consumer.  It does not construct a divisor,
change a multiplicity, certify a map, or assume the input point is torsion.
Only the public Actions execution is permitted.  No data files are written.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in the public repository Actions.")

import hashlib
import json
from sage.all import ZZ, GF, matrix, vector


def _canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def _coordinates(c):
    return [int(a) for a in c.polynomial().list()]


def _line_quotient(A, B, field):
    """Return (num_x,num_y,num_0,den_x,den_0) for the true chord/vertical quotient."""
    z, o = field.zero(), field.one()
    if A.is_zero() or B.is_zero():
        return (z, z, o, z, o)
    if A == -B:
        return (o, z, -A[0], z, o)
    if A == B:
        assert 2*A[1] != 0
        slope = (3*A[0]**2)/(2*A[1])
    else:
        assert B[0] != A[0]
        slope = (B[1]-A[1])/(B[0]-A[0])
    S = A+B
    assert not S.is_zero()
    # (Y-y_A-slope*(X-x_A))/(X-x_(A+B)).
    return (-slope, o, slope*A[0]-A[1], o, -S[0])


def _miller_chain(T, ell, field):
    """Precompute only the ell=5/7 addition-chain functions over the true base field."""
    assert ell in (5, 7) and not T.is_zero() and ell*T == T.curve()(0)
    V = T
    chain = []
    for bit in bin(ell)[3:]:
        chain.append((True, _line_quotient(V, V, field)))
        V = V+V
        if bit == "1":
            chain.append((False, _line_quotient(V, T, field)))
            V = V+T
    assert V.is_zero()
    return tuple(chain)


def _evaluate_miller(chain, point, embed, target_field):
    assert not point.is_zero()
    x, y = point[0], point[1]
    value = target_field.one()
    for square, coefficients in chain:
        if square:
            value *= value
        ax, ay, a0, bx, b0 = [embed(c) for c in coefficients]
        numerator = ax*x+ay*y+a0
        denominator = bx*x+b0
        # The auxiliary-point rule excludes the support of every intermediate line.
        assert numerator != 0 and denominator != 0
        value *= numerator/denominator
    return value


class OriginalTateTraceReader:
    """Read [6] Tr_{F_(r^(2d))/F_(r^2)} P in the SAME original torsion basis."""

    def __init__(self, torsion, prime):
        self.r = int(prime)
        self.ell = int(torsion["ell"])
        assert (self.r, self.ell) in ((29, 5), (41, 7))
        self.E = torsion["curve"]
        self.k = self.E.base_ring()
        self.q = ZZ(self.r)**2
        assert self.k.cardinality() == self.q
        self.basis = tuple(torsion["basis"])
        assert len(self.basis) == 2
        self.coordinate_table = torsion["coordinates"]
        assert len(self.coordinate_table) == self.ell**2
        assert self.coordinate_table[self.basis[0]] == (1, 0)
        assert self.coordinate_table[self.basis[1]] == (0, 1)
        self.fp = GF(self.ell)
        self.chains = tuple(_miller_chain(T, self.ell, self.k) for T in self.basis)
        self.cyclic_groups = tuple(
            tuple(j*T for j in range(self.ell)) for T in self.basis)
        self.auxiliary = (self.basis[1], self.basis[0])
        for i in range(2):
            assert self.auxiliary[i] not in self.cyclic_groups[i]

        self.xi = self.k.multiplicative_generator()**((self.q-1)//self.ell)
        assert self.xi != 1 and self.xi**self.ell == 1
        self.root_powers = tuple(self.xi**j for j in range(self.ell))
        assert len(set(self.root_powers)) == self.ell

        # Actual pairing values, not an assumed Weil pairing convention.
        identity_embedding = lambda c:self.k(c)
        columns = [self._pairing_logs(P, self.k, identity_embedding, 1)[0]
                   for P in self.basis]
        self.M = matrix(self.fp, 2, 2,
                        lambda i, j:columns[j][i])
        assert self.M.det() != 0
        self.M_inverse = self.M.inverse()
        self.total_closed_calls = 0
        self.maximum_residue_degree = 0
        self.divisible_degree_calls = 0
        self.second_auxiliary_choices = 0
        self.calibration = {
            "prime":self.r, "ell":self.ell,
            "fixed_base_cardinality":str(self.q),
            "xi_ell":_coordinates(self.xi),
            "actual_pairing_matrix":[[int(c) for c in row] for row in self.M.rows()],
            "actual_pairing_matrix_inverse":[
                [int(c) for c in row] for row in self.M_inverse.rows()],
            "basis_coordinates":[
                [_coordinates(T[0]), _coordinates(T[1])] for T in self.basis],
            "base_non_degeneracy":"Frob_(r^2)=-r; t1(T,P)=epsilon(T,-6P)",
            "complete_degree_norm_compatibility":True,
        }
        self.calibration["sha256"] = hashlib.sha256(
            _canonical(self.calibration).encode()).hexdigest()

    @staticmethod
    def _embed_point(P, target_curve, embed):
        if P.is_zero():
            return target_curve(0)
        return target_curve([embed(P[0]), embed(P[1])])

    def _pairing_logs(self, P, target_field, embed, degree):
        """Full k_d reduced pairing; no reduction of degree modulo ell."""
        degree = int(degree)
        assert degree >= 1
        assert target_field.cardinality() == self.q**degree
        assert P.curve().base_ring() == target_field
        assert embed(self.k.one()) == target_field.one()
        if P.is_zero():
            return vector(self.fp, [0, 0]), [None, None]
        target_curve = P.curve()
        roots = [embed(c) for c in self.root_powers]
        assert len(set(roots)) == self.ell
        root_log = {c:j for j, c in enumerate(roots)}
        exponent = (self.q**degree-1)//self.ell
        assert self.ell*exponent == self.q**degree-1
        values, chosen_auxiliary = [], []
        for i in range(2):
            subgroup = {
                self._embed_point(T, target_curve, embed)
                for T in self.cyclic_groups[i]}
            U = self._embed_point(self.auxiliary[i], target_curve, embed)
            assert U not in subgroup
            found = None
            for multiplier in (1, 2):
                R = multiplier*U
                Z = P+R
                if R not in subgroup and Z not in subgroup:
                    found = (multiplier, R, Z)
                    break
            assert found is not None
            multiplier, R, Z = found
            numerator = _evaluate_miller(self.chains[i], Z, embed, target_field)
            denominator = _evaluate_miller(self.chains[i], R, embed, target_field)
            ratio = numerator/denominator
            assert ratio != 0
            reduced = ratio**exponent
            assert reduced**self.ell == 1
            assert reduced in root_log
            values.append(root_log[reduced])
            chosen_auxiliary.append(multiplier)
        return vector(self.fp, values), chosen_auxiliary

    def six_trace(self, P, residue_field, base_embedding, residue_degree):
        """Return the exact base-field point [6]Tr(P), with a compact audit record.

        base_embedding MUST be the actual residue embedding, for example
        lambda c: to_kQ(L(c)).  Do not choose an unrelated field isomorphism.
        The caller retains the original full intersection multiplicity.
        """
        d = int(residue_degree)
        logs, chosen = self._pairing_logs(P, residue_field, base_embedding, d)
        coordinate = self.M_inverse*(self.fp(6)*logs)
        point = ZZ(coordinate[0])*self.basis[0]+ZZ(coordinate[1])*self.basis[1]
        assert self.ell*point == self.E(0)
        assert self.coordinate_table[point] == tuple(int(c) for c in coordinate)
        self.total_closed_calls += 1
        self.maximum_residue_degree = max(self.maximum_residue_degree, d)
        if d % self.ell == 0:
            self.divisible_degree_calls += 1
        self.second_auxiliary_choices += sum(c == 2 for c in chosen)
        numerator = self.q**d-1
        assert numerator % self.ell == 0
        audit = {
            "trace_method":"R883G_reduced_Tate_with_full_residue_degree",
            "residue_degree":d,
            "degree_divisible_by_ell":bool(d % self.ell == 0),
            "reduced_pairing_exponent_bits":int((numerator//self.ell).nbits()),
            "pairing_logs":[int(c) for c in logs],
            "auxiliary_multipliers":chosen,
            "six_trace_coordinates":[int(c) for c in coordinate],
        }
        return point, audit

    def summary(self):
        return {
            "calibration":self.calibration,
            "closed_point_calls":self.total_closed_calls,
            "maximum_residue_degree":self.maximum_residue_degree,
            "ell_divisible_degree_calls":self.divisible_degree_calls,
            "second_auxiliary_choices":self.second_auxiliary_choices,
            "norm_compatibility_preserves_complete_trace":True,
        }
