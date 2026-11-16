"""WZE: exact waist reconstruction and all four endpoint contributions.
No entry point, I/O, old producer import or old target invocation.
The api argument is the NEW shared finite-Jet support module. Its algebra
uses positive normalized derivative bounds, never a sampled Taylor series.
All WGS data are admitted saved supremum/component-sum jets.
The owner activates the new shared API record-capture hook before each call;
every issued record is preserved before the next one, including on failure.
Every completed node is handed to publish_graph; downstream work is decoded
only from that callback's canonical, retained 75-digit complete document.
"""
from __future__ import annotations
from fractions import Fraction
from math import factorial
from copy import deepcopy

N0 = 388
FIRST_MODE = 97
WAIST_JS = 268435456
NODE_NAMES = (
    "complete_exact_waist_finite_reconstruction",
    "complete_free_waist_Airy_and_Schur_map",
    "complete_four_waist_endpoint_contributions",
)
QUALIFICATION_NAMES = (
    "same_selected_real_member",
    "same_original_root_cutoff_97_input",
    "complete_WGS_pair_admitted",
    "same_WES_waist_free_neighbourhood_minus_T_gt_L",
    "same_WZR_metric_beta_zero_at_waist",
    "same_N_actual_angular_operator",
    "ordinary_radial_amplitude_derivatives_retained",
    "complete_extended_first_amplitude_admitted",
    "same_SP_actual_waist_density_q_and_mean_records",
    "same_WT_Js_268435456_whole_forward_remainder",
    "same_SW_W_bound_before_waist_ng",
    "original_physical_means_and_transported_input_retained",
)
ORIGINAL_RECORD_PATHS = {
    "waist_ng_upper": {
        "role": "SP",
        "path": ["actual_scientific_receipt", "complete_endpoint_readout_conclusion",
                 "waist_complete_radial_factors", "density_radial_factor_upper"],
        "endpoint": "upper"},
    "waist_q_lower": {
        "role": "SP",
        "path": ["actual_scientific_receipt", "complete_endpoint_readout_conclusion",
                 "waist_complete_radial_factors", "q_lower"],
        "endpoint": "positive_lower"},
    "waist_q_upper": {
        "role": "SP",
        "path": ["actual_scientific_receipt", "complete_endpoint_readout_conclusion",
                 "waist_complete_radial_factors", "q_upper"],
        "endpoint": "upper"},
    "waist_absolute_mean_lower": {
        "role": "SP",
        "path": ["actual_scientific_receipt", "complete_endpoint_readout_conclusion",
                 "waist_complete_radial_factors", "complete_absolute_mean_lower"],
        "endpoint": "positive_lower"},
    "waist_U_L2_upper_from_original_pair_A0": {
        "role": "WGS_original_inputs",
        "path": ["copied_original_scalar_records", "Q_0_0"],
        "endpoint": "upper"},
    "WT_complete_A2_upper": {
        "role": "WT",
        "path": ["complete_fixed_cutoff_results", 1,
                 "forward_complete_strong_remainder"],
        "endpoint": "upper", "required_sibling_J": WAIST_JS},
    "SW_complete_W_Hminus4_3_upper_before_ng": {
        "role": "SW",
        "path": ["complete_new_leading_and_conjugation_conclusion",
                 "complete_W_Hminus4_3_upper"],
        "endpoint": "upper"},
}
INNER_ZERO_TERMS = (
    ("minus_P_ell_mean_G", "ell_at_waist_is_exactly_zero"),
    ("two_beta_Pvphi_mean_I3_uG", "metric_beta_at_waist_is_exactly_zero"),
    ("two_beta_mean_G_Pvphi_Iu", "metric_beta_at_waist_is_exactly_zero"),
    ("minus_P_bloc_mean_W", "bloc_at_waist_is_exactly_zero"),
    ("two_betaK_Pvphi_mean_I3_vW", "metric_beta_at_waist_is_exactly_zero"),
    ("two_betaK_mean_W_Pvphi_Iv", "metric_beta_at_waist_is_exactly_zero"),
    ("two_beta_z3_Pvphi_IU_dphi_I2_uG", "metric_beta_at_waist_is_exactly_zero"),
    ("two_betaK_z3_Pvphi_IU_dphi_I2_vW", "metric_beta_at_waist_is_exactly_zero"),
)
SYMBOL_COMPONENTS = tuple(
    {"input_sign": eps, "reference": reference, "phase_branch": sigma}
    for eps in (-1, 1) for reference in ("Ai", "Bi") for sigma in (-1, 1)
)

def require(condition, message):
    if not condition:
        raise ValueError(message)

def positive_power(api, x, exponent, label):
    exponent = Fraction(exponent)
    if exponent < 0:
        base = api.lower(x, label)
    else:
        base = api.up(x)
        if base == 0:
            require(exponent > 0, "zero nonpositive power: " + label)
            return api.ex(0)
    return api.up(base ** (api.ex(exponent.numerator) /
                           api.ex(exponent.denominator)))

