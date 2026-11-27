#!/usr/bin/env python3
"""Rebuild one actually recorded complete run10 field for same-target mesh reads.

No optimizer is called. The complete original main-constructor block is copied
verbatim and checked against its immutable source at runtime. A checkpoint or
immutable recorded full point supplies every free word. Existing full root,
fixed-seed and calibration words are read without inventing missing orders.
All numerical construction and field calls are public-Actions only.
"""
from __future__ import annotations
import ast
import copy
from fractions import Fraction
from fractions import Fraction as F
import hashlib
import heapq
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
from types import SimpleNamespace

SCHEMA = "actual-run10-same-field-complete-mesh-input-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
SCRIPT = "scripts/resume_20261126"
DRIVER_NAME = "fullclosed_run10_detached_closure_so3_qp.py"
DRIVER_SHA = "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1"
READER_NAME = "read_run10_detached_closure_so3_report.py"
READER_SHA = "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e"
LAUNCHER_SHA = "22069c4bb56a4ca4820b3f608cf720a36b036534e6b1e90b5f467f8eed21e604"
NORMAL_SHA = "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4"
BASE_SHA = "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"
DEEP_SHA = "e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2"
REFERENCE_ID = "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5"
TARGET_ID = "e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049"
INPUT_BINDING_SHA = "4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf"
CHART_SHA = "90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e"
CURRENT_SCALAR_LEAVES = 2218
CONSTRUCTOR_BLOCK_SHA = "612f000bcf42f37c13cecb03f6c380e894176a13a69474c49043c19295ce1d92"
SCALAR_PARENT_SOURCE_SHA = "2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74"
CHECKPOINT_MEMBERS = frozenset(("schema","omega_jets","core","Hcap","mesh",
    "fixed_parent_core","zero_closure_model_json","zero_closure_model_identity_sha256",
    "base_so3_model_identity_sha256","fixed_scalar_metric_identity_sha256",
    "endpoint_root_policy_json","working_integration_order","working_full_angles"))
MEAN_KEYS = ("v","v_phi","v_phiphi","d","d_phi","d_phiphi",
    "w","w_phi","w_phiphi","lambda","lambda_phi","lambda_phiphi")
PLAN_KEYS = ("boundary_values","boundary_weights","boundary_chi","outside_values",
    "outside_weights","base_gauss_u","base_gauss_w")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Complete field reconstruction and meshes run only in public repository Actions")


def sha(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            result.update(block)
    return result.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    import numpy as np
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def load(name, path, expected=None):
    if expected is not None and sha(path) != expected:
        raise ValueError("Changed complete source "+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if expected is not None and sha(path) != expected:
        raise ValueError("A complete source changed during import")
    return module


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".partial")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")
    temporary.replace(path)


class VerifiedFiles:
    def __init__(self):
        self.records = {}

    def verify(self, record):
        if (not isinstance(record, dict) or not isinstance(record.get("path"), str)
                or type(record.get("bytes")) is not int or record["bytes"] < 0
                or not isinstance(record.get("sha256"), str) or len(record["sha256"]) != 64):
            raise ValueError("A consumed file needs its complete path/bytes/SHA record")
        actual = file_record(record["path"])
        expected = {k: record[k] for k in ("path","bytes","sha256")}
        expected["path"] = str(Path(expected["path"]).resolve())
        if actual != expected:
            raise ValueError("Changed complete input "+expected["path"])
        old = self.records.get(actual["path"])
        if old is not None and old != actual:
            raise ValueError("One input path changed its declared complete identity")
        self.records[actual["path"]] = actual
        return Path(actual["path"])

    def add(self, path):
        value = file_record(path)
        self.verify(value)
        return value

    def read_json(self, record):
        path = self.verify(record)
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != record["sha256"] or len(raw) != record["bytes"]:
            raise ValueError("An immutable JSON changed during its read")
        result = json.loads(raw)
        self.verify(record)
        return result

    def recheck(self):
        for record in tuple(self.records.values()):
            self.verify(record)

    def protect(self, directory):
        directory = Path(directory).resolve()
        for record in self.records.values():
            path = Path(record["path"])
            if directory == path or directory in path.parents:
                raise ValueError("A mesh output directory must not contain a consumed source or input")


def capture_report(source, destination):
    """Freeze actual existing bytes; later source progress is not this snapshot."""
    source, destination = Path(source).resolve(), Path(destination).resolve()
    first = source.read_bytes()
    value = json.loads(first)
    if source.read_bytes() != first:
        raise ValueError("The scientific report changed while its immutable input was captured")
    if destination.exists():
        raise FileExistsError("Do not replace a captured scientific report")
    destination.write_bytes(first)
    return value, dict(original_path=str(source), captured_sha256=hashlib.sha256(first).hexdigest(),
        captured_bytes=len(first), captured_copy=file_record(destination),
        original_report_future_mutation_permitted=True, later_report_values_not_inherited=True)


def source_pins(path):
    tree = ast.parse(Path(path).read_text())
    nodes = [n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "SOURCE_PINS" for t in n.targets)]
    if len(nodes) != 1:
        raise ValueError("Use the actual whole driver's single complete source registry")
    value = ast.literal_eval(nodes[0])
    if len(value) != 75:
        raise ValueError("Keep all 75 actual run10 scientific source roles")
    return value


def parse_original_command(driver, record, command_path, repo):
    if (record.get("schema") != "public-actions-complete-run10-detached-closure-values-SO3-command-v1"
            or record.get("source_sha256") != LAUNCHER_SHA
            or record.get("driver_sha256") != DRIVER_SHA
            or record.get("github_run_id") != "45972294636"):
        raise ValueError("Use the whole actual run10 launcher command record")
    command = record.get("command")
    if (not isinstance(command, list) or len(command) < 4
            or not all(isinstance(v,str) for v in command)
            or command[1] != "-u"
            or Path(command[2]).resolve() != Path(driver.__file__).resolve()):
        raise ValueError("Keep the complete original Python driver command without eliding arguments")
    previous = list(sys.argv)
    try:
        sys.argv = [command[2], *command[3:]]
        args = driver.parse_args()
    finally:
        sys.argv = previous
    if Path(args.repo).resolve() != Path(repo).resolve():
        raise ValueError("The actual command repository and requested source checkout differ")
    expected_plan = args.outdir.with_name(args.outdir.name+"-command.json").resolve()
    if Path(command_path).resolve() != expected_plan:
        raise ValueError("Keep the original output/command pairing")
    return args


