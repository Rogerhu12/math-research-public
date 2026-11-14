#!/usr/bin/env python3
"""Copy the actual warm-branch GC source/input closure outside git changes."""
import argparse,hashlib,json,shutil
from pathlib import Path

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
SOURCES=['fd2d-gc-bvp-design-warm.py','fd2d_gc_design_profile.py','fd2d_gc_design_flow.py','fd2d_gc_design_ports.py',
 'fd2d_gc_bvp_newton.py','fd2d_gc_logshape_stable.py','fd2d_gc_logshape.py','fd2d_gc_blended.py','fd2d_gc_intrinsic.py',
 'fd2d_balanced_curvature_core.py','fd2d_metric_curvature_core.py','fd2d_partial_return_parameter.py','fd2d_frozen_ellipse_candidate.py']

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--destination',type=Path,required=True)
    p.add_argument('--candidate',type=Path,required=True);p.add_argument('--warm-field',type=Path,required=True)
    p.add_argument('--linear-tail',type=Path,required=True);a=p.parse_args()
    if a.destination.exists():raise FileExistsError('Use a new stable runtime directory')
    topic=a.destination/'topic';(topic/'scripts').mkdir(parents=True);(topic/'notes').mkdir();(a.destination/'outputs').mkdir()
    inputs=[a.candidate,a.warm_field,a.linear_tail,ROOT/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json',ROOT/'notes/2026-11-12-fd2d-balanced-weighted-means-01.json']
    rows=[]
    for source,target in [(HERE/n,topic/'scripts'/n) for n in SOURCES]+[(s,topic/'notes'/s.name) for s in inputs]:
        data=source.read_bytes();target.write_bytes(data)
        rows.append(dict(original_path=str(source.resolve()),runtime_path=str(target.resolve()),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
    manifest=dict(schema='fd2d-stable-gc-warm-design-runtime-v1',source_inputs_unchanged=True,files=rows,
        candidate=str((topic/'notes'/a.candidate.name).resolve()),warm_field=str((topic/'notes'/a.warm_field.name).resolve()),
        linear_tail=str((topic/'notes'/a.linear_tail.name).resolve()),runner=str((topic/'scripts'/'fd2d-gc-bvp-design-warm.py').resolve()))
    path=a.destination/'source-input-manifest.json';path.write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest,indent=2))

if __name__=='__main__':main()
