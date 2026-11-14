#!/usr/bin/env python3
"""Actual mixed formal Poincare values for mC12 or mC7 against mB in the R141 frame."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def read(path):
    b=path.read_bytes();return json.loads(gzip.decompress(b)),hashlib.sha256(b).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--cm-endpoints',type=Path,default=Path('/tmp/p41_cm_formal_endpoints47_checkpoint.json.gz'))
    p.add_argument('--bases',type=Path,default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    p.add_argument('--jets',type=Path,default=Path('/tmp/p41_source_cubic47_checkpoint.json.gz'))
    p.add_argument('--B-endpoints',type=Path,default=Path('/tmp/p41_hecke3_exponential_checkpoint.json.gz'))
    p.add_argument('--B-height',type=Path,default=Path('/tmp/p41_hecke3_formal_height47_compact.json.gz'))
    p.add_argument('--hessian',type=Path,default=Path('/tmp/p41_hecke3_hessian47_compact.json.gz'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_cm_mixed_formal_height47_checkpoint.json.gz'))
    args=p.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_cm4_divisor47 import kernel
    from p41_formal47_exponential import construct_point
    from p41_poincare_formal47 import principal_inverse
    from p41_hecke3_hessian47 import section_jets
    from p41_poincare_norms47 import pair_mul,pair_inverse
    from p41_formal47_multiply import write_checkpoint,point_hash
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    paths=[args.cm_endpoints,args.bases,args.jets,args.B_endpoints,args.B_height,args.hessian]
    readouts=[read(x) for x in paths];cm,base,jets,Bexp,Bheight,hessian=[d for d,h in readouts]
    inputs={p.name:h for p,(d,h) in zip(paths,readouts)}
    for o in [cm,base,Bexp,Bheight,hessian]:assert o['source_sha256']==hashes
    assert Bexp['bases_sha256']==inputs[args.bases.name] and Bexp['jets_sha256']==inputs[args.jets.name]
    spaces=[];vs=[];families=[]
    for item in base['families']:
        points=[i-1 for i in item['points_1based']];families.append(points)
        W=[r.rows(r.from_json(v),points) for v in jets['evaluation_coefficients']]
        V2,_=section_jets(W,sources,M,r);spaces.append({1:W,2:V2})
        vs.append(r.mm(M['W'],r.from_json(item['v_coefficients'])))
    def raw_norm(coeff,degree,family,parameters):
        values=[r.mm(v,coeff) for v in spaces[family][degree]]
        par=r.from_json(parameters);t=(par[0].T,par[1].T)
        power=r.column([[1,0] for _ in range(54)]);value=r.zeros(54,1)
        for v in values:value=r.add(value,r.mul(v,power));power=r.mul(power,t)
        assert np.all(r.units(values[0])) and np.all(r.units(value))
        ratios=r.mul(value,r.inverse_values(values[0]));out=[1,0]
        for i in range(54):out=pair_mul(out,[int(ratios[0][i,0]),int(ratios[1][i,0])])
        assert out[1]==0
        return out
    def inverse_norm(coeff,other_family,parameters):
        a=raw_norm(coeff,2,other_family,parameters)
        vcf=r.from_json(base['families'][1-other_family]['v_coefficients'])
        b=raw_norm(vcf,1,other_family,parameters)
        return pair_mul(a,pair_inverse(pair_mul(b,b)))
    def enc(value):return hashlib.sha256(json.dumps(value,separators=(',',':')).encode()).hexdigest()
    second_coeff=r.from_json(Bheight['principal_numerators'][1])
    correction=r.from_json(hessian['hecke_correction_matrix'])
    zB=r.from_json(Bexp['exponentials'][1]['target_logarithm'])
    records=[]
    for discr in [12,7]:
        target=cm['targets']['x'+str(discr)]['targets']['m']['exponentials'][0]
        z=r.from_json(target['target_logarithm']);plus=r.from_json(target['point_coordinates'])
        assert point_hash(plus,r.from_json(target['point_frobenius']))==target['point_sha256']
        minus,Aminus,negative=construct_point(r.neg(z),base['families'][0],jets,sources[1],M,r,kernel)
        coeff,proof=principal_inverse(plus,minus,vs[0],vs[1],M,r,random.Random(4104717300+discr))
        first=inverse_norm(coeff,1,Bexp['exponentials'][1]['parameters'])
        second=inverse_norm(second_coeff,0,negative['parameters'])
        delta=pair_mul(first,pair_inverse(second))
        assert delta[1]==0 and delta[0]%47**3==1
        ld=(delta[0]-1)%r.Q;half=ld*pow(2,-1,r.Q)%r.Q
        bval=r.mm(r.mm(z,correction),(zB[0].T,zB[1].T))
        assert bval[1][0,0]==0 and int(bval[0][0,0])%47**2==0
        bv=int(bval[0][0,0]);value=(half+bv)%r.Q
        compact={k:v for k,v in proof.items() if k not in ['product_basis_inverse','colon_kernel_block']}
        compact['omitted_rebuildable_matrix_sha256']={k:enc(proof[k]) for k in ['product_basis_inverse','colon_kernel_block']}
        records.append({'discriminant':-discr,'positive_formal_point_sha256':target['point_sha256'],
                        'negative_formal_point_sha256':point_hash(minus,Aminus),
                        'negative_parameters':negative['parameters'],'actual_first_inverse_function':compact,
                        'first_inverse_degree_zero_norm':first,'second_inverse_degree_zero_norm':second,
                        'double_inverse_unit':delta,'log_double_inverse_unit':ld,'half_log_double_inverse':half,
                        'actual_hecke_bilinear_correction':bv,'actual_hecke_local_log':value,
                        'first_logarithm':target['target_logarithm'],'second_logarithm':Bexp['exponentials'][1]['target_logarithm'],
                        'fibre':'P_(m(P-b),mB), rational1 in precisely the R141 first/second Abel divisor frame'})
        print('ACTUAL CM MIXED FORMAL HEIGHT',discr,'first',first,'second',second,'half',half,'bilinear',bv,'value',value,flush=True)
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'input_sha256':inputs,
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'records':records,
            'status':'actual mixed formal double-inverse norms and Hecke-compatible local values in the fixed R141 frame; not global heights'}
    sha,size=write_checkpoint(args.output,result);print('ACTUAL CM MIXED FORMAL HEIGHTS SAVED',size,sha,flush=True)

if __name__=='__main__':main()