def _build_complete_original(args, driver, paths):
    # The following contiguous constructor block is byte-identical to c3dc main.
    SOURCE_PINS = driver.SOURCE_PINS
    actual_reference = driver.actual_reference
    preparation, reference_binding = actual_reference(args, paths)
    actual_public_scope=load('_actual_run10_public_reference_scope',paths['analytic_J3_binding'])
    if args.material_envelope_binding is None:
        raise ValueError('The whole actually returned run10 input binding is required')
    run10_input_binding=actual_public_scope.bind_actual_run10_input(args.material_envelope_binding,
        current_files=dict(current_reference_bundle=args.reference_bundle,
            current_preparation_report=args.preparation_report,current_carrier=args.carrier,
            current_node_report=args.node_report,current_scalar_input=args.scalar_input))
    reference = load('_so3_independent_axisymmetric_reference', paths['reference'])
    seed_reference = load('_so3_fixed_supported_unit_reference', paths['seed_reference'])
    seed_mean = load('_so3_complete_supported_mean_jets', paths['seed_mean'])
    meridian = load('_so3_actual_independent_axisymmetric_base', paths['meridian'])
    endpoint = load('_so3_independent_frozen_moment_zero_endpoint', paths['endpoint'])
    calibration = load('_so3_complete_reference_centred_calibration',paths['reference_calibration'])
    analytic_stage = load('_actual_complete_analytic_local_J3',paths['analytic_J3'])
    analytic_frame = load('_actual_complete_six_control_analytic_frame',paths['analytic_frame'])
    closure_values = load('_actual_complete_same_chain_closure_values',paths['closure_values'])
    stage_matrices = load('_actual_complete_detached_stage_matrices',paths['stage_matrices'])
    adjacent_matrices = load('_actual_complete_adjacent_frame_matrices',paths['adjacent_matrices'])
    frame_c1 = load('_so3_complete_same_graph_frame_C1',paths['frame_C1'])
    moment_binding = load('_so3_complete_frozen_moment_input', paths['frozen_moment_input'])
    new_moment_binding = load('_so3_explicit_new_reference_literal_Q', paths['new_moment_input'])
    geometry_module = load('_so3_complete_geometry_screen', paths['geometry'])
    spectral = load('_so3_same_spectral_loss', paths['spectral'])
    hessian = load('_so3_same_spectral_hessian', paths['hessian'])
    centered = load('_so3_same_centered_scalar', paths['centered'])
    qp = load('_so3_complete_QPv3', paths['qp'])
    root_packets = load('_actual_immutable_normal_root_packets', paths['root_packets'])
    history = load('_so3_complete_address_history', paths['history'])
    envelope_transfer = load('_actual_complete_envelope_transfer',paths['envelope_transfer'])
    envelope_memory = load('_so3_complete_material_envelope_memory',paths['envelope_memory'])
    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])
    meridian.torch.set_num_threads(args.torch_threads)
    meridian.torch.set_num_interop_threads(1)
    context = reference.AxisymmetricReferenceContext.from_files(repo=args.repo,
        reference_bundle=args.reference_bundle,carrier=args.carrier,node_report=args.node_report,
        scalar_input=args.scalar_input,preparation_report=args.preparation_report,panels=args.panels)
    reference_problem, reference_prepared = context.create_problem(N=args.angles,stage_block=args.stage_block)
    fixed_profile = context.scalar_identity
    if context.model != preparation['reference_definition']:
        raise ValueError('The actual complete reference changed between report and construction')
    seed_parameters = seed_reference.SeedParameters(
        relative_boundary_total_length=args.seed_boundary_total_length,
        profile_delta=args.seed_profile_delta,
        radial_quadrature_order=args.seed_radial_quadrature_order,
        profile_quadrature_order=args.seed_profile_quadrature_order,
        mean_maxiter=args.seed_mean_maxiter, mean_tolerance=args.seed_mean_tolerance,
        scalar_iterations=args.seed_scalar_iterations,
        mean_backtracks=args.seed_mean_backtracks, mean_armijo=args.seed_mean_armijo)
    base = meridian.ClosedMeridianOperator(reference_problem,reference_prepared,seed_reference,
        cache_directory=args.outdir/'fixed-supported-smooth-triangle-reference-cache',integration_order=args.integration_order,
        angle_block=args.angle_block,root_iterations=args.inverse_root_iterations,
        root_tolerance=args.inverse_root_tolerance,
        expected_parent_bundle_sha256=sha(args.reference_bundle),
        seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean)
    root_policy = endpoint.EndpointPolicy(endpoint_tolerance=args.endpoint_root_tolerance,
        maximum_iterations=args.endpoint_root_iterations,maximum_backtracks=args.endpoint_root_backtracks,
        armijo=args.endpoint_root_armijo,control_radius=args.endpoint_control_radius)
    normal_step_nodes = tuple(Fraction(i,args.normal_stages) for i in range(args.normal_stages+1))
    bubble_nodes = [[getattr(args, 'endpoint_bubble_'+str(i)+'_'+position)
        for position in ('left', 'middle', 'right')] for i in (1,2)]
    if args.moment_input_binding == 'supported-smooth-triangle-reference':
        origin = moment_binding.from_parameter_file(args.moment_input,
            input_sha256=args.moment_input_sha256,
            expected_definition_identity_sha256=args.moment_definition_sha256)
        frozen_moment_input = new_moment_binding.bind_new_input(origin,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile,
            initial_full_point_sha256=meridian.array_sha(base.initial()), bubble_nodes=bubble_nodes)
        moment_definition_identity = new_moment_binding.bind_to_base(frozen_moment_input,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile,
            initial_full_point_sha256=meridian.array_sha(base.initial()), bubble_nodes=bubble_nodes)
        moment_input_record = dict(mode='explicit fixed supported-smooth-triangle reference adopts complete published literal Q parameters',
            actual_parameter_file=file_record(args.moment_input),
            input_binding_source=file_record(paths['new_moment_input']),
            no_moment_or_inverse_recomputed=True, old_reference_or_initial_point_binding_inherited=False,
            same_mathematical_g_claimed=False, current_moment_inverse_property_claimed=False)
    else:
        if args.moment_trace_report is not None:
            frozen_moment_input = moment_binding.from_trace(args.repo, args.moment_trace_report,
                trace_report_sha256=args.moment_trace_report_sha256,
                failed_report=args.moment_failed_report,
                expected_definition_identity_sha256=args.moment_definition_sha256)
            moment_input_record = dict(mode='strict SAME reference actual trace word extraction',
                actual_trace_report=file_record(args.moment_trace_report),
                actual_failed_report=file_record(args.moment_failed_report),
                no_moment_or_inverse_recomputed=True)
        else:
            frozen_moment_input = moment_binding.from_parameter_file(args.moment_input,
                input_sha256=args.moment_input_sha256,
                expected_definition_identity_sha256=args.moment_definition_sha256)
            moment_input_record = dict(mode='strict SAME reference published complete parameter definition',
                actual_parameter_file=file_record(args.moment_input),
                no_moment_or_inverse_recomputed=True)
        moment_definition_identity = moment_binding.bind_to_base(frozen_moment_input,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile, bubble_nodes=bubble_nodes)
    q = endpoint.ZeroClosureOperator(base, expected_base_source_sha256=SOURCE_PINS['meridian'][1],
        expected_base_schema='complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1',
        bubble_nodes=bubble_nodes, frozen_moment_input=frozen_moment_input, endpoint_policy=root_policy,
        normal_step_nodes=normal_step_nodes,
        gamma_nodes=(args.gamma_left,args.gamma_middle,args.gamma_right),
        new_input_binder=(new_moment_binding if args.moment_input_binding == 'supported-smooth-triangle-reference' else None),
        reference_centering_module=calibration,frame_c1_module=frame_c1,stage_matrix_module=stage_matrices,
        adjacent_matrix_module=adjacent_matrices,analytic_stage_module=analytic_stage,
        analytic_frame_module=analytic_frame,closure_value_module=closure_values,
        evaluation_progress_path=args.outdir/'actual-normal-evaluation-progress.json')
    coordinates = meridian.RotationH2Coordinates(q, radial_length=args.radial_norm_length,
        angular_transition=args.angular_transition, norm_kind=args.norm_kind)

    return SimpleNamespace(q=q, base=base, coordinates=coordinates, context=context,
        meridian=meridian, endpoint=endpoint, packets=root_packets, seed=seed_reference,
        preparation=preparation, reference_binding=reference_binding,
        run10_input_binding=run10_input_binding, moment=frozen_moment_input,
        moment_identity=moment_definition_identity, paths=paths, args=args)


