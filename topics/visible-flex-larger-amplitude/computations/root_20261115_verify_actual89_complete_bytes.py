#!/usr/bin/env python3
"""Root source/receipt-byte checks; no absent scientific payload or arithmetic."""
from pathlib import Path
import gzip, hashlib, json, subprocess

REPO=Path('/workspace/scratch/visible-larger-recovered-20261114-1843/math-research-public')
ROOT=Path('/tmp/visible-larger-recovery-2207/actions-debug/visible-completed-readback-43676206729-1')
NEW=Path('/tmp/visible-larger-actual89-complete-reader')
OUT=Path('/tmp/2026-11-15-actual89-complete-reader-root-independent-byte-readback.json')
SOURCE='032c513ab5db8aff98a6efca2070375418846098'
def sha(raw):return hashlib.sha256(raw).hexdigest()
def read(name):
    b=(NEW/name).read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)

report={'schema':'actual89-complete-reader-root-independent-byte-v1',
 'scientific_execution':False,'new_download_performed':False,
 'root_full_text_read':['9147-byte complete note with one corrected date link','33475-byte stdlib reader'],
 'frozen_files':[],'actual_dispatch_source_payloads':[], 'original_gzip_byte_copies':[]}
frozen=read('frozen-files.json');preserved={}
for item in frozen['files']:
    b=(NEW/item['file']).read_bytes();assert len(b)==item['bytes'] and sha(b)==item['sha256']
    preserved[item['file']]=b;report['frozen_files'].append(item)
summary=read('2026-11-15-actual89-complete-reader-appendix-summary.json')
cross=read('2026-11-15-actual89-complete-reader-crosswalk-and-byte-audit.json.gz')
assert len(cross['primary_relationship_crosswalk'])==17
assert all(x['primary_recorded_value'] is True and x['local_repeat_from_original_bytes'] is True for x in cross['primary_relationship_crosswalk'])
for row in cross['source_crosswalk']:
    path='topics/visible-flex-larger-amplitude/computations/'+row['name']
    b=subprocess.check_output(['git','show',SOURCE+':'+path],cwd=REPO)
    assert len(b)==row['bytes'] and sha(b)==row['sha256'],row['name']
    report['actual_dispatch_source_payloads'].append({'file':path,'bytes':len(b),'sha256':sha(b)})
assert len(report['actual_dispatch_source_payloads'])==77
for row in summary['original_evidence']:
    b=(NEW/row['file']).read_bytes();raw=gzip.decompress(b)
    assert raw==(ROOT/row['original_file']).read_bytes()
    assert len(b)==row['bytes'] and sha(b)==row['sha256']
    assert len(raw)==row['decoded_bytes'] and sha(raw)==row['decoded_sha256']
    report['original_gzip_byte_copies'].append(row)
for row in cross['local_small_artifact_files']:
    b=(ROOT/row['file']).read_bytes();assert len(b)==row['bytes'] and sha(b)==row['sha256']
assert len(cross['local_small_artifact_files'])==18
assert cross['Actions_raw_payload_descriptors_crosslinked_to_transport']==381
assert len(cross['Actions_raw_payload_descriptor_crosswalk'])==381
assert summary['original_archive_member_count']==413
assert summary['unexported_full_factor_payload_audited'] is False
assert summary['R276_requested'] is False and summary['publication_recovery_requested'] is False
assert (ROOT/'.download-complete').read_text().strip()==summary['reader_tuple']['sha256']
done=subprocess.run(['python',str(NEW/'read_actual89_complete_receipt_bytes.py')],cwd=REPO,capture_output=True,text=True)
assert done.returncode==0,(done.stdout,done.stderr)
for name,b in preserved.items():assert (NEW/name).read_bytes()==b,name
report.update(all_frozen_outputs_replayed_byte_identical=True,primary_relationship_count=17,
 actual_dispatch_source_count=77,local_small_file_count=18,descriptor_transport_links=381,
 original_archive_members=413,original_large_scientific_payload_rehashed_locally=False,
 unexported_complete_factor_payload_audited=False,no_extra_scientific_acceptance_gate=True,passed=True)
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'file':str(OUT),'bytes':OUT.stat().st_size,'sha256':sha(OUT.read_bytes()),
 'passed':True,'source_payloads':77,'local_small_files':18,'relationships':17}))
