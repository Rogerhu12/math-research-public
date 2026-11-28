#!/usr/bin/env python3
"""Complete analytic local normal-plane J3 with original complete AD fallback.

Only the detached diagonal partial in eta changes its numerical producer.
The original full residual, fixed partition, control domain, Newton/Armijo,
angular equations and active implicit graph remain. Small rotations
differentiate the ACTUAL binary-coefficient degree-12 value polynomials.
All scientific operations require this repository's public Actions.
"""
import ast
import hashlib
import json
import math
import os
from pathlib import Path
import time
import textwrap

import numpy as np
import torch

SCHEMA = 'complete-closure-value-compatible-analytic-working-Rodrigues-normal-plane-J3-v1'
ENDPOINT_SCHEMA = 'complete-fixed-fejer-r725-detached-meridian-normal-layer-v1'
BASE_SOURCE_SHA256 = 'b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792'
PARENT_NORMAL_SOURCE_SHA256 = 'd5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb'
TORCH_VERSION = '2.5.1'
CLOSURE_VALUE_SOURCE_SHA256 = '07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6'
METHOD_AST = {
    '_total': 'd402e15c2849dc6b238951e278c0b2f16de8b18fe0e89bc795eb70e127a4b267',
    '_corrected_jets': '790531cf61834d1d4cfbf13f8d6ef4ecb6c5b98a016eeb308d90e96905ab6f13',
    '_closure_jets': '4a090400bd08ab21907cbeb348703c7070a272ae9450eb86921f12c576b43582',
    '_normal_frame_jets': '458f00cb02abc6d279cd4e45feedc21d3e3f34f9168dd497d1f090ad1bc2a8f5',
    '_stage_jacobian': '6db5897c586c0ec00d04ab0a19bebe2743c742bd5d37c4eee1064db8c0fa2010',
    '_stage_jet_jacobian': '7006f94d073979e9530625fa4325f24127bf8895319b20a5e4f9991fc0b63880',
    '_solve_stage': 'ef2857fa502f479cfc4c3ee38a04aad0dbddd7df04fa3650a42fbf1007e356f1',
    '_stage_control_jets': '4a6fc8c940be13fee6faa738e6defff2a8c8c2457f04f8209ebc53fd44e21c8c',
    '_stage_constraints': '804cc04a7a4f374c96607793a0601e2144b27804ca10391e59f8f219094adaf4',
}
COUNTER_KEYS = (
    'matrix_calls_started', 'matrix_calls_returned', 'matrix_calls_failed',
    'requested_angle_blocks', 'analytic_attempts', 'analytic_returns',
    'analytic_failures', 'analytic_angle_blocks_returned',
    'ad_fallback_attempts', 'ad_fallback_returns', 'ad_fallback_failures',
    'ad_fallback_angle_blocks_returned', 'ad_reverse_angle_products',
    'analytic_total_reduction_calls', 'analytic_total_angle_columns',
    'complete_stage_equation_angle_evaluations',
    'complete_closure_jet_angle_evaluations',
    'stage_matrix_angle_evaluations', 'actual_implicit_matrix_angle_rows')
OBSERVED_COUNTER_KEYS = (
    'stage_equation_angle_evaluations', 'closure_jet_angle_evaluations',
    'stage_matrix_angle_evaluations', 'actual_implicit_matrix_angle_rows')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific analytic normal-plane matrices require public Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def _ast_value(value):
    if isinstance(value,ast.AST):
        return [type(value).__name__,[[name,_ast_value(item)]
            for name,item in ast.iter_fields(value)
            if not (name == 'type_params' and item == [])]]
    if isinstance(value,list):
        return [_ast_value(item) for item in value]
    if value is Ellipsis:
        return {'python_literal':'Ellipsis'}
    if isinstance(value,bytes):
        return {'python_bytes_hex':value.hex()}
    return value