def verify_constructor_block(driver):
    source = Path(driver.__file__).read_text()
    begin = source.index("    preparation, reference_binding = actual_reference(args, paths)",
                         source.index("\ndef main():"))
    end = source.index("    restart = seed_report = None", begin)
    original = source[begin:end]
    if hashlib.sha256(original.encode()).hexdigest() != CONSTRUCTOR_BLOCK_SHA:
        raise ValueError("The complete actual q-constructor block differs")
    own = Path(__file__).read_text()
    here = own.index("    preparation, reference_binding = actual_reference(args, paths)",
                     own.index("\ndef _build_complete_original"))
    stop = own.index("\n    return SimpleNamespace(q=q", here)
    if own[here:stop] != original:
        raise ValueError("The new complete constructor must remain literal original code")


def _npz(used, record, descriptors=None):
    import numpy as np
    path = used.verify(record)
    with np.load(path, allow_pickle=False) as data:
        result = {key: np.array(data[key], copy=True) for key in data.files}
    if descriptors is not None:
        by_name = {d["name"]: d for d in descriptors}
        if len(by_name) != len(descriptors) or set(result) != set(by_name):
            raise ValueError("Keep the complete recorded array set")
        for name, value in result.items():
            d = by_name[name]
            if (list(value.shape) != d["shape"] or str(value.dtype) != d["dtype"]
                    or array_sha(value) != d["array_sha256"]):
                raise ValueError("A complete recorded array differs: "+name)
    for value in result.values():
        if value.dtype.kind == "f" and not np.isfinite(value).all():
            raise ValueError("An actual numerical input contains nonfinite words")
        value.setflags(write=False)
    used.verify(record)
    return result


def read_checkpoint(bound, path, raw, used):
    import numpy as np
    q = bound.q
    if raw.get("complete") is not True:
        raise ValueError("Only a genuinely complete scientific report owns a final checkpoint")
    path = Path(path).resolve()
    if path != Path(raw["final_bundle"]).resolve():
        raise ValueError("The requested checkpoint is not the report's actual final")
    record = used.add(path)
    if record["sha256"] != raw["final_bundle_sha256"]:
        raise ValueError("The actual final checkpoint whole bytes differ")
    arrays = _npz(used, record)
    if set(arrays) != CHECKPOINT_MEMBERS:
        raise ValueError("Keep every one of the 13 original checkpoint members")
    if (arrays["core"].shape != (q.M,) or arrays["omega_jets"].shape != (q.J,3,q.n)
            or arrays["Hcap"].shape != ()
            or arrays["working_integration_order"].dtype.kind not in ("i","u")
            or arrays["working_full_angles"].dtype.kind not in ("i","u")
            or arrays["mesh"].tobytes() != q.mesh.tobytes()
            or arrays["fixed_parent_core"].tobytes() != q.parent_core.tobytes()
            or any(arrays[k].dtype != np.dtype("float64") for k in
                ("core","omega_jets","Hcap","mesh","fixed_parent_core"))
            or int(arrays["working_integration_order"]) != q.integration_order
            or int(arrays["working_full_angles"]) != q.full_N
            or json.loads(str(arrays["endpoint_root_policy_json"].item())) != q.policy.metadata()):
        raise ValueError("Keep the complete checkpoint layout, working rule and root policy")
    point = q.load_checkpoint(path)
    core, omega, height = q.unpack(point)
    if (core.tobytes() != arrays["core"].tobytes()
            or omega.tobytes() != arrays["omega_jets"].tobytes()
            or np.array(height,dtype=np.float64).tobytes() != arrays["Hcap"].tobytes()):
        raise ValueError("The checkpoint did not reconstruct every free word exactly")
    digest = array_sha(point)
    final_geometry = raw.get("final_geometry") or {}
    if final_geometry.get("current_full_point_sha256") != digest:
        raise ValueError("The actual final field and its final geometry point differ")
    return point, dict(mode="actual-complete-thirteen-member-final",
        checkpoint=record, current_full_point_sha256=digest,
        final_report_complete=True, every_current_free_word_preserved=True)


