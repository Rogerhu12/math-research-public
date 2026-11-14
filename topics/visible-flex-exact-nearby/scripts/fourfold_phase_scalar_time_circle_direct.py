#!/usr/bin/env python3
"""True scalar field samples on a complex time circle, with analytic aliases.

The radial geometry is evaluated directly at each complex time node.  No real
projection of the mean metric is made at complex radial arguments.  The true
whole-angle/time domain is a separately verified, identity-matched input.
This entry constructs retained coefficients; its cost report alone is not a
reference residual or an actual return-map certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from flint import arb, acb, acb_series, ctx

from fourfold_phase_beta_affine import AffineBulkTarget, sha
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_beta_interval import primitive_fourier_budget, ball_record
from fourfold_phase_field_time_refined_root import prepare_refined_root, RefinedGermTimeModel
from fourfold_phase_uniform_field_time_grid_fast import f_invariants
from fourfold_native_series_fft import NativeSeriesFFT
from fourfold_boundary_fourier_budget import full_fourier_factor


def upper_record(record):
    return arb(record['upper']).upper()


class ScalarTimeCircleField:
    def __init__(self, descriptor_path, domain_path, *, germ=-1, nodes=1024):
        self.descriptor_path, self.domain_path = Path(descriptor_path), Path(domain_path)
        descriptor = json.loads(self.descriptor_path.read_text())
        domain = json.loads(self.domain_path.read_text())
        if not (descriptor.get('complete') and domain.get('complete')
                and domain.get('proved_full_physical_angle_and_complex_time_domain')
                and domain.get('complete_common_span_coverage')):
            raise ValueError('actual complete whole-angle complex-time domain is required')
        if domain['retarget_descriptor_sha256'] != sha(self.descriptor_path):
            raise ValueError('retarget descriptor and domain differ')
        self.object_path, self.root_path = [Path(descriptor[k]['path']) for k in ('target_object', 'target_root')]
        for key, path, hash_key in [('target_object',self.object_path,'target_object_sha256'),
                                    ('target_root',self.root_path,'target_root_sha256')]:
            if sha(path) != descriptor[key]['sha256'] or sha(path) != domain[hash_key]:
                raise ValueError('domain and actual object/root identity differ')
        if domain['exact_delta_fraction'] != descriptor['target_exact_delta_fraction']:
            raise ValueError('exact affine parameter differs')
        self.selected = domain['germs'][germ]
        if not self.selected['passed']:
            raise ValueError('selected actual germ has not passed the domain proof')
        self.cell = tuple(map(Fraction, self.selected['common_span']))
        self.time_endpoints = tuple(map(Fraction, domain['exact_time_endpoints']))
        a,b = self.time_endpoints
        self.tau0, self.h = map(exact_arb, ((a+b)/2,(b-a)/2))
        self.outer = exact_arb(Fraction(domain['time_radius']))
        self.strip = exact_arb(Fraction(domain['physical_theta_strip']))
        self.modulus = upper_record(self.selected['true_field_moduli']['f'])
        self.nodes = int(nodes)
        self.R0, self.RE, self.sigma = map(exact_arb, (Fraction(3,1000),Fraction(1,400),Fraction(8,25)))
        identity = json.loads(Path(descriptor['old_'+domain['leg']+'_reference']['path']).read_text())['trace_identity']
        self.sign = int(identity['sign'])
        self.root_package = prepare_refined_root(self.object_path,self.root_path,nodes=nodes)
        self.root = self.root_package.root
        self.target = AffineBulkTarget(self.object_path,nodes,nodes,self.R0,self.RE,self.sigma)
        self.target.set_cell(*self.cell)
        self.target.fourier = NativeSeriesFFT()
        self.domain = domain

    def sample(self, u, angles):
        """Enclose true f(u,theta_j), with physical theta_j=pi*j/(2N)."""
        if abs(u).upper() >= self.outer:
            raise ValueError('sample leaves the proved complex time disk')
        angles = int(angles)
        if angles < self.nodes or angles & (angles-1):
            raise ValueError('a power-of-two angle grid at least Q long is required')
        oldcap, ctx.cap = ctx.cap, 4
        before = time.monotonic()
        try:
            tau = acb(self.tau0)+self.h*u
            radial = self.root*tau.sin()
            r_tau = self.root*tau.cos()
            coefficient, K, _, budget = self.target.complete_data(radial)
            # complete_data retains complex E and its true infinite correction.
            # Calling target.target here would incorrectly project E to real.
            if not (-K).real > 0:
                raise ValueError('right-half-plane square-root branch not separated')
            kappa = (-K).sqrt(analytic=True)
            beta,gamma,_,_ = self.target.scalars(radial,1)
            geometry_seconds = time.monotonic()-before
            before = time.monotonic()
            frequency_data = np.empty((angles,9),object)
            frequency_data.fill(acb(0))
            for k, frequency in enumerate(self.target.frequency):
                if frequency % 4:
                    raise ValueError('unexpected physical frequency')
                for c in range(3):
                    frequency_data[(frequency//4)%angles,c] = coefficient[k,c][1]
            for k, (b,g) in enumerate(zip(beta,gamma),1):
                if k >= angles//2:
                    raise ValueError('phase modes exceed grid capacity')
                for sign in (-1,1):
                    factor = acb(0,-sign)/2
                    row = (sign*k)%angles
                    frequency_data[row,3:7] = [b[0]*factor,g[0]*factor,b[1]*factor,g[1]*factor]
                    frequency_data[row,7] = b[0]*factor*acb(0,4*sign*k)
                    frequency_data[row,8] = g[0]*factor*acb(0,4*sign*k)
            samples = self.target.fourier.fft(frequency_data,inverse=True)*angles
            errors,_ = primitive_fourier_budget(self.nodes,self.sigma,arb(0),self.R0,
                budget['radius_bound'],budget['height_bound'],budget['tangent_bound'])
            Xerror = (errors[0]/self.R0).upper()
            result=[]; Dlower=None; maximum_radius=arb(0)
            for j in range(angles):
                X=[complex_pad(samples[j,c],Xerror) for c in range(3)]
                D,M,W=f_invariants(X,samples[j,3:])
                lower=D.abs_lower()
                if not lower > 0:
                    raise ValueError('sample denominator enclosure contains zero')
                Dlower=lower if Dlower is None else min(Dlower,lower)
                value=-r_tau*(M+self.sign*kappa*W)/D
                if not value.is_finite():
                    raise ValueError('nonfinite actual field sample')
                result.append(value)
                maximum_radius=max(maximum_radius,value.real.rad().upper(),value.imag.rad().upper())
            return result,dict(geometry_seconds=geometry_seconds,grid_seconds=time.monotonic()-before,
                sample_D_lower=ball_record(Dlower),primitive_derivative_fee=ball_record(Xerror),
                maximum_component_radius=ball_record(maximum_radius))
        finally:
            ctx.cap=oldcap


def time_alias_bounds(model, radius, time_nodes, terms):
    rho=exact_arb(radius)
    if not 0 < rho < model.outer or not 0 < terms <= time_nodes:
        raise ValueError('invalid time circle or retained degree')
    ratio=(rho/model.outer)**time_nodes
    tail_factor=ratio/(1-ratio)
    return [(model.modulus/model.outer**i*tail_factor).upper() for i in range(terms)]


def circle_coefficients(model, angles, time_nodes, terms, radius=Fraction(5,4)):
    if time_nodes < 2 or time_nodes%2 or not 0 < terms <= time_nodes:
        raise ValueError('even positive time-node count and valid retained terms required')
    rho=exact_arb(radius)
    values=np.empty((time_nodes,angles),object)
    timings=[];start=time.monotonic()
    # For real physical theta, real-coefficient germs and the certified right
    # half-plane sqrt branch give exact Schwarz conjugation in complex time.
    for j in range(time_nodes//2+1):
        u=acb(rho) if j==0 else (acb(-rho) if j==time_nodes//2 else rho*acb(0,2*arb.pi()*j/time_nodes).exp())
        sampled,timing=model.sample(u,angles)
        values[j]=sampled
        if 0<j<time_nodes//2:
            values[time_nodes-j]=[value.conjugate() for value in sampled]
        timings.append(dict(time_node=j,**timing))
        if j%8==0 or j==time_nodes//2:
            print(json.dumps(dict(time_node=j,independent_samples=time_nodes//2+1,
                                 elapsed_seconds=time.monotonic()-start,**timing)),flush=True)
    before=time.monotonic()
    coefficients=NativeSeriesFFT().fft(values)/time_nodes
    output=np.empty((angles,1),object)
    for k in range(angles):
        output[k,0]=acb_series([coefficients[i,k]/rho**i for i in range(terms)],prec=terms)
    return output,dict(independent_scalar_time_samples=len(timings),sample_timings=timings,
                       time_DFT_seconds=time.monotonic()-before,total_seconds=time.monotonic()-start)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor',type=Path,default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--domain',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json'))
    p.add_argument('--germ',type=int,default=-1)
    p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--primitive-nodes',type=int,default=512)
    p.add_argument('--time-nodes',type=int,default=32)
    p.add_argument('--terms',type=int,default=17)
    p.add_argument('--radius',default='5/4')
    p.add_argument('--bits',type=int,default=256)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=max(21,args.terms+3)
    start=time.monotonic()
    model=ScalarTimeCircleField(args.descriptor,args.domain,germ=args.germ,nodes=args.primitive_nodes)
    root_seconds=time.monotonic()-start
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
                raise ValueError('scalar-time coefficients disagree with independently differentiated geometry')
            maximum=max(maximum,abs(values[j,0][i]-expected[0][i]).upper())
        checks.append(dict(angle_node=j,all_coefficients_overlap_after_true_time_alias=True,
                           maximum_unpadded_difference=ball_record(maximum)))
    report=dict(kind='actual_scalar_time_circle_field_and_true_time_alias_replay',complete=True,
        source_sha256=sha(__file__),domain_sha256=sha(args.domain),descriptor_sha256=sha(args.descriptor),
        target_object_sha256=sha(model.object_path),target_root_sha256=sha(model.root_path),
        common_span=list(map(str,model.cell)),exact_time_endpoints=list(map(str,model.time_endpoints)),
        angles=args.angles,primitive_nodes=args.primitive_nodes,time_nodes=args.time_nodes,
        retained_time_terms=args.terms,time_circle_radius=args.radius,bits=args.bits,
        actual_time_outer_radius=model.domain['time_radius'],actual_physical_outer_strip=model.domain['physical_theta_strip'],
        actual_outer_modulus=ball_record(model.modulus),refined_root=model.root_package.provenance,
        root_seconds=root_seconds,**timing,true_coefficient_time_alias=[ball_record(v) for v in aliases],
        independent_checks=checks,total_run_seconds=time.monotonic()-start,
        finite_polynomial_saved=False,
        limitations=['No full reference composition, continuous residual, parameter variation, or return-map estimate is asserted.',
                     'This entry checks retained coefficients; finite P storage and full angular alias budgets are separate.'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(complete=True,total_run_seconds=report['total_run_seconds'],
                         sample_seconds=timing['total_seconds'],coefficient_zero_alias=aliases[0].str())),flush=True)


if __name__=='__main__':
    main()
