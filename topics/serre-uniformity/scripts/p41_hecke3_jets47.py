#!/usr/bin/env python3
"""Actual four-target Hecke jets, with exact NumPy trace evaluation."""
import argparse,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

def trace_indices(model):
    import numpy as np
    from verify_p41_makdisi47 import mm2,index
    signed=[0]*1681;n=0
    for k in range(1,1681):
        neg=index(-(k%41),-(k//41))
        if k<neg:n+=1;signed[k]=n;signed[neg]=-n
    signed=np.array(signed,dtype=np.int16)
    gh=np.array([[mm2(g,h) for h in model['sl2_normalizer_mod_signs']] for g in model['sl2_representatives']],dtype=np.int64)
    pairs=np.array(model['basis_pairs'],dtype=np.int64);indices=[]
    for pos in range(2):
        v=pairs[:,pos,:]
        a=(gh[:,None,:,0,0]*v[None,:,None,0]+gh[:,None,:,0,1]*v[None,:,None,1])%41
        b=(gh[:,None,:,1,0]*v[None,:,None,0]+gh[:,None,:,1,1]*v[None,:,None,1])%41
        indices.append(signed[a+41*b])
    signs=np.sign(indices[0]).astype(np.int8)*np.sign(indices[1]).astype(np.int8)
    return abs(indices[0])-1,abs(indices[1])-1,signs

def evaluate(Es,Hs,indices,C,r,degree):
    import numpy as np
    a,b,signs=indices;values=[]
    for H in Hs:
        gram=np.zeros((840,840),dtype=np.int64)
        for j in range(degree+1):
            first=(Es[j].T@H)%r.Q
            gram=(gram+first@Es[degree-j])%r.Q
        # Every Gram dot product has length80; the averaging sum has length42.
        assert 80*(r.Q-1)**2<2**63 and 42*(r.Q-1)<2**63
        values.append((gram[a,b]*signs).sum(axis=2)%r.Q)
    return r.mm(tuple(values),C)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    parser.add_argument('--source-jets',type=Path,default=Path('/tmp/p41_formal47_abel_jets_checkpoint.json.gz'))
    parser.add_argument('--hecke',type=Path,default=Path('/tmp/p41_hecke47_checkpoint.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_hecke3_jets47_checkpoint.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_formal47_multiply import write_checkpoint
    names=['p41_local47_torsion_certificate.json','p41_makdisi47_certificate.json.gz','p41_evaluation_jets47_checkpoint.json.gz']
    raws=[(folder/'data'/n).read_bytes() for n in names]
    torsion,model,jets=[json.loads(gzip.decompress(raw) if n.endswith('.gz') else raw) for n,raw in zip(names,raws)]
    sr=args.source_jets.read_bytes();source=json.loads(gzip.decompress(sr))
    hr=args.hecke.read_bytes();hecke=json.loads(gzip.decompress(hr));op=hecke['operators']['3']
    curve=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
    C=r.from_json(model['basis_inverse']);indices=trace_indices(model)
    out={'level':41,'auxiliary_prime':47,'precision':4,
         'source_sha256':{n:hashlib.sha256(raw).hexdigest() for n,raw in zip(names,raws)},
         'source_jets_sha256':hashlib.sha256(sr).hexdigest(),'raw_hecke_sha256':hashlib.sha256(hr).hexdigest(),'targets':[]}
    if args.output.exists():
        prior=json.loads(gzip.decompress(args.output.read_bytes()))
        assert all(prior[k]==out[k] for k in ['source_sha256','source_jets_sha256','raw_hecke_sha256'])
        out=prior
    for n,target in enumerate(op['targets']):
        if len(out['targets'])>n:continue
        inputs=[torsion['field_polynomial_ascending'],model['sqrt_minus_one_lift'],curve['weil_pairing'],source['P_jets'],source['Q_jets'],target['kernel_x']]
        with tempfile.TemporaryDirectory(prefix='serre-p41-hecke3-jets-') as work:
            work=Path(work);ip=work/'input.gp';opth=work/'output.json'
            ip.write_text('jet_input='+json.dumps(inputs,separators=(',',':'))+';\n')
            scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp','p41_cusp_divisors47.gp','p41_cm4_divisor47.gp']]
            scripts += [Path(__file__).with_name('p41_formal47_abel_jets.gp'),Path(__file__).with_suffix('.gp')]
            code='\n'.join([f'read({json.dumps(str(s))});' for s in scripts]+[f'read({json.dumps(str(ip))});',f'p41_hecke3_jets47(jet_input,{json.dumps(str(opth))});','quit;'])
            process=subprocess.run([args.gp,'-q','-f','-s','268435456'],input=code,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            print(process.stdout,flush=True)
            if process.returncode or '***' in process.stdout or not opth.exists():raise RuntimeError('Actual Hecke jet GP failure')
            record=json.loads(opth.read_text())
        Hs=[np.array(x,dtype=np.int64)%r.Q for x in record[:2]];Es=[np.array(x,dtype=np.int64)%r.Q for x in record[2]]
        actual=evaluate(Es,Hs,indices,C,r,0);assert r.to_json(actual)==target['evaluation_matrix']
        assert [p[0] for p in record[3]]==target['P'] and [p[0] for p in record[4]]==target['Q']
        derivative=evaluate(Es,Hs,indices,C,r,1)
        out['targets'].append({'kernel_x':target['kernel_x'],'P_jets':record[3],'Q_jets':record[4],'evaluation_derivatives':r.to_json(derivative)})
        write_checkpoint(args.output,out)
        print('Actual T3 target',n+1,'all820x73 constant values match R131; first jets complete.',flush=True)
    permutation=[i-1 for i in op['necklace_transport_1based']];tau=[i-1 for i in model['frobenius_permutation_1based']]
    A=r.from_json(model['frobenius_basis_matrix']);matrices=[r.rows(r.from_json(t['evaluation_derivatives']),permutation) for t in out['targets']]
    roots=[t['kernel_x'] for t in out['targets']]
    for j,matrix in enumerate(matrices):
        bar=roots.index([roots[j][0],-roots[j][1]%r.Q])
        assert r.equal(r.mm(matrix,A),r.conjugate(r.rows(matrices[bar],tau)))
    total=r.zeros(820,73)
    for matrix in matrices:total=r.add(total,matrix)
    total=tuple(x*pow(3,-1,r.Q)%r.Q for x in total)
    expected=r.mm(r.from_json(jets['evaluation_derivatives']),r.from_json(op['weight2_operator']))
    assert r.equal(total,expected)
    out['status']='all four actual3-isogeny first jets, full constants, Frobenius and differentiated T3 identity PASS'
    digest,size=write_checkpoint(args.output,out);print('Actual full Hecke jets',size,digest,flush=True)

if __name__=='__main__':main()
