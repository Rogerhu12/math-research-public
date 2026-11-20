#!/usr/bin/env sage-python
"""Read the already certified original v_F and three Y_i in complete sections.

Both actual characteristic-zero PASS receipts are authenticated before any
mathematics.  R881 identifies the complete finite-field kernels with the same
original reductions.  This stage does not claim the cube roots, all divisors,
or the original Frobenius shadow have been computed.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public repository Actions.")
if any(os.environ.get(key) for key in ("GH_TOKEN", "GITHUB_TOKEN", "RANK2_GITHUB_TOKEN")):
    raise SystemExit("Keep every repository token on the host outside Sage.")

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path
from sage.all import PowerSeriesRing, vector
from sage.env import SAGE_VERSION
from original_shadow_receipt_tools import (
    canonical, digest, add_pinned_arguments, pinned_request, validate_envelope)
from original_shadow_coordinate_tools import (
    certificate_weight, complete_product_recipes, prime_residue,
    solve_first, solve_packet, row_serial)
import original_shadow_coordinate_tools

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"


def progress(stage, **kw):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_MAP_SECTIONS_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)


def import_file(filename, module_name):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def series_digest(series, length):
    return digest(row_serial([series[i] for i in range(length)]))


def section_sum(coefficients, rr_basis, S, power, ring, precision):
    """Keep the actual S^power when returning RR functions to sections."""
    assert len(coefficients) == len(rr_basis)
    rr = ring.zero().add_bigoh(precision)
    for coefficient, basis in zip(coefficients, rr_basis):
        if coefficient:
            rr += ring.base_ring()(coefficient)*ring(basis)
    rr = rr.add_bigoh(precision)
    modular = (rr*S**power).add_bigoh(precision)
    return rr, modular


def build_original_map_section_fractions(prime, first, packet, q_precision=1429):
    prime, q_precision = int(prime), int(q_precision)
    assert prime in (29, 41)
    kF, kP = certificate_weight(first, "F"), certificate_weight(packet, "P")
    needed = max(204*kF+613, 204*kP+2)
    assert q_precision >= needed
    r917 = import_file("produce-r917-original-global-rr-q-lattice.py", "map_sections_r917")
    local_module = import_file("produce-original-shadow-local-input.py", "map_sections_local")
    progress("same authenticated original local inputs start", prime=prime,
             original_F_weight=kF, original_P_weight=kP)
    local, local_receipt = local_module.build_local_input(prime, 1226, 1428, 64, (0, 1, 2))
    original, original_receipt = r917.build_original_global_rr_q_lattice(prime, q_precision)
    fp, k = original["constants"], local["constants"]
    assert int(fp.cardinality()) == prime and int(k.cardinality()) == prime**2
    rr_rows = original["original_rr_jets"]
    maximum = max(kP//2, (kF+6)//2)
    recipes, series = complete_product_recipes(
        {"constants":fp}, [list(row) for row in rr_rows.rows()], maximum, q_precision)
    ring = PowerSeriesRing(k, "Q", default_prec=q_precision)
    Q = ring.gen()
    S = ring(original["original_denominator_q_series"]).add_bigoh(q_precision)
    assert S[0] == 1

    a, b = (kF+6)//2, kF//2
    first_row = [prime_residue(z, fp) for z in local["first"]["vF"]]
    progress("same original F complete low kernel start", weight=kF)
    fsol, fmeta = solve_first(series, first_row, kF, fp)
    da = len(series[a])
    fA_rr, fA = section_sum(fsol[:da], series[a], S, a, ring, q_precision)
    fB_rr, fB = section_sum(fsol[da:], series[b], S, b, ring, q_precision)
    fDen = (fB*S**3).add_bigoh(q_precision)
    fN = 204*kF+613
    assert fB_rr and fDen and fA
    assert (fA-fDen*ring(local["first"]["vF"])).add_bigoh(fN) == 0
    assert (fA*fB_rr-fA_rr*fDen).add_bigoh(q_precision) == 0
    first_context = {
        "original_coordinate":"v_F", "numerator_power":a,
        "denominator_recipe_power":b, "denominator_S_power":3,
        "numerator_coordinates":vector(k, fsol[:da]),
        "denominator_recipe_coordinates":vector(k, fsol[da:]),
        "numerator_modular_jets":fA,
        "denominator_recipe_modular_jets":fB,
        "same_degree_denominator_modular_jets":fDen,
        "RR_numerator_jets":fA_rr, "RR_denominator_jets":fB_rr,
        "complete_pole_degree_upper_bound":204*a,
    }
    first_record = dict(fmeta,
        numerator_section_power=a, denominator_recipe_section_power=b,
        denominator_S_power=3, same_degree_section_power=a,
        complete_pole_degree_upper_bound=204*a,
        same_original_ratio_identified_by_R881=True,
        true_modular_fraction="A_F/(B_F*S^3)",
        numerator_coordinates_sha256=digest(row_serial(fsol[:da])),
        denominator_recipe_coordinates_sha256=digest(row_serial(fsol[da:])),
        numerator_modular_jets_sha256=series_digest(fA, q_precision),
        denominator_modular_jets_sha256=series_digest(fDen, q_precision))
    progress("same original F ratio globally identified", **first_record)

    power = kP//2
    dim = len(series[power])
    pcontexts, precords = {}, []
    for i in (0, 1):
        field = fp if i == 0 else k
        local_row = ([prime_residue(z, fp) for z in local["packet"][i]["QY"]]
                     if i == 0 else local["packet"][i]["QY"])
        progress("same original P complete low kernel start", embedding=i, weight=kP)
        solution, meta = solve_packet(series, local_row, kP, field)
        pA_rr, pA = section_sum(solution[:dim], series[power], S, power, ring, q_precision)
        pB_rr, pB = section_sum(solution[dim:], series[power], S, power, ring, q_precision)
        pN = 204*kP+2
        qy = ring(local["packet"][i]["QY"])
        assert pA and pB
        assert (Q*pA-qy*pB).add_bigoh(pN) == 0
        assert (pA*pB_rr-pA_rr*pB).add_bigoh(q_precision) == 0
        assert int(pB.valuation()) == int(pA.valuation())+1
        pcontexts[i] = {
            "original_coordinate":"Y_"+str(i), "section_power":power,
            "numerator_coordinates":vector(k, solution[:dim]),
            "denominator_coordinates":vector(k, solution[dim:]),
            "numerator_modular_jets":pA, "denominator_modular_jets":pB,
            "RR_numerator_jets":pA_rr, "RR_denominator_jets":pB_rr,
            "a17":local["packet"][i]["a17"],
            "lambda":local["packet"][i]["lambda"],
            "v":local["packet"][i]["v"], "vnew":local["packet"][i]["vnew"],
            "complete_pole_degree_upper_bound":204*power,
        }
        record = dict(meta, embedding=i, same_degree_section_power=power,
            exact_original_ratio_identified_by_R881=True,
            same_S_factors_cancelled_power=power,
            complete_pole_degree_upper_bound=204*power,
            numerator_coordinates_sha256=digest(row_serial(solution[:dim])),
            denominator_coordinates_sha256=digest(row_serial(solution[dim:])),
            numerator_modular_jets_sha256=series_digest(pA, q_precision),
            denominator_modular_jets_sha256=series_digest(pB, q_precision))
        precords.append(record)
        progress("same original P ratio globally identified", **record)

    # Constant-field conjugation fixes every original rational global basis
    # section.  It is distinct from the original Artin permutation (2,0,1).
    p1 = pcontexts[1]
    p2 = {key:value for key, value in p1.items()
          if key not in ("numerator_coordinates", "denominator_coordinates",
                         "numerator_modular_jets", "denominator_modular_jets",
                         "RR_numerator_jets", "RR_denominator_jets")}
    p2["original_coordinate"] = "Y_2"
    for key in ("numerator_coordinates", "denominator_coordinates"):
        p2[key] = vector(k, [c**prime for c in p1[key]])
    for key in ("numerator_modular_jets", "denominator_modular_jets",
                "RR_numerator_jets", "RR_denominator_jets"):
        p2[key] = ring([p1[key][j]**prime for j in range(q_precision)]).add_bigoh(q_precision)
    for key in ("a17", "lambda", "v", "vnew"):
        p2[key] = p1[key]**prime
        assert p2[key] == local["packet"][2][key]
    assert [z**prime for z in local["packet"][1]["QY"]] == local["packet"][2]["QY"]
    assert (Q*p2["numerator_modular_jets"]-
            ring(local["packet"][2]["QY"])*p2["denominator_modular_jets"]).add_bigoh(204*kP+2) == 0
    pcontexts[2] = p2
    precords.append({
        "embedding":2, "source":"exact constant Frobenius of original embedding 1",
        "same_original_third_QY_germ_verified":True,
        "original_Artin_operator_unchanged":True,
        "numerator_coordinates_sha256":digest(row_serial(p2["numerator_coordinates"])),
        "denominator_coordinates_sha256":digest(row_serial(p2["denominator_coordinates"])),
        "numerator_modular_jets_sha256":series_digest(p2["numerator_modular_jets"], q_precision),
        "denominator_modular_jets_sha256":series_digest(p2["denominator_modular_jets"], q_precision)})
    context = {
        "kind":"rank2_original_map_section_fractions_context",
        "prime":prime, "constants":k, "original_fp":fp,
        "original_r917_context":original, "local_context":local,
        "complete_RR_product_recipes":recipes, "complete_RR_product_series":series,
        "original_S_series":S, "F":first_context, "P":pcontexts,
        "original_omega":local["omega"], "sigma_a_index":local["sigma_a_index"],
        "q_precision":q_precision, "first_certificate":first, "packet_certificate":packet,
    }
    deps = [Path(r917.__file__), Path(local_module.__file__),
            Path(original_shadow_coordinate_tools.__file__),
            HERE/"original_shadow_receipt_tools.py", HERE/"original_pari_m2_basis.py",
            HERE/"original_good_prime_germ_tools.py", HERE/"check-r873-original-cm-petersson-degree.py",
            HERE/"original_low_weight_cm_tools.py"]
    result = {
        "kind":"rank2_original_map_section_fractions",
        "status":"same_original_vF_and_three_Y_section_ratios_identified",
        "prime":prime, "level":867, "q_precision":q_precision,
        "F_weight":kF, "P_weight":kP,
        "first_original_source":first["source"], "first_original_run":first["run_id"],
        "packet_original_source":packet["source"], "packet_original_run":packet["run_id"],
        "original_local_input":local_receipt, "original_complete_RR_input":original_receipt,
        "complete_product_recipes_sha256":digest(recipes),
        "F":first_record, "P":precords,
        "sigma_a_index":[int(i) for i in local["sigma_a_index"]],
        "original_cube_roots_computed":False,
        "complete_divisors_computed":False, "original_shadow_computed":False,
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "image":os.environ.get("RANK2_IMAGE"), "sage_version":SAGE_VERSION,
        "readme_blobs":{"root":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in deps},
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    return context, result


def main():
    parser = argparse.ArgumentParser()
    add_pinned_arguments(parser)
    args = parser.parse_args()
    request = pinned_request(args)
    incoming = sys.stdin.buffer.read(2*1024*1024+1)
    assert len(incoming) <= 2*1024*1024
    envelope = json.loads(incoming.decode("utf-8"))
    host_hash = hashlib.sha256((HERE/"read-original-shadow-pass-receipts.py").read_bytes()).hexdigest()
    first, packet = validate_envelope(envelope, request, host_hash)
    progress("both original complete characteristic-zero PASS receipts authenticated",
             public_pass_envelope_sha256=envelope["envelope_sha256"])
    context, result = build_original_map_section_fractions(args.prime, first, packet)
    globals()["ORIGINAL_MAP_SECTION_FRACTIONS"] = context
    result["public_pass_envelope_sha256"] = envelope["envelope_sha256"]
    result["authenticated_public_jobs"] = envelope["authentication"]
    payload = canonical(result)
    print("RANK2_MAP_SECTIONS_RESULT "+payload, flush=True)
    print("RANK2_MAP_SECTIONS_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed, exception_type=type(exc).__name__, message=str(exc))
        raise
