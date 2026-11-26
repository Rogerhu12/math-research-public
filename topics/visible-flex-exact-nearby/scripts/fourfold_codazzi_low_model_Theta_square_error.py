"""TQL: complete low96 model-action radius and the same Theta-square error.

Only NEW restriction bounds. No old IR/AS/OT norm or producer is called.
The owner admits/restores BOTH entire96x2240 original carriers first.
"""

ROWS = 96
ALL_MODES = 2240


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(value):
    require(value.is_finite() and value.lower() >= 0,
            "the complete nonnegative saved upper")
    return value.upper()


def complete_low_model_radius(api, all_original_balls, all_original_dyadics):
    require(type(all_original_balls) is list and type(all_original_dyadics) is list
            and len(all_original_balls) == len(all_original_dyadics) == ROWS
            and all(type(row) is list and len(row) == ALL_MODES
                    for row in all_original_balls+all_original_dyadics),
            "both entire96x2240 original carriers, never just the low square")
    require(all(value.is_finite() for row in all_original_balls for value in row)
            and all(value.is_finite() and value.lower() == value.upper()
                    for row in all_original_dyadics for value in row),
            "every formal real ball and every original exact dyadic point")
    square = api.zero
    for j in range(ROWS):
        for n in range(ROWS):
            radius = api.magnitude(all_original_balls[j][n]-all_original_dyadics[j][n])
            square = square+radius*radius
    return square.sqrt().upper()


def complete_low_candidate(api, saved_VQ_error, saved_whole_low_model_radius):
    """Original Gbar E96 is an exact isometry; every full VQ tail remains."""
    return (upper(saved_VQ_error)+upper(saved_whole_low_model_radius)).upper()


def select_whole_saved_candidate(saved_global_error, saved_low_error):
    """Call only after BOTH complete same-square candidates were saved/read."""
    candidates = {"whole_original_global_Theta_error": upper(saved_global_error),
                  "whole_exact_low_model_Theta_error": upper(saved_low_error)}
    selected = min(candidates, key=lambda name: candidates[name])
    return selected, candidates[selected]
