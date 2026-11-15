import gzip, hashlib, json, pathlib, struct, subprocess

repo=pathlib.Path('/workspace/scratch/visible-larger-recovered-20261114-1843/math-research-public')
src=pathlib.Path('/tmp/actual93-inexact-p3-readback')
art=pathlib.Path('/tmp/visible-larger-recovery-2207/actions-debug/visible-mainline-smallcoreresonance-43674264245-1')
base=art/'small-core-inexact-p3-restoration'
dig=lambda b:hashlib.sha256(b).hexdigest()
checks=[]
def check(label,condition):
    assert condition,label
    checks.append(label)
def readj(p):
    b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
summary=readj(src/'2026-11-15-actual93-byte-audit-summary.json')
audit=readj(src/summary['byte_audit']['file'])
literal=readj(src/summary['literal_readout']['file'])
status=readj(base/'inexact-p3-restoration-status.json')
fixed={
'2026-11-15-actual93-inexact-p3-restoration-eight-accepted-directions.md':(22096,'ca1725e734ffd74f1adfbdb99a26a61ca2bf2f3800ef8746d3fdb4aa9b0d746e'),
'2026-11-15-actual93-byte-audit-summary.json':(4142,'30f5a97aafdf2fff32e98e273ac70de5238ed8528645be474580303f88446650'),
'audit_actual93_inexact_p3_bytes.py':(46350,'8356b2fda87ac7e42a97a5c398b95417773119eedfb56b159cab64362a296363')}
for n,(size,sha) in fixed.items():
    b=(src/n).read_bytes();check('frozen '+n,len(b)==size and dig(b)==sha)
for r in [summary['byte_audit'],summary['literal_readout'],*summary['original_payload_copies']]:
    b=(src/r['file']).read_bytes();check('published '+r['file'],len(b)==r['bytes'] and dig(b)==r['sha256'])
    if 'decoded_sha256' in r:
        raw=gzip.decompress(b);check('decoded '+r['file'],len(raw)==r['decoded_bytes'] and dig(raw)==r['decoded_sha256'])
check('complete 5785 audit checks',len(audit['checks'])==5785 and all(r['passed'] is True for r in audit['checks']))
check('all audit flags',audit['all_checks_passed'] is True and summary['all_checks_passed'] is True)
for r in audit['inventory']:
    b=(art/r['file']).read_bytes();check('original '+r['file'],len(b)==r['bytes'] and dig(b)==r['sha256'])
for r in audit['sources']:
    b=subprocess.check_output(['git','show','8adc3251a8fe2ee7bcbc5d6d8381631b1558141e:'+r['file']],cwd=repo)
    check('actual dispatch '+r['file'],len(b)==r['bytes'] and dig(b)==r['sha256'])
check('complete original status bytes',gzip.decompress((src/'2026-11-15-actual93-original-complete-status.json.gz').read_bytes())==(base/'inexact-p3-restoration-status.json').read_bytes())
check('complete original event bytes',gzip.decompress((src/'2026-11-15-actual93-original-evaluation-ledger.jsonl.gz').read_bytes())==(base/status['original_call_trace']['file']['file']).read_bytes())
rawinners=[gzip.decompress((base/r['file']).read_bytes()) for r in status['inner_reports']]
check('all15 original inner numeric tokens',gzip.decompress((src/'2026-11-15-actual93-original-inner-reports.json.gz').read_bytes())==b'[\n'+b',\n'.join(b.strip() for b in rawinners)+b'\n]\n')
counts={'nodes':0,'float_words':0}
skipped=[]
def eq(a,b,path):
    counts['nodes']+=1
    if isinstance(a,float):
        assert isinstance(b,float) and struct.pack('<d',a)==struct.pack('<d',b),path
        counts['float_words']+=1
    elif isinstance(a,dict):
        assert isinstance(b,dict) and a.keys()==b.keys(),path
        for k in a:eq(a[k],b[k],path+'/'+k)
    elif isinstance(a,list):
        assert isinstance(b,list) and len(a)==len(b),path
        for i,(x,y) in enumerate(zip(a,b)):eq(x,y,path+'/'+str(i))
    else:assert type(a) is type(b) and a==b,path
