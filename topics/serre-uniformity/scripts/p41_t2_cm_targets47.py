#!/usr/bin/env python3
"""Actual nonself T2 images of P_minus12 and P_minus7 in the fixed level41 model."""
import argparse,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

def prepare(folder,cm12_path,cm7_path):
    names=['p41_local47_torsion_certificate.json','p41_makdisi47_certificate.json.gz','p41_hecke47_compact.json.gz']
    paths=[folder/'data'/n for n in names]+[cm12_path,cm7_path]
    raws=[p.read_bytes() for p in paths]
    torsion,model,hecke,cm12,cm7=[json.loads(gzip.decompress(b) if p.name.endswith('.gz') else b) for p,b in zip(paths,raws)]
    assert 'independent' in cm12['status'] and 'independent' in cm7['status']
    ew=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')['weil_pairing']
    q=47**4;s=12
    for _ in range(3):s=(s-(s*s-3)*pow(2*s,-1,q))%q
    assert s*s%q==3
    cases=[]
    for label,root in [('CM48_plus',(-1+2*s)%q),('CM48_minus',(-1-2*s)%q)]:
        source=cm12['target_CM_necklace_index_1based'];a,e=model['necklaces'][source-1]
        target=model['necklaces'].index([21*a%41,21**2*e%41])+1
        assert target==hecke['operators']['2']['necklace_transport_1based'][source-1]
        cases.append([label,-15,22,[v[0] for v in cm12['target_P_jets']],[v[0] for v in cm12['target_Q_jets']],
                      cm12['target_frobenius_torsion_matrix'],root,target])
    source=cm7['fixed_necklace_indices_1based'][0];a,e=model['necklaces'][source-1]
    target=model['necklaces'].index([21*a%41,21**2*e%41])+1
    assert target==hecke['operators']['2']['necklace_transport_1based'][source-1]
    cases.append(['CM28',-35,-98,[v[0] for v in cm7['P_jets']],[v[0] for v in cm7['Q_jets']],
                  cm7['frobenius_torsion_matrix'],7,target])
    inputs=[torsion['field_polynomial_ascending'],torsion['frobenius_lift'],ew,model['sqrt_minus_one_lift'],
            model['basis_pairs'],model['basis_inverse'],model['frobenius_basis_matrix'],
            model['sl2_representatives'],model['sl2_normalizer_mod_signs'],cases]
    return inputs,{p.name:hashlib.sha256(b).hexdigest() for p,b in zip(paths,raws)},cases

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--cm12',type=Path,default=Path('/tmp/p41_cm12_hecke47_verified.json.gz'))
    parser.add_argument('--cm7',type=Path,default=Path('/tmp/p41_cm7_q2_support47_verified.json.gz'))
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp');parser.add_argument('--output',type=Path,default=Path('/tmp/p41_t2_cm_targets47_raw.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_formal47_multiply import write_checkpoint
    inputs,hashes,cases=prepare(folder,args.cm12,args.cm7)
    with tempfile.TemporaryDirectory(prefix='serre-p41-t2-cm-targets-') as work:
        work=Path(work);ip=work/'input.gp';op=work/'result.json';ip.write_text('t2cm_input='+json.dumps(inputs,separators=(',',':'))+';\n')
        scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp','p41_formal47_abel_jets.gp']]
        scripts.append(Path(__file__).with_suffix('.gp'))
        code='\n'.join([f'read({json.dumps(str(p))});' for p in scripts]+[f'read({json.dumps(str(ip))});',f'p41_t2_cm_targets47(t2cm_input,{json.dumps(str(op))});','quit;'])
        proc=subprocess.Popen([args.gp,'-q','-f','-s','134217728'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        proc.stdin.write(code);proc.stdin.close();messages=[]
        for line in proc.stdout:print(line.rstrip(),flush=True);messages.append(line)
        rc=proc.wait()
        if rc or '***' in ''.join(messages) or not op.exists():raise RuntimeError(f'Actual T2 CM targets failed (return code {rc})')
        records=json.loads(op.read_text())
    keys=['label','curve_A','curve_B','j_mod47four','necklace_index_1based','P','Q','weight2_values','frobenius_torsion_matrix']
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'cases':cases,
            'records':[dict(zip(keys,rec)) for rec in records],
            'generating_source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_suffix('.gp')]},
            'status':'three actual T2 nonself CM targets, complete calibrated torsion and all73 values PASS; independent verification pending'}
    for rec in result['records']:
        values=r.from_json(rec['weight2_values']);assert any(r.units(values)[0])
        rec['unit_coordinate_1based']=next(j+1 for j in range(73) if r.units(values)[0,j])
    digest,size=write_checkpoint(args.output,result);print('ACTUAL T2 CM TARGETS SAVED',size,digest,flush=True)
if __name__=='__main__':main()

