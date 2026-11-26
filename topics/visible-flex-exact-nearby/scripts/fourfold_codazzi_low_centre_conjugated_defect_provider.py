"""R149 whole-box conjugated defect with a single parent cache.

Pure definitions only: no import, IO, entry point, or numerical execution.
This is the SAME true coefficient defect, with S cancelled analytically
before interval products.  The whole-parent coefficient ball encloses a
varying function; it is never integrated as a constant unknown matrix.
Every private node frame, true cell length, mean row and both boundaries
remain those of the original complete refined R141/R142 comparison model.
"""

N = 193
LEFT = 97
RIGHT = 96


def require(ok, message):
    if not ok:
        raise ValueError(message)


def _diagonal_left(km, entries, matrix):
    require(len(entries) == matrix.rows, "whole exact left diagonal")
    return km.Matrix(matrix.rows, matrix.cols,
        [[entries[i]*value for value in row]
         for i, row in enumerate(matrix.values)])


def _diagonal_right(km, matrix, entries):
    require(len(entries) == matrix.cols, "whole exact right diagonal")
    return km.Matrix(matrix.rows, matrix.cols,
        [[value*entries[j] for j, value in enumerate(row)]
         for row in matrix.values])


def _infinity_upper(api, green, matrix):
    """Directed bound for the induced matrix infinity norm."""
    return green.maximum_upper(api, [
        sum((api.magnitude(value) for value in row), api.zero).upper()
        for row in matrix.values])


def _commutator_template(api, km, green, generator, defect, degree):
    """Uniform enclosure of exp(-tau H) Delta exp(tau H), 0<=tau<=1.

    D=H/2, C=exp(-D) Delta exp(D), P_0=C,
    P_k=(P_(k-1) D-D P_(k-1))/k.
    At t=2*tau-1 the same-point matrix is sum t^k P_k plus its
    complete tail.  q=2||D||_infinity and q/(degree+2)<1 give
    tail <= ||C||_infinity q^(degree+1)/(degree+1)!
                 /(1-q/(degree+2)).
    This bounds every entry, uniformly for ALL Delta in the parent ball.
    """
    require(type(degree) is int and degree >= 1, "declared finite Taylor degree")
    D = km.scale(api, api.rational(1, 2), generator)
    plus = green.directed_exp(api, km, D, api.one)
    minus = green.directed_exp(api, km, D, -api.one)
    centre = km.product(api, minus, defect, plus)
    require(all(value.is_finite() for row in centre.values for value in row),
            "finite whole midpoint-conjugated varying-defect set")
    q = (2*_infinity_upper(api, green, D)).upper()
    require(api.lower(q) >= 0 and bool(q < api.rational(degree+2)),
            "strict geometric tail ratio for the whole signed commutator")
    coefficients = [centre]
    power = centre
    for k in range(1, degree+1):
        power = km.scale(api, api.rational(1, k),
            km.add(api, km.multiply(api, power, D),
                   km.scale(api, -api.one, km.multiply(api, D, power))))
        require(all(value.is_finite() for row in power.values for value in row),
                "complete finite signed commutator coefficient")
        coefficients.append(power)
    first_tail = api.one
    for k in range(1, degree+2):
        first_tail = (first_tail*q/k).upper()
    ratio_gap = (api.one-q/(degree+2)).lower()
    require(api.lower(ratio_gap) > 0, "positive full commutator-tail denominator")
    tail = (_infinity_upper(api, green, centre)*first_tail/ratio_gap).upper()
    require(tail.is_finite() and api.lower(tail) >= 0,
            "whole nonnegative uniform entrywise commutator remainder")
    return coefficients, tail, q


def _whole_conjugated_box(api, km, domain, coefficients, tail, lo, hi):
    """Horner on the ONE common scalar t, followed by the complete tail."""
    t = api.interval(domain.exact(2*lo-domain.fone),
                     domain.exact(2*hi-domain.fone))
    result = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        result = km.add(api, coefficient, km.scale(api, t, result))
    remainder = api.interval(-tail, tail)
    result = km.Matrix(N, N, [[value+remainder for value in row]
                              for row in result.values])
    require(all(value.is_finite() for row in result.values for value in row),
            "complete whole-box same-scalar conjugated defect")
    return result


