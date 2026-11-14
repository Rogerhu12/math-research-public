#!/usr/bin/env python3
"""Refine only the centre-residual Hessian source from completed quarter jets.

The original1341 trial norm rows remain unchanged.  Complete new moving
residuals use saved midpoint/whole target jets, never a target evaluator.
Joint bounds merge mode by mode over actual intersections; pointwise
maxima are used only for the ordinary L-infinity multiplication bounds.
"""
from __future__ import annotations
import argparse,gzip,json,os,shutil,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
import fourfold_codazzi_residual_split_cap_Hessian as prior
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_continuous_residual_v3 import (
    DirectedFFT,exact_candidate_series,target_model)
from fourfold_codazzi_moving_continuous_residual import moving_residual_polynomials
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_box import Box,CBox,zeros,reduce_box
from fourfold_codazzi_known_cut_direction_cap_pilot_v3 import (
    read,sha,positive,rec,exact,rowsha,smaller)

PUBLIC=prior.PUBLIC
KIND='actual_cached_quarter_centre_residual_same_w0_Hessian_inlet_recovery_v2'
QUARTER_SOURCE='54e5ec52033bb109618fde1c840730b4b589280382b2da196d3ea748af4490de'
QUARTER_WORKER='04d4380d840504f3aedf2da2d95f2112677819885f4a1e367480f97298b332db'
QUARTER_MANIFEST='6dc5bf2d8030d506c74dc29ef2cb3c1991cd5f7fb8c2a051b03b0ad89cb2fb69'
ORIGINAL_QUARTER_RUN=43623547711
ORIGINAL_PLAN='406e3e5331720a3f87f2b5f53c2e7d2988bea25b7537d650157ed97278e3073a'
RECOVERY_SOURCE='222b9a3dbfe842fbf8823d79584174cab5a350652db8a35cded0a610c45f6793'
RECOVERY_WORKER='cdaebcd03696c86249dc2cb0798a39fb4e4fabef92259af7ec3fcbe63c12a9e2'
RECOVERY_MANIFEST='b141f6d9be92cb86fc06b49933bfb005eb0de383eef5dd8bd91a6c347d8b1263'
SPLIT='85b6bbb899ab04549131fd20a7b16209056e2a51cb012bffbd7a6ae590b047c5'
SPLIT_SOURCE='a8b1a68d1be78b6288aa5e6db314caded7f80158045a4e7acb959c7e84c25317'
SPLIT_WORKER='0f5bb7c3c747a5e62ac52b40d17ee7dda398f044c30c6c723dccc4b8e7eb0b9b'
SPLIT_MANIFEST='a3b144b5a6e8c9d84c369f97aac1e849e3035bb7067c461ed574b53b1069d842'
INPUTS=prior.INPUTS+('candidate','split','split-process','quarter-plan','quarter-plan-process','quarter','quarter-process')
RANGES=((0,256),(256,512),(512,768),(768,1024),(1024,1280),(1280,1536),(1536,1792),(1792,1977))
LEFT,RIGHT=prior.LEFT,prior.RIGHT
CHANNELS=prior.CHANNELS
N,M,D=256,32,96


def save(path,value):
    raw=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    if str(path).endswith('.gz'):raw=gzip.compress(raw,mtime=0)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=Path(str(path)+'.partial')
    temporary.write_bytes(raw);os.replace(temporary,path)


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError(name)


def actual_quarter(p,run,phase,d,native):
    original=phase=='plan' or phase=='range' and d.get('range') not in ([0,256],[1792,1977])
    worker=QUARTER_WORKER if original else RECOVERY_WORKER
    manifest=QUARTER_MANIFEST if original else RECOVERY_MANIFEST
    source=QUARTER_SOURCE if original else RECOVERY_SOURCE
    kind='actual_complete_fixed_eta_quarter_cap_'+phase+('_v1' if original else '_inlet_recovery_v2')
    expected_run=ORIGINAL_QUARTER_RUN if original else run
    return (p.get('repository')==PUBLIC and str(p.get('run_id'))==str(expected_run)
        and p.get('phase')==phase and p.get('worker_source_sha256')==worker
        and p.get('input_manifest_sha256')==manifest
        and any(c.get('label')=='actual_complete_quarter_cap_'+phase
            and c.get('actual_returncode')==0 for c in p.get('children',[]))
        and any(e.get('sha256')==sha(native) and e.get('logical_file','').startswith('native/')
            for e in p.get('native_files',[]))
        and prior.proved(d) and d.get('source_sha256')==source and d.get('kind')==kind)


