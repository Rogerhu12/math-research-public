"""Exact, bounded reuse inside ONE original four-intersection computation.

This helper is a PROPOSAL until its separate public execution is accepted.
Keys retain the original fraction objects.  A hit requires object identity
or equality of both complete 306-coordinate numerator/denominator vectors.
Unequal representations of an equal function are harmless cache misses.
No hash, norm, degree, prefix or residue is ever an equality oracle.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in the public research Actions.")


def same_complete_original_fraction(left, right, model, fraction_type):
    """Return an exact equality reason, or None without asserting inequality."""
    assert type(left) is fraction_type and type(right) is fraction_type
    assert left.model is right.model is model
    if left is right:
        return "same retained OriginalFraction object"
    if (left.numerator == right.numerator and
            left.denominator == right.denominator):
        return "both whole original numerator and denominator vectors equal"
    return None


def _same_fraction_tuple(left, right, model, fraction_type):
    assert len(left) == len(right)
    reasons = [same_complete_original_fraction(a,b,model,fraction_type)
               for a,b in zip(left,right)]
    return reasons if all(reasons) else None


class OriginalExactIntersectionReuse:
    """At most four power bundles and four complete two-chart ideals."""
    def __init__(self, six, geometry):
        assert geometry["six"] is six
        self.six, self.geometry = six, geometry
        self.model = six["model"]
        self.fraction_type = type(six["ys"])
        self.prime = int(six["prime"])
        self.engines = geometry["engines"]
        self.registry = geometry["registry"]
        self.power_bundles, self.intersections = [], []
        self.power_queries = self.power_hits = 0
        self.intersection_queries = self.intersection_hits = 0

    def frobenius_fractions(self, v, xp, yp, prime, endpoint_pair):
        assert int(prime) == self.prime
        inputs = (v,xp,yp)
        self.power_queries += 1
        for entry in self.power_bundles:
            reasons = _same_fraction_tuple(
                entry["inputs"],inputs,self.model,self.fraction_type)
            if reasons is not None:
                assert entry["prime"] == self.prime
                self.power_hits += 1
                return entry["c0"],entry["y2"],{
                    "reused":True,"first_endpoint_pair":list(entry["first_pair"]),
                    "current_endpoint_pair":list(endpoint_pair),
                    "exact_input_equalities":reasons,
                    "prime_and_original_model_identical":True,
                    "hash_used_to_decide_equality":False,
                }
        c0 = v**((self.prime-2)//3)*xp**self.prime
        y2 = yp**self.prime
        self.power_bundles.append({
            "inputs":inputs,"prime":self.prime,"c0":c0,"y2":y2,
            "first_pair":tuple(endpoint_pair),
        })
        assert len(self.power_bundles) <= 4
        return c0,y2,{
            "reused":False,"first_endpoint_pair":list(endpoint_pair),
            "current_endpoint_pair":list(endpoint_pair),
            "true_original_function_powers_computed":True,
            "prime_and_original_model_identical":True,
            "hash_used_to_decide_equality":False,
        }

    def _pole_equalities(self, old_sources, new_sources):
        reasons = []
        for old,new in zip(old_sources,new_sources):
            for flag in (False,True):
                previous,current = (value["charts"][flag]["negative"]
                                    for value in (old,new))
                assert previous.engine is current.engine is self.engines[flag]
                if previous is current:
                    reason = "same complete original pole ideal object"
                else:
                    assert previous.basis == current.basis
                    assert previous.determinant == current.determinant
                    assert previous.length == current.length
                    reason = "whole canonical pole Hermite bases equal"
                reasons.append({"infinity_chart":flag,"reason":reason})
        return reasons

    def find_intersection(self, y1, yp, poles1, polesp, prime, endpoint_pair):
        assert int(prime) == self.prime
        self.intersection_queries += 1
        for entry in self.intersections:
            reasons = _same_fraction_tuple(
                entry["input_functions"],(y1,yp),self.model,self.fraction_type)
            if reasons is None:
                continue
            assert entry["prime"] == self.prime
            assert entry["six"] is self.six and entry["geometry"] is self.geometry
            assert entry["registry"] is self.registry
            assert all(entry["engines"][flag] is self.engines[flag] for flag in (False,True))
            pole_reasons = self._pole_equalities(
                entry["pole_sources"],(poles1,polesp))
            self.intersection_hits += 1
            return entry,{
                "reused":True,"first_endpoint_pair":list(entry["first_pair"]),
                "current_endpoint_pair":list(endpoint_pair),
                "exact_y1_yp_equalities":reasons,
                "both_complete_pole_ideal_equalities":pole_reasons,
                "same_original_two_chart_engines_and_registry":True,
                "same_entire_effective_divisor_including_infinity":True,
                "output_functions_or_trace_reused":False,
                "hash_used_to_decide_equality":False,
            }
        return None,{
            "reused":False,"current_endpoint_pair":list(endpoint_pair),
            "output_functions_or_trace_reused":False,
            "hash_used_to_decide_equality":False,
        }

    def remember_intersection(self, y1, yp, poles1, polesp, g, ideals,
                              infinity_boundary, degree_receipt, chart_records,
                              boundary_receipt, endpoint_pair):
        assert not g.is_zero() and g.model is self.model
        assert all(ideals[flag].engine is self.engines[flag] for flag in (False,True))
        assert infinity_boundary.engine is self.engines[True]
        degree = int(degree_receipt["original_complete_projective_intersection_degree"])
        assert ideals[False].length+infinity_boundary.length == degree
        entry = {
            "kind":"same_original_complete_intersection_shared_data",
            "six":self.six,"geometry":self.geometry,"engines":self.engines,
            "registry":self.registry,"prime":self.prime,
            "input_functions":(y1,yp),"pole_sources":(poles1,polesp),
            "g":g,"ideals":ideals,"infinity_boundary":infinity_boundary,
            "degree_receipt":degree_receipt,"complete_degree":degree,
            "chart_records":chart_records,"boundary_receipt":boundary_receipt,
            "first_pair":tuple(endpoint_pair),
            "closed_points":None,"closed_point_decomposition_receipt":None,
        }
        self.intersections.append(entry)
        assert len(self.intersections) <= 4
        return entry

    def receipt(self):
        return {
            "power_bundle_queries":self.power_queries,
            "distinct_true_power_bundles":len(self.power_bundles),
            "exact_true_power_reuse_hits":self.power_hits,
            "complete_intersection_queries":self.intersection_queries,
            "distinct_complete_two_chart_intersections":len(self.intersections),
            "exact_complete_intersection_reuse_hits":self.intersection_hits,
            "every_key_retains_its_actual_original_fraction_objects":True,
            "nonidentical_objects_require_both_complete_coordinate_vectors_equal":True,
            "norm_hash_degree_prefix_or_residue_used_as_equality_oracle":False,
            "whole_ideal_objects_shared_not_copied":True,
            "all_four_output_functions_and_trace_loops_retained":True,
        }


def validate_shared_original_intersection(context, item, shared):
    """The shared decomposition belongs to these exact complete ideal objects."""
    assert shared["kind"] == "same_original_complete_intersection_shared_data"
    assert shared["six"] is context["six"]
    assert shared["geometry"] is context["geometry_context"]
    assert shared["registry"] is context["registry"]
    assert all(shared["engines"][flag] is context["engines"][flag] for flag in (False,True))
    assert item["finite_ideal"] is shared["ideals"][False]
    assert item["full_infinity_chart_ideal"] is shared["ideals"][True]
    assert item["infinity_boundary_ideal"] is shared["infinity_boundary"]
    assert item["g"] is shared["g"]
    assert int(item["complete_degree"]) == shared["complete_degree"]
    model = context["six"]["model"]
    assert _same_fraction_tuple(shared["input_functions"],(item["y1"],item["yp"]),
                                model,type(context["six"]["ys"])) is not None
    return {
        "same_entire_original_intersection_ideal_objects":True,
        "same_original_engines_registry_and_fraction_sources":True,
        "first_endpoint_pair":list(shared["first_pair"]),
        "current_endpoint_pair":list(item["endpoint_pair"]),
        "full_projective_degree":shared["complete_degree"],
        "hash_used_to_decide_equality":False,
        "output_functions_and_trace_are_still_current_pair_specific":True,
    }
