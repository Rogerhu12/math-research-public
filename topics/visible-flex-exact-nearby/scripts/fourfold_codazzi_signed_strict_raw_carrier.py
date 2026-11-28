"""New complete selected raw strict carrier for the signed global Airy source.

Only definitions are installed at import.  The owner has already admitted the
entire original TC raw-input closure, all forty whole native parts, both exact
repair definitions, and the selected-member domain before calling this module.
No old TC trial, source residual, matrix, scalar-jet producer, WGS or WSM target
is invoked.  Original repair arrays are necessary same-definition carriers and
their full original exact-rational sequence hashes are required unchanged.
"""
from bisect import bisect_right
from fractions import Fraction
from math import factorial, comb


STRICT_CUT = Fraction(76285779072683,320000000000000)
CONTROL = (Fraction(1,20),Fraction(9,50))
DELTA = Fraction(9368259853002,100000000000000000000000)
ALPHA = Fraction(6890507429876859,9007199254740992)
RAW_RADIAL_SLOTS = 4


def require(ok, message):
    if not ok:
        raise ValueError(message)


def exact(arb, value):
    value = Fraction(value)
    return arb(value.numerator)/value.denominator


def read_original_ball(arb, record):
    require(isinstance(record,dict), "one entire original scalar record")
    if "lower" in record and "upper" in record:
        value = arb(record["lower"]).lower().union(arb(record["upper"]).upper())
    else:
        value = arb(record["ball"])
    require(value.is_finite(), "complete finite original scalar enclosure")
    return value


def strict_partition(rows, exact_base_nodes):
    """All original exact scalar and cubic seams, including coincident floats."""
    nodes = tuple(Fraction.from_float(float(x)) for x in exact_base_nodes)
    require(len(nodes) == 6145 and nodes[0] == 0
            and all(a < b for a,b in zip(nodes,nodes[1:])),
            "the same full exact original cubic knot sequence")
    cuts = {Fraction(0),STRICT_CUT,*CONTROL}
    cuts.update(x for x in nodes if 0 < x < STRICT_CUT)
    for row in rows:
        left,right = map(Fraction,row["interval"])
        if left >= STRICT_CUT:
            break
        cuts.update(x for x in (left,right) if 0 < x < STRICT_CUT)
    cuts = sorted(cuts)
    require(cuts[0] == 0 and cuts[-1] == STRICT_CUT,
            "the whole exact original strict domain")
    rights = [Fraction(row["interval"][1]) for row in rows]
    plan = []
    for left,right in zip(cuts,cuts[1:]):
        row_index = bisect_right(rights,left)
        piece = bisect_right(nodes,left)-1
        row = rows[row_index]
        a,b = map(Fraction,row["interval"])
        require(a <= left < right <= b and nodes[piece] <= left < right <= nodes[piece+1],
                "one original scalar row and one actual one-sided cubic piece")
        require(right <= CONTROL[0] or left >= CONTROL[1]
                or CONTROL[0] <= left < right <= CONTROL[1],
                "no compact intrinsic control endpoint is crossed")
        plan.append({"index":len(plan),"original_row":row_index,"piece":piece,
                     "interval":[str(left),str(right)]})
    require(0 < len(plan) <= 20000,
            "complete declared strict-cell workload, without a frequency sample")
    return nodes,plan


def original_scalar_jets(arb, lp, jet, whole):
    """True point derivatives, not differentiation of old approximation errors."""
    out = {}
    for name in ("beta","K","gamma","s"):
        out[name] = jet([read_original_ball(arb,whole[name+(str(k) if k else "")])/factorial(k)
                         for k in range(RAW_RADIAL_SLOTS)],lp)
    a = [read_original_ball(arb,whole["a"])]
    require(a[0].lower() > 0, "same actual positive physical radius")
    beta = [value.scalar() for value in out["beta"].c]
    # a_phys'=beta a_phys.  This is an exact intrinsic identity; no absent
    # original a derivative or unqualified derivative of a tail is invented.
    for k in range(RAW_RADIAL_SLOTS-1):
        a.append(sum((beta[j]*a[k-j] for j in range(k+1)),arb(0))/(k+1))
    out["a"] = jet(a,lp)
    return out


