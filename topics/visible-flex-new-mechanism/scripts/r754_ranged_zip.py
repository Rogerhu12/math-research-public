"""Bounded original-archive transport. Only completed GitHub artifact members are read."""
from collections import OrderedDict
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


REPO='Rogerhu12/math-research-public'
BLOCK=2**20
LIMIT=16


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):
        return None


def api(path):
    headers={'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28',
             'User-Agent':'R754-completed-parent-reader'}
    token=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:headers['Authorization']='Bearer '+token
    req=urllib.request.Request('https://api.github.com/repos/'+REPO+path,headers=headers)
    return urllib.request.build_opener(NoRedirect).open(req,timeout=30)


def artifact_metadata(spec):
    aid=int(spec['artifact_id'])
    with api('/actions/artifacts/'+str(aid)) as f:
        obj=json.load(f)
    run=obj['workflow_run']
    if (int(obj['id'])!=aid or int(run['id'])!=int(spec['run_id']) or run['head_sha']!=spec['head_sha']
            or obj['expired'] or int(obj['size_in_bytes'])!=int(spec['artifact_bytes'])
            or obj.get('digest')!='sha256:'+spec['artifact_sha256']):
        raise ValueError('actual GitHub artifact identity, size or official digest differs')
    return dict(artifact_id=aid,official_digest=obj['digest'],bytes=int(obj['size_in_bytes']),
                run_id=int(run['id']),head_sha=run['head_sha'])


def signed_url(aid):
    try:
        with api('/actions/artifacts/'+str(int(aid))+'/zip'):
            raise ValueError('GitHub did not issue a separate artifact address')
    except urllib.error.HTTPError as e:
        if e.code not in (301,302,303,307,308):raise OSError('GitHub artifact redirect failed: '+str(e.code)) from None
        address=e.headers.get('Location','')
        e.close()
    return safe_address(address)


def safe_address(address):
    if not address or any(ord(c)<33 for c in address):raise OSError('invalid artifact address')
    uri=urllib.parse.urlsplit(address)
    name=(uri.hostname or '').lower()
    if (uri.scheme!='https' or uri.username or uri.password or uri.port not in (None,443)
            or not any(name.endswith('.'+d) for d in ('blob.core.windows.net','githubusercontent.com',
                                                        'actions.githubusercontent.com'))):
        raise OSError('GitHub returned an unrecognized signed artifact host')
    return address


class RangedArchive(io.RawIOBase):
    def __init__(self,spec,on_transfer=None,authenticated=False):
        super().__init__()
        self.authenticated=authenticated
        if authenticated:
            self.provider=artifact_metadata(spec);address=None
        else:
            authorization=os.environ.get('R754_COMPLETED_ARTIFACT_RECEIPT')
            if not authorization:raise ValueError('missing the original artifact transport receipt')
            hand=json.loads(authorization)
            self.provider=hand['provider']
            want=dict(artifact_id=int(spec['artifact_id']),official_digest='sha256:'+spec['artifact_sha256'],
                      bytes=int(spec['artifact_bytes']),run_id=int(spec['run_id']),head_sha=spec['head_sha'])
            if (self.provider!=want or hand['strong_etag']!=spec['strong_etag']
                    or hand['consumer_run_id']!=os.environ.get('GITHUB_RUN_ID')
                    or hand['consumer_attempt']!=os.environ.get('GITHUB_RUN_ATTEMPT','1')):
                raise ValueError('handoff and immutable original or consumer identity differ')
            address=safe_address(os.environ.get('R754_COMPLETED_ARTIFACT_URL',''))
        self.length=self.provider['bytes'];self.aid=self.provider['artifact_id']
        self.pos=0;self.cache=OrderedDict();self.address=address;self.etag=spec.get('strong_etag')
        self.ranges=0;self.bytes_received=0;self.on_transfer=on_transfer

    def seekable(self):return True
    def readable(self):return True
    def tell(self):return self.pos

    def seek(self,offset,whence=0):
        new=({0:0,1:self.pos,2:self.length}[whence])+offset
        if new<0:raise ValueError('negative original ZIP seek')
        self.pos=new
        return new

    def fetch(self,number):
        if number in self.cache:
            self.cache.move_to_end(number);return self.cache[number]
        lo=number*BLOCK;hi=min(self.length,lo+BLOCK)-1
        for attempt in range(4):
            if self.address is None:
                if not self.authenticated:raise OSError('the original artifact handoff has expired')
                self.address=signed_url(self.aid)
            headers={'Range':f'bytes={lo}-{hi}','Accept-Encoding':'identity'}
            if self.etag is not None:headers['If-Match']=self.etag
            req=urllib.request.Request(self.address,headers=headers)
            try:
                with urllib.request.build_opener(NoRedirect).open(req,timeout=45) as f:
                    cr=f.headers.get('Content-Range','');tag=f.headers.get('ETag','')
                    if (f.status!=206 or cr!=f'bytes {lo}-{hi}/{self.length}' or
                            f.headers.get('Content-Encoding','identity')!='identity' or
                            not re.fullmatch(r'"[^"]+"',tag) or self.etag not in (None,tag)):
                        raise ValueError('signed original range, strong ETag or file length changed')
                    buf=f.read(hi-lo+2)
                    if len(buf)!=hi-lo+1:raise OSError('short original artifact range')
                break
            except urllib.error.HTTPError as e:
                status=e.code;e.close()
                if status in (401,403) and self.authenticated and attempt<3:self.address=None;continue
                if status in (408,429,500,502,503,504) and attempt<3:
                    time.sleep(1+attempt);continue
                raise OSError('signed artifact range failed: '+str(status)) from None
            except (urllib.error.URLError,TimeoutError,OSError):
                if attempt==3:raise OSError('signed artifact range unavailable') from None
                time.sleep(1+attempt)
        self.etag=tag;self.ranges+=1;self.bytes_received+=len(buf)
        if self.on_transfer:self.on_transfer(lo,hi,self.etag)
        self.cache[number]=buf
        if len(self.cache)>LIMIT:self.cache.popitem(last=False)
        return buf

    def read(self,size=-1):
        if size<0:size=max(0,self.length-self.pos)
        if size>96*2**20:raise ValueError('single ZIP directory read exceeds the bounded transfer window')
        end=min(self.length,self.pos+size)
        pieces=[]
        while self.pos<end:
            number,offset=divmod(self.pos,BLOCK)
            data=self.fetch(number)
            n=min(len(data)-offset,end-self.pos)
            pieces.append(data[offset:offset+n]);self.pos+=n
        return b''.join(pieces)


