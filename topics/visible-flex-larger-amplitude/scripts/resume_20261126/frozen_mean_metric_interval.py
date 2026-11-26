#!/usr/bin/env python3
"""Continuous R684 fixed-finite-mean Gram certificate for canonical R671 fields.

The target is a frozen field's COMPLETE radial formula at its FIXED physical
angle rule.  It is never recomputed from the current field or interpolated
from stored observation values.  Every scientific call requires public Actions.
Raw interval returns and journals stay outside the repository.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


SCHEMA = 'R684-frozen-physical-mean-continuous-Gram-v1'
TASK_SCHEMA = 'R684-frozen-physical-mean-continuous-Gram-piece-v1'
KERNEL_SHA = 'fd4cd58045e16a969c8c1be48468ab4c1a7be929ef9b95e2a9a24ca546176b2d'
PROFILE_SHA = 'f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225'
README_TARGET = F(1, 1000000)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific calculation belongs in this public repository Actions')


def load_kernel(repo):
    path = Path(repo)/'topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_relative_gram_interval.py'
    if sha(path) != KERNEL_SHA:
        raise ValueError('Changed frozen R674 cancellation-preserving Gram source')
    name = '_fixed_mean_R674_'+KERNEL_SHA[:16]
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name], path


def identity(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.tmp-'+str(os.getpid()))
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2,
        allow_nan=False)+'\n')
    os.replace(temporary, path)


def outside(path, repo):
    path = Path(path).resolve()
    try:
        path.relative_to(Path(repo).resolve())
    except ValueError:
        return path
    raise ValueError('Raw journals and reports must stay outside the repository')


def positive_dyadic(value, name):
    value = int(value)
    if value < 1 or value & (value-1):
        raise ValueError(name+' must be a positive power of two')
    return value


def ranges(values):
    values = sorted(set(int(v) for v in values))
    if not values:
        return ''
    result, first, last = [], values[0], values[0]
    for value in values[1:]:
        if value == last+1:
            last = value
        else:
            result.append(str(first) if first == last else str(first)+'-'+str(last))
            first = last = value
    result.append(str(first) if first == last else str(first)+'-'+str(last))
    return ','.join(result)


def interval_sum(I, value):
    """Pairwise sum with one outward operation at EVERY addition."""
    lo, hi = np.asarray(value[0]), np.asarray(value[1])
    if lo.shape != hi.shape or lo.shape[-1] < 1:
        raise ValueError('Bad interval sum shape')
    while lo.shape[-1] > 1:
        count = lo.shape[-1]
        even = count-(count % 2)
        a, b = I.add((lo[..., :even:2], hi[..., :even:2]),
                     (lo[..., 1:even:2], hi[..., 1:even:2]))
        if even != count:
            a = np.concatenate((a, lo[..., -1:]), axis=-1)
            b = np.concatenate((b, hi[..., -1:]), axis=-1)
        lo, hi = a, b
    return lo[..., 0], hi[..., 0]


def hull(value):
    return np.asarray(value[0].min(axis=0)), np.asarray(value[1].max(axis=0))


def scalar_hull(value):
    return np.asarray(value[0].min()), np.asarray(value[1].max())


def scalar_add(reader, a, b):
    degree = max(len(a[0]), len(b[0]))-1
    return reader.I.add(reader.r.elevate(a, degree), reader.r.elevate(b, degree))


def endpoint_symbolic(point):
    return [str(v) for v in point]


class FrozenMeanGram:
    """Two independently validated fields and their exact common partition.

    target_arguments and current_arguments contain bundle, node_report,
    scalar_input and optional reference_carrier Paths.  frozen_identity is
    the externally fixed target manifest identity, not a current-field mean.
    """
    def __init__(self, *, repo, current_arguments, target_arguments,
                 frozen_angles, angles, scalar_degree=5, panels=128,
                 frozen_identity=None):
        require_actions()
        self.repo = Path(repo).resolve()
        self.kernel, self.kernel_path = load_kernel(self.repo)
        self.frozen_angles = positive_dyadic(frozen_angles, 'Frozen angle count')
        self.angles = positive_dyadic(angles, 'Certificate angle count')
        self.scalar_degree, self.panels = int(scalar_degree), int(panels)
        if not 3 <= self.scalar_degree <= 8 or self.panels < 1:
            raise ValueError('Use supported scalar Taylor degree and positive oracle panels')
        self.arguments = {}
        for role, supplied in (('current', current_arguments), ('target', target_arguments)):
            clean = {key: Path(value).resolve() for key, value in supplied.items()
                     if value is not None}
            if set(clean)-{'bundle','node_report','scalar_input','reference_carrier'}:
                raise ValueError('Unexpected field argument')
            if not {'bundle','node_report','scalar_input'} <= set(clean):
                raise ValueError('Each field needs its actual bundle, exact nodes and scalar definition')
            self.arguments[role] = clean
        if sha(self.arguments['current']['scalar_input']) != sha(self.arguments['target']['scalar_input']):
            raise ValueError('This fixed-g refinement preserves the common exact scalar definition')
        self.current = self.kernel.make_reader(repo=self.repo,
            **self.arguments['current'], angles=self.angles, radial_subdivisions=1,
            scalar_degree=self.scalar_degree, panels=self.panels)
        with np.load(self.arguments['target']['bundle'], allow_pickle=False) as data:
            frozen_M = (data['qjets'].shape[-1]-2)//3
        self.target_evaluation_angles = self.frozen_angles
        while self.target_evaluation_angles < 12*frozen_M:
            self.target_evaluation_angles *= 2
        self.target = self.kernel.make_reader(repo=self.repo,
            **self.arguments['target'], angles=self.target_evaluation_angles, radial_subdivisions=1,
            scalar_degree=self.scalar_degree, panels=self.panels)
        self.I = self.current.I
        self._validate_common_definition()
        self.frozen_identity = frozen_identity
        self.binding = dict(current_inputs={key: identity(value) for key, value in self.arguments['current'].items()},
            frozen_inputs={key: identity(value) for key, value in self.arguments['target'].items()},
            current_model_identity_sha256=self.current.profile.model_sha,
            frozen_model_identity_sha256=self.target.profile.model_sha,
            frozen_metric_identity=frozen_identity,
            frozen_averaging='physical', frozen_full_angles=self.frozen_angles,
            frozen_weights_exact='1/'+str(self.frozen_angles),
            target_evaluation_angles=self.target_evaluation_angles,
            current_M=self.current.r.M, frozen_M=self.target.r.M,
            current_J=self.current.r.J, frozen_J=self.target.r.J,
            common_scalar_input_sha256=sha(self.arguments['current']['scalar_input']),
            current_global_rho_lower=float(self.current.r.rho[0].min()),
            frozen_global_rho_lower=float(self.target.r.rho[0].min()),
            same_exact_f_lambda=True,
            common_lift_definition=dict(lambda_value=self.current.profile.model['lambda_value'],
                eta_start_symbolic=endpoint_symbolic(self.current.profile.eta_left),
                eta_end_symbolic=endpoint_symbolic(self.current.profile.eta_right),
                width_exact=str(self.current.r.width)))
        self.joint = self._intersection()

    def _validate_common_definition(self):
        a, b = self.current, self.target
        if (a.r.scalar_identity != b.r.scalar_identity or a.r.S_exact != b.r.S_exact
                or a.r.R_exact != b.r.R_exact or a.r.width != b.r.width
                or a.profile.lam != b.profile.lam or a.profile.eta_left != b.profile.eta_left
                or a.profile.eta_right != b.profile.eta_right
                or not np.array_equal(a.r.fixed_core, b.r.fixed_core)):
            raise ValueError('Refinement changed the exact common scalar/lift/design constants')
        for reader in (a, b):
            if not np.isfinite(reader.r.rho[0]).all() or np.any(reader.r.rho[0] <= 0):
                raise ValueError('Both complete material-angle maps need a positive continuous rho bound')
            if len(reader.r.fixed_core) != 3 or F(float(reader.r.R[0])) <= F(1, 5):
                raise ValueError('The fixed core and flat collar around all R661 cap graphs are unpaid')

    @staticmethod
    def _pieces(reader):
        result = []
        for cell in range(reader.r.J-1):
            for part, piece in enumerate(reader.profile.pieces(cell)):
                result.append((cell, part, piece))
        if not result or result[0][2][0] != (F(0), F(0)) or result[-1][2][1] != (F(1), F(0)):
            raise ValueError('Incomplete exact material interval')
        for left, right in zip(result, result[1:]):
            if left[2][1] != right[2][0]:
                raise ValueError('A source partition has a gap or overlap')
        return result

    def _intersection(self):
        a, b = self._pieces(self.current), self._pieces(self.target)
        cmp = self.current.profile.scalar.cmp
        i = j = 0
        result = []
        while i < len(a) and j < len(b):
            left = a[i][2][0] if cmp(a[i][2][0], b[j][2][0]) >= 0 else b[j][2][0]
            right = a[i][2][1] if cmp(a[i][2][1], b[j][2][1]) <= 0 else b[j][2][1]
            if cmp(left, right) >= 0:
                raise ValueError('Unexpected empty intersection of complete ordered partitions')
            result.append(dict(index=len(result), left=left, right=right,
                current_cell=a[i][0], current_part=a[i][1], current_piece=a[i][2],
                frozen_cell=b[j][0], frozen_part=b[j][1], frozen_piece=b[j][2]))
            order = cmp(a[i][2][1], b[j][2][1])
            if order <= 0:
                i += 1
            if order >= 0:
                j += 1
        if i != len(a) or j != len(b):
            raise ValueError('One exact partition ended before the other')
        return result

    @staticmethod
    def restrict_piece(reader, cell, piece, left, right):
        u0, u1 = reader.profile._parameters(cell, left, right)
        return left, right, u0, u1, piece[4], piece[5]

    @staticmethod
    def split_point(left, right, index, count):
        t = F(index, count)
        return tuple((1-t)*a+t*b for a, b in zip(left, right))

    @staticmethod
    def raw_without_common_squares(reader, cell, piece, p):
        """E-f_s^2, Fs.Fphi, |Fphi|^2-f^2*rho^2, BEFORE any hull.

        All triples retain every Fourier mode and the exact cos/sin(delta)
        analytic lift.  The rotating-frame connection is in raw_components.
        """
        I = reader.I
        U, T = reader.raw_components(cell, piece)
        if not p['detail'].get('reference_active') and not piece[4]:
            return [(reader.dot(U, U), None, None), (reader.dot(U, T), None, None),
                    (reader.dot(T, T), None, None)]
        c, d, f = [reader.scalar_poly(v) for v in (p['f'][1], p['z'][1], p['f'][0])]
        Pe = reader.add(reader.dot(U, U), reader.multiply(d, d))
        Pe = reader.add(Pe, I.scale(reader.multiply(d, U[2]), 2))
        Ce, Se = I.scale(reader.multiply(c, U[0]), 2), I.scale(reader.multiply(c, U[1]), 2)
        Pm = reader.add(reader.dot(U, T), reader.multiply(d, T[2]))
        fr = reader.multiply(f, reader.rho_poly)
        Cm = reader.add(reader.multiply(c, T[0]), reader.multiply(fr, U[1]))
        Sm = reader.sub(reader.multiply(c, T[1]), reader.multiply(fr, U[0]))
        Pg = reader.dot(T, T)
        Cg, Sg = I.scale(reader.multiply(fr, T[1]), 2), I.scale(reader.multiply(fr, T[0]), -2)
        return [(Pe, Ce, Se), (Pm, Cm, Sm), (Pg, Cg, Sg)]

    @staticmethod
    def point_values(reader, triple):
        P, C, S = triple
        if C is None:
            return reader.I.at(P, (slice(None), 0))
        degree = max(len(v[0]) for v in triple)-1
        P, C, S = [reader.r.elevate(v, degree) for v in triple]
        I = reader.I
        return I.add(I.at(P, (slice(None), 0)),
            I.add(I.mul(I.at(C, (slice(None), 0)), I.at(reader.cos_delta, 0)),
                  I.mul(I.at(S, (slice(None), 0)), I.at(reader.sin_delta, 0))))

    @staticmethod
    def field_fees(reader, p, E_hat, C_hat):
        """Physical Gram fees in (s,theta); rho cancels in delta F_theta."""
        I = reader.I
        if np.any(np.asarray(E_hat[1]) < 0) or np.any(np.asarray(C_hat[1]) < 0):
            raise ValueError('Negative upper endpoint for a squared physical norm')
        BV = I.sqrt(E_hat)[1]
        BW = I.sqrt(C_hat)[1]
        ev = I.sqrt(I.add(I.square(I.exact(p['f_error'][1])),
                         I.square(I.exact(p['z_error'][1]))))[1]
        ew = I.exact(p['f_error'][0])
        v, bv, bw = I.exact(ev), I.exact(BV), I.exact(BW)
        de = I.add(I.scale(I.mul(bv, v), 2), I.square(v))[1]
        dm = I.add(I.add(I.mul(bw, v), I.mul(bv, ew)), I.mul(v, ew))[1]
        dc = I.add(I.scale(I.mul(bw, ew), 2), I.square(ew))[1]
        return [de, dm, dc]

    def target_polynomials(self, cell, piece, p):
        """The fixed finite rule, with exact rho_* at its own original angles."""
        reader, I = self.target, self.I
        raw = self.raw_without_common_squares(reader, cell, piece, p)
        stride = self.target_evaluation_angles//self.frozen_angles
        if stride*self.frozen_angles != self.target_evaluation_angles:
            raise ValueError('Target evaluation grid must contain exactly the frozen angle nodes')
        select = slice(None, None, stride)
        E_residual_points = I.at(self.point_values(reader, raw[0]), (slice(None), select))
        rho_points = I.at(reader.rho_jets, (0, select))
        if np.any(rho_points[0] <= 0):
            raise ValueError('Frozen mean has a nonpositive material density')
        C_residual_points = I.div(I.at(self.point_values(reader, raw[2]),
            (slice(None), select)), I.square(rho_points))
        inverse_N = reader.r.fraction(F(1, self.frozen_angles))
        E_residual = I.mul(interval_sum(I, E_residual_points), inverse_N)
        C_residual = I.mul(interval_sum(I, C_residual_points), inverse_N)
        if not p['detail'].get('reference_active') and not piece[4]:
            cp2 = f2 = I.exact(np.asarray([0.]))
        else:
            cp2 = reader.profile.product(p['f'][1], p['f'][1])
            f2 = reader.profile.product(p['f'][0], p['f'][0])
        E = scalar_add(reader, cp2, E_residual)
        C = scalar_add(reader, f2, C_residual)
        # Pointwise norms at the target's FIXED finite angle set suffice for
        # its finite mean fee; no claim that these points cover all angles.
        def add_scalar(points, scalar):
            degree = max(len(points[0]), len(scalar[0]))-1
            points = reader.r.elevate(points, degree)
            scalar = reader.r.elevate(scalar, degree)
            return I.add(points, (scalar[0][:, None], scalar[1][:, None]))
        ep = add_scalar(E_residual_points, cp2)
        cp = add_scalar(C_residual_points, f2)
        fees = self.field_fees(reader, p, scalar_hull(ep), scalar_hull(cp))
        return dict(E=E, C=C, E_residual=E_residual, C_residual=C_residual,
                    E_fee=float(fees[0]), C_fee=float(fees[2]))

    def actual_entries(self, numerators, target_E, target_C, target_fees, p, rho):
        I = self.I
        et, ct = target_fees
        E = I.add(target_E, (-et, et))
        C = I.add(target_C, (-ct, ct))
        if np.any(E[0] <= 0) or np.any(C[0] <= 0) or np.any(rho[0] <= 0):
            raise ValueError('Positive frozen target and current material density are unpaid')
        E_hat = I.add(numerators[0], target_E)
        C_hat = I.add(I.div(numerators[2], I.square(rho)), target_C)
        fees = self.field_fees(self.current, p, E_hat, C_hat)
        e_fee = I.div(I.add(I.exact(fees[0]), I.exact(et)), E)[1]
        c_fee = I.div(I.add(I.exact(fees[2]), I.exact(ct)), C)[1]
        scale = I.sqrt(I.mul(E, C))
        m_fee = I.div(I.exact(fees[1]), scale)[1]
        entries = [I.add(I.div(numerators[0], E), (-e_fee, e_fee)),
            I.add(I.div(numerators[1], I.mul(rho, scale)), (-m_fee, m_fee)),
            I.add(I.div(numerators[2], I.mul(I.square(rho), C)), (-c_fee, c_fee))]
        return entries, E, C, [e_fee, m_fee, c_fee]

    def certify_piece(self, joint_index, radial_index=0, radial_subdivisions=1):
        require_actions()
        count = positive_dyadic(radial_subdivisions, 'Radial subdivision count')
        if not 0 <= int(joint_index) < len(self.joint) or not 0 <= int(radial_index) < count:
            raise ValueError('Requested exact joint piece is outside its complete partition')
        started = time.monotonic()
        row = self.joint[int(joint_index)]
        left, right = [self.split_point(row['left'], row['right'], k, count)
                       for k in (int(radial_index), int(radial_index)+1)]
        a, b, I = self.current, self.target, self.I
        ap = self.restrict_piece(a, row['current_cell'], row['current_piece'], left, right)
        bp = self.restrict_piece(b, row['frozen_cell'], row['frozen_piece'], left, right)
        p = a.profile.profile_controls(ap, include_target=False)
        star = b.profile.profile_controls(bp, include_target=False)
        frozen = self.target_polynomials(row['frozen_cell'], bp, star)
        triples = self.raw_without_common_squares(a, row['current_cell'], ap, p)
        Pe, Ce, Se = triples[0]
        Pg, Cg, Sg = triples[2]
        # The exact common f_s^2 and f^2 cancel IDENTICALLY.  The common
        # Taylor polynomial has the same exact center and scalar definition
        # on this common physical piece, irrespective of q mesh/frequency.
        Pe = a.sub(Pe, a.scalar_poly(frozen['E_residual']))
        Pg = a.sub(Pg, a.multiply(a.scalar_poly(frozen['C_residual']),
                                 a.multiply(a.rho_poly, a.rho_poly)))
        residual_triples = [(Pe, Ce, Se), triples[1], (Pg, Cg, Sg)]
        grids = [a.nonlinear_grid(triple) for triple in residual_triples]
        numerators, angular_fee, coefficient_width = [], 0., 0.
        for jets, fourth in grids:
            arc, _, remainder = a.angle_enclosure(jets, fourth)
            numerators.append(hull(arc))
            angular_fee = max(angular_fee, float(np.max(remainder)))
            width = I.sub(I.at(jets, (slice(None), 0)), I.at(jets, (slice(None), 0)))
            coefficient_width = max(coefficient_width, float(np.max(width[1])))
        target_E, target_C = scalar_hull(frozen['E']), scalar_hull(frozen['C'])
        target_fees = frozen['E_fee'], frozen['C_fee']
        entries, E, C, fees = self.actual_entries(numerators, target_E, target_C,
                                                target_fees, p, a.r.rho)
        norm = a.norm_interval(entries)
        upper = float(np.max(norm[1]))
        worst = int(np.argmax(norm[1]))
        lower, witness = 0., None
        rho_points = I.at(a.rho_jets, (0, a.r.angle_slice))
        for endpoint in (0, -1):
            point = [I.at(jets, (endpoint, 0, a.r.angle_slice)) for jets, _ in grids]
            actual, _, _, _ = self.actual_entries(point, I.at(frozen['E'], endpoint),
                I.at(frozen['C'], endpoint), target_fees, p, rho_points)
            point_lower = a.norm_interval(actual)[0]
            index = int(np.argmax(point_lower))
            if float(point_lower[index]) > lower:
                lower = float(point_lower[index])
                witness = dict(endpoint=endpoint, angle_grid_index=index)
        result = dict(joint_piece=int(joint_index), radial_subcell=int(radial_index),
            radial_subdivisions=count, current_cell=row['current_cell'], frozen_cell=row['frozen_cell'],
            symbolic_left=endpoint_symbolic(left), symbolic_right=endpoint_symbolic(right),
            continuous_relative_gram_operator_upper=upper, actual_supremum_lower=max(0., lower),
            maximum_component_absolute_upper=[float(I.absolute_upper(v).max()) for v in entries],
            minimum_frozen_E_lower=float(np.min(E[0])), minimum_frozen_C_lower=float(np.min(C[0])),
            frozen_mean_E_scalar_fee=frozen['E_fee'], frozen_mean_C_scalar_fee=frozen['C_fee'],
            physical_scalar_relative_fee_component_upper=[float(np.max(v)) for v in fees],
            nonlinear_angular_fourth_order_padding_upper=angular_fee,
            numerator_coefficient_interval_width_upper=coefficient_width,
            maximum_numerator_degree=max(len(value[0])-1 for triple in residual_triples
                                         for value in triple if value is not None),
            worst_angle_grid_index=worst, actual_lower_witness=witness,
            current_scalar_profile=p['detail'], frozen_scalar_profile=star['detail'],
            complete_piece_and_full_angle_cover=True, original_full_spectrum_preserved=True,
            untruncated_nonlinear_angular_lift=True, both_physical_scalar_remainders_paid=True,
            exact_common_lift_squares_cancelled=True, frozen_target_recomputed_from_current=False,
            frozen_finite_rule_changed=False, strict_under_stated_IEEE_arithmetic=True,
            seconds=time.monotonic()-started)
        if not math.isfinite(upper) or not 0 <= result['actual_supremum_lower'] <= upper:
            raise ValueError('Invalid actual interval return')
        return result


def read_manifest(path, repo):
    """Independently verify the shared numeric producer's exact target ID."""
    manifest = json.loads(Path(path).read_text())
    if (manifest.get('schema') != 'R684-frozen-rotational-mean-metric-v1'
            or manifest.get('frozen') is not True or manifest.get('averaging') != 'physical'):
        raise ValueError('This continuous consumer needs one frozen physical finite-mean target')
    input_roles = {'bundle','node_report','scalar_input','observation_carrier','reference_carrier'}
    source_roles = {'evaluator','factory','operator','observed','batch','scalar','integer','hold'}
    if set(manifest['inputs']) != input_roles or set(manifest['sources']) != source_roles:
        raise ValueError('The complete frozen target input/source identities are mandatory')
    count = manifest['full_angles']
    if isinstance(count, bool) or not isinstance(count, int) or count < 4:
        raise ValueError('Invalid fixed full angle count')
    positive_dyadic(count, 'Frozen finite rule angle count')
    definition = dict(angle_formula='phi_j=2*pi*j/N_star, j=0,...,N_star-1',
        diagonal_components=['|F_star,s|^2','|F_star,phi|^2/rho_star^2'],
        off_diagonal='zero by exact full-circle reflection parity',
        average_formula='sum_j component_j/N_star',
        radial_rule='Frozen canonical shared quintic on exact symbolic nodes plus its analytic R671 f/h/k, evaluated at every s; no interpolated mean array')
    cap = dict(schema='R661-fixed-p4-graphs-v1', a='3/20',
        radii=['1/25','9/200','1/20','11/200'], height='1/1000',
        upper_centers_xy=[['3/20','0'],['0','3/20'],['-3/20','0']],
        lower_centers_xy=[['0','0']],
        graph='h*(1-|x-c_xy|^2/b^2)_+^4 along each cap outward normal',
        metric_rule='own induced graph metric; height translation independent')
    if manifest['mean_definition'] != definition or manifest['cap_recipe'] != cap:
        raise ValueError('The fixed finite rule or fixed induced cap metric changed')
    model_hash = canonical_sha(manifest['canonical_model'])
    if model_hash != manifest['canonical_model_identity_sha256']:
        raise ValueError('Frozen canonical model hash mismatch')
    payload = dict(schema=manifest['schema'], averaging=manifest['averaging'],
        full_angles=count, canonical_model_identity_sha256=model_hash,
        inputs={role: record['sha256'] for role, record in manifest['inputs'].items()},
        sources={role: record['sha256'] for role, record in manifest['sources'].items()},
        domain=manifest['domain'], cap_recipe=cap, mean_definition=definition)
    target_id = canonical_sha(payload)
    if target_id != manifest['target_identity_sha256']:
        raise ValueError('The full frozen target mathematical identity changed')
    resolved = {}
    for kind in ('inputs', 'sources'):
        resolved[kind] = {}
        for role, record in manifest[kind].items():
            if kind == 'sources' and 'repo_relative_path' in record:
                candidate = (Path(repo).resolve()/record['repo_relative_path']).resolve()
            else:
                candidate = Path(record['path']).resolve()
            if sha(candidate) != record['sha256']:
                raise ValueError('Changed frozen '+kind+'/'+role+': '+str(candidate))
            resolved[kind][role] = candidate
    model = manifest['canonical_model']
    expected_sources = dict(factory=model['source_sha256'],
        operator=model['operator_source_sha256s']['dense'],
        batch=model['operator_source_sha256s']['batch'],
        observed=model['operator_source_sha256s']['observed'],
        scalar=model['source_sha256s']['scalar_source'],
        integer=model['source_sha256s']['integer_source'], hold=model['source_sha256s']['hold_source'])
    for role, wanted in expected_sources.items():
        if manifest['sources'][role]['sha256'] != wanted:
            raise ValueError('Frozen source is not its canonical physical-field source: '+role)
    return ({role: resolved['inputs'][role] for role in ('bundle','node_report','scalar_input','reference_carrier')},
            count, target_id, cap, manifest)


