#!/usr/bin/env python3
"""Refine one genuine original-support actual-DN field with its whole g fixed.

First input: the real lambda-one complete-prefix-QR chord return in its explicitly preserved
original frozen repository. Later inputs: this entry's own strictly accepted
fixed-metric returns. No linear BVP or old warm phase model is invoked. All
source knots, physical support coefficients and the complete exact core lift
are retained in the unaccepted initial guess. The original full nonlinear
tail, complete height Jacobian/audit and eight-outer boundary gate remain.
Finite accepted refinements do not prove a C2 limit or a closed surface.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import copy
import gc
import gzip
import json
import math
from pathlib import Path
import resource
import shutil
import sys
import threading
import time
import traceback
from types import SimpleNamespace

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import qr_fixed_support_actual_model as model
import qr_fixed_support_actual_resources as resources
from qr_fixed_support_actual_model import sha,load,ref,module,checked


def diagnostic(value):
    if isinstance(value,float) and not math.isfinite(value):
        return 'nonfinite:'+repr(value)
    if isinstance(value,dict):
        return {str(k):diagnostic(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [diagnostic(v) for v in value]
    return value


def write(path,value):
    temporary = Path(path).with_suffix(Path(path).suffix+'.tmp')
    temporary.write_text(json.dumps(diagnostic(value),indent=2,allow_nan=False)+'\n')
    temporary.replace(path)


def full_height_bytes(height,M):
    result = np.asarray(height,dtype='<f8')
    if result.shape != (M,) or not np.all(np.isfinite(result)):
        raise ValueError('Every complete physical height coefficient must be finite')
    return result.tobytes()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo','work','source-run','native-source','base-tail-config','tail-config','port','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--origin-repo',type=Path)
    parser.add_argument('--coupling-summary',type=Path)
    parser.add_argument('--modes',type=int,required=True)
    parser.add_argument('--angular',type=int)
    parser.add_argument('--tol',type=float,required=True)
    parser.add_argument('--bc-tol',type=float,required=True)
    parser.add_argument('--physical-bc-tol',type=float,required=True)
    parser.add_argument('--radial-refine',type=int,default=1)
    parser.add_argument('--audit-angular',type=int,nargs='+')
    parser.add_argument('--tail-warmup',type=float,nargs='*',default=[])
    parser.add_argument('--max-nodes',type=int,default=6000)
    parser.add_argument('--verbose',type=int,default=2)
    parser.add_argument('--prepare-only',action='store_true')
    args = parser.parse_args()
    repo,work,out = args.repo.resolve(),args.work.resolve(),args.outdir.resolve()
    source_path,native = args.source_run.resolve(),args.native_source.resolve()
    if repo != HERE.parents[4]:
        raise ValueError('--repo must be the explicitly executing numerical source tree')
    if (repo == work or repo in work.parents or work not in out.parents
            or work not in source_path.parents or work not in native.parents
            or args.max_nodes < 2 or not 1 <= args.modes <= 64):
        raise ValueError('Keep actual fields outside source trees and retain the native M<=64 scope')
    if (args.tail_warmup != sorted(set(args.tail_warmup))
            or any(not math.isfinite(v) or not 0 < v < 1 for v in args.tail_warmup)):
        raise ValueError('Explicit warm factors must be strictly increasing in (0,1)')
    for file in (args.base_tail_config,args.tail_config,args.port):
        if work not in file.resolve().parents:
            raise ValueError('Prepared original numerical inputs must remain in this runner work tree')
    out.mkdir(parents=True,exist_ok=False)
    begin = time.monotonic()
    lock,done = threading.RLock(),threading.Event()
    tail = monitor = None
    record = dict(schema='original-r53-fixed-support-qr-anchor-actual-dn-run-v1',scope=__doc__,
        model_kind=model.KIND,anchor_source_kind=model.ANCHOR_SOURCE_KIND,
        repository=str(repo),command=[sys.executable,*sys.argv],
        command_kind='Python application argv with interpreter flags recorded separately',
        actual_interpreter_argv=list(sys.orig_argv),
        status='validating_actual_source',fixed_metric=True,fixed_core=False,
        fixed_metric_refinement=True,fixed_metric_design_continuation=False,
        boundary_problem_changed=False,same_complete_metric_as_source=True,
        terminal_kind='original_actual_nonlinear_dn',actual_tail_requested=True,
        original_actual_nonlinear_tail=True,parameter_zero_meaning=model.PARAMETER_ZERO,
        linear_bvp_invoked=False,solver_invoked=False,solver_success=False,
        finite_actual_dn_candidate_pass=False,initializer_is_accepted_solution=False,
        exact_lift_coefficient=1,acceptance_kind=None,
        full_Cartesian_seam_paid=False,C2_convergence_proven=False,
        complete_surface=False,stages=[],actual_outer_checks=[],progress={})

    def save():
        with lock:
            record['elapsed'] = time.monotonic()-begin
            write(out/'run.json',record)
            compact = {key:record[key] for key in ('status','model_kind','solver_success',
                'finite_actual_dn_candidate_pass','complete_surface','error','result') if key in record}
            compact.update(progress=record['progress'],stages=record['stages'][-6:])
            if len(json.dumps(diagnostic(compact)).encode()) > 24000:
                raise RuntimeError('The scalar actual-DN summary exceeded 24 KiB')
            write(out/'summary.json',compact)

    def event(name,**data):
        with lock:
            row = diagnostic(dict(event=name,elapsed=time.monotonic()-begin,
                maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**data))
            with (out/'events.jsonl').open('a') as stream:
                stream.write(json.dumps(row,allow_nan=False)+'\n')
            record['progress']['last_actual_event'] = row
            save()
        print(json.dumps(row,allow_nan=False),flush=True)

    save()
    try:
        context = model.accepted_input(source_path,repo=repo,origin_repo=args.origin_repo,
                                       coupling_summary=args.coupling_summary)
        source = context['record']
        gates = dict(tol=args.tol,bc_tol=args.bc_tol,physical_bc_tol=args.physical_bc_tol,
            max_nodes=args.max_nodes,tail_solve_tolerance=2e-9,original_outer_budget=8,
            metric_component_fft=1e-6,metric_sample_operator=1e-6)
        for key,upper in (('tol',1e-6),('bc_tol',1e-7),('physical_bc_tol',2e-9)):
            if not 0 < gates[key] <= min(upper,context['gates'][key]):
                raise ValueError('An original finite gate cannot be loosened: '+key)
        if gates['tol'] >= context['gates']['tol']:
            raise ValueError('The real radial collocation tolerance must be strictly tightened')
        angular = max(source['angular'],32*args.modes,args.angular or 0)
        record.update(modes=args.modes,angular=angular,gates=gates,
            actual_source=ref(source_path),actual_source_role=context['role'],
            actual_source_raw=context['raw'],actual_source_physical=context['physical'],
            actual_source_final_physical_packet=context['final_packet'],
            actual_source_final_physical_height_binding=context['final_height_binding'],
            linear_port_path=str(args.port.resolve()),linear_port_sha256=sha(args.port),
            base_tail_settings=str(args.base_tail_config.resolve()),base_tail_settings_sha256=sha(args.base_tail_config),
            tail_settings=str(args.tail_config.resolve()),tail_settings_sha256=sha(args.tail_config))
        record['first_actual_anchor_unknowns_converted_to_fixed_metric'] = (
            context['role']=='accepted_original_support_qr_chord_design_actual_return')
        record['actual_design_source_relabelled_as_a_fixed_solver_return'] = False
        obj,x,y,par,transfer = model.prepare(context,record,radial_refine=args.radial_refine)
        model.validate_refinement_definition(record,context)
        record['complete_lift_transfer'] = transfer
        if len(x) > args.max_nodes:
            raise ValueError('The maximum node count is below the preserved complete initial mesh')
        original_repo = Path(context['original_repository'])
        scripts = original_repo/'topics/visible-flex-held-10pct/scripts'
        coupler = sys.modules['_metric_coupler']
        cache = module('_fixed_actual_readonly_fourier_cache',HERE.parent/'design/cached_fourier_tables.py')
        cache.install(sys.modules['_metric_fourier_jac'])
        core_cache = module('_fixed_actual_complete_core_cache',HERE.parent/'design/material_core_evaluate_cache.py')
        core_cache.install(sys.modules['material_flattened_support_core'].MaterialFlattenedSupportCore)
        cfg = load(args.tail_config)
        baseline = load(args.base_tail_config)
        port = load(args.port)
        source_cfg = load(checked(context['tail_settings']))
        manifest_path = native/'native-manifest.json'
        manifest = load(manifest_path)
        original = module('_fixed_actual_original_chord_api',scripts/'resume_20261126/continue_original_actual_dn_chord.py')
        original.verify_references(manifest)
        expected_native = dict(M=obj.M,spacing=3,quadrature=cfg['quadrature'],steps=cfg['steps'],
                               projectionFloor=.05,orientation=1,cuspAwareFlow=True)
        if (manifest['fixed_scope'] != expected_native
                or manifest['execution_provider']['workers'] not in (2,4)):
            raise ValueError('The independently prepared full native scope differs from this actual problem')
        with gzip.open(checked(context['final_packet']),'rt') as stream:
            parent_packet = json.load(stream)
        for name,expected in parent_packet['source_sha256'].items():
            if sha(native/'scripts'/name) != expected:
                raise ValueError('The original complete-state worker source changed: '+name)
        mean_nodes = record['mean_nodes']
        audit_angular = sorted(set(max(16*(3*obj.M+1),int(n)) for n in
            (args.audit_angular or [16*(3*obj.M+1),32*(3*obj.M+1)])))
        paths = [Path(__file__),*model.reviewed_source_paths(),HERE/'qr_fixed_support_actual_model.py',
            HERE/'qr_fixed_support_actual_acceptance.py',
            HERE.parent/'design/cached_fourier_tables.py',
            HERE.parent/'design/material_core_evaluate_cache.py',
            scripts/'resume_m3/actual_m3_metric_model.py',scripts/'resume_m3/audit_full_relative_metric.py',
            scripts/'resume_20261126/continue_original_actual_dn_chord.py',
            manifest_path,args.base_tail_config,args.tail_config,args.port]
        record.update(source_hashes={**source['source_hashes'],**resources.sources(),
                **{str(p.resolve()):sha(p) for p in paths}},
            native_manifest=ref(manifest_path),native_workers=manifest['execution_provider']['workers'],
            tail_resolution={k:cfg[k] for k in ('modes','quadrature','steps','depth','shootingParts')},
            actual_tail_RK_refined=cfg['steps']>source_cfg['steps'],actual_audit_angular=audit_angular,
            actual_complete_state_warm_start=True,complete_parent_packet_sources_preserved=True,
            raw_and_final_physical_heights_have_separate_bindings=True,
            warm_height_arithmetic='numpy: H * factor**np.arange(1,M+1)',
            tail_integration_scope='Original complete native discretization; no integration-error or limit bound inferred')
        obj.initial(par)
        if obj._core.homotopy != 1 or obj._core.curvature_blend != 1:
            raise ValueError('The original actual lambda-one support core changed')
        initial_raw = out/'initializer-raw.npz'
        np.savez_compressed(initial_raw,x=x,y=y,p=par,pscale=obj.pscale)
        record['initial_raw'] = ref(initial_raw)
        record['status'] = 'prepared_unaccepted_fixed_actual_support_initializer'
        save()
        if args.prepare_only:
            event('prepared_only',original_solves_executed=0,initial_nodes=len(x),modes=obj.M,
                fixed_delta=record['frozen_profile']['delta'],mean_nodes=mean_nodes)
            return 0
        class ActualSupportBVP(coupler.TailMixin,type(obj)):
            def terminal(self,value,parameters):
                self.initial(parameters)
                return super().terminal(value,parameters)
        obj.__class__ = ActualSupportBVP
        os.environ.update(VISIBLE_FLEX_NATIVE_MANIFEST=str(manifest_path),
            VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=sha(manifest_path),
            VISIBLE_FLEX_NATIVE_RUN_DIR=str(Path(cfg['traceFile']).parent/'native-runs'),
            VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
            VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
        for key in ('LD_PRELOAD','LD_LIBRARY_PATH'):
            os.environ.pop(key,None)
        def watch():
            while not done.wait(15):
                try:
                    value = original.last_scalar_event(Path(cfg['traceFile']))
                    if value is not None:
                        with lock:
                            record['progress']['last_actual_worker_trace'] = value
                            save()
                except (OSError,ValueError):
                    pass
        monitor = threading.Thread(target=watch,daemon=True)
        monitor.start()
        client = module('_fixed_actual_complete_native_client',native/'scripts/950f-tail-client-v3.py')
        record['status'] = 'initializing_original_tail'
        save()
        tail = client.WeightedTailPort(args.tail_config,native/'repro/source-root',out/'tail',node_heap=2048)
        obj.tail = tail
        for key,wanted in record['physical_tail_parameters'].items():
            if tail.ready['parameters'].get(key) != wanted:
                raise ValueError('The original tail physical parameter changed: '+key)
        for key in ('radius','backgroundSlope','backgroundSecond','E','Ep'):
            if tail.ready['cut'][key] != record['physical_tail_cut'][key]:
                raise ValueError('The actual original worker cut changed: '+key)
        write(out/'tail-ready.json',tail.ready)
        record['tail_ready'] = ref(out/'tail-ready.json')
        record['linear_dn_ready_max_difference'] = float(np.max(np.abs(tail.linearD-np.asarray(port['linearSlope'][:obj.M]))))

        def height_binding(tag,height,raw_file,physical_file,*,role,raw_height=None):
            full_height_bytes(height,obj.M)
            item = dict(schema='original-support-fixed-actual-height-v1',height_reference_kind=role,
                candidate_H=np.asarray(height,float).tolist(),modes=obj.M,gauge_q=obj.q,
                bridge_sigma=float(obj.bridge.sigma),mean_nodes=mean_nodes,
                parameter_zero_meaning=model.PARAMETER_ZERO,actual_source=ref(source_path),
                raw=ref(raw_file),physical=ref(physical_file) if physical_file is not None else None,
                raw_candidate_H=None if raw_height is None else np.asarray(raw_height,float).tolist(),
                fixed_problem=record['fixed_problem'],tag=tag,accepted_solution_claimed=False)
            path = out/('height-target-'+tag+'.json')
            write(path,item)
            return path

        def accepted_tail(height,*,binding,factor,name,jacobian=True):
            response = tail.solve(height,jacobian=jacobian,audit=True)
            if (response.get('converged') is not True or response.get('failed')
                    or not model.finite(response.get('residual'),2e-9)
                    or not isinstance(response.get('audit'),dict)):
                raise FloatingPointError('The original complete audited nonlinear-tail gate failed')
            for key in ('fullD','normalizedFullDefect','minLeading','minD','formalCurvature',
                        'maxPhysicalPV','actualMetric','holonomy'):
                value = response['audit'].get(key)
                if (isinstance(value,bool) or not isinstance(value,(int,float))
                        or not math.isfinite(value)):
                    raise ValueError('The original complete tail audit scalar is missing/nonfinite: '+key)
            for key in ('height','slope','second'):
                full_height_bytes(response['jets'][key],obj.M)
            if jacobian:
                jac = np.asarray(response.get('heightJetJacobian'),float)
                if jac.shape != ((3*obj.M+2)*obj.M,) or not np.all(np.isfinite(jac)):
                    raise ValueError('The complete original height Jacobian did not return')
            packet = out/f'tail_{tail.calls:04d}.json.gz'
            with gzip.open(packet,'rt') as stream:
                saved = json.load(stream)
            wanted = full_height_bytes(height,obj.M)
            if (full_height_bytes(saved['request']['height'],obj.M) != wanted
                    or full_height_bytes(saved['response']['checkpoint']['cutHeight'],obj.M) != wanted
                    or saved['request']['audit'] is not True
                    or (jacobian and saved['request']['jacobian'] is not True)):
                raise ValueError('The actual saved packet is not this complete requested height')
            row = dict(name=name,factor=factor,full_height=factor==1.,requested_jacobian=jacobian,
                residual=response['residual'],converged=True,packet=ref(packet),
                height_reference=ref(binding),height_reference_key='candidate_H',height_arithmetic='numpy')
            record['stages'].append(row)
            event('actual_complete_tail_return',stage=row)
            return response,packet

        H = obj.bridge.sigma*obj.q*y[obj.iz:,-1]
        initial_binding = height_binding('initial-raw',H,initial_raw,None,role='unaccepted_complete_initial_nodal_height')
        for factor in args.tail_warmup:
            accepted_tail(H*factor**np.arange(1,obj.M+1),binding=initial_binding,
                          factor=factor,name='initial_warm',jacobian=False)
        response,packet = accepted_tail(H,binding=initial_binding,factor=1.,name='initial_full_H')
        from f6curve_domain_newton import install,STATS
        install()
        portable = module('_fixed_actual_original_domain_guard',scripts/'resume_m3/portable_prefix_continue.py')
        portable.install_rms_domain_guard()
        for outer in range(8):
            record.update(status='original_affine_inner_bvp',current_outer=outer,solver_invoked=True)
            save()
            obj.tail = coupler.AffineTailForInnerBVP(H,response,obj.M)
            try:
                gc.collect()
                sol = resources.solve(obj,x,y,par,outdir=out,record=record,event=event,gates=gates,verbose=args.verbose)
            finally:
                obj.tail = tail
            raw_file = out/f'inner-{outer:02d}.npz'
            np.savez_compressed(raw_file,x=sol.x,y=sol.y,p=sol.p,cubic_x=sol.sol.x,
                                cubic_c=sol.sol.c,rms=sol.rms_residuals,pscale=obj.pscale)
            candidate = obj.bridge.sigma*obj.q*sol.y[obj.iz:,-1]
            record.update(solver_success=bool(sol.success),acceptance_kind='actual_original_support_qr_anchor_fixed_dn_refinement_return',
                raw_return=dict(file=raw_file.name,sha256=sha(raw_file),success=bool(sol.success),status=int(sol.status),
                    message=str(sol.message),nodes=len(sol.x),rms=float(np.max(sol.rms_residuals)),
                    parameters=sol.p.tolist(),candidate_H=candidate.tolist()),domain_newton_stats=dict(STATS))
            save()
            if not sol.success:
                raise FloatingPointError('The original complete inner BVP did not converge')
            obj.initial(sol.p)
            record['returned_support_coefficients'] = np.asarray(obj._core.coefficients).tolist()
            record['returned_actual_q'] = float(obj.support_amplitude)
            flow = obj.flow(sol.p[0])
            physical = SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
            physical.sol = flow.c2_interpolant(physical)
            physical_file = out/f'physical-{outer:02d}.npz'
            np.savez_compressed(physical_file,x=physical.x,c=physical.sol.c,p=sol.p)
            binding = height_binding(f'outer-{outer:02d}-raw',candidate,raw_file,physical_file,
                                     role='actual_outer_raw_nodal_height',raw_height=candidate)
            record['status'] = 'original_actual_candidate_check'
            save()
            actual,packet = accepted_tail(candidate,binding=binding,factor=1.,name=f'outer_{outer:02d}_full_H')
            defect = float(np.max(np.abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p))))
            physical_bc = float(np.max(np.abs(obj.terminal(sol.y[:,-1],sol.p)*obj.bcweights)))
            row = dict(outer=outer,actual_bc=defect,physical_bc=physical_bc,actual_tail=actual['residual'],
                raw=ref(raw_file),physical=ref(physical_file),height_reference=ref(binding),packet=ref(packet))
            record['actual_outer_checks'].append(row)
            event('original_actual_outer_check',check=row)
            if defect <= gates['bc_tol'] and physical_bc <= gates['physical_bc_tol']:
                break
            x,y,par,H,response = sol.x,sol.y,sol.p,candidate,actual
        else:
            raise FloatingPointError('The original eight-outer actual boundary gate failed')
        shutil.copyfile(physical_file,out/'physical.npz')
        record.update(physical_sha256=sha(out/'physical.npz'),actual_scaled_bc_max=defect,
                      actual_physical_bc_max=physical_bc,status='auditing_frozen_actual_metric')
        save()
        metric = module('_fixed_actual_metric_audit',scripts/'resume_m3/audit_full_relative_metric.py')
        report = metric.audit_loaded_model(obj,metric.load_physical(out/'physical.npz'),
            angular=audit_angular,mean_nodes=mean_nodes,batch=8,target=1e-6)
        write(out/'relative-metric.json',report)
        record.update(relative_metric_sha256=sha(out/'relative-metric.json'),metric_diagnostics=report['rows'])

        # The full physical quintic endpoint defines the geometric tail. Its
        # rounded H can differ from the raw collocation endpoint; never swap
        # those source roles. A distinct actual request is made if necessary.
        flow = obj.flow(sol.p[0]);s = np.array([flow.end])
        Y,Yp,Ypp = (physical.sol(s,order) for order in (0,1,2))
        physical_H = obj.bridge.sigma*obj.q*Y[obj.iz:,0]
        final_binding = height_binding('final-physical',physical_H,raw_file,out/'physical.npz',
            role='actual_saved_physical_quintic_endpoint',raw_height=candidate)
        if full_height_bytes(physical_H,obj.M) == full_height_bytes(candidate,obj.M):
            final,final_packet = actual,packet
            record['final_physical_H_bitwise_equal_raw_H'] = True
            record['final_physical_packet_reuses_identical_original_full_H'] = True
        else:
            final,final_packet = accepted_tail(physical_H,binding=final_binding,factor=1.,name='final_physical_full_H')
            record['final_physical_H_bitwise_equal_raw_H'] = False
            record['final_physical_packet_reuses_identical_original_full_H'] = False
        endpoint_bc = float(np.max(np.abs(obj.terminal(Y[:,0],sol.p)*obj.bcweights)))
        n = max(512,64*obj.M)
        B,B1,B2 = flow.basis(n)
        fr,sp,dW = flow.velocity_s(s,Y,Yp,B1,B2)
        _,meanB1,meanB2 = flow.basis(mean_nodes)
        meanfr,_,mean_dW = flow.velocity_s(s,Y,Yp,meanB1,meanB2)
        mean = np.mean(meanfr['V'][:,:,2],axis=1)
        mean_s = np.mean(mean_dW[:,:,2],axis=1)
        geometry = fr['geo']
        chart_error = max(float(np.max(np.abs(geometry[key]))) for key in ('e','v','vs','vp'))
        if chart_error != 0:
            raise ValueError('The original exact identity cut chart is required')
        Fs = geometry['s1']+obj.q*flow.values(Yp,B)
        Fss = geometry['s2']+obj.q*flow.values(Ypp,B)
        Fs[:,:,2] += mean[:,None];Fss[:,:,2] += mean_s[:,None]
        Ft,Ftt,Fst = fr['d'],fr['dd'],sp
        a,ap,_ = flow.profile(s)
        E0,F0,G0 = (np.sum(left*right,axis=2) for left,right in ((Fs,Fs),(Fs,Ft),(Ft,Ft)))
        errors = np.stack((E0-1,F0/a[:,None],G0/a[:,None]**2-1),axis=2)
        Es,Et = 2*np.sum(Fs*Fss,axis=2),2*np.sum(Fs*Fst,axis=2)
        F_s = np.sum(Fss*Ft+Fs*Fst,axis=2);F_t = np.sum(Fst*Ft+Fs*Ftt,axis=2)
        Gs,Gt = 2*np.sum(Ft*Fst,axis=2),2*np.sum(Ft*Ftt,axis=2)
        c1 = np.stack((Es,Et,F_s/a[:,None]-ap[:,None]*F0/a[:,None]**2,
            F_t/a[:,None],Gs/a[:,None]**2-2*ap[:,None]*G0/a[:,None]**3,Gt/a[:,None]**2),axis=2)
        jets = final['jets'];E,sigma = jets['E'],obj.bridge.sigma
        r_ss = -jets['Ep']/(2*E**2)
        expected = (jets['meanSlope']/math.sqrt(E),sigma*(jets['meanSecond']/E+jets['meanSlope']*r_ss))
        expected_second = sigma*(np.asarray(jets['second'])/E+np.asarray(jets['slope'])*r_ss)
        seam = dict(mean_nodes=mean_nodes,angular_samples=n,cut_chart_error=chart_error,
            mean_first_actual=float(mean[0]),mean_second_actual=float(mean_s[0]),
            mean_first_expected=expected[0],mean_second_expected=expected[1],
            mean_first_mismatch=float(mean[0])-expected[0],mean_second_mismatch=float(mean_s[0])-expected[1],
            nonmean_first_mismatch=float(np.max(np.abs(obj.q*Yp[obj.iz:,0]-np.asarray(jets['slope'])/math.sqrt(E)))),
            nonmean_second_mismatch=float(np.max(np.abs(obj.q*Ypp[obj.iz:,0]-expected_second))),
            cut_metric_fft_l1=float(np.max(np.sum(np.abs(np.fft.fft(errors,axis=1)/n),axis=1))),
            cut_metric_c1_fft_l1=float(np.max(np.sum(np.abs(np.fft.fft(c1,axis=1)/n),axis=1))),
            physical_endpoint_bc_max=endpoint_bc,tail_converged=True,tail_shooting_residual=final['residual'],
            tail_packet=ref(final_packet),height_reference=ref(final_binding),
            height_reference_kind='actual_saved_physical_quintic_endpoint',
            scope='Actual frozen finite mean and complete original mean/nonmean physical endpoint jets; no continuous Cartesian seam or infinite closure inferred')
        write(out/'frozen-mean-seam.json',seam)
        metric_pass = bool(report['rows'] and all(model.finite(row['legacy_max_component_fft_l1'],1e-6)
            and model.finite(row['sample_operator_max'],1e-6) for row in report['rows']))
        accepted = bool(sol.success and model.finite(record['raw_return']['rms'],gates['tol'])
            and model.finite(defect,gates['bc_tol']) and model.finite(physical_bc,gates['physical_bc_tol'])
            and model.finite(endpoint_bc,gates['physical_bc_tol']) and metric_pass
            and model.finite(final['residual'],2e-9))
        record.update(status='audited_finite_original_support_actual_dn_candidate',
            finite_actual_dn_candidate_pass=accepted,tail_calls=tail.calls,tail_seam=seam,
            frozen_mean_seam_sha256=sha(out/'frozen-mean-seam.json'),
            final_physical_H=np.asarray(physical_H,float).tolist(),
            result=dict(original_nonlinear_DN_accepted=accepted,raw=ref(raw_file),
                physical=ref(out/'physical.npz'),actual_bc_max=defect,physical_bc_max=physical_bc,
                physical_endpoint_bc_max=endpoint_bc,tail_residual=final['residual'],
                metric_max=max(row['legacy_max_component_fft_l1'] for row in report['rows']),
                height_reference=str(final_binding),height_reference_sha256=sha(final_binding),
                full_height_record=str(final_packet),full_height_record_sha256=sha(final_packet),
                final_height_reference_kind='actual_saved_physical_quintic_endpoint',
                full_Cartesian_seam_paid=False,C2_convergence_proven=False,complete_surface=False))
        save()
        if accepted:
            gate = module('_fixed_actual_final_readback_gate',HERE/'qr_fixed_support_actual_acceptance.py')
            gate.accepted_actual_input(out/'run.json',repo=repo)
        event('actual_fixed_support_terminal',accepted=accepted,metric_pass=metric_pass,
              actual_bc=defect,physical_bc=physical_bc,physical_endpoint_bc=endpoint_bc)
        return 0 if accepted else 2
    except Exception as error:
        record.update(status='actual_fixed_support_stage_failed',error=repr(error),
            exception=traceback.format_exc().splitlines()[-32:],
            finite_actual_dn_candidate_pass=False,tail_calls=tail.calls if tail is not None else 0)
        save()
        event('actual_fixed_support_error',error=repr(error))
        return 2
    finally:
        done.set()
        if monitor is not None:
            monitor.join(timeout=2)
        if tail is not None:
            tail.close()


if __name__ == '__main__':
    raise SystemExit(main())
