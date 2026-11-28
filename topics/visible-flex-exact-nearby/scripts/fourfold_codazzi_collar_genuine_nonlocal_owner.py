"""GNF. First complete finite genuine nonlocal collar and physical-mean column receiver."""
from argparse import ArgumentParser
from copy import copy
from fractions import Fraction as Q
from hashlib import sha1, sha256
from importlib.metadata import version
from math import inf, isfinite, nextafter
from multiprocessing import get_context
from pathlib import Path
from time import monotonic
import gzip
import io
import json
import os
import platform
import struct
import subprocess
import sys

from flint import acb, arb, ctx
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_phase_original_inputs import CUT, check
from fourfold_codazzi_true_characteristic_seed_admission import ROOT, PIECE
from fourfold_codazzi_true_ratio_live_rules import canonical, gate
from fourfold_codazzi_true_ratio_prefix import Prefix, record_failure, replace
from fourfold_codazzi_collar_signed_inputs import receive
from fourfold_codazzi_collar_signed_background_jets import original_majorants, field
from fourfold_codazzi_collar_signed_laurent_enclosure import WIDTH, DEGREE
from fourfold_codazzi_collar_genuine_nonlocal_columns import geometry, physical_inputs
from fourfold_codazzi_genuine_two_circle_residual_words import Words
from fourfold_codazzi_genuine_reflected_circle_inverse import ReflectedInverse
import fourfold_codazzi_genuine_physical_mean_adjoint as adjoint_mean
from fourfold_codazzi_physical_shifted_circle_backend import Backend
import fourfold_codazzi_physical_shifted_circle_receiver as receiver


RAD = 16
STOP = 2**20
SINGLE = 128
WINDOWS = (Q(5,3), Q(2,3))
MODES = ('terminal_Ai', 'both_reference_columns')
ORIGINAL = '8c7e3995ea38d81af07a664866d9e6fd34735f29e1cb3a04ee5c9b9d59e71763'
NATIVE = 'whole-nonlocal-and-physical-mean.bin.gz'
JCR = '73907a2fb13c0db588e599d5ce8b0c3e83760b29c75d9c11b2fdc0e245e53a00'
MAX_RAW = 240_000_000
MAX_RSS = 14 << 30
MAX_WALL = 19_100
SIZE = struct.Struct('<I')
RECT = struct.Struct('<dddd')
SLAB = None


def plan_bands():
    bands = [(j,j) for j in range(97,SINGLE+1)]
    lo = SINGLE+1
    for end,ratio in ((1023,Q(9,8)),(4096,Q(5,4)),(STOP,Q(3,2))):
        while lo<=end:
            hi=min(end,int(lo*ratio)); bands.append((lo,hi)); lo=hi+1
    check(bands[0]==(97,97) and bands[-1][1]==STOP and all(v[1]+1==w[0] for v,w in zip(bands,bands[1:])),
          'complete original finite labels and separate physical-zero exceptions')
    return bands


def up(x):
    z=nextafter(float(arb(x).upper()),inf)
    check(isfinite(z) and z>=0,'finite outward upper')
    return z


def low(x):
    z=nextafter(float(arb(x).lower()),-inf)
    check(isfinite(z),'finite outward lower')
    return z


def box(z):
    out=tuple(y for a in (z.real,z.imag) for y in (low(a),nextafter(float(a.upper()),inf)))
    check(all(map(isfinite,out)),'full finite signed row')
    return out


def encode(x):
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return up(x)


def decode(x):
    if isinstance(x,dict):return {k:decode(v) for k,v in x.items()}
    if isinstance(x,list):return [decode(v) for v in x]
    return arb(x)


def frame(data):return SIZE.pack(len(data))+data


def read_frame(f):
    first=f.read(SIZE.size);check(len(first)==SIZE.size,'complete private frame header')
    size,=SIZE.unpack(first);check(0<size<1_000_000,'bounded complete natural frame')
    data=f.read(size);check(len(data)==size,'whole complete private frame');return data


