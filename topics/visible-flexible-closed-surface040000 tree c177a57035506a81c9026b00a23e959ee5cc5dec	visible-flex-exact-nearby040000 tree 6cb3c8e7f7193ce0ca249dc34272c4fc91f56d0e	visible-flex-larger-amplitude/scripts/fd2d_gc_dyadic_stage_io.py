"""Explicit same-function transport across the R170 search-domain change."""
import json
from pathlib import Path
from types import SimpleNamespace
from fd2d_gc_archive_arrays import identity
from fd2d_gc_selected_normal_io import load_selected_normal
from fd2d_gc_schur_stage_io import factor_binding


def assert_same_finite_function(parent,child):
    keys=('input_npz_sha256','input_npz_bytes','packed_vector','candidate_sha256',
          'reference_inlet_sha256','mathematical_settings','actual_saved_definition_arrays',
          'implementation_sources','parent_objective_source_sha256','finite_rule','grouped_rule_definition')
    for key in keys:
        if parent[key]!=child[key]:
            raise ValueError('A mathematical input changed during domain-only transport: '+key)
    if not child.get('finite_objective_unchanged_by_selected_domain'):
        raise ValueError('Require the explicit genuine R170 context')
    return dict(same_actual_field_and_finite_function=True,checked_keys=list(keys),
        old_global_tail_box_replaced_by_exact_dyadic_rows=True,
        new_source_and_domain_identity_preserved=True,
        no_F_J_normal_or_Schur_recomputed=True)


def selected_normal(context):
    root=Path(context.request['cache_dir']);path=root/'normal-reference.json'
    record=json.loads(path.read_text())
    if record.get('schema')!='fd2d-R170-domain-only-normal-reference-v1':
        raise ValueError('Require an explicitly transported same-function normal')
    if record['finite_goal']!=context.binding:
        raise ValueError('Changed R170 context or domain')
    assert_same_finite_function(record['parent_finite_goal'],context.binding)
    entity=record['normal_manifest'];actual=identity(entity['path'])
    if any(actual[k]!=entity[k] for k in ('sha256','bytes')):
        raise ValueError('Original immutable normal changed')
    old=record['transport_binding']
    bound=old.get('finite_goal',old.get('common',{}).get('field_and_finite_objective'))
    if bound!=record['parent_finite_goal']:
        raise ValueError('The original matrix has a different field/finite goal')
    return Path(entity['path']),old,dict(kind=record['schema'],reference=identity(path),
        same_unscaled_normal_used_under_explicit_new_constraints=True)


def parent_factor_binding(context,normal_manifest,damping,solver_source,producer_source):
    record=json.loads((Path(context.request['cache_dir'])/'normal-reference.json').read_text())
    assert_same_finite_function(record['parent_finite_goal'],context.binding)
    return factor_binding(SimpleNamespace(binding=record['parent_finite_goal']),normal_manifest,
        damping,solver_source,producer_source)
