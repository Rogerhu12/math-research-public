#!/usr/bin/env python3
"""Bind actual91's complete original83/73 raw state, and screen one exact word.

This source executes arithmetic only inside the public repository Actions.
The original complete raw base, H/target/scales/far and three residual arrays
are retained. The old base flow-output was not exported by83 and is neither
reconstructed nor substituted from the rejected trial. A one-coordinate
proposal is ranked on all129248 original rows; this is not native acceptance.
"""
from __future__ import annotations
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import struct
from fractions import Fraction
from decimal import Decimal, localcontext

REPOSITORY='Rogerhu12/math-research-public'
PIN91=dict(run_id=43672150224,artifact_id=14145200674,
 artifact_name='visible-mainline-modelresponse-43672150224-1',expected_size=10267458,
 expected_sha256='78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6')
SOURCE91='b78f0dd1471a118d2ed21467602509d188c2ab67'
SOURCE91_SHA='17659d25b5f24d21843c188f845247ce3a132a7462e28d7b4fbcdf59db17bc8c'
RESULT91_SHA='0b7200064336361ecb36b0627495fca298b7af758ed37d34d6ae6b1a1898db04'
BIND91_SHA='0119e12bfc7f98732189b76b3fdfa23ae05229937a8ea998c9aa38890ff11d0a'
EXACT83_SHA='60feb7732547dcd04ef2469c5a1adf7cef5fd93f714107ac41cdb8f71282ff61'
PROBE83_SHA='7be2d7f0a98445e5efcd0ba146b7f8257483fa7593a54a6b389e8279f7fcf6ea'
STATE_SHA='f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6'
H_SHA='c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f'
TARGET_SHA='e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d'
SIGMA_SHA='ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc'
FAR_SHA='395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54'
J_CHUNK_SHA='fd117e2d3cfdd26ddfa584e5c75e521209f12ca16f098596ec61cab3e47f8677'
OLD_MATRIX='6ea4b16fa7e41ae1099a3e792b67c19cf6c9d4ae41f5c3209fa84d43c5f8fbd8'
NODE,COLUMN=11,75
BASE_WORD='6e1cafdb47e9c93c'
INPUT_MAP={'base-states':'base-states','stage-residuals':'saved-stage-residuals',
 'cut-residual':'saved-cut-residual','end-residual':'saved-end-residual',
 'original-scales':'original-scales','original-far-graph':'original-far-graph',
 'physical-height':'physical-height','cut-target':'cut-target'}
SHAPES={'base-states':[577,224],'stage-residuals':[576,224],
 'cut-residual':[1,112],'end-residual':[1,112],'original-scales':[1,577],
 'original-far-graph':[1,112],'physical-height':[1,112],'cut-target':[1,112]}

def require_actions():
 if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!=REPOSITORY.lower():
  raise RuntimeError('All candidate arithmetic and native execution belong only to this public repository Actions')
def require(ok,label):
 if not ok:raise ValueError(label)
def digest(path):
 h=hashlib.sha256();size=0
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b);size+=len(b)
 return dict(bytes=size,sha256=h.hexdigest())
def sha(path):return digest(path)['sha256']
def read(path):
 b=Path(path).read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)
def descriptor(path,base=None):
 p=Path(path);return dict(file=p.relative_to(base).as_posix() if base else p.name,**digest(p))
