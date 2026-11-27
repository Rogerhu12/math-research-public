#!/usr/bin/env python3
"""Freeze the entire actual run08 chart as an independent target and restore old G.

The current 7c4c chart is a new fixed mathematical input, not the historical
90e6 chart. Its complete 160 literal words, scalar/model/domain definition and
whole reference identity are saved before any new field evaluation. No old
target/field/geometry identity or angle conjugacy is inherited.

The complete historical dc5 observation carrier is nevertheless reconstructed
with the original scalar parameters, observed 2397 leaves and all original
array arithmetic, accepting only its whole SHA and 227202 bytes. That historical
input supplies all old material addresses, not old physical values. The new
consumer must retain P0 plus complete old/current grids and unresolved parallel
typed-history obligations. This is not a reduced address sample or a repair
that simply relabels the old chart constant.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import ast
import gzip
import hashlib
import heapq
import importlib.util
import json
import math
import os
import re
import subprocess
import struct
import sys
import time

SCHEMA = 'independent-run08-fixed-current-chart-and-complete-run05-carrier-input-v1'
PARENT_COMPLETE_SOURCE_SHA256 = '6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19'
BINDING_SCHEMA = 'material-envelope-independent-fixed-chart-binding-v1'
REFERENCE_SHA = '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'
OBSERVED_SHA = '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d'
DEEP_SHA = 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
WARM_SOURCE_SHA = 'bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3'
OLD_RECORD_SHA = '6eca69a388330b3e539aac4e2c793ce8256c724d52abf11adc8c8e85d49d08b3'
OLD_CARRIER_SHA = 'dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0'
WARM_SHA = '3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c'
PARAMETERS_SHA = 'e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa'
OLD_METRIC_KEY = 'axisymmetric-R690-reference-v2-first/report.json'
OLD_STEP = 'independent-axisymmetric-R690-reference-prepare-v2-first-20261126-05'
CURRENT_STEP = 'independent-axisymmetric-R690-reference-prepare-v2-first-20261127-08'
TOPIC = 'topics/visible-flex-larger-amplitude'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('This complete input reconstruction requires public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def event(**value):
    print(json.dumps(value, separators=(',', ':'), allow_nan=False), flush=True)


def load(name, path, expected):
    if sha(path) != expected:
        raise ValueError('Changed complete source: '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def read_public_step(path, expected_sha, step, carrier, *, historical=False):
    if sha(path) != expected_sha:
        raise ValueError('Changed complete public actual-return volume')
    text = Path(path).read_text()
    candidates = []
    for block in re.findall(r'```json\s*\n(.*?)\n```', text, flags=re.S):
        value = json.loads(block)
        if value.get('name') == 'followup:'+step:
            candidates.append(value)
    if len(candidates) != 1:
        raise ValueError('The requested actual preparation must occur exactly once')
    value = candidates[0]
    metrics = value.get('metrics', {}).get(OLD_METRIC_KEY)
    if (value.get('state') != 'completed' or value.get('returncode') != 0
            or not isinstance(metrics, dict) or metrics.get('complete') is not True
            or metrics.get('source_sha256') != REFERENCE_SHA
            or metrics.get('carrier') != carrier
            or (historical and metrics.get('original_warm') != WARM_SHA)
            or metrics.get('scalar_parameters') != PARAMETERS_SHA
            or [metrics.get(k) for k in ('M','J','P','N')] != [160,923,7377,2048]
            or metrics.get('scalar_complete_tail') is not True):
        raise ValueError('The public record is not the full actual reference input')
    for key in ('original_warm','node','scalar_input','carrier','reference','model','fixed_profile'):
        _digest(metrics.get(key),'public metric '+key)
    outputs = {Path(v['path']).name:v for v in value['outputs']}
    for filename, metric in (('observations.npz','carrier'),('reference.npz','reference')):
        if outputs.get(filename, {}).get('sha256') != metrics[metric]:
            raise ValueError('Public output identity disagrees with its actual metric')
    command = value['command']
    def argument(name):
        if command.count(name) != 1:
            raise ValueError('Actual command lacks a unique '+name)
        return command[command.index(name)+1]
    parameters = dict(angles=int(argument('--angles')),
        panels=int(argument('--panels')),
        seed_integration_order=int(argument('--seed-integration-order')),
        integral_tolerance=argument('--scalar-integral-tolerance'),
        tail_cutoff=argument('--scalar-tail-cutoff'),
        clock_admission_seconds=float(argument('--scalar-admission-seconds')))
    if (parameters != dict(angles=2048,panels=128,seed_integration_order=8,
            integral_tolerance='1e-18',tail_cutoff='1/8',clock_admission_seconds=300.0)
            or not isinstance(metrics.get('scalar_tolerance_reached'), bool)
            or (historical and metrics['scalar_tolerance_reached'] is not False)):
        raise ValueError('Keep the complete original parameters and actual accuracy status')
    return value, metrics, outputs, parameters


def bind_actual_current_public_step(args):
    """Bind this run's true complete return; never reuse run07's output identities."""
    run = os.environ.get('GITHUB_RUN_ID', '')
    attempt = os.environ.get('GITHUB_RUN_ATTEMPT', '')
    runner_temp = os.environ.get('RUNNER_TEMP')
    if not run.isdecimal() or not attempt.isdecimal() or not runner_temp:
        raise ValueError('An actual public Actions run/attempt/workspace is required')
    expected_path = (args.repo/TOPIC/'notes'/
        ('2026-11-27-public-actions-'+run+'-'+attempt+'-part-001.md')).resolve()
    if args.current_public_record is not None and args.current_public_record.resolve() != expected_path:
        raise ValueError('Do not substitute another run public return for current input')
    args.current_public_record = expected_path
    if not expected_path.is_file() or not 0 < expected_path.stat().st_size < 60000:
        raise ValueError('The complete bounded current public return is not available')
    public_record = record(expected_path)
    source = expected_path.read_text()
    title = '# 公开Actions '+run+'/'+attempt+'：实际阶段 '
    run_url = 'https://github.com/Rogerhu12/math-research-public/actions/runs/'+run
    if not source.startswith(title) or '[运行]('+run_url+')' not in source:
        raise ValueError('The current public volume belongs to another actual run')
    carrier = record(args.current_carrier)
    value, metrics, outputs, parameters = read_public_step(
        expected_path, public_record['sha256'], CURRENT_STEP, carrier['sha256'])
    if (value.get('step_id') != CURRENT_STEP
            or value.get('source_sha256') != REFERENCE_SHA
            or not re.fullmatch(r'[0-9a-f]{40}', str(value.get('source_commit', '')))):
        raise ValueError('The actual current preparation source or stage changed')
    runwork = (Path(runner_temp)/('visible-larger-research-'+run+'-'+attempt)/'research').resolve()
    expected_inputs = {
        'observations.npz': (runwork/'axisymmetric-R690-reference-v2-first/observations.npz', args.current_carrier),
        'report.json': (runwork/'axisymmetric-R690-reference-v2-first/report.json', args.current_reference_report),
    }
    for name, (required_path, actual_path) in expected_inputs.items():
        output = outputs[name]
        actual = record(actual_path)
        if (actual_path.resolve() != required_path or Path(output['path']).resolve() != required_path
                or actual['sha256'] != output['sha256'] or actual['bytes'] != output['bytes']):
            raise ValueError('The actual current report/carrier differs from its returned output')
    expected_reference = runwork/'axisymmetric-R690-reference-v2-first/reference.npz'
    reference = record(expected_reference)
    returned_reference = outputs['reference.npz']
    if (Path(returned_reference['path']).resolve() != expected_reference
            or returned_reference['sha256'] != reference['sha256']
            or returned_reference['bytes'] != reference['bytes']):
        raise ValueError('The entire actual current reference output is required')
    if record(expected_path) != public_record or record(args.current_carrier) != carrier:
        raise ValueError('Current public evidence changed while it was bound')
    identity = dict(actual_run_id=run, actual_run_attempt=attempt,
        actual_complete_public_volume=public_record, actual_step_id=CURRENT_STEP,
        actual_reference_output=reference, actual_carrier=carrier,
        actual_preparation_report=record(args.current_reference_report),
        actual_source_commit=value['source_commit'], actual_source_sha256=REFERENCE_SHA,
        current_carrier_hash_inferred_from_run07=False,
        original_run05_sha_and_all_reconstruction_parameters_unchanged=True,
        complete_parent_restorer_source_sha256=PARENT_COMPLETE_SOURCE_SHA256,
        current_reported_scalar_tolerance_reached=metrics['scalar_tolerance_reached'],
        actual_current_warm_bundle_sha256=metrics['original_warm'])
    return (value, metrics, outputs, parameters), identity



COMPATIBILITY_SCHEMA = 'independent-current-chart-and-historical-carrier-input-binding-v1'
ORIGIN_ENVELOPE_SOURCE_SHA256 = 'c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'
ORIGIN_MESH_SHA256 = 'eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262'
ORIGIN_CHART_SHA256 = '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'
WARM_RECIPE_SHA256 = '561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4'
WARM_CONTROLLER_SOURCE_SHA256 = '067b3f2e14145a6f88b2d171c555f1174f0505b45a5aaf670c3ec2610f7c286d'
OLD_CARRIER_BYTES = 227202
WARM_MEMBERS = ('mesh','qjets','a_stages','radius','Hcap','width','fixed_core_first3',
                'circle_projection','a_stage_absolute_error','stage_time_absolute_error')
CONSUMED_WARM_PROJECTION = ('mesh','width','radius','qjets[0,0,1:161]','fixed_core_first3')
CURRENT_RECORD_KEYS = ('current_warm_bundle','current_node_report','current_scalar_input',
                       'current_carrier','current_preparation_report','current_reference_bundle')



CURRENT_CHART_SHA256 = '7c4c9b736c0c8081e9f00a131db5fb63af224aa64fb476c07c78c09b5288bb48'
CURRENT_REFERENCE_SHA256 = 'eeb55084744c60a5ed2e2bbb4343b01c73028a6ab61b1216142e4b3bf57dd6b4'
CURRENT_REFERENCE_MODEL_SHA256 = '492456a67601cac752dc8e5cb79c14eaccc7339b2d3206f0d570bb60b02c5c5e'
TARGET_SCHEMA = 'independent-run08-frozen-complete-scalar-and-material-chart-v1'


def chart_words_record(words):
    """Canonical full 160 binary64 words; no truncated coefficient surrogate."""
    if not isinstance(words,list) or len(words)!=160:
        raise ValueError('A complete 160-coefficient fixed chart is required')
    values=[]
    for word in words:
        if not isinstance(word,str):
            raise ValueError('The chart uses canonical literal binary64 hex strings')
        value=float.fromhex(word)
        if not math.isfinite(value) or value.hex()!=word:
            raise ValueError('The chart word is not a canonical finite binary64 value')
        values.append(value)
    raw=b''.join(struct.pack('<d',value) for value in values)
    digest=hashlib.sha256(b'float64')
    digest.update(json.dumps([160]).encode())
    digest.update(raw)
    return dict(dtype='float64',shape=[160],sha256=digest.hexdigest(),
        binary64_byte_order='little',all_words=len(values))


def fixed_target_definition(*, model, scalar_parameters, chart_words, node_definitions,
                            reference_bundle):
    if (canonical(model)!=CURRENT_REFERENCE_MODEL_SHA256
            or model.get('fixed_chart_core_sha256')!=CURRENT_CHART_SHA256
            or model.get('mesh_sha256')!=ORIGIN_MESH_SHA256
            or model.get('original_scalar_parameters_identity_sha256')!=PARAMETERS_SHA
            or canonical(scalar_parameters)!=PARAMETERS_SHA
            or chart_words_record(chart_words)['sha256']!=CURRENT_CHART_SHA256
            or [str(v) for v in chart_words[:3]]!=model.get('fixed_core_first3')
            or reference_bundle.get('sha256')!=CURRENT_REFERENCE_SHA256
            or len(node_definitions)!=923):
        raise ValueError('Freeze this entire actual new chart target, not the historical chart')
    return dict(schema=TARGET_SCHEMA,definition_source_sha256=sha(__file__),
        complete_current_reference_model=model,
        current_reference_model_identity_sha256=CURRENT_REFERENCE_MODEL_SHA256,
        complete_current_reference_bundle_sha256=CURRENT_REFERENCE_SHA256,
        complete_scalar_parameters=scalar_parameters,
        complete_scalar_parameters_identity_sha256=PARAMETERS_SHA,
        complete_current_fixed_scalar_profile_definition=model['fixed_scalar_profile_definition'],
        current_fixed_scalar_metric_identity_sha256=model['fixed_scalar_metric_identity_sha256'],
        fixed_chart_core_binary64_hex=list(chart_words),
        fixed_chart_core_array_record=chart_words_record(chart_words),
        exact_scalar_node_definitions=[list(v) for v in node_definitions],
        exact_scalar_node_definitions_identity_sha256=canonical(node_definitions),
        exact_node_recipe_source_sha256=WARM_SOURCE_SHA,
        complete_literal_mesh_array_sha256=ORIGIN_MESH_SHA256,
        exact_literal_width_hex=float(.05).hex(),
        mathematical_target='ds^2+a_R690(s)^2*dTheta_current(phi0)^2',
        fixed_chart='Theta_current is defined by all 160 literal coefficients in this definition',
        original_complete_scalar_source_sha256=REFERENCE_SHA,
        historical_original_chart_core_sha256=ORIGIN_CHART_SHA256,
        same_original_fixed_chart=False,same_mathematical_g_claimed=False,
        exact_old_to_new_chart_conjugacy_claimed=False,
        target_fixed_before_any_field_or_direction=True,
        current_free_core_does_not_redefine_target=True,
        current_free_height_is_not_a_target_parameter=True,
        old_and_current_literal_material_addresses_all_retained=True,
        historical_angles_reinterpreted_as_new_fixed_chart_phi0=True,
        same_historical_physical_points_claimed=False,
        unknown_parallel_typed_priorities_reconstructed=False,
        unresolved_parallel_history_remains_an_explicit_obligation=True,
        original_branch_replaced_or_declared_finished=False,
        old_field_values_or_scientific_certificates_inherited=False)


def validate_fixed_target_definition(value, *, actual_model, reference_bundle, node):
    if not isinstance(value,dict):
        raise ValueError('Keep the entire independent fixed-target definition')
    definitions=[[str(F(v['S_coefficient'])),str(F(v['constant']))] for v in node['true_scalar_nodes']]
    expected=fixed_target_definition(model=actual_model,
        scalar_parameters=value.get('complete_scalar_parameters'),
        chart_words=value.get('fixed_chart_core_binary64_hex'),
        node_definitions=definitions,reference_bundle=reference_bundle)
    if value!=expected:
        raise ValueError('The complete new target definition differs from its actual files')
    return dict(schema=TARGET_SCHEMA,definition_identity_sha256=canonical(value),
        current_reference_model_identity_sha256=CURRENT_REFERENCE_MODEL_SHA256,
        current_fixed_chart_core_sha256=CURRENT_CHART_SHA256,
        historical_original_chart_core_sha256=ORIGIN_CHART_SHA256,
        same_original_fixed_chart=False,same_mathematical_g_claimed=False,
        old_values_or_certificates_inherited=False)


def _digest(value, name):
    if (not isinstance(value,str) or len(value)!=64
            or any(c not in '0123456789abcdef' for c in value)):
        raise ValueError('A complete actual SHA256 is required: '+name)
    return value


def _valid_record(value, name, *, reread=False):
    if (not isinstance(value,dict) or set(value)!=set(('path','sha256','bytes'))
            or not isinstance(value['path'],str) or not Path(value['path']).is_absolute()
            or type(value['bytes']) is not int or value['bytes']<=0):
        raise ValueError('Keep a complete actual file record: '+name)
    _digest(value['sha256'],name)
    if reread and record(value['path'])!=value:
        raise ValueError('The bound complete file changed: '+name)
    return value


def _bound_json(value, name):
    _valid_record(value,name)
    raw=Path(value['path']).read_bytes()
    if len(raw)!=value['bytes'] or hashlib.sha256(raw).hexdigest()!=value['sha256']:
        raise ValueError('The complete JSON snapshot changed: '+name)
    return json.loads(raw)


def _public_blocks(value):
    _valid_record(value,'public evidence')
    raw=Path(value['path']).read_bytes()
    if len(raw)!=value['bytes'] or hashlib.sha256(raw).hexdigest()!=value['sha256']:
        raise ValueError('The full public volume changed during binding')
    return [json.loads(block) for block in
            re.findall(r'\x60\x60\x60json\s*\n(.*?)\n\x60\x60\x60',raw.decode(),flags=re.S)]


def bind_actual_warm_return(args, current, identity):
    """Bind this run's entire real warm output, not the old warm digest."""
    blocks=_public_blocks(identity['actual_complete_public_volume'])
    matches=[value for value in blocks if value.get('name')=='warm']
    if len(matches)!=1:
        raise ValueError('The actual complete current warm return must occur once')
    value=matches[0]; metrics=value.get('metrics',{})
    source={entry['role']:entry for entry in value.get('input_files',[])}
    if (value.get('state')!='completed' or value.get('returncode')!=0
            or value.get('source_sha256')!=WARM_CONTROLLER_SOURCE_SHA256
            or source.get('recipe',{}).get('sha256')!=WARM_RECIPE_SHA256
            or source.get('hold_warm',{}).get('sha256')!=WARM_SOURCE_SHA
            or metrics.get('old_optimization_directions_started')!=0
            or [metrics.get(k) for k in ('M','J','cells')]!=[160,923,922]
            or metrics.get('hold_bundle_sha256')!=current['original_warm']
            or metrics.get('hold_report_sha256')!=current['node']
            or metrics.get('scalar_input_sha256')!=current['scalar_input']):
        raise ValueError('The current warm/node/scalar must be its actual complete producer return')
    outputs={Path(v['path']).name:v for v in value['outputs']}
    root=Path(os.environ['RUNNER_TEMP'])/(
        'visible-larger-research-'+identity['actual_run_id']+'-'+identity['actual_run_attempt'])/'research/fullclosed_solver/data'
    actual={}
    for key,argument,basename,metric in (
            ('current_warm_bundle',args.warm_bundle,'fullclosed-hold-warm.npz','original_warm'),
            ('current_node_report',args.node_report,'fullclosed-hold-warm.json','node'),
            ('current_scalar_input',args.scalar_input,'pulse-a5-complete-base.json.gz','scalar_input')):
        bound=record(argument);expected=(root/basename).resolve();output=outputs.get(basename)
        if (Path(argument).resolve()!=expected or not isinstance(output,dict)
                or Path(output['path']).resolve()!=expected
                or bound['sha256']!=current[metric] or bound['sha256']!=output.get('sha256')
                or bound['bytes']!=output.get('bytes')):
            raise ValueError('Current source input differs from the real full warm output: '+key)
        actual[key]=bound
    return dict(actual_files=actual,actual_warm_recipe_sha256=WARM_RECIPE_SHA256,
        actual_warm_producer_sha256=WARM_SOURCE_SHA,
        actual_warm_source_commit=value['source_commit'],
        actual_complete_public_volume=identity['actual_complete_public_volume'],
        historical_warm_digest_requirement_applied_to_current=False,
        old_warm_bundle_recreated_or_relabelled=False)


