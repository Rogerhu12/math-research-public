#!/usr/bin/env python3
"""All-time same-label Jacobian ratios of the already certified actual rays.

The complete finite Bernstein reference is enclosed on closed real angular
cells, with exact dyadic Fourier coefficients, a directed native DFT and a
full first-derivative cell fee. Existing complete retarget C1 fees and the
whole-parameter true-Jacobian error are then added, before any ratio.
No finite Q reference is identified with a true Jacobian.
"""
from __future__ import annotations
import argparse, gzip, hashlib, io, json, time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb, acb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read, save, sha, stored
from fourfold_negative_collar_root_fourier_budget import record


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--reference-gate',type=Path,default=Path(
        'notes/2026-11-12-step5-forward-reference-derivative-gate.json.gz'))
    ap.add_argument('--reference-summary',type=Path,default=Path(
        'notes/2026-11-12-step5-forward-reference-derivative-complete-summary.json'))
    ap.add_argument('--ray',type=Path,default=Path(
        'notes/2026-11-13-R106-integrated-source-ray-refinement.json'))
    ap.add_argument('--strict',type=Path,default=Path(
        'notes/2026-11-13-R46-215-cell-scaled-strong-operator.json'))
    ap.add_argument('--nodes',type=int,default=4096)
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or a.nodes<2 or a.nodes&(a.nodes-1) or a.bits<160:
        raise ValueError('new output, power-of-two nodes and directed precision required')
    ctx.prec=a.bits; tick=time.monotonic()
    gate=read(a.reference_gate);summary=read(a.reference_summary)
    ray=read(a.ray);strict=read(a.strict)
    if (not gate['complete'] or not gate['full_branch_nonzero_proved']
        or not summary['complete'] or summary['report_sha256']!=sha(a.reference_gate)
        or not ray['complete'] or not strict['complete'] or not strict['proved']):
        raise ValueError('all full old continuous certificates are required')
    identity=gate['identity']
    if identity['source_sha256']!=sha(Path(__file__).with_name('fourfold_reference_derivative_gate.py')):
        raise ValueError('finite reference derivative source changed')
    for name,digest in gate['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError('finite reference dependency changed: '+name)
    manifest_path=Path(identity['manifest_path']);manifest=read(manifest_path)
    descriptor_path=Path(identity['retarget_descriptor']);descriptor=read(descriptor_path)
    if (sha(manifest_path)!=identity['manifest_sha256']
        or sha(descriptor_path)!=identity['retarget_descriptor_sha256']):
        raise ValueError('exact reference identity changed')
    if (descriptor['target_object']['sha256']!=strict['identity']['object_sha256']
        or descriptor['target_exact_delta_fraction']!=strict['identity']['exact_center_parameter']
        or ray['proved_region']['parameter_center']!=strict['identity']['exact_center_parameter']
        or ray['proved_region']['parameter_half_width']!=strict['identity']['exact_parameter_half_width']):
        raise ValueError('actual family or whole parameter interval differs')
    if (manifest['time_basis']!='bernstein' or manifest['time_degree']!=7
        or manifest['fields']!=['U','L'] or manifest['segment_count']!=550
        or len(gate['segments'])!=550 or ray['proved_region']['segments']!=550
        or ray['proved_region']['time_endpoints']!=['-pi/2','pi/2']
        or a.nodes<=2*manifest['Fourier_degree']):
        raise ValueError('the complete same 550-segment Fourier/Bernstein cover is required')
    if [r['segment'] for r in gate['segments']]!=list(range(550)):
        raise ValueError('reference certificate has a segment gap')
    error=exact_arb(Fraction(ray['bounds']['true_J_minus_reference_q']['exact'])).upper()
    if not 0<error<arb(1)/300:
        raise ValueError('complete true Jacobian error does not fit this consumer')
    # Each angular cell is [x_n-pi/N,x_n+pi/N], modulo the full circle.
    half=arb.pi()/a.nodes
    lows=[None]*a.nodes; highs=[None]*a.nodes
    provenance={str(p):sha(p) for p in (a.reference_gate,a.reference_summary,a.ray,
                                      a.strict,manifest_path,descriptor_path)}
    accepted=[];previous_end=None;count=0;largest_cell_fee=arb(0)
    previous_progress=tick
    for shard in manifest['shards']:
        path=manifest_path.parent/shard['path'];payload=path.read_bytes()
        if hashlib.sha256(payload).hexdigest()!=shard['sha256'] or len(payload)!=shard['bytes']:
            raise ValueError('exact finite reference shard changed')
        provenance[str(path)]=shard['sha256']
        with np.load(io.BytesIO(gzip.decompress(payload))) as z:
            re=z['coefficient_real'];im=z['coefficient_imag'];meta=json.loads(str(z['metadata']))
        start=shard['start_segment'];number=shard['segment_count'];degree=manifest['Fourier_degree']
        if (start!=count or re.shape!=(number,8,2,degree+1) or re.shape!=im.shape
            or re.dtype!=np.dtype('float64') or im.dtype!=np.dtype('float64')
            or not np.all(np.isfinite(re)) or not np.all(np.isfinite(im))
            or np.any(im[...,0]!=0) or meta['start_segment']!=start
            or meta['segment_count']!=number
            or meta['exact_times']!=manifest['exact_time_endpoints'][start:start+number+1]):
            raise ValueError('reference shard scalar definition differs')
        for local in range(number):
            index=start+local;old=gate['segments'][index]
            if (old['base_source']['sha256']!=shard['sha256']
                or old['exact_times']!=manifest['exact_time_endpoints'][index:index+2]):
                raise ValueError('stored continuous gate belongs to a different segment')
            if previous_end is not None and (not np.array_equal(previous_end[0],re[local,0])
                    or not np.array_equal(previous_end[1],im[local,0])):
                raise ValueError('exact original reference seam is discontinuous')
            previous_end=(re[local,-1].copy(),im[local,-1].copy())
            old_width=old['widths']['1/512']
            if not old_width['positive_real_part_gate_proved']:
                raise ValueError('a full reference control gate failed')
            segment_fee=arb(0);segment_min=None;segment_max=None
            for control in range(8):
                coefficients=[acb(0) for _ in range(a.nodes)];coefficients[0]=acb(arb(1)/4)
                variation=arb(0)
                for k in range(1,degree+1):
                    u=acb(arb(float(re[local,control,0,k])),arb(float(im[local,control,0,k])))
                    q=acb(0,k)*u
                    coefficients[k]=q;coefficients[-k]=q.conjugate()
                    variation+=2*k*abs(q)*half
                finite_fee=variation.upper()
                retarget_fee=stored(old_width['retarget_C1_fees'][control]).upper()
                full_fee=(finite_fee+retarget_fee+error).upper()
                segment_fee=max(segment_fee,full_fee)
                values=acb.dft(coefficients,inverse=True)
                for node,val in enumerate(values):
                    val*=a.nodes
                    if not val.is_finite() or not val.imag.contains(0):
                        raise ValueError('complete exact real Fourier derivative lost reality')
                    lower=(val.real.lower()-full_fee).lower()
                    upper=(val.real.upper()+full_fee).upper()
                    if lows[node] is None or lower<lows[node]:lows[node]=lower
                    if highs[node] is None or upper>highs[node]:highs[node]=upper
                    if segment_min is None or lower<segment_min:segment_min=lower
                    if segment_max is None or upper>segment_max:segment_max=upper
            if not segment_min>0:
                raise ValueError('a true same-label real closed-cell lower bound is not positive')
            largest_cell_fee=max(largest_cell_fee,segment_fee)
            accepted.append(dict(segment=index,true_lower=record(segment_min),
                true_upper=record(segment_max),complete_cell_fee=record(segment_fee),
                exact_time_rows=old['exact_times']))
            count+=1
            if time.monotonic()-previous_progress>20:
                print(dict(segments=count,seconds=time.monotonic()-tick),flush=True)
                previous_progress=time.monotonic()
    if count!=550 or any(x is None for x in lows+highs):
        raise ValueError('complete circle/time cover missing')
    ratios=[(hi/lo).upper() for lo,hi in zip(lows,highs)]
    witness=max(range(a.nodes),key=lambda j:ratios[j]);C=ratios[witness]
    if not C>1 or not C<16:
        raise ValueError('requested improved full real relative-flow bound not obtained')
    cell_digest=hashlib.sha256()
    for lo,hi in zip(lows,highs):
        cell_digest.update((lo.str(60)+' '+hi.str(60)+'\n').encode())
    report=dict(kind='actual_complete_same_label_real_relative_ray_Jacobian',complete=True,proved=True,
        source_sha256=sha(__file__),bits=a.bits,nodes=a.nodes,identity=strict['identity'],
        full_time_interval=['-pi/2','pi/2'],entire_parameter_interval=True,
        normalized_label_period='2*pi',physical_angle_period='pi/2',
        all_550_true_segments_and_all_relative_times=True,
        full_real_relative_map_and_inverse_derivative=record(C),
        real_relative_derivative_lower=record((1/C).lower()),
        true_Jacobian_reference_error=record(error),
        complete_maximum_cell_fee=record(largest_cell_fee),
        common_true_label_derivative_lower=record(min(lows)),
        common_true_label_derivative_upper=record(max(highs)),
        ratio_witness=dict(node=witness,closed_cell_center='2*pi*node/nodes',
            true_lower=record(lows[witness]),true_upper=record(highs[witness]),ratio=record(C)),
        complete_cell_endpoint_digest_60_digits=cell_digest.hexdigest(),
        segment_rows=accepted,inputs=provenance,
        original_complex_relative_flow_bound_unchanged=strict['true_relative_flow_derivative_and_inverse'],
        original_complex_flow_strip_unchanged=strict['normalized_flow_strip'],
        real_and_complex_bounds_deliberately_distinct=True,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_reference_derivative_gate.py')},
        seconds=time.monotonic()-tick,
        scope='For every real physical relative characteristic and its inverse, at every pair of times of the same complete forward leg, all real angles and the entire current parameter interval. Exact reflection supplies the other characteristic branch. No larger complex strip or derivative bound is inferred.')
    save(a.out,report)
    print(dict(complete=True,relative_real_J=C.str(18),out=str(a.out),sha256=sha(a.out),seconds=report['seconds']),flush=True)


if __name__=='__main__':main()
