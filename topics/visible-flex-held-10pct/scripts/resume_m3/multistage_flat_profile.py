#!/usr/bin/env python3
"""Explicit multistage meridian law, installed only in a fresh source copy.

The old flat/cosine laws keep their original dispatch. The reference velocity
segments have exact rational data; every prefix length is multiplied by
r=delta/reference_delta. Thus a(s)=1+r*(a_ref(s/r)-1), a' keeps its reference
range and a'' scales by 1/r. This is a new physical metric, not a refinement of
the old metric and not a reach or BVP existence certificate.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil

import numpy as np

TAG = 'held10_multistage_flat_v1'


def _fraction(value):
    return Fraction(str(value))


def _reference(cfg):
    spec = cfg['multistage_flat']
    delta = _fraction(spec['reference_delta'])
    eta = _fraction(spec['eta'])
    if delta <= 0 or not 0 < eta < Fraction(1, 2):
        raise ValueError('Invalid multistage reference excursion or eta')
    if cfg.get('direction', 'outward') != 'outward' or int(cfg['cycles']) != 1:
        raise ValueError('This declared multistage design has one outward cycle')
    strokes = []
    segments = []
    knots = {Fraction(0)}
    s0 = Fraction(0)
    area = Fraction(0)
    for name, sign, peak in (('up', 1, _fraction(cfg['vu'])),
                             ('down', -1, _fraction(cfg['vd']))):
        start = s0
        stroke_area = Fraction(0)
        previous_v = Fraction(0)
        rows = spec[name]
        if not rows:
            raise ValueError('Empty multistage stroke')
        for row in rows:
            if len(row) != 3:
                raise ValueError('Each segment is [v_start,v_end,length]')
            v0, v1, length = map(_fraction, row)
            if length <= 0 or v0 != previous_v:
                raise ValueError('Segment length or velocity continuity failed')
            if min(sign*v0, sign*v1) < 0 or max(sign*v0, sign*v1) > peak:
                raise ValueError('Segment exceeds the declared signed peak velocity')
            segments.append((float(s0), float(length), float(v0), float(v1), float(area)))
            knots.update((s0, s0+length))
            if v0 != v1:
                knots.update((s0+eta*length, s0+(1-eta)*length))
            increment = length*(v0+v1)/2  # Integral of the original F is 1/2.
            area += increment
            stroke_area += increment
            s0 += length
            previous_v = v1
        if previous_v != 0 or stroke_area != sign*delta:
            raise ValueError('Stroke must end at zero speed and have the exact reference area')
        strokes.append(float(s0-start))
    if area != 0:
        raise ValueError('Cycle fails exact radial return')
    return float(delta), float(eta), strokes, segments, np.array(list(map(float, sorted(knots))))


def install(adaptive):
    """Compose with the original source installer before build_classes()."""
    previous_install = adaptive.old.install_source

    def installer(root):
        previous_install(root)
        from fixed_metric_mode3_flow import PlanarSymmetryFlow
        if getattr(PlanarSymmetryFlow, '_held10_multistage_flat_v1', False):
            return
        path = Path(adaptive.old.__file__).with_name('950f-prefix-flat-accel-screen.py')
        spec = importlib.util.spec_from_file_location('_held10_multistage_turn', path)
        turn = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(turn)
        original_init = PlanarSymmetryFlow.__init__
        original_profile = PlanarSymmetryFlow.prefix_profile

        def flow_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            if self.cfg.get('ramp_law') != TAG:
                return
            delta_ref, eta, strokes, segments, knots = _reference(self.cfg)
            ratio = self.delta/delta_ref
            self._multistage_eta = eta
            self._multistage_segments = segments
            self._multistage_ratio = ratio
            self.Tu, self.Td = ratio*np.asarray(strokes)
            # One canonical multiplication also defines the last physical knot.
            # Separately adding rounded Tu and Td can create a one-ULP fake cell.
            self.period = ratio*knots[-1]
            self.prefix_end = self.period
            self.end = self.prefix_end+self.bridge.L
            self.breakpoints = ratio*knots
            bridge_knots = (self.prefix_end+np.asarray(self.bridge.breakpoints)
                            if hasattr(self.bridge, 'breakpoints') else np.array([self.end]))
            self.breaks = np.unique(np.r_[self.breakpoints, bridge_knots, self.end])
            self.multistage_profile_summary = dict(tag=TAG, reference_delta=delta_ref,
                delta=self.delta, length_ratio=ratio, Tu_reference=strokes[0],
                Td_reference=strokes[1], physical_knots=self.breakpoints.tolist(),
                scaling='all prefix lengths; speed fixed, acceleration divided by ratio',
                profile_budget_box=bool(1 <= ratio <= 1.05),
                scope='The box flag only identifies the separately analysed reference range.')

        def prefix_profile(self, s):
            if self.cfg.get('ramp_law') != TAG:
                return original_profile(self, s)
            s = np.asarray(s)
            ratio = self._multistage_ratio
            t = np.mod(s, self.period)/ratio
            dtype = np.result_type(t, float)
            aa = np.empty_like(t, dtype=dtype)
            av = np.empty_like(t, dtype=dtype)
            acc = np.empty_like(t, dtype=dtype)
            starts = np.array([row[0] for row in self._multistage_segments])
            selected = np.clip(np.searchsorted(starts, t, side='right')-1,
                               0, len(starts)-1)
            for index, (start, length, v0, v1, area) in enumerate(self._multistage_segments):
                mask = selected == index
                if not np.any(mask):
                    continue
                u = np.clip((t[mask]-start)/length, 0., 1.)
                F, P, d = turn.turn_ramp(u, self._multistage_eta)
                dv = v1-v0
                aa[mask] = 1+ratio*(area+length*(v0*u+dv*P))
                av[mask] = v0+dv*F
                acc[mask] = dv*d/(ratio*length)
            return aa, av, acc

        PlanarSymmetryFlow.__init__ = flow_init
        PlanarSymmetryFlow.prefix_profile = prefix_profile
        PlanarSymmetryFlow._held10_multistage_flat_v1 = True

    adaptive.old.install_source = installer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-topic', type=Path, required=True)
    parser.add_argument('--dest', type=Path, required=True)
    args = parser.parse_args()
    source, dest = args.source_topic.resolve(), args.dest.resolve()
    if dest.exists() or source == dest or source in dest.parents:
        raise ValueError('Use a fresh source-copy directory outside the input source')
    original = source/'scripts/db6f-prefix-flat-profile.py'
    sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    original_sha = sha(original)
    shutil.copytree(source, dest, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    provider = dest/'scripts/held10_multistage_flat_profile.py'
    shutil.copyfile(__file__, provider)
    installed = dest/'scripts/db6f-prefix-flat-profile.py'
    with installed.open('a') as stream:
        stream.write('''\n# Explicit held10 tag; original flat/cosine dispatch is retained.\n_held10_original_flat_install = install\ndef install(adaptive):\n    _held10_original_flat_install(adaptive)\n    file = Path(__file__).with_name('held10_multistage_flat_profile.py')\n    spec = importlib.util.spec_from_file_location('held10_multistage_provider', file)\n    provider = importlib.util.module_from_spec(spec)\n    spec.loader.exec_module(provider)\n    provider.install(adaptive)\n''')
    report = dict(status='source_copy_ready', tag=TAG, source_topic=str(dest),
        reference_source_topic=str(source), original_flat_installer_sha256=original_sha,
        installed_flat_installer_sha256=sha(installed), provider_sha256=sha(provider),
        scope=__doc__, old_sources_modified=False, complete_surface=False)
    (dest/'multistage-profile-source.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