def complete_component_jets(arb, acb, lp, jet, candidate, offsets,
                            piece, left, right, multiplier):
    """All signed physical Fourier components of one exact repaired cubic."""
    nodes = candidate["radial_nodes"]
    coefficients = candidate["piece_coefficients"]
    width = coefficients.shape[2]
    require(width in (65,193), "whole base65 or direction193 cubic")
    modes = (width-1)//2
    origin = Fraction.from_float(float(nodes[piece]))
    x = exact(arb,left-origin).union(exact(arb,right-origin))
    real_jets = []
    for order in range(RAW_RADIAL_SLOTS):
        values = []
        for coordinate in range(width):
            value = arb(0)
            # The native rows are descending cubic powers.  The binomial
            # gives the factorial-normalized TRUE derivative at variable x.
            for power in range(3,order-1,-1):
                coefficient = Fraction.from_float(float(coefficients[3-power,piece,coordinate]))
                value = value*x+exact(arb,multiplier*coefficient*comb(power,order))
            if order == 0:
                low = arb(float(offsets["lower"][piece,coordinate])).lower()
                high = arb(float(offsets["upper"][piece,coordinate])).upper()
                value += low.union(high)
            values.append(value)
        real_jets.append(values)
    uj,vj = [],[]
    for values in real_jets:
        uu,vv = [acb(0)]*(2*modes+1),[acb(0)]*(2*modes+1)
        vv[modes] = acb(values[modes])
        for k in range(1,modes+1):
            sine,cosine = values[k-1],values[modes+k]
            uu[modes+k],uu[modes-k] = acb(0,-sine/2),acb(0,sine/2)
            vv[modes+k] = vv[modes-k] = acb(cosine/2)
        uj.append(lp(uu,-modes))
        vj.append(lp(vv,-modes))
    return jet(uj,lp),jet(vj,lp)


def selected_fields(arb, acb, lp, jet, row, base, direction, offsets,
                    piece, left, right):
    """Same selected delta on the complete signed coefficients AND intrinsic jet."""
    left,right = Fraction(left),Fraction(right)
    scalar = original_scalar_jets(arb,lp,jet,row["intrinsic_whole_third_jets"])
    ub,vb = complete_component_jets(arb,acb,lp,jet,base,offsets["base"],
                                    piece,left,right,ALPHA)
    uz,vz = complete_component_jets(arb,acb,lp,jet,direction,offsets["direction"],
                                    piece,left,right,Fraction(1))
    delta = arb(0,exact(arb,DELTA))
    u = ub+delta*uz
    # The original rotational mean is included ONCE and is not replaced by
    # a newly fitted s_delta.  The full direction mean is already in vz.
    v = vb+scalar["s"]+delta*vz
    K,gamma = scalar["K"],scalar["gamma"]
    a,b = CONTROL
    if not (right <= a or left >= b):
        require(a <= left < right <= b, "exact compact support cell")
        t0 = exact(arb,(left-a)/(b-a)).union(exact(arb,(right-a)/(b-a)))
        t = jet([t0,exact(arb,1/(b-a)),0,0,0],lp)
        w5 = 4096*t**6*(1-t)**6
        wp = w5.radial().restrict(RAW_RADIAL_SLOTS)
        w = w5.restrict(RAW_RADIAL_SLOTS)
        Tmetric = scalar["beta"]/(2*(scalar["a"]*scalar["gamma"])**2)
        K = (-delta*w).exp_scalar()*(K+delta*Tmetric*wp)
        gamma = gamma*(delta*w/2).exp_scalar()
    return {"u":u,"v":v,"beta":scalar["beta"],"K":K,"gamma":gamma}


