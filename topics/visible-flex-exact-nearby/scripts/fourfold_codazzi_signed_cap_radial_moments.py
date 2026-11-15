#!/usr/bin/env python3
"""New complete known affine moments in the same physical cap.

Pure arithmetic helper for SC.8--SC.22.  It does not load a candidate, construct
a target, change the old trial, or compute any old Gram.  All Fourier products
are complete Laurent products in Arb; the only exponential truncation has its
full Banach-algebra tail.  Derivatives passed here are ordinary derivatives.
"""
from __future__ import annotations

import math
from fractions import Fraction
from flint import arb, acb, acb_poly, arb_mat

ORDER = 3
PHYSICAL_FACTOR = 4
PHYSICAL_TEST_MODES = 128
ORTHONORMAL_INPUTS = 97


def rat(x):
    if isinstance(x, arb):
        return x
    if isinstance(x, Fraction):
        return arb(x.numerator) / x.denominator
    if isinstance(x, int):
        return arb(x)
    if isinstance(x, float):
        f = Fraction.from_float(x)
        return arb(f.numerator) / f.denominator
    f = Fraction(x)
    return arb(f.numerator) / f.denominator


def saved_interval(x):
    """Signed old record; never interpret a midpoint as a complete interval."""
    if not isinstance(x, dict) or "lower" not in x or "upper" not in x:
        raise ValueError("a complete signed lower/upper record is required")
    lo, hi = arb(x["lower"]).lower(), arb(x["upper"]).upper()
    if not lo.is_finite() or not hi.is_finite() or hi < lo:
        raise ArithmeticError("invalid original signed scalar interval")
    return lo.union(hi)


def up(x):
    z = arb(x).upper()
    if not z.is_finite() or z < 0:
        raise ArithmeticError("nonfinite or negative complete error budget")
    return z


def inflate(x, error):
    error = up(error)
    return (x.lower() - error).lower().union((x.upper() + error).upper())


class Laurent:
    """Finite complete sum a[j] exp(i*4*j*phi), with no Fourier truncation."""
    __slots__ = ("lo", "p")

    def __init__(self, coefficients=(), lo=0):
        self.lo = int(lo)
        self.p = coefficients if isinstance(coefficients, acb_poly) else acb_poly(list(coefficients))
        if len(self.p) == 0:
            self.lo = 0

    @staticmethod
    def scalar(x):
        return Laurent([acb(x)], 0)

    @staticmethod
    def one():
        return Laurent.scalar(1)

    def coefficient(self, j):
        k = int(j) - self.lo
        return self.p[k] if 0 <= k < len(self.p) else acb(0)

    def __add__(self, other):
        if not isinstance(other, Laurent):
            other = Laurent.scalar(other)
        lo = min(self.lo, other.lo)
        return Laurent(self.p.left_shift(self.lo-lo) + other.p.left_shift(other.lo-lo), lo)

    __radd__ = __add__

    def __neg__(self):
        return Laurent(-self.p, self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Laurent) else Laurent.scalar(-other))

    def __mul__(self, other):
        if isinstance(other, Laurent):
            return Laurent(self.p * other.p, self.lo + other.lo)
        return Laurent(self.p * acb(other), self.lo)

    __rmul__ = __mul__

    def norm(self):
        return up(sum((abs(self.p[k]) for k in range(len(self.p))), arb(0)))

    def primitive(self):
        values = []
        for k in range(len(self.p)):
            j = self.lo + k
            values.append(self.p[k] / acb(0, PHYSICAL_FACTOR*j) if j else acb(0))
        return Laurent(values, self.lo)

    def nonmean(self):
        values = [self.p[k] for k in range(len(self.p))]
        k = -self.lo
        if 0 <= k < len(values):
            values[k] = acb(0)
        return Laurent(values, self.lo)

    def mean(self):
        z = self.coefficient(0)
        if not z.imag.contains(0):
            raise ArithmeticError("a declared real mean lost its conjugate symmetry")
        return z.real


