#!/usr/bin/env python3
"""Remove only the two cold CSC names after exact in-memory reconstruction.

The independently retained complete CSR archive is the lossless source. No
Jacobian, equation, residual or numerical comparison is recomputed. A single
CSR.tocsc() plus the original SciPy save_npz encoding must reproduce every byte
of the existing CSC archive before either of its two hardlinks is released.
The inverse operation restores those same two paths and verifies the full SHA.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import ctypes
import gc
import hashlib
import inspect
import io
import json
from pathlib import Path
import resource
import shutil
import sys
import time
import zipfile
import zlib

import numpy as np
import scipy
from scipy import sparse

SCHEMA = 'held10-cold-M24-CSC-from-complete-CSR-exact-v1'
EXPECTED_CSC_SHA = '28abf787e7f94ea3424ee1e0d2a9fc5839589698920c5872d3459674d382fe53'
EXPECTED_CSC_SIZE = 82251436
EXPECTED_DECODED = 131207067
ROOT = Path('/workspace/scratch/7c4e33ee17de')
CSR = ROOT/'held10-design-work/check-direct-csr-m24-20261128/actual_direct_csr.npz'
CSC = (ROOT/'held10-linear-work/actual-m24-check/actual_jacobian.npz',
       ROOT/'held10-design-work/check-direct-csc-m24-20261128/actual_direct_csc.npz')
MIB = 1024**2


def sha(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(MIB),b''):
            result.update(block)
    return result.hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def write(path,value):
    path = Path(path)
    temporary = path.with_name(path.name+'.tmp')
    with temporary.open('w') as stream:
        json.dump(value,stream,indent=2,allow_nan=False)
        stream.write('\n');stream.flush();os.fsync(stream.fileno())
    temporary.replace(path)
    descriptor=os.open(path.parent,os.O_DIRECTORY)
    try:os.fsync(descriptor)
    finally:os.close(descriptor)


def versions():
    return dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,
        zlib_compiled=zlib.ZLIB_VERSION,zlib_runtime=zlib.ZLIB_RUNTIME_VERSION,
        scipy_save_npz_source_sha256=hashlib.sha256(inspect.getsource(sparse.save_npz).encode()).hexdigest(),
        scipy_load_npz_source_sha256=hashlib.sha256(inspect.getsource(sparse.load_npz).encode()).hexdigest())


def zip_metadata(value):
    with zipfile.ZipFile(value) as archive:
        rows=[]
        for item in archive.infolist():
            rows.append(dict(name=item.filename,file_size=item.file_size,
                compressed_size=item.compress_size,compress_type=item.compress_type,
                date_time=list(item.date_time),flag_bits=item.flag_bits,
                create_system=item.create_system,create_version=item.create_version,
                extract_version=item.extract_version,external_attr=item.external_attr,
                internal_attr=item.internal_attr,CRC=item.CRC,header_offset=item.header_offset,
                extra_hex=item.extra.hex(),comment_hex=item.comment.hex()))
        return dict(members=rows,archive_comment_hex=archive.comment.hex(),
                    decoded_member_bytes=sum(row['file_size'] for row in rows))


def available_memory():
    for line in Path('/proc/meminfo').read_text().splitlines():
        if line.startswith('MemAvailable:'):
            return int(line.split()[1])*1024
    raise RuntimeError('No MemAvailable observation')


def reconstruct(csr_path,expected_source):
    if ref(csr_path)!=expected_source:
        raise ValueError('The retained complete CSR bytes changed')
    before=available_memory()
    if before<1024*MIB:
        raise MemoryError('Require 1 GiB observed headroom for the bounded in-memory archive reconstruction')
    csr=sparse.load_npz(csr_path)
    if (not sparse.isspmatrix_csr(csr) or csr.shape!=(64191,64191)
            or csr.dtype!=np.dtype('float64') or csr.indices.dtype!=np.dtype('int32')
            or csr.indptr.dtype!=np.dtype('int32')):
        raise ValueError('The independently retained original complete M24 CSR changed its storage contract')
    descriptor=dict(shape=list(csr.shape),nnz=int(csr.nnz),data_dtype=csr.data.dtype.str,
        indices_dtype=csr.indices.dtype.str,indptr_dtype=csr.indptr.dtype.str,
        stored_array_bytes=sum(array.nbytes for array in (csr.data,csr.indices,csr.indptr)))
    csc=csr.tocsc(copy=True)
    del csr
    gc.collect()
    trim=getattr(ctypes.CDLL(None),'malloc_trim',None)
    trimmed=bool(trim(0)) if trim is not None else None
    result=io.BytesIO()
    sparse.save_npz(result,csc,compressed=True)
    del csc
    gc.collect()
    if trim is not None:trim(0)
    view=result.getbuffer()
    digest=hashlib.sha256(view).hexdigest()
    size=len(view)
    view.release()
    result.seek(0)
    details=dict(complete_CSR_storage=descriptor,MemAvailable_before_bytes=before,
        obsolete_CSR_released_before_encoding=True,malloc_trim_after_release=trimmed,
        encoding='scipy.sparse.save_npz(BytesIO, csr.tocsc(copy=True), compressed=True)',
        output_bytes=size,output_sha256=digest,
        observed_process_maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        estimated_peak_budget_bytes=400*MIB,estimate_is_not_a_guarantee=True,
        full_J_recomputed=False,second_large_disk_file_written=False)
    return result,details


def prove_release(outdir):
    out=Path(outdir).resolve()
    if out.exists():raise FileExistsError(out)
    out.mkdir(parents=True)
    begun=time.monotonic()
    source=ref(CSR)
    old=[ref(path) for path in CSC]
    statistics=[path.stat() for path in CSC]
    if (any(item['sha256']!=EXPECTED_CSC_SHA or item['bytes']!=EXPECTED_CSC_SIZE for item in old)
            or len({(s.st_dev,s.st_ino) for s in statistics})!=1
            or any(s.st_nlink!=2 for s in statistics)
            or CSR.stat().st_ino==statistics[0].st_ino):
        raise ValueError('Only the two exact confirmed cold CSC hardlinks may be released')
    old_zip=zip_metadata(CSC[0]);source_zip=zip_metadata(CSR)
    if old_zip['decoded_member_bytes']!=EXPECTED_DECODED or source_zip['decoded_member_bytes']!=EXPECTED_DECODED:
        raise ValueError('The static decoded-array memory inventory changed')
    manifest=dict(schema=SCHEMA,status='checking_exact_lossless_reconstruction',
        source=ref(__file__),retained_CSR=source,original_CSC_paths=old,
        original_shared_inode=dict(device=statistics[0].st_dev,inode=statistics[0].st_ino,
            nlink=2,allocated_bytes=statistics[0].st_blocks*512),
        original_CSC_zip=old_zip,retained_CSR_zip=source_zip,versions=versions(),
        canonical_operation='load_npz(CSR).tocsc(copy=True); save_npz(BytesIO, CSC, compressed=True)',
        encoding_parameters=dict(compressed=True,seekable_output=True),
        scope='Exact reversible encoding relation only; no new matrix or mathematical comparison',
        files_released=[],source_CSR_deleted=False,created_unix=time.time())
    path=out/'manifest.json';write(path,manifest)
    output,details=reconstruct(CSR,source)
    current_zip=zip_metadata(output)
    same=(details['output_bytes']==EXPECTED_CSC_SIZE
          and details['output_sha256']==EXPECTED_CSC_SHA and current_zip==old_zip)
    manifest.update(reconstruction=details,exact_archive_bytes_reproduced=same,
        regenerated_zip_metadata=current_zip,seconds=time.monotonic()-begun)
    if not same:
        manifest['status']='one_original_encoding_did_not_reproduce_bytes_no_files_released'
        write(path,manifest);output.close()
        return 2
    # Revalidate all source/path bytes immediately before mutation. The small
    # durable manifest already suffices to reverse a partial two-unlink action.
    if ref(CSR)!=source or any(ref(p)!=r for p,r in zip(CSC,old)):
        raise ValueError('A retained or released archive changed during the exact proof')
    current=[p.stat() for p in CSC]
    if any((s.st_dev,s.st_ino,s.st_nlink)!=(statistics[0].st_dev,statistics[0].st_ino,2) for s in current):
        raise ValueError('The two original cold names no longer share only their confirmed inode')
    manifest.update(status='exact_bytes_verified_reconstruction_manifest_durable_before_release',
        retained_CSR_second_sha256=sha(CSR),restore_command=[sys.executable,str(Path(__file__).resolve()),
            'restore','--manifest',str(path)])
    write(path,manifest)
    output.close()
    for item in old:
        target=Path(item['path'])
        if ref(target)!=item:raise ValueError('A cold path changed immediately before unlink')
        target.unlink();manifest['files_released'].append(item['path']);write(path,manifest)
    manifest.update(status='exact_cold_CSC_hardlinks_released_CSR_fully_retained',
        retained_CSR_final_sha256=sha(CSR),released_allocated_bytes=statistics[0].st_blocks*512,
        original_names_absent=all(not p.exists() for p in CSC),seconds=time.monotonic()-begun,
        fresh_disk_free_bytes=shutil.disk_usage(out).free)
    write(path,manifest)
    print(json.dumps(dict(status=manifest['status'],manifest=ref(path),
                         released_allocated_bytes=manifest['released_allocated_bytes'])),flush=True)
    return 0


def restore(manifest_path):
    path=Path(manifest_path).resolve();manifest=json.loads(path.read_text())
    if (manifest['schema']!=SCHEMA or manifest.get('exact_archive_bytes_reproduced') is not True
            or manifest['source']!=ref(__file__) or manifest['versions']!=versions()
            or manifest['retained_CSR']!=ref(CSR)
            or [item['path'] for item in manifest['original_CSC_paths']]!=[str(p) for p in CSC]):
        raise ValueError('Require the exact retained CSR, frozen recovery code, versions and original paths')
    existing=[p for p in CSC if p.exists()]
    if existing:
        if any(sha(p)!=EXPECTED_CSC_SHA or p.stat().st_size!=EXPECTED_CSC_SIZE for p in existing):
            raise ValueError('An existing original path contains different bytes')
        base=existing[0]
        for p in CSC:
            if not p.exists():os.link(base,p)
    else:
        if shutil.disk_usage(CSC[0].parent).free<EXPECTED_CSC_SIZE+8*MIB:
            raise OSError('Insufficient disk for the one complete restored CSC archive')
        output,details=reconstruct(CSR,manifest['retained_CSR'])
        if (details['output_sha256']!=EXPECTED_CSC_SHA or details['output_bytes']!=EXPECTED_CSC_SIZE
                or zip_metadata(output)!=manifest['original_CSC_zip']):
            output.close();raise ValueError('No original path written: restoration did not reproduce the full exact archive')
        temporary=CSC[0].with_name(CSC[0].name+'.restore-tmp')
        if temporary.exists():raise FileExistsError(temporary)
        output.seek(0)
        with temporary.open('xb') as target:
            while True:
                block=output.read(MIB)
                if not block:break
                target.write(block)
            target.flush();os.fsync(target.fileno())
        output.close()
        if sha(temporary)!=EXPECTED_CSC_SHA:
            raise ValueError('The retained temporary reconstruction failed its complete disk SHA')
        os.link(temporary,CSC[0]);temporary.unlink()
        os.link(CSC[0],CSC[1])
    if any(sha(p)!=EXPECTED_CSC_SHA for p in CSC):
        raise ValueError('The restored original archive SHA differs')
    receipt=dict(status='both_original_CSC_paths_restored_with_complete_byte_identity',
        manifest=ref(path),source=ref(__file__),paths=[ref(p) for p in CSC],
        retained_CSR=ref(CSR),same_inode=CSC[0].stat().st_ino==CSC[1].stat().st_ino,
        completed_unix=time.time(),full_J_recomputed=False)
    write(path.parent/'restoration.json',receipt)
    print(json.dumps(receipt),flush=True)
    return 0


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest='command',required=True)
    commands.add_parser('prove-release').add_argument('--outdir',type=Path,required=True)
    commands.add_parser('restore').add_argument('--manifest',type=Path,required=True)
    args=parser.parse_args()
    return prove_release(args.outdir) if args.command=='prove-release' else restore(args.manifest)


if __name__=='__main__':raise SystemExit(main())
