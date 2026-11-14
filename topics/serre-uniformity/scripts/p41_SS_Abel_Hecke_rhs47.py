#!/usr/bin/env python3
"""Actual all-SS tiny right hand sides for the Hecke Abel Sylvester system.

Unknown row X_i is the cyclic class coordinate of U_i=20P_i-D.  The exact
equations are A_ell X-X M_ell=-20*sum tiny(P_target-P_reference), modulo47^3.
Every target is checked against all73 embedded point coordinates modulo47^4.
Each computed chart is checkpointed separately before further work.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time

P=47;Q=P**4;Q3=P**3


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--graph',type=Path,required=True)
    ap.add_argument('--lie-tiny',type=Path,required=True)
    ap.add_argument('--rational-atlas',type=Path,required=True)
    ap.add_argument('--polynomials',type=Path,required=True)
    ap.add_argument('--work-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    from p41_elliptic_coarse_atlas47 import setup,Series
    from p41_projective_jet_frames47 import ProjectiveJetFrames,ordinary_physical_jets,matrix_digest
    from p41_global_qc_polynomials47 import Field
    from p41_coprime_kernel_dag47 import save
    import numpy as np
    graph=read(args.graph);assert graph['complete'] and graph['T2_T3_commute_exactly']
    lie=read(args.lie_tiny);rational=read(args.rational_atlas);polynomials=read(args.polynomials)
    at=setup(args.script_dir.resolve());a,r=at.a,at.r;frames=ProjectiveJetFrames(a)
    coarse_path=a.folder/'data/p41_elliptic_coarse_atlas47_verified.json.gz';coarse=read(coarse_path)
    full_path=a.folder/'data/p41_full_chow_heegner_certificate.json.gz';full=read(full_path)
    inputs={path.name:sha(path) for path in [args.graph,args.lie_tiny,args.rational_atlas,args.polynomials,coarse_path,full_path]}
    inverse=r.from_json(lie['divided_Lie_to_cyclic_mod47cubed'],Q3)
    sources={str(j):{'W':ref['W'],'labels':list(range(1,821))} for j,ref in at.refs.items()}
    for rec in coarse['elliptic_charts']:
        sources[rec['kind']]={'W':r.from_json(rec['coarse_values'][0]),'labels':rec['indices_1based']}
    label_row={key:{label:i for i,label in enumerate(source['labels'])} for key,source in sources.items()}
    N=len(graph['vertices']);assert N==3154
    chosen_by_source={};member_vertex={}
    for vertex in graph['vertices']:
        i=vertex['vertex_0based'];member=vertex['chosen_reference'];key=member['reference_key']
        chosen_by_source.setdefault(key,{})[member['input_row_0based']]=i
        for item in vertex['members']:member_vertex[(item['reference_key'],item['necklace_label_1based'])]=i
    multiplication={}
    for ell in [2,3]:
        k=[m['n'] for m in full['row_metadata']].index(ell);M=np.zeros((54,54),dtype=np.int64);offset=0
        for field in full['fields']:
            F=Field(field['factor_descending']);t=F.val(field['directions'][k][0])
            for j in range(F.d):M[offset+j,offset:offset+F.d]=np.asarray(F.mul([0]*j+[1],t),dtype=np.int64)%Q3
            offset+=F.d
        multiplication[str(ell)]=M.astype(int).tolist()
    data={'level':41,'auxiliary_prime':47,'modulus':Q3,'precision':3,'complete':False,
          'equation':'A_ell X-X M_ell=rhs_ell; X_i represents U_i=20P_i-D in the R89 eight-field cyclic basis',
          'rhs_sign_and_scale':-20,'point_verification_modulus':Q,
          'multiplication_matrices':multiplication,'charts':[],'branch_checks':[],
          'input_sha256':inputs,'source_sha256':sha(__file__)}
    save(args.output,data);args.work_dir.mkdir(parents=True,exist_ok=True)
    Wcoeff=[r.zeros(N,73) for _ in range(4)]
    tinycoeff=[r.zeros(N,54) for _ in range(3)]
    Vframe,Ccoord=r.zeros(N,73),r.zeros(N,73);basecoord=r.zeros(N,1)
    covered=set();started=time.monotonic()
    for key,chosen in chosen_by_source.items():
        source=sources[key]
        for chart in frames.iter_charts(source['W'],indices=sorted(chosen),order=3,max_points=64,label=key):
            I=chart['indices_0based'];vertices=[chosen[i] for i in I]
            assert not covered.intersection(vertices);covered.update(vertices)
            wk=[r.mm(w,a.K1) for w in chart['W'][:3]]
            omega=Series(a,3).mul(wk,chart['inverse_Hc'][:3])
            tiny=[]
            for k in range(1,4):
                c=a.scale(a.reduce(omega[k-1],Q3),P**(k-1)*pow(k,-1,Q3),Q3)
                tiny.append(r.mm(c,inverse,Q3))
            for part in range(2):
                for k in range(4):Wcoeff[k][part][vertices]=chart['W'][k][part]
                for k in range(3):tinycoeff[k][part][vertices]=tiny[k][part]
                Vframe[part][vertices]=chart['frame'][part][:,0][None,:]
                Ccoord[part][vertices]=chart['coordinate'][part][:,0][None,:]
                basecoord[part][vertices]=chart['coordinate_base_value'][part]
            ch={'chart_0based':len(data['charts']),'reference_key':key,'vertices_0based':vertices,
                'source_input_rows_0based':I,'frame':r.to_json(chart['frame']),
                'coordinate':r.to_json(chart['coordinate']),'coordinate_base_value':r.to_json(chart['coordinate_base_value']),
                'W_coefficients_0to3':[r.to_json(w) for w in chart['W']],
                'canonical_differential_coefficients_0to2':[r.to_json(v) for v in omega],
                'tiny_cyclic_coefficients_1to3_in_y':[r.to_json(v) for v in tiny],
                'parameter':'y=(W*c/(W*v)-coordinate_base_value)/47',
                'H_v_sha256':matrix_digest(chart['H_matrix'])}
            path=args.work_dir/('chart-'+str(ch['chart_0based']).zfill(3)+'.json.gz');chsha=save(path,ch)
            data['charts'].append({'chart_0based':ch['chart_0based'],'reference_key':key,'vertices_0based':vertices,
                                   'checkpoint_file':path.name,'checkpoint_sha256':chsha})
            data['chart_vertices_completed']=len(covered);save(args.output,data)
        print('True SS differential/tiny charts',key,len(chosen),'total',len(covered),'seconds',round(time.monotonic()-started,2),flush=True)
    assert len(covered)==N
    physical={}
    for j in at.refs:
        physical[str(j)]=ordinary_physical_jets(at,j,order=3)['W']
        print('Physical ordinary jets',j,flush=True)
    for rec in coarse['elliptic_charts']:physical[rec['kind']]=[r.from_json(v) for v in rec['coarse_values']]
    def evaluate_physical(key,labels,parameter):
        ids=[label_row[key][label] for label in labels]
        out=r.zeros(len(ids),73);t=r.column([list(parameter)]*len(ids))
        for coeff in reversed(physical[key]):out=r.add(r.mul(out,t),r.rows(coeff,ids))
        return out
    def rowdot(X,Y):
        return ((X[0]*Y[0]-X[1]*Y[1]).sum(axis=1)[:,None]%Q,
                (X[0]*Y[1]+X[1]*Y[0]).sum(axis=1)[:,None]%Q)
    def tiny_to_points(W,vertices):
        frame=r.rows(Vframe,vertices);coord=r.rows(Ccoord,vertices)
        fv=rowdot(W,frame);assert np.all(r.units(fv))
        z=r.sub(r.mul(rowdot(W,coord),r.inverse_values(fv)),r.rows(basecoord,vertices))
        assert all(not np.any(v%P) for v in z)
        normalized=r.mul(W,r.inverse_values(fv));recovered=r.zeros(len(vertices),73)
        for coeff in reversed(Wcoeff):recovered=r.add(r.mul(recovered,z),r.rows(coeff,vertices))
        assert r.equal(recovered,normalized),'Actual target fails the full73 coordinate chart check'
        y=tuple(v//P for v in z);delta=r.zeros(len(vertices),54)
        for coeff in reversed(tinycoeff):delta=r.mul(r.add(delta,r.rows(coeff,vertices),Q3),y,Q3)
        return delta,z
    rhs={str(ell):r.zeros(N,54) for ell in [2,3]};counts={str(ell):np.zeros(N,dtype=np.int64) for ell in [2,3]}
    for name,branch in graph['constant_branches'].items():
        key=branch['source_reference_key'];ell=branch['ell'];I=graph['source_input_labels_0based'][key]
        selected=[];source_vertices=[]
        for row,label in enumerate(I):
            input_row=label_row[key][label+1]
            if input_row in chosen_by_source[key]:selected.append(row);source_vertices.append(chosen_by_source[key][input_row])
        target_vertices=[branch['target_vertices_0based'][row] for row in selected]
        W=r.zeros(len(selected),73);regular=[];coarselist=[]
        for outrow,row in enumerate(selected):
            label=branch['image_indices_1based'][row]
            if (branch['reference_key'],label) in member_vertex:regular.append((outrow,label))
            else:coarselist.append((outrow,branch['coarse']['image_indices_1based'][row]))
        for items,usecoarse in [(regular,False),(coarselist,True)]:
            if not items:continue
            rec=branch['coarse'] if usecoarse else branch
            tkey=rec['reference_key'];t=rec['invariant_parameter'] if usecoarse else rec['reference_parameter']
            values=evaluate_physical(tkey,[label for i,label in items],t)
            for part in range(2):W[part][[i for i,label in items]]=values[part]
        delta,z=tiny_to_points(W,target_vertices)
        for part in range(2):rhs[str(ell)][part][source_vertices]=(rhs[str(ell)][part][source_vertices]-20*delta[part])%Q3
        counts[str(ell)][source_vertices]+=1
        data['branch_checks'].append({'branch':name,'ell':ell,'source_vertices_count':len(source_vertices),
            'true_elliptic_target_count':len(coarselist),'all73_projective_target_coordinates_match':True,
            'actual_target_parameter_sha256':matrix_digest(z),'tiny_difference_sha256':matrix_digest(delta)})
        save(args.output,data)
        print('Actual Hecke RHS',name,'source vertices',len(source_vertices),'elliptic',len(coarselist),flush=True)
    assert all(np.all(counts[str(ell)]==ell+1) for ell in [2,3])
    # Map each R228 rational center to this actual graph center, preserving its tiny unit.
    geometric={tuple(v['projective_146_mod47_real']):v['vertex_0based'] for v in graph['vertices'] if v['F47_rational']}
    maps=[]
    for disk in rational['SS_disk_records']:
        vertex=geometric[tuple(disk['rational_projective_146_mod47'])]
        ch=rational['charts'][disk['chart_0based']]
        W=r.rows(r.from_json(ch['W_coefficients_0to3'][0]),[disk['chart_row_0based']])
        delta,z=tiny_to_points(W,[vertex])
        maps.append({'disk_id':disk['disk_id'],'vertex_0based':vertex,
              'tiny_C_to_rational_center_mod47cubed':r.to_json(delta)[0],
              'graph_parameter_z_of_rational_center_mod47four':r.to_json(z)[0][0]})
    mapbyid={m['disk_id']:m for m in maps}
    r3=np.asarray([x for ff in polynomials['fields'] for x in ff['r_minus3']],dtype=np.int64)%Q3
    anchors=[]
    for anchor in lie['known_CM_anchored_disks']:
        m=mapbyid[anchor['disk_id']];aa=np.asarray(anchor['actual_center_cyclic_coordinates_mod47cubed'],dtype=np.int64)
        Urational=((r3+20*aa)[None,:]%Q3,np.zeros((1,54),dtype=np.int64))
        delta=r.from_json([m['tiny_C_to_rational_center_mod47cubed']],Q3)
        expected=r.sub(Urational,a.scale(delta,20,Q3),Q3)
        anchors.append({'discriminant':anchor['discriminant'],'disk_id':anchor['disk_id'],'vertex_0based':m['vertex_0based'],
            'expected_U_graph_center_cyclic_coordinates_mod47cubed':r.to_json(expected)[0]})
    data.update(complete=True,rhs={ell:r.to_json(value) for ell,value in rhs.items()},
         rational_disk_maps=maps,known_CM_anchors=anchors,
         all3154_vertices_have_ell_plus1_actual_branches=True,
         all22078_actual_targets_match_all73_projective_coordinates=True,
         total_actual_target_checks=sum(check['source_vertices_count'] for check in data['branch_checks']),
         tiny_atlas_checkpoint_files=len(data['charts']),
         input_sha256=dict(a.inputs,**inputs),
         status='Actual complete Sylvester right hand sides; solving for the center constants is separate')
    assert data['total_actual_target_checks']==3154*7
    digest=save(args.output,data)
    print('PASS3154 actual SS Abel right hand sides;22078 complete target coordinate checks;3 CM anchors;SHA',digest,flush=True)


if __name__=='__main__':main()
