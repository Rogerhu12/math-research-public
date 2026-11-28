#!/usr/bin/env python3
"""Original lambda-zero BVP with complete analytic support-control columns.

This independent entry delegates to the complete CSR/lifecycle/checkpoint
driver.  It installs the checked original PlanarSupportCore coefficient jets
immediately after the original exact core lift.  The original additive-delta
centered difference, every RHS/state column, boundary, mesh, domain, tolerance
and physical audit remain in force.  No core-factory attribute is fabricated.
The existing V5 positive-material delta hook is deliberately not invoked.
"""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path[:0] = [str(HERE), str(HERE.parent/'design'),
               str(SCRIPTS/'resume_m3/round_raw_lib')]
import prefix_chord_checkpoint_driver as base
import planar_support_exact_parameter_jets as jets
import analytic_adaptive_core_jac as analytic
import exact_core_lift as lift

# The existing full-QR driver must intercept this exact original loader.
previous = base.previous


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    command = list(sys.argv)
    if '--help' in command or '-h' in command:
        return base.main()
    required = ('--core-module', '--core-config', '--raw-restart', '--outdir')
    if any(flag not in command for flag in required) or '--tail-config' in command:
        raise ValueError('Require the original lambda-zero raw design and linear-port problem')
    paths = {flag:Path(command[command.index(flag)+1]).resolve() for flag in required}
    if paths['--core-module'] != SCRIPTS/'resume_m3/material_support_factory.py':
        raise ValueError('This entry requires the original material-support factory source')
    settings = json.loads(paths['--core-config'].read_text())
    if float(settings.get('homotopy', 0.)) != 0.:
        raise ValueError('This independent analytic entry is restricted to lambda zero')
    out = paths['--outdir']
    files = [Path(__file__).resolve(), Path(base.__file__).resolve(),
             Path(jets.__file__).resolve(), Path(analytic.__file__).resolve(),
             Path(lift.__file__).resolve(), *paths.values()]
    files.remove(out)
    record = dict(kind='original_lambda_zero_complete_support_jacobian_execution_v1',
        scope=__doc__, actual_command=command,
        source_hashes={str(path):sha(path) for path in files},
        core_settings=settings, installations=[],
        complete_support_controls_retained=True,
        additive_delta_column='original centered difference, unchanged',
        positive_material_delta_adapter_called=False,
        no_missing_factory_attribute_fabricated=True,
        original_residual_boundary_domain_mesh_and_acceptance_changed=False,
        numerical_support_parameter_derivative_changed=True,
        original_run_label_changed=False, accepted_BVP_claimed=False,
        complete_surface=False)
    original_lift = lift.install_core_lift
    original_installer = analytic.install
    original_jets = analytic.parameter_jets

    def save():
        if out.is_dir():
            (out/'zero-planar-support-analytic-execution.json').write_text(
                json.dumps(record, indent=2, allow_nan=False)+'\n')

    def install(Flow, BVP, window=(.5,.9)):
        if record['installations']:
            raise RuntimeError('The lambda-zero analytic hook was unexpectedly installed twice')
        factory = __import__('fixed_metric_mode3_core').PlanarSupportCore
        if hasattr(factory, 'jet_parameter_derivatives'):
            raise ValueError('The actual source no longer takes the original lambda-zero branch')
        provider = sys.modules['portable_m3_custom_core']
        core = provider.OriginalSupportCore
        core_path = Path(sys.modules[core.__module__].__file__).resolve()
        record['actual_original_core_source'] = dict(path=str(core_path), sha256=sha(core_path))
        result = original_lift(Flow, BVP, window)
        record['installations'].append(jets.install(result, analytic,
            window=window, original_installer=original_installer))
        save()
        return result

    lift.install_core_lift = install
    try:
        result = base.main()
        if len(record['installations']) != 1:
            raise RuntimeError('The original portable model did not execute the analytic support hook')
        record['delegate_returned'] = True
        return result
    except BaseException as exc:
        record['delegate_exception'] = dict(type=type(exc).__name__, text=str(exc))
        raise
    finally:
        lift.install_core_lift = original_lift
        analytic.parameter_jets = original_jets
        # V5 owns and restores analytic.install in its own finally block.
        record['owned_hook_restored'] = lift.install_core_lift is original_lift
        record['parameter_jets_restored'] = analytic.parameter_jets is original_jets
        record['original_installer_restored'] = analytic.install is original_installer
        save()


if __name__ == '__main__':
    main()