def select_snapshot(raw, packets, used, model, *, mode, identity=None, point_sha=None):
    entries = (raw.get("normal_root_packets") or {}).get("snapshots", [])
    if not isinstance(entries, list):
        raise ValueError("Keep the actual ordered immutable packet snapshots")
    if identity is not None:
        candidates = [e for e in entries if e.get("snapshot_identity_sha256") == identity]
        if len(candidates) != 1:
            raise ValueError("The explicitly selected immutable snapshot is not in the report")
    elif point_sha is not None:
        candidates = [e for e in entries
            if e.get("summary",{}).get("current_full_point_sha256") == point_sha]
    else:
        candidates = [e for e in entries if
            e.get("summary",{}).get("all_required_angle_roots_recorded") is True
            and e.get("summary",{}).get("current_full_point_sha256") is not None]
    if not candidates:
        if mode == "final":
            return None, None
        raise ValueError("No actual complete selected field snapshot exists")
    selected = candidates[-1]
    snapshot = used.read_json(selected["snapshot_file"])
    summary = packets.validate_snapshot(snapshot, model=model,
        operator_source_sha256=NORMAL_SHA, caller_source_sha256=DRIVER_SHA,
        reread_packets=True, reread_arrays=True)
    if summary != selected["summary"]:
        raise ValueError("The immutable full-point snapshot differs from the scientific report")
    if point_sha is not None and summary["current_full_point_sha256"] != point_sha:
        raise ValueError("A root packet from another point cannot be transferred")
    return snapshot, copy.deepcopy(selected["snapshot_file"])


def restore_root_words(bound, snapshot, used, point_sha):
    import numpy as np
    if snapshot is None:
        return dict(restored_angle_count=0, existing_root_branch_words_reused=False,
            original_missing_roots_inferred=False, continuous_branch_certified=False)
    q, packets = bound.q, bound.packets
    before = array_sha(q._current_x)
    if before != point_sha or q._root_cache:
        raise ValueError("Root restoration starts only at the same complete empty current point")
    restored = []
    for item in snapshot["definition"]["angle_packets"]:
        angle = item["literal_angle_hex"]
        packet = used.read_json(item["packet_file"])
        packets.validate_packet(packet, model=q.model, operator_source_sha256=NORMAL_SHA,
            caller_source_sha256=DRIVER_SHA, point_sha256=point_sha, angle_hex=angle,
            reread_arrays=True)
        definition = packet["definition"]
        arrays = _npz(used,packet["arrays_file"],definition["arrays"])
        stages = []
        for index, entry in enumerate(definition["stages"],1):
            prefix = "stage_"+str(index).zfill(3)+"_"
            stage = {k: np.array(arrays[prefix+k], copy=True) for k in
                     ("eta","frame","controls","J")}
            for value in stage.values():
                value.setflags(write=False)
            name = entry["angular_matrix_array"]
            matrix = None if name is None else np.array(arrays[name],copy=True)
            if matrix is not None:
                matrix.setflags(write=False)
            stage.update(record=copy.deepcopy(entry["original_stage_record"]),
                frame_provenance=copy.deepcopy(entry["frame_provenance"]),
                jacobian=matrix, jacobian_order=entry["actual_cached_implicit_matrix_angular_order"])
            stages.append(stage)
        restored_item = dict(Z=np.array(arrays["Z"],copy=True),
            zero=np.array(arrays["zero"],copy=True), stages=stages,
            order=definition["actual_cached_angular_order"],
            record=copy.deepcopy(definition["original_root_record"]))
        for k in ("Z","zero"):
            restored_item[k].setflags(write=False)
        protection = q.adjacent_frames._root_protection([restored_item],[angle],restored_item["order"])
        if protection != definition["original_protected_root_fields_sha256"]:
            raise ValueError("Restoration changed a protected actual stage/control/frame word")
        if angle in q._root_cache:
            raise ValueError("An actual angle was repeated in the immutable full cache")
        q._root_cache[angle] = restored_item
        restored.append(dict(angle_hex=angle,packet=item["packet_file"],
            completed_angular_order=restored_item["order"]))
    if array_sha(q._current_x) != before:
        raise ValueError("Restoring recorded roots changed the outer point")
    return dict(restored_angle_count=len(restored), records=restored,
        existing_root_branch_words_reused=bool(restored),
        restored_lower_order_jets_are_not_fabricated_second_jets=True,
        matrix_words_only_when_originally_recorded=True,
        scientific_root_calls_during_restore=0, continuous_branch_certified=False)


def restore_fixed_seed(bound, raw, pure, used):
    import numpy as np
    seed = bound.base.parent_jet
    metadata = raw.get("latest_operator_metadata",{}).get("base_complete_metadata",{}).get(
        "fixed_supported_unit_seed")
    if not isinstance(metadata,dict):
        return dict(recorded_plan_available=False,restored_mean_angles=0,
            new_queries_use_complete_original_seed=True)
    if (metadata.get("model") != seed.model
            or metadata.get("model_identity_sha256") != seed.model_identity):
        raise ValueError("The fixed seed is not the same complete reference")
    diagnostics = pure.get("seed_diagnostics")
    if diagnostics is None or diagnostics.get("mean_batch_records") != metadata.get("mean_batch_records"):
        raise ValueError("The whole actual fixed-seed batch provenance differs from its pure read")
    plan = metadata.get("radial_plan")
    if plan is not None:
        arrays = _npz(used,plan["runner_raw_arrays"])
        description = used.read_json(plan["runner_raw_description"])
        if (set(arrays) != set(PLAN_KEYS)|{"model_identity","central_length","outside_integrals"}
                or str(arrays["model_identity"].item()) != seed.model_identity
                or description["seed_model_identity_sha256"] != seed.model_identity
                or canonical(description["pieces"]) != plan["pieces_identity_sha256"]
                or canonical(description["nodes"]) != plan["nodes_identity_sha256"]):
            raise ValueError("The complete actual fixed-seed radial plan changed")
        for name in PLAN_KEYS:
            declared = plan["arrays"][name]
            if (array_sha(arrays[name]) != declared["sha256"]
                    or list(arrays[name].shape) != declared["shape"]
                    or str(arrays[name].dtype) != declared["dtype"]):
                raise ValueError("A fixed-seed radial array differs: "+name)
        lc = float(arrays["central_length"])
        outside = arrays["outside_integrals"]
        if (lc.hex() != plan["central_length_carrier_hex"]
                or float(outside[0]).hex() != plan["outside_horizontal_integral_carrier_hex"]
                or float(outside[1]).hex() != plan["outside_vertical_integral_carrier_hex"]):
            raise ValueError("The actual fixed-seed total words changed")
        seed._plan = dict(arrays={k:arrays[k] for k in PLAN_KEYS},
            central_length=lc,outside_horizontal=float(outside[0]),
            outside_vertical=float(outside[1]),record=copy.deepcopy(plan))
    count = 0
    for batch in metadata["mean_batch_records"]:
        arrays = _npz(used,batch["runner_raw_arrays"])
        angles = batch["literal_angle_hex"]
        if (str(arrays["seed_model_identity"].item()) != seed.model_identity
                or [float(v).hex() for v in arrays["phi"]] != angles
                or batch["seed_model_identity_sha256"] != seed.model_identity):
            raise ValueError("The complete fixed-reference candidate batch changed")
        for name in MEAN_KEYS:
            value = arrays[name]
            expected = (len(angles),) if name.startswith("lambda") else (len(angles),3)
            if value.dtype != np.dtype("float64") or value.shape != expected:
                raise ValueError("Keep all twelve actual fixed-reference mean jet arrays")
        for i,angle in enumerate(angles):
            if angle in seed._mean_cache:
                raise ValueError("Do not silently select among duplicate fixed-reference candidates")
            seed._mean_cache[angle] = {}
            for name in MEAN_KEYS:
                value = np.array(arrays[name][i],copy=True)
                value.setflags(write=False)
                seed._mean_cache[angle][name] = value
            count += 1
        seed._mean_batches.append(copy.deepcopy(batch))
    return dict(recorded_plan_available=plan is not None,restored_mean_angles=count,
        source=copy.deepcopy(metadata), fixed_current_reference_not_old_2397=True,
        scientific_mean_root_calls_during_restore=0)


