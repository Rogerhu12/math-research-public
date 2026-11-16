"""W2C true-collar signed packets and complete delta-family differences.

No entry point, file access, native decoding, old producer import, or old norm
evaluation. The owner first admits the complete original inputs. This module
then supplies PRIVATE finite algebra for the new W2C candidate in its one public
scientific child. Nothing in this module has been evaluated while preparing it.

The repaired centre is the original degree-32 cubic plus all 65 signed physical
offsets, with the signed intrinsic germ boxes. The 193 saved response upper
bounds enclose the family ERROR only. The same ACTUAL eta=-gamma*m_delta is
retained in both A and A_c, using the original saved optical-speed interval.
It is never replaced by -gamma*the centre mean.

API, injected by the new owner:
  zero, one; rational(numerator, denominator=1);
  lower(x), upper(x), magnitude(x); interval(lo, hi); old_interval(record).
lower accepts every finite signed interval; upper need only accept nonnegative
bounds. interval encloses two finite directed endpoint scalars. old_interval
uses the complete original lower.lower/upper.upper hull, not a display centre.
No diagnostic float in an original record participates in numerical algebra.

The returned centre has the original full_packet keys. family_delta is a
DISTINCT increment object with all three ordered primitive words. Complete
signed entries precede any absolute value. True adjoints transpose the entire
physical normalized matrix, including its mean row and primitive projection;
the owner applies the actual input/output Riesz and S factors afterwards.
"""

from fractions import Fraction
from decimal import Decimal


COLLAR_PIECE = 2549
ROOT_INTERVAL = (
    "1191984371497/5000000000000",
    "2383968743003/10000000000000",
)
BODY_CUT = "1192029371497/5000000000000"
CANDIDATE_SHA256 = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
BACKGROUND_DEFINITION_SHA256 = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION_DEFINITION_SHA256 = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
OBJECT_SHA256 = "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
GERM_SOURCE_SHA256 = "a3ad50b828c69d3e6f1e9254c1f266535171741ee2cd675d1569ef8f0fac0491"
ROOT_BUDGET_SOURCE_SHA256 = "4a3ee217b21cabda6ae3dea052f27ff82f03b4218294145dc2f812891688e03e"
COLLAR_MATH_SOURCE_SHA256 = "8d3ab188d47a1aa81cbc304350655f2172333b435fdf0e09482b245f957917bf"
GERM_NATIVE_SHA256 = "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
ROOT_BUDGET_NATIVE_SHA256 = "10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"
INTRINSIC_NAMES = (
    "a", "a1", "a2", "a3", "E", "E1", "E2", "rotational_gap",
    "K", "K1", "gamma", "beta", "s",
)
NATIVE_RECORD_FIELDS = {
    "ball", "lower", "upper", "mid_float", "radius_upper_float",
}
PROCESS_RECORD_FIELDS = {"ball", "lower", "upper"}
CENTRE_KIND = "W2C_true_repaired_degree32_collar_packet_v1"
DELTA_KIND = "W2C_complete_family_increment_not_a_background_packet_v1"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def _q(api, value):
    value = Fraction(value)
    return api.rational(value.numerator, value.denominator)


def _signed_upper(api, value):
    # The old NumericalAPI.upper intentionally rejects negative intervals.
    return -api.lower(-value)


def _hull(api, lo, hi):
    require(lo <= hi, "ordered finite interval endpoints")
    return api.interval(lo, hi)


def _intersect(api, first, second, label):
    lo = max(api.lower(first), api.lower(second))
    hi = min(_signed_upper(api, first), _signed_upper(api, second))
    require(lo <= hi, "same-object enclosures intersect: " + label)
    return _hull(api, lo, hi)


def _symmetric(api, bound):
    bound = api.upper(bound)
    require(bound >= 0, "nonnegative complete error upper")
    return _hull(api, -bound, bound)


def _record(record, label, process=False):
    keys = PROCESS_RECORD_FIELDS if process else NATIVE_RECORD_FIELDS
    require(isinstance(record, dict) and set(record) == keys,
            "complete original record schema: " + label)
    for name in ("ball", "lower", "upper"):
        value = record[name]
        require(isinstance(value, str) and value and value.isascii()
                and "nan" not in value.lower() and "inf" not in value.lower(),
                "finite original endpoint spelling: " + label + "/" + name)
    if not process:
        diagnostics = (record["mid_float"], record["radius_upper_float"])
        require(all(type(value) in (int, float)
                    or (isinstance(value, Decimal) and value.is_finite())
                    for value in diagnostics)
                and record["radius_upper_float"] >= 0,
                "original diagnostic fields remain diagnostic: " + label)
    return record


