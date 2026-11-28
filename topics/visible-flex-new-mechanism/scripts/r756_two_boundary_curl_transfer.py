"""R756 conditional continuum transfer for the two prescribed physical boundaries of R750."""
from r726_closed_spinor_fourier import public
from r734_true_dyadic_tail import I, monotone_trans
from r749_two_cap_volterra_bound import ZERO, ONE, absmax, high, interval, maximum, minimum, nn, root
import re


def lo(x):
    return I(x.lo)


def diameter_width(edges):
    return [high(b-a) for a,b in zip(edges,edges[1:])]


def ordered_edges(values):
    r=[interval(v) for v in values]
    if len(r)<2 or any(b.lo<=a.hi for a,b in zip(r,r[1:])):
        raise ValueError("every material cell needs strictly ordered edges")
    return r


def scale_columns(c):
    rr,rs,ss=(interval(c[k]) for k in ("g_rr","g_rs","g_ss"))
    if min(rr.lo,ss.lo)<=0:
        raise ValueError("the fixed physical metric must be positive")
    det=(lo(rr)*lo(ss)-absmax(rs)**2).lo
    if "det_g_lower" in c:
        det=max(det,interval(c["det_g_lower"]).lo)
    if det<=0 or det>(high(rr)*high(ss)).hi:
        raise ValueError("the fixed nonorthogonal metric needs a true positive determinant lower bound")
    a=monotone_trans(lo(rr),"sqrt")
    d=monotone_trans(I(det),"sqrt")
    # J is the upper triangular change from orthonormal columns to material components.
    return high(ONE/a),high(absmax(rs)/(a*d)),high(root(rr)/d)


def hessian_norm(upper,col):
    a,b,d=col
    rr,rs,ss=upper
    h11=a*a*rr
    h12=a*(b*rr+d*rs)
    h22=b*b*rr+2*b*d*rs+d*d*ss
    return maximum(h11+h12,h22+h12)


def prove_cell(c,delta,dprime,hout,hin,ksout,ksin):
    chi=interval(c["chi"])
    if chi.lo<0 or chi.hi>1:
        raise ValueError("the radial blend must remain within [0,1]")
    ch,cc=high(chi),high(ONE-chi)
    wp,wpp=nn(c["chi_r_abs"]),nn(c["chi_rr_abs"])
    extra=list(map(nn,c["implementation_six_abs"]))
    if len(extra)!=6:
        raise ValueError("all six representative errors are required")
    p,ar,az,arr,arz,azz=extra
    def blend(o,i):
        return maximum((ONE-lo(chi))*o+lo(chi)*i,(ONE-ch)*o+ch*i)
    f=[high(ch*delta+p),high(wp*delta+ar),high(blend(hout,hin)+az),
       high(wpp*delta+arr),high(wp*dprime+arz),high(blend(ksout,ksin)+azz)]
    col=scale_columns(c)
    j1,j2,j3=col
    eu=j1*f[1]
    ev=j2*f[1]+j3*f[2]
    e=root(eu**2+ev**2)
    eta=high(2*e+e**2)
    cross=high(eu+ev+eu*ev)
    nerr=minimum(I(2),2*cross)
    row=dict(six_to_outer_and_beta=[str(x.hi) for x in f],position_to_inner=str((cc*delta+p).hi),
             differential_relative_operator=str(e.hi),relative_Gram_operator=str(eta.hi),
             reference_normal_requires_oriented_same_metric_coframe=True)
    if e.hi>=1:
        row.update(immersion_from_this_bound=False)
        return row
    axes={}
    for name,value in c.get("beta_normal_axis_lower",{}).items():
        axis=interval(value)
        if axis.lo < -1 or axis.hi>1:
            raise ValueError("unit axis projection must be a cosine")
        estimate=max(-1,(lo(axis)-nerr).lo)
        projected=lo(axis)-cross
        if projected.lo>0:
            estimate=max(estimate,(projected/(1+e)**2).lo)
        axes[name]=str(estimate)
    gammas=c["Gamma_abs_rr_rs_ss"]
    if len(gammas)!=3 or any(len(v)!=2 for v in gammas):
        raise ValueError("all six true source Christoffel upper bounds are required")
    hh=[high(f[3+i]+nn(g[0])*f[1]+nn(g[1])*f[2]) for i,g in enumerate(gammas)]
    h=hessian_norm(hh,col)
    t=nn(c["covariant_beta_vector_quadratic_upper"])
    k=nn(c["covariant_beta_normal_operator_upper"])
    curvature=high((k+h+nerr*t)/(1-e)**2)
    return dict(**row,immersion_from_this_bound=True,actual_normal_axis_lower=axes,oriented_normal_error=str(nerr.hi),
                covariant_twojet_relative_error=str(h.hi),principal_curvature_upper=str(curvature.hi))


def rim(c,which):
    expected=1 if which=="inner" else 0
    clamp=list(map(interval,c["true_chi_012"]))
    if len(clamp)!=3 or any(x.lo!=v or x.hi!=v for x,v in zip(clamp,(expected,0,0))):
        raise ValueError("a prescribed edge must have its true clamped cutoff jets")
    impl=list(map(nn,c["implementation_six_abs"]))
    if len(impl)!=6:
        raise ValueError("six implementation errors required at each physical edge")
    ref=[ZERO,nn(c["beta_r_minus_P_r"]),ZERO,nn(c["d_r_beta_r_minus_P_rr"]),
         nn(c["d_s_beta_r_minus_P_rs"]),ZERO]
    return [high(x+y) for x,y in zip(ref,impl)]


