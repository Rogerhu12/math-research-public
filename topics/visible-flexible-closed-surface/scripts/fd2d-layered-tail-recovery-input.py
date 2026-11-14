#!/usr/bin/env python3
"""Rebuild a separately named layered-cap input after the executor change."""
import argparse,copy,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('base',type=Path);p.add_argument('out',type=Path)
p.add_argument('--wcut',type=float,choices=[.1,.3],default=.1);args=p.parse_args()
if args.out.exists():raise RuntimeError('unused output required')
cfg=json.loads(args.base.read_text());cfg.update(rCut=.5,width=.18,wCut=args.wcut,prefixR=64,
 pulseCaps=[[.3*2**(-1.75*n),(.3/64)*2**(-1.75*n)] for n in range(160)],
 valleyCaps=[(.3/64)*2**(-1.75*n) for n in range(160)],valleyControls=[0.]*160,warpWeightLevels=[],
 design_label='uniform R64; layered finite 64:1 pulse caps; new physical g',
 pulse_cap_formula=dict(first_coefficient=.3,first_decay_power=1.75,first_to_second_ratio=64,
 valley_cap='second pulse cap',finite_cells=160),calibration_status='unrecalibrated recovered input')
cfg['recovery_provenance']=dict(base_file=args.base.name,base_sha256=hashlib.sha256(args.base.read_bytes()).hexdigest(),
 generator=Path(__file__).name,generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 reason='Old unpushed files were lost on executor change. This new input will actually be recalibrated; no lost beta is filled from remembered output.')
args.out.write_text(json.dumps(cfg,indent=2)+'\n');print(hashlib.sha256(args.out.read_bytes()).hexdigest())