def save_upper(api, doc, name, value):
    doc[name] = api.record(api.up(value))
    return api.read_up(doc[name])

def save_lower(api, doc, name, value):
    doc[name], ignored = api.lower_record(value, name)
    return api.read_lower(doc[name], name + " retained")

def upper_sum(api, values):
    return api.up(sum(values, api.ex(0)))

def angular(api, jet, degree, label=None):
    jet.need(degree, 0)
    return jet.part(degree, 0, label or jet.label)

def angular_add(api, *jets, label="complete_angular_sum"):
    require(bool(jets), "empty angular sum")
    degree = min(j.m for j in jets)
    return api.add(*jets, m=degree, p=0, label=label)

def angular_mul(api, *jets, label="complete_angular_product"):
    require(bool(jets), "empty angular product")
    degree = min(j.m for j in jets)
    return api.mul(*jets, m=degree, p=0, label=label)

def ordinary_angle(api, jet, order):
    jet.need(order, 0)
    return api.up(api.ex(factorial(order)) * jet.c[0, order])

def retain_angular(api, jet):
    jet.need(jet.m, 0)
    records = [api.record(jet.c[0, j]) for j in range(jet.m + 1)]
    doc = {"shape": [jet.m, 0],
           "normalized_angular_coefficients": records,
           "norm": "complete scalar supremum or amplitude entry-sum; derivative divided by j!"}
    return decode_angular(api, doc, jet.label), doc

def decode_angular(api, doc, label):
    degree, radial = doc["shape"]
    require(radial == 0 and isinstance(degree, int) and degree >= 0,
            "invalid retained angular shape")
    records = doc["normalized_angular_coefficients"]
    require(len(records) == degree + 1, "incomplete retained angular jet")
    return api.Jet(degree, 0, {(0, j): api.read_up(records[j])
                              for j in range(degree + 1)}, label)

def retain_mapping(api, mapping):
    work, doc = {}, {}
    for name, jet in mapping.items():
        work[name], doc[name] = retain_angular(api, jet)
    return work, doc

def decode_mapping(api, mapping):
    return {k: decode_angular(api, v, k) for k, v in mapping.items()}

def finite_primitive_amplitude(api, Hinv, value, count):
    """I_0=H^-1, I_(l+1)=-H^-1 dphi I_l; signs only become positive norms."""
    require(isinstance(count, int) and 0 <= count <= 2, "finite primitive depth")
    result = angular_mul(api, Hinv, value, label="I0_" + value.label)
    for depth in range(count):
        result = angular_mul(api, Hinv,
                   result.derivative(da=1, p=0),
                   label="I" + str(depth + 1) + "_" + value.label)
    return result

def finite_mean_amplitude(api, Hinv, value, count):
    """R_phi a=dphi(H^-1 a), kept distinct from H^-1 dphi a."""
    require(isinstance(count, int) and 0 <= count <= 2, "finite mean depth")
    result = value
    for depth in range(count):
        result = angular_mul(api, Hinv, result).derivative(
            da=1, p=0, label="Rphi_" + str(depth + 1) + "_" + value.label)
    return result

def validate_waist_input(waist):
    flags = waist["qualifications"]
    require(set(flags) == set(QUALIFICATION_NAMES) and
            all(flags.get(k) is True for k in QUALIFICATION_NAMES),
            "one complete same-waist qualification is missing")
    require(waist.get("waist_fixed_Js") == WAIST_JS, "different actual waist cutoff")
    require(set(waist["original_records"]) == set(ORIGINAL_RECORD_PATHS),
            "incomplete typed original waist records")
    for value in waist["original_records"].values():
        require(isinstance(value, dict) and set(value) == {"ball"},
                "a complete original ball record is required")
    for key in ("T", "x", "y", "Q", "H_inverse_entry_sum", "a0", "b0", "phase"):
        require(key in waist["strict"], "missing complete saved strict jet: " + key)
    for key in ("a1_ext", "b1_ext"):
        require(key in waist["extended"], "missing complete extended amplitude: " + key)

def prepare_waist_input(handoff, extended_strict, original_records, qualifications):
    """Type-only adapter. The caller has pinned every old file and saved new node."""
    return {"strict": handoff["patches"]["strict"],
            "extended": extended_strict,
            "strict_eta_lower": handoff["old"]["strict_eta_lower"],
            "strict_phase_lower": handoff["old"]["strict_phase_lower"],
            "original_records": deepcopy(original_records),
            "qualifications": deepcopy(qualifications),
            "waist_fixed_Js": WAIST_JS}

