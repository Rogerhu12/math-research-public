#!/usr/bin/env python3
"""Bounded first-jet calculation in the actual projective infinity chart.

All 6188 original source rows are included: 3333 unit prebasis rows and
the other 2855 rows. No source-compression theorem is transferred between
affine charts. The frozen normal-form engine changes only its input-count guard.
"""
import argparse
import hashlib
import json
import subprocess
import time
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--original-nf-directory', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--normal-form-binary', required=True)
    args = parser.parse_args()
    original = Path(args.original_nf_directory).resolve()
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    own = Path(__file__).resolve()
    cpp = own.with_name('2026-11-14-r150-infinity-first-jet-789f.cpp')
    frozen = own.with_name('2026-11-14-r150-native-normal-form-789f.cpp')
    old_receipt = json.loads((original / 'normal-form-receipt.json').read_text())
    old_input = original / 'normal-form-input.txt'
    if old_receipt['status'] != 'completed' or old_receipt['sourceCount'] != 2195:
        raise RuntimeError('original normal form run was not complete')
    if sha(old_input) != old_receipt['inputSHA256']:
        raise RuntimeError('original parameter input hash changed')
    binary = Path(args.normal_form_binary).resolve()
    if sha(binary) != old_receipt['binarySHA256'] or sha(frozen) != old_receipt['cppSHA256']:
        raise RuntimeError('frozen normal form implementation changed')
    tokens = old_input.read_text().split()
    offset = 0

    def take(n):
        nonlocal offset
        values = tokens[offset:offset+n]
        if len(values) != n:
            raise RuntimeError('truncated original source input')
        offset += n
        return values

    if take(1) != ['R150_NATIVE_NF_V1']:
        raise RuntimeError('original source header')
    lines = ['R150_NATIVE_NF_V1']
    for _ in range(11):
        lines.append(' '.join(take(66)))
        coefficient_rows = []
        for _ in range(11):
            coefficients = take(11)
            coefficient_rows.extend([coefficients[10], coefficients[9]] + ['0'] * 9)
        lines.append(' '.join(coefficient_rows))
    if take(1) != ['3333']:
        raise RuntimeError('original constant source count')
    lines.append('3333')
    prebasis_raw = set()
    for _ in range(3333):
        record = take(4)
        prebasis_raw.add(int(record[3]))
        lines.append(' '.join(record))
    for _ in range(6):
        coefficient_rows = []
        for _ in range(66):
            coefficients = take(6)
            coefficient_rows.extend([coefficients[5], coefficients[4]] + ['0'] * 4)
        lines.append(' '.join(coefficient_rows))
    ns, nt = map(int, take(2))
    if ns != 2195 or nt != 9:
        raise RuntimeError('original complete source/target count')
    multiplier = {}
    for _ in range(ns):
        generator, monomial, raw = take(3)
        index = (int(raw)-1)//17
        if index in multiplier and multiplier[index] != monomial:
            raise RuntimeError('inconsistent original multiplier')
        multiplier[index] = monomial
    if set(multiplier) != set(range(364)):
        raise RuntimeError('incomplete original multiplier list')
    all_nonprebasis = [raw for raw in range(1,6189) if raw not in prebasis_raw]
    if len(all_nonprebasis) != 2855:
        raise RuntimeError('full quotient source count')
    lines.append('2855 0')
    for raw in all_nonprebasis:
        lines.append(str((raw-1)%17)+' '+multiplier[(raw-1)//17]+' '+str(raw))
    if list(map(int, take(nt))) != list(range(2, 11)) or offset != len(tokens):
        raise RuntimeError('original target identities or end of file')
    jet_input = out / 'infinity-first-jet-input.txt'
    jet_input.write_text('\n'.join(lines) + '\n\n')
    receipt = {
        'format': 'r150-infinity-first-jet-run-v1',
        'field': 31,
        'chart': 'u=t/s, y=(u^5,u^4,u^3,u^2,u,1)',
        'linearNTransformation': 'u^10 L(1/u), then mod u^2',
        'quadraticGammaTransformation': 'u^5 Gamma(1/u), then mod u^2',
        'sourceUse': '3333 unit prebasis plus all other 2855 original source rows; no source compression needed',
        'originalInputSHA256': sha(old_input),
        'originalReceiptSHA256': sha(original / 'normal-form-receipt.json'),
        'originalSourceDataSHA256': old_receipt['sourceDataSHA256'],
        'profileSHA256': old_receipt['profileSHA256'],
        'inputSHA256': sha(jet_input),
        'normalFormCppSHA256': sha(frozen),
        'normalFormBinarySHA256': sha(binary),
        'jetCppSHA256': sha(cpp),
        'runnerSHA256': sha(own),
        'perStageSecondsLimit': 60,
        'memoryMiBLimit': 512,
        'status': 'running',
        'stages': [],
    }
    receipt_path = out / 'infinity-first-jet-receipt.json'

    def save():
        receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')

    def run(stage, command, seconds=60):
        started = time.monotonic()
        log = out / (stage + '.log')
        with open(log, 'wb') as f:
            result = subprocess.run(['timeout', '--kill-after=5s', str(seconds) + 's',
                'prlimit', '--as=536870912', '--core=0', '--'] + command,
                stdout=f, stderr=subprocess.STDOUT)
        item = {'stage': stage, 'exitCode': result.returncode,
                'elapsedSeconds': time.monotonic() - started, 'logSHA256': sha(log)}
        receipt['stages'].append(item)
        save()
        print(json.dumps(item), flush=True)
        if result.returncode != 0:
            receipt['status'] = 'failed-or-incomplete'
            save()
            raise RuntimeError('bounded stage failed: ' + stage)

    save()
    jet_binary = out / 'infinity-first-jet'
    run('compile', ['g++', '-O3', '-std=c++17', str(cpp), '-o', str(jet_binary)], 30)
    frozen_text = frozen.read_text()
    if frozen_text.count('ns>2195') != 1:
        raise RuntimeError('source-count guard not found exactly once')
    expanded_source = out / 'normal-form-all-original-rows.cpp'
    expanded_source.write_text(frozen_text.replace('ns>2195', 'ns>6188'))
    receipt['normalFormOnlyPatch'] = {'before':'ns>2195', 'after':'ns>6188'}
    receipt['expandedNormalFormCppSHA256'] = sha(expanded_source)
    expanded_binary = out / 'normal-form-all-original-rows'
    run('compile-expanded-nf', ['g++', '-O3', '-std=c++17', str(expanded_source), '-o', str(expanded_binary)], 30)
    receipt['expandedNormalFormBinarySHA256'] = sha(expanded_binary)
    prefix = out / 'nf'
    run('normal-form', [str(expanded_binary), str(jet_input), str(prefix), 'rref'])
    run('connecting-map', [str(jet_binary), str(prefix) + '-normal-forms.bin', str(out / 'jet')])
    receipt['summary'] = json.loads((out / 'jet-summary.json').read_text())
    receipt['outputs'] = {}
    for name in ['nf-forward.bin', 'nf-backward.bin', 'nf-reduction.bin',
                 'nf-normal-forms.bin', 'jet-operations.bin', 'jet-summary.json']:
        path = out / name
        receipt['outputs'][name] = {'bytes': path.stat().st_size, 'sha256': sha(path)}
    receipt['status'] = 'completed'
    save()
    summary = receipt['summary']
    print(json.dumps({'status': 'completed', 'constantRank': summary['constantRank'],
                     'connectingRank': summary['connectingRank']}), flush=True)


if __name__ == '__main__':
    main()
