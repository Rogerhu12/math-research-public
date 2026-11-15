#!/usr/bin/env python3
"""Only source/configuration and original-byte checks; no scientific import."""
from pathlib import Path
import ast
import gzip
import hashlib
import json
import re
import shlex
import subprocess
import yaml

OUT=Path('/tmp/visible-larger-request98')
BASE=Path('/tmp/visible-larger-request94')
NEW=Path('/tmp/visible-larger-thirty-one-source')
DISPATCH=Path('/tmp/visible-larger-actual94-dispatch-sources')
TRANSPORT=Path('/tmp/visible-larger-request96/root-verified-sources')
COMP=Path('/workspace/scratch/visible-larger-recovered-20261114-1843/math-research-public/topics/visible-flex-larger-amplitude/computations')


def sha(raw): return hashlib.sha256(raw).hexdigest()
def receipt(path):
    raw=path.read_bytes()
    return dict(file=str(path),bytes=len(raw),sha256=sha(raw))
def literal(tree,key):
    n=next(n for n in tree.body if isinstance(n,ast.Assign) and any(
        isinstance(t,ast.Name) and t.id==key for t in n.targets))
    return ast.literal_eval(n.value)


q=json.loads((OUT/'public-condensed-qp-request.json').read_bytes())
oldq=json.loads((BASE/'public-condensed-qp-request.json').read_bytes())
w=yaml.load((OUT/'visible-larger-public-condensed-qp.yml').read_text(),Loader=yaml.BaseLoader)
oldw=yaml.load((BASE/'visible-larger-public-condensed-qp.yml').read_text(),Loader=yaml.BaseLoader)
assert q['request']==98 and q['lanes']==['condensedqp']
assert q['declared_budgets']==oldq['declared_budgets']
assert q['source_sha256'].items()>=oldq['source_sha256'].items()
assert len(q['source_sha256'])==67
assert w['on']==oldw['on']
assert w['on']['push']['paths']==['topics/visible-flex-larger-amplitude/computations/public-condensed-qp-request.json']
assert w['jobs']['followup']['concurrency']==oldw['jobs']['followup']['concurrency']
assert w['jobs']['followup']['strategy']==oldw['jobs']['followup']['strategy']
assert w['jobs']['followup']['timeout-minutes']==oldw['jobs']['followup']['timeout-minutes']=='80'
assert w['jobs']['followup']['env']==oldw['jobs']['followup']['env']
assert w['permissions']==oldw['permissions']
report=dict(schema='request98-independent31-source-only-static-binding-v1',
    scientific_calculation_performed_locally=False,scientific_modules_imported=False,
    git_or_dispatch_performed=False,baseline_request94_files=[receipt(BASE/'visible-larger-public-condensed-qp.yml'),
        receipt(BASE/'public-condensed-qp-request.json')],source_checks=[],shell_checks=[],inline_python_AST_checks=[])
for filename,digest in q['source_sha256'].items():
    path=next(base/filename for base in (NEW,DISPATCH,TRANSPORT,COMP) if (base/filename).is_file())
    raw=path.read_bytes();assert sha(raw)==digest,(filename,sha(raw),digest)
    tree=ast.parse(raw);compile(tree,str(path),'exec')
    report['source_checks'].append(dict(file=filename,local_path=str(path),bytes=len(raw),sha256=digest))
for jobname,job in w['jobs'].items():
    for index,step in enumerate(job['steps']):
        if 'uses' in step:
            assert re.fullmatch(r'[^@]+@[0-9a-f]{40}',step['uses'])
        if 'run' not in step: continue
        raw=step['run']
        shell=re.sub(r'\$\{\{.*?\}\}','EXPRESSION',raw)
        process=subprocess.run(['bash','-n'],input=shell,text=True,capture_output=True)
        assert process.returncode==0,(jobname,index,process.stderr)
        report['shell_checks'].append(dict(job=jobname,step=index,name=step.get('name')))
        lines=raw.splitlines();i=0
        while i<len(lines):
            match=re.search(r"<<'([A-Z][A-Z0-9_]*)'",lines[i])
            if not match:i+=1;continue
            marker=match.group(1);j=i+1
            while j<len(lines) and lines[j]!=marker:j+=1
            assert j<len(lines),(jobname,index,marker)
            body='\n'.join(lines[i+1:j])+'\n';tree=ast.parse(body)
            report['inline_python_AST_checks'].append(dict(job=jobname,step=index,marker=marker))
            if marker=='PYPINS':
                assert set(literal(tree,'required'))==set(q['source_sha256'])
            i=j+1