def start_progress(progress_state, node_name):
    require(isinstance(progress_state, dict), "mutable scientific prefix state")
    require(node_name not in progress_state,
            "a preserved complete or partial target cannot be silently recomputed")
    state = {"kind": "recoverable_new_scientific_node_prefix_v1",
             "node_name": node_name, "complete": False,
             "persisted_complete_node": False, "current_stage": "initializing",
             "complete_scientific_document_prefix": {"kind": node_name, "complete": False},
             "all_record_events_durably_captured_by_owner_neutral_API": True}
    progress_state[node_name] = state
    return state

def progress_group(state, stage, key=None, value=None):
    state["current_stage"] = stage
    if key is not None:
        state["complete_scientific_document_prefix"][key] = value

def finish_progress(state, doc, publish_graph):
    require(callable(publish_graph), "atomic bare-math publication callback")
    state["complete"] = True
    state["current_stage"] = "complete_graph_before_atomic_publication"
    state["complete_scientific_document_prefix"] = doc
    saved = publish_graph(state["node_name"], doc)
    require(isinstance(saved, dict) and saved == doc,
            "complete persisted mathematics changed on canonical readback")
    state["persisted_complete_node"] = True
    state["current_stage"] = "complete_graph_read_back"
    return saved

def complete_waist_reconstruction(api, waist, publish_graph, progress_state):
    state = start_progress(progress_state, NODE_NAMES[0])
    validate_waist_input(waist)
    g = waist["strict"]
    ext = waist["extended"]
    records = waist["original_records"]
    constants = {}
    progress_group(state, "radial_factors", "new_complete_constants", constants)
    einv = save_upper(api, constants, "complete_waist_eta_inverse_upper",
                     api.ex(1) / api.lower(waist["strict_eta_lower"], "saved strict eta"))
    ng = api.read_up(records["waist_ng_upper"])
    qlo = api.read_lower(records["waist_q_lower"], "actual waist q")
    qhi = api.read_up(records["waist_q_upper"])
    qinvhalf = positive_power(api, qlo, Fraction(-1, 2), "actual waist q")
    qhalf = positive_power(api, qhi, Fraction(1, 2), "actual waist q")
    Rop = save_upper(api, constants, "complete_density_pair_operator_upper",
                    ng * max(qinvhalf, qhalf))
    Rfirst = save_upper(api, constants, "complete_density_first_column_entry_sum_upper",
                       ng * api.ex(2).sqrt() * qinvhalf)
    Rsecond = save_upper(api, constants, "complete_density_second_column_entry_sum_upper",
                        ng * api.ex(2).sqrt() * qhalf)

    progress_group(state, "finite_amplitude_ports")
    Hinv = angular(api, g["H_inverse_entry_sum"], 6, "saved_waist_Hinverse_entry_sum")
    T = angular(api, g["T"], 6, "saved_waist_minus_T_sup")
    one = api.constant(api.ex(1), 6, 0, "one")
    # At this waist d=0, DX=X_r=Q*t*y and DT=T_r=Q*x.
    # Matrix entry-sum: 2|X_r|+(1+t)|T_r|. No phase value is used.
    M = angular_mul(api, angular(api, g["Q"], 6),
          angular_add(api,
             api.scale(angular_mul(api, T, angular(api, g["y"], 6)), api.ex(2)),
             angular_mul(api, angular_add(api, one, T),
                         angular(api, g["x"], 6))),
          label="complete_waist_M_entry_sum")
    w0 = angular_add(api, angular(api, g["a0"], 6), angular(api, g["b0"], 6),
                     label="complete_w0")
    w0r = angular_add(api,
          g["a0"].derivative(dr=1, m=5, p=0),
          g["b0"].derivative(dr=1, m=5, p=0), label="complete_w0_r")
    w1 = angular_add(api, angular(api, ext["a1_ext"], 5),
          angular(api, ext["b1_ext"], 5), label="complete_w1_ext")
    w1r = angular_add(api,
          ext["a1_ext"].derivative(dr=1, m=4, p=0),
          ext["b1_ext"].derivative(dr=1, m=4, p=0), label="complete_w1_ext_r")
    ports, port_doc = retain_mapping(api, dict(M=M, w0=w0, w0_r=w0r,
                                               w1_ext=w1, w1_ext_r=w1r))
    progress_group(state, "finite_g_recursion", "complete_amplitude_ports", port_doc)
    gd = {}
    progress_group(state, "g0", "complete_g_jets", gd)
    M, w0, w0r, w1, w1r = (ports[k] for k in
                              ("M", "w0", "w0_r", "w1_ext", "w1_ext_r"))
    g0, dg0 = retain_angular(api, api.scale(
        angular_mul(api, Hinv, M, w0, label="g0"), einv))
    gd["0"] = dg0
    progress_group(state, "g1")
    g1, dg1 = retain_angular(api, angular_mul(api, Hinv,
        angular_add(api,
          api.scale(angular_add(api, angular_mul(api, M, w1), w0r), einv),
          g0.derivative(da=1, p=0)), label="g1"))
    gd["1"] = dg1
    progress_group(state, "g2")
    g2, dg2 = retain_angular(api, angular_mul(api, Hinv,
        angular_add(api, api.scale(w1r, einv),
                    g1.derivative(da=1, p=0)), label="g2"))
    gd["2"] = dg2
    progress_group(state, "g3")
    g3, dg3 = retain_angular(api, angular_mul(api, Hinv,
                           g2.derivative(da=1, p=0), label="g3"))
    gd["3"] = dg3
    gg = [g0, g1, g2, g3]
    require([v.m for v in gg] == [6, 5, 4, 3], "finite endpoint derivative closure")
    g3phi = save_upper(api, constants, "complete_g3_phi_upper",
                      ordinary_angle(api, g3, 1))

    V, Vdoc = {}, {}
    progress_group(state, "complete_V_polynomial", "complete_V_polynomial", Vdoc)
    for k, value in enumerate(gg):
        part = api.scale(value, Rfirst, label="V_" + str(k))
        if k in (0, 1):
            part = angular_add(api, part, api.scale(w0 if k == 0 else w1, Rsecond),
                               label="V_" + str(k))
        V[str(k)], Vdoc[str(k)] = retain_angular(api, part)
    Braw = {}
    I2V, I2doc, terminal_rows = {}, {}, []
    progress_group(state, "finite_outer_primitive", "complete_I2V_polynomial", I2doc)
    progress_group(state, "finite_outer_primitive", "complete_outer_terminal_rows", terminal_rows)
    for k in range(4):
        for depth in range(3):
            part = finite_primitive_amplitude(api, Hinv, V[str(k)], depth)
            power = str(k + depth)
            Braw[power] = angular_add(api, Braw[power], part) if power in Braw else part
            if depth == 2:
                I2V[str(k)], I2doc[str(k)] = retain_angular(api, part)
        terminal_rows.append({
            "input_degree": k,
            "complete_derivative_upper": api.record(ordinary_angle(api, I2V[str(k)], 1)),
        })
    B, Bdoc = retain_mapping(api, {
        str(k): Braw[str(k)] for k in range(6)})
    progress_group(state, "complete_outer_polynomial", "complete_outer_B_polynomial", Bdoc)
    require([B[str(k)].m for k in range(6)] == [6, 5, 4, 3, 2, 1],
            "complete degree-five outer polynomial")
    terminal = save_upper(api, constants, "complete_outer_terminal_weighted_sum_upper",
        upper_sum(api, (
            api.read_up(row["complete_derivative_upper"]) *
            positive_power(api, api.ex(N0), -row["input_degree"], "fixed input cutoff")
            for row in terminal_rows)))
    mean_rows = []
    progress_group(state, "complete_outer_mean", "complete_outer_mean_rows", mean_rows)
    for k in range(6):
        depth = max(0, 2-k)
        value = finite_mean_amplitude(api, Hinv, B[str(k)], depth)
        term = api.up(value.c[0, 0] * positive_power(
                        api, api.ex(N0), 2-k-depth, "fixed input cutoff"))
        mean_rows.append({"input_degree": k, "exact_mean_iterations": depth,
                          "nonpositive_cutoff_exponent": 2-k-depth,
                          "complete_weighted_mean_coefficient_upper": api.record(term)})
    mean_weight = save_upper(api, constants, "complete_outer_mean_coefficient_upper",
        upper_sum(api, (api.read_up(r["complete_weighted_mean_coefficient_upper"])
                        for r in mean_rows)))

    doc = {
        "kind": NODE_NAMES[0], "complete": True,
        "same_waist_qualifications": deepcopy(waist["qualifications"]),
        "complete_amplitude_ports": port_doc,
        "complete_g_jets": {"0": dg0, "1": dg1, "2": dg2, "3": dg3},
        "complete_V_polynomial": Vdoc,
        "complete_I2V_polynomial": I2doc,
        "complete_outer_B_polynomial": Bdoc,
        "complete_outer_terminal_rows": terminal_rows,
        "complete_outer_mean_rows": mean_rows,
        "new_complete_constants": constants,
        "exact_inner_zero_terms": [
            {"term": name, "value": "0", "exact_reason": reason}
            for name, reason in INNER_ZERO_TERMS],
        "full_inner_residual_polynomial": {
            "only_nonzero_degree": 3, "exact_coefficient": "eta_w*dphi(g3)",
            "lower_degrees_cancelled_by_complete_g_recursion": [-1, 0, 1, 2],
            "degrees_4_5_6_exact_zero_from_waist_metric": True},
        "retained_outer_mean_and_terminal": True,
        "retained_independent_physical_mean": True,
        "metric_radial_derivatives_not_declared_zero": True,
        "coefficient_norm": "ordinary angular supremum/component-sum, normalized by j!",
        "primitive_one_fourth_used_only_on_actual_L2_operator": True,
        "original_successful_targets_recomputed": 0,
    }
    saved = finish_progress(state, doc, publish_graph)
    return decode_waist_reconstruction_node(api, saved), saved

