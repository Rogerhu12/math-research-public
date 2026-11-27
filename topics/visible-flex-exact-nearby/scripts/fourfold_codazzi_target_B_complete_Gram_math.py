"""BGR: new complete Gram norm of the same immutable DWTB96 row trial.

Pure directed formulas. The owner restores whole original carrier SHA,
saves every signed Gram entry, reads the complete array, and only then
runs the new operator bound. No old HS/w/residual target is recomputed.
"""
from fractions import Fraction

ROWS, MODES = 96, 192
TARGETS = [
    "complete_DWTB_trial_primitive_Gram_operator_upper",
    "complete_DWTB_target_w_Linf_operator_product_upper",
    "complete_DWTB_inverse96_Gram_row_error_upper",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(value):
    require(value.is_finite() and value.lower() >= 0,
            "one complete finite nonnegative saved upper")
    return value.upper()


def complete_signed_Gram(api, whole_original_exact_row_pairs):
    """All9216 real entries, with all192 positive modes and both signs."""
    require(len(whole_original_exact_row_pairs) == ROWS
            and all(len(row) == MODES for row in whole_original_exact_row_pairs),
            "the entire original96x192 row carrier, after its full SHA gate")
    values = []
    for row in whole_original_exact_row_pairs:
        parsed = []
        for pair in row:
            require(len(pair) == 2, "both whole exact rational components")
            a, b = map(Fraction, pair)
            parsed.append(api.acb(api.rational(a), api.rational(b)))
        values.append(parsed)
    matrix = []
    for j in range(ROWS):
        row = []
        for k in range(ROWS):
            value = api.zero
            for n in range(MODES):
                left = api.acb(values[j][n].real, -values[j][n].imag)
                value = value+2*(left*values[k][n]).real
            require(value.is_finite(), "one whole signed Gram entry")
            row.append(value)
        matrix.append(row)
    return matrix


def complete_Gram_operator_upper(api, saved_whole_Gram):
    """BGR.4. Every actual signed sum must have been saved and read first."""
    require(len(saved_whole_Gram) == ROWS
            and all(len(row) == ROWS for row in saved_whole_Gram)
            and all(value.is_finite() for row in saved_whole_Gram for value in row),
            "all9216 complete signed real Gram balls")
    row_sums = []
    for j, row in enumerate(saved_whole_Gram):
        require(row[j].upper() >= 0,
                "the complete diagonal contains a squared norm")
        total = row[j].upper()
        for k, value in enumerate(row):
            if k != j:
                total = total+abs(value).upper()
        row_sums.append(total.upper())
    return max(row_sums).sqrt().upper()


def complete_new_infinity_product(saved_w_Linf_error, saved_Gram_operator_upper):
    return (upper(saved_w_Linf_error)*upper(saved_Gram_operator_upper)).upper()


def choose_complete_primitive_operator_upper(saved_Gram_operator_upper, old_HS_upper):
    """Both bound the same complete operator; the old HS target is not rerun."""
    records = {"new_complete_Gram": upper(saved_Gram_operator_upper),
               "original_complete_Hilbert_Schmidt": upper(old_HS_upper)}
    selected = min(records, key=records.__getitem__)
    return selected, records[selected]


def choose_complete_product(saved_new_product, old_Linf_product, old_L2_product):
    records = {"new_complete_Gram_Linf_product": upper(saved_new_product),
               "original_complete_HS_Linf_product": upper(old_Linf_product),
               "original_complete_L2_product": upper(old_L2_product)}
    selected = min(records, key=records.__getitem__)
    return selected, records[selected]


def complete_new_row_error(saved_whole_finite_energy_residual, saved_selected_product):
    return (upper(saved_whole_finite_energy_residual)/2
            +upper(saved_selected_product)/4).upper()


def choose_complete_row_error(saved_new_row_error, old_complete_row_error):
    records = {"new_complete_Gram_row_error": upper(saved_new_row_error),
               "original_complete_DWTB_row_error": upper(old_complete_row_error)}
    selected = min(records, key=records.__getitem__)
    return selected, records[selected]



def complete_new_parameter_row_fee(saved_new_row_error, saved_BH, saved_physical_N0):
    """A genuinely new weighted product after the whole BGR3 and BNC7."""
    return (upper(saved_new_row_error)*upper(saved_BH)*upper(saved_physical_N0)).upper()


def complete_refined_parameter_column_error(api, whole_original_component_order,
                                             whole_saved_original_components,
                                             saved_new_row_fee):
    """Keep the other FOUR whole original fees; do not subtract old uppers."""
    require(len(whole_original_component_order) == 5
            and whole_original_component_order[0] == "complete_target_B_row_error_on_NP_trial_upper"
            and set(whole_saved_original_components) == set(whole_original_component_order),
            "all five whole original BNC components, after actual complete7")
    original = {name: upper(value) for name, value in whole_saved_original_components.items()}
    return (upper(saved_new_row_fee)+sum(
        (original[name] for name in whole_original_component_order[1:]), api.zero)).upper()
