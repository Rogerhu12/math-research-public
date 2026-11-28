"""The paid R641 controls, length, amplitude and true centers inside the current full operator."""
import time
import numpy as np
from r641_fixed_physical_center_chart import PhysicalChart
from r641_true_three_end_chart import (LD, Jet, reduced, original, paid, background, adaptive,
    COUNTS, ld_text, identity, DependentEndsPending)
from r632_paid_physical_source_jets import source_value, kinetic_scale, source_history


class Paid48Chart(PhysicalChart):
    def _evaluate_impl(self, parameters, derivatives=True, fixed_state=None, fixed_center=None, enforce_box=True):
        if not derivatives or fixed_state is not None or fixed_center is not None or list(parameters)!=self.paid_state["shape_parameters"]:
            return super()._evaluate_impl(parameters, derivatives, fixed_state, fixed_center, enforce_box)
        state, diagnostics = self.paid_state, self.anchor_diagnostics
        reduced.require_public_science()
        q = np.asarray(parameters,float).copy()
        if (fixed_state is None and fixed_center is None and derivatives and enforce_box
                and self.cache_parameters is not None and np.array_equal(q,self.cache_parameters)):
            self.latest_curve = self.cache_curve
            self.latest_geometry = self.cache_curve["physical_attainers"]
            COUNTS["same_shape_complete_true_chain_cache_reuses"] += 1
            return self.cache_curve
        self.evaluations += 1; self.jet_evaluations += int(derivatives)
        self.last_parameters = q
        started = time.monotonic()
        if q.shape != (self.dimension,) or not np.all(np.isfinite(q)):
            raise ValueError("All 256 actual shape parameters are required")
        self.latest_geometry = {"phase":"actual_three_end_shape_started",
            "actual_shape_parameter_identity":identity(q.tolist()),
            "physical_fields_or_graph_branch_not_yet_qualified":True}
        qld = np.asarray(q,dtype=LD)
        dimension = self.dimension if derivatives else 0
        if fixed_state is None:
            control, root_report = self.scalar_root(qld)
        else:
            if derivatives:
                raise ValueError("A fixed physical fine curve has no re-solved chart derivative")
            control = LD(fixed_state["height_control_LD_decimal"])
            root_report = {"state":"fixed_same_curve_control_not_resolved",
                "actual_control_LD_decimal":ld_text(control), "fine_scalar_P_root_recomputed":False}
        self.last_control = control
        rows, eta, P = self._base_map(qld,control,"full" if derivatives else "value")
        if derivatives:
            Pb = P.derivative[-1]
            if not Pb < -LD(15)/136:
                raise FloatingPointError("Full actual P chain leaves selected nonzero derivative branch")
            db = -P.derivative[:-1]/Pb
            def compose(v):
                return Jet(v.value,v.derivative[:-1]+v.derivative[-1]*db)
            rows = [[compose(v) for v in row] for row in rows]
            eta = [compose(v) for v in eta]
            P = compose(P)
        zero = rows[0][0]*0
        U = K = S2 = S4 = W = zero
        for weight,row,ee in zip(self.grid.weights,rows,eta):
            h,hx,hxx,k,kx,kxx = row
            d,v = h*ee-k,hx*ee-kx/2
            U += weight*(hx/h)**2
            K += weight*k*k
            S2 += weight*ee*d/h
            S4 += weight*ee*k*d*d/h
            W += weight*(v/h)**2
        D, N = U*S4-K*W, K*S2-S4
        self.latest_geometry.update(phase="actual_three_end_integrals_completed",
            actual_base_P0=float(P.value),U=float(U.value),K_kappa=float(K.value),
            S2=float(S2.value),S4=float(S4.value),W0=float(W.value),graph_D=float(D.value),graph_N=float(N.value),
            actual_height_control_LD_decimal=ld_text(control))
        if fixed_state is None:
            if not (U.value>0 and K.value>0 and D.value<0 and N.value<0):
                raise FloatingPointError("Actual R641 negative nondegenerate positive-length graph unavailable")
            L0 = LD(state["physical_length_LD_decimal"])
            z0 = 1/L0**2
            dz = (N.derivative-z0*D.derivative)/D.value
            length = source_value((N/D)**LD("-.5"), state["physical_length_LD_decimal"],
                "length", diagnostics, -L0**3*dz/2)
            z = length**-2
            alpha = kinetic_scale(U, K, length, state["physical_alpha_LD_decimal"], diagnostics)
            amplitude_square = alpha*alpha
        self.latest_geometry.update(actual_physical_length=float(length.value),actual_alpha=float(alpha.value))
        if not (LD("2.1") <= length.value <= LD("7.9")):
            raise FloatingPointError("Actual derived physical L leaves the original unchanged box")
        geometry, acceleration = [], []
        for row,ee in zip(rows,eta):
            h,hx,hxx,k,kx,kxx = row
            geometry.append([h,alpha*k,alpha*ee,hx/length,alpha*kx/length])
            acceleration.append([hxx/length**2,alpha*kxx/length**2])
        report = background.physical_attainers(geometry,self.grid.x,length.value)
        report.update(actual_shape_parameter_identity=identity(q.tolist()),
            fixed_center_kappa_x=ld_text(self.c), fixed_polynomial_background=background.BACKGROUND,
            shape_coordinates_are_all_256_R638_projected_h_and_original_kappa_directions=True,
            actual_height_control_LD_decimal=ld_text(control), scalar_P_root=root_report,
            U=float(U.value),K_kappa=float(K.value),S2=float(S2.value),S4=float(S4.value),W0=float(W.value),
            graph_D=float(D.value),graph_N=float(N.value),graph_z=float(z.value),
            alpha=float(alpha.value),alpha_LD_decimal=ld_text(alpha.value),
            physical_length_LD_decimal=ld_text(length.value),
            actual_kinetic_identity=float(amplitude_square.value*K.value-1-U.value*z.value),
            actual_s0_normalized_identity=float(amplitude_square.value*(amplitude_square.value*S4.value-S2.value-W.value*z.value)),
            actual_base_P0=float(P.value),
            physical_center_v=float(geometry[0][4].value),physical_center_a=float(acceleration[0][0].value),
            physical_center_beta=float(acceleration[0][0].value-geometry[0][0].value*geometry[0][4].value**2/4),
            all_polynomial_hull_fields_in_original_box=False,
            continuous_original_integral_error_not_certified_by_graph_algebra=True)
        self.latest_geometry = report
        if enforce_box and not report["all_sampled_original_physical_fields_in_box"]:
            raise FloatingPointError("Actual R641 field sample leaves an original physical box")
        # q, control, alpha and L are the exact serialized source values here.
        qualification = self.paid_qualification
        self.boxes.latest_record = qualification
        report["adaptive_polynomial_qualification"] = qualification
        good = qualification["state"] == "all_four_represented_polynomial_fields_certified"
        report["all_polynomial_hull_fields_in_original_box"] = good
        if enforce_box and qualification["state"] == "pending":
            raise adaptive.PolynomialPhysicalPending(qualification)
        if enforce_box and not good:
            raise FloatingPointError("Actual R641 polynomial point leaves an original physical box")
        density = [[length*v for v in paid.density(row)] for row in geometry]
        primitive = self.grid.integrate(density)
        total = primitive[-1]
        history = source_history(primitive, state, diagnostics)
        H = geometry[0][0]
        end = [total[1]/length,(8*total[3]+2*total[1])/length,
               8*H**2*total[4]/length,4*H**2*total[6]/length]
        dependent = np.asarray([history[-1][j].value for j in (1,3,6)], dtype=LD)
        report["actual_dependent_three_terminal_values"] = [float(v) for v in dependent]
        report["actual_dependent_three_terminal_max"] = float(np.max(np.abs(dependent)))
        report["unchanged_original_dependent_end_tolerance"] = float(self.original_end_tolerance)
        if fixed_state is None and np.max(np.abs(dependent)) > self.original_end_tolerance:
            raise DependentEndsPending({"state":"actual_dependent_original_ends_unclosed",
                "shape_parameters":q.tolist(), "physical_attainers":report,
                "remaining_r1_objective_does_not_hide_unpaid_dependent_rows":True})
        curve = {"shape_parameters":q,"parameters":q,"geometry":geometry,"acceleration":acceleration,
            "history":history,"total_integral":total,"end":end,"reduced_end":[end[2]],
            "length":length,"grid":self.grid,"alpha":alpha,"physical_attainers":report,
            "knots":self.knots,"height_control":control,"independent_memory_coordinates":0,
            "fixed_physical_alpha_length_height_control_and_center":fixed_state is not None,
            "fixed_polynomial_background":background.BACKGROUND,
            "dependent_three_end_values_are_actual_density_integrals_not_assigned_zero":True}
        curve.update(paid_anchor_state=state, paid_anchor_diagnostics=diagnostics)
        self.latest_curve = curve
        if fixed_state is None and fixed_center is None and derivatives and enforce_box:
            self.cache_parameters,self.cache_curve = q.copy(),curve
        COUNTS["complete_three_end_curve_evaluations"] += 1
        COUNTS["complete_three_end_curve_seconds"] += time.monotonic()-started
        self.clock.check("after_R641_complete_true_three_end_curve")
        return curve
