#!/usr/bin/env python3
"""All-angle C1 remainder of literal finite G/T principal functions.

The actual raw core and physical parameters stay fixed.  A source FFT
only proposes binary64 Fourier coefficients; no FFT accuracy is assumed.
R36 true integrals validate point jets, and interval Taylor remainders
cover every cell of a reflection sector.  Exact D3 covariance covers the
remaining angles.  No full-prefix metric or surface geometry is computed.
"""
import argparse
import ctypes
from fractions import Fraction as F
import json
import math
from pathlib import Path
import sys
import time

import numpy as np

from m3_integral_prefix import load_integral_prefix, sha
from fast_integral_core_intervals import FastExactRawM3Core
import integral_core_intervals as ri
from certify_protected_arc_curvature_dual import decimal

UNIT = F(1, 2**53)
TINY = F(1, 2**1074)
_FENV = ctypes.CDLL(None)
_FENV.fegetround.restype = ctypes.c_int


def verify_arithmetic_environment():
    # FE_TONEAREST=0 is read from this Linux runtime's bits/fenv.h.
    # Both directions of the subnormal probe exclude FTZ and DAZ.
    assert sys.platform.startswith('linux')
    assert _FENV.fegetround() == 0
    normal = float.fromhex('0x1p-1022')
    half = float.fromhex('0x0.8p-1022')
    assert normal*.5 == half and half*2 == normal
    return dict(platform=sys.platform, fegetround=0, FE_TONEAREST=0,
                double_format=float.__getformat__('double'),
                gradual_underflow_output_probe=True, gradual_underflow_input_probe=True)


def vector_sum(*vectors):
    return tuple(ri.sum_intervals(v[j] for v in vectors) for j in range(2))


def vector_scale(v, c):
    return tuple(ri.mul(x, c) for x in v)


def angular_jets(psi, e):
    sn, cs = ri.signed_sincos(ri.scale(psi, 3))
    return (ri.sub(psi, ri.scale(sn, e/3)), ri.sub(ri.point(1), ri.scale(cs, e)),
            ri.scale(sn, 3*e), ri.scale(cs, 9*e), ri.scale(sn, -27*e))


def compose_position(g, t):
    _, a, b, c, d = t
    return (g[0], vector_scale(g[1], a),
            vector_sum(vector_scale(g[2], ri.power(a, 2)), vector_scale(g[1], b)),
            vector_sum(vector_scale(g[3], ri.power(a, 3)),
                       vector_scale(g[2], ri.scale(ri.mul(a, b), 3)), vector_scale(g[1], c)),
            vector_sum(vector_scale(g[4], ri.power(a, 4)),
                       vector_scale(g[3], ri.scale(ri.mul(ri.power(a, 2), b), 6)),
                       vector_scale(g[2], ri.add(ri.scale(ri.power(b, 2), 3), ri.scale(ri.mul(a, c), 4))),
                       vector_scale(g[1], d)))


def compose_tangent(g, t):
    _, a, b, c, _ = t
    return (g[1], vector_scale(g[2], a),
            vector_sum(vector_scale(g[3], ri.power(a, 2)), vector_scale(g[2], b)),
            vector_sum(vector_scale(g[4], ri.power(a, 3)),
                       vector_scale(g[3], ri.scale(ri.mul(a, b), 3)), vector_scale(g[2], c)))


def composition_remainder_bounds(K, e, tangent=False):
    a, b, c, d, f = 1+abs(e), 3*abs(e), 9*abs(e), 27*abs(e), 81*abs(e)
    if tangent:
        return K[5]*a**4+6*K[4]*a*a*b+K[3]*(3*b*b+4*a*c)+K[2]*d
    return (K[5]*a**5+10*K[4]*a**3*b+K[3]*(15*a*b*b+10*a*a*c)
            +K[2]*(10*b*c+5*a*d)+f)


