#!/usr/bin/env python3
"""Read original JSON/bytes only. No scientific module, rational arithmetic or action."""
from pathlib import Path
import json,gzip,hashlib,struct,collections
BASE=Path('/tmp/visible-larger-recovery-2207/actions-debug/visible-mainline-modelresponse-43672150224-1')
SCI=BASE/'actual83-four-row-attribution'
OUT=Path('/tmp/actual91-four-row-readback')
COMP=Path('/workspace/scratch/visible-larger-recovered-20261114-1843/math-research-public/topics/visible-flex-larger-amplitude/computations')
SCHEMA='actual91-original-JSON-raw-byte-and-IEEE-word-identity-audit-v1'
checks=[];files=[];decoded=[];source_checks=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def rawfile(p):return p.read_bytes()
def load(p):
 b=p.read_bytes(); d=gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b
 return json.loads(d)
def check(name,condition,details=None):
 rec={'check':name,'passed':bool(condition)}
 if details is not None:rec['details']=details
 checks.append(rec)
 if not condition:raise AssertionError(name)
def identity(p,relative=None):
 b=p.read_bytes();return {'file':relative or p.name,'bytes':len(b),'sha256':sha(b)}
def descriptor(root,d,label):
 p=root/d['file']; check(label+'/safe-path',not Path(d['file']).is_absolute() and '..' not in Path(d['file']).parts and not p.is_symlink())
 x=identity(p,d['file']);check(label+'/bytes',x['bytes']==d['bytes']);check(label+'/SHA256',x['sha256']==d['sha256']);return p
for p in sorted(BASE.rglob('*')):
 if p.is_file():
  check('regular-file:'+p.relative_to(BASE).as_posix(),not p.is_symlink())
  item=identity(p,p.relative_to(BASE).as_posix());files.append(item)
  if p.suffix=='.gz':
   d=gzip.decompress(p.read_bytes());decoded.append({'file':item['file'],'decoded_bytes':len(d),'decoded_sha256':sha(d),'gzip_CRC_read_succeeded':True})
check('root-download-complete-ZIP-marker', (BASE/'.download-complete').read_text().strip()=='78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6')
summary=load(SCI/'summary.json')
result=load(descriptor(SCI,summary['full_result'],'summary/full-result'))
check('completed-and-no-error',result['completed'] is True and result['errors']==[])
check('four-row-complete-counters',[result[k] for k in ['complete_original_row_count','complete_incoming_contribution_count','complete_outgoing_contribution_count','complete_original_four_node_coordinate_count']]==[4,896,4,896])
check('no-new-RHS-J-ODE-QR-solve-trial',all(result[k]==0 for k in ['new_RHS_calls','new_J_calls','new_ODE_steps','new_QR_calls','new_solve_calls','new_trial_calls']))
check('reported-exact-arithmetic-vs-local-read-only',result['scientific_arithmetic_performed'] is True and result['byte_only'] is False and result['original_full_J_payload_reloaded'] is False)

def display_view(x):
 if isinstance(x,dict):
  if {'numerator','denominator','decimal_display_64_significant_digits'} <= set(x):
   return {'decimal_display_64_significant_digits':x['decimal_display_64_significant_digits'],'exact_numerator_and_denominator_in_full_result':True,'display_is_not_an_interval_enclosure':True}
  return {k:display_view(v) for k,v in x.items()}
 if isinstance(x,list):return [display_view(v) for v in x]
 return x
for k,v in summary.items():
 if k in result:check('summary-exact-field-projection/'+k,v==display_view(result[k]))
