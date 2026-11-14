#!/usr/bin/env python3
"""Rebase the paid true low46 columns on a completed actual new-g node12 trace.

All saved actual low heights are retained.  No new radial integration is
needed: the real source, all 160 frozen shallow cell parameters, and all
mathematical model keys are checked against the certified column source.
The actual floating trace defines exact binary reference heights only; its
radial path or momentum is not thereby certified as an exact trajectory.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import resource
import time

from flint import arb,ctx
from closure_real_head_source_enclosure import exact_q,power2,ball_record
from closure_real_head_green_enclosure import load_json,ball,endpoint,maximum


MODEL_KEYS=['definition','sourceRevision','sourceHashes','start','deepAlpha',
    'exactSourceConstants','frozenWarpAlpha','headFingerprint']
GEOMETRY_KEYS=['rCut','wCut','width','curvatureBound','delta0','R','a','etaPower',
    'etaRatioAtN0','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell',
    'calibrationSteps','warpSteps','quadratureTolerance','slopeCap','capTransition',
    'capMode','cuspAwareQuadrature','valleyControls','rejoinR20At','rejoinIndexOffset',
    'pulseCaps','valleyCaps','flatOuterThroughCell','flatSlope','flatOuterStartSegment',
    'warpWeightLevels','rCuff','oldCut','epsilonScale','prefixRByCell','constructor']
DEFAULTS=dict(flatOuterThroughCell=None,flatSlope=None,flatOuterStartSegment=2,
    rejoinR20At=None,rejoinIndexOffset=4,pulseCaps=None,valleyCaps=None,warpWeightLevels=[])


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def point_record(x):
    m,e=x.man_exp()
    return dict(mantissa=str(m),binary_exponent=int(e))


def signed_range(lo,hi):
    return dict(lower=point_record(lo),upper=point_record(hi))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['columns','ready','new-ready','new-response','out']:
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--relative-radius',default='1/500')
    p.add_argument('--precision',type=int,default=192)
    args=p.parse_args();ctx.prec=args.precision;started=time.monotonic()
    data,draw=load_json(args.columns);ready,rraw=load_json(args.ready)
    actual_ready,nraw=load_json(args.new_ready);actual,araw=load_json(args.new_response)
    if data['modes']!=list(range(2,93,2)):
        raise ValueError('All 46 independent low columns are required')
    if data['start_physical_node']!=12 or data['far_physical_node']!=225:
        raise ValueError('This adapter uses exactly physical node12 to node225')
    if digest(rraw) not in data['input_hashes'].values():
        raise ValueError('The source ready does not belong to the paid columns')
    oldmodel=ready['rationalDeepModel'];newmodel=actual_ready['rationalDeepModel']
    differing=[key for key in MODEL_KEYS if oldmodel[key]!=newmodel[key]]
    if differing:
        raise ValueError('The actual trace belongs to a different mathematical model: '+','.join(differing))
    oldphys=oldmodel['physicalParameters'];newphys=newmodel['physicalParameters']
    differing=[key for key in GEOMETRY_KEYS
        if oldphys.get(key,DEFAULTS.get(key))!=newphys.get(key,DEFAULTS.get(key))]
    if differing:
        raise ValueError('Actual and certified source geometry differ: '+','.join(differing))
    oldcells=ready['shallowSourceParameters']['cells']
    newcells=actual_ready['shallowSourceParameters']['cells']
    if len(oldcells)!=160 or newcells!=oldcells:
        raise ValueError('The complete 160-cell frozen table is not identical')
    if actual.get('ready')!=actual_ready:
        raise ValueError('Response and its ready record differ')
    sol=actual['response'];cfg=actual['config'];req=actual['request']
    if not sol.get('converged') or not sol.get('checkpoint'):
        raise ValueError('A completed actual solve with its checkpoint is required')
    trace=sol['endpointCanonicalTrace'];M=cfg['modes']
    if trace['physicalNode']!=12 or cfg['depth']!=12 or cfg['linearFar']!=225:
        raise ValueError('Actual trace is not the scheduled depth12/far225 endpoint')
    if not 1<=M<=46 or len(req['height'])!=M or len(trace['Q'])!=M or len(trace['canonicalXi'])!=M:
        raise ValueError('The full actual Fourier height vector must be preserved')
    if cfg['spacing']!=2:
        raise ValueError('The real columns represent the physical even modes')
    if not all(math.isfinite(x) for x in trace['Q']+trace['canonicalXi']+req['height']):
        raise ValueError('The actual trace contains non-finite coordinates')
    rc=exact_q(oldphys['rCuff']);eps=exact_q(oldphys['epsilonScale'])/rc**7
    d0=exact_q(oldphys['delta0']);ln2=arb(2).log()
    cells=list(range(12,225));tau=[arb(2) if n<=17 else 1+arb(n-12)*ln2/4 for n in cells]
    amplitudes={};endpoint_rows=[]
    for k,row in enumerate(data['endpoint_rows']):
        m=row['mode'];lo=endpoint(row['Q_gain']['lower']);hi=endpoint(row['Q_gain']['upper'])
        if not (lo>0 or hi<0):
            raise ArithmeticError('The exact shallow height chart is not nonzero')
        gain_sign=1 if lo>0 else -1
        gl,gu=(lo,hi) if gain_sign>0 else (-hi,-lo)
        target=exact_q(trace['Q'][k]) if k<M else arb(0)
        alo=(abs(target).lower()/gu).lower();ahi=(abs(target).upper()/gl).upper()
        amp_sign=(1 if target>=0 else -1)*gain_sign
        amp_lo,amp_hi=(alo,ahi) if amp_sign>0 else (-ahi,-alo)
        amplitudes[m]=ahi
        slope=ball(row['raw_worker_slope'])
        defect=exact_q(trace['canonicalXi'][k])-target*slope if k<M else None
        endpoint_rows.append(dict(mode=m,reference_Q=ball_record(target),
            height_origin='actual new-g binary node12 height' if k<M else
                'chosen zero in the linear reference only; all correction heights remain free',
            required_far_Q=signed_range(amp_lo,amp_hi),Q_gain=row['Q_gain'],
            raw_worker_slope=row['raw_worker_slope'],
            numerical_endpoint_canonical_minus_linear=ball_record(defect) if defect is not None else None))
    X=[arb(0) for _ in cells];group_hashes={}
    for group_ref in data['column_groups']:
        path=Path(group_ref['path']);group,graw=load_json(path)
        if digest(graw)!=group_ref['sha256']:
            raise ValueError('A saved true column group has changed')
        if [r['cell'] for r in group['cell_rows']]!=cells:
            raise ValueError('The true column group does not cover all 213 cells')
        group_hashes[str(path)]=digest(graw)
        for k,row in enumerate(group['cell_rows']):
            for col in row['linear_rows']:
                m=col['mode'];amp=amplitudes[m]
                if amp:
                    X[k]+=(tau[k]*m).exp()*amp*((1+m)**3*ball(col['column_Q_sup']).upper()
                        +(1+m)*ball(col['column_Xi_sup']).upper())
    delta_far=d0*power2(-224)
    Sf=eps/rc**3*(arb(11)*delta_far.log()/2).exp()
    Z0=sum(((arb(38*m)).exp()*a for m,a in amplitudes.items()),arb(0))/Sf
    gap=38-tau[-1];loss=arb(0);worst_mode=None
    for m in data['modes']:
        value=(gap*m).exp()/(1+m)**3
        if value>loss:worst_mode=m
        loss=maximum(loss,value)
    radius=exact_q(Q(args.relative_radius));corrZ=radius*X[-1]*loss/Sf
    completeZ=(Z0+corrZ).upper();rows=[];max_ratio=arb(0)
    for n,t,x in zip(cells,tau,X):
        delta=d0*power2(-n)
        r23=power2(-23)*eps/rc**3*(arb(19)*delta.log()/4).exp()
        B=power2(12)*rc**3/eps*(-arb(19)*delta.log()/4).exp()
        H=power2(8)*rc**7/eps*(-arb(23)*delta.log()/4).exp()
        ratio=x/r23;max_ratio=maximum(max_ratio,ratio)
        rows.append(dict(cell=n,tau=ball_record(t),reference_X=ball_record(x),
            reference_log2_X=ball_record(x.log()/ln2),relative_to_R23_radius=ball_record(ratio),
            complete_R23_source_L1=ball_record(B*x*x),complete_R23_mean_increment=ball_record(H*x*x)))
    checks=dict(same_certified_mathematical_model=True,same_all160_shallow_cells=True,
        all_actual_low_heights_preserved=True,all46_columns_retained=True,
        all_corrected_R23_balls_paid=bool((1+radius)*max_ratio<1),
        target_far_ball_paid=bool(completeZ<power2(-2200)))
    result=dict(status='True linear reference rebased on all actual new-g node12 binary heights; no nonlinear correction or numerical-trajectory certification is asserted',
        checks=checks,modes=data['modes'],reference_modes=M,
        strip_formula='tau_n = max(2, 1 + (n-12)*log(2)/4); each whole cell uses its stated constant strip',
        target_far_strip=38,target_far_log2_ball=-2200,relative_correction_radius=str(Q(args.relative_radius)),
        reference_far_z_bound=ball_record(Z0),reference_far_log2_z=ball_record(Z0.log()/ln2),
        additional_strip_at_far=ball_record(gap),worst_far_conversion_mode=worst_mode,
        far_conversion_factor=ball_record(loss),full_46_correction_far_z_bound=ball_record(corrZ),
        full_46_correction_far_log2_z=ball_record(corrZ.log()/ln2),complete_far_z_bound=ball_record(completeZ),
        complete_far_log2_z=ball_record(completeZ.log()/ln2),
        reference_margin_bits=ball_record(-2200-Z0.log()/ln2),complete_margin_bits=ball_record(-2200-completeZ.log()/ln2),
        maximum_reference_R23_ratio=ball_record(max_ratio),cell_rows=rows,endpoint_rows=endpoint_rows,
        model_identity=dict(keys=MODEL_KEYS,geometry_keys=GEOMETRY_KEYS,frozen_cell_count=160,
            fingerprint=oldmodel['headFingerprint'],frozenWarpAlpha=oldmodel['frozenWarpAlpha']),
        input_hashes={str(args.columns):digest(draw),str(args.ready):digest(rraw),
            str(args.new_ready):digest(nraw),str(args.new_response):digest(araw),**group_hashes},
        source_hashes={name:digest(Path(__file__).with_name(name).read_bytes()) for name in
            ['closure_rebase_actual_reference.py','closure_real_head_green_enclosure.py','closure_real_head_source_enclosure.py']},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['The actual finite new-g endpoint is used only to define exact binary height data for a true linear reference.',
            'All M actual heights and all 46 possible correction heights are retained; zero reference coefficients above M are not nonlinear constraints.',
            'The source is compared by its full mathematical model and complete frozen shallow parameter table; source-integral and nominal-port radii are not identified.',
            'A nonlinear Green fixed point, high-frequency coupling, the outer 0..11 cells and the actual prefix must still be paid for this rebased reference.'])
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(checks=checks,reference_modes=M,reference_far_log2_z=str(Z0.log()/ln2),
        conditional_far_log2_z=str(completeZ.log()/ln2),max_R23_ratio=str(max_ratio),
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    if not all(checks.values()):
        raise SystemExit(1)


if __name__=='__main__':main()
