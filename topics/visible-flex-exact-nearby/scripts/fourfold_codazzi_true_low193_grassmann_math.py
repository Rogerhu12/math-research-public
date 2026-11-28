"""New joint-norm Grassmann charts for the SAME actual WVC low193 BVP.

Floating arithmetic selects nonzero dyadic Householder vectors only. The
mathematical frame is their exact rational orthogonal product. Every matrix
evaluation, local varying-flow error, graph radius, boundary mean, transpose
and complete source covariance retains a directed error. No work at import.
Old TF prefix restoration and new post81 local packets have separate owners.
"""
from __future__ import annotations
import math
from array import array
from collections import OrderedDict

N, P, Q = 193, 97, 96
ROLES = ("ordinary_raw_low_source", "transformed_low_source",
         "low_second_kind_correction", "centre_high0_return_source")


def require(ok, message):
    if not ok:
        raise ValueError(message)


class MatrixBall:
    """One complete family of matrices in an induced-2 ball, never entrywise freedom."""
    def __init__(self, engine, centre, radius, known_norm=None):
        self.e, self.c = engine, centre
        self.rows, self.cols, self.shape = centre.rows, centre.cols, centre.shape
        self.r = engine.upper(radius)
        require(all(x.is_finite() and x.lower() == x.upper()
                    for row in centre.values for x in row), "the whole centre is exact dyadic")
        self._centre_norm = None
        self.known_norm = None if known_norm is None else engine.upper(known_norm)

    def centre_norm(self):
        if self._centre_norm is None:
            self._centre_norm = self.e.flow.two_upper(self.e.api,self.c)
        return self._centre_norm

    def norm(self):
        value = self.e.upper(self.centre_norm()+self.r)
        return value if self.known_norm is None else self.e.minimum(value,self.known_norm)


