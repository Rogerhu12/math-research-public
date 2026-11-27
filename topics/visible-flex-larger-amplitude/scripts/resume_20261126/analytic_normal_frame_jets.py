#!/usr/bin/env python3
"""Complete analytic six-control normal-frame angular jets.

Differentiate the actual six working Rodrigues coefficient functions and
the actual T/Tphi/Tphiphi expressions. Each of the six control columns is
integrated in the original complete _total order. Active upstream edges
are retained. The original complete reverse-product frame is the optional
numerical fallback. No root, stage, angle, variable, row or point is removed.
Scientific evaluation is public repository Actions only.
"""
import ast
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
import torch

SCHEMA = 'complete-analytic-six-control-working-normal-frame-angular-jets-v1'
ENDPOINT_SCHEMA = 'complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
BASE_SOURCE_SHA256 = '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
PARENT_NORMAL_SOURCE_SHA256 = '04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e'
ORIGINAL_FRAME_AST_SHA256 = 'ee015776b374f6cdcf2711b49e2d25e5cfe78b38b3f7d3886d8596a21b1b0cfc'
TORCH_VERSION = '2.5.1'
METHOD_AST = {'_W': 'f37123850c51d2081d6f25a53b08408f19e6d8ea53f0b8ee889f5851dd6d3eda', '_total': 'd402e15c2849dc6b238951e278c0b2f16de8b18fe0e89bc795eb70e127a4b267', '_corrected_jets': '790531cf61834d1d4cfbf13f8d6ef4ecb6c5b98a016eeb308d90e96905ab6f13', '_closure_jets': '4a090400bd08ab21907cbeb348703c7070a272ae9450eb86921f12c576b43582', '_normal_frame_jets': '458f00cb02abc6d279cd4e45feedc21d3e3f34f9168dd497d1f090ad1bc2a8f5', '_stage_control_jets': '4a6fc8c940be13fee6faa738e6defff2a8c8c2457f04f8209ebc53fd44e21c8c', '_stage_constraints': '804cc04a7a4f374c96607793a0601e2144b27804ca10391e59f8f219094adaf4', '_stage_jet_jacobian': '7006f94d073979e9530625fa4325f24127bf8895319b20a5e4f9991fc0b63880', '_run_chain': '66d0674866dd8d68eb62b6161379dc329d2d5be67ec84fe2a81e3752547da73c', '_get_roots': '7bbe362ba1eda9c973ebc34c7c67d5e3e53b6dc073a5d16ca78e722f73d3e554', '_implicit_jet_value': '8b2bb1407c327f454637695f483f4d52dd3ef051f82c47a572b20d482a63ad6c', '_meridian_data': 'e5244b9fc2e68bee33692e76f7e5aa09422564d1b38bd59cf146646bc8530e9e'}
COUNTER_KEYS = (
    'frame_calls_started', 'frame_calls_returned', 'frame_calls_failed',
    'requested_angle_blocks', 'requested_angle_jets',
    'order0_requests', 'order1_requests', 'order2_requests',
    'active_graph_requests', 'detached_value_requests',
    'analytic_attempts', 'analytic_returns', 'analytic_failures',
    'analytic_angle_blocks_returned', 'analytic_angle_jets_returned',
    'analytic_control_columns_started', 'analytic_control_columns_returned',
    'analytic_total_calls_started', 'analytic_total_calls_returned',
    'analytic_total_angle_vectors_requested', 'analytic_total_angle_vectors_returned',
    'actual_coefficient_value_calls', 'actual_coefficient_derivative_calls',
    'ad_fallback_attempts', 'ad_fallback_returns', 'ad_fallback_failures',
    'ad_fallback_angle_blocks_returned', 'ad_fallback_angle_jets_returned',
    'ad_reverse_products_started', 'ad_reverse_products_returned',
    'ad_reverse_angle_products_started', 'ad_reverse_angle_products_returned',
    'actual_closure_jet_angle_evaluations', 'actual_frame_reverse_angle_products')