def _old_upper(api, record, label, process=False):
    value = api.old_interval(_record(record, label, process=process))
    result = _signed_upper(api, value)
    require(result >= 0, "nonnegative saved upper: " + label)
    return result


def _old_positive_lower(api, record, label, process=False):
    value = api.old_interval(_record(record, label, process=process))
    result = api.lower(value)
    require(result > 0, "positive saved lower: " + label)
    return result


def _poly(degree, zero):
    return {j: zero for j in range(-degree, degree + 1)}


def _add(first, second, zero):
    return {j: first.get(j, zero) + second.get(j, zero)
            for j in sorted(set(first) | set(second))}


def _scale(poly, scalar):
    return {j: scalar * value for j, value in poly.items()}


def _convolution(first, second, zero):
    require(bool(first) and bool(second), "complete nonempty finite Laurent supports")
    degree = max(map(abs, first)) + max(map(abs, second))
    out = _poly(degree, zero)
    for j, first_value in first.items():
        for k, second_value in second.items():
            out[j + k] += first_value * second_value
    return out


def _primitive_factors(ui, vr, beta, curvature):
    # u=i*ui. u_phi is even real; v_phi has imaginary odd coefficients.
    left = [
        {j: -4 * j * beta * value for j, value in ui.items()},
        {j: 4 * j * beta * value for j, value in vr.items()},
    ]
    right = [dict(ui), _scale(vr, curvature)]
    return left, right


def _complete_centre_packet(ui, vr, beta, curvature, gamma, actual_eta, zero):
    """Same complete raw generator, with ACTUAL eta supplied explicitly."""
    require(set(ui) == set(vr) == set(range(-32, 33)),
            "all original centre Fourier coordinates")
    u2 = _scale(_convolution(ui, ui, zero), -1)
    v2 = _convolution(vr, vr, zero)
    uv = _convolution(ui, vr, zero)
    energy = _add(u2, _scale(v2, curvature), zero)
    la = _scale(_add(_scale(u2, 3), _scale(v2, curvature), zero), -beta)
    le = _scale(_add(u2, _scale(v2, 3 * curvature), zero), -beta)
    la[0] -= beta
    le[0] += beta
    ell = _scale(uv, -2 * beta)
    drift = {j: beta * value / (4 * j) if j else zero
             for j, value in energy.items()}
    left, right = _primitive_factors(ui, vr, beta, curvature)
    return {
        "kind": CENTRE_KIND,
        "u": dict(ui), "v": dict(vr), "beta": beta, "K": curvature,
        "gamma": gamma, "eta": actual_eta, "actual_eta": actual_eta,
        "mc": vr[0], "S_mean": energy[0], "d": drift,
        "la": la, "le": le, "ell": ell, "Kell": _scale(ell, curvature),
        "a": left, "b": right,
    }


def _complete_family_increment(centre, error_u, error_v, zero):
    """A-A_c by exact ordered algebra; no subtraction of independent uppers."""
    ui, vr = centre["u"], centre["v"]
    beta, curvature = centre["beta"], centre["K"]
    require(set(error_u) == set(error_v) == set(range(-96, 97)),
            "complete193 family error coordinates")
    du2 = _scale(_add(_add(_convolution(ui, error_u, zero),
                          _convolution(error_u, ui, zero), zero),
                     _convolution(error_u, error_u, zero), zero), -1)
    dv2 = _add(_add(_convolution(vr, error_v, zero),
                   _convolution(error_v, vr, zero), zero),
              _convolution(error_v, error_v, zero), zero)
    duv = _add(_add(_convolution(ui, error_v, zero),
                   _convolution(error_u, vr, zero), zero),
              _convolution(error_u, error_v, zero), zero)
    denergy = _add(du2, _scale(dv2, curvature), zero)
    la = _scale(_add(_scale(du2, 3), _scale(dv2, curvature), zero), -beta)
    le = _scale(_add(du2, _scale(dv2, 3 * curvature), zero), -beta)
    ell = _scale(duv, -2 * beta)
    da, db = _primitive_factors(error_u, error_v, beta, curvature)
    # -2[(da)I(b_c) + (a_c)I(db) + (da)I(db)], with every inner mean projected.
    words = [(da, centre["b"]), (centre["a"], db), (da, db)]
    return {
        "kind": DELTA_KIND,
        "u": dict(error_u), "v": dict(error_v), "beta": beta,
        "K": curvature, "gamma": centre["gamma"], "eta": zero,
        "actual_eta_is_identical_in_both_operators": True,
        "mc": centre["mc"], "em": error_v[0],
        "centre_u": centre["u"], "centre_v": centre["v"],
        "S_mean": denergy[0],
        "d": {j: beta * value / (4 * j) if j else zero
              for j, value in denergy.items()},
        "la": la, "le": le, "ell": ell, "Kell": _scale(ell, curvature),
        "primitive_words": words,
        "local_and_primitive_total_band": 192,
        "not_a_replacement_background": True,
    }


