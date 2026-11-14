#!/usr/bin/env python3
"""Exact moduli inventory of X_ns^+(41)(F_47), for local QC input.

This gives Frobenius classes and numbers of coarse points. It does not
replace actual torsion coordinates, Poincare evaluations, or QC functions.
"""
import hashlib
import json
from pathlib import Path

LEVEL, AUXILIARY = 41, 47


def legendre(a, p):
    return 0 if a % p == 0 else (1 if pow(a % p, (p-1)//2, p) == 1 else -1)


def multiply(A, B):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%41,(a*f+b*h)%41,(c*e+d*g)%41,(c*f+d*h)%41)


def matrix_order(A):
    value=(1,0,0,1)
    for n in range(1,1681):
        value=multiply(value,A)
        if value==(1,0,0,1):return n
    raise AssertionError('semisimple Frobenius order')


def inventory():
    records=[]
    for j in range(AUXILIARY):
        if j==0:a,b=0,1
        elif j==1728%AUXILIARY:a,b=1,0
        else:
            k=j*pow((1728-j)%AUXILIARY,-1,AUXILIARY)%AUXILIARY
            a,b=3*k%AUXILIARY,2*k%AUXILIARY
        assert (4*a**3+27*b*b)%AUXILIARY
        actual_j=1728*4*a**3*pow((4*a**3+27*b*b)%AUXILIARY,-1,AUXILIARY)%AUXILIARY
        assert actual_j==j
        trace=-sum(legendre(x*x*x+a*x+b,AUXILIARY) for x in range(AUXILIARY))
        discriminant=(trace*trace-4*AUXILIARY)%LEVEL
        assert discriminant!=0
        frobenius=(0,(-AUXILIARY)%LEVEL,1,trace%LEVEL)
        if trace==0:
            assert legendre(discriminant,LEVEL)==-1
            count=22
        else:count=int(legendre(discriminant,LEVEL)==-1)
        if j in (0,1728%AUXILIARY):assert trace==0
        records.append({'j':j,'curve_A':a,'curve_B':b,'elliptic_frobenius_trace':trace,
                        'frobenius_discriminant_mod41':discriminant,
                        'abstract_frobenius_companion':list(frobenius),
                        'full_41_torsion_residue_degree':matrix_order(frobenius),
                        'coarse_F47_points':count})
    assert sum(r['coarse_F47_points'] for r in records)==129
    assert sum(r['coarse_F47_points']==22 for r in records)==5
    assert sum(r['coarse_F47_points']==1 for r in records)==19
    assert all(r['full_41_torsion_residue_degree']==80 for r in records if r['elliptic_frobenius_trace']==0)
    return {'level':41,'auxiliary_prime':47,'number_of_residue_discs':129,
            'rational_cusps':0,'modular_hecke_trace_check':-81,'fibres':records}


if __name__=='__main__':
    p=Path(__file__).with_name('data')/'p41_residue47_inventory.json'
    p.write_text(json.dumps(inventory(),sort_keys=True,separators=(',',':'))+'\n')
    print('129 exact coarse residue points: five fibres of size22 and nineteen fibres of size1.')
    print('SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
