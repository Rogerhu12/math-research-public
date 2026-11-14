#!/usr/bin/env python3
"""Extend the exact lowered cap ledger to an entire real parameter tube.

The center's true radial coverage is not silently reused: the actual root
tube and exact sine endpoints must fit the union of all supplied germs.
"""
from fractions import Fraction
from flint import arb
from fourfold_phase_parameter_cap_budget import parameter_real_time_caps
from fourfold_phase_domain_cover_verify import Time
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_affine import sha


def complete_parameter_caps(models,reference,image_gate,q_gate):
    if not models:
        raise ValueError("complete actual parameter models required")
    uniform=hasattr(models[0],"half_width")
    if any(hasattr(model,"half_width")!=uniform for model in models):
        raise ValueError("cannot mix central and parameter-tube sources")
    doc=models[0].base.domain
    if uniform:
        intervals=[tuple(model.target.parameter_interval) for model in models]
        if any(row!=intervals[0] for row in intervals):
            raise ValueError("all neighboring germs need exactly the same real parameter interval")
    root=models[0].root
    # The actual physical sine branch and its monotonicity were already
    # verified by the exact full-angle domain.  Recompute its full parameter
    # radial image, not the center's binary endpoints or old cap lengths.
    a,b=map(Time.parse,doc["exact_time_endpoints"])
    endpoints=[root*a.value().sin(),root*b.value().sin()]
    lo=min(value.lower() for value in endpoints)
    hi=max(value.upper() for value in endpoints)
    cells=sorted(model.cell for model in models)
    if any(left[1]!=right[0] for left,right in zip(cells,cells[1:])):
        raise ValueError("supplied actual common spans leave a radial gap")
    if not exact_arb(cells[0][0])<=lo or not hi<=exact_arb(cells[-1][1]):
        raise ValueError("the actual parameter root tube needs an additional adjacent germ")
    result=parameter_real_time_caps(models,reference,image_gate,q_gate)
    result.update(source_sha256=sha(__file__),
        central_cap_algebra_source_sha256=sha(__import__("pathlib").Path(__file__).with_name("fourfold_phase_parameter_cap_budget.py")),
        center_parameter_only=not uniform,whole_real_parameter_tube=uniform,
        exact_parameter_interval=list(map(str,models[0].target.parameter_interval)),
        complete_parameter_radial_coverage=dict(proved=True,
            actual_root_tube=ball_record(root),
            full_radial_lower=ball_record(lo),full_radial_upper=ball_record(hi),
            complete_exact_common_spans=[list(map(str,cell)) for cell in cells],
            actual_parameter_crossing_geometry_recomputed=True))
    return result
