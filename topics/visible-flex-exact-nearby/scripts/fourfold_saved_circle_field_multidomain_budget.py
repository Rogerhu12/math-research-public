#!/usr/bin/env python3
"""Use independently proved wider-angle and larger-time disks for saved P.

For K<N/2, real-grid Fourier folding followed by projection to |k|<=K is a
contraction in every derivative Wiener norm. This pays the analytic time
alias once, on its own proved strip; the true angular tail may use a wider
strip that is not available for the larger time disk.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_boundary_fourier_budget import reconstruction_budget,full_fourier_factor


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def upper(row):
    value=arb(row['upper']).upper()
    if not value.is_finite() or not value>=0:raise ValueError('finite nonnegative directed upper required')
    return value


def endpoints(rows):
    out=[]
    for row in rows:
        if isinstance(row,str):out.append(str(Fraction(row)))
        else:
            if Fraction(row['pi_coefficient'])!=0:raise ValueError('ordinary rational endpoints required')
            out.append(str(Fraction(row['rational'])))
    return out


def domain_data(report,wide,large,manifest):
    if not report['complete'] or not report['actual_full_time_segment_and_angle_field_proved']:
        raise ValueError('completed actual scalar-circle package required')
    identity=report['identity']
    if not manifest['complete'] or not manifest['exactly_reloaded'] or manifest['identity']!=identity:
        raise ValueError('saved polynomial identity is not the completed actual circle field')
    if 'exact complex-time DFT g_i' not in identity['coefficient_origin']:
        raise ValueError('the saved finite coefficient convention is not time-circle DFT')
    if not wide['complete'] or not large['complete']:
        raise ValueError('complete true domains required')
    for data in (wide,large):
        for key,other in [('target_object_sha256','object_sha256'),
                          ('target_root_sha256','root_certificate_sha256'),
                          ('exact_delta_fraction','exact_delta_fraction')]:
            if data[key]!=identity[other]:raise ValueError('actual domain object/parameter mismatch')
        if endpoints(data['exact_time_endpoints'])!=identity['exact_time_endpoints']:
            raise ValueError('actual domain time endpoints mismatch')
        if data['required_common_spans']!=[identity['common_span']]:
            raise ValueError('whole actual segment is not in the same single germ')
    case=next(c for c in wide['cases'] if Fraction(c['physical_theta_strip'])==Fraction(1,48))
    if not case['complete'] or not case['proved_full_physical_angle_and_complex_time_domain']:
        raise ValueError('wider true angle disk not proved')
    if len(case['germs'])!=1 or not case['germs'][0]['passed'] or not large['germs'][0]['passed']:
        raise ValueError('whole chosen germ missing')
    if large['branch_sign']!=identity['branch_sign']:
        raise ValueError('larger time disk branch mismatch')
    # The wider-angle proof bounds |M|+sqrt(|K|)|W| over |D| and hence
    # bounds either sign. Its positive-real -K gate fixes the same root.
    triples=[]
    for data,c in [(wide,case),(large,large)]:
        triples.append((exact_arb(Fraction(data['time_radius'])),
                        exact_arb(Fraction(c['physical_theta_strip'])),
                        upper(c['germs'][0]['true_field_moduli']['f'])))
    return triples


def budget(report,triples,inner_time,inner_strip,derivative):
    n,k=report['angular_nodes'],report['retained_Fourier_degree']
    errors=list(map(upper,report['node_and_DFT_error_of_aliased_time_coefficients']))
    m=len(errors);r=exact_arb(inner_time);s=exact_arb(inner_strip)
    rho=exact_arb(Fraction(report['identity']['time_circle_radius']))
    Nt=report['identity']['time_circle_nodes']
    if not 0<=k<n/2 or not all(r<R and s<S for R,S,M in triples):
        raise ValueError('invalid finite projection or requested actual subdomain')
    noise=sum((r**i*e for i,e in enumerate(errors)),arb(0)).upper()
    angular=[]
    time_tails=[]
    for R,S,M in triples:
        retained=M*sum(((r/R)**i for i in range(m)),arb(0))
        angular.append(reconstruction_budget(n,k,arb(0),S,s,retained,noise,derivative))
        factor=full_fourier_factor(S,s,derivative)
        time_tails.append((M*factor*(r/R)**m/(1-r/R)).upper())
    R,S,M=triples[-1]
    if not rho<R:raise ValueError('actual time circle is outside larger disk')
    alias=(rho/R)**Nt/(1-(rho/R)**Nt)
    time_alias=(M*full_fourier_factor(S,s,derivative)*alias*
                sum(((r/R)**i for i in range(m)),arb(0))).upper()
    # Each separate angular estimate is valid; their two sums may be
    # minimized componentwise without mixing unproved bidisks.
    result=dict(node_error=angular[0]['node_error'],
        true_Fourier_alias=min((b['alias'] for b in angular),key=lambda z:float(z)),
        true_Fourier_tail=min((b['fourier_tail'] for b in angular),key=lambda z:float(z)),
        folded_time_circle_alias=time_alias,
        omitted_true_time_tail=min(time_tails,key=lambda z:float(z)))
    result['total']=sum(result.values(),arb(0)).upper()
    return {key:ball_record(value.upper()) for key,value in result.items()}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    base=Path('data/phase_ring_continuation')
    p.add_argument('--certificate',type=Path,default=base/'type_fixed_step02_d5_exact_affine_step5_reference419_time_circle_field.json')
    p.add_argument('--wider-angle',type=Path,default=base/'type_fixed_step02_d5_exact_affine_step5_reference419_actual_angle_anchors_narrow.json.gz')
    p.add_argument('--larger-time',type=Path,default=base/'step5_sharp_time_domain_R6_order40/forward_0419_r.json.gz')
    p.add_argument('--times',default='1,5/4,3/2')
    p.add_argument('--strips',default='81/10000,1/256,1/512')
    p.add_argument('--bits',type=int,default=256)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    report=read(args.certificate);wide=read(args.wider_angle);large=read(args.larger_time)
    path=Path(report['polynomial_manifest']);manifest=read(path)
    if sha(path)!=report['polynomial_manifest_sha256']:
        raise ValueError('saved polynomial manifest hash changed')
    for row in manifest['shards']:
        pth=path.parent/row['path']
        if sha(pth)!=row['sha256'] or pth.stat().st_size!=row['bytes']:
            raise ValueError('saved exact polynomial shard changed')
    domains=domain_data(report,wide,large,manifest)
    rows=[]
    for r in map(Fraction,args.times.split(',')):
        for s in map(Fraction,args.strips.split(',')):
            rows.append(dict(normalized_time_radius=str(r),physical_theta_strip=str(s),
                             derivative_budgets={str(j):budget(report,domains,r,s,j) for j in range(3)}))
    output=dict(kind='actual_saved_circle_field_multidomain_complete_error',complete=True,
        source_sha256=sha(__file__),bits=args.bits,
        certificate_sha256=sha(args.certificate),polynomial_manifest_sha256=sha(path),
        wider_angle_certificate_sha256=sha(args.wider_angle),larger_time_certificate_sha256=sha(args.larger_time),
        exact_identity=report['identity'],actual_domains=[dict(time_radius=ball_record(R),
             physical_angle_strip=ball_record(S),modulus=ball_record(M)) for R,S,M in domains],
        budgets=rows,limitations=['Same actual segment419 field only; no reference image or flow conclusion.',
          'Larger-time and wider-angle domains are used separately; their Cartesian product is not asserted.'])
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps([dict(time=r['normalized_time_radius'],strip=r['physical_theta_strip'],
         error=r['derivative_budgets']['0']['total']['ball']) for r in rows]),flush=True)


if __name__=='__main__':main()
