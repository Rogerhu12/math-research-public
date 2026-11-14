#!/usr/bin/env python3
"""R153 actual initializer and a targeted nonzero local derivative check.

The prior immutable affine-atlas state is changed explicitly to the local
positive-n Gauss-l field. Removing fully inactive l-hat coefficients is an
exact gauge operation only after that representation change. No BVP/body.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,copy,datetime,gc,json,resource,time,traceback
from pathlib import Path
import numpy as np
from scipy import sparse
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_raw_bump_positive_gauss import PositiveGaussRawBumpDAE,checkpoint_arrays
from fd2d_gc_gauss_cell_positive_gauss import gauss_cell_positive_gauss
from fd2d_gc_gauss_cell_codazzi_chunked import gauss_cell_codazzi
from fd2d_gc_positive_gauss_merit import curvature_merit,high_gauss_merit
from fd2d_gc_bump_residual_locations import residual_locations


def local_view(problem,start,stop):
    view=copy.copy(problem);view.x=problem.x[start:stop+1].copy();view.N=len(view.x)
    view.h=np.diff(view.x);view.size=view.N*view.q+view.parameter_count
    view.affine_residual_size=view.N*view.q+2*view.K+2
    view.coords={k:np.asarray(v,float) for k,v in view.chart.coordinates(view.x).items()}
    view._operator_cache={};view._cell_gauss_view_cache=None;view._chunked_gauss_codazzi_views=None
    view.residual_size=view.affine_residual_size-np.count_nonzero(view.window()[:-1]==1)*view.e
    return view


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','warm-start','radius-packet','reference-inlet','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Choose a fresh actual-field stem')
    started=time.monotonic();here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-R153-initializer-targeted-JVP-check-v1',source=identity(__file__),
        sources={n:identity(here/n) for n in ('fd2d_gc_raw_bump_positive_gauss.py','fd2d_gc_positive_gauss_l.py',
            'fd2d_gc_gauss_cell_positive_gauss.py','fd2d_gc_positive_gauss_merit.py','fd2d_gc_positive_gauss_bounded_schur.py')},
        input=identity(args.warm_start),candidate=identity(args.candidate),
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),completed=False,
        nonlinear_BVP_performed=False,continuous_certificate=False,exception=None)
    def save():
        report.update(seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        old=load_npz(args.warm_start);proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:raise ValueError('Wrong radius packet')
        witness=dict(**identity(args.radius_packet),candidate_sha256=proof['candidate_sha256'])
        problem=PositiveGaussRawBumpDAE(args.candidate,modes=int(old['modes']),max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=.1,minimum_active_n=.05)
        if str(old['candidate_sha256'])!=report['candidate']['sha256'] or not np.array_equal(old['mesh'],problem.x):
            raise ValueError('Different physical input or computational mesh')
        for key in ('angular_atlas_definition','coast_reference_definition','reference_evaluation_definition','seed_weight_definition'):
            if json.loads(str(old[key]))!=getattr(problem,key):raise ValueError('Different declared affine field: '+key)
        before=np.r_[old['corrections'].ravel(),old['parameters']]
        vector=problem.impose_linear_boundary_values(before)
        report['new_field_definition']=problem.gauss_l_definition
        report['conversion']=dict(kind='explicit nonlinear actual-field replacement then exact inert-hat gauge',
            physical_parameters_unchanged=bool(np.array_equal(before[-problem.parameter_count:],vector[-problem.parameter_count:])),
            physical_g_changed=False,mesh_unchanged=True,angular_atlas_unchanged=True,known_lifting_unchanged=True,
            old_actual_field_preserved=False,inactive_l_raw_nodes=problem.inactive_l_raw_nodes.tolist(),
            inactive_l_columns=len(problem.additional_fixed_field_indices),coefficient_gauge_change=float(np.max(abs(vector-before))))
        report['warm']=save_npz(stem.with_name(stem.name+'-warm.npz'),**checkpoint_arrays(problem,vector,report['candidate']['sha256']),
            initializer_definition=np.array(json.dumps(report['conversion'],sort_keys=True)),initializer_input_sha256=np.array(report['input']['sha256']))
        # One full actual finite evaluation, without a full Jacobian.
        raw,data=problem.evaluate(vector);del data['lift']
        curv=curvature_merit(problem,vector,data=data,jacobian=False)
        high=high_gauss_merit(problem,vector,data=data,jacobian=False)
        del data['fields_parameters'];gc.collect()
        quad=gauss_cell_codazzi(problem,vector,order=2,high_weight=1,jacobian=False,block_cells=8,consumer=gauss_cell_positive_gauss)
        residual=np.r_[quad['retained_residual'],raw[(problem.N-1)*problem.d:]]
        data['codazzi_cells']=quad['retained_cells'];n,m,l=(data['fields'][:,:,j] for j in range(3));disc=np.hypot(l-n,2*m)
        w=problem.window();plateau=w==1
        report['actual_initial']=dict(raw_maximum=float(np.max(abs(residual))),full_G_node_maximum=float(np.max(abs(data['full_gauss']))),
            platform_full_G_maximum=float(np.max(abs(data['full_gauss'][:,plateau]),initial=0.)),
            exact_G_identity_roundoff=float(np.max(abs(data['full_gauss']-(1-w)[None,:]*data['affine_full_gauss']))),
            formal_curvature_maximum=float(np.max(np.maximum(abs(n+l+disc),abs(n+l-disc)))/2),
            active_n_node_minimum=data['gauss_l_delta']['sampled_minimum_active_n'],
            sampled_full_average_C_maximum=quad['info']['sampled_full_average_codazzi_maximum'],
            sampled_high_average_C_maximum=quad['info']['sampled_omitted_average_codazzi_maximum'],
            gap=float(data['axes']['gap']),actual_node_l_change_maximum=float(np.max(abs(l-data['affine_fields'][:,:,2]))),
            curvature_merit=curv['info'],high_gauss_merit=high['info'])
        report['actual_initial_locations']=residual_locations(problem,vector,data,{'omitted_codazzi_cells':quad['omitted_codazzi_cells']},7.2)
        del data,quad,raw,residual;gc.collect();save()
        # Exit rim cell and its right neighbor: active quotient, nonzero
        # tail/profile/state columns and the return to unchanged w=0.
        start,stop=71,73;view=local_view(problem,start,stop)
        y,p=problem.unpack(vector);v=np.r_[y[start:stop+1].ravel(),p]
        def bundles(v,jacobian=False):
            if jacobian:r,J,d=view.evaluate(v,jacobian=True)
            else:r,d=view.evaluate(v);J=None
            c=curvature_merit(view,v,cap=1.,data=d,jacobian=jacobian)
            g=high_gauss_merit(view,v,data=d,jacobian=jacobian)
            q=gauss_cell_positive_gauss(view,v,jacobian=jacobian)
            out={'node':r,'curvature':c['residual'],'high_G':g['residual'],
                'endpoint_C':q['retained_residual'],'high_C':q['high_residual']}
            jj={'node':J,'curvature':c['jacobian'],'high_G':g['jacobian'],
                'endpoint_C':q['retained_jacobian'],'high_C':q['high_jacobian']}
            return out,jj
        value,jac=bundles(v,True);directions=[]
        state=np.zeros(view.size);state[:view.N*view.q]=.07*np.sin(.23+np.arange(view.N*view.q)*.63)
        directions.append(('state',state))
        param=np.zeros(view.size);off=view.N*view.q
        param[off+view.tail_parameter_slice.start:off+view.tail_parameter_slice.stop]=.03*np.cos(.7+np.arange(view.K+1)*.31)
        param[off+view.profile_parameter_slice.start:off+view.profile_parameter_slice.stop]=.0003*np.cos(.2+np.arange(len(problem.profile.supports))*.73)
        directions.append(('tail_and_physical_profile',param))
        checks=[]
        for name,direction in directions:
            exact={key:A@direction for key,A in jac.items()}
            for step in (2e-5,1e-5):
                plus,_=bundles(v+step*direction);minus,_=bundles(v-step*direction)
                for key in exact:
                    if plus[key].shape!=exact[key].shape or minus[key].shape!=exact[key].shape:
                        raise ValueError('Actual curvature active set changed in the local check')
                    fd=(plus[key]-minus[key])/(2*step);difference=fd-exact[key]
                    checks.append(dict(direction=name,step=step,block=key,rows=len(fd),
                        analytic_norm=float(np.linalg.norm(exact[key])),max_error=float(np.max(abs(difference),initial=0.)),
                        relative_L2=float(np.linalg.norm(difference)/max(np.linalg.norm(exact[key]),1e-12))))
        report['local_derivative_check']=dict(original_node_range=[start,stop],s=view.x.tolist(),
            curvature_cap_for_nonzero_active_derivative=1.,rows=checks,
            maximum_relative_L2=max(c['relative_L2'] for c in checks))
        report['completed']=True;save()
        print(json.dumps(dict(completed=True,warm=report['warm'],initial=report['actual_initial'],JVP=report['local_derivative_check']['maximum_relative_L2']),allow_nan=False),flush=True)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise

if __name__=='__main__':main()
