#!/usr/bin/env python3
"""Independent exact endpoint bookkeeping for the root metric witness."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--author',type=Path,required=True)
    ap.add_argument('--rerun',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();a=json.loads(args.author.read_text());b=json.loads(args.rerun.read_text())
    assert {k:v for k,v in a.items() if k!='seconds'}=={k:v for k,v in b.items() if k!='seconds'}
    expected='da0795deed1303dac7a38b68ea168ffd2883d8a84559df77c10ed3e91498e1da'
    assert b['manifest_sha256']==expected and not b['whole_surface_upper_bound'] and not b['README_complete']
    w=b['selected_witness'];assert w['span']==4304 and Q(w['local_exact'])==Q(1,2)
    assert w['angle_multiple_of_pi_over_six']==2
    components=[tuple(map(Q,pair)) for pair in w['normalized_component_intervals']]
    def lower(pair):
        lo,hi=pair;assert lo<=hi
        return Q(0) if lo<=0<=hi else min(abs(lo),abs(hi))
    def upper(pair):return max(map(abs,pair))
    exact_lower=max(map(lower,components))
    exact_upper=max(upper(components[0])+upper(components[1]),
                    upper(components[1])+upper(components[2]))
    assert Q(w['relative_operator_lower'])<=exact_lower
    assert Q(w['relative_operator_upper'])>=exact_upper
    assert Q(w['relative_operator_lower'])>Q('2.02348e-7')
    target=Path(__file__).with_name('db6f-root-tail-metric-point.py')
    proof=Path(__file__).parent.parent/'notes/2026-11-09-db6f-root-tail-m8-point-metric-witness.md'
    out={'status':'independent-root-metric-witness-review-pass','target_sha256':sha(target),
         'proof_sha256':sha(proof),'author_report_sha256':sha(args.author),
         'independent_rerun_sha256':sha(args.rerun),'review_script_sha256':sha(__file__),
         'all_mathematical_report_fields_equal':True,'only_runtime_seconds_differ':True,
         'exact_component_minimum_absolute_lower':str(exact_lower),
         'exact_maximum_absolute_row_sum_upper':str(exact_upper),
         'published_strict_decimal_lower':'2.02348e-7',
         'manifest_sha256':expected,'scope':'Only the explicitly bound R18 finite M8 graph and its reviewed original background. Point witness is not a whole-domain upper bound or convergence theorem.'}
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'all_mathematical_fields_equal':True,'strict_lower':out['published_strict_decimal_lower']}))


if __name__=='__main__':main()