def two_boundary_transfer(radial_edges,angular_edges,strips,proof_sha256):
    """Each angular strip supplies both ray errors, the actual two edge data and a radial cell cover.

    Unnormalized coordinates follow the original regular R750 annulus: r rises from
    the inside anchor to 1, s is periodic with period 1. Raw K is det times Cartesian curl.
    The two K suprema supplied below are material-coordinate K and its full s derivative.
    Results hold only for the stated continuum evidence and representative.
    """
    public()
    if not isinstance(proof_sha256,str) or not re.fullmatch("[a-f0-9]{64}",proof_sha256):
        raise ValueError("identify the strict original material evidence")
    r=ordered_edges(radial_edges)
    s=ordered_edges(angular_edges)
    if r[0].lo<=0 or r[-1].lo!=1 or r[-1].hi!=1 or (s[0].lo,s[0].hi,s[-1].lo,s[-1].hi)!=(0,0,1,1):
        raise ValueError("the full regular R750 annulus and original whole circumference are required")
    if len(strips)+1!=len(s):
        raise ValueError("missing angular strip")
    dr,ds=diameter_width(r),diameter_width(s)
    reports=[]
    for j,strip in enumerate(strips):
        cells=strip["cells"]
        if len(cells)!=len(dr):
            raise ValueError("missing radial strip cells")
        mass=[];smass=[]
        for c,width in zip(cells,dr):
            mass.append(high(width*nn(c["K_material_abs"])))
            smass.append(high(width*nn(c["d_s_K_material_abs"])))
        caps=[strip[k] for k in ("inner","outer")]
        bi,bo=(nn(cap["P_s_minus_beta_s"]) for cap in caps)
        bis,bos=(nn(cap["P_ss_minus_d_s_beta_s"]) for cap in caps)
        dprime=high(bi+bo+sum(mass,ZERO))
        left,right=(nn(strip[k]) for k in ("left_ray_abs","right_ray_abs"))
        growth=high(ds[j]*dprime)
        delta=minimum(left+growth,right+growth,maximum(left,right)+growth/2)
        if "all_ray_abs" in strip:
            delta=minimum(delta,nn(strip["all_ray_abs"]))
        prefix=[ZERO];sprefix=[ZERO];suffix=[ZERO]*(len(cells)+1);ssuffix=suffix.copy()
        for i in range(len(cells)):
            prefix.append(high(prefix[-1]+mass[i]))
            sprefix.append(high(sprefix[-1]+smass[i]))
        for i in reversed(range(len(cells))):
            suffix[i]=high(suffix[i+1]+mass[i])
            ssuffix[i]=high(ssuffix[i+1]+smass[i])
        checked=[prove_cell(c,delta,dprime,bo+suffix[i],bi+prefix[i+1],
                            bos+ssuffix[i],bis+sprefix[i+1]) for i,c in enumerate(cells)]
        edges=[rim(cap,k) for cap,k in zip(caps,("inner","outer"))]
        reports.append(dict(angular_strip=j,all_ray_upper=str(delta.hi),all_ray_derivative_upper=str(dprime.hi),
            two_physical_rim_six=[[str(x.hi) for x in z] for z in edges],
            exact_both_physical_rims=all(x.hi==0 for z in edges for x in z),cells=checked))
    return dict(conditional_on_continuous_proof=proof_sha256,angular_strips=len(strips),
                radial_cells_per_strip=len(dr),per_strip=reports,
                six_order=["P","r","s","rr","rs","ss"],raw_cartesian_curl_is_not_material_K=True,
                unknown_shell_pairs_and_time_still_require_separate_cover=True)


def ordered_far_pair(distance_lower,distance_upper,normal_dot_upper,position_errors,normal_error,radius):
    """One directed source–target pair box with independent approximate representatives."""
    public()
    lo_d=lo(interval(distance_lower));hi_d=nn(distance_upper);tau=nn(radius)
    if lo_d.lo<0 or hi_d.hi<lo_d.lo or tau.hi<=0 or len(position_errors)!=2:
        raise ValueError("two actual positions, true distance enclosure and positive radius required")
    drift=sum(map(nn,position_errors),ZERO)
    l=I(max(ZERO.lo,(lo_d-drift).lo))
    dot=nn(normal_dot_upper)+drift+nn(normal_error)*hi_d
    margin=lo(l*l-2*tau*dot)
    return dict(directed_normal_ball_proved=margin.lo>=0,distinct_points_separated=l.lo>0,
                signed_squared_margin_lower=str(margin.lo))


def geodesic_near_pair(curvature_upper,length_upper,radius):
    """Both directed balls for a distinct pair joined by a chart-covered ACTUAL unit-speed geodesic."""
    public()
    k,l,tau=nn(curvature_upper),nn(length_upper),nn(radius)
    if tau.lo<=0:
        raise ValueError("a positive desired radius is required")
    ok=(k*l).hi<=I("1.57079").lo and (k*tau).hi<=1
    return dict(both_normal_balls_if_actual_geodesic_covered=ok,
                requires_all_geodesic_points_and_geodesic_length_proof=True)
