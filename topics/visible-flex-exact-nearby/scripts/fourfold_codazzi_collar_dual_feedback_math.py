"""W2C: complete joint signed centre and five atomic mathematical graphs.

No entry point, numerical package import, file IO, or old producer call.
This is one fixed WVC-reference candidate. The owner admits every old input,
materializes the genuine signed centre on the collar, and supplies the full
positive-family difference comparisons. No original completed norm is rerun.

The signed carrier is H_{97..288}; B_c and B_LH,c have external support <=160.
The actual inverse still acts on the complete infinite high space. Its full
collar/body receiver records are read once. The genuine family residual and
state-dual output support is <=416. The 160 in the inherited radial refinement
is a different index and is not altered here.
"""


def require(ok,message):
    if not ok:
        raise ValueError(message)


GRAPH_NAMES = [
    "complete_primal_trial_and_actual_residual",
    "complete_dual_actual_residual",
    "complete_family_and_dual_feedback",
    "complete_signed_centre",
    "complete_same_actual_finite_comparison",
]

TRIPLE_SUFFIXES = ("_row_ratio_upper","_column_ratio_upper","_norm_upper")
PRIMAL_TRIPLES = (
    "complete_raw_trial",
    "complete_centre_collar_source",
    "complete_centre_body_source",
    "complete_family_collar_source",
    "complete_family_body_source",
)
DUAL_TRIPLES = (
    "complete_centre_collar_dual",
    "complete_centre_body_dual",
    "complete_family_collar_dual",
    "complete_family_body_dual",
)
FAMILY_TRIPLES = (
    "complete_low_family_feedback",
    "complete_cross_family_feedback",
    "complete_trial_family_feedback",
)


def record_names(graph,passed=False):
    if graph==GRAPH_NAMES[0]:
        return [p+s for p in PRIMAL_TRIPLES for s in TRIPLE_SUFFIXES]+[
            "complete_primal_collar_source_upper",
            "complete_primal_body_source_upper",
            "complete_high_state_error_upper"]
    if graph==GRAPH_NAMES[1]:
        return [p+s for p in DUAL_TRIPLES for s in TRIPLE_SUFFIXES]+[
            "complete_dual_collar_residual_upper",
            "complete_dual_body_residual_upper",
            "complete_dual_residual_upper"]
    if graph==GRAPH_NAMES[2]:
        return [p+s for p in FAMILY_TRIPLES for s in TRIPLE_SUFFIXES]+[
            "complete_dual_feedback_error_upper",
            "complete_head_paired_error_upper"]
    if graph==GRAPH_NAMES[3]:
        return ["complete_joint_signed_centre"+s for s in TRIPLE_SUFFIXES]
    if graph==GRAPH_NAMES[4]:
        names=["complete_actual_E0_upper","complete_actual_D_upper",
               "complete_actual_finite_defect_upper"]
        if passed:
            names += ["complete_actual_finite_gap_lower","complete_actual_finite_inverse_upper"]
        return names
    raise ValueError("undeclared complete W2C graph")


def _chain(km,label,*operators):
    require(len(operators)>0,"complete ordered operator chain")
    result=operators[-1]
    for i in range(len(operators)-2,-1,-1):
        result=km.compose(operators[i],result,label+":"+str(i))
    return result


def _sum(km,label,*operators):
    return km.sum_kernel(label,*operators)


def _minus(km,api,operator,label):
    return km.scaled_kernel(-api.one,operator,label)


def complete_joint_operator_graph(api,km,ctx):
    """Materialize only the bounded-width complete joint-kernel interface.

    The old symbolic DAG is retained below as an exact algebraic definition,
    but even its eager zero endpoint matrices grow with its compound ranks.
    Graphs1--3 use their complete scalar comparisons, and graph4 uses the
    proved column realization of the identical WJK formula. No high-rank DAG
    is allocated by the scientific entry point.
    """
    required=("same_WVC_reference","same_actual_S_and_all_seven_ports",
              "all_coefficient_pieces_and_raw_identity_transmissions",
              "true_signed_collar_not_zero_reference_packet",
              "Bc_and_BLHc_external_support_160","trial_support_224",
              "centre_residual_support_288","whole_family_support_416",
              "ordinary_dr_pairing_and_complete_Gf_atoms")
    require(all(ctx.qualifications.get(key) is True for key in required),
            "all original actual-domain and exact-support qualifications")
    require(ctx.operators["G0"].atom_count==0
            and ctx.operators["Gf"].atom_count==193
            and len(ctx.operators["Bc"].inputs)==193,
            "complete original head, mean and output observations")
    return {"Hc":CompleteJointCentreColumns(api,km,ctx),
            "same_exact_WJK7_and_all_five_collar_terms":True,
            "all_other_ports_remain_in_complete_owner_contract":True}


def _uncompressed_joint_operator_graph(api,km,ctx):
    """Exact WJK operator algebra before any norm or absolute value.

    ctx supplies local multiplication maps I/Pc/Pb/chi/chi_prime/psi/psi_prime,
    chi_squared/chi_cubed, Pi0, Ac, D0, Bc, BLHc, Mc, and the true signed G0/Gf.
    All high-square maps use the SAME explicit H97..288 carrier. Bc includes
    the physical right S^-1. Mc=(AL,c-Df)S^-1, with Df the fixed complete WVC
    diagonal reference. Gf includes S on the body and all 193 output atoms.
    G0 has no atoms, no mean, and is exactly zero off modes97..160.

    The masks are the actual fixed functions, not independent interval signs.
    In particular chi=0 on Pc, psi=1 on Pc, and Pi0 Bc=Bc,
    BLHc Pi0=BLHc. These are admitted operator identities, not numerical tests.
    """
    required=("same_WVC_reference","same_actual_S_and_all_seven_ports",
              "all_coefficient_pieces_and_raw_identity_transmissions",
              "true_signed_collar_not_zero_reference_packet",
              "Bc_and_BLHc_external_support_160","trial_support_224",
              "centre_residual_support_288","whole_family_support_416",
              "ordinary_dr_pairing_and_complete_Gf_atoms")
    require(all(ctx.qualifications.get(key) is True for key in required),
            "all actual-domain and exact-support qualifications")
    names=("I","Pc","Pb","X","Xp","X2","X3","Psi","Psip",
           "Pi0","Ac","D0","Bc","BLHc","Mc","G0","Gf")
    require(all(name in ctx.operators for name in names),"complete declared signed input maps")
    o=ctx.operators
    I,Pc,Pb=o["I"],o["Pc"],o["Pb"]
    X,Xp,X2,X3=o["X"],o["Xp"],o["X2"],o["X3"]
    Psi,Psip=o["Psi"],o["Psip"]
    Pi0,A,D0=o["Pi0"],o["Ac"],o["D0"]
    Bc,BLH,Mc,G,Gf=o["Bc"],o["BLHc"],o["Mc"],o["G0"],o["Gf"]
    require(G.atom_count==0 and Gf.atom_count==193,
            "full signed low Green atoms, no reference high atoms")
    require(len(I.inputs)==384 and len(Bc.inputs)==193 and len(Gf.outputs)==193,
            "actual H288 carrier and complete physical head193")
    J=km.collar_primitive(I.domain,I.inputs,Pc.local,"true_Jc")
    Js=km.body_adjoint(J,"true_Jc_adjoint_to_R")
    As=km.body_adjoint(A,"true_Ac_adjoint")
    Gs=km.body_adjoint(G,"true_G0_adjoint")
    Ds=km.body_adjoint(D0,"true_D0_adjoint")
    E=_sum(km,"complete_E",A,_minus(km,api,D0,"minus_D0"))
    Es=_sum(km,"complete_E_adjoint",As,_minus(km,api,Ds,"minus_D0_adjoint"))
    P0=_chain(km,"P0",X,G,X)
    JAJ=_chain(km,"J_A_J",J,A,J)
    primal_poly=_sum(km,"J_plus_JAJ",J,JAJ)
    U=_chain(km,"complete_U",Psi,primal_poly)
    Qstar=_chain(km,"complete_Qstar_collar",
        _sum(km,"minus_Jstar_plus_Jstar_A_Jstar",
             _minus(km,api,Js,"minus_Jstar"),_chain(km,"Jstar_A_Jstar",Js,A,Js)),Psi)
    P=_sum(km,"complete_primal_base",P0,U)
    Qs=_sum(km,"complete_dual_base_adjoint",P0,Qstar)
    trial=_chain(km,"complete_raw_trial",P,Bc)
    Cc=_chain(km,"complete_Cc",Gf,BLH)
    Wstar=_chain(km,"complete_dual_trial_adjoint",Cc,Qs)

    # Lc P0 = chi^2 Pi0 + k0. The genuine chi_prime remains in residuals.
    k0=_chain(km,"complete_k0",
        _sum(km,"Xp_minus_XE",Xp,_minus(km,api,_chain(km,"X_E",X,E),"minus_XE")),G,X)
    S=_sum(km,"complete_S_LcU_minus_Pc",
        _chain(km,"Psip_primal_poly",Psip,primal_poly),
        _minus(km,api,_chain(km,"Psi_Pb_A_J",Psi,Pb,A,J),"minus_Psi_Pb_A_J"),
        _minus(km,api,_chain(km,"Psi_A_J_A_J",Psi,A,J,A,J),"minus_Psi_A_J_A_J"))
    local_source=_sum(km,"chi2_Pi0_minus_Pb",
         _chain(km,"chi2_Pi0",X2,Pi0),_minus(km,api,Pb,"minus_Pb"))
    Rc=_chain(km,"complete_centre_primal_residual",
              _sum(km,"complete_primal_residual_base",local_source,k0,S),Bc)

    # Lc* Q - I is formed in the same ordinary pairing. Taking its true
    # body adjoint first avoids treating Gf's output atoms as absent inputs.
    dual_poly=_sum(km,"minus_J_plus_J_Astar_J",
         _minus(km,api,J,"minus_J"),_chain(km,"J_Astar_J",J,As,J))
    k0dual=_chain(km,"complete_k0_dual",
        _sum(km,"minus_Xp_minus_XEstar",_minus(km,api,Xp,"minus_Xp"),
             _minus(km,api,_chain(km,"X_Estar",X,Es),"minus_XEstar")),Gs,X)
    Sdual=_sum(km,"complete_Sdual",
        _minus(km,api,_chain(km,"Psip_dual_poly",Psip,dual_poly),"minus_Psip_dual_poly"),
        _chain(km,"Psi_Pb_Astar_J",Psi,Pb,As,J),
        _minus(km,api,_chain(km,"Psi_Astar_J_Astar_J",Psi,As,J,As,J),
               "minus_Psi_Astar_J_Astar_J"))
    dual_base=_sum(km,"complete_centre_dual_residual_base",local_source,k0dual,Sdual)
    Dcstar=_chain(km,"complete_centre_dual_residual_adjoint",
                 Cc,km.body_adjoint(dual_base,"complete_dual_base_star"))

    # WJK.14: chi_prime paths are cancelled exactly in THIS whole signed map.
    # They have not been removed from k0 or k0dual above.
    Fbb=_sum(km,"complete_Fbb",
        km.scaled_kernel(2*api.one,P0,"twice_P0"),
        km.scaled_kernel(-api.rational(1,2),_chain(km,"X3_G_X",X3,G,X),"minus_half_X3GX"),
        km.scaled_kernel(-api.rational(1,2),_chain(km,"X_G_X3",X,G,X3),"minus_half_XGX3"),
        _chain(km,"X_G_X2_E_G_X",X,G,X2,E,G,X))
    right_factor=_chain(km,"Pb_Id_minus_chi2Pi0",Pb,
        _sum(km,"Id_minus_chi2Pi0",I,
             _minus(km,api,_chain(km,"X2Pi0",X2,Pi0),"minus_X2Pi0")))
    cross=_sum(km,"complete_collar_cross",
        U,_chain(km,"Qstar_complete_right",Qstar,right_factor),
        _minus(km,api,_chain(km,"P0_S",P0,S),"minus_P0S"),
        _minus(km,api,_chain(km,"Qstar_k0_plus_S",Qstar,
                              _sum(km,"k0_plus_S",k0,S)),"minus_Qstar_k0S"))
    F=_sum(km,"complete_joint_F",Fbb,cross)
    inside=_sum(km,"joint_same_point_low_and_feedback",
                Mc,_chain(km,"complete_BLH_F_Bc",BLH,F,Bc))
    Hc=_chain(km,"complete_joint_signed_centre",Gf,inside)
    require(Hc.atom_count==193 and Dcstar.atom_count==193 and Wstar.atom_count==193,
            "all low root/outer observations transported once")
    return {"J":J,"Jstar":Js,"P0":P0,"U":U,"Qstar":Qstar,"Fbb":Fbb,
            "Fcross":cross,"F":F,"trial":trial,"Rc":Rc,"Dcstar":Dcstar,
            "Wstar":Wstar,"Cc":Cc,"Hc":Hc,
            "all_other_ports_remain_in_complete_owner_contract":True}


