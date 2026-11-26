"""NP: complete finite trial residual for the full selected strict nu particular.

No IO or numerical import.  The public owner provides the original directed
TC arithmetic and whole old scalar jets.  Only necessary centre carriers
are materialized; the original D fees transfer the result to the implicit
selected member without reconstructing its large direction array.
"""
from bisect import bisect_left, bisect_right
from fractions import Fraction
from math import comb, factorial

A, B = Fraction(1,20), Fraction(9,50)
ALPHA = Fraction(6890507429876859,9007199254740992)
DIMENSION, HEAD, CENTRE_HEAD = 193, 96, 32
TRIAL_DENOMINATOR = 4096


def require(ok, message):
    if not ok:
        raise ValueError(message)


def complete_plan(rows, base_nodes):
    """An independent fixed trial mesh and the full exact certification cover."""
    nodes = sorted({Fraction(k,TRIAL_DENOMINATOR)
                    for k in range(int(B*TRIAL_DENOMINATOR)+1)} | {A,B})
    require(nodes[0] == 0 and nodes[-1] == B
            and all(0 < y-x <= Fraction(1,TRIAL_DENOMINATOR)
                    for x,y in zip(nodes,nodes[1:])), "the fixed rational proposal mesh")
    knots = [Fraction.from_float(float(x)) for x in base_nodes]
    plan = []
    cursor = Fraction(0)
    for row in rows:
        lo, hi = map(Fraction,row["interval"])
        if lo >= B:
            break
        lo, hi = max(lo,Fraction(0)),min(hi,B)
        if lo >= hi:
            continue
        cuts = sorted({lo,hi} | set(nodes[bisect_right(nodes,lo):bisect_left(nodes,hi)])
                      | set(knots[bisect_right(knots,lo):bisect_left(knots,hi)]))
        for left,right in zip(cuts,cuts[1:]):
            piece = bisect_right(knots,left)-1
            trial = bisect_right(nodes,left)-1
            require(left == cursor and left < right <= B
                    and knots[piece] <= left < right <= knots[piece+1]
                    and nodes[trial] <= left < right <= nodes[trial+1]
                    and (right <= A or left >= A), "one complete original/source/trial intersection")
            plan.append({"row":row["common_row"], "background_piece":piece,
                         "trial_piece":trial, "interval":[str(left),str(right)]})
            cursor = right
    require(cursor == B and plan, "every strict-source point, including its zero-source prefix")
    return nodes, plan


def base_background(c, module, base, offsets, piece, left, right, mean_scalar):
    """The original repaired M32 centre, with its complete radial mean s."""
    left,right = Fraction(left),Fraction(right)
    knot = Fraction.from_float(float(base["radial_nodes"][piece]))
    end = Fraction.from_float(float(base["radial_nodes"][piece+1]))
    require(knot <= left < right <= end, "one complete original centre cubic")
    raw = base["piece_coefficients"][:,piece,:][::-1]
    cs = [c.Box(x.reshape(65,1))*c.box(ALPHA) for x in raw]
    cs[0] = cs[0]+c.Box(offsets["lower"][piece,:,None],offsets["upper"][piece,:,None])
    cs = c.affine_polynomial(cs,(left+right)/2-knot,(right-left)/2)
    za,zb = (c.zeros((module.GRID,len(cs),1)) for _ in range(2))
    for order,x in enumerate(cs):
        zb[0,order,0] = c.CBox(x[32,0])
        for j in range(1,33):
            u,v = x[j-1,0]/2,x[32+j,0]/2
            za[j,order,0],za[-j,order,0] = c.CBox(0.,-u),c.CBox(0.,u)
            zb[j,order,0],zb[-j,order,0] = c.CBox(v),c.CBox(v)
    field = module.BatchRadialFourier
    return (field.from_fourier(c,za,32,0.,0),
            field.from_fourier(c,zb,32,0.,0)+mean_scalar)


def metric_T_jets(jets, read_ball):
    """Taylor jets through3 of beta/(2 gamma^2 a^2), including whole mean data."""
    beta = [read_ball(jets["beta"+str(k) if k else "beta"])/factorial(k) for k in range(4)]
    gamma = [read_ball(jets["gamma"+str(k) if k else "gamma"])/factorial(k) for k in range(4)]
    a = read_ball(jets["a"])
    require(a.lower() > 0 and gamma[0].lower() > 0, "full original positive metric denominators")
    radius = [a, beta[0]*a, (beta[1]+beta[0]**2)*a/2,
              (2*beta[2]+3*beta[0]*beta[1]+beta[0]**3)*a/6]
    def multiply(x,y):
        return [sum((x[j]*y[k-j] for j in range(k+1)),x[0]*0) for k in range(4)]
    def reciprocal(x):
        out = [1/x[0]]
        for k in range(1,4):
            out.append(-sum((x[j]*out[k-j] for j in range(1,k+1)),x[0]*0)/x[0])
        return out
    inv_g,inv_a = reciprocal(gamma),reciprocal(radius)
    out = multiply(multiply(beta,multiply(inv_g,inv_g)),multiply(inv_a,inv_a))
    return [value/2 for value in out]


