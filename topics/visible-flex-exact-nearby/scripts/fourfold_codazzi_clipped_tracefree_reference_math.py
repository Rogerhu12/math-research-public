"""WVC complete clipped tracefree modal definitions and signed finite circuit.

No entry, numerical-package import, file access, old producer call, or execution.
The caller supplies admitted complete parent identities and the SAME WIC
physical coordinates. Exact diagonal materialization uses rational data.
Numerical preparation is only for genuinely changed reference modes.
"""
from fractions import Fraction


def require(ok, message):
    if not ok:
        raise ValueError(message)


def exact_tracefree_diagonal(packet, j, c, zero):
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


def _vectors(g, odd, even):
    n = g["n"]
    require(len(odd) == n and len(even) == n, "complete body vectors")
    return n


def prepare_tracefree_generators(api, j, h, c, reference_q, coordinate_q,
        sqrt_h, selected_a, theta, p_outer):
    """One complete signed circuit in the original physical Hilbert spaces.

    h/c/q/a are true complete coefficient enclosures of ONE reference.
    selected_a has already been chosen by exact rational clipping.
    No new physical basis or projection is introduced. No tau division.
    """
    require(type(j) is int and 1 <= j <= 96, "physical nonzero mode")
    n = len(h)
    require(n > 0 and all(len(x) == n for x in
            (c, reference_q, coordinate_q, sqrt_h, selected_a)),
            "one complete same-cell reference")
    require(reference_q is coordinate_q, "same admitted reference q and actual S objects")
    z, one = api.zero, api.one
    require(api.lower(theta)>0 and api.lower(p_outer)>=api.rational(1,16),
            "positive outer Riesz weight and complete impedance lower barrier")
    rho = []; transfer = []; forcing = []
    for i in range(n):
        require(api.lower(h[i]) > 0 and api.lower(reference_q[i]) >= api.rational(1,8)
                and api.lower(coordinate_q[i]) > 0 and api.lower(sqrt_h[i]) > 0,
                "same positive h/reference q/physical coordinate q")
        require(api.lower(c[i]) >= 0, "nonnegative complete reference speed")
        # The caller has checked clipping on the exact rational definition.
        # Numerical intervals enclose that definition; they do not select it.
        omega_squared = selected_a[i]*selected_a[i] + c[i]*c[i]*reference_q[i]*reference_q[i]
        x_squared = h[i]*h[i]*omega_squared
        normalizer = one + x_squared/12
        denominator = normalizer*normalizer - x_squared/4
        require(api.lower(denominator) > 0, "true positive Pade denominator")
        A_minus_one = x_squared/(2*denominator)
        A = one + A_minus_one
        B = h[i]*normalizer/denominator
        t11 = A+B*selected_a[i]
        t12 = B*c[i]*reference_q[i]*reference_q[i]
        t21 = B*c[i]
        t22 = A-B*selected_a[i]
        require(api.lower(t11) > 0 and api.lower(t22) > 0,
                "positive complete transfer diagonal")
        rho.append(normalizer)
        transfer.append((t11,t12,t21,t22))
        # T-Id is formed signed; no subtraction of independently saved uppers.
        forcing.append(((A_minus_one+B*selected_a[i],t12),
                        (t21,A_minus_one-B*selected_a[i])))
    p = [z for _ in range(n+1)]
    p[n] = p_outer
    tau = [z for _ in range(n)]
    sigma = [z for _ in range(n)]
    denominators = [z for _ in range(n)]
    backward_input = [None for _ in range(n)]
    direct_forward_input = [None for _ in range(n)]
    for i in range(n-1,-1,-1):
        t11,t12,t21,t22 = transfer[i]
        pn = p[i+1]
        den = t11+pn*t21
        require(api.lower(den) > 0, "complete positive impedance pivot")
        p[i] = (t12+pn*t22)/den
        require(api.lower(p[i]) > 0, "complete positive impedance")
        tau[i] = one/den
        sigma[i] = t21/den
        denominators[i] = den
        U = forcing[i]
        backward_input[i] = [-(U[0][k]+pn*U[1][k])/den for k in range(2)]
        direct_forward_input[i] = [(t11*U[1][k]-t21*U[0][k])/den for k in range(2)]
    H = [z for _ in range(n+1)]
    forward_input=[];forward_output=[];backward_output=[];local_output=[]
    half = one/2
    for i in range(n):
        tr = tau[i]
        H[i+1] = tr*tr*H[i]+sigma[i]
        b = backward_input[i]
        f = [tr*H[i]*b[k]+direct_forward_input[i][k] for k in range(2)]
        forward_input.append(f)
        K = one-p[i]*H[i]
        Kn = one-p[i+1]*H[i+1]
        forward_output.append([-half*(p[i]+tr*p[i+1]),half*(one+tr)])
        backward_output.append([half*(tr*K+Kn),half*(tr*H[i]+H[i+1])])
        local_output.append([
            [one+half*(K*b[0]-p[i+1]*f[0]),
                 half*(K*b[1]-p[i+1]*f[1])],
            [half*(H[i]*b[0]+f[0]),
             one+half*(H[i]*b[1]+f[1])]])
    return {"kind":"complete_clipped_tracefree_modal_generators_v1",
        "j":j,"n":n,"zero":z,"one":one,"transition":tau,
        "forward_input":forward_input,"backward_input":backward_input,
        "forward_output":forward_output,"backward_output":backward_output,
        "local_output":local_output,
        "input_odd":[one/sqrt_h[i] for i in range(n)],
        "input_even":[one/(sqrt_h[i]*coordinate_q[i]) for i in range(n)],
        "output_odd":[sqrt_h[i]/rho[i] for i in range(n)],
        "output_even":[sqrt_h[i]*coordinate_q[i]/rho[i] for i in range(n)],
        "end_from_odd":one,"end_from_even":p_outer,
        "outer_from_forward":theta,"outer_from_backward_end":theta*H[n],
        "outer_direct_even":-theta,"root_from_backward":one,
        "is_positive_majorant":False,"H":H,"p":p,"rho":rho,
        "denominators":denominators}


