#!/usr/bin/env python3
"""Three fixed stages: reviewed root-only A plus isolated final-state Kahan.

Only final RK state-plus-increment arithmetic differs from the reviewed A
source. Ordinary four-term sums, the original RHS, intermediate RK states,
and the shifted root implementation are inherited unchanged. Carry starts
at zero per stage, is not a physical unknown and never enters RHS inputs
except through the rounded state after an ordinary final RK step.
No production, full-tail, flow Jacobian or DN operation is provided here.
"""
import argparse
import gc
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import traceback
import mpmath as mp

SHIFTED_SHA256 = 'fa4c6187031cee0b6828ec5b2af29be1c5c0f1c46ee3fa80aa485c061f1fbf34'
KAHAN_SHA256 = '0f57aa60fe9b76f47ecf949d661998a0fbfff05fd6a7e5e1954f959b51f13221'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ident(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


SHIFTED_PATH = Path(__file__).with_name('probe_shifted_root_stage_flow.py')
KAHAN_PATH = Path(__file__).with_name('probe_frozen_stage_rk_state_carry.mjs')
if sha(SHIFTED_PATH) != SHIFTED_SHA256 or sha(KAHAN_PATH) != KAHAN_SHA256:
    raise ValueError('An independently reviewed arithmetic source changed')
spec = importlib.util.spec_from_file_location('reviewed_shifted_root', SHIFTED_PATH)
shifted = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shifted)
base = shifted.base


class ShiftedRootWithFinalCarry(shifted.ShiftedRootEngine):
    def __init__(self, capsule, fixture, arithmetic):
        # This fixes the reviewed A arm; the linear-split branch is unavailable.
        super().__init__(capsule, fixture, arithmetic, 'root-only')
        self.final_carry = None
        self.carry_diagnostics = None

    def flow(self, fixture):
        state = [self.backend.make(v) for v in fixture['initial42']]
        carry = [self.zero for _ in range(self.size)]
        min_a = min_d = self.infinity
        changed_updates = 0
        maximum_carry = self.zero
        maximum_update_difference = self.zero

        def increment(v, f, h):
            # Identical to the original: carry is not included in b/c/d states.
            return [x+h*f[j] for j, x in enumerate(v)]

        def field(v, profile, step, label, x):
            nonlocal min_a, min_d
            self.emit('rk_field', profile=profile, step=step, label=label, x=x)
            f, ma, md = self.rhs(v, profile, x)
            min_a, min_d = min(min_a, ma), min(min_d, md)
            return f

        for i, grid in enumerate(fixture['grid']):
            for k, point in enumerate(grid):
                x, original_h = point['x'], point['h']
                h = self.backend.make(original_h)
                a = field(state, i, k, 'a', x)
                b = field(increment(state, a, h/2), i, k, 'b', x+original_h/2)
                c = field(increment(state, b, h/2), i, k, 'c', x+original_h/2)
                d = field(increment(state, c, h), i, k, 'd', x+original_h)
                for j in range(self.size):
                    # Ordinary original four-term sum and original h/6 order.
                    step_increment = h*(a[j]+2*b[j]+2*c[j]+d[j])/6
                    previous = state[j]
                    previous_carry = carry[j]
                    ordinary = previous+step_increment  # diagnostic only
                    corrected = step_increment-previous_carry
                    next_state = previous+corrected
                    carry[j] = (next_state-previous)-corrected
                    state[j] = next_state
                    if base.packed([next_state]) != base.packed([ordinary]):
                        changed_updates += 1
                    maximum_carry = max(maximum_carry, abs(carry[j]))
                    maximum_update_difference = max(maximum_update_difference, abs(next_state-ordinary))
                    self.emit('rk_final_carry', profile=i, step=k, component=j,
                              previous=previous, stepIncrement=step_increment,
                              previousCarry=previous_carry, corrected=corrected,
                              ordinary=ordinary, nextState=next_state, carry=carry[j])
        self.final_carry = list(carry)
        self.carry_diagnostics = dict(changed_state_updates=changed_updates,
            maximum_auxiliary_carry=maximum_carry,
            maximum_final_auxiliary_carry=max(map(abs, carry)),
            maximum_local_update_difference=maximum_update_difference,
            final_carry42_sha256=base.numeric_sha(carry))
        return state, min_a, min_d


