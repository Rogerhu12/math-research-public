#!/usr/bin/env python3
"""Independently verify both actual vertical branches and20 CM16 values."""
import argparse,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--input',type=Path,default=Path('/tmp/p41_cm16_hecke47_raw.json.gz'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_cm16_hecke47_verified.json.gz'))
    p.add_argument('--gp',default='/tmp/pari-2.19.0/gp');args=p.parse_args()
    folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    from p41_cm16_hecke47 import prepare
    from p41_formal47_multiply import write_checkpoint
    from p41_hecke3_hessian47 import projective_rows
    import p41_r2_matrix as r
    inputs,hashes,meta=prepare(folder);raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    assert data['source_sha256']==hashes and all(data[k]==v for k,v in meta.items())
    U=inputs[11];D=[[1,0],[0,21]];DI=[[1,0],[0,2]]
    model=json.loads(gzip.decompress((folder/'data/p41_makdisi47_certificate.json.gz').read_bytes()))
    ns=model['necklaces']
    def matmul(a,b):return [[(a[i][0]*b[0][j]+a[i][1]*b[1][j])%41 for j in range(2)] for i in range(2)]
    def necklace(j):
        a,e=ns[j-1];return [[a,(e-a*a)%41],[1,-a%41]]
    def proportional(a,b):
        i0,j0=next((i,j) for i in range(2) for j in range(2) if b[i][j]%41)
        return a[i0][j0]%41!=0 and all((a[i][j]*b[i0][j0]-b[i][j]*a[i0][j0])%41==0 for i in range(2) for j in range(2))
    H=[[(U[i][j]+int(i==j))%41 for j in range(2)] for i in range(2)]
    for k,j in enumerate(meta['source_necklace_indices_1based']):
        R=necklace(j);UR=matmul(U,R);RU=matmul(R,U)
        assert all((UR[i][l]+RU[i][l])%41==0 for i in range(2) for l in range(2))
        target=necklace(meta['target_necklace_indices_1based'][k]);assert proportional(matmul(matmul(DI,R),D),target)
        hp=necklace(meta['source_necklace_indices_1based'][meta['horizontal_permutation_1based'][k]-1])
        assert proportional(matmul(H,R),matmul(hp,H))
    vals=r.from_json(data['weight2_values']);proj=projective_rows(vals,r)
    assert len(proj)==20 and None not in proj and len(set(proj))==20
    cert=[data[k] for k in ['P_plus','Q_plus','P_minus','Q_minus','actual_frobenius_matrix','weight2_values']]
    with tempfile.TemporaryDirectory(prefix='serre-verify-cm16-') as td:
        td=Path(td);ip=td/'input.gp';op=td/'result.json'
        ip.write_text('cm16_input='+json.dumps(inputs,separators=(',',':'))+';\ncm16_cert='+json.dumps(cert,separators=(',',':'))+';\n')
        scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp']]
        scripts.append(Path(__file__).with_suffix('.gp'))
        code='\n'.join([f'read({json.dumps(str(p))});' for p in scripts]+
                       [f'read({json.dumps(str(ip))});',f'p41v_cm16_hecke47(cm16_input,cm16_cert,{json.dumps(str(op))});','quit;'])
        proc=subprocess.Popen([args.gp,'-q','-f','-s','134217728'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        proc.stdin.write(code);proc.stdin.close();lines=[]
        for line in proc.stdout:print(line.rstrip(),flush=True);lines.append(line)
        rc=proc.wait()
        if rc or '***' in ''.join(lines) or not op.exists() or json.loads(op.read_text())!=['PASS']:
            raise RuntimeError('Independent actual CM16 verification failed')
    data.update({'raw_source_sha256':hashlib.sha256(raw).hexdigest(),
                 'verification_source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_suffix('.gp')]},
                 'status':'independent group-law verification of all3 isogenies; opposite vertical kernel and alternative Eisenstein algorithm/direct trace give the same20x73 values; projective distinctness and Cartan transport PASS'})
    sha,size=write_checkpoint(args.output,data);print('INDEPENDENT ACTUAL CM16 PASS',size,sha,flush=True)

if __name__=='__main__':main()

