#!/usr/bin/env python3
"""The actual complete SS coarse T2/T3 graph, with all constant level data.

Every branch is a genuine Velu isogeny.  The raw transported level basis
retains determinant ell.  Geometric coarse vertices are deduplicated in the
published 73-dimensional embedding; extra elliptic automorphisms are kept
as multiplicities.  No Sylvester solution is asserted by this program.
"""
import argparse
from collections import Counter,deque
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def roots_three(A,B):
    from p41_coprime_kernel_dag47 import R
    from p41_etale_torsion_lift47 import QuadraticRing
    F=QuadraticRing(47);aa=tuple(x%47 for x in A);bb=tuple(x%47 for x in B)
    def psi(x,a,b,S):
        return S.sub(S.add(S.add(S.scale(S.power(x,4),3),S.scale(S.mul(a,S.power(x,2)),6)),S.scale(S.mul(b,x),12)),S.mul(a,a))
    def derivative(x,a,b,S):return S.scale(S.add(S.add(S.power(x,3),S.mul(a,x)),b),12)
    roots=[]
    for u in range(47):
        for v in range(47):
            x=(u,v)
            if psi(x,aa,bb,F)!=F.zero:continue
            for _ in range(2):x=R.sub(x,R.mul(psi(x,A,B,R),R.inverse(derivative(x,A,B,R))))
            assert psi(x,A,B,R)==R.zero
            roots.append(x)
    assert len(roots)==4 and len(set(roots))==4
    return roots


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    from p41_dag_level_transport47 import initialize,FullLevelTransport
    from p41_projective_jet_frames47 import ProjectiveJetFrames
    from p41_coprime_kernel_dag47 import roots_cubic,velu_model,R,save
    at=initialize(args.script_dir.resolve());a,r,np=at.a,at.r,at.np
    frames=ProjectiveJetFrames(a);transport=FullLevelTransport(at)
    coarse_path=a.folder/'data/p41_elliptic_coarse_atlas47_verified.json.gz';coarse=read(coarse_path)
    sources={str(j):{'j':j,'W':ref['W'],'indices_1based':list(range(1,821)),'kind':'ordinary'} for j,ref in at.refs.items()}
    for rec in coarse['elliptic_charts']:
        sources[rec['kind']]={'j':0 if rec['kind']=='CM3' else 36,
             'W':r.from_json(rec['coarse_values'][0]),'indices_1based':rec['indices_1based'],'kind':'elliptic_coarse'}
    groups={};source_inputs={}
    for key,source in sources.items():
        I=frames.projective_indices(source['W']);source_inputs[key]=[source['indices_1based'][i]-1 for i in I]
        values=r.mm(r.rows(source['W'],I),frames.candidates)
        for k,i in enumerate(I):
            re,im=values[0][k]%47,values[1][k]%47
            j=next(j for j in range(146) if (int(re[j])**2+int(im[j])**2)%47)
            x,y=int(re[j]),int(im[j]);iv=pow((x*x+y*y)%47,-1,47)
            real=(re*x+im*y)*iv%47;imag=(im*x-re*y)*iv%47
            fpkey=(source['j'],tuple(int(x) for x in real),tuple(int(x) for x in imag))
            member={'reference_key':key,'input_row_0based':i,'necklace_label_1based':source['indices_1based'][i],
                    'kind':source['kind']}
            groups.setdefault(fpkey,[]).append(member)
    assert len(groups)==3154
    vertices=[];lookup={};key_to_vertex={}
    for key in sorted(groups):
        i=len(vertices);key_to_vertex[key]=i;members=groups[key]
        rec={'vertex_0based':i,'j_mod47':key[0],'projective_146_mod47_real':list(key[1]),
             'projective_146_mod47_imag':list(key[2]),'members':members,'chosen_reference':members[0],
             'elliptic_stabilizer_order':3 if members[0]['reference_key']=='CM3' else 2 if members[0]['reference_key']=='CM4' else 1,
             'F47_rational':not any(key[2])}
        vertices.append(rec)
        for member in members:
            mk=(member['reference_key'],member['necklace_label_1based']);assert mk not in lookup;lookup[mk]=i
    frobenius=[]
    for rec in vertices:
        key=(rec['j_mod47'],tuple(rec['projective_146_mod47_real']),tuple(-x%47 for x in rec['projective_146_mod47_imag']))
        frobenius.append(key_to_vertex[key])
    assert all(frobenius[frobenius[i]]==i for i in range(3154))
    assert sum(i==j for i,j in enumerate(frobenius))==110
    data={'level':41,'auxiliary_prime':47,'modulus':47**4,'complete':False,
          'vertices':vertices,'frobenius_permutation_0based':frobenius,'source_input_labels_0based':source_inputs,
          'constant_branches':{},'source_sha256':sha(__file__),'input_sha256':dict(a.inputs,**{coarse_path.name:sha(coarse_path)})}
    if args.output.exists():
        old=read(args.output)
        assert old['source_sha256']==data['source_sha256'] and old['vertices']==vertices
        data['constant_branches']=old['constant_branches']
    def target_vertex(record,row):
        key=record['reference_key'];label=record['image_indices_1based'][row]
        if (key,label) in lookup:return lookup[(key,label)]
        assert key in ['0','36']
        co=record['coarse'];return lookup[(co['reference_key'],co['image_indices_1based'][row])]
    started=time.monotonic()
    for key,source in sources.items():
        ref=transport.refs[key];A,B=ref['A'],ref['B'];P0,Q0=transport.F.point(ref['P']),transport.F.point(ref['Q'])
        I=source_inputs[key]
        for ell,roots in [(2,roots_cubic(A,B)),(3,roots_three(A,B))]:
            for branch,x in enumerate(roots):
                name=key+'/'+str(ell)+'/'+str(branch)
                if name in data['constant_branches']:continue
                kernel=[R.neg(x),R.one];At,Bt=velu_model(ell,kernel,A,B)
                node={'ell':ell,'source_A':A,'source_B':B,'A':At,'B':Bt,'kernel':kernel}
                P,Q=transport.raw_pair(node,P0,Q0)
                rec=transport.record(At,Bt,P,Q,ell,I)
                rec.update(node);rec.update(source_reference_key=key,branch_0based=branch)
                rec['target_vertices_0based']=[target_vertex(rec,k) for k in range(len(I))]
                data['constant_branches'][name]=rec
                data['reference_point_tables']={k:v['certificate'] for k,v in transport.lookup_tables.items()}
                data['input_sha256']=dict(a.inputs,**{coarse_path.name:sha(coarse_path)})
                save(args.output,data)
                print('Actual SS branches',len(data['constant_branches']),'/49',name,'seconds',round(time.monotonic()-started,2),flush=True)
    assert len(data['constant_branches'])==49
    adjacency={};member_checks=0
    for ell in [2,3]:
        possible={}
        for key,I in source_inputs.items():
            branches=[data['constant_branches'][key+'/'+str(ell)+'/'+str(k)] for k in range(ell+1)]
            for row,label in enumerate(I):
                vertex=lookup[(key,label+1)]
                neigh=[br['target_vertices_0based'][row] for br in branches]
                if vertex in possible:
                    assert Counter(possible[vertex])==Counter(neigh),('coarse multiplicity mismatch',ell,key,label+1)
                    member_checks+=1
                else:possible[vertex]=neigh
        assert len(possible)==3154
        rows=[possible[i] for i in range(3154)];adjacency[str(ell)]=rows
        for i,row in enumerate(rows):
            assert len(row)==ell+1
            assert Counter(frobenius[j] for j in row)==Counter(rows[frobenius[i]])
            for j,m in Counter(row).items():
                assert vertices[j]['elliptic_stabilizer_order']*m==vertices[i]['elliptic_stabilizer_order']*rows[j].count(i)
    A2,A3=adjacency['2'],adjacency['3']
    for i in range(3154):assert Counter(k for j in A2[i] for k in A3[j])==Counter(k for j in A3[i] for k in A2[j])
    seen={0};queue=deque([0])
    while queue:
        i=queue.popleft()
        for j in A2[i]+A3[i]:
            if j not in seen:seen.add(j);queue.append(j)
    data.update(complete=True,adjacency=adjacency,
         all_duplicate_coarse_label_adjacencies_match=True,duplicate_checks=member_checks,
         all_Frobenius_equivariant=True,all_stabilizer_weighted_symmetry=True,
         T2_T3_commute_exactly=True,component_of_vertex0_size=len(seen),
         status='Complete actual SS coarse Hecke graph; no Abel constant solution claimed')
    digest=save(args.output,data)
    print('PASS3154 vertices,49 actual branches, duplicate/Hecke/Frobenius/weighted checks; component',len(seen),'SHA',digest,flush=True)


if __name__=='__main__':main()
