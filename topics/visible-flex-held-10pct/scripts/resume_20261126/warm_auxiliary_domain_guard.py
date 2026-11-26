"""Turn only impossible auxiliary exponential trials into domain rejections.

The current warm coordinate inherits the original open domain
1e-7 < q_aux < .124 with q_aux = gauge*exp(p0). The original evaluator
checks that domain after math.exp, which can raise uncaught OverflowError.
This instance adapter pre-rejects parameters outside a deliberately wider
logarithmic interval. The original evaluator still decides every point
near either true boundary, so this adapter does not round, clip, change,
or enlarge the accepted domain and does not change a finite valid value.

This alone neither fixes conditioning nor changes the phase scale contract.
It is not installed by importing this file and is not an accepted solve.
"""
import math
import types
import numpy as np


def install(obj):
    if not obj.fixed:
        raise ValueError('Only the original fixed=True auxiliary exponential path is supported')
    gauge=float(obj.seed_support_amplitude)
    if not 1e-7<gauge<.124:
        raise ValueError('The accepted warm gauge must lie in the original open auxiliary domain')
    lower=math.log(1e-7/gauge)
    upper=math.log(.124/gauge)
    # The one-unit padding is intentional: no finite point near an actual
    # boundary is classified by a rounded logarithm. On this padded interval
    # exp is finite and bounded far away from binary64 overflow/underflow.
    padded_lower,padded_upper=lower-1.,upper+1.
    original=obj.initial
    stats=dict(rejected_before_exp=0,original_open_domain=[1e-7,.124],
        padded_log_precheck=[padded_lower,padded_upper],
        valid_function_and_jacobian_changed=False,
        no_geometry_or_metric_guard_removed=True)
    def initial(self,p):
        p0=float(np.asarray(p)[0])
        if not math.isfinite(p0) or p0<padded_lower or p0>padded_upper:
            stats['rejected_before_exp']+=1
            raise FloatingPointError('Auxiliary log coordinate outside original positive search domain')
        return original(p)
    obj.initial=types.MethodType(initial,obj)
    obj.auxiliary_domain_guard=stats
    return stats
