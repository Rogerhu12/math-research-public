"""TM: actual WFI graph-model adjoint on all96 complete finite DT rows.

Pure formulas, no imports, producer, saved norm or Cayley gap replay.
The genuine target basis is v_n^a, a=2 true H(0), b=a+Omega.
The low reference is exactly one on n1..96, never an unproved low inverse.
"""

ROWS = 96
LOW_REFERENCE_MODES = 96


def require(ok, message):
    if not ok:
        raise ValueError(message)


def complete_original_model_rows(api, positive_original_Astar_rows, omega, source_b, original_mu):
    """Return all real normalized-Y_a coefficient balls and full multipliers.

    Every input row has the entire M+K support. The outer owner must first
    admit the complete same-parameter CYA result and its infinite scope.
    This function does not redo the old distance/gap certificate.
    """
    require(len(positive_original_Astar_rows) == ROWS, "all96 whole DT rows")
    extent = len(positive_original_Astar_rows[0])
    require(extent > LOW_REFERENCE_MODES
            and all(len(row) == extent for row in positive_original_Astar_rows)
            and all(value.is_finite() for row in positive_original_Astar_rows for value in row),
            "the entire common finite support, including both same-sign products")
    require(omega.is_finite() and source_b.is_finite() and original_mu.is_finite(),
            "all original signed mean and true reflection phase balls")
    nu = -original_mu/2
    root2 = api.rational(2).sqrt()
    rows = [[] for _ in range(ROWS)]
    model = []
    for n in range(1, extent+1):
        phase = 2*n*source_b+api.arb.pi()/4
        cosine, sine = phase.cos(), phase.sin()
        if n <= LOW_REFERENCE_MODES:
            denominator, reciprocal = api.one, api.one
            kind = "original_Llow_reference"
        else:
            theta = 2*n*omega+api.arb.pi()/4
            denominator = theta.cos()-nu*theta.sin()/(4*n)
            require(denominator.is_finite() and not denominator.contains(0),
                    "signed actual model division in its already certified high scope")
            reciprocal = 1/denominator
            kind = "original_Mnu_high_reciprocal"
        model.append({"mode": n, "kind": kind, "signed_denominator": denominator,
                      "signed_reciprocal": reciprocal, "true_source_phase": phase})
        for j, row in enumerate(positive_original_Astar_rows):
            coefficient = row[n-1]
            paired = root2*(coefficient.real*cosine-coefficient.imag*sine)
            value = reciprocal*paired
            require(value.is_finite(), "one whole real normalized-Y_a Theta coefficient")
            rows[j].append(value)
    return rows, model


def complete_model_rounding_error(api, all_formal_ball_rows, all_exact_trial_rows):
    """TM.8 after saving and reading every complete real coefficient row."""
    require(len(all_formal_ball_rows) == len(all_exact_trial_rows) == ROWS,
            "all96 entire formal real row carriers")
    extent = len(all_formal_ball_rows[0])
    require(extent > 0 and all(len(row) == extent for row in all_formal_ball_rows)
            and all(len(row) == extent for row in all_exact_trial_rows),
            "every full original finite model output")
    square = api.zero
    row_squares = []
    for balls, trial in zip(all_formal_ball_rows, all_exact_trial_rows):
        one = api.zero
        for ball, point in zip(balls, trial):
            require(ball.is_finite() and point.is_finite(), "whole saved model ball and chosen exact trial")
            radius = abs(ball-point).upper()
            one = one+radius*radius
        row_squares.append(one.upper())
        square = square+one
    return square.sqrt().upper(), row_squares


def complete_original_Theta_error(api, whole_DT_one_loss_error, whole_model_rounding_error):
    require(all(value.is_finite() and value.lower() >= 0
                for value in (whole_DT_one_loss_error, whole_model_rounding_error)),
            "both complete same-operator error records")
    return (whole_DT_one_loss_error.upper()+whole_model_rounding_error.upper()).upper()
