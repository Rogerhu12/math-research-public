#!/usr/bin/env python3
"""Actual complete R109 finite Jacobian, stable normalized materials, version2.

The previous run can produce nan when a broad Arb cbg enclosure contains0.
This version bounds s/(s+|ell|), ell/(s+|ell|) first, and rejects every nan.

Keep all10793 original material rows,20 nonzero centre modes,46 input
modes in each physical component,46 outputs, the complete quadratic
mean derivative, and a rigorously bounded COMPLETE-source derivative
remainder. This is a centre Jacobian, not a whole-ball or cut certificate.
The output norm takes each radial modal supremum before summation.

Author: /root (GPT-6 Astra Pro; AI-assisted),2026-11-13.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ProcessPoolExecutor
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, arb_poly, fmpq, fmpq_poly, ctx

MODES=list(range(2,93,2))
CENTRE=list(range(2,41,2))
FIELDS_SHA='94fb941354dbb4769cb7ce80d5f7fd14eed6bdbce893842881c5c949c460288a'
FIELDS_SOURCE='306b2bc0c49635d731f3bbe91653310f2b2ecba19bcb7437f8ef932f37a5d75b'

def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def point(x):
    if isinstance(x,dict):
        return arb((int(x['mantissa']),int(x['binary_exponent'])))
    return arb((int(x[0]),int(x[1])))

def ball(x):
    if isinstance(x,dict):
        return point(x['lower']).union(point(x['upper']))
    return point(x[0]).union(point(x[1]))

def pack_upper(x,bits=128):
    # Exact outward dyadic endpoints; no decimal reconstruction.
    if not x.is_finite() or x<0:
        raise ArithmeticError('Finite nonnegative bound required')
    x=x.upper()
    if x==0:
        return [0,0]
    mantissa,exponent=x.man_exp()
    mantissa,exponent=int(mantissa),int(exponent)
    shift=max(0,mantissa.bit_length()-bits)
    if shift:
        mask=(1<<shift)-1
        mantissa=(mantissa>>shift)+bool(mantissa&mask)
        exponent+=shift
    return [mantissa,exponent]

class Laurent:
    """Full finite Laurent algebra; no coefficient projection in products."""
    def __init__(self,p,offset=0):
        self.p,self.offset=p,int(offset)
    @classmethod
    def constant(cls,v,kind=arb_poly):
        return cls(kind([v]),0)
    @classmethod
    def from_dict(cls,values,kind=arb_poly):
        lo=min(values,default=0); hi=max(values,default=0)
        return cls(kind([values.get(i,0) for i in range(lo,hi+1)]),-lo)
    def coerce(self,x):
        return x if isinstance(x,Laurent) else Laurent.constant(x,type(self.p))
    def shifted_poly(self,offset):
        return type(self.p)([0]*(offset-self.offset)+self.p.coeffs())
    def __add__(self,x):
        x=self.coerce(x); off=max(self.offset,x.offset)
        return Laurent(self.shifted_poly(off)+x.shifted_poly(off),off)
    __radd__=__add__
    def __neg__(self):
        return Laurent(-self.p,self.offset)
    def __sub__(self,x):
        return self+-self.coerce(x)
    def __rsub__(self,x):
        return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x)
        return Laurent(self.p*x.p,self.offset+x.offset)
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0: raise ValueError('Only full finite products')
        return Laurent(self.p**n,self.offset*n)
    def coeff(self,j):
        i=int(j)+self.offset
        return self.p[i] if 0<=i<len(self.p) else type(self.p)([0])[0]

def algebra(values,z,s,ell,kind=arb_poly,scalar=arb):
    E=1+z
    pa,ka,ta,ua={},{},{},{}
    c2=scalar(0)
    for n,(p,k) in values.items():
        j=n//2
        pa[j],pa[-j]=p,-p
        ka[j]=ka[-j]=k
        ta[j]=ta[-j]=n*p
        ua[j],ua[-j]=-n*k-p,n*k+p
        c2-=((1+3*z)*k*k+E*p*p+2*E*n*k*p)/4
    P,K,T,U=(Laurent.from_dict(a,kind) for a in (pa,ka,ta,ua))
    C=K+T; D=K+E*T
    # Scalar factors explicitly precede products: Laurent has no quotient.
    Q=scalar(1)/4*(-E*s*(U*U)+ell*(C*C+z*(2*K*T+T*T+P*P)))
    L=scalar(1)/2*D+c2
    A=Q+ell*(c2*D+c2*c2)
    S=1-L+L**2-L**3
    H=A*(-1+2*L-3*L**2)
    # BP=i*Bp and BJ=i*Bj. BK,BT,Bc have real Laurent coefficients.
    Bp=S*(E*s*U+ell*z*P)
    Bj=-E*s*S*U
    Bk=ell*S*(E*C-z*K+2*c2)+H
    Bt=ell*E*S*(C+2*c2)+E*H
    Bc=ell*S*(D+2*c2)+H
    return dict(P=P,K=K,T=T,U=U,C=C,D=D,c2=c2,L=L,A=A,S=S,H=H,
                Bp=Bp,Bj=Bj,Bk=Bk,Bt=Bt,Bc=Bc,E=E,z=z,s=s,ell=ell,
                values=values,scalar=scalar,kind=kind)

def column(a,n,component):
    p,k=a['values'].get(n,(0,0)); E,z=a['E'],a['z']
    dc= -E*(p+n*k)/2 if component=='P' else -((1+3*z)*k+E*n*p)/2
    out=[]
    for m in MODES:
        left,right=(m-n)//2,(m+n)//2
        if component=='P':
            v=a['Bp'].coeff(left)-a['Bp'].coeff(right)+n*(a['Bt'].coeff(left)+a['Bt'].coeff(right))
        else:
            v=a['Bk'].coeff(left)+a['Bk'].coeff(right)-n*(a['Bj'].coeff(left)-a['Bj'].coeff(right))
        out.append(v+2*a['Bc'].coeff(m//2)*dc)
    return out

def direct_column(a,n,component):
    """Independent full product rule, used for exact algebra verification."""
    kind,scalar=a['kind'],a['scalar']; j=n//2
    Z=Laurent.constant(0,kind)
    odd=Laurent.from_dict({j:1,-j:-1},kind)
    even=Laurent.from_dict({j:1,-j:1},kind)
    dp,dk,dt,du=(odd,Z,n*even,-odd) if component=='P' else (Z,even,Z,-n*odd)
    p,k=a['values'].get(n,(0,0)); E,z,s,ell=a['E'],a['z'],a['s'],a['ell']
    dc=-E*(p+n*k)/2 if component=='P' else -((1+3*z)*k+E*n*p)/2
    dC=dk+dt; dD=dk+E*dt
    dQ=scalar(1)/2*(-E*s*a['U']*du+ell*(a['C']*dC+z*(dk*a['T']+a['K']*dt+a['T']*dt+a['P']*dp)))
    dA=dQ+ell*(dc*a['D']+a['c2']*dD+2*a['c2']*dc)
    dL=scalar(1)/2*dD+dc
    out=dA*a['S']+a['H']*dL
    return [2*out.coeff(m//2) for m in MODES]

def exact_check():
    values={n:(fmpq((-1)**(n//2),2**(n+10)),fmpq(n+1,3**(n//2+10))) for n in CENTRE}
    a=algebra(values,fmpq(1,9),fmpq(7,5),fmpq(-11,13),fmpq_poly,fmpq)
    comparisons=0
    for n in MODES:
        for component in ('P','K'):
            left,right=column(a,n,component),direct_column(a,n,component)
            if left!=right:
                raise ArithmeticError('Five multipliers differ from full product rule')
            comparisons+=len(left)
    return {'all_full_product_rule_coefficients_equal':True,'exact_rational_equalities':comparisons,
            'includes_full_mean_derivative_and_absent_centre_input_modes':True}

def normalized_materials(s,ell):
    """Exact positive-denominator endpoints, before any wide interval union."""
    sl,sh,el,eh=s.lower(),s.upper(),ell.lower(),ell.upper()
    if not all(x.is_finite() for x in (sl,sh,el,eh)) or not sl>0:
        raise ArithmeticError('Strictly positive material s required')
    ehi=max(abs(el),abs(eh))
    elo=arb(0) if el<=0<=eh else min(abs(el),abs(eh))
    alo=(sl/(sl+ehi)).lower(); ahi=(sh/(sh+elo)).upper()
    blo=(el/(sl-el) if el<0 else el/(sh+el)).lower()
    bhi=(eh/(sl+eh) if eh>0 else eh/(sh-eh)).upper()
    if not all(x.is_finite() for x in (alo,ahi,blo,bhi)) or not alo>=0 or not ahi<=1 or not blo>=-1 or not bhi<=1:
        raise ArithmeticError('Normalized material endpoints invalid')
    return alo.union(ahi),blo.union(bhi)

def group_compute(args):
    g,root,limit=args; root=Path(root);ctx.prec=256
    began=time.monotonic(); zero=arb(0)
    maxima=[[zero for _ in MODES] for _ in range(92)]
    remainder=[[zero for _ in MODES] for _ in range(92)]
    hashes={}; count=0; accepted={q:0 for q in (2,4,8,16)}
    weights={n:(arb(n)/64).exp() for n in MODES}
    for ch in g['chunks']:
        p=root/ch['path']; got=digest(p)
        if got!=ch['sha256']: raise ValueError('Original complete field chunk changed')
        hashes[str(p)]=got
        with gzip.open(p,'rt') as f: d=json.load(f)
        if (d['cell'],d['segment'])!=(g['cell'],g['segment']) or len(d['panels'])!=ch['panels']:
            raise ValueError('Original row identity or coverage changed')
        for row in d['panels']:
            if int(row['panel'])!=count: raise ValueError('Incomplete ordered material rows')
            values={int(v['mode']):(ball(v['P']),ball(v['K'])) for v in row['original_candidate_PK']}
            if sorted(values)!=CENTRE: raise ValueError('All20 centre modes required')
            selected={int(v['mode']):(ball(v['P']),ball(v['K'])) for v in row['true_linear_selected_PK']}
            if sorted(selected)!=[2,4]: raise ValueError('Original two true linear modes required')
            values.update(selected)
            r,rx,w,ell=[ball(row[k]) for k in ('radius','radius_x','w','log_w_x')]
            V=point(row['source_envelope']['lower']) if isinstance(row['source_envelope'],dict) else point(row['source_envelope'][0])
            if ball(row['source_envelope'])!=V or not V>0 or not r>0 or not rx>0 or not w>0 or not w<=arb(1)/2:
                raise ArithmeticError('Positive true physical domain required')
            s=rx/r; sn,ln=normalized_materials(s,ell); a=algebra(values,w*w,sn,ln)
            R=sum((1+n)*weights[n]* (abs(p).upper()+abs(k).upper()) for n,(p,k) in values.items())
            if not R<arb(1)/128: raise ArithmeticError('Complete R109 derivative domain unpaid')
            rq={q:sum((1+n)*arb(q)**n*(abs(p).upper()+abs(k).upper()) for n,(p,k) in values.items()) for q in (2,4,8,16)}
            rq={q:v.upper() for q,v in rq.items() if v<arb(1)/128}
            for q in rq: accepted[q]+=1
            for ix,n in enumerate(MODES):
                coeffs=[column(a,n,'P'),column(a,n,'K')]
                for j,m in enumerate(MODES):
                    err=(6450*R**3*(1+n)*weights[n]/weights[m]).upper()
                    for q,v in rq.items():
                        err=min(err,(6450*v**3*(1+n)*(arb(q)**(-abs(m-n))+arb(q)**(-m-n))).upper())
                    conv=weights[m]/((1+n)*weights[n]*V)
                    er=(err*conv).upper()
                    for component in range(2):
                        k=2*ix+component
                        finite=(abs(coeffs[component][j])*conv).upper()
                        if not finite.is_finite() or not er.is_finite() or not finite>=0 or not er>=0:
                            raise ArithmeticError('Every finite Jacobian entry and complete tail must be finite nonnegative')
                        maxima[k][j]=max(maxima[k][j],(finite+er).upper())
                        remainder[k][j]=max(remainder[k][j],er)
            count+=1
            if limit and count>=limit: break
        if limit and count>=limit: break
    if not limit and count!=g['panels']: raise ValueError('A complete group is required')
    return {'cell':g['cell'],'segment':g['segment'],'rows':count,'complete':count==g['panels'],
            'input_hashes':hashes,'tilted_derivative_domains_accepted':accepted,
            'weighted_source_jacobian_upper':[[pack_upper(v) for v in row] for row in maxima],
            'weighted_complete_derivative_remainder_upper':[[pack_upper(v) for v in row] for row in remainder],
            'elapsed_seconds':time.monotonic()-began,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--fields-summary',type=Path,required=True)
    ap.add_argument('--input-root',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--workers',type=int,default=2)
    ap.add_argument('--first-rows-only',type=int,default=0)
    a=ap.parse_args(); ctx.prec=256; began=time.monotonic(); source_identity=digest(Path(__file__))
    if a.out.exists(): raise FileExistsError('Use a fresh output path')
    if digest(a.fields_summary)!=FIELDS_SHA: raise ValueError('Full fixed-centre source summary differs')
    d=json.loads(a.fields_summary.read_text())
    if not d['all_gates'] or d['source_sha256']!=FIELDS_SOURCE or d['original_panels']!=10793:
        raise ValueError('Original completed R88 field producer required')
    checks=exact_check()
    groups=d['groups'] if not a.first_rows_only else [next(g for g in d['groups'] if g['panels']>a.first_rows_only)]
    args=[(g,str(a.input_root),a.first_rows_only) for g in groups]
    out=[]
    with ProcessPoolExecutor(max_workers=a.workers) as pool:
        for g in pool.map(group_compute,args):
            out.append(g)
            print(json.dumps({'event':'actual_dn4_group','cell':g['cell'],'segment':g['segment'],'rows':g['rows'],'complete':g['complete'],'seconds':g['elapsed_seconds']}),flush=True)
    maxima=[[max(point(g['weighted_source_jacobian_upper'][i][j]) for g in out) for j in range(46)] for i in range(92)]
    column_sums=[sum(row,arb(0)).upper() for row in maxima]
    if source_identity!=digest(Path(__file__)): raise RuntimeError('Producer changed during actual run')
    result={'scope':'Actual centre derivative only; no cut or whole-ball contraction claimed',
            'source_sha256':digest(Path(__file__)),'fields_summary_sha256':FIELDS_SHA,
            'schema':'actual-r109-full46-normalized-material-dn4-v2','all_finite_entries_checked':True,'source_normalization':'s/(s+abs(ell)) and ell/(s+abs(ell)) exact endpoint quotients before interval unions','full_material_cover':not a.first_rows_only and len(out)==18 and sum(g['rows'] for g in out)==10793,
            'exact_algebra_checks':checks,'groups':out,
            'norm':'input sum_n (1+n)e^(n/64) sup_x |delta P_n or delta K_n|/V; output sum_m e^(m/64) sup_x |delta N_m|/(c_bg V^2)',
            'global_radial_sup_before_modal_sum':True,'global_complete_source_derivative_operator_upper':pack_upper(max(column_sums)),
            'global_input_column_sums':[[n,c,pack_upper(column_sums[2*i+j])] for i,n in enumerate(MODES) for j,c in enumerate(('P','K'))],
            'elapsed_seconds':time.monotonic()-began}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    b=(json.dumps(result,separators=(',',':'))+'\n').encode()
    if len(b)>1_000_000:
        if a.out.suffix!='.gz': raise ValueError('Complete primary over1MB requires gzip path')
        b=gzip.compress(b,mtime=0)
    elif a.out.suffix=='.gz': b=gzip.compress(b,mtime=0)
    if len(b)>=5_000_000: raise ValueError('Complete output must be under5MB')
    a.out.write_bytes(b)
    print(json.dumps({'event':'actual_dn4_complete','full_material_cover':result['full_material_cover'],'sha256':digest(a.out),'bytes':len(b)}),flush=True)

if __name__=='__main__': main()
