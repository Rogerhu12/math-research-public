#!/usr/bin/env python3
"""One deterministic new q from the complete, defining support primary moment.

This reads the accepted raw lambda-.02 finite anchor and the already declared
lambda-one a=.21/bp=.32/bc=.4 endpoint. It does not construct an initializer or
call either solver. The true primary factor includes the flattened base, not
only the zero-primary controls. Widths are decimal-roundtrip rationals; q and
lambda are the exact reals represented by the recorded binary64 values.

Write x=phi-pi/3, T=2*pi/3, I_k=(2/T)*integral chi(x)*cos(k*x) dx over
[0,a+bp], beta=-8*(I_0-I_3)/(1-I_0). The base is
unit_rho=-8*cos(3*phi)+lambda*(8*chi*(1+cos(3*phi))+beta*(1-chi)).
Since h+h''=rho, the signed support cosine coefficient is
Q=2*<h*cos(3*phi)>=q*P, P=1+lambda*((2-beta/4)*I_3-I_0-I_6).
Both the raw columns and the new T/U columns have zero mean and primary
support moment by their defining projections. Thus q_new=q_old*P_old/P_new
is uniquely determined, with no amplitude scan or high-mode power predictor.

High precision evaluates the formula; independent Fraction Taylor bounds
certify P_new>0, q_new>0 and the chosen nearest binary64. The enclosure scope
is these defining scalar moments, not numerical libm/core evaluation, an
initial-guess domain or a BVP/closed-surface certificate.
"""
from fractions import Fraction as F
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import mpmath as mp
from circle_trace_controls import defining_moments

LIBRARY=Path(__file__).with_name('round_raw_lib')
if str(LIBRARY) not in sys.path:sys.path.insert(0,str(LIBRARY))
from moment_interval_bounds import add,neg,scale,mul,divide,pi_interval,sincos,beta_characteristic

EXPECTED_CHECKPOINT_SHA='6f5a973c746e1112f827e5478432b9abe9d14931df90157f2a19381cc670b91e'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def one(value):return value,value


def outward_decimal(interval,digits=40):
    """Decimal endpoints obtained by exact integer floor/ceiling operations."""
    denominator=10**digits
    lo=interval[0]*denominator;hi=interval[1]*denominator
    integers=[lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)]
    def show(value):
        sign='-' if value<0 else '';whole,fraction=divmod(abs(value),denominator)
        return sign+str(whole)+'.'+str(fraction).zfill(digits)
    return list(map(show,integers))


def rational_factor(settings):
    a,b=F(str(settings['halfwidth'])),F(str(settings['transition']))
    lam=F.from_float(float(settings['homotopy']));pi=pi_interval();unit=one(F(1))
    I={0:divide(one(3*(2*a+b)),scale(pi,F(2)))}
    for k in [3,6]:
        si,co=sincos(k*a);re,im=beta_characteristic(k*b)
        I[k]=scale(divide(add(mul(si,re),mul(co,im)),pi),F(3,k))
    beta=scale(divide(add(I[0],neg(I[3])),add(unit,neg(I[0]))),F(-8))
    correction=add(add(mul(add(one(F(2)),scale(beta,F(-1,4))),I[3]),neg(I[0])),neg(I[6]))
    P=add(unit,scale(correction,lam))
    return dict(moments=I,beta=beta,P=P)


