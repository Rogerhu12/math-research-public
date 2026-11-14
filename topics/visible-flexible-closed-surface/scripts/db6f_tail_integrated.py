"""Read the explicit integrated-Fr finite tail without its nonlinear solver.

The mathematical definition uses exact binary input nodes/jets and exact
integration.  numpy evaluates that definition approximately.  Stored post-cut
position columns are diagnostics only; they are recomputed from derivative
data here.  The exact rotational background remains a separate input.
"""
from __future__ import annotations
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import numpy as np


class IntegratedTail:
    def __init__(self, manifest):
        self.manifest_path = Path(manifest)
        self.meta = json.loads(self.manifest_path.read_text())
        if self.meta['status'] not in ['finite-C2-integrated-explicit-tail-with-sampled-audit',
                                       'finite-C2-increment-integrated-explicit-tail-with-sampled-audit']:
            raise ValueError('This reader requires the integrated-Fr format')
        if not self.meta.get('finished'):
            raise ValueError('Incomplete export')
        fmt = self.meta['format']
        self.planar_modes = np.array(fmt['planarModes'], dtype=int)
        self.height_modes = np.array(fmt['heightModes'], dtype=int)
        self.P = len(self.planar_modes)
        self.C = fmt['coefficientCount']
        blocks = []
        last = None
        for info in self.meta['files']:
            p = Path(info['path'])
            if not p.exists():
                p = self.manifest_path.parent / p.name
            raw = p.read_bytes()
            if hashlib.sha256(raw).hexdigest() != info['sha256']:
                raise ValueError('data hash mismatch: ' + str(p))
            a = np.frombuffer(gzip.decompress(raw), dtype='<f8').reshape(info['rows'], info['columns']).copy()
            if last is not None:
                if not np.array_equal(a[0], last):
                    raise ValueError('raw-cell interface rows are not identical')
                blocks.append(a[1:])
            else:
                blocks.append(a)
            last = a[-1]
        self.nodes = np.concatenate(blocks)
        self.r_display = self.nodes[:, 0]
        self.r = self.r_display.copy()
        self.bg_height_nodes_approx = self.nodes[:, 1]
        if 'radialGeometry' in self.meta:
            radial = self.meta['radialGeometry']
            self.unscaled_lengths = self.nodes[1:, -1].copy()
            self.radial_scale = Fraction(int(radial['normalization']['numerator']),
                                        int(radial['normalization']['denominator']))
            # Both quantities below are approximate evaluations of exact
            # rational definitions, with extended precision for thin spans.
            scale = np.longdouble(self.radial_scale.numerator) / np.longdouble(self.radial_scale.denominator)
            self.L = self.unscaled_lengths.astype(np.longdouble) * scale
            self.r = np.concatenate([np.array([radial['innerAnchor']], dtype=np.longdouble),
                                     np.longdouble(radial['innerAnchor']) + np.cumsum(self.L)])
            self.r[-1] = np.longdouble(radial['outerAnchor'])
        else:
            self.unscaled_lengths = None
            self.radial_scale = Fraction(1)
            self.L = np.diff(self.r)
        if not np.all(self.L > 0):
            raise ValueError('non-positive physical radial interval')
        v = self.nodes[:, 2:2+4*self.C].reshape(len(self.nodes), 4, self.C)
        self.source_values = v[:, 0]
        self.first = v[:, 1]
        self.second = v[:, 2]
        self.midpoint = v[1:, 3]
        self.value_nodes = np.empty_like(self.first, dtype=np.longdouble)
        self.value_nodes[0] = self.source_values[0]
        increment = self.L[:, None] * (
            (np.longdouble(7) / 30) * (self.first[:-1].astype(np.longdouble) + self.first[1:]) +
            (np.longdouble(8) / 15) * self.midpoint +
            self.L[:, None] * (self.second[:-1].astype(np.longdouble) - self.second[1:]) / 60)
        # Long-double accumulation protects small height and Fourier constants.
        self.value_nodes[1:] = np.asarray(
            np.longdouble(self.value_nodes[0]) +
            np.cumsum(increment.astype(np.longdouble), axis=0), dtype=np.longdouble)

    def coefficients(self, r):
        """Return value, first-r and second-r Fourier coefficients at r."""
        r = np.asarray(r, dtype=np.longdouble)
        if np.any(r < self.r[0]) or np.any(r > self.r[-1]):
            raise ValueError('outside represented finite tail')
        idx = np.clip(np.searchsorted(self.r, r, side='right') - 1, 0, len(self.r) - 2)
        t = ((r - self.r[idx]) / self.L[idx])[..., None]
        return self.span_coefficients(idx, t[..., 0])

    def span_coefficients(self, idx, t):
        """Evaluate a span at exact-coordinate parameter t approximately.

        This interface avoids subtraction of two nearby absolute radii.
        It is preferred for meshes, Bernstein conversion, and quadrature.
        """
        idx, t = np.broadcast_arrays(np.asarray(idx, dtype=int), np.asarray(t, dtype=np.longdouble))
        if np.any(idx < 0) or np.any(idx >= len(self.L)) or np.any(t < 0) or np.any(t > 1):
            raise ValueError('invalid span or local parameter')
        L = self.L[idx][..., None]
        t = t[..., None]
        u0, u1 = self.first[idx], self.first[idx + 1]
        v0, v1 = L * self.second[idx], L * self.second[idx + 1]
        bubble = 16 * self.midpoint[idx] - 8 * (u0 + u1) - 2 * (v0 - v1)
        z0, z1 = u0, v0
        z2 = -3 * u0 + 3 * u1 - 2 * v0 - v1 + bubble
        z3 = 2 * u0 - 2 * u1 + v0 + v1 - 2 * bubble
        z4 = bubble
        value = self.value_nodes[idx] + L * t * (z0 + t * (z1 / 2 + t * (z2 / 3 + t * (z3 / 4 + t * z4 / 5))))
        first = z0 + t * (z1 + t * (z2 + t * (z3 + t * z4)))
        second = (z1 + t * (2 * z2 + t * (3 * z3 + 4 * t * z4))) / L
        return value, first, second

    def perturbation_jets(self, r, theta):
        """Broadcast paired r,theta and return V,Vr,Vtheta,Vrr,Vrtheta,Vthetatheta."""
        r, theta = np.broadcast_arrays(np.asarray(r, dtype=np.longdouble), np.asarray(theta, dtype=np.longdouble))
        value, first, second = self.coefficients(r)
        mp = self.planar_modes
        mh = self.height_modes
        ep = np.exp(1j * theta[..., None] * mp)
        ch, sh = np.cos(theta[..., None] * mh), np.sin(theta[..., None] * mh)

        def apply(c, order):
            planar = np.sum(c[..., :self.P] * ((1j * mp) ** order) * ep, axis=-1)
            if order == 0:
                z = np.sum(c[..., self.P:] * ch, axis=-1)
            elif order == 1:
                z = -np.sum(c[..., self.P:] * mh * sh, axis=-1)
            else:
                z = -np.sum(c[..., self.P:] * mh * mh * ch, axis=-1)
            return np.stack([planar.real, planar.imag, z], axis=-1)

        return apply(value, 0), apply(first, 0), apply(value, 1), apply(second, 0), apply(first, 1), apply(value, 2)

    def xyz_at_nodes(self, indices, theta):
        """Mesh helper; stored rotational heights are approximate quadratures."""
        idx = np.asarray(indices, dtype=int)
        theta = np.asarray(theta, dtype=float)
        r = self.r[idx, None]
        v = self.perturbation_jets(r, theta[None, :])[0]
        bg = np.stack(np.broadcast_arrays(r * np.cos(theta), r * np.sin(theta),
                                         self.bg_height_nodes_approx[idx, None]), axis=-1)
        return bg + v


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('manifest')
    args = ap.parse_args()
    t = IntegratedTail(args.manifest)
    print(json.dumps({'nodes': len(t.r), 'modes': t.C, 'rMin': float(t.r[0]),
                      'rMax': float(t.r[-1]),
                      'derivedNodeValueDifferenceFromStored': float(np.max(np.abs(t.value_nodes - t.source_values))),
                      'scope': 'portable definition reader; no source PDE or continuous geometry certification'}))