def complete_true_collar_packet(admitted, api, *, radial_interval=None):
    """Construct a signed private enclosure on one declared collar subinterval.

    Default enclosure [root_lower,c_body] covers the variable TRUE interval
    [r_star,c_body]; root_lower is not substituted for the physical root.
    Optional exact rational subintervals only restrict this enclosing domain.
    No radial derivative estimate is used from the native inner half disk.
    All native and cubic byte checks belong to the preceding pure owner reader.
    """
    require(admitted.get("collar_inputs_verified") is True,
            "owner has verified all original collar bytes and full domains")
    germ, rb, repair = (admitted[name] for name in ("germ", "rb", "repair"))
    cubic, metadata, literals, process = (admitted[name] for name in
        ("cubic", "candidate_metadata", "literals", "collar_process"))
    require(germ["kind"] == "actual_moving_candidate_complete_physical_angle_complex_turning_germ"
            and germ["complete"] is True and germ["proved"] is True
            and germ["failure"] is None and germ["source_sha256"] == GERM_SOURCE_SHA256
            and germ["candidate_sha256"] == CANDIDATE_SHA256
            and germ["object_sha256"] == OBJECT_SHA256,
            "complete identical signed intrinsic germ")
    require(rb["kind"] == "complete_moving_current_root_scalarization_operator_budget"
            and rb["complete"] is True and rb["proved"] is True and rb["failure"] is None
            and rb["source_sha256"] == ROOT_BUDGET_SOURCE_SHA256
            and str(rb["public_run_id"]) == "43594466882"
            and rb["candidate_sha256"] == CANDIDATE_SHA256
            and rb["background_definition_sha256"] == BACKGROUND_DEFINITION_SHA256
            and rb["explicit_direction_definition_sha256"] == DIRECTION_DEFINITION_SHA256,
            "complete original family budget and definitions")
    require(all(gate["passed"] is True for gate in germ["gates"])
            and all(gate["passed"] is True for gate in rb["gates"])
            and rb["actual_intrinsic_parameter"] == "eta_0"
            and rb["actual_R31_selected_parameter_included"] is True
            and rb["actual_independent_even_mean_preserved"] is True
            and rb["whole_original_intrinsic_parameter_family_claimed"] is False
            and rb["no_actual_PDE_background_transfer_inferred"] is True,
            "same selected full family and all original domain qualifications")
    require(repair["kind"] == "actual_final_exact_continuous_value_repair_v1"
            and repair["complete"] is True
            and repair["candidate_sha256"] == CANDIDATE_SHA256
            and repair["derived_definition_sha256"] == BACKGROUND_DEFINITION_SHA256
            and all(gate["passed"] is True for gate in repair["gates"]),
            "full exact physical repair object, not just a norm projection")
    require(metadata == germ["exact_candidate_metadata"]
            and metadata["modes"] == 32 and metadata["physical_frequency_factor"] == 4
            and metadata["object_sha256"] == OBJECT_SHA256
            and len(cubic.nodes) == 6145,
            "same whole original degree32 cubic and moving Fourier convention")
    alpha = Fraction(metadata["exact_float_amplitude"])
    require(alpha == Fraction(germ["exact_amplitude"])
            and alpha == Fraction(repair["definition"]["exact_alpha"])
            and repair["definition"]["physical_frequency_factor"] == 4
            and repair["definition"]["modes"] == 32
            and repair["definition"]["offsets_independent_of_eta_and_nu"] is True,
            "exact original amplitude and physical offset units")

    roots = tuple(Fraction(value) for value in ROOT_INTERVAL)
    cut = Fraction(BODY_CUT)
    require(tuple(map(Fraction, germ["root_interval"])) == roots
            and tuple(map(Fraction, rb["exact_root_interval"])) == roots
            and tuple(map(Fraction, literals["rstar_interval"])) == roots
            and Fraction(literals["c_body"]) == cut
            and germ["actual_candidate_piece"] == COLLAR_PIECE
            and rb["exact_candidate_and_response_piece"] == COLLAR_PIECE
            and roots[0] < roots[1] < cut <= roots[0] + Fraction(9, 1000000),
            "true variable root and exact original collar cut")
    cell = tuple(map(Fraction, germ["exact_candidate_piece_interval"]))
    rectangle = tuple(map(Fraction, germ["complex_radial_rectangle"]["real_interval"]))
    radius = Fraction(1, 100000)
    delta = Fraction(1, 100000000)
    require(tuple(map(Fraction, rb["exact_piece_interval"])) == cell
            and (cubic.nodes[COLLAR_PIECE], cubic.nodes[COLLAR_PIECE + 1]) == cell
            and rectangle == (roots[0] - radius, roots[1] + radius)
            and rb["exact_radial_rectangle"] == germ["complex_radial_rectangle"]
            and Fraction(germ["complex_radial_radius"]) == radius
            and Fraction(germ["complex_radial_rectangle"]["imaginary_half_width"]) == radius
            and Fraction(rb["exact_outer_radial_radius"]) == radius
            and Fraction(rb["exact_complex_parameter_radius"]) == delta
            and Fraction(germ["moving_phi_strip"]) == Fraction(1, 1024)
            and Fraction(rb["exact_moving_Wiener_strip"]) == Fraction(1, 1024)
            and cell[0] < rectangle[0] < roots[0] < cut < rectangle[1] < cell[1]
            and germ["compact_bump_identically_zero_on_entire_actual_germ"] is True
            and germ["domain_contains_disks_about_every_true_parameter_root"] is True
            and germ["all_finite_candidate_modes_retained"] is True,
            "complete original value rectangle, one true cubic piece and fixed strip")
    offset_strings = rb["exact_background_root_offsets"]
    require(isinstance(offset_strings, list) and len(offset_strings) == 65
            and all(isinstance(value, str) for value in offset_strings),
            "all65 exact signed physical offsets")
    offsets = tuple(map(Fraction, offset_strings))
    repair_piece = repair["special_piece_offsets"][str(COLLAR_PIECE)]
    require(tuple(map(Fraction, repair_piece["physical_offset"])) == offsets
            and tuple(map(Fraction, repair_piece["interval"])) == cell,
            "same exact physical offsets on piece2549, no second amplitude factor")
    if radial_interval is None:
        left, right = roots[0], cut
    else:
        require(isinstance(radial_interval, (tuple, list)) and len(radial_interval) == 2,
                "one exact collar subinterval")
        left, right = tuple(map(Fraction, radial_interval))
        require(roots[0] <= left <= right <= cut, "subinterval stays in the admitted collar enclosure")

    intrinsic_raw = germ["complex_intrinsic_coefficients"]
    require(set(intrinsic_raw) == set(INTRINSIC_NAMES), "all13 original intrinsic objects")
    intrinsic = {}
    for name in INTRINSIC_NAMES:
        original = intrinsic_raw[name]
        require(isinstance(original, dict) and set(original) == {"real", "imag", "modulus_upper"},
                "complete original complex intrinsic record: " + name)
        for part in ("real", "imag", "modulus_upper"):
            _record(original[part], "complex_intrinsic_coefficients/" + name + "/" + part)
        intrinsic[name] = api.old_interval(original["real"])
    require(api.lower(intrinsic["gamma"]) > 0
            and _signed_upper(api, intrinsic["s"]) < 0,
            "actual real gamma positive and original intrinsic mean negative")
    # K is the full signed real box. No positive-body floor is moved to the root.
    values = cubic.polynomial_values(
        COLLAR_PIECE, left, right, lambda value: _q(api, value),
        lambda low, high: _hull(api, _q(api, low), _q(api, high)))
    require(len(values) == 65, "all original cubic components evaluated together")
    physical = [_q(api, alpha) * value + _q(api, offset)
                for value, offset in zip(values, offsets)]
    old_mean = germ["moving_mean_v"]
    require(isinstance(old_mean, dict) and set(old_mean) == {"real", "imag", "modulus_upper"},
            "complete original signed moving mean")
    for part in ("real", "imag", "modulus_upper"):
        _record(old_mean[part], "moving_mean_v/" + part)
    centre_mean = _intersect(api, intrinsic["s"] + physical[32],
        api.old_interval(old_mean["real"]) + _q(api, offsets[32]), "same repaired centre mean")
    require(_signed_upper(api, centre_mean) < 0, "repaired centre mean has the original negative sign")
    ui, vr = _poly(32, api.zero), _poly(32, api.zero)
    vr[0] = centre_mean
    for j in range(1, 33):
        ui[j], ui[-j] = -physical[j - 1] / 2, physical[j - 1] / 2
        vr[j] = vr[-j] = physical[32 + j] / 2

    response_raw = rb["response_repaired_complete_coefficient_upper"]
    require(isinstance(response_raw, list) and len(response_raw) == 193,
            "all193 already-complete response and direction-repair upper records")
    response = [_old_upper(api, record, "response_repaired_complete_coefficient_upper/" + str(i))
                for i, record in enumerate(response_raw)]
    error = [_symmetric(api, _q(api, delta) * bound) for bound in response]
    eu, ev = _poly(96, api.zero), _poly(96, api.zero)
    ev[0] = error[96]
    for j in range(1, 97):
        eu[j], eu[-j] = -error[j - 1] / 2, error[j - 1] / 2
        ev[j] = ev[-j] = error[96 + j] / 2
    mean_min = _old_positive_lower(api, rb["full_complex_mean_abs_lower"],
                                  "full_complex_mean_abs_lower")
    mean_max = _old_upper(api, rb["full_complex_mean_abs_upper"], "full_complex_mean_abs_upper")
    family_mean = _intersect(api, centre_mean + ev[0],
                            _hull(api, -mean_max, -mean_min), "same complete family mean")

    require(process["kind"] == "actual_public_full_real_delta96_root_collar_execution"
            and process["complete"] is True and process["mathematical_complete"] is True
            and process["actual_returncode"] == 0 and str(process["run_id"]) == "43606747196"
            and str(process["run_attempt"]) == "1"
            and process["mathematical_source_sha256"] == COLLAR_MATH_SOURCE_SHA256
            and len(process["mathematical_gates"]) == 19
            and all(gate["passed"] is True for gate in process["mathematical_gates"]),
            "same completed original full-family optical-speed certificate")
    original_bounds = process["fresh_coefficient_bounds"]
    eta_low_record = original_bounds["optical_speed_lower"]
    eta_high_record = original_bounds["optical_speed_upper"]
    eta_low = _old_positive_lower(api, eta_low_record, "optical_speed_lower", process=True)
    eta_high = _old_upper(api, eta_high_record, "optical_speed_upper", process=True)
    actual_eta = _hull(api, eta_low, eta_high)
    # Do not reevaluate either old gl*mgap or old gamma*mmax target.
    packet = _complete_centre_packet(ui, vr, intrinsic["beta"], intrinsic["K"],
                                     intrinsic["gamma"], actual_eta, api.zero)
    family_delta = _complete_family_increment(packet, eu, ev, api.zero)
    angular_raw, angular = {}, {}
    for name in ("direction_angular_norms_u", "direction_angular_norms_v",
                 "full_family_U_angular_norms", "full_family_V_angular_norms"):
        records = rb[name]
        require(isinstance(records, list) and len(records) == 5,
                "complete original angular array: " + name)
        angular_raw[name] = records
        angular[name] = [_old_upper(api, value, name + "/" + str(j))
                         for j, value in enumerate(records)]
    norm_raw = {name: rb[name] for name in ("beta_abs_upper", "K_abs_upper", "gamma_abs_upper")}
    norms = {name: _old_upper(api, value, name) for name, value in norm_raw.items()}
    packet.update({
        "family_delta": family_delta,
        "family_mean": family_mean,
        "intrinsic_real_boxes": intrinsic,
        "original_intrinsic_complex_records": intrinsic_raw,
        "original_repaired_response_upper_records": response_raw,
        "original_exact_offsets": offset_strings,
        "original_angular_records": angular_raw,
        "original_norm_records": norm_raw,
        "original_optical_speed_records": {
            "optical_speed_lower": eta_low_record, "optical_speed_upper": eta_high_record,
        },
        "angular_upper": angular, "norm_upper": norms,
        "exact_direction_radius": str(delta),
        "radial_enclosure": [str(left), str(right)],
        "same_germ": {
            "candidate_sha256": CANDIDATE_SHA256,
            "background_definition_sha256": BACKGROUND_DEFINITION_SHA256,
            "explicit_direction_definition_sha256": DIRECTION_DEFINITION_SHA256,
            "root_germ_native_sha256": GERM_NATIVE_SHA256,
            "root_budget_native_sha256": ROOT_BUDGET_NATIVE_SHA256,
            "piece": COLLAR_PIECE, "true_root_interval": list(ROOT_INTERVAL),
            "body_cut": BODY_CUT, "outer_value_radius": "1/100000",
            "original_moving_strip": "1/1024", "delta_radius": "1/100000000",
            "actual_eta_source": "old completed full-family optical_speed_lower/upper",
            "actual_eta_identity": "-gamma*m_delta; same function in A and A_c",
            "centre_mean_is_separate_from_actual_eta": True,
            "old_193_uppers_are_error_envelopes_not_signed_centre_coefficients": True,
            "true_root_not_replaced_by_enclosure_endpoint": True,
            "only_value_enclosures_no_inner_half_disk_derivative_transfer": True,
            "no_intrinsic_parameter_family_enlargement": True,
            "all_native_bytes_and_full_original_scopes_admitted_by_owner": True,
        },
    })
    return packet


