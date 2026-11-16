"""WVC: complete continuous-centre and clipped-tracefree residual assembly.

No entry point, import of a numerical package, old producer, file IO, or launch.
Use the published physical kernel engine as 'km'.  The caller admits the full
reference/row/cubic/repair closure and stores every emit result before this
module uses its directed readback. An emit(name,value) returns that readback.
The input work is the COMPLETE declared 155-or-fewer comparison partition,
with its original 153-parent identity and SAME S/projection/tail spaces.
The repaired degree32 coefficients vary over the whole radial domain.
Only full96 differences occupy difference_AL/LH; no frozen-centre norm is
subtracted. The high principal is unchanged. No input is a sample table.
"""

def require(ok,message):
    if not ok:
        raise ValueError(message)


def norm_record(api,km,operator,vin,wout,emit,name):
    return km.published_kernel_norm(api,operator,vin,wout,emit,name)


def constant_weights(api,n,dimension):
    return [[api.one]*dimension for _ in range(n)]


def body_weights(api,coords,scales):
    return [[api.one if component==0 else scales[i] for component,j in coords]
            for i in range(len(scales))]


def source_weights(api,coords,riesz,n,inverse=False):
    return [[(api.one/riesz[j] if inverse else api.one) for component,j in coords]
            for _ in range(n)]


def output_weights(api,green):
    body=body_weights(api,green.coords,green.scales)
    atoms=[]
    for component,j in green.atom_coords:
        atoms.append(green.thetas[j] if component==2 else api.one)
    return {"body":body,"atoms":atoms}


def new_operator_graph(api,km,work):
    """Every cross/local factor uses the SAME 193 physical coordinates."""
    n=len(work["lengths"])
    head=km.band(0,96);nonmean=km.band(1,96)
    high=km.band(97,160);source=km.band(97,224)
    require(len(head)==193 and len(high)==128 and len(source)==256,
            "complete reflected physical coordinates")
    scales=work["scales"];sqrt_two=work["sqrt_two"]
    one_high=constant_weights(api,n,len(high))
    one_head=constant_weights(api,n,len(head))
    inv_head=[[api.one if component==0 else api.one/scales[i]
               for component,j in head] for i in range(n)]
    chi_high=[[api.magnitude(work["chi"][i])]*len(high) for i in range(n)]
    source_weight=[[work["source_riesz"][j] for component,j in source] for _ in range(n)]
    low_green=km.GreenMajorant(api,work["lengths"],range(1,97),work["profiles"],
        scales,work["thetas"],include_mean=True,include_atoms=True)
    no_mean_green=km.GreenMajorant(api,work["lengths"],range(1,97),work["profiles"],
        scales,work["thetas"],include_mean=False,include_atoms=True)
    high_green=km.GreenMajorant(api,work["lengths"],range(97,161),work["profiles"],
        [api.one]*n,work["thetas"],include_mean=False,include_atoms=False)

    low_maps=[];hl_maps=[];lh_maps=[];source_local=[];source_kernel=[]
    for i in range(n):
        centre=work["repaired_packets"][i]
        high_principal={"eta":work["etas"][i],"q":work["reference_qs"][i]}
        low_principal={**high_principal,"diagonal":work["selected_diagonals"][i]}
        low_maps.append(km.generator_majorant(api,centre,head,head,sqrt_two,low_principal))
        hl_maps.append(km.generator_majorant(api,centre,head,high,sqrt_two))
        lh_maps.append(km.generator_majorant(api,centre,high,head,sqrt_two))
        # Exact (chi^2-Id) B_HLc: form the scalar difference, never two
        # independently enclosed copies of the same coefficient matrix.
        source_local.append(km.generator_majorant(api,centre,head,source,sqrt_two))
        source_kernel.append(km.kernel_factor_majorant(api,centre,high_principal,
            work["chi"][i],work["chi_prime"][i],high,source,sqrt_two))
    low=km.PointwiseMap(api,low_maps,inv_head,one_head)
    hl_chi=km.PointwiseMap(api,hl_maps,inv_head,chi_high)
    lh=km.PointwiseMap(api,lh_maps,one_high,one_head)
    pretrial=km.Composition(high_green,hl_chi)
    trial=km.Composition(km.DiagonalMap(api,chi_high),pretrial)
    gammahat=km.SumMap(api,[low,km.Composition(lh,trial)])
    body_mask=[[api.zero if work["parent_indices"][i]==0 else v for v in row]
               for i,row in enumerate(source_weight)]
    local_mask=[[value*api.magnitude(work["chi"][i]*work["chi"][i]-api.one)
                 for value in row] for i,row in enumerate(body_mask)]
    sl=km.PointwiseMap(api,source_local,inv_head,local_mask)
    sk=km.PointwiseMap(api,source_kernel,one_high,body_mask)
    residual=km.SumMap(api,[sl,km.Composition(sk,pretrial)])
    lambda_high=[[work["state_inverse_riesz"][j] for component,j in high] for _ in range(n)]
    lh_high_input=km.PointwiseMap(api,lh_maps,lambda_high,one_head)
    low_source=km.Composition(low_green,gammahat)
    paired_cross=km.Composition(low_green,lh_high_input)
    tv_diagonal=[[work["fine_tau"][i]*(api.one if component==0 else scales[i])
                  for component,j in head] for i in range(n)]
    tv=km.DiagonalMap(api,tv_diagonal)
    return {"head":head,"nonmean":nonmean,"high":high,"source":source,
        "low_green":low_green,"no_mean_green":no_mean_green,"high_green":high_green,
        "pretrial":pretrial,"trial":trial,"gammahat":gammahat,"residual":residual,
        "paired_cross":paired_cross,"low_source":low_source,
        "tail_cross":km.Composition(tv,lh_high_input),
        "tail_source":km.Composition(tv,gammahat),"tv":tv}


