#!/usr/bin/env python3
"""Fresh actual M+3 continuation with fixed S, disk QR and domain observations.

The accepted all-core baseline and original complete actual-J warm construction
remain unchanged. The original outer coupling method and complete actual new-H
tests remain unchanged. This entry changes the Newton correction norm, explicitly,
and adds lossless observations of rejected-domain blocks. It does not reuse a
pending q105 affine state or its different H0 response for another target.
"""
from __future__ import annotations
import argparse
import ast
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
EXPECTED={
    'strong_actual_three_control_bvp.py':'a84c8587c8ed605fdc0627c1183d79ff0afaa26d21f2b78e00c7091fa5ba6da4',
    'strong_exact_raw_three_control_bvp.py':'4c0030c38a34f99b4c9c58c02b7c74e32c2795eb55190c623d71f9771e80cc98',
    'strong_disk_actual_backend.py':'402830e66390f660d7f8e846165a2ae7c1e9858addc2317df06348dc1e8634f1',
    'root_disk_block_collocation.py':'f252024e7193b0e98c6f243b9dc6814c94c28c358e059b8a901da8e6396620b2',
    'strong_physical_merit_and_affine_resume.py':'e330336daab09ef9d0bcb93cb36e04581636e33e645ed5e319987c3cc0f2810f',
    'root_actual_neck_bvp.py':'03bd353875b4a7ca248c938887b706ce6e2d3115e9b82f2cf772ccc4b5ce98b7',
    'root_domain_newton.py':'fd0f63fed7d74115c6e482bf47560230409ce2c20880aaa91e4e4ea1fbda0c83'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data=Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def argument(argv,name,count=1):
    if argv.count(name)!=1: raise ValueError('Require one original argument '+name)
    i=argv.index(name)
    value=argv[i+1:i+1+count]
    if len(value)!=count: raise ValueError('Incomplete original argument '+name)
    return value[0] if count==1 else value


def prepare_configuration(argv):
    if any(name in argv for name in ('--resume-actual-iterate','--resume-tail-config',
            '--resume-original-affine-anchor','--original-inner-entry-raw')):
        raise ValueError('This is a fresh accepted-baseline continuation, not a pending affine restart')
    path=Path(argument(argv,'--actual-reference'))
    reference=read(path)
    if not reference.get('solver_success') or reference.get('audit_pending',True):
        raise ValueError('A completed actual accepted baseline is required')
    targets=list(map(float,argument(argv,'--target-core',3)))
    M,q=int(reference['modes']),float(reference['gauge_amplitude'])
    scales=list(map(float,reference['central_correction_scales']))
    weights=[targets[0]/q,*[v/q for v in scales],1.,1.,1.]
    if len(weights)!=M+3 or not all(math.isfinite(v) and v>0 for v in weights):
        raise ValueError('Fixed physical-core-coordinate weights are invalid')
    return dict(mode='fresh-fixed-physical-core-coordinate-merit-v1',modes=M,gauge=q,
        accepted_reference=str(path),accepted_reference_sha256=sha(path),
        target_actual_core=targets,fixed_field_weights=1.,fixed_parameter_weights=weights,
        weights_definition='target c2/gauge for log c2; complete physical core scales/gauge for c4+; 1 for delta/LB/vp',
        weights_fixed_for_entire_run=True,original_Newton_merit_changed=True,
        original_linear_system_and_all_final_physical_gates_unchanged=True,
        original_complete_outer_method_preserved=True,affine_anchor_not_replaced=True)


def build_source(configuration,disk_configuration):
    hashes={}
    for name,expected in EXPECTED.items():
        if sha(HERE/name)!=expected: raise ValueError('Frozen numerical source changed: '+name)
        hashes[str(HERE/name)]=expected
    own=('strong_fresh_physical_merit_actual_bvp.py','strong_fresh_physical_merit_runtime.py',
         'strong_domain_rejection_observer.py')
    hashes.update({str(HERE/name):sha(HERE/name) for name in own})
    spec=importlib.util.spec_from_file_location('strong_fresh_original_exactraw',HERE/'strong_exact_raw_three_control_bvp.py')
    original=importlib.util.module_from_spec(spec);spec.loader.exec_module(original)
    additions=[
        ("'strong_exact_raw_tail_worker.mjs', 'strong_exact_raw_tail_warm.mjs')",
         "'strong_exact_raw_tail_worker.mjs', 'strong_exact_raw_tail_warm.mjs',\n"
         "        'strong_fresh_physical_merit_actual_bvp.py', 'strong_fresh_physical_merit_runtime.py',\n"
         "        'strong_physical_merit_and_affine_resume.py', 'strong_domain_rejection_observer.py',\n"
         "        'strong_disk_actual_backend.py', 'root_disk_block_collocation.py',\n"
         "        'strong_exact_stage_tail_client.py', 'strong_exact_stage_tail_worker.mjs',\n"
         "        'strong_exact_stage_engine.mjs', 'strong_exact_stage_flow_store.mjs',\n"
         "        'strong_exact_stage_seed.mjs', 'strong_exact_stage_evaluation_check.mjs')"),
        ("            loaded = original_loader(name+'_exact_raw', HERE/'strong_exact_raw_tail_client.py')",
         "            loaded = original_loader(name+'_exact_stage', HERE/'strong_exact_stage_tail_client.py')\n"
         "            stage_base = loaded.WeightedTailPort\n"
         "            class ExplicitStagePort(stage_base):\n"
         "                def __init__(self, config, source_root, record_prefix, node_heap=384):\n"
         "                    key = 'VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX'\n"
         "                    old_seed = os.environ.get(key)\n"
         "                    os.environ[key] = str(Path(record_prefix).resolve())+'-exact-initial'\n"
         "                    try:\n"
         "                        super().__init__(config, source_root, record_prefix, node_heap=node_heap)\n"
         "                    finally:\n"
         "                        if old_seed is None: os.environ.pop(key, None)\n"
         "                        else: os.environ[key] = old_seed\n"
         "            loaded.WeightedTailPort = ExplicitStagePort"),
        ('    import root_actual_bounded_neck as bounded',
         '    import root_actual_bounded_neck as bounded\n'
         '    from strong_fresh_physical_merit_runtime import Runtime\n'
         '    from strong_domain_rejection_observer import DomainObservation\n'
         '    merit_runtime = Runtime(FRESH_MERIT_CONFIGURATION, out)\n'
         '    disk_runtime = merit_runtime.install_disk_backend(bounded, '+repr(disk_configuration)+')\n'
         '    domain_runtime = DomainObservation(out, FRESH_MERIT_CONFIGURATION, hashes, emit=merit_runtime.emit)'),
        ('    provenance = dict(scope=__doc__, exact_raw_warm_storage_adapter=EXACT_RAW_SOURCE_TRANSFORM, status=',
         '    provenance = dict(scope=__doc__, fresh_fixed_physical_merit=FRESH_MERIT_SOURCE_TRANSFORM, exact_raw_warm_storage_adapter=EXACT_RAW_SOURCE_TRANSFORM, status='),
        ('    bounded.blocks.prepare_sys.__defaults__ = (options.collocation_batch_size,)',
         '    bounded.blocks.prepare_sys.__defaults__ = (options.collocation_batch_size,)\n'
         '    domain_runtime.install_radial(radial)'),
        ('            checkpoints.install_observer(loaded, path, bounded.adapter, recorder)',
         '            merit_runtime.install_newton(loaded, path, bounded.adapter)\n'
         '            domain_runtime.install_newton(loaded, path, bounded.adapter)\n'
         '            checkpoints.install_observer(loaded, path, bounded.adapter, recorder)'),
        ('                cls.bc_jac = cls.augmented_bc_jac',
         '                cls.bc_jac = cls.augmented_bc_jac\n'
         '                domain_runtime.install_class(cls)'),
        ('        for function, default in zip((radial.value, radial.state_jacobian, bounded.blocks.prepare_sys), defaults):\n'
         '            function.__defaults__ = default\n        gc.collect()',
         '        for function, default in zip((radial.value, radial.state_jacobian, bounded.blocks.prepare_sys), defaults):\n'
         '            function.__defaults__ = default\n        gc.collect()\n'
         '        domain_runtime.finish()\n        disk_runtime.finish()\n        merit_runtime.finish()')]
    edits=list(original.EDITS)+additions
    source=(HERE/'strong_actual_three_control_bvp.py').read_text()
    for before,after in edits:
        if source.count(before)!=1: raise ValueError('Fresh fixed-S source anchor is not unique: '+repr(before))
        source=source.replace(before,after,1)
    ast.parse(source,filename='<fresh-fixed-physical-merit-actual-source>')
    record=dict(scope=__doc__,configuration=configuration,disk_configuration=disk_configuration,
        source_sha256=hashes,template_sha256=EXPECTED['strong_actual_three_control_bvp.py'],
        transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        replacements=[dict(before=a,after=b,count=1) for a,b in edits],
        original_source_files_unchanged=True,original_Newton_merit_changed=True,
        original_equations_and_final_nonlinear_physical_acceptance_preserved=True,
        original_complete_outer_method_and_true_new_H_checks_untouched=True,
        tail_stage_storage=dict(client='strong_exact_stage_tail_client.py',
            directory=configuration['stage_cache_directory'],
            per_worker_generation_seed_prefix='actual live record prefix + -exact-initial',
            same_complete_input_and_identity_only=True,
            original_full_changed_H_solve_and_audit_preserved=True),
        domain_observation_only_no_additional_RHS_or_geometry=True)
    return source,record


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--disk-temporary-parent',type=Path)
    parser.add_argument('--disk-backward-error-tol',type=float,default=5e-11)
    parser.add_argument('--disk-heartbeat-seconds',type=float,default=20.)
    parser.add_argument('--stage-cache-directory',type=Path,required=True)
    own,remaining=parser.parse_known_args()
    if not 0<own.disk_backward_error_tol<=5e-11 or not 5<=own.disk_heartbeat_seconds<=60:
        raise ValueError('The complete backward-check gate cannot be weakened')
    disk=dict(temporary_parent=None if own.disk_temporary_parent is None else str(own.disk_temporary_parent.resolve()),
        backward_error_tolerance=own.disk_backward_error_tol,heartbeat_seconds=own.disk_heartbeat_seconds)
    configuration=prepare_configuration(remaining)
    configuration['stage_cache_directory']=str(own.stage_cache_directory.resolve())
    source,provenance=build_source(configuration,disk)
    namespace=dict(__file__=str(HERE/'strong_actual_three_control_bvp.py'),
        __name__='strong_fresh_fixed_merit_actual_source',FRESH_MERIT_CONFIGURATION=configuration,
        FRESH_MERIT_SOURCE_TRANSFORM=provenance,
        EXACT_RAW_SOURCE_TRANSFORM=dict(exact_raw_template_sha256=EXPECTED['strong_exact_raw_three_control_bvp.py'],
            exact_raw_warm_protocol_preserved=True,
            explicit_complete_input_stage_cache_client=True,combined_source_transform=provenance,
            original_Newton_merit_preserved=False,
            original_discrete_equations_and_final_physical_acceptance_preserved=True))
    old=sys.argv;sys.argv=[old[0],*remaining]
    old_cache=os.environ.get('VISIBLE_FLEX_EXACT_STAGE_CACHE')
    os.environ['VISIBLE_FLEX_EXACT_STAGE_CACHE']=configuration['stage_cache_directory']
    try:
        exec(compile(source,'<fresh-fixed-physical-merit-actual-source>','exec'),namespace)
        namespace['main']()
    finally:
        sys.argv=old
        if old_cache is None: os.environ.pop('VISIBLE_FLEX_EXACT_STAGE_CACHE',None)
        else: os.environ['VISIBLE_FLEX_EXACT_STAGE_CACHE']=old_cache


if __name__=='__main__':main()
