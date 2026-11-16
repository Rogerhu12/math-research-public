#!/usr/bin/env sage-python
"""R889: exact Newton germs for the two unchanged original map problems.

Every truncated equation is checked at the full requested precision.  The
large finite reconstruction characteristic pays all indicated denominators.
Characteristic-zero and small-characteristic inputs retain the old recurrence.
All mathematical execution belongs to this public repository Actions.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research repository Actions.")
from sage.all import PowerSeriesRing
from original_low_weight_cm_tools import original_y_germ as _original_y_germ_reference


def _exp_zero(aa, precision):
    """Finite exp via log-Newton; all 1,...,precision-1 are units."""
    ring = aa.parent()
    field = ring.base_ring()
    assert aa[0] == 0
    current = [field.one()]
    known = 1
    while known < precision:
        target = min(2*known, precision)
        ww = ring(current).add_bigoh(target)
        ratio = (ww.derivative()/ww).add_bigoh(target-1)
        logw = ring([field.zero()] +
                    [ratio[j-1]/field(j) for j in range(1, target)]
                    ).add_bigoh(target)
        correction = (aa.add_bigoh(target)-logw).add_bigoh(target)
        assert correction.valuation() >= known
        neww = (ww*(1+correction)).add_bigoh(target)
        current = [neww[j] for j in range(target)]
        known = target
    answer = ring(current).add_bigoh(precision)
    assert answer[0] == 1
    if precision > 1:
        assert (answer.derivative()-aa.derivative()*answer
                ).add_bigoh(precision-1) == 0
    return answer


def _euler_linear(c, aa, bb, precision):
    """Solve c*Q*u' + a*u = b with a(0)=1, without coefficient convolutions."""
    ring = aa.parent()
    field = ring.base_ring()
    qvar = ring.gen()
    assert aa[0] == 1
    exponent = ring([field.zero()] +
                    [aa[j]/field(c*j) for j in range(1, precision)]
                    ).add_bigoh(precision)
    ww = _exp_zero(exponent, precision)
    wb = (ww*bb).add_bigoh(precision)
    diag = ring([wb[j]/field(c*j+1) for j in range(precision)]
                ).add_bigoh(precision)
    answer = (diag/ww).add_bigoh(precision)
    assert (c*qvar*answer.derivative()+aa*answer-bb
            ).add_bigoh(precision) == 0
    return answer


def _newton_p_germ(field, value, ff, source_n, maximum):
    precision = maximum+1
    assert field.is_finite() and int(field.characteristic()) > 6*maximum+1
    assert len(ff) >= precision and field(ff[0]) == 1
    source_n, value = field(source_n), field(value)
    assert source_n != 0
    parameter = source_n**3*value
    ring = PowerSeriesRing(field, "Q", default_prec=precision)
    qvar = ring.gen()
    ec, rc = [field.one()], [field.one()]
    known = 1
    while known < precision:
        target = min(2*known, precision)
        ee = ring(ec).add_bigoh(target)
        rr = ring(rc).add_bigoh(target)
        fs = ring([field(ff[j]) for j in range(target)]).add_bigoh(target)
        fone = (3*qvar*ee.derivative()+ee-fs*rr).add_bigoh(target)
        ftwo = (rr**2-1+4*parameter*qvar*ee**3).add_bigoh(target)
        assert fone.valuation() >= known and ftwo.valuation() >= known
        aa = (1+6*parameter*qvar*fs*ee**2/rr).add_bigoh(target)
        bb = (-fone-fs*ftwo/(2*rr)).add_bigoh(target)
        de = _euler_linear(3, aa, bb, target)
        dr = ((-ftwo-12*parameter*qvar*ee**2*de)/(2*rr)).add_bigoh(target)
        assert de.valuation() >= known and dr.valuation() >= known
        enew, rnew = (ee+de).add_bigoh(target), (rr+dr).add_bigoh(target)
        assert (3*qvar*enew.derivative()+enew-fs*rnew).add_bigoh(target) == 0
        assert (rnew**2-1+4*parameter*qvar*enew**3).add_bigoh(target) == 0
        ec, rc = [enew[j] for j in range(target)], [rnew[j] for j in range(target)]
        known = target
    ee, rr = ring(ec).add_bigoh(precision), ring(rc).add_bigoh(precision)
    yy = (-(1+rr)/(2*source_n**3*ee**3)).add_bigoh(precision)
    result = [yy[j] for j in range(precision)]
    assert result[0] == -1/source_n**3
    if maximum >= 1:
        assert result[1] == -(value+3/source_n**3)/2
    return result


