"""Short whole-box factors for the same R141 exact comparison model.

No imports, IO, entry point or numerical execution at import.  The caller
provides the directed API, the unchanged R141 core, exact dyadic balances,
and the already declared number of equal subboxes in every original panel.
Only one panel's private factors are retained.  A short scalar Taylor
enclosure replaces exp(tau*H) with a wide interval tau; the mathematical
model, true lengths, actual S, source matrices, all193 atoms and Gram
formulas are unchanged.  All actual evaluations belong in public Actions.
"""


class SharedScalarFactorProvider:
    """Whole-factor evaluator for a fixed complete uniform subbox plan.

    balances[i] is one EXACT positive dyadic trial balance, e.g. the
    binary64 q_balance from the completed v3 plan interpreted exactly.
    It defines an internal B_i, not a replacement for actual reference S_i.
    At the declared higher certification precision this avoids exponentiating the
    earlier 320-bit representation width of reference_qs.

    With D = B H B^-1/(2*n), each subbox has tau=(2*j+1)/(2*n)+t/(2*n),
    |t|<=1.  The exact short variation exp(+/-t D)-I is enclosed by signed
    factorial powers plus a componentwise positive exponential tail.
    """

    def __init__(self, api, km, core, model, step_counts, balances, order=64):
        core.require(model.get("comparison_BVP_verified") is True,
                     "the same complete verified comparison BVP")
        count = len(model["generators"])
        core.require(len(step_counts) == len(balances) == count and count > 0,
                     "one complete uniform plan and balance per original panel")
        core.require(all(type(n) is int and n > 0 for n in step_counts),
                     "positive finite uniform panel substep counts")
        core.require(all(q.is_finite() and q.lower() == q.upper()
                         and api.lower(q) > 0 for q in balances),
                     "strictly positive exact dyadic trial balances")
        core.require(type(order) is int and order >= 1,
                     "declared finite positive Taylor order")
        self.api, self.km, self.core, self.model = api, km, core, model
        self.step_counts, self.balances = tuple(step_counts), tuple(balances)
        self.order, self.cache = order, None
        self.private_statistics = {
            "panels_prepared": 0, "boxes_evaluated": 0,
            "point_recurrence_steps": 0, "backward_requests_restarted": 0,
            "maximum_live_panel_caches": 1,
            "wide_interval_matrix_exponentials": 0,
        }

    def cuts(self, panel):
        one = self.model["context"].domain.fone
        count = self.step_counts[panel]
        return [one*j/count for j in range(count+1)]

    def _diagonal_left(self, factors, matrix):
        self.core.require(len(factors) == matrix.rows, "whole left diagonal")
        return self.km.Matrix(matrix.rows, matrix.cols,
            [[factors[i]*x for x in row] for i, row in enumerate(matrix.values)])

    def _diagonal_right(self, matrix, factors):
        self.core.require(len(factors) == matrix.cols, "whole right diagonal")
        return self.km.Matrix(matrix.rows, matrix.cols,
            [[x*factors[j] for j, x in enumerate(row)] for row in matrix.values])

    def _prepare_panel(self, panel):
        api, km, core, model = self.api, self.km, self.core, self.model
        n = self.step_counts[panel]
        qb = self.balances[panel]
        balance = [api.one]*96 + [qb]*97
        inverse_balance = [api.one]*96 + [api.one/qb]*97
        raw_generator = model["generators"][panel]
        balanced = self._diagonal_right(
            self._diagonal_left(balance, raw_generator), inverse_balance)
        short = km.scale(api, api.rational(1, 2*n), balanced)

        # Every input to exp below encloses one fixed point matrix.  In
        # particular, no whole subbox parameter is passed to matrix exp.
        half_plus = core.directed_exp(api, km, short, api.one)
        half_minus = core.directed_exp(api, km, short, -api.one)
        step_plus = km.multiply(api, half_plus, half_plus)
        step_minus = km.multiply(api, half_minus, half_minus)

        # The nonnegative point matrix M majorizes |D_exact| entrywise.
        # Its exact positive exponential tail majorizes every omitted
        # signed Taylor term for ALL common scalar t in [-1,1].
        majorant = km.Matrix(core.N, core.N,
            [[api.magnitude(x) for x in row] for row in short.values])
        majorant_exp = core.directed_exp(api, km, majorant, api.one)
        signed_power = km.eye(api, core.N)
        positive_power = km.eye(api, core.N)
        positive_prefix = km.eye(api, core.N)
        variation = km.zeros(api, core.N, core.N)
        odd_range = api.interval(-api.one, api.one)
        even_range = api.interval(api.zero, api.one)
        for k in range(1, self.order+1):
            signed_power = km.scale(api, api.rational(1, k),
                                    km.multiply(api, signed_power, short))
            positive_power = km.scale(api, api.rational(1, k),
                                      km.multiply(api, positive_power, majorant))
            positive_prefix = km.add(api, positive_prefix, positive_power)
            variation = km.add(api, variation,
                km.scale(api, odd_range if k % 2 else even_range, signed_power))
        remainder = km.add(api, majorant_exp, km.scale(api, -api.one, positive_prefix))
        whole_variation, tail_rows = [], []
        for row, tail_row in zip(variation.values, remainder.values):
            result, caps = [], []
            for value, tail in zip(row, tail_row):
                cap = core.positive_upper(api, tail)
                caps.append(cap)
                result.append(value + api.interval(-cap, cap))
            whole_variation.append(result)
            tail_rows.append(core.positive_upper(api, sum(caps, api.zero)))
        whole_variation = km.Matrix(core.N, core.N, whole_variation)
        remainder_infinity_upper = core.maximum_upper(api, tail_rows)

        node = model["nodes"][panel]
        raw_columns = km.hcat(node["left"], node["right"])
        raw_rows = km.vcat(node["ell"], node["rho"])
        base_columns = self._diagonal_left(balance, raw_columns)
        base_rows = self._diagonal_right(raw_rows, inverse_balance)
        first_columns = km.multiply(api, half_plus, base_columns)
        first_rows = km.multiply(api, base_rows, half_minus)
        actual_q = model["context"].reference_qs[panel]
        core.require(api.lower(actual_q) > 0, "unchanged positive actual S weight")
        actual_S_over_B = [api.one]*96 + [actual_q/qb]*97
        self.cache = {
            "panel": panel, "index": 0, "balance": balance,
            "actual_S_over_B": actual_S_over_B,
            "step_plus": step_plus, "step_minus": step_minus,
            "variation": whole_variation,
            "remainder_infinity_upper": remainder_infinity_upper,
            "first_columns": first_columns, "first_rows": first_rows,
            "columns": first_columns, "rows": first_rows,
        }
        self.private_statistics["panels_prepared"] += 1

    def local_factors(self, box, source_matrix):
        """The complete OL, OR, IL, IR enclosures on one declared whole box."""
        api, km, core, model = self.api, self.km, self.core, self.model
        domain = model["context"].domain
        domain.validate_box(box)
        panel, lo, hi = box
        steps = self.step_counts[panel]
        index_fraction = lo*steps
        core.require(index_fraction.denominator == 1,
                     "subbox starts at a declared exact uniform cut")
        index = index_fraction.numerator
        core.require(0 <= index < steps and hi == domain.fone*(index+1)/steps,
                     "one entire declared uniform comparison subbox")
        core.require(source_matrix.rows == core.N, "whole raw source matrix")
        if self.cache is None or self.cache["panel"] != panel:
            self._prepare_panel(panel)
        data = self.cache
        if index < data["index"]:
            data["index"] = 0
            data["columns"], data["rows"] = data["first_columns"], data["first_rows"]
            self.private_statistics["backward_requests_restarted"] += 1
        while data["index"] < index:
            data["columns"] = km.multiply(api, data["step_plus"], data["columns"])
            data["rows"] = km.multiply(api, data["rows"], data["step_minus"])
            data["index"] += 1
            self.private_statistics["point_recurrence_steps"] += 1

        # Constant terms are the full signed midpoint products.  Only then
        # is the short scalar variation added.  The shared t and -t have
        # the same complete range, hence the same variation enclosure.
        X, Y, V = data["columns"], data["rows"], data["variation"]
        balanced_source = self._diagonal_left(data["balance"], source_matrix)
        output = self._diagonal_left(data["actual_S_over_B"],
            km.add(api, X, km.multiply(api, V, X)))
        source = km.add(api, km.multiply(api, Y, balanced_source),
                        km.product(api, Y, V, balanced_source))
        self.private_statistics["boxes_evaluated"] += 1
        left_indices, right_indices = tuple(range(core.P)), tuple(range(core.P, core.N))
        return {
            "OL": core.columns(km, output, left_indices),
            "OR": core.columns(km, output, right_indices),
            "IL": core.rows(km, source, left_indices),
            "IR": core.rows(km, source, right_indices),
        }

    def release(self):
        """Release the one private panel cache; no history is retained."""
        self.cache = None

    def current_remainder_infinity_upper(self):
        """One directed private tail bound, never a completed source norm."""
        self.core.require(self.cache is not None, "one prepared panel tail")
        return self.cache["remainder_infinity_upper"]


