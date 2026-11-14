#!/usr/bin/env python3
"""Exact finite coverage and rational comparisons of a completed N certificate."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import numpy as np


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    saved=json.loads(args.certificate.read_text())
    rows=sorted(saved["rows"],key=lambda r:r["interval"][0])
    assert saved["status"]=="complete" and not saved["pending"] and not saved["failures"]
    assert rows[0]["interval"][0]==0 and rows[-1]["interval"][1]==saved["core"][1]
    assert all(a["interval"][1]==b["interval"][0] for a,b in zip(rows[:-1],rows[1:]))
    assert all(r["passed"] and r["positive_multiplier_conditions"] for r in rows)
    assert all(Fraction.from_float(r["N_factor_lower"])>Fraction(37235,100000)
               and Fraction.from_float(r["raw_minus_n_lower"])>Fraction(42529,100000)
               and Fraction.from_float(r["actual_unit_normal_N_upper"])<Fraction(-3092,10000)
               for r in rows)
    with np.load(saved["inputs"],allow_pickle=False) as data:
        multiplicities={}
        for name in data.files:
            if name.endswith("_knots"):
                values,counts=np.unique(data[name],return_counts=True)
                use=(values>-saved["core"][1])&(values<saved["core"][1])
                multiplicities[name]=int(counts[use].max()) if np.any(use) else 0
                assert multiplicities[name]<=1
    endpoint=Fraction.from_float(saved["core"][1])
    report=dict(kind="exact_finite_coverage_and_output_comparison_for_directed_N_certificate",
                certificate_sha256=hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
                radial_cells=len(rows),
                exact_positive_endpoint=dict(numerator=str(endpoint.numerator),denominator=str(endpoint.denominator)),
                whole_closed_positive_interval_covered=True,all_cells_passed=True,
                strict_rational_bounds=dict(N_factor_lower="37235/100000",minus_raw_n_lower="42529/100000",unit_N_upper="-3092/10000"),
                maximum_core_knot_multiplicities=multiplicities)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report),flush=True)


if __name__=="__main__":main()
