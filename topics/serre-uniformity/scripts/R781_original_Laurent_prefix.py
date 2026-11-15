#!/usr/bin/env python3
"""Original R781 inverse-free Laurent prefix, from the completed R774 cube.

All new exact arithmetic runs only in this public repository's GitHub Actions.
The output is the normalized local series, not an A/B map or height value.
"""
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpz_mat, fmpz_poly

RESULT = "R781-original-p41-inverse-free-Laurent-prefix"
FINAL = "p41-original-inverse-free-Laurent-prefix-certificate.json"
BOUND, H3_BOUND = 142, 143
R774_CERT = "p41-original-Hodge-cube-certificate.json"
R774_CERT_SHA = "aea27ac34e9a82203f723af27265db3cbd8d75e615247e11e0591fb2ed249b59"
R774_MANIFEST_SHA = "4d97bb53b106fa53958a943f9ae9e5d00870f7cf774d4617a727b3fa857ac222"
R774_CORE_SHA = "b7e8bf0f7b629881d973afaec01a2b905c4100573d46920841a9d48489e597fa"
R781_PROOF_SHA = "152c723da76b5c899b433db640fb6ac69082b46543f3d6bfa85d1cead7d78de0"
R778_PROOF_SHA = "b23357b3fa74773c1ee45c1740b988ee9d7c96a658d5cdec99881947faf8c727"


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    data = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(data)
    else:
        temporary.write_bytes(data)
    temporary.replace(path)


def rational_pair(value):
    return [str(value.numer()), str(value.denom())]


