#!/usr/bin/env python3
"""Locate componentwise finite-FFT metric peaks of one unchanged exported map.

One radial pass records E-1, F/a and G/a^2-1 separately, with their in/out
state-cutoff l1 masses.  This is a new location/spectrum diagnostic, not a
nonlinear solve, continuous metric bound or closed-geometry certificate.
The original accepted core and every exported shared coefficient are checked.
"""
import argparse
import json
from pathlib import Path
import sys
import time

from m3_integral_prefix import load_integral_prefix, M3IntegralCartesianPrefix, CLOSED, sha
import numpy as np
sys.path.insert(0, str(CLOSED))
from phase_angle_chart import PhaseAngleChart

COMPONENTS = ('E_minus_1', 'F_over_a', 'G_over_a2_minus_1')


def argument(record, key, default):
    command = record['argv']
    return command[command.index(key)+1] if key in command else default


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('data', 'prefix-audit', 'checkpoint', 'source-topic', 'short-bridge', 'port', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--angular', type=int, default=768)
    p.add_argument('--amplitude-floor', type=float, default=1e-14)
    args = p.parse_args()
    began = time.monotonic()
    audit = json.loads(args.prefix_audit.read_text())
    assert audit['packet_sha256'] == sha(args.data)
    assert audit['source']['checkpoint_sha256'] == sha(args.checkpoint)
    assert audit['cut_numerical_identity'] is None
    data = np.load(args.data)
    record, obj, flow, sol, _ = load_integral_prefix(
        args.source_topic, args.short_bridge, args.checkpoint, args.port, audit['angular_samples'])
    width = float(argument(audit, '--center-width', .04))
    model = M3IntegralCartesianPrefix(obj, flow, sol, width, (len(data['planar_modes'])-1)//2)
    phase = PhaseAngleChart(model)
    checks = dict(
        knots=np.array_equal(model.rep.x, data['knots']),
        cartesian_jets=np.array_equal(model.rep.jets, data['jets']),
        reference_radial_jets=np.array_equal(model.lift_rep.jets, data['reference_radial_jets']),
        reference_projection=np.array_equal(model.reference_initial, data['reference_initial_projection']),
        phase_jets=np.array_equal(phase.rep.jets, data['phase_jets']),
        mean_knots=np.array_equal(sol.mean_spline.x, data['mean_knots']),
        mean_jets=np.array_equal(sol.mean_spline.jets, data['mean_jets']))
    assert all(checks.values()), checks
    M, N = obj.M, args.angular
    assert N % 3 == 0 and N > 12*M, 'Use a full C3-compatible finite FFT grid'
    psi = 2*np.pi*np.arange(N)/N
    frequencies = np.rint(np.fft.fftfreq(N)*N).astype(int)
    low = (frequencies % 3 == 0) & (abs(frequencies) <= 3*M)
    high = (frequencies % 3 == 0) & (abs(frequencies) > 3*M)
    other = frequencies % 3 != 0
    s = np.unique(np.r_[data['knots'], (data['knots'][:-1]+data['knots'][1:])/2,
                        np.linspace(0, flow.end, 65), np.linspace(0, width, 65)])

    def spectrum(points):
        X, Xs, _, Xp, _, _ = model.evaluate(points, psi)
        _, rho, _, ts, _, _ = phase.angular(points[:, None], psi[None, :])
        Fs = Xs-ts[:, :, None]*Xp/rho[:, :, None]
        Ft = Xp/rho[:, :, None]
        radius = flow.profile(points)[0]
        residual = np.stack((np.sum(Fs*Fs, axis=2)-1,
                             np.sum(Fs*Ft, axis=2)/radius[:, None],
                             np.sum(Ft*Ft, axis=2)/radius[:, None]**2-1), axis=2)
        return np.fft.fft(residual, axis=1)/N

    scalars = np.empty((len(s), 4, 3))
    for start in range(0, len(s), 16):
        part = slice(start, start+16)
        amplitudes = abs(spectrum(s[part]))
        for j, mask in enumerate((np.ones(N, bool), low, high, other)):
            scalars[part, j, :] = amplitudes[:, mask, :].sum(axis=1)
    peaks, selected = [], set()
    for j, name in enumerate(COMPONENTS):
        positions = np.argmax(scalars[:, :, j], axis=0)
        peak = int(positions[0])
        neighbors = list(range(max(0, peak-1), min(len(s), peak+2)))
        selected.update(neighbors)
        peaks.append(dict(component=name, peak_index=peak, peak_s=float(s[peak]),
                          total_l1=float(scalars[peak, 0, j]),
                          in_band_l1_at_peak=float(scalars[peak, 1, j]),
                          out_band_l1_at_peak=float(scalars[peak, 2, j]),
                          non_threefold_l1_at_peak=float(scalars[peak, 3, j]),
                          in_band_maximum=dict(s=float(s[positions[1]]), l1=float(scalars[positions[1], 1, j])),
                          out_band_maximum=dict(s=float(s[positions[2]]), l1=float(scalars[positions[2], 2, j])),
                          neighbor_indices=neighbors))
    selected = sorted(selected)
    detail = spectrum(s[selected])
    index = {original: row for row, original in enumerate(selected)}

    def summarize(values):
        amplitudes = abs(values)
        ordering = np.argsort(amplitudes)[::-1]
        visible = np.flatnonzero(high & (amplitudes > args.amplitude_floor))
        omitted_peak = int(np.argmax(np.where(high, amplitudes, -1.)))
        return dict(
            dominant_frequency=int(frequencies[ordering[0]]),
            dominant_amplitude=float(amplitudes[ordering[0]]),
            dominant_omitted_frequency=int(frequencies[omitted_peak]),
            dominant_omitted_amplitude=float(amplitudes[omitted_peak]),
            maximum_omitted_abs_frequency_above_floor=int(max(abs(frequencies[visible]))) if len(visible) else None,
            largest_bins=[dict(frequency=int(frequencies[k]), amplitude=float(amplitudes[k]),
                               real=float(values[k].real), imaginary=float(values[k].imag))
                          for k in ordering[:12]])

    for j, peak in enumerate(peaks):
        peak['spectrum_at_peak'] = summarize(detail[index[peak['peak_index']], :, j])
        peak['nearby_slices'] = [dict(s=float(s[k]), total_l1=float(scalars[k, 0, j]),
                                     in_band_l1=float(scalars[k, 1, j]),
                                     out_band_l1=float(scalars[k, 2, j]),
                                     spectrum=summarize(detail[index[k], :, j]))
                                 for k in peak['neighbor_indices']]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    scalar_file = args.out.with_name(args.out.stem+'-radial-scalars.npz')
    np.savez_compressed(scalar_file, material_s=s, component_band_l1=scalars)
    result = dict(
        scope=__doc__, command=sys.argv, source_sha256=sha(__file__),
        inputs={str(f.resolve()): sha(f) for f in (args.data, args.prefix_audit, args.checkpoint,
                                                 args.short_bridge, args.port)},
        reader_sha256=sha(Path(__file__).with_name('m3_integral_prefix.py')),
        original_map_byte_identity_checks=checks, source_protocol=obj.integral_reader_provenance,
        state_modes=M, core_projection_order_J=len(model.core.corrections)+1,
        state_scalar_cutoff=3*M, angular_samples=N, radial_samples=len(s),
        full_radial_passes=1, nearby_slice_reevaluations=len(selected),
        radial_selection='Every shared node and midpoint, 65 uniform domain points and 65 center-strip points',
        amplitude_floor=args.amplitude_floor, components=peaks,
        scalar_output=dict(path=str(scalar_file), sha256=sha(scalar_file)),
        bvp_solves=0, original_map_or_parameters_changed=False,
        continuous_or_true_integral_metric_claimed=False,
        limitations='A finite radial/FFT location diagnostic. Band membership alone does not establish truncation causality, and increasing M may alter old in-band coefficients.',
        seconds=time.monotonic()-began)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(event='located', seconds=result['seconds'],
                          components=[{k: row[k] for k in ('component', 'peak_s', 'total_l1',
                                                            'in_band_l1_at_peak', 'out_band_l1_at_peak')}
                                      | dict(spectrum=row['spectrum_at_peak']) for row in peaks])), flush=True)


if __name__ == '__main__':
    main()
