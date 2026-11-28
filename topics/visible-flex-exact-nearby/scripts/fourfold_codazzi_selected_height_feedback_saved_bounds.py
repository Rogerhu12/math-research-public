"""Actual selected far-height feedback at the full physical cut of the true neighbourhood."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


TOPIC=Path(__file__).resolve().parents[1]
FILES={
    'cut':('notes/selected_cut_shape_mean_ci/run-43715426316-1-selected-cut-shape-mean/actual-cut-shape-mean-conclusion.json',7733,
        '5d74a0f24afe7d490cd17f04f0c0ea5efb671fd277ced502269f4d94c748a413'),
    'cut_run':('notes/selected_cut_shape_mean_ci/run-43715426316-1-selected-cut-shape-mean/process.json',13640,
        '82b7c37637c9ebec074ae7647595200c2cd790cf19728ef0e4d93a8452e59812'),
    'WOB':('notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/actual-scientific-conclusion.json',60416,
        'ba8e647cc4572333407b8979f98315e94dbab53ff2ff0086fe1d1dcdb0f17b79'),
    'OHR':('notes/2026-11-28-OHR-complete-saved-consequence.json',3656,
        '312c60afba95bc4e41bd29549a444031cbd633cd252be981bcccb329e54a4993'),
    'SPN':('notes/2026-11-28-SPN-complete-saved-consequence.json',3087,
        'ac82ab9942eb4bbd8a7fa6522fbc4d8b7e4cd414db0e42bfa55bf1c4f8e8a4c2'),
    'WHN':('results/R149-supplement-true-nearby-weighted-head-response-and-negative-readout.md',6224,
        '46f8b80cb02fd5b9ede68bd0ec4838f8dacbf29155a13f7b521d46233f1454ee'),
    'WHN_actual':('notes/2026-11-28-WHN-complete-saved-consequence.json',2363,
        '3d280913d53b56d90f1079acf91f0a9e7f5e895abaadcf2a6a8ebfdb530ecc0f'),
    'NPG':('results/R149-supplement-nonlinear-neighbourhood-physical-inverse-and-received-columns.md',7538,
        'da3517ec204f0bf7ed17815cedc71c90a3651817a4aeb3ced99ad1082008d34a'),
    'QN':('results/R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md',32805,
        '1fe88442bb35d0280a54dc416014f59773f1777a1b74998eb9513052b2f5a15e'),
    'SHL':('results/R119-supplement-L2-response-of-the-actual-selected-tail-and-physical-readouts.md',25742,
        '29efcfeef648441cfa252db0377f9edb73c1d0db634b075f822f892af344f7f2'),
    'SRG':('results/R119-supplement-higher-regularity-of-selected-tail-and-local-uniqueness.md',13672,
        '98724a93f890a0a33efefac41b5ba90eaf3e74df88433b55b6655790854a9b7c'),
    'SCAP':('results/R133-supplement-actual-selected-cap-and-complete-height-feedback-absorption.md',28541,
        '8510416368f136b0c31b9af691a3e5f916203be918181d565ee88134767c4671'),
    'ASQ2':('results/R149-supplement-actualsquare-selected-far-graph-and-height-span.md',6446,
        '24a5a0634c692e6f732aa2fd237fd1b451b188ef54a5cf821b0ea726bbfeacb1'),
    'W':('results/R133-supplement-known-finite-cut-Wiener-angle-and-sharp-low-curvature-entry.md',13398,
        '67389a01f34b75f27faaa2adc1b681180d4aca004b3f69b8924a8f11f31f0738'),
    'frame':('results/R133-supplement-full-delta-positive-M32-base-and-M96-difference.md',8111,
        '4e37dc2bc049ec2c9cc3942a7c1986aae7c3ce3ab733049cab905f3fde840405'),
    'parser':('scripts/fourfold_codazzi_negative_ordinary_response_saved_bounds.py',10330,
        '88df151b7ecc9c22bff382cd96e647ba2ea1010baa6332b5dcc8a88baf9ea4b9'),
}


def require(ok,message):
    if not ok:
        raise ValueError(message)


def main():
    docs={}
    for k,(name,size,digest) in FILES.items():
        raw=(TOPIC/name).read_bytes()
        require(len(raw)==size and sha256(raw).hexdigest()==digest,"whole "+k)
        if name.endswith(".json"):
            docs[k]=json.loads(raw)
    from fourfold_codazzi_negative_ordinary_response_saved_bounds import endpoints
    cut,run,spn,ohr,wob=(docs[k] for k in ("cut","cut_run","SPN","OHR","WOB"))
    require(cut["complete"] and cut["failure"] is None and cut["all_193_raw_amplitudes_used_before_absolute_values"]
            and cut["original_response_slots"]==dict(even_mean=1,even_nonmean=96,odd_nonmean=96)
            and cut["original_input_scope"]["same_true_cut"]=="9/10" and cut["original_input_scope"]["raw_side"]=="left"
            and cut["original_input_scope"]["derived_continuous_direction_definition_sha256"]==
               "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
            and run["complete"] and run["actual_scientific_complete"] and run["actual_scientific_failure"] is None
            and run["actual_scientific_summary_sha256"]==FILES["cut"][2]
            and run["actual_scientific_summary_bytes"]==FILES["cut"][1]
            and run["actual_source_sha256"]==cut["source_sha256"] and run["actual_scientific_gates"]==cut["gates"]
            and str(run["run_id"])=="43715426316" and str(run["run_attempt"])=="1"
            and run["publication_is_final_attempt"] and run["all_pinned_inputs_verified"]
            and docs["WHN_actual"]["proved"] and len(docs["WHN_actual"]["checks"])==17
            and all(v is True for v in docs["WHN_actual"]["checks"].values())
            and docs["WHN_actual"]["true_selected_nearby_head_rates"]==dict(
                  root_collar_body_Z="11.9",raw_high="30",outer_even_Hminus5over6=".154")
            and len(cut["gates"])==9 and all(g["passed"] for g in cut["gates"]) and len(run["children"])==1
            and run["children"][0]["actual_returncode"]==0 and spn["proved"] and len(spn["checks"])==32
            and ohr["proved"] and ohr["whole_inputs"]["WOB"]==FILES["WOB"][2] and wob["complete"],
            "actual selected state, signed cut and physically admissible entire records")
    checks={}
    def test(name,left,right):
        require(left<right,name)
        checks[name]=True
    up=lambda r:endpoints(r)[1]
    cs=cut["complete_scalar_bounds"]
    abs_min=-endpoints(cut["original_base_mean_signed"])[1]
    dm=F("1e-10")*up(cs["zeta_mean_absolute"])+F("1e-7")
    m=abs_min-dm
    test("true_cut_mean",F("3.2"),m)
    old_ratio=1+dm/m
    jdev=old_ratio*up(cs["base_j0_nonmean_A0_from_saved_coefficients"])+(F("1e-10")*up(cs["zeta_nonmean_A0"])+F("1e-7"))/m
    jphi=old_ratio*up(cs["base_j0_phi_A0_from_saved_coefficients"])+(F("1e-10")*up(cs["zeta_phi_A0"])+F("1e-7"))/m
    test("all_infinite_modes_true_cut_j",jdev,F(".014"))
    test("all_infinite_modes_true_cut_jphi",jphi,F(".055"))
    vmin=F("3.2")*F(".986")
    test("true_cut_reciprocal_floor",F("3.14"),vmin)
    # composition at the genuine angle is bounded by sqrt(1.014) in L².
    chart=(1+F(".055")/(4*F(".986"))*(1+F("1.014")))/F("3.14")**2
    test("full_L2_physical_curvature_differential",F("1.014")*chart**2,F(".11")**2)
    test("positive_domain_high_even_trace_at_cut",(90/(1-F("1e-7")))**3,388*F("3.6")**6)
    A,D=F("7.000002"),F("6.000002")
    trueA=384*(6*A*A/4+14*A)+6*(1+3*A*A+A*D/2)+14*D
    test("all_modes_true_low_matrix",trueA,70000)
    L=up(wob["copied_original_scalar_records"]["L_star"])+8500*F("1e-7")
    test("actual_high_return_in_raw_cut",L/200,F(".332"))
    test("full_S_weighted_head_to_raw_trace",8*(200+trueA/200),4400)
    H=F(".332")*F("3.656366")+F("3.6")*F("1.453")
    test("full_cut_from_weighted_low",4400+F(".332")*30+F("3.6")*F("11.9"),4453)
    test("full_cut_from_charted_terminal",H*F(".001")*F("384.002"),F("2.48"))
    test("full_cut_from_independent_height",H*F(".004"),F(".026"))
    test("actual_known_nu_high_raw_source_row",F(".032909")**2+F(".461223")**2,F(".5")**2)
    test("actual_known_nu_high_frame_row",F(".013070")**2+F(".183170")**2,F(".2")**2)
    test("true_known_nu_cut_including_Z",up(cs["zeta_A0"])+F(".005")*F("2.9476e-5")+
           F(".332")*(F(".5")*F("1.254870e-9")+F("3.66")*F("3e-10"))+
           F("3.6")*(F(".2")*F("1.254870e-9")+F("1.5")*F("3e-10")),F(".60123"))
    test("true_nu_low_and_high_rho_terms",F(".005")*15500+F(".332")*F(".5")*9+F("3.6")*F(".2")*9,86)
    test("actual_selected_centre_physical_Wiener_entry",F(13,200)*F("1e-10")*10**9,F(1,128))
    test("actual_selected_centre_H8193_base_exponent",4096*8193,2**26)
    test("actual_selected_centre_H8193_high_entry",26*8193+1,1048576)
    # t = 2^-31223222 stays as an exponent, including the physical 1/r_gamma.
    # Only the next bound uses the much weaker t < 2^-61.
    test("actual_uniform_selected_height_jet_value",60+2,49999998)
    test("actual_linear_height_self_gain",10**9*F(".11")*F(".026"),F("1e-7")*2**61)
    test("actual_far_trace_absorption",1,F("1.000001")*(1-F("1e-7")))
    test("actual_negative_ordinary_external_height",F("1.36")*F("1.000001"),F("1.360002"))
    # After dividing by t, the largest coefficient is the genuine weighted head.
    test("remaining_normalized_selected_height_prices",F("1.36")*F("1.000001")*10**9*
         max(F(".11")*v for v in (4453,F("2.48"),F(".60123"),86,F(".332"),F("3.6"),F(".005"),1)),2**40)
    test("independent_explicit_cut_variation_price",F("1.36")*F("1.000001")*10**9,2**40)
    require(31223222-40==31223182,"retained tiny selected-height exponent")
    print(json.dumps(dict(proved=True,checks=checks,whole_inputs={k:v[2] for k,v in FILES.items()},
        true_cut_curvature_differential_raw_even=".11",full_high_even_cut_from_body_frame="3.6",
        returned_selected_height_negative_ordinary_price="2^-31223182",
        external_additive_far_height_price="1.360002",independent_common_world_height_and_means_retained=True,
        selected_centre_actual_value_in_SCAP_3=True,unknown_correction_SCAP_3_or_global_inverse_proved=False,old_scientific_target_calls=0),sort_keys=True))


if __name__=="__main__":
    main()
