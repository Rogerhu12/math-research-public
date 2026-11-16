"""WCTR complete clipped scalar-trace modal reference and signed circuit.

No entry point, numerical-package import, filesystem/network access, old
producer call, or execution. Every coefficient is admitted by the future
owner as a complete enclosure of one exact rational reference. The actual
mesh, physical S, root97/outer96 rows, mean, and actual high operator stay
fixed. Full matrix normalizers and two propagation directions are retained.
"""
from fractions import Fraction

def require(ok, message):
    if not ok:
        raise ValueError(message)

def exact_scalar_trace_diagonal(packet, j, c, zero, selected_tracefree):
    """New exact scalar-trace definition with the complete old a identity retained.

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
    require(type(selected_tracefree) is Fraction and selected_tracefree == selected,
            "complete same immutable WVC selected tracefree diagonal")
    signed_trace = (odd+even)/2
    clipped_trace = max(-c/64, min(signed_trace, c/64))
    require(-c/64 <= clipped_trace <= c/64, "exact signed scalar-trace clipping")
    if c == zero:
        require(clipped_trace == zero, "root exact zero trace")
    return {"odd_diagonal": odd, "even_diagonal": even,
            "unclipped_tracefree": signed, "selected_tracefree": selected,
            "unclipped_trace": signed_trace, "selected_trace": clipped_trace,
            "changed_from_WVC": clipped_trace != zero}

def _vectors(g, odd, even):
    n = g["n"]
    require(len(odd) == n and len(even) == n, "complete body vectors")
    return n

def _matvec(matrix, vector):
    return [matrix[i][0]*vector[0]+matrix[i][1]*vector[1] for i in range(2)]


def _matmul(left, right):
    return [[left[i][0]*right[0][k]+left[i][1]*right[1][k]
             for k in range(2)] for i in range(2)]


def prepare_scalar_trace_generators(api, j, h, c, reference_q, coordinate_q,
        sqrt_h, selected_a, selected_r, theta, p_outer):
    """Whole signed finite action in the original WVC physical coordinates.

    Exact clipping/definition identity is checked before this numerical
    function. Input balls enclose those exact definitions; intervals never
    select a new reference. P^-1 is multiplied into complete signed local
    output blocks before a positive majorant is formed. No tau division.
    """
    require(type(j) is int and 1 <= j <= 96, "physical nonzero low mode")
    n = len(h)
    require(n > 0 and all(len(v) == n for v in
            (c,reference_q,coordinate_q,sqrt_h,selected_a,selected_r)),
            "all complete same-cell reference arrays")
    require(reference_q is coordinate_q,
            "same admitted reference q and actual S objects")
    z,one = api.zero,api.one
    require(api.lower(theta)>0 and api.lower(p_outer)>=api.rational(1,16),
            "positive outer Riesz factor and complete impedance barrier")
    inverse_normalizers=[];transfer=[];determinants=[];forcing=[]
    for i in range(n):
        require(api.lower(h[i])>0 and api.lower(sqrt_h[i])>0
                and api.lower(reference_q[i])>=api.rational(1,8)
                and api.lower(coordinate_q[i])>0 and api.lower(c[i])>=0,
                "complete positive length, scale, q and nonnegative speed")
        aa,rr,cc,qq,hh=selected_a[i],selected_r[i],c[i],reference_q[i],h[i]
        omega2=aa*aa+cc*cc*qq*qq
        alpha=one+hh*hh*(rr*rr+omega2)/12
        beta=hh*hh*rr/6
        detP=alpha*alpha-beta*beta*omega2
        require(api.lower(detP)>0, "complete matrix-normalizer determinant")
        Pinv=[[(alpha-beta*aa)/detP, -beta*cc*qq*qq/detP],
              [-beta*cc/detP, (alpha+beta*aa)/detP]]
        m0,m1=alpha-hh*rr/2,beta-hh/2
        n0,n1=alpha+hh*rr/2,beta+hh/2
        denM=m0*m0-m1*m1*omega2
        denN=n0*n0-n1*n1*omega2
        require(api.lower(denM)>0 and api.lower(denN)>0,
                "both complete positive matrix-Pade spectral denominators")
        # Exact signed A-1, not a difference of independently saved uppers.
        Am1=(hh*(alpha*rr-beta*omega2)+hh*hh*(omega2-rr*rr)/2)/denM
        AA=one+Am1
        BB=hh*(alpha-beta*rr)/denM
        t11,t12=AA+BB*aa,BB*cc*qq*qq
        t21,t22=BB*cc,AA-BB*aa
        detT=denN/denM
        require(api.lower(t11)>0 and api.lower(t22)>0 and api.lower(detT)>0,
                "complete positive transfer diagonals and determinant")
        inverse_normalizers.append(Pinv)
        transfer.append((t11,t12,t21,t22))
        determinants.append(detT)
        forcing.append([[Am1+BB*aa,t12],[t21,Am1-BB*aa]])
    p=[z for _ in range(n+1)];p[n]=p_outer
    backward_transition=[z for _ in range(n)]
    forward_transition=[z for _ in range(n)]
    sigma=[z for _ in range(n)]
    denominators=[z for _ in range(n)]
    backward_input=[None for _ in range(n)]
    direct_forward_input=[None for _ in range(n)]
    for i in range(n-1,-1,-1):
        t11,t12,t21,t22=transfer[i]
        pn=p[i+1]
        den=t11+pn*t21
        require(api.lower(den)>0,"complete positive impedance pivot")
        p[i]=(t12+pn*t22)/den
        require(api.lower(p[i])>0,"complete positive impedance")
        backward_transition[i]=one/den
        forward_transition[i]=determinants[i]/den
        sigma[i]=t21/den;denominators[i]=den
        U=forcing[i]
        backward_input[i]=[-(U[0][k]+pn*U[1][k])/den for k in range(2)]
        direct_forward_input[i]=[(t11*U[1][k]-t21*U[0][k])/den for k in range(2)]
    H=[z for _ in range(n+1)]
    forward_input=[];forward_output=[];backward_output=[];local_output=[]
    half=one/2
    for i in range(n):
        tb,tf=backward_transition[i],forward_transition[i]
        H[i+1]=tf*tb*H[i]+sigma[i]
        b=backward_input[i]
        f=[tf*H[i]*b[k]+direct_forward_input[i][k] for k in range(2)]
        forward_input.append(f)
        K=one-p[i]*H[i];Kn=one-p[i+1]*H[i+1]
        F=[-half*(p[i]+tf*p[i+1]),half*(one+tf)]
        G=[half*(tb*K+Kn),half*(tb*H[i]+H[i+1])]
        D=[[one+half*(K*b[0]-p[i+1]*f[0]),
                    half*(K*b[1]-p[i+1]*f[1])],
           [half*(H[i]*b[0]+f[0]),one+half*(H[i]*b[1]+f[1])]]
        # Physical sqrt(h) S stays outside. This full signed P^-1
        # contraction is what replaces the old scalar rho division.
        forward_output.append(_matvec(inverse_normalizers[i],F))
        backward_output.append(_matvec(inverse_normalizers[i],G))
        local_output.append(_matmul(inverse_normalizers[i],D))
    return {"kind":"complete_clipped_scalar_trace_modal_generators_v1",
        "j":j,"n":n,"zero":z,"one":one,
        "backward_transition":backward_transition,
        "forward_transition":forward_transition,
        "forward_input":forward_input,"backward_input":backward_input,
        "forward_output":forward_output,"backward_output":backward_output,
        "local_output":local_output,
        "input_odd":[one/sqrt_h[i] for i in range(n)],
        "input_even":[one/(sqrt_h[i]*coordinate_q[i]) for i in range(n)],
        "output_odd":list(sqrt_h),
        "output_even":[sqrt_h[i]*coordinate_q[i] for i in range(n)],
        "end_from_odd":one,"end_from_even":p_outer,
        "outer_from_forward":theta,"outer_from_backward_end":theta*H[n],
        "outer_direct_even":-theta,"root_from_backward":one,
        "is_positive_majorant":False,"H":H,"p":p,
        "inverse_normalizers":inverse_normalizers,"transfer":transfer,
        "forcing":forcing,"denominators":denominators,
        "signed_matrix_normalizer_in_local_blocks":True}


def apply_generators(g, f_odd, f_even, endpoint_odd, endpoint_even):
    n = _vectors(g, f_odd, f_even)
    zero = g["zero"]
    ro = [g["input_odd"][i] * f_odd[i] for i in range(n)]
    re = [g["input_even"][i] * f_even[i] for i in range(n)]
    backward = [zero for _ in range(n + 1)]
    backward[n] = g["end_from_odd"] * endpoint_odd + g["end_from_even"] * endpoint_even
    for i in range(n - 1, -1, -1):
        b = g["backward_input"][i]
        backward[i] = g["backward_transition"][i] * backward[i + 1] + b[0] * ro[i] + b[1] * re[i]
    forward = [zero for _ in range(n + 1)]
    for i in range(n):
        a = g["forward_input"][i]
        forward[i + 1] = g["forward_transition"][i] * forward[i] + a[0] * ro[i] + a[1] * re[i]
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
        forward[i] += g["forward_transition"][i] * value
        a = g["forward_input"][i]
        ro[i] += a[0] * value
        re[i] += a[1] * value
    # forward[0] is the adjoint of a fixed zero, so is not a data coordinate.
    for i in range(n):
        value = backward[i]
        backward[i + 1] += g["backward_transition"][i] * value
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
    result.update({"kind": "complete_scalar_trace_whole_generator_majorant_v1",
                   "is_positive_majorant": True})

    def full(value):
        if isinstance(value, list):
            return [full(v) for v in value]
        return absolute_upper(value)

    for key in ("backward_transition", "forward_transition", "forward_input", "backward_input",
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

def complete_scalar_trace_reference_receivers(api,parent_lengths,parent_etas,parent_qs,
        selected_parent_diagonals,selected_parent_traces,changed_modes,thetas,old_records,old_upper,
        emit,copy_old,commit_mode,refinement=160):
    """Seven new complete bounds for a genuinely changed whole reference.

    old_records contains the complete finished WVC reference graph records.
    old_upper is their directed readback made by the owner before this call.
    The all-zero trace branch is handled by the owner as a whole-file/object
    copy before this function; it evaluates none of these new bound targets.
    commit_mode(j,running,witnesses,status) durably publishes the FULL prefix
    and returns its directed readback. For a copied-old witness the owner
    preserves its original complete record rather than formatting it again.
    """
    require(refinement==160 and len(parent_lengths)==153,
            "same inherited160 mesh of153 parents")
    require(len(parent_etas)==len(parent_qs)==len(selected_parent_diagonals)==len(selected_parent_traces)==153,
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
    require(all(set(packet)==set(range(1,97)) for packet in list(selected_parent_diagonals)+list(selected_parent_traces)),
            "all complete selected parent modal definitions")
    # The all-zero case is not seven copied reference numbers followed by
    # a re-evaluation of other WVC graphs. The owner must copy the entire
    # completed original candidate and return before opening any new target.
    require(any(changed_modes.values()),
            "all-zero scalar trace: owner must return complete literal WVC candidate")
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
            parent_r=[selected_parent_traces[i][j] for i in range(153)]
            speed=[v for v in parent_c for _ in range(refinement)]
            a=[v for v in parent_a for _ in range(refinement)]
            r=[v for v in parent_r for _ in range(refinement)]
            g=prepare_scalar_trace_generators(api,j,h,speed,q,q,root_h,a,r,
                                         thetas[j],api.rational(13,80))
            positive=whole_positive_generator(g,api.magnitude)
            vout={"odd":vin_odd,"even":vin_even,"root_odd":one,"outer_weighted":thetas[j]}
            sums=complete_weighted_generator_schur_sums(
                positive,vin,vout,positive_lower,api.upper)
            candidate={"q_row":sums["complete_weighted_row_ratio_upper"],
                       "q_column":sums["complete_weighted_column_ratio_upper"]}
            # In the actual S coordinates the full self-adjoint block defect
            # has norm <= d_i. Factor it as diag(d_i I) times a block
            # contraction. The following whole Q*diag(d_i I) Schur bound is
            # therefore valid without treating the matrix defect as diagonal.
            parent_delta=[]
            for length,aa,cc,qq in zip(cell_h,parent_a,parent_c,parent_qs):
                xx=api.rational(81,64)*length*length*(aa*aa+cc*cc*qq*qq)
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
        "w0":api.upper(api.rational(5,4)),"mode_prefix_count":96,
        "new_record_count":7,"copied_record_count":0,
        "finite_dimension":193*n+193,"reference_is_changed":True,
        "all_actual_spaces_unchanged":True,
        "entire_old_candidate_must_be_copied":False}