class Engine:
    def __init__(self, api, km, green, flow):
        self.api,self.km,self.green,self.flow = api,km,green,flow

    def upper(self, value):
        require(value.is_finite(), "finite complete directed scalar")
        out = value.upper()
        require(self.api.lower(out) >= 0, "nonnegative complete norm upper")
        return out

    def minimum(self, a, b):
        a,b = self.upper(a),self.upper(b)
        return a if bool(a <= b) else b

    def exact_float(self, value):
        require(math.isfinite(value), "finite explicit binary64 centre")
        n,d = value.as_integer_ratio()
        out = self.api.rational(n,d)
        require(out.lower() == out.upper(), "exact dyadic at the declared precision")
        return out

    def from_interval(self, matrix, extra_radius=None, known_norm=None):
        """Pay the full Frobenius rounding/box error once, then keep one joint ball."""
        api = self.api
        square,values = api.zero,[]
        for row in matrix.values:
            fresh = []
            for value in row:
                require(value.is_finite(), "complete finite interval matrix")
                centre = self.exact_float(float(value.mid()))
                error = api.magnitude(value-centre)
                square += error*error
                fresh.append(centre)
            values.append(fresh)
        radius = api.sqrt(square)
        if extra_radius is not None:
            radius += self.upper(extra_radius)
        return MatrixBall(self,self.km.Matrix(matrix.rows,matrix.cols,values),radius,known_norm)

    def as_ball(self, value):
        if isinstance(value,MatrixBall):
            require(value.e is self, "same complete directed arithmetic engine")
            return value
        return self.from_interval(value)

    def zero(self, rows, cols):
        return MatrixBall(self,self.km.zeros(self.api,rows,cols),self.api.zero,self.api.zero)

    def eye(self, n):
        return MatrixBall(self,self.km.eye(self.api,n),self.api.zero,self.api.one)

    def transpose(self, value):
        return MatrixBall(self,self.km.transpose(value.c),value.r,value.norm())

    def add(self, *values):
        require(values and all(v.e is self for v in values), "one complete joint arithmetic")
        return self.from_interval(self.km.add(self.api,*(v.c for v in values)),
            sum((v.r for v in values),self.api.zero),
            sum((v.norm() for v in values),self.api.zero))

    def scale(self, scalar, value):
        require(scalar.is_finite(), "whole real scalar multiplier")
        a = self.api.magnitude(scalar)
        return self.from_interval(self.km.scale(self.api,scalar,value.c),
                                  a*value.r,a*value.norm())

    def subtract(self, first, second):
        return self.add(first,self.scale(-self.api.one,second))

    def multiply(self, first, second):
        require(first.e is second.e is self and first.cols == second.rows,
                "whole compatible joint product")
        error = self.minimum(first.norm()*second.r+second.centre_norm()*first.r,
                             first.centre_norm()*second.r+second.norm()*first.r)
        return self.from_interval(self.km.multiply(self.api,first.c,second.c),error,
                                  first.norm()*second.norm())

    def product(self, *values):
        require(values, "nonempty ordered matrix product")
        out = values[0]
        for value in values[1:]:
            out = self.multiply(out,value)
        return out

    def inverse(self, value):
        require(value.rows == value.cols > 0, "whole finite square joint inverse")
        raw = self.green.directed_inverse(self.api,self.km,value.c)
        centre_inverse = self.from_interval(raw)
        g = centre_inverse.norm()
        gap = (self.api.one-g*value.r).lower()
        require(self.api.lower(gap) > 0, "strict complete joint inverse denominator")
        return MatrixBall(self,centre_inverse.c,
            self.upper(centre_inverse.r+g*g*value.r/gap),self.upper(g/gap))

    def submatrix(self, value, rows, cols):
        require(len(set(rows)) == len(rows) and len(set(cols)) == len(cols),
                "coordinate orthogonal projections contain no repeated coordinate")
        matrix = self.green.submatrix(self.km,value.c,tuple(rows),tuple(cols))
        return MatrixBall(self,matrix,value.r,value.norm())

    def rows(self, value, indices):
        return self.submatrix(value,indices,range(value.cols))

    def columns(self, value, indices):
        return self.submatrix(value,range(value.rows),indices)

    def hcat(self, *values):
        radius = self.api.sqrt(sum((v.r*v.r for v in values),self.api.zero))
        bound = self.api.sqrt(sum((v.norm()**2 for v in values),self.api.zero))
        return MatrixBall(self,self.km.hcat(*(v.c for v in values)),radius,bound)

    def vcat(self, *values):
        radius = self.api.sqrt(sum((v.r*v.r for v in values),self.api.zero))
        bound = self.api.sqrt(sum((v.norm()**2 for v in values),self.api.zero))
        return MatrixBall(self,self.km.vcat(*(v.c for v in values)),radius,bound)

    def quadratic(self, middle, sides):
        return self.product(self.transpose(sides),middle,sides)

    def trace_product_upper(self, first, second):
        """For an actual nonnegative Gram contraction, retain every signed centre entry."""
        require(first.rows == first.cols == second.rows == second.cols,
                "whole equal-size signed trace contraction")
        n,api = first.rows,self.api
        centre = sum((first.c.values[i][j]*second.c.values[j][i]
                       for i in range(n) for j in range(n)),api.zero)
        error = n*(first.r*second.centre_norm()+second.r*first.centre_norm()+first.r*second.r)
        return self.upper(centre+error)


def propose_householders(np, engine, propagated_columns):
    """Select exact dyadic vectors; floating orthogonality is never used as evidence."""
    require(propagated_columns.shape == (N,P), "all97 propagated free columns including mean")
    work = np.array([[float(x.mid()) for x in row]
                     for row in propagated_columns.values],dtype=float)
    require(np.all(np.isfinite(work)), "finite whole chart proposal")
    vectors = []
    for j in range(P):
        x = work[j:,j].copy()
        size = float(np.linalg.norm(x))
        require(math.isfinite(size), "finite proposal scale")
        if size == 0:
            v = np.zeros(N-j,dtype=float)
            v[0] = 1.0
        else:
            x[0] += math.copysign(size,float(x[0]))
            scale = float(np.max(np.abs(x)))
            require(math.isfinite(scale) and scale > 0, "nonzero proposed reflector")
            v = x/scale
        denominator = float(v@v)
        require(math.isfinite(denominator) and denominator > 0, "positive proposal denominator")
        work[j:,:] -= (2.0/denominator)*np.outer(v,v@work[j:,:])
        full = [0.0]*j+[float(x) for x in v]
        require(len(full) == N and all(math.isfinite(x) for x in full), "whole dyadic reflector")
        vectors.append(full)
    return vectors