def restore_reference_calibration(bound, snapshot, used):
    import numpy as np
    if snapshot is None:
        return dict(restored_batches=0,existing_reference_words_reused=False)
    q = bound.q
    count = 0
    for item in snapshot["definition"]["actual_reference_calibration_files"]:
        record = item["original_complete_record"]
        arrays = _npz(used,item["immutable_copy"])
        if (set(arrays) != {"phi","core","cap","delta","model_identity","reference_point_sha256"}
                or str(arrays["model_identity"].item()) != q.identity
                or str(arrays["reference_point_sha256"].item())
                    != q.reference_calibration.reference_point_sha256):
            raise ValueError("A fixed-reference calibration belongs to another full model")
        keys = tuple(float(v).hex() for v in arrays["phi"])
        if (canonical(keys) != record["angle_list_sha256"] or len(keys) != record["angle_count"]
                or any(array_sha(arrays[name]) != digest
                       for name,digest in record["arrays_sha256"].items())
                or arrays["core"].shape != (3,len(keys),3)
                or arrays["cap"].shape != (3,len(keys),3)
                or arrays["delta"].shape != (len(keys),3,3)):
            raise ValueError("Keep the complete existing reference core/cap/defect batch")
        if keys in q.reference_calibration.cache:
            raise ValueError("Do not replace a prior frozen-reference calibration batch")
        Gamma = tuple(bound.meridian.tensor(arrays["core"][j]).detach() for j in range(3))
        P = tuple(bound.meridian.tensor(arrays["cap"][j]).detach() for j in range(3))
        # Its immutable copy has the same complete bytes. Runtime metadata names
        # the existing immutable file, rather than a possibly cleaned old cache.
        restored_record = dict(record,path=item["immutable_copy"]["path"],
            sha256=item["immutable_copy"]["sha256"],bytes=item["immutable_copy"]["bytes"])
        q.reference_calibration.cache[keys] = (Gamma,P,restored_record)
        count += 1
    return dict(restored_batches=count,existing_reference_words_reused=bool(count),
        scientific_reference_integrals_during_restore=0)


def restore_working_carrier(bound, raw, used):
    import numpy as np
    metadata = raw.get("normal_root_packets") or {}
    record = metadata.get("fixed_working_carrier")
    if record is None:
        return dict(original_packet_carrier_available=False,
            rebuilt_original_carrier_not_asserted_byte_equal=True)
    arrays = _npz(used,record["arrays_file"],record["arrays"])
    q = bound.q
    observed = dict(mesh=q.mesh,gauss_u=q.gauss_u,gauss_w=q.gauss_w,grid_phi=q.phi)
    for name in ("cells","local","s","widths","weights","h","hp","hpp"):
        value = q.integration_query[name]
        observed["integration_"+name] = (value.detach().cpu().numpy()
            if isinstance(value,bound.meridian.torch.Tensor) else value)
    if (set(observed) != set(arrays) or any(
            array_sha(observed[k]) != array_sha(arrays[k]) for k in observed)):
        raise ValueError("The complete original working integration carrier changed on reconstruction")
    return dict(original_packet_carrier_available=True,all_original_carrier_words_equal=True,
        arrays_file=copy.deepcopy(record["arrays_file"]))


