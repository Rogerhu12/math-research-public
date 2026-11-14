#!/usr/bin/env python3
"""Use the current-anchor loader in the frozen same-g complete-mean comparison.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only the saved-field loader and its explicit provenance change. Actual modes
remain dynamic; M32/M40 mean counts are 1552/1936. Prepare-only reads no coarse
or future fine field and preserves every original same-g acceptance gate.
"""
import ast
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
PINS = {
    'strong_sameg_actual_comparison_complete_mean.py':
        '186175bb540800a7a4e6c0cde8c480dc87639d932c70214d630fd7c0879469bb',
    'strong_frontload_anchor_loader_adapter.py':
        'aa32079179e20a95493cd911185ea69e7df2b4d5b150a713597e9d2f9fd73c86',
    'strong_monotone_initial_speed_anchor.py':
        '583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    for name, expected in PINS.items():
        if sha(HERE/name) != expected:
            raise ValueError('Frozen current-anchor comparison dependency changed: '+name)
    from strong_frontload_anchor_loader_adapter import build
    path = HERE/'strong_sameg_actual_comparison_complete_mean.py'
    original = path.read_text()
    source = original
    edits = [
        ("        mean_counts_for_requested_spectral_pair={'M28':1360,'M32':1552},\n",
         "        mean_counts_for_prepared_spectral_examples={'M32':1552,'M40':1936},\n"
         "        mode_counts_read_from_each_actual_accepted_field=True,\n"),
        ("    if own.prepare_only:\n",
         "    loader_namespace,anchor_provenance=ANCHOR_LOADER_BUILD('audit',CURRENT_ANCHOR_ENTRY_FILE)\n"
         "    identity['frontload_anchor_adapter']=anchor_provenance\n"
         "    identity['complete_mean_anchor_frontend']=COMPLETE_MEAN_ANCHOR_PROVENANCE\n"
         "    if own.prepare_only:\n"),
        ("    loader_spec=importlib.util.spec_from_file_location('sameg_initial_laws_saved_loader',own.source_dir/'strong_initial_laws_interior_fullmean_audit.py')\n"
         "    loader=importlib.util.module_from_spec(loader_spec);loader_spec.loader.exec_module(loader)\n",
         "    # The original loader was prepared above with its explicit current-anchor import.\n"),
        ("    namespace['module']=loader.install_audit_loader(namespace['module'],observations)\n",
         "    namespace['module']=loader_namespace['install_audit_loader'](namespace['module'],observations)\n"),
    ]
    for before, after in edits:
        if source.count(before) != 1:
            raise ValueError('A unique frozen loader/provenance site changed')
        source = source.replace(before, after, 1)
    ast.parse(source)
    reverse = source
    for before, after in reversed(edits):
        if reverse.count(after) != 1:
            raise ValueError('The source adaptation is not uniquely reversible')
        reverse = reverse.replace(after, before, 1)
    if reverse != original:
        raise ValueError('An unlisted comparison formula changed')
    provenance = dict(source_sha256=sha(__file__), pinned_sources=PINS,
        transformed_complete_mean_wrapper_sha256=hashlib.sha256(source.encode()).hexdigest(),
        exact_reverse_recovers_original_complete_mean_wrapper=True,
        actual_sameg_gate_chart_gauge_tail_configuration_and_quintic_formulas_unchanged=True,
        full_mean_formula='max(512,16*(3*M+1)) independently for each accepted field',
        actual_mode_counts_are_not_hardcoded=True,
        original_angular_grid_Gauss6_all_meshes_and_material_jets_retained=True,
        loaded_future_fine_field_in_prepare_only=False)
    namespace = dict(__file__=str(Path(__file__).resolve()),
        __name__='fresh_current_anchor_sameg_complete_mean',
        ANCHOR_LOADER_BUILD=build, CURRENT_ANCHOR_ENTRY_FILE=Path(__file__).resolve(),
        COMPLETE_MEAN_ANCHOR_PROVENANCE=provenance)
    exec(compile(source, '<frozen-fullmean-sameg-with-current-anchor>', 'exec'), namespace)
    namespace['EXPECTED'].update(PINS)
    namespace['main']()


if __name__ == '__main__':
    main()
