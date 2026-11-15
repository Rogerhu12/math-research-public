#!/usr/bin/env python3
"""Request154: full second forward variation of the unchanged149 literal primal.

The original50-decimal values and first-derivative operation order are retained.
All45 symmetric Hessian entries of every nine-parameter intermediate propagate;
no Hessian-vector sampling, normal-equation surrogate, or weak-column truncation.
These are rounded derivatives of the real expression, not derivatives of IEEE
rounding or interval certificates. Scientific evaluation is Actions-only.
"""
from __future__ import annotations
from decimal import DecimalException, getcontext, ROUND_HALF_EVEN
import geometry_20261115_nine_control_decimal_literal_model as original
from geometry_20261115_nine_control_decimal_literal_model import *

BASE_NAME = 'geometry_20261115_nine_control_decimal_literal_model.py'
BASE_SHA = '2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75'
SECOND_SCHEMA = 'nine-control-decimal50-complete-second-forward-v1'
PAIRS = tuple((i,j) for i in range(9) for j in range(i,9))


class SecondJet(original.Jet):
    """Full9 first columns and45 upper-triangle second columns, all Decimal."""
    __slots__ = ('h',)

    def __init__(self, v, d, h):
        super().__init__(v,d)
        self.h = tuple(dec(x) for x in h)
        if len(self.d)!=9 or len(self.h)!=45:
            raise ValueError('Every second jet retains all9 axes and45 pairs')

    def paired(self, other):
        if isinstance(other,SecondJet):
            return other
        if isinstance(other,original.Jet):
            raise TypeError('Do not silently discard another forward object Hessian')
        return SecondJet(dec(other),[ZERO]*9,[ZERO]*45)

    def __add__(self,other):
        b=self.paired(other)
        return SecondJet(self.v+b.v,[x+y for x,y in zip(self.d,b.d)],
                         [x+y for x,y in zip(self.h,b.h)])

    __radd__=__add__

    def __neg__(self):
        return SecondJet(-self.v,[-x for x in self.d],[-x for x in self.h])

    def __sub__(self,other):
        b=self.paired(other)
        return SecondJet(self.v-b.v,[x-y for x,y in zip(self.d,b.d)],
                         [x-y for x,y in zip(self.h,b.h)])

    def __rsub__(self,other):
        return self.paired(other)-self

    def __mul__(self,other):
        b=self.paired(other)
        # The v,d expressions are exactly the original149 Jet expressions.
        d=[a*b.v+self.v*z for a,z in zip(self.d,b.d)]
        h=[self.h[k]*b.v+self.d[i]*b.d[j]+self.d[j]*b.d[i]+self.v*b.h[k]
           for k,(i,j) in enumerate(PAIRS)]
        return SecondJet(self.v*b.v,d,h)

    __rmul__=__mul__

    def __truediv__(self,other):
        b=self.paired(other)
        if b.v==0:
            raise NumericalFailure('Zero denominator in original finite expression')
        v=self.v/b.v
        d=[(a-v*z)/b.v for a,z in zip(self.d,b.d)]
        h=[(self.h[k]-d[i]*b.d[j]-d[j]*b.d[i]-v*b.h[k])/b.v
           for k,(i,j) in enumerate(PAIRS)]
        return SecondJet(v,d,h)

    def __rtruediv__(self,other):
        return self.paired(other)/self

    def sqrt(self):
        if self.v<=0:
            raise NumericalFailure('The selected square-root branch is not strictly positive')
        v=self.v.sqrt()
        d=[a/(TWO*v) for a in self.d]
        h=[(self.h[k]-TWO*d[i]*d[j])/(TWO*v) for k,(i,j) in enumerate(PAIRS)]
        return SecondJet(v,d,h)


def second_columns(x):
    if not isinstance(x,SecondJet):
        return [ZERO]*9,[[ZERO]*9 for unused in range(9)]
    h=[[ZERO]*9 for unused in range(9)]
    for k,(i,j) in enumerate(PAIRS):
        h[i][j]=h[j][i]=x.h[k]
    return list(x.d),h