def original_documents(archive):
    import zipfile
    with zipfile.ZipFile(archive) as z:
        matches=[p for p in z.namelist() if p=='input-identity.json' or p.endswith('/input-identity.json')]
        if len(matches)!=1:raise ValueError('ambiguous original input-identity root')
        prefix=matches[0][:-len('input-identity.json')]
        result={}
        for name in ('input-identity','terminal','continuation','source-identity'):
            p=prefix+name+'.json'
            if z.getinfo(p).file_size>32*2**20:raise ValueError('unexpected original metadata size')
            content=z.read(p)
            result[name]=dict(member=p,sha256=hashlib.sha256(content).hexdigest())
            if name=='terminal':result[name]['input_identity']=json.loads(content)['input_identity']
    return result


if __name__=='__main__':
    import argparse
    args=argparse.ArgumentParser()
    args.add_argument('--metadata',required=True,help='pinned artifact id/size/official digest and run/head')
    args.add_argument('--out',required=True)
    args.add_argument('--launch-driver',action='store_true',
                      help='verify the single original and start the unchanged common driver')
    args.add_argument('--request')
    args.add_argument('--lane',default='actual-physical-disks')
    a=args.parse_args();spec=json.loads(Path(a.metadata).read_text())
    if a.launch_driver:
        if (not a.request or a.lane!='actual-physical-disks' or not os.environ.get('GITHUB_RUN_ID','').isdigit()
                or os.environ.get('GITHUB_REPOSITORY','').lower()!=REPO.lower()):
            raise ValueError('original artifact transport is restricted to the current public disk workflow')
        start=time.monotonic()
        driver=Path(__file__).resolve().with_name('run_inverse_rotational_metric_20261126.py')
        run_id=int(spec['run_id']);job_id=int(spec['job_id'])
        with api('/actions/runs/'+str(run_id)) as f:run=json.load(f)
        with api('/actions/jobs/'+str(job_id)) as f:job=json.load(f)
        if (int(run['id'])!=run_id or run['head_sha']!=spec['head_sha'] or run['status']!='completed'
                or run['conclusion']!='success' or int(job['run_id'])!=run_id or int(job['id'])!=job_id
                or job['status']!='completed' or job['conclusion']!='success'
                or not job.get('completed_at')):
            raise ValueError('the specified parent run/job is not the naturally successful completed allocation')
        provider=artifact_metadata(spec);url=signed_url(int(spec['artifact_id']))
        req=urllib.request.Request(url,headers={'Range':'bytes=0-0','If-Match':spec['strong_etag'],
                                                'Accept-Encoding':'identity'})
        try:
            with urllib.request.build_opener(NoRedirect).open(req,timeout=45) as f:
                if (f.status!=206 or f.headers.get('Content-Range')!='bytes 0-0/'+str(provider['bytes'])
                        or f.headers.get('ETag')!=spec['strong_etag'] or len(f.read(2))!=1):
                    raise ValueError('signed original byte probe, size or strong ETag mismatch')
        except (OSError,urllib.error.HTTPError) as exc:
            raise OSError('signed artifact byte verification failed') from None
        data=dict(provider=provider,strong_etag=spec['strong_etag'],verified_job=job_id,job_completed_at=job['completed_at'],
                  consumer_run_id=os.environ['GITHUB_RUN_ID'],
                  consumer_attempt=os.environ.get('GITHUB_RUN_ATTEMPT','1'))
        # Deliberately omit the signed address from files, command arguments and output.
        output=Path(a.out);output.parent.mkdir(parents=True,exist_ok=True)
        receipt=dict(**data,administrative_seconds=time.monotonic()-start,bytes_received=1,
                     scientific_evaluations=0,full_zip_downloaded=False)
        output.write_text(json.dumps(receipt,sort_keys=True)+'\n')
        env=dict(os.environ,R754_COMPLETED_ARTIFACT_URL=url,
                 R754_COMPLETED_ARTIFACT_RECEIPT=json.dumps(data,sort_keys=True))
        command=[sys.executable,str(driver),'--request',a.request,'--lane',a.lane]
        raise SystemExit(subprocess.run(command,env=env,check=False).returncode)
    with RangedArchive(spec,authenticated=True) as original:
        docs=original_documents(original)
        spec.update(input_identity=docs['terminal']['input_identity'],terminal_sha256=docs['terminal']['sha256'],
                    continuation_sha256=docs['continuation']['sha256'],
                    source_identity_sha256=docs['source-identity']['sha256'],strong_etag=original.etag)
        out=dict(**spec,selected_documents=docs,transport=dict(ranges=original.ranges,bytes=original.bytes_received))
        Path(a.out).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
