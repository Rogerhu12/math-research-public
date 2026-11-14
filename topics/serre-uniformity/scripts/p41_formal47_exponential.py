#!/usr/bin/env python3
"""Actual integral inverse Abel charts and formal exponentials on the41 model."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path


def select_families(r,W,K,tau):
    canonical=r.mm(W,K);families=[];used=set()
    for _ in range(2):
        chosen=[]
        for i,j in enumerate(tau):
            if j<=i or i in used or j in used:continue
            candidate=chosen+[i,j]
            if len(r.rank_pivots(r.rows(canonical,candidate))[0])==len(candidate):chosen=candidate
            if len(chosen)==54:break
        assert len(chosen)==54 and sorted(tau[i] for i in chosen)==sorted(chosen)
        r.inverse_matrix(r.rows(canonical,chosen));families.append(chosen);used.update(chosen)
    return families


def build_base(points,M,derivative,r,rng):
    import numpy as np
    restriction=r.rows(M['W'],points);rr,cc=r.rank_pivots(restriction);assert len(rr)==54
    K,free,block=r.kernel_from_rows(r.rows(restriction,rr),rr,cc)
    assert K[0].shape==(73,19) and r.iszero(r.mm(restriction,K))
    A=r.rows(r.mm(M['A1'],r.conjugate(K)),free)
    assert r.equal(r.mm(K,A),r.mm(M['A1'],r.conjugate(K)))
    assert r.equal(r.mm(A,r.conjugate(A)),r.eye(19))
    space=r.mm(M['W'],K);dspace=r.mm(derivative,K);remaining=[j for j in range(820) if j not in set(points)]
    def section():
        for _ in range(1000):
            seed,coef=r.rational_trace(A,rng);v=r.mm(space,coef)
            if not np.all(r.units(r.rows(v,remaining))):continue
            dv=r.mm(r.rows(dspace,points),coef)
            if not np.all(r.units(dv)):continue
            assert r.iszero(r.rows(v,points))
            return v,r.mm(K,coef),seed,coef
        raise RuntimeError('No simple actual rational section')
    v,vc,vs,vscoef=section()
    small,piv,cols,C=r.normalize(r.rows(M['V2'],remaining),199);assert cols==list(range(199))
    for attempt in range(100):
        g,gc,gs,gscoef=section();ratio=r.mul(r.rows(g,remaining),r.inverse_values(r.rows(v,remaining)))
        scaled=r.mul(ratio,small);R=r.sub(scaled,r.mm(small,r.rows(scaled,piv)))
        kr,kc=r.rank_pivots(R)
        if len(kr)!=72:continue
        aux,afree,ablock=r.kernel_from_rows(r.rows(R,kr),kr,kc);assert r.iszero(r.mm(R,aux))
        aux=r.mm(C,aux);aux,apiv,acols,ainv=r.normalize(aux,127);assert acols==list(range(127))
        AA=r.rows(r.mm(M['A2'],r.conjugate(aux)),apiv)
        assert r.equal(r.mm(aux,AA),r.mm(M['A2'],r.conjugate(aux)))
        assert r.equal(r.mm(AA,r.conjugate(AA)),r.eye(127))
        S=r.mm(M['V2'],aux);atZ=r.rows(S,points);zr,zc=r.rank_pivots(atZ);assert len(zr)==54
        zero,_,_=r.kernel_from_rows(r.rows(atZ,zr),zr,zc);zero=r.mm(aux,zero);Z=r.mm(M['V2'],zero)
        vW=r.mul(v,M['W']);norm,zp,_,_=r.normalize(vW,73)
        assert r.equal(r.mm(Z,r.inverse_matrix(r.rows(Z,zp))),norm)
        afree=[i for i in range(199) if i not in set(apiv)]
        record={'points_1based':[i+1 for i in points],
                'vanishing_space_rank_columns_1based':[i+1 for i in cc],
                'vanishing_space_free_columns_1based':[i+1 for i in free],
                'vanishing_space_kernel_block':r.to_json(block),
                'v_seed':r.to_json(vs),'v_small_coefficients':r.to_json(vscoef),'v_coefficients':r.to_json(vc),
                'g_seed':r.to_json(gs),'g_small_coefficients':r.to_json(gscoef),'g_coefficients':r.to_json(gc),
                'residual_rank_rows_1based':[i+1 for i in kr],'residual_rank_columns_1based':[i+1 for i in kc],
                'residual_coordinate_pivot_rows_1based':[i+1 for i in apiv],
                'residual_coordinate_free_rows_1based':[i+1 for i in afree],
                'residual_coordinate_block':r.to_json(r.rows(aux,afree))}
        return aux,v,record
    raise RuntimeError('No72-degree residual ideal')


def base_from_record(record,r):
    K=r.zeros(199,127);pivot=[i-1 for i in record['residual_coordinate_pivot_rows_1based']];free=[i-1 for i in record['residual_coordinate_free_rows_1based']]
    block=r.from_json(record['residual_coordinate_block'])
    for k in range(2):K[k][pivot]=r.eye(127)[k];K[k][free]=block[k]
    return K


def construct_point(target,record,jets,divs,M,r,kernel):
    import numpy as np
    points=[i-1 for i in record['points_1based']];allpoints=[i-1 for i in jets['point_indices_1based']]
    positions=[allpoints.index(i) for i in points]
    K1=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    Ws=[r.rows(r.from_json(a),positions) for a in jets['evaluation_coefficients']]
    beta=[-3*pow(27652,-1,r.Q)%r.Q]
    for k in (1,2):beta.append(-(1728*beta[k-1]+(27*beta[k-2] if k>=2 else 0))*pow(27652,-1,r.Q)%r.Q)
    Omega=[]
    for n in range(3):
        val=r.zeros(54,54)
        for j in range(n+1):val=r.add(val,tuple(a*beta[j]%r.Q for a in r.mm(Ws[n-j],K1)))
        Omega.append(val)
    r.inverse_matrix(Omega[0]);t=r.zeros(1,54)
    def as_column(t):return t[0].T,t[1].T
    def evaluate(t):
        col=as_column(t);power=r.eye(54)[0][:,0:1]*0+1,np.zeros((54,1),dtype=np.int64)
        total=r.zeros(54,54)
        for n in range(3):
            power=r.mul(power,col);total=r.add(total,tuple(a*pow(n+1,-1,r.Q)%r.Q for a in r.mul(power,Omega[n])))
        return tuple(a.sum(axis=0,keepdims=True)%r.Q for a in total)
    for step in range(3):
        error=r.sub(target,evaluate(t))
        if r.iszero(error):break
        col=as_column(t);J=r.add(Omega[0],r.add(r.mul(col,Omega[1]),r.mul(r.mul(col,col),Omega[2])))
        t=r.add(t,r.mm(error,r.inverse_matrix(J)))
    assert r.equal(evaluate(t),target) and all(np.all(a%47==0) for a in t)
    tau=M['tau'];perm=[points.index(tau[i]) for i in points]
    assert r.equal(r.cols(t,perm),r.conjugate(t))
    moving=r.zeros(54,73);power=(np.ones((54,1),dtype=np.int64),np.zeros((54,1),dtype=np.int64));col=as_column(t)
    for n in range(4):moving=r.add(moving,r.mul(power,Ws[n]));power=r.mul(power,col)
    pairs=[(i-1,j-1) for i,j in divs['square_basis_monomials_1based']]
    values=r.mul(r.cols(moving,[i for i,j in pairs]),r.cols(moving,[j for i,j in pairs]))
    values=r.mm(values,r.from_json(divs['square_basis_inverse']))
    aux=base_from_record(record,r);restriction=r.mm(values,aux);rr,cc=r.rank_pivots(restriction);assert len(rr)==54
    point,free,block=r.kernel_from_rows(r.rows(restriction,rr),rr,cc);assert r.iszero(r.mm(restriction,point))
    point=r.mm(aux,point);point,piv,cols,_=r.normalize(point,73);assert cols==list(range(73))
    A=r.rows(r.mm(M['A2'],r.conjugate(point)),piv)
    assert r.equal(r.mm(point,A),r.mm(M['A2'],r.conjugate(point)))
    assert r.equal(r.mm(A,r.conjugate(A)),r.eye(73))
    return point,A,{'parameters':r.to_json(t),'target_logarithm':r.to_json(target),
                   'point_coordinates':r.to_json(point),'point_frobenius':r.to_json(A),
                   'restriction_rank_columns_1based':[i+1 for i in cc],
                   'restriction_free_columns_1based':[i+1 for i in free],
                   'restriction_kernel_block':r.to_json(block)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--bases',type=Path,default=Path('/tmp/p41_formal47_abel_bases_checkpoint.json.gz'))
    parser.add_argument('--jets',type=Path,default=Path('/tmp/p41_formal47_abel_jets_checkpoint.json.gz'))
    parser.add_argument('--bases-only',action='store_true')
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_formal47_exponential_checkpoint.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_cm4_divisor47 import kernel
    from p41_group_operations47 import load_sources,make_model
    from p41_formal47_multiply import write_checkpoint
    from p41_poincare_norms47 import quotient,determinant
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    jr=(folder/'data/p41_evaluation_jets47_checkpoint.json.gz').read_bytes();derivative=r.from_json(json.loads(gzip.decompress(jr))['evaluation_derivatives'])
    divs=sources[1];K=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    if args.bases.exists():
        base=json.loads(gzip.decompress(args.bases.read_bytes()));assert base['source_sha256']==hashes
    else:
        families=select_families(r,M['W'],K,M['tau']);rng=random.Random(4104713401);records=[];vs=[]
        for j,points in enumerate(families):
            for attempt in range(100):
                aux,v,record=build_base(points,M,derivative,r,rng)
                if j==1:
                    k2=r.rows(r.mul(vs[0],M['W']),M['P2']);k3=r.rows(r.mul(vs[0],M['V2']),M['P3'])
                    Q2,rec2=quotient(k2);Q3,rec3=quotient(k3)
                    c=r.rows(r.mul(v,M['V2']),M['P3']);mu=r.cols(r.mm(Q3,c),[i-1 for i in rec2['free_rows_1based']])
                    det=determinant(mu)
                    if det is None:continue
                    record['disjointness_determinant']=det
                vs.append(v);records.append(record);break
            else:raise RuntimeError('Could not choose disjoint actual bases')
            print('Actual rational residual base',j+1,'degree72 and nonspecial54-point divisor PASS.',flush=True)
        base={'level':41,'auxiliary_prime':47,'precision':4,'modulus':r.Q,'source_sha256':hashes,
              'first_jets_sha256':hashlib.sha256(jr).hexdigest(),'families':records,
              'status':'two actual Q47 nonspecial Abel charts with disjoint126-degree base divisors'}
        digest,size=write_checkpoint(args.bases,base);print('Base data',size,digest,flush=True)
    if args.bases_only:return
    jetraw=args.jets.read_bytes();jets=json.loads(gzip.decompress(jetraw))
    lr=(folder/'data/p41_formal47_log_compact.json.gz').read_bytes();log=json.loads(gzip.decompress(lr));target=r.from_json(log['log_of_signed_multiple'])
    results=[]
    for j,record in enumerate(base['families']):
        point,A,witness=construct_point(target,record,jets,divs,M,r,kernel);results.append(witness)
        print('Actual exponential family',j+1,'complete73-dimensional divisor ideal PASS.',flush=True)
    out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
         'bases_sha256':hashlib.sha256(args.bases.read_bytes()).hexdigest(),'jets_sha256':hashlib.sha256(jetraw).hexdigest(),
         'log_sha256':hashlib.sha256(lr).hexdigest(),'exponentials':results,
         'status':'actual ideal reconstruction from the54 normalized differential logarithms; class comparison follows'}
    digest,size=write_checkpoint(args.output,out);print('Actual exponential data',size,digest,flush=True)


if __name__=='__main__':main()
