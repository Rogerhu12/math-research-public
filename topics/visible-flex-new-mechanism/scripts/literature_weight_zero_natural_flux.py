#!/usr/bin/env python3
"""Two new complete natural-flux observations, on the paid H* and J6.

Only public Actions may run this entry point, including its new fixtures.
Read the two original MEMBER reports and reuse their pure/self identities.
Restore C2/C6 and six required old mixed responses once. Never rerun an old
pure/self map, old rank, profile evaluation, N contraction, or forcing.
The only new scientific maps are 4*left I(u''' M_-2(u,u)), with the SAME anchor.
A surviving nonlocal word is unresolved, never a nonzero-functional verdict.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import time

import literature_weight_zero_joint_self_completion as paid

completed, prior = paid.completed, paid.prior
pure, zero, head, literal = paid.pure, paid.zero, paid.head, paid.literal
colored, exact, formal = paid.colored, paid.exact, paid.formal
selfmap, priority = paid.selfmap, paid.selfmap.priority
canonical, sha = paid.canonical, paid.sha

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
ENTRY = TOPIC + "/scripts/literature_weight_zero_natural_flux.py"
SCHEMA = "visible-flex-weight-zero-natural-flux-two-targets-v1"
REQUEST_SCHEMA = SCHEMA + "-request"
FROZEN_SOURCES = json.loads(r'''{
  "topics/visible-flex-new-mechanism/scripts/literature_character_zero_endpoint_layer.py": "bb7be8fc3fa6b98f3f69aca96e5145c6df1f3d581ea85d14aa7fb6ccfefe6a94",
  "topics/visible-flex-new-mechanism/scripts/literature_endpoint_first_layer.py": "cf14e26c215bd93feb43dc4b56b8ecdcf9f9013084236e772229404eb9401b69",
  "topics/visible-flex-new-mechanism/scripts/literature_character_zero_pure_readout.py": "8d99414bda0a9bf61925f74e5378bfe80532fc8d9b9d35d6cc73625f8f15f7d1",
  "topics/visible-flex-new-mechanism/scripts/literature_character_head_zero.py": "337966b4fb9a417ed62d650cac87ffc4c41bedc9938e11c1520fe1136b53dee4",
  "topics/visible-flex-new-mechanism/scripts/literature_color_priority_words.py": "ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9",
  "topics/visible-flex-new-mechanism/scripts/literature_colored_profile_algebra.py": "c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f",
  "topics/visible-flex-new-mechanism/scripts/literature_pure_bulk_exact_membership.py": "f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70",
  "topics/visible-flex-new-mechanism/scripts/literature_pure_bulk_word_normal_form.py": "d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65",
  "topics/visible-flex-new-mechanism/scripts/literature_character_head_literal_relations.py": "80ab553a2dbb35fd4547beaf1b7ad094e831a2cb7f02e4968b867c4654cd9995",
  "topics/visible-flex-new-mechanism/scripts/literature_character_head_minus2.py": "fcc41b4d5a640a1ac411e7f6f29622db81c39cb2be37aed7811136418a045f11",
  "topics/visible-flex-new-mechanism/scripts/literature_range_profile_algebra.py": "a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52",
  "topics/visible-flex-new-mechanism/scripts/literature_acceleration_layer_mixed.py": "271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c",
  "topics/visible-flex-new-mechanism/scripts/literature_constrained_static_fourth.py": "814e1338679914b32542f8b360978281002ee02a2c4e8c03912aa40c876786f4",
  "topics/visible-flex-new-mechanism/scripts/literature_G_first_translation.py": "331fea2c1aef154c4d5866e4708f067c555f9fb61f02a11ee32a7f44d25f01f5",
  "topics/visible-flex-new-mechanism/scripts/literature_local_fourth_derivative_factors.py": "02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf",
  "topics/visible-flex-new-mechanism/scripts/literature_full_m8_tail_response_projection.py": "e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345",
  "topics/visible-flex-new-mechanism/scripts/literature_local_fourth_quotient.py": "9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0",
  "topics/visible-flex-new-mechanism/scripts/literature_static_G_rational_dual.py": "0872f0fc8b561a547342d530239e35c6ac9a37a5bddc5c472bf16c0df73ac477",
  "topics/visible-flex-new-mechanism/scripts/literature_c7_transverse_tail_probe.py": "98c879d83799e275e145310f5c9fdd9b85a87503d15f1690925d2f648ebc305b",
  "topics/visible-flex-new-mechanism/scripts/literature_full_phase_rational_dual.py": "bcfb26b85918a8648ad98bbde7643c4cf6d01d34b35c53bc06c3dbaff31de84f",
  "topics/visible-flex-new-mechanism/scripts/literature_total_P1_scaling_blocks.py": "40ff170136838907ecb4d2557c2ba3b4d06b5f3fcf63746697f3d5248e92d0fa",
  "topics/visible-flex-new-mechanism/scripts/literature_closed_c1_endpoint.py": "b0c9c5a74cdc50935f97fbe1641b705155dbec82e42750393da2a34f38357bd1",
  "topics/visible-flex-new-mechanism/scripts/literature_full_phase_bridge_exact.py": "d7513321bea70248851e9b71b02c97b7e869531097f290de40257c94507fed0e",
  "topics/visible-flex-new-mechanism/scripts/literature_local_third_bridge_decompose.py": "08ada4219df23e50dff2c784c2457dab3c732cd82cacc1477389fdc53fbb6ee0",
  "topics/visible-flex-new-mechanism/scripts/literature_G_translation_successor.py": "a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406",
  "topics/visible-flex-new-mechanism/scripts/literature_h_axis_sharp_coefficient.py": "7f4ee057a16a620e089102ea9c84fccafd922306e8febf8b73391b478e4a4a0b",
  "topics/visible-flex-new-mechanism/scripts/literature_rational_volterra_polynomial.py": "6bf16dd5c6cc8157fd53b20b58b504a5c3ea56ade9db9b62a30d385e5e69fd22",
  "topics/visible-flex-new-mechanism/scripts/literature_linear_third_bridge_quotient.py": "0627875fe06950c9e7c360baaf0429451697a460e2cf10aa6b3434c501363bd2",
  "topics/visible-flex-new-mechanism/scripts/literature_full_self_euler_coordinates.py": "95ec818ce1fdf815b0390aaf2ad4f976a0dfc7bd0b5218899acd4f4bc271f9ba",
  "topics/visible-flex-new-mechanism/scripts/literature_weight_zero_complete_self.py": "9347caeb4ff7ed54cc88f6c38183d4773d8e12125a5a9631412674550d42b78f",
  "topics/visible-flex-new-mechanism/scripts/literature_weight_zero_joint_self_completion.py": "1f5d671598ca6fc4a804c6f22a65d145b5ced3743506a2144d507717ff4789d3"
}''')
PARAMETERS = {
    "max_seconds": 120,
    "memory_mib": 512,
    "integer_bits": 8192,
    "max_terms": 100000,
    "max_IBP_calls": 300000,
    "max_cache_entries": 250000,
    "max_report_bytes": 95000,
    "max_log_bytes": 8 * 1024 * 1024,
}
RECEIPTS = {
    "Hstar": {
        "run": "43735872441", "job": "132878270740",
        "source": "ca186db057ed753abe565d0c3c2c8305278b5af7",
        "lane": "weight_zero_complete_self",
        "schema": "visible-flex-weight-zero-complete-self-gate-v1",
        "directory": TOPIC + "/notes/actions-43735872441-1-weight_zero_complete_self",
        "receipt": {"bytes": 55780,
                    "sha256": "8d79ddda157153788ae70bb1cc44d6c64d4672541bb2e66f7cfbaf33f9549701"},
        "main": {"filename": "weight-zero-complete-self.json", "bytes": 61441,
                 "sha256": "731ffae43cc8f06346801c444a7de010fe2cf6f9f05ecf4b650d319fa2ee06fd"},
        "log": {"bytes": 182877,
                "sha256": "4d658489abd694f9f4cde2204aec9d23dc507d9ebae47168e42123cf4ff1288f"},
    },
    "J6": {
        "run": "43740129876", "job": "132891272196",
        "source": "a5383f62d353890cc24e927b669dd2d6b67f8c78",
        "lane": "weight_zero_joint_self_completion",
        "schema": "visible-flex-weight-zero-C4-C6-complete-self-v1",
        "directory": TOPIC + "/notes/actions-43740129876-1-weight_zero_joint_self_completion",
        "receipt": {"bytes": 56025,
                    "sha256": "2854aecf26a0abf3b013d0674965315a3ba1702c681b76cf7f9ba1ba32947004"},
        "main": {"filename": "weight-zero-joint-self-completion.json", "bytes": 37516,
                 "sha256": "d4c5709c150392118ea0189be0f2114e52e9511df12d90f139836cace3863ca3"},
        "log": {"bytes": 136609,
                "sha256": "6808d07a3ed6b20d503691de9c979ab5accd9526f52861906c4196ff53d49758"},
    },
}
ORIGINALS = {
    2: {"state": (0, 2, 0, 0),
        "mixed_sha256": "b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f"},
    6: {"state": (1, 1, 1, 0),
        "mixed_sha256": "5ca598f50107cf8f059608f27694ad87bb5cbd26be152ff18d8d0f2e2a95bc02"},
}
TARGETS = {
    "Hstar": {
        "normal_index": 2,
        "response": {2: F(649, 768), 3: F(-73, 3072), 4: F(649, 1536),
                     5: F(-821, 768), 7: F(1, 64), 9: F(187, 1024)},
        "mixed_sha256": "c556d1a99522bb8cdc828d38ff00c8121ecaf7ad02dfe36861d26c547fb2ba76",
        "diagonal_sha256": "c181256a91943ff0df4474737cf097e91cfcf3851810bdeac62047da982df298",
    },
    "J6": {
        "normal_index": 6,
        "response": {2: F(-5, 384), 3: F(5, 1536), 4: F(-5, 768),
                     5: F(1, 384), 9: F(1, 512)},
        "mixed_sha256": "432254370e395477f7636d7f16348a4d3467ffd11b8189a8d249ec813596724e",
        "diagonal_sha256": "163cb66d73959b8db6023525e5cb07755346950b7a4b8d7cb5ec9c17c16a74dd",
    },
}
RESPONSE_LABELS = {
    2: ("p1", 1), 3: ("p1", 12), 4: ("p1", 16),
    5: ("p1", 35), 7: ("p2", 6), 9: ("p2", 14),
}
GAMMA_SHA = "c6276335dd47380509870798123478dc1b5a25ad83f3eef15d30cedcef4ece0b"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_path(repository, text):
    require(isinstance(text, str), "repository path must be text")
    path = Path(text)
    require(not path.is_absolute() and ".." not in path.parts,
            "only relative repository paths are accepted")
    result = (repository / path).resolve()
    require(result.is_relative_to(repository), "repository path escaped its root")
    return result


def read_request(path, repository):
    raw = path.read_bytes()
    require(len(raw) < 100000, "small UTF-8 request required")
    item = paid.decode_json(raw)
    require(item.get("schema") == REQUEST_SCHEMA and
            item.get("repository") == REPOSITORY and
            item.get("entry_point") == ENTRY and
            item.get("targets") == ["Hstar", "J6"] and
            item.get("parameters") == PARAMETERS,
            "the two-target scope or original resource limits changed")
    bindings = item.get("source_sha256", {})
    require(isinstance(bindings, dict) and
            all(bindings.get(k) == v for k, v in FROZEN_SOURCES.items()),
            "the complete 31-file frozen source closure changed")
    require(ENTRY in bindings, "new entry source must be explicitly bound")
    identities = {}
    for name, digest in sorted(bindings.items()):
        source = safe_path(repository, name)
        source_raw = source.read_bytes()
        require(sha(source_raw) == digest, "source SHA mismatch: " + name)
        identities[name] = {"bytes": len(source_raw), "sha256": digest}
    require(Path(__file__).resolve() == safe_path(repository, ENTRY),
            "the executed entry is not the bound repository file")
    return item, {"bytes": len(raw), "sha256": sha(raw)}, identities


def report_from_exact_log(raw, spec):
    """Select the paid MAIN by its exact bytes, not tag uniqueness.

    The same job also prints a development COMPLETE_REPORT of the same schema.
    It is deliberately not read as a scientific result.
    """
    matches = []
    for number, line in enumerate(raw.decode("utf-8-sig").splitlines(), 1):
        clean = paid.ANSI.sub("", line).lstrip("\ufeff")
        clean = paid.TIME_PREFIX.sub("", clean)
        if not clean.startswith("COMPLETE_REPORT "):
            continue
        payload = clean[len("COMPLETE_REPORT "):]
        exact_bytes = payload.encode("utf-8") + b"\n"
        if (len(exact_bytes) != spec["main"]["bytes"] or
                sha(exact_bytes) != spec["main"]["sha256"]):
            continue
        item = paid.decode_json(payload)
        require(item.get("schema") == spec["schema"], "paid report schema mismatch")
        matches.append((item, number))
    require(len(matches) == 1, "one exact original MAIN report required")
    return matches[0]


def coefficient_rows(values):
    return [[j, str(v)] for j, v in sorted(values.items()) if v]


def bind_paid_target(name, repository, reader, report):
    spec, target = RECEIPTS[name], TARGETS[name]
    directory = safe_path(repository, spec["directory"])
    receipt, _ = literal.read_small(directory / "receipt.json", spec["receipt"])
    require(receipt.get("schema") == "visible-new-mechanism-actions-metadata-only-v2" and
            receipt.get("repository") == REPOSITORY and
            str(receipt.get("run_id")) == spec["run"] and
            receipt.get("source_commit") == spec["source"] and
            receipt.get("lane") == spec["lane"] and
            receipt.get("output_payloads_committed_or_uploaded") is False,
            "paid run receipt identity changed")
    paid.output_identity(receipt, spec["main"]["filename"], spec["main"], True)
    run = reader.api("/actions/runs/" + spec["run"])
    job = reader.api("/actions/jobs/" + spec["job"])
    require(str(run.get("id")) == spec["run"] and
            run.get("head_sha") == spec["source"] and
            str(job.get("id")) == spec["job"] and
            str(job.get("run_id")) == spec["run"] and
            (not job.get("head_sha") or job["head_sha"] == spec["source"]) and
            run.get("status") == job.get("status") == "completed" and
            run.get("conclusion") == job.get("conclusion") == "success" and
            spec["lane"] in job.get("name", ""),
            "paid original run/job source or completion changed")
    raw, redirects = reader.log(spec["job"])
    require(len(raw) == spec["log"]["bytes"] and sha(raw) == spec["log"]["sha256"],
            "the complete original job log identity changed")
    old, line = report_from_exact_log(raw, spec)
    require(old.get("completion") == "complete" and
            old.get("github_repository") == REPOSITORY and
            str(old.get("github_run_id")) == spec["run"] and
            old.get("github_sha") == spec["source"],
            "paid scientific MAIN identity changed")
    source_records = paid.source_tree_in_receipt(old.get("source_hashes"), receipt)
    require(source_records > 0, "the original source closure is absent")
    if name == "Hstar":
        decision = old.get("decision", {})
        representative = decision.get("new_representative", {})
        proof = decision.get("fresh_original_verification", {})
        coefficients = representative.get("original_response_coefficients")
        require(decision.get("outcome") == "MEMBER" and
                representative.get("universal_pure_zero") is True and
                representative.get("whole_universal_self_zero") is True and
                representative.get("lambda_plus") == "1" and
                proof.get("fresh_T_and_complete_Euler_exact_zero") is True,
                "R316 did not prove the required same pure/self representative")
    else:
        decisions = [row for row in old.get("decisions", [])
                     if row.get("normal_index") == 6]
        require(len(decisions) == 1, "the original C6 decision is ambiguous")
        decision = decisions[0]
        representative = decision.get("joint_zero_representative", {})
        proof = decision.get("fresh_original_verification", {})
        coefficients = representative.get("original_R126_coefficients")
        require(decision.get("outcome") == "MEMBER" and
                representative.get("universal_pure_zero") is True and
                representative.get("whole_universal_self_zero") is True and
                proof.get("fresh_T_and_complete_Euler_zero") is True,
                "R329 did not prove the required same pure/self representative")
    require(coefficients == coefficient_rows(target["response"]) and
            proof.get("original_mixed_difference_sha256") == target["mixed_sha256"],
            "the paid full original combination or mixed root changed")
    diagonal_hash = proof.get("fresh_global_diagonal_sha256",
                              proof.get("global_diagonal_sha256"))
    require(diagonal_hash == target["diagonal_sha256"],
            "the paid same-color diagonal identity changed")
    report["inputs"][name + "_paid_identity"] = {
        **spec, "main_line_in_complete_original_log": line,
        "source_leaf_records_checked": source_records,
        "log_redirects_without_forwarded_API_credential": redirects,
        "exact_original_response_combination": coefficients,
        "original_mixed_sha256": target["mixed_sha256"],
        "old_pi_or_self_evaluation_performed": False,
    }


def restore_needed_roots(ring, repository, budget, report):
    """Necessary input reconstruction only: 2 static mixed and 6 responses."""
    labels = zero.read_R0_definition(
        safe_path(repository, TOPIC + "/notes/actions-43649525432-1-g_first_translation"),
        report)
    all_labels = dict(zip(zero.R0_KEEP, labels))
    selected = {}
    for old, (quadratic, third) in sorted(RESPONSE_LABELS.items()):
        row = all_labels[old]
        require(row["quadratic_name"] == quadratic and row["third_index"] == third,
                "published old R126 label changed: " + str(old))
        selected[old] = row
    _, data = head.bind_input(
        "static",
        safe_path(repository, TOPIC + "/notes/actions-43645177423-1-local_fourth_quotient"),
        report)
    records = data["local_roots"]
    require(Counter(row["mode"] for row in records) == Counter({-4: 197, -2: 197}),
            "the complete published static source coverage changed")
    rows = [row for row in records if row["mode"] == -2]
    states = []
    for row in rows:
        state, jets = head.split_key(row["geometry_key"])
        require(not any(jets), "static source unexpectedly has geometry derivatives")
        states.append(state)
    require(len(set(states)) == 197, "duplicate original static state")
    coordinates, reference = head.constrained.reference_coordinates()
    require(sha(canonical(reference)) == GAMMA_SHA, "the original Gamma reference changed")
    weights = pure.combine_normalization_rows(
        rows, states, coordinates,
        {i: value["state"] for i, value in ORIGINALS.items()},
        head.constrained.BASIS_STATES)
    needed_W = sorted({row["third_index"] for row in selected.values()})
    names = set().union(*(set(row) for row in weights.values()))
    names.update("W" + str(i) for i in needed_W)
    roots = head.subset_decode(ring, data, names)
    del data
    grade = prior.blocks.ScalingGrading(ring)
    static_roots, descriptions = {}, []
    for i, spec in sorted(ORIGINALS.items()):
        raw = sum((amount * roots[name] for name, amount in sorted(weights[i].items())),
                  ring.number(0))
        value = grade.project(raw, 0)
        require(ring.digest(value) == spec["mixed_sha256"],
                "same-Gamma C%d differs from its published R196 root" % i)
        static_roots[i] = value
        descriptions.append({
            "normal_index": i, "state_key_h_k_omega_logh": list(spec["state"]),
            "mode": -2, "true_weight": 0,
            "original_mixed_sha256": ring.digest(value), "terms": len(value.terms),
            "original_raw_static_combination": [[n, str(c)]
                for n, c in sorted(weights[i].items())],
            "raw_combination_sha256": ring.digest(raw),
        })
        budget.check()
    quadratics = exact.operator_basis(ring)
    response_roots, response_records = {}, []
    for old, row in sorted(selected.items()):
        j, a = row["third_index"], row["quadratic_index"]
        require(row["quadratic_name"] == exact.PARAMETERS[a] and
                prior.blocks.THIRD_WEIGHTS[j] + prior.blocks.PARAMETER_WEIGHTS[a] == 0 and
                ring.digest(roots["W" + str(j)]) == row["third_original_sha256"],
                "original W/quadratic identity changed")
        value = prior.mixed_response(
            ring, colored.ThirdOperator(ring, roots["W" + str(j)]), quadratics[a])
        require(ring.digest(value) == row["original_mode_sha256"]["-2"],
                "restored original R126 mixed SHA mismatch at " + str(old))
        response_roots[old] = value
        response_records.append({
            "R126_old_column": old, "quadratic": row["quadratic_name"],
            "W_index": j, "mixed_sha256": ring.digest(value), "terms": len(value.terms)})
        budget.check()
    report["needed_original_input_restore"] = {
        "static_mixed": descriptions, "six_mixed_responses": response_records,
        "Gamma_reference_sha256": GAMMA_SHA,
        "full_original_N0_retained_in_static_roots": True,
        "restoration_reason": "R126 has no portable response DAG; later metadata-only jobs retained no raw roots",
        "other_static_roots_or_responses_restored": 0,
        "pure_roots_restored": 0, "old_forcing_compiled": False,
        "old_pure_self_NF_rank_or_profile_recomputed": False,
    }
    return static_roots, response_roots


def add(out, key, value):
    value = out.get(key, F(0)) + F(value)
    if value:
        out[key] = value
    else:
        out.pop(key, None)


def local_rows(value):
    return [[p, list(jets), str(c)] for (p, jets), c in sorted(value.items())]


def word_rows(value):
    return [[[[p, [[color, order] for color, order in jets]]
              for p, jets in word], str(c)]
            for word, c in sorted(value.items())]


def left_rows(value):
    return [[power, word_rows(words)] for power, words in sorted(value.items()) if words]


def check_local(value, limits, degree):
    for (power, jets), coefficient in value.items():
        require(type(power) is int and power >= 0 and
                tuple(jets) == tuple(sorted(jets)) and len(jets) == degree and
                all(type(j) is int and j >= 0 for j in jets),
                "homogeneous finite local-jet format changed")
        limits.rational(coefficient)
    require(len(value) <= limits.formal.max_terms, "local coordinate term ceiling")
    limits.check()


def euler_five(local, limits):
    """Full fourth-degree Euler polynomial of a homogeneous quintic density.

    This is a NEW degree-five observation; the old quartic self Euler is not run.
    For compact u: 5 int L = int u*Euler(L), with every boundary term paid.
    Nonzero Euler is faithful for a completely LOCAL functional only.
    """
    check_local(local, limits, 5)
    result = {}
    highest = max((max(jets) for p, jets in local), default=-1)
    for order in range(highest + 1):
        term = selfmap.jet_partial(local, order, limits)
        for _ in range(order):
            term = selfmap.derivative(term, limits)
        for key, value in term.items():
            add(result, key, (-1 if order % 2 else 1) * value)
    check_local(result, limits, 4)
    return result


def split_total_left(left, limits, true_weight=None):
    """Preserve every left polynomial and every ordered word.

    Right-integral words I_w are not ordinary unsigned simplex integrals.
    One letter on the left is minus int(letter); longer words retain their
    original signs and order. No nonlocal nonzero claim is inferred from NF.
    """
    for power, words in left.items():
        for word, coefficient in words.items():
            require(sum(len(letter[1]) for letter in word) == 5,
                    "the new total flux is not homogeneous quintic")
            for letter in word:
                require(priority.is_remainder_letter(letter, ("q",)),
                        "new observation is outside the sound fixed-color grammar")
            if true_weight is not None:
                observed = power + sum(p - sum(j for c, j in jets) + 1
                                       for p, jets in word)
                require(observed == true_weight - 2,
                        "the natural total-flux scaling shift changed")
            limits.rational(coefficient)
    leftover_polynomial = any(power != 0 and words for power, words in left.items())
    words = left.get(0, {})
    local, nonlocal_words = {}, {}
    for word, coefficient in sorted(words.items()):
        if len(word) == 1:
            power, jets = word[0]
            require(all(color == "q" for color, order in jets),
                    "the full original diagonal must use one real profile")
            add(local, (power, tuple(order for color, order in jets)), -coefficient)
        else:
            add(nonlocal_words, word, coefficient)
    fully_local = not leftover_polynomial and not nonlocal_words
    euler = euler_five(local, limits) if fully_local else None
    if leftover_polynomial:
        outcome = "unresolved_left_polynomial_word_relations"
    elif nonlocal_words:
        outcome = "unresolved_nonlocal_ordered_remainder"
    elif euler:
        outcome = "universal_functional_nonzero_by_complete_local_Euler"
    else:
        outcome = "universal_functional_zero_by_complete_local_Euler"
    return {
        "left": left, "local": local, "nonlocal": nonlocal_words,
        "euler": euler, "fully_local": fully_local, "outcome": outcome,
    }


class TotalFluxMapper:
    def __init__(self, ring, parameters):
        self.ring = ring
        self.words = priority.PriorityWords(
            ring, max_calls=parameters["max_IBP_calls"],
            max_terms=parameters["max_terms"], max_weight=5,
            max_shuffle_entries=parameters["max_cache_entries"],
            max_cache_entries=parameters["max_cache_entries"], color_order=("q",))

    def expression(self, mixed, true_weight=None, expected_diagonal=None):
        q = self.ring.color("q")
        diagonal = self.ring.substitute(mixed, {"qbar": q})
        require(not (self.ring.color_degrees(diagonal) - { (("q", 4),) }),
                "the complete original mixed diagonal must be quartic")
        diagonal_hash = self.ring.digest(diagonal)
        if expected_diagonal is not None:
            require(diagonal_hash == expected_diagonal,
                    "new diagonal differs from the paid original diagonal")
        # I = integral_right^x, so 4*I(u''' M_-2)|left = -4 int u''' M_-2.
        # All positive-profile right boundaries remain original, including nested I.
        original_primitive = (q.D().D().D() * diagonal).I()
        normal = self.words.expression(original_primitive)
        left = {}
        for (local, word), value in sorted(normal.terms.items()):
            if local[1]:
                continue  # only OUTER compact jets vanish on the left collar
            add(left.setdefault(local[0], {}), word, 4 * value)
        left = {power: words for power, words in left.items() if words}
        result = split_total_left(left, self.ring.limits, true_weight)
        result.update({
            "original_mixed_sha256": self.ring.digest(mixed),
            "original_mixed_terms": len(mixed.terms),
            "global_diagonal_sha256": diagonal_hash,
            "global_diagonal_terms": len(diagonal.terms),
            "new_primitive_sha256": self.ring.digest(original_primitive),
            "whole_new_primitive_word_sha256": priority.digest(priority.rows(normal)),
            "whole_new_primitive_word_terms": len(normal.terms),
            "complete_left_word_sha256": sha(canonical(left_rows(left))),
            "same_right_anchor_preserved": True,
            "outer_zero_restriction_only_after_complete_new_integral": True,
        })
        return result


def public_observation(name, result):
    return {
        "target": name, "outcome": result["outcome"],
        "natural_flux_equals_raw_Omega_by_paid_universal_pure_zero": True,
        "Omega_definition": "-4 integral u''' M_-2(u,u)",
        "true_cost_weight": 0, "observed_functional_weight": -2,
        "original_mixed_sha256": result["original_mixed_sha256"],
        "original_mixed_terms": result["original_mixed_terms"],
        "global_diagonal_sha256": result["global_diagonal_sha256"],
        "global_diagonal_terms": result["global_diagonal_terms"],
        "new_primitive_sha256": result["new_primitive_sha256"],
        "whole_new_primitive_word_sha256": result["whole_new_primitive_word_sha256"],
        "whole_new_primitive_word_terms": result["whole_new_primitive_word_terms"],
        "complete_left_word_sha256": result["complete_left_word_sha256"],
        "complete_left_polynomial_and_ordered_words": left_rows(result["left"]),
        "complete_local_density": local_rows(result["local"]),
        "complete_nonlocal_constant_words": word_rows(result["nonlocal"]),
        "fully_local": result["fully_local"],
        "complete_Euler_polynomial": None if result["euler"] is None
                                      else local_rows(result["euler"]),
        "Euler_sha256": None if result["euler"] is None
                          else sha(canonical(local_rows(result["euler"]))),
        "nonzero_NF_is_not_nonzero_functional": True,
        "right_anchor_changed": False,
        "discarded_old_N0_or_Gamma_or_left_constants": False,
    }


def compare_two_local(first, second, limits):
    """Only the two NEW Euler images: no old-space rank or elimination."""
    if not (first["fully_local"] and second["fully_local"]):
        return {
            "outcome": "unresolved_nonlocal_or_left_polynomial",
            "n2_in_span_n6": None,
            "no_relation_from_sound_NF_nonzero": True,
        }
    left, right = first["euler"], second["euler"]
    if not right:
        return {
            "outcome": "both_universally_zero" if not left
                       else "n6_zero_n2_nonzero",
            "n2_in_span_n6": not left,
            "coefficient_n2_equals_c_n6": "0" if not left else None,
            "exact_Euler_residual": local_rows(left),
            "proportionality_coefficient_unique": False,
        }
    pivot = min(right)
    coefficient = left.get(pivot, F(0)) / right[pivot]
    residual = dict(left)
    for key, value in right.items():
        add(residual, key, -coefficient * value)
    check_local(residual, limits, 4)
    return {
        "outcome": "universal_proportionality" if not residual
                   else "universal_functional_independence",
        "n2_in_span_n6": not residual,
        "coefficient_n2_equals_c_n6": str(coefficient) if not residual else None,
        "pivot_candidate_coefficient": str(coefficient),
        "exact_Euler_residual": local_rows(residual),
        "proportionality_coefficient_unique": True,
        "only_two_new_local_Euler_polynomials_compared": True,
    }


def actual(repository, report):
    started = time.monotonic()
    reader = paid.OriginalJobReader()
    for name in ("Hstar", "J6"):
        bind_paid_target(name, repository, reader, report)
    report["paid_receipt_read_seconds"] = time.monotonic() - started
    budget = literal.Budget(PARAMETERS["max_seconds"], PARAMETERS["memory_mib"],
                            PARAMETERS["integer_bits"])
    limits = exact.Limits(
        seconds=PARAMETERS["max_seconds"], nodes=350000, atoms=100000,
        terms=PARAMETERS["max_terms"], rewrites=PARAMETERS["max_IBP_calls"],
        memory_mib=PARAMETERS["memory_mib"], rational_bits=PARAMETERS["integer_bits"])
    ring = colored.ColoredRing(limits)
    report["phase"] = "necessary_two_static_six_response_input_restore"
    restore_started = time.monotonic()
    roots, responses = restore_needed_roots(ring, repository, budget, report)
    report["necessary_input_restore_seconds"] = time.monotonic() - restore_started
    mapper = TotalFluxMapper(ring, PARAMETERS)
    internal = {}
    report["observations"] = []
    observation_started = time.monotonic()
    for name in ("Hstar", "J6"):
        spec = TARGETS[name]
        mixed = roots[spec["normal_index"]] + sum(
            (amount * responses[j] for j, amount in sorted(spec["response"].items())),
            ring.number(0))
        require(ring.digest(mixed) == spec["mixed_sha256"],
                "fresh input sum differs from paid full original " + name)
        report["phase"] = "new_complete_Omega_" + name
        item = mapper.expression(mixed, true_weight=0,
                                 expected_diagonal=spec["diagonal_sha256"])
        internal[name] = item
        report["observations"].append(public_observation(name, item))
        budget.check()
    report["new_observation_seconds"] = time.monotonic() - observation_started
    report["decision"] = compare_two_local(internal["Hstar"], internal["J6"], limits)
    report["new_mapper_statistics"] = dict(mapper.words.stats)
    report["new_primitive_calls"] = mapper.words.run_primitive_calls
    report["literal_monitor"] = {
        "operations": budget.operations, "maximum_integer_bits": budget.maximum_bits,
        "is_not_the_total_DAG_arithmetic_counter": True}
    report.update(
        completion="complete", phase="two_complete_natural_flux_observations",
        new_total_flux_targets=2, new_profile_evaluations=0,
        new_pure_maps=0, new_self_maps=0, old_Euler_polynomials_recomputed=0,
        old_rank_experiments_repeated=0, old_forcing_recompiled=False,
        old_static_mixed_inputs_restored=2, old_mixed_responses_restored=6,
        other_roots_or_N_projections_restored=0,
        all_original_N0_Gamma_and_history_terms_retained=True,
        universal_Euler_decision_only_when_all_nonlocal_terms_absent=True,
        actual_cost_joint_control_claimed=False, whole_natural_image_solved=False,
        fixed_profile_circle_period_or_gauge_solved=False)


def development():
    """New Omega framing, quintic Euler, and decision-boundary fixtures only."""
    limits = exact.Limits(seconds=30, nodes=15000, atoms=5000, terms=10000,
                          rewrites=20000, memory_mib=256, rational_bits=2048)
    ring = colored.ColoredRing(limits)
    q, x = ring.color("q"), ring.x()
    v, r, t = q.D(), q.D().D(), q.D().D().D()
    p = dict(PARAMETERS, max_IBP_calls=20000, max_terms=10000,
             max_cache_entries=20000)
    records = []

    def case(name, function):
        try:
            detail = function()
            records.append({"name": name, "passed": True, "detail": detail})
        except Exception as error:
            records.append({"name": name, "passed": False,
                            "error": {"type": type(error).__name__, "message": str(error)}})

    def exact_framing():
        toy = {"schema": "invented", "completion": "complete", "value": "new"}
        body = canonical(toy) + b"\n"
        spec = {"schema": "invented", "main": {"bytes": len(body), "sha256": sha(body)}}
        raw = (b"2026-11-15T00:00:00Z COMPLETE_REPORT {\"schema\":\"invented\",\"development\":true}\n"
               b"2026-11-15T00:00:01Z COMPLETE_REPORT " + body)
        found, number = report_from_exact_log(raw, spec)
        assert found == toy and number == 2
        try:
            report_from_exact_log(raw + b"COMPLETE_REPORT " + body, spec)
        except ValueError:
            return "same-schema development skipped; duplicate exact MAIN rejected"
        raise AssertionError("duplicate exact scientific report accepted")

    def quintic_sign():
        item = TotalFluxMapper(ring, p).expression(-q**4/4)
        assert item["fully_local"]
        assert item["local"] == {(0, (0, 0, 1, 1, 1)): F(6)}
        expected = {(0, (0, 1, 1, 1)): F(-24),
                    (0, (0, 0, 1, 2)): F(-36)}
        assert item["euler"] == expected
        return "Omega=int u'''u^4=6 int u^2(u')^3; complete Euler signs retained"

    def nonlocal_retained():
        item = TotalFluxMapper(ring, p).expression(-q*q*(r*r).I()/4)
        assert not item["fully_local"] and item["euler"] is None
        assert item["outcome"] == "unresolved_nonlocal_ordered_remainder"
        assert item["local"] == {(0, (0, 1, 1, 2, 2)): F(1),
                                 (0, (0, 0, 2, 2, 2)): F(-1)}
        first = (0, (("q", 1), ("q", 1), ("q", 1)))
        second = (0, (("q", 2), ("q", 2)))
        assert item["nonlocal"] == {(first, second): F(-1)}
        return "the exact 3+2 ordered word is retained, with its true right-anchor sign"

    def null_euler():
        potential = {(0, (0, 0, 0, 1, 1)): F(1)}
        derivative = selfmap.derivative(potential, limits)
        assert not euler_five(derivative, limits)
        return "full quintic total derivative has zero complete fourth-degree Euler"

    def nonzero_high_jet():
        local = {(0, (0, 0, 0, 3, 3)): F(1)}
        result = euler_five(local, limits)
        assert result[(0, (0, 0, 0, 6))] == F(-2)
        return "sixth derivative coefficient kept in the new complete quintic Euler"

    def same_anchor():
        potential = q**4
        mixed = (potential.D().I()-potential) + (-q**4/4)
        first = TotalFluxMapper(ring, p).expression(mixed)
        second = TotalFluxMapper(ring, p).expression(-q**4/4)
        assert first["left"] == second["left"]
        return "new outer flux retains the paid zero right boundary; no left reset"

    def reject_wrong_weight():
        try:
            TotalFluxMapper(ring, p).expression(-q**4/4, true_weight=1)
        except ValueError as error:
            assert "scaling shift" in str(error)
            return "a false true-weight tag is rejected before any mathematical verdict"
        raise AssertionError("wrong weight was accepted")

    def relations():
        a = {"fully_local": True, "euler": {(0, (0, 1, 1, 1)): F(2)}}
        b = {"fully_local": True, "euler": {(0, (0, 1, 1, 1)): F(1)}}
        assert compare_two_local(a, b, limits)["coefficient_n2_equals_c_n6"] == "2"
        z = {"fully_local": True, "euler": {}}
        assert compare_two_local(a, z, limits)["n2_in_span_n6"] is False
        assert compare_two_local(z, z, limits)["n2_in_span_n6"] is True
        c = {"fully_local": True, "euler": {(1, (0, 0, 1, 1)): F(1)}}
        assert compare_two_local(a, c, limits)["outcome"] == "universal_functional_independence"
        missing = {"fully_local": False, "euler": None}
        assert compare_two_local(a, missing, limits)["n2_in_span_n6"] is None
        return "only complete local Euler permits exact proportionality or separation"

    for name, function in (
        ("exact_paid_main_framing", exact_framing),
        ("outer_flux_sign_and_quintic_Euler", quintic_sign),
        ("ordered_nonlocal_remainder_is_not_discarded", nonlocal_retained),
        ("full_quintic_Euler_null_Lagrangian", null_euler),
        ("new_Euler_highest_jet", nonzero_high_jet),
        ("same_original_right_anchor", same_anchor),
        ("natural_flux_weight_shift", reject_wrong_weight),
        ("new_two_function_relation_boundary", relations),
    ):
        case(name, function)
    return {"checks": records, "count": len(records),
            "all_passed": len(records) == 8 and all(row["passed"] for row in records),
            "scientific_roots_or_old_development_suites_executed": False,
            "network_or_published_payload_opened": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--development", action="store_true",
                        help="only eight NEW Omega interface fixtures")
    args = parser.parse_args()
    if not (os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") == REPOSITORY):
        parser.error("all new development and science run only in public repository Actions")
    repository = Path.cwd().resolve()
    started = time.monotonic()
    report = {
        "schema": SCHEMA, "completion": "started", "phase": "bind_sources",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "inputs": {}, "targets": ["Hstar", "J6"],
        "scope": "two new complete natural total-flux functionals, not an actual joint-control claim",
        "recomputable_payload_publication_permitted": False,
    }
    code = 0
    try:
        _, request_identity, source_files = read_request(args.request, repository)
        report["request_identity"] = request_identity
        report["source_files"] = source_files
        report["source_hashes"] = paid.source_identity()
        report["source_hashes"]["paid_R329_driver"] = report["source_hashes"].pop("driver")
        report["source_hashes"]["driver"] = literal.identity(__file__)
        if args.development:
            report["development"] = development()
            success = report["development"]["all_passed"]
            report.update(completion="complete" if success else "new_development_failed",
                          phase="eight_new_Omega_interfaces_only")
            code = 0 if success else 1
        else:
            actual(repository, report)
    except (literal.Limit, formal.CompilationBudgetExceeded, MemoryError) as error:
        report.update(completion="resource_limit", error=str(error),
                      partial_is_not_a_universal_decision=True)
        code = 2
    except Exception as error:
        report.update(completion="implementation_check_failed",
                      error={"type": type(error).__name__, "message": str(error)})
        code = 1
    report["elapsed_seconds"] = time.monotonic()-started
    report["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report["local_execution_performed"] = False
    body = canonical(report) + b"\n"
    if len(body) > PARAMETERS["max_report_bytes"]:
        report = {
            "schema": SCHEMA, "completion": "complete_formula_output_limit",
            "original_complete_report_bytes": len(body),
            "original_complete_report_sha256": sha(body),
            "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
            "no_universal_decision_claimed_from_truncated_formula": True,
            "recomputable_payload_publication_permitted": False,
        }
        body = canonical(report) + b"\n"
        code = 2
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(body)
    print("COMPLETE_REPORT " + body.decode().rstrip(), flush=True)
    print(canonical({"bytes": len(body), "sha256": sha(body),
                     "payload_publication_permitted": False}).decode(), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
