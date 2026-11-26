"""SL.9--10: original negative receiver with the true compact nu support.

Pure directed arithmetic definitions, with no import, IO or work at import.
The caller supplies WHOLE saved upper endpoints from the same completed
S0/D/SP/R147 objects; publish returns the upper of each formally saved ball.
"""

TARGETS = (
    "compact_parameter_source_L2_to_waist_gain_upper",
    "selected_base_and_state_change_negative_waist_upper",
    "selected_compact_parameter_change_negative_waist_upper",
    "selected_support_localized_negative_nu_ordinary_waist_upper",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def receive(api, saved, publish):
    require(set(saved) == {"S_N", "A_N", "N_C", "C1", "G_N"},
            "all five complete saved source and receiver inputs")
    require(all(value.is_finite() and value >= api.zero
                for value in saved.values()),
            "finite nonnegative complete saved upper endpoints")
    ratio = api.rational(936826, 1000000)
    length = api.rational(13, 100)
    compact = publish(TARGETS[0], (saved["C1"]*api.sqrt(length)).upper())
    ordinary = publish(TARGETS[1], (
        saved["G_N"]*(saved["S_N"]+ratio*saved["A_N"])).upper())
    metric = publish(TARGETS[2], (compact*ratio*saved["N_C"]).upper())
    whole = publish(TARGETS[3], (ordinary+metric).upper())
    return {"localized_receiver": compact, "noncompact_contribution": ordinary,
            "compact_parameter_contribution": metric,
            "complete_negative_ordinary_contribution": whole}
