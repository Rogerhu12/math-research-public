#!/usr/bin/env python3
"""Same-g symbolic bisection / zero-padded frequency refinement, Actions only.

The ideal Hermite restriction is exact.  Newly stored binary jets are
explicit carriers of it, with outward errors and continuous six-jet
difference bounds.  The actual fine field is reread; no old certificate
or convergence conclusion is inherited.  Original observation locations
and permanent geometric locations remain, with exact binary-coordinate
remapping and positive quadrature weights.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

import numpy as np


EXPECTED = dict(
    observed='26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d',
    batch='02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a',
    dense='e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d',
    scalar='a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670',
    integer='babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0',
    hold='ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1',
    difference='f3b5acf135589c2ad6f10c80bebf7dfdf919350d4b06e9dbb764ba2a2ca0ade0',
    geometry_interval='2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377',
    interval='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d',
    factory='2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216',
    point='fe8e926c3239d707d6af48efbc48c1755bbac84c3d5722bdbf40f7be7bb53cad',
    geometry='a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854',
    spectral='e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b''):
            digest.update(chunk)
    return digest.hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def write_json(path, value):
    path = Path(path)
    tmp = path.with_name(path.name+'.partial')
    tmp.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    tmp.replace(path)


def announce(**value):
    print(json.dumps(value, allow_nan=False), flush=True)


def sources(repo):
    topic = Path(repo)/'topics/visible-flex-larger-amplitude'
    folder = topic/'scripts/resume_20261120'
    return dict(observed=folder/'gauss_observed_closed_gram.py',
        batch=topic/'scripts/resume_20261120_batched_closed_gram.py',
        dense=topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py',
        scalar=topic/'notes/2026-11-17-parallel-model-full-hold-oracle.py',
        integer=topic/'notes/2026-11-17-parallel-inward-integral-enclosure.py',
        hold=topic/'scripts/parallel_20261117_negative_hold_profile_ivp.py',
        difference=folder/'fullclosed_C0_difference_interval.py',
        geometry_interval=folder/'fullclosed_geometry_interval.py',
        interval=topic/'scripts/parallel_20261117_arclength_interval_positive.py',
        factory=folder/'exact_reference_tail_lift.py',
        point=folder/'fullclosed_point_cotangent_working.py',
        geometry=topic/'scripts/resume_20261120_curvature_qp.py',
        spectral=folder/'positive_spectral_gram_weights.py')


def decode_json_scalar(value):
    value = np.asarray(value).item()
    return json.loads(value.decode() if isinstance(value, bytes) else str(value))


def exact_point(nodes, cell, u):
    cell, u = int(cell), F(u)
    if not 0 <= cell < len(nodes)-1 or not F(0) <= u <= F(1):
        raise ValueError('Point is outside the actual symbolic radial mesh')
    left, right = nodes[cell:cell+2]
    return (1-u)*left[0]+u*right[0], (1-u)*left[1]+u*right[1]


def map_point(cell, u, factor):
    """No coordinate rounding: binary u -> exact 2u or 2u-1."""
    cell, u = int(cell), F(float(u))
    if not F(0) <= u <= F(1):
        raise ValueError('Local material position must lie in [0,1]')
    if factor == 1:
        return cell, float(u)
    branch = int(u > F(1, 2))
    new = 2*u-branch
    carrier = float(new)
    if F(carrier) != new:
        raise ArithmeticError('A declared binary bisection coordinate was not represented exactly')
    return 2*cell+branch, carrier


def pad_modes(values, old, new):
    result = np.zeros((*values.shape[:-1], 3*new+2), dtype=values.dtype)
    result[..., :old+1] = values[..., :old+1]
    result[..., new+1:new+old+1] = values[..., old+1:2*old+1]
    result[..., 2*new+1:2*new+old+2] = values[..., 2*old+1:]
    return result


def restrict_jets(difference, modes, factor):
    """Ideal exact-node midpoint formulas, then explicit rounded carriers."""
    r, I = difference.r, difference.I
    old = difference.base['qjets']
    J, oldM = r.J, r.M
    old_boxes = old.copy(), old.copy()
    core = I.at(old_boxes, (0, 0, slice(1, oldM+1)))
    tangent = I.scale(core, -2*np.arange(1, oldM+1))
    old_boxes[0][0, 0, oldM+1:2*oldM+1] = tangent[0]
    old_boxes[1][0, 0, oldM+1:2*oldM+1] = tangent[1]
    newJ = factor*(J-1)+1
    jets = np.zeros((newJ, 3, 3*modes+2))
    errors = np.zeros_like(jets), np.zeros_like(jets)
    nodes = []
    mesh = np.empty(newJ)
    for i in range(J):
        j = factor*i
        jets[j] = pad_modes(old[i], oldM, modes)
        nodes.append(r.nodes[i])
        mesh[j] = r.mesh[i]
        if factor == 1 or i == J-1:
            continue
        h = r.width_box(r.nodes[i], r.nodes[i+1])
        if float(h[0]) <= 0:
            raise ValueError('The original exact cell width was not enclosed positively')
        left, right = I.at(old_boxes, i), I.at(old_boxes, i+1)
        y0, u0, a0 = [I.at(left, k) for k in range(3)]
        y1, u1, a1 = [I.at(right, k) for k in range(3)]
        ym = I.add(I.add(I.scale(I.add(y0, y1), .5),
            I.scale(I.mul(h, I.sub(u0, u1)), 5/32)),
            I.scale(I.mul(I.square(h), I.add(a0, a1)), 1/64))
        um = I.add(I.add(I.scale(I.div(I.sub(y1, y0), h), 15/8),
            I.scale(I.add(u0, u1), -7/16)), I.scale(I.mul(h, I.sub(a1, a0)), 1/32))
        am = I.add(I.scale(I.div(I.sub(u1, u0), h), 3/2), I.scale(I.add(a0, a1), -.25))
        midpoint = I.stack((ym, um, am))
        zero = np.all((left[0] == 0) & (left[1] == 0)
                      & (right[0] == 0) & (right[1] == 0), axis=0)
        midpoint = np.where(zero[None], 0., midpoint[0]), np.where(zero[None], 0., midpoint[1])
        value = midpoint[0]+(midpoint[1]-midpoint[0])/2
        if not np.isfinite(value).all():
            raise ArithmeticError('Midpoint jet carrier is not finite')
        error = I.sub(I.exact(value), midpoint)
        error = np.where(zero[None], 0., error[0]), np.where(zero[None], 0., error[1])
        jets[j+1] = pad_modes(value, oldM, modes)
        errors[0][j+1], errors[1][j+1] = [pad_modes(v, oldM, modes) for v in error]
        nodes.append(tuple((a+b)/2 for a, b in zip(r.nodes[i], r.nodes[i+1])))
        mesh[j+1] = r.mesh[i]+(r.mesh[i+1]-r.mesh[i])/2
    # The affine dependent core slot uses the same declared literal unpack.
    jets[0, 0, modes+1:2*modes+1] = -2*np.arange(1, modes+1)*jets[0, 0, 1:modes+1]
    if not np.all(np.diff(mesh) > 0):
        raise ValueError('Binary carrier cannot resolve the requested symbolic bisection')
    info = dict(parent_J=J, refined_J=newJ, parent_M=oldM, refined_M=modes,
        radial_factor=factor, exact_symbolic_bisection=True,
        exact_frequency_zero_padding=True, kept_node_free_jets_preserved=True,
        all_affine_core_cap_conditions_preserved=True,
        ideal_restricted_field_equals_parent=True,
        literal_stored_field_equality_certified=bool(np.all(errors[0] == 0) and np.all(errors[1] == 0)),
        inserted_jet_error_upper_per_derivative=[float(I.absolute_upper(errors)[:, k].max()) for k in range(3)],
        carrier_rule='Midpoint of outward exact-Hermite jet boxes; new mesh carrier is old literal midpoint',
        stored_field='Actual fine field has literal binary free jets; exact-map errors are reported, not silently identified with zero')
    return jets, nodes, mesh, errors, info


def difference_bounds(reader, nodes, errors, M):
    """Continuous q-only six-jet difference; lift/core/H are unchanged."""
    I = reader.I
    r = type(reader).__new__(type(reader))
    r.I, r.S, r.M, r.nu = I, reader.S, M, 2*np.arange(M+1)
    names = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')
    result = {name: dict(uniform_vector_norm_upper=0., worst_cell=None) for name in names}
    for cell in range(len(nodes)-1):
        if np.all(errors[0][cell:cell+2] == 0) and np.all(errors[1][cell:cell+2] == 0):
            continue
        h = r.width_box(nodes[cell], nodes[cell+1])
        if float(h[0]) <= 0:
            raise ValueError('The refined exact width is not positive')
        co = r.hermite(I.at(errors, cell), I.at(errors, cell+1), h)
        first = r.derivative(co, h)
        second = r.derivative(first, h)
        for name, value, angle_order in zip(names, (co, first, co, second, first, co), (0, 0, 1, 0, 1, 2)):
            channels = r.channels(value, angle_order)
            sums = [I.sum_upper(I.absolute_upper(v), axis=-1) for v, _ in channels]
            squares = [I.square(I.exact(value)) for value in sums]
            bound = float(I.sqrt(I.add(I.add(squares[0], squares[1]), squares[2]))[1].max())
            if bound > result[name]['uniform_vector_norm_upper']:
                result[name] = dict(uniform_vector_norm_upper=bound, worst_cell=cell)
    return dict(bounds=result, arithmetic='f512 outward binary64',
        scope='Same exact alpha*S+beta radial domain and all angles, all old modes plus zero new modes; actual fine binary field minus ideal exact restriction',
        complete_lift_difference_exactly_zero=True, curvature_or_reach_inherited=False)


def combine_observations(observed, mesh, width, new_nodes, old_nodes, old_plan, factor):
    old_rule = .5*old_plan.legacy_simpson_weights+.5*old_plan.quadrature_weights
    if (np.any(old_plan.legacy_simpson_weights < 0) or np.any(old_plan.quadrature_weights < 0)
            or not np.all(np.isfinite(old_rule)) or np.any(old_rule <= 0)):
        raise ValueError('The inherited complete observation rule must have positive finite row weights')
    breakpoint = (F(1), -F(width))
    if new_nodes.count(breakpoint) != 1:
        raise ValueError('Keep the unique exact old lift breakpoint as a refined node')
    plan = observed.make_plan(mesh, width, order=6, lift_break_node=new_nodes.index(breakpoint))
    cells = plan.cells.tolist()
    local = plan.local_u.tolist()
    times = plan.times.tolist()
    weights = list(plan.weights)
    quadrature = (plan.quadrature_weights/2).tolist()
    simpson = plan.legacy_simpson_weights.tolist()
    by_definition = {exact_point(new_nodes, cell, F(float(u))): index
                     for index, (cell, u) in enumerate(zip(cells, local))}
    mapping = []
    for old_index, (cell, u) in enumerate(zip(old_plan.cells, old_plan.local_u)):
        nc, nu = map_point(cell, u, factor)
        definition = exact_point(old_nodes, cell, F(float(u)))
        if exact_point(new_nodes, nc, F(nu)) != definition:
            raise ArithmeticError('Bisection changed an inherited symbolic observation')
        index = by_definition.get(definition)
        if index is None:
            if not old_plan.quadrature_weights[old_index] > 0:
                raise ValueError('An inherited unrepresented row has no positive quadrature weight')
            index = len(cells)
            by_definition[definition] = index
            h = mesh[nc+1]-mesh[nc]
            cells.append(nc); local.append(nu); times.append(mesh[nc]+h*nu)
            weights.append(observed.hermite_weights(h, nu))
            quadrature.append(0.); simpson.append(0.)
        quadrature[index] += old_plan.quadrature_weights[old_index]/2
        mapping.append(index)
    plan.cells = np.asarray(cells, dtype=int)
    plan.local_u = np.asarray(local)
    plan.times = np.asarray(times)
    plan.weights = np.asarray(weights)
    plan.quadrature_weights = np.asarray(quadrature)
    plan.legacy_simpson_weights = np.asarray(simpson)
    if np.any(.5*plan.legacy_simpson_weights+.5*plan.quadrature_weights <= 0):
        raise ArithmeticError('Every retained and new observation must have positive objective weight')
    return plan, np.asarray(mapping, dtype=int)


def upper_float(value):
    out = float(value)
    if F(out) < value:
        out = float(np.nextafter(out, np.inf))
    return out


def prepare_scalar(full, plan, nodes):
    values = np.empty(len(plan.cells))
    errors = np.empty_like(values)
    time_errors = np.empty_like(values)
    cached = {}
    legacy_boxes = []
    started = time.monotonic()
    for index, (cell, u, carrier_time) in enumerate(zip(plan.cells, plan.local_u, plan.times)):
        definition = exact_point(nodes, cell, F(float(u)))
        if definition not in cached:
            time_box = full.affine_time(*definition)
            a_box, _ = full.at_box(time_box)
            value = full.carrier(a_box)
            if definition == (F(0), F(0)):
                value = 1.
            elif definition == (F(1), F(0)):
                value = full.carrier(full.R)
            error = max(abs(F(value)-F(bound, full.h.S)) for bound in a_box)
            cached[definition] = (value, upper_float(error), time_box, a_box)
        values[index], errors[index], time_box, a_box = cached[definition]
        if index < plan.legacy_count:
            # These are the current integer-oracle boxes, in the new
            # node/midpoint order required by the frozen R657 Scalar.
            # No old stage box is copied and no extra oracle query is made.
            legacy_boxes.append(full.enclosure(a_box))
        time_errors[index] = upper_float(max(abs(F(float(carrier_time))-F(bound, full.h.S)) for bound in time_box))
        if (index+1) % 512 == 0:
            announce(event='fixed_g_refinement_scalar_progress', completed=index+1,
                total=len(values), unique_queries=len(cached), seconds=time.monotonic()-started)
    if not np.all(np.isfinite(values)) or not np.all(values > 0):
        raise ValueError('Same scalar oracle did not provide positive finite carriers')
    return values, errors, time_errors, dict(unique_exact_point_queries=len(cached),
        total_rows=len(values), maximum_a_carrier_error=float(errors.max()),
        maximum_time_carrier_error=float(time_errors.max()),
        current_exact_legacy_anchor_count=len(legacy_boxes),
        legacy_anchor_source='The same actual at_box results used for the new literal legacy a carriers',
        old_scalar_values_interpolated=False, new_target_fitted=False,
        scalar=full.metadata(), seconds=time.monotonic()-started), legacy_boxes


def model_definition(data, old_nodes, paths, old_node_report, old_carrier, scalar_input, factory):
    labels = {}
    for key in ('reference_tail_lambda', 'exact_tail_lambda'):
        if key in data:
            labels[key] = F(float(data[key]))
    definition = decode_json_scalar(data['reference_tail_model_json']) if 'reference_tail_model_json' in data else None
    if definition is not None:
        labels['reference_tail_model_json.lambda_value'] = F(float(definition['lambda_value']))
    if labels and (len(set(labels.values())) != 1 or not F(0) <= next(iter(labels.values())) <= F(1)):
        raise ValueError('The actual source field has inconsistent tail-lambda tags')
    lam = float(next(iter(labels.values()))) if labels else 0.
    if definition is None:
        if lam != 0 or 'field_representation' in data:
            raise ValueError('A nonzero/tagged tail field needs its complete actual canonical model')
        return dict(kind='original_polynomial_lift', lambda_value=0., definition=None)
    M = (data['qjets'].shape[-1]-2)//3
    expected = dict(schema=factory.SCHEMA, source_sha256=sha(paths['factory']), M=M,
        mesh_sha256=factory.array_sha(data['mesh']), node_report_sha256=sha(old_node_report),
        scalar_input_sha256=sha(scalar_input), original_observation_carrier_sha256=sha(old_carrier))
    if any(definition.get(key) != value for key, value in expected.items()):
        raise ValueError('R671 definition does not belong to this actual mesh/scalar/factory')
    for key, source in (('scalar_source', 'scalar'), ('integer_source', 'integer'),
                        ('hold_source', 'hold'), ('observed_source', 'observed')):
        if definition.get('source_sha256s', {}).get(key) != sha(paths[source]):
            raise ValueError('Changed R671 scalar/observation source: '+key)
    for key in ('dense', 'batch', 'observed'):
        if definition.get('operator_source_sha256s', {}).get(key) != sha(paths[key]):
            raise ValueError('Changed R671 complete-field operator source: '+key)
    start = tuple(F(v) for v in definition['eta_start_symbolic'])
    end = tuple(F(v) for v in definition['eta_end_symbolic'])
    if (old_nodes[int(definition['eta_start_node'])] != start
            or old_nodes[int(definition['eta_end_node'])] != end
            or end != (F(1), -F(float(data['width'])))):
        raise ValueError('R671 eta symbols and old carrier indices disagree')
    return dict(kind='R671_exact_reference_tail', lambda_value=lam,
                eta_start_symbolic=start, eta_end_symbolic=end, definition=definition)


def remap_manifests(files, old_carrier, old_plan, old_nodes, new_nodes, factor, source_angles):
    kinds = {key: {} for key in ('curvature_points', 'radius_points', 'protected_curvature_points')}
    ancestry = []
    def put(kind, point):
        cell, u, phi = int(point[0]), float(point[1]), float(point[2])
        if not np.isfinite([u, phi]).all() or not 0 <= cell < len(old_nodes)-1 or not 0 <= u <= 1:
            raise ValueError('A permanent geometry point is outside the actual original carrier')
        child, newu = map_point(cell, u, factor)
        if exact_point(old_nodes, cell, F(u)) != exact_point(new_nodes, child, F(newu)):
            raise ArithmeticError('A permanent material location changed under bisection')
        kinds[kind][(child, newu, phi)] = None
    for path in files:
        payload = json.loads(Path(path).read_text())
        declared = payload.get('carrier_sha256', payload.get('observation_carrier_sha256'))
        if declared != sha(old_carrier):
            raise ValueError('Permanent positions need their actual parent carrier identity')
        for kind in kinds:
            for point in payload.get(kind, []):
                put(kind, point)
        for key, kind in (('grid_curvature_locations', 'curvature_points'),
                          ('grid_radius_locations', 'radius_points')):
            N = int(payload.get('optimization_full_angles', payload.get('full_angles', source_angles)))
            for stage, angle in payload.get(key, []):
                stage, angle = int(stage), int(angle)
                if not 0 <= stage < len(old_plan.cells) or not 0 <= angle < N:
                    raise ValueError('Permanent grid location is outside its declared old carrier')
                put(kind, (old_plan.cells[stage], old_plan.local_u[stage], 2*np.pi*angle/N))
        ancestry.append(file_record(path))
    for point in kinds['protected_curvature_points']:
        kinds['curvature_points'][point] = None
    if not kinds['curvature_points'] or not kinds['radius_points']:
        raise ValueError('Provide the complete permanent curvature and radius location union')
    return {key: [list(value) for value in positions] for key, positions in kinds.items()}, ancestry


class CommonGridReadout:
    """The fine field on the identical parent rows/weights/scalar carriers."""
    def __init__(self, problem, old_plan, old_carrier, mapping, source_angles, spectral):
        self.problem, self.spectral = problem, spectral
        self.parameters = spectral.Parameters(p=8, epsilon=.001, scale=.05)
        self.mapping = np.asarray(mapping, dtype=int)
        self.weights = .5*old_plan.legacy_simpson_weights+.5*old_plan.quadrature_weights
        self.a = old_carrier['a_observations']
        self.N = int(source_angles)
        self.angles = np.arange(0, problem.N, problem.full_N//self.N, dtype=int)
        old_phi = np.pi*np.arange(self.N//4+1)/(self.N//2)
        if not np.array_equal(problem.phi[self.angles], old_phi):
            raise ValueError('The common-grid reader needs the literal parent angular carriers')
        self.orbit = problem.multiplicity[self.angles]
        self.count = 0
        self.phi_sum = self.sse = self.maximum = 0.
        self.minimum_determinant = float('inf')
        self.worst = None

    def update(self, E, Fg, G, rho, start, stop):
        rows = np.flatnonzero((self.mapping >= start) & (self.mapping < stop))
        if not len(rows):
            return
        selected = np.ix_(self.mapping[rows]-start, self.angles)
        ar = self.a[rows, None]*rho[self.angles][None]
        residual = np.stack((E[selected]-1, Fg[selected]/ar, G[selected]/(ar*ar)-1), axis=-1)
        plus, minus, _ = self.spectral.eigenvalues(residual)
        maximum = np.maximum(abs(plus), abs(minus))
        index = np.unravel_index(int(np.argmax(maximum)), maximum.shape)
        if float(maximum[index]) > self.maximum:
            self.maximum = float(maximum[index])
            self.worst = dict(parent_stage=int(rows[index[0]]),
                parent_quarter_angle_index=int(index[1]), fine_stage=int(self.mapping[rows[index[0]]]),
                phi=float(self.problem.phi[self.angles[index[1]]]))
        self.minimum_determinant = min(self.minimum_determinant,
            float(((1+residual[..., 0])*(1+residual[..., 2])-residual[..., 1]**2).min()))
        self.phi_sum += float(self.weights[rows]@(
            self.spectral.point_loss(residual, self.parameters)@self.orbit))
        squares = residual[..., 0]**2+2*residual[..., 1]**2+residual[..., 2]**2
        self.sse += float(self.weights[rows]@(squares@self.orbit))
        self.count += len(rows)

    def report(self):
        denominator = float(self.weights.sum()*self.N)
        return dict(parent_rows=len(self.mapping), rows_read=self.count,
            complete_parent_row_scope=self.count == len(self.mapping),
            full_angles=self.N, mean_Phi=self.phi_sum/denominator,
            weighted_frobenius_sse=self.sse, mean_weighted_frobenius_sse=self.sse/denominator,
            maximum_relative_Gram=self.maximum, worst_Gram=self.worst,
            minimum_relative_determinant=self.minimum_determinant if self.count else None,
            positive_spectral_parameters=self.parameters.as_dict(), legacy_fraction=.5,
            minimum_radial_weight=float(self.weights.min()),
            normalization_denominator=denominator,
            exact_parent_scalar_carriers_used=True, same_original_scalar_oracle=True,
            exact_parent_angle_carriers_used=True,
            target_scalar_interpolation_used=False,
            scope='Current fine field at every exact parent observation, with parent angles, parent positive weights and literal parent a carriers',
            cross_layer_fine_Phi_subtraction_used=False,
            parent_field_evaluated_again=False, convergence_claimed=False)


def numerical_readout(op, x, factory, spectral, point, observed, geometry, manifests,
                      old_plan, old_carrier, inherited_map, source_angles):
    p = op.prepare(x)
    radial = op.mixed_stage_weights(.5)
    parameters = spectral.Parameters(p=8, epsilon=.001, scale=.05)
    phi_sum, weighted_sse, maximum, min_det = 0., 0., 0., float('inf')
    K, radius, invalid = 0., 0., 0
    worst_gram = worst_K = farthest = None
    common = CommonGridReadout(op, old_plan, old_carrier, inherited_map, source_angles, spectral)
    for start in range(0, op.P, op.stage_block):
        stop = min(op.P, start+op.stage_block)
        fields = factory.fields_block_observed(op, p, start, stop)
        v, t = fields['Fs'], fields['Fphi']
        E = np.einsum('bni,bni->bn', v, v)
        Fg = np.einsum('bni,bni->bn', v, t)
        G = np.einsum('bni,bni->bn', t, t)
        common.update(E, Fg, G, p.rho, start, stop)
        ar = op.a[start:stop, None]*p.rho[None]
        raw = np.stack((E-1, Fg/ar, G/(ar*ar)-1), axis=-1)
        lp, lm, _ = spectral.eigenvalues(raw)
        error = np.maximum(abs(lp), abs(lm))
        local = np.unravel_index(int(np.argmax(error)), error.shape)
        def location(at):
            row = start+int(at[0])
            return dict(stage=row, cell=int(op.observation_cells[row]),
                u=float(op.observation_u[row]), phi=float(op.phi[int(at[1])]))
        if float(error[local]) > maximum:
            maximum, worst_gram = float(error[local]), location(local)
        min_det = min(min_det, float(((1+raw[..., 0])*(1+raw[..., 2])-raw[..., 1]**2).min()))
        phi_sum += float(radial[start:stop]@(spectral.point_loss(raw, parameters)@op.multiplicity))
        squared = raw[..., 0]**2+2*raw[..., 1]**2+raw[..., 2]**2
        weighted_sse += float(radial[start:stop]@(squared@op.multiplicity))
        normal = np.cross(v, t)
        W2 = np.einsum('bni,bni->bn', normal, normal)
        good = np.isfinite(W2) & (W2 > 0)
        invalid += int(np.count_nonzero(~good))
        np.divide(normal, np.sqrt(np.maximum(W2, 0))[..., None], out=normal, where=good[..., None])
        e, f, g = [np.einsum('bni,bni->bn', fields[name], normal)
                   for name in ('Fss', 'Fsphi', 'Fphiphi')]
        tr = np.divide(e*G+g*E-2*f*Fg, W2, out=np.zeros_like(E), where=good)
        det = np.divide(e*g-f*f, W2, out=np.zeros_like(E), where=good)
        curvature = .5*(np.abs(tr)+np.sqrt(np.maximum(0., tr*tr-4*det)))
        at = np.unravel_index(int(np.argmax(curvature)), curvature.shape)
        if float(curvature[at]) > K:
            K, worst_K = float(curvature[at]), location(at)
        radii = np.linalg.norm(fields['F'], axis=2)
        at = np.unravel_index(int(np.argmax(radii)), radii.shape)
        if float(radii[at]) > radius:
            radius, farthest = float(radii[at]), location(at)
    point_module = factory.point_adapter(point)
    witnesses = {}
    union = dict.fromkeys(tuple(p) for kind in ('curvature_points', 'radius_points')
                          for p in manifests[kind])
    permanent_K, permanent_radius = 0., 0.
    for location in union:
        witness = dict(zip(('cell', 'u', 'phi'), location))
        value = point_module.witness_geometry(op, p, witness, geometry, observed)
        witnesses[str(location)] = value
        if value['complete']:
            permanent_K = max(permanent_K, value['maximum_absolute_principal_curvature'])
            permanent_radius = max(permanent_radius, value['radius'])
        else:
            invalid += 1
    denominator = float(radial.sum()*op.full_N)
    return dict(rows=op.P, full_angles=op.full_N, evaluated_quarter_angles=op.N,
        mean_Phi=phi_sum/denominator, positive_spectral_parameters=parameters.as_dict(),
        minimum_radial_weight=float(radial.min()), normalization_denominator=denominator,
        weighted_frobenius_sse=weighted_sse, mean_weighted_frobenius_sse=weighted_sse/denominator,
        maximum_relative_Gram=maximum, minimum_relative_determinant=min_det,
        worst_Gram=worst_gram, observed_maximum_absolute_curvature=K, worst_curvature=worst_K,
        observed_maximum_radius=radius, farthest=farthest,
        permanent_maximum_absolute_curvature=permanent_K, permanent_maximum_radius=permanent_radius,
        permanent_readout=witnesses, permanent_locations_read=len(union),
        common_parent_grid=common.report(),
        observed_rho_minimum=float(p.rho.min()),
        invalid_point_count=invalid, all_point_immersions_paid=invalid == 0,
        continuous_metric_certified=False, continuous_geometry_certified=False, reach_certified=False,
        accepted_nonlinear_step=False, same_g_refinement_convergence_demonstrated=False,
        scope='Actual new literal fine field; complete new/retained finite rows and every permanent location reread once')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'bundle', 'carrier', 'node-report', 'scalar-input', 'outdir'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--manifest', type=Path, action='append', required=True)
    parser.add_argument('--radial-factor', type=int, choices=(1, 2), default=2)
    parser.add_argument('--modes', type=int)
    parser.add_argument('--source-angles', type=int)
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--stage-block', type=int, default=64)
    parser.add_argument('--transfer-only', action='store_true')
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Same-g scientific refinement belongs in the public repository Actions')
    for key in ('repo', 'bundle', 'carrier', 'node_report', 'scalar_input', 'outdir'):
        setattr(args, key, getattr(args, key).resolve())
    args.outdir.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    paths = sources(args.repo)
    for key, path in paths.items():
        if sha(path) != EXPECTED[key]:
            raise ValueError('Changed proved refinement dependency: '+key)
    observed = load('fixed_g_refinement_observed', paths['observed'])
    factory = load('fixed_g_refinement_reference_tail', paths['factory'])
    difference_module = load('fixed_g_refinement_exact_model', paths['difference'])
    d = difference_module.Difference(args.bundle, args.bundle, args.node_report,
                                    paths['geometry_interval'], paths['interval'])
    data, old_nodes = d.base, d.r.nodes
    oldM = d.r.M
    M = args.modes if args.modes is not None else oldM
    with np.load(args.carrier, allow_pickle=False) as raw:
        old_carrier = {key: np.array(raw[key]) for key in raw.files}
    recorded_angles = old_carrier.get('observation_default_full_angles',
                                      data.get('refinement_evaluation_full_angles'))
    if args.source_angles is None:
        args.source_angles = int(recorded_angles) if recorded_angles is not None else 2048
    elif recorded_angles is not None and args.source_angles != int(recorded_angles):
        raise ValueError('The declared old angular grid differs from its actual refinement carrier tag')
    ratio = args.angles//args.source_angles if args.source_angles > 0 else 0
    if (M < oldM or args.angles <= 4*M or args.angles % 4 or args.source_angles <= 4*oldM
            or args.source_angles % 4 or args.angles % args.source_angles
            or ratio < 1 or ratio & (ratio-1) or args.stage_block < 1):
        raise ValueError('Retain all old modes and use a full angular grid containing the declared old grid')
    if args.radial_factor == 1 and M == oldM and args.angles == args.source_angles:
        raise ValueError('Declare an actual radial, frequency, or angular refinement')
    for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3'):
        if not np.array_equal(data[key], old_carrier[key]):
            raise ValueError('The source observation carrier differs from the actual bundle: '+key)
    old_plan = observed.ObservationPlan.from_arrays(old_carrier)
    model = model_definition(data, old_nodes, paths, args.node_report, args.carrier, args.scalar_input, factory)
    jets, nodes, mesh, errors, transfer = restrict_jets(d, M, args.radial_factor)
    transfer['continuous_sixjet_rounding_difference'] = difference_bounds(d.r, nodes, errors, M)
    error_path = args.outdir/'transfer-jet-error-boxes.npz'
    np.savez_compressed(error_path, lower=errors[0], upper=errors[1],
        old_node_to_new=np.arange(len(old_nodes))*args.radial_factor)
    old_report = json.loads(args.node_report.read_text())
    if old_report['input_sha256'] != sha(args.scalar_input):
        raise ValueError('Refinement cannot replace the original exact scalar input')
    raw = args.scalar_input.read_bytes()
    scalar_data = json.loads(gzip.decompress(raw) if args.scalar_input.suffix == '.gz' else raw)
    scalar_source = load('fixed_g_refinement_original_FullHold', paths['scalar'])
    full = scalar_source.FullHold(scalar_data, paths['integer'], paths['hold'],
        panels=int(old_report['scalar']['simpson_panels_per_ramp']))
    if full.carrier(full.S) != mesh[-1] or full.carrier(full.R) != float(data['radius']):
        raise ValueError('Refinement changed the original scalar endpoint/radius carrier')
    plan, inherited_map = combine_observations(observed, mesh, float(data['width']),
        nodes, old_nodes, old_plan, args.radial_factor)
    scalar_values, scalar_errors, time_errors, scalar_metadata, legacy_a_boxes = prepare_scalar(full, plan, nodes)
    node_path = args.outdir/'refined-symbolic-nodes.json'
    # Rebuild the current node report. Old J/stage counts, stage boxes,
    # projection diagnostics and bundle identity do not describe this mesh.
    new_node_report = dict(schema='same-fixed-g-refined-symbolic-nodes-v1',
        source_sha256=sha(__file__), input_path=str(args.scalar_input),
        input_sha256=sha(args.scalar_input), scalar_source_path=str(paths['scalar']),
        scalar=full.metadata(), S_carrier=float(mesh[-1]), radius_carrier=float(data['radius']),
        M=M, n=3*M+2, J=len(nodes), cells=len(nodes)-1,
        stages=plan.legacy_count, observation_rows=len(plan.cells),
        suggested_operator_N=args.angles, Hcap=float(data['Hcap']),
        width_exact=str(F(float(data['width']))), width_carrier=float(data['width']),
        maximum_a_carrier_error_upper=float(scalar_errors.max()),
        maximum_stage_time_carrier_error_upper=float(time_errors.max()),
        true_a_stage_boxes=legacy_a_boxes,
        true_scalar_nodes=[dict(S_coefficient=str(a), constant=str(b)) for a, b in nodes],
        refinement_parent=file_record(args.node_report),
        field_definition='Exact binary free q jets on the new exact alpha*S+beta nodes; exact core affine slots; original or separately rebound canonical R671 lift',
        numerical_operator_scope='Ordinary double carrier mesh/a/R with enclosed scalar/time errors; this is not a full field rounding or continuous metric certificate',
        nonlinear_solve=False, metric_accepted=False, embedding_certified=False,
        reach_certified=False, old_candidate_certificates_inherited=False,
        refinement=dict(radial_factor=args.radial_factor, original_nodes_retained=True,
            exact_scalar_definition_unchanged=True, target_metric_unchanged=True,
            source_bundle=file_record(args.bundle), source_M=oldM, target_M=M))
    write_json(node_path, new_node_report)
    base_arrays = dict(mesh=mesh, a_stages=scalar_values[:plan.legacy_count],
        a_stage_absolute_error=scalar_errors[:plan.legacy_count],
        stage_time_absolute_error=time_errors[:plan.legacy_count], qjets=jets,
        radius=np.array(data['radius']), width=np.array(data['width']),
        fixed_core_first3=np.array(data['fixed_core_first3']), Hcap=np.array(data['Hcap']),
        core_coefficients=jets[0, 0, 1:M+1],
        refinement_evaluation_full_angles=np.array(args.angles))
    carrier_path = args.outdir/'refined-same-g-observations.npz'
    arrays = plan.arrays()
    arrays.update({key: base_arrays[key] for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3')})
    arrays.update(a_observations=scalar_values, a_observation_absolute_error=scalar_errors,
        observation_time_absolute_error=time_errors, refinement_parent_stage_map=inherited_map,
        refinement_parent_carrier_sha256=np.array(sha(args.carrier)),
        observation_default_full_angles=np.array(args.angles),
        quadrature_definition=np.array('one half new six-Gauss rule plus one half complete parent quadrature; same total radial integral'))
    np.savez_compressed(carrier_path, **arrays)
    provisional = args.outdir/'refined-coordinate-carrier.npz'
    np.savez_compressed(provisional, **base_arrays)
    context = None
    if model['definition'] is not None:
        start = nodes.index(model['eta_start_symbolic'])
        end = nodes.index(model['eta_end_symbolic'])
        context = factory.TailLiftContext.from_files(bundle=provisional, carrier=carrier_path,
            node_report=node_path, scalar_input=args.scalar_input,
            scalar_source=paths['scalar'], integer_source=paths['integer'], hold_source=paths['hold'],
            observed_source=paths['observed'], eta_start_node=start,
            lambda_value=model['lambda_value'], panels=int(full.panels))
        problem, _ = context.create_pair(paths['dense'], paths['batch'],
            N=args.angles, stage_block=args.stage_block, quarter=True)
        if (tuple(F(v) for v in context.definition()['eta_start_symbolic']) != model['eta_start_symbolic']
                or tuple(F(v) for v in context.definition()['eta_end_symbolic']) != model['eta_end_symbolic']):
            raise ArithmeticError('Refinement moved the physical eta transition')
        context.save_carrier(args.outdir/'refined-reference-tail-carrier.npz',
                             args.outdir/'refined-reference-tail-carrier.json')
        x, affine = problem.pack(jets, float(data['Hcap']), require_affine=True)
        final_arrays = context.bundle_arrays(problem, x)
        final_arrays.update(exact_tail_lambda=np.array(model['lambda_value']),
            exact_tail_eta_start_node=np.array(start),
            field_representation=np.array('R671-exact-reference-tail-v1'),
            refinement_evaluation_full_angles=np.array(args.angles))
        refined_model = context.definition()
    else:
        problem = observed.create(paths['dense'], mesh, base_arrays['a_stages'], float(data['radius']),
            data['fixed_core_first3'], batch_source=paths['batch'], observation_plan=plan,
            a_observations=scalar_values, M=M, N=args.angles, width=float(data['width']),
            quarter=True, stage_block=args.stage_block)
        x, affine = problem.pack(jets, float(data['Hcap']), require_affine=True)
        final_arrays = base_arrays
        refined_model = dict(kind='original_polynomial_lift', lambda_value=0.)
    final = args.outdir/'refined-seed.npz'
    np.savez_compressed(final, **final_arrays)
    locations, ancestry = remap_manifests(args.manifest, args.carrier, old_plan,
        old_nodes, nodes, args.radial_factor, args.source_angles)
    manifest_path = args.outdir/'refined-permanent-locations.json'
    permanent = dict(schema='immutable-curvature-history-locations-v1',
        bundle_sha256=sha(final), carrier_sha256=sha(carrier_path), sources=ancestry,
        parent_bundle_sha256=sha(args.bundle), parent_carrier_sha256=sha(args.carrier),
        refinement_source_sha256=sha(__file__), **locations,
        remapping='Exact dyadic radial restriction; every binary phi unchanged; no decimal rounding or geometric value inheritance',
        coordinate_scope='Same exact radial s and chart phi; core is unchanged by zero padding, so material Theta is unchanged at transfer',
        retained_all_declared_location_values=True, old_geometric_values_inherited=False)
    # Compact JSON changes whitespace only; no arbitrary size cutoff and no point removal.
    manifest_path.write_text(json.dumps(permanent, separators=(',', ':'), allow_nan=False)+'\n')
    report_path = args.outdir/'refinement-report.json'
    report = dict(schema='same-fixed-g-fullclosed-refinement-actions-v1',
        source_sha256=sha(__file__), execution={key: os.environ.get(key) for key in
            ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','GITHUB_SHA')},
        sources={key: file_record(path) for key, path in paths.items()},
        inputs=dict(bundle=file_record(args.bundle), carrier=file_record(args.carrier),
            node_report=file_record(args.node_report), scalar_input=file_record(args.scalar_input)),
        outputs=dict(bundle=file_record(final), carrier=file_record(carrier_path),
            node_report=file_record(node_path), permanent_locations=file_record(manifest_path),
            transfer_error_boxes=file_record(error_path)),
        transfer=transfer, exact_affine_seed=affine, scalar_preparation=scalar_metadata,
        parent_model=({key: [str(v) for v in value] if key.endswith('_symbolic') else value
                       for key, value in model.items()}),
        refined_model=refined_model,
        observations=dict(parent_rows=len(old_plan.cells), new_rows=len(plan.cells),
            refined_legacy_rows=plan.legacy_count, inherited_row_mapping_complete=True,
            inherited_scalar_carriers_bitwise_equal=bool(np.array_equal(
                scalar_values[inherited_map], old_carrier['a_observations'])),
            positive_row_weights=True, legacy_fraction=.5,
            quadrature_mixture='one half new per-piece six-Gauss plus one half complete parent rule',
            native_prefix_is_refined_node_midpoint_rows=True,
            exact_Gauss_quadrature_claimed=False),
        angular_refinement=dict(source_full_angles=args.source_angles, refined_full_angles=args.angles,
            dyadic_angle_multiplier=ratio, old_ideal_angles_are_subset=True),
        nonlinear_solve_performed=False, finite_readout_performed=False,
        continuous_metric_certified=False, continuous_geometry_certified=False,
        same_g_refinement_convergence_demonstrated=False, topic_completion_certified=False,
        old_candidate_certificates_inherited=False)
    write_json(report_path, report)
    if not args.transfer_only:
        spectral = load('fixed_g_refinement_spectral_readout', paths['spectral'])
        point = load('fixed_g_refinement_point_fields', paths['point'])
        geometry = load('fixed_g_refinement_true_curvature', paths['geometry'])
        report['readout'] = numerical_readout(problem, x, factory, spectral, point, observed, geometry,
            locations, old_plan, old_carrier, inherited_map, args.source_angles)
        report['finite_readout_performed'] = True
    report['seconds'] = time.monotonic()-started
    write_json(report_path, report)
    announce(event='same_g_refinement_returned', report=file_record(report_path),
        bundle=file_record(final), carrier=file_record(carrier_path), node_report=file_record(node_path),
        manifest=file_record(manifest_path), original_M=oldM, refined_M=M,
        original_J=len(old_nodes), refined_J=len(nodes), finite_readout_performed=report['finite_readout_performed'],
        nonlinear_solve_performed=False, same_g_refinement_convergence_demonstrated=False,
        seconds=report['seconds'])


def common_main(argv):
    """Read a genuinely solved fine candidate on the original common grid."""
    parser = argparse.ArgumentParser(description=common_main.__doc__)
    for key in ('repo', 'refinement-report', 'bundle', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--stage-block', type=int, default=64)
    a = parser.parse_args(argv)
    if a.stage_block < 1:
        raise ValueError('The stage block must be positive')
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual common-grid field reads belong in public Actions')
    report = json.loads(a.refinement_report.read_text())
    if report['source_sha256'] != sha(__file__) or a.out.exists():
        raise ValueError('Use this exact refinement source and a fresh common-grid report')
    paths = sources(a.repo)
    for key, path in paths.items():
        if sha(path) != EXPECTED[key]:
            raise ValueError('Changed common-grid dependency: '+key)
    for record in [report['outputs'][key] for key in ('carrier','node_report')]+[
            report['inputs']['carrier'],report['inputs']['scalar_input']]:
        if sha(record['path']) != record['sha256']:
            raise ValueError('Changed common-grid carrier/scalar input')
    with np.load(a.bundle, allow_pickle=False) as raw:
        data = {key: np.array(raw[key]) for key in raw.files}
    with np.load(report['outputs']['carrier']['path'], allow_pickle=False) as raw:
        carrier = {key: np.array(raw[key]) for key in raw.files}
    with np.load(report['inputs']['carrier']['path'], allow_pickle=False) as raw:
        old_carrier = {key: np.array(raw[key]) for key in raw.files}
    for key in ('mesh','a_stages','radius','width','fixed_core_first3'):
        if not np.array_equal(data[key], carrier[key]):
            raise ValueError('The solved fine candidate changed the declared same-g carrier: '+key)
    observed = load('common_grid_refined_observed', paths['observed'])
    factory = load('common_grid_refined_factory', paths['factory'])
    spectral = load('common_grid_fixed_spectral', paths['spectral'])
    plan = observed.ObservationPlan.from_arrays(carrier)
    old_plan = observed.ObservationPlan.from_arrays(old_carrier)
    M = (data['qjets'].shape[-1]-2)//3
    if M != report['transfer']['refined_M']:
        raise ValueError('The solved candidate changed the declared fine frequency space')
    definition = report['refined_model']
    N = int(report['angular_refinement']['refined_full_angles'])
    if definition.get('schema') == factory.SCHEMA:
        current = decode_json_scalar(data['reference_tail_model_json'])
        if current != definition:
            raise ValueError('The solved fine candidate changed its fixed lambda/eta/scalar model')
        context = factory.TailLiftContext.from_files(bundle=a.bundle,
            carrier=report['outputs']['carrier']['path'], node_report=report['outputs']['node_report']['path'],
            scalar_input=report['inputs']['scalar_input']['path'], scalar_source=paths['scalar'],
            integer_source=paths['integer'], hold_source=paths['hold'], observed_source=paths['observed'],
            eta_start_node=definition['eta_start_node'], lambda_value=definition['lambda_value'],
            panels=int(report['scalar_preparation']['scalar']['simpson_panels_per_ramp']))
        op, _ = context.create_pair(paths['dense'], paths['batch'], N=N,
            stage_block=a.stage_block, quarter=True)
    else:
        if any(key in data for key in ('reference_tail_lambda','exact_tail_lambda')):
            raise ValueError('The common-grid candidate changed the original physical representation')
        op = observed.create(paths['dense'], data['mesh'], data['a_stages'], float(data['radius']),
            data['fixed_core_first3'], batch_source=paths['batch'], observation_plan=plan,
            a_observations=carrier['a_observations'], M=M, N=N, width=float(data['width']),
            quarter=True, stage_block=a.stage_block)
    x, affine = op.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    prepared = op.prepare(x)
    common = CommonGridReadout(op, old_plan, old_carrier, carrier['refinement_parent_stage_map'],
        report['angular_refinement']['source_full_angles'], spectral)
    started = time.monotonic()
    for start in range(0, op.P, op.stage_block):
        stop = min(op.P, start+op.stage_block)
        if not np.any((common.mapping >= start) & (common.mapping < stop)):
            continue
        V, T = op._first_batch_uncached(prepared, start, stop)
        E = np.einsum('bni,bni->bn', V, V)
        Fg = np.einsum('bni,bni->bn', V, T)
        G = np.einsum('bni,bni->bn', T, T)
        common.update(E, Fg, G, prepared.rho, start, stop)
    value = dict(schema='same-fixed-g-solved-fine-field-common-parent-grid-v1',
        source_sha256=sha(__file__), bundle=file_record(a.bundle),
        refinement_report=file_record(a.refinement_report), affine=affine,
        common_parent_grid=common.report(), seconds=time.monotonic()-started,
        parent_field_evaluated_again=False, actual_fine_field_reread=True,
        continuous_metric_certified=False, fixed_metric_refinement_convergence_certified=False)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    write_json(a.out, value)
    announce(event='solved_fine_common_grid_returned', report=file_record(a.out),
             **value['common_parent_grid'])


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'read-common':
        common_main(sys.argv[2:])
    else:
        main()