def copied(a,b,path):
    if isinstance(a,dict):
        assert isinstance(b,dict),path
        for k,v in a.items():
            if k in b:copied(v,b[k],path+'/'+k)
            else:skipped.append(path+'/'+k)
    elif isinstance(a,list):
        assert isinstance(b,list) and len(a)==len(b),path
        for i,(x,y) in enumerate(zip(a,b)):copied(x,y,path+'/'+str(i))
    else:eq(a,b,path)
for k in ['initial','final','initial_projection','initial_original_three_equation_merit','final_original_three_equation_merit','last_accepted_parameters','source_roles','consumed_source_sha256','input_sha256','parent_status','original_complete_circle_check','complete_scalar_domain','seconds','search_stop_reason']:
    eq(literal[k],status[k],k)
for k,v in literal['flags'].items():eq(v,status[k],'flags/'+k)
copied(literal['outer_searches'],status['searches'],'outer_searches')
for i,(lr,rr,rb) in enumerate(zip(literal['inner_reports'],status['inner_reports'],rawinners)):
    ri=json.loads(rb)
    check('inner decoded '+str(i),len(rb)==lr['decoded_bytes'] and dig(rb)==lr['decoded_sha256'])
    eq(lr['receipt'],rr,'inner_receipt/'+str(i))
    for k in ['final_J_parameter_identity','final_original_full_three_by_three_jacobian','inner_call','label','last_probe','original_call_cost','seed_parameters','stop_reason','usable_inner_root','usable_restoration_point']:
        eq(lr[k],ri[k],'inner/'+str(i)+'/'+k)
    copied(lr['steps'],ri['steps'],'inner_steps/'+str(i))
for oi,(lo,ro) in enumerate(zip(literal['outer_searches'],status['searches'])):
    for ti,(lt,rt) in enumerate(zip(lo['trials'],ro['trials'])):
        eq(lt['outer_iteration'],ro['iteration'],'mapped outer_iteration')
        eq(lt['outer_accepted'],rt['accepted'],'mapped outer_accepted')
        for k in ['inner_call','usable_inner_root','usable_restoration_point']:eq(lt[k],rt['inner'][k],'mapped '+k)
        eq(lt['last_inner_probe'],rt['inner'].get('last_probe'),'mapped last_inner_probe')
for lr,rb in zip(literal['inner_reports'],rawinners):
    ri=json.loads(rb)
    for ls,rs in zip(lr['steps'],ri['steps']):eq(ls['p3_newton_direction'],rs.get('p3_newton_direction'),'mapped optional direction')
allowed=('original_J_event_number','inner_call','last_inner_probe','outer_accepted','outer_iteration','p3_newton_direction','usable_inner_root','usable_restoration_point')
check('all extra copied structure keys explicitly mapped except audited event links',all(p.rsplit('/',1)[-1] in allowed for p in skipped))
out={'schema':'actual93-root-independent-byte-readback-v1','actual':summary['actual'],'checks':checks,'check_count':len(checks),'all_checks_passed':True,'agent_check_count':5785,'original_inventory_count':len(audit['inventory']),'actual_dispatch_source_count':len(audit['sources']),'copied_literal_counts':counts,'added_or_mapped_key_count':len(skipped),'scope':'Complete frozen files, original payload bytes, actual dispatch source bytes and copied JSON/IEEE-754 words only. No scientific arithmetic or execution. Four mathematical inputs reuse the already completed actual92 full byte audit.','new_scientific_computation':False}
p=pathlib.Path('/tmp/2026-11-15-actual93-root-independent-byte-readback.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['checks']},indent=2));print('receipt',p.stat().st_size,dig(p.read_bytes()))