def trig(sine, cosine):
    """Raw real amplitudes; cosine includes its independent mean at index zero."""
    N = max(len(sine), len(cosine)-1)
    coeff = [acb(0) for _ in range(2*N+1)]
    if cosine:
        coeff[N] = acb(cosine[0])
    for j in range(1, N+1):
        a = sine[j-1] if j <= len(sine) else arb(0)
        b = cosine[j] if j < len(cosine) else arb(0)
        coeff[N+j] = acb(b/2, -a/2)
        coeff[N-j] = acb(b/2, a/2)
    return Laurent(coeff, -N)


def scalar_mul(a, b):
    return [sum((math.comb(k,j)*a[j]*b[k-j] for j in range(k+1)), arb(0))
            for k in range(ORDER+1)]


def scalar_inverse(a):
    if len(a) != ORDER+1 or a[0].contains(0):
        raise ArithmeticError("a whole-row reciprocal has no strict nonzero denominator")
    out = [1/a[0]]
    for k in range(1, ORDER+1):
        out.append(-out[0] * sum((math.comb(k,j)*a[j]*out[k-j]
                                  for j in range(1,k+1)), arb(0)))
    return out


def jet_add(a, b):
    return [a[k]+b[k] for k in range(ORDER+1)]


def jet_mul(a, b):
    return [sum((a[j]*b[k-j]*math.comb(k,j) for j in range(k+1)), Laurent())
            for k in range(ORDER+1)]


def jet_scale(a, scalar):
    return [a[k]*scalar for k in range(ORDER+1)]


def radial_mul(a, scalar):
    return [sum((a[j]*(math.comb(k,j)*scalar[k-j]) for j in range(k+1)), Laurent())
            for k in range(ORDER+1)]


def centered_fields(u, eta, s, curvature):
    """SC.1,8,9; four ordinary jets, same exact candidate/repair in all inputs."""
    if not all(len(x) == ORDER+1 for x in (u,eta,s,curvature)):
        raise ValueError("complete ordinary jets zero through three are required")
    e = [x.mean() for x in eta]
    m = [s[k]+e[k] for k in range(ORDER+1)]
    if not m[0] < 0 or not s[0] < 0:
        raise ArithmeticError("the actual full moving mean and radial reference must be negative")
    invm, invs = scalar_inverse(m), scalar_inverse(s)
    psi = radial_mul([x.primitive() for x in eta], invm)
    numerator = jet_add(jet_mul(u,u),
        radial_mul(jet_mul(jet_add([Laurent.scalar(x) for x in s],eta),eta),curvature))
    q = dict(
        B=jet_scale(radial_mul(u,invm),2),
        C=jet_scale(radial_mul(eta,scalar_mul(invm,invs)),-2),
        A=jet_scale(radial_mul(numerator,invm),2))
    ne = [x.nonmean() for x in eta]
    var = [x.mean() for x in jet_add(jet_mul(u,u),radial_mul(jet_mul(ne,ne),curvature))]
    meanC = [-x for x in scalar_mul(e,scalar_mul(invm,invs))]
    ke, vm = scalar_mul(curvature,e), scalar_mul(var,invm)
    meanA = [ke[k]+vm[k] for k in range(ORDER+1)]
    return dict(psi=psi,q=q,meanC=meanC,meanA=meanA,mean=m,radial=s)


def moment_derivative_bounds(qnorm, pnorm, n):
    """SC.14 and the corresponding orders zero, one and two, on a real row."""
    Q0,Q1,Q2,Q3 = qnorm
    _,P1,P2,P3 = pnorm
    n = abs(int(n))
    return [
        up(Q0),
        up(Q1+n*P1*Q0),
        up(Q2+2*n*P1*Q1+(n*P2+n*n*P1*P1)*Q0),
        up(Q3+3*n*P1*Q2+3*(n*P2+n*n*P1*P1)*Q1
           +(n*P3+3*n*n*P1*P2+n*n*n*P1**3)*Q0)]


