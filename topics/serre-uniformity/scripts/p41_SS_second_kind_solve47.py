#!/usr/bin/env python3
"""Solve the actual Frobenius-even T3 system and all110 rational SS nu integrals."""
import argparse,gzip,hashlib,json,time
from pathlib import Path
import numpy as np
from flint import nmod_mat

P=47;Q=P**3
def read(p):
    b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(gzip.compress((json.dumps(o,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0))
    return sha(p)
def mm(A,B,q):
    assert A.shape[1]*(q-1)**2<2**53
    return (A.astype(np.float64)@B.astype(np.float64)).astype(np.int64)%q
def r2mm(A,B,q):
    return np.stack(((mm(A[:,:,0],B[:,:,0],q)-mm(A[:,:,1],B[:,:,1],q))%q,
                     (mm(A[:,:,0],B[:,:,1],q)+mm(A[:,:,1],B[:,:,0],q))%q),axis=2)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--graph',type=Path,required=True)
    ap.add_argument('--rhs',type=Path,required=True)
    ap.add_argument('--kernel',type=Path,required=True)
    ap.add_argument('--cache-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();args.cache_dir.mkdir(parents=True,exist_ok=True)
    g=read(args.graph);rhs=read(args.rhs);oldkernel=read(args.kernel)
    assert rhs['complete_actual_second_kind_Hecke_rhs'] and rhs['modulus']==Q
    tau=np.asarray(g['frobenius_permutation_0based'],dtype=np.int64)
    reps=[i for i,j in enumerate(tau) if i<=j];N=len(reps);assert N==1632
    orbit=np.zeros(3154,dtype=np.int64)
    for j,i in enumerate(reps):orbit[i]=orbit[tau[i]]=j
    adjacency=np.asarray([[int(orbit[j]) for j in g['adjacency']['3'][i]] for i in reps],dtype=np.int64)
    def A(X,q):return sum((X[adjacency[:,k]] for k in range(4)),np.zeros_like(X))%q
    H=np.asarray(rhs['T3_rational_matrix'],dtype=np.int64)%Q
    poly=nmod_mat(54,54,(H%P).ravel().tolist(),P).charpoly()
    coeff=[int(x) for x in reversed(poly.coeffs())];assert len(coeff)==55 and coeff[0]==1
    V=np.asarray(oldkernel['right_kernel_mod47'],dtype=np.int64)
    fullv=V.sum(axis=1)%P;v=fullv[reps]
    assert np.array_equal(fullv,fullv[tau]) and v[0]==1
    assert np.array_equal(A(v[:,None],P)[:,0],33*v%P)
    weights=np.zeros(N,dtype=np.int64)
    for i in rhs['B_anchor_vertices_0based']:weights[orbit[i]]+=1
    bmass=int(weights@v)%P;assert bmass==10
    metadata=args.cache_dir/'inverse_manifest.json'
    if metadata.exists():
        meta=json.loads(metadata.read_text())
        assert meta['graph_sha256']==sha(args.graph) and meta['characteristic_polynomial_descending_mod47']==coeff
        blocks=[]
        for chunk in meta['inverse_chunks']:
            p=args.cache_dir/chunk['file'];assert sha(p)==chunk['sha256']
            blocks.append(np.frombuffer(gzip.decompress(p.read_bytes()),dtype=np.uint8).reshape(chunk['rows'],N))
        B=np.concatenate(blocks).astype(np.int64)
    else:
        start=time.monotonic();M=np.eye(N,dtype=np.int64)
        for k,c in enumerate(coeff[1:],1):
            M=A(M,P);M.flat[::N+1]=(M.flat[::N+1]+c)%P
            if k%9==0:print('True even P(A3)',k,'/54',round(time.monotonic()-start,2),flush=True)
        assert not np.any(M@v%P)
        original_digest=hashlib.sha256(M.astype(np.uint8).tobytes()).hexdigest()
        M[0,:]=0;M[0,0]=1
        fm=nmod_mat(N,N,M.ravel().tolist(),P)
        print('Begin exact even inverse',N,flush=True)
        B=np.asarray(fm.inv().tolist(),dtype=np.int64)
        assert not np.any((mm(M,B,P)-np.eye(N,dtype=np.int64))%P)
        chunks=[]
        for first in range(0,N,384):
            block=B[first:first+384].astype(np.uint8)
            p=args.cache_dir/('inverse_rows_'+str(first).zfill(4)+'.bin.gz')
            p.write_bytes(gzip.compress(block.tobytes(),mtime=0))
            chunks.append({'file':p.name,'first_row_0based':first,'rows':len(block),'columns':N,'sha256':sha(p)})
        meta={'result':'R247-even-inverse','vertices':N,'graph_sha256':sha(args.graph),
              'characteristic_polynomial_descending_mod47':coeff,
              'P_A3_even_rank':N-1,'P_A3_even_nullity':1,'P_A3_even_sha256':original_digest,
              'right_kernel_mod47':v.astype(int).tolist(),'kernel_A3_eigenvalue':33,
              'regularized_row_0based':0,'inverse_chunks':chunks,
              'B_anchor_mass_of_kernel_mod47':bmass,'full_inverse_identity_verified':True}
        metadata.write_text(json.dumps(meta,sort_keys=True,indent=2)+'\n')
        print('Complete exact inverse and unit kernel anchor',round(time.monotonic()-start,2),flush=True)
    def solve_digit(Y,target):
        D=np.zeros_like(Y);F=np.eye(54,dtype=np.int64)
        for c in coeff[1:]:
            D=(A(D,P)+mm(Y,F,P))%P
            F=mm(H%P,F,P);F.flat[::55]=(F.flat[::55]+c)%P
        assert not np.any(F)
        D[0]=0;X0=mm(B,D,P)
        cc=(target-weights@X0)*pow(bmass,-1,P)%P
        X=(X0+v[:,None]*cc)%P
        assert np.array_equal((A(X,P)-mm(X,H%P,P))%P,Y),'actual T3 equation fails after B anchor'
        assert np.array_equal(weights@X%P,target)
        return X
    Yfull=np.asarray(rhs['Frobenius_even_rhs_mod47cubed'],dtype=np.int64)
    assert np.array_equal(Yfull,Yfull[tau]);Y=Yfull[reps]
    target=np.asarray(rhs['B_anchor_sum_even_N_mod47cubed'],dtype=np.int64)
    X=np.zeros((N,54),dtype=np.int64)
    for k in range(3):
        E=(Y-A(X,Q)+mm(X,H,Q))%Q;Bres=(target-weights@X)%Q
        assert not np.any(E%(P**k)) and not np.any(Bres%(P**k))
        correction=solve_digit(E//(P**k)%P,Bres//(P**k)%P)
        X=(X+P**k*correction)%Q
        print('Actual even second-kind solution precision',k+1,flush=True)
    assert np.array_equal((A(X,Q)-mm(X,H,Q))%Q,Y)
    assert np.array_equal(weights@X%Q,target)
    anti=np.asarray(rhs['Frobenius_antisymmetric_part_mod47cubed'],dtype=np.int64)
    realN=(X[orbit]+anti)%Q
    adj=np.asarray(g['adjacency']['3'],dtype=np.int64)
    fullAX=sum((realN[adj[:,k]] for k in range(4)),np.zeros_like(realN))%Q
    assert np.array_equal((fullAX-mm(realN,H,Q))%Q,np.asarray(rhs['rhs_real_mod47cubed'],dtype=np.int64))
    assert np.array_equal((realN-realN[tau])%Q,2*anti%Q)
    records=[]
    for d in rhs['rational_SS_center_maps']:
        i=d['vertex_0based'];assert tau[i]==i
        tiny=np.asarray(d['tiny_mu_from_graph_center_mod47four'],dtype=np.int64)%Q
        val=(realN[i]+20*tiny[:,0])%Q
        records.append(dict(d,U_mu_rational_coordinates_mod47cubed=val.astype(int).tolist()))
    assert len(records)==110
    base=next(x for x in records if x['disk_id']=='SS_j0_10')
    Ubase=np.asarray(base['U_mu_rational_coordinates_mod47cubed'],dtype=np.int64)
    Fbase=np.asarray(base['moving_F_rational_center_mod47four'],dtype=np.int64)%Q
    Ci=np.asarray(rhs['rational_to_original_change'],dtype=np.int64)%Q
    for rec in records:
        mc=(np.asarray(rec['U_mu_rational_coordinates_mod47cubed'],dtype=np.int64)-Ubase)*pow(20,-1,Q)%Q
        mu=np.stack((mc,np.zeros(54,dtype=np.int64)),axis=1)[None,:,:]
        F=np.asarray(rec['moving_F_rational_center_mod47four'],dtype=np.int64)%Q
        original=r2mm((mu-F[None,:,:]+Fbase[None,:,:])%Q,Ci,Q)[0]
        # (mu integral - FC(P)+FC(b))*C^-1 returns the original nu basis.
        rec['C_mu_rational_coordinates_mod47cubed']=mc.astype(int).tolist()
        rec['C_original_nu_coordinates_mod47cubed']=original.astype(int).tolist()
    assert not np.any(np.asarray(base['C_original_nu_coordinates_mod47cubed']))
    out={'result':'R247','level':41,'auxiliary_prime':47,'precision':3,'modulus':Q,
         'all110_rational_SS_second_kind_center_integrals_complete':True,
         'all3154_real_parts_of_moved_integrals_complete':True,
         'all3154_full_complex_second_kind_integrals_complete':False,
         'complete_local_QC_heights':False,'complete_common_roots':False,
         'base_disk_id':base['disk_id'],'rational_SS_center_integrals':records,
         'geometric_real_U_mu_integrals_mod47cubed':realN.astype(int).tolist(),
         'actual_T3_and_Frobenius_equations_verified':True,'actual_B_gradient_used_as_anchor':True,
         'Frobenius_orbits':N,'rank_P_A3_even_mod47':N-1,
         'B_kernel_mass_mod47':bmass,'inverse_manifest_sha256':sha(metadata),
         'input_sha256':{p.name:sha(p) for p in [args.graph,args.rhs,args.kernel]},
         'source_sha256':sha(__file__)}
    digest=save(args.output,out)
    print('PASS all110 rational SS actual second-kind center integrals',digest,flush=True)

if __name__=='__main__':main()
