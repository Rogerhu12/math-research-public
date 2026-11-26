#!/usr/bin/env python3
"""Actual new Cauchy INITIAL, original observer, independent complete Cartesian LM.

Recovered text after the 11:20 UTC executor loss. No lost checkpoint or
unpublished controller identity is reused. Numerical source is frozen before
the first pull; only scalar receipts are committed, never the raw arrays.
"""
from __future__ import annotations
import argparse, datetime, hashlib, json, os, re, shutil, subprocess, sys, time
from pathlib import Path

TOPIC = Path('topics/visible-flexible-closed-surface')
H = TOPIC/'HANDOFF.md'
RULES = [Path('README.md'), TOPIC/'README.md']
MARKER = '<!-- 6a65-cartesian-cold-ci-rules -->'
CANDIDATE = TOPIC/'notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json'

def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda: stream.read(1048576), b''):
            digest.update(part)
    return digest.hexdigest()

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def emit(event, **values):
    print(json.dumps(dict(event=event, **values), allow_nan=False), flush=True)

def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')

class RulesChanged(RuntimeError):
    pass

class Controller:
    def __init__(self, args):
        self.repo = Path(__file__).resolve().parents[3]
        self.out = args.directory.resolve()
        if self.out.exists():
            raise FileExistsError('A fresh cold temporary directory is required')
        if self.out == self.repo or self.repo in self.out.parents:
            raise ValueError('Raw numerical files must remain outside Git')
        self.out.mkdir(parents=True)
        self.run_id = os.environ['GITHUB_RUN_ID']
        self.attempt = os.environ.get('GITHUB_RUN_ATTEMPT', '1')
        self.epoch = os.environ['GITHUB_SHA']
        if not re.fullmatch('[0-9a-f]{40}', self.epoch):
            raise ValueError('Actual frozen public commit required')
        if self.git('rev-parse', 'HEAD', capture=True).strip() != self.epoch:
            raise ValueError('Actual trigger checkout mismatch')
        self.last_rules = self.epoch
        self.request_rel = args.request.relative_to(self.repo) if args.request.is_absolute() else args.request
        if self.request_rel.parts[:3] != (TOPIC/'ci-requests').parts:
            raise ValueError('Request must belong to this topic')
        self.request = json.loads((self.repo/self.request_rel).read_text())
        if self.request.get('schema') != '6a65-independent-Cartesian-new-zero-Cauchy-cold-request-v1':
            raise ValueError('Explicit new-input request required')
        self.git_env = os.environ.copy()
        self.git_env.update(GIT_TERMINAL_PROMPT='0', GIT_CONFIG_COUNT='2',
            GIT_CONFIG_KEY_0='credential.helper', GIT_CONFIG_VALUE_0='',
            GIT_CONFIG_KEY_1='credential.helper',
            GIT_CONFIG_VALUE_1='!f() { printf "username=x-access-token\\npassword=%s\\n" "$CART_COLD_TOKEN"; }; f')
        self.child_env = os.environ.copy()
        for name in list(self.child_env):
            if name in ('GH_TOKEN', 'GITHUB_TOKEN', 'CART_COLD_TOKEN', 'M12_RECOVERY_TOKEN', 'VISIBLE_FLEX_TOKEN') or name.startswith('GIT_CONFIG_'):
                self.child_env.pop(name, None)
        self.child_env.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
        self.git('config', 'user.name', 'Astra-visible-flex-6a65')
        self.git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
        self.frozen = self.out/'frozen'
        self.frozen.mkdir()
        entries = subprocess.check_output(['git', 'ls-files', '-z', '--', str(TOPIC)], cwd=self.repo).split(b'\0')
        inventory = []
        for entry in entries:
            if not entry:
                continue
            rel = Path(entry.decode())
            target = self.frozen/rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(self.repo/rel, target)
            inventory.append(dict(path=str(rel), sha256=sha(target), bytes=target.stat().st_size))
        inventory_path = self.out/'frozen-source-inventory.json'
        write(inventory_path, inventory)
        self.scripts = self.frozen/TOPIC/'scripts'
        self.candidate = self.frozen/CANDIDATE
        if sha(self.candidate) != self.request['candidateSHA256']:
            raise ValueError('Candidate changed')
        baseline_recipe = self.frozen/TOPIC/self.request['cauchyRecipe']
        self.recipe = self.frozen/TOPIC/self.request['cartesianRecipe']
        if sha(baseline_recipe) != self.request['cauchyRecipeSHA256']:
            raise ValueError('Original Cauchy physical recipe changed')
        if sha(self.recipe) != self.request['cartesianRecipeSHA256']:
            raise ValueError('Independent Cartesian recipe changed')
        config = json.loads(baseline_recipe.read_text())['config']
        if any(key in config for key in ('z', 'schema', 'source', 'baseline', 'evaluation', 'interfaceProbeOnly')):
            raise ValueError('Cold source must be the explicit new no-z configuration')
        config['independentColdNewInput'] = dict(
            definition='Original factory initialVector from public recipe.config; no checkpoint coefficients copied or inferred.',
            publicRecipeSHA256=sha(baseline_recipe), publicSourceEpoch=self.epoch,
            sameAsLiveStrongCheckpoint=False, inheritedAcceptedSteps=0)
        self.config = self.out/'new-zero-config.json'
        write(self.config, config)
        self.initial = self.out/'new-zero-initial.json'
        self.observer = self.out/'new-zero-observer.json'
        self.prefix = self.out/'cartesian'
        self.target = self.repo/TOPIC/'notes'/f'2026-11-26-6a65-cartesian-cold-{self.run_id}-{self.attempt}.json'
        self.record = dict(schema='6a65-independent-new-zero-Cauchy-then-Cartesian-cold-scalar-v2',
            run_id=self.run_id, run_attempt=self.attempt, source_epoch=self.epoch,
            controllerSHA256=sha(__file__), requestSHA256=sha(self.repo/self.request_rel),
            candidateSHA256=sha(self.candidate), frozenSourceInventorySHA256=sha(inventory_path),
            frozenSourceFiles=len(inventory), cauchyRecipeSHA256=sha(baseline_recipe),
            cartesianRecipeSHA256=sha(self.recipe), newNoZConfigSHA256=sha(self.config),
            newInputNotLiveStrongCheckpoint=True, startedUTC=utc(), stages=[], state='starting',
            rawRetention='RUNNER_TEMP only; no Git, artifact or release raw publication.',
            originalStrongRunUnchanged=True, acceptedLiveCauchyStepsAdded=0,
            continuousCertificate=False, strongTargetComplete=False)

    def git(self, *args, capture=False, check=True):
        result = subprocess.run(['git', *args], cwd=self.repo,
            env=getattr(self, 'git_env', None), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.stdout and not capture:
            print(result.stdout, end='', flush=True)
        if check and result.returncode:
            raise RuntimeError('Git command failed: '+' '.join(args))
        return result.stdout if capture else result

    def run_stage(self, name, command):
        log = self.out/(name+'.log')
        start, began = time.monotonic(), utc()
        emit('cold-numerical-stage-start', stage=name, sourceEpoch=self.epoch)
        with log.open('w') as output:
            process = subprocess.run(command, cwd=self.frozen, env=self.child_env,
                                     stdout=output, stderr=subprocess.STDOUT)
        row = dict(stage=name, startedUTC=began, finishedUTC=utc(),
            OSExitCode=process.returncode, seconds=time.monotonic()-start,
            stdoutSHA256=sha(log), command=command)
        self.record['stages'].append(row)
        write(self.out/'cold-execution-receipt.json', self.record)
        emit('cold-numerical-stage-finished', **row)
        if process.returncode:
            raise RuntimeError(f'Actual subprocess failed: {name}, exit {process.returncode}')

    @staticmethod
    def scalar_value(value):
        scalar = lambda x: x is None or isinstance(x, (str, int, float, bool))
        output = {key: part for key, part in value.items() if scalar(part)}
        for group in ('curvature', 'geometry'):
            if isinstance(value.get(group), dict):
                output[group] = {key: part for key, part in value[group].items() if scalar(part)}
        output['reportContainsScalarFieldsOnly'] = True
        output['completeValueObjectCanonicalSHA256'] = hashlib.sha256(
            json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()
        return output

    def snapshot(self, state):
        self.record.update(state=state, updatedUTC=utc(), outputs={})
        paths = [self.initial, self.observer]+[Path(str(self.prefix)+suffix) for suffix in
                 ('-initial.json', '-state.json', '-observer.json', '-report.json', '-failure.json')]
        for path in paths:
            if path.exists():
                self.record['outputs'][path.name] = dict(sha256=sha(path), bytes=path.stat().st_size)
        def read_if_complete(path):
            if not path.exists():
                return None
            try:
                return json.loads(path.read_text())
            except (ValueError, UnicodeError) as error:
                self.record.setdefault('incompleteJSONOutputs', {})[path.name] = str(error)
                return None
        value = read_if_complete(self.initial)
        if value is not None:
            self.record['actualNewCauchyBaseline'] = dict(schema=value['schema'], dimension=len(value['z']),
                cauchyAcceptedSteps=value['cauchyAcceptedSteps'], accepted=value['accepted'],
                evaluation=self.scalar_value(value['evaluation']), actualDesign=value['actualDesign'],
                source=value['source'], execution=value['execution'])
        for key, path in [('actualNewCauchyObserver', self.observer),
                          ('independentCartesianReport', Path(str(self.prefix)+'-report.json')),
                          ('independentCartesianFailure', Path(str(self.prefix)+'-failure.json'))]:
            value = read_if_complete(path)
            if value is not None:
                self.record[key] = value
        def guard(value):
            if isinstance(value, dict):
                if any(key in value and isinstance(value[key], (list, dict)) for key in ('z', 'coefficients', 'parameterVector')):
                    raise ValueError('A raw parameter vector leaked into the scalar report')
                for part in value.values():
                    guard(part)
            elif isinstance(value, list):
                for part in value:
                    guard(part)
        guard(self.record)
        raw = (json.dumps(self.record, indent=2, allow_nan=False)+'\n').encode()
        if len(raw) >= 100000:
            raise ValueError('Scalar report exceeds 100KB; raw fallback is forbidden')
        self.target.write_bytes(raw)
        write(self.out/'cold-execution-receipt.json', self.record)

    def publish(self, reason):
        subject = f'visible-flex: Cartesian cold {self.run_id}/{self.attempt} {reason}'
        self.git('add', '--', str(self.target.relative_to(self.repo)))
        self.git('commit', '-m', subject)
        while True:
            pulled = self.git('pull', '--rebase', 'origin', 'main', check=False)
            new = self.git('rev-parse', 'origin/main', capture=True).strip()
            difference = self.git('diff', self.last_rules, new, '--', *(str(p) for p in RULES), capture=True)
            if difference:
                print('ROOT_README_DIFF_REQUIRES_APPLICATION\n'+difference, flush=True)
                raise RulesChanged('Apply the actual README diff before resolving or publishing')
            if pulled.returncode:
                conflicts = self.git('diff', '--name-only', '--diff-filter=U', capture=True).splitlines()
                if conflicts != [str(H)]:
                    raise RuntimeError('Actual pull failed outside this controller HANDOFF marker')
                (self.repo/H).write_text(self.git('show', ':2:'+str(H), capture=True))
                self.git('add', '--', str(H))
                env = self.git_env.copy()
                env['GIT_EDITOR'] = 'true'
                if subprocess.run(['git', 'rebase', '--continue'], cwd=self.repo, env=env).returncode:
                    raise RuntimeError('Actual HANDOFF rebase did not finish')
            lines = (self.repo/H).read_text().splitlines(keepends=True)
            own = [i for i, line in enumerate(lines) if line.startswith(MARKER)]
            if len(own) > 1:
                raise RuntimeError('Ambiguous own HANDOFF marker')
            line = f'{MARKER} run {self.run_id}/{self.attempt}；实际pull至 `{new}`；{utc()}；双README无差异。\n'
            if own:
                lines[own[0]] = line
            else:
                if lines and not lines[-1].endswith('\n'):
                    lines[-1] += '\n'
                lines.append(line)
            updated = ''.join(lines)
            if len(updated.encode()) >= 10000:
                raise RuntimeError('HANDOFF exceeds 10KB; root must compact it')
            (self.repo/H).write_text(updated)
            self.last_rules = new
            self.git('add', '--', str(H))
            if self.git('diff', '--cached', '--quiet', check=False).returncode:
                unpublished = self.git('rev-list', 'origin/main..HEAD', capture=True).strip()
                if unpublished:
                    if self.git('log', '-1', '--format=%s', capture=True).strip() != subject:
                        raise RuntimeError('Refusing to amend a different or published commit')
                    self.git('commit', '--amend', '--no-edit')
                else:
                    self.git('commit', '-m', subject)
            pushed = self.git('push', 'origin', 'HEAD:main', check=False)
            if pushed.returncode == 0:
                break
            if not re.search(r'fetch first|non-fast-forward|cannot lock ref|failed to update ref|incorrect old value|is at [0-9a-f]+ but expected', pushed.stdout, re.I):
                raise RuntimeError('Actual push failed outside non-fast-forward/ref-lock')
            emit('non-fast-forward-immediate-pull-rebase-retry')
        emit('actual-cold-scalar-published', state=self.record['state'],
             commit=self.git('rev-parse', 'HEAD', capture=True).strip())

    def execute(self):
        node = ['node', '--expose-gc', '--max-old-space-size=512', '--max-semi-space-size=4']
        self.run_stage('new-Cauchy-complete-value', node+[
            str(self.scripts/'6a65-cauchy-global-position.cjs'), 'value',
            str(self.candidate), str(self.config), str(self.initial)])
        actual = json.loads(self.initial.read_text())
        if actual.get('cauchyAcceptedSteps') != 0 or actual.get('accepted') is not False or actual.get('interfaceProbeOnly'):
            raise ValueError('Actual new baseline identity or counter mismatch')
        self.run_stage('new-Cauchy-same-field-observer', node+[
            str(self.scripts/'6a65-cauchy-same-field-observer-recovered-v2.cjs'),
            str(self.candidate), str(self.initial), str(self.observer), '4', '256'])
        self.snapshot('actual-new-Cauchy-baseline-and-observer-complete')
        self.publish('new baseline and observer exit 0')
        self.run_stage('independent-complete-Cartesian-experiment', [sys.executable,
            str(self.scripts/'6a65-cartesian-independent-experiment-v2.py'),
            '--scripts', str(self.scripts), '--candidate', str(self.candidate),
            '--source', str(self.initial), '--observer', str(self.observer),
            '--prefix', str(self.prefix), '--recipe', str(self.recipe),
            '--source-epoch', self.epoch, '--run-id', self.run_id])
        self.snapshot('independent-Cartesian-experiment-complete')
        self.publish('independent experiment exit 0')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', type=Path, required=True)
    parser.add_argument('--directory', type=Path, required=True)
    controller = Controller(parser.parse_args())
    try:
        controller.execute()
    except RulesChanged:
        emit('pending-scalar-report-awaits-root-rule-application', report=controller.record)
        raise
    except BaseException as error:
        controller.record['actualFailure'] = dict(error=str(error), atUTC=utc(), acceptedStepsNotInferred=True)
        try:
            controller.snapshot('failed-actual-process-or-publication')
            controller.publish('actual failure receipt')
        except BaseException as failure:
            emit('cold-failure-publication-also-failed', error=str(failure))
        raise

if __name__ == '__main__':
    main()