METHOD_SOURCE_OVERRIDES = {"_closure_jets": "    def _closure_jets(self, controls, data, order):\n        return self.detached_closure_values.value(controls, data, order)\n", "_closure_jets_original": "    def _closure_jets_original(self, controls, data, order):\n        corrected = self._corrected_jets(data['meridians'],data['W'],controls,order)\n        names = ('T','Tp','Tpp')\n        self.normal_counts['closure_jet_angle_evaluations'] += len(controls)\n        return torch.stack(tuple(((data['core'][j]-data['reference_core'][j])\n            -(data['cap'][j]-data['reference_cap'][j])\n            +self._total(corrected[names[j]]-data['reference'][names[j]]))/self.S\n            for j in range(order+1)),dim=1)\n"}


def complete_method_ast():
    result=dict(METHOD_AST)
    for name,source in METHOD_SOURCE_OVERRIDES.items():
        nodes=ast.parse(textwrap.dedent(source)).body
        if len(nodes)!=1 or not isinstance(nodes[0],ast.FunctionDef) or nodes[0].name!=name:
            raise ValueError('Keep each complete explicitly derived closure method')
        result[name]=canonical(_ast_value(nodes[0]))
    return result


def definition():
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        parent_complete_normal_source_sha256=PARENT_NORMAL_SOURCE_SHA256,
        complete_base_source_sha256=BASE_SOURCE_SHA256,
        bound_complete_method_AST_sha256=complete_method_ast(),
        complete_closure_value_source_sha256=CLOSURE_VALUE_SOURCE_SHA256,
        unknown='eta in R3; all six current controls previous0+frame0^T eta',
        derivative='partial in eta only; full previous/frame/data fixed locally',
        world_direction='e_j=W frame0[j,:], with all six control columns',
        formula='A(e cross V)+B(e cross (w cross V)+w cross (e cross V))+2(w dot e)(Aq(w cross V)+Bq(w cross (w cross V)))',
        small_branch='q=|w|^2<1/4; original binary A/B value coefficients and degree12 Horner value-and-derivative recurrence',
        large_branch='q>=1/4; original sin(sqrt(q))/sqrt(q) and (1-cos(sqrt(q)))/q',
        separately_rounded_small_Az_Bz_tables_used=False,
        derivative_of_original_value_polynomial_coefficients=True,
        zero_rotation_division_required=False,
        original_complete_stage_residual_read_for_each_analytic_attempt=True,
        integral='all three world columns separately through original complete _total, then /S',
        integral_weights_nodes_widths_and_reduction_order_retained=True,
        full_three_by_three_unsymmetrized_matrix=True,
        rank_clipping_jitter_ridge_or_deleted_columns=False,
        optional_failure_policy='original complete three-reverse-product AD; same residual and all angles',
        source_shape_binding_failures_use_optional_fallback=False,
        original_AD_formula_retained_in_fallback=True,
        common_normal_partition_and_all_stages_retained=True,
        original_control_domain_and_Newton_Armijo_retained=True,
        angular_root_equations_and_6_by_6_9_by_9_paths_retained=True,
        full_active_upstream_first_parameter_J_and_transpose_retained=True,
        Newton_iteration_graph_differentiated=False,
        exact_Rodrigues_is_not_bitwise_working_derivative_claim=True,
        branch_seam_truncation_rounding_and_inverse_errors_enclosed=False,
        matrix_nonsingularity_root_success_or_speedup_claimed=False)


def _copy(value):
    return json.loads(json.dumps(value,allow_nan=False))


def _digest(value):
    return (isinstance(value,str) and len(value)==64
        and all(c in '0123456789abcdef' for c in value))


def _counts(value):
    if (not isinstance(value,dict) or set(value)!=set(COUNTER_KEYS)
            or any(type(v) is not int or v<0 for v in value.values())):
        raise ValueError('Keep every actual analytic/AD attempt and return counter')
    if (value['matrix_calls_started'] != value['matrix_calls_returned']+value['matrix_calls_failed']
            or value['analytic_attempts'] != value['analytic_returns']+value['analytic_failures']
            or value['ad_fallback_attempts'] != value['ad_fallback_returns']+value['ad_fallback_failures']
            or not value['matrix_calls_returned'] <= value['analytic_returns']+value['ad_fallback_returns']
                <= value['matrix_calls_started']
            or value['ad_fallback_attempts'] > value['analytic_failures']
            or value['analytic_attempts'] > value['matrix_calls_started']
            or value['analytic_angle_blocks_returned']+value['ad_fallback_angle_blocks_returned']
                > value['requested_angle_blocks']):
        raise ValueError('Do not equate requests, analytic returns, published returns and actual AD work')
    return dict(value)


