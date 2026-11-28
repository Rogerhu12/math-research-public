"""The actual selected neighbourhood, with its own complete low/high/physical sufficient tests."""
from fractions import Fraction as F
from hashlib import sha256
import json


def require(ok,message):
    if not ok:
        raise ValueError(message)


def fees():
    """Exact new multiplier bounds. Return the exact constants for the directed consumer."""
    A,D=F("7.000001"),F("6.000001")
    rho=F("1e-7")
    local=lambda a,d:2*(a+d/4)+F(5,2)*(a+rho)
    raw_low=8*(6*((2*A+rho)*97+local(A,D))+14*385)
    raw_high=6*((2*A+rho)*98+local(A,D))
    A1,D1=A+D,385*D
    # H^-1 multiplication by A^1 uses duality. The derivative is moved to the low output.
    rough_high=F("384.002")*6*((2*A1+rho)*98+local(A1,D1))
    selected_low_nu=F("1.768")*(6*((2*A+rho)*(19+F(83,4))+19*local(A,D))+14*(83+19))
    require(raw_low<112000 and raw_high<8500 and rough_high<8_800_000
            and selected_low_nu<15500,"entire raw and rough true low equations and full source variation")
    A_true,D_true=F("7.000002"),F("6.000002")
    require(7+19*F("1e-10")+rho<A_true and 6+83*F("1e-10")+rho<D_true,
            "whole true nonlinear state and first angular derivative")
    core_A=384*(6*A_true**2/4+14*A_true)+6*(1+3*A_true**2+A_true*D_true/2)+14*D_true
    require(core_A<70000 and F("25.944")**2/200<4 and F("8.22001")*F(".239")<2,
            "true hybrid operator, and separate root and strict ordinary forcings")
    return dict(low_from_weighted_low=112000,low_from_high_raw=8500,low_from_high_rough=8_800_000,
                selected_low_nu_variation=15500)


