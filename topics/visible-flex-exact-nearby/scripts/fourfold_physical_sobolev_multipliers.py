#!/usr/bin/env python3
"""Complete physical Sobolev multiplier bounds retaining the exact mean.

All inputs are true whole-circle, radial-interval and parameter-family upper
bounds. This helper samples nothing. It returns max(1,|4k|)^s bounds and
separately labeled Bessel-safe bounds; those norms are not silently identified.
"""
from flint import arb, acb_mat
from fourfold_phase_low_feedback_paid_inputs import norm
from fourfold_phase_beta_interval import ball_record


def physical_multiplier_bounds(a_sup,mean_sup,oscillation,first,second,
                               commutator_upper=None):
    a_sup=arb(a_sup).upper();mean_sup=arb(mean_sup).upper()
    O=arb(oscillation).upper();L1=arb(first).upper();L2=arb(second).upper()
    for value in (a_sup,mean_sup,O,L1,L2):
        if not value.is_finite() or not value>=0:
            raise ValueError('complete nonnegative multiplier bounds required')
    mean_sup=min(mean_sup,a_sup).upper()
    kernel=(O+4/arb.pi().sqrt()*(O*L1).sqrt()).upper()
    C=kernel
    if commutator_upper is not None:
        alternate=arb(commutator_upper).upper()
        if not alternate.is_finite() or not alternate>=0:
            raise ValueError('invalid complete alternate commutator bound')
        C=min(C,alternate).upper()
    # Da has exact mean zero. Choosing the constant zero gives oscillation<=L1.
    Cd=(L1+4/arb.pi().sqrt()*(L1*L2).sqrt()).upper()
    matrices={
        'half':acb_mat([[mean_sup,O/2],
            [(O*L1).sqrt(),a_sup+C/2]]),
        'one':acb_mat([[mean_sup,O/4],
            [L1,a_sup+L1/4]]),
        'threehalf':acb_mat([[mean_sup,O/8],
            [(L1*L2).sqrt(),a_sup+C/2+L1/4+Cd/8]]),
        'two':acb_mat([[mean_sup,O/16],
            [L2,a_sup+L1/2+L2/16]])}
    direct={key:norm(mat).upper() for key,mat in matrices.items()}
    M1=direct['one'];M2=direct['two']
    Mh=min(direct['half'],a_sup+C,(a_sup*M1).sqrt()).upper()
    Mt=min(direct['threehalf'],(M1*M2).sqrt(),
           (a_sup*M2*M2*M2).sqrt().sqrt()).upper()
    values={'Mzero':a_sup,'Mhalf':Mh,'Mone':M1,'Mthreehalf':Mt,'Mtwo':M2}
    r=arb(17)/16
    factors={'Mzero':arb(1),'Mhalf':r.sqrt().sqrt(),'Mone':r.sqrt(),
             'Mthreehalf':(r*r*r).sqrt().sqrt(),'Mtwo':r}
    bessel={key:(values[key]*factors[key]).upper() for key in values}
    for value in (*values.values(),*bessel.values()):
        if not value.is_finite() or not value>=0:
            raise ValueError('invalid complete multiplier output')
    report=dict(
        input_bounds={key:ball_record(value) for key,value in
            (('sup',a_sup),('mean',mean_sup),('oscillation',O),
             ('physical_first_derivative',L1),('physical_second_derivative',L2))},
        chosen_complete_commutator=ball_record(C),
        complete_derivative_commutator=ball_record(Cd),
        positive_mean_high_matrices={
            key:[[ball_record(mat[i,j].real) for j in range(2)] for i in range(2)]
            for key,mat in matrices.items()},
        direct_matrix_bounds={key:ball_record(value) for key,value in direct.items()},
        complete_max_weight_bounds={key:ball_record(value) for key,value in values.items()},
        Bessel_conversion_factors={key:ball_record(value) for key,value in factors.items()},
        complete_Bessel_safe_bounds={key:ball_record(value) for key,value in bessel.items()},
        exact_max_weight='max(1,abs(4*k))**s, including mean weight one',
        exact_Bessel_weight='(1+(4*k)**2)**(s/2), including mean weight one',
        conversion='||f||max <= ||f||Bessel <= (17/16)**(s/2)||f||max; one such factor suffices for the converted multiplier bound',
        physical_nonzero_gap=4,
        mean_retained=True,
        full_frequency=True)
    return values,report
