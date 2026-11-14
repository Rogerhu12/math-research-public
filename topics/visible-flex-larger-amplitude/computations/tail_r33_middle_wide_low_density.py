#!/usr/bin/env python3
"""Refine only the constant-strip low-source endpoint contribution.

An arbitrary variable-strip source does not get a whole-cell strip drop.
The fixed low field is analytic on the cell's constant reference strip;
its raw canonical source integral therefore gets the actual endpoint
factor exp(-m*(tau_reference-tau_outer)).  The local physical alternative
remains available, with its original weaker source factor.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import hashlib
from pathlib import Path
import types


def main():
    path=Path(__file__).with_name("tail_r33_middle_hybrid_density.py")
    source=path.read_text()
    changes=[
        ('    args=p.parse_args();ctx.prec=192;started=time.monotonic()',
         '    p.add_argument("--extra-positive",type=Path,required=True)\n'
         '    args=p.parse_args();ctx.prec=192;started=time.monotonic()'),
        ('    for name in ("density", "positive", "subhead", "local", "ready"):',
         '    for name in ("density", "positive", "subhead", "local", "ready", "extra_positive"):'),
        ('    for d in (density,positive,subhead,local):',
         '    for d in (density,positive,subhead,local,docs["extra_positive"]):'),
        ('    ss={r["cell"]:r for r in subhead["cell_rows"]}',
         '    ss={r["cell"]:r for r in subhead["cell_rows"]}\n'
         '    extra=docs["extra_positive"]\n'
         '    if extra["bands"]!=subhead["bands"]:raise ValueError("Extra bands differ")\n'
         '    for row in extra["cell_rows"]:\n'
         '        if row["cell"] in ss:raise ValueError("Overlapping extra matrix")\n'
         '        ss[row["cell"]]=row'),
        ('    if sorted(ss)!=list(range(24,225)) or sorted(ll)!=list(range(12,24)):',
         '    if sorted(ss)!=list(range(16,225)) or sorted(ll)!=list(range(12,24)):'),
        ('                elif n>=24:', '                elif n>=16:'),
        ('                    own=[(A[i][1]*source_integrals[n]/nulo).upper() for i in range(2)]',
         '                    own=[(A[i][1]*source_integrals[n]/nulo).upper() for i in range(2)]\n'
         '                    constant_strip_canonical_source=list(own)'),
        ('                out=[(hom_end[i]+fac*own[i]).upper() for i in range(2)]',
         '                out=[(hom_end[i]+fac*own[i]).upper() for i in range(2)]\n'
         '                if kind=="low_source_residual" and A is not None:\n'
         '                    out=[min(out[i],(hom_end[i]+fac*decay*constant_strip_canonical_source[i]).upper()) for i in range(2)]'),
        ('        input_hashes=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),',
         '        input_hashes=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),\n'
         '        wide_low_adapter_sha256=_adapter_hash,\n'
         '        wide_low_endpoint_proof="The raw source uses its own constant reference strip; only its canonical endpoint term gets exp(-lo*(reference_tau-tau_outer)). Arbitrary variable-strip sources are unchanged.",'),
        ('high-subhead positive matrices are used only on cells24..224, physical local kernels only on cells12..23.',
         'high-subhead positive matrices are used on cells16..224, physical local kernels only on cells12..23.')]
    for before,after in changes:
        if source.count(before)!=1:raise ValueError("Hybrid source anchor changed")
        source=source.replace(before,after)
    module=types.ModuleType("tail_middle_wide_low")
    module.__file__=str(path)
    module.__dict__["_adapter_hash"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    exec(compile(source,str(path),"exec"),module.__dict__)
    module.main()


if __name__=="__main__":main()