def complete_tail_weights(api):
    """Positive integral bounds for the complete two-sign series, not truncations."""
    rows = {}
    gamma = api.ex(1) + api.ex(1) / api.ex(16*FIRST_MODE*FIRST_MODE)
    gamma43 = save_upper(api, rows, "complete_Bessel_ratio_four_thirds_upper",
                        positive_power(api, gamma, Fraction(4, 3), "Bessel ratio"))
    xi0sq = save_upper(api, rows, "complete_Xi0_squared_upper",
                     api.ex(4) / (api.ex(4)**4 * api.ex(3) * api.ex(96)**3))
    xi2sq = save_upper(api, rows, "complete_Xi2_squared_upper",
        api.ex(6) * gamma43 *
        positive_power(api, api.ex(4), Fraction(-4, 3), "physical frequency four") *
        positive_power(api, api.ex(96), Fraction(-1, 3), "integral lower endpoint"))
    ximsq = save_upper(api, rows, "complete_Xi23_6_squared_upper",
                    api.ex(2) * gamma43 /
                    (api.ex(4)**5 * api.ex(4) * api.ex(96)**4))
    xi0 = save_upper(api, rows, "complete_Xi0_upper", xi0sq.sqrt())
    xi2 = save_upper(api, rows, "complete_Xi2_upper", xi2sq.sqrt())
    xim = save_upper(api, rows, "complete_Xi23_6_upper", ximsq.sqrt())
    return {"Xi0": xi0, "Xi2": xi2, "Xi23_6": xim}, {
        "new_complete_records": rows,
        "first_positive_integer_mode": FIRST_MODE,
        "physical_frequency": "4*abs(j)",
        "integral_lower_endpoint": 96,
        "Xi0_reference_sign_count": 4,
        "Xi2_input_sign_count": 2,
        "Xi23_6_input_sign_count": 2,
        "bound": "sum from j=97 to infinity of j^-p is at most integral from 96 to infinity",
        "full_Bessel_weights_retained": True,
        "no_root_scattering_matrix_Hilbert_Schmidt_sum": True,
    }

