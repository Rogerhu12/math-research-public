"""Receive the two immutable original archives before the unchanged common driver."""
import argparse
import json
import os
from pathlib import Path
import time

from completed_artifact_prefetch_20261128 import REPO, emit, plain, receive, require, utc


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--first-metadata',required=True)
    parser.add_argument('--first-zip',required=True)
    parser.add_argument('--parent-metadata',required=True)
    parser.add_argument('--parent-zip',required=True)
    parser.add_argument('--state',required=True)
    args=parser.parse_args()
    require(os.environ.get('GITHUB_ACTIONS')=='true'
            and os.environ.get('GITHUB_REPOSITORY','').lower()==REPO.lower()
            and os.environ.get('GITHUB_RUN_ID','').isdigit(),
            'the two original archives are received only in public Actions')
    state=Path(args.state)
    require(not state.exists(),'do not replace another working scientific state')
    output=state/'transport'/(os.environ['GITHUB_RUN_ID']+'-original-pair.json')
    output.parent.mkdir(parents=True)
    start=time.monotonic()
    record=dict(started_at=utc(),consumer_run=os.environ['GITHUB_RUN_ID'],
                scientific_evaluations=0,old_log_requests=0)
    for name,metadata,path in [('first_completed_checkpoint',args.first_metadata,args.first_zip),
                               ('original_R750_parent',args.parent_metadata,args.parent_zip)]:
        spec=json.loads(Path(metadata).read_text())
        record[name]=receive(spec,Path(path))
        record['administrative_seconds']=time.monotonic()-start
        output.write_text(plain(record)+'\n')
    record.update(completed_at=utc(),transport_complete=True,
                  signed_addresses_and_credentials_written=False)
    output.write_text(plain(record)+'\n')
    emit(record)


if __name__=='__main__':
    try:
        main()
    except Exception as error:
        emit(dict(transport_complete=False,error_type=type(error).__name__,
                  error=str(error) if isinstance(error,ValueError) else 'original-byte transport failed',
                  scientific_evaluations=0))
        raise SystemExit(2) from None
