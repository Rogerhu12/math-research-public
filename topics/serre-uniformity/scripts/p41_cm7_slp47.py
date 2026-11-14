#!/usr/bin/env python3
"""CM7 SLP in a faithful evaluation chart excluding the initial residual support."""
import argparse,gzip,hashlib,json,random,resource,sys,time
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--initial',type=Path);p.add_argument('--checkpoint',type=Path,default=Path('/tmp/p41_cm7_slp47_rolling.json.gz'))
    p.add_argument('--max-bits',type=int,default=304);args=p.parse_args()
    folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model,flip
    from p41_poincare_miller47 import addflip_with_section
    from p41_formal47_multiply import write_checkpoint,restore_tuple,point_hash,zero_test_mod47
    begin=time.monotonic();sources,hashes=load_sources(folder/'data');M0=make_model(sources)
    initial_path=args.initial or folder/'data/p41_cm_based_points47_checkpoint.json.gz'
    raw=initial_path.read_bytes();initial=json.loads(gzip.decompress(raw));assert initial['source_sha256']==hashes
    point=next(a for a in initial['records'] if a['point_label']=='P_minus7')
    Cold,AC=r.from_json(point['point_coordinates']),r.from_json(point['point_frobenius'])
    assert point_hash(Cold,AC)==point['point_sha256']
    val=r.mm(M0['V2'],Cold)
    keep=[i for i in range(820) if np.any(r.units(r.rows(val,[i])))]
    omitted=[i for i in range(820) if i not in set(keep)]
    assert omitted and len(keep)>630
    assert all(M0['tau'][i] in set(omitted) for i in omitted)
    relabel={j:i for i,j in enumerate(keep)}
    M=dict(M0);M['W']=r.rows(M0['W'],keep);M['tau']=[relabel[M0['tau'][i]] for i in keep]
    M['V2'],M['P2'],cols2,C2=r.normalize(r.rows(M0['V2'],keep),199);assert cols2==list(range(199))
    M['V3'],M['P3'],cols3,C3=r.normalize(r.rows(M0['V3'],keep),325);assert cols3==list(range(325))
    C2i=r.inverse_matrix(C2);C3i=r.inverse_matrix(C3)
    M['A2']=r.mm(r.mm(C2i,M0['A2']),r.conjugate(C2));M['A3']=r.mm(r.mm(C3i,M0['A3']),r.conjugate(C3))
    for V,A in [(M['W'],M['A1']),(M['V2'],M['A2']),(M['V3'],M['A3'])]:
        assert r.equal(r.mm(V,A),r.conjugate(r.rows(V,M['tau'])))
    C=r.mm(C2i,Cold)
    assert r.equal(r.mm(M['A2'],r.conjugate(C)),r.mm(C,AC))
    original=lambda K:r.mm(C2,K)
    original_hash=lambda K,A:point_hash(original(K),A)
    enc=lambda A:hashlib.sha256(json.dumps(r.to_json(A),separators=(',',':')).encode()).hexdigest()
    chart={'omitted_evaluation_rows_1based':[i+1 for i in omitted],'remaining_rows':len(keep),
           'maximum_section_degree_in_group_operations':630,'V2_change_sha256':enc(C2),'V3_change_sha256':enc(C3),
           'stored_point_and_section_basis':'all checkpoint point coordinates and principal sections are converted back to the original R102/R110 bases'}
    print('ACTUAL CM7 FAITHFUL CHART',chart,flush=True)
    pub=json.loads(gzip.decompress((folder/'data/p41_formal47_multiplication_saved.json.gz').read_bytes()))
    assert pub['source_sha256']==hashes;m=pub['target_multiplier'];bits=bin(m)[2:];assert len(bits)==304 and m%47==9
    rng=random.Random(4104716607);source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.checkpoint.exists():
        data=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
        assert data['source_sha256']==hashes and data['initial_source_sha256']==hashlib.sha256(raw).hexdigest()
        assert data['initial_point_sha256']==point['point_sha256'] and data['generating_source_sha256']==source_sha
        assert data['working_chart']==chart and data['target_multiplier']==m
        oldK,A=r.from_json(data['point_coordinates']),r.from_json(data['point_frobenius'])
        oldneg,Aneg=r.from_json(data['negative_point_coordinates']),r.from_json(data['negative_point_frobenius'])
        assert point_hash(oldK,A)==data['point_sha256'] and point_hash(oldneg,Aneg)==data['negative_point_sha256']
        K,neg=r.mm(C2i,oldK),r.mm(C2i,oldneg);rng.setstate(restore_tuple(data['random_state']))
        print('ACTUAL CM7 SLP RESUME',data['bits_done'],'bits',len(data['steps']),'steps',flush=True)
    else:
        neg,Aneg,neg_record=flip(r.mm(M['V2'],C),AC,M,rng,'P_minus7 actual negative in faithful chart')
        qnegative=r.mm(Cold,r.column(neg_record['f_coefficients']))
        assert r.equal(r.mm(M0['A2'],r.conjugate(qnegative)),qnegative)
        K,A=C,AC
        data={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'point_label':'P_minus7',
              'initial_source_sha256':hashlib.sha256(raw).hexdigest(),'initial_point_sha256':point['point_sha256'],
              'generating_source_sha256':source_sha,'working_chart':chart,'target_multiplier':m,
              'bits_done':1,'magnitude':1,'sign':1,'steps':[],
              'initial_principal_transport_coefficients':initial['f_b_coefficients'],
              'initial_principal_transport':'h=f_b/f0; A_initial=P7-b+div(h); retain collision frames',
              'local_factor_convention':'F_n=V_n*W_initial^n/W_current; initial P7 factor=t',
              'negative_point_coordinates':r.to_json(original(neg)),'negative_point_frobenius':r.to_json(Aneg),
              'negative_point_sha256':original_hash(neg,Aneg),'negative_quadratic_coefficients':r.to_json(qnegative),
              'negative_principal_function':'qnegative/f0^2 has divisor A_initial+A_negative; F_minus1 is its inverse',
              'negative_flip_record_in_working_chart':neg_record,
              'point_coordinates':r.to_json(original(K)),'point_frobenius':r.to_json(A),'point_sha256':original_hash(K,A),
              'random_state':rng.getstate(),'status':'actual CM7 SLP in progress in819-point faithful chart; no height claimed'}
        sha,size=write_checkpoint(args.checkpoint,data)
        print('ACTUAL CM7 INITIAL SAVED',size,sha,'setup seconds',round(time.monotonic()-begin,2),flush=True)
    start=time.monotonic();start_steps=len(data['steps'])
    def record_step(record,section,operation,bit):
        encoded=r.to_json(r.mm(C3,section));working_hash=record['point_sha256']
        record.update({'operation':operation,'bit':bit,'sign':data['sign'],
                       'working_point_sha256':working_hash,'point_sha256':original_hash(K,A),
                       'principal_section_coefficients':encoded,
                       'principal_coefficient_sha256':hashlib.sha256(json.dumps(encoded,separators=(',',':')).encode()).hexdigest()})
        data['steps'].append(record)
    for n in range(data['bits_done'],min(len(bits),args.max_bits)):
        K,A,f,rec=addflip_with_section(K,A,K,A,M,rng,'P_minus7 double bit'+str(n+1),r,same=True)
        data['sign']*=-1;data['magnitude']*=2;record_step(rec,f,'double',n+1)
        if bits[n]=='1':
            Q,AQ=(C,AC) if data['sign']==1 else (neg,Aneg)
            K,A,f,rec=addflip_with_section(K,A,Q,AQ,M,rng,'P_minus7 add bit'+str(n+1),r)
            data['sign']*=-1;data['magnitude']+=1;record_step(rec,f,'add',n+1)
        data['bits_done']=n+1;assert data['magnitude']==int(bits[:n+1],2)
        data['point_coordinates'],data['point_frobenius']=r.to_json(original(K)),r.to_json(A)
        data['point_sha256']=original_hash(K,A);data['random_state']=rng.getstate()
        if (n+1)%5==0 or n+1==min(len(bits),args.max_bits):
            sha,size=write_checkpoint(args.checkpoint,data)
            print('ACTUAL CM7 SLP CHECKPOINT',n+1,'bits',len(data['steps']),'steps','bytes',size,
                  'seconds',round(time.monotonic()-start,2),'newsteps',len(data['steps'])-start_steps,
                  'peak_MiB',round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,1),'sha',sha,flush=True)
    if data['bits_done']==304:
        assert data['sign']==1 and data['magnitude']==m
        data['zero_test_mod47_in_working_chart']=zero_test_mod47(K,M)
        data['status']='complete actual CM7 signed304-bit SLP, all stored in original bases; full zero reduction PASS; formal endpoint comparison and heights remain subsequent calculations'
        sha,size=write_checkpoint(args.checkpoint,data);print('ACTUAL CM7 SLP COMPLETE',size,sha,flush=True)

if __name__=='__main__':main()