def scalar_green_map(api,km,green,weights):
    require(len(weights)==len(green.lengths),"whole scalar source weight")
    diagonal=[[weight]*green.in_dim for weight in weights]
    return km.Composition(green,km.DiagonalMap(api,diagonal))


def complete_high_trial_source(api,km,work,operators,old,emit):
    """New complete body residual, with original collar source copied once."""
    n=len(work["lengths"]);head=operators["head"];high=operators["high"]
    vin=body_weights(api,head,work["scales"])
    high_out={"body":constant_weights(api,n,len(high)),"atoms":[]}
    source_out={"body":constant_weights(api,n,len(operators["source"])),"atoms":[]}
    trial_norm=norm_record(api,km,operators["trial"],vin,high_out,emit,"complete_trial_raw")
    centre_source=norm_record(api,km,operators["residual"],vin,source_out,
                             emit,"complete_repaired_centre_body_residual")
    # The operator Delta B_HL S^-1 and the source window are unchanged.
    # This complete original record was copied and admitted before import.
    local_family=old["family_HL_body_residual"]
    delta_diag=[[work["lambda_388_minus_two_thirds"]*api.magnitude(work["chi"][i])*
                  work["family_AHH"][i]]*len(high) for i in range(n)]
    kernel_family=norm_record(api,km,km.Composition(km.DiagonalMap(api,delta_diag),
                        operators["pretrial"]),vin,high_out,emit,"complete_family_high_kernel")
    alpha_b=emit("complete_body_ordinary_source_upper",
                  api.upper(centre_source+local_family+kernel_family))
    alpha_c=old["A_c"]  # Verbatim complete old object is copied by the driver.
    state=emit("complete_high_state_error_upper",
               api.upper(old["C_c"]*alpha_c+old["C_b"]*alpha_b))
    trace=emit("complete_high_outer_trace_error_upper",
               api.upper(4*(old["Y_c"]*alpha_c+old["Y_b"]*alpha_b)))
    return {"trial_raw":trial_norm,"body_source":alpha_b,
            "collar_source":alpha_c,"high_state_error":state,"high_trace_error":trace}


