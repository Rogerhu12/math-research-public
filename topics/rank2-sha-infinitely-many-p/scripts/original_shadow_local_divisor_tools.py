#!/usr/bin/env sage-python
"""Original relative-six local divisor backend; public Actions only.

This optional backend retains the SAME source Y, all constants and closed
places.  It uses the already normalized quotient over F_r and exact norms,
then successive tame Kummer completions.  It never calls maximal_order on
the degree288 source.  No map or nonzero shadow is certified by this module.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical backend only in the public repository Actions.")

import hashlib
import json
from sage.all import (ZZ, PolynomialRing, LaurentSeriesRing, infinity)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def progress(stage, **data):
    print("RANK2_ORIGINAL_LOCAL_DIVISOR_STAGE "+
          canonical(dict(stage=stage, **data)), flush=True)


def residue_coordinates(value):
    return [int(a) for a in value.polynomial().list()]


def native_function_hash(value):
    return digest([str(a) for a in value.list()])


def native_place_hash(place):
    return digest({
        "degree":int(place.degree()),
        "generators":[native_function_hash(g) for g in place.prime_ideal().gens()]})


class NeedMorePrecision(Exception):
    pass


class LocalDivisor:
    """The exact divisor interface used by the existing relative consumer."""
    def __init__(self, engine, coefficients=None):
        self.engine = engine
        self.data = {Q:int(n) for Q, n in (coefficients or {}).items() if n}

    def list(self):
        return sorted(self.data.items(), key=lambda pair:pair[0].fingerprint())

    def support(self):
        return [Q for Q, n in self.list()]

    def degree(self):
        return sum(Q.degree()*n for Q, n in self.data.items())

    def multiplicity(self, place):
        return self.data.get(place, 0)

    def is_effective(self):
        return all(n >= 0 for n in self.data.values())

    def numerator(self):
        return LocalDivisor(self.engine, {Q:n for Q, n in self.data.items() if n > 0})

    def denominator(self):
        return LocalDivisor(self.engine, {Q:-n for Q, n in self.data.items() if n < 0})

    def __add__(self, other):
        if other == 0:
            return self
        assert isinstance(other, LocalDivisor) and other.engine is self.engine
        result = dict(self.data)
        for Q, n in other.data.items():
            result[Q] = result.get(Q, 0)+n
        return LocalDivisor(self.engine, result)

    __radd__ = __add__

    def __neg__(self):
        return LocalDivisor(self.engine, {Q:-n for Q, n in self.data.items()})

    def __sub__(self, other):
        return self+(-other)

    def __mul__(self, multiplier):
        n = int(multiplier)
        assert n == multiplier
        return LocalDivisor(self.engine, {Q:n*v for Q, v in self.data.items()})

    __rmul__ = __mul__

    def __eq__(self, other):
        return (isinstance(other, LocalDivisor) and other.engine is self.engine
                and other.data == self.data)

    def __repr__(self):
        return "Original local divisor: %s places, degree %s"%(len(self.data), self.degree())


class LocalSourcePlace:
    def __init__(self, engine, base_place, path, state):
        self.engine = engine
        self.base_place = base_place
        self.path = path
        self.key = (native_place_hash(base_place), path)
        self.state = state
        self.absolute_degree = int(state["residue"].degree())
        assert self.absolute_degree % 2 == 0
        self.original_degree = self.absolute_degree//2
        self.relative_residue_degree = self.absolute_degree//int(base_place.degree())
        assert self.relative_residue_degree*int(base_place.degree()) == self.absolute_degree
        self.ramification_index = int(state["ramification"])
        self.delta_residue = state["generators"][0][0]
        assert self.delta_residue**2 == -3
        assert self.delta_residue**engine.r == -self.delta_residue

    def __hash__(self):
        return hash((id(self.engine), self.key))

    def __eq__(self, other):
        return (isinstance(other, LocalSourcePlace) and other.engine is self.engine
                and other.key == self.key)

    def degree(self):
        """Degree over the original F_(r^2), NOT over the quotient F_r."""
        return self.original_degree

    def fingerprint(self):
        return digest({
            "base_place":self.key[0], "path":list(self.path),
            "absolute_Fp_degree":self.absolute_degree,
            "original_Fp2_degree":self.original_degree,
            "ramification":self.ramification_index,
            "original_delta_residue":residue_coordinates(self.delta_residue),
            "residue_modulus":[int(a) for a in self.state["residue"].modulus().list()]})

    def residue_field(self):
        # The existing consumer uses only the final reduction map; no
        # unsupported inverse residue lifting is advertised.
        def reduce_value(value):
            return self.engine.reduce_at(self, value)
        return self.state["residue"], None, reduce_value

    def __repr__(self):
        return "Original Y place %s (degree %s)"%(self.fingerprint()[:16], self.degree())


def map_series(series, coefficient_map, parameter_image, cutoff=None):
    """Exact Laurent substitution with every omitted-tail error retained."""
    S = parameter_image.parent()
    parameter_order = int(parameter_image.valuation())
    assert parameter_order > 0
    bound = series.precision_absolute()
    if series.is_zero():
        if bound == infinity:
            return S.zero()
        result = S.zero().add_bigoh(parameter_order*int(bound))
    else:
        val = int(series.valuation())
        ring = PolynomialRing(S.base_ring(), "local_substitution")
        # list() starts at the Laurent valuation.  Exact finite polynomials
        # (in particular an unchanged local parameter) need no artificial
        # tail; inexact inputs retain their true absolute precision below.
        unit = ring([coefficient_map(c) for c in series.list()])
        result = unit(parameter_image)*parameter_image**val
        if bound != infinity:
            result = result.add_bigoh(parameter_order*int(bound))
    if cutoff is not None:
        result = result.add_bigoh(int(cutoff))
    return result

def absolute_residual_factor(field, factor, tag):
    """Native finite field and its ACTUAL embedding; polynomial quotient avoided."""
    degree = int(factor.degree())
    if degree == 1:
        return field, (lambda x:x), -factor[0]/factor[1]
    extension, embedding = field.extension(ZZ(degree), "res_"+tag[:14], map=True)
    assert embedding is not None
    R = PolynomialRing(extension, "residual_root")
    transported = R([embedding(a) for a in factor.list()])
    roots = transported.roots(multiplicities=False)
    assert len(roots) == degree
    root = min(roots, key=lambda x:tuple(residue_coordinates(x)))
    assert transported(root) == 0
    assert extension.cardinality() == field.cardinality()**degree
    return extension, embedding, root


def normalized_unit_root(series, exponent, starting_root):
    """Only exponent=2 or3 is inverted, at a specified nonzero residual root."""
    if series.is_zero() or series.valuation() != 0:
        raise NeedMorePrecision("The normalized Kummer unit is not yet visible.")
    precision = int(series.precision_absolute())
    if precision < 2:
        raise NeedMorePrecision("Need at least two unit coefficients.")
    S = series.parent()
    R = PolynomialRing(S.base_ring(), "unit_root_variable")
    p = R([series[i] for i in range(precision)])
    root = p._nth_root_series(int(exponent), precision, start=starting_root)
    result = S(root).add_bigoh(precision)
    assert (result**exponent-series).is_zero()
    return result


def ramified_quadratic_parameter(unit):
    """Invert u^2=s*h(s), retaining the ORIGINAL residue field."""
    if unit.is_zero() or unit.valuation() != 0:
        raise NeedMorePrecision("Quadratic ramification unit not yet visible.")
    old_precision = int(unit.precision_absolute())
    if old_precision < 2:
        raise NeedMorePrecision("Quadratic unit precision is insufficient.")
    field = unit.parent().base_ring()
    precision = 2*old_precision
    S = LaurentSeriesRing(field, "ramified_parameter", default_prec=precision)
    u = S.gen()
    R = PolynomialRing(field, "old_parameter")
    h = R([unit[i] for i in range(old_precision)])
    eta = (u**2/h[0]).add_bigoh(4)
    known = 4
    while known < precision:
        target = min(2*known, precision)
        # Truncated h is safe through 2*old_precision after s=eta~u^2.
        eta = eta.lift_to_precision(target)
        error = eta*h(eta)-u**2
        derivative = h(eta)+eta*h.derivative()(eta)
        assert derivative.valuation() == 0
        eta = (eta-error/derivative).add_bigoh(target)
        assert (eta*h(eta)-u**2).is_zero()
        known = target
    assert eta.valuation() == 2
    return S, eta


class OriginalLocalDivisorEngine:
    def __init__(self, rr, six, initial_precision=16):
        self.rr, self.six = rr, six
        self.r = int(six["prime"])
        assert self.r in (29, 41)
        self.original = six["field"]
        self.k2 = six["constants"]
        self.omega = six["omega"]
        self.delta_original = 1+2*self.omega
        assert self.k2.cardinality() == self.r**2
        assert self.delta_original**2 == -3
        assert self.delta_original**self.r == -self.delta_original
        self.initial_precision = int(initial_precision)
        assert self.initial_precision >= 8
        self.layers, self.fields, self.original_images = [], [], []
        self._flatten_cache, self._source_cache = {}, {}
        self._coefficient_divisors, self._source_divisors = {}, {}
        self._family_cache, self._root_cache = {}, {}
        self._completion_cache = {}
        self._coefficient_expansions = {}
        self.fixed_bad_places = set()

        eta, T = six["eta"], six["T"]
        if rr.get("full_atkin_quotient") is not None:
            self.kind = "full_atkin_genus19"
            self.base = rr["full_atkin_quotient"]
            self.base_into_original = self.base.hom([
                (T+729*eta**12/T)/eta**6, eta+1/eta])
            self.fields = [self.base]
            delta = self._add_layer("constant_delta", 2, self.base(-3),
                                    self.original(self.delta_original))
            s, L = self.base(self.base.base_field().gen()), self.base.gen()
            uu = self._add_layer("atkin_u", 2, self.fields[-1](s**2-4),
                                 eta-1/eta)
            vv = self._add_layer("atkin_v", 2, self.fields[-1](L**2-2916),
                                 (T-729*eta**12/T)/eta**6)
            current = self.fields[-1]
            t_model = (current(s)+current(uu))/2
            T_model = t_model**6*(current(L)+current(vv))/2
        elif rr.get("fricke_quotient") is not None:
            self.kind = "fricke_genus37"
            self.base = rr["fricke_quotient"]
            self.base_into_original = self.base.hom([T+729*eta**12/T, eta])
            self.fields = [self.base]
            delta = self._add_layer("constant_delta", 2, self.base(-3),
                                    self.original(self.delta_original))
            t, J = self.base(self.base.base_field().gen()), self.base.gen()
            ww = self._add_layer("fricke_w", 2,
                                 self.fields[-1](J**2-2916*t**12),
                                 T-729*eta**12/T)
            current = self.fields[-1]
            t_model = current(t)
            T_model = (current(J)+current(ww))/2
        else:
            self.kind = "native_eta48_genus85"
            self.base = rr["field"]
            assert self.base.degree() == 48
            self.base_into_original = self.base.hom([T, eta])
            self.fields = [self.base]
            delta = self._add_layer("constant_delta", 2, self.base(-3),
                                    self.original(self.delta_original))
            current = self.fields[-1]
            t_model = current(self.base.base_field().gen())
            T_model = current(self.base.gen())

        self.fp = self.base.constant_base_field()
        assert self.fp.cardinality() == self.r
        current = self.fields[-1]
        delta = current(delta)
        ys = six["ys"]
        z_image = ys*(ys**2-9)/(ys**2-1)
        zz = self._add_layer("source_z2", 2, current(T_model), z_image)
        current = self.fields[-1]
        delta, zz = current(delta), current(zz)
        rhs = (zz-3*delta)/(zz+3*delta)
        cc = self._add_layer("source_c3", 3, rhs,
                            (ys-self.delta_original)/(ys+self.delta_original))
        self.tower = self.fields[-1]
        self.delta = self.tower(delta)
        self.t_model = self.tower(t_model)
        self.T_model = self.tower(T_model)
        self.y_model = self.delta*(1+self.tower(cc))/(1-self.tower(cc))
        self.relative_degree = 1
        for layer in self.layers:
            self.relative_degree *= layer["exponent"]
        expected = {"full_atkin_genus19":48, "fricke_genus37":24,
                    "native_eta48_genus85":12}[self.kind]
        assert self.relative_degree == expected

        # Actual inverse identities, including source constants and BOTH
        # original rational generators.  No arbitrary Kummer twist is used.
        assert self.from_tower(self.t_model) == eta
        assert self.from_tower(self.T_model) == T
        assert self.from_tower(self.y_model) == ys
        assert self.to_tower(self.original(self.delta_original)) == self.delta
        assert self.y_model**2*(self.y_model**2-9)**2 == (
            self.T_model*(self.y_model**2-1)**2)
        source_base = six["inject_base"].domain()
        value = self.tower.zero()
        for coefficient in reversed(source_base.polynomial().list()):
            value = value*self.T_model+self.map_source_rational(coefficient)
        assert value == 0

        # Only native orders on the already produced small quotient are used.
        self.base.maximal_order()
        self.base.maximal_order_infinite()
        for layer in self.layers:
            for powers, coefficient in layer["coefficients"]:
                if coefficient:
                    self.fixed_bad_places.update(
                        self.native_divisor(coefficient).denominator().support())
        progress("original local tower initialized",
                 quotient=self.kind, quotient_degree=int(self.base.degree()),
                 source_relative_degree_over_Fp_quotient=self.relative_degree,
                 constant_extension_degree=2,
                 fixed_bad_base_places=len(self.fixed_bad_places),
                 fields_not_globally_normalized=[
                     layer["label"] for layer in self.layers])

    def flatten(self, value, depth=None):
        if depth is None:
            depth = len(self.layers)
        field = self.fields[depth]
        value = field(value)
        key = (depth, value)
        if key in self._flatten_cache:
            return self._flatten_cache[key]
        if depth == 0:
            result = [((), self.base(value))] if value else []
        else:
            result = []
            for exponent, coefficient in enumerate(value.list()):
                if coefficient:
                    for powers, base_coefficient in self.flatten(coefficient, depth-1):
                        result.append((powers+(exponent,), base_coefficient))
        self._flatten_cache[key] = result
        return result

    def _add_layer(self, label, exponent, rhs, original_image):
        depth = len(self.layers)
        previous = self.fields[-1]
        rhs = previous(rhs)
        assert rhs != 0
        coefficients = self.flatten(rhs, depth)
        R = PolynomialRing(previous, label)
        field = previous.extension(R.gen()**exponent-rhs, label)
        # This equality is in the SAME original simple source field.
        original_rhs = self.original.zero()
        for powers, coefficient in coefficients:
            term = self.base_into_original(coefficient)
            for image, n in zip(self.original_images, powers):
                term *= image**n
            original_rhs += term
        original_image = self.original(original_image)
        assert original_image**exponent == original_rhs
        self.layers.append({
            "label":label, "exponent":int(exponent), "rhs":rhs,
            "coefficients":coefficients})
        self.fields.append(field)
        self.original_images.append(original_image)
        return field.gen()

    def from_tower(self, value):
        result = self.original.zero()
        for powers, coefficient in self.flatten(value):
            term = self.base_into_original(coefficient)
            for image, n in zip(self.original_images, powers):
                term *= image**n
            result += term
        return result

    def map_source_constant(self, value):
        value = self.k2(value)
        # The chosen original delta, not a new residue square root convention.
        a = self.fp((value+value**self.r)/2)
        b = self.fp((value-value**self.r)/(2*self.delta_original))
        assert self.k2(a)+self.k2(b)*self.delta_original == value
        return self.tower(a)+self.tower(b)*self.delta

    def map_source_rational(self, value):
        def polynomial(p):
            result = self.tower.zero()
            for c in reversed(p.list()):
                result = result*self.t_model+self.map_source_constant(c)
            return result
        numerator = polynomial(value.numerator())
        denominator = polynomial(value.denominator())
        assert denominator
        return numerator/denominator

    def to_tower(self, value):
        value = self.original(value)
        if value in self._source_cache:
            return self._source_cache[value]
        result = self.tower.zero()
        for coefficient in reversed(value.list()):
            result = result*self.y_model+self.map_source_rational(coefficient)
        self._source_cache[value] = result
        return result

    def native_divisor(self, coefficient):
        coefficient = self.base(coefficient)
        assert coefficient
        if coefficient not in self._coefficient_divisors:
            self._coefficient_divisors[coefficient] = coefficient.divisor()
        return self._coefficient_divisors[coefficient]

    def norm_to_base(self, value):
        current = self.tower(value)
        assert current
        for depth in range(len(self.layers), 0, -1):
            assert current.parent() is self.fields[depth]
            current = current.norm()
        return self.base(current)

    def completion(self, place):
        if place not in self._completion_cache:
            name = "b_"+native_place_hash(place)[:12]
            self._completion_cache[place] = self.base.completion(
                place, name="base_parameter", prec=self.initial_precision,
                gen_name=name)
        return self._completion_cache[place]

    def evaluate_coefficients(self, coefficients, state, precision):
        """Evaluate a true tower-basis expression, including its tail errors."""
        S = state["series"]
        result = S.zero()
        comp = self.completion(state["base_place"])
        for powers, coefficient in coefficients:
            if not coefficient:
                continue
            expansion_key = (state["base_place"], coefficient, int(precision))
            if expansion_key not in self._coefficient_expansions:
                self._coefficient_expansions[expansion_key] = comp(coefficient, int(precision))
            expansion = self._coefficient_expansions[expansion_key]
            term = map_series(expansion, state["base_embedding"],
                              state["base_parameter"])
            for generator, exponent in zip(state["generators"], powers):
                if exponent:
                    term *= generator**exponent
            result += term
        return result

    def transformed_state(self, state, target_series, field_map, parameter):
        return {
            "base_place":state["base_place"],
            "series":target_series, "residue":target_series.base_ring(),
            "base_embedding":(
                lambda c, f=field_map, g=state["base_embedding"]:f(g(c))),
            "base_parameter":map_series(state["base_parameter"], field_map, parameter),
            "generators":[map_series(g, field_map, parameter)
                          for g in state["generators"]],
            "ramification":state["ramification"],
            "path":state["path"],
        }

    def extend_state(self, state, layer, precision):
        value = self.evaluate_coefficients(layer["coefficients"], state, precision)
        if value.is_zero():
            raise NeedMorePrecision("Kummer right-hand side still cancels.")
        order = int(value.valuation())
        e = layer["exponent"]
        quotient, remainder = divmod(order, e)
        S = state["series"]
        parameter = S.gen()
        unit = value*parameter**(-order)
        if int(unit.precision_absolute()) < 2:
            raise NeedMorePrecision("Kummer leading unit has too little precision.")
        if remainder:
            assert e == 2 and remainder == 1, (
                "The ORIGINAL cubic layer is everywhere unramified.")
            target, old_parameter = ramified_quadratic_parameter(unit)
            child = self.transformed_state(
                state, target, lambda c:c, old_parameter)
            root = target.gen()*old_parameter**quotient
            child["generators"].append(root)
            child["ramification"] *= 2
            child["path"] += (layer["label"]+":ramified",)
            # Full actual RHS, not just its leading term.
            rhs_image = map_series(value, lambda c:c, old_parameter)
            assert (root**2-rhs_image).is_zero()
            return [child]

        field = state["residue"]
        P = PolynomialRing(field, "residual_kummer")
        residual = P.gen()**e-unit[0]
        factors = list(residual.factor())
        assert all(multiplicity == 1 for factor, multiplicity in factors)
        factors.sort(key=lambda fm:tuple(tuple(residue_coordinates(c))
                                       for c in fm[0].list()))
        assert sum(int(factor.degree()) for factor, multiplicity in factors) == e
        if e == 3:
            # The actual constant delta layer already supplies all mu_3.
            assert all(int(factor.degree()) in (1, 3) for factor, multiplicity in factors)
        result = []
        for index, (factor, multiplicity) in enumerate(factors):
            signature = digest([residue_coordinates(c) for c in factor.list()])
            path_token = layer["label"]+":unramified:"+str(index)+":"+signature
            key = (native_place_hash(state["base_place"]), state["path"], path_token)
            if key not in self._root_cache:
                self._root_cache[key] = absolute_residual_factor(
                    field, factor, digest(list(map(str, key))))
            extension, embedding, residual_root = self._root_cache[key]
            assert sum((embedding(factor[i])*residual_root**i
                        for i in range(factor.degree()+1)), extension.zero()) == 0
            target = LaurentSeriesRing(extension, "unramified_parameter",
                                       default_prec=int(unit.precision_absolute()))
            child = self.transformed_state(state, target, embedding, target.gen())
            unit_image = map_series(unit, embedding, target.gen())
            if layer["label"] == "constant_delta":
                # This is the exact constant field, not a truncated local root.
                assert order == 0 and e == 2 and residual_root**2 == extension(-3)
                root = target(residual_root)
            else:
                root_unit = normalized_unit_root(unit_image, e, residual_root)
                root = target.gen()**quotient*root_unit
            child["generators"].append(root)
            child["path"] += (path_token,)
            assert (root**e-map_series(value, embedding, target.gen())).is_zero()
            result.append(child)
        return result

    def build_family(self, place, precision):
        comp = self.completion(place)
        field = comp.codomain().base_ring()
        assert int(field.degree()) == int(place.degree())
        S = LaurentSeriesRing(field, "base_parameter", default_prec=precision)
        states = [{
            "base_place":place, "series":S, "residue":field,
            "base_embedding":lambda c:c, "base_parameter":S.gen(),
            "generators":[], "ramification":1, "path":(),
        }]
        for layer in self.layers:
            expanded = []
            for state in states:
                expanded.extend(self.extend_state(state, layer, precision))
            states = expanded
        total = 0
        for state in states:
            residual_degree = int(state["residue"].degree())//int(place.degree())
            assert residual_degree*int(place.degree()) == int(state["residue"].degree())
            total += int(state["ramification"])*residual_degree
            assert int(state["residue"].degree()) % 2 == 0
        assert total == self.relative_degree
        return states

    def family(self, place, precision=None):
        previous = self._family_cache.get(place)
        requested = max(self.initial_precision, int(precision or self.initial_precision))
        if previous is not None and previous["precision"] >= requested:
            return previous
        actual = max(requested, previous["precision"] if previous else 0)
        while True:
            try:
                states = self.build_family(place, actual)
                break
            except NeedMorePrecision:
                actual *= 2
                progress("original local Kummer refinement",
                         base_place=native_place_hash(place), precision=actual)
        old_places = previous["places"] if previous else {}
        new_places = {}
        for state in states:
            path = state["path"]
            if path in old_places:
                Q = old_places[path]
                assert Q.state["residue"] is state["residue"]
                assert Q.ramification_index == state["ramification"]
                Q.state = state
            else:
                Q = LocalSourcePlace(self, place, path, state)
            new_places[path] = Q
        if previous:
            assert set(new_places) == set(old_places)
        result = {"precision":actual, "places":new_places}
        self._family_cache[place] = result
        return result

    def values_at_base(self, base_place, tower_value):
        coefficients = self.flatten(tower_value)
        family = self.family(base_place)
        while True:
            values = {}
            try:
                for Q in family["places"].values():
                    series = self.evaluate_coefficients(
                        coefficients, Q.state, family["precision"])
                    if series.is_zero():
                        raise NeedMorePrecision("A nonzero source function still cancels.")
                    values[Q] = series
                return values
            except NeedMorePrecision:
                family = self.family(base_place, 2*family["precision"])

    def divisor(self, source_value):
        source_value = self.original(source_value)
        assert source_value != 0
        if source_value in self._source_divisors:
            return self._source_divisors[source_value]
        tower_value = self.to_tower(source_value)
        coefficients = self.flatten(tower_value)
        norm = self.norm_to_base(tower_value)
        norm_divisor = self.native_divisor(norm)
        candidates = set(norm_divisor.support()) | self.fixed_bad_places
        for powers, coefficient in coefficients:
            if coefficient:
                candidates.update(self.native_divisor(coefficient).denominator().support())
        progress("original local divisor candidate support complete",
                 quotient=self.kind, candidate_base_places=len(candidates),
                 original_function_sha256=native_function_hash(source_value),
                 norm_sha256=native_function_hash(norm))
        output = {}
        for index, place in enumerate(sorted(candidates, key=native_place_hash)):
            values = self.values_at_base(place, tower_value)
            norm_order = 0
            for Q, series in values.items():
                order = int(series.valuation())
                norm_order += Q.relative_residue_degree*order
                if order:
                    output[Q] = order
            assert norm_order == norm_divisor.multiplicity(place)
            if index % 20 == 19 or index+1 == len(candidates):
                progress("original local divisor exact branches",
                         completed=index+1, total=len(candidates),
                         nonzero_source_places=len(output))
        result = LocalDivisor(self, output)
        assert result.degree() == 0
        self._source_divisors[source_value] = result
        progress("original local divisor complete",
                 nonzero_source_places=len(output), total_degree=0,
                 positive_degree=result.numerator().degree(),
                 negative_degree=result.denominator().degree(),
                 full_record_sha256=digest([
                     [Q.fingerprint(), n] for Q, n in result.list()]))
        return result

    def poles(self, source_value):
        return self.divisor(source_value).denominator()

    def reduce_at(self, source_place, source_value):
        source_value = self.original(source_value)
        if not source_value:
            return source_place.state["residue"].zero()
        value = self.to_tower(source_value)
        coefficients = self.flatten(value)
        family = self.family(source_place.base_place)
        while True:
            Q = family["places"][source_place.path]
            assert Q == source_place
            series = self.evaluate_coefficients(
                coefficients, Q.state, family["precision"])
            if series.is_zero():
                if series.precision_absolute() > 0:
                    return Q.state["residue"].zero()
            else:
                order = int(series.valuation())
                if order < 0:
                    raise ValueError("The ORIGINAL source function has a pole at this branch.")
                return Q.state["residue"].zero() if order else series[0]
            family = self.family(source_place.base_place, 2*family["precision"])
