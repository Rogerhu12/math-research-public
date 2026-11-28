"""CFC: all original TC96 columns in the whole physical target space.

This is a new batch application of BFP/DCP, not another SC/JF target.
The original directed Box/FFT backend owns every floating operation.
Whole arrays are saved/read by the public owner before norm reduction.
The true target tail is an error in the infinite L2 space, never zero.
"""
from fractions import Fraction

COLS, SOURCE, TRIAL, W, IMAGE, GRID = 96, 96, 512, 2048, 2560, 8192
TARGETS = [
    "complete_TC96_finite_forward_residual_vector",
    "complete_TC96_true_full_target_error_vector",
    "complete_TC96_true_full_target_joint_error",
    "complete_TC96_true_stored_mean_pair",
    "complete_TC96_true_phase_row",
    "complete_TC96_true_actual_cap_height_row",
    "complete_TC96_true_height_reduced_phase_row",
    "complete_TC96_finite_Theta_matrix",
    "complete_TC96_true_Theta_matrix",
    "complete_TC96_original_coordinate_interface",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(value):
    require(value.is_finite() and value.upper() >= 0, "one entire finite upper")
    return value.upper()


def whole_real(c, values):
    """List-of-lists of Arb balls to the unchanged outward binary64 box."""
    require(values and values[0] and all(len(row) == len(values[0]) for row in values),
            "one complete rectangular scalar carrier")
    lo, hi = [], []
    for row in values:
        converted = [c.arb_box(v) for v in row]
        lo.append([float(v.lo) for v in converted])
        hi.append([float(v.hi) for v in converted])
    return c.finite(c.Box(c.np.array(lo), c.np.array(hi)))


def box_ball(c, value):
    require(value.lo.shape == (), "one entire scalar box")
    return c.arb(float(value.lo)).union(c.arb(float(value.hi)))


def box_vector(c, value):
    require(value.lo.ndim == 1 and value.lo.shape[0] == COLS,
            "all96 scalar outputs, in original source order")
    return [box_ball(c, value[j]) for j in range(COLS)]


def complex_columns(c, api, value):
    require(value.real.lo.ndim == 2 and value.real.lo.shape[1] == COLS,
            "the complete96 independent columns")
    return [[api.acb(box_ball(c, value.real[n, j]), box_ball(c, value.imag[n, j]))
             for n in range(value.real.lo.shape[0])] for j in range(COLS)]


def exact_pairs_box(c, pairs):
    require(len(pairs) == W and all(len(p) == 2 for p in pairs),
            "all2048 original exact Fourier pairs")
    return c.CBox(whole_real(c, [[c.exact(Fraction(p[0]))] for p in pairs]),
                  whole_real(c, [[c.exact(Fraction(p[1]))] for p in pairs]))


def finite_real_grid(c, positive):
    require(positive.real.lo.shape == (SOURCE, COLS),
            "the whole physical source degree96, all96 columns")
    z = c.zeros((GRID, COLS))
    z[1:SOURCE+1] = positive
    for n in range(1, SOURCE+1):
        z[-n] = c.CBox(positive.real[n-1], -positive.imag[n-1])
    return c.real(c.fft.fft(z, inverse=True)*GRID)


def choose_forward_trials(c, original_w_pairs, f_grid, whole_G, whole_Gprime):
    """One floating512x512 solve with all96 RHS, then exact dyadic trials.

    This selects an arbitrary finite trial. No accuracy is inferred from
    interpolation or this solve; every column receives its full residual.
    """
    np = c.np
    require(f_grid.lo.shape == (GRID, COLS) and len(whole_G) == len(whole_Gprime) == GRID,
            "all8192 complete physical input nodes and96 original columns")
    period = float(c.arb.pi()/2)
    x = np.arange(GRID, dtype=np.float64)*(period/GRID)
    g = np.array([float(v.mid()) for v in whole_G])
    gp = np.array([float(v.mid()) for v in whole_Gprime])
    require(np.all(np.isfinite(g)) and np.all(np.isfinite(gp)) and np.all(gp > 0),
            "one finite whole proposal grid")
    f = (f_grid.lo+f_grid.hi)/2
    rhs = np.zeros((TRIAL, COLS), dtype=np.complex128)
    for j in range(COLS):
        sampled = np.interp(x, g, f[:, j]/gp, period=period)
        rhs[:, j] = (np.fft.fft(sampled)/GRID)[1:TRIAL+1]
    w = [complex(float(Fraction(a)), float(Fraction(b))) for a, b in original_w_pairs]
    matrix = np.eye(TRIAL, dtype=np.complex128)
    for i in range(TRIAL):
        for j in range(TRIAL):
            k = i-j
            if k:
                v = w[abs(k)-1]
                matrix[i, j] += (v if k > 0 else v.conjugate())/complex(0, 4*(j+1))
    status = "all96_same_original_B_forward_floating_proposals"
    try:
        trial = np.linalg.solve(matrix, rhs)
        require(np.all(np.isfinite(trial)), "all512x96 finite exact-dyadic proposals")
    except (np.linalg.LinAlgError, ValueError):
        trial = np.zeros((TRIAL, COLS), dtype=np.complex128)
        status = "all96_explicit_zero_trials_after_failed_floating_proposal"
    return c.CBox(c.Box(trial.real.copy()), c.Box(trial.imag.copy())), {
        "status": status, "complete_shape": [TRIAL, COLS], "exact_mean": "0",
        "negative_modes_are_real_conjugates": True, "floating_solve_is_a_proof": False,
        "old_completed_scientific_targets_called": 0}


def complete_same_sign_image(c, original_pairs, source, sign):
    """Full directed convolution, no alias: support [-2047,2560].

    sign=+1 gives Bhat xhat; sign=-1 gives Ahat Gbar xhat.
    Only positive input modes occur in the positive same-sign block.
    The zero and negative coefficients of the multiplication are projected
    out after the full unaliased product, not omitted before multiplication.
    """
    require(sign in (-1, 1) and source.real.lo.shape == (TRIAL, COLS),
            "the declared full same-sign input and sign")
    w = exact_pairs_box(c, original_pairs)
    wz, iz = c.zeros((GRID, 1)), c.zeros((GRID, COLS))
    wz[1:W+1] = w
    for n in range(1, W+1):
        wz[-n] = c.CBox(w.real[n-1], -w.imag[n-1])
    for n in range(1, TRIAL+1):
        iz[n] = source[n-1]*c.CBox(0., c.arb_box(-c.arb(1)/(4*n)))
    product = (c.fft.fft(c.fft.fft(wz, inverse=True)*GRID
                        *(c.fft.fft(iz, inverse=True)*GRID))/GRID)
    image = product[1:IMAGE+1]*sign
    image[:TRIAL] = image[:TRIAL]+source
    require(image.real.lo.shape == (IMAGE, COLS), "all2560x96 signed image coefficients")
    c.finite(image.real); c.finite(image.imag)
    return image


def evaluate_all_unit_circle_columns(c, whole_grid, coefficients, progress, checkpoint, stage):
    """All positive polynomials at all nodes, sharing exact dyadic powers.

    Powers are repeatedly recentered. Their radii use |exp(4it)|=1,
    so no repeated rectangular multiplication can grow as sqrt(2)^n.
    Every term of every column, and its full disk error, is included.
    """
    require(len(whole_grid) == GRID and coefficients.real.lo.shape == (IMAGE, COLS),
            "all8192 complete angles and all2560x96 coefficients")
    np = c.np
    step = c.CBox(whole_real(c, [[(4*g).cos()] for g in whole_grid]),
                  whole_real(c, [[(4*g).sin()] for g in whole_grid]))

    def midpoint(z):
        return c.CBox(c.Box(z.real.lo+(z.real.hi-z.real.lo)/2),
                      c.Box(z.imag.lo+(z.imag.hi-z.imag.lo)/2))

    step_center = midpoint(step)
    tau = c.Box((step-step_center).magnitude_upper())
    power, radius = c.CBox(c.Box(np.ones((GRID, 1)))), c.Box(np.zeros((GRID, 1)))
    values, errors = c.zeros((GRID, COLS)), c.Box(np.zeros((GRID, COLS)))
    for n in range(1, IMAGE+1):
        product = power*step_center
        center = midpoint(product)
        rounding = c.Box((product-center).magnitude_upper())
        radius = c.add_upper(radius, c.mul_upper(c.add_upper(c.Box(1.), radius), tau), rounding)
        power = center
        coefficient = coefficients[n-1:n]
        values = values+center*coefficient
        errors = c.add_upper(errors, c.mul_upper(radius, c.Box(coefficient.magnitude_upper())))
        if n % 64 == 0 or n == IMAGE:
            checkpoint(stage, {"complete_modes": n, "total_modes": IMAGE,
                "all_original_columns": COLS}, power=power, radius=radius, values=values, errors=errors)
            progress(stage, {"complete_modes": n, "total_modes": IMAGE, "complete_columns": COLS})
    answer = values.pad(errors)
    c.finite(answer.real); c.finite(answer.imag)
    return answer


def complete_batch_forward(bundle, io, progress):
    c, api, pure = bundle["c"], bundle["api"], bundle["BFP_math"]
    positive, G, Gp = bundle["physical_coefficients"], bundle["G"], bundle["Gprime"]
    require(positive.real.lo.shape == (SOURCE, COLS), "all original TC physical coefficients")
    fgrid = io.real("complete_TC96_physical_grid", finite_real_grid(c, positive))
    trial, proposal = choose_forward_trials(c, bundle["w_pairs"], fgrid, G, Gp)
    trial = io.complex("complete_TC96_forward_exact_trial", trial, exact=True)
    io.json("complete_TC96_trial_proposal", proposal)
    image = io.complex("complete_TC96_forward_image", complete_same_sign_image(c, bundle["w_pairs"], trial, 1))
    values = evaluate_all_unit_circle_columns(c, G, image, progress, io.checkpoint,
                                             "complete_TC96_forward_pullback")
    values = io.complex("complete_TC96_forward_pullback_values", values)
    gp = whole_real(c, [[v] for v in Gp])
    require(c.np.all(gp.lo > 0), "the whole analytic-chain Jacobian is positive")
    residual = 2*values.real*gp-fgrid
    absolute = c.absolute(residual)
    integrands = io.real("complete_TC96_forward_pullback_square", absolute*absolute/gp)
    squares = box_vector(c, c.upper(c.reduce_box(integrands, axis=0)/GRID))
    image_columns, source_columns = complex_columns(c, api, image), complex_columns(c, api, positive)
    trial_columns = complex_columns(c, api, trial)
    records, errors, finite = [], [], []
    sigma, b = api.rational(1, 128), bundle["bounds"]
    for j in range(COLS):
        z, r, f = trial_columns[j], image_columns[j], source_columns[j]
        n0 = (2*sum((abs(x).upper()**2 for x in z), api.zero)).sqrt().upper()
        i2 = (2*sum((abs(x).upper()**2/(4*n)**2 for n, x in enumerate(z, 1)), api.zero)).sqrt().upper()
        iw = sum((abs(x).upper()/(4*n) for n, x in enumerate(z, 1)), api.zero).upper()
        Ar = sum((2*abs(x).upper()*(4*n*(sigma+upper(b["G0"]))).exp()
                  for n, x in enumerate(r, 1)), api.zero).upper()
        Af = sum((2*abs(x).upper()*(4*n*sigma).exp()
                  for n, x in enumerate(f, 1)), api.zero).upper()
        require(upper(b["G1"]) < 2, "the original whole analytic derivative")
        alias = ((-4*GRID*sigma).exp()*(upper(b["G1"])*Ar+Af)**2/(2-upper(b["G1"]))).upper()
        rho = pure.complete_finite_forward_residual(squares[j], alias)
        products = pure.complete_whole_w_products(api, b["w_Linf"], b["w_L2"], i2, iw)
        selected, product = pure.choose_whole_w_product(products[pure.TARGETS[8]], products[pure.TARGETS[9]])
        # ||(I w+ + I w-)/2|| <= ||whole waist density||/sqrt2.
        N0 = (upper(bundle["waist_trial_norms"][j])/api.rational(2).sqrt()).upper()
        flow = pure.complete_whole_flow_density_error(api, b["EH"], N0, b["G1"], b["H1"], b["m"])
        pde = pure.complete_true_PDE_density_error(api, b["BH"], bundle["waist_errors"][j])
        whole = pure.complete_true_forward_residual(rho, product, flow, pde)
        delta = pure.complete_true_target_column_error(b["B_inverse"], whole)
        records.append({"trial_L2": n0, "primitive_L2": i2, "primitive_positive_Wiener": iw,
            "quadrature_square": upper(squares[j]), "alias_square": alias,
            "finite_residual": rho, "whole_w_Linf_product": products[pure.TARGETS[8]],
            "whole_w_L2_product": products[pure.TARGETS[9]], "chosen_w_product": selected,
            "whole_flow_error": flow, "whole_PDE_error": pde,
            "whole_B_residual": whole, "whole_target_error": delta})
        errors.append(delta); finite.append(rho)
    coords = []
    true_a = bundle["true_a"]
    for n in range(1, TRIAL+1):
        angle = 2*n*true_a
        coords.append([api.rational(2).sqrt()*(trial_columns[j][n-1].real*angle.cos()
                       -trial_columns[j][n-1].imag*angle.sin()) for j in range(COLS)])
    coordinates = io.real("complete_TC96_true_target_coordinates", whole_real(c, coords))
    errors = [upper(v) for v in io.real_vector("complete_TC96_whole_target_errors96", errors)]
    finite = [upper(v) for v in io.real_vector("complete_TC96_finite_forward_residuals96", finite)]
    joint = sum((upper(v)**2 for v in errors), api.zero).sqrt().upper()
    return {"trial": trial, "coordinates": coordinates, "errors": errors, "joint": joint,
            "finite_residuals": finite, "complete_column_records": records}


def complete_batch_Theta(bundle, forward, io, progress):
    """The complete DCP receiver on every original TC column, all tails kept."""
    c, api, pure = bundle["c"], bundle["api"], bundle["DCP_math"]
    coordinates = forward["coordinates"]
    coordinate_columns = [[box_ball(c, coordinates[n, j]) for n in range(TRIAL)] for j in range(COLS)]
    sources = [pure.complete_model_source(api, row, bundle["model2240"], bundle["source_b"])
               for row in coordinate_columns]
    source = c.CBox(whole_real(c, [[sources[j][n].real for j in range(COLS)] for n in range(TRIAL)]),
                    whole_real(c, [[sources[j][n].imag for j in range(COLS)] for n in range(TRIAL)]))
    source = io.complex("complete_TC96_original_model_sources", source)
    v = io.complex("complete_TC96_full_A_model_images",
                   complete_same_sign_image(c, bundle["alpha_pairs"], source, -1))
    primitive = c.zeros((IMAGE, COLS))
    for n in range(1, IMAGE+1):
        primitive[n-1] = v[n-1]*c.CBox(0., c.arb_box(-c.arb(1)/(4*n)))
    primitive = io.complex("complete_TC96_full_positive_primitives", primitive)
    values = evaluate_all_unit_circle_columns(c, bundle["phat_grid"], primitive, progress,
                                             io.checkpoint, "complete_TC96_DCP_primitive_grid")
    values = io.complex("complete_TC96_DCP_complete_samples", values)
    transformed = io.complex("complete_TC96_DCP_complete_FFT", c.fft.fft(values))
    v_columns, transforms = complex_columns(c, api, v), complex_columns(c, api, transformed)
    model_columns = complex_columns(c, api, source)
    records, finite_errors, true_errors, centers = [], [], [], []
    positive_rows, opposite_rows = [], []
    b = bundle["bounds"]
    for j in range(COLS):
        norms = pure.complete_source_norms(api, v_columns[j], b["phat_derivative_perturbation"])
        mn = pure.complete_model_primitive_norms(api, model_columns[j])
        products = pure.complete_alpha_source_products(api, b["IR_H"], b["IR_L2"],
            b["UACT_inverse_Linf_product"], b["UACT_inverse_L2_product"], mn[pure.TARGETS[5]], mn[pure.TARGETS[6]])
        positive, opposite = pure.complete_signed_heads(api, transforms[j], norms[pure.TARGETS[3]], norms[pure.TARGETS[4]])
        # Retain every signed readout and opposite coefficient before norms.
        positive = io.complex_vector("complete_TC96_DCP_positive_%03d"%(j+1), positive)
        opposite = io.complex_vector("complete_TC96_DCP_opposite_%03d"%(j+1), opposite)
        positive_rows.append(positive); opposite_rows.append(opposite)
        head = pure.complete_leakage_head(api, opposite)
        tail = pure.complete_leakage_tail(api, norms[pure.TARGETS[3]])
        map_error = pure.complete_true_map_energy_error(api, b["Ep"], norms[pure.TARGETS[1]], norms[pure.TARGETS[2]])
        leakage = pure.complete_true_leakage(head, tail, map_error)
        signed, center, radius = pure.complete_readout_centers(api, positive)
        signed = io.real_vector("complete_TC96_DCP_signed_%03d"%(j+1), signed)
        radius = sum((abs(value-point).upper()**2 for value,point in zip(signed,center)), api.zero).sqrt().upper()
        chosen = min(products, key=lambda key: upper(products[key]))
        finite = pure.complete_finite_Theta_error(api, leakage, map_error, products[chosen], radius)
        true = pure.complete_full_true_nu_error(finite, b["Theta_trial_norm"], b["Theta_global_error"], forward["errors"][j])
        records.append({"full_v_L2": norms[pure.TARGETS[1]], "full_v_D1_L2": norms[pure.TARGETS[2]],
            "positive_primitive_Wiener": norms[pure.TARGETS[3]], "lower_strip_primitive": norms[pure.TARGETS[4]],
            "model_primitive_L2": mn[pure.TARGETS[5]], "model_primitive_positive_Wiener": mn[pure.TARGETS[6]],
            "whole_alpha_Linf_product": products[pure.TARGETS[7]],
            "whole_alpha_L2_product": products[pure.TARGETS[8]], "chosen_alpha_product": chosen,
            "opposite_head": head, "opposite_infinite_tail": tail, "true_map_error": map_error,
            "true_full_opposite_leakage": leakage, "pairing_radius": radius,
            "finite_Theta_error": finite, "whole_true_Theta_error": true})
        finite_errors.append(finite); true_errors.append(true); centers.append(center)
        if (j+1) % 4 == 0:
            progress("complete_TC96_original_Theta_readout", {"complete_columns": j+1, "total_columns": COLS})
    original_centers = io.json("complete_TC96_Theta_Arb_centers", {
        "rows":COLS,"columns":COLS,"all_mantissa_exponent_pairs":[
            [list(map(int,centers[j][i].man_exp())) for j in range(COLS)] for i in range(COLS)]})
    centers = [[api.rational(Fraction(original_centers["all_mantissa_exponent_pairs"][i][j][0])
        *Fraction(2)**original_centers["all_mantissa_exponent_pairs"][i][j][1])
        for i in range(COLS)] for j in range(COLS)]
    finite_errors = [upper(v) for v in io.real_vector("complete_TC96_finite_Theta_errors96",finite_errors)]
    true_errors = [upper(v) for v in io.real_vector("complete_TC96_true_Theta_errors96",true_errors)]
    chosen = c.np.array([[float(centers[j][i]) for j in range(COLS)] for i in range(COLS)])
    center_matrix = io.real("complete_TC96_Theta_exact_centers", c.Box(chosen), exact=True)
    # Conversion to binary64 adds a full Frobenius error, charged here.
    conversion = sum((abs(box_ball(c, center_matrix[i, j])-centers[j][i]).upper()**2
        for i in range(COLS) for j in range(COLS)), api.zero).sqrt().upper()
    return {"centers": center_matrix, "finite_errors": finite_errors, "true_errors": true_errors,
        "finite_joint": (sum((upper(x)**2 for x in finite_errors), api.zero).sqrt()+conversion).upper(),
        "true_joint": (sum((upper(x)**2 for x in true_errors), api.zero).sqrt()+conversion).upper(),
        "center_conversion": conversion, "complete_column_records": records}


def complete_scalar_rows(bundle, io):
    """New PDE correction of saved AP96/H96 rows, no old integration.

    The first SC execution passively preserves every already-computed
    e_j=sqrt(d_j^2+z_j^2), with its whole original P224/TC identity.
    These complete saved records are copied without a new root/waist call.
    The independent geometric/world ports are not removed by this block.
    """
    api, c = bundle["api"], bundle["c"]
    require(len(bundle["root_errors"]) == len(bundle["negative_root"])
            == len(bundle["negative_strict"]) == COLS,
            "the complete same-first-SC root96 and original negative residual vectors")
    phase, height, reduced = [], [], []
    receivers = bundle["row_receivers"]
    require(set(receivers) == {"phase","height","reduced_phase"}
            and all(len(row)==4 and all(v.is_finite() and v.lower()>=0 for v in row)
                    for row in receivers.values()),
            "all original root/negative/strict/impulse coefficients from the complete same-rho consumer")
    for e, Fn, Fs in zip(bundle["root_errors"], bundle["negative_root"], bundle["negative_strict"]):
        e = upper(e)
        for name,values in (("phase",phase),("height",height),("reduced_phase",reduced)):
            r=receivers[name]
            # The original continuous TC trial has exact zero J_strict.
            values.append((upper(r[0])*e+upper(r[1])*upper(Fn)+upper(r[2])*upper(Fs)).upper())
    errors = {"phase": phase, "height": height, "reduced_phase": reduced}
    result = {}
    for name, corrections in errors.items():
        whole = bundle["saved_rows"][name]
        require(len(whole["centers"]) == COLS, "every signed original trial row entry")
        body = io.json("complete_TC96_"+name+"_exact_centers", {
            "complete_count":COLS,"all_exact_dyadic_centers":list(whole["centers"])})
        centers = [api.rational(Fraction(x)) for x in body["all_exact_dyadic_centers"]]
        corrections = [upper(v) for v in io.real_vector("complete_TC96_"+name+"_PDE_corrections96",corrections)]
        radius = (upper(whole["joint_radius"])+sum((x*x for x in corrections), api.zero).sqrt()).upper()
        result[name] = {"centers": centers, "whole_joint_error": radius,
            "new_PDE_correction_bounds": corrections, "same_trial_joint_error": whole["joint_radius"]}
    require(bundle["stored_means"].lo.shape == (2, COLS), "both original stored means of all96 columns")
    means = io.real("complete_TC96_stored_mean_pair", bundle["stored_means"])
    center = c.Box(means.lo+(means.hi-means.lo)/2)
    center = io.real("complete_TC96_stored_mean_pair_centers", center, exact=True)
    finite = sum((abs(box_ball(c, means[i, j])-box_ball(c, center[i, j])).upper()**2
        for i in range(2) for j in range(COLS)), api.zero).sqrt().upper()
    joint = (finite+sum((upper(x)**2 for x in bundle["waist_errors"]), api.zero).sqrt()).upper()
    result["means"] = {"centers": center, "whole_joint_error": joint,
        "both_stored_coordinates_retained": True, "physical_mean_rank": 1,
        "two_independent_free_mean_unknowns_claimed": False}
    return result
