#!/usr/bin/env python3
"""Full20 amplitude-parameter derivative rows of the actual source functional.

The R48 nonmean candidate is varied affinely by multiplying both signed
Fourier coefficients of each physical mode by eta_m.  The complete mean
is re-solved.  The R74 parameter radii are retained.  The positive norms
saved by the complete source recorder bound this entire parameter product
domain, including the complete mean and Wiener inverse derivative.

This computes all20 columns together as a genuine block row norm; it
does not assign the whole bound to each coefficient or claim a full
outer Schur inverse.  The true head DN derivative is a separate input.
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


def bounds(d):
    lo,hi=point(d['lower']),point(d['upper'])
    if lo>hi:
        raise ValueError('Reversed exact input interval')
    return lo,hi


def upper(d):
    value=bounds(d)[1]
    if value<0:
        raise ValueError('A saved positive majorant is negative')
    return value


def roundup(x,bits=80):
    """Exact rational -> outward dyadic, avoiding unbounded denominators."""
    if x<0:
        raise ValueError('Round only a proved positive majorant')
    if x==0:
        return Fraction(0)
    exponent=x.numerator.bit_length()-x.denominator.bit_length()-bits+1
    scaled=x/Fraction(2)**exponent
    mantissa=-(-scaled.numerator//scaled.denominator)
    return Fraction(mantissa)*Fraction(2)**exponent


def record(x):
    with localcontext() as c:
        c.prec=32
        show=str(Decimal(x.numerator)/Decimal(x.denominator))
    return dict(numerator=str(x.numerator),denominator=str(x.denominator),display=show)


def derivative_majorant(source,sigma):
    """Uniform real/complex parameter differential, before epsilon_max.

