"""Keep the finite bridge attached when physical loop controls change.

The private _prefix_bridge tag describes the finite prefix connector, not
the physical infinite-tail cut. All remaining cut keys and all tail
parameters are preserved exactly. Rebuilding uses the original provider's
bridge class; no alternative bridge equation is introduced.
"""
from __future__ import annotations

import copy

FIELDS = {
    "loop_radius": ("radius", .35),
    "loop_speed": ("speed", .985),
    "loop_curvature": ("curvature", 8.),
    "terminal_peak_fraction": ("peak_fraction", .1),
}


def bridge_spec(profile):
    return {"kind": "finite_neck_terminal_v1", **{
        target: float(profile.get(source, default))
        for source, (target, default) in FIELDS.items()}}


def physical_cut(cut):
    return {key: value for key, value in cut.items() if key != "_prefix_bridge"}


def verify_design_port(port, reference, profile):
    """Allow only the declared finite connector tag to vary with profile."""
    if port["parameters"] != reference["physical_tail_parameters"]:
        raise ValueError("The physical infinite-tail parameters changed")
    if physical_cut(port["cut"]) != physical_cut(reference["physical_tail_cut"]):
        raise ValueError("The physical infinite-tail cut changed")
    if port["cut"].get("_prefix_bridge") != bridge_spec(profile):
        raise ValueError("The finite bridge tag does not match physical controls")


def rebuild(profile, baseline_port, baseline_bridge):
    spec = bridge_spec(profile)
    if spec == baseline_port["cut"]["_prefix_bridge"]:
        # Preserve the exact already-verified baseline arithmetic.
        return baseline_port, baseline_bridge
    port = copy.deepcopy(baseline_port)
    port["cut"]["_prefix_bridge"] = spec
    if (port["parameters"] != baseline_port["parameters"]
            or physical_cut(port["cut"]) != physical_cut(baseline_port["cut"])):
        raise ValueError("Rebuilding the finite bridge changed the tail")
    bridge = type(baseline_bridge)(port["cut"])
    if bridge.sigma != baseline_bridge.sigma:
        raise ValueError("Finite bridge changed the physical height convention")
    return port, bridge
