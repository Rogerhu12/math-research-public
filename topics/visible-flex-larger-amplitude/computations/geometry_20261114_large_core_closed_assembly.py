#!/usr/bin/env python3
"""Finite closed readout of a genuinely accepted complete large-core DN field.

The full prefix has its own z0 and frozen scalar controls.  A single proper
SE(2) normalizes its planar gauge against this exact accepted tail response.
The optional finite-width outer correction uses the complete continuous
material-angle cut difference, with all angular derivatives, rather than a
truncated Fourier approximation to that difference.  Its metric defect is
measured and it is not claimed to solve the exact common-metric problem.

The unchanged finite inner collar and fixed markers remain explicit.  This
entry can run the actual-tail radial readout, source background, closed mesh
and existing finite geometry diagnostics after a real full-DN acceptance.
It cannot create that acceptance or replace its tail by the historical A.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

import numpy as np

from geometry_20261114_full_dn_boundary import MaterialTrace
from geometry_20261114_large_core_saved_prefix import (
    LargeCoreSavedPrefix, actions_only, complete_material_means, read, sha)
from exact_20261114_refined_tail_adapter import (
    RefinedAssembly, RefinedTail, evaluate, hermite, module, synth)
from exact_20261114_closed_display_adapter import display_anchors, merges


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPO = TOPIC.parents[1]
_bundle = None
_last_assembly = None


def maxnorm(value):
    return float(np.max(np.linalg.norm(value, axis=-1), initial=0))


def load_bundle(args):
    global _bundle
    if _bundle is not None:
        return _bundle[:3]
    saved = LargeCoreSavedPrefix(args.checkpoint)
    config, port = read(args.config), read(args.port)
    if config.get("spacing") != 2 or config.get("orientation") != 1:
        raise ValueError("Use the original positive-r, spacing-two native tail")
    geometry = saved.rec["fixed_scalar_profile"]["geometry"]
    if geometry["complete_original_port"] != port:
        raise ValueError("The complete frozen scalar profile was designed for another original port")
    record = read(args.tail_response)
    response = record.get("response", record)
    actual = saved.rec["actual_tail"]
    if sha(args.tail_response) != actual["final_response_sha256"]:
        raise ValueError("Use this full-DN field's final actual audited response, not another same-g tail")
    if sha(args.config) != actual["sources"]["input_config"]:
        raise ValueError("The config does not match the actual full-DN tail invocation")
    origin = read(args.source_topic/"source-origin.json")
    if origin.get("actual_public_repository","").lower() != "rogerhu12/math-research-public":
        raise ValueError("The source bundle must be restored and verified from the public repository")
    verified_sources = {}
    native_prefix = "topics/visible-flexible-closed-surface/"
    for name,digest in actual["sources"].items():
        path = None
        if name.startswith(native_prefix):
            path = args.source_topic/name[len(native_prefix):]
        elif name.endswith(".mjs") and "/" not in name:
            path = HERE/name
        elif name == "frozen_ledger_ready":
            path = TOPIC/"notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json"
        elif name == "frozen_stored_ready":
            path = TOPIC/"notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json"
        if path is not None:
            if sha(path) != digest:
                raise ValueError("A numerical source differs from the accepted actual-tail bundle: "+name)
            verified_sources[name] = digest
    if (response.get("actual_nonlinear_solve") is not True or not response.get("converged") or
            not response.get("residual", np.inf) < config["solveTolerance"] or
            not response.get("audit") or not response.get("heightJetJacobian")):
        raise ValueError("The original actual nonlinear audit and complete DN Jacobian are required")
    T = int(config["modes"])
    H = np.asarray(response["checkpoint"]["cutHeight"], float)
    J = np.asarray(response["heightJetJacobian"], float)
    if H.shape != (T,) or J.size != (3*T+2)*T or not np.all(np.isfinite(J)):
        raise ValueError("The actual complete tail height or Jacobian has been truncated")
    params = response["checkpoint"]["parameters"]
    ignored = {"traceFile", "iterationCheckpointFile", "trialDiagnosticFile", "initialCheckpoint"}
    for key,value in config.items():
        if key in ignored:
            continue
        name = "physicalDepth" if key == "depth" else key
        if params.get(name) != value:
            raise ValueError("The actual response config differs at "+key)
    # Re-evaluate the same full finite operator using the actual augmented
    # endpoint c, whose tiny recorded drift from the inlet core is retained.
    augmented = np.asarray(saved.rec["augmented_states"][-1], float)
    endpoint_core = augmented[saved.n:saved.n+saved.M]
    material_N = int(saved.rec["parameters"]["material_angles"])
    trace = MaterialTrace(saved.M, T, material_N)(endpoint_core,
                        saved.sol.y[2*saved.M+1:, -1], np.zeros(saved.M+1))
    recomputed = -trace.height
    height_gap = float(np.max(abs(recomputed-H), initial=0))
    if height_gap > 1e-12:
        raise ValueError("The complete actual tail H does not match this endpoint's recorded material projection")
    tail = RefinedTail(args.complete)
    hashes = set(tail.meta["input_sha256"].values())
    if sha(args.tail_response) not in hashes or sha(args.config) not in hashes:
        raise ValueError("The radial Cartesian readout is not bound to this exact config and actual response")
    if tail.N != config["quadrature"] or abs(float(tail.r[-1])-config["rCut"]) > 1e-14:
        raise ValueError("The actual radial readout grid/cut differs")
    a, ap, app = saved.profile(saved.flow.end)
    cut = actual["cut"]
    target = np.array([cut["radius"],-1/np.sqrt(cut["E"]),-cut["Ep"]/(2*cut["E"]**2)])
    if np.max(abs(np.array([a,ap,app])-target)) > 5e-12 or ap >= 0:
        raise ValueError("The accepted complete prefix does not end at the physical closing cut")
    binding = dict(
        checkpoint_sha256=sha(args.checkpoint), actual_response_sha256=sha(args.tail_response),
        config_sha256=sha(args.config), complete_readout_sha256=sha(args.complete),
        complete_tail_modes=T, complete_tail_angular=tail.N,
        recomputed_complete_native_H_max_difference=height_gap,
        bitwise_same_recomputed_H=bool(np.array_equal(recomputed,H)),
        material_projection_angular=material_N,
        complete_H=H.tolist(), core_endpoint_vs_inlet_max=float(np.max(abs(endpoint_core-saved.core))),
        source_tail_cut=cut, saved_scalar_cut_012=[float(a),float(ap),float(app)],
        verified_original_numerical_sources=verified_sources,
        historical_A_tail_reused=False, full_continuous_H_truncation_certified=False)
    _bundle = saved, tail, config, binding
    return _bundle[:3]


class LargeCoreAssembly(RefinedAssembly):
    """The old closed-map API with full nonlinear material cut functions."""
    def __init__(self, saved, tail, plan, heights, cut_height):
        global _last_assembly
        self.saved, self.tail, self.plan = saved, tail, plan
        self.height = {float(row["r"]):row for row in heights["rows"]}
        self.inner, self.cut, self.cuff = plan["tail_inner"], plan["cut"], plan["cuff"]
        self.L, self.W = plan["prefix_end"], plan["cut_correction_width"]
        self.sigma = -1.
        self.reflection = np.array([1.,1.,self.sigma])
        self.prefix_cut_mean = float(saved.mean_jets([self.L])[0][0])
        self.inner_coeff = tail.node_coefficients(0)
        self.outer_coeff = tail.node_coefficients(len(tail.r)-1)
        self.tail_cut_mean = float(self.outer_coeff[0][0,2].real)
        self.offset = self.prefix_cut_mean-self.sigma*self.tail_cut_mean
        self.cap_height = self.offset-self.sigma*self.height[self.cuff]["heightFromRToCut"]
        zero = np.zeros_like(self.inner_coeff[0])
        self.inner_collar = hermite(zero,self.inner_coeff[0],zero,self.inner_coeff[1],
                                   zero,self.inner_coeff[2],np.longdouble(self.inner-self.cuff))
        self.a, self.ap, self.app = map(float,saved.profile(self.L))
        if not 0 < self.W < self.cut-self.inner or self.ap >= 0:
            raise ValueError("A positive outer correction width inside this physical tail is required")
        self.cut_radial_jets = dict(radius=self.a,r_s=self.ap,r_ss=self.app,
            material_chart="Complete theta=Phi_c(phi), independent of s; not assumed to be the identity",
            definition="Fr=Fs/ap, Frr=Fss/ap^2-app*Fs/ap^3; all angular derivatives use the same complete inverse")
        theta = 2*np.pi*np.arange(tail.N)/tail.N
        original, _, _ = saved.nine_jets([self.L],theta,normalized=False)
        native = self.native_cut_nine(theta)
        saved.set_native_registration(original[(0,0)][0,:,:2],native[(0,0)][:,:2])
        core_before, _, _ = saved.nine_jets([0.],np.array([0.,np.pi/2]),normalized=False)
        core_after, _, _ = saved.nine_jets([0.],np.array([0.,np.pi/2]))
        turn = np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,1.]])
        self.gauge_witness_info = dict(
            native_cap_rotation_axis_xy=[0.,0.],
            original_core_center_xy=[0.,0.],
            normalized_core_center_xy=((-saved.translation_from_native)@saved.rotation_to_native).tolist(),
            center_rule="The complete even-phi rotating-frame field is centrally symmetric in XY; the single SE2 transforms its center as recorded.",
            core_material_angles=[0.,float(np.pi/2)],
            original_core_positions=core_before[(0,0)][0].tolist(),
            normalized_core_positions=core_after[(0,0)][0].tolist(),
            phase_pi_over_two_core_candidate=(core_after[(0,0)][0,0]@turn.T).tolist(),
            candidate_material_theta=float(np.pi/2),
            original_centered_support_gap=saved.rec["core"]["axis_support_gap"],
            original_gap_reused_as_held_Hausdorff_lower_bound=False,
            definition="The candidate is an actual phase-pi/2 core point in the native cap frame. Its distance must be bounded against the complete baseline surface and fixed caps afresh.")
        self.delta_cache = {}
        self.unpatched_cut = []
        for count in (tail.N,2*tail.N):
            grid = 2*np.pi*np.arange(count)/count
            delta = self.cut_difference(grid)
            self.unpatched_cut.append(dict(angular=count,
                radial_angular_jet_norms={f"r{i}_theta{j}":maxnorm(delta[(i,j)]) for i in range(3) for j in range(3)}))
        # The inherited report writer expects this diagnostic attribute.  Its
        # legacy Fourier label is removed before any report is written; these
        # are full angular function samples, never coefficients of the patch.
        diagnostic = self.cut_difference(theta)
        self.cut_difference_coeff = np.stack([diagnostic[(i,0)] for i in range(3)])
        _last_assembly = self

    def prefix_jets(self,s,theta,height=None):
        return self.saved.material_jets(s,theta,height)

    def native_cut_nine(self,theta):
        theta = np.asarray(theta,float)
        g = self.tail.rows[-1]["geometry"]
        wr = g["w"]*g["dlogwdx"]/g["drdx"]
        background_z = [self.offset,self.sigma*g["w"],self.sigma*wr]
        co, si = np.cos(theta), np.sin(theta)
        circle = [np.column_stack([co,si]),np.column_stack([-si,co]),np.column_stack([-co,-si])]
        out = {}
        for i in range(3):
            radius = [self.cut,1.,0.][i]
            for j in range(3):
                value = synth(self.outer_coeff[i],theta,j)*self.reflection
                value[:,:2] += radius*circle[j]
                if j == 0:
                    value[:,2] += background_z[i]
                out[(i,j)] = value
        return out

    def cut_difference(self,theta):
        theta = np.asarray(theta,float)
        key = theta.tobytes()
        if key in self.delta_cache:
            return self.delta_cache[key]
        prefix, _, _ = self.saved.nine_jets([self.L],theta)
        native = self.native_cut_nine(theta)
        result = {}
        for j in range(3):
            radial = [prefix[(0,j)][0],prefix[(1,j)][0]/self.ap,
                      prefix[(2,j)][0]/self.ap**2-self.app*prefix[(1,j)][0]/self.ap**3]
            for i in range(3):
                result[(i,j)] = radial[i]-native[(i,j)]
        if len(self.delta_cache) >= 8:
            self.delta_cache.pop(next(iter(self.delta_cache)))
        self.delta_cache[key] = result
        return result

    def correction_weights(self,r,derivative):
        t = np.clip((np.asarray(r,np.longdouble)-(self.cut-self.W))/self.W,0,1)
        W = np.longdouble(self.W)
        # At the inner edge all 0/1/2 jets vanish.  At the cut these
        # three columns select the supplied Delta0, Delta1, Delta2 jets.
        c = np.array([[0,0,0],[0,0,0],[0,0,0],
                      [10,-4*W,W*W/2],[-15,7*W,-W*W],[6,-3*W,W*W/2]],np.longdouble)
        weights = np.zeros((len(t),3),np.longdouble)
        for k in range(derivative,6):
            factor = 1
            for j in range(derivative):
                factor *= k-j
            weights += (factor*t**(k-derivative)/W**derivative)[:,None]*c[k]
        weights[np.asarray(r) < self.cut-self.W] = 0
        return np.asarray(weights,float)

    def perturbation(self,r,theta):
        r,theta = np.asarray(r,float),np.asarray(theta,float)
        coefficients = []
        for radius in r:
            if radius >= self.inner:
                c = self.tail.coefficients(radius)
            else:
                width = np.longdouble(self.inner-self.cuff)
                t = np.longdouble(radius-self.cuff)/width
                c = tuple(evaluate(self.inner_collar,t,width,d) for d in range(3))
            coefficients.append(c)
        c = np.asarray(coefficients)
        index = dict(pos=(0,0),s1=(1,0),s2=(2,0),p1=(0,1),p2=(0,2),sp=(1,1))
        out = {name:synth(c[:,i],theta,j) for name,(i,j) in index.items()}
        if np.any(r >= self.cut-self.W):
            delta = self.cut_difference(theta)
            for name,(i,j) in index.items():
                weights = self.correction_weights(r,i)
                values = np.stack([delta[(k,j)]*self.reflection for k in range(3)])
                out[name] += np.einsum("rk,knc->rnc",weights,values)
        return out


def install_consumer(args):
    base = module("large_core_finite_closed_consumer",HERE/"exact_20261114_refined_closed_assembly.py")
    original_write = base.write
    def write(path,obj):
        if isinstance(obj,dict):
            obj["large_core_binding"] = _bundle[3]
            obj["large_core_prefix"] = _bundle[0].definition
            obj["legacy_finite_consumer_sha256"] = sha(HERE/"exact_20261114_refined_closed_assembly.py")
            obj["adapter_sha256"] = sha(__file__)
            obj["complete_state_adapter_sha256"] = sha(HERE/"geometry_20261114_large_core_saved_prefix.py")
            obj["source_revision"] = "Bound by the actual full-DN response's complete public source SHA ledger"
            obj["mean_rule"] = "The state already includes full Z0. Material means are read analytically; only the tail receives one absolute-height alignment."
            obj["display_query_adapter"] = dict(source_sha256=sha(HERE/"exact_20261114_closed_display_adapter.py"),
                merged_near_equal_display_requests=list(merges),physical_function_unchanged=True)
            if obj.get("schema") == "refined-tail-finite-closed-plan-v1":
                obj["schema"] = "large-core-complete-material-finite-closed-plan-v1"
                obj["inputs"]["actual_response"] = dict(file=str(args.tail_response.resolve()),sha256=sha(args.tail_response))
                obj["outer_cut_correction"] = "Full continuous material-angle difference, with exact symbolic radial Hermite endpoint jets; no cut Fourier truncation."
            if obj.get("schema") == "refined-tail-finite-closed-assembly-v1":
                A = _last_assembly
                obj["schema"] = "large-core-complete-material-finite-closed-assembly-v1"
                obj["single_global_planar_registration"] = A.saved.registration
                obj["core_and_hold_gauge"] = A.gauge_witness_info
                obj["shared_cut"].pop("delta_coefficient_l1",None)
                obj["shared_cut"].pop("prefix_untouched",None)
                obj["shared_cut"].update(
                    prefix_single_global_rigid_normalization=True,
                    original_six_jets_retained_before_patch=A.unpatched_cut,
                    correction_angular_definition="Whole Delta_i(theta) from the complete inverse Phi_c and the actual native cardinal tail; not projected to any finite theta bandwidth",
                    symbolic_outer_seam_identity=True,
                    literal_floating_C2_identity_certified=False,
                    floating_endpoint_residual_is_reported=True,
                    exact_common_metric_preserved=False)
                obj["limitations"] = [x for x in obj["limitations"] if "baseline A" not in x]
                obj["limitations"].extend([
                    "The full nonlinear DN finite acceptance is retained, but its material Fourier truncation and the continuous six-jet seam still require convergence.",
                    "The explicit full-angular outer correction gives a finite C2 map; it changes the metric and is not an exact isometric extension.",
                    "The native finite radial/cardinal field, small-mean quadrature and finite inner collar retain their recorded numerical limitations.",
                    "The inlet reflection's z, horizontal Fs and vertical Fss residuals are reported independently; finite BVP success does not certify an exact reflected C2 seam.",
                    "No continuous reach, all-surface Hausdorff amplitude, common-metric limit, or final topic completion is claimed by this mesh readout."])
        original_write(path,obj)
    base.load = load_bundle
    base.RefinedAssembly = LargeCoreAssembly
    base.complete_prefix_heights = complete_material_means
    base.anchors = display_anchors
    base.write = write
    return base


def node_command(script,args,capacity=True):
    command = ["node","--max-old-space-size=3072"]
    if capacity:
        command += ["--import",str(HERE/"exact_20261114_tail_capacity_loader.mjs")]
    return command+[str(HERE/script),*map(str,args)]


def execute(command,log,env):
    print(json.dumps(dict(event="large_core_closed_subprocess",command=command,log=str(log))),flush=True)
    env = dict(env,VISIBLE_FLEX_TAIL_CAPACITY_RECORD=str(Path(log).with_suffix(".capacity.json")))
    with Path(log).open("x") as stream:
        result = subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,env=env)
    if result.returncode:
        raise RuntimeError("Closed readout subprocess failed; original log retained at "+str(log))


def main():
    actions_only()
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action",choices=["plan","render","all"])
    for key in ("checkpoint","port","config","tail-response","out-prefix"):
        p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--source-topic",type=Path,required=True)
    for key in ("complete","plan","heights"):
        p.add_argument("--"+key,type=Path)
    p.add_argument("--readout-levels",default="1,2,4")
    p.add_argument("--angular",type=int,default=96)
    p.add_argument("--phase-samples",type=int,default=9)
    p.add_argument("--marker-k",type=float,default=1/160)
    p.add_argument("--cut-correction-width",type=float,default=.01)
    for key,value in [("prefix-intervals",112),("tail-intervals",112),("collar-intervals",24),
                      ("cap-intervals",40),("mean-batch",8),("reach-ring-stride",2),("reach-angle-stride",4)]:
        p.add_argument("--"+key,type=int,default=value)
    args = p.parse_args()
    args.source_hash = sha(__file__)
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if args.phase_samples < 3 or args.phase_samples%2 != 1:
        raise ValueError("Use an odd phase sample count at least three")
    env = dict(os.environ)
    env.update(VISIBLE_FLEX_TAIL_MODE_CAPACITY=str(read(args.config)["modes"]),
               VISIBLE_FLEX_SOURCE_TOPIC=str(args.source_topic.resolve()),
               VISIBLE_FLEX_SOURCE_ROOT=str(args.source_topic.resolve()/"repro/source-root"))
    # The unchanged Node readout/background entries use these two exact public
    # paths.  Restore omitted sparse assets from public HEAD, without rewriting
    # an existing file or reaching into any private source repository.
    from exact_20261114_true_tail_client import public_asset, DEFAULT_LEDGER, DEFAULT_STORED
    for asset in (DEFAULT_LEDGER,DEFAULT_STORED):
        public_asset(asset,TOPIC/"notes")
    if args.action == "all" and args.complete is None:
        directory = Path(str(args.out_prefix)+"-actual-tail-readout")
        execute(node_command("exact_20261114_resolved_radial_readout.mjs",[
            "--repo-root",REPO,"--source-topic",args.source_topic,"--config",args.config,
            "--response",args.tail_response,"--baseline-config",args.config,
            "--baseline-response",args.tail_response,"--out-dir",directory,
            "--levels",args.readout_levels]),Path(str(args.out_prefix)+"-tail-readout.log"),env)
        finest = max(map(int,args.readout_levels.split(",")))
        args.complete = directory/("complete-"+str(finest)+".json")
    if args.complete is None:
        p.error("An actual completed radial readout is required (--complete or action all)")
    base = install_consumer(args)
    if args.action in ("plan","all"):
        base.plan(args)
        args.plan = Path(str(args.out_prefix)+"-plan.json")
    if args.action == "all":
        args.heights = Path(str(args.out_prefix)+"-heights.json")
        execute(node_command("exact_20261114_closed_background.mjs",[
            "--repo-root",REPO,"--source-topic",args.source_topic,"--config",args.config,
            "--plan",args.plan,"--out",args.heights]),Path(str(args.out_prefix)+"-background.log"),env)
    if args.action in ("render","all"):
        if args.plan is None or args.heights is None:
            p.error("Rendering requires the completed plan and source background")
        base.render(args)


if __name__ == "__main__":
    main()
