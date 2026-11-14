#!/usr/bin/env python3
"""Bind a complete R88 cap-energy proof to the actual R95 cut contact.

The finite input modes and regular mean are retained. The saved hybrid map
has every exact dual output through the interior bandwidth, replacing only
the rigorously enclosed low/regular rows by their tighter true-cap center.
An infinite-output H^(-1/2) error is paid using the complete dual energy gap.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np
from flint import arb,acb,acb_mat,ctx

from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_interval import FiniteTrial,sha
from fourfold_phase_cap_energy_collect import adjoint,hermitian_norm_bound
from fourfold_phase_cap_wiener_cover import read_json,write_json


def finite_matrix(values):
    return acb_mat([[acb(float(z.real),float(z.imag)) for z in row] for row in values])


def weighted_output_norm(values,weights):
    """Directed norm for an exact finite matrix with exact rational weights."""
    nout,nin=values.shape
    result=acb_mat(nin,nin)
    for row,weight in zip(values,weights):
        w=arb(weight[0])/weight[1]
        for i in range(nin):
            first=acb(float(row[i].real),float(-row[i].imag))
            for j in range(nin):
                result[i,j]+=w*first*acb(float(row[j].real),float(row[j].imag))
    # The exact Gram matrix is positive Hermitian. Its trace and its
    # maximum absolute row sum independently bound its largest eigenvalue.
    trace=sum((result[i,i].real.upper() for i in range(nin)),arb(0)).upper()
    row_sum=max(sum((abs(result[i,j]).upper() for j in range(nin)),arb(0)).upper()
                for i in range(nin))
    bound=min(trace,row_sum)
    if not bound>=0:raise ValueError('the complete finite Gram bound is negative')
    return bound.sqrt().upper(),dict(trace_upper=ball_record(trace),row_sum_upper=ball_record(row_sum))


def check_recorded_files(values,source_directory=False):
    for name,digest in values.items():
        path=Path(__file__).with_name(name) if source_directory else Path(name)
        if sha(path)!=digest:raise ValueError('a frozen input to the contact changed: '+name)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--energy',type=Path,default=Path('notes/2026-11-12-actual-cap-compression-energy.json'))
    ap.add_argument('--lift',type=Path,default=Path('notes/2026-11-12-actual-quarter-cut-cap-lift.json'))
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    energy,lift=read_json(args.energy),read_json(args.lift)
    if not energy.get('complete'):
        raise ValueError('a whole-cap contact needs the complete actual body, graft and tail energies')
    if not lift.get('complete') or lift['exact_physical_interface']!='1/4':
        raise ValueError('the real r=1/4 full-angle lift is incomplete or uses another port')
    expected=('fourfold_phase_cap_energy_collect.py','fourfold_phase_cut_cap_lift.py')
    for record,name in zip((energy,lift),expected):
        if record['source_sha256']!=sha(Path(__file__).with_name(name)):
            raise ValueError('a completed cap/contact producer changed: '+name)
    if (energy['object_sha256']!=lift['object_sha256']
        or energy['exact_delta_fraction']!=lift['exact_delta_fraction']
        or energy['exact_radial_cover']!=['1/4','25/8']):
        raise ValueError('the complete energy and lift do not describe the same actual cap')
    check_recorded_files(lift['input_sha256'])
    check_recorded_files(lift['dependency_sha256'],True)
    for item in energy['input_reports']:
        if sha(item['path'])!=item['sha256']:
            raise ValueError('an actual complete body/graft proof changed')
    trial_path=Path(energy['exact_trial_report']['path'])
    if sha(trial_path)!=energy['exact_trial_report']['sha256']:
        raise ValueError('the complete energy changed its exact trial')
    trial=FiniteTrial(trial_path)
    if (trial.report['object_sha256']!=energy['object_sha256']
        or lift['input_sha256'].get(str(trial_path))!=sha(trial_path)):
        raise ValueError('the finite input space or actual graph differs')
    arrays=Path(energy['arrays']['path'])
    if sha(arrays)!=energy['arrays']['sha256']:
        raise ValueError('the complete cap energy matrices changed')
    with np.load(arrays,allow_pickle=False) as saved:
        E=saved['primal_energy_center'].copy()
        D=saved['dual_energy_center'].copy()
        C=saved['actual_cap_compression_center'].copy()
        T=saved['exact_boundary_T'].copy()
    if any(z.shape!=(trial.d,trial.d) for z in (E,D,C,T)):
        raise ValueError('wrong retained finite energy matrix size')
    Eerror=arb(energy['primal_total_operator_error']['ball']).upper()
    Derror=arb(energy['dual_total_operator_error']['ball']).upper()
    gap=finite_matrix(E)-finite_matrix(T)-adjoint(finite_matrix(T))+finite_matrix(D)
    gapnorm,powers=hermitian_norm_bound(gap)
    Delta=(gapnorm+Eerror+Derror).upper()
    stored_Delta=arb(energy['full_actual_primal_dual_gap_upper']['ball']).upper()
    # Both directed recomputation and the completed producer's outward
    # record are valid bounds; keep the larger to avoid formatting ambiguity.
    Delta=max(Delta,stored_Delta)
    if not Delta>=0:raise ValueError('a true full primal/dual defect bound must be nonnegative')
    low_radius=arb(energy['true_cap_compression_operator_radius']['ball']).upper()
    if not low_radius>=0:raise ValueError('the retained cap radius is negative')
    table={row['physical_cutoff']:row for row in lift['contact_constants']['high_trace_table']}
    if trial.B not in table or trial.M not in table:
        raise ValueError('the actual contact table misses the selected physical cut')
    dual=lift['exact_dual_boundary_output']
    if (dual['physical_modes']!=list(range(-trial.M,trial.M+1))
        or not dual['regular_mean_flux_last'] or dual['high_modes_exactly_zero_above']!=trial.M):
        raise ValueError('the saved exact full dual trace has the wrong physical basis')
    J=np.array([[complex(*z) for z in row] for row in dual['matrix_binary64']],complex)
    if J.shape!=(trial.n+1,trial.d):raise ValueError('wrong full finite dual trace size')
    expected_J=np.zeros_like(J)
    expected_J[trial.nonzero]=-trial.flux[:trial.nn]
    expected_J[trial.M]=-trial.flux[trial.nodes*trial.nn]
    expected_J[-1]=trial.flux[trial.nodes*trial.nn]
    if not np.array_equal(J,expected_J):
        raise ValueError('the exact dual boundary output differs from the saved divergence-free flux')
    indices=list(range(trial.M-trial.B,trial.M+trial.B+1))+[trial.n]
    if not np.array_equal(J[indices],T.conj().T):
        raise ValueError('the retained dual output is not the exact adjoint of the boundary pairing T')
    hybrid=J.copy();hybrid[indices]=C
    if not np.all(hybrid[:,trial.B]+hybrid[:,-1]==0):
        raise ValueError('the selected hybrid center lost the exact common-constant input kernel')
    e_high=arb(table[trial.B]['full_cap_high_trace_extension_energy']['ball']).upper()
    hybrid_error=(low_radius**2+e_high*Delta).sqrt().upper()
    original_regular=arb(lift['contact_constants']['regular_mean_extension_energy']['ball']).upper()
    trial_regular=(arb(float(E[-1,-1].real))+Eerror).upper()
    if not trial_regular>0:raise ValueError('the complete regular-column trial energy is not positive')
    regular=min(original_regular,trial_regular)
    e_nonmean=arb(table[0]['full_cap_high_trace_extension_energy']['ball']).upper()
    full_dual_error=((e_nonmean+2*regular)*Delta).sqrt().upper()
    weights=[(1,1) if k==0 else (1,4*abs(k)) for k in range(-trial.M,trial.M+1)]+[(1,1)]
    hybrid_norm,norm_record=weighted_output_norm(hybrid,weights)
    high_rows=[]
    for N in sorted(table):
        selected=[i for i,k in enumerate(range(-trial.M,trial.M+1)) if abs(k)>N]
        finite=J[selected] if selected else np.zeros((0,trial.d),complex)
        w=[weights[i] for i in selected]
        finite_norm,finite_proof=weighted_output_norm(finite,w)
        eN=arb(table[N]['full_cap_high_trace_extension_energy']['ball']).upper()
        error=(eN*Delta).sqrt().upper()
        high_rows.append(dict(physical_cutoff=N,
            exact_dual_high_output_norm_upper=ball_record(finite_norm),
            exact_finite_norm_proof=finite_proof,
            true_high_output_minus_dual_error=ball_record(error),
            true_high_output_norm_upper=ball_record((finite_norm+error).upper()),
            finite_dual_high_trace_exactly_zero=not selected))
    out_arrays=args.out.with_suffix('.npz')
    out_arrays.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(out_arrays,physical_output_modes=np.arange(-trial.M,trial.M+1),
        full_dual_output_center=J,full_hybrid_output_center=hybrid,
        retained_true_cap_center=C,exact_boundary_pairing_T=T)
    result=dict(kind='true_full_cap_output_for_retained_physical_inputs',complete=True,
        source_sha256=sha(__file__),object_sha256=energy['object_sha256'],
        exact_delta_fraction=energy['exact_delta_fraction'],exact_physical_interface='1/4',
        input_reports={str(p):sha(p) for p in (args.energy,args.lift,trial_path,arrays)},
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_cap_energy_collect.py','fourfold_phase_cut_cap_lift.py',
            'fourfold_phase_cap_energy_interval.py','fourfold_phase_beta_interval.py')},
        bits=args.bits,finite_input_modes=trial.B,finite_dual_output_modes=trial.M,
        regular_mean_and_flux_retained=True,
        input_norm='Euclidean norm of the physical modes -B..B and the regular mean; the bound also holds for the larger finite H^(1/2) input norm.',
        output_norm='Physical H^(-1/2): mean weight1, nonmean squared weights1/abs(4k), plus regular flux weight1.',
        complete_primal_dual_gap_upper=ball_record(Delta),
        recomputed_gap_norm_power_bounds=powers,
        retained_true_cap_compression_radius=ball_record(low_radius),
        full_hybrid_output_error=ball_record(hybrid_error),
        full_exact_dual_output_error=ball_record(full_dual_error),
        improved_regular_mean_energy=ball_record(regular),
        complete_regular_trial_column_energy=ball_record(trial_regular),
        exact_hybrid_center_common_constant_kernel=True,
        finite_hybrid_output_norm_upper=ball_record(hybrid_norm),
        finite_hybrid_norm_proof=norm_record,
        true_full_output_norm_upper=ball_record((hybrid_norm+hybrid_error).upper()),
        physical_high_output_bounds=high_rows,
        arrays=dict(path=str(out_arrays),sha256=sha(out_arrays),bytes=out_arrays.stat().st_size),
        scope=['Full uncompressed exterior cap output, including all omitted angular outputs, only for the stated finite input columns.',
               'The hybrid low and regular rows use the complete retained DN enclosure; the orthogonal high rows use the true full dual-gap contact.',
               'This is the r=1/4 physical H^(1/2) port. No turning-root, canonical-angle, full feedback inverse, or nonlinear zero is asserted.'])
    write_json(args.out,result)
    print(json.dumps(dict(complete=True,full_hybrid_output_error=result['full_hybrid_output_error'],
        complete_primal_dual_gap_upper=result['complete_primal_dual_gap_upper'],
        improved_regular_mean_energy=result['improved_regular_mean_energy'],
        true_full_output_norm_upper=result['true_full_output_norm_upper']),indent=2),flush=True)


if __name__=='__main__':main()
