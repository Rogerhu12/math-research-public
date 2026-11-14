#!/usr/bin/env python3
"""Retain the completed CM36 branch0 and finish branch1 without raw ring division.

The original GP source used / on a polynomial unit modulo47^4; PARI's
Euclidean inversion can hit a nonunit intermediate coefficient.  The new
source verifies the already derived integral target equations by cross
multiplication and uses the existing certified unramified-ring inverse.
Both branch source hashes are preserved separately, without relabelling.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    parser.add_argument('--branch0',type=Path,default=Path('/tmp/p41_cm36_hecke47_branch0.json.gz'))
    parser.add_argument('--branch1',type=Path,default=Path('/tmp/p41_cm36_hecke47_branch1.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_cm36_hecke47_raw.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();here=Path(__file__).parent
    sys.path.insert(0,str(here));sys.path.insert(0,str(folder))
    from p41_cm36_hecke47 import prepare,save
    inputs,hashes,meta=prepare(folder)
    raw0=args.branch0.read_bytes();first=json.loads(gzip.decompress(raw0))
    assert hashlib.sha256(raw0).hexdigest()=='9227e6b5661f8a3a966f86462786d31ee17f771e9020620fae2fecc0f4d43666'
    assert first['branch']==0 and first['source_sha256']==hashes
    assert first['generating_source_sha256']=={
      'p41_cm36_hecke47.py':'51479d1351de327e4c691cf04c2618e0d83b5fb10248c0a4ec5cff96d458f557',
      'p41_cm36_hecke47.gp':'d33d164a455aef1efddc3a209d5ea9a12f570c2fb76128d1ba9a6c2c029e08ff'}
    gp_source=here/'p41_cm36_hecke47_corrected.gp'
    sources=[Path(prepare.__code__.co_filename),Path(__file__),gp_source]
    sourcehash={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    if args.branch1.exists():
        second=json.loads(gzip.decompress(args.branch1.read_bytes()))
        assert second['generating_source_sha256']==sourcehash and second['source_sha256']==hashes
    else:
        with tempfile.TemporaryDirectory(prefix='serre-p41-cm36-finish-') as td:
            td=Path(td);ip=td/'input.gp';op=td/'result.json'
            ip.write_text('cm36_input='+json.dumps(inputs,separators=(',',':'))+';\n')
            gp_files=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp',
                 'p41_cm3_makdisi47.gp','p41_formal47_abel_jets.gp']]+[gp_source]
            code='\n'.join([f'read({json.dumps(str(p))});' for p in gp_files]+
                  [f'read({json.dumps(str(ip))});',f'p41_cm36_hecke47(cm36_input,2,{json.dumps(str(op))});','quit;'])
            proc=subprocess.Popen([args.gp,'-q','-f','-s','134217728'],stdin=subprocess.PIPE,
                 stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            proc.stdin.write(code);proc.stdin.close();lines=[]
            for line in proc.stdout:print(line.rstrip(),flush=True);lines.append(line)
            rc=proc.wait()
            if rc or '***' in ''.join(lines) or not op.exists():raise RuntimeError('Actual CM36 branch1 failed')
            record=json.loads(op.read_text())
        keys=['curve_A_extension','curve_B_extension','j_invariant_extension','P_plus','Q_plus',
              'P_minus','Q_minus','actual_frobenius_matrix','weight2_values']
        assert len(record)==len(keys);second=dict(zip(keys,record))
        assert second['actual_frobenius_matrix']==meta['target_frobenius_torsion_matrices'][1]
        for key,value in [('curve_A_extension',meta['actual_curve_A'][1]),
              ('curve_B_extension',meta['actual_curve_B'][1]),('j_invariant_extension',meta['actual_j_invariants'][1])]:
            assert second[key][0]==value and not any(second[key][1:])
        assert len(second['weight2_values'])==20 and all(len(row)==73 for row in second['weight2_values'])
        second.update({'level':41,'auxiliary_prime':47,'precision':4,'branch':1,
          'source_sha256':hashes,'generating_source_sha256':sourcehash,
          'source_necklace_indices_1based':meta['source_necklace_indices_1based'],
          'target_necklace_indices_1based':meta['target_necklace_indices_1based'],
          'target_frobenius_permutation_1based':meta['target_frobenius_permutations_1based'][1],
          'curve_A':meta['actual_curve_A'][1],'curve_B':meta['actual_curve_B'][1],
          'j_invariant':meta['actual_j_invariants'][1],
          'status':'actual two cyclic3-isogenies, calibrated20 CM36 targets, all73 values and full Frobenius PASS; no height claimed'})
        size,sha=save(args.branch1,second);print('ACTUAL CM36 SECOND BRANCH SAVED',size,sha,flush=True)
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
      'generating_source_sha256':sourcehash,'branch_sha256':{'0':hashlib.sha256(raw0).hexdigest(),
        '1':hashlib.sha256(args.branch1.read_bytes()).hexdigest()},'records':[first,second],
      'exact_divisor_identity':'T3(Z_minus4)=2*Z_minus36; degree80=2*40',
      'status':'all4 actual cyclic3-isogenies, two20-point CM36 branches and all73 model values PASS; no Jacobian transport or height claimed'}
    result.update(meta);size,sha=save(args.output,result)
    print('ACTUAL COMPLETE CM36 HECKE SAVED',size,sha,flush=True)


if __name__=='__main__':main()
