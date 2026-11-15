#!/usr/bin/env python3
"""Independent joint-nominal-Pruefer-current-C/R300-v3 complete453 physical-DN BVP adapter.

One actual current profile generates each physical H. The one live current-C
finite nonlinear owner returns its actual response/J, the unchanged R252 FD
runs, then the unchanged complete-band/full-DN main retains all original17
inner trials, eight outer iterations, RMS1e-6/BC1e-11, and fresh endpoint audit.
No old zeroJ, stored graph, successful native parent, or future field is used.
A complete original453 file is solely an explicitly reparameterized initial
guess. All current RHS values are recomputed before the original preflight.
The exact R300 target and numerical compiled/profile/native representatives
remain distinct objects: finite acceptance does not certify exact same-C
realization, evaluator error, continuous metric, C2, embedding, or reach.

Far rows come from the actual R380/R357 complete candidate-oriented unit-row
producer. The complete original family remains distinct from a jointly
formed nominal parameter-box row. All family-to-word errors are retained;
no nominal row is declared an exact global-C member. All native calls
use this same new matrix. No future row or successful response is assumed.

Only public Actions in Rogerhu12/math-research-public may execute science.
The external resource supervisor owns wall/disk limits, all complete readback,
and cleanup. There is no internal protocol-call cap or changed scientific gate.
"""
from __future__ import annotations
import argparse
from contextlib import contextmanager
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
import traceback
import types

HERE=Path(__file__).resolve().parent
ENTRY=Path(__file__).name
REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="current-C-pruefer-joint-nominal-R300-v3-three-active-complete453-physical-DN-v1"
RECIPE_SCHEMA="explicit-current-C-pruefer-joint-nominal-R300-v3-three-active-complete453-recipe-v1"
PARAMETER_ORDER=["p1","p2","p3","theta1","theta2","theta3","eta1","eta2","eta3"]
ACTIVE_INDICES=[0,1,2]
FROZEN_INDICES=[3,4,5,6,7,8]
CLIENT_NAME="geometry_20261115_current_C_pruefer_joint_tail_client.py"
BINDING_NAME="geometry_20261115_continuous_C_full112_binding.py"
SAMPLER_NAME="geometry_20261115_current_C_pruefer_joint_radial_sampling.py"
MODEL="R286-original-stored-continuous-model-convention-C-v1"

PINS = {
    "geometry_20261114_banded_collocation.py": "0780dcc4e331f6cde64141b0fa9ebdd1325eec2af87d94fc455e72405a0524f1",
    "geometry_20261114_constrained_trust_warm.py": "5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2",
    "geometry_20261114_fft_frenet.py": "973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401",
    "geometry_20261114_full_dn_augmented.py": "f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e",
    "geometry_20261114_full_dn_boundary.py": "4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2",
    "geometry_20261114_full_dn_prefix_controls.py": "7bb30855e5f0f5111ef55bbf9fafad8f6f0e8cdc26243780eda5b96600a3255a",
    "geometry_20261114_full_dn_response.py": "38d21971b3b0d462f8cf1b8f0a1cd174a28db3dcba450e89d0d0baecc5e26e74",
    "geometry_20261114_full_dn_solve.py": "c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162",
    "geometry_20261114_lifted_modes_banded_full_dn.py": "390387db4700f64302b76ee684f9a810a611c57c6617eb67d4597a9fa18905c4",
    "geometry_20261114_lifted_modes_full_dn.py": "d885ebc8de5ebd02f006c4104d8b67e856047b4e58f0e125651b38187fb251a5",
    "geometry_20261114_lifted_modes_prepare.py": "9a1ae018d71e38ff901c4b9156b23502a4efde44f812c1ff4e03323878b659db",
    "geometry_20261114_lifted_modes_profile.py": "13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5",
    "geometry_20261114_physical_test_boundary.py": "3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681",
    "geometry_20261114_physical_test_cut_audit.py": "7a548961ff0bd3e5171db18f1133d42f606be19e65e5d2e919432514042ba420",
    "geometry_20261114_physical_test_response.py": "83ce387778fb90209e841fc841a81ed3d99e15181d6e86210ec1244fde017e79",
    "geometry_20261114_projected_core_bvp.py": "2326720f124d2edc40e63089f8e07d6671e053ff108281efb59091d919f15c5b",
    "geometry_20261114_separated_qr_bvp.py": "c76bde190ff67a9e148d230c8e5e7d7a7899324c055e67faac6679b8fba10e39",
    "geometry_20261114_small_core_resonance.py": "3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5",
    "geometry_20261115_small_core_four_control_family.py": "9222390b73abbd2e8bc4a1f8e9d8b861cd66b4a927b21629deb2e6b70073dd11",
    "geometry_20261115_small_core_six_control_family.py": "79464f9c6af8863d3c65254701a858f067881b22ca80dba24bacf2bfea484acf",
    "geometry_20261115_small_core_nine_control_family.py": "086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629",
    "geometry_20261115_stored_continuous_E_cover_v3.py": "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df",
    "geometry_20261115_stored_continuous_E_cover_v2.py": "004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea",
    "geometry_20261115_stored_continuous_E_cover.py": "9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed",
    "tail_frozen_geometry.mjs": "db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3",
    "strong_frozen_calibration_factory.mjs": "77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247",
    "closure_bounded_point_cache.mjs": "35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043",
    "exact_20261114_closed_background.mjs": "be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b",
    "exact_20261114_public_resume.py": "11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5",
    "source-dependencies.json": "7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941",
    "root_20261114_current576_rules_runner.py": "3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde",
    "geometry_20261115_stored_C_v3_cut_twojet_readout.py": "1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed",
    "geometry_20261115_stored_continuous_C_far_graph.py": "fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a",
    "geometry_20261115_stored_C_finite_head_flux.py": "4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d",
    "geometry_20261115_stored_C_finite_head_projective.py": "5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216",
    "geometry_20261115_stored_C_finite_head_riccati.py": "34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124",
    "geometry_20261115_stored_C_finite_head_pruefer.py": "250474d748842d9b5423be2123460308ab16419d4b5dac1d8c9967fc208c0122",
    "geometry_20261115_current_C_general_robin_native.mjs": "fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349",
    "geometry_20261115_current_C_synchronous_linear_bridge.mjs": "67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286",
    "exact_20261115_current_C_general_robin_chain.py": "946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5",
    "geometry_20261115_current_C_projective_native_launch.py": "ae54abbb383269cbd2fd111c08a103b7eb8a14b15db01d09c2fcc8227488bf9d",
    "root_20261115_current_C_projective_native_scalar_readout.py": "8a3ddc5d59244b245292bd5a0e3fb33768527017148cc4e697d2f2cf771989e7",
    "exact_20261114_tail_capacity_loader.mjs": "07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395",
    "geometry_20261114_noj_matched_variational_engine.mjs": "f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9",
    "exact_20261114_native_damped_chain_qr.py": "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
    "geometry_20261115_nine_control_full112.py": "00e4d2c3413cfa6c1df915b9d85050bf375ab88c04e8756149d4ea0533ef3bd8",
    "geometry_20261115_continuous_C_full112_binding.py": "c0bda3350b30b9659c326112eaf8f411d0bb6f825a7a3f81fcc6c7502ed3f952",
    "geometry_20261115_continuous_nine_scalar_factory_v3.py": "0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e",
    "geometry_20261115_continuous_nine_scalar_numeric_v3.py": "7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60",
    "geometry_20261115_continuous_nine_augmented_v3.py": "d86f6fdf3cf59df3d45c907c655fe54ab830180facd27b7402e649b2e14d151b",
    "geometry_20261115_current_C_pruefer_joint_radial_sampling.py": "32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4",
    "geometry_20261115_current_C_pruefer_joint_native_worker.mjs": "d015a52c126b26a749ed1dfd60d613fdf09c54826a9465c7e38824d41bda6e4a",
    "geometry_20261115_current_C_pruefer_joint_tail_client.py": "02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1",
    "geometry_20261115_stored_C_finite_head_pruefer_positive.py": "c2f515aa276890da63871fe0e9e1440775950d4985465457e9d6025976d914c8",
    "geometry_20261115_pruefer_positive_endpoints.py": "91dd207bc20a87a36e2d4bc13e1b88a14333b67cf47ec048f85e8d46500822ff",
    "geometry_20261115_pruefer_joint_row_representative.py": "24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97"
}

