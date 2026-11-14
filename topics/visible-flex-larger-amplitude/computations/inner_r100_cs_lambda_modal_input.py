#!/usr/bin/env python3
"""Actual same-R100 inner auxiliary and transverse lift spectra, no new ODE.

All213 original cells and all46 true low modes are retained. The R121
cell12 canonical pair caps and the original R74 other-cell correction
balls are converted to the very same R42 physical B*p,kappa strong norm.
Both V_s and V'=S*V_s conventions are explicit. The transverse l1 source
has ONE shared budget: its common norm uses a maximum, not a sum of axes.
This is an input interface for the full head, not a new high-source bound.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

PINS={
 'bootstrap':('2026-11-13-inner-aux-cell12-spectral-bootstrap-r1.json.gz','490bbdaa71cbd14b4dab9fbf6ac820d72b895b7fc5664b8a3a2ff454bb63a1c6'),
 'reference':('2026-11-12-closure-newg-strong-m20-real-reference.json','d87a6862836c31f9cb72ed9b8ad74c0ee618797e45a83785c8206a83455233cb'),
 'family':('2026-11-12-root-anisotropic-auxiliary-family-r3.json.gz','4306f0641856e85a8390dee4c22271dbefe1c6c3c7934f9c9b9a1ec6195ad866'),
 'density':('2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'lifts':('2026-11-12-closure-strong-parameter-lifts-r1.json.gz','94db6f6e89e623d27b7661ac8c432335063c1dd9f8303d3cdab93d6751c54497'),
 'r100':('2026-11-13-root-r100-hybrid46-exact-ledger.json','7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9'),
}
MODES=list(range(2,93,2));CELLS=list(range(12,225));S=F(257,256);RT=F(1,32)


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p=Path(path);b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)


def exact(x,side='upper'):
    if isinstance(x,bool) or isinstance(x,float):raise TypeError('No float or Boolean bound')
    if isinstance(x,(int,str)):return F(x)
    if isinstance(x,list):return F(int(x[0]))*F(2)**int(x[1])
    if side in x:return exact(x[side],side)
    if 'upper_dyadic' in x:return exact(x['upper_dyadic'],side)
    if 'numerator' in x:return F(int(x['numerator']),int(x['denominator']))
    return F(int(x['mantissa']))*F(2)**int(x['binary_exponent'])


def up(x,bits=128):
    x=F(x)
    if x<0:raise ArithmeticError('Positive arithmetic only')
    if not x:return x
    e=x.numerator.bit_length()-x.denominator.bit_length()-bits+1
    q=F(2)**e;y=x/q
    ans=((y.numerator+y.denominator-1)//y.denominator)*q
    if ans<x:raise ArithmeticError('An upward rounding went inward')
    return ans


def pack(x):
    x=up(x);d=x.denominator
    if d&(d-1):raise ArithmeticError('Non-dyadic outward output')
    return [str(x.numerator),-(d.bit_length()-1)]


def fraction(x):return dict(numerator=str(x.numerator),denominator=str(x.denominator))


def exp_negative_upper(x):
    """For x>=0, reciprocal positive Taylor lower bound, then upward squares."""
    x=F(x)
    if x<0:raise ArithmeticError('A negative strip loss is not paid')
    reductions=0
    while x>F(1,2):x/=2;reductions+=1
    term=total=F(1)
    for k in range(1,33):term*=x/k;total+=term
    value=up(1/total)
    for _ in range(reductions):value=up(value*value)
    return min(F(1),value)


def save(path,obj):
    p=Path(path)
    if p.exists():raise FileExistsError(p)
    raw=(json.dumps(obj,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if p.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    if len(raw)>=5_000_000:raise ValueError('Repository artifact limit')
    p.write_bytes(raw)
    return dict(path=str(p),sha256=sha(p),bytes=len(raw))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--notes',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    a=ap.parse_args();started=time.monotonic();gates={};ids={};d={}
    def check(name,condition):
        if not condition:raise ArithmeticError(name)
        gates[name]=True
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if list(a.out_prefix.parent.glob(a.out_prefix.name+'-*')):raise FileExistsError(a.out_prefix)
    for key,(name,wanted) in PINS.items():
        p=a.notes/name;check('identity_'+key,sha(p)==wanted)
        d[key]=read(p);ids[key]=dict(path=str(p),sha256=wanted,bytes=p.stat().st_size)
    boot,ref,fam,den,lifts,chart=(d[k] for k in PINS)
    check('original_all_gates',boot['all_gates'] and fam['all_gates'] and chart['all_gates']
          and all(den['gates'].values()) and all(ref['checks'].values()))
    check('complete46_original_modes',ref['modes']==lifts['modes']==MODES
          and [r['mode'] for r in boot['final_modal_rows']]==MODES)
    check('complete213_original_cells',lifts['cells']==CELLS
          and all([r['cell'] for r in obj]==CELLS for obj in
                  (ref['cell_rows'],fam['auxiliary_rows'],den['rows'])))
    check('same_continuous_original_q_strip',lifts['continuous_strip_origin']['sha256']
          ==den['continuous_strip_origin']['sha256']=='0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9'
          and lifts['input_hashes']['notes/'+PINS['density'][0]]==PINS['density'][1])
    check('same_original_reference_and_family',fam['input_hashes']['notes/'+PINS['reference'][0]]==PINS['reference'][1]
          and boot['input_identities']['notes/'+PINS['family'][0]]['sha256']==PINS['family'][1]
          and boot['input_identities']['notes/'+PINS['reference'][0]]['sha256']==PINS['reference'][1])
    check('R100_exact_S_and_domain',exact(chart['constants']['S'])==exact(fam['envelope_factor'])==S
          and chart['domain']['product_modes']==MODES[:6]
          and chart['domain']['weighted_l1_modes']==MODES[6:])
    axes={row['mode']:row for row in fam['parameter_axes']}
    endpoints={row['mode']:row for row in ref['endpoint_rows']}
    chartrows=chart['rows']
    check('all46_R100_axis_rows',[row['mode'] for row in chartrows]==MODES)
    centres=[];cs_heights=[];r59_axes=[];r100_axes=[]
    for m,row in zip(MODES,chartrows):
        centre=exact(endpoints[m]['reference_Q'])
        check('same_exact_centre_'+str(m),centre==exact(row['original_centre']))
        if m in axes:
            check('same_R74_centre_'+str(m),centre==exact(axes[m]['exact_centre']))
        else:check('zero_remaining26_centres_'+str(m),centre==0)
        old_axis=F(2)**int(row['R59_exponent']);axis=exact(row['chosen_axis'])
        check('positive_axis_'+str(m),old_axis>0 and axis>0)
        if m<=12:
            check('same_six_product_axes_'+str(m),axis==exact(axes[m]['half_axis']))
        else:check('same40_transverse_axes_'+str(m),axis==old_axis)
        centres.append(centre);cs_heights.append(abs(centre)+(axis if m<=12 else F(0)))
        r59_axes.append(old_axis);r100_axes.append(axis)
    check('full_213_by46_actual_lifts',len(lifts['A_upper'])==213
          and all(len(row)==46 for row in lifts['A_upper']) and len(lifts['far_E_upper'])==46)
    rows=[];cell12=None
    for i,n in enumerate(CELLS):
        rr,fr,dr=ref['cell_rows'][i],fam['auxiliary_rows'][i],den['rows'][i]
        x=exact(rr['reference_X']);Xbar=exact(dr['canonical_total_envelope'])
        check('exact_fixed_positive_Xbar_'+str(n),Xbar>0 and Xbar==exact(dr['canonical_total_envelope'],'lower') and x>0)
        rho=exact(fr['nonlinear_radius_multiple']);alpha=exact(fr['new_total_linear_factor'])
        check('R74_full_envelope_'+str(n),(alpha+rho)*x<=S*Xbar and all(fr['gates'].values()))
        tau_ref=exact(rr['tau'],'lower');tau_hi=exact(dr['tau_inner']);tau_lo=exact(dr['tau_outer'],'lower')
        check('continuous_strip_under_reference_'+str(n),0<tau_lo<=tau_hi<=tau_ref
              and tau_ref<=exact(dr['certified_reference_tau']))
        ratio=x/(S*Xbar);gap=tau_ref-tau_hi;e2=exp_negative_upper(2*gap)
        angle=[];power=F(1)
        for m in MODES:power=up(power*e2);angle.append(power)
        A=list(map(exact,lifts['A_upper'][i]));linear=[up(A[j]*cs_heights[j]/S) for j in range(46)]
        error=[up(ratio*rho*angle[j]) for j in range(46)]
        complete=[up(linear[j]+error[j]) for j in range(46)]
        error_common=up(ratio*rho*e2)
        provenance='R74 exact canonical correction ball plus true R59/R42 physical linear columns'
        if n==12:
            # R121 serializes this chosen reference through its outward160bit
            # recorder. Its stored upper can be strictly larger than the
            # original exact192bit dyadic; use the larger one in the bridge.
            boot_x_upper=exact(boot['reference_x12'])
            check('R121_same_reference_x12_outward',boot_x_upper>=x and tau_ref==2
                  and boot['target_cell']==12 and boot['canonical_reference_strip']==2)
            boot_ratio=boot_x_upper/(S*Xbar)
            for j,br in enumerate(boot['final_modal_rows']):
                err=up(boot_ratio*exact(br['auxiliary_error_pair_mass_over_reference'])*angle[j])
                can=up(boot_ratio*exact(br['complete_field_pair_mass_over_reference'])*angle[j])
                error[j]=min(error[j],err)
                complete[j]=min(can,up(linear[j]+error[j]))
            error_common=min(error_common,up(boot_ratio*exact(boot['final_common_error_over_reference'])*e2))
            provenance='R121 final complete/error positive pair caps intersected with the same true physical linear columns'
        cs_common=min(F(1),up(sum(complete,F(0))),up(sum(linear,F(0))+min(error_common,sum(error,F(0)))))
        unit59=[up(A[j]*r59_axes[j]/S) for j in range(46)]
        unitT=[unit59[j] if j>=6 else F(0) for j in range(46)]
        lam=[up(RT*z) for z in unitT]
        lam_common=up(RT*max(unitT))
        base=[up(complete[j]+lam[j]) for j in range(46)]
        base_common=min(up(cs_common+lam_common),up(sum(base,F(0))))
        check('strict_positive_actual_common_rows_'+str(n),cs_common>0 and lam_common>0 and base_common>0)
        row=dict(cell=n,reference_x=fraction(x),original_Xbar=fraction(Xbar),R100_Xbar=fraction(S*Xbar),
            tau_reference_lower=fraction(tau_ref),tau_inner_upper=fraction(tau_hi),tau_outer_lower=fraction(tau_lo),
            canonical_to_R100_physical_ratio=fraction(ratio),strip_gap_lower=fraction(gap),
            decay_pair_factors=list(map(pack,angle)),
            Cs_linear_pair_caps=list(map(pack,linear)),Cs_correction_pair_caps=list(map(pack,error)),
            Cs_complete_pair_caps=list(map(pack,complete)),Cs_common_cap=pack(cs_common),
            Cs_correction_common_cap=pack(min(error_common,sum(error,F(0)))),
            all46_R59_unit_axis_lift_pairs=list(map(pack,unit59)),
            transverse_unit_axis_pairs=list(map(pack,unitT)),
            Lambda_pair_caps_at_radius1over32=list(map(pack,lam)),Lambda_common_cap_at_radius1over32=pack(lam_common),
            Cs_plus_Lambda_pair_caps=list(map(pack,base)),Cs_plus_Lambda_common_cap=pack(base_common),
            Cs_provenance=provenance,
            shared_parameter_budget='Lambda_m <= unitT_m*|d_m|/v_m, sum_T |d_m|/v_m<=1/32. Common norm <= max_T(unitT_m)/32; the per-mode full-radius caps must not be summed as an exact common mass.')
        rows.append(row)
        if n==12:cell12=row
    far=list(map(exact,lifts['far_E_upper']))
    far_unit=[up(far[j]*r100_axes[j]) if j>=6 else F(0) for j in range(46)]
    output=dict(schema='inner-r100-Cs-Lambda-modal-input-v1',scope=__doc__,author='/root/geometry_audit',
        source_sha256=sha(__file__),input_identities=ids,all_gates=all(gates.values()),gates=gates,
        modes=MODES,cells=CELLS,R100_envelope_scale=fraction(S),transverse_radius=fraction(RT),
        original_reference_centres=list(map(fraction,centres)),Cs_shallow_modulus_caps=list(map(fraction,cs_heights)),
        original_R59_axes=list(map(fraction,r59_axes)),R100_axes=list(map(fraction,r100_axes)),
        parameter_domain='Same R100 six complex original R74 product axes of radius1, and the40 transverse R59 axes sharing l1 radius1/32.',
        normalization='All field caps use physical (B*p,kappa_perp) strong pair norm divided by V_prime=S*V_s. Multiplication by S returns original R42 V_s units. B and the entire original q continuous tau(r) are unchanged. Positive real sine/cosine pair mass includes both signed Fourier halves.',
        C_S_is_low46_auxiliary=True,C_S_domain_contained_in_R121_R74=True,
        exact_original_continuous_strip_origin=lifts['continuous_strip_origin'],
        far_unit_axis_pairs_unscaled_by_S=list(map(pack,far_unit)),far_common_at_radius1over32=pack(RT*max(far_unit)),
        complete_auxiliary_far_already_in_R74_R121_Cs=True,full_head_correction_e_still_separate=True,
        full_head_source_or_high_trace_certified=False,new_solution_or_closed_surface_claimed=False,
        radial_integrations=0,ODE_Node_Green_calls=0,rows=rows,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    record=save(str(a.out_prefix)+'-all213.json.gz',output)
    mini=dict(schema='inner-r100-Cs-Lambda-cell12-v1',source_sha256=output['source_sha256'],parent=record,
        normalization=output['normalization'],parameter_domain=output['parameter_domain'],modes=MODES,
        R100_envelope_scale=fraction(S),transverse_radius=fraction(RT),row=cell12,
        complete_mean_inverse_and_full_head_e_must_still_be_paid=True)
    tiny=save(str(a.out_prefix)+'-cell12.json',mini)
    print(json.dumps(dict(event='same_R100_Cs_Lambda_input_finished',all_gates=output['all_gates'],gate_count=len(gates),
        full=record,cell12=tiny,Cs12=float(exact(cell12['Cs_common_cap'])),Lambda12=float(exact(cell12['Lambda_common_cap_at_radius1over32'])),
        elapsed_seconds=output['elapsed_seconds'],peak_rss_kib=output['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
