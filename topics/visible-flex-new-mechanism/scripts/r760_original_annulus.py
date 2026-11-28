"""Read the naturally completed R750 allocation through its actual immutable semantic keys."""
import hashlib
import json
from pathlib import Path
import platform
import tempfile
import zipfile

import numpy as np
import scipy
from scipy.sparse import csr_matrix

import r750_rigid_annulus as original
from r754_ranged_zip import RangedArchive

RUN='46174873079'
HEAD='c8c285fee6c7317c8d14749b71d25e703fef1802'
INPUT='2c6e610dcfc7f58328aa9dd3e51799df6ded740e4007caafec0ef69848a48197'
HERE=Path(__file__).resolve().parent


def stream_digest(file):
    value=hashlib.sha256()
    with Path(file).open('rb') as f:
        for chunk in iter(lambda:f.read(2**20),b''):value.update(chunk)
    return value.hexdigest()


class Parent:
    def __init__(self,specification,engine,new_files,archive=None):
        self.engine=engine;self.spec=json.loads(Path(specification).read_text())
        self.bytes_sha={};self.remote=None;s=self.spec
        if (str(s['run_id'])!=RUN or s['head_sha']!=HEAD or s['input_identity']!=INPUT
                or int(s['artifact_id'])!=15276188258 or int(s['job_id'])!=141071182352):
            raise ValueError('R760 requires the original naturally finished R750 job')
        if archive is None:
            self.remote=RangedArchive(s);self.zip=zipfile.ZipFile(self.remote)
            if self.remote.etag!=s['strong_etag']:raise ValueError('different original R750 artifact version')
        else:
            if Path(archive).stat().st_size!=s['artifact_bytes'] or stream_digest(archive)!=s['artifact_sha256']:
                raise ValueError('different original R750 full artifact bytes')
            self.zip=zipfile.ZipFile(archive)
        self.names=set(self.zip.namelist())
        if len(self.names)!=len(self.zip.infolist()) or len(self.names)!=s['member_count']:
            raise ValueError('ambiguous R750 member identities')
        self.prefix=''
        self.meta=self.document('input-identity.json',s['selected_documents']['input-identity']['sha256'])
        self.ident=engine.digest(engine.plain(self.meta).encode())
        if self.ident!=INPUT:raise ValueError('different original R750 semantic input')
        if set(engine.FILES)-set(new_files)!=set(self.meta['sha256']):
            raise ValueError('different R750 physical source closure')
        for name,h in self.meta['sha256'].items():
            if stream_digest(HERE/name)!=h:raise ValueError('changed R750 original physical source: '+name)
        if (self.meta['python'],self.meta['numpy'],self.meta['scipy'])!=(platform.python_version(),np.__version__,scipy.__version__):
            raise ValueError('restore the actual R750 scientific versions')
        self.terminal=self.document('terminal.json',s['terminal_sha256'])
        self.state=self.document('continuation.json',s['continuation_sha256'])
        self.source_id=self.document('source-identity.json',s['source_identity_sha256'])
        self.records=self.state['records'];self.level=int(self.meta['settings']['level'])
        if (self.terminal['input_identity']!=INPUT or self.terminal['run'].split('-')[0]!=RUN or
                self.terminal['finished_phase_records']!=len(self.records)):
            raise ValueError('R750 terminal, current trajectory and original file identities differ')

    def document(self,name,sha):
        raw=self.zip.read(self.prefix+name)
        if hashlib.sha256(raw).hexdigest()!=sha:raise ValueError('different R750 member '+name)
        return json.loads(raw)

    def key(self,kind,key):
        semantic=[self.ident,kind,key]
        name=self.engine.digest(self.engine.plain(semantic).encode())
        return self.prefix+'paid/'+kind+'-'+name+'.npz',semantic

    def has(self,kind,key):
        return self.key(kind,key)[0] in self.names

    def receipt(self,kind,key):
        name,semantic=self.key(kind,key);sha=hashlib.sha256()
        with self.zip.open(name) as source,tempfile.SpooledTemporaryFile(max_size=8*2**20) as copy:
            for chunk in iter(lambda:source.read(2**20),b''):
                sha.update(chunk);copy.write(chunk)
            stamp=sha.hexdigest()
            if self.bytes_sha.setdefault(name,stamp)!=stamp:raise ValueError('R750 parent member changed')
            copy.seek(0)
            with np.load(copy,allow_pickle=False) as record:
                header=json.loads(record['meta'].tobytes())
                if header['semantic']!=json.loads(self.engine.plain(semantic)):
                    raise ValueError('R750 original semantic key mismatch')
                return self.engine.Pack.decode(header['tree'],record)

    def warm(self,phase):
        candidates=[(r['degree'],r['q_values'],r['q']) for r in self.records if r['phase']==phase]
        current=self.state.get('current',{})
        if current.get('phase')==phase:candidates.append((current['degree'],self.state['current_q'],current['q']))
        if not candidates:return None
        degree,values,ident=candidates[-1];vec=np.asarray(values,float)
        if self.engine.array_id(vec)!=ident or vec.size!=3*len(original.tags(degree)):
            raise ValueError('R750 paid coefficient vector disagrees with the archive')
        return degree,vec


