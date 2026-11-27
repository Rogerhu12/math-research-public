"""GYN: new whole GY induced operator norm; no old HS target is repeated."""

POSITIVE_MODES = 192
COLUMNS = 96
REAL_ROWS = 384
TARGETS = ["complete_G_trial_real_matrix_infinity_upper",
           "complete_G_trial_real_matrix_one_upper",
           "complete_G_trial_real_matrix_Schur_two_upper"]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(value):
    require(value.is_finite() and value.lower() >= 0, "one whole nonnegative directed upper")
    return value.upper()


def complete_original_GY_real_matrix(api, original_columns):
    require(type(original_columns) is list and len(original_columns) == COLUMNS
            and all(type(column) is list and len(column) == POSITIVE_MODES for column in original_columns),
            "all original96 columns and all192 positive modes, after the whole trial SHA")
    require(all(value.is_finite() and value.real.is_exact() and value.imag.is_exact()
                for column in original_columns for value in column),
            "every signed original trial coefficient is an exact dyadic")
    root_two = api.rational(2).sqrt()
    rows = []
    for n in range(1, POSITIVE_MODES+1):
        rows.append([root_two*column[n-1].real/(4*n) for column in original_columns])
        rows.append([-root_two*column[n-1].imag/(4*n) for column in original_columns])
    require(len(rows) == REAL_ROWS and all(value.is_finite() for row in rows for value in row),
            "the entire384-by96 normalized real Fourier matrix")
    return rows


def complete_induced_norms(api, whole_saved_real_matrix):
    require(type(whole_saved_real_matrix) is list and len(whole_saved_real_matrix) == REAL_ROWS
            and all(type(row) is list and len(row) == COLUMNS for row in whole_saved_real_matrix)
            and all(value.is_finite() for row in whole_saved_real_matrix for value in row),
            "all36864 formal signed matrix balls before absolute values")
    magnitudes = [[abs(value).upper() for value in row] for row in whole_saved_real_matrix]
    infinity = max(sum(row, api.zero).upper() for row in magnitudes)
    one = max(sum((row[j] for row in magnitudes), api.zero).upper() for j in range(COLUMNS))
    return {TARGETS[0]: infinity, TARGETS[1]: one}


def complete_Schur_from_saved_norms(api, saved_infinity, saved_one):
    return (upper(saved_infinity)*upper(saved_one)).sqrt().upper()


def select_whole_saved_operator_candidate(saved_new_Schur, saved_old_Hilbert_Schmidt):
    values = {"new_complete_GY_operator_Schur": upper(saved_new_Schur),
              "old_complete_GY_Hilbert_Schmidt": upper(saved_old_Hilbert_Schmidt)}
    name = min(values, key=lambda key: values[key])
    return name, values[name]


class WholeContractedProducts:
    """UDR whole products with the newly qualified full GY operator norm.

    This explicitly changes the input's meaning from HS to operator norm;
    the frozen UDR source is neither modified nor given a mislabelled HS.
    """
    def __init__(self, api, *, saved_G_operator, saved_G_positive_W, saved_IR_H, saved_IR_L2):
        self.api = api
        self.J, self.W, self.H, self.e0 = map(upper, (
            saved_G_operator, saved_G_positive_W, saved_IR_H, saved_IR_L2))
        self.S = (api.rational(51, 50)*(self.e0+api.rational(10, 9)*self.H)).upper()
        self.next_n = 1
        self.finf = self.f2square = self.einf = self.e2square = api.zero

    def append(self, n, saved_complete_mode_residual):
        require(n == self.next_n and 1 <= n <= 2048, "all2048 original signed residual modes in order")
        delta = upper(saved_complete_mode_residual)
        self.finf = (self.finf+2*delta*self.J).upper()
        self.f2square = (self.f2square+4*delta*delta*self.W*self.W).upper()
        self.einf = (self.einf+delta*self.H).upper()
        self.e2square = (self.e2square+2*delta*delta*self.S*self.S/9).upper()
        self.next_n += 1

    def finish(self, saved_original_whole_tail_Linf, saved_original_whole_tail_L2):
        require(self.next_n == 2049, "no prefix substitutes for the whole original trial/tail product")
        tail0, tail2 = map(upper, (saved_original_whole_tail_Linf, saved_original_whole_tail_L2))
        return {
            "complete_unit_disk_alpha_finite_Linf_product_upper": (self.finf+tail0*self.J).upper(),
            "complete_unit_disk_alpha_finite_L2_product_upper":
                (self.f2square+2*tail2*tail2*self.W*self.W).sqrt().upper(),
            "complete_unit_disk_alpha_inverse_error_Linf_product_upper": (self.einf+tail0*self.H/2).upper(),
            "complete_unit_disk_alpha_inverse_error_L2_product_upper":
                (self.e2square+tail2*tail2*self.S*self.S/9).sqrt().upper(),
        }
