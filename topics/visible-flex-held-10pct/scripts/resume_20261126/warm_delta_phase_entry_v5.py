#!/usr/bin/env python3
"""Retain one actual R53 design field in the v5 zero-phase coordinates.

No solver runs here.  Original raw p0, base physical profile, chart, mean
rule and physical interpolant are retained.  Literal identities and actual
original finite gates are recomputed before an initial representation is
accepted; its solver flags remain null and source provenance stays separate.
The d1=0 slice is only for choosing a metric during design.  After a genuine
full-H return, fixed-metric refinement may release d1 in the same complete
R70 family.  Neither that nonlinear return nor its refinement runs here.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback
from types import SimpleNamespace
import numpy as np
import scipy.integrate._bvp as bvp
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import warm_delta_phase_factory_v5 as factory_module
KIND = factory_module.KIND
REEXPRESSION = 'same_cartesian_map_verified_reexpression'
SOLVER_RETURN = 'actual_original_portable_solver_return'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def json_value(value):
    # Failed finite diagnostics must not erase their own failure record.
    if isinstance(value, np.generic):
        value = value.item()
    if isinstance(value, float) and not math.isfinite(value):
        return 'nonfinite:'+repr(value)
    if isinstance(value, dict):
        return {str(k):json_value(v) for k,v in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_value(v) for v in value]
    if isinstance(value, np.ndarray):
        return json_value(value.tolist())
    return value


def write(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(json_value(value), indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def finite(value, upper=math.inf):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and 0 <= value <= upper)


def option(record, flag):
    command = record.get('geometry_command', record['command'])
    if command.count(flag) != 1:
        raise ValueError('Require one actual command option: '+flag)
    return command[command.index(flag)+1]


def replace_option(command, flag, value):
    if flag in command:
        command[command.index(flag)+1] = str(value)
    else:
        command.extend((flag, str(value)))


def raw_command(record, raw, provider, config, out):
    """Copy the actual solver driver, including verbose and original guards."""
    command = list(record.get('geometry_command', record['command']))
    command[0] = sys.executable
    for flag in ('--restart-checkpoint', '--control-record'):
        if flag in command:
            index = command.index(flag)
            del command[index:index+2]
    if any(flag in command for flag in ('--skip-audit', '--probe-only', '--tail-config')):
        raise ValueError('Require the original full-audit linear-port command')
    for flag, value in (('--raw-restart',raw), ('--core-module',provider),
                        ('--core-config',config), ('--outdir',out)):
        replace_option(command, flag, value)
    return command


def verify_bindings(record):
    for group in ('source_hashes', 'inputs'):
        if not record.get(group):
            raise ValueError('Missing original complete source/input binding: '+group)
        for path, expected in record[group].items():
            if sha(path) != expected:
                raise ValueError('Changed actual source/input: '+path)


def artifact_data(path, record):
    path = Path(path).resolve()
    raw_path = path.parent/record['raw_return']['file']
    physical_path = path.parent/'physical.npz'
    if (sha(raw_path) != record['raw_return']['sha256'] or
            sha(physical_path) != record['physical_sha256']):
        raise ValueError('Complete raw/physical artifact SHA differs')
    with np.load(raw_path, allow_pickle=False) as data:
        raw = {k:data[k].copy() for k in data.files}
    with np.load(physical_path, allow_pickle=False) as data:
        physical = {k:data[k].copy() for k in data.files}
    for required in ('x', 'y', 'p', 'pscale', 'cubic_c', 'cubic_x', 'rms'):
        if required not in raw:
            raise ValueError('Incomplete actual raw return: '+required)
    M = int(record['modes']); n = 3*M+1
    x, y, p = (raw[k] for k in ('x','y','p'))
    if (x.ndim != 1 or len(x)<2 or np.any(np.diff(x)<=0) or
            y.shape != (n,len(x)) or p.shape != (M,) or
            raw['pscale'].shape != (M-1,) or
            not np.array_equal(raw['cubic_x'], x) or
            raw['cubic_c'].shape != (4,len(x)-1,n) or
            raw['rms'].shape != (len(x)-1,) or
            physical['p'].shape != (M,) or
            not np.array_equal(physical['p'],p) or
            physical['x'].shape != x.shape or
            np.any(np.diff(physical['x'])<=0) or
            physical['c'].shape != (6,len(x)-1,n)):
        raise ValueError('Complete actual raw/physical dimensions differ')
    if not all(np.all(np.isfinite(a)) for a in (*raw.values(),*physical.values())):
        raise FloatingPointError('Nonfinite actual raw/physical arrays')
    expected = np.maximum(float(record['gauge_q'])**np.arange(2,M+1),1e-9)
    if (not np.array_equal(raw['pscale'],expected) or
            not np.array_equal(raw['pscale'],record['parameter_scales']) or
            not np.array_equal(p,record['raw_return']['parameters']) or
            np.any(raw['rms']<0) or
            float(np.max(raw['rms'])) != record['raw_return']['rms'] or
            record['raw_return'].get('nodes') != len(x)):
        raise ValueError('Actual raw parameters/scales/RMS metadata differ')
    frozen = dict(record['physical_profile'],
                  delta=record['physical_profile']['delta']+float(p[0]))
    if frozen != record['frozen_profile']:
        raise ValueError('Original base delta plus actual raw p0 differs')
    return raw, physical


def gate_checks(record):
    gates = record.get('gates') or {}; raw = record.get('raw_return') or {}
    audit = record.get('prefix_audit') or {}
    tolerances = all(finite(gates.get(k), cap) and gates[k]>0 for k,cap in
        (('tol',1e-6), ('bc_tol',1e-7), ('physical_bc_tol',2e-9)))
    rms = tolerances and finite(raw.get('rms'),gates['tol'])
    physical = tolerances and finite(audit.get('physical_bc_max'),gates['physical_bc_tol'])
    N = audit.get('samples_psi'); M = record.get('modes')
    angular = (isinstance(M,int) and M>0 and isinstance(N,int)
               and N>=16*(3*M+1))
    metric = angular and finite(audit.get('metric_l1'),1e-6)
    solver = (record.get('solver_success') is True and raw.get('success') is True
              and raw.get('status') == 0 and not record.get('error'))
    return dict(tolerances=bool(tolerances),rms=bool(rms),physical_bc=bool(physical),
        angular_floor=bool(angular),metric=bool(metric),actual_solver=bool(solver),
        solver_and_boundary_pass=bool(tolerances and rms and physical and angular and solver))


def actual_input(path, *, require_metric=True):
    record = load(path)
    if (record.get('actual_tail_requested') or record.get('original_actual_nonlinear_tail') or
            record.get('fixed_metric') or
            record.get('fixed_metric_refinement')):
        raise ValueError('Require original fixed=False linear-DN design semantics')
    checks = gate_checks(record)
    if not checks['solver_and_boundary_pass'] or (require_metric and not checks['metric']):
        raise ValueError('The actual original finite solver/boundary/metric gates failed')
    verify_bindings(record)
    artifact_data(path,record)
    return record


def accepted_input(path):
    """Explicitly distinguish a verified representation from a new solve."""
    record = load(path)
    if (record.get('model_kind') != KIND or record.get('fixed_metric') is not False or
            record.get('fixed_metric_refinement') is not False or
            record.get('finite_linear_candidate_pass') is not True or
            record.get('error')):
        raise ValueError('This is not an accepted v5 design representation/return')
    settings = record['core_settings']
    factory_module.checked_provider(settings)
    if (settings.get('model_kind') != KIND or
            settings.get('phase_parameter_scale_rule') != factory_module.SCALE_RULE or
            settings.get('fixed_metric') is not False):
        raise ValueError('The v5 physical parameter semantics differ')
    if load(option(record,'--core-config')) != settings:
        raise ValueError('The bound v5 settings file changed')
    if Path(option(record,'--core-module')).resolve() != Path(__file__).with_name(
            'warm_delta_phase_factory_v5.py').resolve():
        raise ValueError('The bound v5 provider differs')
    verify_bindings(record)
    raw, physical = artifact_data(path,record)
    checks = gate_checks(record)
    if record.get('acceptance_kind') == REEXPRESSION:
        identity = record.get('zero_control_identity') or {}
        original = Path(record['origin_design_run'])
        if (record.get('solver_invoked') is not False or record.get('solver_success') is not None or
                record['raw_return'].get('success') is not None or
                record['raw_return'].get('status') is not None or
                identity.get('all_required_exact_equalities') is not True or
                not identity or not all(v is True for v in identity.values()) or
                not np.all(raw['p'][1:]==0) or
                sha(original)!=record['origin_design_sha256'] or
                not finite(record.get('original_scaled_bc_max'),record['gates']['bc_tol']) or
                not all(checks[k] for k in ('tolerances','rms','physical_bc','angular_floor','metric'))):
            raise ValueError('The honest same-map reexpression contract failed')
        actual_input(original)
    elif record.get('acceptance_kind') == SOLVER_RETURN:
        if record.get('solver_invoked') is not True:
            raise ValueError('A new accepted solve must be an actual invoked solver')
        actual_input(path)
    else:
        raise ValueError('Unknown v5 acceptance identity')
    return record


def measure(obj,x,y,p):
    h=np.diff(x)
    cr,ym,f,fm=bvp.collocation_fun(obj.fun,y,p,x,h)
    spline=bvp.create_spline(y,f,x,h)
    rms=bvp.estimate_rms_residuals(obj.fun,spline,x,h,p,1.5*cr/h,fm)
    bc=obj.bc(y[:,0],y[:,-1],p)
    physical_bc=obj.terminal(y[:,-1],p)*obj.bcweights
    if not all(np.all(np.isfinite(v)) for v in (cr,f,fm,rms,bc,physical_bc)):
        raise FloatingPointError('Nonfinite actual raw-equation audit')
    return dict(cr=cr,f=f,fm=fm,rms=rms,bc=bc,physical_bc=physical_bc)


def inspect_transfer(repo,source_path,transfer_path,report_path):
    """Inspect actual core.controls; this is NOT an initializer acceptance gate."""
    source=actual_input(source_path,require_metric=False)
    if source.get('model_kind')!=KIND or source.get('acceptance_kind')!=SOLVER_RETURN:
        raise ValueError('A real v5 solver return must precede original mode transfer')
    factory_module.checked_provider(source['core_settings'])
    raw0,_=artifact_data(source_path,source)
    transfer=load(transfer_path);result=transfer['result']
    raw_path=Path(result['initial_raw'])
    if (sha(raw_path)!=result['initial_raw_sha256'] or
            transfer['source_run_sha256']!=sha(source_path) or
            transfer['exact_lift_coefficient']!=1):
        raise ValueError('The original complete nodal lift binding differs')
    with np.load(raw_path,allow_pickle=False) as data:
        values={k:data[k].copy() for k in data.files}
    M0=int(source['modes']);M=int(result['modes'])
    p1,scales1=values['p'],values['pscale']
    expected=np.maximum(float(source['gauge_q'])**np.arange(2,M+1),1e-9)
    if (M<=M0 or p1.shape!=(M,) or values['y'].shape!=(3*M+1,len(raw0['x'])) or
            not all(np.all(np.isfinite(v)) for v in values.values()) or
            not np.array_equal(values['x'],raw0['x']) or
            p1[0]!=raw0['p'][0] or not np.array_equal(scales1,expected) or
            not np.array_equal(scales1[:M0-1],raw0['pscale']) or
            not np.all(p1[M0:]==0.)):
        raise ValueError('The original nodal lift changed its declared dimensions/scales/p0/zero extension')
    loader=module('_v5_transfer_geometry',Path(repo)/
        'topics/visible-flex-held-10pct/scripts/resume_m3/actual_m3_metric_model.py')
    obj=loader.load_model(dict(source_run=str(Path(source_path).resolve())))
    obj.initial(raw0['p']);core0=obj._core
    core1=type(core0)(obj.q,p1[1:]*scales1,3)
    if (core1.baseline is not core0.baseline or
            not np.array_equal(core1.baseline.original.coefficients,
                               source['core_settings']['anchor_support_coefficients']) or
            core1.homotopy!=source['core_settings']['homotopy'] or
            not np.all(core1.controls[M0:]==0.)):
        raise ValueError('The complete fixed anchor/family/zero extension changed')
    delta=core1.controls[:M0]-core0.controls
    arrays=Path(report_path).with_suffix('.npz')
    np.savez_compressed(arrays,old_actual_phase=core0.controls,new_actual_phase=core1.controls)
    value=dict(status='unaccepted_nodal_initializer_inspected',
        source_run_sha256=sha(source_path),transfer_json_sha256=sha(transfer_path),
        initial_raw_sha256=sha(raw_path),actual_phase_arrays_sha256=sha(arrays),
        actual_phase_arrays=str(arrays.resolve()),
        common_phase_bitwise_equal=bool(np.array_equal(core1.controls[:M0],core0.controls)),
        actual_phase_difference_linf=float(np.max(abs(delta))),
        actual_phase_difference_l1=float(np.sum(abs(delta))),
        new_phase_columns_zero=True,original_p0_preserved=True,
        baseline_and_phase_settings_unchanged=True,exact_lift_coefficient=1,
        same_cartesian_map_claimed=False,accepted_bvp=False,
        scope='Actual core.controls read from the same provider. Floating roundtrip is recorded, not a new stopping gate. The original complete-lift test and next genuine BVP gates remain required.')
    write(report_path,value)
    print(json.dumps(value,allow_nan=False),flush=True)
    return 0


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','source-run'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--outdir',type=Path)
    parser.add_argument('--inspect-transfer',type=Path)
    parser.add_argument('--out-report',type=Path)
    parser.add_argument('--phase-scale',type=float,default=1.)
    args=parser.parse_args()
    if args.inspect_transfer:
        if args.out_report is None or args.outdir is not None:
            raise ValueError('Transfer inspection takes --out-report and no --outdir')
        return inspect_transfer(args.repo,args.source_run,args.inspect_transfer,args.out_report)
    if args.outdir is None or args.out_report is not None:
        raise ValueError('Zero-control reexpression requires --outdir')
    repo=args.repo.resolve(); source_path=args.source_run.resolve(); out=args.outdir.resolve()
    if repo==out or repo in out.parents:
        raise ValueError('Generated fields must remain outside the repository')
    if not math.isfinite(args.phase_scale) or args.phase_scale<=0:
        raise ValueError('Positive finite phase scale required')
    out.mkdir(parents=True,exist_ok=False)
    scripts=repo/'topics/visible-flex-held-10pct/scripts'
    resume=scripts/'resume_m3'; public=scripts/'resume_20261126'
    begin=time.monotonic()
    record=dict(scope=__doc__,command=[sys.executable,*sys.argv],model_kind=KIND,
        status='preparing',solver_invoked=False,solver_success=None,
        acceptance_kind=REEXPRESSION,finite_linear_candidate_pass=False,
        fixed_metric=False,fixed_metric_refinement=False,actual_tail_requested=False,
        parameter_zero_meaning=factory_module.SCALE_RULE['parameter_zero'],
        terminal_kind='original_linear_dn',complete_surface=False)
    def save():
        record['elapsed']=time.monotonic()-begin
        write(out/'run.json',record)
        write(out/'summary.json',dict(status=record['status'],stages=[],
            progress=record.get('progress'),error=record.get('error'),result=dict(
                run=str(out/'run.json'),run_sha256=sha(out/'run.json'),
                solver_invoked=False,solver_success=None,acceptance_kind=REEXPRESSION,
                finite_linear_candidate_pass=record['finite_linear_candidate_pass'],
                homotopy=(record.get('core_settings') or {}).get('homotopy'),
                modes=record.get('modes'),raw_return={k:v for k,v in
                    (record.get('raw_return') or {}).items() if k in
                    ('file','sha256','success','status','nodes','rms','solver_invoked','message')},
                zero_control_identity=record.get('zero_control_identity'),
                metric=(record.get('prefix_audit') or {}).get('metric_l1'))))
    def event(name,**values):
        record['progress']=dict(event=name,**values);save()
        print(json.dumps(json_value(dict(event=name,**values)),allow_nan=False),flush=True)
    try:
        source=actual_input(source_path)
        if source.get('model_kind') or not source.get('core_settings'):
            raise ValueError('Supply the actual original R53 design run, not a warm conversion')
        settings0=source['core_settings']
        if settings0.get('curvature_blend')!=1. or not 0<float(settings0['homotopy'])<=1:
            raise ValueError('A positive-lambda complete original R53 baseline is required')
        if source['gates']['physical_bc_tol']/source['gates']['bc_tol']!=.02:
            raise ValueError('Original boundary normalization changed')
        raw,physical=artifact_data(source_path,source)
        x,y,pold=(raw[k] for k in ('x','y','p'))
        loader=module('_v5_original_geometry_loader',resume/'actual_m3_metric_model.py')
        old=loader.load_model(dict(source_run=str(source_path)))
        old_initial=old.initial(pold).copy();baseline=old._core
        oldflow=old.flow(pold[0]);reference=type(baseline.original)
        if not hasattr(reference,'normal_geometry'):
            raise ValueError('The actual original support reference is required')
        provider_path=HERE/'warm_delta_phase_factory_v5.py'
        files=dict(v5_factory=provider_path,
            v4_factory=public/'warm_homotopy_core_factory_v4.py',
            common_geometry=public/'warm_supported_core_factory.py',
            material_geometry=scripts/'resume_transfer/material_flattened_support_core.py')
        settings=dict(model_kind=KIND,fixed_metric=False,gauge_q=float(old.q),
            phase_control_scale=args.phase_scale,
            phase_parameter_scale_rule=copy.deepcopy(factory_module.SCALE_RULE),
            anchor_support_coefficients=baseline.original.coefficients.tolist(),
            anchor_core_settings=copy.deepcopy(settings0),homotopy=float(baseline.homotopy),
            anchor_run=str(source_path),anchor_run_sha256=sha(source_path),
            implementation_sources={k:dict(path=str(v.resolve()),sha256=sha(v)) for k,v in files.items()})
        v4=module('_v5_formula_definition',files['v4_factory'])
        settings['phase_basis']=copy.deepcopy(v4.BASIS_RULE)
        config=out/'core-config.json';write(config,settings)
        factory=factory_module.make_factory(settings,reference_class=reference,anchor_baseline=baseline)
        __import__('fixed_metric_mode3_core').PlanarSupportCore=factory
        __import__('fixed_metric_mode3_bvp').PlanarSupportCore=factory
        coupler=sys.modules['_metric_coupler']
        Flow,Base=coupler.adaptive.build_classes(copy.deepcopy(source['angular_chart']))
        sys.path.insert(0,str(resume/'round_raw_lib'))
        from exact_core_lift import install_core_lift
        Base=install_core_lift(Flow,Base)
        import analytic_adaptive_core_jac as analytic
        analytic.parameter_jets=lambda core,theta:core.jet_parameter_derivatives(theta)
        analytic.install(Base)
        obj=Base(copy.deepcopy(source['physical_profile']),copy.deepcopy(old.port),
                 old.q,old.M,old.nt,False,float(source['warp_reference']))
        obj.bcweights=old.bcweights.copy()
        p=pold.copy();p[1:]=0.
        new_initial=obj.initial(p).copy();flow=obj.flow(p[0])
        N=int(source['prefix_audit']['samples_psi'])
        theta=2*np.pi*np.arange(N)/N
        identity=dict(literal_baseline_object=obj._core.baseline is baseline,
            zero_phase_controls=bool(np.all(obj._core.controls==0.)),
            original_raw_p0_preserved=bool(p[0]==pold[0]),
            original_base_profile_preserved=obj.cfg==old.cfg,
            original_actual_profile_preserved=source['frozen_profile']==dict(obj.cfg,delta=obj.cfg['delta']+float(p[0])),
            same_gauge=bool(obj.q==old.q),same_modes=bool(obj.M==old.M),
            same_angular_projection=bool(obj.nt==old.nt),
            same_parameter_scales=bool(np.array_equal(obj.pscale,old.pscale)),
            initial_projection_bitwise_equal=bool(np.array_equal(old_initial,new_initial)),
            same_basis=bool(np.array_equal(oldflow.B,flow.B)),
            same_chart_join=bool(obj.chart_join==old.chart_join),
            same_chart_reference_prefix=bool(obj.chart_reference_prefix==old.chart_reference_prefix),
            same_chart_breaks=bool(np.array_equal(obj.chart_breaks,old.chart_breaks)),
            same_prefix_end=bool(flow.prefix_end==oldflow.prefix_end),
            same_physical_end=bool(flow.end==oldflow.end),
            same_mean_nodes=bool(N==source['prefix_audit']['samples_psi']))
        before,after=baseline.evaluate(theta),obj._core.evaluate(theta)
        for key in ('F','Ft','Ftt'):
            identity['core_'+key+'_bitwise_equal']=bool(np.array_equal(before[key],after[key]))
        first,second=measure(old,x,y,pold),measure(obj,x,y,p)
        for key in ('f','fm','cr','rms','bc','physical_bc'):
            identity[key+'_bitwise_equal']=bool(np.array_equal(first[key],second[key]))
        h=np.diff(x);middle=x[:-1]+h/2;offset=h/2*np.sqrt(3/7)
        points=np.r_[x,middle,middle+offset,middle-offset]
        oldchart,newchart=old.chart(points,pold[0]),obj.chart(points,p[0])
        identity['RMS_chart_s_bitwise_equal']=bool(np.array_equal(oldchart[0],newchart[0]))
        identity['RMS_chart_ds_bitwise_equal']=bool(np.array_equal(oldchart[1],newchart[1]))
        pp=PPoly.construct_fast(physical['c'],physical['x'],extrapolate=False,axis=1)
        sol0=SimpleNamespace(x=physical['x'],y=y,p=pold,sol=pp)
        sol1=SimpleNamespace(x=physical['x'],y=y,p=p,sol=pp)
        compare=module('_v5_complete_six_jets',public/'warm_fixed_m3_compare_c2.py')
        sample=np.linspace(physical['x'][0],physical['x'][-1],7)
        jets0=compare.complete_jets(old,oldflow,sol0,sample,N,N,np.zeros(len(sample)))
        jets1=compare.complete_jets(obj,flow,sol1,sample,N,N,np.zeros(len(sample)))
        for key in compare.JETS:
            identity['complete_'+key+'_bitwise_equal']=bool(np.array_equal(jets0[key],jets1[key]))
        record['zero_control_identity']=identity
        if not all(identity.values()):
            raise ValueError('A literal zero-control full-map/raw-equation identity failed')
        rms=float(np.max(second['rms']));bc=float(np.max(abs(second['bc'])))
        physical_bc=float(np.max(abs(second['physical_bc'])))
        gates=copy.deepcopy(source['gates'])
        if not (finite(rms,gates['tol']) and finite(bc,gates['bc_tol']) and
                finite(physical_bc,gates['physical_bc_tol'])):
            raise ValueError('Recomputed original raw RMS/BC gates failed')
        raw.update(p=p,pscale=obj.pscale,rms=second['rms'])
        raw_file=out/'reexpressed-raw.npz';np.savez_compressed(raw_file,**raw)
        physical['p']=p;np.savez_compressed(out/'physical.npz',**physical)
        geometry_command=raw_command(source,raw_file,provider_path,config,out)
        record.update(origin_design_run=str(source_path),origin_design_sha256=sha(source_path),
            source_solver_provenance=dict(run=str(source_path),run_sha256=sha(source_path),
                raw_sha256=source['raw_return']['sha256'],physical_sha256=source['physical_sha256'],
                solver_success=True,raw_success=True,raw_status=source['raw_return']['status'],
                scope='Only this original source actually ran a solver'),
            geometry_command=geometry_command,geometry_command_not_executed=True,
            core_settings=settings,physical_profile=copy.deepcopy(source['physical_profile']),
            frozen_profile=copy.deepcopy(source['frozen_profile']),
            physical_tail_parameters=copy.deepcopy(source['physical_tail_parameters']),
            physical_tail_cut=copy.deepcopy(source['physical_tail_cut']),
            angular_chart=copy.deepcopy(source['angular_chart']),gauge_q=float(old.q),
            warp_reference=source['warp_reference'],modes=old.M,angular=old.nt,gates=gates,
            parameter_scales=obj.pscale.tolist(),mean_nodes=N,
            original_scaled_bc_max=bc,physical_sha256=sha(out/'physical.npz'),
            raw_return=dict(file=raw_file.name,sha256=sha(raw_file),success=None,status=None,
                solver_invoked=False,nodes=len(x),rms=rms,parameters=p.tolist(),
                message='No solver invoked: the actual source field was verified in new control coordinates'),
            fixed_mean_primitive=dict(nodes=N,origin=0.,resampled=False,
                definition='The source literal-node frame.Vz mean primitive; common height primitive cancels in the six-jet comparison'),
            source_hashes={**source['source_hashes'],str(Path(__file__).resolve()):sha(__file__),
                str(resume/'actual_m3_metric_model.py'):sha(resume/'actual_m3_metric_model.py'),
                str(public/'warm_fixed_m3_compare_c2.py'):sha(public/'warm_fixed_m3_compare_c2.py')},
            inputs={**source['inputs'],str(provider_path):sha(provider_path),str(config):sha(config),
                    str(source_path):sha(source_path),str(raw_file):sha(raw_file)})
        event('literal_raw_and_six_jet_identities_verified',rms=rms,scaled_bc=bc,physical_bc=physical_bc)
        # One genuine audit of the identical map with the exact original mean
        # nodes. Its metric scalar must equal the source's recorded audit.
        audit=coupler.adaptive.audit(obj,sol1,N)
        identity['original_metric_bitwise_equal']=bool(audit['metric_l1']==source['prefix_audit']['metric_l1'])
        identity['original_metric_mean_nodes_equal']=bool(audit['samples_psi']==N)
        identity['all_required_exact_equalities']=all(identity.values())
        record['prefix_audit']=audit
        passed=bool(identity['all_required_exact_equalities'] and finite(audit['metric_l1'],1e-6)
                    and finite(audit['physical_bc_max'],gates['physical_bc_tol']))
        record.update(status='verified_zero_control_reexpression',finite_linear_candidate_pass=passed)
        event('actual_original_metric_audit_complete',metric=audit['metric_l1'],accepted_representation=passed)
        if passed:
            accepted_input(out/'run.json')
        return 0 if passed else 2
    except Exception as error:
        record.update(status='reexpression_error',error=repr(error),traceback=traceback.format_exc())
        event('error',error=repr(error))
        return 1
    finally:
        save()


if __name__=='__main__':
    sys.exit(main())