def high_precision_factor(settings,precision=90):
    with mp.workdps(precision):
        defining=defining_moments(settings['halfwidth'],settings['transition'],precision+20)
        I={k:mp.mpf(defining['cosine_moments'][str(k)]) for k in [0,3,6]}
        beta=-8*(I[0]-I[3])/(1-I[0])
        lam=mp.mpf(float(settings['homotopy']))
        P=1+lam*((2-beta/4)*I[3]-I[0]-I[6])
        return dict(moments={str(k):mp.nstr(v,precision-10) for k,v in I.items()},
            beta=mp.nstr(beta,precision-10),P=mp.nstr(P,precision-10))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--endpoint-record',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();began=time.monotonic()
    if sha(args.checkpoint)!=EXPECTED_CHECKPOINT_SHA:raise ValueError('Use the declared accepted raw lambda-.02 M16 anchor')
    cp=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    if cp['solver_success'] is not True or cp['config']['modes']!=16 or not cp['config']['fixed_metric']:
        raise ValueError('The complete finite original-gate anchor is required')
    old=cp['core_round_settings'];new=json.loads(args.endpoint_record.read_text())['settings']
    for value in [old,new]:
        if value['center']!=math.pi/3 or value['bimodal_eta']!=0. or value['lock_fundamental'] is not True:
            raise ValueError('The literal pi/3 n3 eta0 locked-primary definition is required')
    if (old['halfwidth'],old['transition'],old['control_transition'],old['homotopy'])!=(.21,.08,.16,.02):
        raise ValueError('The old physical core definition changed')
    if (new['halfwidth'],new['transition'],new['control_transition'],new['homotopy'])!=(.21,.32,.4,1.):
        raise ValueError('The unique predeclared endpoint definition changed')
    qold=float(cp['actual_primary_amplitude']);rq=F.from_float(qold)
    ro,rn=rational_factor(old),rational_factor(new)
    if ro['P'][0]<=0 or rn['P'][0]<=0:raise ArithmeticError('The defining primary factors are not proved positive')
    qexact=scale(divide(ro['P'],rn['P']),rq)
    if qexact[0]<=0:raise ArithmeticError('The matched physical q is not proved positive')
    qnew=float((qexact[0]+qexact[1])/2)
    previous=math.nextafter(qnew,-math.inf);following=math.nextafter(qnew,math.inf)
    rounding_bin=((F.from_float(previous)+F.from_float(qnew))/2,
                  (F.from_float(qnew)+F.from_float(following))/2)
    if not rounding_bin[0]<qexact[0]<=qexact[1]<rounding_bin[1]:
        raise ArithmeticError('The enclosure does not identify a unique nearest binary64 q')
    residual=add(scale(rn['P'],F.from_float(qnew)),neg(scale(ro['P'],rq)))
    ho,hn=high_precision_factor(old),high_precision_factor(new)
    with mp.workdps(90):
        exact_mp=mp.mpf(qold)*mp.mpf(ho['P'])/mp.mpf(hn['P'])
        qtext=mp.nstr(exact_mp,80)
        if float(exact_mp)!=qnew:raise ArithmeticError('High precision and exact rounding enclosure disagree')
        residual_mp=mp.mpf(qnew)*mp.mpf(hn['P'])-mp.mpf(qold)*mp.mpf(ho['P'])
        residual_text=mp.nstr(residual_mp,60)
    source_paths=[Path(__file__),Path(__file__).with_name('circle_trace_controls.py'),
        Path(__file__).with_name('circle_trace_replacement_basis.py'),
        Path(__file__).with_name('circle_trace_replacement_core.py'),
        LIBRARY/'moment_interval_bounds.py',LIBRARY/'large_radius_local_core.py',
        LIBRARY/'complementary_moment_basis.py']
    source_hashes={str(path.resolve()):sha(path) for path in source_paths}
    for name in ['large_radius_local_core.py','complementary_moment_basis.py']:
        path=LIBRARY/name
        if cp['core_round_sources'][str(path.resolve())]!=sha(path):
            raise ValueError('The scalar definition is not the recorded old physical source: '+name)
    result=dict(scope=__doc__,command=sys.argv,source_sha256=source_hashes,
        checkpoint=dict(path=str(args.checkpoint.resolve()),sha256=sha(args.checkpoint),
            gauge_amplitude=cp['gauge_amplitude'],actual_parameter_q=qold,
            finite_solver_success=True,complete_metric=float(cp['summary']['metric_l1']),
            caveat='The previous finite gates passed, but its full prefix metric failed the 1e-6 target.'),
        coefficient_chunks={str(path.resolve()):sha(path) for path in sorted(args.checkpoint.parent.glob('seed_coeff_*.npy.gz'))},
        endpoint_record=dict(path=str(args.endpoint_record.resolve()),sha256=sha(args.endpoint_record)),
        old_settings=old,new_settings=new,
        normalization='Full-circle average <f>=(2*pi)^-1 integral f; signed support cosine coefficient Q=2<h*cos(3*phi)>.',
        local_phase='x=phi-pi/3, so cos(3*phi)=-cos(3*x).',
        scalar_definition='beta=-8*(I0-I3)/(1-I0); P=1+lambda*((2-beta/4)*I3-I0-I6); Q=q*P.',
        width_interpretation='Exact rational decimal roundtrip of a and primary transition; q and lambda are exact recorded binary64 reals.',
        zero_primary_control_scope='All raw mixed columns with lock_fundamental=True, and all R44 T/U endpoint columns, have zero defining mean/primary support moments. No claim that their floating evaluation is exactly moment-zero.',
        old_factor=dict(**ho,rational_P_enclosure=outward_decimal(ro['P']),rational_beta_enclosure=outward_decimal(ro['beta'])),
        new_factor=dict(**hn,rational_P_enclosure=outward_decimal(rn['P']),rational_beta_enclosure=outward_decimal(rn['beta'])),
        matched_q=dict(rule='q_old*P_old/P_new; no search',high_precision=qtext,
            exact_q_enclosure=outward_decimal(qexact),binary64=qnew,binary64_hex=qnew.hex(),
            uniquely_nearest_binary64_proved=True,primary_match_residual_high_precision=residual_text,
            primary_match_residual_enclosure=outward_decimal(residual,60)),
        BVP_solver_invoked=False,actual_tail_solver_invoked=False,initializer_constructed=False,
        limits='New physical q and endpoint control space. This scalar primary match does not preserve the entire core or g, establish rho positivity or match its centre twojet, and does not inherit R38/R40/R41 geometry.',
        seconds=time.monotonic()-began)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),q_new=qnew,
        P_old=ho['P'],P_new=hn['P'],primary_residual=residual_text,seconds=result['seconds'])),flush=True)


if __name__=='__main__':main()
