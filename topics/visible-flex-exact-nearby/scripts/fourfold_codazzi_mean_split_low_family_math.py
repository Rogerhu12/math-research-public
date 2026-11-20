"""R140 complete nonmean192/mean1 comparison for Gf delta_AL S_inverse.

Pure injected arithmetic, with no entry point, file access, numerical import,
old producer call, parameter search, or scientific execution at module import.
The owner must first admit the full W2C context and unchanged parameter family.
All four angular blocks, all 193 observation coordinates, the true nonlocal
primitive, the independent mean, and the same actual eta remain present.
The angle is the original WVC moving phi, not a substitution of physical theta.
The difference is P_L[G(Q_delta;eta_delta)-G(Q_c;eta_delta)]P_L, using exactly
assembly.prepare_complete_kernel_context's explicit full-family speed slot.
It is NOT the difference from the natural frozen-eta_c generator at Q_c;
that other difference has the additional -gamma*e_mean*J_K*d_phi term.

Source-cell RMS values below are NOT pointwise multiplication bounds.  They
are used only after the complete (r,s) kernel bound and source-cell Cauchy--
Schwarz of R140 (M20)--(M23), followed by the full output integral and atoms.
"""
from fractions import Fraction


BLOCK_NAMES = ("NN", "N0", "0N", "00")
RECORD_NAMES = (
    "complete_mean_split_low_family_row_ratio_upper",
    "complete_mean_split_low_family_column_ratio_upper",
    "complete_mean_split_low_family_norm_upper",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def _q(api, value):
    value = Fraction(value)
    return api.rational(value.numerator, value.denominator)


def _up(api, value):
    return api.upper(value)


def _sqrt_up(api, value):
    # Every caller supplies a sum/product of nonnegative upper POINTS.
    return api.upper(api.sqrt(value))


def _old_upper(collar, api, record, label):
    return collar._old_upper(api, record, "R140/" + label, process=True)


def _sector_formula(api, *, beta, gamma, curvature, U, V, U1, V1,
                    V_nonmean, mean, E0, E1, error_mean,
                    local_a, local_e, local_b, drift, mean_own):
    """R140 M10--M14; complete raw L2 four-block angular bounds."""
    values = (beta, gamma, curvature, U, V, U1, V1, V_nonmean, mean,
              E0, E1, error_mean, local_a, local_e, local_b, drift, mean_own)
    require(all(api.lower(value) >= 0 for value in values),
            "complete nonnegative physical row bounds")
    kappa = max(api.one, curvature)
    En = min(E0, _up(api, E1/4))
    Em = min(E0, error_mean)
    C0 = _sqrt_up(api, U*U+curvature*curvature*V*V)
    C1 = _sqrt_up(api, U1*U1+V1*V1)
    Cn = _sqrt_up(api, U*U+curvature*curvature*V_nonmean*V_nonmean)
    local_row = max(_up(api, local_a+curvature*local_b),
                    _up(api, local_b+local_e))
    local_column = max(_up(api, local_a+local_b),
                       _up(api, curvature*local_b+local_e))
    local = _sqrt_up(api, local_row*local_column)
    primitive = _up(api, beta/2*(
        E1*(C0+kappa*E0)+C1*kappa*E0))
    NN = _up(api, 384*drift+local+primitive)
    # A constant even input has no angular derivative.  I on its inner v
    # coefficient removes precisely that coefficient's mean, before the
    # complete outer multiplier.  The gamma mean-input column is retained.
    local_mean_column = _sqrt_up(api,
        curvature*curvature*local_b*local_b+local_e*local_e)
    primitive_mean_column = _up(api, beta*curvature/2*(
        E1*(V_nonmean+En)+C1*En))
    N0 = _up(api, local_mean_column+primitive_mean_column+gamma*kappa*E1)
    # Full physical mean row, not the mean of an independently bounded
    # local/primitive sum.  Both nonmean input components remain present.
    zero_N = _up(api, 2*beta*((mean+Em)*kappa*En+Em*Cn))
    return {"NN": NN, "N0": N0, "0N": zero_N, "00": _up(api, mean_own)}


def complete_body_sector_bounds(row, api, collar, *, same_actual_eta_retained):
    """Same-eta hybrid Delta_AL; consume rows without calling their producer."""
    require(same_actual_eta_retained is True,
            "actual and centre retain the identical full-family eta function")
    require(row["Z_offset_is_piecewise_radial_constant_angular_derivative_not_radial"] is True
            and row["arbitrary_direction_jump_still_a_separate_affine_source"] is True,
            "original angular derivative and independent jump qualifications")
    base = row["original_complete_repaired_bounds"]
    fees = row["complete_delta_fees"]
    original = row["original_intrinsic_enclosure"]
    U, V, U1, V1, Vn = (_old_upper(collar, api, base[name], "body/" + name)
        for name in ("U_A0", "V_A0", "U_phi_A0", "V_phi_A0", "V_nonmean_A0"))
    E0 = _old_upper(collar, api, row["full_delta_A0"], "body/full_delta_A0")
    E1 = _old_upper(collar, api, row["full_delta_angular_A0"], "body/full_delta_angular_A0")
    Em = _old_upper(collar, api, row["independent_mean_variation_bound"], "body/mean_variation")
    a, e, b, d, c00 = (_old_upper(collar, api, fees[name], "body/complete_delta_fees/" + name)
        for name in ("local_a", "local_e", "local_b", "drift", "mean_own_rate"))
    beta, gamma, curvature = (api.magnitude(api.old_interval(original[name]))
        for name in ("beta", "gamma", "K"))
    mean = api.magnitude(api.old_interval(base["mean_v"]))
    return _sector_formula(api, beta=beta, gamma=gamma, curvature=curvature,
        U=U, V=V, U1=U1, V1=V1, V_nonmean=Vn, mean=mean,
        E0=E0, E1=E1, error_mean=Em, local_a=a, local_e=e, local_b=b,
        drift=d, mean_own=c00)


def complete_collar_sector_bounds(packet, api, collar, sqrt_two):
    """The full genuine-root packet; its signed K box need not be positive."""
    require(packet["kind"] == collar.CENTRE_KIND
            and packet["family_delta"]["kind"] == collar.DELTA_KIND
            and packet["family_delta"]["actual_eta_is_identical_in_both_operators"] is True,
            "entire true collar centre and same-eta family increment")
    angular = packet["angular_upper"]
    old_norms = packet["norm_upper"]
    U, U1 = angular["full_family_U_angular_norms"][:2]
    V, V1 = angular["full_family_V_angular_norms"][:2]
    zu, zu1 = angular["direction_angular_norms_u"][:2]
    zv, zv1 = angular["direction_angular_norms_v"][:2]
    delta = _q(api, packet["exact_direction_radius"])
    beta, curvature, gamma = (old_norms[name] for name in
        ("beta_abs_upper", "K_abs_upper", "gamma_abs_upper"))
    eu, ev = _up(api, delta*zu), _up(api, delta*zv)
    E0, E1 = _up(api, eu+ev), _up(api, delta*(zu1+zv1))
    error = packet["family_delta"]
    Em, mean = api.magnitude(error["em"]), api.magnitude(packet["mc"])
    Vn = min(V, _up(api, sum((api.magnitude(value)
        for j, value in packet["v"].items() if j != 0), api.zero)))
    # Same complete three-word coefficient increment, with all quadratic
    # full96 terms.  No old collar coefficient/norm producer is called.
    du2, dv2 = 2*U*eu+eu*eu, 2*V*ev+ev*ev
    duv = U*ev+V*eu+eu*ev
    a = _up(api, beta*(3*du2+curvature*dv2))
    e = _up(api, beta*(du2+3*curvature*dv2))
    b = _up(api, 2*beta*duv)
    d = _up(api, beta*(du2+curvature*dv2)/4)
    c00 = api.magnitude(collar.family_signed_increment_entry(
        error, (1, 0), (1, 0), sqrt_two, api.zero))
    return _sector_formula(api, beta=beta, gamma=gamma, curvature=curvature,
        U=U, V=V, U1=U1, V1=V1, V_nonmean=Vn, mean=mean,
        E0=E0, E1=E1, error_mean=Em, local_a=a, local_e=e, local_b=b,
        drift=d, mean_own=c00)


def complete_source_sector_rms(api, ctx, admitted, collar, progress):
    """M20 after the whole kernel bound, never a pointwise multiplier claim.

    Every body overlap is exact rational.  The uncertain-root panel uses its
    full uniform fee, so no unknown true collar length is used as a divisor.
    Only the current original row is cached across adjacent panel boundaries.
    """
    domain, rows = ctx.domain, admitted["rows"]
    require(admitted["collar_inputs_verified"] is True and len(rows) == 4650
            and ctx.parent_definition_count == 153
            and ctx.original_intersection_count == 4801
            and len(domain.cells) <= 155,
            "same complete original admission and reference cover")
    root_bounds = complete_collar_sector_bounds(ctx.centre_packets[0], api, collar, ctx.sqrt_two)
    coefficients = []
    cursor = 0
    seen = set()
    intersections = 0
    cached_index, cached_bounds = None, None
    for k, cell in enumerate(domain.cells):
        if ctx.parent_indices[k] == 0:
            require(k == 0 and cell["left"] is None, "one whole genuine-root collar")
            rms = dict(root_bounds)
        else:
            left, right = Fraction(cell["left"]), Fraction(cell["right"])
            require(left < right, "strict exact body comparison panel")
            while cursor < len(rows) and Fraction(rows[cursor]["interval"][1]) <= left:
                cursor += 1
            index, covered, total_weight = cursor, left, Fraction(0)
            squares = {name: api.zero for name in BLOCK_NAMES}
            maxima = {name: api.zero for name in BLOCK_NAMES}
            while index < len(rows) and Fraction(rows[index]["interval"][0]) < right:
                row = rows[index]
                lo = max(left, Fraction(row["interval"][0]))
                hi = min(right, Fraction(row["interval"][1]))
                require(lo == covered and lo < hi, "complete ordered source-row intersection")
                if cached_index != index:
                    cached_bounds = complete_body_sector_bounds(row, api, collar,
                        same_actual_eta_retained=True)
                    cached_index = index
                weight = (hi-lo)/(right-left)
                total_weight += weight
                weight_ball = _q(api, weight)
                for name in BLOCK_NAMES:
                    value = cached_bounds[name]
                    squares[name] += weight_ball*value*value
                    maxima[name] = max(maxima[name], value)
                seen.add(index)
                intersections += 1
                covered = hi
                if covered == right:
                    break
                index += 1
            require(covered == right and total_weight == 1,
                    "all source pieces retained with exact unit total weight")
            cursor = index
            # Both entries are complete bounds on the same RMS coefficient;
            # min also prevents harmless outward rounding from exceeding max.
            rms = {name: min(maxima[name], _sqrt_up(api, squares[name])) for name in BLOCK_NAMES}
        q = ctx.reference_qs[k]
        require(api.lower(q) > 0, "same positive actual reference S factor")
        sigma0 = _up(api, api.one/q)
        sigmaN = max(api.one, sigma0)
        coefficients.append({name: _up(api, rms[name]*(sigma0 if name.endswith("0") else sigmaN))
                             for name in BLOCK_NAMES})
        progress("mean_split_source_panel", {"panels_complete": k+1,
            "comparison_cells": len(domain.cells), "original_rows_covered": len(seen),
            "closed_source_intersections": intersections,
            "source_RMS_is_after_complete_kernel_bound": True})
    require(seen == set(range(4650)) and len(coefficients) == len(domain.cells),
            "entire original body and every source component retained")
    return coefficients, {"original_rows": len(seen), "closed_source_intersections": intersections}


class _TwoSectorReference:
    """Same full WVC receiver, with mean orthogonally separated, not removed."""
    def __init__(self, api, ctx):
        self.api, self.ctx, self.domain = api, ctx, ctx.domain
        self.profiles = ctx.reference_profiles
        self.n = len(self.domain.cells)
        self.modes = tuple(range(1, 97))
        boxes = [self.domain.whole_cell_box(i) for i in range(self.n)]
        self.boxes = boxes
        self.values = {}
        for j in self.modes:
            self.values[j] = []
            for box in boxes:
                value = self.profiles.at(j, box)
                # All four exact profiles are nonnegative.  The repaired
                # reference supplies nonnegative outward interval hulls.
                self.values[j].append({name: _up(api, value[name]) for name in ("p", "H", "K", "g")})
        self.q = [_up(api, q) for q in ctx.reference_qs]
        self.nonmean_tiles = {}
        self.nonmean_atoms = {}

    def nonmean_tile(self, i, k):
        key = (i, k)
        if key in self.nonmean_tiles:
            return self.nonmean_tiles[key]
        api = self.api
        answers = []
        lo, hi = min(i, k), max(i, k)
        q = self.q[i]
        for j in self.modes:
            vr, vs = self.values[j][i], self.values[j][k]
            decay = api.one if i == k else _up(api, self.profiles.mode[j]["products"].between(lo+1, hi))
            if i >= k:
                value = (vr["p"]*vr["p"]+q*q)*(vs["H"]*vs["H"]+vs["K"]*vs["K"])
                answers.append(_up(api, decay*_sqrt_up(api, value)))
            if i <= k:
                value = (vr["K"]*vr["K"]+q*q*vr["H"]*vr["H"])*(api.one+vs["p"]*vs["p"])
                answers.append(_up(api, decay*_sqrt_up(api, value)))
        result = max(answers)
        self.nonmean_tiles[key] = result
        return result

    def nonmean_atom(self, k):
        if k in self.nonmean_atoms:
            return self.nonmean_atoms[k]
        api = self.api
        answers = []
        for j in self.modes:
            v = self.values[j][k]
            root = v["g"]
            # Only an upper number is needed here.  Multiply directed upper
            # POINTS, so a positive factor times a zero-endpoint ball cannot
            # acquire an irrelevant negative represented endpoint.
            outer = _up(api, _up(api, self.ctx.reference_thetas[j])
                *_up(api, self.profiles.to_right(j, self.boxes[k])))
            p, H, K = (v[name] for name in ("p", "H", "K"))
            rows = max(_up(api, root*(api.one+p)), _up(api, outer*(H+K)))
            columns = max(_up(api, root+outer*H), _up(api, root*p+outer*K))
            answers.append(_sqrt_up(api, rows*columns))
        result = max(answers)
        self.nonmean_atoms[k] = result
        return result

    def mean_tile(self, i, k):
        # Exact mean kernel is -q(r) 1_(r<=s), including the same-cell triangle.
        return self.q[i] if i <= k else self.api.zero

    def mean_atom(self, k):
        return self.api.one


def complete_mean_split_low_family(api, ctx, admitted, collar, emit, progress):
    """Compute precisely one complete new three-record comparison (R140 M23).

    emit must durably save each whole upper record and return its directed
    saved upper endpoint.  This function never reevaluates the old L triple.
    No conditional inverse or parent-five-graph completion is returned.
    ctx must be the admitted assembly.prepare_complete_kernel_context result,
    whose body packet eta is complete_delta_bounds.radial_speed, distinct
    from the repaired-centre mean, and whose collar has the same qualification.
    """
    coefficients, cover = complete_source_sector_rms(api, ctx, admitted, collar, progress)
    receiver = _TwoSectorReference(api, ctx)
    n = len(ctx.domain.cells)
    lengths = [_up(api, ctx.domain.full_length(i)) for i in range(n)]
    rowsN, rows0 = [api.zero for _ in range(n)], [api.zero for _ in range(n)]
    reverseN, reverse0 = [api.zero for _ in range(n)], [api.zero for _ in range(n)]
    for i in range(n):
        for k in range(n):
            b = coefficients[k]
            gN, g0 = receiver.nonmean_tile(i, k), receiver.mean_tile(i, k)
            rowsN[i] += lengths[k]*gN*(b["NN"]+b["N0"])
            rows0[i] += lengths[k]*g0*(b["0N"]+b["00"])
            reverseN[k] += lengths[i]*gN
            reverse0[k] += lengths[i]*g0
        progress("mean_split_complete_kernel_row", {"body_output_panels_complete": i+1,
            "comparison_cells": n, "nonmean_dimension": 192, "independent_mean_dimension": 1,
            "all_source_panels_in_this_row": n})
    atomN, atom0 = api.zero, api.zero
    for k in range(n):
        b = coefficients[k]
        tN, t0 = receiver.nonmean_atom(k), receiver.mean_atom(k)
        atomN += lengths[k]*tN*(b["NN"]+b["N0"])
        atom0 += lengths[k]*t0*(b["0N"]+b["00"])
        reverseN[k] += tN
        reverse0[k] += t0
    row = emit(RECORD_NAMES[0], max(_up(api, value) for value in rowsN+rows0+[atomN, atom0]))
    columns = []
    for k in range(n):
        b = coefficients[k]
        columns.append(_up(api, b["NN"]*reverseN[k]+b["0N"]*reverse0[k]))
        columns.append(_up(api, b["N0"]*reverseN[k]+b["00"]*reverse0[k]))
    column = emit(RECORD_NAMES[1], max(columns))
    norm = emit(RECORD_NAMES[2], _sqrt_up(api, row*column))
    return {"row": row, "column": column, "norm": norm, "scope": {
        "whole_operator": "Gf delta_AL S_inverse",
        "nonmean_dimension": 192, "independent_physical_mean_dimension": 1,
        "nonmean_observation_coordinates": 192, "mean_observation_coordinates": 1,
        "comparison_cells": n, "source_cover": cover,
        "all_four_angular_blocks_retained": True,
        "all_three_ordered_primitive_difference_terms_retained": True,
        "identical_actual_eta_in_actual_and_centre": True,
        "family_difference": "P_L[G(Q_delta;eta_delta)-G(Q_c;eta_delta)]P_L",
        "natural_frozen_eta_c_generator_difference_claimed": False,
        "angular_coordinate": "original_WVC_phi",
        "physical_theta_substitution_claimed": False,
        "same_complete_real_delta_family": True,
        "source_RMS_only_after_whole_kernel_weight": True,
        "pointwise_multiplication_RMS_claimed": False,
        "old_low_family_norm_triple_reevaluated": False,
        "complete_parent_graphs_claimed": False, "finite_inverse_claimed": False}}
