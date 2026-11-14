#!/usr/bin/env python3
"""Evaluate actual full fourth period/ruling functions for one frozen R45 input.

All actual compilation, profile integration and geometry integration are restricted
to this public repository's Actions. No lower-order closure is projected out.
"""
from __future__ import annotations

import argparse
from collections import defaultdict, OrderedDict
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial import polynomial as poly
from scipy.linalg import eigh

import literature_range_profile_algebra as formal
import literature_range_numeric_engine as engine
import literature_single_P_instance as single

LD, CD = engine.LD, engine.CD


class CapturingCompiler(formal.Compiler):
    def __init__(self):
        super().__init__()
        self.outputs = []

    def forcing_range(self, *args, **kwargs):
        field, output = super().forcing_range(*args, **kwargs)
        self.outputs.append((field, output))
        return field, output


def bump_polynomial_jets(x, coefficients):
    x = np.asarray(x, dtype=LD)
    out = np.zeros((5, len(x)), dtype=CD)
    inside = abs(x) < 1
    y = x[inside]
    d = 1-y*y
    with np.errstate(under='ignore'):
        eta = np.exp(-1/d)
    r1 = -2*y/d**2
    r2 = -2*(1+3*y*y)/d**3
    r3 = -24*y*(1+y*y)/d**4
    r4 = -24*(1+10*y*y+5*y**4)/d**5
    jets = [eta, eta*r1, eta*(r2+r1*r1), eta*(r3+3*r1*r2+r1**3),
            eta*(r4+4*r1*r3+3*r2*r2+6*r1*r1*r2+r1**4)]
    for order in range(5):
        value = np.zeros(len(y), dtype=CD)
        for j in range(order+1):
            value += math.comb(order, j)*jets[j]*poly.polyval(y, poly.polyder(coefficients, order-j))
        out[order, inside] = value
    return out


def prepare_profile(controls, quadrature_n):
    t, w, _ = engine.gauss_primitive(quadrature_n)
    x, weights = 2*t-1, 2*w
    basis = []
    for degree in (0, 2, 4, 6):
        coefficients = np.zeros(7, dtype=LD)
        coefficients[degree] = 1
        basis.append(bump_polynomial_jets(x, coefficients).real)
    basis = np.array(basis)
    gram0 = np.einsum('in,n,jn->ij', basis[:, 2], weights, basis[:, 2])
    gram2 = (np.einsum('in,n,jn->ij', basis[:, 2], weights*x*x, basis[:, 2])
             +2*np.einsum('in,n,jn->ij', basis[:, 1], weights, basis[:, 1]))
    eigenvalues, vectors = eigh(np.asarray(gram2, dtype=float), np.asarray(gram0, dtype=float))
    if eigenvalues[-1]-eigenvalues[0] < 1e-12*max(1., abs(eigenvalues[-1])):
        f, g = vectors[:, 0], vectors[:, 1]
    else:
        energy = (eigenvalues[1]+eigenvalues[2])/2
        weight = (eigenvalues[-1]-energy)/(eigenvalues[-1]-eigenvalues[0])
        f = math.sqrt(max(0., weight))*vectors[:, 0]+math.sqrt(max(0., 1-weight))*vectors[:, -1]
        g = (vectors[:, 1]+vectors[:, 2])/math.sqrt(2.)
    f_coefficients, g_coefficients = np.zeros(7), np.zeros(7)
    f_coefficients[[0, 2, 4, 6]] = f
    g_coefficients[[0, 2, 4, 6]] = g
    left, right = controls['physical_strip_xi']
    sigma = .8*(right-left)/72
    origin = (left+right)/2-35*sigma
    packet_amplitudes = [(-1 if j % 2 else 1)*np.cbrt(LD(math.comb(7, j))) for j in range(8)]
    amplitude = LD(sigma)**LD('1.5')/np.sqrt(sum(a*a for a in packet_amplitudes))
    result = dict(kind='R52-even-four-mode-overlapping-eight-packet-profile',
        raw_bump='exp(-1/(1-x^2)) on |x|<1; zero elsewhere',
        f_polynomial=f_coefficients.tolist(), g_polynomial=g_coefficients.tolist(),
        packet_centers=[10*j for j in range(8)],
        packet_amplitude_cubes=[(-1 if j % 2 else 1)*math.comb(7, j) for j in range(8)],
        packet_amplitude_formula='the real cube root of the stated signed integer; evaluated in long double',
        origin=origin, sigma=sigma, amplitude_decimal=str(amplitude),
        physical_interval=[left, right], basis_fit_quadrature_n=quadrature_n,
        basis_eigenvalues=eigenvalues.tolist(), gram0_condition=float(np.linalg.cond(np.asarray(gram0, dtype=float))),
        exact_profile_integrals_certified=False,
        normalization='common amplitude sigma^(3/2)/sqrt(sum packet_amplitude^2); fixed after this preparation',
        four_mode_coefficients_refit_during_validation=False,
        R53_fourth_leading_gate_claimed=False)
    encoded = json.dumps(result, sort_keys=True, separators=(',', ':'), allow_nan=False)
    result['profile_identity_sha256'] = hashlib.sha256(encoded.encode()).hexdigest()
    return result