def certify_householder_frame(engine, vectors):
    """Q is the EXACT rational product H(v), not its rounded evaluated centre.

    Each nonzero dyadic v defines H=I-2vv^t/(v^tv), so H^tH=I exactly.
    The complete matrix evaluation gets a separate joint error. Norm one,
    inverse=adjoint and condition one refer only to that exact rational Q.
    """
    e,api = engine,engine.api
    require(len(vectors) in (0,P), "identity root frame or all97 whole reflectors")
    native = api.arb_mat(e.km.eye(api,N).values)
    for j,values in enumerate(vectors):
        require(len(values) == N and all(x == 0.0 for x in values[:j]),
                "complete prescribed Householder coordinates")
        vector = [e.exact_float(float(x)) for x in values]
        denominator = sum((x*x for x in vector),api.zero)
        require(api.lower(denominator) > 0, "strict denominator of the exact rational reflector")
        column,row = api.arb_mat([[x] for x in vector]),api.arb_mat([vector])
        native = native-((native*column)*row)*(api.rational(2)/denominator)
    matrix = e.km.Matrix(N,N,[[native[i,j] for j in range(N)] for i in range(N)])
    return e.from_interval(matrix,known_norm=api.one)


def advance_graph(engine, transfer, graph, new_centre=None):
    """General centred fractional graph step, including all original mean entries."""
    e,api = engine,engine.api
    q,p = graph.rows,graph.cols
    require(p+q == transfer.rows == transfer.cols == N, "whole complementary graph dimensions")
    ix,iy = tuple(range(p)),tuple(range(p,N))
    A,B = e.submatrix(transfer,ix,ix),e.submatrix(transfer,ix,iy)
    C,D = e.submatrix(transfer,iy,ix),e.submatrix(transfer,iy,iy)
    centre = MatrixBall(e,graph.c,api.zero,graph.centre_norm())
    Ac = e.add(A,e.multiply(B,centre))
    inverse_centre = e.inverse(Ac)
    if new_centre is None:
        prediction = e.multiply(e.add(C,e.multiply(D,centre)),inverse_centre)
        proposed = MatrixBall(e,prediction.c,api.zero)
    else:
        proposed = new_centre
    require(proposed.shape == (q,p) and api.lower(proposed.r) == 0
            and proposed.r.upper() == 0, "a complete exact dyadic proposed graph centre")
    Rc = e.subtract(e.add(C,e.multiply(D,centre)),e.multiply(proposed,Ac))
    L = e.subtract(D,e.multiply(proposed,B))
    g,b = inverse_centre.norm(),B.norm()
    gap = (api.one-g*b*graph.r).lower()
    require(api.lower(gap) > 0, "strict centred Grassmann denominator")
    radius = e.upper(g*(Rc.norm()+L.norm()*graph.r)/gap)
    updated = MatrixBall(e,proposed.c,radius)
    inverse = MatrixBall(e,inverse_centre.c,
        e.upper(inverse_centre.r+g*g*b*graph.r/gap),e.upper(g/gap))
    return updated,inverse,{"complete_denominator_lower":gap,
        "complete_graph_radius_upper":radius,"complete_previous_radius_upper":graph.r,
        "complete_centre_residual_upper":Rc.norm(),"mean_coordinate_deleted":False}


def original_outer_boundary(engine, value):
    e = engine
    top = e.add(e.rows(value,range(96)),
                e.scale(e.api.rational(13,80),e.rows(value,range(97,193))))
    return e.vcat(top,e.rows(value,(96,)))


