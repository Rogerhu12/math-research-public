#!/usr/bin/env python3
"""Resolve an actual radial-geometry curvature peak into literal height jets.

The reported geometry is not recomputed or replaced by a Darboux prediction.
This evaluates the same height candidate at its recorded curvature sample and
compares its actual h_rr with the full, unprojected Darboux right-hand side.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


def main(args):
    report_raw = args.report.read_bytes()
    report = json.loads(report_raw)
    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    for path, key in ((args.input, 'input_sha256'),
                      (args.background, 'background_sha256'),
                      (args.height_reader, 'height_reader_sha256')):
        if digest(path) != report[key]:
            raise ValueError(f'{key} does not match the geometry report')
    spec = importlib.util.spec_from_file_location('same_height', args.height_reader)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    reader = module.HeightReader(args.input, args.background, report['N'],
        'k-integral', report['height_coefficient_quadrature']['gauss_order'],
        report['height_anchor'])
    loc = report['worst_curvature']
    cell = loc['cell']; point = loc['x']
    if not reader.breaks[cell] <= point <= reader.breaks[cell+1]:
        raise ValueError('Recorded peak lies outside its atomic cell')
    data = reader.evaluate(np.array([point]), np.array([reader.breaks[cell]]))
    j = round(loc['phi']*reader.N/(2*np.pi)) % reader.N
    rho = getattr(reader, 'rho', np.ones(reader.N))[j]
    rho_phi = getattr(reader, 'rho_phi', np.zeros(reader.N))[j]
    r, w, wr = (data[key][0] for key in ('r', 'w', 'wr'))
    hp, hpp, hrp, hr, hrr = (data[key][0, j] for key in
        ('h_phi', 'h_phiphi', 'hr_phi', 'hr', 'hrr'))
    if abs(r-loc['r']) > 4*np.spacing(r):
        raise ValueError('Actual physical radius differs from the recorded peak')
    y = hr/w; K = y-1; Kr = (hrr-wr*y)/w
    P = hp/(r*w*rho)
    T = hpp/(r*w*rho*rho)-hp*rho_phi/(r*w*rho**3)
    U = hrp/(w*rho)-P
    E = 1+w*w; S = 1-w*w*P*P
    L = y+E*T; N = 1+w*w*y*T/S
    predicted = (wr*S*N+E*w*U*U/r)/L
    result = dict(source_sha256=digest(Path(__file__)),
        readout_report_sha256=hashlib.sha256(report_raw).hexdigest(),
        input_sha256=report['input_sha256'],
        height_reader_sha256=report['height_reader_sha256'],
        r=float(r), x=point, phi=loc['phi'],
        actual_reported_principal_curvature=loc['value'],
        K=float(K), Kr=float(Kr), P=float(P), T=float(T), U=float(U),
        L=float(L), N=float(N), S=float(S), w=float(w), wr=float(wr),
        actual_hrr=float(hrr), wr_times_1plusK=float(wr*y),
        w_times_Kr=float(w*Kr),
        unprojected_Darboux_hrr=float(predicted),
        actual_minus_Darboux_hrr=float(hrr-predicted),
        status='Numerical identity check at an actual reported geometry peak; the prediction is not substituted into the geometry')
    text = json.dumps(result, indent=2)+'\n'
    if args.out:
        args.out.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for option in ('report', 'input', 'background'):
        parser.add_argument('--'+option, type=Path, required=True)
    parser.add_argument('--height-reader', type=Path,
        default=Path(__file__).with_name('2026-11-17-parallel-geometry-stable-height-reader.py'))
    parser.add_argument('--out', type=Path)
    main(parser.parse_args())
