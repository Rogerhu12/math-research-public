#!/usr/bin/env python3
"""Full820-point actual cubic jets for later choices of integral Abel charts."""
import argparse,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    parser.add_argument('--source-jets',type=Path,default=Path('/tmp/p41_formal47_abel_jets_checkpoint.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_source_cubic47_checkpoint.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import numpy as np
    import p41_r2_matrix as r
    from p41_hecke3_jets47 import trace_indices,evaluate
    from p41_formal47_multiply import write_checkpoint
    names=['p41_local47_torsion_certificate.json','p41_makdisi47_certificate.json.gz','p41_evaluation_jets47_checkpoint.json.gz']
    raws=[(folder/'data'/n).read_bytes() for n in names]
    torsion,model,first=[json.loads(gzip.decompress(raw) if n.endswith('.gz') else raw) for n,raw in zip(names,raws)]
    source_raw=args.source_jets.read_bytes();source=json.loads(gzip.decompress(source_raw))
    curve=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
    inputs=[torsion['field_polynomial_ascending'],model['sqrt_minus_one_lift'],curve['weil_pairing'],source['P_jets'],source['Q_jets']]
    with tempfile.TemporaryDirectory(prefix='serre-p41-source-cubic-') as work:
        work=Path(work);ip=work/'input.gp';op=work/'output.json';ip.write_text('source_input='+json.dumps(inputs,separators=(',',':'))+';\n')
        scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp','p41_cusp_divisors47.gp','p41_cm4_divisor47.gp']]
        scripts += [Path(__file__).with_name(n) for n in ['p41_formal47_abel_jets.gp','p41_hecke3_jets47.gp','p41_source_cubic47.gp']]
        code='\n'.join([f'read({json.dumps(str(s))});' for s in scripts]+[f'read({json.dumps(str(ip))});',f'p41_source_cubic47(source_input,{json.dumps(str(op))});','quit;'])
        run=subprocess.run([args.gp,'-q','-f','-s','268435456'],input=code,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        print(run.stdout,flush=True)
        if run.returncode or '***' in run.stdout or not op.exists():raise RuntimeError('Actual cubic GP failure')
        record=json.loads(op.read_text())
    Hs=[np.array(x,dtype=np.int64)%r.Q for x in record[:2]];Es=[np.array(x,dtype=np.int64)%r.Q for x in record[2]]
    indices=trace_indices(model);C=r.from_json(model['basis_inverse']);A=r.from_json(model['frobenius_basis_matrix']);tau=[i-1 for i in model['frobenius_permutation_1based']]
    coefficients=[]
    for k in range(4):
        M=evaluate(Es,Hs,indices,C,r,k)
        if k==0:assert r.to_json(M)==model['evaluation_matrix']
        if k==1:assert r.to_json(M)==first['evaluation_derivatives']
        assert r.equal(r.mm(M,A),r.conjugate(r.rows(M,tau)))
        assert r.to_json(r.rows(M,[i-1 for i in source['point_indices_1based']]))==source['evaluation_coefficients'][k]
        coefficients.append(r.to_json(M));print('Actual full820x73 cubic coefficient',k,'PASS.',flush=True)
    out={'level':41,'auxiliary_prime':47,'precision':4,'order':4,'point_indices_1based':list(range(1,821)),
         'evaluation_coefficients':coefficients,'source_sha256':{n:hashlib.sha256(raw).hexdigest() for n,raw in zip(names,raws)},
         'restricted_cubic_sha256':hashlib.sha256(source_raw).hexdigest(),
         'status':'full actual cubic jets, all Frobenius identities and original108-point restrictions PASS'}
    digest,size=write_checkpoint(args.output,out);print('Full actual source cubic data',size,digest,flush=True)

if __name__=='__main__':main()
