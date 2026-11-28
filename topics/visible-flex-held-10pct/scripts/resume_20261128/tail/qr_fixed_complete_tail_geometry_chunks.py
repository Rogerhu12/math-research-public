#!/usr/bin/env python3
"""Export/certify a genuine own QR fixed-g final-physical-H complete tail.

The own fixed-actual gate runs before any geometry module/provider is loaded.
The reviewed bounded-chunk implementation and the original complete v2
pipeline then receive this field's actual packet, baseline, port, native
scope, complete spectrum and shared mean. No anchor/design record is
relabelled as a fixed return. Every new field receives its own representation
and proofs; only identical durable files of this invocation may be resumed.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import fcntl
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ANALYTIC = HERE.parent/'analytic'
SCRIPTS = HERE.parents[1]
REPO = SCRIPTS.parents[2]
SCHEMA = 'own-original-support-QR-fixed-actual-complete-tail-chunks-v1'
KIND = 'original_r53_literal_fixed_metric_qr_anchor_actual_dn_v1'
SOURCE_KIND = 'accepted_original_support_qr_anchor_fixed_metric_actual_dn_physical_height'
REVIEWED = {
    HERE/'qr_complete_tail_geometry_chunks.py':
        '0bc3a31e348a5885b45ae082486aa470d39693684d3960bcd3ead61cc35fd5ee',
    HERE/'geometry_recursive_write_guard.py':
        '3a3f864be6047953e26c7a54bea352a294c12a5217cc8104a67547bf0ad34fa4',
    ANALYTIC/'qr_fixed_actual_cartesian_prefix.py':
        'e66f8cb57de54f4c62b84f36b6f9983ef7866cd19d959d0ff9eaa13ad856ac77',
    ANALYTIC/'qr_fixed_support_actual_model.py':
        'c85a7affd7e35328bf708510cb2440b6d530f8a259a85f01f8a8f99691db9b88',
    ANALYTIC/'qr_fixed_support_actual_acceptance.py':
        '045960847c115a4d28126bea63b3237a9b429f760c67ead506a59aff1c996c3e',
}
ORIGINAL_SHA = 'c165678d912761163ef29cfca1eb9c4dfc4bbf3102de6a00b228ca537f727615'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for data in iter(lambda:stream.read(1024*1024),b''):
            digest.update(data)
    return digest.hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def checked(reference):
    path = Path(reference['path']).resolve()
    if ref(path) != reference:
        raise ValueError('A complete fixed actual source changed: '+str(path))
    return path


def read(path):
    return json.loads(Path(path).read_text())


def module(name,path):
    path = Path(path).resolve()
    previous = sys.modules.get(name)
    if previous is not None:
        if Path(previous.__file__).resolve() != path:
            raise ValueError('Use a fresh process for the actual bound source tree')
        return previous
    spec = importlib.util.spec_from_file_location(name,path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('source-run','outdir'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--background-summary',type=Path)
    parser.add_argument('--phase',choices=('stage0','all'),default='all')
    parser.add_argument('--resume',action='store_true')
    parser.add_argument('--chunk-stages',type=int,default=8)
    parser.add_argument('--node-heap-mib',type=int,default=512)
    parser.add_argument('--disk-reserve-mib',type=int,default=128)
    parser.add_argument('--difference-step',type=float,default=.00005)
    parser.add_argument('--quadratic-mode-cutoff',type=int,default=12)
    parser.add_argument('--node',default='node')
    args = parser.parse_args()
    if (not 1 <= args.chunk_stages <= 16 or args.node_heap_mib < 256
            or args.disk_reserve_mib < 128 or args.quadratic_mode_cutoff < 0
            or not math.isfinite(args.difference_step) or args.difference_step <= 0):
        raise ValueError('Keep the unchanged bounded chunks, full guards and original numerical settings')
    if args.outdir.resolve() == REPO or REPO in args.outdir.resolve().parents:
        raise ValueError('Complete scientific data stay outside the current checkout')
    for path,digest in REVIEWED.items():
        if sha(path) != digest:
            raise ValueError('A frozen source requires an explicit new version: '+str(path))
    run = args.source_run.resolve()
    if read(run).get('model_kind') != KIND:
        raise ValueError('This independent producer requires a genuine own QR fixed-metric return')
    sys.path.insert(0,str(ANALYTIC))
    reader = module('qr_fixed_actual_cartesian_prefix',ANALYTIC/'qr_fixed_actual_cartesian_prefix.py')
    record, physical, view, provenance = reader.accepted_fixed(run)
    del physical
    if (record['model_kind'] != KIND or provenance['source_kind'] != SOURCE_KIND
            or provenance['source_run'] != ref(run)
            or view['height_reference'] != provenance['endpoint_binding']
            or view['packet'] != provenance['full_height_packet']):
        raise ValueError('The genuine fixed source changed during acceptance')
    runtime_ref,baseline_ref,port_ref = (provenance[key] for key in
        ('runtime_tail_configuration','base_tail_configuration','actual_source_port'))
    runtime,baseline,port = (read(checked(item)) for item in (runtime_ref,baseline_ref,port_ref))
    if ({k:v for k,v in runtime.items() if k not in reader.model.RUNTIME_CONFIG_KEYS} != baseline
            or port['source']['config_sha256'] != baseline_ref['sha256']
            or port['parameters'] != record['fixed_problem']['physical_tail_parameters']):
        raise ValueError('The actual fixed runtime/baseline/port contract changed')
    native_ref = provenance['native_manifest']
    native_manifest = read(checked(native_ref))
    source_topic = Path(native_manifest['source_topic']).resolve()
    native_runs = Path(runtime['traceFile']).resolve().parent/'native-runs'
    if not native_runs.is_dir():
        raise ValueError('The actually used fixed-source native record directory is missing')
    origin_scripts = Path(record['fixed_problem']['original_repository']).resolve()/(
        'topics/visible-flex-held-10pct/scripts')
    original_path = origin_scripts/'resume_20261126/seam_run_tail_geometry_v2.py'
    if sha(original_path) != ORIGINAL_SHA:
        raise ValueError('The actual original-tree complete geometry pipeline changed')
    origin_tail = origin_scripts/'resume_20261128/tail'
    chunk_path = origin_tail/'qr_complete_tail_geometry_chunks.py'
    for name in ('qr_complete_tail_geometry_chunks.py','geometry_recursive_write_guard.py',
                 'geometry_disk_guard.py','geometry_disk_guard.mjs'):
        if sha(origin_tail/name) != sha(HERE/name):
            raise ValueError('The actual complete chunk/guard source tree differs: '+name)
    # Loading geometry only after the genuine fixed gate preserves its
    # independently selected original provider and its absolute source paths.
    sys.path[:0] = [str(origin_tail),str(origin_scripts/'resume_20261126')]
    chunk = module('_fixed_actual_reviewed_complete_chunk_algebra',chunk_path)
    original = module('_fixed_actual_original_complete_geometry_pipeline',original_path)
    if (Path(original.HERE).resolve() != original_path.parent
            or Path(chunk.ORIGINAL).resolve() != original_path
            or Path(chunk.recursive_guard.__file__).resolve() != origin_tail/'geometry_recursive_write_guard.py'
            or Path(chunk.geometry_disk_guard.__file__).resolve() != origin_tail/'geometry_disk_guard.py'):
        raise ValueError('The original geometry pipeline imported another frozen provider tree')
    source_contract = dict(schema=SCHEMA, source=ref(__file__),
        reused_complete_chunk_source=ref(chunk.__file__), original_pipeline=ref(original_path),
        actual_source_kind=SOURCE_KIND, actual_source_model_kind=KIND,
        accepted_source_gate=provenance, fixed_problem=record['fixed_problem'],
        actual_frozen_metric=record['frozen_profile'],
        accepted_final_physical_run=ref(run), physical=view['physical'],
        final_physical_packet=view['packet'], final_physical_height_binding=view['height_reference'],
        raw_height_used_as_definition=False, source_port=port_ref,
        baseline_tail_configuration=baseline_ref, runtime_tail_configuration=runtime_ref,
        native_manifest=native_ref, native_record_dir=str(native_runs),
        source_mean_nodes=view['source_mean_nodes'], source_mean_gauss_order=6,
        anchor_record_relabelled_as_own_return=False,
        old_other_field_map_or_certificate_reused=False,
        original_mathematical_sources=original.source_refs())
    inherited = SimpleNamespace(tail_response=checked(view['packet']),source_port=checked(port_ref),
        source_topic=source_topic,height_reference=checked(view['height_reference']),
        height_reference_key='candidate_H',warm_factor=1.,height_arithmetic='numpy',
        native_record=None,native_record_dir=native_runs,outdir=args.outdir.resolve(),
        phase=args.phase,resume=args.resume,background_summary=args.background_summary,
        degree=None,difference_step=args.difference_step,
        quadratic_mode_cutoff=args.quadratic_mode_cutoff,node=args.node)
    Pipeline = chunk.make_pipeline(original,source_contract,args)
    pipeline = Pipeline(inherited)
    lock = (pipeline.root/'geometry-owner.lock').open('a+')
    try:
        fcntl.flock(lock.fileno(),fcntl.LOCK_EX | fcntl.LOCK_NB)
        chunk.no_live_child(pipeline.state)
        os.environ['HELD10_GEOMETRY_DISK_ROOT'] = str(pipeline.root)
        os.environ['HELD10_GEOMETRY_DISK_FLOOR'] = str(args.disk_reserve_mib*1024**2)
        js_guard = origin_tail/'geometry_disk_guard.mjs'
        os.environ['NODE_OPTIONS'] = ('--max-old-space-size='+str(args.node_heap_mib)+
                                     ' --import='+str(js_guard))
        guard = chunk.geometry_disk_guard.install()
        invocation = pipeline.directory('own-fixed-bounded-chunk-invocation')
        invocation.mkdir()
        execution = dict(schema=SCHEMA,source=ref(__file__),command=[sys.executable,*sys.argv],
            actual_source_kind=SOURCE_KIND,actual_source_model_kind=KIND,
            original_pipeline=ref(original_path),reused_complete_chunk_source=ref(chunk.__file__),
            complete_source_contract=source_contract,
            recursive_python_guard=ref(chunk.recursive_guard.__file__),
            original_python_guard=ref(chunk.geometry_disk_guard.__file__),
            original_node_guard=ref(js_guard),disk_guard=guard,
            node_options=os.environ['NODE_OPTIONS'],chunk_stages=args.chunk_stages,
            own_actual_source_gate_checked_before_geometry_import=True,
            original_native_or_BVP_solves_executed=False,
            previous_large_export_failure_required=False,
            inherited_state_key_actual_QR_physical_height_source_contains_this_own_fixed_contract=True,
            original_complete_mean_spectrum_and_certification_gates_changed=False)
        original.save(invocation/'execution.json',execution)
        pipeline.state['current_chunk_execution'] = ref(invocation/'execution.json')
        pipeline.state['actual_own_fixed_source_schema'] = SCHEMA
        pipeline.save()
        return pipeline.execute()
    finally:
        lock.close()


if __name__ == '__main__':
    sys.exit(main())
