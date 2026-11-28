"""Resume the frozen R760 field with occurrence-aware material Gauss transfer and all twelve original receipts."""
import argparse
from collections import defaultdict, deque
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import time
from types import FunctionType, SimpleNamespace
import zipfile


HERE = Path(__file__).resolve().parent
FIRST_RUN = '46181796301'
FIRST_JOB = 141092792865
FIRST_HEAD = 'd2414100f68ed127210d746d59d064a0c5278eb0'
FIRST_ARTIFACT = 15277979068
FIRST_SIZE = 57530937
FIRST_SHA = '4b6e60590fcd6612cbcf05ab95f27df2f839a803392aec258b574209847370fc'
FIRST_INPUT = '19e2aa6665a8843ac23a5c05615a0674985fab2f7aca8d420a4330fb830d1404'
FIRST_TERMINAL = '9d9315be84e0da3866fe4380d0050016f921fc923f03314cec5c618cfefe7635'
FIRST_CONTINUATION = '65e08a296d54eb6c07b5889317d67e58bb9df3258dadacb2d27d4840297d9082'
EXPECTED = {'native_frame':2, 'native_nodes':2, 'r750_actual_release_probe':1, 'r750_ray_rule':1,
            'r760_actual_full_terminal_moments':1, 'r760_curl_rows':1, 'r760_full_native_seed_jets':2,
            'r760_meridian_phase_parameter':2}
OLD_ERROR = "ValueError('R760 original and refined material quadratures must be strictly increasing')"


