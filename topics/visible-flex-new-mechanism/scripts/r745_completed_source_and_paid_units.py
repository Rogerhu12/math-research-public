"""Typed paid units for one genuine R745 geometry; immutable source receipts are verified before use."""
import hashlib
import json
import os
from pathlib import Path
import time
from collections import ChainMap
import numpy as np
import scipy
from r728_closed_spinor_continuation_20261128 import PaidBook,PaidPause
from r738_negative_tail_and_macro_source import propagated_curve,checked_line,SIGNS
from r745_three_broad_valleys import port_data


class Donor(PaidBook):
    def __init__(self,path,ledger):
        self.root=path;self.ledger=ledger;self.hashlib=hashlib
    def once(self,key,fn):
        if not self.has(key):raise ValueError('Missing already charged R738 DOP source '+key)
        return self.load(key)


class Journal(PaidBook):
    def __init__(self,opt,limit,elapsed,counts,req):
        self.hashlib,self.os,self.elapsed,self.counts=hashlib,os,elapsed,counts
        self.limit,self.reserve=limit,opt['reserve_seconds']
        self.root=Path(os.environ['RUNNER_TEMP'])/'r745-paid';self.root.mkdir(exist_ok=True)
        self.ledger_file=self.root/'ledger.json'
        sources={k:v for k,v in req['source_sha256'].items() if k.endswith('.py')}
        semantic=dict(schema='r745-valleys-v1',sources=sources,geometry=opt,paid_sources=req['completed_sources'],
                       runtime=[np.__version__,scipy.__version__])
        fid=hashlib.sha256(json.dumps(semantic,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        if self.ledger_file.exists():
            self.ledger=json.loads(self.ledger_file.read_bytes())
            if self.ledger.get('fingerprint')!=fid:raise ValueError('R745 paid object changed.')
            counts.update(self.ledger['counts'])
        else:self.ledger=dict(schema='r745-valleys-v1',fingerprint=fid,semantic=semantic,kept={},retired={},
                   counts={},unit_max_seconds={},runs=[],cumulative_seconds=0.,latest_state=None,pending=None,context={})
        self.prior_seconds=self.ledger['cumulative_seconds']
        self.ledger['runs'].append(dict(id=os.environ['GITHUB_RUN_ID'],attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),source=os.environ['GITHUB_SHA']))
        file=self.root/'directed.jsonl';self.directed={}
        if file.is_file():
            for line in file.read_bytes().splitlines():
                z=json.loads(line)
                if z['fingerprint']!=fid or z['key'] in self.directed:raise ValueError('Duplicate/different directed unit.')
                self.directed[z['key']]=z['value']
        self.out=file.open('a',buffering=1)
        self.counts['new_directed_units']=len(self.directed);self.flush()
    def once(self,key,unit,fn=None):
        if fn is None:fn,unit=unit,'directed_cell'
        if unit!='directed_cell':return super().once(key,unit,fn)
        if key in self.records:return self.records[key]['data']
        if self.elapsed()+self.reserve+2>=self.limit:
            self.ledger['pending']=dict(key=key,unit=unit,context=self.ledger['context']);self.flush()
            raise PaidPause(key)
        start=time.monotonic();v=fn()
        z=dict(data=v,seconds=time.monotonic()-start)
        self.out.write(json.dumps(dict(key=key,value=z,fingerprint=self.ledger['fingerprint']),separators=(',',':'),allow_nan=False)+'\n')
        self.directed[key]=z;self.counts['new_directed_units']+=1
        return v


def actual_sources(book,req,opt,counts):
    root=Path(os.environ['RUNNER_TEMP'])/'r745-sources'
    spec=req['completed_sources']
    for name,v in spec['files'].items():
        if name.startswith('/') or '..' in Path(name).parts:raise ValueError('Bad administrative member.')
        p=root/name
        if p.stat().st_size!=v['bytes'] or book.digest(p)!=v['sha256']:raise ValueError('Incorrect completed source '+name)
    required=('r738/ledger.json','r738/r738-negative-and-deep.jsonl','r738/r734-original-tail.jsonl',
               'r738/r734-original-final.json','r735-central.jsonl','r735-final.json','r738-final.json')
    if not all(k in spec['files'] for k in required):raise ValueError('Incomplete list of bound manifests.')
    orig=json.loads((root/required[3]).read_bytes());thin=json.loads((root/required[5]).read_bytes())
    ledger=json.loads((root/required[0]).read_bytes());wide=json.loads((root/required[6]).read_bytes())
    if (orig['source_fingerprint']!='49974e9a223b472eae325e552d99c16880a2fb2d4dd98147e04af31141d24eb6'
       or thin['new_fingerprint']!='da2a68f42a7fbe5d35b294c1badd34dbd76a489e3842dda56596eeb9669c8618'
       or wide['fingerprint']!=ledger['fingerprint'] or wide['kind'] not in ('terminal','paid_partial')):
        raise ValueError('Sources are not the specified naturally completed fields.')
    def records(fn,field,identity):
        z={}
        for line in (root/fn).read_bytes().splitlines():
            a=json.loads(line);k=a['key']
            if a[field]!=identity or k in z:raise ValueError('Wrong donor journal.')
            z[k]=a['value']
        return z
    old=records(required[2],'scientific_fingerprint',orig['source_fingerprint'])
    new=records(required[1],'identity',ledger['fingerprint'])
    high=records(required[4],'fingerprint',thin['new_fingerprint'])
    if len(old)!=orig['paid_units'] or len(high)!=thin['total_new_units']:raise ValueError('Missing completed operator rows.')
    for key in set(new)&set(high):
        if new[key]['data']!=high[key]['data']:raise ValueError('Conflicting inherited R735 and R738 rows.')
    book.records=ChainMap(book.directed,new,high,old)
    donor=Donor(root/'r738',ledger)
    complete=donor.once('complete_tail_source',None)
    ports=port_data(orig,new)
    for (s,j),v in ports.items():
        if v!=complete['actual_new_ports'][str((s,j))]:raise ValueError('Restored physical R738 two-jets differ.')
    native={}
    for s in SIGNS:
        for j in (2,3):
            native[s,j]=propagated_curve(orig,j,s,-1,opt['donor_native_tolerance'],counts,donor)
    history=dict(r734_units=len(old),r734_elapsed=orig['current_elapsed_seconds'],r735_units=len(high),
                 r735_elapsed=thin['current_elapsed_seconds'],r738_cumulative_seconds=ledger['cumulative_seconds'],
                 r738_counts=ledger['counts'],r738_fingerprint=ledger['fingerprint'],r738_global_status=wide['kind'],
                 exact_completed_sources=spec)
    return orig,thin,old,new,ports,native,history


def higher_modes(book,orig,ports,depth):
    for s in SIGNS:
        for j in (4,5,6):
            side='inner' if s==-1 else 'outer';z=book.records[f'side{s}_m{j}_n0_accepted_line']['data']
            # The original R735 true stable j>=4 cut line is already paid at cell zero.
            raw=dict(completed_modes={side+str(j):dict(kind='certified_tail_port',
                         paid_outer_lines=[dict(cell=0,line=z['line'])])})
            v=checked_line(raw,s,j,book,depth)
            if not v['available']:return False
            ports[s,j]=v
    return True