def original_y_germ(field, v, f, n, maximum):
    if field.is_finite() and int(field.characteristic()) > 6*maximum+1:
        return _newton_p_germ(field, v, f, n, maximum)
    return _original_y_germ_reference(field, v, f, n, maximum)


def _short_y_U_reference(field, ff, maximum):
    """U(Q)=q^3*y(q); X^3=U^2-17Q, 2Q U'-U=f0 X^2."""
    if field.is_finite():
        pp = int(field.characteristic())
        assert pp > 6*maximum+1
        fz = [int(field(ff[i])) for i in range(maximum+1)]
        u, xx, bb = [pp-1], [1], [1]
        inv3 = pow(3, -1, pp)
        for n in range(1, maximum+1):
            s = sum(xx[i]*xx[n-i] for i in range(1, n)) % pp
            t = (sum(u[i]*u[n-i] for i in range(1, n))
                 - (17 if n == 1 else 0) - s
                 - sum(bb[i]*xx[n-i] for i in range(1, n))) % pp
            rhs = sum(fz[i]*bb[n-i] for i in range(1, n+1)) % pp
            un = ((2*t+3*s+3*rhs)*pow(6*n+1, -1, pp)) % pp
            xn = ((t-2*un)*inv3) % pp
            u.append(un)
            xx.append(xn)
            bb.append((2*xn+s) % pp)
        assert u[0] == pp-1
        if maximum >= 1:
            assert u[1] == (pp-7) % pp and xx[1] == (pp-1) % pp
        return [field(t) for t in u]
    u, xx, bb = [field(-1)], [field(1)], [field(1)]
    for n in range(1, maximum+1):
        s = sum((xx[i]*xx[n-i] for i in range(1, n)), field(0))
        t = (sum((u[i]*u[n-i] for i in range(1, n)), field(0))
             - (field(17) if n == 1 else field(0)) - s
             - sum((bb[i]*xx[n-i] for i in range(1, n)), field(0)))
        rhs = sum((field(ff[i])*bb[n-i] for i in range(1, n+1)), field(0))
        un = (2*t+3*s+3*rhs)/field(6*n+1)
        xn = (t-2*un)/field(3)
        u.append(un)
        xx.append(xn)
        bb.append(2*xn+s)
    if maximum >= 1:
        assert u[1] == -7 and xx[1] == -1
    return u


def _newton_f_germ(field, ff, maximum):
    precision = maximum+1
    assert field.is_finite() and int(field.characteristic()) > 6*maximum+1
    assert len(ff) >= precision and field(ff[0]) == 1
    ring = PowerSeriesRing(field, "Q", default_prec=precision)
    qvar = ring.gen()
    uc, xc = [field(-1)], [field.one()]
    known = 1
    while known < precision:
        target = min(2*known, precision)
        uu = ring(uc).add_bigoh(target)
        xx = ring(xc).add_bigoh(target)
        fs = ring([field(ff[j]) for j in range(target)]).add_bigoh(target)
        gone = (2*qvar*uu.derivative()-uu-fs*xx**2).add_bigoh(target)
        gtwo = (xx**3-uu**2+17*qvar).add_bigoh(target)
        assert gone.valuation() >= known and gtwo.valuation() >= known
        aa = (-3-4*fs*uu/xx).add_bigoh(target)
        bb = (-3*gone-2*fs*gtwo/xx).add_bigoh(target)
        du = _euler_linear(6, aa, bb, target)
        dx = ((2*uu*du-gtwo)/(3*xx**2)).add_bigoh(target)
        assert du.valuation() >= known and dx.valuation() >= known
        unew, xnew = (uu+du).add_bigoh(target), (xx+dx).add_bigoh(target)
        assert (2*qvar*unew.derivative()-unew-fs*xnew**2).add_bigoh(target) == 0
        assert (xnew**3-unew**2+17*qvar).add_bigoh(target) == 0
        uc, xc = [unew[j] for j in range(target)], [xnew[j] for j in range(target)]
        known = target
    if maximum >= 1:
        assert uc[1] == -7 and xc[1] == -1
    return uc


def short_y_U(field, ff, maximum):
    if field.is_finite() and int(field.characteristic()) > 6*maximum+1:
        return _newton_f_germ(field, ff, maximum)
    return _short_y_U_reference(field, ff, maximum)
