#!/usr/bin/env python3
"""Formal separated-profile compiler through the full fourth range.

Only exact rational/expression algebra is performed. No profile, geometric
control, numerical quadrature, ODE, or optimization is evaluated here.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import time
from typing import Iterable

Monomial = tuple[int, tuple[int, ...]]
ONE: Monomial = (0, ())


class CompilationBudgetExceeded(RuntimeError):
    """A declared resource limit stopped compilation, not a mathematical test."""


class Budget:
    def __init__(self, max_nodes=750000, max_atoms=100000, max_terms=100000,
                 max_seconds=300):
        self.max_nodes = max_nodes
        self.max_atoms = max_atoms
        self.max_terms = max_terms
        self.max_seconds = max_seconds
        self.start = time.monotonic()

    def time_check(self):
        if time.monotonic() - self.start > self.max_seconds:
            raise CompilationBudgetExceeded('declared compilation time budget')


class Coefficients:
    """Interned commutative expression DAG for genuine s coefficients."""
    def __init__(self, budget: Budget):
        self.budget = budget
        self.nodes: list[tuple] = []
        self.ids: dict[tuple, int] = {}
        self.derivatives: dict[int, int] = {}
        self.state_rhs: list[int] = []
        self.state_labels: list[tuple] = []
        self.zero = self.constant(0)
        self.one = self.constant(1)

    def intern(self, node: tuple) -> int:
        if node not in self.ids:
            if len(self.nodes) >= self.budget.max_nodes:
                raise CompilationBudgetExceeded('declared coefficient DAG node budget')
            if len(self.nodes) % 4096 == 0:
                self.budget.time_check()
            self.ids[node] = len(self.nodes)
            self.nodes.append(node)
        return self.ids[node]

    def constant(self, value) -> int:
        value = Fraction(value)
        return self.intern(('c', value.numerator, value.denominator))

    def geometry(self, name: str, order: int = 0) -> int:
        return self.intern(('g', name, order))

    def state(self, rhs: int, label: tuple) -> int:
        index = len(self.state_rhs)
        self.state_rhs.append(rhs)
        self.state_labels.append(label)
        return self.intern(('st', index))

    def power(self, node_id: int, exponent: int) -> int:
        return self.multiply_powers([(node_id, exponent)])

    def multiply(self, *node_ids: int) -> int:
        return self.multiply_powers((node, 1) for node in node_ids)

    def multiply_powers(self, items: Iterable[tuple[int, int]]) -> int:
        value = Fraction(1)
        factors: Counter[int] = Counter()
        for node_id, exponent in items:
            if not exponent:
                continue
            node = self.nodes[node_id]
            if node[0] == 'c':
                value *= Fraction(node[1], node[2]) ** exponent
            elif node[0] == 'mul':
                value *= Fraction(node[1], node[2]) ** exponent
                for factor, power in node[3]:
                    factors[factor] += power * exponent
            else:
                factors[node_id] += exponent
        if not value:
            return self.zero
        fs = tuple(sorted((factor, power) for factor, power in factors.items() if power))
        if not fs:
            return self.constant(value)
        if value == 1 and len(fs) == 1 and fs[0][1] == 1:
            return fs[0][0]
        return self.intern(('mul', value.numerator, value.denominator, fs))

    def linear(self, items: Iterable[tuple[Fraction, int]]) -> int:
        terms: dict[int, Fraction] = {}
        stack = list(items)
        while stack:
            weight, node_id = stack.pop()
            weight = Fraction(weight)
            if not weight:
                continue
            node = self.nodes[node_id]
            if node[0] == 'c':
                weight *= Fraction(node[1], node[2])
                node_id = self.one
            # Keep nested sums as DAG nodes: expanding every historical
            # coefficient would duplicate the actual Volterra history.
            elif node[0] == 'mul' and (node[1], node[2]) != (1, 1):
                weight *= Fraction(node[1], node[2])
                node_id = self.multiply_powers(node[3])
            terms[node_id] = terms.get(node_id, Fraction(0)) + weight
        normalized = tuple(sorted((node, value.numerator, value.denominator)
                                  for node, value in terms.items() if value))
        if not normalized:
            return self.zero
        if len(normalized) == 1:
            node, n, d = normalized[0]
            return self.multiply(self.constant(Fraction(n, d)), node)
        return self.intern(('add', normalized))

    def add(self, *nodes: int) -> int:
        return self.linear((Fraction(1), node) for node in nodes)

    def derivative(self, node_id: int) -> int:
        if node_id in self.derivatives:
            return self.derivatives[node_id]
        node = self.nodes[node_id]
        tag = node[0]
        if tag == 'c':
            result = self.zero
        elif tag == 'g':
            _, name, order = node
            if name == 'omega':
                if order != 0:
                    raise AssertionError('omega jets use the actual k_s/(2h) relation')
                result = self.multiply(self.constant(Fraction(1, 2)),
                                       self.geometry('k', 1), self.power(self.geometry('h'), -1))
            else:
                result = self.geometry(name, order + 1)
        elif tag == 'st':
            result = self.state_rhs[node[1]]
        elif tag == 'add':
            result = self.linear((Fraction(n, d), self.derivative(child)) for child, n, d in node[1])
        elif tag == 'mul':
            factors = node[3]
            terms = []
            for index, (factor, exponent) in enumerate(factors):
                df = self.derivative(factor)
                if df == self.zero:
                    continue
                remaining = list(factors)
                remaining[index] = (factor, exponent - 1)
                term = self.multiply(self.multiply_powers(remaining), df)
                terms.append((Fraction(node[1], node[2]) * exponent, term))
            result = self.linear(terms)
        else:
            raise AssertionError(tag)
        self.derivatives[node_id] = result
        return result


class Profiles:
    """Free differential/Volterra algebra; dependencies are not discarded."""
    def __init__(self, budget: Budget):
        self.budget = budget
        self.atoms: list[tuple] = []
        self.ids: dict[tuple, int] = {}
        self.weights: list[int] = []
        self.derivative_cache: dict[Monomial, dict[Monomial, int]] = {}
        self.conjugate_cache: dict[Monomial, Monomial] = {}

    def atom(self, key: tuple, weight: int) -> int:
        if key not in self.ids:
            if len(self.atoms) >= self.budget.max_atoms:
                raise CompilationBudgetExceeded('declared profile atom budget')
            self.ids[key] = len(self.atoms)
            self.atoms.append(key)
            self.weights.append(weight)
        return self.ids[key]

    def jet(self, kind: str, order: int) -> Monomial:
        return (0, (self.atom(('jet', kind, order), 1),))

    def weight(self, monomial: Monomial) -> int:
        return sum(self.weights[a] for a in monomial[1])

    @staticmethod
    def multiply(left: Monomial, right: Monomial) -> Monomial:
        return left[0] + right[0], tuple(sorted(left[1] + right[1]))

    def primitive(self, monomial: Monomial) -> Monomial:
        return (0, (self.atom(('int_right', monomial), self.weight(monomial)),))

    def conjugate(self, monomial: Monomial) -> Monomial:
        if monomial in self.conjugate_cache:
            return self.conjugate_cache[monomial]
        atoms = []
        for atom in monomial[1]:
            node = self.atoms[atom]
            if node[0] == 'jet':
                name = {'q': 'qbar', 'qbar': 'q'}.get(node[1], node[1])
                atoms.append(self.atom(('jet', name, node[2]), self.weights[atom]))
            else:
                integrand = self.conjugate(node[1])
                atoms.append(self.atom(('int_right', integrand), self.weights[atom]))
        result = (monomial[0], tuple(sorted(atoms)))
        self.conjugate_cache[monomial] = result
        return result

    def derivative(self, monomial: Monomial) -> dict[Monomial, int]:
        if monomial in self.derivative_cache:
            return self.derivative_cache[monomial]
        power, atoms = monomial
        out: Counter[Monomial] = Counter()
        if power:
            out[(power - 1, atoms)] += power
        for atom, count in Counter(atoms).items():
            rest = list(atoms)
            rest.remove(atom)
            base = (power, tuple(rest))
            kind = self.atoms[atom]
            if kind[0] == 'jet':
                derivative = self.jet(kind[1], kind[2] + 1)
            else:
                derivative = kind[1]
            out[self.multiply(base, derivative)] += count
        result = dict(out)
        self.derivative_cache[monomial] = result
        return result


class Algebra:
    def __init__(self, budget: Budget | None = None):
        self.budget = budget or Budget()
        self.c = Coefficients(self.budget)
        self.p = Profiles(self.budget)

    def scalar(self, coeff: int) -> 'Separated':
        return Separated(self, {} if coeff == self.c.zero else {ONE: coeff})

    def number(self, value) -> 'Separated':
        return self.scalar(self.c.constant(value))

    def profile(self, monomial: Monomial) -> 'Separated':
        return Separated(self, {monomial: self.c.one})


class Separated:
    def __init__(self, algebra: Algebra, terms: dict[Monomial, int]):
        self.algebra = algebra
        if len(terms) > algebra.budget.max_terms:
            raise CompilationBudgetExceeded('declared separated-expression term budget')
        self.terms = {m: v for m, v in terms.items() if v != algebra.c.zero}

    def add(self, *others: 'Separated') -> 'Separated':
        slots: dict[Monomial, list[int]] = {m: [v] for m, v in self.terms.items()}
        for other in others:
            for monomial, coeff in other.terms.items():
                slots.setdefault(monomial, []).append(coeff)
        return Separated(self.algebra, {m: self.algebra.c.add(*cs) for m, cs in slots.items()})

    def scale(self, value) -> 'Separated':
        return self.coefficient(self.algebra.c.constant(value))

    def coefficient(self, coeff: int) -> 'Separated':
        return Separated(self.algebra, {m: self.algebra.c.multiply(coeff, v) for m, v in self.terms.items()})

    def multiply(self, other: 'Separated') -> 'Separated':
        slots: dict[Monomial, list[int]] = {}
        for index, (left, lc) in enumerate(self.terms.items()):
            if index % 32 == 0:
                self.algebra.budget.time_check()
            for right, rc in other.terms.items():
                monomial = self.algebra.p.multiply(left, right)
                slots.setdefault(monomial, []).append(self.algebra.c.multiply(lc, rc))
            if len(slots) > self.algebra.budget.max_terms:
                raise CompilationBudgetExceeded('declared separated-product term budget')
        return Separated(self.algebra, {m: self.algebra.c.add(*cs) for m, cs in slots.items()})

    def conjugate(self) -> 'Separated':
        # All geometry/history coefficients in this canonical compiler are real.
        return Separated(self.algebra, {self.algebra.p.conjugate(m): c for m, c in self.terms.items()})

    def dx(self) -> 'Separated':
        slots: dict[Monomial, list[tuple[Fraction, int]]] = {}
        for monomial, coeff in self.terms.items():
            for derivative, multiplicity in self.algebra.p.derivative(monomial).items():
                slots.setdefault(derivative, []).append((Fraction(multiplicity), coeff))
        return Separated(self.algebra, {m: self.algebra.c.linear(cs) for m, cs in slots.items()})

    def ds(self) -> 'Separated':
        return Separated(self.algebra, {m: self.algebra.c.derivative(c) for m, c in self.terms.items()})

    def primitive(self) -> 'Separated':
        return Separated(self.algebra, {self.algebra.p.primitive(m): c for m, c in self.terms.items()})


class Field:
    def __init__(self, compiler: 'Compiler', components: tuple[Separated, Separated, Separated]):
        self.compiler = compiler
        self.components = components
        self._dx = None
        self._cov = None

    def dx(self):
        if self._dx is None:
            self._dx = tuple(v.dx() for v in self.components)
        return self._dx

    def cov(self):
        if self._cov is None:
            v0, v1, v2 = self.components
            self._cov = (v0.ds().add(v1.coefficient(self.compiler.k).scale(-1)),
                         v1.ds().add(v0.coefficient(self.compiler.k), v2),
                         v2.ds().add(v1.scale(-1)))
        return self._cov

    def conjugate(self):
        return Field(self.compiler, tuple(v.conjugate() for v in self.components))

    def scale(self, value):
        return Field(self.compiler, tuple(v.scale(value) for v in self.components))

    def add(self, other: 'Field'):
        return Field(self.compiler, tuple(a.add(b) for a, b in zip(self.components, other.components)))


class Compiler:
    def __init__(self, budget: Budget | None = None):
        self.a = Algebra(budget)
        c = self.a.c
        self.h = c.geometry('h')
        self.k = c.geometry('k')
        self.omega = c.geometry('omega')
        self.gamma = c.geometry('h', 1)
        self.nu = c.derivative(self.omega)
        self.ih = c.power(self.h, -1)
        self.ih2 = c.power(self.h, -2)
        self.zero = self.a.number(0)
        self.z = self.a.profile((1, ())).add(self.a.scalar(self.omega))
        self.e = self.z.coefficient(self.h).add(self.a.scalar(self.k).scale(-1))
        self.K0 = self.z.multiply(self.z).coefficient(self.k).add(
            self.z.coefficient(c.multiply(c.add(c.power(self.k, 2), c.one), self.ih)).scale(-1))
        self.lam = self.z.coefficient(self.gamma).add(
            self.a.scalar(c.multiply(self.h, self.nu)).scale(-1)).coefficient(self.ih2)
        self.records: list[dict] = []
        self.physical_fourth: dict[int, dict[str, Separated]] = {}

    def dot(self, left, right):
        return self.zero.add(*(a.multiply(b) for a, b in zip(left, right)))

    def initial(self, kind: str) -> Field:
        f = self.a.profile(self.a.p.jet(kind, 0))
        fp = self.a.profile(self.a.p.jet(kind, 1))
        return Field(self, (fp.scale(Fraction(-1, 2)), self.zero,
                            f.coefficient(self.h).add(self.e.multiply(fp).scale(Fraction(-1, 2)))))

    def forcing_range(self, pairs, order: int, mode: str, recover: bool):
        # A pair (w,U,V) denotes w times the symmetric bilinear tensor dU*dV.
        J, Tx, Ts, Tsx = self.zero, self.zero, self.zero, self.zero
        for weight, left, right in pairs:
            J = J.add(self.dot(left.components, right.components).scale(weight))
            Tx = Tx.add(self.dot(left.dx(), right.dx()).scale(weight))
            Ts = Ts.add(self.dot(left.cov(), right.cov()).scale(weight))
            mixed = self.dot(left.cov(), right.dx()).add(self.dot(right.cov(), left.dx()))
            Tsx = Tsx.add(mixed.scale(Fraction(weight, 2)))
        B = J.coefficient(self.ih).scale(Fraction(1, 2))
        P = Tx.primitive().coefficient(self.ih).scale(Fraction(-1, 2))
        Ps, Bs = P.ds(), B.ds()
        R = Ts.coefficient(self.ih2).scale(Fraction(1, 2)).add(
            self.K0.multiply(P), self.lam.multiply(Ps).scale(-1),
            self.z.coefficient(self.k).add(self.a.scalar(
                self.a.c.multiply(self.a.c.add(self.a.c.power(self.k, 2), self.a.c.one), self.ih)).scale(-1)).multiply(B),
            Bs.coefficient(self.a.c.multiply(self.gamma, self.ih2)).scale(-1))
        eta = Tsx.coefficient(self.ih).scale(Fraction(-1, 2)).add(
            self.z.coefficient(self.gamma).add(self.a.scalar(self.a.c.multiply(self.h, self.nu)).scale(-1))
                .multiply(P.dx()).coefficient(self.ih).scale(Fraction(1, 2)),
            B.dx().coefficient(self.a.c.multiply(self.gamma, self.ih)).scale(Fraction(1, 2)),
            Ps.scale(Fraction(-1, 2)))
        for expression in (J, Tx, Ts, Tsx, P, B, R, eta):
            if any(self.a.p.weight(m) != order for m in expression.terms):
                raise AssertionError(('homogeneous profile order', order, mode))
        record = {'order': order, 'mode': mode, 'J_terms': len(J.terms),
                  'ruling_integrand_terms': len(Tx.terms), 'R_terms': len(R.terms),
                  'eta0_terms': len(eta.terms), 'P_terms': len(P.terms), 'B_terms': len(B.terms),
                  'recovered': recover,
                  'ruling_integrand_sha256': expression_digest(Tx),
                  'period_rhs_sha256': expression_digest(R)}
        result = None
        if recover:
            state_terms = {m: self.a.c.state(R.terms[m], (order, mode, m)) for m in sorted(R.terms)}
            W = Separated(self.a, state_terms)
            A = W.dx().scale(Fraction(1, 2)).add(eta.coefficient(self.ih))
            result = Field(self, (A, self.z.multiply(P).add(B),
                                 self.e.multiply(A).add(W.coefficient(self.h).scale(-1))))
            record['state_count'] = len(state_terms)
            record['field_component_terms'] = [len(v.terms) for v in result.components]
        self.records.append(record)
        return result, {'ruling_integrand': Tx, 'period_rhs': R, 'P': P, 'B': B, 'eta0': eta}

    def compile(self, max_order: int = 4, progress: bool = False):
        # H(U,V) below is the symmetric bilinear tensor dU*dV, so S=2H.
        A = self.initial('q')
        Abar = A.conjugate()
        B, _ = self.forcing_range([(1, A, A)], 2, 'B=anchored_recovery(H(A,A))', recover=True)
        Bbar = B.conjugate()
        if progress:
            print(json.dumps({'compiled':'second complex square','nodes':len(self.a.c.nodes)}),flush=True)
        if max_order == 2:
            return
        U, _ = self.forcing_range([(1, A, B)], 3, 'U=anchored_recovery(H(A,B))', recover=True)
        V, _ = self.forcing_range([(1, A, Bbar)], 3, 'V=anchored_recovery(H(A,Bbar))', recover=True)
        Ubar, Vbar = U.conjugate(), V.conjugate()
        if progress:
            print(json.dumps({'compiled':'two third complex channels','nodes':len(self.a.c.nodes)}),flush=True)
        if max_order == 3:
            return
        # The six elementary tensors below and their conjugates give all five
        # actual fourth Fourier modes; keeping them separate avoids expanding
        # the same exact coefficient/history several times.
        channels = [('P=H(B,B)', B, B), ('Q=H(B,Bbar)', B, Bbar),
                    ('R=H(A,U)', A, U), ('S=H(A,V)', A, V),
                    ('T=H(A,Vbar)', A, Vbar), ('J=H(Abar,U)', Abar, U)]
        outputs = {}
        for name, left, right in channels:
            self.a.budget.time_check()
            _, outputs[name[0]] = self.forcing_range([(1, left, right)], 4, name, recover=False)
            if progress:
                print(json.dumps({'compiled':name,'nodes':len(self.a.c.nodes)}),flush=True)
        combinations = {
            -4: [('P', -1, 16), ('R', -1, 4)],
            -2: [('P', 1, 8), ('Q', 1, 8), ('R', 1, 4), ('S', 1, 4),
                 ('T', -1, 4), ('J', -1, 4)],
            0: [('P', -1, 16), ('Pbar', -1, 16), ('Q', -1, 4),
                ('J', 1, 4), ('Jbar', 1, 4), ('T', 1, 4), ('Tbar', 1, 4),
                ('S', -1, 4), ('Sbar', -1, 4)]}
        for mode, terms in combinations.items():
            physical = {}
            for key in ('ruling_integrand', 'period_rhs'):
                expression = self.zero
                for name, numerator, denominator in terms:
                    item = outputs[name[0]][key]
                    if name.endswith('bar'):
                        item = item.conjugate()
                    expression = expression.add(item.scale(Fraction(numerator, denominator)))
                physical[key] = expression
            self.physical_fourth[mode] = physical
        for mode in (2, 4):
            self.physical_fourth[mode] = {
                key: expression.conjugate()
                for key, expression in self.physical_fourth[-mode].items()}

    def inventory(self):
        c, p = self.a.c, self.a.p
        geometry_depth = {}
        for node in c.nodes:
            if node[0] == 'g':
                geometry_depth[node[1]] = max(geometry_depth.get(node[1], 0), node[2])
        return {'coefficient_DAG_nodes': len(c.nodes), 'ODE_state_coefficients': len(c.state_rhs),
                'profile_atoms': len(p.atoms),
                'right_anchored_Volterra_atoms': sum(a[0] == 'int_right' for a in p.atoms),
                'max_profile_jet': max((a[2] for a in p.atoms if a[0] == 'jet'), default=0),
                'geometry_derivative_depth': geometry_depth, 'range_channels': self.records,
                'physical_fourth_modes': {
                    str(mode): {key: {'terms': len(expression.terms),
                                      'sha256': expression_digest(expression)}
                                for key, expression in fields.items()}
                    for mode, fields in sorted(self.physical_fourth.items())},
                'coefficient_DAG_sha256': sequence_digest(c.nodes),
                'profile_atom_DAG_sha256': sequence_digest(p.atoms),
                'ordered_state_rhs_sha256': sequence_digest(c.state_rhs)}


def sequence_digest(sequence):
    digest = hashlib.sha256()
    for item in sequence:
        digest.update(json.dumps(item, separators=(',', ':')).encode('utf-8'))
        digest.update(b'\n')
    return digest.hexdigest()


def expression_digest(expression: Separated):
    # Coefficient/profile indices refer to the separately hashed ordered DAGs.
    return sequence_digest(sorted(expression.terms.items()))


def exact_phase_checks():
    """Small free-bilinear Fourier calculation, with no range compilation."""
    def linear(*items):
        out = {}
        for weight, vector in items:
            for symbol, value in vector.items():
                out[symbol] = out.get(symbol, Fraction(0)) + weight * value
        return {symbol: value for symbol, value in out.items() if value}

    def series_linear(*items):
        modes = sorted({mode for _, series in items for mode in series})
        out = {mode: linear(*[(weight, series.get(mode, {}))
                              for weight, series in items]) for mode in modes}
        return {mode: vector for mode, vector in out.items() if vector}

    def bilinear(left, right):
        out = {}
        for a, va in left.items():
            for b, vb in right.items():
                pair = tuple(sorted((a, b)))
                out[pair] = out.get(pair, Fraction(0)) + va * vb
        return {pair: value for pair, value in out.items() if value}

    def product(left, right):
        out = {}
        for lm, lv in left.items():
            for rm, rv in right.items():
                mode = lm + rm
                out[mode] = linear((1, out.get(mode, {})), (1, bilinear(lv, rv)))
        return {mode: vector for mode, vector in out.items() if vector}

    def recover(series, lookup):
        return {mode: {lookup[pair]: value for pair, value in vector.items()}
                for mode, vector in series.items()}

    Y = {-1: {'A': Fraction(1, 2)}, 1: {'Abar': Fraction(1, 2)}}
    Yf = {0: {'A': Fraction(1, 2), 'Abar': Fraction(1, 2)}}
    second_force = series_linear((1, product(Yf, Yf)), (-1, product(Y, Y)))
    Z = recover(second_force, {('A', 'A'): 'B', ('Abar', 'Abar'): 'Bbar'})
    expected_Z = {-2: {'B': Fraction(-1, 4)},
                  0: {'B': Fraction(1, 4), 'Bbar': Fraction(1, 4)},
                  2: {'Bbar': Fraction(-1, 4)}}
    if Z != expected_Z:
        raise AssertionError('exact second Fourier modes')
    third_force = series_linear((-2, product(Y, Z)))
    W = recover(third_force, {('A', 'B'): 'U', ('A', 'Bbar'): 'V',
                             ('Abar', 'B'): 'Vbar', ('Abar', 'Bbar'): 'Ubar'})
    expected_W = {-3: {'U': Fraction(1, 4)},
                  -1: {'U': Fraction(-1, 4), 'V': Fraction(-1, 4), 'Vbar': Fraction(1, 4)},
                  1: {'Ubar': Fraction(-1, 4), 'Vbar': Fraction(-1, 4), 'V': Fraction(1, 4)},
                  3: {'Ubar': Fraction(1, 4)}}
    if W != expected_W:
        raise AssertionError('exact third Fourier modes')
    fourth = series_linear((-1, product(Z, Z)), (-2, product(Y, W)))
    labels = {'P': ('B', 'B'), 'Pbar': ('Bbar', 'Bbar'), 'Q': ('B', 'Bbar'),
              'R': ('A', 'U'), 'Rbar': ('Abar', 'Ubar'),
              'S': ('A', 'V'), 'Sbar': ('Abar', 'Vbar'),
              'T': ('A', 'Vbar'), 'Tbar': ('Abar', 'V'),
              'J': ('Abar', 'U'), 'Jbar': ('A', 'Ubar')}
    expected_labels = {
        -4: {'P': Fraction(-1, 16), 'R': Fraction(-1, 4)},
        -2: {'P': Fraction(1, 8), 'Q': Fraction(1, 8), 'R': Fraction(1, 4),
             'S': Fraction(1, 4), 'T': Fraction(-1, 4), 'J': Fraction(-1, 4)},
        0: {'P': Fraction(-1, 16), 'Pbar': Fraction(-1, 16), 'Q': Fraction(-1, 4),
            'J': Fraction(1, 4), 'Jbar': Fraction(1, 4),
            'T': Fraction(1, 4), 'Tbar': Fraction(1, 4),
            'S': Fraction(-1, 4), 'Sbar': Fraction(-1, 4)}}
    conjugate = {'A': 'Abar', 'Abar': 'A', 'B': 'Bbar', 'Bbar': 'B',
                 'U': 'Ubar', 'Ubar': 'U', 'V': 'Vbar', 'Vbar': 'V'}
    expected = {mode: {tuple(sorted(labels[label])): value for label, value in terms.items()}
                for mode, terms in expected_labels.items()}
    for mode in (2, 4):
        expected[mode] = {tuple(sorted(conjugate[a] for a in pair)): value
                          for pair, value in expected[-mode].items()}
    if fourth != expected:
        raise AssertionError('exact fourth Fourier assembly')
    if linear(*[(1, vector) for vector in Z.values()]):
        raise AssertionError('second field vanishes at the exact seed')
    if linear(*[(1, vector) for vector in W.values()]):
        raise AssertionError('third field vanishes at the exact seed')
    if linear(*[(1, vector) for vector in fourth.values()]):
        raise AssertionError('fourth forcing vanishes at the exact seed')
    return {'second_modes_exact': True, 'third_modes_exact': True,
            'all_five_fourth_modes_exact': True, 'exact_seed_corrections_zero': True,
            'ordinary_bilinear_H_equals_S_over_2': True}


def exact_toy_checks():
    algebra = Algebra()
    q = algebra.profile(algebra.p.jet('toy_q', 0))
    qp = q.dx()
    x = algebra.profile((1, ()))
    sample = x.multiply(q).multiply(qp).add(qp.multiply(qp).scale(3))
    if sample.primitive().dx().terms != sample.terms:
        raise AssertionError('right primitive derivative')
    left = sample.multiply(q).dx()
    right = sample.dx().multiply(q).add(sample.multiply(q.dx()))
    if left.terms != right.terms:
        raise AssertionError('formal profile product rule')
    rhs = algebra.c.multiply(algebra.c.geometry('h'), algebra.c.geometry('k'))
    state = algebra.c.state(rhs, ('toy',))
    if algebra.c.derivative(state) != rhs:
        raise AssertionError('state derivative retains actual RHS')
    complex_q = algebra.profile(algebra.p.jet('q', 0))
    complex_sample = x.multiply(complex_q.dx()).multiply(complex_q)
    if complex_sample.conjugate().conjugate().terms != complex_sample.terms:
        raise AssertionError('profile conjugation involution')
    if complex_sample.primitive().conjugate().dx().terms != complex_sample.conjugate().terms:
        raise AssertionError('common-anchor Volterra conjugation')
    return {'primitive_derivative': True, 'profile_product_rule': True,
            'state_rhs_derivative': True, 'profile_conjugation_involution': True,
            'common_anchor_volterra_conjugation': True, 'phase_algebra': exact_phase_checks()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-order', type=int, choices=(2, 3, 4), default=4)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--progress', action='store_true')
    parser.add_argument('--toy-only', action='store_true',
                        help='only the small exact manual identities; no full range compilation')
    parser.add_argument('--max-coefficient-nodes', type=int, default=750000)
    parser.add_argument('--max-profile-atoms', type=int, default=100000)
    parser.add_argument('--max-separated-terms', type=int, default=100000)
    parser.add_argument('--max-seconds', type=int, default=300)
    args = parser.parse_args()
    if not args.toy_only and not (
            os.environ.get('GITHUB_ACTIONS') == 'true' and
            os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public'):
        parser.error('full target compilation runs only in this public repository GitHub Actions; use --toy-only locally')
    limits = {'max_nodes': args.max_coefficient_nodes, 'max_atoms': args.max_profile_atoms,
              'max_terms': args.max_separated_terms, 'max_seconds': args.max_seconds}
    if any(value <= 0 for value in limits.values()):
        parser.error('compilation budgets must be positive')
    checks = exact_toy_checks()
    payload = {'kind': 'small_exact_development_toy_only' if args.toy_only else 'exact_formal_profile_compilation_only',
               'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'fixed_target': 'g_X + epsilon^2 (dY_f)^2; f=(q+qbar)/2',
               'right_anchor': 'one common fixed xi endpoint r',
               's_anchor': 'one actual initial state; no segment or packet resets',
               'max_order': None if args.toy_only else args.max_order, 'toy_checks': checks,
               'resource_limits': limits, 'completion': 'toy_only' if args.toy_only else 'not_started',
               'github_actions_run': {key: os.environ.get(key) for key in
                                      ('GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_RUN_ATTEMPT', 'GITHUB_SHA')},
               'canonical_history_coefficients_real_and_shared_by_conjugation': True,
               'second_modes': {'-2':'-B/4','0':'(B+Bbar)/4','2':'-Bbar/4'},
               'third_modes': {'-3':'U/4','-1':'(-U-V+Vbar)/4','1':'(-Ubar-Vbar+V)/4','3':'Ubar/4'},
               'fourth_modes': {'-4':'-P/16-R/4','-2':'P/8+Q/8+R/4+S/4-T/4-J/4',
                                '0':'-(P+Pbar)/16-Q/4+(J+Jbar+T+Tbar-S-Sbar)/4',
                                '2':'conjugate of -2','4':'conjugate of -4'},
               'profile_basis_independence_assumed': False,
               'range_recovery_conditional_on_both_full_range_conditions': True,
               'canonical_initial_W': 'zero once at the global s origin; retained across every later segment',
               'third_gauge_reduction': 'if actual whole geometry has zero quadratic period operator, fourth periods are gauge invariant; fourth rulings must lie in the same global three-dimensional w-space',
               'geometry_identity_required_for_future_evaluation': 'R45 exact single P with frame endpoint D and M_P=0, then P,P,P_reverse,P_reverse; not the old Klein-eight-block experiment',
               'whole_range_conditions_satisfied': False, 'specific_P_geometry_supplied': False,
               'profile_integrals_evaluated': False, 'geometric_design_evaluated': False,
               'finite_family_certified': False}
    exit_code = 0
    if not args.toy_only:
        compiler = Compiler(Budget(**limits))
        try:
            compiler.compile(args.max_order, args.progress)
            payload['completion'] = 'complete'
        except CompilationBudgetExceeded as error:
            payload['completion'] = 'resource_budget_exceeded'
            payload['budget_failure'] = str(error)
            exit_code = 2
        payload.update(compiler.inventory())
        payload['elapsed_seconds'] = time.monotonic() - compiler.a.budget.start
    args.out.parent.mkdir(parents=True, exist_ok=True)
    output = json.dumps(payload, indent=2, sort_keys=True)+'\n'
    if len(output.encode('utf-8')) > 1000000:
        raise RuntimeError('summary output unexpectedly exceeds 1 MB; no oversized data written')
    args.out.write_text(output, encoding='utf-8')
    print(json.dumps({'output': str(args.out), 'bytes': args.out.stat().st_size,
                      'sha256': hashlib.sha256(args.out.read_bytes()).hexdigest(),
                      'completion': payload['completion'],
                      'coefficient_DAG_nodes': payload.get('coefficient_DAG_nodes'),
                      'profile_atoms': payload.get('profile_atoms')}))
    raise SystemExit(exit_code)


if __name__ == '__main__':
    main()
