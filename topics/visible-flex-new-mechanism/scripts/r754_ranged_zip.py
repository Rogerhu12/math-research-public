"""Bounded original-archive transport. Only completed GitHub artifact members are read."""
from collections import OrderedDict
import hashlib
import io
import json
import os
from pathlib import Path
import re
import stat
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
            handoff_path=os.environ.get('R754_PARENT_HANDOFF')
            if not handoff_path:raise ValueError('missing the short-lived read-only artifact handoff')
            root=Path(os.environ['RUNNER_TEMP']).resolve()
            path=Path(handoff_path)
            if not path.is_absolute() or path.parent.resolve()!=root:
                raise ValueError('original artifact handoff must be directly under RUNNER_TEMP')
            with os.fdopen(os.open(path,os.O_RDONLY|os.O_NOFOLLOW),'r') as fp:
                st=os.fstat(fp.fileno())
                if (not stat.S_ISREG(st.st_mode) or st.st_uid!=os.getuid() or st.st_mode&0o077
                        or st.st_size>32768):raise ValueError('invalid private artifact handoff')
                hand=json.load(fp)
            self.provider=hand['provider']
            want=dict(artifact_id=int(spec['artifact_id']),official_digest='sha256:'+spec['artifact_sha256'],
                      bytes=int(spec['artifact_bytes']),run_id=int(spec['run_id']),head_sha=spec['head_sha'])
            if (self.provider!=want or hand['strong_etag']!=spec['strong_etag']
                    or hand['consumer_run_id']!=os.environ.get('GITHUB_RUN_ID')
                    or hand['consumer_attempt']!=os.environ.get('GITHUB_RUN_ATTEMPT','1')):
                raise ValueError('handoff and immutable original or consumer identity differ')
            address=safe_address(hand['signed_address'])
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
    args.add_argument('--prepare-signed-handoff',action='store_true',
                      help='authenticated transport step; --out must be a fresh RUNNER_TEMP path')
    a=args.parse_args();spec=json.loads(Path(a.metadata).read_text())
    if a.prepare_signed_handoff:
        root=Path(os.environ['RUNNER_TEMP']).resolve()
        output=Path(a.out)
        if (not output.is_absolute() or output.parent.resolve()!=root or not os.environ.get('GITHUB_RUN_ID','').isdigit()
                or os.environ.get('GITHUB_REPOSITORY','').lower()!=REPO.lower()):
            raise ValueError('the private handoff is restricted to the current research workflow')
        start=time.monotonic();provider=artifact_metadata(spec);url=signed_url(int(spec['artifact_id']))
        req=urllib.request.Request(url,headers={'Range':'bytes=0-0','If-Match':spec['strong_etag'],
                                                'Accept-Encoding':'identity'})
        try:
            with urllib.request.build_opener(NoRedirect).open(req,timeout=45) as f:
                if (f.status!=206 or f.headers.get('Content-Range')!='bytes 0-0/'+str(provider['bytes'])
                        or f.headers.get('ETag')!=spec['strong_etag'] or len(f.read(2))!=1):
                    raise ValueError('signed original byte probe, size or strong ETag mismatch')
        except (OSError,urllib.error.HTTPError) as exc:
            raise OSError('signed artifact byte verification failed') from None
        data=dict(provider=provider,strong_etag=spec['strong_etag'],signed_address=url,
                  consumer_run_id=os.environ['GITHUB_RUN_ID'],
                  consumer_attempt=os.environ.get('GITHUB_RUN_ATTEMPT','1'))
        with os.fdopen(os.open(output,os.O_CREAT|os.O_EXCL|os.O_WRONLY|os.O_NOFOLLOW,0o600),'w') as f:
            json.dump(data,f)
        print(json.dumps(dict(original_artifact=provider['artifact_id'],administrative_seconds=time.monotonic()-start,
                              bytes_received=1,scientific_evaluations=0,full_zip_downloaded=False)))
        raise SystemExit(0)
    with RangedArchive(spec,authenticated=True) as original:
        docs=original_documents(original)
        spec.update(input_identity=docs['terminal']['input_identity'],terminal_sha256=docs['terminal']['sha256'],
                    continuation_sha256=docs['continuation']['sha256'],
                    source_identity_sha256=docs['source-identity']['sha256'],strong_etag=original.etag)
        out=dict(**spec,selected_documents=docs,transport=dict(ranges=original.ranges,bytes=original.bytes_received))
        Path(a.out).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
