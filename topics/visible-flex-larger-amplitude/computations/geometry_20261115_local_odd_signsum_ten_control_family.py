#!/usr/bin/env python3
"""Request174: old-nine plus one fixed all-station odd sign-sum function.

The complete R363 catalogue is formed once at the explicit actual157
parent. Centers, positive dyadic widths and coefficients -1/0/+1 are then
immutable during every nonlinear evaluation, forward response and FD.
The full piecewise C2 function is evaluated at arbitrary stations; all its
support endpoints enter the continuous scalar consumer. Original112
terminal and square453 circle responsibilities are retained.
"""
from __future__ import annotations
import bisect
import hashlib
import importlib.util
import inspect
import json
import os
from pathlib import Path
import sys
import textwrap

HERE=Path(__file__).resolve().parent
BASE_NAME='geometry_20261115_small_core_nine_control_family.py'
BASE_SHA='086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629'
ENTRY='geometry_20261115_local_odd_signsum_ten_control_family.py'
LOCATOR_NAME='geometry_20261115_literal_local_zerojet_station_catalogue.py'
LOCATOR_SHA='2d2d84eb1602b681d2f37b08a484c00f992c3d295ed45ad7624be678e2aba74a'
SCHEMA='R259-nine-plus-fixed-local-odd-signsum-ten-control-circle-family-v1'
SCALAR_SCHEMA='complete-old-nine-plus-fixed-local-odd-signsum-C2-scalar-v1'
DESCRIPTOR_SCHEMA='complete-fixed-local-odd-signsum-ten-control-real-expression-v1'
SIGN_SUM_SCHEMA='R370-fixed-all-station-local-odd-signsum-C2-function-v1'
SIGN_SUM_FORMULA='sum_s c_s*epsilon_s^2*t_s*(1-t_s^2)^3 on abs(t_s)<1, t_s=(x-center_s)/epsilon_s; each c_s in {-1,0,1}; zero elsewhere'
PARAMETER_ORDER=('p1','p2','p3','theta1','theta2','theta3','eta1','eta2','eta3','xi')
SOURCE_DERIVATIONS=[]


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific use is restricted to public repository Actions')