def store_complete_node(engine, store, index, frame, Z, Y):
    e = engine
    W = e.inverse(e.subtract(e.eye(Q),e.multiply(Z,Y)))
    YW,WZ = e.multiply(Y,W),e.multiply(W,Z)
    left = e.multiply(frame,e.vcat(e.eye(P),Z))
    right = e.multiply(frame,e.vcat(Y,e.eye(Q)))
    ell = e.multiply(e.hcat(e.add(e.eye(P),e.multiply(YW,Z)),
                            e.scale(-e.api.one,YW)),e.transpose(frame))
    rho = e.multiply(e.hcat(e.scale(-e.api.one,WZ),W),e.transpose(frame))
    for name,value in (("left",left),("right",right),("ell",ell),("rho",rho)):
        store.put(("node",index,name),value)
    return W.norm()


class JointStore:
    """Private exact binary64 centres and one guarded joint radius per WHOLE matrix."""
    def __init__(self, engine, maximum_bytes=2147483648, maximum_decoded_entries=200000):
        self.e,self.maximum_bytes = engine,maximum_bytes
        self.maximum_decoded_entries = maximum_decoded_entries
        self.data,self.cache = {},OrderedDict()
        self.live_bytes,self.peak_bytes,self.decoded_entries = 0,0,0

    def _outward_float(self, value):
        value = self.e.upper(value)
        out = float(value)
        require(math.isfinite(out) and out >= 0, "finite private joint radius")
        for unused in range(4):
            if bool(self.e.exact_float(out) >= value):
                return out
            out = math.nextafter(out,math.inf)
        raise ValueError("complete private joint-radius containment")

    def put(self, key, value):
        require(key not in self.data, "one complete private joint matrix per key")
        values = array("d")
        for row in value.c.values:
            for entry in row:
                x = float(entry)
                require(self.e.exact_float(x) == entry, "private centre is unchanged exact dyadic")
                values.append(x)
        radius,bound = self._outward_float(value.r),self._outward_float(value.norm())
        size = len(values)*values.itemsize+16
        require(self.live_bytes+size <= self.maximum_bytes, "whole private joint-store byte cap")
        self.data[key] = (value.rows,value.cols,values,radius,bound)
        self.live_bytes += size
        self.peak_bytes = max(self.peak_bytes,self.live_bytes)

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        rows,cols,values,radius,bound = self.data[key]
        matrix = self.e.km.Matrix(rows,cols,[[self.e.exact_float(values[i*cols+j])
                                    for j in range(cols)] for i in range(rows)])
        out = MatrixBall(self.e,matrix,self.e.exact_float(radius),self.e.exact_float(bound))
        self.cache[key] = out
        self.decoded_entries += rows*cols
        while self.decoded_entries > self.maximum_decoded_entries and len(self.cache) > 1:
            unused,old = self.cache.popitem(last=False)
            self.decoded_entries -= old.rows*old.cols
        return out

    def remove(self, key):
        rows,cols,values,unused_radius,unused_bound = self.data.pop(key)
        self.live_bytes -= len(values)*values.itemsize+16
        if key in self.cache:
            old = self.cache.pop(key)
            self.decoded_entries -= old.rows*old.cols