class FiniteFourier:
    """Literal coefficients; a proved IEEE roundoff bound, no libm calls."""
    def __init__(self, modes, coefficients, derivative):
        assert np.dtype(float).itemsize == 8 and float.__getformat__('double').startswith('IEEE')
        self.modes = np.asarray(modes, int)
        self.co = np.asarray(coefficients, complex)
        assert np.all(np.isfinite(self.co))
        self.order = derivative
        self.arithmetic_checks = 0
        verify_arithmetic_environment()
        self.maximum = int(max(abs(self.modes)))
        assert self.maximum <= 4096
        self.norms = [sum((F.from_float(abs(float(c.real)))+F.from_float(abs(float(c.imag))))*abs(int(k))**r
                          for c, k in zip(self.co, self.modes)) for r in range(derivative+2)]
        assert max(self.norms) < F(10)**100
        self.weighted = [self.co*np.asarray([int(k)**r for k in self.modes], float)*(1j**r)
                         for r in range(derivative+1)]

    def evaluate(self, psi):
        assert _FENV.fegetround() == 0
        self.arithmetic_checks += 1
        sn, cs = ri.signed_sincos(psi)
        z = complex(float((cs[0]+cs[1])/2), float((sn[0]+sn[1])/2))
        delta = (ri.magnitude(ri.sub(cs, ri.point(F.from_float(z.real))))
                 +ri.magnitude(ri.sub(sn, ri.point(F.from_float(z.imag)))))
        assert delta < 4*UNIT
        step = delta+32*UNIT
        assert self.maximum*step < F(1, 10**6)
        powers = [1.+0.j]
        for _ in range(self.maximum):
            powers.append(powers[-1]*z)
        powers = np.asarray(powers)
        values = powers[abs(self.modes)].copy()
        negative = self.modes < 0
        values[negative] = values[negative].conjugate()
        result = []
        count = len(self.modes)
        for r, coefficient in enumerate(self.weighted):
            v = complex(np.sum(coefficient*values))
            # Each complex power contributes <= |k|*(delta+32u).
            # Coefficient weights, complex products and at most n-1
            # additions are covered by 32u*(n+4)*l1.  The separate tiny
            # allowance permits gradual underflow; there is no libm here.
            error = step*self.norms[r+1]+32*UNIT*(count+4)*self.norms[r]
            error += 64*TINY*(self.maximum+count+1)*(self.maximum**r+1)
            result.append(tuple(ri.add(ri.point(F.from_float(c)), (-error, error)) for c in (v.real, v.imag)))
        assert _FENV.fegetround() == 0
        self.arithmetic_checks += 1
        return tuple(result)


def difference_norm(a, b):
    return sum(ri.magnitude(ri.sub(x, y)) for x, y in zip(a, b))


