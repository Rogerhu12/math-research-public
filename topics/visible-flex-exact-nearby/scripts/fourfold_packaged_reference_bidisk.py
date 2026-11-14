#!/usr/bin/env python3
"""Full finite reference image and nonzero q on a complex time/label bidisk.

The exact reference is loaded from its self-contained single-segment package.
All symbolic Fourier products are materialized without truncation, as balls
enclosing the *same exact coefficients*. Pointwise closed-cell angular bounds
retain correlation between the small q center and its own time variation.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
import math
from pathlib import Path
import time
from flint import arb,acb,acb_poly,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_retarget_reference_jets import scalar_time_coefficients,time_value
from fourfold_retarget_reference_native_grid import NativeRetargetSegment,RealTimeFourier
from fourfold_retarget_reference_segment_package import load_package


def laurent(row):
    return [v.conjugate() for v in row[:0:-1]]+list(row)


class PackageReference(NativeRetargetSegment):
    def __init__(self,path,left=Fraction(0),right=Fraction(1)):
        if not 0<=left<right<=1:raise ValueError('invalid reference restriction')
        package=load_package(path);arrays=package['arrays'];docs=package['documents']
        meta=package['metadata'];identity=meta['identity'];d=docs['descriptor']['document']
        self.package=package;self.reference=None
        self.leg,self.segment=identity['leg'],identity['segment'];self.left,self.right=left,right
        self.U=RealTimeFourier(scalar_time_coefficients(arrays['base_real'][:,0,:],
                               arrays['base_imag'][:,0,:],left,right))
        self.Q=RealTimeFourier(scalar_time_coefficients(arrays['Q_real'],arrays['Q_imag'],left,right))
        initial=docs['initial_correction']['document'];D=2**int(initial['denominator_power_of_two'])
        self.a=RealTimeFourier([[acb(arb(int(a))/D,arb(int(b))/D)
                    for a,b in initial['nonnegative_integer_coefficients']]])
        self.end=RealTimeFourier([[acb(arb(float(a)),arb(float(b)))
                    for a,b in zip(arrays['forward_end_Q_real'],arrays['forward_end_Q_imag'])]]) if self.leg=='backward' else None
        a,b=map(time_value,meta['exact_time_rows'])
        ta=a+(b-a)*exact_arb(left);tb=a+(b-a)*exact_arb(right)
        self.center,self.h=(ta+tb)/2,(tb-ta)/2
        base=docs['old_'+self.leg+'_reference']['document']
        if not base['time_orientation']*self.h>0:raise ValueError('incorrect reference time orientation')
        self.identity=dict(retarget_descriptor_sha256=docs['descriptor']['sha256'],
            leg=self.leg,segment=self.segment,normalized_subspan=[str(left),str(right)],
            exact_segment_time_rows=meta['exact_time_rows'],branch_sign=identity['branch_sign'],
            target_exact_delta_fraction=identity['target_exact_delta_fraction'],
            old_exact_delta_fraction=identity['old_exact_delta_fraction'],
            target_object_sha256=identity['target_object_sha256'],
            target_root_sha256=identity['target_root_sha256'],package_sha256=package['sha256'])
        self._static={};self._full=None

    def complete_periodic(self):
        """Enclose every coefficient of U+Q*a (or U+Q*(Qend*a))."""
        if self._full is not None:return self._full
        static=acb_poly(laurent(self.a.coefficients[0]));KB=self.a.K
        if self.end is not None:
            static=static*acb_poly(laurent(self.end.coefficients[0]));KB+=self.end.K
        K=max(self.U.K,self.Q.K+KB);positive=[]
        for i in range(self.U.terms):
            product=acb_poly(laurent(self.Q.coefficients[i]))*static
            row=[acb(0) for _ in range(2*K+1)]
            offset=K-self.Q.K-KB
            for j in range(2*(self.Q.K+KB)+1):row[j+offset]+=product[j]
            offset=K-self.U.K
            for j,value in enumerate(laurent(self.U.coefficients[i])):row[j+offset]+=value
            if not row[K].imag.contains(0):raise ValueError('real mean coefficient lost exact reality')
            # These are enclosures, not new chosen coefficient midpoints.
            # Reality of the exact symbolic product fixes its negative modes.
            positive.append([acb(row[K].real)]+row[K+1:])
        self._full=RealTimeFourier(positive)
        return self._full


def continuous_bidisk(reference,*,time_radius=Fraction(3),label_width=Fraction(1,64),
                      nodes=2048,taylor_order=6):
    if nodes<2 or nodes&(nodes-1) or taylor_order<2:
        raise ValueError('positive power-of-two angle grid and Taylor order>=2 required')
    R,s=exact_arb(time_radius),exact_arb(label_width)
    if not R>=1 or not s>=0:raise ValueError('invalid outer reference bidisk')
    full=reference.complete_periodic();K=full.K;p=taylor_order
    hx=arb.pi()/nodes
    frequencies=list(range(-K,K+1));weights=[(-k*s).exp() for k in frequencies]
    variation_q=[arb(0) for _ in range(nodes)]
    image=[arb(0) for _ in range(nodes)]
    yu=[arb(0) for _ in range(nodes)]
    q_lower=None;q_upper=None;center_q_lower=None
    derivative_gaps=[];start,cpu=time.monotonic(),time.process_time()
    for i,row in enumerate(full.coefficients):
        terms=laurent(row)
        current=[v*w for v,w in zip(terms,weights)]
        table=[]
        for j in range(p+1):
            folded=[acb(0) for _ in range(nodes)]
            for k,value in zip(frequencies,current):folded[k%nodes]+=value
            table.append([nodes*v for v in acb.dft(folded,inverse=True)])
            if j<p:current=[v*acb(0,k)*hx/(j+1) for k,v in zip(frequencies,current)]
        Uremainder=sum((abs(v)*abs(w)*(abs(k)*hx)**(p+1)/math.factorial(p+1)
                       for k,v,w in zip(frequencies,terms,weights)),arb(0)).upper()
        Qremainder=sum((abs(v)*abs(w)*abs(k)*(abs(k)*hx)**p/math.factorial(p)
                       for k,v,w in zip(frequencies,terms,weights)),arb(0)).upper()
        derivative_gaps.append(dict(time_coefficient=i,U_remainder=ball_record(Uremainder),
                                    q_remainder=ball_record(Qremainder)))
        lower=[];upper=[]
        for j in range(nodes):
            Ugap=sum((abs(table[r][j]) for r in range(1,p+1)),arb(0))+Uremainder
            qcenter=table[1][j]/hx+(arb(1)/4 if i==0 else 0)
            qgap=sum((abs((r+1)*table[r+1][j]/hx) for r in range(1,p)),arb(0))+Qremainder
            Ubound=(abs(table[0][j])+Ugap).upper()
            qbound=(abs(qcenter)+qgap).upper()
            if i==0:
                lower.append((qcenter.real-qgap).lower());upper.append(qbound)
                image[j]=(abs(s/4+table[0][j].imag)+Ugap).upper()
            else:
                variation_q[j]+=(R**i*qbound).upper()
                image[j]+=(R**i*Ubound).upper()
                yu[j]+=(i*R**(i-1)*Ubound).upper()
        if i==0:q_lower,q_upper=lower,upper;center_q_lower=min(lower)
    for j in range(nodes):
        q_lower[j]=(q_lower[j]-variation_q[j]).lower()
        q_upper[j]=(q_upper[j]+variation_q[j]).upper()
    minimum=min(q_lower);maximum=max(q_upper)
    physical_image=max(image).upper();Yumax=max(yu).upper()
    result=dict(time_radius=str(time_radius),initial_label_strip=str(label_width),
        physical_theta_image_strip=ball_record(physical_image),
        full_complex_time_and_label_q_real_lower=ball_record(minimum),
        full_complex_time_and_label_q_modulus_upper=ball_record(maximum),
        full_Yu_modulus=ball_record(Yumax),
        real_time_center_q_real_lower=ball_record(center_q_lower),
        maximum_pointwise_time_q_variation=ball_record(max(variation_q).upper()),
        global_separated_q_floor=ball_record((center_q_lower-max(variation_q)).lower()),
        q_nonzero_on_complete_bidisk_proved=bool(minimum>0),
        Fourier_degree=K,time_terms=full.terms,angular_nodes=nodes,taylor_order=p,
        all_symbolic_products_retained=True,both_label_boundaries_by_exact_reality=True,
        derivative_remainders=derivative_gaps,
        wall_seconds=time.monotonic()-start,cpu_seconds=time.process_time()-cpu)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package',type=Path,default=Path('data/phase_ring_continuation/step5_forward419_exact_reference_package.npz.gz'))
    p.add_argument('--time-radii',default='3,6')
    p.add_argument('--label-widths',default='1/64,1/128')
    p.add_argument('--nodes',type=int,default=2048);p.add_argument('--taylor-order',type=int,default=6)
    p.add_argument('--bits',type=int,default=256)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    reference=PackageReference(args.package);report=dict(kind='actual_exact_retarget_reference_complete_bidisk_gate',
        complete=False,source_sha256=sha(__file__),bits=args.bits,identity=reference.identity,
        package_sha256=sha(args.package),cases=[],
        scope='Full finite reference image/q gates, not a true-field residual or true-flow certificate.')
    def save():args.out.write_text(json.dumps(report,indent=2)+'\n')
    save()
    for S in map(Fraction,args.label_widths.split(',')):
        for R in map(Fraction,args.time_radii.split(',')):
            row=continuous_bidisk(reference,time_radius=R,label_width=S,nodes=args.nodes,taylor_order=args.taylor_order)
            report['cases'].append(row);save()
            print(json.dumps({k:row[k] for k in ('time_radius','initial_label_strip','physical_theta_image_strip',
               'full_complex_time_and_label_q_real_lower','q_nonzero_on_complete_bidisk_proved','cpu_seconds')}),flush=True)
    full=reference.complete_periodic();checks=[]
    # Independent evaluation routes: original symbolic products at each point,
    # versus a single materialized full Fourier polynomial. No grid projection.
    for u in [acb(arb(1)/2,arb(1)/8),acb(0,arb(5)/4)]:
        Y,Yu,Yx=reference.grid(u,16,Fraction(1,512))
        U,Uu,Ux=full.grid(u,16,Fraction(1,512))
        for j in range(16):
            label=acb(2*arb.pi()*j/16,arb(1)/512)
            actual=[Y[j],Yu[j],Yx[j]];expected=[label/4+U[j],Uu[j],arb(1)/4+Ux[j]]
            if not all(a.real.overlaps(b.real) and a.imag.overlaps(b.imag) for a,b in zip(actual,expected)):
                raise ValueError('materialized full reference differs from symbolic products')
        checks.append(dict(u=repr(u),all_16_full_symbolic_product_checks_passed=True))
    report['symbolic_product_checks']=checks;report['complete']=True;save()


if __name__=='__main__':main()
