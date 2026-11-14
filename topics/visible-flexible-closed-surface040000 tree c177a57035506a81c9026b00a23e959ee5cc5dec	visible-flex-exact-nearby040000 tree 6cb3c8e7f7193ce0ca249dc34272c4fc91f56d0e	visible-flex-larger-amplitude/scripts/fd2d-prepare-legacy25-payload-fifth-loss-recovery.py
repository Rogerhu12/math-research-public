from pathlib import Path
import json, hashlib, os, shutil, subprocess, datetime, sys
SOURCE=Path('/workspace/scratch/fd2d-recovered-20261112/math-research')
TOPIC=Path('topics/visible-flexible-closed-surface')
PUB=Path('/tmp/fd2d-math-research-publish-isolated-25')
AUDIT=Path('/tmp/fd2d-legacy25-audit')
PAYLOAD=Path('/tmp/fd2d-legacy25-payload')
INVENTORY=Path('/tmp/fd2d-legacy25-publication-inventory.json')
AUDIT.mkdir(parents=True,exist_ok=True)
def digest(b):return hashlib.sha256(b).hexdigest()
def gitblob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(p,d):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def relative(raw):
 p=Path(raw)
 if p.is_absolute():p=p.relative_to(SOURCE/TOPIC)
 elif p.parts[:2]==TOPIC.parts:p=p.relative_to(TOPIC)
 if '..' in p.parts or p.is_absolute():raise ValueError('unsafe path')
 if p.as_posix() in ['HANDOFF.md','open.md','log.md','results.md','README.md']:raise ValueError('metadata excluded: '+str(p))
 return p
groups=[
('signed36_baselines','notes/2026-11-12-fd2d-signed36-branch-baselines-closed-manifest.json','57ec62a835b6c31033a35dd8a938b5198e09367d3ce53a72cbd7c499cb56fe43'),
('r181_b32_entry','notes/2026-11-12-fd2d-r181-b32-computable-entry-closed-manifest.json',None),
('r183_publication_wrapper','notes/2026-11-12-fd2d-profile-design-extension-R183-publication-closed-manifest.json','c636a11a13f7b58a11f349893d84ca4dfb700f001cc2e214a247cf2329f9e9cd'),
('signed36mid_transport_failure','notes/2026-11-12-fd2d-signed36mid-normal-transport-failure-01-closed-manifest.json','f5c6e64c37dc3d5db5c66cd613de0f6cf4e3efd7ec72a21178b3a42623f17bc1'),
('r182_exact_domain','notes/2026-11-12-fd2d-metric-signed-trace-linear-domain-R182-closed-manifest.json','27f8cd16cebf7acd1f622b314623e4c26f8a352674df1aba1b20fe269c1a4cfc'),
('r182_windows_wrapper','notes/2026-11-12-fd2d-metric-signed-trace-windows-R182-closed-manifest-publish-wrapper.json','c5297ed770dd8ac42acdb6278413a6714639b20eae402039f625c12279fbf555')
]
rows={};evidence=[];errors=[];mappings=[]
def add(row,group,source_override=None):
 rel=relative(row['path']); source=Path(source_override) if source_override else SOURCE/TOPIC/rel
 old=rows.get(rel.as_posix())
 expected=row.get('sha256')
 if old:
  if expected and old['expected_sha256'] != expected:errors.append({'conflict':str(rel),'groups':old['groups']+[group],'hashes':[old['expected_sha256'],expected]})
  else:old['groups'].append(group)
  return
 rows[rel.as_posix()]={'source':str(source),'destination':str(TOPIC/rel),'original_manifest_path':row['path'],'expected_sha256':expected,'expected_bytes':row.get('bytes'),'groups':[group]}
for label,rel,sha in groups:
 p=SOURCE/TOPIC/rel;b=p.read_bytes();d=json.loads(b)
 if sha and digest(b)!=sha:errors.append({'manifest':rel,'expected':sha,'actual':digest(b)})
 items=d.get('files',d.get('artifacts'))
 if not isinstance(items,list):raise ValueError('manifest rows absent '+rel)
 evidence.append({'group':label,'path':rel,'bytes':len(b),'sha256':digest(b),'declared_items':len(items)})
 mappings.extend(d.get('publication_path_mapping',[]))
 for row in items:add(row,label)
 add({'path':rel,'bytes':len(b),'sha256':digest(b)},label+':manifest')
