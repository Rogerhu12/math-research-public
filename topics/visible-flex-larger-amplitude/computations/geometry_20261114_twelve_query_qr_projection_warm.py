#!/usr/bin/env python3
"""Twelve-query warm with a complete square-root-H alternative to the C baseline.

The baseline is the frozen actual37 continuation: complete twelve-query B,
fixed-support C projection with its outside offset, and original whole-vector
repair/selection. The H candidate retains every original exact coordinate.
Only the full-H helper's inverse slot is replaced by one delayed complete
QR factor and actual original-H readbacks. No old PCG retry is performed.
The actual same-model C/H comparison and all seventeen nonlinear trials
remain those of the frozen original sources. Every saved field is a warm.
"""
from __future__ import annotations

import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'

import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path
import sys
import textwrap
import time
import traceback

import numpy as np

import geometry_20261114_twelve_query_projection_warm as baseline
import geometry_20261114_full_metric_projection_warm as selection_source
import geometry_20261114_full_metric_inequality_correction as correction
import exact_20261114_regularized_block_qr as square_root


HERE=Path(__file__).resolve().parent
engine=baseline.engine
original=engine.baseline.original
SCHEMA='exact-constraint-twelve-query-complete-QR-H-alternative-warm-v1'
BASELINE_SCHEMA=baseline.SCHEMA
INITIAL_PARENT_SCHEMA=baseline.PARENT_SCHEMA
ACTUAL37_WARM_SHA='dd83748341c8d6172096fc644361018be7b29d856de621a0b333104d20aafdb8'
ACTUAL37_STATUS_SHA='37e70ad5a3c9ef828d93bcbf371b3a107e3890026731d7944d98e370987d29e0'
BASELINE_SOURCE_NAMES=baseline.SOURCE_NAMES
SOURCE_NAMES=tuple(dict.fromkeys((Path(__file__).name,Path(square_root.__file__).name,
    Path(selection_source.__file__).name,Path(correction.__file__).name)+BASELINE_SOURCE_NAMES))
FROZEN={
    'geometry_20261114_twelve_query_projection_warm.py':'10ed25405930f3775d8fb88f007aa50be4a53f4b3421904be959f1890ed67477',
    'geometry_20261114_twelve_query_domain_operator.py':'6a428d2f8412659cbd318321aa992c3b4565ff41177131a9cc9d268c6fbb7b1f',
    'geometry_20261114_fixed_support_halfspaces.py':'0c5573ea26d2c69c1a22595e00de9e41b38981793b88f4f52086d7713d111f68',
    'geometry_20261114_full_metric_projection_warm.py':'8fb6411e7b876713725a80c2dbe9e322cc277001b0692ccc59e0edd59ec4e8b0',
    'geometry_20261114_full_metric_inequality_correction.py':'d5e9432e979859ed7d5277452ac058eb93e99da1cae7f96f700f15d7359d919c',
    'exact_20261114_regularized_block_qr.py':'596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722',
    'geometry_20261114_constrained_collocation.py':'70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8',
}
ORIGINAL_CHOOSE=engine.choose_feasible_descent
ORIGINAL_LINEAR=engine.CompleteLinearization
ORIGINAL_SUPPORT=baseline.support.fixed_support_projection
ORIGINAL_PCG=correction._pcg


def _same(a,b,label):
    if a!=b:
        raise ValueError('One complete original finite model is required: '+label)


def _source_guard():
    for name,digest in FROZEN.items():
        _same(original.sha(HERE/name),digest,'frozen source '+name)
    if correction.choose_feasible_descent is not ORIGINAL_CHOOSE or selection_source.ORIGINAL_CHOOSE is not ORIGINAL_CHOOSE:
        raise ValueError('Capture the unchanged selector before installing the new wrapper')