def numerical_gate(*,engine,model,admitted,boundary,boundary_store,gtp,outer_raw,SPN_raw,WHN_raw,
                   whn_spec,radius,emit):
    """One new full physical gate, centred on actual GG, using the perturbed high graph.

    The owner authenticates GG+original maps with the unmodified GG validator and GTP
    admission, and binds the actual successful WHN receipt in its manifest.
    """
    e,api=engine,engine.api
    require(sha256(SPN_raw).hexdigest()=="ac82ab9942eb4bbd8a7fa6522fbc4d8b7e4cd414db0e42bfa55bf1c4f8e8a4c2"
            and sha256(WHN_raw).hexdigest()==whn_spec["sha256"] and len(WHN_raw)==whn_spec["bytes"]
            and sha256(outer_raw).hexdigest()=="769204e822787216c5aebd2cde30e73759fcf66d3bb1d6d1d76d2381bad6cae6",
            "whole actual high neighbourhood, weighted response, original strong physical exterior")
    spn,whn,outer=map(json.loads,(SPN_raw,WHN_raw,outer_raw))
    require(spn["proved"] and whn["proved"] and len(spn["checks"])==32 and len(spn["whole_inputs"])==19
            and all(x is True for x in list(spn["checks"].values())+list(whn["checks"].values()))
            and whn["true_selected_nearby_head_rates"]==dict(root_collar_body_Z="11.9",raw_high="30",
                outer_even_Hminus5over6=".154") and outer["complete"] and outer["full_Hone_sixth_Riccati_graph_proved"]
            and admitted["reference_identity"]==model["context"].reference_identity
            and admitted["low_inverse_basis"]==gtp.TRUE_BASIS and "private_token" in admitted
            and model["private_model_token"] is boundary["private_model_token"]
            and boundary["complete_private_store"]==boundary_store.receipt()
            and boundary["complete_boundary_columns"]==193 and boundary["right_input_has_mean"],
            "actual complete common full-dimensional positive problem")
    radius=F(radius)
    require(0<radius<=F("1e-7"),"positive-radius genuinely nonlinear SPN neighbourhood")
    def Q(s):
        v=F(s)
        return api.rational(v.numerator,v.denominator)
    def save(name,value,bound="upper"):
        point=value.upper() if bound=="upper" else value.lower()
        r=emit(name,point,bound)
        require(r.is_finite() and (bool(r>=point) if bound=="upper" else bool(r<=point)),
                "complete directed current gate readback "+name)
        return r
    d=fees()
    rr=Q(radius)
    rawmap,centre,corr=(admitted["source_bounds"][k] for k in
                      ("ordinary_raw_low_source","centre_high0_return_source","low_second_kind_correction"))
    def maps(source,name):
        return source["body"] if name=="body" else api.sqrt(source[name+"_actual_squared"]).upper()
    names=("body","root","outer")
    k,high0,highm={},{},{}
    lam160=api.sqrt(Q(1+640**2))
    lam288=api.sqrt(Q(1+1152**2))
    lam96=api.sqrt(Q(1+384**2))
    for n in names:
        raw,c,v=(maps(s,n) for s in (rawmap,centre,corr))
        high0[n]=save("actual_nearby_high0_to_low_"+n,c+raw*(admitted["delta_C"]+rr*d["low_from_high_raw"]))
        highm[n]=save("actual_nearby_highminus1_to_low_"+n,
                lam160*c+raw*(lam288*admitted["delta_C"]+rr*d["low_from_high_rough"]))
        Lfactor=api.one+v if n=="body" else api.sqrt(api.one+v*v)
        k[n]=save("actual_nearby_internal_feedback_"+n,
                  Lfactor*admitted["L"]+raw*rr*d["low_from_weighted_low"]+30*high0[n])
    gap=save("actual_nearby_internal_gap",api.one-k["body"],"lower")
    out=dict(kind="R149_actual_low_high_and_physical_gate_in_true_noncompact_neighbourhood_v1",
             private_model_token=model["private_model_token"],radius=str(radius),kappa=k,high_raw=high0,
             high_weak=highm,internal_margin=gap,body_gate_passed=bool(gap>api.zero),
             physical_gate_passed=False,whole_original_193_coordinates=True,original_positive_TP_result_unchanged=True)
    if not out["body_gate_passed"]:
        return out
    def close(label,s):
        B=save(label+"_body",s["body"]/gap)
        return dict(body=B,**{n:save(label+"_"+n,s[n]+k[n]*B) for n in ("root","outer")})
    direct=boundary["actual_directed_observations"]
    G0=maps(corr,"body")
    P={};initial={}
    for which,part,Dr in (("right","charted_right97","reference_weighted_right97_body_upper"),
                          ("left","left96","reference_joint193_boundary_body_upper")):
        initial[which]=dict(body=(api.one+G0)*gtp.saved_upper(api,admitted["D"][Dr]),
                            root=direct["root_raw97"][part],outer=direct["outer_weighted96"][part])
        P[which]=close("nearby_"+which+"_boundary",initial[which])
    J0={n:min((high0[n]*Q("3.656366")*Q(".001")*lam96).upper(),
              (highm[n]*Q("12.912904")*Q(".001")).upper()) for n in names}
    J=close("nearby_outer96_high_return",J0)
    tb=save("actual_nearby_high_outer_readout_from_low_outer",
            min((Q(5)/388*Q("1.452083")*Q(".001")*lam96).upper(),(4*Q("5.128207")*Q(".001")).upper()))
    pl=api.old_interval(outer["bounds"]["actual_reference_outer_p_lower"]).lower()
    pu=api.old_interval(outer["bounds"]["actual_reference_outer_p_upper"]).upper()
    ep=min(rr,Q("9e-10"))
    p=api.interval((pl/(api.one+ep/Q("5.84"))).lower(),(pu/(api.one-ep/Q("5.84"))).upper())
    require(bool(p.lower()>Q(1)/8) and bool(p.upper()<Q(1)/5),"full true optical terminal stays in original chart")
    ah=save("actual_nearby_high_Robin_and_mean_to_right",
            api.sqrt(Q(".000283")**2+Q(".000219")**2))
    # From QN.38: (17/2)E/(1-(17/2)E)<.002402 gives E < .000283.
    ab=save("actual_nearby_low_Robin_and_mean_to_right",
            api.sqrt((Q(3)/80+Q(".000283"))**2+Q(".000219")**2))
    tx=Q(".154")
    u,v,w,z=(ah*tx*P["right"]["body"],ab+ah*(tb+tx*J["body"]),P["right"]["outer"],J["outer"])
    ordinary=[[u,v],[w,z]]
    def inverse2(label,N):
        a,b=N[0];c,d=N[1]
        x=save(label+"_right_margin",api.one-a,"lower")
        y=save(label+"_outer_margin",api.one-d,"lower")
        det=save(label+"_det",x*y-b*c,"lower")
        if not all(bool(v>api.zero) for v in (x,y,det)):
            return None
        return [[(api.one-d)/det,b/det],[c/det,(api.one-a)/det]]
    inverse=inverse2("nearby_direct_boundary",ordinary)
    mode="complete_actual_nearby_direct_boundary"
    if inverse is None:
        expected=next(item["matrix_record"] for item in boundary["complete_private_observations"]
                      if item["observation"]=="outer_weighted96")
        key=("observation","outer_weighted96")
        require(boundary_store.data[key]==expected,"authentic full signed Wc")
        Wc=e.columns(boundary_store.get(key),range(96,193))
        p0=e.exact_float(float(p.mid()))
        K=e.vcat(e.scale(Q(13)/80-p0,e.eye(96)),e.zero(1,96))
        M=e.inverse(e.vcat(e.hcat(e.eye(97),e.scale(-api.one,K)),e.hcat(e.scale(-api.one,Wc),e.eye(96))))
        split=(range(97),range(97,193))
        Mnorm=[[save("nearby_signed_chart_"+str(i)+str(j),e.submatrix(M,ri,cj).norm())
                for j,cj in enumerate(split)] for i,ri in enumerate(split)]
        err=[[u,api.magnitude(p-p0)+ah*(api.one+tb+tx*J["body"])],
             [k["outer"]*P["right"]["body"],J["outer"]]]
        defect=[[save("nearby_actual_signed_defect_"+str(i)+str(j),sum((Mnorm[i][s]*err[s][j]
                      for s in range(2)),api.zero)) for j in range(2)] for i in range(2)]
        N=inverse2("nearby_signed_boundary",defect)
        if N is not None:
            inverse=[[sum((N[i][s]*Mnorm[s][j] for s in range(2)),api.zero) for j in range(2)] for i in range(2)]
        mode="complete_actual_nearby_signed_boundary"
    out.update(initial_boundary=initial,closed_boundary=P,closed_outer_poisson=J,
               high_outer_from_low_outer=tb,high_to_right97=ah,physical_outer_direct_matrix=ordinary)
    if inverse is None:
        out["branch"]="neither_current_sufficient_boundary_test_passed"
        return out
    out["physical_gate_passed"]=True
    out["branch"]=mode
    out["physical_inverse"]=[[save("nearby_final_physical_inverse_"+str(i)+str(j),inverse[i][j])
                              for j in range(2)] for i in range(2)]
    return out


