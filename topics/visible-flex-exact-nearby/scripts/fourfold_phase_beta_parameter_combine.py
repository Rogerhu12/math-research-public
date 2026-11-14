#!/usr/bin/env python3
"""Prove exact bulk coverage and combine a uniform parameter-box beta."""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import numpy as np
from flint import arb, ctx
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_combine import stored_ball, cover_rows


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--center-object",type=Path,required=True)
    parser.add_argument("--collar",type=Path,required=True)
    parser.add_argument("--parts",type=Path,nargs="+",required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    ctx.prec=192
    here=Path(__file__).parent
    definition,origin,direction,center=load_definition(args.center_object)
    object_sha=sha(args.center_object)
    germ_sha=sha(here/"fourfold_phase_beta_parameter_germ.py")
    bulk_sha=sha(here/"fourfold_phase_beta_parameter_bulk.py")
    collar=json.loads(args.collar.read_text())
    if (collar.get("kind")!="uniform_exact_affine_germ_collar"
            or not collar.get("complete") or collar["source_sha256"]!=germ_sha):
        raise ValueError("incomplete uniform collar or different germ source")
    half_width=Fraction(collar["exact_parameter_half_width"])
    expected_interval=[str(center-half_width),str(center+half_width)]
    identity=dict(center_object_sha256=object_sha,
        origin_inputs_sha256=sha(origin),direction_sha256=sha(direction),
        exact_center_parameter=str(center),exact_parameter_half_width=str(half_width),
        exact_parameter_interval=expected_interval)

    def check_identity(report):
        if any(report[key]!=value for key,value in identity.items()):
            raise ValueError("the actual parameter box, origin, or direction differs")
        for name,digest in report["dependency_sha256"].items():
            if sha(here/name)!=digest:
                raise ValueError(f"dependency changed: {name}")

    check_identity(collar)
    collar_sha,cut=sha(args.collar),Fraction(collar["fixed_cut"])
    parts,waist=[],None
    for path in args.parts:
        part=json.loads(path.read_text())
        check_identity(part)
        if (part.get("kind")!="uniform_exact_affine_germ_phase_bulk"
                or part["source_sha256"]!=bulk_sha
                or part["parameter_engine_sha256"]!=germ_sha
                or part["collar_sha256"]!=collar_sha
                or Fraction(part["fixed_cut"])!=cut):
            raise ValueError("bulk source, collar, or cut differs")
        new_waist=Fraction(part["waist_width"])
        if waist is None:
            waist=new_waist
        if waist!=new_waist:
            raise ValueError("different waist cuts")
        parts.append((path,part))
    if not 0<waist<cut:
        raise ValueError("invalid exact bulk interval")
    knots={Fraction(0),waist,cut}
    with np.load(origin,allow_pickle=False) as inputs:
        for key in inputs.files:
            if key.endswith("_knots"):
                knots.update(q for q in
                    (abs(Fraction.from_float(float(x))) for x in inputs[key])
                    if 0<q<cut)
    points=sorted(knots)
    if points[1]!=waist:
        raise ValueError("waist crosses an exact scalar knot")
    cells=[(a,b) for a,b in zip(points,points[1:]) if a>=waist]
    selected,waist_record,part_provenance={},None,[]
    for path,part in parts:
        if part["radial_cells_total"]!=len(cells):
            raise ValueError("different exact scalar partition")
        grouped=defaultdict(list)
        for row in part["accepted_cells"]:
            if not 0<=row["index"]<len(cells):
                raise ValueError("invalid original-span index")
            grouped[row["index"]].append(row)
        for index,rows in grouped.items():
            complete=cover_rows(rows,*cells[index])
            if complete is not None:
                selected[index]=path,complete
        if "waist_integral" in part:
            waist_record=path,part["waist_integral"]
        part_provenance.append(dict(path=str(path),sha256=sha(path),
            accepted_subcells=len(part["accepted_cells"]),
            failed_subcells=len(part["failed_cells"])))
    missing=[index for index in range(len(cells)) if index not in selected]
    if missing or waist_record is None:
        raise ValueError(f"incomplete exact cover: missing={missing}, waist={waist_record is not None}")
    total=stored_ball(waist_record[1])
    sums,subcells=[],0
    for index,(left,right) in enumerate(cells):
        path,rows=selected[index]
        value=sum((stored_ball(row["integral"]) for row in rows),arb(0))
        total+=value
        subcells+=len(rows)
        sums.append(dict(index=index,left=str(left),right=str(right),
            source_part=str(path),subcells=len(rows),integral=ball_record(value)))
    collar_value=stored_ball(collar["collar_integral"])
    beta=(total+collar_value)/2
    scaled=2*arb(5).sqrt()*beta/arb.pi()
    lower=int(scaled.lower().floor().unique_fmpz())
    upper=int(scaled.upper().ceil().unique_fmpz())
    odd=[q for q in range(lower-4,upper+5) if q%2]
    gap=min([arb(1)]+[abs(scaled-q).lower() for q in odd])
    if not gap>0:
        gap=arb(0)
    phase_gap=(arb.pi()*gap/(2*arb(5).sqrt())).lower()
    report={
        "kind":"complete_uniform_exact_affine_parameter_beta",
        "complete":True,**identity,
        "center_object_path":str(args.center_object),
        "source_sha256":sha(__file__),"parameter_engine_sha256":germ_sha,"bulk_source_sha256":bulk_sha,
        "dependency_sha256":collar["dependency_sha256"],
        "collector_helpers_sha256":sha(here/"fourfold_phase_beta_combine.py"),
        "collar_path":str(args.collar),"collar_sha256":collar_sha,
        "part_provenance":part_provenance,
        "exact_original_knot_cells":len(cells),"selected_subcells":subcells,
        "waist_path":str(waist_record[0]),"waist_width":str(waist),"fixed_cut":str(cut),
        "bulk_integral":ball_record(total),"collar_integral":ball_record(collar_value),
        "beta":ball_record(beta),"D5_scaled_beta":ball_record(scaled),
        "D5_odd_norm_gap_lower":ball_record(gap),"D5_beta_lattice_distance_lower":ball_record(phase_gap),
        "D5_candidate_grid_points":[dict(Q=q,beta_grid=ball_record(arb.pi()*q/(2*arb(5).sqrt()))) for q in odd],
        "selected_cells":sums,
        "limitations":[
            "The beta bound is uniform exactly on the stated rational parameter interval",
            "The stated interval is not asserted to be the final KAM interval",
            "Matching the principal rotation and paying the complete scattering remainder, low block, and nonlinear family remain separate requirements"
        ]}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(dict(beta=beta.str(30),D5_norm_gap_lower=gap.str(22),
        D5_phase_gap_lower=phase_gap.str(22))),flush=True)


if __name__=="__main__":
    main()