def write(path,value):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
 b=(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
 if p.suffix=='.gz':b=gzip.compress(b,mtime=0)
 with p.open('xb') as f:f.write(b)
 return descriptor(p)
def safe(base,name):
 p=PurePosixPath(name);require(isinstance(name,str) and not p.is_absolute() and '..' not in p.parts and '\\' not in name,'Safe relative original path')
 q=Path(base).joinpath(*p.parts);require(q.is_file() and not q.is_symlink(),'Original regular file '+name);return q
def verified(base,row):
 p=safe(base,row['file']);require(digest(p)==dict(bytes=row['bytes'],sha256=row['sha256']),'Original complete file '+row['file']);return p

def word(raw,i):return int.from_bytes(raw[8*i:8*i+8],'little')
def finite_word(w):return ((w>>52)&2047)!=2047
def frac_word(w):
 require(finite_word(w),'Finite binary64 mathematical input')
 e=(w>>52)&2047;m=w&((1<<52)-1)
 if e:m|=1<<52;p=e-1075
 else:p=-1074
 if w>>63:m=-m
 return Fraction(m<<p,1) if p>=0 else Fraction(m,1<<(-p))
def rec(value):
 value=Fraction(value)
 with localcontext() as c:
  c.prec=64;c.Emax=999999;c.Emin=-999999
  display='0' if value==0 else format(Decimal(value.numerator)/Decimal(value.denominator),'.63E')
 return dict(numerator=str(value.numerator),denominator=str(value.denominator),
  decimal_display_64_significant_digits=display,display_is_not_interval_enclosure=True)
def wrec(w):
 require(finite_word(w),'Finite candidate word')
 return dict(float64le_hex=w.to_bytes(8,'little').hex(),value=struct.unpack('<d',w.to_bytes(8,'little'))[0],
  classification='negative-zero' if w==(1<<63) else 'finite')

def make_word_delta(base_raw):
 """Preserve signed zero outside the one intended coordinate under v+alpha*d."""
 require_actions();require(len(base_raw)==577*224*8 and hashlib.sha256(base_raw).hexdigest()==STATE_SHA,'Exact complete old base only')
 index=NODE*224+COLUMN;old=word(base_raw,index)
 require(old.to_bytes(8,'little').hex()==BASE_WORD and old>0 and old>>63==0,'Fixed actual91 positive Q76 word')
 desired=old-1;h=frac_word(desired)-frac_word(old)
 # Adjacent finite same-sign operands satisfy Sterbenz; still verify the actual
 # encoded difference and actual unit-step expression here in Actions.
 d=float(h);require(Fraction.from_float(d)==h,'Neighbor difference exactly representable')
 require(struct.pack('<d',struct.unpack('<d',old.to_bytes(8,'little'))[0]+d)==desired.to_bytes(8,'little'),'Original unit trial reaches the neighbor word')
 out=bytearray(len(base_raw))
 for j in range(577*224):
  if word(base_raw,j)==1<<63:out[8*j:8*j+8]=(1<<63).to_bytes(8,'little')
 out[8*index:8*index+8]=struct.pack('<d',d)
 proposed=bytearray(base_raw);proposed[8*index:8*index+8]=desired.to_bytes(8,'little')
 return bytes(out),bytes(proposed),dict(node=NODE,column=COLUMN,component='Q',mode=76,
  base=wrec(old),candidate=wrec(desired),original_direction_sign='negative',
  exact_candidate_increment=rec(h),direction_word=wrec(word(out,index)),
  nonzero_numeric_direction_coordinates=1,preserved_negative_zero_directions=True,
  original_rejected_trial_not_used_as_initial_guess=True),h

def screen_complete_model(raw,stage10_J_raw,proposal_h,output,label):
 """All cut/stage/far rows; exactly225 changed entries for this support."""
 require_actions();require(len(stage10_J_raw)==224*224*8,'Complete stage10 block required')
 require(set(raw)==set(SHAPES),'All eight complete original model arrays')
 require(all(len(raw[n])==8*SHAPES[n][0]*SHAPES[n][1] for n in SHAPES),'All complete model shapes')
 sigma=[frac_word(word(raw['original-scales'],i)) for i in range(577)]
 require(all(s>0 for s in sigma),'Original positive complete residual scales')
 base_max=Fraction(0);candidate_max=Fraction(0);base_where=None;candidate_where=None;changes=[]
 target=Path(output);target.mkdir(parents=True,exist_ok=False)
 (target/'large-arrays').mkdir()
 ledger=target/'large-arrays/complete129248-original-model-rows.jsonl.gz';visited=0
 with gzip.open(ledger,'wb') as stream:
  def visit(kind,n,j,g,rv,delta,scale):
   nonlocal base_max,candidate_max,base_where,candidate_where,visited
   new=rv+delta;b=abs(rv)/scale;c=abs(new)/scale
   where=dict(kind=kind,node=n,row=j,global_equation_row=g)
   if base_where is None or b>base_max:base_max=b;base_where=where
   if candidate_where is None or c>candidate_max:candidate_max=c;candidate_where=where
   entry=dict(**where,base_unscaled=rec(rv),candidate_unscaled=rec(new),changed_exact_value=delta!=0)
   stream.write((json.dumps(entry,separators=(',',':'),allow_nan=False)+'\n').encode());visited+=1
   if delta!=0:changes.append(dict(**where,linear_change=rec(delta),linear_change_over_original_sigma=rec(delta/scale)))
  for j in range(112):visit('cut',0,j,j,frac_word(word(raw['cut-residual'],j)),Fraction(0),sigma[0])
  for n in range(576):
   for j in range(224):
    dr=Fraction(0)
    if n==10:dr=frac_word(word(stage10_J_raw,j*224+COLUMN))*proposal_h
    if n==11 and j==COLUMN:dr-=proposal_h
    visit('stage',n,j,112+n*224+j,frac_word(word(raw['stage-residuals'],n*224+j)),dr,sigma[n])
  for j in range(112):visit('far',576,j,112+576*224+j,frac_word(word(raw['end-residual'],j)),Fraction(0),sigma[576])
 require(visited==129248,'Complete original row count')
 record=dict(schema='one-representable-input-word-complete129248-model-screen-v1',model_label=label,
  original_row_count=visited,all_cut_and_far_and_other_stage_rows_retained=True,
  no_other_direction_coordinate_removed_from_an_existing_QR_direction=True,
  direction_is_new_single_coordinate_proposal_not_the_old_QR_direction=True,
  base_exact_norm=rec(base_max),candidate_exact_norm=rec(candidate_max),
  base_max_coordinate=base_where,candidate_max_coordinate=candidate_where,
  predicted_strict_decrease=candidate_max<base_max,affected_support_stage_rows=[10,11],
  affected_support_count_upper_bound=225,exact_nonzero_row_change_count=len(changes),
  changed_original_rows=changes,complete_row_ledger=descriptor(ledger,target),
  mathematical_inputs={k:dict(bytes=len(v),sha256=hashlib.sha256(v).hexdigest()) for k,v in raw.items()},
  full_stage10_J_sha256=hashlib.sha256(stage10_J_raw).hexdigest(),
  only_candidate_selection=True,native_accepted=False,changed_native_tolerance=False,
  no_actual_noJ_RHS_J_ODE_or_QR_calls=True)
 write(target/'result.json.gz',record)
 return record

def bind_parent91(directory,output):
 require_actions();directory=Path(directory).resolve();output=Path(output).resolve()
 require(not output.exists(),'Independent fresh parent binding directory');output.mkdir(parents=True)
 transport=read(directory/'_pinned_public_artifact_receipt.json')
 require(transport['repository']==REPOSITORY and transport['success'] is True and transport['pinned_input']==PIN91,'Actual91 transport tuple')
 require(transport['download']['actual_size']==PIN91['expected_size'] and transport['download']['actual_sha256']==PIN91['expected_sha256'] and transport['zip_verified_before_extraction'] is True,'Complete actual91 ZIP verified')
 require(transport['public_artifact_metadata']['workflow_run']['head_sha']==SOURCE91,'Actual91 source commit')
 sci=directory/'actual83-four-row-attribution';summary=read(sci/'summary.json')
 result_path=verified(sci,summary['full_result']);require(sha(result_path)==RESULT91_SHA,'Actual91 result bytes')
 result=read(result_path);require(result['completed'] is True and result['source_sha256']==SOURCE91_SHA and result['errors']==[],'Completed original four-row diagnostic')
 binding_path=verified(sci,result['input_binding']);require(sha(binding_path)==BIND91_SHA,'Actual91 input binding bytes')
 binding=read(binding_path);require(binding['original_matrix_binding']['new_matrix_identity_sha256']==OLD_MATRIX,'Original full matrix identity')
 old=sci/'large-arrays/original-inputs';probe=read(old/'actual83-realized-trial/result.json');pbind=read(old/'actual83-realized-trial/input-binding.json.gz');manifest=read(old/'actual83-realized-trial/array-manifest.json')
 require(sha(old/'actual83-realized-trial/result.json')==PROBE83_SHA and sha(old/'actual83-exact/large-arrays/result.json.gz')==EXACT83_SHA,'Actual83 original report bytes')
 exact=read(old/'actual83-exact/large-arrays/result.json.gz');context=pbind['original_context']
 require(exact['original_scope']['original_native_accepted'] is False and exact['original_nonlinear_iteration']==2,'Actual73 failed base, not a solved anchor')
 require(pbind['current_state_sha256']==STATE_SHA and context['nonlinear_iteration']==2 and context['snapshot_sequence']==2 and context['native_call']==1,'Literal original73 iteration2 raw point')
 require(context['numerical_configuration']['maxIterations']==32 and context['numerical_configuration']['solveTolerance']==2e-9,'Original32/tolerance retained')
 require(context['rawNode']==[0,72,144,216,288,360,432,504,576],'Original nine physical boundaries')
 require(manifest==binding['original_probe_array_manifest'],'Original complete fifteen-array manifest')
 entries={x['name']:x for x in manifest['arrays']};raw={};arrays={}
 # Preserve every supplied original91 file, not merely the selected coordinates.
 preserve=output/'large-arrays/original91';preserve.mkdir(parents=True)
 originals=[]
 for p in sorted(directory.rglob('*')):
  if not p.is_file():continue
  require(not p.is_symlink(),'Original artifact contains no symlink')
  rel=p.relative_to(directory);q=preserve/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
  require(digest(q)==digest(p),'Preserved whole original91 file '+str(rel));originals.append(descriptor(q,output))
 for name,original_name in INPUT_MAP.items():
  d=entries[original_name];p=verified(old/'actual83-realized-trial',d);data=p.read_bytes()
  require(d['dtype']=='<f8' and d['order']=='C' and d['shape']==SHAPES[name],'Exact original mathematical shape '+name)
  require(hashlib.sha256(data).hexdigest()==context['raw_array_sha256'][name],'Original current context raw identity '+name)
  raw[name]=data;q=output/'large-arrays/parent-inputs'/ (name+'.f64le');q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(data)
  arrays[name]=dict(**descriptor(q,output),dtype='<f8',order='C',shape=SHAPES[name],original_probe_array=d,original_snapshot_name=name)
 for name,expected in [('base-states',STATE_SHA),('physical-height',H_SHA),('cut-target',TARGET_SHA),('original-scales',SIGMA_SHA),('original-far-graph',FAR_SHA)]:require(hashlib.sha256(raw[name]).hexdigest()==expected,'Pinned actual full '+name)
 jpath=old/'original73-J-chunk/native-noj-primal-current576-damped/iteration-002/snapshot/large-arrays/stage-jacobians-0002.f64le'
 require(digest(jpath)==dict(bytes=1605632,sha256=J_CHUNK_SHA),'Complete original stage8–11 J chunk')
 jraw=jpath.read_bytes();stage10=jraw[2*224*224*8:3*224*224*8]
 delta,trial,word_proposal,h=make_word_delta(raw['base-states'])
 for name,data in [('single-word-delta',delta),('single-word-unit-trial-state',trial)]:
  p=output/'large-arrays'/ (name+'.f64le');p.write_bytes(data)
  word_proposal[name.replace('-','_')]=dict(**descriptor(p,output),dtype='<f8',order='C',shape=[577,224])
 screening=screen_complete_model(raw,stage10,h,output/'old-complete-model','actual73-original-saved-model-via-actual91')
 parent=dict(schema='actual73-failed-current-base-via-complete-actual91-v1',source_public_run=43657001633,
  source_commit='9515d5aaf7c68f8efd366438d6bd81ce73c3486f',source_native_call=1,
  source_nonlinear_iteration=2,source_snapshot_sequence=2,state_raw_sha256=STATE_SHA,
  initial_guess_only=True,native_accepted=False,imported_worker_predictor=False,
  actual91_pin=PIN91,actual91_source_commit=SOURCE91,actual91_result=descriptor(result_path),
  actual91_binding=descriptor(binding_path),original_probe_result=descriptor(old/'actual83-realized-trial/result.json'),
  original_probe_input_binding=descriptor(old/'actual83-realized-trial/input-binding.json.gz'),
  original_exact_result=descriptor(old/'actual83-exact/large-arrays/result.json.gz'),
  original_native_outcome_receipt_only=exact['original_outcome'],original_native_scope=exact['original_scope'],
  original_snapshot_result_receipt_only=pbind['snapshot_result'],
  complete_parent_eight_array_sha256={k:v['sha256'] for k,v in arrays.items()},
  original_base_stage_out_not_exported_or_reconstructed=True)
 payload=dict(schema='native-word-first-parent91-complete-binding-v1',parent_failed73=parent,
  original_context=context,numerical_configuration=context['numerical_configuration'],
  original_numerical_parameters=context['parameters'],original_sources=context['original_sources'],
  original_arrays=arrays,word_proposal=word_proposal,old_complete_model_screen=screening,
  original_complete_source_artifact_preserved=originals,
  all_original91_input_files_preserved=True,old_trial_not_used_as_initial_guess=True,
  no_cached_native_response_or_predictor=True,original_scale_target_H_far_unmodified=True)
 write(output/'input-binding.json.gz',payload)
 return payload
