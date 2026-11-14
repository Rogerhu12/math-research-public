#!/usr/bin/env python3
"""Memory-bounded exact resumption of the published based-CM SLP and full principal functions."""
import argparse,ctypes,gc,gzip,hashlib,json,random,resource,sys,time
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--discriminant',type=int,choices=[7,12],required=True)
    parser.add_argument('--initial',type=Path)
    parser.add_argument('--checkpoint',type=Path)
    parser.add_argument('--max-bits',type=int,default=304)
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model,flip
    from p41_poincare_miller47 import addflip_with_section
    from p41_formal47_multiply import write_checkpoint,restore_tuple,point_hash,zero_test_mod47
    begin=time.monotonic();sources,hashes=load_sources(folder/'data');M=make_model(sources)
    initial_path=args.initial or folder/'data/p41_cm_based_points47_checkpoint.json.gz'
    initial_raw=initial_path.read_bytes();initial=json.loads(gzip.decompress(initial_raw));assert initial['source_sha256']==hashes
    label='P_minus'+str(args.discriminant);point=next(a for a in initial['records'] if a['point_label']==label)
    C,AC=r.from_json(point['point_coordinates']),r.from_json(point['point_frobenius'])
    assert point_hash(C,AC)==point['point_sha256']
    assert r.equal(r.mm(M['A2'],r.conjugate(C)),r.mm(C,AC)) and r.equal(r.mm(AC,r.conjugate(AC)),r.eye(73))
    published=json.loads(gzip.decompress((folder/'data/p41_formal47_multiplication_saved.json.gz').read_bytes()))
    assert published['source_sha256']==hashes
    m=published['target_multiplier'];bits=bin(m)[2:];assert len(bits)==304 and m%47==9
    checkpoint=args.checkpoint or Path('/tmp/p41_cm'+str(args.discriminant)+'_slp47_rolling.json.gz')
    rng=random.Random(4104716600+args.discriminant)
    source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if checkpoint.exists():
        data=json.loads(gzip.decompress(checkpoint.read_bytes()))
        assert data['source_sha256']==hashes and data['initial_source_sha256']==hashlib.sha256(initial_raw).hexdigest()
        assert data['initial_point_sha256']==point['point_sha256'] and data['point_label']==label and data['target_multiplier']==m
        assert data['generating_source_sha256'] in [source_sha, 'f3fb1acbc335b7560ddb00f31f1566be3a6eae06fdb69e47fbf6dc996df0348b']
        if data['generating_source_sha256'] != source_sha:
            data.setdefault('driver_history', []).append({'previous_source_sha256': data['generating_source_sha256'], 'replacement_source_sha256': source_sha, 'reason': 'lost execution session; release unused source JSON after reconstructing identical arithmetic state, RNG and principal-section basis'})
            data['generating_source_sha256'] = source_sha
        K,A=r.from_json(data['point_coordinates']),r.from_json(data['point_frobenius'])
        neg,Aneg=r.from_json(data['negative_point_coordinates']),r.from_json(data['negative_point_frobenius'])
        assert point_hash(K,A)==data['point_sha256'] and point_hash(neg,Aneg)==data['negative_point_sha256']
        rng.setstate(restore_tuple(data['random_state']))
        print('ACTUAL CM SLP RESUME',label,data['bits_done'],'bits',len(data['steps']),'steps',flush=True)
    else:
        neg,Aneg,negative_record=flip(r.mm(M['V2'],C),AC,M,rng,label+' true negative')
        negative_quadratic=r.mm(C,r.column(negative_record['f_coefficients']))
        assert r.equal(r.mm(M['A2'],r.conjugate(negative_quadratic)),negative_quadratic)
        K,A=C,AC
        data={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'point_label':label,
              'initial_source_sha256':hashlib.sha256(initial_raw).hexdigest(),'initial_point_sha256':point['point_sha256'],
              'generating_source_sha256':source_sha,'target_multiplier':m,'bits_done':1,'magnitude':1,'sign':1,'steps':[],
              'initial_principal_transport_coefficients':initial['f_b_coefficients'],
              'initial_principal_transport':'h=f_b/f0; A_initial=P-b+div(h); retain collision frames at P,b',
              'local_factor_convention':'F_n=V_n*W_initial^n/W_current; W_initial=t on the actual P disc, not1',
              'negative_point_coordinates':r.to_json(neg),'negative_point_frobenius':r.to_json(Aneg),
              'negative_point_sha256':point_hash(neg,Aneg),'negative_quadratic_coefficients':r.to_json(negative_quadratic),
              'negative_principal_function':'s_negative=negative_quadratic/f0^2, div=A_initial+A_negative; F_minus1=s_negative^(-1)',
              'negative_flip_record':negative_record,'point_coordinates':r.to_json(K),'point_frobenius':r.to_json(A),
              'point_sha256':point_hash(K,A),'random_state':rng.getstate(),
              'status':'actual based CM SLP in progress; no local or global height claimed'}
        sha,size=write_checkpoint(checkpoint,data)
        print('ACTUAL CM SLP INITIAL SAVED',label,size,sha,'setup seconds',round(time.monotonic()-begin,2),flush=True)
    del sources, initial, initial_raw, published, point
    gc.collect()
    try:
        ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:
        pass
    print('ACTUAL CM MEMORY RELEASE', '; '.join(line for line in Path('/proc/self/status').read_text().splitlines() if line.startswith(('VmRSS:', 'VmHWM:'))), flush=True)
    start=time.monotonic();start_steps=len(data['steps'])
    def record_step(record,section,operation,bit):
        encoded=r.to_json(section)
        record.update({'operation':operation,'bit':bit,'sign':data['sign'],
                       'principal_section_coefficients':encoded,
                       'principal_coefficient_sha256':hashlib.sha256(json.dumps(encoded,separators=(',',':')).encode()).hexdigest()})
        data['steps'].append(record)
    for n in range(data['bits_done'],min(len(bits),args.max_bits)):
        K,A,f,rec=addflip_with_section(K,A,K,A,M,rng,label+' double bit'+str(n+1),r,same=True)
        data['sign']*=-1;data['magnitude']*=2
        record_step(rec,f,'double',n+1)
        if bits[n]=='1':
            Q,AQ=(C,AC) if data['sign']==1 else (neg,Aneg)
            K,A,f,rec=addflip_with_section(K,A,Q,AQ,M,rng,label+' add bit'+str(n+1),r)
            data['sign']*=-1;data['magnitude']+=1
            record_step(rec,f,'add',n+1)
        data['bits_done']=n+1;assert data['magnitude']==int(bits[:n+1],2)
        data['point_coordinates'],data['point_frobenius']=r.to_json(K),r.to_json(A)
        data['point_sha256']=point_hash(K,A);data['random_state']=rng.getstate()
        if (n+1)%5==0 or n+1==min(len(bits),args.max_bits):
            sha,size=write_checkpoint(checkpoint,data)
            print('ACTUAL CM SLP CHECKPOINT',label,n+1,'bits',len(data['steps']),'steps','bytes',size,
                  'seconds',round(time.monotonic()-start,2),'newsteps',len(data['steps'])-start_steps,
                  'peak_MiB',round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,1),'sha',sha,flush=True)
    if data['bits_done']==304:
        assert data['sign']==1 and data['magnitude']==m
        data['zero_test_mod47']=zero_test_mod47(K,M)
        data['status']='complete actual based CM304-bit SLP and full zero reduction; all principal sections retained; actual formal endpoint transfer and heights are subsequent computations'
        sha,size=write_checkpoint(checkpoint,data)
        print('ACTUAL CM SLP COMPLETE',label,len(data['steps']),'steps',size,sha,
              'peak_MiB',round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,1),flush=True)

if __name__=='__main__':main()