def apply_generators(g, f_odd, f_even, endpoint_odd, endpoint_even):
    n = _vectors(g, f_odd, f_even)
    zero = g["zero"]
    ro = [g["input_odd"][i] * f_odd[i] for i in range(n)]
    re = [g["input_even"][i] * f_even[i] for i in range(n)]
    backward = [zero for _ in range(n + 1)]
    backward[n] = g["end_from_odd"] * endpoint_odd + g["end_from_even"] * endpoint_even
    for i in range(n - 1, -1, -1):
        b = g["backward_input"][i]
        backward[i] = g["transition"][i] * backward[i + 1] + b[0] * ro[i] + b[1] * re[i]
    forward = [zero for _ in range(n + 1)]
    for i in range(n):
        a = g["forward_input"][i]
        forward[i + 1] = g["transition"][i] * forward[i] + a[0] * ro[i] + a[1] * re[i]
    out_odd = []
    out_even = []
    for i in range(n):
        F, G, D = g["forward_output"][i], g["backward_output"][i], g["local_output"][i]
        odd = F[0] * forward[i] + G[0] * backward[i + 1] + D[0][0] * ro[i] + D[0][1] * re[i]
        even = F[1] * forward[i] + G[1] * backward[i + 1] + D[1][0] * ro[i] + D[1][1] * re[i]
        out_odd.append(g["output_odd"][i] * odd)
        out_even.append(g["output_even"][i] * even)
    outer = (g["outer_from_forward"] * forward[n]
             + g["outer_from_backward_end"] * backward[n]
             + g["outer_direct_even"] * endpoint_even)
    return {"odd": out_odd, "even": out_even,
            "root_odd": g["root_from_backward"] * backward[0],
            "outer_weighted": outer}


