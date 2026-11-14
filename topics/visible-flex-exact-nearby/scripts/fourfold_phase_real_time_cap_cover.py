#!/usr/bin/env python3
"""Join actual domain leaves with completed same-reference real-time gates."""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_germ_cap_budget import leaf_budget
from fourfold_phase_unified_scalar_time_circle import UnifiedScalarTimeCircleField
from fourfold_retarget_reference_jets import RetargetReference
from fourfold_complete_reference_segment import CompleteReferenceSegment
from fourfold_phase_real_time_cap_budget import real_time_reference_cap,upper


def document(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw)if path.suffix=='.gz'else raw)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--domain-index',type=Path,required=True)
    p.add_argument('--reference-index',type=Path,required=True)
    p.add_argument('--descriptor',type=Path,default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--label-strip',default='1/256');p.add_argument('--primitive-nodes',type=int,default=512)
    p.add_argument('--bits',type=int,default=192);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=21
    domains,refs=document(args.domain_index),document(args.reference_index)
    if domains['retarget_descriptor_sha256']!=sha(args.descriptor)or refs['descriptor_sha256']!=sha(args.descriptor):
        raise ValueError('two actual covers belong to different references')
    ref=RetargetReference(args.descriptor);S=Fraction(args.label_strip)
    completed={case['segment']:case for case in refs['cases']}
    root=arb(domains['refined_root']['refined_root']['ball']);rows=[];covered=[];total=arb(0)
    for case in domains['cases']:
        if case['leg']!=refs['leg']or case['segment']not in completed:continue
        if not case['proved']:raise ValueError('unproved actual domain case')
        rc=completed[case['segment']];path=Path(rc['path'])
        if sha(path)!=rc['sha256']or path.stat().st_size!=rc['bytes']:
            raise ValueError('completed real-time gate leaf changed')
        gates=document(path)
        if not gates['complete']or gates['descriptor_sha256']!=sha(args.descriptor):
            raise ValueError('completed real-time gate identity differs')
        if gates['dependency_sha256']!=refs['dependency_sha256']:
            raise ValueError('reference gate proof dependencies differ from its cover')
        for leaf in case['leaves']:
            if sha(leaf['path'])!=leaf['sha256']:raise ValueError('actual domain leaf changed')
            doc=document(leaf['path']);raw=leaf_budget(doc,root)
            field=UnifiedScalarTimeCircleField(args.descriptor,leaf['path'],
                germ=raw['main_germ_index'],nodes=args.primitive_nodes)
            l,r=map(Fraction,leaf['normalized_subspan'])
            reference=CompleteReferenceSegment(ref,case['leg'],case['segment'],l,r)
            images=[g for g in gates['image_gates']if Fraction(g['initial_label_strip'])==S]
            qs=[g for g in gates['q_gates']if Fraction(g['initial_label_strip'])==S]
            if len(images)!=1 or len(qs)!=1:raise ValueError('same requested label strip not uniquely present')
            paid=real_time_reference_cap(field,reference,images[0],qs[0])
            paid.update(reference_gate_leaf_path=str(path),reference_gate_leaf_sha256=sha(path))
            rows.append(paid);total=(total+upper(paid['integrated_density_cap_error_upper'])).upper()
        covered.append(case['segment'])
        if case['segment']%16==0:print(json.dumps(dict(covered=len(covered),segment=case['segment'],cap_E=ball_record(total))),flush=True)
    out=dict(kind='actual_small_field_cap_budget_on_two_completed_cover_intersection',complete=True,
        source_sha256=sha(__file__),dependency_sha256={name:sha(Path(__file__).with_name(name))for name in[
            'fourfold_phase_real_time_cap_budget.py','fourfold_phase_unified_scalar_time_circle.py',
            'fourfold_complete_reference_segment.py']},
        domain_cover_path=str(args.domain_index),domain_cover_sha256=sha(args.domain_index),
        reference_cover_path=str(args.reference_index),reference_cover_sha256=sha(args.reference_index),
        descriptor_sha256=sha(args.descriptor),initial_label_strip=str(S),bits=args.bits,
        covered_segments=covered,covered_leaves=len(rows),ordinary_crossing_pairs=sum(len(r['pairs'])for r in rows),
        integrated_actual_density_cap_error_upper=ball_record(total),rows=rows,
        complete_reference_leg=False,
        limitations=['Exactly the listed intersection of two completed partial covers, not the whole leg.',
            'Actual cap error only; main-germ finite-field/density and true-flow errors remain separate.',
            'No parameter derivative of a moving cap is inferred.'])
    raw=(json.dumps(out,indent=2)+'\n').encode()
    if len(raw)>1_000_000 and args.out.suffix!='.gz':raise ValueError('gzip required above 1MB')
    raw=gzip.compress(raw,mtime=0)if args.out.suffix=='.gz'else raw
    if len(raw)>5_000_000:raise ValueError('split this actual cap report')
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_bytes(raw)
    print(json.dumps(dict(complete=True,covered=len(covered),pairs=out['ordinary_crossing_pairs'],
        cap_E=ball_record(total),sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()