def verify_config(a):
    raw=a.manifest.read_bytes();check(sha256(raw).hexdigest()==a.manifest_sha,'entire new manifest')
    m=json.loads(raw);check(m['kind']=='R149_GNF_finite_nonlocal_original_columns_v1' and m['old_original_receipts_sha256']==ORIGINAL
        and m['root_interval']==list(ROOT) and m['physical_cut']==str(CUT) and m['inputs']==[97,STOP]
        and m['radial_slabs']==RAD and m['individually_split_through']==SINGLE and m['angular_strip']==str(WIDTH)
        and m['output_windows']==['-5/3','-2/3','scalar'] and m['old_target_calls']==0,'actual complete physical input plan')
    for s in m['files']:
        data=(a.repo/s['path']).read_bytes()
        check((len(data),sha256(data).hexdigest(),sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())==
              (s['bytes'],s['sha256'],s['git_blob_sha']),'actual whole manifest file '+s['path'])
    check(len({s['path'] for s in m['files']})==len(m['files']) and
          [s['sha256'] for s in m['files'] if s['path'].endswith('/'+Path(__file__).name)]==[sha256(Path(__file__).read_bytes()).hexdigest()],
          'one exact GNF owner and distinct complete closure')
    jcr=[s for s in m['files'] if s['sha256']==JCR]
    check(len(jcr)==1 and jcr[0]['bytes']==1796,'the complete actual root-circle consequence')
    paid=json.loads((a.repo/jcr[0]['path']).read_bytes())
    check(paid['proved'] and len(paid['checks'])==20 and all(paid['checks'].values()) and paid['real_full_negative_D_lower']=='0.785'
          and paid['corrected_full_A3_radius']=='1e-7','actual JCR paid whole-circle denominator')
    return m


