"""Reconstruct the paid physical source values and differentiate their original implicit equations."""
import time
import numpy as np
import r632_true_hermite_bvp as solver
from r632_true_hermite_kinetic_chart import LD, Jet, ld_text, paid, original

free_project = solver.project_true_ruling
COUNTS, UNIT, end_chain = solver.COUNTS, solver.UNIT, solver.end_chain


def source_value(raw, stored, name, diagnostics, derivative):
    value = LD(stored)
    diagnostics[name] = {"free_LD_decimal": ld_text(raw.value), "paid_LD_decimal": stored,
        "difference_LD_decimal": ld_text(raw.value-value), "equal": bool(raw.value == value)}
    return Jet(value, derivative)


def kinetic_scale(U, K, length, stored, diagnostics):
    value = LD(stored)
    target = 1+U/length**2
    free = (target/K)**LD(".5")
    return source_value(free, stored, "alpha", diagnostics,
        (target.derivative-value**2*K.derivative)/(2*value*K.value))


def source_history(primitive, state, diagnostics):
    total = primitive[-1]
    zero = total[0]*0
    centers = []
    for j, stored in enumerate(state["all_eight_physical_center_A_LD_decimal"]):
        calculated = -total[j] if j in original.ODD else zero
        centers.append(source_value(calculated, stored, "center_A_"+str(j),
            diagnostics, calculated.derivative))
    # These are the physical initial values used by every opposite-side coefficient,
    # potential, rho integration and ruling in the original complete history.
    return [[centers[j]+v for j, v in enumerate(row)] for row in primitive]


def quotient_at_source(numerator, denominator, stored, name, diagnostics):
    value = LD(stored)
    return source_value(numerator/denominator, stored, name, diagnostics,
        (numerator.derivative-value*denominator.derivative)/denominator.value)


def project(data, fixed_gauges=None, fixed_zeta0=None):
    curve = data["curve"]
    if "paid_anchor_state" not in curve or fixed_gauges is not None or fixed_zeta0 is not None:
        return free_project(data, fixed_gauges=fixed_gauges, fixed_zeta0=fixed_zeta0)
    state = curve["paid_anchor_state"]
    diagnostics = curve["paid_anchor_diagnostics"]
    started = time.monotonic()
    curve = data["curve"]
    zero = data["zeta0"]*0
    base_rows = list(data["base_ruling"])
    op = data["outputs"][0][0]
    numerator = op[0]+op[1]*curve["acceleration"][0][0]
    denominator = 2*paid.weights(curve["geometry"][0])[0]
    physical_zero = quotient_at_source(numerator, denominator, state["dependent_physical_zeta0_LD_decimal"],
        "zeta0", diagnostics)
    delta = physical_zero-data["zeta0"]
    base_rows = [v-2*paid.weights(curve["geometry"][i//2])[0]*delta
                 for i,v in enumerate(base_rows)]
    dd, bb, do, be = zero, zero, zero, zero
    for i in range(0, len(base_rows), 2):
        d, beta = data["design"][i]
        odd, even = (base_rows[i]-base_rows[i+1])/2, (base_rows[i]+base_rows[i+1])/2
        dd, bb, do, be = dd+d*d, bb+beta*beta, do+d*odd, be+beta*even
    if not dd.value > 0 or not bb.value > 0:
        raise FloatingPointError("The full actual two-constant gauge map is degenerate")
    saved = state["two_constant_physical_gauges_LD_decimal"]
    gauges = [quotient_at_source(do, dd, saved[0], "mu", diagnostics),
              quotient_at_source(be, bb, saved[1], "beta", diagnostics)]
    rows = [v-design[0]*gauges[0]-design[1]*gauges[1]
            for v, design in zip(base_rows, data["design"])]
    values, jac = paid.values_and_jacobian(rows)
    values = np.asarray(values, dtype=LD)
    normalization = UNIT*np.sqrt(LD(len(rows)))
    end_value, end_jac = end_chain(curve)
    residual = np.r_[end_value, np.asarray(values/normalization, float)]
    derivative = np.vstack((end_jac, np.asarray(jac/normalization, float)))
    all_values = np.r_[np.asarray(end_value, dtype=LD), values/normalization]
    result = {"data":data, "raw_ruling":values, "residual":residual,
        "jacobian":derivative, "phi":float(np.sum(all_values*all_values)/2),
        "gauges":gauges, "zeta0":physical_zero, "gauge_denominators":[dd, bb],
        "fixed_unit":str(UNIT), "full_off_root_projection_derivative":fixed_gauges is None,
        "fixed_gauges_used":fixed_gauges is not None,
        "all_rows":len(residual), "all_shape_columns":derivative.shape[1]}
    COUNTS["full_LD_projected_ruling_evaluations"] += 1
    COUNTS["full_LD_projected_ruling_rows"] += len(rows)
    COUNTS["full_LD_projection_seconds"] += time.monotonic()-started
    result["source_physical_anchors_and_full_implicit_derivatives"] = diagnostics
    solver.emit("PAID_PHYSICAL_ANCHOR_DIFFERENCES", diagnostics)
    return result