class Element:
    """A primitive packed integer vector times one signed rational scale."""
    __slots__ = ("poly", "scale")

    def __init__(self, poly, scale):
        scale = fmpq(scale)
        if not poly or not scale:
            self.poly, self.scale = fmpz_poly([]), fmpq(0)
            return
        content = int(poly.content())
        assert content > 0
        coefficients = [int(v)//content for v in poly.coeffs()]
        # Fix the sign too, making serialized equality canonical.
        first = next(v for v in coefficients if v)
        if first < 0:
            coefficients = [-v for v in coefficients]
            content = -content
        self.poly, self.scale = fmpz_poly(coefficients), scale*content

    @classmethod
    def retained(cls, poly, scale):
        answer = object.__new__(cls)
        answer.poly, answer.scale = poly, scale
        return answer

    def __bool__(self):
        return bool(self.scale)

    def scaled(self, scalar):
        value = self.scale*fmpq(scalar)
        if not value:
            return Element.retained(fmpz_poly([]), fmpq(0))
        return Element.retained(self.poly, value)

    def __add__(self, other):
        if not self:
            return other
        if not other:
            return self
        common = self.scale.gcd(other.scale)
        left, right = self.scale/common, other.scale/common
        assert left.denom() == 1 and right.denom() == 1
        return Element(self.poly*left.numer()+other.poly*right.numer(), common)

    def __neg__(self):
        return self.scaled(-1)

    def __sub__(self, other):
        return self+(-other)

    def __eq__(self, other):
        return self.scale == other.scale and self.poly == other.poly


class Field:
    """Original M+=Q(B,s,t), B=lambda*b, s²=-3, t=xi+xi^-1."""
    def __init__(self, original_modulus):
        nums, den = original_modulus["numerator"], int(original_modulus["denominator"])
        coeffs = [fmpq(int(v), den) for v in nums]
        assert len(coeffs) == 8 and coeffs[7] == 1
        e2, e3 = 0, 0
        for i in range(7):
            denominator = int(coeffs[i].denom())
            a, b = 0, 0
            while denominator % 2 == 0:
                a += 1
                denominator //= 2
            while denominator % 3 == 0:
                b += 1
                denominator //= 3
            assert denominator == 1
            e2 = max(e2, (a+6-i)//(7-i))
            e3 = max(e3, (b+6-i)//(7-i))
        self.lam = 2**e2*3**e3
        fb = [coeffs[i]*self.lam**(7-i) for i in range(8)]
        assert all(value.denom() == 1 for value in fb)
        self.fB = fmpz_poly([value.numer() for value in fb])
        T = fmpz_poly([0, 1])
        self.chebyshev = [fmpz_poly([2]), T]
        for _ in range(2, 21):
            self.chebyshev.append(T*self.chebyshev[-1]-self.chebyshev[-2])
        self.gt = fmpz_poly([1])
        for value in self.chebyshev[1:]:
            self.gt += value
        assert self.gt.degree() == 20 and self.gt[20] == 1
        b_powers = [fmpz_poly([1])]
        for _ in range(1, 13):
            b_powers.append((b_powers[-1]*T) % self.fB)
        t_powers = [fmpz_poly([1])]
        for _ in range(1, 39):
            t_powers.append((t_powers[-1]*T) % self.gt)
        self.Bred = fmpz_mat(14, 26)
        for j in range(2):
            for i in range(7):
                for power in range(13):
                    self.Bred[7*j+i, 13*j+power] = b_powers[power][i]
        self.Tred = fmpz_mat([[t_powers[r][k] for k in range(20)] for r in range(39)])
        self.zero = Element(fmpz_poly([]), fmpq(0))
        self.one = Element(fmpz_poly([1]), fmpq(1))
        bvector = [0]*280
        bvector[20] = 1
        self.b = self.from_vector(bvector, fmpq(1, self.lam))
        self.description = {
            "original_b_minimal_polynomial": original_modulus,
            "lambda": str(self.lam), "lambda_2_exponent": e2, "lambda_3_exponent": e3,
            "integral_B_minimal_polynomial": [str(v) for v in self.fB.coeffs()],
            "real_cyclotomic_minimal_polynomial": [str(v) for v in self.gt.coeffs()],
            "basis": "B^i*s^j*t^r, j=0..1 outer, i=0..6, r=0..19 inner; B=lambda*b",
            "packed_index": "r+39*i+507*j", "dimension_over_Q": 280,
            "original_b_replaced_by_another_twist": False}

    def from_vector(self, values, scale):
        assert len(values) == 280
        packed = [0]*761
        for j in range(2):
            for i in range(7):
                for r in range(20):
                    packed[r+39*i+507*j] = values[r+20*i+140*j]
        return Element(fmpz_poly(packed), scale)

    def vector(self, value):
        return [value.poly[r+39*i+507*j] for j in range(2) for i in range(7) for r in range(20)]

    def encode(self, value):
        return {"primitive_integer_vector": [str(v) for v in self.vector(value)],
                "rational_scale": rational_pair(value.scale)}

    def decode(self, value):
        numerator, denominator = value["rational_scale"]
        out = self.from_vector([int(v) for v in value["primitive_integer_vector"]],
                               fmpq(int(numerator), int(denominator)))
        assert self.encode(out) == value
        return out

    def multiply(self, left, right):
        if not left or not right:
            return self.zero
        product = left.poly*right.poly
        rows = []
        for j in range(2):
            for i in range(13):
                if j == 0:
                    rows.append([product[r+39*i]-3*product[r+39*i+1014] for r in range(39)])
                else:
                    rows.append([product[r+39*i+507] for r in range(39)])
        reduced = self.Bred*fmpz_mat(rows)*self.Tred
        return self.from_vector([reduced[i, r] for i in range(14) for r in range(20)],
                                left.scale*right.scale)

    def square_convolution(self, values, n):
        total = self.zero
        for i in range(1, (n+1)//2):
            total += self.multiply(values[i], values[n-i]).scaled(2)
        if n % 2 == 0 and n > 0:
            total += self.multiply(values[n//2], values[n//2])
        return total

    def convolution(self, left, right, n, start=0, stop=None):
        total = self.zero
        if stop is None:
            stop = n+1
        for i in range(start, stop):
            total += self.multiply(left[i], right[n-i])
        return total

    def metrics(self, value):
        return {"primitive_vector_max_bits": max((abs(int(v)).bit_length() for v in self.vector(value)), default=0),
                "scale_numerator_bits": abs(int(value.scale.numer())).bit_length(),
                "scale_denominator_bits": int(value.scale.denom()).bit_length()}


class BudgetStop(RuntimeError):
    pass


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.item = read(args.config)
        assert sha(args.proof) == R781_PROOF_SHA == self.item["R781_proof_sha256"]
        assert sha(args.short_proof) == R778_PROOF_SHA == self.item["R778_proof_sha256"]
        assert self.item["prefix_bound"] == BOUND and self.item["H3_prefix_bound"] == H3_BOUND
        self.directory = args.retained/"R774"
        assert sha(self.directory/"full-outputs-manifest.json") == R774_MANIFEST_SHA
        assert sha(self.directory/R774_CERT) == R774_CERT_SHA
        self.manifest = read(self.directory/"full-outputs-manifest.json")
        self.certificate = read(self.directory/R774_CERT)
        self.oldtag = self.certificate["configuration"]
        assert self.certificate["complete"] and self.oldtag["source_sha256"] == R774_CORE_SHA
        assert self.certificate["actual_cusp_ramification_e"] == 1
        assert self.certificate["selected_original_map_index"] == 4
        assert self.certificate["selected_original_map_degree"] == "1206"
        self.files = {row["file"]: row for row in self.manifest["files"]}
        self.scalars = self.retained("R774-original-L-cubic-scalars.json.gz")
        self.field = Field(self.scalars["original_b_minimal_polynomial"])
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R774_producer": self.item["retained_artifacts"]["R774"],
            "R774_manifest_sha256": R774_MANIFEST_SHA, "R774_certificate_sha256": R774_CERT_SHA,
            "R781_proof_sha256": R781_PROOF_SHA, "R778_proof_sha256": R778_PROOF_SHA,
            "selected_map_index": 4, "selected_map_degree": "1206", "actual_cusp_order": 1,
            "prefix_bound": BOUND, "H3_prefix_bound": H3_BOUND,
            "original_qY": "u=exp(2*pi*i*tau/82)",
            "real_tangent_parameter": "v=xi41^-10*u",
            "inverse_free_parameter": "v=kappa*w, kappa=[v]H^3",
            "recurrence": "(R-wR')^3=Atilde*(R^2-cstar*w^2)^2; R0=1",
            "field": self.field.description,
            "new_R775_or_R777_basis_arithmetic_executed": False}

    def retained(self, name):
        entry = self.files[name]
        path = self.directory/name
        assert sha(path) == entry["sha256"] and path.stat().st_size == entry["bytes"]
        obj = read(path)
        assert obj["complete"] and obj["configuration"] == self.oldtag
        return obj

    def path(self, name):
        return self.out/(name+".json.gz")

    def cache(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["configuration"] == self.tag and value["complete"]
        return value

    def store(self, name, value):
        save(self.path(name), dict(value, configuration=self.tag, complete=True))
        print(json.dumps({"stage": name, "seconds": time.monotonic()-self.started,
                          "complete": True}), flush=True)
        return self.path(name)

    def inputs(self):
        name = "R781-original-real-field-input"
        cached = self.cache(name)
        if cached:
            return cached, [self.field.decode(x) for x in cached["H3_coefficients_v"]]
        f = self.field
        rowscales = [fmpq(int(a), int(b))/f.lam**(i % 7)
                     for i, (a, b) in enumerate(self.scalars["rational_row_scales"])]
        denominator = 1
        for value in rowscales:
            denominator = math.lcm(denominator, int(value.denom()))
        multipliers = []
        for value in rowscales:
            scaled = value*denominator
            assert scaled.denom() == 1
            multipliers.append(scaled.numer())
        all_values = [None]*(H3_BOUND+1)
        all_values[0] = f.zero
        source_blocks = []
        phase_checks = 0
        for item in self.certificate["H3_blocks"]:
            first = int(item["file"].split("-qY-")[1].split("-")[0])
            if first > H3_BOUND:
                continue
            block = self.retained(item["file"])
            assert sha(self.directory/item["file"]) == item["sha256"]
            assert block["rational_row_scale_stage_sha256"] == sha(self.directory/"R774-original-L-cubic-scalars.json.gz")
            assert block["first_exponent"] == first
            source_blocks.append({"file": item["file"], "sha256": item["sha256"]})
            for n in range(first, min(H3_BOUND+1, block["last_exponent_exclusive"])):
                assert all_values[n] is None
                vector = []
                offset = 40*(n-first)
                for i in range(14):
                    cyclic = [0]*41
                    for r in range(40):
                        cyclic[(r+10*n) % 41] += int(block["integer_numerators"][i][offset+r])
                    # Canonical degree<40 polynomial, then exact involution.
                    reduced = [v-cyclic[40] for v in cyclic[:40]]+[0]
                    assert all(reduced[r] == reduced[41-r] for r in range(1, 21)), (n, i, "real tangent phase")
                    phase_checks += 1
                    real = fmpz_poly([reduced[0]])
                    for r in range(1, 21):
                        real += f.chebyshev[r]*reduced[r]
                    real %= f.gt
                    vector.extend([multipliers[i]*real[r] for r in range(20)])
                all_values[n] = f.from_vector(vector, fmpq(1, denominator))
        assert all(value is not None for value in all_values)
        assert all_values[1]
        data = {"source_H3_blocks": source_blocks, "H3_bound": H3_BOUND,
                "all_14_coordinate_involutions_verified_at_each_exponent": True,
                "involution_checks": phase_checks, "H3_coefficients_v": [f.encode(v) for v in all_values],
                "field": f.description, "ordinary_common_denominator_D": str(denominator),
                "original_H3_recomputed": False, "kappa_algebraic_inverse_computed": False}
        self.store(name, data)
        return self.cache(name), all_values

    def run(self):
        inputs, kappas = self.inputs()
        f, kappa = self.field, kappas[1]
        initial_name = "R781-inverse-free-Laurent-000"
        initial = self.cache(initial_name)
        if initial is None:
            k2 = f.multiply(kappa, kappa)
            k4 = f.multiply(k2, k2)
            cstar = f.multiply(f.b, k4).scaled(246**6)
            initial = {"order": 0, "input_stage_sha256": sha(self.path("R781-original-real-field-input")),
                "kappa": f.encode(kappa), "cstar": f.encode(cstar),
                "coefficients": {key: f.encode(f.one) for key in ("R", "W", "R2", "W2", "U", "U2", "Atilde", "kappa_power")},
                "normalized_constant_R0_one": True, "exact_differential_identity_at_this_order": True}
            self.store(initial_name, initial)
        else:
            assert initial["input_stage_sha256"] == sha(self.path("R781-original-real-field-input"))
        cstar = f.decode(initial["cstar"])
        values = {key: [f.one] for key in ("R", "W", "R2", "W2", "U", "U2", "Atilde", "kappa_power")}
        prior = self.path(initial_name)
        completed_paths = [prior]
        for n in range(1, BOUND+1):
            name = "R781-inverse-free-Laurent-"+str(n).zfill(3)
            old = self.cache(name)
            if old is not None:
                assert old["order"] == n and old["previous_stage_sha256"] == sha(prior)
                assert old["exact_differential_identity_at_this_order"]
                for key in values:
                    values[key].append(f.decode(old["coefficients"][key]))
                prior = self.path(name)
                completed_paths.append(prior)
                continue
            if time.monotonic()-self.started > self.args.budget_minutes*60:
                raise BudgetStop("Saved complete original Laurent coefficients through "+str(n-1))
            kp = kappa if n == 1 else f.multiply(values["kappa_power"][-1], kappa)
            a = kappas[n+1] if n == 1 else f.multiply(kappas[n+1], values["kappa_power"][n-1])
            values["Atilde"].append(a)
            # New R_n is temporarily zero; all interior terms use saved indices.
            r2_0 = f.square_convolution(values["R"], n)
            w2_0 = f.square_convolution(values["W"], n)
            u_0 = r2_0-(cstar if n == 2 else f.zero)
            u2_0 = u_0.scaled(2)+f.square_convolution(values["U"], n)
            left_0 = w2_0+f.convolution(values["W2"], values["W"], n, 1, n)
            right_0 = u2_0+f.convolution(values["Atilde"], values["U2"], n, 1, n+1)
            residual = left_0-right_0
            rn = residual.scaled(fmpq(1, 3*n+1))
            wn = rn.scaled(1-n)
            assert left_0+wn.scaled(3) == right_0+rn.scaled(4)
            current = {"R": rn, "W": wn, "R2": r2_0+rn.scaled(2),
                "W2": w2_0+wn.scaled(2), "U": u_0+rn.scaled(2),
                "U2": u2_0+rn.scaled(4), "kappa_power": kp}
            for key, value in current.items():
                values[key].append(value)
            current["Atilde"] = a
            stage = {"order": n, "previous_stage_sha256": sha(prior),
                "coefficients": {key: f.encode(value) for key, value in current.items()},
                "recurrence_divisor": 3*n+1, "exact_differential_identity_at_this_order": True,
                "R_coefficient_size": f.metrics(rn), "kappa_algebraic_inverse_computed": False,
                "ordinary_nonzero_integer_division_only": True}
            prior = self.store(name, stage)
            completed_paths.append(prior)
        inventory = self.store("R781-Laurent-stages-manifest", {
            "files": [{"file": path.name, "sha256": sha(path), "bytes": path.stat().st_size}
                      for path in [self.path("R781-original-real-field-input")]+completed_paths]})
        cert = {"result": RESULT, "configuration": self.tag, "complete": True, "p": 41,
            "original_map_index": 4, "original_map_degree": "1206", "actual_cusp_order": 1,
            "normalized_Laurent_R_bound": BOUND, "retained_H3_bound": H3_BOUND,
            "coefficient_field_dimension_over_Q": 280, "all_original_real_tangent_phases_verified": True,
            "all_recurrence_coefficients_verified_exactly": True, "algebraic_kappa_inverse_computed": False,
            "ordinary_integer_divisors": "3*n+1 for n=1..142",
            "clear_original_relation": "246^3*kappa^(n+2)*A_n+sum_(j=0)^(n+1)kappa^j*R_(n-j+1)*B_j=0 for n=-1..141",
            "required_relation_rows_over_L": 2860, "actual_relation_matrix_or_kernel_computed": False,
            "actual_y_map_or_beta_or_height_computed": False,
            "old_H3_or_R775_or_R777_computed_again": False,
            "stages_manifest": {"file": inventory.name, "sha256": sha(inventory),
                                "bytes": inventory.stat().st_size, "stage_count": len(completed_paths)+1},
            "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, cert)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(self.out/FINAL),
            "normalized_Laurent_R_bound": BOUND, "actual_y_map_or_beta_or_height_computed": False})
        return cert


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New exact arithmetic belongs to the public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--short-proof", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        job = Job(args)
        final = args.output/FINAL
        if final.exists():
            cert = read(final)
            assert cert["complete"] and cert["configuration"] == job.tag
            inventory = cert["stages_manifest"]
            assert sha(args.output/inventory["file"]) == inventory["sha256"]
            for entry in read(args.output/inventory["file"])["files"]:
                assert sha(args.output/entry["file"]) == entry["sha256"]
            save(args.output/"core-receipt.json", {"result": RESULT, "complete": True,
                "source_sha256": sha(__file__), "certificate_sha256": sha(final), "reused_complete": True})
            return
        job.run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "completed_and_partial_stages_preserved": True})
        raise


if __name__ == "__main__":
    main()