def own_identity():
    raw=Path(__file__).read_bytes()
    return dict(name=ENTRY,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def _load():
    require_actions()
    path=HERE/BASE_NAME
    if hashlib.sha256(path.read_bytes()).hexdigest()!=BASE_SHA:
        raise ValueError('The frozen complete original nine-control family differs')
    spec=importlib.util.spec_from_file_location(BASE_NAME[:-3],path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


old=_load()
if hashlib.sha256((HERE/LOCATOR_NAME).read_bytes()).hexdigest()!=LOCATOR_SHA:
    raise ValueError('Bind the frozen actual-station locator')
_locator_spec=importlib.util.spec_from_file_location(LOCATOR_NAME[:-3],HERE/LOCATOR_NAME)
locator=importlib.util.module_from_spec(_locator_spec);sys.modules[_locator_spec.name]=locator
_locator_spec.loader.exec_module(locator)
np=old.np
EXPECTED=old.EXPECTED
original=old.original
canonical_sha=old.canonical_sha
encoded=old.encoded
Q=old.Q
write=old.write
OLD_FOUR_COLUMNS=old.OLD_FOUR_COLUMNS
OLD_SIX_COLUMNS=old.OLD_SIX_COLUMNS


def checked_sources():
    result=dict(old.checked_sources())
    result[BASE_NAME]=BASE_SHA
    result[LOCATOR_NAME]=LOCATOR_SHA
    result[ENTRY]=own_identity()['sha256']
    return result


class SignSumSelectionError(ValueError):
    pass


class FrozenOddSignSum:
    """A fixed function; no weights or signs are recomputed by an evaluator."""
    def __init__(self,pieces,selection):
        require_actions()
        self.selection=locator.metadata_copy(selection)
        formed=[]
        for row in pieces:
            sign=row['coefficient']
            if isinstance(sign,bool) or sign not in (-1,0,1):
                raise ValueError('Each frozen odd coefficient is exactly -1,0,+1')
            shape=locator.FrozenLocalShape.from_definition(row['shape_definition'])
            formed.append((shape,sign,row['group_id']))
        formed.sort(key=lambda row:row[0].center)
        if any(a[0].right>=b[0].left for a,b in zip(formed[:-1],formed[1:])):
            raise ValueError('Keep the exact strictly disjoint local supports')
        if len({row[2] for row in formed})!=len(formed):
            raise ValueError('One fixed shape per unique actual station group')
        self.pieces=tuple(formed)
        self.rights=tuple(row[0].right for row in formed)
        self.breakpoints=tuple(sorted({x for shape,_,_ in formed for x in (shape.left,shape.right)}))
        self.mathematical=dict(schema=SIGN_SUM_SCHEMA,formula=SIGN_SUM_FORMULA,
            pieces=[dict(group_id=index,coefficient=sign,
                center=locator.rational_record(shape.center),
                epsilon=locator.rational_record(shape.epsilon),
                shape_mathematical_sha256=shape.mathematical_sha256)
                for shape,sign,index in formed],
            parameter_name='xi',new_parameter_index=9,
            strict_disjoint_supports=True,exact_added_shape_C2_zero_jet=True,
            original_a_b_columns_not_assumed_derivative_compatible=True)
        self.mathematical_sha256=hashlib.sha256(locator.json_bytes(self.mathematical)).hexdigest()
        self.full=dict(schema=SIGN_SUM_SCHEMA,source=own_identity(),locator_source=locator.own_identity(),
            mathematical=self.mathematical,mathematical_sha256=self.mathematical_sha256,
            selection=self.selection,
            frozen_pieces=[dict(group_id=index,coefficient=sign,shape_definition=shape.definition())
                for shape,sign,index in formed])
        self.complete_definition_sha256=hashlib.sha256(locator.json_bytes(self.full)).hexdigest()

    @classmethod
    def from_catalogue(cls,catalogue):
        require_actions()
        if not catalogue.complete or catalogue.failure is not None:
            raise SignSumSelectionError('The all-station original-nine catalogue is incomplete')
        b=catalogue.b
        rows=[];scores=[]
        with b.precision_context():
            for record in catalogue.candidates:
                catalogue._check()
                response=record['response']
                if record['response_error'] is not None or response is None:
                    raise SignSumSelectionError('An allowed station response failed: '+str(record['group_id']))
                v=response['complete_three_rounded_epsilon_sum_weight_over_a']
                if len(v)!=3 or not all(x.is_finite() for x in v):
                    raise SignSumSelectionError('An allowed station has a nonfinite complete quotient-formula response')
                score=b.dot(catalogue.F,v)
                if not score.is_finite():
                    raise SignSumSelectionError('An allowed station has a nonfinite actual full3 score')
                sign=-1 if score>0 else (1 if score<0 else 0)
                rows.append(dict(group_id=record['group_id'],coefficient=sign,
                    shape_definition=record['shape_definition']))
                scores.append(dict(group_id=record['group_id'],
                    original_support_index=record['shape_definition']['selection']['selected_original_support']['index'],
                    complete_three_rounded_epsilon_sum_weight_over_a=v,
                    actual_full3_quotient_formula_score=score,frozen_coefficient=sign,
                    existing_ratio_rule_score=response['formed_original_full3_merit_action'],
                    quotient_formula_score_minus_ratio_rule_score=score-response['formed_original_full3_merit_action']))
            # These are finite formed contractions, not certified exact derivatives.
            assembled=[sum((b.dec(row['frozen_coefficient'])*row['complete_three_rounded_epsilon_sum_weight_over_a'][j]
                for row in scores),b.ZERO) for j in range(3)]
            selection=dict(origin='actual157 original-nine point only',
                actual_parameter_words=list(catalogue.adjoint.binding['actual_parameter_words']),
                original_literal_binding_sha256=catalogue.adjoint.binding['literal_model_binding_sha256'],
                complete_catalogue_sha256=b.digest(catalogue.candidates),
                complete_catalogue_binding_sha256=b.digest(catalogue.binding),
                score_rule='negative sign of formed F dot rounded(epsilon*sum_over_logical_occurrences(w/a)); exact formed zero maps to0',
                all_allowed_stations_used=True,
                coefficient_count=len(rows),
                positive_coefficients=sum(x['coefficient']==1 for x in rows),
                negative_coefficients=sum(x['coefficient']==-1 for x in rows),
                zero_coefficients=sum(x['coefficient']==0 for x in rows),
                complete_score_table_sha256=b.digest(scores),
                formed_combined_quotient_formula_three_response=[str(x) for x in assembled],
                formed_combined_quotient_formula_merit_action=str(b.dot(catalogue.F,assembled)),
                negative_sum_absolute_formed_scores=str(-sum((abs(x['actual_full3_quotient_formula_score']) for x in scores),b.ZERO)),
                accurate_model_box_optimality_not_claimed_from_formed_scores=True,
                complete_value_jet_directions_not_in_this_odd_box=True,
                proof_reference='R370-disjoint-local-shape-box-descent-and-uniform-C2-bounds')
        obj=cls(rows,selection)
        obj.actual_score_rows=scores
        return obj

    @classmethod
    def from_definition(cls,definition):
        require_actions()
        if (definition.get('schema')!=SIGN_SUM_SCHEMA or definition.get('source')!=own_identity()
                or definition.get('locator_source')!=locator.own_identity()):
            raise ValueError('Bind the actual fixed sign-sum family and locator source')
        obj=cls(definition['frozen_pieces'],definition['selection'])
        if obj.full!=definition:
            raise ValueError('Fixed shape center, width, coefficient or complete identity differs')
        return obj

    def complete_definition(self):
        return locator.metadata_copy(self.full)

    def definition(self):
        return dict(family_schema=SCALAR_SCHEMA,shape_schema=SIGN_SUM_SCHEMA,
            formula=SIGN_SUM_FORMULA,
            support=dict(kind='finite strictly disjoint intervals inside original three open supports',
                piece_count=len(self.pieces),breakpoint_count=len(self.breakpoints)),
            mathematical_shape_sha256=self.mathematical_sha256,
            complete_frozen_definition_sha256=self.complete_definition_sha256,
            source=own_identity(),locator_source=locator.own_identity(),
            parameter_name='xi',new_parameter_index=9,
            nonzero_coefficient_count=sum(sign!=0 for _,sign,_ in self.pieces),
            positive_coefficients=sum(sign==1 for _,sign,_ in self.pieces),
            negative_coefficients=sum(sign==-1 for _,sign,_ in self.pieces),
            zero_coefficients=sum(sign==0 for _,sign,_ in self.pieces),
            scalar_zero_jet_order=2,strict_disjoint_supports=True,
            zero_jet_proof_reference='R363 and R370 exact polynomial identities',
            center_width_sign_frozen_for_all_old9_FD_and_real_trials=True,
            refinement_requires_same_frozen_function_not_regenerated_Kronecker_tables=True,
            finite_literal_roundoff_enclosure_claimed=False,
            shape_function_independence_does_not_prove_response_rank=True)

    def _piece(self,s):
        value=locator.rational(s)
        i=bisect.bisect_right(self.rights,value)
        if i<len(self.pieces) and self.pieces[i][0].left<value<self.pieces[i][0].right:
            return self.pieces[i]
        return None

    def jet(self,s):
        require_actions()
        record=self._piece(s)
        if record is None or record[1]==0:
            return np.zeros(3)
        shape,sign,_=record
        # Evaluate the same fixed function at every point. Do not replace
        # its actual binary64 formula by a grid-dependent Kronecker table.
        return np.asarray(shape.jet_binary64(s),float)*sign

    def interval_jet(self,lift,s,branch_midpoint):
        require_actions()
        record=self._piece(branch_midpoint)
        if record is None or record[1]==0:
            z=lift(Q(0));return z,z,z
        shape,sign,_=record
        return tuple(sign*x for x in shape.interval_jet(lift,s,branch_midpoint))


class TenControlProfile:
    def __init__(self,original_nine,frozen_shape):
        if not isinstance(frozen_shape,FrozenOddSignSum):
            raise ValueError('Use the already selected immutable all-station function')
        self.original_nine=original_nine
        self.original_three=original_nine.original_three
        self.extra=frozen_shape
        self.parameter_count=10
        self.bumps=tuple(original_nine.bumps)+(self.extra,)

    def __getattr__(self,name):
        return getattr(self.original_nine,name)

    def base_jet(self,s):
        return self.original_nine.base_jet(s)

    def control_jets(self,s):
        return np.column_stack((self.original_nine.control_jets(s),self.extra.jet(s)))

    def profile(self,s,parameters=None):
        p=np.zeros(10) if parameters is None else np.asarray(parameters)
        if p.shape!=(10,):
            raise ValueError('Retain nine old coordinates and the independent xi coordinate')
        value=self.original_three.base_jet(s)+self.original_three.control_jets(s)@p[:3]
        for i in old.ODD_ADDITION_ORDER:
            if p[3+i]!=0:
                value=value+p[3+i]*self.original_nine.odds[i].jet(s)
        for i in old.QUADRATIC_ADDITION_ORDER:
            if p[6+i]!=0:
                value=value+p[6+i]*self.original_nine.quadratics[i].jet(s)
        if p[9]!=0:
            value=value+p[9]*self.extra.jet(s)
        if np.isrealobj(value) and (not np.all(np.isfinite(value)) or value[0]<=0 or abs(value[1])>=1):
            raise FloatingPointError('Actual combined ten-control scalar a/ap domain failed')
        return value

    def description(self):
        return dict(schema=SCHEMA,parameter_order=list(PARAMETER_ORDER),parameter_count=10,
            original_nine=self.original_nine.description(),
            selected_shape=self.extra.definition(),source=own_identity(),
            original_nine_coefficients_are_separate_from_xi=True,
            zero_xi_reduces_to_original_nine_exact_real_formula=True,
            old_nine_scalar_identity_not_relabelled=True)


class ShapeCoefficientsFrozenProfile:
    def __init__(self,designed,shape_coefficients):
        self.designed_ten=designed
        self.shape_coefficients=np.asarray(shape_coefficients,float).copy()
        if self.shape_coefficients.shape!=(7,) or not np.all(np.isfinite(self.shape_coefficients)):
            raise ValueError('Freeze three odd, three quadratic and one fixed-local-odd-signsum coefficient')
        self.parameter_count=3
        self.bumps=designed.original_three.bumps

    def __getattr__(self,name):
        return getattr(self.designed_ten.original_three,name)

    def base_jet(self,s):
        value=self.designed_ten.original_three.base_jet(s)
        for i in old.ODD_ADDITION_ORDER:
            if self.shape_coefficients[i]!=0:
                value=value+self.shape_coefficients[i]*self.designed_ten.original_nine.odds[i].jet(s)
        for i in old.QUADRATIC_ADDITION_ORDER:
            if self.shape_coefficients[3+i]!=0:
                value=value+self.shape_coefficients[3+i]*self.designed_ten.original_nine.quadratics[i].jet(s)
        if self.shape_coefficients[6]!=0:
            value=value+self.shape_coefficients[6]*self.designed_ten.extra.jet(s)
        return value

    def control_jets(self,s):
        return self.designed_ten.original_three.control_jets(s)

    def profile(self,s,parameters=None):
        p=np.zeros(3) if parameters is None else np.asarray(parameters)
        if p.shape!=(3,):
            raise ValueError('The final square453 check retains exactly three active original controls')
        return self.designed_ten.profile(s,np.r_[p,self.shape_coefficients])


def setup(accepted,prepared,anchor,frozen_shape,angles=4096,workers=1):
    original_profile,flow,boundary=old.setup(accepted,prepared,anchor,angles,workers)
    return TenControlProfile(original_profile,frozen_shape),flow,boundary


def scalar_spec(profile,port,parameters,accepted_sha256):
    if not isinstance(profile,TenControlProfile):
        raise TypeError('The fixed-local-odd-signsum ten-control profile is required')
    p=np.asarray(parameters,float)
    if p.shape!=(10,) or not np.all(np.isfinite(p)):
        raise ValueError('Freeze all actual ten-control scalar coefficients')
    prior=old.scalar_spec(profile.original_nine,port,p[:9],accepted_sha256)
    return dict(schema=SCALAR_SCHEMA,original_nine_specification=prior,
        frozen_design_parameters=p.tolist(),parameter_order=list(PARAMETER_ORDER),
        selected_shape=profile.extra.definition(),frozen_piecewise_definition=profile.extra.complete_definition(),
        added_coefficient=float(p[9]),finite_added_shape_order='after all original nine terms',
        profile_source_sha256=own_identity()['sha256'],complete_scalar_source_sha256=checked_sources(),
        field_modes=profile.M,tail_modes=profile.tail_modes,fixed_core_targets_count=3,
        native_right_rows=profile.M,new_scalar_family_not_a_same_g_refinement=True,
        canonical_material_metric='ds^2+(a_old9(s;p)+xi*h_star(s))^2*dtheta_material^2')


def export_scalar_descriptor(profile,specification):
    if specification.get('schema')!=SCALAR_SCHEMA:
        raise ValueError('Do not relabel this ten-coordinate scalar as an original nine-family')
    prior=specification['original_nine_specification']
    old_three=prior['original_three_parameter_specification']
    rebuilt=scalar_spec(profile,old_three['complete_original_port'],
        specification['frozen_design_parameters'],old_three['accepted_prefix_sha256'])
    if rebuilt!=specification:
        raise ValueError('The actual ten-control specification differs')
    previous=old.export_scalar_descriptor(profile.original_nine,prior)
    shape=specification['selected_shape']
    expression=dict(base_nine_expression=previous['mathematical_expression'],
        base_nine_mathematical_identity_sha256=previous['mathematical_identity_sha256'],
        selected_shape=encoded(shape),
        frozen_piecewise_definition=encoded(specification['frozen_piecewise_definition']),
        added_coefficient=encoded(specification['added_coefficient']),
        parameter_order=list(PARAMETER_ORDER),source_sha256=own_identity()['sha256'],
        finite_addition_order='unchanged original nine terms, then xi*fixed-local-odd-signsum shape',
        original_finite_Gauss_radius_and_independent_ap_app_retained=True)
    return dict(schema=DESCRIPTOR_SCHEMA,full_specification_sha256=canonical_sha(specification),
        mathematical_expression=expression,mathematical_identity_sha256=canonical_sha(expression),
        base_nine_descriptor=previous,new_metric_family=True,
        old_scalar_domain_certificate_reused=False,literal_floating_evaluator_error_verified=False,
        original_global_scalar_C2_interfaces_verified_here=False,
        added_shape_alone_has_exact_declared_zero_012_jets=True)


class ScalarExpression:
    def __init__(self,specification,descriptor,primitive):
        if (descriptor.get('schema')!=DESCRIPTOR_SCHEMA
                or descriptor['full_specification_sha256']!=canonical_sha(specification)
                or descriptor['mathematical_identity_sha256']!=canonical_sha(descriptor['mathematical_expression'])):
            raise ValueError('Bind the complete new mathematical expression')
        self.prior=old.ScalarExpression(specification['original_nine_specification'],
                                      descriptor['base_nine_descriptor'],primitive)
        self.b=self.prior.b
        self.xi=Q(float(specification['added_coefficient']))
        self.shape=FrozenOddSignSum.from_definition(specification['frozen_piecewise_definition'])
        if self.shape.definition()!=specification['selected_shape']:
            raise ValueError('Complete piecewise function and compact identity differ')
        # Every original and new exact support endpoint is part of the same
        # complete expression. No narrow bump can be skipped by one old cell.
        self.breakpoints=sorted(set(self.prior.breakpoints).union(self.shape.breakpoints))
        left,right=self.prior.breakpoints[0],self.prior.breakpoints[-1]
        if any(not left<x<right for x in self.shape.breakpoints):
            raise ValueError('New support endpoints must be inside the original declared interval')

    def branch(self,middle):
        return self.prior.branch(middle)

    def value(self,s,branch,middle):
        result=self.prior.value(s,branch,middle)
        if self.xi:
            result+=self.b(self.xi)*self.shape.interval_jet(self.b,s,middle)[0]
        return result

    def returned_ap(self,s,branch,middle):
        result=self.prior.returned_ap(s,branch,middle)
        if self.xi:
            result+=self.b(self.xi)*self.shape.interval_jet(self.b,s,middle)[1]
        return result


def _derived(function,replacements,namespace):
    raw=inspect.getsource(function)
    changed=raw
    operations=[]
    for before,after,count in replacements:
        if changed.count(before)!=count:
            raise ValueError('A source-bound view no longer has its exact declared occurrence count: '+before)
        changed=changed.replace(before,after)
        operations.append(dict(before=before,after=after,occurrences=count))
    space=dict(vars(old));space.update(namespace)
    space['__name__']=__name__
    exec(compile(textwrap.dedent(changed),str(HERE/ENTRY)+'::<'+function.__qualname__+'>','exec'),space)
    SOURCE_DERIVATIONS.append(dict(original_function=function.__qualname__,
        original_source_sha256=BASE_SHA,original_function_text_sha256=hashlib.sha256(raw.encode()).hexdigest(),
        derived_function_text_sha256=hashlib.sha256(changed.encode()).hexdigest(),operations=operations))
    return space[function.__name__]


class CircleReference(old.CircleReference):
    pass


CircleReference.evaluate=_derived(old.CircleReference.evaluate,[
    ('parameters.shape != (9,)','parameters.shape != (10,)',1),
    ('Consume all nine design controls in their explicitly declared order',
     'Consume all ten design controls in their explicitly declared order',1),
    ('        real = np.isrealobj(parameters)',
     '        nodes = nodes+parameters[9]*self.controls[:, :, 9]\n'
     '        middle = middle+parameters[9]*self.controls_mid[:, :, 9]\n'
     '        real = np.isrealobj(parameters)',1)],globals())
CircleReference.jacobian=_derived(old.CircleReference.jacobian,
    [('range(9)','range(10)',1)],globals())
CircleReference.description=_derived(old.CircleReference.description,[
    ('range(9)','range(10)',1),('np.zeros(9)','np.zeros(10)',1),
    ('all_nine_columns_attempted','all_ten_columns_attempted',1),
    ('all_nine_columns_checked','all_ten_columns_checked',1),
    ('len(errors)==9','len(errors)==10',1),
    ('three_by_nine_parameter_jacobian','three_by_ten_parameter_jacobian',1),
    ('response_shape=[3,9]','response_shape=[3,10]',1),
    ('newly_added_column_indices=[6,7,8], newly_added_column_responses=J[:, 6:9].tolist()',
     'newly_added_column_indices=[9], newly_added_column_responses=J[:, 9:10].tolist(),\n'
     '            original_nine_column_singular_values=np.linalg.svd(J[:, :9], compute_uv=False).tolist(),\n'
     '            fixed_local_odd_signsum_shape=self.profile.extra.definition()',1),
    ('nine_parameter_columns_include_circle_radius_and_all_low_mode_transfers',
     'ten_parameter_columns_include_circle_radius_and_all_low_mode_transfers',1)],globals())
scalar_domain=_derived(old.scalar_domain,[
    ('R259-nine-control-complete-declared-scalar-domain-enclosure-v1',
     'R259-fixed-local-odd-signsum-ten-control-complete-declared-scalar-domain-enclosure-v1',1),
    ('fresh_new_nine_control_identity','fresh_new_ten_control_identity',1)],globals())
complete_reference_check=_derived(old.complete_reference_check,[
    ('all six added shape coefficients fixed','all seven added shape coefficients fixed',1),
    ('all actual odd and quadratic coefficients','all actual odd, quadratic and fixed-local-odd-signsum coefficients',1),
    ('full_parameters[3:9]','full_parameters[3:10]',1),
    ('full_nine_parameters','full_ten_parameters',1),
    ('actual_frozen_quadratic_coefficients=full_parameters[6:9].tolist(),',
     'actual_frozen_quadratic_coefficients=full_parameters[6:9].tolist(),\n'
     '        actual_frozen_local_odd_signsum_coefficient=float(full_parameters[9]),\n'
     '        selected_shape=profile.extra.definition(),',1),
    ('frozen_six_added_shapes_square_check','frozen_seven_added_shapes_square_check',3)],globals())
observed_model_class=_derived(old.observed_model_class,[
    ('nine_control_','local_odd_signsum_ten_control_',4),
    ('current_full_three_by_nine_jacobian','current_full_three_by_ten_jacobian',1)],globals())


def zero_xi_readback(old_model,extended_model,old_state,extended_state):
    """Existing original/new evaluated arrays only; no extra original evaluate."""
    rows=[]
    for name,prior in old_state.items():
        if name=='parameters':
            continue
        a,b=np.ascontiguousarray(prior),np.ascontiguousarray(extended_state[name])
        rows.append(dict(array=name,old_shape=list(a.shape),new_shape=list(b.shape),
            old_dtype=str(a.dtype),new_dtype=str(b.dtype),old_bytes=a.nbytes,new_bytes=b.nbytes,
            old_sha256=hashlib.sha256(a.tobytes()).hexdigest(),
            new_sha256=hashlib.sha256(b.tobytes()).hexdigest(),
            byte_identical=a.shape==b.shape and a.dtype==b.dtype and a.tobytes()==b.tobytes()))
    return dict(original_nine_parameters=old_state['parameters'].tolist(),
        extended_ten_parameters=extended_state['parameters'].tolist(),added_coefficient=0.0,
        array_readback=rows,all_recorded_arrays_byte_identical=all(x['byte_identical'] for x in rows),
        zero_extension_is_a_mathematical_identity=True,
        numerical_word_comparison_is_not_an_acceptance_gate=True,
        old_J_or_merit_not_adopted_by_new_owner=True)


def sampled_shape_binding(profile,literal_mesh_canonical_sha256):
    return dict(kind='independent-sampled-scalar-shape',
        coefficient_is_an_original_nine_parameter=False,source=own_identity(),
        definition=profile.extra.definition(),
        coordinate_contract=dict(derivative_column='derivative with respect to original scalar-table coordinate',
            literal_mesh_canonical_sha256=literal_mesh_canonical_sha256))
