"""First genuine whole-profile reception of the 576 saved negative root-window atoms."""
from argparse import ArgumentParser
from bisect import bisect_right
from fractions import Fraction as Q
from hashlib import sha256
from importlib.metadata import version
from math import inf, isfinite, nextafter
from pathlib import Path
import gzip
import io
import json
import os
import struct
import subprocess
import sys

from flint import arb, ctx
from fourfold_codazzi_signed_density_transport_arithmetic import exact, ball
from fourfold_codazzi_true_characteristic_seed_admission import ROOT
from fourfold_codazzi_true_phase_original_inputs import admit, check, CUT, DELTA, MANIFEST, TOPIC, CONTROL
from fourfold_codazzi_true_phase_signed_speed import Inputs, restricted
from fourfold_codazzi_true_ratio_live_rules import canonical, gate
from fourfold_codazzi_true_ratio_prefix import Prefix, replace, record_failure

OLD = TOPIC + 'notes/actual_first_Airy_seam_operators_ci/run-43625828234-1/consumers/actual-first-Airy-seam-operators.json.gz'
REV = '3f0e88234eb9aec8888606c3ba726c32fc201cbf'
OLD_SHA = '871aa54de8c4ee1caa47cdab39c8033bb9cd02e9d4d1f404b711ab8c28825642'
SCALAR = TOPIC + 'notes/piecewise_real_root_fold_resume_v2_ci/run-43616813816-1/consumers/process.json'
SCALAR_SHA = 'c30eb4c5e1efebd3663528418389ececf1ba8f4450f8e667496026915e2dfb64'
PACK = struct.Struct('<I')
N = 388
WIDTH = Q(1,32)
PRIVATE = 'genuine-root-negative-576-atoms.gz'


def upwards(x):
    z = nextafter(float(x.upper()),inf)
    check(isfinite(z) and z>=0,'finite directed receipt endpoint')
    return z


def dyadic(x):
    m,e=x.upper().man_exp()
    return [str(m),int(e)]


def decode(v):
    return exact(Q(int(v[0]))*Q(2)**int(v[1]))


def frame(b):
    return PACK.pack(len(b))+b


def read_frame(f):
    n,=PACK.unpack(f.read(PACK.size))
    b=f.read(n)
    check(0<n<100000 and len(b)==n,'complete original natural record')
    return b


def check_rule_inputs(repo,read):
    d=read(REV,OLD)
    check(len(d)==904977 and sha256(d).hexdigest()==OLD_SHA,'whole original 1079-seam native')
    old=json.loads(gzip.decompress(d))
    root=list(map(Q,ROOT))
    check(old['complete'] and old['proved'] and old['failure'] is None
          and old['root_native_sha256']=='dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212'
          and old['public_run_id']==str(43625828234) and int(old['public_run_attempt'])==1
          and len(old['seams'])==1079 and old['negative_seam_count']==576
          and list(map(Q,old['exact_root_interval']))==root and Q(old['exact_real_delta_radius'])>=DELTA,
          'original all-coordinate seam definition, family, root interval and actual scope')
    raw=(repo/SCALAR).read_bytes()
    check(len(raw)==32670 and sha256(raw).hexdigest()==SCALAR_SHA,'whole original complex-strip root geometry')
    d=json.loads(raw);b=d['selected']['bounds']
    check(d['complete'] and d['mathematical_complete'] and d['actual_returncode']==0
          and d['selected']['passed'] and d['selected']['exact_radius']=='1/50'
          and ball(b['A_lower']).lower()>4 and ball(b['A_upper']).upper()<23
          and ball(b['angular_Jacobian_fee']).upper()<exact(Q(1,80))
          and ball(b['T_phi']).upper()<exact(Q(7,1000)) and ball(b['T_upper']).upper()<exact(Q(4,25))
          and ball(b['leading_G']).upper()<exact(Q(23,10)),
          'all root-strip bounds used in the genuine whole-profile receiver')
    saved=admit((repo/MANIFEST).read_bytes(),read)
    return old,Inputs(*saved[:-1]),saved[-1]


