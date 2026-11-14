#!/usr/bin/env python3
"""Fresh-process entry point for the unchanged true forward density v9 kernel."""
import argparse
import json
from pathlib import Path
from flint import ctx
from fourfold_retarget_reference_jets import RetargetReference
from fourfold_forward_density_pipeline_composition_v9 import run_leaf


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--arguments',type=Path,required=True)
    request=parser.parse_args()
    doc=json.loads(request.arguments.read_text())
    args=argparse.Namespace(**doc['arguments'])
    for name in ('descriptor','cover','out_directory','reference_seams',
                 'real_gate_directory','expanded_domain_directory','stop_file'):
        value=getattr(args,name,None)
        if value is not None:setattr(args,name,Path(value))
    ctx.prec=args.bits;ctx.cap=24
    reference=RetargetReference(args.descriptor)
    report,_=run_leaf(Path(doc['domain']),reference,args,Path(doc['output']))
    return 0 if report.get('complete_continuous_true_density_proved') else 2


if __name__=='__main__':
    raise SystemExit(main())
