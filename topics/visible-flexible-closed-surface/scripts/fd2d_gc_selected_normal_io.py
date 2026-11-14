"""Explicitly select a freshly merged or independently gap-derived normal."""
import json
from pathlib import Path
from fd2d_gc_archive_arrays import identity
from fd2d_gc_grouped_normal_tile_io import partition_context,merged_normal_binding


def selected_normal(context):
    root=Path(context.request['cache_dir']);record=root/'normal-reference.json'
    if not record.exists():
        _,plan,common,_=partition_context(context)
        return root/'normal-partitioned'/'manifest.json',merged_normal_binding(common,plan),dict(kind='fresh_exact_row_partition')
    description=json.loads(record.read_text())
    if description.get('schema') not in ('fd2d-explicit-derived-normal-reference-v1',
            'fd2d-explicit-piecewise-merged-normal-reference-v1'):
        raise ValueError('Unknown derived normal reference')
    if description['finite_goal']!=context.binding:
        raise ValueError('Derived normal is for a different exact field or finite goal')
    saved=description['normal_manifest'];actual=identity(saved['path'])
    if any(actual[k]!=saved[k] for k in ('sha256','bytes')):
        raise ValueError('Closed derived normal manifest changed')
    expected=description['transport_binding']
    goal=expected.get('finite_goal',expected.get('common',{}).get('field_and_finite_objective'))
    if goal!=context.binding:
        raise ValueError('Derived transport does not bind this actual field')
    return Path(saved['path']),expected,dict(kind=description['schema'],reference=identity(record))


def load_selected_normal(problem,manifest,*,expected_binding):
    schema=json.loads(Path(manifest).read_text()).get('schema')
    if schema=='fd2d-offline-piecewise-ordered-normal-v1':
        from fd2d_gc_piecewise_normal_transport import load_piecewise_normal
        return load_piecewise_normal(problem,manifest,expected_binding=expected_binding)
    from fd2d_gc_normal_checkpoint import load_normal_checkpoint
    return load_normal_checkpoint(problem,manifest,expected_binding=expected_binding)
