"""Strict two-parameter double-kernel box and complete signed second-order port on the actual smoothed profile."""
import argparse
from collections import ChainMap
import hashlib
import json
import os
from pathlib import Path
import time
from r734_true_dyadic_tail import I,D,HIGH,B,L0,ONE,ZERO,Pause,cut_port,monotone_trans,solve_mode
from r735_paid_tail_beta_envelope import cap_integral,recovered


def exp(x):return monotone_trans(I(x),'exp')


def sym(x):
    t=I(x).norm()
    return I(t.copy_negate(),t)


def checked(path,digest):
    if not path.is_file():raise FileNotFoundError(path.name)
    with path.open('rb') as f:v=hashlib.file_digest(f,'sha256').hexdigest()
    if v!=digest:raise ValueError('Wrong paid object: '+path.name)


class Journal:
    def __init__(self,cfg,limit,prior):
        self.started=time.monotonic();self.limit=limit;self.next=None
        base=Path(os.environ['RUNNER_TEMP'])/'r735-paid';base.mkdir(exist_ok=True)
        self.path=base/'central.jsonl'
        hs=hashlib.sha256()
        for n in ('r734_true_dyadic_tail.py','r735_paid_tail_beta_envelope.py',Path(__file__).name):
            hs.update(Path(__file__).with_name(n).read_bytes())
        hs.update(json.dumps({k:v for k,v in cfg.items() if k not in ('maximum_depth','maximum_head')},sort_keys=True).encode())
        self.fingerprint=hs.hexdigest()
        new={}
        if self.path.exists():
            with self.path.open() as f:
                for row in f:
                    r=json.loads(row)
                    if r['fingerprint']!=self.fingerprint or r['key'] in new or r['key'] in prior:raise ValueError('Wrong R735 receipt.')
                    new[r['key']]=r['value']
        self.new=new;self.records=ChainMap(new,prior);self.out=self.path.open('a',buffering=1)
        self.previous_new_cost=sum(v['seconds'] for v in new.values())
    def once(self,key,fn):
        if key in self.records:return self.records[key]['data']
        self.next=key
        if time.monotonic()-self.started+3>self.limit:raise Pause()
        start=time.monotonic();value=fn()
        rec=dict(data=value,seconds=time.monotonic()-start)
        self.out.write(json.dumps(dict(fingerprint=self.fingerprint,key=key,value=rec),sort_keys=True,
                                  separators=(',',':'),allow_nan=False)+'\n')
        self.new[key]=rec;self.next=None
        return value


def graft(sign,ports,jlist):
    # Log-radius from tail to cone is -sign*tau. A Hermite polynomial in log w
    # interpolates values 0,log(ratio) and slopes r_cut w'/w,1.
    tau=ONE/(2**36)
    for thin in range(24):
        for ratio in (1,2,4,8,16,32):
            allrows={}
            for j in jlist:
                k=j*j;P=ports[j];r=I(*P['r']);fp=I(*P['f_0_1_2'][1]);p=r*fp
                slope=I(*P['w_r'])*r/I(*P['w'])
                if (tau*(I(slope.norm())+1)).hi>D('.5'):break
                # 1/2 <= w/w_cut <= 2 ratio throughout; e^{1/2}<2.
                maximum=I(2*ratio*k*(k-1)+2*k+2)
                err=I(max(D(1),(p-k).norm()))*(exp(maximum*tau)-1)
                f=1+sym(err);v=p-k+sym(err);fy=k*f+v/ratio
                # Good coefficient grows on the return from the graft to the core.
                good=(f-sign*fy/j)/2;bad=(f+sign*fy/j)/2
                if good.distance_from_zero()==0:break
                field_bound=(k+2)*I(max(D(1),(p-k).norm()))*exp(maximum*tau)
                allrows[j]=dict(good=good,bad=bad,cap_max_f_or_fy=field_bound)
            if len(allrows)==len(jlist):return dict(tau=tau,ratio=ratio,mode=allrows)
        tau=tau/4
    raise ArithmeticError('No common thin connector certified all requested nonbad modes.')


def cone_amplitude(gr,j,H,boundary):
    g=gr['mode'][j]['good'];b=gr['mode'][j]['bad']
    t=(b/g)*exp(-2*j*H)
    if (1+t).distance_from_zero()==0:raise ArithmeticError('Head loses its material normalization.')
    a=boundary/(1+t)
    return (a,t*a),a*exp(-j*H)/g,t


