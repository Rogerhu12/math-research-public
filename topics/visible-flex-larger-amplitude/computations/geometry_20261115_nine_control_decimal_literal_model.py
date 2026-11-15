#!/usr/bin/env python3
"""Request149: one persistent50-decimal finite literal-coefficient primal.

All mesh/base/control/native-J words are lifted exactly from the original
binary64 model. This does not recompute their source integration or certify
a continuous metric. The complete radius chain, three2x2 mode transfers,
cut subtraction, all112 right rows, and seeded forward variations use one
explicit Decimal context. The derivative is the rounded forward variation
of the corresponding real expression, not a derivative of discrete rounding.
No scientific method is run by importing this module.
"""
from __future__ import annotations

from contextlib import contextmanager
from decimal import (Decimal as D, localcontext, getcontext, ROUND_HALF_EVEN,
                     InvalidOperation, DivisionByZero, Overflow, DecimalException)
import hashlib
import json
import math
import struct
import os
from pathlib import Path

PRECISION = 50
MODEL_SCHEMA = 'nine-control-persistent-decimal50-literal-circle-model-v1'
FAMILY_NAME = 'geometry_20261115_small_core_nine_control_family.py'
FAMILY_SHA = '086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629'
ZERO, ONE, TWO = D(0), D(1), D(2)
# These are the original binary64 algorithmic constants, not a new tolerance.
ARM = D.from_float(0.2)
TOL = D.from_float(1e-8)
EPS64 = D.from_float(float.fromhex('0x1.0000000000000p-52'))
FD_STEPS = tuple(D.from_float(x) for x in (2e-5, 1e-5, 5e-6))


class NumericalFailure(ArithmeticError):
    pass


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific computation is restricted to this public repository Actions')


@contextmanager
def precision_context():
    require_actions()
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_HALF_EVEN
        ctx.Emin, ctx.Emax = -999999, 999999
        for signal in (InvalidOperation, DivisionByZero, Overflow):
            ctx.traps[signal] = True
        yield ctx


def dec(value):
    if isinstance(value, D):
        return value
    if isinstance(value, bool):
        raise TypeError('Boolean is not a model coefficient')
    if isinstance(value, float):
        return D.from_float(value)
    if isinstance(value, (int, str)):
        return D(value)
    raise TypeError('A coefficient must be an exact binary64 lift or explicit decimal')


def clean(value):
    if isinstance(value, D):
        if not value.is_finite():
            return {'nonfinite_decimal': str(value)}
        return str(value)
    if isinstance(value, dict):
        return {str(k):clean(v) for k,v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    if hasattr(value, 'tolist'):
        return clean(value.tolist())
    if isinstance(value, float) and not math.isfinite(value):
        return dict(nonfinite_class=('NaN' if math.isnan(value) else
            ('positive-infinity' if value > 0 else 'negative-infinity')),
            binary64_big_endian_hex=struct.pack('>d', value).hex())
    if value is None or isinstance(value, (str, int, bool, float)):
        return value
    raise TypeError('Unexpected metadata type: '+type(value).__name__)


def encoded(value):
    return json.dumps(clean(value), sort_keys=True, ensure_ascii=True,
                      allow_nan=False, separators=(',', ':')).encode('utf-8')


def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def exact_parameters(values):
    if not isinstance(values, (tuple, list)) or len(values) != 9:
        raise ValueError('All nine parameters are required')
    p = [dec(v) for v in values]
    if not all(v.is_finite() for v in p):
        raise NumericalFailure('Nonfinite original design parameter')
    return p


def dot(a, b):
    if len(a) != len(b):
        raise ValueError('Dot dimensions differ')
    return sum((x*y for x,y in zip(a,b)), ZERO)


def norm(a):
    return dot(a,a).sqrt()


def maxabs(a):
    return max((abs(x) for x in a), default=ZERO)


def sub(a,b):
    if len(a) != len(b):
        raise ValueError('Vector dimensions differ')
    return [x-y for x,y in zip(a,b)]


def add(a,b):
    if len(a) != len(b):
        raise ValueError('Vector dimensions differ')
    return [x+y for x,y in zip(a,b)]


def scale(a,s):
    return [x*s for x in a]


def transpose(a):
    if not a:
        return []
    if any(len(r) != len(a[0]) for r in a):
        raise ValueError('Ragged matrix')
    return [list(c) for c in zip(*a)]


def mv(a,x):
    return [dot(r,x) for r in a]


def mm(a,b):
    bt = transpose(b)
    return [[dot(r,c) for c in bt] for r in a]


def eye(n):
    return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]