def transpose_generators(g, u_odd, u_even, root_odd, outer_weighted):
    n = _vectors(g, u_odd, u_even)
    zero = g["zero"]
    ro = [zero for _ in range(n)]
    re = [zero for _ in range(n)]
    forward = [zero for _ in range(n + 1)]
    backward = [zero for _ in range(n + 1)]
    forward[n] += g["outer_from_forward"] * outer_weighted
    backward[n] += g["outer_from_backward_end"] * outer_weighted
    endpoint_even = g["outer_direct_even"] * outer_weighted
    backward[0] += g["root_from_backward"] * root_odd
    for i in range(n):
        odd = g["output_odd"][i] * u_odd[i]
        even = g["output_even"][i] * u_even[i]
        F, G, D = g["forward_output"][i], g["backward_output"][i], g["local_output"][i]
        forward[i] += F[0] * odd + F[1] * even
        backward[i + 1] += G[0] * odd + G[1] * even
        ro[i] += D[0][0] * odd + D[1][0] * even
        re[i] += D[0][1] * odd + D[1][1] * even
    for i in range(n - 1, -1, -1):
        value = forward[i + 1]
        forward[i] += g["transition"][i] * value
        a = g["forward_input"][i]
        ro[i] += a[0] * value
        re[i] += a[1] * value
    # forward[0] is the adjoint of a fixed zero, so is not a data coordinate.
    for i in range(n):
        value = backward[i]
        backward[i + 1] += g["transition"][i] * value
        b = g["backward_input"][i]
        ro[i] += b[0] * value
        re[i] += b[1] * value
    endpoint_odd = g["end_from_odd"] * backward[n]
    endpoint_even += g["end_from_even"] * backward[n]
    return {
        "odd": [g["input_odd"][i] * ro[i] for i in range(n)],
        "even": [g["input_even"][i] * re[i] for i in range(n)],
        "endpoint_odd": endpoint_odd, "endpoint_even": endpoint_even,
    }


def whole_positive_generator(g, absolute_upper):
    """Absolute values are taken after the complete signed local contractions."""
    result = {key: g[key] for key in ("n", "j", "zero", "one")}
    result.update({"kind": "same_WIC_whole_generator_majorant_v1",
                   "is_positive_majorant": True})

    def full(value):
        if isinstance(value, list):
            return [full(v) for v in value]
        return absolute_upper(value)

    for key in ("transition", "forward_input", "backward_input",
                "forward_output", "backward_output", "local_output",
                "input_odd", "input_even", "output_odd", "output_even",
                "end_from_odd", "end_from_even", "outer_from_forward",
                "outer_from_backward_end", "outer_direct_even",
                "root_from_backward"):
        result[key] = full(g[key])
    return result


def complete_weighted_generator_schur_sums(
        g, input_weights, output_weights, positive_lower, upper):
    """Whole weighted Schur sums for the unchanged Hilbert-space operator.

    positive_lower returns a finite, strictly positive directed point lower.
    upper returns a finite directed point upper. All weights enclose one
    declared positive vector; they are comparison weights, not new coordinates.
    """
    if g["is_positive_majorant"] is not True:
        raise ValueError("one entire positive generator required")
    if set(input_weights) != {"odd", "even", "endpoint_odd", "endpoint_even"}:
        raise ValueError("all complete input comparison weights required")
    if set(output_weights) != {"odd", "even", "root_odd", "outer_weighted"}:
        raise ValueError("all complete output comparison weights required")
    n = _vectors(g, input_weights["odd"], input_weights["even"])
    _vectors(g, output_weights["odd"], output_weights["even"])

    def endpoints(weights):
        highs, lows = {}, {}
        for key, value in weights.items():
            if key in ("odd", "even"):
                lows[key] = [positive_lower(v) for v in value]
                highs[key] = [upper(v) for v in value]
            else:
                lows[key] = positive_lower(value)
                highs[key] = upper(value)
        return highs, lows

    vu, vl = endpoints(input_weights)
    wu, wl = endpoints(output_weights)
    r = apply_generators(g, vu["odd"], vu["even"],
                         vu["endpoint_odd"], vu["endpoint_even"])
    c = transpose_generators(g, wu["odd"], wu["even"],
                             wu["root_odd"], wu["outer_weighted"])
    row_values = r["odd"] + r["even"] + [r["root_odd"], r["outer_weighted"]]
    row_lowers = wl["odd"] + wl["even"] + [wl["root_odd"], wl["outer_weighted"]]
    col_values = c["odd"] + c["even"] + [c["endpoint_odd"], c["endpoint_even"]]
    col_lowers = vl["odd"] + vl["even"] + [vl["endpoint_odd"], vl["endpoint_even"]]
    rows = [upper(upper(value) / lower) for value, lower in zip(row_values, row_lowers)]
    cols = [upper(upper(value) / lower) for value, lower in zip(col_values, col_lowers)]
    return {
        "complete_weighted_row_ratio_upper": max(rows),
        "complete_weighted_column_ratio_upper": max(cols),
        "complete_input_coordinates": 2 * n + 2,
        "complete_output_coordinates": 2 * n + 2,
        "comparison_weights_do_not_change_actual_Hilbert_coordinates": True,
        "matrix_allocations": 0,
    }


