#!/usr/bin/env python3
"""Original-file/JSON/source identity readback only; no scientific imports."""
import argparse, gzip, hashlib, json
from pathlib import Path


def digest(b): return hashlib.sha256(b).hexdigest()
def read(p):
    b=p.read_bytes(); raw=gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b
    return json.loads(raw),b,raw
def subset(a,b): return all(k in b and v==b[k] for k,v in a.items())
def write(p,d,compressed=False):
    b=(json.dumps(d,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
    p.write_bytes(gzip.compress(b,mtime=0) if compressed else b)
    return dict(file=p.name,bytes=p.stat().st_size,sha256=digest(p.read_bytes()))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--published-directory',required=True);ap.add_argument('--parent-directory',required=True);ap.add_argument('--source-directory',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
    root,parent,src,out=map(Path,(a.published_directory,a.parent_directory,a.source_directory,a.out));out.mkdir(parents=True,exist_ok=True)
    receipt,rb,_=read(root/'published-original-fetch.json')
    assert receipt['science_run']==43671882961 and receipt['science_source']=='032c513ab5db8aff98a6efca2070375418846098'
    docs={};files=[]
    for d in receipt['files']:
        x,b,raw=read(root/d['file']);assert len(b)==d['bytes'] and digest(b)==d['sha256']
        if 'original_sha256' in d:
            assert len(raw)==d['original_bytes'] and digest(raw)==d['original_sha256']
            files.append(dict(file=d['original_file'],bytes=len(raw),sha256=digest(raw),scope='Exact gzip-decoded original bytes; not JSON reserialization'))
        files.append(dict(file=d['file'],bytes=len(b),sha256=digest(b)));docs[d['file']]=x
    files.append(dict(file='published-original-fetch.json',bytes=len(rb),sha256=digest(rb)))
    s=docs['twenty-six-condensed-warm/driver-status.json.gz'];m=docs['twenty-six-condensed-warm/model-000.json'];q=docs['twenty-six-condensed-warm/condensed-QP-summary.json'];w=docs['twenty-six-condensed-warm/warm-001.json.gz'];f=docs['physical-response/response-check.json.gz']
    pw,pwb,_=read(parent/'twenty-five-condensed-warm/warm-001.json.gz')
    ps,psb,psraw=read(parent/'twenty-five-condensed-warm/driver-status.json.gz')
    ph=digest(pwb);psh=digest(psraw)
    files.extend([dict(file='actual86/warm-001.json.gz',bytes=len(pwb),sha256=ph),dict(file='actual86/original-decoded-driver-status.json',bytes=len(psraw),sha256=psh)])
    warm_sha=next(d['sha256'] for d in receipt['files'] if d['file'].endswith('warm-001.json.gz'))
    entries=[s['twenty_six_query_projection_entry'],m['twenty_six_query_projection_entry'],w['twenty_six_query_projection_entry']]
    accepted=[t for t in m['trials'] if t['accepted']]
    schema='exact-constraint-twenty-six-query-condensed-complete-H-warm-v1'
    checks={
        'original_parent_warm_sha256':ph=='d38c6968225535cb26c46c9dc3f9892603ef0c94942d9c571356fa016bccf69e' and s['identity']['resume_sha256']==ph and all(e['actual_resume_sha256']==ph for e in entries),
        'original_parent_status_sha256':psh=='7d6e7fa1fa3e92397d353f1e9b7c2a9c12d750f9714c2e79b1cfdfc40862a235' and all(e['actual_parent_status_sha256']==psh for e in entries),
        'parent_status_identity_is_parent_producer_subset':subset(ps['identity'],pw['optimization_warm']),
        'parent_status_binds_parent_warm':ps['latest_warm_sha256']==ph,
        'complete_parent_producer_retained':w['optimization_warm']['resume_producer']==pw['optimization_warm'],
        'actual_new_warm_bytes_match_status':s['latest_warm_sha256']==warm_sha,
        'status_identity_is_new_producer_subset':subset(s['identity'],w['optimization_warm']),
        'status_iteration_is_original_model_subset':len(s['iterations'])==1 and subset(s['iterations'][0],m),
        'FD_binds_actual_new_warm':f['prepared_sha256']==warm_sha,
        'FD_whole_producer_matches_new_warm':f['optimization_warm']==w['optimization_warm'],
        'mesh_preserved':w['mesh']==pw['mesh'],
        'status_transparent_gzip_decode':digest(gzip.decompress((root/'twenty-six-condensed-warm/driver-status.json.gz').read_bytes()))=='c78528682d239d941ccc1391df004c8da3b51d60b6315c6d30334828d0204540',
        'FD_transparent_gzip_decode':digest(gzip.decompress((root/'physical-response/response-check.json.gz').read_bytes()))=='12da677b5be6d4a74023b8c8241e18a8a133d3aba841a9d9d8dc64f233400246',
        'current_schema_binds_all_reports':s['schema']==w['optimization_warm']['schema']==f['optimization_warm']['schema']==schema and all(e['optimizer_schema']==schema for e in entries),
        'original_scientific_unaccepted_flags':s['success'] is False and s['new_coupled_finite_acceptance'] is False and w['success'] is False and w['new_coupled_finite_acceptance'] is False and f['full_BVP_solved'] is False and f['nonlinear_native_at_current_H_solved'] is False,
        'readback_accepted_original_trial':len(accepted)==1 and accepted[0] is m['trials'][-1] and accepted[0]['alpha']==0.03125 and s['accepted_warm_steps']==1 and accepted[0]['actual_fixed_weight_merit']==w['optimization_warm']['actual_fixed_weight_merit'],
        'published_original_fetch_manifest_matches_actual_files':True,
    }
    assert len(checks)==17 and all(checks.values()),checks
    assert len(s['identity']['source_sha256'])==62
    assert len(f['consumed_source_sha256'])==66
    sources={}
    for ledger in [s['identity']['source_sha256'],f['consumed_source_sha256']]:
        for name,h in ledger.items():
            assert name not in sources or sources[name]==h
            sources[name]=h
    verified=[]
    for name,h in sorted(sources.items()):
        b=(src/name).read_bytes();assert digest(b)==h,name
        verified.append(dict(name=name,bytes=len(b),sha256=h,local_file=str(src/name)))
    assert len(verified)==66
    wrapper='geometry_20261114_twenty_six_query_collocation_observer_warm.py'
    wb=(src/wrapper).read_bytes();assert digest(wb)==s['execution_wrapper_source_sha256']==m['execution_wrapper_source_sha256']==w['execution_wrapper_source_sha256']
    assert len(w['mesh'])==len(w['states'])==len(w['rhs'])==699 and all(len(r)==453 for r in w['states']+w['rhs'])
    chain=[];v=w['optimization_warm']
    while isinstance(v,dict):
        chain.append(dict(schema=v.get('schema'),resume_sha256=v.get('resume_sha256'),source_count=len(v.get('source_sha256',{}))))
        v=v.get('resume_producer')
    identity=dict(schema='actual89-published-primary-byte-and-producer-readback-v1',run_id=43671882961,source_commit=receipt['science_source'],job_id=132683564697,artifact_id=14145231618,artifact_bytes=687750414,artifact_sha256='e2859210d8baf814f4b6f88fbea5a0157ebbfce55c4c6a02429d4c64848c3583',
       artifact_identity_scope='Official tuple supplied and pinned by root; full scientific ZIP not downloaded in this local primary readback',scope='Original five published files and two decoded originals, parent bytes, JSON identity relationships and source digests only; no scientific computation',files=files,parent_and_report_checks=checks,source_count=len(verified),mathematical_producer_source_count=62,FD_source_count=66,verified_sources=verified,unresolved_sources=[],additional_observer_wrapper=dict(name=wrapper,bytes=len(wb),sha256=digest(wb)),producer_chain=chain,
       complete_scientific_artifact_downloaded_in_this_local_readback=False,complete_array_byte_audit_performed_in_this_primary_readback=False,full_QR_factor_files_independently_audited=False)
    identity_receipt=write(out/'2026-11-15-actual89-primary-identity-readback.json',identity)
    # Omit only repeated source/provenance subtrees. Numerical, domain, row and
    # original-array descriptor fields, including all six sets of 26 grids, stay.
    omit={'source_entry','resume_producer','twenty_six_query_projection_entry','condensed_QP_entry','read_only_collocation_observer_entry','original_source_and_parent_entry'}
    def prune(v):
        if isinstance(v,dict): return {k:prune(x) for k,x in v.items() if k not in omit}
        if isinstance(v,list): return [prune(x) for x in v]
        return v
    fd={k:v for k,v in f.items() if k!='optimization_warm'}
    literal=dict(schema='actual89-original-report-literal-readout-v1',scope='All current model/trial/selected25/RMS/FD/condensation/QP scientific fields copied from original JSON, without numerical recomputation; repeated source-entry/provenance subtrees omitted and separately bound in identity file.',run_id=43671882961,
       status={k:v for k,v in s.items() if k not in ('identity','iterations','twenty_six_query_projection_entry','condensed_QP_entry','read_only_collocation_observer_entry')},
       original_model=prune(m),original_QP_summary=prune(q),FD=fd,
       actual_native_height=w['optimization_warm']['actual_native_height'],actual_global_scalar_parameters=w['optimization_warm']['actual_global_scalar_parameters'],
       actual_selected_original_angles_after=prune(w['optimization_warm']['actual_selected_original_angles_after']),
       query_specs=w['query_specs'],actual_current_entry=w['twenty_six_query_projection_entry'],actual_current_condensed_entry=w['condensed_QP_entry'],identity_readback=identity_receipt)
    lr=write(out/'2026-11-15-actual89-original-readout.json.gz',literal,True)
    print(json.dumps(dict(identity=identity_receipt,literal=lr,checks=len(checks),sources=len(verified),extra_wrapper=digest(wb)),indent=2))


if __name__=='__main__': main()
