#!/usr/bin/env python3
"""Run one explicitly reviewed held10 follow-up from a new frozen source tree.

This entry itself is included in the original worker snapshot.  A later unique
v3 request can call it after the previous owned session has ended.  The original
source tree and all existing numerical fields remain in place.  Only a fixed
public repository, an explicit commit, and a held10 Python entry are allowed.
The GitHub token is neither required nor accepted by any child command.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

TOPIC = 'topics/visible-flex-held-10pct'
PUBLIC_REPOSITORY = 'https://github.com/Rogerhu12/math-research-public.git'
RULES = ['README.md', TOPIC+'/README.md']


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def full_commit(value):
    if not re.fullmatch('[0-9a-f]{40}', value):
        raise argparse.ArgumentTypeError('An explicitly reviewed full 40-hex commit is required')
    return value


def write(path, value):
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original-repo', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--source-commit', type=full_commit, required=True)
    parser.add_argument('--reviewed-rules-commit', type=full_commit, required=True)
    parser.add_argument('--script', required=True)
    parser.add_argument('entry_args', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    original, work, out = (path.resolve() for path in
                           (args.original_repo, args.work, args.outdir))
    relative = Path(args.script)
    required_prefix = Path(TOPIC)/'scripts'
    if (relative.is_absolute() or '..' in relative.parts
            or required_prefix not in relative.parents or relative.suffix != '.py'):
        raise ValueError('The follow-up entry must be a held10 Python source')
    if (not original.is_dir() or not work.is_dir() or original == work
            or original in work.parents or work not in out.parents
            or original == out or original in out.parents or out.exists()):
        raise ValueError('Require an existing original source/work and an unused owned output directory')
    clean_env = {key:value for key,value in os.environ.items()
        if not any(word in key.upper() for word in ('TOKEN', 'SECRET', 'PASSWORD'))
        and not key.startswith('GIT_CONFIG_')
        and key not in ('PYTHONPATH', 'GIT_ASKPASS', 'SSH_ASKPASS')}
    clean_env.update(GIT_TERMINAL_PROMPT='0', PYTHONDONTWRITEBYTECODE='1')
    out.mkdir(exist_ok=False)
    state_path = out/'followup-entry.json'
    state = dict(schema='held10-explicit-frozen-followup-entry-v1',
        status='preparing_explicit_reviewed_source',
        started_utc=datetime.now(timezone.utc).isoformat(),
        helper_source=dict(path=str(Path(__file__).resolve()), sha256=sha(__file__)),
        original_repository=str(original), shared_numerical_work=str(work),
        source_commit_requested=args.source_commit,
        reviewed_rules_commit=args.reviewed_rules_commit,
        requested_script=args.script, public_repository=PUBLIC_REPOSITORY,
        public_fetch_without_credentials=True, numerical_arrays_uploaded=False,
        original_tree_or_existing_fields_rewritten_by_helper=False,
        original_source_labels_replaced=False, complete_surface=False)
    write(state_path, state)

    def git(directory, *arguments, check=True):
        command = ['git', '-c', 'credential.helper=',
                   '-c', 'http.extraheader=',
                   '-c', 'http.https://github.com/.extraheader=']
        if directory is not None:
            command += ['-C', str(directory)]
        command += list(arguments)
        result = subprocess.run(command, env=clean_env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode and check:
            raise RuntimeError('Public terminal git '+str(arguments[0])+' failed: '+result.stderr[-2500:])
        return result

    def require_commit(directory, value):
        if git(directory, 'cat-file', '-e', value+'^{commit}', check=False).returncode:
            git(directory, 'fetch', '--depth=1', '--filter=blob:none', '--no-tags', 'origin', value)
        if git(directory, 'cat-file', '-t', value).stdout.strip() != 'commit':
            raise ValueError('The explicit source/rules identifier must name a commit object')

    try:
        old_head = git(original, 'rev-parse', 'HEAD').stdout.strip()
        full_commit(old_head)
        state['original_source_commit'] = old_head
        source = out/('frozen-source-'+args.source_commit)
        # An independent partial clone does not update even the original
        # worktree's shared refs/index while its parent continues true pulls.
        git(None, 'clone', '--filter=blob:none', '--no-checkout', '--depth=1',
            '--single-branch', '--branch', 'main', PUBLIC_REPOSITORY, str(source))
        main_head = git(source, 'rev-parse', 'refs/remotes/origin/main').stdout.strip()
        full_commit(main_head)
        require_commit(source, args.source_commit)
        require_commit(source, args.reviewed_rules_commit)
        rules = {}
        for label, commit in [('actual_main', main_head), ('selected_source', args.source_commit)]:
            difference = git(source, 'diff', args.reviewed_rules_commit, commit,
                             '--', *RULES).stdout
            rules[label] = dict(commit=commit,
                difference_sha256=hashlib.sha256(difference.encode()).hexdigest(),
                unchanged=(not difference))
            if difference:
                state.update(status='unreviewed_rule_difference_no_child_started',
                    rule_checks=rules, difference=difference[:12000],
                    actual_main_commit=main_head)
                write(state_path, state)
                raise ValueError('Both actual main and selected source rules must match the explicit reviewed commit')
        git(source, 'sparse-checkout', 'set', '--cone', TOPIC)
        git(source, 'checkout', '--detach', args.source_commit)
        actual = git(source, 'rev-parse', 'HEAD').stdout.strip()
        if actual != args.source_commit:
            raise ValueError('The new numerical tree did not reach the explicit source commit')
        if git(source, 'symbolic-ref', '-q', 'HEAD', check=False).returncode != 1:
            raise ValueError('The new numerical tree must be detached')
        recovery = source/TOPIC/'scripts/nonlinear_tail/m3_coupled_seed_deliverable/m3_source_recovery_manifest.json'
        if recovery.is_file():
            for revision in sorted({row['revision'] for row in json.loads(recovery.read_text())['files']}):
                require_commit(source, full_commit(revision))
        files = []
        for name in git(source, 'ls-files', '-z').stdout.split('\0'):
            if not name:
                continue
            path = source/name
            if path.is_symlink() and source not in path.resolve().parents:
                raise ValueError('A checked-out source symlink leaves the new frozen tree')
            if path.is_file():
                files.append(dict(path=name, bytes=path.stat().st_size, sha256=sha(path)))
        manifest = out/'frozen-source-file-manifest.json'
        write(manifest, dict(commit=actual, files=files))
        entry = (source/relative).resolve()
        if (not entry.is_file() or (source/required_prefix).resolve() not in entry.parents):
            raise ValueError('The selected commit has no such held10 entry')
        raw_args = args.entry_args[1:] if args.entry_args[:1] == ['--'] else args.entry_args

        def substitute(value):
            if not isinstance(value, str) or '\0' in value or '\n' in value:
                raise ValueError('Follow-up arguments must be single-line strings')
            value = (value.replace('@ORIGINAL_REPO@', str(original))
                     .replace('@SOURCE_REPO@', str(source)).replace('@WORK@', str(work)))
            if '@REPO@' in value:
                raise ValueError('Use explicit ORIGINAL_REPO or SOURCE_REPO in the follow-up arguments')
            candidate = value.split('=', 1)[-1] if value.startswith('--') else value
            if '..' in Path(candidate).parts:
                raise ValueError('Parent path components are not accepted')
            if candidate.startswith('/'):
                path = Path(candidate).resolve()
                roots = (work, original/TOPIC, source/TOPIC)
                if (path not in (work, original, source)
                        and not any(path == root or root in path.parents for root in roots)):
                    raise ValueError('A follow-up argument leaves the owned held10 source/work scopes')
            return value

        command = [sys.executable, '-u', str(entry), *[substitute(value) for value in raw_args]]
        child_env = dict(clean_env, GITHUB_WORKSPACE=str(source))
        state.update(status='running_explicit_frozen_followup', actual_main_commit=main_head,
            rule_checks=rules, original_source_commit=old_head,
            frozen_numerical_source=dict(repository=str(source), commit=actual,
                tree=git(source, 'rev-parse', 'HEAD^{tree}').stdout.strip(), detached=True,
                partial_checkout=TOPIC, file_manifest=str(manifest),
                file_manifest_sha256=sha(manifest), checked_out_files=len(files),
                checked_out_file_bytes=sum(row['bytes'] for row in files)),
            command=command, entry_sha256=sha(entry),
            inherits_original_worker_owned_session=True,
            new_source_is_an_explicit_followup_not_a_relabel_of_old_execution=True)
        write(state_path, state)
        print(json.dumps(dict(event='explicit_frozen_followup_started', **state)), flush=True)
        # No start_new_session: v3's existing owned-session lifecycle includes
        # this entry and every ordinary numerical descendant.
        result = subprocess.run(command, cwd=source, env=child_env)
        for row in files:
            if sha(source/row['path']) != row['sha256']:
                raise ValueError('The explicitly frozen follow-up source changed during execution')
        if git(original, 'rev-parse', 'HEAD').stdout.strip() != old_head:
            raise ValueError('The original source identity changed during the follow-up')
        state.update(status='explicit_frozen_followup_process_returned',
            returncode=result.returncode, returned_utc=datetime.now(timezone.utc).isoformat(),
            frozen_source_manifest_rechecked=True, mathematical_acceptance_inferred=False)
        write(state_path, state)
        return result.returncode if result.returncode >= 0 else 128-result.returncode
    except BaseException as exc:
        state.update(status='explicit_frozen_followup_error',
            error=type(exc).__name__+': '+str(exc),
            mathematical_failure_inferred=False)
        write(state_path, state)
        raise


if __name__ == '__main__':
    raise SystemExit(main())
