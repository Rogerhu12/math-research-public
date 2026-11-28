"""Genuine exterior signed carrier multiplier for every frequency and both original columns."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from importlib.metadata import version
from math import inf,isfinite,nextafter
from pathlib import Path
import gzip,io,json,os,struct,subprocess,sys
from flint import arb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as A
import fourfold_codazzi_true_characteristic_seed_admission as S
import fourfold_codazzi_correlated_collar_reference as F
from fourfold_codazzi_true_phase_original_inputs import check
from fourfold_codazzi_true_ratio_live_rules import canonical,gate
from fourfold_codazzi_true_ratio_prefix import Prefix,replace,record_failure
from fourfold_codazzi_signed_density_transport_arithmetic import exact

PRE='topics/visible-flex-exact-nearby/notes/common_radial_potential_budget_ci/run-43685624307-1/execution.json'
PRE_SHA='d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9'
PLAN=((97,97),(98,103),(104,127),(128,191),(192,255),(256,511),(512,1023),(1024,2047),
      (2048,4095),(4096,8191),(8192,65535),(65536,1048576),(1048577,None))
Z_CAP=Q(7,10000)


def background(read):
    names=['complete-background-root-series']
    for i in range(9,15):names+=['background-inputs-degree-%03d'%i,'background-main-degree-%03d'%i]
    stage,_,ids=S.admit(read,names)
    b=stage[names[0]]
    check(all(b[k] for k in ('complete_mean_at_all_orders_retained','original_65_and_193_rows_retained',
            'zero_bump_germ_and_fixed_eta0','positive_order_value_repair_derivatives_exactly_zero')),
            'same complete complex family and one-sided scalar reference coordinate')
    c={k:A.unpack_series(v) for k,v in b['series'].items()}
    for n in range(9,15):
        inp=stage['background-inputs-degree-%03d'%n];main=stage['background-main-degree-%03d'%n]
        check(inp['degree']==main['degree']==n,'same full physical degree')
        for k in ('K','beta','gamma','s','u','v','k'):c[k].append(A.LP.restore(inp['coefficients'][k]))
        for k in ('eta','a'):c[k].append(A.LP.restore(main[k]))
    return c,ids


@lru_cache(None)
def moment(k):
    """Integral of chi(-y)*(y/L)^k dy/(2*sqrt(y))."""
    t=Q(2*k+1,2);c=Q(1);m=Q(1);s=Q(1)
    for j in range(1,65):
        c*= (t-j+1)/(3*j)
        if j%2==0:
            m*=Q(j-1,j+129)
            if j<64:s+=c*m
    # Every later even term is at most 1/9 the previous absolute term.
    rad=abs(c*m)*Q(9,8)
    scale=exact(F.L*Q(3,4)).sqrt()*exact(Q(3,4)**k/Q(2*k+1))
    return (exact(s)+arb(0,exact(rad).upper()))*scale


def signed_moment(c,lo,hi,bounds):
    coeff=F.scaled_potential(c,lo,hi);n=len(coeff)
    check(n==13,'original signed Taylor degrees 0 through 12')
    ratio=exact(F.L/Z_CAP);fac=exact(-F.L/F.R)
    p=arb(1);value=arb(0)
    for k,z in enumerate(coeff):
        value+=z*p*moment(k);p=p*fac
    tail=exact(bounds[0])*ratio**n*moment(n)/(1-ratio)
    full=value+arb(0,tail.upper())
    linear=coeff[0]*moment(0)+coeff[1]*fac*moment(1)
    error=exact(bounds[1])*exact(F.L**2)*moment(2)/2
    other=linear+arb(0,error.upper())
    simple=arb(0,(exact(bounds[0])*moment(0)).upper())
    check(full.overlaps(other) and simple.overlaps(full.intersection(other)),'three complete true exterior potential moments')
    return full.intersection(other).intersection(simple),tail,error


def edges(z):
    a=nextafter(float(z.lower()),-inf);b=nextafter(float(z.upper()),inf)
    check(isfinite(a) and isfinite(b) and a<=b,'complete directed small endpoints')
    return [a,b]


def dyadic(z):
    def enc(a):
        m,e=a.man_exp();return [str(m),int(e)]
    return [enc(z.lower()),enc(z.upper())]


def decode(bounds):
    def side(z):return exact(Q(int(z[0]))*Q(2)**int(z[1]))
    return side(bounds[0]).union(side(bounds[1]))


def resume(a,pr,base,head,plan):
    if not a.resume:return 0,None,arb(0),None
    b=a.resume.read_bytes();check(sha256(b).hexdigest()==a.resume_sha,'entire previous small scientific prefix')
    d=json.loads(b);n=d['completed_subpieces']
    check(not d['complete'] and 0<n<=len(plan) and all(base[k]==d[k] for k in
          ('frequency_plan_sha256','original_background_receipts_sha256','natural_bands')),
          'same genuine cutoff moment and full original plan')
    b=(a.resume_dir/'signed-exterior-potential-bands.gz').read_bytes()[:d['private_prefix_bytes']]
    raw=gzip.decompress(b)
    check((len(b),sha256(b).hexdigest(),len(raw),sha256(raw).hexdigest())==tuple(d[k] for k in
          ('private_prefix_bytes','private_prefix_sha256','private_prefix_uncompressed_bytes','private_prefix_uncompressed_sha256')),
          'complete previous private scientific rows')
    f=io.BytesIO(raw)
    def frame():
        size,=struct.unpack('<I',f.read(4));v=f.read(size);check(len(v)==size<100000,'whole original natural row')
        return v
    check(frame()==head,'same original private header');z=None
    for lo,hi in plan[:n]:
        row=frame();v=json.loads(row);check(v['band']==[lo,hi],'same original frequency interval')
        z=decode(v['signed']);pr.append(struct.pack('<I',len(row))+row)
    check(not f.read(1) and pr.gz.hexdigest()==d['private_prefix_sha256'],'all previous rows copied identically')
    b=(a.resume_dir/d['continuation_file']).read_bytes();raw=gzip.decompress(b)
    check((len(b),sha256(b).hexdigest(),len(raw),sha256(raw).hexdigest())==tuple(d[k] for k in
         ('continuation_bytes','continuation_sha256','continuation_uncompressed_bytes','continuation_uncompressed_sha256')),
         'entire original numerical continuation')
    c=json.loads(raw);check(c['count']==n,'correct previously completed natural frontier')
    pr.commit(dict(base,completed_subpieces=n,prefix_proved=True),raw)
    return n,decode(c['whole_signed_hull']),decode(c['max_radius']),z


def run(a):
    check(os.environ['GITHUB_ACTIONS']=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
          and os.environ['GITHUB_RUN_ATTEMPT']=='1' and sys.version_info[:3]==(3,12,14)
          and version('python-flint')=='0.9.0','original directed public scientific owner')
    gate();ctx.prec=320
    def read(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=a.repo)
    raw=(a.repo/PRE).read_bytes();check((len(raw),sha256(raw).hexdigest())==(27645,PRE_SHA),'original whole potential execution')
    d=json.loads(raw);res=d['actual_scientific_receipt'];case=res['cases'][-1];bs=case['complete_modulus_upper']
    check(d['complete'] and d['actual_returncode']==0 and d['actual_failure'] is None and res['complete'] and res['proved']
          and all(v['passed'] for v in res['gates']) and case['complete'] and case['proved']
          and case['exact_complex_radial_radius']=='1/6000' and case['exact_complex_z_square_halfwidth']=='1/9409'
          and case['fixed_intrinsic_parameter']=='eta_0' and case['exact_complex_delta_square_halfwidth']=='1/100000000'
          and arb(case['reference_image']['complete_image_disk_radius_lower']['ball']).lower()>exact(Z_CAP)
          and arb(bs['V']['ball']).upper()<276 and arb(bs['V_TT']['ball']).upper()<3830956,
          'genuine analytic potential on the full closed original domain')
    c,ids=background(read);plan=list(PLAN)
    check(len(ids)==19 and plan[0][0]==97 and plan[-1][1] is None and
          all(row[1]+1==nex[0] for row,nex in zip(plan,plan[1:])),'the complete frequency family and original input inventory')
    a.private.mkdir(parents=True,exist_ok=True);out=a.private/'signed-exterior-potential-bands.gz'
    head=canonical(dict(plan=plan,original=ids,prior_sha256=PRE_SHA,half_label='n=4|j|',cutoff='WUA.18'))
    base=dict(kind='R149_true_signed_exterior_homogeneous_ratio_translation',run=os.environ['GITHUB_RUN_ID'],attempt=1,
         event_commit=os.environ['GITHUB_SHA'],frequency_plan_sha256=sha256(canonical(plan)).hexdigest(),
         original_background_receipts_sha256=sha256(canonical(ids)).hexdigest(),natural_bands=len(plan),old_targets_recomputed=0)
    pr=Prefix(out,a.receipt,head,base)
    try:
        start,cover,maxrad,z=resume(a,pr,base,head,plan)
        for i,(lo,hi) in enumerate(plan[start:],start+1):
            gate();z,te,le=signed_moment(c,lo,hi,(276,3830956))
            cover=z if cover is None else cover.union(z)
            maxrad=max(maxrad,(z.upper()-z.lower())/2)
            row=canonical(dict(band=[lo,hi],signed=dyadic(z),Taylor_remainder=dyadic(te),linear_remainder=dyadic(le)))
            pr.append(struct.pack('<I',len(row))+row);state=canonical(dict(count=i,whole_signed_hull=dyadic(cover),max_radius=dyadic(maxrad)))
            pr.commit(dict(base,completed_subpieces=i,prefix_proved=True,whole_signed_hull=edges(cover)),state)
    finally:pr.close()
    b=out.read_bytes();u=gzip.decompress(b)
    check(len(b)==pr.csize and sha256(b).hexdigest()==pr.gz.hexdigest() and len(u)==pr.usize and sha256(u).hexdigest()==pr.raw.hexdigest(),
          'whole original frequency partition and signed moments read back')
    result=dict(base,completed_subpieces=len(plan),complete=True,proved=True,all_signed_hull=edges(cover),
         maximum_single_band_radius_upper=edges(maxrad)[1],infinite_band_signed=edges(z),
         all_strictly_positive=cover.lower()>0,all_strictly_negative=cover.upper()<0,
         all_abs_below_one=abs(cover).upper()<1,all_abs_below_six=abs(cover).upper()<6,
         private_bytes=len(b),private_sha256=sha256(b).hexdigest(),private_uncompressed_bytes=len(u),
         private_uncompressed_sha256=sha256(u).hexdigest(),last_rule_read_head=gate())
    replace(a.receipt,canonical(result));print('GXM_WHOLE_SMALL_RECEIPT',canonical(result).decode().strip(),flush=True)


if __name__=='__main__':
    ap=ArgumentParser()
    for x in ('repo','private','receipt'):ap.add_argument('--'+x,required=True,type=Path)
    ap.add_argument('--resume',type=Path);ap.add_argument('--resume-sha');ap.add_argument('--resume-dir',type=Path)
    a=ap.parse_args()
    try:
        check(bool(a.resume)==bool(a.resume_sha)==bool(a.resume_dir),'all complete original continuation identities')
        run(a)
    except Exception as exc:
        record_failure(a.receipt,exc)
        raise
