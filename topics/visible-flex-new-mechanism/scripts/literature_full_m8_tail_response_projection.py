#!/usr/bin/env python3
"""Consume public W36 expressions and project all genuine R8 directions.

Only the pure -4 response on q=(c-xi)^8 is evaluated. No old forcing,
third basis, P1 target, or old finite-node query is recompiled. The one
already published R110 column is consumed byte-for-byte. Actual research
runs exclusively in this public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import resource
import time

import literature_c7_transverse_tail_probe as tail
import literature_colored_profile_algebra as colored
import literature_full_phase_rational_dual as dual
import literature_local_fourth_quotient as local4
import literature_pure_bulk_exact_membership as exact
import literature_total_P1_scaling_blocks as blocks

SCHEMA = "visible-flex-full-m8-pure-tail-R8-projection-v1"
REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = Path(__file__).resolve().parents[1]
PARAMETER_NAMES = ("p0", "p1", "p2", "r0", "r1", "s0", "s1", "t1")
ADAPTER_SHA = "98c879d83799e275e145310f5c9fdd9b85a87503d15f1690925d2f648ebc305b"
PROBE_SHA = "c6c2c4c886dc5f115569ab4dd36176530efcf80ed12bb83b3d19223a7a279746"
PROBE_BYTES = 2179
PROBE_POLYNOMIAL_SHA = "e37a582bd52a0a7028e2794cd0d6084f050dc4a65b5905d949c00e9dcecdf850"
DEFAULT_PROBE = TOPIC/"notes/actions-43643100132-1-c7_transverse_tail_probe/c7-transverse-tail-probe.json"
MAX_RAW_BYTES = 32000000
MAX_FILE_BYTES = 4800000


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    raw = Path(path).read_bytes()
    return {"filename": Path(path).name, "bytes": len(raw), "sha256": sha(raw)}


def dependencies():
    result = local4.dependencies()
    result["portable_expression_producer"] = result.pop("driver")
    adapter = identity(tail.__file__)
    if adapter["sha256"] != ADAPTER_SHA:
        raise ValueError("explicitly rebind the already published exact c,r adapter")
    result["c_r_adapter"] = adapter
    result["driver"] = identity(__file__)
    return result


def checked_bytes(path, maximum):
    raw = Path(path).read_bytes()
    if len(raw) > maximum:
        raise ValueError("declared input/output byte bound")
    return raw


def write_json(path, value):
    raw = canonical(value)+b"\n"
    if len(raw) > MAX_FILE_BYTES:
        raise ValueError("complete JSON file exceeds declared byte bound")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    temporary.write_bytes(raw)
    temporary.replace(path)
    return {"filename": path.name, "bytes": len(raw), "sha256": sha(raw)}


def write_certificate(path, value):
    raw = canonical(value)
    if len(raw) > MAX_RAW_BYTES:
        raise ValueError("complete certificate raw byte bound")
    packed = gzip.compress(raw, mtime=0)
    if len(packed) > MAX_FILE_BYTES:
        raise ValueError("complete certificate packed byte bound")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(packed)
    return {"filename": path.name, "stored_bytes": len(packed),
            "stored_sha256": sha(packed), "raw_bytes": len(raw), "raw_sha256": sha(raw)}


def polynomial_key(value):
    return tuple((a, b, coefficient.numerator, coefficient.denominator)
                 for (a, b), coefficient in sorted(value.terms.items()))


def power(value, exponent):
    if type(exponent) is not int or exponent < 0:
        raise ValueError("nonnegative coordinate powers only")
    out, base = value.ring.number(1), value
    while exponent:
        if exponent & 1:
            out = out*base
        exponent >>= 1
        if exponent:
            base = base*base
    return out


class TailRing(tail.Ring):
    """Reuse the unchanged published Fraction arithmetic, with total guards."""
    def __init__(self, seconds, memory_mib=1024, max_operations=10000000):
        self.memory_mib, self.max_operations = memory_mib, max_operations
        self.linear_operations = 0
        self.raw_atoms_evaluated = self.raw_monomials_evaluated = 0
        super().__init__(seconds=seconds, max_terms=5000, max_degree=80, max_bits=8192)

    def check(self, value):
        super().check(value)
        if self.operations > self.max_operations:
            raise RuntimeError("declared polynomial operation budget")
        if self.operations % 128 == 0:
            self.guard()

    def guard(self):
        if time.monotonic()-self.started > self.seconds:
            raise RuntimeError("declared total projection time budget")
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > self.memory_mib*1024:
            raise RuntimeError("declared projection resident-memory budget")

    def scalar_guard(self, value):
        self.linear_operations += 1
        if max(value.numerator.bit_length(), value.denominator.bit_length()) > self.max_bits:
            raise RuntimeError("declared exact-linear-algebra rational bit budget")
        if self.linear_operations > self.max_operations:
            raise RuntimeError("declared exact-linear-algebra operation budget")
        if self.linear_operations % 128 == 0:
            self.guard()

    def number(self, value):
        return tail.Polynomial(self, {(0, 0): F(value)})


class OriginalTailEvaluator:
    """Evaluate the portable original colored DAG, with no word rewriting.

    The source primitive is I=int_c^xi, whereas the published adapter J
    is int_xi^c. Therefore an original int_right atom is exactly -J.
    """
    def __init__(self, profile_algebra, ring, replacements):
        self.profile_algebra, self.ring = profile_algebra, ring
        self.replacements = replacements
        self.atoms, self.monomials, self.jets = {}, {}, {}
        self.powers = {0: ring.number(1), 1: ring.x()}

    def atom(self, identifier):
        if identifier not in self.atoms:
            node = self.profile_algebra.atoms[identifier]
            if node[0] == "jet":
                name, order = node[1], node[2]
                if name not in self.replacements:
                    raise ValueError("unbound actual colored slot")
                values = self.jets.setdefault(name, [self.replacements[name]])
                while len(values) <= order:
                    values.append(values[-1].D())
                answer = values[order]
            elif node[0] == "int_right":
                answer = -self.monomial(node[1]).J()
            else:
                raise ValueError("unsupported original atom")
            self.atoms[identifier] = answer
            self.ring.raw_atoms_evaluated += 1
        return self.atoms[identifier]

    def monomial(self, value):
        if value not in self.monomials:
            degree, atoms = value
            if degree not in self.powers:
                self.powers[degree] = power(self.ring.x(), degree)
            answer = self.powers[degree]
            for atom in atoms:
                answer = answer*self.atom(atom)
            self.monomials[value] = answer
            self.ring.raw_monomials_evaluated += 1
        return self.monomials[value]

    def expression(self, expression):
        answer = self.ring.number(0)
        for monomial, coefficient in expression.terms.items():
            answer += coefficient*self.monomial(monomial)
        return answer


class OriginalTailThird:
    def __init__(self, profile_algebra, ring, template):
        self.profile_algebra, self.ring, self.template = profile_algebra, ring, template
        self.cache = {}

    def __call__(self, exterior, first, second):
        # Keep the actual exterior/inner ordering. No new symmetry is assumed.
        key = tuple(polynomial_key(x) for x in (exterior, first, second))
        if key not in self.cache:
            evaluator = OriginalTailEvaluator(self.profile_algebra, self.ring,
                {"a": exterior, "b": first, "c": second})
            self.cache[key] = evaluator.expression(self.template)
        return self.cache[key]


class CachedQuadratic:
    def __init__(self, operation):
        self.operation, self.cache = operation, {}

    def __call__(self, left, right):
        key = (polynomial_key(left), polynomial_key(right))
        if key not in self.cache:
            self.cache[key] = self.operation(left, right)
        return self.cache[key]


def add_sparse(target, source, coefficient, ring):
    for monomial, value in source.items():
        result = target.get(monomial, F(0))+coefficient*value
        ring.scalar_guard(result)
        if result:
            target[monomial] = result
        else:
            target.pop(monomial, None)


class ExactProjectedSpan:
    """Exact Q-column elimination of complete finite polynomials only."""
    def __init__(self, ring):
        self.ring = ring
        self.basis, self.original = {}, {}
        self.independent, self.dependencies, self.pivot_records = [], [], []

    def add(self, index, column):
        self.original[index] = dict(column)
        value, representation = dict(column), {index: F(1)}
        for pivot in sorted(self.basis):
            coefficient = value.get(pivot, F(0))
            if coefficient:
                row, combination = self.basis[pivot]
                add_sparse(value, row, -coefficient, self.ring)
                add_sparse(representation, combination, -coefficient, self.ring)
        if value:
            pivot = min(value)
            leading = value[pivot]
            row = {m: v/leading for m, v in value.items()}
            combination = {j: v/leading for j, v in representation.items()}
            for v in (*row.values(), *combination.values()):
                self.ring.scalar_guard(v)
            self.basis[pivot] = (row, combination)
            self.independent.append(index)
            self.pivot_records.append({"column": index, "pivot": list(pivot),
                                       "pre_normalization_leading_value": str(leading)})
            return
        own = representation.get(index, F(0))
        if not own:
            raise AssertionError("new-column dependency lost its own coefficient")
        combination = {j: -v/own for j, v in representation.items() if j != index and v}
        check = dict(column)
        for j, coefficient in combination.items():
            add_sparse(check, self.original[j], -coefficient, self.ring)
        if check:
            raise AssertionError("exact complete-polynomial dependency failed")
        self.dependencies.append({"column": index,
            "basis_combination": [[j, str(v)] for j, v in sorted(combination.items())],
            "complete_polynomial_difference_zero": True})

    def summary(self):
        return {"exact_rank_over_Q": len(self.independent),
            "independent_original_columns": self.independent,
            "pivot_records": self.pivot_records,
            "verified_complete_polynomial_dependencies": self.dependencies,
            "scope": "this complete m8 pure right-tail polynomial projection only",
            "full_operator_dependencies_asserted": False}


def four_block_projection(value):
    # R106: 2(V(c,r)+V(-c,-r)).
    return {key: 4*coefficient for key, coefficient in value.items() if sum(key) % 2 == 0}


def read_probe(path, ring):
    raw = checked_bytes(path, MAX_FILE_BYTES)
    if len(raw) != PROBE_BYTES or sha(raw) != PROBE_SHA:
        raise ValueError("preserve the published R110 actual report byte-for-byte")
    report = json.loads(raw)
    rows = report["complete_minus_four_polynomial"]
    if (report.get("completion") != "complete"
            or report.get("direction") != "B_P(tau_Q,P), P=Phi_t1, Q=Phi_p1"
            or sha(canonical(rows)) != PROBE_POLYNOMIAL_SHA
            or report.get("source_hashes", {}).get("literature_c7_transverse_tail_probe.py", {}).get("sha256") != ADAPTER_SHA):
        raise ValueError("R110 complete polynomial identity mismatch")
    output = tail.Polynomial(ring, {(x["c_power"], x["r_power"]): F(x["coefficient"]) for x in rows})
    return output, {"report_bytes": len(raw), "report_sha256": sha(raw),
        "complete_polynomial_sha256": sha(canonical(rows)),
        "source_run": "43643100132", "source_commit": "8efadbda14ed483c3393227d62bed4d3dea89087",
        "quadratic_index": 7, "third_index": 12, "old_direction_recomputed": False}



def verify_publication_binding(publication, *, source_run, source_commit,
                               report_name, report_bytes, report_sha,
                               export_record, driver_identity):
    """Use the real terminal-publisher manifest when a compact main lost fields."""
    if (publication.get("schema") != "visible-new-mechanism-actions-v1"
            or publication.get("repository") != REPOSITORY
            or str(publication.get("run_id")) != source_run
            or publication.get("source_commit") != source_commit
            or publication.get("lane") != "local_fourth_quotient"):
        raise ValueError("public terminal receipt source/run/repository/lane mismatch")
    driver = publication.get("source_files", {}).get(
        "topics/visible-flex-new-mechanism/scripts/literature_local_fourth_quotient.py")
    if driver != {"bytes": driver_identity["bytes"], "sha256": driver_identity["sha256"]}:
        raise ValueError("public receipt does not bind the actual producer source")
    def one_output(name):
        rows = [row for row in publication.get("outputs", []) if row.get("path") == name]
        if len(rows) != 1:
            raise ValueError("one exact published output entry is required")
        return rows[0]
    main = one_output(report_name)
    if (main.get("bytes"), main.get("sha256"), main.get("raw_bytes"), main.get("raw_sha256")) != (
            report_bytes, report_sha, report_bytes, report_sha):
        raise ValueError("public receipt does not bind the compact producer report bytes")
    exported = one_output(export_record["filename"])
    if (exported.get("bytes"), exported.get("sha256"), exported.get("raw_bytes"), exported.get("raw_sha256")) != (
            export_record["stored_bytes"], export_record["stored_sha256"],
            export_record["raw_bytes"], export_record["raw_sha256"]):
        raise ValueError("public receipt and producer report disagree on the complete W export")
    return {"source_run": source_run, "source_commit": source_commit,
            "matched_output_paths": [report_name, export_record["filename"]],
            "producer_source_identity": driver}


def load_templates(args, limits, report):
    raw_report = checked_bytes(args.source_report, MAX_FILE_BYTES)
    if sha(raw_report) != args.source_report_sha256:
        raise ValueError("explicit published producer report hash mismatch")
    source_report = json.loads(raw_report)
    if source_report.get("schema") != local4.SCHEMA:
        raise ValueError("producer report schema mismatch")
    if source_report["source_hashes"]["driver"] != identity(local4.__file__):
        raise ValueError("portable producer source changed; rebind explicitly")
    metadata = source_report.get("portable_W_expression_export")
    if metadata is None:
        metadata = source_report.get("portable_original_expression_export")
    if not metadata:
        raise ValueError("a completed original W export is required")
    publication_binding = None
    if args.publication_receipt:
        publication_raw = checked_bytes(args.publication_receipt, MAX_FILE_BYTES)
        publication = json.loads(publication_raw)
        publication_binding = verify_publication_binding(publication,
            source_run=args.source_run, source_commit=args.source_commit,
            report_name=args.source_report.name, report_bytes=len(raw_report),
            report_sha=sha(raw_report), export_record=metadata,
            driver_identity=source_report["source_hashes"]["driver"])
        publication_binding.update(filename=args.publication_receipt.name,
            bytes=len(publication_raw), sha256=sha(publication_raw))
    observed_run = source_report.get("github_run_id")
    observed_source = source_report.get("github_sha")
    if observed_run is None and observed_source is None:
        if publication_binding is None:
            raise ValueError("compact producer report needs its real public publication receipt")
        observed_run = publication_binding["source_run"]
        observed_source = publication_binding["source_commit"]
    if str(observed_run) != args.source_run or observed_source != args.source_commit:
        raise ValueError("producer report source/run binding mismatch")
    packed = checked_bytes(args.templates, MAX_FILE_BYTES)
    if len(packed) != metadata["stored_bytes"] or sha(packed) != metadata["stored_sha256"]:
        raise ValueError("public original-expression export bytes changed")
    with gzip.GzipFile(fileobj=io.BytesIO(packed)) as stream:
        raw = stream.read(MAX_RAW_BYTES+1)
    if (len(raw) > MAX_RAW_BYTES or len(raw) != metadata["raw_bytes"]
            or sha(raw) != metadata["raw_sha256"]):
        raise ValueError("public uncompressed expression binding mismatch")
    data = json.loads(raw)
    if data.get("schema") != local4.SCHEMA+"-original-expressions":
        raise ValueError("portable original-expression schema mismatch")
    if data.get("content_scope") == "W-only" and set(data["roots"]) != {"W"+str(j) for j in range(36)}:
        raise ValueError("W-only export must contain exactly the 36 original roots")
    if data.get("source_hashes") != source_report["source_hashes"]:
        raise ValueError("producer report and exported DAG disagree on sources")
    receipt = dual.read_receipt(args.third_receipt)
    ring = colored.ColoredRing(limits)
    roots = local4.decode_expressions(ring, data)
    templates = [roots["W"+str(j)] for j in range(36)]
    binding = data["bound_W"]
    if (binding["receipt_sha256"] != dual.RECEIPT_SHA
            or binding["retained_original_indices"] != blocks.EXPECTED_KEPT):
        raise ValueError("the actual complete W36 basis changed")
    wanted = [x["original_third_sha256"] for x in receipt["control_templates"]]
    got = [ring.digest(x) for x in templates]
    if len(wanted) != 36 or got != wanted or got != binding["raw_template_hashes"]:
        raise ValueError("portable roots do not equal the published original W36")
    if got[12] != "a36765c31af4d4583535ced0ac473d79f8c2a48081a45db7bede1002f7a15d76":
        raise ValueError("the reused R110 column requires the same original tau_p1_t1 root")
    for template in templates:
        if any(ring.p.weight(m) != 3 for m in template.terms):
            raise AssertionError("original third profile degree")
    report["template_input"] = {"producer_run": args.source_run,
        "producer_commit": args.source_commit, "producer_report_sha256": sha(raw_report),
        "producer_completion": source_report.get("completion"),
        "public_terminal_receipt_binding": publication_binding,
        "portable_export": metadata, "content_scope": data.get("content_scope", "W-and-local-target"),
        "used_roots": ["W"+str(j) for j in range(36)],
        "bound_W": binding, "original_36_root_hashes_matched": True,
        "old_116_dependencies_recomputed": False,
        "old_third_or_fourth_forcing_recompiled": False,
        "local_density_roots_consumed": False}
    return ring, templates


def actual(args, report):
    if (os.environ.get("GITHUB_ACTIONS", "").lower() != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("actual projection is restricted to this public repository Actions")
    if not all((args.templates, args.source_report, args.source_report_sha256,
                args.source_run, args.source_commit)):
        raise ValueError("actual mode needs a byte/source-bound published W export")
    started = time.monotonic()
    limits = exact.Limits(seconds=args.max_seconds, nodes=300000, atoms=60000,
                          terms=80000, rewrites=1000, memory_mib=args.memory_mib)
    source_ring, templates = load_templates(args, limits, report)
    remaining = args.max_seconds-(time.monotonic()-started)
    if remaining <= 0:
        raise RuntimeError("input restoration used the declared time bound")
    ring = TailRing(remaining, args.memory_mib, args.max_operations)
    old_column, old_binding = read_probe(args.probe, ring)
    report["reused_completed_column"] = old_binding
    q = ring.power_tail(8)
    quadratics = [CachedQuadratic(op) for op in exact.operator_basis(ring)]
    thirds = [OriginalTailThird(source_ring.p, ring, template) for template in templates]
    spans, records = {}, []
    new_count = 0
    for ti, third in enumerate(thirds):
        for ai, quadratic in enumerate(quadratics):
            index = ti*8+ai
            weight = blocks.THIRD_WEIGHTS[ti]+blocks.PARAMETER_WEIGHTS[ai]
            if (ai, ti) == (7, 12):
                value = old_column
                reused = True
            else:
                value = tail.pure_fourth_response(quadratic, third, q)/16
                reused = False
                new_count += 1
            if any(a+b != 32+weight for a, b in value.terms):
                raise AssertionError("full response violates its true homogeneous scaling weight")
            reflected = four_block_projection(value.terms)
            expected = ({key: 4*v for key, v in value.terms.items()} if weight % 2 == 0 else {})
            if reflected != expected:
                raise AssertionError("complete R106 four-block parity projection")
            span = spans.setdefault(weight, ExactProjectedSpan(ring))
            span.add(index, value.terms)
            records.append({"index": index, "quadratic_index": ai,
                "quadratic_name": PARAMETER_NAMES[ai], "quadratic_weight": blocks.PARAMETER_WEIGHTS[ai],
                "third_index": ti, "v2_original_third_index": blocks.EXPECTED_KEPT[ti],
                "third_weight": blocks.THIRD_WEIGHTS[ti],
                "original_third_sha256": source_ring.digest(templates[ti]),
                "response_weight": weight, "total_degree_if_nonzero": 32+weight,
                "complete_polynomial": value.rows(), "complete_polynomial_sha256": sha(canonical(value.rows())),
                "reused_R110_column": reused, "four_block_factor": 4 if weight % 2 == 0 else 0})
            ring.guard()
        report["completed_original_columns"] = len(records)
        report["completed_new_columns"] = new_count
        if (ti+1) % 6 == 0:
            print(json.dumps({"phase": "complete_m8_original_columns",
                "completed": len(records), "new": new_count}), flush=True)
    if len(records) != 288 or new_count != 287:
        raise AssertionError("the complete E8 by W36 coverage changed")
    blocks_out = {str(weight): span.summary() for weight, span in sorted(spans.items())}
    support = sorted({(row["c_power"], row["r_power"])
                      for item in records for row in item["complete_polynomial"]})
    full_rank = sum(len(span.independent) for span in spans.values())
    closed_rank = sum(len(span.independent) for weight, span in spans.items() if weight % 2 == 0)
    closed_support = [key for key in support if sum(key) % 2 == 0]
    certificate = {"schema": SCHEMA+"-certificate", "source_hashes": report["source_hashes"],
        "template_input": report["template_input"], "reused_completed_column": old_binding,
        "profile": "q=(c-xi)^8, r=c-xi, same true right anchor c",
        "phase": "complete pure -4 response, full F=0 quartic response divided by 16",
        "columns": records, "exact_weight_blocks": blocks_out,
        "all_monomial_rows": [list(key) for key in support],
        "four_block_monomial_rows": [list(key) for key in closed_support],
        "four_block_rule": "2*(V(c,r)+V(-c,-r)); even total degree times four, odd total degree zero",
        "exact_full_projection_rank": full_rank, "exact_four_block_projection_rank": closed_rank,
        "full_operator_rank_or_relations_claimed": False}
    certificate_path = args.out.with_name(args.out.stem+"-certificate.json.gz")
    certificate_info = write_certificate(certificate_path, certificate)
    compact_blocks = {weight: {"columns": sum(1 for x in records if x["response_weight"] == int(weight)),
        "exact_rank_over_Q": item["exact_rank_over_Q"],
        "independent_original_columns": item["independent_original_columns"],
        "verified_projected_dependencies": len(item["verified_complete_polynomial_dependencies"])}
        for weight, item in blocks_out.items()}
    report.update(completion="complete", complete_E8_by_W36_coverage=True,
        total_original_columns=288, newly_evaluated_columns=287, reused_completed_columns=1,
        exact_full_projection_rank=full_rank, exact_four_block_projection_rank=closed_rank,
        monomial_row_count=len(support), four_block_monomial_row_count=len(closed_support),
        exact_weight_blocks=compact_blocks, complete_certificate=certificate_info,
        all_original_column_polynomials_published=True,
        all_projected_dependency_differences_zero=True,
        polynomial_operations=ring.operations, linear_operations=ring.linear_operations,
        raw_original_atoms_evaluated=ring.raw_atoms_evaluated,
        raw_original_monomials_evaluated=ring.raw_monomials_evaluated,
        maximum_intermediate_terms=ring.maximum_terms,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,
        third_basis_recompiled=False, old_forcing_recompiled=False, old_finite_node_query_recomputed=False,
        complete_operator_dependencies_claimed=False, full_R8_dimension_claimed=False,
        baseline_cost_evaluated=False, complete_m8_tail_period_paid=False,
        mixed_mode_or_ruling_paid=False, geometric_path_evaluated=False,
        task_complete=False)
    return report


def toy_only():
    limits = exact.Limits(seconds=40, nodes=10000, atoms=10000, terms=10000,
                          rewrites=10000, memory_mib=256)
    source = colored.ColoredRing(limits)
    a, b, c = (source.color(x) for x in ("a", "b", "c"))
    original = a*b*c+(a.D()*b*c).I()+2*source.x()*a*b.D()*c
    portable = local4.serialize_expressions(source, {"toy": original})
    restored_ring = colored.ColoredRing(limits)
    restored = local4.decode_expressions(restored_ring, portable)["toy"]
    ring = TailRing(40, 256, 100000)
    r = tail.Polynomial(ring, {(0, 1): F(1)})
    endpoint = tail.Polynomial(ring, {(1, 0): F(1)})
    f, g, h = r*r+endpoint, r+endpoint*endpoint, 1+r*r*r
    third = OriginalTailThird(restored_ring.p, ring, restored)
    actual_value = third(f, g, h)
    expected = f*g*h-(f.D()*g*h).J()+2*ring.x()*f*g.D()*h
    checks = {
        "portable_original_DAG_hash_roundtrip": source.digest(original) == restored_ring.digest(restored),
        "original_right_I_is_minus_adapter_J": not (actual_value-expected).terms,
        "outer_and_inner_slots_not_silently_sorted": bool((third(f, g, h)-third(f, h, g)).terms),
    }
    span = ExactProjectedSpan(ring)
    v0, v1 = {(2, 0): F(1)}, {(0, 2): F(1)}
    v2 = {(2, 0): F(2), (0, 2): F(-3)}
    for i, value in enumerate((v0, v1, v2, {})):
        span.add(i, value)
    checks["exact_artificial_projection_rank"] = len(span.independent) == 2
    checks["all_artificial_projected_relations_verified"] = len(span.dependencies) == 2
    mixed = {(2, 0): F(2), (1, 2): F(3), (0, 2): F(-5)}
    checks["four_block_projection_keeps_only_even_total_degree"] = (
        four_block_projection(mixed) == {(2, 0): F(8), (0, 2): F(-20)})
    checks["no_m8_profile_used"] = max(a+b for value in (f,g,h) for a,b in value.terms) <= 3
    export_toy = {"filename": "invented-W.gz", "stored_bytes": 7,
                  "stored_sha256": sha(b"packed!"), "raw_bytes": 9,
                  "raw_sha256": sha(b"original!")}
    driver_toy = {"filename": "literature_local_fourth_quotient.py",
                  "bytes": 4, "sha256": sha(b"code")}
    publication_toy = {"schema": "visible-new-mechanism-actions-v1",
        "repository": REPOSITORY, "run_id": "artificial-run",
        "source_commit": "artificial-source", "lane": "local_fourth_quotient",
        "source_files": {"topics/visible-flex-new-mechanism/scripts/literature_local_fourth_quotient.py":
                         {"bytes": 4, "sha256": sha(b"code")}},
        "outputs": [{"path": "invented-main.json", "bytes": 2, "sha256": sha(b"{}"),
                     "raw_bytes": 2, "raw_sha256": sha(b"{}")},
                    {"path": export_toy["filename"], "bytes": 7, "sha256": export_toy["stored_sha256"],
                     "raw_bytes": 9, "raw_sha256": export_toy["raw_sha256"]}]}
    manifest_arguments = dict(source_run="artificial-run", source_commit="artificial-source",
        report_name="invented-main.json", report_bytes=2, report_sha=sha(b"{}"),
        export_record=export_toy, driver_identity=driver_toy)
    binding = verify_publication_binding(publication_toy, **manifest_arguments)
    checks["compact_report_uses_bound_public_manifest_source"] = (
        binding["source_run"] == "artificial-run" and len(binding["matched_output_paths"]) == 2)
    bad_publication = json.loads(json.dumps(publication_toy))
    bad_publication["outputs"][0]["sha256"] = sha(b"wrong")
    try:
        verify_publication_binding(bad_publication, **manifest_arguments)
        checks["incorrect_public_manifest_report_hash_rejected"] = False
    except ValueError:
        checks["incorrect_public_manifest_report_hash_rejected"] = True
    if not all(checks.values()):
        raise AssertionError({"new_artificial_checks": checks})
    return {"schema": SCHEMA+"-development", "completion": "complete", "all_passed": True,
        "checks": checks, "real_W36_loaded": False, "old_forcing_compiled": False,
        "research_m8_projection_evaluated": False, "geometry_evaluated": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--templates", type=Path)
    parser.add_argument("--source-report", type=Path)
    parser.add_argument("--publication-receipt", type=Path)
    parser.add_argument("--source-report-sha256")
    parser.add_argument("--source-run")
    parser.add_argument("--source-commit")
    parser.add_argument("--third-receipt", type=Path, default=dual.DEFAULT_RECEIPT)
    parser.add_argument("--probe", type=Path, default=DEFAULT_PROBE)
    parser.add_argument("--max-seconds", type=float, default=240)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-operations", type=int, default=10000000)
    args = parser.parse_args()
    started = time.monotonic()
    report = {"schema": SCHEMA, "completion": "started",
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "source_hashes": dependencies(), "task_complete": False}
    failed = False
    try:
        if args.toy_only:
            report.update(toy_only())
        else:
            actual(args, report)
    except Exception as error:
        failed = True
        report.update(completion="incomplete", error_type=type(error).__name__, error=str(error),
            new_mathematical_conclusion_published=False, task_complete=False)
    report["wall_seconds"] = time.monotonic()-started
    result = write_json(args.out, report)
    print(json.dumps(result, sort_keys=True), flush=True)
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
