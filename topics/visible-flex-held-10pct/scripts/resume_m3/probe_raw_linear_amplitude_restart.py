#!/usr/bin/env python3
"""Finite initial-guess check for the linear raw-control amplitude predictor.

Use an existing finite accepted raw prefix.  This does not run a BVP, call a
nonlinear tail, or certify the complete metric.  The declared amplitude changes
the physical design, even though the seed profile and angular chart are reused.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import gzip
import json
from pathlib import Path
import sys
import numpy as np
from couple_m3_smallcut_secant import accepted_anchor
from m3_raw_diagnostic_model import RawDiagnosticEnvironment, sha
from install_endpoint_c2_restart import install as install_c2
from install_raw_linear_amplitude_restart import install as install_linear


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'short-bridge', 'restart', 'linear-port', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--amplitude', type=float, required=True)
    p.add_argument('--nodes', type=int, default=257)
    a = p.parse_args()
    rec = json.loads(gzip.decompress(a.restart.read_bytes()))
    accepted_anchor(rec, a.restart)
    if rec.get('core_control_path') != 'raw-mean-primary-compact-v1':
        raise ValueError('The predictor is intended for physical raw compact controls')
    if not np.isfinite(a.amplitude) or a.amplitude <= 0:
        raise ValueError('The new amplitude must be finite and positive')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    port = json.loads(a.linear_port.read_text()); port['_sha256'] = sha(a.linear_port)
    env = RawDiagnosticEnvironment(a.source_topic, a.short_bridge, rec['chart'],
                                   rec['core_round_settings'])
    class SharedC2(env.BVP):
        pass
    class LinearC2(env.BVP):
        pass
    c2_path = a.out.with_name(a.out.stem+'-c2-seed.json')
    linear_path = a.out.with_name(a.out.stem+'-linear-seed.json')
    old_metadata = install_c2(SharedC2, c2_path)
    new_metadata = install_linear(LinearC2, linear_path)
    def make(cls):
        obj = cls(rec['frozen_profile'], port, a.amplitude, rec['config']['modes'],
                  rec['config']['angular'], False, rec['warp_reference_q'])
        obj.restart_remesh = a.nodes
        return obj
    oldobj, newobj = make(SharedC2), make(LinearC2)
    to, yo, po = oldobj.restart(a.restart)
    tn, yn, pn = newobj.restart(a.restart)
    if not np.array_equal(to, tn) or po[0] != pn[0]:
        raise AssertionError('The common mesh or delta initialization changed')
    co, cn = po[1:]*oldobj.pscale, pn[1:]*newobj.pscale
    previous = np.asarray(rec['parameters'][1:])*np.asarray(rec['central_correction_scales'])
    ratio = a.amplitude/rec['actual_primary_amplitude']
    target = previous*ratio
    expected_old = previous*ratio**np.arange(2, rec['config']['modes']+1)
    conversion_error = float(np.max(abs(cn-target)))
    if conversion_error > 8*np.finfo(float).eps*max(float(np.max(abs(target))), 1e-300):
        raise AssertionError('Physical coefficient gauge conversion does not match linear scaling')
    newf = newobj.flow(pn[0]); s, _ = newobj.chart(tn, pn[0])
    u = np.clip((s-.5*newf.prefix_end)/(.4*newf.prefix_end), 0., 1.)
    window = newf.profile(s)[0]*(1-u**3*(10-15*u+6*u*u))
    oldin, newin = oldobj.initial(po), newobj.initial(pn)
    predicted_difference = (newin-oldin)[:, None]*window[None, :]
    inlet_difference_error = float(np.max(abs((yn-yo)-predicted_difference)))
    exterior = s >= .9*newf.prefix_end
    if not np.array_equal(yn[:, exterior], yo[:, exterior]):
        raise AssertionError('Changing the control predictor affected the field outside the repair window')
    Ho = oldobj.bridge.sigma*oldobj.q*yo[oldobj.iz:, -1]
    Hn = newobj.bridge.sigma*newobj.q*yn[newobj.iz:, -1]
    if not np.array_equal(Ho, Hn):
        raise AssertionError('The control-only predictor changed the initial tail height')
    sources = {**env.sources, str(Path(__file__).resolve()):sha(__file__)}
    for name in ('install_raw_linear_amplitude_restart.py', 'install_endpoint_c2_restart.py'):
        path = Path(__file__).with_name(name); sources[str(path)] = sha(path)
    result = dict(scope=__doc__, command=sys.argv, source_sha256=sources,
        checkpoint=dict(path=str(a.restart.resolve()), sha256=sha(a.restart),
            finite_solver_success=rec['solver_success'],
            full_metric_scope='No full-metric acceptance is inferred from accepted_anchor.'),
        coefficient_chunks={str(f.resolve()):sha(f) for f in sorted(
            a.restart.parent.glob(a.restart.name.split('.')[0]+'_coeff_*.npy.gz'))},
        physical_port=dict(path=str(a.linear_port.resolve()),sha256=sha(a.linear_port)),
        q_old_gauge=rec['gauge_amplitude'], q_old_actual=rec['actual_primary_amplitude'],
        q_new_gauge=a.amplitude, q_new_actual=newobj.support_amplitude,
        physical_amplitude_ratio=ratio, modes=newobj.M, nodes=len(tn),
        core_settings=dict(rec['core_round_settings']),
        old_c2_source=old_metadata, new_linear_c2_source=new_metadata,
        physical_controls_old=previous.tolist(),
        physical_controls_original_power_predictor=co.tolist(),
        physical_controls_linear_predictor=cn.tolist(),
        original_power_formula_error=float(np.max(abs(co-expected_old))),
        linear_formula_error=conversion_error,
        tail_initial_height_identical=True,
        field_outside_C2_repair_identical=True,
        field_difference_vs_inlet_repair_formula_error=inlet_difference_error,
        common_delta_parameter=float(pn[0]),
        initial_numerical_rho_lower=dict(original_power=oldobj._core.rho_lower,
            linear=newobj._core.rho_lower),
        seed_records={str(c2_path.resolve()):sha(c2_path),
            str(linear_path.resolve()):sha(linear_path)},
        conclusion='This finite probe verifies the intended physical coefficient scaling and '
            'unchanged material field outside the shared repair. No full-domain Frenet/metric '
            'check or new amplitude solution has been claimed; the running lambda-one job '
            'does not import this installer.')
    a.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out), ratio=ratio, modes=newobj.M,
        nodes=len(tn), linear_formula_error=conversion_error,
        field_difference_formula_error=inlet_difference_error,
        initial_rho_lower=result['initial_numerical_rho_lower'])), flush=True)


if __name__ == '__main__':
    main()
