#!/usr/bin/env python3
"""Actual canonical-restriction residue-disc jets from the unit Jacobian of global L-quadrics."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--order',type=int,default=16)
    p.add_argument('--labels',nargs='*')
    p.add_argument('--points',type=Path,default=Path('/tmp/p41_canonical_low_points47_certificate.json.gz'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_canonical_low_jets47_raw.json.gz'))
    p.add_argument('--compact-output',type=Path,default=Path('/tmp/p41_canonical_low_jets47_compact.json.gz'))
    args=p.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_cm4_divisor47 import kernel
    from p41_poincare_norms47 import determinant
    from p41_formal47_multiply import write_checkpoint
    sources,hashes=load_sources(args.script_dir/'data');M=make_model(sources);d=sources[1]
    paths=[args.points];inputs=[read(args.points)];point_data=inputs[0][0]
    assert point_data['source_sha256']==hashes
    entries=[(p['label'],[r.from_json([p['normalized_weight2_values']])]) for p in point_data['records']]
    K=r.from_json(kernel(73,d['cusp_rank_columns_1based'],d['cusp_free_columns_1based'],d['canonical_kernel_block']))
    fc=r.mm(K,r.column(d['canonical_coefficients']))
    sq=[(a-1,b-1) for a,b in d['square_basis_monomials_1based']];S=r.from_json(d['square_basis_inverse'])
    pairs=[(i,j) for i in range(73) for j in range(i,73)];aa=[a for a,b in pairs];bb=[b for a,b in pairs]
    wp=r.rows(M['W'],M['P2']);C=r.mul(r.cols(wp,aa),r.cols(wp,bb));H=r.mm(S,C)
    for start in range(0,len(pairs),128):
        js=list(range(start,min(start+128,len(pairs))))
        actual=r.mul(r.cols(M['W'],[aa[j] for j in js]),r.cols(M['W'],[bb[j] for j in js]))
        assert r.equal(actual,r.mm(M['V2'],r.cols(C,js)))
    transpose=lambda x:(x[0].T.copy(),x[1].T.copy())
    def normalized(source):
        f=[r.mm(w,fc) for w in source];inv=[r.inverse_values(f[0])]
        for k in range(1,len(source)):
            total=r.zeros(1,1)
            for j in range(1,k+1):total=r.add(total,r.mul(f[j],inv[k-j]))
            inv.append(r.neg(r.mul(inv[0],total)))
        out=[]
        for k in range(len(source)):
            total=r.zeros(1,73)
            for j in range(k+1):total=r.add(total,r.mul(source[j],inv[k-j]))
            out.append(transpose(total))
        return out
    def monomial_bilinear(x,y,pp):
        return transpose(r.mul(r.rows(x,[a for a,b in pp]),r.rows(y,[b for a,b in pp])))
    rng=random.Random(4104716011);records=[]
    for label,original in entries:
        if args.labels and label not in args.labels:continue
        normalized_known=normalized(original);x0=normalized_known[0]
        assert r.equal(r.mm(transpose(fc),x0),r.eye(1))
        assert r.iszero(r.sub(monomial_bilinear(x0,x0,pairs),r.mm(monomial_bilinear(x0,x0,sq),H)))
        grad=r.zeros(73,len(pairs));gs=r.zeros(73,199)
        for k,(a,b1) in enumerate(pairs):
            for z in range(2):
                grad[z][a,k]=(grad[z][a,k]+x0[z][b1,0])%r.Q
                grad[z][b1,k]=(grad[z][b1,k]+x0[z][a,0])%r.Q
        for k,(a,b1) in enumerate(sq):
            for z in range(2):
                gs[z][a,k]=(gs[z][a,k]+x0[z][b1,0])%r.Q
                gs[z][b1,k]=(gs[z][b1,k]+x0[z][a,0])%r.Q
        grad=r.sub(grad,r.mm(gs,H));rr,cc=r.rank_pivots(transpose(grad));assert len(rr)==71
        jac=transpose(r.cols(grad,rr));Hs=r.cols(H,rr);ps=[pairs[j] for j in rr]
        for attempt in range(1,101):
            seed,uc=r.rational_trace(M['A1'],rng)
            J=(np.vstack([jac[0],fc[0].T,uc[0].T]),np.vstack([jac[1],fc[1].T,uc[1].T]))
            if len(r.rank_pivots(J)[0])==73:break
        else:raise RuntimeError('No actual local parameter')
        Ji=r.inverse_matrix(J);assert r.equal(r.mm(J,Ji),r.eye(73))
        jets=[x0]
        for k in range(1,args.order+1):
            nonlinear=r.zeros(1,71)
            for j in range(1,k):
                term=r.sub(monomial_bilinear(jets[j],jets[k-j],ps),
                           r.mm(monomial_bilinear(jets[j],jets[k-j],sq),Hs))
                nonlinear=r.add(nonlinear,term)
            rhs=r.zeros(73,1)
            for z in range(2):rhs[z][:71,0]=-nonlinear[z][0]%r.Q
            rhs[0][72,0]=int(k==1)
            jets.append(r.mm(Ji,rhs))
        for k in range(args.order+1):
            allpairs=r.zeros(1,len(pairs));selected=r.zeros(1,199)
            for j in range(k+1):
                allpairs=r.add(allpairs,monomial_bilinear(jets[j],jets[k-j],pairs))
                selected=r.add(selected,monomial_bilinear(jets[j],jets[k-j],sq))
            assert r.equal(allpairs,r.mm(selected,H)),'Some actual global quadric fails at the computed jet'
            fvalue=r.mm(transpose(fc),jets[k]);uvalue=r.mm(transpose(uc),jets[k])
            if k:
                assert r.iszero(fvalue)
                target=r.zeros(1,1);target[0][0,0]=int(k==1)
                assert r.equal(uvalue,target)
        # Independently generated modular-form jets must be the same formal branch.
        anchor_orders=len(normalized_known)-1
        if anchor_orders:
            tj=[r.zeros(1,1)]+[r.mm(transpose(uc),v) for v in normalized_known[1:]]
            assert r.units(tj[1])[0,0]
            powers=[[r.eye(1)]+[r.zeros(1,1) for _ in range(anchor_orders)]]
            for k in range(1,anchor_orders+1):
                power=[]
                for n in range(anchor_orders+1):
                    total=r.zeros(1,1)
                    for j in range(n+1):total=r.add(total,r.mul(powers[-1][j],tj[n-j]))
                    power.append(total)
                powers.append(power)
            for n in range(anchor_orders+1):
                composed=r.zeros(73,1)
                for k in range(n+1):composed=r.add(composed,r.mul(jets[k],powers[k][n]))
                assert r.equal(composed,normalized_known[n]),'Independent actual modular jets do not match'
        encoded=[r.to_json(transpose(v))[0] for v in jets]
        record={'label':label,'order':args.order,'selected_quadric_pairs_1based':[[a+1,b+1] for a,b in ps],
                'parameter_seed':r.to_json(seed),'parameter_coefficients':r.to_json(uc),
                'parameter_attempt':attempt,'unit_jacobian_determinant':determinant(J),
                'independent_modular_anchor_orders':anchor_orders,
                'normalized_weight2_coefficients':encoded,
                'jets_sha256':hashlib.sha256(json.dumps(encoded,separators=(',',':')).encode()).hexdigest()}
        records.append(record)
        print('ACTUAL CANONICAL FORMAL DISC',label,'rank71, order',args.order,'all2701 quadrics PASS; modular anchor',anchor_orders,flush=True)
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
            'point_source_sha256':{p.name:h for p,(d,h) in zip(paths,inputs)},
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'line_bundle_degree':126,'global_quadrics_count':len(pairs),'order':args.order,
            'records':records,'normalization':'W/f0; t=u/f0 minus its value at the actual canonical point',
            'status':'actual integral residue-disc jets by unit Jacobian; all global quadrics and available independently generated modular anchors verified; no height claimed'}
    sha,size=write_checkpoint(args.output,result)
    compact={k:v for k,v in result.items() if k!='records'}
    compact['records']=[{k:v for k,v in rec.items() if k!='normalized_weight2_coefficients'} for rec in records]
    compact['raw_rebuild_sha256']=sha
    sha2,size2=write_checkpoint(args.compact_output,compact)
    print('CANONICAL FORMAL DISCS COMPLETE raw',size,sha,'compact',size2,sha2,flush=True)

if __name__=='__main__':main()
