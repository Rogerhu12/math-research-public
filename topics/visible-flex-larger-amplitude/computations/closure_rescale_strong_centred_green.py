#!/usr/bin/env python3
"""Rescale the complete q-centred low Green ledger to the actual strong M20.

R42 supplies a source-cell-constant transformation, so no new flow or radial
quadrature is used.  The complete actual twenty heights and all 46 column
directions remain present.  The physical norm is explicitly the OLD q
continuous strip with the new strong V.  It is not the originally saved
strong strip.  A fresh joint428 check remains necessary after this tool.

For corr, the old matrix was assembled using minima of whole-cell and
panel estimates.  We divide by a lower bound for the SMALLEST chosen old
canonical-rest constant among those providers.  This preserves both
branches of every old minimum, rather than silently using one provider.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx
from closure_real_head_source_enclosure import exact_q,ball_record
from closure_real_head_green_enclosure import load_json,ball,endpoint
from closure_assemble_centred_green import compact_upper


FAMILIES=('main','corr','base','remainder')


def sha(raw):return hashlib.sha256(raw).hexdigest()


def compact(x):
    m,e=map(int,x)
    return arb(m)*(arb(2)**e)


def same_interval(a,b):
    return endpoint(a['lower'])==endpoint(b['lower']) and endpoint(a['upper'])==endpoint(b['upper'])


def exact_endpoint(x):
    m=int(x['mantissa']);e=int(x['binary_exponent'])
    return Fraction(m*(1<<e),1) if e>=0 else Fraction(m,1<<(-e))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('low','columns','ordered','q-density','q-reference',
                 'strong-density','strong-reference','strong-box',
                 'strong-response','strong-low-far-lift','density','out-prefix'):
        p.add_argument('--'+name,type=Path,required=True)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    output=args.out_prefix.with_name(args.out_prefix.name+'.json.gz')
    summary_path=args.out_prefix.with_name(args.out_prefix.name+'-summary.json')
    if output.exists() or summary_path.exists():raise FileExistsError('Use a fresh strong output prefix')
    docs={};hashes={}
    for name in ('low','columns','ordered','q_density','q_reference',
                 'strong_density','strong_reference','strong_box',
                 'strong_response','strong_low_far_lift','density'):
        path=getattr(args,name);docs[name],raw=load_json(path);hashes[str(path)]=sha(raw)
    low=docs['low'];cols=docs['columns'];ordered=docs['ordered']
    qden=docs['q_density'];qref=docs['q_reference']
    sden=docs['strong_density'];sref=docs['strong_reference'];sbox=docs['strong_box']
    response=docs['strong_response'];slift=docs['strong_low_far_lift'];den=docs['density']
    cells=list(range(12,225));modes=list(range(2,93,2));N=len(cells)
    if low['cells']!=cells or low['modes']!=modes or not low['full_range_covered']:
        raise ValueError('The complete true q low46 matrices are required')
    if cols['modes']!=modes or sref['modes']!=modes or qref['modes']!=modes:
        raise ValueError('All46 actual chart directions must be retained')
    for name in ('columns','ordered','q_density','q_reference'):
        if hashes[str(getattr(args,name))] not in low['input_hashes'].values():
            raise ValueError('The old Green ledger uses different '+name)
    for name in ('q_density','strong_density','density','strong_box','strong_low_far_lift'):
        if not all(docs[name]['gates'].values()):raise ValueError('An input domain is unpaid: '+name)
    if not all(sref['checks'].values()) or not all(qref['checks'].values()):
        raise ValueError('The actual auxiliary reference has unpaid identity checks')
    if hashes[str(args.strong_response)] not in sref['input_hashes'].values():
        raise ValueError('The complete actual strong heights differ')
    for data in (sden,sbox,slift):
        if hashes[str(args.strong_reference)] not in data['input_hashes'].values():
            raise ValueError('The strong auxiliary envelope, correction and far lift differ')
    if hashes[str(args.strong_box)] not in slift['input_hashes'].values():
        raise ValueError('The strong auxiliary far lift belongs to another correction box')
    for name in ('q_density','strong_density'):
        if hashes[str(getattr(args,name))] not in den['input_hashes'].values():
            raise ValueError('The common-strip strong density lacks the two actual source envelopes')
    origin=den.get('continuous_strip_origin',{})
    if origin.get('path')!=str(args.q_density) or origin.get('sha256')!=hashes[str(args.q_density)]:
        raise ValueError('The entire continuous strip, not merely its endpoints, must be declared identical to q')
    for data,key in ((qden,'rows'),(sden,'rows'),(den,'rows'),(sbox,'rows'),
                     (qref,'cell_rows'),(sref,'cell_rows'),(low,'source_profiles')):
        if [r['cell'] for r in data[key]]!=cells:raise ValueError('The complete213 cell range is required')
    if low['far_strip']!=38 or low['far_physical_node']!=225:
        raise ValueError('The exact far normalization changed')
    if low['raw_D_constant']!=slift['raw_D_constant']:
        raise ValueError('The R18 raw nonlinear graph constant changed')
    common_fields=('B','Q_coefficient','mu_lower','mu_upper','normalized_width_upper','TV_log_w_upper','w_lower')
    sigma=[];shape_checks=[]
    for n,qr,sr,nr,qt,st in zip(cells,qden['rows'],sden['rows'],den['rows'],qref['cell_rows'],sref['cell_rows']):
        for name in common_fields:
            if not same_interval(qr[name],sr[name]) or not same_interval(qr[name],nr[name]):
                raise ValueError('Real material or common balance changed: '+str(n)+' '+name)
        for name in ('tau_inner','tau_outer'):
            if not same_interval(qr[name],nr[name]):raise ValueError('The NEW norm must use exactly the q continuous strip')
        if not same_interval(qt['tau'],st['tau']):raise ValueError('The auxiliary centre-wide strip differs')
        xq=ball(qr['canonical_total_envelope']);xs=ball(sr['canonical_total_envelope'])
        xn=ball(nr['canonical_total_envelope'])
        if any(r['canonical_total_envelope']['lower']!=r['canonical_total_envelope']['upper'] for r in (qr,sr,nr)) or not xq>0 or not xs>0:
            raise ValueError('Chosen Xbar coefficients must be exact positive dyadics')
        if not xn==xs:raise ValueError('The common-strip envelope is not the actual strong envelope')
        sigma.append(xs/xq)
        if not (exact_endpoint(nr['V_over_w_upper']['lower'])*
                exact_endpoint(qr['canonical_total_envelope']['lower']) >=
                exact_endpoint(sr['canonical_total_envelope']['upper'])*
                exact_endpoint(qr['V_over_w_upper']['upper'])):
            # Compare the chosen dyadics and the exact rational ratio,
            # rather than forcing another outward rounding of sigma.
            raise ValueError('New complete-mean material does not dominate the rescaled q upper')
        shape_checks.append(n)
    actual=response['response']['endpointCanonicalTrace']
    if actual['physicalNode']!=12 or len(actual['Q'])!=20:
        raise ValueError('This entry point requires the full actual M20 at physical node12')
    qcut={r['mode']:abs(ball(r['reference_Q'])) for r in cols['endpoint_rows']}
    scut={m:abs(exact_q(actual['Q'][m//2-1])).upper() if m<=40 else arb(0) for m in modes}
    if not qcut[2].lower()>0:raise ValueError('The actual old m2 amplitude contains zero')
    eta=(scut[2]/qcut[2].lower()).upper()
    # These denominator constants are the actual chosen positive source
    # profile bounds, not estimates of a possibly smaller unknown field.
    old_rest=[ball(r['canonical_rest']).lower() for r in low['source_profiles']]
    rest_provider=[dict(whole_cell=ball_record(v)) for v in old_rest]
    panel_hashes={};panel_cells=[]
    for path,wanted in low['panel_hashes'].items():
        doc,raw=load_json(Path(path));digest=sha(raw)
        if digest!=wanted:raise ValueError('A completed shallow panel provider changed')
        if doc['modes']!=modes:raise ValueError('A panel provider omits low modes')
        n=doc['cell'];k=n-12
        if not 12<=n<=23:raise ValueError('Unexpected shallow panel range')
        panel_cells.append(n)
        value=ball(doc['profiles']['canonical_rest']).lower()
        old_rest[k]=min(old_rest[k],value)
        rest_provider[k]['ordered_panel']=ball_record(value)
        panel_hashes[path]=digest
    if sorted(panel_cells)!=list(range(12,24)) or not all(v>0 for v in old_rest):
        raise ValueError('All12 positive old source-profile providers are required')
    refined={(r['mode'],c['cell']):c for r in ordered['mode_rows'] for c in r['refined_cells']}
    other=[arb(0) for _ in cells];main_mass=[arb(0) for _ in cells];group_hashes={}
    for group_ref in cols['column_groups']:
        group,raw=load_json(Path(group_ref['path']));digest=sha(raw)
        if digest!=group_ref['sha256']:raise ValueError('A complete actual column group changed')
        group_hashes[group_ref['path']]=digest
        if [r['cell'] for r in group['cell_rows']]!=cells:raise ValueError('A true column group omits cells')
        for j,m in enumerate(group['modes']):
            e=group['endpoint_rows'][j]
            lo=endpoint(e['Q_gain']['lower']);hi=endpoint(e['Q_gain']['upper'])
            if not(lo>0 or hi<0):raise ArithmeticError('The true height chart contains zero')
            gain=lo if lo>0 else -hi
            for k,row in enumerate(group['cell_rows']):
                linear=row['linear_rows'][j]
                q=ball(linear['column_Q_sup']).upper()/gain
                xi=ball(linear['column_Xi_sup']).upper()/gain
                cap=refined.get((m,row['cell']))
                if cap:
                    q=min(q.upper(),ball(cap['refined_phi_Q_sup']).upper())
                    xi=min(xi.upper(),ball(cap['refined_phi_Xi_sup']).upper())
                tau=ball(sref['cell_rows'][k]['tau']).upper()
                value=(scut[m]*((1+m)**3*q+(1+m)*xi)*(m*tau).exp()).upper()
                if m==2:main_mass[k]=value
                else:other[k]=(other[k]+value).upper()
    rest=[];source_factors={name:[] for name in FAMILIES};profiles=[]
    for k,n in enumerate(cells):
        correction=(ball(sbox['rows'][k]['correction_radius_multiple']).upper()*
                    ball(sref['cell_rows'][k]['reference_X']).upper()).upper()
        rest.append((other[k]+correction).upper())
        sig=sigma[k]
        source_factors['main'].append((sig*eta).upper())
        source_factors['corr'].append((sig*rest[k]/old_rest[k]).upper())
        source_factors['base'].append((sig*sig).upper())
        source_factors['remainder'].append((sig*sig*sig).upper())
        profiles.append(dict(cell=n,sigma=ball_record(sig),
            canonical_actual_m2=ball_record(main_mass[k]),
            canonical_other_linear_modes=ball_record(other[k]),
            canonical_auxiliary_correction=ball_record(correction),
            canonical_rest=ball_record(rest[k]),
            old_canonical_rest_denominator=ball_record(old_rest[k]),
            old_canonical_rest_providers=rest_provider[k],
            source_factors={name:ball_record(source_factors[name][k]) for name in FAMILIES},
            Xbar=den['rows'][k]['canonical_total_envelope'],
            Astar=den['rows'][k]['V_over_w_upper'],
            tau_inner=den['rows'][k]['tau_inner'],tau_outer=den['rows'][k]['tau_outer']))
    gamma={};far={}
    for name in FAMILIES:
        old=low['gamma_upper'][name];old_far=low['far_z_source_upper'][name]
        if len(old)!=N or any(len(r)!=N for r in old) or len(old_far)!=N:
            raise ValueError('The old complete four-family matrices are truncated')
        gamma[name]=[[compact_upper((compact(old[k][n])*source_factors[name][n]/sigma[k].lower()).upper())
                      for n in range(N)] for k in range(N)]
        far[name]=[compact_upper((compact(old_far[n])*source_factors[name][n]).upper()) for n in range(N)]
    rows=[]
    for k,n in enumerate(cells):
        old=low['rows'][k]
        r=dict(cell=n,r_inner=old['r_inner'],r_outer=old['r_outer'],
               B_low=ball_record((ball(old['B_low']).upper()/sigma[k].lower()).upper()),families={})
        for name in FAMILIES:
            values=[compact(v) for v in gamma[name][k]]
            largest=max(range(N),key=lambda i:values[i])
            r['families'][name]=dict(diagonal=ball_record(values[k]),
                row_sum=ball_record(sum(values,arb(0)).upper()),
                largest_source_cell=cells[largest],largest_entry=ball_record(values[largest]),
                mode_witness='The source-cell-constant rescaling preserves the complete all46 supremum; no individual modal witness was reconstructed.')
        rows.append(r)
    result=dict(status='Complete true low46 centred Green bounds rescaled to the actual strong M20 in the explicitly chosen q continuous strip; joint428 is a separate gate',
        cells=cells,modes=modes,full_range_covered=True,
        exact_panel_cells=low['exact_panel_cells'],whole_cell_cells=low['whole_cell_cells'],
        gamma_upper=gamma,far_z_source_upper=far,
        compact_number=low['compact_number'],family_meanings=low['family_meanings'],
        source_profiles=profiles,rows=rows,E_B_low=low['E_B_low'],
        far_scale_S=low['far_scale_S'],far_strip=38,far_physical_node=225,
        auxiliary_far_z_bound=slift['far_z_dyadic_bound'],raw_D_constant=slift['raw_D_constant'],
        rescaling=dict(rule='R42 theorem42.2',same_continuous_strip_as=str(args.q_density),
            old_strong_saved_strip_reused=False,actual_full_height_modes=20,
            remaining26_shallow_heights='Chosen zero; all46 deep parameters and all46 correction columns remain present.',
            eta_upper=ball_record(eta),sigma_min=ball_record(min(s.lower() for s in sigma)),
            sigma_max=ball_record(max(s.upper() for s in sigma)),
            corr_provider_rule='Use the minimum positive lower endpoint of each old chosen whole-cell/panel canonical-rest constant.',
            radial_integrations=0,linear_flow_solves=0,joint_gate_paid=False),
        input_hashes=hashes,panel_hashes=panel_hashes,group_hashes=group_hashes,
        source_hashes={name:sha(Path(__file__).with_name(name).read_bytes()) for name in
            (Path(__file__).name,'closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py','closure_assemble_centred_green.py')},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(payload)>=5_000_000:raise ArithmeticError('Repository individual-file cap exceeded')
    output.write_bytes(payload)
    summary={k:v for k,v in result.items() if k not in ('gamma_upper','source_profiles','rows')}
    summary.update(output=str(output),output_sha256=sha(payload),bytes=len(payload),
                   first_rows=rows[:3],all213_source_rest_positive=all(v>0 for v in rest))
    summary_path.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',output=str(output),output_sha256=sha(payload),bytes=len(payload),
                         seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
