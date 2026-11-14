"""Content-only bindings for a reusable field solve and bounded small QP."""
from pathlib import Path
from fd2d_gc_archive_arrays import identity


def content(path):
    value=identity(path)
    return dict(name=Path(path).name,bytes=value['bytes'],sha256=value['sha256'])


def factor_binding(context,normal_manifest,damping,solver_source,producer_source):
    here=Path(__file__).resolve().parent
    return dict(schema='fd2d-durable-original-normal-field-Schur-v1',
        finite_goal=context.binding,normal_manifest=content(normal_manifest),
        damping=float(damping),solver_source=content(solver_source),
        schur_search_source=content(here/'fd2d_gc_saved_schur_search.py'),
        producer_source=content(producer_source),binding_source=content(__file__),
        central_search_floor_not_part_of_factor_identity=True,
        physical_equations_or_finite_merit_changed=False)
