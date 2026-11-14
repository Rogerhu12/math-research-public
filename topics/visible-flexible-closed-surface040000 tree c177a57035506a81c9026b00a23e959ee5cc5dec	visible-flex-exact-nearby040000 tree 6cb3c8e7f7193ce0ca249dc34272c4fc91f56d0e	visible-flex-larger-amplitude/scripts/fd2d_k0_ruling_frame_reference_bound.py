#!/usr/bin/env python3
"""Strict normal error relative to E=e1 cross e2, without a quotient jet.

E need not be exactly unit. For C0=G cross X_phi=a*h*E+G cross C,
|N0-E/|E||<=2|G| |C|/|C0| and ||E|-1|<=||M^T M-I||.
The existing whole-ruling normal variation then gives the stated bound.
"""
import argparse,json,time
from pathlib import Path
from flint import arb,ctx
from fd2d_k0_ruling_metric_convolution import load,digest,from_bounds
from fd2d_k0_ruling_angular_certificate import bounds


def main():
    root=Path(__file__).resolve().parent.parent;ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--variation',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-normal-variation-02.json')
    ap.add_argument('--metric',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-metric-convolution-01.json')
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();ctx.prec=192
    var,met=load(args.variation),load(args.metric)
    if not var['passed'] or not met['passed'] or var['metric_sha256']!=digest(args.metric) or var['inlet_sha256']!=met['inlet_sha256']:
        raise ValueError('Normal/metric certificate identity mismatch')
    H=from_bounds(met['frame_Gram_operator_error_upper']).upper();C=from_bounds(met['C_vector_upper']).upper()
    if not H<1:raise ValueError('Frame cross nonvanishing is not paid')
    epsN=from_bounds(var['actual_normal_variation_global_upper']).upper();inlet=arb(0)
    for row in var['boxes']:
        G=from_bounds(row['G_norm_upper']).upper();area=from_bounds(row['whole_ruling_area_lower']).lower()
        if not area>0:raise ValueError('Actual normal denominator is not paid')
        inlet=max(inlet,(2*G*C/area).upper())
    total=(epsN+inlet+H).upper()
    report=dict(schema='fd2d-actual-normal-relative-to-unnormalized-frame-cross-v1',actual_execution=True,
        source_sha256=digest(__file__),inlet_sha256=var['inlet_sha256'],metric_sha256=digest(args.metric),normal_variation_sha256=digest(args.variation),
        reference_vector='E(phi)=e1(phi) cross e2(phi), from the complete finite Cartesian Fourier fields',
        reference_is_assumed_unit=False,exact_frame_or_developability_assumed=False,
        whole_ruling_normal_variation_upper=bounds(epsN),inlet_normalized_reference_error_upper=bounds(inlet),reference_length_error_upper=bounds(H),
        actual_normal_to_frame_cross_global_upper=bounds(total),all_angles_and_all_original_rulings_covered=True,
        passed=True,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),inlet_reference_error_display=float(inlet),total_error_display=float(total),seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
