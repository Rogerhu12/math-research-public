#!/usr/bin/env python3
"""Actual relative real jets with same-label normalized derivative ranges.

All 550 original segments and eight exact Bernstein controls are evaluated
on closed angular cells.  Retarget and true errors are paid before positive
division.  Differences of F^(j)/F' are formed at the same original label,
so the result covers every pair of interior times, in either direction.
"""
from __future__ import annotations
import argparse,gzip,hashlib,io,json,math,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def up(x):return stored(x).upper()
def lo(x):return stored(x).lower()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--old-jets',type=Path,default=Path('notes/2026-11-13-R106-full-relative-real-ray-jets.json.gz'))
    ap.add_argument('--nodes',type=int,default=4096)
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or a.nodes<2 or a.nodes&(a.nodes-1) or a.bits<160:
        raise ValueError('fresh output, full power-of-two circle and directed precision required')
    ctx.prec=a.bits;tick=time.monotonic()
    old=checked(a.old_jets,'fourfold_actual_relative_ray_real_jets.py')
    gp=Path('notes/2026-11-12-step5-forward-reference-derivative-gate.json.gz')
    rp=Path('notes/2026-11-13-R106-integrated-source-ray-refinement.json')
    gate=read(gp);ray=read(rp)
    if old['inputs'].get(str(gp))!=sha(gp) or old['inputs'].get(str(rp))!=sha(rp):
        raise ValueError('the original full reference and true error changed')
    identity=gate['identity'];mp=Path(identity['manifest_path']);manifest=read(mp)
    if old['inputs'].get(str(mp))!=sha(mp) or identity['manifest_sha256']!=sha(mp):
        raise ValueError('the exact full Fourier reference changed')
    degree=int(manifest['Fourier_degree'])
    if (a.nodes<=2*degree or manifest['segment_count']!=550 or manifest['time_degree']!=7
        or manifest['time_basis']!='bernstein' or manifest['fields']!=['U','L']
        or len(gate['segments'])!=550):
        raise ValueError('all 550 exact continuous Fourier/Bernstein controls required')
    sf=exact_arb(Fraction(1,512))
    sr=exact_arb(Fraction(ray['proved_region']['label_strip']))
    error=exact_arb(Fraction(ray['bounds']['true_J_minus_reference_q']['exact'])).upper()
    Cprior=up(old['accepted_relative_first_derivative'])
    previous={z['order']:up(z['accepted_complete_relative_derivative'])
              for z in old['whole_time_relative_derivative_bounds']}
    half=arb.pi()/a.nodes
    lower=[None]*a.nodes;upper=[None]*a.nodes
    ratio_lower=[[None]*a.nodes for _ in range(3)]
    ratio_upper=[[None]*a.nodes for _ in range(3)]
    inputs={str(p):sha(p) for p in (a.old_jets,gp,rp,mp)}
    count=0;previous_end=None;last=tick;maximum_fee=[arb(0)]*4;segment_rows=[]
    print(dict(stage='full_true_inputs_checked',segments=550,nodes=a.nodes,orders=[1,2,3,4]),flush=True)
    for shard in manifest['shards']:
        path=mp.parent/shard['path'];payload=path.read_bytes()
        if hashlib.sha256(payload).hexdigest()!=shard['sha256'] or len(payload)!=shard['bytes']:
            raise ValueError('exact Fourier shard changed')
        inputs[str(path)]=shard['sha256']
        with np.load(io.BytesIO(gzip.decompress(payload))) as z:
            re=z['coefficient_real'];im=z['coefficient_imag'];meta=json.loads(str(z['metadata']))
        start=shard['start_segment'];number=shard['segment_count']
        if (start!=count or re.shape!=(number,8,2,degree+1) or re.shape!=im.shape
            or re.dtype!=np.dtype('float64') or im.dtype!=np.dtype('float64')
            or not np.all(np.isfinite(re)) or not np.all(np.isfinite(im))
            or np.any(im[...,0]!=0) or meta['start_segment']!=start
            or meta['segment_count']!=number
            or meta['exact_times']!=manifest['exact_time_endpoints'][start:start+number+1]):
            raise ValueError('complete original reference scalar definition changed')
        for local in range(number):
            index=start+local;oldrow=gate['segments'][index]
            if (oldrow['segment']!=index or oldrow['base_source']['sha256']!=shard['sha256']
                or oldrow['exact_times']!=manifest['exact_time_endpoints'][index:index+2]):
                raise ValueError('continuous gate uses a different Fourier reference')
            if previous_end is not None and (not np.array_equal(previous_end[0],re[local,0])
                    or not np.array_equal(previous_end[1],im[local,0])):
                raise ValueError('an exact original Bernstein seam is discontinuous')
            previous_end=re[local,-1].copy(),im[local,-1].copy()
            width=oldrow['widths']['1/512']
            if not width['positive_real_part_gate_proved']:raise ValueError('old complete gate failed')
            seglow=None;seghi=None;fees=[]
            for control in range(8):
                u=[acb(0)]+[acb(arb(float(re[local,control,0,k])),
                                   arb(float(im[local,control,0,k]))) for k in range(1,degree+1)]
                retarget=up(width['retarget_C1_fees'][control])
                values=[];fullfees=[]
                for j in range(1,5):
                    coeff=[acb(0) for _ in range(a.nodes)]
                    if j==1:coeff[0]=acb(1)
                    variation=arb(0)
                    for k in range(1,degree+1):
                        v=4*acb(0,k)**j*u[k]
                        coeff[k]=v;coeff[-k]=v.conjugate()
                        variation+=2*k*abs(v)*half
                    fee=(variation+4*math.factorial(j-1)*
                         (retarget/sf**(j-1)+error/sr**(j-1))).upper()
                    maximum_fee[j-1]=max(maximum_fee[j-1],fee)
                    fullfees.append(fee)
                    vals=acb.dft(coeff,inverse=True)
                    values.append(vals)
                fees.append([record(v) for v in fullfees])
                for node in range(a.nodes):
                    box=[]
                    for j in range(4):
                        v=values[j][node]*a.nodes
                        if not v.is_finite() or not v.imag.contains(0):
                            raise ValueError('complete real Fourier derivative lost reality')
                        box.append(v.real+arb(0,fullfees[j]))
                    m=box[0].lower();M=box[0].upper()
                    if not m>0:raise ValueError('true first derivative is not positive on a closed angular cell')
                    if lower[node] is None or m<lower[node]:lower[node]=m
                    if upper[node] is None or M>upper[node]:upper[node]=M
                    if seglow is None or m<seglow:seglow=m
                    if seghi is None or M>seghi:seghi=M
                    for j in range(3):
                        z=box[j+1]/box[0];zl=z.lower();zu=z.upper()
                        if ratio_lower[j][node] is None or zl<ratio_lower[j][node]:
                            ratio_lower[j][node]=zl
                        if ratio_upper[j][node] is None or zu>ratio_upper[j][node]:
                            ratio_upper[j][node]=zu
            segment_rows.append(dict(segment=index,exact_times=oldrow['exact_times'],
                full_normalized_first_derivative_lower=record(seglow),
                full_normalized_first_derivative_upper=record(seghi),
                all_eight_control_full_derivative_fees=fees))
            count+=1
            if time.monotonic()-last>20:
                print(dict(stage='same_label_full_jet_cells',segments=count,
                    seconds=time.monotonic()-tick),flush=True);last=time.monotonic()
    if count!=550:raise ValueError('incomplete actual time interval')
    final=[arb(0),Cprior,arb(0),arb(0),arb(0)]
    witnesses=[None]*5;cells=[]
    for node in range(a.nodes):
        m=lower[node];M=upper[node];C=min(Cprior,(M/m).upper())
        bounds=[max(abs(ratio_lower[j][node]),abs(ratio_upper[j][node])).upper()
                for j in range(3)]
        widths=[(ratio_upper[j][node]-ratio_lower[j][node]).upper() for j in range(3)]
        L,M3,_=bounds;d2,d3,d4=widths
        H2=(C*d2/m).upper()
        H3=(C*(d3+3*L*d2)/m**2).upper()
        H4=(C*(d4+6*L*d3+(15*L**2+4*M3)*d2)/m**3).upper()
        v=[arb(0),C,H2,H3,H4]
        for j in range(2,5):
            if v[j]>final[j]:final[j]=v[j];witnesses[j]=node
        cells.append(dict(node=node,normalized_Fprime_lower=record(m),
            normalized_Fprime_upper=record(M),relative_first_bound=record(C),
            normalized_derivative_ratio_ranges=[
                dict(order=j+2,lower=record(ratio_lower[j][node]),
                     upper=record(ratio_upper[j][node])) for j in range(3)],
            complete_relative_derivative_bounds=[record(v[j]) for j in range(2,5)]))
    accepted=[arb(0),Cprior]+[min(final[j],previous[j]).upper() for j in range(2,5)]
    rows=[dict(order=j,complete_same_label_log_jet_bound=record(final[j]),
        previous_complete_real_bound=record(previous[j]),
        accepted_complete_relative_derivative=record(accepted[j]),
        improvement_factor=record((previous[j]/accepted[j]).lower()),
        witness_cell=witnesses[j]) for j in range(2,5)]
    gates=[]
    def check(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    check('all original exact segments, controls and joins were consumed',count==550)
    check('positive division followed full closed-cell true fees',all(z>0 for z in lower))
    check('same-label derivative ranges improve at least the second derivative',final[2]<previous[2])
    out=dict(kind='actual_full_same_label_relative_real_log_jets_through_four',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,nodes=a.nodes,
        identity=old['identity'],inputs=inputs,native_geometry_recomputed=0,
        all_550_true_segments_and_4400_exact_controls=True,all_549_exact_seams_checked=True,
        entire_original_real_parameter_box=True,all_real_angles=True,
        all_pairs_of_strict_times_and_both_directions=True,
        normalized_flow='F_t=4*Y_t in the original common 2*pi label; H_(t,s)=F_t o F_s^-1',
        ratio_definition='M_j=F_t^(j)/F_t_prime, j=2,3,4; ranges keep the same original label for every t',
        exact_relative_second='Hpp=(Hprime/Fsprime)*(M2_t-M2_s)',
        exact_relative_third='Hppp=(Hprime/Fsprime^2)*(M3_t-M3_s-3*M2_s*(M2_t-M2_s))',
        exact_relative_fourth='H4=(Hprime/Fsprime^3)*(M4_t-M4_s-6*M2_s*(M3_t-M3_s)+(15*M2_s^2-4*M3_s)*(M2_t-M2_s))',
        complete_true_J_error=record(error),true_error_complex_strip=record(sr),
        complete_symbolic_retarget_strip=record(sf),
        maximum_complete_closed_cell_derivative_fees=[record(z) for z in maximum_fee],
        accepted_relative_first_derivative=record(Cprior),
        accepted_real_derivative_bounds=rows,
        original_complete_higher_jet_report=str(a.old_jets),
        unchanged_complex_derivative_and_strip_permission=True,
        no_bare_pullback_operator_difference_assumed=True,
        every_head_mean_source_and_reconstruction_position_unchanged=True,
        fixed_angular_weight_bound_proved=False,finite_head_feedback_solved=False,
        full_returned_remainder_claimed=False,
        cells=cells,segment_rows=segment_rows,gates=gates,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,rows=rows,out=str(a.out),sha256=sha(a.out),
        seconds=out['seconds']),flush=True)


if __name__=='__main__':main()