def inputs(a):
    out={k:sha(getattr(a,k.replace('-','_'))) for k in INPUTS}
    for key,values in (('range-native',a.range_natives),('range-process',a.range_processes)):
        out.update({key+'-'+str(i):sha(p) for i,p in enumerate(values)})
    return out


def validate(a,doc):
    local,background,particular,ordinary=prior.validate(a,doc)
    old,op=read(a.split),read(a.split_process)
    gate(doc,'actual_complete_residual_split_with_same1341_full_trial_rows',
        sha(a.split)==SPLIT and old.get('source_sha256')==SPLIT_SOURCE
        and prior.actual(op,43621690619,SPLIT_WORKER,SPLIT_MANIFEST,SPLIT,old)
        and old.get('complete_local_rows')==1341 and len(old.get('rows',[]))==1341
        and old.get('complete_actual_trial_intersections')==1977
        and old.get('direction_sha256')==ordinary['direction_sha256']
        and old.get('derived_continuous_centre_definition_sha256')==prior.CENTRE)
    plan,pp,full,fp=[read(p) for p in (a.quarter_plan,a.quarter_plan_process,a.quarter,a.quarter_process)]
    gate(doc,'actual_complete1977_quarter_plan_and_full_public_finish',
        sha(a.quarter_plan)==ORIGINAL_PLAN
        and actual_quarter(pp,ORIGINAL_QUARTER_RUN,'plan',plan,a.quarter_plan)
        and actual_quarter(fp,a.quarter_run,'finish',full,a.quarter)
        and full.get('plan_native_sha256')==sha(a.quarter_plan)
        and fp.get('actual_plan_native_sha256')==sha(a.quarter_plan)
        and full.get('complete_original_parent_cells')==1977
        and full.get('completed_new_quarter_domains')==7844 and full.get('complete_quarter_domains')==7908
        and plan.get('original_candidate_sha256')==prior.CURRENT
        and plan.get('derived_continuous_centre_definition_sha256')==prior.CENTRE
        and plan.get('direction_sha256')==ordinary['direction_sha256']
        and full.get('direction_sha256')==ordinary['direction_sha256']
        and plan.get('exact_affine_parameter_offset')=='0'
        and full.get('exact_affine_parameter_offset')=='0'
        and plan['input_sha256']['candidate']==sha(a.candidate)==prior.CURRENT)
    if len(a.range_natives)!=8 or len(a.range_processes)!=8:
        raise ValueError('all8 original completed quarter range artifacts are required')
    table={tuple(r['request']):r for r in plan['reused_quarter_rows']}
    if len(table)!=64:raise ValueError('all64 exact original quarters are required')
    original_receipts={tuple(r['range']):r for r in full['range_receipts']}
    seen=set()
    for npth,ppth in zip(a.range_natives,a.range_processes):
        r,p=read(npth),read(ppth);pair=tuple(r.get('range',[]))
        if pair not in RANGES or pair in seen:raise ValueError('one exact complete receipt per range is required')
        receipt=original_receipts[pair]
        gate(doc,'actual_completed_cached_target_quarter_range_'+str(pair),
            actual_quarter(p,receipt['actual_workflow_run'],'range',r,npth)
            and receipt['actual_workflow_run']==(int(fp['recovered_range_workflow_run']) if pair in ((0,256),(1792,1977)) else ORIGINAL_QUARTER_RUN)
            and receipt['source_sha256']==r.get('source_sha256')
            and receipt['actual_worker_sha256']==p.get('worker_source_sha256')
            and receipt['actual_manifest_sha256']==p.get('input_manifest_sha256')
            and sha(npth)==receipt['native_sha256'] and sha(ppth)==receipt['actual_original_process_sha256']
            and r.get('plan_native_sha256')==sha(a.quarter_plan)
            and r.get('direction_sha256')==ordinary['direction_sha256']
            and r.get('original_array_sha256')==plan['original_array_sha256'])
        assignment=next(x for x in plan['assignments'] if (x['first'],x['end'])==pair)
        if [x['request'] for x in r['rows']]!=assignment['actual_new_requests']:
            raise ValueError('the complete original quarter order differs')
        for cell in r['rows']:
            key=tuple(cell['request'])
            if (key in table or not cell.get('intrinsic_midpoint_jets')
                or not cell.get('all_original_target_coefficients')
                or cell.get('new_parameter_half_width')!='0'
                or not cell.get('complete_new_fixed_eta_coefficient_domain')):
                raise ValueError('a new complete quarter target cache differs or is missing')
            table[key]=cell
        seen.add(pair)
    keys=sorted(table)
    gate(doc,'all7908_original_quarters_once_and64_old_rows_are_byte_defined',
        seen==set(RANGES) and keys==[(i,4,j) for i in range(1977) for j in range(4)]
        and [rowsha(table[tuple(r['request'])]) for r in plan['reused_quarter_rows']]==plan['reused_quarter_row_sha256'])
    cells=[table[k] for k in keys];cursor=LEFT
    for cell in cells:
        left,right=map(Fraction,cell['interval']);i,_,j=cell['request']
        parent=plan['original_parent_rows'][i];pl,pr=map(Fraction,parent['interval'])
        if (left!=cursor or not left<right or left!=pl+(pr-pl)*Fraction(j,4)
            or right!=pl+(pr-pl)*Fraction(j+1,4)
            or cell['original_parent_row_sha256']!=rowsha(parent)):
            raise ValueError('the actual complete cached quarter cover changed')
        cursor=right
    if cursor!=RIGHT:raise ValueError('the true complete cap endpoint is missing')
    groups=[];at=0
    for i,r in enumerate(local['rows']):
        left,right=map(Fraction,r['interval']);cursor=left;intersections=[]
        while at<len(cells) and Fraction(cells[at]['interval'][1])<=left:at+=1
        k=at
        while k<len(cells) and Fraction(cells[k]['interval'][0])<right:
            ql,qr=map(Fraction,cells[k]['interval']);l,z=max(ql,left),min(qr,right)
            if l!=cursor or not l<z:raise ValueError('the actual intersections fail full local coverage')
            intersections.append(dict(request=cells[k]['request'],quarter_row_sha256=rowsha(cells[k]),
                actual_intersection=list(map(str,(l,z)))))
            cursor=z;k+=1
        if cursor!=right:raise ValueError('a complete original Hessian row is not covered')
        eligible=all('intrinsic_midpoint_jets' in table[tuple(x['request'])] for x in intersections)
        if old['rows'][i]['original_local_row_sha256']!=rowsha(r):
            raise ValueError('the original exact split Hessian row changed')
        groups.append(dict(local_source_row=i,interval=r['interval'],intersections=intersections,
            all_target_midpoints_saved=eligible))
    wanted=sorted({tuple(q['request']) for g in groups if g['all_target_midpoints_saved'] for q in g['intersections']})
    gate(doc,'every1341_row_has_actual_complete_intersections_or_keeps_its_original_full_bound',
        len(groups)==1341 and all(groups[i]['local_source_row']==i for i in range(1341)))
    data=load_candidate(a.candidate);meta=json.loads(str(data['metadata']))
    knots=[Fraction.from_float(float(x)) for x in data['radial_nodes']]
    alpha=Fraction.from_float(float(meta['amplitude']))
    gate(doc,'same_complete_raw32_candidate_exact_alpha_and_fixed_intrinsic_target',
        int(meta['modes'])==32 and knots[0]==0 and knots[-1]>=RIGHT
        and alpha==Fraction(6890507429876859,9007199254740992)
        and meta['object_sha256']=='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
        and plan['input_sha256']['candidate']==sha(a.candidate))
    return local,background,particular,ordinary,old,table,groups,wanted,data,knots,alpha