def seam(inp,row):
    r=Q(row['radial']); index=row['right_piece']; i=bisect_right(inp.rights,r)
    rl,rh=map(Q,ROOT);lo,hi=rl-r,rh-r
    check(row['left_piece']==index-1 and inp.nodes[index]==r and CONTROL[1]<r<CUT
          and inp.bounds[i][0]<=r<=inp.bounds[i][1] and 0<lo<=hi<Q(1,50)
          and Q(row['exact_minimum_root_distance'])==lo and Q(row['exact_maximum_root_distance'])==hi,
          'same true cubic seam and actual root distances')
    centre,models=inp.rows[i];xr=exact(r-centre)
    q,qr=[restricted(models['q'],xr,j) for j in (0,1)]
    gamma=restricted(models['gamma'],xr,0)
    beta=abs(restricted(models['beta'],xr,0)).upper()
    u0,v0=inp.piece(index)[0]
    # At this actual right-piece knot the cubic constant is exactly its point value.
    u=u0+inp.du;v=v0+inp.dv+restricted(models['s'],xr,0)
    U,V=u.a(0,WIDTH),v.a(0,WIDTH); vm=v.mean()
    eta=(-gamma*vm).lower(); ql=q.lower()
    check(ql>0 and gamma.lower()>0 and eta>0 and vm.upper()<0,
          'true nonzero geometric and independent-mean denominators')
    dm=exact(Q(row['exact_mean_jump_absolute_bound']))/abs(vm).lower()
    jump=ball(row['original_first_derivative_pair_norm']).upper()
    K=(q*q).upper()
    B=2*beta*max(K*V,U)*jump+dm*(beta*(1+U*U+K*V*V)+abs(qr).upper()/(2*ql))
    C=(2*beta*max(U,V)*jump+2*beta*U*V*dm)/eta
    x=exact(Q(81,80));y=exact(Q(7,1000));g=exact(Q(23,20))
    sup_s=arb(23).root(3)*exact(hi).sqrt();inf_s=arb(4).root(3)*exact(lo).sqrt()
    t=y*sup_s;b=eta*ql
    ja=min((g*(B*t/b+C*x)).upper(),ball(row['first_amplitude_radial_jumps']['a']).upper())
    jb=min((g*(B*x/b+C*t)/inf_s).upper(),ball(row['first_amplitude_radial_jumps']['b']).upper())
    theta=(arb(N).root(3)**(-2)+sup_s**2).sqrt()
    H=(x+y*max(theta,exact(Q(4,25))/theta))/exact(Q(79,80)**2)
    E=y/theta;p,d=exact(Q(4,17)),exact(Q(1,17));h=exact(WIDTH)
    factor=H**2*(1+2*p/h+4*d/h**2)+290*E*(d*H+(p+d/h)*H**2/N)
    weighted=ja+theta*jb
    raw=2*arb(2).sqrt()*weighted*factor.root(6)**5/arb(N).root(6)*(1+exact(Q(1,N*N)))
    after=(raw*ball(row['complete_old_J_one_gain']).upper()).upper()
    receiver=2039 if r>=rh-Q(1,200) else 192
    waist=(receiver*exact(Q(719,1000))*after).upper()
    values=[B,C,ja,jb,theta,H,E,factor,weighted,raw,after,waist]
    check(all(z.is_finite() and z>=0 for z in values),'entire nonnegative reception')
    return {'piece':index,'r':str(r),'radius':[str(lo),str(hi)],'component_digest':
            row['original_first_derivative_component_jump_sha256'],'receiver':receiver,
            'ordered_dyadic_uppers':list(map(dyadic,values))},after,waist


def restore(args,prefix,head,base,plan):
    total=[arb(0),arb(0)]
    if not args.resume_receipt:return 0,total
    record=args.resume_receipt.read_bytes()
    check(sha256(record).hexdigest()==args.resume_sha,'whole original failed-prefix receipt')
    prior=json.loads(record);n=prior['completed_subpieces']
    check(not prior['complete'] and 0<n<=len(plan) and prior['plan_sha256']==base['plan_sha256']
          and prior['original_inputs_sha256']==base['original_inputs_sha256'],'same first unpaid seam frontier')
    data=(args.resume_private/PRIVATE).read_bytes()[:prior['private_prefix_bytes']]
    check(len(data)==prior['private_prefix_bytes'] and sha256(data).hexdigest()==prior['private_prefix_sha256'],
          'whole compressed prefix')
    u=gzip.decompress(data)
    check(len(u)==prior['private_prefix_uncompressed_bytes'] and sha256(u).hexdigest()==prior['private_prefix_uncompressed_sha256'],
          'whole decompressed prefix')
    f=io.BytesIO(u);check(read_frame(f)==head,'same full header')
    for row in plan[:n]:
        payload=read_frame(f);v=json.loads(payload)
        check(v['r']==row['radial'] and v['component_digest']==row['original_first_derivative_component_jump_sha256'],
              'actual paid seam and correct ordinal')
        prefix.append(frame(payload))
    check(not f.read(1) and prefix.gz.hexdigest()==prior['private_prefix_sha256'],'unmodified full ordered prefix')
    fr=(args.resume_private/prior['continuation_file']).read_bytes()
    check(len(fr)==prior['continuation_bytes'] and sha256(fr).hexdigest()==prior['continuation_sha256'],'whole frontier')
    fraw=gzip.decompress(fr)
    check(len(fraw)==prior['continuation_uncompressed_bytes']
          and sha256(fraw).hexdigest()==prior['continuation_uncompressed_sha256'],'whole raw frontier')
    fs=json.loads(fraw);check(fs['count']==n and fs['plan']==base['plan_sha256'],'same exact frontier')
    prefix.commit(dict(base,completed_subpieces=n,prefix_proved=True),fraw)
    return n,list(map(decode,fs['totals']))