bind=load(descriptor(SCI,result['input_binding'],'result/input-binding'))
check('binding-vs-result-preserved-inputs',bind['preserved_original_inputs']==result['preserved_original_inputs'])
check('binding-vs-result-selected-ledgers',bind['selected_node_ledger']==result['selected_original_increment_records'] and bind['selected_row_ledger']==result['selected_original_row_records'])
for i,d in enumerate(result['preserved_original_inputs']):descriptor(SCI,d,'preserved-original/'+str(i))
for i,t in enumerate(result['transport']):
 pin=t['actual_pin'];check('transport/'+str(i)+'/zip',t['download']['actual_size']==pin['expected_size'] and t['download']['actual_sha256']==pin['expected_sha256'])
 check('transport/'+str(i)+'/source',t['metadata']['workflow_run']['head_sha']==t['source_commit'])
 rawt=load(SCI/('large-arrays/original-inputs/'+t['kind']+'/_pinned_public_artifact_receipt.json'))
 check('transport/'+str(i)+'/receipt',rawt['success'] is True and rawt['zip_verified_before_extraction'] is True and rawt['pinned_input']==pin and rawt['download']==t['download'])
oldroot=SCI/'large-arrays/original-inputs'
oldfull=load(oldroot/'actual83-exact/large-arrays/result.json.gz')
oldbind=load(oldroot/'actual83-exact/large-arrays/input-binding.json.gz')
probe=load(oldroot/'actual83-realized-trial/result.json')
probebind=load(oldroot/'actual83-realized-trial/input-binding.json.gz')
manifest=load(oldroot/'actual83-realized-trial/array-manifest.json')
check('original-full-matrix-binding',bind['original_matrix_binding']==oldbind['original_current_matrix_binding'])
check('original-complete-J-descriptor',bind['original_complete_J_descriptor']==probebind['original_J_descriptor_only'])
check('original-probe-manifest-deep-identity',manifest==bind['original_probe_array_manifest']==oldbind['probe_array_manifest'])
check('original-probe-binding-deep-identity',probebind==oldbind['probe_input_binding'])
check('original-probe-summary-deep-identity',load(oldroot/'actual83-realized-trial/summary.json')==oldfull['probe_original_summary'])
check('original-exact-result-pinned',sha((oldroot/'actual83-exact/large-arrays/result.json.gz').read_bytes())=='60feb7732547dcd04ef2469c5a1adf7cef5fd93f714107ac41cdb8f71282ff61')
check('original-probe-result-pinned',sha((oldroot/'actual83-realized-trial/result.json').read_bytes())=='7be2d7f0a98445e5efcd0ba146b7f8257483fa7593a54a6b389e8279f7fcf6ea')
raw={};array_descriptors=[]
for d in manifest['arrays']:
 p=descriptor(oldroot/'actual83-realized-trial',d,'original-raw/'+d['name']);raw[d['name']]=p.read_bytes()
 count=1
 for dimension in d['shape']:count*=dimension
 check('original-raw/'+d['name']+'/shape-dtype-size',d['dtype']=='<f8' and d['order']=='C' and count*8==len(raw[d['name']]))
 array_descriptors.append(d)
check('fifteen-complete-arrays',len(raw)==15)
chunk_rel='native-noj-primal-current576-damped/iteration-002/snapshot/large-arrays/stage-jacobians-0002.f64le'
jraw=(oldroot/'original73-J-chunk'/chunk_rel).read_bytes()
check('full-original-J-chunk',len(jraw)==1605632 and sha(jraw)=='fd117e2d3cfdd26ddfa584e5c75e521209f12ca16f098596ec61cab3e47f8677')
check('pre-arithmetic-J-copy-identical',jraw==(BASE/'large-arrays/request91-pre-arithmetic-inputs'/chunk_rel).read_bytes())
selected={}
for key in ['selected_original_increment_records','selected_original_row_records']:
 d=result[key];p=descriptor(SCI,d,key);s=gzip.decompress(p.read_bytes());lines=s.splitlines(keepends=True)
 check(key+'/decoded-SHA-count',sha(s)==d['extracted_raw_sha256'] and len(lines)==d['extracted_records'])
 selected[key]=[json.loads(v) for v in lines]
