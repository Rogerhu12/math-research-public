#!/usr/bin/env python3
"""Reduce already closed normal tiles using only NumPy and small NPZ pieces.

This is a new explicitly identified transport, NOT the original saver.
Every numeric entry is summed in the original tile ordinal order. Each
piece is immediately durable, and actual consumers reconstruct the exact
original elimination map. No geometry, F/J, scale, damping or QP here.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import argparse,datetime,hashlib,io,json,shutil,struct,subprocess,sys,tempfile,time
from pathlib import Path
from collections import Counter


def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)
def source(p):
    p=Path(p);b=p.read_bytes();return dict(name=p.name,bytes=len(b),sha256=sha(b))
def identity(p):
    p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=sha(b))
def write(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+'.writing')
    tmp.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n');tmp.replace(p)
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def decode(v):
    tag=v[0]
    if tag=='none':return None
    if tag=='bool':return bool(v[1])
    if tag=='str':return v[1]
    if tag=='int':return int(v[1])
    if tag=='float64-bits':return struct.unpack('>d',bytes.fromhex(v[1]))[0]
    if tag in ('list','tuple'):return [decode(x) for x in v[1]]
    if tag=='dict':return {k:decode(x) for k,x in v[1]}
    if tag in ('numpy-scalar','small-numpy-array'):
        import numpy as np
        d=v[1];a=np.frombuffer(bytes.fromhex(v[2]),dtype=np.dtype(d['dtype'])).copy().reshape(d['shape'])
        return a[()] if tag=='numpy-scalar' else a
    raise ValueError('Unsupported exact typed metadata')
def encode(v):
    if v is None:return ['none']
    if type(v) is bool:return ['bool',v]
    if type(v) is int:return ['int',str(v)]
    if type(v) is float:return ['float64-bits',struct.pack('>d',v).hex()]
    if type(v) is str:return ['str',v]
    if type(v) is list:return ['list',[encode(x) for x in v]]
    if type(v) is dict:return ['dict',[[k,encode(x)] for k,x in v.items()]]
    raise TypeError('Only explicit Python JSON types in newly written aggregate metadata')
def array_id(a):
    import numpy as np
    a=np.asarray(a);b=np.ascontiguousarray(a).tobytes()
    return dict(shape=list(a.shape),dtype=a.dtype.str,bytes=len(b),sha256=sha(b))


def index_inputs(request):
    req=json.loads(Path(request).read_text());root=Path(req['cache_dir'])
    path=root/'normal-piece-reduction'/'input-index.json'
    if path.exists():return root,json.loads(path.read_text())
    baseline=json.loads((root/'baseline-summary.json').read_text())
    if baseline['binding']['input_npz_sha256']!=req['input_sha256']:raise ValueError('Wrong actual input state')
    plan=json.loads((root/'normal-partition-plan.json').read_text())
    nodes=[];cells=[];inside=[];boundaries=0;ids=[];state=None;summaries=[];rows=blocks=0;r2=0.;groups=Counter();template=None;common=None
    for descriptor in plan['tiles']:
        nodes.extend(descriptor['node_indices']);cells.extend(descriptor['cell_indices']);inside.extend(descriptor['interior_cells']);boundaries+=int(descriptor['include_boundary'])
        p=root/'normal-tiles'/descriptor['id']/'manifest.json';m=json.loads(p.read_text())
        if m['schema']!='fd2d-lossless-local-normal-checkpoint-v1' or not m['complete'] or m['directory_name']!=p.parent.name:raise ValueError('Unclosed tile')
        if m['binding']['descriptor']!=descriptor or m['binding_sha256']!=sha(canonical(m['binding']).encode()):raise ValueError('Different tile binding')
        if m['metadata_sha256']!=sha(canonical(m['metadata']).encode()):raise ValueError('Corrupt actual typed tile metadata')
        if template is None:template=m;common=m['binding']['common']
        if (m['mapping']!=template['mapping'] or m['mapping_sha256']!=template['mapping_sha256']
                or m['binding']['common']!=common or m['source']!=template['source']
                or m['original_normal_source']!=template['original_normal_source']):raise ValueError('Tile map/source/goal differs')
        for s in (m['source'],m['original_normal_source']):
            if source(Path(__file__).parent/s['name'])!=s:raise ValueError('Original closed source changed')
        meta={k:decode(v) for k,v in m['metadata'].items()};info=meta['info']
        if (info.get('complete_tile') is not True or info.get('full_finite_objective') is not False
                or info['tile_descriptor']!=descriptor or info['scaling_or_damping_applied'] is not False
                or info['state_binding_sha256']!=sha(canonical(info['state_binding']).encode())):raise ValueError('Incomplete actual row ledger')
        if state is None:state=info['state_binding']
        if info['state_binding']!=state:raise ValueError('Different actual row state')
        ledger=info['row_ledger'];counts=Counter()
        for q in ledger:
            if type(q['rows']) is not int or q['rows']<0:raise ValueError('Invalid observed row count')
            counts[q['label']]+=q['rows']
        if dict(counts)!=meta['row_groups'] or sum(counts.values())!=meta['rows'] or len(ledger)!=meta['blocks']:
            raise ValueError('Actual row counters differ')
        if len(m['pieces'])!=template['numerical_piece_count']:raise ValueError('Piece count differs')
        for a,b in zip(m['pieces'],template['pieces']):
            if (a['kind']!=b['kind'] or a.get('node_range')!=b.get('node_range') or set(a['arrays'])!=set(b['arrays'])):raise ValueError('Piece layout differs')
            for k in a['arrays']:
                if any(a['arrays'][k][f]!=b['arrays'][k][f] for f in ('shape','dtype','bytes')):raise ValueError('Array layout differs')
        rows+=meta['rows'];blocks+=meta['blocks'];r2+=float(meta['residual_squared']);groups.update(meta['row_groups'])
        summaries.append(dict(id=descriptor['id'],ordinal=descriptor['ordinal'],rows=meta['rows'],local_blocks=meta['blocks'],residual_squared=float(meta['residual_squared']),row_groups=meta['row_groups']))
        ids.append(identity(p))
    N=plan['tiles'][0]['dimensions']['nodes']
    if nodes!=list(range(N)) or cells!=list(range(N-1)) or boundaries!=1 or inside!=plan['interior_cells']:raise ValueError('Original partition is not complete exactly once')
    if common['field_and_finite_objective']!=baseline['binding'] or common['actual_value_residual']!=baseline['residual'] or common['plan_sha256']!=plan['plan_sha256']:raise ValueError('Actual baseline and closed tiles differ')
    for name,h in common['partition_sources'].items():
        if source(Path(__file__).parent/name)['sha256']!=h:raise ValueError('A frozen row source changed')
    value=baseline['value_packet_manifest']
    if identity(value['path'])!=value:raise ValueError('Actual value packet identity changed')
    expected=float(baseline['residual_squared']);difference=abs(r2-expected)
    if difference>2e-10*max(1.,expected):raise ArithmeticError('Full tile ledger differs from saved actual F squared')
    binding=dict(schema='fd2d-durable-merged-normal-binding-v1',common=common,plan_sha256=plan['plan_sha256'],ordered_tile_ids=[d['id'] for d in plan['tiles']])
    info=dict(schema='fd2d-R159-ordered-normal-tile-sum-v1',complete=True,full_finite_objective=True,
        partition_source_sha256=plan['partition_source_sha256'],plan_sha256=plan['plan_sha256'],
        mapping_sha256=plan['mapping_sha256'],state_binding=state,state_binding_sha256=sha(canonical(state).encode()),
        consumed_tiles=summaries,rows=rows,local_blocks=blocks,row_groups=dict(groups),residual_squared=r2,
        actual_complete_value_objective_squared=expected,actual_objective_squared_difference=difference,
        all_planned_rows_covered_exactly_once=True,scaling_or_damping_applied=False,
        original_ordered_tile_sum_unchanged=True,no_actual_F_or_J_evaluation=True,
        geometry_map_not_reconstructed_offline=True,map_reconstruction_required_before_use=True)
    md={k:encode(v) for k,v in dict(residual_squared=r2,rows=rows,blocks=blocks,row_groups=dict(groups),info=info).items()}
    record=dict(schema='fd2d-piecewise-normal-input-index-v1',source=source(__file__),request=identity(request),
        template_manifest=ids[0],tile_manifests=ids,binding=binding,metadata=md,
        metadata_sha256=sha(canonical(md).encode()),baseline=identity(root/'baseline-summary.json'),
        piece_count=template['numerical_piece_count'],objective_squared_difference=difference,
        complete_row_ledger_verified=True)
    write(path,record);return root,record


def run_piece(root,index,k):
    import numpy as np
    dest=root/'normal-piece-reduction'/f'piece-{k:04d}';closed=dest/'closed.json'
    if closed.exists():raise FileExistsError('Keep each actually completed piece immutable')
    accum=None;reference=None
    for item in index['tile_manifests']:
        if identity(item['path'])!=item:raise ValueError('An actual closed tile manifest changed')
        m=json.loads(Path(item['path']).read_text());row=m['pieces'][k];p=Path(item['path']).parent/row['file']
        raw=p.read_bytes()
        if len(raw)!=row['bytes'] or sha(raw)!=row['sha256'] or len(raw)>=1_000_000:raise ValueError('Closed small piece bytes changed')
        with np.load(io.BytesIO(raw),allow_pickle=False) as pack:
            if set(pack.files)!=set(row['arrays']):raise ValueError('Actual piece keys changed')
            if accum is None:
                reference=row;accum={key:np.zeros(row['arrays'][key]['shape'],dtype=np.dtype(row['arrays'][key]['dtype'])) for key in pack.files}
            for key in pack.files:
                a=pack[key]
                if array_id(a)!=row['arrays'][key] or a.shape!=accum[key].shape or a.dtype!=accum[key].dtype:raise ValueError('Actual logical array bytes changed')
                if not np.all(np.isfinite(a)):raise FloatingPointError('Nonfinite input tile')
                if row['kind']=='mapping':
                    if item==index['tile_manifests'][0]:accum[key][...]=a
                    elif not np.array_equal(accum[key],a):raise ValueError('Actual map arrays differ')
                else:accum[key]+=a
        del m,raw
    dest.parent.mkdir(parents=True,exist_ok=True);tmp=Path(tempfile.mkdtemp(prefix='.piece-incomplete-',dir=dest.parent))
    p=tmp/reference['file']
    with p.open('xb') as f:np.savez(f,**accum);f.flush();os.fsync(f.fileno())
    raw=p.read_bytes()
    if len(raw)>=1_000_000:raise ValueError('Output piece exceeds original limit')
    result=dict(reference,file=p.name,bytes=len(raw),sha256=sha(raw),arrays={key:array_id(a) for key,a in accum.items()})
    record=dict(schema='fd2d-closed-ordered-piece-sum-v1',complete=True,piece_index=k,
        actual_reducer_source=source(__file__),input_index=identity(root/'normal-piece-reduction'/'input-index.json'),
        piece=result,original_tile_order_unchanged=True,actual_F_or_J_evaluated=False)
    write(tmp/'closed.json',record);os.rename(tmp,dest)
    print(json.dumps(dict(event='actual_piece_closed',piece_index=k,bytes=result['bytes'])),flush=True)


def finalize(root,index):
    destination=root/'normal-partitioned'
    if destination.exists():raise FileExistsError(destination)
    template=json.loads(Path(index['template_manifest']['path']).read_text());parts=[]
    tmp=Path(tempfile.mkdtemp(prefix='.normal-piecewise-incomplete-',dir=root))
    index_id=identity(root/'normal-piece-reduction'/'input-index.json')
    for k in range(index['piece_count']):
        directory=root/'normal-piece-reduction'/f'piece-{k:04d}';r=json.loads((directory/'closed.json').read_text())
        if r.get('complete') is not True or r['piece_index']!=k or r['input_index']!=index_id or r['actual_reducer_source']!=source(__file__):raise ValueError('Incomplete or differently bound piece sum')
        q=r['piece'];p=directory/q['file'];raw=p.read_bytes()
        if len(raw)!=q['bytes'] or sha(raw)!=q['sha256']:raise ValueError('Saved output piece changed')
        shutil.copyfile(p,tmp/q['file']);parts.append(q)
    binding=index['binding'];record=dict(schema='fd2d-offline-piecewise-ordered-normal-v1',complete=True,
        directory_name=destination.name,actual_reducer_source=source(__file__),
        input_transport_source=template['source'],original_normal_source=template['original_normal_source'],
        piece_consumer_source=source(Path(__file__).with_name('fd2d_gc_piecewise_normal_transport.py')),
        binding=binding,binding_sha256=sha(canonical(binding).encode()),mapping=template['mapping'],mapping_sha256=template['mapping_sha256'],
        metadata=index['metadata'],metadata_sha256=index['metadata_sha256'],pieces=parts,
        normal_storage_bytes=template['normal_storage_bytes'],numerical_piece_count=len(parts),
        numerical_piece_bytes=sum(p['bytes'] for p in parts),actual_geometry_constructed_offline=False,
        original_field_mapping_must_be_reconstructed_before_use=True,input_index=index_id)
    write(tmp/'manifest.json',record);os.rename(tmp,destination)
    normal_id=identity(destination/'manifest.json')
    write(root/'normal-reference.json',dict(schema='fd2d-explicit-piecewise-merged-normal-reference-v1',
        finite_goal=binding['common']['field_and_finite_objective'],normal_manifest=normal_id,transport_binding=binding,
        actual_reducer_source=source(__file__),new_finite_goal_claimed=False))
    write(root/'normal-partitioned-summary.json',dict(schema='fd2d-complete-piecewise-normal-summary-v1',
        normal_manifest=normal_id,binding=binding,normal_information=decode(index['metadata']['info']),
        objective_squared_difference=index['objective_squared_difference'],actual_new_F_or_J=0))
    print(json.dumps(dict(event='actual_complete_piecewise_normal_closed',normal_manifest=normal_id,
        objective_squared_difference=index['objective_squared_difference'])),flush=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True);ap.add_argument('--piece',type=int)
    args=ap.parse_args();root,index=index_inputs(args.request)
    if args.piece is not None:run_piece(root,index,args.piece);return 0
    report_path=args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    if report_path.exists():raise FileExistsError(report_path)
    report=dict(schema='fd2d-owned-piecewise-normal-reduction-controller-v1',source=source(__file__),
        started_utc=utc(),complete=False,children=[]);write(report_path,report)
    for k in range(index['piece_count']):
        if (root/'normal-piece-reduction'/f'piece-{k:04d}'/'closed.json').exists():continue
        prefix=args.out_prefix.with_name(args.out_prefix.name+f'-p{k:04d}');receipt=prefix.with_name(prefix.name+'-process-receipt.json')
        command=[sys.executable,'-u','scripts/fd2d-run-monitored-command-v2.py','--receipt',str(receipt),'--',
            sys.executable,'-u',__file__,'--request',str(args.request),'--out-prefix',str(prefix),'--piece',str(k)]
        actual=subprocess.run(command);row=dict(piece=k,argv=command,receipt=str(receipt),monitor_returncode=actual.returncode)
        if receipt.exists():
            r=json.loads(receipt.read_text());row.update(child_returncode=r['actual_child_returncode'],seconds=r['seconds'],peak_rss_kib=r['kernel_child_maximum_resident_KiB'])
        report['children'].append(row);write(report_path,report)
        if actual.returncode:
            code=actual.returncode if actual.returncode>0 else 128-actual.returncode
            report.update(returncode=code,ended_utc=utc());write(report_path,report);return code
    finalize(root,index);report.update(complete=True,returncode=0,ended_utc=utc());write(report_path,report);return 0


if __name__=='__main__':raise SystemExit(main())
