"""All 193 independent original physical boundary columns in the genuine GG hybrid."""
from fractions import Fraction


def require(ok, message):
    if not ok:
        raise ValueError(message)


def diagonal(engine, entries):
    api, km = engine.api, engine.km
    n = len(entries)
    matrix = km.Matrix(n,n,[[entries[i] if i == j else api.zero for j in range(n)] for i in range(n)])
    return engine.from_interval(matrix, known_norm=max(api.magnitude(v) for v in entries))


def group_norms(engine, matrix):
    return {"left96": engine.columns(matrix,range(96)).norm(),
            "charted_right97": engine.columns(matrix,range(96,193)).norm(), "joint193": matrix.norm()}


def gram_norms(engine, gram):
    api = engine.api
    result = {}
    for key, rows in (("left96",range(96)),("charted_right97",range(96,193)),("joint193",range(193))):
        result[key] = api.sqrt(engine.submatrix(gram,rows,rows).norm()).upper()
    return result


def local_action(engine, coefficient, span_duration, initial):
    """New action on the physical boundary columns, with time-ordered tail in spectral norm."""
    e, api = engine, engine.api
    beta = coefficient.norm()
    gap = (api.one-beta/18).lower()
    require(api.lower(gap) > 0, "positive degree-16 Peano tail gap")
    first = e.multiply(coefficient,initial)
    term = first
    endpoint = e.add(initial,first)
    span_mid = e.add(initial,e.scale(api.rational(1,2),first))
    span_radius = first.norm()/2
    bound = first.norm()
    for k in range(2,17):
        term = e.scale(api.rational(1,k),e.multiply(coefficient,term))
        endpoint = e.add(endpoint,term)
        span_mid = e.add(span_mid,e.scale(api.rational(1,2),term))
        span_radius += term.norm()/2
        bound = (bound*beta/k).upper()
    tail = (bound*beta/(17*gap)).upper()
    # All true partial-endpoint ordered terms, including the final endpoint.
    span = e.from_interval(span_mid.c,span_mid.r+span_radius+tail)
    endpoint = e.from_interval(endpoint.c,endpoint.r+tail)
    require(api.lower(span_duration) > 0, "positive actual physical duration")
    return endpoint,span


