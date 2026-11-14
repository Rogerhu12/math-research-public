#!/usr/bin/env python3
"""Run a floating producer under an explicit address-space allocation cap.

This wrapper changes no equation, solver coefficient, tolerance, or finite
candidate. Its separate process audit distinguishes an allocation failure
from every mathematical/solver gate and records all accepted checkpoints.
"""
from __future__ import annotations
import argparse,gc,hashlib,json,resource,runpy,sys,time,traceback
from pathlib import Path


def sha(path):
    result=hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):result.update(chunk)
    return result.hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--producer',type=Path,required=True)
    ap.add_argument('--resource-report',type=Path,required=True)
    ap.add_argument('--max-address-space-mib',type=int,default=1536)
    ap.add_argument('producer_arguments',nargs=argparse.REMAINDER)
    args=ap.parse_args();argv=args.producer_arguments
    if argv and argv[0]=='--':argv=argv[1:]
    if args.resource_report.exists():raise FileExistsError('preserve an existing actual process audit')
    if args.max_address_space_mib<512:raise ValueError('at least 512 MiB must be specified explicitly')
    out=Path(argv[argv.index('--out')+1]) if '--out' in argv else None
    root=Path('/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints')
    if '--checkpoint-dir' in argv:root=Path(argv[argv.index('--checkpoint-dir')+1])
    checkpoint_dir=root/out.stem if out else None
    limit=args.max_address_space_mib*1024*1024;tick=time.monotonic()
    audit=dict(kind='explicit_bounded_floating_Codazzi_producer_process',complete=False,
        certified=False,source_sha256=sha(__file__),producer=str(args.producer),
        producer_sha256=sha(args.producer),producer_arguments=argv,
        address_space_limit_bytes=limit,address_space_limit_MiB=args.max_address_space_mib,
        limit_kind='RLIMIT_AS address space, not resident memory',
        mathematical_equations_or_tolerances_modified=False,
        status='started',all_accepted_checkpoints=[],producer_output=str(out) if out else None)
    def save():
        args.resource_report.write_text(json.dumps(audit,indent=2,allow_nan=False)+'\n')
    save();resource.setrlimit(resource.RLIMIT_AS,(limit,limit))
    print(dict(explicit_address_space_limit_MiB=args.max_address_space_mib,
               producer=str(args.producer),resource_report=str(args.resource_report)),flush=True)
    code=0
    try:
        sys.path.insert(0,str(args.producer.parent.resolve()))
        sys.argv=[str(args.producer),*argv]
        runpy.run_path(str(args.producer),run_name='__main__')
        audit['status']='producer_returned_normally'
    except MemoryError as error:
        audit['status']='address_space_allocation_failure'
        audit['error_type']=type(error).__name__;audit['error']=str(error)
        traceback.clear_frames(error.__traceback__);code=70
    except Exception as error:
        audit['status']='producer_exception'
        audit['error_type']=type(error).__name__;audit['error']=str(error)
        traceback.clear_frames(error.__traceback__);code=71
    gc.collect()
    if checkpoint_dir is not None:
        audit['all_accepted_checkpoints']=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)
            for p in sorted(checkpoint_dir.glob('accepted-*.npz'))]
    audit.update(complete=True,process_wrapper_exit_code=code,
        peak_resident_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        wall_seconds=time.monotonic()-tick,
        producer_output_exists=bool(out and out.exists()),
        scope='Only a process allocation guard and complete checkpoint inventory. A normal producer return does not mean its finite BVP converged; the separate producer report retains all actual solver/math gates.')
    if out and out.exists():audit['producer_output_sha256']=sha(out)
    save();print(dict(bounded_process_status=audit['status'],exit_code=code,
        peak_resident_KiB=audit['peak_resident_KiB'],accepted_checkpoints=len(audit['all_accepted_checkpoints'])),flush=True)
    raise SystemExit(code)


if __name__=='__main__':main()
