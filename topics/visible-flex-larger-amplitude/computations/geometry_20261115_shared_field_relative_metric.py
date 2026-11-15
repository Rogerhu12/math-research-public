#!/usr/bin/env python3
"""R251 relative-operator consumer for one complete bound shared-B field.

Reuse the exact finite field and the existing original finite-Gauss scalar
interpreter.  Both full active sheets are covered in closed (u,q) cells,
q=phi/(2*pi); theta=Phi(phi) is retained without a new Fourier projection.
The two original fixed graph caps use their original R14/R248 induced metric.

The original stored tail does NOT yet have a reviewed continuous E(r)
enclosure producer.  Missing tail envelopes remain explicit unpaid cells.
Optional envelopes are external mathematical premises, bound to this exact
original source; neither a schema nor a source hash proves their validity.
No existing sampled w table, B-prime, or different real-integral source is
substituted for the original target.  Results distinguish conditional cell
inequalities, actual-live scalar provenance, and the unpaid global seams.

This is a postprocessing consumer, never a new native acceptance condition.
Scientific arithmetic and original loaders run only in public Actions.
All generated cell/premise payloads are temporary under repository rule 15.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "same-shared-field-R251-complete-relative-metric-consumer-v1"
TAIL_SCHEMA = "same-original-stored-tail-closed-E-envelope-premises-v1"
TAIL_DEFINITION = "Original stored source g_A=(1+w(r)^2)dr^2+r^2dtheta^2; no Bprime substitution"
SOURCE_PINS = {
    "geometry_20261115_shared_active_interval_balls.py":
        "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b",
    "geometry_20261115_fixed_cap_rational_balls.py":
        "a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e",
    "geometry_20261114_full_prefix_operator.py":
        "a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703",
    "geometry_20261114_direct_operator_cell.py":
        "1774f8da00ccd8ced6199e85d1fda6f455a224eed7d20d1a92ac04df3801e2ce",
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Run scientific arithmetic only in the named public repository's Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def receipt(path, root=None):
    digest, size = hashlib.sha256(), 0
    with Path(path).open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            size += len(raw)
            digest.update(raw)
    path = Path(path)
    name = str(path.relative_to(root)) if root is not None else path.name
    return dict(file=name, bytes=size, sha256=digest.hexdigest())


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("Duplicate JSON key: "+key)
        value[key] = item
    return value


def read_bound(path, expected):
    raw = Path(path).read_bytes()
    if sha(raw) != expected:
        raise ValueError("An explicit actual input SHA differs: "+str(path))
    decoded = gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw
    value = json.loads(decoded, object_pairs_hook=unique_object,
        parse_constant=lambda item: (_ for _ in ()).throw(ValueError("Nonfinite JSON token: "+item)))
    return value, dict(file=Path(path).name, bytes=len(raw), sha256=expected,
                       decoded_bytes=len(decoded), decoded_sha256=sha(decoded))


def rational(value):
    # Bounds are exact rational text/integers, never silently decimalized f64.
    if isinstance(value, bool) or not isinstance(value, (str, int, F)):
        raise ValueError("Enclosure bounds require exact rational strings or integers")
    return F(value)


def load_module(directory, name):
    path = Path(directory)/name
    raw = path.read_bytes()
    if sha(raw) != SOURCE_PINS[name]:
        raise ValueError("A frozen defining module changed: "+name)
    module_name = name[:-3]
    previous = sys.modules.get(module_name)
    if previous is not None:
        if receipt(previous.__file__)["sha256"] != SOURCE_PINS[name]:
            raise ValueError("A different module with this basename was already imported")
        return previous
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class Journal:
    """One complete gzip member per flushed record, preserving partial work."""
    def __init__(self, path):
        self.path = path
        self.count = 0
        self.stream = path.open("xb")

    def append(self, record):
        self.stream.write(gzip.compress(canonical(record), mtime=0))
        self.stream.flush()
        self.count += 1

    def close(self):
        self.stream.close()


def tail_identity(field, args, prefix_descriptor):
    """Identity needed by the missing same-original-g producer, not a proof."""
    return dict(
        complete_field_binding=field.binding,
        configuration=receipt(args.config),
        actual_tail_response=receipt(args.tail_response),
        complete_tail_readout=receipt(args.complete),
        original_reference_table=receipt(field.paths["background"]),
        original_profile_fingerprint=field.table["profile_fingerprint"],
        original_target_metric_background_sha256=
            field.A.shared_background_geometry["original_target_metric_background_sha256"],
        original_plan_tail_adapter_sha256=field.plan["adapter_sha256"],
        original_source_revision=field.plan["source_revision"],
        original_reference_table_provenance_fields={key:field.table[key] for key in
            ("source_adapter", "source_revision", "source_sha256", "inputs") if key in field.table},
        exact_closed_radial_domain=[str(field.cuff), str(field.cut)],
        full_prefix_scalar_mathematical_identity_sha256=
            prefix_descriptor["mathematical_identity_sha256"],
        complete_material_core_coefficients=[str(v) for v in field.core],
        complete_material_density_lower=str(field.rho_lower),
        target_definition=TAIL_DEFINITION,
        target_metric_replaced_by_geometric_Bprime=False,
        sampled_reference_rows_used_as_continuous_enclosures=False,
        real_integral_R26_background_substituted_for_stored_source=False)


class TailEnvelopePremises:
    """Finite closed cover of explicitly external, same-source E bounds.

    This reader verifies identity, positivity and interval coverage.  It does
    not prove E_lower <= original E(r) <= E_upper.  That is deliberately a
    named external premise, even if a supplied file contains a true flag.
    """
    def __init__(self, path, expected_sha, expected_binding):
        self.rows, self.cuts = [], []
        self.receipt = None
        self.binding = expected_binding
        self.external_provenance = None
        self.supplied = path is not None
        if not self.supplied:
            return
        data, self.receipt = read_bound(path, expected_sha)
        if (data.get("schema") != TAIL_SCHEMA
                or data.get("original_target_identity") != expected_binding
                or data.get("target_definition") != TAIL_DEFINITION):
            raise ValueError("External tail premises name another source, metric, or complete field")
        self.external_provenance = data.get("enclosure_provenance")
        if not isinstance(self.external_provenance, dict) or not self.external_provenance:
            raise ValueError("External E bounds need an explicit provenance/proof reference")
        domain = tuple(map(rational, expected_binding["exact_closed_radial_domain"]))
        raw_rows = data.get("closed_radial_envelopes")
        if not isinstance(raw_rows, list) or not raw_rows:
            raise ValueError("The external tail premise cover is empty")
        previous = domain[0]
        for index, row in enumerate(raw_rows):
            a, b = map(rational, row["closed_radial_interval"])
            lo, hi = rational(row["E_lower"]), rational(row["E_upper"])
            if a != previous or not a < b <= domain[1] or not 0 < lo <= hi:
                raise ValueError("Tail premise intervals must form the entire contiguous closed positive cover")
            self.rows.append(dict(index=index, left=a, right=b, lower=lo, upper=hi,
                proof_reference=row.get("proof_reference")))
            previous = b
        if previous != domain[1]:
            raise ValueError("An external tail premise omitted the collar or outer cut")
        self.cuts = sorted(set(v for row in self.rows for v in (row["left"], row["right"])))

    def bounds(self, a, b):
        if not self.supplied:
            return None
        # Include both adjacent closed rows at a boundary.  This conservative
        # union never silently chooses a different endpoint target value.
        selected = [row for row in self.rows if row["left"] <= b and a <= row["right"]]
        if not selected or selected[0]["left"] > a or selected[-1]["right"] < b:
            raise ValueError("The requested closed cell lacks full external target coverage")
        return min(row["lower"] for row in selected), max(row["upper"] for row in selected), [row["index"] for row in selected]

    def report(self):
        return dict(
            supplied=self.supplied, input=self.receipt,
            complete_closed_radial_cover_checked=self.supplied,
            source_identity_checked=self.supplied,
            enclosure_provenance=self.external_provenance,
            original_continuous_E_bounds_proved_by_this_consumer=False,
            external_premises_verified_from_schema_or_boolean=False,
            missing_original_stored_g_interval_producer=True,
            scope="Conditional E-envelope premises only; full original-source continuity/enclosure proof remains external")


def closed_scalar_range(scalar, M, a, b):
    """Same finite-Gauss expression; include actual mask-selected endpoints."""
    if any(a < cut < b for cut in scalar.breakpoints):
        raise ValueError("A scalar interval crosses an unsplit source phase/clip/mask/control boundary")
    middle = (a+b)/2
    branch = scalar.branch(middle)
    value = scalar.value(M.interval(a, b), branch, middle)
    endpoint_branches = []
    # Interior branch formulas need not be assumed equal at rounded source
    # interfaces.  Add the actual source-selected value at EACH closed end.
    for endpoint in (a, b):
        selected = scalar.branch(endpoint)
        at = scalar.value(M.ball(endpoint), selected, endpoint)
        value = value.union(at)
        endpoint_branches.append(list(selected))
    return value, dict(interior_branch=list(branch), actual_endpoint_branches=endpoint_branches,
        interval=list(map(str, (a, b))), all_original_Gauss_nodes_weights_retained=True,
        closed_endpoint_values_added_without_assuming_interface_continuity=True,
        returned_ap_app_used_as_derivatives=False,
        scalar_C2_interfaces_proved_here=False)


def angle_density(field, M, angular):
    q = M.Jet2.variable(*angular, coordinate=1)
    phi = M.Jet2.constant(2*M.arb.pi())*q
    theta_q = field.material_angle(phi).d[2]
    lo, hi = M.bounds(theta_q)
    known_lo, _ = M.bounds(2*M.arb.pi()*M.ball(field.rho_lower))
    # The original accepted reader proves this complete-core R237 bound.
    # Intersect two established enclosures; do not invent a positive floor.
    lo = max(lo, known_lo)
    if lo <= 0 or hi < lo:
        raise ArithmeticError("No positive enclosure for the actual full material pullback")
    return M.interval(lo, hi), dict(
        theta_q=M.encode_interval(M.interval(lo, hi)),
        full_rho_lower_exact=str(field.rho_lower),
        formula="q=phi/(2*pi); theta_q=2*pi*(1+sum((1-4*m*m)*c_m*cos(2*m*phi)))",
        finite_phi_band_assumed_for_composed_tail=False,
        finite_theta_band_assumed_for_full_cut=False)


def loewner_certificate(M, E, B, C, g11, g22, eta):
    """R251, for a positive diagonal target, using its conservative bounds."""
    l1, u1 = M.bounds(g11)
    l2, u2 = M.bounds(g22)
    if l1 <= 0 or l2 <= 0:
        return dict(certified=False, reason="target_positive_diagonal_lower_unresolved",
                    target_diagonal=[M.encode_interval(g11), M.encode_interval(g22)])
    one_plus, one_minus = M.ball(1+eta), M.ball(1-eta)
    p11 = one_plus*M.ball(l1)-E
    p22 = one_plus*M.ball(l2)-C
    m11 = E-one_minus*M.ball(u1)
    m22 = C-one_minus*M.ball(u2)
    pd, md = p11*p22-B*B, m11*m22-B*B
    values = dict(plus_leading=p11, plus_determinant=pd,
                  minus_leading=m11, minus_determinant=md)
    margins = {name:M.encode_interval(value) for name,value in values.items()}
    passed = all(M.bounds(value)[0] > 0 for value in values.values())
    return dict(certified=passed, requested_eta_exact=str(eta),
        reason="four_R251_strict_lower_bounds_positive" if passed else "interval_lower_margin_unresolved_not_a_point_failure",
        Gram=dict(E=M.encode_interval(E), B=M.encode_interval(B), C=M.encode_interval(C)),
        target_diagonal=[M.encode_interval(g11), M.encode_interval(g22)],
        lower_target_used_for_plus=True, upper_target_used_for_minus=True,
        strict_margins=margins, component_max_substituted_for_operator_norm=False,
        pointwise_counterexample_proved=False,
        mathematical_scope="Strict relative operator norm < eta, conditional on the stated target bounds")


def inspect_cell(M, field, scalar, tail, spec, eta):
    piece = field.pieces[spec["piece_index"]]
    radial, angular = tuple(map(F, spec["radial"])), tuple(map(F, spec["angular"]))
    kind = piece["kind"]
    if kind != "prefix" and not tail.supplied:
        return dict(certified=False, missing_target_premise=True,
            reason="original_stored_tail_continuous_E_enclosure_not_supplied",
            geometric_Bprime_substituted=False, sampled_w_table_substituted=False,
            original_real_integral_metric_substituted=False)
    values = field.evaluate(piece, radial, angular, spec["lower"])
    X, Y = tuple(v.d[1] for v in values), tuple(v.d[2] for v in values)
    E, B, C = M.dot(X, X), M.dot(X, Y), M.dot(Y, Y)
    theta_q, angular_record = angle_density(field, M, angular)
    if kind == "prefix":
        a, scalar_record = closed_scalar_range(scalar, M, *radial)
        if M.bounds(a)[0] <= 0:
            return dict(certified=False, reason="same_original_scalar_positive_lower_unresolved",
                scalar=scalar_record, scalar_value=M.encode_interval(a), angular=angular_record)
        g11, g22 = M.arb(1), a*a*theta_q*theta_q
        target = dict(kind="original_complete_prefix_scalar", scalar=scalar_record,
                      scalar_value=M.encode_interval(a), tail_bounds_external=False)
    else:
        elo, ehi, rows = tail.bounds(*radial)
        g11 = M.interval(elo, ehi)
        r = M.interval(*radial)
        g22 = r*r*theta_q*theta_q
        target = dict(kind="original_stored_tail_external_continuous_E_premises",
                      premise_rows=rows, tail_bounds_external=True,
                      enclosure_truth_proved_here=False,
                      target_definition=TAIL_DEFINITION)
    result = loewner_certificate(M, E, B, C, g11, g22, eta)
    result.update(target=target, angular=angular_record,
        complete_position_and_six_jets={name:[M.encode_interval(v.d[j]) for v in values]
            for j,name in enumerate(M.JET_NAMES)},
        derivatives_of_bound_exact_field=True,
        renderer_jets_used_as_consistent_derivatives=False,
        complete_material_cut_and_zero_mode_mean_retained=True)
    return result


def root_plan(field, scalar, tail, angular_depth):
    """Compact immutable definition of every root, without a large grid list."""
    angular_count = 2**angular_depth
    blocks = []
    for lower in (False, True):
        for index, piece in enumerate(field.pieces):
            a, b = piece["left"], piece["right"]
            extra = scalar.breakpoints if piece["kind"] == "prefix" else tail.cuts
            cuts = sorted(set([a, b]+[x for x in extra if a < x < b]))
            for radial_index, (left, right) in enumerate(zip(cuts, cuts[1:])):
                blocks.append(dict(block_index=len(blocks), lower=lower, piece_index=index,
                    piece_kind=piece["kind"], scalar_or_target_subinterval=radial_index,
                    radial=list(map(str, (left, right)))))
    return dict(schema=SCHEMA+"-complete-closed-root-plan", radial_blocks=blocks,
        initial_angular_depth=angular_depth, angular_count=angular_count,
        planned_roots=len(blocks)*angular_count,
        exact_rank_formula="rank=block_index*angular_count+angular_index",
        closed_angular_interval_formula="[angular_index/angular_count,(angular_index+1)/angular_count]",
        complete_angular_index_range=[0,angular_count], index_upper_bound_exclusive=True,
        full_q_range=["0","1"], q_definition="physical phi/(2*pi)",
        identical_circle_endpoints_retained=True,
        complete_radial_block_list=True, all_roots_reconstructible_without_sampling=True)


def roots(plan):
    count = plan["angular_count"]
    for block in plan["radial_blocks"]:
        for angular_index in range(count):
            yield dict(block, rank=block["block_index"]*count+angular_index,
                angular_index=angular_index,
                angular=[str(F(angular_index,count)), str(F(angular_index+1,count))],
                depth=0, dyadic_path="")


def split_cell(spec):
    a, b = map(F, spec["radial"])
    c, d = map(F, spec["angular"])
    m, n = (a+b)/2, (c+d)/2
    boxes = [((a,m),(c,n)), ((m,b),(c,n)), ((a,m),(n,d)), ((m,b),(n,d))]
    return [dict(spec, radial=list(map(str, r)), angular=list(map(str, q)),
                 depth=spec["depth"]+1, dyadic_path=spec["dyadic_path"]+str(i))
            for i,(r,q) in enumerate(boxes)]


def cap_identity(Caps, field):
    pa, aa = field.paths["plan"], field.paths["assembly"]
    cuff, height, markers, binding = Caps.bind_geometry(SimpleNamespace(
        plan=pa, plan_sha256=receipt(pa)["sha256"],
        assembly=aa, assembly_sha256=receipt(aa)["sha256"]))
    if (cuff != field.cuff or binding["shared_background_geometry"] != field.A.shared_background_geometry
            or field.plan["fixed_cap"]["theorem"] != "R14-arbitrarily-weak-gaussian-cap-markers"):
        raise ValueError("The fixed caps are not this original R14/R248 design")
    return dict(binding=binding, complete_two_closed_disks=True,
        closed_domain=dict(coordinates="Cartesian xy, including the poles and the entire cuff boundary",
            radius_exact=str(cuff), sheets=["upper", "lower"]),
        exact_graph="F_+(x,y)=(x,y,H+b_+(x,y)); F_-(x,y)=(x,y,-H-b_-(x,y))",
        b_definition="sum of all original A_j*max(0,1-|xy-c_j|^2/R_j^2)^4 on the corresponding cap",
        target_metric_definition="The original R14/R248 fixed-cap induced metric I+Db tensor Db",
        induced_and_target_metric_are_the_same_exact_graph_expression=True,
        exact_relative_operator_error="0", no_angular_or_radial_samples_used=True,
        old_flat_cap_metric_substituted=False,
        target_cap_assignment_reference="R14 section 2; R248 section 4, fixed graph metric chosen in the original design",
        global_cuff_C2_or_target_metric_compatibility_proved_here=False,
        stored_normal_kappa_used_as_graph_derivative=False)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("directory", "source-directory", "descriptor", "checkpoint", "port", "config",
                 "tail-response", "complete", "source-topic", "out"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--basename", default="surface")
    p.add_argument("--source-basename", default="surface")
    p.add_argument("--code-directory", type=Path, default=HERE)
    p.add_argument("--scalar-descriptor", type=Path)
    p.add_argument("--scalar-descriptor-sha256")
    p.add_argument("--tail-target-envelopes", type=Path)
    p.add_argument("--tail-target-envelopes-sha256")
    p.add_argument("--eta", default="1/1000000")
    p.add_argument("--precision-bits", type=int, default=192)
    p.add_argument("--initial-angular-depth", type=int, default=3)
    p.add_argument("--max-depth", type=int, default=10)
    p.add_argument("--max-visited-cells", type=int, default=1000000)
    p.add_argument("--budget-seconds", type=int, default=3600)
    args = p.parse_args()
    require_actions()
    if args.out.exists():
        raise FileExistsError("Preserve all previous results")
    for path_key, hash_key in (("scalar_descriptor", "scalar_descriptor_sha256"),
                               ("tail_target_envelopes", "tail_target_envelopes_sha256")):
        if (getattr(args, path_key) is None) != (getattr(args, hash_key) is None):
            raise ValueError("An optional actual premise and its SHA must be supplied together")
    eta = rational(args.eta)
    if (not 0 < eta < 1 or not 64 <= args.precision_bits <= 8192
            or not 0 <= args.initial_angular_depth <= 20 or not 0 <= args.max_depth <= 30
            or args.max_visited_cells <= 0 or args.budget_seconds <= 0):
        raise ValueError("Invalid explicit target or resource parameters")
    sys.path.insert(0, str(args.code_directory.resolve()))
    M = load_module(args.code_directory, "geometry_20261115_shared_active_interval_balls.py")
    geometry, background, _, active_sources = M.initialise_runtime(args.code_directory)
    Caps = load_module(args.code_directory, "geometry_20261115_fixed_cap_rational_balls.py")
    Prefix = load_module(args.code_directory, "geometry_20261114_full_prefix_operator.py")
    Cell = load_module(args.code_directory, "geometry_20261114_direct_operator_cell.py")
    source_closure = dict(active_sources)
    source_closure.update({name:receipt(args.code_directory/name) for name in SOURCE_PINS})
    source_closure.update({name:dict(sha256=digest, **{"bytes":(args.code_directory/name).stat().st_size})
                           for name,digest in Prefix.checked_original_sources().items()})
    started = time.monotonic()
    old_precision = M.ctx.prec
    args.out.mkdir(parents=True)
    large = args.out/"large-arrays"
    large.mkdir()
    journal = None
    try:
        M.ctx.prec = args.precision_bits+args.max_depth
        bundle = geometry.load_shared_bundle(args)
        field = M.ExactFiniteField(bundle, background)
        specification = field.saved.rec["fixed_scalar_profile"]["geometry"]
        reconstructed = Prefix.export_scalar_descriptor(field.saved.profile_model, specification,
            producer_checkpoint_sha256=Prefix.file_sha(args.checkpoint), origin="reconstructed-from-checkpoint")
        if args.scalar_descriptor is not None:
            read_bound(args.scalar_descriptor, args.scalar_descriptor_sha256)
        scalar_binding = Prefix.descriptor_binding(field.saved, reconstructed, args.scalar_descriptor)
        scalar = Prefix.ScalarExpression(specification, reconstructed, Cell)
        if scalar.boundaries["end"] != field.x[-1]:
            raise ValueError("The complete original scalar and full finite field have different prefix domains")
        tail_binding = tail_identity(field, args, reconstructed)
        tail = TailEnvelopePremises(args.tail_target_envelopes,
                                   args.tail_target_envelopes_sha256, tail_binding)
        cap = cap_identity(Caps, field)
        (large/"same-scalar-expression.json").write_bytes(canonical(reconstructed))
        (large/"required-original-tail-target-identity.json").write_bytes(canonical(tail_binding))
        (large/"original-fixed-cap-target-identity.json").write_bytes(canonical(cap))
        input_binding = dict(schema=SCHEMA+"-binding", source_sha256=sha(Path(__file__).read_bytes()),
            source_closure=source_closure, complete_field_binding=field.binding,
            shared_background_geometry=field.A.shared_background_geometry,
            actual_plan=receipt(field.paths["plan"]), actual_assembly=receipt(field.paths["assembly"]),
            original_inputs={name:receipt(getattr(args,name)) for name in
                ("descriptor", "checkpoint", "port", "config", "tail_response", "complete")},
            scalar_binding=scalar_binding, tail_envelope_premises=tail.report(),
            original_accepted_parent_required_only_by_original_loader=True,
            postprocessed_field_does_not_inherit_an_exact_isometry_from_native_acceptance=True,
            same_material_theta_and_all_components_preserved=True)
        (large/"input-binding.json").write_bytes(canonical(input_binding))
        planned = root_plan(field, scalar, tail, args.initial_angular_depth)
        planned_count = planned["planned_roots"]
        (large/"planned-closed-roots.json").write_bytes(canonical(planned))
        journal = Journal(large/"relative-metric-cells.jsonl.gz")
        journal.append(dict(type="identity", input_binding=receipt(large/"input-binding.json",args.out),
            requested_eta_exact=str(eta), planned_roots=receipt(large/"planned-closed-roots.json",args.out),
            complete_closed_caps=receipt(large/"original-fixed-cap-target-identity.json",args.out)))
        visited = terminal = passed = missing = 0
        root_results = []
        resource_stop = execution_error = None
        pending = []
        next_rank = 0
        counters = {name:dict(planned_roots=sum(row["piece_kind"] == name for row in planned["radial_blocks"])
                              *planned["angular_count"],
                              completed_roots=0, certified_roots=0, terminal_cells=0,
                              certified_cells=0, unresolved_cells=0)
                    for name in ("prefix", "collar", "native")}
        for root in roots(planned):
            next_rank = root["rank"]
            stack = [root]
            root_ok = True
            while stack:
                if visited >= args.max_visited_cells or time.monotonic()-started >= args.budget_seconds:
                    resource_stop = "explicit_cell_or_wall_time_budget_before_next_complete_cell"
                    pending = list(reversed(stack))
                    break
                spec = stack.pop()
                visited += 1
                try:
                    report = inspect_cell(M, field, scalar, tail, spec, eta)
                except (ArithmeticError, ValueError) as exc:
                    report = dict(certified=False, reason="interval_or_declared_expression_evaluation_unresolved",
                                  exception=dict(type=type(exc).__name__, message=str(exc)))
                except Exception as exc:
                    execution_error = dict(type=type(exc).__name__, message=str(exc), cell=spec)
                    pending = [spec]+list(reversed(stack))
                    break
                if (not report["certified"] and not report.get("missing_target_premise", False)
                        and spec["depth"] < args.max_depth):
                    journal.append(dict(type="subdivided", cell=spec, diagnostic=report))
                    stack.extend(reversed(split_cell(spec)))
                    continue
                journal.append(dict(type="terminal_closed_cell", cell=spec, operator=report))
                terminal += 1
                passed += int(report["certified"])
                missing += int(report.get("missing_target_premise", False))
                stats = counters[spec["piece_kind"]]
                stats["terminal_cells"] += 1
                stats["certified_cells"] += int(report["certified"])
                stats["unresolved_cells"] += int(not report["certified"])
                root_ok = root_ok and report["certified"]
            if resource_stop is not None or execution_error is not None:
                break
            root_results.append(dict(rank=root["rank"], piece_kind=root["piece_kind"],
                                     complete_closed_subdivision=True, certified=root_ok))
            counters[root["piece_kind"]]["completed_roots"] += 1
            counters[root["piece_kind"]]["certified_roots"] += int(root_ok)
            next_rank = root["rank"]+1
            if len(root_results) % 20 == 0:
                print(json.dumps(dict(event="same_field_relative_metric_progress",
                    completed_roots=len(root_results), planned_roots=planned_count,
                    terminal_closed_cells=terminal, certified_cells=passed,
                    tail_premises_external=tail.supplied, seconds=time.monotonic()-started),
                    separators=(",", ":")), flush=True)
        complete = len(root_results) == planned_count
        # A partially visited root is represented by its exact remaining DFS
        # cells; all later roots are preserved as a suffix of the immutable plan.
        suffix_start = planned_count if complete else next_rank+1
        pending_record = dict(current_root_rank=None if complete else next_rank,
            remaining_closed_DFS_cells=pending,
            untouched_root_rank_suffix=[suffix_start, planned_count],
            immutable_root_plan=receipt(large/"planned-closed-roots.json",args.out),
            completed_roots=root_results,
            all_unresolved_terminal_cells_remain_in_ledger=True)
        (large/"coverage-and-pending.json").write_bytes(canonical(pending_record))
        journal.append(dict(type="coverage_end", completed=complete,
            coverage=receipt(large/"coverage-and-pending.json",args.out),
            resource_stop=resource_stop, execution_error=execution_error))
        journal.close()
        journal = None
        expression = field.expression_identity()
        (large/"same-exact-finite-field-expression.json").write_bytes(canonical(expression))
        prefix_complete = counters["prefix"]["completed_roots"] == counters["prefix"]["planned_roots"]
        prefix_ok = prefix_complete and counters["prefix"]["certified_roots"] == counters["prefix"]["planned_roots"]
        active_ok = complete and all(row["certified"] for row in root_results)
        result = dict(schema=SCHEMA, completed=complete,
            source_sha256=input_binding["source_sha256"], source_closure=source_closure,
            parameters=dict(eta_exact=str(eta), precision_bits=args.precision_bits,
                effective_precision_bits=args.precision_bits+args.max_depth,
                initial_angular_depth=args.initial_angular_depth, max_depth=args.max_depth,
                max_visited_cells=args.max_visited_cells, budget_seconds=args.budget_seconds),
            input_binding=receipt(large/"input-binding.json",args.out),
            expression=receipt(large/"same-exact-finite-field-expression.json",args.out),
            scalar_expression=receipt(large/"same-scalar-expression.json",args.out),
            required_tail_target_identity=receipt(large/"required-original-tail-target-identity.json",args.out),
            fixed_cap_identity=receipt(large/"original-fixed-cap-target-identity.json",args.out),
            complete_cell_ledger=receipt(large/"relative-metric-cells.jsonl.gz",args.out),
            coverage_and_pending=receipt(large/"coverage-and-pending.json",args.out),
            partition=dict(planned_roots=planned_count, completed_roots=len(root_results),
                visited_cells=visited, terminal_closed_cells=terminal,
                certified_cells=passed, unresolved_terminal_cells=terminal-passed,
                missing_original_tail_target_cells=missing, by_piece=counters,
                both_reflected_sheets_and_all_closed_angle_endpoints=True,
                all_original_field_scalar_source_and_target_boundaries_split=True,
                unvisited_space_never_discarded=True),
            exact_two_original_fixed_cap_operator_error="0",
            complete_prefix_operator_bound_for_declared_real_expression=prefix_ok,
            complete_prefix_operator_bound_with_actual_live_scalar_constants=bool(
                prefix_ok and scalar_binding["actual_live_runtime_constants_verified"]),
            complete_active_operator_bound_under_explicit_target_premises=active_ok,
            whole_closed_chartwise_operator_bound_under_explicit_target_premises=active_ok,
            original_stored_tail_continuous_E_enclosures_proved_here=False,
            external_tail_target_premises=tail.report(),
            target_scalar_live_constants_verified=scalar_binding["actual_live_runtime_constants_verified"],
            global_C2_geometry_seams_proved_here=False,
            global_original_target_metric_interface_compatibility_proved_here=False,
            all_phase_reduction=dict(theorem="R248 section 4", sampled_time_grid_used=False,
                conditional_on_actual_C2_and_original_target_metric_atlas_compatibility=True,
                conclusion="On the original active material charts, relative errors are shifted by theta-alpha; fixed cap errors are exactly zero",
                actual_complete_closed_family_certificate_paid=False),
            whole_original_g_closed_surface_standard4_certified=False,
            rigorous_pointwise_counterexample_proved=False,
            mathematical_failure_inferred_from_budget_or_interval_failure=False,
            target_replaced_by_Bprime=False, new_metric_fitted=False,
            finite_theta_band_mislabeled_finite_phi_band=False,
            full_mean_or_native_mode_dropped=False,
            ordinary_floating_renderer_error_bound_certified=False,
            original_native_BVP_or_RMS_BC_tolerances_changed=False,
            new_native_acceptance_or_jet_machine_gate_added=False,
            same_g_refinement_sequence_completed=False, reach_held_delta_E_or_task_completed=False,
            resource_stop=resource_stop, execution_error=execution_error,
            elapsed_seconds=time.monotonic()-started)
        raw = canonical(result)
        (args.out/"result.json").write_bytes(raw)
        print(json.dumps(dict(event="same_field_relative_metric_component", completed=complete,
            source_sha256=result["source_sha256"], result_bytes=len(raw), result_sha256=sha(raw),
            complete_prefix_operator_bound_for_declared_real_expression=prefix_ok,
            whole_closed_chartwise_bound_under_explicit_external_premises=active_ok,
            original_stored_tail_enclosure_proved_here=False,
            global_seams_and_standard4_paid=False,
            resource_stop=resource_stop, execution_error=execution_error), separators=(",", ":")), flush=True)
        # A completed diagnostic with unresolved cells is not a native failure.
        # Only an actual execution exception changes this component's exit code.
        if execution_error is not None:
            raise SystemExit(1)
    finally:
        if journal is not None:
            journal.close()
        M.ctx.prec = old_precision


if __name__ == "__main__":
    main()
