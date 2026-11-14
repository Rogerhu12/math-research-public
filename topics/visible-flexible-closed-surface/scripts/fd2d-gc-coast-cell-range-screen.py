#!/usr/bin/env python3
"""Small fixed-parameter local Codazzi range screen; never a BVP update.

Every selected original cell supplies only its two actual correction nodes.
The target metric, central/tail/profile parameters and reference definition
remain fixed. Unbounded least squares is a finite representation diagnostic,
not a field satisfying the global boundary, Gauss, or curvature conditions.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,copy,datetime,json,resource,time,traceback
from pathlib import Path
import numpy as np
from scipy import sparse,linalg
from scipy.optimize import lsq_linear
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_raw_bump_coast_reference import CoastReferenceRawBumpDAE
from fd2d_gc_gauss_cell_codazzi_d2 import gauss_cell_codazzi_d2
from fd2d_gc_gauss_cell_codazzi import _view


def local_problem(problem,cell):
    if not 0<=cell<problem.N-1:raise ValueError('Cell outside the saved field')
    view=copy.copy(problem)
    view.x=problem.x[cell:cell+2].copy();view.N=2;view.h=np.diff(view.x)
    view.size=view.N*view.q+view.parameter_count
    view.residual_size=view.N*view.q+2*view.K+2
    view.coords={k:np.asarray(v,float) for k,v in view.chart.coordinates(view.x).items()}
    view._operator_cache={};view._cell_gauss_view_cache=None;view._chunked_gauss_codazzi_views=None
    return view


def point_fields(problem,vector):
    rule=_view(problem,2);qv,tau=rule['view'],rule['tau'];y,p=problem.unpack(vector)
    yq=((1-tau)[None,:,None]*y[:-1,None,:]+tau[None,:,None]*y[1:,None,:]).reshape(qv.N,qv.q)
    lift=qv.lifting(p[qv.profile_parameter_slice],p[qv.tail_parameter_slice])
    fields=np.stack((qv.E@yq[:,:qv.e].T,qv.O@yq[:,qv.e:qv.d].T,qv.E@yq[:,qv.d:].T),axis=-1)+lift['values']
    n,m,l=(fields[:,:,k] for k in range(3));disc=np.hypot(l-n,2*m)
    return dict(n_minimum=float(n.min()),n_maximum=float(n.max()),
        formal_curvature_maximum=float(np.max(np.maximum(abs(l+n+disc),abs(l+n-disc)))/2))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for flag in ('candidate','field','radius-packet','reference-inlet','reference-cache','out-prefix'):
        ap.add_argument('--'+flag,type=Path,required=True)
    ap.add_argument('--cell',type=int,action='append',required=True)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a unique output stem')
    stem.parent.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    report=dict(schema='fd2d-fixed-parameter-local-Codazzi-range-screen-v1',source=identity(__file__),
        inputs={k:identity(getattr(args,k)) for k in ('candidate','field','radius_packet','reference_inlet','reference_cache')},
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),completed=False,exception=None,
        original_field_modified=False,nonlinear_BVP_performed=False,continuous_certificate=False,
        scope='Finite fixed-p affine Codazzi ranges with two free endpoint correction nodes; no global boundary or Gauss/curvature constraints',cells=[])
    def save():
        report['seconds']=time.monotonic()-start;report['peak_RSS_KiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        data=load_npz(args.field);proof=json.loads(args.radius_packet.read_text());candidate=identity(args.candidate)
        if not proof['passed'] or proof['candidate_sha256']!=candidate['sha256']:raise ValueError('Wrong radius packet')
        saved=json.loads(str(data['coast_reference_definition']))
        problem=CoastReferenceRawBumpDAE(args.candidate,modes=int(data['modes']),max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            reference_rim_fraction=float(saved['rim_fraction']),base_lower_bound='4/5',
            base_lower_provenance=dict(**identity(args.radius_packet),candidate_sha256=candidate['sha256']),radius_floor=.1)
        if not np.array_equal(data['mesh'],problem.x) or not np.array_equal(data['profile_supports'],problem.profile.supports):
            raise ValueError('Saved mesh/supports differ from the explicit provider')
        if saved!=problem.coast_reference_definition:raise ValueError('Reference field definition mismatch')
        if json.loads(str(data['seed_weight_definition']))!=problem.seed_weight_definition:raise ValueError('Seed lifting differs')
        y,p=np.asarray(data['corrections'],float),np.asarray(data['parameters'],float)
        report['functional_definition']=saved;report['modes']=problem.K;report['work']=problem.work
        arrays={}
        for cell in args.cell:
            view=local_problem(problem,cell);z=np.r_[y[cell:cell+2].ravel(),p]
            original=gauss_cell_codazzi_d2(view,z,order=2,jacobian=True)
            r=np.r_[original['retained_residual'],original['high_residual']]
            J=sparse.vstack((original['retained_jacobian'],original['high_jacobian']),format='csc')[:,:2*view.q].toarray()
            scale=np.linalg.norm(J,axis=0);nonzero=scale>0
            A=J[:,nonzero]/scale[nonzero]
            row=dict(cell=cell,endpoints=view.x.tolist(),matrix_shape=list(J.shape),
                parameters_fixed=True,actual_before_l2=float(np.linalg.norm(r)),
                actual_before_full_mean_maximum=original['info']['sampled_full_average_codazzi_maximum'],
                actual_before_high_mean_maximum=original['info']['sampled_omitted_average_codazzi_maximum'],
                before_point_fields=point_fields(view,z),cases=[])
            for cutoff in (1e-10,1e-12,1e-14):
                scaled,_,rank,singular=linalg.lstsq(A,-r,cond=cutoff,lapack_driver='gelsd')
                change=np.zeros(2*view.q);change[nonzero]=scaled/scale[nonzero]
                zz=z.copy();zz[:2*view.q]+=change
                direct=gauss_cell_codazzi_d2(view,zz,order=2,jacobian=False)
                rr=np.r_[direct['retained_residual'],direct['high_residual']]
                predicted=r+J@change
                row['cases'].append(dict(relative_svd_cutoff=cutoff,numerical_rank=int(rank),
                    largest_scaled_singular_value=float(singular[0]),smallest_scaled_singular_value=float(singular[-1]),
                    predicted_l2=float(np.linalg.norm(predicted)),actual_l2=float(np.linalg.norm(rr)),
                    affine_backsubstitution_maximum=float(np.max(abs(predicted-rr))),
                    correction_change_maximum=float(np.max(abs(change))),correction_change_l2=float(np.linalg.norm(change)),
                    actual_full_mean_maximum=direct['info']['sampled_full_average_codazzi_maximum'],
                    actual_high_mean_maximum=direct['info']['sampled_omitted_average_codazzi_maximum'],
                    actual_point_Gauss_maximum=direct['info']['sampled_interior_Gauss_maximum'],
                    point_fields=point_fields(view,zz),admissible_global_field_claimed=False))
                key=f'cell{cell}_cutoff{cutoff:.0e}';arrays[key+'_corrections']=zz[:2*view.q].reshape(2,view.q)
                arrays[key+'_actual_residual']=rr;arrays[key+'_singular_values']=singular
            # Every sampled component of a symmetric matrix with spectral
            # norm <= C has absolute value <= C. Fourier row L1 bounds give
            # a deliberately loose necessary coefficient box. This does
            # not assert that the fitted field obeys the curvature cap.
            cap=1/.136
            lift=view.lifting(p[view.profile_parameter_slice],p[view.tail_parameter_slice])['values']
            lift_coeff=np.concatenate((view.PE@lift[:,:,0],view.PO@lift[:,:,1],view.PE@lift[:,:,2]),axis=0).T
            bound=np.r_[np.sum(abs(view.PE),axis=1),np.sum(abs(view.PO),axis=1),np.sum(abs(view.PE),axis=1)]*cap
            lower=(-bound[None,:]-lift_coeff).ravel()
            upper=(bound[None,:]-lift_coeff).ravel()
            current=z[:2*view.q]
            fit=lsq_linear(A,-r,bounds=((lower-current)[nonzero]*scale[nonzero],
                (upper-current)[nonzero]*scale[nonzero]),method='bvls',tol=1e-11,max_iter=200)
            change=np.clip(current,lower,upper)-current
            change[nonzero]=fit.x/scale[nonzero]
            zz=z.copy();zz[:2*view.q]+=change
            direct=gauss_cell_codazzi_d2(view,zz,order=2,jacobian=False)
            rr=np.r_[direct['retained_residual'],direct['high_residual']]
            row['necessary_component_coefficient_box_case']=dict(cap=cap,
                bound_kind='Discrete Fourier row L1 bound implied by componentwise sample cap; deliberately loose, not a sufficient curvature condition',
                solver_status=int(fit.status),solver_message=fit.message,optimality=float(fit.optimality),iterations=int(fit.nit),
                actual_l2=float(np.linalg.norm(rr)),predicted_l2=float(np.linalg.norm(r+J@change)),
                actual_full_mean_maximum=direct['info']['sampled_full_average_codazzi_maximum'],
                actual_high_mean_maximum=direct['info']['sampled_omitted_average_codazzi_maximum'],
                correction_change_maximum=float(np.max(abs(change))),
                actual_point_Gauss_maximum=direct['info']['sampled_interior_Gauss_maximum'],
                point_fields=point_fields(view,zz),admissible_global_field_claimed=False)
            arrays[f'cell{cell}_component_box_corrections']=zz[:2*view.q].reshape(2,view.q)
            arrays[f'cell{cell}_component_box_residual']=rr
            report['cells'].append(row);save();print(json.dumps(row),flush=True)
        arrays['parameters_fixed']=p;arrays['full_original_mesh']=problem.x
        report['local_states']=save_npz(stem.with_name(stem.name+'-local-states.npz'),**arrays)
        report['completed']=True;save();return 0
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise


if __name__=='__main__':raise SystemExit(main())
