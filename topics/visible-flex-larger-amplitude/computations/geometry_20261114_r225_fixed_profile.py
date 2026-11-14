#!/usr/bin/env python3
"""Freeze a designed scalar profile as an exact C2 piecewise polynomial and replay.

The model fixes all core coefficients and every scalar-profile knot. Replays
change only Fourier/angle/time discretization. This is an open-prefix test,
not closure, all-time reach, or a complete Hausdorff-amplitude certificate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import bisect
import gzip
import hashlib
import importlib.util
import json
import time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

P = Path(__file__).resolve().parent


def module(name, filename):
    s = importlib.util.spec_from_file_location(name, P/filename)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


base = module('geometry_fixed_profile_base', 'geometry_20261114_r225_outward_probe.py')
fft = module('geometry_fixed_profile_fft', 'geometry_20261114_fft_frenet.py')


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def canonical_hash(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def exact_original_jet(law, s):
    length, speed, k0 = Q(float(law['length'])), Q(float(law['velocity'])), Q(float(law['k0']))
    s = Q(float(s))
    if s >= length:
        end = 1+length*speed/2+k0*length*length/12
        return end+speed*(s-length), speed, Q(0)
    u = s/length
    b, c, d = k0*length, 3*speed-2*k0*length, k0*length-2*speed
    return (1+length*(b*u*u/2+c*u**3/3+d*u**4/4),
            b*u+c*u*u+d*u**3, (b+2*c*u+3*d*u*u)/length)


class FixedProfile:
    def __init__(self, geometry):
        self.geometry = geometry
        self.knots = geometry['knots']
        self.x = np.array([float(k['s']) for k in self.knots])
        if np.any(np.diff(self.x) <= 0):
            raise ValueError('Profile knots must be strictly ordered')
        self.join = float(self.x[0])
        self.end = float(self.x[-1])
        law = geometry['initial_law']
        self.old = base.control.HermiteOutward(law['velocity'], law['length'], law['k0']).profile
        jets = [tuple(Q(float(k[name])) for name in ('a','ap','app')) for k in self.knots]
        first = exact_original_jet(law, self.join)
        self.first_jet_float_correction = [float(v)-float(w) for v,w in zip(first,jets[0])]
        jets[0] = first
        coefficients = []
        exact_strings = []
        self.exact_seam_checks = 0
        for i in range(len(self.x)-1):
            h = Q(float(self.x[i+1]))-Q(float(self.x[i]))
            left, right = jets[i], jets[i+1]
            c0, c1, c2 = left[0], h*left[1], h*h*left[2]/2
            aa = right[0]-c0-c1-c2
            bb = h*right[1]-c1-2*c2
            cc = h*h*right[2]-2*c2
            coef = [c0,c1,c2,10*aa-4*bb+cc/2,-15*aa+7*bb-cc,6*aa-3*bb+cc/2]
            assert sum(coef) == right[0]
            assert sum(j*coef[j] for j in range(1,6))/h == right[1]
            assert sum(j*(j-1)*coef[j] for j in range(2,6))/(h*h) == right[2]
            self.exact_seam_checks += 3
            coefficients.append([float(v) for v in coef])
            exact_strings.append([str(v) for v in coef])
        self.coefficients = np.array(coefficients)
        self.exact_coefficient_sha256 = canonical_hash(exact_strings)

    def profile(self, s):
        if s <= self.join:
            return self.old(s)
        if s > self.end+2e-13:
            raise ValueError('Fixed profile does not extend beyond its saved end')
        j = min(len(self.x)-2, bisect.bisect_right(self.x, s)-1)
        h = self.x[j+1]-self.x[j]
        u = (s-self.x[j])/h
        c = self.coefficients[j]
        a = np.polynomial.polynomial.polyval(u,c)
        ap = np.polynomial.polynomial.polyval(u,np.arange(1,6)*c[1:])/h
        app = np.polynomial.polynomial.polyval(u,np.arange(2,6)*np.arange(1,5)*c[2:])/(h*h)
        return float(a),float(ap),float(app)


def freeze(args):
    d = read(args.input)
    ident = d['original_metric_identity']
    incoming = d.get('incoming_fixed_metric_profile')
    knots = list(d['scalar_profile_knots'])
    if incoming is not None:
        before = [r for r in incoming['knots'] if r['s'] < knots[0]['s']-1e-12]
        knots = before+knots
    geometry = dict(core_sha256=ident['core_sha256'],
                    coefficients_rational=ident['coefficients_rational'],
                    initial_law=ident['law'], knots=knots)
    profile = FixedProfile(geometry)
    result = dict(schema='r225-exact-C2-scalar-polynomial-profile-v1', geometry=geometry,
                  geometry_sha256=canonical_hash(geometry),
                  exact_coefficient_sha256=profile.exact_coefficient_sha256,
                  exact_seam_checks=profile.exact_seam_checks,
                  first_jet_float_correction=profile.first_jet_float_correction,
                  source_probe_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                  source_probe_status=d['status'],
                  definition='Binary64 stored knots are exact rationals. The first knot jet is replaced by the exact original entrance polynomial jet. Each interval is the unique quintic matching value and first two physical derivatives.',
                  scope='A newly fixed scalar metric; original feedback samples are not asserted to solve this new interpolation exactly.')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('geometry_sha256','exact_coefficient_sha256','exact_seam_checks','first_jet_float_correction')}))


def replay(args):
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    fft_hash = hashlib.sha256((P/'geometry_20261114_fft_frenet.py').read_bytes()).hexdigest()
    saved = read(args.profile)
    g = saved['geometry']
    if canonical_hash(g) != saved['geometry_sha256']:
        raise ValueError('Fixed geometry fingerprint mismatch')
    frozen = FixedProfile(g)
    if frozen.exact_coefficient_sha256 != saved['exact_coefficient_sha256']:
        raise ValueError('Exact polynomial reconstruction mismatch')
    law = g['initial_law']
    coefficients = np.array([float(Q(v)) for v in g['coefficients_rational']])
    q = base.FullCoreProbe(coefficients,args.M,args.N,law['velocity'],law['length'],law['k0'])
    q.profile = frozen.profile
    if not args.dense_kernel:
        fft.enable_fft(q)
    y = q.initial()
    rows = [q.stats(0.,y)]
    states = [y.tolist()]
    locations = [0.]
    last = 0.
    status = 'success'
    begin = time.time()
    mesh = np.unique(np.r_[np.linspace(0,frozen.join,int(np.ceil(frozen.join/args.sample_step))+1),frozen.x])
    for i,s in enumerate(mesh[1:]):
        try:
            sol = solve_ivp(q.fun,(last,s),y,method='DOP853',rtol=args.rtol,atol=args.rtol*.01,
                            max_step=min(args.maxstep,(s-last)/2))
            if not sol.success:
                raise RuntimeError(sol.message)
            y = sol.y[:,-1]
            last = float(s)
            rows.append(q.stats(last,y))
            states.append(y.tolist())
            locations.append(last)
            if (i+1)%20 == 0:
                print(json.dumps(dict(event='fixed_profile',M=args.M,s=last,
                                      metric=rows[-1]['metric_sample'],
                                      kappa=rows[-1]['surface_kappa_sample'],
                                      a_kappa_min=rows[-1]['a']*rows[-1]['kappa_curve_min'],
                                      witness=rows[-1]['core_witness_sample_distance'])),flush=True)
        except Exception as error:
            status = repr(error)
            break
    identity = dict(core_sha256=g['core_sha256'],coefficients_rational=g['coefficients_rational'],
                    law=law,end=frozen.end,fixed_scalar_profile_sha256=saved['geometry_sha256'])
    result = dict(scope=__doc__,status=status,reached_s=last,target_s=frozen.end,
                  metric_identity=identity,metric_identity_sha256=canonical_hash(identity),
                  fixed_metric_profile=g,exact_profile_coefficient_sha256=frozen.exact_coefficient_sha256,
                  numerical_parameters=dict(M=args.M,N=args.N,maxstep=args.maxstep,
                                            sample_step=args.sample_step,rtol=args.rtol,
                                            kernel='dense' if args.dense_kernel else 'fft'),
                  rows=rows,coefficient_states=states,state_locations=locations,
                  core=dict(hmajor=q.hmajor,hminor=q.hminor,gap=q.gap),
                  summary=dict(metric_sample=max(r['metric_sample'] for r in rows),
                               kappa_sample=max(r['surface_kappa_sample'] for r in rows),
                               reflected_prefix_D_sample=2*max(r['ball_radius_max'] for r in rows),
                               core_witness_sample_distance=min(r['core_witness_sample_distance'] for r in rows),
                               smallest_domain_margin=min(r['margin'] for r in rows)),
                  seconds=time.time()-begin,calls=q.calls,source_sha256=source_hash,fft_source_sha256=fft_hash)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    encoded=(json.dumps(result,indent=2)+'\n').encode()
    args.out.write_bytes(gzip.compress(encoded,mtime=0) if args.out.suffix=='.gz' else encoded)
    print(json.dumps({k:result[k] for k in ('status','reached_s','seconds','calls','summary')}),flush=True)


def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest='command',required=True)
    f=sub.add_parser('freeze')
    f.add_argument('--input',type=Path,required=True)
    f.add_argument('--out',type=Path,required=True)
    r=sub.add_parser('replay')
    r.add_argument('--profile',type=Path,required=True)
    r.add_argument('--M',type=int,required=True)
    r.add_argument('--N',type=int,required=True)
    r.add_argument('--sample-step',type=float,default=.005)
    r.add_argument('--maxstep',type=float,default=.00025)
    r.add_argument('--rtol',type=float,default=1e-11)
    r.add_argument('--dense-kernel',action='store_true')
    r.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    freeze(a) if a.command=='freeze' else replay(a)


if __name__=='__main__':
    main()
