#!/usr/bin/env python3
"""Refine the accepted q122 M28 field at the same physical metric in M32.

This is a fresh specialization of the archived exact raw spectral entry.
All 28 prefix modes and all 28 tail Q/pi modes are embedded without resampling;
the four new modes start at zero and are explicitly unsolved. The old full-flow
Jacobian snapshot is not reused across dimensions. The original full-flow
worker and its exact-input stage cache then evaluate the complete new M32
problem with every original Newton/Jacobian/RMS/physical-BC/audit gate.

The physical profile, complete piecewise geometry, reference angular chart,
numerical radial chart, phase, calibration data and tail quadrature are frozen.
Prefix angular 1024->1280 and M28->M32 are numerical representation changes.
Preparation and live-prefix preflight cannot create an accepted numerical result.
No original Python or MJS source is changed.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import ast
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ORIGINAL = 'strong_sameg_spectral_refinement.py'
ORIGINAL_SHA = '65e81c73707c6f094ce5d494965d2fd468e971f4fa450d88513cf4ac622476fd'
EXTRA = {
    'strong_full_tangent_tail_client.py': '9ee68e2af6578f357535317abdf4bbb89dc96e783782c3e66914e83fdbedf045',
    'strong_full_tangent_tail_worker.mjs': '2a0a93902999f244a838effd4ae09930f456f0a97393416bacb1554c075c1653',
    'strong_full_flow_tangent_storage.mjs': 'fb6ed25102cb91a332e1c2d879cf6218f9c88faaebe6916e801e46e6f8c1551f',
    'strong_full_tangent_resource_guard.py': 'bb7b1c863f8fef204131bf7fe1acc063c5ce074e46e04a8332bb2e96453255fd',
    'geometric-checkpoint-core-pullback.py': 'd319574d946f2f6c465b76ffeb92117201aa95bc4318e7100377b184a530fa33',
}
IO_KEYS = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def plain(value):
    if hasattr(value, 'tolist'):
        return plain(value.tolist())
    if isinstance(value, dict):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(v) for v in value]
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    raise TypeError('Unsupported physical segment data: '+str(type(value)))


def canonical(value):
    return json.dumps(plain(value), sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def write_same(path, value, compressed=False):
    raw = (json.dumps(plain(value), indent=2, allow_nan=False)+'\n').encode()
    data = gzip.compress(raw, mtime=0) if compressed else raw
    if len(data) >= 5_000_000:
        raise ValueError('Single archival file limit exceeded')
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data:
            raise FileExistsError('Different immutable M32 preparation: '+str(path))
    else:
        with path.open('xb') as stream:
            stream.write(data)
    return dict(file=str(path), sha256=sha(path), bytes=len(data))


def spectral_tail_warm(tail, old_height, modes, out, config):
    import numpy as np
    old = tail['response']['checkpoint']
    if old['parameters']['modes'] != 28 or modes != 32:
        raise ValueError('This new tail guess must be the declared 28-to-32 embedding')
    states = np.asarray(old['states'], dtype=np.float64)
    raw_node = np.asarray(old['rawNode'], dtype=np.int64)
    old_h = np.asarray(old['cutHeight'], dtype=np.float64)
    if (states.shape != (577, 56) or raw_node.tolist() != list(range(0, 577, 72))
            or np.asarray(old['rawStates'], dtype=np.float64).tobytes() != states[raw_node].tobytes()
            or old_h.tobytes() != np.asarray(old_height, dtype=np.float64).tobytes()
            or old['parameters']['depth'] != 576 or old['parameters']['physicalDepth'] != 8
            or old['parameters']['quadrature'] != 512):
        raise ValueError('Complete accepted old shooting grid or H differs')
    mapping = np.r_[np.arange(28), 32+np.arange(28)]
    new = np.zeros((577, 64), dtype=np.float64)
    new[:, mapping] = states
    height = np.full(32, -0., dtype=np.float64)
    height[:28] = old_h
    if new[:, mapping].tobytes() != states.tobytes() or height[:28].tobytes() != old_h.tobytes():
        raise ValueError('Old complete tail state or H bits changed')
    parameters = copy.deepcopy(old['parameters'])
    parameters['modes'] = modes
    changed = [k for k in set(parameters)|set(old['parameters'])
               if canonical(parameters.get(k)) != canonical(old['parameters'].get(k))]
    if changed != ['modes']:
        raise ValueError('A parameter other than unknown-function mode count changed')
    source = out.with_name(out.name+'-spectral-tail-zero-warm.json.gz')
    seed = dict(scope='Unsolved exact Q/pi spectral embedding only. Original current-H solve and full audit required.',
        parameters=parameters, states=new.tolist(), rawNode=raw_node.tolist(), rawStates=new[raw_node].tolist(),
        cutHeight=height.tolist(), numerical_solution_accepted=False, warm_only=True,
        source_mode_count=28, target_mode_count=32,
        full_flow_tangent_snapshot_transferred=False, original_Q_pi_and_H_bits_preserved=True,
        old_Q_pi_f64le_sha256=hashlib.sha256(states.astype('<f8').tobytes()).hexdigest(),
        new_Q_pi_f64le_sha256=hashlib.sha256(new.astype('<f8').tobytes()).hexdigest(),
        no_resampling_no_geometric_remesh_no_ODE=True)
    record = write_same(source, seed, compressed=True)
    decoded = json.loads(gzip.decompress(source.read_bytes()))
    if (np.asarray(decoded['states'], dtype=np.float64).tobytes() != new.tobytes()
            or np.asarray(decoded['cutHeight'], dtype=np.float64).tobytes() != height.tobytes()):
        raise ValueError('Unsolved spectral warm JSON did not preserve bits')
    write_same(out.with_name(out.name+'-spectral-tail-zero-warm-provenance.json'), dict(
        scope=__doc__, source_tail_config=config, original_checkpoint_parameters=old['parameters'],
        source_full_flow_snapshot_present=bool(tail['response'].get('fullFlowTangentSnapshot')),
        old_snapshot_deliberately_not_reused_across_mode_count=True,
        old_tail_not_a_new_tail_response=True, new_seed=record,
        state_row_mapping=mapping.tolist(), old_state_shape=list(states.shape), new_state_shape=list(new.shape),
        unchanged_all_non_mode_parameters=True, original_raw_node_order_unchanged=True,
        original_Q_pi_and_H_bits_preserved=True, all_new_modes_exactly_zero=True,
        new_mode_residual_Jacobian_audit_or_acceptance_not_computed=True))
    return source


def live_metric_identity(obj, saved, args, out, diagnostic):
    import numpy as np
    flow = obj.flow()
    pb = load('strong_m32_sameg_original_pullback', HERE/'geometric-checkpoint-core-pullback.py')
    reference_path = Path(sys.argv[sys.argv.index('--fixed-reference')+1]) if '--fixed-reference' in sys.argv else None
    # The production parser removes --fixed-reference in a nested adapter.
    reference_path = LIVE_REFERENCE
    old, unused = pb.load_saved(reference_path, Path(args.source_topic), Path(args.port),
                                angular=int(saved['config']['angular']))
    if any(saved['frozen_profile'].get(k, 0.) != 0. for k in ('initial_speed_pulse', 'initial_speed_frontload')):
        raise ValueError('This q122 same-g specialization preserves only the actual zero-weight law')
    before = dict(prefix=plain(old.flow._alternative_neck.segments), bridge=plain(old.flow.bridge.segments))
    after = dict(prefix=plain(flow._alternative_neck.segments), bridge=plain(flow.bridge.segments))
    if canonical(before) != canonical(after):
        raise ValueError('A physical polynomial/angle segment or phase changed')
    grid = np.unique(np.r_[flow.breaks,
        (flow.breaks[:-1, None]+np.diff(flow.breaks)[:, None]*np.array([.125, .375, .625, .875])).ravel()])
    for actual, original in zip(flow.profile(grid), old.flow.profile(grid)):
        if np.asarray(actual, dtype=np.float64).tobytes() != np.asarray(original, dtype=np.float64).tobytes():
            raise ValueError('Original metric a/as/ass callback changed')
    if (flow.cfg != old.flow.cfg or flow.end != old.flow.end
            or flow.general_core_chart.coefficients.tobytes() != old.flow.general_core_chart.coefficients.tobytes()
            or flow.general_core_chart.frequencies.tobytes() != old.flow.general_core_chart.frequencies.tobytes()):
        raise ValueError('Original profile, length, or material coordinate changed')
    record = dict(scope='Real M32 prefix constructor identity, before any tail worker or Newton.',
        original_reference=str(reference_path), original_reference_sha256=sha(reference_path),
        complete_profile_identical=True, all_prefix_and_bridge_segments_identical=True,
        all_segment_phase_and_coefficients_identical=True, a_as_ass_callback_samples_bitwise_equal=True,
        sampled_s=grid.tolist(), complete_segment_structure_sha256=hashlib.sha256(canonical(before)).hexdigest(),
        physical_segments=before, original_material_chart_identical=True,
        original_numerical_reference_identical=True, original_physical_length_identical=True,
        old_modes=28, new_modes=32, old_angular=1024, new_angular=1280,
        tail_quadrature_unchanged=512, tail_worker_started=False, bvp_solved=False,
        full_core_warm_embedding_in_original_raw_report=True,
        later_live_tail_still_requires_original_frozen_profile_fingerprint_gates=True)
    link = write_same(out.with_name(out.name+'-live-physical-identity.json'), record)
    diagnostic['live_physical_metric_identity'] = link


class PreflightFinished(BaseException):
    pass


def resource_class(Base, heap, young):
    from strong_full_tangent_resource_guard import resource_port_class
    Resource = resource_port_class(Base, heap, young)
    class SeedResource(Resource):
        def __init__(self, *args, **kwargs):
            prefix = Path(kwargs.get('record_prefix', args[2] if len(args)>2 else ''))
            key = 'VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX'
            previous = os.environ.get(key)
            os.environ[key] = str(prefix.resolve())+'-exact-stage-seed'
            try:
                super().__init__(*args, **kwargs)
            finally:
                if previous is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = previous
    return SeedResource


def build():
    path = HERE/ORIGINAL
    if sha(path) != ORIGINAL_SHA:
        raise ValueError('Archived original exact spectral entry differs')
    for name, expected in EXTRA.items():
        if sha(HERE/name) != expected:
            raise ValueError('Frozen storage or physical interface differs: '+name)
    source = path.read_text()
    tree = ast.parse(source)
    start, end = tree.body[0].lineno-1, tree.body[0].end_lineno
    lines = source.splitlines(keepends=True)
    source = ''.join(lines[:start])+repr(__doc__)+'\n'+''.join(lines[end:])
    edits = [
        ('if (Mnew,Nnew)!=(28,1024) or old_heap<=0:', 'if (Mnew,Nnew)!=(32,1280) or old_heap<=0:'),
        ("report.get('original_parameter_count')!=27 or report.get('fixed_parameter_count')!=24", "report.get('original_parameter_count')!=31 or report.get('fixed_parameter_count')!=28"),
        ("if M!=24 or saved['modes']!=M or not ident['fixed'] or target_tol!=ident['tol']:", "if M!=28 or saved['modes']!=M or not ident['fixed'] or target_tol!=ident['tol']:"),
        ("if cfg0['modes']!=24 or cfg0['spacing']!=2 or cfg0['quadrature']!=512:", "if cfg0['modes']!=28 or cfg0['spacing']!=2 or cfg0['quadrature']!=512:"),
        ('    cfg=copy.deepcopy(cfg0);cfg[\'modes\']=Mnew\n', "    spectral_tail_seed=SPECTRAL_TAIL_BUILDER(tail,old_H,Mnew,out,cfg0)\n    cfg=copy.deepcopy(cfg0);cfg['modes']=Mnew\n"),
        ('cfg.update(initialCheckpoint=str(own.spectral_warm_tail.resolve()),', 'cfg.update(initialCheckpoint=str(spectral_tail_seed.resolve()),'),
        ("add_exact(remaining,'--radial-batch-size',8)", "add_exact(remaining,'--radial-batch-size',48)"),
        ("add_exact(remaining,'--collocation-batch-size',12)", "add_exact(remaining,'--collocation-batch-size',24)"),
        ("add_exact(remaining,'--point-cache-limit',2)", "add_exact(remaining,'--point-cache-limit',8)"),
        ("        loaded=old_loader(name,path)\n        if Path(path).name=='tail_frozen_client.py':\n", "        loaded=old_loader(name,path)\n        if Path(path).name=='tail_frozen_client.py':\n            loaded=old_loader(name+'_m32_full_flow',HERE/'strong_full_tangent_tail_client.py')\n"),
        ("        atomic_new_or_same(out.with_name(out.name+'-spectral-warm-verified.json'),diagnostic)", "        SPECTRAL_LIVE_IDENTITY(obj,saved,args,out,diagnostic)\n        atomic_new_or_same(out.with_name(out.name+'-spectral-warm-verified.json'),diagnostic)"),
        ('        record=document(warm_path)\n        return sol,record', '        record=document(warm_path)\n        if SPECTRAL_LIVE_PREFLIGHT: raise SPECTRAL_PREFLIGHT_FINISHED()\n        return sol,record'),
        ("source_sha256={**EXPECTED_SOURCE_SHA256,Path(__file__).name:SELF_SHA},", "source_sha256={**EXPECTED_SOURCE_SHA256,**M32_EXTRA_SOURCES,Path(__file__).name:SELF_SHA},"),
        ("        node_old_heap_MiB=old_heap,node_young_semi_space_MiB=own.spectral_node_young_space,", "        node_old_heap_MiB=old_heap,node_young_semi_space_MiB=own.spectral_node_young_space,\n        new_unsolved_tail_seed=dict(file=str(spectral_tail_seed),sha256=digest(spectral_tail_seed)),\n        original_spectral_source_sha256=M32_ORIGINAL_SOURCE_SHA,\n        explicit_full_flow_storage_client=True,old_M_snapshot_not_transferred=True,\n        live_prefix_preflight_only=SPECTRAL_LIVE_PREFLIGHT,"),
    ]
    applied = []
    for before, after in edits:
        if source.count(before) != 1:
            raise ValueError('Original M32 specialization anchor is not unique: '+repr(before))
        source = source.replace(before, after, 1)
        applied.append(dict(before=before, after=after, count=1))
    # Update only diagnostic text, never numeric code or hashes.
    for before, after in [
        ('explicitly M28/N1024', 'explicitly M32/N1280'), ('real 27-to-24', 'real 31-to-28'),
        ('original fixed M24', 'original fixed M28'), ('original 24 core modes', 'original 28 core modes'),
        ('genuine M28 Fixed/Actual', 'genuine M32 Fixed/Actual'),
        ('input M24 manifest', 'input M28 manifest'),
        ('same_g_M28_source_and_data_prepared', 'same_g_M32_source_and_data_prepared'),
        ('same_g_M28_actual_refinement_complete', 'same_g_M32_actual_refinement_complete')]:
        if source.count(before) != 1:
            raise ValueError('Diagnostic specialization anchor differs: '+before)
        source = source.replace(before, after, 1)
        applied.append(dict(before=before, after=after, count=1, diagnostic_text_only=True))
    ast.parse(source, filename='<original-spectral-entry-M32-fullflow>')
    return source, dict(original_file=ORIGINAL, original_sha256=ORIGINAL_SHA,
        compiled_sha256=hashlib.sha256(source.encode()).hexdigest(), replacements=applied,
        wrapper_sha256=sha(__file__), original_Python_and_all_MJS_unchanged=True,
        complete_original_numerical_gates_preserved=True)


def main():
    global LIVE_REFERENCE
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument('--spectral-stage-cache-directory', type=Path, required=True)
    p.add_argument('--spectral-live-preflight-only', action='store_true')
    own, remaining = p.parse_known_args()
    for key in ('--fixed-reference', '--out-prefix'):
        if remaining.count(key) != 1:
            raise ValueError('Require explicit '+key)
    LIVE_REFERENCE = Path(remaining[remaining.index('--fixed-reference')+1])
    out = Path(remaining[remaining.index('--out-prefix')+1])
    source, transform = build()
    transform['stage_cache_directory'] = str(own.spectral_stage_cache_directory.resolve())
    transform['live_prefix_preflight_only'] = own.spectral_live_preflight_only
    write_same(out.with_name(out.name+'-m32-source-transform.json'), transform)
    namespace = dict(__file__=str(Path(__file__).resolve()), __name__='strong_original_spectral_M32',
        SPECTRAL_TAIL_BUILDER=spectral_tail_warm, SPECTRAL_LIVE_IDENTITY=live_metric_identity,
        SPECTRAL_LIVE_PREFLIGHT=own.spectral_live_preflight_only, SPECTRAL_PREFLIGHT_FINISHED=PreflightFinished,
        M32_EXTRA_SOURCES={**EXTRA, ORIGINAL: ORIGINAL_SHA}, M32_ORIGINAL_SOURCE_SHA=ORIGINAL_SHA)
    exec(compile(source, '<original-spectral-entry-M32-fullflow>', 'exec'), namespace)
    namespace['resource_class'] = resource_class
    key = 'VISIBLE_FLEX_EXACT_STAGE_CACHE'
    previous, old_argv = os.environ.get(key), sys.argv
    own.spectral_stage_cache_directory.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(own.spectral_stage_cache_directory.resolve())
    # No explicit old-mode full-flow snapshot may leak in from another task.
    snapshot = os.environ.pop('VISIBLE_FLEX_FULL_TANGENT_START_MANIFEST', None)
    sys.argv = [old_argv[0], *remaining]
    try:
        namespace['main']()
    except PreflightFinished:
        if not own.spectral_live_preflight_only:
            raise
        terminal = json.loads(out.with_name(out.name+'-spectral-terminal.json').read_text())
        if terminal['counters'] != {'raw_spectral_embeddings': 1, 'resource_wrapped_clients': 1}:
            raise ValueError('Expected one full raw embedding and one unstarted client loader')
        write_same(out.with_name(out.name+'-live-preflight-result.json'), dict(
            scope=__doc__, complete_live_prefix_identity_passed=True,
            tail_worker_started=False, full_Jacobian_assembled=False, Newton_run=False,
            numerical_solution_accepted=False, source_transform=transform, terminal=terminal))
        print(json.dumps(dict(event='same_g_M32_live_prefix_preflight_complete',
            original_physical_metric_unchanged=True, numerical_solution_accepted=False,
            tail_worker_started=False, out_prefix=str(out))), flush=True)
    finally:
        sys.argv = old_argv
        if previous is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = previous
        if snapshot is not None:
            os.environ['VISIBLE_FLEX_FULL_TANGENT_START_MANIFEST'] = snapshot


if __name__ == '__main__':
    main()
