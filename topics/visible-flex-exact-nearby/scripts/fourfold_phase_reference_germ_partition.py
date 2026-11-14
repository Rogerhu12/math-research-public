#!/usr/bin/env python3
"""Certify an exact finite time partition and every required scalar germ.

This only locates the actual radial trajectory in common spline spans.  It
does not estimate a field or a residual.  Restricting one fixed finite
reference (and any one fixed finite correction polynomial) to these pieces
creates no jump: the values on a shared rational endpoint are identical.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import time

from flint import ctx

from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_affine import AffineBulkTarget, sha
from fourfold_phase_field_time_germ_union import (
    radial_cover, continuity_gate, reflected_common_domain,
)
from fourfold_phase_field_time_refined_root import prepare_refined_root
from fourfold_phase_reference_time_sample import load_segment


def partition(manifest_path, object_path, root_path, segment, cuts, *, nodes=512):
    manifest, shard, shard_path, _, _, a, b = load_segment(manifest_path, segment)
    identity = manifest['trace_identity']
    if (identity['angular_scale'] != 4 or identity['sign'] not in (-1, 1)
            or identity['source_sha256'] != sha(object_path)
            or identity['root_certificate_sha256'] != sha(root_path)):
        raise ValueError('reference, exact affine graph and certified root are different inputs')
    cuts = [Fraction(value) for value in cuts]
    if not cuts or cuts[0] != 0 or cuts[-1] != 1 or any(x >= y for x, y in zip(cuts,cuts[1:])):
        raise ValueError('strictly increasing rational cuts must partition [0,1]')
    package = prepare_refined_root(object_path, root_path, nodes=nodes)
    target = AffineBulkTarget(object_path, nodes, nodes,
        exact_arb(Fraction(3,1000)),exact_arb(Fraction(1,400)),exact_arb(Fraction(8,25)))
    continuity = continuity_gate(target)
    allradial, allcover, allcells, allcrossed = radial_cover(target,package.root,(a+b)/2,(b-a)/2)
    pieces = []
    for index,(left,right) in enumerate(zip(cuts,cuts[1:])):
        ta,tb = a+(b-a)*left,a+(b-a)*right
        radial,cover,cells,crossed = radial_cover(target,package.root,(ta+tb)/2,(tb-ta)/2)
        pieces.append(dict(index=index,normalized_subspan=list(map(str,(left,right))),
            exact_time_endpoints=list(map(str,(ta,tb))),true_radial_range=ball_record(radial),
            exact_outward_radial_enclosure=list(map(str,cover)),
            required_common_spans=[list(map(str,cell)) for cell in cells],
            guaranteed_crossed_knots=list(map(str,crossed)),single_germ=len(cells)==1))
    return dict(kind='exact_reference_time_partition_with_complete_scalar_germ_cover',proved=True,
        source_sha256=sha(__file__),object_sha256=sha(object_path),root_certificate_sha256=sha(root_path),
        exact_delta_fraction=str(target.affine_delta),reference_manifest=str(manifest_path),
        reference_manifest_sha256=sha(manifest_path),reference_shard_sha256=sha(shard_path),
        segment=segment,exact_original_time_endpoints=list(map(str,(a,b))),cuts=list(map(str,cuts)),
        root_refinement=package.provenance,scalar_continuity=continuity,
        exact_reflected_common_domain=list(map(str,reflected_common_domain(target))),
        whole_true_radial_range=ball_record(allradial),whole_exact_radial_enclosure=list(map(str,allcover)),
        whole_required_common_spans=[list(map(str,cell)) for cell in allcells],
        whole_guaranteed_crossed_knots=list(map(str,allcrossed)),pieces=pieces,
        bits=ctx.prec,nodes=nodes,
        dependency_sha256={name:sha(Path(__file__).parent/name) for name in
            ('fourfold_phase_beta_affine.py','fourfold_phase_field_time_germ_union.py',
             'fourfold_phase_field_time_refined_root.py','fourfold_phase_reference_time_sample.py')},
        limitations=['This certifies radial/germ coverage only, not any field or residual bound',
            'No separately corrected references may be joined without paying their actual jump',
            'Zero new jump applies only when restricting the identical finite reference/correction'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,required=True)
    parser.add_argument('--object',type=Path,required=True)
    parser.add_argument('--root-certificate',type=Path,required=True)
    parser.add_argument('--segment',type=int,default=419)
    parser.add_argument('--cuts',default='0,1/1024,1')
    parser.add_argument('--quarter-nodes',type=int,default=512)
    parser.add_argument('--bits',type=int,default=160)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();ctx.prec=args.bits;ctx.cap=24;started=time.monotonic()
    report=partition(args.manifest,args.object,args.root_certificate,args.segment,
        [Fraction(value) for value in args.cuts.split(',')],nodes=args.quarter_nodes)
    report['elapsed_seconds']=time.monotonic()-started
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(proved=report['proved'],pieces=[dict(normalized=p['normalized_subspan'],
        required_germs=len(p['required_common_spans'])) for p in report['pieces']],
        elapsed_seconds=report['elapsed_seconds']),indent=2),flush=True)


if __name__=='__main__':main()
