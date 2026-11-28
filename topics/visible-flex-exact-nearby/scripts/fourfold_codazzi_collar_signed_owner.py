"""Public first owner for the complete genuine retained local root-collar source."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from importlib.metadata import version
import argparse,gzip,json,os,struct,subprocess,sys
from flint import arb,ctx
import fourfold_codazzi_correlated_collar_reference as F
import fourfold_codazzi_collar_signed_geometry as G
import fourfold_codazzi_collar_signed_operator as O
from fourfold_codazzi_collar_signed_inputs import receive
from fourfold_codazzi_true_characteristic_seed_admission import ROOT,PIECE
from fourfold_codazzi_true_phase_original_inputs import CUT,check
from fourfold_codazzi_true_ratio_live_rules import canonical,gate
from fourfold_codazzi_true_ratio_prefix import Prefix,replace

RAD=4
ANG=128
STOP=2**20
L=struct.Struct('<I')


def bandplan():
    bands=[];lo=97
    while lo<=STOP:
        hi=min(2*lo-1,STOP);bands.append((lo,hi));lo=hi+1
    return bands+[(lo,None)]


def integer_bounds(g,co,lo,sink):
    cap=[arb(0),arb(0)];inv=arb(0).union(F.P.ex(Q(1,4*lo)))
    for a in g:
        vs=F.potential_values(co,a['T']/F.P.ex(F.R))
        for sign in (1,-1):
            row=G.joint(a,inv,*vs,sign)
            cap=[max(m,abs(v).upper()) for m,v in zip(cap,row)]
            for v in [a['T'],*vs,*row]:O.append_box(sink,v)
    return dict(signed_amplitude_upper=list(map(O.upper,cap)),genuine_profile_operator_tail_measured=False)


def resume(a,out,head,plan,base):
    if a.resume is None:return 0,arb(0),[0.,0.]
    import io
    b=a.resume.read_bytes();check(len(b)<100000 and sha256(b).hexdigest()==a.resume_sha,'whole previous collar prefix receipt')
    prior=json.loads(b);n=prior['completed_subpieces']
    check(not prior['complete'] and prior['prefix_proved'] and 0<n<=len(plan)
          and all(prior[k]==base[k] for k in ('kind','plan_sha256','whole_original_input_receipts_sha256','cut','radial_slabs','strip_width')),
          'same complete deterministic collar prefix plan')
    z=(a.resume_directory/'correlated-collar.bin.gz').read_bytes()[:prior['private_prefix_bytes']]
    u=gzip.decompress(z)
    check((len(z),sha256(z).hexdigest(),len(u),sha256(u).hexdigest())==tuple(prior[k] for k in
          ('private_prefix_bytes','private_prefix_sha256','private_prefix_uncompressed_bytes','private_prefix_uncompressed_sha256')),
          'whole preceding private source members')
    stream=io.BytesIO(u);k,=L.unpack(stream.read(4));check(stream.read(k)==head,'entire unchanged source packet header')
    for i in range(n):
        size=stream.read(4);k,=L.unpack(size);rh=stream.read(k);rr=json.loads(rh)
        check([rr['radial_slab'],*rr['band']]==list(plan[i]),'every original preceding physical-band row')
        rp=stream.read(rr['packet_bytes']);check(len(rp)==rr['packet_bytes'],'whole prior signed source row')
        out.append(size+rh+rp)
    check(not stream.read(1) and out.gz.hexdigest()==prior['private_prefix_sha256'] and out.raw.hexdigest()==prior['private_prefix_uncompressed_sha256'],
          'exact complete previous prefix restored with no scientific row rerun')
    a0=(a.resume_directory/prior['continuation_file']).read_bytes();f=gzip.decompress(a0)
    check((len(a0),sha256(a0).hexdigest(),len(f),sha256(f).hexdigest())==tuple(prior[k] for k in
          ('continuation_bytes','continuation_sha256','continuation_uncompressed_bytes','continuation_uncompressed_sha256')),'whole signed frontier')
    d=json.loads(f);check(d['count']==n and d['plan']==base['plan_sha256'],'same prefix endpoint')
    m,e=d['total_exact'];total=F.P.ex(Q(int(m))*Q(2)**int(e));check(total.is_exact() and total>=0,'true previously directed cost')
    out.commit(dict(base,completed_subpieces=n,prefix_proved=True,complete_finite_radial_prefix_upper=O.upper(total.sqrt()),
                    all_processed_frequency_and_strip_amplitude_upper=d['peak'],latest_read_head=gate(),
                    resumed_original_complete_prefix_receipt_sha256=a.resume_sha),f)
    return n,total,d['peak']


def numeric(a):
    check(os.environ.get('GITHUB_ACTIONS')=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
          and os.environ['GITHUB_RUN_ATTEMPT']=='1' and sys.version_info[:3]==(3,12,14)
          and all(version(k)==v for k,v in [('python-flint','0.9.0'),('numpy','2.3.5'),('scipy','1.17.0')]),'declared public science runtime')
    ctx.prec=320;gate()
    def read(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=a.repo)
    c,arr,major,nraw,ntail,outer,ids=receive(read)
    roots=tuple(map(Q,ROOT));pc=tuple(map(Q,PIECE));rlo,rhi=roots;length=rhi-CUT
    check(pc[0]<CUT<rlo<=rhi<pc[1] and 0<length<outer,'complete root/cut same original physical piece')
    bands=bandplan();plan=[(i,lo,hi) for i in range(RAD) for lo,hi in bands]
    base=dict(kind='R149_signed_genuine_complete_local_collar_operator_v1',event_commit=os.environ['GITHUB_SHA'],
              run=os.environ['GITHUB_RUN_ID'],attempt=1,plan_sha256=sha256(canonical(plan)).hexdigest(),
              root_interval=ROOT,cut=str(CUT),radial_slabs=RAD,angular_closed_cells=ANG,strip_width=str(O.WIDTH),
              finite_band_count=len(bands)-1,all_finite_input_labels=[97,STOP],infinite_amplitude_input_start=STOP+1,
              natural_rows=len(plan),whole_original_inputs=len(ids),whole_original_input_receipts_sha256=sha256(canonical(ids)).hexdigest(),
              old_numerators_read=11,old_scientific_targets_recomputed=0,signed_original_local_vectors=3,
              first_row_J_readback_bound_included=True,old_circle_nonlocal_remainder_included=False,full_physical_positive_correction_included=False,
              root_and_endpoint_physical_mismatch_included=False,full_high_inverse_proved=False)
    head=canonical(dict(plan=plan,original=ids,columns=['terminal_Ai','genuine_second'],coordinate='t=T/R; (Y,R*Y_T)'))
    a.private.mkdir(parents=True,exist_ok=True);p=a.private/'correlated-collar.bin.gz';out=Prefix(p,a.receipt,head,base)
    count,total,peak=resume(a,out,head,plan,base);matrix={};slab=None;record=None
    status=json.loads(a.receipt.read_bytes())
    try:
        for i,lo,hi in plan[count:]:
            gate()
            if slab!=i:
                rho=F.P.ex((rlo-CUT)*Q(i,RAD)).union(F.P.ex(length*Q(i+1,RAD)))
                geometry={w:list(G.geometry(arr,major,nraw,ntail[abs(w)],outer,rho,ANG,w)) for w in (O.WIDTH,-O.WIDTH,0)}
                slab=i
            co=matrix.get(lo)
            if co is None:co=F.scaled_potential(c,lo,hi);matrix[lo]=co
            packet=bytearray()
            if hi is None:
                record=integer_bounds(geometry[0],co,lo,packet)
            else:
                val,record=O.band_bound(geometry,co,lo,hi,ANG,packet)
                total=(total+F.P.ex(length/RAD)*val*val).upper()
            peak=[max(t,u) for t,u in zip(peak,record['signed_amplitude_upper'])]
            expected=ANG*(2*8 if hi is None else 2*2*23)*32
            check(len(packet)==expected,'complete original columns, signs, angular contours and Green entries')
            body=canonical(dict(radial_slab=i,band=[lo,hi],packet_bytes=len(packet),**record))
            out.append(L.pack(len(body))+body+packet);count+=1
            status=dict(base,completed_subpieces=count,prefix_proved=True,complete_finite_radial_prefix_upper=O.upper(total.sqrt()),
                        all_processed_frequency_and_strip_amplitude_upper=peak,latest_read_head=gate())
            man,exp=total.man_exp();out.commit(status,canonical(dict(count=count,plan=base['plan_sha256'],total_exact=[str(man),int(exp)],peak=peak)))
            if count==1 or count%8==0:print('GLC_PREFIX',count,len(plan),record,flush=True)
        check(count==len(plan) and (slab==RAD-1 or a.resume is not None),'complete finite bands and genuine infinite-amplitude tails')
    finally:out.close()
    data=p.read_bytes();unc=gzip.decompress(data)
    check((len(data),sha256(data).hexdigest(),len(unc),sha256(unc).hexdigest())==
          (out.csize,out.gz.hexdigest(),out.usize,out.raw.hexdigest()),'whole compressed and uncompressed natural source carrier')
    result=dict(status,complete=True,proved=True,private_bytes=len(data),private_whole_sha256=sha256(data).hexdigest(),
                private_uncompressed_bytes=len(unc),private_uncompressed_sha256=sha256(unc).hexdigest(),
                finite_local_density_Hminus4over3_to_L2dr_Hminus5over3_upper=O.upper(total.sqrt()),
                finite_local_density_below_one_hundredth=bool(total< F.P.ex(Q(1,10000))))
    natural=total.sqrt()*2*2039*F.P.ex(length).sqrt()*F.P.ex(Q(719,1000))
    physical=natural*F.P.ex(Q(124,10));direct=natural*F.P.ex(Q(10611,1000))*F.P.ex(Q(1061,1000))
    direct*=F.P.ex(Q(97**2+22**2,1000**2)).sqrt()/F.P.ex(Q(11,10))
    result.update(finite_original_first_row_Hminus2over3_L2dr_upper=O.upper(2*total.sqrt()),
                  finite_natural_terminal_to_physical_waist_upper=O.upper(natural),
                  finite_common_input_physical_C97_addend_upper=O.upper(physical),
                  finite_actual_ASQ16_high_addend_upper=O.upper(direct),
                  finite_physical_target_5p5_this_addend_only=bool(physical<F.P.ex(Q(11,2))),
                  old_GSF_overlap_on_this_same_region_must_be_counted_once=True)
    b=canonical(result);replace(a.receipt,b);print('GLC_COMPLETE',len(b),sha256(b).hexdigest(),b.decode().strip(),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--private',type=Path,required=True)
    p.add_argument('--receipt',type=Path,required=True);p.add_argument('--resume',type=Path);p.add_argument('--resume-sha')
    p.add_argument('--resume-directory',type=Path);a=p.parse_args()
    try:numeric(a)
    except Exception as exc:
        old=json.loads(a.receipt.read_bytes()) if a.receipt.exists() else dict(completed_subpieces=0,prefix_proved=False)
        old.update(complete=False,proved=False,failure=repr(exc),event_commit=os.environ.get('GITHUB_SHA'))
        replace(a.receipt,canonical(old));raise
