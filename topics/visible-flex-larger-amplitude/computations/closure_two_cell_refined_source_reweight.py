#!/usr/bin/env python3
"""Exact reweighting of the R73 two-cell signed/absolute source kernels.

Only enclosures of the same R48 candidate source may replace old source
boxes.  The complete mean, inverse remainder, true R63 low-far addendum,
shared slope and fixed global mu11 are retained.  Both terminal readouts
are recomputed.  This is a nonlinear-source centre budget, not an outer
Green inverse or an existence proof for the remaining nonlinear problem.
"""
import argparse
from decimal import Decimal,localcontext
from fractions import Fraction
import json
from pathlib import Path
import resource
import time

from closure_split_joint_io_v2 import read,iter_array,digest


def point(d):
    if isinstance(d,list):
        m,k=int(d[0]),int(d[1])
    elif 'numerator' in d:
        return Fraction(int(d['numerator']),int(d['denominator']))
    else:
        m,k=int(d['mantissa']),int(d['binary_exponent'])
    return Fraction(m)*Fraction(2)**k


def interval(d):
    lo,hi=point(d['lower']),point(d['upper'])
    if lo>hi:
        raise ValueError('An exact input interval is reversed')
    return lo,hi


def rational(x):
    with localcontext() as c:
        c.prec=32
        show=str(Decimal(x.numerator)/Decimal(x.denominator))
    return dict(numerator=str(x.numerator),denominator=str(x.denominator),display=show)


def record(v):
    return dict(lower=rational(v[0]),upper=rational(v[1]))


def intersection(a,b):
    result=max(a[0],b[0]),min(a[1],b[1])
    if result[0]>result[1]:
        raise ArithmeticError('Two enclosures of the exact same functional do not intersect')
    return result


def add(a,b):
    return a[0]+b[0],a[1]+b[1]


def multiply(a,b):
    values=[x*y for x in a for y in b]
    return min(values),max(values)