def _coordinate(value):
    require(isinstance(value, tuple) and len(value) == 2
            and type(value[0]) is int and value[0] in (0, 1)
            and type(value[1]) is int and value[1] >= 0
            and (value[0] == 1 or value[1] > 0),
            "physical parity coordinate, with only the true even mean")


def multiplier_entry(poly, parity, output, input_, sqrt_two, zero):
    """Same real L2 matrix: mean basis1, nonmean basis sqrt(2) sin/cos."""
    _coordinate(output)
    _coordinate(input_)
    oc, k = output
    ic, j = input_
    if parity == 0:
        if oc != ic:
            return zero
        if j == 0:
            return poly.get(0, zero) if k == 0 else sqrt_two * poly.get(k, zero)
        if k == 0:
            return sqrt_two * poly.get(j, zero) if ic == 1 else zero
        minus, plus = poly.get(k - j, zero), poly.get(k + j, zero)
        return minus - plus if ic == 0 else minus + plus
    require(parity == 1, "real-even or imaginary-odd Laurent multiplier")
    if oc == ic:
        return zero
    if ic == 1:
        if j == 0:
            return -sqrt_two * poly.get(k, zero)
        return -(poly.get(k - j, zero) + poly.get(k + j, zero))
    if k == 0:
        return -sqrt_two * poly.get(j, zero)
    return poly.get(k - j, zero) - poly.get(k + j, zero)