def complete_primal_graph(api,norms,operators,old,emit):
    """All five kernels cover full input and output; source weights are paid."""
    values={}
    keys=("trial_raw","centre_collar_source","centre_body_source",
          "family_collar_source","family_body_source")
    for key,prefix in zip(keys,PRIMAL_TRIPLES):
        values[key]=norms.complete(operators[key],emit,prefix)
    rho_c=emit("complete_primal_collar_source_upper",api.upper(
        values["centre_collar_source"]+values["family_collar_source"]))
    rho_b=emit("complete_primal_body_source_upper",api.upper(
        values["centre_body_source"]+values["family_body_source"]))
    error=emit("complete_high_state_error_upper",
               api.upper(old["C_c"]*rho_c+old["C_b"]*rho_b))
    return {"raw_trial":values["trial_raw"],"rho_c":rho_c,"rho_b":rho_b,"E":error}


def complete_dual_graph(api,norms,operators,emit):
    """Adjoint norms equal Z -> L2 H1, not the raw L2 high-state norm.

    Each passed map is d_piece^* composed with the COMPLETE input Lambda
    factor. Its output contains all of Z's body and atomic coordinates.
    """
    values={}
    keys=("centre_collar_dual","centre_body_dual",
          "family_collar_dual","family_body_dual")
    for key,prefix in zip(keys,DUAL_TRIPLES):
        values[key]=norms.complete(operators[key],emit,prefix)
    dc=emit("complete_dual_collar_residual_upper",api.upper(
        values["centre_collar_dual"]+values["family_collar_dual"]))
    db=emit("complete_dual_body_residual_upper",api.upper(
        values["centre_body_dual"]+values["family_body_dual"]))
    delta=emit("complete_dual_residual_upper",api.upper(api.sqrt(dc*dc+db*db)))
    return {"delta_c":dc,"delta_b":db,"delta":delta}


def complete_family_graph(api,norms,operators,primal,dual,emit):
    """The three full signed/family operators in W2C.26; no old error subtraction."""
    values={}
    keys=("low_family_feedback","cross_family_feedback","trial_family_feedback")
    for key,prefix in zip(keys,FAMILY_TRIPLES):
        values[key]=norms.complete(operators[key],emit,prefix)
    feedback=emit("complete_dual_feedback_error_upper",api.upper(dual["delta"]*primal["E"]))
    epsilon=emit("complete_head_paired_error_upper",api.upper(
        values["low_family_feedback"]+values["cross_family_feedback"]+
        values["trial_family_feedback"]+feedback))
    return {"dual_feedback":feedback,"epsilon":epsilon}


def complete_signed_centre_graph(norms,operators,emit):
    # norms receives the ENTIRE same-point signed Hc map, never separate norms.
    value=norms.complete(operators["joint_signed_centre"],emit,"complete_joint_signed_centre")
    return {"K":value}


def complete_finite_graph(api,old,centre,family,emit):
    """Complete same-reference finite test; T is an old literal read, not recomputed."""
    e_rho=old["complete_reference_rho_defect_upper"]
    q=old["complete_reference_inverse_norm_upper"]
    eps_b=old["complete_outer_paired_error_upper"]
    o_H=old["complete_head_endpoint_correction_upper"]
    o_b=old["complete_outer_endpoint_correction_upper"]
    T=old["complete_actual_T_upper"]
    w0=api.rational(6,5)
    head=centre["K"]+family["epsilon"]
    E0=emit("complete_actual_E0_upper",api.upper(e_rho+(api.one+e_rho)*
            api.sqrt(w0*w0*head*head+eps_b*eps_b)+
            api.sqrt(w0*w0*o_H*o_H+o_b*o_b)))
    D=emit("complete_actual_D_upper",api.upper((api.one+e_rho)*head+o_H))
    defect=emit("complete_actual_finite_defect_upper",api.upper(E0+3*D*T))
    passed=bool(defect<api.one)
    answer={"E0":E0,"D":D,"T_old":T,"defect":defect,"passed":passed,
            "false_sufficient_gate_is_not_singularity":True,
            "all_four_blocks_and_both_right_hand_sides_retained":True}
    if passed:
        gap=emit("complete_actual_finite_gap_lower",api.lower(api.one-defect),endpoint="lower")
        inverse=emit("complete_actual_finite_inverse_upper",api.upper(q/gap))
        answer.update({"gap":gap,"inverse":inverse})
    return answer


def evaluate_five_complete_graphs(api,norms,operators,old,owner):
    """One ordered first evaluation; owner.emit is durable before returned readback.

    owner.start_graph must atomically save its empty complete-prefix object.
    Every emit adds the actual new ball to that same object, fsyncs and prints
    it, re-reads the canonical saved record, and only then returns a directed
    endpoint. finish_graph preserves all qualifications and the full record map.
    The owner catches exceptions and retains every complete/partial graph.
    """
    name=GRAPH_NAMES[0];emit=owner.start_graph(name,record_names(name))
    primal=complete_primal_graph(api,norms,operators,old,emit);owner.finish_graph(name)
    name=GRAPH_NAMES[1];emit=owner.start_graph(name,record_names(name))
    dual=complete_dual_graph(api,norms,operators,emit);owner.finish_graph(name)
    name=GRAPH_NAMES[2];emit=owner.start_graph(name,record_names(name))
    family=complete_family_graph(api,norms,operators,primal,dual,emit);owner.finish_graph(name)
    name=GRAPH_NAMES[3];emit=owner.start_graph(name,record_names(name))
    centre=complete_signed_centre_graph(norms,operators,emit);owner.finish_graph(name)
    name=GRAPH_NAMES[4];emit=owner.start_graph(name,record_names(name,True))
    result=complete_finite_graph(api,old,centre,family,emit)
    owner.finish_graph(name,passed=result["passed"])
    return result


def complete_weighted_graph_operators(api,km,ctx,signed,family_fees,old):
    """All complete norm legs without evaluating a high-rank residual DAG.

    The centre residual comparisons use the exact cancelled collar equations.
    Whole signed local/cross matrices and complete finite Fourier A0 words
    give their private angular norms. The joint Hc map is kept signed separately.
    """
    domain=ctx.domain;n=len(domain.cells)
    require(all(key in family_fees and len(family_fees[key])==n
                for key in ("AL","HL","LH","A_primal","A_adjoint")),
            "all complete collar and body family error fields")
    require(len(ctx.parent_indices)==n and set(ctx.parent_indices)==set(range(153)),
            "all genuine parent pieces in comparison domain")
    require(len(ctx.S_inverse_norms)==n,"complete physical right S inverse")
    positive=complete_positive_residual_base(api,km,ctx)
    head="physical_scaled_head193_L2";low="raw_low193_L2"
    high224="raw_high224_L2";high288="raw_high288_L2";high416="raw_high416_L2"
    source="complete_high_source_Hminus_two_thirds"
    state="complete_high_state_Hminus_one"
    Y="scaled_head193_body_and_all_193_observations"
    pc=[api.one if p==0 else api.zero for p in ctx.parent_indices]
    pb=[api.zero if p==0 else api.one for p in ctx.parent_indices]
    def diag(values,inp,out,label):
        return km.PointwiseNormComparison(domain,values,inp,out,label)
    def chain(label,*ops):
        result=ops[-1]
        for i in range(len(ops)-2,-1,-1):
            result=km.PositiveComposition(ops[i],result,label+":"+str(i))
        return result
    def mask(operator,values,label):
        return chain(label,diag(values,operator.output_space,operator.output_space,label+":mask"),
                     operator)
    raw_trial,raw_green,raw_Wstar=(positive[key] for key in ("trial","Gf","Wstar"))
    delta_A=diag(family_fees["A_primal"],high224,high416,"full_delta_A_input224")
    delta_B=diag([api.upper(a*s) for a,s in zip(family_fees["HL"],ctx.S_inverse_norms)],
                 head,high416,"full_delta_BHL_Sinverse")
    raw_family_source=km.PositiveSum((
        chain("full_delta_A_trial",delta_A,raw_trial),delta_B),
        "complete_raw_delta_A_trial_plus_delta_B")
    source_factor=old["lambda_388_minus_two_thirds"]
    family_source=chain("whole_family_source_window",
        diag([source_factor]*n,high416,source,"old_complete_source_window"),raw_family_source)
    centre_source=chain("whole_centre_source_window",
        diag([source_factor]*n,high288,source,"old_complete_centre_source_window"),positive["Rc"])
    # True d* Lambda. The whole centre output is <=288, while the family
    # output is <=416; those distinct Riesz costs are not interchanged.
    centre_riesz=diag([api.rational(1153)]*n,state,high288,"whole_Lambda288_majorant")
    centre_collar_dual=chain("whole_centre_collar_H1_dual",positive["Dcstar"],
        diag(pc,high288,high288,"Pc_on_H288"),centre_riesz)
    centre_body_dual=chain("whole_centre_body_H1_dual",positive["Dcstar"],
        diag(pb,high288,high288,"Pb_on_H288"),centre_riesz)
    delta_A_dual=diag(family_fees["A_adjoint"],high416,high224,
                     "true_P224_delta_A_input416_from_adjoint_input224")
    delta_C=chain("full_delta_C",raw_green,
        diag(family_fees["LH"],high416,low,"whole_delta_BLH"))
    raw_family_dual=km.PositiveSum((
        chain("full_Wstar_delta_A",raw_Wstar,delta_A_dual),delta_C),
        "complete_raw_family_dual_adjoint")
    family_riesz=diag([api.rational(1665)]*n,state,high416,"whole_Lambda416_majorant")
    family_collar_dual=chain("whole_family_collar_H1_dual",raw_family_dual,
        diag(pc,high416,high416,"Pc_on_H416"),family_riesz)
    family_body_dual=chain("whole_family_body_H1_dual",raw_family_dual,
        diag(pb,high416,high416,"Pb_on_H416"),family_riesz)
    low_family=chain("complete_low_family_feedback",raw_green,
        diag([api.upper(a*s) for a,s in zip(family_fees["AL"],ctx.S_inverse_norms)],
             head,low,"whole_delta_AL_Sinverse_with_mean"))
    cross_family=chain("complete_cross_family_feedback",raw_green,
        diag(family_fees["LH"],high224,low,"whole_delta_BLH_on_trial224"),raw_trial)
    trial_family=chain("complete_trial_family_feedback",raw_Wstar,raw_family_source)
    return {
        "trial_raw":raw_trial,
        "centre_collar_source":mask(centre_source,pc,"whole_collar_centre_source"),
        "centre_body_source":mask(centre_source,pb,"whole_body_centre_source"),
        "family_collar_source":mask(family_source,pc,"whole_collar_family_source"),
        "family_body_source":mask(family_source,pb,"whole_body_family_source"),
        "centre_collar_dual":centre_collar_dual,"centre_body_dual":centre_body_dual,
        "family_collar_dual":family_collar_dual,"family_body_dual":family_body_dual,
        "low_family_feedback":low_family,"cross_family_feedback":cross_family,
        "trial_family_feedback":trial_family,
        "joint_signed_centre":signed["Hc"],
    }


