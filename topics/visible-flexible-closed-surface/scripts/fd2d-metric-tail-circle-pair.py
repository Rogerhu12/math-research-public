#!/usr/bin/env python3
"""Two-axis Schur spread on the exact M12 tail circle of a saved witness.

The certified background interval is reused only at its identical exact
radius. The source point routine evaluates both angles on the same finite
tail; the reported positive lower bound uses exact rational combinations
of its outward binary endpoints. No ODE or background solve is repeated.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))


def identity(path):
    path=Path(path).resolve()
    return dict(file=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                bytes=path.stat().st_size)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest',type=Path,required=True)
    ap.add_argument('--witness',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic()
    old=json.loads(args.witness.read_text())
    if identity(args.manifest)['sha256']!=old['inputs']['manifest']['sha256']:
        raise ValueError('Witness is about a different finite tail')
    source=HERE/'db6f-root-tail-metric-point.py'
    if identity(source)['sha256']!=old['inputs']['point']['sha256']:
        raise ValueError('The imported point formula differs from the cited witness')
    spec=importlib.util.spec_from_file_location('fd2d_tail_pair_point',source)
    point=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=point
    spec.loader.exec_module(point)
    selected=old['selected_witness']
    geom=point.stream.StreamingExactIntegratedTail(args.manifest)
    idx,local=selected['span'],Q(selected['local_exact'])
    radius=geom.rq[idx]+local*geom.lq[idx]
    if radius!=Q(selected['radius_exact']):
        raise ValueError('The saved background interval is for a different radius')
    w=point.I(*selected['w_interval'])
    rows=[point.point_metric(geom,idx,local,j,w) for j in (0,2)]
    p,q=[row['normalized_component_intervals'][0] for row in rows]
    difference=max(Q(p[0])-Q(q[1]),Q(q[0])-Q(p[1]),Q(0))
    denominator_upper=2+Q(p[1])+Q(q[1])
    if min(1+Q(p[0]),1+Q(q[0]))<=0:
        raise ValueError('The normal radial speeds were not proved positive')
    lower=difference/denominator_upper
    scale=10**24
    integer=lower.numerator*scale//lower.denominator
    out=dict(schema='fd2d-certified-m12-tail-circle-pair-v1',
        script=identity(__file__),manifest=identity(args.manifest),
        input_witness=identity(args.witness),point_formula=identity(source),
        source_identities={name:identity(HERE/name) for name in old['source_sha256']},
        background_definition_hashes=old['background_definition_hashes'],
        exact_radius=str(radius),rows=rows,
        lower_exact=str(lower),safe_decimal_lower_exact=str(Q(integer,scale)),
        safe_decimal_lower=f'{integer//scale}.{integer%scale:024d}',
        lower_display=float(lower),exceeds_2e_minus9=lower>Q(1,500_000_000),
        scope='Any circle-preserving radial and angular material relabeling of this same finite tail; no target change or graph perturbation is implied',
        background_interval_origin='Reused certified interval at exactly the same rational physical radius; verified manifest and radius identity',
        point_formula_scope='At both selected symmetry axes the mixed component vanishes exactly, so normalized radial Gram values equal normal radial speeds squared',
        whole_surface_upper=False,new_solution=False,ODE_calls=0,
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(output=str(args.out),lower=float(lower),
        safe_lower=out['safe_decimal_lower'],axes_Brr=[p,q],
        exceeds_2e_minus9=out['exceeds_2e_minus9'],seconds=out['seconds'])))


if __name__=='__main__':main()
