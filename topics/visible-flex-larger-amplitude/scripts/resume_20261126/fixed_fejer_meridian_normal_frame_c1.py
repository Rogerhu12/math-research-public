#!/usr/bin/env python3
"""R714 same-graph complete normal-frame C1 reuse, with an exact-zero template.

Only one invocation of the original full implicit stage chain owns a scope.
All eighteen control-jet WORDS, every angle, the derivative order, the current
free tensor and all input tensor objects/versions belong to that scope.  No
active graph or template is restored from another invocation or checkpoint.

The zero template uses the complete left exp(Bu) formula and its first two
control derivatives at u=u_phi=u_phiphi=0.  Its floating-point operations are
explicitly a new evaluation order, not a claim of equality to old AD words.
The caller MUST retain each original stage frame_hat value anchor, every
stage equation/matrix/solve, and the full upstream control graph.  Only first
outer-parameter J/J* is supported; this is not an outer Hessian interface.

All numerical operations require the public repository Actions environment.
"""
import ast
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import time
import textwrap

import numpy as np
import torch


SCHEMA = 'complete-closure-value-compatible-normal-frame-C1-reuse-v1'
ANALYTIC_STAGE_SOURCE_SHA256 = '223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811'
TORCH_VERSION = '2.5.1'
CLOSURE_VALUE_SOURCE_SHA256 = '2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0'
BASE_SOURCE = '552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3'
ORIGINAL_CENTERED_SOURCE = 'b2597012ec8ee063fabbb49a758b592d10f607de55ded3becaa8b62b6a50118d'
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


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific C1 normal-frame evaluation requires public repository Actions')


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


def definition(*, minimum_generic_repetitions=8, zero_template=True):
    if (type(minimum_generic_repetitions) is not int or minimum_generic_repetitions < 2
            or type(zero_template) is not bool):
        raise ValueError('Use a declared positive reuse policy; never infer it from a root tolerance')
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        original_complete_centered_source_sha256=ORIGINAL_CENTERED_SOURCE,
        complete_analytic_stage_source_sha256=ANALYTIC_STAGE_SOURCE_SHA256,
        original_frame_and_active_template_methods_retained=False,
        complete_current_frame_and_original_active_template_methods_retained=True,
        original_frame_evaluations_counter_scope='complete current frame method calls, not asserted AD calls',
        bound_complete_method_AST_sha256=complete_method_ast(),
        complete_closure_value_source_sha256=CLOSURE_VALUE_SOURCE_SHA256,
        minimum_generic_full_batch_repetitions=minimum_generic_repetitions,
        complete_zero_control_jet_analytic_template_enabled=zero_template,
        word_key='ALL 3x6 binary64 control-jet words at every literal angle, including signed zero',
        graph_scope='one active full implicit-stage invocation; same x/data/phi/order tensor graph',
        ordinary_template='F(x,Ustar)+stopgrad(D_U F(x,Ustar))*(Ustage-Ustar)',
        zero_template='complete A0/A1/A2 and H0/H1/H2 from left exp(Bu), all angular Leibniz terms',
        no_grad_value_scope='one complete original _run_chain; exact words; current full analytic frame or its full AD fallback on first read',
        no_grad_stage_equations_matrices_and_trace_retained=True,
        no_grad_values_shared_with_active_C1_scope=False,
        optional_value_cache_copy_failure_uses_current_complete_frame=True,
        complete_first_outer_parameter_derivative_retained=True,
        complete_second_outer_parameter_derivative_supported=False,
        original_stage_primal_frame_anchors_required=True,
        original_normal_stages_and_implicit_matrices_retained=True,
        root_or_stage_or_control_variable_deleted=False,
        active_graph_persisted_between_invocations=False,
        approximate_word_match_allowed=False,
        zero_residual_or_root_assumed_from_initial_point=False,
        analytic_working_reordering_is_bitwise_original_AD=False,
        extra_template_failure_falls_back_to_current_full_frame=True,
        quadrature_rounding_or_speedup_certified=False)


