"""Same R141 parent source enclosures -> exact-cell covariance moments.

No imports, IO, entry point or scientific execution at import.  This
provider is only for the admitted fixed WVC context whose centre_matrix
uses one complete original packet per parent.  It caches that enclosing
ball, NOT a constant actual coefficient function.  Varying source roles
always use the pointwise PSD covariance majorant of the exact-moment core.

This file is a future integration adapter, not a change to an active run.
"""

SOURCE_ROLES = (
    "ordinary_raw_low_source",
    "transformed_low_source",
    "true_coefficient_defect",
    "low_second_kind_correction",
    "centre_high0_return_source",
)
CONSTANT_ROLES = ("ordinary_raw_low_source", "transformed_low_source")


def require(ok, message):
    if not ok:
        raise ValueError(message)


class ParentMomentProvider:
    """One current parent template and one current refined-cell frame.

    A defect pass prepares155 parent/source moments.  After its strict
    gate, the four-role pass prepares at most4 moments per parent.  All
    refined cells still use their independent certified node carriers.
    """

    def __init__(self, api, km, green, moment, model, degree=24):
        require(model.get("comparison_BVP_verified") is True
                and model.get("same_exact_parent_midpoint_model") is True,
                "complete same-model refined R141 BVP")
        context = model["context"]
        require(hasattr(context, "original")
                and hasattr(model["generators"], "parents")
                and len(context.original.domain.cells) == 155
                and len(model["generators"].parents) == 155,
                "same155 comparison parents, not a new coefficient mesh")
        for flag in ("same_WVC_reference", "same_actual_S_and_all_seven_ports",
                     "all_coefficient_pieces_and_raw_identity_transmissions",
                     "true_signed_collar_not_zero_reference_packet",
                     "ordinary_dr_pairing_and_complete_Gf_atoms"):
            require(context.qualifications[flag] is True,
                    "original complete coefficient qualification: "+flag)
        self.api, self.km, self.green, self.moment = api, km, green, moment
        self.model, self.degree = model, degree
        self.original = context.original
        self.parent_key = self.template = self.cell_cache = None
        self.role_cache = {}
        self.actual_low = self.Sinv = self.reference_low = None
        self.statistics = {
            "parent_templates_prepared": 0,
            "complete_parent_source_covariances_prepared": 0,
            "parent_source_moment_reuses": 0,
            "complete_parent_low_matrices_prepared": 0,
            "complete_parent_high_return_matrices_prepared": 0,
            "independent_refined_frames_prepared": 0,
            "source_roles_evaluated": 0,
            "source_parent_cache_cap": len(SOURCE_ROLES),
            "maximum_live_parent_templates": 1,
            "maximum_live_refined_frame_caches": 1,
            "actual_coefficient_variation_removed": False,
        }

    def _prepare_parent(self, panel):
        cell = self.model["context"].domain.cells[panel]
        key = cell["parent_panel"], cell["count"]
        if self.parent_key == key:
            return
        balance = self.model["refined_plan"]["balances"][key[0]]
        self.template = self.moment.prepare_model_template(
            self.api, self.km, self.green, self.model, panel, balance, self.degree)
        self.parent_key = key
        self.role_cache = {}
        self.actual_low = self.Sinv = self.reference_low = None
        self.cell_cache = None
        self.statistics["parent_templates_prepared"] += 1

    def _inverse_weight(self):
        if self.Sinv is None:
            api, km = self.api, self.km
            parent = self.parent_key[0]
            q = self.original.reference_qs[parent]
            require(api.lower(q) > 0, "same original positive q")
            entries = [api.one if component == 0 else api.one/q
                       for component, _ in self.green.HEAD]
            self.Sinv = km.Matrix(193, 193, [
                [entries[i] if i == j else api.zero for j in range(193)]
                for i in range(193)])
        return self.Sinv

    def _complete_low_matrix(self):
        if self.actual_low is None:
            parent = self.parent_key[0]
            box = self.original.domain.whole_cell_box(parent)
            self.actual_low = self.original.centre_matrix(
                self.green.HEAD, self.green.HEAD, box)
            require(self.actual_low.shape == (193, 193),
                    "complete parent low193 and independent mean")
            self.statistics["complete_parent_low_matrices_prepared"] += 1
        return self.actual_low

    def _complete_reference_matrix(self):
        if self.reference_low is None:
            api, km = self.api, self.km
            parent = self.parent_key[0]
            eta = self.original.reference_etas[parent]
            q = self.original.reference_qs[parent]
            diagonal = self.original.reference_diagonals[parent]
            values = []
            for oc, j in self.green.HEAD:
                row = []
                for ic, k in self.green.HEAD:
                    value = api.zero
                    if j == k and j:
                        if oc != ic:
                            value = 4*j*eta*(q*q if oc == 0 else api.one)
                        else:
                            value = diagonal[j] if oc == 0 else -diagonal[j]
                    row.append(value)
                values.append(row)
            self.reference_low = km.Matrix(193, 193, values)
        return self.reference_low

    def _complete_source_ball(self, role):
        """Same whole parent matrix ball, not a point evaluation.

        For defect, (H_parent/n)/(h_parent/n) = H_parent/h_parent exactly.
        Using the parent ratio avoids two independently rounded divisions
        while retaining the same genuine uncertain physical length.
        """
        api, km, parent = self.api, self.km, self.parent_key[0]
        if role == "ordinary_raw_low_source":
            return km.eye(api, 193)
        if role == "transformed_low_source":
            return self._inverse_weight()
        if role == "centre_high0_return_source":
            self.statistics["complete_parent_high_return_matrices_prepared"] += 1
            return self.original.centre_matrix(self.green.HEAD, self.green.HIGH0,
                self.original.domain.whole_cell_box(parent))
        actual = self._complete_low_matrix()
        if role == "true_coefficient_defect":
            length = self.original.domain.full_length(parent)
            require(api.lower(length) > 0, "same TRUE complete parent length")
            comparison = km.scale(api, api.one/length,
                                    self.model["generators"].parents[parent])
        elif role == "low_second_kind_correction":
            comparison = self._complete_reference_matrix()
        else:
            raise ValueError("undeclared original source role: "+str(role))
        difference = km.add(api, actual, km.scale(api, -api.one, comparison))
        return km.multiply(api, difference, self._inverse_weight())

    def _moments(self, role):
        require(role in SOURCE_ROLES, "one of the five complete original roles")
        if role in self.role_cache:
            self.statistics["parent_source_moment_reuses"] += 1
            return self.role_cache[role]
        source = self._complete_source_ball(role)
        covariance = self.moment.model_source_covariance(
            self.api, self.km, self.template, source, constant=role in CONSTANT_ROLES)
        result = self.moment.source_moments(
            self.api, self.km, self.template, covariance)
        self.role_cache[role] = result
        require(len(self.role_cache) <= len(SOURCE_ROLES),
                "bounded current-parent source cache")
        self.statistics["complete_parent_source_covariances_prepared"] += 1
        return result

    def _prepare_cell(self, panel):
        if self.cell_cache is not None and self.cell_cache["panel"] == panel:
            return self.cell_cache
        api, km, core, moment = self.api, self.km, self.green, self.moment
        node = self.model["nodes"][panel]
        diagonal, inverse = self.template["diagonal"], self.template["inverse_diagonal"]
        L = moment._diagonal_left(km, diagonal, node["left"])
        R = moment._diagonal_left(km, diagonal, node["right"])
        ell = moment._diagonal_right(km, node["ell"], inverse)
        rho = moment._diagonal_right(km, node["rho"], inverse)
        OL = core.congruence(api, km, km.transpose(L), self.template["U"])
        OR = core.congruence(api, km, km.transpose(R), self.template["U"])
        length = self.model["context"].domain.full_length(panel)
        require(api.lower(length) > 0, "same genuine refined-cell length")
        self.cell_cache = {"panel": panel, "L": L, "ell": ell, "rho": rho,
            "OL_unscaled": OL, "OL": km.scale(api, length, OL),
            "OR": km.scale(api, length, OR), "length": length}
        self.statistics["independent_refined_frames_prepared"] += 1
        return self.cell_cache

    def packet(self, panel, source_role):
        """Whole-cell packet compatible with original PackedPackets.

        The metadata has ONE signed sum of both triangles. A future owner
        must use the new norm accumulator; it must not insert a fake zero
        under the old right-triangle key to satisfy an old schema.
        """
        self._prepare_parent(panel)
        moments = self._moments(source_role)
        cell = self._prepare_cell(panel)
        api, km, core, moment = self.api, self.km, self.green, self.moment
        IL = core.congruence(api, km, cell["ell"], moments["Z"])
        IR = core.congruence(api, km, cell["rho"], moments["Z"])
        rectangle = core.trace_product(api, cell["OL_unscaled"], IL)
        cross = moment._frobenius_inner(api, cell["L"],
            km.multiply(api, moments["Y"], km.transpose(cell["ell"])))
        same = rectangle+moment._trace(api, moments["Y"])-2*cross
        length = cell["length"]
        totals = {"OL": cell["OL"], "OR": cell["OR"],
                  "IL": km.scale(api, length, IL), "IR": km.scale(api, length, IR)}
        self.statistics["source_roles_evaluated"] += 1
        return {"panel": panel, "source_role": source_role, "totals": totals,
                "private_model_token": self.model["private_model_token"],
                "same_panel_complete_HS2_upper":
                    core.positive_upper(api, length*length*same),
                "same_panel_both_triangles_in_signed_complete_sum": True,
                "true_cell_length_retained": True,
                "whole_cell_covariance_moment_contract": "R141_GM1_through17",
                "whole_parent_source_covariance_reused": True,
                "varying_source_was_treated_as_constant": False}

    def release_parent(self):
        """Drop private matrices before a later phase, never a saved scalar."""
        self.parent_key = self.template = self.cell_cache = None
        self.actual_low = self.Sinv = self.reference_low = None
        self.role_cache = {}
