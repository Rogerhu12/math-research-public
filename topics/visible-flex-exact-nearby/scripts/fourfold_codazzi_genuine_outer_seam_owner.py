"""First complete genuine reception of the 1973 exterior true negative polynomial seams."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from hashlib import sha256
from importlib.metadata import version
from pathlib import Path
import gzip,io,json,os,struct,subprocess,sys
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_characteristic_seed_admission import ROOT
from fourfold_codazzi_true_phase_original_inputs import check,DELTA
from fourfold_codazzi_true_ratio_restore_inputs import GPR,PHASE
from fourfold_codazzi_true_ratio_cut_and_reference import Phase
from fourfold_codazzi_true_ratio_live_rules import canonical,gate
from fourfold_codazzi_true_ratio_prefix import Prefix,replace,record_failure
from fourfold_codazzi_genuine_root_seam_receiver import check_rule_inputs,upwards,dyadic,decode,frame
from fourfold_codazzi_genuine_outer_seam_input import TC,TC_SHA,CURRENT,NATIVE
from fourfold_codazzi_genuine_outer_seam_operator import at,receive

CARRIER='complete-1973-genuine-outer-seams.gz'


def node_input(args,inp,read):
    p=args.original/'original-direction.json';info=json.loads(p.read_bytes())
    cube=Path(info['cubic']).resolve()
    check(cube.is_relative_to(args.original.resolve()) and cube.stat().st_size==info['bytes']
          and sha256(cube.read_bytes()).hexdigest()==info['sha256']==NATIVE
          and info['no_old_science'] is True and len(info['all14'])==14,
          'all 14 original 193-coordinate signed shards and the whole native cubic')
    cm=read(CURRENT,TC);check(sha256(cm).hexdigest()==TC_SHA,'actual descriptor')
    old=json.loads(cm);roles=old['roles'];dpath=roles['direction_index'];orig=args.original/'source'
    raw=(orig/dpath).read_bytes();check(sha256(raw).hexdigest()=='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6','complete original direction index')
    index=json.loads(raw);nodes=[]
    z=np.load(cube,mmap_mode='r',allow_pickle=False)
    check(z.shape==(4,6144,193) and z.dtype==np.dtype('float64'),'entire original signed cubic')
    pos=0
    for spec,row in zip(info['all14'],index['parts']):
        path=orig/spec['path'];b=path.read_bytes()
        check(spec['sha256']==row['sha256']==sha256(b).hexdigest() and spec['bytes']==row['bytes']==len(b)
              and path.name==row['file'] and pos==row['first_interval'],'true original full ordered shard')
        with np.load(io.BytesIO(gzip.decompress(b)),allow_pickle=False) as f:
            a=f['piece_coefficients'];r=f['radial_nodes'];end=row['last_interval_exclusive']
            check(np.array_equal(a,z[:,pos:end,:]) and (not nodes or nodes[-1]==Q(float(r[0]))),'whole original coefficients and shared physical seam')
            nodes.extend(Q(float(v)) for v in r[int(pos>0):]);pos=end
    check(pos==6144 and nodes[:len(inp.nodes)]==inp.nodes,'all 2693 strict-plan knots are the actual direction knots')
    return z,info


def read_frame(f):
    n,=struct.unpack('<I',f.read(4))
    check(0<n<2_000_000,'one natural GJO frame')
    b=f.read(n);check(len(b)==n,'whole private GJO frame')
    return b


def continuation(a,pr,head,base):
    if not a.resume:return 0,-1,arb(0),[arb(0),arb(0)]
    b=a.resume.read_bytes();check(sha256(b).hexdigest()==a.resume_sha,'complete original saved receipt')
    d=json.loads(b);n=d['completed_subpieces']
    check(not d['complete'] and 0<n<=1973 and all(d[k]==base[k] for k in ('plan_sha256','original_cubic_sha256',
          'phase_sha256','original_inputs_sha256')),'same complete source plan and prefix')
    body=(a.resume_dir/CARRIER).read_bytes()[:d['private_prefix_bytes']];u=gzip.decompress(body)
    check((len(body),sha256(body).hexdigest(),len(u),sha256(u).hexdigest())==tuple(d[k] for k in
        ('private_prefix_bytes','private_prefix_sha256','private_prefix_uncompressed_bytes','private_prefix_uncompressed_sha256')),
        'whole signed private source and all actual original dyadics')
    f=io.BytesIO(u);check(read_frame(f)==head,'same original source header')
    for k in range(1973,1973-n,-1):
        row=read_frame(f);rec=json.loads(row);check(rec['piece']==k,'same complete original physical seam')
        pr.append(frame(row))
    check(not f.read(1) and pr.gz.hexdigest()==d['private_prefix_sha256'],'complete copied private prefix')
    b=(a.resume_dir/d['continuation_file']).read_bytes();raw=gzip.decompress(b)
    check((len(b),sha256(b).hexdigest(),len(raw),sha256(raw).hexdigest())==tuple(d[k] for k in
        ('continuation_bytes','continuation_sha256','continuation_uncompressed_bytes','continuation_uncompressed_sha256')),
        'whole private original continuation')
    v=json.loads(raw);check(v['count']==n and v['plan']==base['plan_sha256'],'same complete radial frontier')
    pr.commit(dict(base,completed_subpieces=n,prefix_proved=True),raw)
    return n,v['next_cell'],decode(v['log_majorant']),list(map(decode,v['totals']))


def numeric(a):
    check(os.environ['GITHUB_ACTIONS']=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
        and os.environ['GITHUB_RUN_ATTEMPT']=='1' and sys.version_info[:3]==(3,12,14)
        and version('numpy')=='2.3.5' and version('python-flint')=='0.9.0','one first public scientific owner')
    gate();ctx.prec=320;ctx.cap=16
    def read(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=a.repo)
    old,inp,ids=check_rule_inputs(a.repo,read)
    oldneg={s['right_piece']:s for s in old['seams'] if s['side']=='negative'}
    check(set(oldneg)==set(range(1974,2550)) and inp.nodes[1974]==Q(oldneg[1974]['radial']),
          'no one of the 576 previously covered negative seams is re-evaluated')
    phase_raw=(a.parents/'gpr-receipt.json').read_bytes()
    check(len(phase_raw)==GPR[2] and sha256(phase_raw).hexdigest()==GPR[3],'whole historical GPR receipt')
    cert=json.loads(phase_raw)
    check(cert['complete'] is cert['proved'] is True and str(cert['run'])==GPR[0]
          and cert['event_commit']==GPR[1] and cert['private_carrier']==PHASE and all(cert['quantitative_gates'].values())
          and cert['original_receipts_sha256']==sha256(canonical(ids)).hexdigest(),'complete successful original GPR phase')
    phase=Phase(a.parents/'true-phase-inward-complete.bin.gz',PHASE,inp.plan)
    z,original=node_input(a,inp,read)
    rl,rh=map(Q,ROOT);anchor=inp.nodes[1974];knots=inp.nodes
    check(0<rl-anchor<=rh-anchor<Q(1,50) and rl-knots[1973]>Q(1,50) and knots[0]==0,
          'entire actual disjoint strict exterior; no supported potential')
    # The actual root-predecessor certifies k<314 and A>4 on the anchor.
    rootdocs=json.loads((a.repo/('topics/visible-flex-exact-nearby/notes/piecewise_real_root_fold_resume_v2_ci/'
                                'run-43616813816-1/consumers/process.json')).read_bytes())
    from fourfold_codazzi_signed_density_transport_arithmetic import ball
    check(ball(rootdocs['selected']['bounds']['k_upper']).upper()<314,'verified original anchor curvature factor')
    q0=(314*exact(rh-anchor)).sqrt();smin=(exact(rl-anchor)).sqrt()*arb(4).root(3)
    scale0=exact(Q(23,10))*(q0/smin).sqrt()
    plan=[[k,str(knots[k])] for k in range(1973,0,-1)]
    base=dict(kind='R149_original_signed_genuine_outer_1973_physical_seam_receivers',run=os.environ['GITHUB_RUN_ID'],
        attempt=1,event_commit=os.environ['GITHUB_SHA'],retained_root_interface_count=576,
        exterior_seam_count=1973,same_cubic_cut_points_exact_zero=521,all_negative_original_seams=2549,
        plan_sha256=sha256(canonical(plan)).hexdigest(),original_cubic_sha256=NATIVE,
        original_direction_files=14,original_direction_receipts_sha256=sha256(canonical(original['all14'])).hexdigest(),
        original_angular_family_absolute_delta=str(DELTA),phase_sha256=PHASE['sha256'],
        original_inputs_sha256=sha256(canonical(ids)).hexdigest(),previous_paid_science_targets_recomputed=0,
        full_genuine_ordinary_or_positive_or_endpoint_response_claimed=False)
    head=canonical(dict(plan=plan,receipts=ids,gpr=PHASE,original_cubic=NATIVE,anchor=str(anchor),
                    data='all 65 base and 193 direction exact dyadic slope jumps before alpha/delta; original independent mean',
                    receiving='physical reflected first row JP into strict H^-1; no radial weight on impulse'))
    a.private.mkdir(parents=True,exist_ok=True);out=a.private/CARRIER;pr=Prefix(out,a.receipt,head,base)
    try:
        n,next_cell,logbound,totals=continuation(a,pr,head,base)
        for i,cell in enumerate(inp.plan):
            l,r,k,_=cell;rows,errs=phase.row()
            if r>anchor or i<next_cell or n==1973:continue
            gate()
            u,v,beta,K,_,_=at(inp,cell,l,r)
            L=(2*abs(beta*((u*u+v*v*K).mean()))).upper()
            logbound=(logbound+exact(r-l)*L).upper()
            if l!=knots[k] or k==0:continue
            check(k==1973-n,'entire ordered physical one-sided jump')
            rec,basejump,direction=receive(inp,z,cell,k,l,rows,errs,scale0*logbound.exp())
            after=(rec['raw']*rec['strict_J']).upper();totals=[(totals[0]+after).upper(),(totals[1]+rec['waist']).upper()]
            n+=1;data=dict(piece=k,r=str(l),native_cell=i,base=list(map(str,basejump)),direction=list(map(str,direction)),
                  joint_receivers={k:dyadic(v) for k,v in rec.items()},log_majorant=dyadic(logbound),
                  selected_delta_radius=str(DELTA))
            pr.append(frame(canonical(data)))
            front=canonical(dict(count=n,next_cell=i+1,log_majorant=dyadic(logbound),totals=list(map(dyadic,totals)),plan=base['plan_sha256']))
            pr.commit(dict(base,completed_subpieces=n,prefix_proved=True,strict_Hminus1_sum=upwards(totals[0]),
                      natural_to_waist=upwards(totals[1]),last_read_head=gate()),front)
            if n%96==0:print('GJO_COMPLETE_PREFIX',n,upwards(totals[1]),flush=True)
        phase.close()
    finally:pr.close()
    b=out.read_bytes();u=gzip.decompress(b)
    check(n==1973 and len(b)==pr.csize and len(u)==pr.usize and sha256(b).hexdigest()==pr.gz.hexdigest()
          and sha256(u).hexdigest()==pr.raw.hexdigest() and len(u)<150_000_000,
          'all complete physical private signed dyadics read back')
    common=(exact(Q(62,5))*totals[1]).upper()
    result=dict(base,complete=True,proved=True,completed_subpieces=n,strict_Hminus1_sum=upwards(totals[0]),natural_waist=upwards(totals[1]),
          common_input_waist=upwards(common),under_one_tenth=common<exact(Q(1,10)),under_one=common<1,
          private_bytes=len(b),private_sha256=sha256(b).hexdigest(),private_uncompressed_bytes=len(u),
          private_uncompressed_sha256=sha256(u).hexdigest(),last_rules_read_head=gate())
    replace(a.receipt,canonical(result));print('GJO_WHOLE_RECEIPT',canonical(result).decode().strip(),flush=True)


if __name__=='__main__':
    ap=ArgumentParser()
    for x in ('repo','private','receipt','parents','original'):ap.add_argument('--'+x,required=True,type=Path)
    ap.add_argument('--resume',type=Path);ap.add_argument('--resume-sha');ap.add_argument('--resume-dir',type=Path)
    a=ap.parse_args()
    try:
        check(bool(a.resume)==bool(a.resume_sha)==bool(a.resume_dir),'whole continuation identity')
        numeric(a)
    except Exception as exc:
        record_failure(a.receipt,exc)
        raise