def plain(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for part in iter(lambda:f.read(2**20), b''): h.update(part)
    return h.hexdigest()


def atomic(path, raw):
    path.parent.mkdir(exist_ok=True, parents=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as f:
        temp=Path(f.name)
        try:f.write(raw)
        except BaseException:
            temp.unlink(missing_ok=True); raise
    os.replace(temp,path)


def write_json(path,value):
    atomic(path,(plain(value)+'\n').encode())


def rule_identity(rule):
    import numpy as np
    arrays={}
    for name in ('cuts','radius','weights'):
        a=np.asarray(rule[name])
        if a.ndim!=1 or a.dtype!=np.dtype('float64') or not np.isfinite(a).all():
            raise ValueError('incomplete original float64 Gauss rule')
        arrays[name]={'sha256':sha(np.ascontiguousarray(a).tobytes()),'length':len(a)}
    return dict(order=int(rule['order']),anchor=float(rule['anchor']),**arrays)


def occurrences(old,new):
    """Return two separate maps. Geometry may repeat a donor; a weighted contribution never does."""
    import numpy as np
    before,after=rule_identity(old),rule_identity(new)
    if before['order']!=after['order'] or before['anchor']!=after['anchor']:
        raise ValueError('different true R750 radial anchors or Gauss orders')
    n=int(old['order'])
    for p in (old,new):
        cuts,r,w=(np.asarray(p[k]) for k in ('cuts','radius','weights'))
        if (n<1 or len(cuts)<2 or not np.all(np.diff(cuts)>0.) or
                len(r)!=(len(cuts)-1)*n or len(w)!=len(r) or not np.all(w>0.)):
            raise ValueError('invalid positive-weight material Gauss panels')
    x,xx=old['radius'],new['radius'];w,ww=old['weights'],new['weights']
    # The actual panels are identified by the two stored endpoints. A Gauss
    # ordinal within such a panel retains its identity even for tied abscissae.
    panels={(float(a),float(b)):i for i,(a,b) in enumerate(zip(old['cuts'][:-1],old['cuts'][1:],strict=True))}
    weighted=np.full(len(xx),-1,dtype=np.int64);consumed=np.zeros(len(x),dtype=bool)
    for i,ends in enumerate(zip(new['cuts'][:-1],new['cuts'][1:],strict=True)):
        j=panels.get(tuple(map(float,ends)))
        if j is None:continue
        ii=np.arange(i*n,(i+1)*n);jj=np.arange(j*n,(j+1)*n)
        same=(xx[ii]==x[jj]) & (ww[ii]==w[jj])
        weighted[ii[same]]=jj[same];consumed[jj[same]]=True
    from_same_panel=int(consumed.sum())
    pool=defaultdict(deque)
    for j in np.flatnonzero(~consumed):pool[(float(x[j]),float(w[j]))].append(int(j))
    for i in np.flatnonzero(weighted<0):
        matches=pool.get((float(xx[i]),float(ww[i])))
        if matches:weighted[i]=matches.popleft()
    ci=np.flatnonzero(weighted>=0);co=weighted[ci]
    if len(np.unique(co))!=len(co) or not np.array_equal(xx[ci],x[co]) or not np.array_equal(ww[ci],w[co]):
        raise ArithmeticError('original weighted occurrence was used twice or changed')
    # Remaining new rows may still borrow Pr/B/etc. at a genuinely identical
    # radius, including a radius already used by another geometric row.
    at={}
    for j,r in enumerate(x):at.setdefault(float(r),j)
    geometry=weighted.copy()
    for i in np.flatnonzero(geometry<0):geometry[i]=at.get(float(xx[i]),-1)
    gi=np.flatnonzero(geometry>=0);go=geometry[gi]
    if not np.array_equal(xx[gi],x[go]):raise ArithmeticError('unequal physical geometry labels')
    def diagnostics(rule):
        raw=rule['radius'];_,cnt=np.unique(raw,return_counts=True)
        ids=np.flatnonzero(np.diff(raw)<=0.)
        return dict(rows=len(raw),distinct_radii=len(cnt),repeated_occurrences=int(sum(cnt-1)),
                    maximum_multiplicity=int(max(cnt)),nonincreasing_adjacent_rows=len(ids),
                    first_nonincreasing=[dict(index=int(i),old_radius=float(raw[i]),next_radius=float(raw[i+1]),
                      old_weight=float(rule['weights'][i]),next_weight=float(rule['weights'][i+1])) for i in ids[:8]])
    return dict(old=before,new=after,old_ordered_diagnostic=diagnostics(old),new_ordered_diagnostic=diagnostics(new),
                conserved_new=ci.tolist(),conserved_old=co.tolist(),geometry_new=gi.tolist(),geometry_old=go.tolist(),
                same_panel_and_ordinal=from_same_panel,other_equal_weight_occurrences=len(ci)-from_same_panel,
                geometry_only_occurrences=len(gi)-len(ci))


class Maps:
    def __init__(self,root):
        self.root=root/'gauss-occurrences';self.cache={}

    def read(self,old,new,geometry):
        import numpy as np
        ident=[rule_identity(old),rule_identity(new)]
        key=sha(plain(ident).encode())
        if key not in self.cache:
            path=self.root/(key+'.json')
            if path.is_file():
                data=json.loads(path.read_text())
                if [data['old'],data['new']]!=ident:raise ValueError('different material rules in occurrence receipt')
            else:
                data=occurrences(old,new)
                write_json(path,data)
            packed={}
            for which in ('geometry','conserved'):
                ci=np.asarray(data[which+'_new'],dtype=np.int64);co=np.asarray(data[which+'_old'],dtype=np.int64)
                if (ci.shape!=co.shape or np.any(ci<0) or np.any(ci>=len(new['radius'])) or np.any(co<0)
                        or np.any(co>=len(old['radius'])) or np.any(np.diff(ci)<=0)
                        or not np.array_equal(new['radius'][ci],old['radius'][co])):
                    raise ValueError('invalid stored material occurrence map')
                if which=='conserved' and (len(np.unique(co))!=len(co)
                        or not np.array_equal(new['weights'][ci],old['weights'][co])):
                    raise ValueError('invalid stored one-to-one weighted map')
                packed[which]=(ci,co)
            self.cache[key]=packed
        return self.cache[key]['geometry' if geometry else 'conserved']


def decode_meta(raw):
    import numpy as np
    a=np.load(io.BytesIO(raw),allow_pickle=False)
    if a.ndim!=1 or a.dtype!=np.uint8:raise ValueError('invalid original paid header')
    data=a.tobytes()
    if not raw.endswith(data):raise ValueError('unexpected original paid .npy header')
    return json.loads(data),data


def remap(inner,destination,oldsem,newsem):
    """Copy each .npy byte stream. Change only the 64 ASCII bytes of the semantic source identity."""
    source_hasher={}
    with zipfile.ZipFile(io.BytesIO(inner)) as prior:
        entries=prior.infolist()
        if len({x.filename for x in entries})!=len(entries) or sum(x.filename=='meta.npy' for x in entries)!=1:
            raise ValueError('ambiguous original paid NPZ')
        head=prior.read('meta.npy')
        obj,data=decode_meta(head)
        if obj['semantic']!=oldsem:raise ValueError('wrong original R760 paid object')
        token=b'"semantic":["'+oldsem[0].encode()+b'",'
        replacement=b'"semantic":["'+newsem[0].encode()+b'",'
        if data.count(token)!=1 or len(token)!=len(replacement):raise ValueError('ambiguous paid input identity')
        now=data.replace(token,replacement)
        if json.loads(now)!={**obj,'semantic':newsem}:raise ValueError('non-identity bytes changed in paid metadata')
        with tempfile.NamedTemporaryFile(dir=destination.parent,delete=False) as tmp:
            temp=Path(tmp.name)
        try:
            with zipfile.ZipFile(temp,'w') as out:
                for member in entries:
                    if member.filename=='meta.npy':
                        out.writestr(copy.copy(member),head[:-len(data)]+now);continue
                    if not member.filename.endswith('.npy') or '/' in member.filename:
                        raise ValueError('unexpected original numerical member')
                    h=hashlib.sha256()
                    with prior.open(member) as a,out.open(copy.copy(member),'w') as b:
                        for chunk in iter(lambda:a.read(2**20),b''):
                            h.update(chunk);b.write(chunk)
                    source_hasher[member.filename]=h.hexdigest()
            digest=file_sha(temp)
            if destination.exists():
                if file_sha(destination)!=digest:raise ValueError('different saved object at migrated semantic key')
            else:os.replace(temp,destination)
        finally:temp.unlink(missing_ok=True)
    return digest,source_hasher


def migrate(root,source):
    start=time.monotonic()
    archive=Path(source)
    if archive.stat().st_size!=FIRST_SIZE or file_sha(archive)!=FIRST_SHA:
        raise ValueError('different first natural R760 artifact')
    root.mkdir(parents=True,exist_ok=True);paid=root/'paid';paid.mkdir(exist_ok=True)
    memo=root/'r760-first-checkpoint-inheritance.json'
    with zipfile.ZipFile(archive) as first:
        names=first.namelist()
        if len(names)!=20 or len(set(names))!=len(names):raise ValueError('different first R760 member set')
        raw=first.read('input-identity.json');meta=json.loads(raw)
        if sha(plain(meta).encode())!=FIRST_INPUT:raise ValueError('different first R760 mathematical input')
        for name,digest in meta['sha256'].items():
            if Path(name).name!=name or file_sha(HERE/name)!=digest:raise ValueError('changed frozen R760 scientific source')
        wrapper=Path(__file__).name
        after={**meta,'sha256':{**meta['sha256'],wrapper:file_sha(HERE/wrapper)}}
        child=sha(plain(after).encode())
        ip=root/'input-identity.json'
        if ip.exists() and json.loads(ip.read_text())!=after:raise ValueError('refusing the state of another calculation')
        write_json(ip,after)
        if memo.is_file():
            receipt=json.loads(memo.read_text())
            if (receipt['child_identity']!=child or receipt['parent_identity']!=FIRST_INPUT
                    or receipt['artifact_sha256']!=FIRST_SHA or receipt['saved_kind_counts']!=EXPECTED):
                raise ValueError('changed R760 inheritance receipt')
            for record in receipt['units']:
                if file_sha(paid/record['new_file'])!=record['new_file_sha256']:
                    raise ValueError('the migrated scientific object is missing or changed')
            return child
        terminal=first.read('terminal.json');previous=first.read('continuation.json')
        result=json.loads(terminal);state=json.loads(previous)
        if (sha(terminal)!=FIRST_TERMINAL or sha(previous)!=FIRST_CONTINUATION
                or result['input_identity']!=FIRST_INPUT or result['run'].split('-')[0]!=FIRST_RUN
                or result['error']!=OLD_ERROR or result['active_operation']['kind']!='r750_true_ray_kernel'
                or state['phase_index']!=0 or state['accepted']!=0 or state.get('current') is not None):
            raise ValueError('first R760 terminal and restart fields do not match')
        allcost=first.read('cost.jsonl')
        events=[json.loads(line) for line in allcost.splitlines()];saved=[r for r in events if r['event']=='saved']
        failed=[r for r in events if r['event']=='failed']
        if len(failed)!=1 or failed[0]['kind']!='r750_true_ray_kernel':raise ValueError('different first R760 unpaid unit')
        counts={};original_names=set();units=[]
        for item in saved:
            kind,key=item['kind'],item['key']
            oldsem=[FIRST_INPUT,kind,key];newsem=[child,kind,key]
            oldname=kind+'-'+sha(plain(oldsem).encode())+'.npz'
            newname=kind+'-'+sha(plain(newsem).encode())+'.npz'
            if kind not in EXPECTED or item['file']!=oldname or oldname in original_names:
                raise ValueError('unknown or repeated original scientific receipt')
            original_names.add(oldname);counts[kind]=counts.get(kind,0)+1
            oldbytes=first.read('paid/'+oldname)
            if len(oldbytes)!=item['bytes']:raise ValueError('original paid byte count differs')
            stamp,arrays=remap(oldbytes,paid/newname,oldsem,newsem)
            units.append(dict(kind=kind,key=key,old_file=oldname,old_file_sha256=sha(oldbytes),
                       new_file=newname,new_file_sha256=stamp,identical_array_sha256=arrays))
        if counts!=EXPECTED or original_names!={x[5:] for x in names if x.startswith('paid/')}:
            raise ValueError('failed to inherit every successful original R760 object')
        for name in names:
            if name.startswith('paid/'):continue
            if Path(name).name!=name and name!='transport/46181796301-1.json':
                raise ValueError('unexpected first R760 administrative path')
            atomic(root/'r760-first-original'/name,first.read(name))
        resume=root/'continuation.json'
        if resume.exists() and resume.read_bytes()!=previous:raise ValueError('unregistered continuation during first migration')
        if not resume.exists():atomic(resume,previous)
        write_json(memo,dict(parent_identity=FIRST_INPUT,child_identity=child,artifact=FIRST_ARTIFACT,
             run=FIRST_RUN,job=FIRST_JOB,head=FIRST_HEAD,artifact_sha256=FIRST_SHA,
             saved_kind_counts=counts,units=units,source_scientific_cost=result['all_archived_cost'],
             source_wall_seconds=result['this_allocation_wall_seconds'],
             source_archive_seconds=result['this_allocation_archive_seconds'],original_failed_operation=result['active_operation'],
             new_scientific_evaluations=0,administrative_seconds=time.monotonic()-start))
        return child


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or not os.environ.get('GITHUB_RUN_ID','').isdigit()
            or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise SystemExit('R760 recovery runs on the public research Actions runner')
    p=argparse.ArgumentParser(add_help=False);p.add_argument('--first-checkpoint-zip',required=True)
    original,args=p.parse_known_args()
    q=argparse.ArgumentParser(add_help=False);q.add_argument('--state',default='r760-paid-state')
    q.add_argument('--parent-zip',required=True)
    current,_=q.parse_known_args(args)
    state=Path(current.state);child=migrate(state,original.first_checkpoint_zip)
    import r760_relative_material_rows as rows
    import r760_conserved_quadratures as conserved
    import r760_two_boundary_solver as entry
    maps=Maps(state)
    rows.matched_rows=lambda a,b:maps.read(a,b,True)
    # The original integral routine is unmodified except its injected row map.
    # Its extra old/new/weights/orientation/control checks still run.
    action=conserved.pair
    namespace={**action.__globals__,'rows':SimpleNamespace(matched_rows=lambda a,b:maps.read(a,b,False))}
    conserved.pair=FunctionType(action.__code__,namespace,action.__name__,action.__defaults__,action.__closure__)
    entry.NEW=(*entry.NEW,Path(__file__).name)
    print('R760_GAUSS_INHERITED',plain(dict(parent=FIRST_INPUT,child=child,counts=EXPECTED)),flush=True)
    sys.argv=[sys.argv[0],*args]
    entry.main()


if __name__=='__main__':main()
