#!/usr/bin/env python3
"""Independently audit qC target exclusions and reconstructed qT at calibration rows."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys


def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith(".gz") else raw)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--script-dir",type=Path,required=True)
    ap.add_argument("--center",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    sys.path.insert(0,str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import install_exact_float_mm
    install_exact_float_mm(r)
    a=ActualModel(args.script_dir)
    q=47**3
    center=read(args.center)
    basepath=args.script_dir/"data/p41_hecke3_abel_bases_checkpoint.json.gz"
    bases=read(basepath)
    I1,I2=[[i-1 for i in f["points_1based"]] for f in bases["families"]]
    hecke_path=args.script_dir/"data/p41_hecke47_full_saved.json.gz"
    H=read(hecke_path)["operators"]["2"]
    permutation=[i-1 for i in H["necklace_transport_1based"]]
    C,T=[center["actual_connections"][k] for k in ["C","T2C"]]
    qC=r.from_json(C["denominator_linear_coefficients_mod47four"])
    sC=r.from_json(C["numerator_quadratic_coefficients_mod47cubed"],q)
    qT=r.from_json(T["denominator_linear_coefficients_mod47four"])
    sT=r.from_json(T["numerator_quadratic_coefficients_mod47cubed"],q)
    assert np.all(r.units(r.mm(r.rows(a.M["W"],I1+I2),qC)))
    mask=np.ones(820,dtype=bool)
    counts=[]
    total=r.zeros(820,1)
    for target in H["targets"]:
        W=r.from_json(target["evaluation_matrix"])
        V2,_=a.evaluate(W)
        den=r.mm(W,qC)
        numerator=r.mm(a.reduce(V2,q),sC,q)
        good=np.flatnonzero(r.units(den)[:,0]).tolist()
        values=r.zeros(820,1)
        vv=r.mul(r.rows(numerator,good),r.inverse_values(a.reduce(r.rows(den,good),q),q),q)
        for k in range(2):
            values[k][good]=vv[k]
        total=r.add(total,r.rows(values,permutation),q)
        mask&=r.units(den)[:,0][permutation]
        counts.append(len(good))
    total=a.scale(total,pow(2,-1,q),q)
    good=np.flatnonzero(mask).tolist()
    assert len(good)>504
    badcal=[i for i in I1+I2 if i not in good]
    assert counts==T["branch_good_rows"]
    assert len(good)==T["common_good_rows"]
    assert badcal==T["calibration_source_rows_not_used_for_trace_interpolation_0based"]
    assert badcal, "This audit is intended for the actual removable-denominator case"
    den=r.mm(a.M["W"],qT)
    assert np.all(r.units(r.rows(den,I1+I2)))
    assert all(i in I1+I2 for i in badcal)
    values=r.mm(a.reduce(a.M["V2"],q),sT,q)
    wanted=r.mul(a.reduce(r.rows(den,good),q),r.rows(total,good),q)
    assert r.equal(r.rows(values,good),wanted)
    E=a.reduce(r.rows(a.M["V2"],good),q)
    rr,cc=r.rank_pivots(E)
    assert len(rr)==199 and cc==list(range(199))
    out={
        "disk_id":center["disk_id"],"common_good_source_count":len(good),
        "branch_good_counts":counts,
        "excluded_calibration_rows_0based":badcal,
        "original_qC_unit_at_all108_direct_calibration_rows":True,
        "new_qT_unit_at_all108_calibration_rows":True,
        "all_actual_trace_cross_products_verified":True,
        "actual_V2_good_evaluation_unit_rank":199,
        "no_RR_reconstruction_or_group_chain_reexecution":True,
        "input_sha256":dict(a.inputs,**{str(args.center):sha(args.center),str(basepath):sha(basepath),
                                      str(hecke_path):sha(hecke_path)}),
        "source_sha256":sha(__file__),
    }
    args.output.write_text(json.dumps(out,indent=2)+"\n")
    print("PASS",center["disk_id"],"actual denominator audit",len(good),"good rows,excluded calibration",badcal,"SHA",sha(args.output))


if __name__=="__main__":
    main()

