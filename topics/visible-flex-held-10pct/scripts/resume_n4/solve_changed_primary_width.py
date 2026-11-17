#!/usr/bin/env python3
"""Solve a declared new raw n4 primary-core design at a fixed physical profile.

Changing the primary flattening width or lambda changes the complete core.
This is not refinement of the original core. All old physical controls,
including c8, initialize the new family; complete-map projection and an
explicit inlet repair are only an initial guess. The original equations,
linear physical port, exact lift, root/rho guards and terminal tests remain.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
from pathlib import Path
import shlex
import sys
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--loader', type=Path, required=True)
    parser.add_argument('--primary-transition', type=float, required=True)
    parser.add_argument('--homotopy', type=float)
    args, remainder = parser.parse_known_args()
    actual_command = shlex.join(sys.argv)
    sys.path.insert(0, str(args.loader.resolve()))
    import refine_fixed_raw_n4 as raw
    original_build = raw.build_seed

    def new_design_seed(source_topic, checkpoint, modes, angular=1280, **kwargs):
        seed = original_build(source_topic, checkpoint, modes, angular,
                              evaluate_boundary=False)
        oldobj, par, x, old_y = (seed[k] for k in ('obj', 'par', 'x', 'y'))
        rec = seed['record']
        if not rec.get('fixed_metric') or modes != rec['config']['modes']:
            raise ValueError('Use the complete same-mode fixed-g raw checkpoint for this new design')
        oldf = oldobj.flow(par[0])
        oldcore = oldobj._core
        previous_settings = dict(seed['settings'])
        settings = seed['settings']
        settings['transition'] = args.primary_transition
        if args.homotopy is not None:
            settings['homotopy'] = args.homotopy
        # This is the same dictionary captured by the original integral-core
        # factory. The old immutable core and its Flow reference remain intact.
        obj = seed['bvp_class'](seed['cfg'], seed['port'], seed['q_gauge'],
                                modes, angular, True, seed['q_gauge'])
        obj.pscale = oldobj.pscale.copy()
        obj.bcweights = oldobj.bcweights.copy()
        initial = obj.initial(par)
        f = obj.flow(par[0])
        if (obj._core.transition != args.primary_transition or
                obj._core.lam != settings['homotopy']):
            raise ValueError('New primary factory settings were not installed')
        if obj.cfg != oldobj.cfg or obj._core.bimodal_eta != oldcore.bimodal_eta:
            raise ValueError('The physical profile or eta changed')
        s, _ = obj.chart(x, par[0])
        old_s, _ = oldobj.chart(x, par[0])
        if abs(s - old_s).max() > 2e-13:
            raise ValueError('Changing the core width changed the meridian chart')
        N = max(4096, 128 * modes)
        B = f.basis(N)[0]
        old_B = oldf.basis(N)[0]
        y = np.empty_like(old_y)
        projection_error = 0.
        for first in range(0, len(x), 32):
            sl = slice(first, first + 32)
            previous = oldf.geo(s[sl], N)['pos'] + obj.q * oldf.values(old_y[:, sl], old_B)
            reference = f.geo(s[sl], N)['pos']
            y[:, sl] = f.project(previous - reference, B) / obj.q
            projection_error = max(projection_error, float(abs(
                reference + obj.q * f.values(y[:, sl], B) - previous).max()))
        repair = initial - y[:, 0]
        u = np.clip((s - .5 * f.prefix_end) / (.4 * f.prefix_end), 0., 1.)
        weight = f.profile(s)[0] * (1 - u ** 3 * (10 - 15 * u + 6 * u * u))
        y += repair[:, None] * weight[None, :]
        material = 2 * np.pi * np.arange(2048) / 2048
        before, after = oldcore.evaluate(material), obj._core.evaluate(material)
        changed = {key: float(abs(before[key] - after[key]).max())
                   for key in ('F', 'Ft', 'Ftt')}
        row = seed['diagnostics']
        old_identity = {key: row.pop(key) for key in
                        ('complete_core_identity_error', 'complete_map_projection_error',
                         'core_embedding', 'inlet_repair_max', 'seed_boundary_max')}
        row.update(scope=__doc__,
                   starting_checkpoint_embedding=old_identity,
                   new_primary_design=dict(
                       old_settings=previous_settings, new_settings=dict(settings),
                       all_physical_controls_preserved_initially=len(obj.pscale),
                       initial_c8=float(obj.pscale[0] * par[1]),
                       initial_actual_q=obj.support_amplitude,
                       changed_complete_material_core_jets=changed,
                       map_projection_before_repair_error=projection_error,
                       inlet_repair_coefficient_max=float(abs(repair).max()),
                       target_inlet_coefficient_error=float(abs(y[:, 0] - initial).max()),
                       initial_guess_angular_projection=N,
                       primary_transition=args.primary_transition,
                       wrapper_sha256=sha(__file__),
                       raw_driver_sha256=sha(args.loader / 'refine_fixed_raw_n4.py'),
                       actual_command=actual_command,
                       scope='A new complete primary design; no identity with the old core or convergence/refinement claim.'),
                   seed_boundary_max=float(abs(obj.bc(y[:, 0], y[:, -1], par)).max()),
                   boundary_evaluated=True)
        seed.update(obj=obj, par=par, x=x, y=y, diagnostics=row, settings=settings)
        return seed

    raw.module.build_seed = new_design_seed
    raw.module.__doc__ = __doc__
    previous_argv = sys.argv
    try:
        sys.argv = [str(Path(__file__))] + remainder
        raw.module.main()
    finally:
        sys.argv = previous_argv


if __name__ == '__main__':
    main()
