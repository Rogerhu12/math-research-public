#!/usr/bin/env python3
"""Actual same-input first-eight endpoint failure replay and bubble moments.

The original 5b4 numerical root method is copied from its pinned AST.
Observers read small actual arrays; deleting exactly those observer
statements must reproduce the complete original method AST. All
equations, iterations, stopping tests, branch radius and backtracks are
unchanged. No accepted field/checkpoint or continuous proof is produced.
"""
import argparse
import ast
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import numpy as np

SCHEMA='actual-zero-first-eight-endpoint-replay-v1'
TOPIC='topics/visible-flex-larger-amplitude'
INPUT_RELATIVE='scripts/resume_20261126/diagnose_zero_initial_chord.py'
INPUT_SHA='65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0'
ENDPOINT_SHA='5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46'
OBSERVER_NAMES=('_observe_original_root_failure','_observe_original_backtrack')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Actual endpoint re-evaluation requires public repository Actions')


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''):
            h.update(block)
    return h.hexdigest()


def record(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def json_value(value):
    if isinstance(value,dict):
        return {str(k):json_value(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):
        return [json_value(v) for v in value]
    if hasattr(value,'tolist'):
        return json_value(value.tolist())
    if isinstance(value,float) and not math.isfinite(value):
        return None
    return value


def write(path,value):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    part=path.with_name(path.name+'.partial')
    part.write_text(json.dumps(json_value(value),indent=2,allow_nan=False)+'\n')
    part.replace(path)


def load_input(path):
    if sha(path)!=INPUT_SHA:
        raise ValueError('The complete independently bound actual initial-input source changed')
    spec=importlib.util.spec_from_file_location('_zero_actual_initial_chord',path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


def numpy_words(value):
    if hasattr(value,'detach'):
        value=value.detach().cpu().numpy()
    return np.array(value,copy=True)


def array_record(value):
    array=numpy_words(value)
    if array.size>256:
        raise ValueError('The observer only stores the explicitly selected small root arrays')
    flat=array.reshape(-1)
    if array.dtype.kind in 'biu':
        words=[int(v) for v in flat]
        exact=None
        finite=True
    else:
        words=[float(v) if math.isfinite(float(v)) else None for v in flat]
        exact=[float(v).hex() for v in flat]
        finite=bool(np.isfinite(array).all())
    return dict(shape=list(array.shape),dtype=str(array.dtype),values=words,
        exact_binary64_hex_words=exact,finite=finite)


def svd_record(value):
    a=numpy_words(value)
    if a.shape[-2:]!=(3,3) or not np.isfinite(a).all():
        return dict(complete=False,reason='not a finite actual three-by-three matrix')
    try:
        singular=np.linalg.svd(a,compute_uv=False)
    except np.linalg.LinAlgError as error:
        return dict(complete=False,reason=repr(error))
    return dict(complete=True,singular_values=singular.tolist(),
        smallest=singular[...,-1].tolist(),largest=singular[...,0].tolist(),
        minimum_smallest=float(np.min(singular[...,-1])),
        numerical_diagnostic_only=True,rigorous_invertibility_claimed=False)


class Observers:
    def __init__(self,q):
        self.q=q
        self.failures=[]
        self.last_backtrack_by_iteration={}
        self.actual_observed_backtrack_calls=0

    def backtrack(self,local):
        # Inserted immediately after the original trial_norm assignment,
        # before good/accepted updates or any alpha halving.
        index=int(local.get('iteration',-1))
        names=('alpha','candidate','candidate_norm','admissible','trial','trial_norm',
               'norms','accepted')
        item=dict(outer_iteration=index,
            source_location='after actual trial_norm; before good and before alpha halving',
            arrays={name:array_record(local[name]) for name in names if name in local})
        item['armijo_rhs_recomputed_from_same_actual_words']=(
            (1-self.q.policy.armijo*numpy_words(local['alpha']))*numpy_words(local['norms'])).tolist()
        item['rhs_is_a_numerical_diagnostic_not_an_interval_proof']=True
        self.last_backtrack_by_iteration[index]=item
        self.actual_observed_backtrack_calls+=1

    def failure(self,local):
        names=('z','value','norms','A','direction','active','accepted','next_z','alpha',
               'candidate','candidate_norm','admissible','trial','trial_value','trial_norm',
               'final_value','final_norm','singular','iterations')
        item=dict(outer_iteration=int(local.get('iteration',-1)),
            arrays={name:array_record(local[name]) for name in names if name in local},
            actual_failed_angle_indices=[int(v) for v in local.get('bad',[])],
            original_failure_arguments_are_not_modified=True,
            saved_alpha_scope='literal locals at failure; the separate last-backtrack alpha is the actual evaluated value')
        if 'A' in local:
            item['actual_current_A_numerical_singular_diagnostic']=svd_record(local['A'])
        self.failures.append(item)


def observed_original_method(endpoint,path,observers,destination):
    if sha(path)!=ENDPOINT_SHA:
        raise ValueError('The complete original root method source changed')
    tree=ast.parse(Path(path).read_text())
    classes=[node for node in tree.body if isinstance(node,ast.ClassDef) and node.name=='ZeroClosureOperator']
    if len(classes)!=1:
        raise ValueError('One complete original endpoint class is required')
    methods=[node for node in classes[0].body if isinstance(node,ast.FunctionDef) and node.name=='_solve_roots']
    if len(methods)!=1:
        raise ValueError('One complete original numerical method is required')
    original=copy.deepcopy(methods[0])
    original_dump=ast.dump(original,include_attributes=False)
    failure_sites=sum(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute)
        and isinstance(n.func.value,ast.Name) and n.func.value.id=='self' and n.func.attr=='_fail'
        for n in ast.walk(original))
    class AddObservers(ast.NodeTransformer):
        def __init__(self):
            self.failure_sites=0
            self.backtrack_sites=0
        def visit_Expr(self,node):
            node=self.generic_visit(node)
            value=node.value
            if (isinstance(value,ast.Call) and isinstance(value.func,ast.Attribute)
                    and isinstance(value.func.value,ast.Name) and value.func.value.id=='self'
                    and value.func.attr=='_fail'):
                self.failure_sites+=1
                observer=ast.parse('_observe_original_root_failure(locals())').body[0]
                return [observer,node]
            return node
        def visit_Assign(self,node):
            node=self.generic_visit(node)
            if any(isinstance(target,ast.Name) and target.id=='trial_norm' for target in node.targets):
                self.backtrack_sites+=1
                observer=ast.parse('_observe_original_backtrack(locals())').body[0]
                return [node,observer]
            return node
    transform=AddObservers()
    observed=transform.visit(copy.deepcopy(original))
    if transform.failure_sites!=failure_sites or failure_sites<1 or transform.backtrack_sites!=1:
        raise ValueError('Every original failure and the exact actual trial-norm assignment must be observed')
    class RemoveObservers(ast.NodeTransformer):
        def visit_Expr(self,node):
            if (isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name)
                    and node.value.func.id in OBSERVER_NAMES):
                return None
            return self.generic_visit(node)
    restored=RemoveObservers().visit(copy.deepcopy(observed))
    if ast.dump(restored,include_attributes=False)!=original_dump:
        raise ValueError('The complete original numerical method changed beyond read-only observers')
    for node in ast.walk(original):
        if isinstance(node,ast.Name) and node.id in OBSERVER_NAMES:
            raise ValueError('The original method already owns a reserved observer name')
    ast.fix_missing_locations(observed)
    module=ast.Module(body=[observed],type_ignores=[])
    text=ast.unparse(module)+'\n'
    # The full generated method is a small source artifact, not a hidden edit.
    destination.write_text(text)
    environment=dict(endpoint.__dict__)
    environment.update(_observe_original_root_failure=observers.failure,
        _observe_original_backtrack=observers.backtrack,
        __name__='_actual_endpoint_observed_original',__file__=str(destination))
    exec(compile(text,str(destination),'exec'),environment)
    function=environment['_solve_roots']
    return function,dict(original_endpoint_source_sha256=ENDPOINT_SHA,
        original_method_name='ZeroClosureOperator._solve_roots',
        original_complete_method_AST_sha256=hashlib.sha256(original_dump.encode()).hexdigest(),
        removing_exactly_observers_recovers_original_entire_method_AST=True,
        original_failure_sites=failure_sites,observed_failure_sites=transform.failure_sites,
        observed_backtrack_assignment_sites=transform.backtrack_sites,
        complete_generated_method=record(destination),
        q_original_method_replaced=False,physical_equation_or_jacobian_replaced=False,
        original_tolerances_radius_budgets_and_acceptance_unchanged=True)


def hat(v):
    x,y,z=map(float,v)
    return np.array([[0.,-z,y],[z,0.,-x],[-y,x,0.]],dtype=np.float64)


def bubble_moments(actual,endpoint,data,phi):
    q=actual.q
    bubbles,_,masses=q._bubble_values(q.integration_query)
    T=data['meridians']['T']
    with endpoint.torch.no_grad():
        moments=np.stack([numpy_words(q._total(bubbles[i,:,None,None]*T)) for i in range(2)])
        _,_,_,er,et=q._chart(phi)
    er,et=numpy_words(er),numpy_words(et)
    if float(phi[0])!=0. or moments.shape!=(2,len(phi),3):
        raise ValueError('Use the same complete first eight angles, including exact zero')
    original_zero_moments=moments[:,0,:]
    # Exact mathematical axisymmetric reflection imposes y=0. The actual
    # numerical y words remain separately reported, never hidden.
    selected=np.array([[v[0],0.,v[2]] for v in original_zero_moments],dtype=np.float64)
    gram=sum((np.dot(v,v)*np.eye(3)-np.outer(v,v) for v in selected),np.zeros((3,3)))
    result=dict(actual_complete_moments=array_record(moments),
        actual_zero_angle_moments=array_record(original_zero_moments),
        actual_numerical_mass_words=list(map(float,masses)),
        actual_original_radial_cells=q.J-1,actual_quadrature_order=q.integration_order,
        actual_rule='original complete _total with every actual Gauss word and literal mesh width',
        original_total_source_sha256=ENDPOINT_SHA,
        true_moment_integration_or_FloatingPoint_error_certified=False,
        moments_are_working_values_not_true_intervals=True,
        exact_axisymmetric_y_zero_used_only_for_optional_input_definition=True,
        proposed_literal_moments=array_record(selected),
        proposed_covariance_gram=array_record(gram),candidate_Q_installed=False,
        actual_original_input_changed=False)
    if not np.isfinite(gram).all():
        result['candidate_available']=False
        result['candidate_reason']='nonfinite actual moment Gram'
        return result
    result['numerical_gram_eigenvalues']=np.linalg.eigvalsh(gram).tolist()
    try:
        inverse=np.linalg.inv(gram)
    except np.linalg.LinAlgError as error:
        result['candidate_available']=False
        result['candidate_reason']=repr(error)
        return result
    matrices=np.stack([hat(v)@inverse for v in selected])
    if not np.isfinite(matrices).all():
        result['candidate_available']=False
        result['candidate_reason']='nonfinite candidate literal Q'
        return result
    result['candidate_available']=True
    result['candidate_Q_at_angle_zero']=array_record(matrices)
    result['candidate_literal_definition']='exact binary64 matrix words at theta0=0, extended by the same Rz(theta0) conjugation; not yet selected or installed'
    derivative=[]
    for angle in range(len(phi)):
        ez=np.array([0.,0.,1.])
        frame=np.stack([er[angle],et[angle],ez],axis=1)
        Qi=[frame@matrix@frame.T for matrix in matrices]
        derivative.append(sum((-hat(moments[i,angle])@Qi[i] for i in range(2)),np.zeros((3,3))))
    derivative=np.stack(derivative)
    result['candidate_working_Cz_at_zero']=array_record(derivative)
    result['candidate_working_Cz_singular_diagnostic']=svd_record(derivative)
    result['candidate_working_Cz_max_identity_error']=float(np.max(np.abs(derivative-np.eye(3))))
    result['candidate_working_derivative_not_a_true_interval_certificate']=True
    return result


def main(args):
    require_actions()
    started=time.monotonic()
    if args.angle_count!=8 or args.panels<1:
        raise ValueError('Retain the actual failing first eight angles and an explicit valid scalar panel count')
    if args.outdir.exists():
        raise ValueError('Use a fresh small actual endpoint diagnostic directory')
    if args.outdir==args.repo or args.repo in args.outdir.parents:
        raise ValueError('Scientific small reports/caches remain outside the repository')
    args.outdir.mkdir(parents=True)
    args.work_directory=args.outdir/'binding-cache'
    input_path=args.repo/TOPIC/INPUT_RELATIVE
    module=load_input(input_path)
    actual=module.ActualInitialInput(args)
    q=actual.q
    endpoint=sys.modules[q.__class__.__module__]
    for name in ('_C0','_C0_jacobian','_solve_roots','_total','_meridian_data','_bubble_values','_W','_rotate'):
        if sha(getattr(q,name).__func__.__code__.co_filename)!=ENDPOINT_SHA:
            raise ValueError('The original physical/root method changed: '+name)
    phi=np.array(q.phi[:args.angle_count],dtype=np.float64,copy=True)
    query=q.base.make_query(np.array([0],dtype=np.int64),np.array([0.],dtype=np.float64))
    with endpoint.torch.no_grad():
        data,_,_,_=q._meridian_data(endpoint.tensor(actual.x),query,phi,True,'arbitrary')
        zero=endpoint.torch.zeros((len(phi),3),dtype=endpoint.torch.float64)
        initial_C=q._C0(zero,data)
    initial_A=q._C0_jacobian(zero,data)
    moments=bubble_moments(actual,endpoint,data,phi)
    observers=Observers(q)
    function,derivation=observed_original_method(endpoint,endpoint.__file__,observers,
        args.outdir/'observed-original-endpoint-root.py')
    replay_success=False
    actual_error=None
    unexpected=False
    returned=None
    try:
        z,A,records=function(q,data)
        replay_success=True
        returned=dict(z=array_record(z),Cz=array_record(A),records=records)
    except endpoint.EndpointRootFailure as error:
        actual_error=dict(type=type(error).__name__,message=str(error),
            expected_original_numerical_root_failure=True)
    except Exception as error:
        actual_error=dict(type=type(error).__name__,message=repr(error),
            expected_original_numerical_root_failure=False)
        unexpected=True
    last=observers.failures[-1] if observers.failures else None
    last_iteration=None if last is None else last['outer_iteration']
    last_backtrack=observers.last_backtrack_by_iteration.get(last_iteration)
    last_failure=q._last_root_failure
    failed=[] if last_failure is None else list(last_failure.get('first_failed_angle_indices',[]))
    first_failed=None if not failed else int(failed[0])
    failed_summary=dict(index=first_failed,z=None,C=None,norm=None,Newton_direction=None,
        Cz_smallest_singular_value=None,last_actual_alpha=None,last_candidate_norm=None,
        last_candidate_admissible=None,last_actual_trial_norm=None,last_actual_old_norm=None,
        last_armijo_rhs_recomputed=None)
    if last is not None and first_failed is not None:
        def selected(name):
            item=last['arrays'].get(name)
            if item is None:
                return None
            a=np.array(item['values'],dtype=object).reshape(item['shape'])
            return json_value(a[first_failed])
        failed_summary.update(z=selected('z'),C=selected('value'),norm=selected('norms'),
            Newton_direction=selected('direction'))
        singular=last.get('actual_current_A_numerical_singular_diagnostic',{})
        failed_summary['Cz_smallest_singular_value']=None if not singular.get('complete') else singular['smallest'][first_failed]
        if last_backtrack is not None:
            def trial_selected(name):
                item=last_backtrack['arrays'].get(name)
                if item is None:
                    return None
                a=np.array(item['values'],dtype=object).reshape(item['shape'])
                return json_value(a[first_failed])
            failed_summary.update(last_actual_alpha=trial_selected('alpha'),
                last_candidate_norm=trial_selected('candidate_norm'),
                last_candidate_admissible=trial_selected('admissible'),
                last_actual_trial_norm=trial_selected('trial_norm'),
                last_actual_old_norm=trial_selected('norms'),
                last_armijo_rhs_recomputed=last_backtrack['armijo_rhs_recomputed_from_same_actual_words'][first_failed])
    original_failure=actual.failure
    initial_svd=svd_record(initial_A)
    if q.counts['residual_calls'] or q.counts['J_calls'] or q.counts['Jtranspose_calls']:
        raise ArithmeticError('This diagnostic cannot evaluate a complete field/residual/J')
    source_commit=subprocess.check_output(['git','-C',str(args.repo),'rev-parse','HEAD'],text=True).strip()
    report=dict(schema=SCHEMA,source_sha256=sha(__file__),source_commit=source_commit,
        complete=not unexpected,actual_initial_input=actual.binding,
        exact_same_initial_point_sha256=q._current_point_sha256,
        exact_same_model_identity_sha256=q.identity,
        exact_same_fixed_scalar_identity_sha256=actual.profile,
        actual_phi_binary64_hex=[float(v).hex() for v in phi],
        actual_root_policy=q.policy.metadata(),original_report_failure=original_failure,
        new_actual_replay_is_not_an_old_log_read=True,
        actual_failure_values_not_assumed_identical_to_old_run=True,
        complete_original_method_derivation=derivation,
        initial_numerical_C_at_zero=array_record(initial_C),
        initial_numerical_Cz_at_zero=array_record(initial_A),
        initial_numerical_Cz_singular_diagnostic=initial_svd,
        initial_Cz_minimum_smallest_singular_value=initial_svd.get('minimum_smallest'),
        candidate_Cz_minimum_smallest_singular_value=moments.get('candidate_working_Cz_singular_diagnostic',{}).get('minimum_smallest'),
        candidate_Cz_maximum_identity_error=moments.get('candidate_working_Cz_max_identity_error'),
        complete_working_bubble_moments=moments,
        original_method_replay_success=replay_success,
        actual_replay_root_return=returned,actual_replay_error=actual_error,
        actual_replay_failure=last_failure,
        actual_replay_failure_reason=None if last_failure is None else last_failure.get('reason'),
        actual_replay_failure_maximum_residual=None if last_failure is None else last_failure.get('maximum_actual_residual'),
        actual_replay_failure_maximum_correction=None if last_failure is None else last_failure.get('maximum_actual_correction'),
        actual_failed_angle_indices_csv=','.join(map(str,failed)),
        actual_failure_snapshots=observers.failures,
        last_actual_backtrack_by_outer_iteration=observers.last_backtrack_by_iteration,
        actual_observed_backtrack_calls=observers.actual_observed_backtrack_calls,
        first_failed_angle_summary=failed_summary,
        actual_endpoint_counts=dict(q.endpoint_counts),actual_base_counts=dict(q.counts),
        original_source_root_tolerance_unchanged=True,
        original_search_radius_and_budgets_unchanged=True,
        original_initial_point_and_accurate_target_unchanged=True,
        new_input_or_checkpoint_or_field_written=False,
        original_newton_success_not_a_continuous_root_certificate=True,
        full_residual_calls=0,full_J_calls=0,full_Jtranspose_calls=0,
        rigorous_endpoint_derivative_or_root_certificate=False,
        continuous_metric_certified=False,continuous_geometry_certified=False,
        accepted_isometry=False,actual_seconds=time.monotonic()-started)
    write(args.outdir/'report.json',report)
    print(json.dumps(dict(schema=SCHEMA,source_sha256=sha(__file__),
        report_sha256=sha(args.outdir/'report.json'),complete=not unexpected,
        original_replay_success=replay_success,failed_indices_csv=report['actual_failed_angle_indices_csv'],
        initial_Cz_minimum_smallest=initial_svd.get('minimum_smallest'),
        moment_Q_candidate_available=moments['candidate_available'],
        candidate_Q_installed=False,accepted_field=False),allow_nan=False),flush=True)
    return 1 if unexpected else 0


def parse_args():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','failed-report','reference-bundle','preparation-report',
                 'carrier','node-report','scalar-input','outdir'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--panels',type=int,default=128)
    p.add_argument('--angle-count',type=int,default=8)
    args=p.parse_args()
    for key,value in vars(args).items():
        if isinstance(value,Path):
            setattr(args,key,value.resolve())
    return args


if __name__=='__main__':
    raise SystemExit(main(parse_args()))
