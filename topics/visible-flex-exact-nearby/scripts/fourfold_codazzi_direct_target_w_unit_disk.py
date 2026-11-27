"""DWT: first direct true target-w trial from the complete new disk input.

Old alpha/scalar/tail conclusions and all original phases are unchanged.
The same proved ASR tail envelope is reused, without a tail computation.
"""
MODES = 2048
GRID = 8192
TARGETS = [
    "complete_direct_unit_disk_target_w_Linf_error_upper",
    "complete_direct_unit_disk_target_w_L2_error_upper",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def up(value):
    require(value.is_finite() and value.lower() >= 0, "one whole nonnegative finite bound")
    return value.upper()


def complete_w_reference(api, n, saved_complete_disk,
                         whole_omega, whole_source_phase):
    require(type(n) is int and 1 <= n <= MODES, "one natural positive mode")
    require(saved_complete_disk["complete_grid_points"] == GRID
            and saved_complete_disk["complete_positive_mode"] == n,
            "the entire original8192-point disk at this mode")
    require(whole_omega.is_finite() and whole_source_phase.is_finite(),
            "both entire original phase balls")
    center = saved_complete_disk["center"]
    radius = up(saved_complete_disk["radius"])
    require(center.is_finite(), "the complete finite disk center")
    value = api.acb(center.real+api.arb(0, radius),
                    center.imag+api.arb(0, radius))
    theta = 4*n*whole_omega
    phase = 4*n*whole_source_phase
    q = api.acb(theta.cos(), -theta.sin())
    t = api.acb(phase.cos(), -phase.sin())
    denominator = q-1
    divisor_lower = abs(denominator).lower()
    require(divisor_lower.is_finite() and divisor_lower > 0,
            "strict lower for the complete original cohomological divisor")
    reference = -(value+t*api.acb(value.real, -value.imag))/denominator
    require(reference.is_finite(), "the complete direct true-w reference ball")
    return reference, divisor_lower


def complete_w_mode_error(api, saved_reference, saved_divisor_lower,
                          exact_new_w_trial, saved_complete_source,
                          saved_complete_model, saved_complete_alias):
    require(saved_reference.is_finite() and exact_new_w_trial.is_finite(),
            "the whole reference and the exact first trial coefficient")
    require(exact_new_w_trial.real.is_exact() and exact_new_w_trial.imag.is_exact(),
            "the new saved trial coefficient is an exact point")
    require(saved_divisor_lower.is_finite() and saved_divisor_lower > 0,
            "the whole positive original divisor lower")
    rounding = abs(saved_reference-exact_new_w_trial).upper()
    source, model, aliases = map(up, (
        saved_complete_source, saved_complete_model, saved_complete_alias))
    fee = (2*(source+model+aliases)/saved_divisor_lower.lower()).upper()
    return {
        "complete_direct_w_coefficient_error_upper": (rounding+fee).upper(),
        "complete_disk_phase_trial_rounding_upper": rounding,
        "complete_source_model_alias_divisor_fee_upper": fee,
    }


class WholeWErrors:
    """All natural modes precede the original complete universal tail."""

    def __init__(self, api):
        self.api = api
        self.next_n = 1
        self.head_Linf = api.arb(0)
        self.head_L2_squared = api.arb(0)

    def append(self, n, saved_complete_mode_error):
        require(type(n) is int and n == self.next_n and n <= MODES,
                "all2048 complete newly saved mode records in natural order")
        value = up(saved_complete_mode_error)
        self.head_Linf = (self.head_Linf+2*value).upper()
        self.head_L2_squared = (self.head_L2_squared+2*value**2).upper()
        self.next_n += 1

    def finish_with_original_whole_tail_envelope(
            self, saved_ASR_Linf_tail, saved_ASR_L2_tail):
        require(self.next_n == MODES+1,
                "the complete new signed head before any whole target")
        tail_Linf, tail_L2 = map(up, (saved_ASR_Linf_tail, saved_ASR_L2_tail))
        return {
            TARGETS[0]: (self.head_Linf+tail_Linf).upper(),
            TARGETS[1]: (self.head_L2_squared+tail_L2**2).sqrt().upper(),
        }
