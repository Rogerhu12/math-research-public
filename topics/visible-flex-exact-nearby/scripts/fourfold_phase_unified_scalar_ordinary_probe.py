#!/usr/bin/env python3
"""Compare the new unified ordinary samples with the frozen scalar evaluator."""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, acb, ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_scalar_time_circle import SharedBudgetScalarField
from fourfold_phase_unified_scalar_time_circle import (
    UnifiedScalarTimeCircleField, complex_record, write_report,
)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor',type=Path,default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--domain',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json'))
    p.add_argument('--germ',type=int,default=-1)
    p.add_argument('--primitive-nodes',type=int,default=512)
    p.add_argument('--angles',type=int,default=512)
    p.add_argument('--bits',type=int,default=256)
    p.add_argument('--radius',default='5/4')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=21
    start,cpu=time.monotonic(),time.process_time()
    new=UnifiedScalarTimeCircleField(args.descriptor,args.domain,germ=args.germ,nodes=args.primitive_nodes)
    old=SharedBudgetScalarField(args.descriptor,args.domain,germ=args.germ,nodes=args.primitive_nodes)
    if new.turn or new.cell!=old.cell or new.sign!=old.sign:
        raise ValueError('same ordinary analytic germ and branch required')
    if any(v.p or v.q!=q for v,q in zip(new.time_endpoints,old.time_endpoints)):
        raise ValueError('exact time coordinates differ')
    rho=exact_arb(Fraction(args.radius));rows=[]
    for u in (acb(rho),acb(0,rho),rho*acb(0,arb.pi()/4).exp(),acb(-rho),acb(0,-rho)):
        actual,nt=new.sample(u,args.angles);legacy,ot=old.sample(u,args.angles)
        if any(not(a.real.overlaps(b.real)and a.imag.overlaps(b.imag))for a,b in zip(actual,legacy)):
            raise ValueError('unified and frozen scalar samples disagree')
        rows.append(dict(u=complex_record(u),all_angle_intervals_overlap=True,
            maximum_difference=ball_record(max(abs(a-b).upper()for a,b in zip(actual,legacy))),
            unified_timing=nt,frozen_timing=ot))
    report=dict(kind='unified_ordinary_scalar_consistency_with_frozen_true_evaluator',complete=True,
        source_sha256=sha(__file__),dependency_sha256={name:sha(Path(__file__).with_name(name))for name in[
            'fourfold_phase_unified_scalar_time_circle.py','fourfold_phase_scalar_time_circle.py',
            'fourfold_phase_scalar_time_circle_direct.py']},identity=new.identity(),
        angles=args.angles,primitive_nodes=args.primitive_nodes,bits=args.bits,radius=args.radius,
        samples=rows,elapsed_seconds=time.monotonic()-start,cpu_seconds=time.process_time()-cpu,
        limitations=['The two implementations share the invariant formula; this is an implementation consistency check.',
            'Continuous truth follows from the matched domain and directed primitive/time budgets, not finite overlap checks.',
            'No complete actual interval is inferred when the input domain has several required scalar germs.'])
    write_report(args.out,report)
    print(dict(complete=True,elapsed_seconds=report['elapsed_seconds'],cpu_seconds=report['cpu_seconds']),flush=True)


if __name__=='__main__':main()