def verify_projection_origin(repo):
    """Read only the fixed origin constants from the entire original policy source."""
    path=Path(repo)/TOPIC/'scripts/resume_20261126/complete_material_envelope_memory.py'
    if sha(path)!=ORIGIN_ENVELOPE_SOURCE_SHA256:
        raise ValueError('The published whole original envelope input definition changed')
    tree=ast.parse(path.read_text())
    names={'ORIGIN_CARRIER_SHA','ORIGIN_CARRIER_BYTES','ORIGIN_WARM_SHA',
           'ORIGIN_PARAMETERS_SHA','ORIGIN_MESH_SHA','ORIGIN_CHART_SHA'}
    values={}
    for statement in tree.body:
        if isinstance(statement,ast.Assign):
            for target in statement.targets:
                if isinstance(target,ast.Name) and target.id in names:
                    if target.id in values:
                        raise ValueError('The original complete envelope has duplicate origin constants')
                    values[target.id]=ast.literal_eval(statement.value)
    expected=dict(ORIGIN_CARRIER_SHA=OLD_CARRIER_SHA,ORIGIN_CARRIER_BYTES=OLD_CARRIER_BYTES,
        ORIGIN_WARM_SHA=WARM_SHA,ORIGIN_PARAMETERS_SHA=PARAMETERS_SHA,
        ORIGIN_MESH_SHA=ORIGIN_MESH_SHA256,ORIGIN_CHART_SHA=ORIGIN_CHART_SHA256)
    if values!=expected:
        raise ValueError('Do not change the complete historical mesh/chart/carrier definition')
    return record(path)


