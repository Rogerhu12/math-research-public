#!/usr/bin/env python3
"""Explicit same-material old-coast warm transfer and a small atlas/JVP check.
No nonlinear solve is performed. The new actual field and all projection
changes are saved; neither the old field nor an old residual is borrowed.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,copy,datetime,json,platform,resource,time,traceback
from pathlib import Path
import numpy as np
import scipy
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_raw_bump_ruling_atlas import RulingAtlasRawBumpDAE,checkpoint_arrays
from fd2d_gc_gauss_cell_codazzi_chunked import gauss_cell_codazzi
from fd2d_gc_gauss_cell_codazzi_endpoint_d2 import gauss_cell_codazzi_endpoint_d2


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('candidate','warm-start','radius-packet','reference-inlet','out-prefix'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path);ap.add_argument('--modes',type=int,default=15)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Unique output prefix required')
    start=time.monotonic();here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-global-ruling-atlas-explicit-warm-and-local-JVP-v1',
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source=identity(__file__),
        providers={name:identity(here/name) for name in ('fd2d_gc_frozen_ruling_atlas.py','fd2d_gc_raw_bump_ruling_atlas.py',
          'fd2d_gc_raw_bump_coast_reference.py','fd2d_gc_frozen_coast_reference.py','fd2d_k0_ruling_chart.py',
          'fd2d_gc_gauss_cell_codazzi_endpoint_d2.py','fd2d_gc_gauss_cell_codazzi_chunked.py')},
        candidate=identity(args.candidate),old_warm=identity(args.warm_start),reference_inlet=identity(args.reference_inlet),
        versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
        completed=False,nonlinear_solve_performed=False,continuous_certificate=False,exception=None)
    def save():
        report.update(seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    def event(label,**kw):print(json.dumps(dict(event=label,seconds=time.monotonic()-start,**kw),allow_nan=False),flush=True)
    save()
    try:
        proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:raise ValueError('Wrong radius packet')
        witness=dict(**identity(args.radius_packet),candidate_sha256=proof['candidate_sha256'])
        problem=RulingAtlasRawBumpDAE(args.candidate,modes=args.modes,max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=.1)
        report['angular_atlas_definition']=problem.angular_atlas_definition
        report['atlas_mesh_definition']=problem.atlas_mesh_definition
        report['reference_evaluation_definition']=problem.reference_evaluation_definition
        report['radius_proof']=witness;event('provider_ready',nodes=problem.N,work=problem.work)
        a=load_npz(args.warm_start)
        for k,v in [('candidate_sha256',report['candidate']['sha256']),('profile_kind','physical_bumps')]:
            if str(a[k])!=v:raise ValueError('Wrong old field '+k)
        if not np.array_equal(a['profile_supports'],problem.profile.supports):raise ValueError('Different physical bump supports')
        if json.loads(str(a['seed_weight_definition']))!=problem.seed_weight_definition:raise ValueError('Different actual seed lifting')
        if json.loads(str(a['coast_reference_definition']))!=problem.coast_reference_definition:raise ValueError('Different fixed coast lifting')
        vector,conversion=problem.warm_from_old_coast(a['mesh'],a['corrections'],a['parameters'])
        report['warm_conversion']=conversion
        report['warm']=save_npz(stem.with_name(stem.name+'-warm.npz'),**checkpoint_arrays(problem,vector,report['candidate']['sha256']))
        event('warm_saved',identity=report['warm'],projection_errors=conversion['correction_projection_component_maximum_errors']);save()
        interfaces=[]
        for x in (problem.chart.entry_start,problem.chart.entry_s,problem.chart.exit_s,problem.chart.exit_stop):
            left=problem.chart.coordinates([x],side='left');right=problem.chart.coordinates([x],side='right')
            interfaces.append(dict(s=x,value_and_angular_jumps={k:float(np.max(abs(left[k]-right[k]))) for k in ('u','u_xi','u_xixi')},
                radial_jet_jumps={k:float(np.max(abs(left[k]-right[k]))) for k in ('u_s','u_ss','u_sxi')}))
        report['interface_checks']=interfaces
        report['sampled_U_xi_minimum']=float(np.min(problem.coords['u_xi']))
        raw,data=problem.evaluate(vector);fields=data['fields'];n,m,l=(fields[:,:,j] for j in range(3));disc=np.hypot(l-n,2*m)
        quadrature=gauss_cell_codazzi(problem,vector,order=2,high_weight=1.,jacobian=False,block_cells=16,
            consumer=gauss_cell_codazzi_endpoint_d2)
        fullraw=np.r_[quadrature['retained_residual'],raw[(problem.N-1)*problem.d:]]
        report['actual_initial']=dict(raw_endpoint_maximum=float(np.max(abs(fullraw))),
            legacy_trapezoid_maximum=float(np.max(abs(raw))),full_gauss_node_maximum=float(np.max(abs(data['full_gauss']))),
            formal_curvature_node_maximum=float(np.max(np.maximum(abs(n+l+disc),abs(n+l-disc)))/2),
            endpoint_codazzi=quadrature['info'],gap=float(data['axes']['gap']))
        del data,fields,quadrature
        event('actual_new_initial',diagnostics=report['actual_initial']);save()
        # One real coast cell: the full 94 state columns and all parameter
        # columns remain present. This is a small interface/derivative check,
        # not a second global solve or an accuracy gate for the task.
        index=int(np.searchsorted(problem.x,.84)-1);view=copy.copy(problem)
        view.x=problem.x[index:index+2].copy();view.N=2;view.h=np.diff(view.x)
        view.size=view.N*view.q+view.parameter_count;view.residual_size=view.N*view.q+2*view.K+2
        view.coords={k:np.asarray(v,float) for k,v in view.chart.coordinates(view.x).items()}
        view._operator_cache={};view._cell_gauss_view_cache=None;view._chunked_gauss_codazzi_views=None
        yy,p=problem.unpack(vector);z=np.r_[yy[index:index+2].ravel(),p]
        result=gauss_cell_codazzi_endpoint_d2(view,z,order=2,high_weight=1.,jacobian=True)
        rng=np.random.default_rng(149);direction=rng.normal(size=z.shape);direction[:2*view.q]*=.1
        tail=direction[2*view.q+view.tail_parameter_slice.start:2*view.q+view.tail_parameter_slice.stop]
        control=p[view.tail_parameter_slice];tail[(control<1e-4)|(control>1.2-1e-4)]=0.;tail*=.03
        direction[2*view.q+view.profile_parameter_slice.start:]*=.001
        actual=np.r_[result['retained_jacobian']@direction,result['high_jacobian']@direction]
        checks=[]
        for h in (2e-6,1e-6):
            plus=gauss_cell_codazzi_endpoint_d2(view,z+h*direction,order=2,high_weight=1.,jacobian=False)
            minus=gauss_cell_codazzi_endpoint_d2(view,z-h*direction,order=2,high_weight=1.,jacobian=False)
            fd=(np.r_[plus['retained_residual'],plus['high_residual']]-np.r_[minus['retained_residual'],minus['high_residual']])/(2*h)
            checks.append(dict(h=h,absolute_maximum=float(np.max(abs(fd-actual))),
                relative_l2=float(np.linalg.norm(fd-actual)/max(np.linalg.norm(actual),1e-30))))
        report['local_nonzero_JVP']=dict(cell=index,interval=view.x.tolist(),
            state_direction_l2=float(np.linalg.norm(direction[:2*view.q])),tail_direction_l2=float(np.linalg.norm(tail)),
            profile_direction_l2=float(np.linalg.norm(direction[2*view.q+view.profile_parameter_slice.start:])),checks=checks)
        report['reference_cache_statistics']=problem.coast_reference.cache_statistics()
        report['completed']=True;save();event('completed',warm=report['warm'],JVP=checks)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise

if __name__=='__main__':main()
