#!/usr/bin/env python3
"""Resume the pinned q060 inner0 exactly at its actual-tail query.

No old restart, warmup or inner0 solve is performed. A new original worker
owns the accepted new-H response; the original nonlinear BC then decides
whether to export or continue outer1,...,7. Missing old diagnostics stay
missing. Only the independent resume entry and serialization hooks are new.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'

import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import time
from types import SimpleNamespace

import numpy as np
from scipy.interpolate import PPoly

from recovering_tail_client_v2 import (exact_equal,payload_sha,physical_solver_config,
    read_gzip,sha,validate_parameter_io_mapping,write_new_json)


PINNED={
    'entry_plan':'c1460e83e4816043e6f87bdb3aee6b5f98ec737de107fe42d5efc28ddd1fda44',
    'raw_inner':'67112318acde56cf1c797267b2069885e50567f4b5052db008acda64cf70d84d',
    'dn_anchor':'ec23c070f93692835d400a5f0eae60ba24669c862c1045e5184a465483877715',
    'accepted_tail':'2bbce1774e35c2c9936405b61ff66e8fc2db05968be8da12d1fb85a234a823bd',
}


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value);return value


def file_ref(path):
    return dict(path=str(Path(path).resolve()),sha256=sha(path))


def value_after(command,flag):
    if command.count(flag)!=1:raise ValueError('Missing/ambiguous original argument: '+flag)
    return command[command.index(flag)+1]


class ResumeContext:
    def __init__(self,args):
        self.args=args
        for key,digest in PINNED.items():
            if sha(getattr(args,key))!=digest:raise ValueError('The explicit original resume input changed: '+key)
        self.plan=json.loads(args.entry_plan.read_text())
        self.raw=read_gzip(args.raw_inner);self.anchor=json.loads(args.dn_anchor.read_text())
        self.accepted=read_gzip(args.accepted_tail)
        self.manifest=json.loads(args.owned_manifest.read_text())
        self.old_manifest=json.loads(Path(self.plan['owned_source_manifest']['path']).read_text())
        if sha(self.plan['owned_source_manifest']['path'])!=self.plan['owned_source_manifest']['sha256']:
            raise ValueError('Original owned source manifest changed')
        if (self.manifest['owned_topic']!=str(args.source_topic.resolve()) or
                self.manifest['reverse_patch_restores_original_bytes'] is not True or
                self.manifest['runtime_source_root_unchanged'] is not True or
                self.raw['source_sha256']!=self.manifest['original_coupler']['sha256']):
            raise ValueError('Resume source does not descend from the recorded exact inner source')
        self.sources={}
        for key in ('original_source_sha256','original_runtime_source_sha256',
                    'preparation_source_sha256','owned_source_sha256'):
            self.sources.update(self.old_manifest[key])
        for key in ('original_coupler','owned_coupler'):
            ref=self.manifest[key];self.sources[ref['path']]=ref['sha256']
        preparer=Path(__file__).with_name('prepare_saved_inner_resume_source.py')
        if sha(preparer)!=self.manifest['preparer_sha256']:raise ValueError('Resume preparer changed')
        self.sources[str(preparer.resolve())]=sha(preparer)
        self.sources[str(Path(__file__).resolve())]=sha(__file__)
        helper=Path(__file__).with_name('recovering_tail_client_v2.py')
        self.sources[str(helper.resolve())]=sha(helper)
        for ref in self.plan['inputs']:
            if sha(ref['path'])!=ref['sha256']:raise ValueError('Original input changed: '+ref['path'])
        for name,ref in self.raw['inputs'].items():
            if sha(ref['path'])!=ref['sha256']:raise ValueError('Saved inner input changed: '+name)
        if (self.raw['solver_success'] is not False or self.raw['projected_solver_success'] is not True or
                self.raw['actual_tail_accepted'] is not False or self.raw['outer']!=0 or
                self.raw['stage']!='before_actual_tail_query' or self.raw['core_round_record'] is not None):
            raise ValueError('Only the recorded successful projected inner0 is eligible')
        if (self.anchor['outer']!=0 or self.anchor['actual_tail_accepted'] is not False or
                self.anchor['raw_inner']['sha256']!=sha(args.raw_inner) or
                not exact_equal(self.anchor['candidate_cut_height'],self.raw['candidate_cut_height'])):
            raise ValueError('Original raw inner and exact affine anchor differ')
        old_ref=self.anchor['affine_actual_tail'];old=read_gzip(old_ref['path'])
        if (sha(old_ref['path'])!=old_ref['sha256'] or
                payload_sha(old['response'])!=old_ref['response_sha256'] or
                not exact_equal(old['request'],old_ref['request']) or
                payload_sha(old['config'])!=old_ref['configuration_sha256'] or
                old['response'].get('converged') is not True or not old['response']['residual']<2e-9):
            raise ValueError('Recorded old affine-DN anchor is not its original accepted response')
        for filename,digest in old_ref['runtime_source_sha256'].items():
            if sha(filename)!=digest:raise ValueError('Original affine runtime changed')
        if (self.accepted['response'].get('converged') is not True or
                not self.accepted['response']['residual']<2e-9 or
                not exact_equal(self.accepted['request'],dict(height=self.raw['candidate_cut_height'],jacobian=True,audit=True)) or
                not exact_equal(self.accepted['response']['checkpoint']['cutHeight'],self.raw['candidate_cut_height']) or
                self.accepted['response'].get('audit') is None):
            raise ValueError('A genuine same-new-H original-worker/Jacobian/audit result is required')
        J=np.asarray(self.accepted['response']['heightJetJacobian'],float)
        if J.size!=208 or not np.all(np.isfinite(J)):raise ValueError('Incomplete accepted height-jet Jacobian')
        self.original_config=json.loads(Path(value_after(self.plan['new_command'],'--tail-config')).read_text())
        if not exact_equal(physical_solver_config(self.original_config),physical_solver_config(self.accepted['config'])):
            raise ValueError('Accepted new-H tail changed the original physical/discrete/solver configuration')
        self.new_config=copy.deepcopy(self.accepted['config'])
        self.new_config['initialCheckpoint']=str(args.accepted_tail.resolve())
        self.new_config['traceFile']=str(args.out_prefix.with_name(args.out_prefix.name+'-worker.jsonl').resolve())
        if set(k for k in set(self.new_config)|set(self.accepted['config'])
               if not exact_equal(self.new_config.get(k),self.accepted['config'].get(k)))-{'initialCheckpoint','traceFile'}:
            raise AssertionError('Only initializer/trace metadata may change')
        if self.new_config.get('designInitialCheckpoint') or self.new_config.get('secantCheckpoint'):
            raise ValueError('This exact continuation uses the one native initializer only')
        self.config_file=args.out_prefix.with_name(args.out_prefix.name+'-config.json').resolve()
        write_new_json(self.config_file,self.new_config)
        self.expected_native_sources=dict(self.accepted['source_sha256'])
        self.restored=None;self.driver_started=False;self.driver_log=[]
        self.check_sources()

    def check_sources(self):
        for file,digest in self.sources.items():
            if sha(file)!=digest:raise ValueError('Frozen resume/original source changed: '+file)

    def provenance(self):
        return dict(scope=__doc__,entry_plan=file_ref(self.args.entry_plan),
            raw_inner=file_ref(self.args.raw_inner),dn_anchor=file_ref(self.args.dn_anchor),
            accepted_initializer=file_ref(self.args.accepted_tail),
            original_outer_resumed=0,remaining_original_outer_indices=list(range(1,8)),
            prior_native_calls=3,current_client_calls_start_at_zero=True,
            original_warmup_invoked=False,original_restart_invoked=False,original_inner0_recomputed=False,
            old_message_and_interval_rms_not_saved=True,
            cubic_reconstruction_scope='Literal saved coefficients/breaks/axis; evaluations restricted to saved interval; old extrapolation attribute was not saved.')

    def event(self,event,**values):
        row=dict(event=event,**values);self.driver_log.append(row)
        with self.args.out_prefix.with_name(self.args.out_prefix.name+'-resume-events.jsonl').open('a') as stream:
            stream.write(json.dumps(row,separators=(',',':'),allow_nan=False)+'\n')
        print(json.dumps(row,allow_nan=False),flush=True)

    def restore_inputs(self,o,a):
        if self.restored is not None:raise ValueError('The saved inner may be restored exactly once')
        if (not a.lagged_tail or a.fixed or a.preserve_restart_mesh or a.warmup_scales!=[] or
                a.modes!=8 or a.angular!=256 or a.max_nodes!=6000 or a.tol!=1e-6 or
                a.bc_tol!=1e-7 or a.physical_bc_tol!=2e-9 or a.amplitude!=.06 or a.warp_reference!=.06):
            raise ValueError('Original q060 options and empty warmup list are required')
        r=self.raw;raw=r['raw_inner_solution']
        x=np.asarray(raw['mesh'],float);y=np.asarray(raw['values'],float);p=np.asarray(r['parameters'],float)
        breaks=np.asarray(raw['cubic_breaks'],float);coeff=np.asarray(raw['cubic_coefficients'],float)
        if (x.ndim!=1 or not np.all(np.diff(x)>0) or y.shape!=(o.n,len(x)) or
                not np.array_equal(x,breaks) or coeff.shape!=(4,len(x)-1,o.n) or
                not all(np.all(np.isfinite(v)) for v in (x,y,p,coeff)) or
                not exact_equal(o.pscale.tolist(),r['central_correction_scales']) or
                not exact_equal(float(o.q),r['gauge_amplitude'])):
            raise ValueError('Saved original chart/state/parameter arrays do not match the BVP')
        if (not exact_equal(json.loads(a.profile.read_text()),r['input_profile']) or
                not exact_equal(json.loads(a.chart.read_text()),r['chart']) or
                not exact_equal(o.port['parameters'],r['physical_tail_parameters']) or
                not exact_equal(o.port['cut'],r['physical_tail_cut'])):
            raise ValueError('Original profile/chart/physical port identity changed')
        if not exact_equal(r['candidate_frozen_profile'],{**r['input_profile'],'delta':r['input_profile']['delta']+float(p[0])}):
            raise ValueError('Saved physical-profile parameter convention changed')
        candidate=o.bridge.sigma*o.q*y[o.iz:,-1]
        if not exact_equal(candidate.tolist(),r['candidate_cut_height']):
            raise ValueError('The exact original state no longer yields its recorded new H')
        maximum=float(r['max_rms_collocation_residual'])
        if not math.isfinite(maximum) or maximum>a.tol:raise ValueError('The recorded projected inner did not meet its original RMS tolerance')
        cubic=PPoly.construct_fast(coeff,breaks,extrapolate=False,axis=int(raw['cubic_axis']))
        self.restored=SimpleNamespace(x=x,y=y,p=p,sol=cubic,success=True,recorded_raw_max_rms=maximum)
        if hasattr(self.restored,'message') or hasattr(self.restored,'rms_residuals'):
            raise AssertionError('Missing original diagnostics must not be synthesized')
        self.event('saved_original_inner_restored',raw_inner_sha256=sha(self.args.raw_inner),
                   nodes=len(x),candidate_height=candidate.tolist(),recorded_max_rms=maximum,
                   missing_message=True,missing_interval_rms=True,original_inner_solve_invoked=False)
        return x,y,p,dict(method='literal_saved_original_inner',**self.provenance())

    def check_reload(self,tail,height):
        cp=self.accepted['response']['checkpoint']
        transition=validate_parameter_io_mapping(cp['parameters'],tail.ready['parameters'],
                                                 self.accepted['config'],self.new_config)
        if tail.sources!=self.expected_native_sources:raise ValueError('Native worker sources changed')
        code="""const fs=require('fs');const d=JSON.parse(fs.readFileSync(0,'utf8'));
