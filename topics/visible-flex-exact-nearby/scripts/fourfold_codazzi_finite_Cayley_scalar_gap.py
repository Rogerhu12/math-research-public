#!/usr/bin/env python3
"""Complete new finite Cayley arithmetic from immutable old scalar receipts only."""
from __future__ import annotations
import argparse, ast, copy, gzip, hashlib, importlib.metadata, json, os, platform, time, traceback
from fractions import Fraction
from pathlib import Path
from flint import arb, acb, ctx

PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
SOURCE=REL+"scripts/fourfold_codazzi_finite_Cayley_scalar_gap.py"
KIND="actual_complete_finite_Cayley_scalar_arithmetic_v1"
MANIFEST_KIND="complete_finite_Cayley_scalar_input_contract_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0","arithmetic_bits":320}
GATE_COUNT=18
PINNED={
 "gap_process":"afa699e3e86fc1d6678c35606b116dd8074a6ce7adfca246d8804532e32e0f0b",
 "selected_process":"78cbf8e6b207f23f2d2302ac76c09ca5de58a2a308e40e71aff28dc64eec0d47",
 "gap_source":"d9ed9139d5955429f7cf33835f981adce810c18106a9403334ed6d6ed8e671dc",
 "selected_identification":"f5f980a1fb085103f548d7bbdf6fe0124dda176276fa1b8bac6783b6b22a150c",
 "new_contract":"9a4e41c208f785e1dd3960c047a579a81493ea7cba17f870c9661caf550fd44e"}
OLD_GAP_NATIVE="db861442f5b895362abe090306c2899b3771282269b7ccc5743d820e79f8bff3"
OLD_COEFFICIENT_NATIVE="06070fd3b4bd7a3e4ba17d99821c0f6ad06393863bf538f9a8157b6187e60dbb"
SELECTED_SOURCE="de12b8129caeb8c51857f6b44a152c7a91e1facbdc553d2bd4f4ea320a38406a"
A=5831714953207175
B=21212218271020390
FIRST=97
LAST=1023
TAIL=1024
BETA_LO=Fraction("18.4783243050269")
BETA_HI=Fraction("18.4783387425197")
PARAMETERS={
 "arithmetic_bits":320,"runtime":RUNTIME,
 "exact_quadratic_rotation":{"numerator_integer":str(A),"radical":"sqrt(5)","denominator":str(B)},
 "physical_frequency_factor":4,"first_high_label":FIRST,"last_new_finite_label":LAST,
 "analytic_infinite_tail_starts_at":TAIL,"new_positive_labels":927,
 "new_signed_labels":1854,"new_signed_label_root_pairs":7416,
 "signs":[-1,1],"fourth_roots":["1","i","-1","-i"],
 "new_finite_coefficient_rational_endpoints":[str(BETA_LO),str(BETA_HI)],
 "finite_interval_method":"outward Arb union of the two displayed exact rational endpoints",
 "finite_interval_may_be_wider_than_original_native":True,
 "old_infinite_arithmetic_scope":"only the original exact native interval, hence the actual selected coefficient",
 "old_exponential_gap_times_abs_label":"1/512",
 "new_analytic_tail_gap_times_abs_label":"1/1024",
 "selected_relation":"beta_star=-mu_star/4",
 "mean_multiplier":"exactly one; the scalar difference has mean zero",
 "old_integer_candidates_or_diophantine_arithmetic_recomputed":False,
 "old_scalar_finite_part_root_KAM_ray_or_source_calls":0,
 "incoming_inverse_strong_remainder_or_finite_Schur_claimed":False,
 "expected_structural_gates":GATE_COUNT}

def canonical(x):
    return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
def sha_bytes(x):return hashlib.sha256(x).hexdigest()
def sha(p):return sha_bytes(Path(p).read_bytes())
def read(p):return json.loads(Path(p).read_text())
def save(p,x):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_name(p.name+".partial");tmp.write_bytes(canonical(x));tmp.replace(p)
def rational(x):
    x=Fraction(x);return arb(x.numerator)/x.denominator