def _complete_modal_norm_comparison(api,km,ctx,low,input_space,output_space):
    """Whole modal L2 bound with O(N^2) SCALAR tiles, never dense modal kernels."""
    domain=ctx.domain;profiles=ctx.reference_profiles;n=len(domain.cells)
    modes=tuple(range(1,97)) if low else tuple(range(97,161))
    boxes=[domain.whole_cell_box(i) for i in range(n)]
    # These exact reference profiles are nonnegative.  This positive
    # comparison needs only upper numbers: take directed upper POINTS
    # before products/squares.  Multiplying broad nonnegative symmetric
    # balls can otherwise represent a mathematically nonnegative product
    # with a negative lower endpoint (R139 positive-product supplement).
    values={j:[{name:api.upper(value[name]) for name in ("p","H","K","g")}
               for value in (profiles.at(j,box) for box in boxes)] for j in modes}
    def complete_max(values_):
        return max(api.upper(x) for x in values_)
    def decay_upper(j,i,k):
        # The two variable end pieces have true decay <=1. The complete
        # intervening cells retain their original ordered product.
        if i==k:
            return api.one
        lo,hi=min(i,k),max(i,k)
        return api.upper(profiles.mode[j]["products"].between(lo+1,hi))
    def tile(i,k):
        answers=[]
        q=api.upper(ctx.reference_qs[i]) if low else api.one
        for j in modes:
            vr,vs=values[j][i],values[j][k]
            if i>=k:
                answers.append(decay_upper(j,i,k)*api.sqrt(
                    (vr["p"]*vr["p"]+q*q)*(vs["H"]*vs["H"]+vs["K"]*vs["K"])))
            if i<=k:
                answers.append(decay_upper(j,i,k)*api.sqrt(
                    (vr["K"]*vr["K"]+q*q*vr["H"]*vr["H"])*
                    (api.one+vs["p"]*vs["p"])))
        if low and i<=k:
            answers.append(api.magnitude(q))
        return complete_max(answers)
    def atoms(k):
        # The complete modal root/outer rows are one Hilbert observation
        # block. The independent physical mean root row has norm1.
        answers=[api.one]
        for j in modes:
            v=values[j][k]
            root=api.upper(v["g"])
            outer=api.upper(api.upper(ctx.reference_thetas[j])*
                            api.upper(profiles.to_right(j,boxes[k])))
            p,H,K=(api.upper(v[key]) for key in ("p","H","K"))
            rows=complete_max((root*(api.one+p),outer*(H+K)))
            cols=complete_max((root+outer*H,root*p+outer*K))
            answers.append(api.sqrt(rows*cols))
        return complete_max(answers)
    return km.CompleteScalarKernelComparison(domain,input_space,output_space,tile,
        atom_callback=atoms if low else None,
        label="whole_low_Gf_all193_observations" if low else "whole_high_G0")


def _complete_private_centre_norms(api,km,ctx):
    """Private finite-Fourier coefficient fees for this NEW residual candidate.

    A0 below is the actual finite Laurent coefficient sum of the signed centre,
    never a WGS scalar-sup record renamed A0. The two high primitive factors
    have degree32; their intermediate nonzero index is at least65, hence1/260.
    The complete cross matrices are signed before their Schur norm is taken.
    """
    n=len(ctx.domain.cells);caps={key:[] for key in
        ("A160","A224","Astar160","Astar224","E160","Estar160","B","C")}
    h160=tuple((c,j) for c in (0,1) for j in range(97,161))
    lactive=tuple((c,j) for c in (0,1) for j in range(33,97))
    cache={}
    def a0(poly):
        return api.upper(sum((api.magnitude(v) for v in poly.values()),api.zero))
    for i in range(n):
        parent=ctx.parent_indices[i]
        if parent not in cache:
            p=ctx.centre_packets[parent]
            drift=a0(p["d"])
            dphi=api.upper(sum((4*abs(j)*api.magnitude(v) for j,v in p["d"].items()),api.zero))
            local=sum((a0(p[name]) for name in ("la","le","ell","Kell")),api.zero)
            aa=sum((a0(q) for q in p["a"]),api.zero)
            bb=sum((a0(q) for q in p["b"]),api.zero)
            primitive=2*aa*bb/260
            eta=api.magnitude(p["actual_eta"]);curvature=api.magnitude(p["K"])
            principal=eta*max(api.upper(api.one),api.upper(curvature))
            ep=ctx.reference_etas[i];q=ctx.reference_qs[i]
            delta_principal=max(api.upper(api.magnitude(p["actual_eta"]-ep)),
                api.upper(api.magnitude(p["actual_eta"]*p["K"]-ep*q*q)))
            rest=local+primitive
            value={
              "A160":api.upper(640*(principal+drift)+rest),
              "A224":api.upper(896*(principal+drift)+rest),
              "Astar160":api.upper(640*(principal+drift)+dphi+rest),
              "Astar224":api.upper(896*(principal+drift)+dphi+rest),
              "E160":api.upper(640*(delta_principal+drift)+rest),
              "Estar160":api.upper(640*(delta_principal+drift)+dphi+rest),
            }
            box=ctx.domain.whole_cell_box(i)
            B=ctx.centre_matrix(h160,lactive,box)
            B=km.Matrix(B.rows,B.cols,[
                [v/(q if lactive[k][0]==1 else api.one) for k,v in enumerate(row)]
                for row in B.values])
            C=ctx.centre_matrix(lactive,h160,box)
            value["B"]=km.matrix_norm_upper(api,B)
            value["C"]=km.matrix_norm_upper(api,C)
            cache[parent]=value
        for key in caps:
            caps[key].append(cache[parent][key])
    return caps