if(!Object.is(d.height[0]/d.cutHeight[0],1)||!d.height.every((v,j)=>Object.is(v,d.cutHeight[j])))
 throw Error('Changed physical height');
if(!d.height.every((v,j)=>Object.is(v/d.radius**4-d.firstState[j],0)))
 throw Error('Nonzero original reload boundary correction');
console.log(JSON.stringify({ratio:1,zero_boundary_correction:true,radius:d.radius}));"""
        completed=subprocess.run(['node','-e',code],input=json.dumps(dict(height=height.tolist(),
            cutHeight=cp['cutHeight'],firstState=cp['states'][0],radius=tail.cut['radius']),allow_nan=False),
            text=True,capture_output=True,check=True)
        self.event('resume_original_worker_ready',parameter_metadata_transition=transition,
                   reload_arithmetic=json.loads(completed.stdout),native_sources_unchanged=True)

    def solve_after_saved_inner(self,o,tail,x,y,par,a):
        if self.driver_started or self.restored is None:raise ValueError('Invalid or repeated exact resume')
        self.driver_started=True
        if not (x is self.restored.x and y is self.restored.y and par is self.restored.p):
            raise ValueError('Main changed a restored original state array')
        if o.tail is not tail:raise ValueError('Post-inner control flow must already use the actual tail')
        c=self.coupler
        options=dict(tol=a.tol,bc_tol=a.bc_tol,max_nodes=a.max_nodes,fun_jac=o.fun_jac,bc_jac=o.bc_jac)
        sol=self.restored;candidate=o.bridge.sigma*o.q*sol.y[o.iz:,-1]
        self.check_reload(tail,candidate)
        # Resume the actual query itself. Never import an accepted JSON response into cache.
        actual=tail.solve(candidate,jacobian=True,audit=True)
        J=np.asarray(actual['heightJetJacobian'],float)
        if (actual.get('converged') is not True or not actual['residual']<2e-9 or
                J.size!=208 or not np.all(np.isfinite(J)) or actual.get('audit') is None):
            raise ValueError('The new original worker did not genuinely accept the exact new H')
        if o.tail is not tail:raise AssertionError('The original post-tail BC must use the actual client')
        defect=float(np.max(np.abs(o.bc(sol.y[:,0],sol.y[:,-1],sol.p))))
        row=dict(outer=0,inner_success=True,actual_boundary_residual=defect,
                 actual_tail_residual=actual['residual'],tail_calls=tail.calls)
        history=[row];print(json.dumps(dict(event='actual_outer_check',**row)),flush=True)
        self.event('saved_inner_original_post_tail_checked',**row,actual_tail_object=True,
                   old_affine_response_used_as_actual=False,prior_native_calls=3)
        if defect<=a.bc_tol:return sol,history
        x,y,par=sol.x,sol.y,sol.p;height=candidate;response=actual
        # This is the unchanged original inner/actual-tail body, with only the
        # already-used outer0 removed from the original range(8) budget.
        for outer in range(1,8):
            o.tail=c.AffineTailForInnerBVP(height,response,o.M)
            try:sol=c.solve_bvp(o.fun,o.bc,x,y,par,**options)
            finally:o.tail=tail
            if not sol.success:
                history.append(dict(outer=outer,inner_success=False,message=sol.message))
                return sol,history
            candidate=o.bridge.sigma*o.q*sol.y[o.iz:,-1]
            c.record_inner_prefix_debug(o,sol,a,outer,candidate)
            c.client.record_inner_dn_anchor(a,outer,tail,height,response,candidate)
            actual=tail.solve(candidate,jacobian=True,audit=False)
            defect=float(np.max(np.abs(o.bc(sol.y[:,0],sol.y[:,-1],sol.p))))
            row=dict(outer=outer,inner_success=True,actual_boundary_residual=defect,
                     actual_tail_residual=actual['residual'],tail_calls=tail.calls)
            history.append(row);print(json.dumps(dict(event='actual_outer_check',**row)),flush=True)
            if defect<=a.bc_tol:return sol,history
            x,y,par=sol.x,sol.y,sol.p;height=candidate;response=actual
        raise FloatingPointError('Outer true-DN boundary residual did not reach the original tolerance')

    def main_arguments(self):
        old=self.plan['new_command'][2:];rest=[];i=0
        wrapper_flags={'--source-topic','--short-bridge','--restart-port'}
        while i<len(old):
            token=old[i]
            if token in wrapper_flags:i+=2;continue
            if token=='--warmup-scales':
                rest.append(token);i+=1
                while i<len(old) and not old[i].startswith('--'):i+=1
                continue
            if token in ('--tail-config','--out-prefix'):
                rest.extend((token,str(self.config_file if token=='--tail-config' else self.args.out_prefix.resolve())))
                i+=2;continue
            rest.append(token);i+=1
        return ['--source-root',str((self.args.source_topic/'repro/source-root').resolve()),*rest]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for flag in ('entry-plan','raw-inner','dn-anchor','accepted-tail','source-topic','owned-manifest','out-prefix'):
        parser.add_argument('--'+flag,type=Path,required=True)
    args=parser.parse_args()
    args.out_prefix=args.out_prefix.resolve();args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    entry_file=args.out_prefix.with_name(args.out_prefix.name+'-resume-entry.json')
    terminal_file=args.out_prefix.with_name(args.out_prefix.name+'-resume-terminal.json')
    if entry_file.exists() or terminal_file.exists():raise FileExistsError('Use a new resume output prefix')
    context=ResumeContext(args)
    env=context.plan['environment']
    for key,value in env.items():os.environ[key]=value
    source=args.source_topic.resolve()
    c=module('q060_exact_saved_inner_coupler',source/'scripts/db6f-prefix-coupled.py')
    flat=module('q060_exact_saved_inner_flat',source/'scripts/db6f-prefix-flat-profile.py');flat.install(c.adaptive)
    short_path=Path(value_after(context.plan['new_command'],'--short-bridge'))
    short=module('q060_exact_saved_inner_short',short_path)
    install_original=c.adaptive.old.install_source
    def install(root):install_original(root);short.install()
    c.adaptive.old.install_source=install
    c.RESUME_CONTEXT=context;context.coupler=c
    c.solve_with_actual_tail=context.solve_after_saved_inner
    entry=dict(scope=__doc__,command=[sys.executable,*sys.argv],source_sha256=context.sources,
        provenance=context.provenance(),source_manifest=file_ref(args.owned_manifest),
        actual_initializer=file_ref(args.accepted_tail),tail_configuration=file_ref(context.config_file),
        full_physical_height=context.raw['candidate_cut_height'],original_main_arguments=context.main_arguments(),
        environment=env,maximum_total_outer_indices=list(range(8)),warmup_scales=[],
        mathematical_function_scope='Original TailMixin, adaptive BVP, solve_bvp, BC, C2 interpolation and full metric/seam audit; only restore/remaining-outer control flow and missing-diagnostic serialization differ.')
    write_new_json(entry_file,entry)
    context.event('exact_saved_inner_entry',entry=str(entry_file),entry_sha256=sha(entry_file),
                  original_restart_or_warmup_invoked=False)
    old_argv=sys.argv[:];started=time.monotonic()
    terminal=dict(scope='Observed return of the exact saved-inner runner; original summary determines solver success.',
                  entry=file_ref(entry_file),original_main_returned=False)
    try:
        sys.argv=[str(Path(__file__).resolve()),*context.main_arguments()]
        c.main();terminal['original_main_returned']=True
    except Exception as error:
        terminal['error']=repr(error)
        raise
    finally:
        sys.argv=old_argv;context.check_sources()
        summary_file=args.out_prefix.with_name(args.out_prefix.name+'-summary.json')
        if summary_file.is_file():
            summary=json.loads(summary_file.read_text());terminal['original_summary']=file_ref(summary_file)
            terminal['original_solver_success']=summary.get('solver_success')
            terminal['original_error']=summary.get('error')
        terminal['seconds']=time.monotonic()-started
        write_new_json(terminal_file,terminal)
        print(json.dumps(dict(event='exact_saved_inner_terminal',**terminal)),flush=True)


if __name__=='__main__':main()
