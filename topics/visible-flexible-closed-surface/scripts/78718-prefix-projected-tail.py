#!/usr/bin/env python3
"""Keep the original prefix equations, with a wider true finite tail.

The physical height request is E(H)=(H,0). The prefix sees P T_W(EH) and
P DT_W(EH) E. Complete W responses remain in the original packet files and
the saved seam. High-mode slope/two-jet gaps are not asserted to vanish; the
actual full-mode common-cut construction and its continuous bounds pay them.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time
from types import SimpleNamespace

import numpy as np


class ProjectedTailPort:
    def __init__(self, port, prefix_modes):
        self.port = port
        self.M = prefix_modes
        self.W = port.M
        if not 0 < self.M <= self.W:
            raise ValueError('Prefix modes must be covered by the actual tail')
        self.last_full_response = None

    def __getattr__(self, name):
        return getattr(self.port, name)

    @property
    def linearD(self):
        return self.port.linearD[:self.M]

    def solve(self, height, jacobian=True, audit=False):
        h = np.asarray(height, float)
        if h.shape != (self.M,) or not np.all(np.isfinite(h)):
            raise ValueError('Wrong prefix height request')
        embedded = np.zeros(self.W)
        embedded[:self.M] = h
        full = self.port.solve(embedded, jacobian=jacobian, audit=audit)
        self.last_full_response = full
        jets = {key: value[:self.M] if isinstance(value, list) else value
                for key, value in full['jets'].items()}
        jac = full['heightJetJacobian']
        if jac is not None:
            # Original full rows: slope W, second W, meanSlope, meanSecond,
            # height W. Retain both scalar mean rows; columns right-multiply E.
            rows = np.r_[np.arange(self.M), self.W+np.arange(self.M),
                         2*self.W, 2*self.W+1, 2*self.W+2+np.arange(self.M)]
            jac = np.asarray(jac).reshape(3*self.W+2, self.W)[rows, :self.M]
            jac = jac.ravel().tolist()
        return {**full, 'jets': jets, 'heightJetJacobian': jac}

    def close(self):
        self.port.close()


def main(runner):
    """Original coupled main, with explicit projected client and full seam.

