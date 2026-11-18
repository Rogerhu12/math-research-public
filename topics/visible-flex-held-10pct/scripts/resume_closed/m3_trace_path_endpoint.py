#!/usr/bin/env python3
"""Explicit completed M8 lambda=1 reader for the literal R44 endpoint.

The historical wire kind contains partial_lift; it is not used to guess the
mathematics. This reader requires exact lambda=1/strength=1 and the actual
literal_R44_endpoint branch. The original PathEnvironment uses the existing
R44 seven-control core and complete integral lift at this endpoint. Its full
physical p, fixed gauge/scales/warp, base+p0 and saved quintic are retained.

Binding is metadata-only. Native construction uses the unchanged source
factory; position() explicitly runs the original mean primitive if called.
The defining inlet is Gamma, while numerical inversion/quadrature and whole
metric/geometry certification remain separate. No completed endpoint is
invented; a real accepted prefix/audit/tail is required.
"""
from dataclasses import dataclass
import argparse
import copy
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct
import sys
from types import SimpleNamespace


HERE = Path(__file__).resolve().parent
M3 = HERE.parent / 'resume_m3'
KIND = 'exact_m3_finite_circle_trace_path_partial_lift'
CONTROL_PATH = 'finite-cosine-trace-synchronous-lift-v1'
ORIGINAL_COSINE_SHA = '4755143bb3c02c28669eebaa2db53ad97142acec799afd4136125db4277350d9'
MODEL_SHA = 'b5a26902c8af378d0f965269e4463814045ce98fa84f93935db9f31e1c5c950e'
COSINE_READER_SHA = '776bd257f9a299cce73d215597dcf2d02d161bf493deb2a66f9ece0972a327d4'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def load(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def payload_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def checked_file(item):
    if ref(item['path'])['sha256'] != item['sha256']:
        raise ValueError('A declared file changed: ' + item['path'])
    return Path(item['path']).resolve()


def exact_numbers(a, b):
    a, b = list(a), list(b)
    return (len(a) == len(b) and
            struct.pack('<' + 'd' * len(a), *a) == struct.pack('<' + 'd' * len(b), *b))


def check_plan(path):
    plan = load(path)
    unsigned = {key: value for key, value in plan.items() if key != 'identity_sha256'}
    if payload_sha(unsigned) != plan['identity_sha256']:
        raise ValueError('The stored coupled-plan payload changed')
    for name, digest in plan['source_sha256'].items():
        if sha(name) != digest:
            raise ValueError('A defining or execution source changed: ' + name)
    for item in plan['derived_source_files'].values():
        checked_file(item)
    for key in ('profile', 'tail_config', 'initial_plan', 'initial_arrays',
                'completed_initializer', 'starting_actual_anchor'):
        checked_file(plan[key])
    design = plan['design']
    if (plan['fixed_metric'] is not False or design['control_path'] != CONTROL_PATH or
            design['lambda_value'] != 1. or design['lift_window'] != [.5, .9] or
            design['gauge_amplitude'] != .06):
        raise ValueError('This reader is solely the literal lambda=1 M8 endpoint')
    checked_file(design['original_reference_checkpoint'])
    checked_file(design['original_reference_binding'])
    checked_file(design['original_chart'])
    if design['original_reference_checkpoint']['sha256'] != ORIGINAL_COSINE_SHA:
        raise ValueError('Another original cosine reference is not supported')
    if (sha(M3 / 'm3_circle_trace_path_model.py') != MODEL_SHA or
            sha(HERE / 'q060_cosine_reference.py') != COSINE_READER_SHA):
        raise ValueError('The reviewed model/reference reader changed')
    return plan


@dataclass(frozen=True)
class NativePathPrefix:
    binding: object
    environment: object
    obj: object
    flow: object
    core: object
    polynomial: object
    solution: object

    def position(self, s, angular=512):
        """Evaluate this saved finite graph, including its own numerical mean.

        This is an explicit new evaluation entry, not called by metadata
        preparation or native reconstruction. Original angular/segment Gauss
        integration and domain failures are retained; no continuous bound is
        inferred. The representation's height origin is zero at s=0.
        """
        import numpy as np
        if isinstance(angular, bool) or int(angular) != angular or angular < 16*(3*8+1):
            raise ValueError('Use an integer angular count at least the original audit minimum')
        s = np.atleast_1d(np.asarray(s, float))
        if np.any(~np.isfinite(s)) or np.any(s < 0.) or np.any(s > self.flow.end):
            raise ValueError('Evaluate only on the saved physical domain')
        B, _, _ = self.flow.basis(int(angular))
        g = self.flow.geo(s, int(angular))
        mean = self.flow.height_integral(self.solution, s, int(angular), 6)
        value = g['pos'] + self.obj.q * self.flow.values(self.polynomial(s), B)
        value[:, :, 2] += mean[:, None]
        return value


@dataclass(frozen=True)
class TracePathBinding:
    checkpoint: Path
    checkpoint_sha256: str
    plan_path: Path
    plan: dict
    record: dict
    tail_record: Path
    tail_record_sha256: str

    def check_files(self):
        if sha(self.checkpoint) != self.checkpoint_sha256:
            raise ValueError('The bound physical checkpoint changed')
        if sha(self.tail_record) != self.tail_record_sha256:
            raise ValueError('The bound actual tail record changed')
        if ref(self.plan_path) != self.record['path_coupled_entry_plan']:
            raise ValueError('The bound path plan changed')
        check_plan(self.plan_path)
        for chunk in self.record['pp_coefficient_chunks']:
            name = Path(chunk['file'])
            if name.name != str(name) or sha(self.checkpoint.parent / name) != chunk['sha256']:
                raise ValueError('A full physical polynomial chunk changed')

    def descriptor(self):
        r = self.record
        return dict(scope=__doc__, checkpoint=ref(self.checkpoint),
            path_plan=ref(self.plan_path), actual_tail_record=ref(self.tail_record),
            core_kind=KIND, control_path=CONTROL_PATH, modes=8, state_components=25,
            path_lambda=r['path_lambda'], lift_window=r['lift_window'],
            gauge_q=r['gauge_amplitude'], defining_support_q=r['seed_support_amplitude'],
            defining_primary_factor_record=r['defining_primary_factor'],
            complete_parameters=r['parameters'], complete_scales=r['central_correction_scales'],
            complete_physical_controls=r['physical_controls'],
            base_profile=r['path_base_profile'], final_profile=r['frozen_profile'],
            p0_rule='Use path_base_profile plus the complete original p0 exactly once. No delta rebasing is performed.',
            angular_chart=r['angular_chart'], chart_payload_sha256=payload_sha(r['chart']),
            warp_reference_q=r['warp_reference_q'], meridian_length=r['meridian_length'],
            original_cosine_reference=r['original_cosine_reference'],
            physical_tail_parameters=r['physical_tail_parameters'], physical_tail_cut=r['physical_tail_cut'],
            original_solver_success=r['solver_success'], actual_outer_checks=r['actual_outer_checks'],
            sampled_metric_l1=r['summary']['metric_l1'],
            sampled_metric_below_1e_minus_6=r['summary']['metric_l1'] < 1e-6,
            tail_shooting_residual=r['tail_seam']['tail_shooting_residual'],
            represented_field='All 25 saved physical quintic components plus the actual lambda=1 full-lift Flow.geo.',
            endpoint_dispatch=dict(lambda_value=1., branch='literal_R44_endpoint', full_lift_strength=1.,
                historical_wire_kind=KIND, defining_inlet_is_Gamma=True),
            mean_height='Not one of the 25 components. position() explicitly integrates this flow Vz through the original height_integral.',
            raw_cubic_scope='The saved physical quintic is not the original adaptive solver cubic or the original node/RHS tuple. This reader does not manufacture those values.',
            native_model_constructed=False, mean_height_integrated=False,
            initial_guess_projected=False, amplitude_restart_called=False,
            BVP_solver_invoked=False, actual_tail_solver_invoked=False,
            fixed_g_refinement_claim=False, continuous_error_certificate=False,
            exact_circular_inlet_claim=False,
            numerical_circle_certificate_scope='The defining R44 inlet is circular on its protected arc; no new bound on its floating evaluation or full surface follows.')

    def native_prefix(self):
        """Build precisely this recorded model in a fresh Python process.

        No mean primitive, initial guess, adaptive audit or tail solve is run.
        Source initial(p) constructs the actual full core and its projected
        inlet once, as required to attach the correct partial reference lift.
        The returned physical solution intentionally has no fabricated .y:
        evaluating a saved polynomial at nodes is not the original solver y.
        """
        self.check_files()
        import numpy as np
        from scipy.interpolate import PPoly
        from q060_cosine_reference import bind_reference
        original = load(self.record['original_cosine_reference_binding']['path'])
        bound = bind_reference(original['checkpoint']['path'], original['terminal_record']['path'],
                               original['source_topic'], original['short_bridge']['path'])
        native = bound.native_reference()  # Enforces a fresh original-core process.
        sys.path.insert(0, str(M3))
        from m3_circle_trace_path_model import CircleTracePathEnvironment
        r = self.record
        # The current declared family keeps this same base profile. A future
        # explicit rebase must be implemented separately, not silently accepted.
        if r['path_base_profile'] != bound.record['frozen_profile']:
            raise ValueError('A rebased path profile needs an explicit new reader')
        env = CircleTracePathEnvironment(bound, native, copy.deepcopy(r['core_round_settings']))
        obj = env.make(r['path_lambda'], r['seed_support_amplitude'])
        p = np.asarray(r['parameters'], float)
        obj.initial(p)
        flow = obj.flow(float(p[0]))
        if (obj.cfg != r['path_base_profile'] or obj.path_definition != r['path_definition'] or
                not exact_numbers(obj.pscale, r['central_correction_scales']) or
                not exact_numbers(obj.pscale * p[1:], r['physical_controls']) or
                not exact_numbers([obj.support_amplitude, flow.end],
                                  [r['actual_primary_amplitude'], r['meridian_length']]) or
                flow.exact_lift_core is not obj._core or
                not exact_numbers(obj._core.c, r['physical_controls'])):
            raise ValueError('The reconstructed full partial-path definition differs')
        from curve_stable_prefix_bvp import load_checkpoint
        decoded = load_checkpoint(self.checkpoint)
        mesh = np.asarray(decoded['mesh'], float)
        coefficients = np.asarray(decoded['pp_coefficients'], float)
        if (mesh.shape != (r['nodes'],) or coefficients.shape != (6, len(mesh)-1, 25) or
                not np.all(np.isfinite(mesh)) or not np.all(np.isfinite(coefficients)) or
                not np.all(np.diff(mesh) > 0) or mesh[0] != 0. or
                not exact_numbers([mesh[-1]], [flow.end])):
            raise ValueError('The complete physical M8 quintic/domain is required')
        pp = PPoly.construct_fast(coefficients, mesh, extrapolate=False, axis=1)
        physical = SimpleNamespace(x=mesh, sol=pp, p=p.copy())
        self.check_files()
        return NativePathPrefix(self, env, obj, flow, obj._core, pp, physical)


def bind_checkpoint(checkpoint):
    checkpoint = Path(checkpoint).resolve()
    r = load(checkpoint)
    cfg = r['config']
    if (r.get('core_kind') != KIND or cfg.get('core_kind') != KIND or
            r.get('core_control_path') != CONTROL_PATH or cfg['modes'] != 8 or
            cfg['base_mode'] != 3 or cfg['fixed_metric'] is not False or
            cfg['actual_nonlinear_tail'] is not True):
        raise ValueError('Reject legacy raw, full-lift, cosine or other core checkpoints')
    path = checked_file(r['path_coupled_entry_plan'])
    plan = check_plan(path)
    d = plan['design']
    lam = r['path_lambda']
    if (not exact_numbers([lam, r['partial_lift_strength']], [d['lambda_value']]*2) or
            r['lift_window'] != [.5, .9] or r['core_round_settings'] != d['new_core_settings'] or
            r['core_round_sources'] != plan['source_sha256'] or
            r['path_base_profile'] != d['physical_profile'] or
            r['original_cosine_reference'] != d['original_reference_checkpoint'] or
            r['original_cosine_reference_binding'] != d['original_reference_binding'] or
            r['defining_primary_factor'] != d['new_q'] or
            r['angular_chart'] != 'frozen-spline-adaptive-v1' or
            payload_sha(r['chart']) != d['chart_payload_sha256']):
        raise ValueError('The complete coupled path/source/profile identity differs')
    p, scales, controls = r['parameters'], r['central_correction_scales'], r['physical_controls']
    if (len(p) != 8 or len(scales) != 7 or len(controls) != 7 or
            not all(math.isfinite(v) for v in [*p, *scales, *controls]) or
            not exact_numbers(scales, plan['initial_parameter_scales']) or
            not exact_numbers([p[j+1]*scales[j] for j in range(7)], controls) or
            not exact_numbers([r['gauge_amplitude'], r['q_gauge'], r['warp_reference_q']], [.06]*3) or
            not exact_numbers([r['seed_support_amplitude'], r['actual_primary_amplitude']],
                              [d['new_q']['q_binary64']]*2)):
        raise ValueError('The complete parameters or gauge/support convention differs')
    frozen = copy.deepcopy(r['path_base_profile'])
    frozen['delta'] = frozen['delta'] + p[0]
    if frozen != r['frozen_profile']:
        raise ValueError('Final profile is not base profile plus p0 exactly once')
    original = load(r['original_cosine_reference']['path'])
    for key in ('physical_port_sha256', 'physical_tail_parameters', 'physical_tail_cut'):
        if r[key] != original[key]:
            raise ValueError('The original full physical tail/port changed: ' + key)
    definition = r['path_definition']
    if (definition['branch'] != 'literal_R44_endpoint' or
            definition['settings'] != r['core_round_settings'] or definition['lambda_value'] != lam or
            definition['numerical_gauge'] != .06 or definition['warp_reference'] != .06 or
            definition['defining_support_amplitude'] != r['seed_support_amplitude'] or
            definition['fixed_metric'] is not False or
            not exact_numbers(definition['parameter_scales'], scales)):
        raise ValueError('Incomplete or inconsistent partial-path definition')
    history, audit, seam = r['actual_outer_checks'], r['summary'], r['tail_seam']
    if (r['solver_success'] is not True or not history or
            history[-1].get('inner_success') is not True or
            not math.isfinite(history[-1]['actual_boundary_residual']) or
            history[-1]['actual_boundary_residual'] > cfg['bc_tol'] or
            not math.isfinite(audit['metric_l1']) or not math.isfinite(audit['darboux_l1']) or
            seam['tail_converged'] is not True or
            not math.isfinite(seam['tail_shooting_residual']) or
            not seam['tail_shooting_residual'] < 2e-9):
        raise ValueError('A complete original finite prefix/tail terminal is required')
    name = Path(seam['tail_record'])
    if name.name != str(name):
        raise ValueError('The terminal tail record must be a local saved filename')
    tail_path = checkpoint.parent / name
    tail = load(tail_path)
    if (tail['request']['jacobian'] is not True or tail['request']['audit'] is not True or
            tail['response']['converged'] is not True or
            tail['config'] != r['tail_config'] or
            tail['source_sha256'] != plan['native_tail_source_sha256'] or
            not exact_numbers([tail['response']['residual']], [seam['tail_shooting_residual']]) or
            tail['response']['jets'] != seam['tail_jets']):
        raise ValueError('The saved actual tail does not supply this complete seam')
    binding = TracePathBinding(checkpoint, sha(checkpoint), path, plan, r, tail_path, sha(tail_path))
    binding.check_files()
    return binding


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--prepare-from-plan', type=Path)
    group.add_argument('--checkpoint', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.prepare_from_plan is not None:
        plan = check_plan(args.prepare_from_plan)
        result = dict(scope=__doc__, reader=ref(__file__), plan=ref(args.prepare_from_plan),
            model=ref(M3/'m3_circle_trace_path_model.py'),
            original_reader=ref(HERE/'q060_cosine_reference.py'),
            defining_source_count=len(plan['source_sha256']), expected_kind=KIND,
            expected_control_path=CONTROL_PATH, design=plan['design'],
            production_checkpoint_bound=False, native_model_constructed=False,
            mean_height_integrated=False, numerical_equations_evaluated=False,
            acceptance_scope='No new accepted checkpoint is claimed or fabricated. End-to-end native loading remains to be exercised on a genuine complete terminal.',
            command=[sys.executable, *sys.argv])
    else:
        binding = bind_checkpoint(args.checkpoint)
        result = binding.descriptor()
        result.update(reader=ref(__file__), command=[sys.executable, *sys.argv])
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(output=ref(args.out), native_model_constructed=False,
                         mean_height_integrated=False, numerical_equations_evaluated=False)))


if __name__ == '__main__':
    main()
