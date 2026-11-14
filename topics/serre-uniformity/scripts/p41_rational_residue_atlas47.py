#!/usr/bin/env python3
"""Actual rational coarse residue points and Q47 centers in the SS atlas.

Deduplication uses the very ample 73-dimensional projective embedding after
evaluation in 146 Frobenius-fixed spanning sections.  Rational centers are
obtained by fixing a rational etale projective coordinate, not by averaging
the points.  This file does not claim local heights or common QC roots.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

P=47
Q=P**4


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    from p41_elliptic_coarse_atlas47 import setup
    from p41_projective_jet_frames47 import ProjectiveJetFrames,matrix_digest
    at=setup(args.script_dir.resolve());a,r,np=at.a,at.r,at.np;h=ProjectiveJetFrames(a)
    inventory_path=a.folder/'data/p41_residue47_inventory.json';inventory=read(inventory_path)
    coarse_path=a.folder/'data/p41_elliptic_coarse_atlas47_verified.json.gz';coarse=read(coarse_path)
    sources={str(j):{'j':j,'W':ref['W'],'original_labels_1based':list(range(1,821)),
                      'kind':'ordinary_marked_point'} for j,ref in at.refs.items()}
    for rec in coarse['elliptic_charts']:
        key=rec['kind'];sources[key]={'j':0 if key=='CM3' else 36,
             'W':r.from_json(rec['coarse_values'][0]),'original_labels_1based':rec['indices_1based'],
             'kind':'true_elliptic_coarse_point'}
    groups={};count_by_source={};all_geometric={}
    for key,source in sources.items():
        W=source['W'];I=h.projective_indices(W)
        values=r.mm(r.rows(W,I),h.candidates)
        rational_rows=0
        for k,i in enumerate(I):
            vv=values[0][k]%P;ww=values[1][k]%P
            column=next(j for j in range(146) if (int(vv[j])**2+int(ww[j])**2)%P)
            z=int(vv[column]);w=int(ww[column]);norm=pow((z*z+w*w)%P,-1,P)
            real=(vv*z+ww*w)*norm%P;imag=(ww*z-vv*w)*norm%P
            fpkey=(tuple(int(x) for x in real),tuple(int(x) for x in imag))
            all_geometric.setdefault(source['j'],set()).add(fpkey)
            if np.any(imag):continue
            rational_rows+=1
            groupkey=(source['j'],fpkey[0]);label=source['original_labels_1based'][i]
            member={'reference_key':key,'row_0based':i,'original_necklace_label_1based':label,'kind':source['kind']}
            if groupkey not in groups:groups[groupkey]={'j_mod47':source['j'],
                'rational_projective_146_mod47':list(fpkey[0]),'reference_members':[]}
            groups[groupkey]['reference_members'].append(member)
        count_by_source[key]={'nonzero_projective_rows':len(I),'rational_projective_rows_before_quotient':rational_rows}
    disk_by_source={};records=[];byj={}
    for j in sorted(at.refs):
        keys=sorted(k for k in groups if k[0]==j)
        assert len(keys)==22,(j,len(keys))
        byj[str(j)]=len(keys)
        for number,gk in enumerate(keys,1):
            rec=groups[gk];rec['disk_id']='SS_j'+str(j)+'_'+str(number).zfill(2)
            members=rec['reference_members'];member=members[0]
            rec['chosen_reference']=member
            rec['reference_multiplicity']=len(members)
            index=len(records);records.append(rec)
            disk_by_source.setdefault(member['reference_key'],[]).append((member['row_0based'],index))
    assert len(records)==110
    charts=[]
    for key,entries in disk_by_source.items():
        W=sources[key]['W'];lookup=dict(entries)
        for original in h.iter_charts(W,indices=sorted(lookup),order=3,max_points=64,label=key):
            I=original['indices_0based'];n=len(I)
            basecoord=r.mm(original['W'][0],original['coordinate'])
            assert not np.any(basecoord[1]%P)
            shift=(np.zeros((n,1),dtype=np.int64),-basecoord[1]%Q)
            center=r.zeros(n,73)
            power=(np.ones((n,1),dtype=np.int64),np.zeros((n,1),dtype=np.int64))
            for k in range(4):
                center=r.add(center,r.mul(original['W'][k],power));power=r.mul(power,shift)
            rational_values=r.mm(center,h.candidates)
            assert not np.any(rational_values[1]),('center rationality',key,I)
            assert r.equal(r.mm(center,original['frame']),r.column([[1,0]]*n))
            assert r.equal(r.mm(center,original['coordinate']),(basecoord[0],np.zeros_like(basecoord[1])))
            chart=h.local_jets(center,frame=original['frame'],coordinate=original['coordinate'],
                               H_matrix=original['H_matrix'],order=3)
            assert all(not np.any(r.mm(w,h.candidates)[1]) for w in chart['W'])
            chart_index=len(charts)
            disks=[records[lookup[i]]['disk_id'] for i in I]
            charts.append({'chart_0based':chart_index,'reference_key':key,'disk_ids':disks,
                'original_input_rows_0based':I,'frame':r.to_json(original['frame']),
                'coordinate':r.to_json(original['coordinate']),
                'H_v_sha256':matrix_digest(original['H_matrix']),
                'frame_kind':original['frame_kind'],'coordinate_candidate':original['coordinate_candidate'],
                'shift_from_original_center_mod47four':r.to_json(shift),
                'rational_coordinate_at_center_mod47four':basecoord[0][:,0].astype(int).tolist(),
                'W_coefficients_0to3': [r.to_json(w) for w in chart['W']],
                'V2_coefficients_0to3':[r.to_json(v) for v in chart['V2']],
                'V3_coefficients_0to3':[r.to_json(v) for v in chart['V3']],
                'all_centers_and_coefficients_Frobenius_fixed':True,
                'unit_coordinate_tangent':True})
            for row,i in enumerate(I):
                rec=records[lookup[i]];rec.update(chart_0based=chart_index,chart_row_0based=row)
        print('Rational SS centers and jets',key,len(entries),flush=True)
    ordinary=[rec for rec in inventory['fibres'] if rec['coarse_F47_points']==1]
    assert len(ordinary)==19 and sum(byj.values())+len(ordinary)==inventory['number_of_residue_discs']==129
    assert inventory['rational_cusps']==0
    out={'level':41,'auxiliary_prime':47,'modulus':Q,'precision':4,
         'scope':'All110 SS Q47 coarse residue disks with actual embedded rational centers and projective jets',
         'complete_SS_rational_disk_inventory':True,'complete_all129_projective_centers':False,
         'complete_Abel_log_constants':False,'complete_local_QC_sections':False,'complete_common_roots':False,
         'source_row_counts':count_by_source,'geometric_coarse_counts':{str(j):len(v) for j,v in all_geometric.items()},
         'SS_rational_disk_counts':byj,'SS_disk_records':records,'charts':charts,
         'missing19_ordinary_fibres':ordinary,'total_Q47_residue_disks':129,'rational_cusp_disks':0,
         'parameter_convention':'z=W*c/(W*v)-rational_coordinate_at_center, z in47 Z47; each chosen v,c is Frobenius-fixed',
         'center_construction':'In a unit etale coordinate, shift by minus i times the original imaginary coordinate; evaluate integral degree3 jets modulo47^4',
         'projective_criterion':'146 Frobenius-fixed spanning sections; normalize the first unit coordinate, retain exactly rows with every imaginary coordinate zero mod47, then deduplicate',
         'tail_bound':'Integral W,V2,V3 chart coefficients; z in47Z47 makes degree>=4 terms zero mod47^4; derivative recurrence used only unit integers1,2,3',
         'input_sha256':dict(a.inputs,**{coarse_path.name:sha(coarse_path),inventory_path.name:sha(inventory_path)}),
         'helper_sha256':sha(sys.modules['p41_projective_jet_frames47'].__file__),'source_sha256':sha(__file__)}
    args.output.write_bytes(gzip.compress((json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0))
    print('PASS all110 SS coarse rational disks; true Q47 centers and cubic projective jets; 19 ordinary disks remain',flush=True)
    print('Geometric',out['geometric_coarse_counts'],'Rational',byj,'SHA',sha(args.output),flush=True)


if __name__=='__main__':main()
