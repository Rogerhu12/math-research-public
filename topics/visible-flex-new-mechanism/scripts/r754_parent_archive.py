"""Read-only, pinned R746 artifact. No original solver operations or unpickling."""
import hashlib
import json
from pathlib import Path
import platform
import shutil
import tempfile
import zipfile

import numpy as np
import scipy

import r754_nested_rotation as model

HERE=Path(__file__).resolve().parent
RUN='46172869144'
COMMIT='f406ba20aa8cf46172036d071d007d503834faa2'


def stream_digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for b in iter(lambda:stream.read(2**20),b''):
            h.update(b)
    return h.hexdigest()


class Parent:
    def __init__(self,archive,specification,engine):
        self.engine=engine
        spec=json.loads(Path(specification).read_text())
        if (str(spec['run_id'])!=RUN or spec['head_sha']!=COMMIT or int(spec['artifact_id'])<=0
                or len(spec['artifact_sha256'])!=64 or len(spec['input_identity'])!=64):
            raise ValueError('R754 requires the identified natural first R746 allocation')
        self.spec=spec;self.bytes_sha={};self.remote=None
        if archive is None:
            from r754_ranged_zip import RangedArchive
            self.remote=RangedArchive(spec);self.zip=zipfile.ZipFile(self.remote)
            if self.remote.etag!=spec['strong_etag']:
                raise ValueError('strong ETag differs from the pinned original member manifest')
        else:
            if Path(archive).stat().st_size!=int(spec['artifact_bytes']) or stream_digest(archive)!=spec['artifact_sha256']:
                raise ValueError('R746 parent artifact ZIP size or SHA256 mismatch')
            self.zip=zipfile.ZipFile(archive)
        self.names=set(self.zip.namelist())
        if len(self.names)!=len(self.zip.infolist()) or len(self.names)!=int(spec.get('member_count',len(self.names))):
            raise ValueError('ambiguous duplicate paths in the original artifact')
        matches=[p for p in self.names if p=='input-identity.json' or p.endswith('/input-identity.json')]
        if len(matches)!=1:
            raise ValueError('expected exactly one original continuation archive root')
        self.prefix=matches[0][:-len('input-identity.json')]
        self.meta=self.document('input-identity.json',spec['selected_documents']['input-identity']['sha256'])
        self.ident=engine.digest(engine.plain(self.meta).encode())
        if self.ident!=spec['input_identity']:
            raise ValueError('R746 original input metadata disagrees with the parent receipt')
        expected=set(engine.FILES)-set(model.NEW_FILES)
        if expected!=set(self.meta['sha256']):
            raise ValueError('R754 parent source-file closure differs from the original R746 input')
        for f,h in self.meta['sha256'].items():
            if stream_digest(HERE/f)!=h:
                raise ValueError('modified physical parent source: '+f)
        for key,value in (('python',platform.python_version()),('numpy',np.__version__),('scipy',scipy.__version__)):
            if self.meta[key]!=value:
                raise ValueError('restore original numeric environment: '+key)
        self.terminal=self.document('terminal.json',spec['terminal_sha256'])
        self.state=self.document('continuation.json',spec['continuation_sha256'])
        self.source_id=self.document('source-identity.json',spec['source_identity_sha256'])
        if self.terminal.get('input_identity')!=self.ident or str(self.terminal['run']).split('-')[0]!=RUN:
            raise ValueError('foreign R746 terminal record')
        self.records=list(self.state.get('records',[]))
        if self.terminal.get('finished_phase_records')!=len(self.records):
            raise ValueError('parent terminal and continuation disagree on finished phases')
        self.level=int(self.meta['settings']['level'])

    def document(self,name,sha=None):
        b=self.zip.read(self.prefix+name)
        if sha is not None and self.engine.digest(b)!=sha:
            raise ValueError('R746 original document mismatch: '+name)
        return json.loads(b)

    def key(self,kind,key):
        semantic=[self.ident,kind,key]
        sha=self.engine.digest(self.engine.plain(semantic).encode())
        return self.prefix+'paid/'+kind+'-'+sha+'.npz',semantic

    def has(self,kind,key):
        return self.key(kind,key)[0] in self.names

    def receipt(self,kind,key):
        path,semantic=self.key(kind,key)
        with self.zip.open(path) as source, tempfile.SpooledTemporaryFile(max_size=8*2**20) as dest:
            sha=hashlib.sha256()
            for chunk in iter(lambda:source.read(2**20),b''):
                sha.update(chunk);dest.write(chunk)
            checksum=sha.hexdigest()
            if self.bytes_sha.setdefault(path,checksum)!=checksum:
                raise ValueError('an original semantic member changed during the allocation')
            dest.seek(0)
            with np.load(dest,allow_pickle=False) as f:
                header=json.loads(f['meta'].tobytes())
                if header['semantic']!=json.loads(self.engine.plain(semantic)):
                    raise ValueError('R746 cached record does not match original operation identity')
                value=self.engine.Pack.decode(header['tree'],f)
        return value

    def transfer_archive(self,relative,path,sha):
        name=Path(relative).name
        if not name or not name.endswith('.npz'):
            raise ValueError('invalid parent physical archive name')
        item=self.prefix+'physical/'+name
        path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
        if path.exists():
            if stream_digest(path)!=sha:
                raise ValueError('different original physical archive at the destination')
        else:
            temp=path.with_suffix('.partial')
            with self.zip.open(item) as src,temp.open('wb') as dst:
                shutil.copyfileobj(src,dst,length=2**20)
            if stream_digest(temp)!=sha:
                temp.unlink();raise ValueError('R746 true physical six-jet archive mismatch')
            temp.replace(path)
        return path

    def warm(self,phase):
        candidates=[(r['degree'],r['q_values'],r['q']) for r in self.records if r['phase']==phase]
        now=self.state.get('current',{})
        if now.get('phase')==phase and 'current_q' in self.state:
            candidates.append((now['degree'],self.state['current_q'],now['q']))
        if not candidates:
            return None
        degree,values,id0=candidates[-1];old=np.asarray(values,dtype=float)
        if self.engine.array_id(old)!=id0 or old.size!=3*len(model.space.tagged_terms(degree)):
            raise ValueError('original trajectory control vector identity disagrees with the R746 terminal')
        return degree,old
