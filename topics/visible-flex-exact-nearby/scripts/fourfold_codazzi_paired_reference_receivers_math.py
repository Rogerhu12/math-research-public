"""WPS new reference receiver targets. No entry point, imports, IO or old target call.
Pure WIC/WQS definitions below are copied verbatim, not imported as a producer.
The only evaluations are the newly declared complete reference norms.
"""

def _lengths(n, *vectors):
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("positive integer cell count required")
    if any(len(v) != n for v in vectors):
        raise ValueError("complete common cell partition required")

def prepare_mode(j, h, eta, reference_q, coordinate_q, sqrt_h, rho,
                 theta, p_outer, zero, one):
    """Prepare the unique exact modal circuit, to be evaluated outward.

    The nonzero mode is (sqrt(2) sin(4j phi), sqrt(2) cos(4j phi)).
    coordinate_q is the actual S_i even scaling. reference_q belongs only
    to D_i=4j eta_i [[0, reference_q_i**2], [1, 0]]. No transformed endpoint
    continuity is imposed. rho_i is the separately declared positive
    finite diagonal; rho=1 and rho=1+h*4j*eta*q/2 are distinct whole trials.
    """
    if isinstance(j, bool) or not isinstance(j, int) or not 1 <= j <= 96:
        raise ValueError("one genuine nonzero head mode 1..96 required")
    n = len(h)
    _lengths(n, h, eta, reference_q, coordinate_q, sqrt_h, rho)
    two = one + one
    half = one / two
    p = [zero for _ in range(n + 1)]
    p[n] = p_outer
    tau = [zero for _ in range(n)]
    lam = [zero for _ in range(n)]
    mu = [zero for _ in range(n)]
    sigma = [zero for _ in range(n)]
    varrho = [zero for _ in range(n)]
    denominators = [zero for _ in range(n)]
    for i in range(n - 1, -1, -1):
        b = h[i] * (4 * j) * eta[i] / (two * rho[i])
        a = b * reference_q[i] * reference_q[i]
        pn = p[i + 1]
        den = one + two * b * pn + a * b
        denominators[i] = den
        p[i] = ((one + a * b) * pn + two * a) / den
        tau[i] = (one - a * b) / den
        lam[i] = two * b * (pn + a) / den
        mu[i] = two * a * (one + b * pn) / den
        sigma[i] = two * b / den
        varrho[i] = two * a * b / den
    return {
        "kind": "weighted_modal_impedance_circuit_v1",
        "j": j, "n": n, "zero": zero, "one": one, "half": half,
        "p": p, "tau": tau, "lambda": lam, "mu": mu,
        "sigma": sigma, "varrho": varrho, "denominators": denominators,
        "input_odd": [one / sqrt_h[i] for i in range(n)],
        "input_even": [one / (sqrt_h[i] * coordinate_q[i]) for i in range(n)],
        "output_odd": [sqrt_h[i] / rho[i] for i in range(n)],
        "output_even": [sqrt_h[i] * coordinate_q[i] / rho[i] for i in range(n)],
        "theta": theta, "p_outer": p_outer,
        "is_positive_majorant": False,
    }

def mean_action(weights, body, endpoint_mean):
    """Physical mean: weights_i=sqrt(h_i)*coordinate_q_i; no sqrt(2)."""
    _lengths(len(weights), body)
    return {
        "body": [body[i] + weights[i] * endpoint_mean for i in range(len(weights))],
        "root_mean": endpoint_mean,
    }

def mean_transpose(weights, body, root_mean):
    _lengths(len(weights), body)
    value = root_mean
    for i in range(len(weights)):
        value += weights[i] * body[i]
    return {"body": list(body), "endpoint_mean": value}

def complete_mean_norm(weights, zero, one, sqrt):
    """Exact norm formula for [[Id,w],[0,1]], evaluated outward by caller."""
    squared = zero
    for value in weights:
        squared += value * value
    two = one + one
    return (sqrt(two * two + squared) + sqrt(squared)) / two

def inherited_rho_quadratic(j, h, eta, reference_q, one):
    """Frozen WIC primary: rho_2(x)=1+x*x/12, with error <= x**4/720.

    The exact principal Schur normalizer is rho_*(x)=(x/2)coth(x/2).
    This function evaluates only the rational reference. The inequality
    is a theorem; any numerical error record for it is a separate new target.
    """
    if isinstance(j, bool) or not isinstance(j, int) or not 1 <= j <= 96:
        raise ValueError("one genuine nonzero head mode 1..96 required")
    _lengths(len(h), eta, reference_q)
    twelve = 12 * one
    values = []
    for i in range(len(h)):
        x = h[i] * (4 * j) * eta[i] * reference_q[i]
        values.append(one + x * x / twelve)
    return values

