"""Complete B and V derivative packets on the entire genuine cutoff, with the true GCD frequency sectors."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from hashlib import sha256
from importlib.metadata import version
from math import nextafter,inf,isfinite
from pathlib import Path
import gzip,io,json,os,struct,subprocess,sys
from flint import acb,arb,ctx
from fourfold_codazzi_true_ratio_live_rules import canonical,gate
from fourfold_codazzi_true_ratio_prefix import Prefix,replace,record_failure
from fourfold_codazzi_true_phase_original_inputs import check
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_exterior_signed_potential_moment import background,PRE,PRE_SHA,edges,dyadic,decode
from fourfold_codazzi_variable_cutoff_moments import coefficients,packet,RADIUS,L

BINS=256
ARCS=16
BANDS=((97,97),(98,101),(102,122),(123,None))
NAME='complete-negative-variable-cutoff-jets.gz'
BOX=struct.Struct('<dddd')
KEYS=('plan_sha256','prior_sha256','input_receipts_sha256','radial_bins','contour_arcs')


def frame(b):return struct.pack('<I',len(b))+b


def readf(f):
    n,=struct.unpack('<I',f.read(4));b=f.read(n)
    check(n<130000 and len(b)==n,'one complete historical signed sector')
    return b


def sector(group,k):
    a,b=BANDS[group];hi=Q(97,a);lo=Q(97,b) if b else Q(0)
    if k==-1:return acb(exact(lo).union(exact(hi)))
    m=(lo+hi)/2;r=1-m
    theta=arb.pi()*2*exact(Q(k,ARCS)).union(exact(Q(k+1,ARCS)))
    # Make the known unit-disk coordinate bound explicit even on a rectangular arc hull.
    return acb(exact(m)+exact(r)*theta.cos(),exact(r)*theta.sin())


def zsquare(z):
    d=z*z/9409;box=arb(0).union(exact(Q(1,9409)))
    both=(-box).union(box)
    return acb(d.real.intersection(both),d.imag.intersection(both))


def encode(z):
    a=edges(z.real);b=edges(z.imag)
    check(all(isfinite(v) for v in a+b),'finite directed complex rectangle')
    return BOX.pack(*(a+b))


def reset():
    return None,[arb(0)]*9


def update(state,real,vals):
    lo,maxima=state
    if real:
        a=vals[4].real.lower();lo=a if lo is None else min(lo,a)
    return lo,[max(a,abs(v).upper()) for a,v in zip(maxima,vals)]


def frontier(n,state):
    lo,maxima=state
    return canonical(dict(n=n,real_lower=dyadic(lo),maximum=list(map(dyadic,maxima))))


def old(a,pr,base,head,plan):
    if not a.resume:return 0,reset()
    b=a.resume.read_bytes();check(sha256(b).hexdigest()==a.resume_sha,'whole original cutoff prefix receipt')
    d=json.loads(b);n=d['completed_subpieces']
    check(not d['complete'] and 0<n<=len(plan) and all(d[k]==base[k] for k in KEYS),'same entire original family and mesh')
    b=(a.resume_dir/NAME).read_bytes()[:d['private_prefix_bytes']];raw=gzip.decompress(b)
    check((len(b),sha256(b).hexdigest(),len(raw),sha256(raw).hexdigest())==tuple(d[k] for k in
          ('private_prefix_bytes','private_prefix_sha256','private_prefix_uncompressed_bytes','private_prefix_uncompressed_sha256')),
          'complete signed previous numerical prefix')
    f=io.BytesIO(raw);check(readf(f)==head,'same full original scalar header')
    for j in range(n):
        v=readf(f);g=io.BytesIO(v);q=json.loads(readf(g))
        check(q['sector']==list(plan[j]) and len(g.read())==BOX.size*(13+9*BINS),'same all native physical fields')
        pr.append(frame(v))
    check(not f.read(1) and pr.gz.hexdigest()==d['private_prefix_sha256'],'all complete sectors copied once')
    b=(a.resume_dir/d['continuation_file']).read_bytes();raw=gzip.decompress(b)
    check((len(b),sha256(b).hexdigest(),len(raw),sha256(raw).hexdigest())==tuple(d[k] for k in
          ('continuation_bytes','continuation_sha256','continuation_uncompressed_bytes','continuation_uncompressed_sha256')),
          'entire latest directed continuation checkpoint')
    q=json.loads(raw);check(q['n']==n,'correct original frontier')
    pr.commit(dict(base,completed_subpieces=n,prefix_proved=True),raw)
    return n,(decode(q['real_lower']),list(map(decode,q['maximum'])))


def run(a):
    check(os.environ['GITHUB_ACTIONS']=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
          and os.environ['GITHUB_RUN_ATTEMPT']=='1' and sys.version_info[:3]==(3,12,14)
          and version('python-flint')=='0.9.0','physical cutoff original public exact runtime')
    gate();ctx.prec=320
    raw=(a.repo/PRE).read_bytes();check(len(raw)==27645 and sha256(raw).hexdigest()==PRE_SHA,'whole genuine original complex disk')
    d=json.loads(raw);res=d['actual_scientific_receipt'];case=res['cases'][-1];bs=case['complete_modulus_upper']
    check(d['complete'] and d['actual_returncode']==0 and d['actual_failure'] is None and res['complete'] and res['proved']
          and all(v['passed'] for v in res['gates']) and case['complete'] and case['proved']
          and case['exact_complex_radial_radius']=='1/6000' and case['exact_complex_z_square_halfwidth']=='1/9409'
          and case['fixed_intrinsic_parameter']=='eta_0' and case['exact_complex_delta_square_halfwidth']=='1/100000000'
          and arb(case['reference_image']['complete_image_disk_radius_lower']['ball']).lower()>exact(RADIUS)
          and arb(bs['V']['ball']).upper()<276 and arb(bs['V_TT']['ball']).upper()<3830956,'complete original reference image and V jets')
    def read(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=a.repo)
    c,ids=background(read);plan=[(j,k) for j in range(4) for k in ([-1] if j==0 else [-1,*range(ARCS)])]
    check(len(ids)==19 and len(plan)==52,'all actual scalar background inputs and transverse contours')
    topology=dict(bands=BANDS,sectors=plan,radial_bins=BINS,contour_arcs=ARCS,coordinate='x=-T/L',L=str(L))
    head=canonical(dict(topology=topology,original=ids,format='per sector: 13 coefficients V(-Lx); per x bin normalized x jets Vext0..3, B0..4; four outward binary64 real/imag endpoints per complex cell'))
    base=dict(kind='R149_entire_partial_cutoff_integrals_and_complex_transverse_derivatives',run=os.environ['GITHUB_RUN_ID'],
              event_commit=os.environ['GITHUB_SHA'],attempt=1,radial_bins=BINS,contour_arcs=ARCS,natural_sectors=len(plan),
              prior_sha256=PRE_SHA,input_receipts_sha256=sha256(canonical(ids)).hexdigest(),plan_sha256=sha256(canonical(topology)).hexdigest(),
              old_targets_recomputed=0,complete_waist_or_high_inverse_claimed=False)
    a.private.mkdir(parents=True,exist_ok=True);p=a.private/NAME;pr=Prefix(p,a.receipt,head,base)
    try:
        n,state=old(a,pr,base,head,plan)
        for seq,(j,k) in enumerate(plan[n:],n+1):
            gate();z=zsquare(sector(j,k));coeff=coefficients(c,z);parts=[encode(v) for v in coeff]
            for h in range(BINS):
                lo,hi=Q(h,BINS),Q(h+1,BINS)
                aa,bb=packet(coeff,lo,hi);vs=aa+bb
                state=update(state,k==-1,vs);parts.extend(map(encode,vs))
            meta=canonical(dict(sector=[j,k],bins=BINS,transverse=[edges(z.real),edges(z.imag)]))
            body=b''.join(parts);check(len(body)==BOX.size*(13+9*BINS),'all true signed complex original orders')
            pr.append(frame(frame(meta)+body));pr.commit(dict(base,completed_subpieces=seq,prefix_proved=True),frontier(seq,state))
            print('GPM_COMPLETED_ORIGINAL_SECTOR',seq,len(plan),flush=True)
    finally:pr.close()
    b=p.read_bytes();u=gzip.decompress(b)
    check(len(b)==pr.csize and sha256(b).hexdigest()==pr.gz.hexdigest() and len(u)==pr.usize<5_000_000 and sha256(u).hexdigest()==pr.raw.hexdigest(),'whole original numerical carrier readback')
    lower,maxima=state
    cert=dict(base,complete=True,proved=True,completed_subpieces=len(plan),closed_radial_frequency_cells=BINS*len(plan),
              real_B_lower=edges(lower)[0],complete_real_average_above_190=bool(lower>190),
              absolute_upper_normalized_x_Vext_and_B=[edges(q)[1] for q in maxima],complete_complex_B_below_276=bool(maxima[4]<276),
              private_bytes=len(b),private_sha256=sha256(b).hexdigest(),private_uncompressed_bytes=len(u),private_uncompressed_sha256=sha256(u).hexdigest(),
              last_rule_read_head=gate())
    replace(a.receipt,canonical(cert));print('GPM_WHOLE_SMALL_RECEIPT',canonical(cert).decode().strip(),flush=True)


if __name__=='__main__':
    ap=ArgumentParser()
    for k in ('repo','private','receipt'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--resume',type=Path);ap.add_argument('--resume-sha');ap.add_argument('--resume-dir',type=Path)
    a=ap.parse_args()
    try:
        check(bool(a.resume)==bool(a.resume_sha)==bool(a.resume_dir),'identical complete prior cutoff frontier')
        run(a)
    except Exception as exc:
        record_failure(a.receipt,exc)
        raise
