#!/usr/bin/env python3
"""Direct N-polynomial history propagation for R67/R68.

The module has no actual-research CLI: only a small artificial ODE toy. Public
Actions callers must freeze their control word, profile, and shared anchors.
Every DAG node carries its N^0,N^1,N^2 coefficients; no subtraction of large-N
evaluations or separate per-bridge history anchoring is used.
"""
from __future__ import annotations

import argparse
import ctypes
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace

import numpy as np

import literature_endpoint_preserving_h_controls as controls
import literature_range_numeric_engine as engine

LD = engine.LD

POLYNOMIAL_C_SOURCE = r'''
#include <stdint.h>
#include <math.h>
static long double ipow(long double x, int64_t e) {
    int inverse = e < 0;
    uint64_t n = inverse ? (uint64_t)(-e) : (uint64_t)e;
    long double out = 1;
    while (n) { if (n & 1) out *= x; x *= x; n >>= 1; }
    return inverse ? 1/out : out;
}
static void multiply(long double *a, const long double *b) {
    long double c2=a[0]*b[2]+a[1]*b[1]+a[2]*b[0];
    long double c1=a[0]*b[1]+a[1]*b[0];
    a[0]*=b[0]; a[1]=c1; a[2]=c2;
}
static void power(long double *out, const long double *x, int64_t e) {
    out[0]=1; out[1]=0; out[2]=0;
    if (e < 0) { out[0]=ipow(x[0],e); return; }
    uint64_t n=(uint64_t)e;
    long double base[3]={x[0],x[1],x[2]};
    while (n) {
        if (n & 1) multiply(out,base);
        n >>= 1;
        if (n) multiply(base,base);
    }
}
void evaluate(int64_t ns, int64_t np, const int64_t* schedule,
              const int64_t* op, const int64_t* start, const int64_t* count,
              const int64_t* slot, const long double* constant,
              const int64_t* edge, const long double* weight, const int64_t* exponent,
              const long double* geometry, const long double* state, long double* value) {
    for (int64_t ii=0; ii<ns; ++ii) {
        int64_t i=schedule[ii];
        for (int64_t p=0; p<np; ++p) {
            long double v[3]={0,0,0};
            if (op[i]==0) v[0]=constant[i];
            else if (op[i]==1) v[0]=geometry[slot[i]*np+p];
            else if (op[i]==2) {
                for (int d=0; d<3; ++d) v[d]=state[(slot[i]*3+d)*np+p];
            } else if (op[i]==3) {
                for (int64_t j=start[i]; j<start[i]+count[i]; ++j)
                    for (int d=0; d<3; ++d)
                        v[d]+=weight[j]*value[(edge[j]*3+d)*np+p];
            } else {
                v[0]=constant[i];
                for (int64_t j=start[i]; j<start[i]+count[i]; ++j) {
                    long double x[3], powered[3];
                    for (int d=0; d<3; ++d) x[d]=value[(edge[j]*3+d)*np+p];
                    power(powered,x,exponent[j]);
                    multiply(v,powered);
                }
            }
            for (int d=0; d<3; ++d) value[(i*3+d)*np+p]=v[d];
        }
    }
}
'''


