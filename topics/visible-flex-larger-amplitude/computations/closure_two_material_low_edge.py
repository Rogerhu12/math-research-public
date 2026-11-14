#!/usr/bin/env python3
"""Independent radial d1 low-Green edge from actual saved source panels.

No new Peano--Baker flow is used.  The source column is bounded by its
proved whole-cell supremum; the radial source mass retains every actual
panel's V, radius and continuous-strip interval.  This is an independent
d1 upper, never the old combined upper multiplied by an integral ratio.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx
from closure_real_head_source_enclosure import ball_record, power2
from closure_real_head_green_enclosure import ball
from closure_split_joint_io import digest, read, iter_array, metadata_without_array


def compact(value):return arb(int(value[0]))*power2(int(value[1]))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('strong-low','strong-density','strong-reference','source-panel','target-panel','material','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--source-cell',type=int,default=12)
    p.add_argument('--target-cell',type=int,default=13)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a fresh independent two-material edge prefix')
    hashes={str(getattr(args,name)):digest(getattr(args,name)) for name in
        ('strong_low','strong_density','strong_reference','source_panel','target_panel','material')}
    low=read(args.strong_low);den=read(args.strong_density);ref=read(args.strong_reference)
    source=read(args.source_panel);target=read(args.target_panel)
    meta=metadata_without_array(args.material,'panels')
    n,k=args.source_cell,args.target_cell
    if n==k or not 12<=n<=23 or not 12<=k<=23:raise ValueError('This entry checks a distinct shallow source/target pair')
    modes=list(range(2,93,2))
    if source['cell']!=n or target['cell']!=k or source['modes']!=modes or target['modes']!=modes:
        raise ValueError('Both complete real46 panel columns are required')
    if meta['cell']!=n:raise ValueError('The actual source material has another cell')
    for name in ('source_panel','target_panel'):
        path=str(getattr(args,name))
        if low['panel_hashes'].get(path)!=hashes[path]:raise ValueError('A paid real column provider changed')
    for name in ('strong_density','strong_reference'):
        if hashes[str(getattr(args,name))] not in low['input_hashes'].values():raise ValueError('The actual strong source/norm changed')
    if not all(den['gates'].values()) or not all(ref['checks'].values()):raise ValueError('The strong centre/material domain is unpaid')
    if source['input_hashes'].get(str(args.material))!=hashes[str(args.material)]:raise ValueError('The original completed flow used another real material panel set')
    origin=den['continuous_strip_origin']
    if origin['sha256'] not in meta['input_hashes'].values():raise ValueError('The exact continuous q strip is not the material one')
    profiles={row['cell']:row for row in low['source_profiles']}
    sn=ball(profiles[n]['sigma']);sk=ball(profiles[k]['sigma'])
    X=ball(den['rows'][n-12]['canonical_total_envelope'])
    rest=ball(profiles[n]['canonical_rest']).upper()
    tau_ref=ball(ref['cell_rows'][n-12]['tau']).lower()
    mu=ball(meta['mu']).lower();root=arb(12).sqrt()
    total=compact(low['gamma_upper']['corr'][k-12][n-12])
    B=ball(den['rows'][n-12]['B']).lower()
    if not X.lower()>0 or not mu>0 or not sn.lower()>0 or not sk.lower()>0 or not B>=120:
        raise ValueError('A positive true scale or the stated material coefficient domain is absent')
    # Retain only the needed complete positive edge before streaming panels.
    del low,den,ref
    masses={m:arb(0) for m in modes};panels=0;wmax=arb(0);sumrad=arb(0)
    for raw in iter_array(args.material,'panels'):
        radius=ball(raw['radius']);V=sn.upper()*ball(raw['V']).upper()
        tau=ball(raw['tau_range']);dr=ball(raw['radial_log_increment']).upper()
        wmax=max(wmax,ball(raw['w']).upper())
        if not tau_ref>=tau.upper() or not dr>=0:raise ValueError('The actual wide-centre or radial source interval changed')
        eps=(rest/X.lower()*(-2*(tau_ref-tau.upper())).exp()).upper()
        radial=(radius.upper()**4*V**2/(root*mu)*dr*eps).upper()
        sumrad=(sumrad+radial).upper()
        for m in modes:
            masses[m]=(masses[m]+radial*(-m*tau.lower()).exp()).upper()
        panels+=1
    if not panels>0 or not wmax<=arb(1)/2:raise ValueError('The full source panel set or w<=1/2 domain is unavailable')
    source_rows={row['mode']:row for row in source['rows']};target_rows={row['mode']:row for row in target['rows']}
    rows=[];maxrad=arb(0);worst=None
    for m in modes:
        sr,tr=source_rows[m],target_rows[m]
        if k>n:
            col=ball(sr['psi_Q_sup']).upper()
            out=(ball(tr['phi_physical_p_sup']).upper()+ball(tr['phi_physical_kappa_sup']).upper())/sk.lower()
        else:
            col=ball(sr['phi_Q_sup']).upper()
            out=(ball(tr['psi_physical_p_sup']).upper()+ball(tr['psi_physical_kappa_sup']).upper())/sk.lower()
        value=(ball(sr['mu_ratio']).upper()*out*col*masses[m]).upper()
        if value>maxrad:maxrad=value;worst=m
        rows.append(dict(mode=m,radial_material_source_integral=ball_record(masses[m]),
            source_column_sup=ball_record(col),target_physical_norm=ball_record(out),
            independent_radial_Green_upper=ball_record(value)))
    chosen=min(total,maxrad)
    near=(arb(5)/2*chosen+arb(2)/285*total).upper()
    low=(arb(5)/2*chosen+arb(2)/9*total).upper()
    result=dict(status='Independent real d1 corr Green edge paid from complete actual panels and whole-cell true columns',
        source_cell=n,target_cell=k,modes=modes,panels=panels,
        complete_mean_or_source_changed=False,new_ODE_integrations=0,new_radial_source_integrations=0,
        source_material='epsilon_s(r) * d1, d1=V_s^2/(r*w); canonical source mass is r^4*V_s^2/(sqrt12*mu)*epsilon_s*dr/r.',
        source_position_scope='All actual material panels retained. Only the source phi/psi column uses its proved whole-cell supremum, so this may be conservative.',
        combined_corr_upper=ball_record(total),independent_radial_corr_upper=ball_record(maxrad),
        chosen_radial_corr_upper=ball_record(chosen),worst_radial_mode=worst,
        lambda_corr_upper_reason='The old combined positive corr kernel also bounds its d_lambda-only restriction; it is not scaled by an integrated source fraction.',
        conditional_DQ_corr_low_from_near=ball_record(near),conditional_DQ_corr_low_from_low=ball_record(low),
        coefficient_scope='Uses the explicitly stated fixed-mass two-material bounds d1<=5/2, d_lambda<=2/285 for near input or2/9 for low input, under B>=120,w<=1/2. The old main kernel is not altered.',
        old_DQ_corr_upper=ball_record(3*total),ratio_new_near_to_old=ball_record(near/(3*total)),
        B_lower=ball_record(B),w_upper=ball_record(wmax),true_source_sigma=ball_record(sn),true_target_sigma=ball_record(sk),
        summed_radial_material_without_output_angle=ball_record(sumrad),rows=rows,
        input_hashes=hashes,source_sha256=digest(Path(__file__)),
        helper_hashes={name:digest(Path(__file__).with_name(name)) for name in
            ('closure_split_joint_io.py','closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py')},
        full213_matrix_or_joint_gate_paid=False,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='done',source_cell=n,target_cell=k,panels=panels,worst_mode=worst,
        log2_radial=str(maxrad.log()/arb(2).log()),log2_combined=str(total.log()/arb(2).log()),
        new_near_over_old=str(near/(3*total)),seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