def merit(state):
    r = state['equation']
    if len(r) != 3:
        raise ValueError('Retain exactly the original three unweighted equations')
    return dot(r,r)/TWO


class Jet:
    """Forward columns through the actual real-expression arithmetic."""
    __slots__ = ('v','d')

    def __init__(self, value, derivative):
        self.v = dec(value)
        self.d = tuple(dec(x) for x in derivative)

    def paired(self, other):
        if isinstance(other, Jet):
            if len(other.d) != len(self.d):
                raise ValueError('Forward seed column count differs')
            return other
        return Jet(dec(other), [ZERO]*len(self.d))

    def __add__(self, other):
        o = self.paired(other)
        return Jet(self.v+o.v, [a+b for a,b in zip(self.d,o.d)])

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.v, [-a for a in self.d])

    def __sub__(self, other):
        o = self.paired(other)
        return Jet(self.v-o.v, [a-b for a,b in zip(self.d,o.d)])

    def __rsub__(self, other):
        return self.paired(other)-self

    def __mul__(self, other):
        o = self.paired(other)
        return Jet(self.v*o.v, [a*o.v+self.v*b for a,b in zip(self.d,o.d)])

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self.paired(other)
        if o.v == 0:
            raise NumericalFailure('Zero denominator in original finite real expression')
        value = self.v/o.v
        return Jet(value, [(a-value*b)/o.v for a,b in zip(self.d,o.d)])

    def __rtruediv__(self, other):
        return self.paired(other)/self

    def sqrt(self):
        if self.v <= 0:
            raise NumericalFailure('The selected square-root branch is not strictly positive')
        root = self.v.sqrt()
        return Jet(root, [a/(TWO*root) for a in self.d])


def value(x):
    return x.v if isinstance(x,Jet) else x