def cell_bounds(actual, principal, radius, derivative_remainder):
    residual = [difference_norm(a, b) for a, b in zip(actual, principal)]
    order = len(residual)
    value = sum(residual[j]*radius**j/math.factorial(j) for j in range(order))
    value += derivative_remainder*radius**order/math.factorial(order)
    first = sum(residual[j]*radius**(j-1)/math.factorial(j-1) for j in range(1, order))
    first += derivative_remainder*radius**(order-1)/math.factorial(order-1)
    return value, first


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'short-bridge', 'checkpoint', 'port', 'data', 'prefix-audit', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--panels', type=int, default=1024)
    p.add_argument('--proposal-angular', type=int, default=6144)
    p.add_argument('--principal-cutoff', type=int, default=512)
    args = p.parse_args()
    began = time.monotonic()
    initial_arithmetic_environment = verify_arithmetic_environment()
    audit = json.loads(args.prefix_audit.read_text())
    assert sha(args.data) == audit['packet_sha256']
    assert sha(args.checkpoint) == audit['source']['checkpoint_sha256']
    data = np.load(args.data)
    record, obj, flow, _, _ = load_integral_prefix(args.source_topic, args.short_bridge,
                                                args.checkpoint, args.port, audit['angular_samples'])
    core = obj._core
    exact = FastExactRawM3Core(core, obj.integral_reader_provenance)
    er = F.from_float(float(flow.warp_e))
    ec = F.from_float(float(data['phase_jets'][0, 0, 0]))
    assert 0 <= er < 1 and 0 <= ec < 1 and args.panels >= 8
    N = args.proposal_angular
    assert N % 3 == 0 and N > 4*args.principal_cutoff
    psi = 2*np.pi*np.arange(N)/N
    G = core.evaluate(psi-float(er)*np.sin(3*psi)/3)['F']
    T = core.evaluate(psi-float(ec)*np.sin(3*psi)/3)['Ft']
    frequencies = np.rint(np.fft.fftfreq(N)*N).astype(int)
    mask = (frequencies % 3 == 1) & (abs(frequencies) <= args.principal_cutoff)
    modes = frequencies[mask]
    cg = (np.fft.fft(G[:, 0]+1j*G[:, 1])/N)[mask].real.astype(complex)
    ct = 1j*(np.fft.fft(T[:, 0]+1j*T[:, 1])/N)[mask].imag
    # This literal projection builds exact D3 covariance into the proposal.
    assert np.all(cg.imag == 0) and np.all(ct.real == 0)
    principal_g, principal_t = FiniteFourier(modes, cg, 4), FiniteFourier(modes, ct, 3)
    K = exact.material_derivative_bounds()
    remainder_g = composition_remainder_bounds(K, er)+principal_g.norms[5]
    remainder_t = composition_remainder_bounds(K, ec, tangent=True)+principal_t.norms[4]
    pi = ri.pi_interval()
    radius = pi[1]/(6*args.panels)
    centers = [ri.scale(pi, F(2*j+1, 6*args.panels)) for j in range(args.panels)]
    center_float = np.array([float((v[0]+v[1])/2) for v in centers])
    proposals = core.evaluate(center_float-float(er)*np.sin(3*center_float)/3)['phi']
    maxima = [F(0)]*4
    maximum_cells = [None]*4
    for j, (psi_center, phi) in enumerate(zip(centers, proposals)):
        rjets, cjets = angular_jets(psi_center, er), angular_jets(psi_center, ec)
        normal = exact.point_normal_through_four(float(phi))
        material_g = exact.material_intervals(normal, rjets[0])
        material_t = exact.material_intervals(normal, cjets[0])
        aj_g, aj_t = compose_position(material_g, rjets), compose_tangent(material_t, cjets)
        bg = cell_bounds(aj_g, principal_g.evaluate(psi_center), radius, remainder_g)
        bt = cell_bounds(aj_t, principal_t.evaluate(psi_center), radius, remainder_t)
        for k, bound in enumerate(bg+bt):
            if bound > maxima[k]:
                maxima[k], maximum_cells[k] = bound, j
        if (j+1) % 64 == 0:
            print(json.dumps(dict(event='angular_cells', completed=j+1, total=args.panels,
                                  seconds=time.monotonic()-began,
                                  bounds_so_far=[decimal(v, True, 18) for v in maxima])), flush=True)
    packet = args.out.with_name(args.out.stem+'-principal.npz')
    packet.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(packet, modes=modes, position_coefficients=cg, tangent_coefficients=ct,
                        reference_phase=np.array(float(er)), center_phase=np.array(float(ec)))
    here = Path(__file__).resolve().parent
    paths = [Path(__file__), here/'fast_integral_core_intervals.py', here/'integral_core_intervals.py',
             here/'m3_integral_prefix.py', here/'certify_protected_arc_curvature_dual.py',
             here/'certify_m3_large_circle_window.py']
    result = dict(
        scope=__doc__, command=sys.argv, sources_sha256={str(f): sha(f) for f in paths},
        checkpoint_sha256=sha(args.checkpoint), packet_input_sha256=sha(args.data),
        source_protocol=obj.integral_reader_provenance,
        physical_parameters_or_map_changed=False, bvp_solves=0,
        reference_phase_exact=str(er), center_phase_exact=str(ec),
        mathematical_angle_coverage='All real psi by exact D3 covariance from the complete sector [0,pi/3]',
        panels=args.panels, cell_radius_upper=decimal(radius, True),
        proposal_angular_samples=N, principal_frequency_cutoff=args.principal_cutoff,
        literal_coefficient_count=len(modes), proposal_fft_accuracy_assumed=False,
        principal_symmetry=dict(frequencies_mod_three=1, position_coefficients_real=True, tangent_coefficients_pure_imaginary=True),
        uniform_true_remainder_bounds={key: decimal(v, True) for key, v in zip(
            ('G_value', 'G_first_psi', 'T_value', 'T_first_psi'), maxima)},
        maximum_bound_cells=maximum_cells,
        derivative_remainder_bounds=dict(G_fifth=decimal(remainder_g, True), T_fourth=decimal(remainder_t, True)),
        global_material_derivative_bounds={str(j): decimal(K[j], True) for j in range(1, 6)},
        principal_norms=dict(position=[decimal(v, True) for v in principal_g.norms],
                             tangent=[decimal(v, True) for v in principal_t.norms]),
        floating_point_proof=dict(arithmetic='IEEE binary64 round-to-nearest with gradual underflow',
            unit_roundoff=str(UNIT), minimum_positive=str(TINY),
            power_error='|k|*(certified_base_complex_error+32u)',
            weighted_sum_error='32u*(number_of_modes+4)*coefficient_derivative_l1 plus explicit gradual-underflow allowance',
            no_libm_in_principal_evaluation=True,
            initial_environment=initial_arithmetic_environment,
            final_environment=verify_arithmetic_environment(),
            per_evaluation_mode_checks=principal_g.arithmetic_checks+principal_t.arithmetic_checks),
        principal_output=dict(path=str(packet), sha256=sha(packet)),
        continuous_core_C1_remainder_certified=True, full_prefix_metric_or_closed_geometry_certified=False,
        seconds=time.monotonic()-began)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(event='certified', bounds=result['uniform_true_remainder_bounds'],
                          seconds=result['seconds'], principal_sha256=sha(packet))), flush=True)


if __name__ == '__main__':
    main()
