#!/usr/bin/env python3
"""Independently consume every saved exact row of the full1200 certificate.

This reads the complete archived radii, images, positive distance weights,
Jw and all25 physical domains. It independently reconstructs the chosen
radii and physical domains from the frozen original inputs. It does not
rerun an ODE, a near-window kernel, the float proposal, or the original map.
The complete source formulas are covered by the separate read-only audit.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

PINS=dict(certificate='36242d95a210e6aee3e38c994d0a70b61fa1fbb2df672a9ab3f4783bcca93ca1',
    producer='ecdf2516665f10b95ab201dbd92aa42f4e6145f08be0c6c8b6d1db540d611074',
    nonlow_interface='eb5a9a9f2cf01f635f0942bef9299184afb30baab273d26251450395d9046f65')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p=Path(path);data=p.read_bytes()
    return json.loads(gzip.decompress(data) if p.suffix=='.gz' else data)


def exact(value):
    if isinstance(value,int):return F(value)
    if isinstance(value,dict):return F(int(value['numerator']),int(value['denominator']))
    return F(int(value[0]))*F(2)**int(value[1])


def rec(value):
    return dict(numerator=str(value.numerator),denominator=str(value.denominator),display_only=float(value))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('certificate','resource','producer','out'):
        ap.add_argument('--'+key,type=Path,required=True)
    a=ap.parse_args();started=time.monotonic();gates={};comparisons=0;ids={}
    if a.out.exists():raise FileExistsError(a.out)
    def gate(name,condition):
        nonlocal comparisons
        comparisons+=1
        if not condition:raise ArithmeticError(name)
        gates[name]=True
    def checked(record):
        p=Path(record['path']);actual=sha(p)
        gate('identity_'+str(p),actual==record['sha256']);ids[str(p)]=actual
        return read(p)
    gate('pinned_actual_complete_primary',sha(a.certificate)==PINS['certificate'])
    gate('pinned_original_producer',sha(a.producer)==PINS['producer'])
    cert,rs=read(a.certificate),read(a.resource)
    gate('formal_original_exit_zero',rs['exitcode']==0 and rs['termination_signal'] is None)
    gate('full_original_certificate_success',cert['all_gates'] and all(cert['gates'].values())
         and cert['source_sha256']==PINS['producer'])
    gate('all_original_frequency_ranges',cert['low_modes']==list(range(2,93,2))
         and cert['middle_modes']==[94,34814] and cert['infinite_high_cutoff']==34816)
    gate('original_mixed_boundary_scope',cert['full_outer_mixed_boundary_fixed_point_claimed']
         and cert['complete_mean_and_inverse_retained'] and cert['parameter_cut_closed'] is False
         and cert['closed_surface_claimed'] is False and cert['float_proposal_is_not_a_proof'])
    inputs=cert['inputs'];read_inputs={}
    for name,record in inputs.items():
        if name=='nonlow_interface':
            gate('pinned_nonlow_interface',sha(record['path'])==record['sha256']==PINS[name])
            ids[record['path']]=record['sha256']
        else:read_inputs[name]=checked(record)
    cond=read_inputs['conditional_nonlow'];joint=read_inputs['joint'];ss=read_inputs['low_source_summary']
    low=read_inputs['low_summary'];initial=checked(ss['conditional_image_record'])
    gate('same_uniform_complex_R100_domain',cond['same_R126_parameter_domain']
         and exact(cond['transverse_radius'])==F(1,32)
         and exact(joint['transverse_radius'])==F(1,32))
    gate('same_complete25block_partition',ss['comparison_partition']==low['comparison_partition']
         ==joint['comparison_partition']==cond['comparison_partition'])
    for record in ss['source_records']:checked(record)
    for record in low['target_records']:checked(record)
    u=[[exact(x) for x in row] for row in cert['low_mode_radii']]
    r=list(map(exact,cert['finite_radii']));h=list(map(exact,cert['high_radii']))
    gate('complete1200_radius_layout',len(u)==25 and all(len(row)==46 for row in u)
         and len(r)==len(h)==25)
    for j in range(25):
        for m in range(46):
            gate(f'low_radius_identity_{j}_{m}',u[j][m]==exact(cond['low_mode_radii'][j][m])
                 ==2*exact(initial['rows'][j]['separate_mode_caps'][m]))
        gate(f'finite_radius_identity_{j}',r[j]==exact(cond['rows'][j]['finite_radius']))
        gate(f'high_radius_identity_{j}',h[j]==exact(cond['rows'][j]['high_radius']))
    radii=[value for row in u for value in row]+r+h
    image=list(map(exact,cert['complete_images']));weights=list(map(exact,cert['distance_weights']))
    jw=list(map(exact,cert['complete_Jw']));domain=list(map(exact,cert['physical_domains']))
    gate('complete_saved_array_lengths',len(radii)==len(image)==len(weights)==len(jw)==1200
         and len(cert['complete_selfmap_gates'])==len(cert['complete_distance_gates'])==1200
         and len(domain)==25)
    selfrat,dist=[],[]
    for i,(rr,ii,ww,dd) in enumerate(zip(radii,image,weights,jw)):
        gate(f'positive_radius_and_weight_{i}',rr>0 and ww>0)
        gate(f'nonnegative_complete_image_and_Jw_{i}',ii>=0 and dd>=0)
        gate(f'actual_strict_selfmap_{i}',ii<rr and cert['complete_selfmap_gates'][i] is True)
        gate(f'actual_distance_below_one_half_{i}',2*dd<ww and cert['complete_distance_gates'][i] is True)
        selfrat.append(ii/rr);dist.append(dd/ww)
    gate('recorded_maximum_distance_is_outward',max(dist)<=exact(cert['maximum_weighted_distance_upper'])<F(1,2)
         and cert['contraction_target_rational']==[1,2])
    V=[exact(row['V_max']) for row in joint['rows']]
    B=exact(joint['physical_high_conversion']);Rmax=exact(joint['profile_physical_upper'])
    factor=[Rmax if j==21 else B if j==5 else V[j] for j in range(25)]
    true_domains=[]
    for j in range(25):
        value=(10+sum(u[j],F(0))+r[j])*V[j]+factor[j]*h[j]
        true_domains.append(value)
        gate(f'complete_physical_domain_outward_{j}',value<=domain[j]<F(2)**-34)
    low_physical=sum((V[j]*sum(u[j],F(0)) for j in range(25)),F(0))
    finite_physical=sum((V[j]*r[j] for j in range(25)),F(0))
    high_physical=sum((factor[j]*h[j] for j in range(25)),F(0))
    total=low_physical+finite_physical+high_physical
    gate('complete_physical_perturbation_sum_below_two_minus39',0<total<F(2)**-39)
    imax=max(range(1200),key=selfrat.__getitem__);dmax=max(range(1200),key=dist.__getitem__)
    output=dict(schema='full1200-saved-exact-independent-consumer-v1',scope=__doc__,
        all_gates=all(gates.values()),gates=gates,exact_comparisons=comparisons,
        source_sha256=sha(__file__),pinned_certificate_sha256=sha(a.certificate),
        original_producer_sha256=sha(a.producer),original_resource_sha256=sha(a.resource),
        input_sha256=ids,complete_selfmap_rows=1200,complete_distance_rows=1200,complete_physical_domain_rows=25,
        largest_selfmap_row=imax,largest_selfmap_ratio=rec(selfrat[imax]),
        relative_selfmap_margin=rec(1-selfrat[imax]),
        largest_distance_row=dmax,largest_distance_ratio=rec(dist[dmax]),
        largest_saved_physical_domain=rec(max(domain)),largest_reconstructed_physical_domain=rec(max(true_domains)),
        physical_perturbation=dict(low_block_sum=rec(low_physical),finite_block_sum=rec(finite_physical),
            high_block_sum=rec(high_physical),complete_sum=rec(total),target=rec(F(2)**-39),
            scope='Conservative sum over all25 original blocks of already radial-sup-first physical strong mode masses; neither pointwise sup nor a new geometric position/reach bound.'),
        original_scope='Uniform complex R100 six unit axes times T weighted-l1 radius1/32; outer10/11 full-frequency mixed-boundary field, with parameter cut still independent.',
        original_float_proposal_rerun=False,original_source_images_recomputed=False,
        ODE_near_kernel_or_Node_calls=0,parameter_cut_or_closed_surface_claimed=False,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(all_gates=output['all_gates'],exact_comparisons=comparisons,
        selfmap_row=imax,selfmap_ratio=float(selfrat[imax]),distance_row=dmax,distance_ratio=float(dist[dmax]),
        physical_perturbation=float(total),out=str(a.out),sha256=sha(a.out),
        elapsed_seconds=output['elapsed_seconds'],peak_rss_kib=output['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
