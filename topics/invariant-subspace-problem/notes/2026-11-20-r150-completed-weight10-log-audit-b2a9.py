#!/usr/bin/env python3
"""Recover the completed original weight-ten run without rerunning its algebra.

AI-assisted: OpenAI ChatGPT, GPT-6 Astra Pro; Astra-ISP-b2a9acde-20261120.
Input: the full temporary GitHub job log for job 133508782090.
Output: source/run/hash identities and the verified scope, never matrix arrays.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / 'topics/invariant-subspace-problem/notes'


def canon(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()


def digest(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def audit(path):
    log_bytes = path.read_bytes()
    log = log_bytes.decode('utf-8')
    steps = [json.loads(line.split('ISP_REMOTE_STEP ', 1)[1])
             for line in log.splitlines() if 'ISP_REMOTE_STEP ' in line]
    names = [
        'weight10-native-and-independent-controls120',
        'original-ten-parameter-model116-180',
        'original-parameter-seed-compression50-180',
        'original-mean-first30-final180',
        'original-weight8-complete-prepare180',
        'original-weight8-complete-final180',
        'original-complete210-all-sources900',
        'original-delta-weight10-prepare600',
        'original-weight10-full-macaulay600',
        'original-weight10-full-macaulay600-resume2',
    ]
    require([s['stepId'] for s in steps] == names, 'all ten actual ordered attempts')
    for i, step in enumerate(steps):
        require(step['runId'] == '43926933406', 'same actual run')
        require(step['exitCode'] == (75 if i == 8 else 0), 'actual attempt status')
        require(step['python'].startswith('3.12.14 ') and step['pythonFlint'] == '0.9.0', 'original arithmetic versions')
        require(digest((ROOT / step['script']).read_bytes())['sha256'] == step['scriptSHA256'], 'same recorded source')
        require(step['largeDataUploadedOrCommitted'] is False, 'no large-data publication')

    driver = ROOT / steps[-1]['script']
    source = driver.read_text()
    assignments = {}
    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                assignments[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                pass
    pins = assignments['PINS']
    argv = steps[-1]['argvTemplate']
    for key, expected in pins.items():
        option = '--' + key.replace('_', '-')
        helper = argv[argv.index(option) + 1].replace('{scripts}/', '')
        require(digest((NOTES / helper).read_bytes())['sha256'] == expected, 'all nine frozen helper sources')

    receipts = []
    for step in steps[-2:]:
        result = copy.deepcopy(step['result'])
        require(result.pop('events') == [], 'no omitted mathematical events')
        result['source'] = {'path': driver.name, **digest(driver.read_bytes())}
        identity = digest(canon(result))
        require(identity == {'bytes': step['fullTemporaryReceiptBytes'], 'sha256': step['fullTemporaryReceiptSHA256']}, 'whole original raw receipt')
        receipts.append({'step': step['stepId'], **identity})

    last = steps[-1]['result']
    p = last['parameters']
    require(last['status'] == 'completed-negative', 'complete negative branch')
    require(p['nativeCompleteColumns'] == p['independentVerifiedColumns'] == 13808, 'all original columns, including dependent columns')
    require(p['completeSourceFrames'] == 200 and p['nativeObservedRank'] == 13697, 'all original sources and observed rank')
    require(p['fullInputAudit']['originalTerms'] == 8037189 and p['fullInputAudit']['targetTerms'] == 2604, 'whole original input and target')
    require(p['fullInputAudit']['all200OriginalPhaseVectorsMatched'] is True and
            p['fullInputAudit']['all200OriginalBinaryVectorsCompared'] is True and
            p['fullInputAudit']['all77276RowsAnd13808LabelsVerified'] is True and
            p['fullInputAudit']['targetReconstructedAgainFromOriginalMeanMatrix'] is True, 'original polynomial and matrix inputs')
    minor = p['completeOriginalMinorAudit']
    mr = minor['summary']
    for key in ['allOriginalInputsProcessed', 'allRankOriginalSourceLabelsDistinct',
                'allRankOriginalOutputPivotsDistinct', 'allRankFactorsNonzero',
                'allFullBitplanesCanonicalAndNormalized', 'allEarlierCoordinatesAndPaddingZero',
                'allPrecedingDAGShapesAndCoefficientsVerified']:
        require(mr[key] is True, 'complete selected-minor gate: ' + key)
    require(mr['selectedRank'] == 13697 and mr['originalSelectedMinorDeterminant127'] == 126, 'actual original nonzero minor')
    require(mr['inputSHA256'] == p['fullInput']['sha256'], 'same literal matrix')
    mr_raw = canon({'format': last['format'] + '-phase', 'binding': last['binding'], 'data': mr})
    require(digest(mr_raw) == {'bytes': minor['data']['logicalBytes'], 'sha256': minor['data']['logicalSha256']}, 'whole minor audit logical bytes')

    ordinary = p['independentOriginalVerification']
    v = ordinary['summary']
    require(v['binding'] == last['binding'] and v['inputSHA256'] == p['fullInput']['sha256'] and
            v['certificateSHA256'] == p['certificate']['data']['sha256'], 'same independent verifier binding')
    require(v['exitCode'] == 0 and v['verifiedOriginalColumns'] == 13808 and
            v['leftOriginalTargetReadout'] == 1 and v['literalScalarProducts'] == 74037410, 'all independent original products')
    for key in ['allOriginalDictionariesAndCoefficientsVerified', 'all13808OriginalColumnProductsVerified', 'all77276TargetCoordinatesVerified']:
        require(v[key] is True, 'ordinary verifier gate: ' + key)
    # The C++ receipt has a fixed field order and precision(17); a sorted JSON
    # reserialization has a different hash despite representing the same data.
    checker = (NOTES / '2026-11-16-r150-original-weight10-full-ordinary-verifier127-789f.cpp').read_text()
    section = checker[checker.index(' struct rusage ru{}'):checker.index(' if(!out.empty()&&generation)')]
    keys = re.findall(r'\\"([A-Za-z0-9]+)\\":', section)
    require(set(keys) == set(v) and len(keys) == len(v), 'every original C++ receipt field')
    vr_raw = ('{' + ','.join(json.dumps(k) + ':' +
              (format(v[k], '.17g') if isinstance(v[k], float) else json.dumps(v[k], separators=(',', ':')))
              for k in keys) + '}').encode()
    require(digest(vr_raw) == {k: ordinary['receipt'][k] for k in ['bytes', 'sha256']}, 'whole original ordinary-verifier receipt')
    require(p['literalOriginalTargetReadout'] == 1 and p['all13808OriginalColumnsAnnihilated'] is True, 'same target left separation')
    require(p['characteristicZeroConclusion'] is False and p['allHigherBellPowersExcluded'] is False and
            p['originalBellIdealNonmembershipClaimed'] is False, 'original computational scope preserved')
    return {
        'format': 'r150-completed-weight10-log-recovery-b2a9-v1',
        'runId': 43926933406, 'jobId': 133508782090,
        'fullJobLog': digest(log_bytes), 'actualAttempts': len(steps),
        'source': {'path': driver.name, **digest(driver.read_bytes())},
        'allTenRecordedSourceHashesMatch': True, 'allNineFrozenHelperHashesMatch': True,
        'reconstructedOriginalReceipts': receipts,
        'reconstructedMinorLogicalReceipt': digest(mr_raw),
        'reconstructedOrdinaryRawReceipt': digest(vr_raw),
        'allOriginalInputGatesRead': True, 'sameInput': p['fullInput'],
        'sourceRank': 13697, 'originalMinorDeterminant127': 126,
        'independentlyAnnihilatedOriginalColumns': 13808,
        'independentScalarProducts': 74037410, 'leftWitnessSupport': v['certificateSupport'],
        'literalTarget': 'delta14*b^2*e0', 'targetReadout': 1,
        'rawMatrixOrWitnessRecomputedThisAudit': False,
        'characteristicZeroResultRequiresSeparateRankCeilingProof': True,
        'rawLogsOrArraysCommitted': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('job_log', type=Path)
    args = parser.parse_args()
    print(json.dumps(audit(args.job_log), indent=2, ensure_ascii=False))