# Explicit adapters: the core Gram/projection formulas are unchanged.
def panel_gram_packet(provider, panel, cuts, source_role):
    """Whole-box integrals and both same-panel triangles; no sampled values.

    The cuts are exact fractions in [0,1] with both endpoints and strict
    increase.  Every integration box is evaluated on its whole continuum.
    All returned arrays are private inputs to a small complete norm result.
    """
    api, km, core, model = provider.api, provider.km, provider.core, provider.model
    core.require(list(cuts) == provider.cuts(panel),
                 "same whole uniform subbox plan as the factor provider")
    domain = model["context"].domain
    core.require(len(cuts) >= 2 and cuts[0] == domain.fzero and cuts[-1] == domain.fone
            and all(cuts[j] < cuts[j+1] for j in range(len(cuts)-1)),
            "one exact complete normalized panel partition")
    terms = []
    totals = {"IL": km.zeros(api, core.P, core.P), "IR": km.zeros(api, core.Q, core.Q),
              "OL": km.zeros(api, core.P, core.P), "OR": km.zeros(api, core.Q, core.Q)}
    length = domain.full_length(panel)
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        box = (panel, lo, hi)
        factors = provider.local_factors(box, core.source_matrix(api, km, model, box, source_role))
        grams = {"IL": core.source_gram(api, km, factors["IL"]),
                 "IR": core.source_gram(api, km, factors["IR"]),
                 "OL": core.output_gram(api, km, factors["OL"]),
                 "OR": core.output_gram(api, km, factors["OR"])}
        mass = length*domain.exact(hi-lo)
        core.require(api.lower(mass) > 0, "genuine positive ordinary-dr subbox mass")
        for name in totals:
            totals[name] = km.add(api, totals[name], km.scale(api, mass, grams[name]))
        terms.append({"mass_upper": core.positive_upper(api, mass), "grams": grams})
    triangle_left = api.zero
    triangle_right = api.zero
    for i, out in enumerate(terms):
        for j, source in enumerate(terms):
            if i < j:
                triangle_left += out["mass_upper"]*source["mass_upper"]*core.positive_upper(
                    api, core.trace_product(api, out["grams"]["OL"], source["grams"]["IL"]))
            elif i > j:
                triangle_right += out["mass_upper"]*source["mass_upper"]*core.positive_upper(
                    api, core.trace_product(api, out["grams"]["OR"], source["grams"]["IR"]))
            else:
                half_square = out["mass_upper"]*out["mass_upper"]/2
                triangle_left += half_square*core.positive_upper(
                    api, core.trace_product(api, out["grams"]["OL"], source["grams"]["IL"]))
                triangle_right += half_square*core.positive_upper(
                    api, core.trace_product(api, out["grams"]["OR"], source["grams"]["IR"]))
    return {"panel": panel, "source_role": source_role, "totals": totals,
            "private_model_token": model["private_model_token"],
            "same_panel_left_HS2_upper": core.positive_upper(api, triangle_left),
            "same_panel_right_HS2_upper": core.positive_upper(api, triangle_right),
            "complete_subboxes": len(terms)}