def _selector_source():
    """Read one source-bound nested function; retain its complete AST/body.

    No producer main is run to obtain this closure. No equation or gate
    in the actual full-H/C comparator is translated or reimplemented.
    """
    path=Path(selection_source.__file__)
    _same(original.sha(path),FROZEN[path.name],'same-model comparator source')
    source=path.read_text()
    tree=ast.parse(source,filename=str(path))
    mains=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name=='main']
    if len(mains)!=1:
        raise ValueError('Expected one frozen comparator main')
    nodes=[node for node in mains[0].body if isinstance(node,ast.FunctionDef) and node.name=='choose']
    if len(nodes)!=1:
        raise ValueError('Expected the unique complete frozen choose function')
    node=nodes[0]
    segment=textwrap.dedent(''.join(source.splitlines(keepends=True)[node.lineno-1:node.end_lineno]))
    extracted=ast.parse(segment).body[0]
    actual_ast=ast.dump(extracted,include_attributes=False)
    _same(actual_ast,ast.dump(node,include_attributes=False),'unchanged complete comparator AST')
    factory=('def _bind(captured, options, args, entry_identity, previous_write):\n'
             '    selector_calls = 0\n'+textwrap.indent(segment,'    ')+'\n    return choose\n')
    module=ast.parse(factory)
    nested=[item for item in module.body[0].body if isinstance(item,ast.FunctionDef)]
    _same(ast.dump(nested[0],include_attributes=False),actual_ast,'compiled closure complete AST')
    metadata=dict(source_file=path.name,source_sha256=FROZEN[path.name],
        function='main.choose',verbatim_function_text_sha256=hashlib.sha256(segment.encode()).hexdigest(),
        complete_function_AST_sha256=hashlib.sha256(actual_ast.encode()).hexdigest(),
        complete_function_body_retained=True,source_main_not_executed=True,
        original_C_full_model_comparison_R265_R267_and_archive_retained=True)
    return factory,metadata


def _bind_selector(factory,captured,options,args,entry_identity,write):
    namespace=dict(correction=correction,np=np,copy=copy,time=time,traceback=traceback,json=json,
        ORIGINAL_CHOOSE=ORIGINAL_CHOOSE,ArrayArchive=selection_source.ArrayArchive,
        original=original,engine=engine)
    exec(compile(factory,str(Path(selection_source.__file__))+'::source-bound-choose','exec'),namespace)
    return namespace['_bind'](captured,options,args,entry_identity,write)


