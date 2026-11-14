#!/usr/bin/env python3
"""Fresh provider-only anchor adapters for geometry and actual saved loaders.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Each original loader and all its mathematical/acceptance formulas are frozen.
Exactly its frontload import is redirected to the separately identified
current-anchor hook. Both the original and repaired hook identities and all
adapter sources are carried into actual result provenance.
"""
import ast
import hashlib
from pathlib import Path

ROLES={
 'geometry':('root_actual_geometry_field_initial_laws.py','7efa4f617321c5832b59b8ee4c451fc53838ddee61025581b6e5eeda459b1b09'),
 'audit':('strong_initial_laws_interior_fullmean_audit.py','35155b17516ce3ff72ddfc957894e53cbd2c7a4a6707d57e62887a8d72e4fbe0'),
 'fixed_view':('strong_initial_laws_freeze_design_view.py','785442ffad4a72f9671aef285dae4a4bfc11f410b2cec54027cd913a09a61ab3'),
}
ANCHOR_SHA='583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc'
ORIGINAL_HOOK_SHA='12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def build(role,wrapper):
    wrapper=Path(wrapper).resolve();here=wrapper.parent
    name,wanted=ROLES[role];source=(here/name).read_text()
    if sha(here/name)!=wanted or sha(here/'strong_monotone_initial_speed_anchor.py')!=ANCHOR_SHA or sha(here/'strong_monotone_initial_speed.py')!=ORIGINAL_HOOK_SHA:
        raise ValueError('Pinned original loader or anchor hook changed')
    original=source;edits=[]
    def edit(before,after):
        nonlocal source
        if source.count(before)!=1:raise ValueError('Provider-only loader edit is not unique: '+before)
        changed=source.replace(before,after,1)
        if changed.count(after)!=1 or changed.replace(after,before,1)!=source:
            raise ValueError('Provider-only loader edit is not exactly reversible')
        source=changed;edits.append((before,after))
    edit('import strong_monotone_initial_speed as frontload','import strong_monotone_initial_speed_anchor as frontload')
    tree=ast.parse(source)
    expected=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='EXPECTED' for t in n.targets))
    lines=source.splitlines(keepends=True);anchor=''.join(lines[:expected.end_lineno])
    extras={name:wanted,'strong_monotone_initial_speed_anchor.py':ANCHOR_SHA,
        Path(__file__).name:sha(__file__),wrapper.name:sha(wrapper)}
    addition='\nEXPECTED.update('+repr(extras)+')\n'
    edit(anchor,anchor+addition)
    if role=='geometry':
        before="'strong_pulse_augmented_core.py','strong_initial_speed_pulse.py','strong_monotone_initial_speed.py')\\n"
        after="'strong_pulse_augmented_core.py','strong_initial_speed_pulse.py','strong_monotone_initial_speed.py','strong_monotone_initial_speed_anchor.py','strong_frontload_anchor_loader_adapter.py','"+wrapper.name+"')\\n"
        edit(before,after)
        edit("    return entry,namespace['main'],record\n",
             "    record['frontload_anchor_adapter']=ANCHOR_ADAPTER_PROVENANCE\n    return entry,namespace['main'],record\n")
    elif role=='audit':
        edit("    result['initial_laws_provider_adapter'] = dict(\n",
             "    result['frontload_anchor_adapter']=ANCHOR_ADAPTER_PROVENANCE\n    result['initial_laws_provider_adapter'] = dict(\n")
    else:
        edit('    return source, provenance\n',
             "    provenance['frontload_anchor_adapter']=ANCHOR_ADAPTER_PROVENANCE\n    return source, provenance\n")
    ast.parse(source)
    reverse=source
    for before,after in reversed(edits):
        if reverse.count(after)!=1:raise ValueError('Reverse source anchor changed')
        reverse=reverse.replace(after,before,1)
    if reverse!=original:raise ValueError('Unlisted original source modification')
    provenance=dict(scope=__doc__,role=role,original_loader_sha256=wanted,
        original_monotone_hook_sha256=ORIGINAL_HOOK_SHA,current_anchor_hook_sha256=ANCHOR_SHA,
        loader_adapter_source_sha256=sha(__file__),entry_source_sha256=sha(wrapper),
        transformed_loader_sha256=hashlib.sha256(source.encode()).hexdigest(),
        exact_reverse_recovers_original_loader=True,
        mathematical_geometry_mean_quintic_and_acceptance_formulas_changed=False,
        actual_hook_source_fingerprints_explicit_in_result=True,
        installation_order=['original angle','original pulse','fresh current-anchor frontload'],
        original_zero_weight_arithmetic_delegated=True,old_frozen_sources_modified=False)
    namespace=dict(__file__=str(wrapper),__name__='fresh_anchor_'+role,
        ANCHOR_ADAPTER_PROVENANCE=provenance)
    exec(compile(source,'<original-'+role+'-with-explicit-current-anchor-provider>','exec'),namespace)
    for dependency,digest in namespace['EXPECTED'].items():
        if sha(here/dependency)!=digest:raise ValueError('A declared frozen loader dependency changed: '+dependency)
    return namespace,provenance
