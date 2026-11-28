#!/usr/bin/env python3
"""Restore an immutable completed input bundle; perform no scientific evaluation."""
import argparse
import base64
import json
import os
from pathlib import Path, PurePosixPath
import tempfile
import time
import zipfile
from r734_completed_members_transport_20261128 import completed,fetch_zip,require,sha


def safe_name(value):
    path=PurePosixPath(value)
    require(bool(value) and not path.is_absolute() and '..' not in path.parts,'Invalid paid-input path')
    return path


def retain(path,raw):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():require(path.read_bytes()==raw,'Existing immutable input differs: '+path.name)
    else:
        part=path.with_name(path.name+'.transport-part');part.write_bytes(raw);part.replace(path)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--request',required=True);args=ap.parse_args()
    start=time.monotonic();req=json.loads(Path(args.request).read_bytes())
    require(req['repository']=='Rogerhu12/math-research-public','Wrong repository')
    require(os.environ.get('GITHUB_ACTIONS')=='true' and os.environ.get('GITHUB_REPOSITORY','').lower()==req['repository'].lower(),'Public Actions input transport required')
    for path,digest in req['source_sha256'].items():require(sha(Path(path).read_bytes())==digest,'Bound source changed: '+path)
    temp=Path(os.environ['RUNNER_TEMP']);directory=req['paid_source_directory']
    require(PurePosixPath(directory).name==directory,'Input directory must be a basename')
    out=temp/directory;out.mkdir(exist_ok=True)
    token=os.environ.get('GITHUB_TOKEN','');require(bool(token),'Read credential required')
    spec=req['completed_sources'];donor=spec['receiver'];completed(donor,token)
    transported={}
    with tempfile.TemporaryDirectory(prefix='completed-r738-inputs-',dir=temp) as folder:
        path=Path(folder)/'completed.zip';fetch_zip(donor,token,path)
        with zipfile.ZipFile(path) as z:
            names=z.namelist();require(len(names)==len(set(names)),'Repeated completed member')
            for name,meta in spec['files'].items():
                target=safe_name(name);info=z.getinfo(name)
                require(not info.is_dir() and ((info.external_attr>>16)&0o170000)!=0o120000 and info.file_size==meta['bytes'],'Completed member type/size differs')
                raw=z.read(info);require(len(raw)==meta['bytes'] and sha(raw)==meta['sha256'],'Completed member SHA differs: '+name)
                retain(out/target,raw);transported[name]={'bytes':len(raw),'sha256':sha(raw)}
    inlined={}
    for name,meta in req.get('inline_paid_sources',{}).items():
        require(name not in transported,'Repeated inline paid input');target=safe_name(name)
        raw=base64.b64decode(meta['base64'],validate=True)
        require(len(raw)==meta['bytes'] and sha(raw)==meta['sha256'],'Original inline paid metadata differs')
        retain(out/target,raw);inlined[name]={'bytes':len(raw),'sha256':sha(raw)}
    receipt={'kind':'exact_completed_R738_input_restore','receiver':donor,
             'restoring_run':os.environ['GITHUB_RUN_ID'],'restoring_attempt':os.environ.get('GITHUB_RUN_ATTEMPT','1'),
             'member_count':len(transported),'inline_members':inlined,
             'administrative_seconds':time.monotonic()-start,'new_scientific_evaluations':0,
             'original_job_log_requests':0,'files':transported}
    raw=json.dumps(receipt,sort_keys=True,separators=(',',':')).encode()
    receipt_name='input-restore-'+os.environ['GITHUB_RUN_ID']+'-'+os.environ.get('GITHUB_RUN_ATTEMPT','1')+'.json'
    retain(out/receipt_name,raw)
    checkpoint=req.get('new_checkpoint_directory')
    if checkpoint:
        require(PurePosixPath(checkpoint).name==checkpoint,'Checkpoint directory must be a basename')
        folder=temp/checkpoint;folder.mkdir(exist_ok=True)
        retain(folder/receipt_name,raw)
    print('COMPLETED_R738_INPUTS_RESTORED '+json.dumps({k:v for k,v in receipt.items() if k!='files'},sort_keys=True),flush=True)


if __name__=='__main__':main()
