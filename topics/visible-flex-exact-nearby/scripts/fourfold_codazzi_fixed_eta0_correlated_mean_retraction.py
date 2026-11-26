#!/usr/bin/env python3
"""One new fixed-eta0, same-r Taylor mean retraction on the original raw centre.

Only public Actions may execute this consumer. Original completed residual and
Green targets are never called. The old 7296-row native supplies its immutable
partition and identity, not a replacement signed integral. The exact affine
object and all original PPoly coefficients are materialized privately only
for this new integral. Native Acb Fourier arithmetic retains every primitive
tail. Only complete scalar conclusions, counts and provenance leave the runner.
"""
from __future__ import annotations
import argparse, gzip, hashlib, io, json, math, os, time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb, acb, acb_series, ctx
from fourfold_phase_beta_interval import NativeSpline, primitive_fourier_budget
from fourfold_phase_beta_bulk_interval import BulkTarget, exact_arb

REPO = 'Rogerhu12/math-research-public'
KIND = 'R144_fixed_eta0_correlated_rotational_mean_retraction_v1'
NATIVE = '6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1'
NATIVE_SOURCE = '24ec0bf2b9d2b03ebfa07f4b39b8fdee3277f8e4b2aa14385c267122e6b8e81f'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OBJECT = '91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
ALPHA = Fraction(6890507429876859, 9007199254740992)
NU = Fraction(-2572625729470897, 72057594037927936)
ETA = Fraction(-7789843107295549, 4611686018427387904)
ROWS, PIECES, JOINS, MODES = 7296, 6144, 6143, 32
DEGREE, NODES, BITS = 24, 512, 320
END = Fraction(25, 8)
ZEROS = ('old_completed_scientific_targets_called old_mean_Green_targets_called '
         'old_residual_targets_called old_response_targets_called '
         'old_angular_solver_calls published_arrays').split()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'),
            ensure_ascii=False, allow_nan=False)+'\n').encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name+'.tmp')
    with tmp.open('wb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(tmp, path)


def rat(value):
    return exact_arb(Fraction(value))


def unpack(value):
    e = int(value['decimal_exponent'])
    scale = rat(10**e) if e >= 0 else rat(Fraction(1, 10**(-e)))
    m = rat(int(value['midpoint_integer']))*scale
    r = rat(int(value['radius_integer']))*scale
    return (m-r).lower().union((m+r).upper())


def record(value, direction='enclosure'):
    require(value.is_finite(), 'finite complete new scalar')
    m, r, e = value.mid_rad_10exp(75)
    out = dict(kind='complete_decimal_ball_v1', mathematical_direction=direction,
               midpoint_integer=str(int(m)), radius_integer=str(int(r)),
               decimal_exponent=str(int(e)))
    require(int(r) >= 0 and unpack(out).contains(value), 'whole saved scalar containment')
    return out


def real(value, label):
    z = acb(value)
    require(z.is_finite() and z.imag.contains(0), 'finite real coefficient: '+label)
    return z.real


def rseries(value, count, label):
    require(value.prec >= count, 'complete Taylor order: '+label)
    return acb_series([acb(real(value[j], label)) for j in range(count)], prec=count)


def sym(radius):
    return arb(0, radius.upper())


def positive_inverse(value):
    lo, hi = value.lower(), value.upper()
    require(lo > 0, 'strict positive inverse input')
    return (1/hi).lower().union((1/lo).upper())


def modulus(value):
    return abs(value).upper()


def evaluate(series, x, count=None):
    count = series.prec if count is None else count
    out = acb(0)
    for j in range(count-1, -1, -1):
        out = out*x+series[j]
    return out


def polynomial(coefficients, x):
    out = acb_series([0])
    for coefficient in coefficients[::-1]:
        out = out*x+coefficient
    return out


def bump(left, right, z):
    lo, hi = Fraction(1, 20), Fraction(9, 50)
    if right <= lo or left >= hi:
        return acb_series([0])
    require(lo <= left < right <= hi, 'one exact compact-control polynomial')
    t = (z-rat(lo))*100/13
    return 4096*t**6*(1-t)**6


class FixedObject(BulkTarget):
    """Exact affine centre, with no nonzero parameter box silently retained."""
    def __init__(self, object_path, topic):
        definition = parse(Path(object_path).read_bytes())
        require(sha(Path(object_path).read_bytes()) == OBJECT
                and definition['kind'] == 'exact_affine_symmetric_infinite_R33_graph',
                'unchanged exact affine object')
        q = definition['delta_fraction']
        eta = Fraction(int(q['numerator']), int(q['denominator']))
        require(eta == ETA, 'the actual fixed affine parameter eta0')
        origin = topic/definition['origin_inputs']['path']
        direction = topic/definition['direction']['path']
        require(sha(origin.read_bytes()) == definition['origin_inputs']['sha256']
                and sha(direction.read_bytes()) == definition['direction']['sha256'],
                'original frozen affine definition bytes')
        super().__init__(origin, NODES, NODES, arb('.003'), arb('.0025'), arb('.32'))
        with np.load(direction, allow_pickle=False) as saved:
            dr = saved['phase_direction_coefficients'].copy()
            da = saved['alpha_direction'].copy()
        require(dr.shape == self.frozen['phase_coefficients'].shape
                and da.shape == self.frozen['alpha'].shape, 'full exact affine dimensions')
        base = self.frozen['phase_coefficients']
        coefficients = np.empty(base.shape, object)
        for index in np.ndindex(base.shape):
            coefficients[index] = arb(float(base[index]))+rat(eta)*arb(float(dr[index]))
        self.raw = NativeSpline([arb(float(x)) for x in self.frozen['phase_knots']],
                                coefficients, 5, converted=True)
        self.alpha = [arb(float(a))+rat(eta)*arb(float(v))
                      for a, v in zip(self.frozen['alpha'], da)]
        cuts = {Fraction(0), Fraction(3)}
        for name, values in self.frozen.items():
            if name.endswith('_knots'):
                for value in values:
                    r = abs(Fraction.from_float(float(value)))
                    if 0 <= r <= 3:
                        cuts.add(r)
        self.cuts = sorted(cuts)
        self.sigma = arb('.32')
        self.tail_constant = primitive_fourier_budget(
            NODES, self.sigma, arb(0), arb('.003'), arb(1), arb(0), arb(1))[0][0]
        self.graft = None
        self.carrier_calls = 0
        self.complex_calls = 0
        self.angular_tail_max = arb(0)

    def select(self, left, right):
        if right <= 3:
            k = bisect_right(self.cuts, left)-1
            if left == 3:
                k -= 1
            gl, gr = self.cuts[k:k+2]
            require(gl <= left < right <= gr, 'original body scalar germ')
            self.set_cell(gl, gr)
            return 'body', (gl, gr)
        require(3 <= left < right <= END, 'the exact natural graft interval')
        if self.graft is None:
            self.graft = FixedGraft(self)
        return 'graft', (Fraction(3), END)

    def scalar_data(self, z, part):
        if part == 'body':
            beta, vertical, radius, height = self.scalars(z, 1)
            L = radius.derivative()/radius
            H = height.derivative()/radius**2
            return beta, vertical, radius, L, H
        return self.graft.scalars(z)

    def tail(self, center, padding, part):
        old, ctx.cap = ctx.cap, 2
        try:
            square = acb(center)+acb(sym(padding), sym(padding))
            beta, vertical, _, _, _ = self.scalar_data(square, part)
            phase = sum(((modulus(beta[j][0])+modulus(vertical[j][0]))
                         *(self.sigma*(j+1)).cosh()
                         for j in range(self.modes)), arb(0)).upper()
            out = (self.tail_constant*phase*phase.exp()).upper()
            require(out.is_finite(), 'complete primitive analytic-strip tail')
            self.angular_tail_max = max(self.angular_tail_max, out).upper()
            return out
        finally:
            ctx.cap = old

    def intrinsic(self, center, count, part, tail_radius, real_input):
        """Complete target Taylor coefficients, including all primitive aliases."""
        old, ctx.cap = ctx.cap, count
        try:
            beta, vertical, a, L, H = self.scalar_data(acb(center), part)
            tangent = []
            for k in range(NODES):
                b = sum((beta[j]*self.sines[j, k] for j in range(self.modes)),
                        acb_series([0]))
                g = sum((vertical[j]*self.sines[j, k] for j in range(self.modes)),
                        acb_series([0]))
                sb, sg = b.sin(), g.sin()
                cbm, cgm = -2*(b/2).sin()**2, -2*(g/2).sin()**2
                tangent.append((-(1+cgm)*sb, cgm+cbm+cgm*cbm, sg))
            transformed = [[None]*3 for _ in range(NODES)]
            arrays = [[[acb(0) for _ in range(count)] for _ in range(3)]
                      for _ in range(NODES)]
            for j in range(3):
                for q in range(count):
                    values = acb.dft([tangent[k][j][q] for k in range(NODES)])
                    for k in range(NODES):
                        arrays[k][j][q] = values[k]/NODES
            for k, frequency in enumerate(self.frequency):
                coeff = [acb_series(arrays[k][j], prec=count) for j in range(3)]
                transformed[k][0] = (acb(0, frequency)*coeff[0]+coeff[1])/(1-frequency**2)
                transformed[k][1] = (-coeff[0]+acb(0, frequency)*coeff[1])/(1-frequency**2)
                transformed[k][2] = coeff[2]/acb(0, frequency) if frequency else acb_series([0])
            for j in range(3):
                transformed[NODES//2][j] = acb_series([0])
            transformed[0][1], transformed[0][2] = acb_series([0]), acb_series([0])
            for k in range(1, NODES//2):
                for j, parity in enumerate((1, -1, 1)):
                    value = (transformed[k][j]+parity*transformed[-k][j])/2
                    transformed[k][j], transformed[-k][j] = value, parity*value
            # Each epsilon is a coefficient error, not a derivative error.
            tail = self.tail(center, tail_radius, part)
            eps = [tail/tail_radius**q for q in range(count)]
            u = [[L*row[j]+row[j].derivative() for j in range(3)]
                 for row in transformed]
            order = count-1
            eu, Mu = [], []
            for q in range(order):
                eu.append(((q+1)*eps[q+1]+sum(
                    (modulus(L[i])*eps[q-i] for i in range(q+1)), arb(0))).upper())
                Mu.append(max(sum((modulus(u[k][j][q]) for k in range(NODES)), arb(0))
                              for j in range(3)).upper())
            energy = 2*L*u[0][0]+sum(
                (u[k][j]*u[(-k) % NODES][j]
                 for k in range(NODES) for j in range(3)), acb_series([0]))
            padded = []
            for q in range(order):
                fee = sum((2*modulus(L[i])*eu[q-i]
                    +3*(Mu[i]*eu[q-i]+Mu[q-i]*eu[i]+eu[i]*eu[q-i])
                    for i in range(q+1)), arb(0)).upper()
                if real_input:
                    padded.append(acb(real(energy[q], 'energy')+sym(fee)))
                else:
                    padded.append(energy[q]+acb(sym(fee), sym(fee)))
            energy = acb_series(padded, prec=order)
            if real_input:
                a, L, H = (rseries(a, count, 'a'), rseries(L, order, 'beta'),
                           rseries(H, order, 'H'))
            Ebar = L**2+a**2*H**2+energy
            Kold = (H**2*(L**2-L.derivative())+L*H*H.derivative()
                    +(L*energy.derivative()-2*L.derivative()*energy)/(2*a**2))/Ebar**2
            self.carrier_calls += 1
            if not real_input:
                self.complex_calls += 1
            return dict(a=a, beta=L, H=H, energy=energy, Ebar=Ebar,
                        Kold=Kold, primitive_tail=tail)
        finally:
            ctx.cap = old


class FixedGraft:
    """The original exact natural graft evaluated at eta0, without a wide box."""
    def __init__(self, body):
        body.set_cell(body.cuts[-2], Fraction(3))
        old, ctx.cap = ctx.cap, 8
        try:
            beta, vertical, a, z = body.scalars(acb(3), 1)
            la, H = a.log(), z.derivative()/a**2
            self.loga = [real(la[j], 'graft log radius') for j in range(5)]
            self.H = [real(H[j], 'graft slope ratio') for j in range(4)]
            self.beta = [[real((v/a**3)[j], 'graft beta') for j in range(5)]
                         for v in beta]
            self.vertical = [[real((v/a**2)[j], 'graft gamma') for j in range(5)]
                             for v in vertical]
        finally:
            ctx.cap = old

    def scalars(self, center):
        s = acb_series([acb(center)-3, 1])
        t = 8*s
        chi = (1-t)**5*(1+5*t+15*t**2+35*t**3+70*t**4)
        loga = self.loga[0]+self.loga[1]*s+chi*sum(
            (self.loga[j]*s**j for j in range(2, 5)), acb_series([0]))
        a = loga.exp()
        H = self.H[0]+chi*sum((self.H[j]*s**j for j in range(1, 4)), acb_series([0]))
        beta = [a**3*chi*polynomial(row, s) for row in self.beta]
        vertical = [a**2*chi*polynomial(row, s) for row in self.vertical]
        return beta, vertical, a, loga.derivative(), H


def raw_polynomials(coefficients, knot, center):
    x = acb_series([acb(center)-rat(knot), 1])
    state = []
    for j in range(2*MODES+1):
        p = acb_series([0])
        for q in range(4):
            p = p*x+arb(float(coefficients[q, j]))
        state.append(rat(ALPHA)*p)
    w = state[MODES]
    U = sum((p*p for p in state[:MODES]), acb_series([0]))/2
    V = sum((p*p for p in state[MODES+1:]), acb_series([0]))/2
    return w, U, V


def mean_value(coefficients, knot, point):
    delta = rat(point-knot)
    out = arb(0)
    for q in range(4):
        out = out*delta+arb(float(coefficients[q, MODES]))
    return rat(ALPHA)*out


def source_carrier(target, coefficients, knot, left, right, center, count,
                   part, tail_radius, real_input):
    old, ctx.cap = ctx.cap, count
    try:
        data = target.intrinsic(center, count, part, tail_radius, real_input)
        a, L, H, energy, Ebar = (data[k] for k in ('a', 'beta', 'H', 'energy', 'Ebar'))
        z = acb_series([acb(center), 1])
        hh = bump(left, right, z)
        control = (rat(NU)*hh).exp()
        # Avoid a constant subtraction outside the compact support.
        expminus = acb_series([(rat(NU)*hh[0]).expm1()]
                              +[control[j] for j in range(1, control.prec)],
                              prec=control.prec)
        G = Ebar*control
        R = H**2+energy/a**2+Ebar/a**2*expminus
        ratio = G/R
        require(a[0].abs_lower() > 0 and Ebar[0].real > 0
                and G[0].real > 0 and R[0].real > 0 and ratio[0].real > 0,
                'complete holomorphic rotational chart on the stated disc')
        s = -ratio.sqrt()
        K = (data['Kold']+rat(NU)*L*hh.derivative()/(2*a**2*Ebar))/control
        w, U, V = raw_polynomials(coefficients, knot, center)
        m = s+w
        require(m[0].real < 0, 'complete nonzero negative raw mean on stated disc')
        Ns, n = a**2/s**2, a**2/m**2
        N = a**2*w*(2*s+w)/(s**2*m**2)
        c = 2*L*U
        b = 2*L*a**2*(U/s**2+K*V/m**2)
        values = dict(a=a, s=s, m=m, U=U, V=V, Ns=Ns, n=n, N=N, c=c, b=b)
        for name, value in values.items():
            require(value[0].is_finite(), 'finite new correlated carrier: '+name)
        if real_input:
            values = {name: rseries(value, min(value.prec, DEGREE+2), name)
                      for name, value in values.items()}
        return values
    finally:
        ctx.cap = old


def local_model(target, coefficients, knot, left, right):
    part, germ = target.select(left, right)
    mid, half = (left+right)/2, (right-left)/2
    rho = 8*half
    radius, h = rat(rho), rat(half)
    center = rat(mid)
    # This square contains the closed complex radius-rho disc. Only the
    # fixed local polynomial germ is continued; no real target is extrapolated.
    zbox = acb(center+sym(radius), sym(radius))
    bound = source_carrier(target, coefficients, knot, left, right, zbox, 3,
                           part, arb('.003'), False)
    magnitudes = {name: modulus(value[0]) for name, value in bound.items()}
    point = source_carrier(target, coefficients, knot, left, right, acb(center),
                           DEGREE+4, part, max(radius, arb('.003')).upper(), True)
    require(all(point[name].prec >= DEGREE+2 for name in ('a', 's', 'm', 'Ns', 'n', 'N')),
            'complete same-r state Taylor coefficients')
    require(point['c'].prec >= DEGREE+1 and point['b'].prec >= DEGREE+1,
            'complete same-r linear-equation Taylor coefficients')
    old, ctx.cap = ctx.cap, DEGREE+2
    try:
        Ci = acb_series([0]+[point['c'][j]/(j+1) for j in range(DEGREE+1)],
                        prec=DEGREE+2)
        P = Ci.exp()
        quotient = point['b']/P
        Q = acb_series([0]+[quotient[j]/(j+1) for j in range(DEGREE+1)],
                       prec=DEGREE+2)
    finally:
        ctx.cap = old
    theta = h/radius
    require(theta < 1, 'strictly nested Cauchy radius')
    tail_factor = (theta**(DEGREE+2)/(1-theta)).upper()
    MP = (radius*magnitudes['c']).exp().upper()
    MQ = (radius*magnitudes['b']*MP).upper()
    eP, eQ = (MP*tail_factor).upper(), (MQ*tail_factor).upper()
    def point_enclosure(series, x, error):
        return real(evaluate(series, x, DEGREE+2), 'real Taylor evaluation')+sym(error)
    exponential = (-h*magnitudes['c']).exp().lower().union(
                   (h*magnitudes['c']).exp().upper())
    PL = point_enclosure(P, -h, eP).intersection(exponential)
    PR = point_enclosure(P, h, eP).intersection(exponential)
    QL, QR = point_enclosure(Q, -h, eQ), point_enclosure(Q, h, eQ)
    require(PL.lower() > 0 and PR.lower() > 0, 'strict positive exact local multipliers')
    return dict(left=left, right=right, part=part, germ=germ, h=h, radius=radius,
        point=point, magnitudes=magnitudes, P=P, Q=Q, PL=PL, PR=PR, QL=QL, QR=QR,
        MP=MP, MQ=MQ, tail_factor=tail_factor, eP=eP, eQ=eQ)


def advance(model, Wleft, Gleft, Aleft):
    old, ctx.cap = ctx.cap, DEGREE+2
    try:
        T = Wleft*positive_inverse(model['PL'])-model['QL']
        Wseries = model['P']*(acb(T)+model['Q'])
        MW = (model['MP']*(modulus(T)+model['MQ'])).upper()
        eW = (MW*model['tail_factor']).upper()
        source = model['point']
        Dseries = Wseries+source['N']
        Yseries = Wseries+source['Ns']
        h = model['h']
        interval = (-h).lower().union(h.upper())
        def value(name, x):
            if name == 'W':
                polynomial_, fee = Wseries, eW
            elif name == 'D':
                polynomial_, fee = Dseries, eW+model['magnitudes']['N']*model['tail_factor']
            elif name == 'Y':
                polynomial_, fee = Yseries, eW+model['magnitudes']['Ns']*model['tail_factor']
            else:
                polynomial_, fee = source[name], model['magnitudes'][name]*model['tail_factor']
            return real(evaluate(polynomial_, x, DEGREE+2), name+' real interval')+sym(fee.upper())
        whole = {name: value(name, interval) for name in ('W', 'D', 'Y', 'a', 's', 'm', 'n', 'V')}
        end = {name: value(name, h) for name in ('W', 'D', 'Y', 'a', 's', 'm', 'n')}
        begin = {name: value(name, -h) for name in ('a', 's', 'm', 'n')}
        factor = model['PR']*positive_inverse(model['PL'])
        Wdirect = model['PR']*(T+model['QR'])
        end['W'] = end['W'].intersection(Wdirect)
        for values in (whole, end, begin):
            require(values['a'].lower() > 0 and values['m'].upper() < 0,
                    'actual real whole-cell mean and radius chart')
            aL, aU = values['a'].lower(), values['a'].upper()
            mL, mU = (-values['m']).lower(), (-values['m']).upper()
            np = (aL*aL/(mU*mU)).lower().union((aU*aU/(mL*mL)).upper())
            values['n'] = values['n'].intersection(np)
        whole['Y'] = whole['Y'].intersection(whole['n']+whole['D'])
        end['Y'] = end['Y'].intersection(end['n']+end['D'])
        whole['V'] = whole['V'].intersection(arb(0).union(whole['V'].upper()))
        return dict(W=end['W'], G=Gleft*factor, A=Aleft*factor,
                    whole=whole, end=end, begin=begin, factor=factor,
                    cauchy_W_error=eW, cauchy_D_error=(eW+model['magnitudes']['N']*model['tail_factor']).upper())
    finally:
        ctx.cap = old


def kernels(n, Y, a):
    nl, nu, yl, yu = n.lower(), n.upper(), Y.lower(), Y.upper()
    require(nl > 0 and yl > 0 and a.lower() > 0, 'positive physical ratio inputs')
    snl, snu = nl.sqrt().lower(), nu.sqrt().upper()
    syl, syu = yl.sqrt().lower(), yu.sqrt().upper()
    dl = (syl*(snl+syl)).lower()
    du = (syu*(snu+syu)).upper()
    kl = (1/du).lower()
    ku = (1/dl).upper()
    pl = (a.lower()*(snl+syl)).lower()
    pu = (a.upper()*(snu+syu)).upper()
    require(dl > 0 and du > 0 and pl > 0 and pu > 0, 'positive endpoint denominator bounds')
    return kl.union(ku), ku, (1/pu).lower().union((1/pl).upper())


def load_candidate(path):
    path = Path(path)
    require(sha(path.read_bytes()) == CANDIDATE, 'unchanged original candidate index')
    doc = parse(path.read_bytes())
    require(doc['kind'] == 'complete_lossless_radial_cubic_shards_v1'
            and doc['coefficient_shape'] == [4, PIECES, 65]
            and doc['radial_nodes_count'] == PIECES+1, 'complete original raw PPoly shape')
    nodes, blocks, endpoint, next_piece = [], [], None, 0
    for item in doc['parts']:
        require(Path(item['file']).name == item['file'], 'local original shard')
        raw = (path.parent/item['file']).read_bytes()
        require(len(raw) == item['bytes'] and sha(raw) == item['sha256'],
                'complete original candidate shard identity')
        with np.load(io.BytesIO(gzip.decompress(raw)), allow_pickle=False) as data:
            r, c = data['radial_nodes'].copy(), data['piece_coefficients'].copy()
        require(item['first_interval'] == next_piece and c.shape == (4, len(r)-1, 65)
                and bool(np.all(np.diff(r) > 0)) and bool(np.all(np.isfinite(c))),
                'original exact cubic piece coverage')
        if endpoint is not None:
            require(r[0].view(np.uint64) == endpoint.view(np.uint64), 'bitwise shared shard endpoint')
        nodes.append(r if endpoint is None else r[1:])
        blocks.append(c)
        endpoint, next_piece = r[-1], item['last_interval_exclusive']
    r, c = np.concatenate(nodes), np.concatenate(blocks, axis=1)
    require(c.shape == (4, PIECES, 65) and len(r) == PIECES+1 and next_piece == PIECES,
            'all original raw cubic pieces loaded')
    meta = doc['metadata']
    require(meta['modes'] == MODES and meta['object_sha256'] == OBJECT
            and meta['exact_float_amplitude'] == str(ALPHA)
            and meta['exact_float_nu'] == str(NU), 'same raw centre and physical metric')
    require(np.array_equal(c[3, 0, :], np.asarray(doc['initial_state'], dtype=np.float64)),
            'initial state is the original first PPoly trace')
    knots = [Fraction.from_float(float(x)) for x in r]
    require(knots[0] == 0 and knots[-1] == END, 'whole original exact radial interval')
    return doc, knots, c


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native', type=Path, required=True)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--object', type=Path, required=True)
    ap.add_argument('--topic', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == REPO, 'public Actions only')
    require(not args.output.exists(), 'preserve every complete or failed actual output')
    ctx.prec, ctx.cap = BITS, DEGREE+4
    began = time.monotonic()
    doc = dict(identity=dict(kind=KIND, source_sha256=sha(Path(__file__).read_bytes()),
        original_native_sha256=NATIVE, original_native_source_sha256=NATIVE_SOURCE,
        original_candidate_sha256=CANDIDATE, object_sha256=OBJECT, exact_eta=str(ETA),
        exact_nu=str(NU), exact_alpha=str(ALPHA), intrinsic_parameter_half_width='0',
        exact_interval=['0', '25/8'], original_closed_rows=ROWS, original_pieces=PIECES,
        original_interfaces=JOINS, original_modes=MODES, arithmetic_bits=BITS,
        Taylor_source_degree=DEGREE, primitive_nodes=NODES, analytic_angular_strip='8/25',
        radial_Cauchy_radius_to_halfwidth='8', primary_equation="W'=2 beta U W+2 beta a^2(U/s^2+K V/m^2)",
        primary_initial_value='W(0)=0', recovered_D='W+a^2*w*(2*s+w)/(s^2*m^2)'),
        complete=False, proved=False, failure=None, stage='input-admission',
        completed_common_cells=0, expected_common_cells=ROWS, completed_mean_interfaces=0,
        expected_mean_interfaces=JOINS, completed_subcells=0, current_exact_right='0',
        active_original_row=0, interface_consumed_for_active_row=False, current_candidate_piece=0,
        complete_new_scalars={}, continuation_state={}, first_unresolved_positivity=None,
        certified_negative_Y_witness=None, certified_violation_witness=None,
        strict_gates=dict(positive_mean_everywhere='unknown',
            componentwise_moving_C0_within_1e4='unknown', outer_mean_unchanged='unknown'),
        rematerialization=dict(target='only new fixed-eta0 correlated mean integral',
            complete_interval=['0', '25/8'], old_completed_targets_recomputed=0,
            point_carriers=0, complex_disc_carriers=0, local_disc_subdivisions=0,
            original_residual_values_consumed=False, old_7296_partition_consumed=True,
            original_6144_raw_pieces_consumed=True, all_infinite_primitive_tails_retained=True),
        scope=dict(fixed_eta0_and_original_nu0=True, same_u_and_density_j=True,
            true_same_r_products_and_weighted_integral=True, full_forward_D_sensitivity_retained=True,
            all_original_mean_interfaces_retained=True, detailed_rows_private_only=True,
            old_full_eta_rowrange_target_recomputed=False, old_residual_target_recomputed=False,
            continuous_Qrepair_or_selected_delta_inherited=False, selected_phase_preserved=False,
            nonmean_equations_solved=False, outer_cap_or_height_matched=False,
            body_inverse_proved=False, final_topic_complete=False),
        private_trace=dict(records=0, bytes=0, sha256=None, content_published=False,
            scope='saved_accepted_checkpoint_prefix'),
        seconds=0., **{key: 0 for key in ZEROS})
    trace = args.output.with_name('private-fixed-eta0-mean-retraction.ndjson')
    trace_hash, trace_records, trace_bytes = hashlib.sha256(), 0, 0
    target = None
    W, G, A, D0, ymin, vmax, max_cauchy = arb(0), arb(1), arb(0), None, None, arb(0), arb(0)
    last, last_piece, all_positive = None, 0, True

    def snapshot():
        doc['seconds'] = time.monotonic()-began
        doc['private_trace'] = dict(records=trace_records, bytes=trace_bytes,
            sha256=trace_hash.hexdigest(), content_published=False,
            scope='saved_accepted_checkpoint_prefix')
        if target is not None:
            doc['rematerialization']['point_carriers'] = target.carrier_calls-target.complex_calls
            doc['rematerialization']['complex_disc_carriers'] = target.complex_calls
        atomic(args.output, encode(doc))

    def append_trace(value):
        nonlocal trace_records, trace_bytes
        raw = encode(value)
        with trace.open('ab') as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        trace_hash.update(raw)
        trace_records += 1
        trace_bytes += len(raw)

    def save_state():
        values = dict(W_at_current_right=W, forward_multiplier_at_current_right=G,
                      signed_mean_atoms_at_current_right=A,
                      v_difference_upper_on_positive_cells=vmax,
                      maximum_local_D_Cauchy_remainder=max_cauchy)
        if D0 is not None:
            values['initial_D'] = D0
            values['propagated_initial_D'] = G*D0
        if ymin is not None:
            values['Y_lower_over_completed_cells'] = ymin
        if last is not None:
            values.update(D_at_current_right=last['D'], Y_at_current_right=last['Y'],
                          n_at_current_right=last['n'], a_at_current_right=last['a'],
                          s_at_current_right=last['s'], m_at_current_right=last['m'])
            values['signed_bulk_D_at_current_right'] = last['D']-G*D0-A
            if last['Y'].lower() > 0:
                kernel, _, physical = kernels(last['n'], last['Y'], last['a'])
                values['mean_shift_at_current_right'] = -last['m']*last['D']*kernel
                values['physical_Cmean_shift_at_current_right'] = -last['D']*physical
        if target is not None:
            values['maximum_complete_primitive_tail'] = target.angular_tail_max
        doc['complete_new_scalars'] = {name: record(value) for name, value in values.items()}
        doc['continuation_state'] = dict(all_completed_Y_intervals_strictly_positive=all_positive,
            last_completed_piece=last_piece, first_unresolved_positivity=doc['first_unresolved_positivity'],
            certified_negative_Y_witness=doc['certified_negative_Y_witness'],
            certified_violation_witness=doc['certified_violation_witness'],
            state_is_after_current_interface=doc['interface_consumed_for_active_row'])
        snapshot()

    snapshot()
    try:
        raw = args.native.read_bytes()
        require(sha(raw) == NATIVE, 'complete unchanged 7296-row original native')
        native = parse(gzip.decompress(raw))
        require(native['complete'] is True and native['failure'] is None
                and native['kind'] == 'complete_actual_moving_residual_all_closed_rows_and_interfaces'
                and native['source_sha256'] == NATIVE_SOURCE
                and native['candidate_sha256'] == CANDIDATE and native['object_sha256'] == OBJECT
                and native['exact_amplitude'] == str(ALPHA) and native['exact_nu'] == str(NU)
                and native['interval'] == ['0', '25/8'] and len(native['rows']) == ROWS
                and len(native['complete_interface_jumps']) == JOINS
                and native['all_7296_closed_rows_reused_without_recomputation'] is True
                and native['all_6143_actual_interfaces_paid'] is True,
                'complete old whole-domain qualification and exact raw identity')
        require(arb(native['bounds']['minimum_pointwise_v_gap']['ball']) > 0
                and arb(native['bounds']['minimum_mean_gap']['ball']) > 0,
                'already completed whole raw density and mean gap qualification')
        _, knots, coefficients = load_candidate(args.candidate)
        rows = native['rows']
        expected_left, transitions, previous_piece = Fraction(0), 0, 0
        partition = []
        for index, row in enumerate(rows):
            left, right = map(Fraction, row['interval'])
            piece = int(row['candidate_piece'])
            require(row['index'] == index and left == expected_left and left < right
                    and piece == bisect_right(knots, left)-1
                    and knots[piece] <= left < right <= knots[piece+1],
                    'unchanged complete original closed partition')
            if index and piece != previous_piece:
                require(piece == previous_piece+1 and left == knots[piece], 'every actual consecutive raw join')
                transitions += 1
            partition.append([str(left), str(right)])
            previous_piece, expected_left = piece, right
        require(expected_left == END and transitions == JOINS and previous_piece == PIECES-1,
                'whole cover and all 6143 exact original joins')
        require(sha(json.dumps(partition).encode()) == native['exact_full_partition_sha256'],
                'original complete partition SHA256')
        target = FixedObject(args.object, args.topic)
        # The accepted native already refines these exact branches. Verify
        # this explicitly; dyadic trial subdivision may not find a rational
        # compact endpoint such as 1/20 or 9/50.
        branches = sorted(set(target.cuts+[Fraction(1, 20), Fraction(9, 50),
                                          Fraction(3), END]))
        for row in rows:
            lo, hi = map(Fraction, row['interval'])
            position = bisect_right(branches, lo)
            require(position == len(branches) or hi <= branches[position],
                    'old complete row includes every exact scalar/compact/graft branch cut')
        target.select(*map(Fraction, rows[0]['interval']))
        old, ctx.cap = ctx.cap, 2
        try:
            a0 = real(target.scalars(acb(0), 1)[2][0], 'exact waist radius')
        finally:
            ctx.cap = old
        w0 = mean_value(coefficients[:, 0, :], knots[0], Fraction(0))
        require(a0 > 0, 'strict positive exact waist radius')
        t = w0/a0
        D0 = t*(t-2)/(1-t)**2
        # Ns(0)=1 and s(0)=-a0 are the already proved Q.3 identity.
        last = dict(W=arb(0), D=D0, Y=arb(1), n=1-D0, a=a0, s=-a0, m=-a0+w0)
        ymin = arb(1)
        doc['stage'] = 'new-fixed-eta0-correlated-forward-integral'
        save_state()
        for index, row in enumerate(rows):
            left, right = map(Fraction, row['interval'])
            piece = int(row['candidate_piece'])
            doc['active_original_row'] = index
            doc['current_candidate_piece'] = piece
            doc['interface_consumed_for_active_row'] = False
            if index and piece != last_piece:
                require(piece == last_piece+1 and left == knots[piece], 'the next exact raw interface')
                wm = mean_value(coefficients[:, last_piece, :], knots[last_piece], left)
                wp = mean_value(coefficients[:, piece, :], knots[piece], left)
                a, s = last['a'], last['s']
                mm, mp = s+wm, s+wp
                require(mm.upper() < 0 and mp.upper() < 0, 'negative raw means at both true traces')
                jump = a*a*(wp-wm)*(2*s+wp+wm)/(mp*mp*mm*mm)
                A += jump
                Dplus = (W+a*a*wp*(2*s+wp)/(s*s*mp*mp)).intersection(last['D']+jump)
                nplus = a*a/(mp*mp)
                last = dict(W=W, D=Dplus, Y=last['Y'], n=nplus, a=a, s=s, m=mp)
                doc['completed_mean_interfaces'] += 1
                append_trace(dict(kind='signed_raw_mean_interface', common_row=index,
                    exact_r=str(left), piece=piece, W_is_continuous=True,
                    signed_D_jump=record(jump), propagated_atoms=record(A)))
            last_piece = piece
            doc['interface_consumed_for_active_row'] = True
            save_state()
            current = left
            while current < right:
                trial_right, depth = right, 0
                while True:
                    try:
                        model = local_model(target, coefficients[:, piece, :], knots[piece],
                                            current, trial_right)
                        outcome = advance(model, W, G, A)
                        break
                    except (ValueError, ZeroDivisionError) as exc:
                        require(depth < 18, 'unresolved local analytic chart after 18 bisections: '+str(exc))
                        trial_right = (current+trial_right)/2
                        depth += 1
                        doc['rematerialization']['local_disc_subdivisions'] += 1
                # Same intrinsic target at a shared trace; this is a comparison
                # of enclosures, never an imposed modification of the metric.
                outcome['begin']['a'].intersection(last['a'])
                outcome['begin']['s'].intersection(last['s'])
                W, G, A, last = outcome['W'], outcome['G'], outcome['A'], outcome['end']
                whole = outcome['whole']
                ymin = min(ymin, whole['Y'].lower()).lower()
                max_cauchy = max(max_cauchy, outcome['cauchy_D_error']).upper()
                if whole['Y'].lower() <= 0:
                    all_positive = False
                    if doc['first_unresolved_positivity'] is None:
                        doc['first_unresolved_positivity'] = dict(common_row=index,
                            subcell=doc['completed_subcells'], left=str(current), right=str(trial_right))
                if last['Y'].upper() < 0 and doc['certified_negative_Y_witness'] is None:
                    doc['certified_negative_Y_witness'] = dict(common_row=index, exact_r=str(trial_right),
                                                              Y=record(last['Y']))
                if whole['Y'].lower() > 0:
                    _, ku, _ = kernels(whole['n'], whole['Y'], whole['a'])
                    vsize = (-whole['m']).upper()+(64*whole['V'].upper()).sqrt().upper()
                    vbound = (vsize*modulus(whole['D'])*ku).upper()
                    vmax = max(vmax, vbound).upper()
                if last['Y'].lower() > 0:
                    ke, _, _ = kernels(last['n'], last['Y'], last['a'])
                    shift = -last['m']*last['D']*ke
                    if abs(shift).lower() > rat(Fraction(1, 10000)) and doc['certified_violation_witness'] is None:
                        doc['certified_violation_witness'] = dict(common_row=index, exact_r=str(trial_right),
                            absolute_mean_shift_lower=record(abs(shift).lower(), 'lower'))
                append_trace(dict(kind='new_correlated_closed_subcell', common_row=index,
                    exact_interval=[str(current), str(trial_right)], candidate_piece=piece,
                    intrinsic_part=model['part'], actual_scalar_germ=list(map(str, model['germ'])),
                    D=record(last['D']), W=record(W), G=record(G), Y=record(last['Y']),
                    whole_D=record(whole['D']), whole_Y=record(whole['Y']),
                    local_Cauchy_remainder=record(outcome['cauchy_D_error'], 'upper'),
                    same_r_carrier_materialized=True, primitive_tail=record(target.angular_tail_max, 'upper')))
                current = trial_right
                doc['completed_subcells'] += 1
                doc['current_exact_right'] = str(current)
                if current == right:
                    doc['completed_common_cells'] = index+1
                save_state()
            if (index+1) % 16 == 0:
                print(json.dumps(dict(stage=doc['stage'], completed_common_cells=index+1,
                    completed_subcells=doc['completed_subcells'], current_exact_right=str(right),
                    seconds=time.monotonic()-began)), flush=True)
        require(doc['completed_common_cells'] == ROWS and doc['completed_mean_interfaces'] == JOINS
                and doc['current_exact_right'] == '25/8', 'complete new whole-domain target')
        # Coverage is complete, but no completion flag is saved before gates.
        doc['stage'] = 'saved-whole-ball-gates'
        save_state()
        # The final decisions consume the object actually saved on disk.
        saved = parse(args.output.read_bytes())
        values = saved['complete_new_scalars']
        Ymin = unpack(values['Y_lower_over_completed_cells'])
        Vmax = unpack(values['v_difference_upper_on_positive_cells'])
        positive = ('true' if Ymin.lower() > 0 else
                    'false' if saved['certified_negative_Y_witness'] is not None else 'unknown')
        within = ('true' if positive == 'true' and Vmax.upper() <= rat(Fraction(1, 10000))
                  else 'false' if saved['certified_negative_Y_witness'] is not None
                  or saved['certified_violation_witness'] is not None else 'unknown')
        outer = 'unknown'
        if 'physical_Cmean_shift_at_current_right' in values:
            cshift = unpack(values['physical_Cmean_shift_at_current_right'])
            if cshift == 0:
                outer = 'true'
            elif not cshift.contains(0):
                outer = 'false'
        doc['strict_gates'] = dict(positive_mean_everywhere=positive,
            componentwise_moving_C0_within_1e4=within, outer_mean_unchanged=outer)
        doc['proved'] = positive == 'true' and within == 'true' and outer == 'true'
        doc['complete'] = True
        doc['stage'] = 'complete-new-target'
        snapshot()
    except Exception as exc:
        # A prospective subcell or join may already have changed in-memory
        # values when a later kernel, serialization or trace append fails.
        # Never serialize that mixture with the old cursor. The last atomic
        # on-disk checkpoint is the sole committed scientific state.
        committed = parse(args.output.read_bytes())
        committed_bytes = committed['private_trace']['bytes']
        if trace.exists():
            require(trace.stat().st_size >= committed_bytes,
                    'the complete accepted private trace prefix remains available')
            with trace.open('r+b') as stream:
                stream.truncate(committed_bytes)
                stream.flush()
                os.fsync(stream.fileno())
        committed['complete'] = False
        committed['proved'] = False
        committed['stage'] = 'failed_with_complete_prefix'
        committed['failure'] = dict(type=type(exc).__name__, message=str(exc),
            recovery='last atomically saved accepted checkpoint; uncommitted state discarded')
        committed['seconds'] = time.monotonic()-began
        atomic(args.output, encode(committed))
        raise


if __name__ == '__main__':
    main()
