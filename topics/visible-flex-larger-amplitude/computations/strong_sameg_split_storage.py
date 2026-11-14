#!/usr/bin/env python3
"""Run the unchanged same-g M28 entry with separate Jacobian/QR disks.

Only the directory supplied to the already implemented QR file arena changes.
All arrays, arithmetic, iteration rules, full streamed backward checks, full-H
tail requests and original acceptance gates remain those of the locked source.
"""
from __future__ import annotations
import argparse
import errno
import gzip
import hashlib
import inspect
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import time

HERE=Path(__file__).resolve().parent
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
BASE_SHA='65e81c73707c6f094ce5d494965d2fd468e971f4fa450d88513cf4ac622476fd'
BACKEND_SHA='402830e66390f660d7f8e846165a2ae7c1e9858addc2317df06348dc1e8634f1'
DISK_SHA='f252024e7193b0e98c6f243b9dc6814c94c28c358e059b8a901da8e6396620b2'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def argument(argv,key):
    if argv.count(key)!=1:
        raise ValueError('Exactly one original argument required: '+key)
    i=argv.index(key)
    if i+1==len(argv):
        raise ValueError('Missing value: '+key)
    return argv[i+1]


def write_new(path,value):
    data=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    with Path(path).open('xb') as stream:
        stream.write(data);stream.flush();os.fsync(stream.fileno())


