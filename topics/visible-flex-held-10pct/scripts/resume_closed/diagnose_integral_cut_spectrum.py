#!/usr/bin/env python3
"""Finite FFT diagnostic at one already exported prefix cut, without rescanning.

This uses the existing Cartesian two-jet packet.  The reference and center
lifts vanish at this cut and no tail lift was applied in the input export.
The cut is a specified material slice, not the unknown global metric maximum.
Scalar modes above the state cutoff 3M are a diagnostic partition, not a
claim that those metric coefficients were omitted from the original audit.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('data', 'prefix-audit', 'checkpoint', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--angular', type=int, default=256)
    p.add_argument('--amplitude-floor', type=float, default=1e-14)
    args = p.parse_args()
    audit = json.loads(args.prefix_audit.read_text())
    cp = json.load(gzip.open(args.checkpoint, 'rt'))
    assert audit['packet_sha256'] == sha(args.data)
    assert audit['source']['checkpoint_sha256'] == sha(args.checkpoint)
    assert audit['cut_numerical_identity'] is None, 'The input contains another endpoint lift'
    data = np.load(args.data)
    assert np.all(data['reference_radial_jets'][:, 0, -1] == 0)
    assert np.all(data['phase_jets'][:, 0, -1] == 0)
    pm, hm = data['planar_modes'], data['height_modes']
    assert np.all((pm-1) % 3 == 0) and np.all(hm % 3 == 0)
    C = data['jets'][:, :, -1]
    P, M, N = len(pm), cp['config']['modes'], args.angular
    psi = 2*np.pi*np.arange(N)/N
    ep, phase = np.exp(1j*psi[:, None]*pm), psi[:, None]*hm
    planar_s = ep@C[1, :P]
    planar_p = ep@(1j*pm*C[0, :P])
    zs = np.cos(phase)@C[1, P:]
    zp = -np.sin(phase)@(hm*C[0, P:])
    Xs = np.c_[planar_s.real, planar_s.imag, zs]
    Xp = np.c_[planar_p.real, planar_p.imag, zp]
    radius = float(cp['physical_tail_parameters']['rCut'])
    errors = np.stack((np.sum(Xs*Xs, axis=1)-1,
                       np.sum(Xs*Xp, axis=1)/radius,
                       np.sum(Xp*Xp, axis=1)/radius**2-1), axis=1)
    spectrum = np.fft.fft(errors, axis=0)/N
    frequencies = np.rint(np.fft.fftfreq(N)*N).astype(int)
    represented = (frequencies % 3 == 0) & (abs(frequencies) <= 3*M)
    omitted = (frequencies % 3 == 0) & (abs(frequencies) > 3*M)
    forbidden = frequencies % 3 != 0
    rows = []
    for j, name in enumerate(('E_minus_1', 'F_over_a', 'G_over_a2_minus_1')):
        amplitudes = abs(spectrum[:, j])
        ordered = np.argsort(amplitudes)[::-1]
        relevant = np.where(omitted & (amplitudes > args.amplitude_floor))[0]
        strongest = int(np.argmax(np.where(omitted, amplitudes, -1.)))
        rows.append(dict(
            component=name, material_s=float(data['knots'][-1]),
            total_finite_fft_l1=float(amplitudes.sum()),
            represented_band_l1=float(amplitudes[represented].sum()),
            omitted_band_l1=float(amplitudes[omitted].sum()),
            non_threefold_bins_l1=float(amplitudes[forbidden].sum()),
            maximum_omitted_abs_frequency_above_floor=int(max(abs(frequencies[relevant]))) if len(relevant) else None,
            dominant_omitted_frequency=int(frequencies[strongest]),
            dominant_omitted_amplitude=float(amplitudes[strongest]),
            largest_bins=[dict(frequency=int(frequencies[k]), amplitude=float(amplitudes[k]),
                               real=float(spectrum[k, j].real), imaginary=float(spectrum[k, j].imag))
                          for k in ordered[:12]]))
    result = dict(
        scope=__doc__, command=sys.argv, source_sha256=sha(__file__),
        inputs={str(f.resolve()): sha(f) for f in (args.data, args.prefix_audit, args.checkpoint)},
        core_kind=cp['config']['core_kind'], control_path=cp.get('core_control_path'),
        q=cp['actual_primary_amplitude'], homotopy=cp['core_round_settings']['homotopy'],
        state_modes=M, state_scalar_cutoff=3*M, angular_samples=N,
        amplitude_floor=args.amplitude_floor, reference_radius=radius,
        reference_scope='Nominal physical rCut, unit source radial metric, identity material-angle cut; no true-atlas error certificate',
        evaluated_radial_slices=1, global_worst_radial_slice_claimed=False,
        original_full_domain_metric=audit['numerical_profile_metric_fft_component_l1'],
        components=rows, original_map_or_parameters_changed=False,
        limits='Finite DFT only. This named cut slice cannot establish the dominant component or frequency at the global metric maximum.')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('evaluated_radial_slices', 'components')}), flush=True)


if __name__ == '__main__':
    main()
