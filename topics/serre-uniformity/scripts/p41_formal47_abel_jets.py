#!/usr/bin/env python3
"""Actual cubic jets at a rational nonspecial54-point divisor, for formal exp."""
import argparse,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_cm4_divisor47 import kernel
    names=['p41_local47_torsion_certificate.json','p41_makdisi47_certificate.json.gz','p41_cusp_divisors47_certificate.json.gz','p41_evaluation_jets47_checkpoint.json.gz']
    raw=[(folder/'data'/n).read_bytes() for n in names]
    torsion,model,divs,jets=[json.loads(gzip.decompress(b) if n.endswith('.gz') else b) for n,b in zip(names,raw)]
    K=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    canonical=r.mm(r.from_json(model['evaluation_matrix']),K);tau=[x-1 for x in model['frobenius_permutation_1based']]
    families=[];used=set()
    for family_index in range(2):
        selected=[]
        for i,j in enumerate(tau):
            if j<=i or i in used or j in used:continue
            candidate=selected+[i,j]
            if len(r.rank_pivots(r.rows(canonical,candidate))[0])==len(candidate):selected=candidate
            if len(selected)==54:break
        assert len(selected)==54 and sorted(tau[i] for i in selected)==sorted(selected)
        r.inverse_matrix(r.rows(canonical,selected));families.append(selected);used.update(selected)
    selected=sum(families,[]);permutation=[selected.index(tau[i])+1 for i in selected]
    curve=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
    inputs=[torsion['field_polynomial_ascending'],torsion['frobenius_lift'],curve['P'],curve['Q'],curve['weil_pairing'],model['sqrt_minus_one_lift'],model['basis_pairs'],model['basis_inverse'],model['sl2_representatives'],model['sl2_normalizer_mod_signs'],model['frobenius_basis_matrix'],model['frobenius_permutation_1based'],model['evaluation_matrix'],[i+1 for i in selected],permutation,jets['evaluation_derivatives']]
    with tempfile.TemporaryDirectory(prefix='serre-p41-abel-jets-') as work:
        work=Path(work);ip=work/'input.gp';op=work/'output.json';ip.write_text('abel_input='+json.dumps(inputs,separators=(',',':'))+';\n')
        scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp','p41_cusp_divisors47.gp','p41_cm4_divisor47.gp']]+[Path(__file__).with_suffix('.gp')]
        code='\n'.join([f'read({json.dumps(str(s))});' for s in scripts]+[f'read({json.dumps(str(ip))});',f'p41_formal47_abel_jets(abel_input,{json.dumps(str(op))});','quit;'])
        process=subprocess.Popen([args.gp,'-q','-f','-s','268435456'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        process.stdin.write(code);process.stdin.close();output=[]
        for line in process.stdout:print(line.rstrip(),flush=True);output.append(line)
        result=process.wait()
        if result!=0 or '***' in ''.join(output) or not op.exists():raise RuntimeError('Actual Abel jet computation failed: '+str(result))
        record=json.loads(op.read_text())
    result={'level':41,'auxiliary_prime':47,'precision':4,'modulus':47**4,'order':4,
            'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in zip(names,raw)},
            'family':'y^2=x^3+x+32+t','point_indices_1based':[i+1 for i in selected],
            'point_families_1based':[[i+1 for i in family] for family in families],
            'frobenius_permutation_1based':permutation,'P_jets':record[0],'Q_jets':record[1],
            'evaluation_coefficients':record[2],'status':'actual cubic Abel-point jets; formal exponential reconstruction pending'}
    encoded=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode();packed=gzip.compress(encoded,mtime=0)
    out=args.output or folder/'data/p41_formal47_abel_jets_checkpoint.json.gz';out.write_bytes(packed)
    print('Saved',len(packed),'bytes SHA256',hashlib.sha256(packed).hexdigest(),flush=True)


if __name__=='__main__':main()
