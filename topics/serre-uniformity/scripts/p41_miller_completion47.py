#!/usr/bin/env python3
"""Compact completed B Miller fibre and exact CM/canonical norm certificate."""
import argparse,gzip,hashlib,json
from pathlib import Path
Q=47**4

def read(path):
    b=path.read_bytes()
    return json.loads(gzip.decompress(b) if path.suffix=='.gz' else b),hashlib.sha256(b).hexdigest()

def scalar_log(u):
    assert u%47
    z=(pow(u,46,Q)-1)%Q
    return (z-z*z*pow(2,-1,Q)+z*z*z*pow(3,-1,Q))*pow(46,-1,Q)%Q

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--script-dir',type=Path,default=Path(__file__).parent)
    p.add_argument('--miller',type=Path,default=Path('/tmp/p41_poincare_miller_jets47_complete.json.gz'))
    p.add_argument('--cm',type=Path,default=Path('/tmp/p41_miller_cm_prepared47_complete.json.gz'))
    p.add_argument('--low',type=Path,default=Path('/tmp/p41_miller_canonical_low47_complete.json.gz'))
    p.add_argument('--high',type=Path,default=Path('/tmp/p41_canonical_high_endpoint47_complete.json.gz'))
    p.add_argument('--canonical',type=Path,default=Path('/tmp/p41_canonical_restriction47_candidate1_compact.json.gz'))
    p.add_argument('--cm-jets',type=Path,default=Path('/tmp/p41_cm_quadratic_jets47_raw.json.gz'))
    p.add_argument('--endpoint',type=Path,default=Path('/tmp/p41_miller_endpoint47_certificate.json'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_miller_completion47_compact.json.gz'))
    args=p.parse_args()
    paths=[args.miller,args.cm,args.low,args.high];pairs=[read(p) for p in paths]
    full,cm,low,high=[d for d,h in pairs];inputs={p.name:h for p,(d,h) in zip(paths,pairs)}
    assert full['bits_done']==304 and full['sign']==1 and len(full['steps'])==454
    assert full['magnitude']==full['target_multiplier'] and full['target_multiplier']%47==9
    assert cm['bits_done']==low['bits_done']==304 and cm['steps_done']==low['steps_done']==454
    assert cm['input_sha256']['miller']==low['input_sha256']['miller']==inputs[args.miller.name]
    for d in [cm,low,high]:assert d['source_sha256']==full['source_sha256']
    endpoint,esha=read(args.endpoint)
    assert cm['input_sha256']['endpoint']==low['input_sha256']['endpoint']==high['input_sha256']['endpoint']==esha
    assert full['endpoint_transfer']==endpoint['transport_function']
    inputs[args.endpoint.name]=esha
    for step in full['steps']:
        raw=json.dumps(step['principal_section_coefficients'],separators=(',',':')).encode()
        assert hashlib.sha256(raw).hexdigest()==step['principal_coefficient_sha256']
    assert cm['nonunit_divisions']==low['nonunit_divisions']==0
    assert cm['maximum_residual_degree']<=4 and low['maximum_residual_degree']<=4
    scalar=full['endpoint_new_frame_coordinate'];assert scalar[1]==0
    lu=scalar_log(scalar[0]);assert lu==full['endpoint_log_coordinate']
    assert (4263370+lu)*pow(full['target_multiplier'],-1,Q)%Q==full['actual_hecke_local_log_initial_fibre']
    norms=cm['complete_actual_norms'];nlow=low['complete_actual_norms']['on_low_canonical_part']
    nhigh=high['complete_new_frame_norm_mod47four'];nk=nlow*nhigh%Q
    fb,fu,fc=[norms[k][0] for k in ['at_Pminus3','at_Pminus12','at_Pminus7']]
    assert all(norms[k][1]==0 for k in ['at_Pminus3','at_Pminus12','at_Pminus7'])
    nq=norms['on_Q2'];ntu=norms['T2_at_Pminus12'];ntc=norms['T2_at_Pminus7']
    def Dnorm(nt,fp):
        first=nt*pow(fu,3,Q)*pow(nq,-1,Q)%Q
        second=fp*fb*nk%Q
        return pow(first,27,Q)*pow(second,4,Q)%Q
    du,dc=Dnorm(ntu,fu),Dnorm(ntc,fc)
    # Re-evaluate the actual g1/f0 in the normalized fixed modular basis.
    canonical,csha=read(args.canonical);jets,jsha=read(args.cm_jets)
    assert canonical['canonical_candidate']==1 and canonical['source_sha256']==jets['source_sha256']==full['source_sha256']
    assert cm['input_sha256']['jets']==jsha
    inputs[args.canonical.name]=csha;inputs[args.cm_jets.name]=jsha
    divisor_path=args.script_dir/'data/p41_cusp_divisors47_certificate.json.gz'
    divs,dsha=read(divisor_path)
    assert full['source_sha256'][divisor_path.name]==dsha
    inputs[divisor_path.name]=dsha
    small=[row[0] for row in canonical['canonical_coefficients']]
    assert len(small)==54
    gc=[[0,0] for _ in range(73)]
    for index,value in zip(divs['cusp_free_columns_1based'],small):gc[index-1]=value
    for index,row in zip(divs['cusp_rank_columns_1based'],divs['canonical_kernel_block']):
        gc[index-1]=[sum(a*c-b*d for (a,b),(c,d) in zip(row,small))%Q,
                     sum(a*d+b*c for (a,b),(c,d) in zip(row,small))%Q]
    hvals={}
    for label,record in zip(['b','u','c7'],jets['records'][:3]):
        value=[0,0]
        for (a,b),(c,d) in zip(record['normalized_weight2_coefficients'][0],gc):
            value[0]=(value[0]+a*c-b*d)%Q;value[1]=(value[1]+a*d+b*c)%Q
        assert value[1]==0 and value[0]%47;hvals[label]=value[0]
    assert hvals=={'b':344516,'u':247689,'c7':3527523}
    globals_data={}
    for label,filename in [('u','p41_cm12_global_fibre47_certificate.json'),('c7','p41_cm7_global_fibre47_certificate.json')]:
        cert,csha=read(Path('/tmp')/filename);inputs[filename]=csha
        ratio=pow(hvals['b']*pow(hvals[label],-1,Q)%Q,4,Q)
        coordinate=cert['global_sigma_F2_coordinate']*ratio%Q
        globals_data[label]={'original_fixed_K_coordinate':cert['global_sigma_F2_coordinate'],
                            'canonical_change_ratio':ratio,'actual_g1_coordinate':coordinate,
                            'log_of_coordinate_only':scalar_log(coordinate)}
    def collision_counts(d):
        answer={}
        for step in d['steps']:
            for a in step['nonunit_points']:answer[str(a['degree'])]=answer.get(str(a['degree']),0)+1
        return answer
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':full['source_sha256'],'input_sha256':inputs,
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'target_multiplier':full['target_multiplier'],'bits':304,'steps':454,'old_point_sha256':full['point_sha256'],
            'all_principal_sections_present':True,'endpoint_transfer':full['endpoint_transfer'],
            'endpoint_new_frame_coordinate':scalar,'endpoint_log_coordinate':lu,
            'actual_hecke_local_log_initial_fibre_P_B_Y':full['actual_hecke_local_log_initial_fibre'],
            'actual_initial_fibre_Lie_gradient_mod47_cubed':full['actual_initial_fibre_Lie_gradient_mod47_cubed'],
            'endpoint_new_frame_log_norm_jets':full['endpoint_new_frame_log_norm_jets'],
            'negative_B_log_norm_jets':full['negative_B_log_norm_jets'],
            'CM_norms':norms,'canonical_low4_norm':nlow,'canonical_high102_norm':nhigh,'canonical_full106_norm':nk,
            'CM_collision_degree_counts':collision_counts(cm),'canonical_low_collision_degree_counts':collision_counts(low),
            'actual_F2_second_divisor_norms':{
                'u':{'norm':du,'log_norm':scalar_log(du),'divisor':'27(T2u+3u-Q2)+4(u+b+K_g1)'},
                'c7':{'norm':dc,'log_norm':scalar_log(dc),'divisor':'27(T2c7+3u-Q2)+4(c7+b+K_g1)'}},
            'actual_canonical_change_values':hvals,'actual_global_F2_section_coordinates_for_K_g1':globals_data,
            'status':'complete actual B Miller chain, one specified nonformal-first-variable local value,54 local derivatives, and actual26-CM+106-canonical norms; no global height or QC value claimed'}
    # Use the repository's deterministic gzip writer without loading NumPy.
    raw=json.dumps(result,separators=(',',':'),sort_keys=True).encode()
    args.output.write_bytes(gzip.compress(raw,mtime=0))
    data=args.output.read_bytes()
    print('ACTUAL B MILLER COMPLETE SUMMARY',len(data),hashlib.sha256(data).hexdigest(),flush=True)
    print(json.dumps({k:result[k] for k in ['actual_hecke_local_log_initial_fibre_P_B_Y','endpoint_new_frame_coordinate','endpoint_log_coordinate','CM_norms','canonical_full106_norm','actual_F2_second_divisor_norms','actual_global_F2_section_coordinates_for_K_g1']},indent=2),flush=True)

if __name__=='__main__':main()

