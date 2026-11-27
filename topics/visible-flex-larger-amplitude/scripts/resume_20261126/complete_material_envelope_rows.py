#!/usr/bin/env python3
"""Append full current-coordinate envelope rows after the unchanged known prefix.

No historical row is deleted or rescaled. Near-active current-grid choices are
bounded; actual separated typed constraints are permanent and uncapped. The old
full physical nonlinear screen, including all envelope points, accepts trials.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np

SCHEMA = 'complete-current-material-envelope-appended-rows-v1'
KEYS = ('F','Fs','Fphi','Fss','Fsphi','Fphiphi')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual complete envelope rows require public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def _key(location):
    return int(location['cell']),float(location['u']).hex(),float(location['phi']).hex()


def _literal(location):
    return dict(cell=int(location['cell']),u=float(location['u']),phi=float(location['phi']))


def _current_partner(scan):
    D,H,r = float(scan['diameter_point_lower']),float(scan['current_height']),float(scan['maximum_radius'])
    if D == 2.:
        return dict(kind='constant_core_diameter',value=2.)
    if D == 2*abs(H):
        return dict(kind='cap_height_diameter',sign=(1 if H>=0 else -1))
    if D == 2*r:
        return dict(kind='actual_radius_diameter',location=_literal(scan['farthest']))
    raise ValueError('An actual same-parent lower-diameter branch is required')


def _diameter(screen, partner):
    gradient = np.zeros(screen.q.free_size)
    kind = partner['kind']
    if kind == 'constant_core_diameter':
        if partner.get('value') != 2.:
            raise ValueError('Changed exact fixed-core lower-diameter constant')
        return 2.,gradient
    if kind == 'cap_height_diameter':
        sign = partner.get('sign')
        if sign not in (-1,1):
            raise ValueError('Keep the actual selected cap branch')
        D = 2*sign*float(screen._prepared.height)
        gradient[-1] = 2*sign
    elif kind == 'actual_radius_diameter':
        location = partner['location']
        if not screen.envelope.contains(location):
            raise ValueError('The selected lower-diameter point escaped the envelope')
        fields = screen._point(location)
        F = fields['F']
        D = 2*float(np.linalg.norm(F))
        if not math.isfinite(D) or D<=0:
            raise ArithmeticError('This finite lower-diameter branch has no usable nonzero derivative')
        cot = {key:np.zeros(3) for key in KEYS}
        cot['F'] = 4*F/D
        gradient = screen._pullback(location,cot)
    else:
        raise ValueError('Unknown actual lower-diameter branch')
    if not math.isfinite(D) or D <= 0:
        raise ArithmeticError('The retained signed diameter branch is not a positive lower bound here')
    return D,gradient


def _physical_row(screen, item, partner_cache):
    family,location = item['family'],item.get('location')
    if family != 'reach':
        kind = 'witness_distance' if family in ('distance_plus','distance_minus') else family
        sign = (1 if family=='distance_plus' else -1) if kind=='witness_distance' else None
        return screen._amplitude_row(kind,location,sign)
    branch,sign = item['branch'],item['sign']
    if branch not in (0,1) or sign not in (-1,1) or not screen.envelope.contains(location):
        raise ValueError('Retain each actual principal branch/signed envelope inequality')
    fields = screen._point(location)
    kappa,cot,detail = screen.pure.curvature_cotangent(fields,branch)
    gap = float(detail['principal_gap'])
    if not math.isfinite(gap) or gap <= 0 or not math.isfinite(float(kappa)):
        raise ArithmeticError('Selected eigenvalue has no certified simple numerical derivative; not geometric infeasibility')
    token = canonical(item['partner'])
    if token not in partner_cache:
        partner_cache[token] = _diameter(screen,item['partner'])
    D,dD = partner_cache[token]
    dk = screen._pullback(location,cot)
    rho = screen.reach_ratio
    gradient = rho*sign*(D*dk+float(kappa)*dD)
    value = rho*D*sign*float(kappa)-screen.safety
    return value,gradient,dict(kind='signed_necessary_reach_product',location=_literal(location),
        branch=int(branch),curvature_sign=int(sign),signed_principal_curvature=float(kappa),
        principal_gap=gap,diameter_partner=item['partner'],actual_partner_lower_diameter=D,
        all_current_free_core_and_rotation_and_height_derivatives_retained=True,
        formula='reach_ratio * selected_positive_diameter_lower * sign * kappa_branch - safety',
        both_signed_inequalities_equivalent_to_absolute_value=True)


def _candidate_key(item):
    location = None if item.get('location') is None else _literal(item['location'])
    partner = item.get('partner')
    if partner is not None:
        partner = dict(partner)
        if partner.get('location') is not None:
            partner['location'] = _literal(partner['location'])
    return canonical(dict(family=item['family'],location=location,partner=partner,
        branch=item.get('branch'),sign=item.get('sign')))


def _near_active(screen, active_band):
    """Every cell/branch participates; only the extra linear subset is capped."""
    scan = screen._last_scan
    partner = _current_partner(scan)
    D = float(scan['diameter_point_lower'])
    candidates = {}
    inspected = 0
    for cells,kappas,locate in screen.envelope_grids():
        cells = np.asarray(cells,dtype=int)
        if kappas.shape != (len(cells),screen.q.N,2):
            raise ValueError('The complete implicit grid curvature shape changed')
        for cell in range(screen.q.J-1):
            positions = np.nonzero(cells==cell)[0]
            if not len(positions):
                continue
            for branch in (0,1):
                block = np.abs(kappas[positions,:,branch])
                row,angle = np.unravel_index(int(np.argmax(block)),block.shape)
                radial = int(positions[row])
                kappa = float(kappas[radial,angle,branch])
                g = screen.reach_ratio*D*abs(kappa)-screen.safety
                inspected += 1
                if g < -active_band:
                    continue
                item = dict(family='reach',location=_literal(locate(radial,int(angle))),
                    partner=partner,branch=branch,sign=(1 if kappa>=0 else -1),
                    current_physical_g=g,selection='current cell/branch envelope maximum')
                key = _candidate_key(item)
                if key not in candidates or g > candidates[key]['current_physical_g']:
                    candidates[key] = item
    result = sorted(candidates.values(),key=lambda v:(-v['current_physical_g'],_candidate_key(v)))
    cap = screen.envelope.definition['additional_current_near_active_rows']
    return result[:cap],dict(all_cell_branch_maxima_considered=inspected,
        active_band=float(active_band),
        candidate_policy='all current and historical-extra cells, both branch maxima; descending physical g with exact literal tie key',
        near_active_candidates=len(result),new_near_active_row_cap=cap,
        selected_near_active_rows=min(cap,len(result)),all_implicit_points_remain_nonlinearly_permanent=True)


def append_rows(screen,matrix,bounds,metadata,transpose,coordinate_size,*,active_band,block_columns):
    require_actions()
    started = time.monotonic()
    if (screen._last_scan is None or screen._last_scan.get('complete') is not True
            or screen._last_scan['current_full_point_sha256'] != screen._token
            or screen._last_scan['material_envelope']['complete'] is not True
            or screen.envelope.model_identity != screen.q.identity
            or coordinate_size != screen.q.free_size
            or metadata.get('current_full_point_sha256') != screen._token):
        raise ValueError('Append only full current-coordinate rows at the same completely read parent')
    old_count = int(matrix.shape[0])
    if (matrix.shape != (old_count,coordinate_size) or len(bounds)!=old_count
            or metadata['selected_rows'] != old_count
            or metadata['original_prefix_rows']+metadata['appended_amplitude_rows'] != old_count):
        raise ValueError('The complete original geometry plus amplitude prefix is required')
    near,selection = _near_active(screen,float(active_band))
    memory = screen.envelope.separation_rows()
    choices = {}
    for row in memory+near:
        choices.setdefault(_candidate_key(row),row)
    rows = list(choices.values())
    path = Path(metadata['row_cache'])
    old_bytes = old_count*coordinate_size*8
    if not isinstance(matrix,np.memmap) or path.stat().st_size != old_bytes:
        raise ValueError('Append to the actual original complete streamed row cache')
    matrix.flush()
    # Hash is an actual full-prefix read; it is not inferred from count/shape.
    before_sha = sha(path)
    matrix._mmap.close()
    del matrix
    total = old_count+len(rows)
    with path.open('r+b') as stream:
        stream.truncate(total*coordinate_size*8)
    result = np.memmap(path,dtype=np.float64,mode='r+',shape=(total,coordinate_size))
    new_bounds = np.empty(total)
    new_bounds[:old_count] = bounds
    row_metadata = list(metadata['rows'])
    partner_cache = {}
    for offset,item in enumerate(rows):
        value,free_gradient,detail = _physical_row(screen,item,partner_cache)
        gradient = np.asarray(transpose(free_gradient),dtype=float)
        if gradient.shape != (coordinate_size,) or not np.isfinite(gradient).all() or not math.isfinite(value):
            raise FloatingPointError('The complete new coordinate row is missing or nonfinite')
        norm = float(np.linalg.norm(gradient))
        if not math.isfinite(norm):
            raise FloatingPointError('The complete coordinate row norm is nonfinite')
        scale = norm if norm > 0 else 1.
        index = old_count+offset
        # Only the newly allocated suffix is written. Known prefix words stay fixed.
        for begin in range(0,coordinate_size,int(block_columns)):
            end = min(coordinate_size,begin+int(block_columns))
            result[index,begin:end] = gradient[begin:end]/scale
        new_bounds[index] = -value/scale
        row_metadata.append(dict(index=index,**detail,physical_g=float(value),
            physical_current_value=float(value),upper_bound=0.,current_product=None,
            gradient_coordinate_norm=norm,row_normalization_scale=scale,
            zero_gradient_row_retained=bool(norm==0),normalized_bound=float(new_bounds[index]),
            original_prefix_row=False,material_envelope_row=True,
            typed_family=item['family'],typed_constraint_key=_candidate_key(item),
            permanently_separated_constraint=any(_candidate_key(v)==_candidate_key(item) for v in memory),
            current_full_point_sha256=screen._token))
        result.flush()
    # Verify every original byte after extension. Never replace this by a row count.
    h = hashlib.sha256()
    with path.open('rb') as stream:
        remaining = old_bytes
        while remaining:
            block = stream.read(min(1<<20,remaining))
            if not block:
                raise ValueError('The original complete row prefix was truncated')
            h.update(block)
            remaining -= len(block)
    if h.hexdigest() != before_sha:
        raise ValueError('A known original geometry/amplitude row was changed')
    if len(row_metadata)!=total or not np.isfinite(new_bounds).all():
        raise FloatingPointError('The complete original plus envelope rows are inconsistent')
    screen.envelope.rows_built(len(rows))
    output = dict(metadata)
    output.update(selected_rows=total,appended_envelope_rows=len(rows),
        known_geometry_and_amplitude_prefix_rows=old_count,known_prefix_bytes=old_bytes,
        known_prefix_sha256=before_sha,known_prefix_after_append_sha256=h.hexdigest(),
        known_prefix_rewritten=False,no_original_row_removed=True,
        envelope_rows_start_index=old_count,rows=row_metadata,
        row_cache_bytes=total*coordinate_size*8,row_cache_allocated_bytes=path.stat().st_blocks*512,
        material_envelope_rows=dict(schema=SCHEMA,source_sha256=sha(__file__),
            current_full_point_sha256=screen._token,actual_model_identity_sha256=screen.q.identity,
            policy_identity_sha256=screen.envelope.identity,selection=selection,
            actual_permanent_typed_count=len(memory),permanent_typed_rows_not_capped=True,
            actual_appended_typed_count=len(rows),actual_diameter_partner_count=len(partner_cache),
            actual_new_rows_sha256=canonical(row_metadata[old_count:]),
            elapsed_seconds=time.monotonic()-started,
            all_original_free_coordinates_retained=True,original_common_slack_includes_all_appended_rows=True,
            original_nonlinear_thresholds_unchanged=True,continuous_geometry_certified=False),
        material_envelope=screen.envelope.metadata(),
        scope='Original full known 192 geometry selection plus original amplitude prefix, unchanged, followed by complete-current envelope near-active and uncapped permanently separated typed rows; every nonlinear trial reads the whole permanent envelope')
    return result,new_bounds,output
