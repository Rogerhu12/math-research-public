"""NH: whole true high parameter forcing from complete NP/W/JC output.

No IO or numerical import.  All arguments are already admitted WHOLE balls.
publish(name, value, direction) saves/readbacks the complete new ball and
returns its outward lower/upper endpoint.  Never reconstruct old pairings.
"""

OUTPUT_ORDER = (
    "same_true_H_constant_density_nonmean_leakage_upper",
    "complete_trial_two_mean_norm_lower",
    "complete_trial_two_mean_norm_upper",
    "complete_trial_primitive_pair_norm_upper",
    "complete_trial_true_angle_nonmean_pair_norm_upper",
    "complete_raw_paired_cosine96_norm_lower",
    "complete_true_angle_trial_paired_cosine96_norm_lower",
    "complete_trial_paired_high97_norm_upper",
    "complete_true_strict_nu_paired_L2_norm_upper",
    "complete_true_strict_nu_paired_high97_norm_upper",
    "complete_true_strict_nu_incoming_cosine96_error_upper",
    "complete_true_strict_nu_physical_cosine96_error_upper",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def nonnegative_upper(api, value):
    require(value.is_finite() and api.lower(value) >= api.zero,
            "whole finite nonnegative input ball")
    return value.upper()


def magnitude_lower(api, value):
    require(value.is_finite(), "whole finite signed observation")
    lo,hi = value.lower(),value.upper()
    if lo > api.zero:
        return lo
    if hi < api.zero:
        return (-hi).lower()
    return api.zero


def magnitude_upper(api, value):
    require(value.is_finite(), "whole finite signed observation")
    lo,hi = value.lower(),value.upper()
    left,right = abs(lo).upper(),abs(hi).upper()
    return left if left >= right else right


def positive_lower(api, value):
    require(value.is_finite(), "finite full lower expression")
    lo = value.lower()
    return lo if lo > api.zero else api.zero


def sqrt_upper(api, value):
    hi = value.upper()
    require(hi.is_finite() and hi >= api.zero,
            "a whole energy upper minus an actual orthogonal energy lower")
    return api.sqrt(hi).upper()


def complete_high_forcing(api, saved, true_means, raw_pairings, publish):
    """NH.5/8--17, all high modes and both physical means retained.

    saved H1 is the original FULL derivative Wiener sum with exact constant
    coefficient1; m is JC's lower for the WHOLE homotopy including true H.
    raw_pairings are exactly NP's192 uninflated signed observations.  Means
    are NP's two TRUE enclosures.  The exact NP reflected trial has opposite
    physical means; neither mean observation is dropped or set to zero.
    """
    require(set(saved) == {"H1","m","BH","KW","E","D","H"}
            and set(true_means) == {"plus","minus"}
            and set(raw_pairings) == {"declared_incoming_cosine96",
                                      "original_physical_primitive96"},
            "every complete existing scalar, two means and raw pairing group")
    names = {"row_%03d"%j for j in range(1,97)}
    require(all(set(group) == names for group in raw_pairings.values()),
            "all192 entire signed observations, no selected minor")
    H1,BH,KW,E,D,H = (nonnegative_upper(api,saved[key])
                       for key in ("H1","BH","KW","E","D","H"))
    m = saved["m"].lower()
    require(H1 >= api.one and BH >= api.one and KW >= api.one
            and m.is_finite() and m > api.zero,
            "true full derivative identity and the same strictly positive Jacobian")
    def save(index, value, direction="upper"):
        require(direction in ("lower","upper"), "one declared directed endpoint")
        result = publish(OUTPUT_ORDER[index],value,direction)
        require(result.is_finite() and result >= api.zero,
                "whole formally saved nonnegative lower or upper")
        return result
    kappa = save(0,((H1-api.one)/api.sqrt(m).lower()).upper())
    mean_lower_square,mean_upper_square = api.zero,api.zero
    for label in ("plus","minus"):
        lo,hi = magnitude_lower(api,true_means[label]),magnitude_upper(api,true_means[label])
        mean_lower_square += lo*lo
        mean_upper_square += hi*hi
    mean_lower = api.sqrt(mean_lower_square.lower()).lower()
    mean_upper = sqrt_upper(api,mean_upper_square)
    ML = save(1,positive_lower(api,mean_lower-D),"lower")
    possible_MU = (mean_upper+D).upper()
    MU = save(2,H if H <= possible_MU else possible_MU)
    primitive = save(3,sqrt_upper(api,H*H-ML*ML))
    nonmean = save(4,(BH*primitive+kappa*MU).upper())
    incoming = raw_pairings["declared_incoming_cosine96"]
    physical = raw_pairings["original_physical_primitive96"]
    energy = api.zero
    for j in range(1,97):
        name = "row_%03d"%j
        s = magnitude_lower(api,physical[name])
        d = magnitude_lower(api,incoming[name]-physical[name])
        energy += api.rational(2)*(s*s+d*d)
    raw_head = save(5,api.sqrt(energy.lower()).lower(),"lower")
    head = save(6,positive_lower(api,raw_head-E*H),"lower")
    trial_high = save(7,sqrt_upper(api,nonmean*nonmean-head*head))
    full = save(8,(BH*KW*(H+D)).upper())
    assembled_high = (trial_high+BH*KW*D).upper()
    high = save(9,assembled_high if assembled_high <= full else full)
    joint_incoming = save(10,(BH*KW*D+E*H).upper())
    joint_physical = save(11,((BH*D+E*H)*api.sqrt(api.rational(1,2)).upper()).upper())
    return {"paired_high97":high,"paired_full_L2":full,
            "incoming_cosine96_error":joint_incoming,
            "physical_cosine96_error":joint_physical,
            "true_H_mean_leakage":kappa,
            "all_unobserved_low_sines_retained":True,
            "both_physical_means_retained":True,
            "old_pairings_or_trial_recomputed":False}
