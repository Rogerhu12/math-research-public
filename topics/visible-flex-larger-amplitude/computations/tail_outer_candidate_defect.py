#!/usr/bin/env python3
"""Add full continuous R44 residual bounds to the frozen candidate scan.

Only the explicitly checked read-only residual call and result records are
inserted. Deleting those insertions restores the exact executed domain
source. All original candidate, five-integral and source evaluations remain.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import hashlib
from pathlib import Path
import types

from tail_outer_full_mean_residual_bounds import full_mean_residual_bounds


def main():
    path = Path(__file__).with_name("tail_outer_candidate_domain.py")
    source = path.read_text()
    if hashlib.sha256(path.read_bytes()).hexdigest() != "17d6b7d85be80f8f40b3eec411ae49a73c51c6b624d030df57b94202a7d08690":
        raise ValueError("The actually executed R48 candidate source changed")
    changes = [
        ("    leading_min, mean_all, work_all = None, True, True",
         "    leading_min, mean_all, work_all = None, True, True\n    defect_worst = {}"),
        ("            for key, value in values.items():\n                if value > worst[key][\"value\"]:",
         "            full_defect = _full_mean_residual_bounds(\n"
         "                H, K, Kx, modes=modes, weights=weights, radius=r,\n"
         "                radius_x=ball(g[\"radius_x\"]), w=w,\n"
         "                log_w_x=ball(g[\"log_w_x\"]), norms=values)\n"
         "            for key, value in full_defect.items():\n"
         "                if key not in defect_worst or value > defect_worst[key][\"value\"]:\n"
         "                    defect_worst[key] = dict(value=value, witness=witness)\n"
         "            for key, value in values.items():\n                if value > worst[key][\"value\"]:"),
        ("status=\"Complete true-panel domain bounds of the specified actual R48 candidate\"",
         "status=\"Full continuous mean derivative and Darboux defect enclosures of the same actual R48 candidate\""),
        ("        full_mean_radial_derivative_evaluated=False,",
         "        full_mean_radial_derivative_evaluated=True,\n"
         "        full_mean_derivative_method=\"Exact weighted mean identity and full rational-source bound; no finite angular mean projection\","),
        ("        continuous_Darboux_defect_paid=False,",
         "        continuous_Darboux_defect_paid=True,\n"
         "        defect_bounds={key: dict(value=ball_record(item[\"value\"]), witness=item[\"witness\"])\n"
         "                       for key, item in defect_worst.items()},\n"
         "        defect_scope=\"An upper bound for the actual candidate residual, not a zero residual or a certified exact radial solution\",\n"
         "        additional_residual_source_hashes=_additional_residual_source_hashes,"),
    ]
    for before, after in changes:
        if source.count(before) != 1:
            raise ValueError("A frozen domain-source insertion anchor changed")
        source = source.replace(before, after)
    restored = source
    for before, after in reversed(changes):
        if restored.count(after) != 1:
            raise ValueError("A residual hook is not uniquely removable")
        restored = restored.replace(after, before)
    if restored != path.read_text():
        raise AssertionError("Candidate-source identity was not preserved")
    module = types.ModuleType("tail_outer_candidate_with_full_residual")
    module.__file__ = str(path)
    module.__dict__["_full_mean_residual_bounds"] = full_mean_residual_bounds
    module.__dict__["_additional_residual_source_hashes"] = {
        name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in (Path(__file__).name, "tail_outer_full_mean_residual_bounds.py")}
    exec(compile(source, str(path), "exec"), module.__dict__)
    module.main()


if __name__ == "__main__":
    main()