def residual_from_saved_cell(cell,data,knots,alpha,fft):
    left,right=map(Fraction,cell['interval']);piece=bisect_right(knots,left)-1
    germ=list(map(Fraction,cell['actual_scalar_germ']))
    if (piece!=cell['candidate_piece'] or not knots[piece]<=left<right<=knots[piece+1]
        or not germ[0]<=left<right<=germ[1]):
        raise ValueError('the same complete candidate polynomial and target germ are required')
    centre={k:box_from_record(v) for k,v in cell['intrinsic_midpoint_jets'].items()}
    whole={k:box_from_record(v) for k,v in cell['all_original_target_coefficients'].items()}
    fields,full,half=exact_candidate_series(data['piece_coefficients'][:,piece],knots[piece],left,right,M,N,fft)
    model={n:target_model(centre,whole,n,half) for n in ('gamma','beta','K','s')}
    ru,rv,_,_=moving_residual_polynomials(fields,model,alpha,full,M,N,fft)
    polynomials=(ru,rv);length=max(len(p.coefficients) for p in polynomials)
    block=zeros((N,2*length))
    for component,p in enumerate(polynomials):
        for j,value in enumerate(p.coefficients):block[:,2*j+component]=CBox(value)
    coeff=fft.fft(block)/N
    modes=np.arange(N);modes=np.where(modes<N//2,modes,modes-N)
    outside=abs(modes)>D
    if not (np.all((coeff.real.lo[outside]<=0)&(coeff.real.hi[outside]>=0))
        and np.all((coeff.imag.lo[outside]<=0)&(coeff.imag.hi[outside]>=0))):
        raise ValueError('a mathematically absent full moving residual mode lost zero')
    coeff[outside]=0
    envelopes=[];errors=[];A0=[];A1=[]
    order=np.array([j%N for j in range(-D,D+1)])
    for component,p in enumerate(polynomials):
        z=coeff[:,component::2]
        envelope=reduce_box(Box(z.magnitude_upper()).transpose()).transpose()
        values=np.asarray(envelope.hi[order],dtype=float)
        if np.any(values<0) or not np.isfinite(values).all():
            raise ValueError('finite complete mode envelopes must be outward nonnegative numbers')
        # Each hexadecimal value is an exact binary64 upper endpoint of the
        # directed sum over every radial polynomial coefficient.
        envelopes.append([float(v).hex() for v in values])
        error=p.error.upper();errors.append(rec(error))
        A0.append(rec((sum((arb(float(v)) for v in values),arb(0))+error).upper()))
        A1.append(rec((sum((arb(float(v))*(1+4*abs(k)) for k,v in zip(range(-D,D+1),values)),arb(0))
            +385*error).upper()))
    return dict(request=cell['request'],interval=cell['interval'],candidate_piece=piece,
        actual_scalar_germ=cell['actual_scalar_germ'],quarter_row_sha256=rowsha(cell),
        complete_angular_support=96,complete_angular_grid=256,
        finite_coefficient_envelopes_binary64_hex=envelopes,
        complete_joint_uniform_error_A0=errors,raw_complete_A0=A0,raw_complete_A1=A1,
        exact_scalar_midpoint_and_whole_jets_reused=True,new_target_evaluations=0,
        full_even_residual_mean_retained=True)


def merged_residual(local_row,group,results,alpha,F0,F1):
    raw=[results[tuple(q['request'])] for q in group['intersections']]
    # A quarter crossing an original Hessian seam may bound both true
    # intersections; it is still computed only once and never extrapolated.
    factor=abs(exact(alpha));point0=[];point1=[];J0=[];J1=[];finite=[];error=[]
    for component in range(2):
        rows=[[float.fromhex(x) for x in r['finite_coefficient_envelopes_binary64_hex'][component]] for r in raw]
        maximum=np.max(np.asarray(rows),axis=0)
        E=sum((positive(r['complete_joint_uniform_error_A0'][component]) for r in raw),arb(0)).upper()
        finite0=sum((arb(float(v)) for v in maximum),arb(0))
        finite1=sum((arb(float(v))*(1+4*abs(k)) for k,v in zip(range(-D,D+1),maximum)),arb(0))
        point0.append(smaller(positive(local_row['physical_residual_A0'][component]),
            max((factor*positive(r['raw_complete_A0'][component])+F0).upper() for r in raw)))
        point1.append(smaller(positive(local_row['physical_residual_A1'][component]),
            max((factor*positive(r['raw_complete_A1'][component])+F1).upper() for r in raw)))
        J0.append((factor*(finite0+E)+193*F0).upper())
        J1.append((factor*(finite1+385*E)+193*F1).upper())
        finite.append([float(v).hex() for v in maximum]);error.append(rec(E))
    return point0,point1,J0,J1,dict(
        finite_modewise_maximum_binary64_hex=finite,raw_uniform_error_sum=error,
        complete_physical_pointwise_A0=[rec(x) for x in point0],
        complete_physical_pointwise_A1=[rec(x) for x in point1],
        complete_physical_joint_A0=[rec(x) for x in J0],
        complete_physical_joint_A1=[rec(x) for x in J1],
        maximum_of_pointwise_sums_not_used_as_joint_bound=True,
        physical_alpha_applied_once=str(alpha),complete_repair_complex_slots=193)


def composition(J0,J1,psi,old):
    exponential=(384*psi).exp().upper()
    choices=[old,(exponential*J0).upper()]
    c=((exponential-1)/384).upper()
    if 0<=c<=1:choices.append(((1-c)*J0+c*J1).upper())
    value=choices[0]
    for other in choices[1:]:value=smaller(value,other)
    return value


def hessian_rows(local,background,particular,ordinary,old,groups,results,alpha):
    g={k:positive(v) for k,v in background['bounds'].items()}
    C,B,C1,B1,V,U,J,psi=[g[k] for k in (
        'physical_C_A_1over64','physical_B_A_1over64','physical_C_theta_A_1over64',
        'physical_B_theta_A_1over64','physical_v_A_1over64','physical_U_A_1over64',
        'physical_to_moving_measure','actual_inverse_displacement_A_1over64')]
    F0=g['exact_repair_residual_difference_A0'];F1=g['exact_repair_residual_difference_A1']
    H2=positive(local['physical_reconstruction']['h2_from_xC'])
    HC=positive(local['physical_reconstruction']['h1_from_xC'])
    eh=(V*(1+g['corrected_mean_abs_upper']*C)/4).upper()
    gains={k:positive(v) for k,v in local['original_closed_physical_Green_gains'].items()}
    output=[]
    for i,(r,p,o,oldrow,group) in enumerate(zip(local['rows'],particular['rows'],ordinary['rows'],old['rows'],groups)):
        original={k:positive(v) for k,v in oldrow['original_ordinary_sources'].items()}
        original_split={k:positive(v) for k,v in oldrow['new_four_sources'].items()}
        audit=None
        if group['all_target_midpoints_saved']:
            R0,R1,J0,J1,audit=merged_residual(r,group,results,alpha,F0,F1)
            RU,RV=R0;RU1,RV1=R1
            RUA=composition(J0[0],J1[0],psi,positive(oldrow['complete_joint_residual_audit']['U']['chosen_complete_joint_physical_residual']))
            RVA=composition(J0[1],J1[1],psi,positive(oldrow['complete_joint_residual_audit']['V']['chosen_complete_joint_physical_residual']))
            e=(arb.pi()*C*RV/8).upper();tB=(C*RU+B*C*RV).upper();tC=(C*C*RV).upper()
            tB1=(C1*RU+C*J*RU1+(B1*C+B*C1)*RV+B*C*J*RV1).upper()
            tC1=(2*C*C1*RV+C*C*J*RV1).upper()
            bracket=(C*C*RV/4+2*C*e).upper()
            ZBB=(tC*V).upper()
            ordinary_ZBC=(tC*HC+(C*tB+B*tC+tB1*C/4+B1*bracket)*H2).upper()
            ordinary_ZCC=((2*C*tC+tC1*C/4+C1*bracket)*H2).upper()
            split_ZBC=(tC*HC+(2*C*tB+B*tC+B1*bracket)*H2).upper()
            split_ZCC=((3*C*tC+C1*bracket)*H2).upper()
            b=positive(o['physical_B_L2r']);c=positive(o['physical_C_with_mean_L2r'])
            bt=positive(o['physical_B_theta_L2r']);ct=positive(o['physical_C_theta_L2r'])
            cm=positive(p['complete_physical_C_with_mean_module'])
            tight=dict(ordinary_B=(e*bt+ZBB*b+ordinary_ZBC*c).upper(),
                ordinary_C=(e*ct+ordinary_ZCC*c).upper(),divergence_B=arb(0),divergence_C=arb(0))
            split=dict(ordinary_B=(e*bt+ZBB*b+split_ZBC*c).upper(),
                ordinary_C=(e*ct+split_ZCC*c).upper(),
                divergence_B=((C*RUA+B*C*RVA)*eh*cm).upper(),
                divergence_C=(C*C*RVA*eh*cm).upper())
            audit.update(composed_joint_U=rec(RUA),composed_joint_V=rec(RVA),
                ordinary_zero_order=dict(ZBB=rec(ZBB),ZBC=rec(ordinary_ZBC),ZCC=rec(ordinary_ZCC)),
                split_zero_order=dict(ZBB=rec(ZBB),ZBC=rec(split_ZBC),ZCC=rec(split_ZCC)))
        else:
            tight=original;split=original_split
        options=[('original_ordinary',original),('original_split',original_split),
            ('tight_cached_quarter_ordinary',tight),('tight_cached_quarter_split',split)]
        score=lambda v:sum((v[k]*gains[column] for k,column in CHANNELS.items()),arb(0)).upper()
        name,chosen=options[0];value=score(chosen)
        for n,v in options[1:]:
            q=score(v)
            if q<value:name,chosen,value=n,v,q
        output.append(dict(local_source_row=i,interval=r['interval'],
            original_local_row_sha256=rowsha(r),original_ordinary_norm_row_sha256=rowsha(o),
            original_module_norm_row_sha256=rowsha(p),original_split_row_sha256=rowsha(oldrow),
            actual_complete_quarter_intersections=group['intersections'],
            all_target_midpoints_saved=group['all_target_midpoints_saved'],
            missing_midpoint_uses_original_full_row=not group['all_target_midpoints_saved'],
            merged_residual=audit,original_trial_subcells=o['original_trial_subcells'],
            original_ordinary_sources={k:rec(v) for k,v in original.items()},
            original_split_sources={k:rec(v) for k,v in original_split.items()},
            new_ordinary_sources={k:rec(v) for k,v in tight.items()},
            new_split_sources={k:rec(v) for k,v in split.items()},
            selected_four_sources={k:rec(v) for k,v in chosen.items()},
            selected_complete_decomposition=name,selected_local_score=rec(value)))
    return output,gains


def run(a,doc):
    local,background,particular,ordinary,old,table,groups,wanted,data,knots,alpha=validate(a,doc)
    doc.update(requested_new_residual_domains=len(wanted),complete_cached_target_domains=7908,
        original_local_rows_with_complete_cached_midpoints=sum(g['all_target_midpoints_saved'] for g in groups),
        original_local_rows_retained_for_missing_midpoints=sum(not g['all_target_midpoints_saved'] for g in groups),
        original_target_evaluations_executed=0,original_physical_cap_residual_domains_recomputed=0,
        new_quarter_residual_rows=[],new_residual_domains_executed_in_this_child=0)
    if a.resume:
        previous=read(a.resume)
        if (previous.get('kind')!=KIND or previous.get('source_sha256')!=sha(__file__)
            or previous.get('input_sha256')!=doc['input_sha256']):
            raise ValueError('only exact same-input residual prefixes may resume')
        saved=previous.get('new_quarter_residual_rows',[])
        if len(saved)>len(wanted):raise ValueError('an original residual prefix exceeds the exact request')
        for request,row in zip(wanted,saved):
            if (tuple(row.get('request',[]))!=request or row.get('quarter_row_sha256')!=rowsha(table[request])
                or row.get('complete_angular_support')!=96 or row.get('new_target_evaluations')!=0):
                raise ValueError('a completed original cached-target residual cell changed')
        doc['new_quarter_residual_rows']=saved
        doc['original_prefix_sha256']=sha(a.resume)
        doc['original_completed_residual_domains_reused']=len(saved)
    fft=DirectedFFT()
    for request in wanted[len(doc['new_quarter_residual_rows']):]:
        tick=time.monotonic()
        row=residual_from_saved_cell(table[request],data,knots,alpha,fft)
        row['actual_seconds']=time.monotonic()-tick
        doc['new_quarter_residual_rows'].append(row);doc['new_residual_domains_executed_in_this_child']+=1
        n=len(doc['new_quarter_residual_rows'])
        if n%32==0:save(a.out,doc)
        print(json.dumps(dict(request=list(request),complete_residual_domains=n,total=len(wanted),
            actual_seconds=row['actual_seconds'],new_target_evaluations=0)),flush=True)
    gate(doc,'every_requested_new_centre_residual_domain_completed_without_any_target_call',
        [tuple(r['request']) for r in doc['new_quarter_residual_rows']]==wanted
        and all(r.get('full_even_residual_mean_retained') for r in doc['new_quarter_residual_rows']))
    results={tuple(r['request']):r for r in doc['new_quarter_residual_rows']}
    rows,gains=hessian_rows(local,background,particular,ordinary,old,groups,results,alpha)
    resolvent=positive(local['original_complete_bridge_resolvent']);all_bounds={}
    for name,key in (('original_ordinary','original_ordinary_sources'),('original_split','original_split_sources'),
        ('tight_ordinary','new_ordinary_sources'),('tight_split','new_split_sources'),('selected_local','selected_four_sources')):
        norm,bound=prior.accumulated(rows,key,gains)
        all_bounds[name]=dict(source_norms={k:rec(v) for k,v in norm.items()},
            physical_Green_Hessian_source=rec(bound),additive=rec((resolvent*bound).upper()))
    oldadd=positive(old['additive_same_w0_actual_moving_cap_error'])
    candidates=[oldadd]+[positive(v['additive']) for v in all_bounds.values()]
    chosen=candidates[0]
    for v in candidates[1:]:chosen=smaller(chosen,v)
    gate(doc,'all1341_original_full_trial_norm_rows_and1977_intersections_remain',
        len(rows)==1341 and sum(r['original_trial_subcells'] for r in rows)==1977)
    gate(doc,'joint_modewise_merge_and_whole_four_source_comparison_keep_all_means',
        all(v.is_finite() and v>=0 for v in candidates) and chosen<=oldadd
        and all(chosen<=v for v in candidates) and resolvent>=1)
    diagnostics=sorted(sorted(range(1341),key=lambda i:float(positive(rows[i]['selected_local_score'])),reverse=True)[:16])
    doc.update(complete=True,rows=rows,complete_local_rows=1341,complete_actual_trial_intersections=1977,
        complete_new_residual_domains=len(wanted),original_candidate_sha256=prior.CURRENT,
        derived_continuous_centre_definition_sha256=prior.CENTRE,
        direction_sha256=ordinary['direction_sha256'],exact_interval=[str(LEFT),str(RIGHT)],
        exact_affine_offset='0',physical_parameter='fixed physical eta0 and original nu',
        full_original_matrix_array_sha256=ordinary['full_original_matrix_array_sha256'],
        complete_source_decomposition_bounds=all_bounds,diagnostic_local_indices=diagnostics,
        original_complete_Hessian_feedback_resolvent=rec(resolvent),
        multiplier_of_same_w0_complete_physical_cap_error=rec(resolvent),
        previous_residual_split_additive=rec(oldadd),
        additive_same_w0_actual_moving_cap_error=rec(chosen),
        original_complete_Hessian_operator_or_unknown_error_norm_improved=False,
        complete_true_cut_source_claimed=False,complete_finite193_response_error_proved=False,
        complete_infinite_BVP_inverse_proved=False,full_independent_even_mean_retained=True,
        remaining_Z_minus_w0_still_uses_original_complete_moving_error_operator=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in INPUTS+('out',):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--range-natives',type=Path,nargs='+',required=True)
    p.add_argument('--range-processes',type=Path,nargs='+',required=True)
    p.add_argument('--quarter-run',type=int,required=True)
    p.add_argument('--resume',type=Path);a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=PUBLIC:
        raise RuntimeError('new mathematics runs only in this public repository Actions')
    if a.out.exists():raise FileExistsError('preserve each actual residual prefix')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256=inputs(a),actual_original_quarter_run=a.quarter_run)
    if a.resume:
        old=read(a.resume)
        if (old.get('kind')==KIND and old.get('source_sha256')==sha(__file__)
            and old.get('input_sha256')==doc['input_sha256'] and prior.proved(old)
            and old.get('complete_local_rows')==1341):
            a.out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.resume,a.out)
            print(json.dumps(dict(original_complete_native_reused=True,native_sha256=sha(a.out),
                new_target_evaluations=0,new_residual_domains_executed=0)),flush=True);return
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],gates=len(doc['gates']),
        new_residual_domains=doc['new_residual_domains_executed_in_this_child'],
        additive=doc['additive_same_w0_actual_moving_cap_error']['upper'],seconds=doc['seconds'])),flush=True)

if __name__=='__main__':main()
