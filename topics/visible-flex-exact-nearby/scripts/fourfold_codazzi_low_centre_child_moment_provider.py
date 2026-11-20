"""Explicit CC child coefficients -> existing complete GM moment packets.

Pure definitions, no imports, IO, entry point or scientific execution.
The existing parent-provider module is supplied explicitly.  This factory
creates an ordinary subclass; it never patches that module or any model.
The inherited signed packet formula, frame cache and shared-output format
remain unchanged.  Only the scope of the varying source-moment cache changes.
"""

CONSTANT_ROLES = ("ordinary_raw_low_source", "transformed_low_source")
VARYING_ROLES = ("true_coefficient_defect", "low_second_kind_correction",
                 "centre_high0_return_source")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def make_child_moment_provider(parent_math, api, km, green, moment,
                               coefficient_provider, model, degree=24):
    """Return a same-model GM provider with two explicitly different caches.

    parent_math is the unchanged published parent-moment adapter.  Its
    H/Q template and constant I/Sinv moments remain parent/count objects.
    Every varying source is obtained from the complete declared child box
    and has a cache key containing both that box and its template identity.
    A child covariance is never reused on a sibling or larger parent.
    """
    require(tuple(parent_math.CONSTANT_ROLES) == CONSTANT_ROLES
            and set(parent_math.SOURCE_ROLES) == set(CONSTANT_ROLES+VARYING_ROLES),
            "same five original source roles and exactly two constant roles")
    require(coefficient_provider.context is model["context"]
            and coefficient_provider.original is model["context"].original
            and coefficient_provider.domain is model["context"].domain,
            "child coefficients and moment model use the same exact refined domain")
    require(coefficient_provider.api is api and coefficient_provider.km is km
            and coefficient_provider.green is green,
            "same directed arithmetic, signed matrices and original Green contract")

    class ChildMomentProvider(parent_math.ParentMomentProvider):
        def __init__(self):
            super().__init__(api, km, green, moment, model, degree)
            self.coefficient_provider = coefficient_provider
            self.child_moment_key = self.active_child_box = None
            self.child_role_cache = {}
            self.statistics.update({
                "source_parent_cache_cap": len(CONSTANT_ROLES),
                "source_child_cache_cap": len(VARYING_ROLES),
                "complete_child_source_covariances_prepared": 0,
                "child_source_moment_reuses": 0,
                "complete_child_cache_scopes_entered": 0,
                "child_source_reused_on_sibling": False,
                "source_covariance_scope": "constant_parent_and_varying_whole_child",
            })

        def _moments(self, role):
            require(role in CONSTANT_ROLES+VARYING_ROLES,
                    "one of the five complete original roles")
            if role in CONSTANT_ROLES:
                result = super()._moments(role)
                require(set(self.role_cache).issubset(CONSTANT_ROLES),
                        "only truly constant sources may inhabit the parent cache")
                return result
            require(self.active_child_box is not None
                    and self.child_moment_key == (
                        self.template["private_template_token"],
                        self.model["context"].domain.cache_key(self.active_child_box)),
                    "varying source has an active complete child and current template")
            if role in self.child_role_cache:
                self.statistics["child_source_moment_reuses"] += 1
                return self.child_role_cache[role]
            source = self.coefficient_provider.source_matrix(
                self.model, self.active_child_box, role)
            covariance = self.moment.model_source_covariance(
                self.api, self.km, self.template, source, constant=False)
            result = self.moment.source_moments(
                self.api, self.km, self.template, covariance)
            require(result["private_template_token"] is self.template["private_template_token"],
                    "child source moments use the same complete H/Q template")
            self.child_role_cache[role] = result
            require(len(self.child_role_cache) <= len(VARYING_ROLES)
                    and set(self.child_role_cache).issubset(VARYING_ROLES),
                    "only three varying roles in one complete child cache")
            self.statistics["complete_child_source_covariances_prepared"] += 1
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
            # The inherited formula still has BOTH signed triangles, the
            # same independent cell carriers, true h/h^2 and complete mean.
            result = super().packet(panel, source_role)
            constant = source_role in CONSTANT_ROLES
            result.update({
                "whole_parent_source_covariance_reused": constant,
                "whole_child_coefficient_source_enclosure": not constant,
                "source_covariance_cache_scope": "parent" if constant else "complete_child",
                "complete_child_box_key": box_key,
                "child_coefficient_contract": "R141_CC1_through16",
                "varying_source_was_treated_as_constant": False,
            })
            return result

        def release_parent(self):
            super().release_parent()
            self.child_moment_key = self.active_child_box = None
            self.child_role_cache = {}
            self.coefficient_provider.clear_cache()

    return ChildMomentProvider()
