#!/usr/bin/env python3
"""Use the complete direct-CSC assembler around the stable resource V5.

This changes temporary storage, not any matrix entry or floating block
formula. Stable V5 still owns analytical delta, original residuals and gates,
and the full nodal checkpoint before each J. A separate QR wrapper may select
its independently checked complete linear solve.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import prefix_resource_driver_v5 as base
import direct_csc_collocation as assembly
previous=base.previous


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--assembly-block',type=int,default=16)
    options,rest=parser.parse_known_args()
    if options.assembly_block<1:raise ValueError('A positive assembly block is required')
    command=list(sys.argv)
    out=Path(rest[rest.index('--outdir')+1]).resolve() if '--outdir' in rest else None
    path=out.with_name(out.name+'-direct-csc.jsonl') if out is not None else None
    if path is not None and path.exists():raise FileExistsError(path)
    started=time.monotonic();stats=[]

    def event(row):
        stats.append(row)
        if path is not None:
            with path.open('a') as stream:
                stream.write(json.dumps(dict(event='complete_CSC_assembly_return',
                    elapsed=time.monotonic()-started,**row),allow_nan=False)+'\n')

    hashes,restore=assembly.install(options.assembly_block,event)
    sources={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (
        Path(__file__).resolve(),Path(assembly.__file__).resolve(),Path(base.__file__).resolve())}
    sys.argv=[str(Path(base.__file__).resolve()),*rest]
    try:
        return base.main()
    finally:
        restore()
        if out is not None and out.is_dir():
            row=dict(scope=__doc__,actual_command=command,source_hashes=sources,
                original_scipy_function_hashes=hashes,assemblies=stats,
                old_COO_indices_allocated=False,all_original_entries_retained=True,
                numerical_block_arithmetic_changed=False,original_gates_changed=False,
                complete_surface=False)
            (out/'complete-csc-assembly.json').write_text(json.dumps(row,indent=2,allow_nan=False)+'\n')


if __name__=='__main__':main()
