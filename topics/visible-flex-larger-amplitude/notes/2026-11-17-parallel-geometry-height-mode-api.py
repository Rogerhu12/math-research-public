"""Actual finite height coefficients and mean jets, queried by physical r.

No angular interpolation is used: evaluate C_j cos(2j*Theta(phi)) directly.
The supplied mean anchor belongs to the selected reader's own angle measure.
The mean primitive, like the nonconstant primitive, is defined by integration
and evaluated on every atomic cell, with a separate Gauss-order comparison.
"""
from pathlib import Path
import hashlib
import importlib.util

import numpy as np
from scipy.optimize import brentq


def cumulative(values):
    total = 0.; correction = 0.; output = [0.]
    for increment in values:
        adjusted = increment-correction
        updated = total+adjusted
        correction = (updated-total)-adjusted
        total = updated; output.append(total)
    return np.asarray(output)


class HeightModes:
    def __init__(self, source, background, *, mean_anchor, angles=512,
                 height_gauss=8, mean_gauss=8, anchor='left', batch_cells=32,
                 height_reader=None):
        self.height_reader_path = Path(height_reader) if height_reader else (
            Path(__file__).with_name('2026-11-17-parallel-geometry-stable-height-reader.py'))
        spec = importlib.util.spec_from_file_location('mode_height_reader', self.height_reader_path)
        self.module = importlib.util.module_from_spec(spec); spec.loader.exec_module(self.module)
        self.reader = self.module.HeightReader(Path(source), Path(background),
            angles, 'k-integral', height_gauss, anchor)
        self.frequency = self.reader.frequency
        self.mean_gauss = mean_gauss
        self.batch_cells = batch_cells
        left, right = self.reader.breaks[:-1], self.reader.breaks[1:]
        low = self._mean_integrals(left, right, mean_gauss)
        high = self._mean_integrals(left, right, mean_gauss+4)
        prefix, prefix_high = cumulative(low), cumulative(high)
        self.mean_nodes = mean_anchor+prefix-(prefix[-1] if anchor == 'right' else 0.)
        comparison = mean_anchor+prefix_high-(prefix_high[-1] if anchor == 'right' else 0.)
        self.mean_quadrature = dict(gauss_order=mean_gauss,
            comparison_gauss_order=mean_gauss+4,
            max_primitive_node_difference=float(np.max(abs(self.mean_nodes-comparison))),
            sum_cell_integral_difference=float(np.sum(abs(low-high))),
            status='Quadrature comparison, not a rigorous integration error bound')
        self.source_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    def _mean_integrals(self, left, right, order):
        nodes, weights = np.polynomial.legendre.leggauss(order)
        output = np.empty(len(left))
        for start in range(0, len(left), self.batch_cells):
            sl = slice(start, start+self.batch_cells)
            lo, hi = left[sl], right[sl]
            points = (lo[:, None]+(hi-lo)[:, None]*(nodes+1)/2).ravel()
            references = np.repeat(lo, order)
            data = self.reader.evaluate(points, references)
            output[sl] = (hi-lo)/2*(data['height_mean_x'].reshape(len(lo), order)@weights)
        return output

    def at_x(self, points, references=None):
        points = np.atleast_1d(np.asarray(points, dtype=float))
        rd = self.reader
        if np.min(points) < rd.breaks[0] or np.max(points) > rd.breaks[-1]:
            raise ValueError('Requested source coordinate is outside the actual finite field')
        if references is None:
            index = np.clip(np.searchsorted(rd.breaks, points, side='right')-1, 0, len(rd.breaks)-2)
            references = rd.breaks[index]
        else:
            references = np.asarray(references, dtype=float)
            index = np.clip(np.searchsorted(rd.breaks, references, side='right')-1, 0, len(rd.breaks)-2)
        data = rd.evaluate(points, references)
        old = self.module.piece_value(rd.state, points, references)
        old_x = self.module.piece_value(rd.state, points, references, 1)
        k = old[:, rd.M:2*rd.M]
        kr = old_x[:, rd.M:2*rd.M]/data['rx'][:, None]
        C = rd.height_coefficients(points, references)
        Cr = data['w'][:, None]*k
        Crr = data['wr'][:, None]*k+data['w'][:, None]*kr
        mean = self.mean_nodes[index]+self._mean_integrals(rd.breaks[index], points, self.mean_gauss)
        return dict(x=points, r=data['r'], C=C, Cr=Cr, Crr=Crr,
            h0=mean, h0r=data['w']*(1+data['c']),
            h0rr=data['wr']*(1+data['c'])+data['w']*data['cr'],
            c=data['c'], cr=data['cr'], literal_mean=data['literal_mean'])

    def at_r(self, radii):
        radii = np.atleast_1d(np.asarray(radii, dtype=float))
        bg = self.reader.bg
        if np.min(radii) < bg.r[0] or np.max(radii) > bg.r[-1]:
            raise ValueError('Requested physical radius is outside the actual finite field')
        if bg.coordinate != 'source-index':
            return self.at_x(radii)
        points = np.empty(len(radii))
        for j, radius in enumerate(radii):
            i = np.clip(np.searchsorted(bg.r, radius, side='right')-1, 0, len(bg.r)-2)
            if radius == bg.r[i]:
                points[j] = bg.x[i]
            elif radius == bg.r[i+1]:
                points[j] = bg.x[i+1]
            else:
                points[j] = brentq(lambda x: float(bg.radius(x)-radius), bg.x[i], bg.x[i+1],
                    xtol=np.nextafter(0., 1.), rtol=4*np.finfo(float).eps)
        return self.at_x(points)
