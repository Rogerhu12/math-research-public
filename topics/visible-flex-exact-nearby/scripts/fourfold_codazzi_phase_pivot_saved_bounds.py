"""PP: new rational bounds after the actual strict-phase pivot.

Uses only APHI and ASB completed scalar bounds. It does not recompute
NP pairings, PO inversion, phase integration, a norm or an incoming gate.
"""
from fractions import Fraction as F
import json


def conclusions():
    lo, hi, centre = F('.038736784'), F('.038768096'), F('.03875244')
    phase_radius = F('.000015656')
    assert centre-lo == hi-centre == phase_radius
    physical, high, joint = F('.0016047'), F('5.330e-5'), F('6e-7')
    values = {
        'physical_response_over_phase': (physical/lo, F('.041426')),
        'physical_high97_response_over_phase': (high/lo, F('.001376')),
        'same_B_inverse_response_over_phase': (F('.1696')/lo, F('4.378268')),
        'distributed_body_physical_response_feedback': (F(3, 2)*physical/lo, F('.062139')),
        'distributed_body_physical_high97_response_feedback': (F(3, 2)*high/lo, F('.002064')),
        'joint96_phase_normalized_raw_trial_column_error':
            (joint/lo+phase_radius*(physical+joint)/(lo*centre), F('3.224e-5')),
    }
    checks = []
    for name, (value, bound) in values.items():
        assert value < bound, name
        checks.append({'name': name, 'strict_upper': str(bound), 'passed': True})
    return {'kind': 'PP_actual_phase_pivot_saved_scalar_consequences_v1',
            'checks': checks, 'old_scientific_targets_evaluated': 0,
            'known_physical_response_piece_only': True,
            'original_B_high_cutoff': '2^4608',
            'same_sign_B_and_original_target_normalizer_retained': True,
            'all_other_parameter_chart_and_mean_columns_retained': True,
            'nonmean_raw_phase_and_Eprime_a_retained': True,
            'complete_reduced_regular_inverse_proved': False}


if __name__ == '__main__':
    print(json.dumps(conclusions(), sort_keys=True))