class ProfileTable:
    def __init__(self, profiles, definition, n, deadline):
        self.profiles, self.definition = profiles, definition
        self.deadline = deadline
        left, right = definition['physical_interval']
        origin, sigma = definition['origin'], definition['sigma']
        bounds = [left]
        for center in definition['packet_centers']:
            bounds.extend([origin+sigma*(center-1), origin+sigma*(center+1)])
        bounds.append(right)
        if any(b <= a for a, b in zip(bounds[:-1], bounds[1:])):
            raise ValueError('profile panels must be strictly ordered and inside the frozen physical interval')
        t, weights, Q = engine.gauss_primitive(n)
        nodes, full_weights, panels = [], [], []
        for index, (a, b) in enumerate(zip(bounds[:-1], bounds[1:])):
            duration = LD(b)-LD(a)
            nodes.append(LD(a)+duration*t)
            full_weights.append(duration*weights)
            panels.append((slice(index*n, (index+1)*n), duration, weights, Q))
        self.nodes, self.weights = np.concatenate(nodes), np.concatenate(full_weights)
        self.panels = panels
        qjets = np.zeros((5, len(self.nodes)), dtype=CD)
        coefficients = np.asarray(definition['f_polynomial'], dtype=CD)+1j*np.asarray(definition['g_polynomial'], dtype=CD)
        for center, amplitude_cube in zip(definition['packet_centers'], definition['packet_amplitude_cubes']):
            amplitude = np.cbrt(LD(amplitude_cube))
            raw = (self.nodes-LD(origin))/LD(sigma)-LD(center)
            local = bump_polynomial_jets(raw, coefficients)
            for order in range(5):
                qjets[order] += LD(definition['amplitude_decimal'])*amplitude*local[order]/LD(sigma)**order
        self.qjets = qjets
        self.atoms = np.empty((len(profiles.atoms), len(self.nodes)), dtype=CD)
        self.monomial_cache = OrderedDict()
        self.monomial_cache_limit = 512
        self.conjugate_atoms = {}
        self.left_primitive_values = np.zeros(len(profiles.atoms), dtype=CD)
        aliases = 0
        for index, atom in enumerate(profiles.atoms):
            if index % 128 == 0 and time.monotonic() > deadline:
                raise TimeoutError('profile table budget exceeded')
            partner = self.conjugate_atom(index)
            if partner is not None and partner < index:
                self.atoms[index] = np.conjugate(self.atoms[partner])
                self.left_primitive_values[index] = np.conjugate(self.left_primitive_values[partner])
                aliases += 1
            elif atom[0] == 'jet':
                if atom[1] not in ('q', 'qbar') or atom[2] > 4:
                    raise ValueError('unexpected profile input jet')
                self.atoms[index] = qjets[atom[2]] if atom[1] == 'q' else np.conjugate(qjets[atom[2]])
            else:
                values = self.monomial(atom[1])
                primitive, endpoint = self.primitive(values)
                self.atoms[index] = primitive
                self.left_primitive_values[index] = endpoint
        self.conjugation_aliases = aliases

    def conjugate_atom(self, index):
        if index in self.conjugate_atoms:
            return self.conjugate_atoms[index]
        atom = self.profiles.atoms[index]
        if atom[0] == 'jet':
            key = ('jet', 'qbar' if atom[1] == 'q' else 'q', atom[2])
        else:
            power, factors = atom[1]
            partners = [self.conjugate_atom(j) for j in factors]
            if any(j is None for j in partners):
                self.conjugate_atoms[index] = None
                return None
            key = ('int_right', (power, tuple(sorted(partners))))
        partner = self.profiles.ids.get(key)
        self.conjugate_atoms[index] = partner
        return partner

    def monomial(self, monomial):
        if monomial in self.monomial_cache:
            self.monomial_cache.move_to_end(monomial)
        else:
            power, factors = monomial
            values = np.asarray(self.nodes**power, dtype=CD)
            for factor in factors:
                values = values*self.atoms[factor]
            self.monomial_cache[monomial] = values
            if len(self.monomial_cache) > self.monomial_cache_limit:
                self.monomial_cache.popitem(last=False)
        return self.monomial_cache[monomial]

    def primitive(self, values):
        result = np.empty_like(values)
        right_value = CD(0)
        for panel, duration, weights, Q in reversed(self.panels):
            data = values[panel]
            integral = weights@data
            result[panel] = right_value-duration*(integral-Q@data)
            right_value -= duration*integral
        return result, right_value

    def integral(self, monomial):
        return self.weights@self.monomial(monomial)

    def complex_moments(self):
        q1, q2 = self.qjets[1], self.qjets[2]
        values = [self.weights@(q2*q2), self.weights@(self.nodes*q2*q2),
                  self.weights@(self.nodes*self.nodes*q2*q2+2*q1*q1)]
        scales = [self.weights@abs(q2)**2, self.weights@(abs(self.nodes)*abs(q2)**2),
                  self.weights@(self.nodes*self.nodes*abs(q2)**2+2*abs(q1)**2)]
        return dict(values=[complex_pair(z) for z in values],
                    relative_magnitudes=[float(abs(v)/max(LD('1e-40'), s)) for v, s in zip(values, scales)],
                    positive_scales=[float(s) for s in scales],
                    q_jet_sup_samples=[float(np.max(abs(x))) for x in self.qjets])


