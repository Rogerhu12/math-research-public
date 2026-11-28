#!/usr/bin/env node
// Complete source-only derivation. No Python import, AST, field, root or fixture.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const SPEC = [
  {
    "complete_parent": {
      "name": "supported_smooth_triangle_seed_mean_jets.py",
      "path": "scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py",
      "bytes": 34725,
      "sha256": "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917",
      "git_blob_sha": "ee318b8971ce3c3d10715fbcd648c3a3bcfd6712"
    },
    "complete_output": {
      "name": "fixed_fejer_R726_spherical_seed_mean_jets.py",
      "path": "scripts/resume_20261126/fixed_fejer_R726_spherical_seed_mean_jets.py",
      "bytes": 48226,
      "sha256": "2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23",
      "git_blob_sha": "9f7ea1805326a317a281e8c3f6c7cb6ef9709890"
    },
    "complete_reversible_text_patches": [
      {
        "label": "independent mean schema",
        "before": "SCHEMA = \"complete-supported-smooth-triangle-seed-working-newton-mean-and-angular-jets-v1\"",
        "after": "SCHEMA = \"complete-R726-spherical-boundary-paired-halfwave-seed-working-mean-and-angular-jets-v1\""
      },
      {
        "label": "actual boundary equation",
        "before": "    \"central_length*v + integral_boundary N((1-chi)*T0+chi*N(v)) - K = 0\",",
        "after": "    \"central_length*v + integral_boundary S_chi(N(T0),N(v)) - K = 0\","
      },
      {
        "label": "module mathematical scope",
        "before": "All returned values are working binary64 data.  No continuous contraction,\nquadrature, rounding, branch, geometry, or metric certificate is asserted.\n",
        "after": "The boundary is the independent R726 shortest spherical interpolation with\ncomplete zero-angle working coefficients and their own derivatives.  The full\nthree-coordinate Newton, Armijo, R711 auxiliary twelve-piece amplitude solve,\nprojected frame and both angular orders remain.  No old Euclidean mean root,\nR709 ball potential or R722 posterior formula is inherited.\n\nAll returned values are working binary64 data.  Conditional R726 acute-domain\nexistence/uniqueness, quadrature, rounding, branch, geometry and metric bounds\nare not certified by this numerical kernel.\n"
      },
      {
        "label": "full spherical kernel",
        "before": "\ndef smooth_triangle_value_and_derivative(t, profile_delta):",
        "after": "\nSPHERICAL_BOUNDARY_SCHEMA = \"complete-R726-spherical-boundary-working-value-and-angular-jets-v1\"\nSPHERICAL_SMALL_Q_MAX = 0.25\nSPHERICAL_SERIES_DEGREE = 32\nR726_PROOF_SHA256 = \"faa3e44cf1392e6f7e1fb4e04adb039afc54ac881ef3f99b0b4ca9810d9e226b\"\n\n\ndef spherical_boundary_definition():\n    \"\"\"Complete declared formulas; this function evaluates no field or root.\"\"\"\n    return dict(\n        schema=SPHERICAL_BOUNDARY_SCHEMA,\n        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),\n        theorem_source_sha256=R726_PROOF_SHA256,\n        accurate_boundary=\"S_chi(N(x),N(y)); S=sin((1-chi)*theta)/sin(theta)*u+sin(chi*theta)/sin(theta)*d\",\n        accurate_zero_angle=\"the analytic extension at u=d, with value u\",\n        accurate_domain=\"nonzero x,y and N(x) != -N(y); acute-root theorems have additional hypotheses\",\n        accurate_normal_extension=\"normalize both arguments; output normalization is the identity in exact Slerp arithmetic\",\n        working_coordinate=\"q=sum((N(x)-N(y))**2)/2; no clipping of q or dot products\",\n        working_output=\"N(f_(1-chi)(q)*N(x)+f_chi(q)*N(y))\",\n        working_small_q_interval=[0.0, SPHERICAL_SMALL_Q_MAX],\n        working_small_q_degree=SPHERICAL_SERIES_DEGREE,\n        working_coefficient_recurrence=\"c0=a; c[n+1]=(((n+1)**2-a*a)/((n+1)*(2*n+3)))*c[n]\",\n        working_q_derivatives=\"first and second simultaneous Horner derivatives of the same actual coefficient array\",\n        working_a_derivative=\"differentiate the same coefficient recurrence; never substitute a separately rounded derivative table\",\n        working_large_q=\"theta=acos(1-q); f=sin(a*theta)/sin(theta); explicit first/second chain derivatives\",\n        working_coefficient_endpoints=\"a=0 or1 uses the exact constant coefficient value and zero q derivatives; a derivative is retained\",\n        input_normalizations_and_output_normalization_differentiated=True,\n        small_series_truncation_is_not_an_exact_Slerp_identity=True,\n        branch_switch_is_not_claimed_exact_C2_in_working_arithmetic=True,\n        coefficient_rounding_trigonometric_quadrature_root_and_jet_errors_enclosed=False,\n        degree32_exact_coefficient_tail_bounds_at_q_quarter=dict(\n            value_strictly_below=\"2^-98\", q_first_strictly_below=\"2^-91\",\n            q_second_strictly_below=\"2^-84\", a_first_strictly_below=\"2^-96\",\n            scope=\"only infinite-series truncation in exact arithmetic; not floating-point or full-field error\"),\n        R709_Euclidean_potential_or_R722_posterior_formula_inherited=False,\n        R726_acute_existence_or_global_branch_verified=False,\n        working_antipodal_or_nonfinite_pairs_unavailable=True,\n        all_original_boundary_nodes_weights_and_two_angular_orders_retained=True)\n\n\ndef _spherical_coefficients(a, q):\n    \"\"\"Value and true branch derivatives (q,q,a) of the declared working formula.\n\n    The zero-angle branch never evaluates acos, sqrt(q), or division by sin(0).\n    q derivatives differentiate the same coefficient values through Horner.\n    The a derivative differentiates their actual recurrence, not another table.\n    Invalid pairs stay NaN and are rejected by the full caller.\n    \"\"\"\n    a = np.asarray(a, dtype=np.float64)\n    if q.ndim != 2 or a.shape != (q.shape[0], 1):\n        raise ValueError(\"Use one complete radial cutoff coefficient per row\")\n    outputs = [np.full(q.shape, np.nan, dtype=np.float64) for _ in range(4)]\n    value, first, second, a_first = outputs\n    valid = np.isfinite(q) & (q >= 0.0) & (q < 2.0) & np.isfinite(a) & (a >= 0.0) & (a <= 1.0)\n    small = valid & (q <= SPHERICAL_SMALL_Q_MAX)\n    if np.any(small):\n        rows, _ = np.nonzero(small)\n        aa, qq = a[:, 0], q[small]\n        # Coefficients depend only on the radial cutoff, not on the angle.\n        # Keep 33 arrays of P entries, not 33 copies of the full P-by-A grid.\n        c, ca = aa.copy(), np.ones_like(aa)\n        coefficients, a_derivatives = [c], [ca]\n        for n in range(SPHERICAL_SERIES_DEGREE):\n            k = n+1\n            denominator = float(k*(2*k+1))\n            ratio = (float(k*k)-aa*aa)/denominator\n            next_c = ratio*c\n            next_ca = ratio*ca-(2.0*aa/denominator)*c\n            c, ca = next_c, next_ca\n            coefficients.append(c)\n            a_derivatives.append(ca)\n        p, p1, p2 = coefficients[-1][rows].copy(), np.zeros_like(qq), np.zeros_like(qq)\n        pa = a_derivatives[-1][rows].copy()\n        for n in range(SPHERICAL_SERIES_DEGREE-1, -1, -1):\n            # Simultaneous RHS evaluation retains the complete first/second chain.\n            p2, p1, p = p2*qq+2.0*p1, p1*qq+p, p*qq+coefficients[n][rows]\n            pa = pa*qq+a_derivatives[n][rows]\n        value[small], first[small], second[small], a_first[small] = p, p1, p2, pa\n    large = valid & ~small\n    if np.any(large):\n        rows, _ = np.nonzero(large)\n        aa, qq = a[rows, 0], q[large]\n        z = 1.0-qq\n        theta = np.arccos(z)\n        sine, cosine = np.sin(theta), np.cos(theta)\n        argument = aa*theta\n        sn, co = np.sin(argument), np.cos(argument)\n        theta_q = 1.0/np.sqrt(1.0-z*z)\n        theta_qq = -z*theta_q*theta_q*theta_q\n        f = sn/sine\n        f_theta = aa*co/sine-sn*cosine/(sine*sine)\n        f_thetatheta = ((1.0-aa*aa)*sn/sine\n                       -2.0*aa*co*cosine/(sine*sine)\n                       +2.0*sn*cosine*cosine/(sine*sine*sine))\n        value[large] = f\n        first[large] = f_theta*theta_q\n        second[large] = f_thetatheta*theta_q*theta_q+f_theta*theta_qq\n        a_first[large] = theta*co/sine\n    # These are exact coefficient identities, not a clamp of the angle.\n    zero, one = valid & (a == 0.0), valid & (a == 1.0)\n    value[zero], first[zero], second[zero] = 0.0, 0.0, 0.0\n    value[one], first[one], second[one] = 1.0, 0.0, 0.0\n    return tuple(outputs)\n\n\ndef _spherical_state(T0, v, chi, *, phase, metadata, strict=True):\n    \"\"\"One full radial-by-angle value graph, shared by mean/J/angle/radial jets.\"\"\"\n    with np.errstate(over=\"ignore\", invalid=\"ignore\", divide=\"ignore\"):\n        xn = np.linalg.norm(T0, axis=-1)\n        yn = np.linalg.norm(v, axis=-1)\n        u, d = T0/xn[..., None], v/yn[..., None]\n        eye = np.eye(3, dtype=np.float64)\n        Dx = (eye-u[..., :, None]*u[..., None, :])/xn[..., None, None]\n        Dv = (eye-d[..., :, None]*d[..., None, :])/yn[..., None, None]\n        difference = u-d[None, :, :]\n        q = 0.5*np.sum(difference*difference, axis=-1)\n        A, Aq, Aqq, Aa = _spherical_coefficients(1.0-chi[:, None], q)\n        B, Bq, Bqq, Ba = _spherical_coefficients(chi[:, None], q)\n        R = A[..., None]*u+B[..., None]*d[None, :, :]\n        Rnorm = np.linalg.norm(R, axis=-1)\n        value = R/Rnorm[..., None]\n        DR = (eye-value[..., :, None]*value[..., None, :])/Rnorm[..., None, None]\n        available = (np.isfinite(xn) & (xn > 0.0)\n                     & np.isfinite(yn)[None, :] & (yn > 0.0)[None, :]\n                     & np.all(np.isfinite(T0), axis=-1)\n                     & np.all(np.isfinite(v), axis=-1)[None, :]\n                     & np.isfinite(q) & (q >= 0.0) & (q < 2.0)\n                     & np.all(np.isfinite(u+d[None, :, :]), axis=-1)\n                     & (np.linalg.norm(u+d[None, :, :], axis=-1) > 0.0)\n                     & np.isfinite(Rnorm) & (Rnorm > 0.0)\n                     & np.all(np.isfinite(value), axis=-1))\n    if strict and not np.all(available):\n        sites = np.argwhere(~available)\n        _fail(phase, \"Some complete spherical boundary pairs are unavailable\",\n              indices=np.unique(sites[:, 1]),\n              carriers={\"reference\": T0, \"v\": v, \"chi\": chi, \"spherical_q\": q,\n                        \"reference_norm\": xn, \"mean_radius\": yn, \"output_norm\": Rnorm},\n              metadata={**metadata, \"actual_failed_spherical_pair_indices\": sites.tolist(),\n                        \"no_antipodal_angle_or_input_norm_clipping\": True})\n    return dict(u=u, d=d, reference_norm=xn, mean_radius=yn,\n                reference_derivative=Dx, mean_derivative=Dv,\n                difference=difference, q=q, A=A, Aq=Aq, Aqq=Aqq, Aa=Aa,\n                B=B, Bq=Bq, Bqq=Bqq, Ba=Ba, value=value,\n                output_norm=Rnorm, output_derivative=DR, available=available)\n\n\ndef _spherical_y_jacobian(state):\n    \"\"\"Full derivative with respect to all three raw mean coordinates.\"\"\"\n    u, d = state[\"u\"], state[\"d\"][None, :, :]\n    C = state[\"Aq\"][..., None]*u+state[\"Bq\"][..., None]*d\n    middle = (state[\"B\"][..., None, None]*np.eye(3)\n              -C[..., :, None]*state[\"difference\"][..., None, :])\n    return np.einsum(\"paij,pajk,akl->pail\",\n                     state[\"output_derivative\"], middle, state[\"mean_derivative\"])\n\n\ndef _spherical_angle_jets(state, T1, T2, v1, v2):\n    \"\"\"Total two-angle chain including both normalizations and all mixed terms.\"\"\"\n    u, d = state[\"u\"], state[\"d\"][None, :, :]\n    u1 = _apply(state[\"reference_derivative\"], T1)\n    u2 = (_apply(state[\"reference_derivative\"], T2)\n          +_D2N_same(state[\"u\"], state[\"reference_norm\"], T1))\n    d1 = _apply(state[\"mean_derivative\"], v1)[None, :, :]\n    d2 = (_apply(state[\"mean_derivative\"], v2)\n          +_D2N_same(state[\"d\"], state[\"mean_radius\"], v1))[None, :, :]\n    e1 = u1-d1\n    q1 = np.sum(state[\"difference\"]*e1, axis=-1)\n    q2 = (np.sum(e1*e1, axis=-1)\n          +np.sum(state[\"difference\"]*(u2-d2), axis=-1))\n    C = state[\"Aq\"][..., None]*u+state[\"Bq\"][..., None]*d\n    R1 = (state[\"A\"][..., None]*u1+state[\"B\"][..., None]*d1+q1[..., None]*C)\n    R2 = (state[\"A\"][..., None]*u2+state[\"B\"][..., None]*d2\n          +2.0*q1[..., None]*(state[\"Aq\"][..., None]*u1+state[\"Bq\"][..., None]*d1)\n          +q2[..., None]*C\n          +(q1*q1)[..., None]*(state[\"Aqq\"][..., None]*u+state[\"Bqq\"][..., None]*d))\n    first = _apply(state[\"output_derivative\"], R1)\n    second = (_apply(state[\"output_derivative\"], R2)\n              +_D2N_same(state[\"value\"], state[\"output_norm\"], R1))\n    return first, second\n\n\ndef _spherical_radial_jet(state, Ts, chi_s):\n    \"\"\"Complete s derivative: reference turn plus cutoff turn; mean v is fixed.\"\"\"\n    us = _apply(state[\"reference_derivative\"], Ts)\n    qs = np.sum(state[\"difference\"]*us, axis=-1)\n    As = state[\"Aq\"]*qs-state[\"Aa\"]*chi_s[:, None]\n    Bs = state[\"Bq\"]*qs+state[\"Ba\"]*chi_s[:, None]\n    Rs = (state[\"A\"][..., None]*us+As[..., None]*state[\"u\"]\n          +Bs[..., None]*state[\"d\"][None, :, :])\n    return _apply(state[\"output_derivative\"], Rs)\n\n\ndef spherical_boundary_jets(T0, T1, T2, v, v1, v2, chi, *, Ts, chi_s):\n    \"\"\"Actual fixed-seed field interface; same raw v graph as the mean equation.\"\"\"\n    _require_public_actions()\n    values = {name: _real_array(name, value) for name, value in (\n        (\"T0\", T0), (\"T1\", T1), (\"T2\", T2), (\"v\", v), (\"v1\", v1),\n        (\"v2\", v2), (\"chi\", chi), (\"Ts\", Ts), (\"chi_s\", chi_s))}\n    T0, T1, T2, Ts = (values[k] for k in (\"T0\", \"T1\", \"T2\", \"Ts\"))\n    v, v1, v2 = (values[k] for k in (\"v\", \"v1\", \"v2\"))\n    chi, chi_s = values[\"chi\"], values[\"chi_s\"]\n    if (T0.ndim != 3 or T0.shape[-1] != 3 or min(T0.shape[:2]) < 1\n            or T1.shape != T0.shape or T2.shape != T0.shape or Ts.shape != T0.shape\n            or v.shape != T0.shape[1:] or v1.shape != v.shape or v2.shape != v.shape\n            or chi.shape != (T0.shape[0],) or chi_s.shape != chi.shape\n            or not np.all((chi >= 0.0) & (chi <= 1.0))):\n        _fail(\"spherical_field_input\", \"Retain the complete radial/angle arrays and cutoff domain\")\n    metadata = dict(spherical_boundary=spherical_boundary_definition())\n    try:\n        with np.errstate(over=\"raise\", invalid=\"raise\", divide=\"raise\"):\n            state = _spherical_state(T0, v, chi, phase=\"spherical_field_value\", metadata=metadata)\n            first, second = _spherical_angle_jets(state, T1, T2, v1, v2)\n            radial = _spherical_radial_jet(state, Ts, chi_s)\n    except SeedMeanFailure:\n        raise\n    except (FloatingPointError, OverflowError, ValueError, np.linalg.LinAlgError) as error:\n        _fail(\"spherical_field_jets\", \"Actual complete spherical derivative arithmetic failed: \"+str(error),\n              carriers=values, metadata=metadata)\n    answer = dict(T0=state[\"value\"], T0_phi=first, T0_phiphi=second, T0_s=radial)\n    if not all(np.all(np.isfinite(a)) for a in answer.values()):\n        _fail(\"spherical_field_jets\", \"A complete spherical field jet is nonfinite\",\n              carriers=answer, metadata=metadata)\n    for a in answer.values():\n        a.setflags(write=False)\n    return answer\n\n\ndef smooth_triangle_value_and_derivative(t, profile_delta):"
      },
      {
        "label": "trial evaluates every actual spherical angle",
        "before": "def _trial_mean_residual(trial, indices, K0, T0, chi, weights, Lc, counts):\n    \"\"\"Read every proposed angle; unavailable domains remain rejected, not filled.\"\"\"\n    number = len(indices)\n    residual = np.full((number, 3), np.nan, dtype=np.float64)\n    available = np.zeros(number, dtype=bool)\n    counts[\"mean_batches\"] += 1\n    counts[\"mean_trial_batches\"] += 1\n    counts[\"mean_trial_angle_attempts\"] += number\n    # Nonfinite trial arithmetic is recorded as unavailable.  It is never used\n    # in an acceptance comparison or substituted with a finite field value.\n    with np.errstate(over=\"ignore\", invalid=\"ignore\", divide=\"ignore\"):\n        radius = np.linalg.norm(trial, axis=-1)\n        positions = np.flatnonzero(np.isfinite(radius) & (radius > 0.0)\n                                   & np.all(np.isfinite(trial), axis=-1))\n        if len(positions):\n            d = trial[positions]/radius[positions, None]\n            Y = ((1.0-chi)[:, None, None]*T0[:, indices[positions], :]\n                 +chi[:, None, None]*d[None, :, :])\n            ynorm = np.linalg.norm(Y, axis=-1)\n            valid = np.all(np.isfinite(ynorm) & (ynorm > 0.0), axis=0)\n            valid_positions = positions[valid]\n            if len(valid_positions):\n                Tb = Y[:, valid, :]/ynorm[:, valid, None]\n                B = _weighted(weights, Tb)\n                values = Lc*trial[valid_positions]+B-K0[indices[valid_positions]]\n                finite = (np.all(np.isfinite(values), axis=-1)\n                          & np.isfinite(np.linalg.norm(values, axis=-1)))\n                actual_positions = valid_positions[finite]\n                residual[actual_positions] = values[finite]\n                available[actual_positions] = True\n    counts[\"mean_trial_available_angle_evaluations\"] += int(np.count_nonzero(available))\n    counts[\"mean_angle_evaluations\"] += int(np.count_nonzero(available))\n    return available, residual\n",
        "after": "def _trial_mean_residual(trial, indices, K0, T0, chi, weights, Lc, counts):\n    \"\"\"Every proposed angle uses the same full spherical equation and weights.\"\"\"\n    number = len(indices)\n    residual = np.full((number, 3), np.nan, dtype=np.float64)\n    available = np.zeros(number, dtype=bool)\n    counts[\"mean_batches\"] += 1\n    counts[\"mean_trial_batches\"] += 1\n    counts[\"mean_trial_angle_attempts\"] += number\n    # Unavailable normalizations/antipodal pairs and nonfinite arithmetic stay\n    # unavailable. No angle is dropped from the original all-angle Armijo test.\n    with np.errstate(over=\"ignore\", invalid=\"ignore\", divide=\"ignore\"):\n        spherical = _spherical_state(T0[:, indices, :], trial, chi,\n                                     phase=\"mean_trial\", metadata={}, strict=False)\n        B = _weighted(weights, spherical[\"value\"])\n        values = Lc*trial+B-K0[indices]\n        available = (np.all(spherical[\"available\"], axis=0)\n                     & np.all(np.isfinite(values), axis=-1)\n                     & np.isfinite(np.linalg.norm(values, axis=-1)))\n        residual[available] = values[available]\n    counts[\"mean_trial_available_angle_evaluations\"] += int(np.count_nonzero(available))\n    counts[\"mean_angle_evaluations\"] += int(np.count_nonzero(available))\n    return available, residual\n"
      },
      {
        "label": "metadata independent mechanism",
        "before": "        root_equations=list(ROOT_EQUATIONS),\n",
        "after": "        root_equations=list(ROOT_EQUATIONS),\n        spherical_boundary=spherical_boundary_definition(),\n        R709_Euclidean_potential_inherited=False,\n        R722_specialized_posterior_formula_inherited=False,\n        R726_acute_existence_uniqueness_verified=False,\n        working_domain_is_nonantipodal_not_an_acute_proof_gate=True,\n"
      },
      {
        "label": "remove old blend coefficient arrays",
        "before": "    one_minus_chi = (1.0-chi)[:, None, None]\n    chi3 = chi[:, None, None]\n    v = K0/Lc\n",
        "after": "    v = K0/Lc\n"
      },
      {
        "label": "actual current root value",
        "before": "        Y = one_minus_chi*T0 + chi3*d[None, :, :]\n        Tb, Ynorm, DY = _normalization(\n            Y, phase=state[\"phase\"], label=\"boundary_Y\", metadata=metadata)\n        B = _weighted(weights, Tb)\n",
        "after": "        spherical = _spherical_state(T0, v, chi, phase=state[\"phase\"], metadata=metadata)\n        B = _weighted(weights, spherical[\"value\"])\n"
      },
      {
        "label": "full new Jacobian",
        "before": "        # M = integral chi*DN(Y) is symmetric PSD in exact arithmetic;\n        # Jv=Lc*I+M*DN(v) is generally not symmetric.  Solve the complete J.\n        M = np.einsum(\"p,paij->aij\", weights*chi, DY)\n        J_current = Lc*np.eye(3)[None, :, :]+np.einsum(\"aij,ajk->aik\", M, Dv)\n",
        "after": "        # The spherical boundary has a genuinely different full derivative.\n        # Do not substitute the old integral chi*DN(Y) or claim Euclidean PSD.\n        Bv = _weighted(weights, _spherical_y_jacobian(spherical))\n        J_current = Lc*np.eye(3)[None, :, :]+Bv\n"
      },
      {
        "label": "full two angular implicit derivatives",
        "before": "    # All derivatives refer to this same final mean point and the same full rule.\n    state[\"phase\"] = \"mean_first_angular_jet\"\n    Bv = np.einsum(\"p,paij,ajk->aik\", weights*chi, DY, Dv)\n    Jv = Lc*np.eye(3)[None, :, :]+Bv\n    partial_B1 = _weighted(weights, _apply(DY, one_minus_chi*T1))\n    v1 = _checked_solve(Jv, K1-partial_B1, phase=state[\"phase\"],\n                        carriers={\"v\": v}, metadata=metadata, counts=counts)\n    d1 = _apply(Dv, v1)\n    Y1 = one_minus_chi*T1+chi3*d1[None, :, :]\n    Tb1 = _apply(DY, Y1)\n    B1 = _weighted(weights, Tb1)\n    mean_r1 = Lc*v1+B1-K1\n\n    state[\"phase\"] = \"mean_second_angular_jet\"\n    d2_known = _D2N_same(d, radius, v1)\n    Y2_known = one_minus_chi*T2+chi3*d2_known[None, :, :]\n    Tb2_known = _apply(DY, Y2_known)+_D2N_same(Tb, Ynorm, Y1)\n    partial_B2 = _weighted(weights, Tb2_known)\n    v2 = _checked_solve(Jv, K2-partial_B2, phase=state[\"phase\"],\n                        carriers={\"v\": v, \"v_phi\": v1}, metadata=metadata, counts=counts)\n    d2 = _apply(Dv, v2)+d2_known\n    Y2 = one_minus_chi*T2+chi3*d2[None, :, :]\n    Tb2 = _apply(DY, Y2)+_D2N_same(Tb, Ynorm, Y1)\n    B2 = _weighted(weights, Tb2)\n    mean_r2 = Lc*v2+B2-K2\n    metadata.update(\n        maximum_actual_mean_phi_residual=float(np.max(_norms(mean_r1))),\n        maximum_actual_mean_phiphi_residual=float(np.max(_norms(mean_r2))),\n        mean_jacobian_shape=list(Jv.shape),\n        maximum_actual_mean_Jv_infinity_norm=float(np.max(np.sum(np.abs(Jv), axis=-1))),\n        angular_jet_residuals_are_readouts_not_continuous_bounds=True,\n    )\n\n",
        "after": "    # All derivatives refer to this same final mean point and the same full rule.\n    state[\"phase\"] = \"mean_first_angular_jet\"\n    Bv = _weighted(weights, _spherical_y_jacobian(spherical))\n    Jv = Lc*np.eye(3)[None, :, :]+Bv\n    zero_v, zero_T = np.zeros_like(v), np.zeros_like(T0)\n    partial_Tb1, _ = _spherical_angle_jets(spherical, T1, zero_T, zero_v, zero_v)\n    partial_B1 = _weighted(weights, partial_Tb1)\n    v1 = _checked_solve(Jv, K1-partial_B1, phase=state[\"phase\"],\n                        carriers={\"v\": v}, metadata=metadata, counts=counts)\n    d1 = _apply(Dv, v1)\n    # v2=0 leaves every known second-order term: T2, both normalization\n    # accelerations, q1**2, q2 and all reference/mean mixed products.\n    state[\"phase\"] = \"mean_second_angular_jet\"\n    Tb1, Tb2_known = _spherical_angle_jets(spherical, T1, T2, v1, zero_v)\n    B1 = _weighted(weights, Tb1)\n    mean_r1 = Lc*v1+B1-K1\n    partial_B2 = _weighted(weights, Tb2_known)\n    v2 = _checked_solve(Jv, K2-partial_B2, phase=state[\"phase\"],\n                        carriers={\"v\": v, \"v_phi\": v1}, metadata=metadata, counts=counts)\n    d2 = _apply(Dv, v2)+_D2N_same(d, radius, v1)\n    _, Tb2 = _spherical_angle_jets(spherical, T1, T2, v1, v2)\n    B2 = _weighted(weights, Tb2)\n    mean_r2 = Lc*v2+B2-K2\n    metadata.update(\n        maximum_actual_mean_phi_residual=float(np.max(_norms(mean_r1))),\n        maximum_actual_mean_phiphi_residual=float(np.max(_norms(mean_r2))),\n        mean_jacobian_shape=list(Jv.shape),\n        maximum_actual_mean_Jv_infinity_norm=float(np.max(np.sum(np.abs(Jv), axis=-1))),\n        angular_jet_residuals_are_readouts_not_continuous_bounds=True,\n        full_raw_v_chart_is_equivalent_to_R726_alpha_direction_chart_in_exact_arithmetic=True,\n        R726_normal_acceleration_and_reference_mean_mixed_terms_retained=True,\n    )\n\n"
      },
      {
        "label": "actual boundary diagnostics",
        "before": "        actual_boundary_minimum_normalization_norm=float(np.min(Ynorm)),\n",
        "after": "        actual_boundary_minimum_normalization_norm=float(np.min(spherical[\"output_norm\"])),\n        boundary_normalization_norm_scope=\"output of the declared spherical coefficient sum, not the old Euclidean blend Y\",\n        actual_spherical_minimum_reference_norm=float(np.min(spherical[\"reference_norm\"])),\n        actual_spherical_minimum_q=float(np.min(spherical[\"q\"])),\n        actual_spherical_maximum_q=float(np.max(spherical[\"q\"])),\n        actual_spherical_small_series_pair_count=int(np.count_nonzero(spherical[\"q\"] <= SPHERICAL_SMALL_Q_MAX)),\n        actual_spherical_trigonometric_pair_count=int(np.count_nonzero(spherical[\"q\"] > SPHERICAL_SMALL_Q_MAX)),\n        actual_sampled_acute_pairs=bool(np.all(spherical[\"q\"] <= 1.0)),\n        sampled_acute_pairs_are_not_a_whole_domain_or_existence_certificate=True,\n"
      }
    ]
  },
  {
    "complete_parent": {
      "name": "fixed_fejer_paired_halfwave_flat_cutoff_meridian_reference.py",
      "path": "scripts/resume_20261126/fixed_fejer_paired_halfwave_flat_cutoff_meridian_reference.py",
      "bytes": 51540,
      "sha256": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
      "git_blob_sha": "b37f930874dd9b874d58120a2d9fe86031146ccb"
    },
    "complete_output": {
      "name": "fixed_fejer_R726_spherical_halfwave_meridian_reference.py",
      "path": "scripts/resume_20261126/fixed_fejer_R726_spherical_halfwave_meridian_reference.py",
      "bytes": 52457,
      "sha256": "176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a",
      "git_blob_sha": "231bad2fba5f80ade672703114fe5bd776512baf"
    },
    "complete_reversible_text_patches": [
      {
        "label": "real independent mechanism description",
        "before": "The exact definition retains the R708/R709 normalized boundary mean and the R711\nscalar amplitude, with the same opposite paired halfwaves. Only the boundary\ncutoff is changed to the complete fixed-epsilon R725 three-piece C3 law.\n",
        "after": "The exact boundary is the independent R726 shortest spherical interpolation.\nIts complete three-coordinate mean and both angular jets are solved again from\nthat actual boundary function. The R711 scalar amplitude, opposite R724 paired\nhalfwaves, and complete fixed-epsilon R725 three-piece C3 cutoff are retained.\nOld Euclidean boundary roots, R709 ball potentials and R722 posterior formulas\nare not inherited; R726 existence and uniqueness remain conditional until paid.\n"
      },
      {
        "label": "new seed schema",
        "before": "SCHEMA = \"complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1\"",
        "after": "SCHEMA = \"complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1\""
      },
      {
        "label": "new complete mean schema",
        "before": "MEAN_KERNEL_SCHEMA = \"complete-supported-smooth-triangle-seed-working-newton-mean-and-angular-jets-v1\"",
        "after": "MEAN_KERNEL_SCHEMA = \"complete-R726-spherical-boundary-paired-halfwave-seed-working-mean-and-angular-jets-v1\""
      },
      {
        "label": "new complete mean source",
        "before": "MEAN_KERNEL_SHA = \"f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917\"",
        "after": "MEAN_KERNEL_SHA = \"2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23\""
      },
      {
        "label": "whole new field kernel binding",
        "before": "                or sha(mean_kernel_module.smooth_triangle_value_and_derivative.__code__.co_filename) != MEAN_KERNEL_SHA):",
        "after": "                or sha(mean_kernel_module.smooth_triangle_value_and_derivative.__code__.co_filename) != MEAN_KERNEL_SHA\n                or sha(mean_kernel_module.spherical_boundary_jets.__code__.co_filename) != MEAN_KERNEL_SHA\n                or sha(mean_kernel_module.spherical_boundary_definition.__code__.co_filename) != MEAN_KERNEL_SHA):"
      },
      {
        "label": "same value and derivatives definition",
        "before": "        self.boundary_cutoff_definition = boundary_cutoff_definition(support, central)\n",
        "after": "        self.boundary_cutoff_definition = boundary_cutoff_definition(support, central)\n        self.spherical_boundary_definition = mean_kernel_module.spherical_boundary_definition()\n"
      },
      {
        "label": "working method explicit source and scope",
        "before": "            schema=\"paired-halfwave-flat-cutoff-reference-working-definition-v1\",",
        "after": "            schema=\"R726-spherical-boundary-paired-halfwave-reference-working-definition-v1\",\n            spherical_boundary_definition=self.spherical_boundary_definition,\n            mean_and_field_use_same_raw_v_and_full_two_angular_jet_graph=True,\n            old_R709_potential_or_R722_posterior_formula_inherited=False,\n            R726_acute_domain_and_existence_hypotheses_certified=False,"
      },
      {
        "label": "accurate field formula",
        "before": "            accurate_definition=\"fixed original unit T0 outside U; N((1-chi)T0+chi*d) on boundary layers; cos(lambda*h_delta(t/2))*d+sign[index]*sin(lambda*h_delta(t/2))*w on the two equal central intervals\",",
        "after": "            accurate_definition=\"fixed original unit T0 outside U; R726 S_chi(T0,d) on all boundary layers; cos(lambda*h_delta(t/2))*d+sign[index]*sin(lambda*h_delta(t/2))*w on the two equal central intervals\",\n            spherical_boundary_definition=self.spherical_boundary_definition,"
      },
      {
        "label": "accurate mean formula",
        "before": "            accurate_mean_definition=\"Lc*v+B(N(v))=P_original-Gamma_original-integral_complement_U T0; a_delta(lambda)=norm(v)\",",
        "after": "            accurate_mean_definition=\"Lc*v+integral_E S_chi(T0,N(v))=P_original-Gamma_original-integral_complement_U T0; a_delta(lambda)=norm(v)\","
      },
      {
        "label": "new actual radial plan source label",
        "before": "        record = dict(schema=\"complete-paired-halfwave-flat-cutoff-seed-radial-plan-v1\",",
        "after": "        record = dict(schema=\"complete-R726-spherical-boundary-paired-halfwave-seed-radial-plan-v1\","
      },
      {
        "label": "mean cache exposes already retained complete v jets",
        "before": "                for name in (\"d\", \"d_phi\", \"d_phiphi\", \"w\", \"w_phi\", \"w_phiphi\",\n                             \"lambda\", \"lambda_phi\", \"lambda_phiphi\")}",
        "after": "                for name in (\"v\", \"v_phi\", \"v_phiphi\", \"d\", \"d_phi\", \"d_phiphi\",\n                             \"w\", \"w_phi\", \"w_phiphi\", \"lambda\", \"lambda_phi\", \"lambda_phiphi\")}"
      },
      {
        "label": "actual complete spherical boundary value/s/phi/phiphi",
        "before": "        if np.any(boundary):\n            chi = radial[\"chi\"][boundary, None, None]\n            chis = radial[\"chi_s\"][boundary, None, None]\n            Y = (1.-chi)*T[boundary]+chi*d\n            Yp = (1.-chi)*Tp[boundary]+chi*dp\n            Ypp = (1.-chi)*Tpp[boundary]+chi*dpp\n            Ys = (1.-chi)*Ts[boundary]+chis*(d-T[boundary])\n            norm = np.linalg.norm(Y, axis=-1)\n            if not np.isfinite(norm).all() or np.any(norm <= 0):\n                self._fail(\"boundary_normalization\", \"A requested complete boundary blend is zero or nonfinite\",\n                    literal_angle_hex=[float(v).hex() for v in phi])\n            unit = Y/norm[..., None]\n            rp = np.sum(unit*Yp, axis=-1)\n            rpp = (np.sum(Yp*Yp+Y*Ypp, axis=-1)-rp*rp)/norm\n            up = (Yp-unit*rp[..., None])/norm[..., None]\n            upp = (Ypp-unit*rpp[..., None]-2.*up*rp[..., None])/norm[..., None]\n            us = (Ys-unit*np.sum(unit*Ys, axis=-1)[..., None])/norm[..., None]\n            T[boundary], Tp[boundary], Tpp[boundary], Ts[boundary] = unit, up, upp, us\n",
        "after": "        if np.any(boundary):\n            try:\n                actual = self.kernel.spherical_boundary_jets(\n                    T[boundary], Tp[boundary], Tpp[boundary],\n                    mean[\"v\"], mean[\"v_phi\"], mean[\"v_phiphi\"],\n                    radial[\"chi\"][boundary], Ts=Ts[boundary],\n                    chi_s=radial[\"chi_s\"][boundary])\n            except self.kernel.SeedMeanFailure as error:\n                self._fail(\"spherical_boundary_jets\", str(error),\n                    literal_angle_hex=[float(v).hex() for v in phi],\n                    full_working_failure=error.record)\n            T[boundary], Tp[boundary], Tpp[boundary], Ts[boundary] = (\n                actual[\"T0\"], actual[\"T0_phi\"], actual[\"T0_phiphi\"], actual[\"T0_s\"])\n"
      },
      {
        "label": "field metadata explicit new proof boundary",
        "before": "                accurate_mean_root_and_continuous_geometry_certified=False,\n",
        "after": "                accurate_mean_root_and_continuous_geometry_certified=False,\n                spherical_boundary_source_sha256=MEAN_KERNEL_SHA,\n                R726_acute_domain_existence_or_global_branch_verified=False,\n                old_R709_or_R722_mean_certificate_inherited=False,\n"
      }
    ]
  }
];
const identity = b => ({bytes:b.byteLength,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function same(record,b,label) {
  const got=identity(b);
  if(got.bytes!==record.bytes || got.sha256!==record.sha256)
    throw new Error(label+' complete bytes differ: '+JSON.stringify(got));
}
function once(source,before,after,label) {
  if(typeof before!=='string'||!before.length)throw new Error('Empty text anchor '+label);
  const at=source.indexOf(before);
  if(at<0 || source.indexOf(before,at+before.length)>=0)throw new Error('Not one whole literal anchor: '+label);
  return source.slice(0,at)+after+source.slice(at+before.length);
}
function argumentsOnly() {
  const value={};
  for(let i=2;i<process.argv.length;i+=2) {
    const name=process.argv[i], v=process.argv[i+1];
    if(!['--source-directory','--generated-directory'].includes(name)||!v||value[name]!==undefined)
      throw new Error('Use exactly --source-directory DIR --generated-directory DIR');
    value[name]=v;
  }
  if(Object.keys(value).length!==2)throw new Error('Both complete source and independent output directories are required');
  const parent=path.resolve(value['--source-directory']),out=path.resolve(value['--generated-directory']);
  if(parent===out)throw new Error('Use an independent generated source directory');
  return {parent,out};
}
const {parent,out}=argumentsOnly(), records=[];
fs.mkdirSync(out,{recursive:true});
for(const spec of SPEC) {
  const sourcePath=path.join(parent,spec.complete_parent.name);
  const original=fs.readFileSync(sourcePath);
  same(spec.complete_parent,original,'Parent '+sourcePath);
  const originalText=original.toString('utf8');
  if(!Buffer.from(originalText,'utf8').equals(original))throw new Error('Parent is not complete lossless UTF-8');
  let generated=originalText;
  for(const p of spec.complete_reversible_text_patches)generated=once(generated,p.before,p.after,p.label);
  const bytes=Buffer.from(generated,'utf8');
  same(spec.complete_output,bytes,'Generated '+spec.complete_output.name);
  let inverse=generated;
  for(const p of [...spec.complete_reversible_text_patches].reverse())inverse=once(inverse,p.after,p.before,'inverse '+p.label);
  if(inverse!==originalText)throw new Error('Whole inverse does not reproduce the complete parent');
  const destination=path.join(out,spec.complete_output.name);
  if(fs.existsSync(destination)) {
    if(!fs.readFileSync(destination).equals(bytes))throw new Error('Different existing output; do not overwrite '+destination);
  } else fs.writeFileSync(destination,bytes,{flag:'wx'});
  records.push({path:destination,...spec.complete_output,source_path:sourcePath,
    complete_parent:spec.complete_parent,text_patch_count:spec.complete_reversible_text_patches.length,
    whole_inverse_equal:true});
}
process.stdout.write(JSON.stringify({schema:'complete-R726-spherical-seed-source-text-reproduction-v1',
  complete:true,scope:'source bytes only',outputs:records,
  python_import:false,AST_or_compile:false,fixture:false,scientific_field_or_root_evaluation:false,
  accurate_certificate_claimed:false})+'\n');
