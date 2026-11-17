#!/usr/bin/env python3
"""Outward interval sums for the fixed m3 small-cut rotational background.

The first N original nine-piece cells use their frozen binary calibration
constants. Complete interval ranges (not point quadrature errors) enclose A,
B,wA,wB. All remaining cells use a proved geometric-series majorant. The
exact positive radial normalization is (cut-r_deep-int A)/int B.

This proves background bounds only, not the nonrotational finite-map metric.
"""
from pathlib import Path
from fractions import Fraction
import argparse, hashlib, json, math, time
import mpmath as mp

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--input', type=Path, required=True)
p.add_argument('--out', type=Path, required=True)
p.add_argument('--cells', type=int, default=16)
p.add_argument('--panels', type=int, default=64)
a = p.parse_args()
data = json.loads(a.input.read_text())
cfg = data['parameters']
N = a.cells
assert N == 16 and cfg['protectCell'] == 160
assert a.panels > 0 and (a.panels & (a.panels-1)) == 0
assert cfg['orientation'] == 1 and cfg['curvatureBound'] == 8
assert cfg['prefixEnd'] == 15 and cfg['rejoinR20At'] is None
assert not cfg.get('flatOuterThroughCell', False)
assert cfg['a'] == 2.75 and cfg['etaPower'] == 1.5
assert all(c['lengthScale'] == 1 for c in data['cells'])
assert all(.5 <= c['calibrationAlpha'] <= 2 for c in data['cells'])
assert all(v == 0 for v in cfg['valleyControls'][N:])
assert all(all(v == 1 for v in z) for z in cfg.get('warpWeightLevels', [])[1:])
assert len(cfg.get('pulseCaps', [])) <= 1 and len(cfg.get('valleyCaps', [])) <= 1
mp.mp.dps = 90
iv = mp.iv
iv.dps = 60

def lower(z): return mp.make_mpf(z._mpi_[0])
def upper(z): return mp.make_mpf(z._mpi_[1])
def interval(lo, hi):
    assert lo <= hi
    return iv.mpf([lo, hi])
def q(x):
    f = Fraction(x) if isinstance(x, int) else Fraction.from_float(float(x))
    return iv.mpf(f.numerator) / f.denominator
def clamp(z, lo, hi):
    l, h = max(lower(z), mp.mpf(lo)), min(upper(z), mp.mpf(hi))
    if l > h: raise ArithmeticError('empty proved intersection')
    return interval(l, h)
def hull(xs): return interval(min(lower(z) for z in xs), max(upper(z) for z in xs))
def point(x): return iv.mpf(x)
def poly5(x): return x*x*x*(10+x*(-15+6*x))
def smooth(x):
    # S5'=30*x^2*(1-x)^2 >= 0 on [0,1].
    return clamp(hull([poly5(point(lower(x))),poly5(point(upper(x)))]),0,1)
def dsmooth(x):
    vals=[30*t*t*(1-t)*(1-t)for t in [point(lower(x)),point(upper(x))]]
    if lower(x)<=mp.mpf('.5')<=upper(x):vals.append(iv.mpf(15)/8)
    return hull(vals)
def capped(z, dz, c, dc):
    L = q(cfg['capTransition'])
    rel = z-c
    zz, dd = [], []
    if lower(rel) <= -lower(L):
        zz.append(interval(lower(z), min(upper(z), upper(c-L))))
        dd.append(dz)
    if upper(rel) >= lower(L):
        zz.append(c); dd.append(dc)
    if upper(rel) >= -upper(L) and lower(rel) <= upper(L):
        t = clamp((rel+L)/(2*L), 0, 1)
        # Integral of 1 minus the seventh-degree smoothstep.
        def primitive(v):return v-v**5*(7+v*(-14+v*(10-q(2.5)*v)))
        # I'=1-S7 >=0, and S7'=140*t^3*(1-t)^3 >=0.
        I = clamp(hull([primitive(point(lower(t))),primitive(point(upper(t)))]),0,.5)
        zz.append(c-L+2*L*I)
        def dcap(v):return 1-v**4*(35+v*(-84+v*(70-20*v)))
        d = clamp(hull([dcap(point(lower(t))),dcap(point(upper(t)))]),0,1)
        dd.append(d*dz+(1-d)*dc)
    # The smooth cap is nondecreasing and never exceeds its local cap.
    outz = hull(zz)
    outz = interval(lower(outz), min(upper(outz), upper(c)))
    return outz, hull(dd)

