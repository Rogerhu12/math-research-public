"""BR first finite trial selection for the original target B inverse rows.

No certificate is asserted here. The declared Actions caller supplies the
whole BW signed w carrier and the midpoint of its original true phase ball.
The complete BR residual independently pays all finite and infinite errors.
"""
from fractions import Fraction

ROWS = 96
MODES = 192
W_MODES = 2048


def require(ok, message):
    if not ok:
        raise ValueError(message)


def choose_trial_bytes(np, positive_w_pairs, phase_midpoint):
    require(len(positive_w_pairs) == W_MODES
            and all(len(pair) == 2 for pair in positive_w_pairs),
            "all original signed w2048 trial pairs before finite proposal selection")
    require(np.isfinite(phase_midpoint), "one finite midpoint of the complete original phase")
    # These complex128 numbers only choose a trial. The exact rational w
    # carrier and the full true phase are used again in the directed residual.
    positive = np.array([complex(float(Fraction(a)), float(Fraction(b)))
                         for a, b in positive_w_pairs], dtype=np.complex128)
    require(bool(np.isfinite(positive).all()), "every complete finite coefficient is a finite proposal input")
    matrix = np.eye(MODES, dtype=np.complex128)
    for n in range(1, MODES+1):
        for ell in range(1, MODES+1):
            k = n-ell
            coefficient = (positive[k-1] if k > 0 else positive[-k-1].conjugate()
                           if k < 0 else complex(0))
            matrix[n-1, ell-1] -= coefficient/complex(0, 4*ell)
    forcing = np.zeros((MODES, ROWS), dtype=np.complex128)
    for j in range(1, ROWS+1):
        forcing[j-1, j-1] = (4*j/np.sqrt(2.0))*np.exp(complex(0, -2*j*phase_midpoint))
    fallback = None
    try:
        chosen = np.linalg.solve(matrix, forcing)
        if not bool(np.isfinite(chosen).all()):
            fallback = "the floating proposal contained nonfinite entries; exact zero trial retained"
            chosen = np.zeros((MODES, ROWS), dtype=np.complex128)
    except np.linalg.LinAlgError:
        fallback = "the floating proposal solve failed; exact zero trial retained"
        chosen = np.zeros((MODES, ROWS), dtype=np.complex128)
    values = np.empty((MODES, ROWS, 2), dtype="<f8")
    values[:, :, 0], values[:, :, 1] = chosen.real, chosen.imag
    require(values.shape == (MODES, ROWS, 2) and bool(np.isfinite(values).all()),
            "every selected trial coefficient is one finite exact binary64 dyadic")
    raw = values.tobytes(order="C")
    require(len(raw) == MODES*ROWS*2*8, "all192x96 complex coefficients with no omitted row")
    return raw, {"method": "one finite positive same-sign192-mode Galerkin proposal",
        "target": "Bdagger*y_j=4*j*sqrt(2)*cos(4*j*x-2*j*a)",
        "trial_shape": [MODES, ROWS, 2], "dtype": "<f8", "fallback": fallback,
        "negative_modes_are_exact_conjugates": True, "zero_mode_is_exact_zero": True,
        "finite_solve_is_a_full_operator_certificate": False}
