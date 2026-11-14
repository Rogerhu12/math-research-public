#!/usr/bin/env python3
"""Build the actual 47-adic weight-two evaluation model of X_ns^+(41)."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    script = Path(__file__).resolve()
    data_dir = script.with_name('data')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gp', default=shutil.which('gp') or '/tmp/pari-2.19.0/gp')
    parser.add_argument('--precision', type=int, choices=(1, 2, 3, 4), default=4)
    parser.add_argument('--output', type=Path, default=data_dir/'p41_makdisi47_certificate.json.gz')
    args = parser.parse_args()
    torsion_path = data_dir/'p41_local47_torsion_certificate.json'
    hecke_path = data_dir/'p41_full_chow_heegner_certificate.json.gz'
    torsion_bytes = torsion_path.read_bytes()
    hecke_bytes = hecke_path.read_bytes()
    torsion = json.loads(torsion_bytes)
    hecke = json.loads(gzip.decompress(hecke_bytes))
    curve = next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
    i47 = hecke['indices'].index(47)-1
    fields = [[c['factor_descending'], c['directions'][i47][0]] for c in hecke['fields']]
    inputs = [torsion['field_polynomial_ascending'], curve['P'], curve['Q'],
              curve['weil_pairing'], torsion['frobenius_lift'], fields]
    with tempfile.TemporaryDirectory(prefix='serre-p41-makdisi47-') as work:
        work = Path(work)
        input_path = work/'input.gp'
        result_path = work/'result.json'
        input_path.write_text('model_input='+json.dumps(inputs,separators=(',',':'))+';\n')
        source = '\n'.join([
            f'read({json.dumps(str(script.with_name("p41_local47_torsion.gp")))});',
            f'read({json.dumps(str(script.with_suffix(".gp")))});',
            f'read({json.dumps(str(input_path))});',
            f'p41_makdisi47(model_input,{json.dumps(str(result_path))},{args.precision});',
            'quit;'])
        process = subprocess.Popen([args.gp,'-q','-f','-s','1073741824'],
                                   stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,text=True)
        process.stdin.write(source)
        process.stdin.close()
        output=[]
        for line in process.stdout:
            print(line.rstrip(),flush=True)
            output.append(line)
        if process.wait()!=0 or '***' in ''.join(output) or not result_path.exists():
            raise RuntimeError('PARI model construction did not complete; see the output above')
        raw = json.loads(result_path.read_text())
    names = ['precision','sqrt_minus_one_lift','candidate_pairs','pivot_rows_1based',
             'basis_columns_1based','necklaces','sl2_representatives','sl2_normalizer_mod_signs',
             'frobenius_permutation_1based','unit_minor_mod47','basis_inverse',
             'evaluation_matrix','frobenius_basis_matrix','local_factor_descending']
    result = dict(zip(names,raw))
    result.update({
        'level':41,'auxiliary_prime':47,'modulus':47**args.precision,
        'genus':54,'cusp_count':20,'line_bundle':'K_X+D','line_bundle_degree':126,
        'dimension':73,'evaluation_point_count':820,'residue_degree':2,
        'quadratic_polynomial_ascending':[1,0,1],
        'curve_A':1,'curve_B':32,'j_mod47':9,
        'relative_trace_degree':20,'cyclotomic_weight':1,
        'torsion_source':torsion_path.name,
        'torsion_source_sha256':hashlib.sha256(torsion_bytes).hexdigest(),
        'hecke_source':hecke_path.name,
        'hecke_source_sha256':hashlib.sha256(hecke_bytes).hexdigest(),
        'coefficient_order':'constant, sqrt(-1)',
        'result':'actual weight-two evaluation model; no QC root certificate',
    })
    result['basis_pairs']=[result['candidate_pairs'][i-1] for i in result['basis_columns_1based']]
    encoded=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(gzip.compress(encoded,mtime=0))
    print('Raw JSON bytes',len(encoded),'compressed bytes',args.output.stat().st_size)
    print('SHA256',hashlib.sha256(args.output.read_bytes()).hexdigest())


if __name__=='__main__':
    main()
