#!/usr/bin/env python3
"""Actual RHS and boundary-glue checks for the explicitly named v2 controls.

Select `scalar` or `boundary`, then use the corresponding original CLI.
All three scalar probes use real accepted nonaxisymmetric-prefix states.
The boundary check retains the original complete Richardson procedure and
unchanged 5e-5 gate, with its linear-graph reference still labeled as such.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

import numpy as np

import geometry_20261114_full_dn_augmented as augmented
from geometry_20261114_prefix_controls_profile import PrefixControlsProfile, SCHEMA, SCHEME


HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def binding():
    return dict(schema=SCHEMA,control_scheme=SCHEME,
        adapter_source_sha256=sha(__file__),
        profile_source_sha256=sha(HERE/"geometry_20261114_prefix_controls_profile.py"),
        original_scalar_RHS_source_sha256=sha(HERE/"geometry_20261114_full_dn_augmented.py"),
        original_boundary_check_source_sha256=sha(HERE/"geometry_20261114_full_dn_response.py"))


def scalar():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ("accepted","port","out"):
        p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--peak-curvature",type=float,default=2.5)
    p.add_argument("--tail-modes",type=int)
    args = p.parse_args()
    accepted,port = augmented.read(args.accepted),augmented.read(args.port)
    profile = PrefixControlsProfile(accepted,port,args.peak_curvature,args.tail_modes)
    law = accepted["original_metric_identity"]["law"]
    q = augmented.base.native.outward.FullCoreProbe(np.asarray(accepted["core"]["coefficients"]),
            accepted["M"],accepted["N"],law["velocity"],law["length"],law["k0"])
    q.profile = profile.prefix.profile
    augmented.base.fixed.fft.enable_fft(q)
    flow = augmented.AugmentedFlow(q,profile)
    mesh,states = np.asarray(accepted["mesh"]),np.asarray(accepted["states"])
    indices = np.array([0,len(mesh)//2,len(mesh)-1])
    before = augmented.base.BatchedFFTFlow(q)(mesh[indices],states[indices].T)
    after = flow.physical(mesh[indices],states[indices].T,np.zeros((flow.k,len(indices))))
    difference = float(np.max(abs(after-before)))
    if difference > 1e-12:
        raise ValueError("The zero-control wrapper changed the original physical Frenet RHS")
    checks = []
    for j,bump in enumerate(profile.bumps):
        index = int(np.argmin(abs(mesh-(bump.left+bump.right)/2)))
        if not bump.left < mesh[index] < bump.right:
            raise ValueError("The scalar response point must lie inside its actual new support")
        check = augmented.response_check(flow,float(mesh[index]),states[index],np.zeros(flow.k),j)
        check.update(state_kind="actual-accepted-nonaxisymmetric-prefix-state",
                     accepted_node=index,control_support=[bump.left,bump.right])
        checks.append(check)
    result = dict(scope=__doc__,prefix_controls_implementation=binding(),
        scalar_profile=profile.description(),physical_state_dimension=flow.n,
        augmented_state_dimension=flow.dimension,left_rows=2*flow.M+5+flow.M,
        right_rows=profile.tail_modes,zero_control_original_RHS_max_difference=difference,
        scalar_control_directional_checks=checks,source_sha256=sha(__file__),
        accepted_sha256=sha(args.accepted),full_DN_evaluated=False,
        full_DN_boundary_FD_checked=False,full_extension_solved=False,closed_surface_certified=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
    print(json.dumps(dict(control_scheme=SCHEME,zero_control_original_RHS_max_difference=difference,
                         all_scalar_probe_states_are_actual_accepted_prefix=True)),flush=True)
    return 0


def boundary():
    import geometry_20261114_full_dn_response as original
    original.CompleteProfile = PrefixControlsProfile
    original.__file__ = __file__
    result = original.main()
    directory = Path(sys.argv[sys.argv.index("--out")+1])
    path = directory/"response-check.json"
    record = json.loads(path.read_text())
    record["prefix_controls_implementation"] = binding()
    path.write_text(json.dumps(record,indent=2,allow_nan=False)+"\n")
    return result


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Execute these numerical checks only in the public repository's Actions")
    if len(sys.argv) < 2 or sys.argv[1] not in ("scalar","boundary"):
        raise ValueError("Choose scalar or boundary, followed by its original arguments")
    action = sys.argv.pop(1)
    return scalar() if action == "scalar" else boundary()


if __name__ == "__main__":
    raise SystemExit(main())