def _vectors(g, odd, even):
    n = g["n"]
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("positive complete cell count required")
    if len(odd) != n or len(even) != n:
        raise ValueError("both complete modal radial vectors required")
    return n

def generators_from_mode(c):
    n = c["n"]
    zero, one, half = c["zero"], c["one"], c["half"]
    if c["is_positive_majorant"] is not False:
        raise ValueError("complete signed WIC mode required")
    H = [zero for _ in range(n + 1)]
    alpha = [zero for _ in range(n)]
    beta = [zero for _ in range(n)]
    forward_output = []
    backward_output = []
    local_output = []
    for i in range(n):
        tau = c["tau"][i]
        H[i + 1] = tau * tau * H[i] + c["sigma"][i]
        alpha[i] = c["sigma"][i] - tau * H[i] * c["lambda"][i]
        beta[i] = -c["varrho"][i] - tau * H[i] * c["mu"][i]
        K = one - c["p"][i] * H[i]
        Kn = one - c["p"][i + 1] * H[i + 1]
        backward_output.append([
            half * (K * tau + Kn),
            half * (H[i] * tau + H[i + 1])])
        forward_output.append([
            -half * (c["p"][i] + c["p"][i + 1] * tau),
            half * (one + tau)])
        local_output.append([
            [one - half * (K * c["lambda"][i] + c["p"][i + 1] * alpha[i]),
             -half * (K * c["mu"][i] + c["p"][i + 1] * beta[i])],
            [half * (alpha[i] - H[i] * c["lambda"][i]),
             one + half * (beta[i] - H[i] * c["mu"][i])]])
    return {
        "kind": "same_WIC_bidirectional_generators_v1",
        "n": n, "j": c["j"], "zero": zero, "one": one,
        "transition": list(c["tau"]),
        "forward_input": [[alpha[i], beta[i]] for i in range(n)],
        "backward_input": [[-c["lambda"][i], -c["mu"][i]] for i in range(n)],
        "forward_output": forward_output,
        "backward_output": backward_output,
        "local_output": local_output,
        "input_odd": list(c["input_odd"]),
        "input_even": list(c["input_even"]),
        "output_odd": list(c["output_odd"]),
        "output_even": list(c["output_even"]),
        "end_from_odd": one, "end_from_even": c["p_outer"],
        "outer_from_forward": c["theta"],
        "outer_from_backward_end": c["theta"] * H[n],
        "outer_direct_even": -c["theta"],
        "root_from_backward": one,
        "is_positive_majorant": False,
        "H": H,
    }

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


def _positive(api,x):
    value=api.lower(x)
    if not value>0:
        raise ValueError("positive reference denominator")
    return value


def _max_upper(api,values):
    return max(api.upper(v) for v in values)


