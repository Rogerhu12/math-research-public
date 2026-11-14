#!/usr/bin/env python3
"""Triangular coefficient integration for the frozen full-range compiler.

This module evaluates only when explicitly called. Full research callers must
enforce the public Actions gate. The toy is a small artificial polynomial ODE.
"""
from __future__ import annotations

import ctypes
import argparse
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander

LD = np.longdouble
CD = np.clongdouble

C_SOURCE = r'''
#include <stdint.h>
#include <math.h>
static long double ipow(long double x, int64_t e) {
    int inverse = e < 0;
    uint64_t n = inverse ? (uint64_t)(-e) : (uint64_t)e;
    long double out = 1;
    while (n) { if (n & 1) out *= x; x *= x; n >>= 1; }
    return inverse ? 1/out : out;
}
void evaluate(int64_t ns, int64_t np, const int64_t* schedule,
              const int64_t* op, const int64_t* start, const int64_t* count,
              const int64_t* slot, const long double* constant,
              const int64_t* edge, const long double* weight, const int64_t* power,
              const long double* geometry, const long double* state, long double* value) {
    for (int64_t ii=0; ii<ns; ++ii) {
        int64_t i=schedule[ii];
        for (int64_t p=0; p<np; ++p) {
            long double v=0;
            if (op[i]==0) v=constant[i];
            else if (op[i]==1) v=geometry[slot[i]*np+p];
            else if (op[i]==2) v=state[slot[i]*np+p];
            else if (op[i]==3) {
                for (int64_t j=start[i]; j<start[i]+count[i]; ++j)
                    v += weight[j]*value[edge[j]*np+p];
            } else {
                v=constant[i];
                for (int64_t j=start[i]; j<start[i]+count[i]; ++j)
                    v *= ipow(value[edge[j]*np+p], power[j]);
            }
            value[i*np+p]=v;
        }
    }
}
'''


def fraction_ld(numerator, denominator):
    return LD(str(numerator))/LD(str(denominator))


def children(node):
    if node[0] == 'add':
        return [item[0] for item in node[1]]
    if node[0] == 'mul':
        return [item[0] for item in node[3]]
    return []


