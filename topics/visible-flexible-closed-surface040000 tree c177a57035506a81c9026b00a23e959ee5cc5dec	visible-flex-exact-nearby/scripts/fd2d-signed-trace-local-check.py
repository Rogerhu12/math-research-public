#!/usr/bin/env python3
"""One actual nonzero local field/cell check for the explicit signed model."""
from __future__ import annotations
import argparse,datetime,json,time,traceback,resource
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_signed_trace_problem import create_signed_trace_problem,checkpoint_arrays,actual_state_columns
from fd2d_gc_signed_trace_windows import signed_trace_delta
from fd2d_gc_positive_trace_branch import trace_delta_direction
from fd2d_gc_positive_trace_stream_normal import radial_view
from fd2d_gc_signed_trace_cells import gauss_cell_signed_trace


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--request',type=Path,required=True);ap.add_argument('--out-prefix',type=Path,required=True);args=ap.parse_args()
    started=time.monotonic();report=dict(schema='fd2d-R182-actual-signed-window-local-check-v1',source=identity(__file__),request=identity(args.request),started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),completed=False,whole_F_or_normal_evaluated=False)
    try:
        request=json.loads(args.request.read_text());s=request['settings'];origin=load_npz(s['warm_start']);witness=json.loads(Path(s['radius_packet']).read_text())
        windows=[dict(name='mid_positive',sign=1,breaks=[.90,.915,.985,.99]),dict(name='late_negative',sign=-1,breaks=[1.423,1.428,1.442,1.445])]
        problem=create_signed_trace_problem(s['candidate'],origin_field=s['warm_start'],windows=windows,
            modes=s['modes'],max_step=s['mesh_step'],gap=s['gap'],reference_inlet=s['reference_inlet'],reference_cache=s['reference_cache'],
            reference_rim_fraction=s['reference_rim_fraction'],minimum_active_n=s['minimum_active_n'],mesh_relative_tolerance=s['mesh_relative_tolerance'],
            base_lower_bound='4/5',base_lower_provenance=dict(**identity(s['radius_packet']),candidate_sha256=witness['candidate_sha256']),radius_floor=s['radius_floor'])
        old=np.r_[origin['corrections'].ravel(),origin['parameters']]
        vector=problem.impose_linear_boundary_values(old)
        y,p=problem.unpack(vector);oldy,_=problem.unpack(old)
        report.update(origin=identity(s['warm_start']),signed_definition=problem.signed_trace_definition,new_trace_gauge_nodes=problem.inactive_trace_nodes.tolist(),
            retained_node_indices=problem.retained_actual_gauss_nodes.tolist(),raw_gauge_rounding_or_change=float(np.max(abs(vector-old))),nodes=[],cells=[])
        rng=np.random.default_rng(182)
        fv=np.array([[[-.1,.2,-2.]]]);fx=np.array([[[.23,-.4,.19]]]);K=np.array([[.3]]);weight=np.array([[.6]])
        dv=rng.standard_normal((1,1,3));dx=rng.standard_normal((1,1,3));dk=np.array([[.17]])
        packet=signed_trace_delta(fv,fx,K,weight,-1)
        av,ax=trace_delta_direction(packet,dv[...,None],dx[...,None],dk[...,None])
        step=2e-7
        plus=signed_trace_delta(fv+step*dv,fx+step*dx,K+step*dk,weight,-1)
        minus=signed_trace_delta(fv-step*dv,fx-step*dx,K-step*dk,weight,-1)
        err=max(float(np.max(abs((plus['delta']-minus['delta'])/(2*step)-av[...,0]))),float(np.max(abs((plus['delta_xi']-minus['delta_xi'])/(2*step)-ax[...,0]))))
        if err>1e-8:raise ArithmeticError('Negative sign full angular/metric chain mismatch')
        report['negative_algebra_combined_JVP_error']=err
        for node in (84,118):
            view=radial_view(problem,[node]);local=np.r_[y[node],p];oldlocal=np.r_[oldy[node],p]
            _,data=view.evaluate(local);_,before=view.evaluate(oldlocal)
            direction=rng.standard_normal(len(local));direction[:view.q]/=10;direction[view.q:]/=100
            dn,dm,dl=actual_state_columns(view,data,0)
            analytic=np.stack((dn@direction[:view.q],dm@direction[:view.q],dl@direction[:view.q]),axis=-1)
            analytic+=np.einsum('wcp,p->wc',data['fields_parameters'][:,0],direction[view.q:])
            _,plus=view.evaluate(local+step*direction);_,minus=view.evaluate(local-step*direction)
            numeric=(plus['fields'][:,0]-minus['fields'][:,0])/(2*step)
            absolute=float(np.max(abs(numeric-analytic)));relative=absolute/max(1.,float(np.max(abs(analytic))))
            if relative>2e-6:raise ArithmeticError('Actual signed node complete JVP mismatch')
            report['nodes'].append(dict(node=node,s=float(view.x[0]),values_u0=data['fields'][0,0].tolist(),K=float(data['profile_jet']['K'][0]),
                Gauss_max=float(np.max(abs(data['full_gauss']))),trace_weight=float(view.trace_window()[0]),
                exact_gauge_function_float_difference=float(np.max(abs(data['fields']-before['fields']))),
                analytic_JVP_max=float(np.max(abs(analytic))),JVP_absolute_error=absolute,JVP_relative_error=relative))
        for cell in (82,118):
            view=radial_view(problem,[cell,cell+1]);local=np.r_[y[cell:cell+2].ravel(),p]
            data=gauss_cell_signed_trace(view,local,jacobian=True)
            direction=rng.standard_normal(len(local));direction[:2*view.q]/=10;direction[2*view.q:]/=100
            plus=gauss_cell_signed_trace(view,local+step*direction,jacobian=False)
            minus=gauss_cell_signed_trace(view,local-step*direction,jacobian=False)
            checks={}
            for name in ('retained','high'):
                analytic=data[name+'_jacobian']@direction
                numeric=(plus[name+'_residual']-minus[name+'_residual'])/(2*step)
                absolute=float(np.max(abs(numeric-analytic),initial=0.));relative=absolute/max(1.,float(np.max(abs(analytic),initial=0.)))
                if relative>3e-6:raise ArithmeticError('Actual signed split-fine cell complete JVP mismatch: '+name)
                checks[name]=dict(absolute_error=absolute,relative_error=relative,analytic_max=float(np.max(abs(analytic),initial=0.)))
            report['cells'].append(dict(cell=cell,interval=view.x.tolist(),retained_l2=float(np.linalg.norm(data['retained_residual'])),high_l2=float(np.linalg.norm(data['high_residual'])),JVP=checks,quadrature=data['info']))
        arrays=checkpoint_arrays(problem,vector,str(origin['candidate_sha256']),refinement_definition=problem.radial_refinement_definition)
        warm=args.out_prefix.with_name(args.out_prefix.name+'-warm.npz');save_npz(warm,**arrays)
        restored=create_signed_trace_problem(s['candidate'],origin_field=s['warm_start'],saved_field=warm,windows=windows,
            modes=s['modes'],max_step=s['mesh_step'],gap=s['gap'],reference_inlet=s['reference_inlet'],reference_cache=s['reference_cache'],
            reference_rim_fraction=s['reference_rim_fraction'],minimum_active_n=s['minimum_active_n'],mesh_relative_tolerance=s['mesh_relative_tolerance'],
            base_lower_bound='4/5',base_lower_provenance=dict(**identity(s['radius_packet']),candidate_sha256=witness['candidate_sha256']),radius_floor=s['radius_floor'])
        if restored.signed_transition_from_original:raise ArithmeticError('Signed restart incorrectly relabelled as original transition')
        report.update(completed=True,passed=True,actual_warm=identity(warm),own_schema_restored=True,old_representation_not_spoofed=True)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        raise
    finally:
        report['seconds']=time.monotonic()-started;report['peak_RSS_KiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        report['providers']={n:identity(Path(__file__).with_name(n)) for n in ('fd2d_gc_signed_trace_windows.py','fd2d_gc_signed_trace_problem.py','fd2d_gc_signed_trace_cells.py','fd2d_gc_signed_trace_fine_cells.py')}
        args.out_prefix.with_name(args.out_prefix.name+'-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'completed':report['completed'],'seconds':report['seconds'],'nodes':report['nodes'],'cells':[{k:v for k,v in x.items() if k!='quadrature'} for x in report['cells']]}))

if __name__=='__main__':main()
