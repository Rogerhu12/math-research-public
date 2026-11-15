#!/usr/bin/env python3
"""Request164: independent old-nine plus one selected C2 zero-jet shape.

The finite catalogue consists of the three original supports times powers
k=3,4 of t=2*x-1.  The new coefficient xi is coordinate 9 of an explicitly
ten-dimensional family.  It is never written into an old nine-vector.
Source-bound views retain the original complete112 terminal, real/complex
domain logic, all-column FD and the square453 physical circle consumer.
Import/evaluation is permitted only in this repository's public Actions.
"""
from __future__ import annotations
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
ENTRY='geometry_20261115_adjoint_selected_ten_control_family.py'
SCHEMA='R259-nine-plus-selected-power-C2-ten-control-circle-family-v1'
SCALAR_SCHEMA='complete-old-nine-plus-selected-power-C2-scalar-v1'
DESCRIPTOR_SCHEMA='complete-selected-power-ten-control-real-expression-v1'
PARAMETER_ORDER=('p1','p2','p3','theta1','theta2','theta3','eta1','eta2','eta3','xi')
CATALOGUE=tuple((i,k) for i in range(3) for k in (3,4))
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
    result[ENTRY]=own_identity()['sha256']
    return result


class PowerBump:
    def __init__(self,original_bump,support_index,power):
        if (support_index,power) not in CATALOGUE:
            raise ValueError('Select exactly one of the six declared shapes')
        self.left=float(original_bump.left)
        self.right=float(original_bump.right)
        self.width=float(original_bump.width)
        self.support_index=int(support_index)
        self.power=int(power)

    def jet(self,s):
        x=(s-self.left)/self.width
        if x<=0 or x>=1:
            return np.zeros(3)
        t=2*x-1
        P=64*x**3*(1-x)**3
        dP=64*(3*x**2-12*x**3+15*x**4-6*x**5)
        ddP=64*(6*x-36*x**2+60*x**3-30*x**4)
        k=self.power
        return np.array([self.width**2*P*t**k,
            self.width*(dP*t**k+2*k*P*t**(k-1)),
            ddP*t**k+4*k*dP*t**(k-1)+4*k*(k-1)*P*t**(k-2)])

    def definition(self):
        return dict(family_schema=SCALAR_SCHEMA,
            formula='w^2*64*x^3*(1-x)^3*(2*x-1)^k; x=(s-left)/w; zero extension',
            support=dict(index=self.support_index,left=self.left,right_metadata=self.right,
                         stored_width=self.width,mathematical_right='left+stored_width'),
            power=self.power,coordinate='original material scalar-table station s',
            parameter_name='xi',new_parameter_index=9,
            zero_jet_proof_reference='R351; P has a third-order zero at both support endpoints',
            scalar_zero_jet_order=2,finite_literal_roundoff_enclosure_claimed=False,
            shape_function_independence_does_not_prove_response_rank=True)


class TenControlProfile:
    def __init__(self,original_nine,catalogue_index):
        if not isinstance(catalogue_index,int) or isinstance(catalogue_index,bool) or not 0<=catalogue_index<len(CATALOGUE):
            raise ValueError('An actual catalogue index from 0 through5 is required')
        self.original_nine=original_nine
        self.original_three=original_nine.original_three
        self.catalogue_index=catalogue_index
        i,k=CATALOGUE[catalogue_index]
        self.extra=PowerBump(self.original_three.bumps[i],i,k)
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
            original_nine=self.original_nine.description(),catalogue_index=self.catalogue_index,
            selected_shape=self.extra.definition(),source=own_identity(),
            original_nine_coefficients_are_separate_from_xi=True,
            zero_xi_reduces_to_original_nine_exact_real_formula=True,
            old_nine_scalar_identity_not_relabelled=True)


class ShapeCoefficientsFrozenProfile:
    def __init__(self,designed,shape_coefficients):
        self.designed_ten=designed
        self.shape_coefficients=np.asarray(shape_coefficients,float).copy()
        if self.shape_coefficients.shape!=(7,) or not np.all(np.isfinite(self.shape_coefficients)):
            raise ValueError('Freeze three odd, three quadratic and one selected-power coefficient')
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


def setup(accepted,prepared,anchor,catalogue_index,angles=4096,workers=1):
    original_profile,flow,boundary=old.setup(accepted,prepared,anchor,angles,workers)
    return TenControlProfile(original_profile,catalogue_index),flow,boundary


