#!/usr/bin/env python3
"""Check full derivative coverage and propagate a point beta to a true family."""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_combine import stored_ball,cover_rows
from fourfold_phase_beta_parameter_derivative import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--center-object",type=Path,required=True)
    ap.add_argument("--center-beta",type=Path,required=True)
    ap.add_argument("--collar",type=Path,required=True)
    ap.add_argument("--parts",type=Path,nargs="+",required=True)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args();ctx.prec=224
    here=Path(__file__).parent
    definition,origin,direction,center=load_definition(args.center_object)
    collar=json.loads(args.collar.read_text())
    collar_source=here/"fourfold_phase_beta_derivative_collar.py"
    finish_source=here/"fourfold_phase_beta_derivative_collar_finish.py"
    core_source=here/"fourfold_phase_beta_parameter_derivative.py"
    accepted_collar_sources={sha(collar_source):str(collar_source),sha(finish_source):str(finish_source)}
    if (collar.get("kind")!="uniform_true_fixed_r_parameter_derivative_collar"
            or not collar.get("complete") or collar["source_sha256"] not in accepted_collar_sources
            or collar["derivative_core_sha256"]!=sha(core_source)):
        raise ValueError("true derivative collar or its paid source is incomplete")
    if collar["source_sha256"]==sha(finish_source):
        cp=Path(collar["coefficient_checkpoint_path"])
        if (collar["coefficient_kernel_sha256"]!=sha(collar_source)
                or sha(cp)!=collar["coefficient_checkpoint_sha256"]):
            raise ValueError("changed derivative coefficient checkpoint")
    half_width=Fraction(collar["exact_parameter_half_width"])
    identity=dict(center_object_sha256=sha(args.center_object),
        origin_inputs_sha256=sha(origin),direction_sha256=sha(direction),
        exact_center_parameter=str(center),exact_parameter_half_width=str(half_width),
        exact_parameter_interval=[str(center-half_width),str(center+half_width)])

    def check_identity(report):
        for key,value in identity.items():
            if report[key]!=value:
                raise ValueError("parameter identity mismatch: "+key)
        for name,digest in report["dependency_sha256"].items():
            if sha(here/name)!=digest:
                raise ValueError("changed analytic dependency: "+name)

    check_identity(collar)
    point=json.loads(args.center_beta.read_text())
    if (point.get("kind")!="complete_exact_affine_beta_and_D5_norm_grid"
            or not point.get("complete") or point["object_sha256"]!=sha(args.center_object)
            or Fraction(point["exact_delta_fraction"])!=center
            or point["source_sha256"]!=sha(here/"fourfold_phase_beta_affine_combine.py")):
        raise ValueError("center beta does not certify the same exact affine point")
    source_names=["fourfold_phase_beta_derivative_bulk.py","fourfold_phase_beta_derivative_bulk_refined.py"]
    source_map={sha(here/name):name for name in source_names}
    cut=Fraction(collar["fixed_cut"])
    parts=[];waist=None
    for path in args.parts:
        part=json.loads(path.read_text());check_identity(part)
        if (part.get("kind")!="uniform_true_fixed_r_parameter_derivative_bulk"
                or part["source_sha256"] not in source_map
                or part["derivative_core_sha256"]!=sha(core_source)
                or part["root_derivative_report_sha256"]!=collar["root_derivative_report_sha256"]
                or part["center_collar_sha256"]!=collar["center_collar_sha256"]
                or Fraction(part["fixed_cut"])!=cut):
            raise ValueError("bulk derivative source, root or cut differs")
        w=Fraction(part["waist_width"])
        if waist is None:waist=w
        if w!=waist:raise ValueError("bulk derivative waist differs")
        parts.append((path,part))
    if waist is None or not 0<waist<cut:
        raise ValueError("invalid derivative bulk interval")
    knots={Fraction(0),waist,cut}
    with np.load(origin,allow_pickle=False) as data:
        for key in data.files:
            if key.endswith("_knots"):
                knots.update(q for q in (abs(Fraction.from_float(float(x))) for x in data[key]) if 0<q<cut)
    points=sorted(knots)
    if points[1]!=waist:raise ValueError("waist crosses an actual scalar knot")
    cells=[(a,b) for a,b in zip(points,points[1:]) if a>=waist]
    selected={};waist_record=None;provenance=[]
    for path,part in parts:
        if part["radial_cells_total"]!=len(cells):
            raise ValueError("different original scalar partition")
        groups=defaultdict(list)
        for row in part["accepted_cells"]:
            if not 0<=row["index"]<len(cells):
                raise ValueError("invalid original cell index")
            groups[row["index"]].append(row)
        for index,rows in groups.items():
            complete=cover_rows(rows,*cells[index])
            if complete is not None:selected[index]=(path,complete)
        if "waist_derivative_absolute_integral_bound" in part:
            waist_record=(path,part["waist_derivative_absolute_integral_bound"])
        provenance.append(dict(path=str(path),sha256=sha(path),
            source=source_map[part["source_sha256"]],source_sha256=part["source_sha256"],
            accepted_subcells=len(part["accepted_cells"]),failed_subcells=len(part["failed_cells"])))
    missing=[j for j in range(len(cells)) if j not in selected]
    if missing or waist_record is None:
        raise ValueError("incomplete exact derivative cover: "+str(missing))
    bulk=stored_ball(waist_record[1]).upper()
    if not bulk>=0:raise ValueError("negative purported absolute bound")
    rows=[];leaves=0
    for index,(a,b) in enumerate(cells):
        path,sub=selected[index]
        value=arb(0)
        for row in sub:
            z=stored_ball(row["derivative_absolute_integral_bound"]).upper()
            if not z>=0:raise ValueError("negative absolute cell bound")
            value+=z
        value=value.upper();bulk+=value;leaves+=len(sub)
        rows.append(dict(index=index,left=str(a),right=str(b),source_part=str(path),
            subcells=len(sub),derivative_absolute_integral_bound=ball_record(value)))
    bulk=bulk.upper()
    collar_value=stored_ball(collar["derivative_collar_integral"])
    collar_absolute=abs(collar_value).upper()
    B=((bulk+collar_absolute)/2).upper()
    center_beta=stored_ball(point["beta"])
    half=arb(half_width.numerator)/half_width.denominator
    movement=(B*half).upper()
    beta=center_beta+arb(0,movement)
    scaled=2*arb(5).sqrt()*beta/arb.pi()
    lower=int(scaled.lower().floor().unique_fmpz())
    upper=int(scaled.upper().ceil().unique_fmpz())
    odds=[q for q in range(lower-4,upper+5) if q%2]
    gap=min([arb(1)]+[abs(scaled-q).lower() for q in odds])
    if not gap>0:gap=arb(0)
    phase_gap=(arb.pi()*gap/(2*arb(5).sqrt())).lower()
    report=dict(kind="complete_true_parameter_beta_derivative_and_uniform_transfer",
        complete=True,**identity,center_object_path=str(args.center_object),
        source_sha256=sha(__file__),derivative_core_sha256=sha(core_source),
        derivative_collar_source_sha256=sha(collar_source),
        derivative_collar_actual_source=accepted_collar_sources[collar["source_sha256"]],
        derivative_collar_actual_source_sha256=collar["source_sha256"],
        collector_helpers_sha256=sha(here/"fourfold_phase_beta_combine.py"),
        center_beta_path=str(args.center_beta),center_beta_sha256=sha(args.center_beta),
        derivative_collar_path=str(args.collar),derivative_collar_sha256=sha(args.collar),
        part_provenance=provenance,exact_original_knot_cells=len(cells),selected_subcells=leaves,
        fixed_cut=str(cut),waist_width=str(waist),waist_source_path=str(waist_record[0]),
        bulk_absolute_derivative_integral_bound=ball_record(bulk),
        true_derivative_collar_integral=ball_record(collar_value),
        beta_derivative_absolute_bound=ball_record(B),
        center_beta=ball_record(center_beta),maximum_parameter_transfer=ball_record(movement),
        beta=ball_record(beta),D5_scaled_beta=ball_record(scaled),
        D5_odd_norm_gap_lower=ball_record(gap),D5_beta_lattice_distance_lower=ball_record(phase_gap),
        selected_cells=rows,
        justification="fixed-physical-r finite-part differentiation; exact bulk cover; beta-prime bounded by half the absolute bulk plus finite-part collar; real-parameter mean value theorem",
        limitations=["uniform exactly on the displayed real affine parameter interval",
                     "principal return normalization, full scattering remainder, finite low block and nonlinear convergence remain separate"])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(dict(beta_prime=B.str(25),beta=beta.str(30),
        D5_phase_gap_lower=phase_gap.str(25))),flush=True)


if __name__=="__main__":main()

