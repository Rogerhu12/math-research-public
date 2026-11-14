#!/usr/bin/env python3
"""Fresh actual continuation with a declared fixed merit and original H0 anchor.

This is a numerical algorithm change, not an unchanged Newton trajectory.
The original discrete equations, domain checks, raw state, full-H nonlinear
tail tests and final physical gates are retained. It consumes an explicitly
pending complete inner checkpoint; it never marks that checkpoint as audited.
"""
from __future__ import annotations
import argparse
import ast
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_actual_three_control_bvp.py': 'a84c8587c8ed605fdc0627c1183d79ff0afaa26d21f2b78e00c7091fa5ba6da4',
    'strong_exact_raw_three_control_bvp.py': '4c0030c38a34f99b4c9c58c02b7c74e32c2795eb55190c623d71f9771e80cc98',
    'strong_disk_actual_backend.py': '402830e66390f660d7f8e846165a2ae7c1e9858addc2317df06348dc1e8634f1',
    'root_disk_block_collocation.py': 'f252024e7193b0e98c6f243b9dc6814c94c28c358e059b8a901da8e6396620b2',
    'root_actual_neck_bvp.py': '03bd353875b4a7ca248c938887b706ce6e2d3115e9b82f2cf772ccc4b5ce98b7',
    'root_domain_newton.py': 'fd0f63fed7d74115c6e482bf47560230409ce2c20880aaa91e4e4ea1fbda0c83',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def argument(arguments, name, count=1):
    if arguments.count(name) != 1:
        raise ValueError('Require one explicit original argument: '+name)
    index = arguments.index(name)
    values = arguments[index+1:index+1+count]
    if len(values) != count:
        raise ValueError('Incomplete argument: '+name)
    return values[0] if count == 1 else values


def prepare_configuration(arguments, anchor_packet, original_entry_raw, original_entry_config):
    for disallowed in ('--response-data','--tail-warm-checkpoint','--inspect-local-output','--inspect-warm-output'):
        if disallowed in arguments:
            raise ValueError('Use the explicit complete inner restart, not another warm/inspection path')
    reference_file = Path(argument(arguments,'--actual-reference'))
    raw_file = Path(argument(arguments,'--resume-actual-iterate'))
    prior_config = Path(argument(arguments,'--resume-tail-config'))
    initial_packet = Path(argument(arguments,'--initial-audited-tail-packet'))
    initial_ready = Path(argument(arguments,'--initial-audited-tail-ready'))
    targets = list(map(float,argument(arguments,'--target-core',3)))
    reference, raw = document(reference_file), document(raw_file)
    entry = document(original_entry_raw)
    packet = document(anchor_packet)
    M, q = int(reference['config']['modes']), float(reference['gauge_amplitude'])
    identity, provenance = raw['identity'], raw['provenance']
    if (raw.get('solver_success') is not False or raw.get('physical_surface') is not False
            or provenance.get('phase') != 'accepted-newton' or provenance.get('call') != 1
            or not provenance.get('actual_coupled_acceptance_pending')
            or not identity['coupling_context'].get('actual_augmented_three_control')
            or identity['coupling_context']['actual_targets'] != targets
            or identity['modes'] != M or identity['gauge'] != q
            or raw['arrays']['p']['shape'] != [M+3]
            or sha(prior_config) != identity['coupling_context']['tail_config_sha256']):
        raise ValueError('Require the complete pending first-inner-solve M+3 checkpoint and its exact config')
    entry_identity = entry['identity']
    if (entry['provenance'].get('phase') != 'newton-entry' or entry['provenance'].get('call') != 1
            or entry['provenance'].get('iteration') != 0 or entry['solver_success']
            or sha(original_entry_raw) not in provenance['source_sha256'].values()
            or sha(original_entry_config) != entry_identity['coupling_context']['tail_config_sha256']):
        raise ValueError('Require the exact recorded first-inner entry and its original tail config')
    identity_keys = ('modes','angular','gauge','reference_coefficients','reference_frequencies',
        'numerical_reference_knots','parameter_layout','physical_tail_parameters','physical_tail_cut','tol','bc_tol')
    if any(entry_identity[key] != identity[key] for key in identity_keys):
        raise ValueError('Original affine entry and pending iterate changed the numerical or physical problem')
    contexts = [{k:v for k,v in ident['coupling_context'].items() if k != 'tail_config_sha256'}
                for ident in (entry_identity,identity)]
    io_keys = {'traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint'}
    configurations = [{k:v for k,v in document(f).items() if k not in io_keys}
                      for f in (original_entry_config,prior_config)]
    if contexts[0] != contexts[1] or configurations[0] != configurations[1]:
        raise ValueError('The original and current inner tail problems differ beyond output/warm paths')
    anchor_sha = sha(anchor_packet)
    if anchor_sha != sha(initial_packet) or anchor_sha not in provenance['source_sha256'].values():
        raise ValueError('The declared H0 packet is not the original recorded audited anchor')
    request, response = packet['request'], packet['response']
    if (len(request['height']) != M or not request.get('jacobian') or not request.get('audit')
            or not response.get('converged') or response.get('audit') is None
            or len(response['heightJetJacobian']) not in ((3*M+2)*M,3*M+2)):
        raise ValueError('The saved H0 response lacks its original complete Jacobian/audit')
    scales = list(map(float,reference['central_correction_scales']))
    weights = [targets[0]/q,*[v/q for v in scales],1.,1.,1.]
    if len(weights) != M+3 or not all(math.isfinite(v) and v>0 for v in weights):
        raise ValueError('Invalid complete fixed physical-core coordinate scale')
    return dict(
        scope=__doc__,mode='fixed-physical-core-coordinate-merit-v1',modes=M,gauge=q,
        target_actual_core=targets,fixed_field_weights=1.,fixed_parameter_weights=weights,
        weights_definition='c2_target/gauge for log c2; saved physical coefficient scales/gauge for c4+; 1 for delta/LB/vp offsets',
        weights_fixed_for_entire_run=True,original_newton_merit_changed=True,
        original_linear_system_and_all_final_physical_gates_unchanged=True,
        resume_raw=str(raw_file),resume_raw_sha256=sha(raw_file),
        resume_prior_tail_config=str(prior_config),resume_prior_tail_config_sha256=sha(prior_config),
        original_entry_raw=str(original_entry_raw),original_entry_raw_sha256=sha(original_entry_raw),
        original_entry_tail_config=str(original_entry_config),original_entry_tail_config_sha256=sha(original_entry_config),
        affine_anchor_packet=str(anchor_packet),affine_anchor_packet_sha256=anchor_sha,
        affine_anchor_ready=str(initial_ready),affine_anchor_ready_sha256=sha(initial_ready),
        accepted_reference=str(reference_file),accepted_reference_sha256=sha(reference_file),
        restored_raw_H_is_not_the_audited_H0_request=True,
        original_new_H_true_BC_and_final_full_audit_still_required=True,
        static_shape_checks_only_full_packet_source_ready_guard_still_required_at_runtime=True)