class _QRInverseSlot:
    """Replacement only for the frozen helper's two _pcg call sites."""
    def __init__(self,live,captured,args,options,entry_identity,write):
        self.live,self.captured=live,captured
        self.args,self.options,self.entry_identity,self.write=args,options,entry_identity,write
        self.factor=None
        self.model=None
        self.failed_reason=None
        self.factor_attempts=0
        self.calls=[]
        self.extra_reference_A=0
        self.extra_reference_AT=0
        self.completed_reference_A=0
        self.completed_reference_AT=0
        self.actual_complete_H_readbacks=0
        # The original engine first requires an empty output directory.
        # Allocate no file or subdirectory before its initial intent write.
        self.archive=None

    def _archive(self):
        if self.archive is None:
            self.archive=selection_source.ArrayArchive(self.args.out/'block-qr-inverse-arrays')
        return self.archive

    def summary(self):
        factor_report=None if self.factor is None else self.factor.report
        return dict(schema='complete-QR-original-H-inverse-slot-accounting-v1',
            entry=self.entry_identity,factor_attempts=self.factor_attempts,
            old_PCG_called=False,no_second_complete_linearization=True,
            complete_linearization_constructor_calls=self.live.get('constructor_calls',0),
            original_operator_constructions=self.live.get('operator_calls',0),
            original_helper_complete_H_readbacks=self.actual_complete_H_readbacks,
            additional_frozen_reference_A_calls=self.extra_reference_A,
            additional_frozen_reference_AT_calls=self.extra_reference_AT,
            completed_frozen_reference_A_calls=self.completed_reference_A,
            completed_frozen_reference_AT_calls=self.completed_reference_AT,
            action_counts_are_invocations_including_calls_that_raise=True,
            action_count_scope=('The fixed-H helper and its additional frozen-reference readbacks; '
                'raw LSMR, baseline C, outer selector and earlier implementation checks are separate'),
            original_helper_action_counts=(None if self.model is None else dict(self.model.counts)),
            total_original_and_reference_A_calls=(None if self.model is None else self.model.counts['A']+self.extra_reference_A),
            total_original_and_reference_AT_calls=(None if self.model is None else self.model.counts['AT']+self.extra_reference_AT),
            QR_factorization_and_R_triangular_work_are_additional_not_1200_H_products=True,
            QR_full_block_budget=dict(maximum_factorizations=1,physical_blocks=698,global_border=112,
                maximum_active_rows=self.options.full_h_max_active,
                helper_seconds=self.options.full_h_budget_seconds,
                original_trial_reserve_seconds=self.options.full_h_trial_reserve_seconds),
            fixed_support_applies_only_to_baseline_C_projection=True,
            H_candidates_retain_all_original_coordinates=True,
            failed_reason=self.failed_reason,calls=self.calls,factor=factor_report,
            arrays=dict(files=[] if self.archive is None else self.archive.files,large_arrays_artifact_only=True),
            nonlinear_accepted=False,QP_optimality_claimed=False)

    def preserve(self):
        if not self.live.get('output_started',False):
            return
        self.write(self.args.out/'block-qr-inverse-accounting.json',self.summary())
        self.write(self.args.out/'block-qr-inverse-array-manifest.json',dict(
            schema='complete-QR-inverse-actual-array-chunks-v1',entry=self.entry_identity,
            files=[] if self.archive is None else self.archive.files,
            all_actual_returned_RHS_candidate_and_residual_arrays_retained=True,
            large_arrays_artifact_only=True,no_publication_limit_is_a_numerical_gate=True))

    def _unavailable(self,model,initial,label,reason,h_before,**details):
        # In the frozen helper the center initial is exactly z0. A row
        # initial is zero, but started=False makes the helper break before
        # adding that row or its zero vector. Neither is an exact solution.
        value=np.array(initial,dtype=np.float64,copy=True)
        report=dict(label=label,started=False,reason=reason,
            backend='complete-square-root-QR',old_PCG_called=False,
            original_residual_verified=False,converged=False,
            H_products=model.counts['H']-h_before,history=[],
            supplied_initial_returned_unchanged=correction.identity(value)==correction.identity(initial),
            returned_initial=correction.identity(value),
            no_exact_center_or_zero_row_inverse_claim=True,**details)
        self.calls.append(report)
        self.preserve()
        return value,report

    def __call__(self,model,rhs,initial,label,*,max_iterations,relative_tolerance,recompute_every=8):
        request_started=time.monotonic()
        phase='validate-one-fixed-model'
        h_before=model.counts['H']
        if self.model is None:
            self.model=model
        elif self.model is not model:
            raise ValueError('Never reuse one QR factor across two full-H models')
        _same(self.live.get('constructor_calls'),1,'unique CompleteLinearization construction')
        if self.live.get('A') is not model.A or self.live.get('linear') is None:
            raise ValueError('The inverse helper must consume the same live original A object')
        _same(correction.identity(model.C),correction.identity(self.captured['C']),'unchanged original C')
        if model.domain is not self.captured['domain']:
            raise ValueError('The complete B object changed inside the fixed model')
        _same(model.damping,self.live['chosen_damping'],'unchanged complete model damping')
        if self.failed_reason is not None:
            return self._unavailable(model,initial,label,'QR-unavailable-after-preserved-failure',h_before,
                                     failure=self.failed_reason)
        if not model.work_available(1):
            return self._unavailable(model,initial,label,'no-budget-for-original-H-readback',h_before)
        try:
            if self.factor is None:
                phase='initialize-one-complete-QR-factor'
                self.factor_attempts+=1
                _same(self.factor_attempts,1,'one delayed factorization')
                storage=(self.args.out/'block-qr-factor') if self.options.qr_store_factors else None
                column=self.captured['C'] if self.options.qr_column_preconditioner=='original-C' else None
                self.factor=square_root.RegularizedBlockQR(
                    self.live['linear'],self.live['weights'],model.damping,
                    deadline=model.deadline,original_operator=model.proxy_A,
                    column_preconditioner=column,storage_directory=storage,
                    input_identity=dict(entry=self.entry_identity,original_full_H_model=model.fixed_identity,
                        live_model=self.live['public_binding']),
                    progress=lambda row:print(json.dumps({**row,'entry_event':'twelve_query_full_QR_progress'}),flush=True))
                # Count even a reference call that raises before the
                # frozen solve can return its success report. Forward the
                # original action verbatim; do not reconstruct another J.
                reference=self.factor.reference_A
                owner=self
                class CountedReference:
                    shape=reference.shape
                    dtype=reference.dtype
                    def matvec(self,value):
                        owner.extra_reference_A+=1
                        result=reference.matvec(value)
                        owner.completed_reference_A+=1
                        return result
                    def rmatvec(self,value):
                        owner.extra_reference_AT+=1
                        result=reference.rmatvec(value)
                        owner.completed_reference_AT+=1
                        return result
                self.factor.reference_A=CountedReference()
                self.preserve()
                phase='factorize-complete-regularized-block-system'
                self.factor.factorize()
                self.preserve()
            if not model.work_available(1):
                return self._unavailable(model,initial,label,'no-solve-budget-after-completed-QR',h_before)
            counts_before=dict(model.counts)
            phase='solve-and-read-original-H-and-frozen-reference'
            reply=self.factor.solve_H(rhs,label=label,relative_tolerance=relative_tolerance)
            # The factor used model.proxy_A for this complete original H
            # readback, so A/AT are already counted by the frozen helper.
            # Charge its one completed H readback explicitly as well.
            model.counts['H']+=1
            self.actual_complete_H_readbacks+=1
            report=reply['report']
            arrays=self._archive().convert(dict(rhs=np.asarray(rhs),candidate=reply['candidate'],
                original_complete_H_residual=reply['original_residual'],
                factor_normal_residual=reply['factor_normal_residual']))
            path=self.args.out/f'block-qr-inverse-{len(self.calls):03d}.json'
            self.write(path,dict(schema='complete-QR-original-H-inverse-actual-call-v1',
                entry=self.entry_identity,report=report,arrays=arrays,
                original_helper_counts_before=counts_before,original_helper_counts_after=dict(model.counts)))
            diagnostic=dict(label=label,started=True,reason='complete-QR-candidate-with-original-full-H-readback',
                backend='complete-square-root-QR',old_PCG_called=False,
                original_residual_verified=True,original_residual_L2=report['original_residual_L2'],
                original_residual_Linf=report['original_residual_Linf'],rhs_L2=report['rhs_L2'],
                tolerance=float(relative_tolerance)*report['rhs_L2'],
                converged=report['original_residual_within_requested_tolerance'],
                H_products=model.counts['H']-h_before,history=[],
                old_PCG_maximum_iterations_argument_not_used=int(max_iterations),
                old_PCG_recompute_every_argument_not_used=int(recompute_every),
                complete_QR_original_readback_file=dict(file=path.name,sha256=original.sha(path)),
                solution=correction.identity(reply['candidate']),
                actual_full_residual=correction.identity(reply['original_residual']),
                finite_candidate_may_be_used_only_as_a_full_model_basis_vector=True,
                relative_tolerance=float(relative_tolerance),
                inverse_slot_seconds_including_initialization_and_factorization=time.monotonic()-request_started,
                seconds=report['seconds'])
            self.calls.append(diagnostic)
            self.preserve()
            return reply['candidate'],diagnostic
        except Exception as error:
            self.failed_reason=dict(error=repr(error),traceback=traceback.format_exc(),phase=phase,
                inverse_slot_seconds_until_failure=time.monotonic()-request_started,
                partial_factor_report=(None if self.factor is None else self.factor.report),
                numerical_inverse_failure_is_not_a_scientific_failure=True,
                original_C_candidate_and_existing_actual_full_H_basis_retained=True,
                old_PCG_retry_performed=False)
            if self.factor is not None:
                try:
                    self.factor.close()
                except Exception as closing_error:
                    self.failed_reason['factor_close_error']=repr(closing_error)
            return self._unavailable(model,initial,label,'preserved-QR-failure-no-PCG-retry',h_before,
                                     failure=self.failed_reason)

    def close(self):
        if self.factor is not None:
            self.factor.close()
        self.preserve()


