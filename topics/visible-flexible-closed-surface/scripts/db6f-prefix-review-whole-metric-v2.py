#!/usr/bin/env python3
"""Light independent replay and input-contract tests for scalar closure v2.

No metric or curvature backend is rerun. Synthetic metadata fixtures test
binding/rejection only and are never geometric certificates.
"""
import argparse
import copy
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
EXPECTED = '20d9b6127625595afaf14daac4d23ccdd68d10f5d3a36d0697472f5df50d8fc3'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--baseline-report', type=Path, required=True)
    ap.add_argument('--replay-out', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    target = HERE/'db6f-root-whole-metric-reach-v2.py'
    assert sha(target) == EXPECTED
    assert not args.out.exists() and not args.replay_out.exists()
    spec = importlib.util.spec_from_file_location('prefix_review_scalar_v2', target)
    author = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(author)
    old = json.loads(args.baseline_report.read_text())
    budget = author.resolve(args.baseline_report.parent, old['closed_budget']).resolve()
    tail = author.resolve(args.baseline_report.parent, old['tail_certificate']).resolve()
    command = [sys.executable, str(target), '--closed-budget', str(budget),
               '--tail-certificate', str(tail), '--out', str(args.replay_out)]
    proc = subprocess.run(command, text=True, capture_output=True)
    if proc.returncode:
        raise RuntimeError(proc.stderr or proc.stdout)
    replay = json.loads(args.replay_out.read_text())
    scalar_fields = [key for key, value in old.items()
                     if isinstance(value, dict) and 'exact' in value]
    for key in scalar_fields:
        assert replay[key] == old[key], key
    assert replay['separate_tail_metric_certificate'] is None
    assert replay['whole_principal_curvature_upper'] == old['whole_principal_curvature_upper']
    assert replay['README_complete'] is False
    checks = []
    with tempfile.TemporaryDirectory(prefix='db6f-prefix-v2-contract-') as directory:
        folder = Path(directory)
        manifest = folder/'manifest.json'
        manifest.write_text('{"fixture":"no-geometric-claim"}\n')
        data = folder/'data.bin'
        data.write_bytes(b'synthetic binding fixture only\n')
        row_file = folder/'rows.json.gz'
        packet_file = folder/'packet.json'
        report_file = folder/'report.json'
        full = dict(manifest_sha256=sha(manifest), total_finite_spans=2)
        full_packet = dict(background_definition_hashes={'definition': 'frozen-fixture-hash'})
        initial_rows = [dict(packet_row=i, span_index=i-1, metric_operator_upper=0.001*(i+1))
                        for i in range(3)]
        initial_meta = dict(finite_tail_manifest_sha256=sha(manifest), finished=True,
                            background_definition_hashes=copy.deepcopy(full_packet['background_definition_hashes']),
                            data_file=str(data), data_sha256=sha(data))
        initial_report = dict(manifest=str(manifest), manifest_sha256=sha(manifest),
                              packet=str(packet_file), packet_data_sha256=sha(data),
                              complete_packet_partition_validated=True,
                              entire_finite_tail_and_collar_covered=True, collar_included=True,
                              checked_packet_intervals=3, packet_intervals=3,
                              total_finite_spans=2, selected_span_interval=[-1, 2],
                              metric_immersion_certified_on_checked_intervals=True,
                              row_data_file=str(row_file), metric_operator_upper=0.003)

        def run(name, change=None, valid=False):
            rows, meta, report, parent = map(copy.deepcopy,
                (initial_rows, initial_meta, initial_report, full_packet))
            if change:
                change(rows, meta, report, parent)
            row_file.write_bytes(gzip.compress(json.dumps(rows).encode(), mtime=0))
            packet_file.write_text(json.dumps(meta)+'\n')
            report['packet_sha256'] = sha(packet_file)
            report['row_data_sha256'] = sha(row_file)
            report_file.write_text(json.dumps(report)+'\n')
            try:
                value, binding = author.separate_metric_certificate(report_file, full, parent)
            except ValueError as error:
                assert not valid, (name, str(error))
                checks.append(dict(name=name, rejected=True, reason=str(error)))
            else:
                assert valid, name
                assert value == Fraction(0.003)
                assert binding['curvature_source_is_unchanged_full_certificate'] is True
                checks.append(dict(name=name, accepted=True, exact_metric=str(value)))

        run('valid complete same-map/background binding fixture', valid=True)
        run('different finite map', lambda r,m,x,p:x.update(manifest_sha256='0'*64))
        run('different packet finite map', lambda r,m,x,p:m.update(finite_tail_manifest_sha256='0'*64))
        run('unfinished packet', lambda r,m,x,p:m.update(finished=False))
        run('different target background', lambda r,m,x,p:m.update(background_definition_hashes={'definition':'other'}))
        run('empty original background identity', lambda r,m,x,p:p.update(background_definition_hashes={}))
        run('changed packet data binding', lambda r,m,x,p:x.update(packet_data_sha256='0'*64))
        run('partition not validated', lambda r,m,x,p:x.update(complete_packet_partition_validated=False))
        run('collar omitted', lambda r,m,x,p:x.update(collar_included=False))
        run('incomplete selected interval', lambda r,m,x,p:x.update(selected_span_interval=[0,2]))
        run('incomplete count', lambda r,m,x,p:x.update(checked_packet_intervals=2))
        run('row count mismatch', lambda r,m,x,p:r.pop())
        run('missing span despite full flags', lambda r,m,x,p:r[1].update(span_index=1))
        run('row sequence mismatch', lambda r,m,x,p:r[1].update(packet_row=0))
        run('negative row metric', lambda r,m,x,p:r[1].update(metric_operator_upper=-1e-6))
        run('nonfinite row metric', lambda r,m,x,p:r[1].update(metric_operator_upper=float('inf')))
        run('global value below actual row maximum', lambda r,m,x,p:x.update(metric_operator_upper=0.002))
        run('global value above actual row maximum', lambda r,m,x,p:x.update(metric_operator_upper=0.004))
    report = dict(status='PASS-scalar-difference-and-metadata-contract-only',
                  scope=__doc__, target_sha256=sha(target), script_sha256=sha(__file__),
                  baseline_report=str(args.baseline_report), baseline_sha256=sha(args.baseline_report),
                  replay=str(args.replay_out), replay_sha256=sha(args.replay_out),
                  original_exact_scalar_fields_unchanged=scalar_fields,
                  original_curvature_unchanged=True, command=command, tests=checks,
                  synthetic_fixtures_are_not_geometric_certificates=True,
                  partition_scope='The scalar aggregator checks hashes, reviewed backend coverage declarations, row count/order, complete span labels and the row maximum. Exact u-left/u-right packet partition validation remains a dependency of the reviewed metric-only backend.')
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(status=report['status'], exact_scalar_fields=len(scalar_fields),
                          input_contract_cases=len(checks))))


if __name__ == '__main__':
    main()
