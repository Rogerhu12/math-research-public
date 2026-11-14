#!/usr/bin/env python3
"""Background-preserving Cartesian tail adapter for finite closed assembly.

The source background is external. The nonround 512-angle cardinal field has
the same shared nonuniform radial second jets as the measured factor-four
reconstruction. The fixed-width outer correction uses the saved prefix's
actual Fourier coefficients, not a second interpolation of prefix samples.
The inner zero-two-jet collar remains an explicitly approximate closing step.
"""
import gzip
import hashlib
import importlib.util
import inspect
import json
import sys
import textwrap
from functools import lru_cache
from pathlib import Path
from types import MethodType
import numpy as np

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    sys.modules[name] = out
    spec.loader.exec_module(out)
    return out


def hermite(y0, y1, v0, v1, w0, w1, h):
    dy = y1-y0-h*v0
    dv = h*(v1-v0)
    a, b = h*h*w0, h*h*w1
    return np.stack([y0, h*v0, a/2, 10*dy-4*dv-1.5*a+.5*b,
                     -15*dy+7*dv+1.5*a-b, 6*dy-3*dv-.5*a+.5*b])


def evaluate(c, t, h, derivative=0):
    weights = np.zeros(6, np.longdouble)
    for k in range(derivative, 6):
        fac = 1
        for j in range(derivative):
            fac *= k-j
        weights[k] = fac*t**(k-derivative)/h**derivative
    return np.einsum('j,jkc->kc', weights, c)


def fourier(y):
    """Positive-frequency amplitudes: value = Re sum c_k exp(i k theta).

    The even-grid Nyquist coefficient is one cosine, with its full amplitude.
    This defines the same cardinal function at arbitrary angles and phases.
    """
    c = np.fft.rfft(np.asarray(y, float), axis=0)/len(y)
    c[1:-1] *= 2
    return c.astype(np.clongdouble)


def synth(c, theta, derivative=0):
    k = np.arange(c.shape[-2])
    basis = np.exp(1j*np.asarray(theta)[:, None]*k)*(1j*k)**derivative
    return np.asarray(np.einsum('...kc,nk->...nc', c, basis).real, float)


class RefinedTail:
    """Lazy, hash-checked reader; no full-tail arrays or nonlinear engine."""
    def __init__(self, complete):
        self.path = Path(complete)
        self.meta = json.loads(self.path.read_text())
        if not self.meta.get('finished'):
            raise ValueError('A complete radial readout is required')
        self.rows = self.meta['rows'][::-1]
        self.N = self.meta['angular']
        self.r = np.array([x['geometry']['r'] for x in self.rows], np.longdouble)
        if self.N % 2 or not np.all(np.diff(self.r) > 0):
            raise ValueError('Even angular cardinal grid and increasing radii required')
        if not all('meanPerturbationInnerAnchor' in row for row in self.rows):
            raise ValueError('The directly accumulated small mean is required')
        self.verified_nodes = set()

    @lru_cache(maxsize=96)
    def raw(self, index):
        row = self.rows[index]
        data = (self.path.parent/row['file']).read_bytes()
        raw = gzip.decompress(data)
        if hashlib.sha256(data).hexdigest() != row['sha256'] or hashlib.sha256(raw).hexdigest() != row['rawSha256']:
            raise ValueError('Changed radial node '+str(index))
        self.verified_nodes.add(index)
        return np.frombuffer(raw, dtype='<f8').reshape(self.N, 12).astype(np.longdouble)

    @lru_cache(maxsize=64)
    def node_coefficients(self, index):
        z = self.raw(index)
        g = self.rows[index]['geometry']
        y, v, w = z[:, :3].copy(), z[:, 3:6].copy(), np.empty_like(z[:, :3])
        y[:, 2] += np.longdouble(self.rows[index]['meanPerturbationInnerAnchor'])
        v[:, 2] -= np.longdouble(g['w'])
        wr = np.longdouble(g['w'])*np.longdouble(g['dlogwdx'])/np.longdouble(g['drdx'])
        w[:, 2] = z[:, 9]-wr
        if index == 0:
            w[:, :2] = (self.raw(1)[:, 3:5]-z[:, 3:5])/(self.r[1]-self.r[0])
        elif index == len(self.r)-1:
            w[:, :2] = (z[:, 3:5]-self.raw(index-1)[:, 3:5])/(self.r[index]-self.r[index-1])
        else:
            hm, hp = self.r[index]-self.r[index-1], self.r[index+1]-self.r[index]
            w[:, :2] = (hp/(hm+hp)*(z[:, 3:5]-self.raw(index-1)[:, 3:5])/hm +
                         hm/(hm+hp)*(self.raw(index+1)[:, 3:5]-z[:, 3:5])/hp)
        return tuple(fourier(a) for a in (y, v, w))

    @lru_cache(maxsize=64)
    def span(self, index):
        y0, v0, w0 = self.node_coefficients(index)
        y1, v1, w1 = self.node_coefficients(index+1)
        return hermite(y0, y1, v0, v1, w0, w1, self.r[index+1]-self.r[index])

    def coefficients(self, r):
        r = np.longdouble(r)
        if r < self.r[0] or r > self.r[-1]:
            raise ValueError('Outside the represented finite tail')
        if r == self.r[0]:
            return self.node_coefficients(0)
        if r == self.r[-1]:
            return self.node_coefficients(len(self.r)-1)
        index = int(np.searchsorted(self.r, r, side='right')-1)
        h = self.r[index+1]-self.r[index]
        t = (r-self.r[index])/h
        c = self.span(index)
        return tuple(evaluate(c, t, h, d) for d in range(3))