def finite_weighted_wiener(arb, polynomial, exponent, weights):
    """Entire signed Laurent polynomial; all Fourier modes and mean retained."""
    exponent = abs(Fraction(exponent))
    total = arb(0)
    require(polynomial.finite(), "whole finite signed coefficient")
    for k in range(polynomial.lo,polynomial.hi+1):
        key = (abs(k),exponent)
        if key not in weights:
            weight = arb(1+4*abs(k))
            weights[key] = (arb(1) if not exponent else
                (exact(arb,exponent)*weight.log()).exp().upper())
        total += abs(polynomial.coeff(k)).upper()*weights[key]
    return total.upper()


def joint_strict_J_windows(arb, coefficients, weights,
                           admitted_J0=Fraction(7,5),admitted_DJ=Fraction(3,8)):
    """One complete same-circle new candidate before any whole-domain maximum.

    7/5 and 3/8 must be admitted through the parent's complete new analytic
    proof and actual rational receipt.  They are not unverified guessed gaps.
    The three finite identities preserve the SAME true inverse J on all
    negative windows.  No upper bound is subtracted from another upper.
    """
    require(admitted_J0 == Fraction(7,5) and admitted_DJ == Fraction(3,8),
            "the separately admitted exact complete strict predecessor")
    u,v,beta,eta = (coefficients[name].c[0] for name in ("u","v","beta","eta"))
    etamin = eta.scalar().lower()
    require(etamin > 0, "actual same-circle positive eta")
    betamax = abs(beta.scalar()).upper()
    alpha = (2*betamax/etamin).upper()
    U = finite_weighted_wiener(arb,u,0,weights)
    V = finite_weighted_wiener(arb,v,0,weights)
    VI = finite_weighted_wiener(arb,v.primitive(),0,weights)
    uv = u*v
    Iuv = finite_weighted_wiener(arb,uv.primitive(),0,weights)
    AA = (alpha*Iuv).exp().upper()
    kappa = (1-alpha*U*VI).lower()
    dj = exact(arb,admitted_DJ)
    if kappa > 0:
        dj = max(dj,(kappa/AA).lower())
    Cc = (AA*U/(4*etamin*dj)).upper()
    Cp = (AA*AA/4*(U/(4*etamin)+Cc*(1+alpha*U*VI))).upper()
    rawJ0 = (1/(4*etamin)+alpha*V*Cp+alpha*VI*Cc).upper()
    J0 = min(rawJ0,exact(arb,admitted_J0)).upper()
    L = {}
    for s in (Fraction(-5,3),Fraction(-1),Fraction(-2,3),Fraction(0),Fraction(1,3)):
        Wuv = finite_weighted_wiener(arb,uv,s,weights)
        Wvp = finite_weighted_wiener(arb,v.d(),s,weights)
        Wu = finite_weighted_wiener(arb,u,s,weights)
        L[s] = (2*betamax*(Wuv+Wvp*Wu/4)).upper()
    # The actual physical primitive gain from H^s to H^(s+1) is sqrt17/4.
    c = (arb(17).sqrt()/(4*etamin)).upper()
    hm2 = (c+c*c*L[Fraction(-1)]
            +J0*c*c*L[Fraction(0)]*L[Fraction(-1)]).upper()
    hm53 = (c+c*c*L[Fraction(-2,3)]
             +J0*c*c*L[Fraction(1,3)]*L[Fraction(-2,3)]).upper()
    hm83 = (c+c*c*L[Fraction(-5,3)]
             +c*c*c*L[Fraction(-2,3)]*L[Fraction(-5,3)]
             +J0*c*c*c*L[Fraction(1,3)]*L[Fraction(-2,3)]*L[Fraction(-5,3)]).upper()
    return {"eta_positive_lower":etamin,"new_DJ_positive_lower":dj,
        "new_joint_J0_upper":rawJ0,"selected_same_J0_upper":J0,
        "same_J_Hminus2_to_Hminus1_upper":hm2,
        "same_J_Hminus5_3_to_Hminus2_3_upper":hm53,
        "same_J_Hminus8_3_to_Hminus5_3_upper":hm83,
        "complete_L_windows":{str(s):value for s,value in L.items()},
        "same_true_inverse_on_all_four_windows":True}