def complete_free_waist_map(api, waist, reconstruction, extension, publish_graph, progress_state):
    state = start_progress(progress_state, NODE_NAMES[1])
    validate_waist_input(waist)
    require(reconstruction["original_node"] == NODE_NAMES[0],
            "reconstruction must be decoded from its published complete node")
    constants = {}
    progress_group(state, "real_Airy_constants", "complete_real_Airy_constants", constants)
    T = angular(api, waist["strict"]["T"], 2, "actual_waist_minus_T_sup")
    tminus = save_lower(api, constants, "complete_actual_waist_t_lower",
                       api.ex(Fraction(1, 2000)))
    tplus = save_upper(api, constants, "complete_actual_waist_t_upper", T.c[0, 0])
    omega = save_lower(api, constants, "complete_actual_waist_omega_lower",
                      api.ex(Fraction(2, 3)) *
                      tminus ** (api.ex(3)/api.ex(2)))
    pi_ball = api.arb.pi()
    pi_up = save_upper(api, constants, "complete_pi_upper", pi_ball)
    invsqrtpi = save_upper(api, constants, "complete_inverse_sqrt_pi_upper",
                          api.ex(1) / api.lower(pi_ball.sqrt(), "sqrt(pi)"))
    tminus_quarter = save_upper(api, constants, "complete_t_inverse_fourth_upper",
                         positive_power(api, tminus, Fraction(-1, 4), "waist t"))
    tplus_quarter = save_upper(api, constants, "complete_t_fourth_upper",
                         positive_power(api, tplus, Fraction(1, 4), "waist t"))
    uu, vv, airy_exact = [], [], []
    previous = Fraction(1)
    for k in range(1, 4):
        uk = (Fraction((6*k-5)*(6*k-3)*(6*k-1), (2*k-1)*216*k)
              * previous)
        vk = Fraction(6*k+1, 1-6*k) * uk
        uu.append(save_upper(api, constants, "Airy_u_"+str(k), api.ex(uk)))
        vv.append(save_upper(api, constants, "Airy_absolute_v_"+str(k), api.ex(abs(vk))))
        airy_exact.append({"k": k, "u": str(uk), "signed_v": str(vk)})
        previous = uk
    N = api.ex(N0)
    pa = save_upper(api, constants, "complete_scaled_Airy_height_upper",
         tminus_quarter*invsqrtpi*
         (api.ex(1)+upper_sum(api,(uu[k-1]/(N**k*omega**k) for k in range(1,4)))))
    pb = save_upper(api, constants, "complete_scaled_Airy_derivative_upper",
         tplus_quarter*invsqrtpi*
         (api.ex(1)+upper_sum(api,(vv[k-1]/(N**k*omega**k) for k in range(1,4)))))
    Pstar = save_upper(api, constants, "complete_Pstar_upper", max(pa,pb))
    P1 = save_upper(api, constants, "complete_P1_upper",
         invsqrtpi/omega*max(uu[0]*tminus_quarter, vv[0]*tplus_quarter))
    P2 = save_upper(api, constants, "complete_P2_upper",
         invsqrtpi*max(tminus_quarter*(uu[1]/omega**2+uu[2]/(N*omega**3)),
                      tplus_quarter*(vv[1]/omega**2+vv[2]/(N*omega**3))))

    rc = reconstruction["constants"]
    B = reconstruction["B"]
    pieces = {}
    progress_group(state, "complete_column_remainders", "complete_reconstruction_and_map_records", pieces)
    c_first = save_upper(api, pieces, "complete_inner_reconstruction_upper",
               rc["complete_density_pair_operator_upper"]*Pstar*
               rc["complete_g3_phi_upper"]/api.ex(16))
    c_outer = save_upper(api, pieces, "complete_outer_terminal_upper",
               Pstar*rc["complete_outer_terminal_weighted_sum_upper"]/api.ex(4))
    c_mean = save_upper(api, pieces, "complete_outer_auxiliary_mean_upper",
               Pstar*rc["complete_outer_mean_coefficient_upper"])
    crec = save_upper(api, pieces, "complete_reconstruction_upper",
                     c_first+c_outer+c_mean)
    atail = save_upper(api, pieces, "complete_Airy_higher_polynomial_upper",
             Pstar*upper_sum(api, (B[str(k)].c[0,0] *
                       positive_power(api,N,-(k-2),"fixed input cutoff") for k in range(2,6))))
    aone = save_upper(api, pieces, "complete_Airy_first_cross_upper",
                     P1*B["1"].c[0,0])
    atwo = save_upper(api, pieces, "complete_Airy_second_remainder_upper",
                     P2*(B["0"].c[0,0]+B["1"].c[0,0]/N))
    cairy = save_upper(api, pieces, "complete_Airy_remainder_upper", atail+aone+atwo)
    cpre = save_upper(api, pieces, "complete_common_column_remainder_upper", crec+cairy)

    progress_group(state, "complete_symbol_angular_jets")
    tm = api.power_jet(T,tminus,Fraction(-1,4),2,0,"actual_t_inverse_fourth")
    tp = api.power_jet(T,tminus,Fraction(1,4),2,0,"actual_t_fourth")
    oi = api.scale(api.power_jet(T,tminus,Fraction(-3,2),2,0,"actual_t_minus_three_halves"),
                   api.ex(Fraction(3,2)),label="actual_omega_inverse")
    weights = angular_add(api,tm,tp)
    A0 = api.scale(angular_mul(api,weights,angular(api,B["0"],2)),invsqrtpi/2,
                   label="complete_any_Airy_phase_A0")
    cross_weight = angular_add(api,api.scale(tm,uu[0]),api.scale(tp,vv[0]))
    A1 = api.scale(angular_add(api,
            angular_mul(api,weights,angular(api,B["1"],2)),
            angular_mul(api,oi,cross_weight,angular(api,B["0"],2))),
            invsqrtpi/2,label="complete_any_Airy_phase_A1")
    A0, A0doc = retain_angular(api,A0)
    progress_group(state, "complete_symbol_angular_jets", "complete_A0_angular_jet", A0doc)
    A1, A1doc = retain_angular(api,A1)
    progress_group(state, "complete_symbol_angular_jets", "complete_A1_angular_jet", A1doc)
    symbol, symbol_doc = retain_angular(api,angular_add(api,A0,api.scale(A1,api.ex(1)/N),
                              label="complete_A0_plus_input_inverse_A1"))
    progress_group(state, "complete_symbol_schur", "complete_A0_plus_inverse_input_A1_angular_jet", symbol_doc)
    D = [ordinary_angle(api,symbol,j) for j in range(3)]
    symbol_records = [api.record(v) for v in D]
    progress_group(state, "complete_symbol_schur", "complete_symbol_ordinary_derivatives_0_2", symbol_records)
    D = [api.read_up(v) for v in symbol_records]
    ml = api.lower(waist["strict_phase_lower"],"same true phase lower")
    phi2 = ordinary_angle(api,waist["strict"]["phase"],2)
    schur = save_upper(api,pieces,"complete_one_phase_reference_sign_Schur_upper",
        positive_power(api,ml,Fraction(-1,2),"same true phase lower") *
        (D[0]+pi_up*pi_up/api.ex(48)*(D[2]/ml**2+D[1]*phi2/ml**3)))
    schur_all = save_upper(api,pieces,"complete_all_eight_symbol_components_upper",
                          api.ex(len(SYMBOL_COMPONENTS))*schur)
    progress_group(state, "complete_tail_weights")
    tail_work, tail_doc = complete_tail_weights(api)
    progress_group(state, "complete_free_map", "complete_tail_weights", tail_doc)
    free_remainder = save_upper(api,pieces,"complete_free_map_remainder_upper",
                               tail_work["Xi0"]*cpre)
    KF = save_upper(api,pieces,"complete_free_map_L2_to_density_upper",
                   schur_all+free_remainder)
    CB = api.read_up(extension["constants"]["complete_cB_upper"])
    A1bi = save_upper(api,pieces,"complete_Bi_first_coefficients_two_sign_two_phase_sum_upper",
                     api.ex(4)*A1.c[0,0])
    K2 = save_upper(api,pieces,"complete_first_cancellation_column_upper",
                   (api.ex(1)+CB/N)*cpre+CB*A1bi)
    doc = {
        "kind":NODE_NAMES[1],"complete":True,
        "same_reconstruction_node":NODE_NAMES[0],
        "complete_real_Airy_constants":constants,
        "exact_Airy_coefficient_recurrence":airy_exact,
        "complete_reconstruction_and_map_records":pieces,
        "complete_A0_angular_jet":A0doc,
        "complete_A1_angular_jet":A1doc,
        "complete_A0_plus_inverse_input_A1_angular_jet":symbol_doc,
        "complete_symbol_ordinary_derivatives_0_2":symbol_records,
        "complete_symbol_components":[deepcopy(c) for c in SYMBOL_COMPONENTS],
        "one_complete_common_bound_applies_to_each_listed_component":True,
        "complete_tail_weights":tail_doc,
        "same_waist_density_factor_already_in_V_and_B":True,
        "Ai_and_Bi_real_remainders_retained":True,
        "cB_squared_and_first_Airy_cross_retained":True,
        "original_root_matrix_not_treated_as_column_HS_error":True,
        "all_low_outputs_means_and_two_physical_rows_retained":True,
        "new_scalar_exp_or_log_calls":0,
        "original_successful_targets_recomputed":0,
    }
    saved=finish_progress(state,doc,publish_graph)
    return decode_free_waist_map_node(api, saved), saved