def certify_complete_joint_model(np, engine, context, packet_provider,
                                  freeze_vectors, store, progress=None):
    """Use restored raw flows on0..80; NEW packets on81..1423, in original order.

    packet_provider never reintegrates a restored cell. Each complete packet
    contains both raw flows and every one of the five full raw moments.
    freeze_vectors saves/reads the entire new dyadic definition before use.
    The new graph inclusion differs from the old fixed-chart81 pivot target.
    """
    e,api = engine,engine.api
    count = len(context.domain.cells)
    require(count == 1424 and context.qualifications["same_WVC_reference"] is True,
            "the full original true-root WVC domain")
    frame,Z = certify_householder_frame(e,[]),e.zero(Q,P)
    store.put(("frame",0),frame); store.put(("Z",0),Z)
    left_records,right_records,node_records,statistics = [],[],[],[]
    for i in range(count):
        packet = packet_provider(i,"left")
        require(packet["panel"] == i and packet["all193_coordinates_retained"] is True
                and set(packet["true_moments"]["inputs"]) == set(ROLES),
                "one complete ordered local packet, with every source role")
        forward = e.as_ball(packet["forward"])
        proposed_columns = e.product(forward,frame,e.vcat(e.eye(P),
            MatrixBall(e,Z.c,api.zero,Z.centre_norm()))).c
        vectors = freeze_vectors(i+1,propose_householders(np,e,proposed_columns))
        next_frame = certify_householder_frame(e,vectors)
        transfer = e.product(e.transpose(next_frame),forward,frame)
        Z,C,record = advance_graph(e,transfer,Z)
        store.put(("frame",i+1),next_frame)
        store.put(("Z",i+1),Z); store.put(("Uinv",i),C)
        left_records.append(record)
        statistics.append({key:packet[key] for key in
            ("panel","subboxes","beta_sum_upper","beta2_sum_upper",
             "complete_raw_prefix_and_inverse_upper","largest_local_tail_upper")})
        frame,Z = store.get(("frame",i+1)),store.get(("Z",i+1))
        if progress is not None:
            progress("new_joint_left_graph",{"complete_cells":i+1,"whole_cells":count,
                "original_TF_accepted_records_reissued":0,"index":i,
                "complete_record":record})
    outer = original_outer_boundary(e,frame)
    Y = e.scale(-api.one,e.multiply(e.inverse(e.columns(outer,range(P))),
                                    e.columns(outer,range(P,N))))
    node_records.append((count,store_complete_node(e,store,count,frame,Z,Y)))
    if progress is not None:
        progress("new_joint_outer_node",{"index":count,
            "transversality_inverse_upper":node_records[-1][1]})
    store.remove(("Z",count))
    swap = tuple(range(P,N))+tuple(range(P))
    for i in range(count-1,-1,-1):
        packet = packet_provider(i,"right")
        previous_frame = store.get(("frame",i))
        backward = e.as_ball(packet["backward"])
        transfer = e.product(e.transpose(previous_frame),backward,frame)
        reverse_graph_transfer = e.submatrix(transfer,swap,swap)
        Y,D,record = advance_graph(e,reverse_graph_transfer,Y)
        store.put(("Vinv",i),D)
        Z = store.get(("Z",i))
        node_records.append((i,store_complete_node(e,store,i,previous_frame,Z,Y)))
        store.remove(("Z",i))
        right_records.append(record)
        frame = previous_frame
        if progress is not None:
            progress("new_joint_right_graph_and_transversality", {
                "complete_cells":count-i,"whole_cells":count,"complete_nodes":count-i+1,
                "index":i,"complete_record":record,
                "transversality_inverse_upper":node_records[-1][1]})
    require(len(left_records) == len(right_records) == count
            and len(node_records) == count+1, "all new joint inclusions and actual transversality")
    return {"kind":"R149_actual_low193_joint_Grassmann_inverse_v1",
        "context":context,"joint_store":store,"packet_provider":packet_provider,
        "complete_refined_cells":count,"local_statistics":statistics,
        "all_left_inclusions":left_records,"all_right_inclusions":right_records,
        "all_node_transversality":node_records,"private_model_token":object(),
        "true_hybrid_BVP_verified":True,"exact_rational_householder_frames":True,
        "all193_original_mean_and_boundary_coordinates_retained":True,
        "ordinary_dr_and_true_root_lengths_retained":True,
        "physical_S_replaced_by_internal_balance":False,
        "original_TF_accepted_records_reissued":0,
        "actual_full_positive_family_inverse_proved":False}