OBSERVED_COUNTER_KEYS = ('closure_jet_angle_evaluations', 'frame_reverse_angle_products')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific analytic normal frames require public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def _ast_value(value):
    if isinstance(value, ast.AST):
        return [type(value).__name__, [[name, _ast_value(item)]
            for name, item in ast.iter_fields(value)
            if not (name == 'type_params' and item == [])]]
    if isinstance(value, list):
        return [_ast_value(item) for item in value]
    if value is Ellipsis:
        return {'python_literal': 'Ellipsis'}
    if isinstance(value, bytes):
        return {'python_bytes_hex': value.hex()}
    return value


def _digest(value):
    return (isinstance(value, str) and len(value) == 64
        and all(letter in '0123456789abcdef' for letter in value))


def _copy(value):
    return json.loads(json.dumps(value, allow_nan=False))


def definition():
    return dict(schema=SCHEMA, source_sha256=sha(__file__),
        parent_complete_normal_source_sha256=PARENT_NORMAL_SOURCE_SHA256,
        complete_base_source_sha256=BASE_SOURCE_SHA256,
        original_complete_frame_AST_sha256=ORIGINAL_FRAME_AST_SHA256,
        bound_complete_method_AST_sha256=dict(METHOD_AST),
        unknown='partial with respect to all six U0 slots; U1/U2 are independent jet slots',
        output='all requested orders 0,1,2; shape [angle,order+1,3,6]',
        physical_jets='actual complete _corrected_jets T,Tp,Tpp expressions',
        directions='e0=W[:,ell], e1=Wp[:,ell], e2=Wpp[:,ell] for ell=0,...,5',
        radial_jets='q0=w0.w0; q1=2*w0.w1; q2=2*(w1.w1+w0.w2)',
        coefficient_values='all six actual original rotation_coefficients values A,B,Az,Bz,Azz,Bzz',
        small_branch='q<1/4; independently differentiate each original binary-coefficient Horner polynomial',
        large_branch='q>=1/4; full product/quotient chain rule for each original sin/cos/sqrt expression',
        independent_rounded_Az_used_as_derivative_of_A=False,
        independent_rounded_Azz_used_as_derivative_of_Az=False,
        original_working_coefficient_derivative_functions_all_six=True,
        zero_rotation_division_required=False,
        branch_predicate_and_safe_argument_retained=True,
        reference_core_cap_terms_local_control_derivative_zero=True,
        original_unrotated_meridian_and_W_upstream_graph_retained=True,
        previous_U0_U1_U2_upstream_graph_retained=True,
        active_data_or_previous_detached=False,
        integral='each actual column and requested angular jet through original complete _total, then /S',
        integral_weights_nodes_widths_and_reduction_order_retained=True,
        full_six_columns_without_rank_clipping_or_symmetrization=True,
        optional_failure_policy='complete original reverse-product frame on all requested angles and orders',
        source_shape_binding_failures_use_optional_fallback=False,
        fallback_is_original_reverse_product_frame=True,
        frame_reverse_counter_counts_only_actual_original_reverse_products=True,
        analytic_reduction_counters_separate=True,
        full_active_upstream_parameter_J_and_transpose_retained=True,
        original_common_partition_all_stages_and_true_equations_retained=True,
        original_root_and_angular_implicit_solve_paths_retained=True,
        new_frame_cache_created=False,
        actual_floating_frame_may_differ_from_original_reverse_product_words=True,
        exact_Rodrigues_derivative_not_substituted_for_working_polynomial_derivative=True,
        branch_seam_truncation_rounding_and_inverse_errors_enclosed=False,
        uniform_IFT_root_success_or_field_acceptance_inferred=False,
        measured_acceleration_claimed=False,
        all_scientific_execution_public_Actions_only=True)


