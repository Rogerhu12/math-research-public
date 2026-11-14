"""Read-only complete v18/v19 actual finite objective for an immutable state.

Used for explicit new-initial-field comparisons. No Jacobian, direction,
projection or optimizer; every row keeps the live solver's normalization.
"""
import gc
import numpy as np
from fd2d_gc_positive_trace_merit import curvature_merit,high_gauss_merit
from fd2d_gc_positive_trace_interior_merit import interior_gauss_curvature
from fd2d_gc_gauss_cell_codazzi_chunked import gauss_cell_codazzi
from fd2d_gc_gauss_cell_positive_trace import gauss_cell_positive_trace


def actual_finite_objective(problem,vector,*,cells=(63,71,118),curvature_cap=7.2,
        curvature_weight=1.,high_gauss_weight=1.,high_codazzi_weight=1.,interior_gauss_weight=1.):
    trap,data=problem.evaluate(vector)
    del data['lift'],data['fields_parameters'];gc.collect()
    curv=curvature_merit(problem,vector,cap=curvature_cap,weight=curvature_weight,data=data,jacobian=False)
    high=high_gauss_merit(problem,vector,weight=high_gauss_weight,data=data,jacobian=False)
    quad=gauss_cell_codazzi(problem,vector,order=2,high_weight=high_codazzi_weight,
        jacobian=False,block_cells=8,consumer=gauss_cell_positive_trace)
    raw_old=np.r_[quad['retained_residual'],trap[(problem.N-1)*problem.d:]]
    inside=interior_gauss_curvature(problem,vector,cells=cells,gauss_weight=interior_gauss_weight,
        curvature_cap=curvature_cap,curvature_weight=curvature_weight,jacobian=False)
    raw=np.r_[raw_old,inside['retained_residual']]
    groups=dict(raw=raw,node_curvature=curv['residual'],node_high_G=high['residual'],
        high_C=quad['high_residual'],interior_high_G=inside['high_residual'],interior_curvature=inside['curvature_residual'])
    r=np.concatenate(tuple(groups.values()))
    i,j=np.unravel_index(int(np.argmax(abs(quad['point_gauss']))),quad['point_gauss'].shape)
    info=dict(schema='fd2d-v18-v19-complete-value-objective-v1',rows=len(r),objective_norm=float(np.linalg.norm(r)),
        objective_squared=float(r@r),component_squared_norms={k:float(v@v) for k,v in groups.items()},
        raw_maximum=float(np.max(abs(raw))),previous_raw_maximum=float(np.max(abs(raw_old))),
        node_full_G_maximum=float(np.max(abs(data['full_gauss']))),
        node_formal_curvature=curv['info']['sampled_formal_curvature_maximum'],
        whole_G2_Gauss_maximum=float(np.max(abs(quad['point_gauss']))),
        whole_G2_peak=dict(cell=int(j//2),s=float(quad['quadrature_points'][j]),
            xi=float(problem.chart.theta[i]),G=float(quad['point_gauss'][i,j])),
        whole_C_average_maximum=float(np.max(abs(quad['full_codazzi_cells']))),
        high_C_average_maximum=float(np.max(abs(quad['omitted_codazzi_cells']))),
        interior=inside['info'],axes={k:float(data['axes'][k]) for k in ('A','B','gap')},
        minimum_active_coast_n=data['gauss_l_delta']['sampled_minimum_active_n'],
        no_Jacobian=True,no_BVP=True,continuous_certificate=False)
    return info
