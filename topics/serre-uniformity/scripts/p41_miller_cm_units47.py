#!/usr/bin/env python3
"""Track exact finite valuations of saved Miller SLP factors on all required CM support."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def load(path):
    b=path.read_bytes();return json.loads(gzip.decompress(b) if path.name.endswith('.gz') else b),hashlib.sha256(b).hexdigest()

def valuation(a,p=47,cap=4):
    n=int(a);v=0
    if n==0:return cap
    while v<cap and n%p==0:v+=1;n//=p
    return v

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--miller',type=Path,default=Path('/tmp/p41_poincare_miller_jets47_rolling.json.gz'))
    parser.add_argument('--prefix',type=Path,default=Path('/tmp/p41_poincare_miller_slp_prefix47_rolling.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_miller_cm_units47_checkpoint.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_cm4_divisor47 import kernel
    from p41_hecke3_hessian47 import section_jets
    from p41_poincare_norms47 import pair_mul
    from p41_formal47_multiply import write_checkpoint
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    paths=[folder/'data/p41_cm3_makdisi47_certificate.json',Path('/tmp/p41_cm12_hecke47_verified.json.gz'),
           Path('/tmp/p41_cm7_q2_support47_verified.json.gz'),Path('/tmp/p41_cm8_q2_support47_verified.json.gz'),
           Path('/tmp/p41_t2_cm_targets47_verified.json.gz')]
    values=[load(p) for p in paths];b,u,c7,c8,images=[d for d,h in values]
    Wblocks=[r.from_json([b['coarse_evaluation_coefficients'][0]]),r.from_json([u['weight2_evaluation_coefficients'][0]]),
             r.from_json(c7['weight2_evaluation_coefficients'][0]),r.from_json(c8['weight2_evaluation_coefficients'][0])]
    Wblocks += [r.from_json(d['weight2_values']) for d in images['records']]
    W=tuple(np.vstack([a[i] for a in Wblocks]) for i in range(2))
    labels=['P_minus3','P_minus12','P_minus7']+['Z_minus8_'+str(n) for n in c8['fixed_necklace_indices_1based']]+[d['label'] for d in images['records']]
    assert len(labels)==26
    V2,V3=section_jets([W],sources,M,r);V2,V3=V2[0],V3[0]
    K=r.from_json(kernel(73,sources[1]['cusp_rank_columns_1based'],sources[1]['cusp_free_columns_1based'],sources[1]['canonical_kernel_block']))
    fc=r.mm(K,r.column(sources[1]['canonical_coefficients']));fv=r.mm(W,fc);assert np.all(r.units(fv))
    invf=r.inverse_values(fv);invf3=r.mul(r.mul(invf,invf),invf)
    W7=[r.from_json(a) for a in c7['weight2_evaluation_coefficients']];_,V37=section_jets(W7,sources,M,r)
    df7=r.mm(W7[1],fc);f7=r.rows(fv,[2]);if7=r.inverse_values(f7)
    slp={};snapshot_hashes={}
    for path in [args.prefix,args.miller]:
        if not path.exists():continue
        d,h=load(path);assert d['source_sha256']==hashes;snapshot_hashes[path.name]=h
        for k,step in enumerate(d['steps']):
            if 'principal_section_coefficients' not in step:continue
            cf=step['principal_section_coefficients'];hs=hashlib.sha256(json.dumps(cf,separators=(',',':')).encode()).hexdigest()
            assert hs==step['principal_coefficient_sha256']
            if k in slp:assert hs==slp[k]['principal_coefficient_sha256']
            slp[k]=step
    def record(label,cf,degree):
        numerator=r.mm(V3 if degree==3 else V2,cf);iv=invf3 if degree==3 else r.mul(invf,invf)
        result=r.mul(numerator,iv);pairs=[a[0] for a in r.to_json(result)]
        vals=[min(valuation(a),valuation(b)) for a,b in pairs]
        def product(indices):
            out=[1,0]
            for j in indices:out=pair_mul(out,pairs[j])
            assert out[1]==0
            return out
        out={'label':label,'values':pairs,'valuations_capped_at4':vals,
             'nonunit_support_indices_1based':[i+1 for i,v in enumerate(vals) if v],
             'norm_on_Q2_mod47four':product([2,2]+list(range(3,23))),
             'norm_T2_at_Pminus12_mod47four':product([0,23,24]),
             'norm_T2_at_Pminus7_mod47four':product([2,2,25])}
        if degree==3:
            fp=r.mm(V37[1],cf);fval=r.rows(numerator,[2])
            deriv=r.sub(r.mul(fp,r.mul(r.mul(if7,if7),if7)),
                        tuple(3*x%r.Q for x in r.mul(r.mul(fval,df7),r.mul(r.mul(if7,if7),r.mul(if7,if7)))))
            out['derivative_at_CM7_in_B_parameter']=r.to_json(deriv)
            out['CM7_zero_is_simple_mod47']=bool(vals[2] and r.units(deriv)[0,0])
        return out
    cf=r.mm(M['B'],r.column(sources[3]['negative_flip_section_seeds_and_coefficients'][0][1]))
    negative=record('negative_B_quadratic',cf,2)
    records=[]
    for k in sorted(slp):
        step=slp[k];rec=record('AddFlip_'+str(k+1),r.from_json(step['principal_section_coefficients']),3)
        rec.update({'step_index_1based':k+1,'principal_coefficient_sha256':step['principal_coefficient_sha256']});records.append(rec)
    out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
         'point_source_sha256':{p.name:h for p,(d,h) in zip(paths,values)},'snapshot_sha256':snapshot_hashes,
         'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'support_labels':labels,'base_section_values':r.to_json(fv),'available_steps':len(records),
         'missing_step_indices_1based':[k+1 for k in range(max(slp,default=-1)+1) if k not in slp],
         'negative_B':negative,'steps':records,
         'status':'exact recorded unit/valuation data on actual CM points; valuation4 is only a lower bound; no division by47 and no full nonformal height claimed'}
    digest,size=write_checkpoint(args.output,out)
    bad=[rec['step_index_1based'] for rec in records if rec['nonunit_support_indices_1based']]
    print('ACTUAL CM SLP UNIT CHECK',len(records),'steps, nonunit steps',bad,'bytes',size,'sha',digest,flush=True)
if __name__=='__main__':main()

