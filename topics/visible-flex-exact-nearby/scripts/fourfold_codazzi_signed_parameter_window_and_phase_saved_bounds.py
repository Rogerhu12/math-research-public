"""Exact new parameter-transfer and whole real phase comparisons from verified original results."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

TOPIC=Path(__file__).resolve().parents[1]
FILES={
    "WSS_manifest":('notes/2026-11-28-whole-selected-signed-sources-inputs.json',7995,"dc6422b48e17064f7493510aa289a6cc9111887c95d7cb38093241663b5c4bb9"),
    'NHT':('results/R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md',8003,
        '6b4202ede35ed025bb52cd5abcb5a60089353436866a6e32dfac54f0ee5140d9'),
    'NBE':('results/R149-supplement-nonlinear-background-negative-ordinary-response.md',7654,
        '35b2075696ece5529e649bc373d81af4c6551cd1d76dea0aad57e5558649a2d0'),
    'NRO':('results/R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md',8294,
        'fb1e034f04c79c4a893cdd1407b7a590959f5383dddb1ea786abb34366dfa91d'),
    'tail':('notes/known_high_Z_tail_source_ci/run-43628921664-1-complete-known-high-Z-tail-source/evidence/complete-known-high-Z-tail-source-summary.json',14387,
        '74e7b40d0eb4c79bf511a501467e73d80116d46990d1ab8e5b43f66f4fcd1b35'),
    'tail_receipt':('notes/known_high_Z_tail_receipt_ci/run-43630093667-1-known-high-math-success-receipt/evidence/known-high-original-success-receipt.json',12445,
        'cd7aa5f5c21509c629f8508bef21af4254e05716e2868e1804bce60e1ee583fa'),
    'helpers':('scripts/fourfold_codazzi_negative_ordinary_response_saved_bounds.py',10330,
        '88df151b7ecc9c22bff382cd96e647ba2ea1010baa6332b5dcc8a88baf9ea4b9'),
    'K':('notes/selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json',40659,
        '6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071'),
    'outer':('notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-regular-Hs-outer-summary.json',23649,
        '769204e822787216c5aebd2cde30e73759fcf66d3bb1d6d1d76d2381bad6cae6'),
    'NA':('notes/positive_Newton_ordinary_source_ci/run-44765046846-1/positive-Newton-ordinary-source.json',35749,
        '223461e2bf67ee35054b15a713928c5fa90bbf315f442c9f394a8e3403a20166'),
    'NA_run':('notes/positive_Newton_ordinary_source_ci/run-44765046846-1/execution.json',18244,
        'fb7782433762b9e1d4e69c78f319b7b5b15cfae827311cf600654e655bf89198'),
    'NA_manifest':('notes/2026-11-20-R141-positive-Newton-ordinary-source-inputs.json',17776,
        '8866c54756973ef453f18eaa9e1aae22f8a7ac248fb2a823c7a7ed8207200315'),
    'NW':('notes/negative_nu_waist_ci/run-45781137624-1/actual-negative-nu-waist.json',15210,
        '1a06d01060a63eac98aeaa330f130a8ee766ab5ac878634e637f9cea30e1cb70'),
    'NW_run':('notes/negative_nu_waist_ci/run-45781137624-1/execution.json',13970,
        'eeb4ed157912e742e8d773ca32b04570296973b924f4a92b1a4ec153c30efe2b'),
    'NW_manifest':('notes/2026-11-26-negative-nu-waist-inputs.json',11815,
        'b697e8665801a6e4d5120ca312d72a339cc28a2516d6dabd255f56ee79690f2d'),
    'WSS':('notes/whole_selected_signed_sources_ci/run-46136409179-1/whole-selected-signed-source.json',15263,
        'd3135d3cf9855b2312a922c9bfd9162da3debd844855eea22668ba0d8318b16e'),
    'WSS_run':('notes/whole_selected_signed_sources_ci/run-46136409179-1/execution.json',24536,
        'fb1e7e7a828cc8a8086ecd9eb50d96bc895b194a58017271aad210cf986a563a'),
    'WHN':('notes/2026-11-28-WHN-complete-saved-consequence.json',2363,
        '3d280913d53b56d90f1079acf91f0a9e7f5e895abaadcf2a6a8ebfdb530ecc0f'),
    'SPN':('notes/2026-11-28-SPN-complete-saved-consequence.json',3087,
        'ac82ab9942eb4bbd8a7fa6522fbc4d8b7e4cd414db0e42bfa55bf1c4f8e8a4c2'),
    'FHC':('notes/2026-11-28-FHC-complete-saved-consequence.json',2748,
        '6534bd6fb43c492db16fe563f9c1c219b30b913f58d6a3c15ee011754f3e372a'),
    'NPG':('notes/2026-11-28-NPG-root-new-exact-fees.json',552,
        '53f584018bb507c5dd5c34a92c5db7a58c46ff14d4b10d82aa353732261493ee'),
    'ASQ24':('results/R149-supplement-physical-Sobolev-rotation-selection-and-normalized-smooth-family.md',16539,
        '26669f292a88613d3a6de3330c337436571c4c8606590ec5418e11f4075d2c17'),
    'NP':('results/R145-selected-nu-proposal-positive-source-and-outer-rows.md',10867,
        '8fc5bf6263c30f327b4a146d309d093054dd1d97f7bc874cbae7a26502d6876c'),
    'N':('results/R141-supplement-selected-member-and-complete-positive-Newton-source.md',14250,
        'f37eb7ef3f44cac765358ff2ee52afba6237cd37b23d77fabf553247f31ea2f2'),
    'PPR':('results/R149-supplement-parameter-wide-signed-source-and-physical-phase-readout.md',9796,
        '71d65602ea4b4f5fbc4b55e1b1085b4aca809f2f41dfe30eb19091baa74da308'),
}


def require(ok,cause):
    if not ok:
        raise ValueError(cause)


def canon(v):
    return (json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def admit():
    docs={}
    for k,(path,size,hexsum) in FILES.items():
        raw=(TOPIC/path).read_bytes()
        require((len(raw),sha256(raw).hexdigest())==(size,hexsum),"whole "+k)
        if path.endswith(".json"):
            docs[k]=json.loads(raw)
    for prefix,run in (("NA","44765046846"),("NW","45781137624")):
        a,m,e=[docs[prefix+s] for s in ("","_manifest","_run")]
        i=a.get("identity",a)
        require(i["run_id"]==e["run_id"]==run and i["run_attempt"]==e["run_attempt"]=="1"
            and a["complete"] and a["proved"] and a["failure"] is None and e["complete"]
            and e["original_scientific_complete"] and e["failure"] is None and a["actual_returncode"]==e["actual_child_returncode"]==0
            and e["manifest_sha256"]==FILES[prefix+"_manifest"][2]
            and e["current_input_receipts"]==m["files"] and e["old_completed_targets_recomputed"]==0,
            "complete actual "+prefix+" with its original scientific and native closure")
        path,n,h=FILES[prefix]
        require(e["scientific_files"]==[dict(path="topics/visible-flex-exact-nearby/"+path,bytes=n,sha256=h)],"actual "+prefix+" file bound by execution")
        old={x["role"]:x for x in m["files"]}
        if prefix=="NA":
            require(a["source_sha256"]==old["science"]["sha256"] and a["input_manifest_sha256"]==e["manifest_sha256"]
                and a["current_input_receipts"]==m["files"] and len(a["gates"])==18 and all(v["passed"] for v in a["gates"])
                and a["saved_record_count"]==7 and a["actual_scientific_checkout_commit"]==e["actual_scientific_checkout"],
                "original N.14 signed-polynomial positive majorant")
        else:
            require(i["source_sha256"]==old["science"]["sha256"] and i["manifest_sha256"]==e["manifest_sha256"]
                and i["actual_checkout_commit"]==e["actual_scientific_checkout"] and a["saved_record_count"]==4
                and a["whole_completed_inputs"]["D_execution"]["file"]["sha256"]==FILES["K"][2],
                "original readback of the selected member, d-envelope, complete state and source radii")
    d=docs["K"]
    native=d["actual_scientific_receipt"]
    raw=canon(native)
    require(d["run_id"]=="43713242980" and d["actual_returncode"]==native["actual_returncode"]==0
        and d["complete"] and native["complete"] and d["actual_failure"] is None
        and len(native["gates"])==12 and all(x["passed"] for x in native["gates"])
        and d["output_hashes"][0]==dict(file="actual-scalar-conclusion.json",bytes=len(raw),sha256=sha256(raw).hexdigest()),
        "the entire original D physical interval majorant and native source")
    nw,na=docs["NW"],docs["NA"]
    require(nw["parameters"]["continuous_direction_definition_sha256"]==na["parameters"]["direction_definition"]
        ==native["derived_continuous_response_definition_sha256"]==docs["tail"]["exact_continuous_direction_definition_sha256"]
        and nw["parameters"]["continuous_centre_definition_sha256"]==na["parameters"]["centre_definition"]
        ==native["derived_continuous_centre_definition_sha256"],"one true repaired pair")
    s=docs["SPN"]
    require(s["proved"] and all(s["checks"].values()) and all(s["whole_inputs"][k]==FILES[k][2]
        for k in ("K","outer","NHT","NBE","NRO","tail","tail_receipt","helpers")) and docs["WHN"]["proved"]
        and docs["FHC"]["proved"] and docs["FHC"]["whole_inputs"]["WHN_actual"]==FILES["WHN"][2]
        and docs["FHC"]["whole_inputs"]["SPN"]==FILES["SPN"][2]
        and docs["NPG"]["proved"] and docs["NPG"]["whole_proof_sha256"]==docs["FHC"]["whole_inputs"]["NPG"],
        "complete physical response domain, source variation and selected far-graph receipts")
    require(docs["tail"]["complete"] and len(docs["tail"]["gates"])==8 and all(x["passed"] for x in docs["tail"]["gates"])
        and docs["tail_receipt"]["original_complete_known_high_bounds"]==docs["tail"]["complete_known_high_bounds"],
        "actual undiminished original high-source majorant")
    w,e=docs["WSS"],docs["WSS_run"]
    require(w["complete"] and w["proved"] and w["failure"] is None and e["complete"] and e["original_scientific_complete"]
        and e["failure"] is None and e["original_scientific_failure"] is None
        and e["run_id"]=="46136409179" and e["run_attempt"]=="1"
        and e["manifest_sha256"]==FILES["WSS_manifest"][2] and e["completed_natural_targets"]==w["completed_targets"]
        and w["actual_returncode"]==e["actual_child_returncode"]==0 and len(w["completed_targets"])==2
        and e["scientific_files"]==[dict(path="topics/visible-flex-exact-nearby/"+FILES["WSS"][0],bytes=FILES["WSS"][1],sha256=FILES["WSS"][2])]
        and w["new_records"]["whole_selected_signed_577_by_2_source_with_true_compact_metric"]["physical_source_rows"]==577,
        "actual whole signed Newton and parameter columns")
    return docs


def comparisons(docs):
    from fourfold_codazzi_negative_ordinary_response_saved_bounds import endpoints,exponential_upper
    def upper(v):
        return endpoints(v)[1]
    check={}
    def lt(k,x,y):
        require(x<y,k)
        check[k]=True
    d,K,rho=F("1e-10"),F("6e-12"),F("1e-7")
    lo=F(docs["NW"]["selected_member_identity"]["absolute_delta_upper"])
    lt("actual_phase_segment_inside_original_metric_family",lo+K,d)
    core=upper(docs["K"]["actual_scientific_receipt"]["complete_scalar_fee_conclusions"]["whole_core"]["ordinary_L2_bounds"]["complete_additional_response_source"])
    cap=upper(docs["NA"]["complete_new_scalar_records"]["new_outer_tail_selected_nonlinear_remainder_L2_upper"])
    cubic=F("1.768")*6*19**2*(F(83,4)+19)
    lt("full_signed_cubic_positive_interval",cubic,153000)
    lt("symmetric_actual_core_coefficient",core/d,43250)
    lt("same_signed_positive_cap_quadratic",2*cap/d**2,176000)
    lt("full_disjoint_parameter_transfer_with_cubic_fee",(core/d)**2+(2*cap/d**2)**2,(F(182000)-6*d*cubic)**2)
    lt("genuine_extra_signed_source_on_entire_phase_window",182000*K,F("1.093e-6"))
    tail=docs["tail"]["complete_known_high_bounds"]["full_body"]
    t,base=upper(tail["new_tail_only_L2_radial"]),upper(tail["selected_known_high_H_one_third_L2_radial"])
    D1=12*d+(1+12*d)*(104*d+1872*d*d)+12*(d+52*d*d+624*d**3)
    lt("high_parameter_source_on_every_true_metric_member",base+F("10.484")*D1*t,F("1.254870e-9"))
    c=F(2333968743003,10**13)
    U,A,W,H=F("8.22001"),F("25.944"),F("7.269"),F("1.254870e-9")
    old=docs["NW"]["copied_prior_scalar_records"]
    force=upper(old["source_zero_same_fixed_negative_full"])+upper(old["complete_selected_difference_at_radius_d"])
    lt("whole_ordinary_negative_source_no_selected_parameter_shortcut",force,F("1.38e-6"))
    lt("strict_and_root_energy_on_whole_parameter_window",
       F("1.38e-6")**2*((c*U)**2/2+A*A*W*W/200),(F("1.86e-5")-A*F(".071")*H)**2)
    lt("true_mixed_root_forcing_length",F(1,200),F(".071")**2)
    lt("separate_negative_root_extra_gain",A*A/200,4)
    lt("separate_negative_strict_extra_gain",c*U,2)
    w=F("9e-13"); E=exponential_upper(70000*w)
    lt("positive_sliver_complete_low_root_gain",w*E*E,(F("25.95")-A)**2)
    lt("positive_sliver_full_high_frame_gain",w*(E*201*w+3)**2,F("2.86e-6")**2)
    lt("positive_sliver_raw_jump",w*E*E,F("9.54e-7")**2)
    lt("positive_sliver_extra_ordinary",w*E,F("9.1e-13"))
    lt("all_known_source_cost_on_whole_sliver",F("1.86e-5")+w*E*(F("2.9476e-5")+15500*rho+182000*K),F("1.87e-5"))
    lt("genuine_sufficient_half_percent_readout_with_free_ports",F("25.95")*F(".000169")+F("2.86e-6")+F("1.87e-5")+5100*rho+F(".00008"),F(".005"))
    lt("strong_path_ordinary_value_radius",F(".239")*rho*rho,F("5e-8")**2)
    E=F("5e-8")
    loss=318*rho+1920*E+57*K+33*K+(155*rho+6*E+3*K)*11+3300*(25*K+F("5.4")*E)
    lt("pointwise_true_twist_wider_ordinary_value",F(".047")*(1+3300*K),F(".049")-loss)
    lt("signed_matched_true_regular_twist",F(".020"),F(".047")-F("5.38")*F(".005"))
    lt("balanced_signed_rotation_certificate",F("1.1999e-13"),F(".020")*K)
    lt("uniform_true_physical_endpoint_core",F("9e-10")+129**3*F("3.861e-18")+385**3*d*(F("2.31e-11")+F("1.35e-10")),F("1e-9"))
    lt("full_selected_affine_cut_value",F(".065")*d/F("1e-9"),F(1,128))
    return dict(proved=True,checks=check,whole_inputs={k:v[2] for k,v in FILES.items()},
        whole_parameter_window="6e-12",uniform_signed_positive_low_source_rate=182000,
        uniform_nu_strong_high_ordinary="1.254870e-9+9rho",true_root_ordinary_gate=".005",
        actual_signed_rotation_test_half_width="1.2e-13",old_scientific_targets_recomputed=0,
        actual_matched_regular_path_or_global_ports_proved=False,actual_signed_rotation_residual_paid=False)


if __name__=="__main__":
    print(json.dumps(comparisons(admit()),sort_keys=True))
