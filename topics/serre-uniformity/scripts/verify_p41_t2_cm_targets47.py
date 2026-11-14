#!/usr/bin/env python3
"""Independent actual T2 CM target values and the dual ascending branch."""
import argparse,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--input',type=Path,default=Path('/tmp/p41_t2_cm_targets47_raw.json.gz'))
    parser.add_argument('--cm12',type=Path,default=Path('/tmp/p41_cm12_hecke47_verified.json.gz'))
    parser.add_argument('--cm7',type=Path,default=Path('/tmp/p41_cm7_q2_support47_verified.json.gz'))
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_t2_cm_targets47_verified.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    from p41_t2_cm_targets47 import prepare
    from p41_formal47_multiply import write_checkpoint
    raw=args.input.read_bytes();cert=json.loads(gzip.decompress(raw))
    inputs,hashes,cases=prepare(folder,args.cm12,args.cm7);assert hashes==cert['source_sha256'] and cases==cert['cases']
    cm3raw=(folder/'data/p41_cm3_makdisi47_certificate.json').read_bytes();cm3=json.loads(cm3raw)
    inputs.append([[a[0] for a in cm3['P_jets']],[a[0] for a in cm3['Q_jets']]])
    keys=['label','curve_A','curve_B','j_mod47four','necklace_index_1based','P','Q','weight2_values','frobenius_torsion_matrix']
    records=[[rec[k] for k in keys] for rec in cert['records']]
    with tempfile.TemporaryDirectory(prefix='serre-p41-t2-cm-targets-verify-') as work:
        work=Path(work);ip=work/'input.gp';op=work/'result.json'
        ip.write_text('t2cm_input='+json.dumps(inputs,separators=(',',':'))+';\nt2cm_cert='+json.dumps(records,separators=(',',':'))+';\n')
        scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp']]
        scripts.append(Path(__file__).with_suffix('.gp'))
        code='\n'.join([f'read({json.dumps(str(p))});' for p in scripts]+[f'read({json.dumps(str(ip))});',f'p41v_t2_cm_targets47(t2cm_input,t2cm_cert,{json.dumps(str(op))});','quit;'])
        proc=subprocess.Popen([args.gp,'-q','-f','-s','134217728'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        proc.stdin.write(code);proc.stdin.close();messages=[]
        for line in proc.stdout:print(line.rstrip(),flush=True);messages.append(line)
        rc=proc.wait()
        if rc or '***' in ''.join(messages) or not op.exists():raise RuntimeError(f'Independent T2 CM targets failed (return code {rc})')
    q=47**4;j0,j1,j2=[rec['j_mod47four'] for rec in cert['records']]
    assert (j0+j1-2835810000)%q==0 and (j0*j1-6549518250000)%q==0 and j2==16581375%q
    result=dict(cert);result.update({'raw_source_sha256':hashlib.sha256(raw).hexdigest(),
        'CM3_dual_source_sha256':hashlib.sha256(cm3raw).hexdigest(),
        'target_j_polynomials_ascending':{'CM48':[6549518250000,-2835810000,1],'CM28':[-16581375,1]},
        'verification_source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_suffix('.gp')]},
        'status':'independent group-law Velu and all3x73 direct trace values PASS; ascending CM12 branch checked as the actual dual returning CM3; both complete T2 image divisors identified'})
    digest,size=write_checkpoint(args.output,result);print('INDEPENDENT ACTUAL T2 CM TARGETS ALL PASS',size,digest,flush=True)
if __name__=='__main__':main()