def complete_reference_receivers(api,parent_lengths,parent_etas,parent_qs,
        thetas,emit,commit_mode,refinement=160):
    """All 96 direct-sum modes plus the independent true scalar mean.

    parent_lengths enclose the same selected-member physical lengths.  Only
    the first, zero-rate parent can contain the original r_* enclosure.
    commit_mode saves the FULL running prefix and returns its directed
    readback.  No mode table or finite matrix is published.
    """
    if refinement!=160 or len(parent_lengths)!=153:
        raise ValueError("published inherited 160 refinement of 153 parents")
    if not len(parent_lengths)==len(parent_etas)==len(parent_qs):
        raise ValueError("complete parent arrays")
    zero,one=api.zero,api.one
    # Equal subcells inherit each complete parent reference exactly.  Compute
    # repeated scalar factors once per parent; this does not coarsen p/H.
    cell_h=[length/refinement for length in parent_lengths]
    parent_root_h=[api.sqrt(v) for v in cell_h]
    h=[v for v in cell_h for _ in range(refinement)]
    eta=[v for v in parent_etas for _ in range(refinement)]
    q=[v for v in parent_qs for _ in range(refinement)]
    root_h=[v for v in parent_root_h for _ in range(refinement)]
    for i in range(len(h)):
        _positive(api,h[i]);_positive(api,q[i]);_positive(api,root_h[i])
        if api.lower(eta[i])<0:
            raise ValueError("nonnegative reference speed")
    n=len(h)
    v_odd=list(root_h);v_even=[root_h[i]*q[i] for i in range(n)]
    input_weights={"odd":v_odd,"even":v_even,"endpoint_odd":one,"endpoint_even":one}
    running={"q_row":zero,"q_column":zero,"rho_row":zero,"rho_column":zero,
             "odd_endpoint":zero,"Z_squared":zero}
    witnesses={key:None for key in running}
    for j in range(1,97):
        parent_rho=inherited_rho_quadratic(j,cell_h,parent_etas,parent_qs,one)
        rho=[v for v in parent_rho for _ in range(refinement)]
        c=prepare_mode(j,h,eta,q,q,root_h,rho,thetas[j],api.rational(13,80),zero,one)
        for value in c["denominators"]:
            _positive(api,value)
        if not all(api.lower(p)>0 for p in c["p"]):
            raise ValueError("complete positive impedance pivots")
        g=generators_from_mode(c)
        positive=whole_positive_generator(g,api.magnitude)
        output_weights={"odd":v_odd,"even":v_even,"root_odd":one,
                        "outer_weighted":thetas[j]}
        sums=complete_weighted_generator_schur_sums(
            positive,input_weights,output_weights,lambda x:_positive(api,x),api.upper)
        candidate={"q_row":sums["complete_weighted_row_ratio_upper"],
                   "q_column":sums["complete_weighted_column_ratio_upper"]}

        parent_delta=[];zsq=[]
        for length,speed,scale in zip(cell_h,parent_etas,parent_qs):
            x=length*(4*j)*speed*scale
            xx=x*x
            parent_delta.append(min(api.upper(xx/12),api.upper(xx*xx/720)))
            zsq.append(min(api.upper(xx/12),api.upper(x/2)))
        delta=[v for v in parent_delta for _ in range(refinement)]
        rows=apply_generators(positive,
              [api.upper(v_odd[i]*delta[i]) for i in range(n)],
              [api.upper(v_even[i]*delta[i]) for i in range(n)],zero,zero)
        row_values=[api.upper(rows["odd"][i]/_positive(api,v_odd[i])) for i in range(n)]
        row_values += [api.upper(rows["even"][i]/_positive(api,v_even[i])) for i in range(n)]
        row_values += [api.upper(rows["root_odd"]),
                       api.upper(rows["outer_weighted"]/_positive(api,thetas[j]))]
        cols=transpose_generators(positive,v_odd,v_even,one,thetas[j])
        col_values=[api.upper(cols["odd"][i]*delta[i]/_positive(api,v_odd[i])) for i in range(n)]
        col_values += [api.upper(cols["even"][i]*delta[i]/_positive(api,v_even[i])) for i in range(n)]
        candidate["rho_row"]=_max_upper(api,row_values)
        candidate["rho_column"]=_max_upper(api,col_values)
        # The endpoint input has the ACTUAL H^-5/6 Riesz conversion theta^-1.
        endpoint=apply_generators(g,[zero]*n,[zero]*n,one/thetas[j],zero)
        total=sum((api.magnitude(v)**2 for v in endpoint["odd"]+endpoint["even"]+
                   [endpoint["root_odd"],endpoint["outer_weighted"]]),zero)
        candidate["odd_endpoint"]=api.upper(api.sqrt(total))
        candidate["Z_squared"]=_max_upper(api,zsq)
        for key,value in candidate.items():
            value=api.upper(value)
            if value>running[key] or witnesses[key] is None:
                running[key]=value;witnesses[key]=j
        saved=commit_mode(j,running,witnesses)
        if set(saved)!=set(running):
            raise ValueError("whole reference-mode prefix readback")
        running=dict(saved)
    q_r=emit("complete_reference_row_ratio_upper",running["q_row"])
    q_c=emit("complete_reference_column_ratio_upper",running["q_column"])
    qrho_r=emit("complete_reference_rho_row_ratio_upper",running["rho_row"])
    qrho_c=emit("complete_reference_rho_column_ratio_upper",running["rho_column"])
    squared=sum((length*qvalue*qvalue
                 for length,qvalue in zip(parent_lengths,parent_qs)),zero)
    mean_norm=complete_mean_norm(
        [api.sqrt(length)*qvalue for length,qvalue in zip(parent_lengths,parent_qs)],
        zero,one,api.sqrt)
    q_norm=emit("complete_reference_inverse_norm_upper",
               max(api.upper(api.sqrt(q_r*q_c)),api.upper(mean_norm)))
    e_rho=emit("complete_reference_rho_defect_upper",api.upper(api.sqrt(qrho_r*qrho_c)))
    q_o=emit("complete_reference_odd_endpoint_receiver_upper",running["odd_endpoint"])
    q_m=emit("complete_reference_mean_endpoint_receiver_upper",api.upper(api.sqrt(1+squared)))
    zsq=emit("complete_reference_Z_squared_upper",running["Z_squared"])
    w0=emit("complete_reference_head_lift_upper",api.upper(api.sqrt(1+zsq)))
    return {"q":q_norm,"e_rho":e_rho,"q_o":q_o,"q_m":q_m,"w0":w0,
            "mode_prefix_count":96,"finite_dimension":193*n+193,
            "prescribed_root_even_is_rhs_only":True,"physical_mean_separate":True}
