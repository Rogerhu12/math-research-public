#!/usr/bin/env python3
"""Hash source/JSON, parse AST/YAML and bash -n; execute no science."""
from pathlib import Path
import ast
import hashlib
import json
import re
import struct
import subprocess
import yaml

HERE=Path(__file__).resolve().parent
BASE=Path('/tmp/visible-larger-request97')
REPO=Path('/workspace/scratch/visible-larger-recovered-20261114-1843/math-research-public')
COMP=REPO/'topics/visible-flex-larger-amplitude/computations'
ACTUAL=Path('/tmp/visible-larger-recovery-2207/actions-debug/visible-mainline-smallcoreresonance-43676647334-1')
ENTRY='geometry_20261115_small_core_inexact_p3_eta_0p01.py'
ENTRY_SHA='f43c20ea6b8a5616b4330870897a1d0b6bd2c157435544366af1fe70dcdff7bd'
BASELINE='geometry_20261115_small_core_inexact_p3_restoration.py'
BASELINE_SHA='ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e'
STATUS_SHA='d55b5338880cabaae44bd7575db9a10bcba22fad4ae1fce0225f1ef38064f331'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def receipt(p): return dict(file=str(p),bytes=p.stat().st_size,sha256=sha(p))
def read(p): return json.loads(p.read_bytes())
def resolve(n,known):
    if isinstance(n,ast.Name): return known[n.id]
    if isinstance(n,ast.Dict): return {resolve(k,known):resolve(v,known) for k,v in zip(n.keys,n.values)}
    if isinstance(n,(ast.List,ast.Tuple,ast.Set)):
        values=[resolve(v,known) for v in n.elts]
        return tuple(values) if isinstance(n,ast.Tuple) else set(values) if isinstance(n,ast.Set) else values
    return ast.literal_eval(n)
def constants(tree):
    known={}
    for n in tree.body:
        if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name):
            try: known[n.targets[0].id]=resolve(n.value,known)
            except (KeyError,ValueError,TypeError): pass
    return known
def scripts(workflow):
    result={}
    for index,step in enumerate(workflow['jobs']['smallcoreresonance']['steps']):
        lines=step.get('run','').splitlines();i=0
        while i<len(lines):
            match=re.search(r"<<-?'([A-Z][A-Z0-9_]*)'",lines[i])
            if not match: i+=1;continue
            tag=match.group(1);i+=1;body=[]
            while i<len(lines) and lines[i]!=tag: body.append(lines[i]);i+=1
            assert i<len(lines) and tag not in result,tag
            result[tag]=dict(step=index,text='\n'.join(body)+'\n');i+=1
    return result

old_request=read(BASE/'public-small-core-resonance-request.json')
request=read(HERE/'public-small-core-resonance-request.json')
old_workflow=yaml.safe_load((BASE/'visible-larger-public-small-core-resonance.yml').read_text())
workflow=yaml.safe_load((HERE/'visible-larger-public-small-core-resonance.yml').read_text())
parent_path=ACTUAL/'small-core-inexact-p3-restoration/inexact-p3-restoration-status.json'
parent=read(parent_path)
source=HERE/ENTRY;source_text=source.read_text();values=constants(ast.parse(source_text))
assert sha(source)==ENTRY_SHA and source.stat().st_size==46126
assert sha(COMP/BASELINE)==BASELINE_SHA and (COMP/BASELINE).stat().st_size==45133
assert sha(parent_path)==STATUS_SHA and parent_path.stat().st_size==233256
assert (HERE/'actual97-original/inexact-p3-restoration-status.json').read_bytes()==parent_path.read_bytes()
assert len(request['source_sha256'])==73
assert {k:v for k,v in request['source_sha256'].items() if k!=ENTRY}==old_request['source_sha256']
assert request['source_sha256'][ENTRY]==ENTRY_SHA
assert request['inputs']==old_request['inputs'] and request['runtime']==old_request['runtime']
assert request['proofs']==old_request['proofs']
assert {k:v for k,v in request['diagnostic'].items() if k not in ('parameters','damping')}=={k:v for k,v in old_request['diagnostic'].items() if k not in ('parameters','damping')}
assert request['diagnostic']['damping']=='0.01'
assert request['diagnostic']['parameters']==parent['final']['parameters']==parent['last_accepted_parameters']
bits=[struct.pack('<d',v).hex() for v in request['diagnostic']['parameters']]
assert bits==[struct.pack('<d',v).hex() for v in parent['final']['parameters']]
assert request['scientific_source_unchanged'] is False
assert request['output_status_schema']==values['SCHEMA']!=parent['schema']
parent_closure=values['FROZEN'];current_closure={**parent_closure,ENTRY:ENTRY_SHA}
assert len(parent_closure)==13 and len(current_closure)==14
assert parent['consumed_source_sha256']==parent_closure
assert request['source_closure']['parent_producer']==parent_closure
assert request['source_closure']['current_producer']==current_closure
assert parent['input_sha256']==values['ORIGINAL_INPUTS']=={k:v['sha256'] for k,v in request['inputs'].items()}
assert parent['schema']==values['BASELINE_SCHEMA'] and parent['source_sha256']==values['BASELINE_SHA256']
assert values['ACTUAL97_STATUS_BYTES']==233256 and values['ACTUAL97_STATUS_SHA256']==STATUS_SHA
assert parent['last_accepted_point_semantics']=='original-three-merit-accepted-candidate-or-fresh-parent'
assert parent['phase']=='diagnostic-completed' and parent['diagnostic_completed'] is True
assert parent['success'] is False and parent['native_nonlinear_solver_called'] is False
assert parent['full_nonlinear_nonzero_lambda_solution_computed'] is False
assert 'exception' not in parent and parent['search_stop_reason']=='explicit outer direction budget completed'
assert len(parent['searches'])==8 and all(r['accepted'] is True for r in parent['searches'])
assert request['prior_candidate']['original_status']['sha256']==STATUS_SHA
assert request['prior_candidate']['producer_source_sha256']==BASELINE_SHA
assert request['prior_candidate']['parent_model_J_merit_or_state_reused'] is False
assert request['prior_candidate']['parameters_from_original_status_field']=='final.parameters'
assert request['prior_candidate']['parent_damping_cli_text']=='0.1'

