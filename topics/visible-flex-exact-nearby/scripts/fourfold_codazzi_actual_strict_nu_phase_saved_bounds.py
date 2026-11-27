"""APHI: exact new consequences of the six whole completed PHI records.

Only rational arithmetic on saved decimal endpoints. No phase, NP,
PDE, amplitude, residual or norm target is evaluated again.
"""
from fractions import Fraction as F
import json


def conclusions():
    mid, radius = F('.03875244'), F('3.09e-9')
    label = F('5.50392222077496552813253364400563405485109535671474074496929e-6')+F('1.19e-66')
    pde = F('1.01485066607095577078965940248268240908600518825058402490321e-5')+F('1.60e-65')
    lower, upper = mid-radius-label-pde, mid+radius+label+pde
    lo, hi = F('.038736784'), F('.038768096')
    checks = [
        ("whole_trial_and_two_whole_fees_lower", lower > lo),
        ("whole_trial_and_two_whole_fees_upper", upper < hi),
        ("same_strict_phase_scalar_inverse", 1/lo < F('25.82')),
        ("whole_physical_amplitude_over_phase_lower",
         F('.006275')/lo < F('.161991')),
        ("whole_physical_amplitude_over_phase_upper",
         F('.006264')/hi > F('.161576')),
    ]
    assert all(ok for _, ok in checks)
    return {"kind": "APHI_whole_signed_phase_rational_consequences_v1",
            "checks": [{"name": name, "passed": ok} for name, ok in checks],
            "strict_phase_interval": [str(lo), str(hi)],
            "physical_amplitude_over_same_phase_interval": ["-161991/1000000", "-161576/1000000"],
            "same_original_selected_background": True,
            "old_scientific_targets_evaluated": 0,
            "full_nu_phase_Schur_or_height_closed": False}


if __name__ == '__main__':
    print(json.dumps(conclusions(), sort_keys=True))
