"""Point-only defect covariances alongside four unpaid full source moments.

Pure definitions only.  The original defect HS/atoms result is read whole
from R142.  This module materializes only the missing source covariance
Z needed by whole-point receivers, and never recomputes its Y, same-cell
triangle, body HS, or atoms norm.  Point-only packets have NO complete-HS
triangle flag and cannot pass the existing complete-norm accumulator.
"""


def require(ok, message):
    if not ok:
        raise ValueError(message)


def point_source_gram_moment(api, km, moment, template, covariance):
    """The unchanged independent Z branch of original GM source_moments."""
    N = moment.N
    require(covariance.shape == (N, N)
            and all(x.is_finite() for row in covariance.values for x in row),
            "whole same193 point-source covariance")
    v_scale = moment._dyadic_scale(api, moment._infinity_upper(api, covariance))
    Vshort = moment._scale(api, km, covariance, template["step"]/v_scale)
    zterm = zsum = km.zeros(api, N, N)
    for k in range(1, template["degree"]+1):
        old_minus = moment._scale(api, km,
            moment._transpose(km, template["plus_coefficients"][k-1]),
            -api.one if (k-1) % 2 else api.one)
        zterm = moment._scale(api, km, moment._add(api, km,
            km.multiply(api, template["Hshort"], zterm),
            km.multiply(api, Vshort, old_minus)), api.rational(1, k))
        zsum = moment._add(api, km, zsum, zterm)
    Z = moment._inflate(api, km, zsum, template["tail"])
    for A, B, _ in template["stages"][:-1]:
        Z = moment._add(api, km, km.multiply(api, B, Z),
                        km.multiply(api, Z, A))
    A, _, _ = template["stages"][-1]
    integral = moment._scale(api, km,
        km.multiply(api, moment._transpose(km, A), Z), v_scale)
    return {"Z": integral, "private_template_token": template["private_template_token"],
            "old_defect_Y_or_complete_HS_evaluated": False}


def make_four_source_and_point_provider(parent_math, api, km, green, moment,
                                         model, degree=24):
    """One shared parent H/Q template and one same-cell frame per full pass."""
    roles = ("ordinary_raw_low_source", "transformed_low_source",
             "low_second_kind_correction", "centre_high0_return_source")
    require(set(parent_math.SOURCE_ROLES) == set(roles+("true_coefficient_defect",)),
            "all five original physical source definitions remain unchanged")

    class FourSourceAndPointProvider(parent_math.ParentMomentProvider):
        def __init__(self):
            super().__init__(api, km, green, moment, model, degree)
            self.point_moment = None
            self.statistics.update({
                "source_parent_cache_cap": 4,
                "point_source_parent_cache_cap": 1,
                "point_only_parent_Gram_moments_prepared": 0,
                "point_only_refined_cell_packets_prepared": 0,
                "point_parent_Gram_moment_reuses": 0,
                "old_defect_Y_or_complete_HS_evaluated": False,
                "old_defect_atoms_norm_recomputed": False,
                "point_only_packets_claim_complete_HS": False,
            })

        def _prepare_parent(self, panel):
            old = None if self.template is None else self.template["private_template_token"]
            super()._prepare_parent(panel)
            if self.template["private_template_token"] is not old:
                self.point_moment = None

        def packet(self, panel, source_role):
            require(source_role in roles, "only the four unpaid complete source targets")
            return super().packet(panel, source_role)

        def point_packet(self, panel):
            self._prepare_parent(panel)
            if self.point_moment is None:
                source = self._complete_source_ball("true_coefficient_defect")
                covariance = self.moment.model_source_covariance(
                    self.api, self.km, self.template, source, constant=False)
                self.point_moment = point_source_gram_moment(
                    self.api, self.km, self.moment, self.template, covariance)
                self.statistics["point_only_parent_Gram_moments_prepared"] += 1
            else:
                self.statistics["point_parent_Gram_moment_reuses"] += 1
            require(self.point_moment["private_template_token"]
                    is self.template["private_template_token"],
                    "the same current parent H/Q template and point covariance")
            cell = self._prepare_cell(panel)
            Z = self.point_moment["Z"]
            IL = self.green.congruence(self.api, self.km, cell["ell"], Z)
            IR = self.green.congruence(self.api, self.km, cell["rho"], Z)
            self.statistics["point_only_refined_cell_packets_prepared"] += 1
            return {
                "panel": panel, "source_role": "true_coefficient_defect",
                "private_model_token": self.model["private_model_token"],
                "totals": {
                    "OL": cell["OL"], "OR": cell["OR"],
                    "IL": self.km.scale(self.api, cell["length"], IL),
                    "IR": self.km.scale(self.api, cell["length"], IR),
                },
                "point_only_source_covariances_complete": True,
                "whole_parent_source_covariance_reused": True,
                "varying_source_was_treated_as_constant": False,
                "true_cell_length_retained": True,
                "old_defect_Y_or_complete_HS_evaluated": False,
            }

        def release_parent(self):
            super().release_parent()
            self.point_moment = None

    return FourSourceAndPointProvider()