oldsteps=oldw['jobs']['followup']['steps'];steps=w['jobs']['followup']['steps']
assert len(steps)==len(oldsteps)
for i in (1,2,3,6,7,11,12):assert steps[i]==oldsteps[i],(i,steps[i].get('name'))
assert w['jobs']['select']==oldw['jobs']['select']


def first_command(step):
    return shlex.split(step['run'].split("python - <<'PYWARM'")[0].replace('\\\n',' '))


before,after=first_command(oldsteps[9]),first_command(steps[9])
assert before[:2]==after[:2]==['python','-u']
assert before[2].endswith('twenty_eight_query_collocation_observer_warm.py')
assert after[2].endswith('thirty_one_query_collocation_observer_warm.py')
assert len(before)==len(after)
allowed={'--resume','--expected-resume-sha','--parent-status','--expected-parent-status-sha','--out'}
options={}
for i in range(3,len(before),2):
    opt=before[i];assert after[i]==opt
    if i+1==len(before):assert opt=='--condensed-store-root';break
    if opt not in allowed:assert after[i+1]==before[i+1],opt
    options[opt]=after[i+1]
assert options['--expected-resume-sha']==q['actual_parent_warm_sha256']
assert options['--expected-parent-status-sha']==q['actual_parent_status_sha256']
assert options['--out']=='$VISIBLE_OUT/thirty-one-condensed-warm'
expected=dict(iterations='1',damping='270',lsmr_iterations='200',projection_sweeps='200',
    line_search_steps='17',budget_seconds='1200',condensed_budget_seconds='600',
    condensed_trial_reserve_seconds='90',condensed_recovery_reserve_seconds='30',
    condensed_max_working='512',condensed_dual_sweeps='200',angles='4096',jac_workers='2')
for key,value in expected.items():assert options['--'+key.replace('_','-')]==value
assert steps[9]['timeout-minutes']==oldsteps[9]['timeout-minutes']=='35'
assert steps[10]['timeout-minutes']==oldsteps[10]['timeout-minutes']=='25'
assert steps[10]['run'].replace('thirty_one','twenty_eight')==oldsteps[10]['run']
for i in (9,10):
    assert 'GH_TOKEN' not in steps[i].get('env',{}) and 'GITHUB_TOKEN' not in steps[i].get('env',{})

parent_step=steps[8]['run'];old_parent_step=oldsteps[8]['run']
for old,new in [
    (str(q['actual_parent_run']),str(oldq['actual_parent_run'])),
    (q['actual_parent_source_commit'],oldq['actual_parent_source_commit']),
    (q['actual_parent_warm_sha256'],oldq['actual_parent_warm_sha256']),
    (q['actual_parent_status_sha256'],oldq['actual_parent_status_sha256']),
    (q['actual_parent_compressed_status_sha256'],oldq['actual_parent_compressed_status_sha256']),
    (str(q['actual_parent_warm_bytes']),str(oldq['actual_parent_warm_bytes'])),
    (str(q['actual_parent_original_status_bytes']),str(oldq['actual_parent_original_status_bytes'])),
    (str(q['actual_parent_compressed_status_bytes']),str(oldq['actual_parent_compressed_status_bytes'])),
    ('twenty-eight-condensed-warm','twenty-six-condensed-warm'),
    ('exact-constraint-twenty-eight-query-condensed-complete-H-warm-v1','exact-constraint-twenty-six-query-condensed-complete-H-warm-v1'),
    ('actual94','actual89'),('PYPARENT94','PYPARENT89'),('VISIBLE_PARENT94','VISIBLE_PARENT89'),('parent94','parent89')]:
    parent_step=parent_step.replace(old,new)
assert parent_step==old_parent_step

