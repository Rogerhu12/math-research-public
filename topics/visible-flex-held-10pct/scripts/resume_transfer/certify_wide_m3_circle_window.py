#!/usr/bin/env python3
"""New exact rational primary b=.32 circle and controlled-moment window.

This is a new physical core design, with no prefix/tail BVP and no claim
that a closed map exists. All geometry bounds below use Fraction interval
arithmetic, true cutoff integrals, and an explicit quadrature remainder.
The global closed-surface conclusions remain conditional as in R32.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import math
import sys
import time

HERE = Path(__file__).resolve().parent
CLOSED = HERE.parent/'resume_closed'
sys.path.insert(0, str(CLOSED))
import integral_core_intervals as ri
from fast_integral_core_intervals import HornerCutoffPrimitive
from certify_protected_arc_curvature_dual import decimal, show
from certify_m3_large_circle_window import sqrt_bounds

A, B = F(21, 100), F(8, 25)
Q, QLO, QHI = F(17, 200), F(849, 10000), F(851, 10000)
CONTROL = F(2, 25)
ORDER = 80


def moment(order):
    value = A**(order+1)/(order+1)
    for j in range(order+1):
        inner = sum((F(c, j+k+1) for k,c in enumerate(ri.CHI)), F(0))
        value += B*math.comb(order,j)*A**(order-j)*B**j*inner
    return value


def trig_moment(frequency, sine=False):
    parity = int(sine)
    value = sum((F((-1)**((j-parity)//2)*frequency**j, math.factorial(j))*moment(j)
                 for j in range(parity, ORDER+1, 2)), F(0))
    error = (A+B/2)*(frequency*(A+B))**(ORDER+1)/math.factorial(ORDER+1)
    return ri.outward(value-error, value+error)


def primary_constants():
    pi = ri.pi_interval(); L = ri.scale(pi, F(1,3)); root3 = sqrt_bounds(F(3))
    cm = {k:trig_moment(k) for k in (1,2,3,4)}
    sm = {k:trig_moment(k,True) for k in (1,2,4)}
    beta = ri.neg(ri.divide(ri.scale(ri.sub(ri.point(A+B/2),cm[3]),8),
                            ri.sub(L,ri.point(A+B/2))))
    g0 = ri.add(ri.divide(cm[1],root3),sm[1])
    g1 = ri.sub(ri.scale(g0,8),ri.scale(ri.add(ri.divide(ri.add(cm[2],cm[4]),root3),
                                              ri.sub(sm[4],sm[2])),4))
    center = ri.add(ri.sub(ri.sub(ri.point(9),beta),g1),ri.mul(beta,g0))
    assert beta[1] < 0 and center[0] > 9
    return pi,L,root3,beta,center


class PrimaryOnly(ri.ExactRawM3Core):
    """Same Green formula with independently certified new primary constants."""
    def __init__(self, q, L, beta, center):
        self.q, self.lam = q, F(1)
        self.L, self.T = L, ri.scale(L,2)
        self.beta, self.center_per_q = beta, center
        self.primary = HornerCutoffPrimitive(A,B,ri.plain_integrals)

    def control_jets(self,x,order=4):
        return [ri.point(0) for _ in range(order+1)]

    def control_primitive(self,x):
        return ri.point(0)


def signed_cubic_area_integrand(core, x):
    phi = ri.add(core.L,x)
    g = core._normal_jets_local(phi,x)
    px,py = g['position']; sn,cs = ri.neg(g['tangent'][0]),g['tangent'][1]
    real4 = ri.add(ri.sub(ri.power(px,4),ri.scale(ri.mul(ri.power(px,2),ri.power(py,2)),6)),
                   ri.power(py,4))
    imag4 = ri.scale(ri.mul(ri.mul(px,py),ri.sub(ri.power(px,2),ri.power(py,2))),4)
    return ri.scale(ri.mul(g['rho'],ri.add(ri.mul(real4,cs),ri.mul(imag4,sn))),F(1,8))


def calculate(panels):
    pi,L,root3,beta,center = primary_constants()
    green_ratio = ri.divide(L,root3)
    assert F(1,2) < green_ratio[0] <= green_ratio[1] < F(2,3)
    # Periodic Green kernel bounds. The positive primary correction mass is
    # -beta*T; the constant beta has zero derivative.
    delta_h_unit = ri.mul(ri.neg(beta),ri.sub(ri.point(1),ri.divide(L,root3)))[1]
    delta_hp_unit = -beta[0]*L[1]
    unit_position = F(3)+delta_h_unit+delta_hp_unit
    primary_radius = 1+QHI+QHI*delta_h_unit
    primary_support = 1-QHI-QHI*delta_h_unit
    rho_max = 1+8*QHI
    rho_min = 1-8*QHI+QHI*beta[0]
    rho_phi = QHI*(24+ri.cutoff_derivative_bound(1)/B*(16-beta[0]))
    # f=(rho/8) Re(z^4 exp(-i phi)); |z_phi|=rho.
    integrand_lipschitz = (rho_phi*primary_radius**4+4*rho_max**2*primary_radius**3
                           +rho_max*primary_radius**4)/8
    core = PrimaryOnly(Q,L,beta,center)
    values = ri.point(0)
    for j in range(panels):
        x = ri.scale(L,F(2*j+1,2*panels))
        values = ri.add(values,signed_cubic_area_integrand(core,x))
        if (j+1)%32==0:
            print(json.dumps(dict(event='true_moment_panels',completed=j+1,total=panels)),flush=True)
    midpoint = ri.mul(ri.scale(L,F(6,panels)),values)
    quadrature_error = F(3,2)*integrand_lipschitz*L[1]**2/panels
    nominal_moment = ri.add(midpoint,(-quadrature_error,quadrature_error))
    assert nominal_moment[0] > 0
    # Differentiate the exact boundary formula in q. Gamma=n+q*V and
    # rho=1+q*U, so the following bound holds on the whole amplitude interval.
    q_derivative = pi[1]/4*((8-beta[0])*primary_radius**4
                             +4*rho_max*primary_radius**3*unit_position)
    q_cost = max(Q-QLO,QHI-Q)*q_derivative
    primary_moment = ri.add(nominal_moment,(-q_cost,q_cost))
    control_support_constant = ri.sub(ri.divide(ri.point(2),root3),ri.point(1))[1]
    control_support = control_support_constant*CONTROL
    radius = primary_radius+control_support
    support = primary_support-control_support
    controlled_rho = rho_min-CONTROL
    # Support interpolation stays strictly convex and has perimeter 2*pi.
    # Its area-moment shape derivative is integral b*z^3*rho dphi.
    control_moment_cost = 2*pi[1]*radius**3*control_support
    controlled_moment = primary_moment[0]-control_moment_cost
    assert controlled_rho > F(2,25) and controlled_moment > F(1,50)
    alpha = F(3523,5000); ilo,ihi = F(3521,10000),F(141,400)
    rlo,rhi = 1+8*QLO,1+8*QHI
    assert ilo-alpha > -rlo*A and ihi < rlo*A
    protected_material_margin = rlo*A-max(ihi,alpha-ilo)
    assert protected_material_margin > 0
    sine = ri.signed_sincos(ri.point(alpha/(2*rhi)))[0]
    held = ri.mul(ri.mul(root3,ri.scale(center,QLO)),sine)
    assert held[0] > F(53,200)
    ell0,ell1 = F(27,50),F(5401,10000)
    core_diameter = ri.scale(sqrt_bounds(radius**2+(ell1/2)**2),2)
    assert core_diameter[1] < F(233,100)
    active_moment = (ell1-ell0)*controlled_moment/2
    assert active_moment > F(1,10**6)
    rc = F(1,40)
    marker_height = ri.divide(ri.point(8*rc**3),ri.scale(root3,81))
    final_diameter = ri.add(ri.point(F(13249,5000)+ell1-ell0),ri.scale(marker_height,2))
    assert final_diameter[1] < F(53,20)
    dec = lambda x: decimal(x,True)
    return dict(scope=__doc__, primary_definition=dict(base_mode=3,eta='0',homotopy='1',
        protected_halfwidth=str(A),primary_transition=str(B),q_nominal=str(Q),q_interval=[str(QLO),str(QHI)],
        beta=show(beta),circle_center_per_q=show(center)),
        true_zero_control_core=dict(rho_lower=decimal(rho_min),rho_upper=dec(rho_max),
            rho_phi_upper=dec(rho_phi),support_lower=decimal(primary_support),radius_upper=dec(primary_radius),
            unit_position_upper=dec(unit_position)),
        true_primary_cubic_area_moment=dict(convention='Integral over the planar enclosed domain of (X+iY)^3 dA; standard global axes',
            half_sector_panels=panels,finite_midpoint_sum=show(midpoint),
            integrand_lipschitz_upper=dec(integrand_lipschitz),midpoint_remainder_upper=dec(quadrature_error),
            nominal_moment=show(nominal_moment),q_derivative_upper=dec(q_derivative),
            amplitude_interval_cost_upper=dec(q_cost),uniform_primary_moment=show(primary_moment)),
        whole_control_conditions=dict(regularity='C4',period='2*pi/3',zero_mean=True,
            even_about_phi_zero=True,
            support_identically_zero_on_closed_arc_abs_phi_minus_pi_over_3_le_a=True,
            material_H_and_phase_sweep_have_protected_open_neighborhood=True,
            protected_material_margin_lower=str(protected_material_margin),rho_norm_upper=str(CONTROL),
            support_norm_upper=dec(control_support),rho_lower=decimal(controlled_rho),
            support_lower=decimal(support),radius_upper=dec(radius),
            shape_derivative_moment_cost_upper=dec(control_moment_cost),
            absolute_cubic_area_moment_lower=decimal(controlled_moment)),
        conditional_closed_window=dict(phase=str(alpha),fixed_material_H_interval=[str(ilo),str(ihi)],
            cylinder_lengths=[str(ell0),str(ell1)],core_cylinder_diameter_upper=show(core_diameter),
            uniform_whole_image_Hausdorff_lower=show(held),held_ratio_if_D_le_265=show(ri.scale(held,F(20,53))),
            H_diameter_ratio_lower=str(F(54,265)),selected_active_moment_abs_lower=decimal(active_moment),
            unmarked_D_upper='2.6498',unmarked_support_lower='.0801',unmarked_curvature_upper='12.5',
            plane_cap_height_lower='1',plane_cap_open_radius_greater_than='1/40',
            final_D_upper=show(final_diameter),reach_lower='.08',reach_ratio_lower=str(F(8,265)),
            exact_marker_cubic_moment=show(ri.scale(pi,rc**8/140)),
            remaining_hypotheses='Same material-phase/C3/mirror/C2 seam hypotheses and full-surface bounds as R32; actual map, original tail and fixed-g refinement remain unpaid.'),
        arithmetic=dict(exact_rational_inputs=True,moment_taylor_degree=ORDER,
            local_integral_taylor_degree=ri.SERIES_DEGREE,interval_decimal_digits=80,
            no_sampled_extremum_or_unbounded_quadrature_used=True))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--panels',type=int,default=128)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.panels<8:raise ValueError('At least eight complete panels required')
    start=time.monotonic();result=calculate(args.panels)
    sources=[Path(__file__),CLOSED/'integral_core_intervals.py',CLOSED/'fast_integral_core_intervals.py',
             CLOSED/'certify_protected_arc_curvature_dual.py',CLOSED/'certify_m3_large_circle_window.py',
             CLOSED.parent/'resume_n4/audit_large_radius_core.py']
    result.update(command=sys.argv,sources_sha256={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest()for p in sources},seconds=time.monotonic()-start)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ('primary_definition','whole_control_conditions','conditional_closed_window','seconds')},ensure_ascii=False),flush=True)


if __name__=='__main__':main()
