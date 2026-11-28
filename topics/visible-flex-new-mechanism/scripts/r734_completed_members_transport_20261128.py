#!/usr/bin/env python3
"""Transport two exact R734 members from its naturally completed receiver; no science."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

REPO='Rogerhu12/math-research-public'
API='https://api.github.com/repos/'+REPO

def sha(raw):return hashlib.sha256(raw).hexdigest()
def require(ok,message):
    if not ok:raise RuntimeError(message)
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,request,fp,code,msg,headers,newurl):return None

def get_json(path,token):
    request=urllib.request.Request(API+path,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
    with urllib.request.build_opener(NoRedirect).open(request,timeout=60) as response:
        return json.load(response)

def completed(meta,token):
    run=get_json('/actions/runs/'+str(meta['run']),token)
    job=get_json('/actions/jobs/'+str(meta['job']),token)
    require(run['id']==meta['run'] and run['head_sha']==meta['head'] and run['status']=='completed' and run['conclusion']=='success','Original completed run identity differs')
    require(job['id']==meta['job'] and job['run_id']==meta['run'] and job['head_sha']==meta['head'] and job['status']=='completed' and job['conclusion']=='success','Original completed job identity differs')

def fetch_zip(meta,token,dest):
    artifact=get_json('/actions/artifacts/'+str(meta['artifact']),token)
    require(not artifact['expired'] and artifact['size_in_bytes']==meta['zip_bytes'] and artifact['digest']=='sha256:'+meta['zip_sha256'],'Completed artifact bytes/digest differ')
    require(artifact['workflow_run']['id']==meta['run'] and artifact['workflow_run']['head_sha']==meta['head'],'Completed artifact source differs')
    request=urllib.request.Request(API+'/actions/artifacts/'+str(meta['artifact'])+'/zip',headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'})
    try:
        response=urllib.request.build_opener(NoRedirect).open(request,timeout=60)
    except urllib.error.HTTPError as error:
        require(error.code in (301,302,303,307,308),'Artifact redirect failed')
        url=error.headers['Location'];u=urllib.parse.urlsplit(url)
        require(u.scheme=='https' and bool(u.hostname) and not u.username and not u.password,'Artifact redirect is not HTTPS')
        response=urllib.request.urlopen(urllib.request.Request(url),timeout=60)
    total=0;digest=hashlib.sha256()
    with response, dest.open('wb') as out:
        while True:
            block=response.read(1<<20)
            if not block:break
            total+=len(block)
            require(total<=meta['zip_bytes'],'Artifact larger than pinned size')
            digest.update(block);out.write(block)
    require(total==meta['zip_bytes'] and digest.hexdigest()==meta['zip_sha256'],'Completed artifact ZIP changed')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--request',required=True);args=ap.parse_args()
    started=time.monotonic();request=json.loads(Path(args.request).read_bytes())
    require(request['repository']==REPO,'Repository mismatch')
    for path,digest in request['source_sha256'].items():require(sha(Path(path).read_bytes())==digest,'Bound source changed: '+path)
    cfg=json.loads(Path(request['common_parameters']['geometry']).read_bytes());hist=cfg['paid_r734'];donor=hist['receiver']
    token=os.environ.get('GITHUB_TOKEN','');require(bool(token),'Read token required')
    completed(hist,token);completed(donor,token)
    tmp=Path(os.environ['RUNNER_TEMP']);names=request['paid_input_names']
    require(all(PurePosixPath(v).name==v for v in names.values()),'Input names must be basenames')
    output=tmp/names['checkpoint_directory'];output.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='r734-completed-transport-',dir=tmp) as folder:
        archive=Path(folder)/'original.zip';fetch_zip(donor,token,archive)
        with zipfile.ZipFile(archive) as source:
            for which,canonical in [('terminal','r734-original-final.json'),('journal','r734-original-tail.jsonl')]:
                member=donor[which+'_member'];infos=[x for x in source.infolist() if x.filename==member]
                require(len(infos)==1,'Missing or duplicate original member')
                info=infos[0]
                require(not info.is_dir() and info.file_size==hist[which+'_bytes'] and ((info.external_attr>>16)&0o170000)!=0o120000,'Original member type/size differs')
                raw=source.read(info);require(len(raw)==hist[which+'_bytes'] and sha(raw)==hist[which+'_sha256'],'Original member hash differs')
                for dest in [tmp/names[which],output/canonical]:
                    if dest.exists():require(dest.read_bytes()==raw,'Existing paid input differs')
                    else:
                        stage=dest.with_name(dest.name+'.transport-tmp');stage.write_bytes(raw);stage.replace(dest)
    receipt={'kind':'r734_exact_completed_members_transport','original_run':hist['run'],'receiver_run':donor['run'],'receiver_artifact':donor['artifact'],'administrative_seconds':time.monotonic()-started,'completed_original_log_requests':0,'new_scientific_evaluations':0,'members':{k:{'bytes':hist[k+'_bytes'],'sha256':hist[k+'_sha256']} for k in ['terminal','journal']}}
    (output/'completed-members-transport.json').write_text(json.dumps(receipt,sort_keys=True)+'\n')
    print('R734_COMPLETED_MEMBERS_TRANSPORT '+json.dumps(receipt,sort_keys=True),flush=True)
if __name__=='__main__':main()
