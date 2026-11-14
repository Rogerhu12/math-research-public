#!/usr/bin/env python3
"""Explicit compact scalar neck profiles after the verified R225 entrance.

This is a geometry/design screen for a(s), not a nonlinear R225 surface.
The first .9 units exactly retain the verified entrance law. All following
seams preserve a,a',a''. Background sizes and curvatures do not certify the
nonaxis surface, the G witness, the closed diameter, or continuous reach.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np

P = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('geometry_compact_neck_provider', P/'alternative-neck-provider.py')
neck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(neck)


DEFAULT = dict(entry_length=.9, entry_speed=.3, entry_acceleration=.2,
               entry_coast=0., middle_speed=-.6, first_turn_curvature=3.2,
               descent_speed=-.98, second_turn_curvature=7.5,
               sync_curvature=2., loop_radius=.35, loop_ratio=1.1,
               loop_speed=.985, loop_curvature=7.5, terminal_peak_fraction=.1)


class CompactNeck(neck.Pieces):
    def __init__(self, cfg):
        super().__init__(1.)
        self.cfg = dict(cfg)
        self.append(dict(kind='hermite', length=cfg['entry_length'],
                         k0=cfg['entry_acceleration'], v1=cfg['entry_speed']))
        self.coast(self.aend+cfg['entry_speed']*cfg['entry_coast'], cfg['entry_speed'])
        self.turn_begin = self.end
        self.append(neck.fl.turn(math.asin(cfg['entry_speed']), math.asin(cfg['middle_speed']), cfg['first_turn_curvature']))
        self.first_turn_end = self.end
        self.append(neck.fl.turn(math.asin(cfg['middle_speed']), math.asin(cfg['descent_speed']), cfg['second_turn_curvature']))
        self.second_turn_end = self.end
        sync = neck.fl.turn(math.asin(cfg['descent_speed']), -math.asin(cfg['loop_speed']), cfg['sync_curvature'])
        self.coast(cfg['loop_radius']-sync['dr'], cfg['descent_speed'])
        self.append(sync)
        self.loop_begin = self.end
        self.append(neck.fl.turn(-math.asin(cfg['loop_speed']), math.asin(cfg['loop_speed']), cfg['loop_curvature']))
        self.coast(cfg['loop_ratio']*cfg['loop_radius'], cfg['loop_speed'])
        self.append(neck.fl.turn(math.asin(cfg['loop_speed']), -math.asin(cfg['loop_speed']), cfg['loop_curvature']))
        self.coast(cfg['loop_radius'], -cfg['loop_speed'])
        self.Tu = cfg['entry_length']
        self.Td = self.end-self.Tu
        self.period = self.end


def partial_height(seg, u):
    u = np.asarray(u)
    if seg['kind'] in ('hermite', 'boost'):
        v = neck.velocity(seg, u[..., None]*neck.base.gu)
        return seg['length']*u/2*(np.sqrt(1-v*v) @ neck.base.gw)
    return seg['length']*neck.fl.integral(seg, u, 'cos')


def screen(cfg, port, background, samples=401):
    prefix = CompactNeck(cfg)
    bridge_cfg = dict(loop_radius=cfg['loop_radius'], loop_speed=cfg['loop_speed'],
                      loop_curvature=cfg['loop_curvature'], terminal_peak_fraction=cfg['terminal_peak_fraction'])
    bridge = neck.NeckTerminalBridge(neck.tagged_port(port, bridge_cfg)['cut'])
    maximum_norm = 0.
    maximum_kappa = 0.
    rows = []
    for label, obj, zoffset, soffset in [('prefix', prefix, 0., 0.), ('bridge', bridge, prefix.height, prefix.end)]:
        for index, seg in enumerate(obj.segments):
            u = np.linspace(0, 1, samples)
            radius, velocity, acceleration = neck.piece_jet(seg, u)
            height = zoffset+seg['h0']+partial_height(seg, u)
            beta = np.sqrt(1-velocity*velocity)
            curvature = np.maximum(abs(acceleration)/beta, beta/radius)
            norms = np.hypot(radius, height)
            maximum_norm = max(maximum_norm, float(norms.max()))
            maximum_kappa = max(maximum_kappa, float(curvature.max()))
            rows.append(dict(part=label, index=index, kind=seg['kind'],
                             s0=soffset+seg['s0'], s1=soffset+seg['s1'],
                             radius_min=float(radius.min()), radius_max=float(radius.max()),
                             height_min=float(height.min()), height_max=float(height.max()),
                             background_kappa_sample=float(curvature.max()),
                             twice_background_norm_sample=2*float(norms.max())))
    source_h = np.asarray(background['nodeHeightInnerAnchor'])
    radii = np.array([background['rows'][0]['points'][-1]['r']]+[r['points'][0]['r'] for r in background['rows']])
    if len(source_h) != len(radii):
        raise ValueError('Background node dimensions differ')
    cut_height = prefix.height+bridge.height
    tail_height = cut_height+source_h[0]-source_h
    finite_tail_norm = np.hypot(radii, tail_height)
    maximum_norm = max(maximum_norm, float(finite_tail_norm.max()))
    tail_kappa = 0.
    for row in background['rows']:
        for point in row['points']:
            w, wr, r = point['w'], point['wr'], point['r']
            tail_kappa = max(tail_kappa, abs(wr)/(1+w*w)**1.5, w/(r*math.sqrt(1+w*w)))
    maximum_kappa = max(maximum_kappa, tail_kappa)
    return dict(config=cfg, prefix_segments=prefix.segments, bridge_segments=bridge.segments,
                prefix_length=prefix.end, bridge_length=bridge.end,
                turn_begin=prefix.turn_begin, first_turn_end=prefix.first_turn_end,
                second_turn_end=prefix.second_turn_end, loop_begin=prefix.loop_begin,
                prefix_background_height=prefix.height,
                bridge_background_height=bridge.height,
                original_finite_tail_background_height=float(source_h[0]),
                height_through_original_finite_tail=float(tail_height[-1]),
                original_inner_radius=float(radii[-1]),
                twice_maximum_background_norm_through_finite_tail_sample=2*maximum_norm,
                background_kappa_sample=maximum_kappa,
                background_kappa_times_twice_norm_sample=maximum_kappa*2*maximum_norm,
                segment_rows=rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--background', type=Path, required=True)
    ap.add_argument('--port', type=Path, required=True)
    ap.add_argument('--config', type=Path)
    ap.add_argument('--sweep', action='store_true')
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    raw = a.background.read_bytes()
    background = json.loads(gzip.decompress(raw) if a.background.suffix == '.gz' else raw)
    port = json.loads(a.port.read_text())
    cfg = dict(DEFAULT)
    if a.config:
        cfg.update(json.loads(a.config.read_text()))
    configs = [cfg]
    if a.sweep:
        configs = [dict(cfg, first_turn_curvature=k1, second_turn_curvature=k2, entry_coast=coast)
                   for coast in (0., .05) for k1 in (2.8, 3., 3.2, 3.5, 4.) for k2 in (6., 7.5)]
    full = [screen(c, port, background) for c in configs]
    fields = ('config', 'prefix_length', 'bridge_length', 'turn_begin', 'first_turn_end',
              'second_turn_end', 'loop_begin', 'prefix_background_height',
              'bridge_background_height', 'original_finite_tail_background_height',
              'height_through_original_finite_tail', 'original_inner_radius',
              'twice_maximum_background_norm_through_finite_tail_sample',
              'background_kappa_sample', 'background_kappa_times_twice_norm_sample')
    report = dict(scope=__doc__, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  original_background_sha256=hashlib.sha256(raw).hexdigest(),
                  original_background_source_sha256=background['source_sha256'],
                  port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest(),
                  source_profile_fingerprint=background['original_profile_fingerprint'],
                  configurations=[{k:r[k] for k in fields} for r in full],
                  selected=screen(cfg, port, background),
                  caveats=['Only the scalar background and fixed source background tail are evaluated.',
                           'The actual R225 field has not been continued through this profile.',
                           'This is neither the complete closed D nor a reach or G witness certificate.',
                           'The remaining infinite tail/caps and all t remain to be handled.'])
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:report['selected'][k] for k in fields}))


if __name__ == '__main__':
    main()
