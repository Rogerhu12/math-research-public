"""All integer input labels beyond the finite collar calculation, with the full G.8 source."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from importlib.metadata import version
import argparse,gzip,json,os,struct,subprocess,sys
from flint import arb,ctx
import fourfold_codazzi_infinite_collar_symbol as S
import fourfold_codazzi_collar_signed_geometry as G
import fourfold_codazzi_collar_signed_operator as O
from fourfold_codazzi_collar_signed_inputs import receive
from fourfold_codazzi_true_characteristic_seed_admission import ROOT,PIECE
from fourfold_codazzi_true_phase_original_inputs import CUT,check
from fourfold_codazzi_true_ratio_live_rules import canonical,gate
from fourfold_codazzi_true_ratio_prefix import Prefix,replace

RAD=4;ANG=128;SIZE=struct.Struct('<I')

def resume(a,out,head,base):
    if a.resume is None:return 0,arb(0)
    import io
    b=a.resume.read_bytes();check(len(b)<100000 and sha256(b).hexdigest()==a.resume_sha,'original whole infinite collar prefix receipt')
    d=json.loads(b);n=d['completed_subpieces']
    check(not d['complete'] and d['prefix_proved'] and 0<n<=RAD and
          all(d[k]==base[k] for k in ('kind','plan_sha256','whole_inputs_sha256','input_floor','angular_bins','signed_frequency_disk')),
          'same entire infinite physical source plan')
    z=(a.resume_directory/'infinite-collar.bin.gz').read_bytes()[:d['private_prefix_bytes']];raw=gzip.decompress(z)
    check((len(z),sha256(z).hexdigest(),len(raw),sha256(raw).hexdigest())==tuple(d[k] for k in
          ('private_prefix_bytes','private_prefix_sha256','private_prefix_uncompressed_bytes','private_prefix_uncompressed_sha256')),
          'complete confirmed infinite collar private original')
    f=io.BytesIO(raw);k,=SIZE.unpack(f.read(4));check(f.read(k)==head,'same authenticated original header')
    for i in range(n):
        hh=f.read(4);k,=SIZE.unpack(hh);bb=f.read(k);row=json.loads(bb);pp=f.read(row['bytes'])
        check(row['radial_index']==i and len(pp)==row['bytes']==4*ANG*11*32,'same qualified complete previous slab')
        out.append(hh+bb+pp)
    check(not f.read(1) and out.gz.hexdigest()==d['private_prefix_sha256'] and out.raw.hexdigest()==d['private_prefix_uncompressed_sha256'],
          'each resumed whole old natural infinite slab copied byte-for-byte')
    z=(a.resume_directory/d['continuation_file']).read_bytes();v=gzip.decompress(z)
    check((len(z),sha256(z).hexdigest(),len(v),sha256(v).hexdigest())==tuple(d[k] for k in
          ('continuation_bytes','continuation_sha256','continuation_uncompressed_bytes','continuation_uncompressed_sha256')),
          'entire directed mass state')
    state=json.loads(v);check(state['count']==n and state['plan']==base['plan_sha256'],'same signed infinite frontier')
    m,e=state['total'];x=S.P.ex(Q(int(m))*Q(2)**int(e));check(x.is_exact() and x>=0,'confirmed original directed mass')
    out.commit(dict(base,completed_subpieces=n,prefix_proved=True,partial_ordinary_bound=O.upper(x.sqrt()),
                    resumed_whole_prefix_sha256=a.resume_sha),v)
    return n,x


def run(a):
    check(os.environ.get('GITHUB_ACTIONS')=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
          and os.environ['GITHUB_RUN_ATTEMPT']=='1' and sys.version_info[:3]==(3,12,14)
          and all(version(k)==v for k,v in [('python-flint','0.9.0'),('numpy','2.3.5'),('scipy','1.17.0')]),'declared public only')
    ctx.prec=320;gate()
    def read(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=a.repo)
    c,arr,major,raw,ntail,outer,ids=receive(read);rl,rh=map(Q,ROOT);length=rh-CUT
    check(Q(PIECE[0])<CUT<rl<=rh<Q(PIECE[1]) and 0<length<outer,'complete genuine collar support')
    plan=[(str(Q(i,RAD)),str(Q(i+1,RAD))) for i in range(RAD)]
    base=dict(kind='R149_all_infinite_collar_genuine_signed_G8_v1',plan_sha256=sha256(canonical(plan)).hexdigest(),
              run=os.environ['GITHUB_RUN_ID'],attempt=1,event_commit=os.environ['GITHUB_SHA'],input_floor=S.N,
              angular_bins=ANG,strip_width=str(S.WIDTH),signed_frequency_disk=str(S.XI),physical_root_interval=ROOT,
              cut=str(CUT),whole_inputs_sha256=sha256(canonical(ids)).hexdigest(),whole_input_count=len(ids),
              old_numerators_read=11,old_scientific_targets_recomputed=0,complete_high_bvp_proved=False,
              both_genuine_reference_columns=True,all_physical_fourier_outputs=True,full_crossing_means_in_evolution=True,
              physical_projection_on_final_local_scalar_only=True,finite_input_and_infinite_input_disjoint=True)
    a.private.mkdir(parents=True,exist_ok=True);path=a.private/'infinite-collar.bin.gz'
    head=canonical(dict(original=ids,plan=plan,packet=['T','V','V_T','B','B_T','B_TT','x/Delta','y(T-xi^2 V)/Delta',
                                                       'y/Delta','signed joint first amplitude','signed joint second amplitude']))
    out=Prefix(path,a.receipt,head,base);count,total=resume(a,out,head,base);status=json.loads(a.receipt.read_bytes())
    try:
        co=S.zero_frequency_germ(c)
        for i in range(count,RAD):
            gate();rho=S.P.ex((rl-CUT)*Q(i,RAD)).union(S.P.ex(length*Q(i+1,RAD)))
            gs={w:list(G.geometry(arr,major,raw,ntail[abs(w)],outer,rho,ANG,w)) for w in (S.WIDTH,-S.WIDTH)}
            packed=bytearray();val,M,h,k,num=S.packet(gs,co,lambda z:O.append_box(packed,z))
            check(len(packed)==num*11*32 and num==4*ANG,'complete private signed physical frequency-disk packet')
            row=dict(radial_index=i,bytes=len(packed),complete_infinite_Hminus5over3_upper=O.upper(val),
                     full_weighted_B=O.upper(h),interpolation_factor_squared_order=O.upper(k),symbol_component_upper=list(map(O.upper,M)))
            body=canonical(row);gate();out.append(SIZE.pack(len(body))+body+packed);count=i+1
            total=(total+S.P.ex(length/RAD)*val*val).upper();m,e=total.man_exp()
            status=dict(base,completed_subpieces=count,prefix_proved=True,partial_ordinary_bound=O.upper(total.sqrt()),last_read_head=gate())
            out.commit(status,canonical(dict(count=count,total=[str(m),int(e)],plan=base['plan_sha256'])))
            print('GIC_NATURAL_SLAB',count,row,flush=True)
    finally:out.close()
    z=path.read_bytes();u=gzip.decompress(z)
    check(count==RAD and (len(z),sha256(z).hexdigest(),len(u),sha256(u).hexdigest())==
          (out.csize,out.gz.hexdigest(),out.usize,out.raw.hexdigest()),'full compressed and uncompressed complete infinite carrier')
    E=total.sqrt();natural=2*2039*S.P.ex(length).sqrt()*S.P.ex(Q(719,1000))*E
    physical=natural*S.P.ex(Q(124,10));hi=natural*S.P.ex(Q(10611,1000))*S.P.ex(Q(1061,1000))*S.P.ex(Q(97**2+22**2,1000**2)).sqrt()/S.P.ex(Q(11,10))
    result=dict(status,complete=True,proved=True,private_bytes=len(z),private_sha256=sha256(z).hexdigest(),
                private_uncompressed_bytes=len(u),private_uncompressed_sha256=sha256(u).hexdigest(),
                infinite_local_original_density_ordinary_Hminus5over3_upper=O.upper(E),
                infinite_first_row_J_ordinary_Hminus2over3_upper=O.upper(2*E),
                infinite_natural_to_physical_waist_upper=O.upper(natural),infinite_common_C97_addend_upper=O.upper(physical),
                infinite_ASQ16_high_addend_upper=O.upper(hi),infinite_local_physical_below_5p5=bool(physical<S.P.ex(Q(11,2))),
                full_positive_feedback_included=False,complete_nonlocal_mean_and_physical_endpoint_mismatches_included=False)
    b=canonical(result);replace(a.receipt,b);print('GIC_COMPLETE',len(b),sha256(b).hexdigest(),b.decode().strip(),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--private',type=Path,required=True)
    p.add_argument('--receipt',type=Path,required=True);p.add_argument('--resume',type=Path);p.add_argument('--resume-directory',type=Path)
    p.add_argument('--resume-sha');a=p.parse_args()
    try:run(a)
    except Exception as exc:
        prior=json.loads(a.receipt.read_bytes()) if a.receipt.exists() else dict(completed_subpieces=0,prefix_proved=False)
        prior.update(complete=False,proved=False,failure=repr(exc),event_commit=os.environ.get('GITHUB_SHA'))
        replace(a.receipt,canonical(prior));raise