def _counts(value):
    if not isinstance(value, dict) or set(value) != set(COUNTER_KEYS):
        raise ValueError('Keep every actual analytic-frame counter')
    if any(type(item) is not int or item < 0 for item in value.values()):
        raise ValueError('Actual counters are nonnegative integers')
    if (value['frame_calls_started'] != value['frame_calls_returned']+value['frame_calls_failed']
            or value['frame_calls_started'] != sum(value['order%d_requests' % j] for j in range(3))
            or value['frame_calls_started'] != value['active_graph_requests']+value['detached_value_requests']
            or value['analytic_attempts'] != value['analytic_returns']+value['analytic_failures']
            or value['ad_fallback_attempts'] != value['ad_fallback_returns']+value['ad_fallback_failures']
            or value['analytic_attempts'] != value['frame_calls_started']
            or value['ad_fallback_attempts'] > value['analytic_failures']
            or not value['frame_calls_returned'] <= value['analytic_returns']+value['ad_fallback_returns']
                <= value['frame_calls_started']
            or value['analytic_angle_blocks_returned']+value['ad_fallback_angle_blocks_returned']
                > value['requested_angle_blocks']
            or value['analytic_angle_jets_returned']+value['ad_fallback_angle_jets_returned']
                > value['requested_angle_jets']
            or value['analytic_control_columns_returned'] > value['analytic_control_columns_started']
            or value['analytic_control_columns_started'] > 6*value['analytic_attempts']
            or value['analytic_total_calls_returned'] > value['analytic_total_calls_started']
            or value['analytic_total_calls_started'] > 3*value['analytic_control_columns_started']
            or value['analytic_total_angle_vectors_returned'] > value['analytic_total_angle_vectors_requested']
            or value['ad_reverse_products_returned'] > value['ad_reverse_products_started']
            or value['ad_reverse_products_started'] > 9*value['ad_fallback_attempts']
            or value['ad_reverse_angle_products_returned'] > value['ad_reverse_angle_products_started']
            or value['actual_frame_reverse_angle_products'] > value['ad_reverse_angle_products_returned']):
        raise ValueError('Requests, partial work, real fallback AD and returns have different meanings')
    return dict(value)


def validate_metadata(value, *, model, source_by_role, current_full_point_sha256):
    """Pure stdlib attribution; no frame, matrix, root, field or array evaluation."""
    expected = definition()
    if (not isinstance(value, dict) or value.get('schema') != SCHEMA
            or value.get('source_sha256') != source_by_role['analytic_frame']
            or expected['source_sha256'] != source_by_role['analytic_frame']
            or value.get('definition') != expected
            or model.get('analytic_normal_frame') != expected
            or model.get('schema') != ENDPOINT_SCHEMA
            or value.get('actual_model_identity_sha256') != canonical(model)
            or value.get('actual_operator_source_sha256') != model.get('source_sha256')
            or model.get('base_source_sha256') != BASE_SOURCE_SHA256):
        raise ValueError('Bind the whole analytic-frame source and complete actual field')
    counts = _counts(value.get('actual_counts'))
    elapsed = value.get('frame_call_seconds')
    if (isinstance(elapsed, bool) or not isinstance(elapsed, (int,float))
            or not math.isfinite(elapsed) or elapsed < 0):
        raise ValueError('Keep the actual nonnegative frame duration')
    last = value.get('last_call')
    if last is None:
        if counts['frame_calls_started']:
            raise ValueError('Do not omit the last attempted frame')
    else:
        if (not isinstance(last, dict) or not _digest(last.get('current_full_point_sha256'))
                or type(last.get('angle_count')) is not int or last['angle_count'] <= 0
                or type(last.get('order')) is not int or last['order'] not in (0,1,2)
                or last.get('frame_shape') != [last['angle_count'],last['order']+1,3,6]
                or type(last.get('completed')) is not bool
                or type(last.get('active_outer_graph_requested')) is not bool
                or not _digest(last.get('previous_jet_words_sha256'))
                or last.get('point_equals_current_report_point')
                    != (last['current_full_point_sha256'] == current_full_point_sha256)):
            raise ValueError('The last frame request must belong to its actual point and full order')
        duration = last.get('frame_call_seconds')
        if (isinstance(duration, bool) or not isinstance(duration, (int,float))
                or not math.isfinite(duration) or duration < 0):
            raise ValueError('Retain the real frame call duration')
        delta = last.get('actual_normal_counter_deltas')
        if (not isinstance(delta, dict) or set(delta) != set(OBSERVED_COUNTER_KEYS)
                or any(type(number) is not int or number < 0 for number in delta.values())):
            raise ValueError('Do not synthesize old normal counters from requested frame work')
        if last['completed']:
            if (last.get('returned_origin') not in
                    ('analytic_complete_working_frame', 'complete_original_reverse_product_frame')
                    or not _digest(last.get('frame_words_sha256'))):
                raise ValueError('A complete returned frame needs its actual origin and all-word digest')
        elif last.get('frame_words_sha256') is not None or last.get('returned_origin') is not None:
            raise ValueError('An incomplete frame cannot reuse a previous returned frame')
    if (value.get('active_upstream_graph_retained') is not True
            or value.get('normal_chain_replaced') is not False
            or value.get('root_success_inferred_from_frame_production') is not False
            or value.get('measured_acceleration_claimed') is not False):
        raise ValueError('Retain the exact scope of this numerical derivative producer')
    return dict(schema=SCHEMA, source_sha256=source_by_role['analytic_frame'],
        actual_operator_source_sha256=value['actual_operator_source_sha256'],
        actual_model_identity_sha256=value['actual_model_identity_sha256'],
        actual_counts=counts, frame_call_seconds=elapsed, last_call=_copy(last),
        active_upstream_graph_retained=True, normal_chain_replaced=False,
        root_success_inferred_from_frame_production=False,
        measured_acceleration_claimed=False,
        working_derivative_rounding_certified=False)


