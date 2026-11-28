"""Rigorous whole-physical-circle transport errors for true phase and R.

Inputs are one-sided bounds on an entire original radial cell.  Each m slot
uses the actual physical angular derivative divided by m!, including m=0.
No differentiation of a scalar numerical remainder and no frequency cutoff
of the transported true solution are made.
"""
from math import comb


def _nonnegative_upper(values):
    result=[x.upper() for x in values]
    if any(not x.is_finite() or x < 0 for x in result):
        raise ValueError("an error majorant must be finite and nonnegative")
    return result


def propagate(h,one_sided_slope,speed_derivatives,initial,source):
    """Entire cell bound for (partial_t+(d+sigma*b)partial_phi) e = f.

    The slope input encloses max(0, sup(-d_phi)); all d_j, j>=2, enclose
    absolute normalized derivatives. The nilpotent lower triangular part
    ends exactly after at most m products. The scalar b may vary in t.
    """
    degree=len(initial)-1
    if degree<0 or len(source)!=degree+1 or len(speed_derivatives)<=degree:
        raise ValueError("missing qualified transport derivative")
    if not h.is_finite() or not h.lower()>=0:
        raise ValueError("finite inward step of nonnegative length")
    h=h.upper()
    slope=_nonnegative_upper([one_sided_slope])[0]
    initial,source=map(_nonnegative_upper,(initial,source))
    d=_nonnegative_upper(speed_derivatives)
    def lower(vector):
        return [sum((j*d[k-j+1]*vector[j] for j in range(1,k)),h*0).upper()
                for k in range(degree+1)]
    a=initial;v=source
    total=[(x+h*y).upper() for x,y in zip(a,v)]
    weight=h*0+1
    for k in range(1,degree+1):
        a=lower(a);v=lower(v)
        weight=(weight*h/k).upper()
        for m in range(k,degree+1):
            total[m]=(total[m]+weight*(a[m]+h*v[m]/(k+1))).upper()
    return [(total[m]*(m*h*slope).exp()).upper() for m in range(degree+1)]


def gap_source(omega_reference_residual,b_abs,phase_plus_error,phase_minus_error):
    """The source of the correlated omega error in the common-drift chart.

    The supplied error jets belong to the true root labels P_+ and P_-, not
    to guessed physical-ray trajectories. omega_reference_residual is the
    signed common-drift residual before taking its complete cell norm.
    """
    count=len(omega_reference_residual)
    if min(len(phase_plus_error),len(phase_minus_error))<count+1:
        raise ValueError("gap reconstruction needs one more true label derivative")
    return [(omega_reference_residual[m]+b_abs*(m+1)*
             (phase_plus_error[m+1]+phase_minus_error[m+1])/2).upper()
            for m in range(count)]


def initial_whole_circle(node_errors,top_bin_error,halfwidth):
    """Convert signed residual jets at every node to full-cell suprema.

    node_errors[m] is an upper norm of the m-normalized DERIVATIVE of the
    difference at the nodes. top_bin_error bounds the highest (Mth)
    normalized derivative of the difference on whole bins. This function
    uses all lower node differences before taking an angular variation fee.
    """
    M=len(node_errors)
    result=[]
    for m in range(M):
        value=sum((comb(j,m)*node_errors[j]*halfwidth**(j-m)
                   for j in range(m,M)),halfwidth*0)
        result.append((value+comb(M,m)*top_bin_error*halfwidth**(M-m)).upper())
    return result+[top_bin_error.upper()]
