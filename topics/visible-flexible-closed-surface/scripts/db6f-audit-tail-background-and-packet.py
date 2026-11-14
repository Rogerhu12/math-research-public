#!/usr/bin/env python3
"""Independent rational checks of the conditional background/collar bounds.

No constructor or submitted exact-check module is imported. This checks
exact saved finite endpoint polynomials, not an unknown ODE solution.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import json
from pathlib import Path


def q(x):
    return Q.from_float(float(x))


def show(x):
    return {'exact':str(x),'display':float(x)}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('packet',type=Path)
    a.add_argument('output',type=Path)
    a.add_argument('--rerun',type=Path)
    args=a.parse_args()
    packet=json.loads(args.packet.read_text());p=packet['parameters']
    assert p['orientation']==1 and p['curvatureBound']==6 and p['protectCell']==160
    assert Q(1,200)<=q(p['delta0'])<=Q(1,160)
    assert Q(1,25)<=q(p['etaRatioAtN0'])<=Q(1,16)
    assert q(p['wCut'])==Q(1,2) and q(p['a'])==Q(11,4) and p['R']==64
    assert q(p['rCuff'])>Q(7,50)
    assert 0<q(p['slopeCap'])<=Q(1,49)
    assert len(p['pulseCaps'])<=1 and len(p['valleyCaps'])<=1
    assert len(p['warpWeightLevels'])<=1
    assert p.get('flatOuterThroughCell') is None
    # Uniform root-box width requirements, independent of the tiny actual rounding.
    assert Q(1,25)**2/Q(1,160)>Q(1,4)
    assert Q(1,16)**2/Q(1,200)<1
    # q=2^(-3/2)<3/8 and sqrt(12)>3.
    assert Q(3,8)**2>Q(1,8)
    Y0=6*Q(1,160)+6*Q(1,160)*Q(1,16)/(1-Q(3,8))
    assert Y0<Q(1,20)
    exponent=7*Y0/3
    assert 1/(1-exponent)<Q(6,5)
    # 2^(11/4)>6 and a uniform slope amplitude 1280.
    assert 2**11>6**4
    assert 64*Q(1,2)*Q(6,5)/(6*Q(1,200))==1280
    n=160;W=Q(1280,2**280);eta=Q(1,5000*2**240)
    H=17+Q(7,5)*n
    B=Q(7,2)*Q(15,8)*W*H/(Q(7,50)*eta)+7*W/Q(7,50)
    assert B<Q(66,1000)<Q(1,10)
    guard=7*4*W/Q(7,50)
    assert guard<Q(2,10**79)
    assert Q(6,7)**4>Q(1,2)
    decrease=Q(6,7)*(H+Q(7,5))/H
    assert decrease<1
    assert Q(1,49)/Q(7,50)==Q(50,343)<Q(1,6)
    # Hermite Hessian bound: L/a<=1 and LB<=1 imply sqrt(14^2+27)<15.
    assert 14**2+3*3**2<15**2
    assert Q(9,4)**2>5 and Q(3,2)**2>2
    rows=[]
    for row in packet['rows']:
        L=q(row['r'])-q(row['cuff']);a0=q(row['cuff']);b=q(packet['settings']['assumedBackgroundCurvature'])
        assert 0<L<=a0 and L*b<=1 and b>=6
        norms=[]
        for jet in row['coefficients']:
            total=Q(0)
            for coef in jet:
                m=coef['frequency'];assert isinstance(m,int) and m>=0
                total+=(1+m)**2*sum((abs(q(x)) for x in coef['cos']+coef['sin']),Q(0))
                if packet['settings']['symmetry']=='c3':
                    assert coef['sin'][0]==coef['cos'][1]==coef['sin'][2]==0
                    if m%3==0:assert coef['cos'][0]==coef['sin'][1]==0
                    else:
                        assert coef['cos'][2]==0
                        assert q(coef['cos'][0])==(1 if m%3==1 else -1)*q(coef['sin'][1])
            norms.append(total)
        k=norms[0]/L**2+norms[1]/L+norms[2]
        e1=Q(9,4)*L*k;e2=15*k
        assert e1<1
        eg=2*e1+e1**2
        ed=Q(3,2)*b*e2+e2**2/2+b*b*eg
        curvature=(b+e2)/(1-e1)**2
        rows.append({'rawNode':row['rawNode'],'K':show(k),'metric':show(eg),'tensor':show(ed),'curvature':show(curvature)})
    replay=None
    if args.rerun:
        r=json.loads(args.rerun.read_text())
        assert r['inputSHA256']==packet['inputSHA256']
        assert r['settings']==packet['settings']
        byn={z['rawNode']:z for z in packet['rows']}
        for z in r['rows']:
            old=byn[z['rawNode']]
            for key in ('r','cuff','coefficients','projectionChangeNorm','endpointDiagnostics'):
                assert old[key]==z[key],(z['rawNode'],key)
        replay={'input':str(args.rerun),'sha256':sha(args.rerun),'nodes':[z['rawNode'] for z in r['rows']],
                'exact_equal':True}
    out={'status':'PASS conditional rational bounds and finite polynomial packet',
         'scope':'Does not prove continuous ODE endpoint errors, full exterior matching, or an infinite nonlinear tail.',
         'packet':str(args.packet),'packet_sha256':sha(args.packet),'script_sha256':sha(__file__),
         'uniform_background':{'Y0_upper':show(Y0),'W160_upper':show(W),'B160_upper':show(B),
                               'protection_port_upper':show(guard),'successive_B_term_ratio_upper':show(decrease),
                               'slope_cap_exact':show(q(p['slopeCap']))},'rows':rows,'independent_rerun':replay}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'B160_upper':float(B),'rows':[
        {'node':z['rawNode'],'K':z['K']['display'],'metric':z['metric']['display'],'tensor':z['tensor']['display']} for z in rows],
        'independent_rerun':replay},indent=2))


if __name__=='__main__':main()
