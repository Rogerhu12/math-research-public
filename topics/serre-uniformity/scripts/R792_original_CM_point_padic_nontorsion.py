#!/usr/bin/env python3
"""Source-bound finite p-adic non-torsion witness; public Actions only.

The inputs are actual modular CM responses, not rational-reconstruction
suggestions. All affine operations carry an absolute precision. An uncertain
zero is never interpreted as an exact group-law branch.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

sys.set_int_max_str_digits(0)
RESULT = "R792-original-CM-point-padic-nontorsion"
FINAL = "p41-original-CM-point-padic-nontorsion-certificate.json"
PREFIX = "R792-CM-nontorsion-"
DAG_CORE_SHA = "afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b"
METHOD_SHA = "b3b88cc94fc3d716bd39227794f3ec780265cd22bdb3082305070e007da0e0a7"
CM_CERT_SHA = "5de210b5ebb2a8a7fefcc8799888a68353c9c2ac10725fafa239d2bd1082d20c"
P = 1000000753
N = 518
STRATEGY = {
    "input": "completed original 518-digit modular CM quotients and R791 h0, never RR suggestions",
    "branch": "first original branch with simple roots and unit lambda,b,derivative,and h0 denominators",
    "prime": P,
    "absolute_source_precision": N,
    "point_x": "3*h0*(y^2-b)/yprime, original R791(791R.16)",
    "finite_annihilator": "deterministic Hasse interval baby-step giant-step, then exact Fp scalar verification",
    "local_arithmetic": "Qell affine balls with absolute precision and known-nonzero inverses only",
    "uncertain_zero": "stop the finite sufficient test; no exact O or doubling inference",
    "success": "verified annihilator and finite positive valuation of t=-x/y",
    "formal_group": "good reduction over Qell; ell>2; torsion-free even when ell divides m",
    "old_CM_Dixon_RR_Hom_or_DAG_arithmetic_recomputed": False,
    "expanded_original_coordinates_exactly_certified": False}


class BudgetStop(RuntimeError):
    pass


class UndeterminedZero(RuntimeError):
    def __init__(self, reason, value=None):
        super().__init__(reason)
        self.reason, self.value = reason, value


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path, digest, name):
    assert sha(path) == digest
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def polynomial(coefficients, value, modulus):
    answer = 0
    for coefficient in reversed(coefficients):
        answer = (answer*value+int(coefficient)) % modulus
    return answer


def derivative(coefficients):
    return [i*int(coefficients[i]) for i in range(1, len(coefficients))]


def valuation(integer, prime=P):
    assert integer != 0
    answer = 0
    integer = abs(integer)
    while integer % prime == 0:
        integer //= prime
        answer += 1
    return answer


class Ball:
    """p**v * unit + O(p**A), or an uncertified-zero ball O(p**A)."""
    __slots__ = ("u", "v", "A")

    def __init__(self, unit, value, precision):
        self.A = int(precision)
        value = int(value)
        if value >= self.A:
            self.u, self.v = 0, self.A
            return
        unit = int(unit) % pow(P, self.A-value)
        if not unit:
            self.u, self.v = 0, self.A
            return
        while unit % P == 0:
            unit //= P
            value += 1
        self.u, self.v = unit, value

    @classmethod
    def integer(cls, value, precision):
        return cls(value, 0, precision)

    def encode(self):
        return {"unit": str(self.u), "valuation_or_lower_bound": self.v,
                "absolute_precision": self.A, "known_nonzero": bool(self.u)}

    @classmethod
    def decode(cls, row):
        answer = cls(int(row["unit"]), row["valuation_or_lower_bound"], row["absolute_precision"])
        assert answer.encode() == row
        return answer

    def __neg__(self):
        return Ball(-self.u, self.v, self.A)

    def __add__(self, other):
        if isinstance(other, int):
            other = Ball.integer(other, self.A)
        precision = min(self.A, other.A)
        value = min(self.v, other.v, precision)
        if value == precision:
            return Ball(0, precision, precision)
        left = self.u*pow(P, self.v-value) if self.v < precision else 0
        right = other.u*pow(P, other.v-value) if other.v < precision else 0
        return Ball(left+right, value, precision)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, int):
            if not other:
                return Ball(0, self.A, self.A)
            shift = valuation(other)
            return Ball(self.u*(other//pow(P, shift)), self.v+shift, self.A+shift)
        precision = min(self.A+other.v, other.A+self.v)
        return Ball(self.u*other.u, self.v+other.v, precision)

    __rmul__ = __mul__

    def inverse(self):
        if not self.u:
            raise UndeterminedZero("inverse denominator is only a zero ball", self.encode())
        exponent = self.A-self.v
        return Ball(pow(self.u, -1, pow(P, exponent)), -self.v, self.A-2*self.v)

    def __truediv__(self, other):
        return self*other.inverse()

    def reduction(self):
        if self.A < 1 or self.v < 0:
            raise UndeterminedZero("integral residue not determined at this precision", self.encode())
        return self.u % P if self.v == 0 else 0


def ff_neg(point):
    return None if point is None else (point[0], (-point[1]) % P)


def ff_add(left, right):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u:
        if (y+v) % P == 0:
            return None
        assert y == v
        slope = 3*x*x*pow(2*y, -1, P) % P
    else:
        slope = (v-y)*pow(u-x, -1, P) % P
    xx = (slope*slope-x-u) % P
    return xx, (slope*(x-xx)-y) % P


def ff_multiply(integer, point):
    if integer < 0:
        return ff_multiply(-integer, ff_neg(point))
    answer, current = None, point
    while integer:
        if integer & 1:
            answer = ff_add(answer, current)
        integer >>= 1
        if integer:
            current = ff_add(current, current)
    return answer


def encoded_point(point):
    return None if point is None else list(point)


def original_integral_evaluation(values, B, s, modulus):
    assert len(values) == 14
    return (polynomial(values[:7], B, modulus)+s*polynomial(values[7:], B, modulus)) % modulus


def tangent_evaluation(enc, b, zeta, modulus):
    assert len(enc) == 2
    values = []
    for row in enc:
        denominator = int(row["denominator"])
        assert denominator % P
        values.append(polynomial(row["numerator"], b, modulus)*pow(denominator, -1, modulus) % modulus)
    return (values[0]+zeta*values[1]) % modulus


class Job:
    def __init__(self, args):
        self.args, self.started, self.out = args, time.monotonic(), Path(args.output)
        self.out.mkdir(parents=True, exist_ok=True)
        self.io = load(args.dag_core, DAG_CORE_SHA, "frozen_DAG_source_IO")
        self.c = self.io.read(args.config)
        assert self.c["result"] == RESULT and self.c["core_sha256"] == sha(__file__)
        assert self.c["dag_core_sha256"] == DAG_CORE_SHA
        for row in self.c["proofs"].values():
            path = (Path(args.topic)/row["path"]).resolve()
            assert path.is_relative_to(Path(args.topic).resolve()) and sha(path) == row["sha256"]
        assert self.c["proofs"]["nontorsion"]["sha256"] == METHOD_SHA
        assert set(self.c["retained_sources"]) == {"DAG", "CM", "R791"}
        self.sources = {key: self.io.Source(key, row, args.retained) for key, row in self.c["retained_sources"].items()}
        parent, cm, hom = (self.sources[k] for k in ("DAG", "CM", "R791"))
        assert parent.certificate["exact_original_beta_C_as_expression_certified"] is True
        assert parent.certificate["expanded_coordinates_exactly_certified"] is False
        for key in ("CM", "R791"):
            assert parent.tag["source_identities"][key] == self.sources[key].identity
        assert cm.item["certificate"]["sha256"] == CM_CERT_SHA
        assert cm.certificate["source_Dixon_digits"] == N and cm.certificate["all_14_branches_units"] is True
        self.quotient = cm.stage(cm.certificate["modular_value"])
        self.witness = cm.stage(cm.certificate["denominator_unit_witness"])
        self.expression = cm.stage(cm.certificate["implicit_expression"])
        assert self.quotient["all14_original_quotient_identities_verified"] is True
        assert self.quotient["prime"] == self.witness["prime"] == P
        assert self.quotient["digits"] == N and int(self.quotient["modulus"]) == pow(P, N)
        self.field = self.expression["original_field"]
        assert self.quotient["original_field"] == self.field
        self.fB = [int(x) for x in self.field["integral_B_minimal_polynomial"]]
        assert len(self.fB) == 8 and self.fB[-1] == 1
        self.dfB = derivative(self.fB)
        self.lam = int(self.field["lambda"])
        self.roots = self.witness["roots_B_s"]
        assert len(self.roots) == 14
        self.y_values = [int(x) for x in self.quotient["value_y0"]]
        self.dy_values = [int(x) for x in self.quotient["derivative_z_y0"]]
        tangents = hom.stage(hom.files[self.io.TANGENTS])
        assert tangents["original_map_index"] == 4 and tangents["original_c1_slash_count"] == 1
        assert tangents["zero_flags"][4] is False
        self.h0 = tangents["actual_L_coefficients_h_i_over_ds_at_c1"][4]
        self.tag = {"result": RESULT, "source_sha256": self.c["core_sha256"], "p": 41,
            "dag_core_sha256": DAG_CORE_SHA, "proofs": self.c["proofs"],
            "source_identities": {k: value.identity for k, value in self.sources.items()},
            "strategy": STRATEGY, "budget_excluded_from_mathematical_identity": True}

    def path(self, name):
        return self.out/(PREFIX+name+".json.gz")

    def spec(self, name):
        return self.io.spec(self.path(name))

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = self.io.read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def check_budget(self):
        if time.monotonic()-self.started > self.args.budget_minutes*60:
            raise BudgetStop("completed root, reduction, and affine stages retained")

    def store(self, name, value):
        value = {"complete": True, "configuration": self.tag, **value}
        self.io.save(self.path(name), value)
        return value

    def choose_branch(self):
        old = self.cached("original-branch-selection")
        if old:
            return old
        self.check_budget()
        rows, selected = [], None
        common_units = self.lam % P != 0 and all(int(r["denominator"]) % P != 0 for r in self.h0)
        for index, root in enumerate(self.roots):
            B, s = map(int, root)
            assert polynomial(self.fB, B, P) == 0 and (s*s+3) % P == 0
            simple = polynomial(self.dfB, B, P) != 0 and (2*s) % P != 0
            row = {"branch_index": index, "original_roots_B_s": [B, s], "simple": simple,
                   "lambda_and_h0_denominators_units": common_units}
            if common_units and simple:
                b = B*pow(self.lam, -1, P) % P
                dy = original_integral_evaluation(self.dy_values, B, s, P)
                row.update(b_mod_prime=b, derivative_mod_prime=dy, b_unit=b != 0, derivative_unit=dy != 0)
                if b and dy:
                    selected = index
                    rows.append(row)
                    break
            rows.append(row)
        return self.store("original-branch-selection", {"selected_branch": selected, "reviewed_original_branches": rows,
            "source_original_roots": self.sources["CM"].ref(self.sources["CM"].certificate["denominator_unit_witness"]["file"]),
            "source_modular_quotient": self.sources["CM"].ref(self.sources["CM"].certificate["modular_value"]["file"]),
            "source_tangent": self.sources["R791"].ref(self.io.TANGENTS),
            "rational_reconstruction_candidates_used": False})

    def lift_roots(self, selected):
        B, s = map(int, self.roots[selected])
        digits, previous = 1, None
        while True:
            name = f"branch-{selected:02d}-roots-{digits:04d}"
            old = self.cached(name)
            if old:
                assert old["digits"] == digits and old["branch_index"] == selected
                assert old["previous"] == previous
                B, s = int(old["B"]), int(old["s"])
            else:
                self.check_budget()
                modulus = pow(P, digits)
                assert polynomial(self.fB, B, modulus) == 0 and (s*s+3) % modulus == 0
                self.store(name, {"branch_index": selected, "digits": digits, "B": str(B), "s": str(s),
                    "previous": previous, "unique_lift_of_original_simple_roots": True})
            previous = self.spec(name)
            if digits == N:
                return old if old else self.io.read(self.path(name)), previous
            stop = min(2*digits, N)
            next_name = f"branch-{selected:02d}-roots-{stop:04d}"
            if not self.path(next_name).exists():
                self.check_budget()
                modulus = pow(P, stop)
                B = (B-polynomial(self.fB, B, modulus)*pow(polynomial(self.dfB, B, modulus), -1, modulus)) % modulus
                s = (s-(s*s+3)*pow(2*s, -1, modulus)) % modulus
            digits = stop

    def source_point(self, selected):
        old = self.cached("original-point-balls")
        if old:
            return old
        roots, root_spec = self.lift_roots(selected)
        self.check_budget()
        modulus = pow(P, N)
        B, s = int(roots["B"]), int(roots["s"])
        b = B*pow(self.lam, -1, modulus) % modulus
        zeta = (s-1)*pow(2, -1, modulus) % modulus
        y = Ball.integer(original_integral_evaluation(self.y_values, B, s, modulus), N)
        dy = Ball.integer(original_integral_evaluation(self.dy_values, B, s, modulus), N)
        h = Ball.integer(tangent_evaluation(self.h0, b, zeta, modulus), N)
        bb = Ball.integer(b, N)
        assert dy.u and dy.v == 0 and bb.v == 0
        xx = 3*h*(y*y-bb)/dy
        residual = y*y-xx*xx*xx-bb
        assert residual.u == 0, "The source-bound original point failed its modular curve identity"
        point = (xx.reduction(), y.reduction())
        assert (point[1]*point[1]-point[0]**3-b % P) % P == 0
        return self.store("original-point-balls", {"branch_index": selected, "roots": root_spec,
            "x": xx.encode(), "y": y.encode(), "b": bb.encode(), "h0": h.encode(), "yprime": dy.encode(),
            "point_mod_prime": list(point), "b_mod_prime": b % P,
            "curve_residual_contains_zero": True, "curve_residual_absolute_precision": residual.A,
            "point_is_the_source_bound_original_f4_c1": True,
            "expanded_original_coordinates_exactly_certified": False,
            "rational_reconstruction_candidates_used": False})

    def annihilator(self, point):
        old = self.cached("finite-reduction-annihilator")
        if old:
            return old
        self.check_budget()
        base = tuple(point["point_mod_prime"])
        radius = math.isqrt(4*P)
        lower, upper = P+1-radius, P+1+radius
        width = upper-lower+1
        k = math.isqrt(width)
        if k*k < width:
            k += 1
        babies, current = {}, None
        for j in range(k):
            babies.setdefault(current, j)
            current = ff_add(current, base)
        giant = ff_neg(ff_multiply(lower, base))
        stride = ff_neg(ff_multiply(k, base))
        found = None
        for i in range(k):
            if giant in babies:
                j = babies[giant]
                m = lower+i*k+j
                if m <= upper:
                    found = (m, i, j)
                    break
            giant = ff_add(giant, stride)
        assert found is not None, "Hasse interval baby-step giant-step failed"
        m, i, j = found
        assert m > 0 and ff_multiply(m, base) is None
        table = [{"point": encoded_point(p), "first_index": j} for p, j in babies.items()]
        return self.store("finite-reduction-annihilator", {"original_point": self.spec("original-point-balls"),
            "point_mod_prime": list(base), "b_mod_prime": point["b_mod_prime"],
            "hasse_lower": lower, "hasse_upper": upper, "step_size": k,
            "integer_m": m, "matched_giant_index": i, "matched_baby_index": j,
            "actual_baby_table": table, "m_times_original_reduction_is_O": True,
            "m_claimed_to_be_exact_point_order_or_curve_order": False,
            "prime_to_ell_m_required": False})

    def scalar_multiply(self, point, finite):
        x0, y0, b = (Ball.decode(point[k]) for k in ("x", "y", "b"))
        m = finite["integer_m"]
        operations, multiple = [], 1
        for bit in bin(m)[3:]:
            operations.append(("double", multiple, multiple, 2*multiple))
            multiple *= 2
            if bit == "1":
                operations.append(("add_base", multiple, 1, multiple+1))
                multiple += 1
        assert multiple == m
        x, y, previous = x0, y0, self.spec("original-point-balls")
        for step, (operation, left, right, target) in enumerate(operations):
            name = f"scalar-step-{step:03d}"
            old = self.cached(name)
            if old:
                assert old["operation"] == operation and old["input_multiples"] == [left, right]
                assert old["output_multiple"] == target and old["previous"] == previous
                assert old["integer_m"] == m
                x, y = Ball.decode(old["x"]), Ball.decode(old["y"])
                previous = self.spec(name)
                continue
            self.check_budget()
            denominator = 2*y if operation == "double" else x0-x
            if not denominator.u:
                reason = "required affine denominator is only a zero ball"
                return self.store("finite-witness", {"status": "indeterminate", "reason": reason,
                    "step": step, "operation": operation, "input_multiples": [left, right],
                    "denominator": denominator.encode(), "previous": previous,
                    "integer_m": m, "actual_original_point_nontorsion_certified": False})
            if operation == "double":
                slope = (3*x*x)/denominator
                xx = slope*slope-2*x
            else:
                assert left != right, "known equal multiples must use doubling"
                slope = (y0-y)/denominator
                xx = slope*slope-x-x0
            yy = slope*(x-xx)-y
            residual = yy*yy-xx*xx*xx-b
            assert residual.u == 0, "Affine arithmetic lost the exact original curve identity"
            data = {"operation": operation, "input_multiples": [left, right], "output_multiple": target,
                "integer_m": m, "previous": previous, "original_point": self.spec("original-point-balls"),
                "denominator": denominator.encode(), "denominator_known_nonzero": True,
                "x": xx.encode(), "y": yy.encode(), "curve_residual_contains_zero": True,
                "curve_residual_absolute_precision": residual.A,
                "nonprimitive_projective_coordinates_used": False}
            self.store(name, data)
            x, y, previous = xx, yy, self.spec(name)
        if not y.u:
            return self.store("finite-witness", {"status": "indeterminate", "reason": "final y denominator is a zero ball",
                "previous": previous, "integer_m": m, "y": y.encode(),
                "actual_original_point_nontorsion_certified": False})
        t = (-x)/y
        success = bool(t.u) and 1 <= t.v < t.A
        if success:
            assert x.u and y.u and x.v == -2*t.v and y.v == -3*t.v
        else:
            assert not t.u or t.A <= 0 or t.v >= 1, "Finite reduction and local arithmetic disagree"
        return self.store("finite-witness", {"status": "certified" if success else "indeterminate",
            "reason": "finite positive t valuation" if success else "available precision does not certify nonzero formal parameter",
            "integer_m": m, "last_scalar_step": previous,
            "finite_annihilator": self.spec("finite-reduction-annihilator"),
            "x": x.encode(), "y": y.encode(), "formal_parameter_t": t.encode(),
            "actual_original_point_nontorsion_certified": success,
            "m_prime_to_ell_assumed": False, "formal_group_torsion_freeness_applied": success,
            "expanded_original_coordinates_exactly_certified": False})

    def finish(self, witness):
        rows = [self.io.spec(path) for path in sorted(self.out.glob(PREFIX+"*.json.gz"))
                if not path.name.startswith(PREFIX+"stage-manifest-")]
        manifest_name = "stage-manifest-"+self.io.fingerprint(rows)[:24]
        self.io.save(self.path(manifest_name), {"complete": True, "configuration": self.tag, "files": rows})
        success = witness["actual_original_point_nontorsion_certified"]
        cert = {"result": RESULT, "complete": True, "configuration": self.tag, "p": 41,
            "source_Dixon_digits": N, "local_prime": P,
            "original_map_index": 4, "original_map_degree": 1206,
            "source_original_point_DAG": self.sources["DAG"].identity,
            "branch_selection": self.spec("original-branch-selection"),
            "original_point_balls": self.spec("original-point-balls") if self.path("original-point-balls").exists() else None,
            "finite_annihilator": self.spec("finite-reduction-annihilator") if self.path("finite-reduction-annihilator").exists() else None,
            "finite_witness": self.spec("finite-witness"),
            "actual_original_beta_C_nontorsion_certified": success,
            "original_primitive_Q_beta_nontorsion_consequence": success,
            "all_nonzero_original_L_Hom_values_nontorsion_consequence": success,
            "original_value_rowspace_zero_A1_proved": False,
            "expanded_original_coordinates_exactly_certified": False,
            "rational_reconstruction_candidates_used": False,
            "old_CM_Dixon_RR_Hom_or_DAG_arithmetic_recomputed": False,
            "actual_eta_or_height_computed": False,
            "stage_manifest": self.spec(manifest_name), "seconds": time.monotonic()-self.started}
        self.io.save(self.out/FINAL, cert)
        print("PADIC_NONTORSION_RESULT="+json.dumps({k: cert[k] for k in
            ("complete", "actual_original_beta_C_nontorsion_certified", "original_primitive_Q_beta_nontorsion_consequence",
             "all_nonzero_original_L_Hom_values_nontorsion_consequence", "expanded_original_coordinates_exactly_certified", "seconds")}), flush=True)
        return cert

    def run(self):
        if (self.out/FINAL).exists():
            cert = self.io.read(self.out/FINAL)
            assert cert["complete"] is True and cert["configuration"] == self.tag
            return cert
        old = self.cached("finite-witness")
        if old:
            return self.finish(old)
        choice = self.choose_branch()
        if choice["selected_branch"] is None:
            witness = self.store("finite-witness", {"status": "indeterminate", "reason": "no eligible original unit branch",
                "branch_selection": self.spec("original-branch-selection"),
                "actual_original_point_nontorsion_certified": False})
        else:
            point = self.source_point(choice["selected_branch"])
            finite = self.annihilator(point)
            witness = self.scalar_multiply(point, finite)
        return self.finish(witness)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New local arithmetic belongs to public repository Actions.")
    parser = argparse.ArgumentParser()
    for key in ("config", "topic", "dag-core", "retained", "output"):
        parser.add_argument("--"+key, required=True)
    parser.add_argument("--budget-minutes", type=float, default=30)
    args = parser.parse_args()
    io = load(args.dag_core, DAG_CORE_SHA, "frozen_DAG_source_receipts")
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    started, cert, code, error = time.monotonic(), None, 0, None
    try:
        cert = Job(args).run()
    except BudgetStop as exc:
        error, code = "BudgetStop: "+str(exc), 124
    except Exception as exc:
        import traceback
        traceback.print_exc()
        error, code = type(exc).__name__+": "+str(exc), 1
    receipt = {"result": RESULT, "source_sha256": sha(__file__), "complete": cert is not None,
        "error": error, "seconds": time.monotonic()-started,
        "certificate_sha256": sha(output/FINAL) if cert is not None else None,
        "expanded_original_coordinates_exactly_certified": False, "all_completed_stages_preserved": True}
    io.save(output/"core-receipt.json", receipt)
    print("CORE_RECEIPT="+json.dumps(receipt), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