def validate_independent_fixed_target_binding(value, *, actual_model, current_carrier,
        current_preparation_report, current_reference_bundle, current_node_report,
        current_scalar_input):
    """Pure stdlib, complete-file validation; no numerical field construction.

    Consumer arguments are its actual file_record dictionaries. The producer's
    full current warm, node, scalar, reference and preparation files are rehashed;
    no true flag or matching shape substitutes for those recorded whole bytes.
    """
    if (not isinstance(value,dict) or value.get('schema')!=COMPATIBILITY_SCHEMA
            or value.get('producer_source_sha256')!=sha(__file__)
            or value.get('origin_envelope_source_sha256')!=ORIGIN_ENVELOPE_SOURCE_SHA256
            or value.get('historical_warm_bundle_sha256')!=WARM_SHA
            or value.get('complete_scalar_parameters_sha256')!=PARAMETERS_SHA
            or canonical(value.get('complete_scalar_parameters'))!=PARAMETERS_SHA
            or value.get('current_mesh_sha256')!=ORIGIN_MESH_SHA256
            or value.get('historical_mesh_sha256')!=ORIGIN_MESH_SHA256
            or value.get('current_fixed_chart_core_sha256')!=CURRENT_CHART_SHA256
            or value.get('historical_fixed_chart_core_sha256')!=ORIGIN_CHART_SHA256
            or value.get('exact_node_recipe_source_sha256')!=WARM_SOURCE_SHA
            or value.get('consumed_warm_projection')!=list(CONSUMED_WARM_PROJECTION)
            or value.get('literal_width_hex')!=float(.05).hex()):
        raise ValueError('The current projection is not the complete declared independent fixed-chart input')
    supplied=dict(current_carrier=current_carrier,current_preparation_report=current_preparation_report,
        current_reference_bundle=current_reference_bundle,current_node_report=current_node_report,
        current_scalar_input=current_scalar_input)
    for key in CURRENT_RECORD_KEYS:
        _valid_record(value.get(key),key,reread=True)
        if key in supplied and value[key]!=supplied[key]:
            raise ValueError('Consumer current file differs from the producer binding: '+key)
    for key in ('historical_carrier','historical_public_return','current_public_return','origin_envelope_source'):
        _valid_record(value.get(key),key,reread=True)
    if (value['historical_carrier']['sha256']!=OLD_CARRIER_SHA
            or value['historical_carrier']['bytes']!=OLD_CARRIER_BYTES
            or value['historical_public_return']['sha256']!=OLD_RECORD_SHA
            or value['origin_envelope_source']['sha256']!=ORIGIN_ENVELOPE_SOURCE_SHA256
            or value.get('actual_current_model_identity_sha256')!=canonical(actual_model)
            or actual_model.get('source_sha256')!=REFERENCE_SHA
            or canonical(actual_model)!=CURRENT_REFERENCE_MODEL_SHA256
            or current_reference_bundle.get('sha256')!=CURRENT_REFERENCE_SHA256
            or actual_model.get('M')!=160 or actual_model.get('J')!=923
            or actual_model.get('original_warm_bundle_sha256')!=value['current_warm_bundle']['sha256']
            or actual_model.get('symbolic_node_report_sha256')!=current_node_report['sha256']
            or actual_model.get('scalar_input_sha256')!=current_scalar_input['sha256']
            or actual_model.get('observation_carrier_sha256')!=current_carrier['sha256']
            or actual_model.get('original_scalar_parameters_identity_sha256')!=PARAMETERS_SHA
            or actual_model.get('mesh_sha256')!=ORIGIN_MESH_SHA256
            or actual_model.get('fixed_chart_core_sha256')!=CURRENT_CHART_SHA256
            or actual_model.get('fixed_core_first3')!=value.get('fixed_core_first3_hex')
            or actual_model.get('fixed_scalar_metric_identity_sha256')!=value.get('actual_current_fixed_scalar_identity_sha256')
            or canonical(actual_model.get('fixed_scalar_profile_definition'))!=value.get('actual_current_fixed_scalar_identity_sha256')):
        raise ValueError('Full current model/files and declared new chart with original scalar/domain must agree')
    preparation=_bound_json(current_preparation_report,'actual current preparation')
    expected_solver=dict(reference_bundle=current_reference_bundle,carrier=current_carrier,
        node_report=current_node_report,scalar_input=current_scalar_input)
    if (preparation.get('schema')!='R690-independent-axisymmetric-SO3-preparation-v1'
            or preparation.get('source_sha256')!=REFERENCE_SHA or preparation.get('complete') is not True
            or preparation.get('reference_definition')!=actual_model
            or preparation.get('reference_model_identity_sha256')!=canonical(actual_model)
            or preparation.get('input_for_solver')!=expected_solver
            or preparation.get('old_warm_bundle')!=value['current_warm_bundle']
            or preparation.get('old_warm_node_report')!=current_node_report
            or [preparation.get(k) for k in ('M','J','P','N')]!=[160,923,7377,2048]):
        raise ValueError('Use the complete actual preparation, not independently assembled hashes')
    node=_bound_json(current_node_report,'actual current exact-node report')
    definitions=[[str(F(item['S_coefficient'])),str(F(item['constant']))]
                 for item in node['true_scalar_nodes']]
    if (node.get('source_sha256')!=WARM_SOURCE_SHA
            or node.get('schema')!='fullclosed-hold-real-pulse-warm-v1'
            or node.get('bundle_sha256')!=value['current_warm_bundle']['sha256']
            or node.get('input_sha256')!=current_scalar_input['sha256']
            or node.get('exact_core_affine') is not True
            or node.get('M')!=160 or node.get('J')!=923 or len(definitions)!=923
            or canonical(definitions)!=value.get('exact_symbolic_nodes_sha256')
            or node.get('width_carrier')!=float(.05)
            or node.get('width_exact')!=str(F(.05))):
        raise ValueError('The full current symbolic mesh source differs from the verified original recipe')
    target=value.get('fixed_target_definition')
    target_validation=validate_fixed_target_definition(target,actual_model=actual_model,
        reference_bundle=current_reference_bundle,node=node)
    if canonical(target)!=value.get('fixed_target_definition_identity_sha256'):
        raise ValueError('The complete independent fixed target identity changed')
    for key in ('same_complete_scalar_formula_verified','complete_current_fixed_material_chart_verified',
                'same_complete_symbolic_domain_verified','full_original_carrier_sha_verified',
                'actual_current_warm_return_bound','all_original_carrier_members_reconstructed'):
        if value.get(key) is not True:
            raise ValueError('A complete reconstruction obligation is unpaid: '+key)
    for key in ('same_original_fixed_chart','same_mathematical_g_claimed','exact_old_to_new_chart_conjugacy_claimed',
                'historical_whole_warm_recreated','historical_whole_warm_or_height_equality_claimed',
                'old_metric_or_geometry_values_inherited','current_files_relabelled_as_historical'):
        if value.get(key) is not False:
            raise ValueError('Current bytes or scientific conclusions were relabelled: '+key)
    # Actual scalar-file bytes and all exact projected values are checked here,
    # independently of the input model's recorded parameter digest.
    raw=Path(current_scalar_input['path']).read_bytes()
    if len(raw)!=current_scalar_input['bytes'] or hashlib.sha256(raw).hexdigest()!=current_scalar_input['sha256']:
        raise ValueError('The current complete scalar snapshot changed')
    scalar=json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
    parameters=dict(analytic_extension_origin=scalar['analytic_extension_origin'],
        geometry=scalar['fixed_scalar_profile']['geometry'])
    if parameters!=value['complete_scalar_parameters'] or canonical(parameters)!=PARAMETERS_SHA:
        raise ValueError('The actual current scalar has a different complete mathematical projection')
    # Public evidence is matched independently to the actual current files.
    blocks=_public_blocks(value['current_public_return'])
    prepares=[v for v in blocks if v.get('step_id')==CURRENT_STEP]
    warms=[v for v in blocks if v.get('name')=='warm']
    if len(prepares)!=1 or len(warms)!=1:
        raise ValueError('The whole actual current warm and preparation returns are required')
    step=prepares[0]; metrics=step.get('metrics',{}).get(OLD_METRIC_KEY,{})
    warm=warms[0]; wm=warm.get('metrics',{})
    outputs={Path(item['path']).name:item for item in step.get('outputs',[])}
    for key,filename,metric in (('current_carrier','observations.npz','carrier'),
            ('current_reference_bundle','reference.npz','reference'),
            ('current_preparation_report','report.json',None)):
        if outputs.get(filename)!=value[key] or (metric is not None and metrics.get(metric)!=value[key]['sha256']):
            raise ValueError('Public actual preparation output differs from the whole current file: '+key)
    if (step.get('state')!='completed' or step.get('returncode')!=0
            or step.get('source_sha256')!=REFERENCE_SHA or metrics.get('complete') is not True
            or metrics.get('model')!=canonical(actual_model)
            or metrics.get('original_warm')!=value['current_warm_bundle']['sha256']
            or metrics.get('node')!=current_node_report['sha256']
            or metrics.get('scalar_input')!=current_scalar_input['sha256']
            or metrics.get('scalar_parameters')!=PARAMETERS_SHA
            or warm.get('state')!='completed' or warm.get('returncode')!=0
            or warm.get('source_sha256')!=WARM_CONTROLLER_SOURCE_SHA256
            or wm.get('hold_bundle_sha256')!=value['current_warm_bundle']['sha256']
            or wm.get('hold_report_sha256')!=current_node_report['sha256']
            or wm.get('scalar_input_sha256')!=current_scalar_input['sha256']):
        raise ValueError('Current mathematical projection is not bound to its genuine complete public inputs')
    return dict(schema=COMPATIBILITY_SCHEMA,producer_source_sha256=sha(__file__),
        independent_fixed_target_binding_identity_sha256=canonical(value),
        actual_current_model_identity_sha256=canonical(actual_model),
        actual_current_warm_bundle_sha256=value['current_warm_bundle']['sha256'],
        historical_warm_bundle_sha256=WARM_SHA,
        current_and_historical_whole_warm_equal=value['current_warm_bundle']['sha256']==WARM_SHA,
        historical_whole_warm_or_height_equality_claimed=False,
        complete_scalar_parameters_sha256=PARAMETERS_SHA,current_mesh_sha256=ORIGIN_MESH_SHA256,
        current_fixed_chart_core_sha256=CURRENT_CHART_SHA256,
        historical_original_chart_core_sha256=ORIGIN_CHART_SHA256,
        fixed_target_definition_identity_sha256=canonical(target),
        independent_fixed_target=target_validation,
        same_original_fixed_chart=False,same_mathematical_g_claimed=False,
        exact_symbolic_nodes_sha256=value['exact_symbolic_nodes_sha256'],
        historical_carrier_sha256=OLD_CARRIER_SHA,historical_carrier_bytes=OLD_CARRIER_BYTES,
        whole_old_carrier_and_full_current_input_bytes_rechecked=True,
        same_complete_scalar_formula=True,complete_current_fixed_chart_verified=True,
        all_historical_and_current_material_addresses_still_required=True,
        scientific_certificates_inherited=False)


