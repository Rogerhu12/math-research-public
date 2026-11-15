#!/usr/bin/env python3
"""One explicit rational outer point; no old LP, RREF or path integration.

The public actual entry verifies only the proposed change y_12 = -1/2 in the
published static/parity point.  It preserves all 68 archived inequalities,
checks every stored static degree, reads the complete fourteen scalar families,
and checks applicability of the published static and derivative certificates.

A complete degree-at-most-three half-line sign oracle is included as a reusable
exact-arithmetic utility.  Only invented examples call it in this release.
The actual point has a prescribed SOS, so no root isolation or cut loop is run.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as F
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_character_minus2_static_cut as archived

base = archived.base
SCHEMA = "visible-flex-character-minus2-explicit-static-positive-candidate-v1"
REPOSITORY = archived.REPOSITORY
CURRENT_SCHEMA = "visible-flex-character-minus2-static-and-quadratic-parity-cuts-v1"
CURRENT = {
    "run": "43668125602",
    "commit": "c8a89721ee361074096b202af6aa0841ac1bc445",
    "lane": "character_minus2_static_parity",
    "report": {"filename": "character-minus2-static-parity.json", "bytes": 6971,
        "sha256": "bb2e66e4ddd6e0e826c8aa78cef96462e23290852f512b84ab0d3fceb800f968"},
    "publication": {"filename": "receipt.json", "bytes": 40112,
        "sha256": "947bbcd35c08476233568a67c8f6b4c322bf8991284b8c9382fc65fea2ccd6d2"},
    "certificate": {"filename": "character-minus2-static-parity-certificate.json.gz",
        "stored_bytes": 9222,
        "stored_sha256": "2431172cb890ad9d6bc7fa227793fabd9a33e5f254531ff2411b6fbc6870e3af",
        "raw_bytes": 34807,
        "raw_sha256": "f15004c94a2400bf9fed2e9705227ba2cd1ca2dacc38080a25bf703e9f27ef23"},
    "driver": {"filename": "literature_character_minus2_static_and_parity_cuts.py",
        "bytes": 18508,
        "sha256": "9e7f7d2b9b70b78a3eec17f8c4c2e4cd64caf8d6304247355aaff55c962f41e1"},
}
ARCHIVED_HELPER = {"filename": "literature_character_minus2_static_cut.py", "bytes": 26313,
    "sha256": "d5a65482df040627b1a9a13fb8fce3e813f90e8ec196714cb9cf1bd78e97da5d"}
CHANGED_FREE_INDEX = 12
CHANGED_NORMAL_INDEX = 73
CHANGED_VALUE = F(-1, 2)
ALLOWED_STATIC_DEGREES = (0, 2, 4, 6)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    path = Path(path); raw = path.read_bytes()
    return {"filename": path.name, "bytes": len(raw), "sha256": sha(raw)}


def source_identity():
    if identity(archived.__file__) != ARCHIVED_HELPER:
        raise ValueError("frozen archived-row helper changed")
    current_path = Path(__file__).resolve().parent / CURRENT["driver"]["filename"]
    if identity(current_path) != CURRENT["driver"]:
        raise ValueError("published static/parity producer source changed")
    return {"driver": identity(__file__), "archived_row_helper": ARCHIVED_HELPER,
        "archived_exact_engine": archived.source_identity()["archived_exact_finite_system_engine"],
        "published_input_producer": CURRENT["driver"],
        "head_or_original_function_helpers_imported": False}


def read_small(path, expected):
    raw = Path(path).read_bytes()
    if len(raw) != expected["bytes"] or sha(raw) != expected["sha256"]:
        raise ValueError("published small input byte/SHA mismatch")
    return json.loads(raw), raw


def read_gzip(path, expected, budget):
    packed = Path(path).read_bytes()
    if len(packed) != expected["stored_bytes"] or sha(packed) != expected["stored_sha256"]:
        raise ValueError("published certificate packed identity mismatch")
    raw = gzip.decompress(packed)
    if len(raw) != expected["raw_bytes"] or sha(raw) != expected["raw_sha256"]:
        raise ValueError("published certificate raw identity mismatch")
    budget.check()
    return json.loads(raw)


def check_current_publication(publication, main, main_raw):
    if (publication.get("schema") != "visible-new-mechanism-actions-v1"
        or publication.get("repository") != REPOSITORY
        or str(publication.get("run_id")) != CURRENT["run"]
        or publication.get("source_commit") != CURRENT["commit"]
        or publication.get("lane") != CURRENT["lane"]):
        raise ValueError("current publication identity changed")
    if (main.get("schema") != CURRENT_SCHEMA or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != CURRENT["run"]
        or main.get("github_sha") != CURRENT["commit"]
        or main.get("source_hashes", {}).get("driver") != CURRENT["driver"]
        or main.get("target_weight") != -2):
        raise ValueError("complete exact current producer main required")
    rows = publication.get("outputs", [])
    outputs = {Path(row["path"]).name: row for row in rows}
    if len(outputs) != len(rows):
        raise ValueError("ambiguous current output basenames")
    rec = outputs.get(CURRENT["report"]["filename"], {})
    if rec.get("bytes") != len(main_raw) or rec.get("sha256") != sha(main_raw):
        raise ValueError("publication does not bind the current main")
    metadata = main.get("complete_necessary_certificate", {})
    if any(metadata.get(k) != v for k, v in CURRENT["certificate"].items()):
        raise ValueError("current certificate main binding changed")
    expected = CURRENT["certificate"]
    rec = outputs.get(expected["filename"], {})
    for name, key in (("bytes", "stored_bytes"), ("sha256", "stored_sha256"),
                      ("raw_bytes", "raw_bytes"), ("raw_sha256", "raw_sha256")):
        if rec.get(name) != expected[key]:
            raise ValueError("publication does not bind complete packed/raw current certificate")
    sources = publication.get("source_files", {})
    matched = [v for k, v in sources.items() if Path(k).name == CURRENT["driver"]["filename"]]
    if len(matched) != 1 or any(matched[0].get(k) != CURRENT["driver"][k]
                                for k in ("bytes", "sha256")):
        raise ValueError("publication does not bind current producer source")


def consume(args, report, budget):
    main, main_raw = read_small(args.source_report, CURRENT["report"])
    publication, _ = read_small(args.source_publication, CURRENT["publication"])
    check_current_publication(publication, main, main_raw)
    current = read_gzip(args.source_certificate, CURRENT["certificate"], budget)
    original = read_gzip(args.original_system_certificate, archived.PREVIOUS["certificate"], budget)
    if (current.get("schema") != CURRENT_SCHEMA + "-certificate"
        or current.get("source_hashes") != main["source_hashes"]
        or str(current.get("github_run_id")) != CURRENT["run"]
        or current.get("github_sha") != CURRENT["commit"]
        or current.get("input") != main["input"]
        or current.get("target_weight") != -2
        or current.get("all_true_positive_characters_embed_in_this_outer_system") is not True
        or current.get("old_source_system_or_integrals_recomputed") is not False):
        raise ValueError("current complete necessary-system semantics changed")
    previous = main["input"]
    for key in ("run", "commit", "lane"):
        if previous.get(key) != archived.PREVIOUS[key]:
            raise ValueError("current main no longer references the original complete system")
    if (previous.get("certificate") != archived.PREVIOUS["certificate"]
        or original.get("schema") != base.SCHEMA + "-certificate"
        or original.get("source_hashes", {}).get("driver") != archived.PREVIOUS["driver"]
        or original.get("target_weight") != -2
        or original.get("all_true_positive_characters_embed_in_this_outer_system") is not True):
        raise ValueError("original complete coefficient/coordinate semantics changed")
    inherited = current["inherited_system_identity_and_unchanged_data"]
    binds = {"old_equality_rows_sha256": original["equalities"],
             "old_original_inequality_rows_sha256": original["inequalities"],
             "old_rref_sha256": original["rref_equalities"],
             "old_transform_sha256": original["normal_coordinates_as_free_linear_forms"],
             "old_reduced_rows_sha256": original["reduced_inequalities"],
             "old_six_path_integrals_sha256": original["complete_path_integrals"]}
    if any(inherited.get(key) != sha(canonical(value)) for key, value in binds.items()):
        raise ValueError("archived complete system rows or transform were changed")
    if (current["free_normal_coordinates"] != original["free_normal_coordinates"]
        or inherited["free_normal_coordinates"] != original["free_normal_coordinates"]
        or inherited["normal_coordinate_count"] != original["normal_coordinate_count"]
        or inherited["old_static_polynomial_forms"] != original["corrected_scalar_k_polynomials"]["F0"]
        or current["updated_reduced_inequalities"][:len(original["reduced_inequalities"])]
           != original["reduced_inequalities"]):
        raise ValueError("the inherited actual coordinate/row prefix is not unchanged")
    if len(current["updated_reduced_inequalities"]) != 68:
        raise ValueError("the published 68-row static/parity system is required")
    if current.get("decision", {}).get("outer_candidate") is None:
        raise ValueError("published current exact point is missing")
    report["input"] = {"current": CURRENT,
        "original_complete_system_certificate": archived.PREVIOUS["certificate"],
        "original_complete_system_run": archived.PREVIOUS["run"],
        "original_complete_system_source": archived.PREVIOUS["commit"],
        "full_original_coefficients_and_transform_read_without_recomputation": True}
    return original, current


def transformed_families(data, budget):
    """Read every saved degree; reject unsupported nonzero static coefficients."""
    n = data["normal_coordinate_count"]
    free = data["free_normal_coordinates"]; dimension = len(free)
    if len(set(free)) != dimension or any(not isinstance(i, int) or not 0 <= i < n for i in free):
        raise ValueError("invalid inherited free-coordinate list")
    raw = data["normal_coordinates_as_free_linear_forms"]
    if len(raw) != n:
        raise ValueError("inherited transform length changed")
    transform = [base.read_row(row, dimension) for row in raw]
    for j, index in enumerate(free):
        if transform[index] != base.unit(j):
            raise ValueError("free coordinate meanings changed")
    stored = data["corrected_scalar_k_polynomials"]
    if set(stored) != set(base.FAMILIES):
        raise ValueError("the complete fourteen saved families are required")
    families = {}; static_support = []
    for family in base.FAMILIES:
        seen = set(); coefficients = {}
        for degree, row in stored[family]:
            if not isinstance(degree, int) or degree < 0 or degree in seen:
                raise ValueError("invalid or duplicate saved polynomial degree")
            seen.add(degree)
            normal = base.read_row(row, n)
            reduced = base.substitute(normal, transform)
            budget.check(reduced)
            coefficients[degree] = reduced
            if family == "F0":
                static_support.append({"degree": degree,
                    "stored_normal_form": deepcopy(row),
                    "free_form": base.serial_row(reduced),
                    "exactly_zero_after_old_transform": not bool(reduced)})
                if degree not in ALLOWED_STATIC_DEGREES and reduced:
                    raise ValueError("nonzero odd or above-six static coefficient: no sextic truncation allowed")
        families[family] = coefficients
    return transform, families, {"all_stored_F0_degrees_checked": True,
        "allowed_nonzero_degrees": list(ALLOWED_STATIC_DEGREES),
        "every_other_stored_degree_verified_exactly_zero": True,
        "degree_records": static_support,
        "old_RREF_recomputed": False}


def evaluate_saved_families(families, point, budget):
    result = {}
    for family, terms in families.items():
        result[family] = {}
        for degree, row in terms.items():
            value = base.apply_row(row, point)
            budget.check({0: value})
            result[family][degree] = value
    return result


def serialize_polynomials(families):
    return {family: [[degree, str(value)] for degree, value in sorted(terms.items())]
            for family, terms in families.items()}


def nonzero_poly(terms):
    return {degree: value for degree, value in terms.items() if value}


def replace_coordinate(saved, free, position, normal_index, value):
    point = list(map(F, saved))
    if len(point) != len(free) or not 0 <= position < len(point) or free[position] != normal_index:
        raise ValueError("the proposed one-coordinate replacement uses a different interface")
    if not any(point) or any(abs(v) > 1 for v in point):
        raise ValueError("stored nonzero rational boxed point is invalid")
    point[position] = F(value)
    if not any(point) or any(abs(v) > 1 for v in point):
        raise ValueError("new explicit point is not nonzero and in the normalization box")
    return point


def verify_rows(records, point, budget):
    values = []
    for index, record in enumerate(records):
        if record.get("index") != index:
            raise ValueError("archived inequality ordering changed")
        row = base.read_row(record["coefficients"], len(point))
        if not row:
            raise ValueError("archived reduced inequality is zero")
        value = base.apply_row(row, point); budget.check({0: value})
        values.append(value)
    return {"row_count": len(values), "all_rows_satisfied_exactly": all(v >= 0 for v in values),
        "values": list(map(str, values)),
        "negative_row_indices": [i for i, v in enumerate(values) if v < 0],
        "zero_row_indices": [i for i, v in enumerate(values) if v == 0]}


def polynomial(coefficients):
    p = list(map(F, coefficients))
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_eval(coefficients, x):
    out = F(0)
    for c in reversed(coefficients):
        out = out * x + c
    return out


def ceil_fraction(x):
    x = F(x)
    return -((-x.numerator) // x.denominator)


def oracle_halfline_cubic(coefficients, budget):
    """Exact sign classification on x>=0, returning rational k with p(k^2)<0.

    Degree <=3 only.  No algebraic-number library, floating roots or grid.
    Strict-negative critical cases use certified comparisons to bisect toward
    sqrt(r).  With no resource cap this loop terminates by strict continuity.
    This release's actual entry NEVER calls this function.
    """
    p = polynomial(coefficients)
    if len(p) > 4:
        raise ValueError("complete cubic oracle does not truncate higher degree")
    budget.check({i: c for i, c in enumerate(p)})
    cert = {"polynomial_ascending": list(map(str, p)), "domain": "x>=0; x=k^2",
            "all_arithmetic_exact_Q": True, "floating_roots_or_grid_used": False}

    def nonnegative(reason, **details):
        return {**cert, "classification": "globally_nonnegative", "reason": reason, **details}

    def negative(k, reason, **details):
        k = F(k); value = poly_eval(p, k*k)
        budget.check({0:k, 1:value})
        if not value < 0:
            raise AssertionError("claimed rational static witness is not strictly negative")
        return {**cert, "classification": "strictly_negative_somewhere", "reason": reason,
                "rational_k": str(k), "rational_x": str(k*k),
                "exact_value": str(value), **details}

    if not p:
        return nonnegative("zero_polynomial")
    if p[0] < 0:
        return negative(0, "negative_endpoint")
    degree = len(p)-1
    if degree == 0:
        return nonnegative("nonnegative_constant")
    leading = p[-1]
    if leading < 0:
        coefficient_ratio = max((abs(c/leading) for c in p[:-1]), default=F(0))
        bound = F(1)+coefficient_ratio
        budget.check({0:coefficient_ratio,1:bound})
        k = F(max(1, ceil_fraction(bound)))
        return negative(k, "negative_leading_coefficient",
                        positive_tail_x_bound=str(bound), integer_k_chosen_without_scan=str(k))
    if degree == 1:
        return nonnegative("increasing_affine_endpoint")
    critical = {}
    if degree == 2:
        d,b,a = p
        if b >= 0:
            return nonnegative("positive_quadratic_vertex_not_in_open_halfline")
        r = -b/(2*a)
        discriminant_margin = 4*a*d-b*b
        budget.check({0:r,1:discriminant_margin})
        critical = {"critical_point_x":str(r),"quadratic_minimum_numerator":str(discriminant_margin),
                    "quadratic_minimum_denominator":str(4*a)}
        if discriminant_margin >= 0:
            return nonnegative("nonnegative_positive_quadratic_minimum", **critical)
        high_bound = r
        def compare(x):
            return (x > r)-(x < r)
    else:
        d,c,b,a = p
        delta = b*b-3*a*c
        budget.check({0:delta})
        if delta <= 0:
            return nonnegative("cubic_derivative_nonnegative", delta=str(delta))
        if not (b < 0 or c < 0):
            return nonnegative("cubic_positive_local_minimum_absent", delta=str(delta),
                               positive_local_minimum_criterion="b<0 or c<0", b=str(b), c=str(c))
        T = 2*b*b*b-9*a*b*c+27*a*a*d
        difference = T*T-4*delta*delta*delta
        budget.check({0:T,1:difference})
        critical = {"delta":str(delta),"T":str(T),"T_squared_minus_4_delta_cubed":str(difference),
                    "critical_point_expression":"(-b+sqrt(delta))/(3a)",
                    "critical_value_expression":"(T-2*delta*sqrt(delta))/(27*a^2)",
                    "positive_local_minimum_criterion":"b<0 or c<0"}
        if T >= 0 and difference >= 0:
            return nonnegative("nonnegative_positive_cubic_minimum", **critical)
        high_bound = (abs(b)+delta+1)/(3*a)
        def compare(x):
            z = 3*a*x+b
            if z < 0:
                return -1
            difference = z*z-delta
            return (difference > 0)-(difference < 0)
    lower = F(0); upper = F(1+max(0,ceil_fraction(high_bound)))
    if compare(lower*lower) >= 0 or compare(upper*upper) <= 0:
        raise AssertionError("critical-point rational-k isolating interval is invalid")
    steps = 0
    while True:
        budget.check({0:lower,1:upper})
        middle = (lower+upper)/2
        value = poly_eval(p,middle*middle)
        if value < 0:
            return negative(middle,"strict_negative_critical_minimum_rational_isolation",
                            **critical, bisection_steps=steps,
                            last_k_bracket=[str(lower),str(upper)])
        direction = compare(middle*middle)
        if direction == 0:
            raise AssertionError("negative minimum evaluated nonnegative at its exact rational location")
        if direction < 0:
            lower = middle
        else:
            upper = middle
        steps += 1


def static_and_derivative_certificates(families):
    expected = {
        "F0":{0:F(1,2),2:F(-3,2),4:F(1),6:F(1)},
        "Q2_0":{0:F(1),2:F(1)}, "Q2_1":{1:F(-1),3:F(-1)},
        "Q2_2":{0:F(1),2:F(1),4:F(1)},
        "A_hh":{0:F(1),2:F(1)},"A_hk":{1:F(-1)},"A_kk":{0:F(1)},
        "H1":{1:F(-1)},"H2":{0:F(-1)},"Q4_0":{},"Q4_1":{},
        "Q4_2":{0:F(1)},"Q4_3":{1:F(-1)},"Q4_4":{0:F(1),2:F(1)}}
    matches = {f:nonzero_poly(families[f])==expected[f] for f in base.FAMILIES}
    # R172/R173 already prove these algebraic identities.  The new actual work
    # is the complete coefficient comparison above, not recomputing a Gram
    # certificate, a path integral or an old published identity.
    return {"matches_the_prescribed_fourteen_polynomials":matches,
        "static_SOS_applies":matches["F0"],
        "static_SOS_in_x":"(x+2)*(x-1/2)^2+x/4", "x":"k^2>=0",
        "static_strict_positivity_reason":"x=0 gives 1/2; x>0 gives x/4>0",
        "R173_uniform_static_lower_bound":"1/16",
        "R173_uniform_bound_reason":"x>=1/4 gives x/4>=1/16; 0<=x<=1/4 gives (x+2)*(x-1/2)^2>=1/8",
        "global_static_nonnegativity_proved_for_this_point":matches["F0"],
        "Q2_pointwise_SOS_applies":all(matches[f] for f in ("Q2_0","Q2_1","Q2_2")),
        "Q2_SOS":"(1+k^2)*(k_s-k*r_s/2)^2+(1+3*k^2/4+3*k^4/4)*r_s^2",
        "R172_highest_SOS_applicability":all(matches[f] for f in base.FAMILIES[4:]),
        "R172_highest_Gram_theta_eta":["-1","-1"],
        "R172_highest_SOS":"(Z1+Z2/2+Z3/2-Z4)^2+11*(Z2+3*Z3/11)^2/4+6*Z3^2/11+Z4^2",
        "already_proved_R172_R173_identities_recomputed":False,
        "no_previous_layer_certificate_inherited_without_complete_coefficient_match":True,
        "the_candidate_is_not_yet_a_functional_on_the_true_original_function_space":True}


def actual(args, report, ctx, budget):
    report["phase"]="consume_published_68_rows_and_archived_coefficient_forms"
    data,current = consume(args,report,budget)
    transform,families,support = transformed_families(data,budget)
    ctx["static_support_verification"] = support
    saved = current["decision"]["outer_candidate"]
    point = replace_coordinate(saved,data["free_normal_coordinates"],CHANGED_FREE_INDEX,
                               CHANGED_NORMAL_INDEX,CHANGED_VALUE)
    original_digest = sha(canonical(current["updated_reduced_inequalities"]))
    parent_point=list(map(F,saved))
    report["phase"]="one_prescribed_point_exact_archived_row_and_fourteen_family_evaluation"
    parent_values=evaluate_saved_families(families,parent_point,budget)
    values=evaluate_saved_families(families,point,budget)
    rows=verify_rows(current["updated_reduced_inequalities"],point,budget)
    normal_point=[base.apply_row(row,point) for row in transform]
    changed=[i for i,(old,new) in enumerate(zip(parent_point,point)) if old!=new]
    if changed != [CHANGED_FREE_INDEX]:
        raise AssertionError("more or fewer than the prescribed single coordinates changed")
    comparisons={family:values[family]==parent_values[family] for family in base.FAMILIES if family!="F0"}
    scalars={}
    for name in ("normalized_multiplier","translation_c","scaling_d"):
        scalars[name]=[str(base.apply_row(base.read_row(row,data["normal_coordinate_count"]),normal_point))
                       for row in data[name]]
    certificates=static_and_derivative_certificates(values)
    if scalars != {"normalized_multiplier":["0","1","2","0","0","0","0","4"],
                   "translation_c":["0"]*8,
                   "scaling_d":["0","2","6","0","0","0","0","8"]}:
        raise AssertionError("prescribed exact common multiplier/cocycle values did not match stored rows")
    if sha(canonical(current["updated_reduced_inequalities"]))!=original_digest:
        raise AssertionError("read-only verification mutated inherited rows")
    ctx.update(candidate_free_coordinates=list(map(str,point)),parent_candidate=list(saved),
        normal_coordinate_values=list(map(str,normal_point)),family_values=serialize_polynomials(values),
        parent_family_values=serialize_polynomials(parent_values),scalar_values=scalars,
        inequality_verification=rows,algebraic_certificates=certificates,
        unchanged_derivative_families=comparisons,
        inherited_reduced_inequalities=deepcopy(current["updated_reduced_inequalities"]),
        original_rows_sha256=original_digest)
    report["candidate_change"]={"free_coordinate":CHANGED_FREE_INDEX,"normal_coordinate":CHANGED_NORMAL_INDEX,
        "old_value":saved[CHANGED_FREE_INDEX],"new_value":str(CHANGED_VALUE),
        "all_other_free_coordinates_identical":True}
    report["static_support_verification"]={k:v for k,v in support.items() if k!="degree_records"}
    report["inequality_verification"]={k:v for k,v in rows.items() if k!="values"}
    report["fourteen_scalar_families"]=serialize_polynomials(values)
    report["unique_multiplier_and_cocycles"]=scalars
    report["unchanged_derivative_families"]=comparisons
    report["algebraic_certificates"]=certificates
    passed=(rows["all_rows_satisfied_exactly"]
            and all(certificates["matches_the_prescribed_fourteen_polynomials"].values())
            and all(comparisons.values()))
    report.update(completion="complete",phase="one_explicit_point_verification_complete",
        outcome=("explicit_outer_point_passes_68_rows_and_full_scalar_action_SOS_coefficients"
                 if passed else "explicit_outer_point_fails_at_least_one_required_archived_row_or_coefficient"),
        explicit_outer_point_verified=passed,positive_character_excluded=False,
        true_positive_character_constructed=False,complete_functional_relations_paid=False,
        original_function_membership_or_nonmembership_claimed=False,
        real_static_oracle_called=False,LP_or_RREF_or_path_integrals_called=False)


def toy_only():
    checks={};budget=base.Budget(40,512,16384)
    # Every polynomial below is invented.  No stored current point is consumed.
    examples=[
        ([],"globally_nonnegative"),([F(2)],"globally_nonnegative"),([F(-1)],"strictly_negative_somewhere"),
        ([0,2],"globally_nonnegative"),([1,-1],"strictly_negative_somewhere"),
        ([1,0,1],"globally_nonnegative"),([1,-2,1],"globally_nonnegative"),
        ([F(1,2),-2,1],"strictly_negative_somewhere"),
        ([1,0,0,1],"globally_nonnegative"),([1,1,1,1],"globally_nonnegative"),
        ([1,-1,-1,1],"globally_nonnegative"),([1,-3,0,1],"strictly_negative_somewhere"),
        ([1,1,-3,1],"strictly_negative_somewhere"),([1,5,-6,1],"strictly_negative_somewhere"),
        ([1,0,2,1],"globally_nonnegative"),([0,0,0,-1],"strictly_negative_somewhere"),
        ([3,5,-7,-2],"strictly_negative_somewhere"),([4,-3,0,1],"globally_nonnegative"),
    ]
    branches=[]
    for p,classification in examples:
        result=oracle_halfline_cubic(p,budget)
        assert result["classification"]==classification,(p,result)
        if classification=="strictly_negative_somewhere":
            k=F(result["rational_k"])
            assert poly_eval(polynomial(p),k*k)==F(result["exact_value"])<0
        branches.append({"input":list(map(str,p)),"classification":classification,"reason":result["reason"]})
    checks["exact_oracle_handles_constants_affine_quadratic_cubic_degeneracies_and_repeated_minimum"]=True
    # An arbitrarily small rational perturbation below a repeated minimum must
    # not be declared nonnegative by a floating tolerance.
    close=[F(1)-F(1,2**40),F(-1),F(-1),F(1)]
    r=oracle_halfline_cubic(close,budget)
    assert r["classification"]=="strictly_negative_somewhere"
    checks["strict_near_double_zero_is_resolved_by_exact_signs"]=True
    try:oracle_halfline_cubic([0,0,0,0,1],budget)
    except ValueError:checks["higher_degree_oracle_input_is_never_truncated"]=True
    else:raise AssertionError("degree four was silently truncated")
    data={"normal_coordinate_count":3,"free_normal_coordinates":[0,1],
          "normal_coordinates_as_free_linear_forms":[[[0,"1"]],[[1,"1"]],[[0,"1"],[1,"-1"]]],
          "corrected_scalar_k_polynomials":{f:[] for f in base.FAMILIES}}
    data["corrected_scalar_k_polynomials"]["F0"]=[[0,[[0,"1"]]],[2,[[1,"1"]]],
        [9,[[2,"1"],[0,"-1"],[1,"1"]]]]
    _,families,support=transformed_families(data,budget)
    assert support["degree_records"][-1]["exactly_zero_after_old_transform"]
    checks["all_extra_static_degrees_are_checked_after_exact_inherited_substitution"]=True
    for degree in (1,8):
        bad=deepcopy(data);bad["corrected_scalar_k_polynomials"]["F0"].append([degree,[[0,"1"]]])
        try:transformed_families(bad,budget)
        except ValueError:pass
        else:raise AssertionError("nonzero odd/high static degree was accepted")
    checks["nonzero_odd_or_high_static_coefficients_are_rejected"]=True
    old=["1/2","1/3"];point=replace_coordinate(old,[0,1],1,1,F(-1,2))
    assert old==["1/2","1/3"] and point==[F(1,2),F(-1,2)]
    rows=[{"index":0,"coefficients":[[0,"1"]]},
          {"index":1,"coefficients":[[0,"1"],[1,"1"]]},
          {"index":2,"coefficients":[[1,"1"]]}]
    read=verify_rows(rows,point,budget)
    assert read["negative_row_indices"]==[2] and read["zero_row_indices"]==[1]
    checks["point_replacement_is_copy_only_and_every_archived_row_is_verified"]=True
    names=("rref","construct_system","path_integrals","certify_zero",
           "rational_dual_proposal","rational_outer_candidate")
    saved={name:getattr(base,name) for name in names}
    def forbidden(*_a,**_kw):raise AssertionError("forbidden old research was invoked")
    try:
        for name in names:setattr(base,name,forbidden)
        transformed_families(data,budget);evaluate_saved_families(families,point,budget)
        verify_rows(rows,point,budget)
        checks["new_point_interface_does_not_call_old_RREF_LP_path_or_system_builders"]=True
    finally:
        for name,value in saved.items():setattr(base,name,value)
    return {"checks":checks,"all_passed":all(checks.values()),"invented_oracle_cases":branches,
        "artificial_rational_arithmetic_only":True,"real_input_or_candidate_read":False,
        "real_oracle_or_solver_run":False,"old_artificial_suites_repeated":False}


def complete_certificate(report,ctx):
    if not ctx:return None
    complete=all(key in ctx for key in ("candidate_free_coordinates","normal_coordinate_values",
                                       "family_values","inequality_verification","scalar_values"))
    return {"schema":SCHEMA+"-certificate","source_hashes":report["source_hashes"],
        "github_run_id":report["github_run_id"],"github_sha":report["github_sha"],
        "input":report.get("input"),"target_weight":-2,**ctx,
        "complete_point_evaluation_saved":complete,
        "all_original_functional_relations_have_not_been_imposed":True,
        "scalar_action_SOS_does_not_construct_a_true_character":True,
        "old_RREF_LP_path_integrals_or_function_expressions_recomputed":False}


def write_outputs(args,report,certificate):
    args.output.parent.mkdir(parents=True,exist_ok=True);packed=b""
    if certificate is not None:
        raw=canonical(certificate)+b"\n";packed=gzip.compress(raw,mtime=0)
        if len(packed)>args.max_certificate_bytes:
            raise base.Limit("complete explicit-point certificate exceeds output budget")
        path=args.output.with_name(args.output.stem+"-certificate.json.gz");path.write_bytes(packed)
        report["complete_candidate_certificate"]={"filename":path.name,"stored_bytes":len(packed),
            "stored_sha256":sha(packed),"raw_bytes":len(raw),"raw_sha256":sha(raw),
            "contains_all_68_values_all_107_normal_values_and_all_fourteen_polynomials":
                certificate["complete_point_evaluation_saved"]}
    raw=canonical(report)+b"\n"
    if len(raw)>args.max_main_bytes or len(raw)+len(packed)>4800000:
        raise base.Limit("bounded explicit-point publication output limit")
    args.output.write_bytes(raw)
    return {"output":str(args.output),"completion":report["completion"],"bytes":len(raw),"sha256":sha(raw)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    for name in ("source-report","source-publication","source-certificate","original-system-certificate"):
        parser.add_argument("--"+name,type=Path)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--max-seconds",type=float,default=120)
    parser.add_argument("--memory-mib",type=int,default=512)
    parser.add_argument("--rational-bits",type=int,default=16384)
    parser.add_argument("--max-main-bytes",type=int,default=95000)
    parser.add_argument("--max-certificate-bytes",type=int,default=4500000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.rational_bits,args.max_main_bytes,args.max_certificate_bytes)<=0:
        parser.error("positive explicit budgets required")
    if args.max_main_bytes>=100000 or args.max_main_bytes+args.max_certificate_bytes>4800000:
        parser.error("main below100KB and total output at most4.8MB required")
    if not args.toy_only and not all((args.source_report,args.source_publication,args.source_certificate,
                                    args.original_system_certificate)):
        parser.error("all four exact published inputs are required")
    if not args.toy_only and (os.environ.get("GITHUB_ACTIONS")!="true"
                              or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        parser.error("actual point verification only in this public repository Actions")
    started=time.monotonic();budget=base.Budget(args.max_seconds,args.memory_mib,args.rational_bits)
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "source_hashes":{},"target_weight":-2,"positive_character_excluded":False,
        "true_positive_character_constructed":False,"original_function_membership_or_nonmembership_claimed":False,
        "theorem_prerequisites":["R164","R168","R171","R172","R173"],
        "old_RREF_LP_path_integrals_or_function_expressions_recomputed":False,
        "real_static_oracle_called":False,"oracle_utility_used_only_by_new_artificial_examples":True,
        "limits":{"elapsed_seconds":args.max_seconds,"polled_memory_mib":args.memory_mib,
                  "rational_bit_ceiling":args.rational_bits,"main_bytes":args.max_main_bytes,
                  "certificate_bytes":args.max_certificate_bytes}}
    ctx={};code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["toy"]=toy_only()
            report.update(completion="toy_passed",phase="new_exact_cubic_oracle_and_copy_only_point_artificial_tests")
        else:actual(args,report,ctx,budget)
    except base.Limit as error:
        code=2;report.update(completion="resource_limit",error=str(error))
    except Exception as error:
        code=1;report.update(completion="implementation_check_failed",error={"type":type(error).__name__,"message":str(error)})
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    try:written=write_outputs(args,report,complete_certificate(report,ctx))
    except base.Limit as error:
        code=2
        failed={k:report[k] for k in ("schema","phase","github_repository","github_run_id","github_sha",
                                    "source_hashes","target_weight","elapsed_seconds","peak_rss_mib") if k in report}
        failed.update(completion="output_limit",error=str(error),positive_character_excluded=False,
                      true_positive_character_constructed=False,complete_candidate_certificate_not_saved=True)
        if "input" in report:failed["input_identity_sha256"]=sha(canonical(report["input"]))
        raw=canonical(failed)+b"\n";args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(raw)
        written={"output":str(args.output),"completion":"output_limit","bytes":len(raw),"sha256":sha(raw)}
    print(json.dumps(written),flush=True)
    return code


if __name__=="__main__":
    raise SystemExit(main())