parent=Path('/tmp/visible-larger-actual94-published')
warm=parent/'twenty-eight-condensed-warm/warm-001.json.gz'
status=parent/'twenty-eight-condensed-warm/driver-status.json.gz'
raw=gzip.decompress(status.read_bytes());obj=json.loads(raw)
assert sha(warm.read_bytes())==q['actual_parent_warm_sha256']
assert sha(raw)==q['actual_parent_status_sha256']
assert sha(status.read_bytes())==q['actual_parent_compressed_status_sha256']
assert len(raw)==q['actual_parent_original_status_bytes']
assert obj['schema']==q['actual_parent_schema'] and obj['latest_warm_sha256']==q['actual_parent_warm_sha256']
assert q['nearest_rejection']['original_bad_midpoint']['interval']==486
assert q['nearest_rejection']['original_trial_index']==2 and q['nearest_rejection']['alpha']==.25
assert q['nearest_rejection']['actual_merit_evaluated'] is False
assert q['nearest_rejection']['full_original_RMS_scan_executed'] is False
assert q['separate_left_RMS_rejection']['original_trial_index']==1 and q['separate_left_RMS_rejection']['alpha']==.5
assert [x['interval'] for x in q['separate_left_RMS_rejection']['original_RMS_query_checks'][0]['first_invalid_points']]==[464,486]
assert q['separate_left_RMS_rejection']['original_RMS_query_domain_failures']==2
assert q['current_left_RMS_intervals']==sorted(oldq['current_left_RMS_intervals']+[464,486])
assert q['current_original_midpoint_intervals']==sorted(oldq['current_original_midpoint_intervals']+[486])
assert [x for x in q['query_specs'] if x in oldq['query_specs']]==oldq['query_specs']
assert q['expected_complete_B_local_dimension']==8453
assert q['expected_baseline_C_dimension_from_frozen_support_formula']==4059
assert q['selected_angle_row_count']==63488 and q['selected_query_count']==31
assert q['explicit_zero_B_layout_nodes']==q['explicit_zero_B_layout_columns']==[]
assert q['actual_query_endpoint_capture_count']==25 and q['unique_capture_cell_count']==20
assert q['added_original_capture_endpoints']==[464]
assert q['added_original_capture_intervals']==[464,486]
assert q['original_global_physical_column_ranges_added']['node464']==[156494,156832]
sourcecheck=json.loads((NEW/'thirty-one-source-static-check.json').read_bytes())
assert q['query_specs']==[{k:x[k] for k in ('kind','interval','fraction')}
    for x in sourcecheck['query_specs_with_original_index_and_row_ranges']]
assert q['actual_query_endpoint_nodes']==sourcecheck['query_endpoint_nodes']
assert q['complete_B_outside_C_nodes']==sourcecheck['complete_B_outside_C_nodes']
report.update(source_pin_count=len(q['source_sha256']),all63_prior_pins_exactly_preserved=True,
    only_four_new_source_pins=True,unique_existing_trigger_and_concurrency_preserved=True,
    runtime_and_install_steps_unchanged=True,public78_restore_unchanged=True,
    complete_prepared112_and_zero_anchor_inputs_unchanged=True,
    warm_cli_numeric_arguments_and_original_budgets_unchanged=True,
    warm_cli_numeric_arguments=options,original_FD_run_body_reverse_identity=True,
    parent_restore_body_reverse_identity_after_explicit_source_and_original_byte_pins=True,
    science_steps_have_no_token=True,actual94_parent_pair_and_gzip_SHA_verified=True,
    parent_status_bytes_preserved_without_reserialization=True,
    source_static_check=receipt(NEW/'thirty-one-source-static-check.json'),
    output_files=[receipt(OUT/'visible-larger-public-condensed-qp.yml'),receipt(OUT/'public-condensed-qp-request.json')])
path=OUT/'request98-static-check.json'
path.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(file=str(path),bytes=path.stat().st_size,sha256=sha(path.read_bytes()),
    source_pins=len(q['source_sha256']),shell_blocks=len(report['shell_checks']),
    inline_python_blocks=len(report['inline_python_AST_checks']),scientific_execution=False),indent=2))
