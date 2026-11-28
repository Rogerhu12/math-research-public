#!/usr/bin/env python3
"""Resume once the original .016 bootstrap has genuinely paid all its gates.

The retained original bootstrap finishes in its own output tree.  This process
waits for its complete terminal summary, verifies the actual accepted fields,
and then starts a separate original complete-lift secant controller.  Lower
lambda stages are not recomputed.  A supplied earlier source is always another
genuinely accepted field, never an unaccepted predictor or a metric-only return.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'bootstrap-summary', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    repo, work, bootstrap, out = (p.resolve() for p in
        (args.repo, args.work, args.bootstrap_summary, args.outdir))
    if (repo == work or repo in work.parents or work not in out.parents
            or work not in bootstrap.parents):
        raise ValueError('The actual sources and fields must stay in work outside Git')
    handoff = out.with_name(out.name+'-handoff.json')
    if out.exists() or handoff.exists():
        raise FileExistsError(out if out.exists() else handoff)
    here = Path(__file__).resolve().parent
    dispatcher = here/'run_design_qr_dispatch.py'
    state = dict(scope=__doc__, status='waiting_for_actual_original_bootstrap',
        bootstrap_summary=str(bootstrap), output=str(out),
        began_utc=datetime.now(timezone.utc).isoformat(),
        source_hashes={str(p): sha(p) for p in (Path(__file__).resolve(), dispatcher)},
        earlier_accepted_lambda_recomputed=False, original_equations_changed=False,
        original_acceptance_gates_changed=False, complete_surface=False)

    def save():
        temporary = handoff.with_suffix('.tmp')
        temporary.write_text(json.dumps(state, indent=2)+'\n')
        temporary.replace(handoff)

    save()
    terminal_failures = {'design_requires_more_modes', 'design_continuation_step_failed',
                         'design_entry_error'}
    while True:
        try:
            record = json.loads(bootstrap.read_text())
        except (FileNotFoundError, json.JSONDecodeError):
            record = {}
        status = record.get('status')
        if status == 'declared_finite_design_stages_passed':
            break
        if status in terminal_failures:
            state.update(status='source_bootstrap_returned_without_required_terminal',
                actual_source_status=status, actual_source_error=record.get('error'),
                bootstrap_summary_sha256=sha(bootstrap))
            save()
            return 2
        time.sleep(5)
    if record.get('result', {}).get('accepted_lambda') != .016:
        raise ValueError('The original bootstrap did not finish at its declared .016')
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    sys.path[:0] = [str(scripts/'resume_20261126'), str(scripts/'resume_m3')]
    from material_design_secant_predictor import accepted_original, same_design_contract
    right_path = Path(record['result']['run']).resolve()
    right, _ = accepted_original(right_path, repo)
    if right['core_settings']['homotopy'] != .016:
        raise ValueError('The genuine terminal field has a different lambda')
    left_option = []
    left_identity = None
    eligible = [row for row in record['stages'] if row.get('accepted') is True
                and row['homotopy'] < .016 and row['modes'] <= right['modes']]
    if eligible:
        row = max(eligible, key=lambda value: (value['homotopy'], value['modes']))
        left_path = Path(row['run']).resolve()
        left, _ = accepted_original(left_path, repo)
        if left['modes'] == right['modes']:
            same_design_contract(left, right)
        left_option = ['--previous-run', str(left_path)]
        left_identity = dict(run=str(left_path), sha256=sha(left_path),
                             homotopy=left['core_settings']['homotopy'],
                             modes=left['modes'])
    command = [sys.executable, '-u', str(dispatcher), '--controller', 'lifted-secant',
        '--qr-min-modes', '40', '--qr-rhs-block', '8', '--repo', str(repo),
        '--work', str(work), '--source-run', str(right_path), *left_option,
        '--outdir', str(out), '--targets', '.032', '.064', '.128', '.256', '.512',
        '.75', '1', '--mode-levels', '24', '32', '40', '48', '64', '80', '96', '128']
    state.update(status='executing_original_complete_lift_secant_with_qr_dispatch',
        bootstrap_summary_sha256=sha(bootstrap), actual_left=left_identity,
        actual_right=dict(run=str(right_path), sha256=sha(right_path),
                          homotopy=.016, modes=right['modes']),
        command=command, numerical_linear_arithmetic_changed_at_M_ge_40=True)
    save()
    result = subprocess.run(command, cwd=repo)
    state.update(status='original_secant_controller_returned', returncode=result.returncode)
    summary = out/'summary.json'
    if summary.is_file():
        returned = json.loads(summary.read_text())
        state.update(actual_continuation_status=returned.get('status'),
            actual_continuation_result=returned.get('result'), summary_sha256=sha(summary))
    save()
    return result.returncode


if __name__ == '__main__':
    sys.exit(main())