def validate_manifest_field(manifest, reader):
    target = reader.target
    if (manifest['canonical_model'] != target.profile.model
            or manifest['canonical_model_identity_sha256'] != target.profile.model_sha):
        raise ValueError('Actually loaded target field is not the frozen canonical field')
    domain = dict(S_carrier_hex=float(target.r.mesh[-1]).hex(),
        R_carrier_hex=float(target.r.radius_carrier).hex(), width_hex=float(target.r.width).hex(),
        fixed_core_first3_hex=[float(v).hex() for v in target.r.fixed_core],
        eta_left_affine=endpoint_symbolic(target.profile.eta_left),
        eta_right_affine=endpoint_symbolic(target.profile.eta_right),
        scalar_rule='original FullHold S/R from the bound scalar_input, scalar, integer and hold sources')
    if manifest['domain'] != domain:
        raise ValueError('Frozen exact domain or design constants disagree with the actual field')


def validate_return(row, task, reader, radial):
    joint, sub = task
    piece = reader.joint[joint]
    left, right = [reader.split_point(piece['left'], piece['right'], k, radial)
                   for k in (sub, sub+1)]
    if ((row.get('joint_piece'), row.get('radial_subcell')) != task
            or row.get('radial_subdivisions') != radial
            or row.get('current_cell') != piece['current_cell']
            or row.get('frozen_cell') != piece['frozen_cell']
            or row.get('symbolic_left') != endpoint_symbolic(left)
            or row.get('symbolic_right') != endpoint_symbolic(right)):
        raise ValueError('Same-run interval record refers to another exact physical piece')
    for flag in ('complete_piece_and_full_angle_cover','original_full_spectrum_preserved',
                 'untruncated_nonlinear_angular_lift','both_physical_scalar_remainders_paid',
                 'exact_common_lift_squares_cancelled','strict_under_stated_IEEE_arithmetic'):
        if row.get(flag) is not True:
            raise ValueError('Missing interval scope declaration: '+flag)
    upper = row['continuous_relative_gram_operator_upper']
    lower = row['actual_supremum_lower']
    positive = [row['minimum_frozen_E_lower'], row['minimum_frozen_C_lower']]
    if (not all(math.isfinite(v) for v in [upper, lower, *positive])
            or not 0 <= lower <= upper or min(positive) <= 0):
        raise ValueError('Invalid finite interval return or unpaid target positivity')


