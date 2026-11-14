#!/usr/bin/env python3
"""Scalar-time circle with a single proved radial majorant for all nodes.

This is a separately versioned improvement of the direct scalar evaluator.
Its only change is to precompute one larger radial-disk input bound.  Exact
geometry, complex E, field values and all numerical ball radii remain native.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
from flint import arb,acb,ctx
from fourfold_phase_scalar_time_circle_direct import (
    ScalarTimeCircleField, circle_coefficients, time_alias_bounds)
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb,complex_pad
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_field_time_refined_root import RefinedGermTimeModel


class SharedBudgetScalarField(ScalarTimeCircleField):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # For every |u|<=R, |t sin(tau0+h u)-t sin(tau0)|<=t(e^(|h|R)-1).
        # The disk of radius R0 about each sample lies in the center disk R0+d;
        # likewise RE+d.  Their gap is exactly the original R0-RE.  The same
        # true primitive/E majorant consequently applies at every scalar node.
        self.radial_enlargement=(abs(self.root)*((abs(self.h)*self.outer).exp()-1)).upper()
        self.budget_center=self.root*self.tau0.sin()
        self.common_budget=self.target.analytic_input_budget(acb(self.budget_center),
            self.R0+self.radial_enlargement,self.sigma,self.RE+self.radial_enlargement)
        def common_budget(radial,radial_radius,sigma,E_radius):
            # Arb's equality asks for provable scalar equality, so two identical
            # non-dyadic balls need not compare equal.  These are the very same
            # immutable radius objects passed to this target constructor.
            if not (radial_radius is self.R0 and sigma is self.sigma and E_radius is self.RE):
                raise ValueError('shared scalar budget requested with different radii')
            return self.common_budget
        self.target.analytic_input_budget=common_budget


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor',type=Path,default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--domain',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json'))
    p.add_argument('--germ',type=int,default=-1)
    p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--primitive-nodes',type=int,default=512)
    p.add_argument('--time-nodes',type=int,default=16)
    p.add_argument('--terms',type=int,default=9)
    p.add_argument('--radius',default='5/4')
    p.add_argument('--bits',type=int,default=256)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=max(21,args.terms+3)
    start,cpu=time.monotonic(),time.process_time()
    model=SharedBudgetScalarField(args.descriptor,args.domain,germ=args.germ,nodes=args.primitive_nodes)
    init_seconds=time.monotonic()-start
    values,timing=circle_coefficients(model,args.angles,args.time_nodes,args.terms,Fraction(args.radius))
    aliases=time_alias_bounds(model,Fraction(args.radius),args.time_nodes,args.terms)
    a,b=model.time_endpoints
    direct=RefinedGermTimeModel(model.object_path,model.root_path,(a+b)/2,(b-a)/2,
        refined_root=model.root_package,cell=model.cell,nodes=args.primitive_nodes,
        order=args.terms-1,outer_radius=Fraction(model.domain['time_radius']),branch_sign=model.sign)
    checks=[]
    for j in sorted({0,args.angles//7,args.angles//3,args.angles-1}):
        expected,_=direct.time_field([acb(arb.pi()*j/(2*args.angles))])
        maximum=arb(0)
        for i in range(args.terms):
            enclosure=complex_pad(values[j,0][i],aliases[i])
            if not (enclosure.real.overlaps(expected[0][i].real) and enclosure.imag.overlaps(expected[0][i].imag)):
                raise ValueError('cached scalar-time coefficients disagree with independent actual time jets')
            maximum=max(maximum,abs(values[j,0][i]-expected[0][i]).upper())
        checks.append(dict(angle_node=j,all_coefficients_overlap_after_true_time_alias=True,
                           maximum_unpadded_difference=ball_record(maximum)))
    report=dict(kind='actual_scalar_time_circle_with_shared_radial_majorant',complete=True,
        source_sha256=sha(__file__),dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
          ['fourfold_phase_scalar_time_circle_direct.py','fourfold_native_series_fft.py',
           'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_interval.py']},
        domain_sha256=sha(args.domain),descriptor_sha256=sha(args.descriptor),
        target_object_sha256=sha(model.object_path),target_root_sha256=sha(model.root_path),
        common_span=list(map(str,model.cell)),exact_time_endpoints=list(map(str,model.time_endpoints)),
        angles=args.angles,primitive_nodes=args.primitive_nodes,time_nodes=args.time_nodes,
        retained_time_terms=args.terms,time_circle_radius=args.radius,bits=args.bits,
        actual_time_outer_radius=model.domain['time_radius'],actual_physical_outer_strip=model.domain['physical_theta_strip'],
        actual_outer_modulus=ball_record(model.modulus),radial_enlargement=ball_record(model.radial_enlargement),
        common_E_infinite_error=ball_record(model.common_budget['E_error']),
        refined_root=model.root_package.provenance,init_seconds=init_seconds,**timing,
        true_coefficient_time_alias=[ball_record(v) for v in aliases],independent_checks=checks,
        total_run_seconds=time.monotonic()-start,total_cpu_seconds=time.process_time()-cpu,
        finite_polynomial_saved=False,
        limitations=['Retained time coefficients on the finite physical grid only; no full reference residual.',
                     'A separately stored finite P and full angular alias/time budget remain required.'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(complete=True,total_run_seconds=report['total_run_seconds'],
                         total_cpu_seconds=report['total_cpu_seconds'],sample_seconds=timing['total_seconds'])),flush=True)


if __name__=='__main__':
    main()
