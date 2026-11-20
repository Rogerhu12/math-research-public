#!/usr/bin/env python3
"""Bind one actual completed full-QP parent to radial refinement and fine QP.

Default: stdlib report-only identity, terminal-damping and budget diagnosis.
--execute: public Actions only; recover every recorded permanent location,
perform one radial bisection at unchanged M/N/model, then one complete Phi
direction with 256 Hessian advances and atol=0. The frozen R676 entry owns
all scientific transfer/readout/solve operations. No old numerical result
or geometric value is substituted for the actual named parent.
"""
import argparse
import ast
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import subprocess
import sys
import zipfile


REFINEMENT_SHA = '2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a'
FINE_LAUNCHER_SHA = '100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622'
PARENTS = {
    '5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a':
        'fullclosed_gauss_inequality_qp.py',
    'b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8':
        'fullclosed_gauss_exact_tail_inequality_qp.py',
}
SCHEMA = 'completed-full-QP-parent-to-same-g-radial-refinement-v1'
POSITION_SCHEMA = 'immutable-curvature-history-locations-v1'


def sha(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            result.update(block)
    return result.hexdigest()


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def write_json(path, value, *, compact=False):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value, allow_nan=False,
        **(dict(separators=(',', ':')) if compact else dict(indent=2)))+'\n')
    temporary.replace(path)