def magnitude(a):
    return max(abs(a[0]),abs(a[1]))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('functional','linear-cancellation','far-completion','old-budget','family','refined-source','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--rss-kib',type=int,default=40960)
    a=p.parse_args();began=time.monotonic()
    if a.out.exists():
        raise FileExistsError('Use a fresh same-candidate source-reweight output')
    names=('functional','linear_cancellation','far_completion','old_budget','family','refined_source')
    docs={name:read(getattr(a,name)) for name in names}
    hashes={str(getattr(a,name)):digest(getattr(a,name)) for name in names}
    functional,linear,far,budget,family,new=(docs[name] for name in names)
    if any(not d['all_gates'] for d in docs.values()):
        raise ValueError('All complete original and refined source certificates are required')
    if (functional['endpoint_physical_node']!=10 or functional['modes']!=[2,4]
            or functional['counts']['original_material']!=10793
            or not new['same_exact_candidate'] or new['cell']!=10
            or new['original_candidate_modes']!=list(range(2,41,2))):
        raise ValueError('Retain the exact two-cell/m2m4 and full M20 candidate scopes')
    for parent,path in ((functional,a.linear_cancellation),(budget,a.functional),
                        (budget,a.far_completion),(family,a.old_budget)):
        if parent['input_hashes'].get(str(path))!=hashes[str(path)]:
            raise ValueError('The completed same-source dependency chain changed')
    origin=new['original_source_summary']
    if (origin not in functional['input_hashes']
            or new['input_hashes'].get(origin)!=functional['input_hashes'][origin]
            or digest(origin)!=functional['input_hashes'][origin]):
        raise ValueError('The refined source must enclose the same original candidate')
    for path in set(new['input_hashes'])&set(linear['input_hashes']):
        if new['input_hashes'][path]!=linear['input_hashes'][path]:
            raise ValueError('The original source response and linear centre differ')
    new_groups={g['segment']:g for g in new['groups']}
    if sorted(new_groups)!=list(range(9)):
        raise ValueError('All nine refined source groups are required')
    modes=[2,4];totals={m:[[Fraction(0),Fraction(0)] for j in range(2)] for m in modes}
    absolute={m:[Fraction(0),Fraction(0)] for m in modes}
    rows=[];count=0
    for group in functional['kernel_groups']:
        n,j=group['cell'],group['segment']
        kp=Path(group['path']);oldp=Path(group['source_group_path'])
        if digest(kp)!=group['sha256'] or digest(oldp)!=group['source_group_sha256']:
            raise ValueError('An immutable true geometry/source group changed')
        replacement=new_groups[j] if n==10 else None
        sp=Path(replacement['path']) if replacement else oldp
        sha=replacement['sha256'] if replacement else group['source_group_sha256']
        if digest(sp)!=sha:
            raise ValueError('A refined source group changed')
        for path,value in ((kp,group['sha256']),(oldp,group['source_group_sha256']),(sp,sha)):
            hashes[str(path)]=value
        sources={}
        for row in iter_array(sp,'panels'):
            selected={v['mode']:interval(v['complete_source_cosine'])
                      for v in row['selected_cosine_sources']}
            if sorted(selected)!=modes:
                raise ValueError('Both complete signed source coefficients are required')
            sources[row['panel']]=(row['x_left'],row['x_right'],selected)
        sums={m:[[Fraction(0),Fraction(0)] for k in range(2)] for m in modes}
        abs_sums={m:[Fraction(0),Fraction(0)] for m in modes}
        seen=0
        for row in iter_array(kp,'panels'):
            xl,xr,values=sources.pop(row['panel'])
            if (xl,xr)!=(row['x_left'],row['x_right']):
                raise ValueError('Every source must stay at its actual original radial position')
            expected={(m,k) for m in modes for k in range(2)}
            for w in row['weights']:
                m,k=w['mode'],w['readout'];expected.remove((m,k))
                ks=tuple(map(point,w['signed']));ka=point(w['absolute'])
                if ka<0:
                    raise ArithmeticError('An absolute kernel bound is negative')
                ks=intersection(ks,(-ka,ka))
                nl,nh=values[m];c=(nl+nh)/2;rad=(nh-nl)/2
                # A variable source interval cannot be multiplied by only
                # the signed integral.  The whole variation multiplies
                # the separately certified absolute kernel.
                shifted=multiply((c,c),ks);delta=rad*ka
                term=(shifted[0]-delta,shifted[1]+delta)
                direct_cap=max(abs(nl),abs(nh))*ka
                term=intersection(term,(-direct_cap,direct_cap))
                sums[m][k][0]+=term[0];sums[m][k][1]+=term[1]
                abs_sums[m][k]+=direct_cap
            if expected:
                raise ValueError('A complete original dual-readout kernel row is required')
            seen+=1
        if sources or seen!=group['panels']:
            raise ValueError('The complete original geometry/source group was not consumed')
        count+=seen
        for m in modes:
            for k in range(2):
                totals[m][k][0]+=sums[m][k][0];totals[m][k][1]+=sums[m][k][1]
                absolute[m][k]+=abs_sums[m][k]
        rows.append(dict(cell=n,segment=j,panels=seen,source_reenclosed=(n==10),
            source_path=str(sp),kernel_path=str(kp),
            true_global_qv_forcing={str(m):[record(v) for v in sums[m]] for m in modes}))
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:
            raise MemoryError('The exact source reweight exceeded its owned RSS threshold')
    if count!=10793 or len(rows)!=18:
        raise ValueError('Every original real panel in both cells is required')
    original={row['mode']:row for row in functional['rows']}
    lrows={row['mode']:row for row in linear['rows'] if row['endpoint_physical_node']==10}
    frows={row['mode']:row for row in far['propagation_rows'] if row['endpoint_physical_node']==10}
    brows={row['mode']:row for row in budget['rows']}
    axes={row['mode']:row for row in family['parameter_axes']}
    result=[]
    for m in modes:
        original_row=original[m]
        vector=[intersection(tuple(v),interval(original_row['true_global_qv_forcing_vector'][k]))
                for k,v in enumerate(totals[m])]
        factor=interval(original_row['canonical_cut_geometry_factor'])
        forcing=multiply(factor,vector[0])
        forcing=intersection(forcing,interval(original_row['signed_canonical_cut_forcing_contribution']))
        l0=interval(lrows[m]['complete_head_lift_minus_outer_candidate_Q'])
        supplement=interval(frows[m]['cut_Q_centre_addition_upper'])[1]
        complete=add(add(l0,forcing),(-supplement,supplement))
        complete=intersection(complete,interval(brows[m]['original_candidate_complete_node10_centre']))
        centre=interval(lrows[m]['same_exact_saved_cut_Q'])
        if centre[0]!=centre[1] or interval(axes[m]['exact_centre'])!=centre:
            raise ValueError('The completed parameter family has a different exact shallow centre')
        axis=interval(axes[m]['half_axis'])
        if axis[0]!=axis[1] or axis[0]<=0:
            raise ValueError('The actual available axis must be one positive exact dyadic')
        r72=abs(centre[0])/1024
        result.append(dict(mode=m,true_global_qv_forcing_vector=[record(v) for v in vector],
            signed_canonical_cut_source=record(forcing),
            absolute_canonical_cut_source_upper=rational(magnitude(factor)*absolute[m][0]),
            original_source_interval=original_row['signed_canonical_cut_forcing_contribution'],
            source_radius_improvement_ratio=rational(
                (interval(original_row['signed_canonical_cut_forcing_contribution'])[1]-
                 interval(original_row['signed_canonical_cut_forcing_contribution'])[0])/
                (forcing[1]-forcing[0])),
            true_linear_plus_head_nonfar_centre=record(l0),
            explicit_R63_low_far_addition_upper=rational(supplement),
            complete_candidate_node10_centre=record(complete),
            actual_R74_axis=record(axis),R74_axis_ratio_upper=rational(magnitude(complete)/axis[0]),
            within_actual_R74_axis=magnitude(complete)<axis[0],
            original_R72_axis=rational(r72),R72_axis_ratio_upper=rational(magnitude(complete)/r72),
            within_original_R72_axis=magnitude(complete)<r72))
    gates=dict(same_actual_candidate_and_complete_M20_source=True,
        all10793_original_radial_positions_and_both_terminal_readouts=True,
        signed_integral_plus_absolute_source_error_used=True,
        complete_mean_inverse_and_nonzero_R63_low_far_retained=True,
        same_shared_slope_background_and_fixed_global_mu11=True,
        completed_R74_family_origin_and_parameter_units_checked=True,
        no_new_source_integral_or_ODE=True)
    output=dict(status='Complete same-candidate refined-source dual-readout functional',
        gates=gates,all_gates=True,panels=count,cells=[11,10],endpoint_physical_node=10,
        rows=result,group_rows=rows,
        all_centres_within_actual_R74_axes=all(r['within_actual_R74_axis'] for r in result),
        all_centres_within_original_R72_axes=all(r['within_original_R72_axis'] for r in result),
        full_outer_correction_Green_or_Schur_inverse_paid=False,
        input_hashes=hashes,source_sha256=digest(__file__),arithmetic='Exact stdlib Fraction; decimals are display only',
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),all_gates=True,panels=count,
        rows=[dict(mode=r['mode'],source=[r['signed_canonical_cut_source'][k]['display'] for k in ('lower','upper')],
            R74_ratio=r['R74_axis_ratio_upper']['display'],R72_ratio=r['R72_axis_ratio_upper']['display']) for r in result],
        peak_RSS_KiB=output['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':
    main()
