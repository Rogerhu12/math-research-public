#!/usr/bin/env python3
"""Independent actual CM(-12) jets and exact integral local correspondence equation."""
import argparse,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path

def add(a,b):
    n=max(len(a),len(b));out=[0]*n
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def power(a,n):
    out=[1]
    for _ in range(n):out=mul(out,a)
    return out

def local_equation():
    # j1=6912(u+1)^3/((u+4)(2u-1)^2),
    # j2=432(11u-4)^3/((u+4)^2(2u-1)).
    n1=[6912*x for x in power([1,1],3)];d1=mul([4,1],power([-1,2],2))
    n2=[432*x for x in power([-4,11],3)];d2=mul(power([4,1],2),[-1,2])
    phi={(3,0):1,(0,3):1,(2,2):-1,(2,1):1488,(1,2):1488,(2,0):-162000,(0,2):-162000,
         (1,1):40773375,(1,0):8748000000,(0,1):8748000000,(0,0):-157464000000000}
    numerator=[0]
    for (i,j),c in phi.items():
        term=mul(mul(power(n1,i),power(d1,3-i)),mul(power(n2,j),power(d2,3-j)))
        numerator=add(numerator,[c*x for x in term])
    assert numerator==[0]
    b=54000
    assert [c for c in power([-b,1],3)]==[-157464000000000,8748000000,-162000,1]
    derivative=1488*b*b+40773375*b+8748000000
    assert derivative==6549518250000==118800**3//256 and derivative%47==31
    return {'Phi2_terms':[[i,j,c] for (i,j),c in sorted(phi.items())],
            'normalization_parameter':'u=r^3; r^3+A*r+1=0, r(0)=-1',
            'source_j_numerator_ascending':n1,'source_j_denominator_ascending':d1,
            'target_j_numerator_ascending':n2,'target_j_denominator_ascending':d2,
            'Phi2_substitution_numerator':[0],'Phi2_dx_at_CM_pair':derivative,'Phi2_dx_mod47':31,
            'target_j_derivative_at_A0':-118800,'source_fibre_multiplicity_at_target':3,
            'reverse_fibre_multiplicity_at_source':1,'source_j_leading_in_target_j_minus54000':[-1,derivative]}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
    parser.add_argument('--input',type=Path,default=Path('/tmp/p41_cm12_hecke47_certificate.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_cm12_hecke47_verified.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    from p41_formal47_multiply import write_checkpoint
    raw=args.input.read_bytes();cert=json.loads(gzip.decompress(raw))
    names=['p41_local47_torsion_certificate.json','p41_makdisi47_certificate.json.gz','p41_cm3_makdisi47_certificate.json','p41_hecke47_compact.json.gz']
    raws=[(folder/'data'/n).read_bytes() for n in names]
    assert cert['source_sha256']=={n:hashlib.sha256(b).hexdigest() for n,b in zip(names,raws)}
    torsion,model,cm3,hecke=[json.loads(gzip.decompress(b) if n.endswith('.gz') else b) for n,b in zip(names,raws)]
    ew=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')['weil_pairing']
    # Explicit conjugation by diag(1,21), independent of searching the transport table.
    a,e=cm3['CM_necklace'];aa=21*a%41;ee=21**2*e%41
    target=model['necklaces'].index([aa,ee])+1
    assert target==cert['target_CM_necklace_index_1based']==198 and [aa,ee]==[9,34]
    inputs=[torsion['field_polynomial_ascending'],torsion['frobenius_lift'],ew,model['sqrt_minus_one_lift'],
            cm3['P_jets'],cm3['Q_jets'],model['basis_pairs'],model['basis_inverse'],model['frobenius_basis_matrix'],
            model['sl2_representatives'][target-1],cm3['frobenius_torsion_matrix']]
    fields=['weight2_evaluation_coefficients','target_P_jets','target_Q_jets','kernel_x_coefficients','target_A_coefficients','target_B_coefficients']
    vals=[cert[k] for k in fields]
    with tempfile.TemporaryDirectory(prefix='serre-p41-cm12-verify-') as work:
        work=Path(work);ip=work/'input.gp';op=work/'result.json'
        ip.write_text('cm12_input='+json.dumps(inputs,separators=(',',':'))+';\ncm12_cert='+json.dumps(vals,separators=(',',':'))+';\n')
        scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp']]
        scripts.append(Path(__file__).with_suffix('.gp'))
        code='\n'.join([f'read({json.dumps(str(p))});' for p in scripts]+[f'read({json.dumps(str(ip))});',f'p41_verify_cm12_hecke47(cm12_input,cm12_cert,{json.dumps(str(op))});','quit;'])
        run=subprocess.run([args.gp,'-q','-f','-s','268435456'],input=code,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        print(run.stdout,flush=True)
        if run.returncode or '***' in run.stdout or not op.exists():raise RuntimeError('Independent actual CM12 verification failed')
    result=dict(cert);result['unverified_raw_sha256']=hashlib.sha256(raw).hexdigest();result['exact_local_equation']=local_equation()
    result['verification_source_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_suffix('.gp')]}
    result['status']='independent group-law Velu, all73 actual jets, explicit Cartan transport and exact integral Phi2 normalization identity PASS; local T2 branch has source index3 and target index1'
    digest,size=write_checkpoint(args.output,result)
    print('ACTUAL CM12 LOCAL CORRESPONDENCE ALL PASS',size,digest,flush=True)

if __name__=='__main__':main()
