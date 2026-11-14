#!/usr/bin/env python3
"""Publish bounded computed outputs with ordinary Git, preserving failures.

This publishes numerical evidence, never a claim that the research goal is
complete. Credentials live only in the child Git process environment.
"""
from __future__ import annotations
import argparse
import base64
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--results', type=Path, required=True)
    p.add_argument('--lane', choices=('m96', 'rk48', 'geometry', 'free3', 'material', 'coupling', 'couplingcheck', 'tailzero', 'tailzero112', 'prepare112', 'cardinal', 'gwcompat', 'circleprobe', 'gwvelocity', 'stage28', 'coupling112', 'coupling112banded', 'banddirection', 'coupling112physical', 'coupling112physicalqr', 'coupling112bridge', 'operatorcheck', 'coupling112trust', 'trustresume', 'coldtailprobe', 'trustprotected', 'zerorkprobe', 'trustmultiline', 'zerorkprobev2', 'zerorkprobev3', 'angledomain', 'nativeseed', 'angleprojection', 'sevenprojection', 'nativecorrection', 'observedseven', 'fullhprojection', 'nativeband', 'mixedquery', 'tenquery', 'nativeequilibrated', 'elevenquery', 'nativesplitprobe', 'twelvequery', 'nativesplitband', 'twelvequeryqr', 'rawcell0steps', 'rawcell0band', 'rawcell0gauge'), required=True)
    a = p.parse_args()
    if os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise RuntimeError('Results belong to the explicitly designated public repository')
    if not a.results.is_dir():
        print('No numerical output directory; no scientific execution is claimed.', flush=True)
        return 0
    repo = Path(__file__).resolve().parents[3]
    run = os.environ['GITHUB_RUN_ID']; attempt = os.environ['GITHUB_RUN_ATTEMPT']
    rel = Path('topics/visible-flex-larger-amplitude/notes') / ('public-actions-'+run+'-'+attempt+'-'+a.lane)
    dest = repo / rel; dest.mkdir(parents=True, exist_ok=True)
    rows = []
    for src in sorted(a.results.rglob('*')):
        if not src.is_file() or src.is_symlink():
            continue
        within = src.relative_to(a.results)
        row = dict(source=str(within), bytes=src.stat().st_size, sha256=sha(src))
        target = dest / within
        # These native radial point arrays are reproducible from the complete
        # accepted response/config and the pinned readout code. A new M112
        # readout has over 450 MB of raw points; Rule 10 keeps these large
        # intermediates in the already uploaded artifact, not in Git.
        radial_nodes = any(parent.endswith('-actual-tail-readout') and child == 'nodes'
                           for parent, child in zip(within.parts, within.parts[1:]))
        # Fixed optimizer B/J/Gamma arrays are reproducible large
        # intermediates. Keep their complete bytes in the uploaded Actions
        # artifact and their input/source/array hashes in the public manifest.
        domain_arrays = 'domain-operator' in within.parts and src.suffix == '.npz'
        if 'block-qr-inverse-arrays' in within.parts or 'block-qr-factor' in within.parts:
            row['not_published'] = ('Complete reproducible QR inverse evidence or optional factor bytes retained in the Actions artifact. '
                                    'The small public manifests and original-model readback reports bind every actual array and factor identity.')
            rows.append(row)
            continue
        if 'full-H-arrays' in within.parts:
            row['not_published'] = ('Complete reproducible full-model evidence and iteration-basis array retained in the Actions artifact. '
                                    'The public full-H manifest binds every compressed part, shape, dtype, raw-byte SHA and original model/source identity.')
            rows.append(row)
            continue
        if 'large-arrays' in within.parts:
            row['not_published'] = ('Complete reproducible native-model binary array retained in the Actions artifact. '
                                    'The public capture manifest records every chunk, original source/input identity, shape and raw-byte SHA.')
            rows.append(row)
            continue
        if domain_arrays:
            row['not_published'] = ('Reproducible full-angle optimizer row/factor array; retained in the Actions artifact. '
                                    'Regenerate from the actual warm, frozen source, original model settings and domain-operator manifest.')
            rows.append(row)
            continue
        if radial_nodes:
            row['not_published'] = ('Reproducible actual-tail radial point node; retained in the Actions artifact. '
                                    'Regenerate with the accepted response, original config, pinned source and stored readout intent.')
            rows.append(row)
            continue
        if src.stat().st_size > 1000000 and src.suffix in ('.json', '.jsonl', '.log'):
            content = gzip.compress(src.read_bytes(), mtime=0)
            target = target.with_name(target.name+'.gz')
            if len(content) < 5000000:
                target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(content)
            else:
                target = None
        elif src.stat().st_size < 5000000 and src.suffix not in ('.npy', '.dat'):
            target.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(src, target)
        else:
            target = None
        if target:
            row.update(published=str(target.relative_to(repo)), published_bytes=target.stat().st_size,
                       published_sha256=sha(target))
        else:
            row['not_published'] = 'Reproducible intermediate or exceeds single-file limit; retained as Actions artifact'
        rows.append(row)
    manifest = dict(scope=__doc__, recorded_at=datetime.now(timezone.utc).isoformat(),
                    source_commit=os.environ.get('GITHUB_SHA'), run_id=run, run_attempt=attempt,
                    lane=a.lane, files=rows, research_goal_completed=False,
                    run_url='https://github.com/Rogerhu12/math-research-public/actions/runs/'+run)
    manifest_bytes = (json.dumps(manifest, indent=2)+'\n').encode('utf-8')
    if len(manifest_bytes) > 1000000:
        compressed = gzip.compress(manifest_bytes, mtime=0)
        if len(compressed) >= 5000000:
            raise RuntimeError('Publication metadata exceeds the repository bound; original artifact remains available')
        (dest/'publication.json.gz').write_bytes(compressed)
    else:
        (dest/'publication.json').write_bytes(manifest_bytes)
    env = os.environ.copy()
    token = env['GH_TOKEN']
    config = [('credential.helper', ''), ('http.https://github.com/.extraheader', ''),
              ('http.https://github.com/.extraheader', 'AUTHORIZATION: basic '+base64.b64encode(('x-access-token:'+token).encode()).decode())]
    for i,(key,value) in enumerate(config):
        env['GIT_CONFIG_KEY_'+str(i)] = key; env['GIT_CONFIG_VALUE_'+str(i)] = value
    env['GIT_CONFIG_COUNT'] = str(len(config)); env['GIT_TERMINAL_PROMPT'] = '0'
    # Rebase creates commits too. A command-local identity only on `commit`
    # leaves the later `pull --rebase` unable to replay a concurrent result.
    env['GIT_AUTHOR_NAME'] = 'github-actions[bot]'
    env['GIT_AUTHOR_EMAIL'] = '41898282+github-actions[bot]@users.noreply.github.com'
    env['GIT_COMMITTER_NAME'] = env['GIT_AUTHOR_NAME']
    env['GIT_COMMITTER_EMAIL'] = env['GIT_AUTHOR_EMAIL']
    def git(*args, check=True):
        return subprocess.run(['git','-C',str(repo),*args], env=env, check=check)
    git('add','--sparse',str(rel))
    git('-c','user.name=github-actions[bot]','-c','user.email=41898282+github-actions[bot]@users.noreply.github.com',
        'commit','-m','visible-larger: preserve actual '+a.lane+' continuation '+run)
    while True:
        before = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], env=env, text=True).strip()
        git('pull','--rebase','origin','main')
        rule_diff = subprocess.check_output(
            ['git', '-C', str(repo), 'diff', before, 'origin/main', '--',
             'README.md', 'topics/visible-flex-larger-amplitude/README.md'],
            env=env, text=True)
        if rule_diff:
            print(rule_diff, flush=True)
            raise RuntimeError('README rules changed during synchronization; the root worker must read this diff and publish under the new rules. Computed artifacts are preserved.')
        result = subprocess.run(['git', '-C', str(repo), 'push', 'origin', 'HEAD:main'],
                                env=env, check=False, text=True, capture_output=True)
        print(result.stdout + result.stderr, flush=True)
        if result.returncode == 0:
            print('Published '+str(rel),flush=True)
            return 0
        # The user's instruction requires immediate ordinary rebase/push
        # until a non-fast-forward is resolved; no retry-count cutoff.
        failure = result.stdout + result.stderr
        concurrent_advance = (any(reason in failure for reason in ('non-fast-forward', 'fetch first', '[rejected]'))
            or ("cannot lock ref 'refs/heads/main'" in failure and ' is at ' in failure and ' but expected ' in failure))
        if not concurrent_advance:
            raise RuntimeError('Push failed for a reason other than concurrent main advancement; complete outputs remain in the artifact')


if __name__ == '__main__':
    raise SystemExit(main())
