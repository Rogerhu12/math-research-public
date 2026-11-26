"""True-child sources with one parent diagonal covariance and scalar scales.

Pure definitions only: no imports, IO, numerical library, producer, entry point,
model mutation, or work at import.  The caller supplies the unchanged parent
moment module and genuine whole-child signed coefficient provider explicitly.

CD.1--6 prove U_child U_child^T <= sigma_child D_parent.  A zero D row is an
exactly zero source-output row, padded in the original193 coordinates; no mean,
endpoint, or independent source column is deleted.  The fixed diagonal D is
not asserted better than the existing GM midpoint-plus-radius covariance.
"""

N = 193
CONSTANT_ROLES = ("ordinary_raw_low_source", "transformed_low_source")
VARYING_ROLES = ("true_coefficient_defect", "low_second_kind_correction",
                 "centre_high0_return_source")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def _point_upper(api, value):
    point = value.upper()
    require(point.is_finite() and point.lower() == point.upper()
            and api.lower(point) >= 0, "finite exact nonnegative upper point")
    return point


def _absolute_source(api, matrix):
    require(matrix.rows == N and matrix.cols > 0
            and len(matrix.values) == N
            and all(len(row) == matrix.cols for row in matrix.values),
            "all193 output rows and every original source column")
    return [[_point_upper(api, api.magnitude(entry)) for entry in row]
            for row in matrix.values]


def _quadratic_row_upper(api, absolute):
    """Outward (A A^T 1)_i in O(N times input_columns), without forming A A^T."""
    require(len(absolute) == N and absolute and absolute[0],
            "whole nonempty193-row absolute source")
    columns = len(absolute[0])
    require(all(len(row) == columns for row in absolute)
            and all(value.is_finite() and value.lower() == value.upper()
                    and api.lower(value) >= 0
                    for row in absolute for value in row),
            "complete fixed nonnegative source bounds")
    sums = [_point_upper(api, sum((absolute[i][j] for i in range(N)), api.zero))
            for j in range(columns)]
    return [_point_upper(api, sum((absolute[i][j]*sums[j]
                                  for j in range(columns)), api.zero))
            for i in range(N)]


def _intersect_absolute(api, parent, child):
    """Two scalar absolute bounds of each SAME entry, not a PSD-matrix minimum."""
    require(len(parent) == len(child) == N
            and all(len(a) == len(b) for a, b in zip(parent, child)),
            "same full source shape in parent and genuine child")
    result = []
    for arow, brow in zip(parent, child):
        row = []
        for a, b in zip(arow, brow):
            require(a.lower() == a.upper() and b.lower() == b.upper()
                    and api.lower(a) >= 0 and api.lower(b) >= 0,
                    "ordered exact nonnegative absolute endpoints")
            row.append(a if bool(a <= b) else b)
        result.append(row)
    return result


def _child_scale(api, diagonal, absolute):
    """CD.3 including exact zero-row support and the separately proved cap1."""
    require(len(diagonal) == N, "the entire fixed parent diagonal")
    numerator = _quadratic_row_upper(api, absolute)
    sigma = api.zero
    positive = 0
    for i, denominator in enumerate(diagonal):
        require(denominator.is_finite()
                and denominator.lower() == denominator.upper()
                and api.lower(denominator) >= 0,
                "fixed exact nonnegative parent diagonal entry")
        if bool(denominator == api.zero):
            require(all(bool(value == api.zero) for value in absolute[i])
                    and bool(numerator[i] == api.zero),
                    "zero parent support retains an exactly zero whole child row")
            continue
        require(api.lower(denominator) > 0, "division only on positive support")
        positive += 1
        ratio = _point_upper(api, numerator[i]/denominator)
        if bool(ratio > sigma):
            sigma = ratio
    if positive == 0:
        require(bool(sigma == api.zero), "empty positive support is exactly zero")
        return api.zero
    # Both D and sigma_hat D separately dominate the true child covariance.
    # Taking the smaller SCALAR for this one fixed D is therefore rigorous.
    return api.one if bool(sigma >= api.one) else sigma


