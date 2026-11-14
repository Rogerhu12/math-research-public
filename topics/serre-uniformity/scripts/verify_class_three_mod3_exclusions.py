#!/usr/bin/env python3
"""R93 exact coupled mod-47 / mod-3 Frobenius obstruction.

Standard library only. Rebuilds the local characters from the R91 formulas,
then enumerates GL2(F3) to check the Q8 coset trace restrictions independently.
"""
import hashlib
import itertools
import json
from math import isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parent
ops = runpy.run_path(str(ROOT / 'verify_class_number_three_actual_characters.py'))
power, mul, scale, roots = (ops[k] for k in ['power', 'mul', 'scale', 'field_roots'])


def mm(a, b):
    x, y, z, w = a
    r, s, t, u = b
    return ((x*r+y*t)%3, (x*s+y*u)%3, (z*r+w*t)%3, (z*s+w*u)%3)


def determinant(a):
    return (a[0]*a[3]-a[1]*a[2])%3


def matrix_order(a):
    b = (1,0,0,1)
    for k in range(1,49):
        b = mm(b,a)
        if b == (1,0,0,1):
            return k
    raise AssertionError('Not an invertible matrix')


def matrix_certificate():
    gl = [a for a in itertools.product(range(3),repeat=4) if determinant(a)]
    sl = [a for a in gl if determinant(a)==1]
    identity, minus_identity = (1,0,0,1),(2,0,0,2)
    Q8 = [a for a in sl if a in (identity,minus_identity) or (a[0]+a[3])%3==0]
    assert len(gl)==48 and len(sl)==24 and len(Q8)==8
    assert all(mm(a,b) in Q8 for a in Q8 for b in Q8)
    for g in gl:
        inverse = next(h for h in gl if mm(g,h)==identity)
        assert all(mm(mm(g,h),inverse) in Q8 for h in Q8)
    assert all(matrix_order(a)==4 for a in Q8 if a not in (identity,minus_identity))
    assert all((a[0]+a[3])%3 != 0 for a in sl if a not in Q8)
    # Verify the induced permutation group on the four projective lines and its
    # quotient action on the three partitions into two unordered pairs.
    lines=[(1,0),(0,1),(1,1),(1,2)]
    partitions=[frozenset([frozenset([0,1]),frozenset([2,3])]),
                frozenset([frozenset([0,2]),frozenset([1,3])]),
                frozenset([frozenset([0,3]),frozenset([1,2])])]
    quotient = {}
    for a in gl:
        perm=[]
        for x,y in lines:
            u,v=(a[0]*x+a[1]*y)%3,(a[2]*x+a[3]*y)%3
            if u:
                u,v=1,v*pow(u,-1,3)%3
            else:
                u,v=0,1
            perm.append(lines.index((u,v)))
        p3=tuple(partitions.index(frozenset(frozenset(perm[i] for i in pair)
                                           for pair in part)) for part in partitions)
        quotient[a]=p3
    assert len(set(quotient.values()))==6
    assert [a for a in gl if quotient[a]==(0,1,2)] == Q8
    assert all(quotient[a] in [(1,2,0),(2,0,1)] for a in sl if a not in Q8)
    return {'GL2_order':len(gl),'SL2_order':len(sl),'Q8':Q8,
            'nonidentity_cubic_coset_trace_residues':sorted({(a[0]+a[3])%3 for a in sl if a not in Q8})}


def calculate():
    p,e=47,1476
    specs=[(643,7,27,1,(35,5),31,15,1),
           (907,13,25,3,(25,14),139,60,-2)]
    result=[]
    for D,q0,T0,Y0,c,q,U,V in specs:
        z=-D%p
        assert ops['chi'](D,p)==-1 and ops['chi'](D,q)==1
        assert q%p!=1 and q%3==1
        assert T0*T0+D*Y0*Y0==4*q0**3
        assert U*U+D*V*V==4*q*q0
        r0=-T0*pow(Y0,-1,q0)%q0
        assert (U+V*r0)%q0 and (U-V*r0)%q0==0
        alpha=scale((T0,Y0),pow(2,-1,p),p)
        assert power(c,3,p,z)==power(alpha,e,p,z)
        gamma=scale((U,V),pow(2,-1,p),p)
        nu=scale(mul(power(gamma,e,p,z),c,p,z),pow(pow(q0,4,p),-1,p),p)
        field_solutions=[[a,list(beta)] for a,beta in roots(q,p,z) if power(beta,4,p,z)==nu]
        traces=sorted({a for a,_ in field_solutions})
        is_cube=pow(p,(q-1)//3,q)==1
        mod3_allowed=[a for a in traces
                      if ((a%3==0 or (a-q-1)%9==0 or (a+q+1)%9==0)
                          if is_cube else a%3!=0)]
        assert not mod3_allowed
        result.append({'D':D,'p':p,'e':e,'q0':q0,'T0':T0,'Y0':Y0,
                       'c':c,'q':q,'U':U,'V':V,'nu':nu,
                       'Hasse_bound':isqrt(4*q),'roots':field_solutions,'traces':traces,
                       '47_power_cubic_test':pow(p,(q-1)//3,q),
                       '47_is_cube_mod_q':is_cube,'allowed_after_mod3':mod3_allowed})
    assert result[0]['traces']==[-10,10] and result[0]['nu']==(43,12)
    assert result[1]['traces']==[-12,-6,6,12] and result[1]['nu']==(44,27)
    return {'version':1,'matrix_quotient':matrix_certificate(),'cases':result}


def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    path=ROOT/'data/class_three_mod3_exclusions.json'
    result=calculate()
    normalized=json.loads(json.dumps(result))
    if args.write:
        path.write_text(json.dumps(normalized,indent=2)+'\n')
    assert normalized==json.loads(path.read_text())
    for row in result['cases']:
        print('D',row['D'],'p',row['p'],'q',row['q'],'traces',row['traces'],
              'cubic test',row['47_power_cubic_test'],'survivors',row['allowed_after_mod3'])
    print('Verified exact mod-47 and mod-3 incompatibility for both R91 candidates.')
    print('SHA256',hashlib.sha256(path.read_bytes()).hexdigest())


if __name__=='__main__':
    main()