def prefix_cut_coefficients(saved, mean_s, mean_ss, max_frequency):
    """Actual saved nonmean PPoly in the identity cut chart, in r coordinates."""
    s = np.array([saved.flow.end])
    theta = 2*np.pi*np.arange(16)[None, :]/16
    angle = saved.angle(s, theta)
    errors = {key:float(np.max(abs(angle[key]))) for key in ('theta_s','theta_ss','rho_s','rhop_s','rhop')}
    errors.update(rho=float(np.max(abs(angle['rho']-1))), theta=float(np.max(abs(angle['theta']-theta))))
    if max(errors.values()) > 1e-13:
        raise ValueError('Direct prefix Fourier endpoint requires the identity cut chart through two jets')
    a, ap, app = (float(x[0]) for x in saved.flow.profile(s))
    if not ap < 0 or max_frequency < saved.mode*saved.M+1:
        raise ValueError('Closing radial orientation or angular capacity differs')
    y, ys, yss = (saved.sol.sol(s, d)[:, 0] for d in range(3))
    yr = ys/ap
    yrr = (yss-app*yr)/ap**2
    means = [0., mean_s/ap, (mean_ss-app*mean_s/ap)/ap**2]
    result = []
    for order, state in enumerate((y, yr, yrr)):
        p = {1: [a, 1., 0.][order]+saved.q*state[0]}
        for j, n in enumerate(saved.frequencies):
            radial, tangent = saved.q*state[1+j], saved.q*state[1+saved.M+j]
            p[1+int(n)] = (radial+tangent)/2
            p[1-int(n)] = (radial-tangent)/2
        c = np.zeros((max_frequency+1, 3), np.clongdouble)
        for k in range(1, max_frequency+1):
            positive, negative = p.get(k, 0.), p.get(-k, 0.)
            c[k, 0] = positive+negative
            c[k, 1] = -1j*(positive-negative)
        c[0, 2] = means[order]
        for j, n in enumerate(saved.frequencies):
            c[int(n), 2] = saved.q*state[2*saved.M+1+j]
        result.append(c)
    return tuple(result), dict(radius=a, r_s=ap, r_ss=app, chart_identity_residuals=errors,
                               definition='Direct cylindrical saved Fourier coefficients converted to Cartesian amplitudes; no prefix FFT or point interpolation.')


