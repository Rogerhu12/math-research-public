#!/usr/bin/env node
/* Complete original-parent text derivation. No scientific evaluation or Python
 * import/AST/compile; this source is not a scientific admission gate. */
import fs from "node:fs";
import path from "node:path";
import {createHash} from "node:crypto";
const SCHEMA="complete-R730-base-Q-calibration-text-reproducer-v1";
const COMPLETE_JOBS=[
  {
    "role": "meridian",
    "parent": {
      "role": "meridian",
      "name": "fixed_fejer_r728_meridian_operator.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r728_meridian_operator.py",
      "bytes": 40877,
      "sha256": "427227b006741b809fc728d4c4d23fe7fa59f2ccbf5e020e15fc8ed0b730168c",
      "git_blob_sha": "46c5227c3a839aa14695c75f4699b98478bf3cb1"
    },
    "output": {
      "name": "fixed_fejer_r730_meridian_operator.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r730_meridian_operator.py",
      "bytes": 40854,
      "sha256": "b9c787340021b5736f2796f2b84a1c25cb4b0ce96333eb98f543b1e8923ce267",
      "git_blob_sha": "9dc7e423afe81a5f115f2dd60ad97fdff86d79a0",
      "role": "complete R730 base with original full outer field and norm body"
    },
    "edits": [
      {
        "old": "T0 is the explicitly bound paired-halfwave seed, frozen from that",
        "new": "T0 is the explicitly bound R730 safe-cone arclength seed, frozen from that",
        "count": 1
      },
      {
        "old": "complete-fixed-fejer-r728-so3-meridian-with-core-lift-v1",
        "new": "complete-fixed-fejer-r730-so3-meridian-with-core-lift-v1",
        "count": 1
      },
      {
        "old": "c6fc04db9223981e1829620613c71de4c0bec93813ec0eeaf5f8ef7770217e86",
        "new": "53ebce095394a833d95a65b834ae889b4cb9554e06ef839fcb626bddcb8864b8",
        "count": 1
      },
      {
        "old": "                 seed_parameters=None, seed_mean_kernel_module=None):",
        "new": "                 length_parameters=None, length_kernel_module=None):",
        "count": 1
      },
      {
        "old": "Bind the complete fixed paired-halfwave world-meridian reference kernel",
        "new": "Bind the complete fixed R730 safe-cone world-meridian reference kernel",
        "count": 1
      },
      {
        "old": "self.parent_jet = parent_jet_module.SupportedUnitMeridianJet(parent_problem,",
        "new": "self.parent_jet = parent_jet_module.SafeConeUnitMeridianJet(parent_problem,",
        "count": 1
      },
      {
        "old": "            seed_parameters=seed_parameters, mean_kernel_module=seed_mean_kernel_module,",
        "new": "            length_parameters=length_parameters, length_kernel_module=length_kernel_module,",
        "count": 1
      },
      {
        "old": "complete-fixed-fejer-R728-reversed-spherical-boundary-paired-halfwave-meridian-seed-reference-v1",
        "new": "complete-fixed-fejer-R730-safe-cone-arclength-reference-v1",
        "count": 1
      },
      {
        "old": "This entry uses a complete explicitly bound fixed paired-halfwave seed",
        "new": "This entry uses the complete explicitly bound R730 scalar-length and inverse-arclength seed",
        "count": 1
      },
      {
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed",
        "count": 7
      },
      {
        "old": "fixed_safe_cone_unit_seed_mean_kernel_sha256=self.parent_jet.model['mean_kernel_source_sha256']",
        "new": "fixed_safe_cone_unit_seed_length_kernel_sha256=self.parent_jet.model['length_kernel_source_sha256']",
        "count": 1
      },
      {
        "old": "T0='complete fixed R728 reversed spherical-boundary seed from original reference core/H; full complement, R725 epsilon=1/8 three-piece C3 cutoff and equal six-piece central halfwaves with source-fixed signs [-1,+1]'",
        "new": "T0='complete fixed R730 six-control safe-cone primitive with eta=1/32 and one (1-(2*t-1)^12)^7 contraction pulse; unique scalar length root and complete inverse arclength; original frozen core/H'",
        "count": 1
      },
      {
        "old": "seed_mean_Jacobian_not_a_certificate_for_current_closure_control_Jacobian=True",
        "new": "seed_length_inverse_not_a_certificate_for_current_closure_control_Jacobian=True",
        "count": 1
      }
    ],
    "edit_kind": "all-exact-count"
  },
  {
    "role": "new_moment_input",
    "parent": {
      "role": "new_moment_input",
      "name": "fixed_fejer_r728_literal_zero_moment_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r728_literal_zero_moment_input.py",
      "bytes": 44554,
      "sha256": "872dca4cf1e15c419aad68d31c053fc4f3465357a3e162413a19002f5b70e43d",
      "git_blob_sha": "d5d088cc53d7450fd90c8944de731e21a4e30917"
    },
    "output": {
      "name": "fixed_fejer_r730_literal_zero_moment_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r730_literal_zero_moment_input.py",
      "bytes": 37575,
      "sha256": "4e72d300388372ae9fa43ba1795be9ad3ed17805a45fd0c407c4f16ed4aa4d1b",
      "git_blob_sha": "4d71d70d17976721e76d65045acd88e80bd9e284",
      "role": "complete pure literal18 Q binding to true R730 length model"
    },
    "edits": [
      {
        "index": 8070,
        "old": "def _positive_exact_fraction(value, name):\n    if not isinstance(value, str):\n        raise ValueError('Keep an exact canonical Fraction string for '+name)\n    try:\n        number = Fraction(value)\n    except (ValueError, ZeroDivisionError) as error:\n        raise ValueError('Invalid exact Fraction for '+name) from error\n    if number <= 0 or str(number) != value:\n        raise ValueError('Keep a positive canonical exact Fraction for '+name)\n    return number\n\n\ndef _paired_halfwave_definition(central, profile_delta):\n    \"\"\"Exact R728 reversed profile; no numerical mean or field evaluation.\"\"\"\n    if type(PHYSICAL_CENTRAL_POLARITY) is not int or PHYSICAL_CENTRAL_POLARITY != -1:\n        raise ValueError(\"This complete source fixes the whole paired-halfwave polarity at -1\")\n    central = tuple(tuple(Fraction(v) for v in pair) for pair in central)\n    delta = Fraction(profile_delta)\n    if (len(central) != 2 or any(len(pair) != 2 for pair in central)\n            or not Fraction(0) < delta < Fraction(1, 8)\n            or not Fraction(0) < central[0][1]-central[0][0]\n            or central[0][1]-central[0][0] != central[1][1]-central[1][0]):\n        raise ValueError(\"The paired halfwaves require two complete equal positive central intervals\")\n    edges = (Fraction(0), 2*delta, Fraction(1,2)-2*delta, Fraction(1,2),\n             Fraction(1,2)+2*delta, Fraction(1)-2*delta, Fraction(1))\n    if any(a >= b for a, b in zip(edges, edges[1:])):\n        raise ValueError(\"Every one of the six exact halfwave pieces is required\")\n    return dict(schema=\"complete-equal-central-intervals-reversed-paired-halfwave-profile-v1\",\n        proof_result=\"R728\", source_fixed_global_polarity=PHYSICAL_CENTRAL_POLARITY,\n        source_parameter_depends_on_angle_mean_direction_or_outer_point=False,\n        auxiliary_profile=\"the original complete R711 h_delta on [0,1]\",\n        auxiliary_mean_kernel_source_sha256=SEED_MEAN_KERNEL_SOURCE_SHA,\n        auxiliary_mean_rule_piece_count=12,\n        physical_central_interval_count=2, physical_piece_count_per_interval=6,\n        complete_physical_pair_piece_count=12,\n        exact_profile_delta=str(delta),\n        exact_normalized_piece_edges=[str(v) for v in edges],\n        exact_relative_central_intervals=[[str(v) for v in pair] for pair in central],\n        exact_relative_central_each_length=str(central[0][1]-central[0][0]),\n        exact_relative_physical_piece_edges=[\n            [str(a+(b-a)*v) for v in edges] for a,b in central],\n        signs_in_radial_discovery_order=[PHYSICAL_CENTRAL_POLARITY,-PHYSICAL_CENTRAL_POLARITY],\n        physical_profile=\"sign[index]*h_delta(t/2); t=(s-a)/(b-a)\",\n        radial_derivative_chain_factor=\"1/2\",\n        combined_cosine_mean=\"Lc*A_delta(lambda)*d\",\n        combined_transverse_mean=\"zero by equal complete central lengths and opposite signs\",\n        transverse_mean_zero_in_each_individual_interval=False,\n        old_per_interval_odd_physical_profile_inherited=False)\n\n\nBOUNDARY_CUTOFF_EPSILON = \"1/8\"\nBOUNDARY_CUTOFF_SCHEMA = \"complete-fixed-width-three-piece-C3-boundary-cutoff-v1\"\n\n\ndef _flat_cutoff_polynomial_jets(t, epsilon):\n    \"\"\"Exact arithmetic for Fraction inputs; working arithmetic for float inputs.\"\"\"\n    zero, one = t*0, t*0+1\n    if t <= zero:\n        return zero, zero, zero, zero\n    if t >= one:\n        return one, zero, zero, zero\n    denominator = one-epsilon\n    if epsilon <= t <= one-epsilon:\n        return (t-epsilon/2)/denominator, one/denominator, zero, zero\n    reflected = t > one-epsilon\n    u = (one-t)/epsilon if reflected else t/epsilon\n    G = (u*u*u*u)*(5+u*(-6+2*u))/2\n    S = u*u*u*(10+u*(-15+6*u))\n    S1 = 30*u*u*(one-u)*(one-u)\n    S2 = 60*u*(one-u)*(one-2*u)\n    value = epsilon*G/denominator\n    first = S/denominator\n    second = S1/(epsilon*denominator)\n    third = S2/(epsilon*epsilon*denominator)\n    if reflected:\n        return one-value, first, -second, third\n    return value, first, second, third\n\n\ndef _boundary_cutoff_exact_jets(t):\n    \"\"\"R725 value and first three normalized-coordinate derivatives, all exact.\"\"\"\n    if not isinstance(t, (str, Fraction)):\n        raise ValueError(\"Use an exact Fraction boundary cutoff coordinate\")\n    t = Fraction(t)\n    return _flat_cutoff_polynomial_jets(t, Fraction(BOUNDARY_CUTOFF_EPSILON))\n\n\ndef _boundary_cutoff_definition(support, central):\n    \"\"\"Complete fixed-rational three-piece law and every exact physical cut.\"\"\"\n    epsilon = Fraction(BOUNDARY_CUTOFF_EPSILON)\n    support = tuple(tuple(Fraction(v) for v in pair) for pair in support)\n    central = tuple(tuple(Fraction(v) for v in pair) for pair in central)\n    if (epsilon != Fraction(1,8) or len(support) != 2 or len(central) != 2\n            or any(len(pair) != 2 for pair in support+central)):\n        raise ValueError(\"This source fixes the complete R725 cutoff at epsilon=1/8\")\n    edges = (Fraction(0), epsilon, Fraction(1)-epsilon, Fraction(1))\n    layers = []\n    for index, ((left, right), (ca, cb)) in enumerate(zip(support, central)):\n        if not left < ca < cb < right:\n            raise ValueError(\"Every complete original boundary and central interval is required\")\n        for side, a, b, orientation in ((\"left\", left, ca, 1), (\"right\", cb, right, -1)):\n            physical = tuple(a+(b-a)*v for v in edges)\n            layers.append(dict(support_index=index, side=side,\n                exact_relative_interval=[str(a),str(b)],\n                exact_relative_piece_edges=[str(v) for v in physical],\n                exact_relative_internal_cuts=[str(v) for v in physical[1:-1]],\n                original_interval_normalized_piece_edges=[str(v) for v in edges],\n                cutoff_coordinate=\"t\" if orientation == 1 else \"1-t\",\n                odd_material_derivative_orientation=orientation,\n                physical_piece_count=3,\n                branches_in_increasing_material_order=(\n                    [\"left-polynomial\",\"affine\",\"right-reflection\"] if orientation == 1 else\n                    [\"right-reflection\",\"affine\",\"left-polynomial\"])))\n    return dict(schema=BOUNDARY_CUTOFF_SCHEMA, proof_result=\"R725\",\n        exact_epsilon=str(epsilon), epsilon_is_a_fixed_source_parameter=True,\n        epsilon_depends_on_angle_mean_direction_or_outer_point=False,\n        accurate_law=\"C=epsilon*G(t/epsilon)/(1-epsilon); (t-epsilon/2)/(1-epsilon); 1-epsilon*G((1-t)/epsilon)/(1-epsilon)\",\n        exact_G_ascending_coefficients=[\"0\",\"0\",\"0\",\"0\",\"5/2\",\"-3\",\"1\"],\n        exact_velocity_S5_ascending_coefficients=[\"0\",\"0\",\"0\",\"10\",\"-15\",\"6\"],\n        exact_normalized_piece_edges=[str(v) for v in edges],\n        constant_extension_outside_unit_interval=True,\n        piecewise_polynomial_degree=[6,1,6],\n        matching_material_derivative_order=3,\n        fourth_material_derivative_continuity_claimed=False,\n        exact_cut_values_and_first_three_normalized_jets=[\n            [str(v) for v in _boundary_cutoff_exact_jets(t)] for t in edges],\n        exact_first_derivative_peak=str(Fraction(1)/(1-epsilon)),\n        exact_derivative_integral=\"1\", exact_value_integral=\"1/2\",\n        four_boundary_layers=layers, complete_physical_boundary_piece_count=12,\n        complete_new_internal_boundary_cut_count=8,\n        original_central_halfwave_profile_changed=False,\n        original_bubble_gamma_and_raw_defect_lift_changed=False,\n        working_arithmetic=\"binary64 evaluation of this complete exact-rational law\",\n        working_rounding_or_integration_error_enclosed=False)\n\n\nSPHERICAL_BOUNDARY_SCHEMA = \"complete-R726-spherical-boundary-working-value-and-angular-jets-v1\"\nSPHERICAL_SMALL_Q_MAX = 0.25\nSPHERICAL_SERIES_DEGREE = 32\nR726_PROOF_SHA256 = \"faa3e44cf1392e6f7e1fb4e04adb039afc54ac881ef3f99b0b4ca9810d9e226b\"\n\n\ndef _spherical_boundary_definition():\n    \"\"\"Complete declared formulas; this function evaluates no field or root.\"\"\"\n    return dict(\n        schema=SPHERICAL_BOUNDARY_SCHEMA,\n        source_sha256=SEED_MEAN_KERNEL_SOURCE_SHA,\n        theorem_source_sha256=R726_PROOF_SHA256,\n        accurate_boundary=\"S_chi(N(x),N(y)); S=sin((1-chi)*theta)/sin(theta)*u+sin(chi*theta)/sin(theta)*d\",\n        accurate_zero_angle=\"the analytic extension at u=d, with value u\",\n        accurate_domain=\"nonzero x,y and N(x) != -N(y); acute-root theorems have additional hypotheses\",\n        accurate_normal_extension=\"normalize both arguments; output normalization is the identity in exact Slerp arithmetic\",\n        working_coordinate=\"q=sum((N(x)-N(y))**2)/2; no clipping of q or dot products\",\n        working_output=\"N(f_(1-chi)(q)*N(x)+f_chi(q)*N(y))\",\n        working_small_q_interval=[0.0, SPHERICAL_SMALL_Q_MAX],\n        working_small_q_degree=SPHERICAL_SERIES_DEGREE,\n        working_coefficient_recurrence=\"c0=a; c[n+1]=(((n+1)**2-a*a)/((n+1)*(2*n+3)))*c[n]\",\n        working_q_derivatives=\"first and second simultaneous Horner derivatives of the same actual coefficient array\",\n        working_a_derivative=\"differentiate the same coefficient recurrence; never substitute a separately rounded derivative table\",\n        working_large_q=\"theta=acos(1-q); f=sin(a*theta)/sin(theta); explicit first/second chain derivatives\",\n        working_coefficient_endpoints=\"a=0 or1 uses the exact constant coefficient value and zero q derivatives; a derivative is retained\",\n        input_normalizations_and_output_normalization_differentiated=True,\n        small_series_truncation_is_not_an_exact_Slerp_identity=True,\n        branch_switch_is_not_claimed_exact_C2_in_working_arithmetic=True,\n        coefficient_rounding_trigonometric_quadrature_root_and_jet_errors_enclosed=False,\n        degree32_exact_coefficient_tail_bounds_at_q_quarter=dict(\n            value_strictly_below=\"2^-98\", q_first_strictly_below=\"2^-91\",\n            q_second_strictly_below=\"2^-84\", a_first_strictly_below=\"2^-96\",\n            scope=\"only infinite-series truncation in exact arithmetic; not floating-point or full-field error\"),\n        R709_Euclidean_potential_or_R722_posterior_formula_inherited=False,\n        R726_acute_existence_or_global_branch_verified=False,\n        working_antipodal_or_nonfinite_pairs_unavailable=True,\n        all_original_boundary_nodes_weights_and_two_angular_orders_retained=True)\n\n\n\ndef _supported_seed(seed_model, *, reference, reference_id,\n                    initial_reference_bundle_sha256,\n                    fixed_scalar_metric_identity_sha256,\n                    profile, fixed_chart_core_sha256, bubble_nodes):\n    \"\"\"Check the full frozen seed JSON; no seed root or field is evaluated.\"\"\"\n    for value, name in (\n            (SEED_PROVIDER_SOURCE_SHA, 'locked complete supported seed provider'),\n            (SEED_MEAN_KERNEL_SOURCE_SHA, 'locked complete supported seed mean kernel')):\n        require_digest(value, name)\n    if not isinstance(seed_model, dict):\n        raise ValueError('Retain the entire fixed supported-smooth-triangle seed model')\n    seed = json_copy(seed_model)\n    if (seed.get('schema') != SEED_SCHEMA\n            or seed.get('source_sha256') != SEED_PROVIDER_SOURCE_SHA\n            or seed.get('source_fixed_global_central_polarity') != PHYSICAL_CENTRAL_POLARITY\n            or seed.get('original_reference_source_sha256') != REFERENCE_SOURCE_SHA\n            or seed.get('mean_kernel_source_sha256') != SEED_MEAN_KERNEL_SOURCE_SHA\n            or seed.get('initial_reference_bundle_sha256') != initial_reference_bundle_sha256\n            or seed.get('initial_reference_model_identity_sha256') != reference_id\n            or seed.get('complete_axisymmetric_reference_model') != reference\n            or seed.get('fixed_scalar_metric_identity_sha256') != fixed_scalar_metric_identity_sha256\n            or seed.get('fixed_scalar_profile_definition') != profile\n            or seed.get('fixed_chart_core_sha256') != fixed_chart_core_sha256):\n        raise ValueError('Bind the actual complete supported seed to this same full reference, chart and fixed scalar target')\n    word = seed.get('initial_height_hex')\n    if not isinstance(word, str):\n        raise ValueError('The fixed seed must record its actual initial height word')\n    try:\n        height = float.fromhex(word)\n    except ValueError as error:\n        raise ValueError('Invalid fixed seed initial height word') from error\n    if not math.isfinite(height) or height.hex() != word:\n        raise ValueError('Keep the finite canonical fixed seed initial height word')\n    nodes = _nodes(bubble_nodes)\n    expected_support = [[row[0], row[2]] for row in nodes]\n    if seed.get('exact_relative_support_intervals') != expected_support:\n        raise ValueError('The fixed seed uses exactly the two declared wide bubble supports; gamma is not a third interval')\n    boundary = _positive_exact_fraction(seed.get('exact_relative_boundary_total_length'),\n        'fixed seed boundary total length')\n    support = tuple(tuple(Fraction(v) for v in pair) for pair in expected_support)\n    if boundary >= 2*min(b-a for a,b in support):\n        raise ValueError('Keep positive boundary layers and both complete central intervals')\n    end_width = boundary/4\n    central = tuple((a+end_width,b-end_width) for a,b in support)\n    profile_delta = _positive_exact_fraction(seed.get('exact_profile_delta'), 'fixed seed smooth-triangle profile delta')\n    paired = _paired_halfwave_definition(central, profile_delta)\n    if (profile_delta >= Fraction(1, 8)\n            or seed.get('mathematical_profile_piece_count') != 6\n            or seed.get('mathematical_profile_piece_count_scope') != 'one physical central interval'\n            or seed.get('auxiliary_mean_profile_piece_count') != 12\n            or seed.get('complete_physical_pair_piece_count') != 12\n            or seed.get('paired_halfwave_definition') != paired\n            or seed.get('exact_relative_central_intervals') != paired['exact_relative_central_intervals']\n            or seed.get('exact_relative_boundary_each_end_length') != str(end_width)\n            or seed.get('mathematical_amplitude_interval') != '(0,pi)'\n            or seed.get('old_five_piece_working_cache_or_geometry_inherited') is not False):\n        raise ValueError('Bind both complete opposite halfwaves and the original full R711 amplitude rule')\n    cutoff = _boundary_cutoff_definition(support, central)\n    if (seed.get('exact_boundary_cutoff_epsilon') != BOUNDARY_CUTOFF_EPSILON\n            or seed.get('boundary_cutoff_definition') != cutoff):\n        raise ValueError('Bind the full R725 law, all four boundary layers, all eight internal cuts and exact endpoint jets')\n    spherical = _spherical_boundary_definition()\n    if (seed.get('spherical_boundary_definition') != spherical\n            or seed.get('accurate_definition') != 'fixed original unit T0 outside U; R726 S_chi(T0,d) on all boundary layers; cos(lambda*h_delta(t/2))*d+sign[index]*sin(lambda*h_delta(t/2))*w on the two equal central intervals'\n            or seed.get('accurate_mean_definition') != 'Lc*v+integral_E S_chi(T0,N(v))=P_original-Gamma_original-integral_complement_U T0; a_delta(lambda)=norm(v)'):\n        raise ValueError('Bind the complete independent spherical boundary and actual new mean equation')\n    working = seed.get('working_definition')\n    if (not isinstance(working, dict)\n            or working.get('schema') != 'R728-reversed-spherical-boundary-paired-halfwave-reference-working-definition-v1'\n            or working.get('physical_central_profile_definition') != paired\n            or working.get('source_fixed_global_central_polarity') != PHYSICAL_CENTRAL_POLARITY\n            or working.get('old_positive_first_physical_field_or_working_words_inherited') is not False\n            or working.get('spherical_boundary_definition') != spherical\n            or working.get('mean_and_field_use_same_raw_v_and_full_two_angular_jet_graph') is not True\n            or working.get('old_R709_potential_or_R722_posterior_formula_inherited') is not False\n            or working.get('R726_acute_domain_and_existence_hypotheses_certified') is not False\n            or working.get('physical_boundary_cutoff_definition') != cutoff\n            or working.get('exact_boundary_cutoff_epsilon') != BOUNDARY_CUTOFF_EPSILON\n            or working.get('old_boundary_quadrature_mean_root_or_cache_inherited') is not False\n            or working.get('original_outer_whole_cell_Gauss_and_partial_rule_is_separate') is not True\n            or working.get('auxiliary_mean_metadata_describes_original_full_R711_rule') is not True\n            or working.get('physical_profile_is_not_the_auxiliary_full_period_on_each_interval') is not True\n            or working.get('actual_field_quadrature_or_closure_words_inherited_from_original_seed') is not False):\n        raise ValueError('Retain the complete paired physical profile and distinct auxiliary mean rule')\n    # Root/positivity/capacity conditions belong to the real complete provider.\n    # Canonical positive parameters are not a contraction or field certificate.\n    json_copy(working)\n    return seed, canonical(seed)\n\n\n",
        "new": "def _canonical_positive_word(value,name,*,upper=None):\n    if not isinstance(value,str):\n        raise ValueError(\"Keep a canonical binary64 hex word for \"+name)\n    try:number=float.fromhex(value)\n    except ValueError as error:raise ValueError(\"Invalid \"+name) from error\n    if (not math.isfinite(number) or number.hex()!=value or number<=0\n            or (upper is not None and number>=upper)):\n        raise ValueError(\"Keep the complete finite positive \"+name)\n    return number\n\n\ndef _length_definition(value):\n    \"\"\"Pure reconstruction of the complete 87be physical/working declaration.\"\"\"\n    if not isinstance(value,dict):\n        raise ValueError(\"Retain the complete new length/inverse-arclength definition\")\n    orders=value.get(\"declared_original_orders\");budgets=value.get(\"complete_root_budgets\")\n    if (not isinstance(orders,dict)\n            or set(orders)!={\"radial_quadrature_order\",\"profile_quadrature_order\"}\n            or not isinstance(budgets,dict)\n            or set(budgets)!={\"mean_maxiter\",\"scalar_iterations\",\"mean_backtracks\"}):\n        raise ValueError(\"Retain all original declared orders and every complete scalar-root budget\")\n    ints=dict(orders,**budgets)\n    if any(type(v) is not int or v<1 for v in ints.values()):\n        raise ValueError(\"Keep all five positive complete integer rule parameters\")\n    if min(ints[\"radial_quadrature_order\"],ints[\"profile_quadrature_order\"])<4:\n        raise ValueError(\"Keep both complete positive Gauss orders at least four\")\n    tolerance=_canonical_positive_word(value.get(\"root_tolerance_hex\"),\"length root tolerance\")\n    armijo=_canonical_positive_word(value.get(\"armijo_hex\"),\"length Armijo coefficient\",upper=1)\n    eta,maximum=Fraction(\"1/32\"),Fraction(\"3/4\")\n    expected = dict(schema=LENGTH_DEFINITION_SCHEMA,proof_result=\"R730\",\n        exact_handle_length=str(eta),exact_maximum_contraction=str(maximum),\n        pulse_flatness=PULSE_FLATNESS,pulse=\"(1-(2*t-1)^12)^7\",\n        pulse_is_one_global_polynomial=True,polynomial_degree=84,\n        internal_formula_cuts=[],endpoint_vanishing_derivatives=list(range(7)),\n        controls=[\"Gamma\",\"Gamma+eta*ez\",\n            \"Gamma+2*eta*ez+(5/4)*kappa0*eta^2*er(Theta)\",\n            \"(R+2*eta)*er(Theta)+H0*ez\",\"(R+eta)*er(Theta)+H0*ez\",\"R*er(Theta)+H0*ez\"],\n        baseline=\"sum_{j=0}^5 binom(5,j)t^j(1-t)^(5-j)P_j\",\n        z_depends_on_phi=False,\n        contracted_curve=\"G_xi=((1-xi*psi)*baseline_xy,baseline_z)\",\n        accurate_length_equation=\"integral_0^1 |d_t G_xi| dt = S\",\n        accurate_root_range=\"0 < xi(phi) < 3/4\",\n        accurate_inverse_equation=\"integral_0^t |d_u G_xi(phi)| du = s\",\n        accurate_field=\"F(s,phi)=G_xi(phi)(t(s,phi),phi)\",\n        accurate_unit_reference=\"T0=F_s\",\n        complete_domain=\"all s in [0,S] and every original fixed-chart angle\",\n        original_fixed_scalar_chart_and_target_unchanged=True,\n        old_support_complement_boundary_width_and_profile_delta_used=False,\n        old_R709_R722_R726_R727_mean_or_branch_certificate_inherited=False,\n        working_full_cell_rule=\"all original normalized material mesh cells; full positive Gauss\",\n        working_order=max(ints[\"radial_quadrature_order\"],ints[\"profile_quadrature_order\"]),\n        declared_original_orders={n:ints[n] for n in (\n            \"radial_quadrature_order\",\"profile_quadrature_order\")},\n        working_inverse_rule=(\n            \"full positive prefix table and same positive Gauss rule on each required \"\n            \"partial cell; target (s/S)*actual_total_length\"),\n        working_angle_chain=(\n            \"two implicit length-root jets and two inverse-arclength jets of the \"\n            \"accurate expressions, evaluated with complete working quadratures\"),\n        complete_root_budgets={n:ints[n] for n in (\n            \"mean_maxiter\",\"scalar_iterations\",\"mean_backtracks\")},\n        root_tolerance_hex=tolerance.hex(),armijo_hex=armijo.hex(),\n        working_partial_integral_monotonicity_or_exact_discrete_derivatives_claimed=False,\n        quadrature_root_inverse_trigonometry_and_rounding_errors_enclosed=False,\n        original_outer_whole_cell_integration_and_normal32_are_separate=True)\n\n    if value!=expected:\n        raise ValueError(\"The whole exact R730 recipe, working rule or unpaid-error scope changed\")\n    return expected\n\n\ndef _safe_cone_seed(seed_model, *, reference, reference_id,\n                    initial_reference_bundle_sha256,\n                    fixed_scalar_metric_identity_sha256,\n                    profile, fixed_chart_core_sha256, bubble_nodes):\n    \"\"\"Full new seed JSON; no length root, inverse, array, field or old mean.\"\"\"\n    for value,name in ((SEED_PROVIDER_SOURCE_SHA,\"complete R730 provider\"),\n                       (LENGTH_KERNEL_SOURCE_SHA,\"complete R730 length kernel\")):\n        require_digest(value,name)\n    if not isinstance(seed_model,dict):\n        raise ValueError(\"Retain the entire R730 frozen seed model\")\n    seed=json_copy(seed_model)\n    length=_length_definition(seed.get(\"complete_safe_cone_definition\"))\n    _nodes(bubble_nodes)\n    height_word=seed.get(\"initial_height_hex\")\n    _canonical_positive_word(height_word,\"fixed seed height\")\n    radius_word=seed.get(\"radius_carrier_hex\")\n    _canonical_positive_word(radius_word,\"fixed R690 radius\")\n    if radius_word!=reference.get(\"radius_carrier_hex\"):\n        raise ValueError(\"The new reference must use the same complete R690 radius\")\n    raw_kappa=seed.get(\"exact_core_radial_curvature\")\n    if not isinstance(raw_kappa,str):\n        raise ValueError(\"Keep the actual original exact core-curvature Fraction\")\n    try:kappa=Fraction(raw_kappa)\n    except (ValueError,ZeroDivisionError) as error:\n        raise ValueError(\"Invalid exact original core-curvature parameter\") from error\n    if str(kappa)!=raw_kappa:\n        raise ValueError(\"Keep canonical original exact kappa0; no new fitted curvature\")\n    working=seed.get(\"working_definition\")\n    if not isinstance(working,dict):\n        raise ValueError(\"Retain the complete R730 working definition\")\n    S_word=working.get(\"physical_S_carrier_hex\")\n    _canonical_positive_word(S_word,\"same original physical S carrier\")\n    S_definition=working.get(\"exact_S_definition\")\n    if not isinstance(S_definition,dict) or not S_definition:\n        raise ValueError(\"Retain the complete original exact S enclosure record\")\n    json_copy(S_definition)\n    nodes=working.get(\"original_material_affine_nodes\")\n    if (not isinstance(nodes,list) or len(nodes)!=923\n            or any(not isinstance(row,list) or len(row)!=2 for row in nodes)\n            or any(not isinstance(v,str) for row in nodes for v in row)):\n        raise ValueError(\"Retain all 923 original exact-affine material nodes\")\n    try:normalized=[[str(Fraction(v)) for v in row] for row in nodes]\n    except (ValueError,ZeroDivisionError) as error:\n        raise ValueError(\"Invalid exact original affine material address\") from error\n    if normalized!=nodes or nodes[0]!=[\"0\",\"0\"] or nodes[-1]!=[\"1\",\"0\"]:\n        raise ValueError(\"Keep the complete canonical affine source domain including 0 and S\")\n    expected_working=dict(\n        schema=\"complete-R730-safe-cone-reference-working-definition-v1\",\n        length_kernel_source_sha256=LENGTH_KERNEL_SOURCE_SHA,\n        complete_length_definition=length,\n        exact_S_definition=S_definition,\n        physical_S_carrier_hex=S_word,\n        original_material_affine_nodes=nodes,\n        full_original_material_cells=922,\n        working_quadrature_partition=(\n            \"every original increasing material mesh carrier divided by the same S \"\n            \"carrier; this complete partition is a working rule, not a new target\"),\n        root_identity_includes_literal_angle_and_full_frozen_model=True,\n        inverse_queries_use_original_affine_material_addresses=True,\n        original_bubbles_raw_defect_lift_outer_full_cell_Gauss_and_normal32_are_separate=True,\n        working_inverse_normalizes_actual_total_length_to_full_S=True,\n        working_primitive_equals_integral_of_returned_unit_T0_claimed=False,\n        working_errors_enclosed=False)\n    if working!=expected_working:\n        raise ValueError(\"Keep the entire actual reference partition, both inverse chains and unpaid working defects\")\n    expected_seed=dict(schema=SEED_SCHEMA,source_sha256=SEED_PROVIDER_SOURCE_SHA,\n        original_reference_source_sha256=REFERENCE_SOURCE_SHA,\n        length_kernel_source_sha256=LENGTH_KERNEL_SOURCE_SHA,\n        complete_axisymmetric_reference_model=reference,\n        initial_reference_model_identity_sha256=reference_id,\n        initial_reference_bundle_sha256=initial_reference_bundle_sha256,\n        fixed_scalar_metric_identity_sha256=fixed_scalar_metric_identity_sha256,\n        fixed_scalar_profile_definition=profile,\n        fixed_chart_core_sha256=fixed_chart_core_sha256,\n        initial_height_hex=height_word,radius_carrier_hex=radius_word,\n        exact_core_radial_curvature=raw_kappa,exact_physical_handle_length=\"1/32\",\n        exact_maximum_contraction=\"3/4\",\n        complete_safe_cone_definition=length,\n        core_cap_control_jets=\"R730 complete six controls, original kappa0 and fixed Gamma/Theta\",\n        reference_height_is_declared_working_word_not_exact_scalar_integral=True,\n        accurate_S_R_chart_from_complete_original_definition=True,\n        scalar_and_S_carriers_not_promoted_to_exact_values=True,\n        seed_is_frozen_from_original_initial_point=True,\n        current_outer_core_H_and_all_rotation_variables_are_not_seed_inputs=True,\n        original_scalar_reference_outside_old_supports_retained=False,\n        old_mean_v_d_w_lambda_arrays_or_roots_inherited=False,\n        accurate_reference=\"G(xi(phi),t(s,phi),phi), complete scalar length and inverse equations\",\n        accurate_T0=\"the arclength unit tangent of that same complete G\",\n        working_definition=expected_working)\n    if seed!=expected_seed:\n        raise ValueError(\"Bind all and only the complete actual R730 model and its original fixed input\")\n    return seed,canonical(seed)\n\n\n"
      },
      {
        "index": 26,
        "old": "Bind eighteen fixed Q words to one complete R728 reversed spherical-boundary seed.",
        "new": "Bind eighteen fixed Q words to one complete R730 safe-cone length seed."
      },
      {
        "index": 466,
        "old": "fixed paired-halfwave provider.",
        "new": "fixed global safe-cone provider."
      },
      {
        "index": 664,
        "old": "The complete provider, mean-jet\nkernel and base operator",
        "new": "The complete provider, length/inverse-arclength\nkernel and base operator"
      },
      {
        "index": 918,
        "old": "fixed-fejer-r728-reference-literal-zero-endpoint-Q-input-v1",
        "new": "fixed-fejer-r730-reference-literal-zero-endpoint-Q-input-v1"
      },
      {
        "index": 1000,
        "old": "fixed-fejer-r728-reference-literal-two-bubble-endpoint-Q-v1",
        "new": "fixed-fejer-r730-reference-literal-two-bubble-endpoint-Q-v1"
      },
      {
        "index": 1724,
        "old": "complete-fixed-fejer-r728-so3-meridian-with-core-lift-v1",
        "new": "complete-fixed-fejer-r730-so3-meridian-with-core-lift-v1"
      },
      {
        "index": 1801,
        "old": "427227b006741b809fc728d4c4d23fe7fa59f2ccbf5e020e15fc8ed0b730168c",
        "new": "b9c787340021b5736f2796f2b84a1c25cb4b0ce96333eb98f543b1e8923ce267"
      },
      {
        "index": 1882,
        "old": "complete-fixed-fejer-R728-reversed-spherical-boundary-paired-halfwave-meridian-seed-reference-v1",
        "new": "complete-fixed-fejer-R730-safe-cone-arclength-reference-v1"
      },
      {
        "index": 1970,
        "old": "c6fc04db9223981e1829620613c71de4c0bec93813ec0eeaf5f8ef7770217e86",
        "new": "53ebce095394a833d95a65b834ae889b4cb9554e06ef839fcb626bddcb8864b8"
      },
      {
        "index": 2067,
        "old": "2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23",
        "new": "87be2efa7381f50bd419c0d91a3b0c5b1a762f9f1eb7d1f2f7a053f8bc93cfc2"
      },
      {
        "index": 2036,
        "old": "SEED_MEAN_KERNEL_SOURCE_SHA",
        "new": "LENGTH_KERNEL_SOURCE_SHA"
      },
      {
        "index": 23561,
        "old": "SEED_MEAN_KERNEL_SOURCE_SHA",
        "new": "LENGTH_KERNEL_SOURCE_SHA"
      },
      {
        "index": 2130,
        "old": "PHYSICAL_CENTRAL_POLARITY = -1",
        "new": "PULSE_FLATNESS = 6\nLENGTH_DEFINITION_SCHEMA = 'R730-global-single-pulse-contracted-Bezier-physical-definition-v1'"
      },
      {
        "index": 2244,
        "old": "PARENT_COMPLETE_BINDER_SOURCE_SHA = 'ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39'",
        "new": "PARENT_COMPLETE_BINDER_SOURCE_SHA = '872dca4cf1e15c419aad68d31c053fc4f3465357a3e162413a19002f5b70e43d'"
      },
      {
        "index": 3456,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 3491,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 23033,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 23413,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 23499,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 23594,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 23694,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 24544,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 24590,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 26015,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 27428,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 27541,
        "old": "fixed_supported_unit_seed",
        "new": "fixed_safe_cone_unit_seed"
      },
      {
        "index": 23594,
        "old": "fixed_safe_cone_unit_seed_mean_kernel_sha256",
        "new": "fixed_safe_cone_unit_seed_length_kernel_sha256"
      },
      {
        "index": 23007,
        "old": "_supported_seed(",
        "new": "_safe_cone_seed("
      },
      {
        "index": 26940,
        "old": "_supported_seed(",
        "new": "_safe_cone_seed("
      },
      {
        "index": 29578,
        "old": "supported_unit_seed_is_frozen_before_current_free_point",
        "new": "safe_cone_unit_seed_is_frozen_before_current_free_point"
      },
      {
        "index": 31961,
        "old": "supported_unit_seed_is_frozen_before_current_free_point",
        "new": "safe_cone_unit_seed_is_frozen_before_current_free_point"
      },
      {
        "index": 18908,
        "old": "supported-smooth-triangle",
        "new": "R730 safe-cone"
      },
      {
        "index": 20970,
        "old": "supported-smooth-triangle",
        "new": "R730 safe-cone"
      },
      {
        "index": 24837,
        "old": "supported-smooth-triangle",
        "new": "R730 safe-cone"
      },
      {
        "index": 24976,
        "old": "supported-smooth-triangle",
        "new": "R730 safe-cone"
      },
      {
        "index": 27447,
        "old": "supported-smooth-triangle",
        "new": "R730 safe-cone"
      },
      {
        "index": 27878,
        "old": "supported-smooth-triangle",
        "new": "R730 safe-cone"
      },
      {
        "index": 28122,
        "old": "supported-smooth-triangle",
        "new": "R730 safe-cone"
      },
      {
        "index": 28356,
        "old": "supported-smooth-triangle",
        "new": "R730 safe-cone"
      },
      {
        "index": 31659,
        "old": "supported-smooth-triangle",
        "new": "R730 safe-cone"
      },
      {
        "index": 26089,
        "old": "actual supported seed",
        "new": "actual safe-cone seed"
      },
      {
        "index": 27580,
        "old": "whole supported seed",
        "new": "whole safe-cone seed"
      },
      {
        "index": 24800,
        "old": "exactly the twelve declared complete R730 safe-cone input fields",
        "new": "exactly the declared complete R730 safe-cone input fields"
      }
    ],
    "edit_kind": "ordered-exact-offset"
  },
  {
    "role": "reference_calibration",
    "parent": {
      "role": "reference_calibration",
      "name": "fixed_fejer_r728_reference_calibration.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r728_reference_calibration.py",
      "bytes": 11850,
      "sha256": "00d50d208a19e7f75b431e3a8010bca068022539c82dbbb598c1f615b865ae8a",
      "git_blob_sha": "840613d36e1ff24fa19f9d0b086034e4faa622ca"
    },
    "output": {
      "name": "fixed_fejer_r730_reference_calibration.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r730_reference_calibration.py",
      "bytes": 11895,
      "sha256": "7650bbd18c856d70164a8b76eab22d63231d401cff91bf63f8b0bd5019b010fd",
      "git_blob_sha": "dd289d0f24c50cf3afddb7279305d66f697b3c43",
      "role": "complete R730 actual frozen-reference closure calibration"
    },
    "edits": [
      {
        "old": "Complete frozen-reference calibration for the R715 paired-halfwave field.",
        "new": "Complete R715-method frozen-reference calibration for the R730 length field.",
        "count": 1
      },
      {
        "old": "complete-R715-frozen-reference-working-calibration-v1",
        "new": "complete-R730-frozen-reference-working-calibration-v1",
        "count": 1
      },
      {
        "old": "complete-fixed-fejer-r728-detached-meridian-normal-layer-v1",
        "new": "complete-fixed-fejer-r730-detached-meridian-normal-layer-v1",
        "count": 1
      },
      {
        "old": "427227b006741b809fc728d4c4d23fe7fa59f2ccbf5e020e15fc8ed0b730168c",
        "new": "b9c787340021b5736f2796f2b84a1c25cb4b0ce96333eb98f543b1e8923ce267",
        "count": 1
      },
      {
        "old": "complete-fixed-fejer-r728-so3-meridian-with-core-lift-v1",
        "new": "complete-fixed-fejer-r730-so3-meridian-with-core-lift-v1",
        "count": 1
      },
      {
        "old": "c6fc04db9223981e1829620613c71de4c0bec93813ec0eeaf5f8ef7770217e86",
        "new": "53ebce095394a833d95a65b834ae889b4cb9554e06ef839fcb626bddcb8864b8",
        "count": 1
      },
      {
        "old": "2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23",
        "new": "87be2efa7381f50bd419c0d91a3b0c5b1a762f9f1eb7d1f2f7a053f8bc93cfc2",
        "count": 1
      },
      {
        "old": "MEAN_SOURCE",
        "new": "LENGTH_KERNEL_SOURCE",
        "count": 2
      },
      {
        "old": "Calibrate only the complete fixed R711 base",
        "new": "Calibrate only the complete fixed R730 base",
        "count": 1
      },
      {
        "old": "fixed_supported_unit_seed_model",
        "new": "fixed_safe_cone_unit_seed_model",
        "count": 1
      },
      {
        "old": "mean_kernel_source_sha256",
        "new": "length_kernel_source_sha256",
        "count": 1
      },
      {
        "old": "The complete fixed R711 reference changed",
        "new": "The complete fixed R730 length/inverse reference changed",
        "count": 1
      },
      {
        "old": "R715-fixed-reference-centred-working-normal-definition-v1",
        "new": "R730-fixed-length-reference-centred-working-normal-definition-v1",
        "count": 1
      },
      {
        "old": "fixed_supported_reference_identity_sha256",
        "new": "fixed_safe_cone_reference_identity_sha256",
        "count": 1
      }
    ],
    "edit_kind": "all-exact-count"
  }
];
const MINIMAL_KERNEL_DELIVERY={
  "name": "R730-safe-cone-minimal-reference-complete-source-delivery.json",
  "path": "topics/visible-flex-larger-amplitude/computations/R730-safe-cone-minimal-reference-complete-source-delivery.json",
  "bytes": 9725,
  "sha256": "8f59f54e5cffe473c88ae91b2847c763e3a58512ca195bdecf322419ea7e432d",
  "git_blob_sha": "1dc015fc0e7039be74be60810cd1036bf3184d4c",
  "role": "complete two-runtime source delivery and honest necessary successor contract"
};
function digest(value){return createHash("sha256").update(value).digest("hex");}
function exact(record,bytes){
 if(bytes.length!==record.bytes||digest(bytes)!==record.sha256)
  throw Error("Complete whole source mismatch: "+record.path);
}
function apply(body,job,reverse=false){
 let text=body;const edits=reverse?[...job.edits].reverse():job.edits;
 for(const edit of edits){
  const from=reverse?edit.new:edit.old,to=reverse?edit.old:edit.new;
  if(job.edit_kind==="ordered-exact-offset"){
   if(text.slice(edit.index,edit.index+from.length)!==from)
    throw Error("Exact full replacement block changed: "+job.role);
   text=text.slice(0,edit.index)+to+text.slice(edit.index+from.length);
  }else{
   if(text.split(from).length-1!==edit.count)
    throw Error("All complete literal occurrences differ: "+job.role);
   text=text.split(from).join(to);
  }
 }
 return text;
}
const words=process.argv.slice(2),args={};
if(words.length!==4)throw Error("Use --source-repository REPO --generated-directory OUT");
for(let i=0;i<4;i+=2){
 if(!["--source-repository","--generated-directory"].includes(words[i])
    ||args[words[i]]||!words[i+1])throw Error("Keep both complete directory arguments once");
 args[words[i]]=path.resolve(words[i+1]);
}
const source=args["--source-repository"],out=args["--generated-directory"];
if(!source||!out||source===out)throw Error("Use separate complete source and output directories");
const results=[];
for(const job of COMPLETE_JOBS){
 const originalBytes=fs.readFileSync(path.resolve(source,job.parent.path));
 exact(job.parent,originalBytes);
 const original=originalBytes.toString("utf8"),generated=apply(original,job);
 const bytes=Buffer.from(generated,"utf8");exact(job.output,bytes);
 if(apply(generated,job,true)!==original)
  throw Error("Complete parent source is not restored by inverse text derivation");
 const target=path.resolve(out,job.output.path);
 if(!target.startsWith(out+path.sep))throw Error("Output escaped its generated directory");
 if(fs.existsSync(target)&&!fs.readFileSync(target).equals(bytes))
  throw Error("Refuse to replace a different full source");
 fs.mkdirSync(path.dirname(target),{recursive:true});fs.writeFileSync(target,bytes);
 exact(job.output,fs.readFileSync(target));
 results.push({role:job.role,parent:job.parent,output:job.output,
  complete_original_parent_restored_by_inverse_text:true});
}
process.stdout.write(JSON.stringify({
 schema:SCHEMA,complete:true,results,minimal_length_kernel_delivery:MINIMAL_KERNEL_DELIVERY,
 full_parent_bytes_read:true,source_text_only:true,
 AST_compile_or_science_executed:false,new_scientific_admission_gate:false,
 actual_future_point_model_report_packet_or_certificate:null,
 refs_queues_or_running_jobs_modified:false
},null,2)+"\n");
