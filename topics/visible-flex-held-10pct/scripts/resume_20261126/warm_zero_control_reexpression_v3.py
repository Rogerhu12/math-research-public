#!/usr/bin/env python3
"""Actual zero-control v2 field -> new complementary-arc v3 family.

Only an accepted v2 zero-control R53 anchor is eligible. The two finite
control spaces differ; only their actual zero-control complete field is
shared. No new solver is invoked or claimed. All required raw-equation
identities and finite RMS/BC/fullmetric gates are recomputed before this
same-Cartesian-map reexpression can be accepted.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import copy
import json
import math
from pathlib import Path
import sys
import time
import traceback
import numpy as np

HERE=Path(__file__).resolve().parent
SCRIPTS=HERE.parent
sys.path.insert(0,str(HERE))
import warm_fixed_m3_model_v2 as prior
import warm_fixed_m3_model_v3 as model
from warm_zero_control_reexpression_v2 import measure,write


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-run',type=Path,required=True)
    ap.add_argument('--outdir',type=Path,required=True)
    a=ap.parse_args()
    repository=SCRIPTS.parent.parents[1].resolve()
    destination=a.outdir.resolve()
    if destination==repository or repository in destination.parents:
        raise ValueError('Generated raw and physical fields must stay outside the repository')
    a.outdir.mkdir(parents=True,exist_ok=False)
    start=time.monotonic()
    record=dict(scope=__doc__,model_kind=model.KIND,status='preparing',
        command=[sys.executable,*sys.argv],solver_invoked=False,solver_success=None,
        finite_linear_candidate_pass=False,acceptance_kind='same_cartesian_map_verified_reexpression',
        fixed_metric=True,fixed_core=False,fixed_metric_refinement=False,
        fixed_metric_design_continuation=False,same_cartesian_map_as_source=True,
        zero_control_anchor_handoff=True,same_finite_control_span_as_v2=False,
        parameter_zero_meaning='log(q_aux/gauge_q)',
        parameter_meaning='d_j=phase_scale*p_(j-1); new true complementary-arc sine family',
        terminal_kind='original_linear_dn',original_actual_nonlinear_tail=False,
        complete_surface=False,C2_convergence_proven=False,
        source_run=str(a.source_run.resolve()),source_run_sha256=model.sha(a.source_run),
        source_hashes={str(HERE/name):model.sha(HERE/name) for name in
            ('warm_zero_control_reexpression_v3.py','warm_fixed_m3_model_v3.py',
             'warm_complement_core_factory_v3.py','warm_supported_core_factory.py',
             'warm_auxiliary_domain_guard.py','warm_fixed_m3_model_v2.py',
             'warm_zero_control_reexpression_v2.py')})
    def save():
        record['elapsed']=time.monotonic()-start
        write(a.outdir/'run.json',record)
        value=dict(status=record['status'],stages=[],progress=record.get('progress'),
            error=record.get('error'),result=dict(model_kind=model.KIND,
                acceptance_kind=record['acceptance_kind'],solver_invoked=False,solver_success=None,
                finite_linear_candidate_pass=record['finite_linear_candidate_pass'],
                run=str((a.outdir/'run.json').resolve()),run_sha256=model.sha(a.outdir/'run.json'),
                modes=record.get('modes'),homotopy=record.get('homotopy'),
                raw_return=record.get('raw_return'),metric_diagnostics=record.get('metric_diagnostics'),
                zero_control_identity=record.get('zero_control_identity')))
        write(a.outdir/'summary.json',value)
    def event(name,**values):
        record['progress']=dict(event=name,**values)
        save()
        print(json.dumps(dict(event=name,elapsed=time.monotonic()-start,**values),allow_nan=False),flush=True)
    try:
        source=prior.accepted_input(a.source_run)
        if source['homotopy']!=source['warm_definition']['anchor_core_settings']['homotopy']:
            raise ValueError('The direct v3 handoff requires the unchanged R53 anchor lambda')
        raw_path=a.source_run.parent/source['raw_return']['file']
        with np.load(raw_path,allow_pickle=False) as raw:
            values={key:raw[key].copy() for key in raw.files}
        x,y,p0,pscale=(values[key] for key in ('x','y','p','pscale'))
        if np.any(p0!=0):
            raise ValueError('A nonzero v2 phase field is not a literal zero-control v3 anchor')
        design,origin,signature,_=model.bootstrap(source['origin_design_run'])
        if signature!=source['frozen_source_signature']:
            raise ValueError('The original source changed')
        old=prior.build_model(design,origin,source)
        old_initial=old.initial(p0).copy()
        old_core=old._core
        oldflow=old.flow(p0[0])
        if np.any(old_core.controls!=0) or not old_core._zero:
            raise ValueError('The actual reconstructed source core has nonzero phase controls')
        baseline=old_core.baseline
        if not np.array_equal(pscale,old.pscale):
            raise ValueError('The accepted actual scale array changed')
        for key in prior.CONTRACT_KEYS:
            record[key]=copy.deepcopy(source[key])
        definition=record['warm_definition']
        definition.update(phase_basis=copy.deepcopy(model.BASIS_RULE),
            basis_anchor_v2_run=str(a.source_run.resolve()),basis_anchor_v2_sha256=model.sha(a.source_run))
        record.update(basis_anchor_v2_run=str(a.source_run.resolve()),
            basis_anchor_v2_sha256=model.sha(a.source_run),**model.provider_bindings(),
            modes=old.M,angular=old.nt,homotopy=source['homotopy'],source_lambda=source['homotopy'],
            linear_port_path=source['linear_port_path'],linear_port_sha256=source['linear_port_sha256'],
            gates=copy.deepcopy(source['gates']),parameter_scales=old.pscale.tolist(),
            direct_source_model_kind=source['model_kind'])
        if source['acceptance_kind']=='same_cartesian_map_verified_reexpression':
            provenance=copy.deepcopy(source['source_solver_provenance'])
        else:
            provenance=dict(run=str(a.source_run.resolve()),run_sha256=model.sha(a.source_run),
                raw_sha256=model.sha(raw_path),solver_success=bool(source['solver_success']),
                raw_success=bool(source['raw_return']['success']),raw_status=source['raw_return']['status'],
                raw_message=source['raw_return']['message'])
        provenance['scope']='Actual successful upstream solver; neither coordinate reexpression invokes a new solver'
        record['source_solver_provenance']=provenance
        obj=model.build_model(design,origin,record,anchor_baseline=baseline)
        p=np.zeros(obj.M)
        initial=obj.initial(p).copy()
        flow=obj.flow(0.)
        identity=dict(source_actual_phase_controls_zero=bool(np.all(old_core.controls==0)),
            new_actual_phase_controls_zero=bool(np.all(obj._core.controls==0)),
            literal_common_R53_baseline=obj._core.baseline is old_core.baseline,
            same_gauge=bool(old.q==obj.q),same_modes=bool(old.M==obj.M),
            same_angular_projection=bool(old.nt==obj.nt),
            initial_projection_bitwise_equal=bool(np.array_equal(old_initial,initial)),
            same_basis=bool(np.array_equal(oldflow.B,flow.B)),
            physical_end_bitwise_equal=bool(oldflow.end==flow.end),
            prefix_end_bitwise_equal=bool(oldflow.prefix_end==flow.prefix_end),
            chart_join_bitwise_equal=bool(old.chart_join==obj.chart_join),
            chart_reference_prefix_bitwise_equal=bool(old.chart_reference_prefix==obj.chart_reference_prefix))
        theta=2*np.pi*np.arange(1168)/1168
        old_geometry,new_geometry=old_core.evaluate(theta),obj._core.evaluate(theta)
        for key in ('F','Ft','Ftt'):
            identity['core_'+key+'_bitwise_equal']=bool(np.array_equal(old_geometry[key],new_geometry[key]))
        old_values=measure(old,x,y,p0)
        new_values=measure(obj,x,y,p)
        for key in ('f','fm','cr','bc','physical_bc','rms'):
            identity[key+'_bitwise_equal']=bool(np.array_equal(old_values[key],new_values[key]))
        h=np.diff(x);mid=x[:-1]+.5*h;offset=.5*h*np.sqrt(3/7)
        probes=np.r_[x,mid,mid+offset,mid-offset]
        old_chart,new_chart=old.chart(probes,p0[0]),obj.chart(probes,0.)
        identity['all_raw_RMS_chart_s_bitwise_equal']=bool(np.array_equal(old_chart[0],new_chart[0]))
        identity['all_raw_RMS_chart_ds_bitwise_equal']=bool(np.array_equal(old_chart[1],new_chart[1]))
        identity['all_required_exact_equalities']=bool(all(identity.values()))
        record['zero_control_identity']=identity
        if not identity['all_required_exact_equalities']:
            raise ValueError('The new finite family failed a required complete zero-control identity')
        rms=float(np.max(new_values['rms']));bc=float(np.max(abs(new_values['bc'])))
        physical_bc=float(np.max(abs(new_values['physical_bc'])))
        gates=record['gates']
        if rms>gates['tol'] or bc>gates['bc_tol'] or physical_bc>gates['physical_bc_tol']:
            raise ValueError('The recomputed original finite equation gate failed')
        record.update(status='raw_identity_and_finite_equations_verified',
            original_scaled_bc_max=bc,linear_dn_physical_bc_max=physical_bc)
        event('literal_raw_equations_verified',nodes=len(x),rms=rms,scaled_bc=bc,
              physical_bc=physical_bc,all_exact_equalities=True)
        values.update(p=p,rms=new_values['rms'],pscale=obj.pscale)
        raw_file=a.outdir/'reexpressed-raw.npz'
        np.savez_compressed(raw_file,**values)
        record['raw_return']=dict(file=raw_file.name,sha256=model.sha(raw_file),success=None,status=None,
            accepted_representation=True,solver_invoked=False,nodes=len(x),rms=rms,parameters=p.tolist(),
            message='No solver invoked: identical zero-control field in a different finite phase family',
            original_raw_sha256=model.sha(raw_path))
        old_physical=a.source_run.parent/'physical.npz'
        with np.load(old_physical,allow_pickle=False) as saved:
            physical_data={key:saved[key].copy() for key in saved.files}
        if not np.array_equal(physical_data['p'],p0):
            raise ValueError('The bound raw/physical parameters differ')
        physical_data['p']=p
        physical_file=a.outdir/'physical.npz'
        np.savez_compressed(physical_file,**physical_data)
        record.update(physical_sha256=model.sha(physical_file),original_physical_sha256=model.sha(old_physical),
            returned_phase_controls=obj._core.controls.tolist(),actual_q_aux=float(obj.support_amplitude),
            returned_core_summary=obj._core.summary(),
            fixed_mean_primitive=dict(nodes=1168,origin=0.,
                definition='The same literal mean1168 primitive from s=0',resampled=False))
        save()
        audit=model.module('_warm_v3_handoff_metric',SCRIPTS/'resume_m3/audit_full_relative_metric.py')
        floor=16*(3*obj.M+1);angles=[floor,2*floor]
        report=audit.audit_loaded_model(obj,audit.load_physical(physical_file),
            angular=angles,mean_nodes=1168,batch=8,target=1e-6)
        write(a.outdir/'relative-metric.json',report)
        record.update(relative_metric_sha256=model.sha(a.outdir/'relative-metric.json'),
            metric_diagnostics=report['rows'],actual_audit_angular=angles,original_audit_angular_floor=floor)
        passed=bool(all(math.isfinite(row[key]) and 0<=row[key]<=1e-6
            for row in report['rows'] for key in ('legacy_max_component_fft_l1','sample_operator_max')))
        record.update(status='verified_zero_control_reexpression',finite_linear_candidate_pass=passed)
        event('new_family_zero_control_full_metric_audited',finite_linear_candidate_pass=passed,
            component_fft=[row['legacy_max_component_fft_l1'] for row in report['rows']],
            sample_operator=[row['sample_operator_max'] for row in report['rows']])
        if passed:
            model.accepted_input(a.outdir/'run.json')
        return 0 if passed else 2
    except Exception as error:
        record.update(status='error',error=repr(error),traceback=traceback.format_exc())
        event('error',error=repr(error));return 1
    finally:
        save()


if __name__=='__main__':
    sys.exit(main())
