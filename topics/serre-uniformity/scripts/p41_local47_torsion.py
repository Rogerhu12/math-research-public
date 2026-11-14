#!/usr/bin/env python3
"""Generate actual p=41 torsion coordinates for the local auxiliary prime 47."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    source=Path(__file__).resolve()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gp',default=shutil.which('gp') or '/tmp/pari-2.19.0/gp')
    parser.add_argument('--output',type=Path,default=source.with_name('data')/'p41_local47_torsion_certificate.json')
    args=parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='serre-p41-local47-') as work:
        result=Path(work)/'coordinates.json'
        code=f'read({json.dumps(str(source.with_suffix(".gp")))});\np41_local47({json.dumps(str(result))});\nquit;\n'
        call=subprocess.run([args.gp,'-q','-f','-s','268435456'],input=code,text=True,capture_output=True,timeout=180,check=True)
        if '***' in call.stderr:raise RuntimeError(call.stderr)
        print(call.stdout.strip())
        f,phi,rows=json.loads(result.read_text())
    names=['curve_A','curve_B','elliptic_frobenius_trace','j_mod47','P','Q','weil_pairing','CM_unit','CM_matrix','CM_necklace']
    curves=[dict(zip(names,row)) for row in rows]
    curves[0]['label']='CM_minus3'
    curves[1]['label']='Makdisi_j9_fibre'
    data={'level':41,'auxiliary_prime':47,'precision':4,'modulus':47**4,
          'residue_degree':80,'full_41_torsion_residue_degree':80,
          'field_polynomial_ascending':f,'frobenius_lift':phi,'curves':curves}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,separators=(',',':'),sort_keys=True)+'\n')
    print('SHA256',hashlib.sha256(args.output.read_bytes()).hexdigest())


if __name__=='__main__':main()