nodeledger={x['node']:x for x in selected['selected_original_increment_records']}
rowledger={x['node']:x for x in selected['selected_original_row_records']}
check('selected-four-node-indices',sorted(nodeledger)==[9,10,11,12])
check('selected-three-stage-indices',sorted(rowledger)==[9,10,11])
for n,item in nodeledger.items():
 for name,key in [('base-states','base_node_raw_sha256'),('trial-states','trial_node_raw_sha256'),('native-delta','delta_node_raw_sha256')]:
  check('node-ledger-payload/'+str(n)+'/'+name,sha(raw[name][n*224*8:(n+1)*224*8])==item[key])
for n,item in rowledger.items():
 stagebytes=jraw[(n-8)*224*224*8:(n-7)*224*224*8]
 check('stage-ledger-J-payload/'+str(n),sha(stagebytes)==item['realized_action_source']['J_stage_raw_sha256']==item['saved_endpoint_source']['original_J_stage_sha256'])
node_report=load(descriptor(SCI,result['complete_four_node_coordinate_diagnostics'],'node-report'))
check('node-report-counter',node_report['coordinate_count']==896 and node_report['original_nodes']==[9,10,11,12])
coords={};nodechecks=[]
def hword(buf,index):return buf[index*8:(index+1)*8].hex()
for n in node_report['nodes']:
 index=n['node'];check('node-report-full-column-order/'+str(index),[c['column'] for c in n['coordinates']]==list(range(224)))
 for c in n['coordinates']:
  j=c['column'];coords[index,j]=c
  for buf,key in [('base-states','base'),('trial-states','trial'),('native-delta','delta')]:check('node-word/'+str(index)+'/'+str(j)+'/'+key,c[key]['float64le_hex']==hword(raw[buf],index*224+j))
  for k,v in c['original_dyadic_encodings'].items():check('copied-node-dyadic/'+str(index)+'/'+str(j)+'/'+k,v==nodeledger[index][k][j])
  check('base-trial-equality-flag/'+str(index)+'/'+str(j),c['original_base_and_trial_words_equal']==(c['base']['float64le_hex']==c['trial']['float64le_hex']))
  hz=c['exact_h']['numerator']=='0';wz=c['exact_ideal_alpha_delta']['numerator']=='0'
  expected='zero-realized-zero-ideal' if hz and wz else ('zero-realized-nonzero-ideal' if hz else 'nonzero-realized')
  check('recorded-category/'+str(index)+'/'+str(j),c['category']==expected)
 nodechecks.append({'node':index,'columns':224,'all_original_base_trial_delta_words_checked':True,'all_original_dyadic_encodings_copied_exactly':True})