def _array_words(value, shape):
    if isinstance(value,torch.Tensor):
        if value.device.type != 'cpu' or value.dtype != torch.float64:
            raise ValueError('Keep complete CPU binary64 controls')
        value = value.detach().numpy()
    value = np.asarray(value)
    if value.dtype != np.dtype('float64') or value.shape != shape or not np.isfinite(value).all():
        raise ValueError('Keep every finite literal control jet without conversion or truncation')
    array = np.ascontiguousarray(value)
    return array.tobytes(),bool(np.all(array == 0))


def _tensor_identity(value):
    return (id(value),int(value._version),tuple(value.shape),str(value.dtype),
        str(value.device),bool(value.requires_grad),tuple(value.stride()),int(value.storage_offset()))


def _data_identity(value):
    if isinstance(value,torch.Tensor):
        return ('tensor',_tensor_identity(value))
    if isinstance(value,dict):
        if any(not isinstance(key,str) for key in value):
            raise ValueError('Use the complete named original data fields')
        return ('dict',id(value),tuple((key,_data_identity(value[key])) for key in sorted(value)))
    if isinstance(value,(tuple,list)):
        return (type(value).__name__,id(value),tuple(_data_identity(item) for item in value))
    if value is None or type(value) in (bool,int,str):
        return (type(value).__name__,value)
    if type(value) is float and math.isfinite(value):
        return ('float',value.hex())
    raise TypeError('Unexpected mutable or unbound input in the complete normal data graph')


def _new_counts():
    return dict(stage_frame_requests=0,original_frame_evaluations=0,
        planned_word_mismatches=0,generic_templates_built=0,zero_templates_built=0,
        complete_template_reuses=0,generic_partial_reverse_products=0,
        generic_partial_reverse_angle_products=0,structurally_constant_partial_rows=0,
        zero_frame_total_integrations=0,zero_hessian_total_integrations=0,
        zero_hessians_built=0,analytic_cross_array_calls=0,analytic_cross_vector_pairs=0,
        C1_reattachments=0,constant_upstream_template_reads=0,
        template_failures=0,peak_detached_partial_bytes=0,
        detached_value_requests=0,detached_value_hits=0,detached_value_original_reads=0,
        detached_value_cache_failures=0,peak_detached_frame_value_bytes=0)


def _all_data_detached(value):
    if isinstance(value,torch.Tensor):
        return not value.requires_grad and value.grad_fn is None
    if isinstance(value,dict):
        return all(_all_data_detached(item) for item in value.values())
    if isinstance(value,(tuple,list)):
        return all(_all_data_detached(item) for item in value)
    return True


class TemplateUnavailable(RuntimeError):
    pass


