#!/usr/bin/env python3
"""R89 constructor CLI with correctly scoped stdout flushing.

The first constructor genuinely returned and wrote its metadata; its frozen
CLI then exited 1 because json.dumps was given print's flush parameter.  This
independent successor keeps that actual source/result/error and changes only
report/console plumbing. It imports the exact unchanged mathematical class.
"""
import argparse
import json
from pathlib import Path

import actual_closed_sharp_full_disk_marker as actual

CORE_SHA = 'e44cbdaab91969e0bdfeec432a5e6c52126c9b6d6219cbca0e22c91233200f96'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('source-run','geometry-bundle','node-check','old-geometry-report','out'):
        parser.add_argument('--'+key,type=Path,required=True)
    args = parser.parse_args()
    if actual.sha(actual.__file__) != CORE_SHA:
        raise ValueError('The exact unchanged R89 mathematical implementation changed')
    if args.out.exists():
        raise FileExistsError('Keep each actual returned constructor report immutable')
    model = actual.ActualClosedSharpFullDiskMarker(
        args.source_run,args.geometry_bundle,args.node_check,args.old_geometry_report)
    try:
        report = model.metadata()
        report['source_sha256'] = CORE_SHA
        report['actual_cli_source'] = dict(path=str(Path(__file__).resolve()),sha256=actual.sha(__file__))
        report['entry_constructor_actually_returned'] = True
        report['new_full_numerical_query_or_mesh_claimed'] = False
        report['mathematical_constructor_modified'] = False
        args.out.parent.mkdir(parents=True,exist_ok=True)
        with args.out.open('x') as stream:
            stream.write(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(output=str(args.out.resolve()),sha256=actual.sha(args.out))),flush=True)
    finally:
        model.close()


if __name__ == '__main__':
    main()
