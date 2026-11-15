#!/usr/bin/env python3
"""Append only missing old-radial Airy Taylor degrees through twelve.

Every original target, FFT, intrinsic, cubic and finite-output stage is retained.
New supporting algebra is saved separately and only new output degrees are built.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,shutil,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
import flint
from flint import acb,arb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as L

PUBLIC="Rogerhu12/math-research-public"
ROOT="397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
RB="10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"
HIGH="38a8ba8d2998a75ddb863fe9b486defd756a22488e1c3a96ed8bf54581877e8f"
HPROC="3b06c881b8b00f8bb830653b3eb290b09687b0a2576320b605ba758e2e706abe"
HSOURCE="c3bb77f96f05ceedd05a0fc4cda39d591065d4ee2203fd7b05be79169d04709d"
FOLD="84e2bd1b7637299e94428b22cc19aba290d0b661f9dbe18dae918bf752f10077"
FPROC="855730f8bf86d04c6cc7622e1881f9fc29a2af754694dfaf5dad16012b98544e"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
RESPONSE="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
OLD_NATIVE="18990ac2c1ed8e559d00982b75d663c08ad7e193455de1f8482511c36938b719"
OLD_PROCESS="eebbbf37419729069c28ef3cd7c7d34f02154b8c391b0cfa9ca093de8855a356"
OLD_SOURCE="e4ccbf4b343623d74d089f79b6605a0601975c6ea5c1d2e113bad568fe60167d"
OLD_MANIFEST="226e5acac42026431acbd166f92d423b6292ba6f73e65f58f808647d4701f1ad"
HIGHER_NATIVE="ec702cffb8d1dcb25cdb01eaa89127b1f0044ae1cd3cee9e6e293e8165250480"
HIGHER_PROCESS="c7ff69243d3f724f539cd0ee95c2b0ba219caa5ffba47ff9b084387255e78e5b"
HIGHER_SOURCE="a3ff4be3d252dbbc5571924b36927760ace54db91b5e00477749b2f97ba9ace7"
CONTRACT="8bf949ce602ecd2dfa23ded74a78d01aa8b75881b5ccf9a5905a46512f105862"
DELTA=Q(1,10**8)
COUNT=15
ORDER=12
RHO=Q(1,6000)
SIGMA=Q(1,128)
HREAL=Q(9,10**6)
WIDTHS=(Q(0),Q(1,1024),Q(1,512))
I=acb(0,1)

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,separators=(",",":"),allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,compresslevel=6,mtime=0)
    tmp=path.with_name(path.name+".partial");tmp.write_bytes(raw);tmp.replace(path)
def ex(q):return L.ex(q)
def up(v):return abs(v).upper()
def rb(v):
    if isinstance(v,str):return arb(v)
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def cb(v):return acb(rb(v["real"]),rb(v["imag"]))
def record(v):return dict(ball=L.rec(v,90))
def encode(value):
    if isinstance(value,dict):return {k:encode(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [encode(v) for v in value]
    return record(value)
def decode(value):
    if isinstance(value,dict):
        if "ball" in value:return rb(value)
        return {k:decode(v) for k,v in value.items()}
    if isinstance(value,list):return [decode(v) for v in value]
    return value
def interval(a,b):return ex(a).union(ex(b))
def sqr(x):return x*x
def ipow(x,n):
    if n<0:raise ValueError("negative integer exponent must use a paid denominator")
    y=arb(1)
    for _ in range(n):y=y*x
    return y
def series(payload):return {k:L.unpack_series(v) for k,v in payload.items()}
def pack(values):return {k:L.pack_series(v) for k,v in values.items()}
def cprod(a,b,n):
    """A triangular product: an unpaid coefficient is allowed only against exact zero."""
    if n<0:return L.LP.zero()
    out=L.LP.zero()
    for j in range(n+1):
        k=n-j
        if j<len(a) and k<len(b):out+=a[j]*b[k]
        elif j<len(a) and a[j].is_zero():continue
        elif k<len(b) and b[k].is_zero():continue
        else:raise ValueError("triangular recurrence requested an unpaid nonzero factor")
    return out
def D(a,d,count):
    L.require(a,count+1);L.require(d,count)
    return L.sub(L.scale(L.dr(a),-1,count),L.mul(d,L.theta(a),count),count)

def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def static_old_name(name):
    return isinstance(name,str) and name.replace("-","").replace("_","").isalnum()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","out"):parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--resume",type=Path)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new Taylor extension mathematics requires the actual public Actions repository")
    import scipy
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise RuntimeError("the exact completed runtime changed")
    if args.out.exists():raise FileExistsError("preserve every prior native and scientific prefix")
    ctx.prec=320;ctx.cap=4
    start=time.monotonic()
    doc=dict(kind="append_only_complete_old_rho_first_Airy_Taylor_through_twelve",
        complete=False,proved=False,failure=None,gates=[],original_stages={},stages={},
        source_sha256=sha(__file__),algebra_sha256=sha(L.__file__),
        input_manifest_sha256=sha(args.manifest),runtime=runtime,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        original_Taylor_native_sha256=OLD_NATIVE,original_Taylor_process_sha256=OLD_PROCESS,
        original_Taylor_source_sha256=OLD_SOURCE,original_Taylor_manifest_sha256=OLD_MANIFEST,
        higher_intrinsic_native_sha256=HIGHER_NATIVE,higher_intrinsic_process_sha256=HIGHER_PROCESS,
        higher_intrinsic_source_sha256=HIGHER_SOURCE,contract_sha256=CONTRACT,
        complete_larger_fold_native_sha256=FOLD,complete_larger_fold_process_sha256=FPROC,
        background_definition_sha256=BASE,explicit_direction_definition_sha256=ZDEF,
        actual_intrinsic_parameter="eta_0",exact_complex_delta_radius=str(DELTA),
        leading_Taylor_order=COUNT-1,forcing_Taylor_order=ORDER,first_correction_Taylor_order=ORDER,
        complete_non_circular_Fourier_algebra=True,physical_angle_frequency_multiplier=4,
        principal_mu_uses_B_plus_and_leading_a0_uses_B_minus=True,
        original_target_FFT_intrinsic_cubic_ray_or_auxiliary_stages_recomputed=0,
        original_completed_finite_output_stages_recomputed=0,
        original_completed_natural_stage_count=75,original_stages_copied=0,
        new_finite_algebra_stages=0,reused_finite_algebra_stages=0,
        new_unsaved_supporting_algebra_stages=0,reused_unsaved_supporting_algebra_stages=0,
        new_output_degrees=0,reused_new_output_degrees=0,
        new_Fourier_norm_rows=0,reused_new_Fourier_norm_rows=0,
        new_N12_budgets=0,reused_new_N12_budgets=0,
        original_cubic_component_rows_reused=258,
        new_cubic_component_rows=0,exact_structural_views=[],
        branch_epsilon_computed=1,negative_branch_reused_by_exact_same_complex_parameter_symmetry=True,
        all_original_physical_seams_and_independent_mean_equations_retained=True,
        physical_background_outside_original_piece_replaced=False,
        old_circle_I_J_or_independent_even_mean_budget_paid=False,
        complete_strong_return_or_cutoff97_inverse_claimed=False)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(args.out,doc)
    def gate(name,value):
        okay=bool(value);doc["gates"].append(dict(name=name,passed=okay))
        if not okay:raise ValueError("append-only Taylor gate failed: "+name)
    def original_stage(name):
        if name not in doc["original_stages"]:raise ValueError("an accepted old finite stage is missing: "+name)
        r=doc["original_stages"][name];path=args.out.parent/r["file"]
        if sha(path)!=r["sha256"] or path.stat().st_size!=r["bytes"]:
            raise ValueError("an exact original finite stage changed bytes: "+name)
        value=read(path)
        if not (value["stage"]==name and value["complete"]
            and value["source_sha256"]==OLD_SOURCE and value["input_manifest_sha256"]==OLD_MANIFEST
            and value["algebra_sha256"]==doc["algebra_sha256"] and value["runtime"]==runtime):
            raise ValueError("an original finite stage changed its separately pinned old identity")
        return value["payload"]
    def stage(name,build,kind="new_output"):
        if not static_old_name(name) or name in doc["original_stages"]:
            raise ValueError("a new stage attempts to replace an old output")
        if name in doc["stages"]:
            r=doc["stages"][name];path=args.out.parent/r["file"]
            if not path.is_file() or sha(path)!=r["sha256"] or path.stat().st_size!=r["bytes"]:
                raise ValueError("a completed new extension prefix changed")
            value=read(path)
            if not (value["stage"]==name and value["complete"] and value["stage_kind"]==kind
                and value["source_sha256"]==doc["source_sha256"]
                and value["algebra_sha256"]==doc["algebra_sha256"]
                and value["input_manifest_sha256"]==doc["input_manifest_sha256"]
                and value["original_Taylor_native_sha256"]==OLD_NATIVE
                and value["higher_intrinsic_native_sha256"]==HIGHER_NATIVE and value["runtime"]==runtime):
                raise ValueError("a saved new extension stage changed its full scientific identity")
            doc["reused_finite_algebra_stages"]+=1
            if kind=="new_unsaved_helper":doc["reused_unsaved_supporting_algebra_stages"]+=1
            elif kind=="new_Fourier_norm":doc["reused_new_Fourier_norm_rows"]+=1
            elif kind=="new_N12_budget":doc["reused_new_N12_budgets"]+=1
            else:doc["reused_new_output_degrees"]+=1
            return value["payload"]
        payload=build()
        path=args.out.parent/"stages"/(name+".json.gz")
        if path.exists():raise FileExistsError("an unindexed complete new stage must be preserved")
        value=dict(stage=name,complete=True,stage_kind=kind,source_sha256=doc["source_sha256"],
            algebra_sha256=doc["algebra_sha256"],input_manifest_sha256=doc["input_manifest_sha256"],
            original_Taylor_native_sha256=OLD_NATIVE,higher_intrinsic_native_sha256=HIGHER_NATIVE,
            runtime=runtime,payload=payload)
        save(path,value)
        if path.stat().st_size>5_000_000:
            raise ValueError("one natural new Taylor stage exceeds the declared five-megabyte gate")
        doc["stages"][name]=dict(file=str(path.relative_to(args.out.parent)),
            bytes=path.stat().st_size,sha256=sha(path),stage_kind=kind)
        doc["new_finite_algebra_stages"]+=1
        if kind=="new_unsaved_helper":doc["new_unsaved_supporting_algebra_stages"]+=1
        elif kind=="new_Fourier_norm":doc["new_Fourier_norm_rows"]+=1
        elif kind=="new_N12_budget":doc["new_N12_budgets"]+=1
        else:doc["new_output_degrees"]+=1
        checkpoint()
        return payload
    def helper(name,build):
        row=stage("helper-"+name,lambda:dict(name=name,coefficients=L.pack_series(build())),
            kind="new_unsaved_helper")
        if row["name"]!=name:raise ValueError("a supporting series changed its name")
        return L.unpack_series(row["coefficients"])
    def append_series(name,previous,degree_count,build):
        result=list(previous)
        for degree in range(len(previous),degree_count):
            row=stage(name+"-degree-"+str(degree).zfill(3),
                lambda degree=degree:dict(name=name,degree=degree,coefficient=build(degree,result).record()))
            if row["name"]!=name or row["degree"]!=degree:
                raise ValueError("a newly appended scalar degree changed its location")
            result.append(L.LP.restore(row["coefficient"]))
        return result
    try:
        manifest=read(args.manifest)
        gate("the immutable public contract requests only the missing degree-twelve extension",
            manifest["public_repository"]==PUBLIC
            and manifest["mathematical_parameters"]["Taylor_order"]==ORDER
            and manifest["mathematical_parameters"]["leading_Taylor_order"]==COUNT-1)
        for pin in manifest["files"]:
            path=args.repo_root/pin["path"]
            if not path.is_file() or sha(path)!=pin["sha256"] or path.stat().st_size!=pin["bytes"]:
                raise ValueError("an exact completed mathematical input changed: "+pin["path"])
        paths={key:args.repo_root/value for key,value in manifest["input_paths"].items()}
        old,oproc,high,hproc,fold,fproc=[read(paths[key]) for key in
            ("old_native","old_process","higher_native","higher_process","fold_native","fold_process")]
        gate("both original computations and the unchanged larger fold are actual complete successes",
            sha(paths["old_native"])==OLD_NATIVE and sha(paths["old_process"])==OLD_PROCESS
            and sha(paths["higher_native"])==HIGHER_NATIVE and sha(paths["higher_process"])==HIGHER_PROCESS
            and sha(paths["fold_native"])==FOLD and sha(paths["fold_process"])==FPROC
            and all(v["complete"] and v["proved"] and v["failure"] is None
                and all(g["passed"] for g in v["gates"]) for v in (old,high,fold))
            and all(v["complete"] and v["actual_returncode"]==0 and v["mathematical_complete"]
                and v["mathematical_failure"] is None for v in (oproc,hproc,fproc)))
        gate("the exact original sources manifests and all seventy-five finite files remain accepted",
            old["source_sha256"]==oproc["mathematical_source_sha256"]==OLD_SOURCE
            and old["input_manifest_sha256"]==OLD_MANIFEST and len(old["stages"])==75
            and high["source_sha256"]==hproc["mathematical_source_sha256"]==HIGHER_SOURCE
            and high["original_high_native_sha256"]==old["complete_high_root_native_sha256"]==HIGH
            and oproc["all_complete_Fourier_arrays_and_all_natural_prefix_files_verified"]
            and hproc["all_available_natural_stage_files_verified"])
        roots=list(map(Q,old["exact_root_interval"]));cell=list(map(Q,old["exact_original_physical_piece_interval"]))
        gate("the repaired family fixed intrinsic parameter complex delta and physical root piece agree",
            old["background_definition_sha256"]==fold["background_definition_sha256"]==BASE
            and old["explicit_direction_definition_sha256"]==fold["explicit_direction_definition_sha256"]==ZDEF
            and old["actual_intrinsic_parameter"]==high["actual_intrinsic_parameter"]==fold["actual_intrinsic_parameter"]=="eta_0"
            and old["exact_fixed_intrinsic_parameter"]==high["exact_fixed_intrinsic_parameter"]
            and Q(old["exact_complex_delta_radius"])==Q(fold["exact_complex_delta_radius"])==DELTA
            and old["exact_root_interval"]==high["exact_root_interval"]==fold["exact_root_interval"]
            and old["exact_original_physical_piece_interval"]==high["exact_original_physical_piece_interval"]
            and list(map(Q,fold["exact_original_piece_interval"]))==cell)
        rawjets=high["intrinsic_stage"]["ordinary_old_radial_jets"]
        originaljets=high["original_intrinsic_stage"]["ordinary_old_radial_jets"]
        gate("sixteen complete ordinary intrinsic derivatives extend the exact old ten without padding",
            high["intrinsic_stage"]["complete"] and high["intrinsic_stage"]["complete_primitive_and_product_errors_included"]
            and high["intrinsic_stage"]["missing_series_coefficients_padded_with_zero"] is False
            and set(rawjets)=={"K","beta","gamma","s"} and all(len(v)==16 for v in rawjets.values())
            and all(rawjets[k][:10]==v for k,v in originaljets.items())
            and high["exact_original_finite_point_and_low_order_records_preserved"]
            and high["at_the_certified_true_root"]["exact_K0"]=="0"
            and high["original_finite_point_payload_sha256"]==old["original_completed_point_payload_sha256"])
        doc.update(exact_root_interval=copy.deepcopy(old["exact_root_interval"]),
            exact_original_physical_piece_interval=copy.deepcopy(old["exact_original_physical_piece_interval"]),
            exact_fixed_intrinsic_parameter=old["exact_fixed_intrinsic_parameter"],
            old_product_domain=copy.deepcopy(old["old_product_domain"]),
            cubic_point_rows=copy.deepcopy(old["cubic_point_rows"]),
            original_complete_branch_identity=copy.deepcopy(old["complete_branch_identity"]),
            original_first_correction_derivative_budgets=copy.deepcopy(old["first_correction_derivative_budgets"]),
            original_complete_Fourier_coefficient_support=copy.deepcopy(old["complete_Fourier_coefficient_support"]),
            original_structural_views=copy.deepcopy(old["exact_structural_views"]),
            original_original_point_payload_sha256=old["original_completed_point_payload_sha256"],
            original_finite_reference_payload_hashes=copy.deepcopy(high["original_reference_payload_hashes"]))
        for name,entry in old["stages"].items():
            relative=Path(entry["file"])
            if (not static_old_name(name) or relative.is_absolute() or ".." in relative.parts
                or relative!=Path("stages")/(name+".json.gz")):
                raise ValueError("an original natural stage changed its exact relative path")
            source=paths["old_native"].parent/relative;target=args.out.parent/relative
            if not source.is_file() or sha(source)!=entry["sha256"] or source.stat().st_size!=entry["bytes"]:
                raise ValueError("a complete original finite stage is unavailable or changed: "+name)
            target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
            if sha(target)!=entry["sha256"]:raise ValueError("an original finite byte copy differs")
            doc["original_stages"][name]=copy.deepcopy(entry);doc["original_stages_copied"]+=1
            original_stage(name)
        checkpoint()
        if args.resume:
            previous=read(args.resume)
            gate("every accepted new prefix has identical new sources runtime and both original computations",
                previous["source_sha256"]==doc["source_sha256"]
                and previous["algebra_sha256"]==doc["algebra_sha256"]
                and previous["input_manifest_sha256"]==doc["input_manifest_sha256"] and previous["runtime"]==runtime
                and previous["original_Taylor_native_sha256"]==OLD_NATIVE
                and previous["higher_intrinsic_native_sha256"]==HIGHER_NATIVE
                and previous["original_stages"]==doc["original_stages"])
            for name,entry in previous["stages"].items():
                relative=Path(entry["file"])
                if (not static_old_name(name) or name in doc["original_stages"]
                    or relative!=Path("stages")/(name+".json.gz")):
                    raise ValueError("a new resume stage attempts to replace the old inventory")
                source=args.resume.parent/relative;target=args.out.parent/relative
                if not source.is_file() or sha(source)!=entry["sha256"] or source.stat().st_size!=entry["bytes"]:
                    raise ValueError("an accepted new natural prefix changed bytes")
                target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
                doc["stages"][name]=copy.deepcopy(entry)
            doc["preserved_actual_extension_prefix"]=dict(native_sha256=sha(args.resume),
                original_failure=previous["failure"],original_gates=previous["gates"],
                original_complete=previous["complete"],accepted_new_stages=len(previous["stages"]))
            checkpoint()
        case=fold["cases"][1]
        gate("the original complete auxiliary amplitudes and unchanged old product certificate are retained",
            case["complete"] and case["proved"] and case["failure"] is None
            and all(g["passed"] for g in case["gates"])
            and Q(case["exact_fold_radius"])==Q(3,8000)
            and Q(old["old_product_domain"]["exact_rho_radius"])==RHO
            and Q(old["old_product_domain"]["exact_phi_width"])==SIGMA
            and Q(old["old_product_domain"]["exact_physical_inner_radius"])==HREAL)
        coeff_bounds=decode(case["characteristic_refinement_evidence"]["complete_refined_coefficient_majorants"])
        f_bounds=decode(case["fold_evidence"]["complete_fold_and_leading_bounds"])
        original_amp=decode(case["first_forcing_evidence"]["separated_first_amplitudes"])
        hcover=HREAL+roots[1]-roots[0]
        gate("the old complete physical inner cover and all original output norms have identical domains",
            Q(old["old_product_domain"]["exact_physical_rho_cover_radius"])==hcover
            and old["old_product_domain"]["exact_physical_interval"]==[str(roots[0]-HREAL),str(roots[1]+HREAL)]
            and len(old["first_correction_derivative_budgets"])==3
            and all(Q(v["exact_output_phi_width"])==WIDTHS[j]
                for j,v in enumerate(old["first_correction_derivative_budgets"])))

        # Only degrees absent from the complete old output are appended.
        old_background=original_stage("complete-background-root-series")
        c=series(old_background["series"])
        gate("all accepted original background lists have exactly nine complete coefficients",
            set(c)=={"u","v","K","beta","gamma","s","k","eta","a","S","d","e_d"}
            and all(len(v)==9 for v in c.values())
            and old_background["zero_bump_germ_and_fixed_eta0"]
            and old_background["positive_order_value_repair_derivatives_exactly_zero"]
            and old_background["complete_mean_at_all_orders_retained"])
        for degree in range(9,COUNT):
            def build_inputs(degree=degree):
                values={key:L.LP.scalar(acb(rb(rawjets[key][degree]))*
                    ex(Q((-1)**degree,math.factorial(degree)))) for key in ("K","beta","gamma","s")}
                values["u"]=L.LP.zero()
                values["v"]=values["s"]
                values["k"]=L.LP.scalar(acb(rb(rawjets["K"][degree+1]))*
                    ex(Q((-1)**degree,math.factorial(degree+1))))
                return dict(degree=degree,coefficients={key:v.record() for key,v in values.items()},
                    original_cubic_and_constant_repair_higher_coefficients_exactly_zero=True,
                    independent_mean_intrinsic_s_retained=True)
            row=stage("background-inputs-degree-"+str(degree).zfill(3),build_inputs)
            if row["degree"]!=degree:raise ValueError("a new background input degree changed")
            for key,value in row["coefficients"].items():c[key].append(L.LP.restore(value))
        khalf=helper("radial-k-half-through-fourteen",lambda:L.power(c["k"],Q(1,2),COUNT))
        mv=helper("complete-background-mean-v-through-fourteen",lambda:L.mean(c["v"]))
        uu=helper("complete-background-u-square-through-fourteen",lambda:L.mul(c["u"],c["u"],COUNT))
        vv=helper("complete-background-v-square-through-fourteen",lambda:L.mul(c["v"],c["v"],COUNT))
        for degree in range(9,COUNT):
            def build_background(degree=degree):
                eta=-cprod(c["gamma"],mv,degree)
                achar=cprod(c["eta"]+[eta],khalf,degree)
                ss=uu[degree]+cprod(c["K"],vv,degree)
                return dict(degree=degree,eta=eta.record(),a=achar.record(),S=ss.record())
            row=stage("background-main-degree-"+str(degree).zfill(3),build_background)
            if row["degree"]!=degree:raise ValueError("a new complete background degree changed")
            for key in ("eta","a","S"):c[key].append(L.LP.restore(row[key]))
        primitiveS=helper("complete-background-primitive-S-through-fourteen",lambda:L.primitive(c["S"]))
        for degree in range(9,COUNT):
            def build_drift(degree=degree):
                drift=-cprod(c["beta"],primitiveS,degree)
                return dict(degree=degree,d=drift.record(),e_d=(-drift).record())
            row=stage("background-drift-degree-"+str(degree).zfill(3),build_drift)
            if row["degree"]!=degree:raise ValueError("a new complete drift degree changed")
            for key in ("d","e_d"):c[key].append(L.LP.restore(row[key]))
        gate("all fifteen background coefficients retain the old mean and exact new cubic zeros",
            all(len(v)==COUNT for v in c.values())
            and all(q.is_zero() for q in c["u"][9:])
            and all(q.degree<=96 for q in c["u"]+c["v"])
            and all(q.degree<=192 for q in c["S"]+c["d"])
            and c["eta"][0].scalar_value().real>0 and c["k"][0].scalar_value().real>0)

        chi=[];A=[]
        for degree in range(COUNT):
            name="fold-degree-"+str(degree).zfill(3)
            if degree<=8:row=original_stage(name)
            else:
                def build_fold(degree=degree):
                    xp=L.theta(chi);xp[0]+=1
                    xx=(cprod(c["e_d"],xp,degree-1)
                        +cprod(c["a"],L.theta(A),degree-3).scale(ex(Q(2,3)))).divide_scalar(degree)
                    xpnew=L.theta(chi+[xx]);xpnew[0]+=1
                    aa=(cprod(c["e_d"],L.theta(A),degree-1).scale(2)
                        +cprod(c["a"],xpnew,degree).scale(3)).divide_scalar(2*degree+3)
                    if xx.degree>192*degree or aa.degree>192*degree:
                        raise ValueError("a complete new fold coefficient exceeds the exact finite support")
                    return dict(degree=degree,chi=xx.record(),A=aa.record(),full_non_circular_support=True)
                row=stage(name,build_fold)
            if row["degree"]!=degree:raise ValueError("a complete fold degree changed identity")
            chi.append(L.LP.restore(row["chi"]));A.append(L.LP.restore(row["A"]))
        gate("the complete fold appends only nine through fourteen and retains the original root anchor",
            len(chi)==len(A)==COUNT and chi[0].is_zero() and A[0].scalar_value().real>0)

        old_leading={}
        for key in ("Xp","T","Q","EG","G","B_minus","B_plus","mu","a0","b0","mu_inverse"):
            row=original_stage("leading-complete-"+key)
            if row["name"]!=key or len(row["coefficients"])!=9:
                raise ValueError("an original complete leading prefix changed")
            old_leading[key]=L.unpack_series(row["coefficients"])
        powers={}
        for name,power,normalized,base in (
            ("A-two-thirds",Q(2,3),False,A),
            ("A-minus-one-third",Q(-1,3),False,A),
            ("normalized-A-one-sixth",Q(1,6),True,A),
            ("normalized-k-minus-one-quarter",Q(-1,4),True,c["k"])):
            powers[name]=helper(name+"-through-fourteen",
                lambda base=base,power=power,normalized=normalized:L.power(base,power,COUNT,normalized=normalized))
        exponential_rhs=helper("radial-EG-transport-coefficients-through-thirteen",
            lambda:L.scale(L.mul(c["beta"],L.mean(c["S"]),COUNT-1),2))
        leading={}
        leading["Xp"]=append_series("leading-Xp",old_leading["Xp"],COUNT,
            lambda degree,out:chi[degree].theta())
        leading["T"]=append_series("leading-T",old_leading["T"],COUNT,
            lambda degree,out:-powers["A-two-thirds"][degree-1])
        leading["Q"]=append_series("leading-Q",old_leading["Q"],COUNT,
            lambda degree,out:cprod(c["a"],powers["A-minus-one-third"],degree))
        leading["EG"]=append_series("leading-EG",old_leading["EG"],COUNT,
            lambda degree,out:cprod(exponential_rhs,out,degree-1).divide_scalar(degree))
        Gpower=helper("complete-G-fractional-product-through-fourteen",
            lambda:L.mul(powers["normalized-A-one-sixth"],powers["normalized-k-minus-one-quarter"],COUNT))
        leading["G"]=append_series("leading-G",old_leading["G"],COUNT,
            lambda degree,out:cprod(Gpower,leading["EG"],degree))
        Tphi=helper("complete-T-angular-derivative-through-fourteen",lambda:L.theta(leading["T"]))
        Tphi2=helper("complete-T-angular-square-through-fourteen",lambda:L.mul(Tphi,Tphi,COUNT))
        for key,sign in (("B_minus",-1),("B_plus",1)):
            leading[key]=append_series("leading-"+key,old_leading[key],COUNT,
                lambda degree,out,sign=sign:cprod(leading["Xp"],leading["Xp"],degree)
                    +cprod(leading["T"],Tphi2,degree).scale(sign))
        Qsquare=helper("complete-Q-square-through-fourteen",lambda:L.mul(leading["Q"],leading["Q"],COUNT))
        leading["mu"]=append_series("leading-mu",old_leading["mu"],COUNT,
            lambda degree,out:cprod(Qsquare,leading["B_plus"],degree))
        leading["a0"]=append_series("leading-a0",old_leading["a0"],COUNT,
            lambda degree,out:cprod(leading["G"],leading["B_minus"],degree))
        GXp=helper("complete-G-Xphi-product-through-fourteen",lambda:L.mul(leading["G"],leading["Xp"],COUNT))
        leading["b0"]=append_series("leading-b0",old_leading["b0"],COUNT,
            lambda degree,out:cprod(GXp,Tphi,degree).scale(-2*I))
        leading["mu_inverse"]=append_series("leading-mu_inverse",old_leading["mu_inverse"],COUNT,
            lambda degree,out:sum((leading["mu"][j]*out[degree-j] for j in range(1,degree+1)),
                L.LP.zero()).divide_scalar(-leading["mu"][0].scalar_value()))
        gate("all original normalized leading constants and both different B signs are preserved",
            all(len(v)==COUNT for v in leading.values())
            and leading["G"][0].scalar_value()==1 and leading["a0"][0].scalar_value()==1
            and leading["b0"][0].is_zero() and leading["b0"][1].is_zero()
            and leading["T"][0].is_zero() and leading["Xp"][0].scalar_value()==1)

        # Old operator coefficients are returned literally. The two multiplier
        # coefficients at degree thirteen are genuinely new derivative inputs.
        op=series(original_stage("complete-local-operator-series"))
        expected_op={"T0","V0","vartheta","crossd","angular2","ell","epoly","bloc","rQ","tQ"}
        gate("all original operator output prefixes remain complete through six",
            set(op)==expected_op and all(len(v)==7 for v in op.values()))
        uv=helper("complete-u-v-product-through-thirteen",lambda:L.mul(c["u"],c["v"],ORDER+2))
        kvv=helper("complete-K-v-square-through-thirteen",lambda:L.mul(c["K"],vv,ORDER+2))
        earg=helper("complete-epoly-argument-through-thirteen",
            lambda:L.add(L.constant(1,ORDER+2),L.add(L.scale(uu,3),kvv,ORDER+2),ORDER+2))
        barg=helper("complete-bloc-argument-through-thirteen",
            lambda:L.sub(L.constant(1,ORDER+2),L.add(uu,L.scale(kvv,3),ORDER+2),ORDER+2))
        ell=list(op["ell"]);epoly=list(op["epoly"]);bloc=list(op["bloc"])
        for degree in range(7,ORDER+2):
            def build_multipliers(degree=degree):
                out=dict(degree=degree,ell=cprod(c["beta"],uv,degree).scale(-2).record(),
                    bloc=cprod(c["beta"],barg,degree).record())
                if degree<=ORDER:out["epoly"]=(-cprod(c["beta"],earg,degree)).record()
                return out
            row=stage("local-multipliers-degree-"+str(degree).zfill(3),build_multipliers)
            if row["degree"]!=degree:raise ValueError("a new internal multiplier degree changed")
            ell.append(L.LP.restore(row["ell"]));bloc.append(L.LP.restore(row["bloc"]))
            if degree<=ORDER:epoly.append(L.LP.restore(row["epoly"]))
        etainv=helper("complete-eta-inverse-through-twelve",lambda:L.inverse(c["eta"],ORDER+1))
        logeta=helper("complete-eta-log-rho-through-twelve",lambda:L.mul(L.dr(c["eta"]),etainv,ORDER+1))
        dphi=helper("complete-d-angular-derivative-through-thirteen",lambda:L.theta(L.take(c["d"],ORDER+2)))
        ellphi=helper("complete-ell-angular-derivative-through-thirteen",lambda:L.theta(ell))
        blocphi=helper("complete-bloc-angular-derivative-through-thirteen",lambda:L.theta(bloc))
        ephi=helper("complete-epoly-angular-derivative-through-twelve",lambda:L.theta(epoly))
        betaeta=helper("complete-beta-eta-product-through-twelve",lambda:L.mul(c["beta"],c["eta"],ORDER+1))
        upu=helper("complete-u-angular-u-product-through-twelve",lambda:L.mul(L.theta(c["u"]),c["u"],ORDER+1))
        vup=helper("complete-v-u-angular-product-through-twelve",lambda:L.mul(c["v"],L.theta(c["u"]),ORDER+1))
        betaK=helper("complete-beta-K-product-through-twelve",lambda:L.mul(c["beta"],c["K"],ORDER+1))
        vvp=helper("complete-v-v-angular-product-through-twelve",lambda:L.mul(c["v"],L.theta(c["v"]),ORDER+1))
        eta2=helper("complete-eta-square-through-twelve",lambda:L.mul(c["eta"],c["eta"],ORDER+1))
        logpart=helper("complete-Q-logpart-through-twelve",
            lambda:L.add(L.scale(logeta,-1),dphi,ORDER+1))
        inner=helper("complete-AC-local-potential-through-twelve",
            lambda:L.sub(L.mul(ell,ell,ORDER+1),L.scale(L.mul(betaeta,vup,ORDER+1),4),ORDER+1))
        for degree in range(7,ORDER+1):
            def build_operator(degree=degree):
                tq=logpart[degree]+epoly[degree]
                T0=-logeta[degree]-exponential_rhs[degree].scale(2)+dphi[degree].scale(5)
                rq=ell[degree+1].scale(-(degree+1))-cprod(c["d"],ellphi,degree)
                rq+=cprod(c["eta"],ephi,degree)-cprod(betaeta,upu,degree).scale(2)
                rq-=cprod(ell,logpart,degree)
                vt=cprod(op["rQ"]+[rq],etainv,degree)-cprod(betaK,vvp,degree).scale(2)
                Db=bloc[degree+1].scale(-(degree+1))-cprod(c["d"],blocphi,degree)
                V0=cprod(op["tQ"]+[tq],bloc,degree)-Db-cprod(c["K"],inner,degree)
                cd=c["d"][degree+1].scale(degree+1)+cprod(c["d"],dphi,degree)
                a2=cprod(c["d"],c["d"],degree)+cprod(eta2,c["K"],degree)
                values=dict(T0=T0,V0=V0,vartheta=vt,crossd=cd,angular2=a2,
                    ell=ell[degree],epoly=epoly[degree],bloc=bloc[degree],rQ=rq,tQ=tq)
                return dict(degree=degree,coefficients={key:v.record() for key,v in values.items()},
                    internal_ell_and_bloc_degree_thirteen_retained=True)
            row=stage("complete-local-operator-degree-"+str(degree).zfill(3),build_operator)
            if row["degree"]!=degree or set(row["coefficients"])!=expected_op:
                raise ValueError("a new complete local operator degree changed")
            for key,value in row["coefficients"].items():op[key].append(L.LP.restore(value))
        gate("all degree-twelve local outputs and the necessary multiplier-thirteen inputs are complete",
            all(len(v)==ORDER+1 for v in op.values()) and len(ell)==len(bloc)==ORDER+2)

        T,Xp,Qc,a0,b0=[leading[k] for k in ("T","Xp","Q","a0","b0")]
        wr=[];wrr=[];wphi=[];wrphi=[];wphiphi=[]
        for label,values in (("a0",a0),("b0",b0)):
            rr=helper("complete-"+label+"-rho-derivative-through-thirteen",lambda values=values:L.dr(values))
            rr2=helper("complete-"+label+"-rho-second-through-twelve",lambda rr=rr:L.dr(rr))
            pp=helper("complete-"+label+"-phi-derivative-through-fourteen",lambda values=values:L.theta(values))
            rp=helper("complete-"+label+"-rho-phi-through-thirteen",lambda rr=rr:L.theta(rr))
            pp2=helper("complete-"+label+"-phi-second-through-fourteen",lambda values=values:L.theta(values,2))
            wr.append(rr);wrr.append(rr2);wphi.append(pp);wrphi.append(rp);wphiphi.append(pp2)
        w=[a0,b0]
        vq=helper("complete-vartheta-Q-through-twelve",lambda:L.mul(op["vartheta"],Qc,ORDER+1))
        T0d=helper("complete-T0-d-through-twelve",lambda:L.mul(op["T0"],c["d"],ORDER+1))
        Tb0=helper("complete-T-b0-through-twelve",lambda:L.mul(T,b0,ORDER+1))
        nums=[[],[]];F=[[],[]]
        for degree in range(ORDER+1):
            name="forcing-degree-"+str(degree).zfill(3)
            if degree<=6:row=original_stage(name)
            else:
                def build_forcing(degree=degree):
                    nb=[]
                    for h in range(2):
                        value=wrr[h][degree]+cprod(c["d"],wrphi[h],degree).scale(2)
                        value+=cprod(op["crossd"],wphi[h],degree)
                        value+=cprod(op["angular2"],wphiphi[h],degree)
                        value+=cprod(op["T0"],wr[h],degree)
                        value+=cprod(T0d,wphi[h],degree)
                        value+=cprod(op["V0"],w[h],degree)
                        cross=cprod(vq,Tb0 if h==0 else a0,degree).scale(I)
                        nb.append(value+cross)
                    force=[-cprod(leading["mu_inverse"],nums[h]+[nb[h]],degree) for h in range(2)]
                    if any(v.degree>192*(degree+2) for v in force):
                        raise ValueError("a complete new forcing coefficient exceeds its exact support")
                    return dict(degree=degree,numerator_b=nb[0].record(),numerator_a=nb[1].record(),
                        Fb=force[0].record(),Fa=force[1].record(),
                        full_radial_and_angular_terms_and_cross_couplings_retained=True)
                row=stage(name,build_forcing)
            if row["degree"]!=degree:raise ValueError("a forcing degree changed its exact original place")
            nums[0].append(L.LP.restore(row["numerator_b"]));nums[1].append(L.LP.restore(row["numerator_a"]))
            F[0].append(L.LP.restore(row["Fb"]));F[1].append(L.LP.restore(row["Fa"]))

        tr=series(original_stage("complete-normalized-transport-coefficients"))
        expected_tr={"inv00","inv01","inv10","J","Xm","T_excess","Jm","TTphi","TTrho","TXrho","Xrho"}
        gate("all old normalized transport outputs and exact low-order structural zeros are reused",
            set(tr)==expected_tr and all(len(v)==7 for v in tr.values())
            and tr["Xm"][0].is_zero() and tr["Jm"][0].is_zero()
            and tr["T_excess"][0].is_zero() and tr["T_excess"][1].is_zero())
        def determinant_helper():
            result=L.sub(L.mul(a0,a0,ORDER+1),L.mul(T,L.mul(b0,b0,ORDER+1),ORDER+1),ORDER+1)
            # This determinant was never a saved old output. Its exact constant
            # belongs to this new helper; none of the old transport views is rebuilt.
            result[0]=L.known_scalar_view(result[0],1,"same exact leading determinant at the true root")
            return result
        determinant=helper("new-unsaved-leading-determinant-through-twelve",determinant_helper)
        di=helper("new-unsaved-leading-determinant-inverse-through-twelve",lambda:L.inverse(determinant,ORDER+1))
        bdi=helper("complete-b0-determinant-inverse-through-twelve",lambda:L.mul(b0,di,ORDER+1))
        Trho=helper("complete-T-rho-through-thirteen",lambda:L.dr(T))
        Xrho=helper("complete-chi-rho-through-thirteen",lambda:L.dr(chi))
        for degree in range(7,ORDER+1):
            def build_transport_coefficients(degree=degree):
                jj=cprod(Trho,Xp,degree)-cprod(Tphi,Xrho,degree)
                values=dict(inv00=cprod(a0,di,degree),inv01=-cprod(T,bdi,degree),
                    inv10=-bdi[degree],J=jj,Xm=Xp[degree],T_excess=cprod(T,Xp,degree),
                    Jm=jj,TTphi=cprod(T,Tphi,degree),TTrho=cprod(T,Trho,degree),
                    TXrho=cprod(T,Xrho,degree),Xrho=Xrho[degree])
                return dict(degree=degree,coefficients={key:v.record() for key,v in values.items()})
            row=stage("normalized-transport-coefficients-degree-"+str(degree).zfill(3),build_transport_coefficients)
            if row["degree"]!=degree or set(row["coefficients"])!=expected_tr:
                raise ValueError("a new normalized transport coefficient changed identity")
            for key,value in row["coefficients"].items():tr[key].append(L.LP.restore(value))
        fb=[];fa=[]
        for degree in range(ORDER+1):
            name="normalized-forcing-degree-"+str(degree).zfill(3)
            if degree<=6:row=original_stage(name)
            else:
                def build_normalized(degree=degree):
                    vb=cprod(tr["inv00"],F[0],degree)+cprod(tr["inv01"],F[1],degree)
                    va=cprod(tr["inv10"],F[0],degree)+cprod(tr["inv00"],F[1],degree)
                    return dict(degree=degree,fb=vb.record(),fa=va.record())
                row=stage(name,build_normalized)
            if row["degree"]!=degree:raise ValueError("a normalized forcing degree changed")
            fb.append(L.LP.restore(row["fb"]));fa.append(L.LP.restore(row["fa"]))
        An=[];Bn=[]
        for degree in range(ORDER+1):
            def build_transport(degree=degree):
                if degree==0:an=L.LP.zero();bn=fb[0]
                else:
                    n=degree-1
                    rhs=cprod(tr["J"],fa,n)
                    rhs+=cprod(tr["Xrho"],L.theta(An),n).scale(2)
                    rhs-=cprod(tr["Xm"],L.dr(An),n).scale(2)
                    rhs+=cprod(tr["TTphi"],L.dr(Bn),n).scale(2*I)
                    rhs-=cprod(tr["TTrho"],L.theta(Bn),n).scale(2*I)
                    an=rhs.divide_scalar(2*degree)
                    knownA=An+[an]
                    rhs=cprod(tr["J"],fb,degree)
                    rhs+=cprod(tr["TXrho"],L.theta(Bn),degree).scale(2)
                    rhs-=cprod(tr["T_excess"],L.dr(Bn),degree).scale(2)
                    rhs-=cprod(tr["Jm"],Bn,degree)
                    rhs+=cprod(tr["TTphi"],L.dr(knownA),degree).scale(2*I)
                    rhs-=cprod(tr["TTrho"],L.theta(knownA),degree).scale(2*I)
                    bn=rhs.divide_scalar(T[1].scalar_value()*(2*degree+1))
                return dict(degree=degree,A=an.record(),B=bn.record(),
                    actual_same_canonical_Fuchsian_solution=True,unpaid_current_coefficients_discarded=False)
            name="transport-degree-"+str(degree).zfill(3)
            row=original_stage(name) if degree<=6 else stage(name,build_transport)
            if row["degree"]!=degree:raise ValueError("a transport degree changed")
            An.append(L.LP.restore(row["A"]));Bn.append(L.LP.restore(row["B"]))
        a1=[];b1=[]
        for degree in range(ORDER+1):
            def build_reconstructed(degree=degree):
                av=cprod(a0,An,degree)+cprod(Tb0,Bn,degree)
                bv=cprod(b0,An,degree)+cprod(a0,Bn,degree)
                if av.degree>192*(degree+1) or bv.degree>192*(degree+2):
                    raise ValueError("a complete first-correction coefficient exceeds its proved support")
                return dict(degree=degree,a1=av.record(),b1=bv.record(),
                    a1_exact_support_upper=192*(degree+1),b1_exact_support_upper=192*(degree+2),
                    no_incomplete_high_Fourier_output_removed=True)
            name="first-correction-degree-"+str(degree).zfill(3)
            row=original_stage(name) if degree<=6 else stage(name,build_reconstructed)
            if row["degree"]!=degree:raise ValueError("a first-correction degree changed")
            a1.append(L.LP.restore(row["a1"]));b1.append(L.LP.restore(row["b1"]))
        gate("all thirteen complete correction coefficients retain their full Fourier supports and both exact branches",
            len(a1)==len(b1)==ORDER+1 and a1[0].is_zero()
            and all(a1[p].degree<=192*(p+1) and b1[p].degree<=192*(p+2) for p in range(ORDER+1)))
        doc["complete_branch_identity"]=dict(same_complex_delta_without_conjugation=True,
            leading_a0_minus="a0_plus",leading_b0_minus="-b0_plus",
            Fb_minus="Fb_plus",Fa_minus="-Fa_plus",
            normalized_A_minus="-A_plus",normalized_B_minus="B_plus",
            first_correction_a1_minus="-a1_plus",first_correction_b1_minus="b1_plus",
            both_original_Airy_carrier_branches_retained=True)
        checkpoint()

        def tail_factor(x,radial_order):
            den=1-x
            if not den>0:raise ValueError("the actual Taylor inner radius reaches its Cauchy circle")
            if radial_order==0:return ipow(x,ORDER+1)/den
            if radial_order==1:return (ORDER+1)*ipow(x,ORDER)/den+ipow(x,ORDER+1)/sqr(den)
            if radial_order==2:return (ORDER*(ORDER+1)*ipow(x,ORDER-1)/den
                +2*(ORDER+1)*ipow(x,ORDER)/sqr(den)+2*ipow(x,ORDER+1)/(den*den*den))
            raise ValueError("unpaid radial derivative order")
        summaries=[]
        for width in WIDTHS:
            norm_rows=[]
            for degree in range(ORDER+1):
                def build_norm(degree=degree,width=width):
                    return dict(degree=degree,exact_width=str(width),
                        a1=[record(a1[degree].norm(width,q)) for q in range(4)],
                        b1=[record(b1[degree].norm(width,q)) for q in range(4)],
                        a1_actual_Fourier_range=[a1[degree].lo,a1[degree].hi],
                        b1_actual_Fourier_range=[b1[degree].lo,b1[degree].hi],
                        complete_mean_retained_in_angular_order_zero=True)
                tag=str(width.numerator)+"_"+str(width.denominator)
                name="full-Fourier-norm-"+tag+"-degree-"+str(degree).zfill(3)
                row=original_stage(name) if degree<=6 else stage(name,build_norm,kind="new_Fourier_norm")
                if row["degree"]!=degree or Q(row["exact_width"])!=width:
                    raise ValueError("a completed Fourier norm changed width or degree")
                norm_rows.append(row)
            def build_budget(width=width,norm_rows=norm_rows):
                delta=ex(SIGMA-width);z=(-4*delta).exp();one=1-z
                if not (delta>0 and one>0):raise ValueError("the angular tail loses its positive width")
                sums=[(1+z)/one,8*z/sqr(one),32*z*(1+z)/(one*one*one),
                      128*z*(1+4*z+z*z)/ipow(one,4)]
                x=ex(hcover)/ex(RHO)
                tables={}
                for name in ("a1","b1"):
                    values=[[rb(row[name][q]).upper() for q in range(4)] for row in norm_rows]
                    M=up(original_amp[name]);sup={};wiener={};parts={}
                    for p in range(3):
                        for q in range(4):
                            finite=sum((math.factorial(k)//math.factorial(k-p)
                                *values[k][q]*ipow(ex(hcover),k-p) for k in range(p,ORDER+1)),arb(0)).upper()
                            common=M*tail_factor(x,p)/ipow(ex(RHO),p)
                            st=(common*math.factorial(q)/ipow(delta,q)).upper()
                            wt=(common*sums[q]).upper()
                            key=str(p)+","+str(q)
                            sup[key]=(finite+st).upper();wiener[key]=(finite+wt).upper()
                            parts[key]=dict(complete_finite_Fourier_prefix=finite,
                                complete_strip_sup_tail=st,complete_Wiener_tail=wt)
                    tables[name]=dict(strip_sup=sup,Wiener=wiener,parts=parts)
                def local(v):
                    d,dr=coeff_bounds["D"],coeff_bounds["Dr"]
                    return dict(radial_second=v["2,0"],
                        radial_angular=2*d[0]*v["1,1"],
                        angular_second=(d[0]*d[0]+sqr(coeff_bounds["ep"])*coeff_bounds["K"])*v["0,2"],
                        drift_derivative=(dr[0]+d[0]*d[1])*v["0,1"],
                        first_transport=coeff_bounds["T0"]*(v["1,0"]+d[0]*v["0,1"]),
                        scalar_potential=coeff_bounds["V0"]*v["0,0"])
                va,vb=tables["a1"]["strip_sup"],tables["b1"]["strip_sup"]
                pa,pb=local(va),local(vb)
                pa["exact_QK_cross"]=coeff_bounds["vartheta"]*f_bounds["Q"]*f_bounds["TM"]*vb["0,0"]
                pb["exact_QK_cross"]=coeff_bounds["vartheta"]*f_bounds["Q"]*va["0,0"]
                if not f_bounds["mu"]>0:raise ValueError("the paid complete principal factor loses its gap")
                raw=[sum(v.values(),arb(0)).upper() for v in (pa,pb)]
                normalized=[(v/f_bounds["mu"]).upper() for v in raw]
                return dict(first_correction_Taylor_order=ORDER,original_N6_budget_unchanged=True,
                    exact_output_phi_width=str(width),
                    exact_old_rho_Cauchy_radius=str(RHO),exact_old_phi_Cauchy_width=str(SIGMA),
                    exact_physical_rho_cover_radius=str(hcover),
                    complete_geometric_Fourier_sums=encode(sums),first_amplitude_budgets=encode(tables),
                    unnormalized_local_operator_sup_bounds=encode(dict(first=raw[0],second=raw[1])),
                    complete_normalized_local_L0_w1_sup_bounds=encode(dict(first=normalized[0],second=normalized[1])),
                    unnormalized_local_operator_sup_parts=encode([pa,pb]),
                    complete_normalized_local_L0_w1_sup_parts=encode([
                        {k:(v/f_bounds["mu"]).upper() for k,v in row.items()} for row in (pa,pb)]),
                    local_operator_output_space="strip supremum on the declared old physical angle strip",
                    amplitude_Wiener_and_sup_spaces_separately_labelled=True,
                    old_circle_I_J_and_independent_mean_budget_paid=False,
                    canonical_to_old_second_derivative_Cauchy_chain_used=False)
            tag=str(width.numerator)+"_"+str(width.denominator)
            result=stage("complete-old-derivative-budget-N12-"+tag,build_budget,kind="new_N12_budget")
            summaries.append(result)
        doc["first_correction_derivative_budgets"]=summaries
        doc["complete_Fourier_coefficient_support"]=[
            dict(degree=p,a1_range=[a1[p].lo,a1[p].hi],b1_range=[b1[p].lo,b1[p].hi],
                a1_proved_bound=192*(p+1),b1_proved_bound=192*(p+2)) for p in range(ORDER+1)]
        gate("all complete old-radial derivative budgets retain positive angular and radial Cauchy losses",
            len(summaries)==len(WIDTHS)
            and all(Q(v["exact_output_phi_width"])<SIGMA for v in summaries))

        gate("the entire accepted original inventory and old three budgets remain byte-identical",
            len(doc["original_stages"])==75 and doc["original_stages"]==old["stages"]
            and all(sha(args.out.parent/r["file"])==r["sha256"]
                and (args.out.parent/r["file"]).stat().st_size==r["bytes"] for r in doc["original_stages"].values())
            and doc["original_first_correction_derivative_budgets"]==old["first_correction_derivative_budgets"])
        expected_new_norms={"full-Fourier-norm-"+str(width.numerator)+"_"+str(width.denominator)+
            "-degree-"+str(degree).zfill(3) for width in WIDTHS for degree in range(7,ORDER+1)}
        gate("exactly eighteen new complete Fourier norm rows and three N12 budgets are present",
            expected_new_norms=={name for name,r in doc["stages"].items() if r["stage_kind"]=="new_Fourier_norm"}
            and len(expected_new_norms)==18
            and sum(r["stage_kind"]=="new_N12_budget" for r in doc["stages"].values())==3)
        gate("all original no-recomputation requirements and unproved operator scopes are retained",
            doc["original_target_FFT_intrinsic_cubic_ray_or_auxiliary_stages_recomputed"]==0
            and doc["original_completed_finite_output_stages_recomputed"]==0
            and doc["new_cubic_component_rows"]==0 and doc["original_stages_copied"]==75
            and not doc["old_circle_I_J_or_independent_even_mean_budget_paid"]
            and not doc["complete_strong_return_or_cutoff97_inverse_claimed"]
            and all(r["bytes"]<=5_000_000 for r in doc["stages"].values()))
        doc["accepted_original_natural_stage_count"]=len(doc["original_stages"])
        doc["accepted_new_natural_stage_count"]=len(doc["stages"])
        doc["all_original_and_new_complete_Fourier_arrays_retained"]=True
        doc["all_original_and_new_natural_prefix_files_verified"]=True
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            original_completed_natural_stages_preserved=len(doc["original_stages"]),
            new_finite_algebra_stages=doc["new_finite_algebra_stages"],
            reused_finite_algebra_stages=doc["reused_finite_algebra_stages"],
            new_Fourier_norm_rows=doc["new_Fourier_norm_rows"],new_N12_budgets=doc["new_N12_budgets"],
            native_sha256=sha(args.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()
