#!/usr/bin/env python3
"""Exact common-beta postprocessing for already enclosed physical fields.

This program consumes complete SAME-FIELD outward boxes and bound evidence.
It does not evaluate F, six jets, normal roots, quadrature, curvature, or a
diameter.  It checks exact rectangular coverage and rational inequalities.
All such scientific consumption is restricted to the public Actions runner.

The full angular circle is the default.  A proper fundamental domain requires
an additional source-bound mathematical extension certificate.  Its truth,
and the truth of every external enclosure/proof, are NOT established merely
by parsing a declaration or matching a digest.  The output keeps that scope
separate from the algebra checked here.  It is not a solver admission gate.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import time


INPUT_SCHEMA = 'complete-same-field-positive-support-input-v1'
FIELD_SCHEMA = 'complete-physical-field-support-binding-v1'
COVER_SCHEMA = 'exact-affine-physical-patch-rectangle-cover-v1'
CHUNK_SCHEMA = 'same-field-outward-support-box-chunk-v1'
EVIDENCE_SCHEMA = 'same-field-complete-bound-evidence-v1'
OUTPUT_SCHEMA = 'complete-common-positive-support-parameter-result-v1'
REPOSITORY = 'Rogerhu12/math-research-public'
NORMAL_CONVENTION = 'F_phi cross F_s, accurately outward'
CAP_RECIPE = dict(
    schema='R661-fixed-p4-outward-cap-graphs-v1',
    height='1/1000', centre_scale='3/20',
    radii=['1/25', '9/200', '1/20', '11/200'],
    upper_centres=[['3/20', '0'], ['0', '3/20'], ['-3/20', '0']],
    lower_centres=[['0', '0']],
    graph='height*(1-distance_squared/radius_squared)^4 inside each disk; zero outside',
    height_directions=['outward upper', 'outward lower'],
    metric='own induced graph metric; physical cap height fixed along phase')
CAP_GRADIENT = Fraction(1, 20)
CAP_SUPPORT_RADIUS = Fraction(1, 5)
CAP_G = Fraction(1, 100)
CAP_DENOMINATOR = Fraction(801, 800)
CAP_K = Fraction(5)
REACH_RATIO = Fraction(3, 100)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != REPOSITORY):
        raise RuntimeError('Scientific support-box consumption requires public repository Actions')


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode('utf-8')).hexdigest()


def digest(value):
    return (isinstance(value, str) and len(value) == 64
        and all(c in '0123456789abcdef' for c in value))


def qtext(value):
    return str(value.numerator) if value.denominator == 1 else str(value)


def rational(value, name):
    if not isinstance(value, str):
        raise ValueError(name + ' must be an exact canonical rational string, not a float')
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(name + ' is not a rational string') from error
    if qtext(result) != value:
        raise ValueError(name + ' must use canonical n or n/d notation')
    return result


def exact_integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(name + ' must be an actual integer at least ' + str(minimum))
    return value


def record_path(record, root):
    if (not isinstance(record, dict) or not isinstance(record.get('path'), str)
            or not record['path'] or not digest(record.get('sha256'))):
        raise ValueError('Every file must have an explicit path and complete SHA256')
    exact_integer(record.get('bytes'), 'file byte count')
    path = Path(record['path'])
    return (path if path.is_absolute() else root / path).resolve()


def bind_used_record(used, record):
    path = record['path']
    previous = used.get(path)
    if previous is not None and previous != record:
        raise ValueError('A previously bound complete path cannot acquire different bytes or SHA256: ' + path)
    if previous is None:
        used[path] = dict(record)


def verified_bytes(record, root, role, used):
    path = record_path(record, root)
    raw = path.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if len(raw) != record['bytes'] or actual != record['sha256']:
        raise ValueError('Actual full bytes differ for ' + role)
    bind_used_record(used, dict(path=str(path), sha256=actual, bytes=len(raw)))
    return raw


def verified_json(record, root, role, used):
    return json.loads(verified_bytes(record, root, role, used))


def nonempty_text(value, name):
    if not isinstance(value, str) or not value:
        raise ValueError(name + ' must be a nonempty string')
    return value


def validate_execution(value):
    if (not isinstance(value, dict) or value.get('platform') != 'GitHub Actions'
            or value.get('repository') != REPOSITORY
            or not isinstance(value.get('run_id'), str)
            or not value['run_id'].isdigit()
            or not isinstance(value.get('source_commit'), str)
            or len(value['source_commit']) != 40
            or any(c not in '0123456789abcdef' for c in value['source_commit'])):
        raise ValueError('Keep actual public-run provenance; a pending run is not evidence')
    exact_integer(value.get('attempt'), 'actual run attempt', 1)


class RationalInterval:
    """An exact possibly open interval, with one source for each tight end."""
    def __init__(self, low, high, low_open, high_open, name):
        self.low, self.high = low, high
        self.low_open, self.high_open = low_open, high_open
        self.low_reason = self.high_reason = 'domain:' + name
        self.empty_reason = None
        self.counts = dict(total=0, positive=0, negative=0, zero=0)
        self._check()

    def _check(self):
        if (self.empty_reason is None and self.high is not None
                and (self.low > self.high or (self.low == self.high
                    and (self.low_open or self.high_open)))):
            self.empty_reason = dict(kind='incompatible_interval_bounds',
                lower_reason=self.low_reason, upper_reason=self.high_reason)

    def impose(self, coefficient, rhs, strict, reason):
        self.counts['total'] += 1
        sign = 'positive' if coefficient > 0 else 'negative' if coefficient < 0 else 'zero'
        self.counts[sign] += 1
        if self.empty_reason is not None:
            return
        if coefficient == 0:
            if (rhs >= 0 if strict else rhs > 0):
                self.empty_reason = dict(kind='zero_coefficient_contradiction',
                    reason=reason, rhs=qtext(rhs), strict=strict)
            return
        endpoint = rhs / coefficient
        if coefficient > 0:
            if endpoint > self.low:
                self.low, self.low_open, self.low_reason = endpoint, strict, reason
            elif endpoint == self.low and strict:
                self.low_open, self.low_reason = True, reason
        else:
            if self.high is None or endpoint < self.high:
                self.high, self.high_open, self.high_reason = endpoint, strict, reason
            elif endpoint == self.high and strict:
                self.high_open, self.high_reason = True, reason
        self._check()

    def contains(self, value):
        return (self.empty_reason is None
            and (value > self.low or (value == self.low and not self.low_open))
            and (self.high is None or value < self.high
                 or (value == self.high and not self.high_open)))

    def choose(self):
        if self.empty_reason is not None:
            return None
        if self.contains(Fraction(1)):
            return Fraction(1)
        if self.high is None:
            result = self.low + 1
        elif self.low == self.high:
            result = self.low
        else:
            result = (self.low + self.high) / 2
        if result <= 0 or not self.contains(result):
            raise ArithmeticError('The exact interval selector did not return a positive member')
        return result

    def metadata(self):
        return dict(empty=self.empty_reason is not None,
            lower=qtext(self.low), upper=None if self.high is None else qtext(self.high),
            lower_open=self.low_open, upper_open=self.high_open,
            lower_reason=self.low_reason, upper_reason=self.high_reason,
            empty_reason=self.empty_reason, coefficient_counts=dict(self.counts))


class CoverageMinimum:
    """Range-add minimum over exact angular elementary intervals."""
    def __init__(self, size):
        self.size = size
        self.minimum = [0] * (4 * size + 4)
        self.lazy = [0] * (4 * size + 4)

    def add(self, left, right, amount, node=1, lo=0, hi=None):
        if hi is None:
            hi = self.size
        if right <= lo or hi <= left:
            return
        if left <= lo and hi <= right:
            self.minimum[node] += amount
            self.lazy[node] += amount
            return
        mid = (lo + hi) // 2
        self.add(left, right, amount, 2 * node, lo, mid)
        self.add(left, right, amount, 2 * node + 1, mid, hi)
        self.minimum[node] = self.lazy[node] + min(
            self.minimum[2 * node], self.minimum[2 * node + 1])

    def first_uncovered(self, node=1, lo=0, hi=None, above=0):
        if hi is None:
            hi = self.size
        if above + self.minimum[node] >= 1:
            return None
        if hi - lo == 1:
            return lo
        above += self.lazy[node]
        mid = (lo + hi) // 2
        answer = self.first_uncovered(2 * node, lo, mid, above)
        return answer if answer is not None else self.first_uncovered(
            2 * node + 1, mid, hi, above)


def complete_rectangle_cover(rectangles, angle_low, angle_high):
    """Cover every closed [0,1] x angular interval; overlaps are allowed."""
    if not rectangles:
        return dict(complete=False, missing=dict(u=['0', '1'],
            phi_over_pi=[qtext(angle_low), qtext(angle_high)]), strips_checked=0)
    endpoints = {angle_low, angle_high}
    events = defaultdict(list)
    events[Fraction(0)]
    events[Fraction(1)]
    for u0, u1, p0, p1 in rectangles:
        endpoints.update((p0, p1))
        events[u0].append((p0, p1, 1))
        events[u1].append((p0, p1, -1))
    endpoints = sorted(endpoints)
    indices = {value:index for index,value in enumerate(endpoints)}
    tree = CoverageMinimum(len(endpoints) - 1)
    previous = Fraction(0)
    strips = 0
    for current in sorted(events):
        if current > previous:
            strips += 1
            missing = tree.first_uncovered()
            if missing is not None:
                return dict(complete=False, missing=dict(
                    u=[qtext(previous), qtext(current)],
                    phi_over_pi=[qtext(endpoints[missing]), qtext(endpoints[missing+1])]),
                    strips_checked=strips)
        for p0, p1, amount in events[current]:
            tree.add(indices[p0], indices[p1], amount)
        if tree.minimum[1] < 0:
            raise ArithmeticError('Rectangle sweep produced a negative coverage count')
        previous = current
    if previous != 1:
        raise ArithmeticError('The complete radial unit interval was not traversed')
    return dict(complete=True, missing=None, strips_checked=strips)


def affine(value, name):
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError(name + ' must be [coefficient_of_exact_S, constant]')
    return (rational(value[0], name + ':S'), rational(value[1], name + ':constant'))


def affine_lower(value, S_low, S_high):
    coefficient, constant = value
    return constant + coefficient * (S_low if coefficient >= 0 else S_high)


def validate_cover(cover, field):
    definition = cover.get('definition')
    if (not isinstance(definition, dict) or definition.get('schema') != COVER_SCHEMA
            or cover.get('identity_sha256') != canonical(definition)
            or definition.get('field_identity_sha256') != field['identity_sha256']
            or definition.get('box_boundary_convention') != 'all rectangles closed'
            or definition.get('normal_convention') != NORMAL_CONVENTION):
        raise ValueError('Keep one canonical same-field accurate cover and outward normal')
    S_box = definition.get('exact_S_enclosure')
    if not isinstance(S_box, list) or len(S_box) != 2:
        raise ValueError('Retain the accurate symbolic S enclosure, not a floating mesh length')
    S_low, S_high = [rational(v, 'exact S bound') for v in S_box]
    if not 0 < S_low <= S_high:
        raise ValueError('The exact S enclosure must be ordered and strictly positive')
    patches = definition.get('patches')
    if not isinstance(patches, list) or not patches:
        raise ValueError('The complete original physical patch list cannot be empty')
    prepared = {}
    reduction_claims = {}
    minimum_width = None
    for patch in patches:
        name = nonempty_text(patch.get('id'), 'physical patch id')
        if name in prepared:
            raise ValueError('Original physical patch identifiers must be unique')
        nodes = patch.get('mesh_affine')
        if not isinstance(nodes, list) or len(nodes) < 2:
            raise ValueError('Every complete patch retains its full accurate affine mesh')
        mesh = [affine(v, 'physical mesh node') for v in nodes]
        interval = patch.get('exact_parameter_interval_affine')
        if (not isinstance(interval, list) or len(interval) != 2
                or affine(interval[0], 'patch left') != mesh[0]
                or affine(interval[1], 'patch right') != mesh[-1]):
            raise ValueError('Actual patch endpoints must equal the complete affine mesh endpoints')
        for left, right in zip(mesh, mesh[1:]):
            width = affine_lower((right[0]-left[0], right[1]-left[1]), S_low, S_high)
            minimum_width = width if minimum_width is None else min(minimum_width, width)
        mode = patch.get('angular_mode', 'full-circle')
        limits = patch.get('phi_over_pi_interval', ['0', '2'])
        if not isinstance(limits, list) or len(limits) != 2:
            raise ValueError('The exact angular interval must retain both endpoints')
        p0, p1 = [rational(v, 'phi/pi endpoint') for v in limits]
        if not 0 <= p0 < p1 <= 2:
            raise ValueError('The physical angular interval lies inside the complete [0,2] circle')
        if mode == 'full-circle':
            if [p0, p1] != [Fraction(0), Fraction(2)]:
                raise ValueError('A full-circle declaration cannot silently mean a quarter grid')
            if patch.get('angular_extension_evidence_role') is not None:
                raise ValueError('Full-circle and fundamental-domain contracts stay explicit')
        elif mode == 'proved-fundamental-domain':
            role = nonempty_text(patch.get('angular_extension_evidence_role'),
                'same-field angular extension evidence role')
            if role in reduction_claims:
                raise ValueError('Each reduced patch needs its own complete bound extension statement')
            reduction_claims[role] = dict(kind='complete-angular-extension-and-C2-seams',
                patch=name, base_phi_over_pi=[qtext(p0), qtext(p1)],
                destination_phi_over_pi=['0', '2'],
                extension_preserves_outward_support_for_every_positive_beta=True,
                complete_extension_uses_compatible_C2_parameter_diffeomorphisms=True,
                outward_unit_normals_transform_by_origin_fixed_orthogonal_maps_commuting_with_A_beta=True,
                all_angle_and_reflection_seams_C2=True,
                coverage_identity_sha256=cover['identity_sha256'])
        else:
            raise ValueError('Unsupported angular domain; no extension is inferred from carrier nodes')
        radial_mode = patch.get('radial_mode', 'complete-physical-patch')
        if radial_mode == 'proved-radial-fundamental-domain':
            role = nonempty_text(patch.get('radial_extension_evidence_role'),
                'same-field radial extension evidence role')
            if role in reduction_claims:
                raise ValueError('Every radial/angle reduction has a distinct complete statement')
            reduction_claims[role] = dict(kind='complete-radial-extension-and-C2-seams',
                patch=name, coverage_identity_sha256=cover['identity_sha256'],
                all_omitted_original_pieces_and_accurate_tail_accounted_for=True,
                extension_preserves_outward_support_for_every_positive_beta=True,
                complete_extension_uses_compatible_C2_parameter_diffeomorphisms=True,
                outward_unit_normals_transform_by_origin_fixed_orthogonal_maps_commuting_with_A_beta=True,
                all_reflection_core_cap_and_tail_seams_C2=True)
        elif radial_mode != 'complete-physical-patch':
            raise ValueError('Unsupported physical radial domain reduction')
        elif patch.get('radial_extension_evidence_role') is not None:
            raise ValueError('A complete patch does not silently invoke a separate reduced domain')
        prepared[name] = dict(cells=len(mesh)-1, angle_low=p0, angle_high=p1,
            angular_mode=mode, radial_mode=radial_mode)
    return prepared, reduction_claims, minimum_width


def validate_evidence(role, item, expected_claim, field, sources, root, used):
    if not isinstance(item, dict):
        raise ValueError('Missing complete bound evidence for ' + role)
    source_role = nonempty_text(item.get('producer_source_role'), 'evidence producer source role')
    if source_role not in sources:
        raise ValueError('The complete evidence producer source must be byte-bound')
    proof_sources = item.get('proof_sources')
    if not isinstance(proof_sources, list) or not proof_sources:
        raise ValueError('The complete mathematical proof source cannot be replaced by a Boolean')
    proofs = []
    for index, record in enumerate(proof_sources):
        verified_bytes(record, root, role + ':proof:' + str(index), used)
        proofs.append(dict(sha256=record['sha256'], bytes=record['bytes']))
    body = verified_json(item.get('certificate'), root, role + ':certificate', used)
    if (not isinstance(body, dict) or body.get('schema') != EVIDENCE_SCHEMA
            or body.get('role') != role
            or body.get('field_identity_sha256') != field['identity_sha256']
            or body.get('producer_source_sha256') != sources[source_role]['sha256']
            or body.get('claim') != expected_claim
            or body.get('proof_sources') != proofs
            or body.get('complete') is not True
            or type(body.get('remaining_responsibilities')) is not int
            or body['remaining_responsibilities'] != 0):
        raise ValueError('An external complete evidence record changed field, source, proof or scope: ' + role)
    validate_execution(body.get('execution'))
    return dict(certificate_sha256=item['certificate']['sha256'],
        certificate_bytes=item['certificate']['bytes'],
        producer_source_sha256=body['producer_source_sha256'],
        proof_sources=proofs, execution=body['execution'],
        statement=expected_claim,
        complete_bytes_and_same_field_binding_checked_here=True,
        mathematical_truth_or_outward_error_recomputed_here=False)


def read_input(args):
    root = Path(args.input).resolve().parent
    raw = Path(args.input).read_bytes()
    actual_input_sha = hashlib.sha256(raw).hexdigest()
    if not digest(args.expected_input_sha256) or actual_input_sha != args.expected_input_sha256:
        raise ValueError('The actual immutable input differs from the explicit expected SHA256')
    data = json.loads(raw)
    if not isinstance(data, dict) or data.get('schema') != INPUT_SCHEMA:
        raise ValueError('Use the complete new support-box consumer contract')
    used = {str(Path(args.input).resolve()):dict(path=str(Path(args.input).resolve()),
        sha256=actual_input_sha, bytes=len(raw))}
    field = data.get('field')
    if not isinstance(field, dict) or not isinstance(field.get('definition'), dict):
        raise ValueError('Retain the complete physical field definition, not a candidate label')
    definition = field['definition']
    if (definition.get('schema') != FIELD_SCHEMA
            or field.get('identity_sha256') != canonical(definition)
            or not isinstance(definition.get('mathematical_model'), dict)
            or definition.get('mathematical_model_identity_sha256')
                != canonical(definition['mathematical_model'])
            or definition.get('normal_convention') != NORMAL_CONVENTION
            or definition.get('fixed_cap_recipe') != CAP_RECIPE):
        raise ValueError('Keep the canonical complete current model, fixed caps and accurate outward normal')
    for name in ('current_full_point_sha256', 'checkpoint_sha256',
            'fixed_metric_identity_sha256', 'fixed_material_chart_identity_sha256'):
        if not digest(definition.get(name)):
            raise ValueError('A complete current mathematical identity is missing: ' + name)
    sources = data.get('source_files')
    declared_sources = definition.get('source_by_role')
    if (not isinstance(sources, dict) or not sources or not isinstance(declared_sources, dict)
            or set(sources) != set(declared_sources)):
        raise ValueError('Every declared complete field/producer source must have actual full bytes')
    for role, record in sources.items():
        nonempty_text(role, 'source role')
        verified_bytes(record, root, 'source:' + role, used)
        if record['sha256'] != declared_sources[role]:
            raise ValueError('The actual source differs from the canonical same-field definition: ' + role)
    checkpoint = data.get('checkpoint')
    verified_bytes(checkpoint, root, 'actual complete field checkpoint', used)
    if checkpoint['sha256'] != definition['checkpoint_sha256']:
        raise ValueError('The actual checkpoint belongs to a different field')
    cover = data.get('cover')
    if not isinstance(cover, dict):
        raise ValueError('The complete accurate cover definition is required')
    patches, reductions, minimum_width = validate_cover(cover, field)
    bounds = data.get('bounds')
    if not isinstance(bounds, dict) or set(bounds) != {'D_upper', 'K_A_upper', 'H_lower', 'R_lower'}:
        raise ValueError('Keep complete same-field diameter/curvature/cap-height/cap-radius bounds')
    exact = {name:rational(value, name) for name,value in bounds.items()}
    if exact['D_upper'] <= 0 or exact['K_A_upper'] < 0:
        raise ValueError('A positive diameter upper bound and nonnegative absolute curvature bound are required')
    producer_role = nonempty_text(data.get('support_producer_source_role'), 'support producer role')
    if producer_role not in sources:
        raise ValueError('The whole support-box producer must be source-bound')
    chunks = data.get('support_chunks')
    if not isinstance(chunks, list) or not chunks:
        raise ValueError('All complete support boxes must be present, not a chosen sample')
    declared_chunks = []
    for record in chunks:
        record_path(record, root)
        declared_chunks.append(dict(sha256=record['sha256'], bytes=record['bytes']))
    claims = dict(
        current_field_binding=dict(current_full_point_sha256=definition['current_full_point_sha256'],
            checkpoint_sha256=definition['checkpoint_sha256'],
            mathematical_model_identity_sha256=definition['mathematical_model_identity_sha256']),
        physical_six_jets=dict(normal_convention=NORMAL_CONVENTION,
            coverage_identity_sha256=cover['identity_sha256'],
            support_producer_source_sha256=sources[producer_role]['sha256'],
            complete_support_chunk_records=declared_chunks,
            complete_current_physical_lift_retained=True,
            all_root_scalar_quadrature_node_rounding_and_arithmetic_errors_included=True),
        complete_activity_domain_and_seams=dict(coverage_identity_sha256=cover['identity_sha256'],
            complete_original_radial_piece_set=True, all_accurate_tail_included=True,
            all_physical_domain_seams_C2=True),
        closed_sphere_immersion=dict(surface='complete-marked-closed-connected-C2-sphere-immersion',
            actual_activity_caps_and_cuffs_match=True),
        all_physical_phases=dict(formula='S_alpha = R_alpha A union C',
            axis='z', rotation_centre=['0', '0', '0'], activity_rotates=True,
            caps_are_fixed=True, full_physical_phase_range=True),
        diameter_bound=dict(D_upper=bounds['D_upper'], scope='complete-marked-surface-all-physical-phases'),
        activity_curvature_bound=dict(K_A_upper=bounds['K_A_upper'],
            scope='complete-accurate-activity-at-base-phase', all_pieces_and_tail=True),
        fixed_cap_parameters=dict(H_lower=bounds['H_lower'], R_lower=bounds['R_lower'],
            recipe_identity_sha256=canonical(CAP_RECIPE),
            physical_height_fixed_along_all_phases=True,
            own_induced_cap_metric_and_C2_attachment=True))
    if set(claims).intersection(reductions):
        raise ValueError('A reduced-domain evidence role cannot replace a required complete global proof: '
            + ', '.join(sorted(set(claims).intersection(reductions))))
    claims.update(reductions)
    evidence = data.get('evidence')
    if not isinstance(evidence, dict) or set(evidence) != set(claims):
        raise ValueError('Keep exactly every required global/accurate/extension proof, with no silent missing responsibility')
    evidence_records = {role:validate_evidence(role, evidence[role], claim,
        field, sources, root, used) for role,claim in claims.items()}
    boxes = []
    ids = set()
    rectangles = defaultdict(list)
    chunk_records = []
    for index, record in enumerate(chunks):
        chunk = verified_json(record, root, 'support chunk ' + str(index), used)
        if (not isinstance(chunk, dict) or chunk.get('schema') != CHUNK_SCHEMA
                or chunk.get('field_identity_sha256') != field['identity_sha256']
                or chunk.get('coverage_identity_sha256') != cover['identity_sha256']
                or chunk.get('producer_source_sha256') != sources[producer_role]['sha256']
                or chunk.get('normal_convention') != NORMAL_CONVENTION
                or chunk.get('all_values_are_accurate_outward_bounds') is not True
                or not isinstance(chunk.get('boxes'), list)):
            raise ValueError('A support chunk differs in source, field, accurate domain or physical normal')
        validate_execution(chunk.get('execution'))
        for row in chunk['boxes']:
            if not isinstance(row, dict):
                raise ValueError('Each complete closed box must be an explicit record')
            name = nonempty_text(row.get('id'), 'support box id')
            if name in ids:
                raise ValueError('A complete support box identifier was repeated')
            ids.add(name)
            patch = row.get('patch')
            if patch not in patches:
                raise ValueError('A box names an undeclared physical patch')
            cell = exact_integer(row.get('cell'), 'original physical cell')
            if cell >= patches[patch]['cells']:
                raise ValueError('A box lies outside the complete original accurate mesh')
            ul, pl = row.get('u_interval'), row.get('phi_over_pi_interval')
            if not isinstance(ul, list) or len(ul) != 2 or not isinstance(pl, list) or len(pl) != 2:
                raise ValueError('Retain both exact radial and angular closed endpoints')
            u0,u1 = [rational(v, 'local radial endpoint') for v in ul]
            p0,p1 = [rational(v, 'angular endpoint') for v in pl]
            if not (0 <= u0 < u1 <= 1 and patches[patch]['angle_low'] <= p0 < p1 <= patches[patch]['angle_high']):
                raise ValueError('Each closed box must lie in its declared exact original cell/domain')
            a = rational(row.get('a_lower'), 'horizontal support numerator lower')
            b = rational(row.get('b_lower'), 'vertical support numerator lower')
            w = rational(row.get('normal_norm_upper'), 'normal norm upper')
            wl = (None if row.get('normal_norm_lower') is None
                else rational(row['normal_norm_lower'], 'normal norm lower'))
            if w <= 0 or (wl is not None and wl > w):
                raise ValueError('The normal norm enclosure must be ordered with positive upper endpoint')
            boxes.append(dict(id=name, patch=patch, cell=cell, a=a, b=b, w=w, wl=wl))
            rectangles[(patch,cell)].append((u0,u1,p0,p1))
        chunk_records.append(dict(sha256=record['sha256'], bytes=record['bytes'],
            box_count=len(chunk['boxes']), execution=chunk['execution']))
    if not boxes:
        raise ValueError('An empty support list cannot certify any physical surface')
    if exact_integer(data.get('declared_box_count'), 'declared full box count', 1) != len(boxes):
        raise ValueError('The complete declared support count differs from actual supplied boxes')
    coverage = dict(original_cells=0, completely_covered_cells=0,
        missing_cells=0, exact_sweep_strips_checked=0, first_missing_boxes=[])
    for patch, spec in patches.items():
        for cell in range(spec['cells']):
            coverage['original_cells'] += 1
            result = complete_rectangle_cover(rectangles.get((patch,cell), []),
                spec['angle_low'], spec['angle_high'])
            coverage['exact_sweep_strips_checked'] += result['strips_checked']
            if result['complete']:
                coverage['completely_covered_cells'] += 1
            else:
                coverage['missing_cells'] += 1
                if len(coverage['first_missing_boxes']) < 16:
                    coverage['first_missing_boxes'].append(dict(patch=patch, cell=cell,
                        **result['missing']))
    coverage['complete_rectangular_cover'] = coverage['missing_cells'] == 0
    coverage['minimum_proved_affine_cell_width'] = qtext(minimum_width)
    coverage['all_exact_physical_cell_widths_positive'] = minimum_width > 0
    coverage['full_circle_is_default'] = True
    coverage['reduced_patch_proofs_byte_bound'] = sorted(reductions)
    coverage['domain_or_symmetry_truth_inferred_from_cell_count'] = False
    return dict(input_sha256=actual_input_sha, input_bytes=len(raw), field=field,
        cover=cover, patches=patches, exact_bounds=exact, bounds=bounds,
        evidence=evidence_records, boxes=boxes, coverage=coverage,
        chunks=chunk_records, sources={role:dict(sha256=rec['sha256'],bytes=rec['bytes'])
            for role,rec in sources.items()}, used=used)


def choose_parameter(intervals):
    for kind in ('strict', 'weak'):
        for branch in ('beta_le_one', 'beta_ge_one'):
            if intervals[kind][branch].contains(Fraction(1)):
                return Fraction(1), kind, branch
        for branch in ('beta_le_one', 'beta_ge_one'):
            answer = intervals[kind][branch].choose()
            if answer is not None:
                return answer, kind, branch
    return None, None, None


def consume(bound):
    boxes = bound['boxes']
    D = bound['exact_bounds']['D_upper']
    KA = bound['exact_bounds']['K_A_upper']
    H = bound['exact_bounds']['H_lower']
    R = bound['exact_bounds']['R_lower']
    tau = REACH_RATIO * D
    intervals = {kind:dict(
        beta_le_one=RationalInterval(Fraction(0),Fraction(1),True,False,'0<beta<=1'),
        beta_ge_one=RationalInterval(Fraction(1),None,False,False,'1<=beta'))
        for kind in ('weak','strict')}
    for kind, branches in intervals.items():
        strict = kind == 'strict'
        for row in boxes:
            branches['beta_le_one'].impose(row['b'], tau*row['w']-row['a'], strict, row['id'])
            branches['beta_ge_one'].impose(row['b']-tau*row['w'], -row['a'], strict, row['id'])
        branches['beta_le_one'].impose(H, tau*CAP_DENOMINATOR+CAP_G, strict, 'complete-fixed-p4-caps')
        branches['beta_ge_one'].impose(H-tau*CAP_DENOMINATOR, CAP_G, strict, 'complete-fixed-p4-caps')
    cover_paid = (bound['coverage']['complete_rectangular_cover']
        and bound['coverage']['all_exact_physical_cell_widths_positive'])
    beta, choice_kind, branch = choose_parameter(intervals) if cover_paid else (None,None,None)
    supplied_wl = [row['wl'] for row in boxes if row['wl'] is not None]
    min_wl = min(supplied_wl) if supplied_wl else None
    every_wl = len(supplied_wl) == len(boxes)
    curvature_margin = 1 - max(KA, CAP_K)*tau
    caps_fit = R >= CAP_SUPPORT_RADIUS
    report = dict(schema=OUTPUT_SCHEMA, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        input_sha256=bound['input_sha256'], input_bytes=bound['input_bytes'],
        field_identity_sha256=bound['field']['identity_sha256'],
        mathematical_model_identity_sha256=bound['field']['definition']['mathematical_model_identity_sha256'],
        current_full_point_sha256=bound['field']['definition']['current_full_point_sha256'],
        checkpoint_sha256=bound['field']['definition']['checkpoint_sha256'],
        fixed_metric_identity_sha256=bound['field']['definition']['fixed_metric_identity_sha256'],
        coverage_identity_sha256=bound['cover']['identity_sha256'],
        normal_convention=NORMAL_CONVENTION, complete_box_count=len(boxes),
        source_by_role=bound['sources'], support_chunks=bound['chunks'], coverage=bound['coverage'],
        exact_bounds=bound['bounds'], reach_ratio=qtext(REACH_RATIO), tau=qtext(tau),
        cap_recipe_identity_sha256=canonical(CAP_RECIPE),
        cap_constants=dict(g_b=qtext(CAP_G),d_b=qtext(CAP_DENOMINATOR),K_cap=qtext(CAP_K)),
        intervals={kind:{name:item.metadata() for name,item in branches.items()}
            for kind,branches in intervals.items()},
        minimum_supplied_normal_norm_lower=None if min_wl is None else qtext(min_wl),
        rows_without_normal_norm_lower=len(boxes)-len(supplied_wl),
        immersion_positive_from_supplied_boxes=(min_wl>0 if every_wl else None),
        separate_complete_closed_immersion_proof_always_required=True,
        missing_immersion_lower_bounds_filled_with_zero=False,
        fixed_cap_support_disks_fit_from_supplied_R_lower=caps_fit,
        curvature_budget_margin=qtext(curvature_margin), curvature_budget_paid=curvature_margin>=0,
        external_bound_evidence=bound['evidence'],
        selected_global_beta=None, selection_kind=None, selection_branch=None,
        one_common_beta_for_all_boxes_caps_and_phases=True,
        mathematical_uniqueness_of_a_feasible_beta_claimed=False,
        support_parameter_feasible=False, conditional_R650_numerical_budgets_paid=False,
        complete_geometry_certified=False,
        complete_geometry_certificate_scope='This postprocessor checks coverage arithmetic and rational implications; every external accurate enclosure and global geometric proof still requires its own valid complete producer/proof.',
        field_sixjet_root_curvature_or_diameter_generated_here=False,
        external_mathematical_truth_verified_by_metadata_booleans=False,
        local_or_sampled_bounds_used_as_continuous_bounds=False,
        solver_admission_gate=False,
        status='not-paid', reason=None)
    if not cover_paid:
        report['reason'] = 'Accurate physical widths or exact complete rectangle coverage are not paid; no parameter is selected from a partial cover.'
        return report
    if beta is None:
        report['reason'] = 'Both exact rational feasible intervals are empty for the supplied outward bounds; this is not a proof of geometric impossibility.'
        return report
    lam = max(Fraction(1),beta)
    sigma = None
    support_excess = None
    raw_excess = None
    sigma_witness = raw_witness = None
    for row in boxes:
        numerator = row['a']+beta*row['b']
        gap = numerator-tau*lam*row['w']
        if gap < 0 or numerator <= 0:
            raise ArithmeticError('The selected single beta failed the complete exact second pass')
        current_sigma = numerator/row['w']
        if sigma is None or current_sigma < sigma:
            sigma, sigma_witness = current_sigma, row['id']
        if raw_excess is None or gap < raw_excess:
            raw_excess, raw_witness = gap, row['id']
    cap_numerator = beta*H-CAP_G
    cap_gap = cap_numerator-tau*lam*CAP_DENOMINATOR
    if cap_gap < 0 or cap_numerator <= 0:
        raise ArithmeticError('The selected beta did not pay the entire fixed cap bound')
    cap_sigma = cap_numerator/CAP_DENOMINATOR
    if cap_sigma < sigma:
        sigma, sigma_witness = cap_sigma, 'complete-fixed-p4-caps'
    if cap_gap < raw_excess:
        raw_excess, raw_witness = cap_gap, 'complete-fixed-p4-caps'
    support_excess = sigma-tau*lam
    if support_excess < 0 or (choice_kind == 'strict' and support_excess <= 0):
        raise ArithmeticError('The full normalized strict/weak support comparison changed scope')
    # R650 needs a genuine complete immersion, supplied by its distinct bound
    # proof above.  A particular positive quantitative w_lower is helpful but
    # is not an additional mathematical requirement or solver admission gate.
    paid = caps_fit and H>0 and curvature_margin>=0
    report.update(selected_global_beta=qtext(beta), selection_kind=choice_kind,
        selection_branch=branch, lambda_max=qtext(lam), sigma_lower=qtext(sigma),
        sigma_lower_witness=sigma_witness,
        support_excess_over_target=qtext(support_excess),
        minimum_raw_numerator_excess=qtext(raw_excess),
        minimum_raw_numerator_excess_witness=raw_witness,
        fixed_cap_numerator_excess=qtext(cap_gap),
        strict_positive_support_paid=sigma>0,
        strict_positive_excess_over_target=support_excess>0,
        support_parameter_feasible=True,
        full_second_pass_boxes_checked=len(boxes),
        conditional_R650_numerical_budgets_paid=paid,
        conditional_R650_reach_lower_bound=qtext(tau) if paid else None,
        status=('conditional-budgets-paid-with-strict-support-excess' if support_excess>0
            else 'conditional-budgets-paid-at-nonstrict-target-boundary') if paid
            else 'support-parameter-found-other-geometric-budgets-unpaid',
        reason='The exact R650 implication is conditional on all byte-bound external complete proofs; no missing field, root, tail, rounding, topology, seam, or symmetry proof is inferred here.')
    return report


def protected_output(output, used):
    path = Path(output).resolve()
    for original in used:
        source = Path(original)
        if path == source or path in source.parents or source in path.parents:
            raise ValueError('The output must be fresh and disjoint from every actual input/source/proof path')
    if path.exists():
        raise ValueError('Use a fresh complete output; an existing report is immutable')
    return path


def recheck_used(used):
    for path, record in used.items():
        raw = Path(path).read_bytes()
        if len(raw) != record['bytes'] or hashlib.sha256(raw).hexdigest() != record['sha256']:
            raise ValueError('A consumed complete input/source/proof changed during postprocessing')


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, help='Complete immutable same-field support contract JSON')
    parser.add_argument('--expected-input-sha256', required=True)
    parser.add_argument('--output', required=True, help='Fresh compact result JSON; no raw boxes are copied')
    return parser.parse_args()


def main():
    args = parse_args()
    require_actions()
    start = time.monotonic()
    bound = read_input(args)
    own_path = Path(__file__).resolve()
    own_bytes = own_path.read_bytes()
    bind_used_record(bound['used'], dict(path=str(own_path),
        sha256=hashlib.sha256(own_bytes).hexdigest(), bytes=len(own_bytes)))
    output = protected_output(args.output, bound['used'])
    report = consume(bound)
    recheck_used(bound['used'])
    report['input_files_rechecked_after_complete_consumption'] = True
    report['actual_wall_seconds'] = time.monotonic()-start
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(report, sort_keys=True, indent=2, allow_nan=False)+'\n'
    with output.open('x', encoding='utf-8') as stream:
        stream.write(payload)
    summary = dict(schema=OUTPUT_SCHEMA, output_sha256=hashlib.sha256(payload.encode()).hexdigest(),
        complete_box_count=report['complete_box_count'],
        coverage_complete=report['coverage']['complete_rectangular_cover'],
        selected_global_beta=report['selected_global_beta'],
        support_parameter_feasible=report['support_parameter_feasible'],
        conditional_R650_numerical_budgets_paid=report['conditional_R650_numerical_budgets_paid'],
        complete_geometry_certified=False, status=report['status'])
    print(json.dumps(summary, sort_keys=True, allow_nan=False))


if __name__ == '__main__':
    main()
