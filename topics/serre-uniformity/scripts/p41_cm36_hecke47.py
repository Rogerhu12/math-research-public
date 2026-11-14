#!/usr/bin/env python3
"""Actual T3 image of CM(-4): two20-point CM(-36) branches, with all73 values.

Each of the two GP branches is saved separately before the next one starts.
The four actual cyclic kernels, Weil normalization and Frobenius are checked;
the output is data for the actual correspondence, not a height calculation.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2))%41 for j in range(2)] for i in range(2)]


def inverse(a):
    d=pow((a[0][0]*a[1][1]-a[0][1]*a[1][0])%41,-1,41)
    return [[a[1][1]*d%41,-a[0][1]*d%41],[-a[1][0]*d%41,a[0][0]*d%41]]


def act(a,necklace,allnecklaces):
    x,e=necklace
    R=[[x,(e-x*x)%41],[1,-x%41]]
    S=mm(mm(a,R),inverse(a));v=pow(S[1][0],-1,41)
    return allnecklaces.index([S[0][0]*v%41,e*v*v%41])+1


def root_lift(value,residue,q=47**4):
    z=residue
    assert (z*z-value)%47==0
    for _ in range(3):
        z=(z-(z*z-value)*pow(2*z,-1,q))%q
    assert z*z%q==value%q
    return z


def save(path,payload):
    raw=gzip.compress((json.dumps(payload,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0)
    tmp=path.with_suffix(path.suffix+'.new');tmp.write_bytes(raw);tmp.replace(path)
    return len(raw),hashlib.sha256(raw).hexdigest()


def prepare(folder):
    names=['p41_local47_torsion_certificate.json','p41_makdisi47_certificate.json.gz',
           'p41_cm4_divisor47_certificate.json','p41_hecke47_compact.json.gz']
    raw=[(folder/'data'/n).read_bytes() for n in names]
    torsion,model,cm4,hecke=[json.loads(gzip.decompress(b) if n.endswith('.gz') else b)
                           for n,b in zip(names,raw)]
    ew=next(a for a in torsion['curves'] if a['label']=='Makdisi_j9_fibre')['weil_pairing']
    U=cm4['CM_unit_matrix'];F=cm4['frobenius_torsion_matrix']
    D=[[1,0],[0,14]];Di=inverse(D);negative_U=[[-x%41 for x in row] for row in U]
    Ft=[mm(mm(Di,F),D),mm(mm(mm(Di,negative_U),F),D)]
    fixed=cm4['elliptic_necklace_indices_1based'];necklaces=model['necklaces']
    targets=[act(Di,necklaces[j-1],necklaces) for j in fixed]
    assert len(set(targets))==20
    assert targets==[hecke['operators']['3']['necklace_transport_1based'][j-1] for j in fixed]
    permutations=[[targets.index(act(A,necklaces[j-1],necklaces))+1 for j in targets] for A in Ft]
    assert all(tau==cm4['elliptic_frobenius_permutation_1based'] for tau in permutations)
    q=47**4;sqrt2=root_lift(2,7);sqrt3=root_lift(3,12)
    a=root_lift((-1+2*sqrt3*pow(3,-1,q))%q,17)
    b=root_lift((1+2*sqrt3*pow(3,-1,q))%q,3)
    assert a*b*sqrt3%q==1
    A=[(-9-30*a*a)%q,(9-30*b*b)%q]
    B=[(-70*a*a*a-42*a)%q,(-70*b*b*b+42*b)%q]
    j=[1728*4*x**3*pow(4*x**3+27*y*y,-1,q)%q for x,y in zip(A,B)]
    assert j==[(76771008-44330496*sqrt3)%q,(76771008+44330496*sqrt3)%q]
    assert [x%47 for x in j]==[9,10]
    for x in j:assert (x*x-153542016*x-1790957481984)%q==0
    inputs=[torsion['field_polynomial_ascending'],torsion['frobenius_lift'],ew,
            model['sqrt_minus_one_lift'],model['basis_pairs'],model['basis_inverse'],
            model['frobenius_basis_matrix'],model['sl2_representatives'],model['sl2_normalizer_mod_signs'],
            [a[0] for a in cm4['P_jets']],[a[0] for a in cm4['Q_jets']],U,F,fixed,targets,
            permutations[0],permutations[1],sqrt2,sqrt3,a,b]
    meta={'source_necklace_indices_1based':fixed,'target_necklace_indices_1based':targets,
          'target_frobenius_permutations_1based':permutations,
          'target_frobenius_torsion_matrices':Ft,'sqrt_two_mod47four':sqrt2,
          'sqrt_three_mod47four':sqrt3,'kernel_real_root_a':a,'kernel_imaginary_factor_b':b,
          'actual_curve_A':A,'actual_curve_B':B,'actual_j_invariants':j,
          'hilbert_polynomial_ascending':[-1790957481984,-153542016,1],
          'Weil_basis_adjustment':D,'branch_multiplicities':[2,2]}
    return inputs,{n:hashlib.sha256(b).hexdigest() for n,b in zip(names,raw)},meta


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    parser.add_argument('--branch',type=int,choices=[0,1])
    parser.add_argument('--branch-prefix',type=Path,default=Path('/tmp/p41_cm36_hecke47_branch'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_cm36_hecke47_raw.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve()
    inputs,hashes,meta=prepare(folder)
    sourcehash={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                for p in [Path(__file__),Path(__file__).with_suffix('.gp')]}
    branches=[args.branch] if args.branch is not None else [0,1]
    for branch in branches:
        output=Path(str(args.branch_prefix)+str(branch)+'.json.gz')
        if output.exists():
            existing=json.loads(gzip.decompress(output.read_bytes()))
            assert existing['source_sha256']==hashes and existing['generating_source_sha256']==sourcehash
            assert existing['branch']==branch
            print('ACTUAL CM36 REUSE COMPLETE BRANCH',branch,flush=True)
            continue
        with tempfile.TemporaryDirectory(prefix='serre-p41-cm36-') as td:
            td=Path(td);ip=td/'input.gp';op=td/'result.json'
            ip.write_text('cm36_input='+json.dumps(inputs,separators=(',',':'))+';\n')
            scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp',
                                        'p41_cm3_makdisi47.gp','p41_formal47_abel_jets.gp']]
            scripts.append(Path(__file__).with_suffix('.gp'))
            code='\n'.join([f'read({json.dumps(str(p))});' for p in scripts]+
                            [f'read({json.dumps(str(ip))});',
                             f'p41_cm36_hecke47(cm36_input,{branch+1},{json.dumps(str(op))});','quit;'])
            proc=subprocess.Popen([args.gp,'-q','-f','-s','134217728'],stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            proc.stdin.write(code);proc.stdin.close();lines=[]
            for line in proc.stdout:
                print(line.rstrip(),flush=True);lines.append(line)
            rc=proc.wait()
            if rc or '***' in ''.join(lines) or not op.exists():
                raise RuntimeError('Actual CM36 Hecke branch failed: '+str(branch))
            record=json.loads(op.read_text())
        keys=['curve_A_extension','curve_B_extension','j_invariant_extension','P_plus','Q_plus',
              'P_minus','Q_minus','actual_frobenius_matrix','weight2_values']
        result=dict(zip(keys,record));assert len(record)==len(keys)
        assert result['actual_frobenius_matrix']==meta['target_frobenius_torsion_matrices'][branch]
        for key,expected in [('curve_A_extension',meta['actual_curve_A'][branch]),
                             ('curve_B_extension',meta['actual_curve_B'][branch]),
                             ('j_invariant_extension',meta['actual_j_invariants'][branch])]:
            assert result[key][0]==expected and not any(result[key][1:])
        assert len(result['weight2_values'])==20 and all(len(row)==73 for row in result['weight2_values'])
        result.update({'level':41,'auxiliary_prime':47,'precision':4,'branch':branch,
                       'source_sha256':hashes,'generating_source_sha256':sourcehash,
                       'source_necklace_indices_1based':meta['source_necklace_indices_1based'],
                       'target_necklace_indices_1based':meta['target_necklace_indices_1based'],
                       'target_frobenius_permutation_1based':meta['target_frobenius_permutations_1based'][branch],
                       'curve_A':meta['actual_curve_A'][branch],'curve_B':meta['actual_curve_B'][branch],
                       'j_invariant':meta['actual_j_invariants'][branch],
                       'status':'actual two cyclic3-isogenies, calibrated20 CM36 targets, all73 values and full Frobenius PASS; no height claimed'})
        size,sha=save(output,result)
        print('ACTUAL CM36 BRANCH SAVED',branch,size,sha,flush=True)
    if args.branch is not None:return
    records=[];branchhashes={}
    for branch in range(2):
        path=Path(str(args.branch_prefix)+str(branch)+'.json.gz');raw=path.read_bytes()
        records.append(json.loads(gzip.decompress(raw)));branchhashes[str(branch)]=hashlib.sha256(raw).hexdigest()
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
            'generating_source_sha256':sourcehash,'branch_sha256':branchhashes,
            'records':records,'exact_divisor_identity':'T3(Z_minus4)=2*Z_minus36; degree80=2*40',
            'status':'all4 actual cyclic3-isogenies, two20-point CM36 branches and all73 model values PASS; no Jacobian transport or height claimed'}
    result.update(meta);size,sha=save(args.output,result)
    print('ACTUAL COMPLETE CM36 HECKE SAVED',size,sha,flush=True)


if __name__=='__main__':main()
