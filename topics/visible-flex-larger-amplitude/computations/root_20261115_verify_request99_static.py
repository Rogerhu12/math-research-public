#!/usr/bin/env python3
"""Original-byte/AST/literal-field verification only; never execute science."""
from pathlib import Path
import difflib, hashlib, json, struct, subprocess

REPO=Path('/workspace/scratch/visible-larger-recovered-20261114-1843/math-research-public')
TOP='topics/visible-flex-larger-amplitude'
NEW=Path('/tmp/visible-larger-request99');BASE=Path('/tmp/visible-larger-request97')
ACTUAL=Path('/tmp/visible-larger-recovery-2207/actions-debug/visible-mainline-smallcoreresonance-43676647334-1')
SOURCE='15b2028e039d2b93ea01b3bf6ef8c1fed8db15ed'
ENTRY='geometry_20261115_small_core_inexact_p3_eta_0p01.py'
OLDENTRY='geometry_20261115_small_core_inexact_p3_restoration.py'
OUT=Path('/tmp/2026-11-15-request99-root-independent-static-readback.json')
report={'schema':'request99-root-independent-original-byte-static-v1','scientific_execution':False,
 'full_read_scope':['producer entire diff','workflow entire diff','request entire diff',
 '12990-byte complete interface','complete source checker and producer source-only builder'],
 'frozen_files':[],'source_payloads':[],'literal_nodes_checked':0,'IEEE_words_checked':0}
def sha(b):return hashlib.sha256(b).hexdigest()
def git(ref,path):return subprocess.check_output(['git','show',ref+':'+path],cwd=REPO)
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
        report['IEEE_words_checked']+=1
    else:assert a==b

manifest=json.loads((NEW/'frozen-files.json').read_bytes())
for row in manifest['files']:
    b=(NEW/row['file']).read_bytes();assert len(b)==row['bytes'] and sha(b)==row['sha256']
    report['frozen_files'].append(row)
request=json.loads((NEW/'public-small-core-resonance-request.json').read_bytes())
oldrequest=json.loads((BASE/'public-small-core-resonance-request.json').read_bytes())
for name,want in request['source_sha256'].items():
    if name==ENTRY:b=(NEW/name).read_bytes();scope='new distinct producer'
    else:
        b=git(SOURCE,TOP+'/computations/'+name)
        assert b==git('HEAD',TOP+'/computations/'+name)
        assert oldrequest['source_sha256'][name]==want;scope='actual97 and current HEAD Git payloads'
    assert sha(b)==want
    report['source_payloads'].append({'file':name,'bytes':len(b),'sha256':want,'scope':scope})
oldsource=git(SOURCE,TOP+'/computations/'+OLDENTRY)
assert sha(oldsource)=='ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e'
rows=[(oldsource,(NEW/ENTRY).read_bytes(),'frozen-ce93/'+OLDENTRY,'request99/'+ENTRY,'producer-from-ce93.diff')]
for name,path,diff in [('visible-larger-public-small-core-resonance.yml','.github/workflows/visible-larger-public-small-core-resonance.yml','workflow-from-actual97.diff'),
 ('public-small-core-resonance-request.json',TOP+'/computations/public-small-core-resonance-request.json','request-from-actual97.diff')]:
    b=git(SOURCE,path);assert b==(BASE/name).read_bytes()==git('HEAD',path)
    rows.append((b,(NEW/name).read_bytes(),'actual97/'+name,'request99/'+name,diff))
for old,new,oldlabel,newlabel,name in rows:
    d=''.join(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),fromfile=oldlabel,tofile=newlabel))
    assert d==(NEW/name).read_text(),name
report['three_full_diffs_match_actual_Git_bytes']=True
prior=request['prior_candidate']['original_status']
raw=(ACTUAL/'small-core-inexact-p3-restoration/inexact-p3-restoration-status.json').read_bytes()
assert len(raw)==prior['bytes'] and sha(raw)==prior['sha256']
assert raw==(NEW/'actual97-original/inexact-p3-restoration-status.json').read_bytes()==git('HEAD',prior['file'])
parent=json.loads(raw);literal=json.loads((NEW/'actual97-parent-literal-readout.json').read_bytes())
same(literal['copied_original_fields'],{k:parent[k] for k in literal['copied_original_fields']})
same(literal['original_final'],parent['final'])
same(literal['literal_final_parameters'],parent['final']['parameters'])
same(literal['original_parent_source_closure'],parent['consumed_source_sha256'])
last=parent['searches'][-1]
same(literal['last_direction_base_parameters'],last['parameters'])
same(literal['last_direction_model'],last['direction_model'])
motivation=request['saved97_motivation']
same(motivation['last_direction_base_parameters'],last['parameters'])
same(motivation['last_direction_base_residual'],last['residual'])
same(motivation['last_direction_model'],last['direction_model'])
same(motivation['final_accepted_parameters'],parent['final']['parameters'])
same(request['diagnostic']['parameters'],parent['final']['parameters'])
same(request['prior_candidate']['original_final_unit_defects'],parent['final']['unit_diagonal_defects'])
same(request['prior_candidate']['original_final_merit'],parent['final_original_three_equation_merit'])
report['actual97_status_current_public_payload_and_full_copy_byte_identical']=True
report['parent_last_direction_and_final_point_kept_distinct']=True
saved=(NEW/'request99-static-check.json').read_bytes()
p=subprocess.run(['python',str(NEW/'check_request99_static.py')],cwd=REPO,capture_output=True,text=True)
assert p.returncode==0,(p.stdout,p.stderr)
assert saved==(NEW/'request99-static-check.json').read_bytes()
report['entire_frozen_static_receipt_replayed_byte_identical']={'bytes':len(saved),'sha256':sha(saved)}
report['four_full_original_inputs_reuse_prior_paid_actual92_payload_checks']=True
report['four_input_original97_receipts_verified_by_source_checker']=True
report['source_pin_count']=73
report['passed']=True
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'file':str(OUT),'bytes':OUT.stat().st_size,'sha256':sha(OUT.read_bytes()),
 'source_pins':73,'literal_nodes':report['literal_nodes_checked'],'float_words':report['IEEE_words_checked'],'passed':True}))
