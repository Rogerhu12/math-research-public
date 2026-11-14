#!/usr/bin/env python3
"""Exercise only cut-jet schema validation on a real closed s=.25 response.

Malformed jets exist only as in-memory copies. No s=1 packet is constructed,
no solver is imported, and no continuation-success gate is called.
"""
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'


def bind(path):
    path = Path(path).resolve()
    return dict(path=str(path), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    response_path = NOTES / '2026-11-09-db6f-prefix-amplitude-recovery-s025-iter004-01_tail_0001.json.gz'
    original_identity = bind(response_path)
    if original_identity['sha256'] != '07db124d2da380171b99e6d577255b43d4f5496fbd6d982d5dea1a6df873c2e5':
        raise ValueError('Wrong frozen real quarter response')
    record = json.loads(gzip.decompress(response_path.read_bytes()))
    response = record['response']
    jets = response['jets']
    modes = response['checkpoint']['parameters']['modes']
    if modes != 15 or response['converged'] is not True or response['audit'] is not None:
        raise ValueError('The known unaudited quarter response changed')
    source_v1 = HERE / 'db6f-prefix-prepare-final-m15-coupling.py'
    source_v2 = HERE / 'db6f-prefix-prepare-final-m15-coupling-v2.py'
    v1 = load('db6f_final_m15_fixture_v1', source_v1)
    v2 = load('db6f_final_m15_fixture_v2', source_v2)
    if not v2.valid_cut_jets(jets, modes):
        raise ValueError('The actual closed quarter jets were rejected')
    scalar_names = sorted(k for k, value in jets.items() if not isinstance(value, list))
    array_names = sorted(k for k, value in jets.items() if isinstance(value, list))
    if len(scalar_names) != 14 or array_names != ['height', 'second', 'slope']:
        raise ValueError('Unexpected original cutJets schema')
    cases = []

    def rejected(label, changed):
        accepted = bool(v2.valid_cut_jets(changed, modes))
        cases.append(dict(case=label, accepted_by_v2=accepted))
        if accepted:
            raise ValueError('Malformed cut jets accepted: '+label)

    for field in scalar_names:
        for tag, value in [('null', None), ('string', '0'), ('bool_true', True), ('bool_false', False)]:
            changed = copy.deepcopy(jets)
            changed[field] = value
            rejected(field+':'+tag, changed)
    for field in array_names:
        for tag, value in [('null', None), ('string', '0'), ('bool_true', True), ('bool_false', False)]:
            changed = copy.deepcopy(jets)
            changed[field][0] = value
            rejected(field+'[0]:'+tag, changed)
        for tag, changed_array in [('short', jets[field][:-1]), ('long', jets[field]+[0.0])]:
            changed = copy.deepcopy(jets)
            changed[field] = changed_array
            rejected(field+':'+tag, changed)
        changed = copy.deepcopy(jets)
        changed[field] = None
        rejected(field+':null_array', changed)
    for tag, value in [('positive_infinity', float('inf')), ('negative_infinity', -float('inf')), ('nan', float('nan'))]:
        changed = copy.deepcopy(jets)
        changed['E'] = value
        rejected('E:'+tag, changed)
        changed = copy.deepcopy(jets)
        changed['slope'][0] = value
        rejected('slope[0]:'+tag, changed)
    changed = copy.deepcopy(jets)
    del changed['radius']
    rejected('missing_scalar_key', changed)
    changed = copy.deepcopy(jets)
    changed['unexpected'] = 0.0
    rejected('unexpected_key', changed)
    rejected('null_whole_jets', None)
    changed = copy.deepcopy(jets)
    changed['backgroundSlope'] = None
    legacy_accepts_null = bool(v1.finite_tree(changed))
    if not legacy_accepts_null:
        raise ValueError('The specific frozen v1 weakness was not reproduced')
    if original_identity != bind(response_path):
        raise ValueError('Source response unexpectedly changed')
    report = dict(status='PASS-CUT-JETS-SCHEMA-FIXTURE-ONLY', scope=__doc__,
        actual_response_scope='Real converged finite M15 s=.25 warm; audit=None. Not an s=1 result.',
        actual_quarter_jets_accepted=True, source_scalar_fields=scalar_names,
        source_vector_fields=array_names, modes=modes,
        malformed_cases_count=len(cases), all_malformed_cases_rejected=True,
        frozen_v1_null_jet_weakness_reproduced=legacy_accepts_null,
        cases=cases, source_response_unchanged=True,
        numerical_solver_calls=0, complete_gate_calls=0, s1_packets_created=0,
        bound_files=[bind(path) for path in [Path(__file__).resolve(), source_v1, source_v2, response_path]])
    with args.output.open('x') as handle:
        json.dump(report, handle, indent=2, allow_nan=False)
        handle.write('\n')
    print(json.dumps(dict(status=report['status'], malformed_cases=len(cases),
        actual_quarter_jets_accepted=True, numerical_solver_calls=0,
        output=str(args.output), sha256=bind(args.output)['sha256'])))


if __name__ == '__main__':
    main()