def checked(ref):
    if sha(ref['path']) != ref['sha256']:
        raise ValueError('Frozen input/readout changed: ' + ref['path'])
    return base.load(ref['path'])


def compare(state, expected, fixture):
    actual = [mp.mpf(float(v)) for v in state]
    precise = [mp.mpf(v) for v in expected]
    errors = [actual[j]-precise[j] for j in range(42)]
    ratio, scale = mp.mpf(float(fixture['portRatio'])), mp.mpf(float(fixture['normalizationScale']))
    normalized = [abs(errors[j] if j < 20 else errors[j]/ratio)/scale for j in range(40)]
    return dict(maximum_all42_error_to_mp90=mp.nstr(max(map(abs, errors)), 32),
                maximum_mean2_error_to_mp90=mp.nstr(max(map(abs, errors[40:])), 32),
                maximum_normalized_physical_error_to_mp90=mp.nstr(max(normalized), 32),
                mp_error_peak_component=max(range(40), key=lambda j: normalized[j]))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('capsule-summary', 'float-baseline', 'mp90-summary', 'shifted-root-summary',
                 'old-kahan-summary', 'bridge', 'out-prefix'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--node', default='node')
    a = p.parse_args()
    cs, bs, ms, ss, ks = [base.load(path) for path in
        (a.capsule_summary, a.float_baseline, a.mp90_summary, a.shifted_root_summary, a.old_kahan_summary)]
    capsule_ref, baseline_ref, mp_ref = ident(a.capsule_summary), ident(a.float_baseline), ident(a.mp90_summary)
    if (not bs['all_original_operands_and_judgments_bitwise_identical'] or
            not bs['all_three_outputs42_bitwise_identical'] or
            bs['source_sha256'] != shifted.BASE_SHA256 or bs['capsule_summary_sha256'] != capsule_ref['sha256'] or
            ms['validated_baseline_sha256'] != baseline_ref['sha256'] or
            ms['source_sha256'] != shifted.BASE_SHA256 or ms['capsule_summary_sha256'] != capsule_ref['sha256'] or
            ms['precision'] != 'mp' or ms['dps'] != 90 or bs['bridge_sha256'] != sha(a.bridge) or
            ss['arm'] != 'root-only' or ss['source_sha256'] != SHIFTED_SHA256 or
            ss['capsule_summary'] != capsule_ref or ss['float_baseline'] != baseline_ref or
            ss['mp90_summary'] != mp_ref or ss['bridge_sha256'] != sha(a.bridge) or
            ks['source_sha256'][str(KAHAN_PATH.resolve())] != KAHAN_SHA256):
        raise ValueError('The exact original baseline or reviewed comparison identity changed')
    for key in ('source_sha256', 'additional_original_root_sources'):
        for path, digest in cs[key].items():
            if sha(path) != digest:
                raise ValueError('A bound original source changed: ' + path)
    capsule = checked(cs['coefficients'])
    reference = checked(cs['reference'])
    precise = checked(ms['raw'])
    a_raw = checked(ss['raw'])
    k_raw = checked(ks['compensated'])
    if ks['inherited_fixture'] != cs['fixture'] or ks['input_sha256'] != cs['input']['sha256']:
        raise ValueError('Existing Kahan belongs to another original fixture')
    states = {name:{r['stage']:r['state'] for r in data['rows']}
              for name, data in (('original', reference), ('mp90', precise), ('A', a_raw), ('Kahan', k_raw))}
    if [f['stage'] for f in capsule['fixtures']] != [43, 38, 175] or capsule['modes'] != 20:
        raise ValueError('Only the prescribed original three-stage scope is supported')
    del reference, precise, a_raw, k_raw
    gc.collect()
    paths = {name:Path(str(a.out_prefix)+'-'+name+('.json' if name == 'summary' else '.json.gz'))
             for name in ('raw', 'summary', 'failure')}
    for path in paths.values():
        if path.exists():
            raise ValueError('Do not overwrite completed numerical output: ' + str(path))
    a.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    context = dict(scope=__doc__, source=ident(__file__), shifted_root_source=ident(SHIFTED_PATH),
        original_base_source=ident(shifted.BASE_PATH), original_kahan_source=ident(KAHAN_PATH), bridge=ident(a.bridge),
        capsule_summary=capsule_ref, float_baseline=baseline_ref, mp90_summary=mp_ref,
        previously_executed_root_only_A=ident(a.shifted_root_summary),
        previously_executed_original_root_Kahan=ident(a.old_kahan_summary), command=sys.argv,
        root_rules=capsule['root_rules'], original_RHS_unchanged=True,
        original_four_term_sum_unchanged=True, original_intermediate_RK_formulas_unchanged=True,
        shifted_root_code_unchanged=True, carry_zero_initialized_per_stage=True,
        carry_read_by_RHS=False, full_flow_jacobian_computed=False, complete_tail_solver_invoked=False,
        production_source_changed=False, physical_checkpoint_written=False,
        stopping_scope='Inherits reviewed A stable ell+quad stop arithmetic, with original threshold constants. Not original binary64 formed-moment stop-path identity.',
        real_arithmetic_scope='In exact arithmetic (next-previous)-corrected is zero, so carry stays zero and the method reduces to reviewed A. Finite carry is an auxiliary summation value, not an extra physical unknown or an RK stage correction.')
    rows, scalars = [], []
    mp.mp.dps = 140
    began = time.monotonic()
    arithmetic = base.V8Float(a.bridge, a.node)
    try:
        for fixture in capsule['fixtures']:
            engine = ShiftedRootWithFinalCarry(capsule, fixture, arithmetic)
            start = time.monotonic()
            try:
                state, min_a, min_d = engine.flow(fixture)
            except Exception as error:
                shifted.save_gz(paths['failure'], dict(**context, stage=fixture['stage'], error=repr(error),
                    traceback=traceback.format_exc(), events=engine.events, root_outcomes=engine.root_outcomes))
                raise
            stage = fixture['stage']
            comparison = compare(state, states['mp90'][stage], fixture)
            existing = {name:compare(states[name][stage], states['mp90'][stage], fixture)
                        for name in ('original', 'A', 'Kahan')}
            physical = [v if j < 20 else v/fixture['portRatio'] for j, v in enumerate(state[:40])]
            residual = [v-fixture['targetNode40'][j] for j, v in enumerate(physical)]
            histogram = {}
            for root in engine.root_outcomes:
                key = str(root['iteration']); histogram[key] = histogram.get(key, 0)+1
            scalar = dict(stage=stage, **comparison, existing_saved_comparisons=existing,
                root_calls=len(engine.root_outcomes), root_iterations=histogram,
                root_fallbacks=sum(r['fallback'] for r in engine.root_outcomes),
                max_stable_root_relative_residual=max(r['err']/r['scale'] for r in engine.root_outcomes),
                max_formed_moment_root_relative_residual=max(r['formedMomentErr']/r['scale'] for r in engine.root_outcomes),
                carry_diagnostics=engine.carry_diagnostics,
                fixed_target_normalized_residual=max(map(abs, residual))/fixture['normalizationScale'],
                fixed_target_peak_component=max(range(40), key=lambda j:abs(residual[j])),
                output42_sha256=base.numeric_sha(state), minA=min_a, minD=min_d, seconds=time.monotonic()-start)
            scalars.append(scalar)
            rows.append(dict(stage=stage, state=state, residual=residual, carry=engine.final_carry,
                             events=engine.events, root_outcomes=engine.root_outcomes))
            print(json.dumps(dict(event='shifted_carry_stage_complete', **scalar)), flush=True)
    finally:
        arithmetic.close()
    raw = shifted.save_gz(paths['raw'], dict(**context, rows=rows))
    result = dict(**context, named_results=scalars, raw=raw, seconds=time.monotonic()-began,
        conclusion_scope='Only the new three-stage arithmetic output versus existing frozen MP90 and previously saved A/Kahan outputs. No effect, continuous accuracy or full-DN acceptance is presumed.')
    paths['summary'].write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(event='terminal', summary=str(paths['summary'].resolve()), sha256=sha(paths['summary']))), flush=True)


if __name__ == '__main__':
    main()