def cone_beta(sign,gr,H,amplitudes,wc,rc):
    total=ZERO
    coeff={}
    tail={}
    for j in (2,3):
        (a,b),tail[j],_=cone_amplitude(gr,j,H,amplitudes[j]);coeff[j]={-1:a,1:b}
    for l in (-1,1):
        for m in (-1,1):
            p=sign*2*l;q=sign*3*m
            n=2*l+3*m-3*sign
            integ=I(H) if n==0 else (exp(n*H)-1)/n
            total=total-(p*q-9*p-4*q+12)*coeff[2][l]*coeff[3][m]*integ/(2*wc*rc**2)
    return total,tail


def tail_error(sign,gr,H,tail,wc,rc,W,base_bound):
    # The base mathematical f=1 is normalized on the true tail-side cut, after the connector.
    rcut=B-sign*L0;rt=rc*exp(sign*(I(H)+gr['tau']));rhead=rc*exp(sign*H)
    R=rt/rcut;w_tail=wc*exp(sign*H)/gr['ratio']
    vertical=w_tail/(W*16*L0**4)
    amp=I((tail[2]*tail[3]).norm())
    cap=amp*base_bound/(vertical*R**2)
    rlower=I(min(rt.lo,rhead.lo));wlower=w_tail/2
    grafted=gr['tau']*26*amp*gr['mode'][2]['cap_max_f_or_fy']*gr['mode'][3]['cap_max_f_or_fy']/(2*wlower*rlower**2)
    return cap+grafted


def z2(y):return (4+5*y)/(6*(1+2*y))


def pcore(j,y):return j*j-j*(j-1)*(4-y)/2


def central_state_error(j,slope_error,eps):
    # On the constant-w comparison, the exact matrix T_lambda has norm/inverse <100
    # for j=2,3, and <2000 for fixed j=4,5,6, throughout the whole core.
    k=j*j;K=I(100 if j<=3 else 2000)
    width=eps
    diff=I(2*(4+k*(k-1)))*width
    changed=K*(exp(K**2*diff)-1)
    return K*slope_error+changed*(max(1,k-j)+slope_error)


