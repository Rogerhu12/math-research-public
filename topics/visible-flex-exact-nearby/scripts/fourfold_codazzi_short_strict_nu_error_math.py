"""SB: new short radial scalar cost, reusing the entire old SP matrix.

No IO, numerical import, old exponential matrix, PDE residual or old source
integral is evaluated.  The public owner supplies complete original rows.
"""
from fractions import Fraction

OUTPUT_ORDER = (
    "complete_base_short_reverse_radial_cost_upper",
    "complete_selected_short_reverse_radial_cost_upper",
    "complete_NP_selected_ordinary_error_source_upper",
    "complete_short_Hminus1_source_to_waist_density_upper",
    "complete_short_Hminus1_source_to_uniform_primitive_mean_upper",
    "complete_true_NP_short_waist_density_error_upper",
    "complete_true_NP_uniform_primitive_mean_error_upper",
    "complete_NP_selected_L1_L2_error_source_upper",
    "complete_short_L2_source_to_uniform_L2_upper",
    "complete_true_NP_uniform_L2_error_upper",
    "complete_true_NP_L2r_L2_error_upper",
)


def require(ok,message):
    if not ok:
        raise ValueError(message)


def exact(api,value):
    value = Fraction(value)
    return api.arb(value.numerator)/value.denominator


def nonnegative(value):
    require(value.is_finite() and value.lower() >= 0,"whole nonnegative existing scalar")
    return value.upper()


def complete_short_error(api,rows,read_ball,saved,publish):
    """SB.1--12: all source insertion times and the entire true NP error."""
    required = {"Jq","injection","waist_n_upper","waist_q_lower","whole_q_lower","whole_q_upper",
                "R","H0","H1","M0","M1","NC","old_D"}
    require(set(saved) == required and len(rows) == 7721,"entire original scalar inputs and all body rows")
    arb = api.arb;end = Fraction(9,50);edge = Fraction(0);cost = arb(0);count = 0
    for row in rows:
        left,right = map(Fraction,row["interval"])
        if left >= end:
            break
        upper = min(right,end)
        require(left == edge and left < upper,"full true short interval with no missing source insertion interval")
        midpoint,whole = row["intrinsic_midpoint_jets"],row["intrinsic_whole_third_jets"]
        K = read_ball(whole["K"])
        require(K.is_finite() and K.upper() < 0,"whole original negative curvature on each true short cell")
        centre = (left+right)/2
        radius = exact(api,left-centre).union(exact(api,upper-centre))
        maximum_radius = max(abs(left-centre),abs(upper-centre))
        radius2 = arb(0).union(exact(api,maximum_radius**2))
        Kprime = (read_ball(midpoint["K1"])+read_ball(midpoint["K2"])*radius
                    +read_ball(whole["K3"])*radius2/2)
        positive = Kprime.upper() if Kprime.upper() > 0 else arb(0)
        denominator = (-2*K).lower()
        require(denominator > 0,"strict complete curvature denominator")
        cost += exact(api,upper-left)*positive/denominator
        edge = upper;count += 1
    require(edge == end and count > 0,"all original short cells through exactly9/50")
    def save(index,value):return nonnegative(publish(OUTPUT_ORDER[index],value,"upper"))
    base_cost = save(0,cost)
    Jq,injection,nupper,R,H0,H1,M0,M1,NC,old_D = (nonnegative(saved[key]) for key in
        ("Jq","injection","waist_n_upper","R","H0","H1","M0","M1","NC","old_D"))
    selected_cost = save(1,base_cost+Jq)
    theta = exact(api,Fraction(936826,1000000))
    source = save(2,R+theta*(M1*H1+M0*H0)+theta*exact(api,Fraction(13,100)).sqrt()*NC)
    waist_q,whole_q = saved["waist_q_lower"].lower(),saved["whole_q_lower"].lower()
    require(waist_q > 0 and whole_q > 0,"whole original selected scalar lower bounds")
    # The complete old nonradial matrix has Frobenius norm <433/200;
    # every shorter product is already covered.  No old matrix runs again.
    reverse = (exact(api,Fraction(433,200))*selected_cost.exp()).upper()
    Cwaist = save(3,(nupper/waist_q.sqrt().lower())*reverse*injection)
    minimum_q = whole_q if whole_q < 1 else arb(1)
    Cprimitive = save(4,reverse*injection/minimum_q)
    new_D = (Cwaist*source).upper()
    save(5,new_D if new_D < old_D else old_D)
    save(6,Cprimitive*source)
    # Only the original centre residual has the true degree160 support.
    # The selected-operator and true-parameter differences were already
    # paid in full L2 and are retained in those units, without projection.
    source_L2 = save(7,641*R+theta*(M1*H1+M0*H0)+theta*exact(api,Fraction(13,100)).sqrt()*NC)
    q_upper = nonnegative(saved["whole_q_upper"])
    maximum_q = q_upper if q_upper > 1 else arb(1)
    # NR.8, at the ORIGINAL selected background: the same full P_minus
    # has ||D4 P_minus D4^-1||_F<437/200.  No nearby-centre fee is used.
    Cstrong = save(8,exact(api,Fraction(437,200))*selected_cost.exp()*maximum_q/minimum_q)
    uniform_L2 = save(9,Cstrong*source_L2)
    save(10,exact(api,end).sqrt()*uniform_L2)
    return {"complete_source_parent_rows_used":count,"exact_short_interval":["0","9/50"],
            "all_full_original_rows_admitted":7721,"old_nonradial_matrix_targets_evaluated":0,
            "old_NP_residual_or_source_integrals_evaluated":0,
            "degree160_factor_applies_only_to_original_centre_residual":True,
            "selected_operator_and_parameter_terms_keep_full_original_L2_units":True}