# Recover every changed byte and independently recheck all unchanged function bodies.
producer_report=read(HERE/'request99-producer-source-only-check.json')
inverse=source_text
for item in reversed(producer_report['declared_literal_edits']):
    assert inverse.count(item['new'])==1
    inverse=inverse.replace(item['new'],item['old'],1)
assert inverse.encode()==(COMP/BASELINE).read_bytes()
old_defs={n.name:n for n in ast.parse(inverse).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
new_defs={n.name:n for n in ast.parse(source_text).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
assert old_defs.keys()==new_defs.keys()
function_checks=[]
for name,old_node in old_defs.items():
    new_node=new_defs[name]
    body_equal=ast.get_source_segment(inverse,old_node)==ast.get_source_segment(source_text,new_node)
    ast_equal=ast.dump(old_node,include_attributes=False)==ast.dump(new_node,include_attributes=False)
    if name not in ('checked_parent','main'): assert body_equal and ast_equal,name
    function_checks.append(dict(name=name,body_bytes_equal=body_equal,AST_equal=ast_equal))
scientific_tail='    start = time.monotonic()\n    try:\n'
assert source_text[source_text.index(scientific_tail):]==inverse[inverse.index(scientific_tail):]
assert 'if not math.isfinite(damping) or damping != .01:' in source_text
assert 'damping != .1:' not in source_text
assert "elif parent.get('schema') == SCHEMA:\n        expected_sources = sources\n        expected_producer = sources[ENTRY_NAME]" in source_text
assert "expected_sources = FROZEN\n        expected_producer = BASELINE_SHA256" in source_text
assert "parent_damping_binary64=parent.get('damping_binary64')" in source_text
parent_func=ast.get_source_segment(source_text,new_defs['checked_parent'])
assert parent_func.count('damping')==4
assert 'BASELINE_NAME' not in ast.get_source_segment(source_text,new_defs['original_module'])
assert "path = HERE/ORIGINAL_NAME" in ast.get_source_segment(source_text,new_defs['original_module'])

verified=[]
for name,want in request['source_sha256'].items():
    p=source if name==ENTRY else COMP/name
    assert p.is_file() and sha(p)==want,name
    if name.endswith('.py'): compile(ast.parse(p.read_bytes(),filename=name),name,'exec')
    verified.append(receipt(p))
identity_path=ACTUAL/'request97-input-and-source-identity.json'
identity=read(identity_path)
assert identity['source_commit']==request['prior_candidate']['source_commit']
assert {x['file']:x['sha256'] for x in identity['verified_sources']}==old_request['source_sha256']
actual_inputs={x['name']:{k:v for k,v in x.items() if k!='name'} for x in identity['verified_original_inputs']}
assert actual_inputs==request['inputs']
input_scope=[]
for name,item in request['inputs'].items():
    p=REPO/item['file'];exists=p.is_file()
    if exists: assert p.stat().st_size==item['bytes'] and sha(p)==item['sha256']
    input_scope.append(dict(name=name,descriptor=item,original97_verified_input_receipt_equal=True,
        local_payload_present=exists,local_payload_rehashed=exists,
        runtime_sparse_checkout_and_original_hash_check_retained=True))

assert workflow['on']==old_workflow['on'] and workflow['permissions']==old_workflow['permissions']
job=workflow['jobs']['smallcoreresonance'];oldjob=old_workflow['jobs']['smallcoreresonance']
assert {k:v for k,v in job.items() if k not in ('steps','name')}=={k:v for k,v in oldjob.items() if k not in ('steps','name')}
assert len(job['steps'])==len(oldjob['steps'])
assert workflow['on']['push']['paths']==['topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json']
changed_steps=[];shell_checks=[]
for i,(step,oldstep) in enumerate(zip(job['steps'],oldjob['steps'])):
    if step!=oldstep: changed_steps.append(dict(index=i,name=step.get('name',step.get('uses'))))
    if 'run' in step:
        result=subprocess.run(['bash','-n'],input=step['run'],text=True,capture_output=True)
        assert result.returncode==0,(i,result.stderr)
        shell_checks.append(dict(index=i,name=step.get('name'),bash_n_passed=True))
assert [x['index'] for x in changed_steps]==[0,4,6]
assert job['steps'][6]['run']==oldjob['steps'][6]['run']
new_inline=scripts(workflow);old_inline=scripts(old_workflow)
assert set(new_inline)==set(old_inline)=={'PYPINS','PYSOURCE','PYDIAGNOSTIC','PYREAD'}
inline_checks=[]
for label,item in new_inline.items():
    compile(ast.parse(item['text'],filename=label),label,'exec')
    same=item['text']==old_inline[label]['text']
    if label!='PYPINS': assert same,label
    inline_checks.append(dict(label=label,step=item['step'],AST_and_compile_passed=True,
        byte_identical_to_actual97=same,text_sha256=hashlib.sha256(item['text'].encode()).hexdigest()))
pins=constants(ast.parse(new_inline['PYPINS']['text']))
assert pins['expected']==request['diagnostic']
assert pins['source_chain']==request['source_chain']
assert pins['parent_sources']==parent_closure and pins['producer_sources']==current_closure
assert pins['expected_prior']==(request['prior_candidate']['original_status']['file'],233256,STATUS_SHA)
assert request['prior_candidate']['original_status']['file'] in job['steps'][0]['with']['sparse-checkout']
assert "(prior_output/'actual97-inexact-p3-restoration-status.json').write_bytes(prior_raw)" in new_inline['PYPINS']['text']
assert "(args.out/parent_receipt['file']).write_bytes(parent_raw)" in source_text
assert "state = model.evaluate(parameters)" in source_text
assert "status['initial'] = model.description(state)" in source_text
assert all('GH_TOKEN' not in step.get('env',{}) and 'GITHUB_TOKEN' not in step.get('env',{}) for step in job['steps'][:-1])
assert job['steps'][-1]['env']==oldjob['steps'][-1]['env']

report=dict(schema='request99-actual97-independent-fixed-eta-static-readback-v1',status='PASS-source-and-original-JSON-only',
    original_workflow=receipt(BASE/'visible-larger-public-small-core-resonance.yml'),
    original_request=receipt(BASE/'public-small-core-resonance-request.json'),
    workflow=receipt(HERE/'visible-larger-public-small-core-resonance.yml'),
    request=receipt(HERE/'public-small-core-resonance-request.json'),
    old_ce93_source=receipt(COMP/BASELINE),new_scientific_source=receipt(source),
    old_ce93_source_unchanged=True,new_scientific_source_not_the_old_entry=True,
    original_parent=receipt(parent_path),parent_copy=receipt(HERE/'actual97-original/inexact-p3-restoration-status.json'),
    parent_full_bytes_copied_not_reserialized=True,actual97_source_and_input_receipt=receipt(identity_path),
    source_pin_count=len(verified),all_source_pin_files=verified,all72_old_pins_unchanged_plus_one_new_entry=True,
    original_input_scope=input_scope,original_four_input_descriptors_and_saved97_verified_receipts_equal=True,
    first_parent_fixed_actual97_and_original13_closure=parent_closure,
    own_schema_future_parent_uses_new14_closure=current_closure,
    parent_damping_is_metadata_not_a_new_eta_lock=True,
    literal_parameters=parent['final']['parameters'],literal_parameter_binary64le_hex=bits,
    parent_J_merit_state_FD_not_used_as_fresh_values=True,
    full_source_inverse_recovers_frozen_ce93=True,
    top_level_function_class_comparisons=function_checks,
    entire_try_search_final_diagnostics_and_finally_body_byte_identical=True,
    exact_diagnostic=request['diagnostic'],parent_stop_reason=parent['search_stop_reason'],
    same_diagnostic_budgets_except_single_declared_damping=True,
    old_and_new_schemas_distinct=True,only_workflow_steps_changed=changed_steps,
    unchanged_science_argv_invocation_restore_and_readback_inline_blocks=True,
    shell_checks=shell_checks,inline_Python_checks=inline_checks,
    job_and_scientific_timeout_unchanged=True,
    old_complete_function_formulas_retained_not_an_unchanged_old_entry=True,
    original_input_payloads_downloaded_locally=False,numerical_source_imported=False,
    local_scientific_computation=False,workflow_commands_executed=False,
    repository_or_Git_modified=False,workflow_dispatched=False,
    no_new_scientific_gate_or_future_success_claim=True)
path=HERE/'request99-static-check.json'
path.write_text(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
print(json.dumps(dict(status=report['status'],source_count=len(verified),shell_count=len(shell_checks),
    inline_count=len(inline_checks),report=receipt(path)),indent=2))
