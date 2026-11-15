#!/usr/bin/env python3
"""Correlate the complete local first Airy numerator before taking norms.

Read accepted Taylor coefficients only. New signed full Laurent convolutions
produce Nraw[0..10]; positive whole-product tails include every higher degree.
The separate old-circle nonlocal/mean and physical seam sources are not removed.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,shutil,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import acb,arb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as L

PUBLIC="Rogerhu12/math-research-public"
EXTENSION_NATIVE="758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f"
EXTENSION_PROCESS="42ab23b97ce922b042b8291af46cfe8c44ffd7e90ba1e2a6049caef263b7224e"
EXTENSION_SOURCE="42048094f7c5e0ba3b83f10e9e6fcbc5cd4c5b3d67057f69241409a5a4be87a1"
EXTENSION_MANIFEST="5700ded5038d500d14f43dfa69994665d2688f220de155128fff1fec6286e3a5"
OLD_SOURCE="e4ccbf4b343623d74d089f79b6605a0601975c6ea5c1d2e113bad568fe60167d"
OLD_MANIFEST="226e5acac42026431acbd166f92d423b6292ba6f73e65f58f808647d4701f1ad"
FOLD="84e2bd1b7637299e94428b22cc19aba290d0b661f9dbe18dae918bf752f10077"
FPROC="855730f8bf86d04c6cc7622e1881f9fc29a2af754694dfaf5dad16012b98544e"
ALGEBRA="9eb4b99b9a6b569233a3b7c3da80da7d2738c4f0bd18040654ff5b7beace2d4b"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
ORDER=10
COUNT=ORDER+1
RHO=Q(1,6000)
SIGMA=Q(1,128)
HREAL=Q(9,10**6)
DELTA=Q(1,10**8)
WIDTHS=(Q(0),Q(1,1024),Q(1,512))
I=acb(0,1)

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,separators=(",",":"),allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,mtime=0)
    temp=path.with_name(path.name+".partial");temp.write_bytes(raw);temp.replace(path)
def ex(q):return L.ex(q)
def up(v):return abs(v).upper()
def rb(v):
    if isinstance(v,str):return arb(v)
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def record(v):return dict(ball=L.rec(v,90))
def encode(v):
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x) for x in v]
    return record(v)
def decode(v):
    if isinstance(v,dict):
        if "ball" in v:return rb(v)
        return {k:decode(x) for k,x in v.items()}
    if isinstance(v,list):return [decode(x) for x in v]
    return v
def ipow(v,n):
    if n<0:raise ValueError("a nonnegative integer power was required")
    out=arb(1)
    for _ in range(n):out*=v
    return out
def cprod(a,b,n):return L.conv_coefficient(a,b,n)
def payload_sha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def required_input_stage_names():
    return (["complete-background-root-series","complete-local-operator-series","leading-complete-T",
             "helper-complete-T0-d-through-twelve","helper-complete-vartheta-Q-through-twelve"]
        +["first-correction-degree-"+str(j).zfill(3) for j in range(13)]
        +["background-drift-degree-"+str(j).zfill(3) for j in (9,10)]
        +["complete-local-operator-degree-"+str(j).zfill(3) for j in range(7,11)]
        +["leading-T-degree-"+str(j).zfill(3) for j in (9,10)])

def fourier_sums(delta):
    if not delta>0:raise ValueError("the complete angular tail has no positive width")
    z=(-4*delta).exp();d=1-z
    if not d>0:raise ValueError("the complete Fourier geometric denominator vanished")
    return [(1+z)/d,8*z/ipow(d,2),32*z*(1+z)/ipow(d,3),
        128*z*(1+4*z+z*z)/ipow(d,4),
        512*z*(1+11*z+11*z*z+z*z*z)/ipow(d,5)]

def complete_angular_factors(delta):
    """Three angular orders; bare radial and each complete product stay distinct."""
    S=fourier_sums(delta);half=fourier_sums(delta/2)
    bare_sup=[ex(math.factorial(k))/ipow(delta,k) for k in range(3)]
    G={};W={};alternatives={}
    for q in range(3):
        for k in range(3):
            key=str(q)+","+str(k)
            if q==0:
                G[key]=bare_sup[k];W[key]=S[k]
                alternatives[key]=dict(product_holomorphic_on_original_complete_strip=S[k])
            else:
                G[key]=ex(Q(math.factorial(q+k+1),q+1))/ipow(delta,q+k)
                direct=sum((math.comb(k,l)*S[l]*S[q+k-l] for l in range(k+1)),arb(0))
                intermediate=math.factorial(q)*ipow(2/delta,q)*half[k]
                W[key]=min(up(direct),up(intermediate)).upper()
                alternatives[key]=dict(complete_two_sided_convolution=direct,
                    intermediate_strip_and_complete_Fourier_sum=intermediate)
    return dict(delta=delta,bare_sup=bare_sup,bare_Wiener=S[:3],
        G=G,W=W,complete_fourier_sums=S,half_width_fourier_sums=half,
        independent_Wiener_candidates=alternatives)

def complete_remainder(k,norm,radial,multipliers,amplitudes,angular):
    if norm not in ("strip_sup","Wiener"):raise ValueError("unknown complete source norm")
    bare=angular["bare_sup"][k] if norm=="strip_sup" else angular["bare_Wiener"][k]
    g=angular["G"] if norm=="strip_sup" else angular["W"]
    U,V0,V1=radial["U"],radial["V0"],radial["V1"]
    R=ex(RHO)
    terms=dict(bare_radial_second=U*bare/(R*R),
        radial_angular=multipliers["C11"]*V1*g["1,"+str(k)]/R,
        full_first_angular=multipliers["C01"]*V0*g["1,"+str(k)],
        angular_second=multipliers["C02"]*V0*g["2,"+str(k)],
        first_radial=multipliers["C10"]*V1*g["0,"+str(k)]/R,
        scalar_potential=multipliers["C00"]*V0*g["0,"+str(k)])
    core=sum(terms.values(),arb(0))
    result={}
    for name,other,cross in (("a","b","Cab"),("b","a","Cba")):
        own=amplitudes[name]*core
        off=amplitudes[other]*multipliers[cross]*V0*g["0,"+str(k)]
        result[name]=dict(complete_same_amplitude_tail=own,
            complete_cross_amplitude_tail=off,complete_tail=(own+off).upper(),
            complete_same_amplitude_tail_terms={key:amplitudes[name]*v for key,v in terms.items()})
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo-root","manifest","out"):parser.add_argument("--"+key,type=Path,required=True)
    parser.add_argument("--resume",type=Path)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new complete finite and tail mathematics runs only in public Actions")
    import scipy
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
                 numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise ValueError("the exact complete interval environment changed")
    if args.out.exists():raise FileExistsError("preserve every original result and accepted new prefix")
    if sha(L.__file__)!=ALGEBRA:raise ValueError("the original complete non-circular algebra changed")
    ctx.prec=320;start=time.monotonic()
    doc=dict(kind="complete_correlated_first_Airy_local_numerator_and_Taylor_tail",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),
        algebra_sha256=ALGEBRA,runtime=runtime,complete=False,proved=False,failure=None,gates=[],stages={},
        original_extension_native_sha256=EXTENSION_NATIVE,
        original_extension_process_sha256=EXTENSION_PROCESS,
        original_extension_source_sha256=EXTENSION_SOURCE,
        original_extension_manifest_sha256=EXTENSION_MANIFEST,
        original_larger_fold_native_sha256=FOLD,original_larger_fold_process_sha256=FPROC,
        background_definition_sha256=BASE,explicit_direction_definition_sha256=ZDEF,
        fixed_intrinsic_parameter="eta_0",exact_complex_delta_radius=str(DELTA),
        residual_Taylor_order=ORDER,completed_first_correction_Taylor_order=12,
        maximum_output_angular_derivative=2,physical_angle_frequency_multiplier=4,
        original_target_FFT_intrinsic_cubic_ray_fold_Taylor_and_finite_outputs_recomputed=0,
        original_complete_T0_d_and_vartheta_Q_helpers_recomputed=0,
        new_finite_numerator_degrees=0,reused_finite_numerator_degrees=0,
        new_supporting_helper_stages=0,reused_supporting_helper_stages=0,
        new_complete_norm_rows=0,reused_complete_norm_rows=0,
        new_complete_scalar_tail_stages=0,reused_complete_scalar_tail_stages=0,
        new_complete_budget_stages=0,reused_complete_budget_stages=0,
        complete_mean_retained_before_any_projection=True,
        exact_old_D_order_retained=True,principal_mu_uses_B_plus=True,
        all_original_physical_seams_and_independent_mean_equations_retained=True,
        no_principal_factor_division_in_actual_local_numerator=True,
        reconstructed_JP_Airy_operator_and_radial_integral_paid=False,
        old_circle_nonlocal_and_independent_even_mean_terms_paid=False,
        complete_strong_return_or_cutoff97_inverse_claimed=False)
    def gate(name,test):
        passed=bool(test);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("correlated local numerator gate failed: "+name)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(args.out,doc)
    def stage(name,kind,build):
        if name in doc["stages"]:
            entry=doc["stages"][name];path=args.out.parent/entry["file"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("an accepted new natural numerator stage changed bytes")
            v=read(path)
            if not (v["stage"]==name and v["complete"] and v["stage_kind"]==kind
                and v["source_sha256"]==doc["source_sha256"]
                and v["input_manifest_sha256"]==doc["input_manifest_sha256"]
                and v["algebra_sha256"]==ALGEBRA and v["runtime"]==runtime
                and v["original_extension_native_sha256"]==EXTENSION_NATIVE
                and v["original_larger_fold_native_sha256"]==FOLD):
                raise ValueError("a resumed new numerator stage changed exact scientific identity")
            doc["reused_"+kind]+=1
            return v["payload"]
        payload=build()
        path=args.out.parent/"stages"/(name+".json.gz")
        if path.exists():raise FileExistsError("an unindexed natural numerator stage must be preserved")
        value=dict(stage=name,stage_kind=kind,complete=True,source_sha256=doc["source_sha256"],
            input_manifest_sha256=doc["input_manifest_sha256"],algebra_sha256=ALGEBRA,runtime=runtime,
            original_extension_native_sha256=EXTENSION_NATIVE,original_larger_fold_native_sha256=FOLD,
            payload=payload)
        save(path,value)
        doc["stages"][name]=dict(file=str(path.relative_to(args.out.parent)),
            bytes=path.stat().st_size,sha256=sha(path),stage_kind=kind)
        doc["new_"+kind]+=1;checkpoint()
        return payload
    def helper(name,build):
        result=stage("helper-"+name,"supporting_helper_stages",
            lambda:dict(name=name,coefficients=L.pack_series(build())))
        if result["name"]!=name:raise ValueError("a complete new helper changed its name")
        return L.unpack_series(result["coefficients"])
    try:
        m=read(args.manifest)
        gate("the public manifest requests only correlated degree-ten local residual outputs",
            m["public_repository"]==PUBLIC
            and m["mathematical_parameters"]["residual_Taylor_order"]==ORDER
            and m["mathematical_parameters"]["completed_first_correction_Taylor_order"]==12
            and m["mathematical_parameters"]["maximum_output_angular_derivative"]==2)
        pins={}
        for entry in m["files"]:
            path=args.repo_root/entry["path"]
            if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                raise ValueError("an exact pinned complete input changed: "+entry["path"])
            pins[str(path.resolve())]=entry
        paths={k:args.repo_root/v for k,v in m["input_paths"].items()}
        ext,ep,fold,fp=[read(paths[k]) for k in ("extension_native","extension_process","fold_native","fold_process")]
        gate("both original Taylor12 and larger fold computations are actual complete successes",
            sha(paths["extension_native"])==ep["native_sha256"]==EXTENSION_NATIVE
            and sha(paths["extension_process"])==EXTENSION_PROCESS
            and sha(paths["fold_native"])==fp["native_sha256"]==FOLD
            and sha(paths["fold_process"])==FPROC
            and ext["source_sha256"]==ep["mathematical_source_sha256"]==EXTENSION_SOURCE
            and ext["input_manifest_sha256"]==EXTENSION_MANIFEST
            and all(d["complete"] and d["proved"] and d["failure"] is None
                and d["gates"] and all(g["passed"] for g in d["gates"]) for d in (ext,fold))
            and len(ext["gates"])==19 and ep["mathematical_gates"]==ext["gates"]
            and all(p["complete"] and p["actual_returncode"]==0 and p["mathematical_complete"]
                and p["mathematical_failure"] is None for p in (ep,fp))
            and ep["original75_stage_bytes_unchanged"]
            and ep["all_available_natural_stage_files_verified"]
            and len(ext["original_stages"])==75 and len(ext["stages"])==205)
        gate("the exact repaired family complex delta old variables and original physical root piece are unchanged",
            ext["background_definition_sha256"]==BASE
            and ext["explicit_direction_definition_sha256"]==ZDEF
            and ext["actual_intrinsic_parameter"]=="eta_0"
            and Q(ext["exact_fixed_intrinsic_parameter"])==Q(-7789843107295549,4611686018427387904)
            and Q(ext["exact_complex_delta_radius"])==DELTA
            and ext["exact_root_interval"]==fold["exact_root_interval"]
            and ext["principal_mu_uses_B_plus_and_leading_a0_uses_B_minus"])
        olddomain=ext["old_product_domain"];roots=list(map(Q,ext["exact_root_interval"]))
        hcover=HREAL+roots[1]-roots[0]
        gate("the entire inherited old-product and physical inner domains have strictly positive losses",
            Q(olddomain["exact_rho_radius"])==RHO and Q(olddomain["exact_phi_width"])==SIGMA
            and Q(olddomain["exact_physical_inner_radius"])==HREAL
            and Q(olddomain["exact_physical_rho_cover_radius"])==hcover
            and hcover<RHO and all(w<SIGMA for w in WIDTHS)
            and olddomain["exact_physical_interval"]==[str(roots[0]-HREAL),str(roots[1]+HREAL)]
            and Q(ext["exact_original_physical_piece_interval"][0])<roots[0]-HREAL
            and roots[1]+HREAL<Q(ext["exact_original_physical_piece_interval"][1]))
        acase=fold["cases"][1]
        gate("every multiplier bound is from the same complete holomorphic auxiliary case",
            acase["complete"] and acase["proved"] and acase["failure"] is None
            and all(g["passed"] for g in acase["gates"])
            and Q(acase["exact_input_auxiliary_radius"])==Q(1,2000)
            and Q(acase["exact_fold_radius"])==Q(3,8000)>RHO
            and Q(acase["exact_coefficient_width"])==Q(1,32)>SIGMA
            and Q(acase["exact_old_leading_width"])==Q(3,128)>SIGMA)
        cbounds=decode(acase["characteristic_refinement_evidence"]["complete_refined_coefficient_majorants"])
        fbounds=decode(acase["fold_evidence"]["complete_fold_and_leading_bounds"])
        amps0=decode(acase["first_forcing_evidence"]["separated_first_amplitudes"])
        amplitudes=dict(a=up(amps0["a1"]),b=up(amps0["b1"]))
        doc.update(exact_root_interval=copy.deepcopy(ext["exact_root_interval"]),
            exact_original_physical_piece_interval=copy.deepcopy(ext["exact_original_physical_piece_interval"]),
            exact_fixed_intrinsic_parameter=ext["exact_fixed_intrinsic_parameter"],
            old_product_domain=copy.deepcopy(olddomain),
            original_complete_branch_identity=copy.deepcopy(ext["complete_branch_identity"]),
            original_derivative_triangle_budgets=copy.deepcopy(ext["first_correction_derivative_budgets"]),
            contract_sha256=sha(paths["contract"]),
            original_auxiliary_case_payload_sha256=payload_sha(acase),
            original_complete_amplitude_bounds=encode(amplitudes),
            original_selected_natural_stage_receipts={})
        cache={}
        for name in required_input_stage_names():
            old=name in ext["original_stages"]
            entry=(ext["original_stages"] if old else ext["stages"]).get(name)
            if entry is None:raise ValueError("an already completed necessary stage is absent: "+name)
            relative=Path(entry["file"])
            if relative.is_absolute() or ".." in relative.parts or relative.parts[0]!="stages":
                raise ValueError("an original natural stage left its completed directory")
            path=paths["extension_native"].parent/relative
            pin=pins.get(str(path.resolve()))
            if (pin is None or pin["sha256"]!=entry["sha256"] or pin["bytes"]!=entry["bytes"]
                or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]):
                raise ValueError("an exact accepted stage is not independently pinned: "+name)
            value=read(path)
            source=OLD_SOURCE if old else EXTENSION_SOURCE
            manifest=OLD_MANIFEST if old else EXTENSION_MANIFEST
            if not (value["stage"]==name and value["complete"]
                and value["source_sha256"]==source and value["input_manifest_sha256"]==manifest
                and value["algebra_sha256"]==ALGEBRA and value["runtime"]==runtime):
                raise ValueError("an original stage changed its original old-or-new identity: "+name)
            cache[name]=value["payload"]
            doc["original_selected_natural_stage_receipts"][name]=dict(**entry,
                original_source_sha256=source,original_input_manifest_sha256=manifest,
                original_inventory="original75" if old else "extension205",
                original_payload_sha256=payload_sha(value["payload"]))
        gate("all26 complete selected stages are read verbatim from their separate original inventories",
            len(cache)==len(set(required_input_stage_names()))==26)
        if args.resume:
            previous=read(args.resume)
            identity=("public_repository","source_sha256","input_manifest_sha256","algebra_sha256","runtime",
                "original_extension_native_sha256","original_extension_process_sha256",
                "original_extension_source_sha256","original_extension_manifest_sha256",
                "original_larger_fold_native_sha256","original_larger_fold_process_sha256",
                "contract_sha256","old_product_domain","original_selected_natural_stage_receipts")
            gate("the accepted new numerator prefix has the identical source runtime contract and complete inputs",
                all(previous.get(k)==doc.get(k) for k in identity))
            for name,entry in previous.get("stages",{}).items():
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0]!="stages":
                    raise ValueError("a new numerator prefix left its own natural stage directory")
                source=args.resume.parent/relative;target=args.out.parent/relative
                if not source.is_file() or sha(source)!=entry["sha256"] or source.stat().st_size!=entry["bytes"]:
                    raise ValueError("a preserved complete new numerator prefix changed")
                target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
                doc["stages"][name]=copy.deepcopy(entry)
            doc["preserved_actual_prefix"]=dict(native_sha256=sha(args.resume),
                native_bytes=args.resume.stat().st_size,complete=previous["complete"],
                proved=previous["proved"],failure=previous["failure"],gates=previous["gates"])
        checkpoint()
        background=cache["complete-background-root-series"]
        if not (background["zero_bump_germ_and_fixed_eta0"]
                and background["complete_mean_at_all_orders_retained"]):
            raise ValueError("the original background identity lost its independent mean")
        d=L.unpack_series(background["series"]["d"])
        if len(d)!=9:raise ValueError("the original full drift prefix changed length")
        for j in (9,10):
            v=cache["background-drift-degree-"+str(j).zfill(3)]
            if v["degree"]!=j:raise ValueError("a completed drift degree changed order")
            d.append(L.LP.restore(v["d"]))
        op={k:L.unpack_series(v) for k,v in cache["complete-local-operator-series"].items()}
        if any(len(v)!=7 for v in op.values()):raise ValueError("an original operator prefix changed")
        for j in range(7,11):
            row=cache["complete-local-operator-degree-"+str(j).zfill(3)]
            if row["degree"]!=j or set(row["coefficients"])!=set(op):
                raise ValueError("a completed operator degree changed order or names")
            for key,value in row["coefficients"].items():op[key].append(L.LP.restore(value))
        oldT=cache["leading-complete-T"]
        if oldT["name"]!="T":raise ValueError("the original complete fold T changed name")
        T=L.unpack_series(oldT["coefficients"])
        if len(T)!=9:raise ValueError("the original complete T prefix changed length")
        for j in (9,10):
            row=cache["leading-T-degree-"+str(j).zfill(3)]
            if row["name"]!="leading-T" or row["degree"]!=j:
                raise ValueError("a completed fold coefficient changed order")
            T.append(L.LP.restore(row["coefficient"]))
        T0d=L.unpack_series(cache["helper-complete-T0-d-through-twelve"]["coefficients"])
        vq=L.unpack_series(cache["helper-complete-vartheta-Q-through-twelve"]["coefficients"])
        if len(T0d)!=13 or len(vq)!=13:raise ValueError("an accepted complete helper changed its full prefix")
        w=[[],[]]
        for j in range(13):
            row=cache["first-correction-degree-"+str(j).zfill(3)]
            if row["degree"]!=j:raise ValueError("an original complete correction degree changed order")
            w[0].append(L.LP.restore(row["a1"]));w[1].append(L.LP.restore(row["b1"]))
        gate("only existing complete degrees are used for the signed degree-ten differential numerator",
            len(d)==len(T)==COUNT and all(len(v)==COUNT for v in op.values())
            and len(w[0])==len(w[1])==13 and w[0][0].is_zero() and T[0].is_zero())
        wr=[];wrr=[];wphi=[];wrphi=[];wphiphi=[]
        for name,values in zip(("a1","b1"),w):
            r1=helper("correlated-"+name+"-rho-through-eleven",lambda values=values:L.dr(values))
            r2=helper("correlated-"+name+"-rho-second-through-ten",lambda r1=r1:L.dr(r1))
            pp=helper("correlated-"+name+"-phi-through-twelve",lambda values=values:L.theta(values))
            rp=helper("correlated-"+name+"-rho-phi-through-eleven",lambda r1=r1:L.theta(r1))
            p2=helper("correlated-"+name+"-phi-second-through-twelve",lambda values=values:L.theta(values,2))
            wr.append(r1);wrr.append(r2);wphi.append(pp);wrphi.append(rp);wphiphi.append(p2)
        Tb=helper("correlated-T-b1-through-ten",lambda:L.mul(T,w[1],COUNT))
        numerators=[[],[]];supports=[]
        for degree in range(COUNT):
            def build(degree=degree):
                output=[]
                for component in range(2):
                    value=wrr[component][degree]
                    value+=cprod(d,wrphi[component],degree).scale(2)
                    value+=cprod(op["crossd"],wphi[component],degree)
                    value+=cprod(op["angular2"],wphiphi[component],degree)
                    value+=cprod(op["T0"],wr[component],degree)
                    value+=cprod(T0d,wphi[component],degree)
                    value+=cprod(op["V0"],w[component],degree)
                    value+=cprod(vq,Tb if component==0 else w[0],degree).scale(I)
                    output.append(value)
                return dict(degree=degree,Nraw_a=output[0].record(),Nraw_b=output[1].record(),
                    full_mean_a=L.cpack(output[0].mean()),full_mean_b=L.cpack(output[1].mean()),
                    complete_signed_operator_sum_before_norm=True,
                    exact_old_D="-d/drho-d*d/dphi",
                    original_complete_helpers_T0_d_and_vartheta_Q_reused=True)
            row=stage("correlated-local-numerator-degree-"+str(degree).zfill(3),"finite_numerator_degrees",build)
            if row["degree"]!=degree:raise ValueError("a complete new residual degree changed order")
            for component,key in enumerate(("Nraw_a","Nraw_b")):
                numerators[component].append(L.LP.restore(row[key]))
            supports.append(dict(degree=degree,a_range=[numerators[0][-1].lo,numerators[0][-1].hi],
                b_range=[numerators[1][-1].lo,numerators[1][-1].hi],
                full_mean_a=copy.deepcopy(row["full_mean_a"]),full_mean_b=copy.deepcopy(row["full_mean_b"])))
        gate("all eleven complete signed residual coefficients retain every Fourier mode and full mean",
            len(numerators[0])==len(numerators[1])==COUNT
            and all(v.c and all(z.is_finite() for z in v.c) for a in numerators for v in a))
        doc["complete_Fourier_coefficient_support_and_mean"]=supports
        def build_multipliers():
            D,Dr=cbounds["D"],cbounds["Dr"]
            values=dict(C11=2*D[0],
                C01=Dr[0]+D[0]*D[1]+cbounds["T0"]*D[0],
                C02=D[0]*D[0]+cbounds["ep"]*cbounds["ep"]*cbounds["K"],
                C10=cbounds["T0"],C00=cbounds["V0"],
                Cab=cbounds["vartheta"]*fbounds["Q"]*fbounds["TM"],
                Cba=cbounds["vartheta"]*fbounds["Q"])
            return dict(complete_multiplier_bounds=encode({k:up(v) for k,v in values.items()}),
                original_complete_coefficient_payload_sha256=payload_sha(
                    acase["characteristic_refinement_evidence"]["complete_refined_coefficient_majorants"]),
                original_complete_fold_payload_sha256=payload_sha(
                    acase["fold_evidence"]["complete_fold_and_leading_bounds"]),
                exact_coefficient_width=acase["exact_coefficient_width"],
                exact_fold_old_angle_width=acase["exact_old_leading_width"],
                exact_common_product_rho_radius=str(RHO),exact_common_product_phi_width=str(SIGMA),
                no_real_circle_bound_promoted_to_complex_strip=True)
        mult=stage("complete-local-numerator-whole-product-multipliers","complete_scalar_tail_stages",build_multipliers)
        multipliers=decode(mult["complete_multiplier_bounds"])
        def build_radial():
            t=ex(hcover)/ex(RHO);den=1-t;mstart=ORDER+1
            if not (t>0 and den>0):raise ValueError("the exact radial Taylor tail has no positive loss")
            U=((mstart+1)*(mstart+2)*ipow(t,mstart)/den
                +2*(mstart+2)*ipow(t,mstart+1)/ipow(den,2)
                +2*ipow(t,mstart+2)/ipow(den,3))
            V0=(mstart+1)*ipow(t,mstart)/den+ipow(t,mstart+1)/ipow(den,2)
            return dict(exact_rho_radius=str(RHO),exact_physical_rho_cover_radius=str(hcover),
                first_missing_residual_degree=ORDER+1,numeric=encode(dict(t=t,U=U,V0=V0,V1=U/2)),
                all_infinite_radial_coefficients_included=True,
                no_subtraction_of_a_large_complete_geometric_prefix=True)
        radial_stage=stage("complete-local-numerator-positive-radial-tails","complete_scalar_tail_stages",build_radial)
        radial=decode(radial_stage["numeric"])
        budgets=[]
        for wi,width in enumerate(WIDTHS):
            norm_rows=[]
            for degree in range(COUNT):
                def build_norm(degree=degree,width=width):
                    return dict(degree=degree,exact_output_phi_width=str(width),
                        Nraw_a=[record(numerators[0][degree].norm(width,k)) for k in range(3)],
                        Nraw_b=[record(numerators[1][degree].norm(width,k)) for k in range(3)],
                        complete_full_Fourier_outputs_and_mean_retained=True)
                name="full-Nraw-Fourier-norm-"+str(width.numerator)+"_"+str(width.denominator)+"-degree-"+str(degree).zfill(3)
                row=stage(name,"complete_norm_rows",build_norm)
                if row["degree"]!=degree or Q(row["exact_output_phi_width"])!=width:
                    raise ValueError("a complete new residual norm changed degree or width")
                norm_rows.append(row)
            def build_budget(width=width,wi=wi,norm_rows=norm_rows):
                delta=ex(SIGMA-width);angular=complete_angular_factors(delta)
                results={norm:{name:{} for name in ("a","b")} for norm in ("strip_sup","Wiener")}
                parts={norm:{name:{} for name in ("a","b")} for norm in ("strip_sup","Wiener")}
                for k in range(3):
                    finite={name:sum((up(rb(norm_rows[n]["Nraw_"+name][k]))*ipow(ex(hcover),n)
                        for n in range(COUNT)),arb(0)).upper() for name in ("a","b")}
                    for norm in ("strip_sup","Wiener"):
                        tails=complete_remainder(k,norm,radial,multipliers,amplitudes,angular)
                        for name in ("a","b"):
                            tail=up(tails[name]["complete_tail"])
                            value=(finite[name]+tail).upper()
                            if not (value.is_finite() and value>=0):
                                raise ValueError("a complete correlated residual bound is invalid")
                            results[norm][name][str(k)]=value
                            parts[norm][name][str(k)]=dict(
                                complete_correlated_finite_Fourier_prefix=finite[name],
                                complete_infinite_radial_and_angular_tail=tail,
                                complete_tail_terms=tails[name])
                oldbudget=ext["first_correction_derivative_budgets"][wi]
                if Q(oldbudget["exact_output_phi_width"])!=width:
                    raise ValueError("an original comparison norm changed its declared width")
                oldraw=decode(oldbudget["unnormalized_local_operator_sup_bounds"])
                selected=dict(first=min(results["strip_sup"]["a"]["0"],up(oldraw["first"])).upper(),
                    second=min(results["strip_sup"]["b"]["0"],up(oldraw["second"])).upper())
                return dict(exact_output_phi_width=str(width),
                    exact_rho_Cauchy_radius=str(RHO),exact_phi_Cauchy_width=str(SIGMA),
                    exact_physical_rho_cover_radius=str(hcover),residual_Taylor_order=ORDER,
                    complete_Nraw_derivative_budgets=encode(results),
                    complete_finite_and_tail_parts=encode(parts),
                    complete_angular_factors=encode(angular),
                    original_triangle_unnormalized_q0_bound=copy.deepcopy(
                        oldbudget["unnormalized_local_operator_sup_bounds"]),
                    independent_minimum_complete_q0_strip_bound=encode(selected),
                    new_correlated_q0_bound_no_larger_than_original=dict(
                        first=bool(results["strip_sup"]["a"]["0"]<=up(oldraw["first"])),
                        second=bool(results["strip_sup"]["b"]["0"]<=up(oldraw["second"]))),
                    no_improvement_assumed_by_a_mathematical_gate=True,
                    actual_local_source_requires_JP_S_of_this_unnormalized_numerator=True,
                    normalized_L0_w1_is_not_substituted=True,
                    reconstructed_Airy_operator_JP_and_radial_integral_paid=False,
                    independent_even_mean_and_all_old_circle_nonlocal_terms_remain_separate=True)
            tag=str(width.numerator)+"_"+str(width.denominator)
            budget=stage("complete-correlated-Nraw-budget-"+tag,"complete_budget_stages",build_budget)
            budgets.append(budget)
        doc["complete_correlated_Nraw_budgets"]=budgets
        doc["complete_branch_identity"]=dict(same_complex_delta_without_conjugation=True,
            Nraw_a_minus="-Nraw_a_plus",Nraw_b_minus="Nraw_b_plus",
            both_original_Airy_carrier_branches_retained=True)
        gate("three complete norm pairs include every higher radial degree and full two-sided Fourier tail",
            len(budgets)==3 and all(Q(v["exact_output_phi_width"])==WIDTHS[i]
                for i,v in enumerate(budgets))
            and doc["new_finite_numerator_degrees"]+doc["reused_finite_numerator_degrees"]==11
            and doc["new_complete_norm_rows"]+doc["reused_complete_norm_rows"]==33
            and doc["new_complete_scalar_tail_stages"]+doc["reused_complete_scalar_tail_stages"]==2)
        gate("all accepted inputs are unchanged and no separate source or inverse was silently paid",
            doc["original_target_FFT_intrinsic_cubic_ray_fold_Taylor_and_finite_outputs_recomputed"]==0
            and doc["original_complete_T0_d_and_vartheta_Q_helpers_recomputed"]==0
            and len(doc["original_selected_natural_stage_receipts"])==26
            and doc["complete_mean_retained_before_any_projection"]
            and not doc["reconstructed_JP_Airy_operator_and_radial_integral_paid"]
            and not doc["old_circle_nonlocal_and_independent_even_mean_terms_paid"]
            and not doc["complete_strong_return_or_cutoff97_inverse_claimed"])
        doc["accepted_new_natural_stage_count"]=len(doc["stages"])
        doc["all_original_selected_and_new_complete_Fourier_arrays_retained"]=True
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            new_finite_numerator_degrees=doc["new_finite_numerator_degrees"],
            new_complete_norm_rows=doc["new_complete_norm_rows"],accepted_new_stages=len(doc["stages"]),
            native_sha256=sha(args.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()
