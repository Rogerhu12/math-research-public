#!/usr/bin/env python3
"""Decompose one saved actual R165 value packet, without F/J reevaluation."""
import argparse
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_packet_checkpoint import load_actual_packet


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-summary',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    baseline=json.loads(args.baseline_summary.read_text())
    described=baseline['value_packet_manifest']
    actual=identity(described['path'])
    if (actual['sha256'],actual['bytes'])!=(described['sha256'],described['bytes']):
        raise ValueError('Saved actual baseline packet changed')
    packet=load_actual_packet(described['path'],expected_binding=baseline['binding'])
    data=packet['data'];residual=np.asarray(packet['residual'])
    square=lambda x:float(np.asarray(x).ravel()@np.asarray(x).ravel())
    total=square(residual);raw=square(data['original_residual'])
    interior=data['interior_actual_constraints']
    squares={
        'retained_average_Codazzi':square(data['codazzi_cells']),
        'retained_node_Gauss':square(data['projected_gauss']),
        'retained_selected_interior_Gauss':float(interior['retained_residual_l2'])**2,
        'node_curvature_guidance':float(data['curvature_merit']['residual_l2'])**2,
        'high_node_Gauss':float(data['high_gauss_merit']['residual_l2'])**2,
        'high_average_Codazzi':float(data['high_codazzi_merit']['residual_l2'])**2,
        'high_selected_interior_Gauss':float(interior['high_residual_l2'])**2,
        'selected_interior_curvature_guidance':float(interior['curvature_residual_l2'])**2}
    squares['remaining_raw_boundary_and_gap']=raw-sum(squares[k] for k in (
        'retained_average_Codazzi','retained_node_Gauss','retained_selected_interior_Gauss'))
    report=dict(schema='fd2d-saved-actual-value-energy-breakdown-v1',
        source=identity(__file__),baseline_summary=identity(args.baseline_summary),
        actual_value_manifest=actual,input_field_sha256=baseline['binding']['input_npz_sha256'],
        mathematical_settings=baseline['binding']['mathematical_settings'],
        objective_norm=float(np.linalg.norm(residual)),objective_squared=total,
        components={k:dict(squared=v,l2=float(np.sqrt(max(0.,v))),
                          fraction=v/total if total else 0.) for k,v in squares.items()},
        sum_minus_total=sum(squares.values())-total,
        remaining_raw_is_difference_of_saved_squared_norms=True,
        actual_F_or_J_recomputed=False,continuous_certificate=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,allow_nan=False))


if __name__=='__main__':main()
