"""PA: complete selected physical amplitude row and one new nu pairing.

No IO or numerical import.  All old97 row intervals and all frozen trial
coordinates are retained.  Error is measured in primitive plus mean.
"""
from fractions import Fraction

OUTPUT_ORDER = (
    "complete_original_trial_second_primitive_mean_upper",
    "complete_selected_amplitude_row_change_dual_upper",
    "complete_selected_amplitude_row_dual_upper",
    "complete_original_trial_physical_amplitude_pairing",
    "complete_trial_amplitude_row_transfer_error_upper",
    "complete_true_particular_amplitude_error_upper",
    "complete_true_particular_physical_amplitude_enclosure",
    "complete_true_particular_normalized_amplitude_enclosure",
)
SIGNED_INDICES = (3,6,7)


def require(ok,message):
    if not ok:
        raise ValueError(message)


def rational(api,value):
    value = Fraction(value)
    return api.arb(value.numerator)/value.denominator


def magnitude(value):
    require(value.is_finite(),"finite whole old or new signed ball")
    return abs(value).upper()


def nonnegative(value):
    require(value.is_finite() and value.lower() >= 0,"whole finite nonnegative bound")
    return value.upper()


def saved_rational_consequences():
    """Exact comparisons of PA.4/9/10, not new numerical old targets."""
    epsilon = Fraction(19,10**10)*Fraction(936826,10**6)
    checks = {
        "whole_row_change_194":80**2+176**2 < 194**2,
        "actual_selected_row_change":194*epsilon < Fraction(3454,10**10),
        "whole_primitive_mean_dual_18":64+(16+2*epsilon)**2 < 18**2,
    }
    require(all(checks.values()),"all complete analytic rational comparisons")
    return {"checks":checks,"complete_selected_state_difference":str(epsilon),
            "row_change_dual_strict_upper":"3454/10000000000","row_dual_strict_upper":"18"}


def complete_selected_amplitude(api,old_row,trial,saved,publish):
    """PA.2--16.  The full new physical and normalized signed border balls."""
    require(len(trial) == 193 and len(old_row["rows"]) == 96,
            "the complete original real trial and whole97 physical amplitude row")
    require(set(saved) == {"selected_mean","waist_K","waist_a","D","H"},
            "whole selected density inputs and original complete NP error")
    arb = api.arb
    def save(index,value):
        return publish(OUTPUT_ORDER[index],value,
            "signed_enclosure" if index in SIGNED_INDICES else "upper")
    old_m = old_row["actual_mean_abs_interval"]
    m0lo,m0hi = rational(api,old_m["lower"]).lower(),rational(api,old_m["upper"]).upper()
    ms = saved["selected_mean"]
    require(ms.is_finite() and ms.upper() < 0 and m0lo > 1,"both true selected and original negative means")
    selected_mlo,selected_mhi = (-ms).lower(),(-ms).upper()
    mlo = selected_mlo if selected_mlo < m0lo else m0lo
    require(mlo > 1,"the entire common waist mean gap")
    K,a = saved["waist_K"],saved["waist_a"]
    require(K.is_finite() and K.upper() < 0 and a.is_finite() and a.lower() > 0,
            "whole unchanged actual waist intrinsic scalars")
    qlo = (-K).sqrt().lower()
    nglo = (a.lower()**2/selected_mhi**2).lower()
    denominator = (nglo*qlo.sqrt().lower()).lower()
    require(denominator > 0,"same selected n_g sqrt(q) lower, never an upper divisor")
    D,H = (nonnegative(saved[key]) for key in ("D","H"))
    second2 = magnitude(trial[96])**2
    for j in range(1,97):
        second2 += magnitude(trial[96+j])**2/(4*j)**2
    direct,from_H = second2.upper().sqrt().upper(),(H/denominator).upper()
    R2 = nonnegative(save(0,direct if direct < from_H else from_H))
    # Whole original nonmean primitive from all33 saved exact inputs.
    inputs = old_row["exact_inputs"]
    require(len(inputs["V"]) == 33 and inputs["alpha"] == "6890507429876859/9007199254740992",
            "complete raw waist and original exact amplitude scaling")
    alpha = rational(api,inputs["alpha"])
    F0 = arb(0)
    for j,value in enumerate(inputs["V"][1:],1):
        F0 += magnitude(alpha*rational(api,value))/(4*j)
    F0 = F0.upper()
    epsilon = rational(api,Fraction(19,10**10)*Fraction(936826,10**6)).upper()
    deltaF = (epsilon/4).upper()
    deltaTheta = (deltaF/mlo+F0*epsilon/mlo**2).upper()
    Gdelta = (16*epsilon/mlo**3+32*deltaTheta/mlo**2).upper()
    Cdelta = (4*epsilon/mlo**3+8*deltaTheta/mlo**2+24*epsilon*F0/mlo**4
              +8*(4*deltaTheta*F0+deltaF)/mlo**3).upper()
    LA = nonnegative(save(1,(Gdelta**2+Cdelta**2).sqrt()))
    selected_g = (8/mlo**2).upper()
    selected_c = (2/mlo**2+8*(F0+deltaF)/mlo**3).upper()
    CA = nonnegative(save(2,(selected_g**2+selected_c**2).sqrt()))
    scale = int(old_row["exact_interval_denominator"])
    require(scale == 2**384,"the original full exact rational row denominator")
    def interval(pair):
        require(len(pair) == 2,"both entire signed rational endpoints")
        return (arb(int(pair[0]))/scale).union(arb(int(pair[1]))/scale)
    signed = interval(old_row["exact_mean_interval_numerator_at_scale"])*trial[96]
    root2 = arb(2).sqrt()
    for j,row in enumerate(old_row["rows"],1):
        require(row["moving_index"] == j and row["physical_frequency"] == 4*j,
                "all96 old physical direction derivatives in exact original order")
        signed += root2*interval(row["exact_interval_numerator_at_scale"])*trial[96+j]
    signed = save(3,signed)
    rowfee = nonnegative(save(4,LA*R2))
    pdefee = nonnegative(save(5,CA*D/denominator))
    fee = (rowfee+pdefee).upper()
    physical = save(6,signed+(-fee).union(fee))
    save(7,physical/alpha)

