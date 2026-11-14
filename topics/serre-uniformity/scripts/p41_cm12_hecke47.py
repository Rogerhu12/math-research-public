#!/usr/bin/env python3
"""Actual CM(-12) and local T2 branch through the CM(-3) base point."""
import argparse,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_cm12_hecke47_certificate.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_formal47_multiply import write_checkpoint
    names=['p41_local47_torsion_certificate.json','p41_makdisi47_certificate.json.gz','p41_cm3_makdisi47_certificate.json','p41_hecke47_compact.json.gz']
    raws=[(folder/'data'/n).read_bytes() for n in names]
    torsion,model,cm3,hecke=[json.loads(gzip.decompress(b) if n.endswith('.gz') else b) for n,b in zip(names,raws)]
    ew=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')['weil_pairing']
    sourceindex=cm3['CM_necklace_index_1based'];targetindex=hecke['operators']['2']['necklace_transport_1based'][sourceindex-1]
    inputs=[torsion['field_polynomial_ascending'],torsion['frobenius_lift'],ew,model['sqrt_minus_one_lift'],
            cm3['P_jets'],cm3['Q_jets'],model['basis_pairs'],model['basis_inverse'],model['frobenius_basis_matrix'],
            model['sl2_representatives'][targetindex-1],cm3['frobenius_torsion_matrix']]
    with tempfile.TemporaryDirectory(prefix='serre-p41-cm12-') as work:
        work=Path(work);ip=work/'input.gp';op=work/'result.json';ip.write_text('cm12_input='+json.dumps(inputs,separators=(',',':'))+';\n')
        scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp','p41_formal47_abel_jets.gp']]
        scripts.append(Path(__file__).with_suffix('.gp'))
        code='\n'.join([f'read({json.dumps(str(s))});' for s in scripts]+[f'read({json.dumps(str(ip))});',f'p41_cm12_hecke47(cm12_input,{json.dumps(str(op))});','quit;'])
        run=subprocess.run([args.gp,'-q','-f','-s','268435456'],input=code,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        print(run.stdout,flush=True)
        if run.returncode or '***' in run.stdout or not op.exists():raise RuntimeError('Actual CM12 two-isogeny computation failed')
        rec=json.loads(op.read_text())
    W=[r.from_json([a]) for a in rec[0]];pivot=next(j for j in range(73) if r.units(r.cols(W[0],[j]))[0,0])
    # Normalize the actual projective curve coordinates and inspect a true tangent.
    denominator=[r.cols(a,[pivot]) for a in W];iv=[r.inverse_values(denominator[0])]
    for k in range(1,4):
        total=r.zeros(1,1)
        for j in range(1,k+1):total=r.add(total,r.mul(denominator[j],iv[k-j]))
        iv.append(r.neg(r.mul(iv[0],total)))
    affine=[]
    for k in range(4):
        a=r.zeros(1,73)
        for j in range(k+1):a=r.add(a,r.mul(W[j],iv[k-j]))
        affine.append(a)
    tangent=next(j for j in range(73) if r.units(r.cols(affine[1],[j]))[0,0])
    out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in zip(names,raws)},
         'source_CM_necklace_index_1based':sourceindex,'target_CM_necklace_index_1based':targetindex,
         'source_parameter':'A on y^2=x^3+A*x+1; coarse source parameter is A^3',
         'target_curve_at_zero':{'A':-15,'B':22,'j':54000},
         'weight2_evaluation_coefficients':rec[0],'target_P_jets':rec[1],'target_Q_jets':rec[2],
         'kernel_x_coefficients':rec[3],'target_A_coefficients':rec[4],'target_B_coefficients':rec[5],
         'source_j_coefficients':rec[6],'target_j_coefficients':rec[7],'target_frobenius_torsion_matrix':rec[8],
         'unit_coordinate_1based':pivot+1,'tangent_coordinate_1based':tangent+1,
         'affine_coordinate_coefficients':[r.to_json(a)[0] for a in affine],
         'generating_source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_suffix('.gp')]},
         'status':'actual T2 branch and CM_minus12 evaluation jets; complete torsion, target curve and Frobenius checks PASS; independent verification follows'}
    digest,size=write_checkpoint(args.output,out)
    print('Actual CM12 local model',size,digest,'source',sourceindex,'target',targetindex,'tangent',tangent+1,flush=True)

if __name__=='__main__':main()
