#!/usr/bin/env python3
"""Actual one-leg density certificates and ordered global finite corrections.

This version uses the minimal even time DFT length and a freshly proved
larger TRUE field disk when available. The scalar sampler retains its
original small-disk primitive budget; only the analytic complement estimates
use the enlarged disk. A failed enlargement keeps the original certificate.
It reuses the proved ordinary/turn scalar sampler and full finite
reference. Every outer-domain failure is recorded rather than interpreted as
a zero. Complete field/density rectangles pay both infinite complements.
The local quadratic chronological integral may be omitted only with its
explicit finite coefficient norm bound; cross-segment terms are retained.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import time
import traceback
import numpy as np
from flint import arb,acb,acb_poly,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_actual_field_fourier_package import encode_complex,decode_complex,dyadic_pair,read_dyadic
from fourfold_phase_unified_scalar_time_circle import UnifiedScalarTimeCircleField,exact_time
from fourfold_phase_field_time_refined_root import prepare_refined_root
from fourfold_complete_reference_segment import CompleteReferenceSegment
from fourfold_complete_reference_real_time_q import real_time_q
from fourfold_retarget_reference_jets import RetargetReference
from fourfold_packaged_reference_bidisk import continuous_bidisk
from fourfold_phase_germ_cap_budget import leaf_budget
from fourfold_phase_real_time_cap_budget import real_time_reference_cap
from fourfold_phase_time_circle_field_package import combined_budget
from fourfold_actual_reference_density import density_budget,finite_field_modulus
from fourfold_exact_fourier_multipoint import time_coefficients
from fourfold_fourier_local_taylor import finite_taylor_evaluate
from fourfold_saved_circle_field_multidomain_budget import read,upper
import fourfold_expand_optimal_time_domain as time_extension
from fourfold_phase_domain_cover_verify import Closure


def checked_extended_domain(path, original_path, germ_index, closure=None):
    """Check the exact germ identity and every retained-coefficient input."""
    original=read(original_path)
    if closure is None:
        closure=Closure(Path.cwd(),original['target_object_sha256'],original['target_root_sha256'])
    closure.read(path,sha(path),'selected_germ_time_extension')
    domain=read(path)
    closure.check_sources(domain)
    if not domain.get('complete') or not domain.get('proved_selected_actual_germs'):
        raise ValueError('the selected actual larger-time germ is not proved')
    if (domain['source_sha256']!=sha(time_extension.__file__)
        or domain['original_domain_sha256']!=sha(original_path)
        or sha(domain['original_domain_path'])!=sha(original_path)):
        raise ValueError('expanded field has a different source or original domain')
    for key in ('target_object_sha256','target_root_sha256','retarget_descriptor_sha256',
                'exact_delta_fraction','leg','segment','branch_sign','normalized_subspan',
                'required_common_spans','time_grid_manifest_sha256'):
        if domain[key]!=original[key]:
            raise ValueError('expanded actual field identity differs: '+key)
    if (tuple(map(exact_time,domain['exact_time_endpoints']))!=
            tuple(map(exact_time,original['exact_time_endpoints']))
        or Fraction(domain['physical_theta_strip'])!=Fraction(original['physical_theta_strip'])
        or Fraction(domain['time_radius'])<=Fraction(original['time_radius'])):
        raise ValueError('expanded field does not retain the exact time/angle coordinates')
    for row in domain['germs']:
        if (not row.get('passed') or not lower(row['D_lower'])>0
            or not row.get('complete_new_angular_and_time_complements_paid')):
            raise ValueError('expanded field has an unpaid infinite complement')
        curvature=row['curvature']
        bound='Q_real_lower' if curvature['kind']=='root_deflated_Q' else 'minus_K_real_lower'
        if not lower(curvature[bound])>0:
            raise ValueError('expanded selected germ has no actual curvature branch')
        provenance=row['retained_coefficient_provenance']
        closure.domain(provenance['path'],provenance['sha256'])
        for link in provenance['links']:
            closure.domain(link['child_path'],link['child_sha256'])
            closure.domain(link['parent_path'],link['parent_sha256'])
    indices=[int(row['original_germ_index']) for row in domain['germs']]
    if (indices!=domain['selected_germ_indices'] or len(set(indices))!=len(indices)
        or any(j<0 or j>=len(original['germs']) for j in indices)):
        raise ValueError('selected true-germ index list differs from the original cover')
    selected=[row for row in domain['germs'] if row['original_germ_index']==germ_index]
    if len(selected)!=1:
        raise ValueError('the expanded domain does not cover the sampled main germ')
    chosen=selected[0]
    if tuple(map(Fraction,chosen['common_span']))!=tuple(map(Fraction,original['germs'][germ_index]['common_span'])):
        raise ValueError('expanded field selected another true scalar germ')
    return domain,chosen


def extended_field_domains(model, domain_path, args, report, germ_index):
    """Attempt a genuine larger disk without changing the point sampler."""
    domains=[(model.outer,model.modulus)]
    directory=getattr(args,'expanded_domain_directory',None)
    if directory is None:
        return domains
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    digest=sha(domain_path)
    out=directory/('forward_%04d_%s_main%d_optimal_R6_S12.json.gz'%
                   (model.domain['segment'],digest[:12],germ_index))
    if not out.exists():
        original_precision=ctx.prec
        try:
            time_extension.expand_domain(domain_path,out,R=6,S=12,
                descriptor=args.descriptor,nodes=args.primitive_nodes,bits=args.bits,
                radial_degree=args.radial_degree,models={germ_index:model},
                germ_indices=[germ_index],curvature_outer=8)
        finally:
            ctx.prec=original_precision
    enlarged=read(out)
    record=dict(path=str(out),sha256=sha(out),
        proved=bool(enlarged.get('proved_selected_actual_germs')),
        original_sampler_domain_sha256=digest,
        original_sampler_budget_unchanged=True,
        only_sampled_main_germ_is_expanded=True,
        all_other_real_germs_paid_by_original_complete_crossing_caps=True)
    report['expanded_true_field_domain']=record
    if not record['proved']:
        record['failures']=[r.get('failure','denominator or curvature gate failed')
                            for r in enlarged.get('germs',[]) if not r.get('passed')]
        return domains
    enlarged,row=checked_extended_domain(out,domain_path,germ_index)
    domains.append((exact_arb(Fraction(enlarged['time_radius'])),upper(row['true_field_moduli']['f'])))
    record['selected_germ_index']=germ_index
    record['all_true_time_domains']=[dict(radius=ball_record(R),modulus=ball_record(M))
                                     for R,M in domains]
    return domains


def save(path,data):
    path=Path(path);raw=(json.dumps(data,indent=2)+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    elif len(raw)>1_000_000:raise ValueError('large report needs gzip')
    if len(raw)>5_000_000:raise ValueError('report must be split below 5MB')
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.writing');temporary.write_bytes(raw);temporary.replace(path)


def dyadic_midpoint(value,bits):
    """Round the exact high-precision midpoint relatively, never node values."""
    m,e=value.mid().man_exp();m,e=int(m),int(e)
    shift=max(0,abs(m).bit_length()-bits)
    if shift:m,e=m>>shift,e+shift
    return arb((m,e))


def circle_time_coefficients(sampler,N,Nt,m,rho,callback):
    if Nt<2 or Nt%2 or not 0<m<=Nt:raise ValueError('invalid time DFT dimensions')
    values=np.empty((Nt,N),object);timings=[]
    for j in range(Nt//2+1):
        u=acb(rho) if j==0 else (acb(-rho) if j==Nt//2
           else rho*acb(0,2*arb.pi()*j/Nt).exp())
        vals,timing=sampler(u,N)
        if len(vals)!=N or any(not z.is_finite() for z in vals):
            raise ValueError('invalid true sampled function')
        values[j]=vals
        if 0<j<Nt//2:values[Nt-j]=[z.conjugate() for z in vals]
        timing=dict(time_node=j,**timing);timings.append(timing);callback(timing)
    coefficients=np.empty((m,N),object)
    for j in range(N):
        transformed=acb.dft(list(values[:,j]))
        for i in range(m):coefficients[i,j]=transformed[i]/(Nt*rho**i)
    return coefficients,timings


def choose_fourier(time_nodes,K,coefficient_bits):
    """Exact real chosen Fourier polynomial with all coefficient fees."""
    m,N=time_nodes.shape
    if not 0<=K<N//2:raise ValueError('retained modes must be below Nyquist')
    coefficients=[];errors=[];fees=[]
    for i in range(m):
        real=[];mean=arb(0)
        for z in time_nodes[i]:
            if not z.imag.contains(0):raise ValueError('time-aliased coefficient lost reality')
            mean+=z.real.rad();real.append(acb(z.real.mid()))
        mean=(mean/N).upper();transformed=acb.dft(real)
        row=[];rounding=arb(0)
        for k in range(K+1):
            z=transformed[k]/N
            chosen=acb(dyadic_midpoint(z.real,coefficient_bits),
                       arb(0) if k==0 else dyadic_midpoint(z.imag,coefficient_bits))
            if k==0 and not z.imag.contains(0):raise ValueError('zero-mode reality failed')
            rounding=max(rounding,abs(z-chosen).upper());row.append(chosen)
        coefficients.append(row);errors.append((mean+rounding).upper())
        fees.append(dict(mean_time_coefficient_node_fee=ball_record(mean),
                         maximum_DFT_and_dyadic_choice_fee=ball_record(rounding)))
    return coefficients,errors,fees


def full_coefficients(rows):
    return np.array([[z.conjugate() for z in row[:0:-1]]+list(row) for row in rows],dtype=object)


def coefficient_digest(rows,frequency_scale):
    digest=hashlib.sha256()
    digest.update(('exact-positive-time-Fourier-v1;frequency=%s\n'%frequency_scale).encode())
    for row in rows:
        digest.update((json.dumps([encode_complex(z) for z in row],separators=(',',':'))+'\n').encode())
    return digest.hexdigest()


def preserve_rows(directory,rows,identity,frequency_scale):
    """Optional replay inputs; large reproducible rectangles may stay local."""
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    manifest=dict(kind='exact_positive_real_time_Fourier_rectangle',schema_version=1,
        identity=identity,frequency_scale=frequency_scale,time_terms=len(rows),
        Fourier_degree=len(rows[0])-1,complete=False,coefficient_sha256=coefficient_digest(rows,frequency_scale),
        negative_rule='negative frequency is conjugate of positive; zero frequency is real',shards=[])
    for first in range(0,len(rows),4):
        end=min(first+4,len(rows));name='coefficients_%03d_%03d.json.gz'%(first,end-1)
        payload=dict(time_start=first,time_stop=end,identity=identity,
            coefficients=[[encode_complex(z) for z in row] for row in rows[first:end]])
        save(directory/name,payload)
        manifest['shards'].append(dict(path=name,sha256=sha(directory/name),
            bytes=(directory/name).stat().st_size,time_start=first,time_stop=end))
        again=read(directory/name)
        for row,encoded in zip(rows[first:end],again['coefficients']):
            if any(z!=decode_complex(w) for z,w in zip(row,encoded)):
                raise ValueError('exact finite rectangle reload failed')
    manifest['complete']=True;manifest['exactly_reloaded']=True;save(directory/'manifest.json',manifest)
    return dict(path=str(directory/'manifest.json'),sha256=sha(directory/'manifest.json'),
                bytes=sum(r['bytes'] for r in manifest['shards']))


def next_power_two(n):return 1<<(n-1).bit_length()


def adaptive_layout(budget_function,*,N,K,Nt,m,target,max_degree=8191,max_terms=160):
    attempts=[]
    for step in range(100):
        result=budget_function(N,K,Nt,m,[arb(0)]*m)
        amounts={key:(upper(v) if isinstance(v,dict) else v.upper())
                 for key,v in result.items()}
        attempts.append(dict(N=N,K=K,Nt=Nt,m=m,total=ball_record(amounts['total'])))
        if amounts['total']<=target/4:return (N,K,Nt,m),attempts
        if 'fourier_tail' in amounts:
            angle=amounts['fourier_tail']+amounts['alias']
            time_tail=amounts['omitted_true_time_tail'];time_alias=amounts['time_circle_alias']
        else:
            angle=amounts['true_initial_label_Fourier_tail']+amounts['true_initial_label_Fourier_alias']
            time_tail=amounts['omitted_true_time_tail'];time_alias=amounts['folded_time_circle_alias']
        if angle>=max(time_tail,time_alias):
            if K<N//2-1:K=min(K+128,N//2-1)
            else:
                K+=128;N=next_power_two(2*K+1)
        elif time_tail>=time_alias:
            m+=8;Nt=max(Nt,2*((m+1)//2))
        else:Nt+=2
        if K>max_degree or m>max_terms or Nt>2*max_terms:
            raise ValueError('analytic rectangle cost guard exceeded; revise proved domains')
    raise ValueError('rectangle adaptation did not finish')


def coefficient_norms(rows,s):
    K=len(rows[0])-1;weights=[arb(1)]+[2*(k*s).exp() for k in range(1,K+1)]
    zeroth=[];first=[]
    for row in rows:
        zeroth.append(sum((abs(z)*w for z,w in zip(row,weights)),arb(0)).upper())
        first.append(sum((k*abs(z)*weights[k] for k,z in enumerate(row)),arb(0)).upper())
    return zeroth,first


def spatial_derivative_integrals(rows,outer,inner,error):
    """All finite modes and the full error on an intermediate angle strip.

    error is the integrated true-minus-finite SUP error on outer. A Cauchy
    derivative loss, not a same-width Wiener promotion, pays its derivatives.
    """
    width=(outer+inner)/2
    gap=outer-width
    if not 0<=inner<width<outer:
        raise ValueError('strict intermediate spatial strip required')
    weights=[arb(1)]+[2*(k*width).exp() for k in range(1,len(rows[0]))]
    by_order=[[],[],[]]
    for row in rows:
        values=[abs(z)*w for z,w in zip(row,weights)]
        for j in range(3):
            by_order[j].append(sum((k**j*v for k,v in enumerate(values)),arb(0)).upper())
    finite=[sum((2*v/(i+1) for i,v in enumerate(row)),arb(0)).upper() for row in by_order]
    fees=[error.upper(),(error/gap).upper(),(2*error/gap**2).upper()]
    return dict(finite_time_row_derivative_A_norms=[list(map(ball_record,row)) for row in by_order],
        finite_integrated_derivative_majorants=list(map(ball_record,finite)),
        true_error_integrated_derivative_sup_fees=list(map(ball_record,fees)),
        common_true_and_finite_integrated_spatial_majorants=[ball_record((a+b).upper()) for a,b in zip(finite,fees)],
        error_contract='integral of sup on the outer label strip; j!/(outer-inner)^j Cauchy derivative fee',
        all_finite_frequencies_retained=True,complete_caps_and_infinite_tails_in_error=True)


def compress_rectangle(rows,s,frequency_scale,allowance):
    """Drop finite coefficients only after paying their complete A_s norm.

    The time domain here is |u|<=1. No analytic infinite tail is estimated by
    these observed finite coefficients; that complement was already paid.
    """
    m,K=len(rows),len(rows[0])-1
    weights=[arb(1)]+[2*(frequency_scale*k*s).exp() for k in range(1,K+1)]
    original_digest=coefficient_digest(rows,frequency_scale)
    norm=[sum((abs(z)*w for z,w in zip(row,weights)),arb(0)).upper() for row in rows]
    fee_time=arb(0);kept_m=m
    while kept_m>1 and fee_time+norm[kept_m-1]<=allowance/2:
        fee_time=(fee_time+norm[kept_m-1]).upper();kept_m-=1
    mode_norms=[sum((abs(rows[i][k])*weights[k] for i in range(kept_m)),arb(0)).upper()
                for k in range(K+1)]
    fee_angle=arb(0);kept_K=K
    while kept_K>0 and fee_angle+mode_norms[kept_K]<=allowance/2:
        fee_angle=(fee_angle+mode_norms[kept_K]).upper();kept_K-=1
    selected=[row[:kept_K+1] for row in rows[:kept_m]]
    fee=(fee_time+fee_angle).upper()
    if not fee<=allowance:raise ValueError('complete finite compression fee exceeded allowance')
    return selected,fee,dict(original_time_terms=m,original_Fourier_degree=K,
        selected_time_terms=kept_m,selected_Fourier_degree=kept_K,
        original_coefficient_sha256=original_digest,
        selected_coefficient_sha256=coefficient_digest(selected,frequency_scale),
        frequency_scale=frequency_scale,working_strip=ball_record(s),time_radius='1',
        time_coefficient_tail_fee=ball_record(fee_time),angular_coefficient_tail_fee=ball_record(fee_angle),
        total_finite_compression_fee=ball_record(fee),
        complete_infinite_complements_are_separate=True)


def first_integral_and_local_second_bound(rows,sigma):
    """Keep the exact first integral; pay the entire omitted local J."""
    m=len(rows);K=len(rows[0])-1
    first=[sum((2*rows[i][k]/(i+1) for i in range(0,m,2)),acb(0)) for k in range(K+1)]
    norms,derivatives=coefficient_norms(rows,sigma)
    first_norm,first_derivative=coefficient_norms([first],sigma)
    # Even/even terms combine exactly into (G_end)' G_end/2. Odd/odd vanish.
    # Remaining chronological terms are the genuine antisymmetric brackets.
    bound=first_norm[0]*first_derivative[0]/2
    for even in range(0,m,2):
        for odd in range(1,m,2):
            weight=arb(2)/((even+odd+2)*(even+1))
            bound+=weight*(derivatives[odd]*norms[even]+derivatives[even]*norms[odd])
    return first,bound.upper()


def add_ordered_segment(C1,C2,G):
    """Keep every cross-segment frequency, with the old C1 on the right."""
    oldK,newK=len(C1)-1,len(G)-1;K=max(oldK,newK)
    left=[acb(0,k)*(G[abs(k)].conjugate() if k<0 else G[k]) for k in range(-newK,newK+1)]
    right=[C1[abs(k)].conjugate() if k<0 else C1[k] for k in range(-oldK,oldK+1)]
    product=acb_poly(left)*acb_poly(right);offset=oldK+newK
    newC2=[C2[k] if k<len(C2) else acb(0) for k in range(2*K+1)]
    for k in range(offset+1):newC2[k]+=product[offset+k]
    if not newC2[0].imag.contains(0):raise ValueError('quadratic mean lost reality')
    newC2[0]=acb(newC2[0].real)
    newC1=[(C1[k] if k<=oldK else acb(0))+(G[k] if k<=newK else acb(0)) for k in range(K+1)]
    return newC1,newC2


def encode_ball(z):
    return [[dyadic_pair(z.real.mid()),dyadic_pair(z.real.rad().upper())],
            [dyadic_pair(z.imag.mid()),dyadic_pair(z.imag.rad().upper())]]


def decode_ball(row):
    return acb(*[arb(read_dyadic(mid),read_dyadic(radius)) for mid,radius in row])


def save_accumulator(path,C1,C2,identity,summary):
    data=dict(kind='enclosed_complete_ordered_forward_accumulator',identity=identity,
        summary=summary,first=[encode_ball(z) for z in C1],second_cross=[encode_ball(z) for z in C2],
        local_second_integrals='omitted only with the full coefficient bounds in summary',
        every_cross_frequency_retained=True)
    save(path,data);loaded=read(path)
    for key,row in [('first',C1),('second_cross',C2)]:
        restored=[decode_ball(z) for z in loaded[key]]
        if any(not a.real.contains(b.real) or not a.imag.contains(b.imag) for a,b in zip(restored,row)):
            raise ValueError('accumulator reload does not enclose its original balls')
    return sha(path)


def lower(row):
    value=arb(row['lower']).lower()
    if not value.is_finite():raise ValueError('finite directed lower required')
    return value


def records(budget):
    return {key:ball_record(value) for key,value in budget.items()}


def exact_reference_times(reference):
    a,b=map(exact_time,reference.identity['exact_segment_time_rows'])
    return a+(b-a)*reference.left,a+(b-a)*reference.right


def real_reference_gates(reference,S,args):
    """Reuse only an identity-matched completed whole-segment gate."""
    path=args.real_gate_directory/f'{reference.leg}_{reference.segment:04d}.json.gz'
    if path.exists():
        data=read(path)
        expected=dict(reference.identity,normalized_subspan=['0','1'])
        if not data.get('complete') or data['identity']!=expected:
            raise ValueError('saved real-time gate belongs to a different reference')
        images=[g for g in data['image_gates'] if Fraction(g['initial_label_strip'])==S]
        qs=[g for g in data['q_gates'] if Fraction(g['initial_label_strip'])==S]
        if len(images)==len(qs)==1:
            return images[0],qs[0],dict(path=str(path),sha256=sha(path))
    return (reference.real_time_image(S,nodes=args.gate_nodes,p=args.gate_order),
            real_time_q(reference,S,nodes=args.gate_nodes,p=args.gate_order),None)


def run_leaf(domain_path,reference,args,output):
    start,cpu=time.monotonic(),time.process_time();doc=read(domain_path)
    sl,sr=map(Fraction,doc['normalized_subspan'])
    if doc['leg']!='forward':raise ValueError('this runner certifies the forward leg')
    ref=CompleteReferenceSegment(reference,'forward',int(doc['segment']),sl,sr)
    target=arb(args.target);S=Fraction(args.label_strip);sigma=Fraction(args.inner_strip)
    s,inner=exact_arb(S),exact_arb(sigma);rho=Fraction(args.circle_radius)
    if not 0<sigma<S or not target>0:raise ValueError('invalid nested label strips or error target')
    descriptor=reference.doc
    root_package=prepare_refined_root(Path(descriptor['target_object']['path']),
        Path(descriptor['target_root']['path']),nodes=args.root_nodes)
    cap=leaf_budget(doc,root_package.root)
    model=UnifiedScalarTimeCircleField(args.descriptor,domain_path,
        germ=cap['main_germ_index'],nodes=args.primitive_nodes,root_nodes=args.root_nodes,
        radial_degree=args.radial_degree)
    if (exact_reference_times(ref)!=model.time_endpoints
            or ref.identity['target_object_sha256']!=sha(model.object_path)
            or ref.identity['target_root_sha256']!=sha(model.root_path)
            or ref.identity['target_exact_delta_fraction']!=str(model.target.affine_delta)
            or ref.identity['branch_sign']!=model.sign):
        raise ValueError('actual field and exact reference object/time/branch mismatch')
    identity=dict(reference=ref.identity,field=model.identity(),
        exact_time_endpoints=[t.record() for t in model.time_endpoints])
    report=dict(kind='actual_forward_reference_density_leaf',complete=False,
        source_sha256=sha(__file__),identity=identity,domain_path=str(domain_path),
        domain_sha256=sha(domain_path),bits=args.bits,label_strip=str(S),inner_strip=str(sigma),
        target_uniform_density_error=args.target,coefficient_bits=args.coefficient_bits,
        time_circle_radius=str(rho),primitive_nodes=args.primitive_nodes,
        radial_degree=args.radial_degree,reference_outer_gates=[],samples=dict(field=[],density=[]),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_unified_scalar_time_circle.py','fourfold_complete_reference_segment.py',
            'fourfold_complete_reference_real_time_q.py','fourfold_phase_germ_cap_budget.py',
            'fourfold_phase_real_time_cap_budget.py','fourfold_expand_optimal_time_domain.py',
            'fourfold_saved_time_optimal_cauchy_extension.py','fourfold_ordinary_curvature_time_gate.py',
            'fourfold_expand_saved_time_domain.py','fourfold_saved_invariant_time_extension.py',
            'fourfold_phase_domain_cover_verify.py',
            'fourfold_packaged_reference_bidisk.py','fourfold_phase_time_circle_field_package.py',
            'fourfold_actual_reference_density.py','fourfold_fourier_local_taylor.py',
            'fourfold_boundary_fourier_budget.py','fourfold_exact_fourier_multipoint.py')})
    def checkpoint():save(output,report)
    def progress(stage,**kw):
        print(json.dumps(dict(segment=doc['segment'],subspan=doc['normalized_subspan'],stage=stage,**kw)),flush=True)
    checkpoint();progress('initializing',mode=model.mode)
    try:
        image_gate,q_gate,saved_gate=real_reference_gates(ref,S,args)
        if (not image_gate['complete_real_time_image_proved']
            or not q_gate['q_nonzero_on_complete_real_time_label_strip_proved']):
            raise ValueError('real-time reference image/q gate has not passed')
        image=upper(image_gate['physical_theta_image_strip']);qreal=lower(q_gate['full_real_time_q_real_lower'])
        if not qreal>0 or not image<model.strip:
            raise ValueError('actual real-time reference image leaves the true-field domain')
        # A float only proposes a rational enclosing strip; the directed gate
        # immediately below, not the float, certifies the inclusion.
        physical_strip=Fraction(math.ceil(float(image)*2**20)+2,2**20)
        ps=exact_arb(physical_strip)
        if not image<ps<model.strip:raise ValueError('no certified physical approximation margin')
        report['real_reference_gate']=dict(image=image_gate,q=q_gate,saved_gate=saved_gate,
            physical_approximation_strip=str(physical_strip))
        # Fixed-theta matching is bounded before substitution. Only the REAL
        # cap image is needed; no larger complex-time Y image is assumed.
        actual_caps=real_time_reference_cap(model,ref,image_gate,q_gate)
        integrated_cap=upper(actual_caps['integrated_density_cap_error_upper'])
        uniform_cap=upper(actual_caps['uniform_density_cap_error_upper'])
        report['true_crossing_caps']=actual_caps
        checkpoint()
        for text in args.outer_domains.split(','):
            rt,st=text.split(':');R,T=Fraction(rt),Fraction(st)
            gate=continuous_bidisk(ref,time_radius=R,label_width=T,
                                  nodes=args.gate_nodes,taylor_order=args.gate_order)
            report['reference_outer_gates'].append(gate);checkpoint()
            progress('reference_outer_gate',time_radius=str(R),label_strip=str(T),
                q_lower=gate['full_complex_time_and_label_q_real_lower']['ball'],
                passed=gate['q_nonzero_on_complete_bidisk_proved'])
        accepted=[g for g in report['reference_outer_gates']
                  if g['q_nonzero_on_complete_bidisk_proved']
                  and Fraction(g['initial_label_strip'])>S
                  and Fraction(g['time_radius'])>max(Fraction(1),rho)]
        if not accepted:raise ValueError('no proved finite-proxy outer bidisk contains the working domain')
        field_domains=extended_field_domains(model,domain_path,args,report,cap['main_germ_index'])
        checkpoint()
        field_target=(target*qreal/(8*abs(model.h))).lower()
        def field_budget(N,K,Nt,m,errors):
            return combined_budget(N,K,model.strip,ps,1,errors,field_domains,rho,Nt,0)
        layout,attempts=adaptive_layout(field_budget,N=max(512,args.primitive_nodes),
            K=64,Nt=16,m=12,target=field_target,max_degree=args.max_degree,max_terms=args.max_terms)
        N,K,Nt,m=layout
        report['field_layout']=dict(nodes=N,degree=K,time_nodes=Nt,terms=m,adaptation=attempts,
                                    target_error=ball_record(field_target));checkpoint()
        progress('field_sampling',nodes=N,degree=K,time_nodes=Nt,terms=m)
        def field_sample(u,count):return model.sample(u,count)
        def field_progress(timing):
            report['samples']['field'].append(timing);checkpoint()
            if timing['time_node']%8==0:progress('field_node',node=timing['time_node'],of=Nt//2+1)
        time_nodes,timings=circle_time_coefficients(field_sample,N,Nt,m,exact_arb(rho),field_progress)
        rows,errors,fees=choose_fourier(time_nodes,K,args.coefficient_bits);del time_nodes
        actual=field_budget(N,K,Nt,m,errors)
        report['field_reconstruction_error_budget']=records(actual);report['field_coefficient_fees']=fees
        if not actual['total']<=field_target:
            raise ValueError('actual true field node/choice fees exceed the selected error target')
        compression_allowance=min(field_target/4,(field_target-actual['total']).lower()/2)
        if not compression_allowance>0:raise ValueError('no field compression allowance remains')
        rows,compression_fee,compression=compress_rectangle(rows,ps,4,compression_allowance)
        actual['finite_rectangle_compression']=compression_fee
        actual['total']=(actual['total']+compression_fee).upper()
        report['field_error_budget']=records(actual);report['field_compression']=compression
        report['field_coefficient_sha256']=coefficient_digest(rows,4)
        progress('field_compressed',terms=len(rows),degree=len(rows[0])-1,
                 fee=ball_record(compression_fee))
        field_identity=dict(identity=identity,definition='physical frequency 4',layout=report['field_layout'])
        if args.preserve_rectangles:
            report['field_exact_rectangle']=preserve_rows(output.parent/(output.name.split('.')[0]+'_field'),
                                                          rows,field_identity,4)
        field=full_coefficients(rows);del rows
        real_field_fee=(abs(model.h)*actual['total']/qreal).upper()
        report['true_field_transfer_uniform_error']=ball_record(real_field_fee);checkpoint()
        domains=[];report['finite_proxy_domains']=[]
        for gate in accepted:
            R,T=map(Fraction,(gate['time_radius'],gate['initial_label_strip']))
            MP=finite_field_modulus(field,exact_arb(R),upper(gate['physical_theta_image_strip']))
            Mg=((abs(ref.h)*MP+upper(gate['full_Yu_modulus']))/
                  lower(gate['full_complex_time_and_label_q_real_lower'])).upper()
            domains.append((exact_arb(R),exact_arb(T),Mg))
            report['finite_proxy_domains'].append(dict(time_radius=str(R),initial_label_strip=str(T),
                finite_field_modulus=ball_record(MP),finite_density_modulus=ball_record(Mg)))
        def proxy_budget(N,K,Nt,m,errors):
            return density_budget(domains,errors,N,K,exact_arb(rho),Nt,s)
        layout,attempts=adaptive_layout(proxy_budget,N=512,K=128,Nt=16,m=12,
            target=target/2,max_degree=args.max_degree,max_terms=args.max_terms)
        N,K,Nt,m=layout
        report['density_layout']=dict(nodes=N,degree=K,time_nodes=Nt,terms=m,adaptation=attempts)
        checkpoint();progress('density_sampling',nodes=N,degree=K,time_nodes=Nt,terms=m)
        def proxy_sample(u,count):
            tick,tickcpu=time.monotonic(),time.process_time()
            Y,Yu,Yx=ref.grid(u,count,Fraction(0))
            P,info=finite_taylor_evaluate(time_coefficients(field,u),Y,
                anchors=args.anchors,radius=Fraction(1,64),tail_target=args.evaluation_tail)
            result=[(ref.h*a-b)/q for a,b,q in zip(P,Yu,Yx)]
            return result,dict(finite_P_evaluation=info,
                maximum_node_density_modulus=ball_record(max(abs(z).upper() for z in result)),
                wall_seconds=time.monotonic()-tick,cpu_seconds=time.process_time()-tickcpu)
        def proxy_progress(timing):
            report['samples']['density'].append(timing);checkpoint()
            if timing['time_node']%8==0:progress('density_node',node=timing['time_node'],of=Nt//2+1)
        time_nodes,timings=circle_time_coefficients(proxy_sample,N,Nt,m,exact_arb(rho),proxy_progress)
        rows,errors,fees=choose_fourier(time_nodes,K,args.coefficient_bits);del time_nodes,field
        actual_proxy=proxy_budget(N,K,Nt,m,errors);proxy_error=upper(actual_proxy['total'])
        report['finite_density_reconstruction_error_budget']=actual_proxy;report['density_coefficient_fees']=fees
        if not proxy_error<=target/2:
            raise ValueError('actual finite proxy node/choice fees exceed the selected error target')
        compression_allowance=min(target/8,(target/2-proxy_error).lower()/2)
        if not compression_allowance>0:raise ValueError('no density compression allowance remains')
        rows,compression_fee,compression=compress_rectangle(rows,s,1,compression_allowance)
        proxy_error=(proxy_error+compression_fee).upper()
        actual_proxy=dict(actual_proxy,finite_rectangle_compression=ball_record(compression_fee),
                          total=ball_record(proxy_error))
        report['finite_density_error_budget']=actual_proxy;report['density_compression']=compression
        report['density_coefficient_sha256']=coefficient_digest(rows,1)
        progress('density_compressed',terms=len(rows),degree=len(rows[0])-1,
                 fee=ball_record(compression_fee))
        if args.preserve_rectangles:
            report['density_exact_rectangle']=preserve_rows(output.parent/(output.name.split('.')[0]+'_density'),
                rows,dict(identity=identity,layout=report['density_layout']),1)
        base_error=(real_field_fee+proxy_error).upper()
        E=(2*base_error+integrated_cap).upper()
        norms,derivatives=coefficient_norms(rows,s)
        finite_A=sum((2*v/(i+1) for i,v in enumerate(norms)),arb(0)).upper()
        finite_sup=sum(norms,arb(0)).upper();A=(finite_A+E).upper()
        first,local_J=first_integral_and_local_second_bound(rows,inner)
        spatial=spatial_derivative_integrals(rows,s,inner,E)
        spatial.update(outer_label_strip=str(S),spatial_derivative_strip=str((S+sigma)/2),
                       flow_inner_strip=str(sigma),
                       available_flow_displacement_margin=str((S-sigma)/2))
        report['R86_spatial_inputs']=spatial
        del rows
        report['R72_inputs']=dict(
            integrated_approximation_error_E=ball_record(E),common_integrated_majorant_A=ball_record(A),
            common_uniform_majorant=ball_record((finite_sup+base_error+uniform_cap).upper()),
            finite_integrated_majorant=ball_record(finite_A),finite_uniform_majorant=ball_record(finite_sup),
            finite_time_coefficient_A_norms=list(map(ball_record,norms)),
            omitted_local_second_integral_bound_on_inner_strip=ball_record(local_J),
            exact_first_integral_norm_on_inner_strip=ball_record(coefficient_norms([first],inner)[0][0]),
            signed_physical_time_halfwidth_already_included=True,
            every_frequency_of_the_first_integral_retained=True)
        first_path=output.with_name(output.name.removesuffix('.json.gz')+'_first.json.gz')
        first_doc=dict(kind='complete_enclosed_first_integral_of_exact_finite_density',
            identity=identity,density_coefficient_sha256=report['density_coefficient_sha256'],
            coefficients=[encode_ball(z) for z in first],
            definition='2*sum over even i of c[i,k]/(i+1); negative modes conjugate')
        save(first_path,first_doc)
        again=[decode_ball(z) for z in read(first_path)['coefficients']]
        if any(not a.real.contains(b.real) or not a.imag.contains(b.imag) for a,b in zip(again,first)):
            raise ValueError('first integral reload does not enclose the original')
        report['first_integral_file']=dict(path=str(first_path),sha256=sha(first_path),bytes=first_path.stat().st_size)
        report.update(complete=True,complete_continuous_true_density_proved=True,
            wall_seconds=time.monotonic()-start,cpu_seconds=time.process_time()-cpu,
            limitations=['Fixed actual parameter only; no parameter derivatives or KAM acceptance.',
                'This leaf alone is not the full forward flow or the squared principal return.',
                'The complete omitted local second integral is charged, not treated as zero.'])
        checkpoint();progress('complete',A=ball_record(A),E=ball_record(E),local_J=ball_record(local_J),
                              cpu_seconds=report['cpu_seconds'],wall_seconds=report['wall_seconds'])
        return report,first
    except Exception as exc:
        report['failure']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        report['wall_seconds']=time.monotonic()-start;report['cpu_seconds']=time.process_time()-cpu
        checkpoint();raise


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path('data/phase_ring_continuation')
    p.add_argument('--descriptor',type=Path,default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--domains',type=Path,nargs='+',required=True)
    p.add_argument('--out-directory',type=Path,required=True)
    p.add_argument('--real-gate-directory',type=Path,default=base/'step5_complete_reference_real_time_gates_forward')
    p.add_argument('--expanded-domain-directory',type=Path,default=base/'step5_expanded_time_domain_full')
    p.add_argument('--label-strip',default='1/256');p.add_argument('--inner-strip',default='3/1024')
    p.add_argument('--target',default='1e-20');p.add_argument('--circle-radius',default='1')
    p.add_argument('--outer-domains',default='6:1/64,3:1/64,2:1/32,3/2:1/32')
    p.add_argument('--gate-nodes',type=int,default=512);p.add_argument('--gate-order',type=int,default=8)
    p.add_argument('--primitive-nodes',type=int,default=1024);p.add_argument('--root-nodes',type=int,default=1024)
    p.add_argument('--radial-degree',type=int,default=96);p.add_argument('--bits',type=int,default=320)
    p.add_argument('--coefficient-bits',type=int,default=128)
    p.add_argument('--max-degree',type=int,default=8191);p.add_argument('--max-terms',type=int,default=160)
    p.add_argument('--anchors',type=int,default=512);p.add_argument('--evaluation-tail',default='1e-36')
    p.add_argument('--preserve-rectangles',action='store_true');p.add_argument('--resume',action='store_true')
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=24
    reference=RetargetReference(args.descriptor);args.out_directory.mkdir(parents=True,exist_ok=True)
    C1,C2=[acb(0)],[acb(0)];A,E,local_J=arb(0),arb(0),arb(0);last_time=None
    index=dict(kind='actual_forward_density_ordered_finite_correction',complete=False,
        source_sha256=sha(__file__),descriptor_sha256=sha(args.descriptor),label_strip=args.label_strip,
        inner_strip=args.inner_strip,requested_domains=list(map(str,args.domains)),leaves=[])
    index_path=args.out_directory/'index.json';save(index_path,index)
    for number,path in enumerate(args.domains):
        doc=read(path);sl,sr=map(Fraction,doc['normalized_subspan'])
        suffix=hashlib.sha256((str(sl)+':'+str(sr)).encode()).hexdigest()[:10]
        output=args.out_directory/f'forward_{doc["segment"]:04d}_{suffix}.json.gz'
        endpoints=tuple(map(exact_time,doc['exact_time_endpoints']))
        if last_time is not None and last_time!=endpoints[0]:
            raise ValueError('requested domain leaves do not have exact chronological seams')
        if args.resume and output.exists() and read(output).get('complete'):
            report=read(output)
            current_ref=CompleteReferenceSegment(reference,'forward',int(doc['segment']),sl,sr)
            if (report['source_sha256']!=sha(__file__) or report['domain_sha256']!=sha(path)
                or report['label_strip']!=args.label_strip or report['inner_strip']!=args.inner_strip
                or report['identity']['reference']!=current_ref.identity
                or report['identity']['field']['descriptor_sha256']!=sha(args.descriptor)
                or not report.get('complete_continuous_true_density_proved')):
                raise ValueError('completed leaf belongs to different source/domain/reference/strips')
            for name,digest in report['dependency_sha256'].items():
                if sha(Path(__file__).with_name(name))!=digest:
                    raise ValueError('completed density dependency changed: '+name)
            row=report['first_integral_file']
            if sha(row['path'])!=row['sha256']:raise ValueError('saved first-integral hash differs')
            saved_first=read(row['path'])
            if (saved_first['identity']!=report['identity'] or
                saved_first['density_coefficient_sha256']!=report['density_coefficient_sha256']):
                raise ValueError('saved first integral belongs to a different exact density')
            first=[decode_ball(z) for z in saved_first['coefficients']]
        else:report,first=run_leaf(path,reference,args,output)
        inputs=report['R72_inputs'];A=(A+upper(inputs['common_integrated_majorant_A'])).upper()
        E=(E+upper(inputs['integrated_approximation_error_E'])).upper()
        local_J=(local_J+upper(inputs['omitted_local_second_integral_bound_on_inner_strip'])).upper()
        C1,C2=add_ordered_segment(C1,C2,first);last_time=endpoints[1]
        gap=exact_arb(Fraction(args.label_strip)-Fraction(args.inner_strip))
        summary=dict(A=ball_record(A),E=ball_record(E),omitted_local_J=ball_record(local_J),
            R=ball_record(gap),R72_smallness_passed=bool(A<=gap/2))
        if A<=gap/2:
            error=(E*(1+A/gap)+A**3/(2*(gap-A)**2)+local_J).upper()
            summary['true_coordinate_flow_error_with_all_local_J_paid']=ball_record(error)
        if number==0:index['exact_initial_time']=endpoints[0].record()
        index['exact_final_time']=endpoints[1].record()
        index['leaves'].append(dict(path=str(output),sha256=sha(output),bytes=output.stat().st_size,
            segment=doc['segment'],normalized_subspan=doc['normalized_subspan']))
        accumulator_path=args.out_directory/'ordered_accumulator.json.gz'
        accumulator_sha=save_accumulator(accumulator_path,C1,C2,dict(
            descriptor_sha256=sha(args.descriptor),leaves=index['leaves']),summary)
        index.update(summary=summary,accumulator_path=str(accumulator_path),accumulator_sha256=accumulator_sha,
            all_listed_seams_exact=True,whole_forward_leg=False)
        save(index_path,index)
    index['complete']=True
    if index['leaves']:
        start,stop=map(exact_time,(index['exact_initial_time'],index['exact_final_time']))
        from fourfold_phase_field_time_turn_collar import PiTime
        index['whole_forward_leg']=(start==PiTime(Fraction(0),Fraction(-1,2))
                                   and stop==PiTime(Fraction(0),Fraction(1,2)))
    save(index_path,index)


if __name__=='__main__':main()