delta0, c0 = q(cfg['delta0']), q(cfg['etaRatioAtN0'])
eta0 = delta0*c0
aa = q(cfg['rCuff'])
cut, wcut = q(cfg['rCut']), q(cfg['wCut'])
ae = q(cfg['a'])
sqrt12 = iv.sqrt(12)
two = iv.mpf(2)
eta_ratio = two**(-q(1.5))
Y = 6*delta0+6*eta0/(1-eta_ratio)
oldcut = aa*iv.exp(Y/sqrt12)
assert lower(aa) > mp.mpf(1)/25
assert upper(wcut) < mp.mpf(1)/10
assert lower(delta0) >= mp.mpf(1)/200 and upper(delta0) <= mp.mpf(1)/160
assert lower(c0) >= mp.mpf(1)/25 and upper(c0) <= mp.mpf(1)/16
rows = []
total = [iv.mpf(0) for _ in range(4)]
started = time.monotonic()
for n in range(N):
    cell = data['cells'][n]
    delta = delta0*two**(-n)
    c = c0*two**(-iv.mpf(n)/2)
    after = 3*delta0*two**(-n)+6*eta0*two**(-q(1.5)*(n+1))/(1-eta_ratio)
    alpha_cell = q(cell['calibrationAlpha'])
    ld = iv.ln(delta)
    values = [ld, iv.ln(q(cell['R'])), 2*ld-iv.ln(alpha_cell),
              iv.mpf(0), ld+ae*iv.ln(2)]
    beta = q(cfg['valleyControls'][n])
    levels = [q(cfg['slopeCap'])]*5
    if n < len(cfg.get('pulseCaps', [])):
        levels[1] = q(cfg['pulseCaps'][n][0]); levels[3] = q(cfg['pulseCaps'][n][1])
    if n < len(cfg.get('valleyCaps', [])): levels[2] = q(cfg['valleyCaps'][n])
    weights = cfg.get('warpWeightLevels', [])
    weights = weights[n] if n < len(weights) else [1]*5
    cell_sum = [iv.mpf(0) for _ in range(4)]
    offset = iv.mpf(0)
    # Indices of the five plateau levels; odd pieces join adjacent levels.
    for j in range(9):
        transition = j % 2 == 1
        k = (j-1)//2 if transition else j//2
        length = delta*(c if transition or j in (0,8) else 1)
        for panel in range(a.panels):
            x = interval(mp.mpf(panel)/a.panels, mp.mpf(panel+1)/a.panels)
            S, Sp = smooth(x), dsmooth(x)
            logp = values[k]+(values[k+1]-values[k])*S if transition else values[k]
            dlogp = (values[k+1]-values[k])*Sp if transition else iv.mpf(0)
            z = iv.ln(wcut)-ae*iv.ln(2*delta0)+(ae-1)*ld+logp+7*(Y-after-offset-length*x)/sqrt12
            dz = dlogp-7*length/sqrt12
            if j == 3: z += beta*S; dz += beta*Sp
            if j == 4: z += beta
            if j == 5: z += beta*(1-S); dz -= beta*Sp
            rawz, rawdz = z, dz
            caplog = iv.ln(levels[k])
            capd = iv.mpf(0)
            if transition:
                dcap = iv.ln(levels[k+1]/levels[k])
                caplog += dcap*S; capd = dcap*Sp
            z, dz = capped(z, dz, caplog, capd)
            if n == 0 and j == 8: z, dz = rawz, rawdz
            if n == 0 and j == 7:
                z, dz = rawz+(1-S)*(z-rawz), rawdz-Sp*(z-rawz)+(1-S)*(dz-rawdz)
            r_old = aa*iv.exp((after+offset+length*x)/sqrt12)
            rx = r_old*length/sqrt12
            chi, j0 = iv.mpf(1), iv.mpf(1)
            if n == 0 and j == 8:
                chi = 1-S; j0 = 1+(cut/oldcut-1)*S
            weight = q(weights[k])
            if transition: weight *= iv.exp(iv.ln(q(weights[k+1])/q(weights[k]))*S)
            w = iv.exp(z); E = 1+w*w
            A = rx*j0*(1-chi)+chi*abs(w*dz)/(8*E*iv.sqrt(E))
            B = chi*rx/E*weight
            vals = [A,B,w*A,w*B]
            for i,v in enumerate(vals): cell_sum[i] += v/a.panels
        offset += length
    for i in range(4): total[i] += cell_sum[i]
    rows.append(cell_sum)
    print(json.dumps(dict(cell=n,A_upper=float(upper(cell_sum[0])),cumulative_A_upper=float(upper(total[0])))),flush=True)