class ActualField:
    def __init__(self, args):
        require_actions()
        if any(os.environ.get(k)!="1" for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")):
            raise ValueError("Reconstruct under the original launcher complete single-thread BLAS environment")
        import numpy as np
        self.np = np
        self.repo = Path(args.repo).resolve()
        self.topic = self.repo/TOPIC
        self.outdir = Path(args.outdir).resolve()
        if self.outdir == self.repo or self.repo in self.outdir.parents or self.outdir.exists():
            raise ValueError("Use one fresh scientific output directory outside the repository")
        self.outdir.mkdir(parents=True)
        self.used = VerifiedFiles()
        self.used.add(__file__)
        driver_path = self.topic/SCRIPT/DRIVER_NAME
        reader_path = self.topic/SCRIPT/READER_NAME
        if self.used.add(driver_path)["sha256"] != DRIVER_SHA or self.used.add(reader_path)["sha256"] != READER_SHA:
            raise ValueError("The complete actual driver and pure reader sources differ")
        self.driver = driver = load("_mesh_complete_actual_run10_driver",driver_path,DRIVER_SHA)
        self.reader = load("_mesh_complete_actual_run10_reader",reader_path,READER_SHA)
        self.pins = pins = source_pins(driver_path)
        if driver.SOURCE_PINS != pins:
            raise ValueError("The actual imported source registry changed")
        self.source_records = {}
        for role,(relative,digest) in pins.items():
            rec = self.used.add(self.topic/relative)
            if rec["sha256"] != digest:
                raise ValueError("Changed full scientific source role "+role)
            self.source_records[role] = rec
        self.raw, self.report_capture = capture_report(args.report,self.outdir/"input-scientific-report.json")
        frozen_report = self.report_capture["captured_copy"]
        self.used.verify(frozen_report)
        self.pure = self.reader.read_report(self.repo,frozen_report["path"],verify_final_bundle=False)
        if self.pure["report_sha256"] != frozen_report["sha256"]:
            raise ValueError("The complete pure reader consumed different scientific report bytes")
        raw = self.raw
        if (raw["source_sha256_by_role"] != {k:v[1] for k,v in pins.items()}
                or raw["source_sha256"] != DRIVER_SHA
                or raw["independent_fixed_target_definition_identity_sha256"] != TARGET_ID):
            raise ValueError("The current complete report is not the actual run10 fixed-target family")
        command_record = self.used.add(args.command)
        command = self.used.read_json(command_record)
        original = parse_original_command(driver,command,args.command,self.repo)
        if (command.get("source_commit") != raw.get("source_commit")
                or command.get("github_run_id") != raw.get("github_run_id")
                or command.get("workflow_trigger_commit") != raw.get("workflow_trigger_commit")):
            raise ValueError("Keep the actual launcher/driver source commit, run and trigger pairing")
        for role,(relative,digest) in pins.items():
            declared = command["closed_source_records"][role]
            if declared.get("sha256") != digest or declared.get("repo_relative_path") != str(Path(TOPIC)/relative):
                raise ValueError("The original launcher did not bind this complete source role")
        for record in command["actual_input_records"]:
            self.used.verify(record)
        if (Path(args.report).resolve() != (original.outdir/"report.json").resolve()
                or raw.get("bundle_sha256") != sha(original.reference_bundle)
                or raw.get("observation_carrier_sha256") != sha(original.carrier)):
            raise ValueError("Do not mix report, command and original input families")
        self.original_arguments = copy.deepcopy(vars(original))
        original.outdir = self.outdir/"field-reconstruction"
        original.outdir.mkdir()
        paths = {role:self.topic/relative for role,(relative,_) in pins.items()}
        verify_constructor_block(driver)
        self.bound = bound = _build_complete_original(original,driver,paths)
        self.q, self.context = bound.q,bound.context
        q = self.q
        if (q.model != raw["representation"] or q.identity != raw["model_identity_sha256"]
                or bound.coordinates.record != raw["coordinate_norm"]
                or q.base.model["complete_axisymmetric_reference_model"] != bound.context.model
                or bound.context.identity != REFERENCE_ID
                or bound.run10_input_binding != raw["actual_public_reference_input_binding"]
                or bound.run10_input_binding["actual_binding_file"]["sha256"] != INPUT_BINDING_SHA
                or q.base.model["fixed_chart_core_sha256"] != CHART_SHA
                or q.free_size != raw["original_variables"]
                or (q.M,q.J,q.full_N,q.normal_stage_count) != (160,923,2048,32)):
            raise ValueError("Reconstruction changed the complete field/model/norm/reference/target/layout")
        import scipy
        working = raw["working_evaluation"]
        if (working["numpy_version"] != np.__version__
                or working["scipy_version"] != scipy.__version__
                or working["torch_version"] != bound.meridian.torch.__version__
                or working["torch_threads"] != original.torch_threads):
            raise ValueError("Keep the complete actual numerical library/thread environment")
        if raw["working_evaluation"]["integration_order"] != q.integration_order:
            raise ValueError("Keep the complete original quadrature, not a silently changed numerical field")
        for record in bound.run10_input_binding["complete_current_input_files"].values():
            self.used.verify(record)
        self.used.verify(bound.run10_input_binding["actual_binding_file"])
        if bound.context.preparation["true_scalar"]["integral_leaves"] != CURRENT_SCALAR_LEAVES:
            raise ValueError("Retain the genuinely recorded current run10 scalar table")
        snapshot_identity = getattr(args,"snapshot_identity_sha256",None)
        if args.point_source == "final":
            if snapshot_identity is not None:
                raise ValueError("Select a final checkpoint or a named immutable point, not both")
            chosen = args.checkpoint if args.checkpoint is not None else raw.get("final_bundle")
            if chosen is None:
                raise ValueError("No actual final checkpoint was returned")
            self.x, self.point_binding = read_checkpoint(bound,chosen,raw,self.used)
            self.snapshot,self.snapshot_record = select_snapshot(raw,bound.packets,self.used,q.model,
                mode="final",point_sha=array_sha(self.x))
        else:
            if args.checkpoint is not None:
                raise ValueError("A snapshot point does not borrow a different final checkpoint")
            self.snapshot,self.snapshot_record = select_snapshot(raw,bound.packets,self.used,q.model,
                mode="packet",identity=snapshot_identity)
            p = self.snapshot["definition"]["current_point_file"]
            self.x = np.array(_npz(self.used,p["arrays_file"],[p["array"]])["x"],copy=True)
            self.point_binding = dict(mode="actual-immutable-complete-point-snapshot",
                snapshot_file=self.snapshot_record,
                snapshot_identity_sha256=self.snapshot["snapshot_identity_sha256"],
                current_full_point_sha256=p["current_full_point_sha256"],
                field_acceptance_inferred_from_packet=False,every_current_free_word_preserved=True)
        self.point_sha = array_sha(self.x)
        if (self.x.dtype != np.dtype("float64") or self.x.shape != (q.free_size,)
                or not np.isfinite(self.x).all() or self.point_sha != self.point_binding["current_full_point_sha256"]):
            raise ValueError("Keep all original finite current free words")
        q.unpack(self.x)
        q._select_point(self.x)
        self.seed_restore = restore_fixed_seed(bound,raw,self.pure,self.used)
        self.carrier_restore = restore_working_carrier(bound,raw,self.used)
        self.root_restore = restore_root_words(bound,self.snapshot,self.used,self.point_sha)
        self.calibration_restore = restore_reference_calibration(bound,self.snapshot,self.used)
        self.domain = q.domain(self.x)
        self.x.setflags(write=False)
        self.core,self.omega,self.height = q.unpack(self.x)
        self.used.protect(self.outdir/"meshes")
        self.deep,self.scalar_reconstruction = _restore_actual_scalar(self.context)
        self.target_cache = {}
        self.initial_operator_metadata = q.metadata()
        self.binding = dict(schema=SCHEMA,source_sha256=sha(__file__),
            source_commit=subprocess.check_output(["git","-C",str(self.repo),"rev-parse","HEAD"],text=True).strip(),
            github_run_id=os.environ.get("GITHUB_RUN_ID"),github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
            actual_source_commit=raw["source_commit"],actual_scientific_run_id=raw["github_run_id"],
            actual_workflow_trigger_commit=raw["workflow_trigger_commit"],
            original_launcher_numerical_environment={k:os.environ[k]
                for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")},
            scientific_report_capture=self.report_capture,
            original_complete_command=command_record,original_full_argv=command["command"],
            source_roles=self.source_records,complete_model=q.model,model_identity_sha256=q.identity,
            fixed_target_definition_identity_sha256=TARGET_ID,
            complete_actual_public_input_binding=bound.run10_input_binding,
            fixed_scalar_metric=raw["fixed_scalar_metric"],reference_model_identity_sha256=REFERENCE_ID,
            point=self.point_binding,point_sha256=self.point_sha,
            current_height_hex=self.height.hex(),M=q.M,J=q.J,N=q.full_N,
            original_variables=q.free_size,normal_stages=q.normal_stage_count,
            complete_original_coordinate_norm=raw["coordinate_norm"],
            complete_original_working_evaluation=raw["working_evaluation"],
            original_constructor_block_sha256=CONSTRUCTOR_BLOCK_SHA,
            root_restoration=self.root_restore,seed_restoration=self.seed_restore,
            reference_calibration_restoration=self.calibration_restore,
            working_carrier_restoration=self.carrier_restore,
            current_scalar_reconstruction=self.scalar_reconstruction,
            immutable_consumed_file_records=[copy.deepcopy(self.used.records[k])
                for k in sorted(self.used.records)],
            original_frozen_reference_and_current_point_separate=True,
            full_raw_h_Delta_and_all_sixjets_retained=True,
            original_optimizer_reexecuted=False,solution_frequency_or_controls_changed=False,
            continuous_branch_certified=False,continuous_mesh_error_certified=False)
        self.binding_identity = canonical(self.binding)
        atomic_json(self.outdir/"complete-field-binding.json",
            dict(definition=self.binding,definition_identity_sha256=self.binding_identity))
        self.used.recheck()

    def target_radius(self, cell, local):
        key = (int(cell),float(local).hex())
        if key not in self.target_cache:
            definition = self.bound.context.modules["deep_scalar"]
            ref = sys.modules[self.bound.context.__class__.__module__]
            pair = ref.point_definition(self.context.nodes,int(cell),float(local))
            interval = ref.target_a_box(self.context.full,self.deep,definition,pair)
            value,error = ref.midpoint_and_error(interval,definition.SCALE)
            if not math.isfinite(value) or value <= 0 or not math.isfinite(error) or error < 0:
                raise ValueError("The same exact fixed target has no positive finite radius carrier here")
            self.target_cache[key] = (value,error)
        return self.target_cache[key]

    def recheck(self):
        if array_sha(self.x) != self.point_sha or self.q._current_point_sha256 != self.point_sha:
            raise ValueError("A mesh evaluation changed the actual complete current point")
        self.used.recheck()


def counted_tail_class(deep_module):
    """New controller; inherited exact definition and all scalar kernels stay original."""
    class ReconstructedTail(deep_module.DeepValleyTail):
        def __init__(self, full, *, original_input_identity, target_leaves,
                     epsilon, integral_tolerance, historical_clock_seconds):
            self.reconstruction_leaf_target = int(target_leaves)
            if self.reconstruction_leaf_target < 1:
                raise ValueError('A real positive recorded live-leaf count is required')
            super().__init__(full, input_identity=original_input_identity,
                epsilon=epsilon, integral_tolerance=integral_tolerance,
                admission_seconds=historical_clock_seconds)

        def _build_integral_table(self):
            # The original e091 table body is preserved below except that its
            # wall-clock admission comparison is replaced by the observed
            # live-leaf count.  All per-leaf operations and tie order are exact.
            tail = self._tail_integrals(self.epsilon)
            points = sorted(set((self.epsilon,F(1,8),F(1,4))))
            live,heap,sequence = {},[],0
            total = list(tail)
            def admit(leaf):
                nonlocal sequence
                sequence += 1
                live[sequence] = leaf
                width = sum(value[1]-value[0] for value in leaf['values'])
                heapq.heappush(heap,(-width,sequence))
                for j in range(2):
                    total[j] = deep_module.add(total[j],leaf['values'][j])
            for low,high in zip(points,points[1:]):
                admit(self._leaf(low,high))
            count = len(live)
            while heap:
                uncertainty = max(F(value[1]-value[0],deep_module.SCALE)*self.width
                                  for value in total)
                if uncertainty <= self.integration_tolerance:
                    break
                if len(live) >= self.reconstruction_leaf_target:
                    break
                _,key = heapq.heappop(heap)
                leaf = live.pop(key)
                for j in range(2):
                    total[j] = (total[j][0]-leaf['values'][j][0],
                                total[j][1]-leaf['values'][j][1])
                middle = (leaf['low']+leaf['high'])/2
                admit(self._leaf(leaf['low'],middle))
                admit(self._leaf(middle,leaf['high']))
                count += 2
            self.leaves = sorted(live.values(),key=lambda leaf:leaf['low'])
            self.total_integrals_dimensionless = tuple(total)
            self.leaves_evaluated = count
            self.integral_uncertainty = max(F(value[1]-value[0],deep_module.SCALE)*self.width
                                            for value in total)
            self.requested_integral_accuracy_reached = (
                self.integral_uncertainty <= self.integration_tolerance)
            if len(self.leaves) != self.reconstruction_leaf_target:
                raise ArithmeticError('The original accuracy stop preceded the recorded leaf count')
    return ReconstructedTail



def _restore_actual_scalar(context):
    """Reconstruct the actual CURRENT table, not the historical 2397-leaf input."""
    require_actions()
    d=context.modules["deep_scalar"]
    if sha(d.__file__)!=DEEP_SHA or sha(d.DeepValleyTail.metadata.__code__.co_filename)!=DEEP_SHA:
        raise ValueError("Use the whole original exact scalar and all its integral methods")
    report=context.preparation
    actual=report.get("true_scalar")
    if (not isinstance(actual,dict) or actual.get("definition")!=context.scalar_definition
            or actual.get("model_identity_sha256")!=context.scalar_identity
            or canonical(actual["definition"])!=context.scalar_identity
            or actual.get("all_tail_domain_included") is not True
            or actual.get("unresolved_oscillations_dropped") is not False
            or type(actual.get("requested_integral_accuracy_reached")) is not bool
            or type(actual.get("integral_leaves")) is not int or actual["integral_leaves"]<1
            or type(actual.get("integral_leaves_evaluated")) is not int):
        raise ValueError("Read the complete actual current preparation scalar definition and result")
    scalar_class=counted_tail_class(d)
    started=time.monotonic()
    deep=scalar_class(context.full,
        original_input_identity=copy.deepcopy(context.scalar_definition["original_input"]),
        target_leaves=actual["integral_leaves"],
        epsilon=F(actual["infinite_tail_cutoff_exact"]),
        integral_tolerance=F(actual["requested_integral_width_exact"]),
        historical_clock_seconds=actual["admission_seconds"])
    observed=deep.metadata()
    left={k:v for k,v in observed.items() if k!="elapsed_seconds"}
    right={k:v for k,v in actual.items() if k!="elapsed_seconds"}
    if left!=right:
        differing=sorted(k for k in set(left)|set(right) if left.get(k)!=right.get(k))
        raise ValueError("The reconstructed CURRENT complete scalar table differs from actual preparation: "+repr(differing))
    if (deep.definition!=context.scalar_definition
            or deep.model_identity_sha256!=context.scalar_identity
            or observed["integral_leaves"]!=actual["integral_leaves"]
            or observed["requested_integral_accuracy_reached"]!=actual["requested_integral_accuracy_reached"]):
        raise ValueError("A table carrier cannot redefine the fixed scalar target or its actual accuracy status")
    return deep,dict(schema="actual-current-preparation-scalar-table-reconstruction-v1",
        source_sha256=sha(__file__),original_scalar_source_sha256=DEEP_SHA,
        complete_actual_preparation_scalar=copy.deepcopy(actual),
        actual_current_leaf_count=actual["integral_leaves"],
        actual_current_leaf_evaluation_count=actual["integral_leaves_evaluated"],
        current_table_metadata_equal_except_elapsed=True,
        original_accuracy_status_preserved=actual["requested_integral_accuracy_reached"],
        actual_reconstruction_seconds=time.monotonic()-started,
        historical_2397_table_used_as_current=False,
        exact_fixed_scalar_definition_unchanged=True,
        achieved_accuracy_threshold_not_inferred_from_leaf_count=True)




def write_exact_frequency_input(field, directory):
    """Actual complete M160 words -> exact zero inclusion in M320, not a solve."""
    require_actions()
    np = field.np
    directory = Path(directory)
    directory.mkdir(parents=True,exist_ok=False)
    q = field.q
    if (q.M,q.n,q.J,q.K) != (160,482,923,3):
        raise ValueError("This explicit exact coefficient inclusion is for the whole bound run10 layout")
    core,omega,height = q.unpack(field.x)
    Mnew = 320
    nnew = 3*Mnew+2
    new_core = np.zeros(Mnew,dtype=np.float64)
    new_core[:q.M] = core
    new_omega = np.zeros((q.J,3,nnew),dtype=np.float64)
    routes = ((0,q.M+1,0),(q.M+1,2*(q.M+1),Mnew+1),
              (2*(q.M+1),3*q.M+2,2*(Mnew+1)))
    for old_start,old_end,new_start in routes:
        new_omega[:,:,new_start:new_start+old_end-old_start] = omega[:,:,old_start:old_end]
        if (new_omega[:,:,new_start:new_start+old_end-old_start].tobytes()
                != omega[:,:,old_start:old_end].tobytes()):
            raise AssertionError("Exact frequency inclusion changed an original working coefficient")
    if new_core[:q.M].tobytes() != core.tobytes():
        raise AssertionError("Exact core coefficient inclusion changed an original word")
    used = np.zeros(nnew,dtype=bool)
    for a,b,c in routes:
        used[c:c+b-a] = True
    if np.any(new_omega[:,:,~used]) or np.any(new_core[q.M:]):
        raise AssertionError("Every added frequency coefficient must be literal positive zero")
    # Original same-model complete checkpoint is independently useful to a
    # future genuine source-specific transfer. Its archive bytes are new;
    # it is not relabelled as the old final checkpoint's whole SHA.
    current_checkpoint = directory/"actual-selected-run10-thirteen-member-point.npz"
    q.save(current_checkpoint,field.x)
    path = directory/"actual-M160-to-M320-exact-coefficient-inclusion.npz"
    np.savez(path,schema=np.array("exact-coefficient-zero-inclusion-input-only-v1"),
        original_full_point=field.x,current_core=core,current_omega=omega,
        included_core=new_core,included_omega=new_omega,height=np.array(height,dtype=np.float64),
        frozen_reference_core=q.parent_core,original_mesh=q.mesh,
        source_point_sha256=np.array(field.point_sha),
        original_model_identity_sha256=np.array(q.identity),
        fixed_target_definition_identity_sha256=np.array(TARGET_ID))
    definition = dict(schema="actual-run10-same-target-frequency-refinement-input-v1",
        source_sha256=sha(__file__),source_point_sha256=field.point_sha,
        original_complete_model=q.model,original_model_identity_sha256=q.identity,
        fixed_target_definition_identity_sha256=TARGET_ID,
        complete_fixed_reference_model=field.context.model,
        fixed_scalar_metric_identity_sha256=field.context.scalar_identity,
        original_current_M=160,requested_current_M=320,unchanged_reference_M=160,
        original_and_retained_J=923,original_and_retained_N=2048,
        current_coefficient_layout=dict(x_odd=[0,160],y_odd=[0,160],z_even=[1,160]),
        included_coefficient_layout=dict(x_odd=[0,320],y_odd=[0,320],z_even=[1,320]),
        source_to_included_slices=[dict(old_start=a,old_end=b,new_start=c) for a,b,c in routes],
        included_arrays_file=file_record(path),actual_same_model_checkpoint=file_record(current_checkpoint),
        original_scientific_report_capture=field.report_capture,
        original_history_from_full_captured_report_retained=True,
        original_root_packets=field.snapshot_record,
        physical_height_word_unchanged=True,all_old_coefficients_byte_preserved=True,
        all_added_coefficients_exactly_positive_zero=True,
        whole_original_shared_quintic_jets_retained=True,
        exact_outer_omega_and_core_functions_unchanged_by_zero_inclusion=True,
        fixed_reference_chart_not_extended_from_current_core=True,
        normal_six_controls_and_all_32_stages_not_removed=True,
        actual_new_frequency_field_evaluated=False,
        numerical_new_frequency_root_branch_or_objective_inherited=False,
        new_coordinate_norm_or_damping_inherited=False,
        ready_to_replace_source_specific_refined_model_validation=False,
        continuous_root_branch_equivalence_certified=False,
        nonlinear_same_g_frequency_refinement_convergence_claimed=False,
        required_next_source_specific_responsibility=[
            "A complete refined family must bind this actual current run10 target and fixed reference.",
            "Its full source-specific model/initial-layout/point/typed-history transfer must validate these whole inputs.",
            "It must reread its complete field, original and enlarged positive rows, metric objective and full geometry.",
            "Zero inclusion supplies an exact same-function candidate; it is not evidence that any refined nonlinear solve ran."])
    record_path = directory/"frequency-refinement-input.json"
    atomic_json(record_path,dict(definition=definition,definition_identity_sha256=canonical(definition)))
    field.recheck()
    return dict(input_definition=file_record(record_path),definition_identity_sha256=canonical(definition),
        coefficient_file=file_record(path),actual_same_model_checkpoint=file_record(current_checkpoint),
        current_M=160,requested_M=320,unchanged_fixed_reference_M=160,
        actual_new_frequency_field_evaluated=False,nonlinear_refinement_completed=False)
