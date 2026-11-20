#!/usr/bin/env python3
"""Reuse paid high kernels with the refined constant-strip low residual.

No kernel or source equation is changed.  The original successful causal
package remains the immutable kernel source; only its residual upper
vector is replaced by the sharper saved constant-strip calculation.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import hashlib
from pathlib import Path
import types


def main():
    path=Path(__file__).with_name("tail_r33_high_joint_box.py")
    source=path.read_text()
    changes=[
        ('    args=p.parse_args();ctx.prec=192;started=time.monotonic()',
         '    p.add_argument("--wide-hybrid",type=Path,required=True)\n'
         '    args=p.parse_args();ctx.prec=192;started=time.monotonic()'),
        ('    rows={r["cell"]:r for r in middle["cells"]}',
         '    rows={r["cell"]:dict(r) for r in middle["cells"]}\n'
         '    wide,wraw=load_json(args.wide_hybrid)\n'
         '    if dhash not in wide["input_hashes"].values():raise ValueError("Wide residual uses another envelope")\n'
         '    if not wide.get("wide_low_adapter_sha256"):raise ValueError("Need the proved constant-strip residual")\n'
         '    lower_source={n:arb(0) for n in cells}\n'
         '    for band in wide["bands"]:\n'
         '        for row in band["low_source_residual"]["rows"]:\n'
         '            n=row["cell"];lower_source[n]=(lower_source[n]+2*ball(row["combined_bound"])).upper()\n'
         '    for n in cells:\n'
         '        b=(lower_source[n]+ball(rows[n]["far_boundary"])).upper()\n'
         '        rows[n]["low_plus_far_residual"]=ball_record(b)'),
        ('        r=dict(cell=n)',
         '        r=dict(cell=n,refined_low_residual=ball_record(lower_source[n]),\n'
         '            refined_residual_plus_far=rows[n]["low_plus_far_residual"])'),
        ('        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),',
         '        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),\n'
         '        residual_input_hash={str(args.wide_hybrid):hashlib.sha256(wraw).hexdigest()},\n'
         '        refined_adapter_sha256=_adapter_hash,')]
    for before,after in changes:
        if source.count(before)!=1:raise ValueError("Joint-box source anchor changed")
        source=source.replace(before,after)
    module=types.ModuleType("tail_refined_high_joint")
    module.__file__=str(path);module.__dict__["_adapter_hash"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    exec(compile(source,str(path),"exec"),module.__dict__);module.main()


if __name__=="__main__":main()
