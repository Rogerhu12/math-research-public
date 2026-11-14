#!/usr/bin/env python3
"""Verify the same-frame double inverse and evaluate its actual Hecke-compatible log.

All norm verifications use the independent integral-resultant implementation.
The fibre is (Y,Y); this is a local Poincare fibre value, not a global self-height.
"""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--bases',type=Path,default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    parser.add_argument('--exponential',type=Path,default=Path('/tmp/p41_hecke3_exponential_checkpoint.json.gz'))
    parser.add_argument('--principal',type=Path,default=Path('/tmp/p41_hecke3_poincare_principal.json.gz'))
    parser.add_argument('--input',type=Path,default=Path('/tmp/p41_hecke3_poincare_checkpoint.json.gz'))
    parser.add_argument('--hessian',type=Path,default=Path('/tmp/p41_hecke3_hessian47_compact.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_hecke3_formal_height47_compact.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_formal47_multiply import write_checkpoint
    from verify_p41_poincare_algebras47 import polynomial_norm,mul,inv,sub
    from verify_p41_poincare_formal47 import verify_principal,verify_algebra
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    paths=[args.bases,args.exponential,args.principal,args.input,args.hessian]
    raws=[p.read_bytes() for p in paths];base,exp,pr,data,hessian=[json.loads(gzip.decompress(raw)) for raw in raws]
    assert all(a['source_sha256']==hashes for a in [base,exp,pr,data,hessian])
    assert exp['bases_sha256']==hashlib.sha256(raws[0]).hexdigest()
    assert pr['input_sha256'][args.bases.name]==hashlib.sha256(raws[0]).hexdigest()
    assert pr['input_sha256'][args.exponential.name]==hashlib.sha256(raws[1]).hexdigest()
    assert data['principal_sha256']==hashlib.sha256(raws[2]).hexdigest()
    assert base['hessian_sha256']==exp['hessian_sha256']==hessian['raw_hessian_sha256']
    assert [a['points_1based'] for a in base['families']]==[a['points_1based'] for a in hessian['families']]
    vs=[r.mm(M['W'],r.from_json(rec['v_coefficients'])) for rec in base['families']]
    plus=[r.from_json(item['point_coordinates']) for item in exp['exponentials']]
    minus=[r.from_json(item['point_coordinates']) for item in pr['negative_exponentials']]
    coeffs=[]
    for j in range(2):
        coeffs.append(verify_principal(plus[j],minus[j],vs[j],vs[1-j],pr['inverse_functions'][j],M,r))
        assert exp['exponentials'][j]['full_PicChart_comparison'] is True
        print('Same-frame inverse family',j+1,'independent full199 product containment, descent and normalization PASS.',flush=True)
    D=[r.rows(r.mul(v,M['W']),M['P2']) for v in vs]
    cases=[('E2_plus',plus[1],coeffs[0]),('D2',D[1],coeffs[0]),('E1_minus',minus[0],coeffs[1]),('D1',D[0],coeffs[1])]
    compact={};norms={}
    for label,K,coeff in cases:
        rec=data['algebras'][label];Phi2=verify_algebra(label,K,rec['restriction'],rec['algebra'],M,r)
        value=r.mm(Phi2,coeff);poly=[[int(value[0][j,0]),int(value[1][j,0])] for j in range(126)]
        assert poly==rec['numerator_residue_polynomial']
        relation=rec['algebra']['minimal_polynomial_ascending'];norm=polynomial_norm(relation,poly)
        assert list(norm)==data['norms'][label];norms[label]=norm
        compact[label]={'minimal_polynomial_ascending':relation,'numerator_residue_polynomial':poly,'norm':list(norm)}
        print(label,'independent integer-resultant norm',norm,'PASS.',flush=True)
    first=mul(norms['E2_plus'],inv(norms['D2']));second=mul(norms['E1_minus'],inv(norms['D1']))
    delta=mul(first,inv(second));assert list(delta)==data['double_inverse_unit']
    ld=sub(delta,(1,0));assert ld[1]==0 and ld[0]%47**3==0 and ld[0]==data['log_double_inverse_unit']
    half=ld[0]*pow(2,-1,r.Q)%r.Q;assert half==data['odd_total_degree_three_term']
    lograw=(folder/'data/p41_formal47_log_compact.json.gz').read_bytes();log=json.loads(gzip.decompress(lograw))
    z=r.from_json(log['log_of_signed_multiple']);assert exp['log_sha256']==hashlib.sha256(lograw).hexdigest()
    assert all(a%47==0 for A in z for row in A for a in row)
    B=r.from_json(hessian['hecke_correction_matrix']);zt=z[0].T,z[1].T
    correction=r.mm(r.mm(z,B),zt);assert correction[1][0,0]==0
    corr=int(correction[0][0,0]);assert corr%47**2==0
    value=(half+corr)%r.Q
    families=[]
    for a,b in zip(base['families'],exp['exponentials']):
        families.append({'points_1based':a['points_1based'],'base_section_coefficients':a['v_coefficients'],
                         'actual_parameters':b['parameters'],'full_PicChart_comparison':True})
    names=['p41_source_cubic47.gp','p41_source_cubic47.py','p41_hecke3_frame47.py','verify_p41_hecke3_formal_height47.py']
    out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
         'input_sha256':{p.name:hashlib.sha256(raw).hexdigest() for p,raw in zip(paths,raws)},
         'formal_log_sha256':hashlib.sha256(lograw).hexdigest(),
         'generating_source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in names},
         'families':families,'principal_numerators':[rec['numerator_coefficients'] for rec in pr['inverse_functions']],
         'normalization_points_1based':[rec['normalization_point_1based'] for rec in pr['inverse_functions']],
         'restriction_algebras':compact,'first_inverse_degree_zero_norm':list(first),
         'second_inverse_degree_zero_norm':list(second),'double_inverse_unit':list(delta),
         'log_double_inverse_unit':ld[0],'half_log_double_inverse':half,
         'actual_hecke_bilinear_correction':corr,'actual_hecke_local_log_of_same_frame':value,
         'fibre':'P_(Y,Y), Y=m B_minus4; element is the rational1 section of the specified new Abel norm frame',
         'status':'same frame as canonical T3 Hessian; independent actual principal functions and four integer norm verifications PASS; actual Hecke-compatible local Poincare log modulo47^4; not a global self-height or a QC section value'}
    digest,size=write_checkpoint(args.output,out)
    print('SAME-FRAME ACTUAL HECKE LOCAL LOG',{'delta':delta,'half_log':half,'correction':corr,'height':value},flush=True)
    print('Compact actual local log certificate',size,digest,flush=True)

if __name__=='__main__':main()
