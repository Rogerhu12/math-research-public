"""PH: exact rational consequences of already proved, complete bounds.

This file does not restore a trial, integrate a flow, call a producer or
evaluate an old norm.  The cited PH proof identifies every saved bound.
"""
from fractions import Fraction as F
import json


def conclusions():
    checks = []
    def upper(name, value, bound):
        assert value < F(bound), name
        checks.append({"name": name, "strict_upper": bound, "passed": True})
    assert F(22,7)**2 < 12  # pi/(4 sqrt(3)) < 1/2.
    qmin, qmax, epsQ, deltaK = F('.5338'), F('1.03'), F('2e-9'), F('1.048e-7')
    upper('original_complete_v_supremum', F('1.912')/qmin, '4')
    deltaq = deltaK/(2*qmin)
    upper('same_selected_q_difference', deltaq, '1.048e-7')
    deltaR = qmax*epsQ+4*deltaq
    upper('same_selected_R_difference', deltaR, '4.22e-7')
    # e^x-1 <= x/(1-x), 0<x<1, with |delta_*|/2<5e-11.
    x = F('5e-11'); deltagamma = 7*x/(1-x)
    upper('same_selected_gamma_difference', deltagamma, '4e-10')
    delta_a = 2*2*F(1,2)*deltaR+deltagamma
    upper('same_selected_full_field_dual_difference', delta_a, '1e-6')
    assert F('.425')**2 > F(9,50)
    field_dual = qmax*(F('.591950779')+delta_a*F('.425'))
    upper('same_selected_short_ordinary_field_dual', field_dual, '.610')
    label = F(33,32)*F(16,15)
    assert label == F(11,10)
    phase_dual = 2*label**2*F('.610')
    upper('same_selected_full_phase_ordinary_L2_dual', phase_dual, '1.5')
    upper('full_phase_true_NP_error', F(3,2)*F('6.765672e-6'), '1.014851e-5')
    # True H minus the original H24: W + the complete original K48 row.
    initial = F(16,15)*(64*F('2.211e-7')+F(33,32)*F('1.422e-8'))
    ray_value = F(11,10)*F('1e-10')*F('.541')
    upper('original_H24_selected_ray_value_difference', ray_value, '6e-11')
    label_error = initial+256*F('6e-11')+F('2e-12')
    upper('true_selected_label_vs_original_finite_carrier', label_error, '1.6e-5')
    upper('true_selected_squared_label_vs_original_finite_carrier',
          F('1.6e-5')*(2*label+F('1.6e-5')), '3.521e-5')
    assert F(1,240) < F(1,32) and F(1,225) < F(1,32)
    return {"kind":"PH_exact_rational_consequences_v1", "checks":checks,
        "old_scientific_targets_evaluated":0, "new_signed_phase_integral_evaluated":False,
        "full_phase_Schur_or_height_closed":False}


if __name__ == '__main__':
    print(json.dumps(conclusions(), sort_keys=True))
