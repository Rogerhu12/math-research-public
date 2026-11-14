#!/usr/bin/env python3
"""Actual19 ordinary Q47 reference disks and integral projective jets."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

P=47
Q=P**4

def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--lifts',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import p41_r2_matrix as r
    from p41_projective_jet_frames47 import ProjectiveJetFrames,install_exact_float_mm,matrix_digest
    install_exact_float_mm(r)
    from p41_actual_differentials47 import ActualModel
    a=ActualModel(args.script_dir);h=ProjectiveJetFrames(a);np=a.np
    lifts=read(args.lifts);points=sorted(lifts['points'],key=lambda p:p['j_mod47'])
    assert len(points)==19 and len({x['j_mod47'] for x in points})==19
    inventory=read(args.script_dir/'data/p41_residue47_inventory.json')
    assert {x['j_mod47'] for x in points}=={x['j'] for x in inventory['fibres'] if x['coarse_F47_points']==1}
    W=r.from_json([x['W_mod47four'] for x in points]);V2,V3=a.evaluate(W)
    assert r.equal(r.rows(a.M['V2'],a.M['P2']),r.eye(199))
    pa,pb=zip(*[(i,j) for i in range(73) for j in range(i,73)])
    oldprod=r.mul(r.cols(a.M['W'],pa),r.cols(a.M['W'],pb))
    coeff=r.rows(oldprod,a.M['P2'])
    assert r.equal(r.mm(a.M['V2'],coeff),oldprod)
    assert r.equal(r.mm(V2,coeff),r.mul(r.cols(W,pa),r.cols(W,pb)))
    assert not np.any(r.mm(W,h.candidates)[1])
    print('All19 physical rational centers: full2701 quadratic identities verified',flush=True)
    charts=[];records=[{'disk_id':'ORD_j'+str(p['j_mod47']).zfill(2),
                       'j_mod47':p['j_mod47'],'actual_elliptic_model':[p['curve_A'],p['curve_B']],
                       'necklace_1based':p['necklace_1based']} for p in points]
    for chart in h.iter_charts(W,order=3,max_points=64,label='all19ordinary'):
        I=chart['indices_0based'];idx=len(charts)
        assert r.equal(r.mm(a.M['A1'],r.conjugate(chart['frame'])),chart['frame'])
        assert r.equal(r.mm(a.M['A1'],r.conjugate(chart['coordinate'])),chart['coordinate'])
        assert all(not np.any(r.mm(w,h.candidates)[1]) for w in chart['W'])
        center=r.mm(chart['W'][0],chart['coordinate']);assert not np.any(center[1])
        charts.append({'chart_0based':idx,'disk_ids':[records[k]['disk_id'] for k in I],
            'original_input_rows_0based':I,'frame':r.to_json(chart['frame']),
            'coordinate':r.to_json(chart['coordinate']),'frame_kind':chart['frame_kind'],
            'coordinate_candidate':chart['coordinate_candidate'],'H_v_sha256':matrix_digest(chart['H_matrix']),
            'rational_coordinate_at_center_mod47four':center[0][:,0].astype(int).tolist(),
            'W_coefficients_0to3':[r.to_json(x) for x in chart['W']],
            'V2_coefficients_0to3':[r.to_json(x) for x in chart['V2']],
            'V3_coefficients_0to3':[r.to_json(x) for x in chart['V3']],
            'all_centers_and_coefficients_Frobenius_fixed':True,'unit_coordinate_tangent':True})
        for row,k in enumerate(I):records[k].update(chart_0based=idx,chart_row_0based=row)
    out={'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
         'scope':'All19 ordinary Q47 residue disks with actual reference values and cubic projective jets',
         'ordinary_disk_records':records,'charts':charts,
         'all19_actual_references_and_projective_jets_complete':True,
         'with_R228_all129_Q47_residue_disks_complete':True,
         'complete_Abel_log_constants':False,'complete_local_QC_sections':False,'complete_common_roots':False,
         'full_quadratic_product_identity_count':19*2701,
         'parameter_convention':'z=W*c/(W*v)-rational_coordinate_at_center in47 Z47; rational unit frame and etale coordinate',
         'tail_bound':'The smooth integral etale chart has integral coefficients; terms of degree>=4 vanish modulo47^4 for z in47Z47',
         'inputs_sha256':dict(a.inputs,**{args.lifts.name:hashlib.sha256(args.lifts.read_bytes()).hexdigest()}),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_bytes(gzip.compress((json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0))
    print('PASS all19 ordinary Q47 disks, true centers and cubic jets; all129 withR228',flush=True)
    print(hashlib.sha256(args.output.read_bytes()).hexdigest(),flush=True)

if __name__=='__main__':main()
