#!/usr/bin/env python3
"""Consume true phi/chi profiles in source order: whole-field Green norms.

Exact rational arithmetic only.  The source is not collapsed to an
endpoint.  Prefix phi integrals and suffix chi integrals are retained
at each original-position subpanel; the same-panel partial integrals
receive valid absolute bounds.  Both physical components are covered.
"""
import argparse
from decimal import Decimal,localcontext
from fractions import Fraction
import json
from pathlib import Path
import resource
import tempfile
import time

from closure_split_joint_io_v2 import read,iter_array,digest
from closure_outer_source_parameter_rows import point,bounds,record


ZERO=(Fraction(0),Fraction(0))


def pair(d):
    return tuple(point(x) for x in d) if isinstance(d,list) else bounds(d)


def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def remove_summand(total,summand):
    # Both interval endpoints were constructed by exact independent sums.
    # This removes a known summand of that sum, not two correlated balls.
    out=(total[0]-summand[0],total[1]-summand[1])
    if out[0]>out[1]:raise ArithmeticError('A removed exact interval summand is inconsistent')
    return out


def mul(a,b):
    values=[x*y for x in a for y in b]
    return min(values),max(values)


def div(a,b):
    if b[0]<=0<=b[1]:raise ArithmeticError('The only global Wronskian denominator contains0')
    return mul(a,(Fraction(1)/b[1],Fraction(1)/b[0]))


def norm(a):return max(abs(x) for x in a)
def positive_min(a):
    if a[0]<=0<=a[1]:raise ArithmeticError('A nonzero true value is required')
    return min(abs(x) for x in a)


def intersection(a,b):
    lo,hi=max(a[0],b[0]),min(a[1],b[1])
    if lo>hi:raise ArithmeticError('Two certified representations of the same value are disjoint')
    return lo,hi


def rec_interval(a):return dict(lower=record(a[0]),upper=record(a[1]))


def source_integral(kernel,N):
    K=pair(kernel['signed']);A=point(kernel['absolute'])
    centre=(N[0]+N[1])/2;radius=(N[1]-N[0])/2
    value=add(mul((centre,centre),K),(-radius*A,radius*A))
    return value,A*norm(N)


