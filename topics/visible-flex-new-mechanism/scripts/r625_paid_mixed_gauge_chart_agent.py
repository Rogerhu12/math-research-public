#!/usr/bin/env python3
"""R625 continuation: keep a0, use the two original constant gauges directly.

The old published R620 chart is evaluated once only to recover its unstored
LD gauge anchor from the exact paid input. Its complete triangular derivative
is reported, not guessed from the failed step's magnitude. Subsequent charts
use the original center zeta0 identity and two fixed-unit gauge offsets.
All scientific execution is restricted to the named public Actions.
"""
from __future__ import annotations

import time

import numpy as np

import r620_original_center_time_jets_agent as original_center

LD, Jet = original_center.LD, original_center.Jet
paid, reduced = original_center.paid, original_center.reduced
GAUGE_UNIT_TEXT = "3967798143562589"
COORDINATE_ORDER = ["H", "v", "p0c", "p2c", "s1c", "r0c", "a0",
                    "zeta1_fixed_unit_offset", "zeta2_fixed_unit_offset", "L"]


def ld_text(value):
    return np.format_float_scientific(LD(value), precision=24, unique=False, trim="k")


class PaidMixedGaugeChart:
    def __init__(self, legacy_parameters, coefficients, potential, clock, progress):
        reduced.require_public_science()
        started = time.monotonic()
        self.coefficients, self.potential, self.clock = coefficients, potential, clock
        self.unit = LD(GAUGE_UNIT_TEXT)
        self.calls = self.coefficient_evaluations = 0
        self.seconds = self.coefficient_seconds = 0.
        self.active_evaluator = None
        self.progress = progress
        self.progress.update({"stage":"recover_unstored_original_LD_gauge_anchor", "completed":False})
        try:
            clock.check("before_necessary_paid_LD_center_anchor_reconstruction")
            old_chart = original_center.build_center_chart(
                legacy_parameters, coefficients, potential, derivatives=True)
            self.anchor = np.asarray(old_chart["gauge_value"], dtype=LD).copy()
            self.legacy_parameters = np.asarray(legacy_parameters, float).copy()
            self.initial_parameters = self.legacy_parameters.copy()
            self.initial_parameters[7:9] = 0.
            self.anchor_decimal = [ld_text(value) for value in self.anchor]
            transition = np.asarray(old_chart["gauge_parameter_jacobian"], dtype=LD)
            self.receipt = {
                "legacy_parameters":self.legacy_parameters.tolist(),
                "mixed_coordinate_order":COORDINATE_ORDER,
                "mixed_initial_parameters":self.initial_parameters.tolist(),
                "fixed_original_gauge_unit":GAUGE_UNIT_TEXT,
                "necessary_original_LD_gauge_anchor_decimal":self.anchor_decimal,
                "anchor_display_binary64":np.asarray(self.anchor, float).tolist(),
                "legacy_gauge_parameter_jacobian":np.asarray(transition, float).tolist(),
                "legacy_a_j_f_triangular_block":np.asarray(transition[:, 6:9], float).tolist(),
                "legacy_chart_receipt":old_chart["receipt"],
                "new_free_gauges_are_global_constants":True,
                "zero_offsets_represent_the_same_paid_physical_input":True,
                "legacy_D_root_seed_or_fixed_fine_replayed":False,
                "old_matrix_condition_number_was_measured":False,
                "all_ill_conditioning_removed_claim":False}
            self.progress.update({"stage":"recovered_original_LD_gauge_anchor", "completed":True,
                                  "receipt":self.receipt})
            clock.check("after_necessary_paid_LD_center_anchor_reconstruction")
        finally:
            self.progress["seconds"] = time.monotonic()-started

    def build(self, parameters, derivatives=True):
        self.calls += 1
        started = time.monotonic()
        self.active_evaluator = None
        try:
            return self._build(parameters, derivatives)
        finally:
            self.seconds += time.monotonic()-started
            if self.active_evaluator is not None:
                self.coefficient_evaluations += self.active_evaluator.evaluations
                self.coefficient_seconds += self.active_evaluator.seconds
            self.active_evaluator = None

    def _build(self, parameters, derivatives=True):
        reduced.require_public_science()
        started = time.monotonic()
        self.clock.check("before_original_mixed_constant_gauge_chart")
        parameters = np.asarray(parameters, dtype=LD)
        if parameters.shape != (10,) or not np.all(np.isfinite(parameters)):
            raise ValueError("The mixed original chart has exactly ten finite coordinates.")
        dimension = 10 if derivatives else 0
        identity = np.eye(10, dtype=LD) if derivatives else None
        jets = [Jet(value, identity[i] if derivatives else np.zeros(0))
                for i, value in enumerate(parameters)]
        H, v, p0c, p2c, s1c, r0c, a0, u1, u2, length = jets
        if not (LD('.8')<H.value<3 and abs(v.value)<6
                and LD('2.1')<=length.value<=LD('7.9')):
            raise ValueError("The unchanged original center/length physical box is violated.")
        if not (v.value<LD('-.05') and (a0-H*v*v/4).value>LD('.05')):
            raise FloatingPointError("Outside the same declared negative-v, positive-beta center patch.")
        zero = H*0
        center_g = [H, zero, zero, zero, v]
        center_a = [p0c, zero, p2c, zero, zero, s1c, zero, r0c]
        # Constant time jets retain exactly the old value evaluation order.
        # Their time derivatives are not used as a replacement for the ODE.
        time_g = [original_center.TimeJet2.constant(value) for value in center_g]
        time_a = [original_center.TimeJet2.constant(value) for value in center_a]
        evaluator = original_center.OriginalCoefficientTimeJets(self.coefficients)
        self.active_evaluator = evaluator
        op = evaluator.evaluate(time_g, time_a)
        if not (op[1].value<0 and op[2].value>0):
            raise FloatingPointError("The original center Ch/Ck coefficient signs were lost.")
        wc = paid.weights(time_g)[0].v
        zeta0 = (op[0].v+op[1].v*a0)/(2*wc)
        zeta1, zeta2 = self.anchor[1]+self.unit*u1, self.anchor[2]+self.unit*u2
        gauge = [zeta0, zeta1, zeta2]
        initial = center_g+center_a+[zero]*6
        initial_value, initial_jacobian = paid.values_and_jacobian(initial)
        gauge_value, gauge_jacobian = paid.values_and_jacobian(gauge)
        receipt = {
            "parameter_order":COORDINATE_ORDER,
            "actual_coordinate_parameters":np.asarray(parameters, float).tolist(),
            "actual_global_zeta":np.asarray(gauge_value, float).tolist(),
            "actual_global_zeta_LD_decimal":[ld_text(value) for value in gauge_value],
            "fixed_original_gauge_unit":GAUGE_UNIT_TEXT,
            "actual_center_a0":float(a0.value),
            "actual_center_d_first":float((-v/2).value),
            "actual_center_beta_second":float((a0-H*v*v/4).value),
            "center_zeta0_is_original_ruling_identity":True,
            "j0_f0_are_implicit_original_center_jets_not_independent_coordinates":True,
            "two_original_gauges_are_one_constant_pair_for_the_whole_curve":True,
            "complete_original_center_parameter_chain":True,
            "parameter_derivative_dimension":dimension,
            "coefficient_time_parameter_evaluations":evaluator.evaluations,
            "coefficient_time_parameter_seconds":evaluator.seconds,
            "old_identity_or_directional_gate_replayed":False,
            "seconds":time.monotonic()-started}
        self.clock.check("after_original_mixed_constant_gauge_chart")
        return {"parameters":parameters.copy(), "parameter_dimension":dimension,
                "center_geometry":center_g, "center_history":center_a,
                "global_gauge":gauge, "physical_length":length, "initial_jets":initial,
                "initial_value":initial_value, "initial_parameter_jacobian":initial_jacobian,
                "gauge_value":gauge_value, "gauge_parameter_jacobian":gauge_jacobian,
                "receipt":receipt, "coordinate_order":COORDINATE_ORDER}
