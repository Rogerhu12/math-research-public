"""Ordinary Taylor jets in the true lifted label for the signed incoming rays.

Each list holds derivatives divided by factorial, evaluated on a covering box.
Arithmetic uses the caller's outward-rounded scalar or vector interval backend.
No finite-frequency phase approximation is made here.
"""
from math import factorial


def multiply(left, right, order):
    if order < 0 or min(len(left), len(right)) <= order:
        raise ValueError("missing product derivative")
    return [sum(left[i] * right[k-i] for i in range(k+1))
            for k in range(order+1)]


def compose(outer_at_base, inner):
    """Evaluate an angular jet at H; outer coefficients are based at H[0]."""
    order = len(inner)-1
    if order < 0 or len(outer_at_base) <= order:
        raise ValueError("missing composition derivative")
    delta = [0, *inner[1:]]
    acc = [outer_at_base[order]]
    for k in range(order-1, -1, -1):
        n = order-k
        acc = [outer_at_base[k]] + [
            sum(acc[j-i]*delta[i] for i in range(1,j+1))
            for j in range(1,n+1)]
    return acc


def inverse_jet(forward_at_label, label, derivative_positive):
    """Revert a noncritical lifted map at its actual inverse image interval."""
    if len(forward_at_label) < 2 or not derivative_positive(forward_at_label[1]):
        raise ValueError("the full forward derivative must have a positive lower bound")
    result = [label, 1/forward_at_label[1]]
    for k in range(2,len(forward_at_label)):
        # Coefficient k is forward'[0]*inverse[k] plus this lower-order sum.
        lower = compose(forward_at_label[:k+1], result+[0])[k]
        result.append(-lower/forward_at_label[1])
    return result


def ray_rhs(d_angular_derivatives, h_label, eta_q, sign):
    if sign not in (-1,1) or len(d_angular_derivatives) != len(h_label):
        raise ValueError("an entire signed speed jet is required")
    speed = [value / factorial(k) for k,value in enumerate(d_angular_derivatives)]
    speed[0] = speed[0] + sign*eta_q
    return compose(speed,h_label)


def quadrature_rhs(forcing_at_physical_angle, h_label):
    """Input is the signed WUA.16 ratio RHS, differentiated in physical angle."""
    return compose([v/factorial(k) for k,v in enumerate(forcing_at_physical_angle)],
                   h_label[:len(forcing_at_physical_angle)])


def flow_step(initial, step, midpoint_rhs, whole_rhs_radial2):
    """Third-order local enclosure from true midpoint velocity and its second derivative.

    The last slot encloses the TOTAL second inward derivative of the velocity
    along the characteristic on the entire step, component by component.
    Midpoint quadrature has error h^3/24 times the latter interval.
    """
    if not (len(initial)==len(midpoint_rhs)==len(whole_rhs_radial2)):
        raise ValueError("incomplete midpoint enclosure")
    return [x+step*v+(step**3/24)*w for x,v,w in zip(initial,midpoint_rhs,whole_rhs_radial2)]


def velocity_second_total(speed, speed_rho, speed_rho2, h_label):
    """Compute (d/d rho)^2 b(rho,H) for H'=b, with all label derivatives.

    Inputs are divided angular derivatives of b and its fixed-angle inward
    derivatives. Orders m+2,m+1,m respectively suffice for an m-jet.
    The zeroth slot of speed already includes the signed scalar speed.
    """
    m = len(h_label)-1
    if m < 0 or len(speed)<m+3 or len(speed_rho)<m+2 or len(speed_rho2)<m+1:
        raise ValueError("incomplete mixed speed derivatives")
    ang = [(k+1)*speed[k+1] for k in range(m+1)]
    ang2 = [(k+1)*(k+2)*speed[k+2] for k in range(m+1)]
    mixed = [(k+1)*speed_rho[k+1] for k in range(m+1)]
    speed2 = multiply(speed,speed,m)
    terms = (multiply(speed,mixed,m), multiply(speed2,ang2,m),
             multiply(ang,speed_rho,m), multiply(speed,multiply(ang,ang,m),m))
    total = [speed_rho2[k]+2*terms[0][k]+sum(term[k] for term in terms[1:])
             for k in range(m+1)]
    return compose(total,h_label)