NATIVE_PINS = {
    "geometry_20261115_stored_continuous_E_cover_v3.py": "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df",
    "geometry_20261115_stored_continuous_E_cover_v2.py": "004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea",
    "geometry_20261115_stored_continuous_E_cover.py": "9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed",
    "tail_frozen_geometry.mjs": "db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3",
    "strong_frozen_calibration_factory.mjs": "77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247",
    "closure_bounded_point_cache.mjs": "35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043",
    "exact_20261114_closed_background.mjs": "be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b",
    "exact_20261114_public_resume.py": "11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5",
    "source-dependencies.json": "7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941",
    "root_20261114_current576_rules_runner.py": "3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde",
    "geometry_20261115_stored_C_v3_cut_twojet_readout.py": "1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed",
    "geometry_20261115_stored_continuous_C_far_graph.py": "fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a",
    "geometry_20261115_stored_C_finite_head_flux.py": "4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d",
    "geometry_20261115_stored_C_finite_head_projective.py": "5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216",
    "geometry_20261115_stored_C_finite_head_riccati.py": "34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124",
    "geometry_20261115_stored_C_finite_head_pruefer.py": "250474d748842d9b5423be2123460308ab16419d4b5dac1d8c9967fc208c0122",
    "geometry_20261115_current_C_general_robin_native.mjs": "fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349",
    "geometry_20261115_current_C_synchronous_linear_bridge.mjs": "67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286",
    "exact_20261115_current_C_general_robin_chain.py": "946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5",
    "geometry_20261115_current_C_projective_native_launch.py": "ae54abbb383269cbd2fd111c08a103b7eb8a14b15db01d09c2fcc8227488bf9d",
    "root_20261115_current_C_projective_native_scalar_readout.py": "8a3ddc5d59244b245292bd5a0e3fb33768527017148cc4e697d2f2cf771989e7",
    "exact_20261114_tail_capacity_loader.mjs": "07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395",
    "geometry_20261114_noj_matched_variational_engine.mjs": "f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9",
    "exact_20261114_native_damped_chain_qr.py": "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
    "geometry_20261115_current_C_pruefer_joint_radial_sampling.py": "32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4",
    "geometry_20261115_current_C_pruefer_joint_native_worker.mjs": "d015a52c126b26a749ed1dfd60d613fdf09c54826a9465c7e38824d41bda6e4a",
    "geometry_20261115_current_C_pruefer_joint_tail_client.py": "02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1",
    "geometry_20261115_stored_C_finite_head_pruefer_positive.py": "c2f515aa276890da63871fe0e9e1440775950d4985465457e9d6025976d914c8",
    "geometry_20261115_pruefer_positive_endpoints.py": "91dd207bc20a87a36e2d4bc13e1b88a14333b67cf47ec048f85e8d46500822ff",
    "geometry_20261115_pruefer_joint_row_representative.py": "24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97"
}

ORIGINAL_RUNTIME_PINS = {
    "engine": "a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372",
    "product": "205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25",
    "root": "cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88",
    "cusp": "b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f",
    "physicalJet": "2b96df25211c5d6ebfc7faf689ea7035704bf0bf7c1ea3aa50b1c137fbe39ea8",
    "metric": "36e4e642014d5afd733ed3fecc13267d23c40927e1bd2113e53abcdbb588dcb4",
    "noJ": "f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9"
}

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()
def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('The complete scientific adapter may run only in public repository Actions')

def runtime():
    require_actions()
    for name, expected in PINS.items():
        if sha(HERE/name) != expected:
            raise ValueError('A frozen mathematical source differs: '+name)
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[key] = '1'
    import numpy as np
    from scipy.interpolate import CubicHermiteSpline
    import scipy.integrate._bvp as backend
    import geometry_20261115_small_core_nine_control_family as family
    import geometry_20261114_full_dn_solve as core
    import geometry_20261114_lifted_modes_banded_full_dn as banded
    import geometry_20261114_lifted_modes_prepare as preparation
    import geometry_20261114_physical_test_response as response
    from geometry_20261114_full_dn_augmented import AugmentedFlow, SeparatedBoundary
    from geometry_20261114_physical_test_boundary import PhysicalTestBoundary, SCHEMA as PHYSICAL_SCHEMA
    from geometry_20261114_physical_test_cut_audit import audit_cut
    from geometry_20261114_lifted_modes_profile import field_spec
    from geometry_20261114_full_dn_response import refined_directional_check
    closure = dict(core.FROZEN_SOURCES)
    for table in (family.checked_sources(), PINS):
        for name, expected in table.items():
            if name in closure and closure[name] != expected:
                raise ValueError('Two source responsibilities disagree: '+name)
            if sha(HERE/name) != expected:
                raise ValueError('A consumed mathematical source differs: '+name)
            closure[name] = expected
    closure[ENTRY] = sha(__file__)
    import geometry_20261115_continuous_C_full112_binding as current_binding
    import geometry_20261114_full_dn_augmented as actual_augmented
    import geometry_20261114_physical_test_boundary as actual_boundary
    return types.SimpleNamespace(**locals())