class CoefficientEvaluator:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.nodes = coefficients.nodes
        self.temporary = tempfile.TemporaryDirectory(prefix='visible-range-coeff-')
        cfile = Path(self.temporary.name)/'coefficient_dag.c'
        library = Path(self.temporary.name)/'coefficient_dag.so'
        cfile.write_text(C_SOURCE, encoding='utf-8')
        completed = subprocess.run(['cc', '-O3', '-std=c11', '-shared', '-fPIC',
                                    str(cfile), '-o', str(library), '-lm'],
                                   text=True, capture_output=True, timeout=60)
        if completed.returncode:
            raise RuntimeError('small DAG interpreter compilation failed: '+completed.stderr[-2000:])
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
                constants[-1] = fraction_ld(node[1], node[2])
            elif tag == 'g':
                ops.append(1)
                name, order = node[1:]
                if name == 'omega':
                    if order:
                        raise ValueError('omega higher jets must use the true relation')
                    slots[-1] = 8
                else:
                    if name not in ('h', 'k') or order > 3:
                        raise ValueError('unsupported actual geometry jet')
                    slots[-1] = order+(0 if name == 'h' else 4)
            elif tag == 'st':
                ops.append(2)
                slots[-1] = node[1]
            elif tag == 'add':
                ops.append(3)
                for child, n, d in node[1]:
                    edges.append(child)
                    weights.append(fraction_ld(n, d))
                    powers.append(0)
            elif tag == 'mul':
                ops.append(4)
                constants[-1] = fraction_ld(node[1], node[2])
                for child, exponent in node[3]:
                    edges.append(child)
                    weights.append(LD(0))
                    powers.append(exponent)
            else:
                raise ValueError(tag)
            counts.append(len(edges)-starts[-1])
        self.integer_arrays = [np.ascontiguousarray(a, dtype=np.int64)
                               for a in (ops, starts, counts, slots, edges, powers)]
        self.float_arrays = [np.ascontiguousarray(a, dtype=LD) for a in (constants, weights)]
        self.buffer = None
        self.schedule_cache = {}

    def schedule(self, roots):
        key = tuple(map(int, roots))
        if key not in self.schedule_cache:
            active, todo = set(), list(key)
            while todo:
                node = todo.pop()
                if node in active:
                    continue
                active.add(node)
                todo.extend(children(self.nodes[node]))
            self.schedule_cache[key] = np.array(sorted(active), dtype=np.int64)
        return self.schedule_cache[key]

    def evaluate(self, geometry, state, roots):
        geometry = np.ascontiguousarray(geometry, dtype=LD)
        state = np.ascontiguousarray(state, dtype=LD)
        if geometry.ndim != 2 or geometry.shape[0] != 9 or state.shape[1] != geometry.shape[1]:
            raise ValueError('geometry/state batch shape')
        npoints = geometry.shape[1]
        if self.buffer is None or self.buffer.shape != (len(self.nodes), npoints):
            self.buffer = np.empty((len(self.nodes), npoints), dtype=LD)
        schedule = self.schedule(roots)
        ip = ctypes.POINTER(ctypes.c_int64)
        fp = ctypes.POINTER(ctypes.c_longdouble)
        ops, starts, counts, slots, edges, powers = self.integer_arrays
        constants, weights = self.float_arrays
        self.library.evaluate(len(schedule), npoints, schedule.ctypes.data_as(ip),
            ops.ctypes.data_as(ip), starts.ctypes.data_as(ip), counts.ctypes.data_as(ip),
            slots.ctypes.data_as(ip), constants.ctypes.data_as(fp), edges.ctypes.data_as(ip),
            weights.ctypes.data_as(fp), powers.ctypes.data_as(ip), geometry.ctypes.data_as(fp),
            state.ctypes.data_as(fp), self.buffer.ctypes.data_as(fp))
        return self.buffer[np.asarray(roots, dtype=int)].copy()

    def close(self):
        self.temporary.cleanup()


@lru_cache(maxsize=16)
def gauss_primitive(n):
    """Q_ij = integral_0^t_i of the j-th cardinal polynomial."""
    x, weights = leggauss(n)
    x, weights = x.astype(LD), weights.astype(LD)/2
    t = (x+1)/2
    polynomials = legvander(x, n)
    integrated = np.empty((n, n), dtype=LD)
    integrated[:, 0] = t
    for degree in range(1, n):
        integrated[:, degree] = (polynomials[:, degree+1]-polynomials[:, degree-1])/(2*(2*degree+1))
    Q = (integrated*np.arange(1, 2*n, 2, dtype=LD))@(polynomials[:, :n].T*weights)
    return t, weights, Q


def geometry_jets(item, t, omega_offset=0):
    t = np.asarray(t, dtype=LD)
    result = np.zeros((9, len(t)), dtype=LD)
    if item['kind'] in ('constant', 'bulk'):
        result[0] = LD(item['h'])
        result[4] = LD(item['k'])
        result[8] = LD(item['omega'])+LD(omega_offset)
        return result
    duration = LD(item['duration'])
    b0, b1, eta = (LD(item[key]) for key in ('b0', 'b_end', 'eta'))
    k0, k1 = LD(item['k0']), LD(item['k1'])
    r = 1/(1-t)-1/t
    S = np.empty_like(t)
    positive = r >= 0
    with np.errstate(under='ignore'):
        S[positive] = 1/(1+np.exp(-r[positive]))
        er = np.exp(r[~positive])
        S[~positive] = er/(1+er)
    r1 = (1/(1-t)**2+1/t**2)/duration
    r2 = (2/(1-t)**3-2/t**3)/duration**2
    r3 = (6/(1-t)**4+6/t**4)/duration**3
    S1 = S*(1-S)*r1
    S2 = S*(1-S)*(r2+(1-2*S)*r1*r1)
    S3 = S*(1-S)*(r3+3*(1-2*S)*r1*r2+(1-6*S+6*S*S)*r1**3)
    beta = b1-b0+eta
    b = b0+beta*S-eta*S*S
    bprime = (beta-2*eta*S)*S1
    bsecond = (beta-2*eta*S)*S2-2*eta*S1*S1
    bthird = (beta-2*eta*S)*S3-6*eta*S1*S2
    if np.min(b) <= 0:
        raise ValueError('nonpositive frozen reciprocal h')
    result[0] = 1/(2*b)
    result[1] = -bprime/(2*b*b)
    result[2] = bprime*bprime/b**3-bsecond/(2*b*b)
    result[3] = -3*bprime**3/b**4+3*bprime*bsecond/b**3-bthird/(2*b*b)
    result[4] = k0+(k1-k0)*S
    result[5] = (k1-k0)*S1
    result[6] = (k1-k0)*S2
    result[7] = (k1-k0)*S3
    result[8] = LD(item['omega0'])+LD(omega_offset)+(k1-k0)*(
        b0*S+(b1-b0)*S*S/2+eta*(S*S/2-S*S*S/3))
    return result


