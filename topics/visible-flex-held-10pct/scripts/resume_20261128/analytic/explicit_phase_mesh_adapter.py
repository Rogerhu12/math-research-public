#!/usr/bin/env python3
"""Keep each original full-map export and supply an explicit rational phase.

Only CLI time semantics, the documented circle-frame parameter contract and
their provenance are changed. The original actual-source/full-H gates, every
saved mode, geometry evaluation, topology and strict 5 MB PLY rule remain.
Old executed sources stay byte-identical. No source KIND is relabelled.
"""
import hashlib
import importlib.util
import inspect
from pathlib import Path
import sys

import material_circle_phase_contract as phase_api

HERE = Path(__file__).resolve().parent
BASE = {
    'chord': ('chord_export_actual_closed_mesh.py',
        '3ab5594ad5098df5db1300b7add42a2ee1bf9c44540cc9b18e11b6c36d8dde7e'),
    'fixed': ('fixed_actual_export_closed_mesh.py',
        '655801c4f99bcb5a6936cae4d6db81b8600c9268276924f5cfbb164994f119cf'),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def prepare(kind, entry):
    name, expected = BASE[kind]
    source = HERE/name
    if sha(source) != expected:
        raise ValueError('The bound original full-map exporter changed: '+name)
    spec = importlib.util.spec_from_file_location('_explicit_phase_'+kind,source)
    old = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = old
    spec.loader.exec_module(old)
    original = inspect.getsource(old.main)
    modified = original
    edits = []

    def change(before, after, count=1):
        nonlocal modified
        if modified.count(before) != count:
            raise ValueError('The original explicit time integration point changed: '+before)
        modified = modified.replace(before,after)
        edits.append(dict(before=before,after=after,occurrences=count))

    change('    args = parser.parse_args()',
        "    parser.add_argument('--phase-end',type=Q,required=True)\n"
        "    parser.add_argument('--held-width',type=Q,default=Q(27,50))\n"
        "    args = parser.parse_args()\n"
        "    phase_end, held_width = args.phase_end, args.held_width\n"
        "    if phase_end <= 0 or held_width <= 0:\n"
        "        raise ValueError('Use positive exact phase-end and held-width')")
    change("phase_definition='alpha(t)=(9/20)*t, exact real expression'",
        "phase_definition=f'alpha(t)=({phase_end})*t, exact real expression'")
    if kind == 'fixed':
        change('Q(9,20)*t','phase_end*t',2)
        change("frame = mesh.held_frame(value) if args.frame == 'held' else None",
            "frame = phase_api.held_frame(value,phase_end,held_width,mesh.circle) if args.frame == 'held' else None")
        value = 'value'
    else:
        change('Q(9, 20)*t','phase_end*t',2)
        change("frame = held_frame(model) if args.frame == 'held' else None",
            "frame = phase_api.held_frame(model,phase_end,held_width,circle) if args.frame == 'held' else None")
        value = 'model'
    change('alpha=9*t/20','alpha=({phase_end})*t')
    change('    try:\n',
        '    try:\n'
        f'        report.update(explicit_phase_contract=phase_api.describe({value},phase_end,held_width),\n'
        '            explicit_phase_adapter_sources=phase_adapter_sources,\n'
        '            original_main_sha256=phase_original_main_sha256,\n'
        '            executed_main_sha256=phase_executed_main_sha256)\n')
    if any(old_expression in modified for old_expression in ('Q(9,20)*t','Q(9, 20)*t','alpha=9*t/20')):
        raise ValueError('A stale hard-coded phase remains')
    original_sha = hashlib.sha256(original.encode()).hexdigest()
    executed_sha = hashlib.sha256(modified.encode()).hexdigest()
    entry = Path(entry).resolve()
    sources = {str(p.resolve()):sha(p) for p in
        (entry,Path(__file__),Path(phase_api.__file__),source)}
    old.__dict__.update(__file__=str(entry),phase_api=phase_api,
        phase_adapter_sources=sources,phase_original_main_sha256=original_sha,
        phase_executed_main_sha256=executed_sha)
    exec(compile(modified,str(entry)+'::explicit_phase_main','exec'),old.__dict__)
    return old, dict(kind=kind,source=str(source),source_sha256=expected,
        entry=str(entry),entry_sha256=sha(entry),adapter_sources=sources,
        original_main_sha256=original_sha,executed_main_sha256=executed_sha,
        exact_declared_replacements=edits,source_gates_changed=False,
        geometry_or_mesh_algebra_changed=False,real_accepted_field_used=False)


def run(kind, entry):
    module, _ = prepare(kind, entry)
    return module.main()
