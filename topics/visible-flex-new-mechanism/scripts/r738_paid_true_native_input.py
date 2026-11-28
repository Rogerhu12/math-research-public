"""Source identity and durable negative-cell bookkeeping for the R738 public solver."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import time
import numpy as np
import scipy
from r728_closed_spinor_continuation_20261128 import PaidBook,PaidPause
from r738_negative_tail_and_macro_source import SIGNS,MODES,checked_line,propagated_curve
from r738_real_macro_reference import Base
from r738_deep_cap_bounds import deep_cost
from r738_macro_spline_space import PhysicalFields


class SolveBook(PaidBook):
    def __init__(self,opt,limit,elapsed,counts):
        self.hashlib,self.os,self.elapsed,self.counts=hashlib,os,elapsed,counts
        self.limit,self.reserve=limit,opt['reserve_seconds']
        tmp=Path(os.environ['RUNNER_TEMP']);self.root=tmp/'r738-paid'
        self.root.mkdir(parents=True,exist_ok=True)
        self.ledger_file=self.root/'ledger.json'
        req=json.loads(Path(os.environ['R738_REQUEST']).read_bytes())
        sources={k:v for k,v in req['source_sha256'].items() if k.endswith('.py')}
        semantic=dict(schema='r738-native-v1',sources=sources,geometry=opt,runtime=[np.__version__,scipy.__version__])
        identity=hashlib.sha256(json.dumps(semantic,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        if self.ledger_file.exists():
            self.ledger=json.loads(self.ledger_file.read_bytes())
            if self.ledger.get('fingerprint')!=identity:raise ValueError('R738 checkpoint does not match the real problem.')
            counts.update(self.ledger['counts'])
        else:
            self.ledger=dict(schema='r738-native-v1',fingerprint=identity,semantic=semantic,kept={},retired={},
                 counts={},unit_max_seconds={},runs=[],cumulative_seconds=0.,latest_state=None,pending=None,context={})
        self.prior_seconds=self.ledger['cumulative_seconds']
        self.ledger['runs'].append(dict(id=os.environ['GITHUB_RUN_ID'],attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
                                    source=os.environ['GITHUB_SHA'],opening_paid_seconds=self.prior_seconds))
        self.flush()
    def source(self,meta):
        for name,sha in [('r734-original-tail.jsonl',meta['journal_sha256']),('r734-original-final.json',meta['terminal_sha256'])]:
            dest=self.root/name
            if not dest.exists():shutil.copyfile(Path(os.environ['RUNNER_TEMP'])/name,dest)
            if self.digest(dest)!=sha:raise ValueError('Incorrect preserved R734 source '+name)
        raw=(self.root/'r734-original-final.json').read_bytes()
        if len(raw)!=144011:raise ValueError('Incorrect original R734 literal length.')
        q=json.loads(raw);old={}
        for text in (self.root/'r734-original-tail.jsonl').read_text().splitlines():
            j=json.loads(text)
            if j['key'] in old or j['scientific_fingerprint']!=meta['scientific_fingerprint']:raise ValueError('Mixed R734 journal.')
            old[j['key']]=j['value']
        if len(old)!=q['paid_units'] or len(old)!=8558 or q['kind']!='terminal' or q['source_fingerprint']!=meta['scientific_fingerprint']:
            raise ValueError('Incomplete original natural tail.')
        return q,old


class TailBook:
    def __init__(self,book,old):
        self.book=book;self.records=dict(old)
        path=book.root/'r738-negative-and-deep.jsonl'
        if path.exists():
            for txt in path.read_text().splitlines():
                row=json.loads(txt)
                if row['key'] in self.records or row['identity']!=book.ledger['fingerprint']:raise ValueError('Mixed R738 native-tail journal.')
                self.records[row['key']]=row['value']
        self.out=path.open('a',buffering=1)
    def once(self,key,fn):
        if key in self.records:return self.records[key]['data']
        b=self.book
        if b.elapsed()+b.reserve+3>=b.limit:
            b.ledger['pending']=dict(key=key,unit='actual_native_interval',context=b.ledger['context']);b.flush()
            raise PaidPause(key)
        a=time.monotonic();data=fn()
        row=dict(data=data,seconds=time.monotonic()-a)
        self.out.write(json.dumps(dict(identity=b.ledger['fingerprint'],key=key,value=row),allow_nan=False,separators=(',',':'))+'\n')
        self.records[key]=row;b.counts['new_interval_and_deep_units']+=1
        return data


class NativeBook:
    def __init__(self,b):self.b=b
    def once(self,key,fn):
        return self.b.once(key,'actual_native',fn)


def source_fields(book,opt,counts,emit):
    q,old=book.source(opt['paid_r734']);jb=TailBook(book,old);nb=NativeBook(book)
    # The incremental journal itself determines the exact number of accepted interval units on a resume.
    counts['new_interval_and_deep_units']=len(jb.records)-len(old)
    native=[{},{}];cost=[];ports={};scales=[]
    for s in SIGNS:
        row=[];costrow=[]
        for j in MODES:
            book.locate(action='genuine_negative_cells_and_retained_complete_cap',side=s,j=j)
            port=checked_line(q,s,j,jb,opt['cell_depth'])
            if not port['available']:
                raise ArithmeticError('New negative-cell projective direction unavailable '+str(port))
            c=jb.once(f'whole_deep_{s}_{j}',lambda:deep_cost(s,j,port,old,jb))
            # Scale measured cut data; the full omitted cap separately gets its actual nonlinear hard guard.
            peak=max(1.,*(abs(float(z)) for z in port['f_0_1_2'][2]))
            scale=1/peak
            if not np.isfinite(scale) or scale<=0:raise ArithmeticError('Invalid full-column physical scale.')
            row.append(scale);costrow.append(c);ports[str((s,j))]=port
            for i,tol in enumerate(opt['native_tolerances']):
                native[i][s,j]=propagated_curve(q,j,s,-1,float(tol),counts,nb)
        scales.append(row);cost.append(costrow)
    info=dict(original_fingerprint=q['source_fingerprint'],original_paid_units=len(old),
              original_public_elapsed=q['current_elapsed_seconds'],actual_new_ports=ports,actual_deep_cap_cost=cost,
              true_amplitude_scale=scales)
    book.once('complete_tail_source','metadata',lambda:info)
    emit('actual_source_ports',**info)
    b=[Base(k,nb,counts) for k in opt['base_orders']]
    fields=[PhysicalFields(b[i],native[i],counts) for i in range(2)]
    return fields,[PhysicalFields(b[1],native[1],counts,i) for i in (0,2)],np.asarray(scales),cost