def solve(*, engine, model, provider, balances, graph_math, output_store, budget, progress):
    """Distinct private store for right propagation and the whole signed observations.

    A caller must use the fresh live GG model or the wholly authenticated GRR
    reconstruction. Core graph keys are read only. Final public summaries
    contain small bounds and full private matrix identities.
    """
    e, api = engine,engine.api
    context = model["context"]
    require(model["kind"] == "R149_actual_low193_joint_Grassmann_inverse_v1"
            and model["true_hybrid_BVP_verified"] and model["complete_refined_cells"] == 1424
            and provider.context is context and provider.api is api and provider.km is e.km
            and graph_math.Engine is type(e) and len(balances) == 155, "identical original hybrid graph")
    original = model["joint_store"]
    require(output_store is not original and not output_store.data, "fresh independent private destination")
    n, domain = 1424,context.domain
    def node(i, name):
        return original.get(("node",i,name))
    theta = [context.reference_thetas[j] for j in range(1,97)]
    require(all(api.lower(x)>0 for x in theta), "all 96 actual physical weights")
    left = e.inverse(e.rows(node(0,"right"),range(97,193)))
    unit = diagonal(e,[api.one/x for x in theta]+[api.one])
    right = e.multiply(e.inverse(graph_math.original_outer_boundary(e,node(n,"left"))),unit)
    outer_weight = diagonal(e,theta)
    root_weight = diagonal(e,[api.rational(1+16*j*j)**api.rational(1,6) for j in range(1,97)]+[api.one]*97)
    a, c, z = Fraction(17,20),Fraction(9,10),Fraction(19,20)
    def cover(i):
        return tuple(domain.exact_physical_cover((i,Fraction(0),Fraction(1))))
    def wanted(i):
        if i in (0,n):
            return True
        lo,hi = cover(i)
        return a < hi and lo < z
    for i in range(n,-1,-1):
        if wanted(i):
            output_store.put(("reverse_coordinate",i),right)
        if i:
            right = e.multiply(original.get(("Uinv",i-1)),right)
        if i%16 == 0 or i == n:
            progress("all_right97_homogeneous_columns",dict(complete=n-i+1,nodes=n+1))
            budget()
    gram = {key:e.zero(193,193) for key in ("low","shell")}
    observations = {}
    records = []
    def save(key, value):
        require(key not in observations,"one complete physical output per key")
        output_store.put(("observation",key),value)
        certified = output_store.get(("observation",key))
        observations[key] = group_norms(e,certified)
        records.append({"observation":key,"matrix_record":dict(output_store.data[("observation",key)])})
    trace_saved = False
    cursor = a
    def observe(box, duration, span, endpoint):
        nonlocal trace_saved,cursor
        lo,hi = domain.exact_physical_cover(box)
        if hi == c:
            require(not trace_saved,"unique exact cut")
            save("cut_raw193",endpoint)
            trace_saved = True
        if hi <= a or lo >= z:
            return
        require(cursor == lo < hi <= z,"whole shell cover without gap or overlap")
        cursor = hi
        K = None
        for idx,_,_ in provider._body_intersections((lo,hi)):
            value = api.old_interval(provider.rows[idx]["original_intrinsic_enclosure"]["K"])
            K = value if K is None else K.union(value)
        require(K is not None and api.lower(K) > 0,"entire authentic positive shell curvature")
        wk = api.sqrt(api.sqrt(K))
        Y = e.multiply(diagonal(e,[api.one/wk]*96+[wk]*97),span)
        for key,matrix in (("low",Y),("shell",e.rows(Y,tuple(range(32,96))+tuple(range(129,193))))):
            product = e.multiply(e.transpose(matrix),matrix)
            gram[key] = e.add(gram[key],e.scale(duration,product))

    for i in range(n+1):
        if wanted(i):
            arow = output_store.get(("reverse_coordinate",i))
            output_store.remove(("reverse_coordinate",i))
            H = e.hcat(e.multiply(node(i,"right"),left),e.multiply(node(i,"left"),arow))
            if i == 0:
                save("root_mixed_full193",e.multiply(root_weight,H))
                save("root_raw97",e.rows(H,range(97)))
            if i == n:
                save("outer_weighted96",e.multiply(outer_weight,e.rows(H,range(97,193))))
            if 0 < i < n:
                physical = cover(i)
                require(domain.cells[i]["parent_panel"] > 0,"shell occurs on fixed physical panels")
                factor = balances[domain.cells[i]["parent_panel"]]
                D = diagonal(e,[api.one]*96+[factor]*97)
                Dinv = diagonal(e,[api.one]*96+[api.one/factor]*97)
                x = e.multiply(D,H)
                cuts = {Fraction(j,4) for j in range(5)}
                for cut in (a,c,z):
                    if physical[0] < cut < physical[1]:
                        cuts.add((cut-physical[0])/(physical[1]-physical[0]))
                cuts = sorted(cuts)
                stack = list(reversed(list(zip(cuts,cuts[1:]))))
                while stack:
                    lo, hi = stack.pop()
                    if physical[0]+(physical[1]-physical[0])*lo >= z:
                        break
                    box = i,lo,hi
                    dt = domain.full_length(i)*domain.exact(hi-lo)
                    coeff = provider.centre_matrix(e.flow.HEAD,e.flow.HEAD,box)
                    scaled = e.flow.diagonal_similarity(e.km,coeff,[api.one]*96+[factor]*97)
                    G = e.from_interval(e.km.scale(api,dt,scaled))
                    if not api.lower((api.one-G.norm()/18).lower()) > 0:
                        require(hi-lo > Fraction(1,64),"strict new whole-column Peano denominator")
                        mid = (lo+hi)/2
                        stack.extend(((mid,hi),(lo,mid)))
                        continue
                    x,span = local_action(e,G,dt,x)
                    observe(box,dt,e.multiply(Dinv,span),e.multiply(Dinv,x))
                    budget()
        if i < n:
            left = e.multiply(original.get(("Vinv",i)),left)
        if i%16 == 0 or i == n:
            progress("all_left96_and_signed_shell",dict(complete=i+1,nodes=n+1,
                        cut_complete=trace_saved,exact_shell_prefix=str(cursor)))
            budget()
    require(cursor == z and trace_saved,"complete fixed cut and ordinary shell")
    for key in ("low","shell"):
        name=key+"_physical_shell_Gram193"
        output_store.put(("gram",name),gram[key])
        value=output_store.get(("gram",name))
        observations[name] = gram_norms(e,value)
        records.append({"observation":name,"matrix_record":dict(output_store.data[("gram",name)])})
    return dict(kind="R149_true_hybrid_complete_boundary_response_columns_v1",
                private_model_token=model["private_model_token"],
                root_and_outer_boundary_inverses_verified=True,complete_boundary_columns=193,
                right_input_has_mean=True,all_source_map_targets_called=0,
                exact_physical_shell=[str(a),str(z)],exact_physical_cut=str(c),
                complete_private_observations=records,complete_private_store=output_store.receipt(),
                actual_directed_observations=observations,full_physical_matching_proved=False)


