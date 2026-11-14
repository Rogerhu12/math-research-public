#!/usr/bin/env python3
"""Check independent reproductions of the two closed M15 entry diagnostics.

No solve is launched here. Equality of diagnostic data and literal source
extraction is checked; finite angular samples are not rigorous positivity
certificates, and unsuccessful roots do not prove nonexistence.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC/'notes'
CACHE = TOPIC/'repro/source-root/topics/large-amplitude-twist-flex/scripts'


def read(path):
    value = Path(path).read_bytes()
    return json.loads(gzip.decompress(value) if value[:2] == b'\x1f\x8b' else value)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(ok, message):
    if not ok:
        raise ValueError(message)


def content_without_clock(data):
    result = data.copy()
    result.pop('seconds')
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--stage-replay', type=Path, required=True)
    ap.add_argument('--floor-replay', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    originals = [NOTES/'2026-11-09-db6f-tail-m15-failed-stage-diagnostic.json.gz',
                 NOTES/'2026-11-09-db6f-tail-m15-positive-floor-probe.json']
    replays = [args.stage_replay, args.floor_replay]
    datasets = []
    for original, replay in zip(originals, replays):
        a, b = read(original), read(replay)
        check(content_without_clock(a) == content_without_clock(b), 'A diagnostic mathematical field differs')
        for filename, digest in b['sourceSHA256'].items():
            check(sha(filename) == digest, 'A recorded frozen source changed')
        datasets.append(b)
    stage, floor = datasets
    check(stage['scriptSHA256'] == sha(HERE/'db6f-tail-diagnose-failed-stage.mjs'), 'Changed stage instrumentation')
    check(floor['scriptSHA256'] == sha(HERE/'db6f-tail-moment-positive-floor-probe.mjs'), 'Changed floor instrumentation')
    root_text = (CACHE/'general_root_tail_momentum.mjs').read_text()
    split_text = (CACHE/'f6tail_momentum_split_flux.mjs').read_text()
    pieces = [('root', root_text, ' function solveSPD(', ' function initializeFromRaw(', 'extractedRootSHA256'),
              ('RK4', split_text, '  function rk4(', '  return {...base,rhs,rk4,statistics};', 'extractedRK4SHA256')]
    for label, text, start, end, key in pieces:
        check(text.count(start) == 1, 'Nonunique source marker '+label)
        begin = text.index(start)
        body = text[begin:text.index(end, begin)]
        check(hashlib.sha256(body.encode()).hexdigest() == stage[key], 'Changed literal function extraction '+label)
    check(len(stage['cases']) == 5, 'Missing saved failed entry')
    config_path = Path(stage['config']['file'])
    check(sha(config_path) == stage['config']['sha256'], 'Changed stage configuration')
    config = read(config_path)
    parameters = None
    summary = []
    for index, case in enumerate(stage['cases']):
        path = Path(case['input'])
        check(sha(path) == case['inputSHA256'], 'Changed failed entry state')
        saved = read(path)
        p = saved['parameters']
        if parameters is None:
            parameters = p
        check(p == parameters, 'Different parameters across failed entries')
        differences = {key for key in set(config)&set(p) if config[key] != p[key]}
        check(differences <= {'depth', 'linearMethod'} and config['depth'] == p['physicalDepth'],
              'Config/entry mismatch beyond the numerical depth/method labels')
        check(p['projectionFloor'] == .05 and p['modes'] == 15 and p['quadrature'] == 256,
              'Changed original angular problem')
        first = case['firstFailure']
        check(first['ordinaryStep'] == first['substage'] == first['sourceX'] == 0,
              'The first failure is not at the first k1 entry')
        check(case['rhsCalls'] == 1 and case['successfulSteps'] == case['successfulStepByteChecks'] == 0,
              'Incorrect successful trajectory claim')
        check(all(not values for values in case['profileBreakpoints']), 'Unexpected cusp inside this stage')
        check(first['error'] == first['originalUninstrumentedRKError'] == saved['trial']['error'],
              'Different original error')
        initial = first['defaultInitial']
        check(initial['minD'] > .99 and initial['minS'] > .99, 'Unexpected D/S cause')
        if index < 4:
            check(initial['minA'] < .05 and 'D/S/A rejected' in first['error'], 'Unexpected default initial rejection')
        else:
            check(initial['minA'] > .05 and 'line search failed' in first['error'], 'Unexpected later Newton failure')
        check(len(first['alternatives']) == 2 and all(
            a['initial']['passesOriginalGuard'] and not a['originalRootWithSeed']['success']
            for a in first['alternatives']), 'A seeded success or untested initial guess was misreported')
        summary.append(dict(stage=case['stage'], raw_cell=case['rawCell'], raw_segment=case['rawSegment'],
                            step=saved['trial']['step'], first_RK_substage=0,
                            default_min_A_diagnostic=initial['minA'], error=first['error']))
    check(len(floor['records']) == 8 and floor['refinements'] == [], 'Unexpected successful higher-N continuation')
    check({row['floor'] for row in floor['records']} == {.05, .025, .01, .001}, 'Unexpected guard scan')
    for row in floor['records']:
        check(row['N'] == 256 and row['success'] is False
              and row['originalFunctionExactlyReproduced'] is True
              and 'line search failed' in row['error'], 'A local success or formula change was hidden')
    control = floor['controlResult']
    check(control['rootCoefficientsByteIdentical'] is True and control['firstRKStepByteIdentical'] is True,
          'Successful control comparison missing')
    for item in floor['inputs'].values():
        check(sha(item['file']) == item['sha256'], 'Changed floor-probe input')
    cp = read(floor['inputs']['control-checkpoint']['file'])
    cp = cp.get('checkpoint', cp.get('response', {}).get('checkpoint', cp))
    saved = read(floor['inputs']['stage-input']['file'])
    check(cp['parameters'] == parameters, 'Control uses different parameters')
    check(cp['states'][saved['stage']+1] != saved['inputState'], 'Successful control and failed entry were conflated')
    report = dict(status='PASS-read-only-entry-diagnostics-and-independent-data-replays', scope=__doc__,
        script_sha256=sha(__file__), original_files=[dict(file=str(p), sha256=sha(p)) for p in originals],
        replay_files=[dict(file=str(p), sha256=sha(p), bytes=p.stat().st_size) for p in replays],
        all_fields_identical_except_elapsed_seconds=True,
        extracted_original_functions_hashes_verified=True, first_failures=summary,
        original_failed_trials_successful_RK_steps=0, separate_control_successful_RK_steps_verified=1,
        positive_floor_calls=8, positive_floor_successes=0, dense_angular_continuations=0,
        equation_or_active_worker_changed=False, nonexistence_inferred=False,
        finite_sample_positivity_is_a_continuous_certificate=False)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(status=report['status'], failed_entries=5, local_floor_calls=8,
                         successful_roots=0, separate_control_RK_byte_match=True)))


if __name__ == '__main__':
    main()
