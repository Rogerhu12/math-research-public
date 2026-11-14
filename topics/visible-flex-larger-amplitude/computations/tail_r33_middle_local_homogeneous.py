#!/usr/bin/env python3
"""Add homogeneous physical column bounds to the frozen local source tool.

The already saved source computation is left arithmetically unchanged.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import hashlib
from pathlib import Path
import types


def main():
    path=Path(__file__).with_name("tail_r33_middle_local_scalar.py")
    source=path.read_text()
    changes=[
        ('        states=[arb(0) for unused in bands];maximum=[arb(0) for unused in bands]',
         '        states=[arb(0) for unused in bands];maximum=[arb(0) for unused in bands]\n'
         '        homogeneous=[arb(1) for unused in bands];hom_max=[arb(0) for unused in bands]'),
        ('                    within=((growth*states[i]+emitted)/vmin).upper()',
         '                    hom_within=(growth*homogeneous[i]/vmin).upper()\n'
         '                    if hom_within>hom_max[i]:hom_max[i]=hom_within\n'
         '                    homogeneous[i]=(propagator*homogeneous[i]).upper()\n'
         '                    within=((growth*states[i]+emitted)/vmin).upper()'),
        ('                physical_norm_end=ball_record(states[i]),',
         '                physical_norm_end=ball_record(states[i]),\n'
         '                homogeneous_physical_end=ball_record(homogeneous[i]),\n'
         '                homogeneous_peak_over_V=ball_record(hom_max[i]),'),
        ('        input_hashes=hashes,',
         '        input_hashes=hashes, homogeneous_adapter_sha256=_homogeneous_adapter_sha256,'),
        ('status="Validated local ordered scalar source kernels; no incoming-state or full middle-window closure is asserted"',
         'status="Validated local ordered scalar source and homogeneous physical kernels; no full middle-window closure is asserted"')]
    for a,b in changes:
        if source.count(a)!=1:raise ValueError("Local scalar source anchor changed")
        source=source.replace(a,b)
    module=types.ModuleType("tail_ordered_homogeneous")
    module.__file__=str(path)
    module.__dict__["_homogeneous_adapter_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    exec(compile(source,str(path),"exec"),module.__dict__)
    module.main()


if __name__=="__main__":
    main()
