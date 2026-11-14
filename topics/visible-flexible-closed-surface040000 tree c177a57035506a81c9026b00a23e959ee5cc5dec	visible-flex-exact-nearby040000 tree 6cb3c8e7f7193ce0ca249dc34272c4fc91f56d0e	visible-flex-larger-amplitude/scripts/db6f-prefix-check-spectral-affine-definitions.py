#!/usr/bin/env python3
"""Check actual callback definitions without constructing any prefix or solver.

Only module/class definitions are loaded. In particular the original
source installer, domain Newton installer, flow/prefix constructors,
restart initializer, spectral solver factory and BVP/DN are never called.
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--launch', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    helper_path = HERE / 'db6f-prefix-spectral-affine-replay.py'
    spec = importlib.util.spec_from_file_location('spectral_definition_check_helpers', helper_path)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    h.require(not args.out.exists(), 'Do not overwrite a closed definition check')
    launch = h.read(args.launch)
    rec, _, _ = h.validate_inputs(launch)
    import scipy.integrate._bvp as scipy_bvp
    before_newton = scipy_bvp.solve_newton
    sys.path.insert(0, str(Path(launch['source_root']) / 'topics/large-amplitude-twist-flex/scripts'))
    runner = h.module('spectral_definition_check_original', HERE / 'db6f-prefix-flat-coupled.py').m
    Flow, Base = runner.adaptive.build_classes(rec['chart'])  # Class definitions only.
    class BVP(runner.TailMixin, Base):
        pass
    initializer = h.module('spectral_definition_check_restart', HERE / 'db6f-prefix-preserve-restart.py')
    from curve_stable_prefix_bvp import save_checkpoint
    import f6curve_domain_newton as domain_newton
    functions = {'fun': BVP.fun, 'fun_jac': BVP.fun_jac, 'bc': BVP.bc,
                 'bc_jac': BVP.bc_jac, 'terminal': BVP.terminal, 'initial': BVP.initial,
                 'chart': BVP.chart, 'physical_fun': Flow.adapt_fun,
                 'physical_fun_jac': Flow.adapt_fun_jac,
                 'physical_c2_interpolant': Flow.adapt_c2_interpolant,
                 'affine_dn': runner.AffineTailForInnerBVP.solve,
                 'restart': initializer.restart, 'save_checkpoint': save_checkpoint,
                 'domain_install': domain_newton.install,
                 'domain_solve_newton': domain_newton.solve_newton}
    checks = {name: h.check_callback(fn, launch['callbacks'][name]) for name, fn in functions.items()}
    h.require(scipy_bvp.solve_newton is before_newton, 'Definition-only check changed the active Newton')
    report = {'status': 'PASS_DEFINITIONS_ONLY', 'scope': __doc__, **h.FLAGS,
              'checker': h.identity(Path(__file__)), 'helper': h.identity(helper_path),
              'launch': h.identity(args.launch), 'callback_count': len(checks), 'callbacks': checks,
              'scipy_newton_unchanged': True, 'actual_prefix_flow_bridge_constructors': 0,
              'actual_restart_calls': 0, 'actual_domain_install_calls': 0,
              'actual_spectral_solver_factory_calls': 0, 'actual_BVP_DN_calls': 0,
              'runtime_installed_newton_check': 'Still unpaid here; the future actual runner checks it after install().'}
    h.write_json(args.out, report, exclusive=True)
    print(json.dumps({'status': report['status'], 'callback_count': len(checks), **h.identity(args.out)}))


if __name__ == '__main__':
    main()
