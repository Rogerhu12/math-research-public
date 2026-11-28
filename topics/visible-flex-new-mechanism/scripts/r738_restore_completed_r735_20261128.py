#!/usr/bin/env python3
"""Pure I/O: restore the original R734/R735 paid inputs for the first thick-source solve."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from r734_completed_members_transport_20261128 import API, NoRedirect, completed, fetch_zip, require, sha


def completed_job_log(job,token):
    req=urllib.request.Request(API+'/actions/jobs/'+str(job)+'/logs',headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'})
    try:
        response=urllib.request.build_opener(NoRedirect).open(req,timeout=60)
    except urllib.error.HTTPError as error:
        require(error.code in (301,302,303,307,308),'Completed log redirect failed')
        url=error.headers['Location'];parts=urllib.parse.urlsplit(url)
        require(parts.scheme=='https' and bool(parts.hostname) and not parts.username and not parts.password,'Completed log redirect is not HTTPS')
        response=urllib.request.urlopen(urllib.request.Request(url),timeout=60)
    with response:
        raw=response.read(32*1024*1024+1)
    require(len(raw)<=32*1024*1024,'Completed log exceeds this exact-source transport limit')
    found=[]
    for line in raw.decode('utf-8').splitlines():
        marker='R735_FINAL '
        if marker not in line:continue
        value=line.split(marker,1)[1]
        if not value.startswith('{'):continue
        obj=json.loads(value)
        if obj.get('kind')=='terminal' and 'new_fingerprint' in obj:found.append(value.encode())
    require(len(found)==1,'Original R735 terminal literal is missing or duplicated')
    return found[0],len(raw),sha(raw)


def write_once(path,raw):
    if path.exists():require(path.read_bytes()==raw,'Retained completed input changed: '+path.name)
    else:
        stage=path.with_name(path.name+'.transport-tmp');stage.write_bytes(raw);stage.replace(path)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--request',required=True);args=ap.parse_args()
    start=time.monotonic();req=json.loads(Path(args.request).read_bytes())
    require(req['repository']=='Rogerhu12/math-research-public','Repository differs')
    for path,digest in req['source_sha256'].items():require(sha(Path(path).read_bytes())==digest,'Bound source changed: '+path)
    donor=req['completed_r735'];cfg=json.loads(Path(req['common_parameters']['geometry']).read_bytes());original=cfg['paid_r734']
    meta={'run':donor['source_run'],'job':donor['source_job'],'head':donor['source_head'],'artifact':donor['artifact'],'zip_bytes':donor['zip_bytes'],'zip_sha256':donor['zip_sha256']}
    require(donor['source_run_conclusion']=='success','The requested donor did not naturally succeed')
    token=os.environ.get('GITHUB_TOKEN','');require(bool(token),'Read token required')
    completed(meta,token);completed(original,token)
    tmp=Path(os.environ['RUNNER_TEMP']);out=tmp/'r738-paid';out.mkdir(parents=True,exist_ok=True)
    members={}
    with tempfile.TemporaryDirectory(prefix='r738-original-donor-',dir=tmp) as folder:
        zip_path=Path(folder)/'original-r735.zip';fetch_zip(meta,token,zip_path)
        with zipfile.ZipFile(zip_path) as archive:
            for member,base,expected_bytes,expected_sha in [
                ('r734-original-final.json','r734-original-final.json',original['terminal_bytes'],original['terminal_sha256']),
                ('r734-original-tail.jsonl','r734-original-tail.jsonl',original['journal_bytes'],original['journal_sha256']),
                (donor['journal_member'],'r735-original-central.jsonl',None,None)]:
                infos=[i for i in archive.infolist() if i.filename==member]
                require(len(infos)==1,'Missing or repeated exact original archive member: '+member)
                info=infos[0]
                require(not info.is_dir() and ((info.external_attr>>16)&0o170000)!=0o120000 and info.file_size<=512*1024*1024,'Invalid original member type or size')
                raw=archive.read(info)
                require(len(raw)==info.file_size,'Original member was truncated')
                if expected_bytes is not None:require(len(raw)==expected_bytes and sha(raw)==expected_sha,'Original R734 member differs')
                members[member]={'bytes':len(raw),'sha256':sha(raw)}
                write_once(tmp/base,raw);write_once(out/base,raw)
    literal,log_bytes,log_sha=completed_job_log(donor['source_job'],token)
    require(len(literal)==donor['terminal_bytes'] and sha(literal)==donor['terminal_sha256'],'Exact original R735 FINAL differs')
    write_once(tmp/'r735-original-final.json',literal);write_once(out/'r735-original-final.json',literal)
    binding=dict(donor,member_zip_verified=True,journal_bytes=members[donor['journal_member']]['bytes'],journal_sha256=members[donor['journal_member']]['sha256'],donor_source_sha256={name:req['source_sha256']['topics/visible-flex-new-mechanism/scripts/'+name] for name in ['r734_true_dyadic_tail.py','r735_paid_tail_beta_envelope.py','r735_actual_two_port_match.py']})
    raw=json.dumps(binding,sort_keys=True,separators=(',',':')).encode()
    write_once(tmp/'r735-completed-donor-binding.json',raw);write_once(out/'r735-completed-donor-binding.json',raw)
    receipt={'kind':'r738_completed_r735_and_original_r734_transport','administrative_seconds':time.monotonic()-start,'new_scientific_evaluations':0,'original_completed_log_requests':1,'source_run':donor['source_run'],'source_job':donor['source_job'],'source_head':donor['source_head'],'artifact':donor['artifact'],'zip_bytes':donor['zip_bytes'],'zip_sha256':donor['zip_sha256'],'members':members,'literal_bytes':len(literal),'literal_sha256':sha(literal),'original_log_bytes':log_bytes,'original_log_sha256':log_sha}
    (out/'r735-original-transport-receipt.json').write_text(json.dumps(receipt,sort_keys=True)+'\n')
    print('R738_COMPLETED_DONOR_TRANSPORT '+json.dumps(receipt,sort_keys=True),flush=True)
if __name__=='__main__':main()
