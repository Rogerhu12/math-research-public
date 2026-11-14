#!/usr/bin/env python3
"""Compute new loop-profile responses at the genuinely accepted A field.

The former nine-control design omitted every loop-shape control even though
the largest measured principal curvature occurs on its outward loop turn.
This entry adds loop_curvature, loop_radius, loop_speed and
terminal_peak_fraction to the existing prefix-only physical controls. Their
actual providers already implement these parameters. Every perturbation
rebuilds both the loop and finite terminal bridge, with the physical tail
cut and parameters unchanged. It uses the unchanged
fixed-g full collocation matrix, complete stored-H tail derivative, physical
full/half-step forcing and streamed backward-error checks. No new nonlinear
solution or finite-step geometry is claimed by the resulting derivatives.

The baseline and old sources remain untouched. Newly requested physical
controls change g for design purposes; they are not a same-g refinement.
"""
from __future__ import annotations

import ast
import hashlib
import os
from pathlib import Path
import sys

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import strong_initial_laws_disk_control_response as laws
import strong_samechart_initial_laws_anchor_response as anchor

EXTRA = ("loop_curvature", "loop_radius", "loop_speed", "terminal_peak_fraction")
SOURCE = Path(__file__).resolve()


def main():
    prior_transform = laws.transformed_source

    def transformed():
        source, provenance = prior_transform()
        old = "'descending_sync_curvature','coast_outward','loop_ratio','initial_speed_pulse','initial_speed_frontload'))"
        new = old[:-2] + "," + ",".join(repr(name) for name in EXTRA) + "))"
        if source.count(old) != 1:
            raise ValueError("Expected the single existing physical-control list")
        edits = [(old, new),
            ("        baseline_core=np.asarray(self._core.coefficients).copy()",
             "        from strong_20261114_loop_bridge import rebuild as rebuild_bridge\n"
             "        baseline_port,baseline_bridge=self.port,self.bridge\n"
             "        baseline_core=np.asarray(self._core.coefficients).copy()"),
            ("            if field is not None:self.cfg[field]=float(value)\n"
             "            self._flow=None;self._flow_key=None;self._core_key=None;self._initial=None",
             "            if field is not None:self.cfg[field]=float(value)\n"
             "            self.port,self.bridge=rebuild_bridge(self.cfg,baseline_port,baseline_bridge)\n"
             "            self._flow=None;self._flow_key=None;self._core_key=None;self._initial=None"),
            ("                self.cfg=dict(baseline_cfg);self._flow=baseline_flow;self._flow_key='frozen'",
             "                self.port,self.bridge=baseline_port,baseline_bridge\n"
             "                self.cfg=dict(baseline_cfg);self._flow=baseline_flow;self._flow_key='frozen'")]
        changed = source
        for before, after in edits:
            if changed.count(before) != 1:
                raise ValueError("Loop/bridge response source anchor differs: "+repr(before))
            changed = changed.replace(before, after, 1)
        ast.parse(changed)
        result = dict(provenance)
        result["source_sha256"] = {**provenance["source_sha256"],
            str(SOURCE): hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            str(SOURCE.with_name('strong_20261114_loop_bridge.py')):
                hashlib.sha256(SOURCE.with_name('strong_20261114_loop_bridge.py').read_bytes()).hexdigest()}
        result["transformed_source_sha256"] = hashlib.sha256(changed.encode()).hexdigest()
        result["explicit_transforms"] = list(provenance["explicit_transforms"]) + [
            dict(before=a, after=b, replacements=1) for a,b in edits]
        result["loop_profile_response"] = dict(
            scope=__doc__, added_physical_controls=list(EXTRA),
            complete_baseline_matrix_and_tail_H_unchanged=True,
            original_full_half_step_and_backward_checks_unchanged=True,
            finite_bridge_rebuilt_for_each_control_perturbation=True,
            physical_tail_cut_and_parameters_preserved=True,
            nonlinear_solution_claim=False)
        return changed, result

    laws.transformed_source = transformed
    try:
        anchor.main()
    finally:
        laws.transformed_source = prior_transform


if __name__ == "__main__":
    main()
