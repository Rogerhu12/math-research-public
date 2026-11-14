#!/usr/bin/env python3
"""Original accepted quintic/fullmean audit with explicit current-anchor hook.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No actual field is loaded in --anchor-prepare-only mode. Actual execution
retains all original accepted-field, provider, mean, and polynomial gates.
"""
import argparse
import json
from pathlib import Path
from strong_frontload_anchor_loader_adapter import build


def main():
    p=argparse.ArgumentParser(add_help=False)
    p.add_argument('--anchor-prepare-only',type=Path)
    a,remaining=p.parse_known_args()
    namespace,provenance=build('audit',__file__)
    if a.anchor_prepare_only:
        if remaining:raise ValueError('Source-only preparation takes no invented accepted input')
        if a.anchor_prepare_only.exists():raise FileExistsError('Fresh anchor audit preparation required')
        a.anchor_prepare_only.parent.mkdir(parents=True,exist_ok=True)
        a.anchor_prepare_only.write_text(json.dumps(dict(prepared=True,actual_fields_loaded=0,
            ODE_Node_Newton_calls=0,frontload_anchor_adapter=provenance),indent=2)+'\n')
        print(json.dumps(dict(prepared=True,actual_fields_loaded=0,out=str(a.anchor_prepare_only))),flush=True)
        return
    namespace['main']()


if __name__=='__main__':main()
