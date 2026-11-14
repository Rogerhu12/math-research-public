"""Select an explicitly reused or freshly computed actual R170 normal."""
import json
from pathlib import Path
from fd2d_gc_dyadic_stage_io import selected_normal as domain_reused_normal, parent_factor_binding
from fd2d_gc_selected_normal_io import selected_normal as fresh_or_derived_normal,load_selected_normal
from fd2d_gc_schur_stage_io import factor_binding as original_factor_binding
from fd2d_gc_dyadic_normal_tile_io import partition_context,merged_normal_binding


def selected_normal(context):
    root=Path(context.request['cache_dir']);reference=root/'normal-reference.json'
    if reference.exists():
        schema=json.loads(reference.read_text()).get('schema')
        if schema=='fd2d-R170-domain-only-normal-reference-v1':return domain_reused_normal(context)
        return fresh_or_derived_normal(context)
    _,plan,common,_=partition_context(context)
    return root/'normal-partitioned'/'manifest.json',merged_normal_binding(common,plan),dict(kind='fresh_R170_actual_row_partition')


def selected_factor_binding(context,manifest,damping,solver,producer):
    path=Path(context.request['cache_dir'])/'normal-reference.json'
    if path.exists() and json.loads(path.read_text()).get('schema')=='fd2d-R170-domain-only-normal-reference-v1':
        return parent_factor_binding(context,manifest,damping,solver,producer)
    return original_factor_binding(context,manifest,damping,solver,producer)