def complete_four_waist_endpoints(api,waist,free_map,extension,mean_union,publish_graph,progress_state):
    state = start_progress(progress_state, NODE_NAMES[2])
    validate_waist_input(waist)
    require(free_map["original_node"]==NODE_NAMES[1],
            "free-waist map must come from its canonical published node")
    require(mean_union.get("complete_root_to_waist_mean") is True,
            "complete root-to-waist physical mean has not been published")
    require(mean_union.get("coefficient_power")=="n^(-23/6)",
            "different physical mean column normalization")
    records=waist["original_records"]
    ng=api.read_up(records["waist_ng_upper"])
    qlo=api.read_lower(records["waist_q_lower"],"actual waist q")
    qhi=api.read_up(records["waist_q_upper"])
    ml=api.read_lower(records["waist_absolute_mean_lower"],"actual waist physical mean")
    U0=api.read_up(records["waist_U_L2_upper_from_original_pair_A0"])
    WT=api.read_up(records["WT_complete_A2_upper"])
    SW=api.read_up(records["SW_complete_W_Hminus4_3_upper_before_ng"])
    constants={}
    progress_group(state, "scattering_and_mean_endpoint_factors", "complete_new_constants", constants)
    Cs=save_upper(api,constants,"complete_root_scattering_Hminus4_3_to_L2_upper",
         api.ex(Fraction(6,5))*(api.ex(16384)+
             api.ex(2)*positive_power(api,api.ex(N0),Fraction(-2,3),"fixed input cutoff")*
             api.ex(168)*free_map["pi_upper"]*
             api.read_up(extension["constants"]["complete_H1_upper"])))
    Ik=save_upper(api,constants,"complete_I_of_waist_Jb2_L2_upper",
                 U0/(api.ex(4)*ml))
    vz=save_upper(api,constants,"complete_physical_mean_endpoint_vector_upper",
                 ng*(qhi+Ik*Ik/qlo).sqrt())
    # Z is the published full root-to-waist n^-23/6 mean coefficient.
    Z=api.read_up(mean_union["new_complete_records"]["complete_physical_mean_upper"])
    contributions={}
    progress_group(state, "all_four_endpoints", "complete_four_endpoint_records", contributions)
    scatter=save_upper(api,contributions,"complete_scattering_endpoint_upper",free_map["KF"]*Cs)
    cross=save_upper(api,contributions,"complete_second_order_endpoint_upper",
                    free_map["K2"]*free_map["Xi2"])
    normalizer=save_upper(api,contributions,"complete_old_waist_normalizer_endpoint_upper",
                         ng*WT*SW)
    mean=save_upper(api,contributions,"complete_physical_mean_endpoint_upper",
                   vz*Z*free_map["Xi23_6"])
    total=save_upper(api,constants,"complete_same_old_trial_waist_endpoint_upper",
                    scatter+cross+normalizer+mean)
    doc={
        "kind":NODE_NAMES[2],"complete":True,
        "same_free_waist_node":NODE_NAMES[1],
        "complete_new_constants":constants,
        "complete_four_endpoint_records":contributions,
        "exact_signed_operator":
          "B_F^V*S_n*(Droot+Jinfinity)*iota_Ai + E2 - ng0*(P*A2*W,0) + v_z*z_end",
        "same_original_old_trial":"Y_W,J at the actual waist including all stored means",
        "scattering_input_matrix_order_retained":True,
        "original_genuine_Cn_and_beta_n_retained":True,
        "root_matrix_not_replaced_by_a_second_independent_column":True,
        "WT_uses_the_whole_saved_forward_strong_remainder":True,
        "no_first_finite_upper_subtracted_from_WT":True,
        "waist_ng_factor_in_WT_SW_product_count":1,
        "physical_mean_vector_exact_identity":"J_w*b2_w=u_w/m_w; v_z=D0_w*(-u_w/m_w,1)",
        "physical_two_stored_means_retained_in_q_term":True,
        "original_root_to_waist_mean_feedback_retained":True,
        "retained_true_finite_complement_and_parameter_rows":True,
        "original_Ni_and_final_waist_readout_not_applied_here":True,
        "complete_physical_whole_error_claimed":False,
        "finite_Schur_or_incoming_inverse_claimed":False,
        "old_successful_quantities_recomputed":0,
    }
    saved=finish_progress(state,doc,publish_graph)
    return decode_four_waist_endpoints_node(api, saved), saved

