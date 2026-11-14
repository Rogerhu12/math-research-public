#!/usr/bin/env python3
"""Inspect a genuine accepted M32 field plus an explicit M28 warm increment.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original verified coarse-to-fine constructor owns every state/core
increment. The corrected initial-speed anchor hook and the complete original
physical-geometry/mean loops are retained. The fine baseline is never zeroed
in its four new modes. This is an unsolved warm field, never an M32 Jacobian,
accepted new solution, continuous certificate or new tail evaluation.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import ast
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
COARSE_WARM_SHA='ff5acad191d51544bfebaf46902f7e58f89a2e4575130f9b33932aa25ef8972c'
GRID_HELPER_SHA='32d046c158e2c8d64a45b96d0c45c7c56eda6699d779826a88bfa9ebc34c692e'
COARSE_GRID_SHA='6307703991ac484616dcbefca68540748c69ed697f3436303f6ee1c0336dd25f'
FINE_PRIMARY_SHA='4c0e13b2ea4e2541e75891a3b4fafa93ffc2f8331cfdcdc7e4083ac3cbfef1ad'
FINE_AUDIT_SHA='23e2ad81352410296c49f479e00232d79cff610273a7fd38ca61fbb0d4ae21c5'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def one(argv,name):
    if argv.count(name)!=1:raise ValueError('Exactly one original argument required: '+name)
    return argv[argv.index(name)+1]


def fine_grid(record,old_path,audit_path,destination):
    """Preserve the actual old grid and add the genuinely measured fine witness.

    This declared refinement happened to retain both the exact raw mesh and
    the numerical/material chart. Its measured curvature witness has the
    same s/psi coordinates as the previously retained q122 witness. No
    unperformed inverse map or future extremum is invented here.
    """
    if sha(old_path)!=COARSE_GRID_SHA or sha(audit_path)!=FINE_AUDIT_SHA or record['current_reference_sha256']!=FINE_PRIMARY_SHA:
        raise ValueError('This actual fine-grid bridge is only for the accepted q122 M32 pair')
    old=read(old_path);audit=read(audit_path)
    if (old['raw_sha256']!=sha(record['coarse_raw']) or audit['input_sha256']!=FINE_PRIMARY_SHA or
        audit['modes']!=32 or audit['config']['mean_angular']!=1552 or audit['config']['angular']!=768 or
        not record['complete_original_mesh_bits_identical'] or not record['original_material_chart_and_physical_metric_identical']):
        raise ValueError('Actual fine witness, original mesh or unchanged coordinate identity differs')
    k=audit['top']['kappa'];matches=[];evidence={}
    for known in old['known_reference_witnesses']:
        source=Path(known['source_grid']);bundle=read(source);evidence[str(source)]=sha(source)
        for witness in bundle['known_reference_witnesses']:
            if (witness.get('physical_s')==k['s'] and witness.get('eta')==k['psi'] and
                witness['numerical_t']==known['numerical_t'] and
                old['numerical_t'][known['radial_index']]==known['numerical_t']):
                matches.append(dict(known))
    if not matches:raise ValueError('The actual fine witness needs a new measured coordinate map; no guess is allowed')
    witness=matches[0]
    witness.update(physical_s=k['s'],eta=k['psi'],source_audit=str(audit_path),source_audit_sha256=FINE_AUDIT_SHA,
        source_audit_input_sha256=FINE_PRIMARY_SHA,source_polynomial_sample=k['value'],old_witness_only=False,
        current_accepted_fine_polynomial_witness=True,original_numerical_coordinate_via_verified_sameg_chart=True,
        raw_cubic_does_not_replace_actual_quintic_witness=True)
    new=dict(old,raw_sha256=record['current_raw_sha256'],known_reference_witnesses=[*old['known_reference_witnesses'],witness])
    new['actual_sameg_fine_grid_bridge']=dict(source_sha256=sha(__file__),original_grid=str(old_path),original_grid_sha256=COARSE_GRID_SHA,
        coarse_raw_sha256=sha(record['coarse_raw']),fine_raw_sha256=record['current_raw_sha256'],fine_reference_sha256=FINE_PRIMARY_SHA,
        actual_fine_audit=str(audit_path),actual_fine_audit_sha256=FINE_AUDIT_SHA,old_witness_evidence=evidence,
        every_original_numerical_coordinate_preserved=True,physical_and_numerical_charts_identical=True,
        every_fine_raw_node_present_by_same_mesh_identity=True,actual_new_fine_witness_included=True,
        new_field_evaluation=False)
    if destination.exists():
        if read(destination)!=new:raise ValueError('Existing fine common grid differs from this exact bridge')
    else:
        destination.parent.mkdir(parents=True,exist_ok=True);destination.write_text(json.dumps(new,indent=2)+'\n')
    return new['actual_sameg_fine_grid_bridge']


def main():
    p=argparse.ArgumentParser(add_help=False,description=__doc__)
    p.add_argument('--coarse-warm-source',type=Path,required=True)
    p.add_argument('--coarse-reference',type=Path,required=True)
    p.add_argument('--coarse-raw',type=Path,required=True)
    p.add_argument('--coarse-tail',type=Path,required=True)
    p.add_argument('--coarse-response-data',type=Path,required=True)
    p.add_argument('--coarse-control',action='append',default=[])
    p.add_argument('--coarse-grid',type=Path,required=True)
    p.add_argument('--fine-interior-audit',type=Path,required=True)
    p.add_argument('--coarse-fine-geometry-prepare-only',action='store_true')
    own,remaining=p.parse_known_args()
    if any(x in remaining for x in ('--response-data','--target-core','--neutral-control-step','--resume-actual-iterate',
        '--resume-tail-config','--inspect-local-output','--prepare-only','--fixed-reference','--postprocess-only')):
        raise ValueError('The verified coarse increment supplies the sole explicit fine warm construction')
    if '--inspect-warm-output' not in remaining:raise ValueError('Only explicit unsolved geometry inspection is allowed')
    if sha(own.coarse_warm_source)!=COARSE_WARM_SHA or sha(HERE/'root_actual_secant_geometry_complete_mean.py')!=GRID_HELPER_SHA:
        raise ValueError('Verified warm constructor or original complete-grid checker changed')
    spec=importlib.util.spec_from_file_location('geometry_verified_coarse_fine_warm',own.coarse_warm_source)
    coarse=importlib.util.module_from_spec(spec);sys.modules[spec.name]=coarse;spec.loader.exec_module(coarse)
    prepared=coarse.prepare(own,remaining);record,warm=prepared
    grid_path=Path(one(remaining,'--geometry-grid'))
    grid_identity=fine_grid(record,own.coarse_grid,own.fine_interior_audit,grid_path)
    from root_actual_secant_geometry_complete_mean import check_grid
    grid=check_grid(record,remaining)
    if grid['complete_mean_angular']!=1552 or grid['original_parameter_count']!=32:
        raise ValueError('The genuine accepted fine p32 and complete 1552-point mean are required')
    from strong_frontload_anchor_loader_adapter import build
    namespace,anchor=build('geometry',__file__)
    entry,initial_main,initial_record=namespace['prepare_entry']()
    original=inspect.getsource(entry.main);source=original
    for change in initial_record['source_transforms']:
        if source.count(change['before'])!=1:raise ValueError('Original initial-law source preparation anchor differs')
        source=source.replace(change['before'],change['after'],1)
    if hashlib.sha256(source.encode()).hexdigest()!=initial_record['transformed_main_sha256']:
        raise ValueError('The actual corrected initial-law entry was not reconstructed exactly')
    before_warm=source
    edits=[
        ('    if external_shifts and not options.response_data:\n',
         '    if external_shifts and not options.response_data and not verified_warm(\n'
         '            options.actual_reference, options.actual_reference_raw, target, external_shifts):\n'),
        ('    warm = None\n',
         '    warm = verified_warm(options.actual_reference, options.actual_reference_raw,\n'
         '        target, external_shifts, payload=True)\n'),
        ("complete_actual_tangent_warm=warm['provenance'] if warm else None",
         "explicit_coarse_increment_warm=warm['provenance'] if warm else None"),
        ('Complete actual-J warm field on the original residual quadrature and a complete-mean C2 cubic physical image; unsolved comparison only.',
         'Complete accepted M32 field plus an explicitly embedded M28 response increment, with the original complete M32 mean; unsolved warm geometry only.'),
        ('    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}',
         '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}\n    hashes.update(COARSE_WARM_SOURCES)'),
    ]
    for old,new in edits:
        if source.count(old)!=1:raise ValueError('The original explicit warm replacement is no longer unique')
        source=source.replace(old,new,1)
    reverse=source
    for old,new in reversed(edits):reverse=reverse.replace(new,old,1)
    if reverse!=before_warm:raise ValueError('An unlisted corrected original entry site changed')
    ast.parse(source)
    env=dict(initial_main.__globals__);env.update(verified_warm=coarse.verified_warm,COARSE_WARM_SOURCES=record['source_sha256'])
    exec(compile(source,'<actual-M32-coarse-increment-fullmean-geometry>','exec'),env)
    patched=env['main'];prefix=Path(one(remaining,'--out-prefix'));metadata=Path(str(prefix)+'-coarse-fine-geometry-prepared.json')
    if metadata.exists():raise FileExistsError('Fresh actual geometry preparation metadata required')
    import root_actual_geometry_field_complete_mean as geometry
    files=[Path(__file__),own.coarse_warm_source,HERE/'root_actual_secant_geometry_complete_mean.py',
        Path(geometry.__file__),HERE/'strong_frontload_anchor_loader_adapter.py',grid_path,own.fine_interior_audit]
    hashes={**record['source_sha256'],**initial_record['source_inputs'],**{str(x):sha(x) for x in files}}
    metadata.parent.mkdir(parents=True,exist_ok=True)
    metadata.write_text(json.dumps(dict(schema='actual-fine-complete-mean-coarse-increment-geometry-preparation-v1',scope=__doc__,
        source_and_input_sha256=hashes,original_verified_coarse_warm=record,actual_fine_grid_bridge=grid_identity,
        common_grid=grid,corrected_anchor_provider=anchor,initial_laws_source_preparation=initial_record,
        original_initial_laws_main_sha256=hashlib.sha256(before_warm.encode()).hexdigest(),
        explicit_coarse_warm_main_sha256=hashlib.sha256(source.encode()).hexdigest(),
        exact_reverse_recovers_corrected_initial_laws_main=True,
        complete_original_fine_mean_and_geometry_formulas_unchanged=True,
        prepared_only=True,geometry_executed_by_this_record=False,fine_Jacobian_claim=False,
        new_solution_or_true_tail_evaluation=False),indent=2)+'\n')
    oldactive,oldmain,oldargv=coarse._ACTIVE,entry.main,sys.argv
    coarse._ACTIVE=prepared
    try:
        if coarse.verified_warm(Path(record['current_reference']),Path(record['current_raw']),record['target_core'],record['external_shifts'],payload=True) is not warm:
            raise ArithmeticError('Verified full fine-field warm pointer changed')
        if own.coarse_fine_geometry_prepare_only:
            print(json.dumps(dict(event='actual_fine_fullmean_coarse_warm_prepared',metadata=str(metadata),sha256=sha(metadata),
                grid=grid,target=record['target_core'],Flow_ODE_Node_calls=0)),flush=True)
            return
        remaining+=['--target-core',*map(repr,record['target_core'])]
        for key,value in record['external_shifts'].items():remaining+=['--neutral-control-step',key+'='+repr(value)]
        entry.main=patched;sys.argv=[oldargv[0],*remaining]
        geometry.main()
        for path,digest in hashes.items():
            if sha(path)!=digest:raise ValueError('Actual complete warm geometry input changed: '+path)
        report_path=Path(one(remaining,'--inspect-warm-output'));report=read(report_path)
        if report.get('explicit_coarse_increment_warm')!=record or report['geometry_fields']['mean_quadrature']['angular']!=1552 or len(report['actual_core'])!=32:
            raise ValueError('The actual complete field did not consume the declared fine warm identity')
        report['fine_complete_mean_coarse_warm_adapter']=dict(source_sha256=sha(__file__),coarse_constructor_sha256=COARSE_WARM_SHA,
            corrected_anchor_hook_sha256=anchor['current_anchor_hook_sha256'],preparation_file=str(metadata),preparation_sha256=sha(metadata),
            complete_mean_angular=1552,new_fine_modes_preserved_as_baseline=True,fine_control_derivative_claim=False)
        temporary=report_path.with_name(report_path.name+'.fine-warm-provenance.tmp');temporary.write_text(json.dumps(report,indent=2)+'\n');temporary.replace(report_path)
        print(json.dumps(dict(event='actual_fine_complete_mean_coarse_warm_finished',path=str(report_path),sha256=sha(report_path),new_solution=False)),flush=True)
    finally:coarse._ACTIVE,entry.main,sys.argv=oldactive,oldmain,oldargv

if __name__=='__main__':main()