def complete_joint_source_maps(engine, model, progress=None):
    """All four whole maps, all193 atoms, both same-cell triangles; no prefix upgrade."""
    e,api = engine,engine.api
    require(model["true_hybrid_BVP_verified"] is True, "complete new actual inverse first")
    store,count = model["joint_store"],model["complete_refined_cells"]
    node = lambda i,name: store.get(("node",i,name))
    root = e.rows(node(0,"left"),range(P))
    root_accumulator = e.multiply(e.transpose(root),root)
    left_accumulator = e.zero(P,P)
    right_accumulators = {role:e.zero(Q,Q) for role in ROLES}
    body_squares,root_squares = ({role:api.zero for role in ROLES} for unused in range(2))
    for i in range(count):
        moments = model["packet_provider"](i,"maps")["true_moments"]
        X = e.as_ball(moments["output"])
        OL,OR = e.quadratic(X,node(i,"left")),e.quadratic(X,node(i,"right"))
        left_whole = e.add(left_accumulator,OL)
        C,D = store.get(("Uinv",i)),store.get(("Vinv",i))
        for role in ROLES:
            J = e.as_ball(moments["inputs"][role])
            IL = e.quadratic(J,e.transpose(node(i,"ell")))
            IR = e.quadratic(J,e.transpose(node(i,"rho")))
            right_whole = e.add(right_accumulators[role],IR)
            body_squares[role] += e.trace_product_upper(left_whole,IL)+e.trace_product_upper(OR,right_whole)
            root_squares[role] += e.trace_product_upper(root_accumulator,IL)
            right_accumulators[role] = e.quadratic(right_whole,e.transpose(D))
        left_accumulator = e.quadratic(left_whole,C)
        root_accumulator = e.quadratic(root_accumulator,C)
        if progress is not None:
            progress("new_joint_four_complete_source_covariances",{
                "complete_cells":i+1,"whole_cells":count,"roles":list(ROLES)})
    outer_raw = e.rows(node(count,"right"),range(97,N))
    theta = e.from_interval(e.km.Matrix(Q,Q,[[model["context"].reference_thetas[i+1]
        if i == j else api.zero for j in range(Q)] for i in range(Q)]))
    outer = e.multiply(theta,outer_raw)
    outer_gram = e.multiply(e.transpose(outer),outer)
    answers = {}
    for role in ROLES:
        body,root = e.upper(body_squares[role]),e.upper(root_squares[role])
        outer = e.trace_product_upper(outer_gram,right_accumulators[role])
        answers[role] = {"kind":"R149_actual_low193_joint_complete_source_map_v1",
            "source_role":role,"source_columns":128 if role == ROLES[3] else N,
            "complete_true_cells":count,"ordinary_dr":True,
            "body_HS2_upper":body,"root97_HS2_upper":root,"outer96_HS2_upper":outer,
            "body_norm_upper":e.upper(api.sqrt(body)),
            "atoms193_norm_upper":e.upper(api.sqrt(root+outer)),
            "complete_norm_upper":e.upper(api.sqrt(body+root+outer)),
            "all193_original_mean_and_boundary_observations_retained":True,
            "same_cell_triangles_bounded_by_two_complete_positive_squares":True,
            "actual_low_BVP_proved":True,"full_CFB_or_positive_family_inverse_inferred":False}
        record = answers[role]
        record.update({
            "actual_body_norm_upper": record["body_norm_upper"],
            "actual_atoms193_norm_upper": record["atoms193_norm_upper"],
            "actual_complete_source_norm_upper": record["complete_norm_upper"],
            "body_source_has_no_radial_derivative_assumption": True,
            "all193_mean_and_boundary_observations_retained": True,
            "high_return_is_original128_source_without_complete_CFB": True,
            "full_positive_inverse_or_original_RHS_claimed": False})
        if role == ROLES[2]:
            b,a = answers[role]["body_norm_upper"],answers[role]["atoms193_norm_upper"]
            answers[role]["actual_low_second_kind_inverse_upper"] = e.upper(
                (api.sqrt((2+b)**2+a*a)+api.sqrt(b*b+a*a))/2)
            answers[role]["all193_independent_atom_inputs_keep_their_identity"] = True
    return {"kind":"R149_actual_low193_joint_four_whole_source_maps_v1",
        "sources":answers,"private_model_token":model["private_model_token"],
        "complete":True,"source_roles_completed":list(ROLES),
        "same_actual_operator_and_full_original_observation_space":True}