def _tensor(value, shape, label):
    if (not isinstance(value, torch.Tensor) or value.dtype != torch.float64
            or value.device.type != 'cpu' or tuple(value.shape) != tuple(shape)):
        raise ValueError('Use the complete actual CPU float64 tensor: '+label)
    if not bool(torch.isfinite(value).all()):
        raise ValueError('Use finite complete inputs for '+label)


def _words(value):
    array = value.detach().cpu().contiguous().numpy()
    digest = hashlib.sha256(str(array.dtype).encode())
    digest.update(json.dumps(list(array.shape)).encode())
    digest.update(array.tobytes())
    return digest.hexdigest()


def _cross(left, right):
    return torch.cross(left, right, dim=-1)


def _dual_add(left, right):
    return left[0]+right[0], left[1]+right[1]


def _dual_neg(value):
    return -value[0], -value[1]


def _dual_mul(left, right):
    return left[0]*right[0], left[1]*right[0]+left[0]*right[1]


def _dual_div(left, right):
    return left[0]/right[0], (left[1]*right[0]-left[0]*right[1])/(right[0]*right[0])


def _dual_power(value, exponent):
    return value[0]**exponent, exponent*value[0]**(exponent-1)*value[1]


def _coefficient_derivatives(radial):
    """Six derivatives of the six ACTUAL independently rounded functions.

    These are elementary product/quotient rules and Horner recurrences,
    not autograd calls and not the independently rounded Az/Azz tables
    substituted for derivatives of a different coefficient polynomial.
    """
    small = radial < .25
    safe = torch.clamp(radial, min=.25)
    radius = torch.sqrt(safe)
    # In the selected large branch safe==radial and d(radius)/d(radial)=1/(2*radius).
    # Safe positive arguments also keep the unused branch finite at radial=0.
    t = (radius, 1/(2*radius))
    sine = (torch.sin(radius), torch.cos(radius)*t[1])
    cosine = (torch.cos(radius), -torch.sin(radius)*t[1])
    one, two, three, four, five, eight = [(float(n),0.) for n in (1,2,3,4,5,8)]
    radial_pair = (safe, torch.ones_like(safe))
    add, neg, mul, div, power = _dual_add, _dual_neg, _dual_mul, _dual_div, _dual_power
    sub = lambda a,b: add(a,neg(b))
    # The six value expressions have the same arithmetic grouping as the
    # original large branch; only their analytic tangent is consumed.
    large = (
        div(sine,t),
        div(sub(one,cosine),radial_pair),
        div(sub(mul(t,cosine),sine),mul(two,power(t,3))),
        div(sub(mul(t,sine),mul(two,sub(one,cosine))),mul(two,power(t,4))),
        div(add(sub(mul(mul(neg(t),t),sine),mul(mul(three,t),cosine)),
                mul(three,sine)),mul(four,power(t,5))),
        div(add(sub(mul(mul(t,t),cosine),mul(mul(five,t),sine)),
                mul(eight,sub(one,cosine))),mul(four,power(t,6))))
    derivatives = []
    for derivative in (0,1,2):
        for offset in (1,2):
            value = torch.zeros_like(radial)
            tangent = torch.zeros_like(radial)
            for power_index in range(12,derivative-1,-1):
                factor = math.factorial(power_index)//math.factorial(power_index-derivative)
                # Preserve the actual binary coefficient computation of
                # this derivative table, including its independent rounding.
                coefficient = ((-1.)**power_index)*factor/math.factorial(2*power_index+offset)
                tangent = tangent*radial+value
                value = value*radial+coefficient
            derivatives.append(tangent)
    return tuple(torch.where(small, polynomial, formula[1])
        for polynomial,formula in zip(derivatives,large))


