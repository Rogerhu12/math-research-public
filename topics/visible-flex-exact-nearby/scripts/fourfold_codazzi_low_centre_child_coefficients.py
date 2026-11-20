"""Genuine whole-child signed coefficients for the unchanged R141 hybrid.

Pure definitions only: no numerical import, IO, entry point, producer call,
or scientific work at import.  A future public consumer supplies the already
admitted4650 rows, exact candidate reader, full repair, original WVC context,
and the unchanged original/refined evaluation context.

The actual full-family eta is retained.  Old intrinsic and independent-mean
balls are restricted as sets, never divided by a subdivision count.  Each
closed child/old-row intersection is assembled BEFORE the matrices are
hulled.  All primitive intermediates and the independent mean row remain.

This provider does not mutate either context or any comparison generator.
It is not the parent-cached moment provider: its three varying source roles
must be cached by the complete CHILD box, not merely by the parent index.
"""

from bisect import bisect_left
from fractions import Fraction


HEAD = (tuple((0, j) for j in range(1, 97)) + ((1, 0),)
        + tuple((1, j) for j in range(1, 97)))
HIGH0 = tuple((0, j) for j in range(97, 161)) + tuple((1, j) for j in range(97, 161))
ROLES = ("ordinary_raw_low_source", "transformed_low_source",
         "true_coefficient_defect", "low_second_kind_correction",
         "centre_high0_return_source")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def signed_upper(api, value):
    return -api.lower(-value)


def intersection(api, first, second, name):
    """Outward enclosure of a nonempty intersection of signed real balls."""
    lo = max(api.lower(first), api.lower(second))
    hi = min(signed_upper(api, first), signed_upper(api, second))
    require(lo <= hi, "nonempty same-function child intersection: " + name)
    return api.interval(lo, hi)


def matrix_hull(api, km, first, second):
    require(first.shape == second.shape, "whole same-shaped signed matrix hull")
    return km.Matrix(first.rows, first.cols, [
        [api.hull([first.values[i][j], second.values[i][j]])
         for j in range(first.cols)] for i in range(first.rows)])


def matrix_intersection(api, km, first, second):
    require(first.shape == second.shape, "whole same-shaped signed intersection")
    return km.Matrix(first.rows, first.cols, [
        [intersection(api, first.values[i][j], second.values[i][j],
                      "signed matrix entry")
         for j in range(first.cols)] for i in range(first.rows)])