def values(x):
    if isinstance(x,Jet):
        return x.v
    if isinstance(x,dict):
        return {k:values(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [values(v) for v in x]
    return x


def sqrt_positive(x):
    if value(x) <= 0 or not value(x).is_finite():
        raise NumericalFailure('Original circle positive square-root domain failed')
    return x.sqrt()


def m2v(a,b):
    return [a[0][0]*b[0]+a[0][1]*b[1],
            a[1][0]*b[0]+a[1][1]*b[1]]


def m2m(a,b):
    return [[a[i][0]*b[0][j]+a[i][1]*b[1][j] for j in range(2)] for i in range(2)]


def solve2(a,b):
    determinant = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    if value(determinant) == 0 or not value(determinant).is_finite():
        raise NumericalFailure('The complete original two-by-two right cell is singular or nonfinite')
    return [(b[0]*a[1][1]-a[0][1]*b[1])/determinant,
            (a[0][0]*b[1]-b[0]*a[1][0])/determinant]


def lift_nested(a):
    if isinstance(a,(tuple,list)):
        return [lift_nested(x) for x in a]
    return dec(a)


class LiteralCircleModel:
    def __init__(self, original_model, event_sink=None):
        require_actions()
        self.event_sink = event_sink or (lambda event:None)
        self.counts = dict(primal_attempts=0,primal_returns=0,
            forward_attempts=0,forward_returns=0,forward_columns=0,exceptions=0)
        self.phase = 'unspecified'
        if original_model.M != 112 or len(original_model.x) != 699:
            raise ValueError('Bind this experiment to the complete original699/112 model')
        fields = {'mesh':original_model.x,'h':original_model.h,'mid':original_model.mid,
                  'base':original_model.base,'base_mid':original_model.base_mid,
                  'controls':original_model.controls,'controls_mid':original_model.controls_mid,
                  'native_slope_J':original_model.J,'target':original_model.target,
                  'frequency':original_model.frequency}
        self.input_arrays = {}
        for name,array in fields.items():
            if str(array.dtype) != 'float64':
                raise ValueError('Bind the original literal binary64 input array: '+name)
            self.input_arrays[name] = dict(shape=list(array.shape),dtype=str(array.dtype),
                raw_C_order_sha256=hashlib.sha256(array.tobytes(order='C')).hexdigest(),
                exact_Decimal_from_float_lift=True)
        if list(original_model.frequency) != [2.,4.,6.]:
            raise ValueError('Keep the original three low mode frequencies')
        self.x,self.h,self.mid = (lift_nested(fields[k].tolist()) for k in ('mesh','h','mid'))
        self.base,self.base_mid = (lift_nested(fields[k].tolist()) for k in ('base','base_mid'))
        self.controls,self.controls_mid = (lift_nested(fields[k].tolist()) for k in ('controls','controls_mid'))
        self.J,self.target = (lift_nested(fields[k].tolist()) for k in ('native_slope_J','target'))
        self.gamma,self.eh = dec(float(original_model.gamma)),dec(float(original_model.eh))
        self.M = 112
        self.exactly_diagonal = original_model.exactly_diagonal
        self.binding = dict(schema=MODEL_SCHEMA,decimal_digits=PRECISION,
            rounding='ROUND_HALF_EVEN',arrays=self.input_arrays,
            cut_scale_exact_binary64_lift=self.gamma,height_sign_exact_binary64_lift=self.eh,
            original_three_frequencies=[2,4,6],parameter_dimension=9,
            original_mesh_nodes=699,field_and_tail_modes=112,
            complete_original_tail_J_consumed=True,exactly_diagonal_as_original_record=bool(self.exactly_diagonal),
            input_table_formation_recomputed_in_higher_precision=False,
            continuous_metric_or_interval_roundoff_certificate_claimed=False,
            solve2_is_same_real_linear_system_not_the_old_LAPACK_rounding_path=True,
            forward_is_real_expression_variation_not_discrete_rounding_derivative=True)
        self.binding['canonical_binding_sha256'] = digest(self.binding)

    @contextmanager
    def context(self, name):
        old = self.phase
        self.phase = name
        try:
            yield
        finally:
            self.phase = old

    def matrix(self,q,r,s,z):
        answer=[]
        for i in range(len(r)):
            row=[]
            for k in (4,16,36):
                row.append([[q[i]*(1-k),-z[i]*k/r[i]],
                    [s[i]*q[i]/z[i]*(k-1),q[i]*k]])
            answer.append(row)
        return answer

    def _evaluate(self,p):
        # Same exact affine coefficient model as0865. The original explicit
        # odd ordering is theta2,theta1,theta3, then eta1,eta2,eta3. The first
        # three-term sum is re-evaluated here, not claimed old einsum word-equal.
        def formed(base,controls):
            result=[]
            for j in range(len(base)):
                row=[]
                for k in range(2):
                    y=base[j][k]+sum((controls[j][k][i]*p[i] for i in range(3)),ZERO)
                    for i in (4,3,5,6,7,8):
                        y=y+p[i]*controls[j][k][i]
                    row.append(y)
                result.append(row)
            return result
        nodes,middle=formed(self.base,self.controls),formed(self.base_mid,self.controls_mid)
        for row in nodes+middle:
            if (not all(value(x).is_finite() for x in row)
                    or value(row[0]) <= 0 or abs(value(row[1])) >= 1):
                raise NumericalFailure('Original node/mid scalar radius/ap domain failed')
        q=[a[1]/a[0] for a in nodes]
        qm=[a[1]/a[0] for a in middle]
        left=[];right=[]
        for j,h in enumerate(self.h):
            left.append(-ONE-h*(q[j]+TWO*qm[j])/6-h*h*qm[j]*q[j]/12)
            right.append(ONE-h*(q[j+1]+TWO*qm[j])/6+h*h*qm[j]*q[j+1]/12)
            if value(right[-1]) == 0 or not value(right[-1]).is_finite():
                raise NumericalFailure('The original circle radius cell cannot be eliminated')
        radius=[ONE]
        for j in range(len(self.h)):
            radius.append(-left[j]*radius[j]/right[j])
        radius_mid=[(radius[j]+radius[j+1])/TWO
            -h*(q[j+1]*radius[j+1]-q[j]*radius[j])/8 for j,h in enumerate(self.h)]
        speed=[a*b for a,b in zip(q,radius)]
        speed_mid=[a*b for a,b in zip(qm,radius_mid)]
        margin=[ONE-a*a for a in speed]
        margin_mid=[ONE-a*a for a in speed_mid]
        for r in radius+radius_mid:
            if not value(r).is_finite() or value(r) <= 0:
                raise NumericalFailure('The source circle radius left its original positive domain')
        vertical=[sqrt_positive(x) for x in margin]
        vertical_mid=[sqrt_positive(x) for x in margin_mid]
        height=[ZERO]
        for j,h in enumerate(self.h):
            height.append(height[-1]+h*(vertical[j]+vertical[j+1]+4*vertical_mid[j])/6)
        B,Bm=self.matrix(q,radius,speed,vertical),self.matrix(qm,radius_mid,speed_mid,vertical_mid)
        L=[];R=[];modes=[[[ONE,ZERO] for unused in range(3)]]
        for j,h in enumerate(self.h):
            lj=[];rj=[];mj=[]
            for mode in range(3):
                bleft,bright,bmid=B[j][mode],B[j+1][mode],Bm[j][mode]
                ml,mr=m2m(bmid,bleft),m2m(bmid,bright)
                l=[[-(ONE if a==b else ZERO)-h*(bleft[a][b]+TWO*bmid[a][b])/6
                     -h*h*ml[a][b]/12 for b in range(2)] for a in range(2)]
                r=[[(ONE if a==b else ZERO)-h*(bright[a][b]+TWO*bmid[a][b])/6
                     +h*h*mr[a][b]/12 for b in range(2)] for a in range(2)]
                rhs=[-x for x in m2v(l,modes[-1][mode])]
                solved=solve2(r,rhs)
                if not all(value(x).is_finite() for x in solved):
                    raise NumericalFailure('The complete low-mode transfer is nonfinite')
                lj.append(l);rj.append(r);mj.append(solved)
            L.append(lj);R.append(rj);modes.append(mj)
        velocity=[[m2v(B[j][k],modes[j][k]) for k in range(3)] for j in range(len(self.x))]
        if not all(value(x).is_finite() for row in velocity for pair in row for x in pair):
            raise NumericalFailure('The complete low-mode velocity is nonfinite')
        native=[ZERO]*self.M
        for k in range(3):
            native[k]=self.eh*self.target[k]*modes[-1][k][1]
        full=[-self.gamma*sum((self.J[j][k]*native[k] for k in range(self.M)),ZERO)
              for j in range(self.M)]
        for k in range(3):
            full[k]=full[k]+self.target[k]*velocity[-1][k][1]
        unit=[velocity[-1][k][1]-self.gamma*self.eh*self.J[k][k]*modes[-1][k][1]
              for k in range(3)]
        equation=unit if self.exactly_diagonal else full[:3]
        return dict(parameters=p,scalar_nodes=nodes,scalar_middle=middle,
            radius=radius,radius_mid=radius_mid,radius_rhs=speed,
            height=height,height_rhs=vertical,ratio=q,ratio_mid=qm,
            vertical_mid=vertical_mid,margin=margin,margin_mid=margin_mid,
            modes=modes,velocity=velocity,L=L,R=R,B=B,Bmid=Bm,
            radius_left=left,radius_right=right,full_right=full,
            native_first_order_height=native,low_right=full[:3],
            unit_diagonal_defect=unit,equation=equation)

    def evaluate(self, parameters):
        require_actions()
        if getcontext().prec != PRECISION or getcontext().rounding != ROUND_HALF_EVEN:
            raise RuntimeError('The complete primal must remain in its declared Decimal context')
        p=exact_parameters(parameters)
        event=dict(kind='decimal-primal',phase=self.phase,parameters=p,
            index=self.counts['primal_attempts'],returned=False)
        self.counts['primal_attempts']+=1
        try:
            state=self._evaluate(p)
            if not all(x.is_finite() for x in state['equation']+state['full_right']):
                raise NumericalFailure('The complete high-precision right residual is nonfinite')
            self.counts['primal_returns']+=1
            event.update(returned=True,equation=state['equation'],full_right=state['full_right'],
                         unweighted_full3_merit=merit(state))
            return state
        except (DecimalException,NumericalFailure) as error:
            self.counts['exceptions']+=1
            event['exception']=repr(error)
            raise NumericalFailure(str(error)) from error
        finally:
            self.event_sink(event)

    def response(self, parameters, seed=None, label='axis9'):
        require_actions()
        p=exact_parameters(parameters)
        seed=eye(9) if seed is None else seed
        if len(seed)!=9 or not seed[0] or any(len(r)!=len(seed[0]) for r in seed):
            raise ValueError('Every forward seed has nine complete physical parameter rows')
        seed=[[dec(x) for x in row] for row in seed]
        if not all(x.is_finite() for row in seed for x in row):
            raise NumericalFailure('Nonfinite complete forward seed')
        ncol=len(seed[0])
        event=dict(kind='decimal-forward',phase=self.phase,label=label,parameters=p,
            seed=seed,seed_columns=ncol,index=self.counts['forward_attempts'],returned=False)
        self.counts['forward_attempts']+=1;self.counts['forward_columns']+=ncol
        try:
            if getcontext().prec != PRECISION or getcontext().rounding != ROUND_HALF_EVEN:
                raise RuntimeError('Forward/primal contexts must be identical')
            jets=[Jet(p[i],seed[i]) for i in range(9)]
            all_state=self._evaluate(jets)
            state=values(all_state)
            response=[list(x.d) if isinstance(x,Jet) else [ZERO]*ncol
                      for x in all_state['equation']]
            full_response=[list(x.d) if isinstance(x,Jet) else [ZERO]*ncol
                           for x in all_state['full_right']]
            if not all(x.is_finite() for row in response+full_response for x in row):
                raise NumericalFailure('The complete forward variation is nonfinite')
            self.counts['forward_returns']+=1
            report=dict(label=label,actual_parameters=p,physical_seed=seed,
                forward_column_count=ncol,equation_from_same_primal=state['equation'],
                complete_three_row_response=response,
                complete112_response_shape=[self.M,ncol],
                complete112_response_canonical_sha256=digest(full_response),
                all_native_J_rows_and_columns_consumed=True,
                same_primal_expression=True,parameter_projection_to_binary64=False,
                complex_primal_path_used=False,implicit_root_derivative_used=False,
                discrete_rounding_map_derivative_claimed=False,
                exact_derivative_or_interval_accuracy_certificate_claimed=False)
            event.update(returned=True,equation=state['equation'],response=response,
                         full_response_sha256=report['complete112_response_canonical_sha256'])
            return response,report,state
        except (DecimalException,NumericalFailure) as error:
            self.counts['exceptions']+=1;event['exception']=repr(error)
            raise NumericalFailure(str(error)) from error
        finally:
            self.event_sink(event)

    def description(self, state):
        p=state['parameters']
        with self.context('description/fresh-forward-nine'):
            J,jr,forward_state=self.response(p,label='all-nine-axis-columns')
        levels=[]
        for step in FD_STEPS:
            checks=[]
            for column in range(9):
                check=dict(column=column,step=step,valid=False)
                checks.append(check)
                pp=list(p);pm=list(p);pp[column]+=step;pm[column]-=step
                try:
                    with self.context('description/central-difference/column-'+str(column)):
                        plus,minus=self.evaluate(pp),self.evaluate(pm)
                    numerical=[(a-b)/(TWO*step) for a,b in zip(plus['equation'],minus['equation'])]
                    err=maxabs([numerical[i]-J[i][column] for i in range(3)])
                    relative=err/max(ONE,maxabs([J[i][column] for i in range(3)]))
                    check.update(valid=True,positive_parameters=pp,negative_parameters=pm,
                        positive_equations=plus['equation'],negative_equations=minus['equation'],
                        complete_three_row_difference=numerical,relative_error=relative)
                except NumericalFailure as error:
                    check['exception']=repr(error)
            valid=all(x['valid'] for x in checks)
            levels.append(dict(step=step,valid=valid,all_nine_columns_attempted=True,
                all_nine_columns_checked=valid,checks_by_parameter=checks,
                maximum_relative_error=max(x['relative_error'] for x in checks) if valid else None))
        terminal=[]
        for k in range(3):
            a=state['velocity'][-1][k][1]
            b=self.gamma*self.eh*self.J[k][k]*state['modes'][-1][k][1]
            terminal.append(dict(mode=k+1,actual_cut_mode=state['modes'][-1][k],
                actual_cut_velocity=state['velocity'][-1][k],
                Robin_first_term=a,Robin_second_term=b,actual_unit_subtraction=state['unit_diagonal_defect'][k],
                unsigned_term_sum=abs(a)+abs(b),not_a_condition_or_roundoff_bound=True))
        return dict(parameters=p,parameter_encoding='finite-decimal-strings',
            unweighted_full3_merit=merit(state),low_equations_used=state['equation'],
            unit_diagonal_defects=state['unit_diagonal_defect'],
            complete_first_order_right_residual=state['full_right'],
            complete_first_order_native_height=state['native_first_order_height'],
            complete_three_by_nine_forward_response=J,
            forward_response_report=jr,
            forward_primal_equation_words_equal_to_real_state=
                [str(x) for x in forward_state['equation']]==[str(x) for x in state['equation']],
            independent_high_precision_real_parameter_difference_checks=levels,
            terminal_Robin_terms=terminal,
            low_mode_trajectory_max_by_mode=[max(abs(x) for row in state['modes'] for x in row[k]) for k in range(3)],
            scalar_node_and_mid_minimum_radius=min(a[0] for a in state['scalar_nodes']+state['scalar_middle']),
            source_circle_node_and_mid_minimum_radius=min(state['radius']+state['radius_mid']),
            source_circle_node_and_mid_minimum_beta2=min(state['margin']+state['margin_mid']),
            radius_cell_denominator_minimum_absolute=min(abs(x) for x in state['radius_right']),
            high_right_leak_max=maxabs(state['full_right'][3:]),
            high_free_core_Schur_elimination_computed=False,
            high_mode_nonresonance_proved=False,
            same_literal_coefficient_model_not_reformed_continuous_metric=True,
            raw_original_table_accuracy_not_certified=True,
            derivative_accuracy_or_exact_rank_not_certified=True)