def exact_node_definitions(mesh, full, width):
    """The complete bee5 node formula, using its unchanged literal prefix."""
    if len(mesh) != 923 or F(float(mesh[0])) != 0 or F(float(mesh[818])) != 1:
        raise ValueError('The complete original 819-node prefix is required')
    w_exact = F(float(width))
    if w_exact != F(.05):
        raise ValueError('Changed complete original literal lift width')
    nodes = [(F(0),F(float(s))) for s in mesh[:819]]
    fixed_rise_start = full.cut+full.f+full.hold
    fixed_rise_end = fixed_rise_start+full.rise
    segments = [((F(0),F(1)),(F(0),fixed_rise_start),4),
        ((F(0),fixed_rise_start),(F(0),fixed_rise_end),8),
        ((F(0),fixed_rise_end),(F(1),-w_exact),64),
        ((F(1),-w_exact),(F(1),-full.out),12),
        ((F(1),-full.out),(F(1),F(0)),16)]
    for left,right,count in segments:
        if nodes[-1] != left:
            raise ValueError('The original symbolic segments do not concatenate')
        for j in range(1,count+1):
            t = F(j,count)
            nodes.append(((1-t)*left[0]+t*right[0],(1-t)*left[1]+t*right[1]))
    if len(nodes) != 923:
        raise ValueError('The complete node formula has changed')
    return nodes


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