def item_duration(item):
    if item['kind'] == 'bulk':
        return LD(item['turns'])*2*np.arccos(LD(-1))/np.sqrt(1+LD(item['k'])**2)
    return LD(item['duration'])


def triangular_structure(coefficients):
    second = [j for j, label in enumerate(coefficients.state_labels) if label[0] == 2]
    third = [j for j, label in enumerate(coefficients.state_labels) if label[0] == 3]
    if len(second)+len(third) != len(coefficients.state_rhs):
        raise ValueError('only second/third primitive states are expected')
    second_set = set(second)
    last_rhs = max(coefficients.state_rhs, default=-1)
    dependencies, degrees = [], []
    for index, node in enumerate(coefficients.nodes):
        tag = node[0]
        if tag in ('c', 'g'):
            dependencies.append(frozenset())
            degrees.append(0)
        elif tag == 'st':
            dependencies.append(frozenset((node[1],)))
            degrees.append(1 if node[1] in second_set else 2)
        else:
            child_nodes = children(node)
            dependencies.append(frozenset().union(*(dependencies[j] for j in child_nodes))
                                if index <= last_rhs else frozenset())
            if tag == 'add':
                degrees.append(max((degrees[j] for j in child_nodes), default=0))
            else:
                if any(exponent < 0 and degrees[j] for j, exponent in node[3]):
                    raise ValueError('unexpected state-dependent denominator')
                degrees.append(sum(exponent*degrees[j] for j, exponent in node[3]))
    if any(dependencies[coefficients.state_rhs[j]] for j in second):
        raise ValueError('second histories must have geometry-only RHS')
    if any(not dependencies[coefficients.state_rhs[j]].issubset(second_set) or
           degrees[coefficients.state_rhs[j]] > 1 for j in third):
        raise ValueError('third histories must be affine in second histories')
    return np.array(second, dtype=int), np.array(third, dtype=int), degrees


class TriangularIntegrator:
    def __init__(self, compiler, final_roots):
        self.compiler = compiler
        self.coefficients = compiler.a.c
        self.second, self.third, self.degrees = triangular_structure(self.coefficients)
        self.second_roots = [self.coefficients.state_rhs[j] for j in self.second]
        self.third_roots = [self.coefficients.state_rhs[j] for j in self.third]
        self.final_roots = list(map(int, final_roots))
        if max((self.degrees[j] for j in self.final_roots), default=0) > 2:
            raise ValueError('fourth observables exceed their expected weighted state degree')
        self.evaluator = CoefficientEvaluator(self.coefficients)

    def step(self, item, state, n, omega_offset=0):
        # Three constant nodes also integrate the squared quadratic ruling norm.
        count = 3 if item['kind'] in ('constant', 'bulk') else n
        t, weights, Q = gauss_primitive(count)
        duration = item_duration(item)
        geometry = geometry_jets(item, t, omega_offset)
        nodes = np.broadcast_to(np.asarray(state, dtype=LD)[:, None], (len(state), count)).copy()
        second_rhs = self.evaluator.evaluate(geometry, nodes, self.second_roots)
        nodes[self.second] = np.asarray(state)[self.second, None]+duration*(second_rhs@Q.T)
        third_rhs = self.evaluator.evaluate(geometry, nodes, self.third_roots)
        nodes[self.third] = np.asarray(state)[self.third, None]+duration*(third_rhs@Q.T)
        values = self.evaluator.evaluate(geometry, nodes, self.final_roots)
        endpoint = np.asarray(state, dtype=LD).copy()
        endpoint[self.second] += duration*(second_rhs@weights)
        endpoint[self.third] += duration*(third_rhs@weights)
        if not np.all(np.isfinite(values)) or not np.all(np.isfinite(endpoint)):
            raise FloatingPointError('nonfinite coefficient integration; no residual projection')
        return endpoint, duration*weights, geometry, values

    def close(self):
        self.evaluator.close()


