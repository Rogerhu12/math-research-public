"""Explicit R152 background integration composed with the R153 field.

Only the known *affine* lifting receives a separate fine quadrature rule.
The complete nonlinear Gauss-l correction and its Jacobian remain the
actual R153 Gauss2 contribution. In particular this is not R_new(fine,0)
minus R_new(G2,0), and does not treat the new field as affine in the state.
"""
from __future__ import annotations
import copy
import numpy as np
from scipy import sparse
from fd2d_gc_gauss_cell_positive_gauss import gauss_cell_positive_gauss
from fd2d_gc_hybrid_lifting_codazzi_d2 import known_lifting_correction,point_view
from fd2d_gc_codazzi_complement import _high
from fd2d_gc_d2_complements import d2_high_rows


def known_coast_lifting_correction(problem,parameters,*,known_order=8,jacobian=True,point_batch=8):
    """Fine affine integration only on cells meeting the declared coast.

    The selection is a fixed physical interval test on each actual cell;
    it is independent of assembly block size and of optimized parameters.
    All other cells retain the previous finite Gauss2 rule explicitly.
    """
    e,f=problem.gauss_l_definition['support']
    ids=np.flatnonzero((problem.x[:-1]<f)&(problem.x[1:]>e))
    change=np.zeros((problem.work,problem.N-1,2))
    partial=np.zeros((problem.work,problem.N-1,2,problem.parameter_count)) if jacobian else None
    if not len(ids):return dict(change=change,partial=partial,cells=[],fixed_boundaries=[],selected_local_cells=[],support=[e,f])
    start,stop=int(ids[0]),int(ids[-1])+1
    if not np.array_equal(ids,np.arange(start,stop)):raise ValueError('Declared coast cells must form one interval')
    key=np.asarray(problem.x[start:stop+1],float).tobytes()
    cached=getattr(problem,'_positive_known_coast_view',None)
    if cached is None or cached[0]!=key:
        view=point_view(problem,problem.x[start:stop+1])
        problem._positive_known_coast_view=(key,view)
    else:view=cached[1]
    known=known_lifting_correction(view,parameters,known_order=known_order,jacobian=jacobian,point_batch=point_batch)
    change[:,start:stop]=known['change']
    if jacobian:partial[:,start:stop]=known['partial']
    return dict(change=change,partial=partial,cells=[dict(row,local_cell=row['local_cell']+start) for row in known['cells']],
        fixed_boundaries=known['fixed_boundaries'],selected_local_cells=ids.tolist(),support=[e,f])


def gauss_cell_positive_gauss_coast_hybrid(problem,vector,*,order=2,high_weight=1.,jacobian=True,
                                    known_order=8,point_batch=8):
    if order!=2:raise ValueError('The explicitly retained nonlinear correction rule is Gauss2')
    if (type(problem).__module__!='fd2d_gc_raw_bump_positive_gauss'
            or type(problem).__name__!='PositiveGaussRawBumpDAE'):
        raise ValueError('Bind the actual R153 field and its unchanged affine lifting explicitly')
    base=gauss_cell_positive_gauss(problem,vector,order=2,high_weight=high_weight,jacobian=jacobian)
    _,p=problem.unpack(np.asarray(vector,float))
    known=known_coast_lifting_correction(problem,p,known_order=known_order,jacobian=jacobian,point_batch=point_batch)
    change=known['change'];rows=d2_high_rows(problem)
    low=np.concatenate((problem.PE@change[:,:,0],problem.PO@change[:,:,1]),axis=0).T
    high=np.stack((_high(change[:,:,0],problem.E,problem.PE),_high(change[:,:,1],problem.O,problem.PO)),axis=-1)
    result=dict(base)
    result['retained_cells']=base['retained_cells']+low
    result['retained_residual']=result['retained_cells'].ravel()
    result['full_codazzi_cells']=base['full_codazzi_cells']+change
    result['omitted_codazzi_cells']=base['omitted_codazzi_cells']+high
    result['high_residual']=base['high_residual']+high_weight*np.concatenate((rows.project(high[:,:,0],'even'),rows.project(high[:,:,1],'odd')),axis=0).T.ravel()
    if jacobian:
        cells,pc=problem.N-1,problem.parameter_count
        lowp=np.zeros((cells,problem.d,pc));highp=np.zeros((cells,rows.cell_rows,pc))
        for j in range(cells):
            dp=known['partial'][:,j]
            lowp[j]=np.concatenate((problem.PE@dp[:,0],problem.PO@dp[:,1]),axis=0)
            highp[j]=high_weight*np.concatenate((rows.project(_high(dp[:,0],problem.E,problem.PE),'even'),rows.project(_high(dp[:,1],problem.O,problem.PO),'odd')),axis=0)
        offset=problem.N*problem.q
        for key,addition in (('retained_jacobian',lowp),('high_jacobian',highp)):
            old=base[key]
            result[key]=sparse.hstack((old[:,:offset],old[:,offset:]+sparse.csc_matrix(addition.reshape(-1,pc))),format='csc')
            result[key].eliminate_zeros()
    info=dict(base['info'])
    info.update(schema='fd2d-R153-nonlinear-G2-plus-R152-known-coast-cells-v1',
        actual_field_representation_changed=False,physical_metric_changed=False,finite_quadrature_rule_changed=True,
        formula='R153_G2(y,p)+Q2(F_p L_p)-Qfine(F_p L_p), where L_p is the original affine known lifting',
        nonlinear_Gauss_l_correction='Complete Delta l and Delta l_xi values and state/tail/profile Jacobian remain in R153_G2',
        nonlinear_field_treated_as_affine=False,
        new_field_at_zero_state_used_for_lifting_correction=False,
        state_jacobian='Exactly the complete nonlinear R153 Gauss2 state columns; no zero-field state Jacobian added',
        parameter_jacobian='Complete R153 columns plus derivative of the original known-affine-lifting average difference',
        known_lifting_quadrature_order=int(known_order),nonlinear_correction_quadrature_order=2,
        selected_coast_local_cells=known['selected_local_cells'],fine_known_physical_support=known['support'],
        all_other_cells_keep_original_G2=True,selection_independent_of_chunk_size_and_parameters=True,
        known_lifting_fixed_boundaries=known['fixed_boundaries'],known_lifting_cell_rules=known['cells'],
        retained_cell_maximum=float(np.max(abs(result['retained_cells']),initial=0.)),
        sampled_full_average_codazzi_maximum=float(np.max(abs(result['full_codazzi_cells']),initial=0.)),
        sampled_omitted_average_codazzi_maximum=float(np.max(abs(result['omitted_codazzi_cells']),initial=0.)),
        known_lifting_full_change_maximum=float(np.max(abs(change),initial=0.)),
        sampled_interior_Gauss_maximum=base['info']['sampled_interior_Gauss_maximum'],
        point_gauss_scope='Original R153 actual-field Gauss2 points; not fine known-lifting points',continuous_certificate=False)
    if jacobian:
        info['retained_jacobian_nonzeros']=int(result['retained_jacobian'].nnz)
        info['high_jacobian_nonzeros']=int(result['high_jacobian'].nnz)
    result['info']=info
    return result