rows=[];rowaudit=[]
for rs in result['rows']:
 r=load(descriptor(SCI,rs['full_row'],'row/'+str(rs['original_global_equation_row'])));rows.append(r)
 n=r['original_stage'];i=r['original_row'];g=r['original_global_equation_row']
 check('row-map/'+str(g),g==112+n*224+i and r['propagation_orientation']['incoming_node']==n+1 and r['propagation_orientation']['outgoing_node']==n)
 jr=descriptor(SCI,r['original_J_row'],'original-J-row/'+str(g)).read_bytes();off=((n-8)*224*224+i*224)*8
 check('original-J-row-slice/'+str(g),jr==jraw[off:off+1792])
 check('row-all224-original-order/'+str(g),[c['incoming_column'] for c in r['all_224_incoming_contributions']]==list(range(224)))
 groupcounts=collections.Counter()
 for c in r['all_224_incoming_contributions']:
  j=c['incoming_column'];nc=coords[n+1,j];label=str(g)+'/'+str(j);groupcounts[c['category']]+=1
  check('coefficient-word/'+label,c['original_J_coefficient']['float64le_hex']==hword(jr,j))
  check('incoming-state-words/'+label,c['base_state_word']==nc['base'] and c['trial_state_word']==nc['trial'])
  check('incoming-recorded-increments/'+label,all(c[k]==nc[k] for k in ['exact_h','exact_ideal_alpha_delta','exact_h_minus_ideal']) and c['category']==nc['category'])
 for k,v in r['groups'].items():check('row-groupcount/'+str(g)+'/'+k,v['count']==groupcounts[k])
 for name,entry in r['original_eight_row_values'].items():check('copied-eight-original-dyadics/'+str(g)+'/'+name,entry['original_dyadic']==rowledger[n]['exact_vectors'][name][i])
 oc=r['outgoing_negative_identity_contribution'];nc=coords[n,i]
 check('outgoing-original-words/'+str(g),oc['original_base']==nc['base'] and oc['actual_trial']==nc['trial'])
 check('outgoing-recorded-increments/'+str(g),all(oc[k]==nc[k] for k in ['exact_h','exact_ideal_alpha_delta','exact_h_minus_ideal']))
 oo=r['actual_output_and_target']
 check('actual-output-word/'+str(g),oo['original_noJ_flow_output']['float64le_hex']==hword(raw['trial-stage-out'],n*224+i))
 check('actual-target-word/'+str(g),oo['target']['float64le_hex']==hword(raw['trial-states'],n*224+i))
 check('stored-residual-word/'+str(g),oo['stored_trial_residual']['float64le_hex']==hword(raw['trial-stage-residuals'],n*224+i))
 check('row-original-sigma-word/'+str(g),r['original_sigma']['float64le_hex']==hword(raw['original-scales'],n)==rowledger[n]['original_sigma_float64le_hex'])
 check('reported-full-row-identities/'+str(g),r['all_original83_row_equalities_verified'] is True and r['no_coordinate_or_contribution_dropped'] is True)
 check('row-summary-field-copies/'+str(g),rs['groups']==r['groups'] and rs['largest_absolute_incoming_contribution']==r['largest_absolute_incoming_contribution'] and rs['complete_state_formation_sum_over_sigma']==r['complete_state_formation_sum_over_sigma'] and rs['output_and_target_spacing']==oo)
 rowaudit.append({'global_row':g,'stage':n,'row':i,'incoming_count':224,'group_counts':dict(groupcounts),'original_J_row':r['original_J_row'],'complete_row_file':rs['full_row'],'all_values_are_original_Actions_records':True})
# JSON numeric words are checked by byte packing only; no new arithmetic on them.
wordcount=0;neighbourcount=0;wordfail=[]
def wordwalk(v,path):
 global wordcount,neighbourcount
 if isinstance(v,dict):
  if 'float64le_hex' in v and 'value' in v:
   hx=v['float64le_hex']; wordcount+=1
   if v['value'] is not None:
    if struct.pack('<d',v['value']).hex()!=hx:wordfail.append(path)
  if set(['original','down','up'])<=set(v) and isinstance(v['original'],dict) and 'float64le_hex' in v['original']:
   w=int.from_bytes(bytes.fromhex(v['original']['float64le_hex']),'little')
   # Integer-only IEEE encoding adjacency, no floating nextafter or spacing arithmetic.
   lower,upper=((1<<63)|1,1) if w&((1<<63)-1)==0 else ((w+1,w-1) if w>>63 else (w-1,w+1))
   for k,expected in [('down',lower),('up',upper)]:
    if isinstance(v[k],dict) and 'adjacent' in v[k]:
     neighbourcount+=1
     if int.from_bytes(bytes.fromhex(v[k]['adjacent']['float64le_hex']),'little')!=expected:wordfail.append(path+'/'+k)
  for k,item in v.items():wordwalk(item,path+'/'+k)
 elif isinstance(v,list):
  for i,item in enumerate(v):wordwalk(item,path+'/'+str(i))