def complete_prefix_heights(saved, s, angular, batch=8):
    """Original positive span-wise Gauss6 mean primitive, bounded batch only."""
    original = textwrap.dedent(inspect.getsource(saved.flow.height_integral.__func__))
    transformed = original
    for old, new in [('range(0,len(flat),128)',f'range(0,len(flat),{batch})'),
                     ('first:first+128',f'first:first+{batch}')]:
        if old not in transformed:
            raise ValueError('Original mean-integral batch anchor changed')
        transformed = transformed.replace(old, new)
    namespace = dict(saved.flow.height_integral.__func__.__globals__)
    exec(compile(transformed, '<original-Gauss6-with-bounded-batches>', 'exec'), namespace)
    integral = MethodType(namespace['height_integral'], saved.flow)
    h = integral(saved.sol, s, angular, 6)
    _, b1, b2 = saved.flow.basis(angular)
    hp, hpp = np.empty(len(s)), np.empty(len(s))
    for first in range(0, len(s), batch):
        sl = slice(first, first+batch)
        at = s[sl]
        frame, _, dw = saved.flow.velocity_s(at, saved.sol.sol(at), saved.sol.sol(at, 1), b1, b2)
        hp[sl] = np.mean(frame['V'][:, :, 2], axis=1)
        hpp[sl] = np.mean(dw[:, :, 2], axis=1)
    return (h, hp, hpp), dict(angular=angular, quadrature_order=6, batch=batch,
        original_function_sha256=hashlib.sha256(original.encode()).hexdigest(),
        bounded_function_sha256=hashlib.sha256(transformed.encode()).hexdigest(),
        definition='Original full mean primitive anchored at physical s=0; only evaluation batch size changes.')