def clean(value):
    """JSON transport only; never turn a nonfinite value into accepted science."""
    if isinstance(value,dict):return {str(k):clean(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [clean(v) for v in value]
    if isinstance(value,float) and not math.isfinite(value):return {"nonfinite_repr":repr(value)}
    if hasattr(value,"tolist"):return clean(value.tolist())
    if isinstance(value,Path):return str(value)
    return value

def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()

def receipt(path):
    path=Path(path);return dict(file=str(path),bytes=path.stat().st_size,sha256=sha(path))

def raw_words(values):
    return b"".join(struct.pack("<d",float(v)) for v in values)

def checked_json(path,expected):
    from gzip import decompress
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=expected:raise ValueError("Actual input SHA differs: "+str(path))
    decoded=decompress(raw) if raw.startswith(b"\x1f\x8b") else raw
    return json.loads(decoded),dict(file=str(path),bytes=len(raw),sha256=expected,
        decoded_bytes=len(decoded),decoded_sha256=hashlib.sha256(decoded).hexdigest())

def finite_vector(values,count,name):
    if (not isinstance(values,list) or len(values)!=count or any(
        type(v) not in (int,float) or not math.isfinite(v) for v in values)):
        raise ValueError("Keep the complete finite "+name)
    return [float(v) for v in values]

def read_recipe(path,expected):
    value,identity=checked_json(path,expected)
    if (value.get("schema")!=RECIPE_SCHEMA or value.get("parameter_order")!=PARAMETER_ORDER
            or value.get("active_parameter_indices")!=ACTIVE_INDICES
            or value.get("frozen_parameter_indices")!=FROZEN_INDICES
            or value.get("initial_guess_kind")!="complete453-explicit-public-u-reparameterization"):
        raise ValueError("Declare the independent new-C, full453 initial-guess contract")
    finite_vector(value["initial_nine_parameters"],9,"current nine parameters")
    lam=value["lambda_target"]
    if type(lam) not in (int,float) or not math.isfinite(lam) or not 0<lam<=1:
        raise ValueError("One explicit positive lambda on the original low-core target path is required")
    if value.get("height_sign") not in (-1,1):
        raise ValueError("Declare the actual current physical height orientation")
    unchanged=dict(field_modes=112,field_angular_quadrature=2048,
        physical_state_dimension=338,state_dimension=453,material_angles=4096,
        physical_angles=4096,max_nodes=1200,outer_iterations=8,
        original_inner_trial_count=17,collocation_tolerance=1e-6,boundary_tolerance=1e-11,
        original_boundary_FD_threshold=5e-5)
    for k,v in unchanged.items():
        if value.get(k)!=v:raise ValueError("Keep the original complete algorithm parameter: "+k)
    seed=value.get("complete_initial_guess")
    if (not isinstance(seed,dict) or not isinstance(seed.get("source_sha256"),str)
            or len(seed["source_sha256"])!=64 or not isinstance(seed.get("origin"),dict)
            or not seed["origin"]):
        raise ValueError("The complete453 source bytes and their actual origin are required")
    for key in ("mesh_pointer","states_pointer"):
        if not isinstance(seed.get(key),str) or not seed[key].startswith("/"):
            raise ValueError("Explicit original JSON mesh/state pointers are required")
    return value,identity

def temporary_paths(args):
    root=Path(os.environ["RUNNER_TEMP"]).resolve()
    out,work=args.out.resolve(),args.work.resolve()
    if root not in out.parents or root not in work.parents:
        raise ValueError("All regenerable results/factors belong to actual RUNNER_TEMP")
    if out==work or out in work.parents or work in out.parents:
        raise ValueError("Separate the complete result tree and original band factors")
    for output in (out,work):
        for item in (args.recipe,args.accepted,args.complete_seed,args.factory_directory,
                     args.tail_config,args.tail_source_root,HERE):
            p=Path(item).resolve()
            if p==output or output in p.parents:
                raise ValueError("Owned output cannot contain an actual input/source")
        output.mkdir(parents=True,exist_ok=True)
        if any(output.iterdir()):raise ValueError("A fresh independent directory is required")
    return out,work

def bind_current_native(d,args,recipe,profile_owner):
    """Bind actual same-job C input/result, complete sampler, config and sources.

    No full-cut denominator is needed: the actual provider owns complete112
    nondividing rows at its explicitly selected physical finite far radius.
    Interval enclosures and binary64 representatives are not reclassified.
    """
    B=d.current_binding
    cfg,cfgrec=checked_json(args.tail_config,args.tail_config_sha256)
    if (cfg.get("schema")!="current-C-complete112-client-config-v1"
            or cfg.get("model_schema")!=MODEL or cfg.get("repository")!=REPOSITORY
            or Path(cfg["computations"]).resolve()!=HERE
            or Path(cfg["source_topic"]).resolve()!=args.tail_source_root.resolve()):
        raise ValueError("The actual current native config must belong to this checkout/source owner")
    for name,expected in NATIVE_PINS.items():
        if cfg.get("source_sha256",{}).get(name)!=expected or sha(HERE/name)!=expected:
            raise ValueError("Actual native source differs: "+name)
    if cfg.get("original_runtime_sha256")!=ORIGINAL_RUNTIME_PINS:
        raise ValueError("The original actual root/RK runtime identity changed")
    policy=dict(max_iterations=32,line_search_trials=10,nonlinear_tolerance=2e-9,
        eta=1,sensitivity_eta=0,reference_floor=1,projection_floor=.05,quadrature=2048,
        steps=12,linear_budget_seconds=1800,maximum_factor_bytes=2147483648)
    for key,expected in policy.items():
        if cfg.get(key)!=expected:raise ValueError("Keep the explicit original current-native policy: "+key)
    directory=Path(cfg["geometry_directory"]).resolve()
    report,rr=checked_json(directory/"result.json",cfg["geometry_result_sha256"])
    if (report.get("schema")!="current-C-pruefer-joint-nominal-row-physical-radial-samples-and-general-far-v1"
            or report.get("source_sha256")!=PINS[SAMPLER_NAME]
            or report.get("native_geometry_ready") is not True
            or report.get("completed") is not True
            or report.get("run_id")!=os.environ["GITHUB_RUN_ID"]
            or report.get("source_commit")!=os.environ["GITHUB_SHA"]):
        raise ValueError("This job must actually produce the complete current C geometry")
    native_binding=report["actual_original_input_binding"]
    if (B.original_C_core(native_binding["original_C_input_binding"])!=
            B.original_C_core(profile_owner.data["complete_C_binding"])):
        raise ValueError("The accurate new scalar and actual native sampler have different C definitions")
    tail=profile_owner.data["definition"]["continuous_tail"]
    if (native_binding["actual_cover_result"]["sha256"]!=tail["actual_result"]["sha256"]
            or native_binding["original_binary_cut_exact_rational"]!=str(profile_owner.data["cut"])):
        raise ValueError("Use this same actual C result and the exact unchanged physical cut")
    if (profile_owner.data["report"].get("run_id")!=os.environ["GITHUB_RUN_ID"]
            or profile_owner.data["report"].get("source_commit")!=os.environ["GITHUB_SHA"]):
        raise ValueError("The actual current factory must be produced in this job")
    geometry=B.member_json(directory,report["geometry"])
    if (geometry.get("schema")!="current-C-native-radial-geometry-bundle-v1"
            or geometry.get("model_schema")!=MODEL
            or geometry.get("modes")!=112 or geometry.get("stage_count")!=576
            or geometry.get("native_old_graphs_or_gains_used") is not False
            or geometry.get("original_C_input_binding")!=native_binding
            or geometry["numeric_geometry_identity"].get(
                "exact_global_C_realization_of_numeric_representatives_certified") is not False):
        raise ValueError("Actual geometry scope and complete C binding differ")
    if B.rational(geometry["cut_radius"])!=profile_owner.data["cut"]:
        # rational(float) retains the exact actual binary64 word in the binder.
        raise ValueError("The original current physical cut was relabelled")
    return cfg,dict(schema=SCHEMA+"-actual-current-native-binding",
        configuration=cfgrec,actual_geometry_result=rr,geometry=report["geometry"],
        actual_same_job_C_cover=native_binding["actual_cover_result"],
        accurate_factory_result=profile_owner.data["result_receipt"],
        current_C_common_input_binding=copy.deepcopy(native_binding),
        original_native_policy=policy,source_sha256=copy.deepcopy(cfg["source_sha256"]),
        original_runtime_sha256=copy.deepcopy(cfg["original_runtime_sha256"]),
        original_field_plan_and_all_actual_rounding_descriptors_retained=True,
        full112_general_far_rows_required=True,cut_height_division_not_requested=True,
        global_exact_C_realization_or_infinite_DN_certified=False,
        finite_numeric_provider_scope="fresh full nonlinear root/RK/means and all112 endpoint sensitivities")

def prepare_problem(d,args,recipe,inputs,output):
    np,core=d.np,d.core
    accepted,accepted_receipt=checked_json(args.accepted,inputs["accepted"])
    if (accepted.get("success") is not True or accepted.get("status")!=0
            or (accepted.get("M"),accepted.get("N"))!=(96,1024)
            or not 0<=accepted["collocation_rms_max"]<=1e-6
            or not 0<=accepted["boundary_residual_max"]<=1e-11):
        raise ValueError("Keep the genuine accepted96 source as source/target data only")
    target_owner=d.current_binding.CurrentProfile(
        args.factory_directory,args.factory_result_sha256,HERE)
    core_receipt=target_owner.data["definition"]["core_input"]
    if (core_receipt["sha256"]!=inputs["accepted"]
            or core_receipt["geometry_pointer"]!="/fixed_scalar_profile/geometry"):
        raise ValueError("The accurate current factory must retain this actual source core geometry")
    geometry=d.current_binding.json_pointer(accepted,core_receipt["geometry_pointer"])
    if hashlib.sha256(d.current_binding.canonical(geometry)).hexdigest()!=core_receipt["selected_geometry_canonical_sha256"]:
        raise ValueError("Actual source core geometry bytes differ from the factory selection")
    full_p=np.asarray(recipe["initial_nine_parameters"],float)
    shapes=full_p[3:].copy()
    view=target_owner.view(full_p,"three-active")
    # These are derived from the profile's OWN finite compiled leaves. The
    # native values are learned separately from a real current-H response.
    view.cut.update(backgroundSlope=math.sqrt(view.cut["E"]-1),
        backgroundSecond=view.cut["Ep"]/(2*math.sqrt(view.cut["E"]-1)))
    profile_cut_origin=dict(schema=SCHEMA+"-profile-numeric-cut",
        accurate_cut_hulls=target_owner.data["semantic_cut_hulls"],
        profile_own_compiled_cut=dict(view.cut),
        numeric_background_formula="sqrt(E0-1); E1/(2 sqrt(E0-1))",
        native_response_used_to_overwrite_profile_target=False,
        exact_C_evaluator_error_or_same_root_realization_certified=False)
    original_targets=np.asarray(accepted["core"]["coefficients"],float)[:3]
    target=float(recipe["lambda_target"])*original_targets
    core_seed=np.zeros(112);core_seed[:3]=target
    law=accepted["original_metric_identity"]["law"]
    q=core.original_solver.native.outward.FullCoreProbe(core_seed,112,2048,
        law["velocity"],law["length"],law["k0"])
    q.profile=view.profile
    core.original_solver.fixed.fft.enable_fft(q)
    flow=target_owner.flow(d.actual_augmented,q,view,args.jac_workers)
    affine=core.AffineTail(112)
    boundary=target_owner.boundary(d.actual_boundary,view,target,flow,affine,
        height_sign=recipe["height_sign"],material_angles=args.material_angles,
        physical_angles=args.physical_angles)
    if (flow.dimension,flow.n,flow.M,flow.k)!=(453,338,112,3):
        raise ValueError("All physical338/core112/active3 rows are required")
    cfg,native_binding=bind_current_native(d,args,recipe,target_owner)
    parent=recipe["complete_initial_guess"]
    seed=d.current_binding.read_complete453_guess(target_owner,view,flow,
        source_file=args.complete_seed,source_sha256=parent["source_sha256"],
        mesh_pointer=parent["mesh_pointer"],states_pointer=parent["states_pointer"],
        actual_active_parameters=full_p[:3])
    mesh,values,rhs=seed["mesh"],seed["states"],seed["rhs"]
    seed_receipt=dict(seed)
    for key in ("mesh","states","rhs","public_u"):seed_receipt.pop(key,None)
    seed_receipt["origin"]=parent["origin"]
    core.write(output/"complete-source-seed-binding.json",seed_receipt)
    if not np.all(np.isfinite(rhs)):
        raise FloatingPointError("The new target's fresh complete453 node RHS failed its original domain")
    guess=dict(kind=recipe["initial_guess_kind"],source_identity=seed["source_identity"],
        original_full453_source_used_only_as_initial_guess=True,
        full_public_u_reparameterization_and_fresh_RHS=True,
        old_scalar_or_tail_or_parent_acceptance_not_inherited=True,
        original_physical338_and_core112_preserved=True,
        only_explicit_three_active_rows_replaced=True,
        source_original_negative_zero_words_not_exported_not_claimed_recovered=True,
        actual_seed_binding=receipt(output/"complete-source-seed-binding.json"),
        lambda_target=float(recipe["lambda_target"]))
    at=curve_with_exact_nodes(d,mesh,values,rhs)
    preflight=bound_original_preflight(d,output,core.write)
    mesh,values,rhs,residual,additions=preflight(mesh,at,flow,args.max_nodes)
    specification=view.export_specification(values[-1,flow.parameter_slice])
    record=dict(schema=SCHEMA,scope=__doc__,M=112,N=2048,
        mesh=mesh.tolist(),states=values.tolist(),rhs=rhs.tolist(),
        complete_scalar_profile=specification,field_representation=d.field_spec(112,2048),
        state_layout="all physical338, constant core112, constant active p1/p2/p3",
        initial_collocation_max=core.finite_max(residual),preflight_added_nodes=additions,
        initial_guess=guess,current_exact_profile_binding=target_owner.binding,
        current_native_geometry_binding=native_binding,profile_cut_origin=profile_cut_origin,
        success=False,new_coupled_finite_acceptance=False,complete_closed_surface=False,
        current_exact_target_metric_or_infinite_DN_certified=False)
    return types.SimpleNamespace(**locals())

def curve_with_exact_nodes(d, mesh, values, rhs):
    curve = d.CubicHermiteSpline(mesh, values, rhs, axis=0)
    np = d.np

    def at(points):
        points = np.asarray(points)
        result = curve(points)
        index = np.searchsorted(mesh, points)
        safe = np.minimum(index, len(mesh)-1)
        saved = (index < len(mesh)) & (mesh[safe] == points)
        result[saved] = values[index[saved]]
        return result

    return at
def bound_original_preflight(d, output, writer):
    # The frozen helper calls original.preflight internally. Preserve that
    # exact preflight function even when core.main is given this full RMS layer.
    proxy = types.SimpleNamespace(preflight=d.core.preflight,
                                  original_solver=d.core.original_solver)
    globals_ = dict(d.preparation.complete_preflight.__globals__)
    globals_.update(original=proxy, write=writer)
    copied = types.FunctionType(d.preparation.complete_preflight.__code__, globals_,
        name='original_complete_RMS_preflight', argdefs=d.preparation.complete_preflight.__defaults__)

    def run(mesh, initial_at, flow, max_nodes):
        return copied(mesh, initial_at, flow, max_nodes, output)

    return run

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
        physical_test=boundary.description(), current_C_full112_implementation=binding,
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
        restored=finite_vector(cp.get("cutHeight"),112,"actual returned physical H")
        zeros=cp.get("cutHeight_negative_zero_columns",[])
        if not isinstance(zeros,list) or zeros!=sorted(set(zeros)):
            raise ValueError("Actual returned height signed-zero sidecar differs")
        for j in zeros:
            if type(j) is not int or not 0<=j<112 or restored[j]!=0:
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

@contextmanager
def restore_attributes():
    saved = []
    def replace(obj, name, value):
        saved.append((obj, name, getattr(obj, name)))
        setattr(obj, name, value)
    def preserve(obj, name):
        saved.append((obj, name, getattr(obj, name)))
    try:
        yield replace, preserve
    finally:
        for obj, name, value in reversed(saved):
            setattr(obj, name, value)

def original_full_solve(d, args, problem, binding, seed_path, port_path, output, owner):
    """Keep the original complete-band and core main bodies unmodified."""
    np, core, continuation = d.np, d.core, d.banded.continuation
    plain_write, previous_seam = core.write, core.final_height_seam
    context = dict(boundary=None, cut_audit=None, statistics_active_parameters=None)
    final_preflight = bound_original_preflight(d, output, plain_write)
    prepared_at = curve_with_exact_nodes(d, problem.mesh, problem.values, problem.rhs)
    original_band_write = d.banded.write

    def band_write(path, data, *positional, **keywords):
        if isinstance(data, dict) and Path(path).name == 'complete-banded-intent.json':
            data.update(mathematical_BC_changed=True, equation_row_permutation_only=False,
                linear_backend_is_only_row_permutation_of_current_physical_test=True,
                new_scalar_and_explicit_lambda_are_bound_by_independent_adapter=True,
                current_C_full112_implementation=binding,
                actual_native_client_source_sha256=args.expected_tail_client_sha256,
                original_finite_current_C_native_policy_preserved=True,
                old_finite_tail_reused_or_relabelled=False)
            data.pop('native_tail_changed', None)
        return original_band_write(path, data, *positional, **keywords)

    def scalar_spec(profile, port, active, accepted_sha):
        if profile is not problem.view or accepted_sha != binding['input_sha256']['accepted']:
            raise ValueError('The new nine-control scalar owner/source changed')
        record=profile.export_specification(active)
        record["current_C_full112_binding"]=binding
        record["current_finite_numerical_shadow_solved_only_when_original_main_accepts"]=True
        return record

    def make_profile(source, port, peak, source_modes):
        if (source_modes != 96 or peak != args.legacy_peak_curvature_argument
                or port != problem.current_port or source != problem.accepted):
            raise ValueError('The original constructor metadata or actual current port identity changed')
        return problem.view

    def constructor(core_values, M, N, velocity, length, k0):
        if (M, N) != (96, 1024) or not np.array_equal(core_values, problem.accepted['core']['coefficients']):
            raise ValueError('The genuine accepted96 source was reclassified')
        law = problem.accepted['original_metric_identity']['law']
        if (velocity, length, k0) != (law['velocity'], law['length'], law['k0']):
            raise ValueError('The original physical source law changed')
        return problem.q

    def flow_constructor(probe,profile,workers):
        if probe is not problem.q or profile is not problem.view or workers!=args.jac_workers:
            raise ValueError("The current original physical flow owner changed")
        return problem.target_owner.flow(d.actual_augmented,probe,profile,workers)

    def boundary(profile, old_target, rhs, jacobian, affine, *, angular):
        if (profile is not problem.view or angular != args.material_angles
                or not np.array_equal(old_target, problem.original_targets)):
            raise ValueError('The source target must remain original before applying the explicit lambda')
        # The unchanged original boundary gets the current complete RHS/J,
        # the same new scalar, and the actually selected lambda target.
        result = d.PhysicalTestBoundary(profile, problem.target, rhs, jacobian, affine,
            height_sign=problem.boundary.eh, radial_sign=-1,
            angular=angular, physical_angles=args.physical_angles)
        result.current_C_profile_binding=profile.current_C_boundary_binding
        context['boundary'] = result
        return result

    def initial_guess(source, profile, flow, extension_step, taper_fraction):
        if profile is not problem.view or flow.dimension != 453:
            raise ValueError('The complete initial guess layout/scalar changed')
        return problem.mesh.copy(), prepared_at, dict(problem.guess,
            actual_preflight_warm_sha256=sha(seed_path), source_accepted_prefix_not_reclassified=True)

    def load_client(module_path, config, sources, prefix, heap):
        if (Path(module_path).resolve() != args.tail_client.resolve()
                or Path(config).resolve() != args.tail_config.resolve()
                or Path(sources).resolve() != args.tail_source_root.resolve()
                or Path(prefix).resolve() != (output/'true-tail').resolve()
                or heap != args.node_heap):
            raise ValueError('The original full-DN call must retain the exact actual-H FD client owner')
        return owner

    def final_seam(boundary_, flow, q, endpoint, actual):
        result = previous_seam(boundary_, flow, q, endpoint, actual)
        active = np.array(endpoint[flow.parameter_slice], copy=True)
        context['statistics_active_parameters'] = active
        q.profile = lambda s: flow.profile.profile(s, active)
        cut = d.audit_cut(boundary_, flow, endpoint, actual,
                          angular_levels=(args.material_angles, 2*args.material_angles))
        context['cut_audit'] = cut
        plain_write(output/'physical-test-final-cut-audit.json', cut)
        result.update(old_material_test_not_the_acceptance_gate=True,
            finite_boundary_scheme='physical-phi-complete-DN-v1',
            physical_test_final_cut_audit_file='physical-test-final-cut-audit.json',
            physical_test_final_cut_audit_sha256=sha(output/'physical-test-final-cut-audit.json'))
        return result

    def write(path, data):
        if isinstance(data, dict):
            name = Path(path).name
            if name in ('driver-status.json', 'prepared.json.gz', 'actual.json.gz') or name.endswith('-pending.json.gz'):
                data.update(schema=SCHEMA, scope=__doc__, source_sha256=sha(__file__),
                    unchanged_full_DN_core_source_sha256=PINS['geometry_20261114_full_dn_solve.py'],
                    field_representation=d.field_spec(112, 2048),
                    finite_boundary_scheme='physical-phi-complete-DN-v1',
                    current_C_full112_implementation=binding,
                    active_parameter_indices=ACTIVE_INDICES, frozen_parameter_indices=FROZEN_INDICES,
                    original_large_target_scaled_only_by_explicit_lambda=True,
                    source_prefix_or_circle_acceptance_not_inherited=True)
                if 'complete_scalar_profile' in data:
                    data['complete_nine_scalar_parameters'] = data['complete_scalar_profile']['nine_parameters']
            if name == 'actual.json.gz':
                if context['cut_audit'] is None or context['statistics_active_parameters'] is None:
                    raise RuntimeError('Keep the original physical-test cut measurement and frozen-p statistics')
                data['original_source_metric_identity'] = data.pop('original_metric_identity')
                data['original_metric_identity'] = dict(schema='R300-v3-current-numerical-shadow-material-metric-v1',
                    scalar_specification=data['complete_scalar_profile'],
                    core_coefficients=data['core']['coefficients'],
                    material_coordinate='common theta; ds_numeric^2+a_numeric(s_numeric)^2*dtheta^2',
                    public_coordinate='u=s_numeric/L_numeric; accurate target uses its own L_true',
                    accurate_family_binding=problem.target_owner.binding,
                    same_g_as_original_source_claimed=False,
                    exact_R300_target_solved_or_metric_error_certified=False)
                data['solved_metric_definition'].update(
                    scope='Actual finite numerical evaluator; exact target approximation error remains unpaid',
                    exact_target_binding=problem.target_owner.binding,
                    exact_global_C_realization_or_infinite_DN_certified=False,
                    same_g_as_old_finite_scalar=False)
                data['sampled_geometry_scalar_parameters'] = context['statistics_active_parameters'].tolist()
                data['physical_test_final_cut_audit'] = context['cut_audit']
                data['scope'] = __doc__
                data['message'] = 'Current-C/R300 numerical full453 physical-phi DN accepted by the unchanged finite gates; exact target, continuous DN and closed geometry remain unpaid.'
                data['same_metric_refinement'] = False
            if name == 'driver-status.json' and data.get('new_coupled_finite_acceptance'):
                data['new_coupled_finite_acceptance_refers_to'] = SCHEMA
        return plain_write(path, data)

    def enter_core():
        # banded.main has installed this frozen closure, including the original
        # released_newton call and its read-only trial wrapper.
        continuation.install_qr_diagnostics(output, 112, plain_write)
        return core.main()

    old_argv = sys.argv
    argv = [ENTRY, '--accepted', str(args.accepted), '--port', str(port_path),
        '--out', str(output), '--work', str(args.work), '--warm', str(seed_path),
        '--tail-client', str(args.tail_client), '--tail-config', str(args.tail_config),
        '--tail-source-root', str(args.tail_source_root), '--peak-curvature',
        str(args.legacy_peak_curvature_argument),
        '--jac-workers', str(args.jac_workers), '--max-nodes', str(args.max_nodes),
        '--material-angles', str(args.material_angles), '--node-heap', str(args.node_heap),
        '--tol', '1e-6', '--outer-iterations', str(args.outer_iterations)]
    try:
        with restore_attributes() as (replace, preserve):
            for obj, name in ((continuation, 'install_qr_diagnostics'),
                    (core.original_solver, 'released_newton'), (core.original_solver, 'original_splu'),
                    (core.original_qr, 'enable'), (core.original_qr, 'DiskQRFactor'),
                    (d.backend, 'prepare_sys'), (d.backend, 'solve_newton')):
                preserve(obj, name)
            for name, value in (('scalar_spec', scalar_spec), ('CompleteProfile', make_profile),
                    ('FullDNBoundary', boundary), ('AugmentedFlow',flow_constructor),
                    ('prepared_guess', initial_guess),
                    ('preflight', final_preflight), ('load_client', load_client),
                    ('final_height_seam', final_seam), ('write', write)):
                replace(core, name, value)
            replace(core.original_solver.native.outward, 'FullCoreProbe', constructor)
            replace(d.banded, 'write', band_write)
            replace(continuation, 'main', enter_core)
            sys.argv = argv
            return d.banded.main()
    finally:
        sys.argv = old_argv


def make_runtime_compatibility(args,problem,out):
    """Add only the original solver's explicit modes/spacing metadata.

    The actual current-native config source and geometry identities remain
    byte-bound and are copied without mathematical changes. No old port or
    native result is used to create this current record.
    """
    cfg=copy.deepcopy(problem.cfg)
    for key,value in (("modes",112),("spacing",2)):
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

def main(argv=None):
    require_actions()
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("recipe","accepted","complete-seed","factory-directory","tail-config",
                 "tail-source-root","out","work"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--recipe-sha256",required=True)
    parser.add_argument("--accepted-sha256",required=True)
    parser.add_argument("--factory-result-sha256",required=True)
    parser.add_argument("--tail-config-sha256",required=True)
    parser.add_argument("--tail-client",type=Path,default=HERE/CLIENT_NAME)
    parser.add_argument("--jac-workers",type=int,default=2)
    parser.add_argument("--node-heap",type=int,default=6144)
    args=parser.parse_args(argv)
    recipe,recipe_identity=read_recipe(args.recipe,args.recipe_sha256)
    if args.jac_workers<=0 or args.node_heap<=0:
        raise ValueError("Explicit positive worker and Node memory resources are required")
    # These controls are the old complete solve contract, not new accuracy gates.
    args.max_nodes=recipe["max_nodes"]
    args.material_angles=recipe["material_angles"]
    args.physical_angles=recipe["physical_angles"]
    args.outer_iterations=recipe["outer_iterations"]
    args.legacy_peak_curvature_argument=2.5
    if (args.tail_client.resolve()!=HERE/CLIENT_NAME
            or sha(args.tail_client)!=PINS[CLIENT_NAME]):
        raise ValueError("The actual current-C live implementation is an independent frozen source")
    d=runtime()
    inputs=dict(accepted=sha(args.accepted),complete_seed=sha(args.complete_seed),
        factory_result=sha(args.factory_directory/"result.json"),tail_config=sha(args.tail_config))
    if (inputs["accepted"]!=args.accepted_sha256
            or inputs["accepted"]!=d.family.EXPECTED["accepted"]
            or inputs["accepted"]!=recipe["accepted_source_sha256"]
            or inputs["complete_seed"]!=recipe["complete_initial_guess"]["source_sha256"]
            or inputs["factory_result"]!=args.factory_result_sha256
            or inputs["tail_config"]!=args.tail_config_sha256):
        raise ValueError("Every source and actual current runtime result must retain its complete bytes")
    out,work=temporary_paths(args)
    owner=None
    session=dict(schema=SCHEMA,source_sha256=sha(__file__),
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        phase="preparing",success=False,new_coupled_finite_acceptance=False,
        full_Cartesian_closed_surface=False,exact_R300_target_or_continuous_C_DN_certified=False,
        recipe=recipe_identity,input_sha256=inputs,consumed_source_sha256=d.closure,
        resource_scope=dict(outer_iterations=8,first_current_H_FD_anchor_calls=1,
            maximum_original_protocol_solve_entries=18,
            maximum_is_algorithm_path_count_not_an_added_call_limit=True,
            all_native_calls_keep_original_32_iterations_and_10_trials=True,
            no_same_process_worker_split_or_cross_process_response_cache=True,
            one_call_storage_preflight_is_not_a_full_BVP_capacity_guarantee=True,
            resource_supervisor_must_preserve_actual_partial_readback_before_cleanup=True),
        no_current_accepted_field_or_native_parent_assumed=True)
    d.core.write(out/"adapter-status.json",session)
    try:
        seed_dir,fd_dir,full_dir=out/"initial-guess",out/"actual-H-response",out/"full-DN"
        for path in (seed_dir,fd_dir,full_dir):path.mkdir()
        problem=prepare_problem(d,args,recipe,inputs,seed_dir)
        actual_args,port_path=make_runtime_compatibility(args,problem,seed_dir)
        binding=dict(schema=SCHEMA+"-complete-input-binding",source_sha256=sha(__file__),
            consumed_source_sha256=d.closure,input_sha256=inputs,recipe=recipe_identity,
            source_accepted_prefix=dict(M=96,N=1024,sha256=inputs["accepted"],
                used_only_for_actual_source_core_geometry_target_and_constructor_metadata=True),
            lambda_target=float(recipe["lambda_target"]),
            original_low_core_targets=problem.original_targets.tolist(),
            current_fixed_low_core_targets=problem.target.tolist(),
            initial_nine_parameters=problem.full_p.tolist(),
            initial_nine_float64le=[struct.pack("<d",float(x)).hex() for x in problem.full_p],
            actual_frozen_shape_coefficients=problem.shapes.tolist(),
            active_parameter_indices=ACTIVE_INDICES,frozen_parameter_indices=FROZEN_INDICES,
            parameter_order=PARAMETER_ORDER,state_dimension=453,physical_state_dimension=338,
            field_modes=112,tail_modes=112,core_unknowns=112,high_core_free_unknowns=109,
            left_rows=341,right_rows=112,
            current_profile_binding=problem.target_owner.binding,
            current_native_binding=problem.native_binding,
            current_profile_numeric_cut_origin=problem.profile_cut_origin,
            actual_current_port=receipt(port_path),
            actual_BVP_compatible_config=receipt(actual_args.tail_config),
            explicit_current_client_source=dict(file=CLIENT_NAME,sha256=PINS[CLIENT_NAME]),
            physical_flow_adapter=problem.flow.r300_source_binding,
            current_scalar_specification=problem.view.export_specification(problem.full_p[:3]),
            all_338_physical_and_112_core_and_3_active_rows_retained=True,
            original_complete_FD_threshold=5e-5,original_inner_trial_count=17,
            original_collocation_and_frozen_RMS_tolerance=1e-6,original_BC_tolerance=1e-11,
            true_final_native_full_J_and_fresh_audit_required=True,
            old_zero_anchor_J_old_port_graphs_or_source_acceptance_inherited=False,
            whole_cut_linear_R324_denominator_gate_added=False,
            factory_interval_domain_result_is_not_a_new_BVP_gate=True,
            same_new_g_450_refinement_supplied=False,
            later_same_new_g_requires_all_nine_frozen_and_K_equals_k_equals_zero=True,
            finite_numeric_Evaluator_or_global_same_C_realization_error_unpaid=True,
            exact_R300_target_closed_geometry_metric_or_reach_certificate=False)
        problem.record["current_C_full112_implementation"]=binding
        seed_path=seed_dir/"prepared.json.gz"
        d.core.write(seed_path,problem.record)
        session.update(phase="fresh-unaccepted-complete453-preflight",
            implementation=binding,prepared_sha256=sha(seed_path),
            initial_collocation_max=problem.record["initial_collocation_max"])
        d.core.write(out/"adapter-status.json",d.response.clean(session))
        owner=SharedNativeClient(d.core.load_client(actual_args.tail_client,
            actual_args.tail_config,actual_args.tail_source_root,full_dir/"true-tail",
            actual_args.node_heap),fd_dir)
        H=d.core.true_height(problem.boundary,problem.values[-1])
        height_record=dict(schema=SCHEMA+"-actual-first-physical-height",
            formula="Original true_height: current original RHS and full MaterialTrace of actual complete453 endpoint",
            actual_current_full_height=H.tolist(),
            actual_current_full_height_float64le=[struct.pack("<d",float(x)).hex() for x in H],
            actual_current_height_sha256=hashlib.sha256(raw_words(H)).hexdigest(),
            source_prepared=receipt(seed_path),current_profile_binding=problem.target_owner.binding,
            current_C_native_binding=problem.native_binding,
            old_zero_J_or_supplied_literal_height_or_cached_parent_used=False)
        d.core.write(fd_dir/"actual-first-height-input.json",height_record)
        session.update(phase="solving-actual-current-profile-height",
            first_actual_height=receipt(fd_dir/"actual-first-height-input.json"))
        d.core.write(out/"adapter-status.json",d.response.clean(session))
        actual=owner.solve(H,jacobian=True,audit=False)
        d.core.write(fd_dir/"initial-actual-H-tail.json.gz",actual)
        # READY was not a solved anchor. Use the just-computed response's actual
        # cut words, and preserve the exact five original comparisons.
        comparisons=[]
        for key in ("radius","E","Ep","backgroundSlope","backgroundSecond"):
            passed=bool(d.np.isclose(float(owner.cut[key]),float(problem.view.cut[key]),
                rtol=2e-11,atol=2e-13))
            comparisons.append(dict(field=key,native_actual_word=struct.pack("<d",float(owner.cut[key])).hex(),
                profile_own_word=struct.pack("<d",float(problem.view.cut[key])).hex(),
                native_actual_value=float(owner.cut[key]),profile_own_value=float(problem.view.cut[key]),
                original_isclose_passed=passed,rtol=2e-11,atol=2e-13))
        d.core.write(fd_dir/"original-five-cut-comparisons.json",dict(schema=SCHEMA,
            rows=comparisons,actual_response_cut_origin=owner.cut_response_identity,
            no_profile_target_value_replaced=True,
            exact_real_same_C_seam_or_evaluator_error_certified=False))
        session["actual_first_cut_comparisons"]=receipt(fd_dir/"original-five-cut-comparisons.json")
        if not all(row["original_isclose_passed"] for row in comparisons):
            session["phase"]="original-physical-cut-identity-not-matched"
            return 2
        passed,report=actual_boundary_fd(d,problem,actual,H,fd_dir,binding,seed_path)
        session.update(phase="original-actual-H-FD-returned",actual_current_H=H.tolist(),
            response_check_sha256=sha(fd_dir/"response-check.json"),
            original_boundary_FD_passed=passed,
            maximum_boundary_FD_relative_error=report["maximum_relative_directional_error"])
        d.core.write(out/"adapter-status.json",d.response.clean(session))
        if not passed:return 2
        status=original_full_solve(d,actual_args,problem,binding,seed_path,port_path,full_dir,owner)
        final=d.core.read(full_dir/"driver-status.json")
        session.update(phase="original-full-DN-returned",original_full_DN_exit_status=status,
            original_full_DN_phase=final.get("phase"),
            new_coupled_finite_acceptance=final.get("new_coupled_finite_acceptance") is True,
            original_driver_status_sha256=sha(full_dir/"driver-status.json"))
        session["success"]=bool(status==0 and session["new_coupled_finite_acceptance"])
        return status
    except Exception as error:
        session.update(phase="exception",exception=repr(error),traceback=traceback.format_exc())
        raise
    finally:
        if owner is not None:
            try:owner.close()
            except Exception as error:session["native_close_exception"]=repr(error)
            finally:
                session["native_live_calls"]=owner.calls
                session["native_owner_close_attempted"]=owner.close_attempted
                session["native_owner_closed"]=owner.closed
                session["native_owner_close_exception"]=owner.close_exception
        d.core.write(out/"adapter-status.json",d.response.clean(session))
        # Full actual member/trial readback belongs to the independent reader;
        # this bounded event is never a substitute for the original records.
        event=dict(event="current-C-complete453-full-BVP-returned",schema=SCHEMA,
            phase=session["phase"],success=session["success"],
            new_coupled_finite_acceptance=session["new_coupled_finite_acceptance"],
            original_full_DN_phase=session.get("original_full_DN_phase"),
            lambda_target=recipe["lambda_target"],
            actual_protocol_solve_entries=len(session.get("native_live_calls",[])),
            maximum_boundary_FD_relative_error=session.get("maximum_boundary_FD_relative_error"),
            exact_target_or_infinite_DN_or_closed_surface_not_certified=True,
            adapter_status_sha256=sha(out/"adapter-status.json"),
            exception=session.get("exception"))
        print(json.dumps(d.response.clean(event),allow_nan=False),flush=True)

if __name__=="__main__":
    raise SystemExit(main())