for label,value in [('full-result',result),('four-node-coordinates',node_report)]+[('full-row-'+str(r['original_global_equation_row']),r) for r in rows]:wordwalk(value,label)
check('all-original-JSON-float-word-encodings-and-adjacencies',not wordfail,{'packed_word_records':wordcount,'integer_adjacent_word_checks':neighbourcount,'failed_paths':wordfail})
norm=result['dimensionless_native_norm_word_diagnostics'];nw=norm['original_native_base_and_actual_trial_norm']['float64le_hex'];aw=norm['exact_original_global_norms']['realized_affine_residual']['correctly_rounded_binary64']['float64le_hex']
word_distance=int.from_bytes(bytes.fromhex(nw),'little')-int.from_bytes(bytes.fromhex(aw),'little')
check('positive-IEEE-norm-word-distance',word_distance==12,{'native_word':nw,'reported_RN_a_word':aw,'integer_word_distance':word_distance,'no_norm_or_rounding_recomputed':True})
for name,rec in norm['exact_original_global_norms'].items():
 original=oldfull['exact_original_sigma_maxima'][name]
 check('copied-global-norm-original-ratio/'+name,rec['original_exact_maximum']==original['exact_absolute_scaled_value'])
 check('copied-global-norm-original-location/'+name,all(rec['original_max_coordinate'][k]==original[k] for k in rec['original_max_coordinate']))
sourceid=load(BASE/'request91-input-and-source-identity.json')
check('actual91-source-commit',sourceid['source_commit']=='b78f0dd1471a118d2ed21467602509d188c2ab67')
sources={x['file']:dict(x) for x in sourceid['verified_sources']}
for x in oldfull['original_frozen_source_receipts']+oldfull['additional_frozen_consumer_sources']:sources.setdefault(x['file'],dict(x))
sources['exact_20261115_native_realized_step_affine_decomposition.py']={'file':'exact_20261115_native_realized_step_affine_decomposition.py','sha256':oldfull['source_sha256']}
sources[result['rounding_function_text_origin']['file']]=dict(result['rounding_function_text_origin'])
for name,s in sources.items():
 p=COMP/name
 if not p.is_file():
  source_checks.append({'file':name,'expected_sha256':s['sha256'],'local_file_available':False,'recorded_provenance_retained':True});continue
 x=identity(p,name);ok=x['sha256']==s['sha256']
 source_checks.append(dict(x,expected_sha256=s['sha256'],matches_frozen=ok,local_file_available=True))
 check('frozen-source-bytes/'+name,ok)
 if 'bytes' in s:check('frozen-source-size/'+name,x['bytes']==s['bytes'])