def validate_metadata(value, *, model, source_by_role, current_full_point_sha256):
    """Pure stdlib attribution; no array, field, matrix or root is evaluated."""
    expected=definition()
    if (not isinstance(value,dict) or value.get('schema')!=SCHEMA
            or value.get('source_sha256')!=source_by_role['analytic_J3']
            or expected['source_sha256']!=source_by_role['analytic_J3']
            or value.get('definition')!=expected
            or model.get('analytic_stage_jacobian')!=expected
            or model.get('schema')!=ENDPOINT_SCHEMA
            or value.get('actual_model_identity_sha256')!=canonical(model)
            or value.get('actual_operator_source_sha256')!=model.get('source_sha256')
            or model.get('base_source_sha256')!=BASE_SOURCE_SHA256):
        raise ValueError('Bind this entire independent local-matrix producer to the actual full field')
    counts=_counts(value.get('actual_counts'))
    elapsed=value.get('matrix_call_seconds')
    if (isinstance(elapsed,bool) or not isinstance(elapsed,(int,float))
            or not math.isfinite(elapsed) or elapsed<0):
        raise ValueError('Keep the actual nonnegative duration without claiming acceleration')
    last=value.get('last_call')
    if last is None:
        if counts['matrix_calls_started']:
            raise ValueError('Do not omit the last attempted matrix request')
    else:
        if (not isinstance(last,dict) or not _digest(last.get('current_full_point_sha256'))
                or type(last.get('angle_count')) is not int or last['angle_count']<=0
                or last.get('matrix_shape')!=[last['angle_count'],3,3]
                or type(last.get('completed')) is not bool
                or last.get('actual_auxiliary_node_hex')
                    not in model.get('actual_normal_step_carriers_binary64_hex',[])[1:]
                or last.get('point_equals_current_report_point')
                    is not (last['current_full_point_sha256']==current_full_point_sha256)):
            raise ValueError('Keep the own matrix point, all angles and actual common stage carrier')
        for key in ('eta_words_sha256','previous_words_sha256','frame_words_sha256','zero_words_sha256'):
            if not _digest(last.get(key)):
                raise ValueError('Keep the complete literal local inputs: '+key)
        origin=last.get('returned_origin')
        if last['completed']:
            if origin not in ('analytic_working_Rodrigues','complete_original_AD'):
                raise ValueError('Name the actual matrix producer')
            if not _digest(last.get('matrix_words_sha256')):
                raise ValueError('A returned complete matrix needs its own word digest')
        elif origin is not None or last.get('matrix_words_sha256') is not None:
            raise ValueError('A failed request is not a successful matrix return')
        if origin=='complete_original_AD' and not isinstance(last.get('analytic_unavailable'),str):
            raise ValueError('An AD fallback must retain its actual analytic failure')
        delta=last.get('actual_normal_counter_deltas')
        if (not isinstance(delta,dict) or set(delta)!=set(OBSERVED_COUNTER_KEYS)
                or any(type(v) is not int or v<0 for v in delta.values())):
            raise ValueError('Keep actual full residual and matrix-row counter deltas')
    for key in ('root_success_inferred_from_matrix_production','measured_acceleration_claimed',
                'local_derivative_rounding_enclosed','global_implicit_chain_replaced'):
        if value.get(key) is not False:
            raise ValueError('Do not promote a working J3 to a field or numerical certificate')
    return _copy(value)


def _tensor(value,shape,name):
    if (not isinstance(value,torch.Tensor) or value.dtype!=torch.float64
            or value.device.type!='cpu' or tuple(value.shape)!=tuple(shape)
            or value.requires_grad or value.grad_fn is not None):
        raise ValueError('Use the complete detached CPU binary64 '+name+' in its actual shape')
    return value