def main():
    square_root.require_actions()
    _source_guard()
    factory,selector_identity=_selector_source()
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--full-h-budget-seconds',type=float,required=True)
    parser.add_argument('--full-h-trial-reserve-seconds',type=float,required=True)
    parser.add_argument('--full-h-max-active',type=int,default=32)
    parser.add_argument('--full-h-max-products',type=int,default=1200)
    parser.add_argument('--full-h-inner-iterations',type=int,default=64)
    parser.add_argument('--full-h-inner-relative-tolerance',type=float,default=1e-8)
    parser.add_argument('--full-h-dual-sweeps',type=int,default=200)
    parser.add_argument('--qr-column-preconditioner',choices=('none','original-C'),default='none')
    parser.add_argument('--qr-store-factors',action='store_true')
    options,remaining=parser.parse_known_args()
    if (not np.isfinite(options.full_h_budget_seconds) or options.full_h_budget_seconds<=0
            or not np.isfinite(options.full_h_trial_reserve_seconds) or options.full_h_trial_reserve_seconds<0
            or not 0<=options.full_h_max_active<=32 or options.full_h_max_products<1
            or not 1<=options.full_h_inner_iterations<=200
            or not np.isfinite(options.full_h_inner_relative_tolerance) or options.full_h_inner_relative_tolerance<=0
            or not 1<=options.full_h_dual_sweeps<=1000):
        raise ValueError('Retain explicit finite full-H and original-trial reserve budgets')
    binding=argparse.ArgumentParser(add_help=False)
    binding.add_argument('--resume',type=Path,required=True)
    binding.add_argument('--expected-resume-sha',required=True)
    binding.add_argument('--parent-status',type=Path,required=True)
    binding.add_argument('--expected-parent-status-sha',required=True)
    binding.add_argument('--out',type=Path,required=True)
    args,_=binding.parse_known_args(remaining)
    _same(original.sha(args.resume),args.expected_resume_sha,'declared actual parent warm')
    _same(original.sha(args.parent_status),args.expected_parent_status_sha,'declared actual parent status')
    parent_status=original.read(args.parent_status)
    parent_schema=parent_status.get('schema')
    if parent_schema==INITIAL_PARENT_SCHEMA:
        _same(args.expected_resume_sha,ACTUAL37_WARM_SHA,'initial actual37 warm')
        _same(args.expected_parent_status_sha,ACTUAL37_STATUS_SHA,'initial actual37 status')
    elif parent_schema!=SCHEMA:
        raise ValueError('This first QR entry consumes actual37 or its own later actual same-schema warm; no future parent is invented')
    _same(parent_status.get('latest_warm_file'),args.resume.name,'actual parent warm basename')
    entry_identity=dict(schema=SCHEMA,entry_source_sha256=original.sha(__file__),
        frozen_dependencies={name:original.sha(HERE/name) for name in FROZEN},
        initial_actual_parent_warm_sha256=ACTUAL37_WARM_SHA,
        initial_actual_parent_status_sha256=ACTUAL37_STATUS_SHA,
        actual_parent_warm_sha256=args.expected_resume_sha,
        actual_parent_status_sha256=args.expected_parent_status_sha,
        actual_parent_schema=parent_schema,source_bound_same_model_selector=selector_identity,
        query_specs=[dict(q) for q in baseline.domain.QUERY_SPECS],
        selected_angle_row_count=len(baseline.domain.QUERY_SPECS)*2048,
        baseline_C_projection_only=dict(source_sha256=FROZEN[Path(baseline.support.__file__).name],
            support_nodes=list(baseline.support.FIXED_PHYSICAL_NODES),support_dimension=4059,
            complete_B_local_dimension=4397,outside_offset='c+B_out*z0_out',
            final_outside_direction_not_claimed_fixed=True),
        H_candidate_support='all 236036 original exact coordinates, including node470/core/global p',
        inverse_backend='one delayed complete [A;lambda I] square-root block QR',
        old_PCG_retry_performed=False,one_original_CompleteLinearization_only=True,
        QR_work_is_additional_to_original_H_action_budget=True,
        QR_column_preconditioner=options.qr_column_preconditioner,
        QR_large_factors_saved_only_as_optional_artifact=bool(options.qr_store_factors),
        full_H_budget_seconds=options.full_h_budget_seconds,
        original_trial_reserve_seconds=options.full_h_trial_reserve_seconds,
        original_same_f_C_comparison_R265_R267_and_seventeen_trials_retained=True,
        original_midpoint_observer_and_affine_Rphi_FD_scope_retained=True,
        all_original_parent_producer_subtrees_preserved=True,
        nonlinear_native_solved=False,full_BVP_accepted=False)
    captured={}
    live=dict(constructor_calls=0,operator_calls=0)
    raw_write=engine.write

    def current_identity(value):
        if not isinstance(value,dict):
            return
        value['twelve_query_QR_entry']=entry_identity
        value['full_H_inverse_backend']='complete-square-root-QR; no old-PCG retry'
        if 'projection_metric' in value:
            value.setdefault('baseline_C_projection_metric',value['projection_metric'])
            value['projection_metric']='fixed-support C baseline plus complete-global H alternative; actual same full f comparison'
        if 'direction_selection' in value:
            value.setdefault('baseline_C_direction_selection',value['direction_selection'])
            value['direction_selection']='actual same full f comparison of baseline C and complete-global H alternatives; original nonlinear trials'
        for key in ('projection_correction_support_physical_nodes','projection_effective_offset',
                    'projection_outside_raw_preserved_only_before_full_vector_radial'):
            if key in value:
                value['baseline_C_'+key]=value.pop(key)
        value['fixed_support_scope']='baseline C projection only; full-H candidate is global'
        if isinstance(value.get('twelve_query_projection_entry'),dict):
            value['twelve_query_projection_entry']['fixed_support_description_applies_only_to_baseline_C']=True
            value['twelve_query_projection_entry']['complete_global_H_alternative_is_declared_by_twelve_query_QR_entry']=True

    def write(path,value):
        # The baseline writer supplies a converted current object. Only
        # current identity containers are annotated, never resume_producer.
        if isinstance(value,dict):
            if Path(path).name=='optimization-intent.json':
                live['output_started']=True
                current_identity(value)
            elif Path(path).name=='driver-status.json':
                current_identity(value.get('identity'))
            elif Path(path).name.startswith('warm-'):
                current_identity(value.get('optimization_warm'))
                value['source_sha256']=entry_identity['entry_source_sha256']
            value['twelve_query_QR_entry']=entry_identity
            if isinstance(value.get('twelve_query_projection_entry'),dict):
                value['twelve_query_projection_entry']['fixed_support_description_applies_only_to_baseline_C']=True
                value['twelve_query_projection_entry']['complete_global_H_alternative_is_declared_by_twelve_query_QR_entry']=True
        return raw_write(path,value)

    class CapturedLinearization(ORIGINAL_LINEAR):
        def __init__(self,*positional,**keywords):
            live['constructor_calls']+=1
            if live['constructor_calls']!=1:
                raise ValueError('Do not construct a second complete J for the QR alternative')
            super().__init__(*positional,**keywords)
            live['linear']=self

        def operator(self,weights):
            A=super().operator(weights)
            live['operator_calls']+=1
            # Match the frozen operator's np.asarray alias, so the
            # factor's repeated input hashes also watch the live Wr.
            live.update(A=A,weights=np.asarray(weights))
            return A

    def project(domain,z0,diagonal,c,*,max_sweeps,deadline,progress):
        if captured:
            raise ValueError('This entry preserves exactly one actual C projection')
        captured.update(domain=domain,z0=correction.identity(z0),C=np.asarray(diagonal).copy(),
            c=correction.identity(c),original_deadline=float(deadline),domain_model_sha256=domain.model_sha256)
        return ORIGINAL_SUPPORT(domain,z0,diagonal,c,max_sweeps=max_sweeps,
                                deadline=deadline,progress=progress)

    selector=_bind_selector(factory,captured,options,args,entry_identity,write)
    inverse=_QRInverseSlot(live,captured,args,options,entry_identity,write)

    def choose(domain,A,b,z0,projected,damping,c):
        if live.get('A') is not A or live.get('linear') is None or live['constructor_calls']!=1:
            raise ValueError('Reuse the exact same original linearization and returned A object')
        live['chosen_damping']=float(damping)
        live['public_binding']=dict(complete_linearization_constructor_calls=live['constructor_calls'],
            original_operator_constructions_before_choice=live['operator_calls'],
            original_A_object_shared_with_C_comparison=True,
            original_A_shape=list(A.shape),original_weights=correction.identity(live['weights']),
            original_chart_scale=correction.identity(live['linear'].chart.scale),
            original_chart_inlet=correction.identity(live['linear'].chart.inlet),
            complete_B_model_sha256=domain.model_sha256,complete_B_shape=list(domain.shape),
            actual_b=correction.identity(b),actual_z0=correction.identity(z0),
            actual_c=correction.identity(c),damping=float(damping),
            fixed_C_projection_support_does_not_restrict_H=True)
        write(args.out/'block-qr-live-model-binding.json',live['public_binding'])
        try:
            result=selector(domain,A,b,z0,projected,damping,c)
            inverse.preserve()
            return result
        finally:
            inverse.close()

    # Parent binding and the nonlinear engine stay in the twelve-query
    # entry. Its same-schema continuation branch now names this producer;
    # the initial branch still hard-binds the actual37 double identity.
    baseline_saved={key:getattr(baseline,key) for key in ('SCHEMA','SOURCE_NAMES','__doc__')}
    engine_saved={key:getattr(engine,key) for key in ('CompleteLinearization','choose_feasible_descent','write','FROZEN')}
    support_saved=baseline.support.fixed_support_projection
    pcg_saved=correction._pcg
    argv_saved=sys.argv
    baseline.SCHEMA,baseline.SOURCE_NAMES,baseline.__doc__=SCHEMA,SOURCE_NAMES,__doc__
    engine.CompleteLinearization=CapturedLinearization
    engine.choose_feasible_descent=choose
    engine.write=write
    engine.FROZEN={**engine.FROZEN,**FROZEN}
    baseline.support.fixed_support_projection=project
    correction._pcg=inverse
    sys.argv=[argv_saved[0],*remaining]
    try:
        return baseline.main()
    finally:
        sys.argv=argv_saved
        correction._pcg=pcg_saved
        baseline.support.fixed_support_projection=support_saved
        for key,value in engine_saved.items():
            setattr(engine,key,value)
        for key,value in baseline_saved.items():
            setattr(baseline,key,value)
        inverse.close()


if __name__=='__main__':
    raise SystemExit(main())