def requirements(n,m,k):
    # Boundary A/B/P are resident arrays; only interior A/B/P are in the disk arena.
    return dict(matrix_bytes=(m-1)*n*(2*n+k)*8,
        factor_bytes=(m-2)*(4*n*n+n*k+n)*8,
        boundary_resident_bytes=(n+k)*(2*n+k)*8)


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--split-matrix-parent',type=Path,required=True)
    parser.add_argument('--split-factor-parent',type=Path,required=True)
    own,remaining=parser.parse_known_args()
    matrix_parent=own.split_matrix_parent.resolve()
    factor_parent=own.split_factor_parent.resolve()
    matrix_parent.mkdir(parents=True,exist_ok=True)
    factor_parent.mkdir(parents=True,exist_ok=True)
    original_temporary=argument(remaining,'--spectral-temporary-parent')
    remaining[remaining.index('--spectral-temporary-parent')+1]=str(matrix_parent)
    out=Path(argument(remaining,'--out-prefix'))
    prepare='--spectral-prepare-only' in remaining
    old_argv=sys.argv
    for name,expected in (
            ('strong_sameg_spectral_refinement.py',BASE_SHA),
            ('strong_disk_actual_backend.py',BACKEND_SHA),
            ('root_disk_block_collocation.py',DISK_SHA)):
        if sha(HERE/name)!=expected:
            raise ValueError('Locked mathematical/storage source differs: '+name)
    import strong_sameg_spectral_refinement as base
    import strong_disk_actual_backend as backend
    disk=backend.disk
    original_init=disk.DiskDirectBlockQRFactor.__init__
    original_source=inspect.getsource(original_init)
    if Path(inspect.getsourcefile(original_init)).resolve()!=Path(disk.__file__).resolve():
        raise ValueError('The original QR initializer has already been replaced')
    metadata_path=Path(argument(remaining,'--spectral-fixed-raw'))
    raw=json.loads(gzip.decompress(metadata_path.read_bytes()))
    nodes=int(raw['arrays']['x']['shape'][0])
    M=int(argument(remaining,'--modes'));n=3*M+1
    initial=requirements(n,nodes,M)
    maximum=requirements(n,int(argument(remaining,'--max-nodes')),M)
    record=dict(scope=__doc__,entry_sha256=SELF_SHA,
        base_source_sha256=BASE_SHA,backend_source_sha256=BACKEND_SHA,disk_source_sha256=DISK_SHA,
        original_factor_initializer_sha256=hashlib.sha256(original_source.encode()).hexdigest(),
        matrix_parent=str(matrix_parent),factor_parent=str(factor_parent),
        original_single_temporary_parent=original_temporary,
        changed_only=['spectral-temporary-parent storage path','QR initializer directory keyword'],
        mathematical_arguments_unchanged=True,MJS_unchanged=True,
        initial_dimensions=dict(n=n,nodes=nodes,parameters=M),
        initial_storage_bytes=initial,maximum_allowed_mesh_storage_bytes=maximum,
        free_bytes_before=dict(matrix=shutil.disk_usage(matrix_parent).free,
                               factor=shutil.disk_usage(factor_parent).free),
        exact_original_float64_storage=True,old_termination_causes_not_inferred=True)
    if prepare:
        write_new(Path(str(out)+'-split-storage-prepared.json'),record)
        sys.argv=[old_argv[0],*remaining]
        try:
            return base.main()
        finally:
            sys.argv=old_argv
    # Check only storage capacity, not a new mathematical or numerical gate.
    # This is a current observation, never a promise that shared free space stays fixed.
    if (record['free_bytes_before']['matrix']<initial['matrix_bytes']+16*1024**2 or
            record['free_bytes_before']['factor']<initial['factor_bytes']+48*1024**2):
        write_new(Path(str(out)+'-split-storage-preflight-failed.json'),record)
        raise OSError(errno.ENOSPC,'Current owned storage cannot hold the first exact matrix/factor')
    temporary=tempfile.TemporaryDirectory(prefix='visible-flex-M28-QR-',dir=factor_parent)
    record['factor_directory']=temporary.name
    write_new(Path(str(out)+'-split-storage-start.json'),record)
    events=Path(str(out)+'-split-storage-events.jsonl').open('x')
    factors=0;started=time.monotonic();failure=None
    def emit(event,**fields):
        row=dict(event=event,seconds=time.monotonic()-started,**fields)
        text=json.dumps(row,allow_nan=False)+'\n'
        events.write(text);events.flush();os.fsync(events.fileno())
        print(text,end='',flush=True)
    def initialize(self,matrix,n,node_count,k,directory=None):
        nonlocal factors
        if directory is None or Path(directory).resolve().parent!=matrix_parent:
            raise ValueError('The original Jacobian directory escaped this owned matrix parent')
        wanted=requirements(int(n),int(node_count),int(k))
        if matrix.storage.size!=wanted['matrix_bytes']:
            raise ValueError('Original exact matrix byte layout changed')
        free=shutil.disk_usage(temporary.name).free
        emit('split_storage_factor_begin',dimensions=dict(n=n,nodes=node_count,parameters=k),
             exact_storage_bytes=wanted,factor_free_bytes=free,
             original_matrix_directory=str(directory),factor_directory=temporary.name)
        if free<wanted['factor_bytes']+16*1024**2:
            raise OSError(errno.ENOSPC,'Current QR filesystem cannot hold this unchanged exact factor')
        # The original method executes unchanged, with only this keyword redirected.
        original_init(self,matrix,n,node_count,k,directory=temporary.name)
        if self.storage.size!=wanted['factor_bytes']:
            raise ValueError('Original exact QR byte layout changed')
        factors+=1
        emit('split_storage_factor_complete',factor=factors,
             matrix_bytes=matrix.storage.size,factor_bytes=self.storage.size)
    disk.DiskDirectBlockQRFactor.__init__=initialize
    sys.argv=[old_argv[0],*remaining]
    try:
        base.main()
    except BaseException as error:
        failure=repr(error)
        raise
    finally:
        sys.argv=old_argv;disk.DiskDirectBlockQRFactor.__init__=original_init
        emit('split_storage_returned',factors=factors,error=failure,
             scientific_success_inferred=False)
        events.close()
        record.update(factors=factors,error=failure,seconds=time.monotonic()-started,
            original_initializer_restored=True,scientific_success_inferred=False)
        write_new(Path(str(out)+'-split-storage-terminal.json'),record)
        temporary.cleanup()


if __name__=='__main__':
    main()
