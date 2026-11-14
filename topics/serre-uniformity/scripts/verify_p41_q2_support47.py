#!/usr/bin/env python3
"""Independently verify actual CM support and jets of the degree22 T2 fixed divisor."""
import argparse,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    from p41_formal47_multiply import write_checkpoint
    raw=args.input.read_bytes();cert=json.loads(gzip.decompress(raw))
    names=['p41_local47_torsion_certificate.json','p41_makdisi47_certificate.json.gz']
    raws=[(folder/'data'/n).read_bytes() for n in names]
    assert cert['source_sha256']=={n:hashlib.sha256(b).hexdigest() for n,b in zip(names,raws)}
    torsion,model=[json.loads(gzip.decompress(b) if n.endswith('.gz') else b) for n,b in zip(names,raws)]
    ew=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')['weil_pairing']
    inputs=[torsion['field_polynomial_ascending'],torsion['frobenius_lift'],ew,model['sqrt_minus_one_lift'],
            model['basis_pairs'],model['basis_inverse'],model['frobenius_basis_matrix'],model['necklaces'],
            model['sl2_representatives'],model['sl2_normalizer_mod_signs'],cert['CM_discriminant']]
    keys=['curve_A','curve_B','CM_discriminant','P_constant','Q_old_constant','old_Weil_pairing','pairing_adjustment',
          'CM_square_root','CM_endomorphism_matrix','frobenius_torsion_matrix','fixed_necklace_indices_1based',
          'fixed_frobenius_permutation_1based','weight2_evaluation_coefficients','P_jets','Q_jets']
    vals=[cert[k] for k in keys]
    with tempfile.TemporaryDirectory(prefix='serre-p41-q2-verify-') as work:
        work=Path(work);ip=work/'input.gp';op=work/'result.json'
        ip.write_text('q2_input='+json.dumps(inputs,separators=(',',':'))+';\nq2_cert='+json.dumps(vals,separators=(',',':'))+';\n')
        scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp']]
        scripts.append(Path(__file__).with_suffix('.gp'))
        code='\n'.join([f'read({json.dumps(str(p))});' for p in scripts]+
                       [f'read({json.dumps(str(ip))});',f'p41v_q2_support47(q2_input,q2_cert,{json.dumps(str(op))});','quit;'])
        proc=subprocess.Popen([args.gp,'-q','-f','-s','134217728'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        proc.stdin.write(code);proc.stdin.close();messages=[]
        for line in proc.stdout:print(line.rstrip(),flush=True);messages.append(line)
        rc=proc.wait()
        if rc or '***' in ''.join(messages) or not op.exists():raise RuntimeError(f'Independent Q2 support failed (return code {rc})')
    result=dict(cert);result['raw_source_sha256']=hashlib.sha256(raw).hexdigest()
    result['verification_source_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_suffix('.gp')]}
    result['status']='independent group-law CM self-isogeny, lifted41-torsion, primitive Weil root, all actual fixed necklaces and direct all73 coefficient traces PASS'
    digest,size=write_checkpoint(args.output,result)
    print('INDEPENDENT ACTUAL Q2 SUPPORT ALL PASS',size,digest,flush=True)
if __name__=='__main__':main()