def complete_positive_residual_base(api,km,ctx):
    """Complete scalar comparisons of the full trial/residual maps.

    This avoids evaluating any concatenated-rank semiseparable residual.
    Exact collar cancellation and every transition term are taken FIRST;
    the remaining true operators are bounded by ordered whole-space maps.
    Only the joint signed-centre target is excluded from this positive route.
    """
    domain=ctx.domain;n=len(domain.cells)
    cap=_complete_private_centre_norms(api,km,ctx)
    H={b:"raw_high"+str(b)+"_L2" for b in (160,224,288,416)}
    head="physical_scaled_head193_L2";low="raw_low193_L2"
    Y="scaled_head193_body_and_all_193_observations"
    one=[api.one]*n
    pc=[api.one if p==0 else api.zero for p in ctx.parent_indices]
    pb=[api.zero if p==0 else api.one for p in ctx.parent_indices]
    boxes=[domain.whole_cell_box(i) for i in range(n)]
    cut=[ctx.cutoff(box) for box in boxes]
    chi=[api.upper(api.magnitude(v[0])) for v in cut]
    xp=[api.upper(api.magnitude(v[1])) for v in cut]
    psi=[api.upper(api.magnitude(v[2])) for v in cut]
    psip=[api.upper(api.magnitude(v[3])) for v in cut]
    local=[api.upper(api.magnitude(v[0]*v[0]-pb[i])) for i,v in enumerate(cut)]
    def mul(values,space,label):
        return km.PointwiseNormComparison(domain,values,space,space,label)
    def change(inp,out,label):
        return km.PointwiseNormComparison(domain,one,inp,out,label)
    def coeff(key,inp,out):
        return km.PointwiseNormComparison(domain,cap[key],inp,out,"complete_centre_"+key)
    def chain(label,*ops):
        result=ops[-1]
        for i in range(len(ops)-2,-1,-1):
            result=km.PositiveComposition(ops[i],result,label+":"+str(i))
        return result
    def plus(label,*ops):
        return km.PositiveSum(ops,label)
    J={}
    for b in (160,224,288):
        J[b]=km.CompleteScalarKernelComparison(domain,H[b],H[b],
            lambda i,j:api.one if ctx.parent_indices[j]==0 else api.zero,
            label="complete_true_Jc_on_"+str(b))
    Js={b:km.CompletePositiveAdjoint(J[b],"complete_true_Jc_star_to_R_"+str(b))
        for b in J}
    G=_complete_modal_norm_comparison(api,km,ctx,False,H[160],H[160])
    Gf=_complete_modal_norm_comparison(api,km,ctx,True,low,Y)
    B=coeff("B",head,H[160]);C=coeff("C",H[160],low)
    A160=coeff("A160",H[160],H[224]);A224=coeff("A224",H[224],H[288])
    # Norms of the exact adjoint restrictions, not a false reuse of A160.
    Ato160=coeff("Astar160",H[224],H[160])
    Ato224=coeff("Astar224",H[288],H[224])
    E160=coeff("E160",H[160],H[224])
    Eto160=coeff("Estar160",H[224],H[160])
    c160=mul(chi,H[160],"chi160")
    P0=chain("complete_P0_comparison",c160,G,c160)
    primal_poly=plus("whole_J_plus_JAJ_on160",
        chain("whole_J160_in224",change(H[160],H[224],"embedding160to224"),J[160]),
        chain("whole_J224_A160_J160",J[224],A160,J[160]))
    trial_base=plus("whole_primal_base",
        chain("whole_P0_in224",change(H[160],H[224],"embeddingP0"),P0),
        chain("whole_psi_primal_poly",mul(psi,H[224],"psi224"),primal_poly))
    trial=chain("complete_raw_trial_comparison",trial_base,B)

    # The complete Rc local term is chi^2-Pb; it is EXACTLY zero on Pc.
    local_r=chain("whole_Rc_local",change(H[160],H[288],"embeddinglocal"),
                  mul(local,H[160],"absolute_chi2_minus_Pb"))
    kfactor=plus("whole_Xprime_minus_chiE",
        chain("Xp_in224",change(H[160],H[224],"embeddingXp"),mul(xp,H[160],"Xp")),
        chain("chiE160",mul(chi,H[224],"chi224"),E160))
    k0=chain("whole_k0_in288",change(H[224],H[288],"embeddingk0"),
             kfactor,G,c160)
    s1=chain("whole_psi_prime_primal_poly",change(H[224],H[288],"embeddingS1"),
             mul(psip,H[224],"Psip224"),primal_poly)
    s2=chain("whole_psi_Pb_A_J",change(H[224],H[288],"embeddingS2"),
             mul([api.upper(x*y) for x,y in zip(psi,pb)],H[224],"psiPb224"),
             A160,J[160])
    s3=chain("whole_psi_A_J_A_J",mul(psi,H[288],"psi288"),A224,J[224],A160,J[160])
    Rc=chain("complete_centre_Rc_comparison",plus("whole_Rc_base",local_r,k0,s1,s2,s3),B)

    Cc=chain("complete_Gf_BLH",Gf,C)
    # W*=Cc[P0+(-J*+J* A J*)psi], with input224 and complete193 outputs.
    qstar=plus("whole_Qstar_collar",
        chain("whole_minus_Jstar",Js[160],change(H[224],H[160],"project224to160"),
              mul(psi,H[224],"right_psi224")),
        chain("whole_Jstar_A_Jstar",Js[160],Ato160,Js[224],
              mul(psi,H[224],"right_psi224_second")))
    Wstar=chain("complete_dual_trial_adjoint_comparison",Cc,
        plus("whole_Wstar_base",
             chain("whole_P0_from224",P0,change(H[224],H[160],"P0_projection")),
             qstar))

    # Exact d_c^* before the positive comparison. The full H1 input weight
    # is applied later. Every A-to160/A-to224 is its TRUE adjoint restriction.
    d0=chain("whole_dual_local",mul(local,H[160],"dual_absolute_chi2_minus_Pb"),
             change(H[288],H[160],"dual_local_projection"))
    dkfactor=plus("whole_dual_Xprime_plus_Echi",
        chain("dual_Xp",mul(xp,H[160],"dual_Xp160"),
              change(H[224],H[160],"dual_Xp_projection")),
        chain("dual_Echi",Eto160,mul(chi,H[224],"dual_right_chi224")))
    dk=chain("whole_dual_k0star",c160,G,dkfactor,
             change(H[288],H[224],"dual_k0_projection"))
    d1=chain("whole_dual_Jstar_psiprime",Js[160],
             change(H[288],H[160],"dual_first_projection"),
             mul(psip,H[288],"dual_psiprime288"))
    d2=chain("whole_dual_Jstar_A_Jstar_psiprime",Js[160],Ato160,Js[224],
             change(H[288],H[224],"dual_second_projection"),
             mul(psip,H[288],"dual_psiprime288_second"))
    d3=chain("whole_dual_Jstar_A_Pbpsi",Js[160],Ato160,
             change(H[288],H[224],"dual_third_projection"),
             mul([api.upper(x*y) for x,y in zip(psi,pb)],H[288],"dual_Pbpsi"))
    d4=chain("whole_dual_Jstar_A_Jstar_A_psi",Js[160],Ato160,Js[224],Ato224,
             mul(psi,H[288],"dual_right_psi288"))
    Dcstar=chain("complete_centre_dual_residual_comparison",Cc,
                plus("whole_dual_residual_base",d0,dk,d1,d2,d3,d4))
    return {"trial":trial,"Rc":Rc,"Wstar":Wstar,"Dcstar":Dcstar,
            "Gf":Gf,"J":J,"Jstar":Js,"caps":cap,
            "complete_centre_positive_comparison_after_cancellation":True}


class CompleteGraphNorms:
    """One declared whole comparison per target; no alternate-parameter search."""
    def __init__(self,api,km,ctx):
        self.api,self.km,self.ctx=api,km,ctx
        self.used=set()

    def complete(self,operator,emit,prefix):
        require(prefix not in self.used,"a whole new norm target is evaluated once")
        self.used.add(prefix)
        if isinstance(operator,CompleteJointCentreColumns):
            require(prefix=="complete_joint_signed_centre",
                    "the compressed columns represent only the complete joint centre")
            return operator.complete_schur(self.ctx.signed_centre_schur_weights,
                                           emit,prefix,self.ctx.progress)["norm"]
        if isinstance(operator,self.km.SignedKernel):
            require(prefix=="complete_joint_signed_centre",
                    "only the complete signed centre uses this componentwise receiver")
            weights=self.ctx.signed_centre_schur_weights
            result=self.km.whole_signed_kernel_schur(
                operator,weights["input"],weights["body"],weights["atoms"],
                emit,prefix,progress=self.ctx.progress)
            return result["norm"]
        return self.km.complete_positive_comparison_norm(operator,emit,prefix)


# Standard-library exact definition materialization only. No old producer or
# numerical package is imported by this module.
from fractions import Fraction
from bisect import bisect_right
from math import isqrt
import hashlib
import json


def _q(api,value):
    value=Fraction(value)
    return api.rational(value.numerator,value.denominator)


