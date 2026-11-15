#!/usr/bin/env python3
"""R178 fixed-color-priority right-word map, with no cycle fallback.

No research entry point.  A caller must enforce public Actions for actual
targets.  Local artificial checks below exercise only invented identities.
Nonzero representatives have no functional nonmembership interpretation.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json

import literature_colored_profile_algebra as colored
import literature_pure_bulk_exact_membership as exact
import literature_pure_bulk_word_normal_form as words

SCHEMA = "visible-flex-fixed-color-priority-word-map-v1"
ORDER = ("q", "qbar")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def rows(value):
    return [[local, word, coefficient.numerator, coefficient.denominator]
            for (local, word), coefficient in sorted(value.terms.items())]


def local_key(raw, color_order=ORDER):
    if not isinstance(raw, (tuple, list)) or len(raw) != 2:
        raise ValueError("word local monomial needs power and colored jets")
    power, jets = raw
    if type(power) is not int or power < 0:
        raise ValueError("the proved R178 layer has nonnegative xi powers")
    answer = []
    for jet in jets:
        if (not isinstance(jet, (tuple, list)) or len(jet) != 2
            or jet[0] not in color_order or type(jet[1]) is not int or jet[1] < 0):
            raise ValueError("invalid colored jet or undeclared color")
        answer.append((jet[0], jet[1]))
    if answer != sorted(answer):
        raise ValueError("colored jet multisets must be canonical")
    return power, tuple(answer)


def word_key(raw, color_order=ORDER):
    answer = tuple(local_key(item, color_order) for item in raw)
    if any(not item[1] for item in answer):
        raise ValueError("a surviving word letter must have positive profile weight")
    return answer


def is_remainder_letter(local, color_order=ORDER):
    local = local_key(local, color_order)
    if not local[1]:
        return False
    priority = {color:index for index,color in enumerate(color_order)}
    color = max((jet[0] for jet in local[1]), key=priority.__getitem__)
    order = max(jet for kind,jet in local[1] if kind==color)
    return order==0 or local[1].count((color,order))>=2


def decode_rows(owner, payload):
    terms = {}
    previous = None
    for local, word, numerator, denominator in payload:
        key = (local_key(local, owner.color_order), word_key(word, owner.color_order))
        if (type(numerator) is not int or type(denominator) is not int
            or numerator == 0 or denominator <= 0
            or (previous is not None and key <= previous)):
            raise ValueError("word rows must be sorted, unique, nonzero rational terms")
        value = F(numerator, denominator)
        if value.numerator != numerator or value.denominator != denominator:
            raise ValueError("word rationals must already be reduced")
        terms[key] = owner.limits.rational(value)
        previous = key
    return words.WordExpr(owner, terms)


def embed_pure_rows(owner, payload):
    """Read an archived q-only representative; perform no normalization."""
    converted = []
    for local, word, numerator, denominator in payload:
        def one(item):
            power, jets = item
            if any(type(order) is not int or order < 0 for order in jets):
                raise ValueError("invalid archived pure jet")
            return [power, [["q", order] for order in jets]]
        converted.append([one(local), [one(letter) for letter in word],
                          numerator, denominator])
    return decode_rows(owner, converted)


class PriorityWords(colored.ColoredWords):
    """Theorem R178; fixed color first, jet order second.

    Completed cache entries may be persisted.  An active recursive key is an
    implementation error, never a reason to retain an unnormalized raw word.
    """
    def __init__(self, ring, max_calls=250000, max_terms=80000,
                 max_weight=4, max_shuffle_entries=100000,
                 max_cache_entries=250000, color_order=ORDER):
        super().__init__(ring, max_calls, max_terms, max_weight, max_shuffle_entries)
        if len(set(color_order)) != len(color_order) or not color_order:
            raise ValueError("one fixed strict color order is required")
        self.color_order = tuple(color_order)
        self.priority = {color: index for index, color in enumerate(color_order)}
        self.max_cache_entries = max_cache_entries
        self.run_primitive_calls = 0
        self.stats["fixed_color_IBP"] = 0
        self.stats["strict_descent_checks"] = 0
        self.stats["cache_entries_peak"] = 0

    def check_terms(self, terms):
        super().check_terms(terms)
        for (local, word), value in terms.items():
            local_key(local, self.color_order)
            for letter in word:
                local_key(letter, self.color_order)
            self.limits.rational(value)

    def cache_guard(self):
        count = sum(len(cache) for cache in
                    (self.atom_cache, self.monomial_cache,
                     self.primitive_cache, self.shuffle_cache))
        self.stats["cache_entries_peak"] = max(self.stats["cache_entries_peak"], count)
        if count > self.max_cache_entries:
            raise exact.formal.CompilationBudgetExceeded("fixed-color shared cache entry ceiling")

    def selected_jet(self, local):
        jets = local[1]
        if not jets:
            return None
        if any(color not in self.priority for color, _ in jets):
            raise ValueError("color outside the frozen priority order")
        color = max((jet[0] for jet in jets), key=self.priority.__getitem__)
        order = max(j for c, j in jets if c == color)
        return color, order

    def measure(self, local, word):
        selected = self.selected_jet(local)
        return len(word), -1 if selected is None else selected[1]

    def smaller(self, local, word, parent):
        if not self.measure(local, word) < parent:
            raise AssertionError("R178 recursive word/priority-jet measure did not descend")
        self.stats["strict_descent_checks"] += 1
        return self.primitive(local, word)

    def primitive(self, local, word):
        local = local_key(local, self.color_order)
        word = word_key(word, self.color_order)
        key = (local, word)
        if key in self.primitive_cache:
            return self.primitive_cache[key]
        if self.run_primitive_calls >= self.max_calls:
            raise exact.formal.CompilationBudgetExceeded("fixed-color primitive call ceiling")
        self.run_primitive_calls += 1
        self.stats["primitive_calls"] += 1
        self.limits.check()
        if key in self.active:
            raise AssertionError("R178 strict descent forbids an active recursion cycle")
        self.active.add(key)
        try:
            power, jets = local
            parent = self.measure(local, word)
            selected = self.selected_jet(local)
            answer = None
            if selected is not None and selected[1] >= 1 and jets.count(selected) == 1:
                factors = list(jets)
                factors.remove(selected)
                factors.append((selected[0], selected[1]-1))
                antiderivative = (power, tuple(sorted(factors)))
                differential = colored.colored_local_derivative(antiderivative)
                coefficient = differential.pop(local, F(0))
                if coefficient <= 0:
                    raise AssertionError("the selected highest-color derivative is absent")
                answer = self.term(antiderivative, word)
                for remainder, value in sorted(differential.items()):
                    answer -= self.smaller(remainder, word, parent).scale(value)
                if word:
                    answer -= self.smaller(words.local_product(antiderivative, word[0]),
                                           word[1:], parent)
                answer = answer.scale(1/coefficient)
                self.stats["unique_high_jet_IBP"] += 1
                self.stats["fixed_color_IBP"] += 1
            elif not jets:
                if not word:
                    raise ValueError("I of a zero-profile polynomial needs its right-end constant")
                antiderivative = (power+1, ())
                answer = (self.term(antiderivative, word)
                          - self.smaller(words.local_product(antiderivative, word[0]),
                                         word[1:], parent)).scale(F(1, power+1))
                self.stats["nonempty_word_polynomial_IBP"] += 1
            if answer is None:
                answer = self.term(words.ONE, (local,)+word)
            self.primitive_cache[key] = answer
            try:
                self.cache_guard()
            except exact.formal.CompilationBudgetExceeded:
                self.primitive_cache.pop(key, None)
                raise
            return answer
        finally:
            self.active.remove(key)

    def atom(self, atom):
        existed = atom in self.atom_cache
        try:
            answer = super().atom(atom)
            self.cache_guard()
            return answer
        except exact.formal.CompilationBudgetExceeded:
            if not existed:
                self.atom_cache.pop(atom, None)
            raise

    def monomial(self, monomial):
        existed = monomial in self.monomial_cache
        try:
            answer = super().monomial(monomial)
            self.cache_guard()
            return answer
        except exact.formal.CompilationBudgetExceeded:
            if not existed:
                self.monomial_cache.pop(monomial, None)
            raise

    def shuffle(self, left, right):
        key = (left, right) if left <= right else (right, left)
        existed = key in self.shuffle_cache
        try:
            answer = super().shuffle(left, right)
            self.cache_guard()
            return answer
        except exact.formal.CompilationBudgetExceeded:
            if not existed:
                self.shuffle_cache.pop(key, None)
            raise

    def expression(self, expression):
        if expression.ring is not self.ring:
            raise ValueError("one original ring and common right anchor are required")
        terms = {}
        for monomial, coefficient in sorted(expression.terms.items()):
            for key, value in self.monomial(monomial).terms.items():
                words.add_term(terms, key, self.limits.rational(coefficient*value))
            if len(terms) > self.max_terms:
                raise exact.formal.CompilationBudgetExceeded("fixed-color expression term ceiling")
            self.limits.check()
        return words.WordExpr(self, terms)

    def snapshot(self, max_bytes=40000000):
        """Only completed calls; a budget-stopped recursive branch is not a result."""
        if self.active:
            raise ValueError("unwind a stopped recursive branch before checkpointing")
        pool = []
        references = {}
        pool_bytes = 0

        def ref(value):
            nonlocal pool_bytes
            raw = rows(value)
            key = digest(raw)
            if key not in references:
                pool_bytes += len(canonical(raw))
                if pool_bytes > max_bytes:
                    raise exact.formal.CompilationBudgetExceeded("shared-cache expression-pool byte ceiling")
                references[key] = len(pool)
                pool.append({"sha256": key, "rows": raw})
            elif pool[references[key]]["rows"] != raw:
                raise AssertionError("word checkpoint digest collision")
            return references[key]

        payload = {
            "schema": SCHEMA+"-cache", "color_order": list(self.color_order),
            "expression_pool": pool,
            "atom_cache": [[key, ref(value)] for key, value in sorted(self.atom_cache.items())],
            "monomial_cache": [[key, ref(value)] for key, value in sorted(self.monomial_cache.items())],
            "primitive_cache": [[key, ref(value)] for key, value in sorted(self.primitive_cache.items())],
            "shuffle_cache": [[left, right, [[word, count] for word, count in sorted(answer.items())]]
                              for (left, right), answer in sorted(self.shuffle_cache.items())],
            "statistics": dict(self.stats),
            "started_primitive_calls_in_this_run_including_a_stopped_call": self.run_primitive_calls,
            "declared_additional_call_budget_in_this_run": self.max_calls,
            "active_unfinished_calls_included_as_results": False,
        }
        return payload

    def restore(self, data):
        if (data.get("schema") != SCHEMA+"-cache"
            or tuple(data.get("color_order", ())) != self.color_order
            or data.get("active_unfinished_calls_included_as_results") is not False):
            raise ValueError("checkpoint is not the same fixed-color map")
        if any((self.atom_cache, self.monomial_cache, self.primitive_cache, self.shuffle_cache)):
            raise ValueError("restore into a fresh mapper")
        pool = []
        for row in data["expression_pool"]:
            if digest(row["rows"]) != row["sha256"]:
                raise ValueError("stored completed word value changed")
            pool.append(decode_rows(self, row["rows"]))

        def read_table(name, convert):
            out = {}
            for key, index in data[name]:
                key = convert(key)
                if key in out or type(index) is not int or not 0 <= index < len(pool):
                    raise ValueError("invalid shared-cache key or expression index")
                out[key] = pool[index]
            return out

        def atom_key(index):
            if type(index) is not int or not 0 <= index < len(self.ring.p.atoms):
                raise ValueError("saved atom is outside the bound original ring")
            return index

        def original_monomial(raw):
            power, atoms = raw
            if type(power) is not int or power < 0 or list(atoms) != sorted(atoms):
                raise ValueError("invalid original monomial cache key")
            for atom in atoms:
                atom_key(atom)
            return power, tuple(atoms)

        self.atom_cache = read_table("atom_cache", atom_key)
        self.monomial_cache = read_table("monomial_cache", original_monomial)
        self.primitive_cache = read_table("primitive_cache",
            lambda key: (local_key(key[0], self.color_order), word_key(key[1], self.color_order)))
        self.shuffle_cache = {}
        for left, right, answer in data["shuffle_cache"]:
            key = (word_key(left, self.color_order), word_key(right, self.color_order))
            if key in self.shuffle_cache:
                raise ValueError("duplicate saved shuffle key")
            value = {}
            for word, count in answer:
                word = word_key(word, self.color_order)
                if word in value or type(count) is not int or count <= 0:
                    raise ValueError("invalid saved exact shuffle multiplicity")
                value[word] = count
            self.shuffle_cache[key] = value
        saved = data["statistics"]
        if set(saved) != set(self.stats) or any(type(v) is not int or v < 0 for v in saved.values()):
            raise ValueError("invalid completed-map statistics")
        if saved["cycle_fallbacks"] != 0:
            raise ValueError("the fixed-priority theorem has no fallback branch")
        self.stats = dict(saved)
        self.run_primitive_calls = 0
        self.cache_guard()


def artificial_checks():
    limits = exact.Limits(seconds=30, memory_mib=512, terms=4000,
                          rewrites=20000, rational_bits=2048)
    ring = colored.ColoredRing(limits)
    q, qb, x = ring.color("q"), ring.color("qbar"), ring.x()
    mapper = PriorityWords(ring, max_calls=20000, max_terms=4000)
    checks = {}
    identity = (q.D()*qb.D()).I()-q.D()*qb+(q.D().D()*qb).I()
    assert not mapper.expression(identity).terms
    checks["mixed_tied_derivative_identity_uses_fixed_color_not_global_jet_order"] = True
    expected = mapper.term(words.ONE, ((0, (("q", 2), ("qbar", 0))),))
    assert mapper.expression((q.D().D()*qb).I()).terms == expected.terms
    checks["highest_color_zero_jet_stops_even_with_higher_lower_color_jets"] = True
    potential = x*q.D()*qb*qb+q.D().D()*qb.D()
    assert not mapper.expression(potential.D().I()-potential).terms
    checks["mixed_local_total_derivative_recovers_its_zero_right_collar_potential"] = True
    potential = q*qb.D()
    identity = (potential.D()*q.I()).I()-potential*q.I()+(potential*q).I()
    assert not mapper.expression(identity).terms
    checks["nonempty_word_IBP_pays_the_derivative_of_the_remaining_word"] = True
    identity = q.I()*q.I()-2*(q*q.I()).I()
    assert not mapper.expression(identity).terms
    checks["all_depth_shuffle_keeps_repeated_letter_multiplicity"] = True
    identity = (x*q.I()).I()-x*x*q.I()/2+(x*x*q).I()/2
    assert not mapper.expression(identity).terms
    failed = False
    try:
        mapper.expression(x.I())
    except ValueError:
        failed = True
    assert failed
    checks["nonempty_polynomial_letter_boundary_paid_and_empty_boundary_not_discarded"] = True
    invented = [(q.D()*qb.D()).I(), (q*qb.D()*q.I()).I(), x*q.I()*qb.I()]
    first = [mapper.expression(value).digest() for value in invented]
    other = PriorityWords(ring, max_calls=20000, max_terms=4000)
    second = {}
    for i in reversed(range(len(invented))):
        second[i] = other.expression(invented[i]).digest()
    assert first == [second[i] for i in range(len(invented))]
    checks["cache_insertion_order_does_not_change_the_fixed_map"] = True
    old = words.WordNormalizer(ring, max_calls=20000, max_terms=4000)
    fake_archived = old.expression((q.D()*q.D()).I()+q*q.I())
    embedded = embed_pure_rows(mapper, rows(fake_archived))
    assert embedded.terms == mapper.expression((q.D()*q.D()).I()+q*q.I()).terms
    checks["artificial_archived_monochrome_rows_read_without_renormalizing_an_input"] = True
    state = json.loads(canonical(mapper.snapshot()))
    resumed = PriorityWords(ring, max_calls=20000, max_terms=4000)
    resumed.restore(state)
    before = resumed.stats["primitive_calls"]
    assert [resumed.expression(value).digest() for value in invented] == first
    assert resumed.stats["primitive_calls"] == before
    checks["completed_shared_caches_roundtrip_and_do_not_replay_primitive_work"] = True
    tiny = PriorityWords(ring, max_calls=1, max_terms=4000)
    failed = False
    try:
        tiny.expression((q.D()*qb.D()).I())
    except exact.formal.CompilationBudgetExceeded:
        failed = True
    assert failed and not tiny.active
    assert tiny.stats["cycle_fallbacks"] == 0
    checks["a_budget_stop_unwinds_and_never_becomes_a_zero_or_cycle_fallback"] = True
    assert mapper.stats["cycle_fallbacks"] == 0 and all(checks.values())
    return {"all_passed": True, "artificial_only": True,
            "real_input_files_opened": False, "checks": checks}


def artificial_resume_checks():
    """Only the new per-run call and readable-hard-limit continuation edges."""
    limits = exact.Limits(seconds=30,memory_mib=512,terms=4000,rewrites=10000)
    ring = colored.ColoredRing(limits)
    q,qb,x = ring.color("q"),ring.color("qbar"),ring.x()
    target = (x*q.D()*qb.D()).I()
    first = PriorityWords(ring,max_calls=2,max_terms=4000)
    stopped = False
    try:
        first.expression(target)
    except exact.formal.CompilationBudgetExceeded:
        stopped = True
    assert stopped and first.run_primitive_calls == 2 and first.primitive_cache
    snapshot = json.loads(canonical(first.snapshot()))
    second = PriorityWords(ring,max_calls=2,max_terms=4000)
    second.restore(snapshot)
    assert second.run_primitive_calls == 0 and second.stats["primitive_calls"] == 2
    obtained = second.expression(target)
    expected = PriorityWords(ring,max_calls=100,max_terms=4000).expression(target)
    assert obtained.terms == expected.terms
    assert second.run_primitive_calls == 2 and second.stats["primitive_calls"] == 4
    small = PriorityWords(ring,max_calls=100,max_terms=4000,max_cache_entries=1)
    stopped = False
    try:
        small.expression(q.I())
    except exact.formal.CompilationBudgetExceeded:
        stopped = True
    assert stopped and not small.active
    assert sum(map(len,(small.atom_cache,small.monomial_cache,
                       small.primitive_cache,small.shuffle_cache))) <= 1
    restored = PriorityWords(ring,max_calls=100,max_terms=4000,max_cache_entries=1)
    restored.restore(json.loads(canonical(small.snapshot())))
    byte_stop = False
    try:
        second.snapshot(max_bytes=1)
    except exact.formal.CompilationBudgetExceeded:
        byte_stop = True
    assert byte_stop
    return {"all_passed":True,"artificial_only":True,"real_input_files_opened":False,
        "checks":{
            "same_per_run_budget_resumes_only_the_unfinished_call_without_raising_the_cumulative_ceiling":True,
            "cache_ceiling_rolls_back_new_entry_and_the_saved_state_remains_readable_at_the_same_global_cap":True,
            "expression_pool_serialization_has_its_own_explicit_byte_ceiling":True},
        "previous_ten_development_checks_repeated":False}
