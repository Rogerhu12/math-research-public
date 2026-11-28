#!/usr/bin/env python3
"""New whole-tail R/G/S inequalities for the actual R643 coupled mean.

Consume an existing, exact-source CompleteMeanTail and its already-paid
receipt for the same actual response. No old root, ODE, DtN, field, Jacobian,
FFT, position query or old branch gate is executed here. The only implicit
derivative denominator belongs to the fixed accepted seed. The trial mean
remains free, including at a zero trial mean coefficient.

All scientific arithmetic is public-Actions only. Original source errors
remain explicit, and unresolved rows make these conditional exact-source
consequences. Mathematical formulas and continuous domains: R648.
"""
from collections import defaultdict
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
TAIL_SOURCE = 'r643_complete_mean_tail_bounds_20261128.py'
TAIL_SHA = '4cc0d0430efb6815806a6a1ba04a58067c5c5dc7e3efcb124aae9547c184c47a'
MODEL_SOURCE = 'r643_complete_mean_height_model_20261128.py'
MODEL_SHA = '91944d7298d81952a28c09b416db1242d5d913fc43b8d19ea97fbab5c38b8185'
SCHEMA = 'r648-complete-same-mean-true-tail-G-and-normalized-S-v1'
COUNTS = defaultdict(int)


def _load():
    path = HERE / TAIL_SOURCE
    if hashlib.sha256(path.read_bytes()).hexdigest() != TAIL_SHA:
        raise ValueError('the original actual R643 tail source changed')
    spec = importlib.util.spec_from_file_location('r648_actual_r643_tail_formulas', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


tail_module = _load()
paid, bounds, I = tail_module.paid, tail_module.bounds, tail_module.I


def _read_interval(value):
    return paid.supplied_interval(value)


def _basis_second_bound(knots, index, degree):
    """True B-spline derivative recursion, including repeated knots."""
    result = I(0)
    for first in (index, index + 1):
        if knots[first] == knots[first + degree]:
            continue
        outer_width = paid.literal_interval(knots[first + degree]) - paid.literal_interval(knots[first])
        bounds.positive(outer_width)
        inner = I(0)
        for left, right in ((first, first + degree - 1), (first + 1, first + degree)):
            if knots[left] == knots[right]:
                continue
            width = paid.literal_interval(knots[right]) - paid.literal_interval(knots[left])
            bounds.positive(width)
            inner += (degree - 1) / width
        result += degree * inner / outer_width
    return bounds.upper(result)


class CompleteTrueTailConnection:
    def __init__(self, actual_tail):
        bounds.public_only()
        module = sys.modules.get(type(actual_tail).__module__)
        path = HERE / TAIL_SOURCE
        if (module is None or type(actual_tail).__name__ != 'CompleteMeanTail'
                or Path(module.__file__).resolve() != path.resolve()
                or hashlib.sha256(path.read_bytes()).hexdigest() != TAIL_SHA
                or hashlib.sha256((HERE / MODEL_SOURCE).read_bytes()).hexdigest() != MODEL_SHA):
            raise ValueError('the existing unchanged R643 tail object is required')
        self.tail = actual_tail
        self.joint = actual_tail.joint
        self.provenance = self.joint.guard()
        self.source_snapshot = paid.CurrentModelTailAnchor._snapshot(actual_tail)
        if self.source_snapshot != actual_tail.source_snapshot:
            raise ValueError('the actual tail source changed before the new derivative bounds')
        self.rc, self.mouth = actual_tail.rc, actual_tail.mouth
        self.Elo, self.Ehi = actual_tail.Elo, actual_tail.Ehi
        self.Wplus = actual_tail.W_upper
        self.reference = self._complete_reference_budget()
        seed_extra = self._extra_angular_budget(actual_tail.response)
        self.seed = self._combined_budget(actual_tail.seed_angular_budget['scaled'], seed_extra)
        branch = actual_tail.seed_anchor['conditional_whole_tail_mean_branch']
        self.seed_kappa = _read_interval(branch['kappa'])
        self.seed_lambda = actual_tail.seed_lambda_bound
        bounds.positive(self.seed_kappa)
        ref_box = self._box(self.reference, 1 + self.reference['r'])
        bounds.positive(ref_box['M_lower'])
        factor = 2 * ref_box['omega_upper'] / (ref_box['omega_lower'] * ref_box['M_lower'])
        self.Er_WWr = bounds.upper(factor * ref_box['C_over_W'])
        self.Er_W2 = bounds.upper(factor * (
            ref_box['C_over_W'] * self.reference['rr']
            + self.Ehi * ref_box['B_over_W'] ** 2))
        seed_box = self._box(self.seed, 1 + self.seed_lambda + self.seed['r'])
        self.seed_sr_Wr = bounds.upper(seed_box['omega_upper'] / self.seed_kappa * (
            seed_box['C_over_W'] + seed_box['M_upper'] * self.Er_WWr / 2))
        self.seed_sr_W = bounds.upper(seed_box['omega_upper'] / self.seed_kappa * (
            seed_box['C_over_W'] * self.seed['rr']
            + self.Ehi * seed_box['B_over_W'] ** 2
            + seed_box['M_upper'] * self.Er_W2 / 2))
        U, ell, amplitude = actual_tail.U, actual_tail.ell, actual_tail.A
        if U.lo < 108:
            raise ArithmeticError('the complete original cap-to-mouth window changed')
        self.W2_upper = bounds.upper(amplitude ** 2 * bounds.exp_i(-2 * U))
        self.WWr_upper = bounds.upper(amplitude ** 2 / ell
                                     * (U ** 3 + 3 * U ** 2) * bounds.exp_i(-2 * U))
        self.reference_box, self.seed_box = ref_box, seed_box
        COUNTS['complete_existing_tail_connection_consumers'] += 1

    def _complete_reference_budget(self):
        """Only the previously missing rr/rtheta bounds; reuse paid r/q/t."""
        tail = self.tail
        model, old = tail.model, tail.model.old
        original = old.old
        raw_q, raw_knots = model.driver.weak.RAW_Q_JSON, model.driver.weak.RAW_KNOT_JSON
        if (hashlib.sha256(raw_q.encode()).hexdigest() != model.driver.weak.SOURCE_Q_SHA
                or hashlib.sha256(raw_knots.encode()).hexdigest() != model.driver.weak.SOURCE_KNOT_SHA):
            raise ValueError('the same complete old coefficient and knot literals are required')
        old_q = json.loads(raw_q, parse_float=Decimal)
        knots = json.loads(raw_knots, parse_float=Decimal)
        reference_q = json.loads(model.original_q_json, parse_float=Decimal)
        degree, count = int(original.bs.k), len(knots) - int(original.bs.k) - 1
        nb = int(original.nb)
        if degree != 5 or nb != count + 4 or len(old_q) != int(original.original_nq) + 1:
            raise ValueError('the exact old five-degree spline plus four local-extra columns is required')
        P = tail.original_basis_receipt['whole_tail_basis_value_bounds']
        Q = tail.original_basis_receipt['whole_tail_basis_derivative_bounds']
        if len(P) != nb or len(Q) != nb:
            raise ValueError('the paid complete basis receipt differs')
        Q2 = [_basis_second_bound(knots, index, degree) for index in range(count)]
        Q2.extend([I(0)] * 4)
        normal = tail.contract['old_envelope_and_force_normalizations']
        scales = [_read_interval(row) for row in normal['mode_height_scales']]
        scale = _read_interval(normal['envelope_scale'])
        R, alpha = [_read_interval(tail.contract[key]) for key in ('physical_R', 'physical_alpha')]
        gamma, power, U, ell = I(1) / 10000, 2 + 2 * alpha, tail.U, tail.ell
        width = R - tail.mouth
        bounds.positive(width, scale, *scales)
        if (10 / U - 4 * gamma * U ** 3 / ell ** 4 + 3).hi >= 0:
            raise ArithmeticError('whole quartic second-derivative monotonicity is unresolved')
        envelope = tail.reference_construction_receipt['old_envelope_bound']
        B0, B1, G0 = [envelope[key] for key in (
            'value_over_W', 'radial_derivative_over_W', 'quartic_value_over_W')]
        G2 = bounds.upper(((4 * gamma * U ** 5 / ell ** 5 + power / width) ** 2
                           + 20 * gamma * U ** 6 / ell ** 6 + power / width ** 2) * G0)
        square_sum = bounds.total([bounds.upper((tail.seed_ratio[j] / s) ** 2)
                                  for j, s in zip((2, 4, 6, 8), scales)])
        B2 = bounds.upper((4 * tail.W_upper * square_sum + G2) / scale)
        amp = tail.amplitude
        seed_coefficients = [amp] + [paid.absolute(amp * paid.literal_interval(value))
                                     for value in old_q[1:4]]
        values, firsts, seconds = [], [], []
        for mode_index, (j, coefficient) in enumerate(zip((2, 4, 6, 8), seed_coefficients)):
            germ = bounds.upper(coefficient * tail.seed_ratio[j])
            v0, v1, v2 = germ, germ, germ
            for i in range(nb):
                c = paid.absolute(amp * paid.literal_interval(old_q[4 + mode_index * nb + i]))
                v0 += c * B0 * P[i]
                v1 += c * (B1 * P[i] + B0 * Q[i])
                v2 += c * (B2 * P[i] + 2 * B1 * Q[i] + B0 * Q2[i])
            values.append(bounds.upper(v0))
            firsts.append(bounds.upper(v1))
            seconds.append(bounds.upper(v2))
        Vr, Vrr = bounds.total(firsts), bounds.total(seconds)
        Vq = bounds.total([bounds.upper(j * value) for j, value in zip((2, 4, 6, 8), values)])
        Vrt = bounds.total([bounds.upper(j * value) for j, value in zip((2, 4, 6, 8), firsts)])
        saturation = I(3) / 20
        rr = bounds.upper(2 * (Vrr + 2 * tail.W_upper * Vr ** 2 / saturation))
        rt = bounds.upper(Vrt + 2 * tail.W_upper * Vr * Vq / saturation)
        for index, j in enumerate(range(4, 23, 2)):
            c = paid.absolute(amp * paid.literal_interval(reference_q[index + 1]))
            rr += c * tail.seed_ratio[j]
            rt += j * c * tail.seed_ratio[j]
        force = paid.absolute(amp ** 2
            * paid.literal_interval(old_q[int(original.original_nq)])
            * _read_interval(normal['force_tail_multiplier']) / _read_interval(normal['force_scale']))
        rr += force * tail.raw_ratio[4]
        rt += 4 * force * tail.raw_ratio[4]
        result = dict(tail.reference_scaled)
        result.update(rr=bounds.upper(rr), rt=bounds.upper(rt))
        self.reference_extension_receipt = {
            'all_original_basis_columns': nb,
            'all_old_pre_tanh_coefficients_included': 4 * nb,
            'original_canonical512_mean_retained': True,
            'quartic_value_ratio_used': G0,
            'new_quartic_second_radial_ratio': G2,
            'new_complete_envelope_second_radial_ratio': B2,
            'all_original_spline_second_derivative_bounds': Q2,
            'all_original_fixed_post_modes': list(range(4, 23, 2)),
            'original_forced_raw_j4_coefficient_abs': force,
            'literal_reference_q_sha256': hashlib.sha256(model.original_q_json.encode()).hexdigest(),
            'old_paid_q_sha256': model.driver.weak.SOURCE_Q_SHA,
            'old_complete_knots_sha256': model.driver.weak.SOURCE_KNOT_SHA}
        COUNTS['new_full_reference_second_jet_budget_passes'] += 1
        COUNTS['old_pre_tanh_coefficients_in_new_second_jet_sums'] += 4 * nb
        COUNTS['original_basis_second_derivative_bounds_formed'] += count
        return result

    def _extra_angular_budget(self, angular_response):
        tail, model = self.tail, self.tail.model
        if len(angular_response) != model.nq:
            raise ValueError('all original1473 angular coordinates including hard tau are required')
        rr, rt = I(0), I(0)
        for index, j in enumerate(range(4, 23, 2)):
            c = paid.absolute(tail.amplitude * paid.literal_interval(float(angular_response[index])))
            rr += c * tail.seed_ratio[j]
            rt += j * c * tail.seed_ratio[j]
        for mode_index, j in enumerate(model.modes):
            for degree_index, k in enumerate(model.tail_degrees):
                index = model.tail_start + mode_index * len(model.tail_degrees) + degree_index
                c = paid.absolute(tail.amplitude * paid.literal_interval(float(angular_response[index])))
                # These exact-source inequalities were already produced by
                # the preceding complete paid tail receipt. Never ask its
                # _gaussian method to fill a missing old scientific entry.
                key = (int(j), int(k))
                if key not in tail.gaussian_columns:
                    raise ValueError('the same response must have its full paid Gaussian tail receipt first')
                column = tail.gaussian_columns[key]
                _, K1, K2 = column['over_W_threejet_upper']
                rr += c * K2
                rt += int(j) * c * K1
        COUNTS['all_actual_old_germ_second_jet_coefficients_consumed'] += 10
        COUNTS['all_actual_Gaussian_second_jet_coefficients_consumed'] += len(model.modes) * len(model.tail_degrees)
        return {'rr': bounds.upper(rr), 'rt': bounds.upper(rt)}

    def _combined_budget(self, paid_scaled_angular, extra):
        if set(paid_scaled_angular) != {'r', 'q', 't'} or set(extra) != {'rr', 'rt'}:
            raise ValueError('every true tail jet must be accounted')
        result = {key: bounds.upper(self.reference[key] + value)
                  for key, value in paid_scaled_angular.items()}
        result.update({key: bounds.upper(self.reference[key] + value) for key, value in extra.items()})
        return result

    def _box(self, jets, P):
        W = self.Wplus
        beta2 = 1 - (W * jets['q'] / self.rc) ** 2
        bounds.positive(beta2)
        beta = bounds.sqrt_i(beta2)
        u2 = self.Elo - W ** 2 * P ** 2 / beta2
        Nlo = 1 - W ** 2 * P * jets['t'] / (self.rc * beta ** 3)
        Nhi = 1 / beta + W ** 2 * P * jets['t'] / (self.rc * beta ** 3)
        bounds.positive(u2, Nlo)
        u = bounds.sqrt_i(u2)
        Mchange = bounds.upper(W ** 2 * (P * jets['t'] + jets['q'] ** 2 / self.rc))
        return {
            'P': P, 'beta_squared_lower': beta2, 'beta_lower': beta,
            'u_squared_lower': u2, 'u_lower': u, 'N_lower': Nlo, 'N_upper': Nhi,
            'C_over_W': bounds.upper(self.Ehi * jets['t'] + self.mouth * P),
            'B_over_W': bounds.upper(jets['rt'] + jets['q'] / self.rc),
            'M_upper': self.mouth + Mchange, 'M_lower': self.rc - Mchange,
            'omega_upper': 1 / (u ** 3 * self.rc * beta ** 3),
            'omega_lower': 1 / (self.mouth * self.Ehi * bounds.sqrt_i(self.Ehi))}

    def evaluate(self, response, paid_tail_receipt):
        bounds.public_only()
        response = self.joint._check(response)
        tail = self.tail
        if (self.joint.guard() != self.provenance
                or paid.CurrentModelTailAnchor._snapshot(tail) != self.source_snapshot):
            raise ValueError('the actual model/source changed during new tail consumption')
        expected = {
            'joint_model_sha256': self.joint.model_sha256,
            'same_target_sha256': self.joint.identity.target_sha256,
            'actual_response_sha256': paid.json_sha(response.tolist()),
            'fixed_seed_response_sha256': tail_module.SEED_RESPONSE_SHA,
            'fixed_seed_paid_FINAL_sha256': tail_module.SEED_FINAL_SHA}
        if (any(paid_tail_receipt.get(key) != value for key, value in expected.items())
                or paid_tail_receipt.get('old_source_error_accounting') != tail.contract['source_error_accounting']
                or not paid_tail_receipt.get('all94_mean_columns_accounted')
                or paid_tail_receipt.get('mean_columns_zero_here_by_true_support') != 90
                or paid_tail_receipt.get('mean_Gaussian_degree_list') != [0, 1, 2, 3]
                or _read_interval(paid_tail_receipt['true_numerical_mouth']).lo > tail.mouth.lo
                or _read_interval(paid_tail_receipt['true_numerical_mouth']).hi < tail.mouth.hi):
            raise ValueError('the complete preceding tail receipt must be for this same actual response')
        scaled = {key: _read_interval(value) for key, value in
                  paid_tail_receipt['complete_angular_response_budget']['scaled'].items()}
        extra = self._extra_angular_budget(self.joint.angular_response(response))
        actual = self._combined_budget(scaled, extra)
        mean = [_read_interval(value) for value in paid_tail_receipt['actual_new_mean_over_W_threejet_upper']]
        if len(mean) != 3:
            raise ValueError('all actual mean Gaussian radial jets are required')
        P = 1 + self.seed_lambda + mean[1] + actual['r']
        box = self._box(actual, P)
        J2 = bounds.upper(self.seed_sr_W + mean[2] + actual['rr'])
        R1 = bounds.upper(box['omega_upper'] * (
            box['C_over_W'] * (1 + self.seed_sr_Wr) + box['M_upper'] * self.Er_WWr / 2))
        R0 = bounds.upper(box['omega_upper'] * (
            box['C_over_W'] * J2 + self.Ehi * box['B_over_W'] ** 2
            + box['M_upper'] * self.Er_W2 / 2))
        Rbound = bounds.upper(R1 * self.WWr_upper + R0 * self.W2_upper)
        Ehi_sqrt, Elo_sqrt = bounds.sqrt_i(self.Ehi), bounds.sqrt_i(self.Elo)
        A_lower = box['N_lower'] / Ehi_sqrt
        a_upper = box['N_upper'] / box['u_lower']
        bounds.positive(A_lower)
        ut = bounds.upper(
            self.Wplus ** 2 * P * actual['rt'] / (box['u_lower'] * box['beta_squared_lower'])
            + self.Wplus ** 4 * P ** 2 * actual['q'] * actual['t']
              / (box['u_lower'] * self.rc ** 2 * box['beta_squared_lower'] ** 2))
        Fbound = _read_interval(paid_tail_receipt['whole_tail_actual_turning_F_absolute_bound'])
        bounds.nonnegative(Fbound)
        # pi < 22/7 gives an exact rational upward substitute for both
        # continuous convolution norms. No floating value of pi is exacted.
        scalar_primitive, vector_primitive = I(22) / 28, I(22) / 14
        Qbound = bounds.upper(scalar_primitive * Rbound * (1 + a_upper / A_lower))
        Hbound = bounds.upper(Fbound / A_lower * (box['N_upper'] + ut)
                             + self.mouth / A_lower * Qbound)
        Sbound = bounds.upper(vector_primitive * Hbound / Elo_sqrt)
        eta = bounds.upper(3 * Sbound + Sbound ** 2)
        support = box['u_lower'] - Ehi_sqrt * Sbound
        det = self.rc * box['beta_lower'] * support if support.lo > 0 else None
        COUNTS['new_actual_complete_true_tail_G_and_S_bounds'] += 1
        result = {
            'schema': SCHEMA,
            'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'same_original_R643_tail_sha256': TAIL_SHA,
            'same_original_R643_model_sha256': MODEL_SHA,
            **expected,
            'same_actual_source_snapshot_sha256': self.source_snapshot,
            'same_literal_source_contract_sha256': tail.contract_sha,
            'consumed_preceding_tail_receipt_sha256': paid.json_sha(paid_tail_receipt),
            'true_cap_radius': self.rc, 'true_original_numerical_mouth': self.mouth,
            'whole_u_lower': tail.U,
            'new_complete_reference_second_jet_receipt': self.reference_extension_receipt,
            'complete_reference_five_jet_over_W_bound': self.reference,
            'complete_fixed_seed_five_jet_over_W_bound': self.seed,
            'complete_actual_five_jet_over_W_bound': actual,
            'whole_reference_positive_box': self.reference_box,
            'whole_fixed_seed_positive_box': self.seed_box,
            'whole_actual_trial_positive_box': box,
            'same_fixed_seed_kappa': self.seed_kappa,
            'same_fixed_seed_lambda_radius': self.seed_lambda,
            'Eprime_W_absWprime_coefficient': self.Er_WWr,
            'Eprime_W_squared_coefficient': self.Er_W2,
            'fixed_seed_sprime_absWprime_coefficient': self.seed_sr_Wr,
            'fixed_seed_sprime_W_coefficient': self.seed_sr_W,
            'true_W_squared_upper': self.W2_upper,
            'true_W_absWprime_upper': self.WWr_upper,
            'actual_R_W_absWprime_coefficient': R1,
            'actual_R_W_squared_coefficient': R0,
            'whole_true_tail_actual_R_absolute_upper': Rbound,
            'whole_true_tail_actual_G_absolute_upper': Rbound,
            'consumed_whole_true_tail_actual_F_absolute_upper': Fbound,
            'whole_true_tail_actual_A_positive_lower': A_lower,
            'whole_true_tail_actual_u_theta_absolute_upper': ut,
            'whole_true_tail_actual_Q_absolute_upper': Qbound,
            'whole_true_tail_actual_H_vector_norm_upper': Hbound,
            'whole_true_tail_actual_S_vector_norm_upper': Sbound,
            'whole_true_tail_actual_relative_metric_operator_upper': eta,
            'whole_true_tail_actual_horizontal_support_speed_lower': support,
            'whole_true_tail_positive_horizontal_Jacobian_proved_under_same_source_contract': det is not None,
            'whole_true_tail_horizontal_Jacobian_positive_lower_or_unresolved': det,
            'continuous_scalar_primitive_norm_upper': scalar_primitive,
            'continuous_vector_primitive_norm_upper': vector_primitive,
            'pi_upper_used_as_exact_rational': '22/7',
            'all_complete_off_solution_F_G_and_phase_terms_retained': True,
            'only_fixed_accepted_seed_mean_denominator_used': True,
            'trial_mean_elimination_or_lambda_box_used': False,
            'original_tail_boundary_or_any_true_function_changed': False,
            'old_source_error_accounting': tail.contract['source_error_accounting'],
            'unresolved_original_source_errors': tail.unresolved,
            'conditional_on_all_original_declared_source_enclosures': bool(tail.unresolved),
            'finite_FFT_or_radial_evaluation_error_declared_zero': False,
            'continuous_actual_source_and_primitive_bounds_not_finite_array_identity': True,
            'same_prior_tail_receipt_reused_without_replaying_its_gate': True,
            'old_DtN_ODE_mean_root_J_FFT_or_position_queries_executed': False,
            'new_consumer_cumulative_arithmetic_counts': dict(COUNTS),
            'underlying_bound_counters_are_overlapping_not_new_disjoint_costs': dict(bounds.COUNTS),
            'whole_body_curvature_reach_macro_amplitude_or_README_certified': False}
        return paid.tree_intervals(result)
