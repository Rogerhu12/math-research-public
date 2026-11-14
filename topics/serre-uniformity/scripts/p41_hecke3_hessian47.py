#!/usr/bin/env python3
"""Actual principal-part construction of the canonical T3 biextension Hessian.

Every first-order transport function is a quotient of actual V3 sections.
The auxiliary Norm line bundle is never identified with L^4.
"""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def section_jets(Ws,sources,M,r):
    """The fixed actual V2,V3 bases at arbitrary actual point jets."""
    from p41_cm4_divisor47 import kernel
    divs=sources[1];ck=sources[3];order=len(Ws);n=Ws[0][0].shape[0]
    K=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    fc=r.mm(K,r.column(divs['canonical_coefficients']));fs=[r.mm(W,fc) for W in Ws]
    sq=[(a-1,b-1) for a,b in divs['square_basis_monomials_1based']];C2=r.from_json(divs['square_basis_inverse'])
    V2=[]
    for k in range(order):
        raw=r.zeros(n,199)
        for j in range(k+1):raw=r.add(raw,r.mul(r.cols(Ws[j],[a for a,b in sq]),r.cols(Ws[k-j],[b for a,b in sq])))
        V2.append(r.mm(raw,C2))
    pairs=[(a-1,b-1) for a,b in ck['cubic_selected_pairs_1based']];aa=[a for a,b in pairs];bb=[b for a,b in pairs]
    fbase=r.mm(M['W'],fc);oldrows=[M['P2'][b] for b in bb]
    numerator=M['W'][0][oldrows,aa][None,:],M['W'][1][oldrows,aa][None,:]
    coefficient=r.mul(numerator,r.inverse_values((fbase[0][oldrows].T,fbase[1][oldrows].T)))
    extra=r.from_json(ck['cubic_extra_inverse']);newrows=[i-1 for i in ck['cubic_extra_rows_1based']]
    invf=r.inverse_values((fbase[0][M['P2']].T,fbase[1][M['P2']].T))
    C=r.rows(r.mul(r.mul(fbase,M['V2']),invf),newrows)
    V3=[]
    for k in range(order):
        residual=r.zeros(n,126);v3a=r.zeros(n,199)
        for j in range(k+1):
            residual=r.add(residual,r.mul(r.cols(V2[j],bb),r.sub(r.cols(Ws[k-j],aa),r.mul(fs[k-j],coefficient))))
            v3a=r.add(v3a,r.mul(fs[j],V2[k-j]))
        added=r.mm(residual,extra);v3a=r.mul(v3a,invf)
        V3.append(r.hcat(r.sub(v3a,r.mm(added,C)),added))
    return V2,V3

def projective_rows(W,r):
    import numpy as np
    out=[]
    for a,b in zip(W[0]%47,W[1]%47):
        choices=np.flatnonzero((a*a+b*b)%47)
        if not len(choices):out.append(None);continue
        j=int(choices[0]);norm=pow(int((a[j]*a[j]+b[j]*b[j])%47),-1,47)
        ir,ii=int(a[j])*norm%47,-int(b[j])*norm%47
        out.append(tuple((a*ir-b*ii)%47)+tuple((a*ii+b*ir)%47))
    return out

def select_charts(M,targets,K,r):
    source=projective_rows(M['W'],r);images=[projective_rows(W,r) for W in targets]
    source_set=set(source);canonical=r.mm(M['W'],K);used=set();usedimages=set();families=[]
    for family in range(2):
        selected=[]
        for i,j in enumerate(M['tau']):
            if j<=i or i in used or j in used:continue
            new=[im[k] for im in images for k in (i,j)]
            if None in new or len(set(new))!=8 or set(new)&usedimages or set(new)&source_set:continue
            candidate=selected+[i,j]
            if len(r.rank_pivots(r.rows(canonical,candidate))[0])!=len(candidate):continue
            selected=candidate;used.update((i,j));usedimages.update(new)
            if len(selected)==54:break
        assert len(selected)==54
        families.append(selected)
    assert len(usedimages)==432 and len(used)==108
    return families

