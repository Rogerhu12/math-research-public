#!/usr/bin/env python3
"""Complete continuous density g=(h*f(u,Y)-Y_u)/Y_x on one actual segment.

First reconstruct the holomorphic finite proxy g_P with its own entire field
P and independently proved reference bidisks. Then add f-P only on the real
time/working-label domain. True field errors are never DFT sample noise.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_actual_field_fourier_package import (
    load_polynomial,encode_complex,decode_complex,write_json)
from fourfold_exact_fourier_multipoint import time_coefficients
from fourfold_fourier_local_taylor import finite_taylor_evaluate
from fourfold_packaged_reference_bidisk import PackageReference
from fourfold_saved_circle_field_multidomain_budget import read,upper,domain_data,budget
from fourfold_boundary_fourier_budget import reconstruction_budget,full_fourier_factor


def reference_case(path,reference,R,S):
    data=read(path)
    if (not data['complete'] or data['identity']!=reference.identity
            or data['package_sha256']!=reference.package['sha256']):
        raise ValueError('reference bidisk is incomplete or belongs to another exact reference')
    row=next(c for c in data['cases'] if Fraction(c['time_radius'])==R
             and Fraction(c['initial_label_strip'])==S)
    if not row['q_nonzero_on_complete_bidisk_proved']:
        raise ValueError('complete reference q gate has not passed')
    q=arb(row['full_complex_time_and_label_q_real_lower']['lower']).lower()
    if not q>0:raise ValueError('nonpositive directed reference q lower bound')
    return row,q


def finite_field_modulus(coefficients,R,S):
    K=(coefficients.shape[1]-1)//2
    weights=[(4*abs(k-K)*S).exp() for k in range(coefficients.shape[1])]
    return sum((R**i*sum((abs(a)*w for a,w in zip(row,weights)),arb(0))
                for i,row in enumerate(coefficients)),arb(0)).upper()


def density_budget(domains,errors,nodes,degree,rho,time_nodes,inner_strip):
    """A_s error for g_P minus its saved real dyadic polynomial, |u|<=1."""
    m=len(errors);noise=sum(errors,arb(0)).upper();angular=[];alias=[];tail=[]
    for R,S,M in domains:
        if not 1<R or not rho<R or not inner_strip<S:
            raise ValueError('density outer bidisk does not contain requested working domain')
        retained=M*sum((R**(-i) for i in range(m)),arb(0))
        angular.append(reconstruction_budget(nodes,degree,arb(0),S,inner_strip,
                         retained,noise,frequency_scale=1))
        factor=full_fourier_factor(S,inner_strip,frequency_scale=1)
        rat=(rho/R)**time_nodes
        alias.append((M*factor*rat/(1-rat)*sum((R**(-i) for i in range(m)),arb(0))).upper())
        tail.append((M*factor*R**(-m)/(1-1/R)).upper())
    result=dict(node_and_exact_coefficient_choice_error=angular[0]['node_error'],
        true_initial_label_Fourier_alias=min(a['alias'] for a in angular),
        true_initial_label_Fourier_tail=min(a['fourier_tail'] for a in angular),
        folded_time_circle_alias=min(alias),omitted_true_time_tail=min(tail))
    result['total']=sum(result.values(),arb(0)).upper()
    return {key:ball_record(value.upper()) for key,value in result.items()}


def preserve_density(values,rho,terms,degree,directory,identity,save_progress):
    """DFT the sampled *finite proxy*, preserving all node/rounding fees."""
    Nt,N=values.shape
    if not 0<terms<=Nt or not 0<=degree<N//2:
        raise ValueError('invalid density rectangle')
    tic,cpu=time.monotonic(),time.process_time()
    # Time DFT is unnormalized. At real initial labels, its aliased Taylor
    # coefficients are real by exact Schwarz reflection in complex time.
    node_midpoints=np.empty((terms,N),object)
    total=[arb(0) for _ in range(terms)];maximum=[arb(0) for _ in range(terms)]
    for j in range(N):
        row=acb.dft(list(values[:,j]))
        for i in range(terms):
            value=row[i]/(Nt*rho**i)
            if not value.is_finite() or not value.imag.contains(0):
                raise ValueError('density time coefficient reality/finiteness failed')
            fee=value.real.rad().upper()
            total[i]+=fee;maximum[i]=max(maximum[i],fee)
            node_midpoints[i,j]=acb(value.real.mid())
    del values
    mean=[(a/N).upper() for a in total]
    coefficients=[];errors=[];rounding=[]
    for i in range(terms):
        transformed=acb.dft(list(node_midpoints[i]))
        selected=[];fee=arb(0)
        for k in range(degree+1):
            value=transformed[k]/N
            chosen=acb(value.real.mid(),0 if k==0 else value.imag.mid())
            if k==0 and not value.imag.contains(0):raise ValueError('nonreal exact zero mode')
            fee=max(fee,abs(value-chosen).upper());selected.append(chosen)
        coefficients.append(selected);rounding.append(fee)
        errors.append((mean[i]+fee).upper())
    del node_midpoints
    directory.mkdir(parents=True,exist_ok=True)
    manifest=dict(kind='exact_dyadic_reference_coordinate_density',schema_version=1,
        complete=False,exactly_reloaded=False,identity=identity,source_sha256=sha(__file__),
        frequency_scale=1,Fourier_degree=degree,time_terms=terms,bits=ctx.prec,
        definition='sum_i sum_k c[i,k]*u**i*exp(I*k*x); negative k conjugate, zero k real',
        coordinate='g_P=(signed_h_tau*P(u,Y)-Y_u)/Y_x, u from -1 to 1',
        coefficient_origin='real initial-label DFT of complex-time-circle aliased coefficients',
        shards=[],scope='Exact finite chosen polynomial only; complete analytic error is a separate report.')
    path=directory/'manifest.json';write_json(path,manifest)
    for first in range(0,terms,4):
        stop=min(first+4,terms)
        payload=dict(kind='exact_dyadic_reference_coordinate_density_shard',time_start=first,
            time_stop=stop,Fourier_degree=degree,identity=identity,
            coefficients=[[encode_complex(v) for v in coefficients[i]] for i in range(first,stop)])
        data=gzip.compress((json.dumps(payload,separators=(',',':'))+'\n').encode(),compresslevel=9,mtime=0)
        name='coefficients_t%03d_%03d.json.gz'%(first,stop-1)
        destination=directory/name;temporary=destination.with_name(name+'.writing')
        temporary.write_bytes(data);temporary.replace(destination)
        manifest['shards'].append(dict(path=name,time_start=first,time_stop=stop,
            sha256=hashlib.sha256(data).hexdigest(),bytes=len(data)))
        write_json(path,manifest);save_progress()
    manifest['complete']=True
    manifest['coefficient_error_budget']=dict(
        mean_aliased_time_coefficient_node_error=list(map(ball_record,mean)),
        maximum_aliased_time_coefficient_node_error=list(map(ball_record,maximum)),
        maximum_directed_DFT_and_choice_error=list(map(ball_record,rounding)),
        complete_retained_coefficient_error=list(map(ball_record,errors)))
    write_json(path,manifest)
    loaded,again=load_density(path)
    if loaded['identity']!=identity or any(a!=b for row,other in zip(coefficients,again)
                                            for a,b in zip(row,other)):
        raise ValueError('density exact reload failed')
    manifest['exactly_reloaded']=True;write_json(path,manifest)
    return path,coefficients,errors,dict(wall_seconds=time.monotonic()-tic,
                                      cpu_seconds=time.process_time()-cpu)


def load_density(path):
    path=Path(path);m=read(path)
    if (m['kind']!='exact_dyadic_reference_coordinate_density' or not m['complete']
            or m['schema_version']!=1 or m['frequency_scale']!=1):
        raise ValueError('wrong or incomplete exact density schema')
    rows=[];next_time=0
    for shard in m['shards']:
        p=path.parent/shard['path']
        if p.stat().st_size!=shard['bytes'] or sha(p)!=shard['sha256']:
            raise ValueError('density shard hash/size mismatch')
        data=read(p)
        if (data['identity']!=m['identity'] or data['time_start']!=next_time
                or data['time_start']!=shard['time_start'] or data['time_stop']!=shard['time_stop']
                or data['Fourier_degree']!=m['Fourier_degree']
                or len(data['coefficients'])!=data['time_stop']-next_time):
            raise ValueError('density shard identity/order mismatch')
        for row in data['coefficients']:
            if len(row)!=m['Fourier_degree']+1:raise ValueError('density Fourier shape mismatch')
            decoded=[decode_complex(z) for z in row]
            if decoded[0].imag!=0:raise ValueError('density zero mode is not real')
            rows.append(decoded)
        next_time=data['time_stop']
    if next_time!=m['time_terms']:raise ValueError('missing density time coefficients')
    return m,rows


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path('data/phase_ring_continuation')
    p.add_argument('--package',type=Path,default=base/'step5_forward419_exact_reference_package.npz.gz')
    p.add_argument('--field-certificate',type=Path,default=base/'type_fixed_step02_d5_exact_affine_step5_reference419_time_circle_field.json')
    p.add_argument('--wider-angle',type=Path,default=base/'type_fixed_step02_d5_exact_affine_step5_reference419_actual_angle_anchors_narrow.json.gz')
    p.add_argument('--larger-time',type=Path,default=base/'step5_sharp_time_domain_R6_order40/forward_0419_r.json.gz')
    p.add_argument('--wide-reference-gate',type=Path,default=Path('notes/2026-11-12-actual-retarget419-bidisk-broad-label-gates.json'))
    p.add_argument('--large-reference-gate',type=Path,default=Path('notes/2026-11-12-actual-retarget419-bidisk-reference-gates.json'))
    p.add_argument('--real-reference-gate',type=Path,default=Path('notes/2026-11-12-actual-retarget419-real-time-reference-gates.json'))
    p.add_argument('--label-strip',default='1/128');p.add_argument('--field-strip',default='3/500')
    p.add_argument('--nodes',type=int,default=8192);p.add_argument('--degree',type=int,default=3500)
    p.add_argument('--time-nodes',type=int,default=64);p.add_argument('--terms',type=int,default=48)
    p.add_argument('--circle-radius',default='5/4');p.add_argument('--anchors',type=int,default=512)
    p.add_argument('--evaluation-tail',default='1e-42');p.add_argument('--bits',type=int,default=320)
    p.add_argument('--polynomial-dir',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    if args.nodes<2 or args.nodes&(args.nodes-1) or args.time_nodes<2 or args.time_nodes%2:
        raise ValueError('power-of-two angle nodes and even positive time nodes required')
    start,cpu=time.monotonic(),time.process_time()
    ref=PackageReference(args.package);fc=read(args.field_certificate)
    manifest_path=Path(fc['polynomial_manifest'])
    if sha(manifest_path)!=fc['polynomial_manifest_sha256']:raise ValueError('field manifest hash mismatch')
    field_manifest,field=load_polynomial(manifest_path)
    field_domains=domain_data(fc,read(args.wider_angle),read(args.larger_time),field_manifest)
    fi=field_manifest['identity'];ri=ref.identity
    for fk,rk in [('object_sha256','target_object_sha256'),('root_certificate_sha256','target_root_sha256'),
                  ('exact_delta_fraction','target_exact_delta_fraction'),('branch_sign','branch_sign')]:
        if fi[fk]!=ri[rk]:raise ValueError('field/reference exact identity mismatch: '+fk)
    if ref.center!=exact_arb(Fraction(fi['tau_center'])) or ref.h!=exact_arb(Fraction(fi['time_halfwidth'])):
        raise ValueError('field/reference signed time coordinates differ')
    Swork=Fraction(args.label_strip);s=exact_arb(Swork);rho=exact_arb(Fraction(args.circle_radius))
    identity=dict(reference=ri,field_polynomial_manifest_sha256=sha(manifest_path),
                  time_circle_radius=args.circle_radius,time_circle_nodes=args.time_nodes)
    report=dict(kind='actual_complete_reference_coordinate_density_on_one_segment',complete=False,
        source_sha256=sha(__file__),identity=identity,bits=args.bits,angular_nodes=args.nodes,
        retained_initial_label_degree=args.degree,retained_time_terms=args.terms,
        initial_label_strip=args.label_strip,field_error_physical_strip=args.field_strip,
        true_field_certificate_sha256=sha(args.field_certificate),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_packaged_reference_bidisk.py','fourfold_retarget_reference_native_grid.py',
            'fourfold_retarget_reference_segment_package.py','fourfold_fourier_local_taylor.py',
            'fourfold_phase_actual_field_fourier_package.py','fourfold_exact_fourier_multipoint.py',
            'fourfold_saved_circle_field_multidomain_budget.py','fourfold_boundary_fourier_budget.py')},
        finite_proxy_domains=[],samples=[])
    def save():write_json(args.out,report)
    save();domains=[]
    for gate,R,S in [(args.wide_reference_gate,Fraction(3),Fraction(3,100)),
                     (args.large_reference_gate,Fraction(3),Fraction(1,64)),
                     (args.large_reference_gate,Fraction(6),Fraction(1,64))]:
        row,q=reference_case(gate,ref,R,S)
        image=upper(row['physical_theta_image_strip']);yu=upper(row['full_Yu_modulus'])
        MP=finite_field_modulus(field,exact_arb(R),image)
        Mg=((abs(ref.h)*MP+yu)/q).upper()
        domains.append((exact_arb(R),exact_arb(S),Mg))
        report['finite_proxy_domains'].append(dict(reference_gate=str(gate),reference_gate_sha256=sha(gate),
            time_radius=str(R),initial_label_strip=str(S),physical_reference_image=ball_record(image),
            reference_q_real_lower=ball_record(q),finite_field_full_modulus=ball_record(MP),
            finite_density_full_modulus=ball_record(Mg)))
        save()
    real,qreal=reference_case(args.real_reference_gate,ref,Fraction(1),Swork)
    physical_strip=Fraction(args.field_strip)
    if not upper(real['physical_theta_image_strip'])<exact_arb(physical_strip):
        raise ValueError('real-time reference image leaves actual field approximation domain')
    true_field_budget=budget(fc,field_domains,Fraction(1),physical_strip,0)
    real_fee=(abs(ref.h)*upper(true_field_budget['total'])/qreal).upper()
    report['true_field_transfer']=dict(reference_gate=str(args.real_reference_gate),
        reference_gate_sha256=sha(args.real_reference_gate),reference_image=real['physical_theta_image_strip'],
        reference_q_real_lower=ball_record(qreal),field_error_budget=true_field_budget,
        full_density_error_on_real_time_working_label_strip=ball_record(real_fee),
        larger_time_certificate_sha256=sha(args.larger_time),wider_angle_certificate_sha256=sha(args.wider_angle),
        included_in_DFT_node_noise=False)
    save()
    values=np.empty((args.time_nodes,args.nodes),object)
    for j in range(args.time_nodes//2+1):
        tic=time.monotonic();sample_cpu=time.process_time()
        u=acb(rho) if j==0 else (acb(-rho) if j==args.time_nodes//2
            else rho*acb(0,2*arb.pi()*j/args.time_nodes).exp())
        Y,Yu,Yx=ref.grid(u,args.nodes,Fraction(0))
        P,info=finite_taylor_evaluate(time_coefficients(field,u),Y,anchors=args.anchors,
                    radius=Fraction(1,64),tail_target=args.evaluation_tail)
        sampled=[(ref.h*a-b)/q for a,b,q in zip(P,Yu,Yx)]
        if not all(z.is_finite() for z in sampled):raise ValueError('nonfinite actual density sample')
        values[j]=sampled
        if 0<j<args.time_nodes//2:values[args.time_nodes-j]=[z.conjugate() for z in sampled]
        timing=dict(time_node=j,u=repr(u),finite_P_evaluation=info,
            maximum_node_density_modulus=ball_record(max(abs(z).upper() for z in sampled)),
            wall_seconds=time.monotonic()-tic,cpu_seconds=time.process_time()-sample_cpu)
        report['samples'].append(timing);save()
        if j%4==0 or j==args.time_nodes//2:
            print(json.dumps(dict(time_node=j,independent_nodes=args.time_nodes//2+1,
                cpu_seconds=timing['cpu_seconds'],density=timing['maximum_node_density_modulus']['ball'])),flush=True)
    path,coefficients,errors,timing=preserve_density(values,rho,args.terms,args.degree,
                                        args.polynomial_dir,identity,save)
    report['density_polynomial_manifest']=str(path);report['density_polynomial_manifest_sha256']=sha(path)
    report['DFT_preservation_timing']=timing
    finite_budget=density_budget(domains,errors,args.nodes,args.degree,rho,args.time_nodes,s)
    report['complete_finite_proxy_reconstruction_error']=finite_budget
    total=(upper(finite_budget['total'])+real_fee).upper()
    report['full_true_density_uniform_error']=ball_record(total)
    coefficient_norms=[];primitive=[]
    for i,row in enumerate(coefficients):
        value=abs(row[0])+2*sum((abs(v)*(k*s).exp() for k,v in enumerate(row[1:],1)),arb(0))
        coefficient_norms.append(value.upper())
    for k in range(args.degree+1):
        primitive.append(sum((2*coefficients[i][k]/(i+1) for i in range(0,args.terms,2)),acb(0)))
    finite_A=sum((2*v/(i+1) for i,v in enumerate(coefficient_norms)),arb(0)).upper()
    finite_sup=sum(coefficient_norms,arb(0)).upper()
    first_norm=(abs(primitive[0])+2*sum((abs(v)*(k*s).exp()
                 for k,v in enumerate(primitive[1:],1)),arb(0))).upper()
    report['R72_inputs_on_this_whole_segment']=dict(
        exact_finite_density_time_coefficient_A_norms=list(map(ball_record,coefficient_norms)),
        integrated_finite_density_majorant=ball_record(finite_A),
        common_integrated_majorant_A=ball_record((finite_A+2*total).upper()),
        integrated_approximation_error_E=ball_record((2*total).upper()),
        finite_density_uniform_majorant=ball_record(finite_sup),
        common_density_uniform_majorant=ball_record((finite_sup+total).upper()),
        exact_finite_first_integral_A_norm=ball_record(first_norm),
        convention='Integral du from -1 to 1; h_tau already signed inside g. Initial-label frequency is 1.')
    report['complete']=True;report['complete_continuous_true_density_proved_on_this_segment']=True
    report['wall_seconds']=time.monotonic()-start;report['cpu_seconds']=time.process_time()-cpu
    report['limitations']=['Only the identity-matched actual delta5 forward segment419.',
        'The true field segment lies wholly in one common germ; no unpaid crossing caps are included.',
        'No other segment, parameter derivative, full return, exact metric family or final geometry is inferred.']
    save();print(json.dumps(dict(complete=True,error=report['full_true_density_uniform_error'],
        A=report['R72_inputs_on_this_whole_segment']['common_integrated_majorant_A'],
        cpu_seconds=report['cpu_seconds'],wall_seconds=report['wall_seconds'])),flush=True)


if __name__=='__main__':main()
