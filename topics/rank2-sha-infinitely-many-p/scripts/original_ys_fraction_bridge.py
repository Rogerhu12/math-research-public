"""R883/R924 consumer on the SAME original R925 normalization.

Every fraction is a pair of actual integral-basis polynomial vectors.
Multiplication is the fully certified original table; equality is a full
cross-product identity.  The two affine charts, all original constants,
three degeneracies, Artin ordering, CM scales and both endpoints are retained.
No function-field model, independent eta root or new constant field is chosen.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import vector
from section_quotient_algebra import canonical, digest
from original_section_ring_embedding import (
    build_original_section_ring_embedding, polynomial_vector_digest,
    finite_coordinates)
from original_ys_divisor_ideal_tools import (
    OriginalAffineIdealEngine, certify_complete_intersection_degree)
from original_ys_closed_point_tools import (
    OriginalClosedPointRegistry, decompose_complete_ideal)
import original_shadow_relative_six_tools as legacy

ORIGINAL_FOUR_PAIRS = ((0,0),(0,1),(1,1),(1,2))


def _progress(callback, stage, **data):
    if callback is not None:
        callback(stage, **data)


class OriginalFraction:
    """An exact element of the ORIGINAL k(Y), with a complete chart pair."""
    def __init__(self, model, numerator, denominator, pole_weight_bound):
        self.model = model
        P = model.P
        N, D = vector(P, numerator), vector(P, denominator)
        assert len(N) == len(D) == 306 and not D.is_zero()
        bound = int(pole_weight_bound)
        assert bound >= 0
        model.check_weight(N, bound)
        model.check_weight(D, bound)
        if N.is_zero():
            N, D, bound = vector(P, 306), vector(P, model.unit), 0
        else:
            # An explicitly common SCALAR polynomial is a genuine common
            # global factor.  Nothing is inferred from norm gcds or residues.
            common = next(p for p in N if p).monic()
            for p in list(N)+list(D):
                if common.degree() == 0:
                    break
                if p:
                    common = common.gcd(p).monic()
            if common.degree() > 0:
                oldN, oldD = N, D
                assert all(not (p % common) for p in list(N)+list(D))
                N = vector(P, [p//common for p in N])
                D = vector(P, [p//common for p in D])
                assert common*N == oldN and common*D == oldD
                bound -= int(common.degree())
                assert bound >= 0
                model.scalar_cancellations.append({
                    "actual_common_scalar_degree":int(common.degree()),
                    "actual_common_scalar_sha256":digest([
                        finite_coordinates(c, model.k) for c in common.list()]),
                    "both_full_coordinate_vectors_returned_exactly":True,
                })
            leading = next(p for p in D if p).leading_coefficient()
            inverse_leading = model.k.one()/leading
            N, D = inverse_leading*N, inverse_leading*D
        model.check_weight(N, bound)
        model.check_weight(D, bound)
        # The certified Apéry filtration makes this exact coordinate maximum
        # a valid common pole bound.  Tightening it removes needless common
        # powers of s from the infinity-chart pair, without cancelling any
        # non-scalar algebra element or changing the represented function.
        actual_bound = max(int(p.degree())+model.weights[i]
                           for row in (N,D) for i,p in enumerate(row) if p)
        assert 0 <= actual_bound <= bound
        bound = actual_bound
        N.set_immutable()
        D.set_immutable()
        self.numerator, self.denominator, self.pole_weight_bound = N, D, bound
        self._infinity_pair = None

    def is_zero(self):
        return self.numerator.is_zero()

    def __bool__(self):
        return not self.is_zero()

    def __neg__(self):
        return OriginalFraction(self.model, -self.numerator, self.denominator,
                                self.pole_weight_bound)

    def __add__(self, other):
        other = self.model.coerce(other)
        m = self.model
        numerator = m.multiply(self.numerator, other.denominator)+m.multiply(
            other.numerator, self.denominator)
        denominator = m.multiply(self.denominator, other.denominator)
        return OriginalFraction(m, numerator, denominator,
                                self.pole_weight_bound+other.pole_weight_bound)

    __radd__ = __add__

    def __sub__(self, other):
        return self+(-self.model.coerce(other))

    def __rsub__(self, other):
        return self.model.coerce(other)+(-self)

    def __mul__(self, other):
        other = self.model.coerce(other)
        m = self.model
        return OriginalFraction(m, m.multiply(self.numerator, other.numerator),
                                m.multiply(self.denominator, other.denominator),
                                self.pole_weight_bound+other.pole_weight_bound)

    __rmul__ = __mul__

    def inverse(self):
        assert not self.is_zero()
        return OriginalFraction(self.model, self.denominator, self.numerator,
                                self.pole_weight_bound)

    def __truediv__(self, other):
        return self*self.model.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.model.coerce(other)*self.inverse()

    def __pow__(self, exponent):
        exponent = int(exponent)
        if exponent < 0:
            return self.inverse()**(-exponent)
        result, base = self.model.one, self
        while exponent:
            if exponent & 1:
                result = result*base
            exponent >>= 1
            if exponent:
                base = base*base
        return result

    def __eq__(self, other):
        other = self.model.coerce(other)
        if (self.numerator == other.numerator and
                self.denominator == other.denominator):
            return True
        return (self.model.multiply(self.numerator, other.denominator)-
                self.model.multiply(other.numerator, self.denominator)).is_zero()

    def __ne__(self, other):
        return not self.__eq__(other)

    def constant_conjugate(self):
        m = self.model
        def conjugate(row):
            return vector(m.P, [m.P([c**m.prime for c in p.list()]) for p in row])
        return OriginalFraction(m, conjugate(self.numerator), conjugate(self.denominator),
                                self.pole_weight_bound)

    def chart_pair(self, infinity=False):
        if not infinity:
            return self.numerator, self.denominator
        if self._infinity_pair is None:
            m, M = self.model, self.pole_weight_bound
            S, T = m.S.gen(), m.P.gen()
            values = []
            for original in (self.numerator, self.denominator):
                row, returned = vector(m.S, 306), vector(m.P, 306)
                for i, polynomial in enumerate(original):
                    for exponent, coefficient in enumerate(polynomial.list()):
                        if coefficient:
                            output_exponent = M-m.weights[i]-exponent
                            assert output_exponent >= 0
                            row[i] += coefficient*S**output_exponent
                    for exponent, coefficient in enumerate(row[i].list()):
                        if coefficient:
                            returned[i] += coefficient*T**(M-m.weights[i]-exponent)
                assert returned == original
                row.set_immutable()
                values.append(row)
            assert not values[1].is_zero()
            self._infinity_pair = tuple(values)
        return self._infinity_pair

    def receipt(self):
        Ninf, Dinf = self.chart_pair(True)
        return {
            "numerator_sha256":polynomial_vector_digest(self.numerator),
            "denominator_sha256":polynomial_vector_digest(self.denominator),
            "common_infinity_shift":self.pole_weight_bound,
            "common_infinity_shift_is_actual_coordinate_maximum":True,
            "infinity_numerator_sha256":polynomial_vector_digest(Ninf),
            "infinity_denominator_sha256":polynomial_vector_digest(Dinf),
            "same_original_function_both_charts":True,
            "function_field_inverse_used":False,
        }


class OriginalFractionModel:
    def __init__(self, embedding, affine):
        self.embedding, self.affine = embedding, affine
        self.operations = embedding["operations"]
        self.k = embedding["constants"]
        self.prime = int(self.k.characteristic())
        self.P = self.operations["affine_polynomial_ring"]
        self.S = self.operations["infinity_polynomial_ring"]
        self.unit = self.operations["unit"]
        self.weights = tuple(int(d) for d in affine["basis_weights"])
        nonzero = [i for i, c in enumerate(self.unit) if c]
        assert len(nonzero) == 1
        self.unit_index = nonzero[0]
        assert self.weights[self.unit_index] == 0
        assert self.unit[self.unit_index].degree() == 0
        self.unit_scalar = self.k(self.unit[self.unit_index][0])
        self.scalar_cancellations = []
        self.one = OriginalFraction(self, self.unit, self.unit, 0)
        self.zero = OriginalFraction(self, vector(self.P, 306), self.unit, 0)
        self.ys = OriginalFraction(self, self.P.gen()*self.unit, self.unit, 1)

    def check_weight(self, value, bound):
        assert all(not p or int(p.degree())+self.weights[i] <= int(bound)
                   for i, p in enumerate(value))

    def base_scalar(self, value):
        if all(not c for i, c in enumerate(value) if i != self.unit_index):
            return value[self.unit_index]*(self.k.one()/self.unit_scalar)
        return None

    def multiply(self, left, right):
        a = self.base_scalar(left)
        if a is not None:
            return a*right
        b = self.base_scalar(right)
        if b is not None:
            return b*left
        return self.operations["multiply"](left, right)

    def coerce(self, value):
        if isinstance(value, OriginalFraction):
            assert value.model is self
            return value
        scalar = self.k(value)
        return OriginalFraction(self, scalar*self.unit, self.unit, 0)

    def same_degree_section_fraction(self, data):
        return OriginalFraction(self, data["numerator"], data["denominator"],
                                4*int(data["section_power"]))


def build_original_ys_fraction_maps(affine_context, cube_context,
                                   embedding_context=None, progress=None,
                                   compact_context=None):
    """Original F and all Artin-ordered two-endpoint maps, with all identities."""
    cube = cube_context
    assert cube["kind"] == "rank2_original_cube_section_fractions_context"
    assert cube["RF"]["complete_global_identity"]["original_global_identity_certified"] is True
    assert all(cube["RP"][i]["complete_global_identity"]["original_global_identity_certified"] is True
               for i in (0,1,2))
    root_source = cube
    compaction_records = None
    if compact_context is not None:
        compact = compact_context
        assert compact["kind"] == "rank2_original_compact_cube_sections_context"
        assert compact["cube_context"] is cube
        assert compact["complete_product_recipes"] is cube["complete_product_recipes"]
        compaction_records = {}
        for tag,old,new,expected_power in (
                [("RF",cube["RF"],compact["RF"],2)]+
                [("RP%d" % i,cube["RP"][i],compact["RP"][i],3)
                 for i in (0,1,2)]):
            assert new["same_original_function_certified"] is True
            record = new["same_original_function_certificate"]
            assert record["same_original_function_certified"] is True
            source_power,compact_power = int(old["section_power"]),int(new["section_power"])
            assert compact_power == expected_power
            assert int(record["source_section_power"]) == source_power
            assert int(record["compact_section_power"]) == compact_power
            zero_bound = 204*(source_power+compact_power)
            assert int(record["complete_global_zero_degree_bound"]) == zero_bound
            assert int(record["full_checked_coefficients"]) == zero_bound+1
            compaction_records[tag] = record
        root_source = compact
    maps = cube["map_context"]
    if embedding_context is None:
        embedding, embedding_receipt = build_original_section_ring_embedding(
            affine_context, maps, progress=progress, with_map_fractions=True)
    else:
        embedding = embedding_context
        assert embedding["original_map_sections_context"] is maps
        assert embedding["original_affine_context"] is affine_context
        assert embedding["certificate"]["F_and_P_fractions_built"] is True
        embedding_receipt = embedding["certificate"]
    assert embedding["constants"] is cube["constants"]
    model = OriginalFractionModel(embedding, affine_context)
    k, r, ys = model.k, model.prime, model.ys
    # Reuse the ORIGINAL constant routine, including its specified finite
    # field root ordering.  theta17 is a constant here, not a missing Y map.
    constant_input = {
        "constants":k, "prime":r, "omega":cube["original_omega"],
        "original_a_roots":maps["local_context"]["a_roots"],
        "sigma_a_index":maps["sigma_a_index"], "P":maps["P"],
    }
    constants = legacy.fixed_artin_constants(constant_input)
    assert tuple(maps["sigma_a_index"]) == (2,0,1)
    theta, omega = constants["theta17"], constants["omega"]
    section = embedding["section_coordinates"]
    fraction = embedding["same_degree_fraction"]
    recipes = root_source["complete_product_recipes"]
    RF = root_source["RF"]
    RF_power = int(RF["section_power"])
    RF_data = fraction(section(RF_power, recipes[RF_power], RF["numerator_coordinates"], 2),
                       section(RF_power, recipes[RF_power], RF["denominator_coordinates"], 2),
                       RF_power, "same original RF on pi2")
    central_RF = model.same_degree_section_fraction(RF_data)
    central_vF = model.same_degree_section_fraction(embedding["F"][2])
    _progress(progress,"same original central root embedded",
              common_root_bound=central_RF.pole_weight_bound,
              common_y_bound=central_vF.pole_weight_bound)
    endpoint_Y, endpoint_R = {}, {}
    root_embedding_records = [RF_data["certificate"]]
    for index in (0,1,2):
        for exponent in (1,4):
            endpoint_Y[index,exponent] = model.same_degree_section_fraction(
                embedding["P"][index][exponent])
            root = root_source["RP"][index]
            root_power = int(root["section_power"])
            data = fraction(section(root_power, recipes[root_power], root["numerator_coordinates"], exponent),
                            section(root_power, recipes[root_power], root["denominator_coordinates"], exponent),
                            root_power, "same original RP_%d on pi%d" % (index,exponent))
            endpoint_R[index,exponent] = model.same_degree_section_fraction(data)
            root_embedding_records.append(data["certificate"])
            _progress(progress,"same original endpoint root embedded",
                      original_embedding=index,degeneracy=exponent,
                      common_root_bound=endpoint_R[index,exponent].pole_weight_bound,
                      common_y_bound=endpoint_Y[index,exponent].pole_weight_bound)

    def formulas(parameter, swapped=False):
        v = parameter**2-1
        central_T = parameter**2*(parameter**2-9)**2/v**2
        N0 = 5*v+8-parameter*(v-8)
        T0, T2 = N0**3/v**4-27, (v-2)**3/v-27
        epsilon = -central_T*parameter*(v-8)*v**3/(v+4)**6
        f0 = (v+4)/v*central_RF/theta**2
        yF = central_vF/(epsilon*theta**3)
        rows = []
        j0, j2 = (4,1) if swapped else (1,4)
        for constant in constants["rows"]:
            index = int(constant["embedding"])
            dnew, vnew = constant["dnew"], constant["vnew"]
            x0 = N0**2/v**3*endpoint_R[index,j0]/dnew**2
            x2 = (v-2)**2/v*endpoint_R[index,j2]/dnew**2
            y0 = endpoint_Y[index,j0]*2/vnew+1
            y2 = endpoint_Y[index,j2]*2/vnew+1
            rows.append({"x0":x0,"y0":y0,"x2":x2,"y2":y2,
                         "artin_index":int(constant["artin_index"]),
                         "original_embedding":index})
        return {"ys":parameter,"vs":v,"T":central_T,"N0":N0,
                "T0":T0,"T2":T2,"epsilon":epsilon,
                "F_x_over_xs":f0,"F_y":yF,"A":rows}

    actual = formulas(ys)
    v = actual["vs"]
    _progress(progress,"checking original first elliptic equation",
              x_bound=actual["F_x_over_xs"].pole_weight_bound,
              y_bound=actual["F_y"].pole_weight_bound)
    assert actual["F_y"]**2 == v*actual["F_x_over_xs"]**3+1
    for index,row in enumerate(actual["A"]):
        _progress(progress,"checking original two endpoint elliptic equations",
                  artin_index=index,x0_bound=row["x0"].pole_weight_bound,
                  x2_bound=row["x2"].pole_weight_bound,
                  y0_bound=row["y0"].pole_weight_bound,
                  y2_bound=row["y2"].pole_weight_bound)
        assert row["y0"]**2 == v*row["x0"]**3+1
        assert row["y2"]**2 == v*row["x2"]**3+1
    _progress(progress,"all seven original elliptic equations passed")
    _progress(progress,"checking actual original W through proved degeneracy identities")
    W = formulas((ys+3)/(ys-1), swapped=True)
    assert W["T"] == actual["T"]
    assert W["T0"] == actual["T2"] and W["T2"] == actual["T0"]
    correction = 2/(ys-1)
    assert correction*W["F_x_over_xs"] == actual["F_x_over_xs"]
    assert W["F_y"] == -actual["F_y"]
    for original_row, Wrow in zip(actual["A"],W["A"]):
        assert Wrow["y0"] == original_row["y2"]
        assert Wrow["y2"] == original_row["y0"]
        assert correction*Wrow["x0"] == original_row["x2"]
        assert correction*Wrow["x2"] == original_row["x0"]
    _progress(progress,"all original W and endpoint identities passed")
    _progress(progress,"checking original coefficient reflection and CM phases")
    assert actual["F_x_over_xs"].constant_conjugate() == actual["F_x_over_xs"]
    assert actual["F_y"].constant_conjugate() == -actual["F_y"]
    for index, row in enumerate(actual["A"]):
        star, phase = (-index)%3, k.one() if index == 0 else omega**-1
        for tag in ("x0","x2"):
            assert row[tag].constant_conjugate() == actual["A"][star][tag]*phase
        for tag in ("y0","y2"):
            assert row[tag].constant_conjugate() == actual["A"][star][tag]
    records = {tag:actual[tag].receipt() for tag in (
        "ys","vs","T","N0","T0","T2","epsilon","F_x_over_xs","F_y")}
    endpoint_records = [{tag:row[tag].receipt() for tag in ("x0","y0","x2","y2")}
                        for row in actual["A"]]
    receipt = {
        "kind":"rank2_original_Y_fraction_consumer_maps",
        "status":"same_original_maps_and_all_endpoint_CM_reflection_identities",
        "prime":r,"level":3468,"normalization_module_rank":306,
        "same_original_constant_routine_reused":True,
        "original_sigma_a_index":[2,0,1],
        "ordered_packet_embeddings":[int(c["embedding"]) for c in constants["rows"]],
        "theta17_in_original_local_constants":finite_coordinates(theta,k),
        "theta17_is_constant_not_a_missing_function":True,
        "all_original_lambda_h_dnew_scales_retained":True,
        "original_v_and_epsilon_retained":True,
        "first_factor_x_correction":"(v+4)/v",
        "actual_degeneracies":"pi1=q0, pi2=fixed central base, pi4=q2",
        "all_j_to_power_m_differential_factors_retained":True,
        "all_seven_original_elliptic_equations_checked_by_full_ring_identity":True,
        "all_original_W_and_constant_reflection_identities_checked":True,
        "W_implemented_on_proved_original_expression_generators":True,
        "whole_arbitrary_M2_W_matrix_claimed":False,
        "coefficient_Frobenius_distinct_from_function_power_and_Artin":True,
        "embedding_source":embedding_receipt,
        "actual_original_root_embeddings":root_embedding_records,
        "compact_original_roots_used":compact_context is not None,
        "complete_compact_to_original_cross_identity_receipts":compaction_records,
        "actual_RF_section_power":RF_power,
        "actual_RP_section_powers":[int(root_source["RP"][i]["section_power"])
                                    for i in (0,1,2)],
        "old_cube_self_identity_receipts_not_reused_for_new_coordinates":True,
        "actual_scalar_fractions":records,"actual_endpoint_fractions":endpoint_records,
        "exact_shared_base_polynomial_cancellations":model.scalar_cancellations,
        "complete_intersections_computed":False,"original_shadow_computed":False,
        "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "original_constant_consumer_sha256":hashlib.sha256(Path(legacy.__file__).read_bytes()).hexdigest(),
    }
    actual.update({
        "kind":"rank2_original_Y_fraction_consumer_context",
        "prime":r,"constants":k,"omega":omega,"model":model,
        "artin_constants":constants,"cube_context":cube,
        "compact_context":compact_context,
        "embedding_context":embedding,"original_affine_context":affine_context,
        "first_certificate":maps["first_certificate"],
        "packet_certificate":maps["packet_certificate"],
        "certificate":receipt,
    })
    _progress(progress,"same original two-endpoint maps certified in normalization",
              prime=r,all_original_equations=True,original_Artin_order=[2,0,1])
    return actual, receipt


def prepare_original_ys_geometry(six, progress=None, kernel_method="minimal"):
    """Actual complete cusp/branch support and all seven original pole degrees."""
    assert six["kind"] == "rank2_original_Y_fraction_consumer_context"
    model, affine, prime = six["model"], six["original_affine_context"], int(six["prime"])
    operations = model.operations
    engines = {flag:OriginalAffineIdealEngine(
        operations["chart"](infinity=flag),progress=progress,kernel_method=kernel_method)
        for flag in (False,True)}
    basis_identity = {
        "original_curve":"X0(3468)",
        "original_complete_normalization_signature":affine["certificate"]["exact_multiplication_signature_sha256"],
        "original_Y_M2_basis":six["embedding_context"]["coordinate_basis_id"],
    }
    registry = OriginalClosedPointRegistry(basis_identity)
    cache = {}

    def complete_divisor(function, label):
        key = id(function)
        if key in cache:
            assert cache[key]["function"] is function
            return cache[key]
        charts, records = {}, {}
        for flag in (False,True):
            N,D = function.chart_pair(flag)
            positive,negative,record = engines[flag].zero_pole_ideals(N,D,label)
            charts[flag] = {"positive":positive,"negative":negative}
            records[str(flag)] = record
        for sign in ("positive","negative"):
            boundary,record = engines[True].infinity_boundary(charts[True][sign])
            charts[True][sign+"_boundary"] = boundary
            records[sign+"_infinity_boundary"] = record
        positive_degree = charts[False]["positive"].length+charts[True]["positive_boundary"].length
        negative_degree = charts[False]["negative"].length+charts[True]["negative_boundary"].length
        assert positive_degree == negative_degree
        result = {"function":function,"charts":charts,"positive_degree":positive_degree,
                  "negative_degree":negative_degree,"records":records}
        cache[key] = result
        _progress(progress,"same original complete principal divisor certified",
                  label=label,zero_degree=positive_degree,pole_degree=negative_degree)
        return result

    def whole_signed_support(divisor,label):
        entries, records = {}, []
        for flag in (False,True):
            for sign, direction in (("positive",1),("negative",-1)):
                ideal = divisor["charts"][flag][sign]
                points,record = decompose_complete_ideal(
                    engines[flag],ideal,registry,label=label+":"+sign,
                    only_infinity_boundary=flag,progress=progress)
                records.append(record)
                for item in points:
                    point = item["point"]
                    key = id(point)
                    assert key not in entries, "Zero and pole divisors must have disjoint original support."
                    entries[key] = (point,direction*int(item["intersection_multiplicity"]))
        return entries,records

    T_divisor = complete_divisor(six["T"],"same central T")
    v_divisor = complete_divisor(six["vs"],"same v=ys^2-1")
    cusps,T_records = whole_signed_support(T_divisor,"all original cusps")
    v_support,v_records = whole_signed_support(v_divisor,"all original cubic branching")
    assert sum(point["degree_over_original_constants"] for point,m in cusps.values()) == 108
    assert set(v_support).issubset(set(cusps))
    ramified = [(point,m) for point,m in v_support.values() if m % 3]
    assert all(cusps[id(point)][1] < 0 for point,m in ramified)
    assert sum(point["degree_over_original_constants"] for point,m in ramified) == 54
    endpoint_poles = []
    for index,row in enumerate(six["A"]):
        endpoint_poles.append({})
        for tag in ("y0","y2"):
            divisor = complete_divisor(row[tag],"original A%d %s" % (index,tag))
            assert divisor["negative_degree"] == 2256
            endpoint_poles[index][tag] = divisor
    F_poles = complete_divisor(six["F_y"],"original first factor yF")
    first_degree = int(F_poles["negative_degree"])
    assert first_degree > 0
    receipt = {
        "kind":"rank2_original_Y_complete_boundary_and_pole_geometry",
        "status":"same_original_cusps_branching_and_seven_actual_map_pole_divisors",
        "prime":prime,"first_map_degree_from_actual_complete_poles":first_degree,
        "original_geometric_cusp_count":108,"original_cubic_ramified_geometric_count":54,
        "actual_whole_boundary_divisors":[T_records,v_records],
        "all_six_original_endpoint_pole_degrees":2256,
        "actual_endpoint_pole_records":[{tag:value["records"] for tag,value in item.items()}
                                        for item in endpoint_poles],
        "actual_first_factor_pole_records":F_poles["records"],
        "complete_intersection_divisors_computed":False,
        "original_shadow_computed":False,
        "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    return {
        "kind":"rank2_original_Y_complete_pole_geometry_context",
        "six":six,"engines":engines,"registry":registry,
        "original_basis_identity":basis_identity,
        "complete_principal_divisor_cache":cache,
        "complete_divisor":complete_divisor,
        "original_cusp_points":cusps,"original_v_signed_support":v_support,
        "endpoint_poles":endpoint_poles,"F_poles":F_poles,
        "first_map_degree":first_degree,"certificate":receipt,
    },receipt


def build_original_four_intersections(six, geometry_context=None, progress=None,
                                      kernel_method="minimal", decompose_intersections=False):
    """The SAME four entire effective divisors, including the infinity fiber.

    The preceding complete boundary/pole gate may be run and receipted
    separately.  Intersections use g times both complete pole ideals, without
    preliminary factorization of div(g) or any reduced-support shortcut.
    """
    assert six["kind"] == "rank2_original_Y_fraction_consumer_context"
    if geometry_context is None:
        geometry,geometry_receipt = prepare_original_ys_geometry(
            six,progress=progress,kernel_method=kernel_method)
    else:
        geometry = geometry_context
        assert geometry["kind"] == "rank2_original_Y_complete_pole_geometry_context"
        assert geometry["six"] is six
        geometry_receipt = geometry["certificate"]
    prime = int(six["prime"])
    engines,registry = geometry["engines"],geometry["registry"]
    basis_identity = geometry["original_basis_identity"]
    endpoint_poles,F_poles = geometry["endpoint_poles"],geometry["F_poles"]
    first_degree = int(geometry["first_map_degree"])
    cache = geometry["complete_principal_divisor_cache"]
    cusps,v_support = geometry["original_cusp_points"],geometry["original_v_signed_support"]
    use_endpoint_output = first_degree < 2256
    intersections, intersection_receipts = {}, []
    for a,b in ORIGINAL_FOUR_PAIRS:
        if use_endpoint_output:
            a0,y1 = six["A"][a]["x0"],six["A"][a]["y0"]
            xp,yp = six["F_x_over_xs"],six["F_y"]
            output_x,output_y = six["A"][b]["x2"],six["A"][b]["y2"]
            p1,pp = endpoint_poles[a]["y0"],F_poles
            presentation = "A_bq2 output: A_aq0 minus Frobenius F"
        else:
            a0,y1 = six["A"][b]["x2"],six["A"][b]["y2"]
            xp,yp = six["A"][a]["x0"],six["A"][a]["y0"]
            output_x,output_y = six["F_x_over_xs"],six["F_y"]
            p1,pp = endpoint_poles[b]["y2"],endpoint_poles[a]["y0"]
            presentation = "F output: A_bq2 minus Frobenius A_aq0"
        _progress(progress,"building original true Frobenius fractions",
                  endpoint_pair=[a,b],cyclic_presentation=presentation,
                  original_prime=prime,xp_bound=xp.pole_weight_bound,
                  yp_bound=yp.pole_weight_bound)
        c0 = six["vs"]**((prime-2)//3)*xp**prime
        y2 = yp**prime
        g = y1-y2
        assert not g.is_zero()
        xout = a0*output_x/c0
        _progress(progress,"original true Frobenius fractions built",
                  endpoint_pair=[a,b],difference_bound=g.pole_weight_bound,
                  frobenius_x_bound=c0.pole_weight_bound,
                  frobenius_y_bound=y2.pole_weight_bound,
                  output_x_bound=xout.pole_weight_bound)
        ideals, records = {}, []
        for flag in (False,True):
            engine = engines[flag]
            _progress(progress,"building complete original intersection chart",
                      endpoint_pair=[a,b],infinity_chart=flag,
                      common_difference_bound=g.pole_weight_bound)
            pole_product = engine.ideal_product(
                p1["charts"][flag]["negative"],
                engine.ideal_power(pp["charts"][flag]["negative"],prime,
                                   "original r times yp poles"),
                "original complete input pole product")
            N,D = g.chart_pair(flag)
            ideal = engine.integral_fraction_multiple(
                pole_product,N,D,"original E_%d%d effective ideal" % (a,b))
            ideals[flag] = ideal
            records.append({"infinity_chart":flag,
                            "both_complete_pole_product":pole_product.receipt,
                            "whole_effective_intersection":ideal.receipt})
        infinity_boundary,boundary_receipt = engines[True].infinity_boundary(ideals[True])
        degree_receipt = certify_complete_intersection_degree(
            ideals[False],infinity_boundary,prime,first_degree)
        item = {"endpoint_pair":(a,b),"cyclic_presentation":presentation,
                "a0":a0,"y1":y1,"xp":xp,"yp":yp,"c0":c0,"y2":y2,"g":g,
                "output_x":output_x,"output_y":output_y,"xout":xout,
                "finite_ideal":ideals[False],"full_infinity_chart_ideal":ideals[True],
                "infinity_boundary_ideal":infinity_boundary,
                "complete_degree":degree_receipt["original_complete_projective_intersection_degree"]}
        decomposition_records = None
        if decompose_intersections:
            finite_points,finite_receipt = decompose_complete_ideal(
                engines[False],ideals[False],registry,label="original E_%d%d finite" % (a,b),
                progress=progress)
            infinity_points,infinity_receipt = decompose_complete_ideal(
                engines[True],ideals[True],registry,label="original E_%d%d infinity" % (a,b),
                only_infinity_boundary=True,progress=progress)
            item["closed_points"] = finite_points+infinity_points
            assert sum(p["full_local_k_length"] for p in item["closed_points"]) == item["complete_degree"]
            decomposition_records = [finite_receipt,infinity_receipt]
        intersections[a,b] = item
        record = {"endpoint_pair":[a,b],"cyclic_presentation":presentation,
                  "complete_original_degree":degree_receipt,
                  "same_original_difference":g.receipt(),
                  "same_original_output_x":xout.receipt(),
                  "same_original_output_y":output_y.receipt(),
                  "both_complete_ideal_charts":records,
                  "entire_infinity_boundary":boundary_receipt,
                  "all_closed_points_decomposed":bool(decompose_intersections),
                  "closed_point_decompositions":decomposition_records,
                  "local_output_values_and_trace_claimed":False}
        intersection_receipts.append(record)
        _progress(progress,"same entire original intersection certified",
                  endpoint_pair=[a,b],complete_degree=item["complete_degree"],
                  first_map_degree=first_degree,all_infinity_points_retained=True)
    receipt = {
        "kind":"rank2_original_Y_four_complete_intersection_ideals",
        "status":"same_four_original_effective_divisors_and_all_output_fractions",
        "prime":prime,"first_map_degree_from_actual_complete_poles":first_degree,
        "original_geometric_cusp_count":108,"original_cubic_ramified_geometric_count":54,
        "all_six_original_endpoint_pole_degrees":2256,
        "actual_complete_original_geometry":geometry_receipt,
        "same_original_four_pairs":[list(pair) for pair in ORIGINAL_FOUR_PAIRS],
        "complete_intersections":intersection_receipts,
        "all_same_original_rational_output_fractions_retained":True,
        "all_closed_intersection_points_decomposed":bool(decompose_intersections),
        "local_output_values_and_original_shadow_computed":False,
        "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    return {
        "kind":"rank2_original_Y_four_intersection_context",
        "six":six,"geometry_context":geometry,"engines":engines,"registry":registry,
        "original_basis_identity":basis_identity,
        "first_map_degree":first_degree,"intersections":intersections,
        "complete_principal_divisor_cache":cache,
        "original_cusp_points":cusps,"original_v_signed_support":v_support,
        "certificate":receipt,
    },receipt
