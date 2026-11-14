#!/usr/bin/env python3
"""Compute actual T2,T3 on the fixed layer41 evaluation basis at47."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import random


def write_compact(data, raw_sha256, path):
    """Keep final operators and small witnesses; hash reproducible target values."""
    compact = {k:v for k,v in data.items() if k != 'operators'}
    compact['format'] = 'compact-final-operators-with-target-evaluation-hashes'
    compact['full_raw_sha256'] = raw_sha256
    compact['operators'] = {}
    for ell, record in data['operators'].items():
        operator = {k:v for k,v in record.items() if k != 'targets'}
        operator['targets'] = []
        for target in record['targets']:
            entry = {k:v for k,v in target.items() if k != 'evaluation_matrix'}
            values = target['evaluation_matrix']
            assert len(values) == 820 and all(len(row) == 73 for row in values)
            encoded = json.dumps(values, separators=(',', ':')).encode()
            entry['evaluation_matrix_sha256'] = hashlib.sha256(encoded).hexdigest()
            operator['targets'].append(entry)
        compact['operators'][ell] = operator
    encoded = (json.dumps(compact, sort_keys=True, separators=(',', ':'))+'\n').encode()
    packed = gzip.compress(encoded, mtime=0)
    path.write_bytes(packed)
    print('Compact final operators:', path, len(packed), 'bytes; SHA256', hashlib.sha256(packed).hexdigest(), flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    parser.add_argument('--output',type=Path,help='full reproducible raw data; default /tmp/p41_hecke47_checkpoint.json.gz')
    parser.add_argument('--compact-output',type=Path)
    parser.add_argument('--compact-only',type=Path,help='compress an existing complete raw certificate without recomputing')
    args=parser.parse_args()
    folder=args.script_dir.resolve()
    compact_out=args.compact_output or folder/'data'/'p41_hecke47_compact.json.gz'
    if args.compact_only:
        packed=args.compact_only.read_bytes()
        write_compact(json.loads(gzip.decompress(packed)),hashlib.sha256(packed).hexdigest(),compact_out)
        return
    sys.path.insert(0,str(folder))
    from p41_cm4_divisor47 import kernel
    names=['p41_local47_torsion_certificate.json','p41_makdisi47_certificate.json.gz',
           'p41_cusp_divisors47_certificate.json.gz','p41_jacobi_cm_certificate.json']
    raw=[(folder/'data'/n).read_bytes() for n in names]
    torsion,model,divs,jacobi=[json.loads(gzip.decompress(b) if n.endswith('.gz') else b) for n,b in zip(names,raw)]
    curve=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
    K1=kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block'])
    inputs=[torsion['field_polynomial_ascending'],torsion['frobenius_lift'],curve['P'],curve['Q'],
            curve['weil_pairing'],model['sqrt_minus_one_lift'],model['basis_pairs'],model['basis_inverse'],
            model['sl2_representatives'],model['sl2_normalizer_mod_signs'],model['evaluation_matrix'],
            model['frobenius_basis_matrix'],K1,divs['cusp_free_columns_1based'],model['pivot_rows_1based'],
            model['necklaces'],[f['factor_descending'] for f in jacobi['fields']]]
    import p41_r2_matrix as r
    sources=[folder/'p41_local47_torsion.gp',folder/'p41_makdisi47.gp',folder/'p41_cusp_divisors47.gp',Path(__file__).with_suffix('.gp')]
    fingerprint=hashlib.sha256(b''.join(raw)+b''.join(p.read_bytes() for p in sources)).hexdigest()
    work=Path('/tmp/serre-p41-hecke47-work')/fingerprint;work.mkdir(parents=True,exist_ok=True)
    ip=work/'input.gp';ip.write_text('hecke_input='+json.dumps(inputs,separators=(',',':'))+';\n')
    records=[];operators=[];W=r.from_json(model['evaluation_matrix']);A1=r.from_json(model['frobenius_basis_matrix']);K=r.from_json(K1)
    free=[i-1 for i in divs['cusp_free_columns_1based']];piv=[i-1 for i in model['pivot_rows_1based']]
    lookup={tuple(x):i for i,x in enumerate(model['necklaces'])}
    for ell in (2,3):
        targets=[];values=r.zeros(820,73);iv=pow(ell,-1,41)
        permutation=[lookup[(a*iv%41,e*iv*iv%41)]+1 for a,e in model['necklaces']]
        for kr in range(1,ell+2):
            op=work/f'target-{ell}-{kr}.json'
            if not op.exists():
                code='\n'.join([f'read({json.dumps(str(p))});' for p in sources]+[
                    f'read({json.dumps(str(ip))});',f'p41_hecke47(hecke_input,{json.dumps(str(op))},{ell},{kr});','quit;'])
                proc=subprocess.Popen([args.gp,'-q','-f','-s','268435456'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
                proc.stdin.write(code);proc.stdin.close();lines=[]
                for line in proc.stdout:print(line.rstrip(),flush=True);lines.append(line)
                rc=proc.wait()
                if rc!=0 or '***' in ''.join(lines) or not op.exists():
                    raise RuntimeError(f'Actual Hecke target failed, returncode={rc}')
            record=json.loads(op.read_text());targets.append(record)
            values=r.add(values,r.rows(r.from_json(record[5]),[i-1 for i in permutation]))
        values=tuple(x*pow(ell,-1,r.Q)%r.Q for x in values);T=r.rows(values,piv)
        assert r.equal(r.mm(W,T),values)
        assert r.equal(r.mm(A1,r.conjugate(T)),r.mm(T,A1))
        TK=r.rows(r.mm(T,K),free);assert r.equal(r.mm(K,TK),r.mm(T,K))
        if ell==2:assert sum(int(TK[0][j,j]) for j in range(54))%r.Q==(-8)%r.Q and sum(int(TK[1][j,j]) for j in range(54))%r.Q==0
        records.append([ell,permutation,targets,r.to_json(T),r.to_json(TK)]);operators.append(TK)
        print('Actual T',ell,'full820-row/canonical/descent checks PASS.',flush=True)
    H=r.add(operators[0],tuple(2*x%r.Q for x in operators[1]));poly=[1]
    for f in jacobi['fields']:
        pp=f['factor_descending'];out=[0]*(len(poly)+len(pp)-1)
        for i,a in enumerate(poly):
            for j,b in enumerate(pp):out[i+j]+=a*b
        poly=out
    value=r.zeros(54,54)
    for c in poly:value=r.add(r.mm(value,H),tuple((c%r.Q)*x%r.Q for x in r.eye(54)))
    assert r.iszero(value)
    rng=random.Random(4104712107)
    for attempt in range(100):
        v=r.column([[rng.randrange(47),rng.randrange(47)] for _ in range(54)]);cyclic=r.zeros(54,54)
        for j in range(54):cyclic[0][:,j],cyclic[1][:,j]=v[0][:,0],v[1][:,0];v=r.mm(H,v)
        if len(r.rank_pivots(cyclic)[0])==54:break
    else:raise RuntimeError('No unit cyclic vector found')
    r.inverse_matrix(cyclic);cyclic=r.to_json(cyclic)
    print('Actual54-dimensional primitive Hecke spectrum/cyclicity PASS.',flush=True)
    data={'level':41,'auxiliary_prime':47,'precision':4,'modulus':47**4,
          'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in zip(names,raw)},
          'operators':{},'canonical_cyclic_matrix':cyclic,'primitive_polynomial_descending':poly,
          'status':'actual GP operations and full image/descent/spectrum checks; independent verification pending'}
    for ell,permutation,targets,T,TK in records:
        data['operators'][str(ell)]={'necklace_transport_1based':permutation,'weight2_operator':T,'canonical_operator':TK,
             'targets':[{'kernel_x':x,'A':A,'B':B,'P':P,'Q':Q,'evaluation_matrix':W} for x,A,B,P,Q,W in targets]}
    out=args.output or Path('/tmp/p41_hecke47_checkpoint.json.gz')
    encoded=(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode()
    packed=gzip.compress(encoded,mtime=0)
    assert len(packed)<5_000_000
    out.write_bytes(packed)
    print('Saved raw',len(packed),'bytes; SHA256',hashlib.sha256(packed).hexdigest(),flush=True)
    write_compact(data,hashlib.sha256(packed).hexdigest(),compact_out)


if __name__=='__main__':
    main()
