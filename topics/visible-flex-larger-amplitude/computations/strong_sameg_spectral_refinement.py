#!/usr/bin/env python3
"""Same-physical-metric spectral refinement of an accepted fixed actual view.

This entry does not re-solve the accepted M24 design. It requires the genuine
27-to-24 fixed-view report, embeds its complete numerical-coordinate raw field
in M28 without interpolation or inlet correction, and runs the existing
Fixed/Actual outer algorithm. Its old M24 tail is only a geometric warm guess;
all new complete-H, Jacobian, RMS, physical BC and audit gates remain.

Only Python loading, exact warm storage and an explicit Node resource option
are added. No MJS source is changed, no old-M response is a new-M response, and
the embedded raw cubic is not itself an accepted C2 surface.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import copy
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import time
from types import SimpleNamespace

HERE=Path(__file__).resolve().parent
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
EXPECTED_SOURCE_SHA256={
    "root_actual_frozen_neck.py": "50acde6b243f964ba03c9e1916a25ec80fbec7ef72b1d17ea3fb5ee2f86fcfe1",
    "root_actual_fixed_refinement.py": "aac9619f0c54e3bc5dcca2270734d484c858eee1efba7ca78209679372821816",
    "root_actual_bounded_neck.py": "d34bb67dae8e0087607f020102f92ba55b5258e58cab48e226ba7c5b15983734",
    "root_actual_neck_bvp.py": "03bd353875b4a7ca248c938887b706ce6e2d3115e9b82f2cf772ccc4b5ce98b7",
    "root_dual_core_bvp.py": "85c057132c34694558360af857c9686b3ce7be7c31861ae6a3b6e6313184d652",
    "geometric-fixed-dual-prefix.py": "f189c8f94880ff5455a140a686219a1805399e1d45a3809e176630bb92772280",
    "root_raw_collocation.py": "e2378a1c7ee11bd9a4f90b0a46d05d550f9e97a0883dda327a5edc09593eda3f",
    "strong_disk_actual_backend.py": "402830e66390f660d7f8e846165a2ae7c1e9858addc2317df06348dc1e8634f1",
    "tail_frozen_client.py": "fe14e590f56fc43b1d87eb976377cbd1ec6db1c85ce680c264f18afada687e69",
    "strong_tail_constructor_guard.py": "6f51a896e44aff8aa8a2f66a71320b68f15d279ec2a8e2ee0e3093cedf0696a3"
}
IO_KEYS={'traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint'}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    path=Path(path)
    data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)


def atomic_new_or_same(path,value):
    path=Path(path)
    data=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    if path.exists():
        if path.read_bytes()!=data:
            raise FileExistsError('Different immutable spectral provenance: '+str(path))
        return
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.tmp-'+str(os.getpid()))
    with temporary.open('xb') as stream:
        stream.write(data);stream.flush();os.fsync(stream.fileno())
    try:
        try:
            os.link(temporary,path)
        except FileExistsError:
            if path.read_bytes()!=data:
                raise
    finally:
        temporary.unlink()


def argument(argv,name):
    if argv.count(name)!=1:
        raise ValueError('Exactly one explicit argument is required: '+name)
    i=argv.index(name)
    if i+1==len(argv):
        raise ValueError('Argument value is missing: '+name)
    return argv[i+1]


def add_exact(argv,name,value):
    if name in argv:
        if argument(argv,name)!=str(value):
            raise ValueError('A frozen spectral argument differs: '+name)
    else:
        argv.extend([name,str(value)])


def read_arrays(path,record,np):
    values={};pieces=[]
    if set(record['arrays'])!={'x','y','p','cubic','rms'}:
        raise ValueError('The five complete raw arrays are required')
    for name,item in record['arrays'].items():
        shape=tuple(item['shape'])
        if item['dtype']!='float64' or any(type(v) is not int or v<0 for v in shape):
            raise ValueError('Unexpected raw dtype or shape')
        flat=np.empty(math.prod(shape),dtype=np.float64)
        end=0
        for chunk in item['chunks']:
            if Path(chunk['file']).name!=chunk['file'] or chunk['first']!=end:
                raise ValueError('Nonlocal or incomplete raw chunk sequence')
            piece=path.parent/chunk['file']
            if digest(piece)!=chunk['sha256']:
                raise ValueError('Raw piece SHA mismatch: '+str(piece))
            block=np.load(io.BytesIO(gzip.decompress(piece.read_bytes())),allow_pickle=False)
            if block.dtype!=np.float64 or block.shape!=(chunk['count'],):
                raise ValueError('Raw piece binary layout differs')
            flat[end:end+len(block)]=block
            end+=len(block)
            pieces.append(dict(file=str(piece),sha256=chunk['sha256'],bytes=piece.stat().st_size))
        if end!=flat.size or not np.isfinite(flat).all():
            raise ValueError('Raw array is incomplete or nonfinite')
        values[name]=flat.reshape(shape)
    return values,pieces


def resource_class(Base,old_heap,semi_space):
    from strong_tail_constructor_guard import protect_tail_class
    worker=HERE/'tail_frozen_worker.mjs'
    worker_sha=digest(worker)

    class ExplicitFrozenResourcePort(Base):
        def __init__(self,*args,**kwargs):
            prefix=kwargs.get('record_prefix',args[2] if len(args)>2 else None)
            requested=kwargs.get('node_heap',args[3] if len(args)>3 else None)
            if prefix is None or requested!=old_heap:
                raise ValueError('Explicit frozen-worker heap request differs')
            prefix=Path(prefix);original=subprocess.Popen;seen=[]
            def spawn(command,*rest,**kw):
                if (not isinstance(command,(list,tuple)) or not command or
                        command[0]!='node' or str(worker) not in command):
                    return original(command,*rest,**kw)
                if seen or command.count(str(worker))!=1 or not isinstance(kw.get('env'),dict):
                    raise ValueError('Expected one owned frozen worker constructor')
                before='--max-old-space-size='+str(old_heap)
                after=before+' --max-semi-space-size='+str(semi_space)
                if kw['env'].get('NODE_OPTIONS')!=before or digest(worker)!=worker_sha:
                    raise ValueError('Original frozen worker/options changed')
                record=dict(scope='Only Node young-space launch option; no mathematical change',
                    entry_sha256=SELF_SHA,worker_sha256=worker_sha,
                    actual_command=list(command),NODE_OPTIONS_before=before,NODE_OPTIONS_after=after,
                    only_changed_environment_key='NODE_OPTIONS',
                    MJS_bytes_unchanged=True,original_full_Jacobian_and_audit_preserved=True)
                atomic_new_or_same(prefix.with_name(prefix.name+'_spectral-Node-intent.json'),record)
                changed={**kw,'env':{**kw['env'],'NODE_OPTIONS':after}}
                proc=original(command,*rest,**changed)
                self.proc=proc
                seen.append({**record,'owned_child_pid':proc.pid})
                return proc
            subprocess.Popen=spawn
            try:
                super().__init__(*args,**kwargs)
                if len(seen)!=1 or seen[0]['owned_child_pid']!=self.proc.pid:
                    raise ValueError('The explicit resource option did not reach this frozen worker')
                atomic_new_or_same(prefix.with_name(prefix.name+'_spectral-Node-observed.json'),seen[0])
            finally:
                subprocess.Popen=original
    return protect_tail_class(ExplicitFrozenResourcePort)


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--spectral-fixed-raw',type=Path,required=True)
    parser.add_argument('--spectral-fixed-report',type=Path,required=True)
    parser.add_argument('--spectral-warm-tail',type=Path,required=True)
    parser.add_argument('--spectral-baseline-config',type=Path,required=True)
    parser.add_argument('--spectral-temporary-parent',type=Path,required=True)
    parser.add_argument('--spectral-node-young-space',type=int,choices=(1,2,4,8,16),default=4)
    parser.add_argument('--spectral-prepare-only',action='store_true')
    own,remaining=parser.parse_known_args()
    for flag in ('--raw-collocation-restart','--restart','--postprocess-only','--warm-scale',
                 '--allow-converged-design-reference','--extra-physical-mesh','--check-only','--tail-config','--prepare-only'):
        if flag in remaining:
            raise ValueError('This exact spectral entry owns or disables '+flag)
    reference_file=Path(argument(remaining,'--fixed-reference'))
    out=Path(argument(remaining,'--out-prefix'))
    Mnew=int(argument(remaining,'--modes'));Nnew=int(argument(remaining,'--angular'))
    target_tol=float(argument(remaining,'--tol'))
    max_nodes=int(argument(remaining,'--max-nodes'))
    old_heap=int(argument(remaining,'--node-heap'))
    if (Mnew,Nnew)!=(28,1024) or old_heap<=0:
        raise ValueError('This prepared first refinement is explicitly M28/N1024')
    for name,expected in EXPECTED_SOURCE_SHA256.items():
        if digest(HERE/name)!=expected:
            raise ValueError('Frozen Python/source interface differs: '+name)
    saved=document(reference_file);raw_record=document(own.spectral_fixed_raw)
    report=document(own.spectral_fixed_report);tail=document(own.spectral_warm_tail)
    cfg0=document(own.spectral_baseline_config)
    if (not saved.get('solver_success') or saved.get('audit_pending',True) or
            not saved['config'].get('actual_nonlinear_tail') or
            not saved['config'].get('fixed_metric') or not raw_record.get('solver_success') or
            not raw_record.get('raw_collocation_only') or raw_record.get('physical_surface') is not False):
        raise ValueError('A genuinely accepted actual fixed view and full raw state are required')
    if saved['raw_collocation_checkpoint']['sha256']!=digest(own.spectral_fixed_raw):
        raise ValueError('The accepted fixed view links a different raw checkpoint')
    if (report['output']['sha256']!=digest(reference_file) or
            report['raw_output']['sha256']!=digest(own.spectral_fixed_raw)):
        raise ValueError('The fixed-view report does not bind these exact outputs')
    required=('complete_H_bitwise_equal','raw_x_y_cubic_unchanged','physical_quintics_unchanged',
              'all_core_coefficients_unchanged','gauge_unchanged','original_numerical_reference_unchanged',
              'eight_physical_data_unchanged')
    if (not all(report.get(k) is True for k in required) or
            report.get('nonlinear_solve_run') is not False or report.get('tail_worker_started') is not False or
            report.get('original_parameter_count')!=27 or report.get('fixed_parameter_count')!=24 or
            report.get('counters')!={'raw_restorations':1,'residual_checks':1,'tail_start_attempts':0}):
        raise ValueError('The real 27-to-24 physical/RMS/BC conversion has not passed')
    ident=raw_record['identity'];M=int(ident['modes']);n=3*M+1
    if M!=24 or saved['modes']!=M or not ident['fixed'] or target_tol!=ident['tol']:
        raise ValueError('Expected the original fixed M24 and unchanged radial tolerance')
    if Nnew<=ident['angular'] or target_tol!=1e-7:
        raise ValueError('The explicit angular increase/original tolerance differs')
    for a,b in (('gauge','gauge_amplitude'),('profile','frozen_profile'),
                ('physical_tail_parameters','physical_tail_parameters'),('physical_tail_cut','physical_tail_cut'),
                ('reference_coefficients','chart_reference_coefficients'),
                ('reference_frequencies','chart_reference_frequencies')):
        if canonical(ident[a])!=canonical(saved[b]):
            raise ValueError('Fixed raw and physical identity differ: '+a)
    if ident['numerical_reference_knots']!=saved['numerical_meridian_chart']['reference_t']:
        raise ValueError('The saved numerical reference changed')
    if saved['angular_chart']!='general-support-core-blend-v1':
        raise ValueError('Only the original fixed material-angle chart is supported')
    for key in ('initial_speed_pulse','initial_speed_frontload'):
        if saved['frozen_profile'].get(key,0)!=0:
            raise ValueError('Nonzero new initial laws require their explicit provider entry')
    context=ident['coupling_context']
    if (not context.get('actual_nonlinear_tail') or context['coupling']!='outer' or
            context['client']!='stored-resumable' or
            context['tail_config_sha256']!=digest(own.spectral_baseline_config)):
        raise ValueError('Original complete actual coupling/config identity differs')
    if (report['rms_max']>target_tol or report['all_boundary_max']>ident['bc_tol'] or
            report['true_physical_boundary_max']>context['actual_tail_tolerance']):
        raise ValueError('The original fixed view did not satisfy its unchanged gates')
    request,response=tail['request'],tail['response']
    if (not request.get('jacobian') or not request.get('audit') or not response.get('converged') or
            not response.get('audit') or response['residual']>cfg0['solveTolerance'] or
            len(response['heightJetJacobian'])!=(3*M+2)*M or
            tail.get('source_sha256')!=saved['actual_tail']['source_sha256']):
        raise ValueError('The complete original final audited tail is required as a warm source')
    for key in set(cfg0)|set(tail['config']):
        if key not in IO_KEYS and canonical(cfg0.get(key))!=canonical(tail['config'].get(key)):
            raise ValueError('Original finite tail configuration differs: '+key)
    for key,value in saved['physical_tail_parameters'].items():
        if cfg0.get(key)!=value:
            raise ValueError('Tail physical parameter differs: '+key)
    if cfg0['modes']!=24 or cfg0['spacing']!=2 or cfg0['quadrature']!=512:
        raise ValueError('Expected the exact original tail discretization')
    import numpy as np
    from scipy.interpolate import PPoly
    arrays,pieces=read_arrays(own.spectral_fixed_raw,raw_record,np)
    nodes=len(arrays['x'])
    if (arrays['y'].shape!=(n,nodes) or arrays['cubic'].shape!=(4,nodes-1,n) or
            arrays['p'].shape!=(M,) or arrays['rms'].shape!=(nodes-1,) or
            arrays['p'].tolist()!=raw_record['parameter_state'] or
            arrays['p'].tolist()!=saved['parameters'] or np.any(np.diff(arrays['x'])<=0) or
            arrays['x'][0]!=0. or arrays['x'][-1]!=1. or max_nodes<nodes):
        raise ValueError('The full original raw layout or t interval differs')
    if saved['core']['frequencies']!=list(range(2,2*M+1,2)) or len(saved['core']['coefficients'])!=M:
        raise ValueError('All original 24 core modes are required')
    old_H=-float(saved['gauge_amplitude'])*arrays['y'][2*M+1:,-1]
    if np.asarray(request['height'],dtype=np.float64).tobytes()!=old_H.tobytes():
        raise ValueError('The audited original full H does not match this raw state')
    old_z0=2*M+1;new_z0=2*Mnew+1
    # Pinned CylindricalPrefix.basis: row0=er; radial cos rows1..M;
    # tangent sin rows M+1..2M; height cos rows 2M+1..3M.
    mapping=np.r_[np.arange(M+1),Mnew+1+np.arange(M),new_z0+np.arange(M)]
    y=np.zeros((3*Mnew+1,nodes),dtype=np.float64);y[mapping]=arrays['y']
    cubic=np.zeros((4,nodes-1,3*Mnew+1),dtype=np.float64);cubic[:,:,mapping]=arrays['cubic']
    p=np.zeros(Mnew,dtype=np.float64);p[:M]=arrays['p']
    if y[mapping].tobytes()!=arrays['y'].tobytes() or cubic[:,:,mapping].tobytes()!=arrays['cubic'].tobytes():
        raise ValueError('The old raw coefficients were not embedded bitwise')
    new_rows=sorted(set(range(3*Mnew+1))-set(mapping.tolist()))
    if not np.all(y[new_rows]==0) or not np.all(cubic[:,:,new_rows]==0) or not np.all(p[M:]==0):
        raise ValueError('New modes must start exactly at zero')
    cfg=copy.deepcopy(cfg0);cfg['modes']=Mnew
    cfg.update(initialCheckpoint=str(own.spectral_warm_tail.resolve()),
        traceFile=str(out.with_name(out.name+'-tail-trace.jsonl').resolve()),
        iterationCheckpointFile=str(out.with_name(out.name+'-tail-iteration.json.gz').resolve()),
        trialDiagnosticFile=str(out.with_name(out.name+'-tail-trials.jsonl').resolve()))
    changed=[key for key in sorted(set(cfg)|set(cfg0)) if canonical(cfg.get(key))!=canonical(cfg0.get(key))]
    if set(changed)-IO_KEYS!={'modes'}:
        raise ValueError('Only tail mode count and explicit IO locations may change')
    config_file=out.with_name(out.name+'-config.json')
    atomic_new_or_same(config_file,cfg)
    remaining+=['--tail-config',str(config_file),'--raw-collocation-restart',str(own.spectral_fixed_raw)]
    add_exact(remaining,'--nodes',0)
    add_exact(remaining,'--meridian-chart','all-knots')
    add_exact(remaining,'--client','stored-resumable')
    add_exact(remaining,'--coupling','outer')
    add_exact(remaining,'--actual-tail-tol',repr(context['actual_tail_tolerance']))
    add_exact(remaining,'--radial-batch-size',8)
    add_exact(remaining,'--collocation-batch-size',12)
    add_exact(remaining,'--point-cache-limit',2)
    own.spectral_temporary_parent.mkdir(parents=True,exist_ok=True)
    physical_chunks=[]
    for item in saved['pp_coefficient_chunks']:
        if Path(item['file']).name!=item['file']:
            raise ValueError('Physical coefficient chunk must be local')
        path=reference_file.parent/item['file']
        if digest(path)!=item['sha256'] or path.stat().st_size!=item['bytes']:
            raise ValueError('The original full physical interpolant changed')
        physical_chunks.append(dict(file=str(path),sha256=item['sha256'],bytes=item['bytes']))
    plan=dict(scope=__doc__,entry_sha256=SELF_SHA,status='prepared; not a new numerical result',
        supersedes_unexecuted_draft_blob='7128ec437ce72279aa665dcff93c7dfbf8d8f3d7',
        draft_correction='Pinned cylindrical radial mean is row0; preserve M+1 radial, M tangent, M height channels',
        fixed_reference=dict(file=str(reference_file),sha256=digest(reference_file)),
        fixed_raw=dict(file=str(own.spectral_fixed_raw),sha256=digest(own.spectral_fixed_raw)),
        fixed_view_report=dict(file=str(own.spectral_fixed_report),sha256=digest(own.spectral_fixed_report)),
        warm_tail=dict(file=str(own.spectral_warm_tail),sha256=digest(own.spectral_warm_tail),
                       role='old-M accepted geometric warm only; not new-M response/Jacobian'),
        baseline_config=dict(file=str(own.spectral_baseline_config),sha256=digest(own.spectral_baseline_config)),
        new_config=dict(file=str(config_file),sha256=digest(config_file),changed_fields=changed),
        old_modes=M,new_modes=Mnew,old_angular=ident['angular'],new_angular=Nnew,
        tail_quadrature_unchanged=cfg0['quadrature'],radial_tolerance=target_tol,
        initial_nodes=nodes,maximum_nodes=max_nodes,all_original_t_nodes_retained_bitwise=True,
        original_t_interval=arrays['x'][[0,-1]].tolist(),original_numerical_reference=ident['numerical_reference_knots'],
        state_channel_embedding=mapping.tolist(),new_zero_state_rows=new_rows,
        all_old_raw_x_y_cubic_p_retained_bitwise=True,radial_mean_channel_row0_preserved=True,
        vertical_height_mean_is_not_a_raw_channel=True,
        vertical_mean_recomputed_by_unchanged_complete_flow_rule=True,
        no_pullback_no_interpolation_no_inlet_correction=True,
        new_core_modes_are_unknown_boundary_fields=True,profile=saved['frozen_profile'],
        physical_length=saved['meridian_length'],gauge=saved['gauge_amplitude'],
        source_sha256={**EXPECTED_SOURCE_SHA256,Path(__file__).name:SELF_SHA},
        MJS_source_sha256={path.name:digest(path) for path in sorted(HERE.glob('*.mjs'))},
        raw_pieces=pieces,physical_pieces=physical_chunks,
        original_raw_RMS_is_not_new_M_RMS=True,original_final_gates_unchanged=True,
        node_old_heap_MiB=old_heap,node_young_semi_space_MiB=own.spectral_node_young_space,
        source_MJS_modified=False,command_arguments=remaining)
    plan_file=out.with_name(out.name+'-spectral-plan.json')
    atomic_new_or_same(plan_file,plan)
    import root_actual_frozen_neck as frozen
    import root_raw_collocation as raw
    import strong_disk_actual_backend as backend
    old_loader=frozen.bounded.adapter.module;old_read=raw.read;old_argv=sys.argv
    counters=dict(raw_spectral_embeddings=0,resource_wrapped_clients=0)
    diagnostic={}
    runtime=None
    start=time.monotonic()

    def mapped_read(path,obj,args):
        if Path(path).resolve()!=own.spectral_fixed_raw.resolve():
            return old_read(path,obj,args)
        counters['raw_spectral_embeddings']+=1
        if counters['raw_spectral_embeddings']!=1 or not obj.fixed or obj.tail is not None or obj.M!=Mnew or obj.nt!=Nnew:
            raise ValueError('Expected one genuine M28 Fixed/Actual object before any worker')
        obj._neck_knots=np.asarray(ident['numerical_reference_knots'],dtype=float).copy()
        obj.chart_breaks=obj._neck_knots.copy()
        obj._flow=obj._flow_key=obj._core_key=obj._initial=None
        obj.select(p.copy())
        actual=raw.identity(obj,args)
        for key in ('gauge','profile','physical_tail_parameters','physical_tail_cut',
                    'reference_coefficients','reference_frequencies','parameter_layout',
                    'tol','bc_tol','numerical_reference_knots'):
            if canonical(actual[key])!=canonical(ident[key]):
                raise ValueError('The live fixed spectral physical identity changed: '+key)
        if actual['modes']!=Mnew or actual['angular']!=Nnew or not actual['fixed']:
            raise ValueError('Live spectral dimensions/fixed status differ')
        current_context=actual['coupling_context']
        for key in ('actual_nonlinear_tail','client','coupling','actual_tail_tolerance'):
            if current_context[key]!=context[key]:
                raise ValueError('Original actual outer gate changed: '+key)
        if current_context['tail_config_sha256']!=digest(config_file):
            raise ValueError('The live new-M complete tail config differs')
        flow=obj.flow();obj.initial(p)
        # Verify the real pinned basis, rather than inferring row layout from n.
        basis_function=getattr(flow.basis,'__func__',None)
        if basis_function is None:
            raise ValueError('The live cylindrical basis must be an explicit bound method')
        basis_file=Path(basis_function.__code__.co_filename)
        if (digest(basis_file)!='e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2' or
                basis_function.__qualname__!='CylindricalPrefix.basis'):
            raise ValueError('The pinned complete cylindrical basis changed')
        old_basis=basis_function(SimpleNamespace(M=M,n=n,even=2*np.arange(1,M+1)),512)
        new_basis=flow.basis(512)
        for order,(old_values,new_values) in enumerate(zip(old_basis,new_basis)):
            if new_values[mapping].tobytes()!=old_values.tobytes():
                raise ValueError('Spectral embedding changed a live basis angular jet: '+str(order))
        del old_basis,new_basis
        if obj.iz!=new_z0 or flow.ir!=1 or flow.it!=Mnew+1 or flow.iz!=new_z0:
            raise ValueError('Live complete cylindrical mode offsets differ')
        expected_core=np.r_[np.asarray(saved['core']['coefficients']),np.zeros(Mnew-M)]
        if np.asarray(obj._core.coefficients).tobytes()!=expected_core.tobytes():
            raise ValueError('The complete old core was not preserved with zero new modes')
        if flow.cfg!=saved['frozen_profile'] or flow.end!=saved['meridian_length']:
            raise ValueError('The final physical profile or length changed')
        old_breaks=np.asarray(saved['numerical_meridian_chart']['physical_s'],dtype=np.float64)
        if np.asarray(flow.breaks,dtype=np.float64).tobytes()!=old_breaks.tobytes():
            raise ValueError('The physical knot values changed')
        s,ds=obj.chart(arrays['x'],p[0])
        if (np.asarray(s,dtype=np.float64).tobytes()!=np.asarray(saved['mesh'],dtype=np.float64).tobytes()
                or not np.all(np.isfinite(ds)) or np.min(ds)<=0):
            raise ValueError('The original physical sampling or positive numerical chart changed')
        current_H=obj.tail_height(y[:,-1])
        # Multiplication by sigma=-1 may produce -0 in newly zero H components.
        # Old components must be bitwise equal; new components must be exact zero.
        if current_H[:M].tobytes()!=old_H.tobytes() or not np.all(current_H[M:]==0):
            raise ValueError('The full new-M boundary warm vector is not the exact spectral extension')
        sol=SimpleNamespace(x=arrays['x'].copy(),y=y.copy(),p=p.copy(),
            sol=PPoly.construct_fast(cubic.copy(),arrays['x'].copy(),extrapolate=True,axis=1),
            rms_residuals=arrays['rms'].copy(),status=1,success=False,
            message='Exact old raw spectral embedding only; new-M RMS and actual tail not accepted',niter=0)
        warm_path=out.with_name(out.name+'-spectral-warm-raw-collocation.json.gz')
        if warm_path.exists():
            raise FileExistsError('Fresh spectral warm checkpoint prefix required')
        link=raw.write(warm_path,sol,obj,args,dict(spectral_warm_only=True,
            original_solver_success_not_inherited=True,source_plan_sha256=digest(plan_file),
            source_fixed_raw_sha256=digest(own.spectral_fixed_raw),
            old_RMS_array_retained_only_as_diagnostic=True))
        diagnostic.update(live_identity=actual,warm_checkpoint=link,
            exact_complete_warm_H=current_H.tolist(),new_H_not_audited=True,
            original_grid_retained_bitwise=True,physical_grid_retained_bitwise=True,
            actual_basis_zero_first_second_rows_bitwise_equal=True,
            pinned_basis_source_sha256=digest(basis_file),
            inlet_warm_mismatch=float(np.max(abs(y[:,0]-obj.initial(p)))),
            original_RMS_max=float(np.max(arrays['rms'])),original_core_preserved_bitwise=True)
        atomic_new_or_same(out.with_name(out.name+'-spectral-warm-verified.json'),diagnostic)
        print(json.dumps(dict(event='same_g_spectral_warm_verified',nodes=nodes,modes=Mnew,
            warm_checkpoint=link,new_H_not_audited=True,original_g_and_chart_unchanged=True)),flush=True)
        # This manifest was written above with its true new dimensions and
        # explicitly unsuccessful warm status. The input M24 manifest is untouched.
        record=document(warm_path)
        return sol,record

    def loader(name,path):
        loaded=old_loader(name,path)
        if Path(path).name=='tail_frozen_client.py':
            loaded.WeightedTailPort=resource_class(loaded.WeightedTailPort,old_heap,own.spectral_node_young_space)
            counters['resource_wrapped_clients']+=1
        return loaded

    if own.spectral_prepare_only:
        sys.argv=[old_argv[0],*remaining,'--prepare-only']
        try:
            frozen.main()
        finally:
            sys.argv=old_argv
        print(json.dumps(dict(event='same_g_M28_source_and_data_prepared',
            plan=str(plan_file),sha256=digest(plan_file),numerical_execution=False)),flush=True)
        return
    for suffix in ('-summary.json','.json.gz','-disk-events.jsonl','-spectral-warm-raw-collocation.json.gz'):
        if Path(str(out)+suffix).exists():
            raise FileExistsError('Fresh numerical output prefix required: '+str(out)+suffix)
    # Disk QR lives only in the caller-owned temporary directory. The precise
    # matrix/factor byte counts and the current free space are logged by the
    # existing backend; no missing-space condition is called a mathematical failure.
    resource_note=dict(temporary_parent=str(own.spectral_temporary_parent.resolve()),
        free_bytes_before=shutil.disk_usage(own.spectral_temporary_parent).free,
        initial_interior_matrix_block_bytes_only=(nodes-1)*(3*Mnew+1)*(2*(3*Mnew+1)+Mnew)*8,
        no_claim_about_causes_of_past_terminations=True)
    atomic_new_or_same(out.with_name(out.name+'-spectral-storage-start.json'),resource_note)
    raw.read=mapped_read;frozen.bounded.adapter.module=loader
    try:
        runtime=backend.install_disk_backend(frozen.bounded,out,dict(
            backward_error_tolerance=5e-11,heartbeat_seconds=15.,
            temporary_parent=str(own.spectral_temporary_parent.resolve())))
        sys.argv=[old_argv[0],*remaining]
        frozen.main()
    finally:
        sys.argv=old_argv;raw.read=old_read;frozen.bounded.adapter.module=old_loader
        if runtime is not None:
            runtime.finish()
        status=dict(entry_sha256=SELF_SHA,plan_sha256=digest(plan_file),counters=counters,
            seconds=time.monotonic()-start,warm_verification_recorded=bool(diagnostic),
            original_math_and_acceptance_preserved=True,MJS_sources_unchanged=True)
        summary=out.with_name(out.name+'-summary.json')
        if summary.is_file():
            final=document(summary)
            status.update(solver_success=final.get('solver_success'),
                          audit_pending=final.get('audit_pending'),message=final.get('message'),
                          max_rms_collocation_residual=final.get('max_rms_collocation_residual'),
                          actual_tail_residual=final.get('actual_tail',{}).get('residual'))
        status['plan_file']=str(plan_file)
        status['warm_record_file']=(str(out.with_name(out.name+'-spectral-warm-verified.json'))
                                   if diagnostic else None)
        for path in (out.with_suffix('.json.gz'),summary):
            if not path.is_file():
                continue
            result=document(path)
            result['same_g_spectral_refinement']=copy.deepcopy(status)
            data=(json.dumps(result,indent=2)+'\n').encode()
            if path.suffix=='.gz':
                data=gzip.compress(data,mtime=0)
            if len(data)>=5_000_000:
                raise ValueError('Result metadata exceeds the original file-size limit')
            temporary=path.with_name(path.name+'.spectral-metadata.tmp')
            temporary.write_bytes(data);temporary.replace(path)
        atomic_new_or_same(out.with_name(out.name+'-spectral-terminal.json'),status)
    if counters!={'raw_spectral_embeddings':1,'resource_wrapped_clients':1}:
        raise RuntimeError('Expected exactly one explicit spectral embedding and live-client loader')
    final=document(out.with_name(out.name+'-summary.json'))
    if not final.get('solver_success') or final.get('audit_pending',True):
        raise RuntimeError('The original new-M full actual acceptance did not complete')
    print(json.dumps(dict(event='same_g_M28_actual_refinement_complete',
        original_g_unchanged=True,solver_success=True,audit_pending=False,
        out_prefix=str(out))),flush=True)


if __name__=='__main__':
    main()
