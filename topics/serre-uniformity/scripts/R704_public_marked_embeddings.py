#!/usr/bin/env python3
"""Run the original-label R704 arithmetic on public Actions; retain receipts."""
import argparse
import datetime as dt
import gzip
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import traceback

from p41_public_actions_recovery import publish, read, sha, REPO, TOPIC


RESULT = 'R704-marked-p-split-embeddings'
CERTIFICATE = 'r704_marked_p_split_embeddings_certificate.json'


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)


def stop(signum, frame):
    raise InterruptedError('Received signal ' + str(signum))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['compute', 'publish', 'verify'])
    args = parser.parse_args()
    request_path = TOPIC / 'notes/R704-public-embedding-request.json'
    request = read(request_path)
    out = Path(os.environ['RUNNER_TEMP']) / 'serre-o6' / RESULT
    out.mkdir(parents=True, exist_ok=True)
    if args.mode == 'publish':
        return publish({'result': RESULT}, out, artifact_prefix='serre-o6')
    if args.mode == 'verify':
        summary = read(out / 'summary.json')
        certificate = out / CERTIFICATE
        return 0 if (summary['complete'] and certificate.exists()
                     and sha(certificate) == summary['certificate_sha256']) else 1

    source = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
    arithmetic = Path(__file__).with_name('build_r704_marked_p_split_embeddings.py')
    publisher = Path(__file__).with_name('p41_public_actions_recovery.py')
    workflow = REPO / '.github/workflows/serre-o6-marked-p-embeddings.yml'
    r191 = TOPIC / 'notes/r191_eta_ray_certificate.json'
    r305 = TOPIC / 'notes/r305_normal_integral_basis_certificate.json.gz'
    hashes = {
        'arithmetic_source_sha256': sha(arithmetic),
        'wrapper_source_sha256': sha(Path(__file__)),
        'publisher_source_sha256': sha(publisher),
        'workflow_source_sha256': sha(workflow),
        'request_sha256': sha(request_path),
        'R191_input_sha256': sha(r191),
        'R305_compressed_input_sha256': sha(r305),
        'root_readme_sha256': sha(REPO / 'README.md'),
        'topic_readme_sha256': sha(TOPIC / 'README.md'),
    }
    run_url = os.environ.get('GITHUB_SERVER_URL', 'https://github.com') + '/' + \
        os.environ.get('GITHUB_REPOSITORY', 'Rogerhu12/math-research-public') + \
        '/actions/runs/' + os.environ.get('GITHUB_RUN_ID', 'missing-run-id')
    initial = {
        'result': RESULT, 'source_commit': source,
        'source_repository': 'Rogerhu12/math-research-public',
        'request': request, 'run_url': run_url,
        'workflow_run_id': os.environ.get('GITHUB_RUN_ID'),
        'workflow_attempt': os.environ.get('GITHUB_RUN_ATTEMPT'),
        'prepared_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        **hashes,
    }
    save(out / 'public-actions-input.json', initial)
    # Preserve exact sources and complete inputs beside the unchanged math JSON.
    for path in (arithmetic, Path(__file__), publisher, workflow, request_path,
                 REPO / 'README.md', TOPIC / 'README.md', r191):
        name = ('root-README.md' if path == REPO / 'README.md' else
                'topic-README.md' if path == TOPIC / 'README.md' else path.name)
        (out / (name + '.gz')).write_bytes(gzip.compress(path.read_bytes(), mtime=0))
    shutil.copyfile(r305, out / r305.name)
    summary = {
        'result': RESULT, 'source_commit': source, 'run_url': run_url,
        'complete': False, 'computed_now': False, 'reused_from': None,
        'mathematical_certificate_format_changed': False,
        'actual_C_computed': False, 'actual_m_computed': False,
        **hashes,
    }
    save(out / 'summary.json', summary)
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    try:
        assert os.environ.get('GITHUB_ACTIONS') == 'true', 'Run this evaluator on public GitHub Actions.'
        assert os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public'
        assert request['result'] == RESULT and request['p'] == 43
        for key, expected in request['pinned_sha256'].items():
            assert hashes[key] == expected, (key, hashes[key], expected)
        certificate = out / CERTIFICATE
        previous = TOPIC / 'computations' / RESULT
        if request.get('reuse_existing_complete', False):
            for old_summary_path in sorted(previous.glob('*/summary.json')):
                old = read(old_summary_path)
                if not old.get('complete'):
                    continue
                if any(old.get(key) != hashes[key] for key in (
                    'arithmetic_source_sha256', 'R191_input_sha256',
                    'R305_compressed_input_sha256')):
                    continue
                old_certificate = old_summary_path.parent / old['certificate']
                assert sha(old_certificate) == old['certificate_sha256']
                shutil.copyfile(old_certificate, certificate)
                summary['reused_from'] = str(old_summary_path.relative_to(REPO))
                summary['reused_source_commit'] = old['source_commit']
                break
        if not certificate.exists():
            command = [sys.executable, '-u', str(arithmetic), '--r191', str(r191),
                       '--r305', str(r305), '--output', str(certificate)]
            save(out / 'command.json', {'argv': command, 'timeout_seconds': 600})
            with (out / 'public-actions-run.log').open('w') as stream:
                process = subprocess.run(command, cwd=REPO, stdout=stream,
                                         stderr=subprocess.STDOUT, timeout=600)
            summary['process_exit_code'] = process.returncode
            assert process.returncode == 0, 'Arithmetic process failed; its full output is retained.'
            summary['computed_now'] = True
        value = read(certificate)
        assert value['schema'] == 'R704-original-Gamma-p-split-embeddings-v1'
        assert value['p'] == 43 and value['modulus'] == 1849
        assert value['source_sha256']['R191'] == hashes['R191_input_sha256']
        assert value['source_sha256']['R305_compressed'] == hashes['R305_compressed_input_sha256']
        assert value['checks']['embedding_matrix_rank_mod_43'] == 43
        assert value['embedding_matrix_determinant'] == [687, 0]
        assert value['checks']['actual_C_computed'] is False
        assert value['checks']['actual_cs_or_cq_coordinates_computed'] is False
        expected = request.get('development_certificate_sha256')
        if expected:
            assert sha(certificate) == expected, 'Public result differs from the retained development bytes.'
        summary.update({
            'complete': True, 'certificate': CERTIFICATE,
            'certificate_sha256': sha(certificate),
            'embedding_count': 43, 'embedding_matrix_rank_mod_43': 43,
            'embedding_matrix_determinant': value['embedding_matrix_determinant'],
            'public_result_matches_development_bytes': bool(expected),
        })
    except BaseException as exc:
        summary['error'] = type(exc).__name__ + ': ' + str(exc)
        (out / 'failure.txt').write_text(traceback.format_exc())
    summary['finished_at_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    save(out / 'summary.json', summary)
    print(json.dumps(summary), flush=True)
    return 0 if summary['complete'] else 1


if __name__ == '__main__':
    sys.exit(main())
