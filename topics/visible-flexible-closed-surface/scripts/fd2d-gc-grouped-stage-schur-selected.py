#!/usr/bin/env python3
"""Solve the saved normal by small field blocks and save all Schur data."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import importlib
import inspect
from pathlib import Path
import traceback
from fd2d_gc_grouped_search_context import NumericalContext
from fd2d_gc_selected_normal_io import selected_normal,load_selected_normal
load_normal_checkpoint=load_selected_normal
from fd2d_gc_packet_checkpoint import save_actual_packet,load_actual_packet
from fd2d_gc_saved_schur_search import make_schur_packet
from fd2d_gc_schur_stage_io import factor_binding
from fd2d_gc_stage_io import atomic_json
from fd2d_gc_archive_arrays import identity


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--factor-id',required=True)
    ap.add_argument('--damping',type=float,required=True)
    ap.add_argument('--field-solver-module',required=True)
    ap.add_argument('--field-solver-function',default='solve_scaled_normal_field')
    args=ap.parse_args()
    if Path(args.factor_id).name!=args.factor_id or not args.field_solver_module.isidentifier() or not args.field_solver_function.isidentifier():
        raise ValueError('Use explicit local module/function identifiers and a plain factor id')
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=False)
    ctx.report.update(stage='same_normal_small_block_field_factor_and_saved_Schur',stage_source=identity(__file__))
    ctx.save_report()
    try:
        root=Path(ctx.request['cache_dir'])
        normal_manifest,normal_binding,normal_origin=selected_normal(ctx)
        ctx.report['normal_origin']=normal_origin
        module=importlib.import_module(args.field_solver_module)
        solve=getattr(module,args.field_solver_function)
        source=inspect.getsourcefile(solve)
        if source is None:raise ValueError('Field solver must have an explicit frozen source file')
        binding=factor_binding(ctx,normal_manifest,args.damping,source,__file__)
        directory=root/'reduced-factors'/args.factor_id
        manifest=directory/'packet'/'manifest.json';recovered=manifest.exists()
        ctx.event('saved_normal_load_start',manifest=str(normal_manifest))
        normal=load_normal_checkpoint(ctx.problem,normal_manifest,expected_binding=normal_binding)
        ctx.event('saved_normal_load_complete',rows=normal.rows,storage_bytes=normal.storage_bytes())
        if recovered:
            packet=load_actual_packet(manifest,expected_binding=binding)
        else:
            ctx.event('same_normal_block_field_solve_start',damping=args.damping,solver=identity(source))
            def progress(*items,**values):
                ctx.event('block_field_solve_progress',items=list(items),**values)
            solution=solve(normal,damping=args.damping,progress=progress)
            ctx.event('same_normal_block_field_solve_complete',information=solution['info'])
            packet=make_schur_packet(normal,solution,damping=args.damping)
            del solution
            manifest=save_actual_packet(packet,directory/'packet',binding=binding)
        summary=dict(schema='fd2d-complete-saved-normal-Schur-factor-v1',binding=binding,
            factor_id=args.factor_id,damping=args.damping,normal_manifest=identity(normal_manifest),
            packet_manifest=identity(manifest),field_solver_module=args.field_solver_module,
            field_solver_function=args.field_solver_function,solver_source=identity(source),
            producer_source=identity(__file__),schur_minimum_eigenvalue=packet['schur_minimum_eigenvalue'],
            schur_shift=packet['schur_shift'],field_solve_information=packet['field_solve_information'],
            full_normal_rows=normal.rows,recovered_complete_factor=recovered,
            QP_or_line_search_performed=False,residual_or_Jacobian_recomputed=False)
        target=directory/'summary.json'
        if not target.exists():atomic_json(target,summary)
        ctx.save_report(completed=True,factor_summary=identity(target),factor_packet=identity(manifest),
            field_solve_information=packet['field_solve_information'],recovered_complete_factor=recovered)
        ctx.event('normal_Schur_factor_durably_closed',factor_id=args.factor_id,manifest=str(manifest),
            schur_minimum_eigenvalue=packet['schur_minimum_eigenvalue'],schur_shift=packet['schur_shift'])
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        ctx.event('exception',type=type(exc).__name__,message=str(exc));raise


if __name__=='__main__':raise SystemExit(main())
