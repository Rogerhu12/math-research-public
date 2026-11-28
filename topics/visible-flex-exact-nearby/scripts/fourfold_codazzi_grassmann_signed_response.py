"""Two actual signed low193 responses, original boundary units, and whole-cell readout."""
from fractions import Fraction


def require(ok, message):
    if not ok:
        raise ValueError(message)


def interval_matrix(engine, ball):
    """Each entry of the actual matrix lies in centre plus/minus its joint radius."""
    error = engine.api.interval(-ball.r,ball.r)
    return engine.km.Matrix(ball.rows,ball.cols,[[x+error for x in row] for row in ball.c.values])


def peano_columns(api, km, flow, coefficient, forcing, initial, duration, order):
    """Vector-only inhomogeneous Picard polynomial for both endpoint and all earlier times.

    term1=h*(A*x+f), term(k+1)=h*A*term(k)/(k+1). All factors can vary
    independently on the subbox. Entire signed forcing contains both columns.
    The first-term bound scales the tail of exp(beta), without dividing by beta.
    """
    require(coefficient.shape == (193,193) and initial.shape == forcing.shape == (193,2)
            and api.lower(duration) > 0 and type(order) is int and order >= 2,
            "all physical low rows, actual source columns, true duration")
    generator = api.arb_mat(coefficient.values)*duration
    x = api.arb_mat(initial.values)
    term = (api.arb_mat(coefficient.values)*x+api.arb_mat(forcing.values))*duration
    one = km.Matrix(193,2,[[term[i,j] for j in range(2)] for i in range(193)])
    beta = flow.infinity_upper(api,km.scale(api,duration,coefficient))
    gap = (api.one-beta/(order+2)).lower()
    require(api.lower(gap) > 0, "strict complete column Peano tail")
    tail = flow.infinity_upper(api,one)
    unit = api.interval(api.zero,api.one)
    endpoint,span = x+term,x+term*unit
    for k in range(2,order+1):
        term = (generator*term)*api.rational(1,k)
        endpoint,span = endpoint+term,span+term*unit
        tail = (tail*beta/k).upper()
    tail = (tail*beta/(order+1)/gap).upper()
    remainder = api.interval(-tail,tail)
    def finish(matrix):
        return km.Matrix(193,2,[[matrix[i,j]+remainder for j in range(2)] for i in range(193)])
    return finish(endpoint),finish(span)


def cell_columns(engine, model, provider, balances, forcing, panel, initial, observe=None):
    e,api,km,flow = engine,engine.api,engine.km,engine.flow
    context = model["context"]
    domain = context.domain
    require(provider.context is context and forcing.domain is domain and forcing.source_roles == (),
            "same varying operator and original ordinary source without previous map targets")
    factor = balances[domain.cells[panel]["parent_panel"]]
    diagonal = [api.one]*96+[factor]*97
    x = flow.diagonal_left(km,initial,diagonal)
    cuts = {Fraction(j,4) for j in range(5)}
    # At fixed physical panels, use actual endpoints for cut and shell.
    # The single uncertain root panel is far from all three physical cuts.
    whole = domain.exact_physical_cover((panel,Fraction(0),Fraction(1)))
    for point in (Fraction(17,20),Fraction(9,10),Fraction(19,20)):
        if whole[0] < point < whole[1]:
            require(domain.cells[panel]["parent_panel"] > 0,"cut inside a fixed physical panel")
            cuts.add((point-whole[0])/(whole[1]-whole[0]))
    cuts = sorted(cuts)
    pending = list(reversed(list(zip(cuts,cuts[1:]))))
    while pending:
        lo,hi = pending.pop()
        box = panel,lo,hi
        coefficient = flow.diagonal_similarity(km,provider.centre_matrix(flow.HEAD,flow.HEAD,box),diagonal)
        duration = domain.full_length(panel)*domain.exact(hi-lo)
        beta = flow.infinity_upper(api,km.scale(api,duration,coefficient))
        if not api.lower((api.one-beta/18).lower()) > 0:
            require(hi-lo > Fraction(1,64), "strict signed column denominator at finest local cut")
            mid = (lo+hi)/2
            pending.extend(((mid,hi),(lo,mid)))
            continue
        ordinary = flow.diagonal_left(km,forcing(box),diagonal)
        x,span = peano_columns(api,km,flow,coefficient,ordinary,x,duration,16)
        if observe is not None:
            observe(box,duration,flow.diagonal_left(km,span,diagonal,inverse=True),
                    flow.diagonal_left(km,x,diagonal,inverse=True))
    return flow.diagonal_left(km,x,diagonal,inverse=True)


