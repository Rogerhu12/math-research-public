"""Fixed parent midpoint plus true-child radius covariance moments.

Pure definitions only: no import, IO, public owner, entry point, numerical
library, model mutation, or work at import.  This is a separate provider;
it does not modify the active R142 or the earlier full-diagonal provider.

For the EXACT original GM parent midpoint M and original GM diagonal D,
all true child sources obey U U^T <= M M^T + sigma D <= M M^T + D.
Only the covariance ERROR is scaled.  A zero entry of D does not delete
the corresponding, possibly nonzero, constant midpoint row.

Each varying role uses at most two dense source-moment preparations per
parent: C=M M^T and D.  Child Z/Y are their linear combination; the output
moment U, every independent node frame, all input columns, true h/h^2,
and both signed Green triangles are unchanged.  The exact PSD comparison
does not promise smaller final interval scalars or an elapsed-time bound.
"""

N = 193
CONSTANT_ROLES = ("ordinary_raw_low_source", "transformed_low_source")
VARYING_ROLES = ("true_coefficient_defect", "low_second_kind_correction",
                 "centre_high0_return_source")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def _point_upper(api, value):
    require(value.is_finite(), "finite directed scalar")
    point = value.upper()
    require(point.is_finite() and point.lower() == point.upper()
            and api.lower(point) >= 0, "fixed nonnegative upper endpoint")
    return point


def _absolute_column_sums(api, rows):
    require(len(rows) == N and rows and rows[0]
            and all(len(row) == len(rows[0]) for row in rows),
            "all193 rows and all independent source columns")
    require(all(value.is_finite() and value.lower() == value.upper()
                and api.lower(value) >= 0 for row in rows for value in row),
            "fixed nonnegative entrywise bounds")
    return [_point_upper(api, sum((rows[i][j] for i in range(N)), api.zero))
            for j in range(len(rows[0]))]


def _covariance_error_rows(api, absolute_midpoint, radius, midpoint_columns):
    """Outward rows of (|M|R^T+R|M|^T+R R^T)1 in O(193 times columns)."""
    radius_columns = _absolute_column_sums(api, radius)
    columns = len(radius_columns)
    require(len(absolute_midpoint) == N and len(midpoint_columns) == columns
            and all(len(row) == columns for row in absolute_midpoint),
            "same entire midpoint and radius source shape")
    result = []
    for i in range(N):
        result.append(_point_upper(api, sum((
            absolute_midpoint[i][j]*radius_columns[j]
            + radius[i][j]*midpoint_columns[j]
            + radius[i][j]*radius_columns[j]
            for j in range(columns)), api.zero)))
    return result


def _relative_error_scale(api, diagonal, rows):
    """Scale the covariance error only, including exact zero error support."""
    require(len(diagonal) == len(rows) == N, "whole193 error diagonal and row bounds")
    sigma = api.zero
    for denominator, numerator in zip(diagonal, rows):
        require(denominator.is_finite() and denominator.lower() == denominator.upper()
                and api.lower(denominator) >= 0
                and numerator.is_finite() and numerator.lower() == numerator.upper()
                and api.lower(numerator) >= 0,
                "finite exact nonnegative error row and original GM diagonal")
        if bool(denominator == api.zero):
            require(bool(numerator == api.zero),
                    "zero parent covariance-error support remains exact in the child")
            continue
        require(api.lower(denominator) > 0, "division only on positive error support")
        ratio = _point_upper(api, numerator/denominator)
        if bool(ratio > sigma):
            sigma = ratio
    # The whole parent error D and sigma_hat D separately dominate the
    # true child error.  This scalar cap uses the same one fixed D.
    return api.one if bool(sigma >= api.one) else sigma


