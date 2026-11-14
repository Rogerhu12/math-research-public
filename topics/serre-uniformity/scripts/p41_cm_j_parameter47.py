#!/usr/bin/env python3
"""Actual conversion from the fixed CM disc parameters to the global j parameters."""
import argparse,gzip,hashlib,json
from fractions import Fraction
from pathlib import Path
Q=47**4

def read(path):
    b=path.read_bytes();return json.loads(gzip.decompress(b) if path.suffix=='.gz' else b),hashlib.sha256(b).hexdigest()

def mul(a,b):return [(a[0]*b[0]-a[1]*b[1])%Q,(a[0]*b[1]+a[1]*b[0])%Q]
def add(a,b):return [(a[0]+b[0])%Q,(a[1]+b[1])%Q]
def inv(a):
    n=pow((a[0]*a[0]+a[1]*a[1])%Q,-1,Q)
    return [a[0]*n%Q,-a[1]*n%Q]
def dot(a,b):
    s=[0,0]
    for x,y in zip(a,b):s=add(s,mul(x,y))
    return s
def log(u):
    z=(pow(u,46,Q)-1)%Q
    return (z-z*z*pow(2,-1,Q)+z*z*z*pow(3,-1,Q))*pow(46,-1,Q)%Q

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--discs',type=Path)
    p.add_argument('--canonical',type=Path)
    p.add_argument('--cm12',type=Path)
    p.add_argument('--cm7',type=Path)
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_cm_j_parameter47_certificate.json'))
    args=p.parse_args()
    def locate(explicit,name):
        if explicit is not None:return explicit
        target=args.script_dir/'data'/name
        return target if target.exists() else Path('/tmp')/name
    paths=[locate(args.discs,'p41_cm_quadratic_jets47_raw.json.gz'),
           locate(args.canonical,'p41_canonical_restriction47_candidate1_compact.json.gz'),
           args.script_dir/'data/p41_cm3_makdisi47_certificate.json',
           locate(args.cm12,'p41_cm12_hecke47_verified.json.gz'),
           locate(args.cm7,'p41_cm7_q2_support47_verified.json.gz'),
           args.script_dir/'data/p41_formal47_multiplication_saved.json.gz']
    pairs=[read(p) for p in paths];discs,can,b,u,c,formal=[a for a,h in pairs]
    hashes={p.name:h for p,(a,h) in zip(paths,pairs)}
    assert discs['source_sha256']==can['source_sha256']==formal['source_sha256']
    assert all(discs['point_source_sha256'][p.name]==hashes[p.name] for p in paths[2:5])
    fc=[a[0] for a in can['denominator_coefficients']];assert len(fc)==73
    Ws=[b['coarse_evaluation_coefficients'],u['weight2_evaluation_coefficients'],[v[0] for v in c['weight2_evaluation_coefficients']]]
    A,B=-35,-98;D=4*A**3+27*B**2
    jprime=[Fraction(256),Fraction(-118800),Fraction(-6912*A**3*54*B,D**2)]
    assert jprime[2]==Fraction(-170100*105,87808)
    source_parameters=['A^3 on y^2=x^3+A*x+1','source A of the actual CM3-to-CM12 isogeny','B+98 on y^2=x^3-35*x+B']
    records=[]
    for rec,ws,jp,tname in zip(discs['records'][:3],Ws,jprime,source_parameters):
        assert len(ws[0])==len(ws[1])==73
        f0,f1=dot(ws[0],fc),dot(ws[1],fc);fi=inv(f0)
        w0=[mul(x,fi) for x in ws[0]]
        w1=[add(mul(a,fi),mul(mul(x,mul(fi,fi)),[-f1[0]%Q,-f1[1]%Q])) for a,x in zip(ws[1],ws[0])]
        uc=[row[0] for row in rec['parameter_coefficients']]
        t1=dot(w1,uc);assert t1[1]==0 and t1[0]%47
        assert w0==rec['normalized_weight2_coefficients'][0]
        assert w1==[mul(t1,x) for x in rec['normalized_weight2_coefficients'][1]]
        assert dot(rec['normalized_weight2_coefficients'][1],uc)==[1,0]
        assert dot(rec['normalized_weight2_coefficients'][0],fc)==[1,0] and dot(rec['normalized_weight2_coefficients'][1],fc)==[0,0]
        jj=jp.numerator*pow(jp.denominator,-1,Q)%Q;assert jj%47
        alpha=t1[0]*pow(jj,-1,Q)%Q
        records.append({'label':rec['label'],'source_parameter':tname,
                        'j_derivative_in_source_parameter':[jp.numerator,jp.denominator],
                        'local_parameter_derivative_in_source_parameter':t1[0],
                        'dt_over_dj_mod47four':alpha,'dj_over_dt_mod47four':pow(alpha,-1,Q),
                        'log_dt_over_dj_mod47four':log(alpha),
                        'all73_normalized_first_jets_match':True,
                        'normalized_modular_first_jet_sha256':hashlib.sha256(json.dumps(w1,separators=(',',':')).encode()).hexdigest()})
    m=formal['target_multiplier'];ab=records[0]['dt_over_dj_mod47four'];factors={}
    for rec,rp,sb in [(records[1],85,31),(records[2],4,4)]:
        ap=rec['dt_over_dj_mod47four'];value=pow(ap,m*rp,Q)*pow(ab,-m*sb,Q)%Q
        predicted=m*(rp*rec['log_dt_over_dj_mod47four']-sb*records[0]['log_dt_over_dj_mod47four'])%Q
        assert log(value)==predicted
        factors[rec['label']]={'CM_divisor_coefficient':rp,'base_divisor_coefficient':sb,
                              'leading_coefficient_norm_j_over_t':value,'log_factor_mod47four':predicted,
                              'meaning':'parameter-change factor only for the leading-unit product of f_C with div=m(P-b)-A_formal; not a height or a complete collision transport'}
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':discs['source_sha256'],'input_sha256':hashes,
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'records':records,'target_multiplier':m,'F2_leading_norm_parameter_factors':factors,
            'formula':'t=alpha*(j-j(P))+higher; lc_j(f)=alpha^ord_P(f)*lc_t(f)',
            'status':'actual unit parameter conversions at all three CM points; all73 independently modular first jets matched; no nonunit divisions'}
    args.output.write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
    raw=args.output.read_bytes();print('ACTUAL CM J PARAMETER PASS',len(raw),hashlib.sha256(raw).hexdigest())
    print(json.dumps({'records':records,'factors':factors},indent=2))

if __name__=='__main__':main()

