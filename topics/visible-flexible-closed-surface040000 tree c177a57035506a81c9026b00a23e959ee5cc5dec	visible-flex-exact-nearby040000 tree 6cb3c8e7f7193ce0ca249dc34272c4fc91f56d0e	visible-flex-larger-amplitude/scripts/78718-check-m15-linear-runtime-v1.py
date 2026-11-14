#!/usr/bin/env python3
"""Exercise new identity envelopes using original selectors, without a solver.

This fresh-process check installs the original Newton then explicitly selects
the original reviewed release-LU/direct-CSC function objects.  One CSC function
factory is called; no candidate, RHS, Jacobian matrix, LU, Newton, BVP or DN is
called. Original backend namespace references are restored before exit.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    c = module('restart8000_small_runtime_probe_driver', HERE / '78718-prefix-spectral-m15-linear-v1.py')
    audit = module('restart8000_small_runtime_probe_auditor', HERE / '78718-prefix-audit-m15-linear-v1.py')
    _, context = c.i.ancestor_context()
    import scipy.integrate._bvp as backend
    old_newton, old_prepare = backend.solve_newton, backend.prepare_sys
    record = {'schema': '78718-m15-linear-runtime-identity-check-v1',
              'status': 'STARTED_RUNTIME_IDENTITY_CHECK_ONLY', 'scope': __doc__,
              'checker': c.identity(__file__), 'driver': c.identity(c.i.RUNNER),
              'auditor': c.identity(c.i.AUDITOR), 'input_gate': c.identity(c.i.__file__),
              'typed_core': c.identity(c.i.CODE_CORE), 'ancestor': c.identity(c.i.ANCESTOR),
              'candidate_initializations': 0, 'RHS_calls': 0, 'Jacobian_matrices': 0,
              'LU_calls': 0, 'Newton_BVP_DN_calls': 0, 'CSC_function_factory_calls': 0,
              'newton_installations': 0, 'new_candidate_success': False}
    start = time.monotonic()
    code = 2
    try:
        original_path = Path(context['launch']['callbacks']['domain_solve_newton']['file']['path'])
        sys.path.insert(0, str(original_path.parent))
        import f6curve_domain_newton as original
        c.h.check_callback(original.install, context['launch']['callbacks']['domain_install'])
        original.install()
        record['newton_installations'] = 1
        record['newton_transition'] = c.select_runtime_newton(context)
        spectral = c.module('restart8000_small_uninvoked_spectral_module', c.HERE / 'db6f-root-spectral-collocation-v2.py')
        selected = c.select_runtime_csc(context, spectral)
        record['CSC_function_factory_calls'] = 1
        audit.check_csc_runtime_record(selected, context)
        record['selected_runtime'] = selected
        record['complete_live_code_functions'] = len(selected['canonical_functions'])
        negative = []
        for key in sorted(selected['canonical_functions']):
            changed = copy.deepcopy(selected)
            changed['canonical_functions'][key]['canonical_code_sha256'] = '0' * 64
            try:
                audit.check_csc_runtime_record(changed, context)
            except ValueError:
                negative.append(key)
            else:
                raise AssertionError('Typed closure modification was accepted: ' + key)
        record['canonical_closure_changes_rejected'] = negative
        restored = c.restore_runtime_csc(context)
        audit.check_csc_restoration(restored, context)
        record['restoration'] = restored
        record['status'] = 'PASS_COMPLETE_RUNTIME_IDENTITIES_AND_RESTORATION_ONLY'
        code = 0
    except Exception as exc:
        record.update(status='FAILED_RUNTIME_IDENTITY_CHECK', error=repr(exc), traceback=traceback.format_exc())
    finally:
        backend.prepare_sys = old_prepare
        backend.solve_newton = old_newton
        record['original_backend_references_restored'] = (backend.prepare_sys is old_prepare
                                                         and backend.solve_newton is old_newton)
    record['seconds'] = time.monotonic() - start
    raw = (json.dumps(record, indent=2, allow_nan=False) + '\n').encode()
    if len(raw) >= 1_000_000:
        raise ValueError('Unexpectedly large runtime identity record')
    with args.out.open('xb') as stream:
        stream.write(raw)
    print(json.dumps({'status': record['status'], 'seconds': record['seconds'],
        'complete_live_code_functions': record.get('complete_live_code_functions', 0),
        'canonical_closure_changes_rejected': len(record.get('canonical_closure_changes_rejected', [])),
        'report_bytes': len(raw), 'report_sha256': hashlib.sha256(raw).hexdigest(),
        'solver_calls': 0, **({'error': record['error']} if 'error' in record else {})}))
    return code


if __name__ == '__main__':
    sys.exit(main())
