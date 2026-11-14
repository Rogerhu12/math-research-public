#!/usr/bin/env python3
"""Targeted checks of fc-zero charts and all21 genuine elliptic coarse points."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    from p41_elliptic_coarse_atlas47 import setup,Series
    from p41_projective_jet_frames47 import ProjectiveJetFrames,ordinary_physical_jets,matrix_digest
    at=setup(args.script_dir.resolve());a,r=at.a,at.r;h=ProjectiveJetFrames(a)
    def compose_check(raw,chart,z,order):
        selected=[r.rows(w,chart['indices_0based']) for w in raw[:order+1]]
        vv=[r.mm(w,chart['frame']) for w in selected]
        direct=Series(a,order+1).mul(selected,Series(a,order+1).inverse(vv))
        composed=Series(a,order+1).compose(chart['W'][:order+1],z,order+1)
        assert all(r.equal(x,y) for x,y in zip(direct,composed))
    nonunits={}
    for j,ref in at.refs.items():
        ordinary=h.projective_indices(ref['W']);units=r.units(r.mm(ref['W'],a.fc))[:,0]
        nonunits[str(j)]=[i for i in ordinary if not units[i]]
    assert nonunits=={'9':[],'10':[],'44':[218,770],'0':[],'36':[]}
    physical=ordinary_physical_jets(at,44,order=4)
    assert len(physical['W'])==5
    records=[]
    for chart in h.iter_charts(at.refs[44]['W'],nonunits['44'],order=27,max_points=64,label='j44_fc_zero'):
        assert chart['frame_kind']=='unit_replacement'
        z=h.physical_to_chart(physical['W'],chart,4)
        compose_check(physical['W'],chart,z,4)
        records.append({'indices_0based':chart['indices_0based'],'order':27,
                        'frame_sha256':matrix_digest(chart['frame']),
                        'H_v_sha256':matrix_digest(chart['H_matrix']),
                        'coordinate_sha256':matrix_digest(chart['coordinate']),
                        'source820_identity':True,'physical_composition_all73_through_degree4':True,
                        'physical_to_chart_coefficients_0to4':[r.to_json(v) for v in z],
                        'W_sha256':[matrix_digest(v) for v in chart['W']],
                        'V2_sha256':[matrix_digest(v) for v in chart['V2']],
                        'V3_sha256':[matrix_digest(v) for v in chart['V3']]})
    coarse_path=a.folder/'data/p41_elliptic_coarse_atlas47_verified.json.gz'
    coarse=json.loads(gzip.decompress(coarse_path.read_bytes()));coarse_checks=[]
    for rec in coarse['elliptic_charts']:
        W=[r.from_json(w) for w in rec['coarse_values']]
        covered=[]
        for chart in h.iter_charts(W[0],order=3,max_points=64,label=rec['kind']):
            z=h.coarse_to_chart(rec,chart)
            compose_check(W,chart,z,3)
            assert a.np.all(r.units(z[1]))
            covered+=chart['indices_0based']
            coarse_checks.append({'kind':rec['kind'],'indices_0based':chart['indices_0based'],
                                  'coarse_coordinate_u':True,'unit_tangent':True,
                                  'all73_composition_through_degree3':True,
                                  'z_of_u_coefficients_0to3':[r.to_json(v) for v in z]})
        assert sorted(covered)==list(range(len(rec['indices_1based'])))
    # The old fc-unit recurrence is independent of the new variable-fc formula.
    W0=r.rows(at.refs[9]['W'],[0,1,2]);new=h.local_jets(W0,order=27)
    old=a.local_jets(W0,order=27,coordinate_seed=0)
    for key in ['W','V2','V3']:
        assert all(r.equal(x,y) for x,y in zip(new[key],old[key]))
    out={'scope':'Targeted R222 projective-frame and true coarse-coordinate checks',
         'complete':True,'fc_nonunit_ordinary_indices_0based':nonunits,
         'fc_zero_checks':records,'elliptic_coarse_checks':coarse_checks,
         'old_fc_recurrence_three_points_all28_coefficients_matches':True,
         'physical_order4_returns_five_coefficients':True,
         'helper_sha256':hashlib.sha256(Path(sys.modules['p41_projective_jet_frames47'].__file__).read_bytes()).hexdigest(),
         'coarse_input_sha256':hashlib.sha256(coarse_path.read_bytes()).hexdigest(),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':a.inputs}
    args.output.write_bytes(gzip.compress(json.dumps(out,sort_keys=True,separators=(',',':')).encode(),mtime=0))
    print('PASS two fc-zero points; twenty-one coarse points; old fc degree27; SHA',hashlib.sha256(args.output.read_bytes()).hexdigest())


if __name__=='__main__':main()