def main():
    require_actions()
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo','bundle','node-report','scalar-input','frozen-metric','journal','out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--reference-carrier', type=Path)
    parser.add_argument('--angles', type=int, default=4096)
    parser.add_argument('--radial-subdivisions', type=int, default=1)
    parser.add_argument('--scalar-degree', type=int, default=5)
    parser.add_argument('--panels', type=int, default=128)
    parser.add_argument('--budget-seconds', type=float, default=600.)
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    if not math.isfinite(args.budget_seconds) or args.budget_seconds <= 0:
        raise ValueError('Use a positive finite admission budget')
    args.radial_subdivisions = positive_dyadic(args.radial_subdivisions, 'Radial subdivision count')
    args.journal = outside(args.journal, args.repo)
    args.out = outside(args.out, args.repo)
    if args.out.exists():
        raise FileExistsError('Preserve earlier actual outputs')
    if args.journal.exists() != args.resume:
        raise ValueError('Use a fresh journal, or explicit --resume of an existing journal')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    started = time.monotonic()
    target_arguments, frozen_angles, frozen_identity, cap_rule, manifest = read_manifest(args.frozen_metric, args.repo)
    current_arguments = dict(bundle=args.bundle, node_report=args.node_report,
        scalar_input=args.scalar_input, reference_carrier=args.reference_carrier)
    reader = FrozenMeanGram(repo=args.repo, current_arguments=current_arguments,
        target_arguments=target_arguments, frozen_angles=frozen_angles,
        angles=args.angles, scalar_degree=args.scalar_degree, panels=args.panels,
        frozen_identity=frozen_identity)
    validate_manifest_field(manifest, reader)
    execution = {key: os.environ.get(key) for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID',
        'GITHUB_RUN_ATTEMPT','GITHUB_WORKFLOW','GITHUB_SHA')}
    execution['actual_source_commit'] = subprocess.check_output(
        ['git','-C',str(args.repo),'rev-parse','HEAD'], text=True).strip()
    signature = dict(schema=SCHEMA, producer_sha256=sha(__file__),
        kernel_sha256=KERNEL_SHA, binding=reader.binding, angles=args.angles,
        radial_subdivisions=args.radial_subdivisions, scalar_degree=args.scalar_degree,
        panels=args.panels, frozen_manifest_sha256=sha(args.frozen_metric), cap_metric_rule=cap_rule,
        runner_identity={key: execution[key] for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT')})
    binding_sha = canonical_sha(signature)
    header = args.journal/'definition.json'
    if args.resume:
        if json.loads(header.read_text()) != signature:
            raise ValueError('Journal belongs to another producer, field, metric, rule, resolution or Actions run')
    else:
        args.journal.mkdir(parents=True)
        atomic_json(header, signature)
    tasks = [(piece['index'], sub) for piece in reader.joint
             for sub in range(args.radial_subdivisions)]
    task_set = set(tasks)
    returns, failures = {}, {}
    for path in sorted(args.journal.glob('piece-*.json')):
        value = json.loads(path.read_text())
        task = tuple(value.get('task', []))
        if (value.get('schema') != TASK_SCHEMA or value.get('binding_sha256') != binding_sha
                or task not in task_set or task in returns or task in failures):
            raise ValueError('Invalid or duplicate same-run interval return')
        if value.get('state') == 'returned':
            row = value['record']
            validate_return(row, task, reader, args.radial_subdivisions)
            returns[task] = row
        elif value.get('state') == 'failed':
            failures[task] = value
        else:
            raise ValueError('Unknown journal record state')

    def summary(status, admitted):
        covered, paid = [], []
        cell_rows = {}
        required = {cell: [] for cell in range(reader.current.r.J-1)}
        for joint, sub in tasks:
            required[reader.joint[joint]['current_cell']].append((joint, sub))
        for cell, cell_tasks in required.items():
            if all(task in returns for task in cell_tasks):
                rows = [returns[task] for task in cell_tasks]
                upper = max(row['continuous_relative_gram_operator_upper'] for row in rows)
                cell_rows[cell] = dict(upper=upper,
                    lower=max(row['actual_supremum_lower'] for row in rows),
                    E_lower=min(row['minimum_frozen_E_lower'] for row in rows),
                    C_lower=min(row['minimum_frozen_C_lower'] for row in rows))
                covered.append(cell)
                if F(upper) <= README_TARGET:
                    paid.append(cell)
        complete = len(covered) == reader.current.r.J-1
        upper = max((row['upper'] for row in cell_rows.values()), default=None)
        lower = max((row['actual_supremum_lower'] for row in returns.values()), default=None)
        witness = (max(returns.values(), key=lambda row: row['actual_supremum_lower'])
                   if returns else None)
        compact_witness = (None if witness is None else {key: witness[key] for key in
            ('current_cell','frozen_cell','joint_piece','radial_subcell','radial_subdivisions',
             'symbolic_left','symbolic_right','actual_supremum_lower','actual_lower_witness')})
        metric = bool(complete and F(upper) <= README_TARGET)
        output = dict(schema=SCHEMA, source_sha256=sha(__file__),
            kernel_source_sha256=KERNEL_SHA, reference_interval_source_sha256=PROFILE_SHA,
            execution=execution, binding=reader.binding, binding_sha256=binding_sha,
            current_bundle_sha256=reader.binding['current_inputs']['bundle']['sha256'],
            current_node_report_sha256=reader.binding['current_inputs']['node_report']['sha256'],
            frozen_bundle_sha256=reader.binding['frozen_inputs']['bundle']['sha256'],
            frozen_metric_identity_sha256=frozen_identity,
            field_binding_json=json.dumps(reader.binding, sort_keys=True, separators=(',', ':'), allow_nan=False),
            frozen_manifest=identity(args.frozen_metric), cap_metric_rule=cap_rule,
            angles=args.angles, radial_subdivisions=args.radial_subdivisions,
            scalar_degree=args.scalar_degree, panels=args.panels,
            expected_current_cells=reader.current.r.J-1, exact_joint_pieces=len(reader.joint),
            expected_piece_tasks=len(tasks), returned_piece_tasks=len(returns), failed_piece_tasks=len(failures),
            admitted_piece_tasks_this_invocation=admitted, status=status,
            covered_cells_ranges=ranges(covered), target_paid_cells_ranges=ranges(paid),
            covered_cells_count=len(covered), target_paid_cells_count=len(paid),
            covered_relative_gram_operator_upper=upper,
            covered_relative_gram_operator_upper_exact=None if upper is None else str(F(upper)),
            complete_relative_gram_operator_upper=upper if complete else None,
            complete_relative_gram_operator_upper_exact=str(F(upper)) if complete else None,
            covered_actual_supremum_lower=lower, complete_scope=complete,
            returned_point_supremum_lower_exact=None if lower is None else str(F(lower)),
            returned_point_supremum_lower_scope='A global supremum lower bound from all returned exact point witnesses, including pieces of cells whose other pieces remain unpaid',
            actual_lower_witness_json=json.dumps(compact_witness, sort_keys=True, separators=(',', ':'), allow_nan=False),
            README_target_exact=str(README_TARGET), metric_certified=metric,
            target_paid_uniform_upper_exact=str(README_TARGET) if paid else None,
            all_t_metric_certified=metric,
            minimum_covered_frozen_E_lower=min((r['E_lower'] for r in cell_rows.values()), default=None),
            minimum_covered_frozen_C_lower=min((r['C_lower'] for r in cell_rows.values()), default=None),
            actual_candidate_proved_above_target=bool(lower is not None and F(lower) > README_TARGET),
            worst_upper_cells=sorted((dict(cell=cell, **row) for cell, row in cell_rows.items()),
                key=lambda item: item['upper'], reverse=True)[:8],
            failure_types=sorted(set(value['error_type'] for value in failures.values())),
            target_finite_rule_is_exact_definition=True,
            target_Haar_integral_claimed=False, target_inferred_from_current_field=False,
            exact_common_lift_squares_cancelled=True, scalar_and_angular_remainders_paid=True,
            caps_relative_error_exact='0', reflection_preserves_relative_gram=True,
            phase_scope='R248 conjugacy for the same frozen rotational target and fixed caps',
            embedding_certified=False, reach_certified=False, fixed_metric_convergence_certified=False,
            topic_completion_certified=False,
            journal_policy='Actual piece returns stay runner-local; publish only source, identities and compact domain statements',
            seconds=time.monotonic()-started,
            process_peak_rss_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        atomic_json(args.out, output)
        return output

    admitted = 0
    summary('ready', admitted)
    for task in tasks:
        if task in returns or task in failures:
            continue
        if admitted and time.monotonic()-started >= args.budget_seconds:
            break
        begin = time.monotonic()
        record = dict(schema=TASK_SCHEMA, binding_sha256=binding_sha, task=list(task))
        try:
            row = reader.certify_piece(*task, radial_subdivisions=args.radial_subdivisions)
            validate_return(row, task, reader, args.radial_subdivisions)
            record.update(state='returned', record=row)
            returns[task] = row
        except Exception as error:
            record.update(state='failed', error_type=type(error).__name__, error=str(error),
                          mathematical_contribution='No bound on this task')
            failures[task] = record
        record['call_seconds'] = time.monotonic()-begin
        path = args.journal/('piece-'+str(task[0]).zfill(6)+'-'+str(task[1]).zfill(6)+'.json')
        if path.exists():
            raise FileExistsError('Do not overwrite an actual piece return')
        atomic_json(path, record)
        admitted += 1
        output = summary('running', admitted)
        print(json.dumps(dict(event='frozen_mean_Gram_piece_return', task=list(task),
            state=record['state'], seconds=record['call_seconds'],
            covered_cells=output['covered_cells_count'], complete_scope=output['complete_scope'],
            metric_certified=output['metric_certified'])), flush=True)
        if record.get('error_type') == 'MemoryError':
            break
    status = ('complete_cover' if len(returns) == len(tasks)
              else 'returned_plan_with_failed_pieces' if len(returns)+len(failures) == len(tasks)
              else 'admission_budget_checkpoint')
    output = summary(status, admitted)
    print(json.dumps(dict(event='frozen_mean_Gram_checkpoint', report_sha256=sha(args.out),
        frozen_metric_identity=frozen_identity, status=status, complete_scope=output['complete_scope'],
        upper=output['complete_relative_gram_operator_upper'], lower=output['covered_actual_supremum_lower'],
        metric_certified=output['metric_certified'], seconds=output['seconds'])), flush=True)


if __name__ == '__main__':
    main()
