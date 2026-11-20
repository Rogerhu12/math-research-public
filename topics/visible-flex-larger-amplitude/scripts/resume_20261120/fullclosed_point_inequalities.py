#!/usr/bin/env python3
"""Actual-margin first-order geometric inequalities in complete coordinates.

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
                         block_columns=32768):
    q = problem
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
    seen = set()

    def add_candidates(location, value, cot, meta, protected=False):
        for j, (diameter, rloc, _) in enumerate(radii):
            product = reach_ratio*diameter*abs(value)
            required = bool(protected and j == strongest)
            if not required and product < safety-active_band:
                continue
            key = (tuple(location), tuple(rloc))
            if key in seen:
                continue
            seen.add(key)
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
    required_count = sum(c['required'] for c in candidates)
    if required_count > max_rows:
        raise ValueError('Working-row cap would drop a declared protected inequality')
    eligible = len(candidates)
    candidates.sort(key=lambda c: (not c['required'], not c['primary'], -c['product']))
    candidates = candidates[:max_rows]
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
        schema='complete-actual-margin-geometry-inequalities-v1',
        selected_rows=len(candidates), eligible_rows=eligible,
        protected_inequalities=required_count,
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
        selection='Protected largest-absolute-curvature branch first; current near-active strongest-D rows next; other positive-margin branch/diameter pairs afterward',
        nonlinear_memory_policy='No location removed when its linear row is unselected',
        scope='Finite first-order geometric step inequalities only; true full point geometry still decides nonlinear acceptance')
    return matrix, bounds, metadata