def _local_signed_entry(packet, output, input_, sqrt_two, zero):
    oc, k = output
    ic, j = input_
    value = zero
    if oc == ic:
        value += multiplier_entry(packet["la"] if oc == 0 else packet["le"],
                                  0, output, input_, sqrt_two, zero)
        if j:
            value += (4 * j if ic == 0 else -4 * j) * multiplier_entry(
                packet["d"], 1, output, (1 - ic, j), sqrt_two, zero)
    else:
        value += multiplier_entry(packet["Kell"] if oc == 0 else packet["ell"],
                                  1, output, input_, sqrt_two, zero)
        if j == k and j:
            value += 4 * j * packet["eta"] * (packet["K"] if oc == 0 else 1)
    if ic == 1 and j == 0 and k:
        if oc == 0:
            value -= sqrt_two * 4 * k * packet["gamma"] * packet["K"] * packet["v"].get(k, zero)
        else:
            value += sqrt_two * 4 * k * packet["gamma"] * packet["u"].get(k, zero)
    return value


def _primitive_signed_entry(words, output, input_, sqrt_two, zero):
    """Whole -2*a*I*P_even*b, with true intermediate m=1,2,... ."""
    oc, k = output
    ic, j = input_
    value = zero
    for left, right in words:
        ap, bp = left[oc], right[ic]
        adegree = max(map(abs, ap), default=0)
        bdegree = max(map(abs, bp), default=0)
        first = max(1, k - adegree, j - bdegree)
        last = min(k + adegree, j + bdegree)
        for m in range(first, last + 1):
            a = multiplier_entry(ap, 0 if oc == 0 else 1,
                                 output, (0, m), sqrt_two, zero)
            b = multiplier_entry(bp, 1 if ic == 0 else 0,
                                 (1, m), input_, sqrt_two, zero)
            value -= 2 * a * b / (4 * m)
    return value