def complete_moment_models(mid, whole, exponential_degree=32, modes=128):
    """Three full families, true derivative amplitudes, and complete exp tails.

    Uses shared exact Laurent powers.  It does not differentiate the truncated
    exponential.  Every coefficient used by all original input columns remains.
    """
    if exponential_degree < 0 or modes != PHYSICAL_TEST_MODES:
        raise ValueError("the complete original physical128 testing family is required")
    phase = mid["psi"]
    powers = [Laurent.one()]
    for _ in range(exponential_degree):
        powers.append(powers[-1]*phase[0])
    nvals = [PHYSICAL_FACTOR*l for l in range(1,modes+1)]
    weights = [[acb(1)] for _ in nvals]
    for i,n in enumerate(nvals):
        for k in range(1,exponential_degree+1):
            weights[i].append(weights[i][-1]*acb(0,n)/k)
    pwhole = [x.norm() for x in whole["psi"]]
    pzero = phase[0].norm()
    tails = [up((pzero*n).exp()*(pzero*n)**(exponential_degree+1)
                /math.factorial(exponential_degree+1)) for n in nvals]
    result = {}
    for name in ("B","C","A"):
        q = mid["q"][name]
        basis = [q[0],q[1],q[0]*phase[1],q[2],
                 (q[1]*phase[1])*2+q[0]*phase[2],
                 q[0]*phase[1]*phase[1]]
        bnorm = [x.norm() for x in basis]
        sums = [[acb(0),acb(0),acb(0)] for _ in nvals]
        for k,power in enumerate(powers):
            products = [b*power for b in basis]
            for i,n in enumerate(nvals):
                l = i+1
                c = [p.coefficient(-l) for p in products]
                w = weights[i][k]
                sums[i][0] += w*c[0]
                sums[i][1] += w*(c[1]+acb(0,n)*c[2])
                sums[i][2] += w*(c[3]+acb(0,n)*c[4]-n*n*c[5])
        qwhole = [x.norm() for x in whole["q"][name]]
        family = []
        for i,n in enumerate(nvals):
            amplitude = [bnorm[0],up(bnorm[1]+n*bnorm[2]),
                         up(bnorm[3]+n*bnorm[4]+n*n*bnorm[5])]
            errors = [up(x*tails[i]) for x in amplitude]
            finite = [z.imag if name == "B" else z.real for z in sums[i]]
            family.append(dict(
                mid=[inflate(finite[k],errors[k]) for k in range(3)],
                whole=moment_derivative_bounds(qwhole,pwhole,n),
                finite_exponential_tail=errors))
        result[name] = family
    for name in ("meanC","meanA"):
        result[name] = dict(mid=mid[name][:3],
                           whole=[up(abs(x)) for x in whole[name]])
    result["scope"] = dict(ordinary_derivatives=True,
        physical_test_modes=modes,complete_mean_separate=True,
        exponential_degree=exponential_degree,finite_products_untruncated=True,
        known_real_phase_required_for_whole_derivative_bound=True,
        radial_reference_subtraction_does_not_change_unknown_y=True)
    return result


def weighted_model(model, scalar_mid, scalar_whole):
    """Same radial variable: full Leibniz, not a constant-coefficient shortcut."""
    return dict(
        mid=[sum((math.comb(k,j)*scalar_mid[j]*model["mid"][k-j]
                  for j in range(k+1)),arb(0)) for k in range(3)],
        whole=[up(sum((math.comb(k,j)*abs(scalar_whole[j])*model["whole"][k-j]
                       for j in range(k+1)),arb(0))) for k in range(4)])