def complex_pair(value):
    return [float(np.real(value)), float(np.imag(value))]


def function_stats(values, weights):
    return dict(L2=float(np.sqrt(np.sum(weights*abs(values)**2))),
                max_sample=float(np.max(abs(values))),
                imaginary_L2=float(np.sqrt(np.sum(weights*values.imag**2))))


def expression_function(expression, coefficient_values, table):
    result = np.zeros(len(table.nodes), dtype=CD)
    representation_bound = LD(0)
    for monomial, node in expression.terms.items():
        values = table.monomial(monomial)
        coefficient = coefficient_values[node]
        result += coefficient*values
        representation_bound += abs(coefficient)*np.max(abs(values))
    return result, representation_bound


def history_function(compiler, state, order, table, mode_name=None):
    result = np.zeros(len(table.nodes), dtype=CD)
    for index, label in enumerate(compiler.a.c.state_labels):
        if label[0] == order and (mode_name is None or label[1] == mode_name):
            result += state[index]*table.monomial(label[2])
    return result


def project_global_w(K, ws, weights):
    gram = (ws*weights)@ws.T
    rhs = (ws*weights)@K
    gram64 = np.asarray(gram, dtype=float)
    singular = np.linalg.svd(gram64, compute_uv=False)
    coefficients, _, rank, _ = np.linalg.lstsq(gram64, np.asarray(rhs, dtype=complex), rcond=1e-13)
    residual = K-np.asarray(coefficients, dtype=CD)@ws
    total = np.sum(weights*abs(K)**2)
    error = np.sum(weights*abs(residual)**2)
    return dict(L2=float(np.sqrt(total)), quotient_residual_L2=float(np.sqrt(error)),
                quotient_relative=float(np.sqrt(error/max(total, LD('1e-80')))),
                quotient_max_sample=float(np.max(abs(residual))),
                one_global_w_coefficients=[complex_pair(z) for z in coefficients],
                w_gram_singular_values=singular.tolist(), numeric_w_rank=int(rank),
                lstsq_relative_cutoff=1e-13,
                numerical_rank_is_not_an_exact_span_certificate=True,
                exact_range_certified=False)