def make_child_diagonal_moment_provider(parent_math, api, km, green, moment,
                                        coefficient_provider, model, degree=24):
    """Explicit same-model provider: original2 constants and3 true-child roles."""
    require(tuple(parent_math.CONSTANT_ROLES) == CONSTANT_ROLES
            and set(parent_math.SOURCE_ROLES) == set(CONSTANT_ROLES+VARYING_ROLES),
            "exactly the original five full source roles")
    require(len(green.HEAD) == N and len(green.HIGH0) == 128,
            "original193 coordinates and128 high-return input columns")
    require(coefficient_provider.context is model["context"]
            and coefficient_provider.original is model["context"].original
            and coefficient_provider.domain is model["context"].domain,
            "whole child coefficients and moments share the exact refined domain")
    require(coefficient_provider.api is api and coefficient_provider.km is km
            and coefficient_provider.green is green,
            "same directed arithmetic and complete signed Green source contract")

    class ChildDiagonalMomentProvider(parent_math.ParentMomentProvider):
        def __init__(self):
            super().__init__(api, km, green, moment, model, degree)
            self.coefficient_provider = coefficient_provider
            self.parent_diagonal_cache = {}
            self.child_moment_key = self.active_child_box = None
            self.child_role_cache = {}
            self.statistics.update({
                "source_parent_cache_cap": len(CONSTANT_ROLES),
                "parent_diagonal_source_cache_cap": len(VARYING_ROLES),
                "source_child_cache_cap": len(VARYING_ROLES),
                "complete_parent_diagonal_source_moments_prepared": 0,
                "complete_parent_absolute_source_bounds_prepared": 0,
                "complete_child_absolute_source_bounds_prepared": 0,
                "complete_child_relative_scales_prepared": 0,
                "child_scaled_moment_reuses": 0,
                "complete_child_cache_scopes_entered": 0,
                "exact_zero_parent_output_rows_encountered": 0,
                "exact_zero_parent_source_roles": 0,
                "child_scales_equal_one": 0,
                "child_scales_equal_zero": 0,
                "child_source_reused_on_sibling": False,
                "physical_output_dimension_remains193": True,
                "source_columns_deleted": False,
                "fixed_diagonal_asserted_better_than_GM_covariance": False,
                "source_covariance_scope":
                    "constant_parent_and_genuine_child_scale_of_fixed_parent_diagonal",
            })

        def _prepare_parent(self, panel):
            old = None if self.template is None else self.template["private_template_token"]
            super()._prepare_parent(panel)
            if self.template["private_template_token"] is not old:
                self.parent_diagonal_cache = {}
                self.child_moment_key = self.active_child_box = None
                self.child_role_cache = {}

        def _parent_diagonal_plan(self, role):
            require(role in VARYING_ROLES, "only the three original varying roles")
            if role in self.parent_diagonal_cache:
                return self.parent_diagonal_cache[role]
            source = super()._complete_source_ball(role)
            expected_columns = 128 if role == "centre_high0_return_source" else N
            require(source.shape == (N, expected_columns),
                    "same original source columns before balancing")
            balanced = self.moment._diagonal_left(
                self.km, self.template["diagonal"], source)
            absolute = _absolute_source(self.api, balanced)
            diagonal = _quadratic_row_upper(self.api, absolute)
            positive = []
            for i, value in enumerate(diagonal):
                if bool(value == self.api.zero):
                    require(all(bool(entry == self.api.zero) for entry in absolute[i]),
                            "q_i(A)=0 certifies the entire original source row is zero")
                    self.statistics["exact_zero_parent_output_rows_encountered"] += 1
                else:
                    require(self.api.lower(value) > 0, "positive fixed parent support")
                    positive.append(i)
            if positive:
                covariance = self.km.Matrix(N, N, [
                    [diagonal[i] if i == j else self.api.zero for j in range(N)]
                    for i in range(N)])
                result = self.moment.source_moments(self.api, self.km,
                                                    self.template, covariance)
                self.statistics["complete_parent_diagonal_source_moments_prepared"] += 1
            else:
                result = {"U": self.template["U"],
                          "Z": self.km.zeros(self.api, N, N),
                          "Y": self.km.zeros(self.api, N, N),
                          "private_template_token": self.template["private_template_token"]}
                self.statistics["exact_zero_parent_source_roles"] += 1
            require(result["private_template_token"] is self.template["private_template_token"],
                    "one same H/Q moment template for the whole parent")
            plan = {"absolute": absolute, "diagonal": diagonal, "moments": result,
                    "private_template_token": self.template["private_template_token"],
                    "source_columns": expected_columns}
            self.parent_diagonal_cache[role] = plan
            require(len(self.parent_diagonal_cache) <= len(VARYING_ROLES),
                    "bounded three-role current-parent diagonal cache")
            self.statistics["complete_parent_absolute_source_bounds_prepared"] += 1
            return plan

        def _moments(self, role):
            require(role in CONSTANT_ROLES+VARYING_ROLES,
                    "one complete original source role")
            if role in CONSTANT_ROLES:
                result = super()._moments(role)
                require(set(self.role_cache).issubset(CONSTANT_ROLES),
                        "only the two genuine constant sources use the parent role cache")
                return result
            require(self.active_child_box is not None
                    and self.child_moment_key == (
                        self.template["private_template_token"],
                        self.model["context"].domain.cache_key(self.active_child_box)),
                    "one complete declared child and its current H/Q template")
            if role in self.child_role_cache:
                self.statistics["child_scaled_moment_reuses"] += 1
                return self.child_role_cache[role]
            plan = self._parent_diagonal_plan(role)
            require(plan["private_template_token"] is self.template["private_template_token"],
                    "the same current parent covariance plan")
            source = self.coefficient_provider.source_matrix(
                self.model, self.active_child_box, role)
            require(source.shape == (N, plan["source_columns"]),
                    "every true-child independent source column retained")
            balanced = self.moment._diagonal_left(
                self.km, self.template["diagonal"], source)
            absolute = _intersect_absolute(
                self.api, plan["absolute"], _absolute_source(self.api, balanced))
            sigma = _child_scale(self.api, plan["diagonal"], absolute)
            require(sigma.is_finite() and sigma.lower() == sigma.upper()
                    and self.api.lower(sigma) >= 0 and bool(sigma <= self.api.one),
                    "complete child scalar scale in the proved range")
            base = plan["moments"]
            result = {
                "U": self.template["U"],
                "Z": self.km.scale(self.api, sigma, base["Z"]),
                "Y": self.km.scale(self.api, sigma, base["Y"]),
                "private_template_token": self.template["private_template_token"],
            }
            self.child_role_cache[role] = result
            require(len(self.child_role_cache) <= len(VARYING_ROLES)
                    and set(self.child_role_cache).issubset(VARYING_ROLES),
                    "at most three current-child scaled moments")
            self.statistics["complete_child_absolute_source_bounds_prepared"] += 1
            self.statistics["complete_child_relative_scales_prepared"] += 1
            if bool(sigma == self.api.one):
                self.statistics["child_scales_equal_one"] += 1
            if bool(sigma == self.api.zero):
                self.statistics["child_scales_equal_zero"] += 1
            return result

        def packet(self, panel, source_role):
            require(source_role in CONSTANT_ROLES+VARYING_ROLES,
                    "one complete original role before preparing a child")
            self._prepare_parent(panel)
            whole = self.model["context"].domain.whole_cell_box(panel)
            box_key = self.model["context"].domain.cache_key(whole)
            key = self.template["private_template_token"], box_key
            if key != self.child_moment_key:
                self.child_moment_key = key
                self.child_role_cache = {}
                self.statistics["complete_child_cache_scopes_entered"] += 1
            self.active_child_box = whole
            # Original independent frame, true h/h^2, BOTH signed triangles,
            # full193 output atoms and complete source column units remain.
            result = super().packet(panel, source_role)
            constant = source_role in CONSTANT_ROLES
            result.update({
                "whole_parent_source_covariance_reused": constant,
                "whole_child_coefficient_source_enclosure": not constant,
                "parent_diagonal_moments_reused_with_certified_child_scale": not constant,
                "source_covariance_cache_scope":
                    "constant_parent" if constant else "genuine_child_scalar_times_parent_D",
                "complete_child_box_key": box_key,
                "child_coefficient_contract": "R141_CC1_through16",
                "diagonal_child_covariance_contract": "R142_CD1_through6",
                "varying_source_was_treated_as_constant": False,
                "zero_source_output_rows_deleted": False,
            })
            return result

        def release_parent(self):
            super().release_parent()
            self.parent_diagonal_cache = {}
            self.child_moment_key = self.active_child_box = None
            self.child_role_cache = {}
            self.coefficient_provider.clear_cache()

    return ChildDiagonalMomentProvider()
