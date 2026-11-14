#!/usr/bin/env python3
"""Recover selected genuine rational SS reference10 T3 targets from the frozen full-level graph."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time


def read(p):
    return json.loads(gzip.decompress(Path(p).read_bytes()))


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ['script-dir','work-dir','output']:
        ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--disk-id',required=True)
    args=ap.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    from p41_dag_level_transport47 import initialize
    from p41_projective_jet_frames47 import ProjectiveJetFrames,ordinary_physical_jets
    from p41_native_r2_linear47 import install
    from p41_actual_differentials47 import save,digest
    from p41_supersingular_atlas47 import cp,ck,ca,cm,ci
    started=time.monotonic();at=initialize(folder);a,r,np=at.a,at.r,at.np
    install(r,args.work_dir/'native');frames=ProjectiveJetFrames(a)
    data=folder/'data';inputs={}
    def load(name):
        p=data/name;inputs[name]=sha(p);return read(p)
    atlas=load('p41_rational_SS_residue_atlas47_complete.json.gz')
    graph=load('p41_SS_Hecke_graph47.json.gz')
    coarse=load('p41_elliptic_coarse_atlas47_verified.json.gz')
    disk=args.disk_id;ch=next(c for c in atlas['charts'] if disk in c['disk_ids']);row=ch['disk_ids'].index(disk)
    assert ch['reference_key']=='10'
    source_row=ch['original_input_rows_0based'][row]
    assert r.equal(r.from_json(ch['frame']),a.fc)
    W0=r.rows(r.from_json(ch['W_coefficients_0to3'][0]),[row])
    Wraw=r.rows(at.refs[10]['W'],[source_row])
    assert r.equal(W0,r.mul(Wraw,r.inverse_values(r.mm(Wraw,a.fc))))
    members={(m['reference_key'],m['necklace_label_1based']):v['vertex_0based']
             for v in graph['vertices'] for m in v['members']}
    vertex=members[('10',source_row+1)];sourcepos=graph['source_input_labels_0based']['10'].index(source_row)
    physical={};certs={};targets=[];records=[]
    def pointkey(W,modulus=r.Q):
        val=r.mm(W,frames.candidates)
        j=next(i for i in range(146) if r.units(val)[0,i])
        val=r.mul(val,r.inverse_values(r.cols(val,[j])))
        return tuple(int(v)%modulus for part in val for v in part[0])
    for branch in range(4):
        rec=graph['constant_branches']['10/3/'+str(branch)]
        assert rec['ell']==rec['degree']==rec['determinant_mod41']==3
        mat=rec['raw_level_matrix_mod41']
        assert (mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])%41==3
        assert tuple(rec['source_A'])==tuple(at.refs[10]['A']) and tuple(rec['source_B'])==tuple(at.refs[10]['B'])
        key=rec['reference_key'];label=rec['image_indices_1based'][sourcepos]
        coarse_target=(key,label) not in members
        if coarse_target:
            co=rec['coarse'];key=co['reference_key'];label=co['image_indices_1based'][sourcepos]
            cc=next(c for c in coarse['elliptic_charts'] if c['kind']==key)
            i=cc['indices_1based'].index(label);coeff=[r.rows(r.from_json(v),[i]) for v in cc['coarse_values']]
            t=co['invariant_parameter']
        else:
            if key not in physical:
                obj=ordinary_physical_jets(at,int(key),order=3,coarse_path=data/'p41_elliptic_coarse_atlas47_verified.json.gz')
                physical[key]=obj
                certs[key]={'coefficient_sha256':[digest(r.to_json(v)) for v in obj['W']],
                            'clearing_patches':obj['clearing_patches'],'degree':3}
            obj=physical[key];assert label-1 in obj['ordinary_indices_0based']
            coeff=[r.rows(v,[label-1]) for v in obj['W']];t=rec['reference_parameter']
        assert all(v%47==0 for v in t)
        tt=r.column([list(t)]);W=r.zeros(1,73)
        for v in reversed(coeff):W=r.add(r.mul(W,tt),v)
        f=r.mm(W,a.fc);assert np.all(r.units(f));W=r.mul(W,r.inverse_values(f))
        expected_vertex=rec['target_vertices_0based'][sourcepos]
        g=graph['vertices'][expected_vertex]
        assert pointkey(W,47)==tuple(g['projective_146_mod47_real']+g['projective_146_mod47_imag'])
        assert r.equal(r.mm(W,a.fc),r.column([[1,0]]))
        targets.append(W)
        records.append({'branch_0based':branch,'actual_saved_full_level_record':rec,
                        'target_vertex_0based':expected_vertex,'used_true_elliptic_coarse_chart':coarse_target,
                        'all146_projective_reduction_coordinates_match_graph':True,
                        'W_actual_values_in_R2':r.to_json(W)[0],
                        'target_reference_key':key,'target_necklace_label_1based':label})
        print('PASS actual selected SS T3 target',branch,key,label,expected_vertex,flush=True)
    keys=[pointkey(W) for W in targets];assert len(set(keys))==4
    conjugated=[]
    for W in targets:
        F=r.mm(r.conjugate(W),r.conjugate(a.M['A1']))
        conjugated.append(pointkey(F))
    assert set(keys)==set(conjugated)
    assert pointkey(W0,47) not in [pointkey(W,47) for W in targets]
    A,B=at.refs[10]['A'],at.refs[10]['B']
    num=ck(cp(A,3),4);jj=ck(cm(num,ci(ca(num,ck(cp(B,2),27)))),1728)
    assert jj[1]==0 and jj[0]%47==10
    kernel=[ck(cp(A,2),-1),ck(B,12),ck(A,6),(0,0),(3,0)]
    for record in records:
        root=ck(tuple(record['actual_saved_full_level_record']['kernel'][0]),-1)
        value=(0,0)
        for c in reversed(kernel): value=ca(cm(value,root),tuple(c))
        assert value==(0,0)
    out={'result':'R349','source_disk_id':disk,'level':41,'auxiliary_prime':47,'precision':4,'modulus':r.Q,
         'source_reference_key':'10','source_row_0based':source_row,'source_vertex_0based':vertex,
         'actual_source_W_fc_normalized':r.to_json(W0)[0],'actual_source_model':[A,B],
         'actual_source_j_mod47four':jj[0],'actual_T3_targets_fc_normalized':[r.to_json(W)[0] for W in targets],
         'actual_target_vertices_0based':[v['target_vertex_0based'] for v in records],
         'actual_target_Frobenius_permutation_0based':[keys.index(k) for k in conjugated],
         'all_four_true_targets_Frobenius_stable':True,'all_four_targets_separate_from_source':True,
         'source_all73_equals_original_rational_SS_center':True,'physical_jet_certificates':certs,
         'actual_branches':records,'branch_records':records,
         'complete_actual_T3_support':True,'raw_level_determinant_mod41':3,'total_target_degree':4,
         'kernel_polynomial_ascending':[list(ck(cp(A,2),-1)),list(ck(B,12)),list(ck(A,6)),[0,0],[3,0]],
         'kernel_polynomial_coefficient_ring':'R2=Z/47^4[i], i^2=-1','input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),
         'runtime_seconds':round(time.monotonic()-started,3)}
    print('PASS selected SS actual T3 support',save(args.output,out),flush=True)


if __name__=='__main__':
    main()
