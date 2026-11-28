"""Signed physical-r/angle jets on the same original root piece as GLW."""
from fractions import Fraction as Q
from hashlib import sha256
import gzip
import json
from flint import acb,arb
import fourfold_codazzi_true_characteristic_seed_admission as S
from fourfold_codazzi_true_characteristic_root_input import cauchy_tail,radial_laurent
from fourfold_codazzi_true_phase_original_inputs import check
from fourfold_codazzi_collar_signed_laurent_enclosure import Field,WIDTH

RG=Q(3,8000)
CW=Q(1,32)
SCALAR=frozenset(('beta','eta','K'))
NAMES=('u','v','beta','eta','K','d')


def original_majorants(read,receipts):
    """Accept the very same whole original product already admitted by signed_inputs.receive."""
    p,size,digest=S.FIXED['majorants']
    check(sum(r==dict(path=p,bytes=size,sha256=digest) for r in receipts)==1,
          'same actual passed original product in the signed collar inventory')
    raw=read(S.HISTORY,p)
    check(len(raw)==size and sha256(raw).hexdigest()==digest,'entire original refined background product')
    obj=json.loads(gzip.decompress(raw))
    check(obj['complete'] and obj['stage']==obj['name']=='complete-original-reference-holomorphic-majorants'
          and obj['source_sha256']=='f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739'
          and obj['input_manifest_sha256']=='76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a'
          and obj['payload_sha256']=='e0f1852f561b2596018e387a0b6c728441b665fee227e4c6fa85bc352060bf23',
          'original anchored R=3/8000 and coefficient-strip 1/32 lineage')
    v=obj['payload']['coefficients']
    def up(x):return arb(x['ball']).upper()
    maxima={}
    for name,key in (('u','U'),('v','V')):
        for i in range(2):
            for j in range(3):maxima[name,i,j]=up(v[key][i][j])
    for i,k in enumerate(('D','Dr')):
        for j in range(3):maxima['d',i,j]=up(v[k][j])
    for name,zero,one in (('beta','beta','beta_r'),('K','K','Kr')):
        maxima[name,0,0]=up(v[zero]);maxima[name,1,0]=up(v[one])
    maxima['eta',0,0]=up(v['ep'])
    maxima['eta',1,0]=(up(v['ep'])*up(v['eta_log_r'])).upper()
    check(all(z.is_finite() and z>=0 for z in maxima.values()),'all actual same-product quantities')
    return maxima


def field(c,major,name,rho,physical_r=0,angle=0):
    """Ordinary physical partial_r^i partial_phi^j. Includes the genuine mean."""
    i=physical_r;j=angle
    check(name in NAMES and i in (0,1) and j in (0,1,2) and WIDTH<CW,
          'complete physical orders on the original piece')
    if name in SCALAR and j:return Field.scalar(0)
    cs=c[name]
    lp=radial_laurent(cs,rho,i).theta(j)
    # The Taylor series is in inward rho=r_*-r. At fixed phi each
    # original physical r derivative therefore introduces one minus sign.
    if i:lp=-lp
    m=major[name,i,j]
    first=len(cs)-i
    fee=cauchy_tail((m,RG,CW-WIDTH),abs(rho).upper(),first,0,0)
    plain=cauchy_tail((major[name,0,0],RG,CW-WIDTH),abs(rho).upper(),len(cs),i,j)
    fee=min(fee,plain)
    if name in SCALAR:
        check(all(z==0 for h,z in enumerate(lp.c,lp.lo) if h),
              'angularly constant original scalar on its entire real parameter family')
        z=lp.mean()
        check(z.imag.contains(0),'real original scalar value and physical derivative')
        return Field.scalar(acb(z.real+arb(0,fee)))
    return Field(lp.lo,lp.c,fee)