def rec(x):
    x=arb(x)
    if not x.is_finite():raise ArithmeticError("a complete new scalar is nonfinite")
    return dict(ball=x.str(72),lower=x.lower().str(72),upper=x.upper().str(72))
def interval(x):
    lo=arb(x["lower"]).lower();hi=arb(x["upper"]).upper()
    if not lo.is_finite() or not hi.is_finite() or not lo<=hi:
        raise ValueError("an old directed scalar interval is not complete and ordered")
    return lo.union(hi)
def gate(doc,name,ok):
    doc["gates"].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError("finite Cayley gate failed: "+name)
def exact_source_constant(text,name):
    found=[]
    for node in ast.parse(text).body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id==name:
            found.append(ast.literal_eval(node.value))
    if len(found)!=1:raise ValueError("the frozen old source has no unique literal "+name)
    return found[0]
def smaller(new,old):
    if old is None:return True
    if new<old:return True
    if old<=new:return False
    raise ArithmeticError("two directed lower endpoints are not ordered")

def checked_inputs(args,doc):
    actual=dict(Python=platform.python_version(),
                python_flint=importlib.metadata.version("python-flint"),arithmetic_bits=ctx.prec)
    gate(doc,"public repository exact runtime and320-bit directed arithmetic",
         os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
         and actual==RUNTIME)
    doc["runtime"]=actual
    m=read(args.manifest);root=args.repo_root
    paths={k:root/m["input_paths"][k] for k in PINNED}
    files=m["files"];filemap={r["path"]:r for r in files}
    gate(doc,"unchanged complete current small-input closure source manifest parameters and proof",
         m.get("kind")==MANIFEST_KIND and m.get("public_repository")==PUBLIC
         and m.get("parameters")==PARAMETERS and m.get("mathematical_input_sha256")==PINNED
         and m.get("source_sha256")==sha(__file__)
         and len(filemap)==len(files)==6
         and set(m.get("current_text_input_roles",[]))==set(PINNED)|{"new_source"}
         and m.get("legacy_artifact_inputs")==[] and m.get("all_inputs_are_current_small_texts") is True
         and set(filemap)=={m["input_paths"][k] for k in (*PINNED,"new_source")}
         and m["input_paths"]["new_source"]==SOURCE
         and all(sha(paths[k])==v for k,v in PINNED.items())
         and all((root/r["path"]).stat().st_size==r["bytes"] and sha(root/r["path"])==r["sha256"] for r in files))
    doc["input_sha256"]=dict(manifest=sha(args.manifest),**PINNED)
    old=read(paths["gap_process"]);selected=read(paths["selected_process"])
    gate(doc,"the original selected finite-part child and all twelve complete gates are read unchanged",
         selected.get("kind")=="actual_public_first_symbol_parameter_transfer_execution"
         and selected.get("complete") is True and selected.get("mathematical_complete") is True
         and selected.get("transfer_enclosure_complete") is True
         and selected.get("actual_returncode")==0 and selected.get("failure") is None
         and selected.get("mathematical_failure") is None and str(selected.get("run_id"))=="43597209022"
         and selected.get("mathematical_source_sha256")==SELECTED_SOURCE
         and selected.get("native_sha256")==OLD_COEFFICIENT_NATIVE
         and selected.get("manifest_sha256")=="fb578b1d081920a8a75fe58fea0468f5ea58e629f74e4479f9b69f1c63cb2cc5"
         and len(selected.get("mathematical_gates",[]))==12
         and all(g.get("passed") is True for g in selected["mathematical_gates"]))
    gate(doc,"the original exponential arithmetic child and all eleven complete gates are read unchanged",
         old.get("kind")=="actual_public_complete_quadratic_first_phase_arithmetic_execution"
         and old.get("complete") is True and old.get("mathematical_complete") is True
         and old.get("actual_returncode")==0 and old.get("failure") is None and old.get("mathematical_failure") is None
         and str(old.get("run_id"))=="43598755503"
         and old.get("mathematical_source_sha256")==PINNED["gap_source"]
         and old.get("native_sha256")==OLD_GAP_NATIVE
         and old.get("manifest_sha256")=="eb4d3c4b4a57808fce7bac72d6270144322cabb248caa2c5949aeabd751ea180"
         and len(old.get("mathematical_gates",[]))==11
         and all(g.get("passed") is True for g in old["mathematical_gates"]))
    oldsource=paths["gap_source"].read_text()
    gate(doc,"the original exact coefficient-native link and physical scalar recipe are frozen source literals",
         exact_source_constant(oldsource,"INPUT_SHA")==OLD_COEFFICIENT_NATIVE
         and exact_source_constant(oldsource,"A")==A and exact_source_constant(oldsource,"B")==B
         and exact_source_constant(oldsource,"FIRST")==FIRST
         and 'beta = box(original["minus_quarter_of_selected_finite_part_with_no_full_return_identification"])' in oldsource)
    identified=paths["selected_identification"].read_text()
    contract=paths["new_contract"].read_text()
    gate(doc,"the later selected-family identity and new Cayley contract keep the historical candidate wording intact",
         "\\tag{B.11}" in identified and "\\tag{B.12}" in identified and "\\tag{B.13}" in identified
         and "5831714953207175" in identified and "21212218271020390" in identified
         and old.get("actual_full_return_beta_identification_proved") is False
         and selected.get("true_PDE_background_and_full_return_beta_not_claimed") is True
         and "\\tag{CY.32}" in contract and "\\tag{CY.34}" in contract and "\\tag{CY.35}" in contract
         and "\\tag{CY.37}" in contract)
    gate(doc,"only the old complete polynomial and declared all-integer gap are consumed not recomputed",
         old.get("exact_integer_polynomial")==dict(a="10606109135510195",b="-5831714953207175",c="801634672549129",discriminant="5")
         and old.get("exact_uniform_complex_gap_times_abs_n_lower")=="1/512"
         and old.get("exact_scalar_inverse_one_derivative_constant")=="512"
         and old.get("complete_finite_candidates")==1502
         and old.get("candidate_counts_by_fourth_root")=={"0":375,"1":372,"2":382,"3":373})
    srecord=selected["minus_quarter_of_selected_finite_part_with_no_full_return_identification"]
    grecord=old["coefficient_interval"]
    selected_box=interval(srecord);gap_box=interval(grecord)
    gate(doc,"the two original complete scalar records retain positive finite ordered endpoints",
         selected_box.is_finite() and gap_box.is_finite() and selected_box.lower()>0
         and gap_box.lower()>0 and selected_box.upper()<19 and gap_box.upper()<19)
    beta=rational(BETA_LO).union(rational(BETA_HI))
    gate(doc,"the new explicitly wider finite coefficient interval encloses both original directed records",
         beta.lower()<=selected_box.lower() and selected_box.upper()<=beta.upper()
         and beta.lower()<=gap_box.lower() and gap_box.upper()<=beta.upper()
         and beta.lower()>0 and beta.upper()<19)
    gate(doc,"the new analytic tail starts at1024 with a strict exact rational domination",
         FIRST==97 and LAST==1023 and TAIL==1024 and LAST+1==TAIL
         and TAIL*19**3<12*TAIL**2)
    doc["complete_original_scalar_input_conclusion"]={
       "original_selected_run":"43597209022","original_exponential_run":"43598755503",
       "original_selected_coefficient_record_read_verbatim":copy.deepcopy(srecord),
       "original_gap_coefficient_record_read_verbatim":copy.deepcopy(grecord),
       "original_selected_parameter_abs_upper_read_verbatim":copy.deepcopy(selected["actual_selected_R31_parameter_abs_upper"]),
       "original_coefficient_native_sha256":OLD_COEFFICIENT_NATIVE,
       "original_arithmetic_native_sha256":OLD_GAP_NATIVE,
       "original_exact_exponential_gap_read_verbatim":old["exact_uniform_complex_gap_times_abs_n_lower"],
       "original_old_inverse_read_verbatim":old["exact_scalar_inverse_one_derivative_constant"],
       "historical_candidate_flags_retained":True,"later_identification_from_exact_B_primary":True,
       "old_finite_candidates_read_as_metadata_only":1502,
       "new_complete_finite_coefficient_interval":rec(beta),
       "new_finite_rational_endpoints":[str(BETA_LO),str(BETA_HI)],
       "new_finite_interval_is_outward_reconstruction_and_may_be_wider":True,
       "old_infinite_arithmetic_not_extended_to_wider_interval":True,
       "no_binary_native_or_old_producer_read_or_called":True}
    doc["original_successful_small_receipts_read"]=2
    return m,paths,beta

