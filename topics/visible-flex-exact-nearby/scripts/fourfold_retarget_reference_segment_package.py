#!/usr/bin/env python3
"""Preserve one complete exact finite retarget reference segment.

The small package contains the eight U/L controls, eight Q controls, the full
forward-end Q, and exact integer initial correction. Original JSON documents
are embedded byte-for-byte. Loading a package never opens the large original
coefficient shards; extraction first validates and rereads those shards.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import time

import numpy as np

from fourfold_retarget_reference_jets import RetargetReference, segment_arrays


ARRAY_NAMES=("base_real","base_imag","Q_real","Q_imag",
             "forward_end_Q_real","forward_end_Q_imag")
DOCUMENT_NAMES=("old_forward_reference","old_backward_reference","Q_forward",
                "Q_backward","initial_correction","target_object","target_root","target_H")


def digest_bytes(value):
    return hashlib.sha256(value).hexdigest()


def sha(path):
    return digest_bytes(Path(path).read_bytes())


def json_bytes(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False)+"\n").encode()


def byte_array(value):
    return np.frombuffer(value,dtype=np.uint8).copy()


def read_json_array(value):
    if value.dtype!=np.dtype('uint8') or value.ndim!=1:
        raise ValueError('JSON bytes must be an exact one-dimensional uint8 array')
    return json.loads(value.tobytes().decode('utf-8'))


def array_record(value):
    if (value.dtype!=np.dtype('<f8') or not np.all(np.isfinite(value))
            or value.ndim not in (1,2,3)):
        raise ValueError('finite exact little-endian binary64 coefficient arrays required')
    return dict(dtype=value.dtype.str,shape=list(value.shape),
                sha256=digest_bytes(value.tobytes(order='C')),bytes=value.nbytes)


def document_record(path,expected_hash=None):
    path=Path(path);raw=path.read_bytes();actual=digest_bytes(raw)
    if expected_hash is not None and actual!=expected_hash:
        raise ValueError('source JSON identity mismatch: '+str(path))
    text=raw.decode('utf-8')
    json.loads(text)
    return dict(path=str(path),sha256=actual,bytes=len(raw),text=text)


def load_package(path):
    """Return metadata, exact arrays and original JSONs without external reads.

    Returned documents[name]['document'] is parsed JSON, while its 'text'
    retains every original byte for an independent identity check.
    """
    path=Path(path);payload=path.read_bytes()
    if path.suffix!='.gz':
        raise ValueError('the complete small package must use .npz.gz')
    with np.load(io.BytesIO(gzip.decompress(payload)),allow_pickle=False) as data:
        expected=set(ARRAY_NAMES)|{'metadata_utf8','documents_utf8'}
        if set(data.files)!=expected:
            raise ValueError('unknown or missing exact package payload')
        arrays={name:data[name].copy() for name in ARRAY_NAMES}
        metadata=read_json_array(data['metadata_utf8'])
        documents=read_json_array(data['documents_utf8'])
    if (metadata.get('kind')!='exact_symbolic_retarget_single_segment_package'
            or metadata.get('schema_version')!=1 or not metadata.get('complete')):
        raise ValueError('unknown complete finite reference package convention')
    if set(documents)!=set(DOCUMENT_NAMES)|{'descriptor'}:
        raise ValueError('missing full original JSON definitions')
    for name,row in documents.items():
        raw=row['text'].encode('utf-8')
        if len(raw)!=row['bytes'] or digest_bytes(raw)!=row['sha256']:
            raise ValueError('embedded original JSON bytes changed: '+name)
        row['document']=json.loads(row['text'])
    d=documents['descriptor']['document']
    if not d.get('complete') or not d.get('symbolic_product_only'):
        raise ValueError('complete symbolic retarget definition required')
    for name in DOCUMENT_NAMES:
        if (d[name]['path']!=documents[name]['path']
                or d[name]['sha256']!=documents[name]['sha256']):
            raise ValueError('embedded descriptor/document identities disagree')
    identity=metadata['identity'];leg=identity['leg'];index=identity['segment']
    if leg not in ('forward','backward'):
        raise ValueError('unknown package leg')
    base=documents['old_'+leg+'_reference']['document']
    q=documents['Q_'+leg]['document']
    qf=documents['Q_forward']['document']
    if (not 0<=index<base['segment_count'] or base['leg']!=leg or q['leg']!=leg
            or base['time_basis']!='bernstein' or q['time_basis']!='bernstein'
            or base['time_degree']!=7 or q['time_degree']!=7
            or base['fields']!=['U','L'] or q['fields']!=['Qtilde']
            or base['exact_time_endpoints']!=q['exact_time_endpoints']
            or metadata['exact_time_rows']!=base['exact_time_endpoints'][index:index+2]
            or identity['branch_sign']!=base['trace_identity']['sign']
            or identity['old_exact_delta_fraction']!=d['old_exact_delta_fraction']
            or identity['target_exact_delta_fraction']!=d['target_exact_delta_fraction']):
        raise ValueError('time, Fourier, target or branch identity mismatch')
    shapes=dict(base_real=(8,2,base['Fourier_degree']+1),
                base_imag=(8,2,base['Fourier_degree']+1),
                Q_real=(8,q['Fourier_degree']+1),Q_imag=(8,q['Fourier_degree']+1),
                forward_end_Q_real=(qf['Fourier_degree']+1,),
                forward_end_Q_imag=(qf['Fourier_degree']+1,))
    for name,value in arrays.items():
        if value.shape!=shapes[name] or array_record(value)!=metadata['arrays'][name]:
            raise ValueError('complete exact coefficient payload changed: '+name)
        if name.endswith('imag') and np.any(value[...,0]!=0):
            raise ValueError('nonreal finite Fourier mean')
    for name in ('target_object','target_root','target_H'):
        if identity[name+'_sha256']!=documents[name]['sha256']:
            raise ValueError('target document hash differs from package identity')
    return dict(path=str(path),sha256=digest_bytes(payload),bytes=len(payload),
                metadata=metadata,arrays=arrays,documents=documents)


def extract_package(descriptor,leg,segment,out,report_path):
    started,cpu=time.monotonic(),time.process_time()
    descriptor,out,report_path=map(Path,(descriptor,out,report_path))
    if out.exists() or report_path.exists():
        raise ValueError('use fresh package and extraction-report paths')
    if out.suffix!='.gz':
        raise ValueError('package output must end in .npz.gz')
    reference=RetargetReference(descriptor)
    bp,base=reference.base[leg];qp,q=reference.Q[leg]
    br,bi,brow=segment_arrays(bp,base,segment,['U','L'])
    qr,qi,qrow=segment_arrays(qp,q,segment,['Qtilde'])
    fp,fdoc=reference.Q['forward']
    er,ei,erow=segment_arrays(fp,fdoc,fdoc['segment_count']-1,['Qtilde'])
    arrays=dict(base_real=br.copy(),base_imag=bi.copy(),Q_real=qr.copy(),Q_imag=qi.copy(),
                forward_end_Q_real=er[-1].copy(),forward_end_Q_imag=ei[-1].copy())
    documents={'descriptor':document_record(descriptor)}
    for name in DOCUMENT_NAMES:
        row=reference.doc[name]
        documents[name]=document_record(row['path'],row['sha256'])
    identity=dict(leg=leg,segment=segment,branch_sign=base['trace_identity']['sign'],
        old_exact_delta_fraction=reference.doc['old_exact_delta_fraction'],
        target_exact_delta_fraction=reference.doc['target_exact_delta_fraction'],
        target_object_sha256=documents['target_object']['sha256'],
        target_root_sha256=documents['target_root']['sha256'],
        target_H_sha256=documents['target_H']['sha256'])
    def shard_provenance(row,selected_segment,selected_control=None):
        path=Path(row['path'])
        return dict(path=str(path),sha256=row['sha256'],bytes=path.stat().st_size,
                    selected_global_segment=selected_segment,selected_control=selected_control)
    metadata=dict(kind='exact_symbolic_retarget_single_segment_package',schema_version=1,
        complete=True,source_sha256=sha(__file__),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ('fourfold_retarget_reference_jets.py','fourfold_shared_dense_reference.py')},
        identity=identity,exact_time_rows=base['exact_time_endpoints'][segment:segment+2],
        time_coordinate='u in [-1,1]; tau=center+h*u with the original exact rational/pi endpoints',
        Fourier_coordinate='normalized initial label x of period 2*pi; physical Y=x/4+periodic part',
        arrays={name:array_record(value) for name,value in arrays.items()},
        original_coefficient_sources=dict(
            base=shard_provenance(brow,segment),Q=shard_provenance(qrow,segment),
            forward_end_Q=shard_provenance(erow,fdoc['segment_count']-1,7)),
        formula=('Y=x/4+U+Q*a' if leg=='forward' else 'Y=x/4+U+Q*(Q_forward_end*a)'),
        exact_initial_correction='the complete integer polynomial in embedded initial_correction; no Fourier product truncation',
        coefficient_convention='every saved binary64 value is exact; negative Fourier modes are exact conjugates of time-polynomial coefficients',
        scope='One complete finite reference segment only; no true-flow or residual certificate.')
    buffer=io.BytesIO()
    np.savez(buffer,**arrays,metadata_utf8=byte_array(json_bytes(metadata)),
             documents_utf8=byte_array(json_bytes(documents)))
    packed=gzip.compress(buffer.getvalue(),mtime=0)
    if len(packed)>5_000_000:
        raise ValueError('single-segment package exceeds repository file limit')
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(packed)
    loaded=load_package(out)
    # Freshly reread the original complete shards after loading the final
    # package; array equality is bitwise, including the signs of zero.
    rr,ri,_=segment_arrays(bp,base,segment,['U','L'])
    sr,si,_=segment_arrays(qp,q,segment,['Qtilde'])
    tr,ti,_=segment_arrays(fp,fdoc,fdoc['segment_count']-1,['Qtilde'])
    original=dict(base_real=rr,base_imag=ri,Q_real=sr,Q_imag=si,
                  forward_end_Q_real=tr[-1],forward_end_Q_imag=ti[-1])
    checks={name:loaded['arrays'][name].tobytes(order='C')==value.tobytes(order='C')
            for name,value in original.items()}
    if not all(checks.values()):
        raise ValueError('package differs bitwise from freshly reread source coefficients')
    result=dict(kind='exact_single_segment_reference_extraction_check',complete=True,
        source_sha256=sha(__file__),package=dict(path=str(out),sha256=sha(out),bytes=len(packed)),
        identity=identity,exact_time_rows=metadata['exact_time_rows'],
        original_coefficient_sources=metadata['original_coefficient_sources'],
        original_JSONs={name:{key:row[key] for key in ('path','sha256','bytes')}
                        for name,row in documents.items()},
        freshly_reloaded_source_arrays_bitwise_equal=checks,
        all_embedded_original_JSON_byte_hashes_verified=True,
        loader_does_not_open_original_source_paths=True,
        elapsed_seconds=time.monotonic()-started,cpu_seconds=time.process_time()-cpu,
        limitations=['This is the complete exact chosen finite reference for one segment.',
            'The package contains all Fourier modes and the complete symbolic correction; no resampling was used.',
            'It does not prove true-field accuracy, a whole branch, a residual or a flow.'])
    report_path.parent.mkdir(parents=True,exist_ok=True)
    report_path.write_text(json.dumps(result,indent=2)+'\n')
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor',type=Path)
    p.add_argument('--leg',choices=('forward','backward'),default='forward')
    p.add_argument('--segment',type=int,default=419)
    p.add_argument('--out',type=Path);p.add_argument('--report',type=Path)
    p.add_argument('--check',type=Path,help='Validate and inspect a self-contained package, without original data')
    args=p.parse_args()
    if args.check:
        if any(v is not None for v in (args.descriptor,args.out,args.report)):
            raise ValueError('--check is a separate read-only mode')
        d=load_package(args.check)
        print(json.dumps(dict(complete=True,package=d['path'],sha256=d['sha256'],bytes=d['bytes'],
                              identity=d['metadata']['identity'],
                              original_source_files_required=False),indent=2))
    else:
        if any(v is None for v in (args.descriptor,args.out,args.report)):
            raise ValueError('extraction requires --descriptor, --out and --report')
        result=extract_package(args.descriptor,args.leg,args.segment,args.out,args.report)
        print(json.dumps(dict(complete=True,package=result['package'],
                              report=str(args.report),report_sha256=sha(args.report)),indent=2))


if __name__=='__main__':
    main()