def physical_preconditioner(*, engine, model, maps, output_store, admitted, stage, gtp, outer,
                            save):
    """Independent signed physical gate; ordinary TP and its history retain their own kind.

    The caller first authenticates both complete source results, executions and
    manifests. The new certificate uses the real W_c and the saved TP internal
    positive margin. Every scalar output is retained on directed readback.
    """
    e,api = engine,engine.api
    require(maps["kind"] == "R149_true_hybrid_complete_boundary_response_columns_v1"
            and maps["private_model_token"] is model["private_model_token"]
            and maps["complete_boundary_columns"] == 193 and maps["right_input_has_mean"]
            and maps["root_and_outer_boundary_inverses_verified"] is True
            and maps["complete_private_store"] == output_store.receipt()
            and stage["complete"] and stage["proved"] and stage["failure"] is None
            and stage["actual_returncode"] == 0 and "private_token" in admitted
            and stage["result"]["low_inverse_basis"] == gtp.TRUE_BASIS
            and stage["result"]["reference_identity"] == model["context"].reference_identity == admitted["reference_identity"]
            and stage["result"]["same_actual_internal_gate_passed"]
            and stage["result"]["complete_new_record_order"] == stage["completed_targets"]
            and stage["saved_record_count"] == len(stage["completed_targets"])
            and set(stage["new_records"]) == set(stage["completed_targets"]), "actual common complete physical inputs")
    expected = next(r["matrix_record"] for r in maps["complete_private_observations"]
                    if r["observation"] == "outer_weighted96")
    key = ("observation","outer_weighted96")
    require(output_store.data[key] == expected and outer["full_real_delta_outer_graph_proved"]
            and outer["independent_even_mean_and_all_head_and_affine_outer_columns_retained"]
            and outer["native_sha256"] == admitted["negative"]["original_complete_outer_native_sha256"]
            and outer["explicit_direction_definition_sha256"] == admitted["negative"]["explicit_direction_definition_sha256"]
            and outer["derived_definition_sha256"] == admitted["negative"]["derived_definition_sha256"],
            "same whole signed outer96 and actual exterior with every affine row")
    Wc = e.columns(output_store.get(key),range(96,193))
    def read(k):
        return gtp.saved_upper(api, stage["new_records"][k])
    kO = read("actual_internal_feedback_outer_upper")
    PB = read("actual_internal_right_boundary_body_upper")
    JB, JO = (read("actual_internal_outer_b_Poisson_low_"+k+"_upper") for k in ("body","outer"))
    tb = read("actual_outer_b_high_even_trace_upper")
    tx=admitted["tX"]
    ah=read("actual_physical_high_to_right97_upper")
    m = 96
    p_actual = outer["bounds"]
    p_lo = api.old_interval(p_actual["actual_reference_outer_p_lower"]).lower()
    p_hi = api.old_interval(p_actual["actual_reference_outer_p_upper"]).upper()
    require(api.lower(p_lo) > 0 and bool(p_lo <= p_hi), "actual complete selected family scalar interval")
    # This dyadic choice fixes the chart preconditioner, independent of p_delta.
    p_mid = e.exact_float(float(((p_hi+p_lo)/2).mid()))
    delta = api.magnitude(api.interval(p_lo,p_hi)-p_mid)
    K = e.vcat(e.scale(api.rational(13,80)-p_mid,e.eye(m)),e.zero(1,m))
    # Exact jointly bordered system on r97,b96, in the original weighted units.
    inverse = e.inverse(e.vcat(e.hcat(e.eye(97),e.scale(-api.one,K)),
                               e.hcat(e.scale(-api.one,Wc),e.eye(m))))
    rr,bb = range(97),range(97,193)
    splits = (rr,bb)
    P = [[save("signed_boundary_preconditioner_"+a+b,e.submatrix(inverse,ra,rb).norm(),"upper")
          for rb,b in zip(splits,"rb")] for ra,a in zip(splits,"rb")]
    residual = ((ah*tx*PB,delta+ah*(api.one+tb+tx*JB)),(kO*PB,JO))
    N = [[save("true_preconditioned_defect_"+a+b,P[i][0]*residual[0][j]+P[i][1]*residual[1][j],"upper")
          for j,b in enumerate("rb")] for i,a in enumerate("rb")]
    u,v,w,z = N[0]+N[1]
    margin1 = save("signed_preconditioned_right_margin",(api.one-u).lower(),"lower")
    margin2 = save("signed_preconditioned_outer_margin",(api.one-z).lower(),"lower")
    det = save("signed_preconditioned_full_det",(margin1*margin2-v*w).lower(),"lower")
    outcome = dict(kind="R149_signed_low_terminal_charted_97plus96_physical_gate_v1",
                   original_gate_branch=stage["result"]["complete_branch"],
                   reference_identity=admitted["reference_identity"],original_mean_and_height_ports=True,
                   physical_positive_inverse_proved=False,old_TP_gate_reissued=False)
    if not all(api.lower(x) > 0 for x in (margin1,margin2,det)):
        return outcome
    Q = (((api.one-z)/det,v/det),(w/det,(api.one-u)/det))
    outcome["physical_inverse_upper"] = [[save("signed_physical_inverse_"+a+b,
        Q[i][0]*P[0][j]+Q[i][1]*P[1][j],"upper") for j,b in enumerate("rb")] for i,a in enumerate("rb")]
    outcome["physical_positive_inverse_proved"] = True
    return outcome