def public_actions():
    return (os.environ.get('GITHUB_ACTIONS', '').lower() == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public')


def require_actions():
    if not public_actions():
        raise RuntimeError('Scientific arrays, refinement and solving belong in the public repository Actions')


def positive_number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(name+' must be a recorded positive real number')
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(name+' must be positive and finite')
    return value


def exact_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(name+' is not an integer')
    result = int(value)
    if result != value:
        raise ValueError(name+' was not an exact integer value')
    return result


def terminal_damping(report):
    """Replay the two frozen drivers' complete damping update, no solve."""
    if report.get('complete') is not True:
        raise ValueError('Need a naturally completed full-QP report, not a checkpoint')
    current = positive_number(report['initial_damping'], 'initial_damping')
    history = report['directions']
    if not isinstance(history, list):
        raise ValueError('The actual full-QP directions must be a list')
    trace = []
    for index, record in enumerate(history):
        if exact_integer(record['index'], 'direction index') != index:
            raise ValueError('The completed direction history is not the frozen sequential history')
        before = positive_number(record['damping'], 'direction damping')
        if before != current:
            raise ValueError('A recorded direction damping disagrees with the preceding frozen update')
        accepted = record['accepted']
        if not isinstance(accepted, bool):
            raise ValueError('Every completed direction must declare accepted as a boolean')
        alpha = ratio = None
        if accepted:
            alpha = positive_number(record['accepted_alpha'], 'accepted_alpha')
            if alpha > 1:
                raise ValueError('Frozen backtracking does not accept alpha greater than one')
            ratio = record['actual_to_full_step_predicted_decrease']
            if ratio is not None and (isinstance(ratio, bool) or not isinstance(ratio, (int, float))):
                raise ValueError('The recorded actual/predicted ratio must be numeric or null')
            if alpha == 1 and ratio is not None and ratio > .75:
                current = max(1e-8, before/2)
                rule = 'accepted full step with ratio > .75: max(1e-8, damping/2)'
            else:
                current = before
                rule = 'accepted other step: unchanged'
        else:
            current = before*4
            rule = 'complete direction rejected: damping*4'
        positive_number(current, 'terminal damping after direction')
        trace.append(dict(index=index, damping_before=before,
            damping_before_hex=before.hex(), accepted=accepted, accepted_alpha=alpha,
            actual_to_full_step_predicted_decrease=(ratio if ratio is None or math.isfinite(ratio)
                                                  else repr(ratio)),
            rule=rule, damping_after=current, damping_after_hex=current.hex()))
    return dict(initial_damping=float(report['initial_damping']), directions=len(history),
        terminal_damping=current, terminal_damping_hex=current.hex(),
        terminal_damping_exact_binary=str(Fraction(current)), trace=trace,
        no_direction_rule='initial_damping', final_damping_field_used=False,
        terminal_damping_from_this_actual_report_only=True)


def bound_parent_source(report, source_folder, supplied=None):
    declared = report.get('source_sha256')
    if declared in PARENTS:
        path = (Path(supplied).resolve() if supplied else source_folder/PARENTS[declared])
        if sha(path) != declared:
            raise ValueError('The named parent driver bytes do not match the actual parent report')
        return dict(**file_record(path), rule_version='frozen complete original/R671 QP update')
    # The R676 fine launcher generates an AST-derived file with the two
    # explicit manifest edits only. An actual next-level parent may bind it.
    if supplied is None:
        raise ValueError('For a derived fine parent, supply its actual --parent-source file')
    path = Path(supplied).resolve()
    if sha(path) != declared:
        raise ValueError('The actual derived driver SHA differs from the parent report')
    lines = path.read_text().splitlines()
    if len(lines) < 3 or lines[1] != '# Explicit fixed-g refinement driver derivation:' or not lines[2].startswith('# '):
        raise ValueError('Unsupported parent driver update rule; do not guess its final damping')
    derivation = json.loads(lines[2][2:])
    if (derivation.get('frozen_driver_sha256') not in PARENTS
            or derivation.get('derivation_source_sha256') != FINE_LAUNCHER_SHA
            or derivation.get('removed_arbitrary_size_checks') != 1
            or derivation.get('round13_keys_replaced_by_exact_binary_keys') != 6
            or derivation.get('pure_position_schema_insertions') != 1
            or derivation.get('mathematical_objective_changed') is not False
            or derivation.get('numerical_linear_solver_changed') is not False):
        raise ValueError('The parent is not the declared R676 manifest-only driver derivation')
    # A provenance comment is not evidence about an unknown body. Rebuild
    # the declared AST from the exact published base/transformer and compare
    # the entire actual body; no driver or field code is executed here.
    base = source_folder/PARENTS[derivation['frozen_driver_sha256']]
    transformer_path = source_folder/'launch_fixed_g_refinement_qp.py'
    if (sha(base) != derivation['frozen_driver_sha256']
            or sha(transformer_path) != FINE_LAUNCHER_SHA):
        raise ValueError('The exact frozen base and published AST transformer are required')
    name = 'complete_QP_parent_manifest_AST_identity'
    spec = importlib.util.spec_from_file_location(name, transformer_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)  # This bound module imports stdlib only.
    transform = module.ExactLocationDriver()
    expected = ast.fix_missing_locations(transform.visit(ast.parse(base.read_text(), filename=str(base))))
    counts = (transform.removed_size_checks, transform.exact_key_replacements,
              transform.position_schema_insertions)
    if counts != (1, 6, 1):
        raise ValueError('The bound AST transformer no longer has its declared edit sites')
    # The published writer emits ast.unparse; reparse that representation
    # before comparing, so formatting-only canonicalization is identical.
    expected_body = ast.dump(ast.parse(ast.unparse(expected)), include_attributes=False)
    actual_body = ast.dump(ast.parse(path.read_text(), filename=str(path)), include_attributes=False)
    if actual_body != expected_body:
        raise ValueError('The actual derived parent body is not the complete declared manifest-only AST derivation')
    return dict(**file_record(path), rule_version='R676 manifest-only derivation of frozen complete QP',
        declared_derivation=derivation, entire_derived_body_AST_equal=True,
        derived_body_AST_sha256=hashlib.sha256(actual_body.encode()).hexdigest(),
        frozen_base=file_record(base), exact_AST_transformer=file_record(transformer_path),
        parent_driver_body_executed=False)


class Locations:
    """Extract exact numeric positions from full reports, with no round13."""
    def __init__(self, J, P, N):
        self.J, self.P, self.N = J, P, N
        self.curvature = {}
        self.radius = {}
        self.pending = {}
        self.origins = Counter()
        self.occurrences = 0

    @staticmethod
    def role(key, inherited):
        key = str(key).lower()
        if key == 'arbitrary_witnesses':
            # Full geometry appends both curvature and radius witnesses
            # under this untyped key; retain those actual positions in both.
            return None
        if any(word in key for word in ('radius', 'radii', 'diameter', 'farthest')):
            return 'radius'
        if any(word in key for word in ('curvature', 'principal', 'worst')):
            return 'curvature'
        return inherited

    def put(self, cell, u, phi, role, protected, origin):
        cell = exact_integer(cell, 'permanent cell')
        u, phi = float(u), float(phi)
        if not 0 <= cell < self.J-1 or not math.isfinite(u) or not 0 <= u <= 1 or not math.isfinite(phi):
            raise ValueError('A reported permanent position is outside its actual parent domain')
        point = (cell, u, phi)
        if role in (None, 'curvature'):
            self.curvature[point] = self.curvature.get(point, False) or bool(protected)
        if role in (None, 'radius'):
            self.radius[point] = None
        self.origins[origin] += 1
        self.occurrences += 1

    def grid(self, stage, phi, role, protected, origin):
        stage = exact_integer(stage, 'permanent observation stage')
        phi = float(phi)
        if not 0 <= stage < self.P or not math.isfinite(phi):
            raise ValueError('A reported grid point is outside the parent observation plan')
        key = (stage, phi)
        entry = self.pending.setdefault(key, dict(roles=set(), protected=False, origins=set()))
        entry['roles'].update(('curvature','radius') if role is None else (role,))
        entry['protected'] |= bool(protected)
        entry['origins'].add(origin)
        self.origins[origin] += 1
        self.occurrences += 1

    def angle(self, value):
        value = exact_integer(value, 'quarter angle index')
        if not 0 <= value <= self.N//4:
            raise ValueError('The full-QP parent uses the complete quarter grid')
        # Literal formula of the bound quarter operator, not decimal rounding.
        return math.pi*value/(self.N//2)

    def tagged(self, value, role, protected, origin):
        if not isinstance(value, (tuple, list)) or not value or not isinstance(value[0], str):
            return False
        kind = value[0]
        if kind in ('grid', 'grid_radius'):
            expected = 4 if kind == 'grid' else 3
            if len(value) != expected:
                raise ValueError('Malformed recorded grid inequality location')
            self.grid(value[1], self.angle(value[2]),
                'curvature' if kind == 'grid' else 'radius', protected, origin)
            return True
        if kind in ('arbitrary', 'arbitrary_radius'):
            expected = 5 if kind == 'arbitrary' else 4
            if len(value) != expected:
                raise ValueError('Malformed recorded arbitrary inequality location')
            self.put(*value[1:4], 'curvature' if kind == 'arbitrary' else 'radius', protected, origin)
            return True
        if kind in ('fixed_core', 'cap_height'):
            # These are the solver's fixed diameter alternatives, not a
            # forgotten physical observation; the fine driver retains them.
            return True
        return False

    def walk(self, value, path=(), role=None, protected=False):
        origin = '.'.join(str(v) for v in path if not isinstance(v, int)) or 'report'
        if isinstance(value, dict):
            kind = value.get('kind')
            if kind in ('curvature', 'diameter', 'radius'):
                role = 'curvature' if kind == 'curvature' else 'radius'
            protected = protected or bool(value.get('protected', False)) or bool(value.get('protected_inequality', False))
            if all(key in value for key in ('cell','u','phi')):
                self.put(value['cell'], value['u'], value['phi'], role, protected, origin)
            elif 'stage' in value and ('phi' in value or 'angle' in value):
                phi = value['phi'] if 'phi' in value else self.angle(value['angle'])
                self.grid(value['stage'], phi, role, protected, origin)
            for key, item in value.items():
                subrole = self.role(key, role)
                subprotected = protected or 'protected' in key.lower()
                if key in ('curvature_point', 'radius_point') and self.tagged(item, subrole, subprotected, origin+'.'+key):
                    continue
                if (key in ('seed','current_location') and isinstance(item, list)
                        and len(item) == 3 and 'protected_current_representatives' in path):
                    self.put(*item, 'curvature', True, origin+'.'+key)
                    continue
                self.walk(item, path+(key,), subrole, subprotected)
        elif isinstance(value, list):
            if self.tagged(value, role, protected, origin):
                return
            # Pure-position lists may be present in reports' source records.
            if (path and path[-1] in ('curvature_points','radius_points','protected_curvature_points')
                    and len(value) == 3 and all(isinstance(v,(int,float)) and not isinstance(v,bool) for v in value)):
                self.put(*value, role, protected, origin)
                return
            for index, item in enumerate(value):
                if (path and path[-1] in ('curvature_points','radius_points','protected_curvature_points')
                        and isinstance(item,list) and len(item)==3
                        and all(isinstance(v,(int,float)) and not isinstance(v,bool) for v in item)):
                    self.put(*item, role, protected, origin)
                else:
                    self.walk(item, path+(index,), role, protected)

    def summary(self):
        return dict(curvature_numeric_tuples=len(self.curvature), radius_numeric_tuples=len(self.radius),
            protected_curvature_numeric_tuples=sum(self.curvature.values()),
            pending_grid_numeric_tuples=len(self.pending), recorded_position_occurrences=self.occurrences,
            extraction_paths=dict(self.origins), distinct_binary_locations_decimal_rounded=False,
            scope='All recorded physical dictionaries, full-memory entries, trial points, tagged inequality locations and protected representatives; untyped physical geometry records are retained in both point sets')

    def resolve_grid(self, carrier):
        require_actions()
        cells = npy_vector(carrier, 'observation_cells')
        local = npy_vector(carrier, 'observation_u')
        if len(cells) != self.P or len(local) != self.P:
            raise ValueError('The bound carrier does not contain the parent report full observation plan')
        count = len(self.pending)
        for (stage, phi), record in self.pending.items():
            for role in record['roles']:
                self.put(cells[stage], local[stage], phi, role, record['protected'], 'actual_carrier_grid_resolution')
        self.pending.clear()
        return count

    def arrays(self):
        if self.pending:
            raise ValueError('Resolve every grid position on the actual parent carrier before transfer')
        return dict(curvature_points=[list(v) for v in sorted(self.curvature)],
            radius_points=[list(v) for v in sorted(self.radius)],
            protected_curvature_points=[list(v) for v in sorted(self.curvature) if self.curvature[v]])


def npy_vector(path, key):
    """Read only two location-coordinate arrays, using stdlib, in Actions."""
    require_actions()
    with zipfile.ZipFile(path) as archive, archive.open(key+'.npy') as stream:
        if stream.read(6) != b'\x93NUMPY':
            raise ValueError('The observation coordinate is not a NumPy array')
        version = tuple(stream.read(2))
        if version[0] == 1:
            size = struct.unpack('<H', stream.read(2))[0]
        elif version[0] in (2,3):
            size = struct.unpack('<I', stream.read(4))[0]
        else:
            raise ValueError('Unsupported NumPy coordinate-array header')
        header = ast.literal_eval(stream.read(size).decode('utf-8' if version[0] == 3 else 'latin1'))
        if header['fortran_order'] or len(header['shape']) != 1:
            raise ValueError('Observation coordinate array must be a contiguous vector')
        descriptor = header['descr']
        endian = descriptor[0]
        if endian == '=':
            endian = '<' if sys.byteorder == 'little' else '>'
        types = {'i8':'q','i4':'i','u8':'Q','u4':'I','f8':'d'}
        if endian not in ('<','>') or descriptor[1:] not in types:
            raise ValueError('Only literal integer cells and binary64 local coordinates are supported')
        unit = struct.Struct(endian+types[descriptor[1:]])
        payload = stream.read()
        if len(payload) != header['shape'][0]*unit.size:
            raise ValueError('The coordinate array has inconsistent shape or truncated bytes')
        return [item[0] for item in struct.iter_unpack(unit.format, payload)]


def budget(report):
    J, M, N = [exact_integer(report[key], key) for key in ('J','M','N')]
    full_rows = exact_integer(report['all_full_rows'], 'all_full_rows')
    if J < 2 or M < 3 or N % 4 or N <= 4*M or full_rows % (3*N):
        raise ValueError('The bound full report has an incompatible complete-field shape')
    P = full_rows//(3*N)
    if P < 2*J-1:
        raise ValueError('The parent report does not retain its own node/midpoint prefix')
    fineJ = 2*J-1
    new_standard = 2*fineJ-1+6*(fineJ-1)
    retained_extra_upper = P-(2*J-1)
    fineP = new_standard+retained_extra_upper
    increase = (J-1)*3*(3*M+2)
    return dict(parent_J=J, refined_J=fineJ, parent_M=M, refined_M=M,
        parent_full_angles=N, refined_full_angles=N, parent_radial_observations=P,
        radial_factor=2, new_Gauss_order=6, new_standard_observations=new_standard,
        retained_parent_extra_observations_upper=retained_extra_upper,
        complete_refined_radial_observations_upper=fineP,
        refined_original_variables=int(report['original_variables'])+increase,
        refined_integrated_variables=int(report['integrated_variables'])+increase,
        exact_free_coordinate_increase=increase,
        one_complete_quarter_residual_bytes_upper=8*3*fineP*(N//4+1),
        two_complete_firstjet_caches_bytes_upper=8*6*fineP*(N//4+1),
        complete_process_peak_memory_estimated=False,
        scope='Algebraic dimensions and component storage only; actual row duplicates may reduce P; no field values or solver performance have been computed')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','parent-report','bundle','carrier','node-report','scalar-input','outdir'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--manifest', type=Path, action='append', required=True)
    p.add_argument('--parent-source', type=Path)
    p.add_argument('--stage-block', type=int, default=64)
    p.add_argument('--active-rows', type=int, default=192)
    p.add_argument('--qp-rtol', type=float, default=1e-6)
    p.add_argument('--execute', action='store_true', help='Run the prepared chain, only in public Actions')
    a = p.parse_args()
    for key in ('repo','work','parent_report','bundle','carrier','node_report','scalar_input','outdir'):
        setattr(a, key, getattr(a,key).resolve())
    a.manifest = [path.resolve() for path in a.manifest]
    if a.stage_block < 1 or a.active_rows < 1 or not math.isfinite(a.qp_rtol) or a.qp_rtol <= 0:
        raise ValueError('Positive explicit block/active-row/relative-tolerance parameters are required')
    report = json.loads(a.parent_report.read_text())
    source_folder = a.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    parent_source = bound_parent_source(report, source_folder, a.parent_source)
    damping = terminal_damping(report)
    if report.get('final_bundle_sha256') != sha(a.bundle):
        raise ValueError('The actual parent final_bundle_sha256 does not match the supplied parent field')
    if report.get('observation_carrier_sha256') != sha(a.carrier):
        raise ValueError('The actual complete-QP parent uses another observation carrier')
    if report.get('objective') != 'spectral':
        raise ValueError('This single-factor radial continuation keeps the existing positive spectral objective')
    stats = report.get('current', report['initial'])
    spectral = stats.get('spectral', {})
    if any(spectral.get(key) != value for key,value in dict(p=8,epsilon=.001,scale=.05).items()):
        raise ValueError('The bound parent must use the same fixed p8/.001/.05 objective')
    if report['radial_weights']['legacy_fraction'] != .5:
        raise ValueError('The R676 common-parent reader needs the declared half/half parent rule')
    if report['numerical_reach_safety_factor'] != .992:
        raise ValueError('This frozen fine launcher retains the declared .992 numerical geometry policy')
    for report_key, path in (('exact_tail_node_report_sha256',a.node_report),
                             ('exact_tail_scalar_input_sha256',a.scalar_input)):
        if report_key in report and report[report_key] != sha(path):
            raise ValueError('Changed fixed-model input: '+report_key)
    refine = source_folder/'refine_fixed_g_fullclosed.py'
    fine = source_folder/'launch_fixed_g_refinement_qp.py'
    if sha(refine) != REFINEMENT_SHA or sha(fine) != FINE_LAUNCHER_SHA:
        raise ValueError('Use the declared complete R676 transfer and fine solver bridge')
    input_records = {key:file_record(getattr(a,key)) for key in
                     ('parent_report','bundle','carrier','node_report','scalar_input')}
    old_manifests = []
    for path in a.manifest:
        payload = json.loads(path.read_text())
        declared = payload.get('carrier_sha256', payload.get('observation_carrier_sha256'))
        if declared != input_records['carrier']['sha256']:
            raise ValueError('Every supplied historical manifest must use the current parent carrier')
        old_manifests.append(file_record(path))
    shape = budget(report)
    locations = Locations(shape['parent_J'], shape['parent_radial_observations'], shape['parent_full_angles'])
    locations.walk(report)
    initial_locations = locations.summary()
    a.outdir.mkdir(parents=True, exist_ok=True)
    refinement_dir, fine_dir = a.outdir/'refinement', a.outdir/'fine-full-phi'
    fine_work = a.work/(a.outdir.name+'-'+input_records['parent_report']['sha256'][:12]+'-driver-work')
    supplement = a.outdir/'parent-report-permanent-locations.json'
    refine_command = [sys.executable,str(refine),'--repo',str(a.repo),
        '--bundle',str(a.bundle),'--carrier',str(a.carrier),'--node-report',str(a.node_report),
        '--scalar-input',str(a.scalar_input),'--outdir',str(refinement_dir),
        '--radial-factor','2','--modes',str(shape['parent_M']),
        '--source-angles',str(shape['parent_full_angles']),'--angles',str(shape['parent_full_angles']),
        '--stage-block',str(a.stage_block)]
    for path in [*a.manifest, supplement]:
        refine_command.extend(['--manifest',str(path)])
    fine_command = [sys.executable,str(fine),'--repo',str(a.repo),'--work',str(fine_work),
        '--refinement-report',str(refinement_dir/'refinement-report.json'),
        '--outdir',str(fine_dir),'--damping',repr(damping['terminal_damping']),
        '--directions','1','--maxiter','256','--active-rows',str(a.active_rows),
        '--qp-rtol',repr(a.qp_rtol),'--qp-atol','0','--stage-block',str(a.stage_block)]
    centers = report.get('requested_coarse_centers')
    if centers is not None:
        fine_command.extend(['--coarse-centers',','.join(repr(float(v)) for v in centers)])
    plan = dict(schema=SCHEMA,source_sha256=sha(__file__),inputs=input_records,
        parent_driver=parent_source,sources=dict(refinement=file_record(refine),fine_launcher=file_record(fine)),
        parent_dependency_sha256_by_role=report.get('source_sha256_by_role',{}),
        fine_driver_work_directory=str(fine_work),
        caller_manifests=old_manifests,terminal_damping=damping,budget=shape,
        parent_finite_snapshot=dict(max_relative_gram=stats.get('max_relative_gram'),
            mean_Phi=spectral.get('phi_normalized'),parameters={key:spectral[key] for key in ('p','epsilon','scale')},
            final_curvature_filter=report.get('final_curvature_filter'),
            scope='Values from this bound actual parent report only; no certificate inheritance'),
        permanent_location_diagnosis=initial_locations,
        commands=dict(refinement=refine_command,fine_solve=fine_command),
        fixed_budget=dict(radial_bisections=1,M_change=0,full_angle_change=0,Gauss_order=6,
            directions=1,maxiter=256,qp_atol=0.,qp_rtol=a.qp_rtol,active_rows=a.active_rows),
        scientific_arrays_read=False,scientific_execution_started=False,scientific_execution_complete=False,
        fixed_metric_refinement_convergence_claimed=False,
        location_scope='Caller manifests are passed unchanged in addition to all recoverable positions from this full report; values are never inherited; never-recorded points cannot be reconstructed',
        comparison='Full fine weights change; compare the separately returned common-parent-grid functional, not fine-minus-coarse Phi')
    plan_path = a.outdir/'plan.json'
    if plan_path.exists():
        previous = json.loads(plan_path.read_text())
        if (previous.get('scientific_execution_started')
                or previous.get('inputs') != input_records
                or previous.get('source_sha256') != sha(__file__)
                or previous.get('commands') != plan['commands']):
            raise FileExistsError('Use a fresh output directory for a different or already started actual batch')
    write_json(plan_path,plan)
    if not a.execute:
        print(json.dumps(dict(event='full_parent_refinement_report_only',plan=file_record(plan_path),
            terminal_damping=damping['terminal_damping'],budget=shape,
            permanent_locations=initial_locations,scientific_arrays_read=False),allow_nan=False),flush=True)
        return
    require_actions()
    if refinement_dir.exists() or fine_dir.exists():
        raise FileExistsError('Do not repeat an already prepared or executed scientific budget')
    plan.update(scientific_execution_started=True,execution={key:os.environ.get(key) for key in
        ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','GITHUB_SHA')})
    write_json(plan_path,plan)
    resolved = locations.resolve_grid(a.carrier)
    manifest = dict(schema=POSITION_SCHEMA,bundle_sha256=input_records['bundle']['sha256'],
        carrier_sha256=input_records['carrier']['sha256'],parent_report=input_records['parent_report'],
        source_sha256=sha(__file__),parent_driver=parent_source,**locations.arrays(),
        source='All recoverable full-QP history positions; caller manifests are additionally retained unchanged',
        values_inherited=False,decimal_position_rounding=False,
        grid_points_resolved_from_actual_bound_carrier=resolved,
        extraction=locations.summary())
    write_json(supplement,manifest,compact=True)
    plan.update(scientific_arrays_read=True,permanent_location_supplement=file_record(supplement),
                complete_parent_location_union=locations.summary())
    write_json(plan_path,plan)
    env=os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    for stage,command in (('refinement',refine_command),('fine_solve',fine_command)):
        plan['active_stage']=stage
        write_json(plan_path,plan)
        try:
            subprocess.run(command,cwd=a.repo,env=env,check=True)
        except subprocess.CalledProcessError as exc:
            plan.update(failed_stage=stage,subprocess_returncode=exc.returncode)
            write_json(plan_path,plan)
            raise
    returned=json.loads((fine_dir/'report.json').read_text())
    final=fine_dir/'final.npz'
    if returned.get('complete') is not True or returned.get('final_bundle_sha256') != sha(final):
        raise ValueError('The fine solve did not produce the declared naturally completed current field')
    plan.update(active_stage=None,scientific_execution_complete=True,
        actual_outputs={key:file_record(path) for key,path in dict(
            refinement_report=refinement_dir/'refinement-report.json',fine_report=fine_dir/'report.json',
            final_bundle=final,common_parent_grid=fine_dir/'common-parent-grid.json',
            fine_command_plan=fine_work/(fine_dir.name+'-fine-command.json')).items()},
        accepted_fine_directions=sum(record.get('accepted') is True for record in returned['directions']),
        fixed_metric_refinement_convergence_claimed=False)
    write_json(plan_path,plan)
    print(json.dumps(dict(event='bound_full_parent_refinement_chain_returned',plan=file_record(plan_path),
        actual_outputs=plan['actual_outputs'],accepted_fine_directions=plan['accepted_fine_directions'],
        fixed_metric_refinement_convergence_claimed=False),allow_nan=False),flush=True)


if __name__=='__main__':
    main()
