#!/usr/bin/env python3
"""Pure byte transport of the naturally completed R738 source for R745/R748."""
import argparse
import json
import os
from pathlib import Path, PurePosixPath
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from r734_completed_members_transport_20261128 import API, NoRedirect, completed, fetch_zip, require, sha
import run_inverse_rotational_metric_20261126 as rules


def write_once(path,raw):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():require(path.read_bytes()==raw,'Different existing paid member: '+path.name)
    else:
        temp=path.with_name(path.name+'.transport-part');temp.write_bytes(raw);temp.replace(path)


def original_final(meta,token):
    req=urllib.request.Request(API+'/actions/jobs/'+str(meta['job'])+'/logs',headers={
        'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'})
    try:response=urllib.request.build_opener(NoRedirect).open(req,timeout=60)
    except urllib.error.HTTPError as error:
        require(error.code in (301,302,303,307,308),'Completed log redirect failed')
        u=error.headers['Location'];p=urllib.parse.urlsplit(u)
        require(p.scheme=='https' and bool(p.hostname) and not p.username and not p.password,'Invalid completed-log HTTPS redirect')
        response=urllib.request.urlopen(urllib.request.Request(u),timeout=60)
    with response:raw=response.read(32*1024*1024+1)
    require(len(raw)<=32*1024*1024,'Completed log exceeds bound')
    found=[]
    for line in raw.decode('utf-8').splitlines():
        k=line.find('{')
        if k<0:continue
        try:value=json.loads(line[k:])
        except json.JSONDecodeError:continue
        if value.get('kind')=='terminal' and value.get('fingerprint')==meta['fingerprint'] and 'all_parameters' in value:
            found.append(line[k:].encode())
    require(len(found)==1,'Original final missing or duplicated')
    result=found[0]
    require(len(result)==meta['terminal_bytes'] and sha(result)==meta['terminal_sha256'],'Exact original terminal bytes differ')
    return result,len(raw),sha(raw)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--request',required=True);args=ap.parse_args()
    started=time.monotonic();request_path=Path(args.request);req=json.loads(request_path.read_bytes())
    require(req['repository']=='Rogerhu12/math-research-public','Wrong public repository')
    require(os.environ.get('GITHUB_ACTIONS')=='true' and os.environ.get('GITHUB_REPOSITORY','').lower()==req['repository'].lower(),'Public Actions transport required')
    for path,digest in req['source_sha256'].items():require(sha(Path(path).read_bytes())==digest,'Bound administrative source changed: '+path)
    read_public=rules.public_pull(Path.cwd(),req,os.environ['GITHUB_SHA']);read_private=rules.private_pull(req)
    require(json.loads(request_path.read_bytes())==req,'Request changed during current-rules pull')
    for path,digest in req['source_sha256'].items():require(sha(Path(path).read_bytes())==digest,'Administrative source changed after pull: '+path)
    token=os.environ.get('GITHUB_TOKEN','');require(bool(token),'Read credential absent')
    meta=req['completed_r738'];completed(meta,token)
    temp=Path(os.environ['RUNNER_TEMP']);output=temp/'r738-completed-sources';output.mkdir(exist_ok=True)
    actual={}
    with tempfile.TemporaryDirectory(prefix='r738-completed-bytes-',dir=temp) as folder:
        archive=Path(folder)/'original.zip';fetch_zip(meta,token,archive)
        with zipfile.ZipFile(archive) as z:
            infos=z.infolist();names=[x.filename for x in infos]
            require(len(names)==len(set(names)),'Repeated original archive members')
            for source,record in req['members'].items():
                target=PurePosixPath(record['target'])
                require(not target.is_absolute() and '..' not in target.parts,'Invalid output member')
                info=z.getinfo(source)
                require(not info.is_dir() and ((info.external_attr>>16)&0o170000)!=0o120000 and info.file_size==record['bytes'],'Wrong original member type or size')
                raw=z.read(info);require(len(raw)==record['bytes'] and sha(raw)==record['sha256'],'Original paid member hash differs: '+source)
                write_once(output/target,raw);actual[str(target)]={'bytes':len(raw),'sha256':sha(raw)}
    final,log_bytes,log_sha=original_final(meta,token)
    write_once(output/'r738-final.json',final);actual['r738-final.json']={'bytes':len(final),'sha256':sha(final)}
    receipt={'kind':'r738_exact_completed_input_bundle','source':meta,'members':actual,
             'administrative_seconds':time.monotonic()-started,'new_scientific_evaluations':0,
             'original_completed_job_log_requests':1,'original_log_bytes':log_bytes,'original_log_sha256':log_sha,
             'actual_public_rules_read_commit':read_public,'actual_private_rules_read_commit':read_private,
             'is_full_R738_solver_checkpoint':False,'full_original_checkpoint_retained_at_artifact':meta['artifact']}
    write_once(output/'completed-input-transport.json',json.dumps(receipt,sort_keys=True,separators=(',',':')).encode())
    print('R738_COMPLETED_INPUT_BUNDLE '+json.dumps({k:v for k,v in receipt.items() if k!='members'},sort_keys=True),flush=True)
    print('R738_COMPLETED_INPUT_MEMBERS '+json.dumps({'count':len(actual),'uncompressed_bytes':sum(v['bytes'] for v in actual.values()),'manifest_bytes':(output/'completed-input-transport.json').stat().st_size,'manifest_sha256':sha((output/'completed-input-transport.json').read_bytes())},sort_keys=True),flush=True)


if __name__=='__main__':main()
