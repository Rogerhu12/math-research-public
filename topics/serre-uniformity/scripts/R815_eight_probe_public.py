#!/usr/bin/env python3
"""Source-bound standard-library public IO for one new R815 nine-dimensional lattice.
No mathematical core is imported by this runner; inherited IO is pinned byte-for-byte.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import tarfile

S=Path(__file__).resolve().parent
REPO=S.parents[2]
TOPIC=REPO/'topics/serre-uniformity'
REQUEST=TOPIC/'notes/R815_eight_probe-public-request.json'
RESULT='R815-original-normal-derivation-operators'
FINAL='p41-original-normal-derivation-operator-certificate.json'
INPUT_BUNDLE='R815-retained-producer-inputs.tar.gz'
PREVIOUS_SCAN_BUNDLE='R815-three-columns-previous-scan-inputs.tar.gz'
COMPLETED_BUNDLE='R815-eight-probe-completed-three-columns.tar.gz'
REFERENCE='full-outputs-manifest-reference.json'
LABELS=('R806','R813')
ALL_LABELS=('R806','R813','R815')
EPS=[0]+[1]*144+[2]*127
FIELD_BASIS='Q in the unchanged original K-normal basis'
BASE=('result','run_id','source_commit','core_sha256','manifest_sha256')
SOURCE_KEYS=BASE
PATTERN_SHA=re.compile(r'[0-9a-f]{64}')
LEGACY_CORE_SHA='80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d'
IO_HELPER_SHA='c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c'
THREE_IO_SHA='3b573881361342a9b3849aacc35ff040d067938d82da2ff7b7a4568d332fc69f'
THREE_SHA='515e15557ea3681055178f5da742d5c4fcee9d5d6a313e5c5892124872a72f83'
THREE_METHOD_SHA='6d12fe13d77ba1f8d970cc697faf229027d812f7b7a067590bd6a3946426f6d4'
THREE_TAG_SHA='e9bdaaad21dad23d7180383deee207bc279639a8d157029b98ef5fa2236e2c37'
PROJECTIVE_MODE='three-known-columns-and-eight-simultaneous-probes-in-nine-dimensional-lattice'
PROBE_INDICES=(10,11,12,13,15,17,20,24)
OLD_W='R815-original-primitive-polynomial-input.json.gz'
OLD_VECTOR={key:'R815-target-'+key+'-component-00-original-vector.json.gz' for key in ('g','h')}
OLD=None
IO=None

SEARCH_STRATEGY = {
    "probe_indices": list(PROBE_INDICES),
    "probe_source": "four completed original three-column pairs; no new scalar RR or scan",
    "known_columns": [0, 1, 271],
    "known_denominator": "completed jointly reduced d012, not the full operator denominator",
    "integer_row_lattice": "first row [d012,center(d012*r_i) for eight probes]; remaining rows diag M",
    "dimension": 9, "column_weights": [1]*9, "number_of_new_LLL_calls": 1,
    "LLL_parameters": {"delta": "0.99", "eta": "0.51"},
    "LLL_certificate": "all nine returned rows; integer U*H=R and det U=+1 or -1",
    "candidate_rows": "all nine original rows; positive D, d012 divides D, gcd(D,M)=1",
    "candidate_matrix": "exact D/d012 times completed columns0/1/271; all other coefficients=center(D*r)",
    "duplicate_policy": "same integer D and same original current, known columns, W, weighted order and frozen candidate code",
    "old_rejections": "source-bound exact nonzero required commutator entry; never rerun identical candidate",
    "success_exit": "original three columns, weighted support, full exact seven-point commutator, then frozen Gamma",
    "height_or_reconstruction_rectangle": None,
}

def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Execution and new mathematics belong to public repository Actions.")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as compressed:
                compressed.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def check_spec(row):
    assert Path(row["file"]).name == row["file"] and row["file"] not in ("", ".", "..")
    assert isinstance(row["bytes"], int) and row["bytes"] >= 0
    assert PATTERN_SHA.fullmatch(row["sha256"])


def identity(item):
    value = {key: item[key] for key in
             ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name")}
    value["certificate_sha256"] = item["files"][item["certificate_name"]]
    return value


def same_identity(left, right):
    if "files" in left:
        left = identity(left)
    if "files" in right:
        right = identity(right)
    assert set(left) == set(right)
    for key in left:
        assert str(left[key]) == str(right[key]), ("Changed mathematical producer", key)


def topic_path(relative):
    path = (TOPIC/relative).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def github(path):
    return json.loads(subprocess.check_output(
        ["gh", "api", "repos/Rogerhu12/math-research-public/"+path], text=True))




def completed_source_identity(source):
    answer = {key: str(source[key]) for key in SOURCE_KEYS}
    assert answer["result"] == RESULT and answer["core_sha256"] == THREE_SHA
    assert answer["run_id"] == "43762388370"
    assert answer["source_commit"] == "ca1fe0d562497055f9e5441edc17ac588a25229c"
    assert answer["manifest_sha256"] == "0f2be930adc35c414f8f7f69c7dfd2ada3b0b5fe076d66f7c08583d416cd1718"
    answer["configuration_sha256"] = source["configuration_sha256"]
    assert answer["configuration_sha256"] == THREE_TAG_SHA
    for key in ("certificate", "stage_manifest", "known_columns", "scan", "source_audit",
                "input_bundle", "previous_scan_input_bundle"):
        answer[key] = plain(source[key])
    answer["probe_pairs"] = [plain(value) for value in source["probe_pairs"]]
    assert len(answer["probe_pairs"]) == 4
    return answer


def load_io(item):
    global OLD,IO
    path=S/item['three_column_io_helper']
    assert sha(path)==item['three_column_io_helper_sha256']==THREE_IO_SHA
    loader=importlib.util.spec_from_file_location('R815_eight_probe_frozen_source_IO',path)
    OLD=importlib.util.module_from_spec(loader)
    loader.loader.exec_module(OLD)
    OLD.load_io(item)
    IO=OLD.IO


def source_identity(source):
    return {key:str(source[key]) for key in BASE}


def shared_cache_identity(producers):
    return OLD.shared_cache_identity(producers)


def expected_target_configurations(tag,producers):
    return OLD.expected_target_configurations(tag,producers)


def stable_job(item):
    answer=json.loads(json.dumps(item))
    answer.pop('resume',None)
    answer.pop('budget_minutes',None)
    answer['projective_source'].pop('files',None)
    return answer


def stable_expanded(item):
    answer=json.loads(json.dumps(item))
    answer.pop('resume',None)
    answer.pop('budget_minutes',None)
    return answer


def expected_configuration(item,producers,original,previous_tag):
    old_item=dict(item,core_sha256=THREE_SHA,projective_method_sha256=THREE_METHOD_SHA)
    expected=OLD.expected_configuration(old_item,producers,original)
    assert expected==previous_tag and fingerprint(expected)==THREE_TAG_SHA
    answer=dict(expected,source_sha256=item['core_sha256'],projective_mode=PROJECTIVE_MODE,
        projective_method_sha256=item['projective_method_sha256'],
        projective_search_strategy=SEARCH_STRATEGY,
        frozen_three_column_core_sha256=THREE_SHA,
        completed_three_columns_source_identity=completed_source_identity(item['completed_three_columns_source']),
        source_three_column_configuration_sha256=THREE_TAG_SHA,
        old_49_candidate_rejections_reused_only_for_identical_D_M_and_known_columns=True,
        old_three_dimensional_LLL_and_scalar_RR_recomputed=False,
        only_runtime_budget_excluded_from_mathematical_identity=True)
    answer.pop('only_budget_and_probe_pair_limit_excluded_from_mathematical_identity')
    return answer


def completed_root(out):
    return out.parent/'completed-three-columns'


def flat_members(bundle,root=None):
    seen=set()
    with tarfile.open(bundle,'r|gz') as tar:
        for member in tar:
            path=PurePosixPath(member.name)
            assert member.isfile() and len(path.parts)==1 and path.name not in ('','.','..')
            assert not path.is_absolute() and '\\' not in member.name and member.name not in seen
            seen.add(member.name)
            target=None if root is None else root/member.name
            temporary=None if target is None else target.with_name(target.name+'.transfer')
            if temporary is not None: temporary.parent.mkdir(parents=True,exist_ok=True)
            digest,total=hashlib.sha256(),0
            stream=tar.extractfile(member)
            destination=None if temporary is None else temporary.open('wb')
            try:
                for block in iter(lambda:stream.read(1024*1024),b''):
                    digest.update(block);total+=len(block)
                    if destination is not None:destination.write(block)
            finally:
                stream.close()
                if destination is not None:destination.close()
            assert total==member.size
            if temporary is not None:temporary.replace(target)
            yield member.name,{'file':member.name,'bytes':total,'sha256':digest.hexdigest()}


def completed_source_review(item,folder,producers=None,original=None):
    source=item['completed_three_columns_source']
    source_id=completed_source_identity(source)
    assert len(source['files'])==198
    actual={path.name for path in folder.iterdir() if path.is_file()}
    assert actual==set(source['files'])
    for name,entry in source['files'].items():
        check_spec(entry)
        assert file_spec(folder/name)==plain(entry)
    manifest=read(folder/'full-outputs-manifest.json')
    assert manifest['result']==RESULT
    by_name={entry['file']:plain(entry) for entry in manifest['files']}
    assert len(by_name)==len(manifest['files'])==198==source['manifest_file_count']
    assert sha(folder/'full-outputs-manifest.json')==source['manifest_sha256']
    for name,entry in source['files'].items():
        if name not in ('full-outputs-manifest.json',REFERENCE):assert plain(entry)==by_name[name]
    reference=read(folder/REFERENCE)
    assert reference['manifest_sha256']==source['manifest_sha256']
    assert reference['manifest_bytes']==source['manifest_bytes'] and reference['file_count']==198
    for key in ('input_bundle','previous_scan_input_bundle'):
        assert plain(source[key])==by_name[source[key]['file']]
        assert source[key]['file'] not in source['files']
    initial=read(folder/'public-actions-input.json')
    run=read(folder/'run-receipt.json');core=read(folder/'core-receipt.json')
    final=read(folder/source['certificate']['file'])
    assert initial['result']==run['result']==core['result']==final['result']==RESULT
    assert initial['source_commit']==run['source_commit']==source['source_commit']
    assert str(run['workflow_run_id'])==str(source['run_id'])
    assert initial['core_sha256']==initial['job']['core_sha256']==core['source_sha256']==THREE_SHA
    assert initial['driver_sha256']==source['wrapper_sha256']==THREE_IO_SHA
    assert run['complete'] is core['complete'] is final['complete'] is False
    assert run['process_exit_code']==2 and run['error'] is None
    assert run['core_receipt_sha256']==source['files']['core-receipt.json']['sha256']
    assert core['certificate_sha256']==source['certificate']['sha256']
    tag=final['configuration']
    assert tag==initial['actual_projective_configuration'] and fingerprint(tag)==THREE_TAG_SHA
    assert tag['source_sha256']==THREE_SHA and tag['projective_mode']==OLD.PROJECTIVE_MODE
    assert tag['projective_method_sha256']==THREE_METHOD_SHA
    assert tag['projective_search_strategy']==OLD.PROJECTIVE_STRATEGY
    assert source_identity(initial['job']['projective_source'])==source_identity(item['projective_source'])
    assert OLD.previous_scan_identity(initial['job'])==OLD.previous_scan_identity(item)
    for label in LABELS:OLD.same_identity(initial['job']['retained_artifacts'][label],item['retained_artifacts'][label])
    if producers is not None:
        expected=OLD.expected_configuration(initial['job'],producers,original)
        assert expected==tag
        assert final['target_configurations']==expected_target_configurations(tag,producers)
    original_current=plain(item['projective_source']['current'])
    assert final['source_original_current']==original_current
    assert final['source_original_latest_receipt']==plain(item['projective_source']['latest_CRT_receipt'])
    assert final['exact_three_known_columns_input']==plain(source['known_columns'])
    assert final['stage_manifest']==plain(source['stage_manifest'])
    inventory=read(folder/source['stage_manifest']['file'])
    assert inventory['configuration']==tag and inventory['complete'] is True
    items=inventory['files']+inventory.get('current_checkpoints',[])
    indexed={entry['file']:plain(entry) for entry in items}
    assert len(indexed)==len(items)
    def stage(entry,target=None,current=False):
        entry=plain(entry)
        assert entry==indexed[entry['file']]==plain(source['files'][entry['file']])
        data=read(folder/entry['file'])
        assert data['configuration']==tag and data['complete'] is (not current)
        if target is not None:
            assert data['target_configuration']==final['target_configurations'][target]
            assert data['target_configuration_sha256']==fingerprint(data['target_configuration'])
        return data
    for entry in inventory['files']:
        data=read(folder/entry['file'])
        assert plain(entry)==plain(source['files'][entry['file']])==by_name[entry['file']]
        assert data['complete'] is True and data['configuration']==tag
        if 'target_configuration' in data:
            assert data['target_configuration']==final['target_configurations'][data['target']]
            assert data['target_configuration_sha256']==fingerprint(data['target_configuration'])
    scan=stage(source['scan'],current=True)
    assert scan['next_coefficient_index']==25 and scan['completed_pair_count']==4
    assert scan['scalar_RR_failure_count']==8 and scan['scan_finished'] is False
    assert scan['unpaired_failure'] is None
    failures=[]
    for number,entry in enumerate(source['probe_pairs']):
        pair=stage(entry)
        assert pair['source_original_current']==original_current
        assert pair['pair_number']==number and len(pair['probes'])==2
        failures.extend(probe['coefficient_index'] for probe in pair['probes'])
    assert failures==list(PROBE_INDICES)
    known=stage(source['known_columns'],'g')
    assert known['source_original_current']==original_current
    assert known['known_column_indices']==[0,1,271]
    assert known['known_column_coefficient_counts']==[690,962,1234]
    assert known['known_column_total_coefficient_count']==2886
    for key in ('all2886_original_current_congruences_verified','all_three_weighted_supports_verified_coefficientwise',
                'original_We0_equals_e1_and_We1_equals_e271_verified_coefficientwise',
                'raw_third_column_powers6_and7_verified_zero','common_denominator_is_positive_and_jointly_reduced',
                'new_exact_W_times_completed_second_column_actually_performed','all_original_scalar_and_field_normalizations_preserved'):
        assert known[key] is True
    assert known['original_completed_Wvg_recomputed'] is False
    assert len(known['column_integer_numerators'])==3
    assert all(len(column)==6 and all(len(row)==272 for row in column) for column in known['column_integer_numerators'])
    for power,entry in enumerate(known['new_third_column_product_blocks']):
        product=stage(entry,'g')
        assert product['left_W_power']==power
        assert product['source_original_current']==original_current
        assert product['source_original_M_w']==known['source_original_M_w']
    definitions={}
    for name,entry in indexed.items():
        if not (name.startswith('R815-projective-g-candidate-') and name.endswith('-definition.json.gz')):continue
        value=stage(entry,'g');D=value['D'];stem=value['projective_candidate_id']
        assert name==stem+'-definition.json.gz' and D not in definitions
        assert value['source_original_current']==original_current
        assert value['source_exact_three_known_columns']==plain(source['known_columns'])
        rejected=stage(indexed[stem+'-rejected.json.gz'],'g')
        assert rejected['additional']['source_candidate_definition']==entry
        early=stage(rejected['additional']['failed_exact_entry'],'g')
        assert early['source_candidate_definition']==entry and early['zero'] is False
        assert [early['exact_integer_point'],early['output_row'],early['input_column']]==[0,0,2]
        assert early['entry_is_part_of_the_required_full_seven_point_identity'] is True
        assert early['candidate_denominator_before_block_content_reduction']==D
        assert early['source_original_M_w']==known['source_original_M_w']
        assert rejected['no_exact_characteristic_zero_multiplier_claimed'] is True
        definitions[D]=entry
    assert len(definitions)==49 and known['common_positive_denominator'] in definitions
    return {'identity':source_id,'configuration':tag,'target_configurations':final['target_configurations'],
            'actual_small_source_file_count':198,'source_manifest_file_count':198,
            'actual_known_column_count':3,'actual_bound_known_coefficients':2886,
            'fixed_failure_indices':failures,'actual_distinct_previous_rejections':49,
            'original_scalar_RR_LLL_products_and_residuals_recomputed':False}


def prepare_sources(item,out,allow_download,record=True):
    source=item['completed_three_columns_source'];folder=completed_root(out)
    folder.mkdir(parents=True,exist_ok=True)
    bundle=out/INPUT_BUNDLE;previous=out/PREVIOUS_SCAN_BUNDLE
    archive=None;transport=None
    try:
        if not all((folder/name).is_file() for name in source['files']) or not bundle.exists() or not previous.exists():
            assert allow_download
            archive=IO.Archive(source,out.parent/'download-completed-three-columns',whole=False)
            archive.extract_many([(name,entry['sha256'],folder/name,entry['bytes'])
                                  for name,entry in source['files'].items()])
            for key,path in (('input_bundle',bundle),('previous_scan_input_bundle',previous)):
                entry=plain(source[key])
                archive.extract_bound(entry['file'],entry['sha256'],path,entry['bytes'])
            transport=archive.receipt()
        assert file_spec(bundle)==plain(source['input_bundle'])
        assert file_spec(previous)==plain(source['previous_scan_input_bundle'])
        basic=completed_source_review(item,folder)
        retained=out.parent/'retained'
        original_members=dict(OLD.bundle_members(bundle,retained))
        assert len(original_members)==3037
        OLD.restore_previous_scan_bundle(item,out,retained)
        previous_review=OLD.review_previous_scan(item,retained)
        producers={label:OLD.Producer(label,item['retained_artifacts'][label],retained/label) for label in LABELS}
        selection=OLD.select_inputs(producers)
        original=OLD.EndedSource(item['projective_source'],retained/'R815')
        original.prefetch()
        source_review=original.validate(item,producers)
        OLD.check_directory_closure(retained,producers,original)
        assert original_members==OLD.selected_files(producers,original)
        review=completed_source_review(item,folder,producers,original)
        assert review==basic
        expanded=OLD.expanded_job(item,original)
        tag=expected_configuration(item,producers,original,review['configuration'])
        small_bundle=out/COMPLETED_BUNDLE
        if not small_bundle.exists():
            assert record, 'Verification requires the actual saved source carrier.'
            temporary=small_bundle.with_name(small_bundle.name+'.tmp')
            with tarfile.open(temporary,'w:gz') as tar:
                for name in sorted(source['files']):tar.add(folder/name,arcname=name,recursive=False)
            temporary.replace(small_bundle)
        assert dict(flat_members(small_bundle))=={name:plain(value) for name,value in source['files'].items()}
        receipt={
            'result':RESULT,'projective_mode':PROJECTIVE_MODE,
            'selection':selection,'original_425_source_review':source_review,
            'selected_original_R815_files':source_review['files'],
            'actual_selected_file_count':len(original_members),
            'input_bundle':file_spec(bundle),'previous_scan_input_bundle':file_spec(previous),
            'completed_three_columns_input_bundle':file_spec(small_bundle),
            'completed_three_columns_source_review':review,'previous_scan_source_review':previous_review,
            'all_selected_bundle_members_individually_size_and_sha256_verified':True,
            'original_two_carriers_preserved_byte_for_byte':True,
            'actual_previous_small_source_files':198,
            'transport_artifact':transport,
            'new_mathematical_arithmetic_performed':False}
        if record:
            save(out/'retained-inputs-receipt.json',receipt)
            save(out/'public-actions-expanded-job.json',expanded)
        else:
            recorded=read(out/'retained-inputs-receipt.json')
            for key in receipt:
                if key != 'transport_artifact':assert recorded[key]==receipt[key]
            assert read(out/'public-actions-expanded-job.json')==expanded
        return retained,producers,original,selection,expanded,tag,review
    finally:
        if archive is not None:archive.close()


def restore_resume(item,out):
    previous=item.get('resume')
    if previous is None:return
    assert previous['result']==RESULT and previous['core_sha256']==item['core_sha256']
    archive=IO.Archive(previous,out.parent/'download-eight-probe-continuation',whole=True)
    try:
        mpath=archive.extract_bound('full-outputs-manifest.json',previous['manifest_sha256'],out.parent/'previous-manifest.json')
        manifest=read(mpath);assert manifest['result']==RESULT
        entries=archive.verify_all(manifest)
        def bound(name,path=None):
            e=entries[name]
            return archive.extract_bound(name,e['sha256'],path or out.parent/'previous-metadata'/name,e['bytes'])
        initial=read(bound('public-actions-input.json'));run=read(bound('run-receipt.json'))
        assert initial['core_sha256']==item['core_sha256']
        assert initial['driver_sha256']==item['wrapper_sha256']
        assert initial['source_commit']==run['source_commit']==previous['source_commit']
        assert str(run['workflow_run_id'])==str(previous['run_id'])
        assert stable_job(initial['job'])==stable_job(item)
        if 'core-receipt.json' in entries:
            core=read(bound('core-receipt.json'))
            assert core['source_sha256']==item['core_sha256'] and core['result']==RESULT
            assert run['core_receipt_sha256']==entries['core-receipt.json']['sha256']
        else:
            assert run['core_receipt_sha256'] is None and run['complete'] is False
        for name in (INPUT_BUNDLE,PREVIOUS_SCAN_BUNDLE,COMPLETED_BUNDLE):bound(name,out/name)
        restored=dict(flat_members(out/COMPLETED_BUNDLE,completed_root(out)))
        assert restored=={name:plain(value) for name,value in item['completed_three_columns_source']['files'].items()}
        retained,producers,original,_,expanded,tag,review=prepare_sources(item,out,False)
        old_expanded=read(bound('public-actions-expanded-job.json'))
        assert stable_expanded(old_expanded)==stable_expanded(expanded)
        assert initial['expanded_job_sha256']==entries['public-actions-expanded-job.json']['sha256']
        assert initial['actual_projective_configuration']==tag
        targets=expected_target_configurations(tag,producers)
        copied=0;checkpoints=[]
        for name,entry in entries.items():
            if name!=FINAL and not(name.startswith('R815-') and name.endswith('.json.gz')):continue
            if name==FINAL:
                value=read(bound(name))
                assert value['result']==RESULT and value['configuration']==tag
                if value.get('complete') is not True:continue
            path=bound(name,out/name)
            if name.endswith('-CRT-current.json.gz'):
                checkpoints.append(name)
            else:
                value=read(path)
                assert value['configuration']==tag
                if 'target_configuration' in value:
                    assert value['target_configuration']==targets[value['target']]
                    assert value['target_configuration_sha256']==fingerprint(targets[value['target']])
                if value['complete'] is False:checkpoints.append(name)
                else:assert value['complete'] is True
            copied+=1
        save(out/'resume-receipt.json',{
            'result':RESULT,'projective_mode':PROJECTIVE_MODE,'previous_actual_artifact':previous,
            'actual_archive_review':archive.receipt(),'all_previous_manifest_members_SHA_verified':True,
            'same_core_strategy_known_columns_and_sources_preserved':True,
            'restored_stage_count':copied,'restored_incomplete_checkpoints':checkpoints,
            'old_false_FINAL_does_not_override_later_atomic_state':True,
            'previous_nine_dimensional_LLL_and_completed_candidates_recomputed':False})
    finally:
        archive.close()
        path=out.parent/'download-eight-probe-continuation'/'artifact.zip'
        if path.exists():path.unlink()


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, proof, method = S/item["core"], topic_path(item["proof"]), topic_path(item["method"])
    nested_proof, framework = topic_path(item["nested_proof"]), S/item["framework"]
    projective_method, legacy = topic_path(item["projective_method"]), S/item["legacy_core"]
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    initial = {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item, "core_sha256": sha(core),
        "proof_sha256": sha(proof), "nested_proof_sha256": sha(nested_proof),
        "method_sha256": sha(method), "framework_sha256": sha(framework),
        "legacy_core_sha256": sha(legacy), "projective_method_sha256": sha(projective_method),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "io_helper_sha256": sha(S/item["io_helper"]),
        "three_column_io_helper_sha256": sha(S/item["three_column_io_helper"]),
        "frozen_three_column_core_sha256": sha(S/item["three_column_core"]),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "projective_mode": PROJECTIVE_MODE,
        "new_arithmetic": "one complete nine-dimensional lattice from eight completed scalar failures; unchanged three columns and 425 source; exact Mg and original Gamma",
        "original_425_Mg_prime_arithmetic_recomputed": False,
        "independent_Mh_reconstruction": False,
        "polar_preimages_function_DAG_eta_or_height_claimed": False,
    }
    save(out/"public-actions-input.json", initial)
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert item["producer_inputs_pending"] is False
        assert item["requested_stage"] == "original_normal_derivation_operators"
        assert item["requested_targets"] == ["g", "Gamma"]
        assert set(item["retained_artifacts"]) == set(LABELS)
        assert sha(core) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
        assert sha(proof) == item["R813_proof_sha256"] and sha(method) == item["R815_method_sha256"]
        assert sha(nested_proof) == item["R817_proof_sha256"]
        assert sha(projective_method) == item["projective_method_sha256"]
        assert sha(legacy) == item["legacy_core_sha256"] == LEGACY_CORE_SHA
        assert sha(framework) == item["framework_sha256"] == "849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"
        assert sha(S/item["three_column_core"]) == item["three_column_core_sha256"] == THREE_SHA
        load_io(item)
        restore_resume(item, out)
        retained, producers, original, _, expanded, tag, completed_review = prepare_sources(item, out, True)
        initial["expanded_job_sha256"] = sha(out/"public-actions-expanded-job.json")
        initial["actual_original_425_configuration_sha256"] = fingerprint(original.tag)
        initial["actual_projective_configuration"] = tag
        save(out/"public-actions-input.json", initial)
        config = out.parent/"job-config.json"
        save(config, expanded)
        command = [sys.executable, "-u", str(core), "--config", str(config),
            "--proof", str(proof), "--nested-proof", str(nested_proof),
            "--method", str(method), "--projective-method", str(projective_method),
            "--retained", str(retained), "--previous-three-columns", str(completed_root(out)), "--output", str(out),
            "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; completed candidate stages and latest Gamma CRT states retained."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__+": "+str(exception)
    core_receipt = out/"core-receipt.json"
    receipt = read(core_receipt) if core_receipt.exists() else {"complete": False}
    complete = code == 0 and receipt.get("complete") is True
    save(out/"run-receipt.json", {
        "result": RESULT, "p": 41, "complete": complete, "process_exit_code": code, "error": error,
        "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(core_receipt) if core_receipt.exists() else None,
        "projective_mode": PROJECTIVE_MODE,
        "actual_original_Mg_and_Gamma_computed": complete,
        "original_425_Mg_prime_arithmetic_recomputed": False,
        "independent_Mh_reconstructed_or_stored": False,
        "base_polar_preimages_computed": False, "eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    })
    output_manifest(out)
    print(json.dumps({"result": RESULT, "projective_mode": PROJECTIVE_MODE,
                      "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)




def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and path.name.endswith((".tmp", ".download", ".partial")):
            path.unlink()  # Only uncommitted atomic-write temporaries in this private output directory.
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    entries = [dict(file_spec(path), artifact=artifact, included_in_git=False)
               for path in sorted(out.iterdir()) if path.is_file()
               and path.name not in ("full-outputs-manifest.json", REFERENCE)]
    manifest = out/"full-outputs-manifest.json"
    save(manifest, {"result": RESULT, "files": entries,
        "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_rows_certificates_or_input_bundles_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": manifest.name,
        "manifest_sha256": sha(manifest), "manifest_bytes": manifest.stat().st_size,
        "file_count": len(entries), "full_outputs_artifact": artifact,
        "automatic_git_or_release_publication": False})




def verify(item, out):
    """Only IO, exact source bindings and certificate structure; never imports a math core."""
    initial = read(out/"public-actions-input.json")
    run, core = read(out/"run-receipt.json"), read(out/"core-receipt.json")
    assert initial["job"] == item
    assert initial["result"] == run["result"] == core["result"] == RESULT
    assert initial["core_sha256"] == core["source_sha256"] == item["core_sha256"]
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["proof_sha256"] == item["R813_proof_sha256"]
    assert initial["nested_proof_sha256"] == item["R817_proof_sha256"]
    assert initial["framework_sha256"] == core["framework_sha256"] == item["framework_sha256"]
    assert initial["method_sha256"] == item["R815_method_sha256"]
    assert run["source_commit"] == initial["source_commit"]
    assert run["complete"] is True and run["process_exit_code"] == 0
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert core["complete"] is True and core["certificate_sha256"] == sha(out/FINAL)
    for key in ("original_Mg_computed", "original_normal_derivation_connection_computed",
                "all_complete_polynomial_defining_identities_verified"):
        assert core[key] is True
    for key in ("independent_Mh_reconstructed_or_stored", "original_cusp_zero_ideal_computed",
                "original_function_DAG_polar_divisors_eta_or_height_computed"):
        assert core[key] is False
    assert initial["projective_mode"] == PROJECTIVE_MODE
    assert initial["legacy_core_sha256"] == item["legacy_core_sha256"] == LEGACY_CORE_SHA
    assert initial["projective_method_sha256"] == item["projective_method_sha256"]
    assert initial["io_helper_sha256"] == item["io_helper_sha256"] == IO_HELPER_SHA
    assert initial["three_column_io_helper_sha256"] == item["three_column_io_helper_sha256"] == THREE_IO_SHA
    assert initial["frozen_three_column_core_sha256"] == core["frozen_three_column_core_sha256"] == THREE_SHA
    load_io(item)
    retained, producers, original, selection, expanded, tag, review = prepare_sources(item, out, False, record=False)
    count = 3037
    assert initial["expanded_job_sha256"] == sha(out/"public-actions-expanded-job.json")
    assert initial["actual_projective_configuration"] == tag
    assert initial["actual_original_425_configuration_sha256"] == fingerprint(original.tag)
    target_tags = expected_target_configurations(tag, producers)
    certificate = read(out/FINAL)
    assert certificate["result"] == RESULT and certificate["complete"] is True
    assert certificate["configuration"] == tag
    assert certificate["projective_mode"] == PROJECTIVE_MODE
    assert certificate["projective_method_sha256"] == item["projective_method_sha256"]
    assert certificate["legacy_R815_core_sha256"] == LEGACY_CORE_SHA
    assert certificate["source_original_425_identity"] == source_identity(original.item)
    assert certificate["source_original_current"] == plain(original.item["current"])
    assert certificate["source_original_latest_receipt"] == plain(original.item["latest_CRT_receipt"])
    assert certificate["original_425_prime_arithmetic_recomputed"] is False
    assert certificate["completed_original_scalar_scan_reused"] == completed_source_identity(item["completed_three_columns_source"])
    assert certificate["completed_three_columns_source"] == completed_source_identity(item["completed_three_columns_source"])
    assert certificate["exact_three_known_columns_source_group"] == "completed_three_columns_source"
    assert certificate["frozen_three_column_core_sha256"] == THREE_SHA
    assert certificate["known_column_indices"] == [0, 1, 271]
    assert certificate["known_column_coefficient_counts"] == [690, 962, 1234]
    assert certificate["all2886_original_current_congruences_verified"] is True
    assert certificate["external_old_W_and_Krylov_stages_preserve_original_configuration"] is True
    assert certificate["completed_scope"] == "original_normal_derivation_operators"
    assert certificate["requested_targets"] == ["g", "Gamma"]
    assert certificate["target_configurations"] == target_tags
    assert certificate["normal_affine_basis_rank"] == 272 and certificate["normal_basis_degrees"] == EPS
    assert certificate["coefficient_field_basis"] == FIELD_BASIS
    assert certificate["actual_input_producers"] == {label: identity(producers[label].item) for label in LABELS}
    assert certificate["shared_point_mathematical_identity"] == shared_cache_identity(producers)
    assert certificate["source_R813_exact_coordinates"] == producers["R813"].certificate["exact_coordinate_stage"]
    assert certificate["source_R813_normal_interface"] == producers["R813"].certificate["normal_vector_interface"]
    for key in ("original_Mg_computed", "original_normal_derivation_connection_computed",
                "original_Mh_identified_by_nested_commutator_and_original_first_column",
                "all_weighted_supports_and_original_column_constraints_verified",
                "all_complete_polynomial_defining_identities_verified",
                "Gamma_nonhomogeneous_identity_with_actual_Mh_certified",
                "normal_integral_basis_preserved", "all_original_scalar_and_field_normalizations_preserved"):
        assert certificate[key] is True
    for key in ("independent_Mh_reconstructed_or_stored",
                "old_Fourier_Wronskian_S3_Dixon_or_primitive_results_recomputed",
                "characteristic_zero_Krylov_matrix_or_inverse_computed",
                "original_cusp_zero_ideal_computed",
                "original_function_DAG_polar_divisors_eta_or_height_computed"):
        assert certificate[key] is False
    assert certificate["Mg_exact_commutator_points"] == certificate["Gamma_exact_nested_commutator_points"] == list(range(7))
    manifest_spec = certificate["stage_manifest"]
    assert file_spec(out/manifest_spec["file"]) == manifest_spec
    inventory = read(out/manifest_spec["file"])
    assert inventory["configuration"] == tag and inventory["complete"] is True
    entries = {entry["file"]: entry for entry in inventory["files"]}
    assert len(entries) == len(inventory["files"])
    for name, entry in entries.items():
        check_spec(entry)
        assert file_spec(out/name) == entry
        value = read(out/name)
        assert value["configuration"] == tag and value["complete"] is True
        if "target_configuration" in value:
            target = value["target"]
            assert target in target_tags and value["target_configuration"] == target_tags[target]
            assert value["target_configuration_sha256"] == fingerprint(target_tags[target])
        if name.endswith("-Krylov-inverse.json.gz"):
            assert value["shared_point_mathematical_identity"] == certificate["shared_point_mathematical_identity"]
            assert value["external_consumer_must_preserve_original_R815_stage_identity"] is True
        for key in ("source_original_M_w", "source_original_primitive_matrix"):
            if key in value:
                assert plain(value[key]) == original.files[OLD_W]
        if "discarded_candidate_file_history" in value:
            assert value["no_exact_characteristic_zero_multiplier_claimed"] is True
            if value["target"] == "g":
                assert value["only_inactive_rejected_large_candidate_blocks_pruned"] is True
                assert value["original_source_current_or_Krylov_cache_deleted"] is False
                stem = value["candidate_id"]
                assert name == stem+"-rejected.json.gz" and stem.startswith("R815-projective-g-candidate-")
            else:
                assert value["target"] == "Gamma" and value["field_component"] == 0
                stem = "R815-target-Gamma-component-00-attempt-"+str(value["attempt_prime_count"]).zfill(6)
                assert name == stem+"-rejected.json.gz"
            for retired in value["discarded_candidate_file_history"]:
                check_spec(retired)
                assert retired["file"].startswith(stem+"-reconstructed-rows-") or (
                    value["target"] == "Gamma" and retired["file"] == stem+"-candidate-index.json.gz")
                if (out/retired["file"]).exists():
                    assert file_spec(out/retired["file"]) == plain(retired)
    checkpoint_specs = inventory.get("current_checkpoints", certificate.get("current_checkpoints", []))
    checkpoints = {entry["file"]: entry for entry in checkpoint_specs}
    assert len(checkpoints) == len(checkpoint_specs)
    for name, entry in checkpoints.items():
        check_spec(entry)
        assert name not in entries and name.startswith("R815-") and name.endswith(".json.gz")
        assert file_spec(out/name) == plain(entry)
        value = read(out/name)
        assert value["configuration"] == tag and value["complete"] is False
    expected_names = {path.name for path in out.glob("R815-*.json.gz")
                      if not path.name.startswith("R815-stage-manifest-")}
    assert set(entries) | set(checkpoints) == expected_names
    assert not list(out.glob("R815-*-CRT-current.json.gz"))
    assert not list(out.glob("R815-target-h-*-CRT-*.json.gz"))

    def referenced(entry, target=None, original_source=False):
        if original_source:
            assert entry["file"] in original.names
            assert plain(entry) == original.files[entry["file"]]
            data = original.stage(entry, target)
            if target is not None:
                assert data["target_configuration"] == original.old_targets[target]
            return data
        assert entries[entry["file"]] == plain(entry)
        data = read(out/entry["file"])
        if target is not None:
            assert data["target_configuration"] == target_tags[target]
        return data

    audit = referenced(certificate["original_425_source_audit"])
    assert audit["source_original_425_identity"] == source_identity(original.item)
    assert audit["source_original_current"] == plain(original.item["current"])
    assert audit["source_original_latest_receipt"] == plain(original.item["latest_CRT_receipt"])
    assert audit["completed_three_columns_source"] == completed_source_identity(item["completed_three_columns_source"])
    assert audit["fixed_actual_failure_indices"] == list(PROBE_INDICES)
    assert audit["actual_distinct_old_rejections"] == 49
    assert audit["all2886_congruences_imported_from_complete_source_not_recomputed"] is True
    assert audit["known_columns_and_joint_content_not_recomputed"] is True
    assert audit["original_scalar_RR_and_old_three_dimensional_LLL_recomputed"] is False
    known_spec = plain(certificate["exact_three_known_columns_input"])
    assert known_spec == plain(item["completed_three_columns_source"]["known_columns"])
    known = read(completed_root(out)/known_spec["file"])
    lattice = referenced(certificate["complete_nine_dimensional_lattice"])
    assert lattice["dimension"] == 9 and lattice["probe_indices"] == list(PROBE_INDICES)
    assert lattice["source_completed_source_audit"] == certificate["original_425_source_audit"]
    assert lattice["source_original_current"] == plain(original.item["current"])
    assert lattice["source_exact_three_known_columns"] == known_spec
    assert lattice["full_basis_change_equality_verified"] is True
    assert lattice["exact_basis_change_determinant"] in (-1,1)
    assert lattice["full_congruence_lattice_not_a_sublattice"] is True
    assert lattice["number_of_new_LLL_calls"] == 1
    for key in ("actual_integer_lattice_rows", "actual_LLL_rows", "exact_integral_basis_change"):
        assert len(lattice[key]) == 9 and all(len(row)==9 for row in lattice[key])
    assert len(lattice["candidates"]) == 9
    raw = referenced(lattice["source_raw_LLL"])
    assert raw["actual_returned_LLL_rows"] == lattice["actual_LLL_rows"]
    assert raw["actual_integer_lattice_rows"] == lattice["actual_integer_lattice_rows"]
    assert raw["complete_basis_or_multiplier_claimed_by_this_raw_stage"] is False
    assert certificate["resume_state"]["file"] in checkpoints
    assert plain(certificate["resume_state"]) == plain(checkpoints[certificate["resume_state"]["file"]])
    state = read(out/certificate["resume_state"]["file"])
    assert state["complete_nine_dimensional_lattice"] == certificate["complete_nine_dimensional_lattice"]
    assert state["accepted_multiplier_index"] == certificate["operator_indices"]["g"]
    assert len(state["row_decisions"]) == state["next_LLL_row"]
    for ordinal, entry in enumerate(state["row_decisions"]):
        decision = referenced(entry)
        assert decision["LLL_row"] == ordinal and decision["D"] == lattice["candidates"][ordinal]["D"]
        assert decision["source_complete_lattice"] == certificate["complete_nine_dimensional_lattice"]
        if decision["outcome"] == "duplicate_in_new_nine_rows":
            previous = referenced(decision["witness"])
            assert previous["D"] == decision["D"] and previous["LLL_row"] < ordinal
        elif decision["outcome"] == "same_completed_candidate_rejected":
            witness = referenced(decision["witness"], "g")
            assert witness["D"] == decision["D"]
        elif decision["outcome"] == "new_exact_candidate_rejected":
            assert referenced(decision["witness"], "g")["no_exact_characteristic_zero_multiplier_claimed"] is True
        elif decision["outcome"] == "original_multiplier_certified":
            assert decision["certified_multiplier_index"] == certificate["operator_indices"]["g"]
        else:
            assert decision["outcome"] == "search_filter" and decision["search_rejection_reason"] is not None
    for name in entries:
        if name.startswith("R815-eight-probe-g-candidate-") and name.endswith("-previous-rejection.json.gz"):
            value = referenced(entries[name], "g")
            assert value["completed_three_columns_source"] == completed_source_identity(item["completed_three_columns_source"])
            assert value["same_integer_denominator_and_same_complete_candidate"] is True
            assert value["old_nonzero_residual_recomputed"] is False and value["old_source_relabelled"] is False
            assert value["frozen_candidate_constructor_sha256"] == THREE_SHA
            for key in ("source_previous_definition", "source_previous_failed_exact_entry", "source_previous_rejection"):
                entry = plain(value[key])
                assert entry == plain(item["completed_three_columns_source"]["files"][entry["file"]])
            definition = read(completed_root(out)/value["source_previous_definition"]["file"])
            assert definition["D"] == value["D"]
            assert definition["source_exact_three_known_columns"] == known_spec
    assert certificate["baseline_previous_rejection"]["file"] in entries
    assert plain(certificate["baseline_previous_rejection"]) == plain(entries[certificate["baseline_previous_rejection"]["file"]])
    row_ranges = [(first, min(first+16, 272)) for first in range(0, 272, 16)]
    assert certificate["original_vector_input_source_group"] == "R815"
    vector_specs = certificate["original_vector_inputs"]
    for column, target in enumerate(("g", "h")):
        assert plain(vector_specs[target]) == original.files[OLD_VECTOR[target]]
        vector = referenced(vector_specs[target], target, original_source=True)
        assert vector["source_R813_column_index"] == column
        assert vector["source_R813_exact_coordinates"] == certificate["source_R813_exact_coordinates"]
        assert vector["source_R813_normal_interface"] == certificate["source_R813_normal_interface"]
        assert vector["regular_degree_bound"] == 3 and vector["normal_affine_basis_rank"] == 272
        assert vector["original_rational_scale_applied_exactly_once"] is True
        assert vector["no_extra_82_power_or_removed_content_reinserted"] is True
        assert vector["original_D0_qY_multiplier"] == ["1", "82"]
        assert vector["exactly_zero_component"] is False
        assert len(vector["integer_vector_coefficients_low_to_high"]) == 4
        assert all(len(row) == 272 for row in vector["integer_vector_coefficients_low_to_high"])
        assert int(vector["common_positive_denominator"]) > 0
    indexes = certificate["operator_indices"]
    assert set(indexes) == {"g", "Gamma"}
    g_index = referenced(indexes["g"], "g")
    gamma_index = referenced(indexes["Gamma"], "Gamma")
    prime_counts = {}
    for target, index in (("g", g_index), ("Gamma", gamma_index)):
        assert index["target"] == target and index["field_component"] == 0
        assert index["coefficient_field_basis"] == FIELD_BASIS
        assert index["weighted_degree_bound_verified"] is True
        degree = 3 if target == "g" else 2
        assert index["regular_degree_bound"] == degree
        candidate = referenced(index["source_candidate"], target)
        assert candidate["matrix_row_blocks"] == index["matrix_row_blocks_tau"]
        assert candidate["source_original_vector"] == index["source_original_vector"]
        assert len(index["matrix_row_blocks_tau"]) == len(index["matrix_row_blocks_sigma"]) == len(row_ranges)
        for tau_spec, sigma_spec, (first, stop) in zip(
                index["matrix_row_blocks_tau"], index["matrix_row_blocks_sigma"], row_ranges):
            coefficient_count = sum(degree+1+EPS[a]-EPS[b] for b in range(first, stop) for a in range(272))
            for entry in (tau_spec, sigma_spec):
                block = referenced(entry, target)
                assert block["target"] == target and block["field_component"] == 0
                assert (block["row_first"], block["row_stop"]) == (first, stop)
                assert block["regular_degree_bound"] == degree
                assert int(block["common_positive_denominator"]) > 0
                assert len(block["coefficient_numerators"]) == coefficient_count
            sigma = referenced(sigma_spec, target)
            assert sigma["source_tau_matrix_row_block"] == tau_spec
            assert sigma["source_exact_candidate"] == index["source_candidate"]
            if target == "g":
                assert sigma["every_transition_exponent_nonnegative"] is True
                assert sigma["transported_original_first_column_verified_coefficientwise"] is True
                assert sigma["common_homogeneous_factor_in_pair"] == "t^3"
                assert sigma["original_function_or_section_rescaled_by_unit"] is False
            else:
                assert sigma["source_exact_Mg"] == indexes["g"]
                assert sigma["all_negative_power_coefficients_cancelled_exactly"] is True
                assert sigma["original_unit_column_zero_verified"] is True
                assert sigma["regular_derivation_relation"] == "delta_sigma=t*delta_tau"
                assert sigma["homogeneous_matrix_reversal_used_as_connection"] is False
        if target == "g":
            assert index["source_original_vector"] == vector_specs["g"]
            assert index["operator_kind"] == "multiplication"
            assert index["zero_component_proved_from_exact_original_vector"] is False
            assert index["original_first_column_verified_coefficientwise"] is True
            assert index["complete_polynomial_commutator_identity_verified"] is True
            assert index["commutator_maximum_degree"] == 6
            assert index["exact_commutator_points"] == list(range(7))
            assert index["primitive_cyclic_uniqueness_identifies_true_regular_multiplier"] is True
            first = referenced(index["exact_first_column_certificate"], target)
            assert first["original_first_column_verified_coefficientwise"] is True
            assert first["original_second_column_Wvg_verified_coefficientwise"] is True
            assert first["original_column271_WWvg_verified_coefficientwise"] is True
            assert first["source_exact_three_known_columns"] == known_spec
            assert index["original_second_column_Wvg_verified_coefficientwise"] is True
            assert index["original_column271_WWvg_verified_coefficientwise"] is True
            assert index["source_exact_three_known_columns"] == known_spec
        else:
            assert index["source_original_h_vector"] == vector_specs["h"]
            assert index["operator_kind"] == "normal_derivation_connection"
            assert index["source_exact_Mg"] == indexes["g"]
            assert index["weighted_degree_shift"] == 2
            assert index["Gamma_zero_first_column_and_H_original_first_column_verified"] is True
            assert index["complete_nested_commutator_identity_verified"] is True
            assert index["nested_commutator_maximum_degree"] == 6
            assert index["exact_nested_commutator_points"] == list(range(7))
            assert index["cyclic_uniqueness_identifies_H_with_actual_Mh"] is True
            assert index["original_nonhomogeneous_connection_identity_therefore_verified"] is True
            assert index["independent_Mh_reconstructed_or_stored"] is False
            assert index["sigma_regular_connection_verified_with_original_derivation_change"] is True
            equation = referenced(index["source_original_vector"], target)
            assert equation["source_original_g_vector"] == vector_specs["g"]
            assert equation["source_original_h_vector"] == vector_specs["h"]
            assert equation["zero_vector_shortcut_allowed"] is False
            first = referenced(index["exact_original_column_certificate"], target)
            assert first["actual_w0_original_M2_is_e2"] is True
            assert first["actual_original_W_first_column_is_constant_e1"] is True
            assert first["Gamma_e0_zero_verified_coefficientwise"] is True
            assert first["Gamma_e1_equals_original_h_verified_coefficientwise"] is True
            assert first["H_e0_equals_original_h_verified_coefficientwise"] is True
            assert first["source_original_h_vector"] == vector_specs["h"]
            assert first["source_exact_Mg"] == indexes["g"]
        assert first["source_candidate"] == index["source_candidate"]
        assert index["source_R806_cyclic_witness"] == certificate["source_R806_cyclic_witness"]
        points = index["exact_full_matrix_point_certificates"]
        assert len(points) == 7
        for point, entry in enumerate(points):
            data = referenced(entry, target)
            assert data["source_candidate"] == index["source_candidate"]
            assert data["exact_integer_point"] == point and data["full_matrix_shape"] == [272, 272]
            assert data["Krylov_invertibility_not_required_at_exact_verification_point"] is True
            assert data["all_exact_commutator_entries_zero" if target == "g" else "all_exact_nested_commutator_entries_zero"] is True
            blocks = data["full_row_block_certificates"]
            assert len(blocks) == len(row_ranges)
            for block_spec, (first, stop) in zip(blocks, row_ranges):
                block = referenced(block_spec, target)
                assert block["source_candidate"] == index["source_candidate"]
                assert block["exact_integer_point"] == point and block["column_count"] == 272
                assert (block["row_first"], block["row_stop"]) == (first, stop)
                if target == "g":
                    assert block["all_exact_integer_commutator_entries_zero"] is True
                    assert block["both_products_computed_over_Z_after_exact_denominator_clearing"] is True
                else:
                    assert block["all_exact_integer_nested_commutator_entries_zero"] is True
                    assert block["source_exact_Mg"] == indexes["g"]
                    assert block["source_original_h_vector"] == vector_specs["h"]
                    assert block["H_is_only_evaluated_at_this_point_not_reconstructed_as_a_polynomial_table"] is True
        history = referenced(index["latest_CRT_history_receipt"], target)
        assert history["current_full_CRT_checkpoint"] == candidate["source_CRT_checkpoint"]
        assert history["prime_count"] == index["actual_CRT_prime_count"]
        if target == "g":
            assert history["original_external_CRT_source"] == source_identity(original.item)
            assert history["original_external_CRT_receipt"] == plain(original.item["latest_CRT_receipt"])
            assert history["original_external_CRT_configuration_sha256"] == fingerprint(original.tag)
            assert history["original_external_current_preserves_its_own_configuration"] is True
            assert history["original_425_prime_arithmetic_recomputed"] is False
            assert history["source_checkpoint_or_source_temporary_files_deleted"] is False
            assert history["receipt_is_a_new_source_import_record_not_a_relabelled_old_stage"] is True
        else:
            assert history["large_vector_or_matrix_embedded"] is False
            assert history["full_temporary_images_discarded_only_after_CRT_commit"] is True
        prime_counts[target] = index["actual_CRT_prime_count"]
    assert certificate["actual_CRT_prime_counts"] == prime_counts
    assert prime_counts["g"] == 425
    assert g_index["original_external_CRT_source"]
    assert "projective_candidate_id" in g_index
    assert certificate["sigma_base_variable_derivative"] == {
        "matrix_blocks": g_index["matrix_row_blocks_sigma"], "rational_scalar": [-1, 1],
        "identity": "M_(delta_sigma t)=-t^3*D*Mg(1/t)*D^-1"}
    full = read(out/"full-outputs-manifest.json")
    assert full["result"] == RESULT
    names = set()
    for entry in full["files"]:
        check_spec(entry)
        assert entry["file"] not in names and file_spec(out/entry["file"]) == plain(entry)
        names.add(entry["file"])
    assert names == {path.name for path in out.iterdir() if path.is_file()
                     and path.name not in ("full-outputs-manifest.json", REFERENCE)}
    reference = read(out/REFERENCE)
    assert reference["manifest_sha256"] == sha(out/"full-outputs-manifest.json")
    assert reference["file_count"] == len(names)
    print(json.dumps({"R815_VERIFY_REVIEW": {
        "complete": True, "selected_input_files_verified": count, "complete_stage_files_verified": len(entries),
        "actual_CRT_prime_counts": prime_counts, "Mg_exact_points": list(range(7)),
        "Gamma_nested_exact_points": list(range(7)), "normal_affine_basis_rank": 272,
        "actual_core_seconds": certificate["seconds"], "independent_Mh_reconstructed_or_stored": False,
        "projective_mode": PROJECTIVE_MODE, "original_CRT_prime_count_reused": 425,
        "original_425_current_sha256": original.item["current"]["sha256"],
        "actual_original_shared_point_count": len(original.point_names),
        "original_cusp_zero_ideal_computed": False}}), flush=True)
    return 0




def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "verify"])
    args = parser.parse_args()
    out = Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if args.mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    return verify(read(out/"public-actions-input.json")["job"], out)


if __name__ == "__main__":
    sys.exit(main())
