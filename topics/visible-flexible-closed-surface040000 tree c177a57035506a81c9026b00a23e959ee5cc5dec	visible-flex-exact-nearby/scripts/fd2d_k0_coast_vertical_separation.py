#!/usr/bin/env python3
"""Extract an exact vertical-separation corollary from closed dyadic boxes."""
from pathlib import Path
from fractions import Fraction
import argparse,hashlib,json,time


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dyadic(value):
    m,e=value
    return Fraction(int(m))*Fraction(2)**int(e)


def ratio(q):return [str(q.numerator),str(q.denominator)]


def main():
    root=Path(__file__).resolve().parent.parent
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--certificate',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-position-certificate-01.json')
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    started=time.monotonic();data=json.loads(args.certificate.read_text())
    assert data['passed'] and not data['unresolved']
    assert not data['metric_or_Codazzi_compatibility_assumed']
    boxes=sorted(data['boxes'],key=lambda row:Fraction(*row['left_over_2pi']))
    next_edge=Fraction(0)
    for box in boxes:
        left=Fraction(*box['left_over_2pi']);right=Fraction(*box['right_over_2pi'])
        assert left==next_edge and right>left
        next_edge=right
    assert next_edge==1 and len(boxes)==data['accepted_boxes']
    rows=[(dyadic(box[key]['lower_binary']),j,key) for j,box in enumerate(boxes) for key in ('z_start','z_end')]
    minimum,j,key=min(rows)
    threshold=Fraction(14,25);rho=Fraction(17,125)
    assert minimum>threshold and threshold>2*rho
    out=dict(schema='fd2d-ruled-coast-exact-vertical-separation-v1',actual_execution=True,
        source_sha256=digest(__file__),certificate_sha256=digest(args.certificate),
        inlet_sha256=data['inlet_sha256'],boxes=len(boxes),complete_angular_partition_verified=True,
        radial_affinity_used=True,minimum_saved_z_lower_exact=ratio(minimum),
        minimum_box_sorted_index=j,minimum_endpoint=key,
        strict_coast_z_lower=ratio(threshold),rho=ratio(rho),
        upper_to_reflected_coast_distance_strict_lower=ratio(2*threshold),
        upper_to_any_z_nonpositive_set_distance_strict_lower=ratio(threshold),
        reflected_coast_normal_ball_distance_margin_strict=ratio(2*threshold-2*rho),
        nonpositive_set_normal_ball_distance_margin_strict=ratio(threshold-2*rho),
        assertion_scope='Actual finite ruled coast defined in input certificate. Any normal directions are allowed in this separation corollary. Other upper-core parts and same-coast pairs are not certified.',
        full_reach_certificate=False,rounding_used_in_assertions=False,seconds=time.monotonic()-started)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.output),sha256=digest(args.output),strict_z_lower='14/25',strict_reflection_gap='28/25',seconds=out['seconds'])))


if __name__=='__main__':main()