def _canonical_exact(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode("utf-8")


def _max_upper(api,values):
    values=[api.upper(x) for x in values]
    require(values,"nonempty complete positive comparison")
    return max(values)


def _same_parent_mesh(literals):
    root_lower=Fraction(literals["rstar_interval"][0])
    cut=Fraction(literals["c_body"]);right=Fraction(literals["R"])
    rho=cut-root_lower
    require(rho>0,"same genuine root/collar ordering")
    result=[{"kind":"collar","left":None,"right":cut,"length_upper":rho}]
    left=cut
    for band in range(20):
        if left==right:
            break
        end=min(right,root_lower+2*rho)
        require(left<end,"complete body doubling band")
        for sub in range(8):
            lo=left+(end-left)*sub/8;hi=left+(end-left)*(sub+1)/8
            result.append({"kind":"body","left":lo,"right":hi,"length_upper":hi-lo,
                           "band":band,"subcell":sub})
        left=end;rho*=2
    require(left==right and len(result)==153,"same complete original153-parent definition")
    return result


def _same_reference_intrinsic(intrinsic,api,display):
    centres={name:display(intrinsic[name],name+"/ball")
             for name in ("beta","K","gamma","Cref")}
    selected=dict(centres);choices={"beta":"ball_centre"}
    signs={"K":1,"gamma":1,"Cref":-1}
    fallback={"K":Fraction(1,64),"gamma":Fraction(1),"Cref":Fraction(-1)}
    for name,sign in signs.items():
        actual=api.old_interval(intrinsic[name])
        require(api.lower(actual)>0 if sign>0 else -api.lower(-actual)<0,
                "original signed intrinsic domain")
        low=display(intrinsic[name]["lower"],name+"/lower")
        high=display(intrinsic[name]["upper"],name+"/upper")
        candidates=(("ball_centre",centres[name]),("endpoint_display_midpoint",(low+high)/2),
                    ("lower_display_centre",low),("upper_display_centre",high),
                    ("fixed_signed_reference",fallback[name]))
        label,value=next((label,value) for label,value in candidates if sign*value>0)
        selected[name]=value;choices[name]=label
    return selected,centres,choices


def _same_reference_definition(cubic,rows,midpoint,api,display):
    row_index=next(i for i,row in enumerate(rows)
                   if Fraction(row["interval"][0])<=midpoint<Fraction(row["interval"][1]))
    intrinsic=rows[row_index]["original_intrinsic_enclosure"]
    ref,centres,selection=_same_reference_intrinsic(intrinsic,api,display)
    require(ref["K"]>0 and ref["Cref"]<0 and ref["gamma"]>0,
            "same positive exact reference selection")
    scale=1<<20
    q=Fraction(max(scale//8,isqrt((ref["K"].numerator*scale*scale)//ref["K"].denominator)),scale)
    piece=bisect_right(cubic.nodes,midpoint)-1
    require(0<=piece<6144,"same original exact cubic piece")
    alpha=Fraction("6890507429876859/9007199254740992")
    physical=[alpha*x for x in cubic.exact_values(piece,midpoint)]
    physical[32]+=1/ref["Cref"]
    eta=-ref["gamma"]*physical[32]
    ui={j:Fraction(0) for j in range(-32,33)}
    vr=dict(ui);vr[0]=physical[32]
    for j in range(1,33):
        ui[j]=-physical[j-1]/2;ui[-j]=physical[j-1]/2
        vr[j]=vr[-j]=physical[32+j]/2
    definition={"midpoint":str(midpoint),"original_row":row_index,"original_piece":piece,
        "intrinsic_centres":{k:str(v) for k,v in ref.items()},
        "intrinsic_display_centres":{k:str(v) for k,v in centres.items()},
        "intrinsic_reference_selection":selection,
        "intrinsic_selected_values_are_reference_only":True,
        "complete_actual_minus_reference_difference_retained":True,
        "q":str(q),"eta":str(eta),
        "u_imag_laurent":[str(ui[j]) for j in range(-32,33)],
        "v_real_laurent":[str(vr[j]) for j in range(-32,33)],
        "repair_reference_is_zero":True,"actual_repair_enclosure_retained":True}
    identity={k:v for k,v in definition.items() if k not in ("u_imag_laurent","v_real_laurent")}
    require(len(_canonical_exact(identity))<=8192,
            "whole exact reference identity is bounded before kernel arithmetic")
    return {"q_exact":q,"eta_exact":eta,"intrinsic_exact":ref,
            "u_exact":ui,"v_exact":vr,"reference_identity":identity,
            "reference_hash":hashlib.sha256(_canonical_exact(definition)).hexdigest()}


def _same_exact_tracefree_diagonal(packet, j, c, zero):
    """Exact rational signed diagonal recipe; mean and eta are NOT deleted.

    packet is the complete frozen degree32 reference, with rational local
    fields and primitive factors. This routine handles j>0 only. The true
    mean row belongs to the separate unchanged mean branch. The actual
    generator minus this declared reference is charged in full elsewhere.
    """
    require(type(j) is int and 1 <= j <= 96, "true nonzero low mode")
    require(type(c) is Fraction and type(zero) is Fraction and zero == 0,
            "exact rational definition carrier")
    require(c >= zero, "nonnegative exact reference speed")
    for name in ("d", "la", "le"):
        require(all(type(k) is int and abs(k) <= 64 and type(v) is Fraction
                    for k,v in packet[name].items()),
                "complete local degree64 reference")
    require(len(packet["a"]) == 2 and len(packet["b"]) == 2,
            "both complete ordered primitive factors")
    require(all(type(k) is int and abs(k) <= 32 and type(v) is Fraction
                for family in (packet["a"], packet["b"])
                for poly in family for k,v in poly.items()),
            "both complete primitive degree32 supports")
    get = lambda poly, k: poly.get(k, zero)
    odd = get(packet["la"], 0) - get(packet["la"], 2*j) - (4*j)*get(packet["d"], 2*j)
    even = get(packet["le"], 0) + get(packet["le"], 2*j) + (4*j)*get(packet["d"], 2*j)
    for intermediate in range(1, j+33):
        ao = get(packet["a"][0], j-intermediate) - get(packet["a"][0], j+intermediate)
        ae = get(packet["a"][1], j-intermediate) - get(packet["a"][1], j+intermediate)
        bo = get(packet["b"][0], intermediate-j) - get(packet["b"][0], intermediate+j)
        be = get(packet["b"][1], intermediate-j) + get(packet["b"][1], intermediate+j)
        odd -= 2*ao*bo/(4*intermediate)
        even -= 2*ae*be/(4*intermediate)
    signed = (odd-even)/2
    selected = max(-c/32, min(signed, c/16))
    require(-c/32 <= selected <= c/16, "exact signed tracefree clipping")
    if c == zero:
        require(selected == zero, "root zero-rate diagonal")
    return {"odd_diagonal": odd, "even_diagonal": even,
            "unclipped_tracefree": signed, "selected": selected}



def _same_exact_reference_coefficients(definition):
    """Exact rational reference definition; no interval norm or old target."""
    zero=Fraction(0)
    ui=definition["u_exact"];vr=definition["v_exact"]
    beta=definition["intrinsic_exact"]["beta"]
    curvature=definition["intrinsic_exact"]["K"]
    def add(a,b):
        return {j:a.get(j,zero)+b.get(j,zero) for j in set(a)|set(b)}
    def scale(a,k):
        return {j:k*v for j,v in a.items()}
    def conv(a,b):
        out={j:zero for j in range(min(a)+min(b),max(a)+max(b)+1)}
        for j,x in a.items():
            for k,y in b.items():out[j+k]+=x*y
        return out
    u2=scale(conv(ui,ui),-1);v2=conv(vr,vr);uv=conv(ui,vr)
    S=add(u2,scale(v2,curvature))
    la=scale(add(scale(u2,3),scale(v2,curvature)),-beta)
    le=scale(add(u2,scale(v2,3*curvature)),-beta)
    la[0]-=beta;le[0]+=beta
    ell=scale(uv,-2*beta)
    return {"d":{j:(beta*S[j]/(4*j) if j else zero) for j in S},
        "la":la,"le":le,"ell":ell,"Kell":scale(ell,curvature),
        "a":[{j:-4*j*beta*ui[j] for j in ui},
             {j:4*j*beta*vr[j] for j in vr}],
        "b":[dict(ui),scale(vr,curvature)]}


def _body_centre_fields(cubic,repair,piece,left,right,intrinsic,api):
    exact=lambda q:_q(api,q)
    interval=lambda lo,hi:api.interval(exact(lo),exact(hi))
    values=cubic.polynomial_values(piece,left,right,exact,interval)
    alpha=exact("6890507429876859/9007199254740992")
    require(len(values)==65 and len(repair)==65,"whole original65 centre")
    physical=[alpha*x+interval(-Fraction(repair[k]),Fraction(repair[k]))
              for k,x in enumerate(values)]
    cr=api.old_interval(intrinsic["Cref"])
    require(-api.lower(-cr)<0,"same negative body Cref")
    physical[32]+=api.one/cr
    ui={j:api.zero for j in range(-32,33)}
    vr=dict(ui);vr[0]=physical[32]
    for j in range(1,33):
        ui[j]=-physical[j-1]/2;ui[-j]=physical[j-1]/2
        vr[j]=vr[-j]=physical[32+j]/2
    return ui,vr


def _family_panel_values(collar,fees,api):
    return {
        "AL":collar.family_l2_fallback(fees,api,input_last=96,adjoint=False,
                                       include_mean_rank=True),
        "HL":collar.family_l2_fallback(fees,api,input_last=96,adjoint=False,
                                       include_mean_rank=False),
        "LH":collar.family_l2_fallback(fees,api,input_last=96,adjoint=True,
                                       include_mean_rank=False),
        "A_primal":collar.family_l2_fallback(fees,api,input_last=224,adjoint=False,
                                              include_mean_rank=False),
        "A_adjoint":collar.family_l2_fallback(fees,api,input_last=224,adjoint=True,
                                               include_mean_rank=False),
    }



def _complete_signed_centre_matrix(api,km,collar,packet,outputs,inputs,sqrt_two):
    """One complete normalized-real matrix, with ordered primitive factorization.

    The primitive is -2 A I B on its ENTIRE positive intermediate band.
    Matrix multiplication is interval signed arithmetic; no norm, absolute
    value or intermediate Fourier projection is inserted. The genuine full
    physical mean row overwrites the whole local-plus-primitive row.
    """
    outputs,inputs=tuple(outputs),tuple(inputs)
    if not outputs or not inputs:
        return km.zeros(api,len(outputs),len(inputs))
    first=max(1,min(k for _,k in outputs)-32,min(j for _,j in inputs)-32)
    last=min(max(k for _,k in outputs)+32,max(j for _,j in inputs)+32)
    local=km.Matrix(len(outputs),len(inputs),[
        [collar._local_signed_entry(packet,o,i,sqrt_two,api.zero)
         for i in inputs] for o in outputs])
    if first<=last:
        middle=tuple(range(first,last+1))
        left=km.Matrix(len(outputs),len(middle),[
            [collar.multiplier_entry(packet["a"][o[0]],0 if o[0]==0 else 1,
                o,(0,m),sqrt_two,api.zero) for m in middle] for o in outputs])
        right=km.Matrix(len(middle),len(inputs),[
            [collar.multiplier_entry(packet["b"][i[0]],1 if i[0]==0 else 0,
                (1,m),i,sqrt_two,api.zero)/(4*m) for i in inputs] for m in middle])
        local=km.add(api,local,km.scale(api,-2*api.one,km.multiply(api,left,right)))
    values=[list(row) for row in local.values]
    for row,o in enumerate(outputs):
        if o==(1,0):
            values[row]=[collar._centre_mean_row(packet,i,sqrt_two,api.zero) for i in inputs]
    return km.Matrix(len(outputs),len(inputs),values)

def _cutoff_boxes(api,left,right,cut,outer):
    width=Fraction(1,16);up_end=cut+width;down_start=outer-width
    require(cut<up_end<down_start<outer,"same two disjoint original cutoff transitions")
    def enclose(lo,hi):
        return api.interval(_q(api,lo),_q(api,hi))
    def bump(a,b,sign):
        f=lambda t:3*t*t-2*t*t*t
        d=lambda t:6*t*(1-t)/width
        candidates=[d(a),d(b)]
        if a<=Fraction(1,2)<=b:
            candidates.append(d(Fraction(1,2)))
        lo,hi=min(candidates),max(candidates)
        return enclose(f(a),f(b)),enclose(lo,hi) if sign==1 else enclose(-hi,-lo)
    if right<=cut:
        return api.zero,api.zero,api.one,api.zero
    if cut<=left<=right<=up_end:
        a=(left-cut)/width;b=(right-cut)/width
        chi,derivative=bump(a,b,1)
        # This is the exact complement function, not a separate guessed cutoff.
        psi=enclose(1-(3*b*b-2*b*b*b),1-(3*a*a-2*a*a*a))
        return chi,derivative,psi,-derivative
    if up_end<=left<=right<=down_start:
        return api.one,api.zero,api.zero,api.zero
    if down_start<=left<=right<=outer:
        chi,derivative=bump((outer-right)/width,(outer-left)/width,-1)
        return chi,derivative,api.zero,api.zero
    raise ValueError("comparison panels must contain both cutoff joins")


class _Context:
    pass


def prepare_complete_kernel_context(api,km,reference,collar,admitted,provider,old,
                                    display,progress):
    """Complete private materialization, never an old completed norm target.

    The supplied pure reader has already admitted both new whole natives,
    all19 original restores, every original body row, both orders, all seams,
    the original repair, and the immutable full WVC provider. The exact same
    reference definition and selected-diagonal chains are re-identified here.
    The actual collar packet is never the old zero reference packet.
    """
    require(admitted["collar_inputs_verified"] is True,
            "complete signed collar admission before numerical materialization")
    rows=admitted["rows"];cubic=admitted["cubic"]
    repair=admitted["repair_suprema"];literals=admitted["literals"]
    require(len(rows)==4650 and len(repair)==65,"whole admitted old body and repair")
    parents=_same_parent_mesh(literals)
    root_interval=tuple(map(Fraction,literals["rstar_interval"]))
    cut=Fraction(literals["c_body"]);outer=Fraction(literals["R"])
    require(outer==Fraction(25,8),"same genuine outer endpoint")
    definitions=[None]
    selected=[{j:Fraction(0) for j in range(1,97)}]
    chain="947c13032e6e6dc6496e42d2a78b0178b41dbc4372069a321f3f501a07547df7"
    diagonal_chain=hashlib.sha256(b"complete_WVC_root_diagonal_is_zero_v1").hexdigest()
    for i,parent in enumerate(parents[1:],1):
        definition=_same_reference_definition(cubic,rows,(parent["left"]+parent["right"])/2,
                                              api,display)
        packet=_same_exact_reference_coefficients(definition)
        values={j:_same_exact_tracefree_diagonal(packet,j,
            4*j*abs(definition["eta_exact"]),Fraction(0))["selected"] for j in range(1,97)}
        definitions.append(definition);selected.append(values)
        chain=hashlib.sha256(bytes.fromhex(chain)+bytes.fromhex(definition["reference_hash"])).hexdigest()
        raw=_canonical_exact({str(j):str(values[j]) for j in range(1,97)})
        diagonal_chain=hashlib.sha256(bytes.fromhex(diagonal_chain)+hashlib.sha256(raw).digest()).hexdigest()
        progress("same_exact_reference_definition",{"parents_verified":i+1,
            "reference_chain":chain,"selected_diagonal_chain":diagonal_chain,
            "old_bound_targets_recomputed":0})
    require({"count":153,"sha256":chain}==reference.REFERENCE_CHAIN==provider["reference_chain"]
            and {"count":153,"sha256":diagonal_chain}==reference.DIAGONAL_CHAIN==
                provider["reference_selection"]["selected_diagonal_chain"],
            "both complete original fixed-WVC chains")
    root_packet=collar.complete_true_collar_packet(admitted,api)
    root_fees=_family_panel_values(collar,
        collar.complete_family_positive_fees(root_packet,api),api)
    packets=[root_packet];family=[root_fees]
    cursor=0;seen=set();intersections=0
    for i,parent in enumerate(parents[1:],1):
        left,right=parent["left"],parent["right"]
        while cursor<len(rows) and Fraction(rows[cursor]["interval"][1])<=left:
            cursor+=1
        row_index=cursor;covered=left
        ui_all=vr_all=intrinsic_all=None
        fees_all={name:api.zero for name in root_fees}
        while row_index<len(rows) and Fraction(rows[row_index]["interval"][0])<right:
            row=rows[row_index]
            lo=max(left,Fraction(row["interval"][0]))
            hi=min(right,Fraction(row["interval"][1]))
            require(lo==covered and lo<hi,"every closed parent/row intersection")
            intrinsic=row["original_intrinsic_enclosure"]
            ui,vr=_body_centre_fields(cubic,repair,row["original_candidate_piece"],
                                     lo,hi,intrinsic,api)
            values={"beta":api.old_interval(intrinsic["beta"]),
                    "K":api.old_interval(intrinsic["K"]),
                    "gamma":api.old_interval(intrinsic["gamma"]),
                    "eta":api.old_interval(row["complete_delta_bounds"]["radial_speed"])}
            require(api.lower(values["K"])>0 and api.lower(values["eta"])>0,
                    "same actual positive body principal")
            if ui_all is None:
                ui_all,vr_all,intrinsic_all=dict(ui),dict(vr),dict(values)
            else:
                for target,new in ((ui_all,ui),(vr_all,vr)):
                    for j,value in new.items():
                        target[j]=api.hull([target[j],value])
                for name,value in values.items():
                    intrinsic_all[name]=api.hull([intrinsic_all[name],value])
            rowfees=_family_panel_values(collar,
                collar.complete_body_family_positive_fees(row,api,
                    same_actual_eta_retained=True),api)
            for name,value in rowfees.items():
                fees_all[name]=_max_upper(api,(fees_all[name],value))
            covered=hi;seen.add(row_index);intersections+=1
            if covered==right:
                break
            row_index+=1
        require(covered==right and ui_all is not None,"whole original body parent")
        cursor=row_index
        packet=collar._complete_centre_packet(ui_all,vr_all,intrinsic_all["beta"],
            intrinsic_all["K"],intrinsic_all["gamma"],intrinsic_all["eta"],api.zero)
        packets.append(packet);family.append(fees_all)
        progress("complete_new_centre_parent",{"parents_complete":i+1,
            "closed_rows_covered":len(seen),"closed_intersections":intersections,
            "same_actual_eta_retained":True,"new_trial_input_band":224,
            "full_family_output_band":416})
    require(len(packets)==153 and len(seen)==4650 and intersections==4801,
            "all original rows and continuous family intersections")
    panels=[];parent_indices=[]
    split_points=(cut+Fraction(1,16),outer-Fraction(1,16))
    for i,parent in enumerate(parents):
        if i==0:
            parts=[(None,cut)]
        else:
            points=[parent["left"]]+[x for x in split_points
                if parent["left"]<x<parent["right"]]+[parent["right"]]
            parts=list(zip(points,points[1:]))
        for left,right in parts:
            panels.append({"left":left,"right":right,"parent_index":i})
            parent_indices.append(i)
    require(len(panels)<=155 and set(parent_indices)==set(range(153)),
            "same full comparison cover plus cutoff joins")
    domain=km.RadialDomain(api,panels,root_interval,Fraction(0),Fraction(1))
    etas=[api.zero if i==0 else _q(api,abs(definitions[i]["eta_exact"]))
          for i in parent_indices]
    qs=[api.one if i==0 else _q(api,definitions[i]["q_exact"]) for i in parent_indices]
    diagonals=[{j:_q(api,selected[i][j]) for j in range(1,97)} for i in parent_indices]
    identity={"kind":"complete_fixed_WVC_signed_reference_identity_v1",
        "complete_original_WVC_file":dict(reference.WVC_ACTUAL_FILE),
        "original_reference_chain":dict(reference.REFERENCE_CHAIN),
        "selected_diagonal_chain":dict(reference.DIAGONAL_CHAIN),
        "same_original_D_S_and_true_root":True,
        "all_original_parent_definitions_verified":True,
        "no_completed_bound_target_recomputed":True,
        "scalar_trace_identically_zero":True,"reference_outer_impedance":"13/80",
        "fine_refinement":160,"fine_cell_count":24480,
        "finite_normalizer_rule":"rho2=1+h^2*(a^2+c^2*q^2)/12"}
    profiles=reference.prepare_signed_reference_profiles(api,domain,etas,qs,
        diagonals,parent_indices,identity)
    head=tuple((0,j) for j in range(1,97))+((1,0),)+tuple((1,j) for j in range(1,97))
    high=tuple((0,j) for j in range(97,289))+tuple((1,j) for j in range(97,289))
    thetas={j:api.rational(1+16*j*j)**api.rational(-5,12) for j in range(1,97)}
    Gf=reference.complete_signed_reference_kernel(api,domain,profiles,tuple(range(1,97)),
        qs,thetas,True,True,km,coordinates=head,label="same_fixed_WVC_full_Gf")
    G0=reference.complete_signed_reference_kernel(api,domain,profiles,tuple(range(97,161)),
        [api.one for _ in panels],thetas,False,False,km,coordinates=high,
        label="same_fixed_WVC_G0_zero_extension")
    reciprocal=old["reciprocal_sqrt_two"]
    # Both enclosures come from the same original reciprocal record. No new
    # public sqrt2 target is evaluated, nor is an upper used as a lower.
    sqrt_two=api.interval(api.lower(api.one/reciprocal),-api.lower(-(2*reciprocal)))
    require(api.lower(sqrt_two)>0,"whole sqrt2 from the complete original reciprocal record")
    def packet_at(box):
        return packets[parent_indices[domain.cell_index(box)]]
    def scalar_map(coords,evaluate,label):
        n=len(coords)
        field=km.Field(domain,n,n,lambda box:km.scale(api,evaluate(box),km.eye(api,n)),label)
        return km.multiplication(domain,coords,coords,field,label)
    def constant_diag(coords,values,label):
        matrix=km.Matrix(len(coords),len(coords),[
            [values[i] if i==j else api.zero for j in range(len(coords))]
            for i in range(len(coords))])
        return km.multiplication(domain,coords,coords,
            km.constant_field(domain,matrix,label),label)
    def centre_map(outputs,inputs,label,cross=None):
        cache={}
        def evaluate(box):
            cell=domain.cell_index(box)
            if cell in cache:
                return cache[cell]
            packet=packet_at(box)
            active_outputs=tuple(o for o in outputs
                if cross!="HL" or o[1]<=160)
            active_outputs=tuple(o for o in active_outputs
                if cross!="LH" or o[1]>32)
            active_inputs=tuple(q for q in inputs
                if cross!="HL" or q[1]>32)
            active_inputs=tuple(q for q in active_inputs
                if cross!="LH" or q[1]<=160)
            whole=_complete_signed_centre_matrix(api,km,collar,packet,
                active_outputs,active_inputs,sqrt_two)
            ro={o:i for i,o in enumerate(active_outputs)}
            ci={q:i for i,q in enumerate(active_inputs)}
            result=km.Matrix(len(outputs),len(inputs),[
                [whole.values[ro[o]][ci[q]] if o in ro and q in ci else api.zero
                 for q in inputs] for o in outputs])
            if len(cache)>=2:
                cache.pop(next(iter(cache)))
            cache[cell]=result
            return result
        return km.multiplication(domain,outputs,inputs,
            km.Field(domain,len(outputs),len(inputs),evaluate,label),label)
    def reference_map(coords,low,label):
        def evaluate(box):
            i=domain.cell_index(box);eta,q=etas[i],qs[i]
            values=[]
            for oc,k in coords:
                row=[]
                for ic,j in coords:
                    value=api.zero
                    if j==k and j and (low or j<=160):
                        if oc!=ic:
                            value=4*j*eta*(q*q if oc==0 else api.one)
                        elif low:
                            value=diagonals[i][j] if oc==0 else -diagonals[i][j]
                    row.append(value)
                values.append(row)
            return km.Matrix(len(coords),len(coords),values)
        return km.multiplication(domain,coords,coords,
            km.Field(domain,len(coords),len(coords),evaluate,label),label)
    def cutoff(box,index):
        i=domain.cell_index(box)
        if parent_indices[i]==0:
            return (api.zero,api.zero,api.one,api.zero)[index]
        left,right=domain.exact_physical_cover(box)
        return _cutoff_boxes(api,left,right,cut,outer)[index]
    I=constant_diag(high,[api.one]*len(high),"identity_on_complete_H288")
    Pc=scalar_map(high,lambda box:api.one if parent_indices[domain.cell_index(box)]==0
                  else api.zero,"true_collar_mask")
    Pb=scalar_map(high,lambda box:api.zero if parent_indices[domain.cell_index(box)]==0
                  else api.one,"true_body_mask")
    Pi0=constant_diag(high,[api.one if j<=160 else api.zero for _,j in high],"Pi97through160")
    X=scalar_map(high,lambda box:cutoff(box,0),"original_chi")
    Xp=scalar_map(high,lambda box:cutoff(box,1),"complete_original_chi_prime")
    X2=scalar_map(high,lambda box:cutoff(box,0)**2,"same_chi_squared")
    X3=scalar_map(high,lambda box:cutoff(box,0)**3,"same_chi_cubed")
    Psi=scalar_map(high,lambda box:cutoff(box,2),"complete_collar_psi")
    Psip=scalar_map(high,lambda box:cutoff(box,3),"complete_collar_psi_prime")
    def sinverse(box):
        q=qs[domain.cell_index(box)]
        return km.Matrix(len(head),len(head),[
            [((api.one if component==0 else api.one/q) if i==j else api.zero)
             for j in range(len(head))] for i,(component,k) in enumerate(head)])
    Sinv=km.multiplication(domain,head,head,
        km.Field(domain,len(head),len(head),sinverse,"same_actual_right_S_inverse"),
        "same_actual_right_S_inverse")
    Ac=centre_map(high,high,"complete_centre_AHH")
    AL=centre_map(head,head,"complete_centre_ALL_with_physical_mean")
    D0=reference_map(high,False,"same_fixed_high_reference_on_Pi0")
    Df=reference_map(head,True,"same_complete_low_WVC_reference")
    Bc=_chain(km,"complete_BHLc_Sinverse",centre_map(high,head,"complete_BHLc","HL"),Sinv)
    BLH=centre_map(head,high,"complete_BLHc","LH")
    Mc=_chain(km,"complete_low_signed_remainder",
        _sum(km,"complete_ALc_minus_Df",AL,_minus(km,api,Df,"minus_Df")),Sinv)
    ctx=_Context();ctx.domain=domain;ctx.parent_indices=parent_indices
    ctx.S_inverse_norms=[_max_upper(api,(api.one,api.one/q)) for q in qs]
    ctx.progress=progress
    ctx.operators=dict(I=I,Pc=Pc,Pb=Pb,X=X,Xp=Xp,X2=X2,X3=X3,
        Psi=Psi,Psip=Psip,Pi0=Pi0,Ac=Ac,D0=D0,Bc=Bc,BLHc=BLH,Mc=Mc,G0=G0,Gf=Gf)
    ctx.qualifications={name:True for name in (
        "same_WVC_reference","same_actual_S_and_all_seven_ports",
        "all_coefficient_pieces_and_raw_identity_transmissions",
        "true_signed_collar_not_zero_reference_packet",
        "Bc_and_BLHc_external_support_160","trial_support_224",
        "centre_residual_support_288","whole_family_support_416",
        "ordinary_dr_pairing_and_complete_Gf_atoms")}
    ctx.signed_centre_schur_weights={
        "input":[[api.one if comp==0 else q for comp,j in head] for q in qs],
        "body":[[api.one if comp==0 else q for comp,j in head] for q in qs],
        "atoms":[api.one]*97+[thetas[j] for j in range(1,97)]}
    ctx.reference_identity=identity
    ctx.reference_profiles=profiles;ctx.reference_module=reference
    ctx.reference_qs=qs;ctx.reference_etas=etas;ctx.reference_diagonals=diagonals
    ctx.reference_thetas=thetas;ctx.centre_packets=packets;ctx.sqrt_two=sqrt_two
    ctx.collar_module=collar
    ctx.centre_matrix=lambda outputs,inputs,box: _complete_signed_centre_matrix(
        api,km,collar,packet_at(box),outputs,inputs,sqrt_two)
    ctx.cutoff=lambda box:tuple(cutoff(box,j) for j in range(4))
    ctx.parent_definition_count=153;ctx.original_body_row_count=len(seen)
    ctx.original_intersection_count=intersections
    ctx.family_fees={name:[family[i][name] for i in parent_indices] for name in root_fees}
    progress("complete_signed_kernel_inputs",{"parent_count":153,
        "comparison_cells":len(panels),"original_rows":4650,"closed_intersections":4801,
        "physical_head_dimension":193,"all_Gf_atoms":193,"true_signed_collar":True,
        "centre_trial_band":224,"centre_residual_band":288,"full_family_band":416,
        "old_completed_norm_targets_recomputed":0})
    return ctx


class CompleteJointCentreColumns:
    """WJK.7,13,14,21 through stable matrix-field actions, one source panel.

    This is an enclosure of the SAME signed kernel, not a new approximate
    inverse. All five collar terms are retained. Each source column contains
    the joint low remainder and feedback after ONE common Gf, before abs.
    Complete physical mean and all193 atoms are present in every column.

    The two external high supports are K0=97..160. The intermediate carrier
    K1=97..224 is exact for this projected joint map: each centre multiplication
    has bandwidth64 and each displayed word has at most three such factors.
    A path from K0 to K0 cannot pass outside K1 in a word of length <=3.
    This support observation does NOT truncate the actual inverse, the centre
    residual288, the family residual416, or any graph1--3 norm leg.

    G0 actions use the stable signed reference integral backend, with no
    division by a global decay and no growing semiseparable factor ranks.
    WholePanelIntegral handles true ordinary integrals, including J* to R.
    The source point remains a parameter in its entire original panel. The
    field enclosures include both triangles when source/output boxes overlap.
    """
    def __init__(self,api,km,ctx):
        self.api,self.km,self.ctx=api,km,ctx
        self.domain=ctx.domain;self.ref=ctx.reference_module
        self.K0=tuple((c,j) for c in (0,1) for j in range(97,161))
        self.K1=tuple((c,j) for c in (0,1) for j in range(97,225))
        self.low=ctx.operators["Gf"].inputs
        self.active=tuple((c,j) for c in (0,1) for j in range(33,97))
        self.low_position={x:i for i,x in enumerate(self.low)}
        self.k1_position={x:i for i,x in enumerate(self.K1)}
        self.k0_rows=[self.k1_position[x] for x in self.K0]
        self.active_columns=[self.low_position[x] for x in self.active]
        require(len(self.K0)==128 and len(self.K1)==256
                and len(self.low)==193 and len(self.active)==128,
                "complete joint-centre carriers and physical mean")
        self.Gf=ctx.operators["Gf"]
        self.G0=self.ref.complete_signed_reference_kernel(api,self.domain,
            ctx.reference_profiles,tuple(range(97,161)),
            [api.one for _ in self.domain.cells],ctx.reference_thetas,
            False,False,km,coordinates=self.K0,label="joint_column_raw_G0_128")
        require(self.Gf.atom_count==193 and self.G0.atom_count==0,
                "all low observations, no invented high atom")
        self.A10=self._centre_field(self.K1,self.K0,"joint_A10",cache_all=True)
        self.A00=self._field(128,128,
            lambda box:self._restrict_rows(self.A10.at(box)),"joint_A00_from_same_A10")
        self.A11=self._centre_field(self.K1,self.K1,"joint_A11")
        self.A01=self._centre_field(self.K0,self.K1,"joint_A01")
        self.BLH=self._centre_field(self.active,self.K0,"joint_BLH_active",cache_all=True)
        self.integral_A10=km.WholePanelIntegral(self.A10,"joint_collar_A_primitive")
        self.I0=km.eye(api,128)
        self.I10=self._embed_rows(self.I0)
        self.collar_right=self.domain.point(0,self.domain.fone)

    def _centre_field(self,outputs,inputs,label,cache_all=False):
        # The context provider uses one whole coefficient hull per original
        # parent; partial boxes do not alter it. Store the repeated A10 and
        # BLH fields once per parent, instead of reconstructing their signed
        # primitive factors for every source panel. A00 shares A10 scalars.
        # At most153 fixed-size matrices are retained by each complete cache.
        cache={}
        def at(box):
            key=self.ctx.parent_indices[self.domain.cell_index(box)]
            if key not in cache:
                if not cache_all and len(cache)>=2:
                    cache.pop(next(iter(cache)))
                cache[key]=self.ctx.centre_matrix(outputs,inputs,box)
            return cache[key]
        return self.km.Field(self.domain,len(outputs),len(inputs),at,label)

    def _embed_rows(self,matrix):
        require(matrix.rows==128,"full external K0 rows")
        zero=[self.api.zero]*matrix.cols
        lookup={target:source for source,target in enumerate(self.k0_rows)}
        return self.km.Matrix(256,matrix.cols,
            [list(matrix.values[lookup[i]]) if i in lookup else list(zero)
             for i in range(256)])

    def _restrict_rows(self,matrix):
        require(matrix.rows==256,"whole intermediate K1 carrier")
        return self.km.Matrix(128,matrix.cols,
                              [list(matrix.values[i]) for i in self.k0_rows])

    def _field(self,rows,cols,callback,label):
        return self.km.Field(self.domain,rows,cols,callback,label)

    def _is_collar(self,box):
        return self.ctx.parent_indices[self.domain.cell_index(box)]==0

    def _orientation(self,r,s):
        ri,si=self.domain.cell_index(r),self.domain.cell_index(s)
        if ri!=si:
            return 1 if ri>si else -1
        if r[1]>=s[2]:
            return 1
        if r[2]<=s[1]:
            return -1
        return 0

    def _reference_D0(self,box):
        api,km=self.api,self.km
        i=self.domain.cell_index(box)
        eta,q=self.ctx.reference_etas[i],self.ctx.reference_qs[i]
        position={x:i for i,x in enumerate(self.K0)}
        out=[[api.zero]*128 for _ in range(128)]
        for j in range(97,161):
            odd,even=position[(0,j)],position[(1,j)]
            out[odd][even]=4*j*eta*q*q
            out[even][odd]=4*j*eta
        return km.Matrix(128,128,out)

    def _Jstar(self,field,label,support=None):
        """Exactly Pc(r) int_r^R field, with only one cached body-tail matrix.

        The output lives on the FIRST collar panel. It does not need every
        ordinary suffix matrix. The optional support is an EXACT zero-support
        identity of this source field, not a numerical smallness threshold.
        """
        km,api=self.km,self.api
        tail=[]
        def evaluate(box):
            if not self._is_collar(box):
                return km.zeros(api,field.rows,field.cols)
            require(self.domain.cell_index(box)==0,"one complete genuine-root collar panel")
            if not tail:
                value=km.zeros(api,field.rows,field.cols)
                for i in range(1,len(self.domain.cells)):
                    whole=self.domain.whole_cell_box(i)
                    if support is None or support(whole):
                        value=km.add(api,value,km.scale(api,self.domain.full_length(i),
                                                       field.at(whole)))
                tail.append(value)
            part=self.domain.partial_box(box,"suffix")
            first=km.scale(api,self.domain.partial_length(box,"suffix"),field.at(part))
            return km.add(api,first,tail[0])
        return self._field(field.rows,field.cols,evaluate,label)

    def _collar_primitive(self,s,r):
        """A[s,r] for ordered collar points; caller retains the indicator."""
        require(self._is_collar(s) and self._is_collar(r),
                "both true variable-root collar boxes")
        return self.integral_A10.between(s,r)

    def _column(self,s):
        api,km,ctx=self.api,self.km,self.ctx
        source_collar=self._is_collar(s)
        xs,_,psis,_=ctx.cutoff(s)
        label="joint_source_panel_"+str(self.domain.cell_index(s))
        # A point source in K0, not in an invented discretized radial space.
        g=self._field(128,128,lambda r:self.G0.kernel(r,s,self._orientation(r,s)),
                      label+":G0_source")
        def e00(r):
            return km.add(api,self.A00.at(r),
                          km.scale(api,-api.one,self._reference_D0(r)))
        if source_collar:
            # chi(s)=0, hence Fbb and k0 vanish identically for these columns.
            body_feedback=None
            Tc=km.add(api,self.I10,self._collar_primitive(s,self.collar_right))
            def primitive_at(r):
                if not self._is_collar(r):
                    return Tc
                order=self._orientation(r,s)
                if order==-1:
                    return km.zeros(api,256,128)
                value=km.add(api,self.I10,self._collar_primitive(s,r))
                return km.hull(api,km.zeros(api,256,128),value) if order==0 else value
            def U(r):
                return km.scale(api,ctx.cutoff(r)[2],primitive_at(r))
            def S(r):
                if self._is_collar(r):
                    order=self._orientation(r,s)
                    if order==-1:
                        return km.zeros(api,256,128)
                    value=km.scale(api,-api.one,km.multiply(api,self.A11.at(r),
                                               self._collar_primitive(s,r)))
                    return km.hull(api,km.zeros(api,256,128),value) if order==0 else value
                _,_,psi,psip=ctx.cutoff(r)
                if api.upper(api.magnitude(psi))+api.upper(api.magnitude(psip))==0:
                    return km.zeros(api,256,128)
                return km.add(api,km.scale(api,psip,Tc),
                              km.scale(api,-psi,km.multiply(api,self.A11.at(r),Tc)))
            signed_S=self._field(256,128,S,label+":LcU_minus_Pc")
            def chi_S(r):
                chi=ctx.cutoff(r)[0]
                if api.upper(api.magnitude(chi))==0:
                    return km.zeros(api,128,128)
                return km.scale(api,chi,self._restrict_rows(signed_S.at(r)))
            P0Sforcing=self._field(128,128,chi_S,label+":chi_S")
            P0S=self.ref.apply_G_to_matrix_field(self.G0,P0Sforcing,km,label+":G_chi_S")
            def collar_and_body(r):
                return km.add(api,self._restrict_rows(U(r)),
                    km.scale(api,-ctx.cutoff(r)[0],P0S["body"].at(r)))
            tail_source=signed_S
        else:
            # Exact WJK.13--14. The two chi-prime paths are already cancelled.
            def chi2_E_G(r):
                chi=ctx.cutoff(r)[0]
                if api.upper(api.magnitude(chi))==0:
                    return km.zeros(api,128,128)
                return km.scale(api,chi**2,km.multiply(api,e00(r),g.at(r)))
            force=self._field(128,128,chi2_E_G,label+":chi2_E_G_source")
            body_feedback=self.ref.apply_G_to_matrix_field(
                self.G0,force,km,label+":G_chi2_E_G")
            def collar_and_body(r):
                xr=ctx.cutoff(r)[0]
                first=km.scale(api,xr*xs*(2*api.one-(xr*xr+xs*xs)/2),g.at(r))
                second=km.scale(api,xr*xs,body_feedback["body"].at(r))
                # V Pb(1-chi^2 Pi0), after the exact external Pi0 restriction.
                if self._is_collar(r) and api.upper(api.magnitude(psis))>0:
                    ar=self.integral_A10.between(r,self.collar_right)
                    vr=km.add(api,km.scale(api,-api.one,self.I0),self._restrict_rows(ar))
                    third=km.scale(api,psis*(api.one-xs*xs),vr)
                    return km.add(api,first,second,third)
                return km.add(api,first,second)
            def k0(r):
                xr,xp,_,_=ctx.cutoff(r)
                if api.upper(api.magnitude(xr))+api.upper(api.magnitude(xp))==0:
                    return km.zeros(api,256,128)
                raw=g.at(r)
                generator=km.add(api,km.multiply(api,self.A10.at(r),raw),
                    km.scale(api,-api.one,self._embed_rows(
                        km.multiply(api,self._reference_D0(r),raw))))
                return km.scale(api,xs,km.add(api,km.scale(api,xp,self._embed_rows(raw)),
                                              km.scale(api,-xr,generator)))
            tail_source=self._field(256,128,k0,label+":complete_k0")

        # V(k0+S) = -J* psi(k0+S) + J* A J* psi(k0+S).
        # J* keeps its whole transition/body tail; only its OUTPUT is on Pc.
        def psi_k0S(r):
            psi=ctx.cutoff(r)[2]
            if api.upper(api.magnitude(psi))==0:
                return km.zeros(api,256,128)
            return km.scale(api,psi,tail_source.at(r))
        weighted=self._field(256,128,psi_k0S,label+":psi_k0S")
        t0=self._Jstar(weighted,label+":true_Jstar_psi_k0S",
            support=lambda r:api.upper(api.magnitude(ctx.cutoff(r)[2]))>0)
        def A_Jstar(r):
            if not self._is_collar(r):
                return km.zeros(api,128,128)
            return km.multiply(api,self.A01.at(r),t0.at(r))
        t1=self._Jstar(self._field(128,128,A_Jstar,label+":A_Jstar_psi_k0S"),
            label+":true_Jstar_A_Jstar_psi_k0S",support=self._is_collar)
        def F(r):
            value=collar_and_body(r)
            if self._is_collar(r):
                value=km.add(api,value,self._restrict_rows(t0.at(r)),
                              km.scale(api,-api.one,t1.at(r)))
            return value

        # Bc includes the SAME physical S(s)^-1, including every even column.
        B=ctx.centre_matrix(self.K0,self.active,s)
        q=ctx.reference_qs[self.domain.cell_index(s)]
        B=km.Matrix(128,128,[[x if self.active[j][0]==0 else x/q
                             for j,x in enumerate(row)] for row in B.values])
        def low_forcing(r):
            active=km.product(api,self.BLH.at(r),F(r),B)
            out=[[api.zero]*128 for _ in range(193)]
            for k,row in zip(self.active_columns,active.values):
                out[k]=list(row)
            return km.Matrix(193,128,out)
        forcing=self._field(193,128,low_forcing,label+":complete_BLH_F_Bc")
        feedback=self.ref.apply_G_to_matrix_field(self.Gf,forcing,km,
                                                  label+":same_full_Gf_feedback")
        Mc=ctx.operators["Mc"].local.at(s)
        require(Mc.shape==(193,193),"complete low remainder and physical mean")
        def combine(direct,returned):
            require(direct.shape==(193,193) and returned.shape==(193,128),
                    "whole direct and feedback source columns")
            rows=[list(row) for row in direct.values]
            for a in range(193):
                for b,col in enumerate(self.active_columns):
                    rows[a][col]+=returned.values[a][b]
            return km.Matrix(193,193,rows)
        def body(r):
            direct=km.multiply(api,self.Gf.kernel(r,s,self._orientation(r,s)),Mc)
            return combine(direct,feedback["body"].at(r))
        def atoms():
            direct=km.multiply(api,self.Gf.atom_kernel(s),Mc)
            return combine(direct,feedback["atoms"]())
        return {"body":self._field(193,193,body,label+":joint_same_point_body"),
                "atoms":atoms,"physical_mean_and_all193_atoms":True,
                "whole_source_box":s}

    def complete_schur(self,weights,emit,prefix,progress=None):
        """Same continuous/atomic Schur test, traversed source-panel first.

        Every temporary column is released before the next source panel. No
        entire radial kernel matrix, completed array target or file is created.
        A completed column is a private portion of this one whole new norm.
        """
        api,km,domain=self.api,self.km,self.domain
        n=len(domain.cells);iw,bw,aw=weights["input"],weights["body"],weights["atoms"]
        require(len(iw)==len(bw)==n and all(len(w)==193 for w in iw+bw)
                and len(aw)==193 and all(api.lower(x)>0 for w in iw+bw+[aw] for x in w),
                "all complete positive physical Schur weights")
        iu=[[api.upper(x) for x in w] for w in iw]
        bu=[[api.upper(x) for x in w] for w in bw]
        au=[api.upper(x) for x in aw]
        lengths=[api.upper(domain.full_length(i)) for i in range(n)]
        native=hasattr(api,"arb_mat") and hasattr(api.zero,"abs_upper")
        if native:
            # python-flint arb.abs_upper returns an exact directed upper.
            # Native matrix-vector contractions avoid a Python scalar
            # multiplication/addition for every entry of every radial tile.
            native_input=[api.arb_mat([[x] for x in w]) for w in iu]
            native_body=[api.arb_mat([w]) for w in bu]
            native_atoms=api.arb_mat([au])
        def complete_weighted_sums(value,j,i=None):
            if native:
                absolute=api.arb_mat([[x.abs_upper() for x in row] for row in value.values])
                rr=absolute*native_input[j]
                cc=(native_atoms if i is None else native_body[i])*absolute
                # Finiteness of every nonnegative row/column sum is checked
                # here; a nonfinite entry cannot cancel in either contraction.
                return ([api.upper(rr[a,0]) for a in range(193)],
                        [api.upper(cc[0,b]) for b in range(193)])
            rr=[api.zero]*193;cc=[api.zero]*193
            observation=au if i is None else bu[i]
            for a in range(193):
                for b in range(193):
                    magnitude=api.upper(api.magnitude(value.values[a][b]))
                    rr[a]+=magnitude*iu[j][b]
                    cc[b]+=magnitude*observation[a]
            return [api.upper(x) for x in rr],[api.upper(x) for x in cc]
        rows=[[api.zero]*193 for _ in range(n)]
        columns=[[api.zero]*193 for _ in range(n)]
        atoms=[api.zero]*193
        for j in range(n):
            if progress is not None:
                progress("joint_source_panel_started",{"source_panel":j+1,"total":n,
                    "comparison_panels_not_finite_reference_cells":True})
            source=self._column(domain.whole_cell_box(j))
            hs=lengths[j]
            for i in range(n):
                hr=lengths[i]
                value=source["body"].at(domain.whole_cell_box(i))
                rr,cc=complete_weighted_sums(value,j,i)
                for a in range(193):
                    rows[i][a]+=hs*rr[a]
                    columns[j][a]+=hr*cc[a]
            value=source["atoms"]()
            rr,cc=complete_weighted_sums(value,j)
            for a in range(193):
                atoms[a]+=hs*rr[a]
                columns[j][a]+=cc[a]
            if progress is not None:
                progress("complete_joint_source_panel",{"completed":j+1,"total":n,
                    "whole_signed_low_and_feedback_combined_before_abs":True,
                    "all193_output_atoms_and_physical_mean_retained":True,
                    "temporary_columns_not_new_array_targets":True})
            del source
        row=max([api.upper(rows[i][a]/api.lower(bw[i][a]))
                 for i in range(n) for a in range(193)]+
                [api.upper(atoms[a]/api.lower(aw[a])) for a in range(193)])
        column=max(api.upper(columns[j][b]/api.lower(iw[j][b]))
                   for j in range(n) for b in range(193))
        row=emit(prefix+"_row_ratio_upper",row)
        column=emit(prefix+"_column_ratio_upper",column)
        norm=emit(prefix+"_norm_upper",api.sqrt(row*column))
        return {"row":row,"column":column,"norm":norm}
