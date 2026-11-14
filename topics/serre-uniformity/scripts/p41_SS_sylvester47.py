#!/usr/bin/env python3
"""Exact finite-field polynomial inverse for the actual SS Hecke Sylvester map.

For A X-X H=Y and P(H)=0, the Horner divided difference D(Y) satisfies
P(A)X=D(Y).  The full inverse P(A)^-1 is computed over F47 by FLINT and
stored in compressed row blocks.  Actual right sides, when supplied, are
solved digit by digit and checked in the original Sylvester equation.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from flint import nmod_poly,nmod_mat

P=47

def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def digest(a):return hashlib.sha256(np.asarray(a,dtype=np.uint8).tobytes()).hexdigest()

def apply_A(X,adj,q=P,combination=2):
    Y=np.zeros_like(X)
    for k in range(3):Y+=X[adj['2'][:,k]]
    for k in range(4):Y+=combination*X[adj['3'][:,k]]
    return Y%q

def matrix_product(A,B,q=P):
    k=A.shape[1]
    assert k*(q-1)**2<2**53
    assert np.all((A>=0)&(A<q)) and np.all((B>=0)&(B<q))
    return (A.astype(np.float64)@B.astype(np.float64)).astype(np.int64)%q

def field_matrix(fields,q):
    H=np.zeros((54,54),dtype=np.int64);offset=0
    for f in fields:
        pp=f['factor_descending'];d=len(pp)-1
        for j in range(d-1):H[offset+j,offset+j+1]=1
        H[offset+d-1,offset:offset+d]=[-int(x)%q for x in reversed(pp[1:])]
        offset+=d
    assert offset==54
    return H

def build_inverse(graph,fields,cache,combination=2,multiplication=None,kernel=None,regularize=None):
    cache.mkdir(parents=True,exist_ok=True);n=len(graph['vertices'])
    assert n==3154 and graph['T2_T3_commute_exactly'] and graph['complete']
    adj={s:np.asarray(graph['adjacency'][s],dtype=np.int64) for s in ['2','3']}
    H=field_matrix(fields,P)
    if multiplication is not None:
        Hnew=(np.asarray(multiplication['2'],dtype=np.int64)+combination*np.asarray(multiplication['3'],dtype=np.int64))%P
        if combination==2:assert np.array_equal(Hnew,H)
        H=Hnew
    else:assert combination==2
    pp=nmod_mat(54,54,H.ravel().tolist(),P).charpoly()
    coeff=[int(x) for x in reversed(pp.coeffs())]
    assert len(coeff)==55 and coeff[0]==1
    v=np.eye(54,dtype=np.int64)
    for c in coeff[1:]:v=matrix_product(v,H);v.flat[::55]=(v.flat[::55]+c)%P
    assert not np.any(v)
    meta_path=cache/'inverse_manifest.json'
    if meta_path.exists():
        meta=read(meta_path)
        assert meta['characteristic_polynomial_descending_mod47']==coeff and meta['combination_T2_plus_cT3']==combination
        assert meta.get('regularized_vertex_0based')==regularize
        assert all(sha(cache/f['file'])==f['sha256'] for f in meta['inverse_row_chunks'])
        return meta
    start=time.time();poly_path=cache/'P_A_mod47.npy'
    if poly_path.exists():A=np.asarray(np.load(poly_path),dtype=np.int64)
    else:
        A=np.eye(n,dtype=np.int64)
        for k,c in enumerate(coeff[1:],1):
            A=apply_A(A,adj,combination=combination);A.flat[::n+1]=(A.flat[::n+1]+c)%P
            if k%6==0:print('P(A) Horner',k,54,'seconds',round(time.time()-start,2),flush=True)
        np.save(poly_path,A.astype(np.uint8))
    original_fingerprint=digest(A)
    if regularize is not None:
        assert kernel is not None and kernel['nullity']==1
        v=np.asarray(kernel['right_null_vector_mod47'],dtype=np.int64)
        mass=np.asarray([pow(x['elliptic_stabilizer_order'],-1,P) for x in graph['vertices']],dtype=np.int64)
        left=mass*v%P
        assert not np.any((A@v)%P) and not np.any((left@A)%P)
        assert v[regularize] and left[regularize]
        A[regularize,:]=0;A[regularize,regularize]=1
    fingerprint=digest(A)
    print('P(A) constructed; begin exact FLINT inverse',n,round(time.time()-start,2),flush=True)
    M=nmod_mat(n,n,A.ravel().tolist(),P)
    del A
    try:inverse=M.inv()
    except (ZeroDivisionError,ValueError) as e:
        (cache/'singular.json').write_text(json.dumps({'combination':combination,'P_A_sha256':fingerprint,'error':str(e)},indent=2)+'\n')
        raise
    del M
    print('Exact inverse complete',round(time.time()-start,2),flush=True)
    B=np.asarray(inverse.tolist(),dtype=np.uint8);del inverse
    chunks=[]
    for first in range(0,n,384):
        block=B[first:first+384];name='P_A_inverse_rows_'+str(first).zfill(4)+'.bin.gz'
        out=cache/name;out.write_bytes(gzip.compress(block.tobytes(),mtime=0))
        chunks.append({'file':name,'first_row_0based':first,'rows':len(block),'columns':n,
                       'sha256':sha(out),'bytes':out.stat().st_size})
    meta={'level':41,'auxiliary_prime':47,'vertices':n,'combination_T2_plus_cT3':combination,
          'exact_FLINT_inverse_succeeded':True,'characteristic_polynomial_descending_mod47':coeff,
          'P_A_sha256':fingerprint,'inverse_matrix_sha256':digest(B),'inverse_row_chunks':chunks,
          'original_P_A_sha256':original_fingerprint,'regularized_vertex_0based':regularize,
          'rank_one_kernel':kernel,
          'field_matrix_mod47':H.tolist(),'actual_rhs_solved':False,
          'source_sha256':sha(__file__)}
    meta_path.write_text(json.dumps(meta,indent=2)+'\n')
    print('Saved exact inverse in',len(chunks),'row chunks; actual RHS not yet supplied',flush=True)
    return meta

def load_inverse(cache,meta):
    blocks=[]
    for f in meta['inverse_row_chunks']:
        p=cache/f['file'];assert sha(p)==f['sha256']
        block=np.frombuffer(gzip.decompress(p.read_bytes()),dtype=np.uint8).reshape(f['rows'],f['columns'])
        blocks.append(block)
    B=np.concatenate(blocks).astype(np.int64);assert digest(B)==meta['inverse_matrix_sha256']
    return B

def solve_mod47(Y,adj,H,coeff,B,combination=2):
    Z=np.zeros_like(Y);F=np.eye(54,dtype=np.int64)
    for c in coeff[1:]:
        Z=(apply_A(Z,adj,combination=combination)+matrix_product(Y,F))%P
        F=matrix_product(H,F);F.flat[::55]=(F.flat[::55]+c)%P
    assert not np.any(F)
    X=matrix_product(B,Z)
    assert np.array_equal((apply_A(X,adj,combination=combination)-matrix_product(X,H))%P,Y)
    return X

def apply_ell(X,adj,ell,q):
    return sum((X[adj[ell][:,j]] for j in range(adj[ell].shape[1])),np.zeros_like(X))%q

def independent_columns(M):
    A=M.copy()%P;rr=0;cols=[]
    for j in range(A.shape[1]):
        nz=np.flatnonzero(A[rr:,j])
        if not len(nz):continue
        k=rr+int(nz[0]);A[[rr,k]]=A[[k,rr]]
        A[rr]=A[rr]*pow(int(A[rr,j]),-1,P)%P
        factor=A[:,j].copy();factor[rr]=0
        A=(A-factor[:,None]*A[rr])%P
        cols.append(j);rr+=1
        if rr==A.shape[0]:break
    assert rr==54
    return cols

def solve_actual(graph,rhs,cache,meta,output):
    assert meta['regularized_vertex_0based']==0 and meta['combination_T2_plus_cT3']==2
    adj={s:np.asarray(graph['adjacency'][s],dtype=np.int64) for s in ['2','3']}
    mats={s:np.asarray(rhs['multiplication_matrices'][s],dtype=np.int64) for s in ['2','3']}
    Ys={s:np.asarray(rhs['rhs'][s],dtype=np.int64) for s in ['2','3']}
    q=47**3;assert rhs['modulus']==q
    B=load_inverse(cache,meta);H=np.asarray(meta['field_matrix_mod47'],dtype=np.int64)
    kernel=meta['rank_one_kernel'];v=np.asarray(kernel['right_null_vector_mod47'],dtype=np.int64)
    assert v[0]==1
    eig=kernel['eigenvalues_A2_A3']
    C=np.concatenate([(eig[s]*np.eye(54,dtype=np.int64)-mats[s])%P for s in ['2','3']],axis=1)
    columns=independent_columns(C)
    small=np.asarray(nmod_mat(54,54,C[:,columns].ravel().tolist(),P).inv().tolist(),dtype=np.int64)
    for s in ['2','3']:assert np.array_equal(apply_ell(v[:,None],adj,s,P)[:,0],eig[s]*v%P)
    coeff=meta['characteristic_polynomial_descending_mod47']
    def joint(Y2,Y3):
        Y=(Y2+2*Y3)%P;D=np.zeros_like(Y);F=np.eye(54,dtype=np.int64)
        for c in coeff[1:]:
            D=(apply_A(D,adj)+matrix_product(Y,F))%P
            F=matrix_product(H,F);F.flat[::55]=(F.flat[::55]+c)%P
        assert not np.any(F)
        D[0,:]=0;X0=matrix_product(B,D)
        residual=[]
        for s,Ys0 in [('2',Y2),('3',Y3)]:
            Z=(Ys0-apply_ell(X0,adj,s,P)+matrix_product(X0,mats[s]%P))%P
            assert np.array_equal(Z,v[:,None]*Z[0]%P),('residual not in true rank-one kernel',s)
            residual.extend(Z[0].tolist())
        row=np.asarray(residual,dtype=np.int64)[columns][None,:]
        c=matrix_product(row,small)[0]
        X=(X0+v[:,None]*c)%P
        for s,Ys0 in [('2',Y2),('3',Y3)]:
            assert np.array_equal((apply_ell(X,adj,s,P)-matrix_product(X,mats[s]%P))%P,Ys0)
        return X
    n=len(graph['vertices']);X=np.zeros((n,54,2),dtype=np.int64)
    for part in range(2):
        for k in range(3):
            residual={}
            for s in ['2','3']:
                E=(Ys[s][:,:,part]-apply_ell(X[:,:,part],adj,s,q)+matrix_product(X[:,:,part],mats[s]%q,q))%q
                assert not np.any(E%(47**k))
                residual[s]=(E//(47**k))%P
            correction=joint(residual['2'],residual['3'])
            X[:,:,part]=(X[:,:,part]+(47**k)*correction)%q
            print('Actual joint Sylvester solved part',part,'precision',k+1,flush=True)
    for s in ['2','3']:
        for part in range(2):
            assert np.array_equal((apply_ell(X[:,:,part],adj,s,q)-matrix_product(X[:,:,part],mats[s]%q,q))%q,Ys[s][:,:,part])
    anchors=[]
    for a in rhs['known_CM_anchors']:
        i=a['vertex_0based'];want=np.asarray(a['expected_U_graph_center_cyclic_coordinates_mod47cubed'],dtype=np.int64)
        assert np.array_equal(X[i],want),('independent CM anchor mismatch',a['discriminant'])
        anchors.append({'discriminant':a['discriminant'],'vertex_0based':i,'all54_complex_coordinates_match':True})
    rational=[]
    for d in rhs['rational_disk_maps']:
        i=d['vertex_0based'];tiny=np.asarray(d['tiny_C_to_rational_center_mod47cubed'],dtype=np.int64)
        U=(X[i]+20*tiny)%q
        assert not np.any(U[:,1]),('true rational-center imaginary residue',d['disk_id'])
        rational.append({'disk_id':d['disk_id'],'vertex_0based':i,
                         'U_cyclic_coordinates_mod47cubed':U[:,0].astype(int).tolist()})
    assert len(rational)==110
    out={'level':41,'auxiliary_prime':47,'precision':3,'modulus':q,'geometric_vertices':n,
         'all3154_actual_U_Abel_coordinates_computed':True,
         'graph_U_cyclic_coordinates_mod47cubed':X.astype(int).tolist(),
         'rational_SS_center_constants':rational,'all110_rational_SS_center_constants_complete':True,
         'both_actual_Hecke_equations_verified':True,'independent_CM_anchor_checks':anchors,
         'CM_anchors_used_to_solve':False,'regularization_is_artificial_and_then_removed_by_joint_Hecke_equations':True,
         'rank_one_vertex_eigenvalues_mod47':eig,'small_joint_constraint_rank':54,
         'small_joint_unit_columns_0based':columns,
         'complete_local_QC_heights':False,'complete_common_roots':False,
         'inverse_manifest_sha256':sha(cache/'inverse_manifest.json'),'source_sha256':sha(__file__)}
    output.write_bytes(gzip.compress((json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0))
    print('PASS all3154 genuine Abel constants, both Hecke equations, three independent CM anchors, all110 rational centers',flush=True)
    print('Saved',output,sha(output),flush=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--graph',type=Path,required=True)
    ap.add_argument('--fields',type=Path,required=True)
    ap.add_argument('--cache-dir',type=Path,required=True)
    ap.add_argument('--combination',type=int,default=2)
    ap.add_argument('--rhs',type=Path)
    ap.add_argument('--kernel',type=Path)
    ap.add_argument('--regularize-vertex',type=int)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args();g=read(args.graph);fields=read(args.fields)['fields']
    rhs=read(args.rhs) if args.rhs else None
    meta=build_inverse(g,fields,args.cache_dir,args.combination,rhs['multiplication_matrices'] if rhs else None,
                       read(args.kernel) if args.kernel else None,args.regularize_vertex)
    meta['graph_sha256']=sha(args.graph);meta['fields_sha256']=sha(args.fields)
    (args.cache_dir/'inverse_manifest.json').write_text(json.dumps(meta,indent=2)+'\n')
    if args.output:
        assert rhs is not None
        solve_actual(g,rhs,args.cache_dir,meta,args.output)

if __name__=='__main__':main()
