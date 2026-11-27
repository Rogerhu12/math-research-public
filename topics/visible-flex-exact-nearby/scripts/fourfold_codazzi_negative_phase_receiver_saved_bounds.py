"""PRN: new exact rational consequences of complete original saved bounds.

No ODE, FFT, original norm, residual or other scientific target is run.
The seven comparisons certify the complete phase receiver in the original
TC negative source windows, with both means and all true impulses.
"""
from fractions import Fraction as F
import json


def bounds():
    a, ci = F(11,10), F(1031,1000)
    b, gamma, R, L = F(211,1000), F(28,25), F(239,125), F(463,125)
    strict_dual = 4*b*a*a*(ci*R+L/4)+2*gamma*a*a
    qmax = F(103,100)
    root_dual = 4*2*a*a*(ci*qmax*qmax*7+qmax*qmax*6/4)+2*7*qmax*a*a
    rc, radius = F(2333968743003,10**13), F(1,200)
    phase, propagation = F(567,100), F(173872,1000)
    root_state, root_primitive_mean = F(10936120,10**6), F(11272695,10**6)
    source_injection = F(1060693,10**6)
    cut_coefficient = phase*propagation
    root_gain = cut_coefficient*rc*root_primitive_mean+107*radius*root_state
    source_coefficient = cut_coefficient*source_injection
    strict_source_squared = source_coefficient**2*rc**3/3
    root_source_squared = root_gain**2*radius
    strict_impulse = source_coefficient*rc
    comparisons = {
        'complete_primitive_mean_Bessel_constant': ci*ci>F(17,16),
        'complete_strict_phase_energy_dual': strict_dual<F(567,100),
        'complete_root_phase_H1_dual': root_dual<107,
        'complete_root_trace_and_root_impulses': root_gain<2600,
        'complete_root_L2_radial_source': root_source_squared<184**2,
        'complete_strict_L2_radial_source': strict_source_squared<69**2,
        'complete_strict_impulses': strict_impulse<245,
    }
    if not all(comparisons.values()):
        raise ValueError('one new complete PRN rational comparison failed')
    return {'proved':True,'comparisons':comparisons,
        'new_exact_rational_comparisons':len(comparisons),
        'new_exact_values':{name:str(value) for name,value in {
            'strict_phase_dual':strict_dual,'root_phase_H1_dual':root_dual,
            'root_trace_and_impulse_gain':root_gain,
            'root_radial_L2_gain_squared':root_source_squared,
            'strict_radial_L2_gain_squared':strict_source_squared,
            'strict_impulse_gain':strict_impulse}.items()},
        'old_scientific_targets_evaluated':0,'new_numerical_scientific_targets_evaluated':0,
        'whole_TC_negative_residuals_assumed_complete':False,
        'true_root_error_set_to_zero':False,'both_independent_means_retained':True,
        'unknown_response_Fourier_cutoff_used':False,'full_phase_Schur_proved':False}


if __name__ == '__main__':
    print(json.dumps(bounds(),sort_keys=True,separators=(',',':')))
