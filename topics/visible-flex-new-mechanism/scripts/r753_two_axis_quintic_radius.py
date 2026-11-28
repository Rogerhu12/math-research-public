"""R753 optional local inverse certificate for the two true material axes, using existing quintic cap cells."""
import re
from r726_closed_spinor_fourier import public
from r734_true_dyadic_tail import I,monotone_trans
from r749_two_cap_volterra_bound import A0,B0,ZERO,ONE,absmax,high,interval,nn,root,maximum


def lower_sqrt(x):
    if x.lo<=0:
        return ZERO
    return I(monotone_trans(I(x.lo),"sqrt").lo)


def lower(x):
    return I(x.lo)


def intersection(a,b):
    lo=max(a.lo,b.lo)
    hi=min(a.hi,b.hi)
    if lo>hi:
        raise ValueError("incompatible certified enclosures")
    return I(lo,hi)


def joint_axis_certificate(edges,cells,cuts,axis_lengths,C_x,C_z,step_box,
                           normal_height_lower,proof_sha256):
    """Certify local existence for every target in one given pose enclosure.

    The input proof covers one entire original reflection-even material height,
    its fixed rigid boundary triples, a complete positive E and its two axis
    slopes. Each cell carries E, p_plus, p_minus, and gradient_norm_upper.
    """
    public()
    if not isinstance(proof_sha256,str) or not re.fullmatch("[0-9a-f]{64}",proof_sha256):
        raise ValueError("identify the external continuous material evidence")
    r=list(map(interval,edges))
    if (not cells or len(r)!=len(cells)+1 or
        (r[0].lo,r[0].hi)!=(A0.lo,A0.hi) or (r[-1].lo,r[-1].hi)!=(B0.lo,B0.hi) or
        any(b.lo<=a.hi for a,b in zip(r,r[1:]))):
        raise ValueError("a complete strictly ordered original interval cover is required")
    first,last=cuts
    if not isinstance(first,int) or not isinstance(last,int) or not 0<first<=last<len(cells):
        raise ValueError("select two nonoverlapping endpoint intervals at original spline knots")
    lengths=[r[first]-r[0],r[-1]-r[last]]
    ts=[interval(step_box[key]) for key in ("plus","minus")]
    if any(t.lo!=t.hi for t in ts):
        raise ValueError("each chosen correction radius must be an exact decimal")
    sigma=lower(interval(normal_height_lower))
    if not 0<sigma.lo<1 or min(t.lo for t in ts)<=0:
        raise ValueError("positive chart and a nonempty correction box required")
    ceiling=lower_sqrt(ONE-sigma**2)
    gradients=[];groups=[[],[]]
    for i,data in enumerate(cells):
        E=interval(data["E"])
        if E.lo<=0:
            raise ValueError("the real material E lower bound must be positive")
        e=lower_sqrt(E)
        side=0 if i<first else (1 if i>=last else None)
        hp=ZERO if side is None else I("1.875")/lengths[side]
        # The radial blending coefficients (1+cos phi)/2,(1-cos phi)/2
        # are nonnegative and sum to one. |h|<=1 everywhere.
        radial=maximum(*ts)*hp/e
        angle=(ts[0]+ts[1])/(2*I(r[i].lo))
        addition=root(radial**2+angle**2)
        original=nn(data["gradient_norm_upper"])
        gradients.append(high(original+addition))
        if side is not None:
            groups[side].append((E,[interval(data[k]) for k in ("p_plus","p_minus")],hp,original))
    maxgrad=maximum(*gradients)
    common=dict(conditional_on_continuous_proof=proof_sha256,C_x=interval(C_x).bounds(),
                C_z=interval(C_z).bounds(),full_box_gradient_upper=str(maxgrad.hi),
                actual_s_lower_requirement=str(sigma.lo),
                endpoint_field_is_required_at_its_declared_C_z=True,
                proves_body_metric_curvature_or_reach=False)
    if maxgrad.hi>ceiling.lo:
        return dict(**common,conditional_local_inverse=False,reason="full correction box positive-chart budget unresolved")

    phase_cos=monotone_trans(ONE-I(".27")**2,"sqrt")
    stride=B0-A0*phase_cos
    targets=[stride-interval(C_x),stride+interval(C_x)]
    results=[]
    for j,key in enumerate(("plus","minus")):
        gj=[];H=ZERO
        for side,group in enumerate(groups):
            ratios=[];amps=[]
            for E,pairs,hp,original in group:
                p=pairs[j]
                # A>=sqrt(E)s follows from the material graph inequality.
                original_A=intersection(
                    I((lower_sqrt(E)*lower_sqrt(ONE-original**2)).lo,root(E).hi),
                    I(lower_sqrt(E-I(p.norm())**2).lo,root(E).hi))
                ratios.append(p/original_A)
                held=I(p.norm())+ts[j]*hp
                min_A=I(max((sigma*lower_sqrt(E)).lo,lower_sqrt(E-held**2).lo))
                amps.append(high(E/min_A**3))
            gj.append(I(min(z.lo for z in ratios),max(z.hi for z in ratios)))
            H=high(H+(I(10)/7)*maximum(*amps)/lengths[side])
        # Each band's S' has mass one; the derivative at zero lies in this
        # interval even when p/A is not monotone within an endpoint cell.
        jac=gj[1]-gj[0] if j==0 else gj[0]-gj[1]
        L0=interval(axis_lengths[key])
        if L0.lo<=0:
            raise ValueError("invalid original projected axis length")
        target=targets[j]-L0
        row=dict(axis=key,desired_change=target.bounds(),derivative_at_zero=jac.bounds(),
                 absolute_second_derivative_upper=str(H.hi))
        if jac.lo<=0:
            results.append(dict(**row,conditional_axis_inverse=False,reason="endpoint slope separation unresolved"))
            continue
        # A positive interval radius must be rounded inwards.
        radius=I(min(ts[j].lo,(I(jac.lo)/(2*H)).lo))
        der=I((I(jac.lo)-H*radius).lo,(I(jac.hi)+H*radius).hi)
        if der.lo<=0 or absmax(target).hi>(radius*I(der.lo)).lo:
            results.append(dict(**row,conditional_axis_inverse=False,reason="target exceeds certified monotone range",
                                derivative_on_subbox=der.bounds(),subbox_radius=str(radius.lo)))
            continue
        enclosure=intersection(target/der,I(radius.lo.copy_negate(),radius.lo))
        results.append(dict(**row,conditional_axis_inverse=True,root_enclosure=enclosure.bounds(),
                            derivative_on_subbox=der.bounds(),subbox_radius=str(radius.lo)))
    return dict(**common,conditional_local_inverse=all(x["conditional_axis_inverse"] for x in results),axes=results)
