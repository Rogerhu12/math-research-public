#!/usr/bin/env python3
"""Query a new R53 prefix and its own complete actual v2 finite tail as one map.

All saved Fourier/radial coefficients are literal parameters of the finite
map. Full Cartesian cut Hermite corrections, a central cylinder, the actual
deep zero-jet collar, reflected lower pieces and regular disks are explicit.
This is a geometry construction and sampled query, not a continuous metric,
reach, noncongruence, held-width or refinement certificate.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
from functools import lru_cache
from fractions import Fraction
import json
from pathlib import Path
import sys

import numpy as np

from actual_cartesian_prefix import SCRIPTS, load_actual_prefix, sha
sys.path.insert(0, str(SCRIPTS/'resume_20261126'))
from seam_export_tail_geometry_v2 import read, checked, ref, index_shared_nodes
from seam_tail_spectrum_v2 import validate_spectrum_container
from shared_jet import SharedJetQuintic
from m3_shared_prefix import CartesianCutLift, circle
from phase_angle_chart import PhaseAngleChart
from closed_m3_map import Background, ClosedM3Map, rotation


class ActualFiniteTailV2:
    """The complete saved v2 definition, with the same deep collar algebra.

    Radial knots of stages are exact binary reals. The inner collar knot is
    the exact real average of the literal deepest and cuff radii; longdouble
    arithmetic below is only its numerical evaluator.
    """
    def __init__(self, bundle_path, verified_index_path):
        self.bundle_path = Path(bundle_path).resolve()
        self.bundle = read(self.bundle_path)
        b = self.bundle
        if (b.get('status') != 'accepted_new_tail_shared_R_representation_exported'
                or b.get('geometry_schema') != 'actual-m3-native-tail-geometry-v2'
                or b.get('all_stages_exported') is not True
                or b.get('complete_finite_C2_stage_chain') is not True
                or b['height_identity']['factor'] != 1):
            raise ValueError('Use one complete unscaled actual v2 tail definition')
        if sha(b['source']['path']) != b['source']['sha256']:
            raise ValueError('The actual map exporter source changed')
        allowed = {SCRIPTS/'resume_20261126/seam_export_tail_geometry_v2.py',
                   SCRIPTS/'resume_20261126/seam_run_tail_geometry_v2.py'}
        if Path(b['source']['path']).resolve() not in allowed:
            raise ValueError('Unknown v2 map producer requires explicit review')
        self.manifest = checked(b['shared_R_manifest'])
        self.chain = checked(b['mean_chain'])
        self.packet = checked(b['accepted_packet'])
        saved_index = checked(b['canonical_node_index'])
        # Re-read each actual stage once to establish the complete shared-node
        # identity, without rerunning native integration or geometry proofs.
        current = index_shared_nodes(Path(b['shared_R_manifest']['path']),
            Path(b['mean_chain']['path']), Path(verified_index_path))
        if current != saved_index:
            raise ValueError('The complete v2 common-node index changed')
        self.index = current
        self.S = current['finite_stage_count']
        self.entries = {v['stage']: v for v in self.manifest['files']}
        if set(self.entries) != set(range(self.S)):
            raise ValueError('Every actual finite stage is required')
        self.spectrum = checked(self.manifest['spectrumContract'])
        validate_spectrum_container(self.manifest, self.spectrum)
        self.pm = np.asarray(self.spectrum['planar_modes'], int)
        self.hm = np.asarray(self.spectrum['height_modes'], int)
        self.P, self.C = len(self.pm), len(self.pm)+len(self.hm)
        self.parameters = self.manifest['physicalParameters']
        self.cuff = np.longdouble(self.parameters['rCuff'])
        ordered = sorted(current['unique_boundary_nodes'], key=lambda v: v['node'])
        self.boundaries = np.asarray([float(Fraction(v['R_exact_binary']))
                                      for v in ordered], float)
        if len(self.boundaries) != self.S+1 or np.any(np.diff(self.boundaries) >= 0):
            raise ValueError('Actual shared stage boundaries must decrease inward')
        cut, deep = self._data(0)['nodes'][-1], self._data(self.S-1)['nodes'][0]
        self.c, self.deep = np.longdouble(cut['radiusJS']), np.longdouble(deep['radiusJS'])
        self.inner = (self.deep+self.cuff)/2
        self.width = self.deep-self.inner
        self.cut_jets = np.asarray(cut['coefficients'], float)
        self.deep_jets = np.asarray(deep['coefficients'], np.longdouble)
        if (not 0 < self.cuff < self.inner < self.deep < self.c or
                deep['meanPerturbation'] != 0 or deep['meanBackground'] != 0):
            raise ValueError('Invalid actual deep zero-mean collar anchor')
        if cut['meanPerturbation'] != self.cut_jets[0, self.P]:
            raise ValueError('The complete original cut mean is absent')
        self.mean = float(self.cut_jets[0, self.P])

    @lru_cache(maxsize=4)
    def _data(self, stage):
        entry = self.entries[stage]
        data = checked(entry)
        validate_spectrum_container(data, self.spectrum, stage=True)
        if (data['stage'] != stage or data['boundInput'] != self.manifest['input']
                or data['sharing']['mapHash'] != entry['mapHash']):
            raise ValueError('Actual stage/map identity changed')
        return data

    @lru_cache(maxsize=4)
    def _rep(self, stage):
        nodes = self._data(stage)['nodes']
        knots = np.asarray([node['radiusJS'] for node in nodes], float)
        jets = np.transpose(np.asarray([node['coefficients'] for node in nodes], float), (1, 2, 0))
        return SharedJetQuintic(knots, jets)

    def coefficients(self, radius):
        r = np.longdouble(radius)
        if not 0 <= r <= self.c:
            raise ValueError('Outside the complete finite tail disk')
        if r <= self.inner:
            return np.zeros((3, self.C), np.longdouble)
        if r < self.deep:
            t, L = (r-self.inner)/self.width, self.width
            p = np.asarray([t**3*(10+t*(-15+6*t)),
                            t**3*(-4+t*(7-3*t)), t**3*(.5+t*(-1+.5*t))])
            d = np.asarray([30*t*t*(1-t)**2, t*t*(-12+t*(28-15*t)),
                            t*t*(1.5+t*(-4+2.5*t))])
            q = np.asarray([60*t*(1+t*(-3+2*t)), t*(-24+t*(84-60*t)),
                            t*(3+t*(-12+10*t))])
            weights = np.stack((p*np.asarray([1, L, L*L]),
                                d*np.asarray([1/L, 1, L]),
                                q*np.asarray([1/(L*L), 1/L, 1])))
            return weights@self.deep_jets
        if r == self.c:
            return self.cut_jets.copy()
        stage = int(np.searchsorted(-self.boundaries, -float(r), side='right')-1)
        stage = min(max(stage, 0), self.S-1)
        rep = self._rep(stage)
        return np.stack([rep(float(r), j) for j in range(3)])

    def fourier(self, coefficients, theta, order=0):
        theta = np.atleast_1d(np.asarray(theta, float))
        coefficients = np.asarray(coefficients, float)
        xy = (np.exp(1j*theta[:, None]*self.pm)*
              (1j*self.pm)**order)@coefficients[:self.P]
        angle = theta[:, None]*self.hm
        trig = np.cos(angle) if order == 0 else (-np.sin(angle) if order == 1 else -np.cos(angle))
        z = (trig*self.hm**order)@coefficients[self.P:]
        return np.stack((xy.real, xy.imag, z), axis=-1)

    def perturbation_jets(self, radius, theta):
        values = self.coefficients(radius)
        return tuple(self.fourier(values[i], [theta], j)[0]
                     for i, j in ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)))


class ActualCutTarget:
    """One whole Cartesian two-jet, shared by the prefix and tail."""
    def __init__(self, prefix, cap):
        self.prefix, self.cap = prefix, cap
        self.R, self.w = (float(cap.parameters[name]) for name in ('rCut', 'wCut'))
        self.wr = -7*self.w/self.R
        self.ap = -1/np.sqrt(1+self.w*self.w)
        self.app = -self.w*self.wr/(1+self.w*self.w)**2
        self.zcut = float(prefix.sol.mean_spline(prefix.flow.end)[0])
        self.c, self.mean, self.A = cap.c, cap.mean, cap.cut_jets

    def fourier(self, coefficient, psi, order=0):
        return self.cap.fourier(coefficient, psi, order)

    def angular_jets(self, psi):
        psi = np.atleast_1d(np.asarray(psi, float))
        flip = np.asarray([1., 1., -1.])
        answer = []
        for j in range(3):
            er = circle(psi, j)
            X = self.R*er+self.fourier(self.A[0], psi, j)*flip
            XR = er+self.fourier(self.A[1], psi, j)*flip
            XRR = self.fourier(self.A[2], psi, j)*flip
            if j == 0:
                X[:, 2] += self.zcut+self.mean
                XR[:, 2] -= self.w
                XRR[:, 2] -= self.wr
            answer.append(np.stack((X, self.ap*XR,
                self.ap*self.ap*XRR+self.app*XR)))
        return answer

    def perturbation_radius(self, R, width=.02):
        R = np.longdouble(R)
        delta = self.c-np.longdouble(self.R)
        u = np.clip((R-(np.longdouble(self.R)-width))/width, 0, 1)
        S = u**3*(10+u*(-15+6*u))
        Sp = 30*u*u*(1-u)**2/width
        Spp = 60*u*(1-u)*(1-2*u)/width**2
        r = self.c if R == self.R else R+delta*S
        return r, 1+delta*Sp, delta*Spp


class ActualClosedMapV2(ClosedM3Map):
    """Use the actual new prefix/tail with the explicit R23 atlas algebra."""
    def __init__(self, source_run, bundle, node_check, *, marker_strength=0.,
                 cylinder_half_length=0., cut_width=.04,
                 canonical_r67_marker=False):
        self.record, self.prefix = load_actual_prefix(source_run)
        self.cap = ActualFiniteTailV2(bundle, node_check)
        height_source = self.cap.bundle['height_identity']['reference']
        reference = checked(height_source)
        key = self.cap.bundle['height_identity']['reference_key']
        height = reference
        for part in key.split('.'):
            height = height[part]
        actual_height = self.record['raw_return']['candidate_H']
        if (height != actual_height or self.cap.packet['request']['height'] != actual_height
                or self.cap.packet['response']['checkpoint']['cutHeight'] != actual_height
                or self.cap.packet['config']['modes'] != self.prefix.M):
            raise ValueError('The complete tail is not the full actual source height')
        port = checked(self.cap.bundle['source_port'])
        if (port['parameters'] != self.record['physical_tail_parameters']
                or any(self.cap.parameters.get(k) != v for k, v in port['parameters'].items())):
            raise ValueError('The actual prefix and full tail use different physical metrics')
        self.target = ActualCutTarget(self.prefix, self.cap)
        self.prefix.end_lift = CartesianCutLift(self.prefix, self.target, cut_width)
        self.phase_chart = PhaseAngleChart(self.prefix)
        self.end = self.prefix.flow.end
        self.a, self.Rcut = float(self.cap.cuff), self.target.R
        self.cylinder_half_length = float(cylinder_half_length)
        if not 0 <= self.cylinder_half_length <= .005:
            raise ValueError('Use the recorded R54/R67 window: total cylinder length at most .01')
        if marker_strength != 0:
            raise ValueError('The old twofold marker strength is unsupported; select the canonical R67 threefold marker explicitly')
        self.marker_strength = 0.
        self.marker_radius = self.a/2
        self.r67_marker = None
        if canonical_r67_marker:
            from universal_threefold_marker import UniversalThreefoldMarker
            self.r67_marker = UniversalThreefoldMarker(self.marker_radius)
        native = checked(self.cap.bundle['native_record'])
        native_manifest = checked(native['manifest'])
        self.source_topic = Path(native_manifest['source_topic'])
        self.background = Background(self.source_topic,
                                     self.cap.bundle['accepted_packet']['path'])
        self.Zcap = (self.target.zcut+self.target.mean+
            self.background.sample(self.a)['heightFromRToCut'])

    def marker(self, x, y):
        if self.r67_marker is None:
            return 0., np.zeros(2), np.zeros((2, 2))
        return self.r67_marker.jets(float(x), float(y))

    def prefix_jets(self, s, theta, phase=0.):
        s = float(s)
        ell = self.cylinder_half_length
        if abs(s) > self.end+ell:
            raise ValueError('Outside the explicit cylinder/prefix atlas')
        if ell and abs(s) <= ell:
            core = self.prefix.core.evaluate(np.asarray([theta-phase]))
            X = core['F'][0].copy()
            X[2] = s
            jets = (X, np.asarray([0., 0., 1.]), np.zeros(3),
                    core['Ft'][0], core['Ftt'][0], np.zeros(3))
            return tuple(rotation(v, phase) for v in jets)
        sign = 1 if s >= 0 else -1
        result = list(super().prefix_jets(sign*(abs(s)-ell), theta, phase))
        result[0] = result[0]+np.asarray([0., 0., sign*ell])
        return tuple(result)

    def tail_jets(self, R, theta, side=1, phase=0.):
        result = list(super().tail_jets(R, theta, side, phase))
        result[0] = result[0]+np.asarray([0., 0., side*self.cylinder_half_length])
        return tuple(result)

    def disk_jets(self, x, y, side=1):
        X, J, H = super().disk_jets(x, y, side)
        X = X+np.asarray([0., 0., side*self.cylinder_half_length])
        return X, J, H


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in ('source-run', 'geometry-bundle', 'out'):
        ap.add_argument('--'+key, type=Path, required=True)
    ap.add_argument('--cylinder-half-length', type=float, default=0.)
    ap.add_argument('--marker-strength', type=float, default=0.)
    ap.add_argument('--canonical-r67-marker', action='store_true',
                    help='Attach only the reviewed universal threefold R67 marker at its canonical positive amplitude')
    ap.add_argument('--cut-width', type=float, default=.04)
    a = ap.parse_args()
    repo = SCRIPTS.parents[2]
    out = a.out.resolve()
    if out == repo or repo in out.parents:
        raise ValueError('Complete new-map query data must remain outside git')
    out.parent.mkdir(parents=True, exist_ok=True)
    node_check = out.with_name(out.stem+'-verified-node-index.json')
    model = ActualClosedMapV2(a.source_run, a.geometry_bundle, node_check,
        marker_strength=a.marker_strength, cylinder_half_length=a.cylinder_half_length,
        cut_width=a.cut_width, canonical_r67_marker=a.canonical_r67_marker)
    maximum, center, rows = np.zeros(6), np.zeros(6), []
    try:
        end = model.end+model.cylinder_half_length
        for phase in (0., .17, np.pi/3):
            for side in (-1, 1):
                for theta in (0., .123, 1.1, 2.4, 4.7):
                    P = model.prefix_jets(side*end, theta, phase)
                    T = model.tail_jets(model.Rcut, theta, side, phase)
                    ap0, app = model.target.ap, model.target.app
                    shared = (T[0], side*ap0*T[1], ap0*ap0*T[2]+app*T[1],
                              T[3], T[4], side*ap0*T[5])
                    maximum = np.maximum(maximum,
                        [np.linalg.norm(x-y) for x, y in zip(P, shared)])
                    if model.cylinder_half_length:
                        ell = model.cylinder_half_length
                        on = model.prefix_jets(side*ell, theta, phase)
                        # The limiting prefix jets at its exact shared core.
                        off = list(ClosedM3Map.prefix_jets(model, side*0., theta, phase))
                        off[0] += np.asarray([0., 0., side*ell])
                        center = np.maximum(center,
                            [np.linalg.norm(x-y) for x, y in zip(on, off)])
                radii = (0., model.a, float(model.cap.inner), float(model.cap.deep),
                         .08, .2, model.Rcut)
                for R in radii:
                    jets = model.tail_jets(R, .34, side, phase)
                    if not all(np.all(np.isfinite(v)) for v in jets):
                        raise FloatingPointError('Nonfinite new closed-map tail jet')
                    rows.append(dict(phase=phase, side=side, R=R,
                                     point=np.asarray(jets[0], float).tolist()))
        report = dict(scope=__doc__, source_sha256=sha(__file__),
            source_run=ref(a.source_run), geometry_bundle=ref(a.geometry_bundle),
            full_node_check=ref(node_check), modes=model.prefix.M,
            source_homotopy=model.record['core_settings']['homotopy'],
            complete_finite_stage_count=model.cap.S,
            full_source_height_identity_checked=True,
            source_tail_is_actual_coupled=False,
            shared_cut_six_jet_sampled_errors=maximum.tolist(),
            central_cylinder_six_jet_sampled_errors=center.tolist(),
            cylinder_half_length=model.cylinder_half_length,
            marker_strength=model.marker_strength,
            canonical_r67_marker=a.canonical_r67_marker,
            canonical_marker_metadata=(model.r67_marker.metadata()
                                       if model.r67_marker is not None else None),
            canonical_marker_source=(ref(Path(__file__).with_name('universal_threefold_marker.py'))
                                     if model.r67_marker is not None else None),
            source_mean_replaced_by_declared_new_shared_interpolant=True,
            cut_width=a.cut_width,
            tail_cut_radius_reparameterization_delta=float(model.cap.c-model.Rcut),
            cap_height_without_cylinder_approx=float(model.Zcap),
            upper_pole_height_approx=float(model.Zcap+model.cylinder_half_length),
            phase_chart=model.phase_chart.report(),
            background_query=model.background.info,
            finite_queries_all_finite=True, tail_sampled_points=len(rows),
            actual_new_finite_closed_map_constructed=True,
            exact_C2_definition='Shared literal two-jets, full Cartesian Hermite lifts, reflected core/cylinder, actual deep zero-jet collar, and regular disks; smooth real R53 core/background integral definitions.',
            continuous_metric_certificate=False, reach_certificate=False,
            delta_E_proved=False, held_set_gate_proved=False,
            fixed_problem_convergence_proved=False, README_completion=False)
        out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
        out.with_name(out.stem+'-points.json').write_text(json.dumps(rows, indent=2)+'\n')
        print(json.dumps(report, indent=2, allow_nan=False))
    finally:
        model.close()


if __name__ == '__main__':
    main()