ib=INVENTORY.read_bytes()
assert digest(ib)=='c70f29a55c9da10b47c9b923f89e96568bc09ac96ae818b960e8d34750328022'
inv=json.loads(ib)
sn=inv['signed_native']
for kind in ['sources','artifacts']:
 for row in sn[kind]:add(row,'r182_signed_native:'+kind)
for kind in ['proof_note','field','origin']:add(sn[kind],'r182_signed_native:'+kind)
for row in inv['linear_domain']['artifacts']:add(row,'r182_inventory:linear_domain')
add({'path':'notes/2026-11-12-fd2d-metric-R182-original-publication-inventory.json','bytes':len(ib),'sha256':digest(ib)},'r182_inventory',INVENTORY)
for rel,row in rows.items():
 p=Path(row['source'])
 if not p.is_file():errors.append({'missing':str(p),'destination':row['destination']});continue
 b=p.read_bytes(); actual={'bytes':len(b),'sha256':digest(b),'git_blob_sha1':gitblob(b)}
 row.update(actual)
 if row['expected_sha256'] and row['sha256']!=row['expected_sha256']:errors.append({'hash_mismatch':row})
 if row['expected_bytes'] is not None and row['bytes']!=row['expected_bytes']:errors.append({'size_mismatch':row})
 if row['bytes']>=5_000_000:errors.append({'over_five_MB':row['destination'],'bytes':row['bytes']})
 if row['bytes']>1_000_000 and not rel.endswith('.gz'):errors.append({'uncompressed_over_one_MB':row['destination'],'bytes':row['bytes']})
 if rel.endswith('.md') and row['bytes']>=100_000:errors.append({'markdown_over_100KB':row['destination']})
# R183 original proof must be in its mapped notes path, never replace recovery proof.
for m in mappings:
 if m['original_path'] in rows:errors.append({'forbidden_original_R183_proof_destination':m['original_path']})
 if m['publication_path'] not in rows:errors.append({'missing_R183_publication_mapping':m})
pin=subprocess.check_output(['git','rev-parse','origin/main'],cwd=PUB,text=True).strip()
command=['git','ls-tree','-r','-z',pin,'--']+[row['destination'] for row in rows.values()]
out=subprocess.run(command,cwd=PUB,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30,check=True)
tree={}
for item in out.stdout.split(b'\0'):
 if not item:continue
 head,path=item.split(b'\t',1); mode,typ,sha=head.decode().split()
 tree[path.decode()]={'mode':mode,'type':typ,'blob':sha}
counts={'new':0,'same':0,'different':0}
collisions=[]
for row in rows.values():
 entry=tree.get(row['destination']); row['pinned_main']=entry
 classification='new' if entry is None else ('same' if entry['blob']==row.get('git_blob_sha1') else 'different')
 row['main_classification']=classification;counts[classification]+=1
 if classification=='different':collisions.append(row)
report={'schema':'fd2d-legacy25-source-audit-v1','created_utc':utc(),'source_root':str(SOURCE),'publisher':str(PUB),'pinned_main':pin,'no_git_mutations':True,'new_mathematical_evaluations':False,'manifest_evidence':evidence,'R183_mapping':mappings,'files':list(rows.values()),'file_count':len(rows),'total_bytes':sum(x.get('bytes',0) for x in rows.values()),'classification_counts':counts,'errors':errors}
write(AUDIT/'source-audit.json',report)
write(AUDIT/'collisions.json',{'pinned_main':pin,'collisions':collisions,'preservation_complete':False})
if errors:
 print(json.dumps({'complete':False,'errors':errors,'report':str(AUDIT/'source-audit.json')},ensure_ascii=False));sys.exit(1)
for row in rows.values():
 target=PAYLOAD/row['destination'];target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists():
  if digest(target.read_bytes())!=row['sha256']:raise FileExistsError(str(target))
 else:shutil.copyfile(row['source'],target)
 if digest(target.read_bytes())!=row['sha256']:raise RuntimeError('copy verification failed')
write(AUDIT/'payload-original-files.json',{'pinned_main':pin,'files':[{'path':r['destination'],'bytes':r['bytes'],'sha256':r['sha256'],'source':r['source'],'groups':r['groups'],'main_classification':r['main_classification']} for r in rows.values()]})
print(json.dumps({'complete_source_verification':True,'pinned_main':pin,'file_count':len(rows),'total_bytes':report['total_bytes'],'classifications':counts,'collisions':[{'path':x['destination'],'main_blob':x['pinned_main']['blob'],'restored_sha256':x['sha256'],'bytes':x['bytes']} for x in collisions],'audit':str(AUDIT/'source-audit.json'),'payload':str(PAYLOAD)},ensure_ascii=False))