def finite_cayley(doc,beta,checkpoint):
    pi=arb.pi();rho=(arb(A)+arb(5).sqrt())/B
    roots=[acb(1),acb(0,1),acb(-1),acb(0,-1)]
    groups={(sign,k):dict(count=0,bound=None,witness=None) for sign in (-1,1) for k in range(4)}
    audit=[];denmin=None;denominator_count=0
    for j0 in range(FIRST,LAST+1):
        for sign in (-1,1):
            j=sign*j0;x=beta/(2*j)
            denominator=acb(1,-x)
            dl=abs(denominator).lower()
            if not dl.is_finite() or not dl>0:raise ArithmeticError("a Cayley denominator lacks its strict real-mean gap")
            if smaller(dl,denmin):denmin=dl
            denominator_count+=1
            z=acb(0,2*pi*j*rho).exp()*(acb(1,x)/denominator)
            if not z.is_finite():raise ArithmeticError("a complete finite Cayley multiplier is nonfinite")
            for k,root in enumerate(roots):
                difference=z-root;distance=abs(difference)
                lower=(arb(j0)*distance.lower()).lower()
                if not lower.is_finite():raise ArithmeticError("a complete finite weighted-distance lower bound is nonfinite")
                row=dict(index=j,fourth_root_index=k,complete_weighted_distance_lower=rec(lower))
                audit.append(row);g=groups[(sign,k)];g["count"]+=1
                if smaller(lower,g["bound"]):g["bound"]=lower;g["witness"]=row
        if (j0-FIRST+1)%64==0:
            doc["complete_new_finite_progress"]=dict(last_complete_positive_label=j0,
                completed_signed_labels=denominator_count,completed_signed_label_root_pairs=len(audit),
                complete_group_prefix_minima=[dict(sign=sign,fourth_root_index=k,count=g["count"],
                    complete_lower=rec(g["bound"]),witness=g["witness"]) for (sign,k),g in groups.items()],
                prefix_old_arithmetic_recomputed=0)
            checkpoint()
    gate(doc,"all1854 signed Cayley denominators have a positive complete directed separation",
         denominator_count==1854 and denmin is not None and denmin>0)
    gate(doc,"all7416 complete new signed label root intervals have finite directed lower bounds",
         len(audit)==7416 and all(g["bound"] is not None and g["bound"].is_finite() for g in groups.values()))
    keys={(r["index"],r["fourth_root_index"]) for r in audit}
    expected={(sign*j,k) for j in range(FIRST,LAST+1) for sign in (-1,1) for k in range(4)}
    gate(doc,"the new finite cover is exactly927 positive labels both signs and all four roots without duplicate or omission",
         keys==expected and len(keys)==len(audit)==7416)
    global_lower=None;worst=None
    for g in groups.values():
        if smaller(g["bound"],global_lower):global_lower=g["bound"];worst=g["witness"]
    gate(doc,"all eight complete group minima retain927 members and one genuine attained lower-bound witness",
         len(groups)==8 and all(g["count"]==927 and g["witness"] in audit for g in groups.values())
         and worst in audit and global_lower is not None and global_lower.is_finite())
    target=arb(1)/TAIL
    strict=bool(global_lower>0);target_pass=bool(global_lower>target)
    gamma=None;inverse=None
    if strict:
        gamma=target if target_pass else (global_lower/2).lower()
        if not gamma>0 or not gamma<global_lower:
            raise ArithmeticError("the strict finite rational gap could not be selected below the complete lower bound")
        inverse=(1/(4*gamma)).upper()
    gate(doc,"strict positivity and the optional1over1024 target are reported separately from completion",
         strict==(global_lower>0) and target_pass==(global_lower>target)
         and ((not strict and gamma is None and inverse is None)
              or (strict and gamma>0 and gamma<global_lower and gamma<=target and inverse.is_finite())))
    out=dict(new_complete_signed_pair_count=7416,new_complete_signed_label_count=1854,
        complete_finite_coefficient_interval=rec(beta),complete_exact_rotation_enclosure=rec(rho),
        complete_minimum_denominator_lower=rec(denmin),
        complete_finite_weighted_distance_lower=rec(global_lower),complete_worst_finite_pair=worst,
        complete_group_minima=[dict(sign=sign,fourth_root_index=k,count=g["count"],
             complete_weighted_distance_lower=rec(g["bound"]),complete_witness=g["witness"]) for (sign,k),g in groups.items()],
        complete_finite_positive_gap_passed=strict,finite_gap_strictly_above_one_over1024=target_pass,
        complete_selected_same_parameter_scalar_gap_proved=strict,
        complete_uniform_Cayley_gap_times_abs_label=None if gamma is None else rec(gamma),
        complete_physical_one_derivative_inverse_upper=None if inverse is None else rec(inverse),
        finite_scope="entire newly declared wider interval and97<=abs(j)<=1023",
        inherited_tail_scope="original native interval only; actual selected beta belongs to it",
        complete_actual_selected_scope="all abs(j)>=97 and all four roots, conditional on the finite strict verdict",
        original_mean_multiplier_is_exactly_one=True,
        physical_frequency_is_four_times_signed_label=True,
        complete_audit_sha256=sha_bytes(canonical(audit)),complete_audit_pair_count=len(audit),
        no_all_integer_exponential_rerun=True,no_actual_incoming_or_coupled_inverse_claim=True)
    doc["complete_new_finite_Cayley_conclusion"]=out
    doc["complete_new_analytic_tail_conclusion"]=dict(first_abs_label=TAIL,
        original_exponential_gap_times_abs_label="1/512",new_Cayley_gap_times_abs_label="1/1024",
        exact_comparison_left=str(TAIL*19**3),exact_comparison_right=str(12*TAIL**2),
        strict_exact_integer_comparison_passed=True,parameter_scope="same original native interval or actual selected beta",
        wider_finite_interval_does_not_acquire_old_infinite_proof=True,
        exact_mean_difference=0,no_old_scalar_enclosures_recomputed=True)
    doc["complete_Cayley_scalar_gap_proved"]=strict
    doc["new_signed_label_root_pairs_evaluated"]=7416
    doc["new_signed_Cayley_multipliers_evaluated"]=1854
    doc["new_analytic_tail_comparisons"]=1
    doc.pop("complete_new_finite_progress",None)
    checkpoint()
    return audit

