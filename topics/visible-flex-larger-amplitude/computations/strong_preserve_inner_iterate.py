#!/usr/bin/env python3
"""Copy one complete pending Newton checkpoint beyond the active retention set.

Every original compressed byte and relative chunk name is retained. No solve,
physical audit, RMS calculation or success promotion occurs. Existing files
are not overwritten and active ledgers/pointers are not included.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path


def digest(value):
    return hashlib.sha256(value).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('topic', 'raw', 'destination', 'manifest'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--expected-sha256', required=True)
    parser.add_argument('--run-log-alpha', type=float, required=True)
    parser.add_argument('--active-session', type=int, required=True)
    args = parser.parse_args()
    topic = args.topic.resolve()
    source, destination, output = (p.resolve() for p in (args.raw,args.destination,args.manifest))
    if (not all(p.is_relative_to(topic/'notes') for p in (source,destination,output))
            or destination.exists() or output.exists() or not 0 < args.run_log_alpha <= 1):
        raise ValueError('Require fresh local notes paths and the reported positive original step')
    data = source.read_bytes()
    if digest(data) != args.expected_sha256:
        raise ValueError('Observed immutable raw manifest SHA differs')
    record = json.loads(gzip.decompress(data))
    provenance = record['provenance']
    if (record['solver_success'] or record['physical_surface'] or
            not provenance['actual_coupled_acceptance_pending'] or
            provenance['phase'] != 'accepted-newton'):
        raise ValueError('Expected an explicitly pending accepted inner checkpoint')
    destination.mkdir()
    rows = []
    def copy(name, contents, expected):
        if Path(name).name != name or digest(contents) != expected:
            raise ValueError('Nonlocal or changed original chunk')
        target = destination/name
        temporary = target.with_name(target.name+'.tmp')
        temporary.write_bytes(contents)
        temporary.replace(target)
        if digest(target.read_bytes()) != expected or len(contents) >= 5_000_000:
            raise ValueError('Preserved-byte check or individual file-size gate failed')
        rows.append(dict(path=str(target.relative_to(topic)),bytes=len(contents),sha256=expected))
    for spec in record['arrays'].values():
        for chunk in spec['chunks']:
            name = chunk['file']
            if Path(name).name != name:
                raise ValueError('Raw array piece path is not local')
            copy(name,(source.parent/name).read_bytes(),chunk['sha256'])
    copy(source.name,data,args.expected_sha256)
    own = Path(__file__).resolve()
    own_data = own.read_bytes()
    rows.append(dict(path=str(own.relative_to(topic)),bytes=len(own_data),sha256=digest(own_data)))
    summary = dict(scope=__doc__,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        active_session=args.active_session,source_manifest=str(source.relative_to(topic)),
        preserved_manifest=str((destination/source.name).relative_to(topic)),
        run_log_alpha=args.run_log_alpha,alpha_is_taken_from_run_log_not_recomputed_here=True,
        newton_iteration=provenance['iteration'],inner_call=provenance['call'],
        scaled_collocation_max=provenance['scaled_collocation_max'],boundary_max=provenance['boundary_max'],
        solver_success=False,physical_surface=False,actual_coupled_acceptance_pending=True,
        all_piece_hashes_checked=True,files=rows,total_bytes=sum(r['bytes'] for r in rows),
        excluded=['active latest pointer','active iterate ledger','active stdout log','active disk events'])
    output.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(manifest=str(output.relative_to(topic)),sha256=digest(output.read_bytes()),
        preserved_manifest=summary['preserved_manifest'],files=len(rows),total_bytes=summary['total_bytes'])),flush=True)


if __name__ == '__main__':
    main()