def iterate_forward(group,spool_dir):
    """Published profiles are in reverse order; reverse privately on disk."""
    with tempfile.TemporaryFile(mode='w+b',dir=spool_dir) as spool:
        offsets=[]
        for row in iter_array(Path(group['path']),'panels'):
            offsets.append(spool.tell());spool.write(json.dumps(row,separators=(',',':')).encode()+b'\n')
        if len(offsets)!=group['subpanels']:raise ValueError('A complete true profile group is missing')
        for offset in reversed(offsets):
            spool.seek(offset);yield json.loads(spool.readline())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('profiles','completed-source','family','inner-head','linear-cancellation','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--rss-kib',type=int,default=40960)
    a=p.parse_args();began=time.monotonic()
    if a.out.exists():raise FileExistsError('Use a fresh actual whole-field Green budget')
    paths=(a.profiles,a.completed_source,a.family,a.inner_head,a.linear_cancellation)
    docs=[read(x) for x in paths];profiles,completed,family,head,linear=docs
    hashes={str(x):digest(x) for x in paths}
    if any(not d['all_gates'] for d in docs):raise ValueError('All complete actual data are required')
    config=profiles['config'];modes=config['modes']
    if (modes!=[2,4] or config['input_cutoff']!=92 or config['field_radius']!='1/16'
            or profiles['counts']['original_material']!=10793):
        raise ValueError('Retain the full actual two-output/low46-input scope')
    if head['parameter_axes']!=family['parameter_axes']:
        raise ValueError('The true head and candidate use different twenty-parameter axes')
    W={m:pair(config['true_Wronskians'][str(m)]) for m in modes}
    Wabs={m:positive_min(W[m]) for m in modes}
    axes={r['mode']:r for r in family['parameter_axes']}
    hrows={r['mode']:r for r in head['selected_true_DN_minus_exact_linear_DN']}
    lrows={r['mode']:r for r in linear['rows'] if r['endpoint_physical_node']==10}
    crows={r['mode']:r for r in completed['rows']}
    if sorted(hrows)!=modes or sorted(lrows)!=modes or sorted(crows)!=modes:
        raise ValueError('Both actually certified output modes are required')
    if completed['input_hashes'].get(str(a.family))!=hashes[str(a.family)]:
        raise ValueError('The source functional uses another actual R74 family')
    if completed['input_hashes'].get(str(a.linear_cancellation))!=hashes[str(a.linear_cancellation)]:
        raise ValueError('The source functional and affine lift use different exact endpoint data')
    common=profiles['input_hashes']
    for marker in ('closure-outer-two-cell-adjoint-r1.json',
                   'closure-outer-source-cell10-refined-moments-r1-summary.json'):
        matched=[(path,sha) for path,sha in common.items() if path.endswith(marker)]
        if len(matched)!=1 or completed['input_hashes'].get(matched[0][0])!=matched[0][1]:
            raise ValueError('The whole-field and completed boundary source are not the same actual objects')
    # Complete prefix/suffix source totals and field-derivative densities.
    total={m:{name:dict(signed=ZERO,absolute=Fraction(0),derivative=Fraction(0))
              for name in ('phi','chi')} for m in modes}
    group_totals=[];count=0
    for group in profiles['profile_groups']:
        path=Path(group['path'])
        if digest(path)!=group['sha256']:raise ValueError('A true whole-field profile changed')
        hashes[str(path)]=group['sha256']
        recent={m:{name:Fraction(0) for name in ('phi','chi')} for m in modes}
        seen=0
        for row in iter_array(path,'panels'):
            density=point(row['whole_low46_source_derivative_density'])
            if density<0:raise ValueError('The complete field derivative density must be positive')
            for r in row['modes']:
                m=r['mode'];N=pair(r['complete_candidate_source'])
                for name in ('phi','chi'):
                    value,absolute=source_integral(r['integrals'][name],N)
                    bound=point(r['integrals'][name]['absolute'])*density
                    acc=total[m][name]
                    acc['signed']=add(acc['signed'],value)
                    acc['absolute']+=absolute;acc['derivative']+=bound
                    recent[m][name]+=bound
            seen+=1;count+=1
        if seen!=group['subpanels']:raise ValueError('An entire source-position group is required')
        group_totals.append(dict(cell=group['cell'],segment=group['segment'],subpanels=seen,
            derivative_integrals={str(m):{z:record(v) for z,v in r.items()} for m,r in recent.items()}))
    if count!=profiles['counts']['taylor']+profiles['counts']['root_brackets']:
        raise ValueError('The complete ordered source partition is required')
    old_source_checks=[]
    for m in modes:
        old=pair(crows[m]['true_global_qv_forcing_vector'][0])
        agreed=intersection(neg(total[m]['chi']['signed']),old)
        old_source_checks.append(dict(mode=m,new_terminal_q_source=rec_interval(neg(total[m]['chi']['signed'])),
            R79_same_functional=rec_interval(old),intersection=rec_interval(agreed)))
    prefix={m:dict(signed=ZERO,derivative=Fraction(0)) for m in modes}
    suffix={m:dict(signed=total[m]['chi']['signed'],derivative=total[m]['chi']['derivative']) for m in modes}
    maxima={m:{c:dict(derivative=Fraction(-1),candidate_response=Fraction(-1),
                  affine_outer_parameter_lift=Fraction(-1),true_head_value_lift=Fraction(-1),
                  true_head_parameter_derivative_lift=Fraction(-1),where={}) for c in ('P','K')} for m in modes}
    b=pair(config['cut_radius']);mu=pair(config['global_mu_star'])
    if b[0]<=0 or mu[0]<=0:raise ValueError('The true cut radius and momentum scale must be positive')
    cut_w=None;seen=0
    for group in profiles['profile_groups']:
        for row in iterate_forward(group,a.out.parent):
            V=pair(row['source_envelope'])
            if V[0]!=V[1] or V[0]<=0:
                raise ValueError('The exact chosen upward-dyadic physical envelope must be retained')
            V=V[0]
            density=point(row['whole_low46_source_derivative_density'])
            if cut_w is None:cut_w=pair(row['w'])[1]
            # sqrt12>3 gives a fully rational outward bound; the very
            # first whole interval contains the true b and w(b).
            head_conversion=b[1]**4*cut_w**2/(3*mu[0])
            for r in row['modes']:
                m=r['mode'];N=pair(r['complete_candidate_source'])
                pv,pa=source_integral(r['integrals']['phi'],N)
                cv,ca=source_integral(r['integrals']['chi'],N)
                pd=point(r['integrals']['phi']['absolute'])*density
                cd=point(r['integrals']['chi']['absolute'])*density
                after_signed=remove_summand(suffix[m]['signed'],cv)
                after_derivative=suffix[m]['derivative']-cd
                if after_derivative<0:raise ArithmeticError('A true source suffix was lost')
                # The target can be ANY point of this subpanel.  The
                # source on that same subpanel is divided at the target;
                # each partial integral is bounded by its whole absolute
                # integral.  This is conservative but never uses an
                # endpoint integral as a pointwise field value.
                first=add(prefix[m]['signed'],(-pa,pa))
                second=add(after_signed,(-ca,ca))
                fmass=prefix[m]['derivative']+pd
                cmass=after_derivative+cd
                eps=pair(axes[m]['relative_radius'])[1]
                outQ=norm(pair(lrows[m]['exact_saved_outer_candidate_Q']))
                Smin=positive_min(pair(lrows[m]['same_true_S0_Q']))
                # A simple exact rational upper bound on the actual
                # (1+m)exp(m/64) weight; derivative norms cancel it exactly.
                weight=Fraction(1+m)/(1-Fraction(m,64))
                hv=pair(hrows[m]['uniform_value_upper'])[1]
                hd=pair(hrows[m]['first_derivative_linf_to_output_upper'])[1]
                for k,c in enumerate(('P','K')):
                    fp=pair(r['phi_physical_PK'][k]);cp=pair(r['chi_physical_PK'][k])
                    dnorm=(norm(cp)*fmass+norm(fp)*cmass)/(Wabs[m]*V)
                    actual=div(add(mul(cp,first),mul(fp,second)),W[m])
                    cnorm=weight*norm(actual)/V
                    affine=weight*norm(fp)*eps*outQ/(Smin*V)
                    headvalue=norm(cp)*head_conversion*hv/(Wabs[m]*V)
                    headderivative=norm(cp)*head_conversion*hd/(Wabs[m]*V)
                    z=maxima[m][c]
                    values=dict(derivative=dnorm,candidate_response=cnorm,
                        affine_outer_parameter_lift=affine,true_head_value_lift=headvalue,
                        true_head_parameter_derivative_lift=headderivative)
                    for name,value in values.items():
                        if value>z[name]:
                            z[name]=value
                            z['where'][name]=dict(cell=group['cell'],segment=group['segment'],
                                panel=row['panel'],subpanel=row['subpanel'],x_left=row['x_left'],x_right=row['x_right'])
                    if dnorm==z['derivative']:
                        z['derivative_parts']=dict(phi_prefix=record(norm(cp)*fmass/(Wabs[m]*V)),
                            chi_suffix=record(norm(fp)*cmass/(Wabs[m]*V)),
                            same_panel_phi=record(norm(cp)*pd/(Wabs[m]*V)),
                            same_panel_chi=record(norm(fp)*cd/(Wabs[m]*V)))
                prefix[m]['signed']=add(prefix[m]['signed'],pv)
                prefix[m]['derivative']+=pd
                suffix[m]['signed']=after_signed;suffix[m]['derivative']=after_derivative
            seen+=1
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:
                raise MemoryError('The exact ordered Green consumer exceeded its owned RSS gate')
    if seen!=count or any(suffix[m]['signed']!=ZERO or suffix[m]['derivative']!=0 for m in modes):
        raise ValueError('The full source order did not finish exactly')
    rows=[];sums={name:Fraction(0) for name in ('derivative','candidate_response',
        'affine_outer_parameter_lift','true_head_value_lift','true_head_parameter_derivative_lift')}
    for m in modes:
        components={}
        for c,z in maxima[m].items():
            components[c]={name:record(value) for name,value in z.items() if name in sums}
            components[c]['maximizers']=z['where'];components[c]['derivative_parts']=z['derivative_parts']
            for name in sums:sums[name]+=z[name]
        rows.append(dict(mode=m,physical_components=components))
    gates=dict(all10793_original_positions_and10933_true_subpanels=True,
        both_physical_components_whole_intervals=True,
        no_internal_phi_height_division=True,
        source_order_and_same_panel_partials_paid=True,
        candidate_source_agrees_with_independent_R79_terminal_functional=True,
        complete_low46_field_mean_and_Wiener_inverse_derivative=True,
        actual_true_head_parameter_lift_separate=True,
        known_affine_outer_candidate_endpoint_lift_included=True,
        exact_fraction_arithmetic_without_new_source_ODE_Arb=True)
    output=dict(status='Actual whole-field two-output Green bounds with low46 input density and separate endpoint lifts',
        all_gates=all(gates.values()),gates=gates,rows=rows,subpanels=seen,
        sums={name:record(value) for name,value in sums.items()},
        projected_low2_unknown_field_source_derivative_less_than_one=sums['derivative']<1,
        projected_candidate_response_less_than_field_radius=sums['candidate_response']<Fraction(1,16),
        physical_norm='Sum over selected outputs of (1+m)exp(m/64) times the separate sup_r |P_m|/V and sup_r |K_m|/V; input directions include all even m<=92 in the same strong norm',
        exact_envelope_definition='Each original-panel V is the exact upward80bit dyadic sqrt(saved complete_mean_abs upper/4) used before deriving the source density',
        parameter_norm='All20 normalized R74 axes; complete candidate amplitude sigma17/16; unknown field radius1/16',
        endpoint_lift_scope='Affine outer-height lift uses the same linear-head homogeneous phi/S0. Its inner height change must be kept in the parameter evaluation. True-head lift uses chi and the full R78 nonlinear K, not a zero mean approximation.',
        unknown_field_correction_or_full_outer_fixed_point_claimed=False,
        other44_low_output_rows_and_all_high_outputs_remain=True,
        old_terminal_source_checks=old_source_checks,derivative_source_group_totals=group_totals,
        input_hashes=hashes,source_sha256=digest(__file__),
        helper_sha256={n:digest(Path(__file__).with_name(n)) for n in
            ('closure_split_joint_io_v2.py','closure_outer_source_parameter_rows.py')},
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),all_gates=output['all_gates'],
        sums={name:record(value)['display'] for name,value in sums.items()},
        source_derivative_below_one=output['projected_low2_unknown_field_source_derivative_less_than_one'],
        peak_RSS_KiB=output['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
