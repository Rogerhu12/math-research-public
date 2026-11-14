#!/usr/bin/env python3
"""Declare the exact small normal row groups without evaluating F or J."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
from pathlib import Path
from fd2d_gc_staged_search_context import NumericalContext
from fd2d_gc_normal_tile_io import partition_context
from fd2d_gc_archive_arrays import identity


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args()
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=False)
    root,plan,common,baseline=partition_context(ctx)
    counts={kind:sum(d['kind']==kind for d in plan['tiles'])
            for kind in ('nodes','cells','boundary','interior')}
    ctx.save_report(stage='declare_actual_normal_row_partition',stage_source=identity(__file__),
        completed=True,normal_plan=identity(root/'normal-partition-plan.json'),
        common_binding=common,tile_counts=counts,actual_F_or_J_evaluations=0)
    ctx.event('normal_partition_declared',tiles=len(plan['tiles']),counts=counts,
        plan=str(root/'normal-partition-plan.json'))
    return 0


if __name__=='__main__':raise SystemExit(main())