def decode_waist_reconstruction_node(api, saved):
    """Read only a complete retained node; no new target or record is produced."""
    require(saved.get("kind") == NODE_NAMES[0] and saved.get("complete") is True,
            "complete retained waist reconstruction required")
    require(saved.get("retained_outer_mean_and_terminal") is True and
            saved.get("retained_independent_physical_mean") is True and
            saved.get("metric_radial_derivatives_not_declared_zero") is True,
            "waist reconstruction scope changed")
    return {
        "B": decode_mapping(api, saved["complete_outer_B_polynomial"]),
        "constants": {k: api.read_up(v) for k, v in saved["new_complete_constants"].items()},
        "original_node": NODE_NAMES[0],
    }

def decode_free_waist_map_node(api, saved):
    """Decode all downstream factors from their unchanged saved records."""
    require(saved.get("kind") == NODE_NAMES[1] and saved.get("complete") is True and
            saved.get("same_reconstruction_node") == NODE_NAMES[0],
            "complete retained free waist map required")
    require(saved.get("original_root_matrix_not_treated_as_column_HS_error") is True and
            saved.get("all_low_outputs_means_and_two_physical_rows_retained") is True,
            "free waist map scope changed")
    pr=saved["complete_reconstruction_and_map_records"]
    tr=saved["complete_tail_weights"]["new_complete_records"]
    return {
        "KF":api.read_up(pr["complete_free_map_L2_to_density_upper"]),
        "K2":api.read_up(pr["complete_first_cancellation_column_upper"]),
        "Cpre":api.read_up(pr["complete_common_column_remainder_upper"]),
        "Xi2":api.read_up(tr["complete_Xi2_upper"]),
        "Xi23_6":api.read_up(tr["complete_Xi23_6_upper"]),
        "pi_upper":api.read_up(saved["complete_real_Airy_constants"]["complete_pi_upper"]),
        "original_node":NODE_NAMES[1],
    }

def decode_four_waist_endpoints_node(api, saved):
    """Retain the full four-endpoint result without a whole-error claim."""
    require(saved.get("kind") == NODE_NAMES[2] and saved.get("complete") is True and
            saved.get("same_free_waist_node") == NODE_NAMES[1],
            "complete retained four-endpoint result required")
    require(saved.get("original_root_to_waist_mean_feedback_retained") is True and
            saved.get("complete_physical_whole_error_claimed") is False and
            saved.get("finite_Schur_or_incoming_inverse_claimed") is False,
            "four-endpoint scope changed")
    return {
       "Cend":api.read_up(saved["complete_new_constants"][
                         "complete_same_old_trial_waist_endpoint_upper"]),
       "original_node":NODE_NAMES[2],
    }
