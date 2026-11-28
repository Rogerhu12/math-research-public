#!/usr/bin/env python3
"""Paid third activity for one own fixed-QR final physical-H closed map.

The original complete field, interval quadrature, durable leaf write, tail
flux and rational combination are reused. Only the genuine own fixed source
entry and the already constructed own fixed atlas receipt replace anchor
contracts. No old positive interval, native solve or new cap is introduced.
An interval containing zero remains unpaid and does not imply congruence.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import copy
import hashlib
import inspect
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import qr_fixed_geometry_entry as geometry
from qr_fixed_geometry_entry import reader, REF, checked
import qr_fixed_actual_prefix_continuous as fixed_continuous

SCHEMA = 'own-fixed-QR-actual-third-activity-v1'
GEOMETRY_ENTRY_SHA = 'f7d03306323bf11f5ab83e2e22926932c7aff0322621ec94d413383c286fdef0'
REVIEWED = {
    'qr_cartesian_third_activity_moment.py':
        '33143db55427c527b7e5bea9916009a0d484f95cc1dfcfd60b0a7039b322e164',
    'qr_cartesian_third_activity_moment_durable.py':
        'a5fad89bcaf381261a554ae43c89bd44e50b1c7c8b6423d61bb6fca8522719bd',
    'tail_third_activity_flux_bound.py':
        '2dcaf9cfde8a6923c0ac0e32a81ae7f5356d12025239b467c7ad7ab3a94767f7',
    'qr_combine_closed_third_activity.py':
        'af6059bc941c7eba594a104673246c4af886caf21ac93c0b40b92a407359ee98',
}


def setup(args, phase):
    if reader.sha(geometry.__file__) != GEOMETRY_ENTRY_SHA:
        raise ValueError('The reviewed own fixed whole-geometry source entry changed')
    return geometry.setup(args.source_run, 'activity-'+phase)


def load_math(name):
    path = HERE/name
    if reader.sha(path) != REVIEWED[name]:
        raise ValueError('The unchanged actual activity proof source changed: '+name)
    return reader.module('_own_fixed_activity_'+name.replace('.', '_'), path)


def metadata(state, phase):
    return dict(own_fixed_activity_schema=SCHEMA, own_fixed_activity_phase=phase,
        source=REF(__file__), actual_source_kind=reader.SOURCE_KIND,
        actual_fixed_source_verified=True,
        own_fixed_source_contract=copy.deepcopy(state['context'].payload),
        actual_fixed_gate_provenance=copy.deepcopy(state['provenance']),
        final_physical_height_binding=state['view']['height_reference'],
        full_height_packet=state['view']['packet'],
        final_physical_height_is_definition=True, raw_candidate_used_as_final_height=False,
        source_record_relabelled_or_rewritten=False, old_other_field_bounds_reused=False)


def require_activity(state, value, phase):
    for key, wanted in metadata(state, phase).items():
        if value.get(key) != wanted:
            raise ValueError('The same own fixed activity source is required: '+key)


def replace_one(text, before, after):
    if text.count(before) != 1:
        raise ValueError('The reviewed activity entry section changed: '+before[:120])
    return text.replace(before, after, 1)


def make_prefix_main(core, context, new_class, cut_class, write, durable_leaf):
    """Retain every field/integral statement and add durable receipt calls."""
    original = inspect.getsource(core.main)
    changed = replace_one(original,
        '    ap.add_argument("--coupling-summary", type=Path, required=True)\n', '')
    start = '    coupled.check_reviewed_algebra()\n'
    end = '    report = dict(schema=SCHEMA, status="loading_actual_complete_moment_source", scope=__doc__,\n'
    if changed.count(start) != 1 or changed.count(end) != 1:
        raise ValueError('The original moment source-initialization block changed')
    before, rest = changed.split(start)
    replaced, after = rest.split(end)
    changed = before+'    context = _own_context\n    write = _own_write\n'+end+after
    first = '        if context is None:\n'
    last = '        moment = MomentVerifier(verifier, args.bundle is not None)\n'
    if changed.count(first) != 1 or changed.count(last) != 1:
        raise ValueError('The original complete-field verifier source entry changed')
    before, rest = changed.split(first)
    verifier_entry, after = rest.split(last)
    changed = before+(
        '        verifier = _own_cut_class(tables, args.bundle, out, context, args.cut_width)\n')+last+after
    changed = replace_one(changed,
        'source_kind=(coupled.SOURCE_KIND if context else "actual_original_R53_design")',
        'source_kind=_own_source_kind')
    leaf_marker = '                exact_cover.append((left, right))\n'
    changed = replace_one(changed, leaf_marker, leaf_marker+
        '                _own_durable_leaf(out, report, len(leaves), row, total, write)\n')
    core_marker = '        report.update(core_flux=core_report, core_flux_certified=True)\n'
    changed = replace_one(changed, core_marker, core_marker+'        write(out/"summary.json", report)\n')
    namespace = dict(vars(core), __file__=str(Path(__file__).resolve()), __doc__=__doc__,
        SCHEMA='own-fixed-QR-Cartesian-third-activity-core-flux-v1',
        _own_context=context, _own_write=write, _own_new_class=new_class,
        _own_cut_class=cut_class, _own_source_kind=reader.SOURCE_KIND,
        _own_durable_leaf=durable_leaf)
    exec(compile(changed, str(Path(__file__).resolve())+'::original_moment_main', 'exec'), namespace)
    receipt = dict(original_main_sha256=hashlib.sha256(original.encode()).hexdigest(),
        generated_main_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        original_source_initialization_section_sha256=hashlib.sha256((start+replaced).encode()).hexdigest(),
        original_verifier_entry_section_sha256=hashlib.sha256((first+verifier_entry).encode()).hexdigest(),
        field_extraction_density_interval_quadrature_and_complete_loop_unchanged=True,
        source_entry_and_output_identity_changed=True, completed_leaf_durable_calls_added=True)
    return namespace['main'], receipt


def prefix(args):
    state = setup(args, 'prefix')
    context = state['context']
    geometry.scratch_out(state, args.outdir)
    table = checked(REF(args.tables))
    if Path(table['source_run']).resolve() != state['source_run']:
        raise ValueError('The complete moment tables belong to another actual fixed return')
    context.require_report(table)
    reader.validate_bundle_binding(checked(REF(args.bundle)), state['record'],
        state['view'], state['provenance'])
    bases = fixed_continuous.proof_modules(context)
    new_class, cut_class = fixed_continuous.metric_classes(bases)
    core = load_math('qr_cartesian_third_activity_moment.py')
    durable = load_math('qr_cartesian_third_activity_moment_durable.py')
    if core.metric is not bases['metric'] or core.cut_metric is not bases['cut']:
        raise ValueError('The original field extractor is not using the actual fixed proof providers')
    if REF(durable.original.__file__) != REF(core.__file__):
        raise ValueError('The original durable writer references another moment algebra')
    execution = {}

    def own_write(path, value):
        value = dict(value)
        value.update(metadata(state, 'prefix'),
            frozen_mathematical_entry=REF(core.__file__), durable_entry=REF(__file__),
            reused_durable_storage_source=REF(durable.__file__),
            actual_moment_source_adaptation=execution,
            original_geometry_source_or_gates_modified=False)
        context.save(path, value)

    entry, receipt = make_prefix_main(core, context, new_class, cut_class,
                                     own_write, durable.durable_leaf)
    execution.update(receipt)
    context.execution = dict(entry=REF(__file__), phase='own-fixed-third-activity',
        reused_mathematical_entry=REF(core.__file__), reused_durable_writer=REF(durable.__file__),
        own_fixed_gate_keeps_original_KIND=True, **receipt)
    argv = [str(Path(__file__).resolve())+'::prefix']
    for key in ('tables', 'outdir', 'bundle', 'cut_width', 'radial_parts'):
        argv.extend(['--'+key.replace('_','-'), str(getattr(args,key))])
    previous = sys.argv
    try:
        sys.argv = argv
        entry()
    finally:
        sys.argv = previous
    return checked(REF(args.outdir/'summary.json')), 0


def tail(args):
    state = setup(args, 'tail')
    geometry.scratch_out(state, args.outdir)
    place = checked(REF(args.placement_report))
    height = checked(place['absolute_height'])
    geometry.require_own(state, place, 'placement')
    geometry.require_own(state, height, 'placement')
    geometry.require_own(state, checked(height['physical_R_identity']), 'radius')
    if (height['prefix_source_run'] != REF(args.source_run)
            or height['accepted_packet'] != state['view']['packet']):
        raise ValueError('The complete placement is not this own final physical-height source')
    reader.validate_bundle_binding(checked(height['geometry_bundle']), state['record'],
        state['view'], state['provenance'])
    complete = checked(REF(args.complete_original_certificate))
    pipeline = state['scripts']/'resume_20261126/seam_run_tail_geometry_v2.py'
    if (reader.sha(pipeline) != geometry.ORIGINAL_PIPELINE_SHA
            or complete['source'] != REF(pipeline)):
        raise ValueError('The complete projected-disk proof must be the original pipeline of this fixed source')
    core = load_math('tail_third_activity_flux_bound.py')
    original_write = core.write
    original_main = hashlib.sha256(inspect.getsource(core.main).encode()).hexdigest()

    def own_write(path, value):
        value = dict(value)
        value.update(metadata(state, 'tail'), reused_original_flux_source=REF(core.__file__),
            unchanged_original_main_sha256=original_main,
            all_original_projection_inventory_and_flux_formulas_reused=True)
        original_write(path, value)

    core.write = own_write
    argv = [str(core.__file__)]
    for key in ('placement_report', 'complete_original_certificate', 'outdir'):
        argv.extend(['--'+key.replace('_','-'), str(getattr(args,key))])
    previous = sys.argv
    try:
        sys.argv = argv
        core.main()
    finally:
        sys.argv = previous
    return checked(REF(args.outdir/'summary.json')), 0


def make_combine_main(core, source_gate, moment_gate, output):
    """The exact coverage, interval addition and R67 conclusion stay unchanged."""
    original = inspect.getsource(core.main)
    changed = replace_one(original,
        '    parser.add_argument("--coupling-summary", type=Path, required=True)\n', '')
    start = "    context = CoupledContext(args.coupling_summary, 'combine-closed-third-activity')\n"
    end = "    if (tail['status'] != 'actual_complete_tail_and_deep_disk_third_activity_flux_bounded'\n"
    if changed.count(start) != 1 or changed.count(end) != 1:
        raise ValueError('The reviewed full activity source gate changed')
    before, rest = changed.split(start)
    old_gate, after = rest.split(end)
    changed = before+'    context, binding = _own_source_gate(prefix, tail, geometry, source)\n'+end+after
    start = "    if (prefix['frozen_mathematical_entry'] != ref(Path(__file__).with_name('qr_cartesian_third_activity_moment.py'))\n"
    end = "    for item in (source, prefix['physical_file'], prefix['defining_jets'],\n"
    if changed.count(start) != 1 or changed.count(end) != 1:
        raise ValueError('The reviewed complete moment entry identity check changed')
    before, rest = changed.split(start)
    old_entry, after = rest.split(end)
    changed = before+'    _own_moment_gate(prefix)\n'+end+after
    if changed.count("geometry['actual_query']") != 2:
        raise ValueError('The original complete-map receipt locations changed')
    changed = changed.replace("geometry['actual_query']", "geometry['actual_complete_map_definition']")
    changed = replace_one(changed,
        "accepted_packet=tail['accepted_packet'], actual_query=geometry['actual_complete_map_definition'],",
        "accepted_packet=tail['accepted_packet'], actual_complete_map_definition=geometry['actual_complete_map_definition'],")
    changed = replace_one(changed,
        "        actual_source_kind=SOURCE_KIND,actual_coupled_source_verified=True,\n"
        "        coupling_summary=context.payload['coupling_summary'],\n",
        "        actual_source_kind=SOURCE_KIND,actual_fixed_source_verified=True,\n")
    changed = replace_one(changed,
        '    args.out.parent.mkdir(parents=True, exist_ok=True)\n',
        '    result = _own_output(result)\n    args.out.parent.mkdir(parents=True, exist_ok=True)\n')
    namespace = dict(vars(core), __file__=str(Path(__file__).resolve()), __doc__=__doc__,
        SOURCE_KIND=reader.SOURCE_KIND, _own_source_gate=source_gate,
        _own_moment_gate=moment_gate, _own_output=output)
    exec(compile(changed, str(Path(__file__).resolve())+'::original_activity_combiner', 'exec'), namespace)
    receipt = dict(original_main_sha256=hashlib.sha256(original.encode()).hexdigest(),
        generated_main_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        original_source_gate_sha256=hashlib.sha256(old_gate.encode()).hexdigest(),
        original_moment_source_gate_sha256=hashlib.sha256(old_entry.encode()).hexdigest(),
        exact_full_leaf_coverage_accumulation_column_and_phase_formulas_unchanged=True,
        receipt_is_actual_own_map_definition_not_sampled_query=True)
    return namespace['main'], receipt


def combine(args):
    state = setup(args, 'combine')
    geometry.scratch_out(state, args.out)
    core = load_math('qr_combine_closed_third_activity.py')
    execution = {}

    def source_gate(pref, flux, whole, source):
        require_activity(state, pref, 'prefix')
        require_activity(state, flux, 'tail')
        geometry.require_own(state, whole, 'geometry')
        state['context'].require_report(pref)
        definition = checked(whole['actual_complete_map_definition'])
        geometry.require_own(state, definition, 'definition')
        if (source != REF(args.source_run) or flux['accepted_packet'] != state['view']['packet']
                or whole['accepted_packet'] != state['view']['packet']
                or pref['bundle'] != whole['geometry_bundle']
                or definition['geometry_bundle'] != whole['geometry_bundle']
                or definition['source_run'] != source):
            raise ValueError('The complete own prefix, tail and closed field have different physical-H sources')
        reader.validate_bundle_binding(checked(whole['geometry_bundle']), state['record'],
            state['view'], state['provenance'])
        return state['context'], state['view']

    def moment_gate(pref):
        if (pref['frozen_mathematical_entry'] != REF(HERE/'qr_cartesian_third_activity_moment.py')
                or pref['frozen_mathematical_entry']['sha256'] != REVIEWED['qr_cartesian_third_activity_moment.py']
                or pref['durable_entry'] != REF(__file__)
                or pref['reused_durable_storage_source'] != REF(HERE/'qr_cartesian_third_activity_moment_durable.py')
                or pref['reused_durable_storage_source']['sha256'] != REVIEWED['qr_cartesian_third_activity_moment_durable.py']):
            raise ValueError('The true own source did not execute the frozen complete moment/durable formulas')

    def output(value):
        value = dict(value)
        value.update(metadata(state, 'combine'), reused_original_combiner=REF(core.__file__),
                     exact_source_adaptation=execution)
        return value

    entry, receipt = make_combine_main(core, source_gate, moment_gate, output)
    execution.update(receipt)
    argv = [str(Path(__file__).resolve())+'::combine']
    for key in ('prefix_moment_report', 'tail_flux_report', 'closed_geometry_report', 'out'):
        argv.extend(['--'+key.replace('_','-'), str(getattr(args,key))])
    previous = sys.argv
    try:
        sys.argv = argv
        entry()
    finally:
        sys.argv = previous
    return checked(REF(args.out)), 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='phase', required=True)
    p = commands.add_parser('prefix')
    for name in ('source-run', 'tables', 'bundle', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--cut-width', type=float, required=True)
    p.add_argument('--radial-parts', type=int, default=1)
    p = commands.add_parser('tail')
    for name in ('source-run', 'placement-report', 'complete-original-certificate', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p = commands.add_parser('combine')
    for name in ('source-run', 'prefix-moment-report', 'tail-flux-report', 'closed-geometry-report', 'out'):
        p.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    result, code = globals()[args.phase](args)
    print(json.dumps(dict(status=result['status'], phase=args.phase,
                         actual_source_kind=reader.SOURCE_KIND)), flush=True)
    raise SystemExit(code)


if __name__ == '__main__':
    main()