class PolynomialCoefficientEvaluator:
    """Evaluate truncated polynomial coefficients, with an explicit memory cap.

    Negative powers are legal only for state-independent geometry expressions.
    This is checked symbolically by engine.triangular_structure before any C
    evaluation. Floating outputs are approximations, not interval arithmetic.
    """
    def __init__(self, coefficients, buffer_mebibytes=128):
        if buffer_mebibytes <= 0:
            raise ValueError('positive DAG buffer budget required')
        self.coefficients = coefficients
        self.nodes = coefficients.nodes
        self.second, self.third, self.degrees = engine.triangular_structure(coefficients)
        self.buffer_limit = int(buffer_mebibytes * 1024 ** 2)
        self.bytes_per_point = max(1, len(self.nodes) * 3 * np.dtype(LD).itemsize)
        if self.bytes_per_point > self.buffer_limit:
            raise ValueError('DAG budget cannot hold even one three-coefficient point')
        self.chunk_points = max(1, self.buffer_limit // self.bytes_per_point)
        self.temporary = tempfile.TemporaryDirectory(prefix='visible-range-npoly-')
        source = Path(self.temporary.name) / 'polynomial_dag.c'
        library = Path(self.temporary.name) / 'polynomial_dag.so'
        source.write_text(POLYNOMIAL_C_SOURCE, encoding='utf-8')
        completed = subprocess.run(['cc', '-O3', '-std=c11', '-shared', '-fPIC',
            str(source), '-o', str(library), '-lm'], capture_output=True, text=True, timeout=60)
        if completed.returncode:
            self.temporary.cleanup()
            raise RuntimeError('small polynomial interpreter compilation failed: ' + completed.stderr[-2000:])
        self.library = ctypes.CDLL(str(library))
        ip = ctypes.POINTER(ctypes.c_int64)
        fp = ctypes.POINTER(ctypes.c_longdouble)
        self.library.evaluate.argtypes = [ctypes.c_int64, ctypes.c_int64,
            ip, ip, ip, ip, ip, fp, ip, fp, ip, fp, fp, fp]
        self.library.evaluate.restype = None
        ops, starts, counts, slots, constants, edges, weights, powers = [], [], [], [], [], [], [], []
        for node in self.nodes:
            tag = node[0]
            starts.append(len(edges))
            slots.append(0)
            constants.append(LD(0))
            if tag == 'c':
                ops.append(0)
                constants[-1] = engine.fraction_ld(node[1], node[2])
            elif tag == 'g':
                ops.append(1)
                name, order = node[1:]
                if name == 'omega':
                    if order:
                        raise ValueError('omega derivatives must use the true relation')
                    slots[-1] = 8
                elif name in ('h', 'k') and 0 <= order <= 3:
                    slots[-1] = order + (0 if name == 'h' else 4)
                else:
                    raise ValueError('unsupported geometry jet')
            elif tag == 'st':
                ops.append(2)
                slots[-1] = node[1]
            elif tag == 'add':
                ops.append(3)
                for child, numerator, denominator in node[1]:
                    edges.append(child)
                    weights.append(engine.fraction_ld(numerator, denominator))
                    powers.append(0)
            elif tag == 'mul':
                ops.append(4)
                constants[-1] = engine.fraction_ld(node[1], node[2])
                for child, exponent in node[3]:
                    if exponent < 0 and self.degrees[child]:
                        raise ValueError('state-dependent negative power is not polynomial')
                    edges.append(child)
                    weights.append(LD(0))
                    powers.append(exponent)
            else:
                raise ValueError('unknown coefficient operation: ' + str(tag))
            counts.append(len(edges) - starts[-1])
        self.integer_arrays = [np.ascontiguousarray(v, dtype=np.int64)
                               for v in (ops, starts, counts, slots, edges, powers)]
        self.float_arrays = [np.ascontiguousarray(v, dtype=LD) for v in (constants, weights)]
        self.buffer = None
        self.schedule_cache = {}

    def schedule(self, roots):
        key = tuple(map(int, roots))
        if key not in self.schedule_cache:
            active, pending = set(), list(key)
            while pending:
                index = pending.pop()
                if index in active:
                    continue
                active.add(index)
                pending.extend(engine.children(self.nodes[index]))
            self.schedule_cache[key] = np.array(sorted(active), dtype=np.int64)
        return self.schedule_cache[key]

    def evaluate(self, geometry, state, roots):
        geometry = np.asarray(geometry, dtype=LD)
        state = np.asarray(state, dtype=LD)
        roots = list(map(int, roots))
        if (geometry.ndim != 2 or geometry.shape[0] != 9 or state.ndim != 3 or
                state.shape != (len(self.coefficients.state_rhs), 3, geometry.shape[1])):
            raise ValueError('geometry and polynomial state batch shape')
        if roots and (min(roots) < 0 or max(roots) >= len(self.nodes)):
            raise ValueError('invalid coefficient root')
        if max((self.degrees[root] for root in roots), default=0) > 2:
            raise ValueError('requested polynomial root exceeds degree two; no truncation allowed')
        if np.any(state[self.second, 2] != 0):
            raise ValueError('second history input exceeds its symbolic degree one')
        result = np.empty((len(roots), 3, geometry.shape[1]), dtype=LD)
        if not roots:
            return result
        schedule = self.schedule(roots)
        ip = ctypes.POINTER(ctypes.c_int64)
        fp = ctypes.POINTER(ctypes.c_longdouble)
        ops, starts, counts, slots, edges, powers = self.integer_arrays
        constants, weights = self.float_arrays
        root_index = np.asarray(roots, dtype=int)
        for start in range(0, geometry.shape[1], self.chunk_points):
            stop = min(start + self.chunk_points, geometry.shape[1])
            count = stop - start
            geom = np.ascontiguousarray(geometry[:, start:stop])
            states = np.ascontiguousarray(state[:, :, start:stop])
            if self.buffer is None or self.buffer.shape != (len(self.nodes), 3, count):
                self.buffer = np.empty((len(self.nodes), 3, count), dtype=LD)
            self.library.evaluate(len(schedule), count, schedule.ctypes.data_as(ip),
                ops.ctypes.data_as(ip), starts.ctypes.data_as(ip), counts.ctypes.data_as(ip),
                slots.ctypes.data_as(ip), constants.ctypes.data_as(fp), edges.ctypes.data_as(ip),
                weights.ctypes.data_as(fp), powers.ctypes.data_as(ip), geom.ctypes.data_as(fp),
                states.ctypes.data_as(fp), self.buffer.ctypes.data_as(fp))
            result[:, :, start:stop] = self.buffer[root_index]
        if not np.all(np.isfinite(result)):
            raise FloatingPointError('nonfinite polynomial coefficient evaluation')
        return result

    def close(self):
        self.temporary.cleanup()


class NPolynomialIntegrator:
    """Carry all history coefficients across a fixed ordered control word.

    item.kind == 'bulk' means its stored turns give the *base* length ell;
    the research family has actual length N*ell. All other items have fixed
    true length. Altering this classification or the base controls is a new
    design, not a refinement of an existing finite-N candidate.
    """
    def __init__(self, compiler, final_roots, *, buffer_mebibytes=128,
                 geometry_provider=controls.geometry_jets, duration_provider=engine.item_duration):
        self.coefficients = compiler.a.c
        self.second, self.third, self.degrees = engine.triangular_structure(self.coefficients)
        self.second_roots = [self.coefficients.state_rhs[j] for j in self.second]
        self.third_roots = [self.coefficients.state_rhs[j] for j in self.third]
        self.final_roots = list(map(int, final_roots))
        if max((self.degrees[root] for root in self.final_roots), default=0) > 2:
            raise ValueError('fourth observable exceeds weighted history degree two')
        self.geometry_provider = geometry_provider
        self.duration_provider = duration_provider
        self.evaluator = PolynomialCoefficientEvaluator(self.coefficients, buffer_mebibytes)

    def zero_state(self):
        return np.zeros((len(self.coefficients.state_rhs), 3), dtype=LD)

    def step(self, item, state, n, omega_offset=0):
        if int(n) != n or n < 3:
            raise ValueError('at least three bridge quadrature nodes required')
        state = np.asarray(state, dtype=LD)
        if state.shape != (len(self.coefficients.state_rhs), 3):
            raise ValueError('history coefficients must have shape (number_of_states,3)')
        if not np.all(np.isfinite(state)) or np.any(state[self.second, 2] != 0):
            raise ValueError('second history must have degree at most one')
        bulk = item['kind'] == 'bulk'
        shift = int(bulk)
        count = 3 if item['kind'] in ('constant', 'bulk') else int(n)
        t, weights, primitive = engine.gauss_primitive(count)
        duration = LD(self.duration_provider(item))
        if not np.isfinite(duration) or duration <= 0:
            raise ValueError('positive finite fixed or base length required')
        geometry = self.geometry_provider(item, t, omega_offset)
        nodes = np.broadcast_to(state[:, :, None], (*state.shape, count)).copy()
        second_rhs = self.evaluator.evaluate(geometry, nodes, self.second_roots)
        if np.any(second_rhs[:, 1:] != 0):
            raise ValueError('second RHS contains history powers')
        second_integral = duration * (second_rhs @ primitive.T)
        nodes[self.second, shift:, :] += second_integral[:, :3-shift, :]
        third_rhs = self.evaluator.evaluate(geometry, nodes, self.third_roots)
        if np.any(third_rhs[:, 2] != 0):
            raise ValueError('third RHS exceeds degree one in N')
        third_integral = duration * (third_rhs @ primitive.T)
        nodes[self.third, shift:, :] += third_integral[:, :3-shift, :]
        values = self.evaluator.evaluate(geometry, nodes, self.final_roots)
        endpoint = state.copy()
        endpoint[self.second, shift:] += duration * (second_rhs[:, :3-shift, :] @ weights)
        endpoint[self.third, shift:] += duration * (third_rhs[:, :3-shift, :] @ weights)
        increment = np.zeros((len(self.final_roots), 4), dtype=LD)
        increment[:, shift:shift+3] = duration * (values @ weights)
        if not np.all(np.isfinite(endpoint)) or not np.all(np.isfinite(increment)):
            raise FloatingPointError('nonfinite polynomial history propagation')
        return dict(state=endpoint, period_increment=increment,
                    coefficient_values=values, geometry=geometry,
                    nodes=t, base_weights=duration*weights,
                    measure_degree=shift)

    def close(self):
        self.evaluator.close()


def evaluate_polynomial(coefficients, value):
    coefficients = np.asarray(coefficients, dtype=LD)
    result = np.zeros(coefficients.shape[:-1], dtype=LD)
    for coefficient in np.moveaxis(coefficients, -1, 0)[::-1]:
        result = result * LD(value) + coefficient
    return result


def toy_check():
    """Artificial rational ODE, with no actual geometry/profile/compiler run."""
    from literature_range_profile_algebra import Algebra
    algebra = Algebra()
    c = algebra.c
    b = c.state(c.constant(2), (2, 'toy_b'))
    z = c.state(c.add(c.constant(3), c.multiply(c.constant(5), b)), (3, 'toy_c'))
    observable = c.add(c.constant(7), c.power(b, 2), c.multiply(c.constant(11), z))
    forbidden_cubic = c.power(b, 3)
    h, k = c.geometry('h'), c.geometry('k')
    denominator_toy = c.add(c.multiply(c.power(h, -2), c.power(b, 2)),
        c.multiply(c.constant(2), z), c.constant(F(3, 7)), c.multiply(k, h))

    def artificial_geometry(item, t, omega_offset=0):
        result = np.zeros((9, len(t)), dtype=LD)
        result[0] = 2
        result[4] = 3
        return result

    integrator = NPolynomialIntegrator(SimpleNamespace(a=algebra), [observable, denominator_toy],
        buffer_mebibytes=1, geometry_provider=artificial_geometry,
        duration_provider=lambda item: engine.fraction_ld(*item['rational_duration']))

    def padd(*items):
        out = [F(0)] * max(map(len, items))
        for item in items:
            for j, value in enumerate(item):
                out[j] += value
        return out

    def pscale(item, scalar):
        return [scalar * value for value in item]

    def pmul(left, right):
        out = [F(0)] * (len(left) + len(right) - 1)
        for j, value in enumerate(left):
            for i, other in enumerate(right):
                out[j+i] += value * other
        return out

    def array(values, length):
        out = np.zeros(length, dtype=LD)
        for j, value in enumerate(values):
            out[j] = engine.fraction_ld(value.numerator, value.denominator)
        return out

    b_exact, c_exact, period_exact = [F(4), F(-2)], [F(6), F(3), F(1)], [F(0)]
    state = np.stack((array(b_exact, 3), array(c_exact, 3)))
    period = np.zeros((2, 4), dtype=LD)
    largest_state_error = LD(0)
    constant_denominator_error = LD(0)
    items = [('toy_bridge', 3, 7), ('bulk', 2, 5), ('toy_bridge', 5, 11),
             ('bulk', 7, 13), ('toy_bridge', 1, 17)]
    for kind, numerator, denominator in items:
        duration = [F(numerator, denominator)] if kind != 'bulk' else [F(0), F(numerator, denominator)]
        D2, D3 = pmul(duration, duration), pmul(pmul(duration, duration), duration)
        entry_rate = padd([F(7)], pmul(b_exact, b_exact), pscale(c_exact, F(11)))
        second_rate = padd(pscale(b_exact, F(4)), pscale(padd([F(3)], pscale(b_exact, F(5))), F(11)))
        period_exact = padd(period_exact, pmul(entry_rate, duration),
                            pscale(pmul(second_rate, D2), F(1, 2)), pscale(D3, F(59, 3)))
        c_exact = padd(c_exact, pmul(padd([F(3)], pscale(b_exact, F(5))), duration), pscale(D2, F(5)))
        b_exact = padd(b_exact, pscale(duration, F(2)))
        result = integrator.step(dict(kind=kind, rational_duration=(numerator, denominator)), state, 5)
        state, period = result['state'], period + result['period_increment']
        largest_state_error = max(largest_state_error,
            np.max(abs(state[0] - array(b_exact, 3))), np.max(abs(state[1] - array(c_exact, 3))))
        # On this artificial geometry, root2 = b^2/4 + 2c + 45/7.
        # Recover its nodes from the polynomial root1 and the separately
        # propagated state is not necessary: test the interpreter independently.
    period_error = np.max(abs(period[0] - array(period_exact, 4)))
    geometry = artificial_geometry({}, np.array([LD(0), LD(1)]))
    states = np.broadcast_to(state[:, :, None], (2, 3, 2)).copy()
    observed = integrator.evaluator.evaluate(geometry, states, [denominator_toy])[0]
    expected = padd(pscale(pmul(b_exact, b_exact), F(1, 4)), pscale(c_exact, F(2)), [F(45, 7)])
    constant_denominator_error = np.max(abs(observed - array(expected, 3)[:, None]))
    try:
        integrator.evaluator.evaluate(geometry, states, [forbidden_cubic])
    except ValueError:
        cubic_rejected = True
    else:
        raise AssertionError('a cubic observable was silently truncated')
    evaluation_errors = []
    for N in (0, 1, 2, 17):
        exact = sum((value * N ** j for j, value in enumerate(period_exact)), F(0))
        evaluation_errors.append(abs(evaluate_polynomial(period[0], N) -
                                    engine.fraction_ld(exact.numerator, exact.denominator)))
    integrator.close()
    if max(largest_state_error, period_error, constant_denominator_error) > LD('3e-12'):
        raise AssertionError('artificial polynomial propagation disagrees with exact Fraction recurrence')
    if max(evaluation_errors) > LD('3e-9'):
        raise AssertionError('artificial cubic evaluation disagrees with exact Fraction recurrence')

    # Reject a history denominator before a C evaluator or candidate is run.
    bad = Algebra()
    bad_b = bad.c.state(bad.c.constant(1), (2, 'bad_b'))
    bad.c.power(bad_b, -1)
    try:
        engine.triangular_structure(bad.c)
    except ValueError:
        denominator_rejected = True
    else:
        raise AssertionError('history denominator was not rejected')

    return dict(schema='N-polynomial-range-artificial-toy-v1',
        artificial_word=[dict(kind=k, rational_length=f'{n}/{d}') for k,n,d in items],
        exact_period_coefficients=[str(value) for value in period_exact],
        max_history_coefficient_error=float(largest_state_error),
        max_period_coefficient_error=float(period_error),
        geometry_only_denominator_polynomial_error=float(constant_denominator_error),
        max_artificial_polynomial_evaluation_error=float(max(evaluation_errors)),
        state_denominator_rejected=denominator_rejected,
        above_degree_two_observable_rejected=cubic_rejected,
        direct_coefficient_propagation_without_N_sampling=True,
        incoming_nonzero_N_and_N_squared_histories_retained=True,
        actual_geometry_profile_or_full_target_evaluated=False,
        full_fourth_range_paid=False, numerical_interval_certificate=False,
        source_hashes={Path(path).name: hashlib.sha256(Path(path).read_bytes()).hexdigest()
                       for path in (__file__, engine.__file__, controls.__file__)},
        polynomial_interpreter_sha256=hashlib.sha256(POLYNOMIAL_C_SOURCE.encode()).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--toy-only', action='store_true', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    report = toy_check()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
