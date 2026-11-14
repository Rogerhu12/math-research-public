"""R159 selected interior rows with explicit complete cell-consumer plumbing.

This is a separate adapter; the original assembly modules remain frozen.

One original node/cell packet and then one two-node interior packet are
assembled at a time. No whole tall Jacobian is retained. This changes only
storage and floating summation order; the v18 finite objective is intact.
"""
import time
import numpy as np
from fd2d_gc_positive_trace_stream_normal_consumer import stream_positive_trace_normal
from fd2d_gc_gauss_cell_positive_trace import gauss_cell_positive_trace
from fd2d_gc_positive_trace_interior_merit import interior_gauss_curvature


def stream_positive_trace_interior_normal(problem,vector,*,cells=(63,71,118),
        interior_gauss_weight=1.,curvature_cap=7.2,curvature_weight=1.,
        high_gauss_weight=1.,high_codazzi_weight=1.,block_cells=8,progress=None,
        cell_consumer=gauss_cell_positive_trace):
    start=time.monotonic()
    normal,info=stream_positive_trace_normal(problem,vector,
        curvature_cap=curvature_cap,curvature_weight=curvature_weight,
        high_gauss_weight=high_gauss_weight,high_codazzi_weight=high_codazzi_weight,
        block_cells=block_cells,progress=progress,cell_consumer=cell_consumer)
    small=[];q=problem.q;offset=problem.N*q
    for cell in cells:
        cell=int(cell)
        part=interior_gauss_curvature(problem,vector,cells=(cell,),
            gauss_weight=interior_gauss_weight,curvature_cap=curvature_cap,
            curvature_weight=curvature_weight,jacobian=True)
        columns=np.r_[np.arange(cell*q,(cell+2)*q),offset+np.arange(problem.parameter_count)]
        for name in ('retained','high','curvature'):
            normal.add(part[name+'_residual'],part[name+'_jacobian'][:,columns],
                (cell,cell+1),label='interior_'+name)
        small.append(part['info'])
        del part
        if progress is not None:progress('interior_cell',cell,normal.rows)
    info=dict(info,schema='fd2d-R159-interior-local-normal-explicit-consumer-v1',
        selected_interior_cells=list(map(int,cells)),interior_constraints=small,
        rows=normal.rows,local_blocks=normal.blocks,row_groups=dict(normal.row_groups),
        unscaled_normal_storage_bytes=normal.storage_bytes(),seconds=time.monotonic()-start,
        full_v18_finite_objective=True,finite_field_changed=False,
        finite_equations_changed_by_streaming=False,whole_tall_J_stored=False)
    normal.info=info;return normal,info