def _centre_mean_row(packet, input_, sqrt_two, zero):
    ic, j = input_
    beta, curvature, mean = packet["beta"], packet["K"], packet["mc"]
    if j == 0:
        return beta * (1 - packet["S_mean"] - 2 * curvature * mean * mean)
    if ic == 0:
        return 2 * sqrt_two * beta * mean * packet["u"].get(j, zero)
    return -2 * sqrt_two * beta * mean * curvature * packet["v"].get(j, zero)


def _family_mean_row(delta, input_, sqrt_two, zero):
    ic, j = input_
    beta, curvature, mean, error_mean = delta["beta"], delta["K"], delta["mc"], delta["em"]
    if j == 0:
        return -beta * (delta["S_mean"] + 2 * curvature *
                       (2 * mean * error_mean + error_mean * error_mean))
    if ic == 0:
        product = (mean * delta["u"].get(j, zero)
                   + error_mean * delta["centre_u"].get(j, zero)
                   + error_mean * delta["u"].get(j, zero))
        return 2 * sqrt_two * beta * product
    product = (mean * delta["v"].get(j, zero)
               + error_mean * delta["centre_v"].get(j, zero)
               + error_mean * delta["v"].get(j, zero))
    return -2 * sqrt_two * beta * curvature * product


def centre_signed_entry(packet, output, input_, sqrt_two, zero):
    """Complete signed centre entry, BEFORE any absolute value or weighting."""
    require(packet["kind"] == CENTRE_KIND, "true centre packet, not a family error")
    _coordinate(output)
    _coordinate(input_)
    if output == (1, 0):
        return _centre_mean_row(packet, input_, sqrt_two, zero)
    return (_local_signed_entry(packet, output, input_, sqrt_two, zero)
            + _primitive_signed_entry([(packet["a"], packet["b"])],
                                      output, input_, sqrt_two, zero))