At eta=1 the saved quantities are Q=A, mean numerator=B,
c0>=4R0^2 and l0>=c0+||K+E*T||_1.  On |eta_m|<=sigma,
c<=sigma^2*c0, |dc|<=4*sigma*c0*||deta||_infty.
The remainder uses an explicitly differentiated complete mean/inverse,
not a derivative inferred from a point value of N.
"""
    A=upper(source['quadratic_W1_upper'])
    B=upper(source['complete_mean_numerator_change_W1_upper'])
    c0=upper(source['complete_mean_abs'])
    l0=upper(source['leading_nonconstant_plus_mean_W1_upper'])
    if sigma*sigma*c0>=Fraction(1,1024):
        raise ArithmeticError('The entire parameter domain left R33 R<=1/64')
    ell=sigma*l0+sigma*sigma*c0
    if ell>=1:
        raise ArithmeticError('The complete parameter-domain Wiener inverse is not paid')
    main=2*sigma*A
    dmean=8*sigma**3*B
    dleading=l0+4*sigma*c0
    numerator=sigma*sigma*A+sigma**4*B
    remainder=ell*main/(1-ell)+dmean/(1-ell)+numerator*dleading/(1-ell)**2
    return roundup(main),roundup(remainder),ell,sigma*sigma*c0


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('functional','refined-source','family','completed-centres','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--rss-kib',type=int,default=40960)
    a=p.parse_args();began=time.monotonic()
    if a.out.exists():
        raise FileExistsError('Use a fresh actual parameter-source row packet')
    names=('functional','refined_source','family','completed_centres')
    docs={name:read(getattr(a,name)) for name in names}
    hashes={str(getattr(a,name)):digest(getattr(a,name)) for name in names}
    functional,new,family,centres=(docs[name] for name in names)
    if any(not d['all_gates'] for d in docs.values()):
        raise ValueError('All actual source, geometry and parameter packages are required')
    if (functional['modes']!=[2,4] or functional['endpoint_physical_node']!=10
            or functional['counts']['original_material']!=10793
            or new['cell']!=10 or not new['same_exact_candidate']):
        raise ValueError('Keep the certified actual two-cell candidate scope')
    for path in (a.functional,a.refined_source,a.family):
        if centres['input_hashes'].get(str(path))!=hashes[str(path)]:
            raise ValueError('The completed centre package and derivative rows have different inputs')
    axes={r['mode']:r for r in family['parameter_axes']}
    if sorted(axes)!=list(range(2,41,2)):
        raise ValueError('All20 actual parameter axes must be retained')
    eps={m:bounds(r['relative_radius']) for m,r in axes.items()}
    if any(lo!=hi or lo<=0 for lo,hi in eps.values()):
        raise ValueError('The actual independent relative axes must be exact positive numbers')
    eps={m:value[0] for m,value in eps.items()}
    if eps!={m:Fraction(1,16 if m==4 else 1024) for m in axes}:
        raise ValueError('Retain the complete R74 product domain, not a different radius')
    epsmax=max(eps.values());sigma=1+epsmax
    groups={r['segment']:r for r in new['groups']}
    if sorted(groups)!=list(range(9)):
        raise ValueError('All nine refined source segments must be consumed')
    totals={m:[[Fraction(0),Fraction(0)] for readout in range(2)] for m in (2,4)}
    group_rows=[];count=0;max_l,max_c=Fraction(0),Fraction(0)
    for group in functional['kernel_groups']:
        n,j=group['cell'],group['segment'];kp=Path(group['path'])
        replacement=groups[j] if n==10 else None
        sp=Path(replacement['path']) if replacement else Path(group['source_group_path'])
        sh=replacement['sha256'] if replacement else group['source_group_sha256']
        if digest(kp)!=group['sha256'] or digest(sp)!=sh:
            raise ValueError('An actual fixed source/geometry group changed')
        hashes[str(kp)]=group['sha256'];hashes[str(sp)]=sh
        sources={}
        for row in iter_array(sp,'panels'):
            if upper(row['w'])>Fraction(1,2) or bounds(row['w'])[0]<=0:
                raise ArithmeticError('The entire real background w domain is required')
            main,rem,l,c=derivative_majorant(row,sigma)
            max_l=max(max_l,l);max_c=max(max_c,c)
            sources[row['panel']]=(row['x_left'],row['x_right'],main,rem)
        sums={m:[[Fraction(0),Fraction(0)] for readout in range(2)] for m in (2,4)}
        seen=0
        for row in iter_array(kp,'panels'):
            xl,xr,main,rem=sources.pop(row['panel'])
            if (xl,xr)!=(row['x_left'],row['x_right']):
                raise ValueError('Every derivative source must retain its actual radial position')
            expected={(m,k) for m in (2,4) for k in (0,1)}
            for weight in row['weights']:
                m,k=weight['mode'],weight['readout'];expected.remove((m,k))
                absolute=point(weight['absolute'])
                if absolute<0:
                    raise ValueError('A true absolute geometry kernel is negative')
                # The input norm is max_m |deta_m|/epsilon_m.  Taking one
                # epsilon_max controls all20 modes simultaneously.  It
                # is not repeated once per Fourier coefficient.
                coefficient=absolute*epsmax/Fraction(1+m)
                sums[m][k][0]+=main*coefficient
                sums[m][k][1]+=rem*coefficient
            if expected:
                raise ValueError('Every complete dual-readout row is required')
            seen+=1
        if sources or seen!=group['panels']:
            raise ValueError('A complete true material group was omitted')
        count+=seen
        for m in (2,4):
            for k in (0,1):
                for component in (0,1):
                    totals[m][k][component]+=sums[m][k][component]
        group_rows.append(dict(cell=n,segment=j,panels=seen,
            global_qv_parameter_row_norm={str(m):[
                dict(quadratic=record(v[0]),complete_mean_inverse_remainder=record(v[1]))
                for v in sums[m]] for m in (2,4)}))
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:
            raise MemoryError('The exact source parameter row exceeded its RSS stop threshold')
    if count!=10793 or len(group_rows)!=18:
        raise ValueError('All original panels and both terminal readouts must be paid')
    oldrows={r['mode']:r for r in functional['rows']}
    centre_rows={r['mode']:r for r in centres['rows']}
    result=[]
    for m in (2,4):
        factor=max(abs(v) for v in bounds(oldrows[m]['canonical_cut_geometry_factor']))
        axis=bounds(axes[m]['half_axis'])
        if axis[0]!=axis[1] or axis[0]<=0:
            raise ValueError('The canonical output half-axis must be exact and positive')
        main=factor*totals[m][0][0]/axis[0]
        remainder=factor*totals[m][0][1]/axis[0]
        row=main+remainder
        c=centre_rows[m]['complete_candidate_node10_centre']
        centre_ratio=max(abs(v) for v in bounds(c))/axis[0]
        result.append(dict(mode=m,all20_parameter_block_row_norm=record(row),
            quadratic_block_row_norm=record(main),complete_mean_inverse_row_norm=record(remainder),
            actual_R74_axis=axes[m]['half_axis'],
            centre_axis_ratio=record(centre_ratio),centre_plus_source_variation_ratio=record(centre_ratio+row),
            source_only_row_less_than_one=row<1,
            centre_plus_candidate_source_variation_inside_axis=centre_ratio+row<1,
            both_global_qv_readout_rows=[record(sum(v)) for v in totals[m]]))
    gates=dict(complete_actual_R74_twenty_parameter_product=True,
        complete_mean_small_holomorphic_domain_paid_by_absolute_norms=True,
        complete_inverse_and_its_derivative_paid=True,
        all10793_actual_positions_and_both_terminal_readouts=True,
        all20_directions_controlled_simultaneously_without_repeating_total_mass=True,
        source_coefficients_use_true_weight_lower_bound_at_least_one_plus_m=True,
        outward80bit_dyadic_rounding_after_exact_positive_local_arithmetic=True,
        same_fixed_candidate_metric_and_endpoints_at_centre=True,
        no_Cauchy_claim_for_the_unfinished_exact_outer_solution=True,
        no_new_source_integrals_ODE_or_Arb=True)
    output=dict(status='Actual complete amplitude-parameter block rows of the outer candidate source functional',
        gates=gates,all_gates=True,rows=result,group_rows=group_rows,panels=count,
        parameter_definition='eta_m=Q_m/Q_m^0; both signed nonmean coefficients and all nonmean radial jets of the same candidate mode are scaled by eta_m; complete mean is solved afresh',
        parameter_metric='max_m |deta_m|/epsilon_m, epsilon_4=1/16, all other19 epsilon=1/1024',
        output_metric='absolute canonical cut-Q contribution divided by the matching R74 half-axis',
        sigma=record(sigma),epsilon_max=record(epsmax),
        maximum_complete_leading_norm=record(max_l),maximum_mean_radius=record(max_c),
        proof='Saved A,B,c0,l0 are positive homogeneous majorants; ||DQ_eta||<=2 sigma A, c_eta<=sigma^2 c0, ||dc_eta||<=4 sigma c0, mean numerator derivative<=8 sigma^3 B. Differentiate N=(Q+mean)/(1+l) exactly; all inverse-generated modes retained.',
        true_head_DN_derivative_included=False,unknown_outer_field_correction_included=False,
        full_outer_Green_or_Schur_inverse_claimed=False,
        input_hashes=hashes,source_sha256=digest(__file__),arithmetic='Exact Fraction with explicit outward dyadic upper rounding',
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),all_gates=True,panels=count,
        rows=[dict(mode=r['mode'],source_row=r['all20_parameter_block_row_norm']['display'],
            remainder_row=r['complete_mean_inverse_row_norm']['display'],
            centre_plus_row=r['centre_plus_source_variation_ratio']['display']) for r in result],
        peak_RSS_KiB=output['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':
    main()
