#!/usr/bin/env python3
"""Request164: explicitly ten-coordinate Decimal50 literal circle model.

The original nine coefficient arrays and current parameters are retained
as a bound parent object.  One selected independently named shape column
is appended, never placed in any old nine-vector.  Only the affine scalar
formation and dimensional response/FD contracts are extended.  All699
radius steps, three2x2 transfers, complete112 terminal and original domain
arithmetic are source-bound views of the frozen2422 model.
"""
from __future__ import annotations
import hashlib
import importlib.util
import inspect
import os
from pathlib import Path
import sys
import textwrap

HERE=Path(__file__).resolve().parent
BASE_NAME='geometry_20261115_nine_control_decimal_literal_model.py'
BASE_SHA='2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75'
ENTRY='geometry_20261115_adjoint_selected_ten_decimal_model.py'
MODEL_SCHEMA='ten-control-selected-power-persistent-decimal50-literal-circle-model-v1'
SOURCE_DERIVATIONS=[]


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific execution is restricted to public repository Actions')


def _load():
    require_actions()
    path=HERE/BASE_NAME
    if hashlib.sha256(path.read_bytes()).hexdigest()!=BASE_SHA:
        raise ValueError('The frozen complete Decimal primal source differs')
    spec=importlib.util.spec_from_file_location(BASE_NAME[:-3],path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


b=_load()
D=b.D
ZERO,ONE,TWO=b.ZERO,b.ONE,b.TWO
PRECISION=b.PRECISION
ROUND_HALF_EVEN=b.ROUND_HALF_EVEN
ARM,TOL,EPS64,FD_STEPS=b.ARM,b.TOL,b.EPS64,b.FD_STEPS
NumericalFailure=b.NumericalFailure
precision_context=b.precision_context
dec=b.dec;clean=b.clean;encoded=b.encoded;digest=b.digest
dot=b.dot;norm=b.norm;maxabs=b.maxabs;merit=b.merit;eye=b.eye
Jet=b.Jet;value=b.value;values=b.values


def own_identity():
    raw=Path(__file__).read_bytes()
    return dict(name=ENTRY,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def exact_parameters(values):
    if not isinstance(values,(list,tuple)) or len(values)!=10:
        raise ValueError('All ten explicitly declared physical coefficients are required')
    result=[dec(x) for x in values]
    if not all(x.is_finite() for x in result):
        raise NumericalFailure('A ten-control coefficient is nonfinite')
    return result


def _derived(function,replacements,namespace):
    raw=inspect.getsource(function);changed=raw;operations=[]
    for before,after,count in replacements:
        if changed.count(before)!=count:
            raise ValueError('The source-bound finite expression differs: '+before)
        changed=changed.replace(before,after)
        operations.append(dict(before=before,after=after,occurrences=count))
    space=dict(vars(b));space.update(namespace);space['__name__']=__name__
    exec(compile(textwrap.dedent(changed),str(HERE/ENTRY)+'::<'+function.__qualname__+'>','exec'),space)
    SOURCE_DERIVATIONS.append(dict(original_function=function.__qualname__,
        original_source_sha256=BASE_SHA,original_function_text_sha256=hashlib.sha256(raw.encode()).hexdigest(),
        derived_function_text_sha256=hashlib.sha256(changed.encode()).hexdigest(),operations=operations))
    return space[function.__name__]


class LiteralTenModel(b.LiteralCircleModel):
    def __init__(self,actual_nine_model,extended_original_model,family_identity,event_sink=None):
        require_actions()
        if (actual_nine_model.binding.get('parameter_dimension')!=9
                or len(actual_nine_model.x)!=699 or actual_nine_model.M!=112):
            raise ValueError('The parent is an actual complete original nine-coordinate model')
        if (extended_original_model.M!=112 or len(extended_original_model.x)!=699
                or tuple(extended_original_model.controls.shape)!=(699,2,10)
                or tuple(extended_original_model.controls_mid.shape)!=(698,2,10)):
            raise ValueError('The new literal family is independently complete699/112/10')
        self.event_sink=event_sink or (lambda event:None)
        self.counts=dict(primal_attempts=0,primal_returns=0,
            forward_attempts=0,forward_returns=0,forward_columns=0,exceptions=0)
        self.phase='unspecified'
        self.original_nine_binding=dict(actual_nine_model.binding)
        self.M=112;self.exactly_diagonal=actual_nine_model.exactly_diagonal
        self.x,self.h,self.mid=actual_nine_model.x,actual_nine_model.h,actual_nine_model.mid
        self.base,self.base_mid=actual_nine_model.base,actual_nine_model.base_mid
        self.J,self.target=actual_nine_model.J,actual_nine_model.target
        self.gamma,self.eh=actual_nine_model.gamma,actual_nine_model.eh
        # Byte binding only. The original finite controls are not recomputed
        # or modified, and native-J/mesh/base identity is not inferred from p.
        fields={'mesh':extended_original_model.x,'h':extended_original_model.h,
            'mid':extended_original_model.mid,'base':extended_original_model.base,
            'base_mid':extended_original_model.base_mid,
            'controls':extended_original_model.controls,'controls_mid':extended_original_model.controls_mid,
            'native_slope_J':extended_original_model.J,'target':extended_original_model.target,
            'frequency':extended_original_model.frequency}
        self.input_arrays={}
        for name,array in fields.items():
            if str(array.dtype)!='float64':
                raise ValueError('The original/new finite input must expose literal binary64 words: '+name)
            descriptor=dict(shape=list(array.shape),dtype=str(array.dtype),
                raw_C_order_sha256=hashlib.sha256(array.tobytes(order='C')).hexdigest(),
                exact_Decimal_from_float_lift=True)
            self.input_arrays[name]=descriptor
            if name not in ('controls','controls_mid') and descriptor!=actual_nine_model.input_arrays[name]:
                raise ValueError('A non-shape original coefficient array changed: '+name)
            if name in ('controls','controls_mid'):
                prefix=array[:,:,:9]
                prior=actual_nine_model.input_arrays[name]
                if (list(prefix.shape)!=prior['shape']
                        or hashlib.sha256(prefix.tobytes(order='C')).hexdigest()!=prior['raw_C_order_sha256']):
                    raise ValueError('The first nine literal control columns must remain the actual originals')
        self.controls=b.lift_nested(fields['controls'].tolist())
        self.controls_mid=b.lift_nested(fields['controls_mid'].tolist())
        self.binding=dict(schema=MODEL_SCHEMA,source=own_identity(),
            base_primal_source_sha256=BASE_SHA,
            original_nine_literal_binding=actual_nine_model.binding,
            independent_ten_control_family=family_identity,arrays=self.input_arrays,
            parameter_dimension=10,old_parameter_columns=list(range(9)),new_shape_column=9,
            parameter_order=list(extended_original_model.profile.description()['parameter_order']),
            decimal_digits=50,rounding='ROUND_HALF_EVEN',original_mesh_nodes=699,
            field_and_tail_modes=112,complete_original_tail_J_consumed=True,
            old_nine_helper_never_called_with_ten_coordinates=True,
            old_nine_parameter_words_not_projected_to_binary64=True,
            new_control_table_words_are_binary64_source_samples_then_exact_lifts=True,
            new_shape_table_formation_recomputed_in_Decimal=False,
            no_discrete_rounding_derivative_or_interval_accuracy_certificate=True,
            frozen_original_native_anchor_J_is_not_a_new_g_nonlinear_tail_response=True)
        self.binding['canonical_binding_sha256']=digest(self.binding)


LiteralTenModel._evaluate=_derived(b.LiteralCircleModel._evaluate,[
    ('                    row.append(y)',
     '                    y=y+p[9]*controls[j][k][9]\n'
     '                    row.append(y)',1),
    ('Same exact affine coefficient model as0865.',
     'Independent original-nine-plus-one affine coefficient model; old nine terms unchanged.',1)],globals())
LiteralTenModel.evaluate=_derived(b.LiteralCircleModel.evaluate,[],globals())
LiteralTenModel.response=_derived(b.LiteralCircleModel.response,[
    ("label='axis9'","label='axis10'",1),
    ('seed=eye(9)','seed=eye(10)',1),('len(seed)!=9','len(seed)!=10',1),
    ('Every forward seed has nine complete physical parameter rows',
     'Every forward seed has ten complete physical parameter rows',1),
    ('range(9)','range(10)',1),
    ('                complete112_response_canonical_sha256=digest(full_response),',
     '                complete112_response_canonical_sha256=digest(full_response),\n'
     '                complete112_response=full_response,\n'
     '                independent_ten_coordinate_model=True,',1)],globals())
LiteralTenModel.description=_derived(b.LiteralCircleModel.description,[
    ("description/fresh-forward-nine","description/fresh-forward-ten",1),
    ("all-nine-axis-columns","all-ten-axis-columns",1),
    ('range(9)','range(10)',1),
    ('all_nine_columns_attempted','all_ten_columns_attempted',1),
    ('all_nine_columns_checked','all_ten_columns_checked',1),
    ('complete_three_by_nine_forward_response','complete_three_by_ten_forward_response',1)],globals())


def extension_zero_readback(original_state,new_state):
    """Existing states only; do not reevaluate either scientific model here."""
    rows=[]
    for key in original_state:
        if key=='parameters':
            continue
        a,z=encoded(original_state[key]),encoded(new_state[key])
        rows.append(dict(field=key,original_bytes=len(a),new_bytes=len(z),
            original_sha256=hashlib.sha256(a).hexdigest(),new_sha256=hashlib.sha256(z).hexdigest(),
            encoded_words_equal=a==z))
    return dict(added_parameter='0',original_parameter_words=clean(original_state['parameters']),
        new_ten_parameter_words=clean(new_state['parameters']),fields=rows,
        all_recorded_encoded_words_equal=all(row['encoded_words_equal'] for row in rows),
        true_original_nine_and_independent_ten_states_evaluated_separately=True,
        diagnostic_only_not_an_acceptance_or_rank_gate=True)
