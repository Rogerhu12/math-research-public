#!/usr/bin/env python3
"""Actual-margin inequalities with current protected-neighborhood representatives.

Every retained row is C_i z <= b_i with
 C_i = .03*(D sign(kappa) d_kappa + abs(kappa) d_D) T / norm_i,
 b_i = (numerical_safety - .03*D*abs(kappa))/norm_i.
No row is silently changed into a homogeneous tangent equality.
The bounded linear working set is separate from permanent nonlinear memory.
"""
from pathlib import Path
import mmap

import numpy as np


def build_inequality_rows(problem, x, geometry_module, point_module, transpose,
                         coordinate_size, *, reach_ratio=.03, safety=.992,
                         active_band=.025, max_rows=192, top_curvature=16,
                         top_radius=2, witnesses=(), radius_witnesses=(),
                         observed_module=None, matrix_workdir=None,
                         block_columns=32768, protected_angle_radius=.05,
                         diversity_u=1e-3, diversity_phi=None):
    q = problem
    if diversity_phi is None:
        diversity_phi = 1.0/(32*q.M)
    if not (0 < protected_angle_radius < np.pi/2 and diversity_u > 0 and diversity_phi > 0):
        raise ValueError('Need declared positive working-row neighborhood parameters')
    p = q.prepare(x)
    scan, locations, radial_locations = geometry_module.scan_geometry(
        q, x, top_curvature=top_curvature, top_radius=top_radius)
    if not scan['complete']:
        raise ValueError('A singular current point cannot define curvature inequalities')
    if observed_module is None or matrix_workdir is None:
        raise ValueError('Need literal observation weights and an explicit scratch directory')
    radii = []
    radius_records = []
    # Keep only scalar values and tiny point fields here.  Full-free radius
    # covectors are generated lazily after working rows have been selected;
    # 100 radius witnesses must not allocate 100 million-entry covectors.
    for stage, angle in radial_locations:
        f = geometry_module.single_fields(q, p, stage, angle)
        radius = float(np.linalg.norm(f['F']))
        radii.append((2*radius, ('grid_radius', int(stage), int(angle)), f))
    for witness in radius_witnesses:
        cell, u, phi = (int(witness['cell']), float(witness['u']), float(witness['phi']))
        f = point_module.fields_at(q, p, cell, u, phi, observed_module)
        radius = float(np.linalg.norm(f['F']))
        if not np.isfinite(radius) or radius <= 0:
            raise ValueError('Every actual radius witness needs positive finite radius')
        radii.append((2*radius, ('arbitrary_radius', cell, u, phi), f))
        radius_records.append(dict(cell=cell, u=u, phi=phi, diameter=2*radius))
    radii.append((2., ('fixed_core',), None))
    radii.append((2*abs(float(p.height)), ('cap_height',), None))
    strongest = max(range(len(radii)), key=lambda j: radii[j][0])
    candidates = []
    witnesses_read = []
    seen = {}
    witness_details = []

    def add_candidates(location, value, cot, meta, protected=False):
        for j, (diameter, rloc, _) in enumerate(radii):
            product = reach_ratio*diameter*abs(value)
            required = bool(protected and j == strongest)
            if not required and product < safety-active_band:
                continue
            key = (tuple(location), tuple(rloc))
            if key in seen:
                if required:
                    candidates[seen[key]]['required'] = True
                continue
            seen[key] = len(candidates)
            candidates.append(dict(product=product, location=location,
                value=value, cot=cot, principal=meta, diameter=diameter,
                radius_index=j, required=required, primary=(j == strongest)))

    for stage, angle, branch in locations:
        f = geometry_module.single_fields(q, p, stage, angle)
        value, cot, meta = geometry_module.curvature_cotangent(f, branch)
        add_candidates(('grid', int(stage), int(angle), int(branch)), value, cot, meta)
    for witness in witnesses:
        cell, u, phi = (int(witness['cell']), float(witness['u']), float(witness['phi']))
        f = point_module.fields_at(q, p, cell, u, phi, observed_module)
        values = [geometry_module.curvature_cotangent(f, branch) for branch in (0, 1)]
        largest = int(np.argmax([abs(v[0]) for v in values]))
        protected = bool(witness.get('protected', False))
        for branch, (value, cot, meta) in enumerate(values):
            add_candidates(('arbitrary', cell, u, phi, branch), value, cot, meta,
                           protected=(protected and branch == largest))
        witnesses_read.append(dict(cell=cell, u=u, phi=phi,
            signed_principal_curvatures=[v[0] for v in values], protected=protected))
        witness_details.append((cell, u, phi, values, protected))
    representatives = []
    for seed_cell, seed_u, seed_phi, seed_values, is_protected in witness_details:
        if not is_protected:
            continue
        neighbors = [value for value in witness_details if value[0] == seed_cell
                     and abs(value[2]-seed_phi) <= protected_angle_radius]
        current = max(neighbors, key=lambda value: max(abs(branch[0]) for branch in value[3]))
        cell, u, phi, values, _ = current
        branch = int(np.argmax([abs(value[0]) for value in values]))
        value, cot, meta = values[branch]
        add_candidates(('arbitrary', cell, u, phi, branch), value, cot, meta, protected=True)
        representatives.append(dict(seed=[seed_cell, seed_u, seed_phi],
            current_location=[cell, u, phi], current_branch=branch,
            current_absolute_curvature=abs(value),
            rule='same original cell, phi within declared radius; highest among all permanent points'))
    required_count = sum(c['required'] for c in candidates)
    if required_count > max_rows:
        raise ValueError('Working-row cap would drop a declared protected inequality')
    eligible = len(candidates)
    candidates.sort(key=lambda c: (not c['required'], not c['primary'], -c['product']))
    required = [candidate for candidate in candidates if candidate['required']]
    selected = required.copy()
    def physical_location(candidate):
        loc = candidate['location']
        if loc[0] == 'grid':
            stage, angle, branch = loc[1:]
            return (int(q.observation_cells[stage]), float(q.observation_u[stage]),
                    float(q.phi[angle]), int(branch))
        return (int(loc[1]), float(loc[2]), float(loc[3]), int(loc[4]))
    selected_points = [physical_location(candidate) for candidate in selected]
    diversity_skips = 0
    for candidate in candidates:
        if len(selected) >= max_rows:
            break
        if candidate['required'] or not candidate['primary']:
            continue
        cell, u, phi, branch = physical_location(candidate)
        close = any(cell == c and branch == br and abs(u-v) < diversity_u
                    and abs(phi-angle) < diversity_phi for c, v, angle, br in selected_points)
        if close:
            diversity_skips += 1
            continue
        selected.append(candidate)
        selected_points.append((cell, u, phi, branch))
    # If distinct primary rows do not use the cap, retain alternative actual
    # diameter partners.  Do not refill it with near-duplicate primary points.
    for candidate in candidates:
        if len(selected) >= max_rows:
            break
        if candidate['required'] or candidate['primary']:
            continue
        selected.append(candidate)
    candidates = selected
    directory = Path(matrix_workdir)
    directory.mkdir(parents=True, exist_ok=False)
    path = directory/'normalized-inequality-rows.f64'
    matrix = (np.memmap(path, dtype=np.float64, mode='w+',
                       shape=(len(candidates), coordinate_size))
              if candidates else np.empty((0, coordinate_size)))
    bounds = np.empty(len(candidates))
    row_metadata = []
    radius_covectors = {}

    def discard_pages():
        if (isinstance(matrix, np.memmap) and hasattr(matrix._mmap, 'madvise')
                and hasattr(mmap, 'MADV_DONTNEED')):
            matrix._mmap.madvise(mmap.MADV_DONTNEED)

    def radius_covector(index):
        if index in radius_covectors:
            return radius_covectors[index]
        diameter, loc, fields = radii[index]
        if loc[0] == 'fixed_core':
            result = np.zeros(q.free_size)
        elif loc[0] == 'cap_height':
            result = np.zeros(q.free_size)
            result[-1] = 2*np.sign(p.height)
        else:
            cot = {key: np.zeros(3) for key in fields}
            cot['F'] = 4*fields['F']/diameter
            if loc[0] == 'grid_radius':
                result = point_module.pullback(q, p, loc[1], loc[2], cot)
            else:
                result = point_module.pullback_at(q, p, *loc[1:], cot, observed_module)
        radius_covectors[index] = result
        return result

    for index, c in enumerate(candidates):
        loc = c['location']
        if loc[0] == 'grid':
            dk = point_module.pullback(q, p, loc[1], loc[2], c['cot'])
        else:
            dk = point_module.pullback_at(q, p, *loc[1:4], c['cot'], observed_module)
        dD = radius_covector(c['radius_index'])
        gradient = reach_ratio*(c['diameter']*np.sign(c['value'])*dk+abs(c['value'])*dD)
        row = transpose(gradient)
        norm = float(np.linalg.norm(row))
        if not np.isfinite(norm) or norm <= 0:
            raise ValueError('A declared geometric inequality needs positive finite row norm')
        matrix[index] = row/norm
        bounds[index] = (safety-c['product'])/norm
        row_metadata.append(dict(index=index, current_product=c['product'],
            actual_product_margin=safety-c['product'], normalized_bound=bounds[index],
            gradient_coordinate_norm=norm, signed_curvature=c['value'],
            diameter=c['diameter'], curvature_point=loc,
            radius_point=radii[c['radius_index']][1],
            protected_inequality=c['required'], strongest_radius_partner=c['primary'],
            principal_metadata=c['principal']))
        if (index+1) % 8 == 0:
            matrix.flush()
            discard_pages()
    if isinstance(matrix, np.memmap):
        matrix.flush()
        discard_pages()
    metadata = dict(
        schema='complete-actual-margin-neighborhood-diverse-inequalities-v2',
        selected_rows=len(candidates), eligible_rows=eligible,
        protected_inequalities=required_count,
        protected_current_representatives=representatives,
        protected_phi_neighborhood_radius=protected_angle_radius,
        diversity_u=diversity_u,diversity_phi=diversity_phi,
        near_duplicate_primary_rows_deferred=diversity_skips,
        permanently_screened_curvature_locations=len(witnesses),
        permanently_screened_radius_locations=len(radius_witnesses),
        reach_ratio=reach_ratio, safety=safety, active_band=active_band,
        maximum_working_rows=max_rows, top_curvature=top_curvature, top_radius=top_radius,
        row_formula='C=(reach_ratio*(D*sign(kappa)*dkappa+abs(kappa)*dD) T)/norm',
        bound_formula='b=(safety-reach_ratio*D*abs(kappa))/norm; C z <= b',
        homogeneous_equalities_imposed=False, all_original_field_variables_retained=True,
        row_cache=str(path), row_cache_bytes=int(matrix.size*8), block_columns=block_columns,
        lazy_full_free_radius_covectors=len(radius_covectors),
        current_grid_scan=scan, current_arbitrary_curvatures=witnesses_read,
        current_arbitrary_radii=radius_records, rows=row_metadata,
        selection='Original protected points and each protected current same-cell angular-neighborhood maximum first; separated near-active strongest-D rows next; alternative diameter partners only afterward. No nonlinear location merged or dropped',
        nonlinear_memory_policy='No location removed when its linear row is unselected',
        scope='Finite first-order geometric step inequalities only; true full point geometry still decides nonlinear acceptance')
    return matrix, bounds, metadata