check('producer-source-current-and-frozen',result['source_sha256']==sourceid['request']['source_sha256'][result['source_file']])
# The result fields are copied, not re-evaluated. Keep every column and every node coordinate.
literal={'schema':'actual91-complete-literal-readout-no-scientific-recomputation-v1','actual_run':{'run_id':43672150224,'source_commit':'b78f0dd1471a118d2ed21467602509d188c2ab67','job_id':132684339596,'artifact_id':14145200674,'archive_bytes':10267458,'archive_sha256':'78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6'},'complete_original_result':result,'all_four_complete_224_column_reports':rows,'all_four_complete_original_nodes':node_report,'copied_original_node_ledger_records':selected['selected_original_increment_records'],'copied_original_stage_ledger_records':selected['selected_original_row_records'],'local_readout_scope':'Original JSON copying, raw-byte/SHA/IEEE encoding verification only; all mathematical ratios/actions/rounding results are the original Actions outputs.'}
lraw=(json.dumps(literal,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode();lp=OUT/'2026-11-15-actual91-complete-literal-readout.json.gz';lp.write_bytes(gzip.compress(lraw,mtime=0))
compact={'schema':'actual91-four-row-literal-key-results-v1','actual_run':literal['actual_run'],'reported_completion':{k:result[k] for k in ['completed','elapsed_seconds','maximum_RSS_kib','complete_original_row_count','complete_incoming_contribution_count','complete_outgoing_contribution_count','complete_original_four_node_coordinate_count','new_RHS_calls','new_J_calls','new_ODE_steps','new_QR_calls','new_solve_calls','new_trial_calls','errors']},'original_tolerance':result['original_tolerance'],'native_norm_words':norm,'rows':[],'source_scope_limits':result['source_scope_limits'],'complete_literal':identity(lp),'complete_literal_decoded_bytes':len(lraw),'complete_literal_decoded_sha256':sha(lraw)}
for r in rows:
 j=r['largest_absolute_incoming_contribution']['column'];compact['rows'].append({k:r[k] for k in ['original_global_equation_row','original_stage','original_row','component','mode','propagation_orientation','original_sigma','original_eight_row_values','groups','incoming_total_over_sigma','outgoing_negative_identity_contribution','complete_state_formation_sum_over_sigma','largest_absolute_incoming_contribution','actual_output_and_target']}|{'dominant_input_column_complete_original_record':r['all_224_incoming_contributions'][j]})
cp=OUT/'2026-11-15-actual91-literal-key-results.json';cp.write_text(json.dumps(compact,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
audit={'schema':SCHEMA,'all_checks_passed':True,'check_count':len(checks),'scope':{'local_new_scientific_arithmetic':False,'numerical_or_native_modules_imported':False,'local_matrix_or_RHS_J_QR_norm_rational_rounding_actions':0,'JSON_and_bytes_only':True,'integer_IEEE_encoding_checks_only':True,'original_whole_ZIP_verification_by_root_not_repeated':True,'original_matrix_whole_payload_not_reloaded':True,'whole_four_selected_rows_coefficients_verified':True,'whole_896_node_coordinate_words_verified':True,'exact_rational_sums_not_recomputed_locally':True,'full_original83_JSONL_ledgers_not_in_actual91_artifact_selected_complete_lines_only':True},'actual_run':literal['actual_run'],'artifact_file_count':len(files),'artifact_files':files,'decoded_gzip_files':decoded,'current_and_inherited_sources':source_checks,'complete_original_array_descriptors':array_descriptors,'complete_original_array_bytes':sum(x['bytes'] for x in array_descriptors),'node_identity_checks':nodechecks,'four_row_identity_checks':rowaudit,'original_norm_IEEE_word_distance':word_distance,'full_literal':identity(lp),'compact_literal':identity(cp),'checks':checks}
ap=OUT/'2026-11-15-actual91-full-byte-audit.json';a=(json.dumps(audit,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode();ap.write_bytes(a);ag=ap.with_suffix('.json.gz');ag.write_bytes(gzip.compress(a,mtime=0))
small={'schema':'actual91-byte-audit-summary-v1','passed':True,'check_count':len(checks),'artifact_file_count':len(files),'decoded_gzip_count':len(decoded),'frozen_source_count':len(source_checks),'frozen_sources_locally_matched':sum(x.get('matches_frozen',False) for x in source_checks),'original_raw_array_count':len(array_descriptors),'original_raw_array_bytes':audit['complete_original_array_bytes'],'selected_J_chunk_bytes':len(jraw),'selected_row_count':len(rows),'incoming_columns_checked':896,'node_coordinates_checked':896,'IEEE_word_records_checked':wordcount,'IEEE_adjacencies_checked':neighbourcount,'norm_word_distance_integer_only':word_distance,'reported_science_elapsed_seconds':result['elapsed_seconds'],'reported_science_RSS_KiB':result['maximum_RSS_kib'],'full_audit':identity(ag),'full_audit_decoded':identity(ap),'compact_literal':identity(cp),'complete_literal':identity(lp),'scope':audit['scope']}
sp=OUT/'2026-11-15-actual91-byte-audit-summary.json';sp.write_text(json.dumps(small,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(small,indent=2))
