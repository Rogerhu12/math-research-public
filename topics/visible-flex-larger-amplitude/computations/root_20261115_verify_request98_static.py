#!/usr/bin/env python3
"""Root source/byte and literal-field verification only; no scientific execution."""
import difflib, hashlib, json, struct, subprocess
from pathlib import Path

REPO=Path('/workspace/scratch/visible-larger-recovered-20261114-1843/math-research-public')
TOP='topics/visible-flex-larger-amplitude'
NEW=Path('/tmp/visible-larger-thirty-one-source')
REQ=Path('/tmp/visible-larger-request98')
BASE=Path('/tmp/visible-larger-request94')
OLD=Path('/tmp/visible-larger-actual94-dispatch-sources')
SOURCE='b75f41fa32b8ead9bb5121b725a0afe1a2f5ae5c'
OUT=Path('/tmp/2026-11-15-request98-root-independent-static-readback.json')
report={'schema':'request98-root-independent-source-byte-readback-v1',
 'scientific_execution_performed':False,'source_dispatch_commit':SOURCE,
 'root_full_read_scope':['four complete source diffs','17099-byte interface',
 'complete workflow and request diffs','both complete source-only checkers'],
 'frozen_files':[],'actual_git_sources':[],'replayed_static_receipts':[],
 'literal_nodes_checked':0,'IEEE_binary64_words_checked':0}

def sha(b): return hashlib.sha256(b).hexdigest()
def git(ref,path): return subprocess.check_output(['git','show',ref+':'+path],cwd=REPO)
def same(a,b):
    report['literal_nodes_checked']+=1
    assert type(a) is type(b),(type(a),type(b))
    if isinstance(a,dict):
        assert a.keys()==b.keys()
        for k in a:same(a[k],b[k])
    elif isinstance(a,list):
        assert len(a)==len(b)
        for x,y in zip(a,b):same(x,y)
    elif isinstance(a,float):
        assert struct.pack('<d',a)==struct.pack('<d',b)
        report['IEEE_binary64_words_checked']+=1
    else:assert a==b,(a,b)

for d in (NEW,REQ):
    m=json.loads((d/'frozen-files.json').read_bytes())
    for row in m['files']:
        raw=(d/row['file']).read_bytes()
        assert len(raw)==row['bytes'] and sha(raw)==row['sha256'],row['file']
        report['frozen_files'].append({'directory':str(d),**row})

q=json.loads((REQ/'public-condensed-qp-request.json').read_bytes())
oldq=json.loads((BASE/'public-condensed-qp-request.json').read_bytes())
assert len(q['source_sha256'])==67 and len(oldq['source_sha256'])==63
for name,digest in q['source_sha256'].items():
    if (NEW/name).is_file():
        raw=(NEW/name).read_bytes(); origin='new independent source'
    else:
        raw=git('HEAD',TOP+'/computations/'+name);origin='current HEAD Git object'
        assert oldq['source_sha256'][name]==digest
    assert sha(raw)==digest,name
    report['actual_git_sources'].append({'file':name,'bytes':len(raw),'sha256':digest,'origin':origin})

for kind in ('domain_operator','condensed_warm','condensed_response','collocation_observer_warm'):
    oldname='geometry_20261114_twenty_eight_query_'+kind+'.py'
    newname='geometry_20261114_thirty_one_query_'+kind+'.py'
    raw=git(SOURCE,TOP+'/computations/'+oldname)
    assert raw==(OLD/oldname).read_bytes()
    diff=''.join(difflib.unified_diff(raw.decode().splitlines(True),(NEW/newname).read_text().splitlines(True),
      fromfile='actual94-frozen28/'+oldname,tofile='independent31/'+newname))
    assert diff==(NEW/(newname+'.diff')).read_text()
for name,path in [('visible-larger-public-condensed-qp.yml','.github/workflows/visible-larger-public-condensed-qp.yml'),
                  ('public-condensed-qp-request.json',TOP+'/computations/public-condensed-qp-request.json')]:
    raw=git('HEAD',path)
    assert raw==(BASE/name).read_bytes()==git(SOURCE,path)
    diff=''.join(difflib.unified_diff(raw.decode().splitlines(True),(REQ/name).read_text().splitlines(True),
      fromfile='actual94/'+name,tofile='request98/'+name))
    assert diff==(REQ/(name+'.diff')).read_text()
report['all_six_full_diffs_match_actual_Git_baselines']=True

modelpath=Path('/tmp/visible-larger-actual94-published/twenty-eight-condensed-warm/model-000.json')
raw=modelpath.read_bytes();assert sha(raw)==q['actual_parent_original_model']['sha256']
assert len(raw)==q['actual_parent_original_model']['bytes']
model=json.loads(raw);half,near,accepted=[model['trials'][i] for i in (1,2,3)]
same(q['actual_parent_accepted_original_merit'],{k:accepted[k] for k in q['actual_parent_accepted_original_merit']})
same(q['original_fixed_weight_merit_before'],model['fixed_weight_merit_before'])
point=near['domain']['read_only_midpoint_observer']['points'][0]
n=q['nearest_rejection'];h=q['separate_left_RMS_rejection']
same(n['original_bad_midpoint'],{k:point[k] for k in n['original_bad_midpoint']})
same(n['original_linear_beta_squared'],near['selected_linear_beta_squared'])
same(n['original_linear_reserve_slack'],near['all_selected_linear_reserve_slack'])
same(n['alpha'],near['alpha']);same(h['alpha'],half['alpha'])
same(h['original_RMS_query_checks'],half['complete_original_RMS_query_domain']['original_RMS_query_checks'])
for key in ('actual_fixed_weight_merit','actual_merit_reduction','actual_to_predicted_ratio'):same(h[key],half[key])
assert 'actual_fixed_weight_merit' not in near and 'complete_original_RMS_query_domain' not in near
for trial in (half,near):
    assert len(trial['actual_selected_original_angles'])==28
    for item in trial['actual_selected_original_angles']:
        v=item['original_beta_squared'];assert v['nonfinite_count']==v['negative_count']==v['zero_count']==0
report['actual94_original_saved_fields_and_IEEE_words_preserved']=True
for d,script,receipt in [(NEW,'check_thirty_one_sources.py','thirty-one-source-static-check.json'),
                         (REQ,'check_request98_static.py','request98-static-check.json')]:
    before=(d/receipt).read_bytes()
    p=subprocess.run(['python',str(d/script)],capture_output=True,text=True,cwd=REPO)
    assert p.returncode==0,(script,p.stdout,p.stderr)
    assert (d/receipt).read_bytes()==before
    report['replayed_static_receipts'].append({'file':receipt,'bytes':len(before),'sha256':sha(before),
      'entire_original_receipt_byte_identical':True})
report['source_pin_count']=67
report['passed']=True
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'file':str(OUT),'bytes':OUT.stat().st_size,'sha256':sha(OUT.read_bytes()),
 'source_pins':67,'literal_nodes':report['literal_nodes_checked'],'float_words':report['IEEE_binary64_words_checked'],
 'scientific_execution_performed':False,'passed':True}))
