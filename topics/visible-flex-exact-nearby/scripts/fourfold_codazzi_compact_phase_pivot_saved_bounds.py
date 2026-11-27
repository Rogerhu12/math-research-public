"""CP: new uniform candidate phase pivot from complete saved bounds.

Only rational arithmetic on already proved bounds and exact formula
coefficients. No old NP, phase, residual, norm, flow or pairing target.
"""
from fractions import Fraction as F
import json


def conclusions():
    B, G, K, V, Q1 = F(211, 1000), F(28, 25), F(21, 20), F(18, 5), F('5.438')
    b = F(9, 50)
    W = F(2, 5)*V*V*Q1+V**3
    A = B*B*W/2+G*V*B*Q1/2
    C = B*K*W+G*V*K*Q1/2
    source = 2*A+F(256, 5775)*C
    trial = F(17, 40)*F('7.501268')*10+F('6.765672e-6')
    lo, hi, response_error = F('.038736784'), F('.038768096'), F('1.014851e-5')
    hessian, direction, average = F(530), F(132), F(21, 20)
    radial = F(49, 100)
    centre_fee = average*hessian*direction*radial*F('4.760e-7')
    neighbourhood_fee = average*hessian*direction*(
        radial*(F('4.760e-7')+F('1e-7'))+100*F('5e-12'))
    phase_fee = direction*F('1e-8')*(
        F(25, 24)*F(21, 20)*150+F(25, 24)**2*F('2.16'))
    checks = [
        ('entire_original_radius_above_one', F('1.068')*(1-B*b)>1),
        ('complete_true_nu_source_L1_L2_below_10', source<10),
        ('short_radial_sqrt_bound', b<F(17, 40)**2),
        ('whole_fixed_trial_L2_below_32', trial<32),
        ('whole_negative_radial_sqrt_bound', F('.239')<radial**2),
        ('same_H_average_L2_bound', F(33, 32)**3<F(21, 20)**2),
        ('complete_same_metric_centre_phase_change', centre_fee<F('.017134')),
        ('same_metric_centre_positive_candidate_pivot',
         lo-response_error-F('.017134')>F(1, 50)),
        ('entire_nu_interval_inside_original_domain',
         F('.936826')*F('1e-10')+F('5e-12')<F('1e-10')),
        ('all_straight_phase_lifts_have_true_J_lower',
         F(32, 33)-F('1e-8')>F(24, 25)),
        ('all_straight_phase_lifts_inside_original_chart_upper',
         F(32, 31)+F('1e-8')<2),
        ('true_phase_composition_factor', F(25, 24)<F(21, 20)**2),
        ('complete_state_metric_neighbourhood_phase_change',
         neighbourhood_fee<F('.02077')),
        ('complete_phase_chart_change', phase_fee<F('.00022')),
        ('uniform_candidate_phase_pivot_lower',
         lo-response_error-F('.02077')-F('.00022')>F(1, 60)),
        ('uniform_candidate_phase_pivot_upper',
         hi+response_error+F('.02077')+F('.00022')<F(3, 50)),
    ]
    assert all(ok for _, ok in checks)
    return {
        'kind': 'CP_uniform_candidate_phase_pivot_saved_bounds_v1',
        'checks': [{'name': name, 'passed': ok} for name, ok in checks],
        'same_metric_centre_pivot_lower': '1/50',
        'complete_neighbourhood_pivot_interval': ['1/60', '3/50'],
        'complete_neighbourhood_inverse_upper': '60',
        'whole_trial_definition_sha256':
            '83da6322dbb4702fe6ae308acbcfb7bb1ed9410d17e0cded65bc1215dec233db',
        'old_scientific_targets_evaluated': 0,
        'trial_selected_again': False,
        'full_Fourier_and_both_means_retained': True,
        'original_moving_phase_and_unfixed_constant_retained': True,
        'current_regular_and_Eprime_a_defects_retained': True,
        'full_true_response_Schur_or_topic_completion_proved': False,
    }


if __name__ == '__main__':
    print(json.dumps(conclusions(), sort_keys=True))
