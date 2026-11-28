"""Actual one-sided coefficients for the first-order true ray-ratio source.

Only the integral physical slope of the nominal centre and the first radial
derivative of the actual repaired direction are used. The latter follows
from the known cubic and its complete per-coordinate value bound on each
maximal qualified original piece. No RCS target or old direction solve.
"""
from fractions import Fraction
from flint import arb
from fourfold_codazzi_signed_density_transport_arithmetic import exact,hull,LP,ball
from fourfold_codazzi_true_phase_original_inputs import DELTA,CONTROL,check
from fourfold_codazzi_true_phase_signed_speed import restricted,symmetric,coordinate_polys


def make_direction(direction):
    # Signatures include the physical delta multiplier, also for the mean.
    values=[symmetric(exact(DELTA)*abs(ball(z)).upper())
            for z in direction["complete_negative_interval_direction_coefficient_suprema"]]
    return (*coordinate_polys(values),tuple(map(Fraction,direction["exact_phase_interval"])))


def first_raw(inp,original,cell,left=None,right=None):
    l,r,k,i=cell
    l=l if left is None else Fraction(left)
    r=r if right is None else Fraction(right)
    check(cell[0]<=l<=r<=cell[1],"one-sided subcell within its original physical piece")
    centre,models=inp.rows[i]
    xr=hull(l-centre,r-centre);xc=hull(l-inp.nodes[k],r-inp.nodes[k])
    co=inp.piece(k);zu,zv,range_z=original
    width=min(inp.nodes[k+1],range_z[1])-max(inp.nodes[k],range_z[0])
    check(width>0,"maximal known same-cubic direction interval")
    # Sharp degree-three Markov constant. The proof uses the four original
    # polynomial values at the affine Chebyshev extrema, not radial samples.
    markov=exact(Fraction(18)/width)
    def cubic(s):
        v=((co[3][s]*xc+co[2][s])*xc+co[1][s])*xc+co[0][s]
        dr=(co[3][s]*3*xc+co[2][s]*2)*xc+co[1][s]
        return v,dr
    u,ur=cubic(0);v,vr=cubic(1)
    u=u+inp.du;v=v+inp.dv+restricted(models["s"],xr,0)
    ur=ur+zu*markov;vr=vr+zv*markov+restricted(models["s"],xr,1)
    beta,betar=[restricted(models["beta"],xr,j) for j in (0,1)]
    gamma,gr=[restricted(models["gamma"],xr,j) for j in (0,1)]
    q,qr=[restricted(models["q"],xr,j) for j in (0,1)]
    K=-q*q;Kr=-2*q*qr
    a,b=CONTROL
    # Determine active one-sided formulas from the parent piece, even when
    # the requested evaluation is its single endpoint.
    if cell[0]>=a and cell[1]<=b:
        t=hull((l-a)/(b-a),(r-a)/(b-a));v0=t*(1-t);v1=1-2*t
        w=4096*v0**6
        wp=exact(Fraction(24576)/(b-a))*v0**5*v1
        wpp=exact(Fraction(24576)/(b-a)**2)*v0**4*(5*v1*v1-2*v0)
        delta=arb(0,exact(DELTA))
        tm,tmr=[restricted(models["T"],xr,j) for j in (0,1)]
        fac=(-delta*w).exp();gfac=(delta*w/2).exp()
        rawK=K+delta*tm*wp
        Kr=fac*(Kr+delta*(tmr*wp+tm*wpp)-delta*wp*rawK)
        K=fac*rawK
        gr=gfac*(gr+gamma*delta*wp/2);gamma=gamma*gfac
    check(K.upper()<0,"actual negative curvature on the entire strict cell")
    qd=(-K).sqrt()
    mean=v.mean();eta=-gamma*mean;etar=-gr*mean-gamma*vr.mean()
    check(eta.lower()>0,"same physical mean and positive true eta")
    S=u*u+v*v*K
    d=S.primitive()*(-beta)
    ell=u*v*(-2*beta);ellr=u*v*(-2*betar)+(ur*v+u*vr)*(-2*beta)
    e=(1+u*u*3+v*v*K)*(-beta)
    bloc=(1-u*u-v*v*(3*K))*beta
    br=(1-u*u-v*v*(3*K))*betar+(-2*u*ur-v*v*(3*Kr)-v*vr*(6*K))*beta
    dphi=d.d()
    tq=dphi+e+etar/eta
    Rq=ellr-d*ell.d()+e.d()*eta-u.d()*u*(2*beta*eta)-ell*(dphi+etar/eta)
    v0=tq*bloc-br+d*bloc.d()-(ell*ell-v*u.d()*(4*beta*eta))*K
    theta=Rq/eta-v*v.d()*(2*beta*K)
    bval=eta*qd
    brho=-etar*qd+eta*Kr/(2*qd)
    return {"d":d,"K":K,"K_r":Kr,"beta":beta,"beta_mean_S":beta*S.mean(),
            "eta":eta,"eta_r":etar,"b":bval,"b_rho":brho,
            "T0":tq+bloc,"V0":v0,"theta":theta}
