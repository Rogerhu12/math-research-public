#!/usr/bin/env python3
"""Calibrate the independent half-field evaluator on the original R102 fibre."""
import argparse
import hashlib
import json
from pathlib import Path
from p41_ordinary_residue_points47 import point as residue_point,read
from p41_ordinary_point_lifts47 import point as lifted_point,Q

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();model=read(args.script_dir/'data/p41_makdisi47_certificate.json.gz')
    rec={'j_mod47':9,'curve_A':1,'curve_B':32,'elliptic_frobenius_trace':0,
         'full_41_torsion_residue_degree':80}
    r=residue_point(model,rec,10)
    label=r['necklace_1based']-1
    expected=model['evaluation_matrix'][label]
    assert r['W_mod47']==[[u%47,v%47] for u,v in expected]
    alpha=10
    for _ in range(2):alpha=(alpha-(alpha*alpha+41)*pow(2*alpha,-1,Q))%Q
    s=lifted_point(model,r,alpha)
    assert s['W_mod47four']==expected
    out={'level':41,'auxiliary_prime':47,'reference_j':9,
         'reference_necklace_1based':label+1,'reference_necklace':r['necklace'],
         'x_field_degree':40,'all73_residue_values_match_R102':True,
         'all73_precision4_physical_weight2_values_match_R102':True,
         'trace_coordinate_formula':'20/k times absolute trace; negative imaginary coordinate uses trace(i*z)',
         'cyclotomic_quadratic_orientation_mod47':10,
         'W_mod47four':s['W_mod47four'],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS independent half-field evaluator exactly reproduces all73 original R102 physical values mod47^4',flush=True)

if __name__=='__main__':main()