class NormalFrameC1Kernel:
    """Source-bound factory; stores counters only, NEVER an active template graph."""
    def __init__(self, q, *, minimum_generic_repetitions=8, zero_template=True):
        require_actions()
        if torch.__version__.split('+')[0] != TORCH_VERSION:
            raise ValueError('Keep the declared CPU PyTorch version')
        self.q = q
        if (q.analytic_stage_jacobian.q is not q
                or q.analytic_stage_jacobian.definition != q.model.get('analytic_stage_jacobian')
                or q.analytic_stage_jacobian.definition.get('source_sha256') != ANALYTIC_STAGE_SOURCE_SHA256):
            raise ValueError('Bind the complete selected analytic J3 producer before any frame scope')
        self.definition = definition(minimum_generic_repetitions=minimum_generic_repetitions,
            zero_template=zero_template)
        if (q.model.get('normal_frame_C1_reuse') != self.definition
                or canonical(q.model) != q.identity
                or q.model.get('implicit_control_dimension') != 6
                or q.model.get('normal_increment_dimension') != 3
                or q.model.get('implicit_dimension_per_stage') != 9
                or q.model.get('normal_stage_count') != q.normal_stage_count
                or q.model.get('complete_first_angular_implicit_dimension') != 6*q.normal_stage_count
                or q.model.get('complete_second_angular_implicit_dimension') != 9*q.normal_stage_count
                or q.model.get('common_partition_for_all_angles_and_free_points') is not True
                or q.model.get('per_angle_adaptive_normal_partition') is not False
                or q.model.get('stationary_KKT_selection_used') is not False
                or q.model.get('base_source_sha256') != BASE_SOURCE
                or q.model.get('base_complete_model') != q.base.model
                or q.base.model.get('source_sha256') != BASE_SOURCE
                or canonical(q.base.model) != q.base.identity):
            raise ValueError('Bind the complete actual centred model, all free variables and all stages')
        methods = {name:getattr(q,name) for name in complete_method_ast()}
        if any(getattr(method,'__self__',None) is not q for method in methods.values()):
            raise ValueError('Do not replace complete instance methods by unbound callbacks')
        path = Path(methods['_normal_frame_jets'].__func__.__code__.co_filename).resolve()
        source = path.read_bytes()
        source_digest = hashlib.sha256(source).hexdigest()
        if q.model.get('source_sha256') != source_digest:
            raise ValueError('The full actual cached operator source and model differ')
        classes = [node for node in ast.parse(source).body
            if isinstance(node,ast.ClassDef) and node.name == 'ZeroClosureOperator']
        if len(classes) != 1:
            raise ValueError('Use the actual complete ZeroClosureOperator source')
        source_methods = {node.name:node for node in classes[0].body
            if isinstance(node,ast.FunctionDef)}
        for name,method in methods.items():
            function = method.__func__
            if (Path(function.__code__.co_filename).resolve() != path
                    or function.__globals__.get('SCHEMA') != q.model.get('schema')
                    or function.__globals__.get('FRAME_C1_SOURCE_SHA256') != sha(__file__)
                    or function.__globals__.get('DETACHED_CLOSURE_SOURCE_SHA256') != CLOSURE_VALUE_SOURCE_SHA256
                    or function.__globals__.get('ANALYTIC_STAGE_SOURCE_SHA256') != ANALYTIC_STAGE_SOURCE_SHA256
                    or name not in source_methods
                    or canonical(_ast_value(source_methods[name])) != complete_method_ast()[name]):
                raise ValueError('Changed complete C1 mathematical method: '+name)
        rotation = q.rotation_coefficients
        if (sha(rotation.__code__.co_filename) != BASE_SOURCE
                or not math.isfinite(float(q.S)) or float(q.S) <= 0):
            raise ValueError('Keep the bound full rotation coefficients and positive actual S carrier')
        self.methods = {name:method.__func__ for name,method in methods.items()}
        self.actual_operator_source_sha256 = source_digest
        self.model_identity_sha256 = q.identity
        self.minimum_repetitions = minimum_generic_repetitions
        self.zero_template = zero_template
        self.scopes_started = 0
        self.scopes_closed = 0
        self.value_scopes_started = 0
        self.value_scopes_closed = 0
        self.counts = _new_counts()
        self.elapsed_seconds = 0.
        self.last_scope = None
        self.last_value_scope = None

    def scope(self, x, data, phi, order, items):
        require_actions()
        self.scopes_started += 1
        return CompleteFrameC1Scope(self,x,data,phi,order,items,self.scopes_started)

    def _finish(self, record):
        self.scopes_closed += 1
        for key,value in record['counts'].items():
            if key.startswith('peak_'):
                self.counts[key] = max(self.counts[key],value)
            else:
                self.counts[key] += value
        self.elapsed_seconds += record['scope_seconds']
        self.last_scope = record

    def value_scope(self, data, keys, order):
        require_actions()
        self.value_scopes_started += 1
        return CompleteDetachedFrameScope(self,data,keys,order,self.value_scopes_started)

    def _finish_value(self, record):
        self.value_scopes_closed += 1
        for key,value in record['counts'].items():
            if key.startswith('peak_'):
                self.counts[key] = max(self.counts[key],value)
            else:
                self.counts[key] += value
        self.elapsed_seconds += record['scope_seconds']
        self.last_value_scope = record

    def metadata(self):
        return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=self.definition,
            actual_operator_source_sha256=self.actual_operator_source_sha256,
            actual_model_identity_sha256=self.model_identity_sha256,
            scopes_started=self.scopes_started,scopes_closed=self.scopes_closed,
            value_scopes_started=self.value_scopes_started,
            value_scopes_closed=self.value_scopes_closed,
            actual_counts=dict(self.counts),scope_seconds=self.elapsed_seconds,
            last_scope=self.last_scope,last_value_scope=self.last_value_scope,
            active_graphs_stored_in_kernel=False,
            duplicate_rate_or_acceleration_claimed=False,
            scope_seconds_include_the_owning_stage_chain=True,
            scope_seconds_exclude_later_external_backward=True,
            complete_parameter_Hessian_supported=False,arithmetic_errors_enclosed=False)