def toy_check():
    # Artificial c2'=2, c3'=3+5*c2, observable=7+c2^2+11*c3.
    t, weights, Q = gauss_primitive(3)
    duration = LD(3)/7
    c2_start, c3_start = LD(4), LD(6)
    c2 = c2_start+duration*(Q@np.full(3, LD(2)))
    c3 = c3_start+duration*(Q@(3+5*c2))
    exact_c2 = c2_start+2*duration*t
    exact_c3 = c3_start+(3+5*c2_start)*duration*t+5*(duration*t)**2
    observed = duration*np.dot(weights, 7+c2*c2+11*c3)
    exact = (7+c2_start*c2_start+11*c3_start)*duration
    exact += (4*c2_start+11*(3+5*c2_start))*duration**2/2
    exact += (4+55)*duration**3/3
    errors = [np.max(abs(c2-exact_c2)), np.max(abs(c3-exact_c3)), abs(observed-exact)]
    if max(errors) > LD('2e-12'):
        raise AssertionError('small triangular polynomial integration toy')
    # Test the generic C interpreter on three artificial states, no geometry.
    from literature_range_profile_algebra import Algebra
    algebra = Algebra()
    coefficients = algebra.c
    h, k = coefficients.geometry('h'), coefficients.geometry('k')
    state_node = coefficients.state(coefficients.one, ('toy',))
    root = coefficients.add(coefficients.multiply(coefficients.power(h, -2), state_node),
                            coefficients.constant(Fraction(3, 7)), coefficients.multiply(k, h))
    evaluator = CoefficientEvaluator(coefficients)
    geometry = np.zeros((9, 3), dtype=LD)
    geometry[0] = [1, 2, 3]
    geometry[4] = [5, 7, 11]
    states = np.array([[LD(1)/3, LD(2)/5, LD(7)/11]], dtype=LD)
    evaluated = evaluator.evaluate(geometry, states, [root])[0]
    expected = states[0]/geometry[0]**2+LD(3)/7+geometry[4]*geometry[0]
    interpreter_error = float(np.max(abs(evaluated-expected)))
    evaluator.close()
    if interpreter_error > 1e-15:
        raise AssertionError('small synthetic coefficient interpreter toy')
    return dict(kind='small_artificial_triangular_ODE_toy',
                max_error=float(max(errors)), real_geometry_evaluated=False,
                coefficient_interpreter_error=interpreter_error,
                full_target_compiled=False, constant_three_node_exactness_in_exact_arithmetic=True,
                interpreter_source_sha256=hashlib.sha256(C_SOURCE.encode()).hexdigest())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--toy-only', action='store_true', required=True)
    parser.add_argument('--out', type=Path, required=True)
    arguments = parser.parse_args()
    report = toy_check()
    report['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    encoded = json.dumps(report, indent=2, sort_keys=True)+'\n'
    arguments.out.parent.mkdir(parents=True, exist_ok=True)
    arguments.out.write_text(encoded, encoding='utf-8')
    print(json.dumps(dict(output=str(arguments.out), bytes=len(encoded.encode()),
                          sha256=hashlib.sha256(encoded.encode()).hexdigest())))
