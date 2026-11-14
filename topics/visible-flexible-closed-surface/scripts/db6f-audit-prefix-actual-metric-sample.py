#!/usr/bin/env python3
"""Independent sampled first metric of the saved physical prefix interpolant.

The original quintic coefficients, their actual derivative, and the frozen
material-angle chart define the sampled map. The mean-height derivative is
the defining angular mean of its Frenet velocity; no nonmean derivative is
replaced by the source ODE. Results are finite floating diagnostics only.
They do not build the separate finite shared-jet/full-XYZ closed-map model.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.interpolate import CubicSpline

HERE = Path(__file__).resolve().parent
LD = np.longdouble


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def read_metadata(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def evaluate_saved_pp(coefficients, mesh, points, derivative):
    """Physical-s Horner, independent of scipy.PPoly evaluation."""
    degree = coefficients.shape[0]-1
    check(derivative in (0, 1), 'Only actual value and first derivative are used')
    idx = np.clip(np.searchsorted(mesh, points, side='right')-1, 0, len(mesh)-2)
    dx = np.asarray(points, LD)-np.asarray(mesh[idx], LD)
    out = np.zeros((len(points), coefficients.shape[2]), dtype=LD)
    for k in range(degree+1-derivative):
        term = np.asarray(coefficients[k, idx, :], LD)
        if derivative:
            term = term*(degree-k)
        out = out*dx[:, None]+term
    return out


class IndependentMap:
    def __init__(self, record, profile, angular):
        self.record = record
        self.profile = profile
        self.M = record['config']['modes']
        self.q = LD(record['gauge_amplitude'])
        self.end = record['meridian_length']
        self.mesh = np.asarray(record['mesh'])
        self.coefficients = np.asarray(record['pp_coefficients'])
        check(self.coefficients.shape == (6, len(self.mesh)-1, 3*self.M+1),
              'Unexpected complete cylindrical quintic representation')
        check(np.all(np.diff(self.mesh) > 0), 'Nonpositive source span')
        chart = record['chart']
        self.spline = CubicSpline(chart['knots'], chart['values'],
                                 bc_type=((1, 0.), (1, chart['final_derivative'])))
        # Use the same saved-grid double angles; evaluate trigonometry and
        # cancellation-sensitive vector arithmetic in extended precision.
        self.psi = np.asarray(2*np.pi*np.arange(angular)/angular, LD)
        self.m = np.asarray(3*np.arange(1, self.M+1), LD)
        self.co = np.cos(self.m[:, None]*self.psi[None, :])
        self.si = np.sin(self.m[:, None]*self.psi[None, :])
        self.c3 = np.cos(3*self.psi)[None, :]
        self.s3 = np.sin(3*self.psi)[None, :]

    def chart(self, points):
        x = np.asarray(points)/self.end
        # This evaluates the frozen numerical source profile/chart. Exact
        # bridge-root transfer is a separate continuous-certificate input.
        h0 = np.asarray(self.spline(x), LD)
        h1 = np.asarray(self.spline(x, 1)/self.end, LD)
        u = np.asarray(np.clip(4*(x-.75), 0., 1.), LD)
        cut = 1-u**3*(10-15*u+6*u*u)
        cut_s = -30*u*u*(1-u)**2*LD(4/self.end)
        scale = LD(8)*LD(self.record['warp_reference_q'])
        e = scale*h0*cut
        ep = scale*(h1*cut+h0*cut_s)
        gamma = -e[:, None]*self.s3/3
        gamma_s = -ep[:, None]*self.s3/3
        rho = 1-e[:, None]*self.c3
        rho_psi = 3*e[:, None]*self.s3
        check(np.min(rho) > 0, 'Noninvertible angular chart')
        return gamma, gamma_s, rho, rho_psi

    def fields(self, points):
        Y = evaluate_saved_pp(self.coefficients, self.mesh, points, 0)
        D = evaluate_saved_pp(self.coefficients, self.mesh, points, 1)
        R, T, Z = (Y[:, 1+j*self.M:1+(j+1)*self.M] for j in range(3))
        Rs, Ts, Zs = (D[:, 1+j*self.M:1+(j+1)*self.M] for j in range(3))
        a, ap, _ = self.profile(np.asarray(points))
        a, ap = np.asarray(a, LD)[:, None], np.asarray(ap, LD)[:, None]
        gamma, gamma_s, rho, rho_psi = self.chart(points)
        cg, sg = np.cos(gamma), np.sin(gamma)
        q, m = self.q, self.m[None, :]
        # Vectors below use the orthonormal rotating frame at psi. Differentiating
        # that frame gives the -T,+R terms, so these are actual Cartesian jets.
        position_without_mean_height = np.stack((
            a*cg+q*(Y[:, :1]+R@self.co),
            a*sg+q*(T@self.si), q*(Z@self.co)), axis=-1)
        d = np.stack((
            -a*rho*sg-q*((m*R+T)@self.si),
            a*rho*cg+q*(Y[:, :1]+(R+m*T)@self.co),
            -q*((m*Z)@self.si)), axis=-1)
        dd = np.stack((
            a*(-rho*rho*cg-rho_psi*sg)+q*(-Y[:, :1]+(-(m*m+1)*R-2*m*T)@self.co),
            a*(-rho*rho*sg+rho_psi*cg)+q*((-2*m*R-(m*m+1)*T)@self.si),
            -q*((m*m*Z)@self.co)), axis=-1)
        speed = np.sqrt(np.sum(d*d, axis=-1))
        tangent = d/speed[..., None]
        nv = dd-np.sum(dd*tangent, axis=-1)[..., None]*tangent
        nn = np.sqrt(np.sum(nv*nv, axis=-1))
        normal = nv/nn[..., None]
        curvature = nn/(speed*speed)
        binormal = np.cross(tangent, normal)
        alpha = -ap/(a*curvature)
        margin = 1-alpha*alpha
        check(np.min(margin) > 0, 'Frenet root outside its positive branch')
        Vnormal = alpha[..., None]*normal+np.sqrt(margin)[..., None]*binormal
        v = gamma_s/rho
        W = Vnormal+v[..., None]*d
        height_s = np.mean(W[..., 2], axis=1)
        Xu = np.stack((
            ap*cg-a*sg*gamma_s+q*(D[:, :1]+Rs@self.co),
            ap*sg+a*cg*gamma_s+q*(Ts@self.si),
            q*(Zs@self.co)+height_s[:, None]), axis=-1)
        Fs = Xu-v[..., None]*d
        Ft = d/rho[..., None]
        residual = np.stack((np.sum(Fs*Fs, axis=-1)-1,
            np.sum(Fs*Ft, axis=-1)/a,
            np.sum(Ft*Ft, axis=-1)/(a*a)-1), axis=-1)
        return dict(residual=residual, Fs=Fs, Ft=Ft, Vnormal=Vnormal,
            position_without_mean_height=position_without_mean_height,
            rho=rho, root_margin=margin, height_s=height_s)


def run(args):
    started = time.monotonic()
    metadata = read_metadata(args.checkpoint)
    chunks = []
    for item in metadata.get('pp_coefficient_chunks', []):
        path = args.checkpoint.parent/item['file']
        check(sha(path) == item['sha256'] and path.stat().st_size == item['bytes'],
              'Changed saved quintic chunk')
        chunks.append(dict(file=str(path), sha256=sha(path)))
    check(metadata['config']['fixed_metric'] is True, 'Unfrozen physical prefix')
    check(metadata['physical_port_sha256'] == sha(args.linear_port), 'Changed physical port')
    port = read_metadata(args.linear_port)
    check(metadata['physical_tail_parameters'] == port['parameters'] and
          metadata['physical_tail_cut'] == port['cut'], 'Different physical port definition')
    reference = read_metadata(args.reference_geometry)
    same_fields = ['frozen_profile', 'chart', 'warp_reference_q']
    for key in same_fields:
        check(metadata[key] == reference[key], 'Different fixed prefix target '+key)
    check(reference['port_sha256'] == sha(args.linear_port), 'Reference physical port differs')
    loader_path = HERE/'db6f-prefix-flat-geometry-source.py'
    check(reference['profile_loader_sha256'] == sha(loader_path) and
          reference['profile_implementation_sha256'] == sha(HERE/'db6f-prefix-flat-profile.py'),
          'Reference physical profile implementation differs')
    loader = load_module('independent_actual_prefix_loader', loader_path)
    record, obj, flow, _ = loader.source(args.checkpoint, args.linear_port, args.source_root)
    check(record['meridian_length'] == flow.end, 'Changed physical arclength length')
    mapping = IndependentMap(record, flow.profile, args.angular)
    mesh = np.asarray(record['mesh'])
    samples = np.unique(np.r_[np.linspace(0, flow.end, 151), mesh, (mesh[:-1]+mesh[1:])/2])
    maxima = {key: dict(value=0., s=None, component=None) for key in
              ('metric_fft_l1', 'metric_operator_sample', 'entry_absolute_sample', 'flow_velocity_defect')}
    component_fft = np.zeros(3)
    inlet = None
    rho_min, root_min = 1., 1.
    for start in range(0, len(samples), args.batch):
        s = samples[start:start+args.batch]
        fields = mapping.fields(s)
        e = fields['residual']
        l1 = np.sum(abs(np.fft.fft(e, axis=1)/args.angular), axis=1)
        components = np.max(l1, axis=0)
        component_fft = np.maximum(component_fft, components)
        op = (abs(e[..., 0]+e[..., 2])+np.sqrt((e[..., 0]-e[..., 2])**2+4*e[..., 1]**2))/2
        defect = np.sqrt(np.sum((fields['Fs']-fields['Vnormal'])**2, axis=-1))
        arrays = dict(metric_fft_l1=l1, metric_operator_sample=op,
                      entry_absolute_sample=np.max(abs(e), axis=1), flow_velocity_defect=defect)
        for name, values in arrays.items():
            ij = np.unravel_index(np.argmax(values), values.shape)
            value = float(values[ij])
            if value > maxima[name]['value']:
                maxima[name] = dict(value=value, s=float(s[ij[0]]),
                    component=int(ij[1]) if name in ('metric_fft_l1', 'entry_absolute_sample') else None,
                    angular_index=int(ij[1]) if name in ('metric_operator_sample', 'flow_velocity_defect') else None)
        rho_min = min(rho_min, float(np.min(fields['rho'])))
        root_min = min(root_min, float(np.min(fields['root_margin'])))
        if start == 0:
            inlet = dict(component_fft_l1=[float(x) for x in l1[0]], operator_sample=float(np.max(op[0])),
                         mean_height_derivative=float(fields['height_s'][0]))
    source_names = ['db6f-prefix-flat-geometry-source.py', 'db6f-prefix-flat-profile.py',
                    '950f-prefix-flat-accel-screen.py', '950f-prefix-adaptive-chart-bvp-v2.py',
                    '950f-prefix-warped-bvp.py']
    sources = {name: sha(HERE/name) for name in source_names}
    source_root = args.source_root.resolve()
    source_closure = {}
    for module in tuple(sys.modules.values()):
        filename = getattr(module, '__file__', None)
        if filename is None:
            continue
        path = Path(filename).resolve()
        if path.suffix == '.py' and path.is_relative_to(source_root):
            source_closure[str(path.relative_to(source_root))] = sha(path)
    saved_l1 = record.get('summary', {}).get('metric_l1')
    out = dict(status='SAMPLED-independent-actual-quintic-first-metric', scope=__doc__,
        checkpoint=str(args.checkpoint), checkpoint_sha256=sha(args.checkpoint),
        checkpoint_chunks=chunks, checkpoint_status=metadata.get('status'),
        auxiliary_solver_success=metadata.get('solver_success'),
        actual_nonlinear_tail=metadata['config'].get('actual_nonlinear_tail', False),
        frozen_affine_dn=metadata['config'].get('frozen_affine_dn', False),
        script_sha256=sha(__file__), source_sha256=sources,
        frozen_source_closure_sha256=source_closure,
        reference_geometry=str(args.reference_geometry), reference_geometry_sha256=sha(args.reference_geometry),
        unchanged_target_fields=same_fields, same_physical_port_sha256=sha(args.linear_port),
        modes=mapping.M, sampled_s=len(samples), sampled_psi=args.angular,
        source_sampled_s=record.get('summary', {}).get('samples_s'),
        source_sampled_psi=record.get('summary', {}).get('samples_psi'),
        maxima=maxima, component_fft_l1_maxima=[float(x) for x in component_fft], inlet=inlet,
        rho_min_sample=rho_min, root_margin_min_sample=root_min,
        saved_metric_fft_l1=saved_l1,
        independent_minus_saved_metric_fft_l1=None if saved_l1 is None else maxima['metric_fft_l1']['value']-saved_l1,
        saved_pp_derivative_evaluated=True, nonmean_derivative_replaced_by_source_rhs=False,
        mean_height_definition='h(0)=0; h_s is the angular mean of the actual-curve Frenet chart velocity; only h_s is needed here.',
        mean_height_computation='Finite uniform angular quadrature at the reported sampled_psi; its continuous quadrature remainder is not certified here.',
        absolute_mean_height_integrated=False,
        shared_jet_full_xyz_geometry_constructed=False, exact_bridge_root_transferred=False,
        continuous_metric_bound=False, complete_closed_surface=False,
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(out, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key: out[key] for key in ('status', 'modes', 'sampled_s', 'sampled_psi',
        'maxima', 'independent_minus_saved_metric_fft_l1', 'seconds')}))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint', type=Path, required=True)
    ap.add_argument('--linear-port', type=Path, required=True)
    ap.add_argument('--source-root', type=Path, required=True)
    ap.add_argument('--reference-geometry', type=Path, required=True)
    ap.add_argument('--angular', type=int, default=1024)
    ap.add_argument('--batch', type=int, default=16)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    check(args.angular >= 64 and args.batch >= 1, 'Invalid sampling grid')
    run(args)