All flow/BC/audit/outer/Newton functions are the existing runner objects.
The original main assumes equal mode orders in one check and in its client;
this entry makes those two assumptions explicit without changing the flow.
"""
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-root', 'profile', 'chart', 'linear-port', 'tail-config',
                'out-prefix', 'restart'):
        p.add_argument('--'+key, type=Path, required=True)
    for key, default in (('amplitude', .08), ('warp-reference', .08),
                         ('tol', 2e-7), ('bc-tol', 1e-7), ('physical-bc-tol', 2e-9)):
        p.add_argument('--'+key, type=float, default=default)
    for key, default in (('modes', 8), ('angular', 256), ('audit-angular', 512),
                         ('nodes', 601), ('max-nodes', 2400), ('node-heap', 1536)):
        p.add_argument('--'+key, type=int, default=default)
    for key in ('fixed', 'probe-only', 'lagged-tail', 'preserve-restart-mesh'):
        p.add_argument('--'+key, action='store_true')
    p.add_argument('--warmup-scales', type=float, nargs='*', default=[.1,.2,.4,.6,.8,1.])
    a = p.parse_args()
    adaptive = runner.adaptive
    adaptive.old.install_source(a.source_root)
    from curve_stable_prefix_bvp import save_checkpoint
    from f6curve_domain_newton import install, STATS
    cfg = json.loads(a.profile.read_text())
    chart = json.loads(a.chart.read_text())
    port = json.loads(a.linear_port.read_text())
    port['_sha256'] = hashlib.sha256(a.linear_port.read_bytes()).hexdigest()
    tcfg = json.loads(a.tail_config.read_text())
    for k, v in port['parameters'].items():
        if tcfg.get(k) != v:
            raise ValueError('Physical tail parameter mismatch: '+k)
    if tcfg['modes'] < a.modes or tcfg['spacing'] != 3:
        raise ValueError('True tail does not cover prefix modes')
    _, Base = adaptive.build_classes(chart)
    class BVP(runner.TailMixin, Base):
        pass
    o = BVP(cfg, port, a.amplitude, a.modes, a.angular, a.fixed, a.warp_reference)
    o.restart_remesh = a.nodes
    o.bcweights = np.full(o.M, a.physical_bc_tol/a.bc_tol)
    restart_info = None
    if a.preserve_restart_mesh:
        initializer = runner.module('projected_saved_mesh', runner.S/'db6f-prefix-preserve-restart.py')
        x, y, par, restart_info = initializer.restart(o, a.restart, chart)
    else:
        x, y, par = o.restart(a.restart)
    tail = None
    begin = time.time()
    summary = {'scope': __doc__, 'solver_success': False,
               'tail_config_sha256': hashlib.sha256(a.tail_config.read_bytes()).hexdigest()}
    try:
        active = runner.module('projected_actual_client', runner.S/'db6f-prefix-tail-shared-client.py')
        full = active.WeightedTailPort(a.tail_config, a.source_root,
                                     a.out_prefix.with_name(a.out_prefix.name+'_tail'), node_heap=a.node_heap)
        tail = ProjectedTailPort(full, o.M)
        o.tail = tail
        summary['linear_dn_ready_max_difference'] = float(abs(tail.linearD-np.asarray(port['linearSlope'][:o.M])).max())
        H = o.bridge.sigma*o.q*y[o.iz:, -1]
        for scale in a.warmup_scales:
            request = H*np.asarray(scale)**np.arange(1, o.M+1)
            response = tail.solve(request, jacobian=False, audit=True)
            print(json.dumps({'event': 'tail_warmup', 'scale': scale,
                              'converged': response['converged'], 'shoot': response['residual']}), flush=True)
        if a.probe_only:
            response = tail.solve(H, jacobian=True, audit=True)
            summary.update(probe_only=True, tail_converged=response['converged'],
                tail_shooting_residual=response['residual'], tail_calls=tail.calls)
            return
        install()
        print(json.dumps({'event': 'start_coupled', 'q': a.amplitude, 'prefix_modes': o.M,
                          'tail_modes': tail.W, 'nodes': len(x), 'fixed': a.fixed}), flush=True)
        sol, outer_checks = runner.solve_with_actual_tail(o, tail, x, y, par, a)
        f = o.flow(sol.p[0])
        o.initial(sol.p)
        physical = SimpleNamespace(x=o.chart(sol.x, sol.p[0])[0], y=sol.y, p=sol.p)
        physical.sol = f.c2_interpolant(physical)
        frozen = cfg if a.fixed else {**cfg, 'delta': cfg['delta']+sol.p[0]}
        out = dict(scope=__doc__, angular_chart='frozen-spline-adaptive-v1', chart=chart,
            warp_reference_q=a.warp_reference,
            config=dict(modes=o.M, tail_modes=tail.W, base_mode=3,
                core_kind='adaptive_warped_support', angular=o.nt, tol=a.tol,
                bc_tol=a.bc_tol, physical_bc_tol=a.physical_bc_tol,
                fixed_metric=a.fixed, actual_nonlinear_tail=True),
            frozen_profile=frozen, gauge_amplitude=o.q,
            actual_primary_amplitude=o.support_amplitude, meridian_length=f.end,
            physical_port_sha256=port['_sha256'], physical_tail_parameters=port['parameters'],
            physical_tail_cut=port['cut'], tail_config=tcfg,
            parameters=sol.p.tolist(), central_correction_scales=o.pscale.tolist(),
            nodes=len(sol.x), solver_success=bool(sol.success), message=sol.message,
            max_rms_collocation_residual=float(np.max(sol.rms_residuals)),
            newton_domain_audit=dict(STATS), mesh=physical.x.tolist(), pp_coefficients=physical.sol.c)
        out['dn_solver'] = 'outer_actual_inner_affine' if a.lagged_tail else 'actual_dn_at_every_query'
        out['actual_outer_checks'] = outer_checks
        out['restart_mesh_diagnostics'] = restart_info
        cp = a.out_prefix.with_suffix('.json.gz')
        save_checkpoint(cp, out)
        out['summary'] = adaptive.audit(o, physical, a.audit_angular)
        out['tail_seam'] = o.seam_audit(physical)
        j = tail.last_full_response['jets']
        out['tail_seam'].update(full_tail_jets=j, prefix_boundary_modes=o.M, tail_modes=tail.W,
            projection='Request E(H)=(H,0); response P T_W(EH); Jacobian P DT_W(EH) E.',
            high_height_slope_max=float(np.max(np.abs(j['slope'][o.M:]), initial=0.)),
            high_height_second_max=float(np.max(np.abs(j['second'][o.M:]), initial=0.)),
            high_modes_paid_by_prefix_BC=False,
            full_XYZ_seam_requires_actual_common_cut_and_continuous_bound=True)
        out['seconds'] = time.time()-begin
        out['tail_calls'] = tail.calls
        save_checkpoint(cp, out)
        summary = {k: v for k, v in out.items() if k not in ('mesh', 'pp_coefficients')}
        print(json.dumps({'event': 'result', 'success': out['solver_success'],
            'prefix_modes': o.M, 'tail_modes': tail.W, 'metric': out['summary']['metric_l1'],
            'tail_calls': tail.calls}), flush=True)
    except Exception as exc:
        summary.update(error=repr(exc), tail_calls=tail.calls if tail else 0)
        print(json.dumps({'event': 'failure', 'error': repr(exc)}), flush=True)
    finally:
        if tail:
            tail.close()
        summary['seconds'] = time.time()-begin
        a.out_prefix.with_name(a.out_prefix.name+'-summary.json').write_text(json.dumps(summary, indent=2)+'\n')