def original_GM_midpoint_radius_split(api, km, moment, source_box):
    """The SAME M,R,d_i definition and operation order as GM.15.

    Do not recover d_i by subtracting interval diagonal entries of V and
    M M^T: that would not identify the original fixed d_i.  The following
    midpoint, radii, cross products and row-upper operations reproduce
    whole_source_covariance_majorant before its final addition exactly.
    All full input columns are retained; source_box is the balanced ball.
    """
    require(moment.N == N and source_box.rows == N and source_box.cols > 0
            and len(source_box.values) == N
            and all(len(row) == source_box.cols for row in source_box.values)
            and all(entry.is_finite() for row in source_box.values for entry in row),
            "whole original finite balanced source box")
    midpoint = km.Matrix(N, source_box.cols,
        [[entry.mid() for entry in row] for row in source_box.values])
    require(all(entry.lower() == entry.upper()
                for row in midpoint.values for entry in row),
            "the exact original GM parent midpoint matrix")
    radius = km.Matrix(N, source_box.cols, [
        [api.magnitude(source_box.values[i][j]-midpoint.values[i][j])
         for j in range(source_box.cols)] for i in range(N)])
    absolute = km.Matrix(N, source_box.cols,
        [[api.magnitude(entry) for entry in row] for row in midpoint.values])
    cross = km.multiply(api, absolute, km.transpose(radius))
    covariance_error = moment._add(api, km, cross, km.transpose(cross),
                                   km.multiply(api, radius, km.transpose(radius)))
    diagonal = [sum((entry.upper() for entry in row), api.zero).upper()
                for row in covariance_error.values]
    require(all(value.is_finite() and value.lower() == value.upper()
                and api.lower(value) >= 0 for value in diagonal),
            "the exact original directed GM row-upper diagonal")
    midpoint_columns = _absolute_column_sums(api, absolute.values)
    radius_columns = _absolute_column_sums(api, radius.values)
    zero_rows = 0
    for i, value in enumerate(diagonal):
        if not bool(value == api.zero):
            continue
        require(all(bool(entry == api.zero) for entry in radius.values[i])
                and all(bool(absolute.values[i][j] == api.zero)
                        or bool(radius_columns[j] == api.zero)
                        for j in range(source_box.cols)),
                "zero ERROR row: no varying radius row or midpoint-radius cross term")
        # The midpoint row itself may be nonzero and is never removed.
        zero_rows += 1
    return {
        "midpoint": midpoint,
        "absolute_midpoint": absolute.values,
        "midpoint_columns": midpoint_columns,
        "parent_radius": radius.values,
        "diagonal": diagonal,
        "zero_error_rows": zero_rows,
        "midpoint_covariance": moment.constant_source_covariance(api, km, midpoint),
    }


