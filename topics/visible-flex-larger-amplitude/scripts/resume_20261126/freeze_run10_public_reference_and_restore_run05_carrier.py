#!/usr/bin/env python3
"""Freeze genuine completed run10 inputs and reconstruct the entire old carrier.

This independent source consumes the observed public stage 1/2 whole files,
including immutable complete public-text snapshots and all six actual inputs.
The complete 160 fixed-chart words are read from both genuine NPZ files, not
inferred from a changing report hash. Literal equality is reported separately
from an unclaimed mathematical target relation. No old field or certificate is
inherited.

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

SCHEMA = 'actual-public-run10-fixed-target-and-complete-run05-carrier-input-v1'
PARENT_COMPLETE_SOURCE_SHA256 = '9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18'
PUBLIC_INPUT_BINDING_SHA256 = '9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209'
PUBLIC_INPUT_BINDING_NAME = 'actual_public_run10_reference_input_binding.py'
BINDING_SCHEMA = 'material-envelope-actual-public-run10-fixed-target-binding-v1'
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
CURRENT_STEP = 'independent-axisymmetric-R690-reference-prepare-v2-first-20261127-10'
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


def public_input_module():
    path=Path(__file__).with_name(PUBLIC_INPUT_BINDING_NAME)
    module=load('_whole_actual_public_run10_inputs_'+PUBLIC_INPUT_BINDING_SHA256[:12],
        path,PUBLIC_INPUT_BINDING_SHA256)
    for name in ('public_evidence','full_reference_projection','freeze_target',
                 'validate_target','validate_compatibility'):
        if sha(getattr(module,name).__code__.co_filename)!=PUBLIC_INPUT_BINDING_SHA256:
            raise ValueError('The actual public-input validator body changed')
    return module


def bind_actual_current_public_step(args):
    module=public_input_module()
    if (os.environ.get('GITHUB_RUN_ID')!=module.RUN_ID
            or os.environ.get('GITHUB_RUN_ATTEMPT')!=module.RUN_ATTEMPT
            or args.actual_reference_step_id!=CURRENT_STEP):
        raise ValueError('This independent source is bound to the real run10 complete reference')
    files={key:record(path) for key,path in dict(current_warm_bundle=args.warm_bundle,
        current_node_report=args.node_report,current_scalar_input=args.scalar_input,
        current_carrier=args.current_carrier,current_preparation_report=args.current_reference_report,
        current_reference_bundle=args.current_reference_bundle).items()}
    commit=subprocess.check_output(['git','-C',str(args.repo),'rev-parse','HEAD'],text=True).strip()
    documents={}
    for key,path,expected in (
            ('warm',args.actual_public_warm_record,args.actual_public_warm_record_sha256),
            ('reference',args.actual_public_reference_record,args.actual_public_reference_record_sha256)):
        documents[key]=module.freeze_public_document(path,expected,args.repo,args.outdir,key,commit)
    evidence,step,metrics,outputs=module.public_evidence(documents,files,CURRENT_STEP)
    projection=module.full_reference_projection(files)
    if (canonical(projection['model'])!=metrics['model']
            or projection['model']['fixed_scalar_metric_identity_sha256']!=metrics['fixed_profile']):
        raise ValueError('The whole actual NPZ model differs from the genuine public return')
    args.current_public_record=Path(documents['reference']['snapshot_record']['path'])
    args.current_warm_public_record=Path(documents['warm']['snapshot_record']['path'])
    args._actual_public_evidence=evidence
    args._actual_reference_projection=projection
    result=read_public_step(args.current_public_record,documents['reference']['snapshot_record']['sha256'],
        CURRENT_STEP,files['current_carrier']['sha256'])
    if result[:3]!=(step,metrics,outputs):
        raise ValueError('Both complete public-source readers must select the same actual return')
    identity=dict(actual_run_id=module.RUN_ID,actual_run_attempt=module.RUN_ATTEMPT,
        actual_complete_public_volume=documents['reference']['snapshot_record'],
        actual_complete_warm_public_volume=documents['warm']['snapshot_record'],
        original_public_documents=documents,actual_step_id=CURRENT_STEP,
        actual_reference_output=files['current_reference_bundle'],
        actual_carrier=files['current_carrier'],actual_preparation_report=files['current_preparation_report'],
        actual_source_commit=step['source_commit'],actual_source_sha256=REFERENCE_SHA,
        public_input_binding_source=record(Path(__file__).with_name(PUBLIC_INPUT_BINDING_NAME)),
        actual_public_input_evidence=evidence,actual_public_input_evidence_identity_sha256=canonical(evidence),
        current_carrier_hash_inferred_from_run07=False,
        original_run05_sha_and_all_reconstruction_parameters_unchanged=True,
        complete_parent_restorer_source_sha256=PARENT_COMPLETE_SOURCE_SHA256,
        current_reported_scalar_tolerance_reached=metrics['scalar_tolerance_reached'],
        actual_current_warm_bundle_sha256=metrics['original_warm'])
    return result,identity


COMPATIBILITY_SCHEMA = 'actual-public-run10-fixed-target-and-historical-carrier-binding-v1'
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
# Whole actual run10 warm equals the recorded original warm; the complete
# chart words are nevertheless re-read and checked, not replaced by this fact.
CURRENT_CHART_SHA256 = '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'
CURRENT_REFERENCE_SHA256 = '512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b'
CURRENT_REFERENCE_MODEL_SHA256 = '081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5'
TARGET_SCHEMA = 'independently-frozen-actual-public-run10-scalar-and-material-chart-v1'


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


def fixed_target_definition(*,model,scalar_parameters,chart_words,node_definitions,
                            reference_bundle,public_evidence):
    module=public_input_module()
    projection=module.full_reference_projection(public_evidence['current_files'],expected_model=model)
    if (canonical(model)!=CURRENT_REFERENCE_MODEL_SHA256
            or chart_words_record(chart_words)['sha256']!=CURRENT_CHART_SHA256
            or reference_bundle['sha256']!=CURRENT_REFERENCE_SHA256
            or scalar_parameters!=projection['complete_scalar_parameters']
            or chart_words!=projection['fixed_chart_core_binary64_hex']
            or node_definitions!=projection['exact_scalar_node_definitions']
            or public_evidence['current_files']['current_reference_bundle']!=reference_bundle):
        raise ValueError('The complete actual run10 target differs from its returned source files')
    return module.freeze_target(producer_sha256=sha(__file__),evidence=public_evidence,
        projection=projection)


def validate_fixed_target_definition(value,*,actual_model,reference_bundle,node):
    return public_input_module().validate_target(value,producer_sha256=sha(__file__),
        actual_model=actual_model,reference_bundle=reference_bundle,node=node)


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


def bind_actual_warm_return(args,current,identity):
    module=public_input_module()
    evidence=identity['actual_public_input_evidence']
    checked,_,metrics,_=module.public_evidence(evidence['complete_public_documents'],
        evidence['current_files'],CURRENT_STEP)
    if checked!=evidence or metrics!=current:
        raise ValueError('The complete current warm/reference public binding changed')
    return dict(actual_files={k:evidence['current_files'][k] for k in (
            'current_warm_bundle','current_node_report','current_scalar_input')},
        actual_warm_recipe_sha256=WARM_RECIPE_SHA256,
        actual_warm_producer_sha256=WARM_SOURCE_SHA,
        actual_warm_source_commit=evidence['actual_warm_source_commit'],
        actual_complete_public_volume=evidence['complete_public_documents']['warm']['snapshot_record'],
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


def validate_independent_fixed_target_binding(value,*,actual_model,current_carrier,
        current_preparation_report,current_reference_bundle,current_node_report,current_scalar_input):
    return public_input_module().validate_compatibility(value,producer_sha256=sha(__file__),
        actual_model=actual_model,current_carrier=current_carrier,
        current_preparation_report=current_preparation_report,current_reference_bundle=current_reference_bundle,
        current_node_report=current_node_report,current_scalar_input=current_scalar_input)


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
        same_original_fixed_chart=(ref.array_sha(core)==ORIGIN_CHART_SHA256),same_mathematical_g_claimed=False)
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
        reference_bundle=current_identity['actual_reference_output'],
        public_evidence=current_identity['actual_public_input_evidence'])
    target_path=args.outdir/'independent-fixed-target-definition.json'
    target_path.write_text(json.dumps(target,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n')
    report['independent_fixed_target_definition_file']=record(target_path)
    report['independent_fixed_target_definition_identity_sha256']=canonical(target)
    compatibility = dict(schema=COMPATIBILITY_SCHEMA,producer_source_sha256=sha(__file__),
        public_input_binding_source_sha256=PUBLIC_INPUT_BINDING_SHA256,
        actual_public_input_evidence=current_identity['actual_public_input_evidence'],
        actual_public_input_evidence_identity_sha256=canonical(current_identity['actual_public_input_evidence']),
        fixed_target_definition=target,fixed_target_definition_identity_sha256=canonical(target),
        origin_envelope_source_sha256=ORIGIN_ENVELOPE_SOURCE_SHA256,
        origin_envelope_source=origin_source,
        current_warm_bundle=record(args.warm_bundle),
        current_node_report=record(args.node_report),current_scalar_input=record(args.scalar_input),
        current_carrier=record(args.current_carrier),current_preparation_report=record(args.current_reference_report),
        current_reference_bundle=current_identity['actual_reference_output'],
        historical_carrier=actual,historical_public_return=record(args.historical_public_record),
        current_public_return=current_identity['actual_complete_public_volume'],
        current_warm_public_return=current_identity['actual_complete_warm_public_volume'],
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
        same_original_fixed_chart=(ref.array_sha(core)==ORIGIN_CHART_SHA256),
        current_and_historical_fixed_chart_words_sha_equal=(ref.array_sha(core)==ORIGIN_CHART_SHA256),
        same_mathematical_g_claimed=False,
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
        same_original_fixed_chart=(ref.array_sha(core)==ORIGIN_CHART_SHA256),
        same_mathematical_g_claimed=False,
        historical_metric_relation='not claimed; different metadata SHA is not mathematical target inequality',
        original_branch_replaced_or_declared_finished=False,
        physical_field_evaluations=0,Jacobian_evaluations=0,root_evaluations=0,
        nonlinear_optimization_replayed=False,
        old_metric_or_geometry_values_inherited=False,
        unknown_history_claimed_read=False,
        full_unknown_history_envelope_consumer_still_required=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo','warm-bundle','node-report','scalar-input','current-carrier',
                 'current-reference-report','current-reference-bundle','historical-public-record','outdir',
                 'actual-public-warm-record','actual-public-reference-record'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--actual-public-warm-record-sha256',required=True)
    parser.add_argument('--actual-public-reference-record-sha256',required=True)
    parser.add_argument('--actual-reference-step-id',required=True)
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