class AnalyticFrameUnavailable(ArithmeticError):
    pass


class AnalyticNormalFrame:
    """Full local six-control partial with the complete active outer graph."""
    def __init__(self,q):
        require_actions()
        if torch.__version__.split('+')[0] != TORCH_VERSION:
            raise ValueError('Keep the declared complete CPU PyTorch version')
        self.q = q
        self.definition = definition()
        if (q.model.get('schema') != ENDPOINT_SCHEMA
                or q.model.get('analytic_normal_frame') != self.definition
                or canonical(q.model) != q.identity
                or q.model.get('base_source_sha256') != BASE_SOURCE_SHA256
                or q.base.model.get('source_sha256') != BASE_SOURCE_SHA256
                or q.model.get('base_complete_model') != q.base.model
                or canonical(q.base.model) != q.base.identity
                or q.model.get('implicit_control_dimension') != 6
                or q.model.get('normal_increment_dimension') != 3
                or q.model.get('common_partition_for_all_angles_and_free_points') is not True
                or q.model.get('per_angle_adaptive_normal_partition') is not False):
            raise ValueError('Bind the actual complete field, six controls and whole fixed normal chain')
        methods = {name:getattr(q,name) for name in METHOD_AST}
        if any(getattr(method,'__self__',None) is not q for method in methods.values()):
            raise ValueError('Do not replace bound complete methods with callbacks')
        path = Path(methods['_normal_frame_jets'].__func__.__code__.co_filename).resolve()
        source = path.read_bytes()
        source_digest = hashlib.sha256(source).hexdigest()
        if source_digest != q.model.get('source_sha256'):
            raise ValueError('The actual complete normal operator source differs')
        classes = [node for node in ast.parse(source).body
            if isinstance(node,ast.ClassDef) and node.name == 'ZeroClosureOperator']
        if len(classes) != 1:
            raise ValueError('Use the complete independently declared normal operator')
        source_methods = {node.name:node for node in classes[0].body
            if isinstance(node,ast.FunctionDef)}
        for name,method in methods.items():
            function = method.__func__
            if (Path(function.__code__.co_filename).resolve() != path
                    or function.__globals__.get('SCHEMA') != ENDPOINT_SCHEMA
                    or function.__globals__.get('ANALYTIC_FRAME_SOURCE_SHA256') != sha(__file__)
                    or name not in source_methods
                    or canonical(_ast_value(source_methods[name])) != METHOD_AST[name]):
                raise ValueError('A full original method or the explicit frame wrapper changed: '+name)
        rotation = q.rotation_coefficients
        if (rotation.__name__ != 'rotation_coefficients'
                or sha(rotation.__code__.co_filename) != BASE_SOURCE_SHA256
                or not math.isfinite(float(q.S)) or float(q.S) <= 0):
            raise ValueError('Use the complete original working coefficients and positive actual S carrier')
        self.methods = {name:method.__func__ for name,method in methods.items()}
        self.operator_source = source_digest
        self.model_identity = q.identity
        self.model_object = q.model
        self.base_model_object = q.base.model
        self.partition = tuple(float(value).hex() for value in q.normal_step_carriers)
        if list(self.partition) != q.model.get('actual_normal_step_carriers_binary64_hex'):
            raise ValueError('The actual complete common normal partition differs')
        self.counts = {name:0 for name in COUNTER_KEYS}
        self.seconds = 0.
        self.last_call = None

    def _arguments(self,previous,data,order):
        q = self.q
        if (type(order) is not int or order not in (0,1,2)
                or not isinstance(previous,torch.Tensor) or previous.ndim != 3
                or previous.shape[1] < order+1 or previous.shape[2] != 6):
            raise ValueError('Keep all six control columns and every requested angular jet slot')
        if (q.model is not self.model_object or q.base.model is not self.base_model_object
                or q.identity != self.model_identity
                or q.model.get('analytic_normal_frame') != self.definition
                or any(getattr(q,name).__func__ is not function
                    for name,function in self.methods.items())
                or tuple(float(value).hex() for value in q.normal_step_carriers) != self.partition
                or not _digest(q._current_point_sha256)
                or data.get('order') not in (0,1,2) or data['order'] < order):
            raise ValueError('Keep the current full field, complete method bodies and actual data order')
        count = len(previous)
        if count <= 0:
            raise ValueError('Do not discard an angle batch')
        _tensor(previous,(count,previous.shape[1],6),'previous complete control jets')
        points = (q.J-1)*q.integration_order
        for name in ('W','Wp','Wpp')[:order+1]:
            _tensor(data['W'][name],(points,count,3,6),'complete '+name)
        for name in ('T','Tp','Tpp')[:order+1]:
            _tensor(data['meridians'][name],(points,count,3),'complete current '+name)
        for role in ('core','cap','reference_core','reference_cap'):
            if len(data[role]) < order+1:
                raise ValueError('Retain every complete angular '+role+' jet')
            for j in range(order+1):
                _tensor(data[role][j],(count,3),role+' jet '+str(j))
        for name in ('T','Tp','Tpp')[:order+1]:
            _tensor(data['reference'][name],(points,count,3),'complete reference '+name)
        return count

    def _analytic(self,previous,data,order):
        q = self.q
        enabled = torch.is_grad_enabled()
        local = previous[:,:order+1]
        if enabled and not local.requires_grad:
            # Match the original local-leaf convention without detaching an
            # active previous point or any active meridian/data edge.
            local = local.detach().clone().requires_grad_(True)
        apply = lambda matrix,vector: torch.einsum('paij,aj->pai',matrix,vector)
        expand = lambda value: value[...,None]
        W = data['W']
        meridians = data['meridians']
        w = apply(W['W'],local[:,0])
        V = meridians['T']
        radial = (w*w).sum(-1)
        self.counts['actual_coefficient_value_calls'] += 1
        A,B,Az,Bz,Azz,Bzz = q.rotation_coefficients(radial)
        self.counts['actual_coefficient_derivative_calls'] += 1
        Aq,Bq,Azq,Bzq,Azzq,Bzzq = _coefficient_derivatives(radial)
        first = _cross(w,V)
        second = _cross(w,first)
        if order >= 1:
            wp = apply(W['Wp'],local[:,0])+apply(W['W'],local[:,1])
            Vp = meridians['Tp']
            radial_p = 2*(w*wp).sum(-1)
            first_p = _cross(wp,V)+_cross(w,Vp)
            second_p = _cross(wp,first)+_cross(w,first_p)
            Ap,Bp = Az*radial_p,Bz*radial_p
        if order >= 2:
            wpp = (apply(W['Wpp'],local[:,0])+2*apply(W['Wp'],local[:,1])
                +apply(W['W'],local[:,2]))
            Vpp = meridians['Tpp']
            radial_pp = 2*((wp*wp).sum(-1)+(w*wpp).sum(-1))
            first_pp = _cross(wpp,V)+2*_cross(wp,Vp)+_cross(w,Vpp)
            second_pp = _cross(wpp,first)+2*_cross(wp,first_p)+_cross(w,first_pp)
            App = Azz*radial_p*radial_p+Az*radial_pp
            Bpp = Bzz*radial_p*radial_p+Bz*radial_pp
        columns = []
        for ell in range(6):
            self.counts['analytic_control_columns_started'] += 1
            e = W['W'][...,ell]
            dr = 2*(w*e).sum(-1)
            dfirst = _cross(e,V)
            dsecond = _cross(e,first)+_cross(w,dfirst)
            dA,dB = Aq*dr,Bq*dr
            derivatives = [expand(dA)*first+expand(A)*dfirst
                +expand(dB)*second+expand(B)*dsecond]
            if order >= 1:
                ep = W['Wp'][...,ell]
                drp = 2*((e*wp).sum(-1)+(w*ep).sum(-1))
                dfirst_p = _cross(ep,V)+_cross(e,Vp)
                dsecond_p = (_cross(ep,first)+_cross(wp,dfirst)
                    +_cross(e,first_p)+_cross(w,dfirst_p))
                dAp = Azq*dr*radial_p+Az*drp
                dBp = Bzq*dr*radial_p+Bz*drp
                derivatives.append(expand(dAp)*first+expand(Ap)*dfirst
                    +expand(dA)*first_p+expand(A)*dfirst_p
                    +expand(dBp)*second+expand(Bp)*dsecond
                    +expand(dB)*second_p+expand(B)*dsecond_p)
            if order >= 2:
                epp = W['Wpp'][...,ell]
                drpp = 2*(2*(wp*ep).sum(-1)+(e*wpp).sum(-1)+(w*epp).sum(-1))
                dfirst_pp = _cross(epp,V)+2*_cross(ep,Vp)+_cross(e,Vpp)
                dsecond_pp = (_cross(epp,first)+_cross(wpp,dfirst)
                    +2*(_cross(ep,first_p)+_cross(wp,dfirst_p))
                    +_cross(e,first_pp)+_cross(w,dfirst_pp))
                dApp = (Azzq*dr*radial_p*radial_p+2*Azz*radial_p*drp
                    +Azq*dr*radial_pp+Az*drpp)
                dBpp = (Bzzq*dr*radial_p*radial_p+2*Bzz*radial_p*drp
                    +Bzq*dr*radial_pp+Bz*drpp)
                derivatives.append(expand(dApp)*first+expand(App)*dfirst
                    +2*(expand(dAp)*first_p+expand(Ap)*dfirst_p)
                    +expand(dA)*first_pp+expand(A)*dfirst_pp
                    +expand(dBpp)*second+expand(Bpp)*dsecond
                    +2*(expand(dBp)*second_p+expand(Bp)*dsecond_p)
                    +expand(dB)*second_pp+expand(B)*dsecond_pp)
            totals = []
            for derivative in derivatives:
                self.counts['analytic_total_calls_started'] += 1
                self.counts['analytic_total_angle_vectors_requested'] += len(previous)
                totals.append(q._total(derivative)/q.S)
                self.counts['analytic_total_calls_returned'] += 1
                self.counts['analytic_total_angle_vectors_returned'] += len(previous)
            columns.append(torch.stack(totals,dim=1))
            self.counts['analytic_control_columns_returned'] += 1
        result = torch.stack(columns,dim=-1)
        if not bool(torch.isfinite(result).all()):
            raise AnalyticFrameUnavailable('Nonfinite complete six-control analytic frame')
        return result if enabled else result.detach()

    def _original_AD(self,previous,data,order):
        """The original complete frame, with separate attempt counters only."""
        q = self.q
        enabled = torch.is_grad_enabled()
        with torch.enable_grad():
            local = previous[:,:order+1]
            if not local.requires_grad:
                local = local.detach().clone().requires_grad_(True)
            closure = q._closure_jets(local,data,order)
            frames = []
            for j in range(order+1):
                rows = []
                for k in range(3):
                    self.counts['ad_reverse_products_started'] += 1
                    self.counts['ad_reverse_angle_products_started'] += len(previous)
                    rows.append(torch.autograd.grad(closure[:,j,k].sum(),local,
                        create_graph=enabled,retain_graph=True,allow_unused=False)[0][:,0])
                    self.counts['ad_reverse_products_returned'] += 1
                    self.counts['ad_reverse_angle_products_returned'] += len(previous)
                frames.append(torch.stack(rows,dim=1))
                q.normal_counts['frame_reverse_angle_products'] += 3*len(previous)
            result = torch.stack(frames,dim=1)
        result = result if enabled else result.detach()
        if not bool(torch.isfinite(result).all()):
            raise AnalyticFrameUnavailable('Nonfinite complete original reverse-product frame')
        return result

    def frame(self,previous,data,order):
        require_actions()
        started = time.monotonic()
        count = self._arguments(previous,data,order)
        enabled = torch.is_grad_enabled()
        record = dict(current_full_point_sha256=self.q._current_point_sha256,
            angle_count=count,order=order,frame_shape=[count,order+1,3,6],
            active_outer_graph_requested=enabled,previous_jet_words_sha256=_words(previous),
            completed=False,returned_origin=None,frame_words_sha256=None,
            analytic_unavailable=None,point_equals_current_report_point=True)
        self.last_call = record
        before = {name:self.q.normal_counts[name] for name in OBSERVED_COUNTER_KEYS}
        self.counts['frame_calls_started'] += 1
        self.counts['requested_angle_blocks'] += count
        self.counts['requested_angle_jets'] += count*(order+1)
        self.counts['order%d_requests' % order] += 1
        self.counts['active_graph_requests' if enabled else 'detached_value_requests'] += 1
        try:
            self.counts['analytic_attempts'] += 1
            try:
                result = self._analytic(previous,data,order)
            except Exception as error:
                self.counts['analytic_failures'] += 1
                if not isinstance(error,(ArithmeticError,MemoryError,RuntimeError)):
                    raise
                record['analytic_unavailable'] = type(error).__name__+': '+str(error)
                self.counts['ad_fallback_attempts'] += 1
                try:
                    result = self._original_AD(previous,data,order)
                except Exception:
                    self.counts['ad_fallback_failures'] += 1
                    raise
                self.counts['ad_fallback_returns'] += 1
                self.counts['ad_fallback_angle_blocks_returned'] += count
                self.counts['ad_fallback_angle_jets_returned'] += count*(order+1)
                origin = 'complete_original_reverse_product_frame'
            else:
                self.counts['analytic_returns'] += 1
                self.counts['analytic_angle_blocks_returned'] += count
                self.counts['analytic_angle_jets_returned'] += count*(order+1)
                origin = 'analytic_complete_working_frame'
            _tensor(result,(count,order+1,3,6),'returned complete frame')
            record.update(completed=True,returned_origin=origin,frame_words_sha256=_words(result))
            self.counts['frame_calls_returned'] += 1
            return result
        except Exception as error:
            self.counts['frame_calls_failed'] += 1
            record['actual_failure'] = type(error).__name__+': '+str(error)
            raise
        finally:
            elapsed = time.monotonic()-started
            self.seconds += elapsed
            record['frame_call_seconds'] = elapsed
            delta = {name:self.q.normal_counts[name]-before[name] for name in OBSERVED_COUNTER_KEYS}
            record['actual_normal_counter_deltas'] = delta
            self.counts['actual_closure_jet_angle_evaluations'] += delta['closure_jet_angle_evaluations']
            self.counts['actual_frame_reverse_angle_products'] += delta['frame_reverse_angle_products']

    def metadata(self):
        last = _copy(self.last_call)
        if last is not None:
            last['point_equals_current_report_point'] = (
                last['current_full_point_sha256'] == self.q._current_point_sha256)
        return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=self.definition,
            actual_operator_source_sha256=self.operator_source,
            actual_model_identity_sha256=self.model_identity,
            actual_counts=dict(self.counts),frame_call_seconds=self.seconds,last_call=last,
            active_upstream_graph_retained=True,normal_chain_replaced=False,
            root_success_inferred_from_frame_production=False,
            measured_acceleration_claimed=False,
            working_derivative_rounding_certified=False)