def scalar_spec(profile,port,parameters,accepted_sha256):
    if not isinstance(profile,TenControlProfile):
        raise TypeError('The selected-power ten-control profile is required')
    p=np.asarray(parameters,float)
    if p.shape!=(10,) or not np.all(np.isfinite(p)):
        raise ValueError('Freeze all actual ten-control scalar coefficients')
    prior=old.scalar_spec(profile.original_nine,port,p[:9],accepted_sha256)
    return dict(schema=SCALAR_SCHEMA,original_nine_specification=prior,
        frozen_design_parameters=p.tolist(),parameter_order=list(PARAMETER_ORDER),
        selected_catalogue_index=profile.catalogue_index,selected_shape=profile.extra.definition(),
        added_coefficient=float(p[9]),finite_added_shape_order='after all original nine terms',
        profile_source_sha256=own_identity()['sha256'],complete_scalar_source_sha256=checked_sources(),
        field_modes=profile.M,tail_modes=profile.tail_modes,fixed_core_targets_count=3,
        native_right_rows=profile.M,new_scalar_family_not_a_same_g_refinement=True,
        canonical_material_metric='ds^2+(a_old9(s;p)+xi*h_selected(s))^2*dtheta_material^2')


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
        selected_shape=encoded(shape),added_coefficient=encoded(specification['added_coefficient']),
        parameter_order=list(PARAMETER_ORDER),source_sha256=own_identity()['sha256'],
        finite_addition_order='unchanged original nine terms, then xi*selected-power shape',
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
        self.breakpoints=self.prior.breakpoints
        self.xi=Q(float(specification['added_coefficient']))
        shape=specification['selected_shape']
        self.power=int(shape['power'])
        self.control=self.prior.base.controls[int(shape['support']['index'])]

    def branch(self,middle):
        return self.prior.branch(middle)

    def value(self,s,branch,middle):
        result=self.prior.value(s,branch,middle)
        left,width=self.control['left'],self.control['stored_width']
        if self.xi and left<middle<left+width:
            x=(s-self.b(left))/self.b(width)
            result+=self.b(self.xi)*self.b(width)**2*64*x**3*(1-x)**3*(2*x-1)**self.power
        return result

    def returned_ap(self,s,branch,middle):
        result=self.prior.returned_ap(s,branch,middle)
        left,width=self.control['left'],self.control['stored_width']
        if self.xi and left<middle<left+width:
            x=(s-self.b(left))/self.b(width);t=2*x-1;k=self.power
            P=64*x**3*(1-x)**3
            dP=64*(3*x**2-12*x**3+15*x**4-6*x**5)
            result+=self.b(self.xi)*self.b(width)*(dP*t**k+2*k*P*t**(k-1))
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
     '            selected_power_shape=self.profile.extra.definition()',1),
    ('nine_parameter_columns_include_circle_radius_and_all_low_mode_transfers',
     'ten_parameter_columns_include_circle_radius_and_all_low_mode_transfers',1)],globals())
scalar_domain=_derived(old.scalar_domain,[
    ('R259-nine-control-complete-declared-scalar-domain-enclosure-v1',
     'R259-selected-power-ten-control-complete-declared-scalar-domain-enclosure-v1',1),
    ('fresh_new_nine_control_identity','fresh_new_ten_control_identity',1)],globals())
complete_reference_check=_derived(old.complete_reference_check,[
    ('all six added shape coefficients fixed','all seven added shape coefficients fixed',1),
    ('all actual odd and quadratic coefficients','all actual odd, quadratic and selected-power coefficients',1),
    ('full_parameters[3:9]','full_parameters[3:10]',1),
    ('full_nine_parameters','full_ten_parameters',1),
    ('actual_frozen_quadratic_coefficients=full_parameters[6:9].tolist(),',
     'actual_frozen_quadratic_coefficients=full_parameters[6:9].tolist(),\n'
     '        actual_frozen_selected_power_coefficient=float(full_parameters[9]),\n'
     '        selected_shape=profile.extra.definition(),',1),
    ('frozen_six_added_shapes_square_check','frozen_seven_added_shapes_square_check',3)],globals())
observed_model_class=_derived(old.observed_model_class,[
    ('nine_control_','ten_control_',4),
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