def contraction_models(models, beta_mid, beta_whole, gamma_mid, gamma_whole):
    """SC.10 coefficients of z and z_r in original [Bsin128,Cmean,Ccos128] order."""
    M = PHYSICAL_TEST_MODES
    g = [[arb(0) for _ in range(2*M+1)] for _ in range(3)]
    gr = [[arb(0) for _ in range(2*M+1)] for _ in range(3)]
    err = [arb(0) for _ in range(2*M+1)]
    errr = [arb(0) for _ in range(2*M+1)]
    for l in range(1,M+1):
        n = PHYSICAL_FACTOR*l
        B,C,A = (models[name][l-1] for name in ("B","C","A"))
        bB = weighted_model(B,beta_mid,beta_whole)
        bC = weighted_model(C,beta_mid,beta_whole)
        bA = weighted_model(A,beta_mid,beta_whole)
        gB = weighted_model(B,gamma_mid,gamma_whole)
        gA = weighted_model(A,gamma_mid,gamma_whole)
        for k in range(3):
            factorial = math.factorial(k)
            g[k][l-1] = (2*bB["mid"][k]+n*gA["mid"][k])/(2*factorial)
            g[k][M+l] = (-n*gB["mid"][k]+bC["mid"][k]-bA["mid"][k])/(2*factorial)
            gr[k][l-1] = -B["mid"][k]/(2*factorial)
            gr[k][M+l] = -C["mid"][k]/(2*factorial)
        err[l-1] = up((2*bB["whole"][3]+n*gA["whole"][3])/12)
        err[M+l] = up((n*gB["whole"][3]+bC["whole"][3]+bA["whole"][3])/12)
        errr[l-1],errr[M+l] = up(B["whole"][3]/12),up(C["whole"][3]/12)
    mc,ma = models["meanC"],models["meanA"]
    bmc = weighted_model(mc,beta_mid,beta_whole)
    bma = weighted_model(ma,beta_mid,beta_whole)
    for k in range(3):
        g[k][M] = (bmc["mid"][k]-bma["mid"][k])/math.factorial(k)
        gr[k][M] = -mc["mid"][k]/math.factorial(k)
    err[M] = up((bmc["whole"][3]+bma["whole"][3])/6)
    errr[M] = up(mc["whole"][3]/6)
    return dict(z=g,zr=gr,z_error=err,zr_error=errr,
                state_order="Bsin1..128,Cmean,Ccos1..128",
                input_columns=ORTHONORMAL_INPUTS)


def exact_integral_power(left, right, power):
    left,right = Fraction(left),Fraction(right)
    return rat((right**(power+1)-left**(power+1))/(power+1))


def exact_integral_abs_power(left, right, power):
    left,right = Fraction(left),Fraction(right)
    if not left < right or power < 0:
        raise ValueError("a genuine radial interval and nonnegative power are required")
    if left >= 0:
        value = (right**(power+1)-left**(power+1))/(power+1)
    elif right <= 0:
        value = ((-left)**(power+1)-(-right)**(power+1))/(power+1)
    else:
        value = ((-left)**(power+1)+right**(power+1))/(power+1)
    return rat(value)