def metric_T_taylor(c, module, row, left, right, read_ball):
    """Same complete midpoint/whole-third Taylor recipe, for the NEW T scalar."""
    old_l,old_r = map(Fraction,row["interval"])
    left,right = Fraction(left),Fraction(right)
    require(old_l <= left < right <= old_r, "same complete original scalar interval")
    midpoint = metric_T_jets(row["intrinsic_midpoint_jets"],read_ball)
    whole = metric_T_jets(row["intrinsic_whole_third_jets"],read_ball)
    values = midpoint[:3]+[whole[3]]
    centre,half = (old_l+old_r)/2,(old_r-old_l)/2
    points,error = [],c.arb(0)
    for k,value in enumerate(values):
        dyadic = float(value.mid())
        require(c.np.isfinite(dyadic), "finite explicit new scalar Taylor coefficient")
        difference = value-c.arb(dyadic)
        error += max(abs(difference.lower()),abs(difference.upper()))*c.exact(half)**k
        points.append(c.Box(dyadic))
    cs = c.affine_polynomial(points,(left+right)/2-centre,(right-left)/2)
    return module.BatchRadialFourier.scalar(c,cs,c.arb_box(error.upper()).hi)


def control_fields(c,module,left,right):
    """Exact whole bump and exact radial derivative on its original support."""
    left,right = Fraction(left),Fraction(right)
    field = module.BatchRadialFourier
    require(left < right and (right <= A or left >= A) and right <= B,
            "the true compact seam is in the certification cover")
    if right <= A:
        return field.scalar(c,[0.]),field.scalar(c,[0.])
    require(A <= left < right <= B, "whole actual metric support")
    coefficients = [0]*13
    for j in range(7):
        coefficients[6+j] = 4096*(-1)**j*comb(6,j)
    centre,half = (left+right)/2,(right-left)/2
    cs = c.affine_polynomial([c.Box(x) for x in coefficients],
                            (centre-A)/(B-A),half/(B-A))
    w = field.scalar(c,cs)
    return w,w.radial_derivative(c.exact(1/half))


def true_centre_nu_source(c,module,background,scalar,row,left,right,read_ball):
    """NP.8, both ordinary rows and the full source mean, with no PDE substitution."""
    left,right = Fraction(left),Fraction(right)
    w,wp = control_fields(c,module,left,right)
    if right <= A:
        zero = module.BatchRadialFourier.scalar(c,[0.])
        return zero,zero
    u,v = background
    beta,K,gamma = (scalar[name] for name in ("beta","K","gamma"))
    T = metric_T_taylor(c,module,row,left,right,read_ball)
    up,vp,m = u.derivative(),v.derivative(),v.mean()
    vv = v*v
    P = vv.primitive()
    W1,W2 = P*up+vv*u,P*vp+vv*v
    a1,a2 = -beta*T*W1+gamma*m*T*vp,-beta*T*W2
    b1,b2 = (beta*K*W1-gamma*m*K*vp*Fraction(1,2),
              beta*K*W2-gamma*m*up*Fraction(1,2))
    pair = wp*a1+w*b1,wp*a2+w*b2
    require(max(p.degree for p in pair) <= 96, "the complete centre parameter-source support")
    return pair


def certify_cell(c,module,base,offsets,row,item,nodes,jets,read_ball):
    left,right = map(Fraction,item["interval"])
    scalar = {name:module.scalar_taylor(c,row["intrinsic_midpoint_jets"],
                row["intrinsic_whole_third_jets"],name,*row["interval"],left,right,read_ball)
              for name in ("beta","K","gamma","s")}
    background = base_background(c,module,base,offsets,item["background_piece"],left,right,scalar["s"])
    operator = module.prepare_operator(background,scalar)
    i = item["trial_piece"]
    values_l = [c.Box(jets[k][i,:,None]) for k in range(4)]
    values_r = [c.Box(jets[k][i+1,:,None]) for k in range(4)]
    cs = module.hermite_coefficients(c,values_l,values_r,c.exact(nodes[i+1]-nodes[i]))
    cs = module.restrict_trial_coefficients(c,cs,c.exact(nodes[i]),
                c.exact(nodes[i+1]-nodes[i]),left,right)
    trial = module.reflection_polynomial(c,cs)
    derivative = tuple(p.radial_derivative(c.exact(2/(right-left))) for p in trial)
    ordinary = module.complete_residual(operator,trial,derivative)
    source = true_centre_nu_source(c,module,background,scalar,row,left,right,read_ball)
    residual = tuple(x-y for x,y in zip(ordinary,source))
    require(max(p.degree for p in residual) <= 160,
            "all M96 plus twice M32 residual modes are present")
    angular = tuple(p.derivative() for p in trial)
    result = {}
    for name,pair,windows in (
            ("residual_L1_Hminus1",residual,("Hminus1","Hminus1")),
            ("trial_L1_L2",trial,("L2","L2")),
            ("trial_angle_L1_L2",angular,("L2","L2"))):
        square = module.pair_cell_norm_squared(c,pair,right-left,windows,"all")
        result[name] = c.mul_upper(c.sqrt_upper(c.box(right-left)),c.sqrt_upper(square))
    return result


def selected_error(api,records,old):
    """NP.7, combining only formally saved complete new/old upper endpoints."""
    require(set(records) == {"residual_L1_Hminus1","trial_L1_L2","trial_angle_L1_L2"}
            and set(old) == {"C1","M0","M1","N_C"}, "all complete source summands")
    theta = api.arb(936826)/1000000
    changed = theta*(old["M1"]*records["trial_angle_L1_L2"]+old["M0"]*records["trial_L1_L2"])
    metric = theta*(api.arb(13)/100).sqrt()*old["N_C"]
    return (old["C1"]*(records["residual_L1_Hminus1"]+changed+metric)).upper()