def positive_response_and_negative_readout(*,engine,model,admitted,gate,boundary,particular,
                                         original_high_receipt,oa_raw,inputs,column,state_radius,emit):
    """Complete positive solve for the supplied independent data and full original negative-window test.

    Each input is a certified upper for the named norm. A nonlinear Newton
    column away from the selected point must supply its actual residual data.
    """
    e,api=engine,engine.api
    def Q(value):
        v=F(value)
        return api.rational(v.numerator,v.denominator)
    require(column in ("Newton","nu") and gate["physical_gate_passed"] and gate["body_gate_passed"]
            and model["private_model_token"] is gate["private_model_token"] is boundary["private_model_token"]
            and model["private_model_token"] is particular["private_model_token"]
            and sha256(original_high_receipt).hexdigest()=="312c60afba95bc4e41bd29549a444031cbd633cd252be981bcccb329e54a4993",
            "actual successful *current* physical inverse and original signed low columns")
    require(sha256(oa_raw).hexdigest()==json.loads(original_high_receipt)["whole_inputs"]["OA"],
            "entire original OA, with the actual independent physical mean of the Newton residual")
    oa=json.loads(oa_raw)
    require(oa["complete"] and oa["proved"] and oa["actual_returncode"]==0,"actual original physical right-hand side")
    state_radius=F(state_radius)
    require(0<=state_radius<=F(gate["radius"]),"stated current state lies in the entire positive-radius inverse domain")
    expected={"root_left96","root_stable","collar_Hthird","body_Hthird","body_frame_jumps",
              "collar_frame_jumps","cut_stable_jump","cut_unstable_jump","positive_low_raw_jump_sum",
              "low_ordinary_extra","extra_charted_right97","height_second_Hsixth","Robin_extra_Hsixth",
              "mean_extra","negative_root_jump_sum","negative_strict_raw_jump_sum","positive_sliver_low_jump_sum",
              "extra_negative_root_Hthird","extra_negative_strict_L2"}
    if column=="Newton" and state_radius!=0:
        expected.update(("Newton_current_minus_original_low_ordinary","Newton_current_high_ordinary_Hthird",
                         "Newton_current_Robin_Hsixth","Newton_current_mean_residual"))
    require(set(inputs)==expected and all(v.is_finite() and api.lower(v)>=0 for v in inputs.values()),
            "every declared physical datum with the original independent means, height, and jump units")
    def save(name,value):
        v=value.upper()
        r=emit(column+"_"+name,v,"upper")
        require(r.is_finite() and bool(r>=v),"whole directed received upper")
        return r
    f=inputs
    rho=Q(state_radius)
    q=0 if column=="Newton" else 1
    if column=="nu":
        high=Q("1.254870e-9")+9*rho
        R,M=Q("1.23e-11"),Q("9.1e-16")
        change=15500*rho
        low0=Q("2.9476e-5")
    else:
        low0=Q("7.051e-8")
        if state_radius==0:
            high,R,change=Q("1.17560e-19"),Q("1e-14"),api.zero
            M=api.old_interval(oa["complete_new_scalar_records"]["complete_selected_independent_physical_mean_residual_upper"]).upper()
        else:
            high,R,M,change=(f[k] for k in ("Newton_current_high_ordinary_Hthird","Newton_current_Robin_Hsixth",
                "Newton_current_mean_residual","Newton_current_minus_original_low_ordinary"))
    lowextra=change+f["low_ordinary_extra"]
    strongR,strongM=R+f["Robin_extra_Hsixth"],M+f["mean_extra"]
    h=f["height_second_Hsixth"]
    Bext=f["body_frame_jumps"]+Q(".004")*h+23*strongR+28*strongM
    def rows(s,fc,fb,B,jc,js,ju):
        qc,rc,bc,qb,rb,bf=(Q(x) for x in ("750/749","1/749",".009","100/69","31/69",".126142"))
        x=(qc*s+qc*(bc*fc+jc)+js+rc*(qb*(bf*fb+B)+ju))/(api.one-rc*rb)
        y=rb*x+qb*(bf*fb+B)+ju
        return (rc*s+qc*y+qc*(bc*fc+jc),qc*(s+y+bc*fc+jc),qb*(x+bf*fb+B))
    independent=rows(f["root_stable"],f["collar_Hthird"],f["body_Hthird"],Bext,
                     f["collar_frame_jumps"],f["cut_stable_jump"],f["cut_unstable_jump"])
    zero,one=api.zero,api.one
    fc=rows(zero,one,zero,zero,zero,zero,zero)
    fb=rows(zero,zero,one,zero,zero,zero,zero)
    U,V,Zb=(save("direct_selected_strong_"+s,x+api.sqrt(a*a+b*b)*high)
            for s,x,a,b in zip(("outgoing","collar","body"),independent,fc,fb))
    C=save("direct_high_raw_L2",api.sqrt(9*Q("9e-6")*V*V+Q("2.518")**2*Zb*Zb))
    Y=save("direct_high_terminal_y_rough",Q("5/388")*Zb)
    d=save("actual_independent_physical_right97",
        api.sqrt((8*strongR+9*strongM+Q(".0013")*h)**2+
                 (Q("49.012")*strongM+Q(".000822")*h)**2)+gate["high_to_right97"]*Y+f["extra_charted_right97"])
    raw=admitted["source_bounds"]["ordinary_raw_low_source"]
    def g(n):
        return raw["body"] if n=="body" else api.sqrt(raw[n+"_actual_squared"])
    # A one-sided triangular trace lift works at every interior physical interface.
    # Its radial derivative and the full original A^c are charged in raw forcing units.
    Mcore=Q(70000)
    duration=Q("1/40000")
    impulse=one/api.sqrt(duration)+Mcore*api.sqrt(duration/3)
    Sq=max([one]+[api.magnitude(v) for v in model["context"].reference_qs])
    j=f["positive_low_raw_jump_sum"]
    jump_pay={n:g(n)*impulse*j for n in ("body","root","outer")}
    jump_pay["body"]+=Sq*api.sqrt(duration/3)*j
    G=gate["initial_boundary"]
    obs=particular["observations"]
    seed={}
    for n,part in (("body","weighted_body"),("root","root_raw97"),("outer","outer_weighted96")):
        z0=min(obs[part]["column_norm_upper"][q].upper(),(g(n)*low0).upper())
        seed[n]=save("whole_true_hybrid_seed_"+n,z0+g(n)*lowextra+gate["high_raw"][n]*C+
            G["left"][n]*f["root_left96"]+G["right"][n]*d+jump_pay[n])
    B=save("closed_internal_known_weighted_head",seed["body"]/gate["internal_margin"])
    O=save("closed_internal_known_outer96",seed["outer"]+gate["kappa"]["outer"]*B)
    forcing_r=gate["high_to_right97"]*Q(".154")*B
    P=gate["physical_inverse"]
    r,a=(save(k,row[0]*forcing_r+row[1]*O) for k,row in zip(("physical_feedback_right","physical_low_terminal"),P))
    lift,poisson=gate["closed_boundary"]["right"],gate["closed_outer_poisson"]
    X=save("actual_whole_weighted_body",B+lift["body"]*r+poisson["body"]*a)
    rawroot=seed["root"]+gate["kappa"]["root"]*B+lift["root"]*r+poisson["root"]*a
    weight=Q(1+384**2)**Q("1/6")
    raw_to_mixed=api.sqrt((weight*rawroot)**2+f["root_left96"]**2)
    direct=boundary["actual_directed_observations"]["root_mixed_full193"]
    signed_mix=min(obs["root_mixed_full193"]["column_norm_upper"][q].upper(),(weight*g("root")*low0).upper())
    other=weight*(g("root")*lowextra+gate["high_raw"]["root"]*C+jump_pay["root"]+gate["kappa"]["root"]*B+
                  lift["root"]*r+poisson["root"]*a)
    b=save("actual_mixed_low_root",min(raw_to_mixed.upper(),(signed_mix+other+
        direct["left96"]*f["root_left96"]+direct["charted_right97"]*d).upper()))
    both=Q("11.9")*X+Q("1.453")*Q(".001")*api.sqrt(Q(1+384**2))*a
    out=dict(kind="R149_true_positive_response_to_received_signed_and_independent_data_v1",
             column=column,actual_weighted_body=X,actual_mixed_low_root=b,actual_weighted_low_outer=a,
             actual_strong_outgoing=save("true_strong_root_outgoing",U+both),
             actual_strong_collar=save("true_strong_collar",V+both),
             given_input_physical_positive_problem_proved=True,global_input_matching_proved=False)
    if column=="nu":
        # WHN.3 has already charged the known s_delta and the true Z outer rows.
        independent=rows(f["root_stable"],f["collar_Hthird"],f["body_Hthird"],
             f["body_frame_jumps"]+23*f["Robin_extra_Hsixth"]+28*f["mean_extra"],
             f["collar_frame_jumps"],f["cut_stable_jump"],f["cut_unstable_jump"])
        E=Q("25.95")*Q("9.00002")*(f["root_stable"]+independent[0])+Q("2.86e-6")*independent[1]
        E+=Q("25.944")*f["negative_root_jump_sum"]+Q("3.973")*f["negative_strict_raw_jump_sum"]
        E+=Q("9.54e-7")*f["positive_sliver_low_jump_sum"]
        # Additional ordinary low sources on the positive sliver require their own direct integral.
        # The whole-window extra bound pays the sliver by the same Duhamel argument.
        E+=Q("1.005")*Q("9e-13")*f["low_ordinary_extra"]
        E+=2*(f["extra_negative_root_Hthird"]+f["extra_negative_strict_L2"])
        norm=save("whole_negative_ordinary_L2",Q("25.95")*b+2780*X+131*a+Q("1.36")*h+
                  E+Q("1.774e-5")+5530*rho)
        out.update(complete_ordinary_negative_L2_for_received_data=norm,
                   sufficient_negative_gate_for_received_data=bool(norm<=Q(".005")))
    return out