def evaluate_level(compiler, integrator, controls, definition, geometry_n, profile_n, deadline, progress):
    table = ProfileTable(compiler.a.p, definition, profile_n, deadline)
    period_expressions = {mode: compiler.physical_fourth[mode]['period_rhs'] for mode in (-4, -2, 0)}
    rulings = {'second_B': compiler.outputs[0][1]['ruling_integrand'],
               'third_U': compiler.outputs[1][1]['ruling_integrand'],
               'third_V': compiler.outputs[2][1]['ruling_integrand'],
               **{f'fourth_{mode}': compiler.physical_fourth[mode]['ruling_integrand'] for mode in (-4, -2, 0)}}
    root_positions = {node: index for index, node in enumerate(integrator.final_roots)}
    projections = {}
    for name, expression in rulings.items():
        accumulated = defaultdict(lambda: CD(0))
        for monomial, node in expression.terms.items():
            accumulated[root_positions[node]] += table.integral(monomial)
        projections[name] = (np.array(list(accumulated), dtype=int), np.array(list(accumulated.values()), dtype=CD))
    state = np.zeros(len(compiler.a.c.state_rhs), dtype=LD)
    coefficient_integrals = np.zeros(len(integrator.final_roots), dtype=LD)
    absolute_integrals = np.zeros_like(coefficient_integrals)
    items = single.primitive_items(controls)
    reverse_items = [single.reverse_item(item) for item in reversed(items)]
    paths = [items, items, reverse_items, reverse_items]
    omega = LD(controls['start_state'][2])
    all_weights, all_w, all_rulings = [], [], {name: [] for name in rulings}
    boundaries, offsets = [], []
    first_P_integrals = None
    processed = 0
    for block_index, path in enumerate(paths):
        offset = omega-LD(single.item_start(path[0])[2])
        offsets.append(float(offset))
        for item in path:
            if time.monotonic() > deadline:
                raise TimeoutError(f'full geometry evaluation budget after {processed} segments')
            state, weights, geometry, values = integrator.step(item, state, geometry_n, offset)
            coefficient_integrals += values@weights
            absolute_integrals += abs(values)@weights
            h, k, omega_nodes = geometry[0], geometry[4], geometry[8]
            d = h*omega_nodes-k
            ws = np.array([(d*d+1)/(4*h), d/2, h/4], dtype=LD)
            all_weights.append(weights)
            all_w.append(ws)
            for name, (indices, moments) in projections.items():
                all_rulings[name].append((moments@values[indices])/h)
            processed += 1
            if progress and processed % 50 == 0:
                print(json.dumps(dict(stage='coefficient_integration', block=block_index,
                                      processed_segments=processed, geometry_n=geometry_n,
                                      profile_n=profile_n)), flush=True)
        omega += LD(single.item_end(path[-1])[2])-LD(single.item_start(path[0])[2])
        closures = {}
        for order, mode_name in [(2, compiler.a.c.state_labels[integrator.second[0]][1]),
                                  (3, compiler.a.c.state_labels[integrator.third[0]][1]),
                                  (3, 'V=anchored_recovery(H(A,Bbar))')]:
            values = history_function(compiler, state, order, table, mode_name)
            closures[mode_name] = function_stats(values, table.weights)
        boundaries.append(dict(block=block_index+1, state_function_closures=closures,
                               raw_state_sup_only_not_a_range_test=float(np.max(abs(state)))))
        if block_index == 0:
            first_P_integrals = coefficient_integrals.copy()
    weights = np.concatenate(all_weights)
    ws = np.concatenate(all_w, axis=1)
    ruling_reports = {}
    ruling_arrays = {}
    for name, values in all_rulings.items():
        K = np.concatenate(values)
        ruling_arrays[name] = K
        ruling_reports[name] = project_global_w(K, ws, weights) if name.startswith('fourth') else function_stats(K, weights)
    full_coefficients = dict(zip(integrator.final_roots, coefficient_integrals))
    first_coefficients = dict(zip(integrator.final_roots, first_P_integrals))
    abs_coefficients = dict(zip(integrator.final_roots, absolute_integrals))
    periods, arrays = {}, {}
    for mode, expression in period_expressions.items():
        value, bound = expression_function(expression, full_coefficients, table)
        first_value, _ = expression_function(expression, first_coefficients, table)
        arrays[mode] = value
        _, absolute_bound = expression_function(expression, abs_coefficients, table)
        periods[str(mode)] = dict(**function_stats(value, table.weights),
            single_P=function_stats(first_value, table.weights),
            full_minus_four_single_P=function_stats(value-4*first_value, table.weights),
            representation_l1_bound=float(bound), absolute_coefficient_majorant=float(absolute_bound),
            max_over_absolute_coefficient_majorant=float(np.max(abs(value))/max(absolute_bound, LD('1e-80'))),
            numerical_function_sample_sha256=hashlib.sha256(np.asarray(value, dtype=np.complex128).tobytes()).hexdigest())
    exact_seed = arrays[0]+2*np.real(arrays[-2]+arrays[-4])
    exact_seed_ruling = ruling_arrays['fourth_0']+2*np.real(
        ruling_arrays['fourth_-2']+ruling_arrays['fourth_-4'])
    harmonic_period_scale = sum(np.sqrt(np.sum(table.weights*abs(array)**2)) for array in arrays.values())
    return dict(geometry_quadrature_n=geometry_n, profile_quadrature_n=profile_n,
        profile_nodes=len(table.nodes), profile_conjugation_aliases=table.conjugation_aliases,
        profile_atom_bytes=int(table.atoms.nbytes),
        profile_monomial_cache_limit=table.monomial_cache_limit,
        processed_segments=processed, coefficient_precision=str(np.dtype(LD)),
        coefficient_precision_epsilon=float(np.finfo(LD).eps),
        profile_moments=table.complex_moments(), period_functions=periods,
        exact_seed_fourth_function_residual=function_stats(exact_seed, table.weights),
        exact_seed_period_relative_to_harmonics=float(
            np.sqrt(np.sum(table.weights*abs(exact_seed)**2))/max(harmonic_period_scale, LD('1e-80'))),
        exact_seed_fourth_ruling_residual=function_stats(exact_seed_ruling, weights),
        entire_four_block_ruling_global_quotient=ruling_reports,
        actual_boundary_history_functions=boundaries,
        natural_omega_offsets=offsets, natural_omega_end=float(omega),
        no_history_resets=True, profile_or_geometry_refit=False,
        profile_basis_independence_assumed=False,
        sampled_zero_is_not_exact_range=True, exact_fourth_range_certified=False)


