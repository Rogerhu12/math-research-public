"""New complete weighted-model Theta receiver on the original IR/UACT data.

Only the declared new Gram, derivative residual and weighted model targets
are evaluated. No original IR residual norm, UACT product or BFP column
target is called. All infinite residuals remain paid by explicit tails.
"""
ROWS, MODES, GRID, HEAD, MODEL_HEAD = 96, 192, 8192, 2048, 1048576
ALPHA_MODES = 2048
TARGETS = [
    "complete_original_IR_Y_L2_Gram_upper",
    "complete_original_IR_Y_D1_Gram_upper",
    "complete_original_IR_Y_D2_Gram_upper",
    "complete_original_IR_positive_primitive_strip_vector_upper",
    "complete_original_IR_D1_residual_head_Gram_upper",
    "complete_original_IR_D1_residual_infinite_tail_upper",
    "complete_original_IR_D1_true_map_error_upper",
    "complete_original_IR_D1_true_residual_upper",
    "complete_original_IR_true_inverse_error_D1_upper",
    "complete_original_alpha_D1_infinite_tail_upper",
    "complete_original_VQ_joint_D2_error_upper",
    "complete_original_model_D1_head_weight_upper",
    "complete_original_model_D2_infinite_weight_upper",
    "complete_original_Theta_weighted_model_joint_L2_error_upper",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def up(value):
    require(value.is_finite() and value.upper() >= 0, "one finite nonnegative complete upper")
    return value.upper()


def whole_Gram(api, columns, derivative, expected_modes):
    """All signed entries, retaining both normalized Fourier signs."""
    require(len(columns) == ROWS and all(len(c) == expected_modes for c in columns)
            and derivative in (0, 1, 2)
            and all(v.is_finite() for c in columns for v in c),
            "all96 complete original real-conjugate columns")
    weights = [api.rational(2*(4*n)**(2*derivative)) for n in range(1, expected_modes+1)]
    result = [[None for _ in range(ROWS)] for _ in range(ROWS)]
    for j in range(ROWS):
        for k in range(j, ROWS):
            value = sum((weight*(a.real*b.real+a.imag*b.imag)
                         for weight, a, b in zip(weights, columns[j], columns[k])), api.zero)
            require(value.is_finite(), "one entire signed Gram contraction")
            result[j][k] = result[k][j] = value
    return result


def saved_Gram_operator_upper(api, whole_saved_Gram):
    require(len(whole_saved_Gram) == ROWS and all(len(r) == ROWS for r in whole_saved_Gram)
            and all(v.is_finite() for r in whole_saved_Gram for v in r),
            "all9216 formal Gram entries saved/read before the norm")
    rows = [(whole_saved_Gram[j][j].upper()+sum(
        (abs(whole_saved_Gram[j][k]).upper() for k in range(ROWS) if k != j), api.zero)).upper()
        for j in range(ROWS)]
    maximum = max(rows)
    require(maximum >= 0, "the whole positive Gram has a nonnegative eigenvalue upper")
    return maximum.sqrt().upper()


def complete_primitive_vector_strip(api, columns, whole_image_width):
    require(len(columns) == ROWS and all(len(c) == MODES for c in columns), "all original192 by96 inputs")
    width, total = up(whole_image_width), api.zero
    for n in range(1, MODES+1):
        vector = sum((abs(c[n-1]).upper()**2 for c in columns), api.zero).sqrt().upper()
        total += vector*(4*n*width).exp()/(4*n)
    return total.upper()


def complete_new_grid(api, whole_original_grid, terminal_side, K_sines, K_cosines):
    """Reuse all4096 original nodes; add the4096 new interleaved nodes."""
    require(len(whole_original_grid) == 4096 and len(terminal_side) == 129
            and len(K_sines) == len(K_cosines) == 48 and terminal_side[64][1] == 0,
            "the complete original lift, mean, postcomposition and grid")
    terminal = [api.acb(api.rational(a), api.rational(b)) for a, b in terminal_side[65:]]
    post = [api.acb(api.rational(c), -api.rational(s)) for s, c in zip(K_sines, K_cosines)]
    mean = api.rational(terminal_side[64][0])

    def horner(q, coefficients):
        value = api.acb(0)
        for coefficient in reversed(coefficients):
            value = q*(coefficient+value)
        return value

    grid = []
    for index in range(GRID):
        if index % 2 == 0:
            point = whole_original_grid[index//2]
        else:
            x = api.arb.pi()*index/(2*GRID)
            q = api.acb((4*x).cos(), (4*x).sin())
            a = x+mean+2*horner(q, terminal).real
            qa = api.acb((4*a).cos(), (4*a).sin())
            point = a+horner(qa, post).real
        require(point.is_finite(), "one whole same finite compound-lift value")
        grid.append(point)
    return grid


def new_primitive_samples(api, whole_new_grid, columns):
    require(len(whole_new_grid) == GRID and len(columns) == ROWS
            and all(len(c) == MODES for c in columns), "the whole new8192 grid and same192 by96 trial")
    basis = api.acb_mat(GRID, MODES)
    for j, p in enumerate(whole_new_grid):
        q, value = api.acb((4*p).cos(), (4*p).sin()), api.acb(1)
        for n in range(MODES):
            value = value*q
            basis[j, n] = value
    coefficients = api.acb_mat(MODES, ROWS)
    for j, column in enumerate(columns):
        for n, value in enumerate(column, 1):
            coefficients[n-1, j] = value/api.acb(0, 4*n)
    return basis*coefficients


def new_fft_tables(api):
    bits, permutation = GRID.bit_length()-1, []
    for index in range(GRID):
        source, target = index, 0
        for unused in range(bits):
            target, source = (target << 1) | (source & 1), source >> 1
        permutation.append(target)
    stages, width = [], 2
    while width <= GRID:
        angle = 2*api.arb.pi()/width
        step, power, roots = api.acb(angle.cos(), -angle.sin()), api.acb(1), []
        for unused in range(width//2):
            roots.append(power)
            power = power*step
        stages.append((width, roots))
        width *= 2
    return permutation, stages


def whole_new_transform(api, samples, tables):
    require(len(samples) == GRID and all(v.is_finite() for v in samples), "every new complete sample")
    permutation, stages = tables
    work = [api.acb(samples[j]) for j in permutation]
    for width, roots in stages:
        half = width//2
        for start in range(0, GRID, width):
            for k in range(half):
                left, right = work[start+k], roots[k]*work[start+k+half]
                work[start+k], work[start+k+half] = left+right, left-right
    require(all(v.is_finite() for v in work), "all8192 full directed transform outputs")
    return work


def whole_new_head(api, row, transform, primitive_vector_strip):
    require(1 <= row <= ROWS and len(transform) == GRID, "the original full RHS row and the new entire transform")
    sigma, mass = api.rational(1, 256), up(primitive_vector_strip)
    qN = (-4*GRID*sigma).exp()
    result = []
    for k in range(1, HEAD+1):
        alias = (mass*((-4*(GRID-k)*sigma).exp()+(-4*(GRID+k)*sigma).exp())/(1-qN)).upper()
        centre = transform[k]/GRID
        enclosure = api.acb(centre.real+api.arb(0, alias), centre.imag+api.arb(0, alias))
        residual = api.acb(0, 4*k)*enclosure
        if k == row:
            residual -= api.acb(2*row, -2*row)
        require(residual.is_finite(), "one entire signed residual coefficient including all aliases")
        result.append(residual)
    return result


def power_tail(api, power, cutoff, q):
    """Exact positive geometric moments through degree4, all n>cutoff."""
    require(power in (2, 4) and type(cutoff) is int and cutoff >= 0
            and q.is_finite() and q.lower() > 0 and q.upper() < 1,
            "a full convergent positive geometric series")
    q = q.upper()
    d = 1-q
    moments = [1/d, q/d**2, q*(1+q)/d**3,
               q*(1+4*q+q*q)/d**4,
               q*(1+11*q+11*q*q+q**3)/d**5]
    coefficients = (1, 2, 1) if power == 2 else (1, 4, 6, 4, 1)
    start = cutoff+1
    return (q**start*sum((coefficient*start**(power-r)*moments[r]
                         for r, coefficient in enumerate(coefficients)), api.zero)).upper()


def complete_D1_residual_tail(api, primitive_vector_strip):
    # Residual = derivative(positive primitive)+its real conjugate.
    # Its first derivative has the full weight 2*(4n)^4 = 512*n^4.
    q = (-8*api.rational(1, 256)).exp()
    return (up(primitive_vector_strip)*(512*power_tail(api, 4, HEAD, q)).sqrt()).upper()


def complete_D1_true_map_error(api, saved_Ep, Y0, Y1, Y2):
    """Whole analytic p-phat difference, one real homotopy, all columns."""
    E, N0, N1, N2 = map(up, (saved_Ep, Y0, Y1, Y2))
    sigma = api.rational(1, 256)
    m, M, second = api.rational(9749, 10000), api.rational(10251, 10000), api.rational(1, 6)
    return (E*(2*N0/sigma**2+(second+2*M/sigma)*N1+M*M*N2)/m.sqrt()).upper()


def complete_D1_residual(saved_head, saved_tail, saved_model):
    return sum(map(up, (saved_head, saved_tail, saved_model))).upper()


def original_inverse_L2_error(api, original_IR_H, original_IR_L2):
    """The original fixed positive coefficient in UACT's full products."""
    H, e0 = map(up, (original_IR_H, original_IR_L2))
    S = (api.rational(51, 50)*(e0+api.rational(10, 9)*H)).upper()
    # This is a lower bound on the explicit SAVED-BOUND coefficient S,
    # never a lower bound on the unknown actual inverse error.
    require(H > api.rational(14, 100) and e0 > api.rational(435, 1000)
            and S > api.rational(3, 5), "the same complete positive UACT product coefficient")
    return S


def complete_inverse_D1_error(api, saved_D1_residual, original_S):
    return (api.rational(17, 10)*(up(saved_D1_residual)+api.rational(17, 100)*up(original_S))).upper()


def complete_alpha_D1_tail(api, original_T, original_E3, original_m):
    T, E3 = map(up, (original_T, original_E3))
    require(original_m.is_finite() and original_m.lower() > 0, "the whole original AS positive imaginary lower")
    q = (-4*original_m.lower()*api.rational(1, 128)).exp()
    analytic = 1088*T*power_tail(api, 2, ALPHA_MODES, q)
    source = api.rational(17, 2)*E3/(ALPHA_MODES+1)
    return (analytic+source).upper()


def complete_VQ_D2_error(api, *, saved_inverse_D1, original_H, original_S,
                         original_alpha_trial_W, original_positive_GY_W,
                         whole_original_finite_L2_product,
                         whole_original_inverse_L2_product,
                         saved_alpha_D1_tail):
    E1, H, S, A, W, PY, PE, tail = map(up, (
        saved_inverse_D1, original_H, original_S, original_alpha_trial_W,
        original_positive_GY_W, whole_original_finite_L2_product,
        whole_original_inverse_L2_product, saved_alpha_D1_tail))
    K, M = ALPHA_MODES, MODES
    require(S > api.rational(3, 5), "the original fixed positive product weight, not an error lower")
    original_trial_terms = A*S+4*K*A*H/2
    full_inverse_error_terms = (4*K+api.rational(5, 3)*E1)*PE+S*tail/3
    full_finite_trial_terms = 4*(K+M)*PY+api.rational(2).sqrt()*W*tail
    return (E1+original_trial_terms+full_inverse_error_terms+full_finite_trial_terms).upper()


def new_model_record(api, n, omega, original_mu):
    require(type(n) is int and n >= 2241 and omega.is_finite() and original_mu.is_finite(),
            "only the new continuation of the original whole model head")
    theta = 2*n*omega+api.arb.pi()/4
    nu = -original_mu/2
    denominator = theta.cos()-nu*theta.sin()/(4*n)
    require(denominator.is_finite() and not denominator.contains(0),
            "a complete signed model denominator in the original native Cayley scope")
    reciprocal = 1/denominator
    return denominator, reciprocal, (abs(reciprocal).upper()/(4*n)).upper()


def complete_model_infinite_D2_weight(api):
    # CYA: |gamma_n| <= 2048*n, hence |gamma_n|/(4n)^2 <=128/n.
    return (api.rational(128, MODEL_HEAD+1)).upper()


def complete_weighted_Theta_error(api, saved_head_weight, original_VQ_H1_error,
                                  saved_tail_weight, saved_VQ_D2_error,
                                  original_model_rounding):
    head, H1, tail, H2, rounding = map(up, (
        saved_head_weight, original_VQ_H1_error, saved_tail_weight,
        saved_VQ_D2_error, original_model_rounding))
    return ((head*H1)**2+(tail*H2)**2).sqrt().upper()+rounding
