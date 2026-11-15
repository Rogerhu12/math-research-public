#!/usr/bin/env python3
"""Eight new full hook derivatives of the already proved diagonal-zero lifts.

Consume the published W36 original DAG and R254's exact full chi definitions.
Compute only K_f^chi(w), its actual third x derivative, the complete shared
colored-word representative and, when local, its full formal adjoint.
Do not repeat the old diagonal lifts, references, forcing or fourth responses.
Both new development and research first run only in public repository Actions.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace

import literature_colored_profile_algebra as colored
import literature_color_priority_words as priority
import literature_full_m8_tail_response_projection as reader
import literature_pure_bulk_exact_membership as exact

SCHEMA = "visible-flex-third-kernel-eight-local-operators-v1"
REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = Path(__file__).resolve().parents[1]
COLORS = ("f", "w")
TARGET_INDICES = (30, 32, 34, 37, 40, 100, 104, 109)
W_DIRECTORY = "actions-43645177423-1-local_fourth_quotient"
THIRD_DIRECTORY = "actions-43633746055-1-full_phase_bridge_exact"
W_RUN = "43645177423"
W_COMMIT = "2f1b809c0b0abb7a26303d36940edc203815f872"
W_MAIN_SHA = "19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a"
W_PUBLICATION_SHA = "c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba"
PRIOR_LIFTS = {
    "result": "R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md",
    "run_id": "43707570035",
    "source_commit": "282173404f65d5cc7b1dee61c66c69c3ca17866c",
    "job_id": "132791905419",
    "original_stdout_report_bytes": 29457,
    "original_stdout_report_sha256": "79f3fd82a22a3e24122e14f22c07fab89ebb7572048a22f9f5a8321ad1c5d11e",
    "diagonal_zero_inherited_not_recomputed": True,
}

FROZEN_SOURCES = {
    "literature_c7_transverse_tail_probe.py": [
        11020,
        "98c879d83799e275e145310f5c9fdd9b85a87503d15f1690925d2f648ebc305b"
    ],
    "literature_closed_c1_endpoint.py": [
        21532,
        "b0c9c5a74cdc50935f97fbe1641b705155dbec82e42750393da2a34f38357bd1"
    ],
    "literature_color_priority_words.py": [
        21642,
        "ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9"
    ],
    "literature_colored_profile_algebra.py": [
        15738,
        "c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f"
    ],
    "literature_full_m8_tail_response_projection.py": [
        32096,
        "e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345"
    ],
    "literature_full_phase_bridge_exact.py": [
        35368,
        "d7513321bea70248851e9b71b02c97b7e869531097f290de40257c94507fed0e"
    ],
    "literature_full_phase_rational_dual.py": [
        19492,
        "bcfb26b85918a8648ad98bbde7643c4cf6d01d34b35c53bc06c3dbaff31de84f"
    ],
    "literature_linear_third_bridge_quotient.py": [
        24699,
        "0627875fe06950c9e7c360baaf0429451697a460e2cf10aa6b3434c501363bd2"
    ],
    "literature_local_fourth_quotient.py": [
        38857,
        "9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0"
    ],
    "literature_local_third_bridge_decompose.py": [
        30635,
        "08ada4219df23e50dff2c784c2457dab3c732cd82cacc1477389fdc53fbb6ee0"
    ],
    "literature_pure_bulk_exact_membership.py": [
        33718,
        "f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70"
    ],
    "literature_pure_bulk_word_normal_form.py": [
        32310,
        "d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65"
    ],
    "literature_range_profile_algebra.py": [
        33169,
        "a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52"
    ],
    "literature_rational_volterra_polynomial.py": [
        19803,
        "6bf16dd5c6cc8157fd53b20b58b504a5c3ea56ade9db9b62a30d385e5e69fd22"
    ],
    "literature_total_P1_scaling_blocks.py": [
        37293,
        "40ff170136838907ecb4d2557c2ba3b4d06b5f3fcf63746697f3d5248e92d0fa"
    ]
}

LIFTS = [
    {
        "original_index": 30,
        "tau_sha256": "be8a31110800e396af0d8b2c7d240584f03cd30bcf4e1d1d8f222f2cafc8c199",
        "gamma_sha256": "ff6b5eb5de2c4134a1d1d8f9abaa886e0d822c0a0bb51bc0a2988002c2b4d999",
        "chi_sha256": "e934dba9b2ee51574cdf22bb0eb1efa4f151125d2a6973c934d0b3c6942cf72c",
        "coordinates": [
            [
                2,
                "3/256"
            ],
            [
                20,
                "1/256"
            ]
        ]
    },
    {
        "original_index": 32,
        "tau_sha256": "c8f4568fbddee3985dfd3245aff22592bb065d22dbdc958fc61433ba20279f79",
        "gamma_sha256": "85d617b19b2eb0f7e5c75e5d2144c8003e9283aa58dd1c90f63d83fdde86a613",
        "chi_sha256": "d5eecb73427456b3075a0e93526ea5ffaee15baf902d6e72122a184cff14ee43",
        "coordinates": [
            [
                3,
                "1/128"
            ],
            [
                4,
                "-3/128"
            ],
            [
                8,
                "-1/128"
            ],
            [
                21,
                "-1/512"
            ]
        ]
    },
    {
        "original_index": 34,
        "tau_sha256": "4e76c7b917c4a00138308388d72c40def5837044d287c28242f91d635bf5f312",
        "gamma_sha256": "571d5f3ac02bf3feab995cbe1d4bba51719f84abcfd86bf1457052fee41cf849",
        "chi_sha256": "e9711cae8ea70e3d57672acb6577e016630659235732fbb89697671d8ffdc443",
        "coordinates": [
            [
                3,
                "-1/128"
            ],
            [
                4,
                "-5/128"
            ],
            [
                8,
                "-3/128"
            ],
            [
                21,
                "-3/512"
            ]
        ]
    },
    {
        "original_index": 37,
        "tau_sha256": "94b42fb4261209e6e6e72c078b6e873dfe08dd477672afdcb0156f95051ead28",
        "gamma_sha256": "10a08ed427128e7f5bed6d02d81bd5c221904de457225eea5fbd7a12558be8c8",
        "chi_sha256": "3e262852b4a465df76bc6a3c917fb58bd30f73102b60c3b77daebdc7850a7b8f",
        "coordinates": [
            [
                5,
                "1/32"
            ],
            [
                9,
                "1/32"
            ],
            [
                10,
                "1/16"
            ]
        ]
    },
    {
        "original_index": 40,
        "tau_sha256": "b5155855451e65acb83b0efd8ec51e6467fe343fa80fbeab6c04e1e523c0f368",
        "gamma_sha256": "c81e2b2aa662db6d8b01d8a5ef276c7f724dccd79807f3074f614f1d3eed4751",
        "chi_sha256": "f9cbe1f2435f9aeee4acaed8e8862832c067ea2873ba355d023b0cbf8460c71a",
        "coordinates": [
            [
                11,
                "-1/32"
            ]
        ]
    },
    {
        "original_index": 100,
        "tau_sha256": "8aa68ac3defca7d0d88ec9b5c67dc7b30bedc569129d6fbd8705314fbe331e2d",
        "gamma_sha256": "6b32db600f6da3f71a2906e831e8a0435e14b9346dbf58f9a7960433368bde80",
        "chi_sha256": "cf0662a4a39fd1076db9ba1cdf18ec8842d6399fc3852c01e6fbfea94d262a9c",
        "coordinates": [
            [
                5,
                "-1/8"
            ],
            [
                10,
                "-1/4"
            ],
            [
                24,
                "-1/32"
            ]
        ]
    },
    {
        "original_index": 104,
        "tau_sha256": "578763eecd81ff4e4bf2f3775b253c4315c6c3d58cfb2e3346524b79d8203f0d",
        "gamma_sha256": "1d343bd34fc54d582c213164ff4eaec5587ea4ac7d120723189c884ff9d70f10",
        "chi_sha256": "22becb0a3bbe0dae7becd09f079f476fc923be3178653fc8acd0b09a2facd54d",
        "coordinates": [
            [
                0,
                "3/4"
            ],
            [
                6,
                "1/16"
            ],
            [
                11,
                "3/8"
            ],
            [
                14,
                "-3/16"
            ]
        ]
    },
    {
        "original_index": 109,
        "tau_sha256": "63ec5cb74cb487c52a3e81f1f0b010352f7df57edabb1f08f42dea9093eb52ee",
        "gamma_sha256": "a371b3118f0bfa7d0272e17dc9438915361ed42fd8c71ac7e2ac91f2825cad23",
        "chi_sha256": "6f919eb3aca85cb37f930995c088c67fed52ea44b6e0a48c1e99d1bf4c852aa6",
        "coordinates": [
            [
                12,
                "-1/4"
            ]
        ]
    }
]


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    path = Path(path)
    raw = path.read_bytes()
    return {"filename": path.name, "bytes": len(raw), "sha256": sha(raw)}


def require_public_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("new artificial checks and research run only in the public repository Actions")


def source_inventory():
    """Read only source identities; do not execute any old target."""
    root = Path(__file__).resolve().parent
    for name, expected in FROZEN_SOURCES.items():
        found = identity(root/name)
        if [found["bytes"], found["sha256"]] != expected:
            raise ValueError("frozen original API dependency changed: "+name)
    todo, found = [Path(__file__).resolve()], {}
    while todo:
        path = todo.pop()
        if path.name in found:
            continue
        raw = path.read_bytes()
        found[path.name] = {"bytes": len(raw), "sha256": sha(raw)}
        names = []
        for node in ast.walk(ast.parse(raw, filename=path.name)):
            if isinstance(node, ast.Import):
                names.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                names.append(node.module)
        for name in names:
            if "." not in name and name.startswith("literature_"):
                child = root/(name+".py")
                if not child.is_file():
                    raise ValueError("missing imported source: "+name)
                todo.append(child)
    if set(found)-{Path(__file__).name} != set(FROZEN_SOURCES):
        raise ValueError("recursive original-source closure differs from the declared frozen set")
    return dict(sorted(found.items()))


class MonitoredLimits(exact.Limits):
    """Counter covers rational() calls only, not all original DAG arithmetic."""
    def __init__(self, args):
        super().__init__(seconds=args.max_seconds, nodes=args.max_nodes,
            atoms=args.max_atoms, terms=args.max_terms, rewrites=args.max_word_calls,
            memory_mib=args.max_memory_mib, rational_bits=args.max_rational_bits)
        self.monitored_rational_operations = 0
        self.maximum_monitored_rational_bits = 0
        self.max_monitored_operations = args.max_monitored_rational_operations

    def rational(self, value):
        value = super().rational(value)
        self.monitored_rational_operations += 1
        self.maximum_monitored_rational_bits = max(self.maximum_monitored_rational_bits,
            value.numerator.bit_length(), value.denominator.bit_length())
        if self.monitored_rational_operations > self.max_monitored_operations:
            raise exact.formal.CompilationBudgetExceeded("monitored rational call ceiling")
        self.check()
        return value


def mapper_for(ring, args):
    return priority.PriorityWords(ring, max_calls=args.max_word_calls,
        max_terms=args.max_terms, max_weight=3,
        max_shuffle_entries=args.max_cache_entries,
        max_cache_entries=args.max_cache_entries, color_order=COLORS)


def derivative(value, order):
    if type(order) is not int or order < 0:
        raise ValueError("a nonnegative exact derivative order is required")
    for _ in range(order):
        value = value.D()
    return value


def check_word_grammar(value):
    expected = Counter({"f": 2, "w": 1})
    for (local, word), coefficient in value.terms.items():
        priority.local_key(local, COLORS)
        priority.word_key(word, COLORS)
        degrees = Counter()
        for piece in (local,)+word:
            degrees.update(kind for kind, _ in piece[1])
        if degrees != expected:
            raise AssertionError("the full hook derivative lost f^2 w degree")
        if any(not priority.is_remainder_letter(letter, COLORS) for letter in word):
            raise AssertionError("R179 requires the fixed-color canonical remainder grammar")
        if not coefficient:
            raise AssertionError("a zero coefficient survived in a word row")


def local_profile_monomial(ring, power, jets):
    answer = ring.monomial((power, ()))
    for kind, order in jets:
        answer *= ring.color(kind, order)
    return answer


def describe_operator(ring, value):
    """No word or high jet is removed. Return an operator only if all words are empty."""
    check_word_grammar(value)
    counts = {"empty_word_rows": 0, "rows_with_w_in_a_word": 0,
              "rows_with_only_f_in_words_and_w_outside": 0}
    coefficient_rows = {}
    local = True
    for (outer, word), coefficient in sorted(value.terms.items()):
        if word:
            local = False
            has_internal_w = any(kind == "w" for letter in word for kind, _ in letter[1])
            key = ("rows_with_w_in_a_word" if has_internal_w else
                   "rows_with_only_f_in_words_and_w_outside")
            counts[key] += 1
            continue
        counts["empty_word_rows"] += 1
        w_orders = [order for kind, order in outer[1] if kind == "w"]
        f_orders = [order for kind, order in outer[1] if kind == "f"]
        if len(w_orders) != 1 or len(f_orders) != 2:
            raise AssertionError("a local degree-f^2-w row cannot be extracted")
        coefficient_rows.setdefault(w_orders[0], []).append(
            [outer[0], f_orders, str(coefficient)])
    summary = {
        "all_surviving_words_empty": local,
        "row_kinds": counts,
        "full_word_rows": priority.rows(value),
        "nonlocality_interpretation":
            "R179 canonical word space only; no fixed-seed or fixed-circle assertion",
    }
    if not local:
        summary.update(local_operator_order=None,
            local_operator_coefficients=None, at_most_four=None)
        return summary, None, None
    coefficients = {}
    for order, rows in sorted(coefficient_rows.items()):
        current = ring.number(0)
        for power, f_orders, coefficient in rows:
            current += F(coefficient)*local_profile_monomial(
                ring, power, tuple(("f", j) for j in f_orders))
        coefficients[order] = current
    operator = sum((a*ring.color("w", order) for order, a in sorted(coefficients.items())),
                   ring.number(0))
    maximum = max(coefficients, default=-1)
    summary.update(local_operator_order=maximum, at_most_four=maximum <= 4,
        local_operator_coefficients=[
            {"w_derivative_order": order, "coefficient_monomials": rows,
             "coefficient_format": "[xi_power, two_f_jet_orders, exact_rational]"}
            for order, rows in sorted(coefficient_rows.items())])
    return summary, coefficients, operator


def formal_adjoint(ring, coefficients):
    answer = ring.number(0)
    w = ring.color("w")
    for order, a in sorted(coefficients.items()):
        answer += ((-1)**order)*derivative(a*w, order)
    return answer


def local_expression_rows(ring, expression):
    """Read only literal jets; a primitive here is a concrete implementation error."""
    rows = []
    for (power, atoms), coefficient in sorted(expression.terms.items()):
        jets = []
        for index in atoms:
            atom = ring.p.atoms[index]
            if atom[0] != "jet":
                raise AssertionError("a formal local adjoint introduced a right primitive")
            jets.append([atom[1], atom[2]])
        rows.append([power, sorted(jets), str(coefficient)])
    return rows


def read_original_inputs(args, limits, report):
    publication = args.w_directory/"receipt.json"
    publication_raw = reader.checked_bytes(publication, 40000)
    if len(publication_raw) != 31846 or sha(publication_raw) != W_PUBLICATION_SHA:
        raise ValueError("the original W-only publication receipt changed")
    bindings = SimpleNamespace(
        source_report=args.w_directory/"local-fourth-quotient.json",
        source_report_sha256=W_MAIN_SHA, source_run=W_RUN, source_commit=W_COMMIT,
        publication_receipt=publication,
        templates=args.w_directory/"local-fourth-quotient-W-original-expressions.json.gz",
        third_receipt=args.third_directory/"full-phase-bridge-exact.json")
    raw = reader.checked_bytes(bindings.source_report, 4000)
    if len(raw) != 3982 or sha(raw) != W_MAIN_SHA:
        raise ValueError("the original compact W-only main changed")
    producer = json.loads(raw)
    for item in producer["source_hashes"].values():
        if report["source_hashes"].get(item["filename"]) != {
                "bytes": item["bytes"], "sha256": item["sha256"]}:
            raise ValueError("an original W producer dependency changed: "+item["filename"])
    ring, full = reader.load_templates(bindings, limits, report)
    if tuple(reader.blocks.EXPECTED_KEPT) != tuple(range(28))+TARGET_INDICES or len(full) != 36:
        raise ValueError("the original W36 retained indexing changed")
    expected_degree = (("a", 1), ("b", 1), ("c", 1))
    if any(degree != expected_degree for original in full for degree in ring.color_degrees(original)):
        raise AssertionError("the original exterior and interior third slots changed")
    report["template_input"].update({
        "decoded_original_roots_for_binding": 36,
        "old_reference_diagonals_restored": 0,
        "old_diagonal_lifts_recomputed": 0,
        "old_forcing_or_W_producer_called": False})
    return ring, full


def full_lift(ring, full, position, definition):
    """Exact R254 definition and hashes; no diagonal is substituted or checked."""
    if definition["original_index"] != TARGET_INDICES[position]:
        raise ValueError("the inherited eight-lift order changed")
    tau = full[28+position]
    gamma = ring.number(0)
    for index, coefficient in definition["coordinates"]:
        if type(index) is not int or not 0 <= index < 28:
            raise ValueError("the inherited gamma must use original R71 indices")
        gamma += F(coefficient)*full[index]
    chi = tau-gamma
    for label, expression in (("tau", tau), ("gamma", gamma), ("chi", chi)):
        if ring.digest(expression) != definition[label+"_sha256"]:
            raise ValueError("R254 full original "+label+" hash differs for "+str(definition["original_index"]))
    return chi


def analyze_target(ring, hook, mapper, fresh):
    """One NEW raw D^3 target, one original reconstruction identity, and local adjoint."""
    target = derivative(hook, 3)
    representation = mapper.expression(target)
    check_word_grammar(representation)
    structure, coefficients, local_operator = describe_operator(ring, representation)
    original_representative = mapper.to_old(representation)
    if local_operator is not None and local_operator.key() != original_representative.key():
        raise AssertionError("grouped local coefficients do not reconstruct the complete empty-word sum")
    original_difference = target-original_representative
    fresh_difference = fresh.expression(original_difference)
    check_word_grammar(fresh_difference)
    if fresh_difference.terms:
        raise AssertionError("the fresh complete original D^3 difference is not zero")
    result = {
        "K_full_original_sha256": ring.digest(hook),
        "K_full_raw_terms": len(hook.terms),
        "D3K_full_original_sha256": ring.digest(target),
        "D3K_full_raw_terms": len(target.terms),
        "D3K_complete_word": mapper.summary(representation),
        "all_original_slots_and_common_right_anchor_retained": True,
        "original_reconstruction_difference_sha256": ring.digest(original_difference),
        "original_reconstruction_difference_raw_terms": len(original_difference.terms),
        "fresh_original_reconstruction_word": fresh.summary(fresh_difference),
        "fresh_original_reconstruction_zero": True,
        **structure,
    }
    if coefficients is not None:
        adjoint = formal_adjoint(ring, coefficients)
        difference = adjoint-local_operator
        rows = local_expression_rows(ring, difference)
        result.update(
            local_operator_original_sha256=ring.digest(local_operator),
            formal_adjoint_original_sha256=ring.digest(adjoint),
            formal_adjoint_difference_sha256=ring.digest(difference),
            formal_adjoint_difference_rows=rows,
            formally_self_adjoint=not rows,
            annihilates_seed_by_prior_R254_diagonal_identity=True,
            seed_annihilation_target_recomputed=False)
    else:
        result.update(formally_self_adjoint=None,
            formal_adjoint_not_tested_for_a_nonlocal_word_expression=True)
    proof = {
        "full_word_rows": priority.rows(representation),
        "original_reconstruction_difference_sha256": ring.digest(original_difference),
        "fresh_original_difference_rows": priority.rows(fresh_difference),
        "local_adjoint_difference_rows": result.get("formal_adjoint_difference_rows"),
    }
    return result, proof


def research(args, report):
    limits = MonitoredLimits(args)
    report["phase"] = "bind_published_W36_and_prior_full_lifts"
    ring, full = read_original_inputs(args, limits, report)
    mapper, fresh = mapper_for(ring, args), mapper_for(ring, args)
    f, w = ring.color("f"), ring.color("w")
    report["inherited_lifts"] = dict(PRIOR_LIFTS)
    report["results"] = []
    proof = {"schema": SCHEMA+"-in-memory-new-D3-proof",
             "right_integral": "I(F)=integral_right_endpoint^xi F; D I=identity",
             "color_order": list(COLORS), "targets": []}
    emitted = 0
    report["phase"] = "eight_new_complete_hook_third_derivatives"
    for position, definition in enumerate(LIFTS):
        limits.formal.time_check()
        chi = full_lift(ring, full, position, definition)
        hook = ring.substitute(chi, {"a": w, "b": f, "c": f})
        result, evidence = analyze_target(ring, hook, mapper, fresh)
        record = {
            "original_index": definition["original_index"],
            "retained_W_position": 28+position,
            "full_original_lift_definition": definition,
            "full_chi_raw_terms": len(chi.terms),
            **result}
        line = canonical(record)
        if emitted+len(line) > args.max_mathematical_stdout_bytes:
            raise exact.formal.CompilationBudgetExceeded(
                "complete new mathematical row output ceiling; target is not reported complete")
        print("EIGHT_KERNEL_OPERATOR "+line.decode(), flush=True)
        emitted += len(line)
        # Whole new word/adjoint rows already appear verbatim above. Keep the
        # temporary main compact without losing any mathematical evidence.
        brief = {key: value for key, value in record.items() if key not in
                 ("full_word_rows", "formal_adjoint_difference_rows")}
        brief["complete_word_rows_printed_in_EIGHT_KERNEL_OPERATOR"] = True
        brief["formal_adjoint_difference_row_count"] = (
            len(record["formal_adjoint_difference_rows"])
            if record.get("formal_adjoint_difference_rows") is not None else None)
        report["results"].append(brief)
        proof["targets"].append({"original_index": definition["original_index"], **evidence})
        limits.formal.time_check()
    raw_proof = canonical(proof)
    if len(raw_proof) > args.max_proof_bytes:
        raise exact.formal.CompilationBudgetExceeded("in-memory proof byte ceiling")
    report["in_memory_proof"] = {
        "bytes": len(raw_proof), "sha256": sha(raw_proof),
        "written_to_repository_release_or_artifact": False,
        "complete_new_maths_already_printed": True,
        "reconstruction": "same published W36 originals plus frozen R254 coordinates and this source"}
    report["word_maps"] = {
        "complete_new_D3_targets": dict(mapper.stats),
        "fresh_complete_original_reconstruction_differences": dict(fresh.stats),
        "first_map_new_primitive_calls": mapper.run_primitive_calls,
        "fresh_map_new_primitive_calls": fresh.run_primitive_calls,
        "all_surviving_letters_checked_against_R179": True,
        "cycle_fallbacks_used": False}
    report["monitored_cost"] = {
        "rational_calls": limits.monitored_rational_operations,
        "maximum_bits_at_monitored_rational_calls": limits.maximum_monitored_rational_bits,
        "scope": "MonitoredLimits.rational calls only, not all original DAG arithmetic",
        "profile_atoms_including_read_originals": len(ring.p.atoms),
        "complete_mathematical_row_stdout_bytes": emitted}
    local = [r["original_index"] for r in report["results"] if r["all_surviving_words_empty"]]
    selfadjoint = [r["original_index"] for r in report["results"] if r.get("formally_self_adjoint")]
    four = [r["original_index"] for r in report["results"] if r.get("at_most_four")]
    report["mathematical_result"] = {
        "completed_full_hook_D3_targets": len(report["results"]),
        "all_eight_complete_original_reconstruction_identities_zero": True,
        "local_polynomial_operator_indices": local,
        "local_formally_self_adjoint_operator_indices": selfadjoint,
        "local_operator_order_at_most_four_indices": four,
        "all_eight_local_self_adjoint_order_at_most_four":
            len(local) == len(selfadjoint) == len(four) == 8,
        "true_right_three_constants": "all K,K',K'' vanish on the common input zero right collar",
        "exact_reconstruction": "K=-positive_right_integral^3(D^3K), including the complete left tails",
        "diagonal_zero_and_seed_annihilation_inherited_from_R254": True,
        "old_diagonal_or_reference_targets_repeated": 0,
        "new_fourth_responses_evaluated": 0,
        "profile_or_geometry_values_evaluated": 0,
        "fixed_circle_period_rank_or_surjectivity_claimed": False,
        "all_fourth_pure_zero_response_branches_exhausted": False,
        "actual_signed_cost_or_joint_ruling_solution_claimed": False}
    report["phase"], report["completion"] = "complete", "complete"


def artificial_checks(args):
    """Eight invented cases for the new operator/word/adjoint adapter only."""
    limits = MonitoredLimits(args)
    ring = colored.ColoredRing(limits)
    mapper, fresh = mapper_for(ring, args), mapper_for(ring, args)
    f, w, x = ring.color("f"), ring.color("w"), ring.x()
    checks = {}

    local = x*f*f*derivative(w, 1)+f.D()*f.D()*derivative(w, 4)
    description, coefficients, rebuilt = describe_operator(ring, mapper.expression(local))
    assert description["all_surviving_words_empty"] and description["local_operator_order"] == 4
    assert set(coefficients) == {1, 4} and rebuilt.key() == local.key()
    checks["complete_local_w_jet_grouping_reconstructs_both_coefficient_orders"] = True

    description, coefficients, rebuilt = describe_operator(ring, mapper.expression((f*f*w).I()))
    assert not description["all_surviving_words_empty"] and coefficients is None and rebuilt is None
    assert description["row_kinds"]["rows_with_w_in_a_word"] == 1
    checks["a_true_internal_w_primitive_is_not_labelled_a_local_operator"] = True

    description, _, _ = describe_operator(ring, mapper.expression(w*(f*f).I()))
    assert not description["all_surviving_words_empty"]
    assert description["row_kinds"]["rows_with_only_f_in_words_and_w_outside"] == 1
    assert description["row_kinds"]["rows_with_w_in_a_word"] == 0
    checks["an_external_w_times_a_true_f_tail_is_distinguished_from_an_internal_w_tail"] = True

    symmetric = derivative(f*f*derivative(w, 2), 2)+derivative(f.D()*f.D()*w.D(), 1)
    description, coefficients, rebuilt = describe_operator(ring, mapper.expression(symmetric))
    assert description["local_operator_order"] == 4
    assert not (formal_adjoint(ring, coefficients)-rebuilt).terms
    checks["the_complete_coefficient_chain_rule_preserves_an_invented_self_adjoint_fourth_order_form"] = True

    asymmetric = f*f*w.D()
    _, coefficients, rebuilt = describe_operator(ring, mapper.expression(asymmetric))
    assert local_expression_rows(ring, formal_adjoint(ring, coefficients)-rebuilt)
    checks["a_non_self_adjoint_local_form_keeps_its_nonzero_exact_adjoint_difference"] = True

    hook = symmetric.I().I().I()
    assert derivative(hook, 3).key() == symmetric.key()
    analyzed, _ = analyze_target(ring, hook, mapper, fresh)
    assert analyzed["fresh_original_reconstruction_zero"] and analyzed["formally_self_adjoint"]
    checks["three_original_signed_right_integrals_have_the_correct_positive_third_derivative"] = True

    original = w*(f*f.D()).I()
    expected = w*f*f/2
    normalized = mapper.expression(original)
    assert mapper.to_old(normalized).key() == expected.key()
    assert not fresh.expression(original-expected).terms
    checks["a_new_original_same_anchor_IBP_difference_is_checked_after_full_reconstruction"] = True

    higher = f*f*derivative(w, 6)
    description, _, rebuilt = describe_operator(ring, mapper.expression(higher))
    assert description["all_surviving_words_empty"] and description["local_operator_order"] == 6
    assert description["at_most_four"] is False and rebuilt.key() == higher.key()
    checks["a_real_sixth_order_local_target_is_reported_without_a_fourth_order_truncation"] = True

    return {"all_passed": all(checks.values()), "checks": checks,
            "artificial_only": True, "real_input_files_opened": False,
            "old_diagonal_reference_or_fourth_response_targets_repeated": False}


def parse_args(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--w-directory", type=Path, default=TOPIC/"notes"/W_DIRECTORY)
    p.add_argument("--third-directory", type=Path, default=TOPIC/"notes"/THIRD_DIRECTORY)
    p.add_argument("--toy-only", action="store_true")
    p.add_argument("--output", type=Path, required=True,
                   help="runner-temporary main only; no data/certificate/artifact publication")
    p.add_argument("--max-seconds", type=float, default=120)
    p.add_argument("--max-memory-mib", type=int, default=512)
    p.add_argument("--max-nodes", type=int, default=300000)
    p.add_argument("--max-atoms", type=int, default=40000)
    p.add_argument("--max-terms", type=int, default=40000)
    p.add_argument("--max-word-calls", type=int, default=150000)
    p.add_argument("--max-cache-entries", type=int, default=150000)
    p.add_argument("--max-rational-bits", type=int, default=8192)
    p.add_argument("--max-monitored-rational-operations", type=int, default=1000000)
    p.add_argument("--max-proof-bytes", type=int, default=8000000)
    p.add_argument("--max-summary-bytes", type=int, default=95000)
    p.add_argument("--max-mathematical-stdout-bytes", type=int, default=1000000)
    args = p.parse_args(argv)
    for key, value in vars(args).items():
        if key.startswith("max_") and value <= 0:
            p.error(key+" must be positive")
    return args


def emit_report(args, report):
    raw = canonical(report)+b"\n"
    if len(raw) > args.max_summary_bytes:
        report = {
            "schema": SCHEMA, "completion": "output_limit", "phase": report.get("phase"),
            "github_repository": report.get("github_repository"),
            "github_run_id": report.get("github_run_id"), "github_sha": report.get("github_sha"),
            "driver": report.get("driver"), "source_hashes": report.get("source_hashes"),
            "complete_report_bytes": len(raw), "complete_report_sha256": sha(raw),
            "mathematical_result": report.get("mathematical_result"),
            "completed_target_count": len(report.get("results", [])),
            "completed_target_full_rows_already_printed": True,
            "elapsed_seconds": report.get("elapsed_seconds"),
            "peak_resident_mib_linux": report.get("peak_resident_mib_linux"),
            "error": "temporary main exceeds its byte ceiling; use complete emitted target rows",
            "unfinished_targets_are_not_zero": True, "task_complete": False}
        raw = canonical(report)+b"\n"
        if len(raw) > args.max_summary_bytes:
            raise ValueError("summary byte ceiling cannot contain the minimal failure receipt")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(raw)
    print("MATHEMATICAL_RESULT "+json.dumps(report.get("mathematical_result", {
        "completion": report.get("completion"), "phase": report.get("phase"),
        "development": report.get("development"), "error": report.get("error")}),
        sort_keys=True, separators=(",", ":")), flush=True)
    print("COMPLETE_REPORT "+raw.decode().rstrip(), flush=True)
    print("TEMPORARY_MAIN "+json.dumps({"filename": args.output.name,
        "bytes": len(raw), "sha256": sha(raw), "payload_to_be_published": False},
        sort_keys=True, separators=(",", ":")), flush=True)
    return report.get("completion")


def main(argv=None):
    args = parse_args(argv)
    started = time.monotonic()
    report = {
        "schema": SCHEMA, "completion": "started", "phase": "public_gate",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "driver": identity(__file__),
        "parameters": {key: str(value) if isinstance(value, Path) else value
                       for key, value in vars(args).items()},
        "metadata_only": True, "task_complete": False,
        "new_scientific_work": "eight new complete hook third derivatives; zero old diagonal or fourth targets",
        "scope": "universal same-right-anchor functions, not a fixed-circle range or signed cost"}
    try:
        require_public_actions()
        report["source_hashes"] = source_inventory()
        if args.toy_only:
            report["phase"] = "eight_new_artificial_operator_adapter_checks"
            report["development"] = artificial_checks(args)
            if not report["development"]["all_passed"]:
                raise AssertionError("a new artificial operator-adapter check failed")
            report["phase"], report["completion"] = "complete", "complete"
        else:
            research(args, report)
    except exact.formal.CompilationBudgetExceeded as error:
        report.update(completion="resource_limit", error_type=type(error).__name__,
                      error=str(error), unfinished_targets_are_not_zero=True)
    except Exception as error:
        report.update(completion="implementation_check_failed", error_type=type(error).__name__,
                      error=str(error), unfinished_targets_are_not_zero=True)
    report["elapsed_seconds"] = time.monotonic()-started
    report["peak_resident_mib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    status = emit_report(args, report)
    return 0 if status == "complete" else 2


if __name__ == "__main__":
    sys.exit(main())

