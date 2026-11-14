#!/usr/bin/env python3
"""True r=1/4 exterior-cap lifts and full-boundary dual-gap contact.

The boundary norm is physical H^(1/2), not the turning-root H^(1/3).
All body frequencies remain in the harmonic solution. A short physical
Fourier ramp is only a competitor. The regular mean port is retained.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb,acb,ctx

from fourfold_phase_beta_bulk_box import CBox,Box
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_interval import FiniteTrial,sha
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_phase_cap_vector_germs import VectorScaledBodyForm
from fourfold_phase_cap_wiener_cover import read_json,write_json


def real_form_bound(target,left,right):
    # sigma=0 still includes every real angular grid gap in unit_fields.
    # All true scalar, tangent and primitive quantities are real here.
    parts=target.form_parts(acb(real_interval(left,right)),arb(0))
    D,M,W,H,Z,K=[CBox(parts[name].real) for name in ('D','M','W','H','Z','K')]
    alpha=Z*Z*D/(H*H)
    drift=-M/D
    kappa=Z*Z*W*W*K/(D*H*H)
    values=[alpha,alpha*drift,alpha*drift*drift+kappa]
    if any(not np.all(np.isfinite(value.magnitude_upper())) for value in values):
        raise ValueError('a true real all-angle form denominator is unresolved')
    alow=arb(float(np.min(alpha.real.lo)))
    klow=arb(float(np.min(kappa.real.lo)))
    if not min(alow,klow)>0:
        raise ValueError('the true real all-angle form is not separated positive')
    # Pointwise Gershgorin bound, then the complete closed angular cover.
    off=Box(values[1].magnitude_upper())
    first=values[0].real+off
    second=values[2].real+off
    upper=arb(float(max(np.max(first.hi),np.max(second.hi))))
    if not upper>0:raise ValueError('nonpositive real form upper bound')
    return dict(matrix_upper=ball_record(upper),
        alpha_lower=ball_record(alow),kappa_lower=ball_record(klow),
        exact_alpha_upper=str(Fraction(float(np.max(alpha.real.hi)))),
        complete_component_moduli=[ball_record(arb(float(np.max(v.magnitude_upper()))))
                                   for v in values])


def contact_constants(matrix_upper,length,whole_matrix_upper,rows):
    M,d=matrix_upper,exact_arb(length)
    exterior_length=arb(23)/8
    global_regular=(whole_matrix_upper/exterior_length).upper()
    # On each exact closed interval choose e'(r)=1/(J*A_i), where
    # A_i is its exact upper bound on B11 and J=sum length_i/A_i.
    # This is a continuous piecewise-affine, angle-independent competitor.
    # It equals zero at the cut and one beyond the local window, so its
    # true Robin form vanishes. Its entire energy is at most 1/J.
    resistance=sum(((Fraction(row['exact_radial_interval'][1])
        -Fraction(row['exact_radial_interval'][0]))/Fraction(row['exact_alpha_upper'])
        for row in rows),Fraction(0))
    if resistance<=0:raise ValueError('the local regular-mean competitor has no positive resistance')
    local_regular=exact_arb(1/resistance).upper()
    regular=min(global_regular,local_regular)
    table=[]
    for N in (0,4,16,32,64,128,256,1024):
        frequency=arb(4*(N+1))
        z=min(arb(1),(d*frequency).lower())
        energy=(M*(1/z+z/3)).upper()
        table.append(dict(physical_cutoff=N,frequency_lower=4*(N+1),
            full_cap_high_trace_extension_energy=ball_record(energy),
            full_cap_high_flux_contact=ball_record(energy.sqrt().upper()),
            full_cap_high_flux_and_regular_contact=ball_record((energy+regular).sqrt().upper())))
    nonmean=arb(table[0]['full_cap_high_trace_extension_energy']['ball']).upper()
    return dict(exact_finite_exterior_length='23/8',
        complete_physical_trace_norm='abs(a0)^2 + sum_{k!=0} abs(4*k)*abs(a_k)^2',
        exact_local_mean_resistance=str(resistance),
        local_piecewise_mean_extension_energy=ball_record(local_regular),
        global_linear_mean_extension_energy=ball_record(global_regular),
        regular_mean_extension_energy=ball_record(regular),
        regular_flux_contact=ball_record(regular.sqrt().upper()),
        all_boundary_and_regular_contact=ball_record((nonmean+2*regular).sqrt().upper()),
        constant_pair_kernel='left constant a0=1 and regular mean xi=1',
        high_trace_table=table)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--trial',type=Path,default=Path('notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    ap.add_argument('--partition',type=Path,default=Path('data/cap_physical4_energy/body_native_0250_0800_narrow/element_000.json.gz'))
    ap.add_argument('--closed-exterior',type=Path,default=Path('notes/2026-11-12-actual-closed-approximate-exterior.json'))
    ap.add_argument('--bits',type=int,default=160)
    ap.add_argument('--primitive-nodes',type=int,default=256)
    ap.add_argument('--angles',type=int,default=1024)
    ap.add_argument('--max-depth',type=int,default=10)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec,ctx.cap=args.bits,4
    wall,cpu=time.monotonic(),time.process_time()
    trial=FiniteTrial(args.trial);part=read_json(args.partition)
    if (not part['complete'] or part['identity']['object_sha256']!=trial.report['object_sha256']
        or part['identity']['trial_report_sha256']!=sha(args.trial)
        or part['identity']['exact_trial_arrays']!=trial.report['arrays']):
        raise ValueError('the completed partition belongs to another actual trial/object')
    for name,value in part['identity']['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=value:
            raise ValueError('the complete partition dependency changed: '+name)
    left,right=map(Fraction,part['exact_radial_interval'])
    if left!=Fraction(1,4) or not left<right<=3:
        raise ValueError('this lift must start at the actual r=1/4 interface')
    intervals=sorted((list(map(Fraction,row['exact_radial_interval'])) for row in part['intervals']))
    cursor=left
    for a,b in intervals:
        if a!=cursor or not a<b:raise ValueError('partition gap or overlap')
        cursor=b
    if cursor!=right:raise ValueError('the complete partition misses its final endpoint')
    obj=json.loads(trial.object_path.read_text())
    closed=json.loads(args.closed_exterior.read_text())
    if not closed['complete']:raise ValueError('the true global exterior bound is incomplete')
    for key,slot in (('origin_inputs_sha256','origin_inputs'),('direction_sha256','direction')):
        if closed[key]!=obj[slot]['sha256']:raise ValueError('the global exterior uses a different actual family')
    delta=Fraction(trial.report['exact_delta_fraction'])
    pminus,pplus=map(Fraction,closed['exact_parameter_interval'])
    if not pminus<=delta<=pplus:raise ValueError('the true graph is outside the global exterior certificate')
    if closed['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_closed_approximate_exterior.py')):
        raise ValueError('the complete exterior producer changed')
    for name,value in closed['input_sha256'].items():
        if sha(name)!=value:raise ValueError('the complete exterior input changed: '+name)
    MG=arb(closed['complete_finite_positive_operator']['matrix_upper']['ball']).upper()
    target=VectorScaledBodyForm(trial.object_path,args.primitive_nodes,args.angles,
        arb('.003'),arb('.0025'),arb('.32'))
    common=common_cells(target);rows=[];rejected=[];failed=[]
    report=dict(kind='true_quarter_cut_full_cap_lift_and_dual_gap_contact',
        complete=False,source_sha256=sha(__file__),
        object_sha256=trial.report['object_sha256'],exact_delta_fraction=str(delta),
        input_sha256={str(p):sha(p) for p in (args.trial,args.partition,args.closed_exterior)},
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_cap_energy_interval.py','fourfold_phase_cap_scaled_body.py',
            'fourfold_phase_cap_vector_germs.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_beta_affine.py')},
        exact_physical_interface='1/4',exact_lift_window=[str(left),str(right)],
        primitive_nodes=args.primitive_nodes,angular_nodes=args.angles,bits=args.bits,
        intervals=rows,rejected=rejected,failed=failed,
        whole_shear_form_matrix_upper=ball_record(MG),
        scope='Full uncompressed cap from r=1/4 through the true infinite Robin tail. Physical H^(1/2) cut trace and regular mean retained; no turning-root H^(1/3) constant is transferred.')
    def save():
        report['CPU_seconds']=time.process_time()-cpu
        report['wall_seconds']=time.monotonic()-wall
        write_json(args.out,report)
    for a,b in intervals:
        k=bisect_right(common,(a+b)/2)-1
        if not common[k]<=a<b<=common[k+1]:
            raise ValueError('a coefficient interval crosses an actual scalar common knot')
        target.set_cell(common[k],common[k+1])
        pending=[(a,b,0)]
        while pending:
            lo,hi,depth=pending.pop()
            try:
                bounds=real_form_bound(target,lo,hi)
                rows.append(dict(exact_radial_interval=[str(lo),str(hi)],
                    actual_common_span=list(map(str,target.cell)),subdivision_depth=depth,**bounds))
            except (ValueError,ZeroDivisionError) as exc:
                row=dict(exact_radial_interval=[str(lo),str(hi)],depth=depth,reason=str(exc))
                if depth==args.max_depth:failed.append(row)
                else:
                    rejected.append(row);mid=(lo+hi)/2
                    pending.extend([(mid,hi,depth+1),(lo,mid,depth+1)])
            save()
        if failed:break
    rows.sort(key=lambda row:Fraction(row['exact_radial_interval'][0]));cursor=left
    for row in rows:
        lo,hi=map(Fraction,row['exact_radial_interval'])
        if lo!=cursor:break
        cursor=hi
    report['complete']=not failed and cursor==right
    if not report['complete']:
        save();raise SystemExit('the real lift coefficient cover is incomplete')
    M=max(arb(row['matrix_upper']['ball']).upper() for row in rows)
    report['local_physical_matrix_upper']=ball_record(M)
    report['contact_constants']=contact_constants(M,right-left,MG,rows)
    # This is the entire exact dual boundary output, not just its retained
    # 10-by-10 compression. All modes beyond the interior M vanish exactly.
    Pleft=np.zeros((trial.n,trial.d),complex)
    Pleft[trial.nonzero]=trial.flux[:trial.nn]
    Pleft[trial.M]=trial.flux[trial.nodes*trial.nn]
    boundary=np.vstack((-Pleft,Pleft[trial.M:trial.M+1]))
    report['exact_dual_boundary_output']=dict(
        physical_modes=list(range(-trial.M,trial.M+1)),regular_mean_flux_last=True,
        matrix_binary64=[[[float(z.real),float(z.imag)] for z in row] for row in boundary],
        high_modes_exactly_zero_above=trial.M,
        is_adjoint_of_compressed_T_on_retained_rows=True)
    report['dual_gap_transfer']=dict(full_actual_trial_gap_paid=False,
        required_gap='Delta >= norm(Etrue - T - T* + Dtrue), including all body, graft and true tail energies',
        complete_output_error='norm(DN_true*g - exact_dual_boundary_output*g)_(H^-1/2 plus regular) <= all_boundary_and_regular_contact*sqrt(Delta)*norm(g)_2',
        high_output_when_N_ge_interior_M='norm(P_N DN_true*g)_Hdot^-1/2 <= high_flux_contact*sqrt(Delta)*norm(g)_2',
        no_current_full_gap_number='The entire body energy is still being integrated separately.')
    save()
    print(json.dumps(dict(complete=True,local_matrix_upper=report['local_physical_matrix_upper'],
        contact_constants=report['contact_constants'],CPU_seconds=report['CPU_seconds'],
        wall_seconds=report['wall_seconds']),indent=2),flush=True)


if __name__=='__main__':main()
