#!/usr/bin/env python3
"""Metadata/Fraction posterior gate for one reviewed fixed-g closed map.

The fixed terminal threshold is exactly 1/500000000.  A positive result
composes reviewed continuous certificates; it is not a new numerical
certificate, solver run, final independent workflow replay, or existence
theorem for an infinite limit.  The only negative-fixture mode uses the
already frozen actual R21 M12 map and never accepts it as a new candidate.

Only standard-library JSON, gzip envelopes, streaming hashes and Fraction
arithmetic are used.  No numerical backend is imported or executed.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPO = TOPIC.parent.parent
BOUND = Q(1, 500000000)
FACTOR = Q(195883, 20000)
LOWER = Q(370012576184137, 18889465931478580854784)
HEIGHT_SHA = 'dd64e00bf25124b03e725792e321e961106c6ee643f5526e0b5b95383161ff01'
POSITIVE_ALPHA_SHA = '35811ec9035d77e60f5809b6d1e19d8a27f4755f95eb5498eaa8fcc0f4808a19'

SOURCES = {
    'db6f-root-whole-metric-reach-v2.py': '20d9b6127625595afaf14daac4d23ccdd68d10f5d3a36d0697472f5df50d8fc3',
    'db6f-audit-closed-budget-transfer-v3.py': '5ef8d229e0a19bc83381a2cdcaef8b24309e00a1fdc6b9409b20d7ca34092e49',
    'db6f-root-closed-budget-v2.py': '0d68b718a43a69b24a865b1932e2700a47190724a3be4ea3f1202b56d1a59641',
    'db6f-tail-transfer-background-v3.py': 'bdf6307fd93328b1ae70923caac2687fa19b0187ca9c723fe5d7072d7799a47b',
    'db6f-root-transfer-background.py': '35aa82514ec2be4b78cf3670e97343d0ba50085a7a6a687273108fbb6eb09705',
    'db6f-root-common-cut-v2.py': '317e519fda8d78fb70b53f8a8c80d51599dec1ac46e92741cd9b2576a3f4fa7d',
    'db6f-root-mirror-hermite.py': 'ddb785a7e5199f1488fa50937668fc5236a1dee7b24679f75b39a4f15cb7f4b6',
    'db6f-prefix-flat-geometry-source.py': '23299890cebc07c938910995058d8e2ee09fbf289d323a3cac65bc3afc117c6f',
    'db6f-prefix-flat-profile.py': '5066cd6d8f94d3b22c0450cc2016df6f90d04efb85d7a13bc833c11868eaaa4b',
    'db6f-root-exact-bridge.py': 'f5d10784f58fa5008220354665de710ab4991b795f1b902e26a70ca44f382fd1',
    'db6f-audit-continuous-hermite.py': 'e1870297b172a372bbf889f9714249d4997171db7f53dbb3ec6195a5de2c642d',
    'db6f-audit-metric-polynomial.py': '02f9da4d86c7514bf90a3cfd185be85274c7ad0b9b34d3d20ede342d6b8adea4',
    'db6f-audit-metric-supplier.py': 'de2cafcb235a843b2f930decb54cf065c6cbc441884b050f09edb900ac196bd0',
    'db6f-audit-prefix-angular-metric.py': '42e7d222c40512fec2d4fd757544d630b3e372487322e27eb3571a06519eb2fb',
    'db6f-root-volume-moment.py': '502a3d8c9439ee0b707e6be7b367e356ef44d1942aa6a0615330b1005fe10913',
    'db6f_tail_integrated.py': '4714e67860c80ecffc691d0d1e797bf5e8fa62062a4292730646abdf7f6e87ae',
    'db6f-tail-first-bounds.py': 'ba3af5e44b9c727a9b7ca7b25b4e6abf19c504106b0810f4278928b82a084821',
    'db6f-tail-first-bounds-stream.py': '98686f818270191e413fa20b9388637bf85649bfa82b4f60b3cbde40dee0ad7d',
    'db6f-audit-tail-metric-curvature.py': 'ed175aacdb2ba3e84d7c397d121e90c2a6a1492d05f5efdb646690481d302670',
    'db6f-audit-tail-stream.py': 'adfcfbfe03643cf8a4284c078edb13d5caa49ad5eb7f94ce822ba8c27354a456',
    'db6f-audit-tail-metric-only.py': '178d7b7b62deeff93d8e198f271736ac41f258c07b3d8b7a9bc111c909d5ebd6',
}
# Prefix identities are separate: SOURCES below retains the original tail,
# background and fixed M12 reference family without adding or replacing keys.
PREFIX_SOURCES = {
    'db6f-prefix-shared-jet-byte-shards-v2.py': 'b894107ca47773b259f589d0231244e3dbdf86d2285f3c3789f07e318d868c50',
    'db6f-prefix-shared-jet-storage.py': 'c9d6f89b0dd3e8bca744b679ed92ef3176899c8ae30be46f8080b9e6a4b7b9c2',
    'db6f-prefix-fullxyz-hermite-storage.py': 'f7b3659a98d70941377a6e054fd9900a1de45518e65899da862987aae75f9ccc',
    'db6f-prefix-mirror-hermite-storage.py': '163d3ce9b11036c4ff9effce52d02dece2f09e57f582e24ce26e9ae4162eee94',
    'db6f-prefix-continuous-hermite-storage.py': '511b107519652feeda8f2beb3f1935a6f3078d297c3639824c0dabe75bff150c',
    'db6f-prefix-metric-polynomial-storage.py': '70bf1b39e23074069cd11cb5cbe180f40fb7df77b59a1c1622c274665444233d',
    'db6f-prefix-metric-supplier-storage.py': 'cf0981bcb2426c9db4dc35523e46ced805da4a90c37e47eae8a1247ccbd4aa2f',
    'db6f-prefix-volume-moment-storage.py': 'fd81fd2b1ebee77bd95ce9065e4898d5ef03b8bf72e99e3d0858f401b16818c1',
    'db6f-prefix-common-cut-storage.py': 'b994ce2e777eb24f744489ea2a6be96a74764fc75a0b3cea2e6d2d387efc4d3b',
    'db6f-prefix-angular-arithmetic-storage.py': 'd27282a9820d35023b74171bad3cc208429e5b0451d47d3175b7b001caa591c9',
    'db6f-prefix-metric-budget-storage.py': '0009368a049809d3d5864a6ca1adc8e52fbbade1f7b3e184b024b1093408f0c1',
    'db6f-prefix-closed-budget-storage.py': 'dc07d80f74a1cb880132e91ef0296f972e7e550a278eac057975fb8b032a09e9',
    'db6f-prefix-angular-metric-storage.py': '2f24cdf9b9649a5ecd34bdbbdabaf294f1fb985288578b54217a6143c98e902c',
}

REFERENCE = {
    'point': ('notes/2026-11-09-db6f-root-tail-m12-point-metric-witness.json', '13311ea4ecb781d0607ff6b58880c5f70bd79db2df2527aa9de3b6d9ad2e1b5e'),
    'point_wrapper': ('scripts/db6f-root-tail-m12-point.py', '5d950fa6caa3aff062ba5a62e743abac5b00d7ef0721930f299135d1dbdc1bb1'),
    'point_proof': ('notes/2026-11-09-db6f-root-tail-m12-point-lower-proof.md', '955a6550b43efb88f25767eaa0636fdb2be6eb397175507319c96fdddb2b8f92'),
    'point_review': ('notes/2026-11-09-db6f-audit-m12-point-lower.md', '0105a546e1978533a9d6769204cd5910cede0e323b945b860806cf4f5da66466'),
    'geometry': ('notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json', '253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2'),
    'manifest': ('notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json', 'cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'),
    'whole': ('notes/2026-11-09-db6f-root-whole-metric-reach-m12-critical-r01-lowmetric.json', 'f329aaea39722b02b48ce98fe11e4232ae2c60b57a94789b071dfb5c915f49c5'),
    'bridge': ('notes/2026-11-09-db6f-root-exact-bridge-m12.json', '1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa'),
    'target': ('notes/2026-11-09-db6f-root-flat17-m12-target.json', '7b307dd26afbe669a9b52d9f1795ed49c775288f9c9d679759b6036cc3c5c47b'),
}
BACKGROUND = {
    'checkpoint': 'd23b03e4ce5cd7aaf4ac9d1134f8a23ee274be3a1d0a0192a7b294f1195e43f0',
    'calibrations': 'bcfaba00aec62290b5b29432836c9e76ef6cf0d582b06c046677b0f8688ca9f4',
    'alpha': '04aae85c19f78fd82808ac32b104537dbb584c39cac8a648107722c855685c62',
    'cell_zero_A': '2f41f4a2a5879e9363f4e12aa52576aaa758a860c338f19e959e6f387c1b33de',
    'inner_A': '23f67ca7d0bfb981b29f9bddd5bbdd3f8fbb55720c0866c67db3194c858f7bba',
    'outer_B': '53676270742794da8af79d539aece0b7f88dc98d1c73ab1668157ebe700ba185',
}
EXTRA_KEYS = {'iterationCheckpointFile', 'sharedEngines', 'trialDiagnosticFile', 'trialStatePrefix'}
NUMERICAL_KEYS = set('''modes spacing depth physicalDepth steps quadrature linearFar
linearSteps linearMethod fastJacobian cuspAwareFlow actualCuspGrid solveTolerance
auditSteps maxIterations traceFile initialCheckpoint harmonicAmplitudePredictor
shootingParts warpSteps quadratureTolerance cuspAwareQuadrature maxCachedBetas
nodeIndex rhsEvaluation projectionFloor farPadding'''.split()) | EXTRA_KEYS
POLICY = {
    'id': 'visible-flat17-bookkeeping-keys-v2',
    'additional_numerical_keys': sorted(EXTRA_KEYS),
    'base_file': 'db6f-root-transfer-background.py',
    'base_sha256': SOURCES['db6f-root-transfer-background.py'],
    'difference_semantics': 'Key presence and canonical JSON value including JSON types; an unknown added null key rejects.',
}
POLICY_SHA = '2b4fd1d141d9116157037d05748ab2a019c9033441453ee8e6ab917eb355eae3'
PREFIX_KEYS = ('frozen_profile', 'chart', 'warp_reference_q', 'ell',
               'profile_loader_sha256', 'profile_implementation_sha256')
BRIDGE_KEYS = ('script_sha256', 'physical_cut_radius_exact', 'physical_cut_slope_exact',
               'physical_cut_second_derivative_exact', 'exact_pt', 'exact_ps', 'exact_L',
               'gap_at_left', 'gap_at_right', 'gap_derivative_lower_exact',
               'unique_root_in_box', 'arclength_rescale', 'phase_upper')


def check(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False)


def binary(value):
    check(type(value) in (int, float), 'A binary numerical bound is not a number')
    return Q(value)


def exact(record):
    check(type(record) is dict and type(record.get('exact')) is str, 'Missing exact Fraction field')
    return Q(record['exact'])


def same(left, right, message):
    check(canonical(left) == canonical(right), message)


class Files:
    def __init__(self):
        self.records = {}

    def file(self, name, expected, parent, role):
        check(type(expected) is str and len(expected) == 64 and
              all(c in '0123456789abcdef' for c in expected), 'Invalid SHA256 for '+role)
        p = Path(name)
        candidates = (p, Path(parent)/p, TOPIC/p, REPO/p, Path(parent)/p.name)
        path = next((x.resolve() for x in candidates if x.is_file()), None)
        check(path is not None, 'Missing bound file for '+role)
        key = str(path)
        if key not in self.records:
            h = hashlib.sha256()
            with path.open('rb') as stream:
                for block in iter(lambda: stream.read(1 << 20), b''):
                    h.update(block)
            self.records[key] = {'file': key, 'sha256': h.hexdigest(), 'bytes': path.stat().st_size, 'roles': []}
        record = self.records[key]
        check(record['sha256'] == expected, 'Changed file for '+role)
        if role not in record['roles']:
            record['roles'].append(role)
        return path

    def json(self, name, expected, parent, role):
        path = self.file(name, expected, parent, role)
        raw = path.read_bytes()
        check(hashlib.sha256(raw).hexdigest() == expected, 'File changed during read: '+role)
        if raw[:2] == b'\x1f\x8b':
            raw = gzip.decompress(raw)
        def nonfinite(value):
            raise ValueError('Nonfinite JSON constant '+value)
        obj = json.loads(raw, parse_constant=nonfinite)
        check(type(obj) is dict, 'Metadata is not a JSON object: '+role)
        return path, obj

    def item(self, item, parent, role):
        check(type(item) is dict and type(item.get('file')) is str, 'Missing file binding: '+role)
        return self.json(item['file'], item['sha256'], parent, role)

    def source(self, name, declared=None):
        expected = SOURCES[name]
        if declared is not None:
            check(declared == expected, 'Unexpected implementation for '+name)
        return self.file(HERE/name, expected, HERE, 'source:'+name)

    def prefix_source(self, name, declared=None):
        expected = PREFIX_SOURCES[name]
        if declared is not None:
            check(declared == expected, 'Unexpected prefix implementation for '+name)
        return self.file(HERE/name, expected, HERE, 'prefix-source:'+name)

    def output(self):
        return [self.records[key] for key in sorted(self.records)]


def parameters(old, new):
    check(type(old) is dict and type(new) is dict, 'Parameters must be JSON objects')
    for obj in (old, new):
        for key in EXTRA_KEYS:
            if key in obj and obj[key] is not None:
                check(type(obj[key]) is (bool if key == 'sharedEngines' else str), 'Bad metadata-key type: '+key)
    changed = [key for key in sorted(set(old)|set(new))
               if key not in old or key not in new or canonical(old[key]) != canonical(new[key])]
    check(all(key in NUMERICAL_KEYS for key in changed), 'Changed unknown/physical parameter: '+', '.join(
        key for key in changed if key not in NUMERICAL_KEYS))
    return changed


def checkpoint_parameters(record):
    response = record.get('response', record)
    check(type(response) is dict, 'Invalid checkpoint response')
    cp = response.get('checkpoint', response.get('tail_checkpoint', response))
    check(type(cp) is dict and type(cp.get('parameters')) is dict, 'Missing checkpoint parameters')
    return cp['parameters']


def definitions(files, mapping, parent, reference=None):
    check(type(mapping) is dict and set(mapping) == set(BACKGROUND), 'The six background definitions are not exact')
    if reference is not None:
        same(mapping, reference, 'Different fixed background definition mapping')
    result = {}
    for key, digest in BACKGROUND.items():
        check(mapping[key]['sha256'] == digest, 'Changed fixed background '+key)
        result[key] = files.item(mapping[key], parent, 'background:'+key)
    return result


def manifest_files(files, path, meta, role):
    check(meta.get('finished') is True and type(meta.get('totalUniqueNodes')) is int and
          meta['totalUniqueNodes'] >= 2 and len(meta['files']) > 0, 'Incomplete finite manifest: '+role)
    total = 1
    for index, item in enumerate(meta['files']):
        check(type(item['rows']) is int and item['rows'] >= 2, 'Invalid shard row count')
        p = files.file(item['path'], item['sha256'], path.parent, role+':shard:'+str(index))
        check(p.stat().st_size == item['bytes'], 'Changed shard size')
        total += item['rows']-1
    check(total == meta['totalUniqueNodes'], 'Manifest shared-row count mismatch')
    cp_path, cp = files.json(meta['input'], meta['inputSHA256'], path.parent, role+':checkpoint')
    parameters(checkpoint_parameters(cp), meta['parameters'])
    return meta['totalUniqueNodes']-1


def reference(files):
    paths, data = {}, {}
    for key, (name, digest) in REFERENCE.items():
        if name.endswith('.json'):
            paths[key], data[key] = files.json(TOPIC/name, digest, TOPIC, 'M12:'+key)
        else:
            paths[key] = files.file(TOPIC/name, digest, TOPIC, 'M12:'+key)
    point, geom, whole = data['point'], data['geometry'], data['whole']
    check(point['script_sha256'] == REFERENCE['point_wrapper'][1], 'M12 point source identity changed')
    for key in ('geometry', 'manifest', 'whole'):
        check(point['inputs'][key]['sha256'] == REFERENCE[key][1], 'M12 point identity mismatch: '+key)
    check(geom['tail_manifest_sha256'] == whole['tail_manifest_sha256'] == REFERENCE['manifest'][1] and
          whole['geometry_sha256'] == REFERENCE['geometry'][1], 'M12 closed-map connection changed')
    check(geom['bridge_parameter_certificate_sha256'] == REFERENCE['bridge'][1] and
          data['bridge']['target_sha256'] == REFERENCE['target'][1], 'M12 exact-target connection changed')
    point_packet_path, point_packet = files.item(point['inputs']['packet'], paths['point'].parent, 'M12:point-packet')
    check(point_packet['finite_tail_manifest_sha256'] == REFERENCE['manifest'][1] and
          whole['separate_tail_metric_certificate']['packet_sha256'] == point['inputs']['packet']['sha256'],
          'M12 point/whole packet mismatch')
    definitions(files, point['background_definition_hashes'], paths['point'].parent)
    same(point_packet['background_definition_hashes'], point['background_definition_hashes'], 'M12 packet target changed')
    files.file(point_packet['data_file'], point_packet['data_sha256'], point_packet_path.parent, 'M12:point-packet-data')
    for name, digest in point['source_sha256'].items():
        files.file(HERE/name, digest, HERE, 'M12:point-source:'+name)
    manifest_files(files, paths['manifest'], data['manifest'], 'M12:manifest')
    lower = Q(point['whole_actual_metric_error_lower_exact'])
    check(lower == binary(point['selected_witness']['relative_operator_lower']) == LOWER,
          'M12 lower bound is not the independently reviewed exact endpoint')
    check(lower > Q('1.95883e-8') and lower-FACTOR*BOUND > 0, 'M12 strict comparison margin failed')
    return paths, data, lower


def transfer(files, binding, parent, manifest_path, meta, ref, height, positive, height_path):
    path, report = files.item(binding, parent, 'candidate:background-transfer')
    files.source('db6f-tail-transfer-background-v3.py', report['script_sha256'])
    files.source('db6f-root-transfer-background.py', report['base_transfer_script_sha256'])
    check(report.get('mode') == 'finite-background-grid-transfer' and report.get('finished') is True and
          report.get('all_other_parameters_identical') is True and
          report.get('background_definition_hashes_verified') is True, 'A preflight is not a completed transfer')
    same(report['parameter_policy'], POLICY, 'Unexpected transfer policy')
    check(report['parameter_policy_sha256'] == POLICY_SHA == hashlib.sha256(canonical(POLICY).encode()).hexdigest(),
          'Transfer policy hash mismatch')
    new_sha = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    check(report['new_manifest_sha256'] == report['finite_tail_manifest_sha256'] == new_sha and
          binding['new_manifest_sha256'] == new_sha, 'Transfer targets another actual finite map')
    files.file(report['new_manifest'], new_sha, path.parent, 'candidate:transfer-new-manifest')
    old_path, old = files.json(report['old_manifest'], report['old_manifest_sha256'], path.parent, 'candidate:transfer-source-manifest')
    check(binding['old_manifest_sha256'] == report['old_manifest_sha256'] and old.get('finished') is True and
          old['inputSHA256'] == BACKGROUND['checkpoint'], 'Transfer source identity changed')
    changed = parameters(old['parameters'], meta['parameters'])
    check(changed == report['different_numerical_parameter_keys'], 'Transfer parameter ledger mismatch')
    parameters(ref['manifest']['parameters'], meta['parameters'])
    defined = definitions(files, report['background_definition_hashes'], path.parent, ref['point']['background_definition_hashes'])
    parameters(checkpoint_parameters(defined['checkpoint'][1]), old['parameters'])
    packet_path, packet = files.json(report['input_packet'], report['input_packet_sha256'], path.parent, 'candidate:transfer-source-packet')
    check(packet.get('finished') is True and packet['finite_tail_manifest_sha256'] == report['old_manifest_sha256'],
          'Transfer source packet identity mismatch')
    same(packet['background_definition_hashes'], report['background_definition_hashes'], 'Transfer changed the exact target')
    check(packet['data_sha256'] == report['input_data_sha256'], 'Transfer input data mismatch')
    files.file(packet['data_file'], packet['data_sha256'], packet_path.parent, 'candidate:transfer-input-data')
    files.file(report['data_file'], report['data_sha256'], path.parent, 'candidate:transfer-output-data')
    check(height['checkpointSHA256'] == positive['checkpointSHA256'] == BACKGROUND['checkpoint'] and
          positive['calibrationTableSHA256'] == BACKGROUND['calibrations'] and
          positive['cellZeroCertificateSHA256'] == hashlib.sha256(height_path.read_bytes()).hexdigest() and
          positive.get('positiveExactGlobalRadialAlphaProved') is True, 'Height/positive-alpha connection changed')
    tight_path, tight = defined['alpha']
    for key in ('checkpoint', 'calibrations', 'cell_zero_A', 'inner_A', 'outer_B'):
        check(tight['inputs'][key]['sha256'] == BACKGROUND[key], 'Tight-alpha dependency mismatch')
        files.item(tight['inputs'][key], tight_path.parent, 'candidate:tight-alpha:'+key)
    book_path, book = files.item(tight['inputs']['numerical_bookkeeping'], tight_path.parent, 'candidate:bookkeeping')
    book_sha = tight['inputs']['numerical_bookkeeping']['sha256']
    check(height['bookkeepingSHA256'] == defined['calibrations'][1]['bookkeepingSHA256'] == book_sha,
          'Background bookkeeping connection changed')
    return report['background_definition_hashes'], changed


def prefix_storage(files, base_path, base, geom):
    """Hash-only reconstruction; defining base shape precedes common-cut padding.

    This imports only the standard-library storage reader/byte verifier, not
    an ExactHermite class, NumPy, SciPy, or any numerical certificate backend.
    """
    path = files.prefix_source('db6f-prefix-shared-jet-storage.py')
    files.prefix_source('db6f-prefix-shared-jet-byte-shards-v2.py')
    check('data_storage' in base and 'data_file' not in base and
          'data_storage' in geom and 'data_file' not in geom,
          'This candidate entry requires explicit sharded prefix storage')
    same(base['data_storage'], geom['data_storage'], 'Common-cut/base storage reference differs')
    spec = importlib.util.spec_from_file_location('terminal_prefix_jet_storage', path)
    storage = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(storage)
    loaded, payload, records = storage.read_payload(base_path, verify_arrays=False)
    same(loaded, base, 'Base metadata changed during storage verification')
    check(hashlib.sha256(payload).hexdigest() == base['data_sha256'] == geom['data_sha256'],
          'Logical prefix bytes do not match the candidate')
    for item in records:
        bound = files.file(item['file'], item['sha256'], base_path.parent, 'candidate:prefix-storage')
        check(bound.stat().st_size == item['bytes'], 'Changed prefix storage size')
    return records


def prefix_metric(files, path, metric, geom_path, geom, base_path, bridge, explicit_target, ref):
    geometry_sha = hashlib.sha256(geom_path.read_bytes()).hexdigest()
    check(metric['geometry_sha256'] == geometry_sha and metric['geometry_data_sha256'] == geom['data_sha256'] and
          metric.get('entire_prefix_covered') is True, 'Prefix metric is partial or belongs to another final common-cut map')
    angular = metric['script_sha256'] == PREFIX_SOURCES['db6f-prefix-angular-metric-storage.py']
    if angular:
        files.prefix_source('db6f-prefix-angular-metric-storage.py', metric['script_sha256'])
        check(metric.get('finished') is True and metric['requested_intervals'] is None and
              metric['processed_intervals'] == metric['target_intervals'] and
              metric.get('exact_partition_reread_verified') is True, 'Incomplete angular certificate')
        target_path, target = files.item(metric['inputs']['target'], path.parent, 'candidate:prefix-target')
        check(metric['inputs']['geometry']['sha256'] == geometry_sha and
              metric['inputs']['bridge']['sha256'] == geom['bridge_parameter_certificate_sha256'], 'Angular inputs do not identify this map/bridge')
        baseline_path, baseline = files.item(metric['inputs']['baseline'], path.parent, 'candidate:angular-baseline')
        files.prefix_source('db6f-prefix-metric-polynomial-storage.py', baseline['script_sha256'])
        check(baseline['geometry_sha256'] == geometry_sha and baseline['target_sha256'] == metric['target_sha256'] and
              baseline['geometry_data_sha256'] == geom['data_sha256'] and baseline.get('entire_prefix_covered') is True and
              baseline['intervals_checked'] == baseline['intervals'], 'Angular baseline belongs to another map/target or is partial')
        for category in ('row_files', 'interval_summary_files'):
            for item in metric[category]:
                files.file(item['file'], item['sha256'], path.parent, 'candidate:angular:'+category)
        check(binary(metric['metric_operator_upper']) == exact(metric['selected_source_metric_upper']),
              'Angular source metric float is not its exact saved bound')
    else:
        files.prefix_source('db6f-prefix-metric-polynomial-storage.py', metric['script_sha256'])
        check(metric['intervals_checked'] == metric['intervals'] and explicit_target is not None,
              'Original prefix certificate needs complete coverage and explicit --prefix-target')
        target_path, target = files.json(explicit_target, metric['target_sha256'], path.parent, 'candidate:prefix-target')
    if explicit_target is not None:
        files.file(explicit_target, metric['target_sha256'], path.parent, 'candidate:explicit-prefix-target')
    check(hashlib.sha256(target_path.read_bytes()).hexdigest() == metric['target_sha256'] == bridge['target_sha256'] and
          target['geometry_sha256'] == hashlib.sha256(base_path.read_bytes()).hexdigest(), 'Target/base/bridge identity mismatch')
    same(target['frozen_profile'], geom['frozen_profile'], 'Target supplier changed the physical profile')
    same(target['bridge_constants'], ref['target']['bridge_constants'], 'Source bridge constants changed')
    files.prefix_source('db6f-prefix-metric-supplier-storage.py', target['script_sha256'])
    files.prefix_source('db6f-prefix-metric-polynomial-storage.py', target['arithmetic_backend_sha256'])
    check(target.get('prefix_bridge_extension_guard_passed') is True and
          target['data_sha256'] == metric['target_data_sha256'], 'Analytic target enclosure guard/data mismatch')
    files.file(target['data_file'], target['data_sha256'], target_path.parent, 'candidate:prefix-target-data')
    epsilon = binary(metric['metric_operator_upper'])
    eta = binary(bridge['relative_target_metric_difference_upper'])
    check(0 <= epsilon < 1 and 0 <= eta < 1, 'Invalid prefix/bridge error bound')
    result = epsilon*(1+eta)+eta
    if angular:
        check(result == exact(metric['exact_target_metric_operator_upper']) ==
              exact(metric['selected_exact_target_metric_upper']), 'Angular exact-target transfer was not applied once')
    return result


def tail_certificate(files, path, report, manifest_path, meta, defs, metric_only):
    digest = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    check(report['manifest_sha256'] == digest, 'A tail certificate belongs to another candidate map')
    files.file(report['manifest'], digest, path.parent, 'candidate:tail-report-manifest')
    packet_path, packet = files.json(report['packet'], report['packet_sha256'], path.parent, 'candidate:tail-packet')
    check(packet.get('finished') is True and packet['finite_tail_manifest_sha256'] == digest and
          packet['data_sha256'] == report['packet_data_sha256'], 'Tail packet data/map mismatch')
    definitions(files, packet['background_definition_hashes'], packet_path.parent, defs)
    files.file(packet['data_file'], packet['data_sha256'], packet_path.parent, 'candidate:tail-packet-data')
    files.file(report['row_data_file'], report['row_data_sha256'], path.parent, 'candidate:tail-rows')
    n = meta['totalUniqueNodes']-1
    check(report.get('entire_finite_tail_and_collar_covered') is True and report.get('collar_included') is True and
          type(report['packet_intervals']) is int and report['packet_intervals'] > 0 and
          report['checked_packet_intervals'] == report['packet_intervals'] and
          report['total_finite_spans'] == n and report['selected_span_interval'] == [-1, n] and
          report.get('metric_immersion_certified_on_checked_intervals') is True, 'Partial tail/collar certificate')
    if metric_only:
        files.source('db6f-audit-tail-metric-only.py', report['script_sha256'])
        check(report.get('complete_packet_partition_validated') is True and
              report.get('curvature_evaluated') is False and report.get('curvature_certified') is False,
              'Metric-only report has incorrect coverage/curvature scope')
        for name, digest in report['source_sha256'].items():
            check(name in SOURCES, 'Unknown metric-only implementation dependency')
            files.source(name, digest)
        curvature = None
    else:
        files.source('db6f-audit-tail-metric-curvature.py', report['script_sha256'])
        files.source('db6f-audit-metric-polynomial.py', report['polynomial_backend_sha256'])
        files.source('db6f-audit-continuous-hermite.py', report['interval_backend_sha256'])
        files.source('db6f_tail_integrated.py', report['reader_sha256'])
        check(report.get('curvature_all_checked_intervals_resolved') is True, 'Unresolved actual tail curvature')
        check(binary(report['background_curvature_upper_assumed']) >= Q(6),
              'Tail curvature used an unproved improvement of the frozen background bound')
        if 'streaming_geometry_adapter' in report:
            adapter = report['streaming_geometry_adapter']
            files.source('db6f-audit-tail-stream.py', adapter['sha256'])
            check(adapter['frozen_backend_sha256'] == SOURCES['db6f-audit-tail-metric-curvature.py'] and
                  adapter['changes_to_map_or_bound_formulas'] is False, 'Changed streaming representation')
        curvature = binary(report['principal_curvature_upper'])
        check(curvature > 0, 'Invalid actual tail curvature upper bound')
    upper = binary(report['metric_operator_upper'])
    check(0 <= upper < 1, 'Invalid tail metric upper bound')
    return upper, curvature


def candidate(files, whole_path, explicit_target, explicit_bridge_tail, ref):
    for name in PREFIX_SOURCES:
        files.prefix_source(name)
    whole_raw = whole_path.read_bytes()
    whole_path, whole = files.json(whole_path, hashlib.sha256(whole_raw).hexdigest(), whole_path.parent, 'candidate:whole')
    files.source('db6f-root-whole-metric-reach-v2.py', whole['script_sha256'])
    budget_path, budget = files.json(whole['closed_budget'], whole['closed_budget_sha256'], whole_path.parent, 'candidate:closed-budget')
    files.prefix_source('db6f-prefix-closed-budget-storage.py', budget['script_sha256'])
    files.source('db6f-root-closed-budget-v2.py', budget['base_closed_budget_script_sha256'])
    required = {'geometry', 'geometry_certificate', 'metric_certificate', 'moment_certificate',
                'tail_first', 'height', 'positive_alpha'}
    check(set(budget['inputs']) == required, 'Unexpected closed-budget input schema')
    bound = {key: files.item(budget['inputs'][key], budget_path.parent, 'candidate:'+key) for key in sorted(required)}
    check(budget['inputs']['height']['sha256'] == HEIGHT_SHA and
          budget['inputs']['positive_alpha']['sha256'] == POSITIVE_ALPHA_SHA,
          'Changed reviewed common-background height/positive-alpha proof')
    geom_path, geom = bound['geometry']
    geometry_sha = budget['inputs']['geometry']['sha256']
    check(whole['geometry_sha256'] == geometry_sha and geom['representation'] == 'exact-common-cut-prefix' and
          geom.get('exact_common_cut_C2_by_definition') is True and geom.get('mirror_inlet_C2_exact') is True,
          'Candidate is not the specified exact common-cut/mirrored map')
    for key in PREFIX_KEYS:
        same(geom[key], ref['geometry'][key], 'Different fixed prefix target/chart: '+key)
    for key, source in [('common_cut_implementation_sha256', 'db6f-prefix-common-cut-storage.py'),
                        ('wrapper_sha256', 'db6f-prefix-mirror-hermite-storage.py')]:
        files.prefix_source(source, geom[key])
    for key, source in [('profile_loader_sha256', 'db6f-prefix-flat-geometry-source.py'),
                        ('profile_implementation_sha256', 'db6f-prefix-flat-profile.py'),
                        ('tail_reader_sha256', 'db6f_tail_integrated.py')]:
        files.source(source, geom[key])
    base_path, base = files.json(geom['base_geometry'], geom['base_geometry_sha256'], geom_path.parent, 'candidate:base-prefix')
    for key in PREFIX_KEYS:
        same(base[key], geom[key], 'Common-cut metadata changed a copied target field: '+key)
    check(base['data_sha256'] == geom['data_sha256'], 'Common-cut base-data identity mismatch')
    files.prefix_source('db6f-prefix-fullxyz-hermite-storage.py', base['script_sha256'])
    storage_bindings = prefix_storage(files, base_path, base, geom)
    files.file(base['checkpoint'], base['checkpoint_sha256'], base_path.parent, 'candidate:prefix-checkpoint')
    files.file(base['linear_port'], base['port_sha256'], base_path.parent, 'candidate:prefix-port')
    manifest_path, meta = files.json(geom['tail_manifest'], geom['tail_manifest_sha256'], geom_path.parent, 'candidate:manifest')
    check(whole['tail_manifest_sha256'] == geom['tail_manifest_sha256'], 'Whole report refers to another tail map')
    manifest_files(files, manifest_path, meta, 'candidate:manifest')
    bridge_path, bridge = files.json(geom['bridge_parameter_certificate'], geom['bridge_parameter_certificate_sha256'],
                                     geom_path.parent, 'candidate:bridge')
    files.source('db6f-root-exact-bridge.py', bridge['script_sha256'])
    check(bridge['geometry_sha256'] == geom['base_geometry_sha256'] and bridge['unique_root_in_box'] is True,
          'Exact bridge is not bound to the new base prefix')
    for key in BRIDGE_KEYS:
        same(bridge[key], ref['bridge'][key], 'Changed exact bridge target/root definition: '+key)
    cut, slope = binary(meta['parameters']['rCut']), binary(meta['parameters']['wCut'])
    check(cut == Q(bridge['physical_cut_radius_exact']) and slope == Q(bridge['physical_cut_slope_exact']) and
          -7*slope/cut == Q(bridge['physical_cut_second_derivative_exact']), 'Physical cut target mismatch')
    # A bridge certificate may cite an earlier numerical tail grid: only its
    # target/root and this exact physical cut are used, never an old tail bound.
    if bridge['tail_manifest_sha256'] == geom['tail_manifest_sha256']:
        bridge_tail_path, bridge_tail = manifest_path, meta
        if explicit_bridge_tail is not None:
            files.file(explicit_bridge_tail, bridge['tail_manifest_sha256'], bridge_path.parent, 'candidate:bridge-support-manifest')
    else:
        check(explicit_bridge_tail is not None,
              'A distinct bridge-support manifest requires explicit --bridge-tail-manifest')
        bridge_tail_path, bridge_tail = files.json(explicit_bridge_tail, bridge['tail_manifest_sha256'],
                                                   bridge_path.parent, 'candidate:bridge-support-manifest')
    check(bridge_tail.get('finished') is True, 'Bridge-support manifest is incomplete')
    _, bridge_cp = files.json(bridge_tail['input'], bridge_tail['inputSHA256'],
                              bridge_tail_path.parent, 'candidate:bridge-support-checkpoint')
    parameters(checkpoint_parameters(bridge_cp), bridge_tail['parameters'])
    parameters(ref['manifest']['parameters'], bridge_tail['parameters'])
    parameters(bridge_tail['parameters'], meta['parameters'])
    geom_cert = bound['geometry_certificate'][1]
    metric_path, metric = bound['metric_certificate']
    moment = bound['moment_certificate'][1]
    for name, report in [('geometry', geom_cert), ('metric', metric), ('moment', moment)]:
        check(report['geometry_sha256'] == geometry_sha, 'Another graph supplied the '+name+' certificate')
    files.prefix_source('db6f-prefix-continuous-hermite-storage.py', geom_cert['script_sha256'])
    files.prefix_source('db6f-prefix-volume-moment-storage.py', moment['script_sha256'])
    check(geom_cert.get('entire_finite_prefix_covered') is True and geom_cert.get('continuous_bounds_certified') is True and
          geom_cert.get('mirror_interface_certified') is True and geom_cert['data_sha256'] == geom['data_sha256'] and
          moment['data_sha256'] == geom['data_sha256'], 'Incomplete/mismatched prefix geometric or moment certificate')
    first = bound['tail_first'][1]
    check(first['manifestSHA256'] == geom['tail_manifest_sha256'] and first['entireTail']['planarJacobianPositive'] is True and
          first['entireTail']['allCrossSectionsSimple'] is True, 'Tail first-jet certificate is not for this new map')
    first_source = next((name for name in ('db6f-tail-first-bounds.py', 'db6f-tail-first-bounds-stream.py')
                         if SOURCES[name] == first['scriptSHA256']), None)
    check(first_source is not None, 'Unknown tail first-jet implementation')
    files.source(first_source, first['scriptSHA256'])
    files.source('db6f_tail_integrated.py', first['readerSHA256'])
    files.source('db6f-audit-continuous-hermite.py', first['intervalBackendSHA256'])
    defs, changed = transfer(files, budget['same_background_transfer'], budget_path.parent, manifest_path, meta, ref,
                             bound['height'][1], bound['positive_alpha'][1], bound['height'][0])
    pref_upper = prefix_metric(files, metric_path, metric, geom_path, geom, base_path, bridge, explicit_target, ref)
    check(pref_upper == exact(budget['corrected_prefix_exact_target_metric_upper']) == exact(whole['prefix_metric_upper']),
          'Prefix/bridge budget arithmetic differs')
    full_path, full = files.json(whole['tail_certificate'], whole['tail_certificate_sha256'], whole_path.parent, 'candidate:full-tail-certificate')
    tail_upper, tail_curvature = tail_certificate(files, full_path, full, manifest_path, meta, defs, False)
    original_tail_upper = tail_upper
    check(exact(whole['original_full_certificate_tail_metric_upper']) == tail_upper,
          'Whole report changed the complete-tail original metric upper')
    check(whole['packet_sha256'] == full['packet_sha256'] and whole['packet_data_sha256'] == full['packet_data_sha256'] and
          whole['tail_rows_sha256'] == full['row_data_sha256'], 'Whole/full-tail data link mismatch')
    extra = whole['separate_tail_metric_certificate']
    if extra is not None:
        extra_path, extra_report = files.item(extra, whole_path.parent, 'candidate:separate-metric-certificate')
        extra_upper, _ = tail_certificate(files, extra_path, extra_report, manifest_path, meta, defs, True)
        check(extra['manifest_sha256'] == geom['tail_manifest_sha256'] and extra['packet_sha256'] == extra_report['packet_sha256'] and
              extra['packet_data_sha256'] == extra_report['packet_data_sha256'] and extra['row_data_sha256'] == extra_report['row_data_sha256'] and
              extra['complete_rows_rechecked'] == extra_report['packet_intervals'] and
              extra['curvature_source_is_unchanged_full_certificate'] is True and exact(extra['metric_upper']) == extra_upper,
              'Separate metric binding/scalar mismatch')
        same(extra['same_background_definition_hashes'], defs, 'Separate metric uses another target')
        tail_upper = min(tail_upper, extra_upper)
    upper = max(pref_upper, tail_upper, Q(0))
    check(exact(whole['tail_metric_upper']) == tail_upper and exact(whole['whole_metric_operator_upper']) == upper,
          'Whole metric is not the exact component maximum')
    prefix_curvature = binary(geom_cert['principal_curvature_upper'])
    curvature = max(prefix_curvature, tail_curvature, Q(10, 3))
    check(exact(whole['prefix_curvature_upper']) == prefix_curvature and exact(whole['tail_curvature_upper']) == tail_curvature and
          exact(whole['cap_curvature_upper']) == Q(10, 3) and exact(whole['whole_principal_curvature_upper']) == curvature,
          'Whole curvature is not from this candidate own prefix/tail certificates')
    support, diameter = exact(budget['whole_surface_support_lower']), exact(budget['diameter_upper'])
    check(support > 0 and diameter > 0 and curvature > 0, 'Invalid closed geometric quantities')
    reach = min(support, 1/curvature)
    check(exact(whole['whole_support_lower']) == support and exact(whole['diameter_upper']) == diameter and
          exact(whole['whole_reach_lower_by_R10']) == reach and exact(whole['whole_reach_over_diameter_lower']) == reach/diameter,
          'Whole reach composition differs')
    check(budget['embedding_all_phases_follows_from_support_given_reviewed_assembly'] is True and
          budget['rigid_noncongruence_follows_from_moment_given_reviewed_assembly'] is True and
          whole['all_phases_by_R17_rotation_and_material_action'] is True and
          whole['README_geometric_and_metric_thresholds_1_2_3_4_6_paid_given_reviewed_inputs'] is True,
          'Reviewed closed/all-phase assembly input is missing')
    return upper, {'geometry_sha256': geometry_sha, 'manifest_sha256': geom['tail_manifest_sha256'],
                   'prefix_upper_exact': str(pref_upper), 'full_tail_metric_upper_exact': str(original_tail_upper),
                   'prefix_storage_bindings': storage_bindings,
                   'selected_tail_metric_upper_exact': str(tail_upper), 'whole_upper_exact': str(upper),
                   'own_prefix_curvature_upper_exact': str(prefix_curvature),
                   'own_tail_curvature_upper_exact': str(tail_curvature),
                   'different_approved_transfer_parameters': changed,
                   'bridge_support_manifest_sha256': bridge['tail_manifest_sha256'],
                   'bridge_support_physical_parameters_checked': True,
                   'same_g_prefix_fields': list(PREFIX_KEYS), 'same_g_exact_bridge_fields': list(BRIDGE_KEYS),
                   'background_definition_sha256': BACKGROUND,
                   'cap_same_g_reason': 'Identical frozen R16 bump/cuff definition; vertical translations preserve its induced metric.',
                   'independent_complete_input_certificates_remain_proof_dependencies': True}


def scalar_gate(upper, lower):
    check(0 <= upper < 1 and lower > 0, 'Invalid whole upper or old positive lower')
    return {'threshold_exact': str(BOUND), 'tested_whole_upper_exact': str(upper),
            'old_M12_lower_exact': str(lower), 'strict_decrease_factor_exact': str(FACTOR),
            'terminal_metric_gate_passed': upper <= BOUND,
            'strict_actual_decrease_gate_passed': lower > FACTOR*upper,
            'strict_decrease_margin_exact': str(lower-FACTOR*upper),
            'fixed_threshold_factor_margin_exact': str(lower-FACTOR*BOUND)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--whole', type=Path)
    mode.add_argument('--check-m12-negative', action='store_true')
    parser.add_argument('--prefix-target', type=Path,
                        help='Required only when the original prefix report omits a target-file path')
    parser.add_argument('--bridge-tail-manifest', type=Path,
                        help='Required when the exact bridge cites a different numerical tail manifest')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    check(not args.out.exists(), 'Refusing to overwrite a previous output')
    check(not args.check_m12_negative or (args.prefix_target is None and args.bridge_tail_manifest is None),
          'M12 test accepts no future target or bridge-support input')
    files = Files()
    paths, ref, lower = reference(files)
    if args.check_m12_negative:
        upper = exact(ref['whole']['whole_metric_operator_upper'])
        scalar = scalar_gate(upper, lower)
        check(not scalar['terminal_metric_gate_passed'] and lower > BOUND and
              not scalar['strict_actual_decrease_gate_passed'], 'The genuine M12 negative fixture did not reject')
        report = {'status': 'EXPECTED_REJECTION', 'mode': 'frozen-M12-negative-scalar-fixture',
                  'test_only': True, 'certificate_issued': False,
                  'actual_M12_error_strictly_exceeds_threshold': True,
                  'candidate_binding_branch_executed': False, 'future_candidate_was_created': False,
                  'scalar': scalar,
                  'scope': 'Only the frozen actual M12 identity and exact scalar rejection were checked. The normal new-candidate branch was not run.'}
        exit_code = 0
    else:
        upper, binding = candidate(files, args.whole, args.prefix_target, args.bridge_tail_manifest, ref)
        scalar = scalar_gate(upper, lower)
        passed = scalar['terminal_metric_gate_passed'] and scalar['strict_actual_decrease_gate_passed']
        report = {'status': 'PASS-terminal-fixed-g-error-and-one-actual-decrease' if passed else 'REJECTED-terminal-error-or-decrease-gate',
                  'mode': 'reviewed-new-candidate-posterior', 'test_only': False,
                  'certificate_issued': passed, 'candidate_binding_branch_executed': True,
                  'candidate': binding, 'scalar': scalar,
                  'scope': 'Conditional composition of independently reviewed complete same-map/same-g certificates. One terminal bound and one strict actual decrease are paid; no new analytic certification or limit existence is inferred.'}
        exit_code = 0 if passed else 2
    report.update(script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  checked_files=files.output(), actual_new_root_flow_solver_calls=0,
                  numerical_backends_imported=False, radial_grid_evaluated=False,
                  metric_curvature_recomputed=False, packet_or_manifest_generated=False,
                  fixed_g_convergence_gate_5_paid=False,
                  independent_final_full_pipeline_verified=False,
                  infinite_solution_existence_proved=False, README_complete=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'status': report['status'], 'certificate_issued': report['certificate_issued'],
                      'terminal_metric_gate_passed': scalar['terminal_metric_gate_passed'],
                      'strict_actual_decrease_gate_passed': scalar['strict_actual_decrease_gate_passed'],
                      'checked_files': len(report['checked_files']), 'README_complete': False}))
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
