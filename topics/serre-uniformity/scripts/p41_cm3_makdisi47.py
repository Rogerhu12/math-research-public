#!/usr/bin/env python3
"""Compute actual coarse jets of the j=0 CM point in the level-41 model."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    script=Path(__file__).resolve();data_dir=script.with_name('data')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gp',default=shutil.which('gp') or '/tmp/pari-2.19.0/gp')
    parser.add_argument('--coarse-order',type=int,default=3)
    parser.add_argument('--output',type=Path,default=data_dir/'p41_cm3_makdisi47_certificate.json')
    args=parser.parse_args()
    torsion_path=data_dir/'p41_local47_torsion_certificate.json'
    model_path=data_dir/'p41_makdisi47_certificate.json.gz'
    torsion_bytes=torsion_path.read_bytes();model_bytes=model_path.read_bytes()
    torsion=json.loads(torsion_bytes);model=json.loads(gzip.decompress(model_bytes))
    cm=next(c for c in torsion['curves'] if c['label']=='CM_minus3')
    reference=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
    inputs=[torsion['field_polynomial_ascending'],torsion['frobenius_lift'],cm['P'],cm['Q'],
            cm['weil_pairing'],cm['CM_unit'],cm['CM_matrix'],reference['weil_pairing'],
            model['sqrt_minus_one_lift'],model['basis_pairs'],model['basis_inverse'],
            model['frobenius_basis_matrix'],model['sl2_representatives'],model['necklaces']]
    with tempfile.TemporaryDirectory(prefix='serre-p41-cm3-jet47-') as temporary:
        temporary=Path(temporary);input_path=temporary/'input.gp';result_path=temporary/'result.json'
        input_path.write_text('cm_input='+json.dumps(inputs,separators=(',',':'))+';\n')
        code='\n'.join([
            f'read({json.dumps(str(script.with_name("p41_local47_torsion.gp")))});',
            f'read({json.dumps(str(script.with_name("p41_makdisi47.gp")))});',
            f'read({json.dumps(str(script.with_suffix(".gp")))});',
            f'read({json.dumps(str(input_path))});',
            f'p41_cm3_makdisi47(cm_input,{json.dumps(str(result_path))},{model["precision"]},{args.coarse_order});',
            'quit;'])
        proc=subprocess.Popen([args.gp,'-q','-f','-s','1073741824'],stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        proc.stdin.write(code);proc.stdin.close();output=[]
        for line in proc.stdout:print(line.rstrip(),flush=True);output.append(line)
        if proc.wait()!=0 or '***' in ''.join(output) or not result_path.exists():
            raise RuntimeError('CM-jet construction did not complete; see the output above')
        raw=json.loads(result_path.read_text())
    names=['precision','coarse_order','pairing_adjustment','CM_necklace','CM_necklace_index_1based',
           'CM_unit_matrix','frobenius_torsion_matrix','P_jets','Q_jets','stack_evaluation_coefficients',
           'coarse_evaluation_coefficients','unit_coordinate_1based','tangent_coordinate_1based',
           'affine_coordinate_coefficients']
    result=dict(zip(names,raw))
    result.update({'level':41,'auxiliary_prime':47,'modulus':model['modulus'],
                   'stack_parameter':'A in y^2=x^3+A*x+1','coarse_parameter':'t=A^3',
                   'line_bundle_trivialization':'weight-two Weierstrass value divided by A^2',
                   'torsion_source':torsion_path.name,'torsion_source_sha256':hashlib.sha256(torsion_bytes).hexdigest(),
                   'model_source':model_path.name,'model_source_sha256':hashlib.sha256(model_bytes).hexdigest(),
                   'result':'actual coarse CM point and jets; no QC root certificate'})
    encoded=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode()
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(encoded)
    print('Bytes',len(encoded),'SHA256',hashlib.sha256(encoded).hexdigest())


if __name__=='__main__':main()
