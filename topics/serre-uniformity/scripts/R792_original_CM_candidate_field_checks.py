#!/usr/bin/env python3
"""Exact small-field necessary checks, not acceptance of original CM values.

The original y row-space zero (A.1) is not proved by this program.  Even a
successful candidate curve/conjugation check leaves original-value acceptance
false.  Completed CM responses, RR, Hom inputs and DAGs are read unchanged.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_poly

RESULT = "R792-original-CM-candidate-field-checks"
FINAL = "p41-original-CM-candidate-field-checks-certificate.json"
PREFIX = "R792-CM-candidate-"
DAG_CORE_SHA = "afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b"
FIELD_CORE_SHA = "f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251"
CM_CERT_SHA = "5de210b5ebb2a8a7fefcc8799888a68353c9c2ac10725fafa239d2bd1082d20c"
METHOD_SHA = "5ed99ddafb8ff056e2b6fd106a5333263acbf9457ee82ff854bee4896825be6a"
STRATEGY = {
    "input": "the completed 518-digit scalar-RR suggestions and original R791 h0",
    "field": "original Q(b,zeta), integral-coordinate conversion B=lambda*b, s=1+2*zeta",
    "candidate_x": "3*h0*(q^2-b)/d, only if candidate d is nonzero",
    "necessary_checks": ["c(q)=-q", "c(d)=-d", "q^2-b!=0", "d!=0", "x^3=q^2-b", "c(x)=zeta^2*x"],
    "original_value_rowspace_zero_A1_proved": False,
    "original_coordinates_accepted": False,
    "old_CM_RR_Hom_isogeny_constants_or_DAG_recomputed": False,
    "degree21_cubic_root_norm_algorithm_executed": False}


class BudgetStop(RuntimeError):
    pass


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def module(path, digest, name):
    assert sha(path) == digest
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def conjugate(value):
    return value.F.elt(value.a-value.b, -value.b)


def convert_original_integral_coordinates(L, coefficients, lam):
    """The original R792(792.12), once; no old content/denominator insertion."""
    assert len(coefficients) == 14 and all(isinstance(row, list) and len(row) == 2 for row in coefficients)
    values = [fmpq(int(row[0]), int(row[1])) for row in coefficients]
    assert all(int(row[1]) > 0 for row in coefficients)
    powers = [1]
    for _ in range(6):
        powers.append(powers[-1]*lam)
    return L.elt(fmpq_poly([(values[i]+values[i+7])*powers[i] for i in range(7)]),
                 fmpq_poly([2*values[i+7]*powers[i] for i in range(7)]))


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.started, self.out = args, time.monotonic(), Path(args.output)
        self.out.mkdir(parents=True, exist_ok=True)
        self.io = module(args.dag_core, DAG_CORE_SHA, "frozen_R792_DAG_source_classes_only")
        self.c = self.io.read(args.config)
        assert self.c["result"] == RESULT and self.c["core_sha256"] == sha(__file__)
        assert self.c["dag_core_sha256"] == DAG_CORE_SHA and self.c["field_core_sha256"] == FIELD_CORE_SHA
        for row in self.c["proofs"].values():
            path = (Path(args.topic)/row["path"]).resolve()
            assert path.is_relative_to(Path(args.topic).resolve()) and sha(path) == row["sha256"]
        assert self.c["proofs"]["acceptance"]["sha256"] == METHOD_SHA
        assert set(self.c["retained_sources"]) == {"DAG", "CM", "R791"}
        self.sources = {key: self.io.Source(key, value, args.retained) for key, value in self.c["retained_sources"].items()}
        parent = self.sources["DAG"]
        assert parent.certificate["exact_original_beta_C_as_expression_certified"] is True
        assert parent.certificate["expanded_coordinates_exactly_certified"] is False
        for key in ("CM", "R791"):
            assert parent.tag["source_identities"][key] == self.sources[key].identity
        self.tag = {"result": RESULT, "source_sha256": self.c["core_sha256"], "p": 41,
            "python_flint": flint.__version__, "dag_core_sha256": DAG_CORE_SHA, "field_core_sha256": FIELD_CORE_SHA,
            "proofs": self.c["proofs"], "source_identities": {key: source.identity for key, source in self.sources.items()},
            "strategy": STRATEGY, "budget_excluded_from_mathematical_identity": True}
        self.field_module = module(args.field_core, FIELD_CORE_SHA, "original_R754_small_field")
        cm = self.sources["CM"]
        cf = cm.certificate
        assert cm.item["certificate"]["sha256"] == CM_CERT_SHA
        assert cf["source_Dixon_digits"] == 518 and cf["all_14_branches_units"] is True
        assert cf["exact_finite_y_implicit_expression_defined"] is True
        assert cf["expanded_coordinates_exactly_certified"] is False
        self.expression = cm.stage(cf["implicit_expression"])
        self.candidate = cm.stage(cf["coordinate_candidates"])
        self.field = self.expression["original_field"]
        assert self.candidate["candidate_only"] is True and self.candidate["expanded_coordinates_exactly_certified"] is False
        assert self.candidate["exact_bordered_determinant_or_rowspace_zero_certificate_obtained"] is False
        assert self.candidate["may_be_consumed_by_old_R792_success_path"] is False
        for key in ("value_y0", "derivative_z_y0"):
            assert self.candidate["candidates"][key]["all14_reconstructed"] is True
        h = self.sources["R791"]
        self.tangent = h.stage(h.files[self.io.TANGENTS])
        assert self.tangent["original_map_index"] == 4 and self.tangent["original_c1_slash_count"] == 1
        assert self.tangent["zero_flags"][4] is False and h.certificate["original_index4_c1_tangent_nonzero"] is True
        self.L = self.field_module.QKField(self.field_module.dp(self.field["original_b_minimal_polynomial"]))
        assert self.L.degree == 7

    def path(self, name):
        return self.out/(PREFIX+name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        answer = self.io.read(path)
        assert answer["complete"] is True and answer["configuration"] == self.tag
        return answer

    def store(self, name, value):
        if time.monotonic()-self.started > self.args.budget_minutes*60:
            raise BudgetStop("all completed small-field stages retained")
        value = {"complete": True, "configuration": self.tag, **value}
        self.io.save(self.path(name), value)
        return value

    def inputs(self):
        old = self.cached("exact-original-field-inputs")
        if old:
            return old
        lam = int(self.field["lambda"])
        q = convert_original_integral_coordinates(self.L, self.candidate["candidates"]["value_y0"]["coordinates"], lam)
        d = convert_original_integral_coordinates(self.L, self.candidate["candidates"]["derivative_z_y0"]["coordinates"], lam)
        h0 = self.L.decode(self.tangent["actual_L_coefficients_h_i_over_ds_at_c1"][4])
        assert h0
        return self.store("exact-original-field-inputs", {
            "candidate_q": q.encode(), "candidate_d": d.encode(), "original_h0": h0.encode(),
            "original_field": self.field, "source_candidate": self.sources["CM"].ref(self.sources["CM"].certificate["coordinate_candidates"]["file"]),
            "source_tangent": self.sources["R791"].ref(self.io.TANGENTS),
            "coordinate_conversion": "R792(792.12) once; s=1+2*zeta; B=lambda*b",
            "exact_q_d_arithmetic_encodings_not_original_value_acceptance": True,
            "old_RR_or_h0_recomputed": False})

    def checks(self, inputs):
        old = self.cached("necessary-exact-identities")
        if old:
            return old
        q, d, h = (self.L.decode(inputs[key]) for key in ("candidate_q", "candidate_d", "original_h0"))
        b, zeta = self.L.gen, self.L.zeta
        w = q*q-b
        q_conjugacy = conjugate(q)+q
        d_conjugacy = conjugate(d)+d
        flags = {"candidate_q_anti_real": not bool(q_conjugacy), "candidate_d_anti_real": not bool(d_conjugacy),
                 "candidate_w_nonzero": bool(w), "candidate_d_nonzero": bool(d)}
        residuals = {"conjugate_q_plus_q": q_conjugacy.encode(), "conjugate_d_plus_d": d_conjugacy.encode()}
        x = None
        if d:
            x = (3*h*w)/d
            cubic = x*x*x-w
            direction = conjugate(x)-(zeta*zeta)*x
            derivative = d-3*h*x*x
            flags.update(candidate_x_cubic_identity=not bool(cubic), candidate_x_original_conjugation=not bool(direction),
                         candidate_d_differential_identity=not bool(derivative))
            residuals.update(x_cubed_minus_w=cubic.encode(), conjugate_x_minus_zeta2_x=direction.encode(),
                             d_minus_three_h_x_squared=derivative.encode())
        else:
            flags.update(candidate_x_cubic_identity=False, candidate_x_original_conjugation=False,
                         candidate_d_differential_identity=False)
        all_pass = all(flags.values())
        return self.store("necessary-exact-identities", {"flags": flags, "residuals_in_original_b_zeta_basis": residuals,
            "candidate_x": x.encode() if x is not None else None, "candidate_w": w.encode(),
            "all_necessary_field_checks_passed": all_pass,
            "original_value_rowspace_zero_A1_proved": False,
            "original_coordinates_accepted": False,
            "conditional_consequence": "IF exact original A0-q*B0=0 is separately certified, then passed field identities identify x and d",
            "finite_precision_curve_or_conjugacy_used_as_exact_original_value_proof": False})

    def finish(self, checks):
        rows = [self.io.spec(path) for path in sorted(self.out.glob(PREFIX+"*.json.gz"))
                if not path.name.startswith(PREFIX+"stage-manifest-")]
        name = "stage-manifest-"+self.io.fingerprint(rows)[:24]
        self.io.save(self.path(name), {"complete": True, "configuration": self.tag, "files": rows})
        final = {"result": RESULT, "complete": True, "configuration": self.tag, "p": 41,
            "source_Dixon_digits": 518, "source_original_point_DAG": self.sources["DAG"].identity,
            "exact_candidate_inputs": self.io.spec(self.path("exact-original-field-inputs")),
            "necessary_field_checks": self.io.spec(self.path("necessary-exact-identities")),
            "all_necessary_field_checks_passed": checks["all_necessary_field_checks_passed"], "flags": checks["flags"],
            "original_value_rowspace_zero_A1_proved": False, "original_coordinates_accepted": False,
            "expanded_original_coordinates_exactly_certified": False,
            "old_R792_success_recipe_produced": False, "actual_eta_or_height_computed": False,
            "old_CM_RR_Hom_or_isogeny_constants_recomputed": False,
            "degree21_cubic_root_norm_algorithm_executed": False, "stage_manifest": self.io.spec(self.path(name)),
            "seconds": time.monotonic()-self.started}
        self.io.save(self.out/FINAL, final)
        print("CANDIDATE_FIELD_RESULT="+json.dumps({key: final[key] for key in ("complete", "flags", "all_necessary_field_checks_passed",
            "original_value_rowspace_zero_A1_proved", "original_coordinates_accepted", "seconds")}), flush=True)
        return final

    def run(self):
        if (self.out/FINAL).exists():
            value = self.io.read(self.out/FINAL)
            assert value["complete"] is True and value["configuration"] == self.tag
            return value
        return self.finish(self.checks(self.inputs()))


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New field arithmetic belongs to public repository Actions.")
    parser = argparse.ArgumentParser()
    for key in ("config", "topic", "dag-core", "field-core", "retained", "output"):
        parser.add_argument("--"+key, required=True)
    parser.add_argument("--budget-minutes", type=float, default=30)
    args = parser.parse_args()
    io = module(args.dag_core, DAG_CORE_SHA, "frozen_DAG_IO")
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    started, final, error, code = time.monotonic(), None, None, 0
    try:
        final = Job(args).run()
    except BudgetStop as exc:
        error, code = "BudgetStop: "+str(exc), 124
    except Exception as exc:
        import traceback
        traceback.print_exc()
        error, code = type(exc).__name__+": "+str(exc), 1
    receipt = {"result": RESULT, "source_sha256": sha(__file__), "complete": final is not None,
        "error": error, "seconds": time.monotonic()-started,
        "certificate_sha256": sha(output/FINAL) if final is not None else None,
        "original_coordinates_accepted": False, "all_completed_stages_preserved": True}
    io.save(output/"core-receipt.json", receipt)
    print("CORE_RECEIPT="+json.dumps(receipt), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