def make_child_fixed_midpoint_moment_provider(
        parent_math, api, km, green, moment, coefficient_provider, model, degree=24):
    """One original GM midpoint plus a certified child scale of its error D."""
    require(tuple(parent_math.CONSTANT_ROLES) == CONSTANT_ROLES
            and set(parent_math.SOURCE_ROLES) == set(CONSTANT_ROLES+VARYING_ROLES),
            "exactly the original five complete source roles")
    require(len(green.HEAD) == N and len(green.HIGH0) == 128,
            "original193 output coordinates and128 high-return input columns")
    require(coefficient_provider.context is model["context"]
            and coefficient_provider.original is model["context"].original
            and coefficient_provider.domain is model["context"].domain
            and coefficient_provider.api is api and coefficient_provider.km is km
            and coefficient_provider.green is green,
            "same full-family child source, refined domain, arithmetic and Green")

    class ChildFixedMidpointMomentProvider(parent_math.ParentMomentProvider):
        def __init__(self):
            super().__init__(api, km, green, moment, model, degree)
            self.coefficient_provider = coefficient_provider
            self.parent_affine_cache = {}
            self.child_moment_key = self.active_child_box = None
            self.child_role_cache = {}
            self.statistics.update({
                "source_parent_cache_cap": len(CONSTANT_ROLES),
                "parent_affine_source_cache_cap": len(VARYING_ROLES),
                "source_child_cache_cap": len(VARYING_ROLES),
                "complete_original_GM_midpoint_splits_prepared": 0,
                "complete_parent_midpoint_moments_prepared": 0,
                "complete_parent_error_diagonal_moments_prepared": 0,
                "complete_child_radius_bounds_prepared": 0,
                "complete_child_error_scales_prepared": 0,
                "child_affine_moment_reuses": 0,
                "complete_child_cache_scopes_entered": 0,
                "exact_zero_parent_error_rows_encountered": 0,
                "exact_zero_parent_error_covariances": 0,
                "exact_zero_parent_midpoints": 0,
                "child_scales_equal_one": 0,
                "child_scales_equal_zero": 0,
                "exact_PSD_majorant_no_larger_than_same_GM_parent": True,
                "final_interval_scalar_asserted_smaller": False,
                "child_radius_reused_on_sibling": False,
                "physical_output_dimension_remains193": True,
                "source_columns_deleted": False,
                "source_covariance_scope":
                    "original_parent_midpoint_covariance_plus_child_scale_of_original_GM_error",
            })

        def _prepare_parent(self, panel):
            old = None if self.template is None else self.template["private_template_token"]
            super()._prepare_parent(panel)
            if self.template["private_template_token"] is not old:
                self.parent_affine_cache = {}
                self.child_moment_key = self.active_child_box = None
                self.child_role_cache = {}

        def _zero_source_moments(self):
            return {"U": self.template["U"],
                    "Z": self.km.zeros(self.api, N, N),
                    "Y": self.km.zeros(self.api, N, N),
                    "private_template_token": self.template["private_template_token"]}

        def _parent_affine_plan(self, role):
            require(role in VARYING_ROLES, "one original varying source role")
            if role in self.parent_affine_cache:
                return self.parent_affine_cache[role]
            source = super()._complete_source_ball(role)
            columns = 128 if role == "centre_high0_return_source" else N
            require(source.shape == (N, columns), "all original parent source columns")
            balanced = self.moment._diagonal_left(
                self.km, self.template["diagonal"], source)
            plan = original_GM_midpoint_radius_split(
                self.api, self.km, self.moment, balanced)
            if all(bool(entry == self.api.zero)
                   for row in plan["midpoint"].values for entry in row):
                center = self._zero_source_moments()
                self.statistics["exact_zero_parent_midpoints"] += 1
            else:
                center = self.moment.source_moments(
                    self.api, self.km, self.template, plan["midpoint_covariance"])
                self.statistics["complete_parent_midpoint_moments_prepared"] += 1
            if all(bool(entry == self.api.zero) for entry in plan["diagonal"]):
                error = self._zero_source_moments()
                self.statistics["exact_zero_parent_error_covariances"] += 1
            else:
                diagonal_covariance = self.km.Matrix(N, N, [
                    [plan["diagonal"][i] if i == j else self.api.zero
                     for j in range(N)] for i in range(N)])
                error = self.moment.source_moments(
                    self.api, self.km, self.template, diagonal_covariance)
                self.statistics["complete_parent_error_diagonal_moments_prepared"] += 1
            require(center["private_template_token"] is self.template["private_template_token"]
                    and error["private_template_token"] is self.template["private_template_token"],
                    "same exact H/Q template for midpoint and error moments")
            plan.update({"center_moments": center, "error_moments": error,
                         "private_template_token": self.template["private_template_token"],
                         "source_columns": columns})
            # The center covariance is no longer needed once its full
            # moments are prepared; keep only the current-parent plans.
            del plan["midpoint_covariance"]
            self.parent_affine_cache[role] = plan
            require(len(self.parent_affine_cache) <= len(VARYING_ROLES),
                    "at most three current-parent whole source plans")
            self.statistics["complete_original_GM_midpoint_splits_prepared"] += 1
            self.statistics["exact_zero_parent_error_rows_encountered"] += plan["zero_error_rows"]
            return plan

        def _moments(self, role):
            require(role in CONSTANT_ROLES+VARYING_ROLES,
                    "one of the five original complete source roles")
            if role in CONSTANT_ROLES:
                result = super()._moments(role)
                require(set(self.role_cache).issubset(CONSTANT_ROLES),
                        "only genuine constant source roles use the original cache")
                return result
            require(self.active_child_box is not None
                    and self.child_moment_key == (
                        self.template["private_template_token"],
                        self.model["context"].domain.cache_key(self.active_child_box)),
                    "one whole declared child and its same parent template")
            if role in self.child_role_cache:
                self.statistics["child_affine_moment_reuses"] += 1
                return self.child_role_cache[role]
            plan = self._parent_affine_plan(role)
            require(plan["private_template_token"] is self.template["private_template_token"],
                    "the same complete parent midpoint/error split")
            source = self.coefficient_provider.source_matrix(
                self.model, self.active_child_box, role)
            require(source.shape == (N, plan["source_columns"]),
                    "all genuine child independent input columns")
            balanced = self.moment._diagonal_left(
                self.km, self.template["diagonal"], source)
            child_radius = []
            for i in range(N):
                row = []
                for j in range(plan["source_columns"]):
                    local = _point_upper(self.api, self.api.magnitude(
                        balanced.values[i][j]-plan["midpoint"].values[i][j]))
                    parent = plan["parent_radius"][i][j]
                    # Both enclose |U_ij-M_ij| for the SAME fixed exact M.
                    row.append(parent if bool(parent <= local) else local)
                child_radius.append(row)
            rows = _covariance_error_rows(self.api, plan["absolute_midpoint"],
                                           child_radius, plan["midpoint_columns"])
            sigma = _relative_error_scale(self.api, plan["diagonal"], rows)
            require(sigma.lower() == sigma.upper() and self.api.lower(sigma) >= 0
                    and bool(sigma <= self.api.one), "certified child error scale in [0,1]")
            center, error = plan["center_moments"], plan["error_moments"]
            result = {
                "U": self.template["U"],
                "Z": self.km.add(self.api, center["Z"],
                                 self.km.scale(self.api, sigma, error["Z"])),
                "Y": self.km.add(self.api, center["Y"],
                                 self.km.scale(self.api, sigma, error["Y"])),
                "private_template_token": self.template["private_template_token"],
            }
            self.child_role_cache[role] = result
            require(len(self.child_role_cache) <= len(VARYING_ROLES)
                    and set(self.child_role_cache).issubset(VARYING_ROLES),
                    "at most three complete current-child affine moments")
            self.statistics["complete_child_radius_bounds_prepared"] += 1
            self.statistics["complete_child_error_scales_prepared"] += 1
            if bool(sigma == self.api.one):
                self.statistics["child_scales_equal_one"] += 1
            if bool(sigma == self.api.zero):
                self.statistics["child_scales_equal_zero"] += 1
            return result

        def packet(self, panel, source_role):
            require(source_role in CONSTANT_ROLES+VARYING_ROLES,
                    "one complete original source role")
            self._prepare_parent(panel)
            whole = self.model["context"].domain.whole_cell_box(panel)
            box_key = self.model["context"].domain.cache_key(whole)
            key = self.template["private_template_token"], box_key
            if key != self.child_moment_key:
                self.child_moment_key = key
                self.child_role_cache = {}
                self.statistics["complete_child_cache_scopes_entered"] += 1
            self.active_child_box = whole
            result = super().packet(panel, source_role)
            constant = source_role in CONSTANT_ROLES
            result.update({
                "whole_parent_source_covariance_reused": constant,
                "whole_child_coefficient_source_enclosure": not constant,
                "parent_midpoint_and_error_moments_reused": not constant,
                "source_covariance_cache_scope":
                    "constant_parent" if constant else "whole_child_fixed_GM_midpoint_plus_scaled_error",
                "complete_child_box_key": box_key,
                "child_coefficient_contract": "R141_CC1_through16",
                "fixed_midpoint_child_covariance_contract": "R142_CM1_through7",
                "varying_source_was_treated_as_constant": False,
                "zero_error_rows_deleted_from_physical_space": False,
                "exact_PSD_majorant_no_larger_than_same_GM_parent": True,
                "final_interval_scalar_asserted_smaller": False,
            })
            return result

        def release_parent(self):
            super().release_parent()
            self.parent_affine_cache = {}
            self.child_moment_key = self.active_child_box = None
            self.child_role_cache = {}
            self.coefficient_provider.clear_cache()

    return ChildFixedMidpointMomentProvider()