# n>=16: R=64, no valley edits, no non-unit weights; cap only decreases w
# and its total variation. W_n <= 256*2^(-7n/4), H_n <= 17+7n/5.
W = iv.mpf(256)*two**(-iv.mpf(7*N)/4)
HN = 17+iv.mpf(7*N)/5
qq = iv.mpf(3)/10                 # 2^(-7/4) < 3/10
TV = W*((4*HN+1)/(1-qq)+(iv.mpf(28)/5)*qq/(1-qq)**2)
Yrest = 6*delta0*two**(-N)+6*eta0*two**(-q(1.5)*N)/(1-eta_ratio)
radial_rest = aa*iv.expm1(Yrest/sqrt12)
Arest = TV/8+radial_rest
Brest = radial_rest
remainder = [Arest,Brest,W*Arest,W*Brest]
complete = [interval(lower(z),upper(z+r)) for z,r in zip(total,remainder)]
Y160 = 6*delta0*two**(-160)+6*eta0*two**(-240)/(1-eta_ratio)
rdeep = aa*iv.exp(Y160/sqrt12)
target = cut-rdeep
normalization = (target-complete[0])/complete[1]
assert lower(normalization)>0, 'No positive exact normalization certified'
deep_height = iv.mpf(256)*two**(-280)*aa*iv.expm1(Y160/sqrt12)
height = complete[2]+normalization*complete[3]+interval(0,upper(deep_height))
inner_integrals = [sum((row[i] for row in rows[1:]),iv.mpf(0)) for i in range(4)]
inner_complete = [interval(lower(z),upper(z+r)) for z,r in zip(inner_integrals,remainder)]
r1 = rdeep+inner_complete[0]+normalization*inner_complete[1]

def bound(z):
    lo = math.nextafter(float(lower(z)), -math.inf)
    hi = math.nextafter(float(upper(z)), math.inf)
    return dict(lower=lo,upper=hi,lower_exact=str(Fraction.from_float(lo)),upper_exact=str(Fraction.from_float(hi)))
result = dict(scope=__doc__,input_sha256=hashlib.sha256(a.input.read_bytes()).hexdigest(),
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              frozen_calibration_alpha_range=[data['calibrationAlphaMin'],data['calibrationAlphaMax']],
              cells=N,panels_per_piece=a.panels,interval_decimal_precision=iv.dps,
              complete_integrals={k:bound(v)for k,v in zip(['A','B','AH','BH'],complete)},
              positive_exact_normalization=bound(normalization),
              exact_background_height=bound(height),
              cell0_inner_radius=bound(r1),
              analytic_deep_remainder={k:bound(v)for k,v in zip(['A','B','AH','BH'],remainder)},
              seconds=time.monotonic()-started,
              infinite_nonlinear_solution_proved=False,
              nonrotational_geometry_certified=False)
a.out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(alpha=result['positive_exact_normalization'],height=result['exact_background_height'],seconds=result['seconds'])),flush=True)
