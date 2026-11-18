#!/usr/bin/env python3
"""Collect exact three-stage port identity without rerunning any flow."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
from record_fixed_actual import load, scalar_tree, sha
from record_tail_initialization import numeric_identity


def identity(p):
    return dict(path=str(Path(p).resolve()), sha256=sha(p))


def packed(values):
    return struct.pack('<'+'d'*len(values), *values)


def trace_digest(events):
    h = hashlib.sha256()
    for event in events:
        h.update((json.dumps(numeric_identity(event), sort_keys=True, separators=(',', ':'))+'\n').encode())
    return h.hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('capsule-summary', 'float-summary', 'export-resource', 'float-resource',
                'export-log', 'float-log', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise ValueError('A completed record already exists')
    cs, fs = load(a.capsule_summary), load(a.float_summary)
    if (fs['precision'] != 'float' or not fs['all_original_operands_and_judgments_bitwise_identical'] or
            not fs['all_three_outputs42_bitwise_identical']):
        raise ValueError('Only an exactly accepted float baseline is recorded here')
    if fs['capsule_summary_sha256'] != sha(a.capsule_summary):
        raise ValueError('Float port used another original reference capsule')
    for key in ('source_sha256', 'additional_original_root_sources'):
        for path, value in cs[key].items():
            if sha(path) != value:
                raise ValueError('A bound original or exporter source changed: '+path)
    source = Path(fs['command'][0])
    if sha(source) != fs['source_sha256']:
        raise ValueError('The executed evaluator source changed')
    original_root = next(Path(s) for s in cs['source_sha256'] if s.endswith('/periodic-quadrature/general_root_tail_momentum.mjs'))
    for entry in cs['traced_source'].values():
        if sha(entry['path']) != entry['sha256']:
            raise ValueError('A traced source changed')
    for data in (cs['coefficients'], cs['reference'], fs['raw'], cs['fixture'], cs['original_output'], cs['input']):
        if sha(data['path']) != data['sha256']:
            raise ValueError('A bound input, capsule, or raw output changed')
    capsule, reference, port = load(cs['coefficients']['path']), load(cs['reference']['path']), load(fs['raw']['path'])
    old_fixture = load(cs['fixture']['path'])
    if numeric_identity(capsule['trig']) != numeric_identity(old_fixture['trig']):
        raise ValueError('The original full trigonometric tables changed')
    traced = original_root.read_text()
    for patch in capsule['trace_source_patches']:
        if traced.count(patch['original']) != 1:
            raise ValueError('An original trace patch does not uniquely match')
        traced = traced.replace(patch['original'], patch['replacement'])
    if traced.encode() != Path(cs['traced_source']['root']['path']).read_bytes():
        raise ValueError('The traced root has changes beyond the declared callbacks')
    original_split = original_root.with_name('f6tail_momentum_split_flux.mjs').read_text()
    traced_split = original_split.replace("'./general_root_tail_momentum.mjs'",
                                         json.dumps('./'+Path(cs['traced_source']['root']['path']).name))
    if traced_split.encode() != Path(cs['traced_source']['split']['path']).read_bytes():
        raise ValueError('The traced split module differs beyond its owned import')
    stages = {}
    total_events = total_root_calls = 0
    for fixture, previous, original, current, scalars in zip(capsule['fixtures'], old_fixture['fixtures'],
            reference['rows'], port['rows'], fs['named_results'], strict=True):
        if not fixture['stage'] == previous['stage'] == original['stage'] == current['stage'] == scalars['stage']:
            raise ValueError('Prescribed stage identity changed')
        for field in ('initial42', 'targetNode40', 'grid', 'portRatio', 'normalizationScale', 'mu'):
            if numeric_identity(fixture[field]) != numeric_identity(previous[field]):
                raise ValueError('Original finite stage input changed: '+field)
        if len(current['state']) != 42 or packed(current['state']) != packed(original['state']):
            raise ValueError('Complete output identity failed')
        if len(current['events']) != len(original['events']):
            raise ValueError('Original trace length differs')
        for left, right in zip(current['events'], original['events'], strict=True):
            if numeric_identity(left) != numeric_identity(right):
                raise ValueError('An original numerical operand or branch judgment differs')
        event_counts = {}
        for event in current['events']:
            event_counts[event['event']] = event_counts.get(event['event'], 0)+1
        if event_counts['root_return'] != scalars['root_calls'] or scalars['root_calls'] != 64:
            raise ValueError('The original 64 RK field/root calls are not all present')
        state_hash = hashlib.sha256(packed(current['state'])).hexdigest()
        if state_hash != original['state42_sha256'] or state_hash != scalars['output42_float64_sha256']:
            raise ValueError('The original output byte hash differs')
        stages[str(fixture['stage'])] = dict(**scalars, original_operand_and_judgment_events=event_counts,
            canonical_numeric_trace_sha256=trace_digest(current['events']),
            stage_input42_sha256=hashlib.sha256(packed(fixture['initial42'])).hexdigest(),
            target40_sha256=hashlib.sha256(packed(fixture['targetNode40'])).hexdigest())
        total_events += len(current['events'])
        total_root_calls += scalars['root_calls']
    resources = {}
    for name, path, logfile in (('export', a.export_resource, a.export_log), ('float', a.float_resource, a.float_log)):
        data = load(path)
        if data['status'] != 'observed_terminal' or data['child_returncode'] != 0:
            raise ValueError('Actual successful terminal observation required: '+name)
        resources[name] = dict(identity=identity(path), log=identity(logfile), metadata=scalar_tree(data),
                               actual_command=data['command'])
    rules = dict(cs['root_rules'])
    factors = rules.pop('halving_factors')
    rules['halving_count'] = len(factors)
    rules['halving_factors_float64_sha256'] = hashlib.sha256(packed(factors)).hexdigest()
    record = dict(
        scope='Numerical/implementation evidence: the new frozen-coefficient evaluator in float arithmetic reproduces all three original 42-component flow outputs and the captured original root/RK operands and judgments exactly. No MP run is included.',
        collector=identity(__file__), collector_helpers={name: sha(Path(__file__).with_name(name)) for name in
            ('record_fixed_actual.py', 'record_tail_initialization.py')},
        evaluator=identity(source), bridge_sha256=fs['bridge_sha256'],
        original_failed_state=cs['input'], inherited_fixture=cs['fixture'],
        inherited_original_full_jacobian_output=cs['original_output'],
        capsule_summary=identity(a.capsule_summary), float_summary=identity(a.float_summary),
        coefficient_capsule=cs['coefficients'], original_reference=cs['reference'], float_output=fs['raw'],
        source_sha256=cs['source_sha256'], additional_original_root_sources=cs['additional_original_root_sources'],
        original_trace_source=cs['traced_source'], declared_trace_patch_sha256=cs['patch_identity'],
        trace_patch_exact_reconstruction=True,
        original_discretization={key: cs[key] for key in ('modes', 'spacing', 'quadrature',
            'independent_quadrature_nodes', 'steps', 'original_tail_gate')},
        original_root_rules=rules, frozen_coefficient_convention=fs['coefficient_convention'],
        trace_scope='Captured RK entry labels, complete root initial state/target/L, evaluate-L operands and final moments, every ordered D/S/A domain decision, every SPD diagonal positivity decision, original err/scale/tolerance stop, attempted halving factor/trial/acceptance, and possible fallback operands. This records executed paths, not exhaustive branch coverage.',
        all_outputs42_bitwise_identical=True, all_recorded_operands_and_judgments_bitwise_identical=True,
        total_root_calls=total_root_calls, total_trace_events=total_events, named_stages=stages,
        all_42_include_two_mean_components=True, numerical_tolerance_used_for_identity=0,
        source_checkpoint_states_changed=False, production_source_changed=False,
        whole_tail_evaluated=False, nonlinear_tail_solver_invoked=False, multiprecision_executed=False,
        conclusion='The independently expressed finite state evaluator has an exact original-arithmetic baseline on the three prescribed fixtures. This supports a subsequent isolated MP readout but is not a new tail solution or a continuous ODE error bound. MP root branches may differ under identical tests; any later run must report their actual counts and residuals.',
        resources=resources,
        data_policy='Only compact scalar identity evidence and file/source hashes are published. Geometry/coefficients, trig tables, all states and full traces remain scratch-only.')
    text = json.dumps(record, ensure_ascii=False, indent=2)+'\n'
    if len(text.encode()) >= 100000:
        raise ValueError('Compact record must stay under100KB')
    a.out.write_text(text)
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out), total_events=total_events)))


if __name__ == '__main__':
    main()