def run(args):
    started = time.monotonic()
    deadline = started+args.max_seconds
    raw = args.geometry.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != args.geometry_sha256:
        raise ValueError('frozen geometry input SHA256 mismatch')
    source = json.loads(raw)
    if source.get('schema') != 'R45-single-P-instance-v1':
        raise ValueError('only the independent R45 single-P schema is accepted; old Klein output is not valid')
    current_single_sha = hashlib.sha256(Path(single.__file__).read_bytes()).hexdigest()
    current_base_sha = hashlib.sha256(Path(single.base.__file__).read_bytes()).hexdigest()
    if source.get('source_sha256') != current_single_sha:
        raise ValueError('frozen geometry constructor source does not match the imported single-P module')
    if source.get('imported_control_source_sha256') != current_base_sha:
        raise ValueError('frozen low-level control source does not match the imported base module')
    controls = source['controls']
    actual_identity = hashlib.sha256(json.dumps(controls, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()
    if actual_identity != source['design_identity_sha256']:
        raise ValueError('frozen control identity mismatch')
    definition = prepare_profile(controls, args.profile_fit_n)
    compiler = CapturingCompiler()
    compiler.compile(4, progress=args.progress)
    roots = set()
    for mode in (-4, -2, 0):
        for key in ('period_rhs', 'ruling_integrand'):
            roots.update(compiler.physical_fourth[mode][key].terms.values())
    for _, output in compiler.outputs[:3]:
        roots.update(output['ruling_integrand'].terms.values())
    integrator = engine.TriangularIntegrator(compiler, sorted(roots))
    levels, failure = [], None
    try:
        for geometry_n, profile_n in zip(args.geometry_nodes, args.profile_nodes):
            levels.append(evaluate_level(compiler, integrator, controls, definition,
                                        geometry_n, profile_n, deadline, args.progress))
    except (TimeoutError, FloatingPointError, ValueError, MemoryError) as error:
        failure = f'{type(error).__name__}: {error}'
    finally:
        integrator.close()
    result = dict(schema='R45-full-fourth-function-evaluation-v1',
        completion='complete' if failure is None else 'incomplete', failure=failure,
        github={name: os.environ.get(name) for name in
                ('GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_RUN_ATTEMPT', 'GITHUB_SHA')},
        geometry_input=str(args.geometry), geometry_input_sha256=digest,
        geometry_identity_sha256=source['design_identity_sha256'],
        input_geometry_finest_validation={key: source['validation'][-1][key] for key in
            ('single_P_matrix_norm', 'single_P_frame_target_error',
             'natural_four_block_frame_error', 'natural_four_block_alpha_closure_norm',
             'carried_omega_closure', 'scalar_cache_join_max', 'physical_omega_gap')},
        source_hashes={Path(module.__file__).name: hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
                       for module in (formal, engine, single, single.base)},
        runner_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        interpreter_source_sha256=hashlib.sha256(engine.C_SOURCE.encode()).hexdigest(),
        settings={key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()},
        profile_definition=definition, fixed_target='g_X+epsilon^2(dY_f)^2 with the same frozen f at all theta',
        coefficient_graph_sha256=formal.sequence_digest(compiler.a.c.nodes),
        profile_atom_graph_sha256=formal.sequence_digest(compiler.a.p.atoms),
        triangular_structure=dict(second_histories=len(integrator.second), third_histories=len(integrator.third),
            second_rhs_geometry_only=True, third_rhs_affine_in_second=True,
            fourth_observable_weighted_degree_max=max(integrator.degrees[j] for j in roots),
            constant_segments_three_Gauss_nodes_exact_in_exact_arithmetic=True),
        validation=levels, elapsed_seconds=time.monotonic()-started,
        frozen_input_exact_zero_operator_certified=False,
        exact_single_P_reduction_not_forced_on_approximate_input=True,
        finite_continuous_family_constructed=False, embedding_checked=False,
        reach_checked=False, task_complete=False)
    if len(levels) > 1:
        result['frozen_level_changes'] = [{
            str(mode): {key: levels[j]['period_functions'][str(mode)][key]-levels[j-1]['period_functions'][str(mode)][key]
                        for key in ('L2', 'max_sample')}
            for mode in (-4, -2, 0)} for j in range(1, len(levels))]
    return result


def toy_check():
    # Manual center-jet identity; no profile integral is evaluated.
    values = bump_polynomial_jets(np.array([LD(0)]), np.array([LD(1)]))[:, 0]
    expected = np.exp(LD(-1))*np.array([1, 0, -2, 0, -12], dtype=LD)
    error = float(np.max(abs(values-expected)))
    if error > 1e-15:
        raise AssertionError('manual bump center jets')
    return dict(kind='small_manual_profile_interface_toy', bump_center_jet_error=error,
                derivative_formula_up_to_four=True, full_target_compiled=False,
                real_profile_integrals_evaluated=False, real_geometry_evaluated=False,
                engine_toy=engine.toy_check())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--toy-only', action='store_true')
    parser.add_argument('--geometry', type=Path)
    parser.add_argument('--geometry-sha256')
    parser.add_argument('--geometry-nodes', nargs='+', type=int, default=[32, 64])
    parser.add_argument('--profile-nodes', nargs='+', type=int, default=[64, 96])
    parser.add_argument('--profile-fit-n', type=int, default=256)
    parser.add_argument('--max-seconds', type=float, default=1200.)
    parser.add_argument('--progress', action='store_true')
    args = parser.parse_args()
    if args.toy_only:
        result = toy_check()
        result['runner_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    else:
        if not (os.environ.get('GITHUB_ACTIONS') == 'true' and
                os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public'):
            parser.error('actual full fourth evaluation is restricted to this public repository Actions')
        if args.geometry is None or not args.geometry_sha256:
            parser.error('one frozen R45 geometry file and its SHA256 are required')
        if len(args.geometry_nodes) != len(args.profile_nodes) or min(args.geometry_nodes+args.profile_nodes+[args.profile_fit_n]) < 8:
            parser.error('paired refinement lists and at least eight quadrature nodes are required')
        if args.max_seconds <= 0:
            parser.error('positive runtime budget required')
        result = run(args)
    encoded = json.dumps(result, indent=2, sort_keys=True, allow_nan=False)+'\n'
    if len(encoded.encode()) > 1_000_000:
        raise RuntimeError('summary unexpectedly exceeds 1 MB; no large intermediate written')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(encoded, encoding='utf-8')
    print(json.dumps(dict(output=str(args.out), bytes=len(encoded.encode()),
                          sha256=hashlib.sha256(encoded.encode()).hexdigest(),
                          completion=result.get('completion', 'toy_only'))))


if __name__ == '__main__':
    main()