def run(args):
    check(os.environ['GITHUB_ACTIONS']=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
          and os.environ['GITHUB_RUN_ATTEMPT']=='1' and sys.version_info[:3]==(3,12,14)
          and version('numpy')=='2.3.5' and version('python-flint')=='0.9.0','only original public owner')
    gate();ctx.prec=320
    def read(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=args.repo)
    old,inp,ident=check_rule_inputs(args.repo,read)
    plan=sorted((v for v in old['seams'] if v['side']=='negative'),key=lambda v:Q(v['radial']),reverse=True)
    check(len(plan)==576 and all(a['right_piece']==b['right_piece']+1 for a,b in zip(plan,plan[1:]))
          and plan[0]['right_piece']==2549,'all consecutive native negative root-window interfaces')
    ids=[[s['radial'],s['right_piece'],s['original_first_derivative_component_jump_sha256']] for s in plan]
    base=dict(kind='complete_genuine_negative_root_window_576_interface_operators',
              run=os.environ['GITHUB_RUN_ID'],attempt=1,event_commit=os.environ['GITHUB_SHA'],
              original_seam_sha256=OLD_SHA,original_inputs_sha256=sha256(canonical(ident)).hexdigest(),
              original_input_files=len(ident),original_input_bytes=sum(s['bytes'] for s in ident),
              plan_sha256=sha256(canonical(ids)).hexdigest(),original_interfaces=len(plan),
              initial_input_N=N,old_scientific_targets_recomputed=0,outer_negative_seams_included=False)
    head=canonical({k:v for k,v in base.items() if k not in ('run','attempt','event_commit')})
    args.private.mkdir(parents=True,exist_ok=True)
    path=args.private/PRIVATE
    prefix=Prefix(path,args.receipt,head,base)
    try:
        n,totals=restore(args,prefix,head,base,plan)
        for row in plan[n:]:
            gate()
            data,after,waist=seam(inp,row)
            totals=[(totals[0]+after).upper(),(totals[1]+waist).upper()]
            data['ordinal']=n+1;prefix.append(frame(canonical(data)));n+=1
            front=canonical(dict(count=n,totals=list(map(dyadic,totals)),plan=base['plan_sha256']))
            prefix.commit(dict(base,completed_subpieces=n,prefix_proved=True,mixed_sum=upwards(totals[0]),
                               reference_waist_sum=upwards(totals[1]),last_rules_read_head=gate()),front)
            if n%64==0:print('GJR_PREFIX',n,upwards(totals[1]),flush=True)
    finally:prefix.close()
    v=path.read_bytes();u=gzip.decompress(v);total=exact(Q(62,5))*totals[1]
    check(n==576 and len(v)==prefix.csize and sha256(v).hexdigest()==prefix.gz.hexdigest()
          and len(u)==prefix.usize and sha256(u).hexdigest()==prefix.raw.hexdigest() and len(u)<2_000_000,
          'full physical atom stream read back')
    result=dict(base,complete=True,proved=True,completed_subpieces=n,raw_mixed_sum=upwards(totals[0]),
                all_reference_to_physical_waist_sum=upwards(totals[1]),
                common_input_to_physical_waist_sum=upwards(total),under_one_tenth=total<exact(Q(1,10)),
                under_one=total<1,private_bytes=len(v),private_sha256=sha256(v).hexdigest(),
                private_uncompressed_bytes=len(u),private_uncompressed_sha256=sha256(u).hexdigest(),
                last_rules_read_head=gate(),full_physical_response_claimed=False)
    replace(args.receipt,canonical(result))
    print('GJR_WHOLE_SMALL_RECEIPT',canonical(result).decode().strip(),flush=True)


if __name__=='__main__':
    ap=ArgumentParser()
    for name in ('repo','private','receipt'):ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--resume-receipt',type=Path);ap.add_argument('--resume-private',type=Path);ap.add_argument('--resume-sha')
    args=ap.parse_args()
    try:
        check(bool(args.resume_receipt)==bool(args.resume_private)==bool(args.resume_sha),'complete prefix identity')
        run(args)
    except Exception as exc:
        record_failure(args.receipt,exc)
        raise