class RefinedAssembly:
    """Finite map API compatible with the old assembly's jets and piece rules."""
    def __init__(self, saved, tail, plan, heights, cut_height):
        self.saved, self.tail, self.plan = saved, tail, plan
        self.old = module('exact_refined_old_assembly', HERE/'geometric-closed-assembly.py')
        self.height = {float(row['r']):row for row in heights['rows']}
        self.inner, self.cut, self.cuff = plan['tail_inner'], plan['cut'], plan['cuff']
        self.L, self.W = plan['prefix_end'], plan['cut_correction_width']
        self.sigma = float(saved.flow.bridge.sigma)
        if self.sigma != -1. or not np.isclose(self.cut, float(tail.r[-1]), rtol=0, atol=1e-14):
            raise ValueError('This upper closing sheet needs the original reflected positive-r tail')
        self.prefix_cut_mean = float(cut_height[0])
        self.inner_coeff = tail.node_coefficients(0)
        outer = tail.node_coefficients(len(tail.r)-1)
        self.tail_cut_mean = float(outer[0][0, 2].real)
        self.offset = self.prefix_cut_mean-self.sigma*self.tail_cut_mean
        self.cap_height = self.offset-self.sigma*self.height[self.cuff]['heightFromRToCut']
        target, self.cut_radial_jets = prefix_cut_coefficients(saved, cut_height[1], cut_height[2], tail.N//2)
        g = tail.rows[-1]['geometry']
        wr = g['w']*g['dlogwdx']/g['drdx']
        aligned = [c.copy() for c in outer]
        reflection = np.array([1., 1., self.sigma])
        for c in aligned:
            c *= reflection
        for order, radius in enumerate((self.cut, 1., 0.)):
            aligned[order][1, :2] += np.array([radius, -1j*radius])
        aligned[0][0, 2] = 0.
        aligned[1][0, 2] += self.sigma*g['w']
        aligned[2][0, 2] += self.sigma*wr
        self.cut_difference_coeff = np.stack([(a-b)*reflection for a,b in zip(target, aligned)])
        zero = np.zeros_like(target[0])
        self.patch = hermite(zero, self.cut_difference_coeff[0], zero, self.cut_difference_coeff[1],
                             zero, self.cut_difference_coeff[2], np.longdouble(self.W))
        self.inner_collar = hermite(zero, self.inner_coeff[0], zero, self.inner_coeff[1],
                                    zero, self.inner_coeff[2], np.longdouble(self.inner-self.cuff))

    def prefix_jets(self, s, theta, height):
        return self.old.material_jets(self.saved, np.asarray(s), np.asarray(theta), height)

    def perturbation(self, r, theta):
        coefficients = []
        for radius in np.asarray(r):
            if radius >= self.inner:
                c = list(self.tail.coefficients(radius))
            else:
                width = np.longdouble(self.inner-self.cuff)
                t = np.longdouble(radius-self.cuff)/width
                c = [evaluate(self.inner_collar, t, width, d) for d in range(3)]
            if radius >= self.cut-self.W:
                t = np.clip(np.longdouble(radius-(self.cut-self.W))/np.longdouble(self.W), 0, 1)
                c = [v+evaluate(self.patch, t, np.longdouble(self.W), d) for d,v in enumerate(c)]
            coefficients.append(c)
        c = np.asarray(coefficients)
        return dict(pos=synth(c[:,0],theta),s1=synth(c[:,1],theta),s2=synth(c[:,2],theta),
                    p1=synth(c[:,0],theta,1),p2=synth(c[:,0],theta,2),sp=synth(c[:,1],theta,1))

    def tail_jets(self, r, theta):
        r, theta = np.asarray(r), np.asarray(theta)
        out = self.perturbation(r, theta)
        h, w, wr = (np.array([self.height[float(x)][key] for x in r]) for key in ('heightFromRToCut','w','wr'))
        for value in out.values():
            value[:, :, 2] *= self.sigma
        co, si = np.cos(theta)[None,:], np.sin(theta)[None,:]
        z = np.zeros((len(r),len(theta)))
        out['pos'] += np.stack(np.broadcast_arrays(r[:,None]*co,r[:,None]*si,(self.offset-self.sigma*h)[:,None]),axis=-1)
        out['s1'] += np.stack(np.broadcast_arrays(co,si,(self.sigma*w)[:,None]),axis=-1)
        out['s2'][:,:,2] += self.sigma*wr[:,None]
        out['p1'] += np.stack(np.broadcast_arrays(-r[:,None]*si,r[:,None]*co,z),axis=-1)
        out['p2'] += np.stack(np.broadcast_arrays(-r[:,None]*co,-r[:,None]*si,z),axis=-1)
        out['sp'] += np.stack(np.broadcast_arrays(-si,co,z),axis=-1)
        return out

    def marker_rows(self, upper):
        return [row for row in self.plan['fixed_cap']['markers'] if row['upper']==upper]

    def cap(self, r, theta, upper=True):
        xy = np.stack(np.broadcast_arrays(np.asarray(r)[:,None]*np.cos(theta),np.asarray(r)[:,None]*np.sin(theta)),axis=-1)
        z = np.full(xy.shape[:-1], self.cap_height)
        labels = np.ones(z.shape, np.uint8)
        for row in self.marker_rows(upper):
            u = np.sum((xy-row['center'])**2,axis=-1)/row['radius']**2
            z += row['height']*np.maximum(0,1-u)**4
            labels[u<1] = 2
        if not upper:
            z *= -1
        return np.dstack([xy,z]), labels

    def cap_normals(self, xyz, upper=True):
        gradient = np.zeros_like(xyz[...,:2])
        for row in self.marker_rows(upper):
            d = xyz[...,:2]-row['center']
            u = np.sum(d*d,axis=-1)/row['radius']**2
            gradient -= row['kappa']*d*np.maximum(0,1-u)[...,None]**3
        n = np.concatenate([-gradient,np.full(gradient.shape[:-1]+(1,),1. if upper else -1.)],axis=-1)
        return n/np.linalg.norm(n,axis=-1)[...,None]

    def phase_jets(self, kind, coordinate, theta, alpha, height=None):
        if kind == 'prefix':
            jets, residual, _ = self.prefix_jets(coordinate, np.asarray(theta)-alpha, height)
        elif kind in ('tail','collar'):
            jets, residual = self.tail_jets(coordinate, np.asarray(theta)-alpha), 0.
        else:
            raise ValueError('Fixed caps are evaluated without phase changes')
        co, si = np.cos(alpha), np.sin(alpha)
        rotation = np.array([[co,-si,0.],[si,co,0.],[0.,0.,1.]])
        return {key:value@rotation.T for key,value in jets.items()}, residual
