#!/usr/bin/env python3
"""Exact right-tail adapter for the unchanged R56 forcing_range implementation.

Research mode is restricted to this public repository's GitHub Actions.
It compiles q=(c-xi)^m near its right endpoint, with every genuine s history
retained. It does not evaluate a geometric path, integrate the final period,
set histories to zero, or assert a sign for the remaining coefficients.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_range_profile_algebra as formal


MODEL = 'R56-exact-right-tail-polynomial-v1'
REPOSITORY = 'Rogerhu12/math-research-public'
SCRIPT = Path(__file__).resolve()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(',', ':'), allow_nan=False).encode('utf-8')


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = canonical(value) + b'\n'
    pending = path.with_name(path.name + '.tmp')
    pending.write_bytes(raw)
    pending.replace(path)
    return {'file': path.name, 'bytes': len(raw), 'sha256': sha256(raw)}


def source_hashes():
    return {p.name: sha256(p.read_bytes())
            for p in (SCRIPT, Path(formal.__file__).resolve())}


class TailCoefficients(formal.Coefficients):
    """The tail endpoint is an s-constant parameter, not a geometry jet."""
    def derivative(self, node_id):
        node = self.nodes[node_id]
        if node[0] == 'g' and node[1] == 'tail_end':
            return self.zero
        return super().derivative(node_id)


class TailProfiles:
    @staticmethod
    def weight(key):
        # A key is (t power, homogeneous profile order).
        return key[1]


class TailAlgebra:
    def __init__(self, budget):
        self.budget = budget
        self.c = TailCoefficients(budget)
        self.p = TailProfiles()

    def scalar(self, node):
        return TailPolynomial(self, {} if node == self.c.zero else {(0, 0): node})

    def number(self, value):
        return self.scalar(self.c.constant(value))

    def term(self, power, grade=0, coefficient=None):
        if power < 0:
            raise ValueError('negative t powers are outside this adapter')
        node = self.c.one if coefficient is None else coefficient
        return TailPolynomial(self, {(int(power), int(grade)): node})


class TailPolynomial:
    """Finite exact t polynomial, retaining profile grade for R56's guard.

    The coefficient DAG is the original genuine s/history algebra. No t
    truncation is performed, including before or after a xi derivative.
    """
    def __init__(self, algebra, terms):
        self.algebra = algebra
        if len(terms) > algebra.budget.max_terms:
            raise formal.CompilationBudgetExceeded('tail polynomial term budget')
        self.terms = {key: value for key, value in terms.items()
                      if value != algebra.c.zero}

    def add(self, *others):
        slots = {key: [value] for key, value in self.terms.items()}
        for other in others:
            if other.algebra is not self.algebra:
                raise ValueError('different coefficient/history algebras')
            for key, value in other.terms.items():
                slots.setdefault(key, []).append(value)
        return TailPolynomial(self.algebra,
                              {key: self.algebra.c.add(*values)
                               for key, values in slots.items()})

    def coefficient(self, node):
        return TailPolynomial(self.algebra,
                              {key: self.algebra.c.multiply(node, value)
                               for key, value in self.terms.items()})

    def scale(self, value):
        return self.coefficient(self.algebra.c.constant(value))

    def multiply(self, other):
        if other.algebra is not self.algebra:
            raise ValueError('different coefficient/history algebras')
        slots = {}
        for (lp, lg), lv in self.terms.items():
            self.algebra.budget.time_check()
            for (rp, rg), rv in other.terms.items():
                slots.setdefault((lp + rp, lg + rg), []).append(
                    self.algebra.c.multiply(lv, rv))
        return TailPolynomial(self.algebra,
                              {key: self.algebra.c.add(*values)
                               for key, values in slots.items()})

    def dx(self):
        # t=c-xi, so d/dxi=-d/dt.
        c = self.algebra.c
        return TailPolynomial(self.algebra,
                              {(power - 1, grade): c.multiply(c.constant(-power), node)
                               for (power, grade), node in self.terms.items() if power})

    def primitive(self):
        # Original R56 primitive is I=integral_r^xi. The profile is zero
        # from c to r; hence I(t^n)=-t^(n+1)/(n+1), with no free constant.
        c = self.algebra.c
        return TailPolynomial(self.algebra,
                              {(power + 1, grade): c.multiply(c.constant(Q(-1, power + 1)), node)
                               for (power, grade), node in self.terms.items()})

    def ds(self):
        return TailPolynomial(self.algebra,
                              {key: self.algebra.c.derivative(node)
                               for key, node in self.terms.items()})

    def node(self, power, grade):
        return self.terms.get((power, grade), self.algebra.c.zero)


class TailCompiler(formal.Compiler):
    """Reuse original dot, Field covariance and forcing_range, without editing it."""
    def __init__(self, budget, exponent):
        self.a = TailAlgebra(budget)
        c = self.a.c
        self.exponent = exponent
        self.h, self.k = c.geometry('h'), c.geometry('k')
        self.omega, self.tail_end = c.geometry('omega'), c.geometry('tail_end')
        self.gamma, self.nu = c.geometry('h', 1), c.derivative(self.omega)
        self.ih, self.ih2 = c.power(self.h, -1), c.power(self.h, -2)
        self.zero = self.a.number(0)
        self.xi = self.a.scalar(self.tail_end).add(self.a.term(1).scale(-1))
        self.z = self.xi.add(self.a.scalar(self.omega))
        self.e = self.z.coefficient(self.h).add(self.a.scalar(self.k).scale(-1))
        self.K0 = self.z.multiply(self.z).coefficient(self.k).add(
            self.z.coefficient(c.multiply(c.add(c.power(self.k, 2), c.one), self.ih)).scale(-1))
        self.lam = self.z.coefficient(self.gamma).add(
            self.a.scalar(c.multiply(self.h, self.nu)).scale(-1)).coefficient(self.ih2)
        self.records = []
        self.physical_fourth = {}

    def initial_tail(self):
        f = self.a.term(self.exponent, 1)
        fp = f.dx()
        return formal.Field(self, (fp.scale(Q(-1, 2)), self.zero,
                            f.coefficient(self.h).add(self.e.multiply(fp).scale(Q(-1, 2)))))

    def range_and_recover(self, pairs, order, label, recover):
        # Exact original method; recover=False avoids its profile-specific
        # Separated constructor. Its full range formulas and grade test run.
        _, data = formal.Compiler.forcing_range(self, pairs, order, label, False)
        field, W = None, None
        if recover:
            c = self.a.c
            W = TailPolynomial(self.a, {
                key: c.state(node, (order, label, key[0], key[1]))
                for key, node in sorted(data['period_rhs'].terms.items())})
            A = W.dx().scale(Q(1, 2)).add(data['eta0'].coefficient(self.ih))
            field = formal.Field(self, (A, self.z.multiply(data['P']).add(data['B']),
                                       self.e.multiply(A).add(W.coefficient(self.h).scale(-1))))
            self.records[-1]['recovered'] = True
            self.records[-1]['state_count'] = len(W.terms)
            self.records[-1]['state_definition'] = 'one genuine zero-anchored history per t coefficient'
        return field, W, data


class LaurentNormalizer:
    """Exact sparse Laurent expansion of selected genuine coefficient roots.

    State variables remain independent here. Ds has already used their real
    RHS. This normalizer never replaces any state by zero or by an end value.
    """
    def __init__(self, coefficients, max_terms=60000, max_cache_terms=1500000,
                 max_rss_mib=1800):
        self.c = coefficients
        self.max_terms = max_terms
        self.max_cache_terms = max_cache_terms
        self.max_rss_mib = max_rss_mib
        self.cache = {}
        self.cache_terms = 0
        self.calls = 0

    def guard(self, value=None):
        self.calls += 1
        if value is not None and len(value) > self.max_terms:
            raise formal.CompilationBudgetExceeded('Laurent polynomial term budget')
        if self.calls % 128 == 0:
            self.c.budget.time_check()
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 > self.max_rss_mib:
                raise formal.CompilationBudgetExceeded('declared soft RSS budget')

    @staticmethod
    def monomial_product(left, right):
        result = dict(left)
        for variable, exponent in right:
            result[variable] = result.get(variable, 0) + exponent
        return tuple(sorted((name, exponent) for name, exponent in result.items() if exponent))

    def add(self, *items):
        result = {}
        for weight, polynomial in items:
            for monomial, coefficient in polynomial.items():
                value = result.get(monomial, Q(0)) + Q(weight) * coefficient
                if value:
                    result[monomial] = value
                else:
                    result.pop(monomial, None)
            self.guard(result)
        return result

    def multiply(self, left, right):
        result = {}
        for lm, lc in left.items():
            self.guard()
            for rm, rc in right.items():
                monomial = self.monomial_product(lm, rm)
                value = result.get(monomial, Q(0)) + lc * rc
                if value:
                    result[monomial] = value
                else:
                    result.pop(monomial, None)
            self.guard(result)
        return result

    def power(self, value, exponent):
        if exponent < 0:
            if len(value) != 1:
                raise ValueError('nonmonomial inverse is not a Laurent polynomial')
            (monomial, coefficient), = value.items()
            if not coefficient:
                raise ZeroDivisionError()
            return {tuple((v, p * exponent) for v, p in monomial): coefficient ** exponent}
        result = {(): Q(1)}
        while exponent:
            if exponent & 1:
                result = self.multiply(result, value)
            exponent //= 2
            if exponent:
                value = self.multiply(value, value)
        return result

    def node(self, node_id):
        if node_id in self.cache:
            return self.cache[node_id]
        self.guard()
        node = self.c.nodes[node_id]
        tag = node[0]
        if tag == 'c':
            value = Q(node[1], node[2])
            result = {} if not value else {(): value}
        elif tag == 'g':
            result = {((f'{node[1]}_{node[2]}', 1),): Q(1)}
        elif tag == 'st':
            result = {((f'state_{node[1]}', 1),): Q(1)}
        elif tag == 'add':
            result = self.add(*[(Q(n, d), self.node(child)) for child, n, d in node[1]])
        elif tag == 'mul':
            result = {(): Q(node[1], node[2])}
            for child, exponent in node[3]:
                result = self.multiply(result, self.power(self.node(child), exponent))
        else:
            raise ValueError(f'unknown coefficient node {tag}')
        self.guard(result)
        self.cache_terms += len(result)
        if self.cache_terms > self.max_cache_terms:
            raise formal.CompilationBudgetExceeded('Laurent memoized-term budget')
        self.cache[node_id] = result
        return result


def poly_rows(polynomial):
    return [{'monomial': [[v, p] for v, p in monomial], 'coefficient': str(coefficient)}
            for monomial, coefficient in sorted(polynomial.items())]


def root_record(normalizer, node_id, max_rows=1800):
    value = normalizer.node(node_id)
    rows = poly_rows(value)
    raw = canonical(rows)
    return {'coefficient_DAG_root': node_id, 'terms': len(rows),
            'normalized_sha256': sha256(raw), 'exact_zero': not value,
            'readable_terms': rows[:max_rows], 'readable_terms_truncated': len(rows) > max_rows}


def array_roots(polynomial):
    return [{'t_power': p, 'profile_grade': grade, 'coefficient_root': node}
            for (p, grade), node in sorted(polynomial.terms.items())]


def aij(i, j):
    return Q(i * (i - 1) * j * (j - 1), i + j - 3)


def compile_tail(args, output, progress):
    budget = formal.Budget(max_nodes=args.max_nodes, max_atoms=1,
                           max_terms=args.max_tail_terms, max_seconds=args.max_seconds)
    compiler = TailCompiler(budget, args.exponent)
    c = compiler.a.c
    Y = compiler.initial_tail()
    Z2, W2, second = compiler.range_and_recover([(1, Y, Y)], 2, 'B-tail', True)
    U3, W3, third = compiler.range_and_recover([(1, Y, Z2)], 3, 'U-tail', True)
    _, _, fourth = compiler.range_and_recover(
        [(Q(-1, 16), Z2, Z2), (Q(-1, 4), Y, U3)], 4, 'pure-minus-four-tail', False)
    completed2 = W2.add(compiler.lam.multiply(second['P']))
    completed3 = W3.add(compiler.lam.multiply(third['P']))
    completed_rhs4 = fourth['period_rhs'].add(compiler.lam.multiply(fourth['P']).ds())
    m = args.exponent
    p, r, n = 2 * m - 3, 3 * m - 6, 4 * m - 9
    b, u = completed2.node(p, 2), completed3.node(r, 3)
    K = compiler.K0.add(compiler.lam.ds())
    e0 = compiler.e.node(0, 0)
    Ctilde = c.multiply(c.constant(Q(1, 8)), K.node(0, 0),
                       c.add(c.one, c.power(e0, 2)), compiler.ih)
    a, a1, a2, app = aij(m, m), aij(m, p), aij(m, r), aij(p, p)
    beta = a2 / (4 * a)
    alpha = -app / (48 * a) + a2 * a1 / (12 * a * a)
    expected4 = c.multiply(Ctilde, c.linear([
        (-app / 16, c.power(b, 2)), (a2 / 4, u)]))
    potential = c.linear([(alpha, c.power(b, 3)), (beta, c.multiply(b, u))])
    check_roots = {
        'second_completed_leading_ODE': c.linear([(1, c.derivative(b)), (-a, Ctilde)]),
        'third_completed_leading_ODE': c.linear([(1, c.derivative(u)),
                                                 (a1, c.multiply(Ctilde, b))]),
        'pure_completed_leading_density': c.linear([(1, completed_rhs4.node(n, 4)), (-1, expected4)]),
        'pure_leading_total_derivative': c.linear([(1, completed_rhs4.node(n, 4)),
                                                  (-1, c.derivative(potential))]),
    }
    # Preserve the complete genuinely compiled system before optional exact
    # Laurent expansion. A later resource stop must not discard these roots.
    structure = {
        'model': MODEL, 'tail_exponent': m, 'tail_end': 'symbolic real s-constant c',
        'profile': 'q=(c-xi)^m on its right tail; zero to the right',
        'xi_derivative': '-d/dt', 'right_primitive': 'I(t^p)=-t^(p+1)/(p+1)',
        'geometry_relation': 'omega_s=k_s/(2h); D_s c=0',
        'physical_scope': 'h>0 and c+omega uniformly positive; constant endpoint germs; no geometric path chosen',
        'coefficient_DAG': c.nodes, 'state_rhs': c.state_rhs, 'state_labels': c.state_labels,
        'state_initial_values': ['0'] * len(c.state_rhs),
        'second_scalar': array_roots(W2), 'third_scalar': array_roots(W3),
        'second_completed_scalar': array_roots(completed2),
        'third_completed_scalar': array_roots(completed3),
        'pure_original_period_density': array_roots(fourth['period_rhs']),
        'pure_completed_period_density': array_roots(completed_rhs4),
        'pure_P': array_roots(fourth['P']),
        'leading_check_roots': check_roots, 'records': compiler.records,
        'source_hashes': source_hashes(),
    }
    raw_structure = canonical(structure) + b'\n'
    compressed = gzip.compress(raw_structure, compresslevel=9, mtime=0)
    if len(compressed) >= 5_000_000:
        raise formal.CompilationBudgetExceeded('complete compressed structure exceeds 5 MB')
    structure_path = output.with_name(output.stem + '-structure.json.gz')
    structure_path.parent.mkdir(parents=True, exist_ok=True)
    structure_path.write_bytes(compressed)
    progress['compiled_structure'] = {'file': structure_path.name,
                                     'bytes': len(compressed), 'sha256': sha256(compressed)}
    write_json(output, {'completion': 'compiled-before-Laurent-analysis', 'model': MODEL,
                        'genuine_history_count': len(c.state_rhs),
                        'coefficient_DAG_nodes': len(c.nodes), 'source_hashes': source_hashes(),
                        'structure_file': structure_path.name,
                        'structure_compressed_sha256': sha256(compressed)})
    normalizer = LaurentNormalizer(c, args.max_laurent_terms, args.max_cache_terms, args.max_rss_mib)
    checks = {name: root_record(normalizer, node, 0) for name, node in check_roots.items()}
    lower = {}
    for label, polynomial, cutoff, grade in (
        ('second_completed', completed2, p, 2),
        ('third_completed', completed3, r, 3),
        ('fourth_completed_density', completed_rhs4, n, 4)):
        lower[label] = [root_record(normalizer, node, 0) | {'t_power': power}
                        for (power, degree), node in sorted(polynomial.terms.items())
                        if degree == grade and power < cutoff]
    leading_pass = all(v['exact_zero'] for v in checks.values()) and all(
        v['exact_zero'] for values in lower.values() for v in values)
    readable = {
        'model': MODEL, 'tail_exponent': m,
        'meaning': 'Exact coefficient ODEs; each state is a genuine history. Density nonzero is not period nonzero.',
        'second_completed_leading_b': root_record(normalizer, b),
        'third_completed_leading_u': root_record(normalizer, u),
        'Ctilde': root_record(normalizer, Ctilde),
        'leading_total_derivative_potential': root_record(normalizer, potential),
        'fourth_completed_density_coefficients': [],
    }
    # Include later coefficients only while the entire readable artifact fits
    # its declared budget. The full DAG contains every root, without truncation.
    omitted = []
    for power in range(n, min(max(k[0] for k in completed_rhs4.terms), n + args.next_orders) + 1):
        record = root_record(normalizer, completed_rhs4.node(power, 4), args.readable_terms)
        item = {'t_power': power, **record}
        readable['fourth_completed_density_coefficients'].append(item)
        if len(canonical(readable)) > 94000:
            readable['fourth_completed_density_coefficients'].pop()
            omitted.append({'t_power': power, 'coefficient_DAG_root': record['coefficient_DAG_root'],
                            'terms': record['terms'], 'normalized_sha256': record['normalized_sha256']})
    readable['omitted_from_readable_due_to_size'] = omitted
    while len(canonical(readable)) > 94000:
        records = [value for value in readable.values()
                   if isinstance(value, dict) and value.get('readable_terms')]
        records += [value for value in readable['fourth_completed_density_coefficients']
                    if value.get('readable_terms')]
        if not records:
            raise formal.CompilationBudgetExceeded('readable metadata exceeds declared 95 KB budget')
        largest = max(records, key=lambda value: len(canonical(value['readable_terms'])))
        largest['readable_terms'] = largest['readable_terms'][:len(largest['readable_terms']) // 2]
        largest['readable_terms_truncated'] = True
    readable_receipt = write_json(output.with_name(output.stem + '-expressions.json'), readable)
    return {
        'completion': 'complete' if leading_pass else 'exact-leading-check-failed',
        'model': MODEL, 'tail_exponent': m,
        'coefficient_DAG_nodes': len(c.nodes), 'genuine_history_count': len(c.state_rhs),
        'history_counts_by_stage': {str(order): sum(label[0] == order for label in c.state_labels)
                                    for order in (2, 3)},
        'original_R56_forcing_range_reused': True,
        'histories_set_to_zero': False, 'geometric_path_evaluated': False,
        'truncation_of_t_polynomials': False,
        'leading_tail_order': n, 'R85_leading_identities_verified': leading_pass,
        'leading_checks': checks, 'coefficients_below_predicted_order': lower,
        'later_orders_are_density_ODEs_not_closed_period_or_sign_certificates': True,
        'zero_M_endpoint_conditions': 'all second scalar coefficients vanish at s=L; constant endpoint germs give lambda=0',
        'zero_T_endpoint_conditions_if_assumed': 'all third scalar coefficients vanish at s=L; never imposed internally',
        'new_zero_cost_loop_proved': False, 'universal_fourth_sign_proved': False,
        'full_physical_completion': False,
        'artifacts': [readable_receipt, {'file': structure_path.name,
            'compressed_bytes': len(compressed), 'compressed_sha256': sha256(compressed),
            'raw_bytes': len(raw_structure), 'raw_sha256': sha256(raw_structure)}],
        'normalizer_cache_terms': normalizer.cache_terms,
        'elapsed_seconds': time.monotonic() - budget.start,
        'peak_rss_mib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024,
        'source_hashes': source_hashes(),
    }


def developer_check():
    """Artificial polynomial/ODE identities only; no R56 research forcing."""
    budget = formal.Budget(max_nodes=3000, max_atoms=1, max_terms=200, max_seconds=20)
    algebra = TailAlgebra(budget)
    c = algebra.c
    norm = LaurentNormalizer(c, max_terms=1000, max_cache_terms=10000)
    t5 = algebra.term(5, 1)
    zero = t5.primitive().dx().add(t5.scale(-1))
    cparam = c.geometry('tail_end')
    xi = algebra.scalar(cparam).add(algebra.term(1).scale(-1))
    xi_check = xi.dx().add(algebra.number(-1))
    C = c.geometry('artificial_C')
    m = 8
    p, r = 2 * m - 3, 3 * m - 6
    a, a1, a2, app = aij(m, m), aij(m, p), aij(m, r), aij(p, p)
    b = c.state(c.multiply(c.constant(a), C), ('artificial', 'b'))
    u = c.state(c.multiply(c.constant(-a1), C, b), ('artificial', 'u'))
    potential = c.linear([(-app / (48 * a) + a2 * a1 / (12 * a * a), c.power(b, 3)),
                          (a2 / (4 * a), c.multiply(b, u))])
    rhs = c.multiply(C, c.linear([(-app / 16, c.power(b, 2)), (a2 / 4, u)]))
    residual = c.linear([(1, c.derivative(potential)), (-1, rhs)])
    checks = {
        'right_primitive_derivative_exact': all(not norm.node(v) for v in zero.terms.values()),
        'xi_equals_c_minus_t_derivative_exact': all(not norm.node(v) for v in xi_check.terms.values()),
        'tail_endpoint_s_constant': c.derivative(cparam) == c.zero,
        'profile_grade_preserved': all(key[1] == 2 for key in t5.multiply(t5).terms),
        'artificial_triangular_ODE_total_derivative': not norm.node(residual),
        'actual_omega_derivative': not norm.node(c.linear([
            (1, c.derivative(c.geometry('omega'))),
            (Q(-1, 2), c.multiply(c.geometry('k', 1), c.power(c.geometry('h'), -1)))])),
    }
    report = {'mode': 'artificial-development-only', 'checks': checks,
              'passed': all(checks.values()), 'research_forcing_compiled': False,
              'source_hashes': source_hashes()}
    json.loads(canonical(report))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--exponent', type=int, default=8)
    parser.add_argument('--next-orders', type=int, default=4)
    parser.add_argument('--max-seconds', type=float, default=240)
    parser.add_argument('--max-nodes', type=int, default=600000)
    parser.add_argument('--max-tail-terms', type=int, default=1000)
    parser.add_argument('--max-laurent-terms', type=int, default=60000)
    parser.add_argument('--max-cache-terms', type=int, default=1500000)
    parser.add_argument('--max-rss-mib', type=float, default=1800)
    parser.add_argument('--readable-terms', type=int, default=1000)
    args = parser.parse_args()
    if args.check_only:
        report = developer_check()
        write_json(args.out, report)
        print(json.dumps({'passed': report['passed'], 'mode': report['mode']}), flush=True)
        return 0 if report['passed'] else 2
    if os.environ.get('GITHUB_ACTIONS', '').lower() != 'true' or os.environ.get('GITHUB_REPOSITORY') != REPOSITORY:
        raise SystemExit('Research compilation is allowed only in the public repository GitHub Actions.')
    if args.exponent < 8 or args.next_orders < 0:
        raise SystemExit('exponent must be >=8 and next-orders nonnegative')
    started = time.monotonic()
    progress = {}
    try:
        report = compile_tail(args, args.out, progress)
        code = 0 if report['completion'] == 'complete' else 2
    except Exception as exc:
        report = {'completion': 'budget-exhausted' if isinstance(exc, formal.CompilationBudgetExceeded) else 'error',
                  'exception_type': type(exc).__name__, 'error': str(exc), 'model': MODEL,
                  'tail_exponent': args.exponent, 'elapsed_seconds': time.monotonic() - started,
                  'source_hashes': source_hashes(),
                  'universal_fourth_sign_proved': False, 'new_zero_cost_loop_proved': False,
                  'no_missing_tail_coefficient_is_interpreted_as_zero': True}
        if 'compiled_structure' in progress:
            report['preserved_compiled_structure'] = progress['compiled_structure']
        code = 2
    write_json(args.out, report)
    print(json.dumps({'completion': report['completion'],
                      'elapsed_seconds': report['elapsed_seconds'],
                      'output': args.out.name}), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