def family_signed_increment_entry(delta, output, input_, sqrt_two, zero):
    """Complete signed A-A_c entry, including all full96 quadratic terms."""
    require(delta["kind"] == DELTA_KIND
            and delta["actual_eta_is_identical_in_both_operators"] is True,
            "typed complete family increment with no artificial speed difference")
    _coordinate(output)
    _coordinate(input_)
    if output == (1, 0):
        return _family_mean_row(delta, input_, sqrt_two, zero)
    return (_local_signed_entry(delta, output, input_, sqrt_two, zero)
            + _primitive_signed_entry(delta["primitive_words"], output, input_, sqrt_two, zero))


def centre_adjoint_signed_entry(packet, output, input_, sqrt_two, zero):
    """True full adjoint in the SAME normalized real L2 measure."""
    return centre_signed_entry(packet, input_, output, sqrt_two, zero)


def family_adjoint_signed_increment_entry(delta, output, input_, sqrt_two, zero):
    """Includes -(delta d partial + delta d_phi), reversed words, and mean adjoint."""
    return family_signed_increment_entry(delta, input_, output, sqrt_two, zero)


def weighted_signed_entry(entry, packet, output, input_, sqrt_two, zero,
                          output_weight, input_inverse_weight):
    """Apply declared Riesz/S weights to one full signed entry, without abs.

    For a dual map, entry must be the TRUE adjoint callback and these must be
    the actual dual input/output weights. No commutation with multipliers is
    asserted. H1 and fractional rows are not inferred from an L2 scalar fee.
    """
    return (output_weight * entry(packet, output, input_, sqrt_two, zero)
            * input_inverse_weight)


def complete_family_positive_fees(packet, api):
    """Optional private L2 fallback; never the signed paired H_c algorithm.

    Original full_family_U/V are positive sums of germ+repair+delta fees in
    the pinned root-budget SOURCE, so they also dominate the centre terms.
    This does not infer a centre norm from the norm of a sum. The current
    two-sided trial must first combine its full signed (r,s) kernel; this
    fallback must not replace that cancellation by old171 plus positive legs.
    """
    require(packet["kind"] == CENTRE_KIND, "complete collar working packet")
    angular, norms = packet["angular_upper"], packet["norm_upper"]
    U, U1 = angular["full_family_U_angular_norms"][:2]
    V, V1 = angular["full_family_V_angular_norms"][:2]
    zu, zu1 = angular["direction_angular_norms_u"][:2]
    zv, zv1 = angular["direction_angular_norms_v"][:2]
    delta = _q(api, packet["exact_direction_radius"])
    eu, eu1, ev, ev1 = delta * zu, delta * zu1, delta * zv, delta * zv1
    beta, curvature, gamma = (norms[name] for name in
        ("beta_abs_upper", "K_abs_upper", "gamma_abs_upper"))
    du2 = 2 * U * eu + eu * eu
    dv2 = 2 * V * ev + ev * ev
    duv = U * ev + V * eu + eu * ev
    local = (beta * (3 * du2 + curvature * dv2)
             + beta * (du2 + 3 * curvature * dv2)
             + (1 + curvature) * 2 * beta * duv)
    drift_phi = beta * (du2 + curvature * dv2)
    drift = drift_phi / 4
    primitive = beta / 2 * (
        (eu1 + ev1) * (U + curvature * V)
        + (U1 + V1) * (eu + curvature * ev)
        + (eu1 + ev1) * (eu + curvature * ev))
    mean_rank = gamma * (eu1 + curvature * ev1)
    return {"drift": api.upper(drift), "drift_phi": api.upper(drift_phi),
            "local": api.upper(local), "primitive": api.upper(primitive),
            "low_mean_rank": api.upper(mean_rank)}


