#!/usr/bin/env python3
"""Re-enclose the same complete outer candidate using its sharper true moments.

The exact R48 candidate is defined by five real source integrals.  Changing
their enclosing boxes does not change that candidate.  Prefix/suffix sums
retain each original material panel, and selected sources retain all20
modes, the full mean root and the complete analytic inverse remainder.
No new source integral, radial ODE, endpoint or metric is introduced here.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
from itertools import zip_longest
import json
from pathlib import Path
import resource
import time

from flint import arb,ctx

from closure_real_head_source_enclosure import exact_q
from closure_split_joint_io_v2 import read,read_field,iter_array,digest
from closure_shared_slope_cut_interface import ball,record
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_candidate_domain import endpoint_candidate,nonnegative_integral
from tail_outer_weighted_compatible import MOMENT_KEYS,make_weighted_candidate
from tail_outer_centered_quartic_fields_v2 import weighted_panel_fields,finite,intersection
from tail_outer_full_mean_residual_bounds import full_mean_residual_bounds
from closure_outer_candidate_source_record import signed_source_bounds


EXPECTED={
 'closure_outer_true_moment_taylor.py':'38ee3b538a5095fd4501f24c429ff7973bf324a70f515da5c3fff89b34d4e333',
 'tail_outer_centered_quartic_fields_v2.py':'671f6b0c02b3a59dcac79129dc8e73cff4baebe9ec477ee5509e3425f9fb086b',
 'tail_outer_weighted_compatible.py':'03c88b010447c78e4fb6bb26f0d3704fafd23510d16cc00084f315daa07f3d1b',
 'tail_outer_candidate_domain.py':'17d6b7d85be80f8f40b3eec411ae49a73c51c6b624d030df57b94202a7d08690',
 'closure_outer_candidate_source_record.py':'544bab2538a33ac32c546d980e08dc0d95fea383d5f25aed894fea9ce27c3d34',
 'tail_outer_full_mean_residual_bounds.py':'16f9d2d5c2e858686aff9d332df4cc565606481ab45a46d6a9080db29317c8af',
}


def partial_box(before,part,old):
    """An integral of a positive function through a whole original panel."""
    value=before.lower().union((before+part).upper())
    # Keep the proven nonnegative domain even if a rounded Arb union has a
    # tiny negative endpoint.  No independently rounded point integral is
    # substituted for the fixed true integral.
    common=intersection(value,ball(old))
    return nonnegative_integral(record(common))


def save(path,data):
    path=Path(path);raw=(json.dumps(data,separators=(',',':'))+'\n').encode()
    if len(raw)>1_000_000:
        raise ValueError('Keep complete large panel data in compressed groups')
    temp=Path(str(path)+'.partial');temp.write_bytes(raw);temp.replace(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('cell-manifest','moment-summary','source-summary','ports','response','ready','out-prefix'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--rss-kib',type=int,default=40960)
    a=p.parse_args();ctx.prec,ctx.threads=192,1;began=time.monotonic()
    out=Path(str(a.out_prefix)+'-summary.json')
    if out.exists() or Path(str(a.out_prefix)+'-segment0.json.gz').exists():
        raise FileExistsError('Use a fresh complete same-candidate source prefix')
    for name,expected in EXPECTED.items():
        if digest(Path(__file__).with_name(name))!=expected:
            raise ValueError('A frozen actual mathematical implementation changed: '+name)
    paths=[getattr(a,k) for k in ('cell_manifest','moment_summary','source_summary','ports','response','ready')]
    hashes={str(path):digest(path) for path in paths}
    material=read(a.cell_manifest);momdoc=read(a.moment_summary);oldsrc=read(a.source_summary)
    n=material['cell'];meta=material['original_metadata']
    if (not all(material['checks'].values()) or not momdoc['all_gates'] or not oldsrc['all_gates']
            or n!=momdoc['cell'] or n!=oldsrc['cell'] or n not in (10,11)
            or momdoc['panels']!=material['panels'] or oldsrc['panels']!=material['panels']):
        raise ValueError('The full original candidate and all refined true-moment panels are required')
    if (momdoc['entrypoint_sha256']!=EXPECTED['closure_outer_true_moment_taylor.py']
            or momdoc['original_material_manifest']!=str(a.cell_manifest)):
        raise ValueError('The refined moments must be those of this same true material package')
    for path in (a.cell_manifest,a.ready):
        if momdoc['input_hashes'].get(str(path))!=hashes[str(path)]:
            raise ValueError('The refined moment source identity differs')
    for path in (a.cell_manifest,a.ports,a.response,a.ready):
        if oldsrc['input_hashes'].get(str(path))!=hashes[str(path)]:
            raise ValueError('The original complete source used another candidate or source')
    ports=read(a.ports);ready=read(a.ready)
    cp=read_field(a.response,'response')['checkpoint']
    if cp['parameters']['modes']!=20 or cp['parameters']['physicalDepth']!=12:
        raise ValueError('Keep all20 actual saved modes and the original endpoint object')
    head=SourceValues(ready);head.params=ready['rationalDeepModel']['physicalParameters'];cell=OuterCell(head,n)
    prows={r['physical_node']:r for r in ports['rows']};tau=Fraction(oldsrc['tau'])
    left,lr=endpoint_candidate(cell,'inner',n+1,cp['rawStates'][n+1],prows[n+1],ball(meta['inner_radius']),tau,8)
    right,rr=endpoint_candidate(cell,'outer',n,cp['rawStates'][n],prows[n],ball(meta['outer_radius']),tau,8)
    refined={k:nonnegative_integral(v,strict=True) for k,v in momdoc['total_positive_moments'].items()}
    oldtotal={k:nonnegative_integral(v,strict=True) for k,v in meta['total_positive_moments'].items()}
    candidate=make_weighted_candidate(left,right,refined)
    oldcandidate=make_weighted_candidate(left,right,oldtotal)
    modes=sorted(left['H'])
    if modes!=list(range(2,41,2)):
        raise ValueError('The entire actual M20 even candidate is required')
    for m in modes:
        candidate['bubble_coefficient'][m]=intersection(candidate['bubble_coefficient'][m],oldcandidate['bubble_coefficient'][m])
    weights={m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}
    original={g['source_segment']:g for g in material['groups']}
    moment_groups={g['source_segment']:g for g in momdoc['groups']}
    source_groups={g['segment']:g for g in oldsrc['groups']}
    if any(sorted(d)!=list(range(9)) for d in (original,moment_groups,source_groups)):
        raise ValueError('All nine original source segments are required')
    group_sums=[tuple(ball(moment_groups[j]['summed_moments'][k]) for k in MOMENT_KEYS) for j in range(9)]
    total_sum=tuple(sum((v[i] for v in group_sums),arb(0)) for i in range(5))
    for i,k in enumerate(MOMENT_KEYS):
        intersection(total_sum[i],refined[k])
    owned=[];count=0;active=None
    max_R,max_L,max_remainder=arb(0),arb(0),arb(0)
    max_N={m:arb(0) for m in (2,4)}
    def guard():
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:
            raise MemoryError('Observed same-candidate source RSS exceeded its stop threshold')
    def recovery(error=None):
        save(str(a.out_prefix)+'-recovery.json',dict(
            status='Completed refined-source segments; no incomplete full-cell claim',cell=n,
            groups=owned,completed_panels=count,input_hashes=hashes,entrypoint_sha256=digest(__file__),
            error=error,elapsed_seconds=time.monotonic()-began))
    try:
        for j in range(9):
            og,mg,sg=original[j],moment_groups[j],source_groups[j]
            for group in (og,mg,sg):
                if digest(Path(group['path']))!=group['sha256']:
                    raise ValueError('An original/refined complete group changed')
                hashes[group['path']]=group['sha256']
            if (mg['original_group_sha256']!=og['sha256'] or
                    og['panels']!=mg['panels'] or og['panels']!=sg['panels']):
                raise ValueError('The original material partition and refined integrals differ')
            # Keep only five Arb values per leaf.  Full JSON material/source
            # rows are streamed, not retained in memory.
            integrals=[tuple(ball(row['moments'][k]) for k in MOMENT_KEYS)
                       for row in iter_array(mg['path'],'panels')]
            if len(integrals)!=og['panels']:
                raise ValueError('A refined moment group is incomplete')
            suffix=[None]*(len(integrals)+1);suffix[-1]=tuple(arb(0) for k in MOMENT_KEYS)
            for i in range(len(integrals)-1,-1,-1):
                suffix[i]=tuple(integrals[i][z]+suffix[i+1][z] for z in range(5))
            for z in range(5):
                intersection(suffix[0][z],group_sums[j][z])
            earlier=tuple(sum((group_sums[k][z] for k in range(j)),arb(0)) for z in range(5))
            later=tuple(sum((group_sums[k][z] for k in range(j+1,9)),arb(0)) for z in range(5))
            running=tuple(arb(0) for k in MOMENT_KEYS)
            target=Path(str(a.out_prefix)+f'-segment{j}.json.gz')
            if target.exists():
                raise FileExistsError('An actual complete refined-source group would be overwritten')
            active=gzip.open(target,'wt',compresslevel=9)
            active.write('{"cell":'+str(n)+',"segment":'+str(j)+',"tau":'+json.dumps(str(tau))+
                ',"original_material_sha256":'+json.dumps(og['sha256'])+
                ',"same_candidate_refined_moments_sha256":'+json.dumps(mg['sha256'])+',"panels":[\n')
            seen=0;group_N={m:arb(0) for m in (2,4)}
            streams=(iter_array(og['path'],'panels'),iter_array(mg['path'],'panels'),iter_array(sg['path'],'panels'))
            for i,pack in enumerate(zip_longest(*streams)):
                if any(x is None for x in pack):
                    raise ValueError('A full original/refined/source panel stream ended early')
                g,im,old=pack
                positions=[(r['x_left'],r['x_right']) for r in pack]
                if (len(set(positions))!=1 or im['panel']!=i or old['panel']!=i
                        or g['segment']!=j or g['original_parent']!=im['original_parent']):
                    raise ValueError('Same-candidate source rows must keep their exact radial positions')
                prefix={};after={}
                for z,k in enumerate(MOMENT_KEYS):
                    prefix[k]=partial_box(earlier[z]+running[z],integrals[i][z],g['prefix_moments'][k])
                    after[k]=partial_box(later[z]+suffix[i+1][z],integrals[i][z],g['suffix_moments'][k])
                    # Their true sum equals the one fixed whole-cell moment.
                    prefix[k]=nonnegative_integral(record(intersection(prefix[k],refined[k]-after[k])))
                    after[k]=nonnegative_integral(record(intersection(after[k],refined[k]-prefix[k])))
                H,K,Kx=weighted_panel_fields(candidate,u=ball(g['u']),u_x=ball(g['u_x']),
                    prefix_moments=prefix,suffix_moments=after)
                r,w,rx,ell=[ball(g[k]) for k in ('radius','w','radius_x','log_w_x')]
                if not r>0 or not w>0 or not rx>0 or not w<=arb(1)/2:
                    raise ArithmeticError('The unchanged true background lost positivity')
                norms={k:arb(0) for k in ('P_tau','K_tau','Kx_tau','nonmean_L_tau')}
                for m in modes:
                    hc,kk,kx=[finite(2*f[m].real) for f in (H,K,Kx)]
                    norms['P_tau']+=weights[m]*abs(m*hc/(r*w)).upper()
                    norms['K_tau']+=weights[m]*abs(kk).upper()
                    norms['Kx_tau']+=weights[m]*abs(kx).upper()
                    norms['nonmean_L_tau']+=weights[m]*abs(kk-(1+w*w)*m*m*hc/(r*w)).upper()
                norms={k:finite(v).upper() for k,v in norms.items()}
                R=(norms['P_tau']+norms['K_tau']).upper()
                if not R<arb(1)/64:
                    raise ArithmeticError('The complete R33 mean/work domain failed')
                max_R=max(max_R,R);max_L=max(max_L,norms['nonmean_L_tau'])
                full=full_mean_residual_bounds(H,K,Kx,modes=modes,weights=weights,radius=r,
                    radius_x=rx,w=w,log_w_x=ell,norms=norms)
                signed=signed_source_bounds(H,K,full,modes=modes,radius=r,radius_x=rx,w=w,
                    log_w_x=ell,norms=norms,tau=tau,selected=[2,4])
                old_selected={v['mode']:v for v in old['selected_cosine_sources']}
                for v in signed['selected_cosine_sources']:
                    previous=old_selected[v['mode']]
                    for key in ('quadratic_cosine','complete_source_cosine'):
                        v[key]=record(intersection(ball(v[key]),ball(previous[key])))
                    bound=abs(ball(v['complete_source_cosine'])).upper()
                    max_N[v['mode']]=max(max_N[v['mode']],bound)
                    group_N[v['mode']]=max(group_N[v['mode']],bound)
                max_remainder=max(max_remainder,ball(signed['complete_source_minus_quadratic_W1_upper']).upper())
                output={k:g[k] for k in ('segment','x_left','x_right','original_parent','radius_left',
                    'radius_right','radius','radius_x','w','log_w_x','width')}
                output.update(panel=i,complete_nonlinear_source_W1=record(full['complete_nonlinear_source_W1']),
                    complete_nonmean_source_residual_W1=record(full['complete_nonmean_source_residual_W1']),
                    physical_nonmean_second_source_W1=record(full['physical_nonmean_second_source_W1']),
                    complete_mean_abs=record(full['complete_mean_abs']),**signed)
                if seen:
                    active.write(',\n')
                active.write(json.dumps(output,separators=(',',':')))
                running=tuple(running[z]+integrals[i][z] for z in range(5))
                seen+=1;count+=1
                if seen%64==0:
                    guard()
            active.write('\n]}\n');active.close();active=None
            if seen!=og['panels'] or target.stat().st_size>=5*1024*1024:
                raise ValueError('A complete refined-source group failed its coverage/file gate')
            item=dict(segment=j,panels=seen,path=str(target),bytes=target.stat().st_size,sha256=digest(target),
                original_material_sha256=og['sha256'],refined_moments_sha256=mg['sha256'],
                selected_source_absolute_max={str(m):record(v) for m,v in group_N.items()})
            owned.append(item);recovery();guard()
            del integrals,suffix
            print(json.dumps(dict(event='complete_refined_source_segment',cell=n,segment=j,panels=seen,
                seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        if count!=material['panels']:
            raise ValueError('The complete original real cell was not replayed')
        gates=dict(original_metric_endpoints_all20_modes_and_actual_candidate_unchanged=True,
            new_boxes_enclose_the_same_five_true_integrals=True,
            positive_prefix_suffix_sums_keep_original_radial_positions=True,
            full_original_material_cover_replayed=True,
            complete_mean_Wiener_inverse_and_every_generated_mode_retained=True,
            all_selected_source_boxes_intersect_original_true_bounds=True,
            finite_Horner_and_explicit_mean_work_domain_paid=True,
            no_new_ODE_or_source_integral=True)
        result=dict(status='Complete same-candidate source with sharper true-integral enclosures',
            cell=n,panels=count,tau=str(tau),original_candidate_modes=modes,selected_cosine_modes=[2,4],
            groups=owned,gates=gates,all_gates=True,original_source_summary=str(a.source_summary),
            refined_moment_summary=str(a.moment_summary),same_exact_candidate=True,
            selected_source_absolute_max={str(m):record(v) for m,v in max_N.items()},
            maximum_complete_source_minus_quadratic_W1=record(max_remainder),
            maximum_R_tau=record(max_R),maximum_nonmean_L_tau=record(max_L),
            bubble_coefficient_cosine={str(m):record(v) for m,v in candidate['bubble_coefficient'].items()},
            old_bubble_coefficient_cosine={str(m):record(v) for m,v in oldcandidate['bubble_coefficient'].items()},
            endpoints=[lr,rr],source_units=oldsrc['source_units'],
            scope='The same mathematical candidate. New source intervals may reweight the original signed/absolute geometry kernels without new ODE. No exact outer solution claimed.',
            input_hashes=hashes,source_hashes=EXPECTED,entrypoint_sha256=digest(__file__),
            elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(out,result)
        print(json.dumps(dict(event='complete_refined_source',summary=str(out),all_gates=True,
            panels=count,maximum_R_tau=str(max_R),peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    except Exception as error:
        if active is not None:
            active.close()
        recovery(repr(error))
        raise


if __name__=='__main__':
    main()
