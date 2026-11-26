#!/usr/bin/env python3
"""Verify and retain the identical actual R53 field in the v2 phase model.

No BVP solver is invoked. The source's actual successful solver provenance
is retained separately, and all raw collocation/RMS/BC and complete finite
metric gates are genuinely recomputed. Strict raw-function identities must
hold before the unchanged physical interpolant is accepted in new control
coordinates. The initial same-lambda result is not lambda continuation.
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
import scipy
import scipy.integrate._bvp as bvp

HERE=Path(__file__).resolve().parent
SCRIPTS=HERE.parent
sys.path.insert(0,str(HERE))
import warm_fixed_m3_model_v2 as model


def write(path,value):
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    tmp.replace(path)


def measure(obj,x,y,p):
    h=np.diff(x)
    cr,ym,f,fm=bvp.collocation_fun(obj.fun,y,p,x,h)
    spline=bvp.create_spline(y,f,x,h)
    rms=bvp.estimate_rms_residuals(obj.fun,spline,x,h,p,1.5*cr/h,fm)
    bc=obj.bc(y[:,0],y[:,-1],p)
    physical_bc=obj.terminal(y[:,-1],p)*obj.bcweights
    if not all(np.all(np.isfinite(v)) for v in (cr,f,fm,rms,bc,physical_bc)):
        raise FloatingPointError('Nonfinite actual finite-equation audit')
    return dict(cr=cr,f=f,fm=fm,rms=rms,bc=bc,physical_bc=physical_bc,spline=spline)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-run',type=Path,required=True)
    ap.add_argument('--probe-summary',type=Path,required=True)
    ap.add_argument('--outdir',type=Path,required=True)
    ap.add_argument('--phase-scale',type=float,default=1.)
    a=ap.parse_args()
    if not math.isfinite(a.phase_scale) or a.phase_scale<=0:
        raise ValueError('Positive finite phase scale required')
    repository = SCRIPTS.parent.parents[1].resolve()
    destination = a.outdir.resolve()
    if destination == repository or repository in destination.parents:
        raise ValueError("Generated raw and physical fields must stay outside the repository")
    a.outdir.mkdir(parents=True,exist_ok=False)
    begin=time.monotonic()
    record=dict(scope=__doc__,model_kind=model.KIND,status='preparing',
        command=[sys.executable,*sys.argv],solver_invoked=False,solver_success=None,
        finite_linear_candidate_pass=False,
        acceptance_kind='same_cartesian_map_verified_reexpression',
        fixed_metric=True,fixed_core=False,fixed_metric_refinement=False,
        fixed_metric_design_continuation=False,
        zero_control_anchor_handoff=True,same_cartesian_map_as_source=True,
        parameter_zero_meaning='log(q_aux/gauge_q)',
        parameter_meaning='d_j=phase_scale*p_(j-1), using actual inherited 1e-9 legacy scale floor',
        terminal_kind='original_linear_dn',original_actual_nonlinear_tail=False,
        complete_surface=False,C2_convergence_proven=False,
        source_run=str(a.source_run.resolve()),source_run_sha256=model.sha(a.source_run),
        probe_summary=str(a.probe_summary.resolve()),probe_summary_sha256=model.sha(a.probe_summary),
        scipy_version=scipy.__version__,scipy_bvp_sha256=model.sha(bvp.__file__),
        source_hashes={str(HERE/name):model.sha(HERE/name) for name in
            ('warm_zero_control_reexpression_v2.py','warm_fixed_m3_model_v2.py',
             'warm_supported_core_factory_v2.py','warm_supported_core_factory.py',
             'warm_auxiliary_domain_guard.py')})
    def save():
        record['elapsed']=time.monotonic()-begin
        write(a.outdir/'run.json',record)
        summary=dict(status=record['status'],stages=[],error=record.get('error'),
            progress=record.get('progress'),result=dict(
                model_kind=model.KIND,acceptance_kind=record['acceptance_kind'],
                solver_invoked=False,solver_success=None,
                finite_linear_candidate_pass=record['finite_linear_candidate_pass'],
                run=str((a.outdir/'run.json').resolve()),
                run_sha256=model.sha(a.outdir/'run.json'),
                homotopy=record.get('homotopy'),modes=record.get('modes'),
                raw_return=record.get('raw_return'),
                metric_diagnostics=record.get('metric_diagnostics'),
                zero_control_identity=record.get('zero_control_identity')))
        write(a.outdir/'summary.json',summary)
    def event(name,**values):
        record['progress']=dict(event=name,**values)
        save()
        print(json.dumps(dict(event=name,elapsed=time.monotonic()-begin,**values)),flush=True)
    try:
        source=model.load(a.source_run)
        probe=model.load(a.probe_summary)
        if (probe.get('status')!='read_only_probe_complete' or
                probe.get('source_run_sha256')!=model.sha(a.source_run)):
            raise ValueError('The actual completed raw-grid probe must bind this exact accepted source')
        result=probe['result']
        probed=[*result['raw_equation_gaps'].values(),*result['frozen_chart_gap'].values(),
                *result['complete_core_zero_control_jets'].values(),result['initial_projection'],
                *result['same_physical_interpolant_jet_gaps'].values()]
        if not all(row.get('bitwise_equal') for row in probed):
            raise ValueError('The actual independent probe did not establish the required literal equalities')
        if (source.get('error') or source.get('fixed_metric') or source.get('fixed_metric_refinement') or
                not source.get('solver_success') or not source.get('raw_return',{}).get('success')):
            raise ValueError('Require the actual accepted original R53 design return')
        gates=source['gates']
        if (source.get('prefix_audit',{}).get('metric_l1',math.inf)>1e-6 or
                source.get('prefix_audit',{}).get('physical_bc_max',math.inf)>gates['physical_bc_tol']):
            raise ValueError('The original accepted finite metric/physical boundary gate changed')
        if gates['physical_bc_tol']/gates['bc_tol']!=.02:
            raise ValueError('The original boundary normalization is not .02')
        design,origin,signature,origin_p=model.bootstrap(a.source_run)
        raw_path=a.source_run.parent/source['raw_return']['file']
        if model.sha(raw_path)!=source['raw_return']['sha256']:
            raise ValueError('The actual original raw return changed')
        with np.load(raw_path,allow_pickle=False) as raw:
            raw_values={name:raw[name].copy() for name in raw.files}
        x,y,p0,pscale=(raw_values[k] for k in ('x','y','p','pscale'))
        if not np.array_equal(pscale,design.pscale):
            raise ValueError('The actual source parameter scales changed')
        old_initial=design.initial(p0).copy()
        baseline=design._core
        oldflow=design.flow(p0[0])
        source_mean=source.get('prefix_audit',{}).get('samples_psi')
        if source_mean!=1168:
            raise ValueError('A same-Cartesian-map reexpression requires the actual original mean1168 rule')
        frozen={**copy.deepcopy(design.cfg),'delta':float(design.cfg['delta']+p0[0])}
        if frozen!=source['frozen_profile']:
            raise ValueError('The actual delta binding differs')
        definition=dict(gauge_q=float(design.q),phase_control_scale=a.phase_scale,
            phase_parameter_scale_rule=copy.deepcopy(model.SCALE_RULE),
            anchor_support_coefficients=baseline.original.coefficients.tolist(),
            anchor_core_settings=copy.deepcopy(source['core_settings']),
            anchor_run=str(a.source_run.resolve()),anchor_run_sha256=model.sha(a.source_run),
            homotopy=float(baseline.homotopy))
        port=Path(model.option(source,'--port'))
        radial=dict(chart_join=float(design.chart_join),
            chart_reference_prefix=float(design.chart_reference_prefix),
            chart_breaks=np.asarray(design.chart_breaks).tolist(),
            meaning='literal original design numerical radial coordinate frozen at the accepted actual delta')
        record.update(origin_design_run=str(a.source_run.resolve()),
            origin_design_sha256=model.sha(a.source_run),frozen_source_signature=signature,
            frozen_profile=frozen,physical_tail_parameters=copy.deepcopy(source['physical_tail_parameters']),
            physical_tail_cut=copy.deepcopy(source['physical_tail_cut']),
            angular_chart=copy.deepcopy(source['angular_chart']),gauge_q=float(design.q),
            warp_reference=float(source['warp_reference']),warm_definition=definition,
            frozen_radial_chart=radial,**model.provider_bindings(),
            linear_port_path=str(port.resolve()),linear_port_sha256=model.sha(port),
            modes=design.M,angular=design.nt,mean_nodes=1168,bc_normalization=.02,
            homotopy=float(baseline.homotopy),source_lambda=float(baseline.homotopy),
            gates=dict(tol=gates['tol'],bc_tol=gates['bc_tol'],
                physical_bc_tol=gates['physical_bc_tol'],metric_component_fft=1e-6,
                metric_sample_operator=1e-6,max_nodes=gates.get('max_nodes')),
            parameter_scales=design.pscale.tolist(),
            source_solver_provenance=dict(run=str(a.source_run.resolve()),
                run_sha256=model.sha(a.source_run),raw_sha256=model.sha(raw_path),
                solver_success=True,raw_success=True,
                raw_status=source['raw_return'].get('status'),
                raw_message=source['raw_return'].get('message'),
                scope='Actual original solve; no new solve is claimed for the coordinate reexpression'))
        obj=model.build_model(design,origin,record,anchor_baseline=baseline)
        p=np.zeros(obj.M)
        new_initial=obj.initial(p).copy()
        flow=obj.flow(0.)
        identity=dict(zero_phase_controls=bool(np.all(obj._core.controls==0.)),
            literal_baseline_object=obj._core.baseline is baseline,
            same_gauge=design.q==obj.q,same_modes=design.M==obj.M,
            same_angular_projection=design.nt==obj.nt,
            initial_projection_bitwise_equal=bool(np.array_equal(old_initial,new_initial)),
            same_basis=bool(np.array_equal(oldflow.B,flow.B)),
            physical_profile_end_equal=oldflow.end==flow.end,
            prefix_end_equal=oldflow.prefix_end==flow.prefix_end,
            same_chart_join=design.chart_join==obj.chart_join,
            same_chart_reference_prefix=design.chart_reference_prefix==obj.chart_reference_prefix)
        theta=2*np.pi*np.arange(1168)/1168
        before,after=baseline.evaluate(theta),obj._core.evaluate(theta)
        for name in ('F','Ft','Ftt'):
            identity['core_'+name+'_bitwise_equal']=bool(np.array_equal(before[name],after[name]))
        old=measure(design,x,y,p0)
        new=measure(obj,x,y,p)
        for name in ('f','fm','cr','rms','bc','physical_bc'):
            identity[name+'_bitwise_equal']=bool(np.array_equal(old[name],new[name]))
        h=np.diff(x);middle=x[:-1]+.5*h;offset=.5*h*np.sqrt(3/7)
        all_points=np.r_[x,middle,middle+offset,middle-offset]
        oldchart,newchart=design.chart(all_points,p0[0]),obj.chart(all_points,0.)
        identity['all_original_RMS_chart_s_bitwise_equal']=bool(np.array_equal(oldchart[0],newchart[0]))
        identity['all_original_RMS_chart_ds_bitwise_equal']=bool(np.array_equal(oldchart[1],newchart[1]))
        identity['all_required_exact_equalities']=all(identity.values())
        record['zero_control_identity']=identity
        if not identity['all_required_exact_equalities']:
            raise ValueError('A required exact zero-control raw-function identity failed')
        rms=float(np.max(new['rms']));bc=float(np.max(abs(new['bc'])))
        physical_bc=float(np.max(abs(new['physical_bc'])))
        if rms>gates['tol'] or bc>gates['bc_tol'] or physical_bc>gates['physical_bc_tol']:
            raise ValueError('The actually recomputed original finite gate failed')
        record.update(original_scaled_bc_max=bc,linear_dn_physical_bc_max=physical_bc,
            status='raw_identity_and_finite_equations_verified')
        event('literal_raw_equations_verified',nodes=len(x),rms=rms,
              scaled_bc=bc,physical_bc=physical_bc,all_exact_equalities=True)
        raw_values.update(p=p,rms=new['rms'],pscale=obj.pscale)
        raw_file=a.outdir/'reexpressed-raw.npz'
        np.savez_compressed(raw_file,**raw_values)
        record['raw_return']=dict(file=raw_file.name,sha256=model.sha(raw_file),
            success=None,status=None,message='No solver invoked: verified identical raw field in new coordinates',
            accepted_representation=True,nodes=len(x),rms=rms,parameters=p.tolist(),
            original_raw_sha256=model.sha(raw_path),solver_invoked=False)
        source_physical=a.source_run.parent/'physical.npz'
        if model.sha(source_physical)!=source['physical_sha256']:
            raise ValueError('The original physical C2 interpolant changed')
        with np.load(source_physical,allow_pickle=False) as physical:
            data={key:physical[key].copy() for key in physical.files}
        if not np.array_equal(data['p'],p0):
            raise ValueError('Original physical/raw parameter vectors differ')
        data['p']=p
        physical_file=a.outdir/'physical.npz'
        np.savez_compressed(physical_file,**data)
        record.update(physical_sha256=model.sha(physical_file),
            original_physical_sha256=model.sha(source_physical),
            actual_q_aux=float(obj.support_amplitude),returned_phase_controls=obj._core.controls.tolist(),
            returned_core_summary=obj._core.summary(),
            fixed_mean_primitive=dict(nodes=1168,origin=0.,
                definition='Integral from 0 to s of the literal original frame.V_z mean on the same 1168 nodes',
                resampled=False))
        save()
        audit=model.module('_warm_v2_handoff_metric',SCRIPTS/'resume_m3/audit_full_relative_metric.py')
        floor=16*(3*obj.M+1)
        angles=sorted(set((floor,2*floor)))
        report=audit.audit_loaded_model(obj,audit.load_physical(physical_file),
            angular=angles,mean_nodes=1168,batch=8,target=1e-6)
        write(a.outdir/'relative-metric.json',report)
        record.update(relative_metric_sha256=model.sha(a.outdir/'relative-metric.json'),
            metric_diagnostics=report['rows'],actual_audit_angular=angles,
            original_audit_angular_floor=floor)
        passed=all(math.isfinite(row[key]) and row[key]<=1e-6
            for row in report['rows'] for key in
            ('legacy_max_component_fft_l1','sample_operator_max'))
        record.update(status='verified_zero_control_reexpression',finite_linear_candidate_pass=bool(passed))
        event('reexpression_full_metric_audited',finite_linear_candidate_pass=bool(passed),
              component_fft=[r['legacy_max_component_fft_l1'] for r in report['rows']],
              sample_operator=[r['sample_operator_max'] for r in report['rows']])
        if passed:
            model.accepted_input(a.outdir/'run.json')
        return 0 if passed else 2
    except Exception as error:
        record.update(status='error',error=repr(error),traceback=traceback.format_exc())
        event('error',error=repr(error))
        return 1
    finally:
        save()


if __name__=='__main__':
    sys.exit(main())