def resources(start):
    elapsed=monotonic()-start
    check(elapsed<MAX_WALL,'current public scientific wall limit with confirmed natural prefix')
    mem=Path('/sys/fs/cgroup/memory.current')
    if mem.is_file():check(int(mem.read_text())<MAX_RSS,'current whole cgroup memory budget')
    affinity=len(os.sched_getaffinity(0));n=affinity;cpu=Path('/sys/fs/cgroup/cpu.max')
    if cpu.is_file():
        quota,period=cpu.read_text().split()
        if quota!='max':n=min(n,max(1,int(quota)//int(period)))
    n=min(n,4);check(n>=1,'runner allowed scientific CPUs')
    return n


def original_inputs(a):
    def read(commit,path):
        return subprocess.check_output(['git','show',commit+':'+path],cwd=a.repo)
    c,arr,major,_,_,old_outer,receipts=receive(read)
    check(len(receipts)==112 and sha256(canonical(receipts)).hexdigest()==ORIGINAL,
          'all 112 original whole inputs match the completed original receiver inventory exactly')
    bounds=original_majorants(read,receipts)
    return c,arr,major,bounds,old_outer,receipts


def physical_background(c,bounds,rho):
    def f(name,r=0,p=0):return field(c,bounds,name,rho,r,p)
    def scalar(name,r=0):
        z=f(name,r);check(z.error==0 and len(z.p)<=1 and (not len(z.p) or z.lo==0),
                          'true angularly radial scalar '+name)
        v=z.coeff(0);check(v.imag.contains(0),'real physical scalar '+name);return v.real
    return dict(u=f('u'),v=f('v'),d=f('d'),u_phi=f('u',p=1),v_phi=f('v',p=1),d_phi=f('d',p=1),
        u_phiphi=f('u',p=2),v_phiphi=f('v',p=2),u_r=f('u',1),v_r=f('v',1),v_rphi=f('v',1,1),
        beta=scalar('beta'),beta_r=scalar('beta',1),K=scalar('K'),K_r=scalar('K',1),eta=scalar('eta'),eta_r=scalar('eta',1))


def qualified_background(circle,words):
    # The immutable WUA.1--8/JI family is real and reflected on this complete
    # original slab. Both signed representations use the exact same coefficients.
    return (circle['original_sha']==ORIGINAL and 0<=circle['slab']<RAD and circle['root']==list(ROOT)
            and circle['cut']==str(CUT) and words.b.real_ball(words.eta).lower()>0)


class SameCircleJCR(ReflectedInverse):
    """JI.11 at a single actual collar slab using both independent bounds on D.

    The inherited linear expression is unchanged. This coefficient initializer
    differs from the standalone unqualified initializer only in intersecting
    the real mean with the separately admitted JCR estimate on this circle.
    """
    def __init__(self,b,w,circle):
        check(w.b is b and qualified_background(circle,w) and circle['JCR']==JCR,
              'identical original affine reflected collar on the paid JCR domain')
        eta=b.real_ball(w.eta);alpha=2*w.beta/eta
        iv=b.coeff_I(w.v);ell=b.scale(alpha,b.coeff_I(w.u*w.v))
        a=b.coeff_exp(b.scale(-1,ell));ainv=b.coeff_exp(ell)
        positive=b.constant(1)-b.scale(alpha,w.u*iv)
        raw=b.real_ball(b.coeff_Pi(a*positive));floor=exact(Q(785,1000)).lower()
        check(raw.is_finite() and raw.upper()>=floor,'directed new D intersects the authentic JCR enclosure')
        D=raw.intersection(floor.union(raw.upper()))
        check(D.is_finite() and D.lower()>0,'same true physical denominator separated from zero')
        self.b,self.words,self.circle=b,w,circle
        self.a,self.ainv,self.iv,self.eta,self.alpha=a,ainv,iv,eta,alpha
        self.c_weight=a*w.u;self.mean_source=b.scale(-1,positive);self.D=D;self.raw_D=raw


def bind_coefficients(w0,j0,lo,hi,sign):
    # All entries constructed in Words.__init__ and the JI initializer are
    # unshifted coefficient fields or radial scalars. Only applications of a
    # word or JI.11 to a Column use the new physical input-frequency label.
    b=Backend(lo,hi,sign);w=copy(w0);w.b=b
    inverse=copy(j0);inverse.b=b;inverse.words=w
    return w,inverse


def paired_sources(rows,words,inverses,weights,ref):
    # A real WUA reflected input uses its +/- physical coordinates together.
    # For each original reference column both signed components must exist,
    # with the same removed input unit consistently used in both J calls.
    # The JI.11 linear extension is evaluated on summands of that pair. On
    # their physical reflected sum the result is the original inverse. The
    # later independent-sign operator norm is a valid upper for this restriction.
    check(len(rows)==2 and all(len(q)==2 for q in rows) and
          [w.b.sign for w in words]==[1,-1] and all(w.b.lo==words[0].b.lo and w.b.hi==words[0].b.hi for w in words)
          and inverses[0].circle==inverses[1].circle,'same original reflected pair at both inverse applications')
    d=[w.known_rhs(**rows[k][ref]) for k,w in enumerate(words)]
    check(all(x['e'].mean_zero for x in d),'first true projected even source on the full reflected pair')
    v=[inv._signed_formula(x['e']) for inv,x in zip(inverses,d)]
    k=[w.b.add(x['Kw'],w.b.scale(-1,w.RQ(y))) for w,x,y in zip(words,d,v)]
    # All five physical rank vectors in K_w are P of physical coefficient
    # fields. Their zero means hold algebraically even when Field boxes
    # do not encode that exact identity. Apply the actual P explicitly.
    g1=[inv._signed_formula(w.b.P(z)) for inv,w,z in zip(inverses,words,k)]
    g2=[]
    for sign_index,(w,x,y) in enumerate(zip(words,d,v)):
        b=w.b
        mean=b.add(b.Pi(b.mul(w.u,b.add(x['h'],y))),b.scale(w.K,b.Pi(b.mul(w.v_minus_m,x['f']))))
        direct=b.scale(2*w.beta*w.m,mean)
        three=adjoint_mean.signed_readout(w,weights,rows[sign_index][ref])
        check(direct.real.overlaps(three.real) and direct.imag.overlaps(three.imag),
              'full direct and full adjoint signed physical means enclose the same true scalar')
        g2.append(acb(direct.real.intersection(three.real),direct.imag.intersection(three.imag)))
    return g1,g2


def evaluate_group(group):
    r,lo,hi=group;c,g,bg,w0,j0,weights=SLAB
    check(r==j0.circle['slab'],'the same physical-r slab for every signed input')
    words,inverses=zip(*(bind_coefficients(w0,j0,lo,hi,sign) for sign in (1,-1)))
    rows,removed=physical_inputs(c,g,bg['v'],bg['v_phi'],bg['eta'],lo,hi)
    outputs=[paired_sources(rows,words,inverses,weights,ref) for ref in (0,1)]
    first=[[outputs[ref][0][sign] for ref in range(2)] for sign in range(2)]
    second=[[outputs[ref][1][sign] for ref in range(2)] for sign in range(2)]
    budgets={}
    for count,name in enumerate(MODES,1):
        v=[row[:count] for row in first];means=[row[:count] for row in second]
        budgets[name]=dict(g1=[receiver.band(v,lo,hi,p) for p in WINDOWS],g2_squared=receiver.scalar_band(means,lo,hi))
    body=bytearray();errors=[]
    for i,(cols,means) in enumerate(zip(first,second)):
        er=[]
        for col,mean in zip(cols,means):
            for f in (col.oscillatory,col.physical):
                for h in range(-DEGREE,DEGREE+1):body.extend(RECT.pack(*box(f.coeff(h))))
            body.extend(RECT.pack(*box(mean)));er.append([up(col.oscillatory.error),up(col.physical.error)])
        errors.append(er)
    # Transfer only outward f64/bytes between processes. Never pickle an Arb object.
    hdr=dict(group=list(group),field_error_uppers=errors,physical_g1_part_orders=['oscillatory','independent_physical'],
        raw_D=[low(j0.raw_D),up(j0.raw_D)],genuine_D_lower=min(low(z.D) for z in inverses),genuine_D_upper=max(up(z.D) for z in inverses),
        removed_common_phase_finite_mean=box(removed),budgets=encode(budgets),coefficient_bytes=len(body))
    return frame(canonical(hdr))+body


def state0():
    return {name:dict(g1=[receiver.zero() for _ in WINDOWS],g2_squared=arb(0),
        integral_L1=[arb(0)]*3,integral_L2_squared=[arb(0)]*3,
        joint_L1=[arb(0)]*2,joint_L2_squared=[arb(0)]*2) for name in MODES}


def incorporate(state,header,step):
    r,lo,hi=header['group']
    for name in MODES:
        entry=state[name];z=decode(header['budgets'][name]);cost=[]
        entry['g1']=[receiver.merge(a,b) for a,b in zip(entry['g1'],z['g1'])]
        entry['g2_squared']=(entry['g2_squared']+z['g2_squared']).upper()
        if hi!=STOP:continue
        cost=[receiver.full_cost(b) for b in entry['g1']]+[entry['g2_squared'].sqrt().upper()]
        for i,fee in enumerate(cost):
            entry['integral_L1'][i]=(entry['integral_L1'][i]+step*fee).upper()
            entry['integral_L2_squared'][i]=(entry['integral_L2_squared'][i]+step*fee**2).upper()
        for i in range(len(WINDOWS)):
            value=(cost[i]**2+cost[-1]**2).upper()
            entry['joint_L1'][i]=(entry['joint_L1'][i]+step*value.sqrt()).upper()
            entry['joint_L2_squared'][i]=(entry['joint_L2_squared'][i]+step*value).upper()
        entry['g1']=[receiver.zero() for _ in WINDOWS];entry['g2_squared']=arb(0)


def summary(base,state,count,completed_slabs,dmin):
    result={}
    for name,entry in state.items():
        true_mixed=entry['joint_L1'][1]
        waist=(2039*true_mixed).upper();natural=(exact(Q(719,1000))*waist).upper()
        result[name]=dict(actual_PW_full_mixed_atom_L1=up(waist),physical_natural_waist_L1=up(natural),
                          common_input_waist_L1=up(exact(Q(62,5))*natural),L1_rows=encode(entry['integral_L1']),L2_rows=encode([x.sqrt() for x in entry['integral_L2_squared']]),
                          joint_L1=encode(entry['joint_L1']),joint_L2=encode([x.sqrt() for x in entry['joint_L2_squared']]))
    return dict(base,completed_subpieces=count,completed_radial_slabs=completed_slabs,
        prefix_proved=count>0,genuine_min_D_lower_on_saved_groups=dmin,physical_outputs_through_completed_slabs=result)


def row_header(chunk,group):
    f=io.BytesIO(chunk);h=json.loads(read_frame(f))
    count=4*(2*(2*DEGREE+1)+1)*RECT.size
    check(h['group']==list(group) and h['coefficient_bytes']==count==len(f.read())
          and len(h['field_error_uppers'])==2 and all(len(z)==2 for z in h['field_error_uppers'])
          and set(h['budgets'])==set(MODES) and h['genuine_D_lower']>0,
          'entire four-signed-column natural record and positive actual scalar')
    return h


def verified_stream(file,expected_compressed,expected_raw):
    total=0;dz=sha256()
    with file.open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''):dz.update(chunk);total+=len(chunk)
    check((total,dz.hexdigest())==expected_compressed,'whole private compressed carrier')
    size=0;dr=sha256()
    with gzip.open(file,'rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''):dr.update(chunk);size+=len(chunk)
    check((size,dr.hexdigest())==expected_raw,'whole private uncompressed carrier')


def restore(a,pr,head,base,plan):
    if not a.resume:return 0,0,None,state0()
    old=a.resume.read_bytes();check(sha256(old).hexdigest()==a.resume_sha,'entire original terminal scientific prefix')
    pref=json.loads(old);n=pref['completed_subpieces']
    check(not pref['complete'] and not pref['proved'] and pref['prefix_proved'] and 0<n<=len(plan)
        and pref['kind']==base['kind'] and pref['whole_112_original_identity']==ORIGINAL
        and pref['manifest_sha256']==base['manifest_sha256'] and pref['plan_sha256']==base['plan_sha256'],
        'same complete original configuration and still unpaid remaining cells')
    native=a.resume_dir/NATIVE
    verified_stream(native,(pref['private_prefix_bytes'],pref['private_prefix_sha256']),
                    (pref['private_prefix_uncompressed_bytes'],pref['private_prefix_uncompressed_sha256']))
    with gzip.open(native,'rb') as f:
        check(read_frame(f)==head,'same whole old private header')
        for group in plan[:n]:
            chunk=read_frame(f);row_header(chunk,group);pr.append(frame(chunk))
        check(not f.read(1) and pr.gz.hexdigest()==pref['private_prefix_sha256'],'all original saved rows restored byte-for-byte')
    z=(a.resume_dir/pref['continuation_file']).read_bytes();body=gzip.decompress(z)
    check((len(z),sha256(z).hexdigest(),len(body),sha256(body).hexdigest())==tuple(pref[k]
          for k in ('continuation_bytes','continuation_sha256','continuation_uncompressed_bytes','continuation_uncompressed_sha256')),
          'whole original saved physical frontier')
    ft=json.loads(body)
    check(ft['plan']==base['plan_sha256'] and ft['count']==n and ft['slabs']==pref['completed_radial_slabs']
          and ft['Dmin']==pref['genuine_min_D_lower_on_saved_groups'],'actual original prefix edge and denominator record')
    state=decode(ft['state']);pr.commit(summary(base,state,n,ft['slabs'],ft['Dmin']),body)
    return n,ft['slabs'],ft['Dmin'],state


def numeric(a):
    global SLAB
    started=monotonic()
    check(os.getenv('GITHUB_ACTIONS')=='true' and os.getenv('GITHUB_REPOSITORY')=='Rogerhu12/math-research-public'
          and os.getenv('GITHUB_RUN_ATTEMPT')=='1' and sys.version_info[:3]==(3,12,14)
          and {k:version(k) for k in ('numpy','scipy','python-flint')}=={'numpy':'2.3.5','scipy':'1.17.0','python-flint':'0.9.0'}
          and platform.machine()=='x86_64' and os.getenv('OPENBLAS_NUM_THREADS')==os.getenv('OMP_NUM_THREADS')=='1',
          'first complete public physical-frequency runtime and bounded numerical threads')
    ctx.prec=320;gate();workers=resources(started);verify_config(a)
    c,arr,major,bounds,outer,ids=original_inputs(a)
    rlo,rhi=map(Q,ROOT);pcl,pcr=map(Q,PIECE);length=rhi-CUT;step=exact(length/RAD)
    check(pcl<CUT<rlo<=rhi<pcr and 0<length<outer and rhi-Q(1,200)<CUT,
          'complete same physical cut and true root inside the actual PW mixed window')
    bands=plan_bands();plan=[(r,lo,hi) for r in range(RAD) for lo,hi in bands]
    base=dict(kind='R149_finite_genuine_nonlocal_and_independent_physical_mean',run=os.environ['GITHUB_RUN_ID'],attempt=1,
        event_commit=os.environ['GITHUB_SHA'],manifest_sha256=a.manifest_sha,whole_112_original_identity=ORIGINAL,
        plan_sha256=sha256(canonical(plan)).hexdigest(),natural_group_count=len(plan),radial_slabs=RAD,
        original_input_labels=[97,STOP],original_input_signs=[1,-1],terminal_Ai_and_two_genuine_columns=True,
        charged_weight='n^(1/6)*(1+n^2)^(2/3) after n*w0+w1V; n=4j',
        row_order=['g1_Hminus5over3','g1_Hminus2over3','g2_physical_scalar'],
        physical_PW_pair='g1_Hminus2over3 and true independent scalar in quadrature on each slab',
        physical_waist_factors=['2039','719/1000','62/5'],outer_J_factors=0,
        separate_signed_sources=['J(Kw-RQ J(e))','2 beta m Pi( u(h+J(e))+K(v-m)f )'],
        local_source_in_this_target=0,all_five_nonlocal_means_retained=True,complete_global_physical_inverse_proved=False,
        full_infinite_frequency_or_other_radial_intervals_claimed=False,old_scientific_targets_recomputed=0,
        science_workers=workers,maximum_wall_seconds=MAX_WALL,maximum_job_memory_bytes=MAX_RSS,
        maximum_private_raw_bytes=MAX_RAW,raw_output_coefficients_public=0)
    head=canonical(dict(plan=plan,original=ids,source=base['kind'],manifest=a.manifest_sha,cut=str(CUT),root=list(ROOT),
        signs=[1,-1],columns=MODES,lags=[-DEGREE,DEGREE],output_fields=['g1_oscillatory','g1_physical','g2_scalar'],
        stripped_unit='exp(i eps n real finite chi mean) on the original right per sign and radial point',
        convention='little-endian f64 directed complex rectangle; all symbol remainder upper in the corresponding header'))
    a.private.mkdir(parents=True,exist_ok=True);path=a.private/NATIVE;pr=Prefix(path,a.receipt,head,base)
    try:
        count,slabs,dmin,state=restore(a,pr,head,base,plan)
        for r in range(RAD):
            start=r*len(bands);end=start+len(bands)
            if end<=count:continue
            gate();resources(started)
            rho=exact((rlo-CUT)*Q(r,RAD)).union(exact(length*Q(r+1,RAD)))
            circle=dict(slab=r,original_sha=ORIGINAL,root=list(ROOT),cut=str(CUT),JCR=JCR)
            bg=physical_background(c,bounds,rho);prototype=Backend(97,97,1)
            w0=Words(prototype,**bg,m=prototype.real_ball(prototype.coeff_Pi(bg['v'])))
            j0=SameCircleJCR(prototype,w0,circle)
            SLAB=(c,geometry(arr,major,rho),bg,w0,j0,adjoint_mean.coefficient_rows(w0,j0))
            # The parent's real ordered commit stream and each worker's current
            # circle are independent. Old confirmed groups are never submitted.
            with get_context('fork').Pool(processes=workers) as pool:
                for group,chunk in zip(plan[max(start,count):end],pool.imap(evaluate_group,plan[max(start,count):end],chunksize=1)):
                    gate();h=row_header(chunk,group);incorporate(state,h,step)
                    dmin=h['genuine_D_lower'] if dmin is None else min(dmin,h['genuine_D_lower'])
                    count+=1;slabs+=int(group[2]==STOP)
                    check(pr.usize+len(chunk)+SIZE.size<MAX_RAW,'bounded private whole physical carrier')
                    pr.append(frame(chunk));frontier=canonical(dict(plan=base['plan_sha256'],count=count,slabs=slabs,
                        Dmin=dmin,state=encode(state)))
                    pr.commit(summary(base,state,count,slabs,dmin),frontier);resources(started)
                    if count%16==0:print('GNF_CONFIRMED_ORDERED_PREFIX',count,len(plan),flush=True)
        check(count==len(plan) and slabs==RAD and dmin>0,'both complete signs and both full genuine output columns on every slab')
    finally:
        pr.close();SLAB=None
    verified_stream(path,(pr.csize,pr.gz.hexdigest()),(pr.usize,pr.raw.hexdigest()))
    with gzip.open(path,'rb') as f:
        check(read_frame(f)==head,'whole canonical uncompressed true input header')
        for row in plan:row_header(read_frame(f),row)
        check(not f.read(1),'true physical carrier through final verified EOF')
    d=summary(base,state,count,slabs,dmin);d.update(complete=True,proved=True,private_bytes=pr.csize,
        private_sha256=pr.gz.hexdigest(),private_uncompressed_bytes=pr.usize,private_uncompressed_sha256=pr.raw.hexdigest(),
        last_read_head=gate(),actual_scientific_seconds=monotonic()-started)
    body=canonical(d);check(len(body)<95000,'whole small final numerical result')
    replace(a.receipt,body);check(a.receipt.read_bytes()==body,'whole public result readback')
    print('GNF_WHOLE_RESULT',len(body),sha256(body).hexdigest(),body.decode().strip(),flush=True)


if __name__=='__main__':
    ap=ArgumentParser()
    for name in ('repo','manifest','private','receipt'):ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--manifest-sha',required=True)
    ap.add_argument('--resume',type=Path);ap.add_argument('--resume-sha');ap.add_argument('--resume-dir',type=Path)
    args=ap.parse_args()
    try:
        check(bool(args.resume)==bool(args.resume_dir)==bool(args.resume_sha),'complete old public prefix and private original identity')
        numeric(args)
    except Exception as exc:
        record_failure(args.receipt,exc)
        raise
