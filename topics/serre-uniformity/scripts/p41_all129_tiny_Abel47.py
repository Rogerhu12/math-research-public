#!/usr/bin/env python3
"""Combine the110 SS tiny Abel charts with all19 actual ordinary charts."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

Q=47**4;Q3=47**3
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--SS-tiny',type=Path,required=True)
    p.add_argument('--ordinary-atlas',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import ProjectiveJetFrames
    from p41_elliptic_coarse_atlas47 import Series
    a=ActualModel(args.script_dir.resolve());r,np=a.r,a.np;frames=ProjectiveJetFrames(a)
    SS=read(args.SS_tiny);ordinary=read(args.ordinary_atlas)
    assert SS['complete_110_SS_tiny_Abel_integrals']
    assert ordinary['all19_actual_references_and_projective_jets_complete']
    inverse=r.from_json(SS['divided_Lie_to_cyclic_mod47cubed'],Q3)
    AK=r.from_json(a.cusp['canonical_frobenius_matrix'])
    charts=[];ids=[]
    for rec in SS['charts']:
        rec=dict(rec);rec.update(origin='R230_SS',origin_chart_0based=rec['chart_0based'])
        rec['chart_0based']=len(charts);charts.append(rec);ids+=rec['disk_ids']
    for ch in ordinary['charts']:
        W=[r.from_json(v) for v in ch['W_coefficients_0to3']]
        V3=[r.from_json(v) for v in ch['V3_coefficients_0to3']]
        frame,coordinate=r.from_json(ch['frame']),r.from_json(ch['coordinate'])
        H=frames.frame_derivation(frame)['H']
        hc=[r.mm(r.mm(v3,H),coordinate) for v3 in V3[:3]]
        omega=Series(a,3).mul([r.mm(w,a.K1) for w in W[:3]],Series(a,3).inverse(hc))
        assert all(r.equal(r.mm(om,AK),r.conjugate(om)) for om in omega)
        tiny=[]
        for k in range(1,4):
            coeff=a.scale(a.reduce(omega[k-1],Q3),47**(k-1)*pow(k,-1,Q3),Q3)
            value=r.mm(coeff,inverse,Q3)
            assert not np.any(value[1])
            tiny.append(value[0].astype(int).tolist())
        rec={'chart_0based':len(charts),'origin':'R231_ordinary','origin_chart_0based':ch['chart_0based'],
             'disk_ids':ch['disk_ids'],'canonical_differential_coefficients_0to2_mod47four':[r.to_json(om) for om in omega],
             'cyclic_coordinate_tiny_coefficients_1to3_in_y_mod47cubed':tiny,
             'all54_cyclic_coefficients_rational':True,
             'parameter':'y=z/47 in Z47; cyclic tiny equals a(P)-a(center)'}
        charts.append(rec);ids+=rec['disk_ids']
    assert len(ids)==len(set(ids))==129
    out={'level':41,'auxiliary_prime':47,'modulus':Q,'precision':4,
         'complete_all129_tiny_Abel_integrals':True,'complete_all129_Abel_constants':False,
         'complete_local_QC_functions':False,'complete_common_roots':False,
         'SS_disk_count':110,'ordinary_disk_count':19,'rational_cusp_disk_count':0,
         'cyclic_coordinate_precision':3,'charts':charts,
         'cyclic_to_divided_Lie_mod47cubed':SS['cyclic_to_divided_Lie_mod47cubed'],
         'divided_Lie_to_cyclic_mod47cubed':SS['divided_Lie_to_cyclic_mod47cubed'],
         'known_CM_anchored_disks':SS['known_CM_anchored_disks'],
         'differential_formula':SS['differential_formula'],'tiny_formula':SS['tiny_formula'],
         'tail_bound':SS['tail_bound'],'global_precision_reason':SS['global_precision_reason'],
         'input_sha256':dict(a.inputs,**{args.SS_tiny.name:sha(args.SS_tiny),args.ordinary_atlas.name:sha(args.ordinary_atlas)}),
         'source_sha256':sha(__file__)}
    args.output.write_bytes(gzip.compress((json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0))
    print('PASS all129 genuine rational residue disks, each54 differentials and tiny Abel integrals; SHA',sha(args.output),flush=True)


if __name__=='__main__':main()
