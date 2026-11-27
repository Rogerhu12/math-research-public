#!/usr/bin/env python3
"""Same fixed-E numerical chain with an explicit large-centre/small-offset root.

The source field, angular functional, and real equations are unchanged. All
Decimal inputs are exact conversions of the actual binary64 jets, not a
promotion of an already-rounded B. Decimal arithmetic is numerical evaluation,
not outward interval certification of source, angular, or rounding errors.
Only declared public Actions may construct or execute this object.
"""
from collections import defaultdict
from decimal import Decimal, getcontext, localcontext
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np


SCHEMA = 'r618-same-E-split-reference-decimal-mean-chain-v1'
ORIGINAL_CHAIN_SHA = '0668d1afbcdcd5e0c0c16d3784c322d6e0bba3639c547d8ae0bd42900ff09815'
ZERO, ONE, TWO = Decimal(0), Decimal(1), Decimal(2)


def decimal_input(value):
    if isinstance(value, Decimal):
        return value
    if isinstance(value, str):
        return Decimal(value)
    value = float(value)
    if not math.isfinite(value):
        raise ArithmeticError('nonfinite actual scalar/jet input')
    return Decimal.from_float(value)


def mean(values):
    return sum(values, ZERO)/Decimal(len(values))


class SplitReferenceMeanChain:
    @staticmethod
    def policy_descriptor():
        return {
            'schema':SCHEMA,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'original_chain_sha256':ORIGINAL_CHAIN_SHA,
            'decimal_min_precision':80,
            'decimal_max_precision':2048,
            'decimal_guard_digits':30,
            'decimal_precision_uses_actual_expression_and_reciprocal_scales':True,
            'absolute_coordinate_budget':1.e-13,
            'reference_max_steps':256,
            'trial_max_steps':192,
            'reference_derivative_margin_fraction':.01,
            'reference_error_safety_factor':8,
            'reference_and_trial_never_recombine_split_as_binary64':True,
            'actual_float_jets_converted_before_B_and_all_root_means':True,
            'connection_and_output_preserve_decimal_e_E_er_and_mean_sr':True,
            'original_analytic_jacobian_uses_final_binary64_state_and_is_not_high_precision':True,
            'same_continuous_E_and_original_angular_functional':True,
            'source_angular_and_decimal_roundoff_errors_are_not_certified':True,
        }

    def __init__(self, original_chain, numeric_policy, check_clock):
        original_chain.public_only()
        if (hashlib.sha256(Path(original_chain.__file__).read_bytes()).hexdigest()
                != ORIGINAL_CHAIN_SHA or numeric_policy != self.policy_descriptor()):
            raise ValueError('actual original chain and complete split policy required')
        if not callable(check_clock):
            raise TypeError('actual scientific-clock callback required')
        self.original_chain = original_chain
        self.policy = dict(numeric_policy)
        self.check_clock = check_clock
        self.counts = defaultdict(int)
        self.attempts = []
        self.counts['source_bound_split_chains'] = 1

    def _float(self,value):
        result = float(value)
        if not math.isfinite(result):
            raise ArithmeticError('Decimal geometry cannot be represented by the existing finite array interface')
        if result == 0 and value != 0:
            self.counts['decimal_to_binary64_underflow_observations'] += 1
        return result

    def root_attempt_receipts(self):
        return {'retention_limit':16,'last_actual_attempts':json.loads(json.dumps(self.attempts)),
            'complete_work_counters':dict(self.counts),
            'full_scalar_trajectories_or_scientific_arrays_saved':False}

    def _jets(self,jets):
        original = self.original_chain._jets(jets)
        converted = {key:tuple(decimal_input(v) for v in value) for key,value in original.items()}
        self.counts['actual_binary64_jet_scalars_converted_to_decimal'] += sum(map(len,converted.values()))
        return original,converted

    def _precision(self,values,*,divisors=(),derivative=None):
        exponent = max((abs(v).adjusted() for v in values if v),default=0)
        denominator_loss = max((max(0,-abs(v).adjusted()) for v in divisors if v),default=0)
        derivative_loss = 0 if derivative is None or not derivative else max(0,-abs(derivative).adjusted())
        digits = max(0,-decimal_input(self.policy['absolute_coordinate_budget']).adjusted())
        required = max(self.policy['decimal_min_precision'],
            max(0,exponent)+digits+self.policy['decimal_guard_digits']+denominator_loss+derivative_loss)
        if required > self.policy['decimal_max_precision']:
            raise ArithmeticError('actual normalized root exceeds the declared Decimal precision capacity')
        self.counts['maximum_decimal_precision_used'] = max(
            self.counts['maximum_decimal_precision_used'],required)
        return required

    def _root(self,evaluate,left,right,sign,seed,steps,tolerance,counter,
              *,monotone_reference_derivative=False):
        """Absolute-coordinate bracketing, with source errors kept unresolved."""
        self.check_clock()
        left,right,seed,tolerance = map(decimal_input,(left,right,seed,tolerance))
        if left > right or tolerance <= 0 or sign not in (-1,1):
            raise ValueError('finite absolute-coordinate bracket required')
        rec = {'counter':counter,'initial_bracket_decimal':[str(left),str(right)],
            'absolute_coordinate_tolerance_decimal':str(tolerance),'maximum_iterations':int(steps),
            'evaluations':0,'bisection_candidates':0,'status':'started',
            'source_angular_and_roundoff_errors_enclosed':False,
            'bracket_signs_are_numerical_observations_not_interval_certificates':True}
        self.attempts.append(rec)
        if len(self.attempts)>16:
            del self.attempts[0]
        self.counts['decimal_scalar_root_attempts'] += 1

        def call(x):
            self.check_clock()
            self.counts['decimal_scalar_function_evaluations'] += 1
            self.original_chain.COUNTS[counter] += 1
            rec['evaluations'] += 1
            rec['last_attempted_coordinate_decimal'] = str(x)
            value,derivative,payload = evaluate(x)
            if not value.is_finite() or not derivative.is_finite() or sign*derivative <= 0:
                raise ArithmeticError('same Decimal scalar derivative/finite branch lost')
            rec['last_residual_decimal'],rec['last_derivative_decimal'] = str(value),str(derivative)
            return value,derivative,payload

        def finish(x,f,d,payload,reason,iterations):
            rec.update(status='completed',stop_reason=reason,iterations=iterations,
                bracket_decimal=[str(left),str(right)],bracket_width_decimal=str(right-left),
                returned_coordinate_decimal=str(x),residual_decimal=str(f),derivative_decimal=str(d))
            self.counts['decimal_scalar_roots_completed'] += 1
            self.counts['decimal_scalar_stop_'+reason] += 1
            return x,payload,dict(rec)

        try:
            fl,dl,pl = call(left)
            fr,dr,pr = call(right)
            if sign*fl > 0 or sign*fr < 0:
                raise ArithmeticError('actual Decimal endpoints do not bracket the scalar root')
            if left == right:
                if fl != 0:
                    raise ArithmeticError('single-point Decimal bracket has nonzero residual')
                return finish(left,fl,dl,pl,'single_point_decimal_zero_observation',0)
            x = min(max(seed,left),right)
            f,d,payload = call(x)
            if monotone_reference_derivative and f != 0:
                # For the reference scalar, -F_x=.5*mean(N/u^3) is
                # decreasing in x. Its endpoint bounds are already paid.
                low,high = min(abs(dl),abs(dr)),max(abs(dl),abs(dr))
                signed = sign*f
                if signed > 0:
                    a,b = x-signed/low,x-signed/high
                else:
                    a,b = x-signed/high,x-signed/low
                a,b = max(left,a.next_minus()),min(right,b.next_plus())
                self.counts['reference_mean_value_bracket_contractions_attempted'] += 1
                if a <= b:
                    fa,da,pa = call(a);fb,db,pb = call(b)
                    if sign*fa <= 0 and sign*fb >= 0:
                        left,right,fl,fr,dl,dr,pl,pr = a,b,fa,fb,da,db,pa,pb
                        x = min(max(x,left),right)
                        f,d,payload = call(x)
                        self.counts['reference_mean_value_bracket_contractions_used'] += 1
            for iteration in range(steps):
                if right-left <= tolerance:
                    return finish(x,f,d,payload,'declared_absolute_coordinate_width',iteration+1)
                if f == 0:
                    # Do not turn a zero rounded residual into a fabricated
                    # zero-width interval. Query an actual small bracket.
                    a = max(left,x-tolerance/4)
                    b = min(right,x+tolerance/4)
                    if a == b:
                        raise ArithmeticError('Decimal coordinate cannot resolve its declared absolute budget')
                    fa,da,pa = call(a);fb,db,pb = call(b)
                    if sign*fa <= 0 and sign*fb >= 0:
                        left,right = a,b
                        return finish(x,f,d,payload,'decimal_zero_with_observed_small_bracket',iteration+1)
                    raise ArithmeticError('rounded Decimal zero has no observed bracket at the requested budget')
                if sign*f < 0:
                    left,fl,dl,pl = x,f,d,payload
                else:
                    right,fr,dr,pr = x,f,d,payload
                candidate = left+(right-left)/2
                if candidate == left or candidate == right:
                    raise ArithmeticError('Decimal bracket resolution exhausted before the absolute budget')
                self.counts['decimal_scalar_bisection_candidates'] += 1
                rec['bisection_candidates'] += 1
                x = candidate
                f,d,payload = call(x)
            raise ArithmeticError('same Decimal scalar root exhausted its declared iterations')
        except Exception as error:
            rec.update(status='failed',error_type=type(error).__name__,error=str(error),
                bracket_decimal=[str(left),str(right)],bracket_width_decimal=str(right-left))
            self.counts['decimal_scalar_root_failures'] += 1
            raise

    def _reference_arrays(self,r,W,j,inner):
        scale2 = W*W if inner else ONE
        if scale2 == 0:
            raise ArithmeticError('positive reference scale lost in Decimal arithmetic')
        rows = []
        for q,t,fr in zip(j['ft'],j['ftt'],j['fr']):
            b2 = r*r-q*q
            if b2 <= 0:
                raise ArithmeticError('same reference angular graph lost positivity')
            b = b2.sqrt();p = -W+fr
            if inner:
                v = fr/W
                n = (q/W)**2/(b*(r+b))+r*r*(v-1)*(t/W)/(b**3)
                S = -2*v+v*v+(v-1)**2*q*q/b2
            else:
                n = q*q/(b*(r+b))+r*r*p*t/(b**3)
                S = -2*W*fr+fr*fr+p*p*q*q/b2
            B = 2*n+scale2*n*n+S
            rows.append((b,p,n,S,B))
        self.counts['decimal_reference_B_angular_points'] += len(rows)
        return scale2,rows

    def frozen_reference_metric(self,r,W,W_r,reference_jets,*,inner_chart,
            root_steps,root_tolerance,target_sha256,_minimum_precision=None):
        self.original_chain.public_only();self.check_clock()
        started = time.monotonic()
        original,j = self._jets(reference_jets)
        rd,wd,wrd = map(decimal_input,(r,W,W_r))
        if rd <= 0 or wd <= 0:
            raise ArithmeticError('same positive frozen r/W required')
        with localcontext() as ctx:
            ctx.prec = max(self.policy['decimal_min_precision'],_minimum_precision or 0)
            _,probe = self._reference_arrays(rd,wd,j,bool(inner_chart))
            precision = max(ctx.prec,self._precision([v for row in probe for v in row],
                divisors=[wd]+[row[0]**3 for row in probe]))
        with localcontext() as ctx:
            ctx.prec = precision
            scale2,rows = self._reference_arrays(rd,wd,j,bool(inner_chart))
            # The chosen centre is a numerical coordinate, never a new E.
            # Store its binary64-exact Decimal value and the small root
            # separately; all B and B-centre operations are Decimal.
            exact_mean_B = mean([row[4] for row in rows])
            centre = decimal_input(self._float(exact_mean_B))
            differences = [row[4]-centre for row in rows]
            left,right = min(differences),max(differences)
            seed = exact_mean_B-centre

            def evaluate(offset):
                us,Ns,weights,values = [],[],[],[]
                for b,p,n,S,B in rows:
                    u2 = ONE+scale2*((centre-S)+offset)
                    N = ONE+scale2*n
                    if u2 <= 0 or N <= 0:
                        raise ArithmeticError('same reference split root bracket lost positivity')
                    u = u2.sqrt();weight = ONE/(u*(N+u))
                    us.append(u);Ns.append(N);weights.append(weight)
                    values.append(((B-centre)-offset)*weight)
                self.counts['decimal_reference_root_angular_points'] += len(rows)
                return mean(values),-mean([N/u**3 for N,u in zip(Ns,us)])/2,{'u':us,'N':Ns}

            tolerance = decimal_input(self.policy['absolute_coordinate_budget'])/1024
            offset,payload,receipt = self._root(evaluate,left,right,-1,seed,
                self.policy['reference_max_steps'],tolerance,'frozen_reference_root_evaluations',
                monotone_reference_derivative=True)
            # Root-accuracy demand is in the small mean coordinate, using
            # the same reference geometry. The actual whole-box bound is
            # checked again in same_sign_box; none is an interval certificate.
            for tightening in range(8):
                eta = scale2*centre+scale2*offset
                e,E = ONE+eta,wd*wd+ONE+eta
                u,N = payload['u'],payload['N']
                omega = [rd*rd/(ui**3*row[0]**3) for ui,row in zip(u,rows)]
                C = [E*t+rd*row[1] for t,row in zip(j['ftt'],rows)]
                c0 = mean([o*c for o,c in zip(omega,C)])
                if c0 == 0:
                    raise ArithmeticError('same reference Decimal mean derivative vanishes')
                lo,hi = map(Decimal,receipt['bracket_decimal'])
                self.counts['reference_budget_derivative_evaluations'] += 2
                _,dl,_ = evaluate(lo);_,dr,_ = evaluate(hi)
                M = max(abs(dl),abs(dr))
                margin = decimal_input(self.policy['reference_derivative_margin_fraction'])*abs(c0/wd)
                desired = (decimal_input(self.policy['absolute_coordinate_budget'])*margin /
                           (Decimal(self.policy['reference_error_safety_factor'])*M))
                if hi-lo <= desired:
                    break
                offset,payload,receipt = self._root(evaluate,lo,hi,-1,offset,
                    self.policy['reference_max_steps'],desired,'frozen_reference_root_evaluations',
                    monotone_reference_derivative=True)
            else:
                raise ArithmeticError('reference split root cannot pay the absolute mean-coordinate budget')
            across = [frt-q/rd for frt,q in zip(j['frt'],j['ft'])]
            K = [(e+wd*fr)*t+rd*fr-wd*q*q/rd
                 for fr,t,q in zip(j['fr'],j['ftt'],j['ft'])]
            At = [c*frr-E*a*a-wrd*k for c,frr,a,k in zip(C,j['frr'],across,K)]
            er = 2*mean([o*a for o,a in zip(omega,At)])/mean([n/ui**3 for n,ui in zip(N,u)])
            required = self._precision([centre,offset,eta,e,E,er,c0]+C+K+At,
                divisors=[wd]+[ui**3*row[0]**3 for ui,row in zip(u,rows)],derivative=c0/wd)
            if required>ctx.prec:
                self.counts['reference_full_precision_restarts'] += 1
                self.counts['reference_discarded_precision_seconds_in_scientific_clock'] += time.monotonic()-started
                return self.frozen_reference_metric(r,W,W_r,reference_jets,inner_chart=inner_chart,
                    root_steps=root_steps,root_tolerance=root_tolerance,target_sha256=target_sha256,
                    _minimum_precision=required)
            split = {'schema':SCHEMA,'precision':precision,
                'normalization':'W_squared' if inner_chart else 'one',
                'centre_decimal':str(centre),'offset_decimal':str(offset),
                'offset_bracket_decimal':receipt['bracket_decimal'],
                'reference_scalar_derivative_upper_decimal':str(M),
                'reference_mean_derivative_decimal':str(c0),
                'e_r_decimal':str(er),'target_sha256':target_sha256,
                'original_reference_jet_grid_and_functional_retained':True,
                'source_angular_and_roundoff_errors_enclosed':False}
            self.original_chain.COUNTS['frozen_reference_radial_points'] += 1
            self.original_chain.COUNTS['frozen_reference_angular_points'] += len(rows)
            self.counts['split_reference_radial_targets_completed'] += 1
            self.counts['split_reference_seconds_in_scientific_clock'] += time.monotonic()-started
            return {'target_sha256':target_sha256,'r':float(r),'W':float(W),'W_r':float(W_r),
                'eta':None,'eta_inner':None,
                'e':self._float(e),'e_r':self._float(er),'E':self._float(E),
                'E_r':self._float(2*wd*wrd+er),'inner_chart':bool(inner_chart),
                'reference_mean_derivative':self._float(c0),'reference_branch_sign':1 if c0>0 else -1,
                'root_receipt':receipt,'angular_functional_points':len(rows),'split_reference':split,
                'original_requested_root_steps':int(root_steps),'original_requested_root_tolerance':float(root_tolerance),
                'binary64_eta_fields_are_disabled_split_required':True,
                'root_angular_radial_DtN_ODE_and_roundoff_errors_enclosed':False,
                'continuous_target_definition_not_replaced_by_node_table':True}

    def _rebuild_prepared(self,target,original,j):
        """Rebuild every rounded intermediate from exact float inputs at this precision."""
        split=target['split_reference']
        rd,wd=decimal_input(target['r']),decimal_input(target['W'])
        centre,offset=Decimal(split['centre_decimal']),Decimal(split['offset_decimal'])
        scale2=wd*wd if target['inner_chart'] else ONE
        e=ONE+scale2*centre+scale2*offset
        E=wd*wd+e
        b=[]
        for q in j['ft']:
            b2=rd*rd-q*q
            if b2<=0:
                raise ArithmeticError('same split trial angular graph lost positivity')
            b.append(b2.sqrt())
        self.counts['decimal_geometry_input_rebuilds'] += 1
        self.counts['decimal_geometry_b_angular_points'] += len(b)
        return {'target':target,'original_jets':original,'jets':j,'r':rd,'W':wd,
                'centre':centre,'offset':offset,'scale2':scale2,'e':e,'E':E,'b':b,
                'precision':getcontext().prec}

    def _prepare(self,target,jets):
        split = target.get('split_reference')
        if (not isinstance(split,dict) or split.get('schema') != SCHEMA
                or split.get('target_sha256') != target['target_sha256']):
            raise ValueError('same split reference target is required by every geometry consumer')
        original,j = self._jets(jets)
        return self._rebuild_prepared(target,original,j)

    def _geometry(self,prepared,x,chart):
        self.check_clock()
        if prepared['precision'] != getcontext().prec:
            prepared=self._rebuild_prepared(prepared['target'],prepared['original_jets'],prepared['jets'])
        target,j = prepared['target'],prepared['jets']
        r,W,E = prepared['r'],prepared['W'],prepared['E']
        c,offset = prepared['centre'],prepared['offset']
        x = decimal_input(x)
        if chart == 'lambda':
            if not target['inner_chart']:
                raise ValueError('lambda requires the same normalized inner target')
            coordinate_scale,scale2 = W,W*W
        elif chart == 'zeta':
            if target['inner_chart']:
                raise ValueError('zeta requires the same outer target')
            coordinate_scale,scale2 = ONE/W,ONE
        else:
            raise ValueError('split chain retains declared lambda/zeta charts only')
        s = coordinate_scale*x
        fields = {name:[] for name in ('d','p','q','t','b','u','N','C','omega','B','M')}
        residuals,numerators,expression_scales,divisors = [],[],[],[W]
        for q,t,fr,frt,b in zip(j['ft'],j['ftt'],j['fr'],j['frt'],prepared['b']):
            d=s+fr;p=-W+d;b2=b*b
            if chart == 'lambda':
                v=x+fr/W
                n=(q/W)**2/(b*(r+b))+r*r*(v-1)*(t/W)/b**3
                S=-2*v+v*v+(v-1)**2*q*q/b2
            else:
                n=q*q/(b*(r+b))+r*r*p*t/b**3
                S=-2*W*d+d*d+p*p*q*q/b2
            u2=ONE+scale2*((c-S)+offset);N=ONE+scale2*n
            if u2<=0 or N<=0:
                raise ArithmeticError('same split trial lost its positive turning component')
            u=u2.sqrt();C=E*t+r*p;omega=r*r/(u**3*b**3)
            numerator=((2*n+scale2*n*n+S)-c)-offset
            numerators.append(numerator)
            residuals.append(numerator/(u*(N+u)))
            expression_scales.extend((n,S,2*n+scale2*n*n+S,C,omega,numerator))
            divisors.extend((u*(N+u),u**3*b**3))
            for name,value in zip(fields,(d,p,q,t,b,u,N,C,omega,frt-q/r,r+p*t-q*q/r)):
                fields[name].append(value)
        c0=mean([o*c for o,c in zip(fields['omega'],fields['C'])])
        self.counts['decimal_mean_geometry_angular_points'] += len(residuals)
        required=self._precision(expression_scales+[c,offset,E,c0],divisors=divisors,derivative=c0/W)
        if required>getcontext().prec:
            self.counts['trial_geometry_precision_restarts'] += 1
            getcontext().prec=required
            return self._geometry(prepared,x,chart)
        return {'fields':fields,'root_value':mean(residuals),'root_derivative':c0/W,
                'mean_derivative':c0,'s':s,'x':x,'E':E,'coordinate_scale':coordinate_scale,
                'root_residual_scale':scale2,'prepared':prepared,'chart':chart,
                'normalized_root_numerators':numerators}

    def _connection_decimal(self,state,s_r):
        """Consume the same split e/E/e_r before converting any connection array."""
        self.check_clock()
        prepared=state['prepared'];j=prepared['jets'];f=state['fields']
        r,W,e,E=prepared['r'],prepared['W'],prepared['e'],prepared['E']
        Wr=decimal_input(prepared['target']['W_r'])
        er=Decimal(prepared['target']['split_reference']['e_r_decimal'])
        K=[(e+W*d)*t+r*d-W*q*q/r for d,t,q in zip(f['d'],f['t'],f['q'])]
        Q=[E*B*B+Wr*k+er*M/2-C*frr
           for B,k,M,C,frr in zip(f['B'],K,f['M'],f['C'],j['frr'])]
        if s_r is None:
            if state['mean_derivative']==0:
                raise ArithmeticError('actual Decimal mean connection coefficient vanished')
            sr=mean([o*q for o,q in zip(f['omega'],Q)])/state['mean_derivative']
        else:
            sr=decimal_input(s_r)
        D=[C*(sr+frr)-E*B*B-Wr*k-er*M/2
           for C,frr,B,k,M in zip(f['C'],j['frr'],f['B'],K,f['M'])]
        R=[o*d for o,d in zip(f['omega'],D)]
        self.counts['decimal_connection_angular_points'] += len(K)
        required=self._precision([e,E,er,sr]+K+Q+D+R,
            divisors=[W],derivative=state['mean_derivative'])
        if required>getcontext().prec:
            self.counts['connection_precision_restarts'] += 1
            getcontext().prec=required
            updated=self._geometry(prepared,state['x'],state['chart'])
            return self._connection_decimal(updated,s_r)
        result=dict(state)
        result['fields']={**f,'K':K,'Q':Q,'D':D,'R':R}
        result.update(s_r=sr,p0_r=-Wr+sr,
            decimal_mean_connection_residual=mean(R))
        return result

    def _float_state(self,state):
        p=state['prepared'];target=p['target'];W=p['W']
        result={name:np.asarray([self._float(v) for v in values],dtype=float)
                for name,values in state['fields'].items()}
        result.update(target=target,jets=p['original_jets'],x=self._float(state['x']),
            x_decimal=str(state['x']),chart=state['chart'],s=self._float(state['s']),
            p0=self._float(-W+state['s']),E=self._float(state['E']),
            mean_derivative=self._float(state['mean_derivative']),
            root_value=self._float(state['root_value']),
            root_coordinate_derivative=self._float(state['root_derivative']),
            coordinate_scale=self._float(state['coordinate_scale']),
            root_residual_scale=self._float(state['root_residual_scale']),
            split_reference_preserved_in_all_root_and_output_calls=True,
            source_angular_and_roundoff_errors_enclosed=False)
        if result['mean_derivative']==0:
            raise ArithmeticError('existing binary64 derivative interface cannot resolve this same mean branch')
        if 's_r' in state:
            result.update(s_r=self._float(state['s_r']),s_r_decimal=str(state['s_r']),
                p0_r=self._float(state['p0_r']),
                decimal_mean_connection_residual=str(state['decimal_mean_connection_residual']),
                complete_connection_consumed_same_split_before_binary64_conversion=True)
        return result

    def geometry_from_split(self,target,jets,x,chart):
        self.original_chain.public_only();self.check_clock()
        with localcontext() as ctx:
            ctx.prec=int(target['split_reference']['precision'])
            prepared=self._prepare(target,jets)
            return self._float_state(self._geometry(prepared,x,chart))

    def same_sign_box(self,target,jets,chart,width,derivative_margin_fraction,*,_minimum_precision=None):
        self.original_chain.public_only();self.check_clock()
        if float(derivative_margin_fraction)!=self.policy['reference_derivative_margin_fraction']:
            raise ValueError('same source-bound reference derivative margin required')
        self.counts['decimal_coordinate_box_attempts'] += 1
        with localcontext() as ctx:
            ctx.prec=max(int(target['split_reference']['precision']),_minimum_precision or 0)
            prepared=self._prepare(target,jets);w=decimal_input(width)
            while True:
                self.counts['decimal_coordinate_box_endpoint_evaluations'] += 1
                left=self._geometry(prepared,-w,chart);prepared=left['prepared']
                self.counts['decimal_coordinate_box_endpoint_evaluations'] += 1
                right=self._geometry(prepared,w,chart);prepared=right['prepared']
                if left['prepared']['precision']==right['prepared']['precision']:
                    break
            r,W,E=prepared['r'],prepared['W'],prepared['E']
            split=target['split_reference'];a,b=map(Decimal,split['offset_bracket_decimal'])
            deltas=(a-prepared['offset'],b-prepared['offset'])
            lows,highs,u_mins,N_mins,sensitivities=[],[],[],[],[]
            corner_values=[[ZERO,ZERO],[ZERO,ZERO]]
            precision_divisors=[W]
            for i,b in enumerate(prepared['b']):
                lf,rf=left['fields'],right['fields']
                corners=[]
                for side,endpoint in enumerate((left,right)):
                    f=endpoint['fields']
                    for offset_side,delta in enumerate(deltas):
                        u2=f['u'][i]**2+prepared['scale2']*delta
                        C=f['C'][i]+prepared['scale2']*delta*prepared['jets']['ftt'][i]
                        if u2<=0:
                            raise ArithmeticError('same coordinate and reference-offset box lost its positive domain')
                        u=u2.sqrt()
                        numerator=endpoint['normalized_root_numerators'][i]-delta
                        corner_values[side][offset_side] += numerator/(u*(f['N'][i]+u))
                        corners.append((u2,C/W))
                umin=min(c[0] for c in corners)
                umax=max(c[0] for c in corners)
                if lf['p'][i]<=0<=rf['p'][i]:
                    umax=max(umax,*[E+prepared['scale2']*delta for delta in deltas])
                Nmin=min(lf['N'][i],rf['N'][i])
                Nmax=max(lf['N'][i],rf['N'][i])
                if umin<=0 or Nmin<=0:
                    raise ArithmeticError('same Decimal coordinate box lost its positive domain')
                cmin=min(c[1] for c in corners)
                cmax=max(c[1] for c in corners)
                omin=r*r/(umax*umax.sqrt()*b**3)
                omax=r*r/(umin*umin.sqrt()*b**3)
                lows.append((omin if cmin>=0 else omax)*cmin)
                highs.append((omax if cmax>=0 else omin)*cmax)
                u_mins.append(umin);N_mins.append(Nmin)
                sensitivities.append(Nmax/(2*umin*umin.sqrt()))
                precision_divisors.append(umin*umin.sqrt()*b**3)
            self.counts['decimal_coordinate_reference_offset_corner_angular_points'] += 4*len(prepared['b'])
            corner_values=[[v/Decimal(len(prepared['b'])) for v in row] for row in corner_values]
            lower,upper=mean(lows),mean(highs);sign=target['reference_branch_sign']
            signed_lower=lower if sign>0 else -upper
            reference=abs(Decimal(target['split_reference']['reference_mean_derivative_decimal'])/W)
            margin=decimal_input(derivative_margin_fraction)*reference
            if signed_lower<=margin:
                raise ArithmeticError('same reference Decimal derivative component unresolved on coordinate box')
            if (any(sign*v>0 for v in corner_values[0]) or
                    any(sign*v<0 for v in corner_values[1])):
                raise ArithmeticError('same reference Decimal coordinate box does not contain the current mean root')
            a,b=map(Decimal,split['offset_bracket_decimal'])
            trial_reference_sensitivity=mean(sensitivities)
            propagated=trial_reference_sensitivity*(b-a)/signed_lower
            required=self._precision([lower,upper,trial_reference_sensitivity,propagated]+
                [v for row in corner_values for v in row],
                divisors=precision_divisors,derivative=signed_lower)
            if required>ctx.prec:
                self.counts['coordinate_reference_box_precision_restarts'] += 1
                return self.same_sign_box(target,jets,chart,width,derivative_margin_fraction,
                    _minimum_precision=required)
            if propagated>decimal_input(self.policy['absolute_coordinate_budget']):
                raise ArithmeticError('reference offset bracket has not paid the absolute mean-coordinate budget')
            self.counts['decimal_coordinate_boxes_completed'] += 1
            return {'left_value':self._float(left['root_value']),'right_value':self._float(right['root_value']),
                'derivative_lower_observation':self._float(lower),'derivative_upper_observation':self._float(upper),
                'minimum_u_squared_observation':self._float(min(u_mins)),
                'minimum_N_observation':self._float(min(N_mins)),
                'coordinate_halfwidth':float(width),
                'signed_derivative_margin_over_reference_observation':self._float(signed_lower/reference),
                'reference_error_in_coordinate_observation':self._float(propagated),
                'reference_error_in_coordinate_decimal':str(propagated),
                'trial_box_reference_sensitivity_upper_decimal':str(trial_reference_sensitivity),
                'reference_offset_corner_values_decimal':[[str(v) for v in row] for row in corner_values],
                'coordinate_and_reference_offset_box_both_included':True,
                'all_angles_or_roundoff_enclosed':False,
                'source_angular_and_roundoff_errors_enclosed':False,
                'split_target_preserved':True}

    def solve_mean(self,target,jets,*,chart,bracket,seed,root_steps,root_tolerance):
        self.original_chain.public_only();self.check_clock()
        with localcontext() as ctx:
            ctx.prec=int(target['split_reference']['precision'])
            prepared=self._prepare(target,jets)
            def evaluate(x):
                nonlocal prepared
                state=self._geometry(prepared,x,chart)
                prepared=state['prepared']
                return state['root_value'],state['root_derivative'],state
            x,state,receipt=self._root(evaluate,decimal_input(bracket[0]),decimal_input(bracket[1]),
                target['reference_branch_sign'],decimal_input(seed),self.policy['trial_max_steps'],
                min(decimal_input(root_tolerance),decimal_input(self.policy['absolute_coordinate_budget'])),
                'trial_mean_root_evaluations')
            result=self._float_state(self._connection_decimal(state,None))
            result['root_receipt']=receipt
            result['same_target_sha256']=target['target_sha256']
            result['mean_connection_residual_observation']=float(np.mean(result['R']))
            result['continuous_mean_branch_or_errors_certified']=False
            self.original_chain.COUNTS['trial_mean_radial_points'] += 1
            self.original_chain.COUNTS['trial_mean_angular_points'] += len(state['fields']['p'])
            self.counts['split_trial_means_completed'] += 1
            return result

    def literal_reference_state(self,target,jets,chart):
        self.original_chain.public_only();self.check_clock()
        with localcontext() as ctx:
            ctx.prec=int(target['split_reference']['precision'])
            prepared=self._prepare(target,jets)
            state=self._geometry(prepared,ZERO,chart)
            result=self._float_state(self._connection_decimal(state,ZERO))
        result['root_receipt']={'exact_same_reference_definition_used':True,
            'floating_residual_observation':result['root_value'],
            'split_target_consumed_by_literal_zero':True,'continuous_root_errors_certified':False}
        self.counts['split_literal_reference_states'] += 1
        return result

    def state_on_output_grid(self,mean_state,output_jets):
        self.original_chain.public_only();self.check_clock()
        with localcontext() as ctx:
            ctx.prec=int(mean_state['target']['split_reference']['precision'])
            prepared=self._prepare(mean_state['target'],output_jets)
            state=self._geometry(prepared,mean_state['x_decimal'],mean_state['chart'])
            result=self._float_state(self._connection_decimal(state,mean_state['s_r_decimal']))
        result['mean_functional_points']=len(mean_state['p'])
        result['output_mean_a_minus_one_observation']=float(np.mean(result['N']/result['u'])-1)
        result['output_mean_R_alias_observation']=float(np.mean(result['R']))
        self.original_chain.COUNTS['output_radial_angular_points'] += len(result['p'])
        self.counts['split_output_radial_states'] += 1
        return result

    def position_state(self,*args,**kwargs):
        return self.original_chain.position_state(*args,**kwargs)

    def mean_direction(self,*args,**kwargs):
        return self.original_chain.mean_direction(*args,**kwargs)

    def output_direction(self,*args,**kwargs):
        return self.original_chain.output_direction(*args,**kwargs)

    def position_direction(self,*args,**kwargs):
        return self.original_chain.position_direction(*args,**kwargs)
