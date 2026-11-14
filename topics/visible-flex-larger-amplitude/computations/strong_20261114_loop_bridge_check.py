#!/usr/bin/env python3
"""Check actual finite-loop/bridge joins for both signs of each new control."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from strong_20261114_loop_bridge import FIELDS, rebuild, verify_design_port


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    raw = args.reference.read_bytes()
    reference = json.loads(gzip.decompress(raw) if args.reference.suffix == '.gz' else raw)
    here = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location('loop_bridge_original_provider', here/'alternative-neck-provider.py')
    provider = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(provider)
    import strong_angle_boost as angle
    import strong_initial_speed_pulse as pulse
    import strong_monotone_initial_speed_anchor as frontload
    angle.install(provider); pulse.install(provider); frontload.install(provider)
    cfg = reference['frozen_profile']
    port = dict(parameters=reference['physical_tail_parameters'], cut=reference['physical_tail_cut'])
    bridge = provider.NeckTerminalBridge(port['cut'])
    same_port, same_bridge = rebuild(cfg, port, bridge)
    if same_port is not port or same_bridge is not bridge:
        raise ValueError('The exact baseline object is not preserved')
    rows = []
    for field in FIELDS:
        for sign in (-1, 1):
            changed = dict(cfg)
            width = 2e-6*max(.1, abs(cfg[field]))
            changed[field] += sign*width
            current_port, current_bridge = rebuild(changed, port, bridge)
            verify_design_port(current_port, reference, changed)
            prefix = provider.NeckPrefix(changed)
            left = np.asarray(prefix.profile(prefix.end))
            right = np.asarray(current_bridge.profile(0.)).reshape(3)
            terminal = np.asarray(current_bridge.profile(current_bridge.L)).reshape(3)
            cut = current_port['cut']; slope = cut['backgroundSlope']
            target = np.array([cut['radius'], -1/np.sqrt(1+slope*slope),
                -cut['backgroundSecond']*slope/(1+slope*slope)**2])
            rows.append(dict(field=field, sign=sign, width=width,
                prefix_bridge_jet_error=float(np.max(abs(left-right))),
                bridge_tail_jet_error=float(np.max(abs(terminal-target))),
                bridge_length=current_bridge.L,
                old_bridge_length=bridge.L,
                bridge_tag=current_port['cut']['_prefix_bridge']))
    error = max(max(row['prefix_bridge_jet_error'], row['bridge_tail_jet_error']) for row in rows)
    if error > 2e-11:
        raise ValueError('A physical C2 join failed: '+repr(error))
    result = dict(scope=__doc__, finished=True, nonlinear_solution=False,
        reference=str(args.reference), reference_sha256=hashlib.sha256(raw).hexdigest(),
        baseline_objects_identical=True, physical_tail_cut_and_parameters_unchanged=True,
        maximum_jet_error=error, checks=rows)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(finished=True, maximum_jet_error=error)), flush=True)


if __name__ == '__main__':
    main()
