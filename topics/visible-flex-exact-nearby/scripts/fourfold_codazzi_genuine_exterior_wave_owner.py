"""Original signed source and two true physical propagators over the support-exterior strict domain."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from hashlib import sha256
from importlib.metadata import version
from math import isfinite,nextafter,inf
from pathlib import Path
import gzip,io,json,os,struct,subprocess,sys
from flint import arb,ctx
from fourfold_codazzi_true_phase_original_inputs import check,DELTA
from fourfold_codazzi_true_characteristic_seed_admission import ROOT
from fourfold_codazzi_signed_density_transport_arithmetic import exact,ball,hull
from fourfold_codazzi_true_ratio_restore_inputs import PHASE
from fourfold_codazzi_true_ratio_cut_and_reference import Phase
from fourfold_codazzi_true_ratio_label_quadrature import selected_model_inputs
from fourfold_codazzi_true_ratio_complete_carrier_input import Ratio,CARRIER as GRQ_FILE,WHOLE as GRQ_WHOLE
from fourfold_codazzi_genuine_outer_seam_owner import node_input,read_frame
from fourfold_codazzi_genuine_outer_seam_input import NATIVE
from fourfold_codazzi_genuine_root_seam_receiver import dyadic,decode,frame,upwards,SCALAR,SCALAR_SHA
from fourfold_codazzi_genuine_exterior_wave_fields import fields,geom,BINS
from fourfold_codazzi_genuine_exterior_wave_receiver import receive,source_plan
from fourfold_codazzi_true_ratio_live_rules import gate,canonical
from fourfold_codazzi_true_ratio_prefix import Prefix,replace,record_failure

CARRIER='genuine-exterior-ordinary-wave.bin.gz'
BOX=struct.Struct('<dd')


def restore(a,pr,head,base,plan):
    if not a.resume:return 0,arb(0),[arb(0)]*4
    b=a.resume.read_bytes();check(sha256(b).hexdigest()==a.resume_sha,'complete original scientific prefix receipt')
    d=json.loads(b);n=d['completed_subpieces']
    check(not d['complete'] and 0<n<=len(plan) and all(base[k]==d[k] for k in ('gxm_receipt_sha256',
          'original_176_sha256','original_ratio_sha256','whole_plan_sha256','original_direction_sha256')),
          'entire previous original source, amplitude and ordered physical interval')
    b=(a.resume_dir/CARRIER).read_bytes()[:d['private_prefix_bytes']];u=gzip.decompress(b)
    check((len(b),sha256(b).hexdigest(),len(u),sha256(u).hexdigest())==tuple(d[k] for k in
        ('private_prefix_bytes','private_prefix_sha256','private_prefix_uncompressed_bytes','private_prefix_uncompressed_sha256')),
        'both entire private source prefix identities')
    f=io.BytesIO(u);check(read_frame(f)==head,'same entire private header')
    for j in range(n):
        row=read_frame(f);s=io.BytesIO(row);meta=json.loads(read_frame(s))
        check(meta['index']==j and meta['original_GRQ_row']==plan[j][0] and len(s.read())==meta['signed_bytes'],
              'same private natural source row and all original complex signs')
        pr.append(frame(row))
    check(not f.read(1) and pr.gz.hexdigest()==d['private_prefix_sha256'],'all prior natural rows copied exactly')
    b=(a.resume_dir/d['continuation_file']).read_bytes();u=gzip.decompress(b)
    check((len(b),sha256(b).hexdigest(),len(u),sha256(u).hexdigest())==tuple(d[k] for k in
        ('continuation_bytes','continuation_sha256','continuation_uncompressed_bytes','continuation_uncompressed_sha256')),
        'entire same original signed propagation frontier')
    v=json.loads(u);check(v['completed']==n and v['plan_sha256']==base['whole_plan_sha256'],'correct continued source frontier')
    pr.commit(dict(base,completed_subpieces=n,prefix_proved=True),u)
    return n,decode(v['log_scale']),list(map(decode,v['totals']))


def low_high(z):
    a=nextafter(float(z.lower()),-inf);b=nextafter(float(z.upper()),inf)
    check(isfinite(a) and isfinite(b) and a<=b,'finite entire directed signed amplitude interval')
    return BOX.pack(a,b)


def run(a):
    check(os.environ['GITHUB_ACTIONS']=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
          and os.environ['GITHUB_RUN_ATTEMPT']=='1' and sys.version_info[:3]==(3,12,14)
          and version('python-flint')=='0.9.0' and version('numpy')=='2.3.5','original directed public scientific owner')
    ctx.prec=320;ctx.cap=16;gate()
    gb=a.gxm.read_bytes();check(0<len(gb)<100000 and sha256(gb).hexdigest()==a.gxm_sha,'entire actual GXM receipt')
    gr=json.loads(gb);check(gr['complete'] is gr['proved'] is True and gr['completed_subpieces']==gr['natural_bands']==13
        and gr['all_abs_below_six'] is True and gr['kind']=='R149_true_signed_exterior_homogeneous_ratio_translation'
        and gr['old_targets_recomputed']==0,'complete actually proved true scalar on every original frequency')
    lo,hi=[exact(Q.from_float(v)) for v in gr['all_signed_hull']];mid=(lo+hi)/2;radius=(hi-lo)/2
    check(-6<lo<=hi<6,'same complete directed true real potential multiplier')
    def read(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=a.repo)
    inp,_,km,ids=selected_model_inputs(a.repo)
    z,original=node_input(a,inp,read)
    phase=Phase(a.parents/'true-phase-inward-complete.bin.gz',PHASE,inp.plan)
    ratio=Ratio(a.parents/GRQ_FILE,inp)
    rr=tuple(map(Q,ROOT));rl,rh=rr;plan=source_plan(ratio.plan,rr);start=plan[0][3]
    canon=[[n,i,str(l),str(r),mixed] for n,i,l,r,mixed in plan]
    mraw=(a.repo/SCALAR).read_bytes();check(sha256(mraw).hexdigest()==SCALAR_SHA,'whole original global root anchor')
    m=json.loads(mraw);bb=m['selected']['bounds']
    check(m['complete'] and m['mathematical_complete'] and m['actual_returncode']==0 and m['selected']['passed']
          and m['selected']['exact_radius']=='1/50' and ball(bb['A_lower']).lower()>4
          and ball(bb['k_upper']).upper()<314 and ball(bb['leading_G']).upper()<exact(Q(23,10)),
          'complete true same-radius anchor for the common angularly constant gauge')
    qstart=(314*exact(rh-start)).sqrt();sstart=arb(4).root(3)*exact(rl-start).sqrt()
    scale0=exact(Q(23,10))*(qstart/sstart).sqrt()
    base=dict(kind='R149_complete_genuine_ordinary_exterior_two_profile_wave_to_physical_waist',run=os.environ['GITHUB_RUN_ID'],
          attempt=1,event_commit=os.environ['GITHUB_SHA'],gxm_receipt_sha256=a.gxm_sha,original_176_sha256=sha256(canonical(ids)).hexdigest(),
          original_direction_sha256=NATIVE,original_14_direction_receipts_sha256=sha256(canonical(original['all14'])).hexdigest(),
          original_ratio_sha256=GRQ_WHOLE[1],original_phase_sha256=PHASE['sha256'],whole_plan_sha256=sha256(canonical(canon)).hexdigest(),
          original_GRQ_natural_rows=len(ratio.plan),new_source_pieces=len(plan),window=[str(0),str(start)],
          actual_mixed_exterior_split=str(rh-Q(1,200)),frequency_floor=388,original_delta_upper=str(DELTA),
          physical_bins=BINS,old_science_targets_recomputed=0,exterior_potential_tail_retained=True,
          complete_nonlocal_or_independent_mean_or_endpoint_or_positive_response_claimed=False)
    head=canonical(dict(plan=canon,original_inputs=ids,source='each physical bin: signed (f,g), component (imag-a,real-b), normalized angle orders 0..2',
         signed_units='physical (r,phi) fields divided by the common positive radial E(base)',
         physical_measure='true ordinary dr; first physical port after J and reflected waist',gxm_sha=a.gxm_sha))
    a.private.mkdir(parents=True,exist_ok=True);out=a.private/CARRIER;pr=Prefix(out,a.receipt,head,base)
    try:
        n,logscale,totals=restore(a,pr,head,base,plan);idx=-1;pending=n
        for idx_ratio,(cell_i,l0,r0) in enumerate(ratio.plan):
            if cell_i!=idx:rows,errors=phase.row();idx=cell_i
            active=pending<len(plan) and plan[pending][0]==idx_ratio
            rate=ratio.row(active)
            if not active:continue
            while pending<len(plan) and plan[pending][0]==idx_ratio:
                gate();_,i,l,r,mixed=plan[pending];cell=inp.plan[i]
                tau=hull((cell[1]-r)/(cell[1]-cell[0]),(cell[1]-l)/(cell[1]-cell[0]))
                data,jj=fields(inp,z,km,cell,l,r)
                floor=exact(min(Q(5,2)*(rl-r),Q(1,20)))
                check(floor.lower()>=exact(Q(1,2000)).lower(),'full physical circle outside actual potential support')
                geometry=geom(rows,errors,tau,floor)
                length=exact(r-l);logscale=(logscale+length*2*abs(data['g'].c[0][0]).upper()).upper()
                q,one,arr,detail=receive(geometry,data,rate,scale0*logscale.exp(),jj,mid,radius,mixed)
                off=2*int(mixed);totals[off]=(totals[off]+length*q).upper();totals[off+1]=(totals[off+1]+length*one).upper()
                array=b''.join(map(low_high,arr));check(len(array)==BINS*2*2*3*BOX.size,'both full signed source jet tables')
                meta=canonical(dict(index=pending,original_GRQ_row=idx_ratio,original_GPR_row=i,left=str(l),right=str(r),
                    mixed=mixed,whole_waist_fee=dyadic(q),signed_single_waist_fee=dyadic(one),
                    component_bounds=list(map(dyadic,detail)),signed_bytes=len(array)))
                pr.append(frame(frame(meta)+array));pending+=1
                state=canonical(dict(completed=pending,log_scale=dyadic(logscale),totals=list(map(dyadic,totals)),plan_sha256=base['whole_plan_sha256']))
                pr.commit(dict(base,completed_subpieces=pending,prefix_proved=True,natural_waist_prefix=upwards(totals[0]+totals[2]),
                          last_complete_interval=[str(l),str(r)],last_rule_read_head=gate()),state)
                if pending%64==0:print('GXW_COMPLETE_NATURAL_PREFIX',pending,len(plan),upwards(totals[0]+totals[2]),flush=True)
        phase.close();ratio.close()
    finally:pr.close()
    b=out.read_bytes();u=gzip.decompress(b)
    check(pending==len(plan) and len(b)==pr.csize and len(u)==pr.usize<90_000_000 and sha256(b).hexdigest()==pr.gz.hexdigest()
          and sha256(u).hexdigest()==pr.raw.hexdigest(),'entire exterior through the real waist and all signed private rows')
    natural=(totals[0]+totals[2]).upper();common=(exact(Q(62,5))*natural).upper()
    cert=dict(base,complete=True,proved=True,completed_subpieces=pending,strict_natural_waist=upwards(totals[0]),
         mixed_natural_waist=upwards(totals[2]),strict_single_label_waist_coefficient=upwards(totals[1]),
         mixed_single_label_waist_coefficient=upwards(totals[3]),single_label_scalings=['(388/n)^0.5','(388/n)^(1/6)'],
         whole_natural_waist=upwards(natural),common_C97_addend=upwards(common),under_five_and_one_half=common<exact(Q(11,2)),
         private_bytes=len(b),private_sha256=sha256(b).hexdigest(),private_uncompressed_bytes=len(u),
         private_uncompressed_sha256=sha256(u).hexdigest(),last_rules_read_head=gate())
    replace(a.receipt,canonical(cert));print('GXW_WHOLE_SMALL_RECEIPT',canonical(cert).decode().strip(),flush=True)


if __name__=='__main__':
    p=ArgumentParser()
    for x in ('repo','parents','original','private','receipt','gxm'):p.add_argument('--'+x,required=True,type=Path)
    p.add_argument('--gxm-sha',required=True);p.add_argument('--resume',type=Path);p.add_argument('--resume-sha');p.add_argument('--resume-dir',type=Path)
    a=p.parse_args()
    try:
        check(bool(a.resume)==bool(a.resume_sha)==bool(a.resume_dir),'same complete private continuation')
        run(a)
    except Exception as exc:
        record_failure(a.receipt,exc)
        raise