def _words(value):
    array=value.detach().cpu().numpy()
    digest=hashlib.sha256(str(array.dtype).encode())
    digest.update(json.dumps(list(array.shape)).encode())
    digest.update(np.ascontiguousarray(array).tobytes())
    return digest.hexdigest()


def _cross(left,right):
    return torch.cross(left,right,dim=-1)


def _value_coefficients_and_derivatives(q):
    """Differentiate actual value-polynomial coefficients, not rounded Az tables."""
    small=q<.25
    safe=torch.clamp(q,min=.25)
    radius=torch.sqrt(safe)
    sine,cosine=torch.sin(radius),torch.cos(radius)
    large=(sine/radius,(1-cosine)/safe,
        (radius*cosine-sine)/(2*radius**3),
        (radius*sine-2*(1-cosine))/(2*radius**4))
    values=[]
    derivatives=[]
    for offset in (1,2):
        value=torch.zeros_like(q)
        derivative=torch.zeros_like(q)
        for power in range(12,-1,-1):
            # Same binary coefficient expression as derivative=0 of the
            # original bound rotation_coefficients, including its factor.
            factor=math.factorial(power)//math.factorial(power)
            coefficient=((-1.)**power)*factor/math.factorial(2*power+offset)
            derivative=derivative*q+value
            value=value*q+coefficient
        values.append(value)
        derivatives.append(derivative)
    polynomial=(values[0],values[1],derivatives[0],derivatives[1])
    return tuple(torch.where(small,p,t) for p,t in zip(polynomial,large))


class AnalyticStageUnavailable(ArithmeticError):
    pass


