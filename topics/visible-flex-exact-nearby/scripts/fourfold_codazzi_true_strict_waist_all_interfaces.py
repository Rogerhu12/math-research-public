"""Exact original-bounds arithmetic for the true strict physical row and all signed seams."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json


def original(p,sz,digest,run,n):
    b=p.read_bytes();assert (len(b),sha256(b).hexdigest())==(sz,digest)
    d=json.loads(b)
    assert d['complete'] and d['proved'] and d['run']==run and d['attempt']==1 and d['completed_subpieces']==n
    return d


def compute(a,b):
    root=original(a,1210,'47348f89fa2dd8b19c2a5dab4d3719c4ef2adf6f883d36e5d4c43035df6f8f0e','46145341825',576)
    strict=original(b,1510,'7db431ce7fea60a5e46da17641fcefbc8842753430f12a588ee345160c419380','46150669215',1973)
    assert root['original_interfaces']==strict['retained_root_interface_count']==576
    assert strict['all_negative_original_seams']==576+1973 and strict['same_cubic_cut_points_exact_zero']==521
    assert root['old_scientific_targets_recomputed']==strict['previous_paid_science_targets_recomputed']==0
    factor=Q('.719')*Q('1.041')*Q('3.24')*Q('1.488')*Q('1.060693')
    assert factor<Q('3.828')
    high=Q('.00238')*Q('8.22')
    assert high<Q('.01957') and Q(17,16)<Q('1.031')**2
    J=Q('1.031')*(1+Q('1.4')*Q('3.711826'))/Q('1.10865')
    assert J<Q('5.77') and J*high<Q('.113')
    m=Q.from_float(root['raw_mixed_sum']);s=Q.from_float(strict['strict_Hminus1_sum'])
    ext=factor*s;full=Q('40.72')*m+ext
    h2=(Q('10.611')*Q('1.061')/Q('1.1'))**2*(Q('.097')**2+Q('.022')**2)
    assert ext<Q('1.128e-11') and full<Q('8.42e-7') and full*Q('12.4')<Q('1.045e-5') and full**2*h2<Q('8.60e-7')**2
    return dict(complete=True,proved=True,old_scientific_targets_called=0,old_actual_runs=[46145341825,46150669215],
        physical_strict_Hminus1_pair_to_WPL='3.828',strict_L2_pair_to_P97_WPL='.01957',
        strict_Hminus1_to_L2_J='5.77',pre_J_strict_Hminus1_to_P97_WPL='.113',
        all_true_original_seams=2549,additional_zero_cuts=521,strict_1973_natural='1.128e-11',
        whole_negative_seam_natural='8.42e-7',whole_negative_seam_common='1.045e-5',whole_negative_seam_ASQ16='8.60e-7')


if __name__=='__main__':
    p=ArgumentParser();p.add_argument('root_576',type=Path);p.add_argument('outer_1973',type=Path);a=p.parse_args()
    print(json.dumps(compute(a.root_576,a.outer_1973),sort_keys=True,separators=(',',':')))
