#!/usr/bin/env python3
"""Same fixed-E mean/connection derivatives with exact Fourier backgrounds removed.

All height directions are positive even Fourier polynomials of degree <=96.
Their means and the means of their radial jets are exactly zero. Subtract
only the corresponding scalar coefficients before numerical angular means.
Keep all actual states, output directions, off-solution terms and fixed E.
The source/angle/radial errors remain unresolved. Science runs in Actions.
"""
from decimal import Decimal, getcontext, localcontext
import hashlib
import importlib.util
import math
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
BASE_SHA='40e8e1b07a286a573dcd52549909e1b208d9c16e8232b52afce7448ca8a75238'
path=HERE/'r618_split_reference_mean_chain_20261127.py'
if hashlib.sha256(path.read_bytes()).hexdigest()!=BASE_SHA:
    raise RuntimeError('original same-E Decimal evaluator changed')
spec=importlib.util.spec_from_file_location('r618_centered_original_split',path)
base=importlib.util.module_from_spec(spec);sys.modules[spec.name]=base
spec.loader.exec_module(base)
decimal_input,mean=base.decimal_input,base.mean
ZERO,ONE,TWO=base.ZERO,base.ONE,base.TWO

class FourierCenteredMeanChain(base.SplitReferenceMeanChain):
    @staticmethod
    def policy_descriptor():
        policy=base.SplitReferenceMeanChain.policy_descriptor()
        policy.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            unchanged_value_chain_sha256=BASE_SHA,
            direction_policy='exact_zero_mean_Fourier_background_subtraction_v1',
            complete_off_solution_mean_and_connection_terms_retained=True,
            actual_direction_maximum_mode=96,
            minimum_direction_mean_points=512,
            direction_accumulation='Decimal_coefficients_then_longdouble_contractions',
            scalar_iteration='alternating_safeguarded_Newton_bisection_and_signed_small_bracket',
            original_analytic_jacobian_uses_final_binary64_state_and_is_not_high_precision=False,
            derivative_roundoff_and_angular_error_certified=False)
        return policy

    def _root(self,evaluate,left,right,sign,seed,steps,tolerance,counter,
              *,monotone_reference_derivative=False):
        """Absolute-coordinate bracketing, with source errors kept unresolved."""
        self.check_clock()
        left,right,seed,tolerance = map(decimal_input,(left,right,seed,tolerance))
        if left > right or tolerance <= 0 or sign not in (-1,1):
            raise ValueError('finite absolute-coordinate bracket required')
        rec = {'counter':counter,'initial_bracket_decimal':[str(left),str(right)],
            'absolute_coordinate_tolerance_decimal':str(tolerance),'maximum_iterations':int(steps),
            'evaluations':0,'bisection_candidates':0,'newton_candidates':0,'small_bracket_attempts':0,'status':'started',
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
                # A small Newton residual only proposes a short bracket.
                # Both endpoint signs are evaluated before its use; no
                # residual is silently declared zero and the old root stays
                # in the actual observed bracket.
                if abs(f) <= tolerance*abs(d)/16:
                    a=max(left,x-tolerance/4);b=min(right,x+tolerance/4)
                    if a < b:
                        rec['small_bracket_attempts'] += 1
                        self.counts['small_signed_bracket_attempts'] += 1
                        fa,da,pa=call(a);fb,db,pb=call(b)
                        if sign*fa <= 0 and sign*fb >= 0:
                            left,right=a,b
                            self.counts['small_signed_brackets_completed'] += 1
                            return finish(x,f,d,payload,'small_actual_signed_bracket',iteration+1)
                if sign*f < 0:
                    left,fl,dl,pl = x,f,d,payload
                else:
                    right,fr,dr,pr = x,f,d,payload
                candidate=left+(right-left)/2
                use_newton=False
                if iteration%2 == 0 and d:
                    proposed=x-f/d
                    if left < proposed < right:
                        candidate=proposed;use_newton=True
                if candidate == left or candidate == right:
                    raise ArithmeticError('Decimal bracket resolution exhausted before the absolute budget')
                if use_newton:
                    self.counts['decimal_scalar_newton_candidates'] += 1
                    rec['newton_candidates'] += 1
                else:
                    self.counts['decimal_scalar_bisection_candidates'] += 1
                    rec['bisection_candidates'] += 1
                x=candidate
                f,d,payload = call(x)
            raise ArithmeticError('same Decimal scalar root exhausted its declared iterations')
        except Exception as error:
            rec.update(status='failed',error_type=type(error).__name__,error=str(error),
                bracket_decimal=[str(left),str(right)],bracket_width_decimal=str(right-left))
            self.counts['decimal_scalar_root_failures'] += 1
            raise

    def _float_state(self,state):
        result=super()._float_state(state)
        if 's_r' not in state:
            return result
        prepared=state['prepared'];f=state['fields'];j=prepared['jets']
        r,W,e,E=[prepared[k] for k in ('r','W','e','E')]
        Wr=decimal_input(prepared['target']['W_r'])
        er=Decimal(prepared['target']['split_reference']['e_r_decimal'])
        sr=state['s_r'];three=Decimal(3)
        names=('ap_plus_W','aq','at_plus_W_over_r','Lp_minus_Wr',
               'Lq','Lt_minus_Wr_over_r','Lrt','Lrr_minus_W')
        coefficients={name:[] for name in names}
        lp=[]
        for i in range(len(f['p'])):
            p,q,t,b,u,N,C,omega,B,D,d=[f[k][i] for k in
                ('p','q','t','b','u','N','C','omega','B','D','d')]
            frr=j['frr'][i]
            ap=omega*C
            aq=r*q/(u*b**3)+three*r*r*p*t*q/(u*b**5)+N*r*r*p*p*q/(u**3*b**4)
            at=r*r*p/(u*b**3)
            Lp=omega*(Wr*(W*t+r)+er*t/2-r*(sr+frr)
                       -three*D*r*r*p/(u*u*b*b))
            Lq=omega*(-2*E*B/r-2*Wr*W*q/r-er*q/r
                       -three*D*(r*r*p*p*q/(u*u*b**4)+q/(b*b)))
            Lt=omega*(Wr*(e+W*d)+er*p/2-E*(sr+frr))
            Lrt=2*omega*E*B
            Lrr=-ap
            values=(ap+W,aq,at+W/r,Lp-Wr,Lq,Lt-Wr/r,Lrt,Lrr-W)
            for name,value in zip(names,values):
                coefficients[name].append(self._float(value))
            lp.append(Lp)
        result['centered_direction_coefficients']={
            name:np.asarray(values,dtype=float) for name,values in coefficients.items()}
        result['mean_Lp_decimal']=str(mean(lp))
        result['mean_derivative_decimal']=str(state['mean_derivative'])
        result['direction_coefficient_source']='complete_same_split_Decimal_state'
        self.counts['centered_coefficient_radial_states'] += 1
        self.counts['centered_coefficient_angular_points'] += len(f['p'])
        return result

    def _directions(self,state,direction_jets,*,mean_grid):
        H={k:np.asarray(direction_jets[k],dtype=np.longdouble)
           for k in self.original_chain.JET_KEYS}
        shape=H['f'].shape
        if (len(shape)!=2 or shape[0]!=len(state['p'])
                or any(v.shape!=shape for v in H.values())):
            raise ValueError('all six same-angle finite Fourier direction jets are required')
        if mean_grid and shape[0] < self.policy['minimum_direction_mean_points']:
            raise ValueError('mean grid cannot alias the declared positive modes through96')
        if state.get('direction_coefficient_source')!='complete_same_split_Decimal_state':
            raise ValueError('complete same-Decimal derivative coefficients required')
        c={k:np.asarray(v,dtype=np.longdouble)[:,None]
           for k,v in state['centered_direction_coefficients'].items()}
        return H,c

    @staticmethod
    def _finite_float(value):
        result=np.asarray(value,dtype=float)
        if not np.all(np.isfinite(result)):
            raise ArithmeticError('complete centered derivative cannot be represented as finite binary64')
        return result

    def mean_direction(self,state,direction_jets):
        self.original_chain.public_only();self.check_clock()
        H,c=self._directions(state,direction_jets,mean_grid=True)
        angular_mean=lambda v:np.mean(v,axis=0,dtype=np.longdouble)
        c0=np.longdouble(state['mean_derivative_decimal'])
        if not np.isfinite(c0) or c0==0:
            raise ArithmeticError('same mean branch derivative unresolved')
        # Exactly mean(H_r)=mean(H_tt)=0 for every actual parameter column.
        ds=-angular_mean(c['ap_plus_W']*H['fr']+c['aq']*H['ft']
                         +c['at_plus_W_over_r']*H['ftt'])/c0
        # Use Q-s_r C=-D before differentiating the connection mean.
        # The removed coefficients Wr, Wr/r, W multiply exact zero means.
        numerator=angular_mean(c['Lp_minus_Wr']*H['fr']+c['Lq']*H['ft']
            +c['Lt_minus_Wr_over_r']*H['ftt']+c['Lrt']*H['frt']
            +c['Lrr_minus_W']*H['frr'])
        dsr=(numerator+np.longdouble(state['mean_Lp_decimal'])*ds)/c0
        answer=self._complete_output_direction(state,H,c,ds,dsr)
        answer['s_longdouble']=ds
        answer['s_r_longdouble']=dsr
        answer['turning_linearized_residual_observation']=np.mean(answer['a'],axis=0)
        answer['connection_linearized_residual_observation']=np.mean(answer['R'],axis=0)
        self.counts['centered_mean_direction_columns_at_radii'] += H['f'].shape[1]
        self.counts['centered_mean_direction_angular_points'] += H['f'].size
        return answer

    def _complete_output_direction(self,state,H,c,ds,dsr):
        r,W,Wr=[np.longdouble(state['target'][k]) for k in ('r','W','W_r')]
        p,q,t,b,u,N,omega,D=[np.asarray(state[k],dtype=np.longdouble)[:,None]
                            for k in ('p','q','t','b','u','N','omega','D')]
        dp=H['fr']+ds[None,:]
        db=-q*H['ft']/b
        du=-r*r*p*dp/(u*b*b)-r*r*p*p*q*H['ft']/(u*b**4)
        dN=r*q*H['ft']/b**3+r*r*(t*dp+p*H['ftt'])/b**3+3*r*r*p*t*q*H['ft']/b**5
        # Output values retain the removed backgrounds: subtraction is only
        # licensed inside means, not at individual angular points.
        da=(-W*dp-W/r*H['ftt']+c['ap_plus_W']*dp+c['aq']*H['ft']
            +c['at_plus_W_over_r']*H['ftt'])
        dR=(-W*(dsr[None,:]+H['frr'])-Wr*dp-Wr/r*H['ftt']
            +c['ap_plus_W']*(dsr[None,:]+H['frr'])
            -c['Lp_minus_Wr']*dp-c['Lq']*H['ft']
            -c['Lt_minus_Wr_over_r']*H['ftt']-c['Lrt']*H['frt'])
        dw=-3*omega*(du/u+db/b)
        dD=(dR-dw*D)/omega
        result={k:self._finite_float(v) for k,v in
                dict(s=ds,s_r=dsr,p=dp,b=db,u=du,N=dN,a=da,R=dR,D=dD).items()}
        result.update(E=np.zeros_like(result['s']),E_r=np.zeros_like(result['s']))
        return result

    def output_direction(self,state,direction_jets,actual_mean_direction):
        self.original_chain.public_only();self.check_clock()
        H,c=self._directions(state,direction_jets,mean_grid=False)
        ds=np.asarray(actual_mean_direction['s_longdouble'],dtype=np.longdouble)
        dsr=np.asarray(actual_mean_direction['s_r_longdouble'],dtype=np.longdouble)
        answer=self._complete_output_direction(state,H,c,ds,dsr)
        self.counts['centered_output_direction_angular_points'] += H['f'].size
        return answer