class LiteralCircleModel(original.LiteralCircleModel):
    """Original149 evaluator/response with an additional full second method."""
    def __init__(self,original_model,event_sink=None):
        super().__init__(original_model,event_sink)
        self.counts.update(second_forward_attempts=0,second_forward_returns=0,
                           second_forward_axes=0,second_forward_symmetric_pairs=0)
        self.binding['original149_literal_model_binding_sha256']=self.binding['canonical_binding_sha256']
        self.binding.update(second_variation_schema=SECOND_SCHEMA,
            original149_primal_body_reused_without_replacement=True,
            original149_primal_source_sha256=BASE_SHA,
            second_variation_all9_axes_and45_pairs=True,
            actual_binary64_input_table_words_still_only_lifted=True)
        self.binding['canonical_binding_sha256']=digest({k:v for k,v in self.binding.items()
                                                       if k!='canonical_binding_sha256'})

    def curvature(self,parameters,label='complete-nine-second-forward'):
        require_actions()
        if getcontext().prec!=PRECISION or getcontext().rounding!=ROUND_HALF_EVEN:
            raise RuntimeError('Keep original50-decimal context for all second variations')
        p=exact_parameters(parameters)
        event=dict(kind='decimal-second-forward',phase=self.phase,label=label,
            parameters=p,index=self.counts['second_forward_attempts'],returned=False,
            first_axes=9,symmetric_second_pairs=45,all_physical_parameters_retained=True)
        self.counts['second_forward_attempts']+=1
        self.counts['second_forward_axes']+=9
        self.counts['second_forward_symmetric_pairs']+=45
        try:
            seeds=eye(9)
            state2=self._evaluate([SecondJet(p[i],seeds[i],[ZERO]*45) for i in range(9)])
            state=original.values(state2)
            columns=[second_columns(x) for x in state2['equation']]
            J=[x[0] for x in columns];H=[x[1] for x in columns]
            full_columns=[second_columns(x) for x in state2['full_right']]
            full_J=[x[0] for x in full_columns];full_H=[x[1] for x in full_columns]
            all_values=(state['equation']+state['full_right']+
                [x for row in full_J for x in row]+
                [x for hh in full_H for row in hh for x in row]+
                [x for hh in H for row in hh for x in row])
            if not all(x.is_finite() for x in all_values):
                raise NumericalFailure('A complete second response is nonfinite')
            report=dict(schema=SECOND_SCHEMA,parameters=p,
                complete_three_equations=state['equation'],complete_full112_right=state['full_right'],
                complete_three_by_nine_J=J,complete_three_by_nine_by_nine_H=H,
                complete_full112_by_nine_J=full_J,
                complete_full112_by_nine_by_nine_H=full_H,
                complete112_J_sha256=digest(full_J),complete112_H_sha256=digest(full_H),
                equation_Hessian_shape=[3,9,9],full_right_Hessian_shape=[112,9,9],
                symmetric_pair_order=[list(pair) for pair in PAIRS],
                primal_body_is_original149=True,all112_native_rows_and_columns_consumed=True,
                finite_second_variation_of_real_expression=True,
                discrete_rounding_derivative_or_interval_certificate=False,
                continuous_metric_coefficients_recomputed=False,
                parameter_or_state_projection_to_binary64=False,
                singular_or_weak_axes_discarded=False)
            self.counts['second_forward_returns']+=1
            event.update(returned=True,equation=state['equation'],
                full_right=state['full_right'],complete_second_report_sha256=digest(report))
            return J,H,report,state
        except (DecimalException,NumericalFailure) as error:
            self.counts['exceptions']+=1
            event['exception']=repr(error)
            raise NumericalFailure(str(error)) from error
        finally:
            self.event_sink(event)

    def second_difference_checks(self,parameters,reference_H,label,checks=None,checkpoint=None):
        """Three actual real steps, every9 axis, all3x9 response entries.

        This uses original first forward responses at p+-h e_j, not this second
        routine a second time. It is diagnostic only and is never a candidate
        or derivative-accuracy acceptance gate. A failed column is retained and
        remaining columns/steps are still attempted.
        """
        require_actions();p=exact_parameters(parameters)
        checks=[] if checks is None else checks
        checkpoint=checkpoint or (lambda:None)
        for step in FD_STEPS:
            row=dict(step=step,checks_by_parameter=[],valid=True,
                     all_nine_axes_attempted=False,maximum_relative_error=None,
                     comparison_uses_full_three_by_nine_first_responses=True,
                     adds_no_candidate_acceptance_gate=True)
            checks.append(row);checkpoint()
            errors=[]
            for axis in range(9):
                h=step*max(ONE,abs(p[axis]));plus=list(p);minus=list(p)
                plus[axis]+=h;minus[axis]-=h
                item=dict(parameter=axis,actual_step=h,plus_parameters=plus,
                          minus_parameters=minus,attempted=True,complete=False,valid=False)
                row['checks_by_parameter'].append(item)
                checkpoint()
                try:
                    with self.context(label+'/step-'+str(step)+'/axis-'+str(axis)+'/plus'):
                        jp,rp,sp=self.response(plus,label='all9-first-forward-at-plus')
                    item.update(plus_response=jp,plus_equations=sp['equation'],
                                plus_response_report=rp)
                    checkpoint()
                    with self.context(label+'/step-'+str(step)+'/axis-'+str(axis)+'/minus'):
                        jm,rm,sm=self.response(minus,label='all9-first-forward-at-minus')
                    difference=[[(jp[i][j]-jm[i][j])/(TWO*h) for j in range(9)]
                                for i in range(3)]
                    reference=[[reference_H[i][j][axis] for j in range(9)] for i in range(3)]
                    discrepancy=[[difference[i][j]-reference[i][j] for j in range(9)] for i in range(3)]
                    relative=norm([x for rr in discrepancy for x in rr])/max(
                        ONE,norm([x for rr in reference for x in rr]))
                    item.update(minus_response=jm,minus_equations=sm['equation'],
                        minus_response_report=rm,actual_centered_second_column=difference,
                        original_second_forward_column=reference,
                        actual_column_difference=discrepancy,relative_error=relative,
                        valid=relative.is_finite(),complete=True)
                    if relative.is_finite():
                        errors.append(relative)
                    else:
                        row['valid']=False
                except (NumericalFailure,DecimalException) as error:
                    item['exception']=repr(error);item['complete']=True;row['valid']=False
                checkpoint()
            row['all_nine_axes_attempted']=len(row['checks_by_parameter'])==9
            row['all_nine_axes_checked']=all(x['valid'] for x in row['checks_by_parameter'])
            if row['valid'] and len(errors)==9:
                row['maximum_relative_error']=max(errors)
            checkpoint()
        return checks
