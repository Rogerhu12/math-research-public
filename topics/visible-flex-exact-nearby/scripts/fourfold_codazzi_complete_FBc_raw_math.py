"""Complete receiver-free WJK F Bc raw-L2 comparison, pure definitions.

The exact collar cancellation is retained before a whole positive triangle.
The complete signed F is the same WJK finite trial, not the actual G_H.
This minimal module never constructs a G_f/low-inverse receiver, atom norm,
old50 target graph, family remainder, or completed scientific target.
"""

def require(ok, message):
    if not ok:
        raise ValueError(message)

def upper(api, value):
    require(value.is_finite(), "finite complete directed scalar")
    result = value.upper()
    require(api.lower(result) >= 0, "nonnegative mathematical upper")
    return result

def build_receiver_free_WJK_comparisons(api, km, context, assembly, include_actual_remainders=False):
    """Concrete complete F/residual graphs with NO old G_f receiver attached.

    All intermediate angular spaces, five collar/transition terms, and
    true J* integration to R are retained.  This builds a new small set of
    operator-valued scalar comparisons; it neither evaluates the excluded
    old50-target recipe nor concatenates a large signed semiseparable DAG.
    Call complete_positive_comparison_norm on an entire returned operator
    as a separately declared NEW target.  No call is made here at import.
    """
    require(include_actual_remainders is False, "this owner has exactly one receiver-free F Bc target")
    domain, n = context.domain, len(context.domain.cells)
    require(n == 155, "complete same comparison coefficient cover")
    cap = assembly._complete_private_centre_norms(api, km, context)
    H = {j: "R141_raw_high"+str(j)+"_L2" for j in (160, 224, 288, 416)}
    X = "R141_same_transformed_head193_L2"
    one = [api.one]*n
    pc = [api.one if p == 0 else api.zero for p in context.parent_indices]
    pb = [api.zero if p == 0 else api.one for p in context.parent_indices]
    cut = [context.cutoff(domain.whole_cell_box(i)) for i in range(n)]
    chi, xp, psi, psip = ([upper(api, api.magnitude(c[j])) for c in cut] for j in range(4))
    local = [upper(api, api.magnitude(c[0]*c[0]-pb[i])) for i, c in enumerate(cut)]
    def point(values, inp, out, label):
        return km.PointwiseNormComparison(domain, values, inp, out, "R141:"+label)
    def mul(values, space, label):
        return point(values, space, space, label)
    def change(inp, out, label):
        return point(one, inp, out, label)
    def coef(name, inp, out):
        return point(cap[name], inp, out, name)
    def chain(label, *ops):
        result = ops[-1]
        for i in range(len(ops)-2, -1, -1):
            result = km.PositiveComposition(ops[i], result, "R141:"+label+":"+str(i))
        return result
    def plus(label, *ops):
        return km.PositiveSum(ops, "R141:"+label)
    J = {b: km.CompleteScalarKernelComparison(domain, H[b], H[b],
        lambda i, j: api.one if context.parent_indices[j] == 0 else api.zero,
        label="R141:whole_J_with_constant_continuation_"+str(b)) for b in (160, 224, 288)}
    Js = {b: km.CompletePositiveAdjoint(J[b], "R141:true_Jstar_to_R_"+str(b)) for b in J}
    G = assembly._complete_modal_norm_comparison(api, km, context, False, H[160], H[160])
    B = coef("B", X, H[160])
    A160, A224 = coef("A160", H[160], H[224]), coef("A224", H[224], H[288])
    Ato160, Ato224 = coef("Astar160", H[224], H[160]), coef("Astar224", H[288], H[224])
    E160, Eto160 = coef("E160", H[160], H[224]), coef("Estar160", H[224], H[160])
    c160 = mul(chi, H[160], "chi160")
    P0 = chain("P0", c160, G, c160)
    polynomial = plus("J_plus_JAJ",
        chain("embed_J", change(H[160], H[224], "embed_J"), J[160]),
        chain("JAJ", J[224], A160, J[160]))
    Pbase = plus("whole_P",
        chain("embed_P0", change(H[160], H[224], "embed_P0"), P0),
        chain("psi_polynomial", mul(psi, H[224], "psi224"), polynomial))
    PB = chain("whole_PBc", Pbase, B)
    k = plus("Xprime_minus_chiE",
        chain("embed_Xprime", change(H[160], H[224], "embed_Xprime"), mul(xp, H[160], "Xprime")),
        chain("chiE", mul(chi, H[224], "chi224"), E160))
    Rcbase = plus("whole_Rc_base",
        chain("local", change(H[160], H[288], "embed_local"), mul(local, H[160], "chi2_minus_Pb")),
        chain("body_residual", change(H[224], H[288], "embed_body"), k, G, c160),
        chain("psi_prime_polynomial", change(H[224], H[288], "embed_transition"), mul(psip, H[224], "Psiprime224"), polynomial),
        chain("psi_Pb_AJ", change(H[224], H[288], "embed_AJ"), mul([upper(api, x*y) for x, y in zip(psi, pb)], H[224], "psiPb"), A160, J[160]),
        chain("psi_AJAJ", mul(psi, H[288], "psi288"), A224, J[224], A160, J[160]))
    Rc = chain("whole_Rc", Rcbase, B)
    Qstar = plus("whole_Qstar",
        chain("P0_from224", P0, change(H[224], H[160], "P0_projection")),
        chain("minus_Jstar", Js[160], change(H[224], H[160], "Jstar_projection"), mul(psi, H[224], "right_psi")),
        chain("Jstar_A_Jstar", Js[160], Ato160, Js[224], mul(psi, H[224], "right_psi_second")))
    Fpositive = plus("whole_signed_FBc_by_complete_triangle",
        chain("project_PBc", change(H[224], H[160], "project_PBc"), PB),
        chain("Qstar_Rc", Qstar, change(H[288], H[224], "exact_returned_Rc_projection"), Rc))
    return {"whole_FBc_to_K0_raw": Fpositive}

