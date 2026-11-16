#!/usr/bin/env python3
"""R442 full-state SavedPrefix for a genuine complete frozen-M continuous-ten field.

The accurate target retains all ten current dyadic coefficients and the
complete R300/R286 expression family.  The saved field is independently
defined by complete physical nodal values, saved frozen RHS and newly
evaluated original finite-ODE second jets.  An exact rational Hermite
interpretation is provided separately from the existing rounded numerical
quintic evaluator.  Neither is called an exactly isometric solution.

This source deliberately does NOT call the old nine/legacy shared loader:
that loader constructs an old finite frozen tail/background.  A current-C
complete radial native readout and its actual shared background remain
explicit inputs of a future distinct closed producer.  No accepted field,
future coefficient vector, C root, seam, cap, metric bound or reach is chosen.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
from types import SimpleNamespace

REPOSITORY="Rogerhu12/math-research-public"
HERE=Path(__file__).resolve().parent
SCHEMA="R442-continuous-ten-frozen-M-complete-saved-prefix-v1"
CHECKPOINT_NAME="geometry_20261116_continuous_ten_frozen_M_checkpoint.py"
CHECKPOINT_SHA="18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93"
PROFILE_NAME="geometry_20261116_continuous_ten_M_same_metric_profile.py"
PROFILE_SHA="cc70e7699a817c5715e12de2b131d1a381082f630f0fdadf3648d9a8bec0151a"
KERNEL_NAME="geometry_20261114_large_core_saved_prefix.py"
KERNEL_SHA="51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0"
ACTIVE_JET_NAME="geometry_20261115_shared_active_interval_balls.py"
ACTIVE_JET_SHA="675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b"
PHYSICAL_KERNEL_PINS = {
    "alternative-angle-plateau-connector.py": "d9b1a9b9822664fb466942ccab13d2319c9d0f23c7ccacef2aae193b5e7b9ad7",
    "alternative-controlled-profile.py": "0af61a3bfccf093bfe6c255f864c658c37119b890f362d5d2e16429d2969e430",
    "alternative-direct-tail-connector.py": "9a6462c60bc8b3607decca6aab894210011b40903b0406c233090ff7856d4241",
    "alternative-fast-profile.py": "d6e0515c179a1e96ff2507e4fb5c8e3974ca170a0821af7e0441c7564cc0cc76",
    "alternative-neck-excursion.py": "f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c",
    "alternative-neck-flatturn.py": "c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd",
    "alternative-neck-provider.py": "84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2",
    "alternative-outward-probe.py": "cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb",
    "geometry_20261114_block_csc_bvp.py": "af91df83e0bbf255c79ae25d49f107f4967380bfcdaf56c689bdde54b344835e",
    "geometry_20261114_fft_frenet.py": "973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401",
    "geometry_20261114_full_dn_readout.py": "f6602baa54d3f599deb7d7c40ac9f4806e5faca2fc305b674b1c1cda02067cb1",
    "geometry_20261114_full_scalar_profile.py": "8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b",
    "geometry_20261114_large_core_saved_prefix.py": "51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0",
    "geometry_20261114_material_quintic_readout.py": "14e550ed75ad86bd8308966711313b7e0cd8917a2c166c90cf4e6ca1f5f85756",
    "geometry_20261114_prefix_controls_profile.py": "f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24",
    "geometry_20261114_r225_fixed_profile.py": "478d0bf603ea05a9f20228ff2fd591e2f767e6ab0686a6129b1114aa831b0c6c",
    "geometry_20261114_r225_free_core_bvp.py": "a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08",
    "geometry_20261114_r225_high_core_bvp.py": "e12916dcf30dd2088ad59d2059647c8a03bed446aeee693b88f423730fa5a530",
    "geometry_20261114_r225_outward_probe.py": "64a3fd482f6ee01f4d149971dff1212b2c2ca3bdb00f1b733c7b119b458bab5f",
    "root_20261114_scaled_core.py": "8f9fe56da99c21ef9b1e585f6000b595aec5098b13bdda197634bba9f86a7c7a",
    "root_profile_scan.py": "3d940a78d18f509b98caa4fb8782ea34ad54423a58bf94e0f386f4f20e2994db",
    "strong_20261114_scaled_core_tail_connector.py": "661d5d84dc0dd3da46f4936c2c3ad28f80df3475f421c56d770a2afa6402ac08",
    "strong_angle_boost.py": "ce2117cffe2e55d310eb0be219e7d22e750d97cd22704e75c3dd74a085c020be"
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Evaluate complete saved-field jets only in the named public repository Actions")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode()


def load(directory,name,expected,module_name):
    path=Path(directory)/name
    if digest(path)!=expected:
        raise ValueError("A complete same-field source differs: "+name)
    for module in tuple(sys.modules.values()):
        filename=getattr(module,"__file__",None)
        if filename is not None and Path(filename).resolve()==path.resolve():
            return module
    spec=importlib.util.spec_from_file_location(module_name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[module_name]=module
    try:spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(module_name,None);raise
    return module


def checked_sources(directory):
    sources={}
    for name,expected in PHYSICAL_KERNEL_PINS.items():
        if digest(Path(directory)/name)!=expected:
            raise ValueError("The original full physical-jet kernel source differs: "+name)
        sources[name]=expected
    for name,expected in ((CHECKPOINT_NAME,CHECKPOINT_SHA),(PROFILE_NAME,PROFILE_SHA),
                          (KERNEL_NAME,KERNEL_SHA)):
        if digest(Path(directory)/name)!=expected:
            raise ValueError("An independent current-ten source differs: "+name)
        sources[name]=expected
    sources[Path(__file__).name]=digest(__file__)
    return sources


def exact_hermite(left,right,width):
    """Original six coefficient identities over exact nodal dyadic values."""
    if width<=0:
        raise ValueError("An exact full physical cell must have positive width")
    c0,c1,c2=left[0],width*left[1],width*width*left[2]/2
    A=right[0]-c0-c1-c2
    B=width*right[1]-c1-2*c2
    C=width*width*right[2]-2*c2
    return (c0,c1,c2,10*A-4*B+C/2,-15*A+7*B-C,6*A-3*B+C/2)


class ContinuousTenSavedPrefix:
    """The original full six/nine-jet methods, with independent actual inputs.

    Original methods are bound to this object without invoking the legacy
    constructor or changing its module.  Their complete Fourier/mean/material
    inverse/SE2 formulas are unchanged.  No old scalar reconstruction runs.
    """
    def __init__(self,directory,manifest_sha256,code_directory=HERE):
        require_actions()
        self.source_sha256=checked_sources(code_directory)
        C=load(code_directory,CHECKPOINT_NAME,CHECKPOINT_SHA,"_r400_ten_checkpoint")
        checkpoint=C.Checkpoint(directory,manifest_sha256,code_directory).require_frozen_M()
        P=C.load_profile(code_directory)
        kernel=load(code_directory,KERNEL_NAME,KERNEL_SHA,"_r400_complete_physical_saved_kernel")
        self._kernel=kernel
        np=kernel.np
        self.checkpoint=checkpoint
        self.path=Path(directory)/"checkpoint.json"
        # Preserve the complete original result separately; no old schema,
        # target identity or source metric is edited to satisfy a consumer.
        self.rec=copy.deepcopy(checkpoint.raw)
        self.M,self.N,self.mode=checkpoint.M,checkpoint.resolution["field_angular_quadrature"],2
        self.n=3*self.M+2
        self.actual_resolution=copy.deepcopy(checkpoint.resolution)
        self.core=checkpoint.arrays["core"].copy()
        self.frequencies=2*np.arange(1,self.M+1)
        self.density=(1-self.frequencies**2)*self.core
        reference=[Q(6,5)*v for v in kernel.r225_coefficients()]
        exact_core=[Q.from_float(float(v)) for v in self.core]
        rho_reference_lower=1+sum((1-4*m*m)*v for m,v in enumerate(reference,1))
        rho_difference=sum((4*m*m-1)*abs(v-(reference[m-1] if m<=len(reference) else 0))
            for m,v in enumerate(exact_core,1))
        self.rho_lower_exact=rho_reference_lower-rho_difference
        if self.M<len(reference) or self.rho_lower_exact<=0:
            raise ValueError("The existing R237 complete material-inverse sufficient bound remains unpaid; no BVP rejection is inferred")
        self.profile_model=checkpoint.profile
        x=checkpoint.arrays["mesh"].copy()
        Y=checkpoint.arrays["physical"].copy()
        DY=checkpoint.arrays["physical_rhs"].copy()
        law=checkpoint.manifest["original_law"]
        physical=kernel.physical
        q=physical.base.native.outward.FullCoreProbe(self.core,self.M,self.N,
            law["velocity"],law["length"],law["k0"])
        q.profile=self.profile_model.profile
        physical.base.fixed.fft.enable_fft(q)
        DDY,gap=[],0.
        for s,y,yp in zip(x,Y,DY):
            frame=q.frame(float(s),y)
            local=q.project(frame["V"])
            gap=max(gap,float(np.max(abs(local-yp))))
            state=q.project(q.frame(float(s),y.astype(complex)+1j*1e-25*yp,
                strict=False)["V"]).imag/1e-25
            da=-frame["app"]/(frame["a"]*frame["kap"])+frame["ap"]**2/(frame["a"]**2*frame["kap"])
            db=-frame["al"]*da/frame["be"]
            DDY.append(state+q.project(da[:,None]*frame["N"]+db[:,None]*frame["B"]))
        DDY=np.asarray(DDY,dtype=float)
        if DDY.shape!=Y.shape or not np.all(np.isfinite(DDY)):
            raise ValueError("The full original finite-ODE second jet did not return")
        self.quintic=kernel.PhysicalQuintic(x,Y,DY,DDY)
        self.sol=SimpleNamespace(x=x,y=Y.T,p=np.empty(0),sol=self.quintic)
        self.flow=SimpleNamespace(end=float(x[-1]),
            breaks=np.asarray(self.profile_model.knots,float),
            profile=self.profile,bridge=SimpleNamespace(sigma=-1.))
        self.kind="complete-full-state-material-quintic"
        self.rotation_to_native=np.eye(2)
        self.translation_from_native=np.zeros(2)
        self.registration=None
        self.mode_identity=dict(schema=SCHEMA,
            accepted_checkpoint=copy.deepcopy(checkpoint.receipt),
            actual_original_fullDN=copy.deepcopy(checkpoint.manifest["members"]["fullDN"]),
            actual_field_modes=self.M,actual_tail_modes=self.M,actual_angular_quadrature=self.N,
            actual_resolution=copy.deepcopy(self.actual_resolution),
            augmented_state_dimension=4*self.M+2,physical_state_dimension=self.n,
            active_scalar_parameters=0,fixed_core_modes=0,
            separated_left_rows=self.n,right_rows=self.M,
            parameter_order=list(P.PARAMETERS),frozen_parameter_indices=list(range(10)),
            complete_ten_float64le=copy.deepcopy(checkpoint.target_identity["complete_ten_float64le"]),
            exact_target_point=copy.deepcopy(checkpoint.target_identity),
            actual_frozen_M_acceptance_not_parameter_row_deletion=True,
            same_target_freezing_not_a_continuous_isometry_certificate=True)
        nodal_identity={name:dict(shape=list(array.shape),dtype="<f8",
            sha256=hashlib.sha256(array.astype("<f8").tobytes()).hexdigest())
            for name,array in (("mesh",x),("Y",Y),("DY",DY),("DDY",DDY))}
        self.definition=dict(schema=SCHEMA,input_sha256=checkpoint.receipt["sha256"],
            source_sha256=digest(__file__),
            complete_accepted_checkpoint=copy.deepcopy(checkpoint.receipt),
            original_complete_state_jet_kernel_sha256=KERNEL_SHA,
            current_ten_checkpoint_source_sha256=CHECKPOINT_SHA,
            actual_resolution=copy.deepcopy(self.actual_resolution),
            material_Phi_uses_this_actual_core_not_parent_core=True,
            same_target_comparison_requires_the_actual_material_coordinate_transport=True,
            current_ten_profile_source_sha256=PROFILE_SHA,
            consumed_complete_physical_source_sha256=self.source_sha256,
            independent_field_modes=self.mode_identity,
            current_target_identity=copy.deepcopy(checkpoint.target_identity),
            nodal_jet_identity=nodal_identity,
            state_layout="r[0:M+1],t[1:M+1],z[0:M+1]; all3M+2 physical rows",
            full_core_M_retained=True,includes_entire_z0=True,old_mean_added=False,
            saved_first_jet_source="Original accepted frozen-physical RHS, not substituted by a point recomputation",
            saved_second_jet_source="Original complete FullCoreProbe finite-ODE formula at every actual node",
            node_saved_vs_local_RHS_max=gap,
            node_RHS_gap_is_readout_not_new_acceptance_gate=True,
            exact_field_definition="Unique exact rational Hermite quintic per cell through all binary64 Y,DY,DDY nodal values",
            exact_nodal_quintic_joins_share_the_identical_two_jet=True,
            rounded_PhysicalQuintic_coefficients_are_not_relabelled_exact=True,
            exact_Hermite_field_equals_numerical_render_at_all_points_not_proved=True,
            original_saved_field_to_exact_Hermite_geometry_error_not_certified=True,
            global_rho_lower_exact=str(self.rho_lower_exact),
            material_circle_diffeomorphism_source="unchanged R237 complete-core rational triangle bound",
            material_angle_formula="theta=phi+sum_{m=1}^{M} ((1-4m^2)c_m/(2m))*sin(2m*phi)",
            one_global_SE2_registration_still_required_for_actual_tail=True,
            original_C_tail_and_background_readout_not_created=True,
            complete_native_response_retained_but_not_a_radial_field=True,
            accurate_target_public_u_components=["L_true^2","a_true(L_true*u;p10)^2"],
            numerical_prefix_coordinate="s_numeric=L_numeric*u",
            accurate_C_root_family_not_replaced_by_numeric_midpoints=True,
            exact_target_domain_C2_full_seams_relative_metric_reach_and_held_unpaid=True,
            no_legacy_nine_v3_v4_or_finite_Gauss_schema_reused=True,
            accepted_field_created=False,closed_surface=False,task_completed=False)

    def __getattr__(self,name):
        kernel=self.__dict__.get("_kernel")
        if kernel is None:
            raise AttributeError(name)
        method=getattr(kernel.LargeCoreSavedPrefix,name,None)
        if method is None or not callable(method):
            raise AttributeError(name)
        return method.__get__(self,type(self))

    def exact_prefix_coefficients(self,index):
        """All3M+2 exact Hermite coefficient rows; compute only in Actions."""
        require_actions()
        if type(index) is not int or not 0<=index<len(self.quintic.x)-1:
            raise ValueError("Use an actual full prefix cell index")
        width=Q.from_float(float(self.quintic.x[index+1]))-Q.from_float(float(self.quintic.x[index]))
        return tuple(exact_hermite(
            tuple(Q.from_float(float(v[index,j])) for v in self.quintic.nodal),
            tuple(Q.from_float(float(v[index+1,j])) for v in self.quintic.nodal),
            width) for j in range(self.n))

    def complete_closed_input_scope(self):
        """Concrete outstanding inputs; this is not a legacy loader alias."""
        require_actions()
        cp=self.checkpoint.manifest
        return dict(schema=SCHEMA+"-closed-input-scope",
            actual_prefix=self.definition,
            actual_audited_native_response=copy.deepcopy(cp["members"]["final_native"]),
            actual_native_configuration=copy.deepcopy(cp["members"]["native_configuration"]),
            actual_current_C_geometry_result=copy.deepcopy(cp["members"]["native_geometry_result"]),
            actual_native_source_binding=copy.deepcopy(cp["original_native_binding"]),
            needed_current_C_radial_payload=dict(
                owner="a new source must evaluate this very final native checkpoint and current C geometry",
                all_nodes_modes_mean_and_two_radial_jets_required=True,
                current_C_finite_between_node_expression_must_be_declared=True,
                old6b06_RefinedTail_or_old_frozen_background_may_not_be_substituted=True),
            needed_shared_background=dict(
                owner="one actual B Hermite model used by both whole active sheets and both caps",
                exact_rational_nodes_values_first_second_and_cuff_cut_jets_required=True,
                B_is_geometry_only_not_the_accurate_target_g=True,
                current_C_cut_to_natural_Rout_and_unpaid_radial_domains_preserved=True),
            needed_closed_bundle=dict(
                arity7=["paths","plan","assembly","table","saved","A","binding"],
                saved_required_schema=SCHEMA,
                required_new_loader_and_source_guard=True,
                original_complete_material_pullback_SE2_cut_patch_collar_caps_retained=True,
                full_six_jet_mixed_terms_and_complete_angle_cover_required=True,
                actual_loader_not_yet_supplied_by_this_source=True),
            continuous_target_metric_consumer=dict(
                accurate_prefix_target_uses_all10_and_Ltrue_public_u=True,
                tail_target_is_original_C_E_not_one_plus_Bprime_squared=True,
                caps_original_relative_metric_error_zero_and_original_four_Loewner_conditions_required=True,
                actual_shared_B_field_required_before_closed_metric_evaluation=True),
            actual_shared_geometry_produced=False,continuous_metric_or_reach_proved=False)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint-directory",type=Path,required=True)
    parser.add_argument("--checkpoint-sha256",required=True)
    parser.add_argument("--code-directory",type=Path,default=HERE)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args(argv);require_actions()
    temp=Path(os.environ["RUNNER_TEMP"]).resolve()
    if args.out.exists() or not args.out.resolve().is_relative_to(temp):
        raise ValueError("Use a fresh owned temporary metadata file")
    saved=ContinuousTenSavedPrefix(args.checkpoint_directory,args.checkpoint_sha256,args.code_directory)
    result=saved.complete_closed_input_scope()
    result["actual_prefix_cut_scalar_jet"]=list(saved.profile(saved.flow.end))
    result["actual_cut_material_mean_012"]=[float(v[0]) for v in saved.mean_jets([saved.flow.end])]
    result["actual_nodes"]=len(saved.sol.x)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    raw=canonical(result);args.out.write_bytes(raw)
    print(json.dumps(dict(event="continuous-ten-frozen-M-prefix-read",
        output=dict(file=args.out.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()),
        actual_frozen_M_input_consumed=True,closed_field_created=False)),flush=True)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
