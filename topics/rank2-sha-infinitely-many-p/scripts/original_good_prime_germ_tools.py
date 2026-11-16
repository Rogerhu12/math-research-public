"""R881 good-prime low germs after the original characteristic-zero certificates.

This module contains no reconstruction-existence claim.  Its consumer must
supply the two successful original certificate receipts and the original
geometric prime/embeddings before interpreting a residue as an actual map.
All mathematical execution is restricted to the public repository Actions.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research repository Actions.")

def precision_loss_bound(prime, step, maximum):
    """R881(11), entirely in integers."""
    prime, step, maximum = int(prime), int(step), int(maximum)
    assert prime in (29, 41) and step in (3, 6) and maximum >= 0
    power, bound = prime, 0
    while power <= step*maximum+1:
        bound += maximum//power+1
        power *= prime
    return bound

def _valuation_int(n, prime):
    value = 0
    while n % prime == 0:
        n //= prime
        value += 1
    return value

def _check_coefficient(z, required_precision):
    # Absolute precision is the quantity proved in R881, not relative precision.
    assert z.valuation() >= 0, "The supplied certified good-prime germ is not integral"
    assert z.precision_absolute() >= required_precision, "Insufficient absolute precision"

def _prepare(field, prime, coefficients, maximum, precision):
    prime, maximum, precision = int(prime), int(maximum), int(precision)
    assert prime in (29, 41) and precision >= 64
    assert field(prime).valuation() == 1, "An unramified local field is required"
    assert len(coefficients) >= maximum+1
    values = [field(z) for z in coefficients[:maximum+1]]
    for z in values:
        _check_coefficient(z, precision)
    assert values[0] == 1
    return values

def original_P_good_prime_germ(field, prime, vnew, fP, maximum=1226, precision=64):
    """Return QY for the same scaled original P, with Q=q^3.

    Coordinates remain in the caller's local field.  Apply its fixed residue
    identification with the geometric F_(r^2) only after the final assertions.
    """
    maximum, precision, prime = int(maximum), int(precision), int(prime)
    assert 1 <= maximum <= 1226
    ff = _prepare(field, prime, fP, maximum, precision)
    vv = field(vnew)
    _check_coefficient(vv, precision)
    assert ff[1] == -2
    loss_bound = precision_loss_bound(prime, 3, maximum)
    assert precision-loss_bound >= 1
    aa, a2, a3, root = [field(1)], [field(1)], [field(1)], [field(1)]
    loss = 0
    for n in range(1, maximum+1):
        rn = (-4*vv*a3[n-1]
              -sum((root[i]*root[n-i] for i in range(1, n)), field(0)))/2
        root.append(rn)
        an = sum((ff[i]*root[n-i] for i in range(n+1)), field(0))/field(3*n+1)
        loss += _valuation_int(3*n+1, prime)
        _check_coefficient(rn, precision-loss)
        _check_coefficient(an, precision-loss)
        aa.append(an)
        a2.append(sum((aa[i]*aa[n-i] for i in range(n+1)), field(0)))
        a3.append(sum((a2[i]*aa[n-i] for i in range(n+1)), field(0)))
        _check_coefficient(a2[-1], precision-loss)
        _check_coefficient(a3[-1], precision-loss)
    inverse = [field(1)]
    for n in range(1, maximum+1):
        inverse.append(-sum((a3[i]*inverse[n-i] for i in range(1, n+1)), field(0)))
    qy = []
    for n in range(maximum+1):
        qy.append(-(2*inverse[n]+sum(
            (root[i]*inverse[n-i] for i in range(1, n+1)), field(0)))/2)
    required = precision-loss_bound
    for z in qy:
        _check_coefficient(z, required)
    assert loss <= loss_bound
    assert (qy[0]+1).valuation() >= required
    assert (qy[1]+(vv+3)/2).valuation() >= required
    return qy, {
        "kind": "R881_original_P_good_prime_germ",
        "prime": prime, "maximum": maximum, "input_absolute_precision": precision,
        "proved_loss_bound": loss_bound, "actual_divisor_loss_sum": loss,
        "guaranteed_output_absolute_precision": required,
        "source_parameter": "Q=q^3", "output": "Q*Ynew",
        "scope": "Conditional on the same original characteristic-zero P certificate."
    }

def original_F_good_prime_germ(field, prime, fF, maximum=1428, precision=64):
    """Return U=q^3*y on the original E17, with Q=q^6.

    Multiply by prod(1-Q^n)^12 in the fixed residue field to get R878's V.
    """
    maximum, precision, prime = int(maximum), int(precision), int(prime)
    assert 1 <= maximum <= 1428
    ff = _prepare(field, prime, fF, maximum, precision)
    assert ff[1] == -5
    loss_bound = precision_loss_bound(prime, 6, maximum)
    assert precision-loss_bound >= 1
    uu, xx, bb = [field(-1)], [field(1)], [field(1)]
    loss = 0
    for n in range(1, maximum+1):
        sn = sum((xx[i]*xx[n-i] for i in range(1, n)), field(0))
        tn = (sum((uu[i]*uu[n-i] for i in range(1, n)), field(0))
              -(field(17) if n == 1 else field(0))-sn
              -sum((bb[i]*xx[n-i] for i in range(1, n)), field(0)))
        rhs = sum((ff[i]*bb[n-i] for i in range(1, n+1)), field(0))
        un = (2*tn+3*sn+3*rhs)/field(6*n+1)
        xn = (tn-2*un)/3
        loss += _valuation_int(6*n+1, prime)
        _check_coefficient(un, precision-loss)
        _check_coefficient(xn, precision-loss)
        uu.append(un)
        xx.append(xn)
        bb.append(2*xn+sn)
        _check_coefficient(bb[-1], precision-loss)
    required = precision-loss_bound
    for z in uu:
        _check_coefficient(z, required)
    assert loss <= loss_bound
    assert (uu[0]+1).valuation() >= required
    assert (uu[1]+7).valuation() >= required
    return uu, {
        "kind": "R881_original_F_good_prime_germ",
        "prime": prime, "maximum": maximum, "input_absolute_precision": precision,
        "proved_loss_bound": loss_bound, "actual_divisor_loss_sum": loss,
        "guaranteed_output_absolute_precision": required,
        "source_parameter": "Q=q^6", "output": "q^3*yF",
        "scope": "Conditional on the same original characteristic-zero F certificate."
    }
