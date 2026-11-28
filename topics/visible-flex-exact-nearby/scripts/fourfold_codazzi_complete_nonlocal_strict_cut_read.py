"""Exact endpoint comparisons from the completed GNF small receipt, with the actual ASQ29 row."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

ORIGINAL='38ef9f41a3013fc54f6b781365597c96363a8d9674971fd00b82084211958dc7'
EVENT='2ec32df32a1afe66000e4c38f26414e81f3ed32d'


def read(path):
    b=path.read_bytes()
    assert (len(b),sha256(b).hexdigest())==(2754,ORIGINAL)
    d=json.loads(b)
    assert d['run']=='46150791569' and d['attempt']==1 and d['event_commit']==EVENT
    assert d['proved'] is d['complete'] is d['all_five_nonlocal_means_retained'] is True
    assert d['completed_radial_slabs']==16 and d['completed_subpieces']==d['natural_group_count']==1136
    assert d['original_input_labels']==[97,1048576] and d['original_input_signs']==[1,-1]
    assert d['outer_J_factors']==0 and d['old_scientific_targets_recomputed']==0
    assert d['row_order']==['g1_Hminus5over3','g1_Hminus2over3','g2_physical_scalar']
    assert d['private_sha256']=='8364151c983941fa2a467c6da349d094b408c802d6c67bc48973d9f981e51cdb'
    assert d['private_uncompressed_sha256']=='c9a92388e27944369ef8cfb2fe4944fc58fcafd47fdde05751cb6ccf8ec0aa48'
    out={}
    g=Q(4072,100);common=Q(62,5)
    right_sq=(Q(10611,1000)*Q(1061,1000)/Q(11,10))**2*(Q(97,1000)**2+Q(22,1000)**2)
    for name,lo,metrics in [('terminal_Ai','0.0000699273',('0.002848','0.03532','0.00291')),
                            ('both_reference_columns','0.000138375',('0.005635','0.06988','0.00575'))]:
        m=Q.from_float(d['physical_outputs_through_completed_slabs'][name]['joint_L1'][1])
        a,b,c=map(Q,metrics);v=g*m
        assert m<Q(lo) and v<a and v*common<b and v*v*right_sq<c*c
        out[name]=dict(mixed_full_atom_L1_upper=lo,natural_waist_upper=metrics[0],
                       common_physical_upper=metrics[1],ordered_ASQ16_high_action_upper=metrics[2])
    return dict(kind='R149_GNU_actual_finite_nonlocal_mixed_source_through_true_waist',complete=True,
        proved=True,run='46150791569',attempt=1,source_whole_sha256=ORIGINAL,
        original_groups_read_only=1136,old_scientific_targets_called=0,
        full_independent_mean_in_each_mixed_slab=True,extra_angular_J_factors=0,
        full_waist_left_factor='40.72',all=out)


if __name__=='__main__':
    p=ArgumentParser();p.add_argument('original',type=Path)
    print(json.dumps(read(p.parse_args().original),sort_keys=True,separators=(',',':')))
