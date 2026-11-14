#!/usr/bin/env python3
"""Actual T2 transport for one CM class in the disjoint second Abel chart.

The source and three target branches are published R170 data. The selected
54-point certificate, true divisor ideals and325-coefficient sections retain
the new frame. All inversions use unit minors; no division at a zero evaluation
row is used in the principal-function construction.
"""
import argparse,gc,gzip,hashlib,json,random,sys
from pathlib import Path


def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--selection',type=Path,default=Path('/tmp/p41_t2_cm_abel_select47_checkpoint.json.gz'))
    ap.add_argument('--class-name',choices=['x12','x7'],required=True)
    ap.add_argument('--cm-endpoints',type=Path)
    ap.add_argument('--restricted',type=Path,default=Path('/tmp/p41_t2_cm_restricted_cubic47_checkpoint.json.gz'))
    ap.add_argument('--hecke',type=Path)
    ap.add_argument('--base',type=Path,default=Path('/tmp/p41_t2_cm_abel_base47_checkpoint.json.gz'))
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    assert args.restricted.exists()
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_cm4_divisor47 import kernel
    from p41_formal47_exponential import build_base,construct_point
    from p41_formal47_multiply import write_checkpoint,point_hash
    from verify_p41_hecke3_hessian47 import cubic_basis
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    sources[0]=None;sources[2]=None;gc.collect()
    selected,selection_sha=read(args.selection);jets,jsha=read(args.restricted)
    assert jets['selection_sha256']==selection_sha and selected['all_216_supports_distinct_mod47']
    assert not any(selected['disjoint_support_counts'].values())
    points=[j-1 for j in selected['points_1based']]
    assert jets['points_1based']==selected['points_1based']
    jr=(folder/'data/p41_evaluation_jets47_checkpoint.json.gz').read_bytes()
    derivative=r.from_json(json.loads(gzip.decompress(jr))['evaluation_derivatives'])
    rng=random.Random(4104717902)
    if args.base.exists():
        base,bsha=read(args.base)
        assert base['source_sha256']==hashes and base['selection_sha256']==selection_sha
        record=base['family']
    else:
        aux,v,record=build_base(points,M,derivative,r,rng)
        base={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
              'selection_sha256':selection_sha,'first_jets_sha256':hashlib.sha256(jr).hexdigest(),
              'family':record,'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'status':'actual degree72 residual base and54-point integral Abel chart with216 distinct T2/source supports'}
        bsha,bsize=write_checkpoint(args.base,base)
        print('Actual disjoint T2 Abel base',bsize,bsha,flush=True)
    del derivative,jr
    h,hsha=read(args.hecke or folder/'data/p41_hecke47_compact.json.gz')
    assert h['full_raw_sha256']==selected['raw_hecke_sha256']==jets['target_input_sha256']['p41_hecke47_checkpoint.json.gz']
    T=r.from_json(h['operators']['2']['canonical_operator'])
    del h
    lg,lsha=read(args.cm_endpoints or folder/'data/p41_cm_formal_endpoints47_checkpoint.json.gz')
    assert lg['source_sha256']==hashes
    x=r.from_json(lg['targets'][args.class_name]['targets']['m']['logarithm']);tx=r.mm(x,T)
    del lg;gc.collect()
    endpoints=[]
    for name,log in [('Y',x),('T2Y',tx)]:
        point,F,witness=construct_point(log,record,jets['source_jets'],sources[1],M,r,kernel)
        witness['point_sha256']=point_hash(point,F)
        endpoints.append(witness)
        print('Actual new-chart endpoint',name,witness['point_sha256'],flush=True)
    t,s=[r.from_json(w['parameters']) for w in endpoints]

    def evaluate(coefficients,parameter):
        column=parameter[0].T,parameter[1].T
        power=(np.ones((54,1),dtype=np.int64),np.zeros((54,1),dtype=np.int64))
        value=r.zeros(54,73)
        for matrix in coefficients:
            value=r.add(value,r.mul(power,r.from_json(matrix)))
            power=r.mul(power,column)
        return value

    V3,_,C3=cubic_basis(M['W'],r.zeros(820,73),sources,M,None,r)
    assert r.equal(V3,M['V3'])
    def cubic(W):
        return cubic_basis(W,r.zeros(W[0].shape[0],73),sources,M,C3,r)[0]
    def vcat(values):
        return tuple(np.concatenate([v[k] for v in values],axis=0) for k in range(2))

    src0=r.from_json(jets['source_jets']['evaluation_coefficients'][0])
    target0=[r.from_json(j['evaluation_coefficients'][0]) for j in jets['targets']]
    targett=[evaluate(j['evaluation_coefficients'],t) for j in jets['targets']]
    sources_=evaluate(jets['source_jets']['evaluation_coefficients'],s)
    Eplus=vcat([cubic(W) for W in targett]+[cubic(src0)])
    Eminus=vcat([cubic(W) for W in target0]+[cubic(sources_)])
    assert all(np.array_equal(a%47,b%47) for a,b in zip(Eplus,Eminus))
    ideals=[];records=[]
    for label,E in [('plus',Eplus),('minus',Eminus)]:
        rr,cc=r.rank_pivots(E);assert len(rr)==216
        I,free,block=r.kernel_from_rows(r.rows(E,rr),rr,cc)
        assert I[0].shape==(325,109) and r.iszero(r.mm(E,I))
        F=r.rows(r.mm(M['A3'],r.conjugate(I)),free)
        assert r.equal(r.mm(I,F),r.mm(M['A3'],r.conjugate(I)))
        assert r.equal(r.mm(F,r.conjugate(F)),r.eye(109))
        ideals.append((I,F))
        records.append({'label':label,'rank_rows_1based':[j+1 for j in rr],
                        'rank_columns_1based':[j+1 for j in cc],
                        'free_columns_1based':[j+1 for j in free],
                        'kernel_block':r.to_json(block),'frobenius':r.to_json(F)})
        print('Actual216-point divisor ideal',label,'rank109 and integral Frobenius PASS',flush=True)
    Ip,Fp=ideals[0];Im,Fm=ideals[1]
    VI=r.mm(V3,Ip)
    rng=random.Random(4104717903)
    for attempt in range(100):
        seed0,c0=r.rational_trace(Fm,rng);seedg,cg=r.rational_trace(Fm,rng)
        s0,g=r.mm(Im,c0),r.mm(Im,cg)
        sv,gv=r.mm(V3,s0),r.mm(V3,g)
        R=r.hcat(r.mul(gv,VI),r.neg(r.mul(sv,V3)))
        rr,cc=r.rank_pivots(R)
        if len(rr)!=433:continue
        solution,free,block=r.kernel_from_rows(r.rows(R,rr),rr,cc)
        assert solution[0].shape==(434,1) and r.iszero(r.mm(R,solution))
        numerator=r.mm(Ip,r.rows(solution,list(range(109))))
        u=r.rows(solution,list(range(109,434)))
        # Rationalize the one-dimensional solution, retaining the exact input
        # sections in the equation. A unit coordinate gives its scalar action.
        rational_image=r.mm(M['A3'],r.conjugate(numerator))
        piv=next((j for j in range(325) if bool(r.units(r.rows(numerator,[j]))[0,0])),None)
        assert piv is not None
        FA=r.mul(r.rows(rational_image,[piv]),r.inverse_values(r.rows(numerator,[piv])))
        assert r.equal(r.mul(numerator,FA),rational_image)
        assert r.equal(r.mul(FA,r.conjugate(FA)),r.eye(1))
        for _ in range(100):
            seedscalar,scalar=r.rational_trace(FA,rng)
            if bool(r.units(scalar)[0,0]):break
        else:raise RuntimeError('No rational unit in the actual kernel line')
        numerator=r.mul(numerator,scalar);u=r.mul(u,scalar)
        assert r.equal(r.mm(M['A3'],r.conjugate(numerator)),numerator)
        assert r.equal(r.mm(M['A3'],r.conjugate(u)),u)
        nv,uv=r.mm(V3,numerator),r.mm(V3,u)
        assert r.equal(r.mul(gv,nv),r.mul(sv,uv))
        good=[j for j in range(820) if bool(r.units(r.rows(sv,[j]))[0,0])]
        assert good
        normal=good[0]
        kv=r.mul(r.rows(nv,[normal]),r.inverse_values(r.rows(sv,[normal])))
        # The half-trace at a Frobenius pair is a rational unit, so this
        # normalization preserves Q47-rationality of the principal function.
        scale=pow(int(kv[0][0,0]),-1,r.Q)
        numerator=tuple(a*scale%r.Q for a in numerator)
        u=tuple(a*scale%r.Q for a in u)
        nv,uv=r.mm(V3,numerator),r.mm(V3,u)
        assert r.equal(r.mul(gv,nv),r.mul(sv,uv))
        assert r.iszero(r.mm(Eplus,numerator)) and r.iszero(r.mm(Eminus,s0))
        assert all(np.array_equal(a%47,b%47) for a,b in zip(numerator,s0))
        kval=r.mul(r.rows(nv,[normal]),r.inverse_values(r.rows(sv,[normal])))
        conjugate_value=r.mul(r.rows(nv,[M['tau'][normal]]),r.inverse_values(r.rows(sv,[M['tau'][normal]])))
        assert r.equal(conjugate_value,r.conjugate(kval)) and int(kval[0][0,0])==1
        transport={'denominator_coefficients':r.to_json(s0),'numerator_coefficients':r.to_json(numerator),
                   'auxiliary_coefficients':r.to_json(g),'auxiliary_quotient_coefficients':r.to_json(u),
                   'denominator_seed':r.to_json(seed0),'denominator_small_coefficients':r.to_json(c0),
                   'auxiliary_seed':r.to_json(seedg),'auxiliary_small_coefficients':r.to_json(cg),
                   'relation_rank_rows_1based':[j+1 for j in rr],
                   'relation_rank_columns_1based':[j+1 for j in cc],
                   'relation_free_columns_1based':[j+1 for j in free],
                   'relation_kernel_block':r.to_json(block),
                   'normalization_point_1based':normal+1,'normalization_value':r.to_json(kval),
                   'normalization':'Q47-rational half-trace at the specified Frobenius pair equals1',
                   'divisor':'T2(sum P_i(t)-sum P_i(0))-(sum P_i(s)-sum P_i(0))'}
        print('Actual T2 principal function: rank433 kernel, all820 product equations, rationality and216 zeros PASS',flush=True)
        break
    else:raise RuntimeError('No rank433 actual principal-function relation')
    out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
         'selection_sha256':selection_sha,'restricted_cubic_sha256':jsha,'new_base_sha256':bsha,
         'compact_hecke_sha256':hsha,'CM_formal_endpoints_sha256':lsha,'class_name':args.class_name,
         'raw_hecke_sha256':selected['raw_hecke_sha256'],
         'template_R170_source_sha256':'a3cc2242ca6bd5c141e1bf98bce23d5fbab9ecbb473564635b0065606fd48552',
         'points_1based':[j+1 for j in points],'endpoints':endpoints,
         'divisor_ideals':records,'transport':transport,
         'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'status':'true CM T2 Abel-divisor principal transport in second chart disjoint from first/T2first modulo47^4; no Poincare height asserted'}
    sha,size=write_checkpoint(args.output,out)
    print('ACTUAL T2 FORMAL TRANSPORT COMPLETE',size,sha,flush=True)


if __name__=='__main__':main()
