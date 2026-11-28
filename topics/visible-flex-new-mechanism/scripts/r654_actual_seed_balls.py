"""Use the four paid continuous moving-end balls; enclose only changed C3 collars."""
from fractions import Fraction as F
from flint import acb,arb,ctx,fmpq
import r651_four_end_rest_time_search as source
from r654_released_rest_physical_base import PhysicalBase


def fr(x):
    v=F(x)
    return fmpq(v.numerator,v.denominator)


def physical_leg_rates(t,leg,z,zt):
    kind,h0,h1,k0,k1,eta0,T=leg
    if kind=="height":
        h,k,eta=h0+(h1-h0)*z,k0,eta0
        ht,kt=(h1-h0)*zt,0
    else:
        h,k=h0,k0+(k1-k0)*z
        eta=eta0+(k-k0)/(2*h)
        ht,kt=0,(k1-k0)*zt
    d=h*eta-k
    u=ht/(h*T)
    v=(ht*eta-kt/2)/T
    q=1+d*d
    return [T*(k*k-1-u*u),T*(-k*d),T*(eta*d*(k*d-1)/h-v*v/h**2),
            T*(q*(k*k+2*k*d-1)+u*u*q-2*u*d*v)/h**2]


def smooth_actual_seed(paid,epsilon,clock,counts,progress):
    ctx.prec=128
    ball_result=paid["ball_result"]
    raw=ball_result["parameters_exact"]
    p={k:([F(w) for w in v] if k in ("durations","levels") else
          (v if k=="order" else F(v))) for k,v in raw.items() if k!="excursion"}
    if "excursion" in raw:
        p["excursion"]={k:(v if k=="level" else F(v)) for k,v in raw["excursion"].items()}
    base=PhysicalBase(raw,epsilon)
    moving,_,columns=source.pieces(p)
    inverse=source.exact_inverse(columns)
    b=[]
    for text in ball_result["four_original_moving_ends"]:
        middle,radius=text.strip("[] ").split("+/-")
        b.append(acb(arb(fr(middle.strip()))+arb(0,1)*arb(fr(radius.strip()))))
    eps=acb(fr(epsilon))
    report={"epsilon":str(epsilon),"state":"pending","source_b_enclosures_reused":True,
            "changed_collar_integrals":[]}
    progress.append(report)
    for i,leg in enumerate(moving):
        bleg=(leg[0],*(acb(fr(v)) for v in leg[1:]))
        for side in (("right",) if leg[0]=="center" else ("left","right")):
            for j in range(4):
                clock.check("before_R654_changed_collar_ball")
                def delta(u,analytic):
                    counts["changed_collar_ball_callbacks"]+=1
                    x=eps*u if side=="left" else 1-eps+eps*u
                    v=u if side=="left" else 1-u
                    chi=v**4*(35+v*(-84+v*(70-20*v)))
                    chip=140*v**3*(1-v)**3
                    if leg[0]=="center":
                        z=x*(1+x*x*(4+x*(-7+3*x)))
                        zt=(1-x)**2*(15*x*x+2*x+1)
                    else:
                        z=x**3*(10+x*(-15+6*x))
                        zt=30*x*x*(1-x)**2
                    if side=="left":
                        smooth,slope=z*chi,zt*chi+z*chip/eps
                    else:
                        smooth,slope=1+(z-1)*chi,zt*chi-(z-1)*chip/eps
                    after=physical_leg_rates(x,bleg,smooth,slope)[j]
                    before=physical_leg_rates(x,bleg,z,zt)[j]
                    return eps*(after-before)
                value=acb.integral(delta,0,1,abs_tol=1.e-24,rel_tol=1.e-22,eval_limit=16000,depth_limit=80)
                counts["changed_collar_completed_integrals"]+=1
                report["changed_collar_integrals"].append({"leg":i,"side":side,"row":j,
                                                          "delta":value.str(28)})
                if not value.is_finite() or not value.imag.contains(0):
                    return None
                b[j]+=value
    times=[-sum((acb(fr(x))*v for x,v in zip(row,b)),acb(0)).real for row in inverse]
    length=arb(fr(source.length_of_motion(p)))+sum(times,arb(0))
    # Only stationary pieces have a variable duration at q=0. Their two
    # speeds are identically zero however small the positive dwell is.
    bound_hs=max((p.h_speed_numerator/p.duration for p in base.pieces if p.control is None),default=F(0))
    bound_ks=max((p.k_speed_numerator/p.duration for p in base.pieces if p.control is None),default=F(0))
    strict=bool(all(v.lower().fmpq()>0 for v in times) and length.lower().fmpq()>fmpq(21,10)
        and length.upper().fmpq()<fmpq(79,10) and F(4,5)<base.h_min<=base.h_max<3
        and -2<base.k_min<=base.k_max<2 and -1<base.eta_min<=base.eta_max<1 and max(bound_hs,bound_ks)<6)
    report.update(state="certified_continuous_smoothed_four_end_input" if strict else "unclosed",
        four_smoothed_b_balls=[v.real.str(28) for v in b],four_dwell_balls=[v.str(28) for v in times],
        length_ball=length.str(28),physical_h_speed_upper=str(bound_hs),physical_k_speed_upper=str(bound_ks),
        all_physical_fields_and_positive_durations_certified=strict)
    if strict:
        return [float(F(str((v.lower().fmpq()+v.upper().fmpq())/2))) for v in times]
    return None
