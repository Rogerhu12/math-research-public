"""Direct physical Laurent and diagonal Fourier-lag receiver for the whole finite collar."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from hashlib import sha256
from importlib.metadata import version
from pathlib import Path
import gzip,io,json,os,struct,subprocess,sys
from math import isfinite,nextafter,inf
from flint import arb,ctx
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_phase_original_inputs import CUT,check
from fourfold_codazzi_true_characteristic_seed_admission import ROOT,PIECE
from fourfold_codazzi_true_ratio_live_rules import canonical,gate
from fourfold_codazzi_true_ratio_prefix import Prefix,replace,record_failure
from fourfold_codazzi_collar_signed_inputs import receive
from fourfold_codazzi_collar_signed_laurent_enclosure import WIDTH,DEGREE
import fourfold_codazzi_collar_laurent_terminal as T
import fourfold_codazzi_collar_laurent_receiver as W

RAD=16
STOP=2**20
INDIVIDUAL=1023
WORD=struct.Struct('<I')
PAIR=struct.Struct('<dddd')
CARRIER='all-signed-physical-Laurent-rows.gz'


def up(z):
    u=nextafter(float(z.upper()),inf);check(isfinite(u) and u>=0,'finite public upper')
    return u


def bands():
    lo=97;out=[]
    for edge,ratio in [(INDIVIDUAL,Q(9,8)),(4096,Q(5,4)),(STOP,Q(3,2))]:
        while lo<=edge:
            hi=min(edge,int(lo*ratio));out.append((lo,hi));lo=hi+1
    return out


def enc(v):
    if isinstance(v,(list,tuple)):return [enc(t) for t in v]
    return up(v)


def dec(v):
    return [dec(t) for t in v] if isinstance(v,list) else arb(v)


def limits(z):
    pair=[]
    for t in (z.real,z.imag):pair.extend((nextafter(float(t.lower()),-inf),nextafter(float(t.upper()),inf)))
    check(all(map(isfinite,pair)),'complete private signed coefficient')
    return pair


def frame(data):return WORD.pack(len(data))+data


def read_frame(f):
    n,=WORD.unpack(f.read(4));d=f.read(n)
    check(0<n<2000000 and len(d)==n,'whole saved natural row')
    return d


def aggregate(a,b):return W.merge(a,b)


def state0():
    return dict(blocks=[W.zero(),W.zero()],individual=[arb(0)]*(INDIVIDUAL-96),
                l1=[arb(0),arb(0)],l2=[arb(0),arb(0)],core_l1=[arb(0),arb(0)])


def partial(base,sums,at):
    natural=[exact(Q(719,1000))*2039*2*v for v in sums['l1']]
    return dict(base,completed_subpieces=at,prefix_proved=at>0,
        full_completed_slab_integral_L1=enc(sums['l1']),natural_waist_L1=enc(natural),
        root_common_C97_addends=enc([exact(Q(62,5))*v for v in natural]),
        half_read_and_original_gauge_included=True)


def restore(a,pr,head,base,plan):
    if not a.resume:return 0,state0()
    rec=a.resume.read_bytes();check(sha256(rec).hexdigest()==a.resume_sha,'full prior receipt')
    r=json.loads(rec);n=r['completed_subpieces'];check(not r['complete'] and 0<n<=len(plan) and
        r['plan_sha256']==base['plan_sha256'] and r['whole_original_inputs_sha256']==base['whole_original_inputs_sha256'],
        'same entire input and original finite plan')
    data=(a.resume_dir/CARRIER).read_bytes()[:r['private_prefix_bytes']]
    raw=gzip.decompress(data)
    check((len(data),sha256(data).hexdigest(),len(raw),sha256(raw).hexdigest())==tuple(r[k]
          for k in ('private_prefix_bytes','private_prefix_sha256','private_prefix_uncompressed_bytes',
                    'private_prefix_uncompressed_sha256')),'entire confirmed signed prefix')
    f=io.BytesIO(raw);check(read_frame(f)==head,'same signed carrier convention')
    for i in range(n):
        chunk=read_frame(f);row=io.BytesIO(chunk);hdr=json.loads(read_frame(row))
        check(hdr['group']==list(plan[i]) and len(row.read())==hdr['coefficient_bytes'],'same full original physical row')
        pr.append(frame(chunk))
    check(not f.read(1) and pr.gz.hexdigest()==r['private_prefix_sha256'],'restored entire original prefix')
    z=(a.resume_dir/r['continuation_file']).read_bytes();u=gzip.decompress(z)
    check((len(z),sha256(z).hexdigest(),len(u),sha256(u).hexdigest())==tuple(r[k] for k in
          ('continuation_bytes','continuation_sha256','continuation_uncompressed_bytes','continuation_uncompressed_sha256')),
          'whole preceding private frontier')
    frontier=json.loads(u)
    check(frontier['count']==n and frontier['plan']==base['plan_sha256'],'same physical frontier')
    st={k:dec(v) for k,v in frontier['state'].items()}
    pr.commit(partial(base,st,n),u)
    return n,st


def numeric(a):
    check(os.environ['GITHUB_ACTIONS']=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
          and os.environ['GITHUB_RUN_ATTEMPT']=='1' and sys.version_info[:3]==(3,12,14)
          and {k:version(k) for k in ('python-flint','numpy','scipy')}==
             {'python-flint':'0.9.0','numpy':'2.3.5','scipy':'1.17.0'},'single first public science entry')
    ctx.prec=320;gate()
    def read(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=a.repo)
    c,arr,major,num,tail,outer,ids=receive(read)
    lo_root,hi_root=map(Q,ROOT);pc=tuple(map(Q,PIECE));length=hi_root-CUT;step=exact(length/RAD)
    check(pc[0]<CUT<lo_root<=hi_root<pc[1] and length<outer and len(ids)==112,
          'all unrepeated historical inputs and full physical collar')
    levels=bands();plan=[(r,lo,hi) for r in range(RAD) for lo,hi in levels]
    base=dict(kind='R149_finite_full_physical_Laurent_lags_and_projected_root_source',run=os.environ['GITHUB_RUN_ID'],
         attempt=1,event_commit=os.environ['GITHUB_SHA'],physical_root=ROOT,cut=str(CUT),finite_inputs=[97,STOP],
         individual_natural_waist_columns=[97,INDIVIDUAL],physical_output_zero_exactly_removed=True,
         reference_columns=['terminal_Ai_only','two_independent_reference_inputs'],degree=DEGREE,strip=str(WIDTH),
         radial_slabs=RAD,frequency_groups=len(levels),natural_rows=len(plan),plan_sha256=sha256(canonical(plan)).hexdigest(),
         whole_original_inputs_sha256=sha256(canonical(ids)).hexdigest(),old_scientific_targets_recomputed=0,
         old_GLC_green_carrier_consumed=False,complete_nonlocal_or_endpoint_or_positive_response_claimed=False)
    head=canonical(dict(plan=plan,original=ids,signs=[1,-1],columns=['terminal_Ai','Bi'],
        lag_limits=[-DEGREE,DEGREE],signed_coefficient_type='little endian f64 real and imaginary directed endpoints',
        removed_unit='exp(i*sign*n*true real finite Taylor mean of chi), per input and radius',
        frontier='outward running whole input/signed-lag sums and all actual terminal columns'))
    a.private.mkdir(parents=True,exist_ok=True);p=a.private/CARRIER;pr=Prefix(p,a.receipt,head,base)
    st=None;last=None
    try:
        n,st=restore(a,pr,head,base,plan)
        for r,lo,hi in plan[n:]:
            gate()
            if last!=r:
                rho=exact((lo_root-CUT)*Q(r,RAD)).union(exact(length*Q(r+1,RAD)))
                g=T.geometry(arr,major,num,tail[WIDTH],outer,rho);last=r
            rows,caps=T.rows(g,c,lo,hi);weights=W.compress(rows)
            budget=[]
            for sel,single in enumerate((True,False)):
                b=W.band(weights,lo,hi,single);budget.append(W.full_cost(b))
                st['blocks'][sel]=aggregate(st['blocks'][sel],b)
            indiv=[]
            if hi<=INDIVIDUAL:
                for j in range(lo,hi+1):
                    cj=W.full_cost(W.band(weights,j,j,True));indiv.append(up(cj))
                    st['individual'][j-97]=(st['individual'][j-97]+step*cj).upper()
            if hi==STOP:
                for sel,block in enumerate(st['blocks']):
                    fee=W.full_cost(block);st['l1'][sel]=(st['l1'][sel]+step*fee).upper()
                    st['l2'][sel]=(st['l2'][sel]+step*fee**2).upper()
                    st['core_l1'][sel]=(st['core_l1'][sel]+step*sum(block[0],arb(0))).upper()
                st['blocks']=[W.zero(),W.zero()]
            body=bytearray()
            for pair in rows:
                for field in pair:
                    for h in range(-DEGREE,DEGREE+1):body.extend(PAIR.pack(*limits(field.coeff(h))))
            hdr=dict(group=[r,lo,hi],symbol_error_caps=enc([[v.error for v in pair] for pair in rows]),
                 amplitude_and_phase_caps=enc(caps),removed_chi_finite_mean=limits(g['chi'].coeff(0)),
                 joint_weighted_group=enc(budget),individual_lower_input=lo if indiv else None,
                 individual_Hminus5over3_upper=indiv,coefficient_bytes=len(body))
            pr.append(frame(frame(canonical(hdr))+body));n+=1
            frontier=canonical(dict(count=n,plan=base['plan_sha256'],state={k:enc(v) for k,v in st.items()}))
            pr.commit(partial(base,st,n),frontier)
            if n%16==0:print('GLW_COMPLETE_PREFIX',n,base['natural_rows'],flush=True)
    finally:pr.close()
    b=p.read_bytes();u=gzip.decompress(b);d=partial(base,st,n)
    check(n==len(plan) and len(b)==pr.csize and sha256(b).hexdigest()==pr.gz.hexdigest()
          and len(u)==pr.usize and sha256(u).hexdigest()==pr.raw.hexdigest() and len(u)<180_000_000,
          'entire complete physical-signed carrier and frequency shift field read back')
    coef=exact(Q(719,1000))*2039*2
    columns=canonical(dict(input_labels=[97,INDIVIDUAL],reference='true terminal Ai',original_signed_norm='natural H^-4/3',
                        role='per single natural input to physical waist before common right normalizers',
                        physical_waist_uppers=enc([coef*x for x in st['individual']])))
    cp=a.private/'complete-terminal-Ai-individual-columns.json';replace(cp,columns);check(cp.read_bytes()==columns,'entire terminal-column carrier')
    d.update(complete=True,proved=True,L2dr_Hminus5over3=enc([z.sqrt() for z in st['l2']]),core_L1=enc(st['core_l1']),
         natural_terminal_max_single_column=up(coef*max(st['individual'])),individual_column_bytes=len(columns),
         individual_column_sha256=sha256(columns).hexdigest(),private_bytes=len(b),private_sha256=sha256(b).hexdigest(),
         private_uncompressed_bytes=len(u),private_uncompressed_sha256=sha256(u).hexdigest(),
         terminal_physical_below_5p5=d['root_common_C97_addends'][0]<5.5,last_read_head=gate())
    replace(a.receipt,canonical(d));print('GLW_WHOLE_RECEIPT',canonical(d).decode().strip(),flush=True)


if __name__=='__main__':
    ap=ArgumentParser()
    for n in ('repo','private','receipt'):ap.add_argument('--'+n,required=True,type=Path)
    ap.add_argument('--resume',type=Path);ap.add_argument('--resume-sha');ap.add_argument('--resume-dir',type=Path)
    a=ap.parse_args()
    try:
        check(bool(a.resume)==bool(a.resume_sha)==bool(a.resume_dir),'complete prior prefix identity')
        numeric(a)
    except Exception as exc:
        record_failure(a.receipt,exc)
        raise