def build_source(configuration, disk_configuration):
    source_hashes = {}
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('Frozen numerical source differs: '+name)
        source_hashes[str(HERE/name)] = expected
    for name in ('strong_physical_merit_actual_bvp.py','strong_physical_merit_and_affine_resume.py'):
        source_hashes[str(HERE/name)] = sha(HERE/name)
    spec = importlib.util.spec_from_file_location('strong_merit_original_exactraw_changes',HERE/'strong_exact_raw_three_control_bvp.py')
    exact = importlib.util.module_from_spec(spec);spec.loader.exec_module(exact)
    edits = list(exact.EDITS)+[
        ("'strong_exact_raw_tail_worker.mjs', 'strong_exact_raw_tail_warm.mjs')",
         "'strong_exact_raw_tail_worker.mjs', 'strong_exact_raw_tail_warm.mjs',\n"
         "        'strong_physical_merit_actual_bvp.py', 'strong_physical_merit_and_affine_resume.py',\n"
         "        'strong_disk_actual_backend.py', 'root_disk_block_collocation.py')"),
        ('    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}',
         '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}\n'
         '    hashes[FIXED_MERIT_CONFIGURATION["original_entry_raw"]] = FIXED_MERIT_CONFIGURATION["original_entry_raw_sha256"]\n'
         '    hashes[FIXED_MERIT_CONFIGURATION["original_entry_tail_config"]] = FIXED_MERIT_CONFIGURATION["original_entry_tail_config_sha256"]'),
        ('    import root_actual_bounded_neck as bounded',
         '    import root_actual_bounded_neck as bounded\n'
         '    from strong_physical_merit_and_affine_resume import Runtime\n'
         '    merit_runtime = Runtime(FIXED_MERIT_CONFIGURATION, out)\n'
         '    disk_runtime = merit_runtime.install_disk_backend(bounded, '+repr(disk_configuration)+')'),
        ('    provenance = dict(scope=__doc__, exact_raw_warm_storage_adapter=EXACT_RAW_SOURCE_TRANSFORM, status=',
         '    provenance = dict(scope=__doc__, fixed_physical_merit_and_affine_restart=FIXED_MERIT_SOURCE_TRANSFORM, exact_raw_warm_storage_adapter=EXACT_RAW_SOURCE_TRANSFORM, status='),
        ('            checkpoints.install_observer(loaded, path, bounded.adapter, recorder)',
         '            merit_runtime.install_newton(loaded, path, bounded.adapter)\n'
         '            checkpoints.install_observer(loaded, path, bounded.adapter, recorder)'),
        ('                solve = cls.solve_coupled',
         '                merit_runtime.install_affine_on_class(cls)\n'
         '                solve = cls.solve_coupled'),
        ('        for function, default in zip((radial.value, radial.state_jacobian, bounded.blocks.prepare_sys), defaults):\n'
         '            function.__defaults__ = default\n        gc.collect()',
         '        for function, default in zip((radial.value, radial.state_jacobian, bounded.blocks.prepare_sys), defaults):\n'
         '            function.__defaults__ = default\n        gc.collect()\n'
         '        disk_runtime.finish()\n        merit_runtime.finish()'),
    ]
    original = (HERE/'strong_actual_three_control_bvp.py').read_text()
    changed = original
    for old,new in edits:
        if changed.count(old) != 1:
            raise ValueError('The explicit fixed-merit production source anchor is not unique: '+repr(old))
        changed = changed.replace(old,new,1)
    ast.parse(changed,filename='<fixed-physical-merit-actual-source>')
    provenance = dict(scope=__doc__,configuration=configuration,disk_configuration=disk_configuration,
        source_sha256=source_hashes,template_sha256=EXPECTED['strong_actual_three_control_bvp.py'],
        transformed_source_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        replacements=[dict(before=a,after=b,count=1) for a,b in edits],
        original_source_files_unchanged=True,original_newton_merit_changed=True,
        original_equations_and_final_nonlinear_physical_acceptance_preserved=True,
        original_H0_anchor_restored_explicitly_not_relabelled_as_new_H_audit=True)
    return changed,provenance


