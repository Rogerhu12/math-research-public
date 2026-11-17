#!/usr/bin/env python3
"""Compare primary-core spectra in explicitly defined inlet angle charts.

These are finite FFT diagnostics on zero-control lambda=1 primary cores, not
BVP solutions or uniform Fourier-tail certificates. Changing the primary
width changes the physical core. The normal-angle chart is only a diagnostic;
this script does not install it in a prefix or tail solver.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from diagnose_primary_flatten_width import Core, LIB


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def spectral_summary(vector, scalar, freq):
    v = np.linalg.norm(np.fft.fft(vector, axis=0) / len(freq), axis=1)
    k = np.abs(np.fft.fft(scalar) / len(freq))
    return {str(M): dict(vector_fft_l1_above_3Mplus1=float(v[freq > 3*M+1].sum()),
                         kappa_fft_l1_above_3M=float(k[freq > 3*M].sum()))
            for M in (8, 16, 24, 32)}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--primary-record', type=Path, required=True)
    p.add_argument('--warp-e', type=float)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    source = json.loads(a.primary_record.read_text())
    q = source['arguments']['q']; halfwidth = source['arguments']['halfwidth']
    N = source['arguments']['samples']; e = 8*q if a.warp_e is None else a.warp_e
    if not 0 <= e < 1:
        raise ValueError('The diagnostic sine chart must be increasing')
    psi = 2*np.pi*np.arange(N)/N
    freq = abs(np.rint(np.fft.fftfreq(N)*N).astype(int))
    rows = []
    for old in source['rows']:
        width = old['flatten_transition']
        core = Core(q, (), 3, halfwidth=halfwidth, transition=width, homotopy=1.,
                    center=np.pi/3, control_transition=.4, lock_fundamental=True,
                    bimodal_eta=0., arc_nodes=2048, coefficient_precision=80,
                    positivity_grid_max=32768)
        if core.local_flatten_beta != old['flatten_beta']:
            raise ValueError('Primary design differs from the recorded calculation')
        charts = {}
        for kind in ('material', 'sine', 'normal'):
            if kind == 'material':
                u = psi; du = np.ones_like(psi); ddu = np.zeros_like(psi)
                g = core.evaluate(u)
            elif kind == 'sine':
                u = psi - e*np.sin(3*psi)/3
                du = 1-e*np.cos(3*psi); ddu = 3*e*np.sin(3*psi)
                g = core.evaluate(u)
            else:
                u = core.arc(psi)
                jets = core.rho_material_jets(u)
                du = jets['rho']; ddu = jets['rho_phi']
                g = jets
            fpp = g['Ftt']*du[:, None]**2 + g['Ft']*ddu[:, None]
            z = np.exp(1j*u)
            bg = (1j*ddu-du**2)*z
            bg2 = np.stack((bg.real, bg.imag, np.zeros_like(bg.real)), axis=-1)
            pert = fpp-bg2
            charts[kind] = dict(
                minimum_chart_derivative=float(du.min()),
                maximum_chart_derivative=float(du.max()),
                sampled_arc_inverse_residual=float(abs(g['arc_residual']).max()),
                physical_Fuu_composed=spectral_summary(g['Ftt'], g['kappa'], freq),
                chart_Fpsipsi=spectral_summary(fpp, g['kappa'], freq),
                chart_perturbation_Fpsipsi=spectral_summary(pert, g['kappa'], freq))
        # Reproduce the previously saved material-u spectral scalar as an
        # interface check; this is not a second BVP or an independent theorem.
        difference = max(abs(charts['material']['physical_Fuu_composed'][str(M)]
                             ['vector_fft_l1_above_3Mplus1'] -
                             old['retained_state_cutoffs'][str(M)]
                             ['Fuu_vector_fft_l1_above_3Mplus1'])
                         for M in (8, 16, 24, 32))
        row = dict(flatten_transition=width, primary_scalar_reproduction_difference=difference,
                   charts=charts)
        rows.append(row)
        print(json.dumps(dict(width=width, reproduction_difference=difference,
              M16={k: v['chart_perturbation_Fpsipsi']['16'] for k,v in charts.items()})), flush=True)
    files = [Path(__file__), Path(__file__).with_name('diagnose_primary_flatten_width.py'),
             *sorted(LIB.glob('*.py'))]
    result = dict(scope=__doc__, command=sys.argv,
        primary_record=str(a.primary_record.resolve()), primary_record_sha256=sha(a.primary_record),
        source_sha256={str(f.resolve()): sha(f) for f in files},
        samples=N, q=q, halfwidth=halfwidth, warp_e=e,
        chart_definitions=dict(material='u=psi', sine='u=psi-e*sin(3*psi)/3',
                               normal='u=arc_primary(psi), du=rho_primary, ddu=rho_primary_phi'),
        derivative_formula='F_psipsi=F_uu*(du/dpsi)^2+F_u*d2u/dpsi2',
        perturbation_definition='F_psipsi - d2(exp(i*u(psi)))/dpsi2, radius a=1 at inlet',
        rows=rows,
        interpretation='Each row compares the same primary curve in three numerical coordinates. '
        'Only the sine chart has the form currently used at the prefix inlet; the exact normal chart '
        'has not been connected to any BVP. A sampled FFT tail in either chart is not a full-metric '
        'residual, a certified infinite tail, or evidence that a changed physical design solves the BVP.')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')


if __name__ == '__main__':
    main()
