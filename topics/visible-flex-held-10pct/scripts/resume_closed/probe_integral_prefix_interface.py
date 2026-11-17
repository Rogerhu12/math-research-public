#!/usr/bin/env python3
"""Non-solution probe of the actual integral reference interface.

This deliberately sets the finite unknown to its constant inlet projection
and the mean height to s.  It is not a BVP solution or an accepted checkpoint.
The sole purpose is to detect omission/double addition of the installed
source reference and errors in its complete two-jet/export interface.
"""
import argparse
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace

from m3_integral_prefix import (
    module, round_core_type, M3SharedPrefix, M3IntegralCartesianPrefix,
    SharedJetQuintic, ROUND, sha, PAIRS)
import numpy as np


def norm(value):
    return float(np.linalg.norm(value, axis=-1).max())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'short-bridge', 'profile', 'chart', 'port', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--library', type=Path, default=ROUND)
    parser.add_argument('--q', type=float, default=.085)
    parser.add_argument('--homotopy', type=float, default=1.)
    parser.add_argument('--modes', type=int, default=8)
    parser.add_argument('--angular', type=int, default=256)
    parser.add_argument('--radial', type=int, default=129)
    args = parser.parse_args()
    started = time.monotonic()
    source = args.source_topic
    adaptive = module('probe_integral_adaptive', source/'scripts/950f-prefix-adaptive-chart-bvp-v2.py')
    module('probe_integral_flat', source/'scripts/db6f-prefix-flat-profile.py').install(adaptive)
    adaptive.old.install_source(source/'repro/source-root')
    module('probe_integral_short', args.short_bridge).install()
    settings = dict(halfwidth=.21, transition=.08, control_transition=.16,
                    homotopy=args.homotopy, center=np.pi/3, bimodal_eta=0.,
                    lock_fundamental=True, coefficient_precision=80,
                    positivity_grid_max=32768)
    Core = round_core_type(args.library)
    __import__('fixed_metric_mode3_core').PlanarSupportCore = lambda q, corrections=(), base_mode=3: Core(
        q, corrections, base_mode, arc_nodes=1024, **settings)
    chart = json.loads(args.chart.read_text())
    Flow, BaseBVP = adaptive.build_classes(chart)
    original_geo = Flow.geo
    from exact_core_lift import install_core_lift
    BVP = install_core_lift(Flow, BaseBVP)
    profile, port = [json.loads(path.read_text()) for path in (args.profile, args.port)]
    port['cut']['_prefix_bridge'] = profile['prefix_bridge']
    obj = BVP(profile, port, args.q, args.modes, args.angular, True, args.q)
    parameters = np.zeros(args.modes)
    initial = obj.initial(parameters)
    flow = obj.flow(0.)
    nodes = np.unique(np.r_[np.linspace(0, flow.end, args.radial), flow.breaks])
    data = np.zeros((3, len(initial), len(nodes)))
    data[0] = initial[:, None]
    representative = SharedJetQuintic(nodes, data)
    mean = SharedJetQuintic(nodes, np.stack((nodes, np.ones_like(nodes),
                                            np.zeros_like(nodes)))[:, None, :])
    sol = SimpleNamespace(x=nodes, y=representative(nodes), p=parameters,
                          sol=representative, mean_spline=mean)
    model = M3IntegralCartesianPrefix(obj, flow, sol)
    raw_source = M3SharedPrefix(obj, flow, sol)
    psi = 2*np.pi*np.arange(args.angular)/args.angular
    names = ('pos', 's1', 's2', 'p1', 'p2', 'sp')
    single = {key: 0. for key in (*names, 'spp')}
    sizes = dict(single)
    nodal = dict.fromkeys(names, 0.)
    for first in range(0, len(model.rep.x), 16):
        s = model.rep.x[first:first+16]
        geometry = flow.geo(s, args.angular)
        before = original_geo(flow, s, args.angular)
        angular = model.reference_angular_jets(psi)
        radial = model.source_lift_radial_jets(s)
        reference = model.reference_correction(s, psi, source_radial=True)
        checks = list(zip(names, reference))
        checks.append(('spp', radial[1, :, None, None]*angular[2][None, :, :]))
        for key, term in checks:
            actual = geometry[key]-before[key]
            single[key] = max(single[key], norm(actual-term))
            sizes[key] = max(sizes[key], norm(actual))
        actual, _ = raw_source.raw_grid(s, args.angular)
        finite = model.raw_evaluate(s, psi)
        for key, a, b in zip(names, actual, finite):
            nodal[key] = max(nodal[key], norm(a-b))
    X, Xs, Xss, Xp, Xpp, Xsp = [v[0] for v in model.evaluate([0.], psi)]
    theta, rho, rhop, ts, tss, rhos = model.angular(0., psi)
    v, vp, vs = ts/rho, (rhos*rho-ts*rhop)/rho**2, (tss*rho-ts*rhos)/rho**2
    ez = np.zeros_like(X)
    ez[:, 2] = 1.
    center = dict(
        X=norm(X-model.core.evaluate(theta)['F']),
        Fs=norm(Xs-v[:, None]*Xp-ez),
        Fss=norm(Xss-2*v[:, None]*Xsp+v[:, None]**2*Xpp+(v*vp-vs)[:, None]*Xp))
    cutoff = dict(reference_last_two_jet_max=float(abs(model.lift_rep.jets[:, 0, -1]).max()),
                  reference_off_region_two_jet_max=float(abs(
                      model.lift_rep.jets[:, 0, model.rep.x >= model.lift_window[1]]).max()))
    scale = max(1., max(sizes.values()))
    # Engineering checks only.  These detect complete omission/double count
    # for this nonzero high-homotopy source reference; no geometric gate uses
    # these tolerances.
    assert max(single.values()) < 2e-11*scale, single
    assert max(nodal.values()) < 2e-10*scale, nodal
    assert max(center.values()) < 2e-11, center
    assert max(cutoff.values()) == 0., cutoff
    assert sizes['pos'] > 1e-7, 'The probe cannot detect a missing reference term'
    result = dict(
        scope=__doc__, command=sys.argv, accepted_solution=False, bvp_solves=0,
        settings=settings, q=args.q, modes=args.modes, angular=args.angular,
        radial_knots=len(model.rep.x), definition=model.definition_record(),
        actual_source_reference_sizes=sizes,
        single_reference_source_identity_errors=single,
        raw_finite_source_nodal_errors=nodal, center_identity_errors=center,
        cutoff_identity=cutoff, all_engineering_checks_passed=True,
        source_sha256={str(p.resolve()): sha(p) for p in (
            Path(__file__), Path(__file__).with_name('m3_integral_prefix.py'),
            args.short_bridge, args.profile, args.chart, args.port,
            source/'scripts/950f-prefix-adaptive-chart-bvp-v2.py',
            source/'scripts/db6f-prefix-flat-profile.py', *sorted(args.library.glob('*.py')))},
        seconds=time.monotonic()-started)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in (
        'accepted_solution', 'all_engineering_checks_passed',
        'single_reference_source_identity_errors', 'raw_finite_source_nodal_errors',
        'center_identity_errors', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()