def complete_actual_paired_receivers(api,km,work,operators,high_source,old,emit):
    n=len(work["lengths"]);head=operators["head"];high=operators["high"]
    wout=output_weights(api,operators["low_green"])
    wout_no_mean=output_weights(api,operators["no_mean_green"])
    vin_head=body_weights(api,head,work["scales"])
    vin_high=source_weights(api,high,work["state_inverse_riesz"],n,inverse=True)
    paired_centre=norm_record(api,km,operators["paired_cross"],vin_high,wout,
                             emit,"complete_centre_paired_LH")
    # Full96 Delta_LH has zero true mean output. Only its complete error leg uses
    # the full 97..288 input conversion; the centre keeps every actual j.
    delta_weight=[old["shell_1153"]*v for v in work["difference_LH"]]
    delta_map=scalar_green_map(api,km,operators["no_mean_green"],delta_weight)
    delta_cross=norm_record(api,km,delta_map,
        constant_weights(api,n,len(operators["nonmean"])),wout_no_mean,
        emit,"complete_difference_paired_LH")
    paired=emit("complete_actual_paired_LH_upper",api.upper(paired_centre+delta_cross))
    tail_centre=norm_record(api,km,operators["tail_cross"],vin_high,
        {"body":constant_weights(api,n,len(head)),"atoms":[]},
        emit,"complete_centre_tail_LH")
    tail_delta=emit("complete_difference_tail_LH_upper",km.maximum(api,[
        work["fine_tau"][i]*work["S_norm"][i]*old["shell_1153"]*work["difference_LH"][i]
        for i in range(n)]))
    tail=emit("complete_actual_tail_LH_upper",api.upper(tail_centre+tail_delta))

    low_difference=scalar_green_map(api,km,operators["low_green"],
        [work["difference_AL"][i]*work["S_inverse_norm"][i] for i in range(n)])
    low_error=norm_record(api,km,low_difference,constant_weights(api,n,len(head)),
                         wout,emit,"complete_low_generator_difference")
    lh_difference=scalar_green_map(api,km,operators["no_mean_green"],work["difference_LH"])
    lh_error=norm_record(api,km,lh_difference,
        constant_weights(api,n,len(operators["nonmean"])),wout_no_mean,
        emit,"complete_raw_difference_LH_receiver")
    eps_H=emit("complete_head_paired_error_upper",api.upper(low_error+
        lh_error*high_source["trial_raw"]+paired*high_source["high_state_error"]))
    eps_b=emit("complete_outer_paired_error_upper",api.upper(paired*old["P_b_raw"]))

    t_delta_al=emit("complete_low_generator_tail_error_upper",km.maximum(api,[
        work["fine_tau"][i]*work["S_norm"][i]*work["difference_AL"][i]*
        work["S_inverse_norm"][i] for i in range(n)]))
    t_delta_lh=emit("complete_raw_difference_tail_LH_upper",km.maximum(api,[
        work["fine_tau"][i]*work["S_norm"][i]*work["difference_LH"][i] for i in range(n)]))
    return {"paired":paired,"tail":tail,"eps_H":eps_H,"eps_b":eps_b,
            "tail_AL":t_delta_al,"tail_LH":t_delta_lh}


def complete_local_signed_remainder(api,km,work,operators,high_source,receivers,old,emit):
    n=len(work["lengths"]);head=operators["head"]
    vin=body_weights(api,head,work["scales"])
    K_H=norm_record(api,km,operators["low_source"],vin,
        output_weights(api,operators["low_green"]),emit,"complete_signed_centre_paired_source")
    t_hat=norm_record(api,km,operators["tail_source"],vin,
        {"body":constant_weights(api,n,len(head)),"atoms":[]},
        emit,"complete_signed_centre_tail_source")
    t_H=emit("complete_actual_head_tail_source_upper",api.upper(t_hat+
        receivers["tail_AL"]+receivers["tail_LH"]*high_source["trial_raw"]+
        receivers["tail"]*high_source["high_state_error"]))
    t_b=emit("complete_actual_outer_tail_source_upper",api.upper(receivers["tail"]*old["P_b_raw"]))
    return {"K_H":K_H,"t_H":t_H,"t_b":t_b}


def complete_endpoint_correction(api,reference,high_source,old,emit):
    q_R=emit("complete_high_trace_endpoint_receiver_upper",
              api.upper(reference["q_o"]*old["E_minus"]+reference["q_m"]*old["mu_minus"]))
    o_H=emit("complete_head_endpoint_correction_upper",
              api.upper(q_R*high_source["high_trace_error"]))
    o_b=emit("complete_outer_endpoint_correction_upper",api.upper(
        (api.rational(3,80)+old["E_minus"])*reference["q_o"]+
        old["mu_minus"]*reference["q_m"]+q_R*old["Y_b_outer"]))
    return {"o_H":o_H,"o_b":o_b}


def complete_actual_E_D_T(api,reference,receivers,local,endpoint,emit):
    e_rho,w0=reference["e_rho"],reference["w0"]
    h=local["K_H"]+receivers["eps_H"]
    e=emit("complete_actual_E0_upper",api.upper(e_rho+(1+e_rho)*
        api.sqrt(w0*w0*h*h+receivers["eps_b"]*receivers["eps_b"])+
        api.sqrt(w0*w0*endpoint["o_H"]*endpoint["o_H"]+
                 endpoint["o_b"]*endpoint["o_b"])))
    d=emit("complete_actual_D_upper",api.upper((1+e_rho)*h+endpoint["o_H"]))
    t=emit("complete_actual_T_upper",api.upper(api.sqrt(w0*w0*local["t_H"]*local["t_H"]+
                                                     local["t_b"]*local["t_b"])))
    defect=emit("complete_actual_finite_defect_upper",api.upper(e+3*d*t))
    passed=defect<1
    result={"e":e,"d":d,"t":t,"defect":defect,"passed":passed,
        "tail_inverse_upper":3,"all_four_blocks_and_both_rhs_retained":True,
        "full_physical_193_and_root97_outer96_retained":True}
    if passed:
        gap=emit("complete_actual_finite_gap_lower",api.lower(1-defect),endpoint="lower")
        inverse=emit("complete_actual_finite_inverse_upper",api.upper(reference["q"]/gap))
        result.update({"gap":gap,"finite_inverse":inverse})
    return result
