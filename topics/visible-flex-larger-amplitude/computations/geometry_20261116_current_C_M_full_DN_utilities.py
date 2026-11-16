#!/usr/bin/env python3
"""R442: explicit M-dimensional utilities for the original full-DN program.

The original shared-current-H transport, both complete boundary FD groups,
the two Richardson levels, and the live-owner close contract are retained.
Only actual M replaces the old physical-height length and mode metadata.
The original fixed112 adapter is a pinned source ancestor, never a current
M-dimensional response or accepted field. Public Actions only.
Author: exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import math
import os
from pathlib import Path
import struct
import sys

HERE=Path(__file__).resolve().parent
ENTRY=Path(__file__).name
SCHEMA="R442-current-C-complete-M-original-full-DN-utilities-v1"
ORIGINAL_NAME="geometry_20261115_current_C_pruefer_joint_full453_physical_dn.py"
ORIGINAL_SHA="c71d616936cf33e43965906c7cc99face01d06a12433420474b688b8d76b946d"

CLIENT_NAME="geometry_20261116_current_C_M_pruefer_joint_tail_client.py"
SAMPLER_NAME="geometry_20261116_current_C_M_pruefer_joint_radial_sampling.py"
NEW_NATIVE_PINS={
    "geometry_20261116_current_C_M_general_robin_native.mjs": "fb951f3688673a01b698bb7c606d6a854c061816e139bae55e51a176b4439f8c",
    "geometry_20261116_current_C_M_synchronous_linear_bridge.mjs": "8f189c095ec5bfbc3c323e2421cd98f931931334603ec902a94a75a60a3854de",
    "exact_20261116_current_C_M_general_robin_chain.py": "d4f6d4ffa7f54c38fb251ed72ef7d5bcdd8c5371c99506b0b8d98095506c3737",
    "geometry_20261116_current_C_M_pruefer_joint_radial_sampling.py": "9a85d7d17796ea567cdcfdac567ee531fcf5c225bfe9f57699bbb403aead41c1",
    "geometry_20261116_current_C_M_pruefer_joint_native_worker.mjs": "17a58fde59a4dbc126bce6c7f4584edf74a94690ec0aace831a31f10783c8509",
    "geometry_20261116_current_C_M_pruefer_joint_tail_client.py": "ab326e5b4814341b9cf6fbb054d56e8183e4560922c16878a4c57ca6620b135d",
    "geometry_20261116_stored_C_finite_M_head_pruefer_positive.py": "82a3f3e28e506320f474c64fd50d9ceadf3b39e9de9dc07f70c3df3c5c66bde6",
    "geometry_20261116_stored_continuous_C_M_far_graph.py": "5f16872e6e2e71914a73345b2f9b9142dbb0a7438e68805033a3277d3eb3d528"
}
def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda:handle.read(1<<20),b""):h.update(block)
    return h.hexdigest()

def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("Scientific execution belongs only to the named public Actions")

def original_source():
    require_actions()
    path=HERE/ORIGINAL_NAME
    if sha(path)!=ORIGINAL_SHA:
        raise ValueError("The original complete full-DN utility ancestor changed")
    spec=importlib.util.spec_from_file_location("_R442_original_current_DN_utilities",path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    try:spec.loader.exec_module(module)
    except BaseException:sys.modules.pop(spec.name,None);raise
    return module

ORIGINAL=original_source()
PINS=dict(ORIGINAL.PINS)
PINS.update(NEW_NATIVE_PINS)
PINS[ORIGINAL_NAME]=ORIGINAL_SHA
NATIVE_PINS=dict(ORIGINAL.NATIVE_PINS)
NATIVE_PINS.update(NEW_NATIVE_PINS)
ORIGINAL_RUNTIME_PINS=copy.deepcopy(ORIGINAL.ORIGINAL_RUNTIME_PINS)
MODEL=ORIGINAL.MODEL
BINDING_NAME=ORIGINAL.BINDING_NAME

# These generic helpers are the original functions with their original globals.
# The three dimension-bearing functions below are the only copied functions.
clean=ORIGINAL.clean
canonical=ORIGINAL.canonical
receipt=ORIGINAL.receipt
checked_json=ORIGINAL.checked_json
finite_vector=ORIGINAL.finite_vector
raw_words=ORIGINAL.raw_words
curve_with_exact_nodes=ORIGINAL.curve_with_exact_nodes
bound_original_preflight=ORIGINAL.bound_original_preflight
restore_attributes=ORIGINAL.restore_attributes

def __getattr__(name):
    return getattr(ORIGINAL,name)

def actual_boundary_fd(d, problem, response, initial_height, output, binding, seed_path):
    """The original three perturbations, direction set and Richardson helper."""
    np, flow, boundary = d.np, problem.flow, problem.boundary
    problem.affine.set(initial_height, response)
    separated = d.SeparatedBoundary(boundary)
    ya, yb = problem.values[0].copy(), problem.values[-1].copy()
    yb[boundary.iz+1] += 1e-5
    yb[boundary.iz+32] += 1e-9
    yb[boundary.iz+flow.M] += 1e-10
    yb[flow.core_slice] = ya[1:flow.M+1]
    pa, pb, controls = ya[:flow.n].copy(), yb[:flow.n].copy(), yb[flow.parameter_slice].copy()
    direct_directions, augmented_directions = d.response.make_directions(flow, boundary)
    A, B, P = boundary.jacobian(pa, pb, controls)
    direct = d.refined_directional_check(
        lambda v, h: boundary(pa+h*v['ya'], pb+h*v['yb'], controls+h*v['p']),
        lambda v: A@v['ya']+B@v['yb']+P@v['p'], direct_directions)
    AA, BB = separated.jacobian(ya, yb)
    augmented = d.refined_directional_check(
        lambda v, h: separated(ya+h*v['ya'], yb+h*v['yb']),
        lambda v: AA@v['ya']+BB@v['yb'], augmented_directions)
    augmented.update(right_rows_depend_only_on_right_endpoint=True,
        left_right_jacobian_offblock_max=float(max(np.max(abs(AA[separated.left_count:])),
                                                  np.max(abs(BB[:separated.left_count])))))
    groups = (direct, augmented)
    coarse = max(v['relative_error'] for g in groups for item in g['directions'] for v in item['levels'])
    worst = max(v['relative_error'] for g in groups for item in g['directions'] for v in item['fourth_order_levels'])
    contracts = all(g['second_order_truncation_contracts'] for g in groups)
    passed = bool(np.isfinite(worst) and worst <= 5e-5 and contracts)
    record = dict(schema=SCHEMA, physical_test_schema=d.PHYSICAL_SCHEMA,
        direct_boundary=direct, separated_boundary=augmented,
        maximum_relative_directional_error=worst, maximum_second_order_relative_directional_error=coarse,
        maximum_fourth_order_relative_directional_error=worst,
        verification_threshold=5e-5, verification_estimator='two fourth-order Richardson levels',
        second_order_truncation_contracts=contracts, implementation_check_passed=passed,
        physical_test=boundary.description(), current_C_complete_M_implementation=binding,
        prepared_sha256=sha(seed_path), native_anchor_response_sha256=sha(output/'initial-actual-H-tail.json.gz'),
        native_anchor_height=initial_height.tolist(), actual_current_H_solved_before_this_FD=True,
        FD_perturbed_states_use_explicit_affine_map=True,
        zero_anchor_J_not_relabelled_as_current_H_J=True,
        original_three_perturbations_directions_steps_and_threshold_unchanged=True,
        same_live_client_will_be_retained_if_FD_passes=passed,
        full_BVP_solved=False, full_Cartesian_closed_surface=False)
    d.core.write(output/'response-check.json', d.response.clean(record))
    return passed, record


class SharedNativeClient:
    """One current-C worker; real response supplies otherwise absent cut metadata."""
    def __init__(self,client,report_directory):
        self.client,self.closed,self.calls=client,False,[]
        self.close_attempted,self.close_exception=False,None
        self.report_directory=Path(report_directory)
        self._cut=dict(client.cut)
        self.cut_response_identity=None

    @property
    def cut(self):
        return self._cut

    def __getattr__(self,name):
        return getattr(self.client,name)

    def solve(self,height,*,jacobian,audit):
        if self.close_attempted:raise RuntimeError("The same live current-C owner is already closing")
        H=[float(x) for x in height]
        hraw=raw_words(H)
        call=dict(jacobian=bool(jacobian),audit=bool(audit),completed=False,
            actual_current_height_sha256=hashlib.sha256(hraw).hexdigest(),
            actual_current_height_float64le=[struct.pack("<d",v).hex() for v in H])
        self.calls.append(call)
        result=self.client.solve(H,jacobian=jacobian,audit=audit)
        cp=result.get("checkpoint",{})
        restored=finite_vector(cp.get("cutHeight"),self.client.M,"actual returned physical H")
        zeros=cp.get("cutHeight_negative_zero_columns",[])
        if not isinstance(zeros,list) or zeros!=sorted(set(zeros)):
            raise ValueError("Actual returned height signed-zero sidecar differs")
        for j in zeros:
            if type(j) is not int or not 0<=j<self.client.M or restored[j]!=0:
                raise ValueError("Actual returned height signed-zero index differs")
            restored[j]=-0.0
        if (result.get("actual_nonlinear_solve") is not True
                or result.get("converged") is not True or result.get("failed",False)
                or result.get("complete_infinite_C_nonlinear_DN_certified") is not False
                or raw_words(restored)!=hraw or cp.get("cutHeight_sha256")!=hashlib.sha256(hraw).hexdigest()):
            raise ValueError("Only a real converged response for these actual complete H words may be used")
        jets=result["jets"]
        actual_cut={key:float(jets[key]) for key in
            ("radius","E","Ep","backgroundSlope","backgroundSecond")}
        if not all(math.isfinite(v) for v in actual_cut.values()):
            raise ValueError("Actual response cut fields are nonfinite")
        identity=dict(schema=SCHEMA+"-real-current-response-cut",
            actual_native_call=result["call"],actual_height_sha256=call["actual_current_height_sha256"],
            native_owner=result["identity"],ready_cut=dict(self.client.cut),
            actual_response_cut=actual_cut,
            actual_response_cut_words={k:struct.pack("<d",v).hex() for k,v in actual_cut.items()},
            whole_actual_response_canonical_sha256=hashlib.sha256(canonical(result)).hexdigest(),
            profile_target_or_geometry_not_overwritten=True,
            actual_response_fields_not_filled_from_profile_or_ready_defaults=True)
        if self.cut_response_identity is None:
            # READY did not precompute a DN response or these two fields. Only
            # a completed actual call can provide the original main's metadata.
            self._cut=actual_cut
            self.cut_response_identity=identity
            p=self.report_directory/"current-response-cut-origin.json"
            p.write_bytes(canonical(identity))
        else:
            old=self.cut_response_identity["actual_response_cut_words"]
            if identity["actual_response_cut_words"]!=old:
                raise ValueError("Background geometry changed within the same live current-C owner")
        call.update(completed=True,actual_native_call=result["call"],
            normalizedResidual=result["normalizedResidual"],
            actual_response_canonical_sha256=identity["whole_actual_response_canonical_sha256"],
            actual_fresh_audit=bool(audit),finite_nonlinear_scope_only=True)
        return result

    def close(self):
        if not self.close_attempted:
            self.close_attempted=True
            try:
                self.client.close();self.closed=True
            except Exception as error:
                self.close_exception=repr(error);raise


def make_runtime_compatibility(args,problem,out):
    """Add only the original solver's explicit modes/spacing metadata.

    The actual current-native config source and geometry identities remain
    byte-bound and are copied without mathematical changes. No old port or
    native result is used to create this current record.
    """
    cfg=copy.deepcopy(problem.cfg)
    for key,value in (("modes",problem.flow.M),("spacing",2)):
        if key in cfg and cfg[key]!=value:raise ValueError("Actual config mode metadata differs")
        cfg[key]=value
    cfg["current_BVP_adapter_origin"]=dict(source_sha256=sha(__file__),
        original_configuration=problem.native_binding["configuration"],
        only_added_compatibility_fields=["modes","spacing"],
        original_current_native_source_and_science_parameters_unchanged=True)
    path=out/"current-native-full-BVP-config.json"
    path.write_bytes(canonical(cfg))
    actual_args=argparse.Namespace(**vars(args))
    actual_args.tail_config=path
    actual_args.expected_tail_client_sha256=PINS[CLIENT_NAME]
    port=dict(schema=SCHEMA+"-current-numeric-physical-port",
        parameters={key:cfg[key] for key in ("modes","spacing","model_schema","geometry_result_sha256")},
        actual_original_current_native_configuration=problem.native_binding["configuration"],
        actual_BVP_compatible_configuration=receipt(path),
        current_profile_binding=problem.target_owner.binding,
        exact_target_C_or_legacy_stored_port_relabelled=False,
        old_node_graphs_gains_or_zero_J_used=False)
    problem.current_port=port
    port_path=out/"current-profile-native-port.json"
    port_path.write_bytes(canonical(port))
    return actual_args,port_path