def absolute_matrix(A):
    return arb_mat([[abs(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())])


def integrate_contraction(models, trial_coefficients, left_minus_center, right_minus_center,
                          with_error_budget=False):
    """Whole signed vector over a true cell, including all ordinary third tails.

    trial_coefficients[p] is the exact/directed 257x97 coefficient of
    (r-c)^p of the original physical Hermite trial, p=0..3.  Its derivative
    is formed from that same polynomial.  No new trial or QR is constructed.
    """
    states,columns = 2*PHYSICAL_TEST_MODES+1,ORTHONORMAL_INPUTS
    if len(trial_coefficients) != 4 or any(
        A.nrows()!=states or A.ncols()!=columns for A in trial_coefficients):
        raise ValueError("the complete original 257-state97-input exact Hermite cubic is required")
    l,r = Fraction(left_minus_center),Fraction(right_minus_center)
    if not l < r:
        raise ValueError("the physical integration interval is empty")
    value,error = arb_mat(1,columns),arb_mat(1,columns)
    for p,A in enumerate(trial_coefficients):
        absolute = absolute_matrix(A)
        for k in range(3):
            mass = exact_integral_power(l,r,p+k)
            value += arb_mat([[x*mass for x in models["z"][k]]])*A
        mass_abs = exact_integral_abs_power(l,r,p+3)
        error += arb_mat([[x*mass_abs for x in models["z_error"]]])*absolute
        if p:
            for k in range(3):
                mass = p*exact_integral_power(l,r,p-1+k)
                value += arb_mat([[x*mass for x in models["zr"][k]]])*A
            mass_abs = p*exact_integral_abs_power(l,r,p+2)
            error += arb_mat([[x*mass_abs for x in models["zr_error"]]])*absolute
    result=[inflate(value[0,j],up(error[0,j])) for j in range(columns)]
    if with_error_budget:
        return result,[up(error[0,j]) for j in range(columns)]
    return result


def target_change_bound(d,mean_abs_lower,mean_bound,shape_A0,jlower,jupper):
    """SC.22, in a full real selected-parameter segment, scalar mean test fixed."""
    d,ml,M,S,jm,jp = map(rat,(d,mean_abs_lower,mean_bound,shape_A0,jlower,jupper))
    if not d >= 0 or not M >= 0 or not S >= 0 or not jm > 0 or not jp >= jm:
        raise ArithmeticError("invalid complete selected target domain")
    gap = ml-d*M
    if not gap > 0:
        raise ArithmeticError("selected full moving mean gap failed")
    ratio = 1+d*M/gap
    return up(d*jp.sqrt()*(M+96*ratio*S/jm))


def evaluate_model(model, displacement):
    """SC18 on the same whole row; no new intrinsic point is sampled."""
    x=rat(displacement)
    value=model["mid"][0]+x*model["mid"][1]+x*x*model["mid"][2]/2
    return inflate(value,model["whole"][3]*abs(x)**3/6)


def endpoint_pairing(models, trial_value, displacement=0):
    """Full SC11 at a true endpoint of the same row and original Hermite."""
    M=PHYSICAL_TEST_MODES
    if trial_value.nrows()!=2*M+1 or trial_value.ncols()!=ORTHONORMAL_INPUTS:
        raise ValueError("all original physical128 rows and97 inputs are required")
    weights=[arb(0) for _ in range(2*M+1)]
    for l in range(1,M+1):
        weights[l-1]=evaluate_model(models["B"][l-1],displacement)/2
        weights[M+l]=evaluate_model(models["C"][l-1],displacement)/2
    weights[M]=evaluate_model(models["meanC"],displacement)
    result=arb_mat([weights])*trial_value
    return [result[0,j] for j in range(ORTHONORMAL_INPUTS)]


def endpoint_parameter_model(models, trial_value):
    """Three ordinary delta jets and a complete third derivative majorant.

    The physical trial is fixed in delta.  The selected test S_delta enters its
    separate left-defect fee, never an extra derivative of this same z.
    """
    M=PHYSICAL_TEST_MODES
    if trial_value.nrows()!=2*M+1 or trial_value.ncols()!=ORTHONORMAL_INPUTS:
        raise ValueError("the same full original physical128-by97 trial is required")
    weights=[[arb(0) for _ in range(2*M+1)] for _ in range(3)]
    third=[arb(0) for _ in range(2*M+1)]
    for l in range(1,M+1):
        for k in range(3):
            weights[k][l-1]=models["B"][l-1]["mid"][k]/2
            weights[k][M+l]=models["C"][l-1]["mid"][k]/2
        third[l-1]=models["B"][l-1]["whole"][3]/2
        third[M+l]=models["C"][l-1]["whole"][3]/2
    for k in range(3):
        weights[k][M]=models["meanC"]["mid"][k]
    third[M]=models["meanC"]["whole"][3]
    jets=arb_mat(weights)*trial_value
    remainder=arb_mat([third])*absolute_matrix(trial_value)
    return dict(ordinary_jets=[[jets[k,j] for j in range(ORTHONORMAL_INPUTS)]
                               for k in range(3)],
                third_bound=[up(remainder[0,j]) for j in range(ORTHONORMAL_INPUTS)])
