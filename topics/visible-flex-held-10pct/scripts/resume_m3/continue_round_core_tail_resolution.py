#!/usr/bin/env python3
"""Actual round-core continuation with a finer finite tail shooting mesh.

All physical controls and the original tail acceptance gate are retained.
The original warm-remeshing worker supplies the new multiple-shooting guess.
This changes finite numerical resolution and is not a fixed-g proof by itself.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import continue_round_core as driver


def main():
    p=argparse.ArgumentParser(add_help=False,allow_abbrev=False)
    p.add_argument('--tail-parts',type=int)
    p.add_argument('--tail-steps',type=int)
    a,rest=p.parse_known_args()
    if a.tail_parts is None and a.tail_steps is None:
        raise ValueError('Specify an actual finite-tail refinement')
    out=Path(rest[rest.index('--outdir')+1]).resolve()
    record=dict(scope=__doc__,outer_command=sys.argv,
        source_sha256={str(f.resolve()):hashlib.sha256(f.read_bytes()).hexdigest()
            for f in [Path(__file__),Path(driver.__file__)]})
    original_run=subprocess.run
    def save():
        if out.exists():
            (out/'tail-resolution-record.json').write_text(json.dumps(record,indent=2)+'\n')
    def run(command,**kwargs):
        cfg_path=Path(command[command.index('--tail-config')+1]);cfg=json.loads(cfg_path.read_text())
        before={k:cfg.get(k) for k in ('shootingParts','steps','solveTolerance','modes','quadrature')}
        for key,value in [('shootingParts',a.tail_parts),('steps',a.tail_steps)]:
            if value is not None:
                if value<cfg[key]:raise ValueError('This entry only increases tail resolution')
                cfg[key]=value
        if all(cfg[k]==before[k] for k in ('shootingParts','steps')):
            raise ValueError('Requested tail mesh is unchanged')
        cfg_path.write_text(json.dumps(cfg,indent=2)+'\n')
        record.update(before=before,after={k:cfg.get(k) for k in before},
            actual_command=command,tail_config_sha256=hashlib.sha256(cfg_path.read_bytes()).hexdigest())
        save();return original_run(command,**kwargs)
    subprocess.run=run;sys.argv=[str(Path(driver.__file__))]+rest
    try:driver.main()
    except SystemExit as exc:
        record['driver_exit_code']=exc.code;raise
    except Exception as exc:
        record['startup_exception']=repr(exc);raise
    finally:save()


if __name__=='__main__':main()