def render(doc):
    x=doc.get("complete_new_finite_Cayley_conclusion",{})
    verdict=x.get("complete_finite_positive_gap_passed") is True
    lines=["# Actual finite Cayley scalar arithmetic","",
       "- Public run: "+str(doc.get("run_id"))+"/"+str(doc.get("run_attempt")),
       "- Complete structural gates: "+str(len(doc.get("gates",[]))),
       "- Complete new signed label/root intervals: "+str(doc.get("new_signed_label_root_pairs_evaluated",0)),
       "- Actual finite strict gap: "+("passed" if verdict else "not proved"),
       "- Old scalar, root, ray, KAM and exponential arithmetic recomputed: 0.",""]
    for name in ("complete_finite_weighted_distance_lower","complete_uniform_Cayley_gap_times_abs_label",
                 "complete_physical_one_derivative_inverse_upper"):
        value=x.get(name);lines.append("- "+name+": "+("not supplied" if value is None else value["ball"]))
    lines += ["","The finite intervals use the explicitly declared wider coefficient enclosure. "
       "The inherited infinite tail applies only to the original native interval and the same actual selected coefficient. "
       "The complete mean, all labels below97, physical mean rows, incoming inverse, strong return errors and finite Schur problem remain independent.",
       "No numerical array, archive, Release or new Actions artifact is published.",""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--workdir",type=Path,required=True)
    p.add_argument("--process",type=Path,required=True)
    p.add_argument("--conclusion",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec=320;start=time.monotonic()
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=None,failure=None,gates=[],
       source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),public_repository=PUBLIC,
       run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
       workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
       runtime=RUNTIME,arithmetic_bits=320,mathematical_parameters=PARAMETERS,
       original_successful_small_receipts_read=0,new_signed_label_root_pairs_evaluated=0,
       new_signed_Cayley_multipliers_evaluated=0,new_analytic_tail_comparisons=0,
       old_numerical_enclosures_recomputed=0,old_finite_part_root_ray_or_KAM_calls=0,
       old_exponential_arithmetic_or_candidate_enumeration_calls=0,old_scientific_source_imports=0,
       original_input_bytes_modified=False,new_recomputable_arrays_persisted=False,
       complete_Cayley_scalar_gap_proved=False,full_incoming_inverse_claimed=False,
       full_return_R0_claimed=False,finite_Schur_inverse_claimed=False,actual_PDE_solution_claimed=False,
       final_surface_claimed=False)
    args.workdir.mkdir(parents=True,exist_ok=True)
    def checkpoint():
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-start
        save(args.process,doc)
        print(json.dumps(dict(kind="finite_Cayley_checkpoint",stage=doc.get("stage"),
            complete=doc["complete"],gates=len(doc["gates"]),pairs=doc["new_signed_label_root_pairs_evaluated"]),
            sort_keys=True),flush=True)
    checkpoint();audit=[]
    try:
        doc["stage"]="immutable-small-inputs"
        m,paths,beta=checked_inputs(args,doc);checkpoint()
        doc["stage"]="new-complete-finite-Cayley-arithmetic"
        audit=finite_cayley(doc,beta,checkpoint)
        gate(doc,"all original small input bytes remain unchanged and no old scientific producer was imported",
             all(sha(paths[k])==v for k,v in PINNED.items())
             and all(doc[k]==0 for k in ("old_numerical_enclosures_recomputed","old_finite_part_root_ray_or_KAM_calls",
                      "old_exponential_arithmetic_or_candidate_enumeration_calls","old_scientific_source_imports")))
        gate(doc,"the complete new temporary audit has exactly7416 records and the small conclusion preserves its full hash",
             len(audit)==7416
             and sha_bytes(canonical(audit))==doc["complete_new_finite_Cayley_conclusion"]["complete_audit_sha256"])
        gate(doc,"all eighteen structural gates complete independently of the finite strict-margin verdict",
             len(doc["gates"])==17 and all(g["passed"] for g in doc["gates"])
             and doc["new_signed_Cayley_multipliers_evaluated"]==1854
             and doc["new_signed_label_root_pairs_evaluated"]==7416)
        doc.update(complete=True,proved=True,actual_returncode=0,stage="complete-new-finite-Cayley-arithmetic")
    except Exception as error:
        doc.update(actual_returncode=1,failure=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc()))
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-start
    native=dict(complete_small_conclusion=doc,new_finite_audit=audit,numerical_arrays_are_temporary_only=True)
    raw=canonical(native);args.out.parent.mkdir(parents=True,exist_ok=True)
    tmp=args.out.with_name(args.out.name+".partial");tmp.write_bytes(gzip.compress(raw,mtime=0));tmp.replace(args.out)
    doc["temporary_native_sha256"]=sha(args.out);doc["temporary_native_bytes"]=args.out.stat().st_size
    # Always preserve complete science before any bounded presentation or publication check.
    save(args.process,doc)
    args.conclusion.parent.mkdir(parents=True,exist_ok=True);args.conclusion.write_text(render(doc))
    print(json.dumps(dict(kind="finite_Cayley_complete_small_science_identity",
        bytes=len(canonical(doc)),sha256=sha_bytes(canonical(doc)),complete=doc["complete"],
        strict_gap_proved=doc["complete_Cayley_scalar_gap_proved"],actual_returncode=doc["actual_returncode"]),
        sort_keys=True),flush=True)
    if len(canonical(doc))>45000:
        raise RuntimeError("complete new science is already saved but exceeds the bounded small-presentation budget")
    if not doc["complete"]:raise SystemExit(1)

if __name__=="__main__":main()