class AnalyticNormalStageJacobian:
    """Detached local partial only; no root, matrix or active graph is cached."""
    def __init__(self,q):
        require_actions()
        if torch.__version__.split('+')[0]!=TORCH_VERSION:
            raise ValueError('Keep the declared CPU PyTorch version')
        self.q=q
        self.definition=definition()
        if (q.model.get('schema')!=ENDPOINT_SCHEMA
                or q.model.get('analytic_stage_jacobian')!=self.definition
                or canonical(q.model)!=q.identity
                or q.model.get('base_source_sha256')!=BASE_SOURCE_SHA256
                or q.base.model.get('source_sha256')!=BASE_SOURCE_SHA256
                or q.model.get('base_complete_model')!=q.base.model
                or canonical(q.base.model)!=q.base.identity
                or q.model.get('implicit_control_dimension')!=6
                or q.model.get('normal_increment_dimension')!=3
                or q.model.get('common_partition_for_all_angles_and_free_points') is not True
                or q.model.get('per_angle_adaptive_normal_partition') is not False):
            raise ValueError('Bind the actual complete base, six controls and fixed normal chain')
        methods={name:getattr(q,name) for name in complete_method_ast()}
        if any(getattr(method,'__self__',None) is not q for method in methods.values()):
            raise ValueError('Do not substitute unbound method callbacks')
        path=Path(methods['_stage_jacobian'].__func__.__code__.co_filename).resolve()
        source=path.read_bytes()
        source_digest=hashlib.sha256(source).hexdigest()
        if source_digest!=q.model.get('source_sha256'):
            raise ValueError('The complete actual operator bytes differ')
        classes=[node for node in ast.parse(source).body
            if isinstance(node,ast.ClassDef) and node.name=='ZeroClosureOperator']
        if len(classes)!=1:
            raise ValueError('Use the complete independent normal operator')
        source_methods={node.name:node for node in classes[0].body
            if isinstance(node,ast.FunctionDef)}
        for name,method in methods.items():
            function=method.__func__
            if (Path(function.__code__.co_filename).resolve()!=path
                    or function.__globals__.get('SCHEMA')!=ENDPOINT_SCHEMA
                    or function.__globals__.get('ANALYTIC_STAGE_SOURCE_SHA256')!=sha(__file__)
                    or function.__globals__.get('DETACHED_CLOSURE_SOURCE_SHA256') != CLOSURE_VALUE_SOURCE_SHA256
                    or name not in source_methods
                    or canonical(_ast_value(source_methods[name]))!=complete_method_ast()[name]):
                raise ValueError('A full original method or the explicit wrapper changed: '+name)
        rotation=q.rotation_coefficients
        if (sha(rotation.__code__.co_filename)!=BASE_SOURCE_SHA256
                or not math.isfinite(float(q.S)) or float(q.S)<=0):
            raise ValueError('Keep the bound full working rotation and positive actual S carrier')
        self.methods={name:method.__func__ for name,method in methods.items()}
        self.failure_type=methods['_stage_jacobian'].__func__.__globals__['EndpointRootFailure']
        self.operator_source=source_digest
        self.model_identity=q.identity
        self.model_object=q.model
        self.base_model_object=q.base.model
        self.partition=tuple(float(v).hex() for v in q.normal_step_carriers)
        if list(self.partition)!=q.model.get('actual_normal_step_carriers_binary64_hex'):
            raise ValueError('The complete actual common partition differs')
        self.counts={name:0 for name in COUNTER_KEYS}
        self.seconds=0.
        self.last_call=None

    def _arguments(self,eta,data,previous,frame,zero,tau):
        q=self.q
        if (q.model is not self.model_object or q.base.model is not self.base_model_object
                or q.identity!=self.model_identity
                or q.model.get('analytic_stage_jacobian')!=self.definition
                or any(getattr(q,name).__func__ is not function
                    for name,function in self.methods.items())
                or tuple(float(v).hex() for v in q.normal_step_carriers)!=self.partition
                or float(tau).hex() not in self.partition[1:]
                or not _digest(q._current_point_sha256)
                or data.get('order') not in (1,2)):
            raise ValueError('Keep the actual current field, every method and a declared stage')
        count=len(eta)
        if count<=0:
            raise ValueError('Do not discard the angle batch')
        _tensor(eta,(count,3),'eta')
        _tensor(previous,(count,3,6),'previous controls')
        _tensor(frame,(count,3,3,6),'preceding frame jets')
        _tensor(zero,(count,3,3),'complete zero-target jets')
        points=(q.J-1)*q.integration_order
        _tensor(data['W']['W'],(points,count,3,6),'complete world control matrix')
        _tensor(data['meridians']['T'],(points,count,3),'current uncorrected meridian')
        return count

    def _pay_matrix_rows(self,count):
        self.q.normal_counts['stage_matrix_angle_evaluations']+=count
        self.q.normal_counts['actual_implicit_matrix_angle_rows']+=3*count

    def _analytic(self,eta,data,previous,frame,zero,tau):
        q=self.q
        with torch.no_grad():
            # The full original endpoint/reference/target equation is read.
            # Its nonintegral terms are fixed ONLY in this local eta partial;
            # their complete outer graph remains in the original implicit path.
            q._stage_constraints(eta[:,None],data,previous,frame,zero,tau,0)[:,0]
            controls=q._stage_control_jets(previous,frame,eta[:,None],0)[:,0]
            W=data['W']['W']
            V=data['meridians']['T']
            w=torch.einsum('paij,aj->pai',W,controls)
            radial=(w*w).sum(-1)
            A,B,Aq,Bq=_value_coefficients_and_derivatives(radial)
            c=_cross(w,V)
            d=_cross(w,c)
            coefficient=Aq[...,None]*c+Bq[...,None]*d
            columns=[]
            for j in range(3):
                e=torch.einsum('paij,aj->pai',W,frame[:,0,j,:])
                first=_cross(e,V)
                derivative=(A[...,None]*first
                    +B[...,None]*(_cross(e,c)+_cross(w,first))
                    +(2*(w*e).sum(-1))[...,None]*coefficient)
                self.counts['analytic_total_reduction_calls']+=1
                self.counts['analytic_total_angle_columns']+=len(eta)
                columns.append(q._total(derivative)/q.S)
            result=torch.stack(columns,dim=-1).detach()
        self._pay_matrix_rows(len(eta))
        if not bool(torch.isfinite(result).all()):
            raise AnalyticStageUnavailable('Nonfinite complete analytic local three-by-three matrix')
        return result

    def _original_AD(self,eta,data,previous,frame,zero,tau):
        q=self.q
        # Same original d5da residual and three reverse products. Only the
        # helper's own actual-AD counters are added; no selected row is omitted.
        with torch.enable_grad():
            local=eta.detach().clone().requires_grad_(True)
            value=q._stage_constraints(local[:,None],data,previous,frame,zero,tau,0)[:,0]
            rows=[]
            for j in range(3):
                self.counts['ad_reverse_angle_products']+=len(eta)
                rows.append(torch.autograd.grad(value[:,j].sum(),local,
                    retain_graph=j<2,create_graph=False)[0])
            result=torch.stack(rows,dim=1).detach()
        self._pay_matrix_rows(len(eta))
        if not bool(torch.isfinite(result).all()):
            raise self.failure_type('Nonfinite actual three-dimensional normal-plane Jacobian')
        return result

    def matrix(self,eta,data,previous,frame,zero,tau):
        require_actions()
        count=self._arguments(eta,data,previous,frame,zero,tau)
        record=dict(current_full_point_sha256=self.q._current_point_sha256,
            angle_count=count,matrix_shape=[count,3,3],actual_auxiliary_node_hex=float(tau).hex(),
            eta_words_sha256=_words(eta),previous_words_sha256=_words(previous),
            frame_words_sha256=_words(frame),zero_words_sha256=_words(zero),
            completed=False,returned_origin=None,matrix_words_sha256=None,
            analytic_unavailable=None,point_equals_current_report_point=True)
        self.last_call=record
        before={name:self.q.normal_counts[name] for name in OBSERVED_COUNTER_KEYS}
        started=time.monotonic()
        self.counts['matrix_calls_started']+=1
        self.counts['requested_angle_blocks']+=count
        try:
            self.counts['analytic_attempts']+=1
            try:
                result=self._analytic(eta,data,previous,frame,zero,tau)
            except Exception as error:
                self.counts['analytic_failures']+=1
                if not isinstance(error,(ArithmeticError,MemoryError,RuntimeError)):
                    raise
                record['analytic_unavailable']=type(error).__name__+': '+str(error)
                self.counts['ad_fallback_attempts']+=1
                try:
                    result=self._original_AD(eta,data,previous,frame,zero,tau)
                except Exception:
                    self.counts['ad_fallback_failures']+=1
                    raise
                self.counts['ad_fallback_returns']+=1
                self.counts['ad_fallback_angle_blocks_returned']+=count
                origin='complete_original_AD'
            else:
                self.counts['analytic_returns']+=1
                self.counts['analytic_angle_blocks_returned']+=count
                origin='analytic_working_Rodrigues'
            _tensor(result,(count,3,3),'returned complete local matrix')
            result_digest=_words(result)
            record.update(completed=True,returned_origin=origin,matrix_words_sha256=result_digest)
            self.counts['matrix_calls_returned']+=1
            return result
        except Exception as error:
            self.counts['matrix_calls_failed']+=1
            record['actual_failure']=type(error).__name__+': '+str(error)
            raise
        finally:
            elapsed=time.monotonic()-started
            self.seconds+=elapsed
            record['matrix_call_seconds']=elapsed
            delta={name:self.q.normal_counts[name]-before[name] for name in OBSERVED_COUNTER_KEYS}
            record['actual_normal_counter_deltas']=delta
            self.counts['complete_stage_equation_angle_evaluations']+=delta['stage_equation_angle_evaluations']
            self.counts['complete_closure_jet_angle_evaluations']+=delta['closure_jet_angle_evaluations']
            self.counts['stage_matrix_angle_evaluations']+=delta['stage_matrix_angle_evaluations']
            self.counts['actual_implicit_matrix_angle_rows']+=delta['actual_implicit_matrix_angle_rows']

    def metadata(self):
        last=_copy(self.last_call)
        if last is not None:
            last['point_equals_current_report_point']=(last['current_full_point_sha256']
                == self.q._current_point_sha256)
        return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=self.definition,
            actual_operator_source_sha256=self.operator_source,
            actual_model_identity_sha256=self.model_identity,
            actual_counts=dict(self.counts),matrix_call_seconds=self.seconds,last_call=last,
            root_success_inferred_from_matrix_production=False,
            measured_acceleration_claimed=False,local_derivative_rounding_enclosed=False,
            global_implicit_chain_replaced=False)