class WholeChildSignedCoefficientProvider:
    """Bounded-memory explicit source provider; no implicit monkeypatching.

    original_context is the admitted155-panel context.  evaluation_context
    is either that context or its exact refined context.  to_original_box
    maps a complete evaluation-domain box to its ORIGINAL155-panel box;
    use refined.domain.to_parent_box for the existing refined adapter, or
    lambda box: box when the two domains agree.  Physical covers are checked
    to agree exactly; a child is never substituted for its parent or for the
    true interval length.

    Only one current child's two signed matrices and one original panel's
    two comparison enclosures are cached.  The original4650 input rows are
    read-only; no child matrix or coefficient array is a public artifact.
    """

    def __init__(self, api, km, green, assembly, collar, admitted,
                 original_context, evaluation_context, to_original_box):
        require(admitted.get("collar_inputs_verified") is True,
                "whole original collar/body admission precedes child bounds")
        require(len(admitted["rows"]) == 4650
                and len(admitted["repair_suprema"]) == 65
                and len(original_context.domain.cells) == 155,
                "same4650 body rows,65 repair components,155 comparison panels")
        require(evaluation_context is original_context
                or getattr(evaluation_context, "original", None) is original_context,
                "evaluation context is this original context or its direct exact refinement")
        require(tuple(green.HEAD) == HEAD and tuple(green.HIGH0) == HIGH0,
                "same193 coordinates and128 high-return columns")
        for name in ("same_WVC_reference", "same_actual_S_and_all_seven_ports",
                     "all_coefficient_pieces_and_raw_identity_transmissions",
                     "true_signed_collar_not_zero_reference_packet",
                     "ordinary_dr_pairing_and_complete_Gf_atoms"):
            require(original_context.qualifications[name] is True,
                    "same original coefficient qualification: " + name)
        self.api, self.km, self.green = api, km, green
        self.assembly, self.collar, self.admitted = assembly, collar, admitted
        self.original, self.context = original_context, evaluation_context
        self.domain = evaluation_context.domain
        self.to_original_box = to_original_box
        self.rows = admitted["rows"]
        self.intervals = [tuple(map(Fraction, row["interval"])) for row in self.rows]
        self.rights = [right for _, right in self.intervals]
        require(all(left < right for left, right in self.intervals)
                and all(self.intervals[i][1] == self.intervals[i+1][0]
                        for i in range(len(self.intervals)-1)),
                "complete unchanged positive-body row cover")
        self.child_key = self.parent_key = None
        self.child_matrices, self.parent_matrices = {}, {}
        self.statistics = {
            "complete_child_low_matrices": 0,
            "complete_child_high_return_matrices": 0,
            "closed_body_intersections_assembled": 0,
            "closed_zero_length_endpoint_intersections": 0,
            "true_root_child_packets": 0,
            "child_family_speed_intersections": 0,
            "maximum_live_child_matrix_caches": 2,
            "maximum_live_parent_matrix_caches": 2,
            "intrinsic_balls_narrowed_without_new_evidence": False,
            "family_parameter_radius_changed": False,
            "old_scientific_targets_called": 0,
        }

    def clear_cache(self):
        self.child_key = self.parent_key = None
        self.child_matrices, self.parent_matrices = {}, {}

    def _box(self, box):
        self.domain.validate_box(box)
        original_box = self.to_original_box(box)
        self.original.domain.validate_box(original_box)
        cover = tuple(self.domain.exact_physical_cover(box))
        require(cover == tuple(self.original.domain.exact_physical_cover(original_box)),
                "child and original normalized coordinates have the same true cover")
        key = self.domain.cache_key(box)
        if key != self.child_key:
            self.child_key, self.child_matrices = key, {}
        panel = self.original.domain.cell_index(original_box)
        if panel != self.parent_key:
            self.parent_key, self.parent_matrices = panel, {}
        return panel, cover

    def _body_intersections(self, cover):
        left, right = cover
        require(self.intervals[0][0] <= left <= right <= self.intervals[-1][1],
                "whole child cover remains in the admitted positive body")
        index = bisect_left(self.rights, left)
        covered, count = left, 0
        while index < len(self.rows) and self.intervals[index][0] <= right:
            old_left, old_right = self.intervals[index]
            lo, hi = max(left, old_left), min(right, old_right)
            if lo <= hi:
                require(lo <= covered, "no omitted child/old-row intersection")
                covered = max(covered, hi)
                count += 1
                yield index, lo, hi
            index += 1
        require(count > 0 and covered == right, "complete closed child coefficient cover")

    def _body_packet(self, index, left, right, tighten_eta):
        api, row = self.api, self.rows[index]
        intrinsic = row["original_intrinsic_enclosure"]
        ui, vr = self.assembly._body_centre_fields(
            self.admitted["cubic"], self.admitted["repair_suprema"],
            row["original_candidate_piece"], left, right, intrinsic, api)
        beta, K, gamma = (api.old_interval(intrinsic[name])
                          for name in ("beta", "K", "gamma"))
        eta = api.old_interval(row["complete_delta_bounds"]["radial_speed"])
        require(api.lower(K) > 0 and api.lower(gamma) > 0 and api.lower(eta) > 0,
                "unchanged true positive-body signs")
        family_mean = None
        if tighten_eta:
            em = api.magnitude(api.old_interval(row["independent_mean_variation_bound"]))
            family_mean = intersection(
                api, vr[0] + api.interval(-em, em),
                api.old_interval(row["complete_delta_bounds"]["mean_v"]),
                "same full-family child mean")
            eta = intersection(api, -gamma*family_mean, eta,
                               "eta_delta=-gamma*m_delta on the child")
            require(api.lower(eta) > 0, "strict original full-family child speed")
            self.statistics["child_family_speed_intersections"] += 1
        packet = self.collar._complete_centre_packet(
            ui, vr, beta, K, gamma, eta, api.zero)
        # mc remains the repaired-centre mean; never replace it by family_mean.
        if family_mean is not None:
            packet["whole_child_family_mean"] = family_mean
        return packet

    def _root_packet(self, cover, tighten_eta):
        packet = self.collar.complete_true_collar_packet(
            self.admitted, self.api, radial_interval=cover)
        if tighten_eta:
            eta = intersection(self.api, -packet["gamma"]*packet["family_mean"],
                               packet["actual_eta"], "same true-collar family speed")
            require(self.api.lower(eta) > 0, "strict original true-collar optical speed")
            packet["eta"] = packet["actual_eta"] = eta
            self.statistics["child_family_speed_intersections"] += 1
        self.statistics["true_root_child_packets"] += 1
        return packet

    def _signed_matrix(self, packet, outputs, inputs):
        return self.assembly._complete_signed_centre_matrix(
            self.api, self.km, self.collar, packet, outputs, inputs,
            self.original.sqrt_two)

    def _parent_matrix(self, outputs, inputs):
        key = (outputs, inputs)
        if key not in self.parent_matrices:
            whole = self.original.domain.whole_cell_box(self.parent_key)
            self.parent_matrices[key] = self.original.centre_matrix(outputs, inputs, whole)
        return self.parent_matrices[key]

    def centre_matrix(self, outputs, inputs, box):
        outputs, inputs = tuple(outputs), tuple(inputs)
        require(outputs == HEAD and inputs in (HEAD, HIGH0),
                "only complete AL193 or complete CHL193-by128, no projection change")
        panel, cover = self._box(box)
        key = (outputs, inputs)
        if key in self.child_matrices:
            return self.child_matrices[key]
        tighten_eta = inputs == HEAD
        result = None
        if panel == 0:
            result = self._signed_matrix(self._root_packet(cover, tighten_eta), outputs, inputs)
        else:
            for index, left, right in self._body_intersections(cover):
                packet = self._body_packet(index, left, right, tighten_eta)
                block = self._signed_matrix(packet, outputs, inputs)
                result = block if result is None else matrix_hull(self.api, self.km, result, block)
                self.statistics["closed_body_intersections_assembled"] += 1
                if left == right:
                    self.statistics["closed_zero_length_endpoint_intersections"] += 1
        require(result is not None and result.shape == (193, len(inputs)),
                "complete signed child matrix before any absolute value")
        result = matrix_intersection(self.api, self.km, result,
                                     self._parent_matrix(outputs, inputs))
        require(all(value.is_finite() for row in result.values for value in row),
                "finite complete signed child source")
        if inputs == HIGH0:
            require(all(self.api.lower(value) == 0 and signed_upper(self.api, value) == 0
                        for value in result.values[96]),
                    "retained mean output is identically zero by full degree32 support")
            self.statistics["complete_child_high_return_matrices"] += 1
        else:
            self.statistics["complete_child_low_matrices"] += 1
        self.child_matrices[key] = result
        return result

    def source_matrix(self, model, box, role):
        """Same five source units, with explicit child evaluation for three roles.

        Complete Green/atom/Neumann claims still belong to the unchanged
        R141 theorem and a future fully completed scientific target.  This
        method itself grants none of those claims.
        """
        require(role in ROLES and model["context"] is self.context,
                "same model context and one declared complete source role")
        self.domain.validate_box(box)
        api, km, green = self.api, self.km, self.green
        index = self.domain.cell_index(box)
        if role == "ordinary_raw_low_source":
            return km.eye(api, 193)
        if role == "centre_high0_return_source":
            return self.centre_matrix(HEAD, HIGH0, box)
        Sinv = green.physical_weight(api, km, model, index, inverse=True)
        if role == "transformed_low_source":
            return Sinv
        actual = self.centre_matrix(HEAD, HEAD, box)
        if role == "true_coefficient_defect":
            length = self.domain.full_length(index)
            require(api.lower(length) > 0, "true child length, not padded-cover width")
            difference = km.add(api, actual,
                                km.scale(api, -api.one/length, model["generators"][index]))
            return km.multiply(api, difference, Sinv)
        eta, q = self.context.reference_etas[index], self.context.reference_qs[index]
        diagonal = self.context.reference_diagonals[index]
        values = []
        for oc, j in HEAD:
            row = []
            for ic, k in HEAD:
                value = api.zero
                if j == k and j:
                    if oc != ic:
                        value = 4*j*eta*(q*q if oc == 0 else api.one)
                    else:
                        value = diagonal[j] if oc == 0 else -diagonal[j]
                row.append(value)
            values.append(row)
        reference = km.Matrix(193, 193, values)
        return km.multiply(api, km.add(api, actual, km.scale(api, -api.one, reference)), Sinv)
