# R165 finite objective entry; never consumes a v25 old-goal packet.
#!/usr/bin/env python3
"""Evaluate and durably save the actual initial value packet, then exit."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import hashlib
import json
import os
from pathlib import Path
import traceback
import numpy as np
from fd2d_gc_grouped_search_context import NumericalContext, array_identity
from fd2d_gc_packet_checkpoint import save_actual_packet, load_actual_packet
from fd2d_gc_archive_arrays import identity
from fd2d_gc_bump_residual_locations import residual_locations


def atomic_json(path, value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.writing')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    os.replace(temporary,path)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args()
    request=json.loads(args.request.read_text())
    root=Path(request['cache_dir']);root.mkdir(parents=True,exist_ok=True)
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=True)
    ctx.report.update(stage='actual_value_baseline',stage_source=identity(__file__))
    ctx.save_report()
    try:
        manifest=root/'baseline-values'/'manifest.json'
        recovered=manifest.exists()
        if recovered:
            packet=load_actual_packet(manifest,expected_binding=ctx.binding)
            if array_identity(packet['vector'])!=array_identity(ctx.vector):
                raise ValueError('Saved value packet has a different actual state')
            residual,data=packet['residual'],packet['data']
        else:
            residual,data=ctx.objective(ctx.vector)
            packet=dict(vector=ctx.vector.copy(),residual=residual,data=data)
            manifest=save_actual_packet(packet,root/'baseline-values',binding=ctx.binding)
        diagnostics=ctx.diag(ctx.vector,data)
        current=ctx.checkpoint(ctx.vector,'-actual-current.npz')
        summary=dict(schema='fd2d-durable-actual-value-baseline-v1',
            binding=ctx.binding,value_packet_manifest=identity(manifest),
            actual_current_state=current,vector=array_identity(ctx.vector),
            residual=array_identity(residual),residual_squared=float(residual@residual),
            objective_norm=float(np.linalg.norm(residual)),diagnostics=diagnostics,
            locations=residual_locations(ctx.problem,ctx.vector,data,
                data['codazzi_complement_result'],ctx.args.curvature_cap),
            stage_source=identity(__file__),recovered_complete_packet=recovered,
            actual_new_F_evaluations=ctx.objective_evaluations,
            finite_success=False,strong_target_complete=False)
        destination=root/'baseline-summary.json'
        if not destination.exists():atomic_json(destination,summary)
        else:
            old=json.loads(destination.read_text())
            if old['binding']!=ctx.binding or old['residual']!=summary['residual']:
                raise ValueError('Existing baseline summary describes a different actual packet')
        ctx.save_report(completed=True,actual_baseline_summary=identity(destination),
            value_packet_manifest=identity(manifest),initial=diagnostics,
            recovered_complete_packet=recovered)
        ctx.event('baseline_closed',objective_norm=summary['objective_norm'],
            residual_squared=summary['residual_squared'],manifest=str(manifest),
            recovered_complete_packet=recovered)
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        ctx.event('exception',type=type(exc).__name__,message=str(exc))
        raise


if __name__=='__main__':raise SystemExit(main())
