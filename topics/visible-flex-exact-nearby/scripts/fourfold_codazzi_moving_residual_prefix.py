#!/usr/bin/env python3
"""Save already-completed exact closed rows without repeating their arithmetic."""
import argparse,gzip,hashlib,json
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--source',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();ctx.prec=192
    if a.out.exists():raise FileExistsError('preserve the exact completed prefix record')
    raw=a.source.read_bytes();old=json.loads(gzip.decompress(raw));rows=old['rows'][:8]
    if len(rows)!=8 or old['failure'] is not None or [r['index'] for r in rows]!=list(range(8)):raise ValueError('eight complete valid rows are required')
    upper=lambda field:max(box_from_record(r[field]).upper() for r in rows).upper()
    residual=[max(box_from_record(r['complete_residual_A0'][k]).upper() for r in rows).upper() for k in ('U','V')]
    gap=min(box_from_record(r['absolute_v_gap']).lower() for r in rows).lower();kappa=upper('candidate_principal_abs_upper')
    source_C=max(box_from_record(r['complete_inverse_coordinate_and_physical_residual']['physical_C_residual_C0']).upper() for r in rows).upper()
    gates=dict(complete_U_below_2058e11=residual[0]<arb('0.00000002058'),complete_V_below_9116e12=residual[1]<arb('0.000000009116'),
      true_v_gap_above_0090153=gap>arb('0.090153'),candidate_kappa_below_11092579=kappa<arb('11.092579'),
      full_physical_C_source_below_000002870=source_C<arb('0.00002870'),all_cubic_modes_retained=all(r['exact_angular_support_index']==96 for r in rows),
      complete_intermediate_degree_and_mean=old['complete_intermediate_primitive_support']==64 and old['full_mean_and_nonlocal_primitive_retained'])
    doc=dict(kind='selected_eight_actual_closed_moving_residual_rows_without_recomputation',complete=all(gates.values()),
      whole_body_complete=False,source_identity=old['identity'],source_checkpoint_path=str(a.source),
      source_checkpoint_snapshot_sha256=hashlib.sha256(raw).hexdigest(),selected_exact_interval=[rows[0]['interval'][0],rows[-1]['interval'][1]],
      selected_count=8,total_required_partition_cells=old['total_partition_cells'],rows=rows,gates=gates,
      residual_A0=[record(z) for z in residual],minimum_v_gap=record(gap),candidate_kappa=record(kappa),
      physical_C_source_C0=record(source_C),producer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      all_interface_jumps_and_remaining_closed_rows_still_required=True,nonlinear_solution_proved=False,final_geometry_proved=False)
    a.out.write_bytes(gzip.compress((json.dumps(doc,indent=2)+'\n').encode(),mtime=0));print({k:v for k,v in doc.items() if k not in ('rows','source_identity')})
    if not doc['complete']:raise RuntimeError('a true closed-prefix gate failed')

if __name__=='__main__':main()
