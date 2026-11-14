#!/usr/bin/env python3
"""An explicit C2 finite-Fourier XYZ prefix from shared endpoint jets.

The exact map is defined by the saved binary64 nodal two-jets and exact
quintic Hermite interpolation, not by rounded power coefficients. The mean
height's nodal values are exact sums of saved per-span increments, avoiding
loss from subtracting independently rounded cumulative heights. Other data
are finite binary rationals. Numerical evaluation uses long double.

This is a representation and sampled-audit layer. It neither proves an
infinite tail nor converts sampled bounds into continuous certificates.
"""
import os
for _k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly
from scipy.special import jv, jvp

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source(checkpoint, port_path, source_root):
    spec = importlib.util.spec_from_file_location(
        'root_adaptive_source', HERE / '950f-prefix-adaptive-chart-bvp-v2.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.old.install_source(source_root)
    from curve_stable_prefix_bvp import load_checkpoint
    rec = load_checkpoint(checkpoint)
    port = json.loads(Path(port_path).read_text())
    _, BVP = module.build_classes(rec['chart'])
    M = rec['config']['modes']
    q = rec['gauge_amplitude']
    obj = BVP(rec['frozen_profile'], port, q, M, max(256, 32*M),
              True, rec['warp_reference_q'])
    par = np.asarray(rec['parameters'], dtype=float).copy()
    par[0] = math.log(rec['actual_primary_amplitude']/q)
    flow = obj.flow(par[0])
    obj.initial(par)
    mesh = np.asarray(rec['mesh'])
    pp = PPoly.construct_fast(np.asarray(rec['pp_coefficients']), mesh,
                             extrapolate=True, axis=1)
    sol = SimpleNamespace(x=mesh, y=pp(mesh), p=par, sol=pp)
    return rec, obj, flow, sol


def angular_warp_jets(flow, s):
    x = np.asarray(s)/flow.end
    h0 = flow.spline(x)
    h1 = flow.spline(x, 1)/flow.end
    h2 = flow.spline(x, 2)/flow.end**2
    u = np.clip((x-.75)/.25, 0., 1.)
    fac = 4/flow.end
    c = 1-u**3*(10-15*u+6*u*u)
    cp = -30*u*u*(1-u)**2*fac
    cpp = -60*u*(1-u)*(1-2*u)*fac**2
    return (flow.warp_e*h0*c,
            flow.warp_e*(h1*c+h0*cp),
            flow.warp_e*(h2*c+2*h1*cp+h0*cpp))


def build(args):
    rec, obj, flow, sol = source(args.checkpoint, args.linear_port,
                                args.source_root)
    M0 = obj.M
    M = max(M0, args.modes)
    # Source mesh already contains the physical and chart spline breaks.
    # Refinement changes only the representation, never the physical metric.
    parts = [sol.x]
    for j in range(1, args.subdivide):
        parts.append(sol.x[:-1]+np.diff(sol.x)*j/args.subdivide)
    mesh = np.unique(np.concatenate(parts))
    if np.min(np.diff(mesh)) <= 0:
        raise ValueError('Non-increasing mesh')
    n = 3*M+2
    jets = np.zeros((3, len(mesh), n))
    aa = flow.profile(mesh)
    e, ep, epp = angular_warp_jets(flow, mesh)
    k, kp, kpp = e/3, ep/3, epp/3
    for d in range(3):
        raw = obj.q*sol.sol(mesh, d).T
        jets[d, :, 0] = raw[:, 0]
        jets[d, :, 1:M0+1] = raw[:, 1:M0+1]
        jets[d, :, M+1:M+M0+1] = raw[:, M0+1:2*M0+1]
        jets[d, :, 2*M+1:2*M+M0+1] = raw[:, 2*M0+1:]
    for j in range(M+1):
        J = jv(j, k)
        J1 = jvp(j, k, 1)
        J2 = jvp(j, k, 2)
        vals = (aa[0]*J,
                aa[1]*J+aa[0]*J1*kp,
                aa[2]*J+2*aa[1]*J1*kp+
                aa[0]*(J2*kp*kp+J1*kpp))
        idx, factor = (0, 1) if j == 0 else (
            (j, 2) if j % 2 == 0 else (M+j, -2))
        for d in range(3):
            jets[d, :, idx] += factor*vals[d]

    _, B1, B2 = flow.basis(args.angular)
    for first in range(0, len(mesh), 32):
        s = mesh[first:first+32]
        fr, _, dW = flow.velocity_s(s, sol.sol(s), sol.sol(s, 1), B1, B2)
        jets[1, first:first+len(s), -1] = np.mean(fr['V'][:, :, 2], axis=1)
        jets[2, first:first+len(s), -1] = np.mean(dW[:, :, 2], axis=1)

    # Positive Gauss quadrature independently on each canonical span.
    # Save the increments themselves as exact constants for the explicit map.
    g, w = np.polynomial.legendre.leggauss(args.quadrature)
    steps = np.empty(len(mesh)-1)
    for first in range(0, len(steps), 8):
        left = mesh[:-1][first:first+8]
        right = mesh[1:][first:first+8]
        h = right-left
        s = ((left+right)[:, None]+h[:, None]*g[None, :])/2
        fr = flow.frame(s.ravel(), obj.q*sol.sol(s.ravel()), B1, B2)
        means = np.mean(fr['V'][:, :, 2].astype(np.longdouble), axis=1)
        integrals = (h.astype(np.longdouble)/2 *
                     (means.reshape(s.shape) @ w.astype(np.longdouble)))
        steps[first:first+len(h)] = integrals
    # These displayed cumulative values are not the defining constants.
    jets[0, :, -1] = np.r_[0., np.cumsum(steps.astype(np.longdouble))]
    before = jets[:, 0].copy()
    # Planar inlet value and vertical first jet. The adaptive chart has a
    # nonzero second s-jet at the inlet, so its tangential Fss must be kept.
    # A constant-psi cylinder cannot be glued here without a chart change.
    jets[0, 0, 2*M+1:] = 0.
    jets[1, 0, :] = 0.
    jets[1, 0, -1] = 1.
    interface_change = np.max(abs(jets[:, 0]-before), axis=1).tolist()
    payload = io.BytesIO()
    np.savez(payload, mesh=mesh.astype('<f8'), jets=jets.astype('<f8'),
             mean_increments=steps.astype('<f8'))
    out_data = args.out_prefix.with_name(args.out_prefix.name+'-data.npz.gz')
    out_data.write_bytes(gzip.compress(payload.getvalue(), mtime=0))
    if out_data.stat().st_size >= 5_000_000:
        raise ValueError('Checkpoint exceeds the repository file-size limit')
    meta = dict(
        scope=__doc__, mathematical_definition='Exact shared nodal two-jet '
        'quintic Hermite, finite cylindrical Fourier modes 3j. All nodal '
        'constants and span increments are exact saved binary64 rationals. '
        'Mean height value at node i is the exact sum of increments before i; '
        'its saved cumulative array is for display only. Planar inlet and '
        'vertical first jet are imposed; second jet retains the adaptive '
        'chart transport, and a cylinder interface is not certified.',
        data_file=out_data.name, data_sha256=sha(out_data),
        checkpoint=str(args.checkpoint), checkpoint_sha256=sha(args.checkpoint),
        linear_port=str(args.linear_port), port_sha256=sha(args.linear_port),
        source_root=str(args.source_root),
        script_sha256=sha(__file__), source_modes=M0, modes=M,
        nodes=len(mesh), minimum_span=float(np.min(np.diff(mesh))),
        maximum_span=float(np.max(np.diff(mesh))),
        mean_quadrature_order=args.quadrature, mean_angular_nodes=args.angular,
        subdivisions=args.subdivide, frozen_profile=rec['frozen_profile'],
        chart=rec['chart'], warp_reference_q=rec['warp_reference_q'],
        ell=args.ell, inlet_jet_changes=interface_change,
        cylinder_second_jet_certified=False,
        core_reference=obj._core.summary(),
        continuous_bounds_certified=False, complete_closed_surface=False)
    out_meta = args.out_prefix.with_suffix('.json')
    out_meta.write_text(json.dumps(meta, indent=2)+'\n')
    print(json.dumps({k: meta[k] for k in ('modes', 'nodes', 'minimum_span',
          'inlet_jet_changes', 'continuous_bounds_certified')}, indent=2))
    print(json.dumps({'data_bytes': out_data.stat().st_size}))


class SharedHermite:
    def __init__(self, meta_path):
        self.meta = json.loads(Path(meta_path).read_text())
        data_path = Path(meta_path).parent/self.meta['data_file']
        if sha(data_path) != self.meta['data_sha256']:
            raise ValueError('Geometry data hash mismatch')
        raw = np.load(io.BytesIO(gzip.decompress(data_path.read_bytes())),
                      allow_pickle=False)
        self.x = raw['mesh']
        self.jets = raw['jets'].astype(np.longdouble)
        self.steps = raw['mean_increments'].astype(np.longdouble)
        self.jets[0, :, -1] = np.r_[np.longdouble(0), np.cumsum(self.steps)]
        self.M = self.meta['modes']
        self.h = np.diff(self.x.astype(np.longdouble))
        Y, D, Q = self.jets
        h = self.h[:, None]
        delta = Y[1:]-Y[:-1]
        delta[:, -1] = self.steps
        e0 = delta-h*D[:-1]-h*h*Q[:-1]/2
        e1 = h*(D[1:]-D[:-1])-h*h*Q[:-1]
        e2 = h*h*(Q[1:]-Q[:-1])
        self.c = np.stack((Y[:-1], h*D[:-1], h*h*Q[:-1]/2,
                           10*e0-4*e1+e2/2,
                           -15*e0+7*e1-e2,
                           6*e0-3*e1+e2/2), axis=1)

    def evaluate(self, s, derivative=0):
        s = np.atleast_1d(s).astype(np.longdouble)
        i = np.clip(np.searchsorted(self.x, s, side='right')-1,
                    0, len(self.x)-2)
        tau = (s-self.x[i])/self.h[i]
        out = np.zeros((len(s), self.c.shape[-1]), dtype=np.longdouble)
        for j in range(5, derivative-1, -1):
            factor = math.factorial(j)//math.factorial(j-derivative)
            out = out*tau[:, None]+factor*self.c[i, j]
        return out/self.h[i, None]**derivative

    def basis(self, angular):
        # Components expressed in the rotating (e_r,e_theta,e_z) frame.
        # Dot products and cross products can be computed directly here.
        psi = 2*np.pi*np.arange(angular)/angular
        B = np.zeros((3*self.M+2, angular, 3), dtype=np.longdouble)
        B1 = B.copy()
        B2 = B.copy()
        B[0, :, 0] = 1
        B1[0, :, 1] = 1
        B2[0, :, 0] = -1
        B[-1, :, 2] = 1
        for j in range(1, self.M+1):
            m = 3*j
            co, si = np.cos(m*psi), np.sin(m*psi)
            r, t, z = j, self.M+j, 2*self.M+j
            B[r, :, 0] = co
            B1[r, :, 0] = -m*si
            B1[r, :, 1] = co
            B2[r, :, 0] = -(m*m+1)*co
            B2[r, :, 1] = -2*m*si
            B[t, :, 1] = si
            B1[t, :, 0] = -si
            B1[t, :, 1] = m*co
            B2[t, :, 0] = -2*m*co
            B2[t, :, 1] = -(m*m+1)*si
            B[z, :, 2] = co
            B1[z, :, 2] = -m*si
            B2[z, :, 2] = -m*m*co
        return B, B1, B2


def audit(args):
    geom = SharedHermite(args.geometry)
    meta = geom.meta
    _, obj, flow, _ = source(Path(meta['checkpoint']),
                            Path(meta['linear_port']), args.source_root)
    if sha(meta['checkpoint']) != meta['checkpoint_sha256']:
        raise ValueError('Source checkpoint changed')
    B, B1, B2 = geom.basis(args.angular)
    s = np.unique(np.r_[geom.x, (geom.x[:-1]+geom.x[1:])/2,
                       np.linspace(0, geom.x[-1], args.radial)])
    out = dict(scope='Sampled actual shared-jet Hermite Cartesian geometry. '
               'No continuous enclosures and no closed surface claim.',
               geometry=str(args.geometry), geometry_sha256=sha(args.geometry),
               nodes=len(geom.x), modes=geom.M, samples_s=len(s),
               samples_psi=args.angular, metric_l1=0., metric_max=0.,
               darboux_l1=0., kappa_max=0., support_min=float('inf'),
               norm_max=0., chart_rho_min=float('inf'),
               continuous_bounds_certified=False)
    def values(c, b):
        return np.einsum('nk,kpc->npc', c, b, optimize=True)
    for first in range(0, len(s), 16):
        ss = s[first:first+16]
        c, d, dd = (geom.evaluate(ss, j) for j in range(3))
        X, Xs, Xss = values(c, B), values(d, B), values(dd, B)
        Xp, Xsp, Xpp = values(c, B1), values(d, B1), values(c, B2)
        X[:, :, 2] += meta['ell']
        g = flow.geo(ss, args.angular)
        a, ap, app = (v.astype(np.longdouble) for v in flow.profile(ss))
        rho, v, vp, vs, rhop = (g[k].astype(np.longdouble) for k in
                               ('rho', 'v', 'vp', 'vs', 'rhop'))
        Fs = Xs-v[:, :, None]*Xp
        Ft = Xp/rho[:, :, None]
        Fss = (Xss-2*v[:, :, None]*Xsp+v[:, :, None]**2*Xpp+
               (v*vp-vs)[:, :, None]*Xp)
        Fst = (Xsp-vp[:, :, None]*Xp-v[:, :, None]*Xpp)/rho[:, :, None]
        Ftt = Xpp/rho[:, :, None]**2-Xp*rhop[:, :, None]/rho[:, :, None]**3
        E = np.sum(Fs*Fs, axis=2)
        F = np.sum(Fs*Ft, axis=2)
        G = np.sum(Ft*Ft, axis=2)
        errors = np.stack((E-1, F/a[:, None], G/a[:, None]**2-1), axis=2)
        out['metric_max'] = max(out['metric_max'], float(abs(errors).max()))
        ft = np.fft.fft(errors.astype(float), axis=1)/args.angular
        out['metric_l1'] = max(out['metric_l1'], float(np.sum(abs(ft), axis=1).max()))
        normal = np.cross(Ft, Fs)
        normal /= np.sqrt(np.sum(normal*normal, axis=2))[:, :, None]
        L, M, N = (np.sum(A*normal, axis=2) for A in (Fss, Fst, Ftt))
        detI = E*G-F*F
        tr = (L*G-2*M*F+N*E)/detI
        detII = (L*N-M*M)/detI
        kap = (abs(tr)+np.sqrt(np.maximum(0., tr*tr-4*detII)))/2
        out['kappa_max'] = max(out['kappa_max'], float(kap.max()))
        out['support_min'] = min(out['support_min'], float(np.sum(X*normal, axis=2).min()))
        out['norm_max'] = max(out['norm_max'], float(np.sqrt(np.sum(X*X, axis=2)).max()))
        out['chart_rho_min'] = min(out['chart_rho_min'], float(rho.min()))
        Hst = (Fst-ap[:, None, None]/a[:, None, None]*Ft)/a[:, None, None]
        Htt = (Ftt+(a*ap)[:, None, None]*Fs)/a[:, None, None]**2
        gram = (np.eye(3)[None, None]-Fs[:, :, :, None]*Fs[:, :, None, :]-
                (Ft/a[:, None, None])[:, :, :, None]*
                (Ft/a[:, None, None])[:, :, None, :])
        tensor = (.5*(Fss[:, :, :, None]*Htt[:, :, None, :]+
                      Htt[:, :, :, None]*Fss[:, :, None, :])-
                  Hst[:, :, :, None]*Hst[:, :, None, :]+
                  (app/a)[:, None, None, None]*gram)
        ft = np.fft.fft(tensor.astype(float), axis=1)/args.angular
        bound = np.sum(np.sqrt(np.sum(abs(ft)**2, axis=(2, 3))), axis=1)
        out['darboux_l1'] = max(out['darboux_l1'], float(bound.max()))
    out['two_ball_diameter_sample'] = 2*out['norm_max']
    args.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    b = sub.add_parser('build')
    for name in ('source-root', 'checkpoint', 'linear-port', 'out-prefix'):
        b.add_argument('--'+name, type=Path, required=True)
    b.add_argument('--modes', type=int, default=16)
    b.add_argument('--angular', type=int, default=768)
    b.add_argument('--quadrature', type=int, default=8)
    b.add_argument('--subdivide', type=int, default=1)
    b.add_argument('--ell', type=float, default=.16)
    a = sub.add_parser('audit')
    for name in ('source-root', 'geometry', 'out'):
        a.add_argument('--'+name, type=Path, required=True)
    a.add_argument('--angular', type=int, default=512)
    a.add_argument('--radial', type=int, default=401)
    args = p.parse_args()
    if args.command == 'build':
        build(args)
    else:
        audit(args)


if __name__ == '__main__':
    main()
