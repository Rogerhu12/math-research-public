#!/usr/bin/env python3
"""Export each true middle-band envelope inside a paid joint high box.

The immutable causal-kernel code is reused.  Every band keeps its own
operator response to the full high-source bound, fixed wide-low source,
and true far trace, then intersects the result with the paid total radius.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import hashlib
from pathlib import Path
import types


def main():
    path=Path(__file__).with_name("tail_r33_middle_causal_box.py")
    source=path.read_text()
    changes=[
        ('    args=p.parse_args();ctx.prec=192;started=time.monotonic()',
         '    p.add_argument("--joint",type=Path,required=True)\n'
         '    args=p.parse_args();ctx.prec=192;started=time.monotonic()'),
        ('    gamma={(n,j):arb(0) for n in range(12,225) for j in range(n,225)}',
         '    joint,jraw=load_json(args.joint)\n'
         '    if not all(joint["gates"].values()):raise ValueError("The joint high box must be paid")\n'
         '    if densityhash not in joint["input_hashes"].values():raise ValueError("Different joint envelope")\n'
         '    if joint["z_log2"]!=args.z_log2:raise ValueError("Far parameter ball differs")\n'
         '    jointrows={r["cell"]:r for r in joint["rows"]}\n'
         '    h=ball(joint["infinite_radius"])\n'
         '    forces={n:(64*(ball(jointrows[n]["middle_radius"])+h)*(1+ball(jointrows[n]["middle_radius"])+h)).upper() for n in range(12,225)}\n'
         '    band_results=[]\n'
         '    gamma={(n,j):arb(0) for n in range(12,225) for j in range(n,225)}'),
        ('    for bi,b in enumerate(bands):\n        for j in range(224,11,-1):',
         '    for bi,b in enumerate(bands):\n'
         '        band_nonlinear={n:arb(0) for n in range(12,225)}\n'
         '        band_far={n:arb(0) for n in range(12,225)}\n'
         '        for j in range(224,11,-1):'),
        ('            peak=2*c["peak"]',
         '            peak=2*c["peak"]\n'
         '            band_nonlinear[j]=(band_nonlinear[j]+peak*forces[j]).upper()'),
        ('                if 2*peak>gamma[n,j]:gamma[n,j]=(2*peak).upper();argmax[n,j]=bi',
         '                band_nonlinear[n]=(band_nonlinear[n]+2*peak*forces[j]).upper()\n'
         '                if 2*peak>gamma[n,j]:gamma[n,j]=(2*peak).upper();argmax[n,j]=bi'),
        ('            far[n]=(far[n]+2*peak).upper()',
         '            far[n]=(far[n]+2*peak).upper()\n'
         '            band_far[n]=(2*peak).upper()'),
        ('        print(json.dumps(dict(event="band",first=lo,last=b["last_mode"],',
         '        lowrows={r["cell"]:r for r in hybrid["bands"][bi]["low_source_residual"]["rows"]}\n'
         '        outrows=[]\n'
         '        for n in range(12,225):\n'
         '            low=(2*ball(lowrows[n]["combined_bound"])).upper()\n'
         '            uncut=(low+band_far[n]+band_nonlinear[n]).upper()\n'
         '            bound=min(uncut,ball(jointrows[n]["middle_radius"]))\n'
         '            outrows.append(dict(cell=n,norm_bound=ball_record(bound),log2_norm_bound=ball_record(bound.log()/ln2),\n'
         '                low_source=ball_record(low),high_source=ball_record(band_nonlinear[n]),far_boundary=ball_record(band_far[n]),unclipped_bound=ball_record(uncut)))\n'
         '        band_results.append(dict(first_mode=lo,last_mode=b["last_mode"],rows=outrows))\n'
         '        print(json.dumps(dict(event="band",first=lo,last=b["last_mode"],\n'
         '            cell12_log2=outrows[0]["log2_norm_bound"]["display"],'),
        ('    residual={n:far[n] for n in far}',
         '    result=dict(status="Band-resolved rigorous response enclosures within a successful joint high box; low feedback remains open",\n'
         '        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",bands=band_results,\n'
         '        norm="For each cell, sum over all signed modes in the band of (1+abs(m)) times the separate radial suprema of exp(tau(r)*abs(m))*abs(B*p_m)/V and exp(tau(r)*abs(m))*abs(kappa_m)/V.",\n'
         '        infinite_radius=joint["infinite_radius"],z_log2=args.z_log2,\n'
         '        input_hashes={**hashes,str(args.joint):hashlib.sha256(jraw).hexdigest()},\n'
         '        base_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),adapter_sha256=_adapter_hash,\n'
         '        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)\n'
         '    encoded=gzip.compress((json.dumps(result,separators=(",",":"))+"\\n").encode(),mtime=0)\n'
         '    if args.out.suffix!=".gz" or len(encoded)>=5_000_000:raise ValueError("Use gzip below5MB")\n'
         '    args.out.write_bytes(encoded)\n'
         '    print(json.dumps(dict(output=str(args.out),bytes=len(encoded),seconds=result["elapsed_seconds"],RSS_KiB=result["peak_RSS_KiB"])),flush=True)\n'
         '    return\n'
         '    residual={n:far[n] for n in far}')]
    for before,after in changes:
        if source.count(before)!=1:raise ValueError("Causal-kernel source anchor changed")
        source=source.replace(before,after)
    module=types.ModuleType("tail_high_band_envelopes")
    module.__file__=str(path);module.__dict__["_adapter_hash"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    exec(compile(source,str(path),"exec"),module.__dict__);module.main()


if __name__=="__main__":main()
