#!/usr/bin/env python3
"""Directed local moving-root jets of one exact R57 affine object.

A previously certified global t' interval first transports a tight singleton
root to an exact local parameter tube. The frozen R58 mixed-jet evaluator then
computes true t' and t'', including its interval DFT and infinite primitive
corrections. No rounded control-vector checkpoint is introduced.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_interval_scalar import floor_float, ceiling_float
from fourfold_phase_root_interval import Box
from fourfold_phase_parameter_root_jets import AffineMixedTarget


CAPTURED_HASHES = {}


def digest(path):
    path = Path(path)
    key = str(path.resolve())
    if key not in CAPTURED_HASHES:
        CAPTURED_HASHES[key] = hashlib.sha256(path.read_bytes()).hexdigest()
    return CAPTURED_HASHES[key]


def document(path):
    path = Path(path)
    raw = path.read_bytes()
    CAPTURED_HASHES[str(path.resolve())] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def fraction(value):
    return Fraction.from_float(float(value))


def enclosure(left, right):
    return [floor_float(left), ceiling_float(right)]


def verify_family(document, inputs, direction):
    if not document["proved"]:
        raise ValueError("unproved predecessor")
    if document["origin_inputs_sha256"] != digest(inputs):
        raise ValueError("origin mismatch")
    if document["frozen_direction_sha256"] != digest(direction):
        raise ValueError("direction mismatch")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object", type=Path, required=True)
    p.add_argument("--point-root", type=Path, required=True)
    p.add_argument("--global-jets", type=Path, required=True)
    p.add_argument("--common-root", type=Path, required=True)
    p.add_argument("--parameter-radius", type=float, default=1e-6)
    p.add_argument("--quarter-nodes", type=int, default=256)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    topic = Path(__file__).resolve().parents[1]
    obj = document(args.object)
    inputs, direction_path = (topic/obj[key]["path"] for key in ("origin_inputs", "direction"))
    for key, path in (("origin_inputs", inputs), ("direction", direction_path)):
        if obj[key]["sha256"] != digest(path):
            raise ValueError("exact object dependency mismatch")
    center = Fraction(int(obj["delta_fraction"]["numerator"]),
                      int(obj["delta_fraction"]["denominator"]))
    if fraction(obj["delta"]) != center or float(obj["delta"]).hex() != obj["delta_hex"]:
        raise ValueError("inconsistent exact parameter descriptor")
    root = document(args.point_root)
    global_jets = document(args.global_jets)
    common = document(args.common_root)
    for doc in (root, global_jets, common):
        verify_family(doc, inputs, direction_path)
    if Fraction(root["exact_delta_fraction"]) != center:
        raise ValueError("tight root belongs to another parameter")
    if (root["common_root_certificate_sha256"] != digest(args.common_root)
        or global_jets["common_root_certificate_sha256"] != digest(args.common_root)):
        raise ValueError("different common root branch")
    if global_jets["run_source_sha256"] != digest(Path(__file__).with_name("fourfold_phase_parameter_root_jets.py")):
        raise ValueError("R58 mixed-jet implementation changed")
    for name, value in global_jets["dependency_sha256"].items():
        if value != digest(Path(__file__).with_name(name)):
            raise ValueError("R58 dependency changed: "+name)
    global_interval = list(map(fraction, global_jets["exact_parameter_interval"]))
    if global_jets["exact_parameter_interval"] != common["exact_parameter_interval"]:
        raise ValueError("global parameter interval mismatch")
    radius = fraction(args.parameter_radius)
    if radius < 0:
        raise ValueError("negative radius")
    parameter_exact = [center-radius, center+radius]
    if not (global_interval[0] <= parameter_exact[0] <= parameter_exact[1] <= global_interval[1]):
        raise ValueError("local tube exits the global root branch")
    parameter_binary = enclosure(*parameter_exact)
    if not (global_interval[0] <= fraction(parameter_binary[0])
            and fraction(parameter_binary[1]) <= global_interval[1]):
        raise ValueError("outward parameter box exits global branch")
    # The evaluator uses the outward binary box, so transport must cover its
    # slightly larger radius too, rather than only the exact requested tube.
    covering_radius = max(center-fraction(parameter_binary[0]),
                          fraction(parameter_binary[1])-center)
    lipschitz = max(abs(fraction(v)) for v in global_jets["root_parameter_first"])
    transported_exact = [fraction(root["root_interval"][0])-covering_radius*lipschitz,
                         fraction(root["root_interval"][1])+covering_radius*lipschitz]
    radial_binary = enclosure(*transported_exact)
    collar = list(map(fraction, common["outward_binary_collar"]))
    if not (collar[0] <= fraction(radial_binary[0]) <= fraction(radial_binary[1]) <= collar[1]):
        raise ValueError("transported root exits common analytic collar")
    with np.load(inputs, allow_pickle=False) as data:
        frozen = {k:data[k].copy() for k in data.files}
    with np.load(direction_path, allow_pickle=False) as data:
        direction = {k:data[k].copy() for k in data.files}
    target = AffineMixedTarget(frozen, direction, parameter_binary, args.quarter_nodes)
    radial = Box(*radial_binary)
    c, k, evaluation = target.evaluate(radial)
    if float(c["Cx"].lo) <= 0:
        raise ValueError("implicit derivative denominator is not positive")
    t1 = -c["Cp"]/c["Cx"]
    t2 = -(c["Cpp"]+2*c["Cxp"]*t1+c["Cxx"]*t1*t1)/c["Cx"]
    # Continuous endpoint value Q(1,p)=t(p) K_x(t(p),p)/2.
    ip = k["Kxp"]+t1*k["Kxx"]
    ipp = k["Kxpp"]+2*t1*k["Kxxp"]+t1*t1*k["Kxxx"]+t2*k["Kxx"]
    Q = radial*k["Kx"]/2
    Qp = (t1*k["Kx"]+radial*ip)/2
    Qpp = (t2*k["Kx"]+2*t1*ip+radial*ipp)/2
    if float(Q.lo) <= 0:
        raise ValueError("endpoint Q positivity not proved")
    report = dict(kind="directed_local_exact_affine_moving_root_parameter_jets", proved=True,
        object_sha256=digest(args.object), point_root_sha256=digest(args.point_root),
        global_root_jets_sha256=digest(args.global_jets), common_root_sha256=digest(args.common_root),
        origin_inputs_sha256=digest(inputs), frozen_direction_sha256=digest(direction_path),
        source_sha256=digest(__file__),
        dependency_sha256={"fourfold_phase_parameter_root_jets.py":global_jets["run_source_sha256"],
                           **global_jets["dependency_sha256"]},
        exact_parameter_center=str(center), exact_parameter_radius=str(radius),
        exact_parameter_interval=list(map(str, parameter_exact)),
        outward_binary_parameter_interval=parameter_binary,
        covering_binary_parameter_radius_exact=str(covering_radius),
        certified_global_root_Lipschitz_exact=str(lipschitz),
        transported_root_interval_exact=list(map(str, transported_exact)),
        root_interval=radial_binary, root_parameter_first=t1.pair(), root_parameter_second=t2.pair(),
        endpoint_Q=Q.pair(), endpoint_Q_parameter_first=Qp.pair(),
        endpoint_Q_parameter_second=Qpp.pair(), quarter_nodes=args.quarter_nodes,
        root_evaluation=evaluation,
        justification="Global R58 t' transports the singleton tight root by the real mean-value theorem; the same exact affine mixed jets then give implicit first and second derivatives on the complete resulting box.",
        limitations=["No control-vector rounding, Gaussian smoothing, or change of target metric is introduced.",
                     "Endpoint Q derivatives are at fixed s=1 only, not complete ODE Taylor bounds.",
                     "No actual flow, continuous return error, KAM, or exact isometric-family conclusion."])
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k:report[k] for k in ("proved", "root_interval", "root_parameter_first",
        "root_parameter_second", "endpoint_Q", "endpoint_Q_parameter_first", "endpoint_Q_parameter_second")}))


if __name__ == "__main__":
    main()
