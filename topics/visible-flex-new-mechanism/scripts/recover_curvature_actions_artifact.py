#!/usr/bin/env python3
"""Recover one completed public Actions artifact without redoing any research.

Network, ZIP validation and extraction run only in the authorized repository's
GitHub Actions. GITHUB_TOKEN is read from the environment and sent only to
api.github.com; archive redirect requests never inherit authorization.
Scientific JSON bytes are copied verbatim, never reserialized.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import stat
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

REPOSITORY = 'Rogerhu12/math-research-public'
ORIGINAL_RUN = 43645177423
ORIGINAL_JOB = 132601261692
ORIGINAL_ARTIFACT = 14133787467
ORIGINAL_SOURCE = '2f1b809c0b0abb7a26303d36940edc203815f872'
ORIGINAL_ARCHIVE_SHA256 = 'ba8737026d71a111a685eea7056614755335f95fc8c7eff5262f2dba46dbc133'
ORIGINAL_ARCHIVE_BYTES = 823379
ORIGINAL_FILE_COUNT = 6
ARTIFACT_NAME = 'visible-new-mechanism-continuation-curvature_epigraph_exchange-43645177423-1'
FULL_NAME = 'curvature-epigraph-exchange-audit.json'
BRIEF_NAME = 'curvature-epigraph-exchange-audit-brief.json'
SUMMARY_NAME = 'curvature-epigraph-exchange-audit-summary.json'
DEVELOPMENT_NAME = 'curvature-exchange-development.json'
REQUIRED_FILES = (FULL_NAME, BRIEF_NAME, SUMMARY_NAME, DEVELOPMENT_NAME)
RECOVERED_FILENAMES = {
    'pre-research-pull.json': 'original-pre-research-pull.json',
    'publication-status.json': 'original-publication-status.json',
}
EXPECTED_SOURCES = {
    'frame_curvature_epigraph_exchange.py': '8c26353df012ca61f37149b2e2ab52acaec4ca22fde68017261c0bd68992ebf5',
    'frame_curvature_epigraph_exchange_audit.py': '7162b7c56bb865591316b1ca576c7b0929d55619353567ccd4f3df789543802a',
}
MAX_JSON_BYTES = 64 * 1024 * 1024
MAX_TOTAL_JSON_BYTES = 256 * 1024 * 1024
MAX_METADATA_BYTES = 2 * 1024 * 1024


class RecoveryError(RuntimeError):
    pass


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def safe_json(data):
    def bad_constant(value):
        raise RecoveryError('nonfinite JSON constant in preserved artifact: '+value)
    try:
        return json.loads(data, parse_constant=bad_constant)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise RecoveryError('an artifact .json file is not valid UTF-8 JSON') from error


def public_actions_guard():
    if os.environ.get('GITHUB_ACTIONS', '').lower() != 'true':
        raise RecoveryError('artifact recovery is restricted to actual GitHub Actions')
    if os.environ.get('GITHUB_REPOSITORY') != REPOSITORY:
        raise RecoveryError('artifact recovery is restricted to the exact authorized public repository')
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        raise RecoveryError('GITHUB_TOKEN must be supplied only through the environment')
    return token


def validate_url(url, *, api_only=False):
    parsed = urllib.parse.urlsplit(url)
    if (parsed.scheme != 'https' or parsed.username is not None or parsed.password is not None
            or parsed.port not in (None, 443) or not parsed.hostname or parsed.fragment):
        raise RecoveryError('unsafe download URL rejected')
    host = parsed.hostname.lower()
    if api_only and (host != 'api.github.com' or not parsed.path.startswith('/repos/'+REPOSITORY+'/actions/')):
        raise RecoveryError('authenticated request is not this repository Actions API')
    if not api_only:
        allowed = (host in ['api.github.com','github.com']
            or host.endswith('.blob.core.windows.net')
            or host.endswith('.actions.githubusercontent.com')
            or host.endswith('.githubusercontent.com')
            or host.endswith('.amazonaws.com'))
        if not allowed:
            raise RecoveryError('archive redirect left the permitted GitHub artifact storage hosts')
    return parsed


def open_no_redirect(url, headers):
    opener = urllib.request.build_opener(NoRedirect())
    request = urllib.request.Request(url, headers=headers, method='GET')
    try:
        return opener.open(request, timeout=60)
    except urllib.error.HTTPError as error:
        if error.code in (301,302,303,307,308):
            return error
        code = int(error.code)
        error.close()
        raise RecoveryError('GitHub artifact request returned HTTP status '+str(code)) from None
    except urllib.error.URLError:
        raise RecoveryError('GitHub artifact network request failed') from None


def api_json(path, token):
    url = 'https://api.github.com/repos/'+REPOSITORY+'/actions/'+path
    validate_url(url, api_only=True)
    headers = {'Accept':'application/vnd.github+json','Authorization':'Bearer '+token,
        'X-GitHub-Api-Version':'2022-11-28','User-Agent':'visible-flex-public-artifact-recovery'}
    with open_no_redirect(url, headers) as response:
        if response.status != 200:
            raise RecoveryError('unexpected redirect or non-200 response for metadata')
        raw = response.read(MAX_METADATA_BYTES+1)
    if len(raw)>MAX_METADATA_BYTES:
        raise RecoveryError('artifact metadata exceeds declared bound')
    value = safe_json(raw)
    if not isinstance(value,dict):
        raise RecoveryError('artifact metadata must be a JSON object')
    return value,sha256(raw)


def download_archive(token):
    url = 'https://api.github.com/repos/'+REPOSITORY+'/actions/artifacts/'+str(ORIGINAL_ARTIFACT)+'/zip'
    redirect_hosts = []
    for step in range(8):
        parsed = validate_url(url, api_only=(step==0))
        redirect_hosts.append(parsed.hostname)
        headers = {'User-Agent':'visible-flex-public-artifact-recovery','Accept':'application/octet-stream'}
        if step==0:
            headers.update(Authorization='Bearer '+token, Accept='application/vnd.github+json',
                **{'X-GitHub-Api-Version':'2022-11-28'})
        # No authorization header is added after any redirect, even if a
        # later redirect happens to return to api.github.com.
        with open_no_redirect(url,headers) as response:
            if response.status in (301,302,303,307,308):
                location = response.headers.get('Location')
                if not location:
                    raise RecoveryError('archive redirect lacks a Location')
                url = urllib.parse.urljoin(url,location)
                validate_url(url)
                continue
            if response.status != 200:
                raise RecoveryError('archive download did not return HTTP 200')
            data = response.read(ORIGINAL_ARCHIVE_BYTES+1)
            if len(data)!=ORIGINAL_ARCHIVE_BYTES:
                raise RecoveryError('downloaded archive byte count differs from the original official artifact')
        if sha256(data)!=ORIGINAL_ARCHIVE_SHA256:
            raise RecoveryError('downloaded archive SHA256 differs from the original official artifact')
        return data,redirect_hosts
    raise RecoveryError('too many archive download redirects')


def atomic_original_bytes(path, data):
    if path.is_symlink():
        raise RecoveryError('refusing to replace a symlink in the recovery output')
    if path.exists():
        if not path.is_file() or path.read_bytes()!=data:
            raise RecoveryError('recovery output collision has different original bytes: '+path.name)
        return
    fd,name=tempfile.mkstemp(prefix='.recover-',suffix='.tmp',dir=str(path.parent))
    try:
        with os.fdopen(fd,'wb') as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name,path)
    finally:
        if os.path.exists(name):
            os.unlink(name)
    if path.read_bytes()!=data:
        raise RecoveryError('original-byte write verification failed: '+path.name)


def write_receipt(path, record):
    raw=(json.dumps(record,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode('utf-8')
    fd,name=tempfile.mkstemp(prefix='.receipt-',suffix='.tmp',dir=str(path.parent))
    try:
        with os.fdopen(fd,'wb') as handle:
            handle.write(raw)
        os.replace(name,path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def verified_json_members(archive):
    try:
        zf=zipfile.ZipFile(io.BytesIO(archive),'r')
    except zipfile.BadZipFile:
        raise RecoveryError('verified artifact bytes are not a readable ZIP') from None
    files=[]
    names=set()
    total=0
    with zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            name=info.filename
            rel=PurePosixPath(name)
            mode=(info.external_attr>>16)&0xFFFF
            if ('\\' in name or '\x00' in name or rel.is_absolute() or '..' in rel.parts
                    or len(rel.parts)!=1 or rel.suffix.lower()!='.json' or name in names
                    or name in ['artifact-recovery-receipt.json','artifact-recovery-failure.json']
                    or stat.S_ISLNK(mode) or (stat.S_IFMT(mode) not in (0,stat.S_IFREG))
                    or info.flag_bits&1):
                raise RecoveryError('unsafe, duplicate, encrypted, non-JSON or non-flat artifact member')
            if info.compress_type not in (zipfile.ZIP_STORED,zipfile.ZIP_DEFLATED):
                raise RecoveryError('unexpected artifact ZIP compression method')
            if info.file_size<0 or info.file_size>MAX_JSON_BYTES:
                raise RecoveryError('JSON member exceeds declared decoded bound')
            total+=info.file_size
            if total>MAX_TOTAL_JSON_BYTES:
                raise RecoveryError('artifact decoded total exceeds declared bound')
            names.add(name)
            try:
                with zf.open(info,'r') as handle:
                    data=handle.read(MAX_JSON_BYTES+1)
            except (zipfile.BadZipFile, RuntimeError):
                raise RecoveryError('ZIP member CRC or decoding validation failed') from None
            if len(data)!=info.file_size:
                raise RecoveryError('artifact JSON decoded size differs from ZIP directory')
            value=safe_json(data)
            files.append((name,data,value,{'archive_member':name,'raw_bytes':len(data),
                'raw_sha256':sha256(data),'zip_compressed_bytes':info.compress_size,
                'zip_crc32_hex':format(info.CRC,'08x')}))
    if len(files)!=ORIGINAL_FILE_COUNT or not set(REQUIRED_FILES)<=names:
        raise RecoveryError('original six JSON outputs or required scientific reports are missing')
    return files


def verify_scientific_bindings(files):
    byname={name:(raw,value) for name,raw,value,meta in files}
    raw,full=byname[FULL_NAME]
    if not isinstance(full,dict) or full.get('github_sha')!=ORIGINAL_SOURCE or str(full.get('github_run_id'))!=str(ORIGINAL_RUN):
        raise RecoveryError('complete scientific report does not match the original source/run')
    if full.get('artificial_inputs_only') is not False:
        raise RecoveryError('the preserved complete report is not the requested actual report')
    dev=byname[DEVELOPMENT_NAME][1]
    for document in [full,dev]:
        if not isinstance(document,dict):
            raise RecoveryError('complete report and development output must be JSON objects')
        for name,expected in EXPECTED_SOURCES.items():
            if document.get('source_files_sha256',{}).get(name)!=expected:
                raise RecoveryError('original calculation implementation hash differs: '+name)
    brief=byname[BRIEF_NAME][1]
    summary=byname[SUMMARY_NAME][1]
    if (not isinstance(brief,dict) or brief.get('complete_report',{}).get('raw_sha256')!=sha256(raw)
            or brief.get('complete_report',{}).get('raw_bytes')!=len(raw)
            or brief.get('complete_report',{}).get('filename')!=FULL_NAME):
        raise RecoveryError('preserved semantic brief does not bind the original full-report bytes')
    if (not isinstance(summary,dict) or summary.get('full_report',{}).get('sha256')!=sha256(raw)
            or summary.get('full_report',{}).get('bytes')!=len(raw)):
        raise RecoveryError('preserved original summary does not bind the original full-report bytes')
    return {'full_report_raw_bytes':len(raw),'full_report_raw_sha256':sha256(raw),
        'original_full_report_status':full.get('status'),
        'original_development_passed':dev.get('passed'),
        'original_development_status_not_reinterpreted':True,
        'original_report_and_both_summaries_bound_verbatim':True,
        'original_two_calculation_sources_sha256':dict(EXPECTED_SOURCES)}


def recover(out_dir):
    started=time.monotonic()
    token=public_actions_guard()
    out_dir=Path(out_dir)
    if out_dir.is_symlink():
        raise RecoveryError('output directory must not itself be a symlink')
    out_dir.mkdir(parents=True,exist_ok=True)
    if not out_dir.is_dir():
        raise RecoveryError('recovery output directory is invalid')
    record={'schema':'public-actions-original-curvature-artifact-recovery-v1','status':'started',
        'original_repository':REPOSITORY,'original_run_id':ORIGINAL_RUN,'original_job_id':ORIGINAL_JOB,
        'original_source_commit':ORIGINAL_SOURCE,'original_artifact_id':ORIGINAL_ARTIFACT,
        'original_artifact_name':ARTIFACT_NAME,
        'original_archive_sha256':ORIGINAL_ARCHIVE_SHA256,
        'original_archive_bytes':ORIGINAL_ARCHIVE_BYTES,
        'original_publication_failed':True,
        'original_publication_failure':'publisher rejected the raw complete JSON before gzip because its diagnostic byte limit was exceeded',
        'original_research_step_completed_successfully':True,
        'original_job_log_url':'https://github.com/'+REPOSITORY+'/actions/runs/'+str(ORIGINAL_RUN)+'/job/'+str(ORIGINAL_JOB),
        'recovery_workflow_run_id':os.environ.get('GITHUB_RUN_ID'),
        'recovery_workflow_source_commit':os.environ.get('GITHUB_SHA'),
        'recovery_script_sha256':sha256(Path(__file__).read_bytes()),
        'research_geometry_evaluated':False,'optimizer_called':False,
        'scientific_JSON_reserialized':False,'token_only_from_environment':True,
        'archive_redirects_never_receive_authorization':True,
        'presigned_archive_URLs_not_recorded':True,'files':[]}
    phase='original-run-metadata'
    try:
        run,run_metadata_sha=api_json('runs/'+str(ORIGINAL_RUN),token)
        if (run.get('id')!=ORIGINAL_RUN or run.get('head_sha')!=ORIGINAL_SOURCE
                or run.get('repository',{}).get('full_name')!=REPOSITORY
                or run.get('status')!='completed'):
            raise RecoveryError('original run metadata does not match the requested completed source')
        record['original_run_metadata']={key:run.get(key) for key in ['id','head_sha','run_attempt','status','conclusion','html_url']}
        record['original_run_metadata_response_sha256']=run_metadata_sha
        phase='original-artifact-metadata'
        artifact,artifact_metadata_sha=api_json('artifacts/'+str(ORIGINAL_ARTIFACT),token)
        origin=artifact.get('workflow_run',{})
        if (artifact.get('id')!=ORIGINAL_ARTIFACT or artifact.get('name')!=ARTIFACT_NAME
                or artifact.get('expired') is not False
                or artifact.get('size_in_bytes')!=ORIGINAL_ARCHIVE_BYTES
                or origin.get('id')!=ORIGINAL_RUN or origin.get('head_sha')!=ORIGINAL_SOURCE):
            raise RecoveryError('artifact metadata does not bind the requested original run/source/size')
        digest=artifact.get('digest')
        if digest is not None and digest!='sha256:'+ORIGINAL_ARCHIVE_SHA256:
            raise RecoveryError('official artifact digest differs from the known original archive')
        record['original_artifact_metadata']={key:artifact.get(key) for key in ['id','name','size_in_bytes','digest','created_at','expires_at','expired','workflow_run']}
        record['original_artifact_metadata_response_sha256']=artifact_metadata_sha
        phase='archive-download-with-no-cross-host-token'
        archive,hosts=download_archive(token)
        record['download_redirect_hostnames']=hosts
        record['downloaded_archive_sha256']=sha256(archive)
        record['downloaded_archive_bytes']=len(archive)
        phase='safe-JSON-only-ZIP-validation'
        files=verified_json_members(archive)
        phase='original-scientific-source-and-summary-bindings'
        record['scientific_bindings']=verify_scientific_bindings(files)
        phase='verbatim-original-JSON-writes'
        for name,data,value,meta in files:
            recovered_name=RECOVERED_FILENAMES.get(name,name)
            atomic_original_bytes(out_dir/recovered_name,data)
            meta=dict(meta,recovered_filename=recovered_name,original_bytes_preserved=True,
                operational_receipt_renamed_to_avoid_current_run_collision=(recovered_name!=name))
            if isinstance(value,dict):
                meta['original_schema']=value.get('schema')
                meta['original_status']=value.get('status')
            record['files'].append(meta)
        record.update(status='complete-original-artifact-recovered-without-research-rerun',
            phase='complete',elapsed_seconds=time.monotonic()-started,
            json_file_count=len(files),all_original_JSON_bytes_preserved=True,
            original_publication_failure_not_reclassified_as_scientific_failure=True)
        write_receipt(out_dir/'artifact-recovery-receipt.json',record)
        return record
    except Exception as error:
        # Network helpers replace URL-bearing exceptions with fixed messages;
        # neither the token nor signed download query is serialized here.
        record.update(status='artifact-recovery-failed-with-original-data-unchanged',phase=phase,
            elapsed_seconds=time.monotonic()-started,
            error={'type':type(error).__name__,'message':str(error)})
        write_receipt(out_dir/'artifact-recovery-failure.json',record)
        raise


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-dir',type=Path,required=True)
    args=parser.parse_args()
    try:
        report=recover(args.out_dir)
    except Exception as error:
        print(json.dumps({'status':'artifact-recovery-failed','error_type':type(error).__name__}),flush=True)
        raise SystemExit(1)
    print(json.dumps({'status':report['status'],'original_run_id':ORIGINAL_RUN,
        'original_artifact_id':ORIGINAL_ARTIFACT,'json_file_count':report['json_file_count'],
        'archive_sha256':report['downloaded_archive_sha256'],'research_reexecuted':False}),flush=True)


if __name__=='__main__':
    main()
