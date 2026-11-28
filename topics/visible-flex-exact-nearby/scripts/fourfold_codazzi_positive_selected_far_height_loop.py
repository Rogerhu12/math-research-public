"""Close the true selected far-height function after the actual 193-row physical inverse."""
from fractions import Fraction
from hashlib import sha256
import json


def require(ok,message):
    if not ok:
        raise ValueError(message)


def close(*,engine,model,admitted,gate,boundary,particular,npg,fhc_raw,fhc_spec,oa_raw,ohr_raw,
          state_radius,inputs,column,explicit_cut_L2,external_height,cut_entry,emit):
    """Use original signed Newton/nu and every supplied independent port in the same solve.

    Nonzero state radius additionally requires two directed actual cut bounds in the units
    of W.31/33. They must be bound to the same state by the calling scientific owner.
    """
    api=engine.api
    def Q(s):
        f=Fraction(s)
        return api.rational(f.numerator,f.denominator)
    def save(name,value,bound="upper"):
        point=value.upper() if bound=="upper" else value.lower()
        out=emit(column+"_"+name,point,bound)
        require(out.is_finite() and (bool(out>=point) if bound=="upper" else bool(out<=point)),
                "complete directed selected-height endpoint "+name)
        return out
    fhc=json.loads(fhc_raw)
    require(len(fhc_raw)==fhc_spec["bytes"] and sha256(fhc_raw).hexdigest()==fhc_spec["sha256"]
            and fhc["proved"] and all(x is True for x in fhc["checks"].values())
            and fhc["selected_centre_actual_value_in_SCAP_3"]
            and fhc["true_cut_curvature_differential_raw_even"]==".11"
            and fhc["returned_selected_height_negative_ordinary_price"]=="2^-31223182"
            and fhc["whole_inputs"]["WHN_actual"]=="3d280913d53b56d90f1079acf91f0a9e7f5e895abaadcf2a6a8ebfdb530ecc0f"
            and sha256(ohr_raw).hexdigest()==fhc["whole_inputs"]["OHR"],
            "whole actual height, WHN and OHR receipts")
    require(column in ("Newton","nu") and gate["body_gate_passed"] and gate["physical_gate_passed"]
            and gate["private_model_token"] is model["private_model_token"] is boundary["private_model_token"]
            and particular["private_model_token"] is model["private_model_token"],
            "the actual successful current physical inverse and the actual signed source")
    rho=Fraction(state_radius)
    require(0<=rho<=Fraction(gate["radius"]),"same true nonlinear state")
    require(bool(inputs["height_second_Hsixth"]==0) and explicit_cut_L2.is_finite()
            and external_height.is_finite() and api.lower(explicit_cut_L2)>=0 and api.lower(external_height)>=0,
            "independent far height is replaced by its one physical graph equation")
    if rho:
        require(set(cut_entry)=={"actual_even_correction_H1","actual_even_minus_base_H8193"}
                and all(v.is_finite() and api.lower(v)>=0 for v in cut_entry.values())
                and bool(cut_entry["actual_even_correction_H1"]<=Q("1.96875e-11"))
                and bool(cut_entry["actual_even_minus_base_H8193"]<=Q(2)**393000),
                "true admitted physical gamma at the same nonlinear cut, W.31 and W.33")
    else:
        require(cut_entry is None,"actual selected centre uses its original full W.1")
    # Unit-height response at the same fixed base, for every Fourier direction.
    hu=Q(".004")
    S0=Q("1.453")*hu
    C0=Q("3.656366")*hu
    ah=gate["high_to_right97"]
    d0=api.sqrt(Q(".0013")**2+Q(".000822")**2)+ah*Q("5/388")*S0
    seed={n:gate["high_raw"][n]*C0+gate["initial_boundary"]["right"][n]*d0 for n in ("body","outer")}
    b0=seed["body"]/gate["internal_margin"]
    o0=seed["outer"]+gate["kappa"]["outer"]*b0
    r,a=(row[0]*ah*Q(".154")*b0+row[1]*o0 for row in gate["physical_inverse"])
    body=save("unit_selected_graph_complete_body",b0+gate["closed_boundary"]["right"]["body"]*r+
              gate["closed_outer_poisson"]["body"]*a)
    outer=save("unit_selected_graph_complete_terminal",a)
    cut=save("unit_selected_graph_complete_cut",4453*body+Q("2.48")*outer+Q(".026"))
    omega=Q(10**9)*Q(2)**(-31223222)
    loop=save("complete_selected_height_loop",Q(".11")*omega*cut)
    margin=save("complete_selected_height_margin",api.one-loop,"lower")
    result=dict(complete_selected_height_loop_passed=bool(margin>api.zero),full_loop=loop,margin=margin,
                physical_input_value_in_SCAP_3=True,other_global_port_matching_proved=False)
    if not result["complete_selected_height_loop_passed"]:
        return result
    f=dict(inputs)
    # Original analytic OHR Newton centred at zero height; the selected real f is bounded
    # by the actual SRG norm. Off-centre Newton needs the supplied actual current residual.
    if column=="Newton" and not rho:
        fheight=Q(2)**(-49999998)
        f["Robin_extra_Hsixth"]+=Q(".000134")*fheight
        f["mean_extra"]+=Q(".00001675")*fheight
    def receive(tag,data):
        return npg.positive_response_and_negative_readout(engine=engine,model=model,admitted=admitted,
            gate=gate,boundary=boundary,particular=particular,original_high_receipt=ohr_raw,
            oa_raw=oa_raw,inputs=data,column=column,state_radius=state_radius,
            emit=lambda n,v,d:emit(tag+"_"+n,v,d))
    open_body=receive("open_height",f)
    # The whole base QN strong table, including every independent physical source row.
    B=open_body["actual_weighted_body"]
    a=open_body["actual_weighted_low_outer"]
    if column=="nu":
        H=Q("1.254870e-9")+9*Q(rho)
        R,M=Q("1.23e-11"),Q("9.1e-16")
        low=Q("2.9476e-5")+15500*Q(rho)
        known_cut=Q(".601229")
    else:
        low,known_cut=Q("7.051e-8"),api.zero
        if rho:
            H=f["Newton_current_high_ordinary_Hthird"]
            R,M=f["Newton_current_Robin_Hsixth"],f["Newton_current_mean_residual"]
            low+=f["Newton_current_minus_original_low_ordinary"]
        else:
            H,R=Q("1.17560e-19"),Q("1e-14")
            oa=json.loads(oa_raw)
            M=api.old_interval(oa["complete_new_scalar_records"]["complete_selected_independent_physical_mean_residual_upper"]).upper()
    ext=f["body_frame_jumps"]+23*(R+f["Robin_extra_Hsixth"])+28*(M+f["mean_extra"])
    ports=[f["root_stable"],f["collar_Hthird"],f["body_Hthird"],ext,f["collar_frame_jumps"],
           f["cut_stable_jump"],f["cut_unstable_jump"]]
    def table(coefficients):
        return sum((Q(c)*v for c,v in zip(coefficients,ports)),api.zero)
    raw=table(["3.656366",".032909",".461223","3.656366","3.656366","3.651469",".010252"])+Q(".5")*H
    frame=table(["1.452083",".013070",".183170","1.452083","1.452083","1.450147",".001938"])+Q(".2")*H
    open_cut=save("complete_zero_height_cut",4453*B+Q("2.48")*a+known_cut+
                  Q(".332")*raw+Q("3.6")*frame+Q(".005")*(low+f["low_ordinary_extra"])+f["positive_low_raw_jump_sum"])
    F=save("whole_selected_far_height",(external_height+omega*(explicit_cut_L2+Q(".11")*open_cut))/margin)
    f["height_second_Hsixth"]=F
    result.update(actual_selected_far_height=F,complete_zero_height_cut=open_cut,
                  received_selected_positive_solution=receive("closed_height",f))
    return result