class CompleteFrameC1Scope:
    """Exactly one full angle batch and one existing outer graph."""
    def __init__(self, kernel, x, data, phi, order, items, serial):
        require_actions()
        self.kernel,self.q = kernel,kernel.q
        if (not torch.is_grad_enabled() or not isinstance(x,torch.Tensor) or not x.requires_grad
                or x.dtype != torch.float64 or x.device.type != 'cpu'
                or tuple(x.shape) != (self.q.free_size,) or order not in (1,2)):
            raise ValueError('C1 scopes serve one complete active first-parameter J/J* call')
        phi = np.asarray(phi)
        if phi.dtype != np.dtype('float64') or phi.ndim != 1 or not len(phi) or not np.isfinite(phi).all():
            raise ValueError('Retain every ordered finite binary64 material angle')
        if len(items) != len(phi) or int(data['order']) != order:
            raise ValueError('Use all actual selected roots at this exact angular order')
        self.x,self.data,self.phi = x,data,np.array(phi,copy=True)
        self.phi.setflags(write=False)
        self.order,self.count,self.serial = int(order),len(phi),serial
        self.shape = (self.count,3,6)
        self.x_identity = _tensor_identity(x)
        self.data_identity = _data_identity(data)
        self.point_identity = self.q._current_point_sha256
        self.model_object = self.q.model
        if (self.point_identity is None or self.q.identity != kernel.model_identity_sha256
                or canonical(self.q.model) != kernel.model_identity_sha256):
            raise ValueError('The frame scope has no same actual selected free point/model')
        value = np.ascontiguousarray(x.detach().numpy())
        point = hashlib.sha256(str(value.dtype).encode())
        point.update(json.dumps(list(value.shape)).encode())
        point.update(value.tobytes())
        if point.hexdigest() != self.point_identity:
            raise ValueError('C1 reuse does not reinterpret a different current-point word sequence')
        if any(len(item['stages']) != self.q.normal_stage_count for item in items):
            raise ValueError('No stage may be removed from the complete selected root chain')
        self.planned,self.planned_zero = [],[]
        for index in range(self.q.normal_stage_count):
            values = (np.zeros(self.shape,dtype=np.float64) if index == 0 else
                np.stack([item['stages'][index-1]['controls'] for item in items]))
            words,zero = _array_words(values,self.shape)
            self.planned.append(words)
            self.planned_zero.append(zero)
        self.multiplicity = Counter(self.planned)
        self.cache,self.blocked = {},set()
        self.next_stage = 0
        self.counts = _new_counts()
        self.failures = []
        self.closed = False
        self.started = time.monotonic()
        self.binding = dict(scope_serial=serial,actual_model_identity_sha256=self.q.identity,
            actual_full_free_point_sha256=self.point_identity,
            literal_phi_words_sha256=canonical([float(v).hex() for v in phi]),
            literal_angle_count=self.count,angular_order=order,
            complete_control_jet_shape=list(self.shape),normal_stage_count=self.q.normal_stage_count,
            planned_distinct_full_batch_word_groups=len(self.multiplicity),
            planned_zero_full_batch_stages=sum(self.planned_zero),
            planned_eligible_generic_groups=sum(value >= kernel.minimum_repetitions
                for value in self.multiplicity.values()),
            same_invocation_graph_only=True,working_frames_anchored_by_original_stage=True)

    def _check(self, previous, index):
        if (self.closed or index != self.next_stage or not 0 <= index < len(self.planned)
                or not torch.is_grad_enabled()
                or _tensor_identity(self.x) != self.x_identity
                or _data_identity(self.data) != self.data_identity
                or self.q._current_point_sha256 != self.point_identity
                or self.q.identity != self.kernel.model_identity_sha256
                or self.q.model is not self.model_object
                or any(getattr(self.q,name).__func__ is not function
                    for name,function in self.kernel.methods.items())):
            raise ValueError('A C1 template cannot cross points, graphs, orders, methods or stages')
        words,zero = _array_words(previous,self.shape)
        self.next_stage += 1
        self.counts['stage_frame_requests'] += 1
        return words,zero

    def _original(self, previous):
        self.counts['original_frame_evaluations'] += 1
        return self.q._normal_frame_jets(previous,self.data,self.order)

    def _finite(self, value, label):
        if not bool(torch.isfinite(value.detach()).all()):
            raise TemplateUnavailable('Nonfinite optional '+label+'; retain the original complete frame')
        return value

    def _generic(self, previous):
        local = previous.detach().clone().requires_grad_(True)
        frame = self.q._normal_frame_jets(local,self.data,self.order)
        self._finite(frame,'same-point active frame')
        flat = frame.reshape(self.count,-1)
        rows = []
        # The source-pinned complete rotation/closure/total have NO angle
        # mixing.  A sum over angles therefore returns every own-angle
        # derivative, not a coupled or averaged Jacobian.
        for index in range(flat.shape[1]):
            value = flat[:,index].sum()
            derivative = (torch.autograd.grad(value,local,create_graph=False,
                retain_graph=True,allow_unused=True)[0] if value.requires_grad else None)
            self.counts['generic_partial_reverse_products'] += int(value.requires_grad)
            self.counts['generic_partial_reverse_angle_products'] += self.count*int(value.requires_grad)
            if derivative is None:
                derivative = torch.zeros_like(local)
                self.counts['structurally_constant_partial_rows'] += 1
            rows.append(derivative.detach())
        partial = torch.stack(rows,dim=1).reshape(self.count,self.order+1,3,6,3,6)
        self._finite(partial,'complete control-jet partial')
        self.counts['generic_templates_built'] += 1
        return dict(kind='generic',local=local.detach(),frame=frame,partial=partial)

    def _cross(self, left, right):
        if left.shape != right.shape or left.shape[-1] != 3:
            raise ValueError('All analytic vector products retain their complete explicit shapes')
        self.counts['analytic_cross_array_calls'] += 1
        self.counts['analytic_cross_vector_pairs'] += left.numel()//3
        return torch.cross(left,right,dim=-1)

    def _zero_inputs(self):
        names = ('T','Tp','Tpp')
        matrices = ('W','Wp','Wpp')
        Q = [self.data['meridians'][names[j]] for j in range(self.order+1)]
        B = [self.data['W'][matrices[j]].permute(0,1,3,2) for j in range(self.order+1)]
        points = (self.q.J-1)*self.q.integration_order
        if (any(tuple(value.shape) != (points,self.count,3) for value in Q)
                or any(tuple(value.shape) != (points,self.count,6,3) for value in B)):
            raise ValueError('The analytic template uses EVERY original radial node and six controls')
        return B,Q

    def _column_total(self, value, *, hessian):
        # Repacking the complete six independent control columns as columns
        # of _total leaves every original cell/Gauss/reduction weight intact.
        # Only the vector algebra and column packing are new working orders.
        if value.shape[1:] != (self.count,6,3):
            raise ValueError('Integrate all complete control columns')
        answer = self.q._total(value.reshape(value.shape[0],self.count*6,3))
        self.counts['zero_hessian_total_integrations' if hessian else
            'zero_frame_total_integrations'] += 1
        return answer.reshape(self.count,6,3).transpose(-1,-2)/float(self.q.S)

    def _zero_frame(self, previous):
        B,Q = self._zero_inputs()
        rows = []
        for j in range(self.order+1):
            terms = [math.comb(j,k)*self._cross(B[k],Q[j-k].unsqueeze(-2).expand_as(B[k]))
                for k in range(j+1)]
            rows.append(self._column_total(sum(terms),hessian=False))
        frame = self._finite(torch.stack(rows,dim=1),'complete analytic zero frame')
        self.counts['zero_templates_built'] += 1
        return dict(kind='zero-analytic',local=previous.detach().clone(),frame=frame,partial=None)

    def _zero_partial(self):
        # Only D_U F coefficients are stop-gradient.  The separate analytic
        # A0/A1/A2 frame keeps the complete current q/B external-parameter
        # graph.  R714 requires only one outer derivative at U-Ustar=0.
        with torch.no_grad():
            B,Q = self._zero_inputs()
            angular = []
            for j in range(self.order+1):
                columns = []
                for control in range(6):
                    value = None
                    for first in range(j+1):
                        for second in range(j-first+1):
                            third = j-first-second
                            coefficient = math.factorial(j)//(
                                math.factorial(first)*math.factorial(second)*math.factorial(third))
                            Qc = Q[third]
                            left_inner = self._cross(B[second],Qc.unsqueeze(-2).expand_as(B[second]))
                            left = self._cross(B[first][:,:,control].unsqueeze(-2).expand_as(left_inner),left_inner)
                            right_inner = self._cross(B[second][:,:,control],Qc)
                            right = self._cross(B[first],right_inner.unsqueeze(-2).expand_as(B[first]))
                            term = (coefficient*.5)*(left+right)
                            value = term if value is None else value+term
                    columns.append(self._column_total(value,hessian=True))
                angular.append(torch.stack(columns,dim=2))
            H = torch.stack(angular,dim=1)
            partial = torch.zeros((self.count,self.order+1,3,6,3,6),dtype=torch.float64)
            for j in range(self.order+1):
                for k in range(j+1):
                    partial[:,j,:,:,k,:] = math.comb(j,k)*H[:,j-k]
            self._finite(partial,'complete analytic zero control-jet partial')
        self.counts['zero_hessians_built'] += 1
        return partial.detach()

    def _measure_partial_storage(self):
        self.counts['peak_detached_partial_bytes'] = max(
            self.counts['peak_detached_partial_bytes'],sum(
                item['partial'].numel()*item['partial'].element_size()
                for item in self.cache.values() if item['partial'] is not None))

    def frame(self, previous, stage_index):
        words,zero = self._check(previous,stage_index)
        if words != self.planned[stage_index]:
            self.counts['planned_word_mismatches'] += 1
            return self._original(previous)
        use_zero = self.kernel.zero_template and zero
        if (words in self.blocked or
                (not use_zero and self.multiplicity[words] < self.kernel.minimum_repetitions)):
            return self._original(previous)
        try:
            if words in self.cache:
                template = self.cache[words]
                self.counts['complete_template_reuses'] += 1
            else:
                template = self._zero_frame(previous) if use_zero else self._generic(previous)
                self.cache[words] = template
                self._measure_partial_storage()
            if not previous.requires_grad:
                # A truly constant upstream tensor has no missing U_x edge.
                # This is normally stage one.  It does NOT justify dropping
                # any subsequent stage or its differentiated zero target.
                self.counts['constant_upstream_template_reads'] += 1
                return template['frame']
            if template['partial'] is None:
                template['partial'] = self._zero_partial()
                self._measure_partial_storage()
            partial = template['partial']
            difference = previous-template['local']
            # Identical binary64 words were checked immediately above.  This
            # term is value-zero but carries ALL preceding stage derivatives.
            answer = template['frame']+torch.einsum('ajkilh,alh->ajki',partial,difference)
            self.counts['C1_reattachments'] += 1
            return self._finite(answer,'complete reattached first-parameter frame')
        except (TemplateUnavailable,RuntimeError,MemoryError) as error:
            # Optional higher partial work may fail even when the original
            # full frame is available.  Do not change the root or truncate
            # any variable.  Retry the original complete formula instead.
            self.cache.pop(words,None)
            self.blocked.add(words)
            self.counts['template_failures'] += 1
            self.failures.append(dict(stage_index=int(stage_index),
                full_control_words_sha256=hashlib.sha256(words).hexdigest(),
                template_kind='zero-analytic' if use_zero else 'generic',
                exception_type=type(error).__name__,reason=str(error),
                fallback='original complete normal frame'))
            error.__traceback__ = None
            return self._original(previous)

    def close(self):
        if self.closed:
            return
        record = dict(binding=self.binding,counts=dict(self.counts),
            stage_requests_completed=self.next_stage,
            all_stage_frame_requests_completed=self.next_stage == self.q.normal_stage_count,
            scope_seconds=time.monotonic()-self.started,template_failures=list(self.failures),
            graph_released_from_scope=True,scientific_success_inferred=False,
            numerical_template_or_AD_rounding_enclosed=False)
        self.closed = True
        self.cache.clear()
        self.blocked.clear()
        self.planned.clear()
        self.multiplicity.clear()
        self.data,self.x = None,None
        self.kernel._finish(record)

    def __enter__(self):
        return self

    def __exit__(self, error_type, error, traceback):
        self.close()
        return False


