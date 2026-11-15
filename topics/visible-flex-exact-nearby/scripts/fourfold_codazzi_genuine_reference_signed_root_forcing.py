#!/usr/bin/env python3
"""Signed genuine-reference first forcing at the same certified true root.

Only the three original complete root-series stages are consumed. New work
is the signed Laurent/rational assembly in F.20--F.22 and its complete
Fourier norms. No old target, FFT, cubic, intrinsic derivative, fold or
accepted Taylor coefficient is evaluated again. Full new coefficients remain
temporary under rule15; only small actual conclusions are published.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np,scipy
from flint import arb,acb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as L

PUBLIC="Rogerhu12/math-research-public"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
ALGEBRA="9eb4b99b9a6b569233a3b7c3da80da7d2738c4f0bd18040654ff5b7beace2d4b"
CONTRACT="052a0b23535c42523bc25734ed6366fd01a765c6a309b8ca88731b3ffdd707d8"
OLD_SOURCE="e4ccbf4b343623d74d089f79b6605a0601975c6ea5c1d2e113bad568fe60167d"
OLD_MANIFEST="226e5acac42026431acbd166f92d423b6292ba6f73e65f58f808647d4701f1ad"
TAYLOR="758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f"
TPROC="42ab23b97ce922b042b8291af46cfe8c44ffd7e90ba1e2a6049caef263b7224e"
TPUB="dc7d7f0fca329f4e16af276ea762ab9316285e803d0816b6b8ec01fe3896e7d3"
TSOURCE="42048094f7c5e0ba3b83f10e9e6fcbc5cd4c5b3d67057f69241409a5a4be87a1"
TMANIFEST="5700ded5038d500d14f43dfa69994665d2688f220de155128fff1fec6286e3a5"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
ROOTS=("1191984371497/5000000000000","2383968743003/10000000000000")
PIECE=("2147184947341121/9007199254740992","4295308144604611/18014398509481984")
DELTA=Q(1,10**8)
Z=Q(1,9409)
WIDTHS=(Q(0),Q(1,128),Q(3,128))
DERIVATIVES=(0,1,2,3)
STAGES={
 "background_stage":("complete-background-root-series",75245,
    "a6f89d9bf9523d04fd0534f7224b7a8bb3ecc8b0b201ffccf3839585df56b0c8"),
 "operator_stage":("complete-local-operator-series",198895,
    "2361459d324b9de0cfe2d53e06ad5f168d91110e72ac920c28fdc779e2fd87f2"),
 "leading_Q_stage":("leading-complete-Q",80521,
    "0aa0da3c5260ebab0f64afaf0df07eab854988a9a630260714a783ef1c21d523")}
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
def jhash(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def ex(value):return L.ex(Q(value))
def cv(value):return acb(ex(value)) if isinstance(value,(int,Q)) else acb(value)
def up(value):return abs(cv(value)).upper()
def rec(value):return dict(ball=L.rec(value,64))
def crec(value):
    value=cv(value)
    return dict(real=rec(value.real),imag=rec(value.imag))
def require(a,count):
    if len(a)<count:raise ValueError("an unpaid root derivative was requested")
def jconstant(value,count):return [cv(value)]+[acb(0) for _ in range(count-1)]
def jadd(a,b,count):
    require(a,count);require(b,count)
    return [a[k]+b[k] for k in range(count)]
def jscale(a,value,count=None):
    count=len(a) if count is None else count;require(a,count);value=cv(value)
    return [x*value for x in a[:count]]
def jmul(a,b,count):
    require(a,count);require(b,count)
    return [sum((a[k]*b[n-k] for k in range(n+1)),acb(0)) for n in range(count)]
def jdr(a):return [(k+1)*a[k+1] for k in range(len(a)-1)]
def jinv(a,count):
    require(a,count)
    if a[0].contains(0):raise ValueError("a complete scalar denominator contains zero")
    y=[1/a[0]]
    for n in range(1,count):
        y.append(-y[0]*sum((a[k]*y[n-k] for k in range(1,n+1)),acb(0)))
    return y
def jdiv(a,b,count):return jmul(a,jinv(b,count),count)
def scalar_r_jets(values,count):
    require(values,count)
    return [values[p].scalar_value()*((-1)**p) for p in range(count)]
def fourier_r_jets(values,mode,count):
    require(values,count)
    return [values[p].coefficient(mode)*((-1)**p) for p in range(count)]
def P(value):
    # The original exact old-circle projection; every other coefficient stays.
    return L.LP(value.lo,[acb(0) if j==0 else z for j,z in enumerate(value.c,value.lo)])
def is_odd(value):
    return value.mean().contains(0) and all(
        (value.coefficient(j)+value.coefficient(-j)).contains(0)
        for j in range(1,value.degree+1))
def complete_norm_rows(value):
    return [dict(exact_old_phi_width=str(width),
        derivative_orders=list(DERIVATIVES),
        complete_joint_Wiener_derivative_upper=[rec(value.norm(width,q)) for q in DERIVATIVES],
        normalized_angular_measure=True,physical_derivative_multiplier="4ij",
        no_finite_output_projection=True)
        for width in WIDTHS]

def rational_frequency_shift(c,qinf,kappa):
    """F.22 directly: never subtract independently enclosed full potentials."""
    count=3
    beta=scalar_r_jets(c["beta"],count)
    eta=scalar_r_jets(c["eta"],count)
    K=scalar_r_jets(c["K"],count)
    if K[0]!=0:raise ValueError("the accepted exact true-root K0 is not zero")
    z=acb(arb(0,ex(Z)),arb(0,ex(Z)))
    U=jconstant(0,count);W=jconstant(0,count);mix=jconstant(0,count)
    minimum=arb(1)
    for mode in range(1,97):
        den=1-mode*mode*z
        gap=den.real.lower()
        if not gap>0:raise ValueError("one complete primitive intermediate denominator lost its gap")
        minimum=min(minimum,gap)
        uj=fourier_r_jets(c["u"],mode,count)
        um=fourier_r_jets(c["u"],-mode,count)
        vj=fourier_r_jets(c["v"],mode,count)
        vm=fourier_r_jets(c["v"],-mode,count)
        U=jadd(U,jscale(jmul(uj,um,count),2*mode*mode/den),count)
        W=jadd(W,jscale(jmul(vj,vm,count),2*mode*mode/den),count)
        mix=jadd(mix,jscale(jmul(uj,vm,count),mode/den),count)
    alpha=jscale(jmul(beta,mix,count),-I)
    ratio=jdiv(alpha,eta,count)
    denominator=jadd(jconstant(1,count),jscale(ratio,z),count)
    gap=abs(denominator[0]).lower()
    if not gap>0:raise ValueError("the complete finite-frequency a/eta root denominator lost its gap")
    Q1=jadd(jscale(jmul(beta,U,2),-2),
        jscale(jmul(jmul(beta,K,2),W,2),2),2)
    Q1=jadd(Q1,jdiv(jdr(ratio),denominator,2),2)
    bracket=Q1[1]/2-qinf*Q1[0]/2-z*Q1[0]*Q1[0]/4
    deltaV=z*bracket/(kappa*kappa)
    if not deltaV.is_finite():raise ValueError("the complete removable frequency correction is nonfinite")
    return deltaV,dict(
        exact_complex_z_square_halfwidth=str(Z),
        all_input_j_abs_at_least=97,physical_frequency="4j",
        both_carrier_signs=True,
        full_intermediate_labels=list(range(1,97)),
        full_intermediate_denominator_modulus_lower=rec(minimum),
        complete_one_plus_z_alpha_over_eta_modulus_lower=rec(gap),
        complete_root_potential_difference=crec(deltaV),
        root_potential_difference_modulus_upper=rec(up(deltaV)),
        factored_root_difference_divided_by_z_modulus_upper=rec(up(bracket/(kappa*kappa))),
        fixed_z_radial_derivative=True,
        independent_full_potential_upper_bounds_subtracted=False,
        only_new_rational_root_scalar_algebra=True),dict(
        z=L.cpack(z),U=[L.cpack(v) for v in U],W=[L.cpack(v) for v in W],
        alpha=[L.cpack(v) for v in alpha],alpha_over_eta=[L.cpack(v) for v in ratio],
        Q1=[L.cpack(v) for v in Q1],deltaV=L.cpack(deltaV))

def root_forcing(c,op,kappa):
    d=c["d"][0];C=d.theta();Cphi=C.theta()
    Cr=c["d"][1].theta().scale(-1)
    DC=Cr-d*Cphi
    C2=C*C
    v2=c["v"][0]*c["v"][0]
    beta=c["beta"][0].scalar_value()
    Kr=-c["K"][1].scalar_value()
    eta=c["eta"][0].scalar_value()
    Lroot=-c["a"][1].scalar_value()/c["a"][0].scalar_value()
    qinf=op["epoly"][0].mean()-op["bloc"][0].mean()-c["eta"][1].scalar_value()/eta
    theta_raw=op["vartheta"][0]
    if not is_odd(theta_raw):raise ValueError("the original complete vartheta lost its exact reflection identity")
    theta=P(theta_raw)
    if C.mean()!=0 or Cr.mean()!=0:raise ValueError("an old angular derivative acquired a constant coefficient")
    if not (DC.mean()-C2.mean()).contains(0):
        raise ValueError("the complete periodic DC mean identity is inconsistent with the accepted root data")
    multiplier=ex(Q(12,35))*Lroot-ex(Q(3,2))*qinf
    terms=dict(linear_C=C.scale(multiplier),
        quadratic_C=P(C2).scale(ex(Q(-291,140))),
        material_C=P(DC).scale(ex(Q(15,14))),
        curvature_v2=P(v2).scale(2*beta*Kr))
    bracket=sum(terms.values(),L.LP.zero())
    fb_nonmean=bracket.divide_scalar(-kappa*kappa)
    fa=(Cphi.scale(ex(Q(8,5)))-theta).scale(I/kappa)
    if not is_odd(fa):raise ValueError("the complete second forcing row lost its odd root identity")
    fa=P(fa)
    deltaV,frequency,finite_work=rational_frequency_shift(c,qinf,kappa)
    quadratic_mean=ex(Q(141,140))*C2.mean()/(kappa*kappa)
    root_mean=deltaV+quadratic_mean
    fb=fb_nonmean+root_mean
    if max(fb.degree,fa.degree)>384:
        raise ValueError("a complete root forcing exceeded its proved noncircular support")
    # Check the mean using the unsplit F.20 expression before its exact projection.
    unsplit=(C.scale(multiplier)+C2.scale(ex(Q(-291,140)))
        +DC.scale(ex(Q(15,14)))+P(v2).scale(2*beta*Kr)).divide_scalar(-kappa*kappa)+deltaV
    if not (unsplit.mean()-root_mean).contains(0):
        raise ValueError("the two exact complete old-angle scalar identities are inconsistent")
    for j in range(-384,385):
        if not (unsplit.coefficient(j)-fb.coefficient(j)).contains(0):
            raise ValueError("the exact scalar/nonconstant split changed one complete signed Fourier mode")
    public=dict(
        exact_point="the original certified true root, physical piece2549",
        exact_complex_delta_square_halfwidth=str(DELTA),
        old_angular_root_mean_of_normalized_first_forcing=crec(root_mean),
        root_mean_modulus_upper=rec(up(root_mean)),
        nonradial_quadratic_root_mean=crec(quadratic_mean),
        nonradial_quadratic_root_mean_modulus_upper=rec(up(quadratic_mean)),
        amplitude_mean_is_not_independent_physical_even_mean=True,
        rational_frequency_conclusion=frequency,
        complete_first_row=complete_norm_rows(fb),
        complete_nonconstant_first_row=complete_norm_rows(fb_nonmean),
        complete_second_row_epsilon_plus=complete_norm_rows(fa),
        exact_carrier_sign_rule=dict(fb_minus="fb_plus",fa_minus="-fa_plus",
            same_complex_delta_without_conjugation=True),
        complete_Fourier_support=dict(first=[fb.lo,fb.hi],second=[fa.lo,fa.hi],
            proved_max_absolute_label=384,physical_multiplier=4,noncircular=True),
        complete_coefficients_enclosed_uniformly_before_sum_over_output_modes=True,
        parameter_reality_not_assumed=True,
        no_projection_back_to_background_degree96=True,
        old_circle_I_J_and_distributional_reference_seams_not_removed=True,
        independent_even_mean_equation_retained=True,
        genuine_new_w1_not_yet_solved=True,
        whole_root_piece_source_norm_proved=False,full_high_BVP_inverse_proved=False)
    work=dict(C=C.record(),C2=C2.record(),DC=DC.record(),vartheta=theta.record(),
        complete_ordered_nonconstant_terms={k:v.record() for k,v in terms.items()},
        fb=fb.record(),fb_nonmean=fb_nonmean.record(),fa_epsilon_plus=fa.record(),
        root_mean=L.cpack(root_mean),qinf=L.cpack(qinf),Lroot=L.cpack(Lroot),
        kappa=L.cpack(kappa),finite_frequency_work=finite_work)
    return public,work

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","manifest","out-dir"):parser.add_argument("--"+k,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new signed root mathematics runs only in the authorized public Actions repository")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),
        python_flint=flint.__version__,numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the reviewed exact runtime changed")
    ctx.prec=320;ctx.cap=4
    args.out_dir.mkdir(parents=True,exist_ok=True)
    native=args.out_dir/"temporary-genuine-reference-root-forcing.json.gz"
    if native.exists():raise FileExistsError("preserve an original complete or failed temporary result")
    started=time.monotonic()
    doc=dict(kind="actual_signed_genuine_common_reference_root_first_forcing",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),algebra_sha256=sha(L.__file__),
        input_manifest_sha256=sha(args.manifest),runtime=runtime,
        complete=False,proved=False,actual_returncode=None,failure=None,gates=[],
        original_target_FFT_intrinsic_cubic_or_point_derivatives_recomputed=0,
        original_fold_forcing_or_saved_Taylor_coefficients_recomputed=0,
        original_natural_stage_bytes_modified=0,original_complete_root_stages_read=0,
        new_complete_signed_root_forcing_cases=0,new_ordinary_source_or_full_inverse_claimed=False,
        reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def checkpoint():
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started;save(native,doc)
    def gate(name,value):
        ok=bool(value);doc["gates"].append(dict(name=name,passed=ok));checkpoint()
        if not ok:raise ValueError(name)
    try:
        manifest=read(args.manifest)
        gate("the current signed-root source, complete algebra and manifest have exact reviewed identities",
            doc["input_manifest_sha256"]==args.manifest_sha
            and doc["source_sha256"]==manifest["scientific_source_sha256"]
            and doc["algebra_sha256"]==ALGEBRA and manifest["public_repository"]==PUBLIC
            and manifest["mathematical_parameters"]["exact_complex_z_square_halfwidth"]==str(Z)
            and manifest["mathematical_parameters"]["exact_complex_delta_square_halfwidth"]==str(DELTA)
            and manifest["mathematical_parameters"]["exact_old_phi_widths"]==list(map(str,WIDTHS)))
        for entry in manifest["files"]:
            p=args.repo/entry["path"]
            if not p.is_file() or p.stat().st_size!=entry["bytes"] or sha(p)!=entry["sha256"]:
                raise ValueError("an immutable reviewed input changed: "+entry["path"])
        paths={k:args.repo/v for k,v in manifest["input_paths"].items()}
        gate("all exact original root files and the newly proved signed identity were checked",
            sha(paths["contract"])==CONTRACT and sha(paths["Taylor_native"])==TAYLOR
            and sha(paths["Taylor_process"])==TPROC and sha(paths["Taylor_publication"])==TPUB
            and sha(paths["original_Taylor_source"])==OLD_SOURCE
            and sha(paths["original_Taylor_manifest"])==OLD_MANIFEST)
        tn,tp,pub=[read(paths[k]) for k in ("Taylor_native","Taylor_process","Taylor_publication")]
        sm=tp["scientific_metadata"]
        gate("the original complete Taylor run actually succeeded and retained all old75 stage bytes",
            tn["complete"] and tn["proved"] and tn["failure"] is None
            and tn["source_sha256"]==TSOURCE and tn["input_manifest_sha256"]==TMANIFEST
            and tn["runtime"]==runtime and tn["algebra_sha256"]==ALGEBRA
            and tp["actual_returncode"]==0 and tp["native_sha256"]==TAYLOR
            and tp["mathematical_complete"] and tp["mathematical_proved"]
            and tp["mathematical_failure"] is None and tp["original75_stage_bytes_unchanged"]
            and all(v["passed"] for v in tn["gates"])
            and pub["actual_returncode"]==0 and pub["complete"])
        gate("the same true root, repaired finite family and fixed eta0 are retained",
            sm["background_definition_sha256"]==BASE
            and sm["explicit_direction_definition_sha256"]==ZDEF
            and sm["actual_intrinsic_parameter"]=="eta_0"
            and sm["exact_complex_delta_radius"]==str(DELTA)
            and sm["exact_root_interval"]==list(ROOTS)
            and sm["exact_original_physical_piece_interval"]==list(PIECE))
        published={entry["file"]:entry for entry in pub["files"]}
        stages={};receipts=[]
        for key,(name,size,digest) in STAGES.items():
            path=paths[key];entry=tn["original_stages"][name]
            saved=read(path);publication=published["consumers/"+entry["file"]]
            gate("the original complete "+name+" keeps its exact old header and byte identity",
                sha(path)==digest and path.stat().st_size==size
                and entry["sha256"]==publication["sha256"]==digest
                and entry["bytes"]==publication["bytes"]==size
                and saved["stage"]==name and saved["complete"]
                and saved["source_sha256"]==OLD_SOURCE
                and saved["input_manifest_sha256"]==OLD_MANIFEST
                and saved["algebra_sha256"]==ALGEBRA and saved["runtime"]==runtime)
            stages[key]=saved["payload"]
            receipts.append(dict(name=name,original_relative_file=entry["file"],bytes=size,sha256=digest,
                original_payload_sha256=jhash(saved["payload"]),
                original_source_sha256=OLD_SOURCE,original_manifest_sha256=OLD_MANIFEST))
            doc["original_complete_root_stages_read"]+=1
        bg=stages["background_stage"]
        gate("the old complete repair and both physical mean slots remain in the original root background",
            bg["complete_mean_at_all_orders_retained"]
            and bg["positive_order_value_repair_derivatives_exactly_zero"]
            and bg["original_65_and_193_rows_retained"] and bg["zero_bump_germ_and_fixed_eta0"])
        c={key:L.unpack_series(values) for key,values in bg["series"].items()}
        op={key:L.unpack_series(values) for key,values in stages["operator_stage"].items()}
        qstage=stages["leading_Q_stage"]
        leadingQ=L.unpack_series(qstage["coefficients"])
        kappa=leadingQ[0].scalar_value()
        gate("only original full root coefficients and the already paid scalar kappa are consumed",
            qstage["name"]=="Q" and len(leadingQ)==9 and len(c["u"])==len(c["v"])==9
            and all(v.degree<=96 for v in c["u"]+c["v"])
            and all(len(op[key])==7 for key in ("vartheta","epoly","bloc"))
            and c["K"][0].is_zero()
            and c["u"][0].mean()==0 and c["u"][1].mean()==0 and c["u"][2].mean()==0
            and c["eta"][0].scalar_value().real>0 and kappa.real>0)
        doc["original_stage_receipts"]=receipts
        public,work=root_forcing(c,op,kappa)
        doc["complete_root_conclusion"]=public;doc["temporary_signed_work"]=work
        doc["new_complete_signed_root_forcing_cases"]=1
        gate("the full old-angle mean and every signed Fourier coefficient satisfy F20 to F22",
            public["complete_Fourier_support"]["proved_max_absolute_label"]==384
            and public["amplitude_mean_is_not_independent_physical_even_mean"]
            and public["complete_coefficients_enclosed_uniformly_before_sum_over_output_modes"])
        gate("both carrier signs, the old primitive and the independent physical even mean remain",
            public["exact_carrier_sign_rule"]["same_complex_delta_without_conjugation"]
            and public["old_circle_I_J_and_distributional_reference_seams_not_removed"]
            and public["independent_even_mean_equation_retained"]
            and not public["whole_root_piece_source_norm_proved"]
            and not public["full_high_BVP_inverse_proved"])
        doc["complete"]=doc["proved"]=True;doc["actual_returncode"]=0
    except Exception as error:
        doc["failure"]=type(error).__name__+": "+str(error);doc["actual_returncode"]=1
    finally:
        checkpoint()
        compact={k:v for k,v in doc.items() if k!="temporary_signed_work"}
        compact["temporary_native_sha256"]=sha(native)
        compact["temporary_native_bytes"]=native.stat().st_size
        compact["temporary_native_is_not_published"]=True
        compact_raw=(json.dumps(compact,separators=(",",":"),allow_nan=False)+"\n").encode()
        if len(compact_raw)>60000:raise ValueError("actual small root process exceeds60000 bytes")
        save(args.out_dir/"process.json",compact)
        lines=["# Actual signed first forcing at the genuine common-reference root","",
            "Public Actions run "+str(doc["run_id"])+"/"+str(doc["run_attempt"])+".",
            "Actual mathematical return code: "+str(doc["actual_returncode"])+".",
            "Source SHA256: "+doc["source_sha256"]+".",
            "Input manifest SHA256: "+doc["input_manifest_sha256"]+".",
            "Original targets, FFTs, intrinsic derivatives, repairs, fold and accepted Taylor coefficients recomputed: 0.",
            "Only the original three complete root stages are consumed; complete new work remains temporary.","",
            "Scope: the same finite repaired complex-delta family at fixed eta0 and the certified true root.",
            "All input |j|>=97, both carrier signs, and every physical Fourier output are retained.",
            "The amplitude mean below is not the independent physical even-mean equation.",
            "No whole-piece forcing norm, new w1 solution, complete old-circle remainder or high inverse is claimed.",""]
        if doc.get("complete_root_conclusion"):
            c=doc["complete_root_conclusion"];f=c["rational_frequency_conclusion"]
            lines+=["## Complete root scalar conclusions","",
                "- Complete amplitude root mean modulus: "+c["root_mean_modulus_upper"]["ball"]+".",
                "- Nonradial quadratic amplitude mean modulus: "+c["nonradial_quadratic_root_mean_modulus_upper"]["ball"]+".",
                "- Factored finite-frequency root potential difference modulus: "+f["root_potential_difference_modulus_upper"]["ball"]+".",
                "- Difference divided by z modulus: "+f["factored_root_difference_divided_by_z_modulus_upper"]["ball"]+".",
                "- Full intermediate denominator gap: "+f["full_intermediate_denominator_modulus_lower"]["ball"]+".",
                "- Full a/eta root gap: "+f["complete_one_plus_z_alpha_over_eta_modulus_lower"]["ball"]+".","",
                "The zero Fourier coefficient was assembled from the signed F21--F22 identity. No two unrelated upper bounds were subtracted.",""]
            for label in ("complete_first_row","complete_nonconstant_first_row","complete_second_row_epsilon_plus"):
                lines+=["## "+label.replace("_"," "),"",
                    "| old phi width | derivative0 | derivative1 | derivative2 | derivative3 |",
                    "|---|---|---|---|---|"]
                for row in c[label]:
                    lines.append("| "+row["exact_old_phi_width"]+" | "+" | ".join(
                        v["ball"] for v in row["complete_joint_Wiener_derivative_upper"])+" |")
                lines.append("")
            lines+=["The minus-carrier first row equals the plus row; its second row has the opposite sign at the same complex delta.",
                "The independent even mean, genuine matching jumps, and complete old-circle I/J terms remain obligations.",""]
        lines+=["## Actual gates",""]+["- "+v["name"]+": "+str(v["passed"])+"." for v in doc["gates"]]
        if doc["failure"]:lines+=["","Actual failure: "+doc["failure"]]
        text="\n".join(lines)+"\n"
        if len(text.encode())>60000:raise ValueError("actual small root conclusion exceeds60000 bytes")
        (args.out_dir/"conclusion.md").write_text(text,encoding="utf-8")
    print(json.dumps(dict(complete=doc["complete"],actual_returncode=doc["actual_returncode"],
        original_complete_root_stages_read=doc["original_complete_root_stages_read"],
        original_saved_stages_recomputed=0,new_complete_signed_root_forcing_cases=doc["new_complete_signed_root_forcing_cases"],
        actual_seconds=doc["actual_mathematical_wall_seconds"]),sort_keys=True),flush=True)
    raise SystemExit(doc["actual_returncode"])

if __name__=="__main__":main()