def whole_box_projection_bound(provider, panel, box, defect_packets,
                               defect_source_covariances, body_output_norm, epsilon):
    """Quantitative TRUE whole-box transversality after the strict low gate.

    Full local covariance integrals dominate their partial integrals in PSD
    order.  Thus this enclosure covers every point of box, not its endpoints.
    It is a separate point-receiver bound; an L2 input trace is never read.
    """
    api, km, core, model = provider.api, provider.km, provider.core, provider.model
    core.require(bool(epsilon < api.one) and box[0] == panel, "strict whole actual low coefficient gate")
    core.require_complete_packets(model, defect_packets, "true_coefficient_defect")
    core.require(defect_source_covariances["source_role"] == "true_coefficient_defect"
            and body_output_norm["source_role"] == "true_coefficient_defect"
            and defect_source_covariances["private_model_token"] is model["private_model_token"]
            and body_output_norm["private_model_token"] is model["private_model_token"]
            and bool(epsilon >= body_output_norm["body_norm_upper"]),
            "point certificate consumes the same complete actual-defect upper")
    Sinv = core.physical_weight(api, km, model, panel, inverse=True)
    factors = provider.local_factors(box, Sinv)
    totals = defect_packets[panel]["totals"]
    left_source = defect_source_covariances["left"][panel]
    right_source = km.add(api, defect_source_covariances["right"][panel], totals["IR"])
    receiver_gram = km.add(api, core.congruence(api, km, factors["OL"], left_source),
                          core.congruence(api, km, factors["OR"], right_source))
    receiver = core.positive_upper(api, api.sqrt(core.psd_operator_upper(api, receiver_gram)))
    # Output covariances depend only on S and the model; the source role used
    # to obtain them is irrelevant.  They include body only, no atom terms.
    left_output = km.add(api, body_output_norm["private_output_left_covariances"][panel], totals["OL"])
    right_output = body_output_norm["private_output_right_covariances"][panel]
    column_gram = km.add(api,
        core.congruence(api, km, km.transpose(factors["IL"]), left_output),
        core.congruence(api, km, km.transpose(factors["IR"]), right_output))
    column = core.positive_upper(api, api.sqrt(core.psd_operator_upper(api, column_gram)))
    left_projection = km.multiply(api, factors["OL"], factors["IL"])
    right_projection = km.multiply(api, factors["OR"], factors["IR"])
    model_projection = core.maximum_upper(api, [core.operator_upper(api, km, left_projection),
                                          core.operator_upper(api, km, right_projection)])
    total = core.positive_upper(api, model_projection + receiver*column/(api.one-epsilon).lower())
    q = model["context"].reference_qs[panel]
    Sbound = core.maximum_upper(api, [api.one, q])
    Sinvbound = core.maximum_upper(api, [api.one, api.one/q])
    raw_projection = core.positive_upper(api, Sbound*Sinvbound*total)
    angle = (api.one/(api.sqrt(api.rational(2))*raw_projection)).lower()
    core.require(api.lower(angle) > 0, "positive true whole-box combined-frame lower")
    return {"model_projection_upper": model_projection,
            "defect_point_receiver_upper": receiver,
            "model_point_column_upper": column,
            "actual_weighted_oblique_projection_upper": total,
            "actual_raw_oblique_projection_upper": raw_projection,
            "actual_raw_orthonormal_matching_singular_lower": angle,
            "covers_every_point_of_box": True, "whole_high_feedback_included": False}
