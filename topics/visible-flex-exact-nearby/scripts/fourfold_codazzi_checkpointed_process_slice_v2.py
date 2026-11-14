#!/usr/bin/env python3
"""Yield only after a complete persisted QR substitution checkpoint.

This is a process scheduling wrapper. It does not change the producer,
factor fingerprint, mathematical equations, Newton acceptance or backward
residual gate. A requested slice pause is a normal process result but is
explicitly not a finite solve or a mathematical certificate.
"""
from __future__ import annotations
import argparse, fcntl, gc, hashlib, json, os, resource, runpy, sys, time
from pathlib import Path


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''): h.update(block)
    return h.hexdigest()


class PersistedSlicePause(Exception):
    def __init__(self, factor, stage, index):
        self.record=dict(factor_fingerprint=factor,stage=stage,next_index=index,
                         pause_after_successful_atomic_progress_save=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--producer',type=Path,required=True)
    ap.add_argument('--process-report',type=Path,required=True)
    ap.add_argument('--slice-seconds',type=float,default=38.)
    ap.add_argument('--max-address-space-mib',type=int,default=1024)
    ap.add_argument('producer_arguments',nargs=argparse.REMAINDER)
    args=ap.parse_args(); argv=args.producer_arguments
    if argv and argv[0]=='--': argv=argv[1:]
    if args.process_report.exists(): raise FileExistsError('preserve each actual slice outcome')
    if args.slice_seconds<=0 or args.max_address_space_mib<512: raise ValueError('invalid resource controls')
    out=Path(argv[argv.index('--out')+1])
    checkpoint_root=Path('/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints')
    if '--checkpoint-dir' in argv: checkpoint_root=Path(argv[argv.index('--checkpoint-dir')+1])
    lock_root=Path('/workspace/scratch/ac0d699811ad/codazzi_process_locks')
    lock_root.mkdir(exist_ok=True)
    lock_path=lock_root/(hashlib.sha256(str(out.resolve()).encode()).hexdigest()+'.lock')
    lock_stream=lock_path.open('a')
    fcntl.flock(lock_stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
    tick=time.monotonic(); deadline=None
    audit=dict(kind='actual_complete_QR_substitution_process_slice',certified=False,
        complete=False,status='started',source_sha256=sha(__file__),
        producer=str(args.producer),producer_sha256=sha(args.producer),
        producer_arguments=argv,requested_slice_seconds=args.slice_seconds,
        slice_clock='starts after the actual complete factor constructor returns',
        max_address_space_mib=args.max_address_space_mib,
        mathematical_equations_or_gates_modified=False,
        source_factor_and_RHS_identity_checks_unchanged=True,
        original_complete_backward_residual_gate=5e-8,
        all_accepted_checkpoints=[],producer_output=str(out))
    def save():
        tmp=args.process_report.with_name(args.process_report.name+'.partial')
        tmp.write_text(json.dumps(audit,indent=2,allow_nan=False)+'\n')
        os.replace(tmp,args.process_report)
    save()
    limit=args.max_address_space_mib*1024*1024
    resource.setrlimit(resource.RLIMIT_AS,(limit,limit))
    sys.path.insert(0,str(args.producer.parent.resolve()))
    from fourfold_codazzi_block_qr_persistent import PersistentCheckpointBoundaryQR
    original_init=PersistentCheckpointBoundaryQR.__init__
    def sliced_init(self,*pos,**kw):
        nonlocal deadline
        original_init(self,*pos,**kw)
        deadline=time.monotonic()+args.slice_seconds
        def hook(stage,index):
            if time.monotonic()>=deadline and stage!='complete':
                raise PersistedSlicePause(self.fingerprint,stage,int(index))
        self.checkpoint_hook=hook
    PersistentCheckpointBoundaryQR.__init__=sliced_init
    code=0
    try:
        sys.argv=[str(args.producer),*argv]
        runpy.run_path(str(args.producer),run_name='__main__')
        audit['status']='producer_returned_normally'
    except PersistedSlicePause as pause:
        audit['status']='intentional_saved_complete_substitution_checkpoint_pause'
        audit['saved_complete_substitution_progress']=pause.record
        audit['finite_BVP_success_not_claimed']=True
    except MemoryError as exc:
        audit.update(status='address_space_allocation_failure',error_type=type(exc).__name__,error=str(exc));code=70
    except Exception as exc:
        audit.update(status='producer_exception',error_type=type(exc).__name__,error=str(exc));code=71
    finally:
        PersistentCheckpointBoundaryQR.__init__=original_init
    gc.collect()
    audit.update(complete=True,actual_wrapper_exit_code=code,
        peak_resident_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        wall_seconds=time.monotonic()-tick,producer_output_exists=out.exists(),
        all_accepted_checkpoints=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)
            for p in sorted((checkpoint_root/out.stem).glob('accepted-*.npz'))],
        scope='Only actual process scheduling. No completed finite solve, infinite PDE solution or geometric certificate is implied by a normal slice exit.')
    if out.exists(): audit['producer_output_sha256']=sha(out)
    save()
    print(dict(process_slice_status=audit['status'],exit_code=code,
        saved_progress=audit.get('saved_complete_substitution_progress'),
        accepted_checkpoints=len(audit['all_accepted_checkpoints']),
        seconds=audit['wall_seconds']),flush=True)
    raise SystemExit(code)


if __name__=='__main__': main()