def certified_box(head,eps,gr,base,W,extra):
    H=I(head);jj=[2,3]+([4,5,6] if extra else [])
    slopes={};state_error={}
    for j in jj:
        for sign in (-1,1):
            _,_,t=cone_amplitude(gr[sign],j,H,ONE)
            slopes[sign,j]=I((2*j*t/(1+t)).norm())
        state_error[j]=central_state_error(j,slopes[-1,j],eps)
    root=(25-monotone_trans(I(145),'sqrt'))/60
    def valid_faces(lo,hi,v):
        Y=I(lo.lo,hi.hi);lam=2/(4-Y);Z=z2(Y)+sym(v);nu=lam*Z
        if lam.lo<=D('.5') or lam.hi>=D('.55') or nu.lo<=D('.26') or nu.hi>=D('.4'):return None
        err={}
        for j in jj:
            f0=1+2*pcore(j,Y);k=j*j;ez=state_error[j];pr=slopes[1,j]
            den=I(f0.distance_from_zero())*lam*(k+j)
            if den.lo<=0:return None
            err[j]=(ez+nu*(pr*I(f0.norm())+(k+j+pr)*ez))/den
        def difference(vv):
            return -(30*vv**2-25*vv+4)/(12*(1+2*vv)*(6*vv-5))
        lower=difference(lo);upper=difference(hi);both=err[2]+err[3]
        if not (v.lo>err[2].hi and lower.lo>both.hi and upper.hi<both.hi.copy_negate()):return None
        if extra:
            for j in (4,5,6):
                p=pcore(j,Y);z=(j*j-3*p/(1+2*p))/(j*(j+1))
                if (z-Z).lo<=err[j].hi:return None
        return dict(y=Y,lam=lam,nu=nu,Z=Z,errors=err)
    checks=[]
    box=valid_faces(I(1)/5,I(11)/50,ONE/20000)
    if box is None:return dict(accepted=False,reason='strict_four_faces_or_requested_nonresonances_fail')
    for power in range(4,19):
        rad=ONE/(10**power)
        smaller=valid_faces(root-rad,root+rad,rad)
        if smaller is None:break
        box=smaller;checks.append(power)
    y,lam,nu=box['y'],box['lam'],box['nu']
    a=pcore(2,y);c=pcore(3,y);f0={2:1+2*a,3:1+2*c}
    # Central comparison integrates the whole constant segment analytically.
    center=-(8+4*y-9*y**2)/(3*lam)
    e=max(state_error[2].hi,state_error[3].hi)
    grad=I(11)*I(e)
    outside_layers=52*(20*grad+grad**2)
    # |(f,v)|<=600+e from the unperturbed propagator bound, and w>=1/4 on these layers.
    large=13*(600+I(e))
    inside_layers=2*eps*26*(2*large**2+100)
    center=center+sym(outside_layers+inside_layers)
    total=center;head_values={};caps={}
    for sign in (-1,1):
        rc=ONE if sign==-1 else I(3);wc=ONE if sign==-1 else nu
        amps={j:ONE if sign==-1 else f0[j]+sym(state_error[j]) for j in (2,3)}
        h,ar=cone_beta(sign,gr[sign],H,amps,wc,rc)
        remainder=tail_error(sign,gr[sign],H,ar,wc,rc,W,base[sign])
        total=total+h+sym(remainder);head_values[str(sign)]=h.bounds();caps[str(sign)]=remainder.bounds()
    ok=total.lo>1
    # On the left central smoothing strip, d(w/sqrt(1+w^2))/dr is the true meridional curvature.
    curvature_change=1/monotone_trans(I(2),'sqrt')-lam/monotone_trans(1+lam**2,'sqrt')
    k_lower=curvature_change/(exp(eps)-1)
    # Include the actual flat rim radii, independently of the still missing closing shell.
    a=(B/(B+L0))*exp(-H-gr[-1]['tau']);b=3*(B/(B-L0))*exp(H+gr[1]['tau'])
    return dict(accepted=ok,reason='finite_true_double_kernel_and_beta' if ok else 'whole_beta_enclosure_not_separated',
        actual_fixed_material_representative='lexicographically least common shooting zero in the certified compact box',
        head_log_length=head,central_log_smoothing_width=eps.bounds(),y_box=y.bounds(),lambda_box=lam.bounds(),
        nu_box=nu.bounds(),whole_beta=total.bounds(),finite_head_signed_terms=head_values,normalized_true_caps_and_connectors=caps,
        actual_central_term=center.bounds(),successively_certified_decimal_box_exponents=checks,
        actual_inner_to_outer_radius=(a/b).bounds(),normalized_meridian_curvature_lower=k_lower.bounds(),
        reach_over_whole_D_necessary_upper=(1/(2*b*k_lower)).bounds(),
        these_normalized_finite_inputs_meet_full_reach=False,
        normalized_shooting_uniform_errors={str(j):v.bounds() for j,v in box['errors'].items()},
        nonresonances_4_5_6=extra,first_and_second_order_tilt_only=True,README_completion_claim=False)

