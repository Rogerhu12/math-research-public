"""Complete four T,v graphs using their actual scalar N,D and the original post-ideal operator return."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the named public research Actions.")
import hashlib
import inspect
import textwrap
from pathlib import Path
from sage.all import identity_matrix, vector
import original_complete_quadratic_returns as quadratic
import original_short_graph_outer as outer
from original_ys_divisor_ideal_tools import digest, element_digest, polynomial_digest, polynomial_matrix_digest

SOURCE_DEPENDENCIES = (
    "original_direct_scalar_fraction_graph.py","original_short_graph_outer.py",
    "original_complete_quadratic_returns.py","original_ys_fraction_bridge.py",
    "original_ys_equation_transport.py","original_ys_geometry_transport.py")
PINNED_OUTER = "1723f3e67615b184af3298d47188c7a9e32bae3acd28f1fa5bca737755349f20"
CURRENT = None
SEEN = []
SCALAR_CODE = None
OWNERS = {"T":"same central T","vs":"same v=ys^2-1"}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def exact_inputs(six, engines, function, flag, N, D, name):
    """Read both source scalars against the actual unit; never assume that the unit coordinate equals one."""
    model, engine = six["model"], engines[flag]
    chart = engine.chart
    R, k = engine.R, engine.k
    raw = function.chart_pair(flag)
    i = int(model.unit_index)
    require(type(flag) is bool and six["kind"] == "rank2_original_Y_fraction_consumer_context" and
            six["prime"] == model.prime == 29 and six["constants"] is model.k is k and
            model.affine is six["original_affine_context"] and model.embedding is six["embedding_context"] and
            model.operations is model.embedding["operations"] and function is six[name] and function.model is model and
            raw[0] is N and raw[1] is D and engine.infinity_chart is flag and chart["infinity_chart"] is flag and
            N.base_ring() is D.base_ring() is R is chart["polynomial_ring"] is (model.S if flag else model.P) and
            chart["constants"] is k is R.base_ring() and int(k.cardinality()) == 29**2 and
            engine.dimension == chart["dimension"] == len(N) == len(D) == 306 and
            engine.unit == chart["unit"] and tuple(chart["original_basis_weights"]) == tuple(model.weights) and
            model.weights[i] == 0 and all(not value for j,value in enumerate(engine.unit) if j != i),
            "Changed the original scalar fraction, weight-zero unit, or one of its charts")
    unit = engine.unit[i]
    require(unit and unit.degree() == 0 and unit[0] == model.unit_scalar, "Changed the original constant unit coordinate")
    inverse = k.one()/unit[0]
    n, d = R(inverse*N[i]), R(inverse*D[i])
    require(n and d and n*engine.unit == N and d*engine.unit == D,
            "The entire numerator and denominator did not lie on the actual scalar unit line")
    t = R.gen()
    if flag:
        u,v = (((1-9*t**2)**2,t**2*(1-t**2)**2) if name == "T" else (1-t**2,t**2))
    else:
        u,v = ((t**2*(t**2-9)**2,(t**2-1)**2) if name == "T" else (t**2-1,R.one()))
    require(u.gcd(v) == R.one() and n*v == d*u, "The physical scalar source did not represent the original T or v")
    g = n.gcd(d).monic()
    c, rem_n = n.quo_rem(g)
    b, rem_d = d.quo_rem(g)
    require(not rem_n and not rem_d and g*b == d and g*c == n, "Common polynomial did not return both raw scalars")
    lam = k.one()/b.leading_coefficient()
    b,c = lam*b,lam*c
    one, x, y = b.xgcd(c)
    require(b.is_monic() and one == R.one() and x*b+y*c == R.one() and d*c == n*b and
            b==v.monic() and c.monic()==u.monic(), "The complete source scalar or ratio unit changed")
    return n,d,b,c,dict(original_fraction=OWNERS[name], chart=flag, actual_unit_coordinate=i,
        source_N=element_digest(N), source_D=element_digest(D), physical_scalars=[polynomial_digest(n),polynomial_digest(d)],
        actual_common_gcd=polynomial_digest(g), common_normalizing_unit=polynomial_digest(R(lam)),
        actual_coprime_denominator=polynomial_digest(b), actual_paired_numerator=polynomial_digest(c),
        physical_ratio_retained=True, complete_polynomial_bezout=[polynomial_digest(x),polynomial_digest(y)])


class ScalarSource:
    """Independent immutable inner and post-ideal views in the original ring."""
    def __init__(self,H,B,C):
        self.H,self.B,self.C = tuple(outer.freeze_matrix(value) for value in (H,B,C))
        self.R, self.n = self.B.base_ring(), int(self.B.nrows())
        self.b, self.c = self.B[0,0], self.C[0,0]
        ident = identity_matrix(self.R,self.n)
        require(self.b and self.c and self.b.is_monic() and self.b.gcd(self.c) == self.R.one() and
                self.H == self.B == self.b*ident and self.C == self.c*ident and
                self.H.is_immutable() and self.B.is_immutable() and self.C.is_immutable(),
                "The immutable scalar graph did not return its complete two input blocks")

    def decode(self, h):
        require(h.base_ring() is self.R and len(h) == self.n, "Foreign complete Hermite row")
        coefficients = []
        for value in h:
            quotient,rem = value.quo_rem(self.b)
            require(not rem, "A whole original negative row failed exact division")
            coefficients.append(quotient)
        row = vector(self.R,coefficients)
        require(self.b*row == h, "A complete original-domain scalar source row failed its inverse return")
        return self.c*row


def prepare_projected_body():
    require(hashlib.sha256(Path(outer.__file__).read_bytes()).hexdigest() == PINNED_OUTER,
            "Changed the original complete projected-pair implementation")
    original = outer.projected_pair_after_proof
    require(original.__globals__ is vars(outer) and original.__closure__ is None,
            "Changed original complete projected-pair source owner")
    body = textwrap.dedent(inspect.getsource(original))
    previous = "    if engine.unit*MN!=N or engine.unit*MD!=D:"
    current = "    _verify_current_scalar_operators(MN,MD)\n"+previous
    require(body.count(previous)==1 and "_verify_current_scalar_operators" not in body,
            "Changed full original operator creation site")
    new = body.replace(previous,current,1)
    require(new.replace(current,previous,1)==body, "Nonreversible complete operator check")
    return compile(new,str(Path(outer.__file__))+":four-scalar-direct-graphs","exec"),dict(
        original_outer_function_sha256=hashlib.sha256(body.encode()).hexdigest(),
        actual_outer_function_with_operator_gate_sha256=hashlib.sha256(new.encode()).hexdigest(),
        extra_operator_checks_in_original_body=1)


def actual_pair(six,engines,function,flag,N,D,label,name):
    engine = engines[flag]
    n,d,b,c,proof = exact_inputs(six,engines,function,flag,N,D,name)
    I = engine.identity
    require(I == identity_matrix(engine.R,306), "Changed original 306-dimensional identity")
    Y,X = b*I,c*I
    G = c.monic()*I
    calls = []
    def operators(MN,MD):
        require(MN.base_ring() is MD.base_ring() is engine.R and MN==n*I and MD==d*I,
                "A real full 306x306 original multiplication operator differs from its source scalar")
        calls.append("operators")
    def project(left,attached,bound,progress=None,try_prime=True):
        require(progress is engine.progress and bound == (1836 if name=="T" else 612),
                "Changed original scalar graph projection owner")
        if len(calls)==1:
            require(calls==["operators"] and left is Y and attached is X and
                    Y.is_hermite() and Y==b*I and X==c*I and b.is_monic(), "Wrong original negative projection")
            H,section,image,factor = Y,Y,X,engine.k.one()
            calls.append("negative")
        else:
            require(calls==["operators","negative"] and left is X and attached is None and
                    G.is_hermite() and G==c.monic()*I, "Wrong original independent positive projection")
            H,section,image,factor = G,G,None,c.leading_coefficient()
            calls.append("positive")
        require(left==factor*H and H==(engine.k.one()/factor)*left and
                quadratic.complete_remainder_rows(left,H).is_zero() and
                quadratic.complete_remainder_rows(section,H).is_zero(),
                "Full projection submodule or dynamic original complete Hermite remainder changed")
        return H,section,image,dict(method="complete original scalar projection with two inverse units",
            original_source_sha256=polynomial_matrix_digest(left),full_hnf_sha256=polynomial_matrix_digest(H),
            attached_source_sha256=None if image is None else polynomial_matrix_digest(image),
            full_forward_reverse_polynomial_module_return=True)
    def admit(yy,xx,minus,plus):
        require(calls==["operators","negative","positive"] and yy is Y and xx is X and minus is Y and plus is G and
                Y==b*I and X==c*I and G==c.monic()*I, "The two pre-construction complete scalar modules changed")
        return dict(complete_graph_for_this_full_original_function=True,route="complete coprime scalar Bezout graph",
                    physical_source=proof,actual_owner=id(function),infinity_chart=flag)
    namespace = dict(outer.projected_pair_after_proof.__globals__)
    require(namespace["projection_return"] is outer.projection_return and namespace["PairedSource"] is outer.PairedSource and
            namespace["graph_scan"] is outer.graph_scan and namespace["original_operator_product"] is outer.original_operator_product,
            "Changed an original complete-projection dependency")
    namespace.update(projection_return=project,PairedSource=ScalarSource,_verify_current_scalar_operators=operators)
    exec(SCALAR_CODE,namespace)
    run = namespace["projected_pair_after_proof"]
    pos,neg,ret = run(engine,N,D,Y,X,label,admit,1836 if name=="T" else 612,max(six["model"].weights))
    require(pos.basis==G and neg.basis==Y and pos.length==306*c.degree() and neg.length==306*b.degree() and
            ret["post_ideal_outer"]["source_row_count_verified_after_both_ideals"]==306,
            "Wrong returned complete physical scalar ideal")
    ret.update(original_function=label,numerator_sha256=element_digest(N),denominator_sha256=element_digest(D),
        zero_ideal=pos.receipt,pole_ideal=neg.receipt,concrete_implementation="original complete coprime scalar graph",
        only_this_affine_chart=True,closed_points_or_shadow_claimed=False,
        common_zeros_handled_by_complete_polynomial_syzygy=True)
    return pos,neg,ret


def bind_after_endpoint_selector(module, endpoint_binding):
    global CURRENT,SCALAR_CODE
    require(CURRENT is None and not SEEN and not module.SESSIONS and module.scalar._new_geometry_runner is module._new_geometry_runner and
            module._new_geometry_runner.__globals__ is vars(module) and endpoint_binding["reversible_new_call_sites"]==1 and
            endpoint_binding["mathematical_instances_by_binding"]==0, "Bind the pinned original endpoint selector first")
    SCALAR_CODE,prepared = prepare_projected_body()
    previous = module.EndpointSession
    class ScalarAndEndpoint(previous):
        def selected(self,six,engines,function,flag,N,D,label):
            names = [name for name in OWNERS if function is six[name]]
            if not names:
                require(label not in OWNERS.values(), "The scalar label belongs to a different original object")
                return super().selected(six,engines,function,flag,N,D,label)
            name, = names
            require(label==OWNERS[name] and all(entry[3:5]!=(name,flag) for entry in SEEN),
                    "Changed original scalar graph label or duplicate chart")
            result=actual_pair(six,engines,function,flag,N,D,label,name)
            SEEN.append((self,six,engines,name,flag,N,D,*result))
            return result
    module.EndpointSession = ScalarAndEndpoint
    CURRENT = (module,previous,ScalarAndEndpoint)
    return dict(prepared=prepared,same_original_endpoint_session_runner=True,
                unchanged_endpoint_selector_body=endpoint_binding["prepared_body"], mathematical_instances_by_binding=0)


def actual_scalar_graph_usage(context, support_usage):
    require(CURRENT is not None and context["certificate"]["status"]=="all_requested_original_acceptance_gates_completed" and
            support_usage["actual_scalar_primary_call_count"]==13 and support_usage["actual_infinity_boundary_call_count"]==4 and
            support_usage["actual_base_prime_factor_call_count"]==9, "Incomplete original geometric acceptance or old scalar audit")
    module,previous,bound=CURRENT
    geo,six=context["geometry"],context["six"]
    require(module.EndpointSession is bound and bound.__bases__==(previous,) and len(module.SESSIONS)==1 and
            module.scalar._new_geometry_runner is module._new_geometry_runner and geo["six"] is six and
            [(row[3],row[4]) for row in SEEN]==[(name,flag) for name in ("T","vs") for flag in (False,True)],
            "Any of the four actual scalar chart returns is absent or out of order")
    result=[]
    for own,src,engines,name,flag,N,D,pos,neg,ret in SEEN:
        fn,engine=six[name],engines[flag]
        item=geo["complete_principal_divisor_cache"][id(fn)]
        n,d,b,c,source=exact_inputs(src,engines,fn,flag,N,D,name)
        graph,outer_record=ret["kernel"],ret["post_ideal_outer"]
        scan=graph["all_rows"]
        require(own is module.SESSIONS[0] and type(own) is bound and src is six and engines is geo["engines"] and
                item["function"] is fn and ret is item["records"][str(flag)] and
                pos is item["charts"][flag]["positive"] and neg is item["charts"][flag]["negative"] and
                pos.engine is neg.engine is engine and pos.basis==c.monic()*engine.identity and neg.basis==b*engine.identity and
                ret["zero_ideal"]==pos.receipt and ret["pole_ideal"]==neg.receipt and
                graph["complete_low_graph"]["actual_owner"]==id(fn) and graph["complete_low_graph"]["physical_source"]==source and
                graph["original_G_N_sha256"]==source["source_N"] and graph["original_G_D_sha256"]==source["source_D"] and
                graph["full_MN_sha256"]==polynomial_matrix_digest(n*engine.identity) and
                graph["full_MD_sha256"]==polynomial_matrix_digest(d*engine.identity) and
                outer_record["actual_positive_id"]==id(pos) and outer_record["actual_negative_id"]==id(neg) and
                outer_record["actual_engine_id"]==id(engine) and outer_record["infinity_chart"] is flag and
                outer_record["actual_numerator_input_id"]==id(N) and outer_record["actual_denominator_input_id"]==id(D) and
                outer_record["positive_hnf_sha256"]==polynomial_matrix_digest(pos.basis) and
                outer_record["negative_hnf_sha256"]==scan["complete_hermite_sha256"]==polynomial_matrix_digest(neg.basis) and
                outer_record["source_row_count_verified_after_both_ideals"]==306 and
                [r["index"] for r in scan["complete_source_rows"]]==list(range(306)) and
                all(r["exact_full_residual_zero"] for r in scan["complete_source_rows"]) and
                outer_record["complete_post_ideal_row_stream_sha256"]==digest(scan["complete_source_rows"]) and
                outer_record["complete_X_sha256"]==scan["complete_X_sha256"]==polynomial_matrix_digest(c*engine.identity),
                "The final original scalar geometry consumer, raw operators, complete X, or either genuine HNF changed")
        result.append(dict(original_function=name,infinity_chart=flag,actual_graph_sha256=digest(graph),
                           positive_length=int(pos.length),negative_length=int(neg.length),whole_post_ideal=outer_record))
    return dict(actual_original_four_scalar_graphs=result,existing_support_primary_calls=13,
                raw_operators_checked_twice_and_306_inner_outer_rows_per_chart=True)
