#!/usr/bin/env python3
"""Freeze the compact record of nineteen actually completed current fields.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This archive consumes the original owned nineteen-field reader receipt.  It
preserves exact bytes of all small reconstruction records, without duplicating
the cheaply reproducible arrays.  It performs no ODE or geometric evaluation.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


READER_SHA = 'b69abdc1f615a9d96b65fb187f2e87831bf975f5b2752303db4c10c37f9c3b84'
EXACT_READER_SHA = '167de07932c93a60fda5f5a1c51d32933027f108fdb73171f908db30228224cf'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def save_fresh(path, data):
    path = Path(path)
    if path.exists():
        raise FileExistsError(path)
    if len(data) >= 5_000_000:
        raise ValueError('A compact archive item must stay below five MB')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return dict(path=str(path), sha256=sha(path), bytes=len(data))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--reader', type=Path, required=True)
    parser.add_argument('--reader-resource', type=Path, required=True)
    parser.add_argument('--top', type=Path, required=True)
    parser.add_argument('--tag', required=True)
    args = parser.parse_args()
    plan, receipt, owned = map(read, (args.plan, args.reader, args.reader_resource))
    if not (receipt['schema'] == 'actual-current-M32-nineteen-field-anchor-reader-bridge-v1'
            and receipt['source_sha256'] in (READER_SHA, EXACT_READER_SHA)
            and receipt['all_identity_gates'] and receipt['total_fields'] == 19
            and receipt['plan_sha256'] == sha(args.plan)):
        raise ValueError('Require the original complete current-nineteen reader receipt')
    if not (owned['wait4_observed'] and owned['exitcode'] == 0
            and owned['termination_signal'] is None
            and '--verify-only' in owned['command']
            and str(args.plan) in owned['command']
            and str(args.reader) in owned['command']):
        raise ValueError('Require the original owned completed reader invocation')
    if Path.cwd() != Path(plan['cwd']):
        raise ValueError('Keep the actual producer path identities')
    if (plan['baseline_only'] or plan['modes'] != 32
            or receipt['complete_mean_angular'] != 1552
            or receipt['old_coarse_or_stale_derivative_fields_used']
            or receipt['common_shape'][1:] != [768, 3]
            or receipt['full_finite_row_count'] != 5 * receipt['common_shape'][0] * 768):
        raise ValueError('The complete current-M32 grid or scope changed')

    embedded = {}

    def retain(path, expected=None):
        path = Path(path)
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if expected is not None and digest != expected:
            raise ValueError('A completed small reconstruction record changed: ' + str(path))
        if len(data) >= 1_000_000:
            raise ValueError('Large scientific inputs/arrays are referenced, not duplicated')
        entry = dict(path=str(path), sha256=digest, bytes=len(data), utf8=data.decode('utf-8'))
        previous = embedded.setdefault(str(path), entry)
        if previous != entry:
            raise ValueError('An embedded path changed during archive construction')

    retain(args.plan)
    retain(Path(plan['grid']))
    retain(args.reader)
    retain(args.reader_resource)
    recovery_plan = plan
    visited_recovery_plans = set()
    while 'io_only_interruption_recovery' in recovery_plan:
        recovery = recovery_plan['io_only_interruption_recovery']
        if recovery['original_plan'] in visited_recovery_plans:
            raise ValueError('A recovery provenance chain must be acyclic')
        visited_recovery_plans.add(recovery['original_plan'])
        retain(recovery['receipt'], recovery['sha256'])
        retain(recovery['original_plan'], recovery['original_plan_sha256'])
        recovery_plan = read(recovery['original_plan'])
    exact_proofs = receipt.get('actual_exact_chart_order_reader_adapter', {}).get('actual_field_proofs', [])
    if exact_proofs:
        if receipt['source_sha256'] != EXACT_READER_SHA or receipt['original_reader_source_sha256'] != READER_SHA:
            raise ValueError('Require the explicitly frozen exact-order reader identity')
        definition = plan['actual_current_exact_chart_order_field_plan']
        retain(definition['original_plan'], definition['original_plan_sha256'])
        retain(definition['original_chart_probe'], definition['original_chart_probe_sha256'])
        for proof in exact_proofs:
            for key in ('proof', 'original_failed_report', 'original_failed_resource'):
                retain(proof[key], proof[key + '_sha256'])
        for source, expected in plan['source_and_input_sha256'].items():
            if source.endswith('source-preparation.json') or source.endswith('chart-probe-r1-resource.json'):
                retain(source, expected)
    by_name = {row['name']: row for row in receipt['fields']}
    if set(by_name) != {row['name'] for row in plan['candidates']}:
        raise ValueError('The actual nineteen names changed')
    fields = []
    chunks = []
    for row in plan['candidates']:
        saved = by_name[row['name']]
        for key in ('report', 'resource', 'field'):
            retain(row[key], saved[key + '_sha256'])
        retain(saved['source_preparation'], saved['source_preparation_sha256'])
        report, resource, storage = map(read, (row['report'], row['resource'], row['field']))
        command = row['command'][row['command'].index('--') + 1:]
        if not (resource['wait4_observed'] and resource['exitcode'] == 0
                and resource['termination_signal'] is None and resource['command'] == command
                and report['finished'] and report['finite_domain_passed']
                and report['geometry_fields']['mean_quadrature']['angular'] == 1552
                and not report['nonlinear_solution'] and report['worker_start_attempts'] == 0):
            raise ValueError('The original actual field resource or completion gates changed')
        for item in storage['chunks']:
            chunks.append(dict(field=row['name'], path=str(Path(row['field']).with_name(item['file'])), **item))
        fields.append(dict(name=row['name'], direction=row['direction'], physical_step=row['step'],
            original_command=row['command'], report_sha256=saved['report_sha256'],
            resource_sha256=saved['resource_sha256'], field_manifest_sha256=saved['field_sha256'],
            wall_seconds=resource['wall_seconds'], peak_rss_kib=resource['peak_rss_kib'],
            finite_domain_passed=True, complete_mean_angular=1552,
            kappa_abs_max_sample=report['geometry_fields']['kappa_abs_max_sample'],
            twice_norm_max_sample=report['geometry_fields']['twice_radius_max_sample']))
    if (len(chunks) != receipt['total_chunks']
            or sum(item['bytes'] for item in chunks) != receipt['total_compressed_derived_array_bytes']):
        raise ValueError('The full derived-array inventory changed')
    response = Path(receipt['response_file'])
    if sha(response) != receipt['response_sha256']:
        raise ValueError('The genuinely completed current nine response changed')

    packet = dict(schema='current-M32-complete-nineteen-field-reconstruction-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
        actual_plan_sha256=sha(args.plan), original_reader_sha256=sha(args.reader),
        original_reader_resource_sha256=sha(args.reader_resource), cwd=plan['cwd'],
        actual_current_response=dict(path=str(response), sha256=sha(response)),
        current_fields=fields, exact_small_file_bytes=list(embedded.values()),
        complete_derived_array_inventory=chunks,
        total_derived_array_bytes=sum(item['bytes'] for item in chunks),
        derived_arrays_scratch_only=True, all_19_fields_actually_completed=True,
        no_old_coarse_fields_used=True, no_new_ODE_Node_Jacobian_or_field=True,
        no_new_accepted_solution_or_continuous_geometry_certificate=True)
    prefix = args.top / 'notes' / args.tag
    packet_path = Path(str(prefix) + '-reconstruction.json.gz')
    save_fresh(packet_path, gzip.compress((json.dumps(packet, indent=2) + '\n').encode(), mtime=0))
    proof = f'''# Current A M32: complete nineteen-field finite geometry input

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

The unique accepted-A comparison baseline and all eighteen two-sided current
direction fields have actually completed the original domain and full-grid
checks. Every field retains all 32 core modes, the same {receipt['common_shape'][0]}
radial points and 768 angles, and the original complete mean at 1552 angles.
The current accepted physical-quintic curvature witness is included in this
common grid. The raw-state cubic comparison fields and the accepted physical
quintic remain different objects.

The original reader `{READER_SHA}`, with the separately identified exact-order
outer-entry bridge when declared in the receipt, completed
{receipt['gate_count']} original identity checks. It rehashed all
{receipt['total_chunks']} stored chunks and checked
their complete ordered radial coverage, every actual provider fingerprint,
the exact command and owned exit status of each field, the common grid, and
the genuinely completed current nine-control response
`{receipt['response_sha256']}`. No old M28 field, padded old derivative,
partial response or future state is substituted. The baseline was reused;
only its eighteen direction fields were newly evaluated.

These arrays contain the two principal-curvature samples and twice the
position norm. Their five signed/size constraint families contain
{receipt['full_finite_row_count']:,} finite rows. This archive does not claim
that a minimax candidate has already passed those rows: the subsequent
consumer must load the complete arrays and replay every row for its selected
numerical prediction. Finite differences, complete core-tail constraints,
and the exact binary-rational full-core gap G=2 sum(c[0],c[2],...,c[30]) remain
design evidence. Original nonlinear BVP, complete inlet, actual warm-field,
continuous reach, full closed diameter and set-Hausdorff requirements are
not discharged by these direction fields.

## Reproduction and storage

The compact reconstruction packet preserves the exact UTF-8 bytes, original
paths and SHA-256 of the plan, grid, all field screens, owned resources,
storage manifests, and provider-preparation records. Its complete inventory
contains every derived array's filename, shape interval, byte count and SHA.
The {receipt['total_compressed_derived_array_bytes']:,} derived bytes remain
in scratch under repository rule 11. Reproduction uses each verbatim owned
command, the pinned actual accepted/raw/response inputs and the saved grid;
the regenerated arrays are compared against those original byte hashes.
No large derived array is duplicated into Git by this archive.
'''
    if exact_proofs:
        proof += '''
## Explicit exact-order identity for the Ksync negative field

The original minus-0.002 Ksync field exited 1 at the strict displayed-grid
orientation predicate. Its completed negative record remains in the archive.
All 2590 original raw physical knots were strictly increasing; one pair of
common-grid t values, separated by one Float64 ULP in the same chart piece,
had displayed equal physical s values. The corresponding exact stored
binary-coefficient polynomial difference is strictly positive. The fresh
entry additionally verifies every raw and common exact adjacent difference
(2589 + 3766 = 6355 pairs), and every original piece's Bernstein derivative
lower bound. The common pair is retained twice at its original input values.

The cubic uses only the original strictly increasing raw physical knots.
All geometry jets use analytic cubic derivatives, and the reviewed Gauss6
routine uses original raw intervals; no common-grid adjacent ds is a
derivative denominator. The unchanged complete-mean formulas can therefore
evaluate the original finite grid with the explicit exact-order predicate.
The current native entry, its exact reverse source edits, the actual proof,
all source identities, the original failure and all finite physical inputs
are retained. This does not certify arbitrary binary-polynomial seam
continuity, floating chart alignment, or continuous curvature.
'''
    proof_path = Path(str(prefix) + '-proof.md')
    save_fresh(proof_path, proof.encode())
    source_target = args.top / 'computations' / Path(__file__).name
    data = Path(__file__).read_bytes()
    if source_target.exists():
        if source_target.read_bytes() != data:
            raise ValueError('A frozen archive source cannot be replaced')
    else:
        source_target.write_bytes(data)
    files = [dict(path=str(path.relative_to(args.top)), sha256=sha(path), bytes=path.stat().st_size)
             for path in (source_target, packet_path, proof_path)]
    if exact_proofs:
        for name in ('root_actual_current_geometry_exact_chart_order.py',
                     'root_geometry_current_exact_chart_reader.py'):
            source = Path(__file__).parent / name
            target = args.top / 'computations' / name
            data = source.read_bytes()
            if target.exists():
                if target.read_bytes() != data:
                    raise ValueError('A frozen exact-order source cannot be replaced')
            else:
                target.write_bytes(data)
            files.append(dict(path=str(target.relative_to(args.top)), sha256=sha(target), bytes=len(data)))
    manifest_path = Path(str(prefix) + '-manifest.json')
    manifest = dict(schema='actual-current-M32-nineteen-field-compact-archive-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', files=files,
        total_bytes=sum(item['bytes'] for item in files), actual_completed_fields=19,
        original_owned_field_exitcodes_all_zero=True, baseline_recomputed=False,
        complete_finite_row_count=receipt['full_finite_row_count'],
        original_exact_chart_order_field_proofs=len(exact_proofs),
        all_derived_chunks_preserved_by_hash=True, derived_arrays_archived=False,
        no_continuous_geometry_or_new_solution_claimed=True)
    save_fresh(manifest_path, (json.dumps(manifest, indent=2) + '\n').encode())
    print(json.dumps(dict(manifest=str(manifest_path), sha256=sha(manifest_path),
        files=len(files), total_bytes=manifest['total_bytes'], actual_fields=19)), flush=True)


if __name__ == '__main__':
    main()