def part_angles(piece,columns):
    cols=np.asarray(columns,dtype=int)
    nr,ns=piece['shape'];idx=(np.arange(nr)[:,None]*ns+cols).ravel()
    raw=csr_matrix((piece['data'],piece['indices'],piece['indptr']),shape=(nr*ns,piece['nterm']))[idx]
    return dict(shape=(nr,len(cols)),ns=len(cols),ss=piece['ss'][cols],weights=piece['weights'],
          goals=piece['goals'][cols],physical_source_inner=piece['physical_source_inner'][cols],
          inner_displacement=piece['inner_displacement'][cols],matrix=piece['matrix'][idx],pr=piece['pr'][idx],
          nterm=piece['nterm'],data=raw.data,indices=raw.indices,indptr=raw.indptr)


def join_angles(parts,requested):
    from scipy.sparse import vstack
    if len(parts)==1 and np.array_equal(parts[0]['ss'],requested):return parts[0]
    ss=np.concatenate([p['ss'] for p in parts]);ind=np.argsort(ss)
    if not np.array_equal(ss[ind],requested):raise ValueError('incomplete or duplicate R760 material angle partition')
    nr=parts[0]['shape'][0];nterm=parts[0]['nterm'];ns=len(ss)
    for p in parts:
        if p['nterm']!=nterm or p['shape'][0]!=nr or not np.array_equal(p['weights'],parts[0]['weights']):
            raise ValueError('cannot join different physical radial rules')
    relative=(np.arange(nr)[:,None]*ns+ind).ravel()
    # Concatenation of actual CSR chunks stores each entire radial-by-angle cube.
    grouped=np.concatenate([(np.arange(nr)[:,None]*ns+
                      (sum(x['ns'] for x in parts[:j])+np.arange(p['ns']))).ravel() for j,p in enumerate(parts)])
    back=np.argsort(grouped)[relative]
    matrices=np.concatenate([p['matrix'] for p in parts])[back];pr=np.concatenate([p['pr'] for p in parts])[back]
    raw=vstack([csr_matrix((p['data'],p['indices'],p['indptr']),shape=(nr*p['ns'],nterm)) for p in parts],format='csr')[back]
    return dict(shape=(nr,ns),ns=ns,ss=ss[ind],weights=parts[0]['weights'],matrix=matrices,pr=pr,nterm=nterm,
             data=raw.data,indices=raw.indices,indptr=raw.indptr,
             **{k:np.concatenate([p[k] for p in parts])[ind] for k in ('goals','physical_source_inner','inner_displacement')},
             **{k:sum(p[k] for p in parts) for k in ('original_geometry_and_coefficient_rows','new_material_rows')})