def complete_tracefree_reference_receivers(api,parent_lengths,parent_etas,parent_qs,
        selected_parent_diagonals,changed_modes,thetas,old_records,old_upper,
        emit,copy_old,commit_mode,refinement=160):
    """Seven new complete bounds, or seven verbatim copies if no mode changes.

    old_records contains the whole original WPS reference graph records.
    old_upper is their directed readback made by the owner before this call.
    commit_mode(j,running,witnesses,status) durably publishes the FULL prefix
    and returns its directed readback. For a copied-old witness the owner
    preserves its original complete record rather than formatting it again.
    """
    require(refinement==160 and len(parent_lengths)==153,
            "same inherited160 mesh of153 parents")
    require(len(parent_etas)==len(parent_qs)==len(selected_parent_diagonals)==153,
            "complete same parent definitions")
    require(set(changed_modes)==set(range(1,97)) and
            all(type(v) is bool for v in changed_modes.values()),
            "exact-definition changed/unchanged qualification")
    names={
        "q_row":"complete_reference_row_ratio_upper",
        "q_column":"complete_reference_column_ratio_upper",
        "rho_row":"complete_reference_rho_row_ratio_upper",
        "rho_column":"complete_reference_rho_column_ratio_upper",
        "odd_endpoint":"complete_reference_odd_endpoint_receiver_upper"}
    full_names=[names["q_row"],names["q_column"],names["rho_row"],names["rho_column"],
        "complete_reference_inverse_norm_upper","complete_reference_rho_defect_upper",
        names["odd_endpoint"]]
    require(all(k in old_records and k in old_upper for k in full_names) and
        "complete_reference_mean_endpoint_receiver_upper" in old_upper,
        "complete bound objects of the original actual reference")
    zero,one=api.zero,api.one
    def positive_lower(value):
        out=api.lower(value)
        require(out>0,"complete strictly positive comparison weight")
        return out
    require(set(thetas)==set(range(1,97)),"all original outer Riesz weights")
    require(all(set(packet)==set(range(1,97)) for packet in selected_parent_diagonals),
            "all complete selected parent modal definitions")
    if not any(changed_modes.values()):
        selected={key:copy_old(key,old_records[key]) for key in full_names}
        running={key:old_upper[name] for key,name in names.items()}
        witnesses={key:{"origin":"complete_old_reference_graph",
                        "record_key":name,"mode":None} for key,name in names.items()}
        saved=commit_mode(96,running,witnesses,
            {"changed_modes_completed":0,"unchanged_modes_qualified":96,
             "all_reference_targets_copied":True})
        require(set(saved)==set(running),"complete copied reference prefix")
        return {"q":selected["complete_reference_inverse_norm_upper"],
            "e_rho":selected["complete_reference_rho_defect_upper"],
            "q_o":selected[names["odd_endpoint"]],
            "q_m":old_upper["complete_reference_mean_endpoint_receiver_upper"],
            "w0":api.upper(api.rational(6,5)),"mode_prefix_count":96,
            "new_record_count":0,"copied_record_count":7,
            "finite_dimension":193*(153*160)+193,
            "reference_is_changed":False,"all_actual_spaces_unchanged":True}
    cell_h=[v/refinement for v in parent_lengths]
    parent_sqrt_h=[api.sqrt(v) for v in cell_h]
    h=[v for v in cell_h for _ in range(refinement)]
    root_h=[v for v in parent_sqrt_h for _ in range(refinement)]
    q=[v for v in parent_qs for _ in range(refinement)]
    n=len(h)
    vin_odd=list(root_h)
    vin_even=[root_h[i]*q[i] for i in range(n)]
    vin={"odd":vin_odd,"even":vin_even,"endpoint_odd":one,"endpoint_even":one}
    running={key:zero for key in names};witnesses={key:None for key in names}
    changed_count=0;unchanged_count=0
    for j in range(1,97):
        if not changed_modes[j]:
            # A restriction of the same old COMPLETE modal operator bound.
            candidate={key:old_upper[name] for key,name in names.items()}
            origin={key:{"origin":"copied_old_mode_bound","record_key":names[key],
                         "mode":j} for key in names}
            unchanged_count+=1
        else:
            parent_c=[(4*j)*v for v in parent_etas]
            parent_a=[selected_parent_diagonals[i][j] for i in range(153)]
            speed=[v for v in parent_c for _ in range(refinement)]
            a=[v for v in parent_a for _ in range(refinement)]
            g=prepare_tracefree_generators(api,j,h,speed,q,q,root_h,a,
                                         thetas[j],api.rational(13,80))
            positive=whole_positive_generator(g,api.magnitude)
            vout={"odd":vin_odd,"even":vin_even,"root_odd":one,"outer_weighted":thetas[j]}
            sums=complete_weighted_generator_schur_sums(
                positive,vin,vout,positive_lower,api.upper)
            candidate={"q_row":sums["complete_weighted_row_ratio_upper"],
                       "q_column":sums["complete_weighted_column_ratio_upper"]}
            parent_delta=[]
            for length,aa,cc,qq in zip(cell_h,parent_a,parent_c,parent_qs):
                xx=length*length*(aa*aa+cc*cc*qq*qq)
                parent_delta.append(min(api.upper(xx/12),api.upper(xx*xx/720)))
            delta=[v for v in parent_delta for _ in range(refinement)]
            rows=apply_generators(positive,
                [api.upper(vin_odd[i]*delta[i]) for i in range(n)],
                [api.upper(vin_even[i]*delta[i]) for i in range(n)],zero,zero)
            row_values=[api.upper(rows["odd"][i]/positive_lower(vin_odd[i])) for i in range(n)]
            row_values+=[api.upper(rows["even"][i]/positive_lower(vin_even[i])) for i in range(n)]
            row_values+=[api.upper(rows["root_odd"]),
                         api.upper(rows["outer_weighted"]/positive_lower(thetas[j]))]
            cols=transpose_generators(positive,vin_odd,vin_even,one,thetas[j])
            col_values=[api.upper(cols["odd"][i]*delta[i]/positive_lower(vin_odd[i]))
                        for i in range(n)]
            col_values+=[api.upper(cols["even"][i]*delta[i]/positive_lower(vin_even[i]))
                         for i in range(n)]
            candidate["rho_row"]=max(row_values)
            candidate["rho_column"]=max(col_values)
            endpoint=apply_generators(g,[zero]*n,[zero]*n,one/thetas[j],zero)
            total=sum((api.magnitude(v)**2 for v in endpoint["odd"]+endpoint["even"]+
                       [endpoint["root_odd"],endpoint["outer_weighted"]]),zero)
            candidate["odd_endpoint"]=api.upper(api.sqrt(total))
            origin={key:{"origin":"new_changed_mode","mode":j} for key in names}
            changed_count+=1
        for key,value in candidate.items():
            value=api.upper(value)
            if witnesses[key] is None or value>running[key]:
                running[key]=value;witnesses[key]=origin[key]
        saved=commit_mode(j,running,witnesses,
            {"changed_modes_completed":changed_count,
             "unchanged_modes_qualified":unchanged_count,
             "all_reference_targets_copied":False})
        require(set(saved)==set(running),"complete five-record modal prefix")
        running=dict(saved)
    qr=emit(names["q_row"],running["q_row"])
    qc=emit(names["q_column"],running["q_column"])
    er=emit(names["rho_row"],running["rho_row"])
    ec=emit(names["rho_column"],running["rho_column"])
    qbound=emit("complete_reference_inverse_norm_upper",
        max(api.upper(api.sqrt(qr*qc)),
            api.upper(one+old_upper["complete_reference_mean_endpoint_receiver_upper"])))
    erho=emit("complete_reference_rho_defect_upper",api.upper(api.sqrt(er*ec)))
    qo=emit(names["odd_endpoint"],running["odd_endpoint"])
    return {"q":qbound,"e_rho":erho,"q_o":qo,
        "q_m":old_upper["complete_reference_mean_endpoint_receiver_upper"],
        "w0":api.upper(api.rational(6,5)),"mode_prefix_count":96,
        "new_record_count":7,"copied_record_count":0,
        "finite_dimension":193*n+193,"reference_is_changed":True,
        "all_actual_spaces_unchanged":True}