class CompleteDetachedFrameScope:
    """Original numerical frames in one detached root/jet chain only.

    A stage Jacobian differentiates eta with this already selected previous
    frame fixed.  No outer derivative is recovered from this cache.  The
    active first-parameter chain necessarily creates a SEPARATE C1 scope.
    """
    def __init__(self, kernel, data, keys, order, serial):
        require_actions()
        self.kernel,self.q = kernel,kernel.q
        if (torch.is_grad_enabled() or order not in (1,2) or not keys
                or len(keys) != len(data['core'][0]) or int(data['order']) != order
                or not _all_data_detached(data)):
            raise ValueError('Numerical frame reuse requires the complete original detached root data')
        keys = tuple(keys)
        if any(not isinstance(key,str) or not math.isfinite(float.fromhex(key))
                or float.fromhex(key).hex() != key for key in keys):
            raise ValueError('Keep every ordered canonical literal angle in this root batch')
        self.data,self.keys,self.order = data,keys,int(order)
        self.shape = (len(keys),3,6)
        self.point_identity = self.q._current_point_sha256
        if (self.point_identity is None or self.q.identity != kernel.model_identity_sha256
                or canonical(self.q.model) != kernel.model_identity_sha256):
            raise ValueError('The detached frame scope has no same actual free point/model')
        self.model_object = self.q.model
        self.data_identity = _data_identity(data)
        self.cache = {}
        self.blocked = set()
        self.failures = []
        self.next_stage = 0
        self.closed = False
        self.counts = _new_counts()
        self.started = time.monotonic()
        self.binding = dict(scope_serial=serial,actual_model_identity_sha256=self.q.identity,
            actual_full_free_point_sha256=self.point_identity,
            literal_phi_words_sha256=canonical(keys),literal_angle_count=len(keys),
            angular_order=order,complete_control_jet_shape=list(self.shape),
            normal_stage_count=self.q.normal_stage_count,
            first_value_source='complete current analytic-frame producer or its full AD fallback under no_grad',
            all_stage_roots_matrices_residual_rereads_and_trace_retained=True,
            outer_parameter_derivatives_obtained_from_this_cache=False)

    def frame(self, previous, stage_index):
        if (self.closed or torch.is_grad_enabled() or stage_index != self.next_stage
                or not 0 <= stage_index < self.q.normal_stage_count
                or not isinstance(previous,torch.Tensor) or previous.requires_grad
                or previous.grad_fn is not None or not _all_data_detached(self.data)
                or _data_identity(self.data) != self.data_identity
                or self.q._current_point_sha256 != self.point_identity
                or self.q.identity != self.kernel.model_identity_sha256
                or self.q.model is not self.model_object
                or any(getattr(self.q,name).__func__ is not function
                    for name,function in self.kernel.methods.items())):
            raise ValueError('Do not reuse numerical frame values across a graph, point, order or stage')
        words,_ = _array_words(previous,self.shape)
        self.next_stage += 1
        self.counts['detached_value_requests'] += 1
        if words in self.cache:
            try:
                value = self.cache[words].clone()
            except (RuntimeError,MemoryError) as error:
                self._cache_failure(words,stage_index,'return cached clone',error)
                return self._original_value(previous)
            self.counts['detached_value_hits'] += 1
            return value
        value = self._original_value(previous)
        if not bool(torch.isfinite(value).all()) or words in self.blocked:
            # Preserve the original caller's nonfinite-field failure path.
            # Never memoize a failed frame or substitute an assumed zero.
            return value
        try:
            self.cache[words] = value.detach().clone()
        except (RuntimeError,MemoryError) as error:
            self._cache_failure(words,stage_index,'save original clone',error)
            return value
        self.counts['peak_detached_frame_value_bytes'] = max(
            self.counts['peak_detached_frame_value_bytes'],sum(
                item.numel()*item.element_size() for item in self.cache.values()))
        return value

    def _original_value(self, previous):
        self.counts['detached_value_original_reads'] += 1
        value = self.q._normal_frame_jets(previous,self.data,self.order)
        if (value.requires_grad or value.grad_fn is not None
                or tuple(value.shape) != (self.shape[0],self.order+1,3,6)):
            raise ValueError('The original numerical frame did not return the complete detached value')
        return value

    def _cache_failure(self, words, stage_index, operation, error):
        self.cache.pop(words,None)
        self.blocked.add(words)
        self.counts['detached_value_cache_failures'] += 1
        self.failures.append(dict(stage_index=int(stage_index),operation=operation,
            complete_control_words_sha256=hashlib.sha256(words).hexdigest(),
            exception_type=type(error).__name__,reason=str(error),
            fallback='already computed or newly read original complete frame'))
        error.__traceback__ = None

    def close(self):
        if self.closed:
            return
        record = dict(binding=self.binding,counts=dict(self.counts),
            stage_requests_completed=self.next_stage,
            all_stage_frame_requests_completed=self.next_stage == self.q.normal_stage_count,
            scope_seconds=time.monotonic()-self.started,
            same_actual_value_words_reused=True,unexecuted_AD_reread_words_claimed_equal=False,
            optional_cache_failures=list(self.failures),
            derivative_graph_borrowed_by_active_scope=False,scientific_success_inferred=False)
        self.closed = True
        self.cache.clear()
        self.blocked.clear()
        self.data = None
        self.kernel._finish_value(record)

    def __enter__(self):
        return self

    def __exit__(self, error_type, error, traceback):
        self.close()
        return False
