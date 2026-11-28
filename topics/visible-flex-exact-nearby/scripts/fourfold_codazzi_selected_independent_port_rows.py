"""All independent physical datum columns through the selected-height and full negative response."""
from fractions import Fraction


def complete(*,engine,model,admitted,gate,boundary,fields,selected,emit):
    api=engine.api
    if not (gate["physical_gate_passed"] and selected["complete_selected_height_loop_passed"] and
            model["private_model_token"] is gate["private_model_token"] is boundary["private_model_token"]):
        raise ValueError("actual complete physical and selected-height inverses required")
    def Q(s):
        q=Fraction(s)
        return api.rational(q.numerator,q.denominator)
    z,one=api.zero,api.one
    g0=admitted["source_bounds"]["ordinary_raw_low_source"]
    raw={n:g0["body"] if n=="body" else api.sqrt(g0[n+"_actual_squared"]) for n in ("body","root","outer")}
    dt=Q("1/40000")
    lift=one/api.sqrt(dt)+70000*api.sqrt(dt/3)
    Sq=max([one]+[api.magnitude(x) for x in model["context"].reference_qs])
    lam=api.sqrt(Q(1+384**2))
    low_root_weight=Q(1+384**2)**Q("1/6")
    ah=gate["high_to_right97"]
    def response(unit):
        f={k:one if k==unit else z for k in fields}
        s,fc,fb,jc,js,ju=(f[k] for k in ("root_stable","collar_Hthird","body_Hthird","collar_frame_jumps",
                                           "cut_stable_jump","cut_unstable_jump"))
        R,M,H=f["Robin_extra_Hsixth"],f["mean_extra"],f["height_second_Hsixth"]
        def graph(h):
            ext=f["body_frame_jumps"]+Q(".004")*h+23*R+28*M
            p=(s,fc,fb,ext,jc,js,ju)
            def row(coefficients):
                return sum((Q(v)*w for v,w in zip(coefficients,p)),z)
            body=row(("1.452083",".013070",".183170","1.452083","1.452083","1.450147",".001938"))
            out=row((".452083",".013070",".183170","1.452083","1.452083",".450147",".001938"))
            raw=row(("3.656366",".032909",".461223","3.656366","3.656366","3.651469",".010252"))
            # QN.43 gives S_c=U_a+s for these actual complete strong data.
            return body,out,out+s,raw
        SB,U,V,C=graph(H)
        datum=api.sqrt((8*R+9*M+Q(".0013")*H)**2+(Q("49.012")*M+Q(".000822")*H)**2)
        datum+=ah*Q("5/388")*SB+f["extra_charted_right97"]
        jumps=f["positive_low_raw_jump_sum"]
        G=f["low_ordinary_extra"]
        left=f["root_left96"]
        d=gate["initial_boundary"]
        initial={n:raw[n]*(G+lift*jumps)+gate["high_raw"][n]*C+d["left"][n]*left+d["right"][n]*datum
                 for n in ("body","root","outer")}
        initial["body"]+=Sq*api.sqrt(dt/3)*jumps
        X=initial["body"]/gate["internal_margin"]
        O=initial["outer"]+gate["kappa"]["outer"]*X
        r,a=(row[0]*ah*Q(".154")*X+row[1]*O for row in gate["physical_inverse"])
        P,J=gate["closed_boundary"]["right"],gate["closed_outer_poisson"]
        B=X+P["body"]*r+J["body"]*a
        root=initial["root"]+gate["kappa"]["root"]*X+P["root"]*r+J["root"]*a
        b=api.sqrt((low_root_weight*root)**2+left**2)
        high_head=Q("11.9")*B+Q("1.453")*Q(".001")*lam*a
        high_raw=30*B+Q("3.656366")*Q(".001")*lam*a+C
        cut=4400*B+Q(".332")*high_raw+Q("3.6")*(SB+high_head)+Q(".005")*G+jumps
        _,Ue,Ve,_=graph(z)
        E=Q("25.95")*Q("9.00002")*(s+Ue)+Q("2.86e-6")*Ve
        E+=Q("25.944")*f["negative_root_jump_sum"]+Q("3.973")*f["negative_strict_raw_jump_sum"]
        E+=Q("9.54e-7")*f["positive_sliver_low_jump_sum"]+Q("1.005")*Q("9e-13")*G
        E+=2*(f["extra_negative_root_Hthird"]+f["extra_negative_strict_L2"])
        return dict(weighted_body=B,mixed_low_root=b,charted_low_outer=a,strong_outgoing=U+high_head,
                    strong_collar=V+high_head,whole_even_cut=cut,ordinary_negative=Q("25.95")*b+2780*B+131*a+Q("1.36")*H+E)
    unit_height=response("height_second_Hsixth")
    omega=Q(10**9)*Q(2)**(-31223222)
    gap=selected["margin"]
    result={}
    for datum in [k for k in fields if k!="height_second_Hsixth"]+["selected_cut_explicit_L2","external_added_far_height"]:
        open_=response(datum)
        F=(Q(".11")*omega*open_["whole_even_cut"]+(omega if datum=="selected_cut_explicit_L2" else z)+
           (one if datum=="external_added_far_height" else z))/gap
        out={k:emit(datum,k,v+unit_height[k]*F) for k,v in open_.items()}
        out["selected_far_height"]=emit(datum,"selected_far_height",F)
        result[datum]=out
    return dict(whole_received_port_columns=result,source_coordinates="independent_original_norms_before_global_matching",
        complete_signed_affine_constants_are_separate=True,actual_global_port_values_verified=False)