def family_l2_fallback(fees, api, *, input_last, adjoint=False, include_mean_rank=True):
    """Complete unweighted L2 bound with the TRUE input derivative factor.

    For input_last=224 the primal drift factor is 896, not the old640.
    The adjoint additionally pays delta d_phi. Full output can reach416;
    this routine does not project it to224 or infer any H1/Riesz bound.
    A mean-rank omission requires the caller's exact corresponding projection.
    """
    require(type(input_last) is int and input_last >= 0,
            "actual declared Fourier input band")
    require(type(adjoint) is bool and type(include_mean_rank) is bool,
            "explicit adjoint and mean-rank qualifications")
    value = 4 * input_last * fees["drift"] + fees["local"] + fees["primitive"]
    if adjoint:
        value += fees["drift_phi"]
    if include_mean_rank:
        value += fees["low_mean_rank"]
    return api.upper(value)


def complete_body_family_positive_fees(row, api, *, same_actual_eta_retained):
    """Private full-family error fees on ONE admitted original body row.

    The 4650-row/4801-intersection closure and both whole orders belong to the
    owner's existing readonly admission. This function reads all required
    complete old records. It never calls the original coefficient or delta
    producer and never recreates its saved drift/local fees. The only new
    products are the complete error legs for the new trial, whose true input
    band is subsequently passed to family_l2_fallback.

    The centre and actual generator must retain the SAME actual full-family
    optical speed. This is a function identity of the chosen trial, not a
    comparison of two interval displays. There is then no principal-speed
    error. All mean ranks, true adjoint drift derivatives and output spaces
    remain to be paid as declared. The old640 bound is not extended to224.
    """
    require(same_actual_eta_retained is True,
            "actual and centre principal speed are the same full-family function")
    left, right = tuple(map(Fraction, row["interval"]))
    require(Fraction(BODY_CUT) <= left < right <= Fraction(25, 8),
            "original body row; collar germ is not extrapolated into transition")
    require(row["Z_offset_is_piecewise_radial_constant_angular_derivative_not_radial"] is True
            and row["arbitrary_direction_jump_still_a_separate_affine_source"] is True,
            "original direction derivative and independent affine-jump qualifications")
    base = row["original_complete_repaired_bounds"]
    fees = row["complete_delta_fees"]
    U, V, U1, V1 = (
        _old_upper(api, base[name], "body/original_complete_repaired_bounds/" + name, process=True)
        for name in ("U_A0", "V_A0", "U_phi_A0", "V_phi_A0"))
    e0 = _old_upper(api, row["full_delta_A0"], "body/full_delta_A0", process=True)
    e1 = _old_upper(api, row["full_delta_angular_A0"],
                    "body/full_delta_angular_A0", process=True)
    intrinsic = row["original_intrinsic_enclosure"]
    boxes = {}
    for name in ("beta", "K", "gamma", "Cref"):
        boxes[name] = api.old_interval(_record(intrinsic[name],
                                               "body/original_intrinsic_enclosure/" + name))
    require(api.lower(boxes["K"]) > 0 and api.lower(boxes["gamma"]) > 0
            and _signed_upper(api, boxes["Cref"]) < 0,
            "original body intrinsic domain, using its complete endpoint hull")
    beta, curvature, gamma = (api.magnitude(boxes[name]) for name in ("beta", "K", "gamma"))
    saved = {name: _old_upper(api, fees[name], "body/complete_delta_fees/" + name, process=True)
             for name in ("local_a", "local_e", "local_b", "drift", "drift_phi")}
    local = saved["local_a"] + saved["local_e"] + (1 + curvature) * saved["local_b"]
    # Exact three-word difference grouped as da*I*(bc+db)+ac*I*db.
    # e1 is the original complete u/v pair derivative fee, not twice that fee.
    primitive = beta / 2 * (
        e1 * (U + e0 + curvature * (V + e0))
        + (U1 + V1) * (1 + curvature) * e0)
    mean_rank = gamma * (1 + curvature) * e1
    return {
        "drift": saved["drift"], "drift_phi": saved["drift_phi"],
        "local": api.upper(local), "primitive": api.upper(primitive),
        "low_mean_rank": api.upper(mean_rank),
    }
