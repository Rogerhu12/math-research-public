#!/usr/bin/env python3
"""Continuous metric of one new accepted warm field's explicit C2 prefix.

The original R62 interval/Taylor algorithm is reused with the actual M,
the exact common-right-two-jet field/chart, freshly certified true-core
arrays, the frozen endpoint-normalized profile, and literal mean1168.
No old field's numerical bounds, inlet repair, bridge or tail are reused.
No BVP, DN solve, or refinement acceptance is performed by this entry.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
from fractions import Fraction as Q
import gc
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback
import numpy as np
import mpmath as mp


REVIEWED={
    'resume_m3/certify_prefix_metric_interval_taylor.py':
        '6b36ccd6bab54fa35c6fe62a433f417faf7a51b80c35b798b17567eb22714986',
    'resume_m3/certify_r59_fixed_mean_ranges.py':
        'ab08dc1dc7f24f6e92e3d64fcc530767cb66f5ae5a2940f953460a3274b6a1a5',
    'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py':
        '6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7',
    'resume_20261126/seam_m3_prefix_pieces.py':
        'dd353c3306ea35dd068e25951917fd8d204635b9e4cc07a41f7957834cbee01d',
    'resume_20261126/seam_certify_true_cut_height.py':
        '998509f9463e0d377dc6dcde42ae71c62dcc0c02e77d6e1ec24bb634050a5b7c',
}
V3='warm-supported-material-phase-fixed-metric-v3'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


def write(path,value):
    temp=path.with_suffix(path.suffix+'.tmp')
    temp.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    temp.replace(path)


def interval_array(values,shape,name):
    values=np.asarray(values)
    if (values.dtype!=np.float64 or values.shape!=shape or
            not np.all(np.isfinite(values)) or np.any(values[0]>values[1])):
        raise ValueError('Invalid complete interval array: '+name)
    return values.copy()


def external_core(certificate_path,arrays_path,run_path,physical_path,run,mean,helper):
    """Bind a complete cyclic point/box oracle to exactly the same new field."""
    certificate=read(certificate_path)
    if (certificate.get('complete') is not True or
            certificate.get('kind')!='warm_true_core_external_intervals' or
            certificate.get('format_version')!=1 or
            certificate.get('model_kind')!=run['model_kind'] or
            certificate.get('modes')!=run['modes'] or
            certificate.get('mean_nodes')!=1168 or
            certificate.get('source_run_sha256')!=sha(run_path) or
            certificate.get('physical_sha256')!=sha(physical_path) or
            certificate.get('warm_definition_sha256')!=helper.canonical_sha(run['warm_definition'])):
        raise ValueError('Require this new field\'s complete true external-core certificate')
    for key in ('model_kind','modes','homotopy','warm_definition_sha256','phase_basis_family',
                'oracle','continuous_all_angle_bounds'):
        if certificate.get(key)!=mean.get(key):
            raise ValueError('Mean and external certificates differ in '+key)
    bounds=certificate.get('continuous_all_angle_bounds',{})
    core_lower=bounds.get('kappa_lower')
    if (bounds.get('positive_curvature_certified') is not True or
            not isinstance(core_lower,(int,float)) or
            not math.isfinite(core_lower) or core_lower<=0):
        raise ValueError('The true-core positive-curvature certificate is incomplete')
    source_kind=run.get('linear_source_model_kind',run['model_kind'])
    if source_kind==V3:
        for key,expected in (
                ('linear_source_model_kind',source_kind),
                ('warm_definition',run['warm_definition']),
                ('phase_basis',run['warm_definition']['phase_basis']),
                ('basis_anchor_v2_run',run['basis_anchor_v2_run']),
                ('basis_anchor_v2_sha256',run['basis_anchor_v2_sha256'])):
            if certificate.get(key)!=expected:
                raise ValueError('The complete v3 true-core family differs in '+key)
    arrays=certificate['arrays']
    if (Path(arrays['path']).resolve()!=arrays_path.resolve() or
            sha(arrays_path)!=arrays['sha256'] or
            certificate.get('interval_output_sha256')!=arrays['sha256']):
        raise ValueError('The bound external core arrays changed')
    sources=certificate.get('source_hashes')
    if not isinstance(sources,dict) or not sources:
        raise ValueError('Require actual bound external-oracle source files')
    for path,digest in sources.items():
        if sha(path)!=digest:
            raise ValueError('An external core source changed: '+path)
    count=certificate.get('nodes')
    if not isinstance(count,int) or isinstance(count,bool) or count<16:
        raise ValueError('The external array must cover a complete cyclic grid')
    result={}
    with np.load(arrays_path,allow_pickle=False) as data:
        for name in ('psi','psi_lo','psi_hi'):
            values=data[name]
            if (values.dtype!=np.float64 or values.shape!=(count,) or
                    not np.all(np.isfinite(values))):
                raise ValueError('Invalid cyclic angular coordinates: '+name)
            result[name]=values.copy()
        for name in ('theta_point','theta_box'):
            result[name]=interval_array(data[name],(2,count),name)
        for kind in ('point','box'):
            for jet in ('F','Ft','Ftt','Fttt','Ftttt'):
                name=kind+'_'+jet
                result[name]=interval_array(data[name],(2,count,3),name)
    psi,lo,hi=(result[name] for name in ('psi','psi_lo','psi_hi'))
    if (psi[0]!=0 or np.any(np.diff(psi)<=0) or
            not np.array_equal(lo,psi) or not np.array_equal(hi[:-1],psi[1:]) or
            np.any(hi<=lo)):
        raise ValueError('The external closed boxes do not cover all interpolation edges')
    mp.iv.dps=75
    period=2*mp.iv.pi
    period_low=helper.jets.m.K.dn(float(period.a))
    period_high=helper.jets.m.K.up(float(period.b))
    if not psi[-1]<period_low or hi[-1]<period_high:
        raise ValueError('The complete cyclic grid must enclose the true final endpoint 2*pi')
    # The last true endpoint has exactly the first node's value by the
    # true periodicity proved for both admitted phase families.
    return certificate,result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','source-run','physical','core-mean-certificate','core-mean-intervals',
                 'core-angle-certificate','core-angle-intervals','outdir'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--target',type=float,default=9.7e-7)
    p.add_argument('--max-attempts',type=int,default=100000)
    p.add_argument('--max-depth',type=int,default=28)
    p.add_argument('--allow-intermediate-lambda',action='store_true')
    a=p.parse_args()
    repo=a.repo.resolve();out=a.outdir.resolve()
    if out==repo or repo in out.parents:
        raise ValueError('Complete certificate leaves must remain outside the repository')
    if (not math.isfinite(a.target) or not 0<a.target<=1e-6 or
            a.max_attempts<1 or not 1<=a.max_depth<=28):
        raise ValueError('Retain the original positive metric gate and finite subdivision controls')
    out.mkdir(parents=True,exist_ok=False)
    begin=time.monotonic()
    report=dict(status='validating_actual_inputs',complete=False,stages=[],progress={},
        result={},error=None,scope=__doc__,BVP_invoked=False,DN_invoked=False,
        complete_surface=False,fixed_metric_C2_convergence_paid=False,
        original_inlet_repair_reused=False,old_numeric_bounds_reused=False)
    def save():
        report['seconds']=time.monotonic()-begin
        write(out/'summary.json',report)
    def event(name,**values):
        report['progress']=dict(event=name,**values)
        save()
        print(json.dumps(dict(event=name,seconds=time.monotonic()-begin,**values),allow_nan=False),flush=True)
    save()
    try:
        scripts=repo/'topics/visible-flex-held-10pct/scripts'
        support=scripts/'resume_m3';current=scripts/'resume_20261126'
        for name,digest in REVIEWED.items():
            if sha(scripts/name)!=digest:
                raise ValueError('A reviewed prefix algorithm or input contract changed: '+name)
        sys.path.insert(0,str(support));sys.path.insert(0,str(current))
        helper=module('_warm_continuous_prefix_contract',current/'seam_certify_true_cut_height.py')
        metric=helper.prefix_mean
        kernel=scripts/'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py'
        helper.jets.m.K=module('_warm_continuous_prefix_intervals',kernel)
        run_path=a.source_run.resolve();physical_path=a.physical.resolve()
        run,obj,model_path,gate=helper.source_model(run_path,a.allow_intermediate_lambda)
        if sha(physical_path)!=run['physical_sha256']:
            raise ValueError('The actual physical field changed')
        mean,psi,lift=helper.core_intervals(a.core_mean_certificate,a.core_mean_intervals,
                                           run_path,physical_path,run)
        angles,external=external_core(a.core_angle_certificate,a.core_angle_intervals,
                                      run_path,physical_path,run,mean,helper)
        physical_loader=module('_warm_continuous_prefix_physical',support/'audit_full_relative_metric.py')
        physical=physical_loader.load_physical(physical_path)
        M=run['modes'];dimension=3*M+1
        if (physical.sol.c.shape!=(6,len(physical.x)-1,dimension) or
                physical.p.shape!=(M,) or not np.all(np.diff(physical.x)>0) or
                not all(np.all(np.isfinite(x)) for x in (physical.x,physical.sol.c,physical.p))):
            raise ValueError('Invalid full actual m3 quintic representation')
        pieces=helper.M3PrefixPieces(obj,physical)
        if not np.isfinite(pieces.f.warp_e) or abs(float(pieces.f.warp_e))>=1:
            raise ValueError('External material-angle boxes require finite abs(warp_e)<1')
        if (pieces.xx[0]!=0 or pieces.xx[-1]!=pieces.end or pieces.grid[0]!=0 or
                pieces.grid[-1]!=pieces.entry or not 0<pieces.entry<pieces.end):
            raise ValueError('The actual source or complete prefix domain changed')
        if not np.array_equal(np.asarray(pieces.f.exact_lift_initial,float),lift['exact_lift_initial']):
            raise ValueError('Core mean arrays subtracted a different complete projection')
        endpoints=pieces.exact_endpoint_report()
        pieces.field_coefficients_exact.clear()
        pieces.field_right_targets_exact.clear()
        gc.collect()
        with np.load(a.core_mean_intervals,allow_pickle=False) as values:
            lift['H']=interval_array(values['H'],(2,1168,3),'H')
        mt=metric.AngleTable(psi,psi,pieces.frequencies)
        mt.load_mean_lift(lift)
        pt=metric.AngleTable(external['psi'],external['psi'],pieces.frequencies)
        bt=metric.AngleTable(external['psi_lo'],external['psi_hi'],pieces.frequencies)
        pt.build_lift(external,pieces.f,'point',pieces.q)
        bt.build_lift(external,pieces.f,'box',pieces.q)
        step=float(np.max((metric.I(bt.hi)-metric.I(bt.lo)).x[1]))
        verifier=metric.PrefixMetric(pieces,mt,pt,bt,step)
        sources=[Path(__file__),model_path,support/'audit_full_relative_metric.py',
                 support/'certify_bridge_metric_fourier_taylor.py',
                 support/'certify_r59_shared_jet_transfer.py',*[scripts/name for name in REVIEWED]]
        source_hashes={str(path.resolve()):sha(path) for path in sources}
        grid_file=out/'radial-grid.json'
        write(grid_file,dict(radial_breakpoints_exact=[str(x) for x in pieces.grid],
                            prefix_end_exact=str(pieces.entry),cut_s_exact=str(pieces.end)))
        report.update(status='covering_continuous_prefix',model_kind=run['model_kind'],
            source_acceptance=gate,source_run=helper.ref(run_path),physical=helper.ref(physical_path),
            modes=M,field_dimension=dimension,mean_nodes=1168,literal_psi_sha256=helper.PSI_SHA,
            angular_nodes=pt.N,angular_step_upper=step,target=a.target,
            target_metric='ds^2+a_star(s)^2*dtheta^2 on this once-frozen endpoint-normalized prefix',
            warm_definition=run['warm_definition'],warm_definition_sha256=helper.canonical_sha(run['warm_definition']),
            homotopy=run['warm_definition']['homotopy'],
            core_mean_certificate=helper.ref(a.core_mean_certificate),
            core_angle_certificate=helper.ref(a.core_angle_certificate),
            core_mean_intervals=helper.ref(a.core_mean_intervals),
            core_angle_intervals=helper.ref(a.core_angle_intervals),
            actual_state_frequencies=pieces.frequencies.tolist(),
            phase_basis=run['warm_definition'].get('phase_basis',dict(family='full_period_sine_v1',frequency='3*j')),
            source_hashes=source_hashes,exact_endpoint_algebra=endpoints,
            radial_grid=helper.ref(grid_file),radial_initial_cells=len(pieces.grid)-1,
            prefix_end_exact=str(pieces.entry),cut_s_exact=str(pieces.end),
            exact_lift_initial_sha256=mean['exact_lift_initial_sha256'],
            explicit_common_right_two_jet_map=True,source_float_map_identified_with_explicit_C2_map=False,
            metric_transfer_to_any_different_target_certified=False,
            mathematical_mean_rule='Literal mean1168; true common primitive anchored at Z(0)=0',
            accepted=0,attempts=0,splits=0,domain_splits=0,peak=0.,root_lower=None,
            angular_second_upper=0.,principal_curvature_upper=0.,curvature_unresolved_cells=0)
        event('continuous_prefix_inputs_bound',modes=M,radial_initial_cells=len(pieces.grid)-1,
              angular_nodes=pt.N,source_acceptance_kind=gate['acceptance_kind'])
        todo=[(l,r,0) for l,r in zip(pieces.grid[:-1],pieces.grid[1:])][::-1]
        covered=Q(0);failure=None;last_event=time.monotonic()
        leaves=out/'continuous-prefix-metric-leaves.jsonl.gz'
        with gzip.open(leaves,'wt') as stream:
            while todo:
                left,right,depth=todo.pop()
                if report['attempts']>=a.max_attempts:
                    failure=dict(left_exact=str(left),right_exact=str(right),depth=depth,
                                 reason='Declared absolute radial-box attempt budget reached')
                    break
                report['attempts']+=1
                try:
                    bound,meta=verifier.enclose(left,right)
                    if not math.isfinite(bound) or bound<0:
                        raise ArithmeticError('Invalid metric operator upper bound')
                    reason='Continuous metric bound exceeds the original target'
                except (ValueError,ArithmeticError,FloatingPointError) as error:
                    bound=math.inf;meta=None;reason=str(error)
                    report['domain_splits']+=1
                if bound>a.target:
                    if depth>=a.max_depth or report['attempts']>=a.max_attempts:
                        failure=dict(left_exact=str(left),right_exact=str(right),depth=depth,
                            reason=reason,last_bound=bound if math.isfinite(bound) else None,
                            last_components=meta)
                        break
                    middle=(left+right)/2
                    todo.extend([(middle,right,depth+1),(left,middle,depth+1)])
                    report['splits']+=1
                else:
                    curvature=None;curvature_error=None
                    try:
                        curvature=verifier.curvature(bound)
                        if not math.isfinite(curvature) or curvature<0:
                            raise ArithmeticError('Invalid continuous principal-curvature upper bound')
                    except (ValueError,ArithmeticError,FloatingPointError) as error:
                        curvature_error=str(error);curvature=None
                        report['curvature_unresolved_cells']+=1
                    if curvature is not None and curvature>report['principal_curvature_upper']:
                        report.update(principal_curvature_upper=curvature,
                                      curvature_peak_interval_exact=[str(left),str(right)])
                    report['accepted']+=1;covered+=right-left
                    if bound>report['peak']:
                        report.update(peak=bound,peak_interval_exact=[str(left),str(right)],peak_components=meta)
                    root=meta['fixed_mean_root']
                    if not math.isfinite(root) or root<=0:
                        raise ArithmeticError('The complete fixed-mean Frenet domain was not proved')
                    report['root_lower']=root if report['root_lower'] is None else min(root,report['root_lower'])
                    report['angular_second_upper']=max(report['angular_second_upper'],meta['angular_second'])
                    stream.write(json.dumps(dict(left_exact=str(left),right_exact=str(right),depth=depth,
                        metric_operator_upper=bound,components=meta,principal_curvature_upper=curvature,
                        curvature_unresolved_reason=curvature_error),separators=(',',':'),allow_nan=False)+'\n')
                if report['attempts']%50==0 or time.monotonic()-last_event>=40:
                    event('continuous_prefix_progress',accepted=report['accepted'],attempts=report['attempts'],
                          splits=report['splits'],remaining=len(todo),s=float(right),peak=report['peak'])
                    last_event=time.monotonic()
        report['leaves']=helper.ref(leaves)
        report['covered_radial_length_exact']=str(covered)
        if failure is not None:
            report.update(status='continuous_prefix_not_certified',unresolved=failure,
                          remaining=len(todo)+1)
            report['result']=dict(continuous_prefix_metric_certified=False,partial_metric_peak=report['peak'])
            event('continuous_prefix_not_certified',accepted=report['accepted'],attempts=report['attempts'])
            return 1
        if covered!=pieces.entry or report['accepted']<1 or report['root_lower'] is None:
            raise ArithmeticError('Accepted radial leaves do not cover the complete exact prefix')
        # This names only the proved prefix component and never promotes it
        # to a seam, patched inlet, tail, reach or convergence certificate.
        report.update(status='explicit_C2_warm_prefix_continuous_metric_certified',complete=True)
        report['result']=dict(continuous_prefix_metric_certified=True,
            metric_operator_upper=report['peak'],metric_target=a.target,
            continuous_prefix_curvature_certified=report['curvature_unresolved_cells']==0,
            principal_curvature_upper=(report['principal_curvature_upper']
                                      if report['curvature_unresolved_cells']==0 else None),
            covered_radial_length_exact=str(covered),accepted_radial_cells=report['accepted'],
            mean_nodes=1168,angular_nodes=pt.N,modes=M,
            complete_surface=False,fixed_metric_C2_convergence_paid=False)
        event('continuous_prefix_metric_certified',metric_operator_upper=report['peak'],
              curvature_unresolved_cells=report['curvature_unresolved_cells'])
        return 0
    except Exception as error:
        report.update(status='error',complete=False,error=repr(error),traceback=traceback.format_exc())
        event('error',error=repr(error))
        return 1
    finally:
        save()


if __name__=='__main__':
    raise SystemExit(main())