def compare_member(np, left, right):
    if (left.dtype != right.dtype or left.shape != right.shape):
        return False
    return np.ascontiguousarray(left).tobytes() == np.ascontiguousarray(right).tobytes()


def array_record(reference, value):
    return dict(dtype=str(value.dtype),shape=list(value.shape),
                sha256=reference.array_sha(value))


def execute(args, report):
    import numpy as np
    started = time.monotonic()
    repo = args.repo.resolve()
    topic = repo/TOPIC
    reference_path = topic/'scripts/resume_20261126/so3_axisymmetric_reference.py'
    ref = load('_restore_run05_reference',reference_path,REFERENCE_SHA)
    paths,modules = ref.paths_and_modules(repo)
    if (ref.SOURCE_PINS['observed'][1] != OBSERVED_SHA
            or ref.SOURCE_PINS['deep_scalar'][1] != DEEP_SHA
            or ref.SOURCE_PINS['warm_producer'][1] != WARM_SOURCE_SHA):
        raise ValueError('The complete original source role binding changed')
    old_step,old,old_outputs,old_args = read_public_step(
        args.historical_public_record,OLD_RECORD_SHA,OLD_STEP,OLD_CARRIER_SHA,historical=True)
    current_result,current_identity = bind_actual_current_public_step(args)
    current_step,current,current_outputs,current_args = current_result
    report['actual_current_public_binding'] = current_identity
    warm_return = bind_actual_warm_return(args,current,current_identity)
    report['actual_current_warm_public_binding'] = warm_return
    origin_source = verify_projection_origin(repo)
    if int(old['scalar_leaves']) != 2397:
        raise ValueError('The historical live-leaf evidence changed')
    for path,expected in (
            (args.warm_bundle,current['original_warm']),
            (args.node_report,current['node']),
            (args.scalar_input,current['scalar_input']),
            (args.current_carrier,current['carrier']),
            (args.current_reference_report,current_outputs['report.json']['sha256'])):
        if sha(path) != expected:
            raise ValueError('Changed actual current input '+str(path))
    current_report = json.loads(args.current_reference_report.read_text())
    current_model = current_report['reference_definition']
    if (current_report.get('schema') != ref.PREPARATION_SCHEMA
            or current_report.get('source_sha256') != REFERENCE_SHA
            or current_report.get('complete') is not True
            or current_report.get('reference_model_identity_sha256') != current['model']
            or canonical(current_model) != current['model']
            or current_model.get('observation_carrier_sha256') != current['carrier']
            or current_model.get('original_warm_bundle_sha256') != current['original_warm']
            or current_model.get('symbolic_node_report_sha256') != current['node']
            or current_model.get('scalar_input_sha256') != current['scalar_input']
            or current_model.get('original_scalar_parameters_identity_sha256') != PARAMETERS_SHA
            or current_model.get('source_sha256') != REFERENCE_SHA
            or canonical(current_model)!=CURRENT_REFERENCE_MODEL_SHA256
            or current_identity['actual_reference_output']['sha256']!=CURRENT_REFERENCE_SHA256):
        raise ValueError('Current full preparation/model binding is incomplete')
    node = json.loads(args.node_report.read_text())
    if (node.get('schema') != 'fullclosed-hold-real-pulse-warm-v1'
            or node.get('source_sha256') != WARM_SOURCE_SHA
            or node.get('bundle_sha256') != current['original_warm']
            or node.get('input_sha256') != current['scalar_input']
            or node.get('M') != 160 or node.get('J') != 923
            or node.get('exact_core_affine') is not True):
        raise ValueError('Current warm/node/scalar source closure is incomplete')
    with np.load(args.warm_bundle,allow_pickle=False) as data:
        warm = {key:np.array(data[key],copy=True) for key in data.files}
    if set(warm)!=set(WARM_MEMBERS):
        raise ValueError('Keep all ten actual original warm-producer members')
    mesh = np.array(warm['mesh'],copy=True)
    if (mesh.shape != (923,) or warm['qjets'].shape != (923,3,482)
            or not np.isfinite(mesh).all() or not np.all(np.diff(mesh)>0)):
        raise ValueError('The original complete warm layout changed')
    core = np.array(warm['qjets'][0,0,1:161],copy=True)
    if (str(mesh.dtype)!='float64' or str(core.dtype)!='float64'
            or str(warm['qjets'].dtype)!='float64'
            or str(warm['fixed_core_first3'].dtype)!='float64'
            or warm['fixed_core_first3'].shape!=(3,)
            or core.shape!=(160,) or not np.isfinite(core).all()
            or not np.array_equal(core[:3],warm['fixed_core_first3'])):
        raise ValueError('Keep the complete real fixed-core projection and original first three words')
    if (ref.array_sha(mesh)!=ORIGIN_MESH_SHA256 or ref.array_sha(core)!=CURRENT_CHART_SHA256
            or current_model.get('mesh_sha256')!=ORIGIN_MESH_SHA256
            or current_model.get('fixed_chart_core_sha256')!=CURRENT_CHART_SHA256
            or current_model.get('fixed_core_first3')!=[float(v).hex() for v in core[:3]]):
        raise ValueError('The actual whole mesh or entire new fixed chart differs from this independent input')
    report['actual_warm_member_records'] = {key:array_record(ref,warm[key]) for key in WARM_MEMBERS}
    report['current_consumed_projection'] = dict(
        mesh_sha256=ref.array_sha(mesh),fixed_chart_core_sha256=ref.array_sha(core),
        fixed_core_first3_hex=[float(v).hex() for v in core[:3]],
        consumed_projection=list(CONSUMED_WARM_PROJECTION),
        current_complete_warm_sha256=current['original_warm'],
        historical_complete_warm_sha256=WARM_SHA,
        current_and_historical_whole_warm_equal=current['original_warm']==WARM_SHA,
        whole_warm_or_height_equality_inferred=False,
        historical_chart_core_sha256=ORIGIN_CHART_SHA256,
        same_original_fixed_chart=False,same_mathematical_g_claimed=False)
    raw = ref.read_scalar(args.scalar_input)
    projected = ref.scalar_parameters(raw)
    if canonical(projected) != PARAMETERS_SHA:
        raise ValueError('Complete mathematical scalar parameters differ from old actual input')
    full = modules['scalar'].FullHold(raw,paths['integer'],paths['hold'],panels=old_args['panels'])
    if full.carrier(full.S) != float(mesh[-1]) or full.carrier(full.R) != float(warm['radius']):
        raise ValueError('The actual consumed warm endpoints do not fit the exact scalar')
    if any(warm[key].shape!=() or str(warm[key].dtype)!='float64'
            or not np.isfinite(warm[key]).all() for key in ('width','radius','Hcap')):
        raise ValueError('Keep the genuine scalar carrier words in the complete warm input')
    width = float(warm['width'])
    definitions = exact_node_definitions(mesh,full,width)
    actual_definitions = [(F(v['S_coefficient']),F(v['constant']))
                          for v in node['true_scalar_nodes']]
    if definitions != actual_definitions:
        raise ValueError('Current symbolic nodes differ from the exact original producer recipe')
    if definitions[0] != (F(0),F(0)) or definitions[-1] != (F(1),F(0)):
        raise ValueError('Original symbolic endpoint definitions changed')
    # Current model and node provenance stay current.  This old input_identity
    # is the genuinely recorded ORIGINAL definition, not a claim that the
    # current scalar file has the original scalar file digest.
    original_identity = dict(scalar_input=old['scalar_input'],
        scalar_source=ref.SOURCE_PINS['scalar'][1],
        integer_source=ref.SOURCE_PINS['integer'][1],
        hold_source=ref.SOURCE_PINS['hold'][1])
    report['source_and_parameter_binding'] = dict(
        reference=record(reference_path),
        dependencies={role:record(path) for role,path in paths.items()},
        historical_public_return=record(args.historical_public_record),
        current_public_return=record(args.current_public_record),
        current_full_preparation=record(args.current_reference_report),
        actual_current_inputs={role:record(path) for role,path in dict(
            warm_bundle=args.warm_bundle,node_report=args.node_report,
            scalar_input=args.scalar_input,current_carrier=args.current_carrier).items()},
        original_recorded_scalar_file_sha256=old['scalar_input'],
        current_actual_scalar_file_sha256=current['scalar_input'],
        original_recorded_node_report_sha256=old['node'],
        current_actual_node_report_sha256=current['node'],
        original_scalar_file_recreated=False,original_node_report_recreated=False,
        current_files_relabelled_as_historical=False,
        complete_scalar_parameters_sha256=canonical(projected),
        scalar_projection_keys=['analytic_extension_origin','fixed_scalar_profile.geometry'],
        original_profile_input_identity=original_identity,
        exact_node_recipe_source_sha256=WARM_SOURCE_SHA,
        exact_symbolic_nodes_sha256=canonical([[str(a),str(b)] for a,b in definitions]),
        exact_node_recipe_matches_current_report=True,
        historical_full_warm_bundle_sha256=WARM_SHA,
        current_actual_full_warm_bundle_sha256=current['original_warm'],
        whole_warm_or_height_equality_claimed=False,
        actual_current_projection=report['current_consumed_projection'],
        original_envelope_input_source=origin_source,
        original_recorded_preparation_source_commit=old_step['source_commit'],
        current_recorded_preparation_source_commit=current_step['source_commit'])
    deep_module = modules['deep_scalar']
    ReconstructedTail = counted_tail_class(deep_module)
    deep = ReconstructedTail(full,original_input_identity=original_identity,
        target_leaves=int(old['scalar_leaves']),epsilon=F(old_args['tail_cutoff']),
        integral_tolerance=F(old_args['integral_tolerance']),
        historical_clock_seconds=old_args['clock_admission_seconds'])
    report['scalar_reconstruction'] = dict(
        control='exact recorded live-leaf count; original complete integer arithmetic',
        original_live_leaves=int(old['scalar_leaves']),
        actual_live_leaves=len(deep.leaves),
        actual_evaluated_leaves=deep.leaves_evaluated,
        original_clock_admission_seconds=old_args['clock_admission_seconds'],
        wall_clock_stop_replayed=False,wall_clock_budget_imposed=False,
        integral_uncertainty_exact=str(deep.integral_uncertainty),
        recorded_integral_uncertainty_exact=old['scalar_width_exact'],
        original_requested_accuracy_reached=old['scalar_tolerance_reached'],
        reconstructed_requested_accuracy_reached=deep.requested_integral_accuracy_reached,
        all_infinite_tail_included=True,
        original_complete_scalar_definition=deep.definition,
        reconstructed_profile_identity_sha256=deep.model_identity_sha256,
        original_profile_identity_sha256=old['fixed_profile'])
    if (deep.integral_uncertainty != F(old['scalar_width_exact'])
            or deep.requested_integral_accuracy_reached is not False
            or deep.model_identity_sha256 != old['fixed_profile']):
        raise ArithmeticError('Recorded exact scalar computation was not reproduced')
    radius,radius_error = ref.midpoint_and_error(deep.R,deep_module.SCALE)
    if radius.hex() != old['radius'] or radius_error != old['radius_error']:
        raise ArithmeticError('Recorded original radius word/error were not reproduced')
    breaks = [j for j,v in enumerate(definitions) if v == (F(1),-F(width))]
    if len(breaks) != 1:
        raise ValueError('Original exact symbolic observation breakpoint is not unique')
    plan = modules['observed'].make_plan(mesh,width,order=6,lift_break_node=breaks[0])
    if len(plan.cells) != 7377 or plan.legacy_count != 1845:
        raise ValueError('Every original positive observation is required')
    a,ae,te = [],[],[]
    for index,(cell,u,tc) in enumerate(zip(plan.cells,plan.local_u,plan.times)):
        definition = ref.point_definition(definitions,int(cell),float(u))
        value,error = ref.midpoint_and_error(
            ref.target_a_box(full,deep,deep_module,definition),deep_module.SCALE)
        a.append(value);ae.append(error)
        sb = full.affine_time(*definition)
        te.append(ref.upper_float(max(
            abs(F(float(tc))-F(sb[0],full.h.S)),
            abs(F(float(tc))-F(sb[1],full.h.S)))))
        if (index+1)%1024 == 0:
            event(event='reconstructed_old_carrier_observations',
                  completed=index+1,total=7377)
    a,ae,te = np.asarray(a),np.asarray(ae),np.asarray(te)
    if not np.isfinite(a).all() or np.any(a<=0):
        raise ArithmeticError('Each old fixed scalar observation must remain positive')
    carrier_path = args.outdir/'run05-observations-restored.npz'
    # Exact original keyword order, dtype construction and array content.
    # Save-container compatibility is VERIFIED by whole-file SHA, never assumed.
    np.savez_compressed(carrier_path,**plan.arrays(),mesh=mesh,a_stages=a[:1845],
        a_observations=a,a_observation_absolute_error=ae,observation_time_absolute_error=te,
        radius=np.array(radius),width=np.array(width),fixed_core_first3=core[:3],
        fixed_scalar_metric_identity_sha256=np.array(deep.model_identity_sha256))
    actual = record(carrier_path)
    report['restored_carrier_candidate'] = actual
    report['expected_original_carrier'] = dict(sha256=OLD_CARRIER_SHA,
        bytes=old_outputs['observations.npz']['bytes'],
        original_path=old_outputs['observations.npz']['path'])
    report['full_original_carrier_sha_match'] = actual['sha256'] == OLD_CARRIER_SHA
    if (actual['sha256'] != OLD_CARRIER_SHA
            or actual['bytes'] != old_outputs['observations.npz']['bytes']):
        raise ArithmeticError('Complete old carrier SHA mismatch; no old address identity is established')
    with np.load(args.current_carrier,allow_pickle=False) as data:
        current_arrays = {key:np.array(data[key],copy=True) for key in data.files}
    with np.load(carrier_path,allow_pickle=False) as data:
        restored = {key:np.array(data[key],copy=True) for key in data.files}
    comparisons = {}
    for key in plan.arrays():
        if key not in current_arrays:
            raise ValueError('Current carrier lacks complete plan member '+key)
        comparisons[key] = dict(
            original=array_record(ref,restored[key]),
            current=array_record(ref,current_arrays[key]),
            byte_identical=compare_member(np,restored[key],current_arrays[key]))
    addresses_equal = all(comparisons[k]['byte_identical']
                          for k in ('observation_cells','observation_u'))
    report['complete_plan_array_comparison'] = comparisons
    report['actual_original_gauss_unit_nodes_hex'] = [
        float(v).hex() for v in restored['observation_gauss_unit_nodes']]
    report['actual_current_gauss_unit_nodes_hex'] = [
        float(v).hex() for v in current_arrays['observation_gauss_unit_nodes']]
    report['current_and_original_material_radial_addresses_byte_identical'] = addresses_equal
    target=fixed_target_definition(model=current_model,scalar_parameters=projected,
        chart_words=[float(v).hex() for v in core],
        node_definitions=[[str(a),str(b)] for a,b in definitions],
        reference_bundle=current_identity['actual_reference_output'])
    target_path=args.outdir/'independent-fixed-target-definition.json'
    target_path.write_text(json.dumps(target,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n')
    report['independent_fixed_target_definition_file']=record(target_path)
    report['independent_fixed_target_definition_identity_sha256']=canonical(target)
    compatibility = dict(schema=COMPATIBILITY_SCHEMA,producer_source_sha256=sha(__file__),
        fixed_target_definition=target,fixed_target_definition_identity_sha256=canonical(target),
        origin_envelope_source_sha256=ORIGIN_ENVELOPE_SOURCE_SHA256,
        origin_envelope_source=origin_source,
        current_warm_bundle=record(args.warm_bundle),
        current_node_report=record(args.node_report),current_scalar_input=record(args.scalar_input),
        current_carrier=record(args.current_carrier),current_preparation_report=record(args.current_reference_report),
        current_reference_bundle=current_identity['actual_reference_output'],
        historical_carrier=actual,historical_public_return=record(args.historical_public_record),
        current_public_return=current_identity['actual_complete_public_volume'],
        historical_warm_bundle_sha256=WARM_SHA,
        actual_current_model_identity_sha256=canonical(current_model),
        actual_current_fixed_scalar_identity_sha256=current_model['fixed_scalar_metric_identity_sha256'],
        complete_scalar_parameters=projected,complete_scalar_parameters_sha256=canonical(projected),
        historical_mesh_sha256=ORIGIN_MESH_SHA256,current_mesh_sha256=ref.array_sha(mesh),
        historical_fixed_chart_core_sha256=ORIGIN_CHART_SHA256,
        current_fixed_chart_core_sha256=ref.array_sha(core),
        fixed_core_first3_hex=[float(v).hex() for v in core[:3]],
        exact_symbolic_nodes_sha256=canonical([[str(a),str(b)] for a,b in definitions]),
        exact_node_recipe_source_sha256=WARM_SOURCE_SHA,literal_width_hex=width.hex(),
        consumed_warm_projection=list(CONSUMED_WARM_PROJECTION),
        same_complete_scalar_formula_verified=True,complete_current_fixed_material_chart_verified=True,
        same_original_fixed_chart=False,same_mathematical_g_claimed=False,
        exact_old_to_new_chart_conjugacy_claimed=False,
        same_complete_symbolic_domain_verified=True,full_original_carrier_sha_verified=True,
        actual_current_warm_return_bound=True,all_original_carrier_members_reconstructed=True,
        historical_whole_warm_recreated=False,historical_whole_warm_or_height_equality_claimed=False,
        old_metric_or_geometry_values_inherited=False,current_files_relabelled_as_historical=False)
    validation = validate_independent_fixed_target_binding(compatibility,actual_model=current_model,
        current_carrier=record(args.current_carrier),current_preparation_report=record(args.current_reference_report),
        current_reference_bundle=current_identity['actual_reference_output'],
        current_node_report=record(args.node_report),current_scalar_input=record(args.scalar_input))
    report['independent_fixed_target_binding'] = compatibility
    report['independent_fixed_target_binding_validation'] = validation
    report['material_envelope_binding'] = dict(schema=BINDING_SCHEMA,
        independent_fixed_target_binding=compatibility,
        independent_fixed_target_binding_identity_sha256=canonical(compatibility),
        fixed_target_definition=target,fixed_target_definition_identity_sha256=canonical(target),
        origin_carrier=actual,current_carrier=record(args.current_carrier),
        producer=dict(source_sha256=sha(__file__),
            source_commit=report['source_commit'],
            reconstruction_scope='Independent complete current fixed chart; reconstruct full historical carrier only for its complete material-address responsibility, accepting only original whole SHA'),
        original_full_carrier_sha_verified=True,
        original_reference_report_sha256=old_outputs['report.json']['sha256'],
        actual_current_reference_report=record(args.current_reference_report),
        actual_cells_and_u_equal=addresses_equal,
        consumer_must_rehash_and_read_complete_arrays=True,
        surface_history_values_or_certificates_inherited=False)
    binding_path = args.outdir/'material-envelope-carrier-binding.json'
    write_json(binding_path,report['material_envelope_binding'])
    report['material_envelope_binding_file'] = record(binding_path)
    report['complete'] = True
    report['seconds'] = time.monotonic()-started
    report['scientific_scope'] = dict(input_reconstruction_only=True,
        reference_height_reintegrated=False,whole_reference_bundle_recreated=False,
        explicit_independent_new_fixed_material_chart=True,
        same_original_fixed_chart=False,same_mathematical_g_claimed=False,
        original_branch_replaced_or_declared_finished=False,
        physical_field_evaluations=0,Jacobian_evaluations=0,root_evaluations=0,
        nonlinear_optimization_replayed=False,
        old_metric_or_geometry_values_inherited=False,
        unknown_history_claimed_read=False,
        full_unknown_history_envelope_consumer_still_required=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo','warm-bundle','node-report','scalar-input','current-carrier',
                 'current-reference-report','historical-public-record','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--current-public-record',type=Path,default=None,
        help='Optional explicit path; if supplied it must be this actual run08 public volume')
    args = parser.parse_args()
    require_actions()
    args.repo = args.repo.resolve()
    args.outdir = args.outdir.resolve()
    if args.outdir.exists() or args.outdir == args.repo or args.repo in args.outdir.parents:
        raise ValueError('Use a fresh complete reconstruction output outside the repository')
    args.outdir.mkdir(parents=True)
    report = dict(schema=SCHEMA,source_sha256=sha(__file__),
        source_commit=subprocess.check_output(
            ['git','-C',str(args.repo),'rev-parse','HEAD'],text=True).strip(),
        complete=False,full_original_carrier_sha_match=False,
        current_and_original_material_radial_addresses_byte_identical=None,
        material_envelope_binding=None,
        requested_actions_run_id=os.environ.get('GITHUB_RUN_ID'),
        requested_actions_run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'))
    start = time.monotonic()
    try:
        execute(args,report)
    except Exception as exc:
        report['complete'] = False
        report['failure'] = dict(type=type(exc).__name__,message=str(exc))
        report['seconds'] = time.monotonic()-start
        write_json(args.outdir/'report.json',report)
        event(event='old_carrier_reconstruction_unavailable',report=record(args.outdir/'report.json'),
              failure=report['failure'])
        raise
    write_json(args.outdir/'report.json',report)
    event(event='old_carrier_reconstruction_complete',
          report_sha256=sha(args.outdir/'report.json'),
          carrier_sha256=report['restored_carrier_candidate']['sha256'],
          original_address_identity_verified=True,
          current_address_arrays_identical=report['current_and_original_material_radial_addresses_byte_identical'],
          nonlinear_solve=False)


if __name__ == '__main__':
    main()