class ParentConjugatedDefectProvider:
    """One parent four-box cache; every original refined frame is separate.

    A cached Z_j encloses B exp(-tau H_i) Delta(r) exp(tau H_i) B^-1
    for every point of subbox j of every refined cell in that parent.
    Delta(r)=Atrue(r)-H_parent/h_parent retains the actual TRUE h_parent.
    Only this pointwise enclosure is reused.  No coefficient dependence,
    cell, output component, or source direction is deleted.
    """

    def __init__(self, api, km, green, loop, model, subboxes=4, degree=24):
        count = loop.validate_model(model)
        context = model["context"]
        require(model.get("same_exact_parent_midpoint_model") is True
                and hasattr(context, "original")
                and hasattr(model["generators"], "parents")
                and len(context.original.domain.cells) == 155
                and len(model["generators"].parents) == 155,
                "same complete155-parent R141/R142 model")
        require(type(subboxes) is int and subboxes > 0
                and type(degree) is int and degree >= 1, "complete declared local plan")
        self.api, self.km, self.green, self.loop = api, km, green, loop
        self.model, self.original = model, context.original
        self.subboxes, self.degree = subboxes, degree
        self.parent_key = self.parent_cache = self.cell_cache = None
        self.statistics = {
            "parent_conjugated_templates_prepared": 0,
            "whole_parent_defect_matrices_prepared": 0,
            "whole_conjugated_subboxes_prepared": 0,
            "independent_refined_frames_prepared": 0,
            "complete_signed_cell_packets": 0,
            "maximum_live_parent_templates": 1,
            "maximum_live_refined_frames": 1,
            "conjugated_boxes_per_parent": subboxes,
            "shared_scalar_commutator_Taylor_degree": degree,
            "varying_source_treated_as_constant": False,
            "actual_S_replaced_by_internal_balance": False,
            "physical_S_cancelled_only_in_same_point_crosses": True,
            "comparison_cells": count,
        }

    def cuts(self, panel):
        require(type(panel) is int
                and 0 <= panel < len(self.model["generators"]), "one actual cell")
        one = self.model["context"].domain.fone
        return [one*j/self.subboxes for j in range(self.subboxes+1)]

    def _prepare_parent(self, panel):
        api, km, green, model = self.api, self.km, self.green, self.model
        cell = model["context"].domain.cells[panel]
        key = cell["parent_panel"], cell["count"]
        if self.parent_key == key:
            return
        parent, count = key
        require(type(parent) is int and 0 <= parent < 155
                and type(count) is int and count > 0,
                "whole declared original-parent affine refinement")
        qb = model["refined_plan"]["balances"][parent]
        require(qb.is_finite() and qb.lower() == qb.upper()
                and api.lower(qb) > 0, "same strictly positive exact dyadic balance")
        diagonal, inverse = [api.one]*96+[qb]*97, [api.one]*96+[api.one/qb]*97
        length = self.original.domain.full_length(parent)
        require(length.is_finite() and api.lower(length) > 0,
                "whole positive true original-parent length")
        actual = self.original.centre_matrix(
            green.HEAD, green.HEAD, self.original.domain.whole_cell_box(parent))
        require(actual.shape == (N, N), "all193 original components including mean")
        comparison = km.scale(api, api.one/length, model["generators"].parents[parent])
        delta = km.add(api, actual, km.scale(api, -api.one, comparison))
        balanced_delta = _diagonal_right(km,
            _diagonal_left(km, diagonal, delta), inverse)
        balanced_generator = _diagonal_right(km,
            _diagonal_left(km, diagonal, model["generators"][panel]), inverse)
        coefficients, tail, q = _commutator_template(
            api, km, green, balanced_generator, balanced_delta, self.degree)
        cuts = self.cuts(panel)
        domain = model["context"].domain
        boxes = [_whole_conjugated_box(api, km, domain, coefficients, tail, lo, hi)
                 for lo, hi in zip(cuts[:-1], cuts[1:])]
        self.parent_key = key
        self.parent_cache = {"diagonal": diagonal, "inverse": inverse,
                             "boxes": boxes, "tail_upper": tail, "q_upper": q}
        self.cell_cache = None
        self.statistics["parent_conjugated_templates_prepared"] += 1
        self.statistics["whole_parent_defect_matrices_prepared"] += 1
        self.statistics["whole_conjugated_subboxes_prepared"] += len(boxes)

    def _prepare_cell(self, panel):
        if self.cell_cache is not None and self.cell_cache["panel"] == panel:
            return self.cell_cache
        node = self.model["nodes"][panel]
        cache, km = self.parent_cache, self.km
        cell = {
            "panel": panel,
            "L": _diagonal_left(km, cache["diagonal"], node["left"]),
            "R": _diagonal_left(km, cache["diagonal"], node["right"]),
            "ell": _diagonal_right(km, node["ell"], cache["inverse"]),
            "rho": _diagonal_right(km, node["rho"], cache["inverse"]),
        }
        require(cell["L"].shape == (N, LEFT) and cell["R"].shape == (N, RIGHT)
                and cell["ell"].shape == (LEFT, N)
                and cell["rho"].shape == (RIGHT, N),
                "all original independent complementary signed node frames")
        self.cell_cache = cell
        self.statistics["independent_refined_frames_prepared"] += 1
        return cell

    def packet(self, panel):
        """R149 core packet, with signed true masses and both local branches."""
        self._prepare_parent(panel)
        cell = self._prepare_cell(panel)
        api, km, loop, model = self.api, self.km, self.loop, self.model
        domain = model["context"].domain
        length = domain.full_length(panel)
        require(length.is_finite() and api.lower(length) > 0,
                "whole actual refined-cell length, not its upper endpoint")
        cuts = self.cuts(panel)
        a, b = km.zeros(api, RIGHT, LEFT), km.zeros(api, LEFT, RIGHT)
        terms = []
        for Z, lo, hi in zip(self.parent_cache["boxes"], cuts[:-1], cuts[1:]):
            domain.validate_box((panel, lo, hi))
            A = km.product(api, cell["rho"], Z, cell["L"])
            B = km.product(api, cell["ell"], Z, cell["R"])
            require(loop.finite_matrix(A) and loop.finite_matrix(B),
                    "complete signed same-point crosses after exact S cancellation")
            mass = length*domain.exact(hi-lo)
            require(api.lower(mass) > 0, "whole positive signed ordinary-dr mass")
            a = km.add(api, a, km.scale(api, mass, A))
            b = km.add(api, b, km.scale(api, mass, B))
            terms.append((mass, A, B))
        triangle = api.zero
        for earlier, (mass_s, A, _) in enumerate(terms):
            triangle += (mass_s*mass_s/2)*loop.rectangular_trace(
                api, A, terms[earlier][2])
            for later in range(earlier+1, len(terms)):
                mass_r, _, B = terms[later]
                triangle += mass_s*mass_r*loop.rectangular_trace(api, A, B)
        require(triangle.is_finite() and loop.finite_matrix(a)
                and loop.finite_matrix(b), "complete signed whole-cell integrals")
        self.statistics["complete_signed_cell_packets"] += 1
        return {
            "panel": panel, "source_role": "true_coefficient_defect",
            "private_model_token": model["private_model_token"],
            "a_source_earlier": a, "b_output_later": b,
            "same_cell_ordered_loop_integral": triangle,
            "complete_subboxes": len(terms),
            "whole_closed_source_boxes_used": True,
            "signed_true_dr_masses_used": True,
            "same_cell_ordered_triangle_complete": True,
            "actual_coefficient_variation_retained": True,
            "mean_and_all_193_components_retained": True,
            "same_scalar_conjugated_defect_boxes_used": True,
        }

    def release_parent(self):
        self.parent_key = self.parent_cache = self.cell_cache = None