def solve_transport(points,W,V3,dV3,targetV3,targetdV3,other,M,K,T,r,rng):
    """Solve all54 actual first-order principal functions simultaneously."""
    import numpy as np
    from p41_poincare_norms47 import determinant
    EV=r.hcat(*[r.eye(1)]) if False else (np.concatenate([r.rows(V3,points)[0]]+[r.rows(A,points)[0] for A in targetV3]),
                                       np.concatenate([r.rows(V3,points)[1]]+[r.rows(A,points)[1] for A in targetV3]))
    dEV=(np.concatenate([r.rows(dV3,points)[0]]+[r.rows(A,points)[0] for A in targetdV3]),
         np.concatenate([r.rows(dV3,points)[1]]+[r.rows(A,points)[1] for A in targetdV3]))
    rr,cc=r.rank_pivots(EV);assert len(rr)==270
    B,free,block=r.kernel_from_rows(r.rows(EV,rr),rr,cc);assert B[0].shape==(325,55) and r.iszero(r.mm(EV,B))
    AB=r.rows(r.mm(M['A3'],r.conjugate(B)),free)
    assert r.equal(r.mm(B,AB),r.mm(M['A3'],r.conjugate(B))) and r.equal(r.mm(AB,r.conjugate(AB)),r.eye(55))
    space=r.mm(V3,B);dspace=r.mm(dEV,B);remaining=[i for i in range(820) if i not in set(points)]
    for attempt in range(1000):
        seed,bc=r.rational_trace(AB,rng);bv=r.mm(space,bc);bd=r.mm(dspace,bc)
        if np.all(r.units(r.rows(bv,remaining))) and np.all(r.units(bd)):break
    else:raise RuntimeError('No simple denominator avoiding remaining766 points')
    b=r.mm(B,bc)
    Vsmall,piv,columns,C=r.normalize(r.rows(V3,remaining),325);assert columns==list(range(325))
    for attempt in range(100):
        gs,gc=r.rational_trace(AB,rng);gv=r.mm(space,gc)
        ratio=r.mul(r.rows(gv,remaining),r.inverse_values(r.rows(bv,remaining)))
        scaled=r.mul(ratio,Vsmall);residual=r.sub(scaled,r.mm(Vsmall,r.rows(scaled,piv)))
        cr,ccol=r.rank_pivots(residual)
        if len(cr)!=108:continue
        aux,afree,ablock=r.kernel_from_rows(r.rows(residual,cr),cr,ccol)
        assert r.iszero(r.mm(residual,aux));aux=r.mm(C,aux)
        break
    else:raise RuntimeError('No complete108-degree residual pole divisor')
    restrictions=r.mm(EV,aux);ar,ac=r.rank_pivots(restrictions);assert len(ar)==216
    Omega=tuple(x*(-3*pow(27652,-1,r.Q)%r.Q)%r.Q for x in r.mm(r.rows(W,points),K))
    Oinv=r.inverse_matrix(Omega);TP=r.mm(r.mm(Omega,T),Oinv)
    # Parameter t is a row.  Target first-order parameter is t*TP.
    rhs=r.zeros(270,54);sourcepart=r.mul(r.rows(bd,list(range(54))),(TP[0].T,TP[1].T))
    for k in range(2):rhs[k][:54]=sourcepart[k]
    for branch in range(4):
        deriv=r.rows(bd,list(range(54*(branch+1),54*(branch+2))))
        for k in range(2):rhs[k][54*(branch+1):54*(branch+2)]=(-np.eye(54,dtype=np.int64)*deriv[k])%r.Q
    coeff=r.zeros(217,54)
    solved=r.mm(r.inverse_matrix(r.cols(r.rows(restrictions,ar),ac)),r.rows(rhs,ar))
    for k in range(2):coeff[k][ac]=solved[k]
    assert r.equal(r.mm(restrictions,coeff),rhs),'Actual Hecke principal parts fail the54 residue/cohomology conditions'
    numer=r.mm(aux,coeff)
    normal=next(i for i in remaining if M['tau'][i]==i)
    constant=r.mul(r.mm(r.rows(V3,[normal]),numer),r.inverse_values(r.rows(bv,[normal])))
    numer=r.sub(numer,r.mul(b,constant))
    assert r.iszero(r.mm(r.rows(V3,[normal]),numer))
    assert r.equal(r.mm(EV,numer),rhs)
    perm=[points.index(M['tau'][i]) for i in points]
    assert r.equal(r.mm(M['A3'],r.conjugate(b)),b)
    assert r.equal(r.mm(M['A3'],r.conjugate(numer)),r.cols(numer,perm))
    z0,z1=r.rows(V3,other),r.rows(dV3,other)
    av,ad=r.mm(z0,numer),r.mm(z1,numer);b0,b1=r.mm(z0,b),r.mm(z1,b)
    derivative=r.mul(r.sub(r.mul(ad,b0),r.mul(av,b1)),r.inverse_values(r.mul(b0,b0)))
    print('Actual270 principal parts,217-dimensional pole space and54 full cohomology identities PASS.',flush=True)
    record={'points_1based':[i+1 for i in points],
            'abel_tangent_determinant':determinant(Omega),'abel_tangent_matrix':r.to_json(Omega),
            'T3_parameter_matrix':r.to_json(TP),'pole_evaluation_rank_columns_1based':[i+1 for i in cc],
            'pole_evaluation_kernel_block':r.to_json(block),'denominator_seed':r.to_json(seed),
            'denominator_small_coefficients':r.to_json(bc),'denominator_coefficients':r.to_json(b),
            'auxiliary_seed':r.to_json(gs),'auxiliary_small_coefficients':r.to_json(gc),
            'residual_rank_rows_1based':[i+1 for i in cr],'residual_rank_columns_1based':[i+1 for i in ccol],
            'residual_kernel_block':r.to_json(ablock),'restricted_V3_pivot_rows_1based':[i+1 for i in piv],
            'restricted_V3_basis_inverse':r.to_json(C),'principal_part_rank_rows_1based':[i+1 for i in ar],
            'principal_part_rank_columns_1based':[i+1 for i in ac],
            'normalization_point_1based':normal+1,'numerator_coefficients':r.to_json(numer),
            'derivatives_at_other_chart':r.to_json(derivative)}
    return record,derivative,Omega

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--hecke',type=Path,default=Path('/tmp/p41_hecke47_checkpoint.json.gz'))
    parser.add_argument('--jets',type=Path,default=Path('/tmp/p41_hecke3_jets47_checkpoint.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_hecke3_hessian47_checkpoint.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_cm4_divisor47 import kernel
    from p41_formal47_multiply import write_checkpoint
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    hr=args.hecke.read_bytes();jr=args.jets.read_bytes();h=json.loads(gzip.decompress(hr));j=json.loads(gzip.decompress(jr))
    assert j['raw_hecke_sha256']==hashlib.sha256(hr).hexdigest() and len(j['targets'])==4
    op=h['operators']['3'];permutation=[i-1 for i in op['necklace_transport_1based']]
    targets=[r.rows(r.from_json(a['evaluation_matrix']),permutation) for a in op['targets']]
    dtargets=[r.rows(r.from_json(a['evaluation_derivatives']),permutation) for a in j['targets']]
    raw=(folder/'data/p41_evaluation_jets47_checkpoint.json.gz').read_bytes();dw=r.from_json(json.loads(gzip.decompress(raw))['evaluation_derivatives'])
    V2s,V3s=section_jets([M['W'],dw],sources,M,r)
    assert r.equal(V2s[0],M['V2']) and r.equal(V3s[0],M['V3'])
    alltargets=[section_jets([a,b],sources,M,r)[1] for a,b in zip(targets,dtargets)]
    targetV3=[a[0] for a in alltargets];targetdV3=[a[1] for a in alltargets]
    divs=sources[1];K=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    families=select_charts(M,targets,K,r);T=r.from_json(op['canonical_operator']);rng=random.Random(4104714101)
    records=[];derivatives=[];Omegas=[]
    for i,points in enumerate(families):
        rec,der,Omega=solve_transport(points,M['W'],V3s[0],V3s[1],targetV3,targetdV3,families[1-i],M,K,T,r,rng)
        records.append(rec);derivatives.append(der);Omegas.append(Omega)
        write_checkpoint(args.output,{'source_sha256':hashes,'families':records,'status':'actual canonical T3 transport Hessian in progress'})
        print('Actual canonical transport functions chart',i+1,'complete.',flush=True)
    Cparam=r.sub(derivatives[1],(derivatives[0][0].T,derivatives[0][1].T))
    O1=r.inverse_matrix(Omegas[0]);O2=r.inverse_matrix(Omegas[1])
    C=r.mm(r.mm(O1,Cparam),(O2[0].T,O2[1].T));D=r.neg(C)
    AK=r.from_json(divs['canonical_frobenius_matrix'])
    assert r.equal(r.mm(r.mm(AK,r.conjugate(C)),(AK[0].T,AK[1].T)),C)
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
            'raw_hecke_sha256':hashlib.sha256(hr).hexdigest(),'hecke_jets_sha256':hashlib.sha256(jr).hexdigest(),
            'first_jets_sha256':hashlib.sha256(raw).hexdigest(),'families':records,
            'canonical_scalar_mixed_hessian':r.to_json(C),'T3_defect_matrix':r.to_json(D),
            'status':'actual T3 canonical norm/projection transport mixed Hessian; independent verification and Hecke correction follow'}
    digest,size=write_checkpoint(args.output,result);print('Actual canonical T3 mixed Hessian',size,digest,flush=True)

if __name__=='__main__':main()
