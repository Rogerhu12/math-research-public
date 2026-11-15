#!/usr/bin/env python3
"""New complete original96 waist lifting from three immutable small scientific receipts."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,platform,time,traceback
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
SOURCE=TOPIC/"scripts/fourfold_codazzi_complete_waist_lifting.py"
KIND="actual_complete_waist_lifting_from_saved_positive_algorithm_v1"
CONTRACT="e2e9d6d4dc98c8f0b2d9c6c5cc7700a3389d228c39470736f3a8706dccbd192e"
D_SOURCE="827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320"
D_MANIFEST="14271d7d61c70996092f105768ca29cc0dd355665be0becea4386441b38c907f"
CPA_SOURCE="c8aaace95295a58d761d1b74422a38d1de721fdf7fd27867b8a7c4e87e88c5b1"
CPA_MANIFEST="fc5acb986c2f8c55e9f6bd25a093a8d9e0594890ad8fbf24175e46e74abe001c"
WA_SOURCE="098ae59647b7555840aff41153d90c6cc9b25faa9561a96ccf74eb3b3aff1e91"
WA_MANIFEST="3cf007a268086df861947dc3bf8efc996828fb908dca28b89599d4aa38cc8a0f"
BACKGROUND="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
FIXED_INPUTS={
    "D_execution":"6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071",
    "D_source":D_SOURCE,
    "CPA_execution":"6865e7e88c9d1be02b6fe062765750fa2f66a1186ab4ff9d43127f2c9c92f4b8",
    "WA_execution":"ae7c3b792d36b9df06362eec362f03978e7a4a97e3e126eb34e066a98d41d538",
    "NF_contract":"9c33e8827d7c3f1d76d6ba74d8cde7be6e98f822b00520932a9e02eeacb245ef",
    "SR_contract":"43da1e99cfcbfc406fb391600b1451c523ab4505aeba9ae1f2335d1c34c59be5",
    "new_contract":CONTRACT}
DELTA=Fraction(1,10**10);LENGTH=Fraction(9,10)
NEGATIVE=Fraction(2383968743003,10**13)
WINDOWS=("whole_inner_body","fixed_complete_negative_phase_window","true_cut_trace")
DOMAINS=(("full_physical_gamma_product","1/1000000000"),
         ("tail_physical_gamma_subdomain","1/128000000000"))
PARAMETERS=dict(exact_parameter_half_width=str(DELTA),exact_core_interval=["0",str(LENGTH)],
    exact_negative_interval=["0",str(NEGATIVE)],background_pair_A0="7",
    background_pair_angle_A0="6",response_pair_A0="19",response_pair_angle_A0="83",
    head_maximum_physical_frequency=384,original96_orthonormal_waist_rows=True,
    ordinary_source_measure="ordinary dr and normalized physical circle",
    full_even_mean_retained=True,only_whole_successful_CPA_cases_used=True,
    old_scientific_producers_or_integrals_called=0,expected_structural_gate_count=18)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def canonical(v):return (json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
def save(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".partial")
    t.write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+"\n");t.replace(p)
def gate(doc,name,passed):
    doc["gates"].append(dict(name=name,passed=bool(passed)))
    if not passed:raise ValueError("scientific gate failed: "+name)
def exact(value):
    f=Fraction(value);return arb(f.numerator)/arb(f.denominator)
def up(v):
    a=arb(v)
    if not a.is_finite():raise ArithmeticError("a complete directed scalar is not finite")
    return a.upper()
def nonnegative(v):
    a=arb(v)
    if not a.is_finite() or not a.lower()>=0:
        raise ArithmeticError("a complete positive scalar is negative or nonfinite")
    return a
def saved(raw):
    if not isinstance(raw,dict) or set(raw)!={"ball"} or not isinstance(raw["ball"],str):
        raise ValueError("an original complete scalar ball has the wrong schema")
    return nonnegative(arb(raw["ball"])).upper()
def positive_lower(v):
    a=arb(v)
    if not a.is_finite() or not a.lower()>0:
        raise ArithmeticError("a required complete denominator is not strictly positive")
    return a.lower()
def root_upper(v):return up(nonnegative(v).upper().sqrt())
def rec(v):
    a=arb(v)
    if not a.is_finite():raise ArithmeticError("refuse to serialize a nonfinite scientific value")
    return dict(ball=a.str(60,radius=True))
def complete_receipt(execution,run,source,manifest,gates):
    r=execution.get("actual_scientific_receipt",{})
    return (execution.get("complete") is True and execution.get("actual_returncode")==0
        and execution.get("actual_source_budget_processes")==1
        and execution.get("source_budget_source_sha256")==source
        and execution.get("input_manifest_sha256")==manifest
        and execution.get("old_numerical_enclosures_recomputed")==0
        and r.get("complete") is True and r.get("actual_returncode")==0 and r.get("failure") is None
        and r.get("source_sha256")==source and r.get("input_manifest_sha256")==manifest
        and str(r.get("run_id"))==run and str(r.get("run_attempt"))=="1"
        and len(r.get("gates",[]))==gates
        and all(g.get("passed") is True for g in r["gates"]))
class Inputs:
    def __init__(self,root,manifest,doc):
        root=Path(root);m=read(manifest);self.paths={}
        gate(doc,"public runtime and exact320-bit directed scalar arithmetic",
            os.environ.get("GITHUB_ACTIONS")=="true"
            and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
            and platform.python_version()=="3.12.14" and flint.__version__=="0.9.0" and ctx.prec==320)
        ok=(m.get("public_repository")==PUBLIC and m.get("source_path")==str(SOURCE)
            and m.get("source_sha256")==sha(root/SOURCE)
            and m.get("parameters")==PARAMETERS and m.get("expected_scientific_gates")==18
            and m.get("all_inputs_are_current_small_texts") is True
            and m.get("legacy_artifact_inputs")==[]
            and m.get("old_successful_scientific_calls_allowed") is False)
        paths={}
        for e in m["files"]:
            p=Path(e["path"])
            if p.is_absolute() or ".." in p.parts or not str(p).startswith(str(TOPIC)+"/"):
                raise ValueError("a pinned input left the authorized topic")
            if str(p) in paths:raise ValueError("duplicate immutable input")
            f=root/p
            ok=ok and f.is_file() and f.stat().st_size==e["bytes"] and sha(f)==e["sha256"]
            ok=ok and e["bytes"]<100000 and f.suffix in (".json",".py",".md")
            paths[str(p)]=f
        self.paths={role:paths[p] for role,p in m["input_paths"].items()}
        ok=ok and set(m["input_paths"])==set(FIXED_INPUTS)|{"new_source"}
        ok=ok and set(paths)==set(m["input_paths"].values())
        ok=ok and all(sha(self.paths[k])==v for k,v in FIXED_INPUTS.items())
        ok=ok and self.paths["new_source"]==root/SOURCE and sha(root/SOURCE)==doc["source_sha256"]
        gate(doc,"complete pinned small closure and unchanged scientific parameters",ok)
        nf=self.paths["NF_contract"].read_text();sr=self.paths["SR_contract"].read_text()
        wl=self.paths["new_contract"].read_text()
        gate(doc,"same fullmean original96 lift and uniform complete secant inverse contracts",
            all(r"\tag{NF."+str(k)+"}" in nf for k in (21,22,23,24))
            and all(r"\tag{SR."+str(k)+"}" in sr for k in (20,21))
            and all(r"\tag{WL."+str(k)+"}" in wl for k in (6,8,10,12,15,16,17)))
        de=read(self.paths["D_execution"]);d=de["actual_scientific_receipt"];self.d=d
        gate(doc,"original D unique child and all twelve complete gates succeeded",
            complete_receipt(de,"43713242980",D_SOURCE,D_MANIFEST,12)
            and d.get("proved") is True and d.get("complete_selected_parameter_body_scalar_fees_proved") is True
            and d.get("original_enclosures_recomputed")==0
            and d.get("old_target_Fourier_cubic_mean_residual_integral_or_Green_calls")==0)
        ds=self.paths["D_source"].read_text()
        required=(
            'Q0=q(7);Q1=q(6);Z0=q(19);Z1=q(83);Em=d*Z0',
            'E0=d*Z0;E1=d*Z1;m0=Q0',
            'gp=up(g*half)',
            'kp=max(arb(1),up(full*(k+d*t*W1)))',
            'change=up(kp*(2*Q0*E0+E0*E0))',
            'M1=up(b*change/4+gp*kp*Em+b*kd*Q0*Q0/4+m0*jd)',
            'M0=up(3*b*change+b*kp*(E0*Q1+(Q0+E0)*E1)/2+gp*kp*E1')
        gate(doc,"the exact original nonnegative M0 and M1 algorithm terms are retained",
            all(s in ds for s in required) and "def selected_parameter_fees(jets,left,right):" in ds)
        p=d["parameters"];whole=d["complete_scalar_fee_conclusions"]["whole_core"];self.whole=whole
        legacy=d["original_response_legacy_progress"]
        gate(doc,"the complete old core restrictions support the fixed selected parameter ball",
            p["delta_half_width"]==str(DELTA) and p["exact_core_interval"]==["0",str(LENGTH)]
            and p["exact_negative_interval"]==["0",str(NEGATIVE)]
            and p["exact_compact_support"]==["1/20","9/50"]
            and p["complete_original_interval"]==["0","25/8"]
            and p["complete_original_parts"]==40 and p["complete_original_rows"]==7721
            and p["fixed_intrinsic_parameter"]=="eta_0" and p["real_delta_family_only"] is True
            and p["head_maximum_physical_frequency"]==384 and p["original_physical_frequency_factor"]==4
            and p["source_norm"]=="ordinary L2_r L2_phi; normalized circle, full mean"
            and d["complete_original_rows_verified"]==7721 and len(d["original_part_receipts"])==40
            and d["derived_continuous_centre_definition_sha256"]==BACKGROUND
            and d["derived_continuous_response_definition_sha256"]==DIRECTION
            and whole["exact_interval"]==["0",str(LENGTH)]
            and whole["exact_total_radial_measure"]==str(LENGTH)
            and whole["original_closed_rows_consumed"]==6376 and whole["new_exact_scalar_restrictions"]==6377
            and legacy["actual_completed_common_rows"]==7680 and legacy["complete_common_rows"]==7721
            and legacy["complete_original_part_and_row_cover_verified_separately"] is True)
        chosen=dict(background_pair_A0="7",background_pair_angle_A0="6",
                    response_pair_A0="19",response_pair_angle_A0="83")
        gate(doc,"all four complete repaired state bounds lie in the original chosen constants",
            d["chosen_global_constants"]==chosen and all(
                saved(d["verified_global_state_bounds"][k])<=exact(v) for k,v in chosen.items()))
        self.max0=saved(whole["maxima"]["M0"]);self.max1=saved(whole["maxima"]["M1"])
        gate(doc,"the two full saved positive budget maxima are finite and strictly positive",
            self.max0>0 and self.max1>0)
        ce=read(self.paths["CPA_execution"]);c=ce["actual_scientific_receipt"];self.cpa=c
        gate(doc,"original CPA unique child and all eighteen complete structural gates succeeded",
            complete_receipt(ce,"43741463694",CPA_SOURCE,CPA_MANIFEST,18)
            and c["proved_complete_weighted_inner_cap_difference_diagnosis"] is True
            and c["new_finite_case_count"]==c["new_finite_case_pass_count"]==2
            and c["original_F_case_recomputations"]==0
            and c["original_Green_native_matrix_Gram_sweep_or_target_calls"]==0)
        cp=c["parameters"]
        gate(doc,"ordinary wholecore inputs and truecut outputs retain every mean and high qualification",
            cp["exact_core_interval"]==["0",str(LENGTH)] and cp["exact_cap_interval"]==["9/10","25/8"]
            and cp["complete_even_mean_and_all_physical_Fourier_modes_retained"] is True
            and cp["unknown_high_input_is_not_truncated"] is True
            and cp["normalized_outer_height_radius"]=="1/1152921504606846976"
            and c["original_source_measure"]=="ordinary dr and normalized physical circle"
            and c["original_right_row_input_units"]=="original97 regular row Euclidean coordinates; no second rho input weight"
            and c["full_even_mean_and_all_physical_modes_retained"] is True
            and c["unknown_high_and_original_full97_coordinates_retained"] is True)
        cases=c["complete_gamma_domain_cases"];self.cases=cases
        case_ok=len(cases)==2
        for row,(name,radius) in zip(cases,DOMAINS):
            f=row["new_finite_feedback"];g=f["transferred_columns"]["ordinary_whole_core_source"]
            case_ok=case_ok and row["name"]==name and row["physical_gamma_A0_radius"]==radius
            case_ok=case_ok and row["all_new_strict_sufficient_gates_passed"] is True
            case_ok=case_ok and row["input_domain_is_original_physical_reflection_product"] is True
            case_ok=case_ok and row["ordinary_inner_Cmean_retained"] is True and row["unknown_high_input_is_not_truncated"] is True
            case_ok=case_ok and f["all_strict_sufficient_gates_passed"] is True
            case_ok=case_ok and f["finite193_inverse_under_stated_boundary_hypotheses_proved"] is True
            case_ok=case_ok and f["actual_cap_domain_hypotheses_required"] is True
            case_ok=case_ok and f["actual_cap_domain_proved_by_this_consumer"] is False
            case_ok=case_ok and f["true_high_inverse_required_before_infinite_Schur"] is True
            case_ok=case_ok and len(f["diagonal_gaps"])==2 and all(
                arb(x["ball"]).lower()>0 for x in f["diagonal_gaps"])
            case_ok=case_ok and arb(f["determinant"]["ball"]).lower()>0
            case_ok=case_ok and len(f["strict_sufficient_gates"])==3 and all(
                v is True for v in f["strict_sufficient_gates"].values())
            case_ok=case_ok and set(g)==set(WINDOWS) and all(saved(g[k])>0 for k in WINDOWS)
        gate(doc,"each complete successful CPA case supplies its own three ordinary gains",case_ok)
        we=read(self.paths["WA_execution"]);w=we["actual_scientific_receipt"];self.wa=w
        gate(doc,"original WA unique child and all thirteen complete gates succeeded",
            complete_receipt(we,"43747940791",WA_SOURCE,WA_MANIFEST,13) and w["proved"] is True
            and w["new_exact_rational_dot_products"]==3 and w["new_uniform_parameter_intervals"]==4
            and w["old_response_or_repair_producers_called"]==w["old_Green_or_Poisson_products_recomputed"]==0
            and w["old_scientific_source_imports"]==0)
        wi=w["complete_input_identity_conclusion"]
        gate(doc,"the WA norm uses the same continuous193 direction and original96 orthonormal rows",
            wi["background_definition_sha256"]==BACKGROUND and wi["direction_definition_sha256"]==DIRECTION
            and wi["physical_frequency_factor"]==4 and wi["original_full_state_sizes"]==[65,193]
            and wi["new_base_bitwise_entries_checked"]==65
            and wi["orthonormal_waist_conversion"]=="raw sine amplitude divided by sqrt(2)"
            and wi["background_only_multiplied_by_alpha"] is True and wi["response_not_multiplied_by_alpha"] is True
            and wi["original_even_mean_retained_in_input_identity"] is True
            and wi["no_even_mean_constraint_or_high_waist_condition_removed"] is True)
        selected=[r for r in w["complete_uniform_waist_conclusion"] if r["exact_parameter_half_width"]==str(DELTA)]
        gate(doc,"exactly the completed WA radius1e-10 is selected without a new normalization",
            len(selected)==1 and selected[0]["normalized_circle_odd_L2"] is True
            and selected[0]["no_parameter_sampling"] is True
            and selected[0]["no_extension_of_PDE_phase_cap_or_metric_domain"] is True)
        self.wa_row=selected[0];self.wa_upper=saved(self.wa_row["uniform_original96_Euclidean_waist_norm_upper"])
        doc["original_successful_small_receipts_read"]=3
        doc["complete_original_input_conclusion"]=dict(
            source_receipts={name:dict(run=run,source_sha256=source,manifest_sha256=manifest,gates=count)
                for name,run,source,manifest,count in (
                    ("D","43713242980",D_SOURCE,D_MANIFEST,12),
                    ("CPA","43741463694",CPA_SOURCE,CPA_MANIFEST,18),
                    ("WA","43747940791",WA_SOURCE,WA_MANIFEST,13))},
            original_small_input_sha256=FIXED_INPUTS,chosen_global_constants=chosen,
            complete_original_rows=7721,complete_original_parts=40,
            complete_core_original_closed_rows=6376,complete_core_exact_restrictions=6377,
            complete_core_exact_measure=str(LENGTH),compact_support=["1/20","9/50"],
            original_progress_7680_is_not_completion=True,
            background_definition_sha256=BACKGROUND,direction_definition_sha256=DIRECTION,
            original_D_M0_maximum=whole["maxima"]["M0"],original_D_M1_maximum=whole["maxima"]["M1"],
            original_WA_selected_radius=str(DELTA),
            original_WA_waist_norm=self.wa_row["uniform_original96_Euclidean_waist_norm_upper"],
            original_WA_selected_complete_row_sha256=hashlib.sha256(canonical(self.wa_row)).hexdigest(),
            same_original96_coordinates_no_second_alpha_or_sqrt2=True)

def recover_positive_products(inp,doc):
    eps=Fraction(19)*DELTA;eps1=Fraction(83)*DELTA;u0=14*eps+eps*eps
    B=up(inp.max0/(3*positive_lower(exact(u0))))
    G=up(inp.max1/positive_lower(exact(eps)))
    gate(doc,"two new complete coefficient products follow from positive algorithm summands",
        B.is_finite() and G.is_finite() and B>0 and G>0 and u0>0 and eps>0)
    doc["new_positive_algorithm_product_bounds"]=2
    doc["complete_positive_product_conclusion"]=dict(
        exact_epsilon=str(eps),exact_epsilon1=str(eps1),exact_U0=str(u0),
        B_star=rec(B),G_star=rec(G),
        B_star_scope="absolute beta times max(1,absolute K_delta), uniformly on the whole core",
        G_star_scope="absolute G_delta times max(1,absolute K_delta), uniformly on the whole core",
        same_original_positive_algorithm_lower_summands_used=True,
        no_abstract_operator_norm_reverse_inference=True,
        no_division_by_current_delta_or_unknown_state=True)
    return B,G,eps,eps1

def complete_lift_constants(B,G,eps,eps1,doc):
    M=exact(Fraction(7)+eps);Mp=exact(Fraction(6)+eps1)
    a=up(384*(arb.pi()*B*M*M/8+G*M)+B*(1+3*M*M+M*Mp/2)+G*Mp)
    directB=root_upper(exact(LENGTH/3))
    invL=root_upper(exact(1/LENGTH));ell=up(invL+a*directB)
    J=NEGATIVE-NEGATIVE*NEGATIVE/LENGTH+NEGATIVE**3/(3*LENGTH*LENGTH)
    directN=root_upper(exact(J))
    gate(doc,"the complete finite96 coefficient and both exact ordinary radial lift integrals are finite",
        all(v.is_finite() and v>=0 for v in (M,Mp,a,directB,invL,ell,directN))
        and Fraction(0)<NEGATIVE<LENGTH and J>0)
    doc["new_complete_finite96_coefficients"]=1;doc["new_complete_ordinary_lift_coefficients"]=1
    doc["complete_lift_constant_conclusion"]=dict(
        M=rec(M),M_phi=rec(Mp),a_star=rec(a),ell_star=rec(ell),
        exact_L=str(LENGTH),exact_negative_endpoint=str(NEGATIVE),exact_J_N=str(J),J_N=rec(exact(J)),
        direct_whole_body_lift=rec(directB),direct_negative_window_lift=rec(directN),
        direct_truecut_lift_is_exactly_zero=True,
        original_maximum_physical_frequency=384,original_left_row_input_dimension=96,
        complete_projected_body_dimension=193,full_even_mean_retained=True,
        square_roots_from_nonnegative_exact_quantities_or_proved_upper_bounds=True,
        source_measure="ordinary dr and normalized circle pair L2")
    return ell,directB,directN

def complete_case_columns(inp,ell,directB,directN,doc):
    rows=[]
    for original in inp.cases:
        f=original["new_finite_feedback"];g=f["transferred_columns"]["ordinary_whole_core_source"]
        gains={k:saved(g[k]) for k in WINDOWS}
        new=dict(whole_inner_body=up(directB+gains["whole_inner_body"]*ell),
            fixed_complete_negative_phase_window=up(directN+gains["fixed_complete_negative_phase_window"]*ell),
            true_cut_trace=up(gains["true_cut_trace"]*ell))
        rows.append(dict(name=original["name"],physical_gamma_A0_radius=original["physical_gamma_A0_radius"],
            original_inner_pair_kappa=original["inner_pair_kappa"],
            original_diagonal_gaps=f["diagonal_gaps"],original_determinant=f["determinant"],
            original_strict_sufficient_gates=f["strict_sufficient_gates"],
            original_ordinary_source_gains=g,
            complete_original96_waist_columns={k:rec(new[k]) for k in WINDOWS},
            complete_selected_waist_contributions={k:rec(up(new[k]*inp.wa_upper)) for k in WINDOWS},
            exact_selected_parameter_half_width=str(DELTA),
            original_WA_waist_norm=inp.wa_row["uniform_original96_Euclidean_waist_norm_upper"],
            input_original96_Euclidean_no_second_weight=True,
            same_CPA_case_used_for_all_three_outputs=True,
            independent_even_mean_and_high_body_high_cut_preserved=True,
            uniform_in_same_case_bounded_secant_cap_operator=True,
            actual_cap_product_domain_hypotheses_required=True,
            actual_cap_domain_entry_proved_here=False,
            affine_right_nonlinear_sources_and_high_inverse_still_independent=True))
    gate(doc,"both complete CPA cases have all three new fifth columns without cross-case minima",
        len(rows)==2 and tuple((r["name"],r["physical_gamma_A0_radius"]) for r in rows)==DOMAINS
        and all(set(r["complete_original96_waist_columns"])==set(WINDOWS) for r in rows))
    doc["complete_fifth_column_cases"]=rows;doc["new_complete_case_count"]=2
    doc["new_complete_waist_column_count"]=6;doc["new_complete_selected_waist_contribution_count"]=6
    return rows

def render(doc):
    lines=["# Actual complete waist lifting from the saved positive scalar algorithm","",
        "Public run: "+doc["run_id"]+"/"+doc["run_attempt"]+".",
        "Complete new scalar target: "+str(doc["complete"])+".",
        "Scientific child return code: "+str(doc["actual_returncode"])+".","",
        "Source SHA256: "+doc["source_sha256"],"Manifest SHA256: "+doc["input_manifest_sha256"],""]
    p=doc.get("complete_positive_product_conclusion",{})
    k=doc.get("complete_lift_constant_conclusion",{})
    if p:
        lines+=["## New complete positive products","",
            "- B_star: "+p["B_star"]["ball"],"- G_star: "+p["G_star"]["ball"],""]
    if k:
        lines+=["## Complete finite96 lift","",
            "- a_star: "+k["a_star"]["ball"],"- ell_star: "+k["ell_star"]["ball"],
            "- Exact negative-window lift integral J_N: "+k["exact_J_N"],""]
    rows=doc.get("complete_fifth_column_cases",[])
    if rows:
        lines+=["## Original96 fifth columns and known selected-waist contributions","",
            "| Complete CPA case | Output | Fifth column | Known waist contribution |","|---|---|---|---|"]
        for row in rows:
            for key in WINDOWS:
                lines.append("| "+row["name"]+" | "+key+" | "+row["complete_original96_waist_columns"][key]["ball"]
                    +" | "+row["complete_selected_waist_contributions"][key]["ball"]+" |")
        lines+=[""]
    lines+=["## Scope","",
        "The fixed selected parameter radius is exactly 1e-10. All complete even means, original96 waist units and both independent high inputs are retained.",
        "D positive summands are read by exact identity; CPA gains come from the same whole case; WA is read with no new alpha or sqrt(2).",
        "No original row, response, repair, source integral, Green sweep, Poisson product or successful scalar was recomputed.",
        "The physical cap entry, right affine and nonlinear sources, whole-core ball, high inverse, parameter equation and final geometry remain separate obligations.",""]
    if doc.get("failure"):lines+=["Actual failure: "+json.dumps(doc["failure"],ensure_ascii=False),""]
    return "\n".join(lines)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root",type=Path,required=True);ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--workdir",type=Path,required=True);ap.add_argument("--process",type=Path,required=True)
    ap.add_argument("--conclusion",type=Path,required=True);ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;started=time.monotonic()
    if args.process.exists() or args.out.exists():raise FileExistsError("preserve an existing actual new waist lift")
    args.workdir.mkdir(parents=True,exist_ok=True)
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),
        runtime=dict(Python=platform.python_version(),python_flint=flint.__version__),
        arithmetic_bits=320,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID",""),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT",""),workflow_event_commit=os.environ.get("GITHUB_SHA",""),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT",""),
        mathematical_parameters=PARAMETERS,original_successful_small_receipts_read=0,
        new_positive_algorithm_product_bounds=0,new_complete_finite96_coefficients=0,
        new_complete_ordinary_lift_coefficients=0,new_complete_case_count=0,
        new_complete_waist_column_count=0,new_complete_selected_waist_contribution_count=0,
        old_numerical_enclosures_recomputed=0,old_rows_or_integrals_recomputed=0,
        old_Green_or_Poisson_products_recomputed=0,old_WA_rational_dot_products_recomputed=0,
        old_scientific_source_imports=0,original_input_bytes_modified=False,
        new_recomputable_arrays_persisted=False,full_high_inverse_claimed=False,
        actual_cap_domain_entry_proved=False,actual_PDE_solution_claimed=False,final_surface_claimed=False,
        scope="only the complete original96 fifth column and its selected-waist contribution under the same successful CPA hypotheses")
    try:
        inp=Inputs(args.repo_root,args.manifest,doc);save(args.process,doc)
        B,G,eps,eps1=recover_positive_products(inp,doc);save(args.process,doc)
        ell,directB,directN=complete_lift_constants(B,G,eps,eps1,doc);save(args.process,doc)
        rows=complete_case_columns(inp,ell,directB,directN,doc)
        gate(doc,"all six complete selected-waist contributions retain every independent obligation with zero old recomputation",
            doc["new_complete_waist_column_count"]==doc["new_complete_selected_waist_contribution_count"]==6
            and all(set(r["complete_selected_waist_contributions"])==set(WINDOWS) for r in rows)
            and doc["old_numerical_enclosures_recomputed"]==doc["old_rows_or_integrals_recomputed"]==0
            and doc["old_Green_or_Poisson_products_recomputed"]==doc["old_WA_rational_dot_products_recomputed"]==0
            and doc["old_scientific_source_imports"]==0)
        if len(doc["gates"])!=18:raise ArithmeticError("the complete new waist lift gate count changed")
        doc.update(complete=True,proved=True,actual_returncode=0)
    except Exception as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
    # Always atomically save every complete scientific scalar before rendering or publication.
    save(args.process,doc);raw=canonical(doc)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with gzip.GzipFile(filename=str(args.out),mode="wb",mtime=0) as out:out.write(raw)
    args.conclusion.parent.mkdir(parents=True,exist_ok=True);args.conclusion.write_text(render(doc))
    print(json.dumps(dict(complete=doc["complete"],actual_returncode=doc["actual_returncode"],
        scientific_conclusion_bytes=len(raw),scientific_conclusion_sha256=hashlib.sha256(raw).hexdigest(),
        gates=len(doc["gates"]),old_numerical_enclosures_recomputed=0),sort_keys=True),flush=True)
    if not doc["complete"]:raise SystemExit(1)
if __name__=="__main__":main()
