#!/usr/bin/env python3
"""R790: original CM values and first coarse jets, in public Actions only.

Read the completed original U modulus, oriented Weil pairing and M2 recipes.
Lift only the new epsilon jets.  The original 5040-term half trace is evaluated
by its proved C3 projection and the two exact degree-280 field traces.
No original y value, beta point, or height is claimed by this producer.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_poly

RESULT = "R790-original-CM-fiber-jets"
FINAL = "p41-original-CM-fiber-jets-certificate.json"
P, LEVEL, DEGREE, ORDER, DIMENSION = 41, 82, 280, 5, 146
SCALE = LEVEL**2
FIELD_CORE_SHA = "f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251"
INPUTS = {
    "R735": "p41-original-torsion-modulus.json.gz",
    "R754": "R754-original-Weil-pairing.json.gz",
    "R771": "R771-original-level82-Eisenstein-label-group.json.gz",
    "R775": "R775-basis-M2.json.gz",
}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Mathematical execution belongs to public repository Actions.")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))+"\n").encode("utf-8")
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb",
                               mtime=0, compresslevel=2) as compressed:
                compressed.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def rational(value):
    return [str(value.numer()), str(value.denom())]


class BudgetStop(RuntimeError):
    pass


class Jet:
    """A truncated epsilon series over the retained exact field K(U)."""
    __slots__ = ("F", "n", "c")

    def __init__(self, field, coefficients, precision):
        self.F, self.n = field, int(precision)
        assert self.n > 0
        coefficients = tuple(coefficients)
        self.c = tuple(field.elt(value) for value in coefficients[:self.n]) + \
                 (field.zero,)*max(0, self.n-len(coefficients))

    @classmethod
    def constant(cls, field, value, precision):
        return cls(field, (value,), precision)

    @classmethod
    def decode(cls, field, value):
        assert value["epsilon_precision"] == len(value["coefficients"])
        return cls(field, [field.decode(c) for c in value["coefficients"]],
                   value["epsilon_precision"])

    def encode(self):
        return {"epsilon_precision": self.n,
                "coefficients": [value.encode() for value in self.c]}

    def cut(self, precision):
        return Jet(self.F, self.c, precision)

    def scalar(self, value):
        return Jet.constant(self.F, value, self.n)

    def other(self, value):
        if isinstance(value, Jet):
            assert value.F is self.F and value.n == self.n
            return value
        return self.scalar(value)

    def __bool__(self):
        return any(self.c)

    def __eq__(self, other):
        other = self.other(other)
        return self.c == other.c

    def __neg__(self):
        return Jet(self.F, [-x for x in self.c], self.n)

    def __add__(self, other):
        other = self.other(other)
        return Jet(self.F, [x+y for x, y in zip(self.c, other.c)], self.n)

    __radd__ = __add__

    def __sub__(self, other):
        return self+(-self.other(other))

    def __rsub__(self, other):
        return self.other(other)-self

    def __mul__(self, other):
        if not isinstance(other, Jet):
            other = self.F.elt(other)
            return Jet(self.F, [x*other if x else self.F.zero for x in self.c], self.n)
        other = self.other(other)
        out = [self.F.zero for _ in range(self.n)]
        if other is self:
            for i, x in enumerate(self.c):
                if not x:
                    continue
                if 2*i < self.n:
                    out[2*i] += x*x
                for j in range(i+1, self.n-i):
                    if self.c[j]:
                        out[i+j] += 2*(x*self.c[j])
        else:
            for i, x in enumerate(self.c):
                if x:
                    for j in range(self.n-i):
                        if other.c[j]:
                            out[i+j] += x*other.c[j]
        return Jet(self.F, out, self.n)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        exponent = int(exponent)
        if exponent < 0:
            return self.inverse()**(-exponent)
        out, value = self.scalar(1), self
        while exponent:
            if exponent & 1:
                out = out*value
            exponent >>= 1
            if exponent:
                value = value*value
        return out

    def inverse(self):
        assert self.c[0], "Only a unit epsilon series is inverted"
        leading_inverse = self.c[0].inverse()
        out = [leading_inverse]
        for n in range(1, self.n):
            value = self.F.zero
            for j in range(1, n+1):
                if self.c[j] and out[n-j]:
                    value += self.c[j]*out[n-j]
            out.append(-leading_inverse*value)
        return Jet(self.F, out, self.n)

    def __truediv__(self, other):
        if isinstance(other, (int, fmpq)):
            assert other != 0
            return Jet(self.F, [value/other for value in self.c], self.n)
        if isinstance(other, Jet):
            return self*other.inverse()
        return self*self.F.elt(other).inverse()

    def __rtruediv__(self, other):
        return self.inverse()*other

    def shift(self, amount):
        assert amount >= 0
        return Jet(self.F, (self.F.zero,)*amount+self.c, self.n)

    def rotate(self, amount=1):
        """Substitute epsilon -> zeta^amount epsilon, with coefficients fixed."""
        units = (self.F.one, self.F.zeta, self.F.zeta**2)
        return Jet(self.F, [c*units[(amount*n) % 3] if c else self.F.zero
                           for n, c in enumerate(self.c)], self.n)

    def square_root_one(self):
        assert self.c[0] == 1
        out = [self.F.one]
        for n in range(1, self.n):
            cross = self.F.zero
            for j in range(1, n):
                cross += out[j]*out[n-j]
            out.append((self.c[n]-cross)/2)
        value = Jet(self.F, out, self.n)
        assert value*value == self
        return value


def curve_y(r, B, d_inverse):
    epsilon = Jet(r.F, [0, 1], r.n)
    return ((r*r*r+epsilon*r+B)*d_inverse).square_root_one()


def add_points(first, second, d0, doubling=False, d_inverse=None):
    """Nonexceptional group law; return point and actual weight-one slope."""
    r, v = first
    u, w = second
    assert r.F is u.F and r.n == u.n
    if doubling:
        assert r == u and v == w
        epsilon = Jet(r.F, [0, 1], r.n)
        slope = (3*r*r+epsilon)/(2*v)
        normalized = slope*(d_inverse if d_inverse is not None else d0.inverse())
    else:
        assert (u-r).c[0], "The selected distinct 41-torsion points are not opposite"
        normalized = (w-v)/(u-r)
        slope = normalized*d0
    new_r = normalized*normalized*d0-r-u
    new_v = -v+normalized*(r-new_r)
    return (new_r, new_v), slope


def short_forty(point, d0, d_inverse):
    """New-jet chain 1,2,4,5,10,20,40, without any division polynomial."""
    two, _ = add_points(point, point, d0, doubling=True, d_inverse=d_inverse)
    four, _ = add_points(two, two, d0, doubling=True, d_inverse=d_inverse)
    five, _ = add_points(four, point, d0, d_inverse=d_inverse)
    ten, _ = add_points(five, five, d0, doubling=True, d_inverse=d_inverse)
    twenty, _ = add_points(ten, ten, d0, doubling=True, d_inverse=d_inverse)
    forty, _ = add_points(twenty, twenty, d0, doubling=True, d_inverse=d_inverse)
    return forty


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.config = read(args.config)
        assert self.config["result"] == RESULT and self.config["p"] == P
        assert self.config["producer_inputs_pending"] is False
        assert self.config["cm_jet_order"] == ORDER
        assert self.config["core_sha256"] == sha(__file__)
        assert self.config["R790_proof_sha256"] == sha(args.proof)
        assert self.config["field_core_sha256"] == sha(args.field_core) == FIELD_CORE_SHA
        self.tag = {"result": RESULT, "source_sha256": sha(__file__),
            "python_flint": flint.__version__, "R790_proof_sha256": sha(args.proof),
            "field_core_sha256": sha(args.field_core), "cm_jet_order": ORDER,
            "retained_artifacts": self.config["retained_artifacts"]}
        module_spec = importlib.util.spec_from_file_location("R790_retained_field", args.field_core)
        self.old = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(self.old)
        self.data, self.input_files = self.inputs()
        modulus = self.old.dp(self.data["R735"][INPUTS["R735"]]["monic_U_modulus"])
        assert modulus.degree() == DEGREE and modulus[DEGREE] == 1
        self.F = self.old.QKField(modulus)
        self.B, self.d = self.F.gen/4, self.F.one+self.F.gen/4
        self.d_inverse = self.d.inverse()
        self.s = 1+2*self.F.zeta
        self.c = 3*self.B/(8*self.d)
        self.coarse_factor = -81*self.B*self.B
        self.xi = self.F.decode(self.data["R754"][INPUTS["R754"]]["xi"])
        # Read the proved orientation; these are multiplications in the NEW trace,
        # not a repeated Miller/Weil-pairing calculation.
        self.xi82 = -(self.xi**21)
        self.phase_cache = {0: self.F.one, 1: self.xi82}
        self.modulus_derivative = modulus.derivative()
        self.recipes = [row["recipe"] for row in self.data["R775"][INPUTS["R775"]]["basis"]]
        assert len(self.recipes) == DIMENSION
        self.seeds = {}
        for recipe in self.recipes:
            assert recipe["kind"] == "det_semilinear_E1_pair_trace"
            assert recipe["phase"] == "xi82^(j*det(g)_mod82)"
            assert recipe["exact_global_field"] == "K"
            assert 0 <= recipe["j"] < 40
            index = int(recipe["R771_seed_index"])
            pair = (tuple(recipe["lambda"]), tuple(recipe["mu"]))
            if index in self.seeds:
                assert self.seeds[index] == pair
            self.seeds[index] = pair
        # Actual accepted R775 rows use five seeds.  Twelve candidate seed-image
        # stages in that producer are not twelve seeds in the retained basis.
        assert set(self.seeds) == {0, 1, 2, 3, 11}
        self.multiple_cache, self.point_cache, self.pair_cache = {}, {}, {}
        self.P1, self.eP = None, None

    def inputs(self):
        assert set(self.config["retained_artifacts"]) == {"R735", "R754", "R771", "R775"}
        all_data, records = {}, []
        for label, producer in self.config["retained_artifacts"].items():
            directory = self.args.retained/label
            manifest_path = directory/"full-outputs-manifest.json"
            assert sha(manifest_path) == producer["manifest_sha256"]
            manifest = read(manifest_path)
            assert manifest["result"] == producer["result"]
            entries = {row["file"]: row for row in manifest["files"]}
            data = {}
            for name, digest in producer["files"].items():
                assert Path(name).name == name
                path = directory/name
                assert entries[name]["sha256"] == digest == sha(path)
                assert path.stat().st_size == entries[name]["bytes"]
                data[name] = read(path)
                records.append(dict(file_spec(path), producer=label))
            cert = data[producer["certificate_name"]]
            assert cert["complete"] is True
            if label == "R735":
                identity = cert["identity"]
                assert identity["source_sha256"] == producer["core_sha256"]
                assert identity["p"] == P and identity["torsion_degree"] == DEGREE
                assert identity["python_flint"] == "0.9.0"
                assert data[INPUTS[label]]["identity"] == identity
                assert cert["torsion_modulus_sha256"] == producer["files"][INPUTS[label]]
            else:
                tag = cert["configuration"]
                assert tag["source_sha256"] == producer["core_sha256"]
                assert tag["python_flint"] == "0.9.0"
                stages = {row["file"]: row for row in cert["stages"]}
                for name, value in data.items():
                    if name == producer["certificate_name"]:
                        continue
                    assert value["complete"] is True and value["configuration"] == tag
                    assert stages[name]["sha256"] == producer["files"][name]
            all_data[label] = data
        pairing = all_data["R754"][INPUTS["R754"]]
        assert pairing["analytic_orientation"] == "exp(2*pi*i/41), by R751 sigma and Legendre proof"
        assert pairing["p_power_equals_one"] is True and pairing["not_one"] is True
        group = all_data["R771"][INPUTS["R771"]]
        assert len(group["H82_mod_center"]) == 126 and len(group["H82"]) == 252
        assert group["original_tame_C"] == [0, 1, 1, 1]
        assert group["all_group_determinants_one_mod82"] is True
        basis = all_data["R775"][INPUTS["R775"]]
        assert basis["rank"] == DIMENSION
        assert basis["characteristic_zero_independence_certified_by_unit_reduction"] is True
        cosets = all_data["R775"]["R775-determinant-cosets.json.gz"]
        assert len(cosets["cosets"]) == 40 and cosets["GL_group_order"] == 10080
        assert cosets["original_mod2_component"] == "identity"
        assert cosets["original_mod41_component"] == \
            "matrix(a,-b;b,a+b), norm a^2+a*b+b^2"
        assert cosets["all_representatives_normalize_original_H82"] is True
        return all_data, records

    def budget(self):
        if time.monotonic()-self.started > 60*self.args.budget_minutes:
            raise BudgetStop("Completed exact CM stages retained; resume the same configuration")

    def path(self, name):
        assert name.startswith("R790-") and Path(name).name == name
        return self.out/(name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["configuration"] == self.tag and value["complete"] is True
        return value

    def store(self, name, value):
        value = dict(value, configuration=self.tag, complete=True)
        save(self.path(name), value)
        print(json.dumps({"stage": name, "complete": True,
                          "elapsed_seconds": round(time.monotonic()-self.started, 3)}), flush=True)
        return value

    def constant(self, value, precision=ORDER+1):
        return Jet.constant(self.F, value, precision)

    def decode(self, value):
        return Jet.decode(self.F, value)

    def curve_check(self, point):
        r, v = point
        epsilon = Jet(self.F, [0, 1], r.n)
        assert v*v*self.d == r*r*r+epsilon*r+self.B

    def lift_torsion(self):
        final = self.cached("R790-original-P-torsion-jet")
        if final:
            self.P1 = (self.decode(final["r"]), self.decode(final["v"]))
            return self.P1
        r, old_precision = self.constant(1, 1), 1
        for precision in (2, 4, 6):
            name = "R790-torsion-r-precision-"+str(precision).zfill(2)
            prior = self.cached(name)
            if prior:
                next_r = self.decode(prior["r"])
                assert next_r.n == precision and next_r.cut(old_precision) == r
            else:
                self.budget()
                candidate = r.cut(precision)
                v = curve_y(candidate, self.B, self.d_inverse)
                (r40, v40) = short_forty((candidate, v), self.d, self.d_inverse)
                error = r40-candidate
                assert not error.cut(old_precision)
                assert not (v40+v).cut(old_precision)
                next_r = candidate+error/P
                self.store(name, {"epsilon_precision": precision,
                    "previous_precision": old_precision, "r": next_r.encode(),
                    "old_precision_residual_and_negative_branch_verified": True,
                    "root_derivative_identity": "F_r=-41 at the original exact root, for every epsilon",
                    "update": "r_new=r+(r40-r)/41",
                    "old_torsion_modulus_recomputed": False})
            r, old_precision = next_r, precision
        self.P1 = (r, curve_y(r, self.B, self.d_inverse))
        self.curve_check(self.P1)
        # These exact point/multiplier stages are reused by e(P), all labels,
        # and continuations.  The final chain is never calculated twice.
        forty, M40 = self.multiple(40)
        assert forty[0] == self.P1[0] and forty[1] == -self.P1[1]
        self.store("R790-original-P-torsion-jet", {
            "r": self.P1[0].encode(), "v": self.P1[1].encode(),
            "epsilon_precision": ORDER+1, "original_constant_point": [1, 1],
            "exact_40P_equals_negative_P_verified": True,
            "formal_curve_equation_verified": True,
            "same_completed_multiplication_chain_used_for_E1": True})
        return self.P1

    def multiple(self, n):
        """Point [n]P and M_n with e([n]P)=n e(P)-M_n; 1<=n<=40."""
        assert 1 <= n <= 40 and self.P1 is not None
        if n in self.multiple_cache:
            return self.multiple_cache[n]
        name = "R790-P-multiple-"+str(n).zfill(2)
        prior = self.cached(name)
        if prior:
            assert prior["multiplier"] == n
            point = self.decode(prior["r"]), self.decode(prior["v"])
            M = self.decode(prior["accumulated_slope"])
        elif n == 1:
            point, M = self.P1, self.constant(0)
        else:
            self.budget()
            if n % 2 == 0:
                half, Mh = self.multiple(n//2)
                point, slope = add_points(half, half, self.d, doubling=True,
                                          d_inverse=self.d_inverse)
                M = 2*Mh+slope
                parents = [n//2, n//2]
            else:
                previous, Mp = self.multiple(n-1)
                point, slope = add_points(previous, self.P1, self.d,
                                          d_inverse=self.d_inverse)
                M = Mp+slope
                parents = [n-1, 1]
            self.curve_check(point)
            self.store(name, {"multiplier": n, "parents": parents,
                "r": point[0].encode(), "v": point[1].encode(),
                "accumulated_slope": M.encode(),
                "formal_curve_equation_verified": True,
                "identity": "e(nP)=n*e(P)-M_n with original invariant differential"})
        self.multiple_cache[n] = point, M
        return point, M

    def normalize_eP(self):
        prior = self.cached("R790-original-E1-P-jet")
        if prior:
            self.eP = self.decode(prior["e_P"])
            return self.eP
        self.budget()
        forty, M40 = self.multiple(40)
        assert forty[0] == self.P1[0] and forty[1] == -self.P1[1]
        self.eP = M40/P
        assert 40*self.eP-M40 == -self.eP
        self.store("R790-original-E1-P-jet", {
            "e_P": self.eP.encode(), "exact_e40P_equals_negative_eP_verified": True,
            "completed_zeta_linear_terms_preserved_by_addition": True,
            "normalization": "E1_alg=-completed_zeta; e(P)=M40/41"})
        return self.eP

    def signed_multiple(self, residue, rotated=False):
        assert residue % P
        integer = residue % P
        if integer > P//2:
            integer -= P
        point, M = self.multiple(abs(integer))
        r, v = point
        e = abs(integer)*self.eP-M
        if integer < 0:
            v, e = -v, -e
        if rotated:
            r, v = r.rotate()*self.F.zeta, v.rotate()
            e = e.rotate()*(self.F.zeta**2)
        return r, v, e

    def point(self, a, b):
        """Actual 41-part a Q+b P; cache the four features used by pair traces."""
        a, b = a % P, b % P
        assert (a, b) != (0, 0)
        key = (a, b)
        if key in self.point_cache:
            return self.point_cache[key]
        name = "R790-point41-"+str(a).zfill(2)+"-"+str(b).zfill(2)
        prior = self.cached(name)
        if prior:
            assert prior["label_Q_P"] == [a, b]
            value = {field: self.decode(prior[field])
                     for field in ("e", "inverse_v", "r_over_v", "r_squared_over_v")}
        else:
            self.budget()
            if a == 0:
                r, v, e = self.signed_multiple(b)
            elif b == 0:
                r, v, e = self.signed_multiple(a, rotated=True)
            else:
                rQ, vQ, eQ = self.signed_multiple(a, rotated=True)
                rP, vP, eP = self.signed_multiple(b)
                (r, v), slope = add_points((rQ, vQ), (rP, vP), self.d,
                                          d_inverse=self.d_inverse)
                e = eQ+eP-slope
            self.curve_check((r, v))
            inverse_v = v.inverse()
            assert v*inverse_v == 1
            r_over_v = r*inverse_v
            value = {"e": e, "inverse_v": inverse_v, "r_over_v": r_over_v,
                     "r_squared_over_v": r*r_over_v}
            self.store(name, {"label_Q_P": [a, b],
                **{field: item.encode() for field, item in value.items()},
                "formal_curve_equation_verified": True,
                "point_y_unit_inverse_verified": True,
                "completed_zeta_addition_used": True})
        self.point_cache[key] = value
        return value

    def pair_phi(self, first, second, parity_first, parity_second):
        e, f, g, h = (first[name] for name in
                      ("e", "inverse_v", "r_over_v", "r_squared_over_v"))
        E, F, G, H = (second[name] for name in
                      ("e", "inverse_v", "r_over_v", "r_squared_over_v"))
        zero = (0, 0)
        if parity_first == zero and parity_second == zero:
            return 3*e*E
        if parity_first == zero:
            return e*(3*(E-H)-F.shift(1))
        if parity_second == zero:
            return E*(3*(e-h)-f.shift(1))
        indices = {(0, 1): 0, (1, 0): 1, (1, 1): 2}
        difference = (indices[parity_second]-indices[parity_first]) % 3
        cross1, cross2 = g*F, f*G
        linear = (h-e)*F+f*(H-E)
        base = 3*(e-h)*(E-H)
        if difference == 0:
            return base+(linear-2*g*G).shift(1)+(f*F).shift(2) \
                   -(cross1+cross2)*(3*self.B)
        sign = 1 if difference == 1 else -1
        delta = self.constant(3*self.s*self.B) + \
                self.constant(2*self.s/(9*self.B)).shift(3)
        epsilon = Jet(self.F, [0, 1], ORDER+1)
        assert delta*delta == self.constant(-27*self.B*self.B)-4*(epsilon**3)
        return base+(linear+g*G).shift(1)+(cross1+cross2)*(3*self.B/2) \
               +delta*(cross1-cross2)*(sign*fmpq(1, 2))

    def pair(self, seed_index, reflected):
        key = seed_index, bool(reflected)
        if key in self.pair_cache:
            return self.pair_cache[key]
        name = "R790-seed-pair-"+str(seed_index).zfill(3)+("-F" if reflected else "-I")
        prior = self.cached(name)
        if prior:
            assert prior["R771_seed_index"] == seed_index
            assert prior["reflected_mod41_only"] is bool(reflected)
            value = self.F.decode(prior["value_before_field_trace"])
            derivative = self.F.decode(prior["coarse_derivative_before_field_trace"])
        else:
            self.budget()
            labels = self.seeds[seed_index]
            coordinates, parities = [], []
            for a, b in labels:
                parities.append((a % 2, b % 2))
                if reflected:
                    a, b = -a, b-a
                coordinates.append((21*a % P, 21*b % P))
            first, second = (self.point(*label) for label in coordinates)
            phi = self.pair_phi(first, second, *parities)
            # This is the complete proved mu3 projection BEFORE removing epsilon².
            projected = phi+phi.rotate()*self.F.zeta+phi.rotate(2)*(self.F.zeta**2)
            assert all(not projected.c[n] for n in (0, 1, 3, 4))
            assert projected.c[2] == 3*phi.c[2] and projected.c[5] == 3*phi.c[5]
            value = phi.c[2]*self.c
            derivative = phi.c[5]*self.c*self.coarse_factor
            self.store(name, {"R771_seed_index": seed_index,
                "original_labels": [list(label) for label in labels],
                "reflected_mod41_only": bool(reflected),
                "actual_41_labels_Q_P": [list(label) for label in coordinates],
                "unchanged_mod2_labels": [list(parity) for parity in parities],
                "value_before_field_trace": value.encode(),
                "coarse_derivative_before_field_trace": derivative.encode(),
                "complete_mu3_projection_before_regularization": True,
                "two_frame_zeros_and_forbidden_epsilon_coefficients_verified": True,
                "original_coarse_coordinate": "z=a-1 at original c1=4424, a=1",
                "coarse_derivative_factor": "-81*(U/4)^2 before field trace",
                "two_torsion_extension_constructed": False})
        self.pair_cache[key] = value, derivative
        return value, derivative

    def phase(self, exponent):
        exponent %= LEVEL
        if exponent not in self.phase_cache:
            # Every such multiplication belongs to the current new weighted trace.
            if exponent % 2:
                self.phase_cache[exponent] = self.phase(exponent-1)*self.xi82
            else:
                half = self.phase(exponent//2)
                self.phase_cache[exponent] = half*half
        return self.phase_cache[exponent]

    def trace(self, value):
        def component(poly):
            return ((poly*self.modulus_derivative) % self.F.mod)[DEGREE-1]
        return self.F.elt(component(value.a), component(value.b))

    def K_coordinates(self, value):
        assert value.a.degree() <= 0 and value.b.degree() <= 0
        return [rational(value.a[0]), rational(value.b[0])]

    def m2_row(self, index):
        name = "R790-M2-CM-jet-"+str(index).zfill(4)
        recipe = self.recipes[index]
        prior = self.cached(name)
        if prior:
            assert prior["index"] == index and prior["original_recipe"] == recipe
            return file_spec(self.path(name))
        self.budget()
        seed, exponent = recipe["R771_seed_index"], recipe["j"]
        V, J = self.pair(seed, False)
        VF, JF = self.pair(seed, True)
        positive, negative = self.phase(exponent), self.phase(-exponent)
        unscaled_value = 3*self.trace(positive*V+negative*VF)
        unscaled_derivative = 3*self.trace(positive*J+negative*JF)
        value, derivative = SCALE*unscaled_value, SCALE*unscaled_derivative
        self.store(name, {"index": index, "original_recipe": recipe,
            "value_K_1_zeta": self.K_coordinates(value),
            "derivative_z_K_1_zeta": self.K_coordinates(derivative),
            "unscaled_value_K_1_zeta": self.K_coordinates(unscaled_value),
            "unscaled_derivative_z_K_1_zeta": self.K_coordinates(unscaled_derivative),
            "integer_scale": str(SCALE), "R786_power1_scale_preserved": True,
            "original_c1": 4424, "original_Y_CM_point": "P1, E6/eta12=24*sqrt(-3)",
            "K_basis": ["1", "zeta=(-1+sqrt(-3))/2"],
            "coarse_coordinate": "z=a-1; z=-epsilon^3/(81*(U/4)^2)+O(epsilon^6)",
            "primitive_xi82": "-xi41^21 from original positive Weil pairing",
            "exact_original_group_terms": 5040,
            "compression": "3*Tr_M/K(xi82^j V + xi82^-j VF); same formula for coarse derivative",
            "full_original_half_trace_equality_used": True,
            "artificial_average_or_numerical_descent_used": False,
            "M2_recipe_source_sha256": self.config["retained_artifacts"]["R775"]["files"][INPUTS["R775"]]})
        return file_spec(self.path(name))

    def finish(self):
        self.lift_torsion()
        self.normalize_eP()
        rows = [self.m2_row(index) for index in range(DIMENSION)]
        # Every completed stage is bound to the same code/proof/producers.
        entries = []
        manifest_name = "R790-stage-manifest"
        for path in sorted(self.out.glob("R790-*.json.gz")):
            if path == self.path(manifest_name):
                continue
            value = read(path)
            assert value["complete"] is True and value["configuration"] == self.tag
            entries.append(file_spec(path))
        self.store(manifest_name, {"files": entries, "M2_output_rows": rows})
        certificate = {"result": RESULT, "complete": True, "configuration": self.tag,
            "p": P, "M2_dimension": DIMENSION, "cm_jet_order": ORDER,
            "stage_manifest": file_spec(self.path(manifest_name)),
            "M2_output_rows": rows, "retained_source_files": self.input_files,
            "original_psi_values_and_first_coarse_jets_verified": True,
            "original_c1": 4424, "original_Y_CM_point": "P1",
            "original_epsilon_to_coarse_derivative_factor": "-81*(U/4)^2",
            "output_K_basis": ["1", "zeta=(-1+sqrt(-3))/2"],
            "original_M2_scale": str(SCALE), "R786_power5_product_scale": str(LEVEL**10),
            "distinct_retained_M2_seeds": len(self.seeds),
            "actual_reflected_seed_pairs": 2*len(self.seeds),
            "old_torsion_modulus_or_Weil_pairing_or_M2_basis_recomputed": False,
            "new_torsion_jets_computed_by_short_40_multiple_lift": True,
            "two_torsion_extension_constructed": False,
            "original_half_trace_not_normalized_average": True,
            "actual_y_beta_or_height_computed": False,
            "common_zero_of_later_R787_A_and_B_excluded": False,
            "formal_variable": "epsilon in (1+U/4)*v^2=r^3+epsilon*r+U/4",
            "first_coarse_jet_only_no_assumed_denominator_nonvanishing": True}
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(self.out/FINAL),
            "M2_dimension": DIMENSION, "cm_jet_order": ORDER,
            "actual_y_beta_or_height_computed": False})
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--field-core", type=Path, required=True)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        return Job(args).finish()
    except Exception as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "actual_y_beta_or_height_computed": False})
        if isinstance(error, BudgetStop):
            print(str(error), flush=True)
            return 124
        raise


if __name__ == "__main__":
    sys.exit(main())