def solve(engine, model, provider, balances, forcing, left96, charted_right97, observe,
          progress=None):
    e,api,km = engine,engine.api,engine.km
    require(model["kind"] == "R149_actual_low193_joint_Grassmann_inverse_v1"
            and model["true_hybrid_BVP_verified"] is True and model["complete_refined_cells"] == 1424
            and left96.shape == (96,2) and charted_right97.shape == (97,2),
            "same genuinely complete hybrid and two entire boundary data columns")
    store,n = model["joint_store"],model["complete_refined_cells"]
    def node(i,key):
        return store.get(("node",i,key))
    right = e.from_interval(km.Matrix(97,2,[
        [x/model["context"].reference_thetas[i+1] if i < 96 else x for x in row]
        for i,row in enumerate(charted_right97.values)]))
    outer_left = node(n,"left")
    top = e.add(e.rows(outer_left,range(96)),e.scale(api.rational(13,80),e.rows(outer_left,range(97,193))))
    outer = e.vcat(top,e.rows(outer_left,(96,)))
    a = e.multiply(e.inverse(outer),right)
    b = e.multiply(e.inverse(e.rows(node(0,"right"),range(97,193))),e.from_interval(left96))
    store.put(("response_a",n),a)
    for i in range(n-1,-1,-1):
        zero = km.zeros(api,193,2)
        inc = e.from_interval(cell_columns(e,model,provider,balances,forcing,i,zero))
        store.put(("signed_increment",i),inc)
        a = e.multiply(store.get(("Uinv",i)),e.subtract(a,e.multiply(node(i+1,"ell"),inc)))
        store.put(("response_a",i),a)
        if progress: progress("both_signed_increments_and_backward",n-i)
    root_atoms = outer_atoms = None
    for i in range(n+1):
        a = store.get(("response_a",i))
        x = e.add(e.multiply(node(i,"left"),a),e.multiply(node(i,"right"),b))
        store.remove(("response_a",i))
        if i == 0:
            root_atoms = e.rows(x,range(97))
        if i == n:
            rows = interval_matrix(e,e.rows(x,range(97,193))).values
            outer_atoms = e.from_interval(km.Matrix(96,2,[
                [model["context"].reference_thetas[j+1]*v for v in row] for j,row in enumerate(rows)]))
            break
        cell_columns(e,model,provider,balances,forcing,i,interval_matrix(e,x),observe)
        inc = store.get(("signed_increment",i))
        b = e.add(e.multiply(store.get(("Vinv",i)),b),e.multiply(node(i+1,"rho"),inc))
        store.remove(("signed_increment",i))
        if progress: progress("both_signed_whole_cell_responses",i+1)
    return {"kind":"R149_joint_full_cell_signed_low193_Newton_and_nu_response_v1",
            "private_model_token":model["private_model_token"],"root97":root_atoms,"outer96":outer_atoms,
            "whole_original_cells":n,"column_names":forcing.column_names,
            "independent_mean_retained":True,"original_charted_right_unweighted_once":True,
            "whole_four_map_targets_recomputed":0,"full_positive_or_negative_response_proved":False}


class CutAndShell:
    """Per signed column, one raw cut and the two original NGA ordinary-dr weighted windows."""
    def __init__(self, api, forcing):
        self.api,self.forcing = api,forcing
        self.start,self.cut,self.end = Fraction(17,20),Fraction(9,10),Fraction(19,20)
        self.cursor,self.trace = self.start,None
        self.low = [api.zero,api.zero]
        self.shell = [api.zero,api.zero]

    def __call__(self, box, duration, span, endpoint):
        from bisect import bisect_right
        api,f = self.api,self.forcing
        left,right = f.domain.exact_physical_cover(box)
        if right == self.cut:
            require(self.trace is None, "one exact physical cut endpoint")
            self.trace = endpoint
        if right <= self.start or left >= self.end:
            return
        require(self.cursor == left < right <= self.end, "whole ordered physical shell partition")
        self.cursor = right
        row = bisect_right(f.ends,left)
        cur,K = left,None
        while cur < right:
            r = f.rows[row]
            stop = min(f.ends[row],right)
            require(cur < stop and f.bounds[row][0] <= cur, "whole original shell K row")
            value = f.read_ball(r["intrinsic_whole_third_jets"]["K"])
            K = value if K is None else K.union(value)
            row += 1
            cur = stop
        require(api.lower(K) > 0, "positive actual physical curvature on the whole shell")
        # Squares of K^(-1/4), K^(1/4), exactly once, act on odd and even.
        wv = api.sqrt(K)
        wu = api.one/wv
        for col in range(2):
            for j,rows in enumerate(((range(96),range(96,193)),(range(32,96),range(129,193)))):
                odd,even = rows
                bound = wu*sum((api.magnitude(span.values[i][col])**2 for i in odd),api.zero)
                bound += wv*sum((api.magnitude(span.values[i][col])**2 for i in even),api.zero)
                acc = self.low if j == 0 else self.shell
                acc[col] += duration.upper()*bound.upper()

    def complete(self):
        require(self.trace is not None and self.cursor == self.end,
                "the true cut and every shell interval were evaluated")
        return {"raw193_cut_columns":self.trace,
                "raw_cut_L2_upper":[self.api.sqrt(sum((self.api.magnitude(row[k])**2
                                    for row in self.trace.values),self.api.zero)).upper()
                                    for k in range(2)],
                "P_weighted_low96_L2_upper":[self.api.sqrt(x).upper() for x in self.low],
                "P_weighted_shell33_through96_L2_upper":[self.api.sqrt(x).upper() for x in self.shell],
                "physical_weight":"diag(K^(-1/4),K^(1/4))","origin":"same joint low193 hybrid BVP",
                "nonlinear_NGA_inputs_inferred":False}