def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'
        or not os.environ.get('GITHUB_RUN_ID','').isdigit()):
        raise SystemExit('Bound public Actions required.')
    ap=argparse.ArgumentParser();ap.add_argument('--geometry',required=True);ap.add_argument('--max-seconds',type=float,required=True)
    args=ap.parse_args();cfg=json.loads(Path(args.geometry).read_bytes())
    tmp=Path(os.environ['RUNNER_TEMP']);hist=cfg['paid_r734']
    journal=tmp/'r735-source-tail.jsonl';terminal=tmp/'r735-source-final.json'
    checked(journal,hist['journal_sha256']);checked(terminal,hist['terminal_sha256'])
    prior_json=json.loads(terminal.read_bytes())
    if prior_json.get('kind') not in ('terminal','paid_partial') or prior_json['source_fingerprint']!=hist['scientific_fingerprint']:
        raise ValueError('Unexpected naturally completed R734 scientific endpoint.')
    baseline=tmp/'r735-paid';baseline.mkdir(exist_ok=True)
    # The administrative downloader verifies the original completed run/job/artifact. Retain
    # the literal source journal and terminal for recovery independently of artifact expiry.
    import shutil
    for k,p in (('r734-original-tail.jsonl',journal),('r734-original-final.json',terminal)):
        dest=baseline/k
        if not dest.exists():shutil.copyfile(p,dest)
        checked(dest,hist['journal_sha256'] if p==journal else hist['terminal_sha256'])
    prior={}
    with journal.open() as f:
        for row in f:
            r=json.loads(row)
            if r['scientific_fingerprint']!=hist['scientific_fingerprint'] or r['key'] in prior:raise ValueError('Invalid source journal.')
            prior[r['key']]=r['value']
    if len(prior)!=prior_json['paid_units']:raise ValueError('Incomplete source journal.')
    W=I(hist['weight']);book=Journal(cfg,args.max_seconds,prior);completed=[];ports={-1:{},1:{}}
    width=D(hist['relative_width']);steps=cfg['maximum_depth'];budget=cfg['maximum_head']
    prior_cost=sum(float(v['seconds']) for v in prior.values())
    try:
        base={}
        for extra in (False,True):
            modes=[2,3] if not extra else [2,3,4,5,6]
            for sign in (-1,1):
                side='outer' if sign==1 else 'inner'
                for j in modes:
                    if j in ports[sign]:continue
                    val=prior_json['completed_modes'].get(side+str(j))
                    if val is None or val.get('kind')!='certified_tail_port':
                        val=solve_mode(j,W,width,steps,book,sign)
                    port=val.get('actual_cut_port')
                    if not port or port.get('normalization')!='f(cut)=1':
                        completed.append(dict(phase='necessary_R734_tail_port',mode=j,side=side,unavailable=val))
                        raise ArithmeticError('A true input line could not be normalized at this declared resolution.')
                    ports[sign][j]=port
                if sign not in base:
                    cb=book.once('base_absolute_beta_'+side,lambda:cap_integral(sign,W,book.records,book))
                    base[sign]=I(*cb['normalized_base_absolute_beta_upper'])
            gr={s:graft(s,ports[s],modes) for s in (-1,1)}
            def graft_id(data):
                return {str(s):dict(ratio=v['ratio'],tau=v['tau'].bounds(),
                        good_and_bad={str(j):[w['good'].bounds(),w['bad'].bounds()] for j,w in v['mode'].items()}) for s,v in data.items()}
            cc=graft_id(gr);gid=hashlib.sha256(json.dumps(cc,sort_keys=True).encode()).hexdigest()[:20]
            answered=None;last=None
            # Width is fixed at each candidate, and the subsequent validated face proof uses that same profile.
            for H in cfg['head_schedule']:
                if H>budget:continue
                for power in cfg['smoothing_exponents']:
                    if power<8:raise ValueError('Declared finite smoothing would exceed the proven positive bounds.')
                    tag=f'finite_certificate_{gid}_H{H}_eps{power}'
                    ans=book.once(tag,lambda:certified_box(H,ONE/(2**power),gr,base,W,extra))
                    last=ans
                    if ans['accepted']:
                        answered=dict(actual=ans,finite_join_choices=cc,source_tail_bounds={str(s):v.bounds() for s,v in base.items()})
                        completed.append(answered)
                        print('R735_CERTIFIED '+json.dumps(answered,sort_keys=True,separators=(',',':')),flush=True)
                        break
                if answered:break
            if not answered:
                completed.append(dict(phase='concrete_central_match',last=last,nonresonant_stage=extra,geometry_unqualified=True))
                break
        kind='terminal'
    except Pause:
        kind='paid_partial'
    except ArithmeticError as exc:
        kind='unclosed';completed.append(dict(reason=str(exc)))
    finally:
        book.out.flush();book.out.close()
    print('R735_FINAL '+json.dumps(dict(kind=kind,actual_results=completed,next_unit=book.next,prior_R734_metadata=hist,
          prior_R734_fingerprint=prior_json['source_fingerprint'],prior_R734_paid_units=len(prior),
          prior_R734_paid_unit_seconds=prior_cost,prior_R734_elapsed=prior_json['current_elapsed_seconds'],
          new_fingerprint=book.fingerprint,total_new_units=len(book.new),previous_new_paid_seconds=book.previous_new_cost,
          current_elapsed_seconds=time.monotonic()-book.started,finite_q_solution=False,README_completion_claim=False),
          sort_keys=True,separators=(',',':'),allow_nan=False),flush=True)


if __name__=='__main__':main()