def main():
    parser = argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--resume-original-affine-anchor',type=Path,required=True)
    parser.add_argument('--original-inner-entry-raw',type=Path,required=True)
    parser.add_argument('--original-inner-entry-tail-config',type=Path,required=True)
    parser.add_argument('--disk-temporary-parent',type=Path)
    parser.add_argument('--disk-backward-error-tol',type=float,default=5e-11)
    parser.add_argument('--disk-heartbeat-seconds',type=float,default=20.)
    own, remaining = parser.parse_known_args()
    if not 0<own.disk_backward_error_tol<=5e-11 or not 5<=own.disk_heartbeat_seconds<=60:
        raise ValueError('Use the unchanged or stricter full-matrix backward gate and bounded heartbeat')
    disk = dict(temporary_parent=None if own.disk_temporary_parent is None else str(own.disk_temporary_parent.resolve()),
        backward_error_tolerance=own.disk_backward_error_tol,heartbeat_seconds=own.disk_heartbeat_seconds)
    configuration = prepare_configuration(remaining,own.resume_original_affine_anchor,
        own.original_inner_entry_raw,own.original_inner_entry_tail_config)
    source, provenance = build_source(configuration,disk)
    namespace = dict(__file__=str(HERE/'strong_actual_three_control_bvp.py'),
        __name__='strong_fixed_physical_merit_actual_source',
        FIXED_MERIT_CONFIGURATION=configuration,FIXED_MERIT_SOURCE_TRANSFORM=provenance,
        EXACT_RAW_SOURCE_TRANSFORM=dict(
            exact_raw_warm_adapter_sha256=EXPECTED['strong_exact_raw_three_control_bvp.py'],
            same_grid_raw_tail_warm_and_strict_audited_H_guard_preserved=True,
            combined_source_transform=provenance,
            original_newton_merit_preserved=False,
            original_discrete_equations_and_final_physical_acceptance_preserved=True))
    old = sys.argv;sys.argv = [old[0],*remaining]
    try:
        exec(compile(source,'<fixed-physical-merit-actual-source>','exec'),namespace)
        namespace['main']()
    finally:
        sys.argv = old


if __name__ == '__main__':
    main()
