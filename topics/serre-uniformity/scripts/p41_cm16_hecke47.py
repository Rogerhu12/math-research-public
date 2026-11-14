#!/usr/bin/env python3
"""Actual T2 action on the full CM(-4) divisor and its20 vertical CM(-16) targets."""
import argparse,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2))%41 for j in range(2)] for i in range(2)]
def inverse(a):
    d=pow((a[0][0]*a[1][1]-a[0][1]*a[1][0])%41,-1,41)
    return [[a[1][1]*d%41,-a[0][1]*d%41],[-a[1][0]*d%41,a[0][0]*d%41]]
def act(a,necklace,allnecklaces):
    x,e=necklace;R=[[x,(e-x*x)%41],[1,-x%41]];S=mm(mm(a,R),inverse(a));u=pow(S[1][0],-1,41)
    return allnecklaces.index([S[0][0]*u%41,e*u*u%41])+1

def prepare(folder):
    names=['p41_local47_torsion_certificate.json','p41_makdisi47_certificate.json.gz',
           'p41_cm4_divisor47_certificate.json','p41_hecke47_compact.json.gz']
    raws=[(folder/'data'/n).read_bytes() for n in names]
    torsion,model,cm4,hecke=[json.loads(gzip.decompress(b) if n.endswith('.gz') else b) for n,b in zip(names,raws)]
    ew=next(a for a in torsion['curves'] if a['label']=='Makdisi_j9_fibre')['weil_pairing']
    U=cm4['CM_unit_matrix'];F=cm4['frobenius_torsion_matrix'];D=[[1,0],[0,21]];Di=inverse(D)
    negU=[[-x%41 for x in row] for row in U];Ft=mm(mm(mm(Di,negU),F),D)
    horizontal=[[(U[i][j]+int(i==j))%41 for j in range(2)] for i in range(2)]
    fixed=cm4['elliptic_necklace_indices_1based'];ns=model['necklaces']
    targets=[act(Di,ns[j-1],ns) for j in fixed]
    assert len(set(targets))==20
    assert targets==[hecke['operators']['2']['necklace_transport_1based'][j-1] for j in fixed]
    hperm=[fixed.index(act(horizontal,ns[j-1],ns))+1 for j in fixed]
    assert all(hperm[hperm[j]-1]==j+1 and hperm[j]!=j+1 for j in range(20))
    tau=[targets.index(act(Ft,ns[j-1],ns))+1 for j in targets]
    assert tau==cm4['elliptic_frobenius_permutation_1based']
    delta=7;q=47**4
    for _ in range(3):delta=(delta-(delta*delta-2)*pow(2*delta,-1,q))%q
    assert delta*delta%q==2
    inputs=[torsion['field_polynomial_ascending'],torsion['frobenius_lift'],ew,model['sqrt_minus_one_lift'],
            model['basis_pairs'],model['basis_inverse'],model['frobenius_basis_matrix'],
            model['sl2_representatives'],model['sl2_normalizer_mod_signs'],
            [a[0] for a in cm4['P_jets']],[a[0] for a in cm4['Q_jets']],U,F,fixed,targets,tau,delta]
    meta={'source_necklace_indices_1based':fixed,'target_necklace_indices_1based':targets,
          'horizontal_permutation_1based':hperm,'target_frobenius_permutation_1based':tau,
          'target_frobenius_torsion_matrix':Ft,'sqrt_two_mod47four':delta}
    return inputs,{n:hashlib.sha256(b).hexdigest() for n,b in zip(names,raws)},meta

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_cm16_hecke47_raw.json.gz'))
    args=p.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    from p41_formal47_multiply import write_checkpoint
    inputs,hashes,meta=prepare(folder)
    with tempfile.TemporaryDirectory(prefix='serre-p41-cm16-') as td:
        td=Path(td);ip=td/'input.gp';op=td/'result.json';ip.write_text('cm16_input='+json.dumps(inputs,separators=(',',':'))+';\n')
        scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp','p41_formal47_abel_jets.gp']]
        scripts.append(Path(__file__).with_suffix('.gp'))
        code='\n'.join([f'read({json.dumps(str(p))});' for p in scripts]+
                       [f'read({json.dumps(str(ip))});',f'p41_cm16_hecke47(cm16_input,{json.dumps(str(op))});','quit;'])
        proc=subprocess.Popen([args.gp,'-q','-f','-s','134217728'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        proc.stdin.write(code);proc.stdin.close();lines=[]
        for line in proc.stdout:print(line.rstrip(),flush=True);lines.append(line)
        rc=proc.wait()
        if rc or '***' in ''.join(lines) or not op.exists():raise RuntimeError('Actual CM16 Hecke calculation failed')
        rec=json.loads(op.read_text())
    keys=['P_plus','Q_plus','P_minus','Q_minus','actual_frobenius_matrix','weight2_values']
    result=dict(zip(keys,rec));assert result['actual_frobenius_matrix']==meta['target_frobenius_torsion_matrix']
    result.update(meta);result.update({'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
      'curve_A':-11,'curve_B':-14,'j_invariant':287496,
      'generating_source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_suffix('.gp')]},
      'status':'actual horizontal1+i and both vertical2-isogenies; calibrated20 CM16 targets and all73 values PASS; independent verification pending'})
    sha,size=write_checkpoint(args.output,result);print('ACTUAL CM16 HECKE SAVED',size,sha,flush=True)

if __name__=='__main__':main()

